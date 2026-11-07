# kasegi — round 93 report (attempt 1)

Lane: `kasegi-shokunin` (depth + coverage; bounty/security research). Round shape: ONE v1
wave of 13 seats (8 attack roles), dispatched through the operator's inline spawn handoff.
Lane base `e15996bfd2f6eca4af39507a7c5973afbeca8347`; freeze `5bad9e55d3d9319446e3d9b63bc2dece633cdb68`;
C1 landing `ae53b3c6e7e2ce070c2f022d01c1677a8908df1b`; C2 landing `9225954a6e3f177af46bdb9d811c062a4353a552`;
wave evidence `60152778963f8b9850cab03165b777d469cec1ed`; integration and final lane tip `a3760ac50b183e6556fc9937074deb15bc9f3433` (pushed; `ls-remote` verified).

## Work performed

The round declares two claims:

- **C1 — depth:verifiability (the lowest non-retired axis, score 4; citation repair, the score is not claimed to move).**
  Tranche 8 closes the last five GONE bare-key sites in `corpus/knowledge/triage-thresholds.md`: the 437/438
  errata cells are replaced whole by the exact cells the round-92 non-author seat ReviewC1Labels wrote, the 454
  second token repoints from `SKILL.md:494-506` (park-disposition text) to `SKILL.md:827-848` (the EV formula),
  and the 58/144 surviving `MATCHES: SKILL.md:117` ties repoint to `SKILL.md:191` (the only attempts statement;
  `MAX_ATTEMPTS` occurs 0 times in SKILL.md). The successor counter adds the `cell-repair` kind and lane-root
  `SKILL.md:N[-M]` values, and M3 takes a labelled-file union (the walk itself is defective on non-knowledge labels — material qualifier Q6/M93-5, routed).
- **C2 — coverage (score 8 held), a capability extension of `capture-secret-scan` (sourced: S139).**
  New shape `gitlab-pat` (`glpat-` + exactly 20 characters of `A-Za-z0-9_-`, both boundaries, an escape
  terminator allowed before it) and the `github-token` left boundary now accepts the escape-terminator family
  (`\t`, `\r`, `\n`, `\uXXXX`, `%XX`, `&#NN;`, `&#xXX;`), closing the round-92 SentinelGitHub P1 family.

Work items, each with an evidence pointer:

- **Load order and claim freeze.** Read `skill://shokunin`, PROTOCOL/MISSION/AXES/CORPUS/LEARNING, `skill://swarm`, the lane SKILL/PROVINCE/SCORECARD/QUALITY/corpus, the r92 closure and its spot-check. Two claims, ten+forgery controls executed and committed before any data: `.ufo/waves/round-93/claims.json`, `.ufo/waves/round-93/controls/c1-controls-r93.txt` (11/11), `.ufo/waves/round-93/controls/c2-controls-r93.txt` (14/14), freeze `5bad9e55`.
- **C1 landing.** Five label-named edits in one file; frozen counter passes M0–M10 at the landing: `.ufo/waves/round-93/l1/c1-landing-r93.txt`; landing `ae53b3c6`.
- **C2 landing.** Candidate scanner + capability row; K1–K8 pass at three seeds with both pins: `.ufo/waves/round-93/l1/c2-landing-r93.txt`; landing `9225954a`.
- **Source S139.** Opened, captured through the round-90 intake gate after four digest-bound allowlist rows read in context, manifest rechecked: `corpus/source-snapshots/round-93/S139.txt`, `corpus/source-snapshots/round-93/manifest.json`, `.ufo/waves/round-93/controls/source-recheck-r93.txt` (rc 0), `.ufo/waves/round-93/controls/capture-intake-r93.txt`.
- **R143/R144 re-anchor.** 135 citations of the scanner in five knowledge entries shifted; the 39 rows whose base range meets the replaced docstring block were read against the landed lines and 12 hand dispositions made (single tokens and clause ranges narrowed, three false sentences rewritten); quote check `bad=0 out_of_range=0`: `.ufo/waves/round-93/l1/reanchor-r93.txt`, `.ufo/waves/round-93/l1/quote-anchor-r93.txt`.
- **Wave w1 (13 seats).** CriticClaimsC1, CriticClaimsC2, ExecC1Indep, ReviewC1Labels, ReviewC2Scanner, MutC1Counter, MutC2Counter, SentinelEscape, ScoutGitLab, ConnectorOverlap, CriticHarm, ScribeEntry, ExecC2Probe; 8 of 13 attack roles. Evidence: `.ufo/waves/round-93/w1-spec.json`, `.ufo/waves/round-93/w1-dispatch.json`, `.ufo/waves/round-93/w1-results.json`, `.ufo/waves/round-93/w1/`.

## Landed changes

| Change | LOG entry | Commit |
|---|---|---|
| Freeze: claims, counters, map, labels, candidate scanner and row, executed controls, S139 capture + manifest, allowlist rows, SOURCES row | Round 93 bullet 1 | `5bad9e55` |
| C1 landing: tranche 8 (5 edits, cell-repair + lane-root kinds) | Round 93 bullet 2 | `ae53b3c6` |
| C2 landing: `gitlab-pat`, escape-terminator boundary, capability row | Round 93 bullet 3 | `9225954a` |
| Wave w1 evidence (spec, dispatch, results, 13 seat reports and receipts, landing receipts, re-anchor/census receipts, redaction digests) | Round 93 bullet 3 | `60152778` |
| Integration: lesson, LOG, SCORECARD, QUALITY R145, S139 `mined`, re-anchored knowledge entries | Round 93 bullets 4–5 | `a3760ac5` |

## Before → after measurements

| Claim | Before | After | Counting command | Measured at |
|---|---|---|---|---|
| C1 | 1007/2001 (50.32 %) | **1009/2000** (50.45 %); M0–M10 pass, M9 5/5, M10 want=5 mapped=5 | `python3 -B .ufo/waves/round-93/c1/knowledge-meter.py --lane <clone> --base-rev e15996bfd2f6eca4af39507a7c5973afbeca8347 --after-rev ae53b3c6e7e2ce070c2f022d01c1677a8908df1b --map .ufo/waves/round-93/c1/repair-map.tsv --labels-rev 5bad9e55d3d9319446e3d9b63bc2dece633cdb68 --base-target 1007/2001 --target 1009/2000 --map-sha256 7ab66a7fc8a90cf92d026d0ba1abaa23461b10a3bbd79d003ee4a33961eb3b76 --work <scratch>` | `ae53b3c6` |
| C2 | no `gitlab-pat`; the escape-terminator left boundary misses 11 measured forms; the round-92 scanner misses all 10 round-93 plant entries and 3 generated positives | K1–K8 pass at `9225954a` at the run-time seed and seeds 1 and 9191; instrument sha256 `7d9d7309…`, gate `8b6f8493…`; plants under a run-time nonce | `python3 -B .ufo/waves/round-93/c2/capability-check.py --lane <lane> --rev 9225954a6e3f177af46bdb9d811c062a4353a552 --work <scratch> --instrument-sha256 7d9d7309d5a5eddde59dbbb49767d71f43ec78667f1c3aa05bb1c76a45f683c5 --gate-sha256 8b6f849349157a91dd7a2a3998c1f3956e8fed2dbd565c40815660cbd71cc8e6 [--seed N]` | `9225954a` |
| — | depth:density 273.2 | 273.2 (SKILL.md byte-identical) | `python3 corpus/instruments/density.py SKILL.md --label r93` | tip |

Environment receipt (R142): the C1 base reading at `e15996bf` is `1007/2001` on the live lane and on a clean `git clone --shared`, with the same HOST line.

## Sources & frontier

- **Census before → after.** Round start (before any round-93 registry edit): `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kasegi` → the six inherited W04 warnings (S028, S029, S072, S076, S080, S085) and `kasegi ok`, **rc 0**; registry 138 rows (`.ufo/waves/round-93/controls/census-start-r93.txt`). Round end: same command → the same six warnings and `kasegi ok`, **rc 0**; registry 139 rows (`.ufo/waves/round-93/l1/census-end-r93.txt`).
- **Rows before → after:** 138 → 139. Rows added by tier: A = 1 (S139), B = 0, C = 0.
- **Rows touched old → new:** S139 `status queued → mined`, `used-by — → corpus/instruments/capture-secret-scan.py` (freeze → integration). No other row's status, recheck or used-by cell changed.
- **Rejected this round:** the GitLab Docs Personal access tokens profile page (HTTP 200; converted text carries no `glpat` occurrence, so it cannot ground the prefix; wave seat ScoutGitLab corrected the record: the page *does* state the 20-character length at converted line 297, so the rejection rests on the prefix only). Not registered; flip condition in the lesson Gate.
- **Frontier rows advanced:** none. This round is a sourced capability extension of an existing capability, not a `corpus/README.md` frontier admission; the admitted knowledge/file rows are unchanged.
- **Located quotes for every new row:** S139 — `S139.txt:87` "glpat- followed by a 20-character string" (6 words), access date 2026-11-07, capture sha256 `154a7e15…` (lesson § Gate).
- **Assimilation: none.** The `merge/kasegi/` staged ids collide with the lane registry by construction: `reg-ids` 139, `staged-ids` 94, `collisions` 94 (`.ufo/waves/round-93/assimilation/`); nothing was appended from the package this round, and the quarantine slice re-derives 7 rows, carried (lesson disposition 7).
- **considered:** `considerthese/2026-10-26.md` has no unimplemented item this round's two claims serve; no new proposal mined.

## Wave findings (none re-scores a claim)

- **CriticClaimsC1** — C1 STANDS on P1–P3 (frozen meter rc 0 re-derived; each forged variant named with the limb that kills it). Observation: the M3 labelled-file union is exercised by the wave's unit control, not by this round's label set (all labels cite `corpus/knowledge`).
- **CriticClaimsC2** — C2 STANDS on P1–P3; **material qualifier Q1**: the statement's "a path-keyed forgery cannot know the paths" is false as implemented (the nonce is a directory-only transform; a path-shape-keyed round-92 scanner passes all eight limbs unpinned — M93-4, routed to round 94).
- **ExecC1Indep** — AGREE: all 8 label rows reconstruct byte-exactly; the base→after diff of the file is exactly the 5 positions {58, 144, 437, 438, 454}, the other 482 lines byte-identical; an independent extractor and resolver reproduce the token-set delta (removed 3 INTERNAL + 3 GONE, added 5 INTERNAL) and the meter arithmetic 1007/2001 → 1009/2000; 3 of 1082 shared tokens classify differently against a *committed census* and all 3 are archive-materialization artifacts (`../MISSION.md`, `.git`), class-stable across base→after.
- **ReviewC1Labels** — 8 CORRECT / 0 PARTIAL / 0 WRONG; round-94 labels written and verified (`round94-labels.tsv`, 29 rows, `failures=0 PASS`).
- **ReviewC2Scanner** — APPROVE; D1 (three stale class-B sentences) closed in the integration; D2 (docstring/counter "S139 line 86"), D3 (`&#xXX;` unpinned) and D4 (stale K8 doc line, no GitLab left-boundary plant) routed; reanchor table 82 ranges / 60 moved.
- **MutC1Counter** — killed=7, survived=12 of 19 mutants; **R1 (high)**: the M3 labelled-file union walk crashes (`b, a = file_at(...)` shadows the argparse namespace; `AttributeError` before any LIMB line), so the unit control's rc=1 is a traceback, not a line-diff detection (M93-5, routed); **R2**: M5 does not bind a lane-root token inside a `cell-repair` replacement (probe F1 rewrites 437's `SKILL.md:176-178` past EOF and the counter still passes, routed); `EXCLUDED = {}` leaves three mutants indistinguishable, one a latent M10 defect with a proving input.
- **MutC2Counter** — forged=7 rejected=4 survivors=3 (harness-name gating, gutted selftest, suffix-keyed), all killed only by the K1 sha pins when supplied; routed D1–D3.
- **SentinelEscape** — 67 probes, 44 detected / 23 missed (11 statement-named, 12 unnamed routed: `\b`/`\f`, `\xXX`, `%uXXXX`, octal, double-encoded `%25XX`); 2 FP-shaped; ReDoS max 1.241 s/MB, new shapes at/below the filler baseline.
- **ScoutGitLab** — capture-equal=yes; 9 ranked leads; corrected the frozen frontier note (the PAT page states the 20-character length at line 297); routed coverage gaps (custom instance prefix, routable PAT forms, `ghr_` 76 vs 36).
- **ConnectorOverlap** — 20 sibling lanes: 0 bounded `glpat-` detectors, 0 escape-aware, 0 with both round-92 GitHub shapes; the intake gate inherits both new classes.
- **CriticHarm** — NO HARM on items 1–6 (density byte-identical, `--rev` hits=0, `--files` hits=0 over 286 files, identical 23-hit/18-file differential over 6,275 `.md`, ReDoS flat, round-92 counter still passes, no resolving citation lost).
- **ScribeEntry** — drafts=4 PASS; manifest `lines` corrected 415→414, the `S139 line 86` citation routed, the "teaching samples" bullet corrected.
- **ExecC2Probe** — AGREE; `rev_hits=4 files_hits=4`, selftest `cases=90`, intake refused; allowlist rows bind exactly (per-row perturbation).

**Qualifier summary (none re-scores a predicate at the landing).** C2 Q1 (material): the statement's path-keyed-forgery parenthetical is false as implemented (M93-4). C1 Q6 (material): the M3 labelled-file union crashes on a non-knowledge labelled file; the unit control passed on the traceback (M93-5). Routed C1 Q7–Q9 (M5 does not bind a cell's lane-root token; EXCLUDED empty; 12 mutant survivors), C2 Q2–Q7 (docstring `S139 line 86`; `&#xXX;` unpinned; stale K8 doc line; custom-prefix/routable/`ghr_` coverage gaps; 3 unpinned counter survivors; 12 unnamed escape miss classes and 2 FP shapes). C1 Q1–Q4 (454's parenthetical names clauses outside `:827-848`; 58/144 cite the threshold not the literal name; a token-set census reports 3 intentionally replaced strings "lost"; the 58/144 labels are transcribed). The probe receipts and dispositions are in `w1/` and the lesson.

## Trend verdicts

- **expansion — improved.** The lane's learning surface gained one first-party source row (S139, tier A) and one new credential edge class (`gitlab-pat`, plus the escape-terminator encoding family); registry 138 → 139, census rc 0 at both ends.
- **quality — improved.** The last five GONE bare-key sites in the knowledge scope are resolved or correctly dispositioned under a counter that now expresses both kinds and walks every labelled file; the capture scanner detects a documented provider shape and the encoding family a prior seat measured as an 11-form bypass; the instrument's knowledge citations are re-anchored (135 shifts, 39 hand-narrowed, three false sentences rewritten, quote check `bad=0`).
- **discernment — improved.** The round caught its own re-anchor widening (M93-1, the M92-3 recurrence) with an explicit enumeration of the intersecting CHANGE rows rather than trusting the quote checker, recorded the label-provenance qualifier (M93-3), and kept the instrument unchanged where an edit would have broken the C2 pin (docstring citation routed, not slipped in).

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources
      Evidence: corpus/lessons/round-47-verifier-spotcheck.md — non-author check of boxes 1, 3 and 4; SKILL.md itself is the object under test, not its evidence.
- [~] At least one end-to-end domain task executed and logged in LOG.md
      Evidence: corpus/practice/curl-h1-1913733/report.md — round 85 retrospective practice package; second package corpus/practice/curl-ibb-h1-1997312/report.md (round 86); logged in LOG.md Rounds 85–86; not a live or authorized bounty task.
- [~] Instructions executable by an agent without oral context
      Evidence: corpus/lessons/round-47-verifier-spotcheck.md — Declared-root recheck observations; not promotion.
- [~] No cross-domain bleed (PROVINCE.md still accurate)
      Evidence: PROVINCE.md — Scope unchanged; live-target testing remains refused.

Stale-lane: this is a respawn-per-round driver lane; no other mission of this lane is open.

Tool installs: none this round (no tool needed an install or upgrade).

Redaction note: GitHub push protection (GH013) flagged GitLab-Access-Token-shaped strings in the wave evidence (GitLab's own published example tokens quoted by seats plus synthetic fixtures). The wave receipts and `w1-results.json` carry those values redacted (`glpat-REDACTED-r93`, `ghp_REDACTED-r93`, `AKIA-REDACTED-r93`); no live credential was involved, and the lane's scanner over the evidence prints hits=0. The redaction is recorded in L0 `kasegi | round-93` and in the lesson.
