# kaika W3 — non-author review: kasegi round 22

Reviewer: W3ReviewKasegi (non-author; fresh task dispatched by the orchestrator). Date 2026-10-19.
Subject: lane commit `c8b719d22882863ea7cd89b14c8bc078228001ed` (branch `kaika/round`, base `94aace2`); fleet report `.ufo/reports/round-22/kasegi.md` (ledger worktree, uncommitted).
Scope: read-only. Trees measured from `git archive` copies (`base` = 94aace2, `head` = c8b719d) under `/tmp/kaika-verify/kasegi/`, deleted at the end. Lane worktree not modified (`git status --short` empty).

## Recommendation

- **Admit C2** (expansion: 5 admitted entries; `sources-registry` capability enters). Every counting command reproduces; census validate exits 0; the re-opened quotes match.
- **Do not admit C1 as a `depth:verifiability` improvement.** Its counts reproduce exactly, but the axis is defined by `resolve.py` and `anchorcheck.py` (SCORECARD.md:33-38), and both are unchanged for the legacy entries. The move is provenance disclosure, which is closer to freshness. Orchestrator ruling needed (H1).
- **Trend corrections:** expansion `improved` (verified). Quality should be `unchanged`, not `improved` (H2). Discernment `improved` (my spot-check agrees on all sampled decisions).
- **Round verdict:** partial. One of two claims verifies on its declared axis. Record the Medium and Low items as appended corrections in round 23. No fabrication, credential, or append-only breach found.

## Verdicts by check

| # | Check | Verdict | Evidence |
|---|---|---|---|
| 1 | Provenance | PASS | one round commit; author and committer both `kasegi-shokunin <kasegi@shokunin.local>` |
| 2 | Append-only | PASS with one defect (M1) | LOG.md, lessons, QUALITY.md: 0 deleted lines; knowledge: 32 removed lines, all prefix-preserved; SKILL.md: 0; SCORECARD.md: 1 non-prefix line |
| 3 | Claims re-run | C1 counts verified; C2 counts verified; axis verdicts per H1 | see § Claims |
| 4 | SOURCES | PASS | validate exit 0; 14 rows re-opened, 2 of them rejected |
| 5 | Discernment | PASS, agree 5/5 | see § Spot-check |
| 6 | New entries | Headers PASS; recheck NOT runnable (M2) | see § New entries |
| 7 | Credentials | PASS | grep prints nothing |
| 8 | Report | PASS with pointer and count defects (M3, M4) | all required sections present in order; no `[x]`; cites `c8b719d` |

## 1. Provenance

Command: `git -C <lane> log --format='%h %an <%ae> | %cn <%ce> | %s' 94aace2..c8b719d`

Output:
`c8b719d kasegi-shokunin <kasegi@shokunin.local> | kasegi-shokunin <kasegi@shokunin.local> | round-22: QUALITY bar, SOURCES registry, frontier F01-F05 admitted, legacy provenance disclosure`

One commit in the range. Passes.

## 2. Append-only

Command: `git -C <lane> diff --numstat 94aace2 c8b719d` (totals: 38 files, +822 −34).

| file | +/− | note |
|---|---|---|
| LOG.md | 61 / 0 | append only |
| corpus/lessons/round-22.md | 155 / 0 | new file |
| corpus/QUALITY.md | 40 / 0 | new file |
| corpus/SOURCES.md | 54 / 0 | new file; base has no SOURCES.md |
| corpus/knowledge/* (25 legacy) | 32 removed in 6 files | every removed line is a prefix of its replacement, in order |
| SKILL.md | 11 / 0 | append only |
| corpus/README.md | 26 / 1 | removed line 5 extended by suffix; prefix-preserved |
| PROVINCE.md | 24 / 0 | append only |
| SCORECARD.md | 61 / 1 | **removed `| — none yet — | | | |` (line 295 at base) and replaced with the sources-registry row — not a prefix (M1)** |

Knowledge check: a Python script paired each removed line in every `-U0` hunk with an in-order added line that starts with it. Result: `knowledge hunks: 52 removed lines: 32 unmatched: 0`.

Anchor safety (SCORECARD counting block, run on base and head): `25 0` for each of the 25 legacy files, meaning zero base lines fail to be a prefix of the same-numbered head line.

## 3. Claims

Every row below was measured on `base` and `head` by `/tmp/kaika-verify/kasegi/measure2.sh`. It runs the SCORECARD round-22 counting block, restricting C1 to the 25 base file names. For `head`, the `anchor` check reads `base` as the reference.

| measure | base 94aace2 | head c8b719d | report says | reproduces? |
|---|---|---|---|---|
| C1 `source:` legacy | 0/25 | 25/25 | 0→25/25 | yes |
| C1 `verified-at:` legacy | 0/25 | 25/25 | 0→25/25 | yes |
| C1 `recheck:` legacy | 0/25 | 25/25 | 0→25/25 | yes |
| C1 recheck exit codes | 25× no recheck | 23× exit 1, 2× exit 0 | 23×1, 2×0 | yes |
| C1 base lines not prefix-preserved | 25×0 | 25×0 | 25/25, 0 non-prefix | yes |
| C1 `r22 correction` markers | 0 | 31 | 0→31 | yes |
| C1 presence-wording sweep | 8 | 5 | 8→5 | yes |
| C2 frontier admitted `F0[1-5]` | 0 | 5 | 0→5 | yes |
| C2 coverage-map rows | 25 | 33 | 25→33 | yes |
| C2 PROVINCE Core/Frontier/Adjacent | 0 | 3 | 0→3 | yes |
| C2 SOURCES rows | absent | 27 | 0→27 | yes |
| no-harm density `SKILL.md` mean | 154.0 (18 blocks) | 154.0 (19 blocks) | 154.0→154.0 | yes |
| no-harm anchorcheck `SKILL.md` | 7 in range, 0 bad, LOST-RECORDED=306 | identical | identical | yes (`diff` empty) |
| resolver (run in scratch copy) skill / corpus / all, GONE | 32/506, 140/1212, 156/1539, GONE 1383 | 39/513, 187/1259, 203/1586, GONE 1383 | as reported | yes |

The resolver's INTERNAL class rises from 146 to 193. The SCORECARD formula counts INTERNAL as resolved, so the all-citations fraction would move from 10.1% to 12.8% (156/1539 → 203/1586). The lane does not credit this, and I agree: the new citations are self-references. I note it for transparency.

Axis verdicts (recommended):

- **depth:verifiability (4), C1:** the counts are verified as measured, but the SCORECARD axis measure (`resolve.py` + `anchorcheck.py`, SCORECARD.md:33-38) did not move. Recommended axis verdict: `unchanged` (score held). Verdict for the claim as declared on depth:verifiability: `not-verified` (H1). If the orchestrator re-scopes C1 to freshness, it verifies there.
- **coverage (7), C2:** the counts are verified. The coverage axis is domain-root surfaces (SCORECARD.md:43-47, still 0/18 present), which the five frontier entries do not change. Recommended axis verdict: `unchanged` (score held). The claim verifies as a frontier and capability move.
- **depth:density (9):** `unchanged`, no harm.
- **Capability `sources-registry`:** enters. All seven contract census commands run clean (§4).

## 4. SOURCES

Command: `bash /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/fleet-census/scripts/sources-census.sh validate /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/kasegi-shokunin`

Output: `kasegi-shokunin	ok	/home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/kasegi-shokunin/corpus/SOURCES.md` — EXIT=0.

Contract census (run on head copy): rows 27; malformed 0; tier A=25 C=2; status mined=15 queued=10 rejected=2; duplicate ids none; enum/tier-inflation none; missing used-by none. Matches the lesson's census block.

Re-opened rows (14; ≥3 required; includes tier-A and both rejected rows):

| row | source re-opened | checked | result |
|---|---|---|---|
| S001 (A, mined) | first.org CVSS v4 user guide | Gate quote "CVSS Base (CVSS-B) scores are designed to measure…" in §"CVSS Base Score (CVSS-B) Measures Severity, not Risk" | verbatim |
| S002 (A, mined) | first.org CVSS v4 specification | entry quote "These factors are outside the scope of CVSS." (Introduction); "Assessment of the Threat and Environmental metrics is not required…" | verbatim |
| S004 (A, mined) | CERT/CC VDP | Gate quote "We think that 45 days can be a pretty tough deadline…" (FAQ) | verbatim |
| S005 (A, mined) | Project Zero FAQ | Gate quote "Our expectation is that the developer will fix the security vulnerability…within 90 days." | verbatim |
| S006 (A, mined) | HackerOne safe harbor FAQ | Gate quote "Adopting a Safe Harbor does not change the program scopes." | verbatim, **but the Gate names the wrong section** (M5): the sentence sits in "How to Enable Safe Harbors (Program Owners & Admins)", not "What is safe harbor?" |
| S007 (A, mined) | Bugcrowd disclose.io page | Gate quote "An exhaustive list of In-Scope properties…"; entry quote "does not represent the same level of commitment as full safe harbor" | verbatim |
| S010 (A, mined) | Project Zero Naptime | entry quote "vulnerability discovery tasks can be structured so that potential solutions can be verified automatically with absolute certainty." (Perfect Verification) | verbatim |
| S011 (A, mined) | Cloudflare Glasswing post | Gate quote "a suspected flaw without a working proof is speculation, and Mythos Preview closes that gap on its own." | verbatim; Validate stage quote also verbatim |
| S014 (A, mined) | MITRE 2025 key insights | Gate quote "Base and Variant level CWEs should be used whenever possible…"; "The shift in scoring and the fewer CWE mappings…" | verbatim; 39,080 figure matches |
| S016 (A, queued) | Anthropic CVD policy | Gate quote "Reports originating from AI-powered discovery are clearly labeled as such." | verbatim |
| S018 (A, queued) | FIRST multi-party v1.1 | Gate quote "All parties should clearly and securely communicate and negotiate expectations and timelines." | verbatim; "Version 1.1, Released Spring, 2020" |
| S024 (A, queued) | EUR-Lex 2024/2847 HTML | Gate quote is recital (2): "placed on the market with fewer vulnerabilities and that manufacturers take security seriously throughout a product's lifecycle" | verbatim; Article 14 not reached (see L1) |
| S026 (C, rejected) | CISA Gold Eagle page **and its linked 2-page PDF** | Gate quote "Gold Eagle lets organizations report, validate, and track AI-related vulnerabilities at scale." | verbatim; PDF describes ingestion/validation/dedup but gives no validation protocol or results. **Rejection holds** |
| S027 (C, rejected) | HN item 38389728 | title and date 2023-11-23, score 2; link to a Medium post | item matches; Medium returned HTTP 403 on re-open, so the flip is not met. **Rejection holds** |

## 5. Spot-check (LEARNING.md "Discernment is checked from outside")

| decision | artefact | agree / disagree | reason |
|---|---|---|---|
| admit | `corpus/knowledge/authorization-safe-harbor-and-scope.md` | agree | Evidence quotes S006/S007/S008 point to the same scope-vs-badge distinction. The S006 quote and S007 quote are verbatim. The Gate table mislabels S006's location (M5); the entry itself cites the right section. |
| admit | `corpus/knowledge/cvss-v4-severity-and-vector.md` | agree | S001 ×3 and S002 ×4 quotes verbatim; the rule (publish vector and CVSS-B/BE/BT/BTE label) is falsifiable against a report; Rejected section correctly grounded in S001 "should not be used alone to assess risk." |
| admit | `corpus/knowledge/coordinated-disclosure-timelines.md` | agree | S004 and S005 quotes verbatim (checked); the rejected universal-90-day claim is contradicted by S004's "Extenuating circumstances…may result in earlier or later disclosure." |
| reject | S026 Gold Eagle (CISA) | agree | the linked PDF, read in full (2 pages), has no validation protocol or measured results; flip not met. The lane should name the PDF in its sweep (M6). |
| reject | S027 HN link | agree | link-only item; destination returns 403; flip not met. |

Result: 5 of 5 sampled decisions agree (3 admits, 2 rejects). The one defect (M5) is a Gate location error, not a gate decision.

## 6. New knowledge entries (`cvss…`, `coordinated-disclosure…`, `authorization…`, `ai-assisted…`, `cwe-top25…`)

- **Headers (lines 2–4):** `source:` (S### + URL + anchor), `verified-at: 2026-10-19`, `recheck:` present in all 5. PASS.
- **Recheck runs:** NO. Each `recheck:` is a prose reread instruction with URL anchors, not a command. Run through the lane's own harness (`bash -c "$r"`), all 5 exit 2 (`cvss… exit 2`, `coordinated-disclosure… exit 2`, `authorization… exit 2`, `ai-assisted… exit 2`, `cwe-top25… exit 2`). Q1 allows "the runnable command or URL anchor", and LEARNING.md:62 allows "the command or citation", so the URL-anchor branch is conformant. The check-6 requirement that the recheck runs is not met (M2).
- **Q3 quote length:** 102 curly-quoted strings across the 5 entries; max 25 words; none over 25 (`python3` word count).
- **Q6:** no `op://`, no credentials, documentation-only statements present in each entry's Limits.
- **Claim vs source:** verified for the S-ids listed in §4. S003, S008, S009, S012, S013, S015, S021, S022, S023, S025 were not re-opened by me; the critic and reviewer re-opened S003, S009, S012 and S013 per the lesson.

## 7. Credentials

Command: `git -C <lane> diff 94aace2 c8b719d | grep -nE 'op://[A-Za-z0-9]|BEGIN [A-Z ]*PRIVATE KEY|ghp_[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}|xox[baprs]-[A-Za-z0-9]'` — no output, exit 1. A broader grep (`password|secret|token|api[_-]?key|session=`) matched only descriptive prose (e.g., the sibling-lane pointer "kagi — secrets and vault handling").

## 8. Report

Required sections, in order: Work performed; Landed changes; Before → after measurements; SHONEN; Sources & frontier; Mistakes; Trend verdicts; L0 questions; Integrator notes. All present. SHONEN has `[~]` and `[ ]` only (no `[x]`). Cites `c8b719d22882863ea7cd89b14c8bc078228001ed`. Pointers in the report itself check out at head (`SKILL.md:1014`, `LOG.md:1046`, `SCORECARD.md:176/191-192/301/309/316`, `corpus/README.md:191`, `PROVINCE.md:27/35/40`, `QUALITY.md:10-40`). Pointers inside the lesson are defective (M4).

## Per-axis recommended verdicts

| axis | before | after | recommended verdict |
|---|---|---|---|
| depth:verifiability | 4 | 4 | unchanged; C1 `not-verified` on this axis (H1) |
| coverage | 7 | 7 | unchanged; C2 verified as a frontier/capability move |
| depth:density | 9 | 9 | unchanged, no harm |
| capability sources-registry | — | enters | verified |

## Trend verdicts

- **Expansion — improved (verified).** Five admitted entries each cite a `mined` row. Base knowledge has no CVSS hits and no CVD-timeline or CWE-Top-25-methodology hits (`grep -il`). Safe harbor and AI validation overlap with program-specific notes at base (`mission-ledger.md`, `program-quirks.md`), so those two entries are on partly covered ground. Coverage map 25→33.
- **Quality — recommend `unchanged`, not `improved` (H2).** LEARNING.md:31 defines `improved` as a weaker entry superseded, or stale entries re-verified, with *no admitted entry failing its re-check*. No legacy entry was re-verified, and 23 of 25 legacy rechecks exit 1 today. `harmed` is not met, because the stale lines are now marked. The disclosure is real and useful, but it does not meet the trend's own definition.
- **Discernment — improved (verified on sample).** 5/5 sampled decisions agree (§5). Every Q/R criterion cites a lesson row (10 unlearned classes mapped; the count command prints 10). Residual: M5 and M15 are uncaptured (the lesson says so).

## Defects by severity

**High (verdict-affecting)**

- **H1 — C1 does not move its declared axis.** The C1 counting command measures provenance headers and recheck runnability. The axis is defined by `resolve.py` + `anchorcheck.py` (SCORECARD.md:33-38); both unchanged (anchorcheck diff empty; resolves=10 in both). Axis score held at 4. The lane's own AXES row places "stale items flagged or fixed" under freshness. Fix: re-scope C1 to freshness, or record it as not-verified on depth:verifiability.
- **H2 — quality trend `improved` does not meet LEARNING.md:31.** See trend verdicts. Fix: record `unchanged`.

**Medium**

- **M1 — "34 deletions, all same-line suffix appends, 0 non-prefix" is false for one line.** The fleet report (§Landed changes, first sentence) and SCORECARD round-22 block claim this for all 34 removed lines. SCORECARD.md line 295 at base (`| — none yet — | | | |`) was replaced by the sources-registry row. The counting block only checks `corpus/knowledge/`. Fix: correct the sentence; a placeholder replacement is fine but must be named.
- **M2 — new entries' rechecks are not runnable.** Five prose rechecks, exit 2 when executed (§6). Conformant under the Q1 URL-anchor branch, but check 6 expects a running recheck. Fix: either accept in the record, or add a runnable recheck in round 23 (an appended correction).
- **M3 — lesson B2 counts are stale and contradict R2.** `corpus/lessons/round-22.md:151-153` says "numstat shows 22 deletions in six legacy files … (16 hunks, 0 non-prefix)". `git diff --numstat` on the committed tree shows 32 removed lines in those six files (intake-and-finalize 6, operator-queue 3, ops-invariants 6, submitted-registry 14, triage-thresholds 2, citation-bases 1). R2 requires deletion counts to cite the command, and this one does not match it. The prefix claim itself holds (§2).
- **M4 — lesson pointers use base line numbers, unlabeled, but the lesson says they were re-opened in this worktree.** `corpus/lessons/round-22.md` M3 cites `corpus/README.md:168`, which is line 176 at head (the sentence "REJECTED with evidence" is there). M14 cites `corpus/README.md:145`, which is 153 at head. M12 cites `SCORECARD.md:251`, which is 257 at head. The same round inserted lines above those points. Fix: re-point, or label the numbering.
- **M5 — S006 Gate location wrong.** Gate row S006 says "What is safe harbor?". The quoted sentence is under "How to Enable Safe Harbors (Program Owners & Admins)". Q3 requires the exact location. Entry is correct; registry record is not.
- **M6 — S026 rejection's absence claim does not name the linked PDF.** Both the HTML and the 2-page PDF show no protocol, so the rejection holds. Under the lesson's own M3 logic the sweep should name the PDF.

**Low**

- **L1 — S024 `teaches` overreaches its gate.** Row says "manufacturer obligations"; the opened anchor is recital (2) only. Row's own anchor says Article 14 was not reached. Harmless while `queued`.
- **L2 — search-log PRISMA counts do not reconcile.** "General bug-bounty advice": identified 9, screened 1, included 0, excluded 1. Eight identified items are unaccounted for.
- **L3 — M16 lesson count.** States "3 with a Gate section" at base. Under the contract's own rule (`^## Gate$`, lesson Gate note) base has 2. The loose pattern gives 3.
- **L4 — SCORECARD round-22 rows omit "measured commit".** Round prompt §2.5 requires it. The fleet report carries the hash, so this is a ledger-only gap.
- **L5 — lesson line 4 is stale.** It says QUALITY.md was "uncommitted in the worktree when this lesson was written". It is now committed (`git diff --numstat`: QUALITY.md 40/0).

**Residual risk (not a defect this round)**

- **Calibration.** "Improved, score held" repeats for depth:verifiability (4) and coverage (7) across rounds 15–22 (SCORECARD.md:85-86, 103-104, 134-135, 202-204, 253-255, 327-328). Claims verify on counts that never move a scored measure. The scores are then an opinion, which AXES.md:52-55 warns against.
- **Self-citation credit.** The resolver's INTERNAL class rose 146→193, so the all-citations fraction moves 10.1%→12.8% if INTERNAL counts. The lane does not credit it. Good, but it means the no-harm test is sensitive to the definition.

## Verification gaps

- Not re-opened by me: S003, S008, S009, S012, S013, S015, S017, S019–S023, S025 (critic and reviewer per the lesson cover S003, S009, S012, S013). L1's 85/85 string sweep is not reproduced beyond the sample above.
- Not verifiable from the repo: godspeed prompt bytes, the 12+3 batched L2 dispatch, the 100-job-cap refusals, "No model was passed".
- Fleet report is uncommitted in the ledger worktree; read as given.
- Lane worktree was not modified. Scratch copies and outputs are deleted at the end of the review.
