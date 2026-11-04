# mado — round 72 report (hyaku run 15)

lane: mado-shokunin
round: 72 (attempt 1; no earlier attempt existed — `.ufo/watchdog.log` carries no
`lane-dead-no-report mado round=72` line before this launch, so nothing was inherited)
base: `976684a27e99c2508037a60eec415f550f53d70e`
lane tip at filing: `3894451f71c76d202fe03ead9e05a8c467a3b98d`
declared claims: 2 — C1 **calibration** (the landing kill credit requires the run's own failure
detail) and C2 **operability** (the contract outcome reads the extracted instrument's own
summary, not its exit status); both frozen before any candidate data
(`.ufo/waves/round-72/claims-declaration-r72.md`, `5601e526`).

## Work performed

The round's declared claims: **C1 calibration** — credit a landing kill only when the child's
last parsed `MADO_LANDING_COUNTERS_SELFTEST: p/n` summary reports `n > 0` and `p < n` **and**
the run's own `SELFTEST FAIL` lines number exactly `n − p`; **C2 operability** — green the
contract outcome only on that last parsed summary (`n > 0`, `p == n`) with the kill count still
at 2/2, recording the exit status as evidence rather than the gate. No third claim; the r71
guard-census widening stays deferred and is named in the planned row.

- Froze both claims with predicates, counting commands, kill rules, targets and limits, plus the
  pre-freeze do-nothing controls: `5601e526` (`.ufo/waves/round-72/`; held 6/8 and 4/8).
- Built the round-72 harness generation carrying the two disjoint rule deltas (`credit()`,
  `summary_green()`/`outcome_verdict()`) with a hermetic selftest (83/83 at landing, 87/87 after
  the review repair): `9bcb4fd5`, `4f598cfd` (`quality/counters/c1-r72-landing-controls.py`).
- Built C1's counting command over eight real `bash` fixture modes (selftest 33/33) and C2's over
  eight frozen `(gate_out, gate_rc, killed)` cases (selftest 24/24, 25/25 after repair):
  `9bcb4fd5`, `4f598cfd` (`quality/counters/c1-r72-summary-credit.py`, `c2-r72-outcome.py`).
- Ran both frozen counting commands verbatim at `9bcb4fd5` and re-scored them identically at
  the repair `4f598cfd`: `MADO_R72_SUMMARY_CREDIT: cases=8 correct=8 base_correct=6
  verdict=TARGET_MET` (rc 0) and `MADO_R72_OUTCOME: cases=8 correct=8 base_correct=4
  verdict=TARGET_MET` (rc 0) — `.ufo/waves/round-72/measurement-c{1,2}-r72.txt`,
  `receipts/re-measure-r72.txt`.
- Opened two admits and one rejection on CPython 3.14.8 (three fetches each, byte-identical,
  receipts under `.ufo/waves/round-72/fetch/`), appended S444/S445/S446, census exit 0
  (380 → 383 rows).
- Admitted two knowledge entries, indexed them (85 → 87 rows), extended the Frontier, refined
  PROVINCE, added QUALITY criteria 116–117, registered the harness and both counters in
  `quality/tool-ledger.md` (122 → 125) and four r71/r72 counting instruments in the `SKILL.md`
  Gate registry (the r71 routed defect).
- Repaired or curated the r71 spot-check's routed/conformance defects: the uncurated reject
  (now S446), the 404-at-tag anchor (S446 at `Doc/builtins/stdtypes.rst`), the quote word
  count (re-counted with `awk`), and the harm-watch rc wording (per-command rc recorded;
  QUALITY 116(b)). The "no per-seat status in results.json" is the driver's file shape: this
  report gives the per-seat observations directly (below) instead of trusting a status field.
- Wave: one v1 wave of 13 seats (executor 3, scribe 3, scout 2, reviewer 2, critic 1,
  mutation-tester 1, connector 1; attack share 4/13 = 30.8 %), validated under the band-8–16
  policy and dispatched through the inline spawn handoff; settlement and per-seat deliverables
  below.
- Applied the wave's review findings as a repaired instrument (`4f598cfd`) plus an append-only
  declaration erratum (`18db46bd`): literal "last parsed summary", the production fail-line
  grammar, the stream-precedence limit and the finite-set statements.

## Wave 1 — shape, seats and settlement

One v1 wave, 13 seats, validated under `/home/vgpnk/Projects/shokunin/scripts/hyaku/ufo-wave-policy.json`
(band 8–16; spawn 13, resume 0), dispatched via `.ufo/waves/round-72/w1.ready` →
`w1-dispatch.json`. All 13 seats settled; `w1-results.json` carries 13 entries, every output
non-empty, and each named file exists on disk (per-seat observation below; `results.json` has no
`status` field, so settlement alone is not treated as delivery).

| Seat | Role | Deliverable | Observation |
|---|---|---|---|
| R72ExecC1 | executor | `w1/R72ExecC1/R72ExecC1.md` | re-ran the frozen C1 command (rc 0, `correct=8 base_correct=6`) and the held prototype; reconciled with the receipt |
| R72ExecC2 | executor | `w1/R72ExecC2/R72ExecC2.md` + `rederive-baseline.py`, `independent-baseline.txt` | re-ran the frozen C2 command (rc 0, `correct=8 base_correct=4`), independently re-derived the held 4/8 |
| R72ExecBattery | executor | `w1/R72ExecBattery.md` | ran the harm battery; caught the mid-flight census E11 (rows before entry) and the expected pre-registration ledger uncovered=3; final converged run green |
| R72ScribeEntryC1 | scribe | `w1/R72ScribeEntryC1.md` + draft entry + selftest observation | drafted the C1 entry (decision table, negatives, ties, replay limit) |
| R72ScribeEntryC2 | scribe | `w1/R72ScribeEntryC2/report.md` + draft entry | drafted the C2 entry; correctly kept the strict directory bound |
| R72ScribeLesson | scribe | `w1/R72ScribeLesson.md` + `draft/{corpus/lessons/round-72.md,QUALITY-criteria.md,SOURCES-rows.md}` | drafted lesson, three registry rows and two criteria |
| R72ScoutSources | scout | `w1/R72ScoutSources.md` + `receipts.jsonl`, `quotes.md`, `fetch/` | three fetches per URL byte-identical; reproduced the r71 reject's 404 at the cited path and the 200 at the real path |
| R72ScoutFrontier | scout | `w1/R72ScoutFrontier.md` + census snapshots, guard proof | census before/after, id-collision guard proof (0–3-space fixture), index/ledger counts |
| R72RevC1 | reviewer | `w1/R72RevC1/R72RevC1.md` + `review_probe.py`, `harness-delta.diff` | F1 P2 (last prefix vs last parsed), F2 P3 (`SELFTEST FAILURE` counted); both repaired |
| R72RevC2 | reviewer | `w1/R72RevC2/R72RevC2.md` + `repro.py` | Medium (stream-concatenation order defeats chronological last-wins), Low (fraction vs parsed summary); the first became the erratum's declared limit, the second was repaired |
| R72CriticClaims | critic | `w1/R72CriticClaims/R72CriticClaims.md` + `audit.py`, `q1..q4.txt` | constant controls cannot reach either target; Counterexample A (zero-denominator blind spot), Counterexample B (last parsed) — both addressed (repair + finite-set statement) |
| R72MutBattery | mutation-tester | `w1/R72MutBattery/R72MutBattery.md` + mutants/runs | M1/M2/M4 killed; **M3 and M5 survived** (GAP-1 zero-denominator, GAP-2 vacuous None-guard), disclosed |
| R72ConnSiblings | connector | `w1/R72ConnSiblings/R72ConnSiblings.md` | found the summary-over-status doctrine in kengaku; named one considerthese proposal (live-tool table) not implemented |

Attack share 4/13 = 30.8 % ≥ 25 %; one connector seat. No seat died; no seat was replaced.

## Landed changes

| Change | LOG entry | Commit |
|---|---|---|
| Frozen claims declaration, the two frozen control sets and the pre-freeze do-nothing baselines | round-72 entry, bullet 1 | `5601e5269bdc365213507604357375a74fe61fe1` |
| Harness generation `c1-r72-landing-controls.py` (two rule deltas) and both counting commands | round-72 entry, bullets 2–3 | `9bcb4fd5b598844f168230dc05e441721d95b272` |
| Wave spec/dispatch/ready evidence and both measurement receipts | round-72 entry, bullets 4 and 9 | `fd9ea03b554d6925594957c381f09e29a2ac159e` |
| SOURCES S444/S445/S446, two knowledge entries, README index + Frontier, PROVINCE refinement, QUALITY 116–117, lesson, SKILL Gate registry, tool ledger | round-72 entry, bullets 5–8 | `925a3e8a355bf8b343ba3591c8290dd3ffe2c609` |
| SCORECARD round-72 section, LOG entry, harm-watch receipt | round-72 entry, bullet 10 | `200c16524602720470b731a1f0361571506bcf7a` |
| Harm-watch re-run appended after the scorecard commit (axis table 0 mismatched) | round-72 entry, bullet 10 | `10730ee8952a3e3b9284310df8584369ccf1e1f9` |
| Review-driven repair (literal last parsed summary; production fail-line grammar) + red-before/green-after receipt | round-72 entry, appended repair bullet | `4f598cfd142e1bfcf4d63341e0b5ea11348c5c4c` |
| Declaration erratum, LOG bullet, lesson addendum and scorecard repair subsection | round-72 entry, appended repair bullet | `18db46bd5978bb55c04d96748c67ac4470023d93` |
| Wave 1 seat reports, results, dispatch markers, harm-watch re-run and the mutation-gap disclosure | round-72 entry, appended wave bullet | `3894451f71c76d202fe03ead9e05a8c467a3b98d` |

## Before → after measurements

**C1 — calibration.** Counting command (from the lane root):

```sh
python3 -I quality/counters/c1-r72-summary-credit.py --repo . --rev 9bcb4fd5b598844f168230dc05e441721d95b272 \
  --base-rev 976684a27e99c2508037a60eec415f550f53d70e --scratch-root DIR
```

Before: the held round-71 harness scores the eight frozen modes `base_correct=6/8` (bounded
7.5000), crediting exactly `bare-failing` and `mismatch-detail`
(`.ufo/waves/round-72/control-baseline-c1-r72.txt`). After: `cases=8 correct=8 base_correct=6
verdict=TARGET_MET`, rc 0, measured at `9bcb4fd5`
(`.ufo/waves/round-72/measurement-c1-r72.txt`) — bounded 10.0000. The repaired instrument
(`4f598cfd`) scores the identical frozen set (`receipts/re-measure-r72.txt`).

**C2 — operability.** Counting command (from the lane root):

```sh
python3 -I quality/counters/c2-r72-outcome.py --repo . --rev 9bcb4fd5b598844f168230dc05e441721d95b272 \
  --base-rev 976684a27e99c2508037a60eec415f550f53d70e \
  --controls .ufo/waves/round-72/controls/c2-controls-r72.json --scratch-root DIR
```

Before: the held `outcome_verdict(selftest_rc, killed)` scores `base_correct=4/8` (bounded
5.0000), wrong in both directions (`failing-summary-exit0`, `green-summary-exit2`,
`no-summary-exit0`, `garbled-summary-exit0`; `.ufo/waves/round-72/control-baseline-c2-r72.txt`).
After: `cases=8 correct=8 base_correct=4 verdict=TARGET_MET`, rc 0, measured at `9bcb4fd5`
(`.ufo/waves/round-72/measurement-c2-r72.txt`) — bounded 10.0000; identical at the repaired
instrument.

**Harm watch at the landing tip** (`18db46bd` and re-run appended after the wave integration,
`.ufo/waves/round-72/receipts/harm-watch-r72.txt`): gate `MADO_SELFTEST: 460/460`; index
`indexed=87/87 missing=0 dangling=0`; ledger `population=125 ledger_rows=125 uncovered=0
verdict=TARGET_MET`; axis table `checked=3 mismatched=0` (navigation 87/87, calibration 86/86,
operability 12/12); census exit 0; frozen r71 instruments and `tools/mado-verify.sh` /
`quality/landing-counters.sh` blob-identical at base and tip.

**Mutation gaps disclosed (not hidden).** `R72MutBattery`: M1 (no arithmetic), M2 (relaxed
comparison) and M4 (kill-count-only outcome) are killed by the frozen sets; **M3** (dropping
`summary_green()`'s `n > 0` guard) and **M5** (the counters' `score()` None-guard) survive both
frozen sets — GAP-1 (no zero-denominator case) and GAP-2 (no absent candidate). Both become
round-73 controls under a new frozen denominator; this round does not widen its sets, and the
harness selftest carries the zero-total case that would catch M3.

## Sources & frontier

Census command, run at round start and round end:

```sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin mado
```

- Before: exit 0, `mado ok …/corpus/SOURCES.md`, **380** registry rows
  (`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`), last id S443.
- After: exit 0, `mado ok …/corpus/SOURCES.md`, **383** rows, last id S446.
- Rows added by tier: **A = 3** (S444 docs, S445 code, S446 docs/rejected); B = 0; C = 0.
- Rows touched old→new: S442 `used-by` gained `corpus/knowledge/summary-credit-own-detail-r72.md`
  (old→new logged in `corpus/lessons/round-72.md` § Gate); S444/S445 enter `mined`; S446 enters
  `rejected` with reason and flip. No `status`/`recheck` cell of a held row changed.
- Frontier rows advanced: the r71 kill-credit bullet extended with the own-detail rule and the
  summary-driven outcome (`corpus/README.md` § Frontier, round-72 bullet); two entries admitted
  on ground the coverage map did not hold.
- The round start is exit 0 (the registry already existed); W04 warnings are the held
  superseding-URL family only.
- **Assimilation: none** — no `merge/mado/` theme was adopted; the round's ground is the lane's
  own instrument chain and the CPython sources above. `considerthese/2026-10-28.md` was scanned
  (connector seat); the proposal that fits (a live-tool table with last-live-run) is not
  implemented this round.

## Trend verdicts

- **expansion: improved** — two admitted knowledge entries on ground the coverage map did not
  hold (`summary-credit-own-detail-r72.md`, `outcome-verdict-gate-summary-r72.md`), each
  `source:` citing rows opened this round or held mined rows (S444/S445 new, S442 mined), index
  85 → 87, plus the round-72 Frontier bullet and the capability row.
- **quality: improved** — the landing instrument chain gains two rules the previous generation
  did not have, each with a frozen control set, a do-nothing control, a measured red-before and
  a review-driven repair; four r71 routed/conformance defects are repaired or curated.
- **discernment: improved** — one new rejection curated as a row with its flip (S446); the
  round's Gate records both admits and the reject for the closure's non-author spot-check;
  QUALITY 116–117 added from this round's own defects with "shown able to fail" controls; the
  wave's attack seats produced findings that changed the shipped instrument (F1/F2 repair,
  the erratum), and the mutation survivors are disclosed rather than reclassified.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources —
  pointer: `SKILL.md` § Gate registry (four new gate rows, `925a3e8a`); no non-author verifier.
- [~] At least one end-to-end domain task executed and logged in LOG.md — pointer: LOG.md
  round-72 entry and `.ufo/waves/round-72/measurement-c{1,2}-r72.txt`; instrument work, not a
  desktop task, and no outside-lane verification.
- [~] Instructions executable by an agent without oral context — pointer: the two counting
  commands in this report run from the lane root exactly as written; dispatched subagents are
  the lane, so this stays asserted.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — pointer: PROVINCE.md round-72
  refinement and the changed paths of `925a3e8a`/`4f598cfd` (corpus, instruments, registry
  only); no sibling repo, config plane or compositor touched.

## Stale-lane

Respawn-per-round driver: this mission opened at the round-72 launch and is closed by this
report; no other mado mission is open. Progressing: lane commits `5601e526` … `3894451f` inside
the mission window.

## Tool installs

None. No pacman transaction (host-wide pause respected); no `uv tool`/`npx`/binary install; no
tool upgraded.
