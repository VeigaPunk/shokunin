# kama round 50 report

author: kama L1 (agent `KamaR50`)
date: 2026-10-27
attempt: 1 (watchdog: `2026-10-26T21:10:17-03:00 launch kama round=50 pgid=3210392 driver=hyaku-inline attempt=1`; no `lane-dead-no-report kama round=50` line, nothing inherited)
base: `26ecba64ad6fb571d09074b07202d1618a46ecd1` (round-49 verifier spot-check; lane remote tip at launch)
freeze: `601c8889f33d1797c712feb753974c20cf891264` (preregistration `.ufo/waves/round-50/preregistration.json`, frozen_at 2026-10-27T00:20:47Z; KQ64 receipt `freeze/prereg-time-check.out` → `RESULT pass`, exit 0)
build: `97c864bead3ee4a2f629574e77263d33834ec98a`
build-fix: `3d42897b65294ad963cd3686ced4666822e0ec73` (S498 row tick parity)
measured commit: `8370e39cc9a0589b831a724b00e6fa4a6293e52f` (`.ufo/waves/round-50/measured/c1.out`, `c2.out`, each carrying `tip=8370e39c…`)
lane tip: `5a1e29a14669521982843fd249583bf8ba755a51` (`git ls-remote origin refs/heads/master` prints it; `jj-lane.sh state` → `ahead=0 behind=0`, `git status --porcelain` empty)
Stale-lane: progressing. The driver respawns the lane each round; no other mission of this lane is open.

## Round shape
One v2 wave `kama-r50-w1`, 66 seats, validated under policy v2 with exit 0 (`.ufo/waves/round-50/w1/dispatch.json`; spec `6f3bd322`, validator exit 0 documented in `w1/validate.out`).
- Role mix: executor 22, reviewer 10, scribe 10, critic 6, connector 5, mutation-tester 4, scout 4, sentinel 3, revenger 1, simplifier 1.
- m_flash share under the live `agentModelOverrides` (executor, scribe, simplifier, revenger, sentinel; critic is `@m_kfc`): 37/66 (56%). Attack roles (reviewer, critic, mutation-tester): 20/66 (30%).
- Ready file written 2026-10-27T00:28:19Z; markers `w1.ready.partial`, then `w1.ready.dispatched`. WAVE-DONE received ("all 66 seats settled"; `.ufo/waves/round-50/w1/w1-results.json`). All 66 seats have reports (`w1/out/*.md` = 66). **Dead seats: 0.** No residual call. **Round total: 66 seats.**
- Planner seat: held by the L1 (the validator rejects `planner`); planning data-walk rode on connectors N2Couple2, N3Pattern2, N5Sources2.

## Work performed
Two claims, frozen before any build at `601c8889` (`.ufo/waves/round-50/preregistration.json`; KQ64 check `freeze/prereg-time-check.out` → `RESULT pass`, exit 0):
- **C1, operability 8→8, sourced on S496 and S497:** the witnessed replay is bound to its own process tree, its rerun receipt, a clean interpreter environment and the model bytes its server maps, and killing the invoker removes the whole tree within 30 s (round-49 closure R1, R2). Counter `tools/round50-replay-bind-audit.py`.
- **C2, calibration 7→7** (the lowest-scoring non-retired axis): append-only-audit v5 — origin is the union of section titles at every birth of a line's key (order-independent), sections ignore fenced `## ` lines, origin keys drop one trailing CR, graded+ungraded==deleted for every event (closure R3). Counter `tools/round50-append-audit-v5-check.py`.

Work items:
- **Protocol load:** `skill://godspeed`, `skill://swarm`, the round prompt, SCORECARD (§Planned round 50, §Round 49), the round-49 report and `corpus/lessons/round-49-verifier-spotcheck.md` (R1–R6), `considerthese/2026-10-26.md`; goal file run-9 blocks.
- **Source opening (2026-10-27T00:14:13Z):** `proc_pid_maps(5)` (`.ufo/waves/round-50/c1/proc_pid_maps.5.txt`), `PR_SET_PDEATHSIG(2const)` (`.ufo/waves/round-50/c1/PR_SET_PDEATHSIG.2const.txt`), CommonMark 0.31.2 §4.5 (`.ufo/waves/round-50/c2/commonmark-0.31.2-s4.5.txt`).
- **Freeze `601c8889`:** both counters, preregistration, base controls (`base.c1.out` `bind=0 teardown=0 newrow=0 bound=0/3 met=False`; `base.c2.out` `fixture=0 lane=1 scenarios=9/12 met=False`), start census (exit 0), source captures.
- **Build `97c864be`:** `--witness` isolation (`python -I`, env allow-list, preexec_fn pdeathsig; replay self-pdeathsig), `model_mapping` record and refusal, aoa v5 (birth-DAG origin, fence-aware sections, CRLF keys), S496–S498. Build-fix `3d42897b` (S498 tick parity). Dry runs at the build: C1 `bind=1 teardown=1 newrow=1 bound=3/3 met=True`; C2 `fixture=1 lane=1 scenarios=12/12 met=True`.
- **Wave spec `6f3bd322`** (`build_spec.py`; 66 items; m_flash 37/66; attack 20/66).
- **Integration (measured) `8370e39c`:** SCORECARD round-50 section, authority, calibration spot-check count 36, depth row re-anchor (SKILL 1522 lines / 38 headings / sha `33b2d628…`), SKILL `## Round-50 instrument registry` + how-to, LOG entry, lesson `round-50.md`, QUALITY KQ80–KQ84, README frontier disposition, wave evidence committed. r41/r42/gate verified green at the measured commit; end census exit 0; misroot sweep empty (`.ufo/waves/round-50/measured/misroot-sweep.out`).
- **Routed closure items:** R1+R2 → C1; R3 → C2; R4 → the four mutation seats (M1Ctr, M2Live, M3Tool, M4Ctr); R5 carried (sub-20, prerelease cliff, b11906 population); R6 operator-side (prompt route map stale; live map count used).
- **Assimilation:** pre-checks by seat X1Assimilation: 9 staged-id collisions (S330/S333-335/S346/S347/S352/S353/S363) with already-adopted lane rows → no adoption, no renumbering (quarantine-first round; verdicts per quarantine row in `X1Assimilation/quarantine-verdicts.md`; scratch-mirror census gate exit 0 once the round-50 lesson exists).
- **considerthese:** no proposal taken by name this round (T8Considerthese table updated; six proposals remain unimplemented; wave-state markers committed this round).
- **Tooling:** no installs by the L1; seats used stdlib + existing tools only. No pacman.

## Landed changes
Every hash is a `landed` line from `jj-lane.sh`; each maps to `LOG.md` §Round 50.

| Change | Lane commit |
|---|---|
| Freeze: counters, preregistration, base controls, start census, source captures | `601c8889` |
| Build: replay isolation + parent-death teardown, live model-mapping, aoa v5, S496–S498 | `97c864be` |
| Build-fix: S498 tick parity | `3d42897b` |
| Wave spec, dispatch, validation, build receipts | `6f3bd322` |
| Build regression battery receipts | `3b79eadd` |
| Integration (SCORECARD, SKILL registry, LOG, lesson, QUALITY KQ80-84, README frontier, wave evidence) | `1c030f18` |
| Integration-fix: depth row SKILL line count | `8370e39c` |
| Measured results, end census, misroot sweep | `cc80bec2` |
| Measured-fill (SCORECARD section) | `db6bfa8d` |
| R3Provenance model receipt; X1Assimilation evidence | `f0b5b27f`, `5a1e29a1` |

## Before → after measurements
- **C1 operability 8→8: met.** Command: `python3 tools/round50-replay-bind-audit.py --repo <fresh clone> --tip <commit> --scratch <dir>`. Base `26ecba64`: `bind=0 teardown=0 newrow=0 bound=0/3 met=False`, exit 1 (`controls/base.c1.out`). Measured `8370e39c`: `bind=1 teardown=1 newrow=1 bound=3/3 met=True`, exit 0 (`measured/c1.out`). Independent: R1Rerun2 (2× met at the build, met=False at base), N2Couple2 (C1 alone on the freeze tree meets), S2Gate2 (met at build on own clone). Not shown: a decoy replay that execs the host b11909 binary in place of the replay and sanitizes its environment and mapping honestly passes the counter (J4Decoy — stated limit); a host-copy binary passes (`stated limit); the loaded model bytes rewritten in place after mapping are indistinguishable; btrfs subvolumes fail closed on dev mismatch; probe code behind `tools/kama-probe.sh` resolves through the injected PATH (Sen1Env — five vectors execute inside the replay, none trip the planted marker; routed).
- **C2 calibration 7→7: met.** Command: `python3 tools/round50-append-audit-v5-check.py --repo <fresh clone> --tip <commit> --scratch <dir>`. Base: `fixture=0 lane=1 scenarios=9/12 met=False`, exit 1. Measured `8370e39c`: `fixture=1 lane=1 scenarios=12/12 met=True`, exit 0 (`measured/c2.out`); lane `ungraded_lines 89` (v4: 82), event `0718b6abbda6` ungraded 72 = natively exempt 72, event `dd9f5dc6c0e6` ungraded 17 <= 23. Independent: R2Rerun2 (2× met, byte-identical), N2Couple2, S2Gate2, V3Stable, V4Determinism. Not shown: the counter's fence parser and CR-key are not lane-exercised (0 fence/CR lines in the event parents) and the lane bound is exactly tight at the tip (M4Ctr); the sub-20 threshold hides 97 events incl. the real `LOG.md` loss at `ed135b3c` (graded at line level; X13Threshold).
- **Tip regressions at `8370e39c`:** gate `registered 46 unregistered 0 defective 0`; capability census `listed 11 observed 11 met True`; r41/r42 `mismatches=0 met=True`; r43 `registered=46 mismatches=0 met=True`; pointer `met=True`; digest-ledger `unknown=0`; `sources-append-only --from 26ecba64` exit 0; `append-only-audit` exit 0; selftests AOA 36/36, KLR 23/23, live ok, check-receipt 16 VALID/107 rejected; round-48 C2 counter exit 0; round-49 C1 counter still `met=True`; round-49 C2 counter `lane=0` (expected supersession of v4 origin). hexrun-census `unknown=1` (`f8cdb853…`, round-49 fleet report commit in the spot-check) — carried from base.

## Sources & frontier
- **Census validate** (`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kama`): start exit **0** (`.ufo/waves/round-50/census/start.out`); end exit **0** (`.ufo/waves/round-50/measured/census-end.out`). Code counts from the end receipt (`awk -F'\t' 'NF>=3 {print $2}' census-end.out | sort | uniq -c`): W01=1 W04=93 (and one `ok` line; no `E` code).
- **Row count** (`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`): **237 → 240**.
- **Rows added:** three tier-A rows, mined, opened 2026-10-27T00:14:13Z (Gate in `corpus/lessons/round-50.md`): S496 (proc_pid_maps(5)), S497 (PR_SET_PDEATHSIG(2const)), S498 (CommonMark §4.5).
- **Rows touched old→new:** none.
- **Frontier advanced:** witness bound to the replay's own process tree, clean environment and mapped model bytes; teardown covers the whole tree; append-only origin follows the commit graph (birth-DAG), fence-aware sections, CRLF-normalized keys, complete per-event accounting. Still frontier: decoy in-place exec, probe PATH execution, pid-join edges, revision-after-load indistinguishability, sub-20 deletions, prerelease cliff, b11906 population at b11909+, counter `--out` parent creation.
- **Sourced claim:** C1 rests on S496 (and S497 for the teardown mechanism); C2 rests on S498.
- **Mistakes mined:** four rows in the lesson (S498 tick parity; untracked wave markers; stale spot-check count 35; counter `--out` parent).
- **Assimilation:** first-round quarantine-first: package not appendable as shipped (9 id collisions, 90 staged rows census E01, 24 re-cites of adopted documents); quarantine slice verdicts per row — no fabrication found; adoption deferred (X1Assimilation).
- **considerthese:** latest file `2026-10-26.md` — no proposal taken by name; six numbered proposals remain unimplemented (T8Considerthese table).

## Trend verdicts
- **expansion: unchanged.** Capabilities 11 → 11; the witness binding and v5 origin are depth on held ground, not new surface; no knowledge entry added.
- **quality: improved.** The replay is now observable as the replay's own process with a clean environment and a hashed mapped model; killing the starter removes the whole tree (measured 0.10 s); append-only verdicts no longer depend on listing order, fenced content or line endings, and every deleted line is accounted for; gate, reconcilers, digest/census instruments and selftests are green at the measured tip.
- **discernment: unchanged.** The outside spot-check of the S496–S498 admits and the Gate rejects (environ-only, maps-inode-only, pdeathsig-only) is still owed; per KQ61, `improved` waits for it. The round-49 closure's R1/R2/R3 are all closed and independently re-measured (R1/R2Rerun2, N2Couple2, S2Gate2).

## SHONEN
- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources → `SKILL.md` §Round-50 instrument registry and isolated-witness how-to; gate `registered 46 unregistered 0 defective 0` (`.ufo/waves/round-50/measured/gate.int.out`). Author assertion; no non-author verifier.
- [~] At least one end-to-end domain task executed and logged in LOG.md → three isolated witnessed b11909 replays observed by the counter (`.ufo/waves/round-50/measured/c1.out`, `LOG.md` §Round 50); teardown measured (0.10 s). A seat is not a non-author mark.
- [~] Instructions executable by an agent without oral context → the SKILL how-to covers the isolated invocation, planted canaries and teardown observation; seats K1Fresh-style fresh-session runs are pending. No independent review after integration.
- [~] No cross-domain bleed (PROVINCE.md still accurate) → `PROVINCE.md` unchanged this round; sibling scan N1Overlap2 reported no overlap, not absorbed.

Open L0 questions (routed around; none filed this round): `kama | round-35` (MISSION.md axes pair), `kama | round-39` (validator band and planner), `kama | round-41..43` (parked worktree).
