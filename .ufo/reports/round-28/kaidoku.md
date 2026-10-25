# kaidoku — round 28 report (attempt 2)

Lane repo `/home/vgpnk/Projects/shokunin/kaidoku-shokunin`. Base `935c36608008f79e3dea4f1ed191df3c89e3b848`. Lane tip at filing: `242b0d8b8ad6ff6c693fa5114216fbb538b587bf`.
Attempt 1 (launched 14:09:06-03, watchdog `lane-dead-no-report kaidoku round=28` at 14:30:08-03) died in an omp process restart at 17:26Z. Attempt 2 is this report.

## Work performed

Declared claims, both frozen by attempt 1 before their counted data:
- **R28-C1, coverage** (learning claim, PROVINCE Frontier "EVM bytecode (extended)"). The round-25 primary EVM selector-naming rule is scored, unchanged, on 61 held-out carriers and 187 held-out selectors. Frozen at `87d3dfb6` (`.ufo/waves/round-28/claims.json`). **Target missed, honest stop: 60/61 runs, 186/187 rows.**
- **R28-C2, depth** (learning claim). openchain's `filtered` flag follows Sourcify's `filterResponse` code (S084, S085). Frozen at `86fa8526` (`.ufo/waves/round-28/claims-c2.json`). **The counter target is met. The wave showed the test is a re-observation, not a held-out test (M28-4).**

Work items:
- Inherited state re-verified and committed: the C2 openchain fetch (230 responses plus manifest, fetched 17:22:05Z–17:25:57Z, after the C2 freeze at 17:21:55Z) and attempt 1's unsent wave-1 spec, dispatch and registry. All four untracked paths landed at `a2673116` (`ReviewInheritedCommits.md`: no frozen file changed after its freeze, and no attempt-1 seat was dispatched).
- C1 miss cause: REA 6.5.0 refused carrier h09 (`invalid_format`). The file `Cr1LibUser.noopt.runtime.hex` holds one unlinked-library placeholder, `__$a2bad93077572174e8e5044433a5a7d5f3$__` (S086 `:74`; `corpus/evidence/round-28/c1/envelopes/h09.json`; `ExecH09Probe.md` reproduced the refusal byte for byte). There was no re-run, no list or counter edit and no narrowing (`CriticC1Miss.md`).
- Entries: `corpus/knowledge/2026-10-22-r28-evm-heldout-selector-naming.md` (triple `named 137, right 137, wrong 0`; title and text carry the miss) and `corpus/knowledge/2026-10-22-r28-openchain-filtered-flag.md` (`mismatches 0 of 246 entries`, with the weakened pre-registration and the corrected limits disclosed).
- Sources: S084 (Sourcify `handlers.ts` at `189cd726`), S085 (`canonical-signatures.json`, same commit) and S086 (Solidity docs `v0.8.30`, Library Linking), all opened this round by the L1 with curl. Gate in `corpus/lessons/round-28.md`.
- Mistakes mined: M28-1 to M28-5 (`corpus/lessons/round-28.md` `## Mistakes`). New QUALITY rows 41 to 44. Two checks shown able to fail on real bytes: `tools/round-28/hex-screen.py` (red on h09, green on the other 60) and `tools/round-28/preseen-overlap.py` (exit 1, 168 pre-seen).
- Round-27 routed defects (spot-check `:150-159`, all 8): 1 r26-entry pointer plus QUALITY row 41 superseding 37; 2 still open (seat `ExecR27SelftestFix` returned a fixture diff after the hard stop; it was not applied, and the selftest stays red, `FAIL correct-stub`, exit 1); 3 SKILL.md `### Round-27/28 measurement registry`; 4 both round-28 freezes pin every loaded file; 5 green look-alike case in the round-28 C1 counter (round-27 C1 not re-scored); 6 QUALITY row 42; 7 SCORECARD clarification of `:3125`/`:3130`; 8 mutation tests on QUALITY rows 39 and 40, the C2 counter and the entry gate (QUALITY row 38: 4 of 10 mutants killed; row 39: 3 of 5; row 40: 1 of 4; `xpin-attribute.mjs`: 17 of 17; C2 counter: 12 of 16; entry gate: 10 of 10. Survivors are missing selftest cases, recorded as coverage findings). Pointer: `SCORECARD.md` round-28 section `### Round-27 routed defects` and `### Round-28 wave findings`.
- Freeze ledger: row `round-28 FLAGGED INSTRUMENT_UNRESOLVED,INSTRUMENT_UNPINNED` in `corpus/claim-freezes.tsv` (gate run by `ExecFreezeGate.md`; C2 was audited by hand because the gate reads only `claims.json`).

## Landed changes

Every commit landed through `jj-lane.sh commit` (`landed <hash>` after remote verification). The LOG.md round-28 entry is at `LOG.md:2985-2995`.
- `87d3dfb6`, `86fa8526`, `ca4069a4`, `cb8d495e` (attempt 1, inherited, re-verified): freezes, C1 runs, C1 lookups and tally. LOG "Freeze" bullet.
- `a267311678309fd17772407e8afa122ec3219289`: C2 fetch and attempt-1 wave files (inherited leftovers). LOG "Freeze" bullet.
- `9db24c9e10287d44d9f780d782ab608f3c84ff5a`: both entries, S084-S086, lesson, QUALITY rows 41-43, hex screen, a2 and a2w specs and dispatches. LOG "Measured" and "Learned".
- `2832c5b3e20d84729bbd7f1b30afc081de9557b5`: SCORECARD round-28 section, r26 pointer, search log, coverage-map and index rows, PROVINCE line, after receipts. LOG "Round-27 routed defects".
- `071270b58e6d2d5f437f1dfa48e4388263ea0026`: wave corrections (C2 relabel, limits correction, M28-4, M28-5, QUALITY row 44, preseen-overlap check). LOG "Learned" and "Mistakes mined".
- `cae73c4966763103a7d67deca7a7f67322715a59`: LOG entry, C1 wording fix, M28-1 correction, hex screen `0X` and green receipt. LOG "Mistakes mined".
- `e01deb198d46073d599d9a3aa1ad624a9f1d685d`: claim-freezes row and seat reports. LOG "Freeze".
- `6ae8c70da15774512ccd1ea54ab507c6a9e7e729`: SKILL.md registry, SCORECARD wave findings, seat reports and the unsent v2 registry. LOG "Round-27 routed defects" and "Wave".
- `242b0d8b8ad6ff6c693fa5114216fbb538b587bf`: final seat reports and SCORECARD defect-2 status (open). LOG "Wave".

## Before → after measurements

| claim | counting command | before (at `935c3660`) | after | measured at | verdict |
|---|---|---|---|---|---|
| R28-C1 | `python3 -I -B tools/round-28/c1-heldout-naming.py --root /home/vgpnk/Projects/shokunin/kaidoku-shokunin --rev <REV>` | exit 2, frozen lists absent (`.ufo/waves/round-28/before/c1-at-935c3660.txt`) | `runs_ok=60/61 rows_complete=186/187 tally_equal=1 entry_ok=1`, exit 1 | `9db24c9e` (receipt `.ufo/waves/round-28/after/c1-at-9db24c9e.txt`), same at `071270b5` and `242b0d8b8ad6ff6c693fa5114216fbb538b587bf` | **missed (honest stop)** |
| R28-C2 | `python3 -I -B tools/round-28/c2-filtered-flag.py --root /home/vgpnk/Projects/shokunin/kaidoku-shokunin --rev <REV>` | exit 2, pinned inputs absent (`before/c2-at-935c3660.txt`) | `responses_complete=230/230 entries=246 mismatches=0 predicted_true=59 entry_ok=1`, exit 0 | `9db24c9e` (`after/c2-at-9db24c9e.txt`), same at `071270b5` and `242b0d8b8ad6ff6c693fa5114216fbb538b587bf` | target met. The test is weakened: 168 of 230 selectors were pre-seen (`after/preseen-overlap-c2.txt`) |

Selftests at `9db24c9e`: C1 21 cases, 0 failures. C2 17 cases, 0 failures. Independent re-derivations: C1 137/137/0/50 with pycryptodome keccak (`ExecIndependentC1.md`). All 187 tally rows re-derived in 4 slices, 0 disagreeing. C2 230/246/0/59 (`ExecIndependentC2.md`).

## Sources & frontier

- Census command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kaidoku`. Round start (17:46Z, before any round-28 row): `kaidoku ok` with W04 warnings S033, S047, S054, S062, S069 and S083, **exit 0**. Round end (at `242b0d8b8ad6ff6c693fa5114216fbb538b587bf`): `kaidoku ok` with the same six W04 warnings and no new warning, **exit 0**.
- Rows 83 → 86 (`git show <rev>:corpus/SOURCES.md | grep -cE '^\| S[0-9]{3,} \|'` at `935c3660` and `242b0d8b8ad6ff6c693fa5114216fbb538b587bf`). Added by tier: A 3 (S084 code, S085 dataset, S086 docs). Rows touched old→new: none; no existing status, recheck or used-by changed. Search-log line added for round 28. The planned S087 (4byte.directory server source) was never opened and is not a row.
- Frontier: the "EVM bytecode (extended)" bullet is annotated, not moved (`PROVINCE.md:94`, claim missed). The coverage map gains two rows (`corpus/README.md:77-78`).
- Sourced claim: R28-C2's entry cites S084 and S085, opened this round. R28-C1's entry cites S086.
- Mined mistake: M28-1 (frozen carrier list held a non-hex carrier). Its fix was shown able to fail: `hex-screen.py` exits 1 on the frozen list and 0 on the 60 others. Also M28-2 to M28-5.

## Trend verdicts

- **expansion: improved (author's reading).** Knowledge files 110 → 112 (`git ls-tree --name-only <rev> corpus/knowledge/ | grep -c '\.md$'`), on ground the map did not hold: an out-of-sample score of the round-25 naming rule and the code mechanism of openchain's `filtered` flag. Rows S084-S086 are new. Neither claim is admitted, so the outside reviewer rules.
- **quality: unprovable-but-better.** The round-25 rule's zero-error record now holds out of sample on 137 named rows, re-derived by 5 independent seats. The r26 entry and QUALITY row 37 got their round-27 pointer and successor row. But the C2 test turned out to be a re-observation (M28-4), and its frozen limits sentence was wrong (M28-5). Both are disclosed, not fixed by edit.
- **discernment: unprovable-but-better.** All 8 routed defects were acted on, with 3 sources admitted after critic review, 5 mistakes mined and 4 QUALITY rows added. The lane's own wave caught a weakness in its own claim (C2 pre-registration) before filing. That is self-reported and needs the non-author spot-check.

Axes: coverage unchanged (C1 missed; no harm). Depth unchanged on the proxy; C2's own reading is `unprovable-but-better`, not `improved`. Calibration, operability, freshness and adjacency unchanged, not claimed. Admission: the round does not meet the every-claim-verifies rule (fleet `AXES.md`). By the round-27 precedent the expected outside status is `rejected-honest-stop` (inference). The outside reviewer rules.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md:81-314`; round 28 appends the `### Round-27/28 measurement registry` table at `SKILL.md:948-954`.
- [~] At least one end-to-end domain task executed and logged in LOG.md — 61 REA 6.5.0 `inspect-evm-interface` calls (`corpus/evidence/round-28/c1/runs.tsv`), with LOG at `LOG.md:2985`.
- [~] Instructions executable by an agent without oral context — the `recheck:` lines of both round-28 entries are offline commands over committed bytes.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md:94` annotation only; Adjacent unchanged; revenger overlap cited, not absorbed (`ConnectorSiblings.md`).

## Round shape, seats and conformance

- Shape: one v1 wave (`a2w`, 36 seats, policy v1, band 32-64): reviewer 11, executor 7, critic 6, mutation-tester 6, scout 3, scribe 2, connector 1. Attack roles 23 of 36 (64%). Round total 36 seats. No wave 2, and no residual call (scope freeze at 18:41Z). A 73-seat v2 wave (`a2-spec.json`, validated, policy v2) waited about 30 minutes for seat capacity (`live_estimate=60 cap=85` at 18:19Z) and was withdrawn before dispatch, so it never spawned (M28-2). Gate: `granted lane=kaidoku wave=kaidoku-r28-a2-a2w seats=36 live=49` at 18:22:34Z, dispatched as one `task` call with the validator's `taskCall` unchanged.
- §3 L2 floor met inside `a2w`: connector, 7 executors, 2 scribes, 3 scouts, reviewers, critics. Planner seat: held by the L1. The planning data-walk rode the scouts and the connector. Routing: no `model` passed; roles routed by `task.agentModelOverrides`.
- Seats: all 36 returned reports (`.ufo/waves/round-28/a2w/`, 36 `.md` files); none died and none refused. `ExecR27SelftestFix` returned after Main's 19:25Z hard stop, and its diff is not integrated. Slot release: `wave-slot.sh release kaidoku kaidoku-r28-a2-a2w`.
- Integration owner: the L1. Seats wrote only their own reports in the lane and worked in `/fast/scratch/hyaku/kaidoku-r28/seats/a2w/` and sandbox clones.
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain -uall` lists untracked `AGENTS.md`, `live_s228.html`, `nama.html`, `tf_bavelas.html` and a `__pycache__` file. None names kaidoku or round 28. Nothing was moved.
- Inherited state: attempt 1's 4 untracked paths (`corpus/evidence/round-28/c2/db/`, `.ufo/waves/round-28/w1-spec.json`, `w1-dispatch.json`, `w1/swarm-registry.json`) were all re-verified and committed at `a2673116`, and none was reverted. Attempt 1's pushed commits `87d3dfb6`..`cb8d495e` were re-verified and kept. Not authored by this round, read only: `corpus/lessons/round-27-verifier-spotcheck.md`.
- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
- Tool installs: L1 none. Seat `ExecIndependentC1` made a `uv venv` (CPython 3.15.0) with `uv pip install pycryptodome 4.1.0` in its scratch dir, to get an independent keccak. No other seat installed anything. No pacman transaction.
- Open L0 questions: none from this lane.
- Next planned move: a real held-out test of the `filtered` rule on the 26 untested canonical keys, frozen before any fetch (QUALITY row 44), or the EVM naming rule on a hex-screened carrier list (QUALITY row 43).
