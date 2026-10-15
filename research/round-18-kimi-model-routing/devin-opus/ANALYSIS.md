# M10 — devin STRONG entry: `claude-opus-5-5-high`

Mission M10 (`r18-devin-opus`, branch `feat/r18-devin-opus-strong-entry`), round 18.
**Outcome: positive — the backend serves Claude Opus 5.5, the entry is registered
as a splice quote, and the route to it is measured.** Deliverable blocks are in
`SPLICE-QUOTE.md`; this document is the evidence behind them. The live config was
never written by this mission.

| | |
| --- | --- |
| Live config | `~/.kimi-code/config.toml`, sha256 `c5f12997f7cee456eacddbaf03c95e598ca5911cb18d6e6cf7821909b6fc9ebf` (= M4's pin, unchanged) |
| Opus entries in it | **0** (`grep -ci opus` → 0; `raw/run.log`) |
| Candidate entry | pool alias `devin/opus-5.5-high` → served id `claude-opus-5-5-high` |
| Measurement window (UTC) | 2026-10-15T14:30:50Z → 2026-10-15T14:37:00Z |
| Requests spent | **36** chat requests to the shim (journal-verified below) + 1 `GET /v1/models` |
| Score | **9/9 correctness probes**, TTFT 3079 ms med, TPS 161.74 med |

---

## 1. Discovery — the premise held, but not where the mission expected it

The mission's discovery task was written against `GET /v1/models` on the shim.
That endpoint is **not authoritative**: `devin-shim/shim.py:47` carries a *static*
`MODELS` list ("verified via `devin models list`") of exactly 9 ids, and the shim's
`map_model()` only aliases `swe-2` → `swe-2-high` before passing the id straight
through as the upstream `chatModelUid` (`shim.py:362`, `shim.py:272`). A listing
that stale can neither confirm nor deny a served model, and this one denies one
that exists.

The authority is the CLI's own catalog:

| source | says | evidence |
| --- | --- | --- |
| `devin models list` (operator's account) | **54 families**; "Claude Opus 5.5 (claude-opus-5.5)" with ids `claude-opus-5-5-low\|medium\|high\|xhigh\|max` plus five `-fast` twins; the `-high` id is `[1M context, $4 / 1M Input · $0.2 / 1M cached · $20 / 1M Output]` | `raw/devin-models-list.txt` (line 30), `raw/devin-models-opus.txt` |
| shim `GET /v1/models` | 9 ids: swe-2 family, deepseek-v4-1-flash-high/max, glm-5-3-flash-low/high/max — **no opus** | `raw/models-shim-live.json` |
| live config | 9 `[models."devin/*"]` blocks, **0** opus matches | `raw/run.log` |
| live probe of the candidate id | **200** — `claude-opus-5-5-high` answers through the shim | `raw/smoke-cold.json` |

The family count is **54**, from the catalog's own header line
(`Available models (54 families)`) and from a strict family-header match,
`grep -cE '^[A-Za-z].*\([a-z0-9.-]+\)$' raw/devin-models-list.txt` → 54. A loose
"name then parentheses anywhere on the line" pattern reports 56 because it also
matches two lines that are not families: the header itself (line 1) and the closing
usage note `Pass a family slug, alias, or model UID to --model (e.g. --model opus)`
(line 959). `raw/run.log`'s `families: 56` line is that loose pattern's output from
the M10 runner — an artefact of the count, not the count; the pattern is corrected
in `scripts/run_all.sh` for future runs and the capture is left as it was taken.

Mission's decision point — "if no opus-5.5 exists on the backend, STOP" — therefore
resolves the other way: it exists, and the id spelling is **`claude-opus-5-5-high`**.
The family label's dot form is not servable:

| spelling probed | status | body code |
| --- | --- | --- |
| `claude-opus-5-5-high` | 200 | — |
| `claude-opus-5.5` (family label) | 403 | `permission_denied` |
| `claude-opus-5-5` (bare, no effort suffix) | 403 | `permission_denied` |
| `opus-5.5-high` | 403 | `permission_denied` |

Evidence: `raw/id-*.json`, `raw/id-spelling-summary.json`. The 403 is the same
"permission_denied server-side" behaviour the shim's own comment records for the
bare `swe-2` uid — i.e. an id the backend will not serve is refused, not silently
substituted. So the "don't invent an id" guard is backed by the backend itself.

## 2. Method (M3 conventions, one documented deviation)

Everything is the M3 battery's own code path — same prompts, same warm-up
pre-call for devin-class lanes, same n=2 sequential reps, same 400 s devin-class
timeout, same grader, same one-attempt rule — run through
`scripts/run_battery_lane.py`, which exists for exactly one reason:

**Deviation: the `temperature` field is dropped from every probe body.**
The M3 openai body sends `temperature: 0`; this lane answers that body with HTTP
400 `invalid_argument`. Field isolation (`raw/shape-summary.json`):

| body | status |
| --- | --- |
| bare (no temperature, no stream_options) | 200 |
| `temperature: 0` | **400** |
| `temperature: 1.0` | 200 |
| `stream_options: {include_usage: true}` | 200 |
| `temperature: 0` + `stream_options` | **400** |

Two consequences, both material:

1. **It does not bind live traffic.** The kimi client transmits no temperature
   field at all — M2's mock capture records `effort` / `max_tokens` / `tools` and
   no temperature key (M2 s3; the string "temperature" does not appear anywhere in
   `definitions/raw/client-semantics.json`).
2. **It does bind any other tool** that talks to this shim with the OpenAI house
   style of `temperature: 0` — the shim passes it upstream and the model refuses.
   Recorded as a lane property in `SPLICE-QUOTE.md`, not as a probe artefact.

The adapter's deviation is recorded inside `raw/run-manifest.json` under `adapter`
so the capture set is self-describing. The first battery attempt (without the
adapter) is preserved in `raw/run.log`: **2 × `format_break`** (the warm-up and
perf-r1 — the only two requests actually sent, both HTTP 400) followed by
**10 × `skipped_after_fatal`** for the probes the one-attempt rule then withheld.
The failure is evidence, not a discarded run; the shim journal confirms exactly two
POSTs for that attempt (11:31:11).

## 3. Measurement

### 3.1 TTFT / TPS (n=2, identical prompt, max_tokens 256, stream)

| probe | elapsed ms | TTFT content ms | decode span ms | TPS | completion tokens | prompt tokens |
| --- | --- | --- | --- | --- | --- | --- |
| warm-up (excluded from metrics) | 2836 | 2797 | — | — | 4 | 4 |
| perf-r1 | 4071 | 2128 | 1878 | 159.77 | 301 | 4 |
| perf-r2 | 5898 | 4030 | 1833 | 163.70 | 301 | 4 |
| **median** | — | **3079** | — | **161.74** | — | — |

The stream is genuinely incremental (decode span ≈ 1.9 s over 300 tokens, well
over M3's 50 ms burst threshold), so TPS is a real throughput number and not the
burst artefact that took the two cascade lanes out of M3's TPS ranking.

Where that lands against M3's measured pool (`battery/ANALYSIS.md` s2–s4):

- TTFT **3079 ms** sits between the STRONG median (2545 ms) and the MIDDLE median
  (4172 ms): slower than both measured codex lanes (2212 / 2878 ms), faster than
  every MIDDLE lane except glm-5-turbo and grok-4.5.
- TPS **161.74** is ~2.3× the codex lanes (64.46 / 70.82) and above every
  non-deepseek lane M3 measured. For a strong-tier lane it is fast.

### 3.2 Correctness — 9/9

| probe | pass | notes |
| --- | --- | --- |
| c1 PONG exact | ✅ | no reasoning streamed |
| c2 JSON exact | ✅ | |
| c3 three lines exact | ✅ | |
| c4 "strawberry" count | ✅ | streamed 100 chars of reasoning before `3` |
| c5 sentence without "e" | ✅ | slowest probe at 13.4 s (hard constraint, reasoning 13.3 s) |
| k1 `rev` function | ✅ | |
| k2 `len(set(...))` | ✅ | |
| k3 `sorted({...})` | ✅ | |
| t1 tool call | ✅ | see s5 |

`raw/telemetry.csv`, `raw/responses/devin-opus-5.5-high/*.json`.

## 4. Devin-class overheads, for **this** model

**Cold start (M1 D7): not reproduced, and not provably testable here.** M10's
first call answered in **1339 ms** (`raw/smoke-cold.json`). But the shim's journal
shows another client's chat calls at 11:28:18–11:28:55 local, ~2.3 minutes before
that first call, so the lane was not idle and the 180–300 s block M1 D7 recorded
is neither confirmed nor denied for this model. Stated as an open item, not as a
contradiction of D7.

**Prompt-token billing (M1 D9): the ~12k overhead does not apply to this model.**
M1 D9 measured 12 163 prompt tokens for the identical short prompt and attributed
that to the devin leg as such. Here:

| call shape | calls | prompt tokens billed |
| --- | --- | --- |
| no tools sent (smoke, battery warm-up/perf/c1-c5/k1-k3, id, shape and effort probes, `tool-none`) | 20 | **4** every time |
| 1 tool schema, `get_weather`, weather prompt | 3 | 395, 395, 395 |
| 1 tool schema, "say hello" prompt | 1 | 381 |
| 25 small tool schemas | 2 | 4, 4 |

Every accepted call in the run is accounted for: 20 + 3 + 1 + 2 = 26 HTTP 200s
(plus 2 × 400 and 3 × 403, which carry no usage).

So the tax belongs to the model M1 measured (`deepseek-v4-1-flash-high`), not to
the lane, and on opus a text call bills 4 tokens. The 381–395 cells are a genuine
open question: a **per-tool cost model is disproved** by the 25-schema cells (the
model enumerated all 25 tool names in its answer — it had them — and billed 4 both
times). `raw/billing-summary.json`, `raw/toolcost-summary.json`, `raw/billing-*.json`.
The mechanism is left unnamed rather than guessed; the number that matters for cost
is that live text traffic bills 4, and the live client's own tool-carrying calls
were not replicated.

**Price.** The backend catalog prices this id at $4 / 1M input and $20 / 1M output
(1M context), versus the swe-2 family's "Free" line — this is a *billed* devin
lane, unlike the swe-2 pins already in the config. `raw/devin-models-opus.txt:30`.

## 5. Tool, effort, and reasoning verdicts

**Tools: capable.** `tool_choice` `auto` and `required` both returned a
well-formed call — `get_weather`, arguments `{"city": "Paris"}`, `finish_reason:
tool_calls` — on three calls (battery t1 plus `raw/tool-required.json`,
`raw/tool-auto.json`), and a fourth well-formed call came back from a 25-schema
probe (`m10_tool_07`, `raw/billing-call-25tools.json`); the no-tools control
returned text. M2's "the devin leg is
chat-only" finding does **not** carry to this entry: that verdict came from an
earlier window on a different model (`glm-5-3-flash-max` prose on the cascade
lane; direct devin probe unmeasurable). The role string therefore claims tool
capability, on the same evidence standard M2 used (a well-formed call, not prose).

**Effort: the lane ignores the field, and the id is the effort.** An invalid value
(`m10-invalid-effort-value`, in no model's `support_efforts`) returned **200**;
`high` and `low` also returned 200 (`raw/effort-summary.json`). That is M2's
"ignores" verdict, and source inspection explains it: `devin-shim/shim.py`
contains no `reasoning_effort` handling at all, so no effort value can reach the
backend through this shim. The family expresses effort through the served id
suffix (`-low|medium|high|xhigh|max`, each a separate id per the catalog), which
is why the entry pins HIGH as `claude-opus-5-5-high` and omits
`support_efforts`/`default_effort` rather than declaring a label with no wire
effect.

**Reasoning: `reasoning_content` is emitted** on c4, c5, k1, k2, k3 (88–371 chars)
and absent on c1–c3 and the perf reps. Content and reasoning are cleanly separated
by the shim. The entry declares `reasoning_key = "reasoning_content"`, the same
correction M2's DEF-10 applies to the xai/hyper lanes. No `reasoning_tokens`
breakdown is returned, so reasoning cost is invisible in `usage`.

**Capabilities claimed:** `thinking`, `tool_use` only. `image_in` was **not**
probed, and M2 s3 rule 5 shows declaring it would change the payload (it adds
`ReadMediaFile` to the client's tool array) — an unmeasured claim with a live
effect, so it is not made.

## 6. Registration

See `SPLICE-QUOTE.md`: the `[models."devin/opus-5.5-high"]` block, the STRONG pool
line for `routing/kimi-secondary-models-round18.toml`, the ledger/comparison lines,
the apply order (routing table first, while the live file sha still equals M4's
pin), and the list of things the entry explicitly does not claim.

## 7. Limits

- n=2 for TTFT/TPS; correctness is one draw per probe (M3 s9). Signals, not scores.
- **36 chat requests**, one lane, one window, no retry loops. Accounting, from the
  shim journal (`journalctl --user -u devin-shim`, local 11:30:40–11:35:30): my 36
  requests are 27 × 200, 6 × 400 and 3 × 403 (the id-spelling probes). The 400s are
  the two temperature-0 attempts — 2 from the first battery attempt, 2 from the
  shape isolation (`shape-temp0`, `shape-temp0-streamopts`) and 2 from the first
  tool attempt (`tool-required`, `tool-auto`; that attempt's `tool-none` control
  returned 200 and is counted with the 200s). Two further 200s at
  11:37:01/11:37:04 belong to another client of the same shim, which is why the
  journal's 38-POST total is two more than mine; no foreign call falls inside the
  measurement window (11:32:50–11:33:45 local), so the timings are uncontended.
- The live client's 25–30-schema tool array was not replicated; the tool verdict
  rests on a single-schema probe plus one 25-schema probe whose *call* was correct.
- Cold-start behaviour on a genuinely idle lane is untested: another client had
  used the shim 2.3 minutes before M10's first call.
- The prompt-token mechanism on tool-carrying calls is unexplained (s4); the
  no-tools figure (4 tokens) is the one that holds across all 20 such calls.
- No image probe; no long-context probe; `max_context_size` is the backend's
  declared value, never transmitted.

## 8. Reproduce

```bash
cd research/round-18-kimi-model-routing/devin-opus
bash scripts/run_all.sh            # every stage, in order
bash scripts/run_all.sh shape      # or one stage: discovery|smoke|battery|ids|shape|
                                   #   effort|tool|toolcost|billing
python3 scripts/verify_splice_payload.py   # parses the quote, read-only
bash scripts/hygiene_check.sh              # secrets gate, see HYGIENE.md
```

Artifacts: `raw/run.log` (stage log), `raw/telemetry.csv` + `raw/run-manifest.json`
(battery), `raw/responses/devin-opus-5.5-high/*.json` (11 per-probe captures),
`raw/models-shim-live.json`, `raw/devin-models-list.txt` (discovery),
`raw/{id,shape,effort,tool,toolcost,billing}-*.json` (entry probes).