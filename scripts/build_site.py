"""Render the static knowledge-base site from data/ into docs/.

Usage: python scripts/build_site.py
The output is plain HTML/CSS/JS suitable for GitHub Pages.
"""
from __future__ import annotations

import json
import shutil
from datetime import datetime, timezone
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs"
SITE = ROOT / "site"
PAPERS = ROOT / "repertoire" / "01_papers"

SITE_URL = "https://bugbounty.danubelabs.net"
SITE_NAME = "Bounty Atlas"
SITE_TAGLINE = "Research atlas for autonomous vulnerability discovery"
GITHUB_URL = "https://github.com/FiredMosquito831/bugbounty-cybersec-ai-agent-resources"

NAV = [
    ("library.html", "Library"),
    ("collections.html", "Collections"),
    ("papers.html", "Papers"),
    ("repos.html", "Repositories"),
    ("taxonomy.html", "Taxonomy"),
    ("blueprint.html", "Blueprint"),
    ("about.html", "About"),
]

env = Environment(
    loader=FileSystemLoader(SITE / "templates"),
    autoescape=select_autoescape(["html"]),
    trim_blocks=True,
    lstrip_blocks=True,
)


def number(value: int | float | None) -> str:
    return f"{int(value or 0):,}"


env.filters["num"] = number


def load(name: str):
    path = DATA / name
    if not path.exists():
        raise SystemExit(f"missing dataset {path}; run scripts/build_data.py first")
    return json.loads(path.read_text(encoding="utf-8"))


def render(out_name: str, template: str, **context) -> None:
    template_obj = env.get_template(template)
    page = {
        "site_name": SITE_NAME,
        "tagline": SITE_TAGLINE,
        "site_url": SITE_URL,
        "github_url": GITHUB_URL,
        "nav": NAV,
        "current": out_name,
        "year": datetime.now(timezone.utc).year,
        **context,
    }
    html = template_obj.render(**page)
    target = DOCS / out_name
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(html, encoding="utf-8")
    print(f"  {out_name:<20} {len(html) / 1024:6.1f} kB")


def main() -> None:
    sources = load("sources.json")
    collections = load("collections.json")
    papers = load("papers.json")
    repos = load("repos.json")
    taxonomy = load("taxonomy.json")
    blueprint = load("blueprint.json")

    stats = {
        "sources": len(sources),
        "hosts": len({s["host"] for s in sources}),
        "described": sum(1 for s in sources if s["has_description"]),
        "collections": len(collections),
        "papers": len(papers),
        "anchors": sum(1 for p in papers if p["anchor"]),
        "repos": len(repos),
        "repo_stars": sum(r["stars"] or 0 for r in repos),
        "classes": len(taxonomy["vulnerability_classes"]),
        "tool_groups": len(taxonomy["tooling"]),
        "tools": sum(len(group["tools"]) for group in taxonomy["tooling"]),
        "insights": len(blueprint["insights"]),
    }
    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    generated = f"v{version}"

    DOCS.mkdir(exist_ok=True)
    print("Rendering pages:")
    render("index.html", "index.html", title="Autonomous bug-bounty research atlas",
           description="A curated, indexed research atlas for building an autonomous bug-bounty and vulnerability-discovery agent: "
                       f"{number(stats['sources'])} sources, {stats['papers']} papers, {stats['repos']} repositories and a full taxonomy.",
           stats=stats, collections=collections[:6], papers=papers, blueprint=blueprint,
           generated=generated, canonical=f"{SITE_URL}/")
    render("library.html", "library.html", title="Source library",
           description=f"Search and filter {number(stats['sources'])} curated security sources across {stats['collections']} research collections.",
           stats=stats, collections=collections, generated=generated,
           canonical=f"{SITE_URL}/library.html")
    render("collections.html", "collections.html", title="Research collections",
           description=f"{stats['collections']} research collections covering cloud, LLM security, mobile, Web3, supply chain and more.",
           stats=stats, collections=collections, generated=generated,
           canonical=f"{SITE_URL}/collections.html")
    render("papers.html", "papers.html", title="Papers",
           description=f"{stats['papers']} downloaded papers on autonomous agents, LLM fuzzing, prompt-injection defence and vulnerability discovery.",
           stats=stats, papers=papers, generated=generated, canonical=f"{SITE_URL}/papers.html")
    render("repos.html", "repos.html", title="Repositories",
           description=f"{stats['repos']} reference repositories ({number(stats['repo_stars'])} combined stars) for security agents and tooling.",
           stats=stats, repos=repos, generated=generated, canonical=f"{SITE_URL}/repos.html")
    render("taxonomy.html", "taxonomy.html", title="Taxonomy",
           description="OWASP Top 10, additional vulnerability classes and a tooling taxonomy for security agents.",
           stats=stats, taxonomy=taxonomy, generated=generated, canonical=f"{SITE_URL}/taxonomy.html")
    render("blueprint.html", "blueprint.html", title="Agent blueprint",
           description="Architecture insights for an autonomous vulnerability-discovery agent, drawn from verified research.",
           stats=stats, blueprint=blueprint, generated=generated, canonical=f"{SITE_URL}/blueprint.html")
    render("about.html", "about.html", title="About this atlas",
           description="Provenance, methodology, scope and responsible-use policy for this research archive.",
           stats=stats, blueprint=blueprint, generated=generated, canonical=f"{SITE_URL}/about.html")
    render("404.html", "404.html", title="Page not found",
           description="Page not found.", stats=stats, generated=generated, canonical=f"{SITE_URL}/404.html")

    # Assets
    assets = DOCS / "assets"
    if assets.exists():
        shutil.rmtree(assets)
    shutil.copytree(SITE / "static", assets)
    print(f"  assets/              copied")

    # Papers (self-contained site)
    papers_dir = DOCS / "papers"
    papers_dir.mkdir(exist_ok=True)
    copied = 0
    paper_files = sorted(f for f in PAPERS.iterdir() if f.suffix in (".pdf", ".html"))
    for source in paper_files:
        target = papers_dir / source.name
        if not target.exists() or target.stat().st_size != source.stat().st_size:
            shutil.copy2(source, target)
            copied += 1
    print(f"  papers/              {len(paper_files)} files ({copied} copied)")

    # Library dataset for client-side search
    library_dir = DOCS / "data"
    library_dir.mkdir(exist_ok=True)
    library = [
        {
            "id": s["id"],
            "t": s["title"],
            "u": s["url"],
            "h": s["host"],
            "d": s["description"],
            "c": s["collection"],
            "cn": s["collection_name"],
        }
        for s in sources
    ]
    (library_dir / "library.json").write_text(
        json.dumps(library, ensure_ascii=False, separators=(",", ":")), encoding="utf-8"
    )
    print(f"  data/library.json    {len(library)} rows")

    # sitemap / robots / CNAME
    urls = ["/", "/library.html", "/collections.html", "/papers.html", "/repos.html", "/taxonomy.html", "/blueprint.html", "/about.html"]
    sitemap = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    priorities = {"": "1.0", "/library.html": "0.9", "/papers.html": "0.8", "/collections.html": "0.8",
                  "/repos.html": "0.7", "/taxonomy.html": "0.7", "/blueprint.html": "0.6", "/about.html": "0.5"}
    for url in urls:
        sitemap.append(
            f"  <url><loc>{SITE_URL}{url}</loc>"
            f"<changefreq>monthly</changefreq><priority>{priorities.get(url, '0.5')}</priority></url>"
        )
    sitemap.append("</urlset>\n")
    (DOCS / "sitemap.xml").write_text("\n".join(sitemap), encoding="utf-8")
    (DOCS / "robots.txt").write_text(
        f"User-agent: *\nAllow: /\n\nSitemap: {SITE_URL}/sitemap.xml\n", encoding="utf-8"
    )
    (DOCS / "CNAME").write_text("bugbounty.danubelabs.net\n", encoding="utf-8")
    print("  sitemap.xml, robots.txt, CNAME")


if __name__ == "__main__":
    main()
