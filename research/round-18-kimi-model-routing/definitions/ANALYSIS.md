# R18 definitions audit — ANALYSIS

Scope: every `[models.*]` entry in `~/.kimi-code/config.toml` — their declared
limits, capabilities, effort values, reasoning key, protocol and base_url — plus
what the shipped client actually transmits for each of those declarations.

| Metric | Value |
| --- | --- |
| Config path | `/home/vgpnk/.kimi-code/config.toml` |
| Config file sha256 | `e3c223e054a626b847e69f73020ac9b4fdec1ccc2c8f00dcbf414dcda8acfe78` |
| Config json-canonical digest/16 | `61f22a2bbe52d616` |
| Providers | 13 |
| `[models.*]` entries | 143 |
| Distinct (provider, model) pairs | 140 |
| Global `[thinking] effort` | `max` |
| Findings | 121 defects, 94 notes, 46 verify-later |

**Provenance.** The json-canonical digest above is `61f22a2bbe52d616`, byte-identical
to the digest the M1 census was measured against, so every census finding (D1–D9)
still applies to this config and is used as evidence below without re-probing it.
The file-bytes digest of the same file is `e3c223e054a626b8`; the two differ because M1 digests
the parsed structure, not the bytes. No config edit happened between the two missions.

---

## 1. Method and probe budget

Three evidence channels, in increasing order of cost:

1. **Static audit** (`scripts/audit_definitions.py`) — reads the config and the
   client binary's own strings; costs nothing. The binary is an unstripped Rust
   build, so a declared field that never appears in it cannot be parsed:

   | field | occurrences in `~/.kimi-code/bin/kimi` |
   | --- | --- |
   | `max_input_size` | 0 |
   | `off_effort` | 0 |
   | `protocol` | 5 |
   | `max_output_size` | 6 |
   | `reasoning_key` | 12 |
   | `max_context_size` | 16 |
   | `display_name` | 19 |
   | `support_efforts` | 22 |
   | `default_effort` | 25 |
   | `overrides` | 238 |
   | `capabilities` | 390 |

   The two zeros are the audit's first hard result: **`off_effort` and
   `max_input_size` are not fields this client knows.** `kimi doctor config`
   reports nothing about them because it does not validate model-level keys at
   all — a config with a deliberately misspelled model key (`zzz_unknown_key`),
   a bogus effort value and a bogus capability is reported as valid, so doctor's
   silence is not evidence either way (verified, see section 7).

2. **Client wire capture** (`scripts/probe_client_semantics.py` +
   `scripts/mock_provider.py`) — runs the real client against a loopback mock
   provider and records the request it builds. Zero quota: the upstream is local.
   This is what turns "declared" into "transmitted".

3. **Live probes** (`scripts/probe_live.py`) — one request per cell against the
   real lanes. Budget: 72 requests in total across three passes, every one of them
   minimal (`max_tokens` 16, 256 for the tool suite after pass 1 showed thinking
   models spend the whole 16-token budget on reasoning before emitting a call).
   No loops, no repeats except one deliberate reproducibility row.

Two method corrections were forced by the evidence and are worth stating, because
both first-pass results were probe artefacts, not lane properties:

- **User-Agent.** With Python's default UA, every `opencode-go` request returned
  `403 error code: 1010` (a Cloudflare block). The same request with a browser UA
  returned 200. Pass 1's opencode-go rows are therefore void and were re-run in
  pass 2 (`raw/probes-*-pass2.json`).
- **`tool_choice`.** Forcing a tool choice returned 400 on the `hyper` and
  `opencode-go`/anthropic lanes. The mock capture shows the client **never sends
  `tool_choice` at all** — it sends `tools` and lets the model decide — so the
  400s measured the probe, not the lane. Pass 3 re-ran those cells in the
  client's own shape and all three returned a well-formed tool call.

---

## 2. The audit table

The full per-entry table (all 143 entries, every field the mission asked for) is
`audit-table.md`; `audit-table.json` carries the same rows plus every finding.
Summary of what is declared:

| Dimension | Values across the file |
| --- | --- |
| protocols | anthropic, kimi, openai, openai_responses |
| effort values declared | high, low, max, medium, minimal, xhigh |
| `off_effort` values | none |
| `default_effort` values | high, low, max, xhigh |
| entries with no `max_output_size` | 25 |
| entries declaring `off_effort` | 10 |
| entries declaring `max_input_size` | 9 |

---

## 3. What the client actually transmits (mock capture)

One request per test model against a loopback provider, two config flavours
(`global_max` = the live `[thinking] effort = "max"`, `no_global` = the same file
with that line removed). Evidence: `raw/client-semantics.json`; reproduce with
`python3 scripts/probe_client_semantics.py`.

| declared | sent (global effort present) | sent (global effort absent) |
| --- | --- | --- |
| `mock/plain` | effort='max'<br>tools=25 | effort=None<br>tools=25 |
| `mock/offnone` | effort='max'<br>tools=25 | effort='high'<br>tools=25 |
| `mock/noonf` | effort='max'<br>tools=25 | effort='high'<br>tools=25 |
| `mock/offeffs` | effort='max'<br>tools=25 | effort='high'<br>tools=25 |
| `mock/override` | effort='max'<br>tools=25 | effort='low'<br>tools=25 |
| `mock/xhigh` | effort='max'<br>tools=25 | effort='medium'<br>tools=25 |
| `mock/onlymax` | effort='max'<br>tools=25 | effort='max'<br>tools=25 |
| `mock/onlylow` | effort='max'<br>tools=25 | effort='low'<br>tools=25 |
| `mock/lowhigh` | effort='max'<br>tools=25 | effort='high'<br>tools=25 |
| `mock/allof` | effort='max'<br>tools=25 | effort='medium'<br>tools=25 |
| `mock/wide` | effort='max'<br>tools=25 | effort='high'<br>tools=25 |
| `mock/maxout` | effort='max'<br>max_tokens=64000<br>tools=25 | effort=None<br>max_tokens=64000<br>tools=25 |
| `mock/imgonly` | effort='max'<br>tools=26 | effort=None<br>tools=26 |
| `mock/notools` | effort='max'<br>tools=25 | effort=None<br>tools=25 |
| `mock/toolgated` | effort='max'<br>tools=26 | effort=None<br>tools=26 |
| `mock/anthropic` | effort='max'<br>max_tokens=12345<br>tools=25 | effort='high'<br>max_tokens=12345<br>tools=25 |
| `mock/anthropic2` | effort='max'<br>max_tokens=64000<br>tools=25 | effort='medium'<br>max_tokens=64000<br>tools=25 |
| `mock/responses` | effort='max'<br>tools=25 | effort='medium'<br>tools=25 |
| `mockkimi/kmock` | effort='max'<br>max_completion_tokens=261951<br>tools=25 | effort='max'<br>max_completion_tokens=261951<br>tools=25 |
| `mockkimi/kimiout` | effort=None<br>max_completion_tokens=12345<br>tools=25 | effort=None<br>max_completion_tokens=12345<br>tools=25 |

**The rules this establishes.**

1. **Effort is selected as: global `[thinking] effort` > per-model `default_effort`**
   **(top-level or `[models.<alias>.overrides]`, both verified) >
   `support_efforts[floor(n/2)]`** when neither is declared, else nothing is sent.
   The middle-index rule reproduces on 11 distinct declared lists, e.g.
   `[low, medium, xhigh] -> medium`, `[low, high, max] -> high`,
   `[max, minimal] -> minimal`, `[max] -> max`.
2. **A global `effort` overrides every model's own default and is not clamped to
   `support_efforts`.** With the live `effort = "max"`, even a model declaring
   `[low, medium, xhigh]` is sent `reasoning_effort: "max"` — a value it does not
   claim to accept. 31 entries in the file are in that position (finding DEF-3b).
3. **The effort key is protocol-specific**, so a per-model claim cannot be checked
   without the right shape:

   | protocol | request field |
   | --- | --- |
   | `openai` | `reasoning_effort` |
   | `anthropic` | `output_config.effort` (+ `context_management`, `max_tokens`) |
   | `openai_responses` | `reasoning.effort` (+ `store:false`) |
   | `kimi` | `thinking.effort` |

4. **`max_output_size` is transmitted**, as `max_tokens` on `openai`/`anthropic`
   (and as `max_completion_tokens` on `kimi`); with the field absent the openai
   lanes send no cap at all, `anthropic` falls back to a hardcoded 64000, and
   `kimi` sends `max_context_size - 193`.
5. **`capabilities` barely reaches the wire.** Only `image_in`/`video_in` change
   the payload, and they add exactly one tool (`ReadMediaFile`) — 26 tools vs 25
   in this capture, 30 vs 29 under the fuller live config. `tool_use` presence or
   absence does not add or remove the tool array: a model declaring only
   `["thinking"]` still receives every tool. `always_thinking` and
   `dynamically_loaded_tools` produced no observable difference.
   Consequence: a lane being "chat-only" **cannot be expressed in config**; the
   client will always offer tools, and only the upstream's behaviour decides.
6. **The client never sends `tool_choice`**, and sends `tools` on every request
   regardless of the model's declared capabilities.

---

## 4. Live probe evidence

### 4.1 Effort values (one request per cell)

An `invalid-control` token (in no model's `support_efforts`) is sent once per lane.
It is the difference between "this lane accepts xhigh" and "this lane accepts
anything":

| lane | declared values accepted (200) | control behaviour | reading |
| --- | --- | --- | --- |
| `alibaba-token-plan` | max, xhigh | invalid-control returned 400 | validates the value |
| `cursor` | max | invalid-control returned 200 | ignores the field |
| `devin` | - | invalid-control timed out (TimeoutError: timed out) | unmeasurable |
| `hyper` | high, low, max, medium, minimal, none, xhigh | invalid-control returned 200 | ignores the field |
| `openai-codex` | max | invalid-control returned 400 | validates the value |
| `opencode-go` | max, none, xhigh | invalid-control returned 400 | validates the value |
| `xai-oauth` | max, xhigh | invalid-control returned 200 | ignores the field |
| `zai-coding-plan` | max | invalid-control returned 200 | ignores the field |

What this settles: on `alibaba-token-plan`, `openai-codex` and `opencode-go` the
acceptance is real (the same lane rejects a value it does not know, 400). On
`hyper`, `zai-coding-plan`, `xai-oauth` and `cursor` the field is ignored — the
acceptance is vacuous, and the xai shim's documented rewrite of unsupported
values is consistent with that. `devin` could not be measured: the lane answered
`502 {"error": {"message": "session/prompt: Reached free model rate limit.
Please switch to a different model. Your limit will reset in 1 hour 7 minutes
(at 13:01 UTC)."}}` for a direct chat instead of a completion.

The `off_effort` value was sent directly as well (pass 4, one request per lane):
both probed lanes answered 200 for `none` — `hyper`, which ignores the field, and
`opencode-go`, which rejects values it does not know (control 400). So `none` is a
value those backends understand; the config simply declares it in a field the
client never reads, which is why it cannot take effect through the client.

### 4.2 Tool calling (the census's open gap)

One request carrying a single function schema (`r18_echo`), the client's own shape.
A cell counts as positive only when a well-formed call for that function returns
(a 200 that merely *describes* the call in prose does not count). The `status=400`
cells are pass 2's forced-`tool_choice` artefact, re-run clean in pass 3; the
`status=403` cells are pass 1's User-Agent block on opencode-go, re-run in pass 2.

| lane | verdict | pass detail (source:status/served model) |
| --- | --- | --- |
| `alibaba-token-plan` | tool-capable | tool-pass2:call/deepseek-v4.1-flash; tool:status=200/deepseek-v4.1-flash |
| `cursor` | no tool call observed | tool:status=200/composer-2.5-fast |
| `devin` | unmeasurable (request timed out) | tool:status=None |
| `ds-flash-cascade` | tool-capable | tool-pass2:call/deepseek-v4.1-flash; tool:status=200/deepseek-v4.1-flash |
| `glm-flash-cascade` | tool-capable | tool-pass2:call/glm-5.3-flash; tool:status=200/glm-5-3-flash-max |
| `hyper` | tool-capable | tool-pass2:status=400; tool-pass2:call/qwen3.8-flash; tool-pass2:call/qwen3.8-max; tool-pass3:call/qwen3.8-flash; tool:status=400 |
| `openai-codex` | tool-capable | tool-pass2:call; tool:status=200 |
| `opencode-go` | tool-capable | tool-pass2:call/glm-5.3-flash; tool-pass2:status=400/qwen3.8-flash; tool-pass3:call/qwen3.8-flash; tool-pass3:call/claude-haiku-5-5; tool:status=403; tool:status=403 |
| `xai-oauth` | tool-capable | tool:call/grok-4.5 |
| `zai-coding-plan` | tool-capable | tool-pass2:call/glm-5.3-flash; tool:status=200/glm-5.3-flash |

The census recorded these claims but could not test them; measured, they hold with
one nuance worth keeping: `cursor` answers a tool request with prose ("Calling
`r18_echo` with the text `ping`") and `tool_calls: null`, which is exactly the
"CHAT-ONLY (no tool calls)" note in `[secondary_model.models]`. The
`cascade/glm-5.3-flash` entry is "chat-only" **for its devin leg only**: pass 1 was
served by devin (`glm-5-3-flash-max`, prose, no call) and pass 2 — after devin
rate-limited — fell through to the zai leg (`glm-5.3-flash`) and returned a proper
call. So the lane's tool capability depends on which leg answers, and the routing
note's warning about a degraded tool task applies only to the devin leg.

### 4.3 `image_in` claims

A real PNG, base64 data URL, in the first user message. Pass 1 used 1x1 — which
turned out to be *below* several lanes' minimum and produced the useful error
messages below; pass 2 repeated the cells with 32x32.

| alias | declares image_in | result |
| --- | --- | --- |
| `alibaba-token-plan/qwen3.8-flash` | yes | 32x32 -> 200 |
| `hyper/qwen3.8-27b` | yes | 32x32 -> 200 |
| `opencode-go/deepseek-v4-flash-vision-exp` | yes | 32x32 -> 200 |
| `opencode-go/mimo-v2.5` | yes | 32x32 -> 200 |
| `xai-oauth/grok-4.5` | yes | 32x32 -> 200 |
| `zai-coding-plan/glm-5-turbo` | NO (control) | 32x32 -> 400 |
| `zai-coding-plan/glm-5.3-flash` | yes |  |

The 1x1 rejections are themselves evidence of image processing — the lane inspected
the dimensions before refusing ("Image is too small or too large", "height:1 or
width:1 must be larger than 10", "Both width and height must be at least 8
pixels"). The **negative control is clean**: `zai-coding-plan/glm-5-turbo` does not
declare `image_in` and rejected the same payload with `messages.content.type is
invalid, allowed values: ['text']` at both sizes, so these lanes really do
discriminate on image input.

### 4.4 `reasoning_key`

For every response whose message keys were captured, the key the config declares
vs. the key the lane actually returned:

| alias | declared reasoning_key | responses carrying it | message keys seen |
| --- | --- | --- | --- |
| `alibaba-token-plan/deepseek-v4.1-flash` | `reasoning_content` | 3/3 | content,reasoning_content,role,tool_calls |
| `alibaba-token-plan/qwen3.8-flash` | `reasoning_content` | 1/1 | content,reasoning_content,role |
| `alibaba-token-plan/qwen3.8-max` | `reasoning_content` | 1/1 | content,reasoning_content,role |
| `cascade/deepseek-v4.1-flash` | `-` | 2/2 | content,reasoning_content,role,tool_calls |
| `cascade/glm-5.3-flash` | `-` | 1/2 | content,reasoning_content,role,tool_calls |
| `cursor/composer-2.5-fast` | `-` | 0/3 | content,role |
| `hyper/glm-5.2` | `-` | 1/1 | content,reasoning_content,role |
| `hyper/glm-5.3` | `-` | 1/1 | content,reasoning_content,role |
| `hyper/qwen3.7-max` | `-` | 4/6 | content,reasoning_content,role |
| `hyper/qwen3.8-27b` | `-` | 1/1 | content,reasoning_content,role |
| `hyper/qwen3.8-flash` | `-` | 2/2 | content,reasoning_content,role,tool_calls |
| `hyper/qwen3.8-max` | `-` | 1/1 | content,reasoning_content,role,tool_calls |
| `openai-codex/gpt-6.1-sol` | `-` | 0/1 | error |
| `opencode-go/claude-haiku-5-5` | `-` | 0/2 | content,id,model,role,stop_details,stop_reason,stop_sequence,type,usage |
| `opencode-go/deepseek-v4-flash-vision-exp` | `reasoning_content` | 1/1 | content,reasoning_content,role |
| `opencode-go/glm-5.3-flash` | `reasoning_content` | 0/1 | content,name,reasoning_content,role,tool_calls |
| `opencode-go/gpt-6-luna` | `-` | 0/1 | error,model |
| `opencode-go/hy3` | `-` | 0/1 | content,reasoning,refusal,role |
| `opencode-go/kimi-k3` | `reasoning_content` | 0/1 | content,reasoning,reasoning_details,refusal,role |
| `opencode-go/mimo-v2.5` | `reasoning_content` | 0/1 | content,reasoning,reasoning_details,refusal,role |
| `opencode-go/qwen3.8-flash` | `-` | 0/2 | content,id,model,role,stop_reason,type,usage |
| `opencode-go/qwen3.8-max` | `-` | 0/2 | content,id,model,role,stop_reason,type,usage |
| `xai-oauth/grok-4.5` | `-` | 2/5 | content,reasoning_content,refusal,role,tool_calls |
| `zai-coding-plan/glm-5.3-flash` | `reasoning_content` | 5/5 | content,reasoning_content,role,tool_calls |

Every lane that declares `reasoning_content` and returned reasoning returned it
under exactly that name — no mismatch was found. A `0/N` row means the sample's
reasoning went into a tool call or the lane answered without a reasoning block,
not that the name is wrong.

---

## 5. Defect classes

Every finding is in `audit-table.json` with its `triage` (defect / note /
verify-later), the affected alias, the config value, a one-line `detail` and an
`evidence` pointer. Counts by class:

| class | findings | triage |
| --- | --- | --- |
| effort fallback | 71 | note |
| unverified capability | 46 | verify-later |
| global effort overrides model | 31 | defect |
| unregistered field | 29 | defect |
| cross-provider divergence | 19 | defect |
| cap inconsistency | 14 | defect |
| capability claim | 14 | note |
| missing reasoning_key | 9 | defect |
| formula-derived cap | 6 | defect |
| base_url doc trap | 6 | note |
| missing output cap | 4 | defect |
| unentitled id | 4 | defect |
| dead lane | 3 | defect |
| duplicate alias pair | 3 | note |
| reasoning_key mismatch | 2 | defect |

The classes that need a decision:

**A. Two declared field names do not exist in this client** (19 findings, defect).
`off_effort` (10 entries) and `max_input_size` (9 entries) have zero occurrences in
the binary, and the mock capture shows `off_effort` has no effect on what is sent.
The effort value is chosen from `default_effort`/`support_efforts` only. These are
declarations that read as limits and enforce nothing.

**B. Size caps that are arithmetic, not measurement** (24 findings, defect).
`hyper/kimi-k2-thinking = 26214`, `hyper/minimax-m2.7 = 6553`,
`hyper/gpt-oss-120b = 13107` are exactly `floor(2^18/10)`, `floor(2^16/10)`,
`floor(2^17/10)`, and `hyper/gemma-4-26b-a4b-it = 25600` is exactly
`max_context_size/10`. Since `max_output_size` is transmitted as `max_tokens`, a
unit slip here truncates real output. The same class covers 7 entries whose output
cap equals or exceeds their context size, 6 where input + output exceeds context,
and 1 where `max_input_size == max_context_size`.

**C. The global thinking effort silently overrides 31 model declarations** (DEF-3b).
See section 3, rule 2. `[thinking] effort = "max"` is sent to models that declare
no support for it. Whether that breaks anything is lane-dependent and measured in
4.1 — the lanes that validate values (token-plan, codex, opencode-go) did accept
`max`, so this is a correctness-of-intent issue rather than a live outage; but the
file's per-model `support_efforts` are currently decorative.

**D. Dead lanes and unentitled ids** (7 findings, defect). From the census and still
true against this digest: `managed:kimi-code` answers 401 on every path (empty
OAuth store), keys 2 and 3 of the token-plan are quota-exhausted (429),
`glm-5` is unentitled on all three token-plan lanes (403) and
`zai-coding-plan/glm-5.3-highspeed` is not in its plan (429). That is
**42 of 143 entries routing to lanes that cannot serve them**.

**E. Cross-provider divergence for the same served id** (19 findings, defect).
`glm-5.3-flash` is declared with `max_output_size` 131072 on zai/opencode-go but
128000 on hyper; `deepseek-v4.1-flash` with 262144 on hyper but 384000 on
token-plan and opencode-go; `kimi-k2.6` with `max_output_size` equal to its whole
context on all three token-plan lanes. One of each pair is wrong; none was
measured, so these go to verify-later with the conservative default (smallest
declared value).

**F. Capability claims the client cannot enforce** (14 notes, 46 verify-later).
`tool_use` absence does not stop the client sending tools (section 3, rule 5), so
the "chat-only" marking in the routing table is documentation rather than a
setting. `video_in`/`audio_in` are unprobed claims.

**G. `reasoning_key` does not match what the lane returns** (11 findings, defect;
probe-derived, so they live in `audit-table.json` as DEF-9/DEF-10). Two entries
declare `reasoning_content` while the lane returns `reasoning` +
`reasoning_details` and never the declared key — `opencode-go/kimi-k3` and
`opencode-go/mimo-v2.5`. Nine entries declare no key at all while the lane
returned `reasoning_content`: the eight probed `hyper` models, plus
`xai-oauth/grok-4.5` and the two cascade entries. A reasoning pane cannot render
either way until the declaration matches the lane. The `reasoning` field the
opencode-go models return is a plain string holding the same text as
`reasoning_details[0].text`, so `reasoning` is the recommended replacement;
which key the client actually reads is not settled here and is listed in
verify-later.

---

## 6. Config corrections

`config-corrections.toml` holds 56 splice-ready model blocks with an `# evidence:`
line each, plus the quarantine list for the dead lanes and a verify-later list.
The file is parsed by TOML at generation time (`scripts/build_corrections.py`), so
it is valid TOML by construction, and it contains no credential values.

Three things it deliberately does **not** do:

- It does not invent replacement numbers for the bad caps. Every such correction is
  a removal, because the client then sends no cap and the server decides —
  strictly safer than an arithmetic guess, and reversible.
- It does not touch the live config. Corrections are staged for the operator.
- It does not rewrite entries whose only finding is a note.

---

## 7. Secrets hygiene

Command and result (`HYGIENE.md` carries the full log):

````
$ bash scripts/hygiene_check.sh
# Secrets hygiene -- R18 definitions audit

Gate: `bash scripts/hygiene_check.sh` scans every file in this tree, raw
captures included, for (1) the exact credential values in the live config and
(2) generic credential shapes.

Credential values are read from the config inside the scan process and are
never printed, passed as arguments, or written to disk; only counts leave it.

```
scan root:        /home/vgpnk/Projects/shokunin/.tower/worktrees/wt-2/research/round-18-kimi-model-routing/definitions
files scanned:    24
distinct configured credential values tested: 12

exact  provider alibaba-token-plan api_key          hits=0 
exact  provider alibaba-token-plan-2 api_key        hits=0 
exact  provider alibaba-token-plan-3 api_key        hits=0 
exact  provider zai-coding-plan api_key             hits=0 
exact  provider hyper api_key                       hits=0 
exact  provider opencode-go api_key                 hits=0 
exact  provider opencode-go header x-opencode-session hits=0 
exact  provider openai-codex api_key                hits=0 
exact  provider devin api_key                       hits=0 
exact  provider xai-oauth api_key                   hits=0 
exact  provider cursor api_key                      hits=0 
exact  provider ds-flash-cascade api_key            hits=0 
exact  provider glm-flash-cascade api_key           hits=0 

shape  credential prefix                            hits=0 
shape  bearer token                                 hits=0 
shape  assigned secret                              hits=0 

TOTAL HITS: 0
RESULT: PASS -- no credential value or credential-shaped string in any artifact
```

Exit status: 0 (0 = clean). Probe captures record credential header
names with a `<redacted:len=N>` marker instead of values
(see scripts/common.py `redact_headers`).
````

The scan tests every configured credential value — every provider `api_key` and
the opencode session header — against every file in this tree, and separately for
credential-shaped strings. Probe captures store header names with a
`<redacted:len=N>` marker, never values (`scripts/common.py`), and the live config
is never modified.

---

## 8. What this audit does not cover

- **`max_context_size`.** The client never transmits a context limit, so no cheap
  probe can falsify these declarations; only a deliberately over-long prompt per
  lane would, and that is a quota-heavy test.
- **`video_in` / `audio_in`.** Declared on 41 entries, probed on none.
- **Devin.** Rate-limited during the audit window; its direct chat path and its
  leg-1 behaviour should be re-checked after the reset.
- **The `[secondary_model.models]` routing table** is only audited where it points
  at models with defects found here; routing policy itself is M4's scope.

---

## 9. Reproducing this

```
python3 scripts/audit_definitions.py        # -> audit-table.json, audit-table.md
python3 scripts/probe_client_semantics.py  # -> raw/client-semantics.json (no quota)
python3 scripts/probe_live.py all          # -> raw/probes-{effort,tool,image}.json
python3 scripts/probe_live.py pass2        # -> raw/probes-*-pass2.json (UA + budget fixes)
python3 scripts/probe_live.py pass3        # -> raw/probes-tool-pass3.json (client shape)
python3 scripts/probe_live.py pass4        # -> raw/probes-effort-pass4.json (off_effort value)
python3 scripts/merge_probe_findings.py    # folds DEF-9/DEF-10 into audit-table.json
python3 scripts/build_corrections.py       # -> config-corrections.toml
bash    scripts/hygiene_check.sh           # -> HYGIENE.md, exit 0 expected
python3 scripts/build_analysis.py          # -> ANALYSIS.md (embeds HYGIENE.md)
```

Order matters in two places: `merge_probe_findings.py` must run after
`audit_definitions.py` (which rewrites `audit-table.json` and drops the
probe-derived DEF-9/DEF-10 rows) and before `build_corrections.py`; and
`hygiene_check.sh` must run before `build_analysis.py`, because ANALYSIS.md
embeds the hygiene log verbatim.
Re-running the four generators after a probe run reproduces the committed
`audit-table.*`, `config-corrections.toml` and `ANALYSIS.md` byte for byte; only
the probe scripts themselves spend quota, so they are the only steps that need
re-running to refresh evidence.

Each probe script prints the config's json-canonical digest before probing, so a
config edit between runs is visible rather than silent.
