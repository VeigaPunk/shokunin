# kengaku — round 97 (hyaku run 15, attempt 1)

## Work performed

Declared **R97-C1 coverage** (lowest non-retired axis, cap7): fifteenth located offline TB2 grader replay, `sparql-university`; **R97-C2 calibration** (ceiling10): registry gate-kind/no-selftest-spelling mismatches44→0. Frozen at `8d9d271306c4e7e2d586e51cd546652249d286cb`, measured T `f1083da60e7ff6b88f7420aae7424f7762d14700` (`plans/round-97-claims.md`).

**Self-verdict: honest stop, not admitted.** Both measured targets reproduce. C1 is met as measured; C2 is **not admitted**, because its exact frozen ROWS171 includes C1's two registry rows while the C2-only control prints169. The two controls establish instrument separability, not exact-string/candidate-byte separability (ConnectorOverlap F1/F2). Q80's second committed prefreeze counter runs are also missing. Late successful repetitions cannot backdate compliance. No frozen bytes were repaired.

- Captured nine source files at TB2 pin `2fd12b88`, filed mechanism predictions before test-graph execution; 18/18 predictions reproduced after fixing a staging bug (`L1/predictions-mechanism.txt`, `L1/dryrun/README.md`).
- Replay: unchanged grader functions plus real pytest reward in clearenv/no-network bwrap; Python3.13, rdflib7.1.4, pytest8.4.1. The wrapper's CTRF plugin/reporting and prebuilt image were not executed. New member ledger40→41, file-artifact31→32/76 (`corpus/evidence/round97/sparql-probe.txt`).
- Calibration: exactly44 kind-only gate→probe changes, no old script edited. Independent AST/CLI audit confirms all44 lack self-invocation modes; zero other cells changed (`w1/ExecC2.md`). This is not a claim that the remaining84 gates satisfy full semantic Gate-standard conformance.
- Pre-freeze no-work, positive, forgery, separability and harm controls committed at P2 before F (`L1/controls/`). All named negative controls reject. C scope exactly three candidate-byte files plus the receipt, frozen instruments10/10 intact (`w1/ExecHarm.md`).
- One v1 wave11 seats; all settled before this report, WAVE-DONE received from Main. Roles:3 executor,2 reviewer,1 critic,2 mutation-tester,1 scout,1 connector,1 scribe; attack5/11, connector1; no residual calls, no dead seats. Planner held by L1, bounded planning data-walk by connector (`w1-spec.json`, `w1-dispatch.json`, `w1-results.json`).
- MutC2 falsified detector discrimination: nine forged commits emit the exact frozen output block,16/18 selftest mutants survive; one load-bearing add_parser-regex deletion leaves selftest green while making T red (`w1/MutC2.md`). Finite actual44→0 still corroborated; no general soundness credit.
- Added sourced knowledge, coverage-map row, lesson M1–M7, Q81, SCORECARD and LOG. Preserved inherited r96 permanent history harm, standing reds, r95/round92 debts (`corpus/lessons/round-97.md`).
- New debt: anchor-digest already red80→86 (six new nested captures unbound); historical sweep27→28. Selected gate exit codes unchanged, not a universal no-harm claim (`w1/ScoutSources.md`, `w1/ConnectorOverlap.md`). Source wording corrections dated in lesson; immutable source rows not rewritten.

## Landed changes

All changes tie to `LOG.md:3673-3685` (Round97).

| landed lane hash | change / LOG pointer |
|---|---|
| `5b41c1c3e1a8e542d3a38c9f20965f7ea6404019` | P0 capture, predictions, census start; LOG order |
| `b2352135e2b55e8017b6e9d1e7bc4d34d5062438` | P1 instruments/cases/dry runs, BASE census; LOG order |
| `e40fd0c2a00ba95c190925a6ce066bc8354949ff` | P2 controls, candidate copies, harm outputs; LOG order |
| `8d9d271306c4e7e2d586e51cd546652249d286cb` | F frozen predicates, ten instrument hashes, three candidate hashes; LOG order |
| `f1083da60e7ff6b88f7420aae7424f7762d14700` | C official receipt, ledger/class flip,44 kind cells, S317–S325; LOG order |
| `2227bcf11a38043e0ef5e0e134b752f0128610ac` | integration after WAVE-DONE: all11 seats, knowledge, lesson, Q81, index, scorecard, LOG |
| `3d52d89e25da2719e1138a95aa41644e83add422` | final receipts plus LOG verification pointer |

Final pushed lane tip **`3d52d89e25da2719e1138a95aa41644e83add422`**: `git -C /home/vgpnk/Projects/shokunin/kengaku-shokunin ls-remote origin refs/heads/master` printed that hash.

## Before → after measurements

Paths below are lane-relative under `.ufo/waves/round-97/` unless stated.

**C1:** `python3 plans/round97_c1_replay.py --lane . --rev REV --work DIR --grader-venv G`.
- Before BASE `4992cd0e32b8db23ca20310deb7de12d485f8bcc`: executed40/88, file-artifact31/76; no-work rc1. Independent BASE replay all9 legs fail (`w1/ExecC1.md`, independent BASE receipt cited there).
- T `f1083da6`: `LEGS L1=pass L2=pass L3=pass L4=pass L5=pass L6=pass L7=pass L8=pass L9=pass`; `TARGET executed_rows=41 member=sparql-university cells=file-artifact:32 set_contains_base=1 located=1 executed=1 cases=18 legs=72 mismatches=0 defects=0`; `PREDICATE R97-C1 pass`, rc0 (`L1/c1-tip.txt`). ExecC1, ReviewC1, critic and connector reproduce it independently. Score7→7 held.

**C2:** `python3 plans/round97_gate_selftest_census.py --lane . --rev REV`.
- BASE: rows168, gates127/with-selftest83/without44; `MISMATCH_TOTAL n=44`; fail rc1 (`L1/c2-base.txt`).
- T: `ROWS base=168 rev=171 removed=0 duplicate=0 cells_changed=0`; `GATES total=84 with_selftest=84 without=0 demoted_with_selftest=0 scripts_changed=0`; `MISMATCH_TOTAL n=0`; pass rc0 (`L1/c2-tip.txt`).
- **Measured target true, admission withheld**: exact C2-only ROWS169 differs from frozen171, and shared SKILL candidate hash binds both edits. Mutation findings constrain discrimination; no repair or target narrowing after freeze. Score10→10 held.

**Final integrated check:** measured revision `2227bcf11a38043e0ef5e0e134b752f0128610ac`, `L1/final-verification.txt`: both predicates rc0, freeze-integrity10/10 intact rc0, census rc0, anchor-line live0/cells0 rc0. The last commit only retains this receipt/LOG. No claim that post-freeze reruns cure Q80.

## Sources & frontier

SOURCES rows **308→317**. Counting command `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`, or the census CLI below. Added S317–S325: tierA8/tierB1; mined6/rejected3. No existing status/recheck/used-by changes. S317–S322 ground C1 and `corpus/knowledge/tb2-sparql-university-grader.md`; coverage-map row in `corpus/README.md` names the newly held SPARQL hidden-graph surface. Frontier member unexecuted→executed. ScoutSources live verification9/9 HTTP200, byte/sha/quote/word counts equal (max24 words). Six new anchor-digest findings are retained, not hidden behind anchor-line green.

Search/Gate and mistake mine: `corpus/lessons/round-97.md` (every URL/access date/located quote, admit and reject reasons/flips, M1–M7). Q81 distinguishes spelling from self-test capability, with committed red laundering controls. Outside discernment sample remains for closure: a dispatched seat is still this lane.

Assimilation: none (merge/kengaku inherited L0 round54 hold). No considerthese proposal adopted; ScoutSources verified all five latest2026-11-05 proposals remain unimplemented; coverage-cap L0 remains open. No new L0 question filed.

Census command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kengaku`.

Start output (`L1/census-start.txt`):
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
kengaku	W04	S256 duplicate url raw.githubusercontent.com/harbor-framework/terminal-bench-2/2fd12b88aafdd04a52c298e3940bcb189f9766d6/README.md across scopes
kengaku	W04	S266 duplicate url raw.githubusercontent.com/harbor-framework/terminal-bench-2/2fd12b88aafdd04a52c298e3940bcb189f9766d6/log-summary-date-ranges/instruction.md across scopes
kengaku	W04	S268 duplicate url raw.githubusercontent.com/harbor-framework/terminal-bench-2/2fd12b88aafdd04a52c298e3940bcb189f9766d6/log-summary-date-ranges/tests/test.sh across scopes
kengaku	W04	S269 duplicate url raw.githubusercontent.com/harbor-framework/terminal-bench-2/2fd12b88aafdd04a52c298e3940bcb189f9766d6/nginx-request-logging/tests/test.sh across scopes
kengaku	W04	S270 duplicate url raw.githubusercontent.com/harbor-framework/terminal-bench-2/2fd12b88aafdd04a52c298e3940bcb189f9766d6/pyproject.toml across scopes
kengaku	ok	/home/vgpnk/Projects/shokunin/kengaku-shokunin/corpus/SOURCES.md
rc=0
```
End output (`L1/census-end.txt`, explicit observed exit0):
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
kengaku	W04	S256 duplicate url raw.githubusercontent.com/harbor-framework/terminal-bench-2/2fd12b88aafdd04a52c298e3940bcb189f9766d6/README.md across scopes
kengaku	W04	S266 duplicate url raw.githubusercontent.com/harbor-framework/terminal-bench-2/2fd12b88aafdd04a52c298e3940bcb189f9766d6/log-summary-date-ranges/instruction.md across scopes
kengaku	W04	S268 duplicate url raw.githubusercontent.com/harbor-framework/terminal-bench-2/2fd12b88aafdd04a52c298e3940bcb189f9766d6/log-summary-date-ranges/tests/test.sh across scopes
kengaku	W04	S269 duplicate url raw.githubusercontent.com/harbor-framework/terminal-bench-2/2fd12b88aafdd04a52c298e3940bcb189f9766d6/nginx-request-logging/tests/test.sh across scopes
kengaku	W04	S270 duplicate url raw.githubusercontent.com/harbor-framework/terminal-bench-2/2fd12b88aafdd04a52c298e3940bcb189f9766d6/pyproject.toml across scopes
kengaku	ok	/home/vgpnk/Projects/shokunin/kengaku-shokunin/corpus/SOURCES.md
rc=0
```

## Trend verdicts

- **expansion: improved.** One new sourced knowledge entry on previously unexecuted SPARQL hidden-graph ground, indexed in the coverage map; real replay40→41. Not row-count-only credit.
- **quality: unchanged.** No older knowledge entry reverified/superseded. New source-model wording issues are marked; six extra anchor-digest findings and historical sweep delta remain debt. No universal no-harm verdict.
- **discernment: unchanged pending outside closure.** Lane seats reopen9/9 and Q81 is grounded, but these seats do not satisfy the external spot-check rule. C2 non-admission and Q80 defect disclosed, not laundered into an improvement.

## SHONEN

- [~] Real decision tables/error patterns/checklists/cited sources — `SKILL.md`, new knowledge entry; independent scope review `w1/ConnectorOverlap.md`, no promotion requested.
- [~] End-to-end domain task executed/logged — official SPARQL replay + `LOG.md:3673`, reproduced by ExecC1/ReviewC1.
- [~] Executable without oral context — commands in frozen claim/registry, independent reruns in `w1/ExecC1.md`; not blanket certification.
- [~] No cross-domain bleed — `PROVINCE.md`; ConnectorOverlap's named province ruling, operator promotion unchanged.

Stale-lane: respawn-per-round, no other kengaku mission open. Inherited uncommitted state at start: none. Misroot sweep left orchestrator `.scratch/` changes and unrelated numeric `w4lines.txt` untouched; no seat-attributed fleet misroot found.
Tooling: no host installs/upgrades. Preinstalled uv0.13.0; scratch-only CPython3.13.16 (official uv distribution), rdflib7.1.4/pytest8.4.1 and transitive pyparsing3.3.3 (uv pip/PyPI) for grader reproduction; scratch removed after receipts. Pacman and host sysctls untouched.
