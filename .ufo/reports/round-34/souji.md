# Souji round 34 — attempt 2

## Status

STATUS: PARTIAL — both frozen targets were missed; five honest C1 restatements and the source/lesson/measurement records landed, but frozen counter defects make C1 unreachable and C2 feasibility remains red.

## Evidence

- Fresh-start sweep of the three rejected closures (rounds 31–33) is committed at `souji-shokunin/census/round-34/records/closure-sweep.txt`.
- Initial freeze: `2b591924f607940febbb99f922cc9bb090508eb6`; base: `9c76c7222a8abff027af42e37f0d160d52526bba`. C2 implementation repair/re-pin: `2b0171e2071fdc9c16a69bed12b0d040e574d8c8`; amendment record: `census/round-34/preregistration.txt` A1–A6.
- C1 do-nothing receipt: `SUMMARY items=60 agree=35 mismatches=25 restated=0`, rc 1 (`census/round-34/records/controls.txt`). C1 behavioral junk control: 3/3 forged rows rejected (`census/round-34/records/junk-c1.txt`). Five append-only rows E04, E05, E18, E23a, G23 were individually accepted in W1/W2 scratch probes and landed in SCORECARD; no full-width landing/tip counter pass is claimed.
- C2 repaired feasibility at `60def78d16017be528ba6b439e350918587cb80b`, list revision `2b0171e…`: `SUMMARY legs=13 pass=9 fail=4 harm=0`, rc 1. W2, W3, N3 and J1 failed; details and the 900-second J1 timeout are in `census/round-34/records/controls.txt` and `feasibility-final.txt`. No C2 target pass is claimed.
- Frontier source S230 is committed in `corpus/SOURCES.md`; the fetched bwrap v0.13.1 XML and capture hashes are in `census/round-34/waves/w1/` and the committed wave receipt. QUALITY Q79, SKILL registry/error-pattern updates, the lesson and SCORECARD measurement/plan rows are committed.
- Wave evidence capture: `bash tools/souji-wave-evidence-capture.sh <lane> 34 --verify --rev cdbae3bda828075c472a40b5181e8edc7f3f3b70` returned `records=170 failed=0 uncovered=0`.
- Wave shape: W1 40 seats (17 executor, 4 critic, 2 mutation-tester, 4 reviewer, 3 scout, 3 connector, 4 scribe, 1 sentinel, 1 revenger, 1 simplifier); W2 32 seats (17 critic, 15 reviewer); total 72. Both waves settled with no dead seats reported. The L1 held the planner seat. W2 addressed 32 distinct attack targets: the 25 C1 base mismatches plus seven separate C1/C2 instrument/leg attacks.
- Disk/resource deviation: `disk-guard.sh status` observed `/fast/scratch/hyaku` at 83% used / 140.5G free; after W1 the owned scratch root was 59.7G, exceeding the operator's <50MB per-fixture cap. All owned scratch was removed after W1 and W2 settlement; post-clean measurements were 26–28% used and >585G free. W2 scratch remained 19.1MB. This L1 conformance miss is recorded in `census/round-34/records/controls.txt` and the lesson.
- No tools were installed or updated; no pacman transaction occurred. Owned axis scores remain calibration 7, operability 8, coverage 8; certification OFF, K5 HELD, F5 reap and NAMESPACE holds unchanged.

## Findings

1. **C1 is not honestly reachable under the frozen bytes.** W1/W2 reproduced unreachable tab-delimited G05/G17b predicates, G24's `at` revision predating its script, and cause/item-file blocks for E23b and E26. W2 further confirmed E26's same-cause path lacks an item-file touch and its argv-correction statement is self-referential at landing; the only engine-accepted sed route strips the revision provenance and was not landed. W1/W2 also reproduced the off-by-one SKILL `where` binding and false-cause accepts for G17a/G21. G23 is a valid exception: W2 verified its actual authoring commit wrote both the preceding row named by the frozen cell and the adjacent r29-counter row, and independently reproduced the frozen engine acceptance. Five valid corrections landed; no total `agree=60` claim is made.
2. **C1 counter survivor:** the counter accepts wildcard exit `*` independent of the measured rc. W1 reproduced an E18 wildcard row as AGREE, although that particular run returned rc 0; accepting a nonzero result is supported by the source rule but was not separately executed. This remains an open counter weakness, not a claimed nonzero exploit reproduction.
3. **C2 is not operationally green.** The first feasibility run found N3's unstaged `tool.sh` and W2's unsandboxed execution; these implementation defects were repaired and re-pinned. The repaired full run then exposed W2/N3 fixture timeouts, W3's missing scratch-path normalization, and J1's runtime timeout. W2 independently confirmed W3's mismatch and a G5 mixed-commit coverage gap. No post-data C2 predicate or frozen leg was changed.
4. **Scratch discipline failed at L1.** The 59.7G owned scratch footprint breached the run-specific cap. The owned tree was removed after each wave settled; the final root is empty. No large counter/fixture run was started after the guard warning.

## Attack log

- W1/W2 evidence is captured under `souji-shokunin/census/round-34/waves/`; key reports include `SwarmExecutor01.md`, `SwarmExecutor02.md`, `SwarmExecutor05.md`, `SwarmExecutor10.md`, `SwarmCritic18.md`, `SwarmCritic20.md`, `AttackG21.md`, `AttackE23b.md`, `AttackE26.md`, `AttackC2W3PathNormalization.md`, and `AttackC2G5Disjointness.md`.
- E04/E05/E18/E23a/G23 corrections were individually exercised in scratch and are append-only. No dishonest G05/G17a/G17b/G21/E23b/E26 row or frozen-list amendment was landed.
- C2's four failed legs remain failures; the captured J1 timeout is not relabeled as a pass.

## Deliveries

- Lane tip pushed: `cdbae3bda828075c472a40b5181e8edc7f3f3b70` (`jj-lane.sh push` returned `landed` for this hash).
- Committed round-34 wave receipt: `souji-shokunin/census/round-34/waves/manifest.sha256` (`records=170 failed=0 uncovered=0`).
- Committed lesson: `souji-shokunin/corpus/lessons/round-34.md`.
- Fleet report `fleet-commit.sh --as souji` commit/push succeeded; `git ls-remote --exit-code origin refs/heads/master` returned lane hash `cdbae3bda828075c472a40b5181e8edc7f3f3b70`.
