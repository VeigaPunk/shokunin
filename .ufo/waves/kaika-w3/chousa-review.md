# kaika W3 — non-author verification: chousa round 24

Reviewer: W3ReviewChousa (fresh task dispatched by the orchestrator; not the lane's author).
Lane commit: `6572827a39760f293c5401cabf08a5ce387af073` (branch `kaika/round`, base `ab19cff53`).
Report under review: `.ufo/reports/round-24/chousa.md` (fleet-ledger worktree).
Scope: read-only. Scratch `/tmp/kaika-verify/chousa/` (removed at end). Recommendation only.

Trees used: `before` = `git archive ab19cff53`; `after` = `git archive 6572827a3`; `before-l` = `before` plus the landed `corpus/lessons/round-24.md` (the claim-3 count needs it, as the lane's own before-log did).

Incident: the shared parent `/tmp/kaika-verify/` was reset at 19:13 (dir mtime `2026-10-19 19:13:51`) and `/tmp/kaika-verify/chousa/` vanished mid-review. I did not identify the actor (sibling W3 reviewers use the same parent). I rebuilt my trees from git and re-ran the affected checks (drift, full-r6). Earlier results were not affected: they were recorded before the reset.

## 1. Provenance — PASS
Command: `git -C <W> log --format='%h %an <%ae> | %cn <%ce> | %s' ab19cff53..6572827a3`
Output: `6572827 chousa-shokunin <chousa@shokunin.local> | chousa-shokunin <chousa@shokunin.local> | round-24: --json delimiter edge closed ...`
One round commit; author and committer are the lane identity.

## 2. Append-only — PASS (with notes)
Command: `git -C <W> diff --numstat ab19cff53..6572827a3`
- `LOG.md` 11+ / 0−; `corpus/QUALITY.md` 48+ / 0−; `corpus/lessons/round-24.md` new file (86+ / 0−); `corpus/SOURCES.md` new file (83+ / 0−). No prior line deleted or modified in the three named surfaces.
- `corpus/knowledge/verification-r16.md` 10+ / 0− (addendum, rows unchanged).
- Outside the named set, for the record: `SKILL.md` 12+ / 7− (the seven deleted lines are the gate-row selftest count `133` → `136`, disclosed in the report); `corpus/evidence/README.md` 19+ / 1− where the 1 deleted line is `round-1 receipt blocker stands (operator-side).` re-added unchanged with a trailing newline (`\ No newline at end of file`). Content identical; byte-level EOF change only.
- `corpus/SOURCES.md` did not exist at base, so no in-place edit occurred; the lesson's `Rows touched old→new: none` is consistent.

## 3. Claims — each re-run at both trees
Counting command for all three claims: `bash <tree>/corpus/evidence/round24-measure.sh <tree> [<bar>]` (run from the after-tree script against both trees; the before-tree has no script of its own).

| Claim | Command | Before (ab19cff53) | After (6572827a3) | Report says | Verdict |
|---|---|---|---|---|---|
| 1 operability (delimiter edge) | script §claim 1 | `MANIFEST_LINES=1 INVALID_JSON_LINES=1` | `MANIFEST_LINES=2 INVALID_JSON_LINES=0` | same | **verified** |
| 1 score re-derived (criterion 12) | script §score | `VERDICT_BEARING_EXPORTS=3/3` | `VERDICT_BEARING_EXPORTS=3/3` | 3 → 3 | **verified** (score unchanged) |
| 1 selftest | `bash tools/research-gate.sh --selftest` | `RESEARCH_GATE_SELFTEST: PASS (133 cases, 0 skipped)` | `PASS (136 cases, 0 skipped)` | 133 → 136 | **verified** |
| 1 cases 1–133 stable | `diff <(head -133 before.out) <(head -133 after.out)` | — | identical | byte-identical | **verified** |
| 1 mutants | copy of after tree, one edit each, `--selftest` | m1 `if false` on prefix arm → `FAIL (2/136)` (cases 134, 135); m2 old `$(tail -c1)` probe → `FAIL (1/136)` (case 135); m3 refusal → `if false` → `FAIL (1/136)` (case 136) | — | each fails its pinning case | **verified** |
| 1 drift | `bash tools/research-gate.sh --drift corpus/evidence/gate-baseline-r12-20261019T115519Z.json` | `GATE_DRIFT: none`, exit 0 | `GATE_DRIFT: none`, exit 0 | none | **verified** |
| 1 full-r6 verify-all | `verify-all corpus/fixtures/full-r6.md --root .` | identical output | identical output (modulo timestamps) | battery identical | **verified** for this fixture (receipt battery not re-run in full) |
| 2 coverage + registry | script §claim 2 | `EXPANSION_ADMITTED=0/3`; `corpus/SOURCES.md absent` | `EXPANSION_ADMITTED=3/3` | 0/3 → 3/3 | **verified** (before is an absence; see D-2) |
| 2 SOURCES census | script §census; contract v1 census | — | `rows: 18`, `malformed: 0`, `tiers: A=14 B=1 C=3`, `status: mined=8 queued=7 rejected=3`, `dup-ids: []`, `enum/inflation: []`, `missing-used-by: []`, `sections: 4/4` | same | **verified** |
| 2 census validator | `bash <fleet-census>/scripts/sources-census.sh validate <W>` | — | `chousa-shokunin	ok	<W>/corpus/SOURCES.md`, exit 0 | exit 0 | **verified** |
| 2 validator discernment | same validator on a copy with S016 tier changed to `A` and a `mined` row S099 with missing `used-by` path | — | `E10 S016 community-at-A`, `E11 S099 missing used-by`, exit 1 | — | validator works |
| 3 calibration | script §claim 3 | `MISTAKE_CLASSES=14 CAPTURED_BY_CRITERION=3 UNCAPTURED=11` | `MISTAKE_CLASSES=14 CAPTURED_BY_CRITERION=13 UNCAPTURED=1` | 3 → 13 | **verified** (mechanical; see D-3) |

Before/after log files: my re-runs match the committed `round24-measure-before.log` and `-after.log` line for line (only the tree label and the `ab19cff:` bar label differ).

Recheck-only items (entry `recheck:` commands): `grep -n 'None of the five proves semantic support' corpus/README.md` → line 164 (claim-support entry, present). `verify-chain` see §5.

## 4. SOURCES — PASS
- `bash /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/fleet-census/scripts/sources-census.sh validate /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/chousa-shokunin` → `chousa-shokunin	ok	/home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/chousa-shokunin/corpus/SOURCES.md`, **exit 0**.
- Validator selftest: `sources-census.sh selftest` → `selftest ok`, exit 0.

Re-opened rows (14 of 18: 13 web, 1 local; live fetch by curl/pdftotext, or the reader tool where curl was blocked):

| Row | Tier / status | Anchor checked | Gate quote | Result |
|---|---|---|---|---|
| S013 JSON Lines (jsonlines.org) | A, mined | Requirement 3 | "If a line terminator follows the last JSON value in a file, it must be the last byte in the file" | **verbatim, present** (count 1) |
| S006 Cited but Not Verified (arXiv 2605.06635v1) | A, mined (NEW tier-A) | §3.3, §3.3.3 | §3.3.3 "citations where the source exists and is topically relevant but does not support the specific claims attributed to it" | **present** (count 1) |
| S006 (same) | A, mined | §3.3 | lesson Gate: "Link Works verifies URL accessibility, Relevant Content measures topical alignment, and Fact Check validates factual accuracy against source content" | **not verbatim**: source reads "(1) Link Works verifies URL accessibility, (2) Relevant Content measures topical alignment, and (3) Fact Check validates…"; the enumerators were dropped (count 0 for the lesson string) |
| S005 Chen et al. (ACL 2025.acl-long.1534) | A, mined (NEW tier-A) | §4 p.5; §6 p.8; Fig 1 fn 1 p.1 (pdftotext per page) | "Assessing citation fidelity requires measuring how faithfully a citation reflects the original findings of the cited work" (p.5); "scientific claims can evolve or degrade, as they are repeatedly paraphrased…" (p.8); "The low-fidelity citation case overstates conclusions…" (p.1) | **present; page numbers match** the entry |
| S007 DeepResearch Bench II (arXiv 2601.08536v3) | A, mined | §2.1 | "this only measures the accuracy of the citations and does not necessarily confirm that the information is correct" | **present** |
| S002 IFCN Code of Principles | A, mined | Principle #2 criteria | "uses the best available primary, not secondary, sources of evidence wherever suitable primary sources are available" | **present** |
| S004 Cochrane Handbook ch.24 | A, mined | §24.2.1.3 | "We advise caution in assessing NRSI according to existing 'evidence hierarchies'…" | **present** |
| S003 SIFT (hapgood.us) | A, mined | "Trace claims…" | "trace the claim, quote, or media back to the source…" | **present** |
| S010 CiteEval (ACL 2025.acl-long.1574) | A, queued | Abstract | "…which we argue is a suboptimal proxy" | **present** |
| S011 TREC 2025 RAG overview | A, queued | §1 | "Each sentence in a generated answer is checked against its cited document to verify factual grounding" | **present** in the PDF text (count 1) |
| S018 Schreieder et al. survey | B, queued | Abstract | "we systematically analyze 134 papers, introduce a unified taxonomy" | **present** |
| S014 OCEBM 2011 | C, rejected | opening | "no evidence ranking system or decision tool can be used without a healthy dose of judgement and thought" | **present** (reader tool; curl got 403) |
| S015 OpenAI deep research | C, rejected | "Limitations" | "It can sometimes hallucinate facts in responses or make incorrect inferences, though at a notably lower rate…" | **present** |
| S016 Wikipedia Hierarchy of evidence | C, rejected | Criticism | "hierarchies are a poor basis for the application of evidence in clinical practice" | **present** |
| S001 (own-work) | A, mined | `tools/research-gate.sh` | "A manifest whose last byte is not '\n' (hand-edited, truncated, or written by another tool) would glue this object onto its last line" | **present** at `tools/research-gate.sh:2490`; case names at `:5189-5192` |

Only S006's Gate quote is inexact (see D-4).

## 5. Knowledge entries — headers and rechecks
- Header trio (`source:` / `verified-at:` / `recheck:`) present in all four new entries: `json-delimiter-r24.md`, `claim-support-states-r24.md`, `citation-chain-fidelity-r24.md`, `contextual-source-admission-r24.md`.
- QUALITY 6 linkage (each `source:` S### row `mined` with `used-by` naming the entry): S001→json; S013→json; S006,S007→claim-support; S005→citation-chain; S003→citation-chain + contextual; S002,S004→contextual. Confirmed by the script's `EXPANSION_ADMITTED=3/3`.
- Recheck runs:
  - json-delimiter: `bash tools/research-gate.sh --selftest` → `PASS (136 cases, 0 skipped)` ✓.
  - claim-support: `grep -n 'None of the five proves semantic support' corpus/README.md` → line 164 ✓ (the bullet continues on line 165 with "uniqueness or the source's own truth").
  - citation-chain: the stated command `bash tools/research-gate.sh verify-chain corpus/fixtures/chain-r3.md --root ..` **does not reproduce** from the tower worktree: `RESOLVED_HOPS=0/22`, `RESEARCH_GATE: DRIFT (... refused=17 ...)` exit 1, because `..` (`.tower/worktrees/kaika`) does not contain `research/`. With `--root /home/vgpnk/Projects/shokunin` the same command gives `RESOLVED_HOPS=17/22` `RESEARCH_GATE: CLEAN` exit 0, matching the entry; the broken control `chain-r3-broken.md` gives `RESOLVED_HOPS=1/2` DRIFT exit 1. → Recheck command is location-dependent (D-5).
  - contextual-source-admission: `on-release`, no command. Admitted by QUALITY 6 wording; S002/S003/S004 re-opened ✓.
- Entry claim vs source: json (S013 §3 quote ✓; receipts ✓, see §3); claim-support (S006 §3.3.1 "Link Works assesses URL accessibility without LLM inference." ✓; S006 §3.3.3 ✓; S007 §2.1 ✓); citation-chain (S005 page quotes ✓; "0.06" and "13 million" appear in S005 ✓; the extension to web chains is labelled Inference ✓); contextual (S002/S003/S004 quotes ✓; "analogy" labelled ✓).
- Receipts cited by json entry, re-read: `json-r24-…-demo.log` lines 14/16 (`MANIFEST_LINES=1 INVALID_JSON_LINES=1` → `2`/`0`), 32–40 (mutant FAIL lines), `…-battery.log:2` `ALL IDENTICAL (183 lines; 8 runs …)`, `…-drift.log:1` `GATE_DRIFT: none`.

## 6. Discernment spot-check (LEARNING.md) — sample of 7 gate decisions (4 admit, 3 reject)

| # | Decision | Item | Verdict | Reason |
|---|---|---|---|---|
| A1 | admit | `corpus/knowledge/claim-support-states-r24.md` | **agree** | Four-state separation rests on S006 §3.3 and S007 §2.1, both verbatim at the anchors; S006 results (model evaluations) are kept out and labelled kengaku; state 4 is labelled an inference. |
| A2 | admit | `corpus/knowledge/citation-chain-fidelity-r24.md` | **agree** | S005 quotes verified at pp.5/8/1; numbers 0.06 and 13M present; the transfer from S2ORC to web chains is labelled Inference. Caveat: the resolve-only limit was already held by `chain-resolution-r3.md:133` and `anchor-boundaries-r4.md:131`, so the "uncovered" ground is partly the new fidelity method, not the boundary itself. |
| A3 | admit | `corpus/knowledge/json-delimiter-r24.md` | **agree** | S013 quote verified; receipts and mutants re-run; limits (concurrency, CRLF, NUL) stated. |
| A4 | admit | `corpus/knowledge/contextual-source-admission-r24.md` | **agree** | S002/S003/S004 quotes verified; cross-domain analogy explicitly labelled "analogy… the lane's construction". |
| R1 | reject | S014 OCEBM 2011 (tier C) | **agree** | Text confirms the scope ("a hierarchy of the likely best evidence"; "NOT intended to provide you with a definitive judgment") and rejects universal use. |
| R2 | reject | S015 OpenAI launch page (tier C) | **agree (reason imprecise)** | Outcome right; the vendor's own statement "according to internal evaluations" supports the rejection. "Capability numbers rest on self-reported internal evaluations" overstates: HLE and GAIA are public benchmarks (GAIA leaderboard linked). Flip stated. |
| R3 | reject | S016 Wikipedia Hierarchy of evidence (tier C) | **agree** | Tertiary, community-edited; Criticism-section quote verified. |

Sample result: **7/7 agree** (one reason imprecise). Limits: small sample; the three rejections are easy calls (vendor page, tertiary wiki, 2011 scoped ladder); the rejected-candidate sweep's search log says it stopped at three "because the round assignment asked for at least two rejections" (the search log, SOURCES.md `## Search log`) — a quota-driven stop (D-6). The lesson's `## Gate` has no spot-check slot yet (LEARNING requires one; see D-8).

## 7. Credentials — PASS
`git -C <W> diff ab19cff53..6572827a3 | grep -nE 'op://[A-Za-z0-9]|BEGIN [A-Z ]*PRIVATE KEY|ghp_[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}|xox[baprs]-[A-Za-z0-9]'` → no output (grep exit 1); 1108 added lines scanned (`grep -c '^+[^+]'`).

## 8. Report — conformance
- Sections present in order: Work performed; Landed changes; Before → after measurements; SHONEN; Sources & frontier; Mistakes; Trend verdicts; L0 questions; Integrator notes. ✓
- Round commit cited (`6572827a3…`) and gate shas (`b5d0f93d…` → `752e4e38…`) match the tree (`gate` line in both logs). ✓
- No `[x]` in SHONEN; four `[~]` with pointers. ✓ But `SHONEN.md` in the tree still has four `- [ ]` boxes (`grep -nE '^\s*- \[' SHONEN.md`); no `SHONEN.md` change in the diff. The report's `[~]` is not reflected in the file (D-7).
- Mistake pointers spot-checked against base: `SKILL.md:432-434` ✓; `considerthese/2026-10-19.md:3` ✓; `SCORECARD.md:1175` ✓; `LOG.md:816-820` ✓; `SCORECARD.md:7` ✓.
- Not verified by me: the claim of a batched 10-member L2 call and godspeed/directive prompt bytes (transcripts not checked; outside my check list).

## Per-claim verdicts (recommended)
1. **operability — verified.** Defect closed as measured (INVALID 1→0), selftest 133→136 with cases 1–133 identical, three mutants killed, drift none, full-r6 identical. Axis score unchanged at 3 (re-derived 3/3).
2. **coverage + registry — verified.** Registry exists and validates (exit 0); three entries admitted with mined rows; validator demonstrably fires on a broken copy.
3. **calibration — verified (mechanical).** 3/14 → 13/14 reproduced; the captured-by column is written by the lane (see D-3).

## Recommended per-axis verdicts (axes the lane scores or names)
| Axis | Score | Recommended verdict | Evidence |
|---|---|---|---|
| operability | 3 → 3 (`VERDICT_BEARING_EXPORTS=3/3`, both trees) | **score unchanged; claim 1 verified as defect closure** — the report's "improved" label should read "defect closed; score unchanged" (D-1) | §3 |
| coverage (unscored) | — | **improved (qualified)** | §3, §6 |
| calibration (unscored) | — | **improved (qualified)** — mechanical count (D-3) | §3 |
| depth (unscored) | — | **unchanged** (agree; not claimed) | report |
| freshness (unscored) | — | **unchanged** (agree; drift none; knowledge entries 24→28 and lessons 11→12, counted with `ls corpus/knowledge/*.md` and `ls corpus/lessons/*.md` then `wc -l`) | §3 |
| adjacency (unscored) | — | **unchanged** (agree) | report |

## Trend verdicts
- **expansion — improved (qualified).** Evidence: 3 admitted knowledge entries, each citing mined rows (`EXPANSION_ADMITTED=3/3`). Base coverage map (`git show ab19cff53:corpus/README.md`) has no row for source admission or claim-support states as methods; "claim-support" appears only as a Known-gaps bullet (`:151`). Citation-chain fidelity is partly covered by `chain-resolution-r3.md` and `anchor-boundaries-r4.md` coverage rows (README `:10`). So 2 of 3 are clearly uncovered ground; the third is a new method on a partly covered boundary. The report's "3 admitted entries on uncovered ground" overstates by one.
- **quality — improved (thin).** Evidence: one stale open finding closed by appended addendum (`corpus/knowledge/verification-r16.md:78-88`, row 24); four new entries carry headers, verified quotes, runnable rechecks (except D-5). No pre-round knowledge entry was re-verified or superseded (LEARNING's trigger for `improved` is supersession or re-verification); the gate fix is operability, not knowledge quality. Admission bar growth (5→12) is a process change and is not itself evidence of quality.
- **discernment — improved (qualified).** Evidence: my 7-decision spot check agrees 7/7 (one reason imprecise). The 3→13 mistake-capture count is self-assigned (the lane writes the criterion numbers the lesson cites), so it measures bookkeeping, not discernment.

## Defects (by severity)

**Medium**
- **D-1 (operability label).** SCORECARD and report say `operability: improved` while the scored construct (3 archived inputs, `VERDICT_BEARING_EXPORTS`) is unchanged at 3. The claim moved a different counter (delimiter defect). Recommend restating as "claim verified; defect closed; axis score unchanged" so the trend isn't read as a score move. Evidence: `SCORECARD.md` round-24 verdict table row 1; §3 above.
- **D-2 (claim-2 before is an absence).** `EXPANSION_ADMITTED 0/3` and `registry absent` at base make the before-state trivially zero, and the after-state is satisfied by criteria the lane wrote for itself in the same commit. The census (contract v1) is independent and clean, so the capability holds; the coverage "improved" leans on the lane's own counter.
- **D-3 (claim-3 circular count).** `CAPTURED_BY_CRITERION` counts whether each mistake row's `captured-by` names an existing criterion number; the lane writes both sides. It proves bookkeeping, not that the criteria would have caught the mistake. The report's own `none` for M-8 is the only real negative.

**Low**
- **D-4 (S006 Gate quote not verbatim).** `corpus/lessons/round-24.md:43`/row S006: the quote drops the enumerators `(2)` and `(3)` from the arXiv text (§3.3). Fix: quote the sentence verbatim or elide with `…`.
- **D-5 (citation-chain recheck is location-dependent).** `corpus/knowledge/citation-chain-fidelity-r24.md:5` `--root ..` returns `RESOLVED_HOPS=0/22` DRIFT from the tower worktree; `--root /home/vgpnk/Projects/shokunin` returns `17/22` CLEAN. Fix: write the fleet root (or `CHOUSA_ROOT`) into the recheck text.
- **D-6 (rejected-sweep stop rule cites the quota).** `SOURCES.md` `## Search log` item 2: "Stopped at three because the round assignment asked for at least two rejections (the contract sets no row quota)". The contract (rule 5) requires a stop rationale; a quota is not one. The three rejections are also the easy calls (vendor page, tertiary wiki, scoped 2011 ladder).
- **D-7 (SHONEN.md unchanged).** Report lists four `[~]`; `SHONEN.md` in the tree still has four `- [ ]`. Protocol expects the lane's own assessment `[~]` in the checklist file.
- **D-8 (LEARNING spot-check slot absent).** `corpus/lessons/round-24.md` `## Gate` has no admit/reject candidate list for knowledge entries and no spot-check result. LEARNING requires both. This review's §6 is the non-author spot-check to record there by the orchestrator.
- **D-9 (contract rule 1 and rule 2 deviation, disclosed).** Lesson `## Gate`: "Before commit the L1 narrowed, without re-opening, three cells": S006/S007 `scope`/`teaches`, S001 `anchor`. Contract rule 1 says write a row only after opening its source; rule 2 says log old→new. The narrowed values are accurate (I re-opened S006/S007), but the old values are not recorded for the scope/teaches/anchor changes.
- **D-10 (stale lesson header).** `corpus/lessons/round-24.md:5-6` says "worktree HEAD `ab19cff`" and "`corpus/QUALITY.md` and `tools/research-gate.sh` carry uncommitted r24 edits". At the landing commit neither is true. QUALITY 10 requires dated snapshots that name a commit window.
- **D-11 (`closed r24` vs named debt).** `corpus/knowledge/verification-r16.md:82` marks finding 24 "closed r24". The json entry's own named limits keep the concurrency race (one blank line under 16 parallel appenders; `…-demo.log` concurrency section) open, with `flock` as the candidate fix. Recommend "closed for single-writer; concurrent-writer debt open".

**Info**
- Scratch-parent collision (see Incident): sibling reviewers share `/tmp/kaika-verify/`. Route to the integrator.
- `corpus/evidence/README.md` EOF newline added (content identical).
- `SKILL.md` gate rows 133 → 136 edited in place (disclosed; outside the three append-only surfaces).

## L0 / integrator notes
- Record the spot-check (§6) in `corpus/lessons/round-24.md` `## Gate` (D-8).
- Consider whether `coverage: improved` should carry the qualifier in §Trend (D-2/expansion overstatement).
- Round 25 queue (`SCORECARD.md` `## Planned — round 25`) can absorb D-4, D-5, D-7 and D-10 as appended corrections; D-1 to D-3 need only the restated labels.

## Admit / reject recommendation
**ADMIT** (conditions are recorded corrections, none blocking):
- All three claims reproduce from their counting commands on both trees; the census validates (exit 0) and the validator fires on a broken copy; no axis score moved down; the gate's selftest, mutants, drift and full-r6 receipts reproduce; credential sweep clean; provenance clean; append-only holds on the named surfaces.
- Before the lane's next round, the orchestrator should restate claim 1 as "defect closed; score unchanged" (D-1), fix or footnote the S006 quote and the citation-chain recheck command (D-4, D-5), and record this spot-check (D-8). Lane self-verdicts to be restated as: operability — claim verified, score unchanged; coverage — improved (qualified); calibration — improved (mechanical, qualified); expansion — improved (qualified); quality — improved (thin); discernment — improved (qualified).
