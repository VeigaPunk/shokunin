# Tameshi round 24 — frozen hardening predicates, fresh falsification and bounded verdict

## Work performed

**Declared C1 — calibration (tied lowest owned axis): harden required-command binding against eleven named predicates.** The frozen counter moves **1/11 → 11/11**; K4 was already caught at base, so ten predicates actually move. Numeric calibration remains **8→8, delta 0**. This is not a general mutation-adequacy, producer-authentication, historical R17 command-coverage or promotion claim. C1 verifies against the frozen contract; broader end-to-end replay hardening does **not** follow. Independent closure still decides admission.

Paths below are lane-relative under `/home/vgpnk/Projects/shokunin/tameshi-shokunin/`, unless explicitly called fleet paths. Frozen contract: `.ufo/evidence/round-24/contract.json`; counter: `measure.py` in that directory, SHA-256 `0a7f6daa7ddaa0ef0b4140c20f5e3eef91b781f2d3119e1819c83191e57daa64`.

### Resumption and inherited work

The held claim remained round=24, attempt=1, base=`6a1821a8897eea6e7d9669292160ec9593669409`. The author/coordinator **CloseTameshi22** died with session `01a15c83` (SIGHUP, 2026-10-21 13:10:51 -03), inside its dispatch retry loop. **TameshiR24-2** is the replacement writer for that same claim. No claim was advanced, no dead seat was revived or replaced, and round 25 was not started.

Inherited, re-verified and retained:
- Freeze commit `e338f1bd0749a1786d95d3d3cd9572bb10757667`: contract, ruler and before receipt. Fresh RunRulerBase reproduced the before stdout byte-identically: 1/11, exit 1. ResAfterRuler independently verified unchanged ruler bytes and after-output fidelity, with only the three generated K11 temporary paths differing.
- Implementation `d2eaecd443bf5f4e387e7e5331282e3d11dea047`: supplemental fixtures, the fixture loader, successor `tools/registry-replay.py`, three registry supersessions/four new active rows, source rows S084/S085 and corpus additions. RunSelftests reproduced 44/44 and 10/10; PredK1–K6 inspected attribution; MutPins attacked the two registry pins. Tool production comparisons themselves were already exact at base; K1–K3 strengthen the fixture suite, not those comparisons.
- Actual replay `bd38c02a8b74752accaf88089c8c17024b2ab893`: 43 frozen round23 requirements replayed at d2eaecd, all held; gate exit 0/`[]`, bundle digest `4f4240230d4faecb54f488bb0d889de472e4e3f97e693e9304288429a722a9c6`. RunReplayGate reproduced the verdict and both older pinned bundle rows. RowAudit01–08 audited all 43 stored rows; RevRunnerHash verified the hash of the clone runner that actually executed.
- Re-anchor `c8c5b88c8e961a929cdc351b95a7074c76958909`: fifteen actual traced source reads and preserved ledger prefix. RunMonitor reproduced 62/62, restraint 8, depth 8. These are author source reads, not blind cold-read, recipe execution or independent promotion evidence.
- Untracked inherited wave directory: the validated `spec1.json`/`task-call1.json`, validator outputs, generator and two refusal receipts. The validated taskCall was dispatched unchanged on replacement attempt 3; the generator is retained as historical scaffolding for the already-dispatched evidence, not re-executed or treated as validation authority.

**Discarded/not credited:** the dead session's unfinished retry process; its unretained working-tree after run (replaced by actual fresh receipts); a failed final measurement attempt whose receipt writes hit ENOSPC on `/tmp`; and RevLiveRows' assertion that a kagi pin was pruned. That assertion used mistyped `feece8743`; actual `fecee874` resolves to a reachable commit. The underlying hidden live-sibling dependency remains real.

### What the eight deferred repairs actually became

The disposition is not “all eight repaired.” See the appended knowledge-entry table and lesson Errata E–P plus residual corrections.

| Routed round23 item | Round24 result |
|---|---|
| argv name-insensitive/swap-name mutant | K1 now killed by the public selftest |
| negative-exit mutant | K3 named mutant now killed |
| two bundle-digest registry pins | K5/K6 substitutions stop holding; pristine controls hold |
| dropped held/cleanup/external metadata | successor consumes held/cleanup as publication gates and reports live flags; K7/K8/K10 test synthetic fixtures, not preserved receipt fields |
| hash the clone runner | implemented and per-run digest verified; no frozen predicate, so not counted as a QUALITY48 repair |
| fleet-root realpath | new plan CLI passes K11's alias fixture; symlink-sibling naming/coverage gaps remain |
| bounded streams/redaction | K9 refuses bundle publication only; full observations remain unbounded and unredacted |
| loose stdout tokens | unchanged/open, a choice already recorded in round23; successor expectations could strengthen them without rewriting the frozen pair |

K2 is author-added case-fold coverage; K4 is a carried any-token control from round23's selftest. Seven moved mechanism groups is one optional taxonomy only: argv K1/K2, exit K3, pins K5/K6, held/cleanup K7/K8, size K9, listing K10, identity K11. Combining all refusal returns instead gives six moved groups. The measured unit is eleven predicates, not a mechanism count.

### Fresh falsification, corrections and limits

The fresh 64-seat wave confirmed the declared before/after result, but found important limits. The replacement L1 retained all reports, appended lesson Errata E–P, corrected the knowledge entry, and added direct **SKILL.md consumer warnings** after residual critics found that lesson-only corrections were insufficient. No production tool, frozen fixture, ruler or registry expectation was changed after the falsification wave.

- Single-fixture predicates miss weaker implementations. Executed examples include per-token argv-prefix, absolute-value/truthiness exits, character-not-byte stream counting, unresolved siblings, and schema/name/stream-type guard removals (MutFixtures, MutProject, MutPlan). Several additional variants in PredK4/8/9/10/11 are **static seat inferences**, not fresh executions. The lesson now makes that distinction.
- K10 combines both live triggers, so deleting either disjunct leaves it green; the independent single-trigger selftest cases catch those deletions (MutProject M05/M06). QUALITY49's stronger loop-position rule is **not operationalized** by a landed fixture. Its Mistakes-row “failure-backed fix” claim was withdrawn; the separate missing-after-receipt repair supplies this round's failure-backed frontier example.
- `--project` validates less than its consumer: malformed observations can publish bundles that command-binding rejects with exit 2; synthetic undeclared requirements can bind cleanly. A lone-surrogate stream crashes instead of yielding the documented invalid-input report (CodeProjectInputs).
- Publication is non-atomic. A refusal in a reused output directory leaves an older mutually consistent bundle/expected pair that still passes cleanly. Git hooks can write outside `--out`; the clone is not isolation and selected-revision code inherits caller authority (CodePublish, SentinelRun). These warnings are now directly on the consumer SKILL surface. The unchanged tool docstring's stronger promises are explicitly not reliable.
- The “41 revision-pinned / 2 live” classification means **not declared live**, not self-contained. Two additional rows read live sibling object stores. The clean gate covers all 43 receipts, including the declared-live rows; the classification sidecar is not digest-covered. The 43-row replay and 47-row current battery are different populations (CodeLiveList, RunRegistry, CodeRunReplay).
- Three harmed monitor intermediates are retained and restored, not hidden: A at bd38c02 (47/62, restraint 6), B at 250069f (60/62, restraint 6), C at c6e827a (59/62, restraint 6). Actual traced author reads restore the bounded monitor. A numerical score cannot detect all misleading prose; direct warnings and open defects remain part of this verdict.

Residual reviewer reports are under `.ufo/waves/round-24/residual/`. ResAfterRuler, ResMonitorReanchor and ResRegistryCensus independently reproduced the principal results. ResVerdictCritic accepted C1 within the frozen bounds and identified the consumer-warning and harmed-intermediate omissions, which were corrected. ResAccounting confirmed the totals; its allegation that the lesson cited the lane destination as the misroot site is rejected—the committed lesson actually names the fleet-root source path. No report was edited to erase a disagreement.

### Dispatch, routing, accounting and cleanup

- **Wave 1:** one validated 64-seat payload; role mix **14 reviewer, 13 critic, 11 scout, 10 executor, 6 connector, 4 mutation-tester, 3 revenger, 1 sentinel, 1 scribe, 1 simplifier**. L1 holds the planner seat; PlanWalk supplies a bounded mapping walk. The inherited validator refusal of `labrat` was fixed before validation. Attempts 1–2 refused all 64 with `Background job limit reached (100)` and spent zero seats. Attempt 3 spawned 64; all 64 delivered completed callbacks. The slot was acquired immediately before that call and released on return.
- **Residual checks:** one ordinary eight-seat batch (4 reviewer, 4 critic), not a falsely labeled 64-seat wave. Only eight consolidated correction/receipt surfaces remained; no second full wave was padded from repeated attacks. Attempts 1–4 refused all eight at the job cap; unchanged attempt 5 spawned eight. All eight completed.
- **Round total: 72 seats, 72 completed, 0 dead, 0 replaced.** Dead-seat list: none. No provider death occurred in this round's spawned seats. Host routing was used without per-seat model parameters; older route-mix output is retained as its historical observation, not asserted to describe later host routing changes.
- `tools/wave-accounting.py` over `.ufo/waves/round-24/round-accounting{,-expected}.json` → exit 0, `[]`, totals 72/72/0 (`round-accounting-receipt.json`). Basis is retained completed callbacks, never report presence or provider authentication. Eight residual reports and all 64 wave reports are committed. Original validator registry null handles remain historical; actual identities are explicitly mapped in the accounting bundle/outcomes and dispatch receipt.
- RowAudit01 misrooted its report to the fleet root. It was copied byte-exact into the lane, `cmp` returned 0, then the fleet copy was removed. Destination SHA-256 `3bc5633cbdb22df4861df820849a69c6ba37eca53bc5953762cfb626ad0b908f`. The current required fleet-wide sweep is retained in `misroot-sweep.json`; it records present absence, not a fabricated replay of the old copy. Other lanes' untracked files/state were untouched.
- `/tmp` filled during receipt capture. Only tameshi-owned scratch was cleaned; all current-round scratch in `/tmp` and `/fast/scratch/hyaku/tameshi-r24/` was removed after retaining evidence, per the parent directive. No other lane's scratch was deleted.
- **Installs/updates:** none by this replacement, predecessor in r24, or reported r24 seats. No routing/configuration, fleet script/template, MANIFEST or campaign-state mutation.
- **L0:** no new question. The inherited round18 R17-INCIDENT helper-recovery question remains on the side channel; no ruling is inferred from present helper behavior. The older round1 numbering question remains historical.

**Stale-lane:** same held round24 claim only; no other mission of this lane is open and no round25 was started.

## Landed changes

All new changes are motivated in `LOG.md`'s round24 section; the appended lesson and SCORECARD link the measurements and limitations. Lane tip is **`09a3a309376e3e883053773a35bac801d10d8402`** (committed and pushed through `jj-lane.sh`).

| Landed commit | Work |
|---|---|
| `e338f1bd0749a1786d95d3d3cd9572bb10757667` | predecessor: freeze contract/ruler/before |
| `d2eaecd443bf5f4e387e7e5331282e3d11dea047` | predecessor: fixtures, replay successor, registry pins, sourced entry and QUALITY48 |
| `bd38c02a8b74752accaf88089c8c17024b2ab893` | predecessor: real 43-row replay and gate receipt |
| `c8c5b88c8e961a929cdc351b95a7074c76958909` | predecessor: fifteen traced source re-anchors |
| `04657a63fd140451a487aa8a6c333663f7061685` | replacement: actual 11/11 after receipt and no-harm receipt |
| `250069f1b4ea735cbe89a0637a96af9fae640dca` | after measurement, fresh-wave errata, dispositions and QUALITY49 |
| `671a6e2e970955a77aa7dacddde6419a3b8d6ecc` | two actual B source re-anchors; preserve harmed intermediate |
| `4903959687d16623adeeeae059bc010dcfc9d23f` | wave spec/refusals/dispatch, 64 seat reports, accounting and lesson |
| `c6e827a97bba5998503b087ce8b91b77fef682ed` | residual corrections, direct consumer warnings, narrower QUALITY49 |
| `113c1aa7ab81630eeade36f90a448f93cd3c104d` | three actual C source re-anchors, preserved prefix and harmed C |
| `09a3a309376e3e883053773a35bac801d10d8402` | eight residual reviews, final 72-seat accounting, census and landing receipts |

The predecessor hashes above were inherited as already pushed durable history and re-verified for reuse. Replacement hashes are the helper's final `landed` outputs. No raw lane git/jj commit or push was used.

## Before → after measurements

### C1 — improved against the frozen predicates; numeric calibration 8→8

Counting command (ruler unchanged throughout):

```sh
python3 .ufo/evidence/round-24/measure.py --repo CLONE_AT_REV
```

| Observation | Measured revision | Result | Retained evidence |
|---|---|---|---|
| Before | `6a1821a8897eea6e7d9669292160ec9593669409` | 1/11, exit 1; only K4 caught | `before.json`; fresh RunRulerBase reproduction |
| After | `c8c5b88c8e961a929cdc351b95a7074c76958909` | 11/11, exit 0; K1–K4 controls/restoration clean | `after.json`; RunRulerAfter |
| Post-errata | `4903959687d16623adeeeae059bc010dcfc9d23f` | 11/11, exit 0 | `final-verification.json`; ResAfterRuler |
| Post-consumer-correction | `113c1aa7ab81630eeade36f90a448f93cd3c104d` | 11/11, exit 0 | `landing-verification.json` |

K1–K4 are four specific mutant kills, not arbitrary weakening coverage. K5/K6 test row digest pins with self-consistent substituted bundles; changing both declaration and bundle later selects a new contract. K7–K11 are successor projection/plan synthetic capability checks, not a negative real-run replay. The actual replay refused **0/43** rows. No general end-to-end hardening inference is admitted.

Selftests at measured 4903959: command-binding **44/44**, replay **10/10**, exits 0 (`final-verification.json`). Frozen round23 ruler still gives **10/10** (RunR23Ruler). The source-read pair remains **1/ARGV_MISMATCH**, its correct control **0**, and pinned bundle report values match (RunReplayGate).

### No-harm monitors and retained harms

```sh
python3 .ufo/evidence/round-21/coldread/measure.py --repo LANE --rev REV --explain
python3 tools/registry-check.py --root LANE --rev REV --json
```

`registry-check --rev` grades a throwaway fleet-shaped clone; the `--root` identity must preserve sibling layout. RunRegistry's malformed isolated-root 45/47 was an invocation-layout failure; the layout-faithful run was 47/47. It remains on record rather than being counted as a revision defect.

| Point | Revision | Source sections | Restraint / depth | Registry |
|---|---|---:|---|---|
| Base | 6a1821a | 62/62 | 8 / 8 | 46/46, 4 superseded (r23 final, inherited) |
| Harm A | bd38c02 | 47/62 | 6 / 8 | — |
| Restored | c8c5b88 | 62/62 | 8 / 8 | 47/47, 7 superseded |
| Harm B | 250069f | 60/62 | 6 / 8 | — |
| Restored | 4903959 | 62/62 | 8 / 8 | 47/47, 7 superseded |
| Harm C | c6e827a | 59/62 | 6 / 8 | 47/47 (residual reviewer) |
| Final measured content | 113c1aa | 62/62 | 8 / 8 | 47/47, 7 superseded, exit 0 |

Receipts: `monitor-intermediate-A/B/C.json`, `noharm-c8c5b88.json`, `final-verification.json`, `landing-verification.json`. Final monitor is strict, overrides false. Final landing adds evidence/reviews only after 113c1aa; no monitored content changed. Three C entries preserve the prior **284** entries and append to **287** (`source-prefix-preservation-C.json`); original mistakes and old entries remain. These checks support bounded no-harm, not a proof about arbitrary behavior or prose quality.

## Sources & frontier

**SOURCES: 81→83 rows**, A72→74 / B7→7 / C2→2; mined52→54 / queued23→23 / rejected6→6; malformed0→0 (`sources-invariants.json`). Added tier-A/mined **S084** (official Python realpath docs) and **S085** (own-work routed-defect record). No existing registry row's immutable fields, status, recheck or used-by changed. No F1–F10 frontier row advances; this is same-ground calibration. S085's “each” teaching overclaim is explicitly narrowed in the lesson/knowledge errata, not silently rewritten.

Counting command, at the before and final measured revisions:

```sh
git show "$REV:corpus/SOURCES.md" | python3 -c 'import sys,re,collections,json; r=[[c.strip() for c in x.split("|")[1:-1]] for x in sys.stdin.read().splitlines() if re.match(r"^\|\s*S[0-9]{3,}\s*\|",x)]; print(json.dumps({"rows":len(r),"tiers":dict(collections.Counter(x[3] for x in r)),"statuses":dict(collections.Counter(x[7] for x in r)),"malformed":sum(len(x)!=11 for x in r)},sort_keys=True))'
```

S084 was opened by the predecessor this round and independently reopened by source reviewers; S085's pinned text/quote was rechecked. The lesson `## Gate` records both access dates, bounded lookup **2 identified / 2 screened / 2 included / 0 excluded**, and located ≤25-word quotes. The knowledge entry cites both rows. Corrections scope realpath's default behavior to missing components, loops or OSError, and distinguish the defect-field slice from the full array.

Census command:

```sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root ROOT tameshi
```

**Timing conformance limitation:** no retained temporal round-start census from the predecessor exists. The replacement measured the base retrospectively in a fleet-shaped private clone, with the current conf used only for path routing. It is **not** represented as a historical start-time run (`census-base-recheck.json`). That base run and the final live-root run both exit **0** and print these same seven pre-existing warnings:

```text
tameshi W04 S047 duplicate url pitest.org/quickstart/incremental_analysis across scopes
tameshi W04 S048 duplicate url pitest.org/quickstart/incremental_analysis across scopes
tameshi W04 S075 duplicate url man7.org/linux/man-pages/man1/strace.1.html across scopes
tameshi W04 S076 duplicate url docs.jj-vcs.dev/latest/git-compatibility across scopes
tameshi W04 S077 duplicate url man7.org/linux/man-pages/man2/PR_SET_CHILD_SUBREAPER.2const.html across scopes
tameshi W04 S078 duplicate url man7.org/linux/man-pages/man2/open.2.html across scopes
tameshi W04 S081 duplicate url bazel.build/reference/test-encyclopedia across scopes
```

Base final line: `tameshi ok /fast/scratch/hyaku/tameshi-r24/census-base/tameshi-shokunin/corpus/SOURCES.md` (exit0). End final line: `tameshi ok /home/vgpnk/Projects/shokunin/tameshi-shokunin/corpus/SOURCES.md` (exit0, `landing-verification.json`). Retained JSON preserves exact tab-separated output. Census conformance is not admission.

**Mined mistake with an executed falsifier:** the author promised an after-measurement “below” without retaining one. `git cat-file -e c8c5b88:.ufo/evidence/round-24/after.json` exited **128**; at 04657a6 it exited **0** after the actual receipt landed (lesson Mistakes row, QUALITY6). The separate QUALITY49 row is explicitly **not** claimed failure-backed; its existing probes motivate the rule, and conforming fixture work was not performed. The dispatch role refusal, cap refusals, misroot and three drift harms remain as additional mistakes, not erased history.

## Trend verdicts

- **Expansion: unchanged.** Same-ground calibration; no uncovered F1–F10 ground absorbed. The successor capability row is demonstrated only within the named synthetic limits. Connector checks found no contested kagi/kumitate/kama/mori ownership.
- **Quality: improved, narrowly.** The named argv/exit mutants are now caught and the two digest substitutions no longer hold their registry rows; frozen count 1/11→11/11. Fresh review exposed substantial open defects; direct consumer warnings and preserved errata prevent treating the counter as end-to-end safety. Final bounded monitor and battery are restored after all three harmed intermediates.
- **Discernment: unchanged pending outside closure.** The falsifiers and residual reviewers were dispatched by this lane, not independent promotion/closure authorities. Their disagreements are retained and corrections distinguish executed probes from static inferences. No self-awarded outside discernment credit.

## SHONEN

- [~] Real sourced tables/error patterns/checklists — SKILL.md registry additions and direct appended corrections; S084/S085, knowledge disposition/errata, QUALITY48/49 with explicit limitations. No named independent promotion verifier.
- [~] End-to-end domain task executed/logged — stored 43-row replay and binding gate, current 47/47 battery, LOG.md round24; `replay-command.json`, `replay-gate.json`, `landing-verification.json`. Refusal paths remain synthetic, real replay refused0/43. No independent promotion verifier.
- [~] Instructions executable without oral context — strict source-input monitor 62/62 with 287-entry ledger, retained trace files and preserved prefix. Author re-reads are not blind cold-read or required-command execution. No promotion credit.
- [~] No cross-domain bleed — PROVINCE.md boundaries unchanged; only lane corpus/tools/evidence and this fleet report were authored. Connector findings remain advisory; sibling content and operator-owned fleet files were not edited. No independent promotion verifier.
