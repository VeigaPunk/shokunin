# revenger — round 96 (hyaku run 15, attempt 1)

Lane: revenger (`revenger-shokunin`, province: reverse engineering of shipped artifacts; axes coverage + calibration).
Lane final hash: **66cb784ddb676b679ac4debd290cec471a9566cb** (`ls-remote origin refs/heads/main` = same; `jj-lane.sh state` ahead=0 behind=0).
Landing commit: 8d456c58e3625f0b4cf8e29bb810b47e82963b7b. Freeze commit: ff767436feed32cf2f4074f05f938f8cea98e69a (base 2875b9c9fa4cc15fd5a8ff991f04cdd0417bec97).

Outcome in one line: **C1 (coverage K) NOT VERIFIED — an honest miss; C02 admission withheld. C2 (calibration) met on its frozen predicate, contested.** Nothing is admitted this round; K stays 12/15.

## Work performed

**Declared claims (2 of max 3; frozen at `ff76743`, `reports/round-96/claims.md`):**

- **C1 — coverage, K (lowest owned criterion, 12/15 = 8.0).** Move coverage-map row C02 (native analysis sessions) `partial` → `held`, backed by the candidate entry `corpus/knowledge/round-96-native-analysis-sessions.md`. Predicate: `C1_VERDICT=pass` from `reports/round-96/c1_k_admit_counter5.py`. **Verdict: NOT VERIFIED (honest miss).** Evidence: with the admission flip applied, 17 of the counter's 18 legs pass; the single failure is `C1_SOURCES` (used-by exclusivity compares against the fixture form `knowledge/round-96-…md`, while the census and all registry rows use `corpus/knowledge/…`). The flip was withheld and reverted; the frozen counter is not edited. `reports/round-96/c1-tree-flip-diagnostic.log`, `reports/round-96/c1-tree-landed-state.log`, lesson M5 (`corpus/lessons/round-96.md`).
- **C2 — calibration.** The frozen v4 counter passes the three r95-routed NEW vectors (A4 shadow entry, A3 used-by drift, M8 frozen-dir pycache) and leaves six legs without a discriminating self-test delta. A v5 successor counter and battery close them. Predicate: `BATTERY5_VERDICT=pass` from `reports/round-96/forge_battery5.py --stage full`. **Verdict: met on the frozen predicate; contested** (see the critic and mutation results below). Evidence: `reports/round-96/controls/battery5-red-v4.log` (`V4_REACH_NEW=3/3`, `V4_SELFTEST_UNCOVERED=6/6`, `RED_V4_VERDICT=pass`), `reports/round-96/controls/battery5-full.log` and `battery5-full-landing.log` (`V5_KILLS=3/3`, `DELTA_RECEIPTS=31/31`, `MUTANT_V5_REGISTRY_KILLED=pass`, `POS_C1V5=pass`, `DO_NOTHING_C1V5=fail-as-required`, `STUB_REJECTED=pass`, `HOLD_R95_BATTERY=pass`).

Frontier step (§2b; not a claim): one sourced claim cites opened rows (S502, S503, S504); one mistake class set mined (`corpus/lessons/round-96.md` `## Mistakes`, M1–M7).

**Work items (each with its pointer):**

- Load order and lane state read: MISSION/AXES/PROTOCOL/CORPUS/LEARNING; SCORECARD; PROVINCE; QUALITY; README; round-95 spot-check (`corpus/lessons/round-95-verifier-spotcheck.md`). Lane clean at `2875b9c` before the round (`jj-lane.sh state`).
- Host probes: `rea --version` = 6.7.0; `rea doctor` ghidra scope healthy (ghidra 12.1.4, headless, native_decompiler, java 21.0.13); Hopper absent. Evidence: `corpus/live/runs/round-96/rea-doctor-r96.txt`.
- Authored-fixture premise: `gen_pe_r75.py` regen is byte-identical to the committed `fixture.exe` (sha256 `fe060de1bc5106f30dec532270fc634426484e4e2ef186e5b7617443950afd72`). `ExecSession/regen.exe` and `controls/`.
- Session record: `rea decompile corpus/fixtures/pe-r75-headless-smoke/fixture.exe 140001000` exit 0, Evidence `ev_cc0b9d88200afef1e7bf90e77f4d52faa20a049f85f1db1a7bf4a531282ffefe` (`corpus/live/runs/round-96/rea-decompile.raw.txt`); Ghidra 12.1.4 headless with the committed round-75 postScript exit 0, `function_count=1`, `FUNC entry @ 140001000`, body `return 0x2a;` (`ghidra-headless-r96.log`, `codeable-decompiled.c`).
- Post-freeze re-run (wave seat `ExecSession`): `rea decompile` re-run printed the identical Evidence ID, and `rea-diff.txt` is empty (the record is byte-identical). This answers the entry's Unknown on stability for this host with one re-run; the frozen entry bytes are not edited (the votes bind them). `.ufo/waves/round-96/w1/ExecSession/`.
- Sources fetched at pinned REA revision `12f6e0974cc0db0b3a9b86246accc76556837222`, 2026-11-05: S502 `references/native-and-artifacts.md` (HTTP 200, 38167 B, sha256 `c818ee34…cc24`); S503 `SKILL.md` (HTTP 200, 35095 B, sha256 `b5f17fdf…796ccc`). The `cli-command-map.md` path returns 404 at that revision (recorded in the fetch log; no row). `reports/round-96/quote-receipts/`; `audit_source_quotes.py verify` → `SUMMARY rows=2 verified=2`. Installed-copy drift from the pinned bodies is disclosed in the entry.
- Candidate entry written and gated: `corpus/knowledge/round-96-native-analysis-sessions.md`; lint `LINT_QMAP=0 LINT_Q14=0 LINT_Q15=0 LINT_HEADER=0`; embedded check exit 0. Candidate digest `2f7d4c1b754d812102563869b511a746c7c49750d8cc42859b2a6466d776d923`.
- Counter v5 and battery v5 written, self-tested, and frozen (`reports/round-96/c1_k_admit_counter5.py`, `forge_battery5.py`). Self-test `SELFTEST_C1V5=pass`, 31 forged deltas each with a per-delta receipt (`controls/per-delta/`). Do-nothing base fails (`controls/c1v5-do-nothing.log`, `C1_C02_HELD=fail`, rc 1).
- Wave (one v1 wave, 12 seats, see Round shape): reviewer votes (`ReviewerGate`, `ReviewerBlind`), critic (`CriticR96`), mutation-tester (`MutationR96`), executors (`ExecSession`, `ExecReceipts`, `ExecBattery`, `ExecFrozen`), scout (`ScoutReopen`), scribe (`ScribeLesson`), connector (`ConnectorOverlap`), sentinel (`SentinelScope`). Votes copied to `reports/round-96/votes/`, all three bind the candidate digest with 11 PASS each.
- Critic (CriticR96) fresh forgeries against the frozen v5 counter: 19 attacks, **13 PASS** (findings F1–F14 in `.ufo/waves/round-96/w1/CriticR96/findings.md`; receipts per forgery). Most important: F1, a decorated admitted status line (`admission-status: admitted (…)`) passes `C1_ADMITTED_UNION` because the leg anchors with `$` (lesson M6); F2–F4, the union scan is non-recursive, case-sensitive on the extension and skips undecodable files; F5, a vote artifact that is an HTML comment passes `C1_VOTES`. Six kills (K1–K6) confirm the counter does reject the other classes. The entry audit found no scope overreach.
- Mutation (MutationR96): five mutants of the v5 counter run on scratch copies. Four KILLED (`a-union`, `b-usedby`, `c-pycache`, `e-heldback`, each by a named delta). **`d-host` (receipt host allowlist) SURVIVES:** no delta covers it. Not in the frozen predicate; routed (`.ufo/waves/round-96/w1/MutationR96/mutants.md`).
- Sibling overlap and assimilation: ConnectorOverlap re-ran the frozen §10 collision check: reg-ids 501, staged-ids 155, collisions 155 (100 %). **Assimilation: none** stands (`.ufo/waves/round-96/w1/ConnectorOverlap/overlap.md`).
- Sentinel audit of the freeze and the wave: freeze hygiene pass (no `__pycache__`; touched paths only in the claimed areas; 50 paths), frozen bytes unchanged, seat bounds pass (`.ufo/waves/round-96/w1/SentinelScope/audit.md`).
- Frozen-instrument holds: the r95 counter self-test and battery re-run green on the freeze archive, and the F4/M/A1v2 probes hold (`.ufo/waves/round-96/w1/ExecFrozen/holds.log`).
- Round-95 erratum (spot-check §5 item 1, the votes relabel) appended to `corpus/lessons/round-95.md` in the freeze (`ff76743`).
- Honest-miss handling: the admission flip was applied, measured, found to fail `C1_SOURCES`, and reverted to the frozen bytes (the entry `admission-status: candidate`; README C02 `partial`). The landing tree carries the diagnostic log and the reject record in the lesson's `## Gate`.

## Landed changes

Each change is tied to its LOG.md / SCORECARD.md entry and to the commit that carries it (`git log` on the lane):

- **Round-96 LOG.md entry** (`## Round 96 …`, C1 miss, C2 met on frozen predicate, votes, critic, post-freeze observation, sources, assimilation) — commit **8d456c5** (landing).
- **Round-96 SCORECARD.md section** (K 12/15 → 12/15, `NOT VERIFIED`; calibration `BATTERY5_VERDICT=pass` contested; other criteria unchanged; routed to r97) — commit **8d456c5**.
- **SKILL.md gate registry**: `c1_k_admit_counter5` and `forge_battery5` blocks (entry command, verdict map, pinned-value path, write scope); the self-test row corrected to the measured 18 legs — commit **8d456c5**.
- **corpus/SOURCES.md**: rows S502, S503 (docs, tier A) and S504 (own-work, tier A), all `mined`, opened 2026-11-05, used-by the candidate entry — commit **8d456c5**. `corpus/lessons/round-96.md` `## Gate` records the reject and the located quotes.
- **corpus/lessons/round-96.md** (new): `## Gate` (candidates, votes, located quotes, C02 reject record), `## Frontier`, `## Post-freeze observations`, `## Mistakes` M1–M7, `## Routed forward` — commit **8d456c5**.
- **Freeze** (`ff76743`): frozen claims, counter, battery, controls and 31 per-delta receipts; the candidate entry; `corpus/live/runs/round-96/` (session record); S502/S503 receipts; `corpus/lessons/round-95.md` erratum.
- **Wave evidence** `.ufo/waves/round-96/` (spec, plan, dispatch, ready marker, results, all twelve seat directories) and **votes** `reports/round-96/votes/` — commit **8d456c5**.
- **Adjudication** (landed-revision measurements, `reports/round-96/measure-after.log`, `controls/c1v5-landing-rev.log`, `battery5-full-landing.log`, `census-round-end.log`) — commit **66cb784** (lane final).
- **Fleet**: L0 question appended (`.ufo/l0-questions.md`, `revenger | round-96`), committed with this report.

Not changed (checked): `PROVINCE.md`, `corpus/QUALITY.md`, `corpus/README.md` (coverage row C02 stays `partial`), `corpus/knowledge/round-96-…` (candidate bytes equal the freeze), and every pre-existing SOURCES row (0 touched).

## Before → after measurements

Counting commands are re-runnable against the named revision (`git show <rev>:<path>` or `--rev`). Every value below was measured on a committed revision.

| claim / criterion | before (base `2875b9c`) | after (landing `8d456c5`) | counting command | verdict |
|---|---|---|---|---|
| C1 — K (coverage, C02) | `K_HELD_BACKED` 12/15 (8.0); C02 `partial` | 12/15 (8.0); C02 `partial` | `git show 8d456c5:corpus/README.md \| awk -F'\|' '/^\| *C[0-9]+ *\|/ {s=$(NF-1); gsub(/^ +\| +$/,"",s); n[s]++; t++} END{printf "total=%d ", t; for(k in n) printf "%s=%d ", k, n[k]; print ""}'` → `total=15 partial=2 held=12 uncovered=1` (`measure-after.log`); `PYTHONUTF8=1 python3 -B reports/round-96/c1_k_admit_counter5.py --rev 8d456c5` → `C1_VERDICT=fail`, rc 1 (`controls/c1v5-landing-rev.log`) | **NOT VERIFIED** (honest miss) |
| C1 — with flip applied (diagnostic only) | — | 17 of 18 legs pass; `C1_SOURCES` fails (`C1_K_HELD_BACKED=13/15` on the flip) | `PYTHONUTF8=1 python3 -B reports/round-96/c1_k_admit_counter5.py --tree <tree with flip>` (`c1-tree-flip-diagnostic.log`) | diagnostic |
| C2 — counter reach over routed vectors (red, frozen v4) | — | `V4_REACH_NEW=3/3` (all three vectors pass the frozen v4 counter); `V4_SELFTEST_UNCOVERED=6/6` | `python3 -B reports/round-96/forge_battery5.py --stage red-v4` (`controls/battery5-red-v4.log`) | red-before |
| C2 — v5 kills and receipts (after) | — | `V5_KILLS=3/3`, `DELTA_RECEIPTS=31/31`, `MUTANT_V5_REGISTRY_KILLED=pass`, `STUB_REJECTED=pass`, `HOLD_R95_BATTERY=pass`, `BATTERY5_VERDICT=pass` (freeze and landing re-run) | `python3 -B reports/round-96/forge_battery5.py --stage full` (`controls/battery5-full.log`, `battery5-full-landing.log`) | **met on frozen predicate; contested** |
| C2 — mutation survivors (support, not a predicate) | — | 4/5 mutants KILLED; `d-host` SURVIVED | `.ufo/waves/round-96/w1/MutationR96/mutants.md` | routed to r97 |
| frozen holds (no claim) | F4 11/11, M 3/3, A1v2 5/5; r95 self-test `SELFTEST_C1V4=pass legs=24`, `BATTERY4_VERDICT=pass` | unchanged | `.ufo/waves/round-96/w1/ExecFrozen/holds.log` | unchanged |

## Sources & frontier

SOURCES before → after (`corpus/SOURCES.md`, census-shape counts):

- Rows: **501 → 504** — `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` at `2875b9c` → `501`, at `8d456c5` → `504`.
- Tier histogram: **A=452 → 455**; B=21 and C=28 unchanged (`awk` tier histogram over the same rows).
- Status histogram: **mined=465 → 468**; queued=16 and rejected=20 unchanged.
- Diff: `git diff --numstat 2875b9c 8d456c5 -- corpus/SOURCES.md` → `3 0 corpus/SOURCES.md` (3 insertions, 0 deletions); rows touched old→new: **0** (no existing row's status, recheck or used-by changed).
- Rows added by tier: S502 (A, docs), S503 (A, docs), S504 (A, own-work). All `mined`, opened 2026-11-05, used-by `corpus/knowledge/round-96-native-analysis-sessions.md` (the candidate entry; not admitted).
- Census: round start `controls/census-round-start.log` exit 0; round end `controls/census-round-end.log` and `controls/census-landing-tree.log` exit 0 (`sources-census.sh validate --root /home/vgpnk/Projects/shokunin revenger`; W01/W04 warnings only).
- Frontier rows advanced: **none admitted.** C02 moved `partial` → candidate (not held); the candidate's two tier-A sources are opened and receipted, so the next admission needs only the successor counter (`corpus/lessons/round-96.md` Routed forward).
- Sourced claim: C1 rests on S502/S503 (opened, receipted) and the own-work row S504.
- Assimilation: none (155/155 staged-id collisions, re-verified; L0 `revenger | round-91` unanswered).
- considerthese: `considerthese/2026-11-05.md` proposal 1 (counter-reachability receipts) carried as standing practice (per-delta receipts and the stub control, closing the r95 recorded PARTIAL gap). No new proposal adopted.
- Quarantine-first duty (wave-4): performed in round 92 (26/26 verdicts); not repeated.

## Trend verdicts

- **expansion: unchanged.** No knowledge entry admitted; the K count is 12/15 before and after. The candidate entry is on ground the coverage map already holds as `partial`, so it is not new uncovered ground, and it is not admitted.
- **quality: unchanged.** No admitted entry changed; the two new tier-A sources and the own-work record are opened and receipted, but nothing admitted moved. The post-freeze Evidence-ID re-run supports the entry's claim for this host without editing the frozen bytes.
- **discernment: unchanged.** No non-author admit/reject spot-check on record: the three votes are lane-internal (LEARNING.md: a subagent the lane dispatched is still the lane). The gate's behaviour is itself evidence: it withheld the admission on its own defect (C1 miss), and the critic found 13 counter-PASS forgeries, which are routed to r97 with receipts. Non-author closure is required before any `unprovable-but-better` or `improved` verdict.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — lane attestation only; the registry gained two rows this round (`SKILL.md` §Gate registry, `c1_k_admit_counter5` and `forge_battery5`). Pointer: `SKILL.md` lines 586–602 at `8d456c5`.
- [~] At least one end-to-end domain task executed and logged in LOG.md — the native-analysis session on the authored fixture (`rea decompile` + ghidra-headless, Evidence `ev_cc0b9d88…`), logged in `LOG.md` round-96 and recorded in `corpus/live/runs/round-96/`; re-run post-freeze (`.ufo/waves/round-96/w1/ExecSession/rea-diff.txt` empty).
- [~] Instructions executable by an agent without oral context — `corpus/knowledge/round-96-native-analysis-sessions.md` derivation table gives commands and expected outputs; re-run by `ExecSession` and `ExecReceipts` (`verify.md`). No non-author verifier yet.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` byte-unchanged; the sibling overlap scan (`ConnectorOverlap/overlap.md`) reports no absorbed scope.

No box is `[x]`: no non-author verifier has checked a box this round.

## Round shape

- Shape: ONE v1 wave, **12 seats**, band 8–16 (`scripts/hyaku/ufo-wave-policy.json`, waveMinLanes 8, waveMaxLanes 16). Round total 12 seats; **no residual call**.
- Role mix: scout 1 (`ScoutReopen`); scribe 1 (`ScribeLesson`); executor 4 (`ExecSession`, `ExecReceipts`, `ExecBattery`, `ExecFrozen`); reviewer 2 (`ReviewerGate`, `ReviewerBlind`); critic 1 (`CriticR96`); mutation-tester 1 (`MutationR96`); connector 1 (`ConnectorOverlap`); sentinel 1 (`SentinelScope`).
- Attack share: reviewer ×2 + critic + mutation-tester = 4/12 = 33.3 % (≥25 %). Connector: 1 (≤2).
- Planner: the L1 holds the canonical planner seat; no planner was dispatched (the validator rejects it).
- Routing: `task.agentModelOverrides` (operator-owned); no model was passed. Seats' answering models were not captured by the orchestrator; no claim depends on them.
- Dispatch: `w1.ready` written after `plan` and `run` validated the spec; the orchestrator took it (`w1.ready.dispatched`). `WAVE-DONE revenger r96 w1: all 12 seats settled` received; results `.ufo/waves/round-96/w1-results.json`.
- Dead seats: **none recorded.** All twelve settled. Seat final text was not retained by the orchestrator (kernel restart mid-wave); the seat report files in `.ufo/waves/round-96/w1/` are the evidence.
- Scribe output: `w1/ScribeLesson/lesson-draft.md` was NOT adopted; the round lesson was written by the L1 from the frozen bytes. The draft is retained as wave evidence.
- Pre-report gate: `ls-remote origin refs/heads/main` = `66cb784ddb676b679ac4debd290cec471a9566cb`.

## Misroot sweep

`git -C /home/vgpnk/Projects/shokunin status --porcelain` at report time: `.scratch/run15-state.json` (orchestrator-owned; not touched), `.ufo/l0-questions.md` (this round's L0 line, committed with this report). No seat misroot found; nothing copied or deleted from the fleet root.

## Tool installs

None. `rea` 6.7.0 and ghidra 12.1.4 were already present on this host; no install, upgrade, sudo, pacman, or sysctl action by any seat or by the L1. `user.max_user_namespaces` was not touched.

## Stale-lane

The driver launch for r96 (2026-11-05T15:06:17-03:00, attempt 1; `.ufo/watchdog.log` line `launch revenger round=96 … attempt=1`) is the L1's only open mission; no other mission of this lane is open. Progressing: lane commits `8d456c5` and `66cb784` and the wave writes since launch. No earlier attempt for round 96 (no `lane-dead-no-report` line).

## L0

`.ufo/l0-questions.md`: `revenger | round-96 | …` — the v5 used-by convention and the successor plan. Operator decision requested; the lane routed around it, and the default plan is a v6 successor on a new round-97 freeze with the same candidate digest, so the three existing votes remain valid.

## Open debts (routed; none changes a frozen predicate)

1. v6 counter on a new freeze: used-by normalizer accepts the census form (M5), with a red-before on a corpus-prefixed landed-tree fixture.
2. `C1_ADMITTED_UNION` anchor without `$`, with a decorated delta (M6, critic F1); union scan recursive, case-insensitive, undecodable-safe (F2–F4); vote-artifact substance (F5); symlink containment (F6); sid/pycache coverage (F7, F8); quote↔anchor binding (F9); URL cell (F10); derivation-table verification (F11); extra Q-map rows (F13); one fetch line for several receipts (F14).
3. `d-host` receipt-host delta (MutationR96).
4. `self-test legs=` label is deltas+2, not the leg count (M7).
5. Index or reject `corpus/knowledge/claude-red-re-bridge.md` (M4).
6. Entry Unknown on Evidence-ID stability: one post-freeze re-run recorded; the frozen entry bytes stay as written until a successor admission.
