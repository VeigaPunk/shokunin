# KamaHistoryClaims — advisory

Seat: `KamaHistoryClaims` (L2 leaf, report-only). Not a native judge verdict, lane round report, receipt, or admission.

Lane: `kama-shokunin` @ `ea72c3eae4ecc68dab2b0a08153c9c1d2e16df21` (matches `baselines.json` kama.head). Plan: `kama-shokunin/plans/wwkd-round-4-recensus.md`. Before receipt: `.ufo/waves/shokunin12h-20261014-p1-repair/evidence/kama-before.json` (`consumers` exit 0; not re-run).

Write scope used: this file only. No lane file, gate file, LOG, corpus note, SCORECARD, or sibling report was edited. Original LOG/corpus bytes are unchanged. Credentials, oauth, `server.token`, and session material were not content-copied. `~/.omp/agent/config.yml` and `~/.config/opencode/opencode.json` were shape-checked only (existence, line count, key/selector booleans, secretish-line redaction).

## Verdict

No remaining falsified gate defect. Round-3 `$UFO_SRC` / `--ufo-src` repair still matches the live probe. Do not re-repair it.

Citation inventory is not clean. Present-tense SKILL, PROVINCE, and several corpus notes still cite deleted host paths or superseded dispatch lines as current. The 2026-10-14 `consumer-registry.md` §Errata still matches the deleted-path and relocated-anchor measurements, but it does not cover those other surfaces, and it pins a revision hash that must be described, not treated as durable identity.

Parent appends the drafts below. This seat does not.

## Measurement basis (2026-10-14, this seat)

- `git -C kama-shokunin rev-parse HEAD` → `ea72c3eae4ecc68dab2b0a08153c9c1d2e16df21`. Porcelain: `?? plans/` only (parent plan; not this seat).
- `git -C ~/Projects/ufo-fsd-alpha rev-parse HEAD` → `964f443ee53df0ce06bd689af01f0dea031b01f9`, subject starts `routing: regenerate omp-seat-routing mirror`. `git cat-file -t 964f443e` → `commit`. `merge-base --is-ancestor 964f443e HEAD` exit 0. Remote *names* only: `cursor`, `origin`. `~/Projects/origin-work/ufo-fsd-alpha` absent.
- Probe/registry hashes (file bytes, not a gate run): `tools/kama-probe.sh` md5 `1f81e859c2d7f43f87d1f7e01327b2cf` (1093 split lines, no trailing newline → 1092 newline-count, matching SCORECARD); `registry/endpoint-consumers.tsv` md5 `aa033020d99d2e271d2eb0499ab8281f`; `tools/test-snapshot.sh` md5 `860f26ac05938cdfc1a8816eff1570b4`, 24 `ok` sites counted, suite not executed.
- TCP `connect_ex` 127.0.0.1, 0.4s: `8080`, `34113`, `8790`, `8791`, `8888`, `11434` → 111 (refused); `631` → 0 (listening). HTTP class of 631 was not fingerprinted.
- `systemctl --user is-active qwen-coder.service` → `inactive` (rc 4); `is-enabled` → `not-found` (rc 4). `~/.config/systemd/user/qwen-coder*` glob empty.
- `docker ps --format '{{.Names}}'` → 0 containers; no jitsi name.
- `~/.local/bin/omp` contains `LLAMA_CPP_BASE_URL || "http://127.0.0.1:8080"` once (byte search, no other strings copied).
- `~/.config/opencode/opencode.json`: exists, 95 bytes, 5 lines; booleans `qwen`/`8080`/`baseURL`/`34113` all false. Content not copied.
- `~/.omp/agent/config.yml`: exists, 492 lines. Claimed alias lines 21–44 do not contain the claimed keys or selectors. Non-secret loopback line count 0. Line 168 does not contain `8790`. Line 169 matches a secretish pattern and was not copied. Exact `modelRoles:` header at line 160.

Path existence (deleted vs present) is the classification evidence for citation-to-deleted. Line reads below are the evidence for line-drift vs live anchors.

## How to read a class

- **live** — cited path and claimed fact still measure true.
- **superseded historical** — true of a named earlier time, and either already marked or safe to mark historical without rewriting the original sentence.
- **unresolved** — still written as current, and measurement falsifies that reading. Retained as named debt until parent appends errata. Not a license to edit the original bytes.

Defect kinds, by measurement: stale `--src` (none remaining in the gate), citation-to-deleted, line-drift, genuine defect (none in the probe).

## Clusters

### 1. SKILL body still speaks as if the 2026-09-28 box is now — unresolved, citation-to-deleted

`SKILL.md:33-84` (worked example, six-consumer table, fossils), decision-table “Live:” cells (`:110`, `:114`, `:118`), checklist items 3–13 (`:193-223`), and anti-patterns 1, 5, 7, 9 (`:229-263`) use present tense for paths that are absent:

| cited as current | measured |
|---|---|
| `~/.config/systemd/user/qwen-coder.service` and `qwen-coder*.service*` archives / ctx32k unit | absent; unit `not-found` |
| `~/.config/opencode/agents/janitor.md`, `distiller.md`, `agents/` | absent |
| `~/.local/bin/the-janitor`, `~/.config/the-janitor/` | absent |
| `opencode.json.*.bak*` fossils named at `:82-84` and `:318-322` | absent |
| `~/.config/opencode/opencode.json:154,158,161` pin `localhost:8080/v1` | file exists, 5 lines, no `8080` / `qwen` / `baseURL` |
| `~/.local/bin/llama-server` | absent (cited-sources bullet already says producer files are historical) |
| `docker-jitsi-meet-jvb-1` on 8080; llama-server pid 1299 on 34113 | no containers; both ports refused |
| checklist item 13 `active/running/1299` | `inactive` / `not-found` |

Checklist item 1 (`SKILL.md:174-184`) and the cited-sources tail (`:300-311`, `:312-315`) already record the 3-row / DEAD / deleted-producer state. The body contradicts that tail. A reader who stops at the worked example will reprobe deleted files.

`SKILL.md:93` cites `corpus/knowledge/consumer-registry.md:54-55` as the census rows for the-tick and local-helper. Those lines are the webzites-deletion errata sentence, not the table. Rows 17–18 are at `consumer-registry.md:106-107`. Line-drift caused by the errata insert. Unresolved.

`SKILL.md:326` says “37-row census”. The table has 38 numbered rows (`| 1 |` … `| 38 |`). Off-by-one, not a deletion.

Registry md5, 3 row ids, and the `--ufo-src` > `$UFO_SRC` > first-existing order at `SKILL.md:300-307` match `kama-probe.sh:103-106,141-142,537-551` and `endpoint-consumers.tsv:35-37`. That slice is **live**.

### 2. PROVINCE owns-table — unresolved, citation-to-deleted

`PROVINCE.md:10-11` still names as concrete artifacts:

- `~/.config/systemd/user/qwen-coder.service` (llama-server, `127.0.0.1:34113`) — file absent, unit not-found, port refused.
- `~/.config/opencode/opencode.json:158` — file exists, pin absent (cluster 1).
- `~/.config/opencode/agents/janitor.md:21` — file absent.

`PROVINCE.md:22-26` write boundary and `:17-20` refuse-list are still the right contract (internal citations from `cross-lane-scope.md` to those lines still resolve). No errata section exists.

### 3. `consumer-registry.md` §Errata — live for deletions; hash must not be pinned

`corpus/knowledge/consumer-registry.md:30-80` (2026-10-14) still matches this pass:

- `origin-work/ufo-fsd-alpha` absent; `~/Projects/ufo-fsd-alpha` present.
- `~/Projects/webzites` absent (also `~/wikillm/llm-wiki`, `~/Projects/ephemeral`).
- Deleted set in `:56-62` still absent, including `~/archive/bench-arena/loop.sh` and `/tmp/fleet-override.yml`.
- opencode.json shape matches `:62-64`.
- Ports 8080 and 34113 refused; unit deleted. Matches `:70-72`.
- `$UFO_SRC` resolution text matches the probe. Not a stale `--src`.

Re-measured anchors that the errata says still hold, and do:

| anchor | this pass |
|---|---|
| `config/the-tick.machine.json:16` endpoint `http://127.0.0.1:34113/v1/chat/completions` | exact (`:16`); `apiModel` `:13`; path `:12`; slots `:17-18`; model block `:7-13` |
| `scripts/local-helper.mjs:8` `DEFAULT_URL` | exact; `DEFAULT_MODEL` `:9`; doc `:312`; call `:325`; credential-free `endpoint_invalid` condition `:159-161` (range `:155-161` also includes the invalid-URL fail at `:157`) |
| `tests/the-tick.test.js:61,:125,:1457` | exact 34113 strings |
| `tests/local-helper.test.js:263-266` | exact four 8080 rejection fixtures |
| `docs/THE-TICK.md:29` | exact 34113 completions URL |
| `evidence/nightcall-integration/nc2-verify-global-r01-route-authority.json:135,:144` | exact endpoint and the quoted “No Qwen3-Coder/34113/…” sentence |
| `config/mission-nightcall.yml:4-5` | exact “GLOBAL m_* alias table … no project route pins” |

`MODEL_OK` / `FOREIGN_SERVICE` cells in the preserved table are already declared historical by `:72-73`. Do not rewrite those rows.

Describe-don’t-pin: the errata and `endpoint-consumers.tsv:36` and `LOG.md:55-56` and `SKILL.md:91` all print `HEAD 964f443e` as if it were the checkout’s identity. It equals HEAD *today*. It is not a superseded-revision falsehood yet. It will become one on the next commit if left as a pin. Draft below says “describe the resolver; record the hash only as the measurement-time value.”

The one-line finding at `consumer-registry.md:16-28` (“still pin”, “live llama-server”) sits *above* the errata and is easy to read as current. Class: superseded historical, marking incomplete. Do not edit those sentences; append a pointer.

### 4. Alias table — unresolved, superseded revision presented as current

`corpus/knowledge/alias-endpoint-normalization.md:7-31` is labeled the canonical current `modelRoles` table and cites `~/.omp/agent/config.yml:21-44`.

Measured: lines 21–44 are comment/rules text, not alias rows. Every claimed key and every claimed selector is absent on its cited line. Loopback grep claim in the 2026-10-14 errata (`:41`) still holds (0 non-secret loopback lines; line 168 has no `8790`). That errata did **not** re-check the line table.

Key presence anywhere in the file (names only; values not copied):

- Absent as keys: `m_kimi`, `m_dsflash`, `m_qwen`, `m_lunamax`, `m_daybreak`, `m_grok46`, `m_astra`, `m_z53`, `m_zflx`, `m_grok47`, `m_kcode`, `m_opus`, `m_opus_h`, `m_sol6`, `m_composer_h`.
- Claimed selectors absent even as substrings on non-secret lines: `cursor/kimi-k3-max:max`, `openai-codex/gpt-5.6-luna:low`, `openai-codex/gpt-daybreak-blue-latest:max`, `xai-oauth/grok-4.5:low`, `xai-oauth/grok-4.6:xhigh`, `openai-codex/gpt-6-astra:max`, `devin/swe-2:max`, `zai/glm-5.3-flashx:xhigh`, `xai-oauth/grok-4.7:high`, `openai-codex/gpt-5.6-sol:high`, `anthropic/claude-opus-5-5:max`, `anthropic/claude-opus-5-5:high`, `openai-codex/gpt-6-sol:high`, `xai-oauth/grok-composer-2.5-fast:high`.
- `alibaba-token-plan/deepseek-v4.1-flash:max` and `alibaba-token-plan/qwen3.8-max:xhigh` occur only on secretish lines (counts 5 and 3). Not copied. Not evidence they are still `modelRoles` values.
- Keys that still occur, not at the cited lines: `m_flash`, `m_luna`, `m_grok`, `m_composer`, `m_swe`, `m_zfl`, `m_sol`, `m_antigravity`. `m_luna`’s old selector `gpt-5.6-luna:low` is absent; `openai-codex/gpt-6-luna:max` is present on non-secret lines 269 and 482. That is a superseded selector, not a line slide of the same claim.
- New keys not in the 2026-09-28 table (names only): `m_strong`, `m_qwen38max`, `m_mid`, `m_fast`, `m_k3`, `m_kfc`, `m_glm53`, `m_grok45`, `m_haiku`, plus effort variants. Do **not** publish a replacement table.

`alias-endpoint-normalization.md:46` cites `MISSION.md:37-43` as the mission route bucket and `kama-round-1.md:7` as the kama route map.

- `kama-round-1.md:7` is **live**: the long line does contain `Route map: planner/connector @m_lunamax; executor/scribe/scout @m_flash; … @m_zfl`. It names aliases, not endpoints.
- `MISSION.md:37-43` is **line-drift**. Those lines are the axes-framework section, not a route bucket. The role-class table is `MISSION.md:56-60` (heavy-reasoning / fast-execution / economy). It still defines no `@m_*` selector and no endpoint. The negative claim survives at the drifted location; the cited lines do not.

`alias-endpoint-normalization.md:56` still says `~/.local/bin/the-janitor:16-19` must remain a registry row and `distiller.md:5-8` is cascade-protected. Both files are absent; those registry rows were removed in round 3 (`SKILL.md:308-311`). Unresolved citation-to-deleted plus a stale obligation.

`config/l1-max-context.yml:19-22` (`alias-endpoint-normalization.md:48`, repeated from the 2026-10-14 errata) overruns EOF. The file is 20 lines at this same HEAD `964f443e`. Lines 16–20 are the context-policy statement (`extendedContext: true` at `:20`). Substance live; range wrong when the errata was written. Line-drift, not a later move.

### 5. `cross-lane-scope.md` — unresolved present tense; report citations live

`corpus/knowledge/cross-lane-scope.md` has no errata. Present-tense host claims are falsified by cluster 1:

- `:12-18` ownership rows cite deleted `opencode.json:154-163`, `janitor.md`, `distiller.md`, `the-janitor:16-19`, `qwen-coder.service:13-22`.
- `:20` “endpoint currently at 8080 is Jitsi” / “llama-server is on 34113” — both ports refused; no jitsi container.
- `:38-41` handoffs: “still target 8080”, “34113 is the local llama.cpp serving endpoint”.
- `:30` “existing disabled 8080 variant must not be enabled” — unit file absent, so the trap is historical, not latent.

These are citation-to-deleted / stale host-state, unresolved until an append marks them historical.

Citations that still resolve (live historical documents, not deleted):

- `../.ufo/reports/round-3/kagi.md:23-27,67-71` — lines exist and still say endpoint drift / Jitsi squat (`:23-25`, `:69-71`). File is 73 lines.
- `../.ufo/reports/round-4/kengaku.md:18-25,70-79` — lines exist; `:20-23` still records the drift; `:79` is the operator-repoint note. File is 79 lines.
- `MINT.md` cited ranges (`:16-17`, `:18-22`, `:35-42`, `:49-59`) are inside the 67-line file. `MINT.md:29-30` already marks `~/Projects/webzites` historical. That path is still absent. Superseded historical, already marked.
- `PROVINCE.md:22-26` write-boundary citations still match.
- `../AXES.md:15-17` still the calibration/adjacency rows. Live.
- `../.ufo/reports/round-*/kotoba.md` and `kumitate.md` “no 8080|34113 matches” was a round-1 search. Not re-run this seat (sibling trees are moving under other lanes). Do not treat that negative as a fresh fleet fact.

### 6. `drift-timeline.md` — superseded historical, marking incomplete

`corpus/knowledge/drift-timeline.md:7-20` is a dated reconstruction whose source files are now absent (opencode backups, `qwen-coder.service`, `the-janitor`, agent files, and the 2026-09-28 “Current consumer” row at `:17`). No deletion errata. The dates were true when measured; the word “Current” is not true now. Class: superseded historical. Append a banner; do not rewrite the table.

Jitsi `Created=2026-09-15T01:31:55Z` (`:15`) cannot be re-checked: no jitsi container is running. Leave the row as historical evidence, not a live docker fact.

### 7. Probe line pins — line-drift, not a genuine defect

`endpoint-identity.md`, `snapshot-history.md`, and `corpus/lessons/round-2.md` cite `tools/kama-probe.sh` line ranges from before the round-3 growth. Same md5 GateRepair reported; no probe edit this wave. Behavior was not lost. The coordinates moved.

| cited range | what is there now | symbol still in file |
|---|---|---|
| `:32-34` (called the normalizer) | exit-code comment; served-id rules *header* starts at `:34` | rules body `:35-39`; `normalize_id` `:370-371` |
| `:47-48`, `:83-85` (timeouts) | persistence comments; `cleanup` trap | usage `--timeout` / `--connect-timeout` `:107-108` |
| `:80-85`, `:723-733` (`--port` / `--expect`) | `warn`/`die`; row resolve | `--port` parse `:120` |
| `:111-150` (single-port persist refusal) | usage text; `:150` is the `OPT_PORT` parse branch | comment `:46` “snapshot refuses --port mode” |
| `:253-256` (no retry loop) | listener-owner loop | no-retry site **not re-located** this pass |
| `:338-350` (normalize) | python `group()` | `normalize_id` `:370-371` |
| `:386` (`GET /v1/models`) | `found==0` return | fetch `:418` |
| `:481-487` (`schema-unrecognized`) | `served_ids` assign | reason `:516` |
| `:555-572` (userinfo strip) | `expand_path` / `$UFO_SRC` | userinfo strip `:609` (also mentioned `:950`) |
| `:799-803`, `:932-936` (`eval_rows` status capture) | `EV_` fill; delta append | `eval_rows` defined `:788` |
| `:911-928` (basename/`.gguf`) | delta text | `normalize_id` `:370-371` |
| `:932-1003` (exit + flock) | delta append; flock comment happens to sit at `:998` | do not treat the span as an identity |

`listener-census.md` line pins inside `endpoint-identity.md` that still match the historical sample: `:50` 8080, `:51` 8888, `:52` 8790, `:54` 4226, `:55` 43999, `:56` 9222, `:59` 40993, `:60` 45507. `:171` does **not**: `endpoint-identity.md:13` says port 40961 had no listener at `listener-census.md:171`. Line 171 is the “§4 Drift flags” heading. The 40961 row is `listener-census.md:179`. Line-drift inside a historical sample. The census header (`listener-census.md:3`, measured 2026-09-28) already makes the file superseded historical. SKILL checklist item 3 still tells the operator to pin those classes as current (`SKILL.md:196-199`). That reuse is unresolved, same as cluster 1.

`endpoint-identity.md:122` “`opencode.json:158` declares `http://localhost:8080/v1`” is present tense. Citation-to-deleted/emptied. Unresolved.

`served-model-identity.md:20-21` slot JSON, cited by `endpoint-identity.md:91`, still matches that historical sample. The file is a captured curl transcript, not a live probe. Superseded historical by genre; no deletion mark. Port 34113 refused, so the transcript must not be re-read as now.

### 8. Round-2 citation errata overtaken by deletion — superseded historical

`corpus/lessons/round-1-citations.md:64-75` correctly recorded, on 2026-09-29:

- `enabled_providers` at `the-janitor/opencode.json:5-7`, baseURL at `:16`.
- `~/bench-arena/loop.sh:5` moved to `~/archive/bench-arena/loop.sh:5`.

Both paths are now absent (round-3 deletion, confirmed this pass). The errata was right when written and is now itself a citation-to-deleted. Do not rewrite it. Append that the correction was later overtaken.

`corpus/README.md:28-32` already marks the three operator pins historical and points at §Errata. That paragraph is **live**. It does not cover SKILL/PROVINCE/cross-lane-scope.

`LOG.md:55-56` origin-work errata is accurate as a historical marker. The hash in it is a pin (cluster 3). Do not edit the line.

### 9. Sibling-doc citations — live targets, stale host claims are not kama’s to absorb

These `consumer-registry.md` rows still resolve to the claimed text. They are not citation-to-deleted:

| row | path:line | this pass |
|---|---|---|
| 22 | `kengaku-shokunin/SKILL.md:322-323` | still says “now Jitsi” / “live llama-server” / `qwen-coder.service` |
| 23 | `kengaku-shokunin/PROVINCE.md:14` | still presents `http://127.0.0.1:34113` as the served local model |
| 24 | `kagi-shokunin/.../janitor-env-contract.md:55` | still quotes `MODEL_ENDPOINT=...8080/v1` |
| 25 | `handler-trust-boundary.md:131,:246` | 8080 baseURL and 34113 repair snippet still there |
| 26 | `credential-isolation.md:35,:75` | 8080 strings still there |
| 27 | `drift-gate.md:185` | `sed` 8080→34113 still there |
| 28 | `kumitate-shokunin/.../ops-watchers.md:393` | still quotes `config.backend.endpoint` 34113 |
| 29 | `remaining-scripts-census.md:524` | line contains `127.0.0.1` and `34113` (local-helper prose) |
| 30 | `.ufo/waves/round-9/seats/standing-tables.md:131,:243-244` | still says both configs pin 8080 and 34113 health is 200 |

Verdict cells on those rows are already covered by the blanket “every MODEL_OK/FOREIGN_SERVICE in the table is historical” (`consumer-registry.md:72-73`). The *sibling documents* still speak in the present. Owner is the sibling lane / aggregator, not a kama gate edit.

`opencode.log` row 35 cites lines 3898, 5281, 6194, 6308. File exists, **3211 lines**. Those line numbers are past EOF. Line-drift / truncation. Content not read (log may carry prompts). Unresolved until the row is marked “lines no longer in the file; do not re-pin.”

`~/Projects/ufo-fsd-alpha/.omp/skills/ufo/references/run-logic.md:495` and `skills/wwkd/SKILL.md:129` are prose uses of the word “endpoint”, not URL pins. Matches the 2026-10-14 re-measure. Live as prose citations.

### 10. Stale `--src` — none remaining

Gate resolution (`kama-probe.sh:527-551`) is flag, then `$UFO_SRC` if a directory, then first existing of `~/Projects/ufo-fsd-alpha`, `~/Projects/origin-work/ufo-fsd-alpha`, else empty → `file=missing`. Registry rows use `$UFO_SRC/...`, not a hardcoded checkout. `origin-work/` strings left in the corpus table and `LOG.md:52-53` are historical and already marked (`LOG.md:55-56`, `consumer-registry.md:35-38`). Explicit bad `--src` stays bad (`:141-142`). No code change.

`KamaGateRepair` reported the same conclusion and did not edit the probe. This seat agrees. Doc line-drift is not a probe defect.

## Proposed delta

Append-only. Do not rewrite, rebase, or “fix” the original sentences. Do not edit `tools/kama-probe.sh`, `registry/endpoint-consumers.tsv`, or `tools/test-snapshot.sh` for any cluster above.

Describe-don’t-pin rule for every draft: name the resolver or the heading, record a hash or a line number only as “at this measurement”, and do not install a new canonical table.

### Draft — append to `SKILL.md`

```markdown
## Errata — 2026-10-14 freshness re-census (append-only)

The worked example, decision table, checklist items 3–13, anti-patterns, and fossil list above are the 2026-09-28 observation, not the current box. Do not restore those sentences into the present tense.

Measured this pass, not a new pin: `qwen-coder.service` is `not-found` and its unit files are absent; `~/.config/opencode/agents/`, `~/.local/bin/the-janitor`, `~/.config/the-janitor/`, the named `opencode.json.*.bak*` fossils, and `~/.local/bin/llama-server` are absent; `~/.config/opencode/opencode.json` exists and does not contain `8080` or `qwen-local`; ports 8080 and 34113 refused; `docker ps` showed no jitsi container. The surviving loadable pins are the omp builtin default (still in `~/.local/bin/omp`) and the two `$UFO_SRC` rows. Checklist item 1 and the cited-sources tail already say this; the body does not.

`corpus/knowledge/consumer-registry.md:54-55` is not the the-tick / local-helper census. At this measurement those rows were table rows 17–18. Search the table; do not pin the line. The census table has 38 numbered rows, not 37.

Do not pin ufo-fsd-alpha `HEAD`. Resolve `$UFO_SRC` as the probe does. At this measurement that checkout’s HEAD equalled `964f443ee53df0ce06bd689af01f0dea031b01f9`.
```

### Draft — append to `PROVINCE.md`

```markdown
## Errata — 2026-10-14 (append-only)

The owns-table paths `~/.config/systemd/user/qwen-coder.service`, `~/.config/opencode/opencode.json:158`, and `~/.config/opencode/agents/janitor.md:21` are historical examples of the surface, not live artifacts. The unit is `not-found`; the agent file is absent; `opencode.json` no longer carries the 8080 pin. Province is still “local model serving and endpoint health”, detected and reported, never written into `~/.config`, `~/.omp`, or systemd. A contraction of that province, if the serving surface is permanently gone, is an L0 decision (`LOG.md` round-3 carried debt), not a silent edit of this table.
```

### Draft — append to `corpus/knowledge/consumer-registry.md`

```markdown
## Errata — 2026-10-14 freshness re-census, second note (append-only)

The §Errata above still matches a re-measure of deleted paths, the emptied opencode.json, refused ports 8080/34113, and the relocated-tree anchors it names. Do not rewrite the table.

Describe, don’t pin: `HEAD 964f443e` in that errata was the measurement-time checkout, not an identity. Resolve the tree with `$UFO_SRC` (probe order). At this later pass the same checkout still had that commit; a future HEAD does not by itself falsify the anchors until an anchor is re-read and misses.

`config/l1-max-context.yml:19-22` overruns the file (20 lines at that same commit). The context-policy statement is the closing lines of the file (`extendedContext: true` on the last line). Do not re-pin a range.

`~/.local/share/opencode/log/opencode.log` still exists and is 3211 lines. Row 35’s line numbers (3898 and above) are past EOF. The log was not content-read. Do not re-pin lines.

The one-line finding above this file’s first errata is the round-1 present tense. The errata supersedes it.
```

### Draft — append to `corpus/knowledge/alias-endpoint-normalization.md`

```markdown
## Errata — 2026-10-14 freshness re-census (append-only)

The canonical table’s `config.yml:21-44` citations do not resolve. Those lines are not `modelRoles` rows. `modelRoles:` is a later header (measurement-time line 160 of a 492-line file). Do not publish a replacement alias table from this note.

Of the 2026-09-28 keys, these were absent as keys on this pass: `m_kimi`, `m_dsflash`, `m_qwen`, `m_lunamax`, `m_daybreak`, `m_grok46`, `m_astra`, `m_z53`, `m_zflx`, `m_grok47`, `m_kcode`, `m_opus`, `m_opus_h`, `m_sol6`, `m_composer_h`. Several other keys still occur under different line numbers, and at least `m_luna`’s old selector `gpt-5.6-luna:low` is absent while a different luna selector is present. Treat the whole table as superseded historical, not as a line slide.

Loopback result from the earlier errata still holds: no non-secret `127.0.0.1` / `localhost` line, and line 168 has no `8790`. Secret-shaped lines were not copied.

`MISSION.md:37-43` is the axes framework, not the route bucket. The role-class table is `MISSION.md:56-60` at this measurement (no `@m_*`, no endpoint). `kama-round-1.md:7` still contains the round-1 route map (aliases only). `config/l1-max-context.yml` ends at line 20; `:19-22` was already past EOF.

`~/.local/bin/the-janitor` and `distiller.md` are absent. They are not registry obligations. The surviving non-alias local pin in the registry is the omp builtin default.
```

### Draft — append to `corpus/knowledge/cross-lane-scope.md`

```markdown
## Errata — 2026-10-14 (append-only)

Host-state sentences in the present tense (“still target 8080”, “currently at 8080 is Jitsi”, “34113 is the serving endpoint”, “disabled 8080 variant”) are the round-1 observation. Those consumer files and the qwen unit are absent; ports 8080 and 34113 refused; no jitsi container was listed. Ownership rules (kama = endpoint identity, kagi = credentials, kotoba = agent text, kumitate = route mechanism, kengaku = eval, operator = edits) are unchanged.

Round-3 kagi and round-4 kengaku report citations still resolve at the cited lines. They are historical reports, not a live probe. The round-1 “no 8080|34113 in kotoba/kumitate reports” search was not repeated.
```

### Draft — append to `corpus/knowledge/drift-timeline.md`

```markdown
## Errata — 2026-10-14 (append-only)

Every path in the table is a point-in-time source. The opencode backups, `qwen-coder.service` and its archives, `the-janitor`, and the agent files are absent. “Current consumer” in the 2026-09-28 row means current as of that row’s date. Jitsi creation time was not re-checked: no jitsi container is running. Do not rewrite the dated rows.
```

### Draft — append to `corpus/knowledge/endpoint-identity.md` and `snapshot-history.md` and `corpus/lessons/round-2.md`

```markdown
## Errata — 2026-10-14 probe coordinates (append-only)

Do not pin `tools/kama-probe.sh` line numbers. The file at md5 `1f81e859c2d7f43f87d1f7e01327b2cf` still implements normalization, timeouts, schema-unrecognized, userinfo stripping, `eval_rows`, and flock, but the cited ranges no longer contain those statements. At this measurement: `normalize_id` is the basename/`.gguf` function; timeout defaults are the `--timeout` / `--connect-timeout` usage lines; `schema-unrecognized` is the JSON reason arm; userinfo stripping is the credential-strip comment in resolve; `eval_rows` is the function of that name; `GET /v1/models` is the fetch call in the per-port probe. A no-retry claim previously cited at `:253-256` was not re-located — do not invent a line.

`listener-census.md:171` is not the 40961 row; that row is later in §4 (measurement-time `:179`). Census line pins that still match the 2026-09-28 sample are historical sample coordinates, not a live listener map.

`opencode.json:158` does not declare `http://localhost:8080/v1` anymore.
```

### Draft — append to `corpus/lessons/round-1-citations.md`

```markdown
## Errata — 2026-10-14 (append-only)

The round-2 correction (janitor `enabled_providers` at lines 5–7, `loop.sh` moved to `~/archive/bench-arena/loop.sh:5`) was true on 2026-09-29. Both paths are now absent. Deletion, not a repoint, removed them. The round-1 log stays historical.
```

`corpus/README.md` does not need a new deletion note for the three pins it already marks. Optional one-liner, only if parent wants the index to point at the SKILL/PROVINCE gap: those two files still lack the errata the index claims the corpus has.

## Named debt (retain; do not close)

| debt | why it stays open | unblock | owner |
|---|---|---|---|
| Positive controls `ufo-fsd-thetick` and `ufo-fsd-local-helper` read `DEAD` | pins verify `file=yes` at the relocated tree; nothing accepts on 34113 | operator restarts a model unit or retires the surface | operator |
| omp builtin `LLAMA_CPP_BASE_URL \|\| http://127.0.0.1:8080` still in the binary | byte search count 1; registry row `omp-llama-cpp-default` is the right live row; port 8080 is refused, so the class is `DEAD`, not `FOREIGN_SERVICE` | operator sets the env or accepts a dead default; kama does not patch the binary | operator / kumitate (binary), kama reports |
| Province contraction if serving is permanently gone | unit `not-found` is not proof the upstream 34113 pins were retired | L0/fleet decision | L0, not this lane |
| Present-tense dead-path citations in SKILL, PROVINCE, cross-lane-scope, alias table, drift-timeline, endpoint-identity | measured false; original bytes preserved on purpose | parent appends the drafts above | kama parent (integration) |
| `SCORECARD.md:28` “dead-path citations zero outside errata” | falsified by clusters 1, 2, 4, 5 | do not re-pin the score; record the miss when the round log is appended | kama parent |
| Port 631 accepts TCP | connect_ex 0; HTTP class not fingerprinted this seat | do not assert CUPS from the 2026-09-28 census | whoever owns the live listener pass |
| Sibling docs still say Jitsi/34113 are live | citations resolve; claims are theirs | kengaku / kagi / kumitate / aggregator errata, not a kama edit | those lanes |
| `opencode.log` cited lines past EOF | file shorter than the citation | mark historical; do not content-read the log to “fix” lines | kama parent (append only) |
| Probe `:253-256` no-retry citation | old range is the owner loop; new site not found | leave unlocated rather than guess a line | kama parent, docs only |

No debt here is cleared by editing the probe.

## Cross-domain

- **operator** — dead endpoints and deleted unit. Kama still does not write `~/.config`, `~/.omp`, or systemd.
- **kumitate** — relocated tree anchors are live file pins with a dead endpoint; route mechanism stays kumitate’s. Remote URL strings were not re-fetched.
- **kengaku** — `SKILL.md:322-323` and `PROVINCE.md:14` still present the 2026-09-28 server as live. Not absorbed.
- **kagi** — janitor/credential docs still describe the deleted wrapper. Credential lines in `config.yml` were not copied. 8790/8791 refused; they are not a live auth-broker observation.
- **kotoba** — agent files absent; instruction ownership is moot until files exist again.
- **aggregator** — `standing-tables.md:131,243-244` still says D-85 drift persists and both configs pin 8080. Historical fleet note.
- **GateRepair** — no implementation change. Agreed in-seat: hash pin is a docs problem, not `tools/`.

## Axes (advisory only)

| axis | this seat |
|---|---|
| freshness | Re-measured deletion, relocation, alias lines, and probe coordinates against the tree. Did not treat the round-3 errata as self-certifying. |
| operability | Gate still resolves `$UFO_SRC` and fail-closes a bad flag. No second repair. |
| calibration | Separated live anchors, already-marked history, line-drift, and unresolved present tense. Did not call the matching hash “superseded”, and did not call doc drift a probe bug. |
| adjacency | Sibling stale claims named and left with their owners. |

## Parent, after integration (this seat did not run these)

From `kama-shokunin`, full stdout/stderr, exit code, and `git rev-parse HEAD`. Do not re-pin expectations to make a red gate green.

```bash
git rev-parse HEAD
bash tools/kama-probe.sh consumers; echo EXIT:$?
bash tools/kama-probe.sh check; echo EXIT:$?
```

Expect, while 8080 and 34113 stay refused: `consumers` exit 0, three rows, `file_match=yes` on the two `$UFO_SRC` rows; `check` exit 2, `model_ok=0`, `drift=3`. That shape is the carried debt, not a citation repair.
