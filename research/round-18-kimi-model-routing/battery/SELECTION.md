# R18 capability battery — probe target selection

Scope: `research/round-18-kimi-model-routing/battery/**`. Owner: mission M3 (`r18-battery`), branch
`feat/r18-capability-battery`.

## 1. What was selected

The target set is **the live `[secondary_model.models]` routing table** of
`~/.kimi-code/config.toml` — not a hand-picked sample, and not the pre-edit list carried in the
mission notes. Every id the routing table assigns is a probe target, so "every provider" and "every
routing bucket" are covered by construction.

| | |
| --- | --- |
| Config read | `~/.kimi-code/config.toml` |
| sha256 | `e3c223e054a626b847e69f73020ac9b4fdec1ccc2c8f00dcbf414dcda8acfe78` |
| Size / read time | 1521 lines, 2026-10-15T11:42Z |
| Pool entries selected | **17** (FAST 9, MIDDLE 6, STRONG 2) |
| Distinct provider configs | 9 of the 13 declared |

| # | Pool id | Provider | Protocol | Bucket (from the routing annotation) |
| --- | --- | --- | --- | --- |
| 1 | `cascade/glm-5.3-flash` | `glm-flash-cascade` (shim :8793, devin leg 1) | openai | FAST |
| 2 | `zai-coding-plan/glm-5.3-flash-low` | `zai-coding-plan` | openai | FAST |
| 3 | `cursor/composer-2.5` | `cursor` (shim :8788) | openai | FAST (annotated "VERY-FAST") |
| 4 | `cursor/cursor-grok-4.5-low-fast` | `cursor` (shim :8788) | openai | FAST (annotated "VERY-FAST") |
| 5 | `hyper/deepseek-v4.1-flash` | `hyper` | openai | FAST |
| 6 | `cascade/deepseek-v4.1-flash` | `ds-flash-cascade` (shim :8791) | openai | FAST |
| 7 | `alibaba-token-plan/deepseek-v4.1-flash` | `alibaba-token-plan` (key 1) | openai | FAST |
| 8 | `alibaba-token-plan-2/deepseek-v4.1-flash` | `alibaba-token-plan-2` (key 2) | openai | FAST |
| 9 | `alibaba-token-plan-3/deepseek-v4.1-flash` | `alibaba-token-plan-3` (key 3) | openai | FAST |
| 10 | `alibaba-token-plan/qwen3.8-flash` | `alibaba-token-plan` (key 1) | openai | MIDDLE |
| 11 | `alibaba-token-plan-2/qwen3.8-flash` | `alibaba-token-plan-2` (key 2) | openai | MIDDLE |
| 12 | `alibaba-token-plan-3/qwen3.8-flash` | `alibaba-token-plan-3` (key 3) | openai | MIDDLE |
| 13 | `zai-coding-plan/glm-5-turbo` | `zai-coding-plan` | openai | MIDDLE |
| 14 | `hyper/qwen3.8-flash` | `hyper` | openai | MIDDLE |
| 15 | `xai-oauth/grok-4.5` | `xai-oauth` (shim :8790) | openai | MIDDLE |
| 16 | `openai-codex/gpt-6.1-sol` | `openai-codex` (shim :8789) | openai_responses | STRONG |
| 17 | `openai-codex/gpt-6.1-sol-high` | `openai-codex` (shim :8789) | openai_responses | STRONG |

Bucket is read from the annotation text the config itself attaches to each entry ("FAST bucket",
"MIDDLE bucket", "STRONG bucket", "VERY-FAST lane"). Nothing here is re-bucketed by the battery; the
battery's job is to test whether the declared bucket survives measurement.

The alibaba-token-plan **3-key matrix** is covered in full: three provider sections that share one
base_url host and differ only in `api_key`, each contributing a FAST and a MIDDLE entry (6 models).
That is the only multi-key lane family the live pool declares.

## 2. Why this selection

1. **Operator directive 2026-10-15 — "test the models we have assigned in our pools."** The pool is
   the only set whose behaviour changes routing, so measuring anything else would not inform M4.
2. **Full pool, not a sample.** With 17 entries the cost of measuring all of them is bounded
   (10 requests per model, section 4), while a sample would leave M4 guessing about the entries it
   must keep, drop, or re-bucket.
3. **Every bucket is represented**, which makes the cross-bucket check possible: are lanes the config
   calls FAST actually faster than the ones it calls MIDDLE and STRONG? That check is the main
   deliverable, and it needs at least one measured lane per bucket.
4. **Dead-lane members stay in.** Keys 2 and 3 are quota-exhausted per the M1 census (D2). They are
   still in the pool, so they get exactly one attempt and a recorded failure class (never a retry),
   which is the evidence M4 needs to justify dropping them.

## 3. Pool diff vs the mission notes (finding for M4)

The mission notes carry a **pre-edit 26-model pool**. The live table holds **17**. The pre-edit list
came from a config that was rewritten at `2026-10-15T08:26` local (the same edit the M1 census
re-baselined against). Per the tower briefing, the live pool is what gets tested; the diff is
recorded here as the finding M4 needs.

**13 pre-edit ids are no longer in the pool** (removed from routing, not necessarily deleted from
`[models.*]`): `zai-coding-plan/glm-5.3-flash`, `hyper/glm-5.3-flash`,
`alibaba-token-plan/qwen3.8-max`, `alibaba-token-plan/qwen3.8-max-xhigh`,
`alibaba-token-plan-2/qwen3.8-max`, `alibaba-token-plan-3/qwen3.8-max`, `zai-coding-plan/glm-5.3`,
`hyper/qwen3.8-max`, `opencode-go/deepseek-v4.1-flash`, `opencode-go/gpt-6-luna`,
`openai-codex/gpt-6-luna`, `xai-oauth/grok-4.7`, `xai-oauth/grok-4.6`.

**4 ids are new**: `cascade/glm-5.3-flash`, `cascade/deepseek-v4.1-flash`,
`cursor/composer-2.5`, `cursor/cursor-grok-4.5-low-fast`.

Consequences worth M4's attention:

- The **STRONG bucket shrank from 13 declared models to 2** — both `openai-codex`, both the same
  underlying model (`gpt-6.1-sol`) with different effort pins. If either codex path is unavailable,
  the pool has no STRONG lane left. That is a single-provider dependency the pool did not have
  before this edit.
- The **cascade shims are now pool members in their own right** (`:8791` ds-flash, `:8793`
  glm-flash), and one of them (`glm-flash-cascade`) resolves its first leg to **devin**, which the
  M1 census flagged as a lane with an unbounded cold start (D7) and a ~11.7k-token fixed prompt
  overhead (D9). A FAST-bucket entry that pays that overhead is a routing contradiction worth
  checking, which the battery does.
- Three declared providers now have **no pool member at all**: `managed:kimi-code` (its 4 entries
  were never in the pool), `opencode-go`, and `devin`.

## 4. Probe plan (identical for every selected model)

| Probe | Requests | Shape | Measured |
| --- | --- | --- | --- |
| `perf` | 2 reps, sequential | streaming, `max_tokens` 256, temperature 0, fixed ~50-token prompt | TTFT ms, TPS, prompt/completion tokens, finish_reason, burst-vs-incremental |
| `c1`–`c5` | 5 | instruction/format contract, non-streaming, `max_tokens` 192 | exact-match / structural grade |
| `k1`–`k3` | 3 | tiny code tasks with exact-answer grading, `max_tokens` 192 | exact-match or exec-checked behaviour |
| `t1` | 1 | tool-call format probe (`tools` + `tool_choice`), `max_tokens` 192 | well-formed `tool_calls` block |
| `warmup` | 0 or 1 | devin-class lanes only, `max_tokens` 16, excluded from every metric | whether the cold start clears |

10 measured requests per model, 170 total, plus one warm-up for the devin-backed lane.

Design consequences, all deliberate:

- **TTFT and TPS come from the same request.** The binding methodology fixes the prompt and the
  `max_tokens≈256` for both; issuing one request per rep rather than two halves the quota cost
  without changing either definition. TTFT = send → first content-bearing delta; TPS =
  (last-token time − first-token time) / (server `completion_tokens` − 1), decode span excluding
  TTFT, as specified.
- **n = 2 reps, sequential within a model**, so a lane's own concurrency is never the variable.
  Models run with bounded concurrency (4 in flight).
- **`temperature` 0 everywhere it is accepted.** The codex protocol rejects `temperature` outright
  (M1 D6), so those two models omit it and the omission is recorded per request.
- **Codex shape** is the D6 shape: `store: false`, `stream: true` always, list-form `input`, no
  `temperature`, `max_output_tokens >= 16`.
- **Devin-class lanes** (`glm-flash-cascade`, first leg devin) get a 400 s timeout and one warm-up
  pre-call that is excluded from every metric, because M1 measured a cold start that blocked past
  180 s and 300 s. `ds-flash-cascade` is *not* given the warm-up: M1 evidence puts its first leg on
  opencode-go (48 prompt tokens vs glm-flash-cascade's 11734), so it is not devin-backed in practice.
- **One attempt per model on a dead lane.** If the first request for a model fails with an
  auth/quota/transport class error, the remaining probes for that model are recorded as
  `skipped_after_fatal` with the same class. No retries, so a quota-dead lane costs one request.
- **`max_tokens` 192 for correctness probes, not 64.** M1 §5 showed reasoning tokens are billed
  outside a small `max_tokens` cap, and `hyper` returned `finish_reason: length` on an 8-token
  request. A tiny cap would manufacture truncation failures that are an artefact of the probe, not
  of the model's instruction-following.
- **No `stream_options` fallback ladder.** `stream_options: {include_usage: true}` is sent on openai
  lanes (it worked across all openai lanes in M1). If a lane rejects it, that is recorded as a
  format/transport observation rather than retried in a second shape — one attempt per probe keeps
  the failure taxonomy honest.
