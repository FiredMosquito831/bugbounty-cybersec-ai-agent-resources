"""Build the structured dataset used by the static knowledge-base site.

Reads the raw research artefacts in `repertoire/` and emits JSON into `data/`:

  sources.json     1,216 catalogued resources (title, URL, description, collection)
  collections.json 19 research collections with counts
  papers.json      17 downloaded papers with metadata
  repos.json       36 reference repositories from the manifest
  taxonomy.json    OWASP classes, vulnerability classes, tooling categories
  blueprint.json   architecture insights parsed from the context document

The script is deterministic and dependency-free (stdlib only).
"""
from __future__ import annotations

import hashlib
import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REP = ROOT / "repertoire"
OUT = ROOT / "data"

# Human names and one-line scopes for the 19 research batches.
COLLECTIONS: dict[str, tuple[str, str]] = {
    "EXHAUSTIVE RESEARCH REPORT: Automated Dependency Confusion Attacks, Typosquatting Detection, and CI/CD Pipeline Compromise Techniques": (
        "Dependency Confusion & CI/CD",
        "Package-registry confusion, typosquatting detection and compromise of build pipelines.",
    ),
    "MOBILE PENTESTING RESEARCH: DECOMPILATION, SSL PINNING BYPASS & RUNTIME MANIPULATION": (
        "Mobile Pentesting",
        "Android/iOS decompilation, SSL pinning bypass and runtime instrumentation.",
    ),
    "Deep Research Agent 6: GraphQL & API Security Automation": (
        "GraphQL & API Security",
        "Introspection abuse, authorization testing and automated API security workflows.",
    ),
    "Web3 & Smart Contract Vulnerability Research — Comprehensive Source Catalog": (
        "Web3 & Smart Contracts",
        "Reentrancy, oracle manipulation, MEV and smart-contract analysis tooling.",
    ),
    "Deep Research Agent 11: Cloud IAM Privilege Escalation & Multi-Account Attack Path Detection": (
        "Cloud IAM & Attack Paths",
        "Cross-account privilege escalation and attack-path analysis in AWS, Azure and GCP.",
    ),
    "OAuth/OIDC & SSO Exploitation: Exhaustive Research Source Compilation": (
        "OAuth, OIDC & SSO",
        "Redirect-URI abuse, token theft, PKCE weaknesses and single-sign-on bypasses.",
    ),
    "DEEP RESEARCH REPORT: LLM Attack Surfaces & Automated Exploitation": (
        "LLM Attack Surfaces",
        "Prompt injection, tool poisoning and automated exploitation of LLM agents.",
    ),
    "Deep Research Report: Machine Learning Approaches for Automated Vulnerability Discovery": (
        "ML for Vulnerability Discovery",
        "Learning-based bug finding, fuzzing and program-analysis research.",
    ),
    "Research Agent 9: Container Escape Detection, Kubernetes Privilege Escalation, and Cluster Misconfiguration Exploitation": (
        "Container Escape & Kubernetes",
        "Container escapes, cluster privilege escalation and misconfiguration exploitation.",
    ),
    "**COMPREHENSIVE SOURCE REPOSITORY: LLM SECURITY & PROMPT INJECTION**": (
        "LLM Security & Prompt Injection",
        "Defences, benchmarks and red-teaming material for language-model systems.",
    ),
    "COMPREHENSIVE RESEARCH SOURCES: AI-DRIVEN VULNERABILITY DISCOVERY & FUZZING": (
        "AI-Driven Fuzzing",
        "LLM-guided fuzzer synthesis, harness generation and symbolic execution.",
    ),
    "Deep Research Agent 10: Cloud Security Misconfiguration at Scale": (
        "Cloud Misconfiguration at Scale",
        "Detecting and exploiting misconfigured cloud services across large estates.",
    ),
    "**CONTAINER & KUBERNETES SECURITY POSTURE — EXHAUSTIVE RESEARCH COMPILATION**": (
        "Container & Kubernetes Posture",
        "Hardening, runtime security and posture management for cloud-native workloads.",
    ),
    "METHODOLOGIES & FRAMEWORKS (15 sources)": (
        "Methodologies & Frameworks",
        "PTES, OWASP WSTG/ASVS, NIST, MITRE ATT&CK and adjacent standards.",
    ),
    "Research Compilation: OAuth Token Fishing, Authorization Code Injection & SSO Bypass": (
        "OAuth Token Attacks & SSO Bypass",
        "Token interception, authorization-code injection and SSO trust abuse.",
    ),
    "COMPREHENSIVE RESEARCH FINDINGS: WIRELESS & IoT PROTOCOL EXPLOITATION": (
        "Wireless, Bluetooth & IoT",
        "Wi-Fi, BLE, RF and embedded-device protocol research.",
    ),
    "I. GraphQL Introspection Attacks & Reconnaissance": (
        "GraphQL Reconnaissance",
        "Introspection as a discovery channel and GraphQL-specific reconnaissance.",
    ),
    "**COMPREHENSIVE RESEARCH: MOBILE APP REVERSE ENGINEERING AUTOMATION**": (
        "Mobile Reverse Engineering",
        "Automated APK/IPA analysis, hooking frameworks and obfuscation handling.",
    ),
    "SUPPLY CHAIN & DEPENDENCY VULNERABILITY AUTOMATION: COMPREHENSIVE RESEARCH": (
        "Supply Chain & Dependencies",
        "Dependency scanning, SBOM analysis and software-supply-chain attack paths.",
    ),
}

GENERIC_TITLE_RE = re.compile(
    r"^(exhaustive|comprehensive|deep research|research|methodologies|complete|full)\b", re.IGNORECASE
)
LEADING_NUMBER_RE = re.compile(r"^\s*(?:[IVXLC]+\.|[0-9]+(?:\.[0-9]+)*(?:[.)])?)\s+")
MARKDOWN_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)\s]*)\)")
GITHUB_RE = re.compile(r"^https?://(?:www\.)?github\.com/([^/]+)/([^/#?]+)", re.IGNORECASE)
ARXIV_RE = re.compile(r"^https?://(?:www\.)?arxiv\.org/(?:abs|pdf)/([^/?#]+)", re.IGNORECASE)


def clean(text: str) -> str:
    text = text.replace("�", "—")
    text = html.unescape(text)
    text = text.replace("**", "").replace("__", "")
    text = MARKDOWN_LINK_RE.sub(r"\1", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip(" \t—-")


def slug(text: str) -> str:
    text = clean(text).lower()
    text = re.sub(r"[^a-z0-9]+", "-", text).strip("-")
    return text or "untitled"


def title_from_url(url: str) -> str:
    github = GITHUB_RE.match(url)
    if github:
        return f"{github.group(1)}/{github.group(2)}"
    arxiv = ARXIV_RE.match(url)
    if arxiv:
        return f"arXiv:{arxiv.group(1)}"
    without_scheme = re.sub(r"^https?://", "", url)
    host, _, path = without_scheme.partition("/")
    host = host.removeprefix("www.")
    tail = unquote(path).rstrip("/").split("/")[-1]
    tail = re.sub(r"\.(html?|php|aspx?|pdf|md)$", "", tail)
    tail = tail.replace("-", " ").replace("_", " ").strip()
    if tail and not tail.isdigit():
        return f"{tail} — {host}"
    return host


def unquote(text: str) -> str:
    from urllib.parse import unquote as _u

    return _u(text)


def display_title(raw: str, url: str, collection_header: str) -> str:
    title = clean(raw)
    if title and title.lower().startswith("url:"):
        title = title[4:].strip()
    if title:
        title = LEADING_NUMBER_RE.sub("", title)
    generic = (
        not title
        or title.isdigit()
        or len(title) < 3
        or title.lower() == collection_header.lower()
        or GENERIC_TITLE_RE.match(title) is not None
    )
    if generic:
        return title_from_url(url)
    return title


def load_collections() -> list[dict]:
    rows = []
    for header, (name, description) in COLLECTIONS.items():
        rows.append({"id": slug(name), "name": name, "description": description, "source": header})
    return rows


def build_sources(known_headers: list[str]) -> tuple[list[dict], list[dict]]:
    tsv = REP / "_new_sources_full.tsv"
    if not tsv.exists():
        raise SystemExit(f"missing dataset: {tsv}")
    by_header = {h: COLLECTIONS[h] for h in COLLECTIONS}
    unknown = set()
    sources: list[dict] = []
    for lineno, line in enumerate(tsv.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
        if not line.strip():
            continue
        parts = line.split("\t")
        if len(parts) < 5:
            raise SystemExit(f"{tsv.name}:{lineno}: expected 5 columns, got {len(parts)}")
        _, header, raw_title, url, description = parts[:5]
        header = header.replace("�", "—").strip()
        if header not in by_header:
            unknown.add(header)
            continue
        name, _ = by_header[header]
        url = url.strip()
        if not url.startswith(("http://", "https://")):
            raise SystemExit(f"{tsv.name}:{lineno}: invalid URL {url!r}")
        title = display_title(raw_title, url, header)
        description = clean(description)
        host = re.sub(r"^https?://", "", url).split("/")[0].removeprefix("www.")
        sources.append(
            {
                "id": hashlib.sha1(url.encode()).hexdigest()[:12],
                "title": title,
                "url": url,
                "host": host,
                "description": description,
                "has_description": bool(description),
                "collection": slug(name),
                "collection_name": name,
                "source_report": header,
            }
        )
    if unknown:
        raise SystemExit("unmapped collection headers:\n" + "\n".join(sorted(unknown)))
    sources.sort(key=lambda s: (s["collection_name"], s["title"].lower()))
    counts: dict[str, int] = {}
    for source in sources:
        counts[source["collection"]] = counts.get(source["collection"], 0) + 1
    collections = load_collections()
    for collection in collections:
        collection["count"] = counts.get(collection["id"], 0)
    collections.sort(key=lambda c: (-c["count"], c["name"]))
    return sources, collections


def build_papers() -> list[dict]:
    index = (REP / "00_REPERTOIRE_INDEX.md").read_text(encoding="utf-8")
    papers: dict[str, dict] = {}
    row_re = re.compile(r"^\| `([^`]+\.(?:pdf|html))` \| (.+?) \| (.+?) \| (.+?) \|$", re.MULTILINE)
    for match in row_re.finditer(index):
        filename, title, source, description = (clean(part) for part in match.groups())
        path = REP / "01_papers" / filename
        if not path.exists():
            raise SystemExit(f"paper listed in index but missing on disk: {filename}")
        link = MARKDOWN_LINK_RE.search(match.group(3))
        source_url = link.group(2) if link else ""
        source_label = link.group(1) if link else source
        kind = "HTML" if filename.endswith(".html") else "PDF"
        is_anchor = "★★★★★" in description
        description = re.sub(r"★★★★★\s*anchor\.", "", description)
        description = re.sub(r"\s*★+\s*", " ", description).strip()
        papers[filename] = {
            "file": filename,
            "title": title,
            "source_url": source_url,
            "source_label": source_label,
            "description": description,
            "kind": kind,
            "anchor": is_anchor,
            "local_path": f"papers/{filename}",
            "slug": slug(Path(filename).stem),
        }
    files = {p.name for p in (REP / "01_papers").iterdir() if p.suffix in (".pdf", ".html")}
    missing = files - set(papers)
    if missing:
        raise SystemExit("paper files without metadata:\n" + "\n".join(sorted(missing)))

    # Merge duplicate copies (same paper, different file) under one entry.
    def work_key(paper: dict) -> str:
        url = paper.get("source_url", "")
        arxiv = ARXIV_RE.match(url)
        if arxiv:
            return "arxiv:" + re.sub(r"v\d+$", "", arxiv.group(1))
        return url or f"file:{paper['file']}"

    groups: dict[str, list[dict]] = {}
    for paper in papers.values():
        groups.setdefault(work_key(paper), []).append(paper)

    merged: list[dict] = []
    for group in groups.values():
        def rank(paper: dict) -> tuple:
            placeholder = paper["title"].startswith("(") or paper["description"].lower().startswith(
                ("same as", "duplicate of")
            )
            return (placeholder, -len(paper["description"]), paper["file"])

        group.sort(key=rank)
        primary = dict(group[0])
        primary["alternates"] = [
            {"file": other["file"], "note": other["description"] or "alternate copy"}
            for other in group[1:]
        ]
        merged.append(primary)

    return sorted(merged, key=lambda p: (not p["anchor"], p["title"].lower()))


def build_repos() -> list[dict]:
    manifest = (REP / "REPO_MANIFEST.md").read_text(encoding="utf-8")
    row_re = re.compile(r"^\| `(03_repos/[^`]+)` \| (\S+) \| (.+?) \| (.+?) \|$", re.MULTILINE)
    repos = []
    for match in row_re.finditer(manifest):
        directory, url, stars, description = (part.strip() for part in match.groups())
        name = directory.split("/", 1)[1]
        stars_value = int(stars) if stars.isdigit() else None
        category = classify_repo(name, description)
        repos.append(
            {
                "dir": directory,
                "name": name,
                "url": url,
                "stars": stars_value,
                "description": clean(description),
                "category": category,
            }
        )
    if not repos:
        raise SystemExit("no repositories parsed from manifest")
    return sorted(repos, key=lambda r: (-(r["stars"] or 0), r["name"].lower()))


def classify_repo(name: str, description: str) -> str:
    haystack = f"{name} {description}".lower()
    if "owasp" in haystack:
        return "OWASP & standards"
    if "claude" in haystack or "skill" in haystack or "agent" in haystack:
        return "Claude Code & agents"
    if any(word in haystack for word in ("awesome", "resources", "roadmap", "methodology", "guide", "cheatsheet", "wiki")):
        return "Learning & methodology"
    if any(word in haystack for word in ("pentest", "toolkit", "scanner", "framework", "fuzz", "payload")):
        return "Toolkits & frameworks"
    return "Toolkits & frameworks"


def build_taxonomy() -> dict:
    context = (REP / "AUTONOMOUS_AGENT_CONTEXT.md").read_text(encoding="utf-8")

    def section(start: str, end: str) -> str:
        a = context.find(start)
        b = context.find(end, a + len(start))
        if a == -1 or b == -1:
            raise SystemExit(f"taxonomy section not found: {start!r}")
        return context[a:b]

    owasp_block = section("### OWASP Top 10 (2021)", "### OWASP Top 10:2025 Changes")
    owasp = []
    for line in owasp_block.splitlines():
        m = re.match(r"^\d+\. \*\*(A\d+): ([^*]+)\*\* — (.+)$", line.strip())
        if m:
            owasp.append({"code": m.group(1), "name": clean(m.group(2)), "detail": clean(m.group(3))})

    changes_block = section("### OWASP Top 10:2025 Changes", "### OWASP API Top 10 (2023)")
    changes = [clean(line.lstrip("- ")) for line in changes_block.splitlines() if line.strip().startswith("- ")]

    api_block = section("### OWASP API Top 10 (2023)", "### Additional Classes")
    api_line = next((line for line in api_block.splitlines() if line.strip().startswith("- API1:")), "")
    api = [part.strip() for part in api_line.lstrip("- ").split(",") if part.strip()]

    classes_block = section("### Additional Classes", "## Tooling Taxonomy")
    classes = []
    for line in classes_block.splitlines():
        m = re.match(r"^- \*\*(.+?)\*\* — (.+)$", line.strip())
        if m:
            classes.append({"name": clean(m.group(1)), "detail": clean(m.group(2))})

    tools_block = section("## Tooling Taxonomy", "## Methodology Stack")
    tools = []
    current = None
    for line in tools_block.splitlines():
        heading = re.match(r"^### (.+)$", line.strip())
        if heading:
            current = {"name": clean(heading.group(1)), "tools": [], "_text": []}
            tools.append(current)
        elif current is not None:
            current["_text"].append(line)
            if line.strip().startswith(("`", "- ", "* ")):
                items = re.findall(r"`([^`]+)`", line)
                if not items:
                    items = [clean(line.lstrip("-* "))]
                current["tools"].extend(i for i in items if i)

    for group in tools:
        if not group["tools"]:
            text = " ".join(group["_text"])
            group["tools"] = [t for t in re.findall(r"`([^`]+)`", text) if t]
        group.pop("_text", None)

    if not (owasp and classes and tools):
        raise SystemExit("taxonomy parsing produced empty sections")
    return {
        "owasp_top10_2021": owasp,
        "owasp_2025_changes": changes,
        "owasp_api_top10": api,
        "vulnerability_classes": classes,
        "tooling": tools,
    }


def build_blueprint() -> dict:
    context = (REP / "AUTONOMOUS_AGENT_CONTEXT.md").read_text(encoding="utf-8")
    start = context.find("## Key Architecture Insights")
    end = context.find("## The Claude Code Bug Bounty Ecosystem", start)
    if start == -1 or end == -1:
        raise SystemExit("architecture insights section not found")
    block = context[start:end]
    items = []
    for chunk in re.split(r"^### ", block, flags=re.MULTILINE)[1:]:
        lines = chunk.splitlines()
        heading = clean(lines[0])
        m = re.match(r"^(\d+)\. (.+?)(?: \(.+\))?$", heading)
        number = int(m.group(1)) if m else len(items) + 1
        title = clean(m.group(2)) if m else heading
        finding = why = how = ""
        for line in lines[1:]:
            fm = re.match(r"^- \*\*Finding:\*\* (.+)$", line.strip())
            wm = re.match(r"^- \*\*Why it matters:\*\* (.+)$", line.strip())
            hm = re.match(r"^- \*\*How to apply:\*\* (.+)$", line.strip())
            if fm:
                finding = clean(fm.group(1))
            elif wm:
                why = clean(wm.group(1))
            elif hm:
                how = clean(hm.group(1))
        if finding or why or how:
            items.append({"number": number, "title": title, "finding": finding, "why": why, "how": how})
    if not items:
        raise SystemExit("no architecture insights parsed")
    return {
        "insights": items,
        "phases": [
            {"phase": 1, "name": "Research & curation", "status": "complete", "detail": "This archive: sources, papers, repositories and taxonomies."},
            {"phase": 2, "name": "Architecture design", "status": "next", "detail": "Agent roles, model routing, tool interface, scope enforcement and evidence capture."},
            {"phase": 3, "name": "Agent implementation", "status": "planned", "detail": "Recon, analysis, validation and reporting stages with deterministic guardrails."},
            {"phase": 4, "name": "Testing & iteration", "status": "planned", "detail": "Benchmarks against known targets, ablation studies and regression suites."},
        ],
    }


def main() -> None:
    OUT.mkdir(exist_ok=True)
    sources, collections = build_sources(list(COLLECTIONS))
    papers = build_papers()
    repos = build_repos()
    taxonomy = build_taxonomy()
    blueprint = build_blueprint()
    datasets = {
        "sources.json": sources,
        "collections.json": collections,
        "papers.json": papers,
        "repos.json": repos,
        "taxonomy.json": taxonomy,
        "blueprint.json": blueprint,
    }
    for name, payload in datasets.items():
        (OUT / name).write_text(json.dumps(payload, ensure_ascii=False, indent=1), encoding="utf-8")

    unique_hosts = len({s["host"] for s in sources})
    print(f"sources      {len(sources):>5}  ({unique_hosts} hosts, {sum(s['has_description'] for s in sources)} with descriptions)")
    print(f"collections  {len(collections):>5}")
    print(f"papers       {len(papers):>5}")
    print(f"repos        {len(repos):>5}  ({sum(r['stars'] or 0 for r in repos):,} combined stars)")
    print(f"taxonomy     {len(taxonomy['vulnerability_classes']):>5} classes, {len(taxonomy['tooling'])} tooling groups")
    print(f"blueprint    {len(blueprint['insights']):>5} insights")


if __name__ == "__main__":
    main()
