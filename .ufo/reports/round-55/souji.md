# souji round 55 — report

Round 55, attempt 1. Lane `souji` (`/home/vgpnk/Projects/shokunin/souji-shokunin`). Base `f056aaa031bb65de27e7fa5daa38b0d4a443aedc` (the r54 non-author verifier spot-check, verdict ok/admitted). Freeze `e8f338674dea386c186aa7657ef2142cbb4b6d48`. Measured revision for the real-lane legs `4b10ddd1741a948c89d283358affd1da2ab3fd95`. Lane tip at report time `6d8bfb8ebb00f4806e7f83a0173aa4768358de33` (= `origin/master`, verified by `git ls-remote` before this report).

## Work performed

Declared claims (2, one per distinct axis; no exploratory claim):

- **C1 — calibration 7** (the lowest non-retired axis): the annotation-agreement counter amended to v4 (`census/round-55/c1-counter.py`) to instrument the r54 routed surfaces, over 27 committed fixtures. Verdict basis: the frozen predicate holds; **a v3→v4 regression (S55-S2) is recorded as a harm**, so the no-harm rule is not met on that shape.
- **C2 — coverage 8**: the capture counter amended to v4 (`census/round-55/c2-counter.py`) to instrument NL-1/NL-3/NL-4/NL-5 and the M11 pin branch, over 13 fixtures plus 2 selftest arms. Verdict basis: the frozen predicate holds; **a v3→v4 regression (RD-A) is recorded as a harm**, so the no-harm rule is not met on that shape.

Work items (evidence pointers):

- Protocol load: `skill://shokunin`, kimi-shokunin SKILL/PROTOCOL/MISSION/AXES/CORPUS/LEARNING, lane SKILL/PROVINCE/SCORECARD, corpus QUALITY/README, lessons 54 and the 54 spot-check. Round-start census `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin souji` rc 0 (201 rows).
- Freeze commit `e8f33867` (prereg, counters, builder, expected TSVs, two do-nothing controls, pre-flight receipts). `tools/souji-freeze-check.py --rev e8f33867`: `SUMMARY claims=2 findings=0`, rc 0 (`census/round-55/records/freeze-check-at-freeze.txt`).
- Capture commit `9a1eaaa2` (fleet-root census at fleet HEAD `e5396bee`, 49 entries, staged outside the root and copied byte-exact). Receipt correction `4b10ddd1` (the first receipt had an empty ENTRIES cell; `RECEIPT-MALFORMED` caught it; the receipt now takes ENTRIES from the capture header).
- Official post-freeze matrices `census/round-55/records/c{1,2}-matrix-v{3,4}.tsv`, reproduced byte-identically by `census/round-55/fixtures/run-matrix.sh` against the dry-run matrices.
- Real-lane legs at `4b10ddd1`: `census/round-55/records/c1-tip.txt` exit 0 (`unfiled=0 … alias=0 pairinert=0`); `census/round-55/records/c2-tip.txt` exit 0 (`receipt=ok sorted=ok tool_pin=ok`). Wrong pin rc 1 `TOOL-SHA-ARG-MISMATCH`, run by the L1.
- S278 (Python 3.12 `str.splitlines`, tier A, opened live 2026-11-03: HTTP 200, sha256 `0b10fb9e…a352`; located quotes `census/round-55/sources/s278-located-quote.txt`). Knowledge entry `corpus/knowledge/splitlines-line-model.md`, registry row S278, search-log entry, README frontier note.
- QUALITY Q109 (a measured revision cites a committed receipt; red arm `8fb6fbc6` with zero receipts in r54, green arm `4b10ddd1` with two) and Q110 (a counted kill row names its finding; red arm r54 `FA8-SYMLINK-CLASS finding=-`, green arm zero unnamed rows). Both answer the r54 spot-check §5.1 and §5.2 (`corpus/QUALITY.md` `### Round 55 criteria`).
- Erratum and probes: ERRATUM-R55-1 (F7-FF bytes are vertical tab, not form feed; the form-feed shape measured in `census/round-55/records/probe-erratum-r55-1-formfeed.txt`: frozen v3 exit 0 with both corrections filed, v4 exit 1 `CORRECTION-IN-FENCE`). The repository-local `core.quotePath=false` numstat limit: `census/round-55/records/probe-numstat-quotepath.txt`.
- Wave `w1`: one v1 wave, 12 seats, all returned output, none dead. Evidence `census/round-55/wave/` (spec, dispatch, registry, `w1-results.json`, seat reports and receipts). Lesson `corpus/lessons/round-55.md` `## Wave findings` and the addendum.
- S2 regression probe (after the wave): `census/round-55/records/probe-s2-pair-indent-comment.txt` (frozen v3 exit 1 `UNFILED-SOURCES-ANNOTATION`, v4 exit 0 on the same overstatement behind a four-space `<!--` line).

Wave shape: one v1 wave, 12 seats (scout 1, executor 3, scribe 1, reviewer 2, critic 1, mutation-tester 1, sentinel 1, connector 1, revenger 1). Attack roles 4 of 12 = 33% (≥25%). Connectors 1 (≤2). Band 8–16. The L1 holds the canonical planner seat (the validator rejects it as a swarm role). Residual calls: none. Round total: 12 seats. Dead seats: none. Routing: run-15 map, no `model` argument. Dispatch `.ufo/waves/round-55/w1-dispatch.json` (validated `run` rc 0, 12 spawns).

Wave verdicts (seat by seat; full text in the lesson):

- executor01 / executor02 — AGREE on all reproduction steps (selftests 27/27 and 15/15; matrices and real-lane legs byte-equal).
- executor03 — landing suite (`census/round-46/c1-counter.py`) `assertions=580 mismatches=76 registered=76 unfiled=0` at `4b10ddd1` and at the wave tip; r53 counters 10/10.
- scout01 — frozen pins verified; 17 routed items mapped, 0 unmapped.
- scribe01 — S278 re-open PASS (byte-equal capture, four quotes). Found a Q62 K1 defect (the new entry's `source:` line cited S277 while S277's `used-by` did not name the entry); fixed by removing the S277 id from the `source:` line. Recheck set to `on-release`.
- critic01 — both claims SURVIVE the literal kill rules; N1–N15 named limits; the N1 pair-filing-in-fence false pass is the highest.
- mutation01 — C1: 14/14 mutants killed by their named fixture. C2: survivors C2-15b (print-only, equivalent for the detector), C2-17 and C2-18 (the selftest does not assert that every expected row ran).
- reviewer01 — 66 C1 attack states: 41 CommonMark-consistent or counter-internal, 17 routed-defect proposals, 7 named-limit confirmations, 1 render-inconclusive.
- reviewer02 — 54 C2 attack states: frozen kill rule holds; **RD-A regression** (v4 passes `1KEY=x`, `_KEY=x`, `2=x` that v3 refused); RD-B to RD-E routed.
- revenger01 — 27 r54 routed items: INSTRUMENTED 21, REPAIRED-BY-DISCLOSURE 2, OPEN 3 (S4 relative `--work`, S5 docstring `PRISTINE FAIL` phrase, N6 exit-code legend).
- connector01 — line-numbering mechanism overlaps with siblings: kaidoku `tools/round-59/annotation-audit.py` and chousa `tools/corpus/evidence/round50/stale-count-check.py` use `splitlines` on the S1 defect class (routed to their lanes; not edited here). Receipt grammar: no overlap. Declared count: class overlaps with kaidoku; grammar disjoint. One proposal P1 (hyphenated receipt keys), not applied.
- sentinel01 — **CONDITIONAL PASS**: S55-S1 HIGH (a NUL byte in a correction file makes numstat binary; carried from v3); **S55-S2 MEDIUM (v3→v4 regression, confirmed by the L1)**; S55-S3 named (corrections outside the lexing tolerance are unjudged); S55-S4 LOW (pycache without `-B`, gitignored); S55-S5 LOW (empty-value receipt keys ignored).

Harms (the admission bar: every claim verifies and no axis is harmed):

- **C1 — S55-S2 (regression).** A four-space-indented `<!--` line before an overstatement in LOG.md hides the overstatement from the pair scan under v4 (exit 0); the frozen v3 refuses it (exit 1, `UNFILED-SOURCES-ANNOTATION`). Cause: the R6 change made the pair scan skip lines hidden by `hidden_lines()`, and its comment branch opens at any indent. Receipt `census/round-55/records/probe-s2-pair-indent-comment.txt`.
- **C2 — RD-A (regression).** `1KEY=x`, `_KEY=x` and `2=x` are refused as unknown receipt keys by v3 and pass silently under v4 (the first-character class was narrowed to a letter without a differential). Receipt `census/round-55/wave/w1/S55reviewer02/receipt-key-differential.txt`.

Neither harm is in the frozen kill list, so both predicates hold literally. Neither is fixed in-round: the frozen bytes cannot change, and each fix is a new counter version with its own prereg. The lane does not admit either claim. The operator rules (L0 line filed below).

## Landed changes

| commit | change | LOG entry |
|---|---|---|
| `e8f33867` | freeze: prereg, both v4 counters, builder, expected TSVs, controls, pre-flight receipts | `## Round 55` |
| `9a1eaaa2` | fleet-root capture (fleet HEAD `e5396bee`, 49 entries) and official post-freeze matrices | `## Round 55` |
| `4b10ddd1` | capture receipt correction (ENTRIES from the capture header); measured revision | `## Round 55` |
| `3ce0ba03` | real-lane legs at `4b10ddd1`; S278 captured sources | `## Round 55` |
| `913fa479` | S278 registry row; `splitlines-line-model.md`; lesson; QUALITY Q109/Q110; SKILL round-55 contracts; probe receipts | `## Round 55` |
| `b6c6a93a` | S278 search-log entry; README round-55 frontier; SCORECARD round-55 measurements | `## Round 55` |
| `f9da665e` | wave evidence; S2 probe receipt; lesson wave findings and addendum; SCORECARD corrections | `## Round 55` |
| `51551399` | SKILL PTR wording (ERRATUM-R55-2); harms recorded | `## Round 55` |
| `6d8bfb8e` | SCORECARD round-55 rows cite committed paths only (landing-suite `unfiled=0` restored) | `## Round 55` |

## Before → after measurements

| claim | axis | before | after | counting command | measured commit |
|---|---|---|---|---|---|
| C1 v4 instruments the r54 routed filing surfaces | calibration 7 | v3 exit 0 on 8 of 8 acceptance attacks (F7-FF, F13, F14, F15, F16, F20, F21, F22); v3 exit 1 on 3 honest over-hide states (F17, F18, F19); 27-row exit-0 count 11 | v4 exit 1 on 8 of 8 acceptance attacks with named findings; v4 exit 0 on F17, F18, F19; 13 carry-over rows identical; 27-row exit-0 count 6; real lane exit 0 | `awk -F'\t' 'NR>1 && $5==0{n++} END{print n+0}' census/round-55/records/c1-matrix-v3.tsv census/round-55/records/c1-matrix-v4.tsv` (11 → 6); `python3 -B census/round-55/c1-counter.py --root LANE --rev 4b10ddd1741a948c89d283358affd1da2ab3fd95 --base f056aaa031bb65de27e7fa5daa38b0d4a443aedc --record-sha256 2b90a262c29772d4a9a7bd5ab29ce06b9d8f350832f0d0cd5114d52b0f6dad30 --sources-rev-before f778b9d131574d3ff09c0cc8a077643c0fc84bb4 --sources-rev-after 9bf9234ae4d11c7b31706354302a9e95ad0d1f81 --scratch DIR` | `4b10ddd1741a948c89d283358affd1da2ab3fd95` |
| C2 v4 instruments the NL and pin surfaces | coverage 8 | v3 exit 0 on FB1-TAB4-ROW, FB2-LOWER-KEY, FB3-NOSPACE-KEY; 13-row exit-0 count 5 | v4 exit 1 on FB1–FB3 with named findings; FA8 named CLASS-MISMATCH; FH/FH2/FA1–FA7 identical; 13-row exit-0 count 2; selftest 15/15; real lane exit 0 `receipt=ok sorted=ok tool_pin=ok`; wrong pin rc 1 | `awk -F'\t' 'NR>1 && $5==0{n++} END{print n+0}' census/round-55/records/c2-matrix-v3.tsv census/round-55/records/c2-matrix-v4.tsv` (5 → 2); `python3 -B census/round-55/c2-counter.py --root LANE --rev 4b10ddd1741a948c89d283358affd1da2ab3fd95 --capture census/round-55/records/fleet-root-census.tsv --receipt census/round-55/records/fleet-root-census-run.txt --tool-sha256 e7e79952f7830d75c5b0eee35c2369716053f40121c7d3be370f7abdda067a5b --scratch DIR` | `4b10ddd1741a948c89d283358affd1da2ab3fd95` |

Numeric axis scores unchanged (calibration 7, coverage 8, operability 8). The no-harm failures on both claims are the admission question for the operator; the lane claims no admission.

Standing checks at the final tip `6d8bfb8e`:

- Landing suite `python3 -B census/round-46/c1-counter.py --root LANE --rev 6d8bfb8e… --work DIR`: `SUMMARY assertions=597 mismatches=76 registered=76 corrected=0 exempted=0 unfiled=0`, rc 0 (`/fast/scratch/hyaku/souji-r55/L1/landing-tip.txt`, scratch).
- Census round-end `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin souji`: rc 0 (202 rows; W04 61, pre-existing).
- r52/r53/r54 counters were re-run by executor03 at the wave tip (identical verdicts; r52 c1/c2 exit 0; r53 10/10).

## Sources & frontier

- SOURCES: before 201 rows (freeze `f056aaa0`), after 202 rows (`6d8bfb8e`). Count command: `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`. Census `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin souji` rc 0 at start and at the tip.
- Rows added by tier: A +1 (S278, Python 3.12 `str.splitlines`, docs, status `mined`, recheck `on-release`, cited by `corpus/knowledge/splitlines-line-model.md`).
- Rows touched old→new: none. S277's `used-by` was deliberately left unchanged; the Q62 defect was closed by removing S277 from the new entry's `source:` line (option b, scribe01).
- Frontier rows advanced: none. No Core promotion. The new entry sits on Core ground (correction-filing line model).
- K1 replay after the change: `tools/souji-registry-agreement.py --root . --rev 6d8bfb8e… --list-rev b8cb4b31ce80e2e3314b88e85d40ea9873180804` → `SUMMARY k1=2 k2=0 mismatches=2` (both pre-existing: S146 cited-no-row, S110 cited-not-in-used-by; zero from this round).
- Search log: one entry (S278; identified 1, screened 1, included 1, excluded 0).
- Assimilation: none (shokuknow `merge/souji` held by the open r46 L0 on mass id drift; `considerthese/` absent in this lane).
- Mistake mined: `corpus/lessons/round-55.md` `## Mistakes` (ten rows, including the two regressions and the ERRATUM-R55-1 label error).
- Sourced claim: C1 cites S278 through `corpus/knowledge/splitlines-line-model.md`.

## Trend verdicts

- **expansion: unchanged.** One knowledge entry admitted on Core ground the lane already holds; no frontier row moved; no new source kind; registry +1 (S278).
- **quality: harmed (trade reported, not admitted).** The instrument gained real kill-power: 8 of 8 acceptance attacks and 3 honest over-hide repairs on C1; 3 of 3 C2 receipt-key attacks. Two v3→v4 regressions were introduced (S55-S2 on C1, RD-A on C2), so the trade is reported and not admitted; the operator rules.
- **discernment: unchanged.** The attack seats (dispatched by the lane, hence not non-author) found 17+ routed defects and both regressions; the gate did not catch the regressions before freezing. No non-author spot-check of this round has run yet, so there is no evidence of improved discernment, and no evidence that it worsened beyond these two learned cases.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — pointer: `SKILL.md` `## Round 55 contracts` (gate-registry rows with entry commands, verdict maps, pinned digests); decision tables and error patterns unchanged from r54.
- [~] At least one end-to-end domain task executed and logged in LOG.md — pointer: `LOG.md` `## Round 55`; the end-to-end capture, matrix, real-lane and wave legs above.
- [~] Instructions executable by an agent without oral context — pointer: `census/round-55/preregistration.txt` recompute commands; `census/round-55/fixtures/run-matrix.sh`; `SKILL.md` Round 55 contracts.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — pointer: `PROVINCE.md` unchanged; connector01 NO-OVERLAP on the three surfaces; sibling defects routed to kaidoku and chousa, not edited.

## Stale-lane, holds, L0, incidents

- Stale-lane: none. No other mission of this lane is open; the w1 wave settled (WAVE-DONE) before this report.
- Tool installs: none (no installs or upgrades by the L1 or any seat; pacman paused, untouched).
- Holds unchanged: certification OFF, K5 HELD, NAMESPACE/reap holds; L0 rulings open (credential-shaped names refuse-vs-redact; the `ignored` derivation; r46 mass id drift).
- L0 (filed in `.ufo/l0-questions.md` with this report): operator ruling on the admission of round 55 — C2 RD-A and C1 S55-S2 regressions; options: admit with the harms recorded, or re-run as r56 with the fixes first. Lane default: no admission until ruled.
- Incidents (disclosed in the lesson `## Mistakes`): an empty-body edit emptied the new lesson file once (uncommitted; rewritten from the same text); the fleet-root misroot sweep found no seat-written fleet file (`.scratch/` orchestrator state and a sibling round-31 report were not touched); a probe in scratch was contaminated by committing on top of a fixture and was rebuilt as a single-commit repository.
- Scratch: `/fast/scratch/hyaku/souji-r55/` (L1 and seat trees); removed after this report.

## Named limits (routed to r56; none edits the frozen bytes)

- N1 (critic; highest): a pair filing (`R53-CORRECTION`) inside a fenced block or an HTML comment in SCORECARD.md counts as filed (carried from v3).
- S55-S2 (regression, C1): a four-space-indented `<!--` opener hides a real overstatement from the pair scan (introduced by R6).
- RD-A (regression, C2): `1KEY=x`, `_KEY=x`, `2=x` pass silently (first-character class narrowed).
- S55-S1 (HIGH, carried): a NUL byte in a correction file makes numstat binary; DELETED-LINES reads -1 and the bogus correction goes unjudged.
- Closers with exotic whitespace (A09–A13), list-item fences (E09/E10), first-anchor INERT over-refusal (C04/C07), ratio exemption `2.5:1` (N4 / ERRATUM-R55-2), pair separators `=>` and `—>`, prose counts, `SOURCES.md` without `corpus/`, the first pair per line only, `\d` ASCII, unlexed bare filings (no FINDING id), empty-value receipt keys (S55-S5), RD-B/RD-C/RD-D/RD-E, hyphenated receipt keys (P1), selftest row-set assertion (C2-17/18), the numstat `\n`-only parse (repository-local `core.quotePath=false`), S4 relative `--work`, S5 docstring phrase, N6 exit-code legend, the form-feed fixture (ERRATUM-R55-1).
- Errata (append-only, in the lesson): ERRATUM-R55-1 (F7-FF bytes are vertical tab), ERRATUM-R55-2 (PTR wording: ratios exempt), ERRATUM-R55-3 (hand-written control labels), ERRATUM-R55-4 (pre-flight base field), ERRATUM-R55-5 (receipt exit codes).

## Pre-report gate

- `git ls-remote origin refs/heads/master` → `6d8bfb8ebb00f4806e7f83a0173aa4768358de33` (equals the lane tip).
- `grep -c '^## SHONEN' .ufo/reports/round-55/souji.md` → 1 (checked before the fleet commit).
- Misroot sweep: `git status --porcelain` at the fleet root shows only `.scratch/` orchestrator state and another lane's `.ufo/reports/round-31/kagi.md`; none was written by a souji seat and none was touched.
- Commit route: lane commits through `jj-lane.sh` only; report and L0 line through `fleet-commit.sh --as souji`.

```json
{"round":55,"lane":"souji","claims":[{"id":"C1","axis":"calibration 7","predicate":"holds","harm":"S55-S2 v3->v4 regression","admitted":false},{"id":"C2","axis":"coverage 8","predicate":"holds","harm":"RD-A v3->v4 regression","admitted":false}],"lane_head":"6d8bfb8ebb00f4806e7f83a0173aa4768358de33","report_commit":"pending","wave":{"v1":1,"seats":12,"attack":4,"connectors":1,"dead":0},"round_total_seats":12,"dead_seats":[],"open_l0":["round-55 admission: C2 RD-A, C1 S55-S2"],"trends":{"expansion":"unchanged","quality":"harmed","discernment":"unchanged"}}
```
