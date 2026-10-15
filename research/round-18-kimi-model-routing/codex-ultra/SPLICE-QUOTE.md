# SPLICE-QUOTE — codex STRONG variant on the top reasoning tier (R18 M8)

Splice-ready blocks for the operator's two files, per the mission
(`r18-codex-ultra`). Nothing here has been applied — the live config was only
read, never written.

**The one-line answer:** the operator's word was "ultra". The wire does not
accept `ultra`; it accepts `none, minimal, low, medium, high, xhigh, max` and
**`max` is the accepted top tier**. So the variant pins **`max`** and is named
for the value it actually sends. `ultra` is declared by the codex model catalog
and the CLI binary but rejected by the backend validator — evidence in
`ANALYSIS.md` s3–s4 and `raw/discovery-evidence.json` / `raw/ultra-probe.json`.

```
POST http://127.0.0.1:8789/backend-api/codex/responses
{"reasoning": {"effort": "ultra"}}                       -> 400

{
  "error": {
    "message": "Invalid value: 'ultra'. Supported values are: 'none', 'minimal', 'low', 'medium', 'high', 'xhigh', and 'max'.",
    "type": "invalid_request_error",
    "param": "reasoning.effort",
    "code": "invalid_value"
  }
}
```

`high`, `xhigh` and `max` with the identical shape → `200`, and every accepted
request echoes its effort back in `response.created`
(`{"effort": "max", "context": "all_turns", "summary": null, "mode": "standard"}`).
Measured at n=2 on the M3 battery prompt (`max_output_tokens` 256): the `max`
pin lands at **2927 ms / 74.98 tok/s** next to the M3 high-pin row's
**2878 ms / 70.82** (+49 ms / +5.9% TPS) — same shim, same upstream model id,
and the field demonstrably tiers backend behaviour (reasoning tokens billed:
0 at `high`, 25–26 at `xhigh`, 37–43 at `max`).

One caveat on that comparison: the M3 high-pin row was measured **without a
reasoning field on the wire** (the M3 probe path never sends one — the backend
default, echoed as `medium` in this run's no-effort control, ANALYSIS s5), so
read +49 ms / +5.9% as `max` vs the lane's no-field default, not as a
same-conditions high-vs-max delta. The same-window M8 rows are the tighter
comparison and favour `max` more strongly still (`high` 64.64 → `max` 74.98
TPS), so the recommendation is unaffected.

---

## Block A — new `[models]` entry for `~/.kimi-code/config.toml`

Insert immediately after the existing
`[models."openai-codex/gpt-6.1-sol-high".overrides]` table (its
`default_effort = "high"` line, live lines 1296–1297 at pin time), before
`[models."openai-codex/gpt-6-luna"]`. Alias `openai-codex/gpt-6.1-sol-max`
keeps the pool's `openai-codex/gpt-6.1-sol-<effort>` naming convention; the
full metadata block copies every field from its siblings (docs prerequisite:
a variant is a standalone entry and inherits nothing).

```toml
[models."openai-codex/gpt-6.1-sol-max"]
provider = "openai-codex"
model = "gpt-6.1-sol"
max_context_size = 500000
capabilities = [ "image_in", "thinking", "tool_use" ]
display_name = "GPT-6.1 Sol Max (Codex)"
support_efforts = [ "low", "medium", "high", "xhigh", "max" ]

[models."openai-codex/gpt-6.1-sol-max".overrides]
default_effort = "max"
```

Notes on the fields:

- `support_efforts` keeps the sibling list. Every value is on the wire's
  accepted list; `ultra` is deliberately absent (rejected by the validator).
  The wire additionally accepts `none`/`minimal`, which the model's catalog
  entry does not declare — not added, to stay identical to the siblings.
- `default_effort = "max"` must be a member of `support_efforts` (docs), and
  the `overrides` table is the documented pin point that survives refreshes.
- The alias is a *second entry on the same upstream model*, not an independent
  lane — the same honest scope note as ranks 1–2 (M3 SELECTION s3).

## Block B — replacement STRONG section for `routing/kimi-secondary-models-round18.toml`

Replace the current three-line `# --- STRONG ---` block (lines 81–83) with this
block. Ranks 1–2 are unchanged; the variant is rank 3.

```toml
# --- STRONG ---
"openai-codex/gpt-6.1-sol" = "STRONG rank 1 (codex lane): 2212 ms, TPS 64.46, 9/9 -- the fastest measured bucket member in the pool, measured not assumed [M3 s4]. Needs the M1 D6 request shape (store false, stream true, list input, no temperature, max_output_tokens >= 16) [M1 D6]; no effort pin on the entry, client picks high (M2 DEF-3d)."
"openai-codex/gpt-6.1-sol-high" = "STRONG rank 2, pinned to HIGH effort: 2878 ms, TPS 70.82, 9/9 [M3 s2]. Same shim, same upstream model id as rank 1 -- a second effort pin, not an independent provider fallback [M3 SELECTION s3]."
"openai-codex/gpt-6.1-sol-max" = "STRONG rank 3, pinned to MAX effort -- the top tier the backend accepts; the catalog/CLI-declared ultra is rejected on the wire (400 invalid_value, param reasoning.effort) [M8 s4]. Measured n=2 on the M3 prompt at 256 tokens: 2927 ms, TPS 74.98, every rep a correct prefix of 1..150 [M8 s5]; reasoning tokens billed 37-43 (0 at high). Same shim, same upstream model id as ranks 1-2 -- a third effort pin, not an independent provider fallback [M3 SELECTION s3]. Correctness not re-run by M8; with the live global [thinking] effort=max the wire value today coincides, so treat the pin as intent + immunity to global changes [M8 s7]."
```

**Note on the rank-2 ↔ rank-3 comparison.** The rank-2 line is kept verbatim
from M3, and M3's probe path measures **without a reasoning field on the wire**
— the backend's default behaviour, which this run's no-effort control echoes as
`medium` (ANALYSIS s5). The rank-3 numbers (2927 ms / 74.98) are measured at an
explicit `reasoning.effort: "max"`. Same-window M8 rows at the identical shape:
`high` 1786 ms / 64.64, `xhigh` 2574 ms / 67.81, `max` 2927 ms / 74.98 — `max`
posts the best TPS and a higher TTFT median at n=2 [M8 s5]; the n=2 spread is
wide (max TTFT reps 2480 / 3374), so treat this as a signal, not a benchmark.

### Optional ancillary updates (same file, keep in sync)

These two optional blocks also quote the M3 rank-2 row (2878 ms / 70.82); the
same no-reasoning-field caveat applies (ANALYSIS s5).

EVIDENCE LEDGER (append one row after the `openai-codex/gpt-6.1-sol-high` line,
currently line 117):

```
# openai-codex/gpt-6.1-sol-max      | STRONG       | add (verify-first after apply) | 2927 ms / 74.98 / prefix-ok both reps | ctx 500000, no out cap | pinned max (top wire-accepted tier) | M8 s4+s5; ultra declared by catalog but rejected on the wire
```

STRONG ladder comment (cross-provider fallback order, currently lines 191–194):

```
# STRONG (quality-first):
#   1 openai-codex/gpt-6.1-sol              2212 ms / 64.46 (9-9)
#   2 openai-codex/gpt-6.1-sol-high         2878 ms / 70.82 (9-9)
#   3 openai-codex/gpt-6.1-sol-max          2927 ms / 74.98 (n=2, prefix-ok; max = top wire-accepted tier)
#   4 xai-oauth/grok-4.7                    verify-first (census 1166 ms / 493.74)
```

## The recipe being followed (documentation quotes, transcribed exactly)

From the config-files documentation, *Different thinking efforts per pool
entry* (https://moonshotai.github.io/kimi-code/en/configuration/config-files.html):

> 1. Register a second entry for the same underlying model in `[models]`,
>    overriding only `default_effort` via `[models."<alias>".overrides]`.
> 2. List both the original alias and the variant alias in the pool.

> The variant is a standalone entry and does not inherit fields from the entry
> it points at: copy `capabilities`, `support_efforts`, and the other metadata
> over in full, otherwise `default_effort` has no effect (it must be a member of
> `support_efforts`).

> Note the asymmetry between the main agent and pool-bound subagents: for the
> main agent, a configured global `[thinking].effort` overrides the variant's
> `default_effort`; for subagents the variant's `default_effort` wins over the
> global value, and only `[secondary_model].default_effort` outranks it.

Block A copies all metadata in full; Block B lists the variant in the pool —
the recipe's two steps, nothing else.

## Apply + verify-after-apply

1. Back up `~/.kimi-code/config.toml` (the operator's existing convention).
2. Splice Block A into the config; splice Block B (and optionally the
   ancillary lines) into the routing table per `routing/APPLY.md`.
3. Reload/restart so the new alias resolves, then dispatch one real subagent
   task at the new alias.
4. **Verify after apply** — the one thing this probe cannot exercise is the
   subagent-path resolution. Confirm the wire value: the shim's request log or
   a capture should show `reasoning.effort: "max"` on the subagent's turns. If
   the client instead resolves the global `[thinking].effort` (M2's
   global-wins ordering was measured on a different path than the docs'
   asymmetry describes), the observed value is still `max` today because the
   live global is `max` — but re-check after any change to the global setting.
5. The variant is **unmeasured as a pool entry**: all numbers in
   `ANALYSIS.md` come from direct HTTP probes at an explicit
   `reasoning.effort`, not from a dispatch through the pool.