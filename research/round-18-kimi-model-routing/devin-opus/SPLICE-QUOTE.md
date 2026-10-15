# SPLICE-QUOTE — `devin/opus-5.5-high` (M10, round 18)

Splice-ready blocks for the operator to apply to `~/.kimi-code/config.toml` and to
`research/round-18-kimi-model-routing/routing/kimi-secondary-models-round18.toml`.
**This mission wrote neither file.** Evidence for every claim below is in
`devin-opus/ANALYSIS.md`; the raw captures are under `devin-opus/raw/`.

## Pin (verified at M10 run start, 2026-10-15)

| | |
| --- | --- |
| live config | `/home/vgpnk/.kimi-code/config.toml` |
| file sha256 | `c5f12997f7cee456eacddbaf03c95e598ca5911cb18d6e6cf7821909b6fc9ebf` |
| `[secondary_model.models]` region | lines **1483–1504** (17 entries) |
| `[models."devin/…"]` region | lines **1307–1368** (9 entries, last is `glm-5-3-flash-max`) |
| opus entries in live config | **0** (`grep -ci opus` → 0) |
| M4 routing-table file | `routing/kimi-secondary-models-round18.toml`, STRONG section |
| M10 evidence | `devin-opus/ANALYSIS.md`, `devin-opus/raw/**` |

## Apply order (this matters — the splice tool guards the live file hash)

1. Splice the routing table **first**, while the live file sha still equals M4's
   pin: add Block B to `routing/kimi-secondary-models-round18.toml` (above its
   `# SPLICE-END` sentinel), then run `routing/splice_secondary.py --apply`
   (M4's `APPLY.md` Steps 0–2). Doing it first is what lets the guard pass
   unmodified.
2. Add Block A (`[models.*]`) **after** that, in the same session, back to back —
   between the two steps the pool briefly references a model with no `[models]`
   entry, which the client cannot resolve. Any earlier edit changes the live file
   sha and forces `--no-hash-guard`, which M4's `APPLY.md` reserves for scratch
   configs. Block A is the same shape as the M2 corrections step (`APPLY.md`
   Step 3), which runs after the splice for the same reason.
3. Verify: `python3 -c "import tomllib;c=tomllib.load(open('/home/vgpnk/.kimi-code/config.toml','rb'));print(c['secondary_model']['models']['devin/opus-5.5-high']);print(c['models']['devin/opus-5.5-high'])"`
   then one chat probe through the CLI (or `curl` the shim as in
   `devin-opus/scripts/run_all.sh`) — the entry must answer with
   `model: claude-opus-5-5-high`.

**Quote verification (done, read-only).** `python3 scripts/verify_splice_payload.py`
parses Block A, inserts Block B into M4's payload above its sentinel, and re-parses
the result: pool 13 → 14 entries, pool id consistent across both blocks. Output:
`raw/splice-verify.json`. The same pool id → served id resolution was exercised
end-to-end by the measurement itself — `scripts/candidate-config.toml` carries
exactly this `[models]` entry and the battery ran through it
(`raw/telemetry.csv`, `raw/run-manifest.json`).

---

## Block A — `[models]` entry (live `~/.kimi-code/config.toml`)

Insert with the other `devin/*` entries, after `[models."devin/glm-5-3-flash-max"]`
(live line ~1368, before `[models."xai-oauth/grok-4.7"]` at ~1370):

```toml
[models."devin/opus-5.5-high"]
provider = "devin"
model = "claude-opus-5-5-high"
max_context_size = 1048576
capabilities = [ "thinking", "tool_use" ]
display_name = "Devin Claude Opus 5.5 High"
reasoning_key = "reasoning_content"
```

Field-by-field justification (all measured, M10 rounding):

| field | value | why |
| --- | --- | --- |
| `provider` | `devin` | the shim at `http://127.0.0.1:8787/v1` is the only path that serves this id |
| `model` | `claude-opus-5-5-high` | the **exact** served id; `claude-opus-5.5`, `claude-opus-5-5` and `opus-5.5-high` all returned 403 `permission_denied` (`raw/id-*.json`) |
| `max_context_size` | `1048576` | the backend's own catalog line: "claude-opus-5-5-high … [1M context, $4 / 1M Input … $20 / 1M Output]" (`raw/devin-models-opus.txt:30`); declared only — never transmitted (M2 s8) |
| `capabilities` | `thinking`, `tool_use` | `reasoning_content` observed on 5 probes, well-formed `tool_calls` on 3 (M10 s5). **Not** `image_in` — never probed. **Not** `always_thinking` — c1 streamed no reasoning at all |
| `reasoning_key` | `reasoning_content` | the shim emits `reasoning_content` deltas; without this the client drops them (the M2 DEF-10 class) |
| `max_output_size` | *(omitted)* | not measured for this lane; M2's correction policy removes guessed caps rather than inventing them — with the field absent the openai path sends no cap and the server decides (M2 s3 rule 4) |
| `support_efforts` / `default_effort` | *(omitted)* | would be inert: the shim has no `reasoning_effort` plumbing, and an invalid effort value returned 200 (`raw/effort-summary.json`). Effort on this lane is the **id suffix**, exactly as in the existing `devin/swe-2-high` / `devin/glm-5-3-flash-high` pins |

Optional variant, only if the operator wants the client-side label: adding
`support_efforts = [ "low", "medium", "high", "xhigh", "max" ]` documents the
family's real ids (each is a separate served id per `raw/devin-models-opus.txt`)
but changes nothing on the wire. The six ids, for reference:
`claude-opus-5-5-low|medium|high|xhigh|max` and the `-fast` twins at 2× price.

---

## Block B — STRONG pool line

Into `routing/kimi-secondary-models-round18.toml`, in the `[secondary_model.models]`
payload under `# --- STRONG ---`, directly after the two `openai-codex` lines and
before the `# --- VERIFY-FIRST adds …` comment:

```toml
"devin/opus-5.5-high" = "STRONG rank 3 (devin lane), HIGH effort pinned by served id suffix: measured TTFT 3079 ms, TPS 161.74 tok/s, 9/9 probes [M10 s3] -- throughput well above both codex STRONG lanes (2.3x), TTFT between the STRONG median 2545 ms and the MIDDLE median 4172 ms. 1M declared context. Tool-capable: well-formed get_weather call under tool_choice auto and required [M10 s5], so unlike the deepseek leg M2 measured, tool subtasks survive on this lane. Effort is the id itself: only claude-opus-5-5-high resolves (dot-form and bare id return 403) and the shim drops reasoning_effort entirely, so support_efforts on the entry would be inert [M10 s5]. Bills 4 prompt tokens per text call -- M1 D9's ~12k overhead did NOT reproduce for this model [M10 s4]. Cold start: first call answered in 1339 ms, but another client had used the shim 2.3 min earlier, so M1 D7's 180-300 s block is neither reproduced nor excluded -- expect a possible one-off stall on a genuinely idle lane [M10 s4]. Lane constraint: temperature 0 is rejected with 400 invalid_argument (the CLI never sends a temperature field, so live traffic is unaffected) [M10 s4]."
```

Companion ledger line for the file's EVIDENCE LEDGER block:

```toml
# devin/opus-5.5-high             | STRONG       | add        | 3079 ms / 161.74 / 9-9 | ctx 1048576, no out cap | pinned high (id suffix; effort field inert) | M10 s3+s4+s5; cold start unreproduced but unexcluded (first call 1339 ms, lane not provably idle); discovery raw/devin-models-opus.txt
```

And for the BUCKET SEMANTICS / STRONG cross-provider order section, the STRONG
ladder becomes 3 measured lanes plus 1 verify-first:

```
# STRONG (quality-first):
#   1 openai-codex/gpt-6.1-sol              2212 ms / 64.46 (9-9)
#   2 openai-codex/gpt-6.1-sol-high         2878 ms / 70.82 (9-9)
#   3 devin/opus-5.5-high                   3079 ms / 161.74 (9-9)  <- new (M10)
#   4 xai-oauth/grok-4.7                    verify-first (census 1166 ms / 493.74)
#   Operator note: #1 and #2 share one shim and one upstream model id, so #3 is
#   the first STRONG lane on a genuinely different provider chain.
```

---

## What this entry does NOT claim

- No `image_in`: unmeasured on this lane.
- No tool-verdict extension beyond the single-schema probe: the live client sends
  25–30 schemas (M2 s3 rules 5–6); 25 tools were offered in one probe and the call
  came back well-formed, but the client's own schemas were not replicated.
- No cold-start verdict: M1 D7's 180–300 s cold start neither reproduced nor was
  ruled out — another client hit the shim 2 minutes before M10's first call
  (`raw/run.log`, shim journal), so the lane was not provably idle.
- No claim that the prompt-token accounting is understood: measured 4 on every
  text call and 4–395 on tool-carrying calls with no dependence on tool-array size
  (M10 s4). The lower figure is what matters for cost.