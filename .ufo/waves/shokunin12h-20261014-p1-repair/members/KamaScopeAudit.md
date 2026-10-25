# KamaScopeAudit — baseline scope audit

Advisory only. Not a native judge verdict, lane-round report, receipt, or admission. No lane files were edited. No build, lint, test, formatter, or `kama-probe.sh` gate was executed. `lsp` is not in this leaf's tool inventory; shell citations were checked by read and line measurement, not a semantic index.

Revision measured: `ea72c3eae4ecc68dab2b0a08153c9c1d2e16df21` (matches `baselines.json`). Worktree porcelain: `?? plans/` only. Probe/registry/self-test digests still match the round-3 SCORECARD pins (`kama-probe.sh` md5 `1f81e859c2d7f43f87d1f7e01327b2cf`, `wc -l` 1092; `test-snapshot.sh` md5 `860f26ac05938cdfc1a8816eff1570b4`; registry md5 `aa033020d99d2e271d2eb0499ab8281f`, 3 data rows).

Axes: freshness, operability, calibration, adjacency.

## What is not a remaining source-root defect

`ufo_src` (`tools/kama-probe.sh:537-551`) and `parse_args` (`:141-143`) implement the documented order: `--ufo-src` if non-empty, else `$UFO_SRC` when it is a directory, else the first existing of `~/Projects/ufo-fsd-alpha` then `~/Projects/origin-work/ufo-fsd-alpha`, else empty → `file=missing`. A non-directory `--ufo-src` dies at parse time (exit 1) and does not fall through. That matches "explicit bad `--src` stays bad."

Measured today: `$UFO_SRC` unset; `~/Projects/ufo-fsd-alpha` exists; `~/Projects/origin-work/ufo-fsd-alpha` absent; `~/Projects/webzites` absent. Checkout HEAD is still `964f443ee53df0ce06bd689af01f0dea031b01f9` ("routing: regenerate omp-seat-routing mirror"). First-existing is unambiguous on this box right now. Do not re-repair the resolver.

Pins that still resolve at the cited lines:

- `config/the-tick.machine.json:16` endpoint `http://127.0.0.1:34113/v1/chat/completions`; `:13` `apiModel`; `:17-18` `parallelSlots` 2 / `contextTokens` 16384. Also `:6` `contextTokensPerRunner` 8192, which the planned context-size move would have to reconcile and which is not a pin defect.
- `scripts/local-helper.mjs:8` `DEFAULT_URL`, `:9` `DEFAULT_MODEL`, `:155-161` credential-free loopback gate, `:312` doc, `:325` call site.
- `tests/the-tick.test.js:61` and `:1457` loopback endpoint; `tests/local-helper.test.js:263-266` 8080 rejection fixtures; `docs/THE-TICK.md:29`; nightcall JSON `:135` and `:144`.
- `.omp/skills/ufo/references/run-logic.md:495` and `.omp/skills/wwkd/SKILL.md:129` still exist and are prose ("endpoint" / "More endpoints"), not URL pins. The round-3 line retarget holds.
- Fleet report citations still resolve: `.ufo/reports/round-3/kagi.md:23-25,69-70` and `.ufo/reports/round-4/kengaku.md:20-23,79`.

`eval_rows` (`:820-821`, `:837`) treats any non-`MODEL_OK` verdict, including `DEAD` on `file=yes`, as drift exit 2. The captured before receipt (`evidence/kama-before.json`) ran `consumers`, not `check`, and recorded `file_match=yes` with `DEAD` on the two `$UFO_SRC` rows. That is ground truth for a dead listener, not a probe defect. Do not change the probe to force `MODEL_OK`.

## Findings

### 1. SKILL still teaches a live 11-row MODEL_OK world — calibration / operability

`SKILL.md` was partly updated and partly left as a current procedure.

Updated and consistent with the tree: cited-sources `:300-311` (3 rows, removed-row list) and `:312-315` (producer marked historical). Checklist item 1 (`:175-184`) expects `registry_rows_evaluated=3 model_ok=0 drift=3 exit=2`.

Still written as current operator procedure, and false against this tree:

- `:33-39` "Worked example — the live drift": six surfaces "still pin 8080"; sample `ss` output shows `llama-server` pid 1299 on 34113 and Jitsi on 8080.
- `:89-96` positive controls "if they ever stop reading `MODEL_OK`, the probe itself is suspect, not the endpoint." Round-3 LOG `:257-260` and SCORECARD `:31-34` already record the opposite: `DEAD` with `file=yes` is ground truth. Following `:95-96` would authorize a false probe repair.
- Checklist items 3-5 and 7-8 (`:193-218`) still pin `34113 MODEL_OK`, `consumer_rows_evaluated=11`, and JSON summary `registry_rows_evaluated:11, model_ok:3, drift:8`, and expect `curl` `/health` → `{"status":"ok"}`.
- Items 11-13 (`:221-223`) tell the operator to read `qwen-coder*.service*` and expect `ActiveState=active`, `MainPID=1299`.
- Decision table `:110-121` and error row `:162` still name live owners (Jitsi container, auth-broker pids 1297/2997, `janitor.md:21`, `distiller.md:7`) as the thing to act on now.
- Anti-pattern 10 (`:264-266`) says `check` evaluates 11 rows against a 37-row census. Cited-sources `:326` still says "37-row census"; SCORECARD says 38. The live registry is 3 rows.

Measured absences (existence/shape only; no secret content read):

- `~/.config/systemd/user/qwen-coder.service` absent; glob `qwen-coder*` empty. `~/.local/bin/llama-server` absent.
- `~/.config/opencode/agents/janitor.md`, `distiller.md`, `~/.config/the-janitor/opencode.json`, `~/.local/bin/the-janitor` absent.
- `~/.config/opencode/opencode.json` exists, 5 lines, 95 bytes. Pattern counts for `qwen-local`, `baseURL`, `8080`, `34113`, `localhost`, `127.0.0.1`, `apiKey`, `token` are all 0. Line `:158` is past EOF. This is citation-to-deleted / past-EOF, not line-drift.

Classification: preserved live claims over a deleted surface. Not a resolver defect. Proposed delta: append a banner at `SKILL.md:33` and at checklist item 3 stating that items 3-8 and 11-13, the worked example, and the positive-control `MODEL_OK` rule are historical as of the 2026-10-14 re-census; the runnable expectation is item 1. Do not rewrite round-1 LOG paragraphs. Owner: parent records (HistoryClaims/RecordPrep). Not GateRepair.

### 2. Province boundary still owns deleted host artifacts — adjacency

`PROVINCE.md:10-11` lists as current concrete artifacts:

- `~/.config/systemd/user/qwen-coder.service` (llama-server, `127.0.0.1:34113`) — absent.
- `~/.config/opencode/opencode.json:158` and `agents/janitor.md:21` — past EOF / absent.

`LEARNING.md:64-71` asks for Core / Frontier / Adjacent. This province has Owns / Refuses / Write boundary / Out of province, and no Frontier. The write boundary (`PROVINCE.md:22-26`) still holds and should not be widened.

`corpus/knowledge/cross-lane-scope.md` has no errata section. It still states, as current:

- `:12-17` OpenCode, janitor, distiller, the-janitor, and `qwen-coder.service:13-22` as live declarations; "Jitsi owns the current 8080 listener."
- `:20` "the endpoint currently at `127.0.0.1:8080` is the Jitsi/Jetty service, while the local `llama-server` is on `127.0.0.1:34113`."
- `:38-41` handoffs to kagi, kengaku, kumitate, and kotoba that say those pins still target 8080.
- `:47` operator line recommending a repoint of `qwen-local` and `the-janitor` from 8080 to 34113.

Those handoffs would send sibling lanes after files that are gone. `consumer-registry.md:30-80` already records the deletion; `cross-lane-scope.md` and `PROVINCE.md` do not point at it. `corpus/README.md:28-32` does, so the index is ahead of the province and the adjacency note.

`LOG.md:262-265` already says a province contraction is an L0 decision, not a lane self-edit. That deferral is correct. Leaving the Owns table and the handoff lines unmarked is still a live false boundary.

Proposed delta: do not self-edit the province into a smaller core this wave. Append an errata pointer on `PROVINCE.md:10` and a dated banner on `cross-lane-scope.md:8` that the host-consumer rows and the `:47` repoint line are historical; surviving loadable pins are the omp binary default and the two `$UFO_SRC` rows. Owner: L0 for any core contraction; parent records for the errata banner. Not GateRepair. Do not absorb kumitate's checkout or kagi's credential surface.

`drift-timeline.md:17` says "Current consumer still pins" inside a dated 2026-09-28 row. The date makes it recoverable as history; the word "Current" does not. Lower severity than the undated handoffs. `listener-census.md:376-382` one-line summary is unmarked and still says the model server is at 34113 with health ok and four other pins on Jitsi. Same class.

### 3. endpoint-identity line citations drifted onto different statements — freshness

`corpus/knowledge/endpoint-identity.md` cites `tools/kama-probe.sh` lines that moved when the file grew (round-1 788 lines → 1092). The behavior those sentences describe is still in the file; the line numbers are not.

| Cited | Claimed | Measured |
|---|---|---|
| `:47-48,83-85` | 2s connect / 5s total timeouts | `:47-48` are persistence comments; `:61-62` are `TIMEOUT=5` / `CONNECT_TIMEOUT=2`; `:83-85` are the cleanup trap; flag defaults are `:107-108` |
| `:386` | `GET /v1/models` | `:386` is `model_matches` "no id found → return 2"; the fetch is `:418` |
| `:80-85,723-733` | `--port` / `--expect` | `:80-85` are `warn`/`die`/`cleanup`; `:723-730` is `resolve_row`'s url/raw case; `--port` handling is `:120-121` and `:738-747` |
| `:481-487` | `schema-unrecognized` | `:481-487` extract served ids and set `runtime=llama.cpp` on the `MODEL_OK` path; `schema-unrecognized` is `:516` |
| `:32-34,338-350` | basename/`.gguf` normalization | `:32-34` are exit-code comments; `:338-350` are inside `served_ids`; `normalize_id` is `:370-371` |
| `:253-256` | one fetch, no retry | `:232-256` is `load_listeners`; the single fetch is `fetch` at `:418` inside `classify` |

The `:481-487` miss is the dangerous one: a repair aimed at the cited lines would edit the match path, not the foreign-service reason. Classification: line-drift, not a logic defect. The ordered classify cases at `:458-524` still implement the table. Proposed delta: append corrected anchors; do not move code to satisfy the old numbers. Owner: parent records. Not GateRepair.

`SKILL.md:93` cites `consumer-registry.md:54-55` as the the-tick / local-helper census rows. Those lines are now the webzites-deletion errata. The re-measured rows are `:106-107`, and they already mark `MODEL_OK` historical. `SKILL.md:101` cites `:49` for the omp builtin; `:49` is the nightcall JSON path. The omp sentence is `:66-67`. Same class: the round-3 errata insertion shifted lines the SKILL still cites. Line-drift, not citation-to-deleted.

`consumer-registry.md:45` groups `the-tick.test.js:125` with the loopback pins. `:125` is `http://192.168.1.1:34113/...`, a non-loopback fixture, not a positive pin. `:61` and `:1457` are the loopback pins. Minor calibration miss inside an otherwise accurate errata.

### 4. Gate inventory does not meet the fleet registry shape — operability

`PROTOCOL.md` Gate standard wants a `SKILL.md` row: name, `gate|probe`, entry command, verdict map onto `clean|failed|could-not-evaluate`, self-test spelling, pinned-value path, write scope, owner. `SKILL.md` has no such row. Usage (`kama-probe.sh:110-111`) declares `0` reconciled, `2` drift, `1` probe error. Under the fleet rule, an undeclared nonzero code reads as `could-not-evaluate`. A closure reader can therefore treat a real drift exit 2 as unevaluable. That is an inventory gap, not a wrong exit in the script.

Two commands are easy to confuse:

- `check` / `snapshot` (`eval_rows:837`): exit 2 when any row is not `MODEL_OK`.
- `consumers` (`:754-755`, `:776`): exit 2 only for `file_match` `no` or `missing`. Endpoint `DEAD` with `file_match=yes` still exits 0. The JSON map at `:770` says so: `"0": "registry text matches every file"`.

The wave before receipt argv is `bash tools/kama-probe.sh consumers`, exit 0, with `DEAD` rows. That receipt does not measure the identity gate. Parent integration must run `check` (and the fixture self-test) and must not read consumers exit 0 as clean.

`tools/test-snapshot.sh` has 24 `ok` sites (14 direct, 2 via `assert_file`, 8 via `assert_contains`) and is hermetic. It does not cover `$UFO_SRC` / `--ufo-src`, the consumers-vs-check exit split, or the omp inherited row. There is no committed `expected.json` pinning input digests for the live `check` gate. The live verdict depends on host listeners; the frozen capability evidence is the fixture script only. No code change required for that gap this wave. Proposed delta: a SKILL registry row mapping `0→clean`, `2→failed`, `1→could-not-evaluate`, entry `bash tools/kama-probe.sh check`, self-test `bash tools/test-snapshot.sh`, write scope `registry/history` for `snapshot` only. Owner: parent records. Not a probe edit.

### 5. omp row cannot falsify its own declared URL — coverage hole, pre-existing

Registry row `omp-llama-cpp-default` uses `grep:LLAMA_CPP_BASE_URL`. `resolve_spec` (`:601`) is `grep -a -oE -m1`. The first binary hit is the bare token, which is not a URL, so the row is `resolver_kind=raw`, `file_match=inherited`, and the endpoint echoed is the registry's declared `http://127.0.0.1:8080`. The before receipt shows exactly that.

A separate `strings -a` measurement (URL fragments only; one credential-shaped hit withheld) still finds `baseUrl: Bun.env.LLAMA_CPP_BASE_URL || "http://127.0.0.1:8080"`. The pin is true. The gate did not derive it. Counterexample: change only the URL literal and leave the token; `consumers` still reports the declared 8080 and `file_match=inherited`. `SKILL.md:163` describes this class for the removed distiller row and does not apply it to the surviving omp row.

This is not a source-root defect and not a reason to repin the row to make a red gate green. If anyone tightens it later, the grep must be a pattern whose first match contains the URL literal; the verdict should stay `DEAD` until something listens. Owner: lane registry, parent-scheduled. Not required to close this re-census.

## Implicit source assumptions (counterexamples, not current failures)

1. Directory existence is identity. `ufo_src` does not check a marker file, HEAD, or remote. If both candidate directories exist, `~/Projects/ufo-fsd-alpha` wins even when it is a stub and `origin-work` holds the pins. Today only the first exists, so this is latent. Header `:532-533` says a miss is never a silently guessed path; the candidate walk is the specified fallback, but a stub directory is accepted as the checkout.
2. `$UFO_SRC` set to a missing path is skipped (`:542` requires `-d`) and the candidate walk runs. A typo'd env does not stay bad; only a non-directory `--ufo-src` flag dies. Documented in usage (`:104-106`), overclaimed by the header.
3. `--ufo-src=` (empty equals-form) leaves `OPT_UFO_SRC` empty, so the `-d` die does not run and resolution falls through. `--ufo-src` with no value does die (`:133`). Narrow counterexample to "explicit empty override stays bad."
4. `--ufo-src` is cwd-relative. The same relative argument differs if the parent runs from the fleet root versus `kama-shokunin/`.
5. A wrong but existing `--ufo-src` (for example `/tmp`) is kept and rows go `file=missing`. That part is the intended fail-closed behavior, not a bug.

No self-test encodes 1-4. Do not change the resolver unless a later run reproduces a wrong root on this box. It does not, on the measurements above.

## Missing coverage

- Context-size reconciliation (`limit.context` / `/props` vs `contextTokens` 16384 and `contextTokensPerRunner` 8192) is already named blocked debt (SCORECARD `:38-41`). Unblock remains an operator listener, not a schema edit against a refused port.
- Invocation cadence: nothing in-repo calls `snapshot`. A transition between calls is invisible. Already stated. Scheduling is operator-owned (`PROVINCE.md` write boundary).
- `listeners` is outside the 3-row gate. A new loopback pin in a file the registry does not name is invisible to `check`. The round-1 census is not a live sweep; this audit did not re-census listeners (that is the live-anchor seat, and the gate was not re-run).
- `consumers`/`check` JSON still emit `resolved_from_file`, `evidence`, and `notes` (`:761-765`, `:829-833`). Snapshot redacts userinfo (`test-snapshot.sh:113-114`; `persist_clean`). A future row whose resolved URL carries userinfo would leak on the non-snapshot commands even though `resolve_spec:609-612` strips userinfo from URL-kind matches. Inherited/raw rows are not stripped. No current registry row has userinfo. Residual, not a live leak.
- `~/.omp/agent/config.yml` was shape-only (492 lines, 26148 bytes). Counts for `127.0.0.1`, `localhost`, `baseURL`, `baseUrl`, `34113`, `8080`, `qwen-local` are 0, which agrees with the errata that row #13 is historical. Line claims `:13-44`, `:24`, and `:168` were not content-checked; the file is credential-bearing. Unverified line anchors, not a contradicted loopback claim.
- `corpus/QUALITY.md` is absent. Corpus contract expects it. Out of the gate-repair slice; discernment has no local bar file to spot-check against.

## Recommendation

No gate-implementation change from this audit. The source-root derivation is already the specified priority, explicit bad `--src` stays bad, and the current checkout is the cited HEAD. The remaining falsifications are claim-boundary errors: SKILL, PROVINCE, and `cross-lane-scope.md` still speak as if the 2026-09-28 drift is live, and `endpoint-identity.md` cites probe lines that now mean something else.

Parent, after integration, should run `bash tools/kama-probe.sh check` and `bash tools/test-snapshot.sh` from `kama-shokunin/`, record full verdict lines and this revision, and not treat the consumers exit-0 receipt as the identity gate. Carry the dead-listener debt as named: operator restores a listener before `MODEL_OK` or context-size reconciliation means anything. Province contraction stays an L0 decision.
