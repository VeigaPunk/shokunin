# LEGORDER — glm-flash cascade leg order (M9, round 18)

**Verdict.** The live `glm-flash-shim` was **devin-first**, contradicting the
operator's standing lane policy (zai-primary → devin-secondary) that M4 records
as routing text. The order is now **zai → devin → hyper** in the live unit, and
that order is verified serving: `/health`, the shim's own startup log and three
probes (chat, streaming, timestamped stream trace) all show the **zai leg**
answering, with zai's fingerprint — serving model id `glm-5.3-flash`,
`prompt_tokens=19`, z.ai response headers.

| | leg 1 | leg 2 | leg 3 |
| --- | --- | --- | --- |
| before (live) | devin `127.0.0.1:8787` | zai `api.z.ai` | hyper `hyper.charm.land` |
| after (live) | **zai** `api.z.ai` | **devin** `127.0.0.1:8787` | hyper `hyper.charm.land` |

Files edited (both outside this worktree, operator-directed serving-plane work):
`~/.local/share/glm-flash-shim/shim.py` and
`~/.config/systemd/user/glm-flash-shim.service`.
Timestamps: edit + restart at **2026-10-15 11:27:18–11:27:27 -03**.

---

## 1. What defines the order (inspect pass, read-only)

**Mechanism: hardcoded list order in `shim.py::_build_legs()`, with per-leg env
overrides that were not in use.** There is no config file, and the systemd unit
carries no active `GLM_LEG*` environment line — every such line in the unit is
commented out. So the module constants were the live order.

Current order verbatim, from the unit and the shim (`raw/unit.before.txt`,
`raw/shim-buildlegs.before.txt`):

```
[Unit]
Description=glm-flash-shim - OpenAI-compatible 3-leg cascade shim (devin -> zai -> hyper)
[Service]
ExecStart=/usr/bin/python3 %h/.local/share/glm-flash-shim/shim.py
Environment=PYTHONUNBUFFERED=1
# Leg endpoints/keys are overridable here without editing shim.py, e.g.:
#Environment=GLM_LEG2_KEY=<REDACTED-ZAI-KEY>
#Environment=GLM_LEG3_KEY=<REDACTED-HYPER-KEY>
#Environment=GLM_SHIM_TIMEOUT=15
```

```python
# shim.py, before (line 104)
def _build_legs():
    return [
        _leg(1, os.environ.get("GLM_LEG1_NAME", "devin"),
             ... "http://127.0.0.1:8787/v1/chat/completions",
             ... os.environ.get("GLM_LEG1_KEY", "dummy"),
             os.environ.get("GLM_LEG1_MODEL", "glm-5-3-flash-max")),
        _leg(2, os.environ.get("GLM_LEG2_NAME", "zai"),
             ... "https://api.z.ai/api/coding/paas/v4/chat/completions",
             ... os.environ.get("GLM_LEG2_KEY", "<REDACTED-ZAI-KEY>"),
             os.environ.get("GLM_LEG2_MODEL", "")),          # pass-through
        _leg(3, os.environ.get("GLM_LEG3_NAME", "hyper"),
             ... "https://hyper.charm.land/v1/chat/completions",
             ... os.environ.get("GLM_LEG3_KEY", "<REDACTED-HYPER-KEY>"),
             os.environ.get("GLM_LEG3_MODEL", "")),
    ]
```

`run_cascade()` (line 288) walks `for leg in LEGS` in that list order and
advances only on failure, so list position **is** the leg order. `shim.py:443`
prints the chain at startup — that line is the cheapest live proof of order.

Live order before the edit, three independent confirmations:

```
$ curl -s http://127.0.0.1:8793/health
{"ok": true, "service": "glm-flash-shim", "port": 8793, "legs": ["devin", "zai", "hyper"]}

$ journalctl --user -u glm-flash-shim -n 14      # every request, devin-first era
... rid=df3d842dd88f leg=1/devin OK status=200 stream=True 11.578s
... rid=70aed8ab8bf9 leg=1/devin OK status=200 stream=False 1.161s
... rid=39f6c23e14a5 leg=1/devin OK status=200 stream=False 0.949s
```

So yes — **the live order was devin-first**, exactly the state M2 §4.2 inferred
from its tool probe (pass 1 answered by `glm-5-3-flash-max`, pass 2 by
`glm-5.3-flash` after devin rate-limited) and the state M4's routing text flagged
as an "operator check".

---

## 2. The change

Both files were backed up before editing, outside the repo (they carry key
material, so they must not land in the worktree):

```
backup dir  ~/.local/state/glm-flash-legorder-backups/20261015T112513-0300/
            shim.py.bak                        sha256 e7be82845e89b0f151f14c85fa5ea46e58b737ce7e8061ebd53b150549914842
            glm-flash-shim.service.bak         sha256 b3029ad57d04d8db0bf99ff4029be5078576e37304d2684572db1e102d5680df
```

Applied by two auditable scripts in `scripts/` that refuse to run unless the
input's sha256 matches the recorded pre-edit hash:

* `apply_legorder.py` — moves whole `_leg(...)` blocks, so each leg keeps its own
  URL, key literal and model rewrite. Nothing is retyped: no key value appears in
  any command, artifact or report, and **no key material was added to the unit**
  (the active-env route would have required writing the zai key into
  `~/.config`, which is what M1 filed as a vulnerability — it was not taken).
  The script also proves the transformation is index-only (line multiset
  unchanged after blanking `GLM_LEG<n>_` and index digits), compiles the result,
  imports it, asserts the leg list, and asserts the set of
  `Authorization` digests is unchanged (values permuted, never printed).
* `apply_unit_desc.py` — changes exactly one line, the `[Unit] Description`,
  and refuses to write unless every other line — **all 4 comment lines
  included** — is byte-identical.

Resulting sha256 (after): shim.py `710f60c8163bf7a2330398504049774fc7792e3bafe8e7a105153deb28a21a0f`,
unit `257a9e7e53c38b5e8d65fcf9a8d3e1a66225105522ad332573928e0f156ef250`.

**Commented key material (M1 vuln finding): preserved byte-for-byte.**
`grep '^#' <unit> | sha256sum` is `8c779d100e934598364c63243b80ba7475a6187554155cca4d5b30e42f3afa62`
on both the backup and the live file, 4 comment lines on both sides
(`raw/comment-preservation.txt`). Nothing was uncommented, added or removed.

### Diff — shim.py (redacted)

```diff
--- ~/.local/share/glm-flash-shim/shim.py.pre-replace
+++ ~/.local/share/glm-flash-shim/shim.py
@@ -6,12 +6,15 @@
 ordered 3-leg provider cascade, advancing to the next leg only when the
 current leg FAILS.
 
+Leg order follows the operator's lane policy for glm-5.3-flash: zai is the
+primary leg, devin the secondary/fallback leg.
+
 Default legs (all overridable via env - see "LEG CONFIG" below):
-  1. devin        POST http://127.0.0.1:8787/v1/chat/completions  (local
+  1. zai          POST https://api.z.ai/api/coding/paas/v4/chat/completions
+                  (body forwarded as-is; model glm-5.3-flash is correct here)
+  2. devin        POST http://127.0.0.1:8787/v1/chat/completions  (local
                   devin-shim; the body's `model` field is rewritten to the
                   devin slug "glm-5-3-flash-max" before forwarding)
-  2. zai          POST https://api.z.ai/api/coding/paas/v4/chat/completions
-                  (body forwarded as-is; model glm-5.3-flash is correct here)
   3. hyper        POST https://hyper.charm.land/v1/chat/completions
                   (body forwarded as-is)
 
@@ -29,8 +32,8 @@
 to the caller as-is.
 
 LEG CONFIG (env vars, defaults are the module constants below):
-  GLM_LEG1_NAME/URL/KEY/MODEL          leg 1 (devin)
-  GLM_LEG2_NAME/URL/KEY/MODEL          leg 2 (zai)
+  GLM_LEG1_NAME/URL/KEY/MODEL          leg 1 (zai)
+  GLM_LEG2_NAME/URL/KEY/MODEL          leg 2 (devin)
   GLM_LEG3_NAME/URL/KEY/MODEL          leg 3 (hyper)
 A leg's MODEL env var, when non-empty, replaces the request body's `model`
 field for that leg (used by devin); empty means "pass the body through as-is".
@@ -105,26 +108,26 @@
     return [
         _leg(
             1,
-            os.environ.get("GLM_LEG1_NAME", "devin"),
+            os.environ.get("GLM_LEG1_NAME", "zai"),
             os.environ.get("GLM_LEG1_URL",
-                           "http://127.0.0.1:8787/v1/chat/completions"),
+                           "https://api.z.ai/api/coding/paas/v4/chat/completions"),
             {
                 "Authorization": "Bearer " + os.environ.get(
-                    "GLM_LEG1_KEY", "dummy"),
+                    "GLM_LEG1_KEY",
+                    "<REDACTED-ZAI-KEY>"),
             },
-            os.environ.get("GLM_LEG1_MODEL", "glm-5-3-flash-max"),
+            os.environ.get("GLM_LEG1_MODEL", ""),  # empty = body as-is
         ),
         _leg(
             2,
-            os.environ.get("GLM_LEG2_NAME", "zai"),
+            os.environ.get("GLM_LEG2_NAME", "devin"),
             os.environ.get("GLM_LEG2_URL",
-                           "https://api.z.ai/api/coding/paas/v4/chat/completions"),
+                           "http://127.0.0.1:8787/v1/chat/completions"),
             {
                 "Authorization": "Bearer " + os.environ.get(
-                    "GLM_LEG2_KEY",
-                    "<REDACTED-ZAI-KEY>"),
+                    "GLM_LEG2_KEY", "dummy"),
             },
-            os.environ.get("GLM_LEG2_MODEL", ""),  # empty = body as-is
+            os.environ.get("GLM_LEG2_MODEL", "glm-5-3-flash-max"),
         ),
         _leg(
             3,
```

### Diff — unit

```diff
 [Unit]
-Description=glm-flash-shim - OpenAI-compatible 3-leg cascade shim (devin -> zai -> hyper)
+Description=glm-flash-shim - OpenAI-compatible 3-leg cascade shim (zai -> devin -> hyper)
 After=network-online.target devin-shim.service
```

That is the whole diff: 1 changed line, 4 comment lines untouched.

Applied with `systemctl --user daemon-reload` + `systemctl --user restart
glm-flash-shim.service`; listener healthy on 8793 (new PID 878771, active within
2 s, `Restart=on-failure` unchanged).

---

## 3. Verification captures

```
$ systemctl --user status glm-flash-shim.service | head -3
● glm-flash-shim.service - glm-flash-shim - OpenAI-compatible 3-leg cascade shim (zai -> devin -> hyper)
     Active: active (running) since Thu 2026-10-15 11:27:27 -03
   Main PID: 878771 (python3)

$ curl -s http://127.0.0.1:8793/health
{"ok": true, "service": "glm-flash-shim", "port": 8793, "legs": ["zai", "devin", "hyper"]}

$ curl -s http://127.0.0.1:8793/v1/models
{"object": "list", "data": [{"id": "glm-5.3-flash", "object": "model", "created": 0,
 "owned_by": "glm-flash-shim"}]}

$ journalctl --user -u glm-flash-shim   # startup, after restart
... glm-flash-shim listening on http://127.0.0.1:8793 (max 128 concurrent, leg timeout 15s)
... leg 1: zai -> https://api.z.ai/api/coding/paas/v4/chat/completions
... leg 2: devin -> http://127.0.0.1:8787/v1/chat/completions  [model->glm-5-3-flash-max]
... leg 3: hyper -> https://hyper.charm.land/v1/chat/completions
```

Three probes, all against the live 8793 listener, all `rid`-matched in the shim
journal to **`leg=1/zai OK status=200`** (`raw/journal.after-probes.txt`):

```
11:27:36 rid=23aaac319c17 REQUEST model='glm-5.3-flash' stream=False
11:27:39 rid=23aaac319c17 leg=1/zai OK status=200 stream=False 3.081s
11:27:46 rid=55b7c9e020b6 REQUEST model='glm-5.3-flash' stream=True
11:27:49 rid=55b7c9e020b6 leg=1/zai OK status=200 stream=True 2.689s
11:28:03 rid=67614ee97a0c REQUEST model='glm-5.3-flash' stream=True
11:28:06 rid=67614ee97a0c leg=1/zai OK status=200 stream=True 2.752s
```

### Serving-leg fingerprints (same one-line prompt: "Reply with exactly one word: pong")

| probe | path | serving model id | prompt_tokens | headers | wall |
| --- | --- | --- | --- | --- | --- |
| chat (non-stream) | live 8793 → **zai** | `glm-5.3-flash` | **19** | `ga-traceid`, `X-LOG-ID`, `Alt-Svc: h3=":443"`, `Set-Cookie: acw_tc=…` | 3.08 s |
| streaming | live 8793 → **zai** | `glm-5.3-flash` (65 chunks) | **19** | same shape | 2.69 s |
| stream trace | live 8793 → **zai** | `glm-5.3-flash` | — | 42 reads, burst | 2.76 s |
| devin leg direct | 8787 | `glm-5-3-flash-max` | 396 | `Server: devin-openai-shim/2` | 0.87 s |
| failover scratch A | 8795 → leg 2 | `glm-5-3-flash-max` | 396 | — | 1.08 s |
| failover scratch B | 8795 → leg 2 | `glm-5-3-flash-max` | 140 | — | 0.78 s |

So all three response signals agree that the **zai leg** serves leg 1:

1. **Serving model id** — zai passes the body through, so it answers as
   `glm-5.3-flash`; only the devin leg rewrites the body's model to
   `glm-5-3-flash-max` (that is the mechanism M2 §4.2 used to identify legs).
2. **Prompt-token billing** — 19 on the identical prompt, against 140–396 when
   the devin leg answers and 12163 on M1's identical-probe sweep. The overhead is
   leg-attributable; its magnitude is **not** a constant (see §5 caveat).
3. **Header shape** — z.ai's edge headers (`ga-traceid`, `X-LOG-ID`,
   `Alt-Svc: h3`, an `acw_tc` cookie) versus the devin shim's bare
   `Server: devin-openai-shim/2`. The live cascade now returns the former.

Transport note, honestly: the stream trace reports `decode_span_ms=0.4` →
**burst**, i.e. the whole SSE body arrives in one read batch after ~2.75 s. M3
(G3) recorded this lane as burst-flushed and attributed it implicitly to the
devin leg era; the zai leg measured here is *also* burst, matching M1's own
`zai-coding-plan` classification. The lane's missing-TPS property therefore
survives the reorder — it is not a devin artefact.

---

## 4. Leg-2 fallthrough trigger, from the code, and how to test it

`shim.py` advances to the next leg (`run_cascade`, line 288) on exactly:

* connection error (`OSError` / `HTTPException`) — e.g. `devin-shim` down;
* timeout — `GLM_SHIM_TIMEOUT`, default **15 s**, on connect or body read;
* HTTP **402 / 403 / 429** (`FAIL_STATUSES`, line 62);
* HTTP **5xx**;
* HTTP 200 whose first `GLM_SHIM_MARKER_BYTES` (default 2048) contain a quota /
  balance / rate-limit / usage marker — the list is `FAIL_MARKERS`, line 66
  (`quota`, `balance`, `insufficient`, `rate limit`, `rate_limit`, `rate-limit`,
  `ratelimit`, `too many requests`, `usage exhausted`, `exhausted`, `out of
  credits`, `no credits`, `insufficient credits`, `credit balance`, `billing`,
  `payment required`, `limit reached`, `upgrade your plan`, `no remaining`).

Any other status is **terminal** (no advance), and if every leg fails the *last*
leg's status+body is returned to the caller. For `stream: true` the leg is chosen
from the response headers before a single body byte is relayed, so a leg-1
failure never leaks partial output.

**Tested, on scratch ports, without touching the live unit or zai quota**
(`scripts/scratch_failover_test.sh`, output `raw/failover-scratch.txt`):

```
=== A. leg-1 connection error -> leg 2 ===
leg 1: zai-dead -> http://127.0.0.1:9/v1/chat/completions
leg=1/zai-dead FAIL status=None reason=connection error: ConnectionRefusedError: [Errno 111] Connection refused
leg=2/devin OK status=200 stream=False 1.077s
response: {"model": "glm-5-3-flash-max", ..., "usage": {"prompt_tokens": 396, ...}}  http_code=200

=== B. leg-1 HTTP 429 -> leg 2 ===
leg=1/zai-429 FAIL status=429 reason=http 429
leg=2/devin OK status=200 stream=False 0.779s
response: {"model": "glm-5-3-flash-max", ..., "usage": {"prompt_tokens": 140, ...}}  http_code=200
```

Both triggers fall through to the reordered leg 2 and the answer carries devin's
fingerprint. To re-run: `bash scripts/scratch_failover_test.sh` (starts two
throwaway shims on 8795 with leg 1 pointed at a dead port and at
`scripts/mock_429.py`; kills both on exit). It never calls z.ai.

---

## 5. zai quota / rate-limit observation

**No rate limiting observed.** All three live probes were answered by leg 1
(zai) with HTTP 200 on the first attempt; no 429, no marker-bearing 200, no
failover happened in production traffic. The shim's own `FAIL_MARKERS` list is
what would catch a zai quota response, and by construction any such response
would fall through to devin — so zai exhaustion degrades to the previous
behaviour rather than to an error. zai's own limits remain under-sampled (M2 saw
the *devin* leg rate-limit mid-probe); M9 adds three clean zai calls, not a rate
study.

Caveat carried forward: the ~11.7k prompt-token figure must not be quoted as a
fixed constant. On M9's one-line prompt the devin leg billed **396**, and an
identical re-run billed **140**, while M1's sweep on the same mechanism recorded
12163. The claim the evidence supports is "far above the zai leg for an
identical request", not a fixed number.

---

## 6. Follow-up patch text (not applied — `routing/` is outside M9's scope)

### 6a. Required — `cascade/glm-5.3-flash` entry in `routing/kimi-secondary-models-round18.toml:73`

Replace the current value with (the demote stands; the leg-order clause and the
"operator check" caveat are what change):

```toml
"cascade/glm-5.3-flash" = "NOT a FAST lane (demoted). Lane policy (operator directive 2026-10-15): zai-coding-plan is leg 1, devin leg 2 -- applied to the live shim 2026-10-15 by M9 and verified serving (health legs [zai,devin,hyper]; chat + stream probes answered by the zai leg, serving model id glm-5.3-flash, prompt_tokens 19 on a one-line prompt). Measured as configured: 4952 ms -- slower than the MIDDLE median 4172 ms [M3 s8 RE-BUCKET], no tool_calls on the tool probe [M3 s6 t1], and the answering leg billed ~11775 prompt tokens for the identical prompt [M3 s2] -- that billing figure belongs to the devin leg's overhead and was taken while the shim was still devin-first [M1 D9, M2 s4.2]; the devin leg bills 140-396 tokens on M9's one-line probe against 19 on the zai leg, so the overhead is leg-attributable but not a fixed constant. Fallback-only: use when both deepseek cascades and token-plan key 1 are exhausted."
```

### 6b. Optional — the same caveat in the evidence ledger (`:100-105`)

```diff
 # LANE POLICY (operator directive 2026-10-15): opencode-go is used for
 #   deepseek-v4.1-flash ONLY. zai-coding-plan is the primary leg for glm-5.3-flash,
 #   and devin is its secondary/fallback leg. Applied below: the opencode-go GLM lane
 #   is not admitted at all, and the glm-5.3-flash cascade is described as
-#   zai-primary -> devin-secondary, with an operator check recorded on whether the
-#   live shim actually honours that order.
+#   zai-primary -> devin-secondary. The earlier operator check is CLOSED: M9 found
+#   the live shim devin-first, reordered it, and verified the zai leg serving
+#   (glm-flash-legorder/LEGORDER.md).
```

### 6c. Optional — `cascade/glm-5.3-flash` in the ledger row (`:108`) and `routing/APPLY.md` item 6

The row's `(leg order unverified -- operator check)` tail can become
`(leg order zai-first, applied + verified 2026-10-15, M9)`. `APPLY.md` step 4
item 6 ("Operator check — leg order vs the declared policy") is now done: the
shim *was* inspected and edited, and the order matches the policy; item 6 can be
replaced by the verification commands in §3 above.

### 6d. Worth knowing before the next edit of this shim

The unit's commented example line names `GLM_LEG2_KEY` for the zai key. After the
reorder **leg 2 is devin**, so that comment's index is now stale (the value is
unchanged and was preserved byte-for-byte as M1 required). Anyone using the
commented line as the env-var map should read `GLM_LEG1_KEY` for zai now. A
future edit that rewrites that comment should not re-add key material; the
active-env override route would need the key written into `~/.config`, which is
the M1 vulnerability.

---

## 7. Rollback

```bash
BK=~/.local/state/glm-flash-legorder-backups/20261015T112513-0300
cp -p "$BK/shim.py.bak" ~/.local/share/glm-flash-shim/shim.py
cp -p "$BK/glm-flash-shim.service.bak" ~/.config/systemd/user/glm-flash-shim.service
systemctl --user daemon-reload && systemctl --user restart glm-flash-shim.service
curl -s http://127.0.0.1:8793/health       # expect legs back to ["devin","zai","hyper"]
```

The `.bak` files are byte copies of the pre-edit originals (`cp -p`, mode
preserved); the hashes in §2 identify them.

---

## 8. Hygiene

Recorded verbatim in `raw/hygiene-after.txt` (40 files scanned):

```
$ scripts/hygiene_check.sh .
HYGIENE OK: 0 credential-shaped hits under research/round-18-kimi-model-routing/glm-flash-legorder
exit=0

$ grep -rlE "<hex32>\.<alnum16>|sk-<16+>|Bearer <16+>" .     # output to /tmp, then moved in
(no matches -> 0 hits; grep exit 1)
```

(Second command abbreviated: the real one uses the four full patterns from
`scripts/redact.sh`. Its output must go to a file **outside** the scanned tree —
the first attempt redirected into the tree and the recursive grep read the file
it was writing, spinning for 90 s+ in state `R`; `TaskStop`ped, re-run with a
`/tmp` target, identical verdict. Worth knowing for any future sweep here.)

All captures pass through `scripts/redact.sh` at write time, so no artifact here
can carry a key: the unit capture, the shim excerpts and the diffs show
`<REDACTED-ZAI-KEY>` / `<REDACTED-HYPER-KEY>` placeholders. The hygiene patterns
are shape-based (32-hex `.` 16-alnum; `sk-…`; `Bearer …`), not the two known key
values, so an unexpected secret in a future capture is caught too. No
key material was copied into this directory, into the worktree, or into the unit
file; the only key material this mission moved is the existing literals inside
`shim.py`, which stayed in that file and were verified digest-identical across
the edit.

---

## 9. Open items

1. `routing/kimi-secondary-models-round18.toml` and `routing/APPLY.md` still
   carry the pre-M9 "operator check" wording — patch text is in §6, application
   is the routing owner's call.
2. **No re-measure of the M3 perf prompt through the reordered cascade.** The
   landed order was verified for identity (which leg serves), not re-benchmarked
   for latency/TPS; the M3 numbers (4952 ms, burst, 11775 tokens) were taken while
   devin was leg 1 and are not a post-change measurement. A fresh battery row for
   `cascade/glm-5.3-flash` is the natural next step.
3. zai's rate-limit behaviour under sustained load is still unsampled (three
   clean calls here); the fallthrough it would trigger is tested, the threshold
   is not.
4. The unit's stale `GLM_LEG2_KEY` comment (§6d) and the plaintext-key exposure
   M1 filed remain open at host level; M9 preserved them deliberately and did not
   fix or worsen them.