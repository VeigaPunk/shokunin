# R18 provider & model census — ANALYSIS

Scope: every provider and `[models.*]` entry in `~/.kimi-code/config.toml`, probed live on the date recorded in `manifest.json`. Raw captures live in `raw/`; `manifest.json` is the redacted inventory. Every number below is read out of one of those files by `scripts/build_analysis.py`, so re-running the probes and the generator reproduces this document — and `scripts/verify_numbers.py` enforces that claim mechanically, failing if any figure in this document appears in no capture.

## 1. Inventory

| Metric | Value |
| --- | --- |
| Providers | 13 |
| `[models.*]` entries | 143 |
| Distinct (provider, model) pairs | 140 |
| Distinct model base_urls | 12 |
| Models by protocol | anthropic: 6, kimi: 4, openai: 124, openai_responses: 9 |
| Default model | `kimi-code/kimi-for-coding` |
| Secondary-model default | `cascade/deepseek-v4.1-flash` |
| Config digest (sha256/16) | `61f22a2bbe52d616` |

Note: the 143 `[models.*]` entries resolve to 140 distinct (provider, model) pairs; the 3 extra entries are deliberate effort-pinning aliases that reuse a model id with an `overrides.default_effort` (for example `alibaba-token-plan/qwen3.8-max-xhigh` and `zai-coding-plan/glm-5.3-flash-low`). The distinction matters when counting what a lane can actually serve.

### Config provenance (read this before quoting any number)

This census was invalidated once by a mid-flight config edit and re-baselined. The first pass read a config with **11 providers and 139 model entries** and 4 local shim units; the config was rewritten at `2026-10-15T08:26:02-03:00` and now declares **13 providers and 143 model entries** and 6 shim units. Every number in this document was re-measured against the config whose digest is `61f22a2bbe52d616`. `scripts/run_census.sh` now prints the config digest before and after a run, so the same edit cannot invalidate a future census silently. The first-pass observation is recorded in `raw/census-first-pass.json`.

**How that digest is built** (it is easy to check the wrong way): it is `sha256(json.dumps(parsed_toml, sort_keys=True))[:16]` — the sha256 of the *parsed* TOML re-serialised with sorted keys, computed by `scripts/common.py:config_digest()`. It is **not** the sha256 of the file's bytes, so `sha256sum ~/.kimi-code/config.toml` will print a different value and that is expected. `scripts/run_census.sh` prints both, labelled `file_sha256_16` and `parsed_sha256_16`, so a reader can compare against whichever they have.

Because the config is live, treat the digest above as the census's identity: if `~/.kimi-code/config.toml` no longer hashes to it, re-run `scripts/run_census.sh` rather than trusting these tables.

## 2. Local shims

| Unit | Port | is-active | is-enabled | Listener | Config providers on that port |
| --- | --- | --- | --- | --- | --- |
| `devin-shim.service` | 8787 | active | enabled | yes | `devin` |
| `cursor-shim.service` | 8788 | active | enabled | yes | `cursor` |
| `codex-shim.service` | 8789 | active | enabled | yes | `openai-codex` |
| `xai-shim.service` | 8790 | active | enabled | yes | `xai-oauth` |
| `ds-flash-shim.service` | 8791 | active | enabled | yes | `ds-flash-cascade` |
| `glm-flash-shim.service` | 8793 | active | enabled | yes | `glm-flash-cascade` |

Shim units are discovered from `systemctl --user list-units` rather than hardcoded, so a shim added after this census was written still appears. All 6 discovered units are `active` + `enabled` with a live listener on their port (`raw/shims.json`, from `systemctl --user is-active|is-enabled` and `ss -ltnp`).

One further listener exists in the 8780-8800 range that no discovered shim unit owns and no config provider points at: `127.0.0.1:8799`. It is recorded because a stray listener on the shim port block is worth a glance, but nothing in the config references it, so it is an observation rather than a defect. Evidence: `raw/shims.json:listener_rows_8780_8800`.

**Credential exposure found while capturing this table.** Two of the cascade shim unit files carry live API keys in commented-out `Environment=` lines — `glm-flash-shim.service` holds the zai-coding-plan key verbatim and `ds-flash-shim.service` holds the opencode-go key. Their recorded modes are `0644` and `0644`, against the config's own `0600`, so the values sit outside the credential store's permissions; `~/.config` is a git repository, though both units are currently untracked and the repo has no remote, so they are not published. This is not a census artifact — the keys are in `~/.config/systemd/user/`, outside this mission's scope — and it was filed as a `vuln` TowerFinding rather than fixed here. `scripts/hygiene_check.sh` is what surfaced it: the first run exited non-zero on `raw/shims.json` because the shim probe had captured `systemctl --user cat` output verbatim. `probe_shims.py` now redacts at capture time, so no census artifact contains those values. See `HYGIENE.md`.

## 3. Census table

`/models` = HTTP status of `GET {base_url}/models` (5 s timeout). `served` = ids the endpoint returned. `cfg→res` = configured ids that appear in that listing. `chat` = status of one minimal completion (`max_tokens <= 8`, `temperature 0`) over the protocol the config declares; `chat ms` is the slowest of that lane's protocol probes. `usage` = the response carried a populated usage block.

| Provider | Auth | Protocol(s) | `/models` | ms | served | cfg→res | chat | chat ms | usage | Failure mode |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `managed:kimi-code` | oauth | kimi | 401 | 1539 | 0 | 4→0 | 401 | 576 | no | **auth failure** — OAuth token store empty; 401 on every path |
| `alibaba-token-plan` | api_key | openai | 200 | 1231 | 16 | 19→10 | 200 | 6769 | yes | id mismatch (9 configured ids not served) |
| `alibaba-token-plan-2` | api_key | openai | 200 | 1009 | 16 | 19→10 | 429 | 1032 | no | **quota exhausted** — 429 insufficient_quota, whole lane |
| `alibaba-token-plan-3` | api_key | openai | 200 | 1085 | 16 | 19→10 | 429 | 1032 | no | **quota exhausted** — 429 insufficient_quota, whole lane |
| `zai-coding-plan` | api_key | openai | 200 | 1034 | 11 | 7→5 | 200 | 2159 | yes | id mismatch (2 configured ids not served) |
| `hyper` | api_key | openai | 200 | 293 | 21 | 21→21 | 200 | 6938 | yes | none observed |
| `opencode-go` | api_key | anthropic,openai,openai_responses | 200 | 679 | 37 | 31→29 | 200, 200, 200 | 1978 | yes | id mismatch (2 configured ids not served) |
| `openai-codex` | api_key | openai_responses | 400 | 145 | 0 | 2→2 | 400 | 381 | no | **base_url/route mismatch** — `{base_url}/models` is not the shim's static route; chat needs a narrow streaming shape (see the defect list) |
| `devin` | api_key | openai | 200 | 1 | 9 | 9→9 | timeout | 180052 | no | **unbounded cold start** — /models fine; first chat attempt blocked 180s then 300s |
| `xai-oauth` | api_key | openai | 200 | 247 | 14 | 3→3 | 200 | 1930 | yes | none observed |
| `cursor` | api_key | openai | 200 | 1 | 259 | 4→4 | 200 | 6917 | yes | none observed |
| `ds-flash-cascade` | api_key | openai | 200 | 1 | 1 | 1→1 | 200 | 1844 | yes | none observed |
| `glm-flash-cascade` | api_key | openai | 200 | 1 | 1 | 1→1 | 200 | 4242 | yes | none observed |

Per-lane detail, including every id that did and did not resolve, is in `raw/models-<lane>.json`; per-protocol chat shape is in `raw/chat-<lane>.json`.

### Ids that did not resolve

| Provider | Configured | Served | Unresolved ids |
| --- | --- | --- | --- |
| `managed:kimi-code` | 4 | 0 | `k3`, `k3-256k`, `kimi-for-coding`, `kimi-for-coding-highspeed` |
| `alibaba-token-plan` | 19 | 16 | `MiniMax-M2.5`, `deepseek-v3.2`, `deepseek-v4-flash`, `deepseek-v4-pro-0813`, `glm-5`, `glm-5.1`, `kimi-k2.5`, `kimi-k2.6`, `qwen3.6-plus` |
| `alibaba-token-plan-2` | 19 | 16 | `MiniMax-M2.5`, `deepseek-v3.2`, `deepseek-v4-flash`, `deepseek-v4-pro-0813`, `glm-5`, `glm-5.1`, `kimi-k2.5`, `kimi-k2.6`, `qwen3.6-plus` |
| `alibaba-token-plan-3` | 19 | 16 | `MiniMax-M2.5`, `deepseek-v3.2`, `deepseek-v4-flash`, `deepseek-v4-pro-0813`, `glm-5`, `glm-5.1`, `kimi-k2.5`, `kimi-k2.6`, `qwen3.6-plus` |
| `zai-coding-plan` | 7 | 11 | `glm-5.2-highspeed`, `glm-5.3-highspeed` |
| `opencode-go` | 31 | 37 | `deepseek-v4-flash`, `deepseek-v4-flash-vision-exp` |

## 4. Defects

### D1. managed:kimi-code returns 401 on every endpoint; its OAuth token store is empty

Both `GET {base_url}/models` and a minimal chat completion return HTTP 401 `invalid_authentication_error` / `Invalid Authentication`. The config declares `storage = "file"` with `key = "oauth/kimi-code-env-0e4f99c69cc27850"`, and that file exists but is 0 bytes, so no bearer token can be minted from it. Every one of the 4 configured models is therefore unreachable, including `default_model = kimi-code/kimi-for-coding`. **Scope of this claim:** the lane is unreachable to any client relying on the on-disk credential store — which is what this probe, and any client started fresh from the config, does. A live session already holding a valid in-memory token is not covered by this probe, so a working interactive `kimi` session is not evidence against this finding. Evidence: `raw/models-managed-kimi-code.json`, `raw/chat-managed-kimi-code.json`.

**Suggested fix.** Re-authenticate the kimi-code provider so the token store is populated, or point `default_model` at a lane that answers.

### D2. token-plan keys 2 and 3 are quota-exhausted for the whole lane

Chat on key 2 returns 429 `insufficient_quota` — "Your token-plan 1-month quota has been exhausted. The quota will reset at 10-23 16:00:00 UTC" — with `retry-after: 707432`. Key 3 returns the same with a 10-28 16:00:00 UTC reset and `retry-after: 1139431`. Re-probing the *fast* model each lane is routed to (`deepseek-v4.1-flash`) reproduces the 429 with `retry-after: 707213` and `1139212`, so this is not flagship-model-specific. `GET /models` still answers 200 on both keys, which means an endpoint listing is not evidence of usable quota. The current config still lists `alibaba-token-plan-2/deepseek-v4.1-flash` and its key-3 twin in `[secondary_model.models]`, so subagent dispatch keeps landing on two dead lanes. Evidence: `raw/chat-alibaba-token-plan-2.json`, `raw/chat-alibaba-token-plan-3.json`, `raw/recheck-quota-lanes.json`.

**Suggested fix.** Remove or quarantine keys 2 and 3 from the secondary-model routing table until their reset times (10-23 16:00:00 UTC and 10-28 16:00:00 UTC), or make the cascade lanes absorb them.

### D3. Configured ids that the endpoint refuses: alibaba `glm-5`, zai `glm-5.3-highspeed`

These ids are absent from their lane's `/models` listing, and a direct chat completion confirms they are genuinely unentitled rather than merely unlisted: `alibaba-token-plan/glm-5` returns 403 "Access to model denied. Please make sure you are eligible for using the model." and `zai-coding-plan/glm-5.3-highspeed` returns 429 "Your current subscription plan does not yet include access to GLM-5.3-Highspeed". Evidence: `raw/chat-unresolved-id-checks.json`.

**Suggested fix.** Drop both ids from config, or move them behind a lane that is entitled.

### D4. `/models` is an incomplete oracle — some configured ids work while unlisted

`opencode-go/deepseek-v4-flash` is absent from that lane's 37-id `/models` listing yet a direct chat completion returns 200 with a populated usage block. The same holds on the token-plan lanes, where 9 configured ids are unlisted. So the "unresolved" column below is a prompt to re-check, not proof of breakage — which is exactly why D3's two ids needed a chat probe to separate them from this case. Evidence: `raw/chat-unresolved-id-checks.json`, `raw/models-opencode-go.json`.

**Suggested fix.** Do not use `/models` membership as a routing gate; gate on a real completion.

### D5. `openai-codex` base_url does not reach the shim's model route

The provider declares `base_url = http://127.0.0.1:8789/backend-api/codex`, so `{base_url}/models` resolves to `/backend-api/codex/models` and the upstream answers 400 `missing query parameter: client_version`. The shim's own static list lives at `/v1/models` and returns 200 with `gpt-6.1-sol, gpt-6-luna`. Evidence: `raw/models-openai-codex.json`.

**Suggested fix.** Expected for a Responses-protocol lane; if model listing matters, the shim should serve it under the configured prefix too.

### D6. `openai-codex` accepts only a narrow streaming request shape (no `temperature`, `max_output_tokens` floor of 16)

A shape ladder against the lane returns, in order: 400 `Input must be a list`, 400 `Store must be set to false`, 400 `Stream must be set to true`, 400 `Unsupported parameter: temperature`, 400 `Invalid 'max_output_tokens': integer below minimum value. Expected a value >= 16, but got 8`, and finally 200 with the minimal shape. The lane therefore **works** — it streams `response.created` … `response.output_text.delta` … and answers `"pong"` — but it cannot satisfy a `max_tokens <= 8` probe, and any client that sends `temperature` or `store: true` will be rejected. Evidence: `raw/chat-openai-codex-input-list.json`.

**Suggested fix.** Treat the census's `max_tokens <= 8` figure as inapplicable to this lane; a client must omit `temperature` and set `store: false`.

### D7. The devin chat path has an unbounded cold-start latency

On the first pass a minimal chat completion did not return within 180 s, nor within a 300 s retry (`raw/recheck-devin-chat.json`). A later streaming probe against the same shim returned 200 with TTFT 3715 ms and 61 completion tokens (`raw/stream-devin.json`), so the lane does work — the failure was a cold `devin acp` start, not a dead path. `GET {base_url}/models` answers 200 and all 9 configured ids resolve. The practical consequence is that the first request after the shim has been idle can block for minutes with no bound. Evidence: `raw/chat-devin.json`, `raw/recheck-devin-chat.json`, `raw/stream-devin.json`, `raw/shims.json`.

**Suggested fix.** Warm the shim on service start (or add a healthcheck that issues one throwaway turn), so the first real request does not pay the cold start.

### D8. `opencode-go` model-level `base_url` overrides point at a path with no `/models`

Six `opencode-go` model entries declare `base_url = https://opencode.ai/inference/go` (no `/v1`). `GET {that}/models` returns 404, while the provider-level `.../go/v1/models` returns 200 with 37 ids. The override is correct for the `anthropic` protocol those entries use (`/v1/messages`), so this is a documentation trap rather than a break — but it means the override base_url must never be used for model listing. Evidence: `raw/models-opencode-go.json`.

**Suggested fix.** No change required; note it so tooling does not derive a `/models` URL from a model-level base_url.

### D9. The devin-backed lanes bill a large fixed prompt overhead

Every streaming probe in section 6 sent the *same* short prompt, so `prompt_tokens` differences are the lane's own overhead. The spread is 24 to 12163 tokens:

| Lane | Model | prompt_tokens for the identical prompt | Starts on a devin leg |
| --- | --- | --- | --- |
| `devin` | `deepseek-v4-1-flash-high` | 12163 | yes |
| `glm-flash-cascade` | `glm-5.3-flash` | 11734 | yes |
| `xai-oauth` | `grok-4.7` | 1260 | no |
| `alibaba-token-plan` | `deepseek-v4-flash-0731` | 101 | no |
| `ds-flash-cascade` | `deepseek-v4.1-flash` | 48 | no |
| `hyper` | `glm-5.3-flash` | 31 | no |
| `opencode-go` | `glm-5.3-flash` | 30 | no |
| `zai-coding-plan` | `glm-5.3-flash` | 30 | no |
| `openai-codex` | `gpt-6.1-sol` | 24 | no |

The 2 lanes that start on a devin leg are the extreme cases: `devin` (12163), `glm-flash-cascade` (11734). The devin shim drives a `devin acp` subprocess, which appends a large fixed system prompt, so a short subtask routed to a devin leg pays for it. The contrast is inside the same mechanism: `ds-flash-cascade` starts on opencode-go and billed 48 tokens for the identical request, while `glm-flash-cascade`, which starts on devin, billed 11734. So the overhead belongs to the devin leg, not to the cascade wrapper. Lanes at or above 1000 tokens: `devin` (12163), `glm-flash-cascade` (11734), `xai-oauth` (1260). Lanes below it: `openai-codex` (24), `opencode-go` (30), `zai-coding-plan` (30), `hyper` (31), `ds-flash-cascade` (48), `alibaba-token-plan` (101). Evidence: `raw/stream-<lane>.json`.

**Suggested fix.** If a devin leg is going to be used for short subtasks, the per-call prompt overhead should be trimmed or the leg reserved for work where a few thousand prompt tokens are noise.

## 5. Usage / quota evidence (operator add-on)

Signals were taken only from the credentials already in the config, via two sources: the `usage` block and rate-limit headers of the minimal chat probe already captured (read, not re-issued — no extra quota), and a bounded set of GETs against plausible usage/account paths on each lane's own base_url host. Those paths were probed and reported, never assumed.

| Lane | Auth | `usage` block from chat | Rate-limit / quota headers | Account-endpoint probes |
| --- | --- | --- | --- | --- |
| `managed:kimi-code` | oauth | absent | none returned | coding/v1/usage→404; coding/v1/user/balance→404; coding/v1/dashboard/billing/usage→404; coding/v1/quota→404; coding/v1/account/usage→404; usage→404; v1/usage→404 |
| `alibaba-token-plan` | api_key | {"prompt_tokens": 11, "total_tokens": 372, "completion_tokens": 361, "prompt_tokens_details": {"cached_tokens": 0}, "completion_tokens_details": {"reasoning_tokens": 344}} | {"x-request-id": "938810ca-af56-42ba-bab3-6979f7171113"} | compatible-mode/v1/usage→404; compatible-mode/v1/user/balance→404; compatible-mode/v1/dashboard/billing/usage→404; compatible-mode/v1/quota→404; compatible-mode/v1/account/usage→404; usage→404; v1/usage→404 |

**`managed:kimi-code` — exposes no usage signal at all.** Its chat probe is a 401 with no `usage` block and no rate-limit headers, and all 7 probed usage/account paths (`/usage`, `/user/balance`, `/dashboard/billing/usage`, `/quota`, `/account/usage` under the declared base_url, plus `/usage` and `/v1/usage` at the host root) return 404. So this lane's consumption is not observable with the credentials currently in the config — the absence is the finding, as the tower anticipated. Evidence: `raw/usage-managed-kimi-code.json`.

**`alibaba-token-plan` (key 1) — usage visible, quota not.** A 200 chat completion returns a full `usage` block including a reasoning breakdown, but no rate-limit or quota headers, and every usage/account path 404s. Key 1 is alive; keys 2 and 3 report their exhaustion in the *error body* of a 429 rather than in a quota header, with `retry-after` as the only machine-readable field. Evidence: `raw/usage-alibaba-token-plan.json`, `raw/recheck-quota-lanes.json`.

**Reasoning tokens are billed but not capped by `max_tokens`.** The chat probes asked for at most 8 output tokens, yet these lanes reported far more completion tokens, nearly all of them reasoning:

| Lane | Model | completion_tokens | reasoning_tokens | max_tokens asked | finish_reason |
| --- | --- | --- | --- | --- | --- |
| `alibaba-token-plan` | `qwen3.7-max` | 361 | 344 | 8 | stop |
| `hyper` | `qwen3.7-max` | 415 | 398 | 8 | length |

A tiny `max_tokens` therefore does not bound a thinking model's actual spend, which matters for any quota arithmetic that assumes it does. Evidence: the `raw/chat-*.json` captures above.

**Lanes that do expose quota telemetry** (read from the captures, not asserted):

| Lane | Model | Usage cost/remaining fields | Quota headers |
| --- | --- | --- | --- |
| `hyper` | `qwen3.7-max` | {"cost": {"usd": 0.00314, "hypercredits": 0.0628}, "remaining": {"hypercredits": 231.76623379999998}} | {"x-ratelimit-limit-day": "10000", "x-ratelimit-limit-hour": "1000", "x-ratelimit-remaining-day": "9434", "x-ratelimit-remaining-hour": "839"} |
| `openai-codex` | `gpt-6.1-sol` | — | {"x-codex-active-limit": "premium", "x-codex-plan-type": "pro", "x-codex-primary-used-percent": "1", "x-codex-secondary-used-percent": "0", "x-codex-primary-window-minutes": "10080", "x-codex-primary-over-secondary-limit-percent": "0", "x-codex-secondary-window-minutes": "0", "x-codex-primary-reset-after-seconds": "585645", "x-codex-secondary-reset-after-seconds": "0", "x-codex-primary-reset-at": "1792649629", "x-codex-secondary-reset-at": "", "x-codex-credits-has-credits": "True", "x-codex-credits-balance": "62500.0000000000", "x-codex-credits-unlimited": "False", "x-codex-turn-state": "<len=780>", "x-codex-safety-buffering-enabled": "true", "x-codex-safety-buffering-faster-model": "gpt-6-luna"} |
| `xai-oauth` | `grok-4.7` | {"num_sources_used": 0, "cost_in_usd_ticks": 3046400} | {"x-ratelimit-limit-tokens": "53000000", "x-ratelimit-remaining-tokens": "53000000", "x-ratelimit-limit-requests": "8300", "x-ratelimit-remaining-requests": "8300", "x-request-id": "17b6de1c-c856-9dd3-8aff-831da5d51a5c"} |
| `zai-coding-plan` | `glm-5.3-flash` | — | {"X-Request-ID": "5a5f3309-72c6-4173-99f3-880dc1aaa50a"} |
| `alibaba-token-plan` | `qwen3.7-max` | — | {"x-request-id": "938810ca-af56-42ba-bab3-6979f7171113"} |

A lane that is absent from this table returned neither a cost/remaining field nor a quota header on its probe.

## 6. TTFT / TPS smoke (operator add-on)

One streaming request per lane and per declared protocol, with a fixed identical short prompt ("Count from 1 to 30, space separated, numbers only. No other text.") and `max_tokens = 64`. `TTFT` is measured from request send to the first content-bearing chunk; `TPS` excludes TTFT and uses the server-side `usage` completion-token count as the numerator (`(completion_tokens - 1) / decode span`). `ttft(think)` is the first *reasoning* chunk when the lane streams one before any content. Streaming was not forced: a lane that answers with one complete JSON body, or errors on `stream: true`, is recorded as not streaming.

| Lane | Protocol | Model | Status | Streaming | TTFT ms | ttft(think) ms | TPS | completion_tokens | prompt_tokens | decode span ms | content deltas | Note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `managed:kimi-code` | kimi | `kimi-for-coding` | 401 | n/a | — | — | — | — | — | — | 0 | probe failed (status 401) |
| `alibaba-token-plan` | openai | `deepseek-v4-flash-0731` | 200 | yes | 2496 | 2287 | 207.17 | 64 | 101 | 304 | 11 | — |
| `alibaba-token-plan-2` | openai | `deepseek-v4-flash-0731` | 429 | n/a | — | — | — | — | — | — | 0 | probe failed (status 429) |
| `alibaba-token-plan-3` | openai | `deepseek-v4-flash-0731` | 429 | n/a | — | — | — | — | — | — | 0 | probe failed (status 429) |
| `zai-coding-plan` | openai | `glm-5.3-flash` | 200 | yes | 3163 | 3163 | — | 64 | 30 | 0 | 28 | not derivable: stream was not incrementally flushed (decode span 0 ms < 50 ms) |
| `hyper` | openai | `glm-5.3-flash` | 200 | yes | 533 | 418 | — | 64 | 31 | 0 | 1 | not derivable: stream was not incrementally flushed (decode span 0 ms < 50 ms) |
| `opencode-go` | openai | `glm-5.3-flash` | 200 | yes | 1198 | 822 | 269.3 | 64 | 30 | 234 | 10 | — |
| `opencode-go` | anthropic | `qwen3.8-flash` | 200 | yes | 2587 | 1293 | 25.11 | 64 | 80 | 2509 | 3 | — |
| `opencode-go` | openai_responses | `grok-4.7` | 200 | yes | 3018 | 2574 | — | 154 | 1260 | 6 | 59 | not derivable: stream was not incrementally flushed (decode span 6 ms < 50 ms) |
| `openai-codex` | openai_responses | `gpt-6.1-sol` | 200 | yes | 1525 | — | 64.2 | 63 | 24 | 966 | 59 | — |
| `devin` | openai | `deepseek-v4-1-flash-high` | 200 | yes | 3715 | — | — | 61 | 12163 | 0 | 1 | not derivable: stream was not incrementally flushed (decode span 0 ms < 50 ms) |
| `xai-oauth` | openai | `grok-4.7` | 200 | yes | 1166 | — | 493.74 | 59 | 1260 | 117 | 59 | — |
| `cursor` | openai | `composer-2.5-fast` | 200 | yes | 5966 | — | — | — | — | 0 | 1 | not derivable: stream was not incrementally flushed (decode span 0 ms < 50 ms) |
| `ds-flash-cascade` | openai | `deepseek-v4.1-flash` | 200 | yes | 2467 | 2467 | — | 64 | 48 | 0 | 7 | not derivable: stream was not incrementally flushed (decode span 0 ms < 50 ms) |
| `glm-flash-cascade` | openai | `glm-5.3-flash` | 200 | yes | 4349 | — | — | 61 | 11734 | 0 | 1 | not derivable: stream was not incrementally flushed (decode span 0 ms < 50 ms) |

**These are smoke-level numbers from a single small draw per lane**, with a prompt short enough that TTFT is dominated by connection and prefill overhead rather than prompt length. The powered TTFT/TPS benchmark with n >= 2 reps is the M3 battery's job; this table is the census-level first look, and its job is to say which lanes stream at all and roughly how they compare.

Raw stream captures (SSE previews redacted, per-line timing kept) are in `raw/stream-<lane>.json`; the flattened view is `raw/stream-summary.json`.

**Reading the TPS column.** 12 of 15 probe rows streamed incrementally, 0 returned no incremental deltas at all, and 3 could not be stream-probed. Of the rows that did stream, 7 delivered their tokens in a single buffered burst (decode span under 50 ms), so no TPS is reported for them — a throughput figure derived from a burst is a measurement artefact, not throughput. Those lanes are: `zai-coding-plan` (openai), `hyper` (openai), `opencode-go` (openai_responses), `devin` (openai), `cursor` (openai), `ds-flash-cascade` (openai), `glm-flash-cascade` (openai).

## 7. How this was produced

```
python3 scripts/build_manifest.py          # -> manifest.json (redacted)
python3 scripts/probe_shims.py             # -> raw/shims.json
python3 scripts/probe_models.py            # -> raw/models-*.json
python3 scripts/probe_chat.py              # -> raw/chat-*.json
python3 scripts/probe_codex_input_shape.py # -> raw/chat-openai-codex-input-list.json
python3 scripts/probe_rechecks.py          # -> raw/recheck-*.json
python3 scripts/probe_stream.py            # -> raw/stream-*.json  (TTFT/TPS)
python3 scripts/probe_usage.py             # -> raw/usage-*.json
python3 scripts/build_analysis.py          # -> ANALYSIS.md
python3 scripts/verify_numbers.py          # every ANALYSIS.md figure traces to a capture
bash    scripts/hygiene_check.sh           # -> HYGIENE.md (0 hits expected)
```

Quota politeness: one `/models` GET per provider plus one supplementary GET per distinct model-level base_url; one 8-token chat completion per provider and per declared protocol; three targeted id checks; two quota re-checks; one 64-token streaming request per lane and protocol. No lane was loop-chatted. The census was run twice because the first pass was invalidated by a config edit, and `devin` was probed at length both times because its chat path kept hitting the timeout while its streaming path answered.

Secrets handling: `scripts/common.py` reads credentials from the config at runtime and passes them only into request headers. Captures record which credential headers were *sent* (names, never values); `Authorization`, `Set-Cookie` and the session-header value are replaced with a length marker; key material appears only as a sha256 digest in `manifest.json`. `HYGIENE.md` records the scan that proves it.

## 8. What this census does not cover

- **Tool / function calling.** The routing table marks several lanes "CHAT-ONLY (no tool calls)" and the cascade entries claim their first two legs are tool-capable while the devin leg is not. This census issued text completions and model listings only, so none of those claims are tested here. A tool-call probe (one request carrying a trivial function schema, checking for a `tool_calls` / `tool_use` block) is the natural next step and is cheap.
- **Effort-parameter behaviour.** `support_efforts`, `default_effort` and the `off_effort` values per model were inventoried but not exercised, nor was the xai shim's documented rewriting of unsupported `reasoning_effort` values.
- **Multimodal input.** `image_in` / `video_in` / `audio_in` capabilities are recorded from config; no image, video or audio payload was sent.
- **Context limits.** `max_context_size` / `max_output_size` are recorded from config and were not validated against the endpoints.
- **Powered TTFT/TPS.** Section 6 is a single small draw per lane. The n >= 2 benchmark belongs to the M3 battery.

