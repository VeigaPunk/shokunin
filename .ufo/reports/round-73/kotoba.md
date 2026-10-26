# kotoba — round 73 report (hyaku run 7, attempt 1)

Lane repo `kotoba-shokunin`, branch `master`, base `072048fa8e8a52c707d25f7079772fa317244eb7`, final lane tip
`ec756f6cd384f8d4c038acecc5c933f99185367c` (`jj-lane.sh state` → `local=ec756f6… remote=ec756f6… ahead=0`; `git ls-remote origin
refs/heads/master` prints the same hash). **This round is short of the floor: wave 2 (the falsify wave) was drafted and never
dispatched after the run-budget notice, wave 1 dispatched 36 seats and 34 spawned, round total 34 spawned seats against the 64-seat floor.**
No fresh seat attacked the landed claims; the wave-1 attacks produced two errata before data (below).

## Work performed

Declared claims (frozen `plans/round-73.md` at `b337035`; errata E1 `3da11a5`, E2 `8c7029c`, freeze 2 `ccac253`): **C1 depth** (sourced,
assimilation: four Chinese-vendor skill surfaces) and **C3 operability** (the tip battery counter, M127). The planned C2 (registry out of
`SKILL.md`) contradicted PROTOCOL.md line 398 (fleet root, § Gate standard) and was withdrawn in E1; its replacement (own description) was withdrawn in E2 after
`CriticC2Counter` read nine worse descriptions as `3 of 3` — both before any data, no claim, no count. An L0 question was appended.

- Round start: census before exit 0, 142 rows (`.ufo/waves/round-73/receipts/census-before.txt`); the base battery counter read `2 of 6`
  (`receipts/c3-base-battery-counter.txt`); id collision 14 (`S203`–`S216`), lane 142 ids / package 188 (`assimilation/collisions`).
- M127 cause found by the L1 and confirmed by `ExecBatteryFix` and `RevengerBatteryDiag`: `check_tip_battery.py:609-610` derived the fleet root from
  `Path(args.repo).parent`; with the documented `--repo .` that is the lane, so `../` citations died (`receipts/m127-l1-repro.txt`).
- C3: counter anchored (`.resolve()`, fleet-equals-lane exit 2), guard base rebased to the r73 base, 69-assertion self-test (was 42), the r72
  spot-check indexed and the corpus baseline re-recorded (`11b05d9`). Mutation re-run: 22 of 23 killed, M10 equivalent (`receipts/c3-mutation-rerun.txt`).
- C1: entry `corpus/knowledge/chinese-vendor-skill-surfaces-round73.md` (TRAE, CodeBuddy IDE and CLI, Kimi Code two pages, Zhipu), rows S217–S222
  renumbered by document, six snapshots pinned in `snapshots/MANIFEST.sha256`, PROVINCE bullet, SKILL.md registry rows, counter
  `verifiers/check_cn_vendor_surfaces.py` (161-assertion self-test). Staged claims the live pages do not carry were corrected or refused
  (lesson § Gate).
- Mined mistake: `verifiers/check_report_pointers.py` (57-assertion self-test); red-before on the r72 report at the r72 tip `34 of 37; unresolved 3`, exit 1
  (`receipts/pointers-red-before.txt`). `captured-by: none` was false (Q36, Q50, Q60 existed): recorded as a third recurrence after capture.
- Routed r72 defects: 1 M127 fixed (C3); 2 falsify wave — **not done**; 3 SOURCES.md search-log damage — appended correction note (no structural guard);
  4 typo repaired (`corpus/knowledge/resident-index-and-rungs-round72.md:45`); 5 receipt names — correction below; 6 SHONEN stays `[~]`.
- **Correction of the r72 report (append-only, not a rewrite):** it cites two receipt names, tip-check_tip_battery.txt and tip-check_substrate_repin_v2.txt (as printed there, without backticks here), which exist at no revision; the committed files
  are tip-tip_battery.txt, tip-tip_battery-run2.txt and tip-substrate_repin_v2.txt (`ls .ufo/waves/round-72/receipts`).
- Round shape: two v1 waves planned, **wave 1 only run**. Wave 1: 36 dispatched, 34 spawned — executor 15, scribe 4, critic 4, reviewer 4,
  connector 2, scout 2, mutation-tester 2, revenger 1; m_flash roles (executor, scribe, critic, revenger) 24 of 34 = 71%; attack roles
  (reviewer, critic, mutation-tester, revenger) 11 of 34 = 32%. **Two dispatched seats never spawned:** `CriticC1Counter` and `CriticC3Counter` collided with kake r57's
  same-named seats (the dispatcher keys handles by seat name; `w1-results.json` carries kake's outputs for them; Main was told). Dead seats 0. No residual
  `task` call; the L1 held the planner seat. Wave 2 (35 seats, lane-unique names) was generated and discarded unrun. Round total 34 spawned. The wave waited ~70 min in the queue and was re-sized 49 → 36 to fit.
- Stale-lane: respawn-per-round driver; no other mission of this lane is open. Inherited state: none (`git status` clean at start). Tool installs: none.
  Open L0 questions: one appended (considerthese item 2 versus PROTOCOL.md line 398 (fleet root, § Gate standard)).
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` lists .tower/, .ufo/waves/round-30/, .ufo/reports/round-41/mado.md and demo-cwd.txt: none carries kotoba/round-73 content (other lanes'; not touched). Seat scratch under `/tmp/k73*` removed.

## Landed changes

| commit | change | LOG.md entry |
|---|---|---|
| `b337035` | plan, base receipts, id scratch | `## Round 73` |
| `3da11a5`, `8c7029c` | addenda E1, E2 | `## Round 73` |
| `6c57e83`, `856120a`, `ac8fc59` | wave-1 spec versions (49 → 42 → 36 seats) | `## Round 73` |
| `11b05d9` | C3: counter fix, self-test, index row, baseline | `## Round 73` |
| `ccac253` | freeze 2: C1 counter, pointer gate, snapshots, receipts, addendum 3 | `## Round 73` |
| `0f3e8ad` | C1 data: entry, S217–S222, PROVINCE, registry rows, lesson, QUALITY Q66–Q69, typo repair | `## Round 73` |
| `4cb4258` | LOG, SCORECARD annotation, lesson falsify note, baseline re-record | `## Round 73` |
| `da9eb0b` | wave-1 seat reports and results | `## Round 73` |
| `ec756f6` | tip receipts (lane HEAD) | `## Round 73` |

## Before → after measurements

- **C1 depth** — `python3 -B verifiers/check_cn_vendor_surfaces.py --rev <rev>`: `vendor skill surfaces backed 0 of 4`, exit 1, `held at base: 0` @ `072048f`
  (`receipts/c1-base-freeze.txt`) → `4 of 4`, exit 0 @ `0f3e8ad` (`receipts/c1-data-0f3e8ad750c5d25789a5a8599b77cdaa0e7a8487.txt`; `opened this round 4 of 4`, `province surfaces
  named 4 of 4`, `registry home ok`, census conformant); re-read at `da9eb0b` exit 0. Shortcut worlds: seven committed, all below 4 (`receipts/c1-controls-freeze.txt`).
  Bounded (Q26): form, sources and tokens are counted; whether an entry sentence is true is a reviewer judgement **no non-author made**; documentary evidence only.
- **C3 operability** — `python3 -B verifiers/check_tip_battery.py --rev <rev>`: form `--repo .` `2 of 6`, guards `4 of 5`, exit 1; absolute form `4 of 6` @ `072048f`
  → `fleet root /home/vgpnk/Projects/shokunin; guards 5 of 5; tip battery exit 0: 6 of 6`, exit 0 in both forms @ `11b05d9` (`receipts/c3-formA-11b05d9.txt`, `c3-formB-11b05d9.txt`)
  and again at `da9eb0b` (`receipts/tip-noharm-da9eb0bd624eba190867f970e3c93ea0fded9e39.txt`). Shortcut worlds replayed: none reads exit 0 (`receipts/c3-controls-11b05d9.txt`).
  Bounds: a *replaced* counter is outside the predicate; the form-B half is reachable by the index row and baseline alone (`CriticC3AxisR73` was planned, not run) — the form-A half is the discriminating one.
- No-harm at `da9eb0b` (`receipts/tip-noharm-da9eb0bd624eba190867f970e3c93ea0fded9e39.txt`): gate registry `58 of 58`; pins, surfaces, province core, sibling census, author rules, repin v2, census all exit 0; SKILL.md 572 of 600 lines.
  **`compare_harness_independent.py` exits 2** (`false blocker: scoped row omp.catalogue.found … recomputation gives …`): it reads the host omp catalogue; the round changed no input of it [INFERENCE, unrun at base].

## Sources & frontier

- `corpus/SOURCES.md` rows: 142 → 148 — `grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` (`receipts/census-before.txt`; after: `sources-census.sh validate --root … kotoba` exit 0, 148 rows).
  Added by tier: B 6 (S217–S222), A 0. Touched old→new: none (rows only appended; two search-log notes appended, the second corrects the r72 D3 split). Frontier row advanced: the round-1 Chinese-vendor channel moved to Core in part (`corpus/README.md` § Frontier, round-73 note).
- Census before → after: exit 0 → exit 0 (W04 20 → 20 at the registry level; the six new rows add no duplicate URL).
- **Assimilation:** one theme from `merge/kotoba/` — the Chinese-vendor skill surfaces; id collision 14 (`S203`–`S216`), lane ids 142, staged ids 188, renumber by document S214→S217, S216→S218, S217→S219, S219→S220, S218→S221, S221→S222;
  guard proof `assimilation/guard-proof/proof.txt`; scratch census exit 0 `assimilation/validate-final/census.txt`. One entry admitted; refused with reason and flip: Qwen census extension, translation-drift (refuted by the two Kimi pages), TRAE build-vs-translation; pointer-only: two entries. Quarantine slice 13 rows, none appended.
  **considerthese:** none worked (item 2 contradicts PROTOCOL.md line 398 (fleet root, § Gate standard); item 5 withdrawn before data).
- The sourced claim is C1 (rows opened 2026-10-25; located quotes in the lesson `## Gate`).

## Trend verdicts

- **expansion: improved** — one admitted entry on ground the coverage map did not hold (`receipts/base-sweeps.txt`: one unrelated hit at base), six mined rows; self-assessed only, no non-author spot-check yet.
- **quality: unchanged** — M127 resolved and the r72 defects D3/D4 handled, but the `check_report_pointers.py` fix is shown on a red-before only, no fresh seat attacked any landed claim, and the SOURCES.md splice has no structural guard.
- **discernment: unchanged** — wave-1 attacks turned two frozen claims into errata before data (a gain), but no non-author reviewer has checked this round's gate decisions; the spot-check sample is named in the lesson for the closure.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md` § Gate registry now 58 rows (`python3 -B verifiers/check_gate_registry.py --rev da9eb0b` → `58 of 58`); no non-author verifier.
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md` `## Round 73`; C1 entry from six re-fetched vendor pages (`receipts/c1-data-0f3e8ad750c5d25789a5a8599b77cdaa0e7a8487.txt`).
- [~] Instructions executable by an agent without oral context — no fresh cold run this round; `corpus/lessons/round-8-aggregator-box3-coldrun.md` remains the only record.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` § Core round-73 bullet; Qwen and translation commentary refused as sibling/other ground; `check_province_core.py --rev da9eb0b` exit 0 (`receipts/tip-noharm-da9eb0bd624eba190867f970e3c93ea0fded9e39.txt`).
