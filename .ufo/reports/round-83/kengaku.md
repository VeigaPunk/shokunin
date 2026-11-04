# kengaku round 83 — report

2026-11-04, hyaku run15, attempt1; L1 KengakuR83. Lane final **ca1deea2f36150402659585d9957de5e84f9d111**; `git ls-remote origin refs/heads/master` printed the same hash before filing. Unless identified as fleet, paths below are relative to `kengaku-shokunin/`.

## Work performed

Declared **R83-C1 / coverage**: first located, reproducible offline replay of base-unattempted `code-from-image`; **R83-C2 / calibration**: repair eight round82 outside self-assessment/record mismatches with substantive, base-sensitive checks. Frozen at `6f076679931367d540c3897a4eafa0eca752e1d4`, base `614f00559c75155ec100e945b3e8257b14fb7496` (`plans/round-83-claims.md`). Coverage is lowest non-retired (7, L0 cap); calibration stays 10. Both frozen counters verify; separate outside admission remains the integrator's decision.

- Executed the actual captured grader inside fresh bubblewrap sandboxes: eight real-file end states, two independently called functions, sixteen matching legs, zero mismatches. Source/table/tool/host/tip pins and exact reconstructed argv bind the receipt. This is grader acceptance coverage, **not** image understanding, implementing pseudocode, running a model or a new grader class (`corpus/evidence/round83/mint-run.txt`, `code-from-image-probe.txt`; `plans/round83_code_image_probe.py`).
- Implemented C1 revision-isolated reproduction and C2 fixed-universe debt checks; actual controls, selftests, attributed mutants and eight base failures were exercised (`plans/round83_c1_replay.py`, `round83_c2_debt.py`, `round83_c2_checks.py`; `corpus/evidence/round83/*selftest.txt`, `*mutants.txt`, `c2-sensitivity.txt`).
- Corrected quote counts, retained the historical census, distinguished six affected seats from final output categories, fixed commit attribution/index shape/Gate omissions/selftest quantifier/timezone labels. Eight source/repair-bound rows and dated corrections leave historical records intact (`corpus/lessons/round-83.md:27-59`, `corpus/routed-findings.jsonl`, `r82-census-after.txt`, `r82-seat-census.json`, `r82-report-preservation.txt`).
- Opened S267–S270, admitted one new sourced knowledge entry and mined repeated annotation mistakes into Q60 with actual red/green witnesses (`corpus/SOURCES.md`, `corpus/knowledge/tb2-code-from-image-offline.md`, `corpus/QUALITY.md` Q60; `q60-red-green.txt`).
- Integrated wave attacks: forged census/Gate and contradictory count-text false greens were retained and addressed; reviewer/sentinel's freeze-printer finding was addressed with real gate control receipts. No absent-code review was represented as validation (`.ufo/waves/round-83/w1/{CriticR83,MutationR83,ReviewerR83,SentinelR83}/report.txt`; integrated C2 battery has 20 cases and 19 mutants).
- Resolved an actual downstream vocabulary mismatch without changing the frozen observation label or old gate: append the **actual already-observed C1 admission counter stdout**, command/revision/exit as a distinct receipt trailer. The original probe block remains byte-identical. Red population receipt at 0c56b4eb and green at 5beac9c4 are both retained (M83-1; `population-after.txt`, `population-final.txt`, `preservation.json`).

## Landed changes

All rows tie to `LOG.md` round83, lines3218–3231.

| carrying commit | landed change / LOG evidence |
|---|---|
| `6f076679931367d540c3897a4eafa0eca752e1d4` | Frozen claims, case table, initial absence/anti-vacuity preview and before census; LOG:3220. |
| `ddb903a876648d4f2471345cb20c61959502c3c1` | Four instruments, registry rows, S267–S270, knowledge/lesson/QUALITY/index and substantive historical repair receipts; LOG:3221–3224. |
| `0c56b4eb44536a468473b1b5ffb45444ea2a6288` | First clean replay receipt, executed ledger row, derived file-artifact 19/76 cell and exercised batteries/controls; LOG:3225–3227. |
| `5beac9c43fe6bbe3b29652dabc888dfabeeb8b6c` | Actual admission-output trailer, preserved population red leg, lesson limits and coverage/province updates; LOG:3228–3229. |
| `ca1deea2f36150402659585d9957de5e84f9d111` | Final SCORECARD/registry boundary/LOG, measured green receipts, preservation evidence and settled twelve-seat wave; LOG:3230–3231. |

## Before → after measurements

Measurements use committed bytes; current instrument ddb903a8 grades the frozen BASE for before, and **5beac9c43fe6bbe3b29652dabc888dfabeeb8b6c** for final after. Final landing adds records/wave evidence and a historical-sweep boundary note, not changed grader/table/ledger/repair predicates.

| claim | counting command (lane cwd) | observed before → after |
|---|---|---|
| R83-C1 | `python3 plans/round83_c1_replay.py --lane . --rev REV --work DIR` | BASE: `located=0 executed=0 defects=34`, exit1 → 5beac9c4: `TARGET members=1 cases=8 legs=16 mismatches=0 located=1 executed=1 defects=0`, `PREDICATE R83-C1 pass`, exit0 (`c1-before.txt`, `c1-final.txt`). Coverage **7→7 held**, member coverage improves. |
| R83-C2 | `R83_FLEET_REPO=/home/vgpnk/Projects/shokunin python3 plans/round83_c2_debt.py --lane . --rev REV --work DIR` | BASE: `ids=8 closed=0 checks_passed=0 indexed=no defects=9`, exit1 → 5beac9c4: `TARGET ids=8 closed=8 checks_passed=8 indexed=yes defects=0`, pass, exit0 (`c2-before.txt`, `c2-final-tip.txt`). Calibration **10→10 held**, eight actual mismatches discharged. |

- C1 selftest **29 cases / 28 red / 0 failures**, mutants **15/15**; real do-nothing, ledger-only and fabricated-observation controls all `target_reached=False` (`c1-selftest.txt`, `c1-mutants.txt`, `c1-control-*.txt`). The preview `freeze-controls.txt` does **not** substitute for counter rejection. Integrated controls ran before the L1's production mint; seats' static/fixture/independent reference probes are separately labelled.
- C2 selftest **20/19/0**, mutants **19/19**, presence-only control loses; `--sensitivity` gives **failed_at_base=8**, exit0. Checks' own self-invocation also exercises 20/19/0; probe selftest **6/0** (`c2-selftest.txt`, `c2-mutants.txt`, `c2-control-presence.txt`, `c2-sensitivity.txt`, `checks-selftest.txt`, `probe-selftest.txt`).
- Q60: changing only S268's count 4→6 or deleting only S266's Gate row makes the corresponding actual check exit1; pristine/restored states exit0 (`q60-red-green.txt`).
- Bounded integration: standing population **27 replayed/located, 61 unexecuted, defects=0**; index parity **knowledge77/77, lessons139/139, evidence dirs74/74**, exit0 (`population-final.txt`, `index-final.txt`). All 258 old source rows and named historical gate/source bytes are preserved (`preservation.json`). C2 already passed at ddb903a8 before C1 receipt/ledger landing (`c2-after.txt`); C1 does not consume C2 correction records.
- Remaining scores held: novelty8 (canonical coverage/construct mapping), depth10, operability10, freshness10, adjacency9. No new model/method, serving-plane or route authority claim. The prior 26-member sweep is explicitly historical, **not** advertised as a current 27-member sweep; R82-F1 and old divergences remain backlog, not repairs claimed here.

## Sources & frontier

Registry **258→262 rows**; A/B/C **228/24/6→232/24/6**; mined/rejected/queued **235/15/8→238/16/8**. Added **A4/B0/C0**: S267 grader, S268 supersedes S262 (4 tokens), S269 supersedes S263 (2), S270 rejected supersedes S264 (HTTP404, reason+flip). Existing rows touched old→new: **none** (258/258 byte-identical); no status/recheck/used-by changes. New used-by paths resolve. The lesson Gate re-opens and enumerates missing S265/S266 provenance without altering their rows.

Row-count command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh census --root /home/vgpnk/Projects/shokunin kengaku` → rows262, A232/B24/C6, mined238/queued8/rejected16, exit0 at the final lane tree. Before: the same census implementation's `census --file <pinned SOURCES.md>` output at historical a44b2f08 is retained in `.ufo/waves/round-83/w1/HistoryReceiptR83/r82-registry-totals.txt` (rows258, A228/B24/C6, mined235/queued8/rejected15, exit0); those source bytes are identical at BASE614f0055. L1 also directly parsed BASE/current rows with the contract's 0–3-space row prefix, eleven cells and tier/status histograms. The independent final index receipt supplies the knowledge/lesson/evidence counts above.

Frontier advanced: one previously unattempted file-artifact **member**, not a class; new admitted knowledge cites mined S267 and the new `corpus/README.md` coverage-map bullet. `PROVINCE.md:1132-1136` keeps image solving outside performed work. The rejected instruction-as-solving **scope** does not reject the instruction's task-spec authority. S270 is the retained source-locator reject, with an explicit reachable-pinned-file flip; unreachable is not fabrication.

**Assimilation: none.** Latest `considerthese/2026-10-26.md` proposal2 remains unimplemented; a per-member probe is not its standing all-five admission counter. Proposal1 burn-down was already held. The older planned sweep-divergence/parser work was not covertly declared as another claim.

Required census command, before and after, full retained outputs and exit codes:

```text
COMMAND /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kengaku
REV 614f00559c75155ec100e945b3e8257b14fb7496
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
kengaku	W04	S071 duplicate url docs.python.org/3/library/json.html across scopes
kengaku	W04	S075 duplicate url docs.python.org/3/library/json.html across scopes
kengaku	W04	S076 duplicate url docs.python.org/3/library/json.html across scopes
kengaku	W04	S100 duplicate url github.com/laude-institute/terminal-bench-2 across scopes
kengaku	W04	S213 duplicate url raw.githubusercontent.com/harbor-framework/terminal-bench-2/2fd12b88aafdd04a52c298e3940bcb189f9766d6/chess-best-move/tests/test_outputs.py across scopes
kengaku	W04	S214 duplicate url raw.githubusercontent.com/harbor-framework/terminal-bench-2/2fd12b88aafdd04a52c298e3940bcb189f9766d6/configure-git-webserver/tests/test_outputs.py across scopes
kengaku	W04	S215 duplicate url raw.githubusercontent.com/harbor-framework/terminal-bench-2/2fd12b88aafdd04a52c298e3940bcb189f9766d6/configure-git-webserver/tests/verify.sh across scopes
kengaku	W04	S216 duplicate url raw.githubusercontent.com/harbor-framework/terminal-bench-2/2fd12b88aafdd04a52c298e3940bcb189f9766d6/configure-git-webserver/instruction.md across scopes
kengaku	W04	S217 duplicate url raw.githubusercontent.com/harbor-framework/terminal-bench-2/2fd12b88aafdd04a52c298e3940bcb189f9766d6/feal-linear-cryptanalysis/environment/task-deps/gen.py across scopes
kengaku	W04	S222 duplicate url raw.githubusercontent.com/harbor-framework/terminal-bench-2/2fd12b88aafdd04a52c298e3940bcb189f9766d6/openssl-selfsigned-cert/instruction.md across scopes
kengaku	W04	S227 duplicate url encoding.spec.whatwg.org/index-windows-1252.txt across scopes
kengaku	W04	S234 duplicate url raw.githubusercontent.com/harbor-framework/terminal-bench-2/2fd12b88aafdd04a52c298e3940bcb189f9766d6/kv-store-grpc/tests/test_outputs.py across scopes
kengaku	W04	S237 duplicate url raw.githubusercontent.com/harbor-framework/terminal-bench-2/2fd12b88aafdd04a52c298e3940bcb189f9766d6/kv-store-grpc/tests/test_outputs.py across scopes
kengaku	W04	S243 duplicate url raw.githubusercontent.com/harbor-framework/terminal-bench-2/2fd12b88aafdd04a52c298e3940bcb189f9766d6/nginx-request-logging/tests/test_outputs.py across scopes
kengaku	W04	S256 duplicate url raw.githubusercontent.com/harbor-framework/terminal-bench-2/2fd12b88aafdd04a52c298e3940bcb189f9766d6/README.md across scopes
kengaku	W04	S266 duplicate url raw.githubusercontent.com/harbor-framework/terminal-bench-2/2fd12b88aafdd04a52c298e3940bcb189f9766d6/log-summary-date-ranges/instruction.md across scopes
kengaku	ok	/home/vgpnk/Projects/shokunin/kengaku-shokunin/corpus/SOURCES.md
EXIT 0
```

```text
COMMAND /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kengaku
REV 5beac9c43fe6bbe3b29652dabc888dfabeeb8b6c
SOURCES_SHA e1a6ff5ae828ea745eef64b93503de6ef7757893c4957e2a69242cebec85c80d
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
kengaku	W04	S071 duplicate url docs.python.org/3/library/json.html across scopes
kengaku	W04	S075 duplicate url docs.python.org/3/library/json.html across scopes
kengaku	W04	S076 duplicate url docs.python.org/3/library/json.html across scopes
kengaku	W04	S100 duplicate url github.com/laude-institute/terminal-bench-2 across scopes
kengaku	W04	S213 duplicate url raw.githubusercontent.com/harbor-framework/terminal-bench-2/2fd12b88aafdd04a52c298e3940bcb189f9766d6/chess-best-move/tests/test_outputs.py across scopes
kengaku	W04	S214 duplicate url raw.githubusercontent.com/harbor-framework/terminal-bench-2/2fd12b88aafdd04a52c298e3940bcb189f9766d6/configure-git-webserver/tests/test_outputs.py across scopes
kengaku	W04	S215 duplicate url raw.githubusercontent.com/harbor-framework/terminal-bench-2/2fd12b88aafdd04a52c298e3940bcb189f9766d6/configure-git-webserver/tests/verify.sh across scopes
kengaku	W04	S216 duplicate url raw.githubusercontent.com/harbor-framework/terminal-bench-2/2fd12b88aafdd04a52c298e3940bcb189f9766d6/configure-git-webserver/instruction.md across scopes
kengaku	W04	S217 duplicate url raw.githubusercontent.com/harbor-framework/terminal-bench-2/2fd12b88aafdd04a52c298e3940bcb189f9766d6/feal-linear-cryptanalysis/environment/task-deps/gen.py across scopes
kengaku	W04	S222 duplicate url raw.githubusercontent.com/harbor-framework/terminal-bench-2/2fd12b88aafdd04a52c298e3940bcb189f9766d6/openssl-selfsigned-cert/instruction.md across scopes
kengaku	W04	S227 duplicate url encoding.spec.whatwg.org/index-windows-1252.txt across scopes
kengaku	W04	S234 duplicate url raw.githubusercontent.com/harbor-framework/terminal-bench-2/2fd12b88aafdd04a52c298e3940bcb189f9766d6/kv-store-grpc/tests/test_outputs.py across scopes
kengaku	W04	S237 duplicate url raw.githubusercontent.com/harbor-framework/terminal-bench-2/2fd12b88aafdd04a52c298e3940bcb189f9766d6/kv-store-grpc/tests/test_outputs.py across scopes
kengaku	W04	S243 duplicate url raw.githubusercontent.com/harbor-framework/terminal-bench-2/2fd12b88aafdd04a52c298e3940bcb189f9766d6/nginx-request-logging/tests/test_outputs.py across scopes
kengaku	W04	S256 duplicate url raw.githubusercontent.com/harbor-framework/terminal-bench-2/2fd12b88aafdd04a52c298e3940bcb189f9766d6/README.md across scopes
kengaku	W04	S266 duplicate url raw.githubusercontent.com/harbor-framework/terminal-bench-2/2fd12b88aafdd04a52c298e3940bcb189f9766d6/log-summary-date-ranges/instruction.md across scopes
kengaku	W04	S268 duplicate url raw.githubusercontent.com/harbor-framework/terminal-bench-2/2fd12b88aafdd04a52c298e3940bcb189f9766d6/log-summary-date-ranges/tests/test.sh across scopes
kengaku	W04	S269 duplicate url raw.githubusercontent.com/harbor-framework/terminal-bench-2/2fd12b88aafdd04a52c298e3940bcb189f9766d6/nginx-request-logging/tests/test.sh across scopes
kengaku	W04	S270 duplicate url raw.githubusercontent.com/harbor-framework/terminal-bench-2/2fd12b88aafdd04a52c298e3940bcb189f9766d6/pyproject.toml across scopes
kengaku	ok	/home/vgpnk/Projects/shokunin/kengaku-shokunin/corpus/SOURCES.md
EXIT 0
```

Both exit0. W04 **27→30**: three added same-URL/different-scope supersede warnings, not suppressed errors. Historical round82 after really had 27 (not its report's 26); the exact old-tip rerun is separate `r82-census-after.txt`. Gate access dates, URLs and ≤25-word located quotes for every new row are in `corpus/lessons/round-83.md` Gate. No outside spot-check of this round's admit/reject is self-awarded.

## Trend verdicts

- **expansion: improved** — one newly executed member, new sourced knowledge on named coverage-map ground and demonstrated `tb2-code-from-image-replay` capability (SCORECARD round83; C1 receipt). No new class or model ability credit.
- **quality: improved** — eight substantive historical repairs, immutable supersede corrections and executable rejection/sensitivity witnesses; the population interface red leg is retained and repaired with genuine admission output, not hidden. Historical sweep limitations are marked, not left as current claims.
- **discernment: improved** — round82 outside V1/V6 disagreement becomes Q60 plus failable count/Gate witnesses; current admits/rejects remain for the separate outside closure. Dispatched seats are author-side, not independent verification.

## SHONEN

- [~] Decision tables/error patterns/checklists with cited sources — `SKILL.md`, S267 and the registered round83 instruments; the old seven-of-ten selftest overclaim is corrected, not repeated.
- [~] End-to-end domain work executed and logged — actual offline captured-grader replay, `mint-run.txt`, `code-from-image-probe.txt`, `LOG.md:3225-3230`; not image-task solving.
- [~] Instructions executable without oral context — knowledge entry, frozen claims, exact commands, green `index-final.txt`; C2 fleet-repo dependency explicit.
- [~] No cross-domain bleed — `PROVINCE.md:1132-1136`, connector report; serving/route/image/model capability exclusions retained.

No `[x]`; named independent promotion verifier not supplied by this lane.

## Round shape and closeout

ONE validated v1 wave, **12 seats**, band8–16, maxLanes12. Executor4, scribe2, scout1, connector1, reviewer1, critic1, mutation-tester1, sentinel1. Attack share **3/12=25%** (campaign list; sentinel not counted), connector1≤2. L1 holds planner per validator ruling; bounded planner walk via SourceScoutR83. No residual calls, duplicates or replacements; total12. Main's **WAVE-DONE** arrived before report filing; `w1-results.json` has 12 nonempty JSON-object outputs, no dead note (no outer status fields), so **0 dead seats reported**. `.ufo/waves/round-83/wave-summary.json` retains accounting and handoff. Host table routed every role through @m_zfl at observation; no model override or unsupported actual-answering-model claim.

Inherited lane state: initial helper state tracked0/untracked0, no inherited round83 work to discard. Fleet misroot sweep found no identified kengaku-round83 output; unrelated `.scratch/`/root artifacts were left untouched. No tool installs/updates. Scratch `/fast/scratch/hyaku/kengaku-r83` removed after lane landing; evidence is committed, not scratch-dependent.

Stale-lane: launch digest `2026-11-04T12:42:07-03:00 launch kengaku round=83 pgid=80529 driver=hyaku-inline attempt=1`. At 18:19:45Z its age was 2h37m38s (>two450s ticks), **progressing**, with own landed commits through ca1deea2f36150402659585d9957de5e84f9d111, not silent. This assignment opened no second lane mission.

L0: none newly filed. Existing coverage-cap/retired-surface questions (kengaku round25/33/51) and earlier admission/provenance questions remain operator-owned and are not treated as answered. No new claim depends on resolving them. Separate outside closure/admission remains pending; final pushed lane hash is ca1deea2f36150402659585d9957de5e84f9d111.
