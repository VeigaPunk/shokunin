# kotodama — round 50 (hyaku, attempt 1)

## Work performed

Declared claims (frozen in `reports/round-50/claims.json`, base **4ad26836552462d28a946ca3b067cab0b5ce3532**): **C / coverage** — one pastoralism/animal-husbandry production-register entry; **O / operability** — jj-colocation-safe receipt and README-revision gates; **Ca / calibration** — detect the round-49 separability mistake with a checker and QUALITY criterion 7.

**Author-side outcome: NOT ADMITTED as declared.** C's coverage measurements and O's bounded operational tests improve. Ca detects the historical pair, but its frozen self-application command exits **2**, not 0; the runner silently measures a different manifest. The substitute manifest's clean result also misses the real dependency on the round lesson's Gate. These are reported, not redefined away. Driver completion is not admission; independent closure remains required.

- Added `corpus/knowledge/culture-material/pastoralism-animal-husbandry.md` and its filename-ordered README row; 225→226 knowledge files, culture-material 27→28, 204-line entry, 22 cited source rows. Source re-openers and all section reviewers are durable in `.ufo/waves/round-50/falsify/`; scope/anchor/calibration corrections landed in `c8865c7` and `1923bfe`.
- Extended `tools/harness/receipt_guard.py` from HEAD-only detection to branch/remote refs, with distinct landed identity. Final controls include symrefs escaping the protected namespaces and jj's virtual-root HEAD (71/71). `tools/check-readme-revisions.py` fails closed on an unavailable pin and bounds upward git discovery (15/15). Evidence: `reports/round-50/validation.json`, `telemetry/jj-probe-v3.txt`, and falsify `ReviewGuardCode.md`, `ScoutJjLive.md`, `ReviewReadmeRevCode.md`.
- Added `tools/check-claim-separability.py`, the frozen r49 fixture, and QUALITY criterion 7 grounded in the outside r49 disagreement. Its 56/56 selftest and historical C→S finding hold; its own-round acceptance does not establish the declared claim. Evidence: `falsify/CriticR50Manifest.md`, `ReviewSepTool.md`, `ReviewCriterion7.md`, `ReviewSepFixture.md`, `telemetry/final-conformance.json`.
- Curated S048–S069 and appended S070 correcting S060's bibliography; mined mistakes R50-M1…M9 and retained unresolved findings rather than suppressing them. `corpus/lessons/round-50.md` includes the final reconciliation and conformance defects.
- Reconciled the lessons index: 36 rows / 36 files, findings 3→0; selftest 28/28. Evidence: `corpus/lessons/README.md` revision 5 and `reports/round-50/telemetry/final-conformance.json`.

## Landed changes

Final lane tip: **8c128fc8b1e303201706cdd61778379b194af1ab**. Each hash below was returned by the lane helper's final `landed` line; all are ancestors of the final tip.

| Landed hash | Work | LOG linkage |
|---|---|---|
| `1c779e4a316efcbfbcba54cb8b2a1e0dda2353d0` | Inherited build landing: entry/index, S048–S069, gates/probe/checker, QUALITY criterion 7, build-wave evidence | `LOG.md` round-50 Trigger, C/O/Ca bullets |
| `c8865c738408e5e48a0a37dd2e4eff22a103cf03` | Post-falsify C corrections; S070; guard symref/jj-root repairs; README-revision discovery ceiling; probe v3; committed runner word-boundary correction; falsify evidence | `LOG.md` round-50 C/O bullets |
| `1923bfe2a215cd470d905cfd42d9984f41e3ed9d` | Final §2/§5/§10 neighbour, lexicon and ritual corrections; **measurement revision** | `LOG.md` round-50 Final entry reconciliation |
| `8c128fc8b1e303201706cdd61778379b194af1ab` | Complete 139-seat records; validation/provenance/census receipts; SCORECARD/LOG/SHONEN; lesson and index revision 5 | `LOG.md` round-50 Evidence/Frontier bullets |

At handoff the helper reported local=remote=`8c128fc…`, ahead=0, behind=0, tracked=0, untracked=0. `snapshot.auto-track` was observed as `none()`; no ignored PDF scratch was tracked.

## Before → after measurements

Measured base **4ad2683** and work **1923bfe** in fresh clones under `/fast/scratch/hyaku/kotodama-r50/`. Commands below are reproducible against those pinned revisions; scratch paths are not permanent evidence. Committed outputs are `reports/round-50/validation.json` and `measurement-provenance.json` (base/work hashes, runner/probe/tool/entry/source SHA-256 values, receipt hash).

Common runner:

```sh
python3 -B <after>/reports/round-50/run-validation.py --tree <after> --base-tree <before>
```

Observed exit **0**, `acceptance_passed: true`; this is the runner's narrower acceptance, **not** admission of every frozen clause.

| Claim | Counting/test command | Before → after and verdict |
|---|---|---|
| C / coverage | `find corpus/knowledge -name '*.md' \| wc -l`; `ls corpus/knowledge/culture-material/*.md \| wc -l`; `python3 -B reports/round-28/readme/sweep.py` | 225→226; 27→28; sweep rows/files 225/225→226/226, topic_mismatch 0 both, exit 0. Entry 204 lines, 1 H1, 0 H3, ordered eight-field head, 22 source IDs resolved. **Measured coverage improvement**; residual content/commissioning limits below remain disclosed. |
| O / operability | `python3 -B reports/round-50/jj-colocation-probe.py --tools-root <tree>`; gate `--selftest` commands | Probe v3 false negatives **3/3→0/3**, false positives **0/4→0/4**; guard controls **45→71**, 71/71 pass; README-revisions **11→15**, 15/15 pass. **Improved within the exercised cases.** |
| Ca / calibration | `python3 -B tools/check-claim-separability.py reports/round-50/separability/r49-fixture.json`; `--selftest`; **declared:** `... reports/round-50/claims.json` | Known r49 pair detected **0/1→1/1**; fixture exits 1 with six findings including C→S; selftest 56/56. **Declared self-application fails: exit 2, `manifest is missing base, schema`. NOT MET as declared.** |

Instrument history is retained: v1 scored the build tools 1/3; predecessor v2 relaxed R1 to accept a remote ancestor (0/3), defensible against the declared wording but vulnerable to fake labels. Falsify-driven v3 requires exact `origin/main` tip identity plus refusal, using a receipt-free base and two local commits. Base remains 3/3; build and repaired tools remain 0/3; fake `<HEAD^>` and `<root>` labels are flagged (1/3). See all three `telemetry/jj-probe-v*.txt` files.

The build commit's runner still matched `herd` inside `sherd`, causing C's before-check to fail; the predecessor's passing receipt used uncommitted code. The existing correction was inherited, re-verified and landed in `c8865c7`; the final receipt was regenerated with committed runner bytes at `1923bfe`.

No numeric expertise score is manufactured: the lane retains its historical uncalibrated-score-rubric conformance gap. Freshness is the historically lowest axis but its round-11 L0 pause remains; coverage is the lowest claimable axis per the frozen declaration.

## Sources & frontier

Same census command at start and end:

```sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama
```

Before (inherited `telemetry/census-before.txt`, independently corroborated by the base clone and `falsify/ScoutCensusAfter.md`):

```text
kotodama ok /home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md
exit=0
rows=47; A=34 B=6 C=7; mined=20 queued=22 rejected=5
```

After (`telemetry/census-after.txt`):

```text
kotodama ok /home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md
exit=0
rows=70; A=51 B=12 C=7; mined=42 queued=23 rejected=5
```

- Added **23 rows**: A=17, B=6, C=0. S048–S069 enter mined, used-by the new entry; S070 enters queued, used-by `—`, and its teaches opens `supersedes S060 —` (Crossref page metadata 165–181).
- No pre-existing row's status/recheck/used-by changed. The preamble Gate pointer was corrected for S044–S047 and extended through S070; old→new is in the lesson.
- Every new row has its URL/date/located ≤25-word quote under the lesson's Gate; all 22 original quotes were re-opened by the falsify source seats, with route limitations recorded. Source tiers were scoped rather than globally assigned; no tier-inflation defect was found by the source-conformance reviewer.
- The pastoral production-system frontier moved into the coverage map. Mined mistake: the outside r49 separability disagreement produced QUALITY criterion 7 and a checker shown able to fail on r49; the checker is explicitly not treated as sufficient for this round's self-admission.
- **Frontier conformance defects retained:** the round-50 search-log note lacks identified/screened/excluded counts and stop rationale; several registry locators/access claims need superseding rows (S050/S052/S054/S064 and S065 teaches precision). S070 does not silently rewrite S060. See `falsify/ReviewSourcesConformance.md`, `ReviewLessonGate.md`, and lesson final reconciliation.

## Trend verdicts

- **expansion — improved (bounded author assessment):** one new sourced register on previously unowned ground, 225→226 entries; C's structural counts reproduce. This is not a declaration that all commissioned prose targets passed: the ≥15-neighbour table target remains unmet at 11, and the lesson records remaining boundary/calibration concerns.
- **quality — unchanged:** new-entry source/scope repairs and gate improvements landed, but no claim is made that an older weaker knowledge entry was superseded or stale corpus knowledge re-verified. Retained registry/measurement limitations prevent a broader quality claim.
- **discernment — improved, pending independent closure:** the outside r49 disagreement became a lesson-grounded criterion and a demonstrably rejecting control. This round also refuses its own false-green Ca self-application. Author-dispatched review seats are still author-lane evidence, not the required fresh outside admit/reject spot-check.

The runner found no measured regression on its tested surfaces; wider no-harm/separability is **not established** by its green result. Admission is withheld for Ca and the disclosed coupling, rather than averaging the improvements.

## SHONEN

- [~] Real decision tables/error patterns/checklists with sources — `SKILL.md:20,468,522`; `corpus/SOURCES.md`; no named non-author promotion verifier.
- [~] End-to-end domain task executed/logged — `LOG.md` round-50 entry, new entry, source-opening/falsification evidence, `reports/round-50/validation.json`.
- [~] Executable without oral context — committed wave prompts, pinned clone replay and SCORECARD round-50 commands; Ca's invalid command is explicitly disclosed rather than claimed executable.
- [~] No cross-domain bleed — `PROVINCE.md`, entry §2/§15, connector reports; lore still owns canon. No promotion claimed.

### Resume, swarms and conformance

Replacement coordinator: **KotodamaR50-2**. Predecessor: **ChousaR27R2 (reused idle agent; Main spawn job-capped)**. Its earlier chousa-overlap seats are excluded by kotodama's assignment receipts.

- **Inherited and re-verified:** build landing `1c779e4`, 73 build reports/receipts, gate/checker fixtures and patches, source rows/quotes, entry/index; inherited runner word-boundary edit; prevalidated 66-seat falsify payload. Fresh-clone replays, all-row reopens, section reviews and mutation reports supply the re-verification.
- **Discarded/replaced:** the uncommitted predecessor validation output was regenerated from committed final bytes, not accepted by timestamp; six executor work clones (510 MB) were disposable scratch whose patches already landed and were removed; the stale fixture-pin lessons-index patch was not applied. Build evidence is retained, including conflicting findings.
- **Build wave (inherited): 73 seats** — executor 6, reviewer 12, critic 5, sentinel 1, revenger 3, connector 3, scout 27, scribe 16. Three cap-refused calls preceded its successful dispatch; 73/73 reports.
- **Falsify wave (post-crash dispatch of predecessor's unspent validated payload): 66 seats** — scout 27, reviewer 24, critic 7, sentinel 1, mutation-tester 3, connector 2, simplifier 2. 66/66 reports. Assignment map/recording receipt and registry are committed.
- **Total 139 dispatched seats; dead/report-less seats: 0 (none to name).** No dead seat was replaced. Refused calls spent zero seats. L1 holds the canonical planner seat; it is not a validator role. No model parameter or routing/configuration edit was used; seats retained captured provider histories. No provider deaths were observed.
- **Retry defect:** predecessor falsify attempt 1 was refused; replacement attempts 2–20 fired within about one second because of a loop bug, all 66/66 refused. Attempt 21 also refused, only ~72 seconds after that burst; attempt 22, 180 seconds later, spawned 66. The append-only attempts file and annotation disclose this violation of the ~3-minute cadence; successful dispatch does not erase it.
- **Load-order defect:** the replacement read the shokunin/swarm bindings and required jj trial/audit after dispatch, not before as required. Later reads are not a repair of that process breach.
- **Misroots:** SimplifyGuard and SimplifySepTool reports were copied byte-exact from fleet `.ufo/waves/round-50/falsify/` to the lane, verified with `cmp`, and fleet copies removed. Final no-pathspec fleet status contained only operator/runtime changes; no owned misroots remained.
- **Other residuals:** checker relative-path blind spot, incomplete export range/shared-land attribution, mutation/acceptance-vacuity gaps; guard remote-holder ambiguity and uncovered namespaces; selftest mutant survivors; README sweep duplicate/order blind spots. Full evidence and dispositions are in lesson final reconciliation and the 66 falsify reports. They are not silently fixed by narrowing frozen targets.
- **Tools:** no installs or upgrades by coordinator/seats. `snapshot.auto-track=none()` observed; commits used only `jj-lane.sh`; the report uses only `fleet-commit.sh`. All round-owned heavy scratch under `/tmp` (`k50-*`, `kr50-*`), lane wave `work/`, and `/fast/scratch/hyaku/kotodama-r50/` was removed after evidence was committed. Unrelated ignored historical scratch was untouched.
- **Stale-lane:** this held round exceeded two driver ticks but was progressing through lane-authored commits and seat reports; no other kotodama mission is open. No r51 dispatch, claim mutation, state advance, or MANIFEST edit was performed.
- **Open L0:** existing kotodama round-11 “drift-recheck threshold calibration” remains unruled and freshness remains paused. Historical lore intake/digest questions remain outside this round; no new operator decision was required or asked.
