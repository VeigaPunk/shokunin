# Hyaku Phase 3 — 12-hour training leg

- T0: `2026-10-22T04:56:36-03:00` (UTC `2026-10-22T07:56:36Z`).
- Phase 0 hard cap: `2026-10-22T09:11:36Z`; no new rounds after `2026-10-22T18:56:36Z`; wrap by `2026-10-22T19:56:36Z`.
- Binding contract: `/home/vgpnk/Projects/shokunin/.scratch/goal-20261022-hyaku-12h.md`.
- Main orchestrates only; lane authors and fresh non-author closures own content and verdicts. Ledger is append-only.

## Operator directives (verbatim)

1. "train our shokunins for the next 12 hours; in the best way possible, without degrading in quality, getting into recursive loops, and optimizing for quality, knowledge, capability enhancing"
2. "i want to train them all to round 100, also"
3. "each round should be a 32-100 swarm round"
4. "pick the order of training the shokunins, also"

## Starting lane tips

| Lane | Starting next round | Branch | Starting tip | Ahead / behind |
|---|---:|---|---|---|
| revenger | 62 | main | `876630dbb4d630e016d7d8c32a19ea04c646cbae` | 0 / 0 |
| tsukuroi | 24 | master | `eef0b8e9a6d7bd6dfc7defee621e3e5530bdce13` | 0 / 0 |
| kama | 24 | master | `147f5bdd3228ab712520b5f377346cb2d9a64769` | 0 / 0 |
| tameshi | 25 | master | `1f7315732e0cfe0ba9dfe0fff2ef36d1c8481bb5` | 0 / 0 |
| tabi | 22 | master | `e3cf4e0d30bb835532ff44b118c5ad52e09eb76d` | 0 / 0 |
| mado | 23 | master | `e33ea30461f6e9bbeee40beef19770a953f7a105` | 0 / 0 |
| mori | 24 | master | `c725aa37aa3c9ec4f34e3c2abc8ca1b616c7c130` | 0 / 0 |
| souji | 22 | master | `4edb25dfe262515d0da63224bbba71e02e36cba5` | 0 / 0 |
| kaidoku | 25 | main | `fafdd283432731a675b71e201bb9ba767c394553` | 0 / 0 |
| kake | 28 | master | `22c1669c1fec83d1a0769de6b9ce686c75657e66` | 0 / 0 |
| kagi | 28 | master | `899c50b42634a3a4ad0b28ab7509786315e2fc2b` | 0 / 0 |
| kasegi | 23 | master | `1fafde8f11454f3b0b98ab7f2b2e640aaf7f399a` | 0 / 0 |
| chousa | 28 | master | `7c87b9734eb71985e19767af36d57dff89536521` | 0 / 0 |
| kengaku | 29 | master | `1f3b0f1ec41ec297130e8944ff97968d32324632` | 0 / 0 |
| kumitate | 39 | master | `fac39171ac28c606e90da75fc2ba2ed3df52f4ea` | 0 / 0 |
| kotoba | 48 | master | `75f671b109d8eddd0d64c1429bd6379fe577175a` | 0 / 0 |
| kotodama | 51 | main | `5ab36346bafbbf2d35d74073d248e2c8d8847804` | 0 / 0 |

## Session state

- Scheduling: K=3; order tameshi, chousa, kotoba, mori, tsukuroi, kaidoku, kotodama, kama, kake, kumitate, mado. Tier A up to 3 turns per cycle; other tiers up to 2. Closure must settle before a lane resumes.
- Held lanes untouched: kagi r28, revenger r62, souji r22, tabi r22, kasegi r23, kengaku r29. Held item: kotodama51-prereg-critic; no retry or reroute.
- Mado and kumitate each have one authorized repair-first recovery round. No unblock yet.
- Prior private author trees remain preserved and are read-only input to fresh authors. No private custody layers are continued.
- Installs: none.

## Event ledger

| Timestamp | Event | Evidence / result |
|---|---|---|
| 2026-10-22T04:56:36-03:00 | One driver preflight | `pgrep -af 'shokunin-watchdog|inline.sh'` returned no matches (exit 1). No watchdog started. |
| 2026-10-22T08:04:00Z | Load complete | Canonical skill and all six protocol files, swarm skill, addendum, closure prompt, inline header, HANDOFF latest checkpoint, PHASE2 tail, prior wrap JSON, and tooling policy opened. |
| 2026-10-22T08:04:00Z | Read-only capacity | async.maxJobs=200; task.maxConcurrency=200; task.maxRecursionDepth=3; retry.maxRetries=5 (no task.maxRetries field). Starting state helper succeeded for all 17 pool lanes; all ahead=0, behind=0. |
| 2026-10-22T08:04:00Z | Routing source | task/main/planner @m_opus; critic/connector @m_auto; sentinel @m_luna; mutation-tester/executor/scribe/labrat/simplifier/distiller @m_mim; scout/security-reviewer/sonic/seance @m_flash; reviewer/revenger @m_zfl. Settings unchanged. |
| 2026-10-22T08:04:00Z | Resource sample | MemAvailable=27,871,036 kB; swap used=0. /tmp inodes 64M total, 102 used; /fast inodes 402M total, 283K used. Byte headroom recorded next. |
| 2026-10-22T08:04:00Z | Provider smoke batch | Six minimal fresh seats, one per distinct configured alias; no model parameter. Jobs HyakuSmokeOpus, HyakuSmokeAuto, HyakuSmokeLuna, HyakuSmokeMim, HyakuSmokeFlash, HyakuSmokeZfl. |
| 2026-10-22T08:04:00Z | Provider replies | task @m_opus answered anthropic/claude-opus-5-5 (runtime report); critic @m_auto answered Auto / cursor/default, underlying model not exposed. |

### Phase 0 continuation

- Timestamp correction: the initial `08:04:00Z` labels were not captured event times. Those events occurred before the observed clock sample `2026-10-22T07:59:38.545438Z`; treat them as untimed initial records, not future-dated evidence.
- The driver preflight pattern contained a literal pipe; its actual result was no matching processes, exit 1.

| Observed checkpoint | Event | Evidence / result |
|---|---|---|
| 2026-10-22T07:59:38Z | Filesystem byte headroom | `/tmp`: 128G total, 2.5G used, 126G available; `/fast`: 804G total, 21G used, 783G available. |
| 2026-10-22T07:59:38Z | Live session rebound | `live-session-dir` now points to `2026-10-22T07-55-56-355Z_01a1629c-0c43-7754-9701-07270d148a3a`, replacing the dead session. |
| 2026-10-22T07:59:38Z | Provider replies | reviewer @m_zfl answered `zai/glm-5.3-flash`; scout @m_flash answered `charm-hyper/deepseek-v4.1-flash`; sentinel @m_luna answered, actual model not exposed. Scribe @m_mim remains pending. |
| 2026-10-22T07:59:38Z | Addendum amendment delegated | `HyakuAmendAddendum` owns only `scripts/hyaku/lane-addendum.md` and its protocol helper commit. No other fleet script edits authorized. |
| 2026-10-22T07:59:38Z | Stale claim: kasegi r23 | Held; claim untouched. |
| 2026-10-22T07:59:38Z | Stale claim: souji r22 | Held; claim untouched despite an existing closure. |
| 2026-10-22T07:59:38Z | Stale claim: tabi r22 | Held; claim untouched. |
| 2026-10-22T07:59:38Z | Stale claim: kengaku r29 | Held; claim untouched; excluded history not opened. |
| 2026-10-22T07:59:38Z | Stale claim: kagi r28 | Held; claim untouched. |
| 2026-10-22T07:59:38Z | Stale claim: revenger r62 | Held; claim untouched. |
| 2026-10-22T07:59:38Z | Stale claim: kama r24 | `closed` returned `1 rejected`; `advance` succeeded, next=25. No in-session admission claimed for this old closure. |
| 2026-10-22T07:59:38Z | Stale claim: mori r24 | `closed=0 none`; verify failed report_of; fail returned `RETRYABLE attempt 1/3`. Fresh identity required. |
| 2026-10-22T07:59:38Z | Stale claim: kotodama r51 | `closed=0 none`; verify failed report_of; fail returned `RETRYABLE attempt 1/3`. Item hold remains. |
| 2026-10-22T07:59:38Z | Stale claim: kotoba r48 | `closed=0 none`; verify failed report_of; fail returned `RETRYABLE attempt 1/3`. Fresh identity required. |
| 2026-10-22T07:59:38Z | Stale claim: kaidoku r25 | `closed=0 none`; verify failed report_of; fail returned `RETRYABLE attempt 1/3`. Existing measured work is input, not admission. |
| 2026-10-22T07:59:38Z | Stale claim: tameshi r25 | `closed=0 none`; verify failed report_of; fail returned `RETRYABLE attempt 1/3`. Fresh identity required. |
| 2026-10-22T07:59:38Z | Stale claim: tsukuroi r24 | `closed=0 none`; verify failed report_of; fail returned `RETRYABLE attempt 1/3`. Old identity backoff is not resumed. |
| 2026-10-22T07:59:38Z | Stale claim: chousa r28 | `closed=0 none`; verify succeeded: report `60f0810`, lane tip `7c87b9734`. Fresh closure prompt rendered and `HyakuCloseChousa28` dispatched; only committed safe material allowed. |
| 2026-10-22T07:59:38Z | Stale claim: kake r28 | `closed=0 none`; verify failed report_of; fail returned `RETRYABLE attempt 1/3`. Fresh identity required. |
| 2026-10-22T07:59:38Z | Baseline closure count | 118 hyaku rows exist before new closures. Latest existing row index 440 is kama r24. New closure sequence begins after this checkpoint. |

- All seven retryable stale failures used: `superseded at 2026-10-22T04:56:36-03:00: stale 2026-10-21/22 author; fresh attempt`. No prior author identity was resumed; no private tree was deleted.

### Provider preflight settled — 2026-10-22T08:00:22Z

| Alias | Probe role | Answering model observed | Result |
|---|---|---|---|
| @m_opus | task | anthropic/claude-opus-5-5 | Ready |
| @m_auto | critic | cursor/default (Auto; underlying model not exposed) | Ready |
| @m_luna | sentinel | Not exposed to seat | Ready |
| @m_mim | scribe | opencode-go/minimax-m3.1-flash-free:high | Ready |
| @m_flash | scout | charm-hyper/deepseek-v4.1-flash | Ready |
| @m_zfl | reviewer | zai/glm-5.3-flash | Ready |

- Six distinct configured aliases answered. No model parameter, routing change, install, or explicit reroute was used. This proves current answers, not the availability of every fallback or sustained swarm capacity.
- The scribe reported unrelated historical/global log noise; it is not attributed to this session without a correlated identity. No held item gains clearance from a smoke answer.
- Initial ledger commit/push observed: `b76621931c7bf094a79c1fff5bac9f2e2b64f397`.

### Depth sentinel baseline

Computed at `2026-10-22T08:00:22Z` from the latest five explicitly admitted hyaku reports available per lane. Evidence pointers are occurrences matching repo-relative paths, URLs, or 7–40-digit commit hashes; the same expression is used at closure. Fewer than five available reports are disclosed, not fabricated.

| Lane | Available admitted reports | Median bytes | Median evidence-pointer occurrences |
|---|---:|---:|---:|
| tameshi | 5 | 16228 | 131 |
| chousa | 1 | 17076 | 107 |
| kotoba | 0 | unavailable | unavailable |
| mori | 5 | 14952 | 114 |
| tsukuroi | 5 | 18253 | 141 |
| kaidoku | 5 | 16446 | 125 |
| kotodama | 0 | unavailable | unavailable |
| kama | 5 | 10129 | 70 |
| kake | 4 | 12665.5 | 102.5 |
| kumitate | 1 | 12145 | 94 |
| mado | 5 | 14093 | 128 |

- Sentinel threshold is strictly below 40% of a lane's median in either field; it triggers a restore-depth note to the next L1, not a padded report or automatic verdict.

### Phase 0 close and first dispatches

| Observed checkpoint | Event | Evidence / result |
|---|---|---|
| 2026-10-22T08:02:00Z | Operator interjection | Message `/m,odel`, read as a mistyped `/model` picker command. No setting, route or model changed; the leg continues. |
| 2026-10-22T08:02:00Z | Addendum amendment landed | `HyakuAmendAddendum` committed and pushed `2a835a9523da1560412ab45d802900334b6282a6` through `fleet-commit.sh --as protocol`; only `scripts/hyaku/lane-addendum.md` changed. Main reviewed it: directive 3 quoted verbatim, round total 32–100 seats, v1 build/falsify default and v2 single-wave alternative, the exact routing sentence, the goal-file reference for lane order, and §6.9 Claim sizing. Residual note: the v2 attack-role list names labrat, but the validator taxonomy is normative and labrat runs only as an executor-spawned probe. |
| 2026-10-22T08:02:30Z | Seat gate | `wave-slot.sh status`: live_estimate=1, recent_reservations=0, cap=200 (state), mem_avail_mb=27038. Old ledger rows are outside the 120 s pending window. |
| 2026-10-22T08:02:57Z | Dispatch tameshi r25 attempt 2 (A1) | `inline.sh dispatch tameshi` exit 0; dispatch evidence `699a21d`; base `1f7315732e0c`; L1 job `TameshiR25`. |
| 2026-10-22T08:02:58Z | Dispatch kotoba r48 attempt 2 (A3) | `inline.sh dispatch kotoba` exit 0; dispatch evidence `70fc54b`; base `197b5a4087ba` (attempt-1 prerequisites `c0185da5` and `75f671b1` are on the branch); L1 job `KotobaR48`. |
| 2026-10-22T08:03:00Z | Dispatch mori r24 attempt 2 (B4) | `inline.sh dispatch mori` exit 0; dispatch evidence `3c2bf2f`; base `c725aa37aa3c`; L1 job `MoriR24`. |
| 2026-10-22T08:04:00Z | Closure chousa r28 | `HyakuCloseChousa28` (fresh, non-author; model `anthropic/claude-opus-5-5`): status ok, admitted=false, verdict rejected-honest-stop. Operability unprovable, other axes unchanged. Trends: expansion unchanged, quality unchanged, discernment improved. Spot-check `6c5eb1466f2b`; MANIFEST rounds[441] at fleet `fd9509e4586d`. Routed defects D1–D5 include run-together words and an 8 h 21 min round. |
| 2026-10-22T08:04:07Z | Advance chousa → BLOCKED | `inline.sh advance chousa` printed `BLOCKED after 3 rejected` (r26 rejected-harmed, r27 rejected, r28 rejected); next=29. Parked for this leg; L0 line appended. |
| 2026-10-22T08:05:00Z | Timers armed | `bg_4` fires the 2 h freeze message at 10:03:00Z; `bg_5` fires the T0+4h checkpoint at 11:56:36Z. |
| 2026-10-22T08:05:00Z | Phase 0 complete | Finished in about 9 minutes, inside the 75-minute cap. Slots 3/3: tameshi, kotoba, mori. Next eligible in order: tsukuroi, kaidoku, kotodama, kama, kake, kumitate (recovery), mado (recovery). |

- Sentinel accounting rule: an in-session closure is the closure of a round dispatched after T0. The chousa r28 closure reconciled a pre-T0 round. It appears in the wrap tally but is excluded from the sentinel windows and the K-raise count, because it measures the old regime, not this leg's dispatch note.
- L0 baseline: 2 lines contained `L0 ANSWER` at T0+9min. Any later increase is checked for a hold answer, and the answered lane joins at the end of the order.

### Operator directive 5 — swarm skill invoked

- Verbatim, with `/swarm` invoked: "for this, 32-100 per round". Read as: swarm mode on for this conversation; each lane round totals 32–100 seats. This matches directive 3 and the landed addendum (`2a835a95`) that every prompt this leg embeds. No prompt, setting or route changed. The three running L1s already carry the rule (one match each for "32–100 seats in total" in their rendered prompts).

| Observed checkpoint | Event | Evidence / result |
|---|---|---|
| 2026-10-22T08:10:00Z | Validator band smoke (`plan` only; no dispatch, no registry) | `ufo-swarm-wave.mjs plan` over synthetic scout specs. Policy v1: 31 → exit 1 `too_few_lanes`; 32 → exit 0; 64 → exit 0; 65 → exit 1 `wave_too_wide`. Policy v2: 63 → exit 1 `too_few_lanes`; 64 → exit 0; 100 → exit 0; 101 → exit 1 `too_many_lanes` (cap 100). The validator gates each wave; the addendum text and the closure enforce the 100-seat round total across waves. |

### Operator directive 6 — tower skill invoked

- Verbatim, with `/tower` invoked (argument "r"): "yyyou should do it inline". Read as: keep the training inline. Rounds and closures run as in-session `task` subagents through `inline.sh`; no watchdog, no headless `omp -p` processes, no tower or Sighting fleet panes. This matches the binding contract and the phase-1 directive "do it inline with multiple swarms of subagents". Nothing changed.

| Observed checkpoint | Event | Evidence / result |
|---|---|---|
| 2026-10-22T08:12:00Z | Inline confirmation | `pgrep -af` for the watchdog, `inline.sh`, tower-fleet, ufo-sighting and `omp -p` returned no matches (exit 1); no tmux server is running. `proc://` lists only in-session jobs: TameshiR25, KotobaR48, MoriR24 (task, running) and timers bg_4 and bg_5. Ledger commit `7b2d2093` pushed. |
| 2026-10-22T08:12:00Z | Directives relayed | Main sent directives 5 and 6, verbatim, to TameshiR25, KotobaR48 and MoriR24. They are a steer only, with no new scope; every L1 prompt already carries both rules. |

### Operator directive 7 — concurrency

- Verbatim: "more concurrency". This is a priority interjection. It supersedes the goal file's K=3 start and its K-raise gate (≥4 in-session closures at ≥50% admitted). K is raised from 3 to 6 immediately, taking the next three lanes in the training order. The 200-job gate (`async.maxJobs` 200; wave-slot cap 200 from state) stays the hard ceiling; it was not changed. Above about 6 lanes, extra lanes mostly queue on seats, so a further raise waits for observed headroom during running waves. Drop-back trips stay in force: >20% dead seats in a wave, refusal of Main's own dispatches at the job cap, or a memory stall.

| Observed checkpoint | Event | Evidence / result |
|---|---|---|
| 2026-10-22T08:15:00Z | Seat gate before raise | `wave-slot.sh status`: live_estimate=66, recent_reservations=33, cap=200, mem_avail_mb=25255. |
| 2026-10-22T08:15:06Z | Dispatch tsukuroi r24 attempt 2 (B5) | `inline.sh dispatch` exit 0; dispatch evidence `88f66dc`; base `f169b3ba9a59`; L1 job `TsukuroiR24`. Old identity backoff not inherited. |
| 2026-10-22T08:15:08Z | Dispatch kaidoku r25 attempt 2 (C6) | `inline.sh dispatch` exit 0; dispatch evidence `6677542`; base `18e7eb6d9fe8`; L1 job `KaidokuR25`. |
| 2026-10-22T08:15:09Z | Dispatch kotodama r51 attempt 2 (C7) | `inline.sh dispatch` exit 0; dispatch evidence `2136bbc`; base `bff83ba65bf9`; L1 job `KotodamaR51`. The `kotodama51-prereg-critic` hold is quoted in the session note. |
| 2026-10-22T08:15:30Z | Timer armed | `bg_217` fires the 2 h freeze message for the second batch at 10:15:10Z. The job counter is session-global, so seats' shell jobs also advance it. |
| 2026-10-22T08:15:30Z | Slots | 6/6 busy: tameshi, kotoba, mori, tsukuroi, kaidoku, kotodama. Next eligible in order: kama (C8), kake (C9), kumitate (D10 recovery), mado (D11 recovery). |
| 2026-10-22T08:16:00Z | Seat gate after K=6 | `wave-slot.sh status`: live_estimate=71, recent_reservations=0, cap=200, mem_avail_mb=24896. |
| 2026-10-22T08:16:00Z | K raised 6 → 8 | Same directive. Reasoning: a lane averages roughly 20–30 live seats across a round (waves cover part of its time), so eight lanes put expected demand at about the 200 cap. Beyond eight, lanes mostly queue for seats and rounds drift toward the freeze limit, which costs quality. |
| 2026-10-22T08:16:39Z | Dispatch kama r25 attempt 1 (C8) | `inline.sh dispatch` exit 0; dispatch evidence `a79fb0f`; base `147f5bdd3228`; L1 job `KamaR25`. Repair-first; outcome files r23=rejected-harmed, r24=rejected, so one more rejection blocks it. |
| 2026-10-22T08:16:40Z | Dispatch kake r28 attempt 2 (C9) | `inline.sh dispatch` exit 0; dispatch evidence `9765401`; base `22c1669c1fec`; L1 job `KakeR28`. Repair-first; outcome files r26=rejected-honest-stop, r27=rejected, so one more rejection blocks it. |
| 2026-10-22T08:17:00Z | Timer armed | `bg_276` fires the 2 h freeze message for kama and kake at 10:16:41Z. |
| 2026-10-22T08:17:00Z | Slots | 8/8 busy: tameshi, kotoba, mori, tsukuroi, kaidoku, kotodama, kama, kake. Waiting in order: kumitate (D10 recovery), mado (D11 recovery). |

### Capacity trip and correction — job limit is 100, not 200

| Observed checkpoint | Event | Evidence / result |
|---|---|---|
| 2026-10-22T08:26:00Z | Job-cap refusals (trip) | Four L1 build waves were granted by the seat gate (cap 200, live 127–138), then refused in full by the task tool with "Background job limit reached (100)", 0 spawned: KaidokuR25 37 seats (`kaidoku-shokunin/.ufo/waves/round-25/a2/w1-refusal-1.json`), KotodamaR51 36 seats at 08:26:41Z (`.ufo/waves/round-51/build-task-refusal-1.txt`), TsukuroiR24 40 seats, KakeR28 38 seats (`.ufo/waves/round-28/w1-dispatch-attempt1-refused.json`). The process admits a task call only while fewer than 100 background jobs run; earlier waves pushed the count above 100. |
| 2026-10-22T08:29:00Z | Limit source (read-only) | `config.yml` has `async.maxJobs: 200` (line 245) and `task.maxConcurrency: 200` (line 131); no project-level `.omp` config overrides it. Config mtime is 05:01:04 -03, after process start (04:55:56 -03), but Main read 200 at about 04:58 -03, before that write. Routing (`agentModelOverrides`) is unchanged from the 07:59Z read. The omp binary's message prints the enforced value (`Background job limit reached (${o})`). Why the process enforces 100 is unresolved and operator-owned. L0 line filed. |
| 2026-10-22T08:30:00Z | Seat gate repaired | `~/.local/state/shokunin-hyaku/wave-cap` changed from 200 to 85. This is driver state for the wave-slot helper; no script, OMP setting or route changed. Reason: wave-live counts agents only, while the harness limit also counts background shell jobs (L1 gate waits, timers); 85 leaves room so that a grant is admitted and Main's closures can still spawn. Same threshold as `await-capacity.sh`'s default. |
| 2026-10-22T08:30:00Z | K cut 8 → 4 (trip action) | Under a 100-job ceiling, about 85 seats serve about 4 lanes. Eight lanes would mostly queue for seats and miss their freeze limits. Kept, top of the order: tameshi, kotoba, mori, tsukuroi. Stood down: kaidoku, kotodama, kama, kake. This is a capacity decision by Main, not a lane fault. Each stand-down still counts as one of the lane-round's two session attempts. |
| 2026-10-22T08:30:00Z | Messages | Stand-down orders to KaidokuR25, KotodamaR51, KamaR25 and KakeR28. TsukuroiR24 told to release and re-acquire through the corrected gate (timeout 3600 s) and resend the identical payload. TameshiR25, KotobaR48 and MoriR24 informed of the real cap. |
| 2026-10-22T08:31:00Z | Kotodama r51 stood down | Returned `STOOD DOWN kotodama r51`, 15m10s: nothing committed or pushed, no report; 11 uncommitted paths left as read-only input; validated 36-seat spec `kotodama-shokunin/.ufo/waves/round-51/build-spec.json`. `inline.sh fail` → `RETRYABLE attempt 2/3`. |
| 2026-10-22T08:31:00Z | Kake r28 stood down | Returned `STOOD DOWN kake r28`, 13m50s. Pushed lane commits from this attempt: `84ea5b1` (declarations) and `b5d423fc0205` (C1 landed, 15/15); lane tip local = remote `b5d423fc`. Ten uncommitted paths left (one pre-existing `__pycache__` not theirs); validated 38-seat spec `kake-shokunin/.ufo/waves/round-28/w1-spec.json`. `inline.sh fail` → `RETRYABLE attempt 2/3`. |
| 2026-10-22T08:33:00Z | Kama r25 stood down | Returned `STOOD DOWN kama r25`, 14m06s. Pushed lane commit `efe58e96e6cf` (preregistration, amendment, pilot, census before). Its 34-seat build wave had been admitted earlier: 4 seats returned, and the L1 cancelled 30 by id. No `llama-server` left running. Uncommitted outputs under `kama-shokunin/.ufo/waves/round-25/build/`; partial outputs from cancelled seats must be re-checked before reuse. `inline.sh fail` → `RETRYABLE attempt 1/3`. Dead seats: 30 cancelled by order, not by error. |
| 2026-10-22T08:33:00Z | Seat gate after correction | `wave-slot.sh status`: live_estimate=78, recent_reservations=0, cap=85 (state), mem_avail_mb=23056. Kaidoku stand-down still pending. |
| 2026-10-22T08:35:00Z | Kaidoku r25 stood down | Returned `STOOD DOWN kaidoku r25`, 16m06s. No wave ran: the 37-seat call was refused in full. Pushed lane commits from this attempt: `9dcd11ec` (two counting tools) and `7ef837a473ae` (claims file with before receipts); lane tip local = remote `7ef837a4`. Six uncommitted paths left (wave spec and dispatch, refusal record, `corpus/evidence/round-25/a2/c2/`, `tools/round-25/a2/resolve-selectors.py`); validated 37-seat spec `kaidoku-shokunin/.ufo/waves/round-25/a2/w1-spec.json`. `inline.sh fail` → `RETRYABLE attempt 2/3`. |
| 2026-10-22T08:35:00Z | Timer cancelled | `bg_276` (kama/kake freeze) killed; both lanes stood down. Background shell jobs count against the 100-job limit, so moot timers are removed. |
| 2026-10-22T08:35:00Z | State | Lanes in flight 4/4: tameshi r25, kotoba r48, mori r24, tsukuroi r24. Waiting in order for a free slot: kaidoku r25 (attempt 3), kotodama r51 (attempt 3), kama r25 (attempt 2), kake r28 (attempt 3), kumitate r39 (recovery), mado r23 (recovery). Seat gate live_estimate=71, cap=85. Kaidoku, kotodama and kake each have one session attempt left for this lane-round. |
| 2026-10-22T08:40:00Z | Seat bounds breach (tameshi r25) | TameshiR25 reported that its seat `ReReplay14` ran `jj log` at the fleet root at about 08:21Z ("working-copy reset and git import"; fleet `.jj` op heads changed 05:21 -03). Main read-only check: HEAD = origin/master = `de7f1961`, `git diff --cached` empty, fleet pushes unaffected. `git status` shows intent-to-add (` A`) entries for untracked files (`.scratch/goal-20261022-hyaku-12h.md`, three `.ufo/state/*.report-baseline`, `scripts/hyaku/__pycache__/append-closure.cpython-314.pyc`, `write`). Cause: the fleet root's `jj config get snapshot.auto-track` = `all()` (the session-3 note said none), so any jj command without `--ignore-working-copy` tracks untracked files into jj working-copy commit `735c27150d1c`. No repair: `fleet-commit.sh` is pathspec-limited git and cannot sweep these, and an untrack would take a mutating jj command at the fleet root. Rule restated for every wave context: read-only jj only with `--ignore-working-copy`, never at the fleet root. TameshiR25 records the breach in its report. |

### First landing and K=6

| Observed checkpoint | Event | Evidence / result |
|---|---|---|
| 2026-10-22T09:18:00Z | Kotoba r48 landed (L1 KotobaR48, 1h15m) | Lane pushed at `e5c926c5f9d4`; report fleet `ff9b983`, landed last. Shape: two v1 waves, build 33 + falsify 34 = 67 seats, 0 dead, no residual call; attack seats 38/67 (57%). L1 claims: C1 freshness (new knowledge entry, 34 → 35; its own critic disputes the axis as coverage), C2 depth (instrument ruler 5 target failures → 0). Process slip disclosed: the build gate slot was released while 7 seats still ran. Installs by seats: `skills-ref` 0.1.1 via `uv tool install` (PyPI) plus scratch-only npm packages. |
| 2026-10-22T09:19:13Z | Verify kotoba | `inline.sh verify kotoba` → `OK kotoba r48 landed: report ff9b983 lane tip e5c926c5f`. Depth sentinel: 13973 bytes, 110 evidence-pointer occurrences; no admitted baseline for kotoba (n=0), so no trip can be computed. |
| 2026-10-22T09:19:13Z | Closure dispatched | `inline.sh closure kotoba` rendered `.ufo/prompts/closure/kotoba-round-48.md`; fresh non-author job `HyakuCloseKotoba48`. |
| 2026-10-22T09:19:13Z | Seat gate | live_estimate=20, cap=85, mem_avail_mb=25377. Lanes in flight sit between waves much of the time. |
| 2026-10-22T09:19:30Z | K raised 4 → 6 | Operator directive 7 ("more concurrency") plus the observed headroom (live 20 of 85 with three lanes in flight). Since the cap fix, a grant is admissible, so extra lanes queue at the gate instead of being refused. Kake stays next in line, the most fragile lane: last session attempt and one rejection from a driver block. Drop-back signal: acquire timeouts or refusals. |
| 2026-10-22T09:19:46Z | Dispatch kaidoku r25 attempt 3 (last this session) | Dispatch evidence `366e53f`; base `18e7eb6d`; L1 `KaidokuR25a3`. Inherits pushed `9dcd11ec`, `7ef837a4` and the uncommitted wave spec, evidence and tool. |
| 2026-10-22T09:19:48Z | Dispatch kotodama r51 attempt 3 (last this session) | Dispatch evidence `2cb9c5b`; base `bff83ba6`; L1 `KotodamaR51a3`. Prereg-critic hold restated; inherits uncommitted claims drafts and the 36-seat spec. |
| 2026-10-22T09:19:49Z | Dispatch kama r25 attempt 2 | Dispatch evidence `e4cd8af`; base `147f5bdd`; L1 `KamaR25a2`. Inherits pushed `efe58e96` and partial outputs from cancelled seats (re-check required). |
| 2026-10-22T09:20:00Z | Timer armed | `bg_1486` fires the 2 h freeze message for kaidoku, kotodama and kama at 11:19:50Z. `bg_217` (10:15:10Z) now applies to tsukuroi only. Every new L1 context now carries the 100-job fact, the cap-85 gate, gate acquire timeout 3600 s, and the never-jj-at-fleet-root bound. |
| 2026-10-22T09:20:00Z | State | Lanes in flight 6/6: tameshi r25, mori r24, tsukuroi r24, kaidoku r25, kotodama r51, kama r25. Closure running: kotoba r48. Next in order: kake r28 (attempt 3), kumitate r39 (recovery), mado r23 (recovery). |
| 2026-10-22T09:25:00Z | Mori r24 landed (L1 MoriR24, 1h22m) | Lane pushed at `4f05dd5a3205`; report fleet `c7613588b56c`, landed last. Shape: two v1 waves, build 33 + falsify 36 = 69 seats, 0 dead, no residual call; falsify wave was 16 mutation-testers + 14 reviewers + 4 critics + 2 scouts. L1 claims: C1 calibration (routed check 3/4 → 4/4; backdated wave-1 ledger rows 8 → 0), C2 coverage (pressure tool, selftest 12/12; mutants 10 killed, 6 survived, disclosed). Census live DRIFT with 30 findings is host state, not this round. Installs: none. |
| 2026-10-22T09:26:05Z | Verify mori | `OK mori r24 landed: report c761358 lane tip 4f05dd5a3`, with `WARN lane repo has uncommitted changes: 2 paths` (`?? .scratch/`, `?? tools/__pycache__/`; the closure rules whether they are round work). Depth sentinel: 11439 bytes (0.77 of the 14952 median), 79 evidence-pointer occurrences (0.69 of 114). No trip. |
| 2026-10-22T09:26:14Z | Dispatch kake r28 attempt 3 (last this session) | Dispatch evidence `9581c4e`; base `22c1669c`; L1 `KakeR28a3`. Inherits pushed `84ea5b1`, `b5d423fc` and the uncommitted sources and 38-seat spec. Dispatched in the same task call as the mori closure; its task text overrides the shared closure-flavoured context. Future calls keep L1s and closures separate. |
| 2026-10-22T09:26:30Z | Closure dispatched | Fresh non-author job `HyakuCloseMori24` for `.ufo/prompts/closure/mori-round-24.md`. |
| 2026-10-22T09:26:30Z | Timer armed | `bg_1580` fires the 2 h freeze message for kake at 11:26:15Z. `bg_4` (10:03Z) now applies to tameshi only. |
| 2026-10-22T09:26:30Z | State | Lanes in flight 6/6: tameshi r25, tsukuroi r24, kaidoku r25, kotodama r51, kama r25, kake r28. Closures running: kotoba r48, mori r24. Next in order: kumitate r39 (recovery), mado r23 (recovery). Seat gate live_estimate=35, cap=85. |

### First admission

| Observed checkpoint | Event | Evidence / result |
|---|---|---|
| 2026-10-22T09:29:00Z | Closure kotoba r48: ADMITTED | `HyakuCloseKotoba48` (fresh, non-author; model `anthropic/claude-opus-5-5`; 10m08s): status ok, admitted=true. MANIFEST `rounds[442]` at fleet `7de34fe995d2`; spot-check lane commit `a5adc146a299`. C1 freshness re-measured 34 → 35 knowledge entries (the closure ruled the axis dispute for freshness); C2 depth verified from pinned receipts (5 → 0 target failures). Spot-check agreed on 4 of 4 decisions. Trends: expansion improved, quality improved, discernment improved. Routed R1–R5 to r49. Remote `main` in kotoba is stale at `c87cb30` (helper pushes `master` only). |
| 2026-10-22T09:30:07Z | Advance kotoba | `inline.sh closed kotoba` → `1 admitted`; `advance` → `kotoba r48 admitted -> next 49`. Sentinel windows (in-session closures): 1 closure, 1 admitted. |
| 2026-10-22T09:30:07Z | Seat gate | live_estimate=39, recent_reservations=38, cap=85. Samples this hour ran 20 to 78 of 85. Landed rounds took 1h15m and 1h22m, inside the 2 h freeze. |
| 2026-10-22T09:30:26Z | K raised 6 → 7; dispatch kotoba r49 attempt 1 (Tier A, second round this cycle) | Directive 7 plus observed slack. Dispatch evidence `595f068`; base `a5adc146`; L1 `KotobaR49`. The note routes R1–R5 and guards against a third same-surface freshness claim (r47 and r48 both worked freshness on the frontmatter/instrument surface). |
| 2026-10-22T09:31:00Z | Timer armed | `bg_1650` fires the 2 h freeze message for kotoba r49 at 11:30:27Z. |
| 2026-10-22T09:31:00Z | Cross-lane source available | Admitted this session: `kotoba-shokunin/corpus/knowledge/frontmatter-rule-authorities-round48.md@e5c926c5` (which authority imposes which SKILL.md frontmatter rule). Later dispatch notes may route it to lanes whose claims touch SKILL.md frontmatter or triggers. |
| 2026-10-22T09:31:00Z | State | Lanes in flight 7/7: tameshi r25, tsukuroi r24, kaidoku r25, kotodama r51, kama r25, kake r28, kotoba r49. Closure running: mori r24. Next in order: kumitate r39 (recovery), mado r23 (recovery). |
| 2026-10-22T09:35:00Z | Closure mori r24: ADMITTED | `HyakuCloseMori24` (fresh, non-author; 8m46s; no review seats): status ok, admitted=true. MANIFEST `rounds[443]` at fleet `a39a35bfecfb`; spot-check lane commit `28b79d3d1b76`. C1 calibration re-derived (8 of 9 rows pre-dispatch at base → 0 of 2 at head; bounded: lane-written times, 2-row after-set); C2 coverage verified from committed gate evidence (selftest 12/12, `MATCHER 48/48`; order shown, not independence). The untracked `.scratch/` and `tools/__pycache__/` are not round work. Spot-check 3 of 3 agree (S091 admit, S093 new row, S097 reject). Axes: calibration and coverage improved, others unchanged. Trends: expansion improved, quality unchanged, discernment improved. Routed D1–D4. Fleet note: local `main` tracks a stale `origin/main` (`c87cb300`); helpers push `master`. Not an integrity failure. |
| 2026-10-22T09:35:46Z | Advance mori | `closed` → `1 admitted`; `advance` → `mori r24 admitted -> next 25`. Sentinel windows: 2 in-session closures, 2 admitted. |
| 2026-10-22T09:35:46Z | K held at 7 | Gate live_estimate=58, recent_reservations=8, cap=85. Four build waves (kaidoku 37, kotodama 36, kama 34, kake 38) plus tsukuroi 40 are about to contend, so an eighth lane would only queue. Mori r25 (B4, second round this cycle) takes the next free slot, ahead of kumitate and mado. |
| 2026-10-22T09:36:00Z | Timers consolidated | Killed `bg_217`, `bg_1486`, `bg_1580`, `bg_1650` and `bg_5`: background shell jobs count against the 100-job ceiling while the seat gate cannot see them. One timer runs at a time (`bg_4`, 10:03:00Z); each firing arms the next deadline from the list below. |

#### Deadline list (UTC; authoritative across compaction)

| Deadline | Action |
|---|---|
| 10:03:00 | Freeze message: tameshi r25 (dispatched 08:02:57) |
| 10:15:06 | Freeze message: tsukuroi r24 (08:15:06) |
| 11:19:46 | Freeze messages: kaidoku r25 a3, kotodama r51 a3, kama r25 a2 (09:19:46–49) |
| 11:22:57 | Hard stop if no landed report: tameshi r25 |
| 11:26:14 | Freeze message: kake r28 a3 (09:26:14) |
| 11:30:26 | Freeze message: kotoba r49 (09:30:26) |
| 11:35:06 | Hard stop if no landed report: tsukuroi r24 |
| 11:56:36 | T0+4h read-only drift checkpoint (≤15 min) |
| 12:39:46 | Hard stop if no landed report: kaidoku, kotodama, kama |
| 12:46:14 | Hard stop: kake r28 |
| 12:50:26 | Hard stop: kotoba r49 |
| 15:56:36 | T0+8h read-only drift checkpoint |
| 18:56:36 | T0+11h: no new dispatches |
| 19:56:36 | Wrap complete |

- Each new dispatch adds a freeze line at +2 h and a hard-stop line at +3 h 20 min. A landed report removes that lane's later lines.

### Landings 3–4 and the first recovery round

| Observed checkpoint | Event | Evidence / result |
|---|---|---|
| 2026-10-22T09:40:00Z | Tameshi r25 landed (L1 TameshiR25, 1h37m) | Lane pushed at `f4e8f7d835a8`; report fleet `0888a12dd3c3`, landed last. Shape: one v2 wave of 65 seats (28 reviewer, 16 critic, 4 mutation-tester, 5 scout, 6 executor, 4 scribe, 2 connector); attack 48/65 (74%); 0 dead; no residual call. L1 claims: C1 calibration (`c1-measure` 0/3 → 3/3, a record repair with gate code unchanged), C2 coverage capability (`tools/mte-interop.py` absent → PASS 8/8, selftest 17/17). Disclosed mid-round harm: cold-read monitor 62/62 → 45/62 → back to 62/62 through 17 author re-anchors (not independent cold reads). Seat install: `puppeteer-core@23.11.1` via npm into /tmp. |
| 2026-10-22T09:41:50Z | Verify tameshi; closure | `OK tameshi r25 landed: report 0888a12 lane tip f4e8f7d83`. Depth sentinel: 13446 bytes (0.83 of median), 83 pointers (0.63). No trip. Fresh non-author job `HyakuCloseTameshi25`; it must rule on the harm-and-restore. |
| 2026-10-22T09:42:02Z | Dispatch mori r25 attempt 1 (B4, second round this cycle) | Dispatch evidence `49f0d4a`; base `28b79d3d`; L1 `MoriR25`. Routes r24 D1–D4 plus the six surviving mutants. |
| 2026-10-22T09:42:30Z | Tsukuroi r24 landed (L1 TsukuroiR24, 1h26m) | Author verdict: honest stop. C1 missed (267/268 findings with recorded operations); C2 missed (4/5 premises; snapshot-boot behaviour unverified). Lane `f923750ddcb5`; report fleet `6babb7cd5743`. Shape: two v1 waves, build 40 + falsify 34 = 74 seats, 0 dead. Sources 86 → 114. Scope and sequencing violations disclosed. Installs: none. |
| 2026-10-22T09:43:00Z | Verify tsukuroi; closure | `OK tsukuroi r24 landed: report 6babb7c lane tip f923750dd`. Depth sentinel: 14876 bytes (0.81), 76 pointers (0.54). No trip. Fresh non-author job `HyakuCloseTsukuroi24`. |
| 2026-10-22T09:43:13Z | Kumitate unblocked (operator ruling, D10) | Removed `blocked/kumitate`, which read: "three consecutive rejected closures through round 38 (2026-10-21T05:19:27-03:00)". Appended to `events.log`: `2026-10-22T06:43:13-03:00 operator-unblock lane=kumitate round=39 reason=goal-20261022-hyaku-12h operator ruling: one repair-first recovery round (D10); restore block if rejected`. Outcome files r36–r38 are all rejected, so a rejected r39 re-blocks through the driver's streak rule. Main verifies that at advance. |
| 2026-10-22T09:43:13Z | Dispatch kumitate r39 attempt 1 (recovery) | Dispatch evidence `072cbfd`; base `fac39171`; L1 `KumitateR39`. |
| 2026-10-22T09:44:00Z | Timers | `bg_4` and `bg_1965` killed as moot (tameshi and tsukuroi landed). One timer: `bg_1985` fires at 11:19:46Z. |
| 2026-10-22T09:44:00Z | State | Lanes in flight 7/7: kaidoku r25, kotodama r51, kama r25, kake r28, kotoba r49, mori r25, kumitate r39. Closures running: tameshi r25, tsukuroi r24. Next in order: tameshi r26 and tsukuroi r25 after their closures, then mado r23 (recovery). |

Deadline list update (UTC): remove 10:03:00, 10:15:06, 11:22:57 and 11:35:06 (landed). Add 11:42:02 freeze mori r25; 11:43:13 freeze kumitate r39; 13:02:02 hard stop mori r25; 13:03:13 hard stop kumitate r39.
| 2026-10-22T09:49:00Z | Closure tameshi r25: ADMITTED | `HyakuCloseTameshi25` (fresh, non-author; 7m52s; no review seats; ephemeral `uv run --with jsonschema==4.25.1`, no install): status ok, admitted=true. MANIFEST `rounds[444]` at fleet `0f418855d06d`; spot-check lane commit `d4140796f4e4`. C1 calibration measured (dispositioned R23-ROUTED rows 0 → 3); C2 capability verified (closure validated the 8 committed reports against the official 3.9.0 schema itself: 8/8). Harm ruling: no owned axis harmed at head. The 62/62 restore is valid for the input-keyed monitor but not independent cold-read evidence, so SHONEN box 3 stays `[~]`. Amendments came before the after-measurement and changed no target. Trends: expansion improved, quality improved (narrowly), discernment improved. Routed 1–5, including the seat `jj` runs. |
| 2026-10-22T09:50:37Z | Advance tameshi | `closed` → `1 admitted`; `advance` → `tameshi r25 admitted -> next 26`. Sentinel windows: 3 in-session closures, 3 admitted. |
| 2026-10-22T09:50:37Z | K held at 7 | Gate live_estimate=69 of 85. The 09:19Z batch (three last-attempt lanes plus kama) is entering its build waves. An eighth lane now would only queue and push those rounds toward their freeze. Tameshi r26 (A1, second round this cycle) takes the next free slot. |
| 2026-10-22T09:50:37Z | Cross-lane source available | Admitted: `tameshi-shokunin/corpus/knowledge/mte-report-interop.md@f4e8f7d8` (mutation-testing-elements report interop: emitting gate mutant ledgers in the standard schema and checking them with the official library). Candidate route for lanes whose claims rest on mutation-tested gates. |
| 2026-10-22T09:50:00Z | Closure tsukuroi r24: REJECTED (honest stop) | `HyakuCloseTsukuroi24` (fresh, non-author; 7m49s): status ok, admitted=false, verdict rejected-honest-stop. MANIFEST `rounds[445]` at fleet `abe5ca55d6bc`; spot-check lane commit `b90460168312`. C1 missed (267 of 268; one finding has no tool operation, and C1 did not count self-assessment mismatches as a calibration claim must); C2 missed (4 of 5; P3 snapshot-boot unverified). All six axes unchanged, none harmed. Disclosed violations (sudo read-only probes incl. `mkinitcpio -g --nopost` into scratch, `unshare`, `sudo python3 -`; no pacman transaction after 2026-10-21T18:07) classed as status-neutral conformance defects. Spot-check 5 of 5 agree. Trends: expansion unchanged, quality improved, discernment improved. Routed 1–7, including a read-only sudo allow-list for seats and an operator-authorized snapshot boot for P3. |
| 2026-10-22T09:51:36Z | Advance tsukuroi | `closed` → `1 rejected`; `advance` → `tsukuroi r24 rejected -> next 25`. Outcomes r22 admitted, r23 rejected, r24 rejected: one more rejection blocks it in the driver. In-session rejections for tsukuroi: 1. Sentinel windows: 4 in-session closures, 3 admitted (75%). |
| 2026-10-22T09:53:00Z | Stray r24 seats still writing | The closure found `TsukuroiR24.ExecPauseGateChecker-2` and `TsukuroiR24.ScribeGateEntry-2` running after the round ended. `proc://…/kill` refused: not spawned by Main. Main sent each a direct stop order through `agent://`. Lane working copy now shows ` M .ufo/waves/round-24/w1/ExecPauseGateChecker/check-pause-gate.py`, ` M .ufo/waves/round-24/w1/RevGateSchema.md`, and untracked `w1/ScribeGateEntry/p2-measured-probe.txt` and `zero-probes-measured.txt`. These are not round evidence. Tsukuroi r25 dispatch waits until both seats stop. Its note must order those leftovers reverted (tracked files restored from the branch) or re-verified in-round. |
| 2026-10-22T09:52:10Z | K raised 7 → 8; dispatch tameshi r26 attempt 1 (A1, second round this cycle) | Gate live_estimate=65 of 85. The next landing is expected around 10:35Z. A new L1 spends its first 20–30 min loading and planning, so its first wave reaches the gate around 10:20Z, after the current build waves drain. Dispatch evidence `7f8dc0d`; base `d4140796`; L1 `TameshiR26`. The note routes r25 items 1–5 and the kotoba frontmatter entry as an optional sibling source. Every L1 context now requires all spawned seats to have returned before the report is filed (the tsukuroi stray-seat lesson). |

Deadline list update (UTC): add 11:52:10 freeze tameshi r26; 13:12:10 hard stop tameshi r26.

| 2026-10-22T09:53:00Z | State | Lanes in flight 8/8: kaidoku r25, kotodama r51, kama r25, kake r28, kotoba r49, mori r25, kumitate r39, tameshi r26. No closure running. Next in order: tsukuroi r25 (after its stray seats stop; repair-first; one rejection from a driver block), mado r23 (recovery). |
| 2026-10-22T09:58:00Z | Kake r28 landed (L1 KakeR28a3, 32m09s) | Lane pushed at `36b6b21022f7`; report fleet `33d8f19`, landed last. Shape: one v1 build wave of 38 seats plus one leftover-checks call of 8 (5 reviewer, 3 critic); round total 46, 0 dead, 0 refused. No falsify wave: wave 1 produced fewer than 32 attack items, so a second wave would have been padding. L1 claims: C1 operability 4/15 → 15/15 (repair of the round-27 citing-set gate; selftest 29/29; 7 of 7 revert mutants caught), C2 freshness 0/4 → 4/4 (field-performance entry; sources S036–S039 re-opened). Discloses that neither counter is airtight. Installs: none. |
| 2026-10-22T09:59:00Z | Verify kake; closure | `OK kake r28 landed: report 33d8f19 lane tip 36b6b2102`, `WARN … 1 paths` (the pre-existing round-26 `__pycache__`). Depth sentinel: 12513 bytes (0.99 of median), 113 pointers (1.10). No trip. Fresh non-author job `HyakuCloseKake28`. |
| 2026-10-22T09:59:00Z | Stray tsukuroi seats exited | `proc://TsukuroiR24.ExecPauseGateChecker-2` and `…ScribeGateEntry-2` are no longer found. Before exiting they also modified `w1/ScribeGateEntry/pause-lift-gate-r24.json`. Leftovers in the lane: 3 modified tracked files and 2 untracked, all under `.ufo/waves/round-24/w1/`. |
| 2026-10-22T09:59:28Z | Dispatch tsukuroi r25 attempt 1 (B5, second round this cycle) | Dispatch evidence `853e671`; base `b9046016`; L1 `TsukuroiR25`. The note orders the five leftovers reverted (tracked files from the branch) or committed only as an incident record, routes r24 items 1–7, forbids claiming P3 without an operator-authorized snapshot boot, and routes sibling source `mori-shokunin/corpus/knowledge/system-pressure-r24.md@4f05dd5a`. |

Deadline list update (UTC): remove 11:26:14 and 12:46:14 (kake landed). Add 11:59:28 freeze tsukuroi r25; 13:19:28 hard stop tsukuroi r25.

| 2026-10-22T10:00:00Z | State | Lanes in flight 8/8: kaidoku r25, kotodama r51, kama r25, kotoba r49, mori r25, kumitate r39, tameshi r26, tsukuroi r25. Closure running: kake r28. Next in order: kake r29 (C9, if admitted), mado r23 (recovery). |
