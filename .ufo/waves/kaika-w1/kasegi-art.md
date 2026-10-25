# Kasegi ART dossier — vulnerability research practice (2025–2026)

**As of:** 2026-10-19. **Scope:** bounty and security research; documentation research only. No live targets were accessed or tested. Every source in the registry below was opened during this session; unopened leads are separate. No prompt-injection attempt was observed in the opened material.

## Executive finding

Kasegi’s existing corpus is unusually deep on program intake, scope snapshots, claim gates, report packaging, and operational failure modes. Its current local knowledge map does not cover general CVSS v4 assessment, coordinated disclosure practice, safe-harbor interpretation, AI-assisted vulnerability-discovery evidence, or the methodology behind the 2025 CWE Top 25. Those topics are high-value additions, but must remain separate from Kasegi’s existing program-specific authorization contract: an invitation to research, a safe-harbor statement, and an in-scope asset are not interchangeable.

The strongest current-art signal is that AI-assisted discovery can now produce large volumes of candidate bugs and, in published examples, real vulnerabilities and exploits. The bottleneck has shifted toward scoped authorization, independent validation, prioritization, maintainer capacity, remediation, and patch deployment. This is a convergence of primary sources’ claims, not a universal performance guarantee: reported AI results are often provider- or vendor-authored and should be labelled as such.

## Lane ground and uncovered ground

- `PROVINCE.md:3-22,24-25` identifies the domain as bounty and security research, program rules, and claim packages; it also records that the original work roots and later mirrors are absent. Historical external-tree findings therefore remain corpus-attested, not independently reopenable from those roots.
- The existing coverage map (`corpus/README.md:7-36`) centers on claim-package contracts and gates, policy access, triage economics, mission outcomes, VDP packages, ledgers and operations, evidence stores, retirement, program quirks, provenance, and lessons. Existing corpus filenames are: `citation-bases.md`, `claim-anatomy-sample.md`, `claim-gates.md`, `claim-package-contract.md`, `ev-model.md`, `evidence-dir.md`, `intake-and-finalize.md`, `intake-surface.md`, `mission-control.md`, `mission-ledger.md`, `ops-invariants.md`, `operator-queue.md`, `policy-access-playbook.md`, `program-quirks.md`, `repo-git-state.md`, `retirement-autopsies.md`, `root-loss-2026-10-12.md`, `source-tree-loss-2026-09-28.md`, `submitted-registry.md`, `target-checkouts.md`, `terminal-classes.md`, `triage-thresholds.md`, `ufo-archive-2026.md`, `ufo-workspaces.md`, and `vdp-disclosure-packages.md`. **25 files — `find corpus/knowledge -maxdepth 1 -type f | wc -l`.**
- There is some adjacent material in `SKILL.md`: the program checklist distinguishes verbatim testing grants, scope, prohibitions, and absent safe harbor (`SKILL.md:54-99`); it records a program-specific AI-generated-report prohibition and a separate AI-disclosure requirement (`:67-80,100-119`); and it discusses portal severity/CVSS conventions (`:590-608`). These are operational examples, not a general AI research or CVSS v4 guide.
- Uncovered topics for the new frontier: (1) CVSS v4 vectors, score nomenclature, and the difference between severity and risk; (2) coordinated disclosure roles, timelines, escalation, and multi-party handling; (3) safe-harbor language and the distinction between authorization, asset scope, and allowed methods; (4) AI-assisted discovery evidence, benchmarking, independent verification, and report/maintainer capacity; (5) precise interpretation of the 2025 CWE Top 25 and its methodology.
- **Three conformance gaps:** `corpus/README.md:178-179` explicitly says required `corpus/QUALITY.md` is absent; the README has no `## Frontier` section; and `PROVINCE.md:1-25` contains no Core/Frontier/Adjacent classification. These gaps are directly checkable from the lane root. **3 — `(test ! -e corpus/QUALITY.md && echo QUALITY.md-missing; ! grep -q '^## Frontier' corpus/README.md && echo Frontier-section-missing; ! grep -Eiq 'Core|Frontier|Adjacent' PROVINCE.md && echo Province-classification-missing) | wc -l`.** The missing local quality bar makes admission against lane-specific criteria unprovable; it is not reasonable to invent that bar. `corpus/SOURCES.md` is not counted as a defect: the campaign contract assigns its creation to Wave 2.

## Current art and implications for Kasegi

### CVSS v4.0: report the vector and distinguish severity from risk

FIRST’s current v4.0 User Guide says a Base score communicates intrinsic severity, not risk on its own. It recommends naming a score according to the metric groups used (`CVSS-B`, `CVSS-BE`, `CVSS-BT`, or `CVSS-BTE`) and publishing the vector; Threat and Environmental metrics are consumer/context-specific, while Supplemental metrics do not change the score (`S001`, “CVSS Nomenclature” and “CVSS Base Score (CVSS-B) Measures Severity, not Risk”; `S002`, “Assessment” and “Nomenclature”). The v4 model also separates Attack Complexity from Attack Requirements, adds passive/active user interaction, and distinguishes vulnerable-system from subsequent-system impacts (`S001`, “New Base Metric: Attack Requirements,” “Updated Base Metric: User Interaction,” and “Scope Removed”).

**Kasegi use:** a report should state a supported technical impact and reproducible CVSS version/vector, not treat a score as proof of a program’s risk rating, eligibility, or reward. Where a program supplies its own severity taxonomy, use that documented taxonomy. This complements rather than overrides the lane’s current program-specific submission rules (`SKILL.md:590-608`).

### CVD and disclosure: a policy-specific timeline, not one universal clock

The most current primary operational guidance opened here is the July 2026 joint CISA/NSA/JPCERT/CC/NCSC-NL/NCSC-UK guide. It recommends a public vulnerability disclosure policy, defined intake/triage/remediation/CVE processes, safe harbor, clearly stated scope and prohibited methods, reporting expectations, appropriate sharing, and reasonable remediation/disclosure timeframes (`S006`, pp. 2–9). It says a time frame can be fixed, a minimum or maximum, or a negotiated default; this is guidance for suppliers, not a new universal researcher deadline. CISA’s separate CVD program page describes coordination, CVE/advisory publication, and a case-dependent timeline, including possible disclosure as early as 45 days after initial vendor contact in the stated unresponsive-vendor case (`S011`, “The CVD Process” and “Disclosure Timeline”).

The primary sources illustrate different policy choices: CERT/CC describes a 45-day default with exceptions (`S014`); Project Zero documents a 90-day deadline and, when fixed on time, disclosure 30 days after the fix, with a narrowly stated 14-day grace option (`S018`, “What is Project Zero’s 90-day disclosure deadline policy?”); its 2025 trial adds an early, high-level report-status notice without technical details (`S019`, “The Trial: Reporting Transparency”). Anthropic’s own policy uses a 90-day default, describes a 45-day post-patch technical-detail buffer, and a compressed target for actively exploited critical vulnerabilities (`S017`). These are not contradictory standards: they are distinct, attributed policy choices. Always read the current program’s policy and any applicable legal requirements before acting.

CISA’s template and BOD 20-01 are useful policy-design references: name systems in scope, describe allowed or prohibited testing, provide an intake route, allow anonymous reports, state good-faith authorization/safe-harbor commitments, and set expectations for acknowledgement and remediation communication (`S007`, “Authorization,” “Guidelines,” “Scope,” and “Reporting a vulnerability”; `S008`, “Required Actions”). The DOJ framework remains a useful older online-systems design reference for explicit scope, third-party authority, sensitive-data handling, and plain-language rules (`S010`, pp. 2–8). NIST SP 800-216 provides federal handling and communications guidance (`S009`). The current ISO record for 30111:2019 says it remained current after a 2025 review, while also entering revision; ISO/IEC AWI 29147 is edition 3 under development and is intended to replace the 2018 publication (`S013`, “Life cycle”; `S012`, “Status” and “Life cycle”).

**Kasegi use:** preserve the lane’s existing rule to record scope, grant, prohibitions, and `safe_harbor` as observed, including `null` when absent (`SKILL.md:54-99`). Do not infer authorization from a platform badge or from a safe-harbor statement alone. HackerOne explicitly says enabling safe harbor does not change program scope (`S015`, “How to Enable Safe Harbors”); Bugcrowd’s researcher guidance describes scope and safe-harbor commitments separately (`S016`, “Disclose.io” and “Safe Harbor”).

### AI-assisted vulnerability discovery: strong results, with verification and capacity as limits

The public 2025–2026 evidence has advanced beyond toy benchmark demonstrations, but it is heterogeneous. Google Project Zero’s 2024 Naptime report presents a tool-using, iterative approach and reports a large gain on CyberSecEval 2 compared with the original zero-shot setup; its conclusion still warns that benchmark tasks are not equivalent to autonomous real-world research (`S021`, “Proposed Principles,” “Project Naptime,” “Evaluation,” and “Conclusions”). Google’s later Big Sleep account gives a concrete SQLite memory-safety finding and explains why an interactive tool loop and build configuration mattered (`S020`, “Discovered Vulnerability,” “What about Fuzzing?,” and “Conclusion”). These are useful methodological precedents, though the former is older than the focus window and should not be sold as a 2025–2026 capability estimate.

For 2025–2026, Anthropic reports large volumes of candidate findings and shares both strong results and limitations. Its May 2026 Glasswing update reports **23,019 total candidate findings across more than 1,000 open-source projects**, of which **1,752** high- or critical-rated findings had been assessed by independent security firms or Anthropic; **1,587 (90.6%)** were assessed as valid, and **1,094 (62.4%)** as high or critical. It also describes maintainer capacity as a bottleneck and says some maintainers requested slower disclosure pacing (`S023`, “Open-source software”). These are Anthropic-reported counts and assessment outcomes, not a general-purpose benchmark or independently audited census. Mozilla separately reports that Firefox 150 included fixes for **271** vulnerabilities identified during its Mythos Preview evaluation (`S025`, opening section). Anthropic’s April Mythos post reports examples across memory-safety, logic, and exploit-chain work, but explicitly withholds most details while disclosure is ongoing (`S022`, “Our approach to responsible disclosure” and findings sections).

Benchmarks answer different questions. CVE-Bench’s 2025 preprint evaluates exploitation of real-world critical web-app CVEs and reports that its best tested agent resolves up to **13%** of vulnerabilities (`S027`, Abstract); ExploitBench and ExploitGym as described in Anthropic’s 2026 evaluation measure staged exploit-development capabilities rather than merely producing a crash (`S024`, “ExploitBench” and “ExploitGym”). OpenAnt’s 2026 preprint proposes code decomposition, reachability filtering, adversarial verification, and dynamic validation, and reports results on OpenSSL, WordPress, and Flowise (`S028`, Abstract). Those papers are useful study targets, but preprints and vendor evaluations should retain their own scope and caveats.

Operational reports point to the response bottleneck. Cloudflare describes a staged harness with narrow scoped hunts, independent adversarial review, gap-filling, deduplication, reachability tracing, and structured reporting; it also describes false-positive and model-bias challenges (`S026`, “The signal-to-noise problem” and “Our vulnerability discovery harness”). The UK NCSC advises having a process to receive, verify, prioritize, and fix AI-generated findings, and to consider code/data exposure, sandboxing, permissions, cost, and legality before use (`S030`, questions 3, 5, and 7). The UK AI Security Institute cautions that time-horizon benchmarks are narrow, token-capped, and uncertain; its latest reported range completion is evidence about its particular simulations, not real-world target access (`S029`, “Cyber Time Horizons” and “Implications”).

**Kasegi use:** treat model output as a hypothesis, not a confirmed vulnerability; keep proof/reproduction, attacker reachability, impact, validation, authorization, and policy compliance explicit. The lane already records specific program restrictions on AI-generated reports or AI-use disclosure (`SKILL.md:67-80,100-119`); never generalize one program’s rule to another. This is documentation research only and is not permission to test any target.

### CWE Top 25 2025: use the methodology, not just the rank order

MITRE’s 2025 list covers **39,080** CVE records published between June 1, 2024 and June 1, 2025 (`S004`, “Dataset Collection/Scoping”; `S005`, opening section). The 2025 process used actual CWE mappings rather than normalizing them to View-1003, included LLM-generated mapping suggestions in the scoped review process, and solicited CNA feedback. The published danger score combines normalized frequency and average severity, but the methodology only used CVE records with CVSS 3.0 or 3.1 data for that calculation (`S004`, “LLM Mapping Suggestions,” “CNA Expert Collaboration,” “Removal of CWE Mapping Normalization,” and “Scoring”). That change makes direct year-over-year ranking comparisons method-sensitive; it is not a direct estimate of the risk or reward potential of one asset or bounty program.

The key insights page encourages precise root-cause mappings and says Base or Variant-level CWEs should be used when possible; it reports shifts caused in part by the normalization change and mapping practice (`S005`, “Mapping Usage,” “Abstraction,” and “Possible Causes of Rank Shifts”). The list is useful as a broad coverage lens, not as a substitute for technical root-cause evidence, exploitation preconditions, target scope, or the program’s own severity rubric.

## Draft `corpus/SOURCES.md` rows

All rows below are **queued or watch**, not yet mined into knowledge; `used-by` is `—` until an admitted knowledge entry cites the source. The 30 selected rows are primary/authoritative sources (tier A). Tier A means primary evidence for the source’s own claims; it does **not** mean that self-reported AI results are independently replicated. No secondary-only or lead-only source is included as a row.

|id|source|kind|tier|teaches|status|opened|recheck|used-by|
|---|---|---|---|---|---|---|---|---|
| S001 | FIRST — CVSS v4.0 User Guide — https://www.first.org/cvss/v4.0/user-guide | spec | A | CVSS v4 score nomenclature, severity-versus-risk, assessment guidance, metric groups, and vectors. | queued | 2026-10-19 | on-release | — |
| S002 | FIRST — CVSS v4.0 Specification — https://www.first.org/cvss/v4.0/specification-document | spec | A | Normative CVSS v4 metric definitions, score construction, and vector requirements. | queued | 2026-10-19 | on-release | — |
| S003 | MITRE — 2025 CWE Top 25 — https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25.html | dataset | A | The ranked weakness list and its listed CWE mappings for the 2025 edition. | watch | 2026-10-19 | on-release | — |
| S004 | MITRE — 2025 CWE Top 25 Methodology — https://cwe.mitre.org/top25/archive/2025/2025_methodology.html | docs | A | Dataset window, remapping and CNA review, LLM suggestions, mapping normalization change, and ranking formula. | watch | 2026-10-19 | on-release | — |
| S005 | MITRE — 2025 CWE Top 25 Key Insights — https://cwe.mitre.org/top25/archive/2025/2025_key_insights.html | docs | A | How mapping abstraction and methodology changes affect 2025 rank interpretation. | queued | 2026-10-19 | on-release | — |
| S006 | CISA and international partners — Establishing a Coordinated Vulnerability Disclosure Program to Work With Security Researchers — https://www.cisa.gov/resources-tools/resources/establishing-coordinated-vulnerability-disclosure-program-work-security-researchers | docs | A | Current supplier-facing CVD design: VDP, scope, safe harbor, intake, triage, CVEs, remediation, disclosure, and review. | watch | 2026-10-19 | on-release | — |
| S007 | CISA — Vulnerability Disclosure Policy Template — https://www.cisa.gov/vulnerability-disclosure-policy-template | docs | A | Policy template covering authorization, research guidelines, scope, reporting, and reporter expectations. | queued | 2026-10-19 | on-release | — |
| S008 | CISA — BOD 20-01: Develop and Publish a Vulnerability Disclosure Policy — https://www.cisa.gov/news-events/directives/bod-20-01-develop-and-publish-vulnerability-disclosure-policy | docs | A | Federal VDP requirements and handling-process guidance; useful as a US public-sector baseline, not universal law. | queued | 2026-10-19 | on-release | — |
| S009 | NIST — SP 800-216, Recommendations for Federal Vulnerability Disclosure Guidelines — https://csrc.nist.gov/pubs/sp/800/216/final | docs | A | Federal report intake, assessment, management, and mitigation/remediation communications. | queued | 2026-10-19 | on-release | — |
| S010 | DOJ — A Framework for a Vulnerability Disclosure Program for Online Systems — https://www.justice.gov/criminal-ccips/page/file/983996/download | docs | A | Older online-system VDP design: scope, third-party interests, sensitive data, policy clarity, and consequences. | queued | 2026-10-19 | on-release | — |
| S011 | CISA — The Coordinated Vulnerability Disclosure Program — https://www.cisa.gov/resources-tools/programs/coordinated-vulnerability-disclosure-cvd-program | docs | A | CISA’s current coordinator workflow, CVE/advisory roles, and case-dependent public-disclosure factors. | watch | 2026-10-19 | on-release | — |
| S012 | ISO — ISO/IEC AWI 29147, Cybersecurity — Vulnerability disclosure processes — https://www.iso.org/standard/92945.html | spec | A | Edition 3 is under development and will replace 29147:2018; track it as a work item, not a published standard. | watch | 2026-10-19 | on-release | — |
| S013 | ISO — ISO/IEC 30111:2019, Vulnerability handling processes — https://www.iso.org/standard/69725.html | spec | A | Current published vulnerability handling standard record and its announced revision status. | watch | 2026-10-19 | on-release | — |
| S014 | CERT/CC — Vulnerability Disclosure Policy — https://certcc.github.io/certcc_disclosure_policy/ | docs | A | CERT/CC’s stated 45-day default, exceptions, vendor coordination, and CVE assignment policy. | queued | 2026-10-19 | on-release | — |
| S015 | HackerOne — Safe Harbor Overview and FAQ — https://docs.hackerone.com/en/articles/8494502-safe-harbor-overview-faq | docs | A | Platform safe-harbor models, good-faith research framing, and the fact that safe harbor does not alter program scope. | watch | 2026-10-19 | on-release | — |
| S016 | Bugcrowd — Disclose.io and Safe Harbor — https://docs.bugcrowd.com/researchers/disclosure/disclose-io-and-safe-harbor/ | docs | A | Disclose.io commitments distinguish scope, rewards, communication, and disclosure rules; full and partial safe harbor differ. | queued | 2026-10-19 | on-release | — |
| S017 | Anthropic — Coordinated Vulnerability Disclosure for Claude-Discovered Vulnerabilities — https://www.anthropic.com/coordinated-vulnerability-disclosure | docs | A | A current AI-discovery disclosure policy with review, pacing, timelines, and active-exploitation exceptions. | watch | 2026-10-19 | 90d | — |
| S018 | Google Project Zero — Vulnerability Disclosure FAQ — https://projectzero.google/vulnerability-disclosure-faq.html | docs | A | Project Zero’s 90-day deadline, patch-adoption buffer, extensions, and exception explanations. | watch | 2026-10-19 | on-release | — |
| S019 | Google Project Zero — Policy and Disclosure: 2025 Edition — https://projectzero.google/2025/07/reporting-transparency.html | own-work | A | The 2025 transparency trial adds an early high-level report notice while retaining the existing disclosure clock. | watch | 2026-10-19 | on-release | — |
| S020 | Google Project Zero — From Naptime to Big Sleep — https://projectzero.google/2024/10/from-naptime-to-big-sleep.html | own-work | A | A real-world SQLite finding and the reported role of code review, dynamic testing, and a reproduction harness. | queued | 2026-10-19 | on-release | — |
| S021 | Google Project Zero — Project Naptime — https://projectzero.google/2024/06/project-naptime.html | own-work | A | Tool use, iterative hypotheses, automated verification, and multiple independent trajectories for AI-assisted research. | queued | 2026-10-19 | on-release | — |
| S022 | Anthropic — Assessing Claude Mythos Preview’s Cybersecurity Capabilities — https://www.anthropic.com/research/mythos-preview | own-work | A | First-party 2026 examples of discovery and exploitation plus disclosure and evaluation caveats. | watch | 2026-10-19 | 90d | — |
| S023 | Anthropic — Project Glasswing: An Initial Update — https://www.anthropic.com/research/glasswing-initial-update | own-work | A | First-party reported open-source finding and validation counts, patching bottlenecks, and disclosed examples. | watch | 2026-10-19 | 90d | — |
| S024 | Anthropic — Measuring LLMs’ Ability to Develop Exploits — https://www.anthropic.com/research/exploit-evals | own-work | A | ExploitBench, ExploitGym, and SCONE evaluation goals and first-party model comparisons. | watch | 2026-10-19 | 90d | — |
| S025 | Mozilla — The Zero-Days Are Numbered — https://blog.mozilla.org/en/firefox/privacy-security/ai-security-zero-day-vulnerabilities/ | own-work | A | Mozilla’s first-party report of AI-assisted Firefox findings and the organizational response. | watch | 2026-10-19 | 90d | — |
| S026 | Cloudflare — Project Glasswing: What Mythos Showed Us — https://blog.cloudflare.com/cyber-frontier-models/ | own-work | A | First-party lessons on scoped parallel hunting, adversarial validation, deduplication, reachability, and report pipelines. | watch | 2026-10-19 | 90d | — |
| S027 | CVE-Bench — A Benchmark for AI Agents’ Ability to Exploit Real-World Web Application Vulnerabilities — https://arxiv.org/abs/2503.17332 | paper | A | A 2025 preprint benchmark for exploiting real vulnerable web applications and its reported success ceiling. | queued | 2026-10-19 | on-release | — |
| S028 | OpenAnt — LLM-Powered Vulnerability Discovery Through Code Decomposition, Adversarial Verification, and Dynamic Testing — https://arxiv.org/abs/2606.19149 | paper | A | A 2026 preprint on reachability filtering, adversarial verification, dynamic testing, and repository-scale analysis. | watch | 2026-10-19 | 90d | — |
| S029 | UK AI Security Institute — How Fast Is Autonomous AI Cyber Capability Advancing? — https://www.aisi.gov.uk/blog/how-fast-is-autonomous-ai-cyber-capability-advancing | docs | A | Independent government evaluation with explicit task-suite, token-cap, human-baseline, and confidence limitations. | watch | 2026-10-19 | 90d | — |
| S030 | UK NCSC — 10 Questions to Ask When Using AI Models to Find Vulnerabilities — https://www.ncsc.gov.uk/blogs/10-questions-ask-using-ai-models-find-vulnerabilities | docs | A | Operational questions on verification, vulnerability-handling capacity, sandboxing, data exposure, legality, and patching. | watch | 2026-10-19 | on-release | — |

**30 source rows — `grep -cE '^\| S[0-9]{3} ' corpus/SOURCES.md` (run after the draft rows are copied into that file).** **30 tier-A rows, 0 tier-B, 0 tier-C — `grep -E '^\| S[0-9]{3} ' corpus/SOURCES.md | awk -F'|' '{gsub(/ /,"",$5); print $5}' | sort | uniq -c` (same condition).**

## Candidate knowledge entries

All candidates below are **provisional, not admitted**. Each has an authoritative source and a bounded claim. The lane’s `corpus/QUALITY.md` is absent (`corpus/README.md:178-179`), so none can honestly be certified against the lane’s actual admission bar until that file is restored. The entries should carry explicit `source:`, `verified-at: 2026-10-19`, and `recheck:` metadata if later admitted; this is a metadata proposal, not a claim about the missing quality rubric.

### C1 — `cvss-v4-severity-and-vector.md`

- **Falsifiable claim:** Every report that publishes a numeric CVSS v4 score also publishes its vector and a nomenclature label that identifies the metric groups used; the report does not describe CVSS-B alone as a complete risk assessment.
- **Source and exact location:** S001, “CVSS Base Score (CVSS-B) Measures Severity, not Risk.” **Quote:** “CVSS Base (CVSS-B) scores are designed to measure the severity of a vulnerability and should not be used alone to assess risk.”
- **Coverage/frontier row filled:** New frontier row `CVSS v4 and evidence-calibrated severity`, linked to existing claim-package and policy-access coverage (`corpus/README.md:11-13`).
- **Recheck:** https://www.first.org/cvss/v4.0/user-guide, same section; compare against the current specification S002 on release.
- **Quality status:** Unverifiable against the missing `QUALITY.md`; candidate uses a primary spec, exact quote, and a testable reporting claim, but no local criterion can be certified.

### C2 — `coordinated-disclosure-timelines.md`

- **Falsifiable claim:** No general Kasegi guidance treats one disclosure interval as universal; every concrete deadline is attributed to the specific policy/coordinator and its trigger, with any extension condition kept explicit.
- **Source and exact location:** S006, p. 6, “Establish Reasonable Time Frames for Remediation and Disclosure of Reported Vulnerabilities.” **Quote:** “A time frame may be a fixed period, a minimum or maximum, or a negotiated default starting point.”
- **Coverage/frontier row filled:** New frontier row `CVD timelines and coordination`, extending the existing VDP package and policy-access coverage (`corpus/README.md:13,16`).
- **Recheck:** https://www.cisa.gov/sites/default/files/2026-07/joint-guide-establishing-a-cvd-program-to-work-with-security-researchers_508c.pdf, p. 6; cross-check examples against S014, S017, and S018 whenever those policies change.
- **Quality status:** Unverifiable against the missing `QUALITY.md`; the claim is falsifiable by source comparison and keeps policy choices attributed, but no local criterion can be certified.

### C3 — `authorization-safe-harbor-and-scope.md`

- **Falsifiable claim:** A program’s safe-harbor statement is never treated as expanding the asset list or authorizing an unlisted action; each candidate action is checked against the program’s actual scope and method rules.
- **Source and exact location:** S015, “How to Enable Safe Harbors.” **Quote:** “Adopting a Safe Harbor does not change the program scopes.”
- **Coverage/frontier row filled:** New frontier row `Authorization, scope, safe harbor`, complementing the current verbatim-scope, grant, prohibition, and null-safe-harbor checks (`SKILL.md:54-99`).
- **Recheck:** https://docs.hackerone.com/en/articles/8494502-safe-harbor-overview-faq, same section; compare the actual program’s current terms rather than relying on a platform-wide description.
- **Quality status:** Unverifiable against the missing `QUALITY.md`; supported by a primary platform policy and a bounded authorization rule, but no local criterion can be certified.

### C4 — `ai-assisted-finding-validation.md`

- **Falsifiable claim:** No AI-generated finding is described as confirmed solely because a model produced it; a claim-ready finding has independent reproduction/validation, an evidenced impact and reachability path, and any applicable program AI-use disclosure is honored.
- **Source and exact location:** S030, question 7, “Where should I start?” **Quote:** “look for ways to verify the results, by using both AI and humans.”
- **Coverage/frontier row filled:** New frontier row `AI-assisted discovery, verification, and maintainer capacity`; this adds general method evidence to the existing program-specific AI clauses (`SKILL.md:67-80,100-119`).
- **Recheck:** https://www.ncsc.gov.uk/blogs/10-questions-ask-using-ai-models-find-vulnerabilities, question 7; compare the current practice evidence in S023 and S026 on recheck.
- **Quality status:** Unverifiable against the missing `QUALITY.md`; the proposed claim has an observable admission test and primary guidance, but no local criterion can be certified.

### C5 — `cwe-top25-2025-methodology.md`

- **Falsifiable claim:** The 2025 list is not used as a per-target risk score or as a directly comparable prevalence trend without disclosing the changed mapping methodology and the use of CVSS 3.0/3.1 data in its score.
- **Source and exact location:** S004, “Removal of CWE Mapping Normalization.” **Quote:** “For the first time in 2025, the Top 25 used the actual CWE mappings as provided, without normalizing them back to View-1003.”
- **Coverage/frontier row filled:** New frontier row `CWE root-cause mapping and 2025 Top 25`, absent from the current coverage map (`corpus/README.md:7-36`).
- **Recheck:** https://cwe.mitre.org/top25/archive/2025/2025_methodology.html, “Scoring” and “Removal of CWE Mapping Normalization”; reread the annual edition when MITRE publishes a later list.
- **Quality status:** Unverifiable against the missing `QUALITY.md`; method is cited directly and the claim is limited to the methodology, but no local criterion can be certified.

**5 candidate entries — `grep -cE '^### C[1-5] — ' local://kaika-w1-kasegi-art.md`.**

## Study paths

1. **CVSS and root cause:** S001 FIRST User Guide → S002 FIRST Specification → S004 CWE methodology → S003 CWE list → S005 key insights. Learn score semantics first, then map a technically evidenced root cause, then interpret the global ranking with its methodology caveats.
2. **Authorization and disclosure:** S007 CISA VDP template → S015/S016 platform safe-harbor guidance → S006 joint CVD guide → S009 NIST SP 800-216 and S013 ISO 30111. Start with what is authorized and where to report; then study handling, triage, remediation, and multi-party disclosure. Apply the actual program policy, not a generalized template.
3. **AI-assisted research and safe operations:** S021 Naptime → S020 Big Sleep → S027 CVE-Bench and S024 exploit evaluations → S026 Cloudflare’s staged harness → S030 NCSC and S029 AISI limitations. Move from research method to a real finding, then benchmark interpretation, pipeline design, and governance/capacity constraints.

## Rejected knowledge candidates

These are intentionally rejected claims, with reasons retained as evidence of taste rather than converted into rules unsupported by the sources.

1. **“A high CVSS number is a complete risk or payout decision.”** Rejected: FIRST explicitly distinguishes Base severity from contextual risk, and program reward/severity policy is program-specific (S001; local related anti-pattern in `SKILL.md:590-608`).
2. **“Every coordinated disclosure should use a universal 90-day deadline.”** Rejected: opened primary policies differ, and CISA’s 2026 supplier guidance permits fixed, minimum, maximum, or negotiated default timeframes (S006, S014, S017, S018). Keep chosen deadlines attributed and policy-bound.
3. **“The 2025 CWE Top 25 tells a hunter which weakness will pay on this target.”** Rejected: the ranking aggregates CVE mappings and a frequency/severity formula, and its mapping normalization changed in 2025; it does not establish target scope, exploitability, or bounty reward (S003-S005).
4. **“A model-generated bug report is already a confirmed vulnerability.”** Rejected: NCSC recommends verification using both AI and humans, and the Glasswing report describes a human/independent assessment stage and maintainer capacity constraints (S023, S030). Discovery, reproduction, reachability, severity, and remediation are distinct evidence steps.
5. **“A safe-harbor badge authorizes all systems and methods.”** Rejected: the platform’s own guidance says safe harbor does not change program scope, while disclosure guidance calls for explicit scope and prohibited-method rules (S006, S015-S016).

**5 rejected knowledge candidates — `grep -cE '^[1-5]\. \*\*' local://kaika-w1-kasegi-art.md`.**

## Mistakes mined from Kasegi’s existing craft record

These ten items are **corpus-attested historical cases**, not independently rechecked against the now-absent external roots. They are mined from the lane’s current `SKILL.md` taxonomy (`SKILL.md:565-670`):

1. Internal verdict strings were used where a portal expected its own severity vocabulary and CVSS (`SKILL.md:590-596`).
2. Severity language was both hedged below evidence and inflated beyond demonstrated impact (`:597-608`).
3. A report’s absolute “no live host was contacted” claim contradicted recorded earlier GET/HEAD reconnaissance (`:609-614`).
4. Internal authorization/orchestration material was attached where only triage-useful proof belonged; the recorded WordPress package had 17 attachments against a 3-file allowlist (`:615-621`).
5. Historical `claim-ready` tags and stale generated metadata were treated as current authority rather than checking current package bytes and gates (`:622-635`).
6. Empty `in_scope_assets` was overclaimed as “no scope,” despite the schema meaning “none observed in this response” (`:636-638`).
7. **Claiming safe harbor the program doesn't grant** — a recorded program's language covered active exploits only, not routine research (`SKILL.md:640-643`).
8. **Manufactured findings** — an invariant rejects inventing findings; an honest zero is an acceptable bounded result (`:644-651`).
9. **Precondition laundering** — a local PoC was treated as if it proved live impact; the source records explicit precondition gates and resume conditions (`:652-664`).
10. **Treating DONE as claimable** — a DONE state alone did not satisfy claimability, evidence-binding, review, and safety gates (`:665-670`).

Together these ten mined classes capture disclosure defects and research/claim-integrity failures documented in the lane’s current skill record; they remain historical claims whose named external artifacts are not currently available for independent re-open.

**10 mistakes mined — `awk '/^## Disclosure anti-patterns / {section=1; next} section && /^## / {exit} section && /^[0-9]+\. \*\*/ {n++} END {print n+0}' /home/vgpnk/Projects/shokunin/kasegi-shokunin/SKILL.md`.**

## Leads (unopened)

These are not SOURCES rows because they were not opened in this session; they are leads only.

- ISO/IEC WD 30111.2 vulnerability-handling work item: https://www.iso.org/standard/92946.html
- FIRST, Guidelines and Practices for Multi-Party Vulnerability Coordination and Disclosure, v1.1: https://www.first.org/global/sigs/vulnerability-coordination/multiparty/guidelines-v1-1
- EU Cyber Resilience Act official text, for EU-specific legal requirements: https://eur-lex.europa.eu/eli/reg/2024/2847/oj/eng
- ExploitGym original evaluation/preprint: https://arxiv.org/abs/2605.11086
- CVE CNA Operational Rules and assignment guidance: https://www.cve.org/ResourcesSupport/AllResources/CNARules

## Recommendations

1. Restore and apply the lane’s real `corpus/QUALITY.md` before admitting any new entry; keep these five as candidates until their evidence and quality gate are reviewed.
2. Add one narrow Frontier area for authorization/CVD and one for evidence-calibrated technical assessment (CVSS/CWE/AI verification); keep program-specific policy facts separate from general practice.
3. When authoring the registry, retain all 30 primary sources with explicit opened/recheck fields, and keep self-reported AI results marked as first-party evidence rather than independent consensus.
