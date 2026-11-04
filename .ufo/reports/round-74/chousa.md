# chousa — round 74

## Work performed

Declared **C1 operability** (lowest measured non-retired axis): repair the correction counter's actual Git loader. Frozen predicate: **LOADER_MATRIX=9/9 C1=PASS and the successor public CLI reports C2=PASS checks=7/7 on r73's committed landing**. Predicate met narrowly; **round not admitted under the current quality bar** because prefreeze detection-forger evidence required by QUALITY 126 was omitted. No calibration or capability claim, no retroactive admission of r73.

- Read r71–r73 rejected closures before choosing the fresh-start claim; r73 battery/preflight completion was not re-claimed. Source S182: `corpus/lessons/round-73-verifier-spotcheck.md:67`.
- Added a distinct successor changing numstat deletion orientation; historical r73 counter stays frozen. `corpus/evidence/round74/correction-count.py:131`; freeze `1eaa30ad248bbd3bd7469b2c17295fcda5fc02bb`.
- Exercised nine real committed Git fixtures through the public CLI/load path, not helper-only injections; before control 3/9, prefreeze positive 9/9. `corpus/evidence/round74/{loader-matrix.py,before-matrix.txt,positive-matrix.txt}`.
- Completed one v1 wave: **10 settled seats**, 3 executor, 1 scribe, 1 scout, 1 connector, 2 reviewer, 1 critic, 1 mutation-tester; 40% attack, L1 canonical planner, no residual. Main delivered WAVE-DONE before this report; `.ufo/waves/round-74/w1-results.json`. No dead seat reported. Configured routes all @m_zfl under the latest operational amendment; no model parameter supplied (`routing.txt`); actual answering model is not independently asserted.
- Integrated mixed-file/equal-line probes (7/7 expected outcomes), mutation kills (reversion 3/9; zero-deletions 5/9), source gates and reviewer limits. `.ufo/waves/round-74/w1/{R74ExecC,R74Mutation,R74Scribe,R74Review}.md`.
- **Surviving forge and admission defect:** R74Critic's invocation-order oracle scores 9/9 without reading sources; constants score 4/9, 4/9, 1/9. A matching digest identifies the reviewed successor but does not kill that forge. R74ReviewFreeze identifies the missing prefreeze QUALITY 126 battery. Neither finding is concealed or repaired by changing the frozen predicate. `.ufo/waves/round-74/w1/{R74Critic,R74ReviewFreeze}.md`.
- Mined r73 loader/test-path mistake into QUALITY 134 and disclosed this round's prefreeze omission. `corpus/lessons/round-74.md`, `corpus/QUALITY.md:1026`.

Stale-lane: respawn-per-round; no other mission of this lane is open. Tool installs/updates: none. No external fetch, source-tree mutation or sibling-domain absorption. Open carried operator questions: fetch approval, historical Windows flock/load questions, SHONEN promotion and non-author entailment review; none presumed answered or newly filed. No inherited uncommitted lane work at start (`jj-lane.sh state`: tracked=0 untracked=0). Fleet misroot sweep found no identified chousa-r74 seat file; ambiguous fleet `after` contained only `== SCORECARD diff base-` and was left untouched, as were orchestrator `.scratch/` files (`fleet-misroot-sweep.txt`).

## Landed changes

- Freeze/controls: **1eaa30ad248bbd3bd7469b2c17295fcda5fc02bb**, named by `LOG.md` Round 74 Action entry.
- Integrated evidence, source rows S182/S183, lesson, QUALITY 134, gate registration, SCORECARD and corpus index: **5f754bd12ec5d0d006ca05751250d5ee1caaf29e**, `LOG.md` Round 74 and its Outcome subsection. No capability row or numeric score increase.
- Final pre-report remote gate: `git -C /home/vgpnk/Projects/shokunin/chousa-shokunin ls-remote origin refs/heads/master` → `5f754bd12ec5d0d006ca05751250d5ee1caaf29e refs/heads/master`, exit 0. Both commits produced helper `landed` lines.

## Before → after measurements

Instrument revision: **1eaa30ad248bbd3bd7469b2c17295fcda5fc02bb**. Measurement receipts land in **5f754bd12ec5d0d006ca05751250d5ee1caaf29e**; frozen instrument bytes were digest-compared with their committed blobs after all seats settled. Successor SHA256 `9334721a5e7a4080255b478771bf5443739738fb1936b40c116da28d7fa8ac41`.

Run from lane root, with an existing scratch work directory:

```sh
python3 -B corpus/evidence/round74/loader-matrix.py --counter corpus/evidence/round73/c2-count.py --work /fast/scratch/hyaku/chousa-r74/L1
# LOADER_MATRIX=3/9 C1=FAIL; exit 1 (before-matrix.txt)
python3 -B corpus/evidence/round74/loader-matrix.py --counter corpus/evidence/round74/correction-count.py --work /fast/scratch/hyaku/chousa-r74/L1
# LOADER_MATRIX=9/9 C1=PASS; exit 0 (after-matrix.txt)
python3 -B corpus/evidence/round73/c2-count.py --lane . --base f748abbb6bf58388e732facd4ecec5612419c457 --rev 5aec90775fc7cc1fe9ad442e0d5491731323eec1
# C2=FAIL checks=6/7; exit 1 (before-historical.txt)
python3 -B corpus/evidence/round74/correction-count.py --lane . --base f748abbb6bf58388e732facd4ecec5612419c457 --rev 5aec90775fc7cc1fe9ad442e0d5491731323eec1
# C2=PASS checks=7/7; exit 0 (after-historical.txt)
```

Receipts: `corpus/evidence/round74/`. Matrix checks exit plus exact failed-check set. The historical CLI's C2 label is inherited; it is **not** a second round claim. C1 improves on its fixed predicate; historical numeric operability stays 3/10 (delta 0). Other axes unchanged. Limits: nine text cases, inherited substring semantics, nonnumeric fallback not covered by frozen matrix, invalid-UTF8 binary diagnostics, order-oracle forgery. No general robustness or truth/entailment claim. Full research-gate battery/preflight not rerun.

## Sources & frontier

Registry rows **181 → 183**, exit 0 on both counts. Counting command (before: pipe `git show 8a28732b3c1591b52449a982849b758cda6f4c45:corpus/SOURCES.md`; after: pipe `cat corpus/SOURCES.md`):

```sh
python3 -c 'import sys,re; print(sum(bool(re.match(r"^ {0,3}\|\s*S\d{3,}\s*\|", x)) for x in sys.stdin))'
```

`.ufo/waves/round-74/source-counts.txt` records code/results. Added B=1 (S182 mined), C=1 (S183 rejected), A=0. Tier totals A123/B45/C13 → A123/B46/C14; statuses mined147/queued19/rejected15 → mined148/queued19/rejected16. No existing status/recheck/used-by cell touched. Gate records own-work paths, pinned revision, access date 2026-11-04 and located ≤25-word quotes. Frontier coverage rows advanced: 0; no knowledge entry or new capability. Assimilation: none; latest considerthese opened, no independent proposal uptake or package adoption.

Required census command, run at both ends:

```sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin chousa
```

Before (`census-start.txt`, exit 0):
```text
chousa W04 S051 duplicate url www.w3.org/TR/2017/REC-html52-20171214/syntax.html across scopes
chousa W04 S053 duplicate url docs.python.org/3/library/socket.html across scopes
chousa W04 S073 duplicate url www.gnu.org/software/coreutils/manual/coreutils.html across scopes
chousa W04 S074 duplicate url docs.python.org/3/library/hashlib.html across scopes
chousa W04 S075 duplicate url www.gnu.org/software/coreutils/manual/coreutils.html across scopes
chousa ok /home/vgpnk/Projects/shokunin/chousa-shokunin/corpus/SOURCES.md
```
After (`census-end.txt`, exit 0):
```text
chousa W04 S051 duplicate url www.w3.org/TR/2017/REC-html52-20171214/syntax.html across scopes
chousa W04 S053 duplicate url docs.python.org/3/library/socket.html across scopes
chousa W04 S073 duplicate url www.gnu.org/software/coreutils/manual/coreutils.html across scopes
chousa W04 S074 duplicate url docs.python.org/3/library/hashlib.html across scopes
chousa W04 S075 duplicate url www.gnu.org/software/coreutils/manual/coreutils.html across scopes
chousa ok /home/vgpnk/Projects/shokunin/chousa-shokunin/corpus/SOURCES.md
```

Tabs rendered as spaces above; raw output plus EXIT markers is committed under `.ufo/waves/round-74/`. Mistake fix shown able to fail by the unchanged r73 counter (3/9). Independent non-author spot-check of S182 admit/S183 reject remains requested; wave seats do not satisfy it.

## Trend verdicts

- **expansion: unchanged** — no new knowledge, capability or coverage-map advance; registry curation alone is not expansion.
- **quality: improved** — narrowly: real numeric loader defect repaired and public-path outcomes remeasured; surviving matrix weakness explicitly marked rather than admitted as sound. `after-matrix.txt`, lesson integration section.
- **discernment: improved** — r73 disagreement becomes grounded QUALITY 134 with red-before evidence; outside admit/reject agreement is still pending. The current prefreeze omission is explicitly retained, not claimed fixed.

No scalar learning verdict. **Admission withheld/not admitted** due QUALITY 126 prefreeze noncompliance, notwithstanding the measured narrow C1 result; canonical closure owns the final ruling.

## SHONEN

- [~] Decision tables, error patterns, checklists and cited sources: `SKILL.md:13–77`, Gates registry; lane assertion, no non-author promotion verifier.
- [~] End-to-end task executed/logged: `LOG.md` Round 74; actual historical correction verification and `corpus/evidence/round74/after-historical.txt`.
- [~] Executable without oral context: frozen `corpus/evidence/round74/claims.md` and CLI matrix; scope/forgery limits explicitly disclosed.
- [~] No cross-domain bleed: unchanged `PROVINCE.md`; `.ufo/waves/round-74/w1/R74Connect.md`; lane assertion, no non-author promotion verifier.
