# ART dossier — revenger

**Research date:** 2026-10-19  
**Domain:** Binary forensics and RE evidence-ledger discipline  
**Scope:** Read-only source research. Sources listed below were opened in this session; fetched text was treated as data. No instruction-like prompt injection was observed.

## Findings in brief

**Observed locally.** `PROVINCE.md:3-7` says revenger owns reverse engineering of shipped artifacts and requires each conclusion to distinguish observation, inference, and unknown while citing Evidence IDs. `PROVINCE.md:9-16` identifies the REA skill/toolset, a knowledge seed, and host readiness as sources. The visible knowledge filenames are `corpus/knowledge/seed.md` and `corpus/knowledge/2026-10-12-rea-readiness-checklist.md`; I read filenames only, not their bodies.

**Observed local contract defects.** The ART inputs `corpus/README.md`, `corpus/QUALITY.md`, and root `SKILL.md` each returned “not found”; they are also absent from the lane root/corpus listings. Thus there is no visible coverage map or Frontier table to map proposed research into, no lane-specific admission criteria to apply, and no skill headings to assess. This is not proof the knowledge bodies lack related facts: those bodies were intentionally not read.

**Inference.** The lane already has an explicit general evidence-ledger principle, but its visible knowledge filenames do not identify topic entries for chain of custody, acquisition integrity, or forensic-tool validation. The research below proposes those topics as candidate coverage; it does not claim they are absent from unseen text.

**Unresolved.** Existing citation use in the two knowledge files, the intended `QUALITY.md` threshold, any previous round mistakes, and the exact intended coverage/frontier row names remain unknown. This ART pass did not inspect `LOG.md`, lessons, or `SCORECARD.md` because they are outside the named ART inputs; consequently it mines no lane-round mistakes.

## Research counts

Counts are reproducible against this artifact. The tier command uses the registry's fourth field (`tier`).

- Sources opened and listed: **25** — `grep -cE '^\| S[0-9]{3} ' local://kaika-w1-revenger-art.md`
- Tier A: **25** — `awk -F'|' '/^\| S[0-9]{3} / {gsub(/ /,"",$5); n[$5]++} END {print n["A"]+0}' local://kaika-w1-revenger-art.md`
- Tier B: **0** — `awk -F'|' '/^\| S[0-9]{3} / {gsub(/ /,"",$5); n[$5]++} END {print n["B"]+0}' local://kaika-w1-revenger-art.md`
- Tier C: **0** — `awk -F'|' '/^\| S[0-9]{3} / {gsub(/ /,"",$5); n[$5]++} END {print n["C"]+0}' local://kaika-w1-revenger-art.md`
- Candidate knowledge entries: **5** — `awk '/^### Candidate — / {n++} END {print n+0}' local://kaika-w1-revenger-art.md`
- Rejected research candidates: **4** — `awk '/^- Rejected candidate: / {n++} END {print n+0}' local://kaika-w1-revenger-art.md`
- Lane-round mistakes mined in this ART dossier: **0** — `awk '/^### Mined mistake: / {n++} END {print n+0}' local://kaika-w1-revenger-art.md` (not a claim that the lane has no mistakes; round records were not inspected).
- Missing required ART inputs observed: **3** — from the lane repository root: `for p in corpus/README.md corpus/QUALITY.md SKILL.md; do test -f "$p" || printf '%s\n' "$p"; done | wc -l`

## Uncovered ground and current art

### Coverage boundary

The local province grounds revenger in shipped-artifact reverse engineering and an evidence-ledger discipline (`PROVINCE.md:3-7`). The repository has visible generic REA knowledge filenames, but the missing `corpus/README.md` prevents reading its coverage map and `## Frontier`; missing `corpus/QUALITY.md` prevents deciding whether any candidate meets the lane's admission bar; missing `SKILL.md` prevents comparing topic coverage to its learning path. The statements below are therefore *index-level gaps and proposed coverage*, not negative claims about unseen file bodies or old lessons.

### Current art surfaced

- **Current operational handling guidance:** SWGDE's opened pages identify final 2025 revisions for computer evidence collection (18-F-002-2.0), computer forensic acquisition (17-F-002-2.1), computer examination (18-F-001-2.0), and mobile-device evidence collection/acquisition (18-F-003-2.0). The documents emphasize contemporaneous records, device state, item identifiers, transfer details, acquisition hashes, tool versions/settings, errors, and scope-specific deviations. Mobile handling has additional volatile-state, power, network-isolation, and dynamic-data risks; a generic disk-image recipe cannot stand in for mobile-specific preservation.
- **Tool-validation now has an actionable baseline:** SWGDE 18-Q-001-2.1 (2024) says testing is function- and category-oriented, may use known data or competent external reports, should retain limitations and results, and is not always pass/fail. The NIST CFTT pages identify test specifications, procedures, criteria, sets, and test hardware; the DHS report index is organized by test category and publication date.
- **Concrete CFTT evidence is narrow and useful:** the opened Forensic Explorer report tests graphic-file carving only for tool version 5.6.8.4340, with named file types and image layouts. It reports both false positives and incomplete/extra-content behaviors for some cases. It is an example of why a report must be bound to exact tool version, feature, input data, settings, and observed anomaly—not treated as a product-wide approval.
- **Reference data is growing:** the opened NIST CFReDS portal describes documented datasets for testing tools, learning tool behavior, and training; its visible list includes 2025 CFTT cloud datasets and later additions. The specific 2025 CDX dataset page did not render detailed item content in this session, so its contents are not assessed here.
- **Evidence-management work in 2025:** the NIJ page for the NIST/NIJ Evidence Management Steering Committee report (published September 2025) describes recommendations on retention, preservation, integrity, and disposition, grounded in a survey, research review, stakeholder workshop, and report. This widens context beyond acquisition hashes to lifecycle and institutional evidence management.
- **Hash standards need currency awareness:** FIPS 180-4 specifies digest algorithms for detecting message change, and FIPS 202 specifies SHA-3/SHAKE. NIST's FIPS 180-4 revision notice says SHA-1 is to be removed but the revision effort had not begun as of that notice; the NIST CAVP secure-hashing page, updated September 2026, still lists SHA-1 among tested algorithms. Do not read a test listing as a recommendation. Record the chosen algorithm, digest, byte scope, and time; verify the applicable current policy before selecting algorithms. Hash equality supports fixity for the hashed bytes; it does not alone establish source authenticity, acquisition completeness, custody history, or a valid interpretation.
- **Canonical references remain useful but are not current operating procedures:** NIST SP 800-86 is an older IT incident-response-oriented guide and explicitly says it is not an all-inclusive, step-by-step law-enforcement guide. RFC 3227 is a 2002 IETF BCP with collection and custody fundamentals; it should supplement, not replace, recent device- and jurisdiction-specific guidance. ENFSI's digital-technology BPM is Version 01 (November 2015), a knowledge-base framework rather than an SOP; use it as historical quality context alongside updated domain guidance.
- **Standards status must be rechecked:** ISO's catalog describes ISO/IEC 27037:2012 as the identification/collection/acquisition/preservation standard; its lifecycle text contains review information, so this dossier does not infer future stability. IEC catalog pages summarize ISO/IEC 27041:2015 (method suitability) and ISO/IEC 27042:2015 (analysis/interpretation). The ISO catalog page for ISO/IEC 27043:2015 gives a broad investigation-process scope and also records review lifecycle activity. Only catalog/abstract pages were read, not the full standards.

**Coverage proposal:** add a map/frontier row for *Evidence provenance and custody across collection → acquisition → handling → preservation*, a row for *Tool/process validation against known truth and documented limitations*, and a row for *Hash/fixity claims versus chain-of-custody and archive evidence*. These are proposals for Wave 2; there are no observed existing rows to replace or extend.

## Candidate knowledge entries

These are candidates, not admitted knowledge entries. For each, the included excerpt is at most 25 words and names its exact location. The cited source was opened in this session. Because `corpus/QUALITY.md` is missing, none can honestly be certified against the lane's actual quality gate. Provisional admission evidence would need to show a primary source, a narrow falsifiable claim, exact provenance, an explicit limitation, and a recheck path; the non-author verification gate must also be retained. Wave 2 must compare each candidate with the real `QUALITY.md` before admission.

### Candidate — `custody-transfer-ledger.md`

- **Falsifiable claim:** A custody-transfer record is incomplete if it cannot link each transfer to a unique evidence identifier, transferring person, receiving person/facility, and date/time; a sample ledger validator should reject each missing field and unlinked transfer.
- **Source and location:** S018, SWGDE *Best Practices for Digital Evidence Collection*, §14 “Documentation”; corroborate with S019, SWGDE *Best Practices for Computer Forensic Acquisitions*, §9 “Documentation.”
- **Quote:** “The chain of custody documentation should be contemporaneous to the collection” — SWGDE 18-F-002-2.0, §14.
- **Coverage row filled:** proposed *Evidence provenance and custody* map/frontier row; no existing map row was available to inspect.
- **Recheck:** compare the proposed ledger fields against S018 §14 and S019 §9; cite the versions in the eventual entry. Re-open the SWGDE current-document page before mining because SWGDE explicitly advises checking for revisions.
- **Quality status:** not assessable against missing `corpus/QUALITY.md`; a validator and independent reviewer should be required before admission.

### Candidate — `acquisition-fixity-and-coverage.md`

- **Falsifiable claim:** A matching acquisition hash only supports equality over the bytes actually hashed; an acquisition report that omits source/target scope, verification method, or read errors cannot support a whole-source completeness claim.
- **Source and location:** S019, SWGDE *Best Practices for Computer Forensic Acquisitions*, §§8–10 “Verification and Preview,” “Documentation,” and “Preservation.”
- **Quote:** “Verification is the validation of the integrity of the acquired data” — SWGDE 17-F-002-2.1, §8.
- **Coverage row filled:** proposed *Acquisition integrity and hash-scope limits* row.
- **Recheck:** S019 §8 says verification may not verify all source data (for example, unreadable or excluded regions); §9 specifies acquisition documentation fields. Recheck against a known fixture where source and acquisition scope are independently known.
- **Quality status:** not assessable against missing `corpus/QUALITY.md`; require a negative case (mismatch or unreadable region) so the claim is not merely a hash-success example.

### Candidate — `tool-validation-by-function-and-version.md`

- **Falsifiable claim:** A tool-validation claim must name the tested function and tool/version plus representative inputs/settings; evidence for one function/version does not validate untested functions or versions. The proposed check is to reject a validation row lacking any of those identifiers or an observed limitation/result.
- **Source and location:** S017, SWGDE *Minimum Requirements for Testing Tools Used in Digital and Multimedia Forensics*, §§2, 4, and 5; compare S013–S016 for CFTT methods and one bounded report.
- **Quote:** “Testing is not necessarily pass/fail.” — SWGDE 18-Q-001-2.1, §4.
- **Coverage row filled:** proposed *Forensic tool/process validation and calibration* row.
- **Recheck:** use a known dataset and compare the claim to S017's test type/frequency recommendations; use S016 only for its documented graphic-file-carving function and version. Cite the exact test report rather than generalizing from a product name.
- **Quality status:** not assessable against missing `corpus/QUALITY.md`; preserve test failures, anomalies, and rejected tool claims rather than flattening them into a pass/fail badge.

### Candidate — `reproducible-finding-ledger.md`

- **Falsifiable claim:** Every reported interpretation should link to its exact input, operation/method, tool/version, recorded output and limits so an independent reviewer can scrutinize or repeat it; the lane's existing province additionally requires OBSERVATION/INFERENCE/UNKNOWN separation and Evidence IDs.
- **Source and location:** S007, IEC catalog description of ISO/IEC 27042:2015, abstract; local contract at `PROVINCE.md:3-7`.
- **Quote:** “recording sufficient information to allow such processes to be subjected to independent scrutiny when required” — ISO/IEC 27042:2015, IEC catalog abstract.
- **Coverage row filled:** proposed *Repeatable analysis, interpretation, and evidence-linked claims* row.
- **Recheck:** run the eventual ledger checker over a deliberately incomplete sample and confirm it identifies missing Evidence ID, input identity, method/version, or uncertainty/coverage fields; compare the expected fields to S007's abstract and `PROVINCE.md:3-7`.
- **Quality status:** not assessable against missing `corpus/QUALITY.md`; must not turn the ledger schema into a claim that a tool result is true.

### Candidate — `long-term-fixity-evidence-records.md`

- **Falsifiable claim:** For material requiring long-term preservation, a durable evidence record must permit verification of archived-object integrity/existence over time and document renewal when cryptographic mechanisms become weak; this is a separate archive-preservation claim, not a substitute for transfer-by-transfer custody records.
- **Source and location:** S005, RFC 4998, §§1.1–1.2 “Motivation” and “General Overview and Requirements.”
- **Quote:** “This document specifies the syntax and processing of an Evidence Record, a structure designed to support long-term non-repudiation of existence of data.” — RFC 4998, Abstract.
- **Coverage row filled:** proposed *Long-term evidence preservation and algorithm-transition limits* row.
- **Recheck:** verify a retained Evidence Record using the RFC's generation/verification procedures; for any algorithm choice, recheck S009–S012 rather than assuming an older digest remains acceptable.
- **Quality status:** not assessable against missing `corpus/QUALITY.md`; admit only if long-term archival integrity is a lane need, and explicitly keep this separate from operational chain of custody.

## Study paths

- **Collection and custody:** S018 → S019 → S002 → S003 → S005. Start with current collection records, move to source/acquisition verification and preservation, then use ISO's handling scope and NIST evidence-preservation framing; finish with RFC 4998 only for long-term archive evidence.
- **Tool validation:** S017 → S013 → S014 → S023 → S016. Move from lab testing requirements to CFTT methodology, then test-data sources and a real version/function-scoped report; record false positives and limitations as findings, not cleanup noise.
- **Analysis and hash discipline:** S006 → S007 → S008 → S001 → S009/S011/S012. Read method fitness, interpretation, and investigation-process scope before legacy incident-response context; then distinguish a digest algorithm specification from policy status and algorithm validation.

## Rejected candidates and reasons

- Rejected candidate: treat SHA-256/SHA-3 output alone as proof of chain of custody or complete acquisition. A digest standard specifies hash behavior; it does not identify each custodian, account for transfer events, establish source authenticity, or prove that every source byte was acquired.
- Rejected candidate: use RFC 3227 alone as a current forensic acquisition SOP. It is a useful IETF BCP foundation for evidence collection, notes, volatility, and custody, but is from 2002 and is not a current device-specific or jurisdiction-specific operating procedure.
- Rejected candidate: promote a single CFTT report into a product-wide endorsement. The opened report is limited to one tested tool version and graphic-file-carving behavior; any use beyond that scope is unsupported.
- Rejected candidate: infer complete normative requirements from ISO catalog pages. The pages provide authoritative metadata and abstracts, but the full ISO/IEC standards were not read; no clause-level claims beyond the visible descriptions are admitted here.

## Mistakes mined

No lane-round mistakes were mined. `LOG.md`, `SCORECARD.md`, and `corpus/lessons/` are not named ART inputs and were not opened; do not interpret this as a sweep finding of zero rejected, harmed, honest-stop, or corrected rounds. The four rejections above are research-selection decisions, not mined lane mistakes.

## Leads (unopened)

- Full normative texts for ISO/IEC 27037, 27041, 27042, and 27043; this session opened official catalog descriptions/abstracts only. Confirm present lifecycle/revision status before using any version as current.
- Individual NIST CFTT test plans/specifications, raw test sets, and reports beyond the specific graphic-file-carving report in S016; the CFTT technical index was opened, but these linked materials were not.
- The item-level detail and files for the CFReDS 2025 CDX Cloud Datasets v1.1 entry. The CFReDS portal was opened; the specific item page did not return detailed content.
- The full September 2025 NIJ Evidence Management Steering Committee report and its associated NIST SP 1500-33B/33C survey and research review; only the NIJ landing page and abstract were opened.
- Current local citation coverage within `seed.md` and `2026-10-12-rea-readiness-checklist.md`; filenames only were inspected.

## Recommendations for Wave 2

- Restore or create the missing lane ART inputs before proposing a round that changes corpus structure: coverage map/Frontier, explicit `QUALITY.md` admission criteria, and `SKILL.md` learning path. Do not silently fabricate their contents in this dossier.
- Prioritize a narrow round that builds a fixture-backed chain-of-custody/acquisition ledger, distinguishes byte fixity from acquisition completeness, and requires an independent verifier; bind each measurement to a pasteable command and to the lane's existing per-claim axes.
- Build tool-validation entries around exact feature/version, known-truth test data, settings, anomalies, and test-report scope. Use the 2025 SWGDE guidance and current CFTT materials; keep mobile and volatile/live acquisition as distinct, specialized cases.
- Keep each sourced fact in `knowledge/` and every opened learning lead in the eventual append-only `SOURCES.md`. These opened sources are all queued/watch, not mined: no candidate entry has yet been admitted or cited by a lane knowledge file.
