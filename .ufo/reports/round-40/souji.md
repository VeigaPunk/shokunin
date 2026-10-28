# souji — Round 40 (attempt 3)

## Work performed

**Declared claims:** C1 — calibration, evidence-bound closure lines and strict-descendant register rows; C2 — operability, wrapped docstring refusal-class entries; C3 — coverage, multiple TOTAL rows, `--skip-unrecorded`, and invalid-UTF-8 record branches. The frozen preregistration is `souji-shokunin/census/round-40/preregistration.txt` (base `0242085909fb6a4ee041c5443d76316ac6d59d4b`). All three were measured, but none is admitted: their scope/baseline inputs were not fully frozen before seat scoring (details under measurements and `corpus/lessons/round-40.md` M40-3–M40-13).

- **C1 calibration:** landed an evidence-pointer counter, strict-descendant register checks, evidence-content comparison, and separate forged controls. Final receipt: `souji-shokunin/census/round-40/records/c1-after-h.txt`; 11-case fixture: `souji-shokunin/tests/fixtures/r40-c1-evidence.py`. The counter validates three rows (D1-D3), not the prior 16-item routed set; D2's evidence depends on a C2 receipt, so the measured C1 set is not causally separable. Wave-2 `R40w2critic02.md` and `R40w2critic03.md` independently demonstrate the coupling and false-value risk; the latter was hardened after wave data, so it does not retroactively admit the frozen claim.
- **C2 operability:** landed a continuation-line reader and a seven-leg counter, with a joined-vs-one-line control (`census/round-40/records/c2-after-h.txt`, `tests/fixtures/r40-docstring-joined.py`). W1/W2 found that the finite class/trigger set, probe bytes, join grammar and runner conditions were not frozen before dispatch; the counter tests 3 of 10 refusal classes. See W1 `R40sentinel11.md`, `R40sentinel23.md`, `R40executor14.md` and W2 `R40w2critic04.md`.
- **C3 coverage:** landed an eight-case record fixture and four-mutant battery (`census/round-40/records/c3-after-h.txt`, `tests/fixtures/r40-drift-record-branches.py`). W2 found the base-fixture wording ambiguous, the fixture misses prior-round regression cases and several mutants, and the tool accepts a first-disagreeing/last-agreeing TOTAL sequence contrary to its docstring. See `R40connector09.md`, `R40connector33.md`, `R40reviewer54.md`, `R40w2critic07.md`, `R40w2critic08.md`, and M40-4/M40-12/M40-13.
- Curated sources, re-opened W2 quote/scope findings, mapped correction entries and mined mistakes: `corpus/SOURCES.md`, `corpus/README.md`, `corpus/knowledge/`, `corpus/QUALITY.md`, and `corpus/lessons/round-40.md`.
- Dispatched two v2 waves; the L1 held the frozen-topology planner seat as required. All wave inputs/results and seat outputs are captured in `census/round-40/waves/`.

## Landed changes

Every lane change is recorded by the Round 40 append-only entry in `souji-shokunin/LOG.md:1901-1911` and carried by a lane commit:

| change | commit |
|---|---|
| C1/C2/C3 instruments, fixtures, preregistration, initial source entries and lessons | `128e412b0ced3c243dc27c3dd3332054a611bc2e` |
| C2 committed-analyzer loading / C3 attribution fixes | `8a5fbdbddaab24c5ba43fc6a133499efb405f214` |
| first instrument receipts | `6ded1248b6d0005ac31ff2e1c867ecb0a075ab39` |
| QUALITY Q89-Q92 | `556c24a5cacf208c5144c459838712594a43e1f2` |
| C1 item inventory, forged set, register and closure lines | `549d9ec53a1f5932337ff14438fcd22b0621828d` |
| C1 path-bound evidence hardening | `994de3b447e9a7bea2abfbd80c4736f6215d3e47` |
| W1 capture, C1 evidence-content/input binding and W1 lessons | `42e18ed77e7b7e856815139cfa568479b7f54983` |
| C1 evidence-byte/nonempty-forgery checks; C3 `--base-rev` fixture read | `dc8bd47c693097a69ccaa39b514ce9689a642edc` |
| W2 capture, S255-S257 source corrections, assimilation corrections, final census | `d86ef3ea8a4504d31f07ad5b660fdac5c932e5c5` |
| final receipts, Scorecard and LOG | `bffcc0f660ff36eb8add3f61582748a7af019a5b` |

The L0 assimilation-collision correction was committed/pushed in the fleet repo at `a8663a8969056186993b0de08ce6bda46b8ff009`; the earlier protocol-authored L0 line remains unchanged as history.

## Before → after measurements

| claim | before | after | counting command | measured commit / verdict |
|---|---|---|---|---|
| C1 — calibration | `SUMMARY items=3 open=3` at the frozen base; the r39 token-only control closes (`ITEM FORGE-TOKEN CLOSED`) | At final instrument revision `dc8bd47`: `items=3 open=0 forged=3 forged_open=3 forged_closed=0 register_mismatches=0 register_violations=0`; fixture `cases=11 pass=11` (`c1-after-h.txt`) | `python3 -B census/round-40/c1-counter.py --root . --rev <full40> --items census/round-40/c1-items.tsv --forged census/round-40/c1-forged.tsv --register census/round-40/cells.tsv --min-cells 3 --min-commit-rows 3 --scratch <scratch>` | `dc8bd47c693097a69ccaa39b514ce9689a642edc`; **unprovable** against the prior 16-item population and independent-claim requirement (M40-5/M40-6). D1's 178-row receipt predates the final S255-S257 source append (M40-10). |
| C2 — operability | one-line control `SUMMARY cases=9 pass=6 fail=3` | joined fixture `9/9`; counter `SUMMARY legs=7 pass=7 fail=0 harm=0` (`c2-after-h.txt`) | `python3 -B census/round-40/c2-counter.py --root . --rev <full40> --base-rev 0242085909fb6a4ee041c5443d76316ac6d59d4b --scratch <scratch>`; `python3 -B tests/fixtures/r40-docstring-joined.py [--one-line]` | `dc8bd47c693097a69ccaa39b514ce9689a642edc`; **unprovable** because the observed pair set, probe, join grammar and runner preconditions were not frozen before data (M40-3). |
| C3 — coverage | r39 fixtures did not assert the three named branch families; r40 base arm reports new mutants survive (`base_killed=0`) | `mutants=4 killed=4 survived=0 pristine=ok base_killed=0 cases=8` (`c3-after-h.txt`) | `python3 -B census/round-40/c3-counter.py --root . --rev <full40> --base-rev 0242085909fb6a4ee041c5443d76316ac6d59d4b --scratch <scratch>` | `dc8bd47c693097a69ccaa39b514ce9689a642edc`; **unprovable**: the frozen phrase “r39 base fixture” admits two identities, the counter's four mutants do not preserve r39's four regression mutants, and additional branch mutants survive (M40-4/M40-12/M40-13). |

These are measured instrument outputs, not admissions. C1 measured three rows, not all 16 prior routed items; the item population was not enumerated by the preregistration. C2's three selected pairs do not cover all ten refusal classes the tool can raise. C3's four declared mutants pass, but the frozen base and full branch contracts were not made falsifiable before data. Owned scores remain unchanged (calibration 7, operability 8, coverage 8); no score mapping exists.

## Sources & frontier

Census command (both ends):

```sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin souji
```

- **Before:** `souji ok` for `corpus/SOURCES.md`, exit 0; 174 source rows, W04=48 (`census-before.txt`, round-start census and base-tree row count).
- **After initial source append:** 178 rows, W04=49, exit 0 (`census-after.txt`; this receipt is historical and predates the W2 corrections).
- **Final:** 181 rows, W04=52, exit 0 (`census-final.txt`; final command output is preserved there).
- **Rows added by tier:** S251-S257, all tier A / `mined` (7 rows). No old row's `status`, `recheck`, or `used-by` cell changed in place; S255-S257 are append-only corrections superseding the quote/scope defects in S252-S254.
- **Frontier:** no F1/F4 status change and no ground moved to Core. F1/F4 remain frontier; the added entries are on already-held grounds.
- **Assimilation:** one staged theme from `/home/vgpnk/Projects/shokuknow/merge/souji/` (GVFS `trashlib` reader; staged entry `origin-record-format-gvfs-r26.md`). The collision sweep found 58 overlapping IDs, 55 different-document overlaps and 3 same-document overlaps; staged S146 itself is free in the live registry. Lane S254 was the next unused ID, not an arithmetic repair. W2 found the read-side material is corroborative on held F4 ground; no expansion credit is claimed. The append-only L0 correction is committed at `a8663a8969056186993b0de08ce6bda46b8ff009`.
- `considerthese/` is absent from this lane; no proposal was mined.

## Trend verdicts

- **expansion — unchanged.** Seven rows and correction entries were added, but F1/F4 were already held and no coverage-map ground moved to Core (`corpus/README.md` Round 40 frontier update; `corpus/SOURCES.md` S251-S257).
- **quality — improved.** W2 found quote/scope and evidence-instrument defects; exact source corrections S255-S257 and QUALITY Q89-Q97 were added and the contradictory/unfrozen parts were recorded as honest stops (`corpus/lessons/round-40.md` M40-3–M40-13; `corpus/QUALITY.md` Round 40 criteria). The remaining TOTAL-docstring/runtime discrepancy is explicitly disclosed, not called clean.
- **discernment — unprovable-but-better.** The round converted W1/W2 disagreements into 13 lesson entries and Q93-Q97, but W1/W2 seats are lane-dispatched, not an independent non-author spot-check. No outside verifier is claimed; evidence is in `corpus/lessons/round-40.md` and `corpus/QUALITY.md`.

## Stale-lane

Stale-lane: respawn-per-round driver; no other mission of this lane is open; round 40 was progressing through its recorded commits.

## SHONEN

- [~] SKILL.md contains decision tables, error patterns and checklists — `SKILL.md` §§Receipt taxonomy / Decision tables / Error patterns / Checklists; `corpus/SOURCES.md` S100-S103.
- [~] End-to-end domain task executed and logged — `LOG.md:1901-1911`; this round's counters/fixtures are measurement work, not deletion authority.
- [~] Instructions executable without oral context — `census/round-40/preregistration.txt`, `census/round-40/c1-counter.py`, `census/round-40/c2-counter.py`, `census/round-40/c3-counter.py`; no promotion check is claimed.
- [~] No cross-domain bleed — `PROVINCE.md` and W2 sibling-overlap scan `census/round-40/waves/w2/R40w2connector02.md`.

## Round shape, seat accounting, and deviations

- **Actual shape:** two v2 waves, W1=64 and W2=64, 128 seats total (inside the run-11 64-128 band); W1 was inherited from attempt 1, its ready file was not rewritten, and the orchestrator rebound delivery to SoujiR40a3. This two-v2-wave shape is not one of the prompt's two canonical shape choices (one v2 wave or two v1 waves); it is reported as dispatched, not normalized after the fact. No residual task call.
- **W1 role mix:** executor 14, critic 9, scribe 6, scout 5, reviewer 5, mutation-tester 5, connector 5, simplifier 5, sentinel 5, revenger 5; attack roles reviewer+critic+mutation-tester = 19/64 (29.7%); connectors 5. W1: 64 settled, 56 report files; eight results-only seats: R40executor01/02/03, R40scout05, R40executor13/15, R40revenger24, R40scout29. The W1 handoff records no dead-seat error text; results are captured in `census/round-40/waves/w1-results.json`.
- **W2 role mix:** critic 13, reviewer 12, executor 8, mutation-tester 7, sentinel 6, scribe 4, revenger 4, simplifier 4, scout 3, connector 3; attack roles reviewer+critic+mutation-tester = 32/64 (50%); connectors 3. W2: 64 settled, 61 report files; R40w2reviewer01 and R40w2reviewer04 died with `Codex error event: Invalid prompt: your prompt was flagged as potentially violating our usage policy`; R40w2mutationtester01 completed without a report after an inconclusive pristine-only run and did not remove its scratch. Full result accounting is in `census/round-40/waves/w2-results.json`.
- L1 held the planner seat per the frozen-topology ruling. The floor roles (connector, executor, scribe, scout, reviewer, critic) appear in both waves.
- **Misroot sweep:** `git -C /home/vgpnk/Projects/shokunin status --porcelain` was run with no pathspec before report; it showed other lanes' `.scratch/`, `lane3/`, and `tools/` artifacts but no untracked souji-round-40 seat note. None was moved or deleted. Lane `jj-lane.sh state` is clean at `bffcc0f660ff36eb8add3f61582748a7af019a5b`; `ls-remote origin refs/heads/master` matched that hash.
- **Disk guard:** `disk-guard.sh status` reported `/tmp` 21% (101.9G free) and `/fast/scratch/hyaku` 52% (386.0G free); the status command timed out while enumerating top consumers (exit 124). No ENOSPC death was reported by either wave. Round scratch was removed after landing (see final handoff).
- **Stale-lane:** respawn-per-round driver; no other mission of this lane is open; round 40 was progressing through the recorded commits above.
- **Tools installed/updated:** none. Pacman stayed paused.
- **Attribution note:** the lane's `SCORECARD.md`, `LOG.md`, corpus and evidence commits use the souji identity via `jj-lane.sh`; the L0 line was already present in the fleet HEAD with protocol attribution before the helper call returned `nothing to commit`, and the later correction is a souji fleet commit. This is disclosed, not rewritten.
