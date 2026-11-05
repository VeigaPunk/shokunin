# kengaku — round 87 (hyaku run 15, attempt 1)

Lane `kengaku-shokunin`, branch `master`. Base `b9be687774e6b559470f5b0d9b936315b51ff311` (round-86 spot-check tip).
Freeze `b0f076518dad55f62a89183c5a873957ad3cf6a5` (claims and case table, before any instrument). Instruments `21da383b44a399f40faf346eed89210c9114848d`.
Receipt `corpus/evidence/round87/mteb-retrieve-probe.txt` (LANE_TIP `21da383b`, WORKTREE clean). Measured tip `10de494d14abf0b77979225f51b3b72e73c0d2ed`.
Lane HEAD at report time: 6b7e83aa2aabdc26089830986e8ee2e04a2ba00d (`master`, round-87 commit D; the remote `refs/heads/master` carries the same hash at filing).

**Wave status, stated first:** one v1 wave `w1` (12 seats, policy v1, plan and run validated, band 8–16) was handed off through `.ufo/waves/round-87/w1.ready` at 00:58 -03. The orchestrator never marked it (`w1.ready.dispatched` absent), no WAVE-DONE arrived, and the fleet watchdog log has not advanced since 00:53 -03 while `.scratch/run15-drain` has existed since 00:54 -03. Two background waits of 1500 s each released with no handoff. **Zero seats ran.** Every measurement below was made by the L1 on committed bytes; no independent seat verification, attack, spot-check or mutation battery exists for this round. The L0 question is in the fleet file .ufo/l0-questions.md at line 312. The round's verdicts are therefore L1-measured and not non-author verified.

## Work performed

The round declared **two claims**, each on a distinct axis and each causally separable:

- **R87-C1 — coverage** (lowest non-retired axis, held at its L0 cap of 7): a fifth located offline replay of a Terminal-Bench 2.0 grader, `mteb-retrieve`, with the counter `plans/round87_c1_replay.py` over the frozen eight-case table `plans/round87-cases.json`. The counter counts its own executed rows from the ledger (closes round-86 defect R86-V4).
- **R87-C2 — calibration** (held at its ceiling of 10): the live current-state wording of the round-86 case set (`corpus/README.md`, `PROVINCE.md`, `SKILL.md`) agreed with the table-derived split (eight case shapes, six schema-drift, two controls), by `plans/round87_c2_wording.py` (closes round-86 defect R86-V3 in live docs).

Plus the frontier step (one sourced claim, a mined mistake) and the report-pointer checker.

Work items, each with its evidence pointer:

- **Protocol load.** `skill://shokunin`, `skill://swarm`, `/home/vgpnk/.omp/agent/RULES.md` (tooling directive read), `MISSION.md`, `AXES.md`, `PROTOCOL.md`, `CORPUS.md`, `LEARNING.md`, the lane's `SCORECARD.md`, `SHONEN.md`, `corpus/QUALITY.md`, `corpus/README.md`, and the round-86 spot-check `corpus/lessons/round-86-verifier-spotcheck.md`.
- **Freeze, commit A** `b0f07651`: `plans/round-87-claims.md` and `plans/round87-cases.json` (eight cases; predicted vectors read from the captured grader before any execution).
- **Instruments, commit B** `21da383b`: `plans/round87_mteb_probe.py` (bubblewrap replay of the captured grader; stages `/app/result.txt` per case), `plans/round87_c1_replay.py` (legs L1–L8), `plans/round87_c2_wording.py`, `plans/round87_report_paths.py`.
- **Receipt and ledger, commit C** `10de494d`: `corpus/evidence/round87/mteb-retrieve-probe.txt` (`PREDICATE R87-PROBE pass`, eight cases, sixteen legs, zero mismatches); `plans/grader-population-ledger.json` row `mteb-retrieve` → executed, round 87; `corpus/README.md` line 941 wording repaired and round-87 index rows added.
- **Sources.** Both pinned grader URLs were opened on 2026-11-05 (HTTP 200): `mteb-retrieve` 559 B, sha256 `e4e6b21f…c0b`, byte-identical to `corpus/evidence/round52/graders/mteb-retrieve/tests/test_outputs.py` (`cmp` silent); `mteb-leaderboard` 537 B, sha256 `b28f8fc8…892cf`. Rows S275 (admitted) and S276 (rejected, with flip) in `corpus/SOURCES.md`; Gate in `corpus/lessons/round-87.md`.
- **Controls** (`.ufo/waves/round-87/L1/controls.txt`, built in scratch clones): ledger-only → `DEFECT L1-receipt`, rc 1; forged `LANE_TIP` to an orphan commit → `DEFECT L3-tip`, rc 1; C2 wrong derived split → `DEFECT CANON`, rc 1; C2 stray "five schema-drift cases" → `DEFECT MISMATCH`, rc 1.
- **Do-nothing baselines at BASE** (`.ufo/waves/round-87/L1/base-runs.txt`): C1 `defects=3`, rc 1; C2 `mismatches=1 defects=2`, rc 1.
- **Pointer checker red-before** (`.ufo/waves/round-87/L1/paths-red.txt`): run on the round-86 filed report, `DEFECT pointer .ufo/waves/round-86/L1/outside-gates.txt (report line 59)`, `POINTERS n=26 missing=1`, rc 1.
- **Census** (`scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kengaku`): exit 0 before and after.
- **Wave, planned not run.** Spec `.ufo/waves/round-87/w1-spec.json` (generator `.ufo/waves/round-87/make-spec.py`); dispatch payload `.ufo/waves/round-87/w1-dispatch.json` (`counts spawn=12 resume=0 total=12`, `waveMinLanes 8`, `waveMaxLanes 16`); validator registry `.ufo/scopes/kengaku-r87-w1/swarm-registry.json` (agent ids null; no spawn recorded). Planned seats: ScoutR87 (scout), ScribeR87 (scribe), ExecBaseR87, ExecCtrlR87, ExecCensusR87 (executor ×3), ReviewerR87a/b/c (reviewer ×3), CriticR87 (critic), MutTesterR87 (mutation-tester), SentinelR87 (sentinel), ConnectorR87 (connector). Planned attack share 5/12 (42 %). Planner seat held by the L1. No model was passed; routing is the global table.
- **Mistakes mined** (`corpus/lessons/round-87.md` `## Mistakes`): reference-drift (the dead pointer above; fixed by the checker, shown red on the round-86 report), number-drift (a BASE figure carried into the frozen claim text; criterion Q66, no executable half yet), vacuous (the `members=1` literal; fixed by the executed-row count).
- **Misroot sweep** (`git -C /home/vgpnk/Projects/shokunin status --porcelain`): fleet-root entries are `M .scratch/run15-state.json`, `A mo.tip` (staged by another party) and `?? .scratch/run15-drain`. None was written by a seat of this round; none copied; nothing deleted. `.scratch/` is orchestrator state and was not touched.

## Landed changes

Each change is tied to its LOG entry (`LOG.md`, section "Round 87") and to the commit that carries it:

| change | LOG entry | commit |
|---|---|---|
| frozen claims and case table | Round 87, claim lines | `b0f07651` |
| probe, C1 counter, C2 counter, pointer checker | Round 87, claim lines and pointer checker | `21da383b` |
| receipt, ledger row, README wording and round-87 index rows, S275/S276, lesson, Q66, BASE transcripts | Round 87, all lines | `10de494d` |
| wave spec, generator, dispatch, registry, control and tip transcripts, LOG and SCORECARD entries, ready file | Round 87 (commit message) | `6b7e83aa` |
| this report and the L0 line (fleet file .ufo/l0-questions.md, line 312) | — | filed with fleet-commit.sh --as kengaku (the fleet-repo commit carries both) |

Corrections and errata in this round:

- **Frozen claim text, not edited.** `plans/round-87-claims.md` states C1 BASE `defects=7`; the counter measures `defects=3` at `b9be6877`. The predicate `defects=0` is unchanged. The measured figure is recorded in LOG and in `corpus/lessons/round-87.md` Mistakes 2.
- **Frozen control text, not edited.** The claim file says a C2 fixture "five schema-drift and three controls" must report `mismatches>=1`. The counter rejects that fixture with `DEFECT CANON` and reports `mismatches=0 defects=1`. The frozen wording is imprecise; the counter still rejects the fixture.
- **Erratum to the round-86 filed report (bytes not rewritten).** Report line 59 cites the round-86 outside-gates file, which exists in no ref (round-86 spot-check defect 1). The Q20 roster is at `.ufo/waves/round-86/w1/ExecGatesR86/gate-receipt.txt`, a `git archive` extraction at `f357e4c1` and `ab9da0d4`, before instrument v2 `e23bec07`, with `--lane`/`--repo` overrides; it is not a shared clone at the tip (round-86 defect 5). Round-86 report line 7 "zero dead seats" and line 242 "naming the two incomplete seats above" conflict with line 230 (one incomplete seat, ReviewerC286); the spot-check routed them as defect 2. The round-86 pointer to the outside-gates file is the dead one named in the checker's red-before run.

## Before → after measurements

Counting commands are re-runnable from the lane root; the commit each was measured against is named.

| claim | before (base `b9be6877`) | after (tip `10de494d`) | counting command |
|---|---|---|---|
| R87-C1 coverage | `TARGET executed_rows=30 member=mteb-retrieve located=0 executed=0 cases=0 legs=0 mismatches=0 defects=3`, `PREDICATE R87-C1 fail`, rc 1 | `TARGET executed_rows=31 member=mteb-retrieve located=1 executed=1 cases=8 legs=16 mismatches=0 defects=0`, `PREDICATE R87-C1 pass`, rc 0 | `python3 plans/round87_c1_replay.py --lane . --rev REV --work DIR` |
| R87-C1 ledger | `executed` count 30 (`json.load` of the ledger at `b9be6877`) | 31 at `10de494d` | `python3 -c "import json;print(sum(v['status']=='executed' for v in json.load(open('plans/grader-population-ledger.json'))['members'].values()))"` run with `git show REV:` bytes |
| R87-C2 calibration | `TARGET mismatches=1 defects=2 total=8 schema=6 control=2`, `PREDICATE R87-C2 fail`, rc 1 | `TARGET mismatches=0 defects=0 total=8 schema=6 control=2`, `PREDICATE R87-C2 pass`, rc 0 | `python3 plans/round87_c2_wording.py --lane . --rev REV --work DIR` |

Transcripts: `.ufo/waves/round-87/L1/base-runs.txt` and `.ufo/waves/round-87/L1/tip-runs.txt`. The ledger row's population class `file-artifact` goes from 22 of 76 to 23 of 76 at the same two revisions.

Claim verdicts, as measured by the L1 (not non-author verified): **R87-C1 met on its frozen predicate**; **R87-C2 met on its frozen predicate**. Scores: coverage 7 (held at its L0 cap; the expansion observable did not move); calibration 10 (held; the mismatch count 1 → 0 is recorded, not added to the score, as in the round-86 C2 precedent).

Honest limits: the receipt's stamp names the measured tip, and L6 reproduces the observation block from an extraction of the tree; neither authenticates an author. The eight cases yield four distinct predicted vectors (`P/P` ×2, `F/F`, `P/F` ×3, `P/E` ×2). No independent seat has re-run any counter.

## Sources & frontier

- **Registry before → after.** Counting command: `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`, run at `b9be6877` (`git show` of the file) and at `10de494d`: **266 → 268**. Census: `sh scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kengaku` exit 0 before and after (`W04` duplicates unchanged in kind; the `ok` line names the lane's SOURCES.md).
- **Rows added by tier.** Tier A: 2 (S275 admitted, mined; S276 rejected with flip). Tier B: 0. Tier C: 0.
- **Rows touched old → new.** None. No existing row's status, recheck or used-by cell changed. Status histogram: mined 242 → 243; rejected 16 → 17; queued 8 → 8.
- **Frontier rows advanced.** S275 (the `mteb-retrieve` grader bytes) is the round's sourced row: the frozen claim, the receipt's `SUBJECT_SHA` and the ledger row cite it through `corpus/lessons/round-87.md`. It moves the member from frontier to the replayed set.
- **Assimilation.** None. `merge/kengaku/` remains blocked by L0 `kengaku | round-54`. `considerthese/`: no unimplemented proposal was taken this round (the latest proposal 2 of `considerthese/2026-10-26.md` is Q61's per-entry form, per the round-86 spot-check).
- **Non-author spot-check.** Not run: the ReviewerR87c item was in the wave that never dispatched. The gate decisions (admit S275, reject S276) therefore carry no outside verdict this round.

## Trend verdicts

- **expansion — unchanged.** One member of the same replay method; no new kind of source; no admitted `knowledge/` entry on uncovered ground (the `raman-fitting` knowledge entry was held in round 86 for the Q13 shape; no knowledge entry was written this round). Evidence: `corpus/SOURCES.md` S275 row; `corpus/lessons/round-87.md` Gate.
- **quality — improved.** A stale live entry is repaired by derivation: `corpus/README.md` line 941 said "eight frozen schema-drift cases" and now carries the table-derived sentence (C2 `mismatches 1 → 0`). A fix that was not checkable is now checkable: the report pointer checker is red on the round-86 report and fails closed. No admitted entry failed a re-check. Evidence: `.ufo/waves/round-87/L1/base-runs.txt`, `tip-runs.txt`, `paths-red.txt`.
- **discernment — unchanged.** No non-author spot-check ran, so the lesson's gate decisions have no outside agreement or disagreement on record this round. The routed Q66 criterion has no executable half yet, so no disagreement was turned into an executable criterion.

Stale-lane: no other mission of this lane is open; round 87 attempt 1 is the only open mission. The round's wave `w1` is handed off and unsettled, which is the L0 question, not a second mission.

Tool installs: none. `/home/vgpnk/.omp/agent/RULES.md` was read; bubblewrap 0.13.1 and `curl` were already present and used as-is. pacman remained paused.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — SKILL.md
- [~] At least one end-to-end domain task executed and logged in LOG.md — LOG.md:7
- [~] Instructions executable by an agent without oral context — corpus/lessons/round-8-aggregator-box3-coldrun.md:48
- [~] No cross-domain bleed (PROVINCE.md still accurate) — PROVINCE.md:151

Round shape: one v1 wave planned (12 seats: scout 1, scribe 1, executor 3, reviewer 3, critic 1, mutation-tester 1, sentinel 1, connector 1; attack share 5/12). Spawned 0. Dead seats: none (none spawned). Residual call: none. Wave 2: none. Round total seats run: 0.
