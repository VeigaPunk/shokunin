# R18 capability battery — ex-ante predictions

**Filed 2026-10-15T11:45:00Z, before the first real request** (see `ordering.log` and the sibling
`.sha256` digests). Machine-readable twin: `PREDICTIONS.json` — it carries the same numbers and is
the file the close-out scorer reads. Pool: the 17 live `[secondary_model.models]` entries
(`../SELECTION.md`), config sha256 `e3c223e0…8acfe78`.

Calibration base: the M1 census, which drew one small streaming request per lane. Where a census
number exists for a comparable lane it is quoted under "basis"; predictions are that number shifted
to the current model id and to this battery's 256-token generation. Ranges are deliberately wide
because the census numbers are single draws.

## 1. Per-model predictions

`pass/9` = expected passes across the 9 correctness probes (c1–c5, k1–k3, t1). `TTFT` is the median
of the two reps. `TPS d.` = predicted to be derivable (the lane flushes incrementally rather than in
one burst).

| Model | Bucket | TTFT ms pred (range) | TPS pred | TPS d. | pass/9 | Predicted failure mode |
| --- | --- | --- | --- | --- | --- | --- |
| `cascade/glm-5.3-flash` | FAST | 6000 (3500–45000) | — | no | 6 | transport (devin cold start) + format_break (chat-only, tool probe) |
| `zai-coding-plan/glm-5.3-flash-low` | FAST | 3200 (2000–6000) | — | no | 9 | truncation risk (always-thinking) |
| `cursor/composer-2.5` | FAST | 6000 (4000–12000) | — | no | 8 | format_break (no tool_use capability) |
| `cursor/cursor-grok-4.5-low-fast` | FAST | 4500 (2500–9000) | — | no | 8 | format_break (no tool_use capability) |
| `hyper/deepseek-v4.1-flash` | FAST | 900 (400–3000) | — | no | 8 | truncation risk (thinking eats the budget) |
| `cascade/deepseek-v4.1-flash` | FAST | 2500 (1500–6000) | — | no | 9 | none |
| `alibaba-token-plan/deepseek-v4.1-flash` | FAST | 2600 (1500–6000) | 180 | yes | 9 | none |
| `alibaba-token-plan-2/deepseek-v4.1-flash` | FAST | — | — | no | 0 | auth: 429 quota (key 2) |
| `alibaba-token-plan-3/deepseek-v4.1-flash` | FAST | — | — | no | 0 | auth: 429 quota (key 3) |
| `alibaba-token-plan/qwen3.8-flash` | MIDDLE | 3500 (2000–8000) | 55 | yes | 8 | truncation risk (thinking) |
| `alibaba-token-plan-2/qwen3.8-flash` | MIDDLE | — | — | no | 0 | auth: 429 quota (key 2) |
| `alibaba-token-plan-3/qwen3.8-flash` | MIDDLE | — | — | no | 0 | auth: 429 quota (key 3) |
| `zai-coding-plan/glm-5-turbo` | MIDDLE | 2800 (1500–7000) | — | no | 9 | none |
| `hyper/qwen3.8-flash` | MIDDLE | 1500 (700–4000) | 120 | yes | 8 | truncation risk (thinking) |
| `xai-oauth/grok-4.5` | MIDDLE | 1400 (800–3500) | 300 | yes | 9 | none |
| `openai-codex/gpt-6.1-sol` | STRONG | 1600 (1000–4000) | 65 | yes | 9 | none |
| `openai-codex/gpt-6.1-sol-high` | STRONG | 2500 (1500–6000) | 55 | yes | 9 | none |

## 2. Ordering predictions

Each is stated so it can come back hit, miss, or unprovable (a claim is unprovable when one side has
no usable measurement — a dead lane cannot lose a race).

| id | Claim as predicted | Why |
| --- | --- | --- |
| O1 | `cascade/deepseek-v4.1-flash` TTFT < `cursor/composer-2.5` TTFT | 2467 ms vs 5966 ms in the census |
| O2 | `hyper/deepseek-v4.1-flash` is the fastest FAST lane | 533 ms census draw, closest hyper edge |
| O3 | `cascade/glm-5.3-flash` is the slowest FAST lane | devin leg: 4349 ms census TTFT with a cold-start tail to 300 s |
| O4 | `xai-oauth/grok-4.5` is the fastest MIDDLE lane | 1166 ms census draw on 4.7 |
| O5 | `alibaba-token-plan/qwen3.8-flash` is the slowest MIDDLE lane | thinking model on the slowest answering alibaba path |
| O6 | `gpt-6.1-sol` TTFT < `gpt-6.1-sol-high` TTFT | higher effort thinks longer before the first token |
| O7 | the fastest FAST lane beats every MIDDLE and STRONG lane | hyper's 533 ms edge is 2× better than any MIDDLE draw |
| O8 | the fastest MIDDLE lane beats the fastest STRONG lane | 1400 ms (grok-4.5) vs 1600 ms (codex) — narrow, low confidence |
| **O9** | **the FAST bucket's median TTFT is *not* lower than MIDDLE's** | FAST holds the devin cascade and two cursor shims; predicted FAST median 4500 ms vs MIDDLE 2150 ms |
| O10 | `cascade/glm-5.3-flash` is slower than every MIDDLE and STRONG lane | same devin-leg reasoning as O3; the weakest of the ordering claims |
| O11 | `xai-oauth/grok-4.5` has the highest derivable TPS | 493.74 TPS census draw on 4.7 |
| O12 | `alibaba-token-plan/deepseek-v4.1-flash` TPS > `…/qwen3.8-flash` TPS | 207 TPS census vs a 25 TPS thinking draw elsewhere |
| O13 | burst-vs-incremental is a lane property, stable across the two reps | the census burst pattern came from the lane's flush behaviour, not the draw |
| O14 | the two codex models' TPS agree within 25% | same backend, same generation shape, only the effort pin differs |

O9 and G2 are the claims that matter most: they assert the **declared bucket ordering does not
survive measurement**, which is exactly what M4 needs either way.

## 3. Global claims

| id | Claim | Predicted |
| --- | --- | --- |
| G1 | every pool model answers at least one request | **false** — keys 2 and 3 are quota-dead (4 models) |
| G2 | the declared FAST bucket is genuinely fastest by TTFT | **false** — same reasoning as O9 |
| G3 | ≥3 of 17 lanes deliver a single buffered burst (TPS not derivable) | true |
| G4 | both codex models answer 200 under the D6 shape | true |
| G5 | `cascade/glm-5.3-flash` bills >10000 prompt tokens on the ~50-token prompt | true |
| G6 | ≥1 lane rejects `tools`+`tool_choice` with an HTTP 4xx instead of answering in text | true |

## 4. What would falsify this

- **TTFT/TPS rows** are scored as point errors (predicted − observed median, ms and tok/s) and as
  directional hits on the range: inside range = hit, outside = miss with the signed gap recorded.
- **`pass/9` rows** are scored as point errors against the graded pass count.
- **Failure-mode rows** are scored per model: the observed dominant class either matches the
  predicted class or does not; a lane predicted to work but graded 0 is a miss even if the TTFT
  point error is small.
- **O9/G2** are falsified if FAST's median TTFT comes out lower than MIDDLE's; that outcome would say
  the config's bucket labels describe intended role rather than measured speed, and the routing table
  should say so explicitly.
- A prediction of "no TPS" (burst) is falsified if the lane delivers an incremental flush with a
  decode span ≥50 ms in both reps.

Predictions were filed before any request to any real endpoint. The only network traffic before this
point in the mission was none: the runner did not exist yet, and the config was read from disk.
