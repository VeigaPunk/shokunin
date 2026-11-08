# mado round 99 — report (hyaku run 15, attempt 4)

Lane `/home/vgpnk/Projects/shokunin/mado-shokunin`, branch `master`. Base
`2cbaa141f42df9dfeee4d207cae6558a4dd59863` (round-98 closure tip). Round contract
`.ufo/waves/round-99/claims-declaration-r99.md`; plan and pre-file amendments
`plans/round-99.md`; frozen claims `.ufo/waves/round-99/claims.json`; falsification ledger
`.ufo/waves/round-99/claim-falsification.tsv`. Lane tip at filing: `0e8f39f5`
(local = remote, `ls-remote origin refs/heads/master`).

**Declared claims (2), each on a distinct axis, causally separable, no exploratory claim.**

- **C1 — coverage (capability, new surface): the launch spawn environment.** After this round
  `tools/mado-launchenv.py` answers, read-only, what surrounds a launch argv — the load gate
  (`TryExec` then `Exec` through `g_find_program_for_path` with the entry's `Path=` as working
  directory), the twelve-row `Terminal=true` terminal selection and prepend, the post-prepend
  `argv[0]` lookup, `Path=` as the child's cwd (empty inherits, unenterable fails the spawn), and
  `GIO_LAUNCHED_DESKTOP_FILE` — scored against the installed `/usr/bin/gio` on a frozen case set.
  Sourced claim: S532/S533/S534. **Narrowed pre-file (A1):** the base already holds the
  `g_find_program_for_path` primitive (`tools/mado-mime.py:467`); the claim is the composite and
  its refusal causes, not the primitive.
- **C2 — operability: the harm watch as an instrument.** After this round `quality/harm-watch.py`
  replays a frozen 28-leg panel, each with a frozen expectation (`rc` + stdout marker), and its
  census fails closed on a leg the panel declares but does not carry (plus an undeclared extra
  row). **Narrowed pre-file (A5):** of the two round-98 dropped legs, `r97c1_filetype` was noticed
  only by the outside spot-check while `r97c2_counter_selftest` was already named in the lane's
  own final round-98 receipt (`harm-final-r98.txt:41-43`, committed `fa4445af`). Also narrowed:
  A3 (the predicate's `selftest_checks` is the counter's fixture selftest, not the gate's
  `--selftest`), A4 (a per-leg setup error aborts the remainder and exits 2), A6 (the
  count/duplicate/round-missing census checks are gate behaviour, not counter-verified).
  **Verdict: TARGET_MISSED (honest stop, A9).** The attempt-4 re-derivation of the unchanged
  predicate scores 26/28 legs with two timeouts at the frozen 600 s per-leg cap under fleet load;
  the instrument and its discrimination controls land, but `mismatches == 0` is unmet and is
  reported, not narrowed.

## Work performed

- **C1 candidate, oracle-labelled cases, mutants and controls.** `tools/mado-launchenv.py`
  (frozen sha `a63c20c8…eb16`) reads one desktop file, an argument list and a PATH string and
  answers the five surfaces plus four refusal causes; `quality/counters/c1-r99-launchenv.py`
  scores it on 67 cases / 31 classes, 69 counted mutants, a seeded fresh leg and two controls.
  Evidence: `.ufo/waves/round-99/receipts/c1-measured-r99.txt`,
  `.ufo/waves/round-99/receipts/c1-at-base-r99.txt`; commit `56a9b299`.
- **C1 rules grounded in the fetched GLib bytes and the spec.** `gdesktopappinfo.c`
  (load gate `:1946-2004`, terminal table `:2765-2830`, prepend/lookup `:3027-3093`, env
  `:3036-3040`, spawn `:3134`), `gutils.c` (`g_find_program_for_path` `:300-500`, `IS_DIR` at
  `:340` and `:487`), `gio-tool-launch.c` (`:91`, `:116`), the Desktop Entry Specification's
  `TryExec`/`Path`/`Terminal` sentences. Evidence: `corpus/knowledge/gio-launch-env-r99.md`,
  `.ufo/waves/round-99/receipts/sources-open-r99.txt`, `.ufo/waves/round-99/fetch/`.
- **C2 gate, panel, planted controls and counter.** `quality/harm-watch.py` (frozen sha
  `37a0544b…65b9`) plus `quality/counters/c2-r99-harm-watch.py`; the frozen 28-leg panel
  (`.ufo/waves/round-99/controls/harm-panel-r99.json`, sha `160763ce…e39a`) and five planted panels
  (`.ufo/waves/round-99/controls/harm-planted/`). The attempt-4 re-derivation ran 28/28 legs, 26
  green, two timeouts at the frozen 600 s cap (`mismatches=2`); the discrimination controls stayed
  green. Evidence: `.ufo/waves/round-99/receipts/c2-measured-r99.txt`,
  `.ufo/waves/round-99/receipts/c2-probe-r99.txt`,
  `.ufo/waves/round-99/receipts/c2-at-base-r99.txt`; commit `3b69f041`; verdict TARGET_MISSED
  (honest stop, A9).
- **Frontier step.** `corpus/SOURCES.md` 466 → 469 rows / 119 → 120 entries (S532
  `gio-tool-launch.c`, S533 `gutils.c`, S534 the recognised-keys spec; all tier A, all opened this
  round); the entry `corpus/knowledge/gio-launch-env-r99.md`; README index and Frontier rows;
  `SKILL.md` rows `mado-launchenv` / `mado-r99-launchenv` / `mado-harm-watch` /
  `mado-r99-harm-watch`; `quality/tool-ledger.md` rows 234–237; PROVINCE round-99 refinements
  (read-only, no new write surface). Evidence: `corpus/lessons/round-99.md` `## Gate`,
  `.ufo/waves/round-99/receipts/census-start-r99.txt` (rc 0, 466 rows),
  `.ufo/waves/round-99/receipts/census-end-r99.txt` (rc 0, 469 rows),
  `.ufo/waves/round-99/receipts/readback-r99.txt` (rows=469 entries=120 findings=0).
- **Record repairs D1–D8 from the round-98 outside spot-check.** D1 the S532–S534 rows; D2 the
  readback gate re-run at the records tip (`readback-r99.txt`, findings=0); D3 the two r98 SKILL
  rows' pins re-derived (`SKILL.md:2980`, `:2982`); D4 the LOG round-98 seed and mistake count
  corrected (`LOG.md:4657-4673`, seed `f00d3edcdb285ac0`, 12 mistakes); D5 the panel restores both
  dropped legs; D6 QUALITY 170 (M98-1 class) and 171 (M99-1); D7 this report; D8 the two-commit
  attribution in the LOG erratum. Evidence: `.ufo/waves/round-99/w1/R99MReviewRecords.md` sections
  1–10; `.ufo/waves/round-99/receipts/review-records-r99.txt`.
- **Wave w1 falsification.** One v1 wave, 12 seats, attack 6/12 = 50 %: reviewer C1, reviewer
  records, critic C2, two mutation-testers, connector, plus scout, scribe and four executors. The
  attacks falsified three claim sentences (A1, A3/A4, A5/A6) and confirmed the C1 numbers; the C2
  number was **not** confirmed — the attempt-4 re-derivation missed at the frozen 600 s cap (A9)
  and the mutation seat's F5 had predicted the cap's fragility. Every attack seat is reconciled in
  `claim-falsification.tsv`. Evidence:
  `.ufo/waves/round-99/w1-results.json`, `.ufo/waves/round-99/w1/*.md`; commit `3b69f041`.
- **Pre-file falsification gate (Amendment 59).** Skeleton written from `claims.json` + the six
  attack artifacts; narrowed verdicts point to `plans/round-99.md`; the control (one attack-seat
  row removed) printed `FINDING attack-seat-unread` and the frozen ledger passes. Evidence:
  `.ufo/waves/round-99/claim-falsification.tsv`,
  `.ufo/waves/round-99/receipts/prefile-control-r99.txt`.

## Landed changes

| Change | LOG entry | Commit |
|---|---|---|
| C1 candidate, counter, frozen cases/mutants/fresh generator, controls | Round 99, C1 bullet | `56a9b299` |
| Knowledge entry, SOURCES S532–S534 + used-by on S504/S506/S528/S529/S531, README index/frontier, SKILL and tool-ledger rows, PROVINCE refinements, QUALITY 170–171, lesson Gate/M99-1/M99-2, measured receipts | Round 99, frontier bullet | `87ebed1a` |
| The entry's `gdesktopappinfo.c`/`gshell.c` citations acknowledged in S504/S506 `used-by` (read-back R4) | Round 99, frontier bullet | `dc0a8637` |
| Harm-watch ledger pointer drops a backticked non-path token | Round 99, C2 bullet | `19835e0e` |
| Harm watch gains `--only` (census still full-panel); counter scopes planted runs; panel timeout re-frozen to 600 s | Round 99, C2 bullet | `e39cd5e0` |
| Harm-watch gate pin follows the `--only` patch (`37a0544b`) | Round 99, C2 bullet | `4c7cf0cb` |
| Wave w1 evidence (results, seat reports, regenerated controls) | Round 99, wave bullet | `3b69f041` |
| `plans/round-99.md` (plan + pre-file amendments A1–A9), frozen `claims.json`, `claim-falsification.tsv`, regenerated C2 receipt and two-leg probe receipt, pre-file gate control receipt, C2 measurement runner, round-99 SCORECARD/LOG entries, lesson M99-3/M99-4, QUALITY 172 | Round 99, pre-file bullet | `0e8f39f5` |

## Before → after measurements

**C1 — coverage.** Counting command (full pinned argv in `claims.json` /
`.ufo/waves/round-99/claims-declaration-r99.md` §Freeze):

```
python3 -I quality/counters/c1-r99-launchenv.py --repo . --rev 56a9b2992f1bcd1a1752f77b5b8ce8c4bc8634ea \
  --base-rev 2cbaa141f42df9dfeee4d207cae6558a4dd59863 --cases .ufo/waves/round-99/controls/launchenv-cases-r99.json \
  --expect-cases-sha256 14b4cc57…82acd --mutants .ufo/waves/round-99/controls/launchenv-mutants-r99.json \
  --expect-mutants-sha256 57b11e14…85e36 --genseed .ufo/waves/round-99/controls/launchenv-fresh-r99.py \
  --expect-genseed-sha256 50126423…e6dbf --expect-tool-sha256 a63c20c8…23eb16 \
  --expect-execargv-sha256 49f7fecd…5f713 --expect-gio-sha256 d2164260…cfc462 --scratch-root DIR
```

- **Before (at `2cbaa141`):** `SETUP_ERROR … tools/mado-launchenv.py absent at 2cbaa141` (exit 2;
  `receipts/c1-at-base-r99.txt`).
- **After (measured at `56a9b299`, ver `56a9b2992f1bcd1a1752f77b5b8ce8c4bc8634ea`):** `TARGET_MET
  pred=PRED-C1-r99-v1` — cases 67/67, classes 31/31, mutants 69/69 killed (class_kills 31/31,
  crashed 0, survived 0), fresh 60/60 at seed `7d00c2c940ceb88e`, control_naive 1/67,
  control_held_r98 4/67 (`receipts/c1-measured-r99.txt`).

**C2 — operability.** Counting command:

```
python3 -I quality/counters/c2-r99-harm-watch.py --repo . --rev 3b69f04113a235aace713bc1c84ea2b695606b6a \
  --base-rev 2cbaa141f42df9dfeee4d207cae6558a4dd59863 --panel .ufo/waves/round-99/controls/harm-panel-r99.json \
  --expect-panel-sha256 160763ce…1dae39a --planted-dir .ufo/waves/round-99/controls/harm-planted \
  --expect-gate-sha256 37a0544b…4165b9 --scratch-root DIR
```

- **Before (at `2cbaa141`):** `SETUP_ERROR … quality/harm-watch.py absent at 2cbaa141` (exit 2;
  `receipts/c2-at-base-r99.txt`).
- **After (measured at `3b69f041`; attempt-4 re-derivation):** `MADO_HARM_WATCH: TARGET_MISSED
  pred=PRED-C2-r99-v1` — panel_legs 28/28, legs_run 28, **mismatches 2**: `r92_gate_defects` and
  `r97c1_filetype` hit the panel's frozen 600 s per-leg cap (`rc=124`,
  `timeout-after-600s`) under fleet load; all five planted panels are caught, the marker-blind gate
  is flagged, the stub is flagged, the counter selftest is 17/0. The frozen `mismatches == 0`
  conjunct is unmet → **TARGET_MISSED (honest stop, `plans/round-99.md` A9)**: the target is not
  narrowed after landing; the panel-timeout repair is routed to round 100. The attempt-3
  `TARGET_MET` line left no receipt; this re-derivation is the reported value. The two-leg probe at
  a short scratch root reproduces both timeouts (`receipts/c2-probe-r99.txt`), and it rules out the
  full run's `r97c1_filetype` `rc=2` (the fresh generator's AF_UNIX path-length failure under the
  long scratch root).

## Sources & frontier

- **Counting command:** `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin mado`
  → start rc 0, 466 rows (`receipts/census-start-r99.txt`); end rc 0, 469 rows
  (`receipts/census-end-r99.txt`). Read-back gate: `rows=469 entries=120 findings=0`
  (`receipts/readback-r99.txt`).
- **Rows added by tier:** 3 tier-A rows — S532 (`gio-tool-launch.c`), S533 (`gutils.c`), S534
  (Desktop Entry Specification recognised keys).
- **Rows touched old→new:** `used-by` cells on S504, S506, S528, S529 and S531 (the new entry's
  citations and the read-back R4 acknowledgement).
- **Frontier rows advanced:** `corpus/README.md` index row for `knowledge/gio-launch-env-r99.md`
  and the Frontier paragraph moving the launch spawn environment into core. Sourced claim: C1
  (S532/S533/S534, all opened 2026-11-07 with located quotes in `corpus/lessons/round-99.md`).
- **Assimilation: none.** `/home/vgpnk/Projects/shokuknow/merge/mado/MERGE-REPORT.md` holds no
  entry on the launch/terminal/`Exec` plane (the closest staged entry, the systemd unit fragment
  plane, is out of province for this surface); no row was appended. `considerthese/`: no
  still-unimplemented proposal matched this round's surface.

## Trend verdicts

- **expansion — improved.** A new composite surface (the launch spawn environment) lands with a
  capability row, a knowledge entry and three registry rows; the lane can now answer what
  surrounds a launch argv, which no lane tool did before (`SETUP_ERROR` at the base).
- **quality — improved.** C1 is 67/67 over 31 classes with 69/69 mutants killed, fresh 60/60, both
  controls behind; C2's gate is a 28-leg frozen panel with five planted controls, a marker-blind
  forgery and a stub refused, and its claim files as an honest stop (26/28 legs at the frozen cap)
  rather than a borrowed green. QUALITY 170–172 and lesson M99-1..M99-4 encode the round's defects.
- **discernment — improved.** The wave's attack seats falsified three claim sentences (A1, A3/A4,
  A5/A6) and the round narrowed them before filing instead of filing the wider sentence; the
  attempt-4 re-derivation then caught the C2 number failure (two timeouts at the frozen cap) and
  the round reports the miss instead of reusing the unrecorded attempt-3 `TARGET_MET`. This is the
  Amendment-59 defect class caught in the lane that would have filed it.

## SHONEN

- `[~]` SKILL.md contains real decision tables, error patterns, checklists, cited sources —
  `SKILL.md:2983-2986` (four r99 rows) and `:3015-3034` (usage/decision prose); non-author verifier
  not yet recorded for promotion.
- `[~]` At least one end-to-end domain task executed and logged in LOG.md — this round executes
  the launch-environment task end to end; `LOG.md` Round 99 entry and `receipts/c1-measured-r99.txt`.
- `[~]` Instructions executable by an agent without oral context — `SKILL.md:2983-2986` carry the
  exact commands, exit codes and selftests; `claims.json` carries the pinned counting argv.
- `[~]` No cross-domain bleed (PROVINCE.md still accurate) — connector sweep over all 20 sibling
  lanes finds the C1/C2 surfaces uncontested (`receipts/connector-sweep-r99.txt`,
  `w1/R99MConnector.md`); PROVINCE round-99 refinements are read-only within province.

## Pre-file falsification gate

```
PREFILE-FALSIFICATION: pass claims=2 rows=8 attack_seats=6 findings=0
```

Skeleton `claim-falsification.tsv`: 8 rows, 2 claims, all 6 attack seats read
(`R99MConnector`, `R99MReviewC1`, `R99MReviewRecords`, `R99MCriticC2`, `R99MMutC1`,
`R99MMutC2`); the control with one seat row removed prints `FINDING attack-seat-unread`
(`receipts/prefile-control-r99.txt`).

## Round shape, inherited state, tooling

- **Round shape:** one v1 wave `w1` of 12 seats (1 scout, 1 scribe, 1 connector, 4 executors,
  2 reviewers, 1 critic, 2 mutation-testers; attack 6/12 = 50 %). No residual call. No dead seats.
  Round total 12. The planner seat is the L1 (the validator rejects `planner`); the bounded
  planning data-walk rode the scout and the records reviewer.
- **Inherited state (attempts 1–3 ended `lane-dead-no-report`):** reused after re-verification —
  the way the wave results and seat reports were read back into this attempt, the frozen
  declaration, `c1-measured-r99`/`c1-at-base-r99`/`c2-at-base-r99`/`census-*`/`readback-r99`
  receipts. Re-computed: the C2 measured receipt (the declaration cited
  `receipts/c2-measured-r99.txt`, which did not exist at attempt-4 start — regenerated at the
  pinned rev; the re-derivation failed at the frozen per-leg cap, so its own `TARGET_MET` line is
  not reused and the round reports `TARGET_MISSED`, A9). Discarded: nothing. New this attempt:
  `plans/round-99.md`, `claims.json`, `claim-falsification.tsv`, the C2 full-panel and two-leg
  probe receipts, the round-99 SCORECARD/LOG records, lesson M99-3/M99-4, QUALITY 172.
- **Stale-lane:** respawn-per-round driver; no other mission of this lane is open.
- **Tooling:** no tool installed or upgraded; no pacman transaction. Used `python3` (stdlib), `git`
  read-only, the lane's own counters and `jj-lane.sh`/`fleet-commit.sh` for landing.
