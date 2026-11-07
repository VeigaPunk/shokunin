# souji — round 81 report (L1 SoujiR81, attempt 1)

Lane repo `/home/vgpnk/Projects/shokunin/souji-shokunin`, branch `master`. Base `b15279bbc3f11ec10fc375a05a08b19cac460d0c` (r80 closed `admitted`, spot-check committed). Preregistration `census/round-81/preregistration.txt` (frozen at F `0b1aeaf1c1bb11605bb9e139116323f5680b1a1c`; freeze-check `--substance --chronology` `SUMMARY claims=2 findings=0`, `census/round-81/records/freeze-check-at-F.txt`).

## Work performed

Declared claims (two, causally separable; S81Connector: SEPARABLE — no C1 receipt binds a vault-tool byte, no C2 receipt binds a C1 counter byte):

- **C1 — calibration (the lowest owned axis, 7):** a successor pointer counter `census/round-81/c1-pointer-counter.py` binds a MOVED target under the capture root `census/round-<N>` to a wave capture subtree (`waves/`, `wave/`, `records/wave-<w>/`) that keeps a whole-component suffix of the token's own path — the shape of all 14 real MOVED rows of the r77/r78 ledgers. It refuses the r80 wave's NF12 decoy and two siblings and keeps three true captures. Frozen 25-row harness: **accepted 3 → 0, refused_true 0, mismatches 3 → 0, EXIT=0**.
- **C2 — operability (sourced on S329, opened this round):** `tools/souji-vault-verify.sh` runs its advisory Obsidian CLI call (the tool's only `timeout` child, base line 213, S80Connector MEDIUM) as an asynchronous job with the caller's stdin kept by `<&0` (S329), traps TERM/INT/HUP while it waits, kills timeout's group and exits 128 + n with a stderr line. Frozen 12-row counter: **mismatches 8 → 0, orphans 8 → 0, EXIT=0** at W2; launch-qualified (below).

Work items:

- Protocol load; r80 spot-check routed defects 1-7 and r80 lesson routes (a)-(d) dispositioned in `corpus/lessons/round-81.md` `## Inherited` (defect 1 as verification V1; 2 and 5 by `census/round-81/rec.sh`, which binds the executed bytes with mode; 4 by registry repairs; 6 NF12 as C1; 7 by lesson note; `_regular` pathspec, intro-blob row, fork-tail row carried by name).
- Pre-freeze feasibility (Q70) in scratch: `census/round-81/records/prefreeze/` (C1 draft = committed counter minus docstring lines 13-15; C2 draft byte-equal to W2; a pid-only kill draft also scores 12/0, disclosed).
- P `804f132ef717d96157c107e219a254286644b706`: harness + 25-row population, C2 counter + 12-row population, control variants and receipts, rec.sh r81, S329 capture and row, lesson Inherited/Gate, census-before, registry base, prefreeze and V1 receipts.
- F `0b1aeaf1c1bb11605bb9e139116323f5680b1a1c`: preregistration. W1 `308bc77bddc725aa8f302e4f62746bde3f843f56` (C1 counter, sha256 `ca97b984…`). W2 `7076ed2d12faf82e9c762f49d627b84ae549fbd1` (C2 tool, blob `ba61e912…`). A `cb14eae71c02d51d2e071628ac4c882f01daf844` (after-arms).
- I `f6f699de6321defe135d1f15e5cb4547fc2857ce`, I2 `c25f000fc7387f0da524282dcd74ede81a4e72b7`: knowledge r81 section, SKILL r81 gate rows and vault exit codes, QUALITY Q146/Q147, SOURCES used-by repairs, README/LOG/SCORECARD, lesson Measured/Registry/Mistakes, launch receipts, M2 diagnosis.
- V1 (verification, not a claim): the r80 quarantine front at base re-measured — frozen r80 counter 15/15 (also SHELLOPTS=monitor), three repair probes green (`census/round-81/records/v1-quarantine/`); S81ExecV1 saw one monitor-mode flake (1 in 7), routed.
- Wave w1 (13 seats, 0 dead) → probe D `398e568cb0389093b3298e68e185827c45978dd0` (fails 3/3 at W2) → repair R `ef76a14f77bde593b5a1adf47772ad8b192feb7d` and receipts `0e25024b3279c3edf6912816ada5bdf6ed267dea`; wave mirror and integration `10362d2632da4f85a9b407465f1133c2ee98d866`; census-after `492da800c92d703ce1011b75d219dbb77970a545`.
- Domain trial (C2 conjunct, real lane bytes): base and candidate over PROVINCE.md, `census/round-80/records/wave-w1`, `err4.nl2` in one layout, identical, 3/3 verdicts (`census/round-81/records/c2-domain-trial.txt`; at R `records/repair/domain-trial-at-R.txt`). The real ledger is empty, so it reaches only `cli=unavailable` (stated); S81ExecC2 added a real-bytes trial reaching cli_claim, byte-identical over 5 CLI states.

## Landed changes

Every change is tied to LOG.md `## Round 81` and to the commit that carries it.

| change | commit |
|---|---|
| instruments, populations, control variants and receipts, rec.sh, S329 row/capture, lesson start, census-before, registry base, prefreeze, V1 | `804f132ef717d96157c107e219a254286644b706` |
| preregistration | `0b1aeaf1c1bb11605bb9e139116323f5680b1a1c` |
| C1 counter (+ freeze-check receipt) | `308bc77bddc725aa8f302e4f62746bde3f843f56` |
| C2 tool | `7076ed2d12faf82e9c762f49d627b84ae549fbd1` |
| after-arms, regressions, domain trial, refuses-empty negative | `cb14eae71c02d51d2e071628ac4c882f01daf844` |
| knowledge, SKILL rows, QUALITY Q146/Q147, SOURCES used-by repairs (S062 S110 S251 S298 S321), wave spec | `f6f699de6321defe135d1f15e5cb4547fc2857ce` |
| lesson Measured/Registry/Mistakes, launch receipts (M4), M2 diagnosis, README/LOG/SCORECARD | `c25f000fc7387f0da524282dcd74ede81a4e72b7` |
| probe D failing at W2 (vault-path write), SKILL wording | `398e568cb0389093b3298e68e185827c45978dd0` |
| repair R (`cli_tmp_ok`) | `ef76a14f77bde593b5a1adf47772ad8b192feb7d` |
| R receipts; QUALITY Q146/Q147 refined | `0e25024b3279c3edf6912816ada5bdf6ed267dea` |
| wave mirror, lesson Wave/Repairs/Routed, SCORECARD r81 done / r82 planned | `10362d2632da4f85a9b407465f1133c2ee98d866` |
| census-after, registry at tip | `492da800c92d703ce1011b75d219dbb77970a545` |

## Before → after measurements

| claim | before | after | counting command | measured commit |
|---|---|---|---|---|
| C1 | `census/round-81/controls/c1-K-a-r80-counter.txt`: `SUMMARY rows=25 mismatches=3 accepted=3 refused_true=0 errors=0`, EXIT=1 (NF12, NF12c, NF12d) | `census/round-81/records/c1-after.txt`: `rows=25 mismatches=0 accepted=0 refused_true=0 errors=0`, EXIT=0; K-b refuse-all refused_true=3, K-c without-suffix accepted=1; r78 22/22 + 12/12, r77 35/35 + 7/7, r79 harness 9/9, r80 harness 18/18 | `python3 -B census/round-81/c1-false-row-harness.py --counter census/round-81/c1-pointer-counter.py --lane LANE --fleet-root FLEET --work WORK` | `308bc77bddc725aa8f302e4f62746bde3f843f56` |
| C2 | `census/round-81/controls/c2-K-a-do-nothing.txt` (base blob `5cb0fb13…`): `SUMMARY rows=12 mismatches=8 errors=0 orphans=8`, EXIT=1 | `census/round-81/records/c2-after.txt`: `rows=12 mismatches=0 errors=0 orphans=0`, EXIT=0; K-b 8/8, K-c p3 `cli=empty`; selftest 57/0, r17 37/0/0, trial identical 3/3 | `python3 -B census/round-81/c2-vault-signal-counter.py --tool FILE --work WORK` | `7076ed2d12faf82e9c762f49d627b84ae549fbd1` (blob `ba61e912…`); at R `ef76a14f` (`records/repair/c2-at-R.txt` 12/0/0) |

**C1** — verified on its frozen predicate; reproduced by S81ExecC1, S81Reviewer, S81CriticClaims, S81MutCounter, S81Scribe. Qualifications: the suffix binding's only pressure is NF12c, and NF12c/NF12d falseness is stipulated by the L1 (S81CriticClaims); mutants M7 and M8 survive (M8 reopens decoys under `records/<non-wave>/`); a byte-equal decoy in the token's **own** round tree (`.ufo/waves/round-32/decoy/…`) is accepted — the rule never runs there (S81MutCounter MEDIUM); the prereg's stated-limit example is in fact refused (its true instance is a partial-suffix decoy). Routed to r82.

**C2** — verified on its frozen predicate at W2 under the default and `&` launches (S81ExecC2, S81ExecEvade, S81Reviewer, S81CriticClaims, S81MutTool). Qualifications the closure must rule on:
- **Launch-dependent:** under `env SHELLOPTS=monitor` the frozen counter at W2 reads `mismatches=2 orphans=2` (v7/v8: the CLI stub's own job-controlled grandchild leaves timeout's group; `census/round-81/records/launch/c2-at-W2-monitor.txt`; lesson M4, found by the L1 and independently by S81ExecC2, rated HIGH there). Base under the same launch: 8 mismatches, 8 orphans (`launch/c2-K-a-base-monitor.txt`) — a residual within the prereg's stated limit class, not a harm against base. Not repaired; routed (descendant-tree kill).
- **Harm at W2, repaired:** the private CLI output file was written under a vault path when TMPDIR sat inside/at/above the vault (S81Sentinel LOW-1, S81ExecEvade), breaking the tool's own rail "Nothing is ever written under a vault path". Probe D fails 3 of 4 arms at W2 in 3 of 3 runs, 4/4 at base; R `ef76a14f` runs the call in the foreground in that configuration; at R probe D 4/4 ×3, frozen counter 12/0/0, selftest 57/0, r17 37/0/0, trial identical; S81ExecEvade re-ran the counter at R (12/0/0). The R bytes were attacked only by the two seats asked after the repair (S81ExecEvade, S81MutTool: N1/N3 mutants survive probe D, two arms missing).
- Unmeasured branches: the KILL fallback (M03) and the post-call trap reset (M05) survive the frozen rows (S81MutTool); the group kill is equivalent to a pid kill on every row (S326; lesson M3).

No owned axis score changed (calibration 7, coverage 8, operability 8).

## Sources & frontier

- **Census.** Command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin souji`.
  - Before: `census/round-81/records/census-before.txt`, `souji ok`, EXIT=0 (87 W04 lines). The receipt binds the census script's own digest (r80 defect 5).
  - After: `census/round-81/records/census-after.txt`, `souji ok`, EXIT=0.
- **Rows** (`grep -cE '^ {0,3}\| *S[0-9]{3,}' corpus/SOURCES.md`): 251 → 252.
  - Added: tier A ×1 — S329 GNU Bash 5.3 manual, node 3.2.4 Lists of Commands, as installed (bash 5.3.20-1; sha256 equal to the r79 capture; excerpt `census/round-81/srcs/bash.info-5.3-Lists.txt`; `mined`; grounds C2's `<&0`). Located quote (17 words) and access date 2026-11-07 in `corpus/lessons/round-81.md` Gate. Not a duplicate of S325 (S81ScoutSources, S81CriticDiscern agree).
  - Rows touched old→new (used-by only, each citing entry re-read): S062, S110, S251, S298, S321 (lesson Gate lists each old→new). Registry agreement (`tools/souji-registry-agreement.py`): K1 7 → 1 (`records/registry-agreement-base.txt` → `registry-agreement-at-10362d26.txt`); K1 S146 (provenance prose, not a citation) and K2 SCORECARD rewrite recorded accepted-red with reasons.
- **Frontier advanced.** README "Frontier (r81 vault CLI signal handling and the r80 wave's census decoy)"; knowledge `corpus/knowledge/gate-signal-handling.md` r81 section (cites S329); QUALITY Q146, Q147.
- **Mistakes mined:** four (`corpus/lessons/round-81.md` `## Mistakes` M1-M4): M1 a pipe in a registry cell (census E01 fired), M2 the counter's first parse (diagnosis receipt `records/diagnosis-m2-first-parse-at-base.txt`, EXIT=1 — shown able to fail), M3 unmeasured kill branches, M4 the launch-mode residual.
- **Sourced claim:** C2 rests on S329 (opened this round).
- **Assimilation: none.** `considerthese/` is absent in this lane; no `merge/souji/` theme fits the frozen claims.

## Trend verdicts

- **expansion: improved** — one mined tier-A row on ground the lane did not hold (asynchronous-command stdin), a knowledge section on the async-job pattern for a single bounded call, QUALITY Q146/Q147, two closure-gated capability rows, a reusable vault signal counter and a vault-rail probe.
- **quality: unprovable-but-better** — the vault tool no longer leaves its CLI running on a caller's signal (8 → 0 orphan rows at W2 and R), five registry used-by cells now match their citations (K1 7 → 1), and a wave-found rail harm was repaired behind a failing-first probe; but C2 is launch-dependent (2 orphan rows under SHELLOPTS=monitor), two kill branches are unmeasured, and C1's discriminating rows are L1-built. No single counter carries the net; the operator rules.
- **discernment: improved** — the L1 found M4 itself before the wave reported it, kept the defective first parse as a diagnosis that fails, applied five non-author corrections (quote count, carried items, draft identity, limit wording, id-reuse note), disclosed that a pid-only kill scores the same, and refused to repair probe-less LOWs (stale `$!`, reopen-by-name) without a failing probe.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources. Evidence: SKILL.md gate rows "r81 false-ledger-row harness (C1)" and "r81 vault CLI signal counter (C2)" and the souji-vault-verify exit-code row (`f6f699de`, `398e568c`).
- [~] At least one end-to-end domain task executed and logged in LOG.md. Evidence: LOG.md `## Round 81` — the vault tool over three real lane targets, base vs candidate byte-identical (`census/round-81/records/c2-domain-trial.txt`, `records/repair/domain-trial-at-R.txt`).
- [~] Instructions executable by an agent without oral context. Evidence: thirteen seats re-ran the prereg commands as written and reproduced the receipts (`.ufo/waves/round-81/w1/S81ExecC1.md`, `S81ExecC2.md`, `S81Reviewer.md`).
- [~] No cross-domain bleed (PROVINCE.md still accurate). Evidence: sibling tools documented, not edited (`.ufo/waves/round-81/w1/S81Connector.md` item 3); PROVINCE.md unchanged; misroot sweep found no file of this lane.

## Other

- **Round shape:** one v1 wave `w1` of 13 seats, validated under `ufo-wave-policy.json` (band 8-16; spawn 13), dispatched via the inline handoff (`w1.ready` 06:21:57, `w1.ready.dispatched` 06:29:32 after queueing for fleet slots). WAVE-DONE received (`w1-results.json`, 13 results). No residual call; round total 13. The L1 holds the §3 planner seat.
  - Role mix: connector 1, scout 1, executor 4, mutation-tester 2, reviewer 1, critic 2, sentinel 1, scribe 1. Attack seats 5 of 13 (38 %).
- **Dead seats:** 0. After the repair the L1 messaged two of its own seats (S81ExecEvade, S81MutTool) to attack R; both did.
- **Misroot sweep:** `git -C /home/vgpnk/Projects/shokunin status --porcelain` lists orchestrator `.scratch/*` and the pre-existing `?? f.txt`, `?? trail-ids.txt` (already present at r80, not this lane's); nothing moved.
- **Routed to r82:** lesson `## Routed to round 82` (a)-(d) and SCORECARD "r82 (planned)".
- **Open L0 questions:** none new.
- **Tool installs:** none. No pacman transaction, no sysctl, sudo or kernel change.
- **Scratch:** `/fast/scratch/hyaku/souji-r81/` removed at landing.

## Stale-lane

Stale-lane: respawn-per-round driver; this lane has no other open mission.

Final lane hash: 492da800c92d703ce1011b75d219dbb77970a545
