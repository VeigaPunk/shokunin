# tsukuroi — round 96 report

Lane: tsukuroi (operability + freshness; host operability and repair). Fleet campaign: hyaku, run 15.
Pre-round lane tip `73c47107e8bda79375517ee24ec3c13688586305`; freeze `38adc4ed`; dispatch
`b0bf1be9`; final lane hash is cited at the end (and in the driver's closure ledger).

## Work performed

Declared claims (2, frozen in `.ufo/plans/round-96.md` and `.ufo/waves/round-96/claims.json`):

- **C1 — depth 8 (tied lowest)**: `tools/limine-pin-battery-r96.py` gains four roster families beyond
  the r95 roster (99): `EXPLICIT-VERSION-ECHO` (an explicit `--limine-version` is echoed in the JSON
  with source `flag`), `EXPLICIT-VERSION-ERA` (`visibility_era` follows the whole tuple),
  `REFUSAL-VERSIONS-9DIGIT-Y` (the Y-component cap accepted in both eras) and `EXTRA-COMPONENT`
  (four four-component shapes refused, `12.9.6` the same-list positive control), with four
  one-clause bends and the r95 battery as the do-nothing control.
- **C2 — calibration 9**: `tools/check-r96-calibration.py` binds the six routed round-95
  self-assessment defects (F1-F6) to the lane's bytes: criterion 140 exists, the registry-gate
  receipt and SCORECARD void binding, the r95 docstring correction, the README scope, a
  `b8f878c8` registry PASS receipt, and the report's own count against the committed ledger.

Work items, each with its evidence pointer:

- **Freeze and controls** (`38adc4ed`): the battery, bend emitter and calibration checker, the
  do-nothing copies (`do-nothing-battery-r95.py` sha256 `a51dca18…`, byte-identical to the r95 land
  at `b8f878c8`; `do-nothing-gate-r95.py` `7d79ac29…`, the unchanged gate), the four bends, the
  pre-round calibration receipt and the development runs, pinned in
  `.ufo/waves/round-96/before/instruments.sha256` (17 entries, `sha256sum -c` 0 FAILED).
- **Wave w1** (`b0bf1be9`): one v1 wave, 14 seats — 5 executors (`ExecBattery`, `ExecBend`,
  `ExecDoNothing`, `ExecCalibration`, `ExecControls`), 2 scouts (`ScoutSources`, `ScoutDrift`),
  2 scribes (`ScribeKnowledge`, `ScribeLesson`), 2 reviewers (`ReviewBattery`, `ReviewCalibration`),
  1 critic (`CriticClaims`), 1 mutation-tester (`MutBound`), 1 connector (`ConnectorOverlap`);
  attack seats by the prefile gate's role set are 5/14 = 36 % (≥25 %); validator `counts` 14 spawn /
  0 resume / 14 total, `w1-validate.err` 0 bytes; seat reports under `.ufo/waves/round-96/w1/`.
  The L1 holds the §3 planner seat (the `ScoutDrift` item carries the bounded planning data-walk).
- **C1 landed leg** (measured at `59cbfe2f`): `103/103 met` in each of three runs, `failed_families []`,
  0 error rows, canonical lane and `git clone --shared` at the freeze tip — receipts
  `.ufo/waves/round-96/after/c1/gate-canonical.json`, `w1/ExecBattery/c1-canonical.json`,
  `w1/ExecBattery/c1-clone.json`.
- **C1 bend legs** (measured at `59cbfe2f`): N01 `102/103 ["EXPLICIT-VERSION-ECHO"]` 0 err; N02
  `102/103 ["REFUSAL-VERSIONS-9DIGIT-Y"]` **4 err** (its own rc-64 refusals, A3); N03
  `102/103 ["EXPLICIT-VERSION-ERA"]` 0 err; N04 `101/103 ["EXTRA-COMPONENT","REFUSAL-VERSIONS"]`
  0 err, each ×3 both layouts — `.ufo/waves/round-96/after/c1/bend-*.json`, `w1/ExecBend/`.
- **C1 do-nothing legs**: the r95 battery reads `99/99 met` on the landed gate and N01/N02/N03, and
  `98/99 unmet ["REFUSAL-VERSIONS"]` on N04 (the pre-existing `12.9.5.1` row), 0 error rows, ×3 both
  layouts — `.ufo/waves/round-96/after/c1/dn-gate.json`, `dn-N04.json`, `w1/ExecDoNothing/`.
- **C1 mutation evidence**: 8 one-clause gate mutants; 5 killed (M01/M02/M03/M04/M05), 3 survived —
  M06 (Z-component cap, Frontier), M07 (`lower()` equivalent) and M08 (9-digit leading-zero
  boundary, Frontier) — `w1/MutBound/` (`summary.json`, `mutants-manifest.json`).
- **C1 forgers**: 5 of 7 wrong gates killed by the new families (source-always-probe, source-always-
  flag, era-first-component, era-max-component, blanket refusal, fixed echo); F-E
  (`label-boundary-only`) and F-G (`trailing-zero-accepted`) read `103/103 met` — recorded as
  Frontier, not claimed — `w1/ReviewBattery/`.
- **C2 counter** (measured at `59cbfe2f`/`a814f24d`): pre-round `73c47107` + r95 report/ledger →
  `FAIL` with findings in F1-F6; landed tree + the filed report + the committed ledger → `PASS`
  `findings []`; `--selftest` `PASS 7/7`; six one-fault fixtures fire exactly their own id (A1) —
  `.ufo/waves/round-96/before/c2-before-73c47107.json`, `after/c2-after-landed.json`,
  `w1/ExecCalibration/`, `w1/ExecControls/`.
- **C2 repairs**: QUALITY 140 (`corpus/QUALITY.md`), receipt `.ufo/waves/round-96/before/r95-registry-gate.sha256`
  (sha256 `6fcb2d0a…` = `git show b8f878c8:tools/check-registry-coverage.py`) plus the SCORECARD
  Round 96 void binding, both r95 tool docstrings corrected (`59cbfe2f`), README sentence scoped
  (F4), `b8f878c8` registry PASS receipt (F5), and the report count (F6, this file).
- **Falsification ledger**: the committed `.ufo/waves/round-96/claim-falsification.tsv` holds 11
  rows — 3 falsifies-wording rows and 1 falsifies-number row, plus 7 neutral — covering both claims
  and all five attack seats (`ReviewBattery`, `ReviewCalibration`, `CriticClaims`, `MutBound`,
  `ConnectorOverlap`); every row names an existing wave artifact and each wording row names the
  amendment that narrows it. `scripts/hyaku/prefile-falsification.py` (run before filing) reads
  `PASS`.
- **Corpus and frontier step**: the CPython `sys.int_info` source opened and landed as S390, then
  superseded by S391 (CORPUS.md rule 2) after the first anchor byte was found wrong: S391 carries
  the corrected anchor (sentence starts at byte 157851, id at 157525 of the 2026-11-08 pin, sha256
  `a7e00587…`) and the version-pinned `/3.15/` URL; S390's `status`/`used-by` moved mined→queued and
  entry→`—` (logged in the lesson). Landed with it: knowledge entry
  `corpus/knowledge/limine-bound-per-component-r96.md`, lesson `corpus/lessons/round-96.md` (Gate,
  Mistakes, Routed, the r95-manifest relation), README Round 96 + Frontier, SCORECARD measured rows;
  census `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tsukuroi` exit 0
  before (389 rows) and after (391 rows).
- **Assimilation**: `considerthese/2026-10-26.md` — its "counter-attack scoreboard" proposal
  (adopted as QUALITY 115 at r82, not practised since r85) is the one item revived this round; it
  lands as the C1 row above (arms fielded 4 bends + 8 mutants, killed/survived and the class that
  decided each), cited to the proposal and date. The same sweep corrected an older broken locator:
  `corpus/README.md` cited `considerthese/2026-10-26.md #22`, which exists in no lane copy; it now
  names the "Downstream patch-offset check" bullet.
- **Registry**: the three r96 tools registered in `SKILL.md`; `check-registry-coverage.py --revision
  a814f24d...` → `PASS`, 154/154 — `.ufo/waves/round-96/after/registry-a814f24d.json`.

## Landed changes

| Change | LOG.md entry | Commit |
|---|---|---|
| Freeze: battery r96, bend emitter, calibration checker, controls, pre-round receipt, development runs | "Round 96 — freeze" | `38adc4ed` |
| Wave spec, dispatch, registry, ready file | "Round 96 — wave" | `b0bf1be9` |
| C2 repairs (QUALITY 140, SCORECARD void binding + tip receipt, r95 docstrings, README scope), S390 row, knowledge entry, lesson, LOG/SCORECARD | "Round 96 — C2 repairs" / "Round 96 — settle" | `59cbfe2f` |
| Registry rows for the three r96 tools; A4/A5 amendments; wave-discernment mistakes; frontier additions | "Round 96 — settle" | `a814f24d` |
| Wave evidence (14 seat reports, receipts, results) and the final measured receipts | "Round 96 — settle" | `92e03af7` (evidence), `c6786148` (results) |

## Before → after measurements

### C1 — depth 8 (roster 99 → 103; metadata and per-component accepted legs)

Counting command: `python3 tools/limine-pin-battery-r96.py --gate <GATE> --runs 3 --work <scratch>
--json <out>`; summary with
`python3 .ufo/waves/round-95/before/controls/count-runs.py <out> --family EXPLICIT-VERSION-ECHO
--family EXPLICIT-VERSION-ERA --family REFUSAL-VERSIONS-9DIGIT-Y --family EXTRA-COMPONENT`.

- Before: the r95 roster is 99 families and has none of the four names; it reads `99/99 met` on the
  landed gate (do-nothing leg) and cannot see N01/N02/N03 (`99/99 met`), while N04 moves only its
  pre-existing `REFUSAL-VERSIONS` row (`98/99 unmet`).
- After (measured at `59cbfe2f`): `103/103 met` ×3 canonical + ×3 clone, 0 error rows; the four
  bends at `102/103` (N04 `101/103`) with the frozen failed-family sets; N02's four error rows are
  its own rc-64 refusals (A3). Mutation and forger evidence: 5 of 8 one-clause gate mutants killed
  (M06/M08 and the equivalent M07 survive) and 5 of 7 wrong-gate forgers killed (F-E/F-G survive) —
  `w1/MutBound/`, `w1/ReviewBattery/`; every survivor is named in the README Frontier.
- Verdict: **met on A3+A4** (author-side; closure to re-derive). A4: `EXTRA-COMPONENT` is a QUALITY
  136 twin — the r95 roster alone kills its bend and the r95 `--usage-check` already sends
  `12.9.6.1` — so the measured discrimination delta is three families, not four.

### C2 — calibration 9 (six routed r95 self-assessment defects → 0)

Counting command: `python3 tools/check-r96-calibration.py --root <tree> --report <report> --tsv
<ledger>` and `python3 tools/check-r96-calibration.py --selftest`.

- Before (`73c47107` + r95 report + r95 ledger): `status FAIL`, 10 findings covering F1-F6 — ids
  `F1,F2,F3,F4,F5,F6` — identical to the committed `before/c2-before-73c47107.json` when re-run with
  the freeze-pinned checker (two seats reproduced it field by field).
- After (landed tree + this report + `.ufo/waves/round-96/claim-falsification.tsv`): `status PASS`,
  `findings []`; `--selftest` `PASS 7/7`; one-fault fixtures fire exactly their own id (A1).
- Verdict: **met on A5** (author-side; closure to re-derive). A5: the checker asserts six remedy
  conditions; only F6 binds a recorded number (the report's count to the round ledger) and it binds
  the first numeric occurrence of each class — a named limit, not a re-measurement of r95 facts.

## Sources & frontier

`SOURCES.md` rows before → after: 389 → 391 (`git show 73c47107:corpus/SOURCES.md | grep -cE
'^\|[[:space:]]*S[0-9]{3,}'` → 389; `grep -cE '^\|[[:space:]]*S[0-9]{3,}' corpus/SOURCES.md` → 391).
Rows added by tier: two A (S390, CPython `sys.int_info.default_max_str_digits`, and S391 which
supersedes it with the corrected anchor and the version-pinned URL). Rows touched old→new: S390
`status` mined→queued and `used-by` entry→`—`; S389 re-opened and still `mined`.
Census: `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tsukuroi` exit 0
before and after (0 E findings; 57 W04 + 1 W01 after). Frontier rows advanced: the r95
"four-component shape not sent at battery level" correction (roster and instrument); new rows for
the Z-component boundary and leading-zero boundary (uncertified), the Y-family docstring's era claim
(false; routed), and the calibration checker's F6 first-match/provenance limits plus F4's
raw-substring clause 2, which misses a newline-wrapped over-scope sentence (`w1/ScoutDrift`
p4-f4-blindspot). Assimilation: one `considerthese/2026-10-26.md` proposal (counter-attack
scoreboard, adopted as QUALITY 115 at r82 and revived here) mined into the C1 row.

## Trend verdicts

- **expansion — improved.** One admitted knowledge entry on ground the coverage map did not hold
  (`knowledge/limine-bound-per-component-r96.md`, the per-component cap and the gate's reported
  metadata) and one new SOURCES row (S390), census exit 0; a new kind of evidence (the metadata
  families) enters the battery.
- **quality — improved.** The r95 routed defects are closed with a re-runnable counter (before six
  classes, after zero; one-fault controls), the registry is green at the landed tip (154/154) and
  the r95 docstring/README false statements are corrected with their manifest relation stated; no
  admitted entry fails its re-check.
- **discernment — improved.** Five wave seats produced six narrowings (A1-A5 plus the F-4 docstring
  routing) and three named survivors (M06/M07/M08, F-E/F-G), each recorded with its receipt; the
  capsule's own errors (the frozen 0-error clause, the EXTRA twin, the remedy-checklist wording,
  the checker drift) are filed as mistakes rather than papered over.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — unchanged
  this round apart from the three registry rows; author-side pointer: `SKILL.md` registry table
  (rows `limine-pin-battery-r96`, `make-r96-bends`, `check-r96-calibration`) and
  `check-registry-coverage.py --revision a814f24d` = PASS 154/154.
- [~] At least one end-to-end domain task executed and logged — C1's landed/bend/do-nothing legs and
  C2's before/after runs are this round's executed task; pointer `.ufo/waves/round-96/after/`.
- [~] Instructions executable by an agent without oral context — the seat prompts in
  `.ufo/waves/round-96/w1-spec.json` and the seat reports show 14 seats ran from the spec alone;
  no whole-SKILL no-oral-context retest was executed.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `w1/ConnectorOverlap/` scanned 20 siblings
  (0 duplicate claims, 0 contradictions), stayed out of kama/kumitate and left kaidoku/revenger
  ownership unruled; no PROVINCE change was needed.

## Round shape and incidents

Wave w1: 14 seats, 5 attack (36 %), 0 connector duplicate (1 seat), 14 total in one v1 wave; 0 dead
seats; residual call none. The L1's §3 planner seat is held by the L1 (validator rejects a planner
item; the `ScoutDrift` data-walk rides a scout). Tool installs: none. Stale-lane: respawn-per-round
driver; no other mission of this lane is open. Disclosed: the frozen calibration checker's worktree
bytes drifted for ~6 minutes mid-wave (`ad894667` vs pinned `7ff63524`) and were restored to the
pinned bytes; two seats caught it, the void clause is evaluated on the manifest bytes, and A2
records the window (`before/plan-amendments-A1-A2.md`).

Lane HEAD (pushed): `c67861483ad64491954fdcfd2003189b2dfad8b9` —
`git ls-remote origin refs/heads/master` reports the same hash; every lane-side receipt cited above
is at or before that revision, and the frozen instrument bytes are unchanged (`sha256sum -c
.ufo/waves/round-96/before/instruments.sha256` → 0 FAILED).
