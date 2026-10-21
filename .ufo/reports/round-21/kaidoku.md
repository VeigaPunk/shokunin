# Kaidoku round 21 — record-bound evidence and bounded observations

## Work performed

Declared **R21-C1/calibration** (tied-lowest finite proxy): bind the cited exact Evidence id and operation in the same supported record without a typed refusal, and replace C1's dependence on a C3 receipt with an isolated inert control. Declared **R21-C2/depth**: distinguish missing/malformed observation from bounded silence and preserve kind/index semantics. Both are **improved in the frozen finite measurements**; independent admission and current-round outside admit/reject sampling remain pending. R20 is admitted and was not redone.

- Baseline B=`2dd430cb6bcad60ff4db720c052074f1f75eecbc`; declaration `f4e95af909d692156e984bf2049e1c7fb4a2a836`; independent contract `53166ab0aae495c964d956050ca0ca3a4f29014a`; concrete fixtures `d93c85887d9ae77d224c82c8f56bc8cca86d1a75`. All freezes precede measurements (`.ufo/waves/round-21/claims.json`, `fixture-contract.json`, `fixtures/battery.json`).
- Record parser rejects cross-record/prose association, typed refusal envelopes and duplicate members. Unsupported representations are unevaluable, not guessed. Current registry callers use the successor; old R20 tools remain historical authorities. Evidence: `SKILL.md`, `corpus/QUALITY.md` #26/28, `verify/final-fixed/after-C1.json`.
- Comparator requires an explicit bounded envelope and typed failure members; null means absence through `last_line`, never analyzer success. Evidence: QUALITY #27, `verify/final-fixed/after-C2.json`; all nineteen old pairs are retrospective compatibility, not new forecasts.
- Source frontier and mistakes: reopened S049/S050; mined outside R20-EVIDENCE/R20-SEP into sourced criteria and paired negative/positive controls. Evidence: `corpus/lessons/round-21.md`, `verify/frozen-input-red.json`.
- Recovery reused the frozen declaration/spec/fixture contract and inherited source/lesson drafts only after rereading them and reopening sources. The inherited dispatch registration proves **zero spawned seats**, not a completed wave. No output from the unused external `kaidoku-r21-{coverage,compare,battery}` worktrees is credited. No operator/aggregator-owned lane artifact was modified.
- One W1 report was misrooted in the fleet: `ScoutCatalogBytes.md`. Required fleet `git status --porcelain` found the untracked round tree; `cp` → `cmp` → removal of only the seat-authored fleet copy exited0. Exact report bytes are in lane `w1/ScoutCatalogBytes.md`; lesson Mistakes records it.

No REA producer, analyzed native carrier, private HOME/config/account/provider probe or host package/service/boot mutation was run by the coordinator. No tools were installed or updated. Stale-lane: respawn-per-round replacement for the same already-held kaidoku21 claim; no other kaidoku mission is open and no next round was started.

## Landed changes

All work is tied to `LOG.md` round-21 and its measured continuation; the initial measured source is V=`a75c3c67e4e658a232e1842ab1aceb383b711269`; final corrected source is F=`2f351728f961f3a9a4f53cd1706ad594bf5b5f9a`.

| Change | Pushed lane commit | LOG/evidence |
|---|---|---|
| Frozen declaration | `f4e95af909d692156e984bf2049e1c7fb4a2a836` | LOG round21 declaration; claims.json |
| Independent case contract and concrete fixtures | `53166ab0aae495c964d956050ca0ca3a4f29014a`, `d93c85887d9ae77d224c82c8f56bc8cca86d1a75` | LOG frozen-contract bullet |
| Parser/comparator, isolated receipt control, sources, criteria, skill/index updates | `fe11e4df2803ac205ecc1c1023b9796075b4d7dc` | LOG C1/C2/frontier bullets; lesson Gate |
| Frozen-authority binding, controls, W1 evidence and verification producer | `88718ca7fa39f8f7a2b7e184ad3aa1b9be20b92a`, `a75c3c67e4e658a232e1842ab1aceb383b711269` | LOG recovery/integration; battery.py, verify.py |
| Measured records and claim verdicts | `e8df81801805336dbefd33b0001a2d4dd661f498` | LOG measured continuation; verify/*.json; SCORECARD measured records |
| Post-wave independent template and complete v2 freeze | `174948f0e6052ec90a0c51f14516ded210b99273`, `ae73ec7734c8edc70350995267ddc1f0d2f603e4` | LOG post-wave integration and failed-positive continuation; both fixture versions retained |
| Adopt W2 independence criticism, preserve real red, complete metadata | `93c931a205e2e52b2a4257e9f895a175ea5f0727`, `2f351728f961f3a9a4f53cd1706ad594bf5b5f9a` | LOG post-wave and failed-positive entries; QUALITY28; `verify/final/`14/16 retained |
| Complete final measurements and round evidence | `7787fea4d6fd718726de92ed20759d11ce7b8b48` | LOG final corrected demonstration; SCORECARD delivered correction; `verify/final-fixed/summary.json`16/16 |

Final lane delivery state: helper printed `landed 7787fea4d6fd718726de92ed20759d11ce7b8b48`; subsequent `jj-lane.sh state "$L"` printed `branch=main local=7787fea4d6fd718726de92ed20759d11ce7b8b48 remote=7787fea4d6fd718726de92ed20759d11ce7b8b48 ahead=0 behind=0 head=detached tracked=0 untracked=0`. No unrelated lane debt was swept.

**Correction history is not erased:** W2's connector found the initial control called the validator's `_carrier_receipt`. A separately authored v1 template was then actually tested and rejected for missing `python`/`orig_argv` (14/16 expected checks at `93c931a2`, `verify/final/summary.json`). Complete v2 was independently frozen before the final demonstration; the control now imports no validator/builder and records template, validator and pins digests. Final no-C3 positive0/decoy1 succeeds; an altered v2 template returns2 `snapshot_tampered`. The old invalid-revision exception leak is also retained red1→fixed2 as a supplementary compatibility case, never added to the frozen12-case denominator.

## Before → after measurements

Measured at B and final F=`2f351728f961f3a9a4f53cd1706ad594bf5b5f9a`; scores remain10.0→10.0 (delta0), finite structural proxies, not domain mastery. Claim-specific commands load only their own changed predicate. `--claim C1 --regression` is explicitly refused; the separate isolated receipt control runs in a scratch root with no C3 files.

```sh
L=/home/vgpnk/Projects/shokunin/kaidoku-shokunin
B=2dd430cb6bcad60ff4db720c052074f1f75eecbc
V=2f351728f961f3a9a4f53cd1706ad594bf5b5f9a
python3 -I -B "$L/.ufo/waves/round-21/battery.py" --root "$L" --rev "$B" --claim C1
python3 -I -B "$L/.ufo/waves/round-21/battery.py" --root "$L" --rev "$V" --claim C1
python3 -I -B "$L/.ufo/waves/round-21/battery.py" --root "$L" --rev "$B" --claim C2
python3 -I -B "$L/.ufo/waves/round-21/battery.py" --root "$L" --rev "$V" --claim C2 --regression
```

| Claim | B → V | Actual exits / evidence |
|---|---|---|
| R21-C1 calibration | Expected decisions3/12→12/12; false-clean9→0; crashes0→0; all positive controls preserved | 1→0; `verify/final-fixed/before-C1.json`, `after-C1.json`; independent positive0/decoy1 at `isolated-without-C3.json` |
| R21-C2 depth | Expected decisions14/20→20/20; false-clean5→0; undeclared KeyError1→0 | 1→0; `verify/final-fixed/before-C2.json`, `after-C2.json`; nineteen retained R20-C3 pairs19/19 match with equal bound-log SHA-256 |

`verify.py --root "$L" --before "$B" --after "$V" --out-dir "$L/.ufo/waves/round-21/verify/final-fixed"` exited0 with16/16 expected child exits (`verify/final-fixed/summary.json`). Four self-invocation selftests returned0 with stable finding IDs. A copied fixture changed to `{}` made the same battery exit2 `snapshot_tampered` (`verify/final-fixed/frozen-input-red.json`). The two fixed Git freeze revisions—not a mutable expected manifest alone—select canonical contract/fixture bytes.

No-harm command: `python3 -I -B "$L/.ufo/waves/round-21/controls.py" --root "$L" --before "$B" --after "$V"`, exit0. It counted1134 prior R20/knowledge/lesson files with zero byte changes; LOG/SCORECARD prefixes preserved; prior25 admission rows identical and three added; coverage map102/102 and citation proxy17/17 unchanged (`verify/final-fixed/no-harm.json`). `tools/verb-coverage.py --root "$L" --rev "$V"` exited0, mentions133/153 and all five historical targets retained with exact-record witnesses (`verify/final-fixed/verb-coverage.json`), including pathless objdump and synthetic Harmony limits. No general Evidence authentication, temporal continuity, analyzer repair or broad semantic no-harm claim follows.

## Sources & frontier

SOURCES **48→50**, tier A42→44/B5→5/C1→1, mined46→48/rejected2→2. Added S049 (RFC8259 §4, primary JSON member interoperability) and S050 (Python3.15 JSON decoder duplicate-name policy), both opened/reopened2026-10-21 and mined by `corpus/lessons/round-21.md` Gate. The lesson holds the URL/access date/located ≤25-word contiguous quotes; both support R21-C1, not cryptographic Evidence authenticity.

Counting command (re-executes the exact retained producer):
```sh
python3 -I -B -c 'import json,subprocess; d=json.load(open(".ufo/waves/round-21/verify/final-fixed/source-rows.json")); raise SystemExit(subprocess.run(d["argv"]).returncode)'
```
Observed exit0 and the above B/V histograms are retained in that JSON. `verify/final-fixed/source-integrity.json` retains its separate exact argv, exit0: old48 rows byte-identical; added `[S049,S050]`. **Old→new touches: none**; no existing status/recheck/used-by cell changed. Frontier ground advanced: none. No new knowledge entry or capability row; row growth alone is not expansion. Known lint/sandbox, timestamp exclusions, DATED census/guard bypasses, source-anchor/rendering and adjacency debts remain named in lesson Residual dispositions.

Census command at recovery start and end (both actually run; initial inherited S049/S050 drafts were already present):
```sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kaidoku
```
Both outputs and exit codes (`start-census.json`, `verify/final-fixed/sources-census.json`):
```text
kaidoku W04 S033 duplicate url github.com/NationalSecurityAgency/ghidra/pull/9348 across scopes
kaidoku W04 S047 duplicate url go.dev/dl/?mode=json&include=all`, across scopes
kaidoku ok /home/vgpnk/Projects/shokunin/kaidoku-shokunin/corpus/SOURCES.md
exit=0
```
Original round-start48 is independently retained in the preexisting claims.json and re-counted from B. Mistakes mined: vacuous token association, vacuous unbounded silence, C1/C3 fixture scope coupling and the observed scout misroot. Actual red-before results and an altered-input red prove the relevant new criteria can fail; location repair does not claim runtime enforcement. Corpus conformance is supported for these exercised rules; a full historical semantic corpus audit and outside current-round spot-check were not performed.

## Trend verdicts

- **expansion — unchanged:** knowledge102 and province frontier unchanged; two source rows are not new domain holdings.
- **quality — improved, bounded:** typed record/observation successors remove the frozen false-clean/crash paths while retaining positives and19 retrospective matches; structural no-harm remains clean. Evidence: `verify/final-fixed/summary.json`, `after-C1.json`, `after-C2.json`, `no-harm.json`.
- **discernment — improved via outside-routed learning:** the R20 outside verifier's R20-EVIDENCE/R20-SEP disagreements became mistake-backed QUALITY26–28 and exercised negative/positive controls (`corpus/lessons/round-21.md`). Current-round outside admit/reject agreement remains pending; every dispatched seat is author-side, not a non-author verifier.

## SHONEN

- [~] Real decision tables/error patterns/checklists/citations — `SKILL.md` round21 decision table and registry, historical craft proxy17/17; no named non-author promotion verifier.
- [~] End-to-end domain task — historical2026-10-15 native recipe in `SHONEN.md`/`evidence/round-1-2026-10-15/rea-bundle.json`; this round executes metadata validation, not a new native task.
- [~] Instructions executable without oral context — frozen cases and exact argv/outputs in `verify/final-fixed/`; full-province outside instruction audit not performed.
- [~] No cross-domain bleed — `PROVINCE.md` remains unchanged; R20-ADJACENCY remains unresolved, no new ownership claimed.

Open L0: no new question. Carried kaidoku/revenger overlap remains unresolved (standing `tsukuroi | round-1 | Ratify ... kaidoku/revenger ...` question; lesson R20-ADJACENCY). The existing host pacman pause is obeyed; no ruling or host repair is implied.

## Wave evidence and limitations

L1 holds the canonical planner seat; the validator excludes `planner` as a swarm role. Exactly one unchanged accepted taskCall per validated wave; refused whole calls spawned nobody and were never split. All item paths are lane-absolute; routing stayed role-bound with no model parameter or configuration write. Later routing changes apply only to fresh captures and were not used to restart seats.

| Wave | Seats / role mix | Settled result |
|---|---|---|
| W1 build |64: executor3, reviewer20, scout20, connector8, scribe6, critic6, sentinel1 |26 reports after byte-exact misroot relocation;19 errors and19 aborts;38 reportless, uncaused0 |
| W2 falsify |68: reviewer56, scout7, connector1, mutation-tester4 |49 reports;19 errors;19 reportless, uncaused0 |
| Total |132 seats |75 reports,57 reportless; no replacements |

W1's inherited first dispatch was job-cap refused (zero spawned); this recovery's unchanged call spawned64. W2's first whole call was also refused, then the same payload succeeded after the mandated180-second wait. Specs/dispatches/registries and both attempt records are in `.ufo/waves/round-21/`; wave-slot reservations were released. W2 has68 distinct concrete attacks:32 frozen cases,19 retained logs,5 actual witnesses,2 source reopens,2 isolated-control limbs,4 crosschecks and4 schema mutations.

All4 mutants were killed while preserving positives and exact restoration (`w2/R21Attack65.md`–`68.md`). The returned scoped checks do not substitute for the complete parent matrix, and dead seats receive no verification credit. The connector's real independence limitation was integrated, not dismissed. W2 lacked a fresh critic-role seat (the six W1 critics all died); its reviewer/connector/mutation attacks and final parent-run matrix are reported as what actually ran, not a claimed critic pass.

Per-seat evidence and observation cutoffs: `wave1-terminal.json`, `wave2-terminal.json`, both `*-causes.json`, both `*-outcomes.json`. W1 terminal cutoff initially saw25 lane reports; after the one known fleet misroot was copied/compared/removed, W1 outcomes counted26. This is a location correction, not an extra seat or rewritten cutoff.

**Dead/reportless W1 seats by name:** C1CaseBoundary, C1DirectoryCite, C1HarmonyWitness, C1PositiveWitness, C1RefusalRecord, C1ToonBoundary, C2BoundTypes, C2ExtractorExit, C2IndexTypes, C2MissingIndex, ConnCountDesign, ConnLearning, ConnNoHarm, ConnPriorC1C3, CriticBudget, CriticClaimC1, CriticClaimC2, CriticPopulation, CriticSeparability, CriticSources, ExecFailureCompare, ExecFrozenBattery, ExecVerbBinding, ScoutBindingSchema, ScoutEvidenceJson, ScoutFailureLogs, ScoutHarmonyShape, ScoutRoutes, ScoutSourcePython, ScoutSourceQuotes, ScoutWasmErrors, ScribeMistake, ScribeNullLesson, ScribeRegistry, ScribeResiduals, ScribeSourceGate, ScribeTrend, SentinelParserScope.

**Dead/reportless W2 seats by name:** R21Attack05, R21Attack11, R21Attack13, R21Attack16, R21Attack18, R21Attack21, R21Attack22, R21Attack25, R21Attack34, R21Attack38, R21Attack41, R21Attack50, R21Attack51, R21Attack52, R21Attack54, R21Attack55, R21Attack59, R21Attack61, R21Attack64.

Exact retained terminal error classes: W1 has13 Codex errors,6 Haiku errors and19 `Request was aborted` terminal messages; W2 has18 Zai errors and1 Codex error. Text includes:
```text
Retry budget exhausted after 5 retries: Codex error event: Codex is at capacity, please try again later (code=turn_rate_limit_exceeded)
[anthropic/claude-haiku-5-5] 429 ... This request would exceed your account's rate limit. Please try again later. ... retry-after-ms=4259000
Retry budget exhausted after 5 retries: 429 Rate limit reached for requests
Rate limit reached for requests (type=1302)
Request was aborted
```
Full exact per-seat messages are retained; ellipses in the Haiku summary above abbreviate JSON/request IDs, not a fabricated diagnostic. Aborts are not relabeled provider failures; their cause beyond the retained interruption is not inferred.

Required final fleet misroot sweep `git -C /home/vgpnk/Projects/shokunin status --porcelain` printed only ` M .ufo/l0-questions.md` from another writer; it was left untouched and is not included in this report commit. No untracked own seat report remained. Tool installs/updates: none. Domain source trees and operator configuration remained read-only.
