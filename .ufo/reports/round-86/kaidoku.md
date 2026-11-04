# kaidoku — round 86 (attempt 1)

Lane repo `kaidoku-shokunin` (branch `main`). Lane tip at report time: `697193400d45b4989acfec0b397ae12aa758affc` (verified `ls-remote origin refs/heads/main`). Round base `2cf0b7ff93c698809bed321f7338276a22d6beb9`. Measured revision for every claim: `4cc03025e6d4f6f1e00b5e402fcc0180e6e730bc`.

## Work performed

**Declared claims (2; axes coverage, depth, calibration; calibration is the tied-lowest axis).**

- **R86-C1 — calibration.** Three record cells that state a value about a committed object (the SOURCES registry row that supersedes S303; the `tools/round-84/mutation-closure.py` docstring sentence about an absent declared case; the SCORECARD `| coverage |` receipt pointer) are re-derived from the bytes they describe by `tools/round-86/record-agreement.py`. Target: agreed 0/3 → 3/3. **Verdict: missed.**
- **R86-C2 — operability (the lane-claimed axis; not an owned lane score, see verdict).** The round-85 gate `tools/round-85/predicate-bind.py` is registered in the SKILL instrument registry and its five declared fields re-derive by `tools/round-86/gate-registry.py`. Target: agreed 0/5 → 5/5. **Verdict: target met at the measured revision; not admitted.**
- No stagnation waiver. No exploratory claim. No capability row entered. Frontier step: one sourced claim (S255, opened this round), one mined mistake set (M86-1..M86-4), census before and after (see Sources & frontier).

**Evidence per work item.**

- Protocol and inherited state: `corpus/lessons/round-85-verifier-spotcheck.md` read (routed R85-1..R85-6, and the discernment verdict). The round-85 spot-check's untracked orchestrator markers `.ufo/waves/round-85/r85-w1.ready(.dispatched)` are left untouched.
- Declaration `b205bb8b66ec7b61e028bccd92f64eade8942461` (plan `plans/round-86-claims.md`, two counters, BASE receipts `.ufo/waves/round-86/pre/*-at-base.json`, control receipts). Container commit `ec9963eb9e5c1eedfada9a69f073c1639e7911f9`: the first container was FLAGGED by the R84-C1 freeze gate because receipt paths sat in claim strings; the paths were moved and the container is CLEAN (`pre/freeze-precheck-at-declaration.json`, met true with positive and negative containers).
- Wave `r86-w1`: spec `.ufo/waves/round-86/r86-w1-spec.json`; validated dispatch `.ufo/waves/round-86/r86-w1-dispatch.json` (validator exit 0, twelve tasks); ready file `.ufo/waves/round-86/r86-w1.ready` taken by the orchestrator; WAVE-DONE received; results `.ufo/waves/round-86/r86-w1-results.json`; seat reports `.ufo/waves/round-86/w1/<seat>/`.
- Integration `4cc03025e6d4f6f1e00b5e402fcc0180e6e730bc`: A2 docstring repair at `tools/round-84/mutation-closure.py:8` (docstring only, sha256 `4d73c89e…`, old `e5cfd2ed…`); S305 supersession row at `corpus/SOURCES.md:221` (S303 untouched, `:219`); S255 re-open and used-by extension at `corpus/SOURCES.md:172`; registry rows for `tools/round-85/predicate-bind.py` and both round-86 counters at `SKILL.md:1930–1932`; knowledge `corpus/knowledge/2026-11-04-r86-record-agreement.md` with map row `corpus/README.md:127` and index row `:264`.
- Record commit `63c30e9d37556bd14fc21ec172d079f676684a2d`: `SCORECARD.md` round-86 section (appended after line 6445); `LOG.md` round-86 entry (after line 4871); `corpus/QUALITY.md` rows 150–151 (after row 149); `corpus/lessons/round-86.md`; container `measured_revision`, `declaration_pointer` and `instrument_supersessions` (`.ufo/waves/round-86/claims.json`); measured receipts `.ufo/waves/round-86/l1/scores/*`; sweeps `.ufo/waves/round-86/l1/sweep/*`.
- Wave evidence commit `697193400d45b4989acfec0b397ae12aa758affc`: the twelve seat directories, results handoff and census receipts.
- Sweep for M86-2 (behavioural, red on the frozen counter): a SKILL row whose self-test command is `python3 -c "import sys; sys.exit(0)"` scores `agreed=5/5` (`.ufo/waves/round-86/l1/sweep/g3-behavioural-red.txt`, `g3-foreign-command-accepted.json`).
- Sweep for M86-3: `git show 2cf0b7ff:SCORECARD.md | grep -c '^| coverage |'` = 23 (`.ufo/waves/round-86/l1/sweep/atom-clause-sweep-red.txt`).

## Landed changes

| commit | LOG / SCORECARD / lesson tie | change |
|---|---|---|
| `4cc03025e6d4f6f1e00b5e402fcc0180e6e730bc` | LOG round-86 entry; SCORECARD round-86 record | `tools/round-84/mutation-closure.py:8` docstring (R85-5); `corpus/SOURCES.md` S305 (R85-3) and S255 used-by; `SKILL.md` registry rows (R85-2); knowledge entry and map/index rows |
| `63c30e9d37556bd14fc21ec172d079f676684a2d` | SCORECARD round-86 section; LOG round-86; `corpus/lessons/round-86.md` Corrections C-R86-1/2/3 | `corpus/QUALITY.md` rows 150–151; container measured fields; receipts and sweeps |
| `697193400d45b4989acfec0b397ae12aa758affc` | lesson `## Sweep evidence`; SCORECARD round-86 record | wave evidence and census receipts |

Not landed, by decision: the coverage row (R85-6) is unchanged; no receipt was created or backdated to satisfy A3; the scribe's proposed coverage-row edit was not adopted.

## Before → after measurements

Counting commands are run from the lane root with `python3 -I -B`; receipts are retained.

| claim | before (base `2cf0b7ff`) | after (measured `4cc03025`) | command | exit |
|---|---|---|---|---|
| R86-C1 | agreed 0/3 (`pre/c1-at-base.json`) | agreed 2/3, mismatch `A3-receipt-pointer` (`l1/scores/c1-at-integration.json`) | `python3 -I -B tools/round-86/record-agreement.py --root . --rev 4cc03025e6d4f6f1e00b5e402fcc0180e6e730bc --json-out <receipt>` | 1 |
| R86-C1 control (`substring-only`) | accepts the BASE records, mismatches 0 | accepts, mismatches 0 (`l1/scores/c1-control-at-integration.json`) | `… --control substring-only …` | 0 |
| R86-C2 | agreed 0/5 (`pre/c2-at-base.json`) | agreed 5/5 (`l1/scores/c2-at-integration.json`) | `python3 -I -B tools/round-86/gate-registry.py --root . --rev 4cc03025e6d4f6f1e00b5e402fcc0180e6e730bc --work <scratch> --json-out <receipt>` | 0 |
| R86-C2 control (`file-exists`) | accepts the unregistered state | accepts (`l1/scores/c2-control-at-integration.json`) | `… --control file-exists …` | 0 |
| depth table (round-85 frozen, no-harm check) | 3/21 at round 85 | 21/21 killed, pristine green, table identity matched (`l1/scores/c2-mutation-closure-r85-table-at-integration.json`) | `python3 -I -B tools/round-84/mutation-closure.py --root . --rev 4cc03025… --mutants .ufo/waves/round-85/mutants.json --work <scratch> --json-out <receipt>` | 0 |
| counter selftests at `4cc03025` | — | record-agreement 11/0; gate-registry 8/0; mutation-closure 10/0 | `--selftest` | 0 |

Caveat on the C2 measurement: the gate counter runs G2 and G3 from the working tree, not from the revision (sentinel C-1). The measured run was made with `tools/round-85/` and `SKILL.md` clean against the commit, so the worktree bytes equal the committed bytes at measurement.

**Attack results (wave `r86-w1`).** Record counter: "newest" is last-in-file; the count selector and docstring disagree; "covered by" means "named by the row"; A3 is satisfiable by a fabricated receipt or by rewriting the row's round; A1 is self-referential; fenced and split-sentence cases are accepted. Gate counter: a foreign command passes G3; a verdict-map substring `10=` satisfies `0=`; a six-cell duplicate row is dropped silently; a pin naming another round passes; G2/G3 run the worktree tool; `--json-out` can clobber `pre/`; `GIT_DIR` redirects its git children. Mutation: 20 mutants on the two counters, killed 7, survived 13, inconclusive 0.

## Sources & frontier

- `corpus/SOURCES.md` census, validate exit codes: before `0` (`pre/sources-census-before.txt`), after `0` (`pre/sources-census-after.txt`); round-end conformance `sources-census.sh validate --root /home/vgpnk/Projects/shokunin kaidoku` exit 0.
- Rows: 209 → 210. Tiers A 190 → 191, B 11 → 11, C 8 → 8. Status: mined 187 → 187, rejected 22 → 23.
- Rows added by tier: S305 (tier A, status rejected, a correction row for S303's scope count; no document opened and no URL of its own).
- Rows touched old → new: S255 used-by `…corpus/lessons/round-83.md` → `…corpus/lessons/round-83.md, corpus/knowledge/2026-11-04-r86-record-agreement.md`; S255 `opened` stays 2026-11-01, and the re-open is recorded in the knowledge entry and the lesson's Gate block. S303 unchanged (rejected).
- Sourced claim: the knowledge entry cites S255, opened 2026-11-04 (HTTP 200, 246736 bytes, sha256 `a3716a4d6c236082b0f6d08da64735765f376c1c32ba5ede93b70b013f52a9aa`, located quote "For plain blobs, it shows the plain contents." DESCRIPTION, 8 words).
- Frontier rows advanced: none (no frontier promotion).
- Assimilation: none. No `merge/kaidoku/` package was consumed; `considerthese/` does not exist in this lane.
- Coverage-map: one map row added (`2026-11-04-r86-record-agreement`); the coverage score row is unchanged.

## Trend verdicts

- **expansion: unchanged.** One bounded apparatus knowledge entry and one correction row; no domain ground or frontier moved.
- **quality: improved (bounded to the record and registry surfaces).** Two of three record cells now re-derive (A1, A2), and the round-85 gate has a registry row whose self-test is run by the counter. The counters' false greens are named limits, not admitted quality.
- **discernment: unchanged, pending non-author closure.** This round's attacks found real false greens in both counters and a misspecified frozen atom (M86-2, M86-3). That is evidence the attack seats discern, but no non-author verdict on this round exists yet.

Round verdicts: C1 missed (frozen target not reached; no calibration move). C2 met its frozen measure but is not admitted, because operability is not an owned lane axis (the SCORECARD marks it "fleet axis, unowned proxy"), so no owned score can move. The round is not admitted. No owned axis score changed (coverage 10.0, depth 10.0, calibration 10.0, freshness 10.0); no axis is harmed.

## SHONEN

[~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — evidence: `SKILL.md:1930–1932` (round-85 and round-86 registry rows with executable commands); the round added rows, it did not add decision tables.
[ ] At least one end-to-end domain task executed and logged in LOG.md — no domain task ran this round; the round is apparatus work.
[~] Instructions executable by an agent without oral context — evidence: `SKILL.md:1930–1932` (each registry row names its entry command, verdict map and exit codes); the counters' own limits are open (see Sources & frontier and the SCORECARD round-86 record).
[~] No cross-domain bleed (PROVINCE.md still accurate) — evidence: `git diff 2cf0b7ff 4cc03025 -- PROVINCE.md` is empty; PROVINCE.md was not reviewed for accuracy this round.

grep -c '^## SHONEN' prints 1 for this file.

## Wave shape, seats and dead seats

- One v1 wave `r86-w1` (policy band 8–16): twelve seats — scout 1, executor 3, scribe 2, reviewer 2, critic 1, mutation-tester 1, sentinel 1, connector 1. Attack seats 5/12 = 41.7 % (reviewer ×2, critic, mutation-tester, sentinel), connector 1. The L1 held the planner seat (disclosed deviation; a planner is not a swarm role). Residual call: none.
- Dead seat: `ScribeSources` — no report file written; its S305 and knowledge drafting was superseded by the L1's own integration, and its row was not used. Results file reports `output: null` for all twelve seats because the orchestrator kernel restarted mid-wave; eleven seats have reports in `.ufo/waves/round-86/w1/`.
- Incident: the L1 made one direct `task` call to message its own seats, which the inline spawn handoff forbids. It spawned `KaidokuR86.ScoutRecon-6`; I cancelled it within seconds. It failed upstream (`402 Insufficient account funds`, opencode-go) with no output and wrote nothing; it is not a wave seat and contributed nothing. The three running seats were then messaged by id and settled.

## Stale-lane

Stale-lane: no. No other mission of this lane is open.

## Tool installs

None. No tool installed or upgraded during the round (tooling authorization read; pacman paused and not used).

## Misroot sweep and inherited state

- `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows no untracked file that names round 86 or this lane at the fleet root; the untracked `.scratch/closure-*.json` entries belong to the orchestrator and were not touched.
- Lane untracked leftovers: `.ufo/waves/round-85/r85-w1.ready(.dispatched)` (round-85 orchestrator markers) and `.ufo/waves/round-86/r86-w1.ready(.dispatched)` (this round's orchestrator handoff); both are left untracked. `tools/round-86/__pycache__` is gitignored.
- Watchdog: one launch line for `kaidoku round=86` (attempt 1); no `lane-dead-no-report` line.

## Open L0 question

Appended to `.ufo/l0-questions.md` with this report: operability is not an owned lane axis, so R86-C2 cannot be admitted as drafted. The operator must rule whether the lane may own operability or whether registry claims must name an owned axis.

## Routed to the next steered round

1. C1 atom A3 is misspecified (exactly one `| coverage |` row; the card has 23); re-declare against the card's own current-assessment pointer with a pre-freeze sweep (M86-3; R85-6 stays open).
2. Gate counter: G2 and G3 must run from `git show REV:` blobs (sentinel C-1); enforce "on that tool path"; refuse verdict substrings and six-cell rows; refuse `--json-out` into `pre/` (M86-2).
3. Record counter: define "newest" by id or date; make the count selector match the docstring; refuse fenced and split-sentence cases; make the rev-shape check a commit check.
4. Selftests: close the 13 surviving mutants (`.ufo/waves/round-86/w1/MutationR86/report.md`) and have the selftests exercise the production atoms.
5. Carried: R85-4 (declared-case binding limits); the planner-seat deviation.
