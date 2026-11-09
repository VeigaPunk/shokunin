# souji — round 99 (attempt 1)

Lane repo `souji-shokunin`, lane base `c94d678c8a76f3f87f73b49a11a9d4e2aff73e3b`, lane tip at filing `5c47055e30e51f7ecf5ebe0ab7655b3bfd81fd37` (pushed; `git ls-remote origin refs/heads/master` matches). L1 `SoujiR99`. Lesson `corpus/lessons/round-99.md`. Plan `plans/round-99.md`.

## Work performed

**Declared claims (2; both on distinct axes):**

- **C1 — calibration 7 (lowest-scoring owned axis; Q173, Q178).** The declared-exit shape table's kind labels are read from the L1-frozen file `census/round-99/shapes.tsv`, pinned by sha256, and the r98 object-keyed latch hook is unchanged. Verdict: **admitted-candidate**, pending the non-author closure (the pin amendment A99.1 was filed after seats scored; disclosed in the plan and the lesson).
- **C2 — operability 8 (Q174–Q177).** The arms counter reaps only the spawn pid and its ppid-chain descendants (branch (c) removed). Verdict: **harmed (trade); not admitted.** Its decoy predicate is met, but the T1 setsid escapee is no longer reaped. The frozen predicate does not measure that leg.

**Wave (one v1 wave, `w1`, 14 seats; policy band 8–16):** 5 executor (ExecC1, ExecC1b, ExecC2, ExecC2b, ExecCensus), 2 reviewer, 1 critic, 2 mutation-tester, 1 sentinel, 1 connector, 1 scout, 1 scribe. Attack seats (reviewer, critic, mutation-tester) = 5/14 = 36 %; connector 1; sentinel 1. Dead seats: 0 (`census/round-99/wave-evidence/w1-results.json`: 14 seats with output; R99Scribe returned an empty `error` field and its report file is present). Residual calls: none. Wave shape: validated by `ufo-swarm-wave.mjs plan` rc 0 and rendered by `run` rc 0; spawned 14/14 (`inline-dispatcher.log`: `spawned souji 99 w1 14`).

**Work items with evidence:**

1. **C1 freeze runner.** `census/round-99/declared-shapes.py` reads the shapes from `--freeze`, prints `FREEZE sha256=`, refuses rc 2 on a hash that differs from `--expect-sha256`, and refuses a row count other than 17 with distinct names (A99.1). Evidence: seat `ExecC1` (`.ufo/waves/round-99/w1/R99ExecC1.md`, relabel → `mismatched=3`); reviewer `R99Reviewer1` (duplicate row `shapes=18 mismatched=0`, missing row `shapes=16 mismatched=0` on the unpinned runner).
2. **C1 measurement (L1, committed).** `census/round-99/records/c1-r99.txt`:
   - M1 pinned file + r98 hook: `SHAPES-SUMMARY shapes=17 mismatched=0`, EXIT 0.
   - M2 relabelled copy, pin enforced: `SHAPES-FATAL … != pinned 8bc642c4…a8a14`, EXIT 2.
   - M3 relabelled copy with its own hash (no pin): `shapes=17 mismatched=3` (q1o, q1q, q1i), EXIT 1.
   - Controls on the pinned file: r95 hook `mismatched=3` (t1, t4, q1i), EXIT 1; r97 hook `mismatched=3` (q1o, q1q, q1i), EXIT 1.
3. **C1 population no-harm.** `census/round-99/c1-survivor-search.py` is a byte copy of the r98 search (sha256 `e8ba780a…`, verified by `R99MutC1`), so the 278-mutant verdicts are unchanged by construction; seat `R99ExecCensus` reports the population run (`wave-evidence/w1/R99ExecCensus.md`).
4. **C2 counter.** `census/round-99/c2-setup-arms.py`: `_reap_owned` keeps only (a) the spawn pid (starttime-verified) and (b) ppid-chain descendants. Branch (c) (`elif _is_descendant(pid, os.getpid())`) is removed (grep: no `os.getpid()` ownership line). Evidence: `ExecC2` (`R99ExecC2.md`).
5. **C2 decoy and do-nothing (L1, committed).** `census/round-99/records/c2-decoy-{r99,r98,r97,cm8}.txt`:
   - r99 counter: `DECOY-PLANTED n=83 dead=0 alive=83`, `DECOY-SUMMARY verdict=spared`, EXIT 0.
   - r98 counter: `dead=0 alive=83`, `verdict=spared`, EXIT 0.
   - r97 counter (argv-only): `dead=60 alive=23`, `verdict=killed`, EXIT 1.
   - CM8 argv-only mutant: `dead=82 alive=1`, `verdict=killed`, EXIT 1.
6. **C2 escapee measurement (L1, committed; the decisive leg).** `census/round-99/records/c2-escapee-r99.txt` (live-process count with each run's own T1 token after the counter exits):
   - r99: `ESCAPEE-ALIVE run=r99 alive=1` (pid 3122349, state S, ppid 1525).
   - r98: `alive=0`. r97: `alive=0`.
   - Superseded lines: `census/round-99/records/c2-counter-*.txt` contain an `ESCAPEE-ALIVE alive=0` line from a doubled-path bug in my first script (M12); `records/c2-escapee-NOTE.txt` supersedes them. The script is fixed in `census/round-99/c2-measure.sh`.
7. **Cross-arm probe (seat `ExecC2b`, `Sentinel`, `MutC2`).** Clean runs spare a counter-descendant carrier outside the spawn chain (MutC2 pristine: `CROSS-ARM-PLANTED n=30 dead=0 alive=30`, `verdict=spared`). Critic (R99Critic) reports 3 of 4 runs confounded by concurrent decoy storms (M11); those runs are not cited.
8. **Mutation of the C2 counter (`R99MutC2.md`).** Restoring branch (c) is killed by the cross-arm probe only (`planted-killed 32`, `verdict=killed`). `m_noppid`, `m_nosttime` and `m_spawnonly` survive both decoy and cross-arm predicates; `m_noppid` is the escapee-reap loss, and no frozen predicate measures it.
9. **Sentinel safety review (`R99Sentinel.md`).** Zero positive-pid `kill()` calls by the r99 counter (strace ground truth). Foreign carriers (token-in-argv, reparented, cross-arm) spared; r98 and r97 overkill under the same harness (positive control). FINDING 1 (HIGH, operability): the T1 escapee is not reaped; it is a live orphan under the counter. Sentinel's mechanism matches ours: `PR_SET_CHILD_SUBREAPER` is not inherited across fork, so the escapee's parent is the counter. FINDING 2 (MEDIUM): the escapee holds the fixture pipes after the counter exits. FINDING 3 (LOW): `_reap_by_identity` is dead with a stale docstring. FINDING 4 (LOW, carried from r97): the /tmp guard is prefix-only. FINDING 5: no counter writes under /tmp regardless of TMPDIR.
10. **C2 reviewer and critic.** `R99Reviewer2.md` F1–F3: "starttime verified" holds only for the spawn pid; "kills only … descendants" is true only for the T1 `_reap_owned` path; the escapee is provably not spawn-chain reachable. `R99Critic.md`: the wording matches the code; the under-kill direction is a falsified implied claim.
11. **Scout re-verification (`R99ScoutSources.md`).** S075 (`proc_pid_stat(5)`; "The time the process started after system boot." occurrence 1), S368 (setsid(2); occurrence 1), S372 (sys.monitoring RERAISE; occurrence 1): each live fetch HTTP 200, byte-identical to its committed capture, each quote occurring exactly once.
12. **Pre-file falsification ledger.** `.ufo/waves/round-99/claim-falsification.tsv` (11 rows; every attack seat appears; narrowing pointers `plans/round-99.md A99.1` and `A99.2`). `claims.json` written. Gate run: see the Landed changes section and the final line below.
13. **Misroot repair (fleet-root sweep).** The plan was first written to the fleet root (`plans/round-99.md`, 4595 bytes); the lane amendments were in a separate lane file (2870 bytes). Concatenated byte-exact (verified with `cmp`/`head -c`), committed as `118e5b7d`, and the fleet copy deleted (lesson M13).

## Landed changes

Each change is tied to the LOG entry `LOG.md` `## Round 99` and to the commit that carries it (lane branch `master`):

| change | LOG.md | commit |
|---|---|---|
| C1 freeze file, pinned runner, C1 receipts, C2 counter, decoy/cross-arm/escapee receipts, wave evidence, plan, lesson, SCORECARD r99 + planned r100, QUALITY Q177/Q178 | `## Round 99` | `d31c07d6` (code and records; plan amendments only) |
| wave evidence: `w1-results.json`, final seat reports, MANIFEST | `## Round 99` (evidence) | `183dd640` |
| full plan restored (fleet misroot repaired) | `## Round 99` (M13) | `118e5b7d` |
| lesson M13 (misroot) | `## Round 99` | `d54b6c1c` |
| claim-falsification ledger header removed (gate pass) and wave-evidence manifest | `## Round 99` (evidence) | `5c47055e` (lane tip at filing) |

Fleet-root commits: this report and the L0 question, via `fleet-commit.sh --as souji` (below).

## Before → after measurements

Counting commands are pasted above; each row carries its commit (`measured against`).

| claim | before | after | counting command | measured against |
|---|---|---|---|---|
| C1 binding of shape labels | r98 runner with hard-coded labels: relabelling q1o/q1q/q1i reaches `mismatched=0` (r98 M6 receipt `.ufo/waves/round-98/w1/R98Scribe/repro/do-nothing-control-movability.py`) | pinned file: M1 `shapes=17 mismatched=0` EXIT 0; M2 refused EXIT 2; M3 unpinned relabel `mismatched=3` EXIT 1 | `python3 -B census/round-99/declared-shapes.py --freeze census/round-99/shapes.tsv --expect-sha256 8bc642c44e0c1f6414fb4b07aaf922c01bf2d2ea8b91bda7bac81f60a05a8a14 --search census/round-98/c1-survivor-search.py --scripts census/round-98/shapes --work <empty>` | `d31c07d6` (records `census/round-99/records/c1-r99.txt`) |
| C1 do-nothing controls | — | r95 `mismatched=3`, r97 `mismatched=3` on the pinned file | same, with `--search census/round-98/controls/c1-r95-search.py` and `…/c1-r97-search.py` | `d31c07d6` |
| C2 decoy spared (safety) | r98 counter: `verdict=spared`, dead 0 / alive 83 | r99 counter: `verdict=spared`, dead 0 / alive 83 | `python3 -B census/round-99/c2-decoy-test.py --counter census/round-99/c2-setup-arms.py --probe census/round-98/c2-forgery-probe.py --tool tools/souji-record-agreement.py --before census/round-92/controls/c2-before-tool.py --work <empty> --arm-timeout 200 --plant-delay 2` | `d31c07d6` (`records/c2-decoy-r99.txt`) |
| C2 do-nothing (r97 argv-only) and CM8 | r97 `verdict=killed` (dead 60); CM8 `verdict=killed` (dead 82) | unchanged (do-nothing red as frozen) | same, `--counter census/round-97/c2-setup-arms.py` / `census/round-98/c2-cm8-mutant.py` | `d31c07d6` |
| C2 escapee reap (operability) | r98 counter: `ESCAPEE-ALIVE alive=0` | r99 counter: `alive=1` (harm) | `bash census/round-99/c2-escapee-check.sh <scratch-root>` | `d31c07d6` (`records/c2-escapee-r99.txt`) |
| C2 cross-arm carrier | r98: killed (branch (c); Sentinel r98 receipts) | r99: spared 30/30 (MutC2 pristine) | `python3 -B census/round-99/c2-cross-arm-probe.py …` (seat-run; see `R99ExecC2b.md`) | `d31c07d6` |

Verdicts from the table: C1 **improved** (movable → refused; binding measured); C2 **harmed** (the reap leg is lost; the safety leg is unchanged on the decoy).

## Sources & frontier

- `corpus/SOURCES.md` before and after: **294 → 294 rows** (`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`). Census before: `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin souji` EXIT 0 at round start; EXIT 0 at round end (`ok …corpus/SOURCES.md`). Malformed-row and duplicate-id checks: unchanged (no row written).
- Rows added: none. Rows touched (status, recheck, used-by): none. Re-verified this round: S372 (C1's latch), S075 (C2's starttime field), S368 (setsid new group), each live and byte-identical to its committed capture.
- Frontier: F5 (process residue; reap authority) advanced by the escapee measurement and by the routed r100 successor; F1–F4 unchanged. Knowledge entries: none touched (the lesson carries the Gate).
- Assimilation: none (no `merge/souji/` theme taken). considerthese: the lane has no `considerthese/` directory.

## Trend verdicts

- **expansion: unchanged.** No registry row added; the knowledge base gained no entry on new ground.
- **quality: improved.** C1 makes the calibration input a pinned file and refuses the relabel attack that r98's do-nothing control passed (Q178, lesson M9). C2's measured regression is recorded as a harm, not a gain.
- **discernment: harmed.** The pre-freeze gate did not catch the unpinned freeze hash (M9, found by Reviewer1) or the spawn-chain escapee assumption (M10, found by Sentinel, Reviewer2, MutC2 and our own escapee measurement). M11 is a measured confound and M12 and M13 are L1-authored defects, caught in-round.

## SHONEN

Count: `grep -c '^## SHONEN' <this report>` = 1. SHONEN.md boxes were not touched in r99; each pointer below was re-resolved.

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — SKILL.md Gate registry; corpus/SOURCES.md S100–S103; corpus/lessons/round-21.md Gate
- [~] At least one end-to-end domain task executed and logged in LOG.md — LOG.md:362 (2026-10-19 operator sweep)
- [~] Instructions executable by an agent without oral context — census/round-21/run-acceptance.py; census/round-21/accepted-matrix.json
- [~] No cross-domain bleed (PROVINCE.md still accurate) — PROVINCE.md Round21 privacy boundary; .ufo/waves/round-21/w1/ConnSiblingOverlap.md; corpus/lessons/round-21.md Boundaries

## Stale-lane, tools, L0

- Stale-lane: the lane is a respawn-per-round driver lane; no other mission of this lane is open.
- Tool installs: none in this round.
- L0 question: appended to `.ufo/l0-questions.md` (C2 escapee reap authority; see below).
- Open limits: (a) C2 escapee leak (routed r100); (b) the escapee holds the fixture pipes after the counter exits (Sentinel FINDING 2); (c) the /tmp guard is prefix-only (Sentinel FINDING 4, r97 carry); (d) M11 cross-arm runs need a quiet-host gate.
- Pre-file falsification gate (run at filing, after the ledger header fix): `PREFILE-FALSIFICATION: pass claims=2 rows=11 attack_seats=7 findings=0` — exit 0.
