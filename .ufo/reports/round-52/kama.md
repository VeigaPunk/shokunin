# kama — round 52 report

Lane: kama-shokunin (local model serving and endpoint health). L1: `KamaR52` (attempt 1; no earlier attempt of this round in `.ufo/watchdog.log`). Base `9ff76b1f763512be2f554cbbfd0b2213b63b0847`. Final lane tip `eb7b16cfa6b535d726027e338f0fb7232359a995` (pushed; `git ls-remote origin refs/heads/master` prints it).

## Round shape

One v2 wave, `kama-r52-w1`: 70 seats, validated under policy v2 (`.ufo/waves/round-52/w1/validate.out` exit=0), dispatched through the inline handoff (`w1.ready`, `w1.ready.dispatched`). Role mix: executor 21, reviewer 12, scout 10, critic 8, mutation-tester 6, scribe 5, sentinel 3, connector 3, simplifier 1, revenger 1; attack share (reviewer + critic + mutation-tester) 26/70 = 37 %. No residual call. Round total 70 seats. WAVE-DONE received from the orchestrator; `.ufo/waves/round-52/w1/w1-results.json`: 70/70 seats settled with a final output, **0 dead seats**. 66 wrote a top-level report file; S7Exempt, A1Assim, Sc3Province and K8Routed returned their findings only in their final output (recorded in the results file). M6Restore reported itself incomplete (one of six mutations exercised, killed) and V4Review incomplete against its 20-line recomputation (its sampled blocks clean). Three J5HostMemfd strace logs over 1 MiB (1.1–1.2 MB) were skipped by the lane helper and deleted from the worktree; the seat report and its committed 968 KB trace carry the finding. The §3 planner seat is held by the L1 (the validator rejects `planner`); planning data-walks rode scouts S6Limits/S7Exempt and connector N2Pattern. Routing came from the live `task.agentModelOverrides` map (seat Sen3Policy recorded config mtime `2026-10-27T02:39:08Z`, sha256 `0d587466…addc`); no `model` was passed.

## Work performed

Declared claims (frozen at `8551ba7f`, `.ufo/waves/round-52/preregistration.json`):
- **C1 — operability 8→8 (measured, sourced on S500 memfd_create(2)):** the replay's server runs from a sealed anonymous memfd the replay filled from its verified archive member stream.
- **C2 — calibration 7→7 (measured):** the A-corr append-only files hold every line they declared append-only (155 lost lines re-appended verbatim; ledger keeps only the 10 A/A-row lines), checked by a counter with its own region logic.

Work items:
- Protocol load, round-51 closure read (`corpus/lessons/round-51-verifier-spotcheck.md`), start census exit 0 (`.ufo/waves/round-52/census/start.out`).
- Freeze `8551ba7f`: counters `tools/round52-replay-memfd-audit.py` (sha256 `053ff502…21f5`) and `tools/round52-append-restore-check.py` (`29dfd886…53ea`), base controls `controls/base.c1.out` (`bind=1 sealed=0 teardown=1 newrow=0 met=False`) and `controls/base.c2.out` (`fixture=1 lane=0 corr_lost=151 met=False`); `freeze/prereg-time-check.out` → `RESULT pass`.
- Build `5dacf2c7`: `tools/kama-live-replay.py` `sealed_member()` (tar stream → memfd, hash, seals 15, `--server-fd`), `tools/kama-llamacpp-live.py` `--server-fd`/`sealed_fd()` (exec via `/proc/<pid>/fd/<n>`, `LD_LIBRARY_PATH` + cwd because ggml searches the exe dir), `server_exe` records `nlink`/`seals`; S500 row; 155 lines re-appended in 18 files under `Restored lines (round 52)`; ledger 165 → 10 rows; SKILL §Round-52 registry; hexrun rows for `39877b17` and the re-appended wrong hash `907cdcc0…c50725…`; round-51 D1 `X7Regen.md` restored to its committed bytes. Build battery clean (`.ufo/waves/round-52/measured/*-build.out`).
- Wave `kama-r52-w1` (spec commit `34d82600`): controls J1–J10 all as preregistered (C1 J1PathExec/J2Unsealed/J3CopyDecoy/J4Hardlink `sealed=0 met=False`; limit probes J5HostMemfd `met=True`, J6RenameOver `met=True`; C2 J7Prefix/J8LeaveRows/J9DropContract/J10CorrRow `lane=0 met=False`), independent reruns X1Rerun/X2Rerun/X6Rerun agree, reviews V3Review/V5Review find no counter-vs-preregistration defect (`.ufo/waves/round-52/w1/out/`).
- Integration `35e3b1dc` from wave findings: check-receipt admits `LD_LIBRARY_PATH` only in fd mode (V2Review: fd-mode receipts were INVALID); replay MFD_EXEC (S502, S4NoExec), sealed-byte re-hash, five selftest cases killing M2Replay's survivors (`integration/m2replay-survivors-killed.out`); live selftest drives `sealed_fd()` (X5Selftest), F_SEAL_EXEC refusal and launch errno (Sen1Exec); `tools/kama-probe.sh` honours `TMPDIR` (Sen2Scratch, scratch directive §7.4); SOURCES S501–S505; QUALITY KQ89–KQ93; lesson Gate/Errata/Mistakes; README frontier; LOG; SCORECARD round-52 section, banner, Planned (round 53).
- Measurement at `35e3b1dc` (`.ufo/waves/round-52/measured/*.out`), results commit `ade21a45`, pointer receipt at `ade21a45` (`measured/pointer-results.out`, `met=True`).
- Routed round-51 defects: D1 (X7Regen restored; report filed after WAVE-DONE), D2 corrected — **51 of 66 seat reports at filing, 15 running** (not 50/16), D3 receipt `.ufo/waves/round-52/d3/pointer-1ab1de39.out` (`met=True`), D4 scope (X7Regen matched 142 of 165 rows, the whole-file-graded slice), D5 → the two claims, D6 flip conditions, D7 KQ89/KQ90 — all in `corpus/lessons/round-52.md` §Errata.

## Landed changes

| Commit | What | LOG.md entry |
|---|---|---|
| `8551ba7f` | freeze: preregistration, counters, base controls, start census, S500 text copy | LOG §Round 52 (freeze bullet) |
| `5dacf2c7` | build (C1 memfd replay, C2 restoration, SKILL registry, re-anchors, hexrun rows, D1) | LOG §Round 52 (C1, C2 bullets) |
| `34d82600` | wave spec (70 seats) and build battery receipts | LOG §Round 52 (wave bullet) |
| `35e3b1dc` | integration (hardening, sources, QUALITY, lesson, README, LOG, SCORECARD) — measured commit | LOG §Round 52 (integration bullet) |
| `ade21a45` | measured results, receipts, wave markers, seat outputs in hand | LOG §Round 52 (measurement pointer) |
| `eb7b16cf` | wave results record, late seat outputs, end census, pointer receipt | LOG §Round 52 |

## Before → after measurements

- **C1** — `python3 tools/round52-replay-memfd-audit.py --repo <lane clone> --tip <full commit> --scratch <dir> --out <receipt>`: base `9ff76b1f` `bind=1 sealed=0 teardown=1 newrow=0 bound=3/3 sealedruns=0/3 met=False` (exit 1) → measured `35e3b1dc` `bind=1 sealed=1 teardown=1 newrow=1 bound=3/3 sealedruns=3/3 met=True` (exit 0) (`.ufo/waves/round-52/measured/c1.out`). Verdict: **verified** on the frozen predicate. Limits: a memfd filled from the host's byte-identical install meets (J5HostMemfd, preregistered); libraries and the model still load by path (K2Design).
- **C2** — `python3 tools/round52-append-restore-check.py --repo <lane clone> --tip <full commit> --scratch <dir> --out <receipt>`: base `fixture=1 lane=0 scenarios=8/8 corr_lost=151 row_lost=10 disclosed=165 met=False` (exit 1) → measured `35e3b1dc` `fixture=1 lane=1 scenarios=8/8 corr_lost=0 row_lost=10 disclosed=10 met=True` (exit 0) (`.ufo/waves/round-52/measured/c2.out`). Verdict: **verified** on the frozen predicate. Limits: byte retention, not visibility (K4Cheat: an HTML comment passes); simpler `exempt=` rule (4 SCORECARD lines, L2Slice); fixtures kill 2 of 8 tool mutants (M5Fixtures); `corr_lost` counts contract-graded lines, not every append-only sentence (K7Calib).
- No axis harmed: SCORECARD scores unchanged (8/8/7/9/7/7), capabilities 11 → 11, full regression battery clean at `35e3b1dc`. The round-51 C1 counter now reads `own=0` (`measured/r51c1.out`): its path binding is superseded by the memfd binding (seats R1Old, K5Harm judged it supersession). The round-51 decision to disclose the `ed135b3c` LOG loss is reversed (restored as retracted history; lesson §Gate decision with flip condition) — reported for the operator to rule.

## Sources & frontier

- Census command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kama` — start exit 0 (`census/start.out`, 94 W04, 1 W01), end exit 0 (`census/end.out`, 94 W04, 1 W01, 0 E).
- Rows: **240 → 246** (`git show <rev>:corpus/SOURCES.md | grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'` at `9ff76b1f` → 240, at `ade21a45` → 246). Added by tier: A 6 — S500 (memfd_create(2), mined), S501 (F_GET_SEALS(2const), mined), S502 (kernel mfd_noexec, mined), S503 (fexecve(3), rejected), S504 (execveat(2), rejected), S505 (ggml-backend-reg.cpp b11909, rejected). Rows touched old→new: none. Gate: `corpus/lessons/round-52.md` §Gate (URLs, access times, located quotes).
- Sourced claim: C1 rests on S500 (opened this round, cited by the counter's `newrow` leg and the lesson).
- Frontier advanced: replay server image on disk → held (memfd); A-corr lost lines → held; still frontier: verifier-owned server bytes, library/model mapping identity, vm.memfd_noexec=2 hosts (`corpus/README.md` §Frontier disposition — round 52).
- Mined mistakes: 9 rows in `corpus/lessons/round-52.md` §Mistakes (each with captured-by and a fix shown able to fail).
- Assimilation: none — this round's claims were frozen on routed defects; seat A1Assim's reconnaissance of `merge/kama/` returned "Assimilation: none" with an id-collision count of 9 against the staged package (S330, S333–S335, S346, S347, S352, S353, S363); nothing was appended from shokuknow. considerthese: `considerthese/2026-10-26.md` proposal 1 (flag deletions in append-only files) is carried into C2's restoration and cited by KQ89 (seat N3Consider).

## Trend verdicts

- **expansion: unchanged** — no new `corpus/knowledge/` entry; capabilities 11 → 11; new source rows are mechanism grounding, not coverage ground.
- **quality: improved** — the replay's server identity moved from a path to a sealed anonymous image (C1, re-measured, base fails); 155 lost lines restored and the ledger reduced to genuine A/A-row losses (C2); receipt-checker, probe-scratch and selftest defects found by the wave fixed with fail-capable evidence; no admitted entry failed a re-check.
- **discernment: unprovable-but-better** — 3 admits and 3 rejects (plus control-grounded rejects) recorded with quotes and flips; QUALITY KQ89–KQ93 each cite a lesson (closing D7); the outside spot-check of this round is pending, so no `improved` is claimed.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources → `SKILL.md` §Round-52 instrument registry and "Reading the sealed server and the restored lines"; gate `registered 50 unregistered 0 defective 0` (`.ufo/waves/round-52/measured/gate.out`). Author assertion; no non-author verifier.
- [~] At least one end-to-end domain task executed and logged in LOG.md → three witnessed b11909 replays whose servers run from the replay's sealed memfd (`.ufo/waves/round-52/measured/c1.out`; `LOG.md` §Round 52). A seat is not a non-author mark.
- [~] Instructions executable by an agent without oral context → seat X4Fresh replayed receipt-2 from the docstring and `--help` (`match=true`, own memfd recorded) but needed lane-tree siblings the docstring does not mention (`.ufo/waves/round-52/w1/out/X4Fresh.md`). A seat is not a non-author mark.
- [~] No cross-domain bleed (PROVINCE.md still accurate) → `PROVINCE.md` unchanged this round; seat Sc3Province: the memfd exec and append-only restoration surfaces sit inside the province as written (serving runtime/tool surfaces); seat N1Overlap: 16 sibling touchpoints reported, none absorbed. A seat is not a non-author mark.

## Extras

- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
- Tool installs: none (pacman paused; nothing needed).
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` → empty at 2026-10-27T05:39Z; no misroot. One seat (K5Harm) wrote 23 receipts into the L1's `measured/` dir; moved into its out dir (lesson Mistakes #7).
- Open L0 questions (carried, not answered): planner seat under the policy-v2 validator (`kama | round-39`), MISSION axes pair (`kama | round-35`), parked worktree (`kama | round-41..43`). New: whether withdrawn operator canon may be held as restored history (lesson §Gate decision) — routed in this report, no new L0 line.
- Scratch: `/fast/scratch/hyaku/kama-r52` removed after landing.
