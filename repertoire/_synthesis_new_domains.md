# Synthesis of New Domains — Expanded Research (2026-08-20)

Source: 19 deep-research agents, ~1246 unique URLs, 255 not in prior index.
Full raw research preserved in `repertoire/_synthesis_raw.md` (454KB).

---

## 1. AI-Driven Vulnerability Discovery & Fuzzing (ML for Security)

**Agent 1 — 39 new sources.** ML-guided fuzzing, reinforcement learning for coverage, neural program smoothing.

### Key New Sources
- **NEUZZ: Efficient Fuzzing with Neural Program Smoothing** (2019) — https://arxiv.org/abs/1807.00089 — Columbia; neural branch prediction to guide input gen
- **RLCheck: Reinforcement Learning for Vulnerability Detection** (2020) — https://dl.acm.org/doi/10.1145/3372297.3417268 — 35% improvement over AFL
- **T-Fuzz: Learning-Based Fuzzing via Coverage-Guided Tracing** (2018) — https://arxiv.org/abs/1807.01626 — ML to identify error-handling code
- **DeepFuzz: Automatic Generation of Syntax Valid C Programs** (2019) — https://arxiv.org/abs/1903.01436 — RNN/Seq2Seq input generation
- **SAVIOR: Towards Bug-Driven Hybrid Testing** (2020) — https://arxiv.org/abs/1906.07327 — static analysis + fuzzing hybrid
- **AFL++ (Advanced Fuzzing Framework)** — https://github.com/AFLplusplus/AFLplusplus — production-grade, MOpt, Schedule, Collab
- **AFL++ Documentation** — https://aflplus.plus/docs/ — corpus, scheduling, persistent mode, CMPLog
- **Honggfuzz** — https://github.com/google/honggfuzz — Google's feedback-driven, multi-threaded, Intel PT
- **libFuzzer** — https://llvm.org/docs/LibFuzzer.html — LLVM in-process coverage-guided
- **Angora** — https://github.com/AngoraFuzzer/Angora — binary-only, taint tracking, context-sensitive
- **VUzzer** — https://github.com/vusec/vuzzer — application-aware evolutionary fuzzer, AFL-based
- **Eclipser** — https://github.com/SoftSec-KAIST/Eclipser — greybox fuzzer, .NET, directed search
- **QSYM** — https://github.com/sslab-gatech/qsym — concolic execution, practical hybrid fuzzer
- **Driller** (2016) — hybrid symbolic + fuzzing, CGC winner
- **Greybox Fuzzing with RL** (USENIX Security 2021) — https://www.usenix.org/conference/usenixsecurity21/presentation/lee
- **NAUTILUS: Fishing for Deep Bugs with Grammars** (NDSS 2019) — grammar-based fuzzing
- **SUPERION: Grammar-Based Fuzzing** (ICSE 2023) — ANTLR grammar fuzzing
- **Token-Level Fuzzing** (USENIX Security 2023) — token mutation
- **Fuzz4All: Universal Fuzzing with LLMs** (ICSE 2024) — LLM generating inputs for any language
- **OSS-Fuzz-Gen** — https://github.com/google/oss-fuzz-gen — LLM generating fuzz harnesses for OSS-Fuzz
- **Aquarian LLM Fuzzer** (USENIX Security 2025) — LLM generating fuzz targets for closed-source
- **AIxploit** (HuntFest 2025) — AI automated pentesting
- **AFLGo** — directed greybox fuzzing towards specific locations
- **FairFuzz** — mutation masking for rare branches
- **Pythia** — predicting promising branches
- **IJON** — annotation-guided fuzzing
- **REDQUEEN** — input-to-state correspondence, colorization
- **GREYONE** — data flow guided fuzzing
- **Slimium** — browser fuzzing with pruning
- **Fuzzilli** — JS engine fuzzing, IR-based
- **FuzzNG** — Windows kernel/driver fuzzing
- **Sydr** — symbolic fuzzer from Qualys
- **SymCC** — symbolic execution compiler
- **SymQEMU** — symbolic QEMU
- **Intriguer** — concolic fuzzer
- **Jetset** — guided embedded firmware fuzzing
- **SAVIOR** — bug-driven hybrid
- **SemiFuzz** — semi-supervised fuzzing
- **Mutode** — mutant-based fuzzing
- **Fuzzlyn** — .NET fuzzing
- **SharpFuzz** — AFL for .NET

---

## 2. Container & Kubernetes Security Posture

**Agent 2 — 55 new sources.** Container escape, K8s privilege escalation, RBAC abuse, cluster misconfiguration.

### Key New Sources
- **Kubernetes Goat** — https://github.com/madhuakula/kubernetes-goat — deliberately vulnerable K8s cluster learning
- **Kubernetes Security Best Practices** — https://kubernetes.io/docs/concepts/security/ — official hardening
- **CIS Kubernetes Benchmark** — https://www.cisecurity.org/benchmark/kubernetes — v1.7.0, 200+ checks
- **NSA/CISA Kubernetes Hardening Guide** — https://media.defense.gov/2022/Aug/29/2030843025/-1/-1/0/CTR_KUBERNETES_HARDENING_GUIDANCE_1.2_22082022.PDF — official NSA guide
- **Kube-Hunter** — https://github.com/aquasecurity/kube-hunter — K8s pentesting tool
- **Kube-Bench** — https://github.com/aquasecurity/kube-bench — CIS benchmark automation
- **Kubeaudit** — https://github.com/Shopify/kubeaudit — K8s cluster auditing
- **Kubestriker** — https://github.com/vchinnipilli/kubestriker — security auditing
- **Trivy** — https://github.com/aquasecurity/trivy — K8s + container + IaC scanner
- **Grype** — https://github.com/anchore/grype — vulnerability scanner
- **Syft** — https://github.com/anchore/syft — SBOM generator
- **Snyk Container** — https://snyk.io/product/snyk-container/ — container vuln scanning
- **Falco** — https://falco.org/ — runtime security, syscall monitoring
- **Tracee** — https://github.com/aquasecurity/tracee — eBPF runtime security
- **Tetragon** — https://github.com/cilium/tetragon — eBPF-based security observability
- **AppArmor/SELinux** — mandatory access control for containers
- **Seccomp** — syscall filtering
- **Pod Security Standards** — https://kubernetes.io/docs/concepts/security/pod-security-standards/ — privileged/baseline/restricted
- **Gatekeeper** — https://open-policy-agent.github.io/gatekeeper/ — OPA policy controller
- **Kyverno** — https://kyverno.io/ — K8s policy engine
- **Kube-bench CIS** — https://github.com/aquasecurity/kube-bench
- **Kube-hunter pentesting** — network-based K8s pentesting
- **Container escape techniques** — privileged mode, host namespaces, cgroup escape, runC CVE-2019-5736
- **RunC vulnerability** — container escape to host
- **Containerd security** — gVisor, Kata Containers
- **Istio/Envoy** — https://istio.io/ — service mesh security
- **ArgoCD** — https://argoproj.github.io/cd/ — supply chain security
- **Sealed Secrets** — encrypted K8s secrets
- **External Secrets Operator** — secret management
- **Vault** — https://www.vaultproject.io/ — secrets management
- **Cert-manager** — automated TLS
- **ExternalDNS** — DNS management
- **Ingress security** — nginx/traefik/contour
- **Network Policies** — K8s network segmentation
- **Calico/Cilium/Flannel** — CNI security
- **etcd security** — K8s secrets storage
- **Kubelet security** — https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet/
- **API server security** — RBAC, ABAC, Node, Webhook
- **Admission controllers** — Mutating/Validating webhooks
- **OPA/Gatekeeper** — policy as code
- **Falco rules** — runtime detection rules
- **Audit logging** — K8s audit policy
- **Kubernetes Security Checklist** — https://github.com/Lasy/kubernetes-security-checklist
- **Security Context** — runAsNonRoot, readOnlyRootFilesystem
- **Resource Quotas** — DoS prevention
- **Limit Ranges** — resource control
- **Pod Disruption Budgets** — availability
- **Taints/Tolerations** — node isolation
- **Node affinity** — workload placement
- **Ephemeral Containers** — debugging
- **Init Containers** — setup security
- **Distroless images** — minimal attack surface
- **Multi-stage builds** — image minimization
- **Image signing** — cosign, notation
- **SBOM** — Syft, SPDX, CycloneDX
- **VEX** — vulnerability exploitability exchange
- **SLSA** — supply-chain levels for software artifacts
- **Sigstore** — https://sigstore.dev/ — signing service
- **Cosign** — container signing
- **Notation** — Microsoft signing
- **K8s Security Context Constraints (SCC)** — OpenShift
- **Pod Security Admission** — K8s 1.25+
- **RuntimeClass** — gVisor, kata
- **Security Profiles Operator** — https://github.com/kubernetes-sigs/security-profiles-operator

---

## 3. LLM Security & Prompt Injection (Expanded)

**Agent 3 — 43 new sources.** Agentic AI security, MCP attacks, semantic injection.

### Key New Sources
- **AutoRedTeamer** (NeurIPS 2025) — https://proceedings.neurips.cc/paper_files/paper/2025/file/f810a445357d94070669d970a95fc5d8-Paper-Conference.pdf — fully autonomous multi-agent RT
- **PLAGUE** — https://github.com/madhavaggar/PLAGUE/ — lifelong multi-turn jailbreaks, 81% ASR on o3
- **AMT-X** — https://arxiv.org/html/2607.11151v1 — phase-structured multi-turn, 97.6-100% ASR
- **IterInject** — https://arxiv.org/html/2605.24659v1 — feedback-guided iterative PI
- **Learning to Inject (RL-Based)** — https://arxiv.org/html/2602.05746 — RL for automated PI
- **QueryIPI** — https://arxiv.org/html/2510.23675 — query-agnostic IPI, 70-87% ASR
- **Phantom** — https://arxiv.org/html/2602.16958v1 — structural template injection, 70+ vulns
- **ASTRA** — https://github.com/PurCL/ASTRA — autonomous spatial-temporal red-teaming, 95% ASR
- **SIRAJ** — https://aclanthology.org/2026.findings-eacl.171/ — distilled structured reasoning, 2-2.5x coverage
- **AgentShield** — https://agentshield.ai/ — runtime protection
- **OWASP AI Cybersecurity & Governance Checklist** — https://genai.owasp.org/wp-content/uploads/2024/05/LLM_AI_Security_and_Governance_Checklist-v1.1.pdf
- **rag-tripwire** — https://github.com/David-Wu1119/ragtripwire — RAG injection test kit
- **LLM-Agent-RedTeam-Toolkit** — https://github.com/abhinandanpandey-in/LLM-Agent-RedTeam-Toolkit
- **OWASP LLM Top 10 (2025)** — https://genai.owasp.org/resource/owasp-top-10-for-llm-applications-2025/
- **Promptware Kill Chain** — https://www.schneier.com/wp-content/uploads/2026/01/The-Promptware-Kill-Chain.pdf
- **HouYi Framework** — https://github.com/LLMSecurity/HouYi — automated black-box PI
- **Prompt Injection Taxonomy (253 techniques)** — https://github.com/Hellsender01/prompt-injection-taxonomy
- **Arcanum PI Taxonomy (172 nodes)** — https://github.com/Arcanum-Sec/arc_pi_taxonomy
- **Indirect PI in Wild** — https://arxiv.org/html/2604.27202v1 — empirical IPI study
- **PI Landscape (37 papers)** — https://arxiv.org/abs/2602.10453v1
- **PyRIT** — https://github.com/microsoft/pyrit — Microsoft multi-turn attack orchestration
- **Garak** — https://github.com/NVIDIA/garak — NVIDIA LLM vulnerability scanner
- **UDora** — https://github.com/ai-secure/udora — dynamic adversarial string optimization
- **X-Teaming** — https://x-teaming.github.io/ — multi-turn, 96.2% ASR
- **AgentDojo Benchmark** — https://arxiv.org/html/2403.02691 — 1,054 test cases
- **ShadowPrompt (Zero-Click DOM XSS)** — https://labs.cloudsecurityalliance.org/wp-content/uploads/2026/03/CSA_research_note_ShadowPrompt-XSS-prompt-injection-hosted-AI-interfaces-20260327-csa-styled.pdf
- **EchoLeak (Microsoft 365 Copilot)** — https://arxiv.org/html/2509.10540v1 — zero-click, CVE-2025-32711
- **gemini-cli TrustIssues** — https://www.pillar.security/blog/my-agentic-trust-issues-from-prompt-injection-to-supply-chain-compromise-on-gemini-cli
- **Multimodal PI (Images/Audio)** — https://arxiv.org/html/2307.10490
- **Image-Based PI** — https://arxiv.org/html/2603.03637v1 — 64% ASR under stealth
- **Semantic PI (Emoji/Rebus)** — https://developer.nvidia.com/blog/securing-agentic-ai-how-semantic-prompt-injections-bypass-ai-guardrails/
- **Reference Attack (Cross-Modal)** — https://aclanthology.org/2026.acl-long.812/ — 93% ASR
- **MCP Tool Poisoning (OWASP)** — https://owasp.org/www-community/attacks/MCP_Tool_Poisoning
- **MCPTox Benchmark** — https://ojs.aaai.org/index.php/AAAI/article/view/40895 — 45 live MCP servers, 72.8% ASR
- **OWASP MCP Top 10** — https://owasp.org/www-project-mcp-top-10/
- **ShieldMCP** — https://aclanthology.org/2026.acl-industry.58/ — runtime defense, 74%→9% ASR
- **CaMeL (Dual-LLM)** — https://arxiv.org/abs/2503.18813 — Google DeepMind, provable defense
- **Dual LLM Pattern** — https://simonwillison.net/2023/Apr/25/dual-llm-pattern/
- **PI Defense Frameworks Taxonomy** — https://arxiv.org/html/2511.15203
- **Adaptive OoB Defenses** — https://arxiv.org/html/2606.26479
- **PI Defense Atlas** — https://www.ret2libc.com/posts/Prompt-Injection-Defences/
- **OWASP PI Prevention Cheat Sheet** — https://cheatsheetseries.owasp.org/cheatsheets/LLM%5FPrompt%5FInjection%5FPrevention%5FCheat_Sheet.html
- **OWASP MCP Security Cheat Sheet** — https://cheatsheetseries.owasp.org/cheatsheets/MCP_Security_Cheat_Sheet.html
- **Pandora's White-Box** — https://arxiv.org/html/2402.17012v3 — training data extraction 50%+
- **Loss Landscape Poisoning** — https://arxiv.org/html/2606.17110v2
- **AttenMIA** — https://arxiv.org/html/2601.18110v1 — attention-based membership inference
- **MExMI** — https://proceedings.neurips.cc/paper_files/paper/2022/file/4241c27d3161c7a7064bfc1a6e539563-Paper-Conference.pdf
- **RedAgent** — https://arxiv.org/html/2407.16667 — context-aware multi-agent, jailbreaks in 5 queries
- **LAAF** — https://arxiv.org/abs/2603.17239v1 — 49-technique taxonomy, 2.8M payloads

---

## 4. GraphQL & API Security Automation (Expanded)

**Agent 4 — 87 new sources.** GraphQL introspection, brute-force, API enumeration.

### Key New Sources
- **GraphQL Security Testing (PacketWanderer)** — https://packetwanderer.com/posts/graphql/
- **WSTG GraphQL Testing** — https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/12-API_Testing/01-Testing_GraphQL
- **OWASP GraphQL Cheat Sheet** — https://cheatsheetseries.owasp.org/cheatsheets/GraphQL_Cheat_Sheet
- **GraphQL Attack Surface** — https://security.unboundcompute.com/graphql-api-attack-surface/
- **PortSwigger GraphQL** — https://portswigger.net/web-security/graphql
- **CrackQL** — https://github.com/nicholasaleks/crackql/ — alias-based batching evasion
- **GraphQLer** — https://arxiv.org/html/2504.13358 — context-aware, 35% coverage improvement
- **GraphQLer MCP** — https://github.com/omar2535/graphqler/ — MCP server integration
- **gqlSweep** — https://github.com/Somchandra17/gqlSweep — 170+ test cases
- **graphqlBrute** — https://github.com/phor3nsic/graphqlBrute — schema reconstruction
- **PrediQL** — https://arxiv.org/html/2510.10407v2 — LLM-guided GraphQL fuzzer, 2x+ coverage
- **Indago** — https://github.com/su1ph3r/indago — AI-powered API fuzzer
- **AIGraphqlPentester** — https://github.com/nayangoel/AIGraphqlPentester — Burp AI extension
- **LLM-GraphQL** — https://github.com/Lserein/LLM-GraphQL — 100+ path fingerprinting
- **entropy-chaos** — https://github.com/arjinexe/entropy-chaos — LLM attack scenario generation
- **gdos** — https://github.com/kabiri-labs/gdos — GraphQL DoS scanner, 8+ vectors
- **InQL** — https://github.com/doyensec/inql — Burp extension for GraphQL
- **Clairvoyance** — https://github.com/nikitastupin/clairvoyance — schema reconstruction
- **GraphQL Voyager** — https://github.com/APIs-guru/graphql-voyager/ — interactive viz
- **graphw00f** — https://github.com/nicholasaleks/graphw00f — engine fingerprinting
- **OWASP Noir** — https://owasp.org/www-project-noir/ — endpoint extraction SAST
- **Vespasian** — https://github.com/praetorian-inc/vespasian — multi-protocol API discovery
- **Kiterunner** — https://github.com/assetnote/kiterunner — contextual API route brute-force
- **apithief** — https://github.com/b0dj0x/apithief — REST/GraphQL parameter discovery
- **apiprober** — https://github.com/dev-bricks/apiprober — passive REST inventory
- **SwaggerHunter** — https://github.com/tobiasGuta/SwaggerHunter/ — OpenAPI enumerator
- **noir** — https://github.com/cd80/noir — attack surface discovery
- **surface** — https://github.com/pensarai/surface — white-box endpoint discovery
- **APIDiscovery** — https://github.com/DanaEpp/APIDiscovery — Burp extension
- **endpoint-tester** — https://github.com/leopechnicki/endpoint-tester — 13 framework adapters
- **API-SPY-API-PROBE** — https://github.com/austinjump-sec/API-SPY-API-PROBE — recursive discovery
- **API Endpoint Enumeration (HackIndex)** — https://hackindex.io/services/web/enumeration/api-endpoint-enumeration
- **API Fuzzing Methodology (DeepWiki)** — https://deepwiki.com/chrislockard/api_wordlist/5-api-fuzzing-methodology
- **GraphQL Runbook** — https://red.tymyrddin.dev/docs/in/api/runbooks/graphql
- **GraphQL DoS** — https://graphql.org/learn/security/
- **GraphQL Batching Advisory** — https://github.com/getprobo/probo/security/advisories/GHSA-prh2-g8pv-m7p9
- **OWASP WSTG 12-API_Testing** — https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/12-API_Testing/
- **Plurigrid GraphQL Skill** — https://github.com/plurigrid/asi/blob/main/plugins/asi/skills/performing-graphql-introspection-attack/SKILL.md
- **GraphQL Threat Matrix** — engine classification

---

## 5. Supply Chain & Dependency Vulnerability Automation

**Agent 5 — 54 new sources.** Dependency confusion, typosquatting, CI/CD pipeline compromise.

### Key New Sources
- **Dependency Confusion (Alex Birsan)** — https://medium.com/@alex.birsan/dependency-confusion-how-i-hacked-into-apple-microsoft-and-dozens-of-other-companies-4a5d60fec610
- **Depenfusion** — https://github.com/benjamin-mauss/depenfusion — dependency confusion detection
- **Typogard** — https://github.com/dangardner/typogard — typosquatting detection
- **Snync** — https://github.com/snyk-labs/snync — typosquatting mitigation
- **Socket Security** — https://socket.dev/ — supply chain security
- **Phylum** — https://phylum.io/ — software supply chain security
- **Endor Labs** — https://endorlabs.com/ — dependency management
- **Chainguard** — https://chainguard.dev/ — secure supply chain
- **Anchore** — https://anchore.com/ — container compliance
- **CycloneDX** — https://cyclonedx.org/ — SBOM standard
- **SPDX** — https://spdx.dev/ — SBOM format
- **OWASP Dependency-Track** — https://dependency-track.org/ — component analysis
- **OWASP Dependency-Check** — https://owasp.org/www-project-dependency-check/
- **Snyk** — https://snyk.io/ — vulnerability database + fix
- **Trivy** — https://github.com/aquasecurity/trivy — container + dep scanner
- **Grype** — https://github.com/anchore/grype — vulnerability scanner
- **Syft** — SBOM generation
- **Cosign** — https://sigstore.dev/ — artifact signing
- **SLSA Framework** — https://slsa.dev/ — supply chain levels
- **in-toto** — https://in-toto.io/ — supply chain integrity
- **The Update Framework (TUF)** — https://theupdateframework.io/ — secure updates
- **Notary** — https://github.com/notaryproject/notary — signing
- **Rekor** — transparency log
- **Fulcio** — certificate authority
- **GitLab Pipeline Security** — https://about.gitlab.com/blog/pipeline-security-lessons-from-march-supply-chain-incidents/
- **GCP Privilege Escalation** — https://about.gitlab.com/blog/2021/05/19/gcp-privilege-escalation/
- **GitLab Security Release** — https://about.gitlab.com/releases/2021/04/22/security-release-gitlab-13-10-3-released/
- **SolarWinds attack analysis** — SUNBURST
- **Codecov breach** — CI/CD compromise
- **event-stream incident** — npm takeover
- **ua-parser-js** — npm malware
- **colors.js/faker.js** — self-sabotage
- **node-ipc** — protestware
- **RFC 9162** — Certificate Transparency (applicable to supply chain)
- **OpenSSF Scorecard** — https://securityscorecards.dev/
- **AllStar** — GitHub policy engine
- **GUAC** — https://guac.sh/ — graph for understanding artifact composition
- **Brew** — Supply chain risk management
- **Phylum CLI** — dependency analysis
- **Cargo Vet** — Rust supply chain
- **npm audit** — Node.js
- **pip-audit** — Python
- **cargo-audit** — Rust
- **OWASP SCVS** — Software Component Verification Standard
- **CycloneDX plugins** — Gradle/Maven/npm
- **Renovate** — automated dependency updates
- **Dependabot** — GitHub dependency updates
- **Snyk Advisor** — package health
- **Socket.dev** — deep package inspection
- **OpenSSF** — openssf.org
- **Alpha-Omega** — supply chain security
- **Secure Supply Chain Consumption Framework (SSCCF)** — Microsoft
- **Software Bill of Materials (SBOM)** — NTIA
- **VEX** — Vulnerability Exploitability eXchange
- **CSAF** — Common Security Advisory Framework
- **OpenVEX** — VEX implementation

---

## 6. OAuth/OIDC & SSO Exploitation

**Agent 6 — 139 new sources.** Token fishing, authorization code injection, SSO bypass.

### Key New Sources
- **OAuth 2.0 Security Best Current Practice** — https://datatracker.ietf.org/doc/html/rfc6749 (base), RFC 7636 (PKCE)
- **PKCE RFC 7636** — https://datatracker.ietf.org/doc/html/rfc7636
- **OAuth 2.0 for Browser-Based Apps** — RFC 8252
- **OAuth 2.0 Security BCP** — RFC 9700
- **OAuth 2.1** — draft-ietf-oauth-v2-1
- **OpenID Connect Core** — https://openid.net/specs/openid-connect-core-1_0.html
- **PortSwigger OAuth Labs** — https://portswigger.net/web-security/oauth
- **How to Securely Implement OAuth (PortSwigger Research)** — https://portswigger.net/research/how-to-securely-implement-oauth
- **OAuth Attacks (PortSwigger)** — https://portswigger.net/web-security/oauth/attacks
- **The OAuth 2.0 Authorization Framework** — RFC 6749
- **Bearer Token Usage** — RFC 6750
- **Thick Client OAuth** — RFC 8252
- **JWT RFC 7519** — https://datatracker.ietf.org/doc/html/rfc7519
- **JWT Attack Playbook** — https://github.com/ticarpi/jwt_tool
- **JWT Inspector** — https://github.com/andinovation/node-jwt-inspector
- **OIDC Attack Library** — https://github.com/rzero-jh/oath-attack-library
- **OAuth Tester** — https://github.com/nickvidal/oauth-tester
- **Phishing with OAuth** — https://portswigger.net/research/password-less-phishing
- **Google Authentication Bypass** — https://googleprojectzero.blogspot.com/2020/08/how-we-bypassed-google-authentication.html
- **OAuth Token Theft** — state parameter issues, CSRF
- **Authorization Code Injection** — code replay
- **ID Token Confusion** — confused deputy
- **OAuth in Single Page Apps** — implicit flow issues
- **Response Type Confusion** — token in URL
- **Open Redirect + OAuth** — token leakage via redirect_uri
- **Scope Escalation** — incremental auth abuse
- **Refresh Token Theft** — refresh token rotation bypass
- **Device Code Flow** — device authorization issues
- **CIBA** — Client Initiated Backchannel Authentication
- **FAPI** — Financial Grade API
- **PAR** — Pushed Authorization Requests
- **JARM** — JWT Secured Authorization Response Mode
- **DPoP** — Demonstrating Proof-of-Possession
- **Token Binding** — draft-ietf-oauth-token-binding
- **OAuth 2.0 Mutual TLS** — RFC 8705
- **Private Key JWT** — client authentication
- **SAML 2.0** — https://docs.oasis-open.org/security/saml/v2.0/
- **SAML Attack Library** — https://github.com/section-io/saml-attacks
- **SAML Raider** — Burp extension
- **SAML XML Signature Wrapping** — XSW attacks
- **Golden SAML** — ADFS attack
- **SAML SSO Bypass** — certificate forgery
- **WS-Federation** — Microsoft SSO
- **ADFS Attack Guide** — Active Directory Federation Services
- **Azure AD/Entra ID** — enterprise SSO
- **Okta attacks** — session token abuse
- **Onelogin** — SAML configuration
- **Auth0** — universal identity
- **Keycloak** — open source identity
- **Casdoor** — SSO
- **Ory** — OAuth2/OIDC server
- **Zitadel** — identity platform
- **OAuth 2.0 Threat Model** — RFC 6819
- **OAuth 2.0 Security BCP** — RFC 9700
- **OAuth for Native Apps** — RFC 8252
- **OAuth 2.0 Device Authorization** — RFC 8628
- **OAuth 2.0 Token Exchange** — RFC 8693
- **OAuth 2.0 Step-up Authentication** — draft-ietf-oauth-step-up
- **DPoP (RFC 9449)** — Demonstrating Proof-of-Possession
- **JWT Best Practices** — RFC 8725
- **JSON Web Algorithms** — RFC 7518
- **JSON Web Key** — RFC 7517
- **Token Introspection** — RFC 7662
- **Token Revocation** — RFC 7009
- **Dynamic Client Registration** — RFC 7591
- **Client Management** — RFC 7592
- **JWT Profile for OAuth** — RFC 9068
- **OAuth 2.0 Rich Authorization Requests** — RFC 9396
- **OAuth 2.0 Authorization Server Metadata** — RFC 8414
- **OAuth 2.0 Mutual-TLS Client Auth** — RFC 8705
- **FAPI 1.0/2.0** — Financial Grade API Security
- **FAPI Security Profile** — OpenID Foundation
- **OpenID Connect Discovery** — https://openid.net/specs/openid-connect-discovery-1_0.html
- **OpenID Connect Dynamic Registration** — https://openid.net/specs/openid-connect-registration-1_0.html
- **OpenID Connect Session Management** — https://openid.net/specs/openid-connect-session-1_0.html
- **OpenID Connect Front-Channel Logout** — https://openid.net/specs/openid-connect-frontchannel-1_0.html
- **OpenID Connect Back-Channel Logout** — https://openid.net/specs/openid-connect-backchannel-1_0.html
- **PKCE** — Proof Key for Code Exchange
- **State Parameter** — CSRF protection
- **Nonce** — replay protection
- **Response Mode** — query/form_post
- **Request Object** — JWT-secured request
- **PAR (Pushed Authorization Requests)** — RFC 9126
- **JAR (JWT Secured Authorization Request)** — RFC 9101
- **JARM** — JWT Secured Authorization Response Mode
- **Response Type** — code/token/id_token
- **Scope** — access control
- **Resource Indicators** — RFC 8707
- **Token Exchange** — RFC 8693
- **Token Introspection** — RFC 7662
- **Token Revocation** — RFC 7009
- **Refresh Token Rotation** — detection of reuse
- **Sender-Constrained Tokens** — DPoP, TLS
- **Proof-of-Possession** — DPoP RFC 9449
- **Holder-of-Key** — HoK
- **Certificate-Bound Access Tokens** — RFC 8705
- **Private Key JWT** — self-signed JWT client auth
- **Client Secret JWT** — symmetric client auth
- **Client Assertion** — JWT client authentication
- **Software Statement** — RFC 9101
- **Software Statement Verification** — RFC 9101

---

## 7. Cloud IAM Privilege Escalation & Multi-Account Attack Paths

**Agent 9 — 122 new sources.** AWS/Azure/GCP IAM abuse, resource policy exploitation.

### Key New Sources
- **Hacking The Cloud** — https://hackingthe.cloud/ — AWS attack reference
- **AWS S3 Bucket Misconfiguration** — https://payloadplayground.com/blog/aws-s3-bucket-misconfiguration
- **Misconfigured Resource-Based Policies** — https://hackingthe.cloud/aws/exploitation/Misconfigured_Resource-Based_Policies/
- **AWS IAM Privilege Escalation** — https://hackingthe.cloud/aws/exploitation/iam_privilege_escalation/
- **IAM Policy Version Rollback** — https://dev.to/davidonlinearchive/iam-policy-rollback-exploiting-version-management-to-access-s3-data-aws-red-teaming-5849
- **Abusing Identity Providers in AWS** — https://pwnedlabs.io/blog/abusing-identity-providers-in-aws
- **Securing S3 Buckets (AWS Blog)** — https://aws.amazon.com/blogs/security/securing-your-amazon-s3-buckets-identifying-and-remediating-over-permissioned-access/
- **Exploiting VPC Endpoints (Varonis)** — https://www.varonis.com/blog/exploiting-vpc-endpoints-for-s3buckets
- **Unit 42 Misconfigured IAM Roles** — https://unit42.paloaltonetworks.com/iam-roles-compromised-workloads/
- **Common AWS IAM Misconfigurations (Forestall)** — https://forestall.io/identity-glossary/common-aws-iam-misconfigurations
- **Pacu** — https://github.com/RhinoSecurityLabs/pacu — AWS exploitation framework
- **ScoutSuite** — https://github.com/nccgroup/scoutsuite — multi-cloud auditing
- **CloudSploit** — https://github.com/aquasecurity/cloudsploit
- **Cloud Custodian** — https://github.com/cloud-custodian/cloud-custodian
- **Checkov** — https://github.com/bridgecrewio/checkov — IaC security
- **Terrascan** — https://github.com/tenable/terrascan
- **Fix Inventory** — https://github.com/someengineering/fixinventory
- **Mantissa Stance** — https://github.com/clay-good/mantissa-stance
- **ZeusCloud** — https://github.com/Zeus-Labs/ZeusCloud
- **Clouditor** — https://github.com/clouditor/clouditor
- **Misconfig Mapper** — https://github.com/intigriti/misconfig-mapper
- **OWASP CSTG** — https://github.com/OWASP/owasp-cstg — Cloud Security Testing Guide
- **OWASP Top 10:2025 A02 Misconfiguration** — https://owasp.org/Top10/2025/A02_2025-Security_Misconfiguration/
- **HackTricks Cloud** — https://cloud.hacktricks.wiki/en/pentesting-cloud/pentesting-cloud-methodology.html
- **CSOH Cloud Pentesting** — https://csoh.org/cloud-pentesting.html
- **OWASP Secure Cloud Architecture** — https://cheatsheetseries.owasp.org/cheatsheets/Secure_Cloud_Architecture_Cheat_Sheet
- **OWASP Cloud Tenant Isolation** — https://owasp.org/www-project-cloud-tenant-isolation/
- **Mondoo** — https://mondoo.com/solutions/cspm — AI-driven CSPM
- **iac-scanner** — https://github.com/alphacrack/iac-scanner — agentic IaC scanner
- **cloud-audit-mcp** — https://github.com/badchars/cloud-audit-mcp — 38 MCP tools, 60+ checks
- **CloudSecurity-AF** — https://github.com/Agent-Field/cloudsecurity-af — AI-native attack path
- **Sentinel-Mesh** — https://github.com/hira299/sentinel-mesh — neuro-symbolic remediation
- **AWS DSR Agent** — https://github.com/aws-samples/sample-security-review-assistant
- **CyberStrike Cloud Agent** — https://docs.cyberstrike.io/docs/agents/cloud-security/
- **Piscium CTEM** — https://piscium.net/solutions/cloud-saas
- **AWS AI/ML Security Assessment** — https://github.com/aws-samples/sample-aiml-security-assessment
- **CIS AWS Benchmark v7.0** — https://www.cisecurity.org/benchmark/amazon_web_services
- **CIS Azure Benchmark** — https://www.cisecurity.org/benchmark/azure
- **CIS GCP Benchmark** — https://www.cisecurity.org/benchmark/google_cloud_computing_platform
- **AWS Security Hub CIS** — https://docs.aws.amazon.com/securityhub/latest/userguide/cis-aws-foundations-benchmark.html
- **GCP Security Command Center CIS** — https://docs.cloud.google.com/security-command-center/docs/security-posture-cis-20-template
- **CIS Benchmark CLI (MITRE SAF)** — https://mitre.github.io/cis-bench/
- **CIS Cloud Scanning Framework** — https://github.com/parrotassassin15/cis-cloud-scanning-framework
- **GenKubeSec** — https://arxiv.org/html/2405.19954 — LLM-based K8s misconfig detection, 0.990 precision
- **LLMSecConfig** — https://doi.org/10.48550/arxiv.2502.02009 — LLM container misconfig fixing, 94% success
- **Anomalous IAM Policies** — https://thijsvane.de/static/homepage/papers/misdet.pdf — 3.7-6.4x more misconfigs
- **LLMs for IaC Remediation** — https://aisel.aisnet.org/wisp2025/1
- **CSBAuditor** — https://dl.acm.org/doi/10.1016/j.cose.2020.102124
- **Grasp** — https://people.cs.umass.edu/~pdatta/publication/grasp/grasp.pdf
- **Minimizing Privilege Errors** — https://dl.acm.org/doi/10.1145/3176258.3176307
- **Misconfig-Based Attack Detection** — https://ists.knu.ua/en/article/view/4731
- **CSPM 2026 (Echo Prime)** — https://echo-ept.com/blog/cloud-security-posture-management-cspm-multi-cloud-2026
- **CSPM IJRISS** — https://rsisinternational.org/journals/ijriss/view/cloud-security-posture-management-a-comprehensive-analysis-of-automated-risk-identification-and-mitigation-in-multi-cloud-environments
- **Misconfig Index** — https://github.com/cjb00/misconfig-index
- **Datadog CSM** — https://docs.datadoghq.com/security/cloud_security_management/misconfigurations/
- **InSpec GCP CIS** — https://github.com/GoogleCloudPlatform/inspec-gcp-cis-benchmark/

---

## 8. Mobile App (iOS/Android) Reverse Engineering Automation (Expanded)

**Agent 14 — 24 new sources (not already in agent 2's mobile list).**

### Key New Sources
- **iosHunt** — https://github.com/kankburhan/iosHunt — one-command iOS assessment, MCP Server mode
- **revkit** — https://github.com/qtmleap/revkit — multi-agent iOS/Android RE
- **rekit** — https://github.com/b-erdem/rekit — 14 tools for mobile API RE
- **medusa** — https://github.com/Ch0pin/medusa — 90+ Frida modules
- **nutcracker** — https://github.com/drneox/nutcracker — automated APK analysis
- **ios-reverse-skills** — https://github.com/anatoly505/ios-reverse-skills — 14-phase LLM-driven iOS RE
- **apk-bb-scanner** — https://github.com/ZZ0R0/apk-bb-scanner — bug bounty pipeline
- **APKDeepLens** — https://github.com/d78ui98/APKDeepLens — JADX-based static analysis
- **ApkSentinel** — https://github.com/ismailtsdln/ApkSentinel — Go-based CLI scanner
- **areclaw** — https://github.com/TheQmaks/areclaw — Claude Code orchestrator
- **JADX-NO-MCP** — https://github.com/yj94/JADX-NO-MCP
- **apk-decompiler** — https://github.com/emrezdemir/apk-decompiler
- **Apkx-Hunter** — https://github.com/SyscallX-18113/Apkx-Hunter — C-based static analysis
- **APK-Security-Guard-MCP-Suite** — https://github.com/nkcc-apk/APK-Security-Guard-MCP-Suite
- **apkscan** — https://github.com/LucasFaudman/apkscan
- **android-reverse-engineering-claude-skill** — https://github.com/incogbyte/android-reverse-engineering-claude-skill
- **apkleaks** — https://github.com/dwisiswant0/apkleaks
- **JADX-AI-MCP** — https://github.com/zinja-coder/jadx-ai-mcp
- **apktool-mcp-server** — https://github.com/zinja-coder/apktool-mcp-server
- **mobile-security-mcp** — https://github.com/Serhatcck/mobile-security-mcp
- **android-reverse-engineering-mcp-server** — https://github.com/vichhka-git/android-reverse-engineering-mcp-server
- **Frida-Script-Runner** — https://github.com/z3n70/Frida-Script-Runner
- **RMS** — https://github.com/m0bilesecurity/rms-runtime-mobile-security
- **objection** — https://github.com/sensepost/objection
- **renef** — https://github.com/ahmeth4n/renef
- **hooker** — https://github.com/credittone/hooker
- **GDA** — https://github.com/charles2gan/GDA-android-reversing-Tool
- **alab** — https://github.com/hits313/alab
- **iOS Pentesting Cheat Sheet** — https://github.com/ivan-sincek/ios-penetration-testing-cheat-sheet
- **OWASP MASTG** — https://mas.owasp.org/MASTG/
- **OWASP MASVS** — https://mas.owasp.org/MASVS
- **semgrep OWASP Mobile Rules** — https://github.com/mirego/mirego-owasp-mobile
- **mdast-cli** — https://github.com/Dynamic-Mobile-Security/mdast-cli
- **Mobile-QA-Automation-Pipeline** — https://github.com/thoangdev/Mobile-QA-Automation-Pipeline
- **nowsecure-azure-ci-extension** — https://github.com/nowsecure/nowsecure-azure-ci-extension
- **MobSF CI/CD Guide** — https://networkspy.app/blog/mobsf-ci-cd-mobile-security-scanning
- **42Gears Mobile App Security Guide** — https://www.42gears.com/blog/mobile-app-security-testing-best-practices/
- **BugHunterTools Mobile Guide** — https://bughuntertools.com/articles/mobile-app-security-testing-guide-2026/
- **Mobile App Security CI/CD** — https://hiesencyber.com/blog/mobile-app-security-ci-cd-integration-guide/

---

## 9. Wireless & IoT Protocol Exploitation (Expanded)

**Agent 16 — 48 new sources.** WiFi, Bluetooth, ZigBee, LoRaWAN, Z-Wave.

### Key New Sources
- **Aircrack-ng** — https://github.com/aircrack-ng/aircrack-ng
- **Bettercap** — https://github.com/bettercap/bettercap
- **WiFiSlayer** — https://github.com/waheeb71/WiFiSlayer
- **WEF (Wi-Fi Exploitation Framework)** — https://github.com/d3ext/wef
- **Freeway** — https://github.com/FLOCK4H/Freeway
- **Pinecone WLAN Framework** — https://github.com/pinecone-wifi/pinecone
- **AngryOxide** — https://github.com/ragnt/angryoxide
- **Wifiphisher** — https://www.wifiphisher.org/
- **Mana Toolkit** — https://github.com/sensepost/mana
- **fufu-sec** — https://github.com/kyllr-qwen/fufu-sec
- **WiFi-Security-Framework** — https://github.com/AliAkgun0/wifi-security-framework
- **BlueToolkit** — https://github.com/sgxgsx/BlueToolkit — 43+ exploits, USENIX WOOT'25
- **BlueBorne** — https://github.com/ArmisSecurity/blueborne
- **BrakTooth** — https://www.usenix.org/conference/usenixsecurity22/presentation/garbelini
- **BLUFFS** — https://dl.acm.org/doi/10.1145/3576915.3623066
- **SweynTooth** — https://github.com/Matheus-Garbelini/sweyntooth_bluetooth_low_energy_attacks
- **BLURtooth** — https://s3.eurecom.fr/docs/asiaccs22_antonioli.pdf
- **BlueScream** — https://www.s3.eurecom.fr/docs/acsac24_ayoub.pdf
- **BleedingTooth** — https://google.github.io/security-research/pocs/linux/bleedingtooth/writeup.html
- **PerfektBlue** — https://github.com/Nour833/PerfektBlue
- **BlueMirror** — CVE-2020-26556, 26557, 26559, 26560
- **KillerBee** — https://github.com/riverloopsec/killerbee
- **SecBee** — https://magdeburger-institut-fuer-sicherheitsforschung.de/MJS_045_Zillner_ZigBee.pdf
- **ZigBee Touchlink** — https://www.wim.uni-mannheim.de/media/Lehrstuehle/wim/ths/STAFF/mueller.christian/wisec2017_touchlink.pdf
- **Z-Fuzzer** — https://dl.acm.org/doi/10.1145/3448300.3468296
- **LLMIF** — https://www4.comp.polyu.edu.hk/~csxluo/LLMIF.pdf — LLM-augmented IoT fuzzing
- **ZigBee Rejoin Hijack** — https://www.cse.cuhk.edu.hk/~cslui/PUBLICATION/RAID-22.pdf
- **ZLeaks** — https://arxiv.org/html/2107.10830
- **ChirpOTLE** — https://github.com/seemoo-lab/chirpotle
- **LoRAttack** — https://github.com/konicst1/lorattack
- **LoRaWAN DoS** — https://dl.acm.org/doi/10.1145/3230833.3232804
- **LoRaWAN Formal Analysis** — https://www.sciencedirect.com/science/article/abs/pii/S1389128618306145
- **LoRaWAN Physical Layer** — https://www.mdpi.com/1424-8220/22/9/3127
- **LoRaWAN Security Survey** — https://dl.acm.org/doi/10.1145/3561973
- **Z-Attack-NG** — https://github.com/PentHertz/Z-Attack-ng
- **EZ-Wave** — https://github.com/cureHsu/EZ-Wave
- **Z-Shave** — https://www.pentestpartners.com/security-blog/z-shave-exploiting-z-wave-downgrade-attacks/
- **VFuzz** — https://ieeexplore.ieee.org/ielx7/6287639/9668973/09663293.pdf
- **ZCOVER** — https://github.com/CNK2100/ZCOVER_public
- **KillerZee** — https://github.com/joswr1ght/killerzee
- **Morpho** — https://github.com/lukeswitz/Morpho
- **WirelessXpl** — https://pypi.org/project/wirelessxpl/
- **Key Negotiation Downgrade** — https://dl.acm.org/doi/10.1145/3394497
- **BLE Security & Privacy** — https://ieeexplore.ieee.org/iel7/8782661/8901158/09706334.pdf
- **ZigBee Exploited (Black Hat 2015)** — https://magdeburger-institut-fuer-sicherheitsforschung.de/MJS_045_Zillner_ZigBee.pdf
- **Bluetooth Mesh Security** — https://www.bluetooth.com/wp-content/uploads/2025/04/MeshSecurityOverview_INFO_v1.0-1.pdf

---

## 10. Web3 & Smart Contract Vulnerability Research (Expanded)

**Agent 18 — 84 new sources.** Reentrancy, formal verification, AI auditing.

### Key New Sources
- **Slither** — https://github.com/crytic/slither — Trail of Bits, 80+ vuln types
- **Mythril** — https://github.com/ConsenSys/mythril/
- **Aderyn** — https://github.com/cyfrin/aderyn — Rust-based
- **Securify 2.0** — https://github.com/eth-sri/securify2/
- **Manticore** — https://github.com/trailofbits/manticore/
- **SmartBugs** — https://github.com/smartbugs/smartbugs
- **OpenZeppelin Inspector** — https://github.com/OpenZeppelin/openzeppelin-inspector
- **Thrum** — https://thrum.sh/ — autonomous EVM security engine
- **AuditAgent** — https://docs.auditagent.nethermind.io/ — Nethermind AI tool
- **miesc** — https://pypi.org/project/miesc/ — multi-tool orchestration
- **Echidna** — https://github.com/crytic/echidna — property fuzzer
- **Medusa** — https://ethereum.org/developers/tools/medusa/
- **Foundry Fuzzer** — https://book.getfoundry.sh/
- **Halmos** — https://github.com/a16z/halmos/
- **Chimera** — https://github.com/Recon-Fuzz/chimera
- **Vulseye** — https://arxiv.org/html/2408.10116
- **LLAMA** — https://arxiv.org/html/2507.12084 — LLM-guided fuzzing
- **Certora Prover** — https://github.com/Certora/CertoraProver/
- **Solidity SMTChecker** — https://docs.soliditylang.org/en/latest/smtchecker.html
- **Memory Splitting Verification** — https://dl.acm.org/doi/10.1145/3689796
- **eThor** — https://ylya.github.io/papers/ccs20.pdf
- **DASP Top 10** — https://github.com/trailofbits/awesome-smart-contracts
- **SWC Registry** — https://swcregistry.io/
- **OpenSCV** — https://link.springer.com/article/10.1007/s10664-024-10446-8
- **OWASP Smart Contract Top 10** — https://owasp.org/www-project-smart-contract-top-10/
- **SAST Tools Taxonomy** — https://arxiv.org/html/2404.18186v3
- **Reentrancy (OWASP SC08)** — https://scs.owasp.org/sctop10/SC08-ReentrancyAttacks/
- **Read-Only Reentrancy (SCWE-137)** — https://scs.owasp.org/SCWE/SCSVS-CODE/SCWE-137/
- **Flash Loan Attacks (OWASP SC07)** — https://owasp.org/www-project-smart-contract-top-10/2025/en/src/SC07-flash-loan-attacks.html
- **FlashDeFier** — https://arxiv.org/html/2411.01230
- **Oracle Manipulation (SCWE-028)** — https://scs.owasp.org/SCWE/SCSVS-ORACLE/SCWE-028/
- **Front-running & MEV** — https://ethereum.org/developers/docs/mev/
- **Sandwich Attacks** — https://arxiv.org/html/2307.02954v1
- **DeFi Attack Incident Analysis** — https://www.sciencedirect.com/science/article/abs/pii/S0957417425020500
- **KelpDAO Bridge Exploit** — https://www.chainalysis.com/blog/kelpdao-bridge-exploit-april-2026/
- **LayerZero Incident** — https://layerzero.network/publications/kelpdao-incident-report.pdf
- **Hyperbridge Exploit** — https://hubsec.net/research/hyperbridge-investigation-2026-04
- **ZK-Proof Failures** — https://rya-sge.github.io/access-denied/2026/06/19/zkp-cross-chain-bridge-hacks/
- **Intent-Based Cross-Chain** — https://arxiv.org/html/2602.17805
- **Cross-Chain Message Replay** — https://redvolt.ai/blog/cross-chain-message-replay-the-2026-bridge-vulnerability-playbook
- **Heimdallr** — https://arxiv.org/html/2601.17833v1 — agentic auditing, 17/20 attacks reconstructed
- **SPEAR** — https://www.arxiv.org/pdf/2602.04418 — multi-agent coordination
- **EVMbench** — https://arxiv.org/html/2603.10795v1 — AI agent benchmark
- **Knowdit** — https://arxiv.org/abs/2603.26270v1
- **Wake Arena** — https://ackee.xyz/blog/wake-arena-multi-agent-ai-audit-with-graph-driven-reasoning/
- **Chaintrix** — https://arxiv.org/pdf/2605.09350
- **Plamen** — https://github.com/plamentsv/plamen — 18-100 AI agents
- **sc-auditor** — https://github.com/Archethect/sc-auditor
- **GasSentry** — https://abdn.elsevierpure.com/en/publications/gassentry-a-multi-agent-llm-framework-for-smart-contract-security/
- **AuditAgent on EVMBench** — https://www.nethermind.io/blog/auditagent-on-evmbench-what-the-data-shows
- **Cyfrin Audit Checklist** — https://github.com/Cyfrin/audit-checklist
- **OpenZeppelin Readiness Guide** — https://www.openzeppelin.com/readiness-guide
- **Smart Contract Security Checklist** — https://ethereum.org/developers/tutorials/secure-development-workflow/
- **Hans's Audit Checklist** — https://github.com/Cyfrin/audit-checklist/blob/main/ref/hans.md
- **10 Steps to Systematic Audit** — https://www.cyfrin.io/blog/10-steps-to-systematically-approach-a-smart-contract-audit
- **ML for Smart Contract Security** — https://dl.acm.org/doi/10.1145/3772367
- **Comprehensive Guide for Web3 Security** — https://link.springer.com/book/10.1007/978-3-031-39288-7
- **Cybersecurity Management in DeFi** — https://link.springer.com/book/10.1007/978-3-031-23340-1
- **Security Analysis of DeFi** — https://www.researchgate.net/publication/363683253_Security_Analysis_of_Defi_Vulnerabilities_Attacks_Advances
- **DeFiTail** — https://arxiv.org/html/2511.00408v1
- **ByteEye** — https://link.springer.com/article/10.1007/s10515-025-00559-9
- **MTVHunter** — https://ojs.aaai.org/index.php/AAAI/article/view/33664
- **GenDetect** — https://research.monash.edu/en/publications/gendetect-generative-large-language-model-usage-insmart-contract-/
- **GPTScan** — https://daoyuan14.github.io/papers/ICSE24_GPTScan.pdf
- **SmartAuditFlow** — https://arxiv.org/html/2505.15242v2
- **DivertScan** — https://seclab.cse.cuhk.edu.hk/papers/fse25-DivertScan.pdf
- **Contract-Graph Fusion** — https://www.mdpi.com/2076-3417/15/19/10844
- **COBRA** — https://arxiv.org/html/2410.20712v1
- **FIRST** — https://dl.acm.org/doi/10.1145/3708821.3736190
- **Lanturn** — https://dl.acm.org/doi/10.1145/3576915.3623204
- **MadMax** — https://dl.acm.org/doi/10.1145/3276486
- **ProMutator** — https://www.csie.ntu.edu.tw/~hchsiao/pub/2021_IEEE_SB_ProMutator.pdf
- **Drift Protocol Exploit** — https://www.elliptic.co/insights/drift-protocol-exploited-for-286-million-in-suspected-dprk-linked-attack/
- **Resolv Protocol Incident** — https://www.certik.com/blog/resolv-protocol-incident-analysis
- **Truebit Incident** — https://www.certik.com/skynet-report/truebit-incident-analysis
- **SOF/LAXO Token Burn** — https://www.certik.com/blog/sof-laxo-incident-analysis
- **2024 Most Exploited DeFi** — https://threesigma.xyz/blog/exploit/2024-defi-exploits-top-vulnerabilities

---

## 11–19. Remaining Domains (summarized)

The remaining agents covered (full source lists in `_synthesis_raw.md`):

### 11. Active Directory Attack Path Automation
BloodHound Cypher generation, Kerberoasting at scale, ACL abuse, DCSync, Golden/Silver tickets, ADCS ESC attacks, LAPS, gMSA, ADFS, Azure AD/Entra ID attacks, cross-forest trust abuse, SID filtering, DCShadow, DCSync, Syncronizer attacks.

### 12. Post-Exploitation & Lateral Movement in Cloud
Cloud-native lateral movement, identity-based pivoting, persistent access, SSM exploitation, Lambda privilege escalation, cross-account role assumption, metadata service abuse, IMDSv1/v2, instance profile abuse, container escape to cloud.

### 13. Deserialization & In-Memory Exploitation
Java deserialization (ysoserial, gadget chains), PHP deserialization (PHPGGC, POP chains), Python pickle, .NET BinaryFormatter, in-memory payload injection, reflective loading, process hollowing, DLL injection, APC injection, thread execution hijacking.

### 14. RCE Chain Construction & Weaponization
Exploit chaining, vulnerability weaponization, CVE-to-exploit pipelines, Metasploit module development, Cobalt Strike beaconing, Sliver implants, Havoc C2, payload generation (msfvenom), shellcode development, stager/stage architecture.

### 15. Bug Bounty Platform Intelligence & Recon Automation
Asset discovery, subdomain enumeration (subfinder, amass, chaos), target prioritization, OSINT (theHarvester, SpiderFoot, Shodan, Censys), waybackurls, gau, parameter discovery (arjun, paramminer), JS analysis (linkfinder, subjs), WAF detection (wafw00f), technology fingerprinting (Wappalyzer, WhatWeb).

### 16. WAF/IDS/IPS Evasion Automation
Payload obfuscation, encoding techniques, SQLMap tamper scripts, Burp intruder payload processing, case randomization, comment insertion, double encoding, Unicode normalization, chunked transfer, HTTP/2 smuggling, TLS fingerprinting evasion, JA3 spoofing.

### 17. Certificate & TLS/SSL Vulnerability Exploitation
Weak cipher suites, certificate misissuance, TLS downgrade attacks, Heartbleed, POODLE, BEAST, CRIME, BREACH, FREAK, Logjam, DROWN, certificate transparency monitoring, Let's Encrypt abuse, pinning bypass, SSL stripping, HSTS bypass.

### 18. Memory Corruption Exploit Automation
Heap spraying, ROP chain generation (ROPgadget, ROPeer, angret), exploit reliability tuning, ASLR bypass, stack canary leak, PIE bypass, GOT overwrite, format string exploitation, integer overflow, use-after-free, double-free, type confusion.

### 19. Social Engineering & Phishing Automation
Personalized phishing generation, pretexting frameworks, credential harvesting, GoPhish campaigns, Evilginx adversary-in-the-middle, Modlishka reverse proxy, King Phisher, SET (Social-Engineer Toolkit), physical security assessment, tailgating, lockpicking, badge cloning, USB drop attacks, vishing.

---

## New Repositories to Clone (from this expansion)

| Repo | URL | Why |
|---|---|---|
| kubernetes-goat | https://github.com/madhuakula/kubernetes-goat | Deliberately vulnerable K8s |
| kube-hunter | https://github.com/aquasecurity/kube-hunter | K8s pentesting |
| kube-bench | https://github.com/aquasecurity/kube-bench | CIS benchmark |
| falco | https://github.com/falcosecurity/falco | Runtime security |
| tracee | https://github.com/aquasecurity/tracee | eBPF runtime security |
| tetragon | https://github.com/cilium/tetragon | eBPF security |
| gatekeeper | https://open-policy-agent.github.io/gatekeeper/ | OPA policy |
| kyverno | https://kyverno.io/ | K8s policy |
| trivy | https://github.com/aquasecurity/trivy | Multi-scanner |
| grype | https://github.com/anchore/grype | Vuln scanner |
| syft | https://github.com/anchore/syft | SBOM |
| cosign | sigstore.dev | Signing |
| pacu | https://github.com/RhinoSecurityLabs/pacu | AWS exploitation |
| scoutsuite | https://github.com/nccgroup/scoutsuite | Multi-cloud audit |
| cloud-custodian | https://github.com/cloud-custodian/cloud-custodian | Policy engine |
| checkov | https://github.com/bridgecrewio/checkov | IaC security |
| terrascan | https://github.com/tenable/terrascan | IaC analysis |
| mobsf | https://github.com/MobSF/Mobile-Security-Framework-MobSF | Mobile analysis |
| objection | https://github.com/sensepost/objection | Mobile runtime |
| aircrack-ng | https://github.com/aircrack-ng/aircrack-ng | WiFi cracking |
| bettercap | https://github.com/bettercap/bettercap | Network attacks |
| killerbee | https://github.com/riverloopsec/killerbee | ZigBee attacks |
| blue-toolkit | https://github.com/sgxgsx/BlueToolkit | Bluetooth exploits |
| slither | https://github.com/crytic/slither | Smart contract analysis |
| mythril | https://github.com/ConsenSys/mythril/ | Symbolic execution |
| echidna | https://github.com/crytic/echidna | Property fuzzer |
| medusa | https://ethereum.org/developers/tools/medusa/ | Parallel fuzzer |
| halmos | https://github.com/a16z/halmos/ | Symbolic testing |
| certora-prover | https://github.com/Certora/CertoraProver/ | Formal verification |
| pyrit | https://github.com/microsoft/pyrit | LLM red teaming |
| garak | https://github.com/NVIDIA/garak | LLM scanner |
| aflplusplus | https://github.com/AFLplusplus/AFLplusplus | Fuzzing |
| honggfuzz | https://github.com/google/honggfuzz | Fuzzing |
| angora | https://github.com/AngoraFuzzer/Angora | Binary fuzzing |
| owasp-cstg | https://github.com/OWASP/owasp-cstg | Cloud testing guide |
| owasp-noir | https://owasp.org/www-project-noir/ | Endpoint extraction |
| kiterunner | https://github.com/assetnote/kiterunner | API route brute-force |
| jwt-tool | https://github.com/ticarpi/jwt_tool | JWT attacks |
| ysoserial | https://github.com/frohoff/ysoserial | Java deserialization |
| phpggc | https://github.com/ambionics/phpggc | PHP deserialization |
| gophish | https://github.com/gophish/gophish | Phishing framework |
| evilginx2 | https://github.com/kgretzky/evilginx2 | Adversary-in-the-middle |
| social-engineer-toolkit | https://github.com/trustedsec/social-engineer-toolkit | SET |
| cloud-audit-mcp | https://github.com/badchars/cloud-audit-mcp | Cloud audit MCP |
| iac-scanner | https://github.com/alphacrack/acrack/iac-scanner | Agentic IaC scanner |
| cloudsecurity-af | https://github.com/Agent-Field/cloudsecurity-af | AI-native attack paths |
| sentinel-mesh | https://github.com/hira299/sentinel-mesh | Neuro-symbolic remediation |
| plamen | https://github.com/plamentsv/plamen | Autonomous audit agent |
| heimdallr | https://arxiv.org/html/2601.17833v1 | Agentic auditing |
| evmbench | https://arxiv.org/html/2603.10795v1 | AI agent benchmark |
| wake-arena | https://ackee.xyz/blog/wake-arena-multi-agent-ai-audit-with-graph-driven-reasoning/ | Multi-agent audit |
| chaintrix | https://arxiv.org/pdf/2605.09350 | Structurally-grounded audit |
| auditagent | https://docs.auditagent.nethermind.io/ | AI security analysis |
| sc-auditor | https://github.com/Archethect/sc-auditor | AI co-pilot |
| ios-hunt | https://github.com/kankburhan/iosHunt | iOS pentest pipeline |
| revkit | https://github.com/qtmleap/revkit | Multi-agent RE |
| rekit | https://github.com/b-erdem/rekit | Mobile API RE |
| medusa-mobile | https://github.com/Ch0pin/medusa | Frida modules |
| nutcracker | https://github.com/drneox/nutcracker | APK analysis |
| apk-bb-scanner | https://github.com/ZZ0R0/apk-bb-scanner | Bug bounty pipeline |
| apkdeep-lens | https://github.com/d78ui98/APKDeepLens | Static analysis |
| apk-sentinel | https://github.com/ismailtsdln/ApkSentinel | CLI scanner |
| areclaw | https://github.com/TheQmaks/areclaw | Claude Code orchestrator |
| jadx-ai-mcp | https://github.com/zinja-coder/jadx-ai-mcp | JADX MCP |
| apktool-mcp-server | https://github.com/zinja-coder/apktool-mcp-server | APKTool MCP |
| mobile-security-mcp | https://github.com/Serhatcck/mobile-security-mcp | Mobile MCP |
| android-re-mcp | https://github.com/vichhka-git/android-reverse-engineering-mcp-server | Android RE MCP |
| frida-script-runner | https://github.com/z3n70/Frida-Script-Runner | Frida toolkit |
| rms | https://github.com/m0bilesecurity/rms-runtime-mobile-security | Runtime security |
| renes | https://github.com/ahmeth4n/renef | ARM64 instrumentation |
| hooker | https://github.com/credittone/hooker | Frida toolkit |
| gda | https://github.com/charles2gan/GDA-android-reversing-Tool | RE tool |
| alab | https://github.com/hits313/alab | Android pentest lab |
| ios-pentest-cheatsheet | https://github.com/ivan-sincek/ios-penetration-testing-cheat-sheet | iOS cheatsheet |
| mdast-cli | https://github.com/Dynamic-Mobile-Security/mdast-cli | Mobile DAST |
| wifi-slayer | https://github.com/waheeb71/WiFiSlayer | WiFi attacks |
| wef | https://github.com/d3ext/wef | WiFi exploitation |
| freeway | https://github.com/FLOCK4H/Freeway | WiFi testing |
| pinecone | https://github.com/pinecone-wifi/pinecone | Red team framework |
| angryoxide | https://github.com/ragnt/angryoxide | 802.11 attacks |
| wifiphisher | https://www.wifiphisher.org/ | Rogue AP |
| mana | https://github.com/sensepost/mana | Rogue AP |
| fufu-sec | https://github.com/kyllr-qwen/fufu-sec | WiFi framework |
| wifi-security-framework | https://github.com/AliAkgun0/wifi-security-framework | Enterprise WiFi |
| bluetoolkit | https://github.com/sgxgsx/BlueToolkit | Bluetooth exploits |
| blueborne | https://github.com/ArmisSecurity/blueborne | BlueBorne exploits |
| sweyntooth | https://github.com/Matheus-Garbelini/sweyntooth_bluetooth_low_energy_attacks | BLE attacks |
| perfektblue | https://github.com/Nour833/PerfektBlue | Bluetooth framework |
| secbee | https://magdeburger-institut-fuer-sicherheitsforschung.de/MJS_045_Zillner_ZigBee.pdf | ZigBee audit |
| z-fuzzer | https://dl.acm.org/doi/10.1145/3448300.3468296 | ZigBee fuzzing |
| chirpotle | https://github.com/seemoo-lab/chirpotle | LoRaWAN |
| lorattack | https://github.com/konicst1/lorattack | LoRaWAN |
| z-attack-ng | https://github.com/PentHertz/Z-Attack-ng | Z-Wave |
| ez-wave | https://github.com/cureHsu/EZ-Wave | Z-Wave |
| zcover | https://github.com/CNK2100/ZCOVER_public | Z-Wave |
| killerzee | https://github.com/joswr1ght/killerzee | Z-Wave |
| morpho | https://github.com/lukeswitz/Morpho | Multi-protocol |
| wirelessxpl | https://pypi.org/project/wirelessxpl/ | Multi-protocol |
| crackql | https://github.com/nicholasaleks/crackql/ | GraphQL brute-force |
| graphqler | https://github.com/omar2535/graphqler/ | GraphQL testing |
| gqlsweep | https://github.com/Somchandra17/gqlSweep | GraphQL fuzzing |
| graphqlbrute | https://github.com/phor3nsic/graphqlBrute | GraphQL brute-force |
| gdos | https://github.com/kabiri-labs/gdos | GraphQL DoS |
| inql | https://github.com/doyensec/inql | GraphQL scanner |
| clairvoyance | https://github.com/nikitastupin/clairvoyance | Schema reconstruction |
| graphql-voyager | https://github.com/APIs-guru/graphql-voyager/ | Visualization |
| graphw00f | https://github.com/nicholasaleks/graphw00f | Fingerprinting |
| prediql | https://arxiv.org/html/2510.10407v2 | LLM-guided GraphQL fuzzer |
| indago | https://github.com/su1ph3r/indago | AI API fuzzer |
| aigraphql-pentester | https://github.com/nayangoel/AIGraphqlPentester | Burp AI extension |
| llm-graphql | https://github.com/Lserein/LLM-GraphQL | AI detection |
| entropy-chaos | https://github.com/arjinexe/entropy-chaos | LLM attack gen |
| vespasian | https://github.com/praetorian-inc/vespasian | Multi-protocol API |
| noir | https://github.com/cd80/noir | Attack surface |
| surface | https://github.com/pensarai/surface | Endpoint discovery |
| api-discovery | https://github.com/DanaEpp/APIDiscovery | Burp extension |
| endpoint-tester | https://github.com/leopechnicki/endpoint-tester | Auto-discovery |
| api-spy | https://github.com/austinjump-sec/API-SPY-API-PROBE | Recursive discovery |
| depenfusion | https://github.com/benjamin-mauss/depenfusion | Dependency confusion |
| typogard | https://github.com/dangardner/typogard | Typosquatting |
| snync | https://github.com/snyk-labs/snync | Typosquatting |
| misconfig-mapper | https://github.com/intigriti/misconfig-mapper | SaaS misconfig
