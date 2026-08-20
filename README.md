# Bug Bounty & Cybersec Resources for AI Agents

> **This repository is the predecessor and active work-in-progress foundation for an autonomous bug bounty / vulnerability discovery AI agent.** It is a comprehensive, indexed research archive — the knowledge base that the agent will be built on.

## What This Repo Is

A curated, read-only archive of **everything needed to build an autonomous AI agent that performs deep bug bounty hunting and vulnerability discovery** across web applications, APIs, networks, cloud infrastructure, binaries, smart contracts, and emerging attack surfaces.

This is **Phase 1 (Research & Curation)** of a larger project. The archive feeds directly into agent architecture design and implementation.

## Why It Exists

Building an autonomous security agent requires grounding in:
- **Established methodology** (OWASP, PTES, NIST, MITRE ATT&CK) — so the agent tests systematically
- **Verified research** (Sailor, ELFuzz, ARACNE, NOVA) — architectures proven to work (30x improvement via composition)
- **Production tooling** (36 repos) — real tools for the agent to invoke
- **Real-world patterns** (681 disclosed reports, 2887 HackerOne cases) — learning from what actually gets paid
- **The Claude Code ecosystem** (11,573 stars of agent blueprints) — building on existing patterns

## What's Inside

| Category | Count | Location |
|---|---|---|
| Cloned repos (read-only) | 36 | `repertoire/03_repos/` (see `REPO_MANIFEST.md` for URLs) |
| Academic/industry papers | 17 | `repertoire/01_papers/` |
| Catalogued sources with descriptions | 1,216 | `repertoire/_new_sources_full.tsv` |
| Books catalogued | 55+ | `repertoire/00_REPERTOIRE_INDEX.md` |
| YouTube channels | 28 | index |
| Conferences | 12 | index |
| Claude Code bug bounty repos | 12 (11,573 stars) | `repertoire/03_repos/` |

## Start Here

1. **`repertoire/AUTONOMOUS_AGENT_CONTEXT.md`** — full context document (what, why, how, architecture insights, continuation guide). Read this first.
2. **`repertoire/00_REPERTOIRE_INDEX.md`** — master index of every source (2,861 lines)
3. **`repertoire/REPO_MANIFEST.md`** — manifest of 36 cloned repos (URLs to re-clone)

## Project Status

| Phase | Status |
|---|---|
| Phase 1: Research & Curation | **Complete** (this repo) |
| Phase 2: Architecture Design | Up next |
| Phase 3: Agent Implementation | Planned |
| Phase 4: Testing & Iteration | Planned |

### What's Already Done
- 3 research expansions totaling 105+ deep-research agents
- 12 verified research findings (adversarial 3-vote verification)
- Full vulnerability class taxonomy (63+ classes)
- Tooling taxonomy (14 categories, 60+ tools)
- Methodology stack (PTES, WSTG, ASVS, NIST, OSSTMM, PCI DSS, ATT&CK)
- 10 identified gaps (opportunities for the agent)

### What's Next (for the autonomous agent)
1. Read key papers for architecture decisions (Sailor, ARACNE, NOVA, ELFuzz)
2. Study bug bounty repos for implementation patterns (claude-bughunter, pentest-agents)
3. Design multi-agent, multi-model pipeline with scope enforcement
4. Extract disclosed-report patterns for training data
5. Implement recon → analysis → exploitation → reporting workflow

See **"What To Build Next"** in `AUTONOMOUS_AGENT_CONTEXT.md` for the full continuation guide.

## Key Insights (from verified research)

1. **Composition beats model selection** — Sailor pipeline found 379 vulns vs 12 (30x) via architecture, not better models
2. **Every component is essential** — ablation studies show removing any guidance mechanism collapses performance
3. **Multi-agent, multi-model** — different LLMs for planning vs execution vs summarization increases accuracy
4. **Scope enforcement at OS level** — deterministic hooks outside the agent loop (not prompt instructions)
5. **Evidence-first** — no theoretical findings, only verified PoCs with captured evidence
6. **Disclosed-report patterns** — 681+ real patterns available as structured training data

## Critical Rules

- **All repos are READ-ONLY.** Browse for knowledge and patterns only. Do not execute any downloaded code.
- **For authorized testing only.** Always obtain written permission before testing any system you do not own.
- **Re-clone repos** from `repertoire/REPO_MANIFEST.md` (they're gitignored — already versioned upstream).

## Research Methodology

Built through 3 expansions:
1. **Manual deep research** — 105-agent workflow, OWASP/PTES/NOVA/ARACNE sources
2. **Full cybersec scope** — 19 deep-research agents covering all domains
3. **Gap discovery** — found the Claude Code bug bounty repo ecosystem (missed by broad searches)

## License & Disclaimer

This archive is for **authorized security research and education only**. All sources are read-only references. The repository does not contain any exploit code or active attack tools — only knowledge, methodology, and patterns for building defensive/offensive security agents operating within legal boundaries.

---

*This is the research foundation (Phase 1) for an autonomous bug bounty / vulnerability discovery AI agent. The archive is the agent's knowledge base — everything it needs to reason about security testing, choose tools, follow methodology, and learn from real-world patterns.*

*2026-08-20*
