# APPLY — R18 routing table + M2 definition corrections

Operator runbook for mission M4 (`r18-routing`). Everything here is a step for a
human or an operator session to run against `~/.kimi-code/config.toml`.

**This mission did not write the live config.** At M4 run time the live file was:

| | |
| --- | --- |
| path | `/home/vgpnk/.kimi-code/config.toml` |
| file sha256 | `c5f12997f7cee456eacddbaf03c95e598ca5911cb18d6e6cf7821909b6fc9ebf` |
| size / lines | 48123 bytes / 1520 lines |
| json-canonical /16 | `2c61f6bbe6c77dc7` |
| `[secondary_model.models]` sha256 | `9dcbc7d2549a911588fb15a8163a5732f00eeaf4ea29b8015415ed749322858d` (17 entries) |
| `[secondary_model]` region | lines **1483–1504** |

The canonical digest is `sha256(json.dumps(parsed_toml, sort_keys=True))[:16]`, the
convention M1/M2 used (`definitions/ANALYSIS.md` provenance block). It is *not*
the file-bytes digest; `sha256sum` will print the other value and that is expected.

**The config has drifted repeatedly today** (32 backups under `~/.kimi-code/`, 21 of
them dated 2026-10-15). Re-run the preflight below before every apply; if the hashes
moved, re-derive the pool and re-check the table rather than applying blindly.

---

## Step 0 — preflight (read-only)

```bash
cp -p ~/.kimi-code/config.toml /tmp/r18-preflight.toml
sha256sum /tmp/r18-preflight.toml
python3 - <<'EOF'
import tomllib, json, hashlib
cfg = tomllib.loads(open('/tmp/r18-preflight.toml').read())
print('pool entries:', len(cfg['secondary_model']['models']))
print('models.*     :', len(cfg['models']))
print('canonical    :', hashlib.sha256(json.dumps(cfg, sort_keys=True).encode()).hexdigest()[:16])
EOF
```

Expected: pool 17, models 143, canonical `2c61f6bb`. If the pool count is not 17,
stop and re-run the M4 table derivation (the table's bucket assignments follow the
pinned pool; `routing/kimi-secondary-models-round18.toml` header records the pin).

Dry-run the splice — this prints the exact diff and writes nothing:

```bash
cd research/round-18-kimi-model-routing/routing
python3 splice_secondary.py                 # DRY RUN against ~/.kimi-code/config.toml
```

The tool refuses to apply when either the file hash or the pool hash differs from
the pin. `--no-hash-guard` exists for scratch/test configs only.

## Step 1 — timestamped backup (host convention)

The host convention is `config.toml.YYYYmmdd-HHMMSS.bak`, next to the config:

```bash
cp -p ~/.kimi-code/config.toml ~/.kimi-code/config.toml.$(date +%Y%m%d-%H%M%S).bak
ls -1t ~/.kimi-code/config.toml.*.bak | head -1     # confirm the new backup
```

`routing/splice_secondary.py --apply` writes this backup itself before replacing
the file, so either path satisfies the convention — do not skip both.

## Step 2 — splice the routing table

```bash
cd research/round-18-kimi-model-routing/routing
python3 splice_secondary.py --apply
```

What it does: reads the 14-entry `[secondary_model]` payload from
`kimi-secondary-models-round18.toml` (everything above its `# SPLICE-END`
sentinel), replaces live lines 1483–1504, re-parses the result with `tomllib`,
checks the new pool equals the table, writes the backup, then replaces the file
atomically with mode 0600. It prints the new file sha256 and the rollback command.

Verified on a synthetic config copy (17-entry pool + `[[hooks]]` tail):
apply → pool 14, `[models.*]` and `[[hooks]]` byte-identical, backup holds the
17-entry pool, no temp files left. The live config was not touched.

Manual alternative (same effect): replace lines 1483–1504 with the payload block
(header comments included) and leave the rest of the file untouched.

### What changes in the pool

| change | ids | evidence |
| --- | --- | --- |
| kept, role text rewritten with measured numbers | 11 (4 FAST, 1 FAST-fallback, 3 MIDDLE, 1 batch, 2 STRONG) | M3 `battery/ANALYSIS.md` §2/§3 |
| demoted (kept, slower role) | `cascade/glm-5.3-flash` (FAST → fallback-only), `alibaba-token-plan/qwen3.8-flash` (MIDDLE → batch) | M3 §8 RE-BUCKET / SLOW-OUTLIER |
| quarantined until reset | 4 token-plan keys 2/3 entries | M1 census D2 (10-23 / 10-28 16:00Z), M3 §3 0/9 |
| dropped | `cursor/composer-2.5`, `cursor/cursor-grok-4.5-low-fast` | M3 §8 RE-BUCKET+SLOW-OUTLIER+NO-TOOL-FORMAT(+WRONG-ANSWER), M2 §4.2 |
| added, verify-first | `xai-oauth/grok-4.7`, `opencode-go/glm-5.3-flash`, `opencode-go/deepseek-v4.1-flash` | census §6 smoke / M6 §2 — census-level evidence only, no battery run |

Dropping the two cursor ids removes two configured lanes. Nothing else in the
config references them (checked: the only references are the `[models.*]` entries
and the pool lines), so no `default_model` or hook breaks. If you want to keep a
cursor lane anyway, keep its measured numbers honest: 7198 ms / 7-9 and 8275 ms /
8-9, both burst-flushed, both unable to emit a tool call.

`default_model` is unchanged (`cascade/deepseek-v4.1-flash`). Rationale: it is the
only entry with a cross-provider chain (opencode-go → hyper → devin) and its
measured 3179 ms sits inside the FAST band (M3 §2/§8). If you prefer raw latency
over resilience, the evidence-based alternative is
`default_model = "hyper/deepseek-v4.1-flash"` (2081 ms / 375.91 tok/s, M3 §2) —
single provider, no fallback.

## Step 3 — M2 definition corrections (`definitions/config-corrections.toml`)

The corrections file holds **56 splice-ready `[models.*]` blocks** (30 in section A,
7 in A2, 19 in E) plus a quarantine list (D), a verify-later list (F) and a global
effort recommendation (C). It was generated against revision `61f22a2bbe52d616`;
the live file is `2c61f6bbe6c77dc7`. Its own drift notice applies:

> "A block carries WHOLE fields, so applying a stale block reverts the newer edit.
> Re-check each block against the current file before splicing."

### 3a. Pool-relevant blocks — 4 of 56 (verified field-by-field against the live file)

| block | live entry today | block would change | verdict |
| --- | --- | --- | --- |
| `hyper/qwen3.8-flash` (A) | `off_effort="none"`, no `reasoning_key` | drops `off_effort` (inert), adds `reasoning_key="reasoning_content"`, adds explicit `protocol`/`base_url` equal to the provider's | **splice-safe** |
| `cascade/deepseek-v4.1-flash` (A2) | no `reasoning_key`; `display_name` identical to the block | adds `reasoning_key`, adds explicit `protocol`/`base_url` (equal) | **splice-safe** |
| `xai-oauth/grok-4.5` (A2) | no `reasoning_key` | adds `reasoning_key`, adds explicit `protocol`/`base_url` (equal) | **splice-safe** |
| `cascade/glm-5.3-flash` (A2) | `capabilities=["thinking","tool_use"]`, `display_name="GLM 5.3 Flash (cascade: devin→zai→hyper)"` | **reverts both**: block carries `["thinking"]` and `...chat-only)` | **do NOT splice as-is** — see below |

`protocol` and `base_url` are real model-level fields (12 live `[models.*]` entries
declare them, all `opencode-go`), and for these four lanes the block values equal
the provider defaults (`hyper` type openai / `https://hyper.charm.land/v1`;
`ds-flash-cascade` `http://127.0.0.1:8791/v1`; `glm-flash-cascade`
`http://127.0.0.1:8793/v1`; `xai-oauth` `http://127.0.0.1:8790/v1`), so making them
explicit is behaviour-neutral.

**Recommended minimal edits instead of whole-block splices** (safer, same effect):

1. `hyper/qwen3.8-flash`: delete the `off_effort = "none"` line and add
   `reasoning_key = "reasoning_content"`.
2. `cascade/deepseek-v4.1-flash`: add `reasoning_key = "reasoning_content"`.
3. `xai-oauth/grok-4.5`: add `reasoning_key = "reasoning_content"`.
4. `cascade/glm-5.3-flash`: add `reasoning_key = "reasoning_content"` and **leave
   `capabilities` and `display_name` as the live file has them**. The A2 block's
   `["thinking"]` + `...chat-only)` values predate the operator's 09:52 edit that
   added `tool_use`; pasting them back would re-assert a chat-only claim the live
   file has since dropped.

Why `reasoning_key` matters: every one of those lanes returned reasoning under
`reasoning_content` while the config named no key (DEF-10, `definitions/ANALYSIS.md`
§4.4), so a reasoning pane cannot render until the declaration matches the lane.

### 3b. The other 52 blocks — catalog-wide, not routing-critical

They touch `[models.*]` entries that no pooled id references (token-plan key-2/3
catalog entries, `hyper/qwen3.7-*`, `kimi-code/*`, `opencode-go/*` catalog entries,
`devin/*`, effort pins in section E). Applying them is an operator call; the same
rule applies — re-check each against the current file first, because 10 fields have
already moved since the audit revision (all `capabilities` gaining `tool_use` on
9 `devin/*` entries plus `cascade/glm-5.3-flash`). None of the drifted entries
except `cascade/glm-5.3-flash` carries a correction block, so only that one block
can revert a newer edit.

Also in that file, and *not* part of the 56:

- **Section C — global thinking effort.** Live `[thinking] effort = "max"` is sent
  to every model and is not clamped to `support_efforts` (DEF-3b, 31 entries; M2
  §3 rule 2). The audit's recommended splice is `enabled = true` with the `effort`
  line removed. Measured consequences (M2 §4.1): `alibaba-token-plan`,
  `openai-codex`, `opencode-go` **validate** the value and accepted `max`;
  `hyper`, `zai-coding-plan`, `xai-oauth`, `cursor` **ignore** the field entirely.
  So dropping the global pin is safe for the pool and is the only way the
  `zai-coding-plan/glm-5.3-flash-low` LOW pin could ever reach the wire — though
  zai ignores the field anyway, so that pin stays cosmetic either way.
- **Section D — quarantine list.** `managed:kimi-code` (401, empty OAuth store, M1
  D1), `alibaba-token-plan{,-2,-3}/glm-5` (403, M1 D3),
  `zai-coding-plan/glm-5.3-highspeed` (429 not in plan, M1 D3), keys 2/3 (429, M1
  D2). None of these ids appears in the pool table (checked) — the routing table
  already handles keys 2/3 by quarantine. They stay catalog entries the operator
  may drop. Note the pool's own `zai-coding-plan/glm-5.3-flash-low` is a different
  id from `glm-5.3-highspeed`.
- **Section F — verify-later.** 46 unverified `video_in`/`audio_in` claims,
  `max_context_size` values (never transmitted), cross-provider cap divergences
  (DEF-5), lanes that ignore `reasoning_effort`, and the devin rate-limit window
  that blocked its re-check.

## Step 4 — reload and verify

The client reads the config at process start, so "reload" means a fresh session.

1. **Parse and digest check**

   ```bash
   python3 - <<'EOF'
   import tomllib, json, hashlib
   raw = open('/home/vgpnk/.kimi-code/config.toml','rb').read()
   cfg = tomllib.loads(raw.decode())
   pool = cfg['secondary_model']['models']
   print('pool entries:', len(pool))                      # expect 14
   print('file sha256:', hashlib.sha256(raw).hexdigest())
   print('pool sha256:', hashlib.sha256(json.dumps(pool, sort_keys=True, separators=(',',':')).encode()).hexdigest())
   EOF
   ```

   The tool already does this before writing, but confirm on the real file.

2. **Syntax gate — and its limit.** `kimi doctor config` is a syntax check only:
   M2 §1 verified that a config with a deliberately misspelled model key, a bogus
   effort value and a bogus capability is reported as **valid**. A clean doctor
   run therefore says nothing about the definitions. It is not a substitute for
   step 3.

3. **One live request per changed lane.** Cheapest instrument is the census chat
   probe (one minimal completion per declared protocol on a provider):

   ```bash
   python3 research/round-18-kimi-model-routing/census/scripts/probe_chat.py \
       ~/.kimi-code/config.toml hyper
   ```

   It prints `status=`, latency, whether reasoning was present and whether a usage
   block came back, and writes `census/raw/chat-<provider>.json` — run it from a
   scratch clone if you do not want that artifact refreshed. For the four lanes
   that gained `reasoning_key`, the same probe shows whether reasoning actually
   returns. Providers worth one probe each after this splice: `hyper`,
   `alibaba-token-plan`, `zai-coding-plan`, `xai-oauth`, `openai-codex`, plus
   `ds-flash-cascade` and `glm-flash-cascade` (the two cascades).

4. **Full re-battery of the changed set** (spends quota: 10 requests per model):

   ```bash
   python3 research/round-18-kimi-model-routing/battery/scripts/run_battery.py \
       --models hyper/deepseek-v4.1-flash,cascade/deepseek-v4.1-flash \
       --outdir /tmp/r18-verify
   ```

   Use this before promoting any verify-first entry — a census smoke number is not
   a battery measurement.

5. **4xx triage — what a failure means**

   | symptom | reading | action |
   | --- | --- | --- |
   | 429 `insufficient_quota` | token-plan key quota dead | keep quarantined until the reset (M1 D2) |
   | 403 `Access to model denied` | id not entitled on that lane | drop the id (M1 D3) |
   | 400 `Unsupported service_tier` | only for codex if you ever add the field | no fast-mode entry exists; see M5 |
   | 400 on an effort value | lane validates effort and rejects it | remove or change the global `[thinking] effort` (M2 §3 rule 2) |
   | 403 `error code: 1010` | scripted user agent blocked (opencode-go) | use a browser-class UA in probes (M2 §1) |
   | request hangs past ~300 s | devin cold start | warm the shim (M1 D7); not a config defect |
   | `temperature` / `max_output_tokens` 400 on codex | D6 shape | omit `temperature`, `max_output_tokens >= 16`, `store:false`, `stream:true` |

## Step 5 — rollback

```bash
cp -p ~/.kimi-code/config.toml.<stamp>.bak ~/.kimi-code/config.toml
```

The backup is a byte copy of the pre-splice file (mode preserved by `cp -p`), so
rollback restores the exact prior state — including the 17-entry pool. The
routing-table file and the M2 corrections file are evidence artifacts; neither is
consumed by the client, so no rollback is needed for them.

## Step 6 — housekeeping

- Re-run `routing/hygiene_check.py` after any edit to the routing tree (it scans
  the tree plus `.ufo/reports/round-18/kengaku.md` for live credential values and
  credential shapes).
- Keep the pool pin in the table's header current: if the operator edits
  `[secondary_model.models]` by hand, the pinned `9dcbc7d2…` no longer describes
  the pool and the bucket assignments must be re-derived from M3's measurements
  for the ids that moved.
- Do not promote a verify-first entry into a bucket without an M3-style run: the
  operator's binding rule is that an unmeasured model may not be promoted.
