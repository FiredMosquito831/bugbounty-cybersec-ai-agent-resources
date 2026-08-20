# Autonomous Bug Bounty Agent — Research Archive & Context

> **Version:** 1.0 — 2026-08-20  
> **Status:** Research & curation phase complete. Ready for architecture design and agent implementation.  
> **Purpose:** This archive is a comprehensive, indexed knowledge base prepared specifically for designing and building an **autonomous AI agent that performs deep, profound bug bounty hunting and vulnerability discovery** across web applications, APIs, networks, cloud infrastructure, binaries, and emerging attack surfaces.

---

## Table of Contents

1. [What This Archive Is](#what-this-archive-is)
2. [Why It Exists](#why-it-exists)
3. [How to Use This Archive](#how-to-use-this-archive)
4. [Archive Structure](#archive-structure)
5. [Research Methodology](#research-methodology)
6. [Complete Source Inventory](#complete-source-inventory)
7. [Key Architecture Insights (Why + How)](#key-architecture-insights-why--how)
8. [The Claude Code Bug Bounty Ecosystem](#the-claude-code-bug-bounty-ecosystem)
9. [Vulnerability Class Taxonomy](#vulnerability-class-taxonomy)
10. [Tooling Taxonomy](#tooling-taxonomy)
11. [Methodology Stack](#methodology-stack)
12. [What To Build Next (Continuation Guide)](#what-to-build-next-continuation-guide)
13. [Known Gaps](#known-gaps)
14. [Operational Notes](#operational-notes)

---

## What This Archive Is

This is a **curated, indexed, read-only research archive** containing:

- **36 cloned repositories** (read-only, no code executed) — production-tested security tools, skill bundles, methodologies, and autonomous agent frameworks
- **17 academic/industry papers** (PDFs) — verified research on AI-driven vulnerability discovery, fuzzing pipelines, prompt injection, and agent architectures
- **1,216+ catalogued sources** with titles, URLs, and descriptions — every tool, framework, book, technique, and standard referenced
- **55+ security books** catalogued with metadata
- **28 YouTube channels + 12 conferences** for ongoing learning
- **12 Claude Code bug bounty repos** totaling 11,573 stars — ready-made agent blueprints

Everything is indexed in `00_REPERTOIRE_INDEX.md` (2,861 lines) — the single source of truth.

---

## Why It Exists

### The Goal
Build an **autonomous AI agent** that can:
1. **Discover** vulnerabilities across the full attack surface (web, API, network, cloud, mobile, binary, smart contract, IoT)
2. **Reason** about findings like a professional security researcher (threat modeling, chaining, impact assessment)
3. **Act** with structured methodology (PTES-aligned: recon → analysis → exploitation → reporting)
4. **Validate** findings with working proof-of-concepts (evidence-first, no theoretical findings)
5. **Learn** from disclosed reports and adapt to new attack surfaces

### Why This Archive Was Needed
Building such an agent requires grounding in:
- **Established methodology** (OWASP, PTES, NIST, MITRE ATT&CK) — so the agent tests systematically, not randomly
- **Verified research** (Sailor, ELFuzz, ARACNE, NOVA) — so the agent uses architectures proven to work (30x improvement via composition, not model selection)
- **Production tooling** (36 repos) — so the agent has real tools to invoke, not just theoretical knowledge
- **Real-world patterns** (681 disclosed reports, 2887 HackerOne cases) — so the agent learns from what actually gets paid
- **The Claude Code ecosystem** (11,573 stars of agent blueprints) — so the agent builds on existing patterns, not from scratch

### Why These Specific Sources
Every source was selected because it is **actionable for agent construction**:
- Methodologies → agent workflow design
- Papers → agent architecture decisions (multi-agent, multi-model, feedback loops)
- Tools → agent tool-use capabilities
- Bug bounty repos → agent skill/prompt patterns
- Books → deep domain knowledge for reasoning

---

## How to Use This Archive

### For an AI Agent (CLAUDE.md-style entry)
```
You are building an autonomous bug bounty agent. All research is in:
  pentesting_research/repertoire/

START HERE:
  1. Read 00_REPERTOIRE_INDEX.md (the master index, 2861 lines)
  2. For methodology: see OWASP WSTG (03_repos/owasp-wstg), PTES, ASVS 5.0 (03_repos/owasp-asvs)
  3. For agent architecture: see papers in 01_papers/ (Sailor, ARACNE, NOVA, ELFuzz)
  4. For production agent patterns: see 03_repos/claude-bughunter, pentest-agents, bughunter-ai
  5. For tooling: see 03_repos/payloads-all-the-things, internal-all-the-things, threatswarm
  6. For vulnerability patterns: see 03_repos/payloads-all-the-things (63+ categories)
  7. For verified research findings: see "Deep Research Workflow" section in index

CRITICAL: All repos are READ-ONLY. Do not execute any downloaded code.
Browse for knowledge, patterns, and methodology only.
```

### For a Human Researcher
1. Open `00_REPERTOIRE_INDEX.md` — search for any topic
2. Follow URLs to primary sources
3. Read the papers in `01_papers/` for architecture decisions
4. Study the repos in `03_repos/` for implementation patterns
5. Use `_new_sources_full.tsv` as a searchable catalog of 1,216 sources

---

## Archive Structure

```
pentesting_research/
└── repertoire/
    ├── AUTONOMOUS_AGENT_CONTEXT.md    ← THIS FILE (start here for context)
    ├── 00_REPERTOIRE_INDEX.md         ← master index (2861 lines, every source)
    ├── _new_sources_full.tsv          ← 1216 new sources (title+url+description)
    ├── _synthesis_raw.md              ← raw research from 19 agents (454KB)
    ├── 01_papers/                     ← 17 academic/industry papers (PDFs)
    ├── 02_books/                      ← book references (metadata only)
    ├── 03_repos/                      ← 36 cloned repos (read-only)
    │   ├── owasp-wstg/                ← OWASP Web Security Testing Guide v5.0
    │   ├── owasp-asvs/                ← OWASP ASVS 5.0 (May 2025)
    │   ├── owasp-cheatsheets/         ← Full OWASP Cheat Sheet Series
    │   ├── payloads-all-the-things/   ← 63+ vulnerability categories + payloads
    │   ├── internal-all-the-things/   ← AD/internal pentest cheatsheets
    │   ├── hardware-all-the-things/   ← IoT/hardware pentest wiki
    │   ├── claude-bughunter/          ← 82 skills, 681 disclosed-report patterns
    │   ├── shuvonsec-claude-bug-bounty/ ← AI-powered bug bounty hunting
    │   ├── H-mmer-pentest-agents/     ← 48 agents, 26 commands, exploit chains
    │   ├── MyuriKanao-src-hunter-skill/ ← 305 payloads, 263 WAF bypasses
    │   ├── trailofbits-skills/        ← 79 security skills (Trail of Bits)
    │   ├── threatswarm/              ← 27 agents, 754 MITRE-mapped skills
    │   ├── cai/                       ← Cybersecurity AI framework (9644 stars)
    │   └── ... (24 more)
    ├── 04_methodologies/              ← placeholder for future extraction
    ├── 05_skills_plugins/             ← 5 ThreatSwarm built-in skills extracted
    ├── 06_tools_ref/                  ← placeholder for future extraction
    └── 07_vulnerability_classes/      ← placeholder for future extraction
```

---

## Research Methodology

### How This Archive Was Built (3 Expansions)

**Expansion 1 — Manual Deep Research (105-agent workflow)**
- 5 broad scope searches → 20 targeted research angles
- Deep-fetched 15+ high-density sources (OWASP, NOVA, ARACNE, ThreatSwarms)
- Verified 12 claims via 3-vote adversarial verification
- Manually cloned 18 repos, downloaded 11 papers
- Result: 1,036-line index covering methodology, web/app security, agent architectures

**Expansion 2 — Full Cybersec Scope (19 deep-research agents)**
- Phase 1: 5 broad searches mapped ALL cybersecurity domains
- Phase 2: 19 targeted agents (one per domain), each finding 40-139 sources
- Phase 3: Opus synthesis (partial — API budget hit on scope-synthesis)
- Manual extraction: 1,216 new sources catalogued with descriptions
- Added 6 repos (OWASP WSTG, ASVS, Cheat Sheets, PATT, InternalAllTheThings, HardwareAllTheThings)
- Result: 2,861-line index, 1,216 new sources

**Expansion 3 — Gap Discovery (targeted repo search)**
- Found an entire MISSED category: Claude Code bug bounty repos
- Searched GitHub for `claude code bug bounty skills/pentest agents`
- Found 15+ repos totaling 11,573 stars
- Cloned top 12 repos
- Result: 36 total repos, new category added to index

### Verification Approach
- **12 claims verified** via 3-vote adversarial verification (from deep-research workflow)
- **8 claims refuted** (overgeneralized or unverifiable) — documented for awareness
- **Key verified findings:**
  - Hybrid LLM + program analysis pipelines dominate pure approaches (Sailor: 379 vulns vs 12)
  - Each pipeline component is essential (ablation: removing any → collapse to baseline)
  - OWASP Top 10:2025 elevated Supply Chain to A03
  - Threat modeling's 4-question framework maps to agent workflow

### What Was Missed (and caught)
- **Claude Code bug bounty repos** — broad searches found methodologies but not specific GitHub repos. Caught by manual check of `elementalsouls/Claude-BugHunter`. Led to discovery of 12 repos / 11,573 stars.
- **Lesson:** Always supplement broad searches with targeted repo searches for "claude code + [domain]".

---

## Complete Source Inventory

### By Type

| Type | Count | Location |
|---|---|---|
| Cloned repos (read-only) | 36 | `03_repos/` |
| Academic/industry papers | 17 | `01_papers/` |
| New sources (expansion 2) | 1,216 | `_new_sources_full.tsv` |
| Books catalogued | 55+ | `00_REPERTOIRE_INDEX.md` |
| YouTube channels | 28 | index |
| Conferences | 12 | index |
| Built-in skills extracted | 5 | `05_skills_plugins/` |

### By Domain (expansion 2 — 1,216 sources)

| Domain | Sources |
|---|---|
| OAuth, OIDC & SSO Exploitation | 168 |
| Cloud Security, IAM & Multi-Account Attack Paths | 168 |
| Container, Kubernetes & Cloud-Native Security | 133 |
| GraphQL, API Security & Endpoint Enumeration | 139 |
| Software Supply Chain & Dependency Security | 132 |
| Mobile App Pentesting & Reverse Engineering | 112 |
| Web3, Smart Contract & Blockchain Security | 84 |
| LLM Security, Prompt Injection & AI Red-Teaming | 89 |
| AI/ML for Vuln Discovery & Fuzzing | 89 |
| Wireless, Bluetooth, IoT & Protocol Exploitation | 46 |
| Methodologies, Frameworks, Compliance, AD, Deserialization, RCE, Evasion, Memory, Recon, Social Engineering | 68 |

### By Domain (expansion 3 — 12 repos, 11,573 stars)

| Domain | Repos | Stars |
|---|---|---|
| Claude Code bug bounty skill bundles | 12 | 11,573 |

---

## Key Architecture Insights (Why + How)

### 1. Composition Beats Model Selection (Why: Sailor paper)
- **Finding:** Sailor pipeline found 379 vulns vs Claude Code alone finding 12 (30x)
- **Why it matters:** The agent's architecture (how components compose) matters more than which LLM it uses
- **How to apply:** Design multi-phase pipelines (static analysis → LLM synthesis → symbolic execution → validation), not single-pass LLM calls

### 2. Every Component Is Essential (Why: Ablation studies)
- **Finding:** Removing ANY guidance mechanism collapses performance to near-baseline
- **Why it matters:** Don't build a "good enough" agent with missing pieces — each component (targeting, feedback, validation) is load-bearing
- **How to apply:** Include ALL of: static analysis targeting, iterative LLM feedback loops, concrete validation, evidence capture

### 3. Multi-Agent, Multi-Model (Why: ARACNE paper)
- **Finding:** Different LLMs for planning (GPT-o3-mini) vs execution (LLaMA 3.1) vs summarization (GPT-4o) increases accuracy
- **Why it matters:** One model for all tasks is suboptimal
- **How to apply:** Route tasks to specialized agents/models based on task type

### 4. Scope Enforcement at OS Level (Why: ThreatSwarm)
- **Finding:** Deterministic hooks outside the agent loop prevent scope violations
- **Why it matters:** Autonomous agents need hard boundaries, not prompt-instruction boundaries
- **How to apply:** Implement `scope_check.py`-style hooks that run OUTSIDE the agent loop, CIDR-aware

### 5. Evidence-First (Why: ThreatSwarm + professional practice)
- **Finding:** No theoretical findings — only verified PoCs with captured evidence
- **Why it matters:** Bug bounty platforms reject reports without working proofs
- **How to apply:** Every finding must produce: working PoC + HTTP evidence + screenshot + CVSS

### 6. Disclosed-Report Patterns (Why: Claude-BugHunter, src-hunter-skill)
- **Finding:** 681 disclosed-report patterns + 2887 HackerOne cases available as structured data
- **Why it matters:** Agent should learn from what actually gets paid, not just theory
- **How to apply:** Train/fine-tune on disclosed reports; use as few-shot examples for vulnerability classes

### 7. MITRE ATT&CK Mapping (Why: ThreatSwarm 754 skills)
- **Finding:** Every technique mapped to ATT&CK, CSF 2.0, ATLAS, D3FEND, AI RMF
- **Why it matters:** Structured threat intelligence enables systematic coverage
- **How to apply:** Map every agent action to ATT&CK technique for coverage tracking

### 8. Lifecycle Security (Why: AgentWard)
- **Finding:** Protection across initialization → input → memory → decision → execution
- **Why it matters:** Agent security failures propagate across stages
- **How to apply:** Defense-in-depth at each agent lifecycle stage

---

## The Claude Code Bug Bounty Ecosystem

### Why This Category Matters
The broad research searches (expansions 1-2) found methodologies, tools, and papers — but **missed an entire ecosystem** of production-ready Claude Code bug bounty agent implementations. These 12 repos (11,573 stars) are **direct blueprints** for the agent being built.

### The Repos (by stars)

| Stars | Repo | Key Content |
|---|---|---|
| ⭐4256 | [shuvonsec/claude-bug-bounty](https://github.com/shuvonsec/claude-bug-bounty) | Recon, 20 vuln classes, autonomous hunting, report generation |
| ⭐3699 | [elementalsouls/Claude-BugHunter](https://github.com/elementalsouls/Claude-BugHunter) | 82 skills, 15 slash commands, 681 disclosed-report patterns, 24 vuln classes |
| ⭐802 | [H-mmer/pentest-agents](https://github.com/H-mmer/pentest-agents) | 48 agents, 26 commands, 19 CLI tools, 2 MCP servers, exploit chain builder |
| ⭐599 | [MyuriKanao/src-hunter-skill](https://github.com/MyuriKanao/src-hunter-skill) | 19 playbooks, 305 payloads, 263 WAF/EDR bypasses, 2887 HackerOne cases |
| ⭐476 | [transilienceai/communitytools](https://github.com/transilienceai/communitytools) | Open-source skills, agents, slash commands for pentesting/bug bounty |
| ⭐383 | [Gabson0x/bountyforge](https://github.com/Gabson0x/bountyforge) | Smart contract audits (EVM, Move, Solana, TRON), web/API, reports |
| ⭐221 | [shuvonsec/public-skills-builder](https://github.com/shuvonsec/public-skills-builder) | Generate skills from public HackerOne reports — 18 vuln classes |
| ⭐64 | [h4ckologic/bughunter-ai](https://github.com/h4ckologic/bughunter-ai) | 20 AI agents, state-machine orchestration, Burp Suite MCP |
| ⭐53 | [gigioneggiando/argo](https://github.com/gigioneggiando/argo) | LLM-native static vuln detection, reviewable reports |
| ⭐40 | [26zl/cybersec-toolkit](https://github.com/26zl/cybersec-toolkit) | 670+ tools, 870+ skills, authorization-gated MCP |
| ⭐36 | [0xGhostCAT/claude-ai-cyber-security-skills](https://github.com/0xGhostCAT/claude-ai-cyber-security-skills) | 30 skills + 60+ tools for HackerOne/Bugcrowd |
| ⭐23 | [Orizon-eu/claude-code-pentest](https://github.com/Orizon-eu/claude-code-pentest) | 6 skills, full pentest lifecycle, 43 scripts |

### What These Repos Contain (for agent design)
1. **Vulnerability playbooks** — structured skill definitions for XSS, SQLi, SSRF, IDOR, etc.
2. **WAF/EDR bypass libraries** — 263+ bypass techniques (src-hunter-skill)
3. **Disclosed-report pattern libraries** — 681 patterns (Claude-BugHunter), 2887 HackerOne cases (src-hunter-skill)
4. **Multi-agent orchestration** — 48 agents (pentest-agents), 20 agents (bughunter-ai)
5. **Exploit chain builders** — chaining low-severity into high-impact
6. **Autonomous hunt loops** — recon → vuln discovery → validation → reporting
7. **Report generation** — submission-ready for HackerOne, Bugcrowd, Intigriti, Immunefi

### How to Use These Repos for Your Agent
- **Study the skill structure** — how vulnerability classes are defined as agent skills
- **Extract disclosed-report patterns** — use as training data / few-shot examples
- **Copy orchestration patterns** — multi-agent coordination, state machines
- **Adapt WAF bypass libraries** — encode as agent knowledge
- **Use exploit chain builders** — chain low → high severity automatically

---

## Vulnerability Class Taxonomy

### OWASP Top 10 (2021) — primary classification
1. **A01: Broken Access Control** — IDOR/BOLA, privilege escalation, CORS, JWT attacks
2. **A02: Cryptographic Failures** — weak algorithms, key management, SSL/TLS, padding oracles
3. **A03: Injection** — SQLi, NoSQLi, OS command, SSTI, XXE, LDAP, XPath, CRLF
4. **A04: Insecure Design** — business logic, race conditions, state machine abuse
5. **A05: Security Misconfiguration** — default accounts, headers, CORS/CSP, cloud misconfig
6. **A06: Vulnerable Components** — known CVEs, supply chain, dependency confusion
7. **A07: Auth Failures** — weak passwords, credential stuffing, JWT flaws, OAuth misconfig
8. **A08: Software/Data Integrity** — insecure deserialization, CI/CD abuse
9. **A09: Logging Failures** — missing logs, log injection
10. **A10: SSRF** — URL fetching, cloud metadata, IPv4/IPv6 bypass

### OWASP Top 10:2025 Changes
- **A02: Security Misconfiguration** moved to #2 (from #5)
- **A03: Software Supply Chain Failures** newly elevated to top-10

### OWASP API Top 10 (2023)
- API1: BOLA, API2: Broken Auth, API3: Mass Assignment, API4: Resource Consumption, API5: BFLA, API6: Sensitive Business Flows, API7: SSRF, API8: Misconfiguration, API9: Inventory Management, API10: Unsafe API Consumption

### Additional Classes (beyond OWASP Top 10)
- **XSS** — Reflected, Stored, DOM, Blind, via file upload
- **SSTI** — Jinja2, Twig, Freemarker, Velocity
- **XXE** — SVG uploads, DOCX/XLSX, OOB DTD
- **File Upload** — extension bypass, Content-Type, double extensions, web shell
- **LFI/RFI** — path traversal, PHP wrappers, log poisoning
- **CSRF** — missing tokens, SameSite bypass
- **Open Redirect** — absolute URLs, @ syntax, hash manipulation
- **Prototype Pollution** — __proto__, constructor.prototype
- **Cache Poisoning** — header reflection, X-Forwarded-Host
- **Subdomain Takeover** — dangling CNAMEs
- **GraphQL** — introspection, authorization, injection
- **WebSockets** — message injection, auth bypass
- **OAuth** — redirect_uri, state, PKCE, code interception
- **Business Logic** — workflow bypass, pricing, race conditions
- **Deserialization** — Java, PHP, Python, .NET gadget chains
- **Memory Corruption** — buffer overflow, UAF, format string, integer overflow
- **Auth Bypass** — SQLi-based, JWT alg=none, session prediction
- **Privilege Escalation** — horizontal, vertical, AD, sudo
- **Cryptography** — weak ciphers, ECB, hardcoded keys, timing attacks
- **Secrets Exposure** — API keys in code, git history, logs
- **Prompt Injection** — direct, indirect, MCP tool poisoning, semantic
- **Smart Contract** — reentrancy, flash loans, oracle manipulation, MEV

---

## Tooling Taxonomy

### Reconnaissance / OSINT
`subfinder`, `amass`, `assetfinder`, `findomain`, `chaos`, `crt.sh`, `Censys`, `Shodan`, `theHarvester`, `SpiderFoot`, `securitytrails`

### HTTP/URL Discovery
`gau`, `waybackurls`, `katana`, `ffuf`, `gobuster`, `feroxbuster`, `httpx`, `httprobe`, `aquatone`, `linkfinder`, `kiterunner`

### Network Scanning
`nmap`, `naabu`, `masscan`, `rustscan`, `Bettercap`, `Responder`, `testssl.sh`, `sslscan`

### Web Proxy / Interception
`Burp Suite`, `OWASP ZAP`, `mitmproxy`

### Web Fuzzing / Scanning
`ffuf`, `nuclei`, `sqlmap`, `dalfox`, `XSStrike`, `wpscan`, `nikto`, `graphqler`, `crackql`, `inql`

### API Testing
`RESTler`, `arjun`, `jwt_tool`, `Postman`, `vespasian`, `apithief`, `apiprober`

### Password / Credential
`hashcat`, `John the Ripper`, `CeWL`, `hydra`, `medusa`, `mimikatz`, `secretsdump`, `linpeas`, `winpeas`

### Exploitation Frameworks
`Metasploit`, `searchsploit`, `Sliver`, `Havoc`, `Pacu` (AWS), `pwnable.kr`

### Post-Exploitation
`linpeas`/`winpeas`, `BloodHound`, `Certipy`, `Impacket`, `chisel`, `ligolo-ng`

### Wireless
`aircrack-ng`, `bettercap`, `killerbee` (ZigBee), `chirpotle` (LoRaWAN), `z-attack-ng` (Z-Wave), `angryoxide`

### Cloud
`Pacu`, `ScoutSuite`, `cloud-custodian`, `checkov`, `terrascan`, `trivy`, `grype`, `syft`, `cloudsploit`

### Mobile
`MobSF`, `Frida`, `jadx`, `apktool`, `objection`, `medusa`, `rekit`, `revkit`

### Social Engineering
`GoPhish`, `evilginx2`, `SET`, `modlishka`

### Evasion
`Donut`, `LOLBins`, `AMSI bypass`, `AV/EDR evasion`

### Forensic / DFIR
`Volatility3`, `AVML`, `Timesketch`, `Velociraptor`, `Elastic SIEM`, `Splunk`, `Wazuh`, `Sigma`

### Binary / Reverse Engineering
`Ghidra`, `Radare2`, `Binary Ninja`, `IDA`, `GDB`+`pwndbg`/`GEF`, `pwntools`, `angr`, `ROPGadget`

### Compliance
`OpenSCAP`, `Lynis`, `kube-bench`, `kube-hunter`

### Static Analysis / Code Review
`CodeQL`, `Semgrep`, `SonarQube`, `ESLint`, `SpotBugs`, `Bandit`, `gosec`, `cargo-audit`, `npm audit`, `pip-audit`, `slither` (smart contracts), `mythril`

### Fuzzing
`AFL++`, `libFuzzer`, `Honggfuzz`, `Angora`, `VUzzer`, `Eclipser`, `QSYM`, `Driller`, `Echidna`, `Medusa`, `Halmos`

### Claude Code Specific
Kali MCP integration, Playwright screenshots, `scope_check.py` (deterministic OS-level scope gating)

---

## Methodology Stack

### PTES — Penetration Testing Execution Standard (7 phases)
1. Pre-engagement Interactions
2. Intelligence Gathering
3. Threat Modeling
4. Vulnerability Analysis
5. Exploitation
6. Post Exploitation
7. Reporting

### OWASP WSTG v5.0 (12 chapters, 100+ tests)
Information Gathering → Configuration/Deployment → Identity Management → Authentication → Authorization → Session Management → Input Validation → Error Handling → Weak Cryptography → Business Logic → Client-side → API Testing

### OWASP ASVS 5.0 (May 2025, 14 requirements, 3 levels)
Level 1 (BAS), Level 2 (信用), Level 3 (HIGH). Requirements: Architecture, Authentication, Session Management, Access Control, Validation/Sanitization/Encoding, Cryptography, Error Logging, Data Protection, Communications, Malicious Software, Business Logic, Files/Resources, API, Configuration.

### NIST SP 800-115
Review Techniques → Target Identification → Vulnerability Validation → Assessment Planning → Execution → Post-Testing

### OSSTMM
Security Analysis, Operational Metrics, Trust, Work Flow, Human Security, Physical Security, Wireless, Telecommunications, Data Networks, Compliance

### PCI DSS (Req 11.3)
Components, Qualifications, Methodologies, Reporting. Covers CDE + critical systems, external + internal, application + network layers.

### Threat Modeling (4Q + STRIDE)
- What are we working on? / What can go wrong? / What are we going to do? / Did we do a good enough job?
- STRIDE: Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privileges

### MITRE ATT&CK (12 tactics, 50+ techniques)
Initial Access → Execution → Persistence → Privilege Escalation → Defense Evasion → Credential Access → Discovery → Lateral Movement → Collection → Exfiltration → C2 → Impact

### Agent Workflow (synthesized)
```
Pre-engagement (scope, rules) 
  → Recon (subdomains, CT logs, JS, ASN, ports)
  → Mapping (manual app mapping, param discovery, tech fingerprinting)
  → Analysis (per-vuln-class testing with checklists)
  → Exploitation (PoC construction, chaining)
  → Validation (clean-environment replay, evidence capture)
  → Reporting (CVSS, steps, impact, remediation)
```

---

## What To Build Next (Continuation Guide)

### Immediate Next Steps
1. **Read the key papers** (in `01_papers/`) for architecture decisions:
   - `sailor_llm_fuzzing_vuln_discovery.pdf` — pipeline composition
   - `aracne_llm_pentesting_agent.pdf` — multi-LLM routing
   - `nova_frontier_ai_vuln_discovery.html` — multi-agent/multi-model
   - `elfuzz_llm_synthesized_fuzzers.pdf` — fuzzer space model
   - `design_patterns_securing_llm_agents.pdf` — agent security

2. **Study the bug bounty repos** (in `03_repos/`) for implementation patterns:
   - `claude-bughunter/` — 82 skills, 681 disclosed-report patterns
   - `H-mmer-pentest-agents/` — 48 agents, orchestration
   - `h4ckologic-bughunter-ai/` — state-machine orchestration
   - `MyuriKanao-src-hunter-skill/` — 305 payloads, 263 WAF bypasses

3. **Design the agent architecture** based on verified findings:
   - Multi-agent (separate recon/web/API/AD/cloud/mobile/crypto/reverse/DFIR/report agents)
   - Multi-model (planning LLM + execution LLM + summarization LLM)
   - Multi-phase pipeline (static analysis → LLM synthesis → validation → evidence)
   - OS-level scope enforcement (deterministic hook outside agent loop)
   - Evidence-first (PoC required for every finding)

4. **Extract disclosed-report patterns** from `claude-bughunter` and `src-hunter-skill` for training data

5. **Map every action to MITRE ATT&CK** for coverage tracking

### Architecture Decisions to Make
- **Model routing:** Which LLMs for which tasks? (ARACNE pattern: GPT-o3-mini plan, LLaMA execute, GPT-4o summarize)
- **Agent granularity:** How many specialist agents? (ThreatSwarm: 27, pentest-agents: 48, bughunter-ai: 20)
- **Scope enforcement:** How to implement deterministic hooks?
- **Evidence format:** What does a finding look like? (CVSS + steps + HTTP evidence + screenshot)
- **Validation:** How to replay findings in clean environment? (NOVA principle)

### Implementation Order
1. Recon agent (subdomain enum, HTTP probing, tech fingerprinting) — most mature tools
2. Web vuln agent (per OWASP WSTG test categories)
3. API security agent (REST/GraphQL/gRPC)
4. Cloud agent (AWS/Azure/GCP IAM, storage, compute)
5. Reporting agent (CVSS, steps, impact, remediation)
6. Orchestration layer (multi-agent coordination, task routing)

---

## Known Gaps

These areas were identified during research but not yet fully covered:

1. **Cloud pentesting deep methodology** — tools referenced (Pacu, ScoutSuite) but no dedicated playbook. Need: cloud goats (flaws.cloud, etc.), Stratus Red Team
2. **Kubernetes pentesting** — kube-hunter/kube-bench referenced but no dedicated methodology. Need: Kubernetes Goat, Kubewarden, NSA/CISA K8s Hardening Guide
3. **Mobile pentesting (iOS/Android)** — tools referenced but no OWASP MSTG in cloned repos. Need: MSTG, Damn Vulnerable iOS App, InsecureBankV2
4. **Heap exploitation deep techniques** — general methodology but no unlink/fastbin/tcache specifics. Need: how2heap, Glibc malloc internals
5. **Fuzzing pipelines (practical)** — papers (Sailor, ELFuzz) but no AFL++/libfuzzer tutorial. Need: AFL++ docs, LLVM fuzzing guide, OSS-Fuzz methodology
6. **Supply chain deep methodology** — OWASP A03:2025 recognized but no SBOM/SLSA deep dive. Need: in-toto, sigstore, cosign, SLSA framework
7. **AD pentesting full chain** — 5 ThreatSwarm skills cover AD but no unified doc. Need: SpecterOps AD attack paths, HarmJ0y methodology
8. **Smart contract full methodology** — Trail of Bits has 2 skills but no dedicated audit guide. Need: Trail of Bits smart contract security guide, Consensys best practices, SWC Registry
9. **Red team full methodology** — PTES + PTF but no comprehensive red team planning doc. Need: BloodHound tactics, MITRE ATT&CK Navigator, crimson pentagon
10. **Unified agent architecture paper** — pieces exist (NOVA, ARACNE, ThreatSwarm, Aegis, AgentWard) but NO single paper proposes a unified architecture for autonomous pentest/bug bounty agent. **This is the gap your agent fills.**

---

## Operational Notes

### Critical Rules
- **All repos are READ-ONLY.** Browse for knowledge, patterns, and methodology only. Do not execute any downloaded code.
- **For authorized testing only.** Always obtain written permission before testing any system you do not own.
- **Evidence-first.** No theoretical findings — only verified PoCs with captured evidence.
- **Scope enforcement.** Implement deterministic hooks outside the agent loop.

### File Locations
- Master index: `repertoire/00_REPERTOIRE_INDEX.md`
- New sources catalog: `repertoire/_new_sources_full.tsv` (1,216 sources, tab-separated)
- Raw research: `repertoire/_synthesis_raw.md` (454KB, all 19 agents)
- Papers: `repertoire/01_papers/` (17 PDFs)
- Repos: `repertoire/03_repos/` (36 repos)
- This context: `repertoire/AUTONOMOUS_AGENT_CONTEXT.md`

### Statistics (as of 2026-08-20)
- 36 repos (read-only)
- 17 papers
- 1,216 new sources cataloged (981 with descriptions)
- 55+ books
- 28 YouTube channels, 12 conferences
- 12 bug bounty repos (11,573 stars)
- 12 verified research findings, 8 refuted
- 10 identified gaps

---

*This archive was built through 3 research expansions totaling 105+ deep-research agents, 23+ source fetches, and adversarial verification of 20+ claims. It is ready for the next phase: architecture design and agent implementation.*

*For questions or continuation: start with `00_REPERTOIRE_INDEX.md` and the key papers in `01_papers/`.*
