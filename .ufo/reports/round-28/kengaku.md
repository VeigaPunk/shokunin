# Kengaku — round 28

## Work performed

Declared claims: **C1 — legacy novelty → canonical coverage/constructs (lowest7): acquire pinned benchmark task-spec observability. C2 — calibration8: repair and measure bounded literal source-reference coverage.** Both are measured improvements in local observability; scores remain7/8. No scientific-method novelty, runtime benchmark validity or model-performance gain is claimed. Outside non-author closure remains separate.

- Built the read-only WebArena audit:812 task specs,5 evaluator-type sets,27 strata,16 source-audited cases,651 page targets. Source/scorer/helper bytes are pinned; upstream code is never executed. Evidence: `plans/benchmark_spec_audit.py`, `corpus/knowledge/webarena-task-spec-audit.md`, `corpus/evidence/round28-calibration/complete-acceptance/` in the lane.
- Built the frozen13-row/35-path registry diagnostic:12 literal row-file links across2 files, baseline2 mismatched rows→0. S038 was already disclosed; S050 is corrective-reference indexing, not endorsement of its superseded no-match reason. Evidence: `plans/registry_check.py`, `plans/fixtures/r28/registry/population.json`, staged receipts and lesson M65/M67/Q17.
- Curated9 tierA rows S061–S069, including append-only source-location/scope qualifications; reopened S005/S006 for bounded task/test-audit precedent context. Older knowledge corrections are append-only. Evidence: `corpus/SOURCES.md`, `corpus/lessons/round-28.md` Gate and `prior-art-reopen.txt`.
- Independently replayed metrics and attacked contracts with two validated64-seat waves. Build:59 completed/5 provider deaths; falsify:64 completed/0 deaths;128 total unique seats, no replacements. Specs, unchanged dispatch payloads, registries, reports and returned-report pins are under `.ufo/waves/round-28/`.
- Fixed retained-byte identity, raw/effective provenance, scoped parser behavior and missing-control findings. C1/C2 selftests are67/15, exit0. Initial red receipts are retained. A later actual-commit check exposed and repaired a legacy P4 EOF-scope bug using a permanent red1→green0 witness. Evidence: `historical-scope-selftest-{red,green}.txt`, `plans/fixtures/r28/state-check-scope-fix.json`.
- Preserved the previous boundary: P4 still has **48 MATCH,1 SUPERSEDED,2 OFFLINE_UNVERIFIABLE** among51 IDs. Whole historical checker:329 checked,318 MATCH/0 MISMATCH/6 SUPERSEDED/5 offline.29 OOP disclosures comprise26 old+3 round28; they are not newly checked assertions. Evidence: `actual-census-corrected.txt`.

## Landed changes

All lane paths below are relative to `kengaku-shokunin/`; LOG round28 and its appended subsections connect every package to its motivation and evidence.

| Pushed commit | Landed work | LOG evidence |
|---|---|---|
| `f0ba09be0f3066daba2134b943d973ad1588f34a` | Preregistration, immutable task/scorer fixtures and bounded reference population | Round28 opening; `plans/round-28-claims.md` |
| `18b192266389e8d6c74d0e1f1f2db337739e63dd` | Build tools, source openings, build wave and deferred candidate | Round28 build measurements |
| `df33fc83764975fd808b0945097b5d0c7aca3901` | Reviewed v4 entry, index/coverage, source-use links and full wave evidence | Exact reviewed knowledge admission |
| `78e6df8171edf8afbb85e7345aea97f6cb2c7228` | Required plain review marker and root-cause historical-section boundary repair | Actual-commit findings corrected without rerolling history |
| `ed26bdf5d924755697cd6812129be2fa441c42a3` | Corrected measurement pins and final evidence | Corrected measured revision and final evidence |

Final lane tip/remote: **`ed26bdf5d924755697cd6812129be2fa441c42a3`**. Helper state after landing: ahead0/behind0, tracked0/untracked0. Commits used only `jj-lane.sh`; no direct lane Git/jj mutation. The fleet report lands last through the serialized fleet helper.

First admission `df33fc83764975fd808b0945097b5d0c7aca3901` had Gate/census exit1, honestly retained. The Gate defect was an unanchored heading-form PASS; the census defect was historical revision text read through EOF. Neither is relabeled a pass. Corrected measured revision `78e6df8171edf8afbb85e7345aea97f6cb2c7228` has Gate1/1/0 and census exit0, with commit-tree byte proof of the approved entry and reports.

## Before → after measurements

| Claim | Counting command and baseline | Delivered result / measured revision |
|---|---|---|
| C1 | `git cat-file -e b9b24796277020d1b9b01923b45313d6a565e664:plans/benchmark_spec_audit.py` →128, absent/0 dedicated audits. After: `python3 plans/benchmark_spec_audit.py --summary` |812 tasks/812 IDs,5 type sets,27 strata,16 cases,651 targets,0 findings; URL205=196 explicit+9 defaulted. Measured `78e6df8171edf8afbb85e7345aea97f6cb2c7228`; final tip preserves those bytes. |
| C2 | Same delivered checker: `python3 plans/registry_check.py --json --root <export-of-b9b2479>` →exit1,2 mismatched rows/3 findings. Reproducible export and row/cell deltas are in `python3 plans/fixtures/r28/acceptance.py --root . --out <receipt-dir>`. |13 rows/35 paths/12 links,0 mismatched rows, exit0 at `78e6df8171edf8afbb85e7345aea97f6cb2c7228`. Baseline+S050-only stays red onS038; adding onlyS038 status/used-by yields green. S038-only on the original baseline remains red onS050. |

Commands and actual outputs: `corpus/evidence/round28-calibration/actual-census-corrected.txt`, `audit-summary-final.txt`, `registry-summary-final.txt`, `complete-acceptance/commands.json`. Complete acceptance exits0 with11 expected-exit stages, alternate metrics/projections equal, two-way revert counters equal and actual new-entry source links clean. The alternate oracle code is L1-authored, **independent logic, not independent authorship**; fresh wave numeric replays are separately implemented.

Actual timing check: `python3 plans/gate_timing_check.py --lesson corpus/lessons/round-28.md --commit 78e6df8171edf8afbb85e7345aea97f6cb2c7228 --repo .` → admissions1/passed1/failed0. Source-truth/number endorsement comes from returned complete Q10 judgments, not structural presence. Both final reports cover candidate SHA256 `50589759b82b26a7199d157035c852260ab1b10b59815f7b57e7534eccfd2ead`; `actual-final-byte-proof.json` verifies the committed bytes.

No full general-input, semantic-vacuity or exhaustive mutation-coverage claim is made. Stock tests retain disclosed test-only survivor gaps; current implementation passes the independent41 string-schema/43 task-shape probes. No live browser task, hosted-judge call or model trial was run.

## Sources & frontier

Census command, before and end: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kengaku`.

Before, exit0 (tab spacing normalized in the retained start receipt):
```text
kengaku W04 S040 duplicate url arxiv.org/abs/2301.09633 across scopes
kengaku W04 S048 duplicate url aclanthology.org/2020.acl-main.442 across scopes
kengaku W04 S057 duplicate url arxiv.org/abs/2405.11874 across scopes
kengaku W04 S058 duplicate url github.com/UKGovernmentBEIS/inspect_ai/blob/63e45cc52d39b873b944124613da21fdad6f6dcc/src/inspect_ai/scorer/_pattern.py across scopes
kengaku W04 S059 duplicate url www.rfc-editor.org/rfc/rfc8259 across scopes
kengaku ok /home/vgpnk/Projects/shokunin/kengaku-shokunin/corpus/SOURCES.md
exit=0 (whitespace normalized from tab-separated tool rendering)
```
After admission, exit0; source bytes are unchanged by the subsequent scope-only checker repair:
```text
kengaku	W04	S040 duplicate url arxiv.org/abs/2301.09633 across scopes
kengaku	W04	S048 duplicate url aclanthology.org/2020.acl-main.442 across scopes
kengaku	W04	S057 duplicate url arxiv.org/abs/2405.11874 across scopes
kengaku	W04	S058 duplicate url github.com/UKGovernmentBEIS/inspect_ai/blob/63e45cc52d39b873b944124613da21fdad6f6dcc/src/inspect_ai/scorer/_pattern.py across scopes
kengaku	W04	S059 duplicate url www.rfc-editor.org/rfc/rfc8259 across scopes
kengaku	W04	S064 duplicate url spec.commonmark.org/0.31.2 across scopes
kengaku	W04	S065 duplicate url docs.python.org/3/library/json.html across scopes
kengaku	W04	S066 duplicate url doi.org/10.1017/S0950268810000385 across scopes
kengaku	W04	S067 duplicate url doi.org/10.1017/S0950268810000385 across scopes
kengaku	W04	S068 duplicate url raw.githubusercontent.com/web-arena-x/webarena/dce04686a56253aefba7b18a4fa0937cf1dc987b/config_files/test.raw.json across scopes
kengaku	W04	S069 duplicate url raw.githubusercontent.com/web-arena-x/webarena/dce04686a56253aefba7b18a4fa0937cf1dc987b/evaluation_harness/evaluators.py across scopes
kengaku	ok	/home/vgpnk/Projects/shokunin/kengaku-shokunin/corpus/SOURCES.md
exit=0
```

Inventory counting commands and outputs are in `source-inventory-before.json` / `source-inventory-after.json`:60→69 rows, malformed0→0; A54→63/B4→4/C2→2; mined47→57/queued9→8/rejected4→4. Added9 tierA scoped rows, **not9 publications**. S061–S063 are primary artifact files; S064–S069 are scoped extensions/corrections of opened sources.

Touched existing cells: S038 queued→mined and used-by—→its citing knowledge path; S050 used-by gains the corrective-reference path; S005/S006 gain lesson and new-entry use. Admission links for S061/S062/S063/S068/S069 gain the canonical entry. All old→new changes are logged in the lesson; immutable cells are preserved, with S067/S068/S069 superseding errors rather than silently rewriting them.

Frontier: one admitted entry on previously unheld task-spec/scorer ground, knowledge/index35→36. Only the pinned WebArena static surface is partly discharged; named Terminal-Bench/Toolathlon/SWE-bench Pro specs, generated configs, runtime DOM/helper/judge validity and contamination remain open. New rows and the new entry do not enter C2's frozen population. M65 has actual failure-capable same-checker evidence; Q17 is grounded in it. No round27 verifier-spotcheck or operator lesson file matched the recorded input sweep; the operator-provided r27 admission and limitations were carried, not re-adjudicated.

## Trend verdicts

- **expansion: improved** — admitted sourced task-spec entry and demonstrated capability on previously unheld coverage-map ground; source-row growth alone is not the claim.
- **quality: improved** — older source-location/scope errors are explicitly superseded; byte identity and actual frozen-scope regression are repaired, with final gates clean. No admitted false statement is knowingly left unmarked.
- **discernment: unchanged** — Q17 and mistakes are grounded, but this lane's own swarm is author-side. No roster-external admit/reject spot-check for round28 has yet been supplied; outside closure must judge it.

## SHONEN

- [~] Decision tables/error patterns/checklists/citations: `SKILL.md` Task-spec/scorer observability and the new knowledge entry; author assertion only.
- [~] End-to-end domain task executed/logged: LOG round28 → audit, independent replay, staged repair, commit-tree verification and this handoff.
- [~] Executable without oral context: documented CLI/fixture defaults, `complete-acceptance/commands.json`, actual census and Gate commands.
- [~] No cross-domain bleed: PROVINCE round28 partial frontier; `ConnectScope.md`/`FConnector.md`; serving/restoration, general method and web operations remain outside.

No promotion or non-author checklist attestation is claimed.

## Execution boundaries

Wave1 roles: executor3/scout32/reviewer8/critic6/revenger6/mutation-tester3/scribe2/connector2/simplifier2.
Wave2 roles: scout22/revenger14/reviewer12/critic11/mutation-tester4/connector1. L1 held the canonical planner seat. Both waves validated under policy-v2 and each used one unchanged batched taskCall. Wave1's first whole batch was job-cap refused with no spawns; unchanged retry after180s succeeded. Slots acquired/checked/released; no dead seat replaced.

Deaths: ExecBenchmark,ExecOracle,ExecRegistry ended with `[openai-codex/gpt-6-luna] Retry budget exhausted after 5 retries: Codex is at capacity ... turn_rate_limit_exceeded`; DraftKnowledge/DraftMistake ended Haiku429 `rate_limit_error`, retry-after-ms3194000. Exact retained errors: `build-dead-seats.json`. L1 wrote their missing deliverables with actual writer identity. Role routing was host-bound; no model parameter or availability/failover claim was made.

Tools: L1 installed/updated none; seats reported no installs. No pacman/system upgrade/service changes. Disposable browser profile and unused writer clones were removed; analytical evidence is retained. Fleet misroot sweep found no kengaku-r28 file; a foreign kagi ScribeLesson was routed to KagiR26, who relocated it. Runtime/fleet-owned files were untouched.

Stale-lane: progressing, one round28 claim/attempt1; no successor round started. No MANIFEST edit or independent closure was performed by this lane.

L0: no new question. Inherited unruled questions remain `kengaku | round-25 | Coverage cap (re-filed...)` and `kengaku | round-25 | Novelty verdict conversion (re-filed...)`; conservative scores/cap remain held. No answer was required to finish this round.
