# Cascade leg order — ds-flash-shim `deepseek-v4.1-flash` (mission M7)

| Item | Value |
| --- | --- |
| Mission | M7 `r18-legorder` — R18 ds-flash cascade leg order (operator-directed serving-plane change) |
| Branch / worktree | `feat/r18-ds-flash-cascade-leg-order` in `.tower/worktrees/wt-7` |
| Applied on | 2026-10-15 11:26:20 -03 (restart 11:26:26 -03) |
| Target | `~/.local/share/ds-flash-shim/shim.py` + `~/.config/systemd/user/ds-flash-shim.service` (host files, outside the repo — not part of this branch's diff) |
| Listener | `127.0.0.1:8791`, serving `deepseek-v4.1-flash` (client lane `cascade/deepseek-v4.1-flash`, provider `ds-flash-cascade`) |
| Status | applied, restarted, healthy, verified live |

Operator directive (verbatim, from the mission's Context):

> insert the alibaba token plan as the first one on the cascade for deepseek v4.1 flash; then charm hyper; then opencode go | for the deepseek v4.1 flash cascade

## 1. Before and after, verbatim

| | Leg 1 | Leg 2 | Leg 3 |
| --- | --- | --- | --- |
| BEFORE | `opencode-go` | `hyper` | `devin` |
| AFTER | `alibaba-token-plan` | `hyper` | `opencode-go` |

The former leg 3 (`devin`) carried a model rewrite — the request body's `model` field
was replaced with `deepseek-v4-1-flash-high` before forwarding to the local devin-shim
at `http://127.0.0.1:8787/v1/chat/completions`. That leg is now **removed from this
cascade**; the rewritten body field is gone with it (all three remaining legs pass the
body through unchanged).

Before, read out of the running service:

* `GET /health` → `{"legs": ["opencode-go", "hyper", "devin"], "ok": true, "port": 8791, "service": "ds-flash-shim"}`
* startup log: `leg 1: opencode-go -> https://opencode.ai/inference/go/v1/chat/completions`,
  `leg 2: hyper -> https://hyper.charm.land/v1/chat/completions`,
  `leg 3: devin -> http://127.0.0.1:8787/v1/chat/completions  [model->deepseek-v4-1-flash-high]`
* unit `Description=ds-flash-shim - OpenAI-compatible 3-leg cascade shim (opencode-go -> hyper -> devin)`
* live traffic in the journal was `leg=1/opencode-go OK` on every request

After, read out of the restarted service (`raw/after-alibaba-first.json`):

* `GET /health` → `{"legs": ["alibaba-token-plan", "hyper", "opencode-go"], "ok": true, ...}`
* startup log: `leg 1: alibaba-token-plan -> https://token-plan.ap-southeast-1.maas.aliyuncs.com/compatible-mode/v1/chat/completions`,
  `leg 2: hyper -> https://hyper.charm.land/v1/chat/completions`,
  `leg 3: opencode-go -> https://opencode.ai/inference/go/v1/chat/completions`
* `Description=ds-flash-shim - OpenAI-compatible 3-leg cascade shim (alibaba-token-plan -> hyper -> opencode-go)`

## 2. The mechanism that expresses the order (and what the unit does NOT contain)

The order is **hardcoded as the default leg list in the shim's own code** — `_build_legs()`
in `~/.local/share/ds-flash-shim/shim.py` (after the change: lines 103-145, consumed at
line 148 `LEGS = _build_legs()`). The systemd unit only launches
`python3 %h/.local/share/ds-flash-shim/shim.py`; it sets **no** `DS_LEG*` variable, so
every leg name/URL/key/model comes from those module defaults. Its only leg-related lines
are three commented examples (`#Environment=DS_LEG1_KEY=oc_sk_...`,
`#Environment=DS_LEG2_KEY=sk-hype...`, `#Environment=DS_SHIM_TIMEOUT=15`) — the plaintext
key exposure of the M1 vuln finding. **Those commented lines were not touched** (§4).

Each leg is overridable per-index through the environment: `DS_LEG<N>_NAME`,
`DS_LEG<N>_URL`, `DS_LEG<N>_KEY`, `DS_LEG<N>_MODEL`, plus `DS_LEG1_SESSION` /
`DS_LEG3_SESSION` for the opencode-go session header. A non-empty `DS_LEG<N>_MODEL`
replaces the request body's `model` for that leg; empty means pass-through. This is why the
reorder had to be a code edit: env vars can swap *what* a leg points at, but not the order
of the list, and expressing "opencode-go third" purely by env would have duplicated two
credentials into the unit file.

## 3. The change set

| File | sha256 before | sha256 after | Backup (timestamped, pre-write) |
| --- | --- | --- | --- |
| `~/.local/share/ds-flash-shim/shim.py` | `b9c2056f70612a6b…` | `054011ea87cfc236…` | `shim.py.20261015-112418.bak` (manual) and `shim.py.20261015-112620.bak` (script) |
| `~/.config/systemd/user/ds-flash-shim.service` | `a0668e5a82e9937a…` | `220dbe1ea8ec667d…` | `ds-flash-shim.service.20261015-112418.bak` and `.20261015-112620.bak` |

Diff (masked, regenerated from disk by `scripts/record_diffs.py`):
`raw/shim-py-diff-masked.txt` — 4 hunks, +22 / −18 lines; `raw/unit-diff-masked.txt` —
1 hunk, +1 / −1 line. Changed regions in the new `shim.py`:

* docstring "Default legs" block (new lines 8-12) and "LEG CONFIG" block (new lines 28-33);
* `_build_legs()` (new lines 103-145): leg 1 = `alibaba-token-plan` with the token-plan
  endpoint and `DS_LEG1_KEY`; leg 2 = `hyper` **byte-identical to before** (the diff shows
  no hunk for it); leg 3 = `opencode-go` with the URL, key default and
  `x-opencode-session` value copied out of the file's own former leg-1 constants, and
  `DS_LEG3_MODEL` emptied.

Edit procedure and its safety properties are in `scripts/apply_legorder.py`: the file is
rewritten only if every anchor matches the expected text; the candidate is `py_compile`d
before it replaces anything; backups are taken before the write; credential values are
read from the live config inside the process and never printed (the diff it prints is
masked). After the write it re-imports the file and asserts the built leg list — the probe
returned `[{1 alibaba-token-plan, 2 hyper, 3 opencode-go}]` with `model: ""` on all three
(`raw/apply-record-20261015-112620.json`).

Preservation check on the unit file: `diff` of the backup against the current file shows
exactly one changed line — the `Description=` (line 2). The commented `DS_LEG2_KEY`
plaintext line and every other line, including the `After=… devin-shim.service` ordering
line, are byte-identical. The Three keys that the M1 vuln finding records are untouched by
this mission.

Reload + restart:

```
systemctl --user daemon-reload
systemctl --user restart ds-flash-shim     # MainPID 535566 -> 877365
systemctl --user is-active ds-flash-shim   # active
```

## 4. Verification captures

| Probe | Before (`raw/baseline-opencode-first.json`) | After (`raw/after-alibaba-first.json`) |
| --- | --- | --- |
| `/health` legs | opencode-go, hyper, devin | alibaba-token-plan, hyper, opencode-go |
| `/models` | 200, `deepseek-v4.1-flash` | 200, `deepseek-v4.1-flash` (unchanged) |
| chat (non-stream, 8 tokens) | 200, 1505 ms, leg = opencode-go | 200, 1360 ms, leg = **alibaba-token-plan** |
| chat (`stream: true`) | 200, 2164 ms to first bytes, leg = opencode-go | 200, 1478 ms to first bytes, leg = **alibaba-token-plan** |

Leg identification is header-based, because the shim relays every non-hop-by-hop upstream
header to the caller (M6 used the same trick for `x-opencode-endpoint-id: novita-deepseek`,
which the baseline reproduced). After the change both probes carry the Aliyun Maas gateway
signature — `server: istio-envoy`, `x-envoy-upstream-service-time: 304`, `req-arrive-time`,
`resp-start-time` — and **no** `x-opencode-*` / `CF-RAY` header at all. The response `usage`
block shows the token-plan shape (`prompt_tokens_details.text_tokens`,
`completion_tokens_details.text_tokens`), and reasoning-first output
(`reasoning_content` filled, `content` empty at 8 tokens), matching the M1/M3 description
of the key-1 lane. The shim's own log is the second, independent witness:

```
rid=d4ade316c6b7 leg=1/alibaba-token-plan OK status=200 stream=False 1.360s
rid=7c51cd6678c3 leg=1/alibaba-token-plan OK status=200 stream=True 1.399s
```

Live end-to-end: from the restart until 11:28:37 the journal records **56 requests and 56
`leg=1/alibaba-token-plan OK`, zero failures, zero leg-2 or leg-3 events**. Two of those are
the probes above; the rest is live client traffic through the lane — the cascade in the new
order is serving real work, not just probes.

Key-1 pre-flight (`raw/leg-health-preedit.json`, direct to the provider, shim bypassed):
key 1 = 200 in 1910 ms; keys 2 and 3 = 429 `"Your token-plan 1-month quota has been
exhausted. The quota will reset at 10-23 16:00:00 UTC."` / `10-28 16:00:00 UTC`. The
operator's "key 1 first" intent is therefore verifiable and satisfied.

## 5. How leg 2 / leg 3 take over (for the operator's failover tests)

From the code (`shim.py` `attempt_leg()` / `run_cascade()`), a leg FAILS and the chain
advances on any of:

1. connection error (ECONNREFUSED, TLS failure) — logged `reason=connection error: …`;
2. timeout `DS_SHIM_TIMEOUT` (default 15 s) at connect or on the response head;
3. HTTP 402 / 403 / 429 (`FAIL_STATUSES`);
4. HTTP 5xx;
5. HTTP 200 whose first `DS_SHIM_MARKER_BYTES` (2048) bytes contain `quota`, `balance`,
   `insufficient`, `rate limit`, `usage exhausted`, `out of credits`, `billing`,
   `payment required`, `upgrade your plan`, `no remaining`, … (case-insensitive).

A non-200 outside that set (e.g. 400) is **terminal**: it is returned to the caller and the
remaining legs are not tried. If every leg fails, the caller receives the LAST leg's
response (status + body) verbatim; if no leg produced a response at all, the shim answers
502.

Measured, against the live shim code, on scratch instances with stub/dead legs
(`scripts/verify_fallthrough.py`, full capture `raw/fallthrough-verification.json`):

| Scenario | Result (measured) |
| --- | --- |
| legs 1-2 connection-refused | `leg=1 FAIL … Connection refused`, `leg=2 FAIL … Connection refused`, `leg=3/opencode-go OK` — caller served by leg 3 |
| legs 429 → 500 → 200-with-quota-marker | each fails in order with `reason=http 429`, `http 500 (5xx)`, `200 body marker 'quota'`; caller receives the last leg's 200 body |
| leg 1 200-with-quota-marker | fails with `200 body marker 'quota'`, leg 2 hyper serves |
| leg 1 400 | `http 400 (terminal)`; legs 2-3 never contacted; caller gets the 400 |
| **stream**, leg 1 200-with-quota-marker | leg 1 is **ACCEPTED** — no advance. On `stream: true` the leg is chosen from the response headers before any body byte is read, so a quota message hidden in a 200 body is invisible to the shim |
| **stream**, leg 1 429 | fails over: `leg=1 FAIL http 429`, leg 2 hyper serves |

Consequence worth knowing before testing failover: the real clients send `stream: true`,
and on that path only status-based failures trigger a cascade step. Key-1 exhaustion should
therefore show up as a 429 (which does fail over to hyper) — a "200 with a quota message"
would be passed through to the client as a normal answer. Do not use the streaming shape to
judge whether failover works.

Operator recipe to re-test failover at any time, without touching the live service:

```
# scratch shim on a free port with leg 1 dead, real legs 2-3 untouched:
DS_SHIM_PORT=8794 DS_LEG1_URL=http://127.0.0.1:9/v1/chat/completions DS_LEG1_NAME=dead-leg1 \
  python3 ~/.local/share/ds-flash-shim/shim.py &
python3 research/round-18-kimi-model-routing/cascade-legorder/scripts/probe_cascade.py \
  --port 8794 --out /tmp/scratch.json
# the scratch instance's own log names the serving leg (leg=2/hyper …)
```

`scripts/verify_fallthrough.py` automates exactly this for six scenarios; it needs no
arguments beyond `--out`.

## 6. Quota implication (recorded as the mission requires)

`alibaba-token-plan` key 1 is now **both** the cascade's first leg **and** a pooled FAST
lane in its own right (`alibaba-token-plan/deepseek-v4.1-flash`, FAST rank 2 in
`routing/kimi-secondary-models-round18.toml`), while the cascade is also the pool's
`default_model`. Every default-routed request therefore lands on the same single key.
Keys 2 and 3 of that plan are quota-dead (429) until 10-23 16:00 UTC and 10-28 16:00 UTC,
and the M1 census already recorded that key 1 exposes no quota headers at all — the usage
block is the only signal, and exhaustion is reported in a 429 error body with `retry-after`
as the only machine-readable field. So:

* load on the one healthy alibaba key went up by ~all cascade traffic (previously served by
  opencode-go);
* the pool's FAST rank 2 entry and the default cascade lane now contend for the same quota;
* when key 1 does exhaust, the cascade advances to hyper (leg 2) on a 429 — that behaviour
  is verified above — and to opencode-go (leg 3) if hyper also fails. The shim does not
  rotate among keys 1/2/3; there is no mechanism for that today.

## 7. Follow-up patch text (operator-spliceable)

The three descriptions below still name the old order. They are quoted in full so the
operator can splice them; **this mission did not edit them** (the routing table is M4's
artifact and the live config is outside this mission's write scope).

**7a. `routing/kimi-secondary-models-round18.toml`, line 70 — replace the whole line:**

```toml
"cascade/deepseek-v4.1-flash" = "FAST rank 4 and default (CASCADE lane, leg order reset 2026-10-15 by operator directive: alibaba-token-plan first, hyper fallback, opencode-go third; the devin leg is out of this cascade). 3179 ms measured through the shim under the previous order, burst-flushed so no client-side TPS exists [M3 s2], 8/9; its value is the cross-provider fallback chain, not raw speed [M3 s8]. All three legs pass the tool probe [M3 s2 t1; M6 s4 for the opencode-go leg], where the removed devin leg was chat-only [M2 s4.2]. Leg 1 after the reset: 1360 ms non-stream / 1478 ms to first stream byte on small probes, reasoning-first, Aliyun Maas headers [M7 s4]; it is the same key as FAST rank 2 above, and keys 2/3 of that plan are quota-dead until 10-23/10-28 UTC [M1 usage, M7 s6]."
```

**7b. Same file, line 110 — replace the comment line:**

```toml
# cascade/deepseek-v4.1-flash      | FAST         | keep (default) | 3179 ms / burst (no TPS) / 8-9 (measured under the previous leg order) | ctx 1048576, no out cap (client sends none, M2 s3 rule 4) | none | M3 s2, M3 s8, M6 s6 (opencode-go leg 4157 ms, now leg 3), M7 s4 (leg 1 = token-plan 1360/1478 ms)
```

**7c. Same file, line 173 — replace the chain line:**

```toml
#   4 cascade/deepseek-v4.1-flash          chain alibaba-token-plan -> hyper -> opencode-go
```

**7d. Live `~/.kimi-code/config.toml` (operator applies; not edited here):**

```diff
-# Cascade lanes: ds-flash-shim :8791 (opencode-go→hyper→devin) and glm-flash-shim      # line 18
+# Cascade lanes: ds-flash-shim :8791 (alibaba-token-plan→hyper→opencode-go) and glm-flash-shim
```

```diff
-display_name = "DeepSeek V4.1 Flash (cascade: opencode-go→hyper→devin)"                 # line 1430
+display_name = "DeepSeek V4.1 Flash (cascade: alibaba-token-plan→hyper→opencode-go)"
```

```diff
-"cascade/deepseek-v4.1-flash" = "FAST bucket, CASCADE lane (default): opencode-go first, hyper fallback, devin third on quota exhaustion. Legs 1-2 are tool-capable; leg 3 (devin) is chat-only — a tool task that cascades all the way degrades."   # line 1493
+"cascade/deepseek-v4.1-flash" = "FAST bucket, CASCADE lane (default): alibaba-token-plan (token-plan key 1) first, hyper fallback, opencode-go third on quota exhaustion; the devin leg is out of this cascade. All three legs are tool-capable."
```

## 8. Rollback

```
cp -p ~/.local/share/ds-flash-shim/shim.py.20261015-112620.bak ~/.local/share/ds-flash-shim/shim.py
cp -p ~/.config/systemd/user/ds-flash-shim.service.20261015-112620.bak ~/.config/systemd/user/ds-flash-shim.service
systemctl --user daemon-reload && systemctl --user restart ds-flash-shim
```

`GET /health` should then report `["opencode-go", "hyper", "devin"]` again. The earlier
`.20261015-112418.bak` pair is the same pre-change content.

## 9. Evidence index

| Path | What it is |
| --- | --- |
| `scripts/probe_cascade.py` | `/health` + `/models` + chat + stream probe with header-signature leg identification |
| `scripts/probe_leg_health.py` | direct single-lane (optionally key-1/2/3 triplet) provider probe |
| `scripts/apply_legorder.py` | the reviewed edit: anchors, backups, py_compile gate, masked diff, rebuild assertion |
| `scripts/verify_fallthrough.py` | six-scenario fallthrough harness with local stub legs |
| `scripts/record_diffs.py` | regenerates the masked diffs + hashes from the live files |
| `raw/baseline-opencode-first.json` | before: health/models/chat/stream + leg signatures |
| `raw/after-alibaba-first.json` | after: same four probes, served by alibaba-token-plan |
| `raw/leg-health-preedit.json` | token-plan keys 1/2/3 direct health |
| `raw/fallthrough-verification.json` | the six measured fallthrough scenarios |
| `raw/apply-record-20261015-112620.json` | hashes, backup paths, leg-order assertion after the edit |
| `raw/shim-py-diff-masked.txt`, `raw/unit-diff-masked.txt` | the applied diffs, masked |
| `HYGIENE.md` | secrets-hygiene gate over every artifact in this directory |