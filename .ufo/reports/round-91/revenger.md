# revenger — round 91 (hyaku run 15, attempt 1)

Lane `revenger-shokunin` (branch `main`), fleet root `/home/vgpnk/Projects/shokunin`.
Base `f6356ffb8b665bddc5ee2cfac81443c1300b59bf`; freeze
`b13aac756ac33aa5245c13966c624de4370206d0`; wave evidence
`d509e982844d31bd26f3cb96e1a663e7d36f2ca8`; landing
`d3f4e6cfd393824705633dc60a44f0cde7f47681`; receipts commit
`c517dba09e4bce3fce6072deea9aeaffa22c0236`; **final pushed lane tip
`ed2d9f14fc07d23511b8ee9743b227287f5a8f0f`** (`git ls-remote origin
refs/heads/main` printed it before this report was committed).

**Round verdict: honest stop — not admitted.** C1 is met on its frozen counter but
that counter is reachable by a skip-work control (critic-reproduced); C2 is **not
verified** because its frozen probe is reachable by three stubs. Both defects are
self-ruled, both hardened successors landed unclaimed, and the work is real and
pushed. Details below; the operator rules.

## Work performed

Two claims were frozen before any build seat ran (`reports/round-91/claims.md`):

- **C1 — calibration:** make the lane's self-assessment gate read the K statement
  **where the lane states it** (the stated before→after cell of its own SCORECARD
  row) instead of the last token-adjacent `N/D` anywhere on the line — the r90
  critic's pointer-cell defect. Target `SM6_MISCLASS=0/22`, `MUTANTS_KILLED=11/11`,
  impl self-test exit 0, `REAL_SELF_MISMATCH=0`.
- **C2 — operability, capability acquisition:** the lane can measure
  commit-message↔tree conformance over its own history. Target
  `CAP_MESSAGE_TREE=pass`.

Work items, each with its evidence:

- **Frozen instruments** (`reports/round-91/`, at `b13aac7`): `claims.md` (predicates,
  kill rules, controls), `sm6_battery_v3.py` (21 hand-labelled cases, 9 in the lane's
  own table-row format), `mutants.py` (11 rule mutants, each with the case that must
  kill it), `c1_counter.py`, `cap_probe.py`, and three red-before logs.
- **Red before:** v2 `SM6_MISCLASS=5/22`, all five in real-format cases R03–R06/R08
  (`reports/round-91/c1-red-v2.log`); v1 `11/22` (`c1-red-v1.log`); C2 instrument
  absent `CAP_PRESENT=0` (`c2-red-absent.log`).
- **C1 implementation:** `corpus/self_assessment_check3.py` (executor seat
  `ExecR91Sm6V3`), SM1–SM5 byte-identical to v2, four new real-format self-test legs.
  v2 bytes untouched (`git diff b13aac7..d3f4e6c -- corpus/self_assessment_check2.py`
  empty).
- **C2 implementation:** `reports/round-91/message_tree_check.py` (`ExecR91MsgTree`),
  per-commit and summary lines, planted-miss self-test, `--json`.
- **Real-history measurement:** `MESSAGE_TREE commits=23 cited=25 misses=9`, one
  genuine mismatch and eight ambiguous bare names, each proved by a read-only command
  (`.ufo/waves/round-91/w1/ExecR91RealRun/real-run-table.md`). The one genuine
  mismatch is **this round's own** wave-evidence commit `d509e98`, which cites
  `ufo-wave-policy.json` — a fleet-root script that is not in the lane tree.
- **Independent held-out check (unclaimed):** 22 fresh real-format cases, labels
  hand-derived and scored against the frozen rule before v3 was scored — v3 0/22,
  v2 5/22 (`.ufo/waves/round-91/w1/ReviewerR91C1.md`).
- **Battery cross-check:** 21/21 labels re-derived as forced, `reference` 0/21, all 11
  frozen mutants killed, no docstring kill-case wrong; **eight rule elements have no
  discriminating case** (`ExecR91BatteryX.md`).
- **Implementation mutation (unclaimed):** 17 attributed mutants of the v3 bytes,
  11 killed / 6 survived (`MutR91Sm6.md`).
- **Attacks:** `CriticR91Claims` reproduced **a 21-entry lookup table that passes the
  frozen C1 counter without reading the stated cell** (`receipts/c1-fit-hardcoded.log`)
  and **three C2 stubs that pass the frozen probe** — `stubD` (no tree or filesystem
  lookup), `stubE` (worktree-only), `stubA` (`receipts/probe-stubD.log`, `probe-stubE.log`).
  `ReviewerR91C2` adds `C2_DISAGREE=6/13` including the freeze inconsistency: the
  frozen description says "backticked" paths, the range has 0 backticks and 8 `.log`
  tokens, so a spec-faithful reading cites 8 and cannot reach probe leg 4's `cited>=20`.
- **Scope audit:** `SentinelR91Scope` ran 24 checks (22 pass, 2 disclosures, 0
  violations); frozen artefacts byte-unchanged at its snapshot; no protected path, no
  credential shape, no sibling-repo write.
- **Surface map:** `ScoutR91Surfaces` named 9 edit sites in 4 files; all were applied.
- **Sibling overlap:** `ConnectorR91Overlap` — no sibling lane holds a
  message↔tree instrument; the closest are receipt/orphan sweeps over registry rows,
  not commit messages.
- **Hardened successors (unclaimed, post-freeze):** `reports/round-91/c1_counter2.py`
  (adds 40 run-time-generated cases; landed v3 `RANDOM_MISCLASS=0/40`, the fitted
  lookup table **18/40**) and `reports/round-91/cap_probe2.py` (random absent path, a
  worktree-vs-tree leg, `commits` and exit-code cross-checks; landed instrument pass,
  stubA/stubD/stubE all fail). Receipts: `reports/round-91/after-successors.log`.
- **Frontier step:** three sources opened this round and admitted as S488–S490
  (git-log `%B`, `git cat-file -e`, Conventional Commits), with the fetched text kept
  as the receipt; one mistake mined in the lesson plus the two counter defects; the
  `considerthese/2026-11-04.md` proposal 4 is C2's ground.
- **Assimilation:** none — the `merge/revenger/` package's 155 staged ids collide
  155/155 with the lane registry (mass id drift); nothing adopted, L0 question
  appended.

## Landed changes

Every change is tied to the `LOG.md` round-91 entry (`LOG.md`, "## Round 91") and to
landing commit `d3f4e6cfd393824705633dc60a44f0cde7f47681` unless stated:

| change | path | note |
|---|---|---|
| SM6 v3 gate | `corpus/self_assessment_check3.py` | new; reads the stated cell; 4 real-format self-test legs |
| message↔tree instrument | `reports/round-91/message_tree_check.py` | new capability, registered as a `probe` |
| hardened successors | `reports/round-91/c1_counter2.py`, `cap_probe2.py` | unclaimed; r92 freeze candidates |
| gate registry | `SKILL.md` | two new blocks (`self_assessment_check3`, `message_tree_check`); stale "registers exactly one committed gate" sentence corrected to 17 blocks with the counting command |
| corpus index | `corpus/README.md` | v3 index line (this was the SM2 mismatch that made the first after-run 1) and the Known-gaps sentence |
| scorecard | `SCORECARD.md` | `message-tree-conformance` capability row; round-91 section with per-claim verdicts and routed-forward |
| sources | `corpus/SOURCES.md` | S488–S490 appended inside the Registry (census exit 0) |
| lesson | `corpus/lessons/round-91.md` | Gate, source table, four mistakes, final measurements |
| wave evidence | `.ufo/waves/round-91/**` | spec, dispatch, validate output, 11 seat reports, receipts, assimilation guard, L1 source fetches |
| receipts | `reports/round-91/{c1-after,after-successors,census-round-start,census-round-end}.log` | commit `c517dba` |

## Before → after measurements

| claim | counting command | before | after | verdict |
|---|---|---|---|---|
| C1 calibration | `PYTHONUTF8=1 python3 -B reports/round-91/c1_counter.py --impl corpus/self_assessment_check3.py --real <landing archive> --lane .` | `f6356ff`: v2 `SM6_MISCLASS=5/22` (`c1-red-v2.log`), v1 `11/22` | `d3f4e6c`: `SM6_MISCLASS=0/22`, `MUTANTS_KILLED=11/11`, selftest 0, `REAL_SELF_MISMATCH=0`, `C1_VERDICT=pass` (`c1-after.log`) | **MET on the frozen counter; admission contested** — a fitted lookup table also passes it (`c1-fit-hardcoded.log`). Successor: `c1_counter2.py` → v3 `pass` (0/40 random), fitted table `fail` (18/40) |
| C2 operability (capability) | `PYTHONUTF8=1 python3 -B reports/round-91/cap_probe.py --lane . --range 7fab03f..refs/heads/main` | `f6356ff`: instrument absent, `CAP_MESSAGE_TREE=fail` | `d3f4e6c`: `CAP_MESSAGE_TREE=pass`, `commits=24 cited=25 misses=9` (`c1-after.log`) | **NOT VERIFIED** — `stubD`/`stubE` also pass (`CriticR91Claims` C2-2/C2-3). Successor `cap_probe2.py`: landed instrument `pass`, stubA/stubD/stubE `fail` (`after-successors.log`) |
| coverage (no claim) | `reports/round-73/measure.py .`; `reports/round-81/f_probe4.py corpus` | `f6356ff`: `K_HELD_BACKED=8/15`, `C10_HELD_BACKED=0/1`, `F4_COVERAGE=11/11` | `d3f4e6c`: same (`holds.log`) | unchanged hold — routed on documented unreachability, reason frozen in `claims.md` |

## Sources & frontier

Census command (both runs, same command):

```sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin revenger
```

- **Before:** exit **0** (`reports/round-91/census-round-start.log`; 21 W01 + 10 W04
  warnings, 0 errors, last line `revenger ok …/corpus/SOURCES.md`). The round start
  was *not* exit 2 — the registry existed.
- **After:** exit **0** (`reports/round-91/census-round-end.log`; 0 E, same warning
  classes, last line `revenger ok …`).
- **Rows:** 487 → **490** (`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'` style
  count over the registry; the census prints `revenger ok`).
- **Rows added by tier:** 3 external docs, tier A — S488 (git-log `--format`/`%B`),
  S489 (`git cat-file -e` existence test), S490 (Conventional Commits message shape).
  Zero own-work rows, zero rejected rows this round; external additions are non-zero.
- **Rows touched old→new:** none — no existing row's `status`, `recheck` or `used-by`
  changed this round (S481/S486 supersession stands from r90).
- **Frontier rows advanced:** none. C15 (tool landscape) and C10 (evidence-ledger
  discipline) stay `uncovered`/`partial`; C03/C05/C08 unchanged. Coverage got no claim
  this round — see the reason in `claims.md` and the named next move in
  `SCORECARD.md` (r92: admit C03 from the r85 oracle-checked managed records, or C10
  with a source-opening wave).
- **Assimilation: none** — mass id collision (155/155) with `merge/revenger/`; guard
  proved able to fail (`assimilation/guard/guard-proof.log`, `indented_row_detected=1`);
  L0 question appended. `considerthese/2026-11-04.md` proposal 4 is C2's ground;
  proposals 1, 2, 3, 5 stay unimplemented.

## Trend verdicts

- **expansion: unchanged.** No `corpus/knowledge/` entry was admitted and no coverage
  row moved (`K_HELD_BACKED=8/15` both ends). Three external tier-A source rows are
  curation, not expansion (`CORPUS.md` rule 4). The new capability is repertoire, not
  corpus breadth, and its claim is not verified.
- **quality: improved.** A gate that misread the lane's own row format now reads the
  stated cell, and the fix is measured against a frozen battery, 11 frozen rule
  mutants, an independent held-out probe (v3 0/22 vs v2 5/22) and a randomized
  successor (v3 0/40, fitted control 18/40). Two probe/gate defects the round exposed
  in itself (the frozen C2 probe's stub reachability, the frozen C1 battery's
  enumerability) are closed by committed, red/green-demonstrated successors. A stale
  SKILL sentence that credited the registry with exactly one gate is corrected to a
  countable 17 blocks. No admitted entry, instrument or criterion was weakened; v1 and
  v2 checker bytes are unchanged.
- **discernment: improved.** The round refused to admit either claim on its own
  counters: C2 is self-ruled **NOT VERIFIED** and C1 is reported **contested**, both
  with the reproducing control named, rather than prettified as r90's C2 was nearly
  admitted. Two wrong numbers in the frozen claims file ("seven of nine rounds" →
  6/9; "verbatim" battery rows → truncated) were corrected in an appended erratum
  instead of being quietly restated. The cost is a third consecutive honest stop; the
  alternative was a false green.

## SHONEN

`grep -c '^## SHONEN'` = 1; one line per box of `SHONEN.md`, none `[x]` (no non-author
verifier this round).

- [~] SKILL.md decision tables / cited sources — `SKILL.md` gained two registry blocks
  and lost a stale count sentence (`SKILL.md:326-350`); still no outside confirmation
  of the current bytes (r69 spot-check V7 stands).
- [~] At least one end-to-end domain task in LOG.md — the round's end-to-end work is
  the self-assessment gate over the real tree plus the message↔tree run over 23
  commits (`reports/round-91/c1-after.log`, `ExecR91RealRun/real-run-table.md`); no REA
  producer run this round.
- [~] Instructions executable without oral context — both new instruments were run
  from their documented commands by three seats (`ExecR91Sm6V3`, `ExecR91MsgTree`,
  `ReviewerR91C1`); no independent outside instruction verifier.
- [~] No cross-domain bleed — `PROVINCE.md` byte-unchanged
  (`git diff f6356ff..d3f4e6c -- PROVINCE.md` empty); ADJ-06 stays reported, not
  absorbed; no sibling repo written (`SentinelR91Scope` checks 05–07, 20).

## Round notes

- **Shape:** one v1 wave, **13 seats**, validated under
  `scripts/hyaku/ufo-wave-policy.json` (band 8–16), dispatch
  `w1.ready` → `w1.ready.dispatched`; roles: 4 executor, 2 scribe, 1 scout,
  2 reviewer, 1 critic, 1 mutation-tester, 1 connector, 1 sentinel — **attack 4/13 =
  30.8 %**. No planner seat (the L1 holds the canonical planner seat; the validator
  rejects `planner`). No residual call. Round total **13 seats**.
- **Dead seats:** `ScribeR91Sources` and `ScribeR91Skill` settled with empty output and
  no wave artefacts (`agent://ScribeR91Sources`, `agent://ScribeR91Skill`); they were
  not replaced, and the L1 did their work (three source openings with committed fetch
  receipts, the lesson). `ExecR91Sm6V3` stalled waiting on the README-index decision;
  it was messaged the decision and finished. All other seats produced their reports.
- **Misroot sweep:** `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows no
  revenger file at the fleet root; `.scratch/*`, `after` and `kama.md` belong to other
  lanes. `.ufo/l0-questions.md` carries this round's sanctioned append.
- **Stale-lane:** no. Respawn-per-round driver; no other mission of this lane is open.
- **Tool installs:** none (no seat installed or upgraded a tool; nothing to record).
- **L0 questions:** one appended — `revenger | round-91 | Assimilation id-collision
  guard … 155/155 collide … renumber the package per lane or adopt by document`.
  Routed around, not assumed answered.
- **Earlier attempts:** none (no `lane-dead-no-report revenger round=91` line in
  `.ufo/watchdog.log`); `.ufo/waves/round-91/` was empty at round start, so nothing was
  inherited.
- **Seat routes:** never passed `model`; routes are `task.agentModelOverrides`.
  `CriticR91Claims` and the two reviewers answered; the two scribe seats produced
  nothing and their route is not asserted.
