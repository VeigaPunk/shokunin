# SHONEN — Round 18: kimi secondary-model routing (tower fleet report)

Mission M4 (`r18-routing`, branch `feat/r18-routing-table-and-docs`). Deliverables:
`research/round-18-kimi-model-routing/routing/kimi-secondary-models-round18.toml`,
`routing/APPLY.md`, `routing/splice_secondary.py`, `routing/hygiene_check.py`,
`routing/HYGIENE.md`, this report.

Evidence trees this report summarises, all on `master`:
`census/ANALYSIS.md` (M1), `definitions/ANALYSIS.md` + `config-corrections.toml` (M2),
`battery/ANALYSIS.md` + `battery/SELECTION.md` (M3), `fastmode/ANALYSIS.md` (M5),
`battery-opencode/ANALYSIS.md` (M6).

Pinned state at M4 run time — live `~/.kimi-code/config.toml`, 48123 bytes,
file sha256 `c5f12997f7cee456eacddbaf03c95e598ca5911cb18d6e6cf7821909b6fc9ebf`,
json-canonical `/16` `2c61f6bbe6c77dc7`, `[secondary_model.models]` sha256
`9dcbc7d2549a911588fb15a8163a5732f00eeaf4ea29b8015415ed749322858d` (17 entries),
`[models.*]` 143 entries, providers 13. **The live config was not modified by this
work.**

## 1. Verdict

The pool now has a routing table whose every bucket assignment carries a measured
TTFT/TPS/pass number from the M3 battery, and whose six unreachable or mislabelled
lanes are quarantined, demoted or dropped with the evidence attached. Eleven of the
17 pooled ids keep their slot with rewritten role text; two are demoted
(`cascade/glm-5.3-flash` out of FAST, `alibaba-token-plan/qwen3.8-flash` to batch);
two cursor lanes are dropped; four token-plan key-2/3 entries are quarantined until
their 429 resets; two catalog ids enter as verify-first with census evidence and
explicitly no bucket promotion. The operator's lane policy (2026-10-15) is applied:
opencode-go serves deepseek-v4.1-flash only, and glm-5.3-flash is zai-primary with
devin as its secondary/fallback leg. The definitions work from M2 is staged as a
reviewed splice checklist rather than applied blindly, because one of the four
pool-relevant blocks would revert a newer operator edit.

## 2. Census verdicts (M1)

13 providers / 143 `[models.*]` entries / 140 distinct pairs / 6 shim units all
`active`+`enabled` with live listeners (`census/ANALYSIS.md` §1–§2). Nine defects,
D1–D9; the ones that bind routing:

- **D1 — `managed:kimi-code` answers 401 on every path**, OAuth store file is 0
  bytes. `default_model = kimi-code/kimi-for-coding` is therefore unreachable to any
  client starting fresh from the config (§4 D1). Not in the pool.
- **D2 — token-plan keys 2 and 3 are quota-dead for the whole lane**: 429
  `insufficient_quota`, resets **10-23 16:00Z** and **10-28 16:00Z**; `/models` still
  returns 200 on both keys, so an endpoint listing is not evidence of quota (§4 D2).
- **D3 — `alibaba-token-plan/glm-5` 403 "Access to model denied"** on all three keys
  and **`zai-coding-plan/glm-5.3-highspeed` 429 "subscription plan does not yet
  include access"** (§4 D3).
- **D4 — `/models` is an incomplete oracle**: some configured ids work while unlisted,
  so route on a real completion, never on listing membership (§4 D4).
- **D5/D6 — codex**: `{base_url}/models` misses the shim's route, and the lane accepts
  only a narrow streaming shape (`store:false`, `stream:true`, list `input`, no
  `temperature`, `max_output_tokens >= 16`) (§4 D5–D6).
- **D7 — devin cold start is unbounded**: first chat blocked past 180 s and 300 s; the
  same shim streamed fine afterwards (§4 D7).
- **D8 — opencode-go model-level `base_url` has no `/models`** — a documentation trap,
  not a break (§4 D8).
- **D9 — devin-backed lanes bill a fixed prompt overhead**: 12163 tokens (`devin`) and
  11734 (`glm-flash-cascade`) for an identical short prompt, against 24–48 on the
  non-devin lanes (§4 D9).
- **Usage telemetry**: `managed:kimi-code` exposes no usage signal at all (7 probed
  paths 404); `hyper`, `xai-oauth`, `openai-codex` expose quota headers; reasoning
  tokens are billed outside a small `max_tokens` (361 completion tokens on an
  8-token ask) (§5).
- **Credential exposure (filed as vuln by M1, host-level)**: `glm-flash-shim.service`
  and `ds-flash-shim.service` carry live keys in commented `Environment=` lines at
  mode 0644 vs the config's 0600, inside a git repo with no remote (§2).

Census-level TTFT/TPS smoke: 12 of 15 rows streamed, 7 delivered the answer in one
burst (no TPS reported — "a throughput figure derived from a burst is a measurement
artefact"), 3 could not be probed (§6).

## 3. Definitions audit — defects found, and what is fixed vs staged (M2)

121 defects / 94 notes / 46 verify-later over 143 entries (`definitions/ANALYSIS.md`
§5). The findings that changed the routing table's wording:

- **Two declared fields do not exist in this client**: `off_effort` and
  `max_input_size` have **0 occurrences** in the client binary and **0 wire effect**
  (§1, §3 rule 1). Anything the old table claimed about them was aspirational.
- **The global `[thinking] effort = "max"` overrides every model's own default and is
  not clamped to `support_efforts`** — 31 entries are sent a value they do not declare
  (§3 rule 2, DEF-3b). Measured per lane (§4.1): `alibaba-token-plan`, `openai-codex`,
  `opencode-go` validate the field (invalid control → 400) and accepted `max`;
  `hyper`, `zai-coding-plan`, `xai-oauth`, `cursor` ignore it (invalid control → 200),
  so their "acceptance" proves nothing. Consequence recorded in the table:
  `zai-coding-plan/glm-5.3-flash-low`'s LOW pin cannot reach the wire today.
- **`max_output_size` is transmitted as `max_tokens`**; absent, openai lanes send no
  cap and the server decides (§3 rule 4). The M2 correction for bad caps is removal,
  never a guessed number.
- **`capabilities` barely reaches the wire**: only `image_in`/`video_in` change the
  payload (one extra tool); `tool_use` presence does not add or remove the tool array,
  so **"chat-only" cannot be expressed in config** (§3 rules 5–6). This is why the
  dropped cursor lanes could not be protected by their own label.
- **`reasoning_key` drift**: 2 entries declare `reasoning_content` while the lane
  returns `reasoning`/`reasoning_details` (DEF-9), and 9 declare nothing while the lane
  returns `reasoning_content` (DEF-10) — including three pooled lanes
  (`cascade/deepseek-v4.1-flash`, `cascade/glm-5.3-flash`, `xai-oauth/grok-4.5`) and
  `hyper/qwen3.8-flash` (§4.4).
- **Cross-provider cap divergence** on 19 same-id pairs (DEF-5); **42 of 143 entries
  route to lanes that cannot serve them** (§5 class D).
- **`kimi doctor config` validates no model-level keys** — a deliberately misspelled
  key, a bogus effort value and a bogus capability are reported as valid (§1), so
  doctor's silence is not evidence of correctness.

Staged fixes (not applied by this mission): `config-corrections.toml` with 56
splice-ready blocks (30 A + 7 A2 + 19 E) plus the quarantine list (D) and
verify-later list (F). **Four blocks are pool-relevant**; their field-by-field
verdicts are in `routing/APPLY.md` §3a. One of them, `cascade/glm-5.3-flash`, carries
pre-edit `capabilities = ["thinking"]` and a `...chat-only)` `display_name`, both of
which the live file has since changed — splicing it verbatim would revert the newer
edit, exactly as the file's own drift notice warns. APPLY.md therefore specifies the
minimal per-entry edits instead.

## 4. Battery results (M3), opencode probe (M6), fast mode (M5)

**M3 — the measured pool** (`battery/ANALYSIS.md`; 17 models, 188 of 188 requests,
config `e3c223e0…`, window 2026-10-15T11:59:13Z→12:02:41Z, 0 re-grade mismatches):

| bucket | measured TTFT median | best TPS | members |
| --- | --- | --- | --- |
| STRONG | 2545 ms | 70.82 | 2 (both codex, same upstream model) |
| FAST | 2796 ms | 375.91 | 7 |
| MIDDLE | 4172 ms | 235.56 | 6 |
| VERY-FAST | 7736 ms | — | 2 (both cursor, burst-only) |

- **Bucket labels are not measured speed**: FAST vs MIDDLE holds, but MIDDLE vs
  STRONG, FAST vs STRONG and VERY-FAST vs MIDDLE are all inverted (§4). "Bucket labels
  in this config describe intended role, not measured latency."
- FAST, fastest first: `hyper/deepseek-v4.1-flash` 2081 ms / 375.91 / 8-9;
  `alibaba-token-plan/deepseek-v4.1-flash` 2251 ms† / 226.72 / 8-9;
  `zai-coding-plan/glm-5.3-flash-low` 2796 ms† / 138.21 / 7-9;
  `cascade/deepseek-v4.1-flash` 3179 ms / burst / 8-9;
  `cascade/glm-5.3-flash` 4952 ms / burst / 8-9 (§3).
- MIDDLE: `zai-coding-plan/glm-5-turbo` 2957 / 157.07 / 8-9; `xai-oauth/grok-4.5`
  3476 / 66.71 / 9-9; `hyper/qwen3.8-flash` 4868 / 178.96 / 9-9;
  `alibaba-token-plan/qwen3.8-flash` 13282 / 235.56 / 9-9.
- STRONG: `openai-codex/gpt-6.1-sol` 2212 / 64.46 / 9-9 and `gpt-6.1-sol-high`
  2878 / 70.82 / 9-9 — the two fastest lanes measured, despite the STRONG label.
- † = the lane spends the whole budget on reasoning and never emits a content token,
  so the figure is first-decoded-token time, not content TTFT.
- **10 probes failed on their merits; 40 more were never attempted** because their
  lane had already refused at the perf probe (the four key-2/3 entries, 0/9 each).
- Four lanes are burst-only and carry no derivable TPS (§9) — a shim property, not a
  model property.
- Prediction scoring: ordering claims 7 hit / 7 miss; global claims 5 hit / 1 miss
  (§7). TTFT point error median 1048 ms over 13 models; TPS 52.84 tok/s over 6.

**M6 — `opencode-go/deepseek-v4.1-flash`**: 4157 ms / 327.29 tok/s / 8-9, incremental,
mixed TTFT basis; the pre-registered rule ("earns a FAST slot iff TTFT med ≤ 2800 ms
and pass ≥ 8/9") **fails on latency**, so **no direct FAST slot** (§6). The lane is
already the first leg of the live default cascade, whose value is its fallback chain,
not its speed.

**M5 — codex fast mode: no-go.** `service_tier: "priority"` is accepted (200) while
`flex`, `fast`, `auto` and an invalid control all return 400, so the field is real and
the value passes a value check — but every serviced response echoes `service_tier`
`auto`→`default`, no quota/usage field moves (`x-codex-credits-balance` static at
62500, used-percent static at 1), and the timing delta (+14.00 TPS vs the M3 baseline,
+12.77 vs `default`) is not separable from noise at n=2 while `priority`'s slowest rep
falls below every `default` rep (§1, §5–§6). The kimi client cannot send the field at
all (§3), so a fast-mode routing entry could not work today. Conditional-go protocol
recorded in M5 §7; a shim-side `SHIM_SERVICE_TIER` injection mirroring its existing
effort fix is filed as an idea, not implemented. **No fast-mode entry exists in the
routing table.**

## 5. The new routing policy

`routing/kimi-secondary-models-round18.toml` — 13 live entries replacing 17. Every
role string quotes its measured numbers and its evidence pointer; the full ledger,
ladders and limits are comment blocks in that file.

**Operator lane policy (directive 2026-10-15, recorded verbatim in M4's mission
notes):** *"the opencode-go should be used for deepseek v4.1 flash only, i have a zai
subscription and devin is the secondary provider for the glm 5.3 flash."* Applied:
opencode-go is admitted for `deepseek-v4.1-flash` only (its GLM lane is not in the
table at all), and the glm-5.3-flash cascade is described as zai-primary →
devin-secondary.

- **FAST ladder** (latency-first, measured): hyper 2081 ms → token-plan key 1
  2251 ms → zai `glm-5.3-flash-low` 2796 ms → `cascade/deepseek-v4.1-flash`
  (chain opencode-go→hyper→devin) → `cascade/glm-5.3-flash` (declared policy
  zai→devin, leg order unverified — operator check). Keys 2/3 excluded until reset;
  opencode-go appears on the ladder for deepseek-v4.1-flash only.
- **MIDDLE ladder**: `zai-coding-plan/glm-5-turbo` → `xai-oauth/grok-4.5` →
  `hyper/qwen3.8-flash` → `alibaba-token-plan/qwen3.8-flash` (batch only) →
  `opencode-go/deepseek-v4.1-flash` (verify-first overflow).
- **STRONG ladder**: `gpt-6.1-sol` → `gpt-6.1-sol-high` → `xai-oauth/grok-4.7`
  (verify-first). The table names the single-provider risk: both measured STRONG lanes
  share one shim and one upstream model id.
- **Demotions**: `cascade/glm-5.3-flash` loses its FAST claim (4952 ms, slower than the
  MIDDLE median; no tool call on the tool probe; ~11.8k prompt tokens per call on the
  answering leg); it is now described by policy as zai-primary → devin-secondary, and
  the report carries an operator check on the live shim's actual leg order (§6 item 5).
  `alibaba-token-plan/qwen3.8-flash` becomes a batch lane (13282 ms first token, but
  9/9 at 235.56 tok/s).
- **Drops**: both cursor lanes — the two slowest measured lanes, burst-flushed, and
  unable to emit a tool call (`cursor/composer-2.5` also answered one probe wrong).
- **Quarantine**: the four token-plan key-2/3 entries, with the reset times and the
  re-entry rule (a passing chat probe, not a `/models` 200).
- **Verify-first adds** (census evidence only, never a measured claim):
  `xai-oauth/grok-4.7` (census 1166 ms / 493.74 tok/s) and
  `opencode-go/deepseek-v4.1-flash` (M6-measured, no FAST slot; the only admitted
  opencode-go entry per the lane policy).
- **`default_model` unchanged** (`cascade/deepseek-v4.1-flash`): the only entry with a
  cross-provider chain, measured inside the FAST band; the latency-first alternative
  (`hyper/deepseek-v4.1-flash`) is recorded in APPLY.md §2.

Pool diff, documented per the tower's requirement: the mission notes carried a
26-entry pre-edit pool; the live table holds 17. M3 `SELECTION.md` §3 records the
exact movement — **13 ids removed** (`zai-coding-plan/glm-5.3-flash`,
`hyper/glm-5.3-flash`, `alibaba-token-plan{,-2,-3}/qwen3.8-max`,
`alibaba-token-plan/qwen3.8-max-xhigh`, `zai-coding-plan/glm-5.3`,
`hyper/qwen3.8-max`, `opencode-go/deepseek-v4.1-flash`, `opencode-go/gpt-6-luna`,
`openai-codex/gpt-6-luna`, `xai-oauth/grok-4.7`, `xai-oauth/grok-4.6`) and **4 added**
(`cascade/glm-5.3-flash`, `cascade/deepseek-v4.1-flash`, `cursor/composer-2.5`,
`cursor/cursor-grok-4.5-low-fast`). I read the 08:12:08 backup directly and reproduce
the same two lists; by annotation that revision split 8 FAST / 6 MIDDLE / 12 STRONG
(the mission note's "7 FAST / 6 MIDDLE / 13 STRONG" does not match any revision
retained in `~/.kimi-code/*.bak`, so the captured artifact is used as the authority).
The live 17-id set is **identical** to M3's measured set; only the
`cascade/glm-5.3-flash` role string and 10 `capabilities` fields moved afterwards, so
every measured number in the table applies to a live entry.

## 6. Carried-open items (named, with owner)

1. **token-plan keys 2 and 3** — dead until 10-23 / 10-28 16:00Z; quarantined in the
   table. Owner: operator (M1 D2).
2. **Shim burst-flush fix** — four lanes (both cascades, both cursor lanes) buffer the
   whole answer, so no client-side TPS exists for them; the fix is incremental
   flushing in the shims, outside routing and outside this mission. Owner: shim/operator
   (M3 §9).
3. **opencode-go WAF/UA finding** — a scripted user agent gets `403 error code: 1010`
   from Cloudflare; browser-class UA required for probes, and the client's own UA is
   untested. Owner: tooling/operator (M2 §1).
4. **`kimi doctor` validation gap** — it validates no model-level keys, so a misspelled
   key or bogus capability passes; the verification checklist in APPLY.md therefore does
   not rely on it. Owner: kimi-code client (upstream).
5. **OMP-native route admission (round-17 blocker) — NOT fixed by this work.** Binding
   these definitions into OMP's native routing is kumitate/operator-owned. What this
   round supplies is tested definitions plus a measured, evidence-tagged pool; the
   admission path itself remains outside this fleet's scope.
6. **Credential exposure in the two cascade shim unit files** (live keys in commented
   `Environment=` lines, mode 0644, inside a git repo) — filed as a `vuln` finding by
   M1; host-level fix, operator-owned.
7. **D1 `managed:kimi-code` 401** (empty OAuth store) — `default_model =
   kimi-code/kimi-for-coding` is unreachable to a fresh client; re-auth is the operator's
   call (M1 D1).
8. **D7 devin cold start** — warm the shim on service start so the first real request
   does not pay minutes of latency (M1 D7).
9. **STRONG single-provider dependency** — both measured STRONG lanes share one shim and
   one upstream model; `xai-oauth/grok-4.7` is the cheap mitigation and needs a battery
   run before promotion (M3 SELECTION §3).
10. **M5 conditional-go fast mode** — n ≥ 10 interleaved A/B, both sol pins, independent
    applied-tier confirmation, and a shim `SHIM_SERVICE_TIER` mechanism (the client
    cannot send the field today). Owner: operator/shim (M5 §7).
11. **M2 verify-later** — `video_in`/`audio_in` claims (46 entries), `max_context_size`
    (never transmitted), cross-provider cap divergence (DEF-5), which `reasoning_key`
    spelling the client actually renders for the DEF-9 entries (M2 §8, §F).
12. **Stray listener `127.0.0.1:8799`** in the shim port block, owned by no discovered
    unit and referenced by no provider — recorded as an observation (M1 §2).
13. **Cascade glm-flash-shim leg order vs the zai-primary policy — operator check.**
    Policy (2026-10-15): zai-coding-plan is glm-5.3-flash's primary leg, devin its
    secondary/fallback leg. M2's tool probe was answered by the **devin** leg in pass 1
    and by the **zai** leg in pass 2 (`definitions/ANALYSIS.md` §4.2), so the live shim
    may currently be devin-first. Not asserted either way and not fixed here — shim
    edits are out of scope; APPLY.md Step 4 item 6 is the check.

## 7. Secrets hygiene

`routing/hygiene_check.py` scans every file in this tree plus this report for (1) the
exact credential values configured in the live config (12 provider keys/headers) and
(2) credential-shaped strings. Values are read inside the scan process and never
printed, passed as arguments or written to disk; only counts leave it. Result: **0
hits, exit 0** (`routing/HYGIENE.md`). No credential value, and no
credential-shaped string, appears in any artifact this mission produced; the live
config was opened read-only and never written.

## 8. Verification performed on this mission's own artifacts

- `kimi-secondary-models-round18.toml` parses with `tomllib`; 13 entries, no duplicate
  ids, every id resolves to a live `[models.*]` entry; all 17 pinned pool ids are
  accounted for (13 live + 6 in the quarantine/drop evidence) alongside 2 verify-first
  adds, and the evidence ledger carries all 19 ids. No occurrence of the lane-policy
  excluded GLM entry remains in any artifact.
- `routing/splice_secondary.py`: dry run prints the exact 1483–1504 region diff and
  writes nothing; the pinned-hash guard was exercised (it refused a synthetic config
  and refused on the real config when a guard was re-enabled); an end-to-end `--apply`
  against a synthetic 17-entry config copy produced pool 13, `[models.*]` and
  `[[hooks]]` byte-identical, a timestamped backup holding the 17-entry pool, and no
  leftover temp files. After the lane-policy revision the dry run was repeated against
  a `/tmp` copy of the live config (same pinned bytes): the guards passed and the diff
  is sane.
- `routing/hygiene_check.py`: exit 0, 0 hits (section 7), re-run after the revision
  with identical output.
- Every routing claim in the table quotes an M1/M2/M3/M5/M6 section pointer; the
  per-entry ledger in the TOML carries the decision, the measured numbers, the declared
  caps, the effort note and the evidence pointer.

## 9. Limits — what this does not prove

- n = 2 reps per model for TTFT/TPS and one draw per correctness probe: every number
  is a signal, not a benchmark score (M3 §9).
- Burst-only lanes cannot be ranked on throughput from a client-side measurement.
- The performance prompt is ~50 tokens; long-context ranking may differ.
- Verify-first entries carry census smoke numbers only and must not be promoted without
  a battery run.
- The table is a recommendation with a reviewed splice path; the pool is an operator
  artifact and the live config still holds the old strings until the operator runs
  `routing/APPLY.md`.

## 10. Revision — operator lane policy (2026-10-15, post-review, pre-merge)

The operator issued a lane-policy directive before merge, recorded verbatim in M4's
mission notes: *"the opencode-go should be used for deepseek v4.1 flash only, i have a
zai subscription and devin is the secondary provider for the glm 5.3 flash."*

Changes made, all inside the original scope, no evidence overturned:

- The opencode-go GLM verify-first add is withdrawn entirely — the string does not
  appear in any artifact of this mission. `opencode-go/deepseek-v4.1-flash` remains as
  verify-first (M6 numbers unchanged) and is the only admitted opencode-go entry; the
  FAST-bucket ladder now names opencode-go for that model only.
- `cascade/glm-5.3-flash` keeps its demote decision and every measured number (4952 ms,
  no tool call on the tool probe, ~11.8k prompt tokens on the answering leg), but its
  role and ledger row now state the declared lane policy: zai-coding-plan primary,
  devin secondary/fallback. A one-line operator check is attached because M2's tool
  probe was answered by the devin leg in pass 1 and the zai leg in pass 2 — the live
  shim may be devin-first, which would contradict the policy; the shim was neither
  inspected nor edited (out of scope).
- Counts recomputed: 13 live entries in the table (11 kept + 2 adds), 6 excluded ids
  (4 quarantined + 2 dropped), 19 ids in the evidence ledger.
- APPLY.md carries the shim leg-order check as reload item 6; the routing table holds
  the policy in the ledger header and the fallback-ladder block. Hygiene re-run clean;
  the splice dry run against a `/tmp` copy of the pinned live config still prints a
  sane diff after the revision.

