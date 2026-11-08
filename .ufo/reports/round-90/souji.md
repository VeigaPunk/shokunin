# souji round 90 — report

Lane `souji-shokunin` (id `souji`). Lane base `bd760432df2cc3ba6c5f1ccc540b050fe2ac09e2` (r89 closed); round tip
`93c7e6dc07f71cfe9c81d5db40c91a217c535ac0` pushed to `refs/heads/master` (`git ls-remote origin` prints it).
Report round 90, attempt 1. Frozen preregistration `fd25bfc5`; instruments P1 `1952c1c7`, P2 `e2a11c73`; C2 repair
`4cb3a06f`.

## Work performed

The round declares two claims. **C1 (axis calibration 7, the lane's lowest owned non-retired axis):** the r89
sixteen-member mutant set's sole surviving clause — the `_ledger` `len(r) < 3` malformed-row guard, dropped by
`m17c-no-malformed` — is bound by one new population row, `LD2b`, which appends the 2-column ledger row
`ZZ9<TAB>ABSENT` under an id absent from the frozen r77 ledger, so the length guard rather than the duplicate leg is
the only refusal left. **C2 (axis operability 8):** the K4 FLAGFAIL detail spells the raw byte `0x85` as `\x85` and
the CHARACTER U+0085 (NEL) as `\u0085`, so the byte/character pair the r89 repair left colliding is no longer one
cell, and the dead escape-first helper `_one_line` (zero callers) is deleted. Both after-states are re-derived by
non-author seats and by the L1 from committed bytes.

Work items, each with its evidence pointer:

- **The C1 population and harness extension.** `census/round-90/c1-false-rows.tsv` (58 rows, sha
  `d64d7695…`) is `census/round-89/c1-false-rows.tsv` byte-for-byte plus the `LD2b` line; the harness copy gains the
  `LD2b` append branch and the population pin (`census/round-90/c1-false-row-harness.py`, sha `c3664747…`), the
  battery gains the r90 PINS entry (`census/round-90/c1-clause-battery.py`, sha `e7265335…`), and the mutants file
  carries the same sixteen members (sha `39252248…`). Evidence: `census/round-90/records/prefreeze-c1-control.txt`,
  `census/round-90/records/c1-after.txt`; seat reproductions `S90ExecC1`, `S90ExecC3`, `S90MutCounter`,
  `S90Reviewer`, `S90Reviewer2`.
- **The C2 repair.** `tools/souji-record-agreement.py` at `4cb3a06f` (sha `d095b52f…`): the `o == 0x85` branch is
  removed from the C0 arm, U+0085 joins U+2028/U+2029 on the `\uNNNN` arm, and the dead `_one_line` is deleted.
  Evidence: `census/round-90/records/c2-after.txt` (12/12 vs 10/10, EXIT 0), `prefreeze-c2-control.txt` (10/10,
  EXIT 1), `prefreeze-c2-k4-regression.txt` (rows=12 mismatches=0), and the seat re-runs `S90ExecC2`, `S90Sentinel`,
  `S90Critic`, `S90Labrat`.
- **The r90 fixture.** `tests/fixtures/r90-k4-flagfail.py` (sha `d4417213…`, 12 cases): the ten r89 cases are
  unchanged; KFF9 (nelchar) and KFF10 (nelbyte) are added and bound to an injectivity pair check that now runs on
  both arms (plans/round-90.md A0.1). Evidence: `S90ExecC2` §AST comparison, `S90ExecC3` §5 inventory.
- **The source and corpus work.** S353 admitted (Unicode UAX #14, Unicode 18.0.0 rev 57, NL class for U+0085);
  UAX #13 opened and rejected as a tombstone; `corpus/knowledge/nel-byte-character-pair.md` added; QUALITY Q165
  added; `corpus/README.md` gains the r87–r90 frontier rows the r89 spot-check routed; `corpus/lessons/round-90.md`
  records the Gate, three mistakes and the wave findings. Evidence: `census/round-90/srcs/tr14.html` (sha
  `296df533…`), `census/round-90/srcs/tr13.html` (sha `bfa7f97b…`), `census/round-90/records/sources-census-before.txt`,
  `sources-census-after.txt`; `S90ScoutSources`, `S90Scribe`, `S90Reviewer`.
- **The wave.** One v1 wave, 12 seats (`w1`), dispatched from
  `.ufo/waves/round-90/w1-dispatch.json` via `.ufo/waves/round-90/w1.ready` (the orchestrator spawned it at
  11:47:09 -03: `spawned souji 90 w1 12`). Roles: 3 executor, 2 reviewer, critic, mutation-tester, sentinel,
  connector, scout, scribe, and the labrat duty on a revenger-role seat (the validator refuses `labrat` as a swarm
  role); the L1 holds the canonical planner seat. Attack share 7/12 = 58 % (≥25 %), connector 1 (≤2), residual 0,
  dead seats 0. Every seat report and receipt is committed under `.ufo/waves/round-90/w1/` (134 files in the pushed
  tree, verified with `git ls-tree -r master -- .ufo/waves/round-90 | wc -l`), fixing the r89 durability defect.
- **Settlement lag (disclosed).** The wave spawned at 11:47:09 -03; the driver wrote no `w1-results.json` and sent
  no `WAVE-DONE` for ~29 minutes although all twelve reports existed by 12:07 (three were still being finalised), so the L1 wrote a provisional record
  from the dispatch list and the reports with `_source: l1-constructed` (plans/round-90.md A0.7; L0 line appended)
  and kept working; the seats then finalised three reports at 12:13–12:14 and the driver wrote its own record, which
  the WAVE-DONE handoff at 12:16 -03 named and which superseded the provisional one. All 12 seats settled; the
  final wave bytes (including the Scribe's post-commit finalisation and the deletion of its throwaway scaffold) are
  committed at `47bd575b`, and no seat output is invented.
- **Misroot sweep.** `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows no untracked file naming
  `souji`/`round-90`; the only entries are other lanes' reports and orchestrator state. No fleet-root write to
  repair.

## Landed changes

Each change cites the commit that carries it and its LOG.md entry (LOG.md `## Round 90`).

| change | commit | LOG.md |
|---|---|---|
| instruments P1: population, harness, battery, mutants, r90 fixture, before-tool control, S353 captures, C2 pre-freeze receipts | `1952c1c7` | `## Round 90` (Claims, Measured, Sources) |
| instruments P2: C1 do-nothing control receipt on the r89 population | `e2a11c73` | `## Round 90` (Measured) |
| C2 repair: U+0085 `\u0085` spelling; dead `_one_line` deleted | `4cb3a06f` | `## Round 90` (Claims, Measured) |
| freeze F: `census/round-90/preregistration.txt` alone | `fd25bfc5` | `## Round 90` (Claims) |
| round integration: C1/C2 after receipts, S353 row + entry, Q165, README frontier rows, lesson, plan, SCORECARD r90 rows and capability rows, LOG entry, wave evidence (12 seat reports + receipts + results + ledger) | `8eba0131` | `## Round 90` (all) |
| after-census receipt (275 rows, EXIT 0) | `a711c357` | `## Round 90` (Sources) |
| final wave bytes after WAVE-DONE: the driver's `w1-results.json`, the three seats that finalised at 12:13–12:14, the Scribe's scaffold deletion, and the A1 durable-reproducer pointer | `47bd575b` | `## Round 90` (Wave) |
| `plans/round-90.md` A0.7 settlement outcome (driver record superseded the provisional one at 12:16) | `93c7e6dc` | `## Round 90` (Wave) |

`census/round-90/claims.json` is tied to the same LOG entry (`## Round 90` → Claims/Measured) and to
`.ufo/waves/round-90/claim-falsification.tsv`.

## Before → after measurements

**C1 — calibration 7.** Counting command:
`python3 -B census/round-90/c1-clause-battery.py --counter census/round-87/c1-pointer-counter.py --work WORK --only r89,r90 --expect-killed 31`
(the counter is byte-identical `fd0a8e24…`; the mutant texts are unchanged).

- Before (do-nothing control, same battery and 16 mutants, the r89 57-row population alone), measured at the P2
  commit `e2a11c73`: `SUMMARY mutants=16 sets=r89 pristine_r89=ok killed_r89=15 killed_total=15`, `MUTANT-PAIR
  m17c-no-malformed pop=r89 killed=no`, EXIT 0 (`census/round-90/controls/c1-before-r89-population.txt`).
- After (F `fd25bfc5`, instruments P1/P2), measured at `8eba0131`: `ARM pristine pop=r89 rows=57 mismatches=0
  errors=0 exit=0`, `ARM pristine pop=r90 rows=58 mismatches=0 errors=0 exit=0`, `killed_r89=15 killed_r90=16
  killed_total=31`, EXIT 0 (`census/round-90/records/c1-after.txt`). The frozen target is met; the delta is `LD2b`
  and nothing else (S90ExecC1 sole-killer table; S90MutCounter §2).

**C2 — operability 8.** Counting command:
`python3 -B tests/fixtures/r90-k4-flagfail.py --tool tools/souji-record-agreement.py --before census/round-90/controls/c2-before-tool.py --work WORK`.

- Before (the r89 tool bytes as BOTH arms), committed in P1 `1952c1c7`: `SUMMARY cases=12 tool_pass=10
  before_pass=10`, KFF9 and KFF10 fail on both arms, EXIT 1 (`prefreeze-c2-control.txt`).
- After (tool `4cb3a06f`, fixture sha `d4417213…`), measured at `8eba0131`: `SUMMARY cases=12 tool_pass=12
  before_pass=10`, EXIT 0 (`census/round-90/records/c2-after.txt`); regression `SUMMARY rows=12 mismatches=0
  errors=0`, EXIT 0 (`prefreeze-c2-k4-regression.txt`); `grep -c 'def _one_line('` = 0 and the module loads.

Both claims verify under the narrowings recorded in `plans/round-90.md` A1, A4 and A5: the fixture's substring
counts do not by themselves certify the word "injective" (a doubled-backslash mutant survives 12/12, S90Sentinel
H1), a raw-window cut inside U+0085's encoding renders the surviving byte `\x85` (S90Reviewer2), the "one physical
line" clause is not enforced (S90Reviewer2), the deletion is measured by grep+load rather than by the fixture
(S90Critic), and the battery does not print its own hash (S90Critic). The tool's injectivity on the pair stands
(S90Sentinel probe6: zero collisions among 14 single characters and all 2-char strings).

## Sources & frontier

`SOURCES:`

- Counting command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin souji`;
  row count `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`.
- **Before → after:** 274 → 275 rows; census EXIT 0 both ends, W04 warnings only (`census/round-90/records/
  sources-census-before.txt`, `sources-census-after.txt`).
- **Rows added by tier:** 1 row, tier A (`docs`), status `mined`: **S353** (Unicode UAX #14, Unicode 18.0.0 rev 57,
  NL class for U+0085; capture `census/round-90/srcs/tr14.html` sha `296df533…`; quote "The NL class acts like BK in
  all respects (there is a mandatory break after any NEL character)." 18 words, occurrence 1; used by
  `corpus/knowledge/nel-byte-character-pair.md`).
- **Rows touched old→new:** none. S353 is new; no existing row's `status`, `recheck` or `used-by` changed. The r89
  lesson's unfiled reject label `S352` is not a registry row and stays unused (plans/round-90.md A0.2, lesson M3).
- **Reject sample (not filed):** UAX #13 — the live URL is a supersession tombstone (capture
  `census/round-90/srcs/tr13.html`, quote 25 words) and the archived `tr13-9.html` confirms it adds no decision for
  this cell; reason and flip condition in the lesson Gate and the entry's Gate.
- **Frontier rows advanced:** `corpus/README.md` gains the r87–r90 frontier section (five bullets: the two-stream
  path spelling, one escaped diagnostic line, the raw-first/`surrogateescape` decode, the byte/character pair, and
  the malformed-guard row). The r89 spot-check's routed map gap (entries r87–r89 unindexed) is closed.
- **Assimilation: none.** `/home/vgpnk/Projects/shokuknow/merge/souji/SOURCES.append.md` staged ids re-measured 134,
  **58 collide** with the lane registry (275 ids; nonempty `.ufo/waves/round-90/assimilation/collisions`), so no
  row is appended and no entry adopted this round; renumbering in scratch is a later round's work.
- **considerthese:** absent (`souji-shokunin/considerthese/` does not exist), so this round mines none.

## Trend verdicts

- **expansion: improved.** SOURCES 274 → 275 with one tier-A `mined` row (S353) and one admitted knowledge entry
  (`corpus/knowledge/nel-byte-character-pair.md`) whose `source:` cites S353, S348 and S351; the frontier map gains
  the r87–r90 rows and the C1 population/mutant ground grows by the LD2b row on ground the r88 corpus did not hold.
- **quality: improved.** The filed tool separates the byte/character pair through the public path (12/12 vs the r89
  tool's 10/12), the r87 12-row K4 counter stays green, the dead helper is deleted, and the wave's four C2 sentence
  narrowings and one C1 evidence narrowing are recorded in the plan and carried to r91 rather than filed as wider
  claims. No admitted entry was found false and left unmarked.
- **discernment: improved.** The round's own wave falsified four C2 sentences and one C1 evidence sentence before
  filing; the L1 narrowed them in `plans/round-90.md` (A1, A4, A5) instead of defending them, and the S353 offset
  slip and the reject word count were corrected before the row and entry landed (S90ScoutSources, S90Scribe).

## SHONEN

`SHONEN.md` boxes (four; a box is `[x]` only with a named non-author verifier, `[~]` with a resolvable pointer):

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md` Decision
  tables/Error patterns/Checklists/Gate registry; `corpus/SOURCES.md` S100–S103 and S353; `corpus/lessons/round-90.md`
  Gate; QUALITY Q165.
- [~] At least one end-to-end domain task executed and logged in LOG.md — LOG.md `## Round 90` (the C1 battery, the
  C2 fixture, the r87 regression and the census, all re-run on committed bytes by non-author seats).
- [~] Instructions executable by an agent without oral context — `census/round-90/preregistration.txt` + the
  instruments it pins; `S90ExecC1`/`S90ExecC2`/`S90Reviewer2` reproduced the commands from the prereg alone.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — PROVINCE.md Round 87 boundary note; the r90 connector's
  sibling scan found no contested scope (`S90Connector` §3); the lane never touched credentials, history or another
  lane.

## Extras

- **Round shape:** one v1 wave, 12 seats; role mix 3 executor / 2 reviewer / critic / mutation-tester / sentinel /
  connector / scout / scribe / revenger (labrat duty); attack share 7/12; connector 1; residual 0; round total 12;
  dead seats 0. Planner: L1 (validator-frozen seat).
- **Pre-file falsification ledger:** `python3 scripts/hyaku/prefile-falsification.py --lane souji --round 90` →
  `PREFILE-FALSIFICATION: pass claims=2 rows=18 attack_seats=7 findings=0`, `EXIT=0` (run immediately before filing,
  against the driver's `w1-results.json` and the 18-row ledger).
- **Stale-lane:** respawn-per-round driver, round 90 of the hyaku campaign; no other mission of this lane is open.
- **Tool installs:** none. No pacman (paused host-wide), no uv/npx/binary fetch, no sysctl/sudo/kernel change.
- **Inherited state:** none (no earlier attempt of r90; `.ufo/watchdog.log` carries only the launch at 11:31 and the
  spawn at 11:47). Files not authored by this lane (other reports, `.ufo/state/*`, `.ufo/l0-questions.md` appends by
  other lanes) were not edited.
- **L0 questions:** `souji | round-90 | WAVE-DONE pending …` appended (settlement request); the round routed around
  it as recorded above.
