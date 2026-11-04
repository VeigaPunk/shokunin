# Kengaku — round 73, attempt 1

## Work performed

Declared **R73-C1 — coverage** (lowest non-retired axis, L0-capped at7): widen the advertised-instrument universe to plans documents and register the exposed instruments. Declared **R73-C2 — calibration**: derive a registry-row audit from repository declarations and bring its mismatch count to zero. **Both original claims are NOT ADMITTED.** Their engineering repairs run green, but the original C1 predicate contradicts completed registration and C1's row additions invalidate C2's frozen exact denominator. No retroactive re-scoring or axis increase is claimed.

All lane-relative pointers below resolve beneath `/home/vgpnk/Projects/shokunin/kengaku-shokunin/`; fleet reports are explicitly identified. Final pushed lane tip: **`f669367c9051a1716a622e756325f4a48c360348`**. Final exercised implementation snapshot: **`208ed16a1ba28af8ddcac9011af77fcf98a1b063`**; the later commit records its receipts and append-only measurement notes, not a new implementation.

- Froze two instruments, claims, controls and red-before receipts at `255c261db2119906c70195291a2b6f9f46f82a72`, base `d96c3e62fd01771718368688c2685dceeef5b83e`. Evidence: `plans/round-73-claims.md`; `corpus/evidence/round73/{c1-before,c1-control-legacy,c2-red-before,c2-control-frozen-tuple}.txt`.
- Widened `plans/round52_c2_registry.py` to read plans/*.md and added seven exposed registry rows plus the new audit row. Corrected the sources-adopt invocation/map and class-survey kind; integrated independent row audits fixing the absent r69 receipt, missing usage exits and underdeclared write scopes. Removed the obsolete malformed five-cell tensor row after adding its full replacement. Evidence: `SKILL.md` registry, `corpus/evidence/round73/w1/c1-row-audit.md:51-69`, `c1-rows-draft.json`.
- Added `plans/round73_c2_registry_audit.py`: parse-survivor row derivation, declaration-shape checks, duplicate-name check, AST construction and item-local revision tokens. It is **not semantic truth or runtime certification**. Selected mutants7/7 are not comprehensive: the separate sixteen-case attack accepts thirteen cases. Evidence: `final-checks.txt:48-89`, `.ufo/waves/round-73/w1/C2BlindSpotR73.md` and `C2CriticR73.md`.
- Corrected the round's self-assessment rather than reporting amended green as original success. A1 replaces self-defeating plans_only with plans_seen; A2 relaxes exact106 after the registry grows114. They were mid-wave amendments; absence of returned reports did not prove absence of scoring. Actual amendment commit time is 02:48:24Z, not the future heading times. Evidence: claims E-R73-1; `a1-red-green.txt`; `.ufo/waves/round-73/w1/RegistryReviewerR73.md`; lesson M73-1…4.
- Fixed a safety defect discovered by CredentialSentinelR73: selftest/mutants deleted the caller's entire --work directory. Both now allocate and remove only an owned child. Red-before canaries were deleted; after-repair and committed-clone canaries survive with no fixture children left. Evidence: `.ufo/waves/round-73/w1/CredentialSentinelR73.md:29-46`, `cleanup-after.txt`, `final-checks.txt:63-89`. This security repair changes scratch ownership, not frozen verdict rules.
- Curated S249 from a live source opening; integrated a **held** knowledge candidate, the round lesson and Q54's projected-registered-tree freeze criterion. No held HF candidate admitted. Evidence: `corpus/SOURCES.md` S249, `corpus/knowledge/instrument-registry-derivation.md`, `corpus/lessons/round-73.md`, `corpus/QUALITY.md` Q54.
- Retained cross-lane findings without copying or mutating sibling code: tabi registry checks, kama process-provenance observations, mori population digests, kotoba field checks. Evidence: `.ufo/waves/round-73/w1/SiblingConnectorR73.md`, `corpus/evidence/round73/w1/sibling-overlap.md`. Outside-observed HF provenance remains unimplemented, not silently claimed.

**Wave contract.** One validated v1 wave, sixteen seats; no residual dispatch. Role mix: executor4, reviewer3, critic2, scout2, scribe2, mutation-tester1, connector1, sentinel1. Attack roles6/16 =37.5%; connector1. L1 KengakuR73 holds the canonical planner seat; RoundStateScoutR73 provides the bounded planning data-walk (validator forbids a planner swarm role). `w1-validate.rc` is `rc=0`; ready handed to orchestrator once. WAVE-DONE was received **before integration and this report**. `w1-results.json` has seats16, results length16 and no non-null notes; all sixteen seat reports are present. Zero deaths reported; the result wrapper omits explicit per-seat status/id fields, so no stronger provider-status claim is inferred. Actual configured routes read from `/home/vgpnk/.omp/agent/config.yml:430-445`: reviewer @m_zfl, other used roles @m_flash, no m_mim; no model overrides passed. Answering-provider identity is not established by the results wrapper and neither claim depends on one.

**Scope/housekeeping.** Required fleet porcelain sweep found only orchestrator .scratch state, sibling kama report and an unattributable `after` file whose sole text is `== SCORECARD diff base-`; none names this lane/round sufficiently to authorize relocation. No misroot attributable to our seats was moved/deleted. No MANIFEST/runtime/sibling/domain-source files edited. No inherited uncommitted round work adopted from another attempt; base included the committed non-author round72 spot-check, left unchanged. Stale-lane: this dispatched round only, no other mission of this lane open; observable landed commits throughout. Tools installed/updated: **none**; pacman remained paused. Existing L0 questions carried unchanged: kengaku rounds25/33/51,54,56,63,65,66,67. No operator answer inferred.

## Landed changes

Each row is tied to append-only `LOG.md` round73 (`:2746-2790`). Only helper-verified `landed` hashes are cited.

| commit | landed work | LOG/evidence |
|---|---|---|
| `255c261db2119906c70195291a2b6f9f46f82a72` | freeze, instruments, controls, starting census, validated sixteen-seat spec/dispatch | LOG round73 Claims/Controls; `plans/round-73-claims.md`, `.ufo/waves/round-73/w1-spec.json` |
| `ea41880fa755816d2c21a7ee53e14bf95d95e340` | initial registry additions/corrections and A1/A2, initial after receipts | LOG Verdicts/Registry corrections; `c1-after.txt`, `c2-after.txt`; original failures retained |
| `208ed16a1ba28af8ddcac9011af77fcf98a1b063` | settled sixteen-seat findings, audited row corrections, owned-child cleanup repair, S249, held candidate, lesson/Q54, honest scorecard/index/log | LOG Learning/Registry corrections; full `.ufo/waves/round-73/` and `corpus/evidence/round73/w1/` |
| `f669367c9051a1716a622e756325f4a48c360348` | final committed-snapshot checks, end census and appended measured-revision notes | LOG Round73 measured landing/security disposition; `final-checks.txt`, `census-after.txt` |

Remote proof executed before writing this report:

```text
$ git -C /home/vgpnk/Projects/shokunin/kengaku-shokunin ls-remote origin refs/heads/master
f669367c9051a1716a622e756325f4a48c360348  refs/heads/master
```

## Before → after measurements

### R73-C1 — original not admitted; coverage7→7

Counting command: `python3 plans/round52_c2_registry.py --lane . ; echo "rc=$?"`.

| measured bytes | observed | evidence under `corpus/evidence/round73/` |
|---|---|---|
| base d96c3e62 | ADVERTISED110, MISSING5, R52 fail, rc1 | `c1-before.txt` |
| frozen counter255c261d over the same complete registered tree used by its amendment | ADVERTISED113, MISSING0, plans_only0, **R73-C1 fail, rc1** | `a1-red-green.txt` |
| amended implementation208ed16a, clean shared clone | full mode, files134, plans_seen82, plans_only0; ADVERTISED113; REGISTERED113 rows115; five inventory legs0; R73-C1 pass rc0 | `final-checks.txt:5-19` |
| legacy mode on208ed16a | ADVERTISED113, MISSING0, plans_seen0; R52 pass, **R73 fail rc1** | `final-checks.txt:21-35` |

Completeness remains bounded to the CMD regex and existing-script filter: two real hyphenated evidence instruments are omitted, plus deliberately excluded nested fixture helpers (`c1-row-audit.md:28-40`). Post-registration legacy and full have the same set because SKILL.md itself advertises registered entries. The before-registration full sweep exposed two additional instruments; that is not a post-registration unique-contribution measurement. Original target112 and amended113 must not be called unchanged. The freeze's plans_only condition is mathematically incompatible with missing0; RegistryReviewerR73 independently confirms it. No coverage increment and no capability acquisition.

Selftest command: `python3 plans/round52_c2_registry.py --selftest` → cases4 failures0 rc0. The plans-only fixture distinguishes full/legacy, but does not repair the original landing contradiction. Control receipts are preserved at freeze, not invented after review.

### R73-C2 — original not admitted; calibration10→10, exercised

Counting command: `python3 plans/round73_c2_registry_audit.py --lane . ; echo "rc=$?"`.

| measured bytes | observed | evidence under `corpus/evidence/round73/` |
|---|---|---|
| frozen audit over base d96c3e62 | scripts106, MISMATCH2, rc1; sources-adopt failure-map declaration and class-survey kind | `c2-red-before.txt` |
| old round72 counter on fifth-defective-row fixture | E1a/E1b/E1c/E2 ok, DEFECTS0 rc0; new audit on same fixture MISMATCH2 rc1 | `c2-control-frozen-tuple.txt` |
| final implementation208ed16a, clean shared clone | instruments114 rows114, parsed114 failed0, D1–D4 zero, MISMATCH0, R73-C2 pass rc0 | `final-checks.txt:48-61` |

The exact frozen106 denominator misses114 and causally depends on C1 adding rows. A2's threshold is not original admission authority. Moreover malformed lines could disappear before pricing; one obsolete malformed tensor declaration was removed only after its complete replacement landed. Pins/scope are nonempty-only, CLI flags are not acceptance-tested, successful AST construction is not compilation/execution, owner-prefix matching is not identity verification, and D4 token co-occurrence accepts contradictory prose. These limits are explicit in the held entry and lesson; the unqualified “every row/every field truth” claim is rejected.

Exercised controls on208ed16a:

```text
--selftest --work DIR: SELFTEST arms=4 red=3 ok=True; rc0
--mutants --work DIR: MUTANTS total=7 killed=7 survived=0 invalid=0 null_detected=1; rc0
both modes: CALLER-PRESERVED True
sources_adopt.py --selftest: SELFTEST cases=17 failed=0; rc0
staging scan: SCAN files=55 skipped=0 hits=0; rc0
```

All commands/direct exits and measured revision are in `final-checks.txt`; no new model/service replay or global no-harm proof is asserted. No axis score increased. Known false-green/weakly tested behaviours are marked rather than passed off as comprehensive conformance. Round admission is withheld because both original claims fail, independent of any no-harm opinion.

## Sources & frontier

`corpus/SOURCES.md`: **240→241 rows**; one new row, **A=1, B=0, C=0 added**, S249. No pre-existing status/recheck/used-by cell changed. S249 absent→mined, on-release, used-by round73 lesson and held registry-derivation entry. Source admission supports R73-C2's AST-construction leg only. HTTP200, Python3.15.2 documentation, 362493 bytes, sha256 `94bead0ac6482efc08bbc790acb1cff809ca4b8a9829a1def2245451a42fe809`; capture quote at2680 “Parse the source into an AST node.” (seven words). The warning2708-2715 rejects executable-validity inference. Local runtime in seat receipts is Python3.14.8; the docs are an API source, not a claimed runtime-version pin. See SourcesAstR73 report and `sources/ast-anchor.md`.

Counting command for row totals:
`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` on the cited before/after trees.
Census command at both ends (full outputs below):

```sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kengaku
```

Before, base d96c3e62, exit0 (`census-before.txt`):

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
kengaku	ok	/home/vgpnk/Projects/shokunin/kengaku-shokunin/corpus/SOURCES.md
rc=0
```

After, measured208ed16a, exit0 (`census-after.txt`):

```text
COMMAND: /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kengaku
MEASURED_COMMIT: 208ed16a1ba28af8ddcac9011af77fcf98a1b063
RUN_AT: 2026-11-04T03:01:38.175297+00:00
ROWS: 241
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
kengaku	ok	/home/vgpnk/Projects/shokunin/kengaku-shokunin/corpus/SOURCES.md
rc=0
```

Both have25 W04 across-scope duplicate-URL warnings, no new census defect. No frontier-to-core knowledge admission; new candidate remains hold, as do the round71/72 HF entries. **Assimilation: none.** No staged shokuknow append or renumber map applied. Latest `considerthese/2026-10-26.md` proposal2 (standing TB2 package-admission/filler control) considered, not implemented: it is a different surface from this round's frozen registry checks. The reflection is not evidence; S249 is the actual opened source. Rejected AST-executable-validity inference and flip condition are in lesson Gate. Mistake repairs demonstrated red-before: A1 identical-tree fail→pass and sentinel caller-canary deletion→preservation. Dispatched reviewers are still the lane; outside spot-check remains pending.

## Trend verdicts

- **expansion: unchanged** — one narrow source row and held candidate, no admitted new knowledge/capability or frontier-to-core movement (`corpus/README.md` round73 boundary; lesson Gate).
- **quality: improved** — missing rows and invalid/dead registry entry declarations corrected; caller-owned scratch deletion fixed with red/green evidence; structural weakness explicitly marked, not hidden (`c1-row-audit.md`, `cleanup-after.txt`, `final-checks.txt`). This is bounded engineering improvement, not original-claim admission or whole-lane conformance.
- **discernment: unchanged** — own adversarial seats expose invalid freezes and thirteen accepted attack cases; Q54 records the mistake. No outside non-author agree/disagree on this round yet; no self-awarded discernment improvement.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md`, `corpus/knowledge/instrument-registry-derivation.md` decision table (held candidate, structural limits explicit).
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md:2746-2790`, measured registry/audit workflow and cleanup repair in `final-checks.txt`; original predicates honestly miss.
- [~] Instructions executable by an agent without oral context — exact commands, isolated fixture receipts, source captures and explicit exit maps in `SKILL.md` registry; incomplete selftest finding-id conformance remains named.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` unchanged; SiblingConnectorR73 reports sibling patterns without code adoption or sibling writes. No named non-author promotion verifier; no [x].

### Prior-round errata (filed reports remain unchanged)

1. **R72-V1:** fleet `.ufo/reports/round-72/kengaku.md` landing citation `08df910a461620741d433def3df38a8406efe9f` is39 characters and dead. Correct object: **`08df910ab461620741d433def3df38a8406efe9f`**. It supersedes all four malformed report mentions and the inherited box2 citation, not the report's historical bytes. Ground: `corpus/lessons/round-72-verifier-spotcheck.md:136-140`.
2. **R72-V2:** `corpus/evidence/round72/census-after.txt` says LANE_TIP b6336136 while describing a landing-worktree run; the file first ships with08df910ab. db78d059 reran final-c1-check/c2-green/c2-controls, **not that census**. Exact historical worktree identity cannot be reconstructed from its wrong label; census substance was re-derived by the non-author spot-check. Do not attribute this receipt to the final-tip rerun. Ground: round72 spot-check §1 and §6 item2.
3. **R72-V3:** round72 lesson reject ground(iii)'s “no N14/N20 rows” sweep is withdrawn: it returns unrelated battery38 lines. Refusal remains on the independently sufficient triad/source-id provenance grounds; no fabricated negative sweep substituted. Ground: spot-check §6 item3; round73 Mistakes M72-V3.
4. **R71-R2 carried:** fleet round71 report attributed counter receipts to edaea66e; `corpus/evidence/round71/final-c2-gate.txt:1` records **c80fcdb3761035a711aaa7f1edfabaaa5da01eb3**. That is the receipt's measured revision, not edaea66e. Historical report untouched.
5. **This round's amendments:** A1/A2 were committed at02:48:24Z, not their heading02:54/02:56Z. E-R73-1 preserves this correction and the original not-admitted outcomes. “No reports returned” never establishes “no data scored.”
