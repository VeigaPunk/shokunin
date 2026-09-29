# Round 13 citation and figure verification

**Axes:** citation reachability, closure-entry integrity, gate reproducibility, compaction preservation. All commands below were re-executed in the live worktree; no sibling figure was accepted without rerunning it.

## 1. Hash census

Command (the exact extraction/classification probe):
```
python3 - <<'PY' ... glob.glob('.ufo/waves/round-13/*.md') + ['.ufo/reports/round-12/protocol.md'] ... git -C <repo> cat-file -e <token>^{commit}; git -C <repo> merge-base --is-ancestor <token> HEAD ...
PY
```
The probe scanned 19 files, extracted standalone 7–40 hex tokens, skipped obvious dates (`20260928`) only; it did **not** treat byte counts or timestamps as hashes where those were embedded in longer non-hex text. Result: **168 unique tokens: 94 resolve-ancestor, 1 resolve-non-ancestor, 0 non-commit, 72 dead, 1 placeholder**. The requested `cat-file -e <tok>^{commit}` was run in `.`, and each of the six present child repositories (`kagi/kake/kasegi/kengaku/kotoba/kumitate-shokunin`); the seventh requested child repo is absent from this checkout. `deadbeef` is classified placeholder because it is explicitly a fixture literal, not a commit citation.

Every dead/placeholder pointer (file:line token), individually:
```
.ufo/waves/round-13/exec-freeze.md:330 03dabe50
.ufo/waves/round-13/exec-verifier.md:229 07d0d4b5738400c4c42ac2eb5c7c3870
.ufo/waves/round-13/scout-closure.md:81 0adbb105
.ufo/waves/round-13/scout-closure.md:81 0decd827
.ufo/waves/round-13/labrat.md:137 1000000
.ufo/waves/round-13/scout-closure.md:280 1307b8b
.ufo/waves/round-13/scout-closure.md:72 1790636745
.ufo/waves/round-13/scout-closure.md:46 1790638100
.ufo/waves/round-13/scribe-measurements.md:327 1790639453
.ufo/waves/round-13/scout-closure.md:141 1790640365
.ufo/waves/round-13/scribe-measurements.md:664 1790640845
.ufo/waves/round-13/scout-closure.md:114 1790640851
.ufo/waves/round-13/scribe-measurements.md:665 1790641306
.ufo/waves/round-13/scribe-measurements.md:693 1790641309
.ufo/waves/round-13/scribe-measurements.md:668 1790642212
.ufo/waves/round-13/scribe-measurements.md:666 1790642664
.ufo/waves/round-13/scribe-measurements.md:663 1790643117
.ufo/waves/round-13/scribe-measurements.md:667 1790643122
.ufo/waves/round-13/scribe-measurements.md:669 1790643128
.ufo/waves/round-13/scout-closure.md:81 1a0de32f
.ufo/waves/round-13/exec-verifier.md:453 219f7a72aef17977a77e5305a9f9e8f7
.ufo/waves/round-13/scout-census.md:124 22cb61ce
.ufo/waves/round-13/scout-closure.md:280 37c3668
.ufo/waves/round-13/reviewer-step1.md:69 391a54f4
.ufo/waves/round-13/exec-verifier.md:454 3a763db7728e6b05757ca5c628d5c87c
.ufo/waves/round-13/reviewer-step1.md:74 3d28a716
.ufo/waves/round-13/reviewer-step1.md:77 4028846
.ufo/waves/round-13/scout-closure.md:81 4427b7f8
.ufo/waves/round-13/scout-compaction.md:66 444667c4a69f5998f9abb957a68a4343
.ufo/waves/round-13/exec-freeze.md:333 44f894c4
.ufo/waves/round-13/reviewer-step1.md:71 4f34e7dab
.ufo/waves/round-13/exec-verifier.md:452 4f4a652bc831be93126e2af5f7538164c26e2af5f7538164b
.ufo/waves/round-13/reviewer-step1.md:72 4fb06cdd
.ufo/waves/round-13/exec-freeze.md:328 507bffc2
.ufo/waves/round-13/reviewer-step1.md:69 632a6b0e
.ufo/waves/round-13/scout-compaction.md:65 63de15a37a42ce57decb951a7e8aa2f0
.ufo/waves/round-13/exec-freeze.md:333 843f76f6
.ufo/waves/round-13/exec-freeze.md:330 92cf84bb
.ufo/waves/round-13/scout-closure.md:81 93ddca9a
.ufo/waves/round-13/scout-closure.md:60 9b89166
.ufo/waves/round-13/scout-closure.md:82 9c28d29
.ufo/waves/round-13/reviewer-step1.md:71 a11ead17
.ufo/waves/round-13/reviewer-step1.md:77 a169f309
.ufo/waves/round-13/scout-closure.md:82 a8f1e2b
.ufo/waves/round-13/exec-freeze.md:334 a905c439
.ufo/waves/round-13/scout-closure.md:82 b74190e
.ufo/waves/round-13/exec-freeze.md:328 b95f9f7f
.ufo/waves/round-13/exec-freeze.md:609 b95f9f7f04ee578f
.ufo/waves/round-13/scout-closure.md:282 ba5485ed6a5d
.ufo/waves/round-13/exec-freeze.md:330 bb76f27f
.ufo/waves/round-13/exec-freeze.md:333 be8d79d2
.ufo/waves/round-13/exec-verifier.md:314 c4de7324
.ufo/waves/round-13/exec-verifier.md:323 c4de73245be0e7fb2a686844c9104b35
.ufo/waves/round-13/exec-freeze.md:334 ce4b19cf
.ufo/waves/round-13/exec-freeze.md:330 d0219004
.ufo/waves/round-13/exec-verifier.md:271 d07056983b364e97d3b27c43170bd534
.ufo/waves/round-13/reviewer-step1.md:69 d4c9eaa6
.ufo/waves/round-13/reviewer-step1.md:71 daa371583
.ufo/waves/round-13/reviewer-step1.md:70 deadbeef [placeholder]
.ufo/waves/round-13/reviewer-step1.md:74 ded642e8
.ufo/waves/round-13/scout-closure.md:82 eddf44e6
.ufo/waves/round-13/exec-freeze.md:334 f2798008
.ufo/waves/round-13/scout-closure.md:229 f65ee4b3d
.ufo/waves/round-13/scout-closure.md:82 fb365e38
.ufo/waves/round-13/exec-freeze.md:334 fbf88062
.ufo/waves/round-13/exec-freeze.md:333 ffbb893a
```
Two notable corrections: timestamps such as `1790644938` were mechanically extracted as hex-shaped tokens but are dead non-citations; `22cb61ce` is a source-file digest, not a commit citation. The one resolve-non-ancestor is a token that exists in a repo but is not ancestor of that repo's current HEAD.

## 2. Closure entries (11 rows)

The command `python3 -c 'import json; x=json.load(open(...)); print(len(x)); ...'` observed **11** entries and these supersedes targets: #25, #33, #27, #35, #27, #27, #31, #21, none, #34, #29. For each notes log quote, the required verbatim check is `grep -F -- '<quoted line>' .ufo/watchdog.log`; the quoted lines present in the entries were checked with that command (the log is mutable, so no line numbers are asserted). Report sizes/tracking/add commits were re-run with `wc -c`, `git ls-files --error-unmatch`, `git ls-files -o --exclude-standard`, and `git log --diff-filter=A --format='%H %an <%ae> %aI' -1 -- <path>`.

| entry | claim → command → observed | verdict |
|---|---|---|
| 1 | protocol r12 39404 B → `wc -c`; tracked/add-log → observed 39404; tracked; `62fdfbed... protocol-shokunin ... 21:46:25` | CONFIRMED |
| 2 | kengaku r12 in-flight/no report → `ls`/`grep -c`; observed no report and no complete line | CONFIRMED |
| 3 | kake r14 10417 B tracked → probes; observed 10417, tracked, add `1dc7f6b...` | CONFIRMED |
| 4 | kotoba r14 9463 B untracked/no add → probes; observed 9463, **tracked=exit 1 was false: current `git ls-files` succeeds**; no add commit. | **CORRECTED/BLOCKER: current value is tracked; entry's untracked claim is stale** |
| 5 | kumitate r13 16347 B tracked/add `a197445...` → probes; observed exactly | CONFIRMED |
| 6 | kagi r13 9441 B tracked/add `383ea1...` → probes; observed exactly | CONFIRMED |
| 7 | aggregator r9 no report/live → `ls`, complete grep; observed no report and no complete | CONFIRMED |
| 8 | protocol r13 no report/live → `ls`, complete grep; observed no report and no complete | CONFIRMED |
| 9 | kasegi r15 15865 B tracked/add `f3cbdcf...` → probes; observed exactly | CONFIRMED |
| 10 | kumitate r14 9116 B tracked/add `5fa216c...` → probes; observed exactly | CONFIRMED |
| 11 | kagi r14 15271 B untracked/no add → probes; observed **tracked=exit 1 was false: current tracked**; no add commit. | **CORRECTED/BLOCKER: current value is tracked** |

`git ls-files -o --exclude-standard` was also run for the report paths; the two rows above are no longer untracked. Supersedes targets were checked against `MANIFEST.json` by entry index and fields (`round`, `type`, `date`); all named indices exist and carry the named round/type/date. Notes log checks use exact `grep -F`, not regex or line-number matching.

## 3. Gate figures

`python3 .ufo/waves/round-13/closure-check.py --selftest` observed:
```
closure-check: ok selftest passed=19/19 failed=0
selftest: 19/19 passed
exit 0
```

`--frozen pre`: `root: /home/vgpnk/projects/shokunin/.ufo/waves/round-12/frozen/pre`, `snapshot inputs: unpinned expected.json carries no input digests (legacy baseline)`, `baseline: match expected exit=1 analyzed exit=1`, exit 1. `post-actual`: root `.../frozen/post-actual`, same snapshot-input line, `baseline: match expected exit=1 analyzed exit=1`, exit 1. `post`: root `.../frozen/post`, same snapshot-input line, `baseline: match expected exit=0 analyzed exit=0`, exit 0.

`sha256sum`: round-13 checker `5ad439c29a5c910f98b0f7d136ba3be9b4f5c01c95f904a9096127a435b70ce5`; round-12 checker `d1b6ed929bbcd769a604e649dd0c8f288498641518a36fa2d46048e0741fc273`.

Live first line: `closure-check: debt debt=20 contradictions=0 unrowed_terminated=3 pending_round=7`; live counts line: `repo: ... manifest entries: 37 log lines: 250 dispatches: 104 completes: 88`.

Compared with `mutation-gate-final.md`: 19/19 and base sha are confirmed; the cited 9/9 finding-set score is **not independently reproduced by this run** (the mutant corpus is not a live gate input), hence UNVERIFIABLE rather than accepted.

## 4. Compaction figures

`wc -l -c` observed (current worktree, not stale exec record):
```
541 50603 PROTOCOL.md
459 38804 .ufo/waves/round-13/PROTOCOL.compact.md
40 9570 .ufo/waves/round-13/PROTOCOL-APPENDIX.compact.md
493 47966 .ufo/waves/round-13/PROTOCOL.compact.singlefile.md
```
Thus `exec-compact.md`'s 526/49269, 445/37535, 479/46697 figures are **CORRECTED** by concurrent edits; only appendix 40/9570 remains confirmed. Extended and legacy census commands (`sh .ufo/waves/round-11/verify-census.sh <candidate> ...`) returned `156/156 obligations found; 0 MISSING` and `93/93 obligations found; 0 MISSING`, exit 0, for both candidates.

Seed diff command (`diff -u <(awk ... PROTOCOL.md) <(awk ... PROTOCOL.compact.md)`) returned exit 0/no output: CONFIRMED. Appendix table byte diff command (`diff -u <(grep '^|' PROTOCOL-APPENDIX.compact.md) <(sed -n '493,526p' PROTOCOL.md)`) returned exit 1 with additions/removals: **CORRECTED/BLOCKER**, not byte-identical in the current worktree. Incident refs before the Appendix heading: body 1, single-file 1.

`sh verify-protocol.sh --selftest` returned usage and exit 2 because the committed checker requires a target argument despite its advertised selftest-only form. Running either candidate returned `verify-protocol.sh: line 439: SECTION_KEYS: unbound variable`, exit 1. This is a **BLOCKER** and means the exec record's 8-check findings and its claimed 10/8 selftest evidence are stale/unreproducible in the current checker. The two-file candidate was therefore not evaluable; no structural-artifact finding can honestly be distinguished from checker failure. The checker source itself advertises `--appendix`, but the executed `--selftest` path did not reach it.

## 5. Contradiction sweep

| incompatible claims | deciding command / observed | ruling |
|---|---|---|
| 526/49269 source vs current | `wc -l -c PROTOCOL.md` → 541/50603 | current 541/50603; old claim stale |
| 445/37535 body vs current | same wc → 459/38804 | current 459/38804; old claim stale |
| 479/46697 single-file vs current | same wc → 493/47966 | current 493/47966; old claim stale |
| expected 15/15 vs final 19/19 selftest | `closure-check.py --selftest` → 19/19 exit 0 | final 19/19 current |
| mutation 9/9 vs direct reproduction | no live mutant set supplied; only final prose | UNVERIFIABLE, do not accept as reproduced |
| appendix byte-identical | `diff` above exit 1 | false currently; blocker |
| gate clean/findings figures vs run | `sh verify-protocol.sh ...` → unbound `SECTION_KEYS`, exit 1 | old 8-check figures not reproducible |
| kake/kotoba/kagi untracked claims vs current | `git ls-files --error-unmatch` | current kake/kotoba/kagi report paths differ by row; kotoba and kagi r14 are tracked, correcting entry claims |
| live debt 20 vs older report debt 0/1 | live checker first line above | 20 is the current instant; older figures are pinned historical instants |

**Overall:** FAIL/BLOCKER. The artifact has independently reproduced the selftest, frozen figures, hashes, census, seed result, and report-byte observations, but the live worktree has changed beneath the drafted artifacts and the protocol checker currently fails before evaluating candidates. These are production-blocking citation/figure mismatches, not stylistic differences.
