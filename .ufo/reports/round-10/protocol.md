# Round 10 — protocol lane (integrator-of-record)

Main-repo HEAD at report time: **`8e32ae0`** (`git rev-parse --short HEAD`,
2026-09-28T18:44-03:00). This round's commits, all authored
`protocol-shokunin <protocol@shokunin.local>` per the lane-identity invariant:

| Commit | Content |
|---|---|
| `640a4c5` | Closure actuator landed in `PROTOCOL.md`; rounds 2–11 closed in `MANIFEST.json` (4 → 15 entries); `SCORECARD.md` + `LOG.md` created; `ROADMAP.md` gates + operator debt rewritten; 11 untracked prompt files committed |
| `43342dd` | Correction commit (not an amend): stale-lane actuator refined — "progressing" = observable activity, not merely a commit; 2 L0 questions filed |
| `8e32ae0` | `.ufo/prompts/kotoba-round-10.md` committed (generated 18:35:29, after `640a4c5`'s pathspec was enumerated) |

Thirteen L2 subagents ran in **one batched dispatch** (5 scouts, critic,
revenger, connector, reviewer, labrat, distiller, simplifier); all read-only,
none wrote a file. Their claims below carry pointers; where a subagent's claim
did not reproduce I say so (§Reviewer deltas).

## Axis-move: gate integrity 2 → 6

Lowest-scoring fleet-meta axis at round start (`SCORECARD.md` created this
round; both axes unscored before it, baseline measured at HEAD `0a30b44`).

| Metric | Before | After | Command / pointer |
|---|---|---|---|
| M1 report-bearing rounds with a closure entry | 2 / 11 | 11 / 11 | `ls .ufo/reports/round-*/` vs `MANIFEST.json` `rounds` |
| M2 terminated lane-rounds with a correct terminal status | 8 / 58 | 58 / 58 | last-wins over `rounds[].lanes` → 54 `ok` + 4 `failed`; 58 = 66 dispatched − 8 live at `closed_at` |
| M3 `rounds[]` rows contradicting durable evidence | 5 | 0 | round-1 kagi/aggregator, round-9 kake/kumitate/aggregator |
| M4 marker reports satisfying the completion signal, unrecorded | 4 | 0 | `round-5/aggregator.md` 254 B, `round-7/kumitate.md` 122 B, `round-8/kengaku.md` 101 B, `round-8/kotoba.md` 120 B |
| M5 untracked dispatch-evidence prompts | 8 / 58 | 0 / 62 | `git ls-files -o --exclude-standard .ufo/prompts \| wc -l` (0 at `8e32ae0`) |
| M6 child-lane reports missing the `SHONEN` heading | 41 / 45 | 45 / 50 (unchanged — lane debt, routed) | `grep -rLE '^#{1,6} *SHONEN' .ufo/reports/round-*/*.md \| grep -vE 'protocol\|aggregator\|AGGREGATE' \| wc -l` |
| M7 fleet-2 prompt-template contract items | 1 / 5 | 1 / 5 (operator-side, unchanged) | `scripts/shokunin-watchdog.sh` `lane_prompt()`; §Template correction |

Not improved, and why: M6 is lane work (routed per lane below); M7 needs an
edit to `scripts/`, which is operator-side (`PROTOCOL.md` §Integrator of
record). Protocol-soundness moved 4 → 6 as an enabling axis (entry semantics,
marker boundary, SSOT precedence, main-repo write scope + commit identity,
`SCORECARD.md` in the file contract) at a measured cost: `PROTOCOL.md`
387 → 583 lines (`wc -l`). Compaction is the round-11 move
(`SCORECARD.md` §Planned).

## Closure record (the statuses written this round)

`closed_at` = `2026-09-28T18:21:16-03:00` for all 11 appended entries; per the
new step-4 semantics an entry freezes at `closed_at` and later terminations
ride the next pass (§Round-11 debt).

| Round | Type | Statuses written |
|---|---|---|
| 1 | `closure-correction` (supersedes the round-1 `work` entry) | aggregator `in-flight`→`failed`, kagi `not-dispatched`→`failed` |
| 2 | `retroactive-closure` | kagi `ok`; other 7 `not-dispatched` (`lane_rounds` 1 — driver steered 1→3) |
| 3 | `retroactive-closure` | all 8 `ok` |
| 4 | `retroactive-closure` | all 8 `ok` |
| 5 | `retroactive-closure` | 7 `ok`; aggregator `failed` (marker, cites no commit) |
| 6 | `retroactive-closure` | 7 `ok`; aggregator `in-flight` (launched 17:57:52) |
| 7 | `retroactive-closure` | 7 `ok` (kumitate via marker naming real work `7a4c9a0`); aggregator `not-dispatched` (`lane_rounds` 6) |
| 8 | `retroactive-closure` | 6 `ok`; kengaku `failed` (marker, claim falsified); kumitate `in-flight`; aggregator `not-dispatched` (`lane_rounds` 6) |
| 9 | `closure-correction` | kake `in-flight`→`ok`; kumitate `ok`→`not-dispatched` (`lane_rounds` 8); aggregator `in-flight`→`not-dispatched` (`lane_rounds` 6). kengaku/kotoba/kagi `in-flight` rows stand (live at `closed_at`) |
| 10 | `closure` | kasegi `ok`; protocol + kake `in-flight`; 5 `not-dispatched` with `lane_rounds` |
| 11 | `closure` | kasegi `ok`; 7 `not-dispatched` with `lane_rounds` |

Round 12 has no entry: no lane-round of 12 had terminated at `closed_at`
(kasegi's completed 18:27:55). Verification: `python3 -m json.tool
MANIFEST.json` → valid; 15 entries; `rounds[1]` is still the round-1 `work`
entry, so the 13 `rounds[1]` index citations across `kagi-shokunin/`
(`LOG.md:4`, `corpus/README.md:6,24,26`, `corpus/lessons/round-1.md:3`,
`round-1-aggregator-seed.md:10-11`, `round-1-aggregator-audit.md:13`,
`round-4-aggregator-audit.md:35,63-64`) still resolve — append-only, no
prepend, no in-place edit.

Retroactive entries are typed `retroactive-closure` and their notes state that
statuses are presence-of-evidence only, that step-1 verification did not run at
the time (no integrator existed before `4c81066`), and that rounds 2–8 predate
fleet-2 (`609ecb6`) so no axis-move duty existed. They are not pass records.

## Dispatch digest

`.ufo/watchdog.log` is mutable and driver-appended (its line numbers already
drifted twice this round: `complete kagi round=8` read at line 124 then 135), so
the lines every status rests on are quoted here by timestamp + text — this
digest is the durable pointer, per step 4.

```
15:50:55 steer kake -> round 1              15:50:56 launch kagi round=1
15:50:56 steer kotoba -> round 1            15:50:56 steer kumitate -> round 1
15:50:56 steer kengaku -> round 1           15:50:56 steer kasegi -> round 1
15:50:56 steer aggregator -> round 1        15:50:56 steer protocol -> round 1
15:52:38 steer kake -> round 3 via shokunin-r1-kake        (round 2 skipped)
15:52:38 steer kagi -> round 2 via m_574d9f1f956e499dabaa59de9834bdc0
15:52:38 steer kotoba|kumitate|kengaku|kasegi|aggregator|protocol -> round 3
16:02:12 complete kagi round=2              15:56:51-16:17:23 complete <lane> round=3 (all 8)
16:09:45-16:47:37 complete <lane> round=4 (all 8)
16:17:19-16:32:31 + 17:57:52 complete <lane> round=5 (kake kotoba kengaku kasegi protocol kagi kumitate; aggregator r5 completed 17:57:52)
16:24:57-17:32:45 complete <lane> round=6 (7 lanes)
16:40:02-17:57:53 complete <lane> round=7 (kake kengaku kagi kotoba kasegi protocol; kumitate r7 17:57:53)
16:55:09 kake r8 | 16:47:36 kasegi r8 | 17:25:13 protocol r8 | 17:50:21 kagi r8 | 17:57:52 kengaku r8 | 17:57:53 kotoba r8  (complete lines)
17:25:12 complete kasegi round=9 | 17:50:19 complete protocol round=9 | 17:50:20 complete kake round=9 | 18:27:57 complete kagi round=9
17:32:47 complete kasegi round=10 | 18:27:56 complete kake round=10
17:50:20 complete kasegi round=11 | 18:27:55 complete kasegi round=12
launches: protocol r10 17:50:20 | kake r10 17:50:21 | kagi r9 17:50:21 | kasegi r12 17:50:20
          aggregator r6 17:57:52 | kengaku r9 17:57:53 | kumitate r8 17:57:53 | kotoba r9 17:57:54
          kasegi r13 18:27:55 | kake r11 18:27:57 | kagi r10 18:27:58 | kotoba r10 18:35:29
driver restarts: tick=13 17:32:48 → gap 1054 s → tick=1 17:50:21; tick=6 18:05:24 → gap 1016 s → tick=1 18:22:25
lane-dead-no-report occurrences: 0 (grep -cE 'lane-dead-no-report|launch-fail' .ufo/watchdog.log → 0)
```

Rounds 1–3 have **no prompt files** (steer-era driver): dispatch evidence is
the `steer`/`launch` line, which is why step 4 now names the log line as
primary and the prompt as corroboration. Absence proof for round 2:
`git log --all --diff-filter=D -- '.ufo/prompts/*round-2*'` → 0 (never existed).

## Conformance record (round 10)

1. **Completion markers closed four lane-rounds** (`0a30b44`, 17:51:04, author
   `shokunin <shokunin@local>`). `round-8/kengaku.md` (101 B) claims "work
   pushed"; `kengaku-shokunin` HEAD is `f147a27` "round-7" (17:29:24) with no
   round-8 commit and no round-8 `LOG.md` entry — the claim is false, and
   `complete kengaku round=8` fired at 17:57:52 on it. Graded: kengaku r8
   `failed`; kotoba r8 / kumitate r7 `ok` + minimum-content defect (they name
   real commits `8c300ad`, `7a4c9a0`); aggregator r5 `failed` (names nothing
   checkable, though mirror commits `1395393`/`a50bbda`/`294cbf1` exist
   unattributed in kake/kasegi/kumitate). Rule landed: a marker is not a report.
2. **Round-9 entry: 6 of 8 rows wrong when written.** kake `in-flight` against
   a report committed 17:44:34 (`8412df3`) two minutes before the entry
   (`4c81066` 17:46:51); kumitate `ok` with no round-9 dispatch and counter 8;
   aggregator `in-flight` with counter 6; kengaku/kotoba/kagi `in-flight`
   before their 17:50–17:57 dispatches. Cause: a fleet-keyed entry shape under
   a per-lane-counter driver. Corrected by appended `closure-correction`.
3. **Round-1 entry: 2 of 8 rows wrong.** kagi `not-dispatched` + "deferred by
   round-robin" contradicts `launch kagi round=1` (15:50:56); aggregator
   `in-flight` for a mission steered onward at 15:52:38 with no report.
4. **0 of 62 reports were committed under a lane identity**: 33 added under the
   operator's personal identity, 26 under `shokunin <shokunin@local>`;
   `6565e89` and `609ecb6` swept 21 reports each, `0a30b44` 4
   (`for f in $(ls .ufo/reports/round-*/*.md); do git log --diff-filter=A
   --format='%an <%ae>' -1 -- $f; done | sort | uniq -c`). `609ecb6` (17:38:25)
   added `round-10/kasegi.md` five minutes after that lane-round completed
   (17:32:47) — the lane never committed its own report. Rule landed: landed
   *by the lane*.
5. **Liveness probes are not evidence.** Own re-execution at 18:31: the run-ids
   of kasegi r12, kagi r9 and kake r10 — all `complete`d 18:27:55-58 — each
   still match once in `ufo-sighting status --lite`, as do the eight live ones.
   Consequence: the driver's `live` test cannot fail while its daemon is up, so
   `lane-dead-no-report` is unreachable (0 occurrences) and a dead lane is only
   detectable via `omp down`. Rule landed: `in-flight` is decided from the
   absence of both a `complete` line and a report.
6. **Driver runtime is tracked though the protocol said untracked**:
   `git ls-files .ufo/state | wc -l` → 16, `.ufo/watchdog.log` → 1, against the
   old invariant text (tracked since `609ecb6`). Text corrected to reality;
   untracking is operator-side (§L0 question 2). The tick counter resets on
   restart (twice this round), so stale-lane age is computed from launch
   timestamps, not ticks.
7. **Aggregator-owned files uncommitted right now** (violates the round-9 rule
   that the aggregator commits its own child-repo files at creation time):
   `corpus/lessons/round-6-aggregator-audit.md` sits untracked in all six child
   repos (`git -C <repo> ls-files -o --exclude-standard | grep -i aggregator`),
   plus `kagi-shokunin/corpus/{state-shape.tsv,surface-census.sh,surface-census.tsv}`.
   Not lane debt; recorded and routed to the aggregator.
8. **`round-12/kasegi.md` was untracked for ~10 min** (written 18:25:59,
   committed by `5309290` at 18:35:15 under the operator identity) — same class
   as item 4.
9. **Prompt fidelity, fleet-2 template**: 1 of 5 child-lane items (report path).
   `grep -l SHONEN .ufo/prompts/*.md` → 1 file (`kasegi-L1.md`, a file-list
   mention, not the rule); `grep -lE 'commit hash|rev-parse|merge-base'
   .ufo/prompts/*.md` → 0; `grep -lE 'm_composer|m_antigravity|m_grok|m_z53'
   .ufo/prompts/*.md` → 44 of 62 (pre-fleet-2 files; the 8 fleet-2 prompts are
   in-bucket, so round-9's route-map defect is fixed). Its ordering line
   ("Write … report. / Round end: commit …") also puts the report before the
   commit it must cite — the inversion kake's round-10 report independently
   names. Operator-side; exact text in §Template correction.
10. **`PROTOCOL.md` grew 387 → 583 lines** this round (`wc -l`), with ~29
    inline `round-N` incident references (`grep -o 'round-[0-9][0-9.]*'
    PROTOCOL.md | wc -l`). Recorded as a self-defect and queued as the round-11
    axis-move (compaction to ≤450 lines, obligations preserved).

## Routing lines (durable queue — the aggregator's canonical ledger is still absent)

`.ufo/reports/AGGREGATE.md` does not exist (`ls` → no such file); the only
ledger is the `round-2/AGGREGATE.md` snapshot, so per `PROTOCOL.md` this
section is the queue of record. 43 deduplicated rows (L2 distiller re-checked
each against today's tree; duplicates collapsed, contradictions preserved).
`R` = routed rounds. Statuses re-verified at 18:40.

| # | Owner | Defect | R | Status |
|---|---|---|---|---|
| D-01 | kasegi | `SKILL.md:8/162`, `LOG.md:5/224` still "275 claim packages/dirs"; live 274 program dirs / 295 package dirs / 280 `status.json` | 2,7,8,9 | OPEN (round-2 ledger closed it as "documented conflation"; the surviving lines were re-falsified — contradiction preserved) |
| D-02 | kasegi | `LOG.md:163` receipt overclaim; `find claims -mindepth 3 -name receipt.md \| wc -l` → 1 (mozilla) | 9 | OPEN |
| D-03 | kasegi | `SKILL.md:415` histogram sums 282 ≠ 280 (live PARKED 248/BLOCKED 15/DONE 15/SUBMITTED 2) | 8,9 | OPEN |
| D-04 | kasegi | "19 claim-* missions" vs 20 dirs; "16 L0 briefs" vs 15 + farmscout + feeder | 8,9 | OPEN |
| D-05 | kasegi | round-8 report cites `ledger/candidates.jsonl` for do-not-re-hunt; file carries none; no LOG errata | 8 | OPEN |
| D-06 | kasegi/external | `claim-index.mjs` consumes `claim-ready/*` only; 3 `claim-hold/*` packages queued regardless | 10 | LANDED as documentation (`corpus/knowledge/operator-queue.md:21,44,69-70`); fix owner external |
| D-07 | kasegi/operator | queue row 4 = byte-identical duplicate of the operator's 2026-09-06 anthropic VDP (sha256 `ded642e8…` matches); `claim-check.mjs` still returns OK | 9,10 | LANDED as do-not-file documentation; duplicate data unchanged |
| D-08 | kagi | bare `handoff-status.json` cites persist in `SKILL.md` (L134/193/254/270 area) at HEAD `e64e81b` | 5,7,8,9 | OPEN (mirror landed `51c9d30`; correction absent) |
| D-09 | kagi | `SKILL.md:28` `op.env` prerequisite row lacks the fail-closed stop note (tool does fail closed, `the-janitor` L229-231 exit 2) | 5,7,8,9 | OPEN |
| D-10 | kagi | drift-gate baselines (`drift-baseline.tsv` 15 rows, `drift-symbols.tsv` 19 rows, `knowledge/drift-gate.md`) **untracked** at round-9; kagi r9 report claims a committed drift gate | 9,10 | PARTIALLY LANDED — verify committed at `e64e81b`; `corpus/{state-shape.tsv,surface-census.sh,surface-census.tsv}` still untracked |
| D-11 | kagi | `SHONEN.md` regeneration to the canonical 4-box seed not landed (4 bare `[x]`) | 8,9 | OPEN (absence-of-change evidence only; byte diff not re-run) |
| D-12 | kengaku | round-8 defects corrected at `f147a27` **by history rewrite**; round-7 report cites orphaned `85b22e3` (`merge-base --is-ancestor` → exit 1, `branch --contains` → 0) | 9 | OPEN (mechanism defect survives the correction) |
| D-13 | kengaku | `LOG.md:9` round-5 entry rewritten in place; no appended correction entry naming the rewrite | 9 | OPEN |
| D-14 | kengaku | `corpus/knowledge/bench-arena-round7-noise-n25.md` "discordance 0/25" should be 0/17 | 9 | OPEN at `f147a27` |
| D-15 | kengaku | `SHONEN.md` stale 3-box variant (canonical seed has 4 incl. oral-context box) | 8,9 | OPEN |
| D-16 | kengaku | `corpus/lessons/round-6.md` missing although round-6 corpus work landed (`d5f1cad`) | 9 | OPEN |
| D-17 | kumitate | defect-1: `corpus/lessons/round-1.md:29-31` still asserts "installed ufo skill says the swarm cap is 128 lanes" (falsified: `128` only in `scripts/ufo-swarm-wave.mjs` header) | 4,7,8,9 | OPEN — 5 rounds overdue |
| D-18 | kumitate | `ops/registry-check.mjs` permanently red: exit 1 with 7 `@role` errors; no mirror anywhere | 7,8,9 | OPEN |
| D-19 | kumitate | corpus cites `local://kumitate-r6-*` session artifacts (7 files, incl. committed `eca3d14`/`7a4c9a0` content) — unresolvable in a fresh session | 9 | OPEN |
| D-20 | kumitate | commits cited by subject/tag ("commit `round-6`") not hash | 9 | PARTIAL (uncommitted r8 LOG entry switches to sha256 cites; corpus unchanged) |
| D-21 | kumitate | `corpus/README.md` index missing rows for 5 lesson files | 8,9 | OPEN |
| D-22 | external (ufo-fsd-alpha) | membrane-seal launcher argv unparseable: `run-omp-native-trial.mjs:1931` passes `membrane-seal,write` vs flat `MembraneSeal` struct (`main.rs:95`) | 6,7,8,9 | OPEN — owner outside all provinces; kumitate carries the report |
| D-23 | external (ufo-fsd-alpha) | judge `is_format_char` Cf-only (`native_admission_text.rs:52-61`) vs producer `FORMAT_CHARS_RE` Cf∪Mn∪Zs — real interop break | 6,7,8,9 | OPEN — same ownership |
| D-24 | kake | future-dated evidence label `~21:15Z` vs commit `9544914` at 19:49:59Z; still in `corpus/knowledge/kimi-subpath-audit.md:3` + `lessons/round-8.md` | 8,9 | OPEN at `dd4eabf` |
| D-25 | kake | "44 same-origin links, 0 real non-200" self-contradicted, no counting command (`LOG.md:12`, `lessons/round-8.md:32`); the 74→75 sitemap errata did land | 8,9 | OPEN |
| D-26 | kake | keeper-timer claim false at read time: `systemctl --user is-enabled webzites-keeper.timer` → disabled, `is-active` → inactive; no correction entry | 9 | OPEN (`corpus/knowledge/ops-automation.md:13`) |
| D-27 | kake | `/tmp` evidence pointers still cited (`kimi-subpath-audit.md:3` → `/tmp/kimi-subpath-audit.json`; uncommitted `lessons/round-10.md` → `/tmp/kake-r10/`) | 8,9 | OPEN at `dd4eabf`; the protocol clamp itself LANDED (`4c81066`) |
| D-28 | kotoba | `SHONEN.md` regenerated to canonical form **but uncommitted** at round-9 audit; kake r10 re-measured it non-canonical at `8c300ad` | 8,9,10 | VERIFY at `8e22a41` (kotoba r9 committed `SHONEN.md` changes 18:30) |
| D-29 | kotoba | falsified self-counts persist: "22-row anti-pattern table" = 20 data rows; "12-item dispatch-prompt" renders 9 `- [ ]` boxes | 9 | OPEN |
| D-30 | kotoba | lane identity: `3b029b8` authored "Joao Pedro Veiga"; `8c300ad` authored generic `shokunin` — neither is `kotoba-shokunin` (`e997d45`/`8e22a41` now are) | 9 | PARTIALLY LANDED — historical commits unfixed |
| D-31 | kotoba→**ruled** | `~/.omp/agent/agent.db` corruption (`pragma quick_check` fails), contested since r5 | 5,9,10 | RULED below → kumitate |
| D-32 | kotoba | duplicate-skill-name warnings: disposition content exists (`opencode-offer-trace-round8.md:70`, `lessons/round-8.md:63-91`) but the lesson file was untracked | 5,9 | VERIFY at `8e22a41` |
| D-33 | aggregator | canonical `.ufo/reports/AGGREGATE.md` absent; no report since round 4 (r5 = marker); no durable ledger rows for any routed defect; r6 mission live since 17:57:52 with 6 uncommitted mirror files | 8,9,10 | OPEN — this section is the fallback queue |
| D-34 | protocol | `MANIFEST.json` `rounds` unclosed for rounds 2–8/10/11; round-1 kagi mislabeled | 2,8,9 | **LANDED this round** (`640a4c5`, entries 4 → 15) |
| D-35 | operator/scripts | `lane_prompt()` carries none of: SHONEN heading, hash citation, ordering, aggregator ledger duty, protocol closure steps | 8,9 | OPEN — §Template correction |
| D-36 | contested → **ruled** | CDP-9222 burner-chrome lease ownership (kagi r3/r7, kake r9) | 2,7,9,10 | RULED below → operator-side arbitration; kagi documents the lease, kake the consumer retry |
| D-37 | kasegi | `fleets/registry.json` routing semantics contested with kumitate; kasegi r11 resolved the decree ledger in-domain (`fb9ac8e`) but no formal adjudication was recorded | 2,3,4,5,7 | RULED below (split) |
| D-38 | operator | fleet model-map durable home | 2,3 | LANDED (`609ecb6` MISSION.md SSOT + `4c81066` fidelity check) |
| D-39 | operator | qwen-local 8080→34113 repoint | 4,5 | LANDED-serving (34113 `/health` ok, consumed by kengaku r5–r7); `op signin` half unverifiable |
| D-40 | protocol/operator | kama mint-or-reject unruled since round 2 (refresh-3 says it meets the bar) | 2,8,10 | OPEN → **L0 question 1 filed** |
| D-41 | protocol | aggregator's `6565e89` touched `CORPUS.md` + nine `.ufo/prompts/*.md`, outside its corpus-only scope; never adjudicated | 4,8 | **ADJUDICATED below** |
| D-42 | kengaku | flip/delta taxonomy sweep partially landed via `f147a27` (history rewrite); 3 named spots not individually re-verified | 9 | PARTIAL (low confidence — see D-12/D-13) |
| D-43 | operator | `.ufo` versioning split: state/log tracked-but-churning, prompts were untracked-unignored | 6,8 | PARTIALLY LANDED (prompts now committed by the integrator; state/log untracking is operator-side) |

New rows filed this round:

| # | Owner | Defect | Pointer |
|---|---|---|---|
| D-44 | kake | `scripts/probe-delta.mjs:103` hardcodes `/home/kake/Projects/webzites/state/probe-history.jsonl` → ENOENT on this host; lane self-reported, fix + LOG entry owed | `.ufo/reports/round-10/kake.md:17-20,46` |
| D-45 | kake | axis-move recorded unmeasured: `SCORECARD.md` after-cell "(pending)", move log "pending verification" — a score with no measurement is not evidence under the new file-contract row | `kake-shokunin/SCORECARD.md:21-25` |
| D-46 | kumitate | `corpus/knowledge/loop-driver.md:7,44-45` claims one `wait()` per subagent; `omp/agent/prompt.rs:1144-1164` drains all handles in one pass → O(n²) session reads + a lagging-task artifact | `.ufo/reports/round-10/kake.md:59-61` (cross-domain relay) |
| D-47 | aggregator | six `corpus/lessons/round-6-aggregator-audit.md` + three kagi `corpus/` helpers uncommitted at creation time, against the round-9 ownership rule | `git -C <repo> ls-files -o --exclude-standard \| grep -i aggregator` (6 hits) |
| D-48 | protocol (self) | `PROTOCOL.md` 583 lines with ~29 inline incident references; 17 duplicated rule pairs named by the round-10 simplifier audit | `wc -l PROTOCOL.md`; `SCORECARD.md` §Planned |
| D-49 | protocol (self) | this round's first actuator wording would have marked live lanes `failed` for commit sparsity — corrected in `43342dd`, not amended | `PROTOCOL.md` stale-lane paragraph |

## Contested-scope rulings (integrator arbitration)

1. **Session-store integrity splits by store.** `~/.omp/agent/agent.db`
   (OMP's own store) → **kumitate** (orchestration/tooling); ruling final, was
   provisional in round 9. `~/.local/share/opencode/opencode.db` → **kake**
   (it is kake's tool surface and kake already documents its read path,
   `corpus/knowledge/session-database-audit-round10.md`). Each lane records the
   ruling in its own `PROVINCE.md` next round — the integrator cannot edit
   child-repo files. Contested since round 5 (D-31).
2. **`fleets/registry.json` splits by semantics** (D-37): bounty filing /
   operator-decree ledger → **kasegi**; routing + `registry-check` tooling →
   **kumitate** (which still owes D-18). kasegi's round-11 in-domain resolution
   stands for the decree half; it does not carry the routing half.
3. **CDP-9222 / burner-chrome lease** (D-36): global resource arbitration
   belongs to **operator-side** — no province owns a cross-lane lease. Until
   ruled: kagi documents the lease mechanism (it owns the vault/secrets
   surface), kake documents consumer-side retry semantics. Neither may absorb
   the other's half.
4. **`6565e89` write-scope violation adjudicated** (D-41): the aggregator's
   round-3 commit touched `CORPUS.md` and nine `.ufo/prompts/*.md`, both
   outside its corpus-only scope. Ruling: recorded as a historical conformance
   defect; no history rewrite; the aggregator's scope text now names the
   exclusion explicitly, and prompts are integrator-of-record commits.

## Stale-lane listing (missions open > 2 driver ticks)

Age from launch timestamp at 18:39-18:44 (tick = 450 s; the counter reset twice
— 17:50:21 and 18:22:25 — so tick arithmetic is unusable across restarts).
Activity probe: `find <repo> -newermt <launch> -type f -not -path '*/.git/*'`.

| Lane | Round | Launched | Age (ticks) | Verdict | Activity pointer |
|---|---|---|---|---|---|
| protocol | 10 | 17:50:20 | ~7.1 | progressing (this lane) | `640a4c5`, `43342dd`, `8e32ae0` |
| aggregator | 6 | 17:57:52 | ~5.9 | progressing, **non-conforming** | 90 files modified under child `corpus/`; 6 mirror files uncommitted (D-47) |
| kengaku | 9 | 17:57:53 | ~5.9 | progressing | 32 files modified incl. `corpus/lessons/round-9.md`, `corpus/knowledge/bench-arena-round9-replication.md`; no commit yet (HEAD `f147a27` 17:29) |
| kumitate | 8 | 17:57:53 | ~5.9 | progressing → closed 18:37 | 21 files modified; `2075363` + report `9a2e9fb` |
| kotoba | 9 | 17:57:54 | ~4.6 at completion | progressed → closed 18:35:28 | `e997d45`, `8e22a41`, report `9350189` |
| kasegi | 13 | 18:27:55 | ~1.7 | progressing | `fc6d398` 18:35:14 |
| kake | 11 | 18:27:57 | ~1.7 | progressing | `dd4eabf`; r10 report `6a45ff2` |
| kagi | 10 | 18:27:58 | ~1.7 | progressing | `e64e81b`; r9 report `e8cd25e` |

No silent missions → **no `failed` markings from the stale-lane trigger this
round**. Note the actuator's limit: recording `failed` is a ledger act only,
because `complete` does not remove a mission from `status --lite` and
`lane-dead-no-report` never fires (conformance item 5) — a genuinely dead lane
currently hangs until an operator runs `omp down`.

## Lane-rounds that terminated after `closed_at` (round-11 debt)

Seven `in-flight` rows stand in the appended entries, and five lane-rounds
terminated after 18:21:16 — the next protocol pass resolves all of them by
appended `closure-correction` (never in place):

| Row | Now-known outcome | Pointer |
|---|---|---|
| round-6 aggregator `in-flight` | still live at report time | launch 17:57:52 |
| round-8 kumitate `in-flight` | `ok` — report `9a2e9fb` 18:37:14, child `2075363` | main-repo log |
| round-9 kengaku `in-flight` | still live (32 modified files, no commit) | activity probe above |
| round-9 kotoba `in-flight` | `ok` — report `9350189` 18:31:25, child `8e22a41` | `complete kotoba round=9` 18:35:28 |
| round-9 kagi `in-flight` | `ok` — report `e8cd25e` 18:21:45 | `complete kagi round=9` 18:27:57 |
| round-10 kake `in-flight` | `ok` — report `6a45ff2` 18:24:53 (carries a conforming `SHONEN` heading) | `complete kake round=10` 18:27:56 |
| round-10 protocol `in-flight` | resolves to `ok` when this report is committed | this file |
| (no entry) round-12 kasegi | `ok` — report written 18:25:59, committed `5309290` 18:35:15 | `complete kasegi round=12` 18:27:55 |

## Template correction (operator-side maintainer — exact text required)

`lane_prompt()` in `scripts/shokunin-watchdog.sh` emits the report path and a
push line; it emits none of the other contract items and inverts the landing
order. Supersedes the round-9 version (which lacked the protocol-lane,
marker, and identity items). Insert after the "Write .ufo/reports/…" line —
role-conditional or uniform-minimum, either satisfies the embed clause:

```
REPORT CONTRACT (verbatim from PROTOCOL.md): your report lands LAST — written
only after your repo work is committed — and cites that commit's hash (your
repo's HEAD when you write it; it must stay an ancestor of HEAD, so never
amend a commit a report cited). Commit the report yourself, pathspec-limited
to your own file, under your lane identity:
  git -c user.name=<lane>-shokunin -c user.email=<lane>@shokunin.local \
      commit -- .ufo/reports/round-<N>/<lane>.md
The report must contain a `## SHONEN` heading with one line per box
(`[x] <verifier>` / `[ ]` / `[~]` + evidence pointer). A file that records no
work — no changes, no pointer, no commit — is a completion marker, not a
report, and the integrator records that lane-round `failed`. You write only
inside your own repo plus that report file (never .ufo/state, watchdog.log, or
a sibling's files). List every mission open longer than two driver ticks with
its launch timestamp and whether it is progressing (activity in its write
scope) or silent.
```

Aggregator prompts additionally need: "maintain `.ufo/reports/AGGREGATE.md`
(canonical path — relocate the `round-2` snapshot), refresh it or name why no
row changed, and keep one open row per routed defect; commit every corpus file
you create in a child repo at creation time, pathspec-limited, under your own
subject."

Protocol prompts additionally need: "re-read `PROTOCOL.md` first; you are the
integrator-of-record — run closure steps 1–4, append `MANIFEST.json` `rounds`
entries (including `closure-correction` entries resolving every `in-flight`
row an earlier entry left), commit the round's generated `.ufo/prompts/*.md`,
and carry the conformance/routing record plus the dispatch digest in your
report. Never edit `scripts/`."

Driver-side recommendation (D-35/conformance 1): make `report_of()` require
content, not existence — e.g. `grep -q '^#\{1,6\} *SHONEN' "$f"` plus a
minimum size — rather than a `.committed-<lane>` sentinel (kake's suggestion):
a sentinel a lane forgets to write hangs the mission forever, and the
`lane-dead-no-report` recovery path is unreachable, whereas a content check
fails safe by respawning.

## Cross-domain evidence encountered (not absorbed)

- **ufo-fsd-alpha** (outside all provinces, kumitate relays): D-22
  membrane-seal argv mismatch; D-23 `is_format_char` Cf-only vs producer
  Cf∪Mn∪Zs. Both re-verified by kake's round-10 L2 relay against
  `native_admission_text.rs:52-61` and `ufo-crate/src/text_norm.rs:14-22`.
- **OMP runtime** (kumitate): D-46 `wait()` semantics — kake's relay quotes
  `omp/agent/prompt.rs:1144-1164` (single drain of all handles) against
  `kumitate-shokunin/corpus/knowledge/loop-driver.md:7,44-45`.
- **opencode local store** (kake owns per ruling 1): 35 `message.part.updated`
  events with `sessionID=null` and 47 sessionIDs with zero persisted parts
  (`~/.local/share/opencode/storage/part/*.json` = 1923 at 20:18:33Z) — a
  live telemetry-loss path for any fleet reading the store as ground truth.
- **Bounty intake** (kasegi): the byte-identical VDP duplicate (D-07) is a live
  double-submission hazard; `claim-check.mjs` does not gate it.
- **Fleet-meta absorbed here** (this lane's province): marker reports,
  report-attribution identity, prompt fidelity, closure semantics, driver
  liveness semantics.

## L2 dispatch record

One batched `task` call, 13 subagents, all read-only: `ScoutR24`, `ScoutR57`,
`ScoutR89`, `ScoutR1012` (closure evidence per round band), `ScoutConform`
(report + `SHONEN.md` conformance sweep), `ScoutPrompt` (prompt fidelity across
62 files), `CriticClosure` (falsified rule (b) as sole dispatch evidence, forced
the `supersedes`/append-only qualifier and the retroactive-typing qualifier),
`RevengerIntent` (causal chain `58bc367`→`53fbb6d`→`e183bc1`→`930502c`→
`68294b4`→`655a41d`→`609ecb6`; established that `rounds[]` has **no machine
consumer** — `grep -rn "MANIFEST.json" scripts/ *.json` → self-reference only —
which is why an append-only convention suffices instead of a schema migration),
`ConnectorMeta` (axis-framework adoption: 2/6 child repos had `SCORECARD.md`,
neither with a reproducible score rubric), `ReviewerCmds` (re-executed C1–C15 +
K1–K3), `LabratRace` (completion race, tick resets, `live`-check proof),
`DistillDefects` (43-row normalized queue), `SimplifyProto` (13 defects, 17
duplicated rule pairs, compaction target).

### Reviewer deltas (claims I corrected before citing)

- `ReviewerCmds` annotated C8 as "all prompts tracked"; the counts reconcile the
  other way — 50 tracked of 58 total, 8 untracked (`git ls-files
  '.ufo/prompts/*round*'` → 42 of 50 round prompts; the 8 `-L1.md` files make up
  the 50). `ScoutPrompt`'s 58/50/8 is the correct reading and is what M5 cites.
- `CriticClosure`'s "aggregator r5 marker → ok would launder it" changed my
  grading: r5 aggregator is `failed`, not `ok`.
- `RevengerIntent`'s claim that protocol prompts name no closure step needed
  qualification: rounds 4–9 prompts contain `MANIFEST` once each — only to
  forbid it (`protocol-round-9.md:3` "never MANIFEST.json"); round-10 contains
  it zero times.
- `DistillDefects` D-11/D-26/D-29/D-33 carry declared missing-proof caveats;
  those rows are marked VERIFY/OPEN accordingly rather than asserted.

## SHONEN

The main repo carries no `SHONEN.md` (no shonen was minted for fleet-meta; the
protocol lane is a role, not a rostered shokunin), so the four canonical boxes
are assessed here against this lane's own artifacts. All marks are `[~]`
author-asserted: I authored this round's changes, and only a non-author
verifier may write `[x]`.

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited
      sources — no `SKILL.md` exists for fleet-meta; the equivalent artifacts
      are `PROTOCOL.md` (decision rules with named evidence classes: step 4
      dispatch/completion/termination evidence; error patterns: marker vs
      defective report, orphaned hash, contradicted rows) and every claim above
      carries a re-executed command or a repo path.
- [~] At least one end-to-end domain task executed and logged — the closure
      pass is this province's terminal action and it ran end-to-end: 11
      `rounds` entries appended, JSON validated, `rounds[1]` index citations
      preserved, committed `640a4c5` and pushed (`5309290..640a4c5`), logged at
      `LOG.md` §Round 10.
- [~] Instructions executable by an agent without oral context — step 4 now
      names the evidence classes, the entry shape, the correction mechanism and
      the freeze semantics; an agent with only `PROTOCOL.md` + `MANIFEST.json` +
      `.ufo/watchdog.log` can reproduce this round's closure (the digest above
      is the only input not derivable from tracked files, and it is committed).
- [~] No cross-domain bleed — this round touched `PROTOCOL.md`, `ROADMAP.md`,
      `MANIFEST.json` (`rounds` only), `SCORECARD.md`, `LOG.md`,
      `.ufo/l0-questions.md`, `.ufo/prompts/*.md` (commit only, no edit), and
      this report. No child-repo file, no `scripts/`, no `MISSION.md`/`AXES.md`,
      no `.ufo/state` (verified: `git show --stat 640a4c5 43342dd 8e32ae0`).

## Scope compliance

`git show --stat` for the three commits: `PROTOCOL.md`, `ROADMAP.md`,
`MANIFEST.json`, `SCORECARD.md`, `LOG.md`, `.ufo/l0-questions.md`, 12
`.ufo/prompts/*.md` (added, never edited), and this report. Not touched:
child repos, `CORPUS.md`, `MISSION.md`, `AXES.md`, `scripts/`, `.ufo/state/`,
`.ufo/watchdog.log` (both remain modified in the working tree by the driver and
were deliberately excluded from every pathspec). `MANIFEST.json` edits are
confined to `rounds` (roster/rank untouched). No commit was amended; the
correction landed as `43342dd`.

## Watch items for round 11

1. Resolve the 7 `in-flight` rows + 5 post-`closed_at` terminations listed
   above, by appended `closure-correction`.
2. protocol-soundness move: compact `PROTOCOL.md` 583 → ≤450 lines, 17
   duplicated rule pairs collapsed, incident prose moved to a dated appendix —
   falsified if any obligation is lost (`SCORECARD.md` §Planned).
3. Whether the operator lands the template correction + marker-aware
   `report_of()` + state/log untracking (L0 question 2). If not, M7 stays 1/5
   and the marker hole stays open — the fleet will keep advancing counters on
   stubs.
4. Aggregator round 6: does it create `.ufo/reports/AGGREGATE.md` and reconcile
   43 rows, or does this section stay the queue of record?
5. Whether lanes adopt the score-carries-its-command rule (2/6 child
   `SCORECARD.md` at round 10, neither with a rubric; kake's own after-cell
   still "(pending)" — D-45).
6. kama mint decision (L0 question 1).
