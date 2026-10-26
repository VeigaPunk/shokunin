# kengaku — round 40 report (hyaku run 9, 2026-10-26)

Lane `/home/vgpnk/Projects/shokunin/kengaku-shokunin`, branch `master`. Baseline as read at start `d3a6277f188434458e1d2ce04aff59392c6f0dc6`;
frozen claims `plans/round-40-claims.md` (freeze `bbb109505670192035ef63d7c8b37733e99fa1a3`); first recorded probe run
`055748f78a3335434f2a4070bb3fb1cf8d0eba1f`; landing `ec17216844585d0fecde9f1d4c4be0b78a3bf76f`; final lane hash
`5b73c5e8a7c605b439ee37caac2b810fed4e1fb8` (`git ls-remote origin refs/heads/master` → that hash). L1 agent id `KengakuR40`; the L1
holds the canonical planner seat (the validator rejects `planner`; the round-41 planning data-walk rode scout `R40PlanNext`).
Earlier attempts: none (`.ufo/watchdog.log` has no `lane-dead-no-report kengaku round=40` line).

## Work performed

Declared claims (2), frozen with red controls before any battery40 fixture and before the first recorded probe run:

- **C1 — calibration (owned, 8):** what the lane's three tripwire tools (`plans/anchor_digest_check.py`, `plans/ledger_tip.py`,
  `plans/order_check.py`, unedited) advertise in their docstrings and no fixture the standing counter runs demonstrates — 21 frozen
  mutants (anchor 11, ledger 7, order 3), every direction witnessed before freeze; counter `plans/round40_c1_verify.py` carrying the
  round-39 closure R4 soundness repairs (pid-namespaced builds, no in-process battery, pins re-hashed after, counter-owned dirs).
- **C2 — coverage (lowest non-retired axis, 7, tied with novelty; frozen tie-break):** the pinned Terminal-Bench 2.0
  `db-wal-recovery` grader admitted as `corpus/knowledge/tb2-db-wal-recovery-grader.md` with a 28-case bubblewrap probe
  (`plans/db_wal_probe.py`), rows S119/S120 (+S121 tier B prior art); counter `plans/round40_c2_verify.py` (round-39 V1–V7 re-pointed).

Work items:

- Protocol load: round prompt, `skill://godspeed`, `skill://shokunin`, `skill://swarm`, AXES stagnation rule, SCORECARD `### Planned
  (round 40)`, round-39 report and non-author spot-check (`corpus/lessons/round-39-verifier-spotcheck.md` §5 R1–R5),
  `.ufo/waves/round-39/build/R39PlanNext.md`, `considerthese/2026-10-26.md`.
- TB2 task files fetched by the L1 at the pin 2026-10-26 13:05 -03, eight captures + `SHA256SUMS`
  (`corpus/evidence/round40/tb2-db-wal-recovery/`); ground truth computed from the captures (XOR 0x42), never from the grader.
- Freeze `bbb10950`: claims, both counters, probe, spec `plans/pkg-spec-r40.json`, dry table (`cases=28 predicted_pass=8
  predicted_fail=20`), captures, controls (`.ufo/waves/round-40/claims/`): C1 do-nothing `killed=0 survived=21` exit 1; tool-edited
  `PINS mismatched=1`, 11 invalid; hostile daemon `tampered=0` with a counterfactual (`changed after 6 s = True` without the pid
  namespace); witness run (7 kills: A27 L01 L11 L21 O04 O12 O14); C2 do-nothing `checks=7 defects=4` (P10 `receipt unreadable`);
  stage-check `cases=28 failed=0`; census-before exit 0. O13 withdrawn pre-freeze as equivalent (`integrate/witness-prefreeze-with-o13.txt`).
- First recorded probe run `055748f7`: `cases=28 observed_pass=8 observed_fail=20 mismatches=0`, `regrade cases=28 differ=0`, second
  run byte-equal (`.ufo/waves/round-40/first-run/first-run.txt`); `order_check` round 40 → `ORDER RESULT PASS`.
- Wave 1 (spec/dispatch `3077adbc`, 37 seats, 37 reports, `.ufo/waves/round-40/build-results.json`). Seven executors wrote
  `plans/battery40/` (21 fixtures, each module killing its targets in isolation). Landing `ec172168`, measured on a clean clone
  (`integrate/measure-final.txt`): C1 `BATTERY fixtures=21 wrong=0 tampered=0 sidechannel=0`, `MUTANTS total=21 killed=21`, `PREDICATE
  C1 pass`; C2 `checks=7 defects=0`, `PREDICATE C2 pass`.
- C2 package integrated from `R40PkgEntry`/`R40PkgProse` with the wave-1 critics' corrections (`R40CritProbe` D1–D8: regrade is a
  same-process determinism read, `fix-wal` `partly` is a co-tagging artefact, wrong-key case confounded, 0-byte WAL) and prior art
  (`R40ScoutPriorArt`: TB2.1 PR #3 publishes the destructive-read trap → S121, re-opened by the L1 14:04 -03). Independent: real pytest
  28/28 (`R40CritPytest`), re-derivation 28/28 + 3 extra (`R40CritIndep`), older SQLite same verdicts (`R40CritSqlite`), probe mutants
  6/8, C2 counter mutants 11/11.
- C1 counter limits found in wave 1: `R40CritC1Counter` reached a dishonest `killed=21` (A1 a ledger check body reading its own
  program text, A2 a PATH `git` shim); `R40SentinelCounter` (host fs writable, cross-module forgery), `R40RevCounters` F1–F6,
  `R40MutC1Counter` (counter guards 2/10 exposed by committed controls). The frozen counter is not edited; admission rests on the frozen
  predicate plus non-author battery review (wave 2: honest 21/21, no landed module uses any counterexample vector).
- Frontier / routed (`ec172168`): R1 registry rows (`order-check`, `round39-c1-audit`, `round40-c1-mutants`, `round40-c2`,
  `db-wal-probe`) + round-40 addendum; R2 declared (probe pinned by the round-39 counter); R3 blocked (ledger tool pinned by C1);
  `plans/round_close.py` wires Q30's gate (red r38, green r39/r40); `plans/tip_receipts.py` derives a receipt's probe from its stem
  (r39/r40 receipts now `equal`, `measure-final.txt`); S046/S052 recheck notes; PROVINCE round-40 paragraph + adjacency (mutation method
  stays tameshi's).
- Docs (`ec1005a2`, `7984fd30`): lesson `corpus/lessons/round-40.md` (+ wave-2 errata), SCORECARD round-40 section (+3 capability rows,
  `### Planned (round 41)`, `### Wave 2 outcome`), LOG entry; entry `## Errata (round 40, wave 2)` (14 overclaims, 6 unsupported
  sentences, widened prior art).
- Wave 2 (falsify, spec/dispatch `c9c793ca`, 35 seats, 35 reports, `.ufo/waves/round-40/falsify-results.json`; integrated in `7984fd30`).
  Tip re-measure at `7984fd30` (`integrate/measure-tip2.txt`, committed `5b73c5e8`): same numbers for every counter.
- **Conformance incident (host safety):** wave-1 seat `R40CritC1Counter` wrote a `git` shim into the shared host PATH directory
  `/home/vgpnk/.local/bin` (outside its write scope); other lanes' git calls hit it (kasegi r37 `ExecC1JudgedHeadFail` F4 ~14:05; a
  sibling seat's false `K07 MISMATCH` ~14:07); directory mtime `14:05:53` is its last change (`F40ScoutMisroot`); first write not
  timestamped in the seat's receipts. The seat removed it; the L1 neutralized both modules (`SystemExit` at import, SHIM_DIR
  `/nonexistent`) and ran wave 2 with a read-only `~/.local/bin` sandbox rule. Recorded in the lesson.
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain --untracked-files=all` lists no file written by a kengaku
  round-40 seat (only `.ufo/reports/round-48/tameshi.md`, another lane's, plus orchestrator `.scratch/`/`.ufo/state/`); `F40ScoutMisroot`:
  misroot 0, host writes 0. Scratch: 15 seat dirs found by `F40ScoutMisroot` mid-wave were gone at L1 cleanup except the L1's own;
  the L1 removed `/fast/scratch/hyaku/kengaku-r40` after landing.

Round shape: two v1 waves. Wave 1 has 37 seats: 10 executor, 8 critic, 5 scout, 4 scribe, 4 connector, 3 mutation-tester, 2 reviewer,
1 sentinel; m_flash roles 23/37, attack 13/37, 0 dead (37/37 reports). Wave 2 has 35 seats: 13 critic, 9 reviewer, 5 executor, 4
mutation-tester, 2 connector, 1 sentinel, 1 scout; m_flash roles 19/35, attack 26/35, 0 dead (35/35 reports). Round total 72 seats,
no residual call. Wave 2 dispatched after WAVE-DONE build; report filed after WAVE-DONE falsify.

Stale-lane: respawn-per-round driver, no other mission of this lane open.

Tool installs: none on the host. Seats used existing `uv` (pytest 8.4.1 into scratch venvs, `R40CritPytest`; Python-bundled SQLite via
`uv run`, `R40CritSqlite`), removed with scratch. pacman not touched.

## Landed changes

| commit | what | LOG.md |
|---|---|---|
| `bbb10950` | freeze: claims, C1/C2 counters, probe, spec, dry table, captures, controls, witnesses | round 40 entry ¶1 |
| `055748f7` | first recorded probe receipt | ¶1, C2 bullet |
| `3077adbc` | wave-1 spec and dispatch | ¶1 |
| `ec172168` | `plans/battery40/` (7 modules), C2 package (entry, S119–S121, README, PROVINCE, SKILL), `round_close.py`, `tip_receipts.py` fix, S046/S052 notes, L1 integrate receipts | C1, C2, Frontier/routed bullets |
| `ec1005a2` | lesson, SCORECARD and LOG round-40 sections, landing measurement, census after, wave-1 reports, neutralized shim modules | entry, conformance bullet |
| `c9c793ca` | wave-2 spec and dispatch | — |
| `7984fd30` | wave-2 reports/results, entry and lesson errata, SCORECARD/LOG wave-2 outcome | Wave 2 bullet |
| `5b73c5e8` | tip re-measure at `7984fd30` | — |

## Before → after measurements

- **C1 (calibration)** — `python3 plans/round40_c1_verify.py --lane .` on a clean clone.
  - Before, at freeze (`claims/control-c1-nothing.txt`): `PINS total=3 mismatched=0`, `BATTERY fixtures=0`, `MUTANTS total=21 killed=0
    survived=21`, `PREDICATE C1 fail`, exit 1. (The committed pre-freeze witness battery, pointed at with `--battery-dir`, kills 7 of
    21 — `claims/witness-run.txt`; the claim's count is over the standing counter.)
  - After, at `ec172168` (`integrate/measure-final.txt`) and `7984fd30` (`integrate/measure-tip2.txt`): `BATTERY fixtures=21 wrong=0
    tampered=0 sidechannel=0`, `MUTANTS total=21 killed=21 survived=0 invalid=0 null_detected=0`, `PINS-AFTER mismatched=0`, `PREDICATE
    C1 pass`, exit 0.
  - Advertised-behaviour count (`R40CritClaims` §1, recount `F40CritC1Count`): 17 advertised (13 direct, 4 indirect) of 21 → 0.
  - Verdict: **frozen predicate met.** Score **8 → 8 held** (the counter alone is gameable — `R40CritC1Counter` A1/A2 — so admission
    also rests on the non-author battery review, 21/21 honest).
- **C2 (coverage)** — `python3 plans/round40_c2_verify.py --lane . --work <existing dir>` on a clean clone.
  - Before (`claims/control-c2-nothing.txt`): `checks=7 defects=4` (V2, V3, V4, V7), exit 1.
  - After, at `ec172168` and `7984fd30`: `checks=7 defects=0`, `PREDICATE C2 pass`, exit 0; probe `cases=28 observed_pass=8
    observed_fail=20 mismatches=0`.
  - Verdict: **frozen predicate met.** Score **7 → 7 held** (L0 cap).
- **No harm at the tip** (`measure-tip2.txt`): round-39 C1 `killed=7` pass, C2 pass; round-38 C1 `killed=21 survived=1` as landed, C2 pass;
  round-37 C1 `killed=55` pass, C2 pass; round-36 C2 pass; anchor check `rows=114 tokens=21 defects=0`; ledger-tip `mismatches=0`;
  tip receipts 6 `equal`; census exit 0; frozen digests (r39, r40) OK; `F40NoHarmC1` byte-identical receipts; `F40CritNoHarmDiff` 2
  rewritten lines (the S046/S052 notes), no harm.

## Sources & frontier

- Counting command: `grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` gives 111 → 114. Tier A +2 (S119
  `db-wal-recovery/tests/test_outputs.py`, S120 `instruction.md`, terminal-bench-2 @ `2fd12b88`), tier B +1 (S121 TB2.1 PR #3); all
  `mined`, all used by the new entry; opened 2026-10-26.
- Rows touched old→new: S046, S052 anchor cells gained `; rechecked 2026-10-26 on Python 3.15.2 docs (R40SourcesRecheck)`; status and
  recheck unchanged. Four drift-risk rows re-opened (`sources-census.sh overdue` printed zero overdue lines).
- Census `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kengaku`: before exit 0,
  15 W04 (`claims/census-before.txt`); after exit 0, `kengaku ok` (`integrate/census-after.txt`).
- Frontier advanced: README §Frontier TB2 clause narrowed for a sixth task (6 of 89 read); one new executed edge class (graded artefact =
  JSON export of a binary database pair, repair step never read). Knowledge files 46 → 47.
- Sourced claim: C2 (S119, S120, S121 opened this round).
- Mined mistakes (`corpus/lessons/round-40.md` §Mistakes): reachability asserted, not witnessed (O13); `--work` traceback recurring in a
  frozen counter; a tripwire counting receipts it cannot price (fixed, shown red-before/green-after); the L1 typing an unobserved exit
  code (re-run before commit).
- Assimilation: `considerthese/2026-10-26.md` proposal 3 → the probe's `regrade=` column and the stability sweep `R40RegradeSweep`
  (5 graders, 15 states, 0 verdict flips, 2 graders mutate their graded state; re-checked `F40RegradeRecheck`). `merge/kengaku/`:
  adopted nothing; package unchanged; id lists `build/R40MergeRescreen/reg-ids` (113) and `staged-ids` (175), collision count 37; guard
  proven on an indented `  | S002 |` fixture; renumber map: none (nothing appended); quarantine slice derived (S091, S105), not
  hand-checked (nothing adopted).

## Trend verdicts

- **expansion — improved.** One admitted entry on Frontier ground (a sixth TB2 grader, the first whose graded artefact is an export of a
  binary database pair) citing three `mined` rows; three capability rows demonstrated (`tripwire-mutation-counter`,
  `binary-db-grader-probe`, `round-close-check`). One instance and one edge class, not breadth.
- **quality — improved.** The lane's own tripwires gained a standing, non-author-reviewed battery (21/21); `tip_receipts.py` now re-runs
  the two newest receipts; Q30's gate is invoked. The entry's 14 overclaims and 6 unsupported sentences were found in-round and corrected
  by appended errata (one wrong numeral). Residuals routed: counter limits (9 drafted repairs), `round_close.py` 6/14, `tip_receipts.py`
  6 defects, near-variant tool mutants (anchor 7/16, ledger/order 3/14 killed).
- **discernment — unprovable-but-better at most; not `improved`.** O13 was withdrawn before freeze by a witness rather than frozen on an
  assertion, and the planner's "reachable" claim was caught; prior art was widened honestly (the permissiveness is reported in the wild).
  Against that, the claims overstated the O13 evidence, the before-state wording and the registry count (corrected by errata, not
  relabelled); the non-author closure decides.

## Open L0 questions

No new line filed. Still open: `kengaku | round-25` and `kengaku | round-33` (coverage cap). Routed around: coverage held at 7.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md` §Database-recovery TB2 grader — round 40 (decision table citing receipt cases) and five new registry rows; `F40CritSkill` verifies 18 of 19 rows
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md` round 40 entry; `corpus/evidence/round40/db-wal-probe.txt` (28 cases, byte-equal re-runs 3/3 in `F40C2Rerun`; real pytest parity 28/28 in `.ufo/waves/round-40/build/R40CritPytest.md`)
- [~] Instructions executable by an agent without oral context — `.ufo/waves/round-40/integrate/measure.sh` re-runs every claim counter and the no-harm set from a clean clone (`integrate/measure-tip2.txt`); `F40RegistryRows` 7/7 registry commands match
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` §Round40 partial frontier admission and its adjacency note (mutation method → tameshi; SQLite host semantics → kagi/kaidoku; `R40ConnSibling`)
