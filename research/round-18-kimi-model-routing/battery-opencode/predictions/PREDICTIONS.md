# R18 opencode-go deepseek probe — ex-ante predictions

**Filed 2026-10-15T12:41:43Z, before the first real request** (see `ordering.log` and the sibling
`.sha256`). Machine-readable twin: `PREDICTIONS.json`, the file the close-out scorer reads.

Lane under test: `opencode-go/deepseek-v4.1-flash` — the `[models.opencode-go/deepseek-v4.1-flash]`
entry, reached through provider `opencode-go` (`https://opencode.ai/inference/go/v1`, openai
protocol). It was in the pre-edit 26-model pool but is **not** in the live
`[secondary_model.models]` table, so the M3 battery (which tested exactly the live pool) never
measured it. It is the first leg of the live `cascade/deepseek-v4.1-flash` lane.

## Calibration base — the measured siblings and the leg-1 proxy

| source | lane / probe | number used here |
| --- | --- | --- |
| M3 ANALYSIS §2 | `hyper/deepseek-v4.1-flash` (same model id, direct provider) | TTFT med 2081 ms (reps 1807 / 2355), TPS med 375.91 (366.1 / 385.8), 8/9, c5 truncation, incremental |
| M3 ANALYSIS §2 | `alibaba-token-plan/deepseek-v4.1-flash` (same model id, gateway) | first-decoded 2251 ms (no content token in the 256-token budget), TPS 226.72 (215.2 / 238.3), 8/9, c5 truncation, incremental |
| M3 ANALYSIS §2 | `cascade/deepseek-v4.1-flash` (leg 1 **is** opencode-go) | TTFT 3179 ms, burst flush, 8/9 |
| M1 census `raw/stream-summary.json` | `ds-flash-cascade` shim, model `deepseek-v4.1-flash`, 64-token smoke | 2467 ms to first decoded token (reasoning first), content 48 chars, burst flush, upstream headers `x-opencode-endpoint-id` / `x-zen-model` / `server: cloudflare` prove the opencode-go upstream |
| M2 definitions ANALYSIS §1 | opencode-go transport constraint | scripted Python UA → `403 error code 1010` (Cloudflare); browser UA → 200. This probe sends the browser UA class, so a 403 is not expected; if it appears it is a lane-level auth wall, not this probe's artifact |

Reasoning behind the numbers: the two sibling lanes that serve this exact model id sit at
2081 ms and 2251 ms; the only direct observation *of this provider* is 2467 ms, and it was taken
through a local buffering shim, i.e. it is an upper bound on the direct lane. A public gateway with
Cloudflare in front should not beat a direct provider, so the prediction is anchored between the
slowest sibling and the shim proxy.

## 1. The lane's prediction

`pass/9` = expected passes over the 9 correctness probes (c1–c5, k1–k3, t1). TTFT is the median of
the two reps.

| field | predicted | range | basis |
| --- | --- | --- | --- |
| TTFT med ms | 2500 | 1700–3800 | siblings 2081 / 2251, leg-1 shim proxy 2467, cascade upper bound 3179 |
| TTFT reps | 2400 / 2600 | — | both siblings' reps spread by 548 ms (hyper) and 1506 ms (token-plan) |
| TPS med tok/s | 240 | 110–430 | token-plan sibling 226.72, hyper sibling 375.91; both are the same backend |
| TPS derivable | yes | — | a direct HTTP lane, not a local buffering shim (the burst lanes in M3 were the shims) |
| content token inside the 256-token budget | yes, at least one rep | — | cascade rep 1 and the census smoke both emitted content; token-plan emitted none |
| pass /9 | 8 | 7–9 | both measured siblings scored 8/9, failing exactly c5 with `truncation` |
| failing probe | c5 | — | identical failure on `hyper/…` and `alibaba-token-plan/…` |
| dominant failure class | truncation | — | the model is `always_thinking` at this budget |
| stream shape | incremental | — | direct provider-style stream; M3's burst lanes were all local shims |

Predicted failure modes, most to least likely:

1. **truncation** — reasoning consumes the fixed 192-token correctness budget before content
   (c5; the same failure both siblings showed).
2. **transport** — gateway queueing/timeout: opencode.ai adds Cloudflare + router hops; a 120 s
   socket timeout is not expected but is the natural second-order risk.
3. **auth** — only if the M2 UA block reappears despite the browser UA class (predicted not to).
4. **format_break** — a rejected tool probe (`tools` + `tool_choice: auto`). M2 pass 2 already
   returned a well-formed tool call on opencode-go with the openai shape, so this is the least
   likely.

## 2. Ordering claims

| id | claim | predicted |
| --- | --- | --- |
| OC1 | this lane's TTFT med is below `cascade/deepseek-v4.1-flash`'s measured 3179 ms | true |
| OC2 | this lane's TTFT med is within ±25 % of the median of its two measured siblings (2166 ms → 1625–2708 ms) | true |
| OC3 | this lane's TTFT med is above `hyper/deepseek-v4.1-flash`'s 2081 ms | true |
| OC4 | this lane's TPS med is below `hyper/deepseek-v4.1-flash`'s 375.91 tok/s | true |
| OC5 | this lane's TPS med is above `alibaba-token-plan/deepseek-v4.1-flash`'s 226.72 tok/s | true, low confidence (point 240 is only 6 % above the sibling) |
| OC6 | this lane's pass count equals both siblings' 8/9 | true |
| OC7 | stream shape is incremental, i.e. TPS is derivable | true |

## 3. Global claims

| id | claim | predicted |
| --- | --- | --- |
| OG1 | every request returns 200; none returns 403/1010 | true |
| OG2 | the server `usage` block is present and `completion_tokens` is readable | true |
| OG3 | the perf probe bills ≥ 80 prompt tokens on the ~50-token prompt (siblings billed 89) | true |
| OG4 | at least one probe consumes its entire output budget on reasoning tokens | true |
| OG5 | the response `model` field echoes `deepseek-v4.1-flash` (no silent reroute) | true |
| OG6 | the tool probe returns a well-formed `get_weather` call | true |

## 4. Routing prediction (to be tested against the measurement)

The question the operator asked is whether this lane deserves a **FAST-bucket slot** on its own
rather than only existing inside the cascade. Predicted decision rule, fixed before the run:

- **Earns a direct FAST slot** if TTFT med ≤ 2800 ms (inside the FAST band the siblings occupy) and
  pass ≥ 8/9. Predicted: **true** (2500 ms, 8/9).
- **Does not** earn a slot if TTFT med > 3179 ms (the cascade's measured leg-1 time) or pass ≤ 6/9.
- The cascade lane keeps its value regardless: its worth is the fallback chain (hyper, then devin),
  not its speed — leg 1 alone is not redundant with a direct entry when leg 1's own quota or
  availability is the thing that fails.

## 5. Scoring rules (fixed before the run)

- TTFT/TPS/pass rows are scored as signed point errors (predicted − observed median / count).
- Range claims are hit/miss by containment.
- Ordering and global claims come back hit, miss, or unprovable (a claim is unprovable when one
  side has no usable measurement).
- Failure-mode claims are scored on the dominant observed class and on the identity of the failing
  probe.
