# hyaku run 12 — 2026-10-29

Operator directive (verbatim): "ok, let's continue the training rounds; i want you to do 10
rounds per shokunin, so we can keep consistency and not get messy with commits and
dispatches; the goal is to reach round 100 on each; choose the order you deem best to do so.
| /skill:godspeed | we are on the hyaku mode, which seems the one that works best; make sure
to adapt to the 64-128 per round directive; max ceiling of 256 | use the same model
delegations we were using as before | i want you to use m_mim, m_zfl, m_flash, m_luna (max)
and also m_kfc; assign accordingly" — plus "actually, use m_swe instead of m_daybreak" for
the revenger role.

## Routing (never pass `model`)

`task.agentModelOverrides` in `~/.omp/agent/config.yml` (backup `config.yml.pre-run12-20261029`):

| roles | model |
|---|---|
| task, scout | @m_zfl |
| main, executor, simplifier, sonic, scribe, distiller | @m_flash |
| labrat, mutation-tester, sentinel | @m_mim |
| planner, critic, seance | @m_luna (alias already :max) |
| reviewer, connector, security-reviewer | @m_kfc |
| revenger | @m_swe (operator directive) |

m_kfc fallback chain: dead `"@m_swe"` hop expanded to `devin/swe-2:max` (run-11 finding:
aliases inside fallback chains do not resolve; the hop was skipped straight to luna).
Seats keep the route captured at spawn. L1_MODEL/JUDGE_MODEL labels in hyaku.env = @m_zfl.

## Round shape

64–128 seats per round, 256 hard ceiling. One v2 wave or two v1 waves; ≥25 % attack seats;
a few connector seats. File the report only after WAVE-DONE for every launched wave.

## Lane order

Lowest `next/` round first (queue order). ~4-6 lanes live at once (two 64–128 seat waves
fill in tranches under the ~96-seat ceiling; more L1s just queue). Each lane runs its
10-round block, one steered round per dispatch, non-author closure before the next dispatch.

| # | lane | run-12 start (next) | block target | notes |
|---|------|--------------------|--------------|-------|
| 1 | souji | 42 | 51 | |
| 2 | tabi | 43 | 52 | fresh-start: rejected closures r39–42 (re-blocked run 11) |
| 3 | kasegi | 46 | 55 | r46 work landed at wrap-up; re-dispatch inherits |
| 4 | kaidoku | 50 | 59 | r50 landed at wrap-up (report 1532c905); re-dispatch inherits |
| 5 | tsukuroi | 52 | 61 | fresh-start: rejected closures r49–51 (blocked run 11) |
| 6 | kengaku | 53 | 62 | GH013 resolved by operator run 11; r53 landed (e99074ba) |
| 7 | mado | 56 | 65 | r56 landed at wrap-up (4386b7f0); re-dispatch inherits |
| 8 | tameshi | 57 | 66 | r57 landed at wrap-up (38390835); re-dispatch inherits |
| 9 | mori | 61 | 70 | fresh-start: rejected closures r58–60 (re-blocked run 11) |
| 10 | chousa | 63 | 72 | r63 landed at wrap-up (795fd3b6); re-dispatch inherits |
| 11 | kama | 64 | 73 | r64 landed at wrap-up (90b4309d); re-dispatch inherits |
| 12 | kake | 64 | 73 | |
| 13 | kumitate | 69 | 78 | |
| 14 | revenger | 73 | 82 | revenger seats route @m_swe this run |
| 15 | kotodama | 79 | 88 | |
| 16 | kotoba | 82 | 91 | |

## Holds

- **kagi (next 29)** — operator HOLD stands (2026-10-21 content-safety refusal; documentary
  close r28 rejected-honest-stop rounds[638]; open L0 `kagi | round-28`). Run 11 held it under
  the same operator directive wording; not dispatched this run either. Operator to rule.
- protocol/aggregator — fleet meta-lanes, not in the pool (closures stand in for protocol).
- audio, game-dev-2d, game-dev-3d, lore — already ≥100 (101, 105, 108, 103 reports).

## Fresh-start rule

tabi, tsukuroi, mori: first run-12 round reads the last three rejected closures and
spot-checks first; declares only claims a do-nothing control cannot reach (addendum §9).
Their `blocked/` files are lifted at run start per this directive ("reach round 100 on
each"); `advance` re-blocks on a fresh 3-rejection streak, as in run 11.

## Run-start repairs / carried state

- Streak blocks lifted: tabi, tsukuroi, mori. kagi hold kept (see Holds).
- Tracked orphan `.ready` files from run 11 kept in place: kasegi r42 w2, kengaku r50 w1
  (both have `.dispatched`; bootstrap adopts, never re-registers).
- tsukuroi pre-run dirty receipt `.ufo/waves/round-51/before/c2-cheats-at-amend1.json`
  (committed empty at 91227829; closed round) — left as run 11 left it.
- Resume lanes (kasegi 46, kaidoku 50, kengaku 53, mado 56, tameshi 57, chousa 63, kama 64):
  L1 work landed and was verified at wrap-up, but no closure ran — dispatch re-claims the
  same round; the L1 inherits landed work under the lane repo and files the report.
- `/tmp/verif-kasegi-r42` (25.4 G, idle ~27 h) is above the disk guard's age floor; the
  guard's dispatch-time sweep owns its reclamation.

## Run log (orchestrator, append-only)

- Run-start probes (`probe-alias.sh`, 2026-10-29): m_zfl ✓ glm-5.3-flash primary; m_mim ✓
  MiniMax-M3.1-Flash primary; m_luna ✓ gpt-6-luna primary; m_kfc ✓ kimi-for-coding primary
  (run-11's 403 cleared). m_flash ✗ cursor `USAGE_PRICING_REQUIRED` (weekly quota) and
  m_swe ✗ `devin/swe-2` "no longer available" (model removal, not quota) — both walk chains.
- Chain repairs (primaries untouched, per run-11 precedent): m_flash dead hops
  (commandcode 401, opencode-go 402, devin deepseek quota, devin swe-2) replaced with
  MiniMax → glm → haiku → luna; m_swe chain rebuilt devin/swe-2:max (kept) → haiku → glm →
  luna; m_kfc dead swe-2 hop replaced with haiku. Backup config.yml.pre-run12-20261029.

