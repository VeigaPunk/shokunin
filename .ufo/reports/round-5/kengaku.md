# kengaku-shokunin — round-5 report

Commit: `782dd2d` (`round-5`) in `kengaku-shokunin/`.

## Gap selected

Corpus README's only executable open gap: *"full 33-task re-run under fixed
endpoint config remains optional"* + *"remaining karpathy branches open"*.
Both closed this round.

## What landed

| Artifact | Content |
|---|---|
| `corpus/knowledge/bench-arena-round5-battery.md` | Full-battery executed run: predictions vs observed, 8 flips, truncation class, sha-identity set, canary table, calibration delta |
| `corpus/knowledge/eval-design-digest-2.md` | Second wiki digest: 22 remaining files swept → 9 corpus-usable rules + mechanism notes + sweep command logged |
| `corpus/lessons/round-5.md` | 6 lessons: aggregate-right/model-wrong, truncation class, pipeline-owned latency signature, sha-identity = scaffold insensitivity, stable-FAIL as evidence, sweep-first digestion |
| `SKILL.md` | Telemetry parsing rules updated: FAIL-latency now pipeline-tagged, `fence_found=0`×`finish_reason` split, win-set rotation rule, sha-identity rule; 2 new cited sources |
| `SHONEN.md` | All three promotion checkboxes now verified (each cites evidence) |
| `corpus/README.md` | Index +2 rows; coverage map extended; 3 open gaps remain (n≥2 on flip set, planning-horizon coverage, task-27 timeout) |

## Executed eval — headline numbers

- Pipeline: direct `POST 127.0.0.1:34113/v1/chat/completions`, temp 0.2,
  max_tokens 4096, n=1/task, all 33 tasks, graded by repo `grade.sh`.
- **20/33 PASS — aggregate prediction hit exactly** (predicted 20, range 17–22).
- **8/33 status flips vs v2** (24% win-set rotation under a stable headline):
  P→F: 03, 09, 13, 20; F→P: 08, 12, 31; 06 → HARNESS_DEFECT (truncation at
  token cap, `finish=length`, not a harness fault).
- 5 tasks byte-identical `sol_sha256` across pipelines (16, 25, 28, 32, 33).
- FAIL median wall 1.71 s / 260 tok vs PASS 0.84 s / 128 tok — opposite sign
  to v2's inference-latency signature; signature is pipeline-owned.
- Per-task prediction accuracy: 24/33; flip prediction: predicted 1,
  observed 8 — per-task generative model was wrong despite exact aggregate.

## Evidence trail

- Predictions written before first request: `/tmp/bench-r5/predictions.md`.
- Artifacts (ephemeral): `/tmp/bench-r5/{run.py,run.log,telemetry-kq-r5.csv,
  report-kq-r5.v2.csv,out/,graded/}`.
- Endpoint verified live pre-run: `/v1/models` + `/health` 200.
- Wiki sweep: `grep -inE 'eval|benchmark|test|measur|metric|verif|correct|fail'`
  over 22 files + `sed` reads; command recorded inside the digest entry per
  CORPUS.md negative-claim rule.

## Rank status

SHONEN checklist now 3/3 checked (skill tables/sources, executed end-to-end
task, province accuracy). Promotion decision belongs to the orchestrator.
