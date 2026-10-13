# kama-shokunin — round 1 report

**Lane:** kama (local model serving & endpoint health — probation, shonen)
**Commit:** `c6199a2` in `VeigaPunk/kama-shokunin` (pushed; 23 files, +3164/−27)
**Axis moved:** **operability** 0 → 8 (measured via freshness 0 → 6) — the lowest axes in a
repo that had no `SCORECARD.md` at round start (`SCORECARD.md` created per `AXES.md`).
**Round shape:** the domain's one recurring defect class was still being discovered by
*accident* in other lanes (kagi r3, kengaku r4 — the mint cause). Round 1 converts it into a
single command with an exit code, and pays for it with a full live census.

## What landed (verifiable artifacts)

| Artifact | Measure |
|---|---|
| `tools/kama-probe.sh` | 788 lines, 0755, md5 `932ea3dc365e066e740731cf6a939506`; `bash -n` + `shellcheck -S warning` clean |
| `registry/endpoint-consumers.tsv` | 11 rows × 6 cols, md5 `87eb156b7cc36e98f3cbfb37c00f5351` |
| `corpus/knowledge/*` (8) | listener census (23 listeners, 1 row each), consumer registry (38 rows), `endpoint-identity.md` (7 rule rows), `served-model-identity.md`, `drift-timeline.md`, `cross-lane-scope.md`, `alias-endpoint-normalization.md` |
| `corpus/lessons/*` (5) | `round-1.md` (7 carry-forward rules + 5 method traps), `probe-mutation-matrix.md`, `round-1-critic.md`, `round-1-citations.md`, `round-1-safety.md` |
| `SKILL.md` | 315 lines: 12-row decision table, 11 verbatim error signatures, 13-item runnable checklist, 11 anti-patterns, 47 `path:line` citations |
| `SCORECARD.md` / `PROVINCE.md` / `SHONEN.md` | before→after per axis; owned-surface table + hard write boundary; 4 boxes checked with evidence, promotion **not** claimed (MINT §Probation ≥3 rounds) |

**Gate, run by L1 on the shipped build:**

```
$ bash tools/kama-probe.sh check; echo $?
registry_rows_evaluated=11 model_ok=3 drift=8 exit=2
EXIT=2
$ bash tools/kama-probe.sh check --json | jq .summary
{"registry_rows_evaluated":11,"model_ok":3,"drift":8,"exit":2}
```
3 `MODEL_OK` rows are **positive controls** (`systemd-qwen-coder` @34113, plus both
`ufo-fsd-alpha` pins) — so `check` can report "right", not only "wrong". 8 rows are the
stale 8080 family, all `FOREIGN_SERVICE/html-non-model`.

**Mutation matrix executed by L1 against the shipped build** (scratch fixtures, removed):
M3 correct port + bare-id expectation → `MODEL_OK` exit 0 (proves the `.gguf`-basename
normalization); M4 look-alike JSON, wrong id → `MODEL_MISMATCH served-id-mismatch`; M5 `:8790`
→ `UNAUTHORIZED_SERVICE http-401`; M6 non-HTTP bytes → `NOT_HTTP no-http-response` (no hang);
M2 nothing listening → `DEAD connection-refused`; M7 wrong expected id on the healthy 34113 →
`MODEL_MISMATCH`. All six verdict classes exercised; the four rule holes filed by
`probe-mutation-matrix.md` (M7 identity semantics, M6 timeout, M4 schema boundary, M2
transport map) are closed in the shipped build — contract v3's ordered precedence, which I
issued mid-round as amendments v2/v3.

## The drift, with root cause (the domain's worked example)

- **Live now:** `127.0.0.1:8080` = `docker-jitsi-meet-jvb-1` (`docker-proxy` pid 2245).
  `GET/POST /v1/*` → Jetty HTML `404` (`text/html;charset=iso-8859-1`). Trap: `/metrics`
  returns **200** `application/openmetrics-text` (27461 B), so status-only liveness false-passes
  the stale port.
- **Live now:** `127.0.0.1:34113` = `llama-server` pid 1299, `qwen-coder.service`
  (enabled, active since 2026-09-28 02:55:28), `--port 34113`, serving
  `/scratch/models/qwen3-coder-30b/Qwen3-Coder-30B-A3B-Instruct-UD-IQ2_XXS.gguf`.
- **Stale pins (5 + 1 code default):** `~/.config/opencode/opencode.json:158` (mtime
  **2026-09-28 16:46** — freshly edited, pin still stale), `~/.config/opencode/agents/janitor.md:21`
  ("there is no fallback"), `~/.config/the-janitor/opencode.json:16` (`enabled_providers` =
  `qwen-local` only → fails closed), `~/.local/bin/the-janitor:19`, and the omp binary's
  builtin `baseUrl = Bun.env.LLAMA_CPP_BASE_URL || "http://127.0.0.1:8080"` (env unset).
  `agents/distiller.md:5` is the only one that survives (explicit cloud cascade).
- **Origin of the pin:** `qwen-coder.service.bak.1788033391` (epoch = 2026-08-29) read
  `--port 8080`; the unit was rewritten to `34113` on 2026-09-08 and consumers were never
  repointed. The live unit still advertises the fossil at `:16` (`--cors-origins
  http://127.0.0.1:8080`), and 5 further `.bak`/variant units also read `--port 8080`
  (`qwen-coder.ctx32k-q4.service` is a disabled "UNTESTED variant" that would collide with
  Jitsi if enabled).
- **The box holds the bug and its fix simultaneously:** `~/Projects/origin-work/ufo-fsd-alpha/
  {config/the-tick.machine.json:16, scripts/local-helper.mjs:8}` pin `34113` and probe
  `MODEL_OK` — in **two** checkouts (github-origin `5725fa7d3`, cursor-origin `0522e67a`).
- **The id axis is a second, independent drift:** llama.cpp reports the served id only as an
  absolute GGUF path (`models[].name`/`.model`, `data[].id`/`.aliases`; `models[]` has no `id`
  key) while every consumer declares the bare id — including the *correct-pin* family. And
  `POST /v1/chat/completions` with `{"model":"DEFINITELY-NOT-THE-MODEL"}` returns **200**
  echoing the loaded path, so a round-trip can never detect it. A fix that only repoints
  8080→34113 still reports `MODEL_MISMATCH` unless the comparison normalizes.

## Falsified expectations and corrected claims (peer arbitration)

- **My own frozen fact was wrong:** `~/.omp/agent/config.yml:24` is
  `m_flash: charm-hyper/deepseek-v4.1-flash:max`; my `alibaba-token-plan/…` value was stale.
  Caught by `KamaReviewerCitations`, corrected, never repeated (the reviewer role paid for
  itself).
- **"No config pins 34113" → falsified** (ufo-fsd-alpha family, two checkouts).
- **"Live ESTAB socket to 8080" → not reproducible** (transient; re-samples 0). Superseded by a
  durable TIME-WAIT asymmetry — scout samples 62/26 vs 12/6, `~7×` more host traffic to the
  *stale* port. L1's own two samples read 0, so it is intermittent; the source pid is
  **unattributed** (open).
- **Critic's verdict: CLAIM HOLDS, with corrected wording** — 8080 is HTTP-alive-but-foreign,
  **not** "dead"; kernel-level NAT is undecidable without root. Report wording follows it.
- **Method traps that produced wrong peer conclusions:** bare `ss -tnp` cannot see listeners
  (`0` vs `23` with `-l`); `/home/vgpnk/projects` ≠ `/home/vgpnk/Projects` (inodes `101125103`
  vs `27238`) so a lowercase-root sweep misses the whole ufo-fsd-alpha family;
  `git remote -v | head -2` invents a remote difference.

## L2 concurrency (13 subagents, one batched `task` call)

`KamaPlanner` (endpoint-identity, 7 rows) · `KamaExecutorProbe` (probe+registry) ·
`KamaScoutConsumers` (38-row registry; falsified the 34113 expectation; closed a peer dispute
with inode evidence) · `KamaScoutListeners` (23-listener census; **died after landing its
artifact** — Devin `failed_precondition: weekly usage quota exhausted`, trace
`531a8627a5cbd9852b21d3b7c1480a92`; nothing orphaned) · `KamaScribeSkill` (SKILL.md) ·
`KamaRevengerTimeline` (drift timeline) · `KamaLabratIdentity` (served-id reconciliation) ·
`KamaCriticFalsify` · `KamaReviewerCitations` · `KamaSentinelSafety` (probe redaction/authority
audit) · `KamaMutationMatrix` · `KamaDistillerAliases` · `KamaConnectorSiblings` (cross-lane
scope + handoffs). All edits confined to this repo; operator configs read-only.

**Hygiene:** a whole-file read of `~/.omp/agent/config.yml` surfaced its credential line (key
`token`, `:169`). No artifact contains that value — a key-side scan over every corpus/report
file returned 0 hits. An L1 redaction pass then mis-fired in the *other* direction (a substring
regex matched the model route `alibaba-token-plan/…` because it contains "token"); 4 legitimate
routes were restored. Rule recorded in `corpus/lessons/round-1.md` — same defect class kagi
filed in its round-10 L0 item.

## Adjacency — reported, not absorbed

- **kengaku:** `/home/vgpnk/bench-arena/loop.sh:5` scrapes `:8080/metrics`; `-fsS` passes on
  Jitsi's 200 response, and the parser's `prompt|eval` substring match finds 0 names there vs 4
  on 34113, so benchmark telemetry silently degrades to `journal` instead of llama.cpp counters.
- **kumitate/kagi:** the omp builtin `llama-cpp-local` endpoint default is a fleet-wide code
  path (`LLAMA_CPP_BASE_URL` unset); 8790/8791 are `omp auth-broker`/`auth-gateway` (401) — a
  consumer repointed there would aim prompts at credential brokers.
- **Out of province:** `0.0.0.0:40993` serves a browsable `/tmp` listing on the LAN;
  `127.0.0.1:9222` DevTools with 21 logged-in targets; `the-janitor`'s own service port
  (`40961`) has no listener while its launcher pins it.

## Operator decision filed (`.ufo/l0-questions.md`)

Who applies the 8080→34113 repoint to the four operator-owned pins? kama is charter-bound
(`PROVINCE.md` §Write boundary) to detect and report — writing to `~/.config`, `~/.local/bin`
or systemd units is outside its authority. The correct port is already pinned twice in
ufo-fsd-alpha and the override knobs already exist (`LLAMA_CPP_BASE_URL`,
`UFO_LOCAL_HELPER_URL`, `LLAMA_METRICS_URL`), so the repair is one line per pin. The same file
carries an addendum: the janitor's own config declares `limit.context: 32768` while the live
server runs `--ctx-size 16384` (a second drift class in province, not yet in the registry
schema).

## Residual gaps (round-2 candidates)

1. **Freshness is manual** — nothing runs the gate on a schedule; a pin that goes stale is
   still only caught when someone runs it. Planned round-2 move.
2. 8080 traffic attribution (durable TIME-WAIT asymmetry, unnamed pid).
3. Non-llama.cpp runtimes: rule 6 is measured only for llama.cpp; vLLM/ollama rows are
   `[INFERENCE]`.
4. Declared-vs-served **context** drift, not yet expressible in the registry schema.

**Blockers:** none. **Push scope:** this repo (`VeigaPunk/kama-shokunin`, pushed) and this
report on `VeigaPunk/shokunin`; no domain source tree was written to or pushed.