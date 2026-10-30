# hyaku run 13 — 2026-10-30

Operator directive (verbatim): "ok i want you to train our shokunins on the hyaku style, but
using 16-32 lanes per round; all using m_zfl, m_mim or m_swe for the roles; assign accordingly |
| choose the order to train them, do 10 rounds sequentially on each, until we reach 100 rounds
trained."

## Campaign shape

- **Budget: 100 lane-rounds trained this run** (one "trained round" = one lane-round that
  landed, was verified, closed by a non-author judge and advanced). With 10-round blocks
  (the directive's "10 rounds sequentially on each"), that is **10 lanes × 10 rounds**.
- **Wave band: 16-32 seats per round** per L1 (the directive's "16-32 lanes per round";
  down from run 12's 64-128). 256 stays the hard ceiling (`maxLanes`). Shape: ONE v1 wave of
  16-32 seats under `ufo-wave-policy.json` (band now 16-32), ≥25 % attack seats, a few
  connector seats; residual ≤8 seats in one ordinary task call, counted in the round total.
- Hyaku in-session inline mode (operator session orchestrator + `task` L1s + fresh non-author
  closure judges); lane VCS jj through `jj-lane.sh`; fleet commits through `fleet-commit.sh`.
- Concurrency: ~4-6 L1 lanes live at once (run-12 pattern); seats fill in tranches under the
  98-seat ceiling / 100-job host cap.

## Routing (never pass `model`)

`task.agentModelOverrides` in `~/.omp/agent/config.yml` (backup
`config.yml.pre-run13-20261030`). Every role rides one of the three operator-named models:

| roles | model |
|---|---|
| task, main, planner, reviewer, security-reviewer, scout | @m_zfl (zai/glm-5.3-flash:max) |
| connector, critic, mutation-tester, sentinel, labrat, seance, distiller, simplifier, sonic, scribe | @m_mim (minimax-code/MiniMax-M3.1-Flash:high) |
| executor, revenger | @m_swe (devin/swe-2:max) |

Reasoning/verification seats on m_zfl; volume execution/drafting/attack-economy seats on m_mim;
code-writing seats on m_swe (run-12 precedent: revenger @m_swe; operator ruling "devin/swe-2 is
always the ultimate fallback" stays — fallback chains unchanged). L1_MODEL/JUDGE_MODEL labels in
hyaku.env stay @m_zfl. m_kfc, m_flash, m_luna, m_opus, m_sol are off every role this run.

## Lane order (10 lanes × 10 run-13 rounds = 100)

Queue order = lowest `next/` round first (established `inline.sh queue` order). The 10 lowest
dispatchable lanes; kagi (operator HOLD) and mado (SECURITY HOLD, live-credential history) are
not dispatchable and are excluded; audio, game-dev-2d, game-dev-3d, lore are ≥ round 100;
protocol/aggregator are fleet meta-lanes.

| # | lane | run-13 block | start state |
|---|------|--------------|-------------|
| 1 | tabi | r44–r53 | streak-block lifted at r43 (3 rejected closures r41–r43) → fresh-start round r44 (addendum §9) |
| 2 | souji | r46–r55 | r45 landed unclosed (run-12 wrap-up debt — close first, then block) |
| 3 | kasegi | r50–r59 | r49 landed unclosed (same debt treatment) |
| 4 | kaidoku | r53–r62 | streak-block lifted at r52 → fresh-start r53 |
| 5 | tsukuroi | r53–r62 | streak-block lifted at r52 → fresh-start r53 |
| 6 | kengaku | r55–r64 | clean |
| 7 | tameshi | r60–r69 | streak-block lifted at r59 → fresh-start r60 |
| 8 | mori | r62–r71 | streak-block lifted at r61 → fresh-start r62 |
| 9 | chousa | r66–r75 | r65 landed unclosed (debt treatment) |
| 10 | kama | r65–r74 | streak-block lifted at r64 → fresh-start r65 |

Fresh-start rule (established run 8–12, operator-sanctioned): each lifted lane's first round
reads its last three rejected closures and spot-checks first, and declares only claims a
do-nothing control cannot reach (addendum §9). `advance` re-blocks on a fresh 3-rejection streak.

## Run-12 carry-in debt (closed before the campaign, not counted in the 100)

Run 12 wrapped up mid-round (operator wrap-up, 2026-10-30 ~13:17) releasing claims without
closures. Landed-but-unclosed rounds: **souji r45, kasegi r49, chousa r65, revenger r73**
(reports committed + pushed; lanes ahead=0). These four get reconstructed claims (BASE = the
previous round's closure-recorded lane tip), non-author closures, then `advance`, before their
run-13 blocks start. The other wrap-up releases (kengaku r55, kumitate r70, kotoba r82,
kotodama r79) never landed reports — clean re-dispatch, no debt.

BASE hashes (from run-12 closure rows, `commit` field = lane tip at that closure):
souji r45 base `souji-shokunin@8376f442389f304340db2eab683b241694298188` (r44 closure row),
kasegi r49 base `kasegi-shokunin@11c9818462fcd87680fe05e45cb188610c1eaf6f` (r48 admitted),
chousa r65 base `chousa-shokunin@10e1b84e1b56b0f81f785fc73d7be0cb149a23fd` (r64 closure),
revenger r73 base `revenger-shokunin@d6475ee35427412c948639369aea21ea11855e30` (r72 closure).

## Holds (unchanged, operator-owned)

- **kagi** — operator HOLD 2026-10-21 (content-safety refusal; open L0 `kagi | round-28`).
  Not dispatched. `blocked/kagi` stays.
- **mado** — SECURITY HOLD (r56 local commits include live credential capture; GH013 blocked
  push). NEVER run `inline.sh verify mado`, push, or dispatch until operator-authorized
  credential revocation/history sanitization + independent clearance. `blocked/mado` stays;
  the stale claim `claims/mado` (r56, 2026-10-30T01:32) is left for the operator path — mado
  is not in this run.

## Standing rules (carried from runs 7–12, still binding)

10-round blocks; one steered round per dispatch; non-author closure before the next dispatch;
clean commits (only the L1 commits, through jj-lane.sh / fleet-commit.sh; seats never commit);
file the report only after WAVE-DONE for every launched wave; §3 misroot sweep before report;
claim sizing per §9 (do-nothing control receipt); assimilation contract §10 (shokuknow
`merge/<LANE>/` + `considerthese/` — adopt one theme or say `Assimilation: none`);
disk-guard gates every dispatch/spawn; seat scratch under $HYAKU_SCRATCH; fresh closures are
fresh sessions (non-author by session); append-closure.py is the only MANIFEST writer.
