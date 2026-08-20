# Cloned Repository Manifest

This file lists all cloned repositories with their source URLs. The repo working trees are gitignored (already versioned upstream) — re-clone any with `git clone <url>`.

| Directory | Source URL | Stars | Description |
|---|---|---|---|
| `03_repos/awesome-pentest` | https://github.com/enaqx/awesome-pentest | 26604 | Awesome pentesting resources list |
| `03_repos/bug-bounty-methodology-2025` | https://github.com/amrelsagaei/Bug-Bounty-Hunting-Methodology-2025 | 477 | Bug Bounty Methodology 2025 |
| `03_repos/bug-bounty-methodology-2026` | https://github.com/ItsDarker/Bug-Bounty-Methodology-2026 | — | 7-phase workflow 2026 |
| `03_repos/bug-bounty-roadmap-2025` | https://github.com/l3tchupkt/Bug-Bounty-Roadmap-2025 | 3 | 10-phase progressive roadmap |
| `03_repos/bugbounty-cheatsheet` | https://github.com/EdOverflow/bugbounty-cheatsheet | 6000 | Payloads, tips, books |
| `03_repos/bugbountyguide` | https://github.com/EdOverflow/bugbountyguide | 472 | BBB launchpad |
| `03_repos/cai` | https://github.com/aliasrobotics/cai | 9644 | Cybersecurity AI framework |
| `03_repos/claude-bughunter` | https://github.com/elementalsouls/Claude-BugHunter | 3699 | 82 skills, 681 disclosed-report patterns |
| `03_repos/claude-code-plugins-plus` | https://github.com/danielmiessler/claude-code-plugins-plus | — | 25 security plugins |
| `03_repos/claude-pentest` | https://github.com/stickman230/claude-pentest | 84 | 15 agents, 63 attack categories |
| `03_repos/claude-skills-pentest` | https://github.com/WolzenGeorgi/claude-skills-pentest | — | VPS-based scanner |
| `03_repos/hardware-all-the-things` | https://github.com/swisskyrepo/HardwareAllTheThings | — | IoT/hardware pentest wiki |
| `03_repos/internal-all-the-things` | https://github.com/swisskyrepo/InternalAllTheThings | — | AD/internal pentest cheatsheets |
| `03_repos/nahamsec-resources` | https://github.com/nahamsec/Resources-for-Beginner-Bug-Bounty-Hunters | 11923 | Curated beginner collection |
| `03_repos/owasp-asvs` | https://github.com/OWASP/ASVS | — | ASVS 5.0 (May 2025) |
| `03_repos/owasp-cheatsheets` | https://github.com/OWASP/CheatSheetSeries | — | Full Cheat Sheet Series |
| `03_repos/owasp-secure-agent-playbook` | https://github.com/OWASP/secure-agent-playbook | — | AI-assisted security plays |
| `03_repos/owasp-wstg` | https://github.com/OWASP/www-project-web-security-testing-guide | — | WSTG v5.0 |
| `03_repos/payloads-all-the-things` | https://github.com/swisskyrepo/PayloadsAllTheThings | — | 63+ vuln categories |
| `03_repos/payloadsallthethings-skills` | https://github.com/mohdhaji87/payloadsallthethings-skills | 21 | 61 skills from PATT |
| `03_repos/perseus` | https://github.com/kaivyy/perseus | 67 | Multi-language security assessment |
| `03_repos/secskills` | https://github.com/trilwu/secskills | 111 | Security skills (offense/defense/core) |
| `03_repos/security-skills` | https://github.com/mn-youssef/security-skills | 40 | Defensive + offensive skills |
| `03_repos/threatswarm` | https://github.com/mukul975/Threatswarm | 66 | 27 agents, 754 MITRE-mapped skills |
| `03_repos/trailofbits-skills` | https://github.com/trailofbits/skills | 6655 | 79 security skills |
| `03_repos/shuvonsec-claude-bug-bounty` | https://github.com/shuvonsec/claude-bug-bounty | 4256 | AI bug bounty hunting |
| `03_repos/H-mmer-pentest-agents` | https://github.com/H-mmer/pentest-agents | 802 | 48 agents, exploit chains |
| `03_repos/MyuriKanao-src-hunter-skill` | https://github.com/MyuriKanao/src-hunter-skill | 599 | 305 payloads, 263 WAF bypasses |
| `03_repos/transilienceai-communitytools` | https://github.com/transilienceai/communitytools | 476 | Open-source pentest skills |
| `03_repos/Gabson0x-bountyforge` | https://github.com/Gabson0x/bountyforge | 383 | Bug bounty + smart contracts |
| `03_repos/shuvonsec-public-skills-builder` | https://github.com/shuvonsec/public-skills-builder | 221 | Generate skills from HackerOne reports |
| `03_repos/h4ckologic-bughunter-ai` | https://github.com/h4ckologic/bughunter-ai | 64 | 20 AI agents, state-machine |
| `03_repos/gigioneggiando-argo` | https://github.com/gigioneggiando/argo | 53 | LLM-native static vuln detection |
| `03_repos/0xGhostCAT-claude-ai-cyber-security-skills` | https://github.com/0xGhostCAT/claude-ai-cyber-security-skills | 36 | 30 skills + 60 tools |
| `03_repos/26zl-cybersec-toolkit` | https://github.com/26zl/cybersec-toolkit | 40 | 670+ tools, 870+ skills |
| `03_repos/Orizon-eu-claude-code-pentest` | https://github.com/Orizon-eu/claude-code-pentest | 23 | 6 skills, full pentest lifecycle |

## Re-clone script

To restore all repos, run:

```bash
while IFS='|' read -r dir url stars desc; do
  [[ "$dir" =~ ^# ]] && continue
  dir=$(echo "$dir" | xargs)
  url=$(echo "$url" | xargs)
  [ -z "$url" ] && continue
  echo "Cloning $dir ..."
  git clone --depth 1 "$url" "$dir"
done < <(grep "^|" REPO_MANIFEST.md | grep -v "Directory")
```
