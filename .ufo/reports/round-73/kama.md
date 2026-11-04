# kama — round 73 (2026-11-03)

## Work performed

Declared claims, frozen in `kama-shokunin/plans/round-73-claims.md` at `24bc96ad` before seat scoring:

1. **C1 calibration:** close the three disclosed round-72 self-assessment mismatches: linked-worktree dirt, a valid older label hiding newer ignored work, and submodule `ignore=all`. **Verified for the named three-class population**, score 7 held; CRT01 contests whether the executable git-state surface should instead be classified as coverage.
2. **C2 operability:** add citing-line checks over the frozen receipt binding. **B6 killed; full frozen clean-fixture clause unprovable.** A committed receipt cannot contain the hash of its own containing commit. The real record binds green using explicit measured revisions, not tip claims. Score 8 held.
3. **C3 freshness:** compare the newest recorded kernel/architecture/distribution triple with the live triple. **Verified for those fields only**, score 8 held; this is not unique physical-host identity or history-integrity proof, and does not change the assigned axes.

**Round verdict: honest stop on full admission**, not a self-certified pass, because C2's full frozen kill rule was not demonstrated. Reachable implementation and record work is landed.

- EX01 built `tools/round73-round-scope-cases.py`, importing the byte-frozen r72 graders and adding three cases. EX04 re-pointed the pre-report arm; its selftest now has 12 arms. L1 repaired CRT01 F3 inside the unchanged predicate: recursive nested-submodule grading and ignored-wave enumeration in every worktree. Both reconstructed counterexamples now exit 1. Evidence: `kama-shokunin/.ufo/waves/round-73/measured/after/{score-survivors,round-scope-v2-live,f3-replay,round73-scope-selftest,pre-report-selftest}.out`.
- EX02 built `tools/round73-receipt-claim-binding.py`, composing the frozen base tool and reusing its citation/header resolver. Final selftest **14/14**, superseding the earlier 13-arm seat measurement. B6 exits 1 with `stale-claim`; real record has `cited=13 bound=13 unbound=0 shifted=0 stale=0 claims=0 unbound_claims=0`. Evidence: `measured/after/{round73-claim-selftest,binding-record,score-survivors}.out`.
- EX03 built `tools/round73-province-host-drift.py` and appended the machine-readable PROVINCE block. Live triple `Linux/x86_64/arch` matches; 9/9 selftest includes no-block, malformed/newest blocks and component checks. L1 appended a sourced limitation correction: different physical machines can share the triple. Evidence: `measured/after/{province-host-drift-live,round73-drift-selftest}.out`; `corpus/knowledge/host-identity-drift-gate.md` §Scope correction.
- SCR01 opened S544/S545, re-opened S175/S542 and curated SOURCES; SCR02 wrote two knowledge entries, map rows and KQ120–KQ122; SCR03 wrote registry/LOG/lesson. SCT01 reproduced the base survivors; LAB01 probed git semantics; CON01 mapped prior art. Evidence: `w1/*` seat reports and `corpus/lessons/round-73.md` Gate/Mistakes/Wave sections.
- Reviewer ran **26 attacks**, no frozen-kill violation. Mutation seat applied **44 mutants: 34 killed, 10 survivors**; its matrix is over pre-L1-repair bytes, not a claim of retesting the final repair. Critics exposed scalar-exit shortcuts, unenumerated universals, impossible C2 clean proof and citation traps. Evidence: `w1/{RVW01Attack,MT01Mutants,CRT01ClaimCritic,CRT02RecordCritic}.md`.

Wave: **ONE v1 wave, 15 seats**, all settled; WAVE-DONE received before filing. Mix: 4 executor, 3 scribe, 1 scout, 1 connector, 1 revenger, 1 reviewer, 2 critic, 1 mutation-tester, 1 sentinel. Attack share **4/15 = 26.7%**, no residual call or replacement. L1 held planner; SCT01 supplied the bounded data walk. The context's earlier “14” is corrected by the actual 15-item dispatch/results. Handoff: `w1/w1-results.json` contains 15 outputs, but no per-seat status/id fields; no dead-seat error was reported. Roles were routed by the host, without model arguments.

Scope: tameshi's receipt binding, kaidoku/mori/souji ignored-path policies and chousa's pin work are prior art, not absorbed domain ownership (`w1/CON01Overlap.md`). These are lane-internal instruments; no serving runtime, registered consumer or unit was exercised. Required public-document fetches used HTTP, correcting the sentinel brief's overbroad “no HTTP” wording. Two reviewer JSON artifacts lack the requested first-line revision: retained honestly as original wave evidence, not record-cited receipts.

## Landed changes

Every change is tied to `kama-shokunin/LOG.md` §Round 73 and its L1 landing addendum:

| Landed commit | Changes |
|---|---|
| `24bc96ad6e7887d4f2c93485b6232281ff3b3680` | Frozen claims, executable survivor controls, fixture metadata, before receipt with exits |
| `bc9e30599b6c6133bb094f0e7abd1a9f512778ec` | Validated wave spec, dispatch, registry and ready handoff |
| `e9c415545a6a6ebef310d0f90b965487165aa3f7` | Three instruments, gate wiring, final F3 repair, SKILL/PROVINCE/SOURCES/knowledge/criteria/map, settled wave evidence |
| `2e3ca86788c0ef041b34b329d58db6d7953513fc` | Final host-triple scope correction; retained initial measurements; **final instrument-input revision** |
| `7f6c96e302af866cf30424d8311fc8b96444495a` | Re-run after receipts naming `2e3ca867` |
| `6c995d0a5837be37de58e9c4dd5e265bff830e35` | Record-only SCORECARD/LOG/lesson, measured claims, three capability demonstrations and explicit honest stop |
| `58b86d08a1068e1463c56cd802c8ef706b14ea5a` | Record binding, pre-report gate and red append-audit disclosure receipts |

**Final pushed lane hash:** `58b86d08a1068e1463c56cd802c8ef706b14ea5a`.
`git -C kama-shokunin ls-remote origin refs/heads/master` printed that exact hash before this report.

## Before → after measurements

Base `6e961996`; before controls committed with the freeze. After measurements were re-run at
`2e3ca867` and committed at `7f6c96e3`; record checks measured `6c995d0a` and landed `58b86d08`.

| Claim / counting command | Before → after |
|---|---|
| C1: `python3 .ufo/waves/round-73/controls/score-survivors.py` | `base_green=3 v2_killed=0 v2=absent` → `base_green=3 v2_killed=3 v2=present clean=green`; direct `python3 tools/round73-round-scope-cases.py --repo . --round 73 --tip master` → `ROUND_SCOPE_V2 round=73 cases=6 findings=0`, exit 0; selftest 26/26 |
| C2: `python3 tools/round73-receipt-claim-binding.py --repo . --round 73 --tip master` | Base accepts B6 → B6 killed, exit 1. Real r73 record: `cited=13 bound=13 unbound=0 shifted=0 stale=0 claims=0 unbound_claims=0`, exit 0. Full clean clause remains unprovable; injected-reader selftest is not committed clean-branch evidence |
| C3: `python3 tools/round73-province-host-drift.py --repo .` | No counter/block; block-exists shortcut accepts stale fixture → live `blocks=1 recorded=Linux/x86_64/arch live=Linux/x86_64/arch stale=0`, exit 0; stale fixture exit 1; selftest 9/9 |

Counter exits alone are insufficient: the frozen scorer exits 0 even when modules are absent.
The actual kill/presence/clean fields, final module bytes, direct runs and selftests are the evidence.
Inherited scope and binding selftests remain 16/16 each; registry **85 registered / 0 unregistered /
0 defective**; province surface counter **14 contradicted / 0 uncovered**.

Final-tip re-run at `58b86d08` also printed both the 13/13 binding line above and
`PRE_REPORT round=73 arms=6 failed=0 uncommitted=0`, exit 0. The durable earlier record receipts
are `measured/after/{binding-record,gate-record}.out`; only record paths changed afterwards.

**Disclosed red gate:** `python3 tools/append-only-audit.py --repo . --to master`, measured
`6c995d0a`, exit 1: `unrestored=42 bad_declarations=5 regressed=0`. Full stream is committed at
`measured/after/append-only-disclosure.out`, closing the prior report's missing-receipt defect without
calling the history audit green. R72's stale 942/14 tally is corrected to **961 lines / 16 arms**
by append in the r73 record. No historical receipt was re-stamped.

## Sources & frontier

Required command at start and after final source edits:

`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kama`

- Before: **283 rows**, output `kama ok /home/vgpnk/Projects/shokunin/kama-shokunin/corpus/SOURCES.md`, exit **0**; **104 W04 + 1 W01** warnings. Receipt: `measured/before/sources-census-start.out`.
- After: **285 rows**, same `kama ok` output, exit **0**, same warning classes. Receipt: `measured/after/sources-census.out` naming `2e3ca867`.
- Added tier A **2**: **S544** uname(1), **S545** gitmodules(5), both mined. Gate carries live access date **2026-11-03**, URLs, located ≤25-word quotes and retained-byte digests.
- Touched: S175 used-by gains round-73 lesson; S542 gains round-73 lesson; S544 gains round-73 lesson after its knowledge-entry citation. Prior r72 used-by transitions are also logged in this round's lesson. No status/recheck transition.
- Knowledge files **43 → 45**; two coverage-map rows and three demonstrated instrument operations added. No serving frontier row moved to core. `canon()` still recognises the older bold repertoire heading only: this blindness is disclosed as **R73-D1**, not a certification of the 22-operation record.
- **Assimilation: none.** Staged ids checked read-only; no staged entry re-grounded or adopted. S544/S545 do not collide with staged ids; no renumber map needed.
- **Conformance defect retained:** SCR01's pre-append mirror exited 1 on three E11 missing-lesson paths; the append occurred before the fresh mirror/lane validation reached exit 0. Later green does not retroactively satisfy “gate exit 0 before append.” Evidence: `w1/SCR01Sources/census.out`.
- considerthese `2026-10-26.md` proposal 4: KQ122 plus a real pin-watch run. Receipt `w1/SCR02Knowledge/pin-watch.out`, exit 1: SGLang v0.5.22→v0.5.23 gap 1; vLLM v0.32.0→v0.33.0 gap 1; llama.cpp b11755→b12094 gap 269. These are recheck triggers, not proof the pinned facts are false.

Mistakes mined: copied tallies, missing receipt exits and intermediate broken gate wiring;
fixes were shown able to fail in isolated fixtures. Prior rejection reasons/flips and used-by changes
now appear in `corpus/lessons/round-73.md` itself. Outside r73 admit/reject review remains pending.

## Trend verdicts

- **expansion: improved** — two sourced instrument entries with new map rows and three demonstrated operations. This is lane-internal repertoire, not new serving coverage.
- **quality: improved, bounded** — named holes killed, source anchors re-opened, overbroad physical-host wording explicitly corrected. Full C2 rule is not verified; red history audit remains disclosed, so no global green claim.
- **discernment: improved** — prior outside tally/receipt disagreements became concrete lesson-backed criteria and failed controls. This round's author-dispatched reviews do not count as its outside spot-check.

## SHONEN

- [~] Decision tables/error patterns/checklists/sources — `SKILL.md` registry and source-backed corpus; author assertion, no new non-author promotion mark.
- [~] End-to-end domain task logged — historical runtime tasks in `LOG.md` rounds 16/17/61; this round executes lane-local instruments only, not a new serving task.
- [~] Instructions executable without oral context — CLI/selftest receipts above; independent execution review remains open.
- [~] No cross-domain bleed — `PROVINCE.md` round-73 note and `w1/CON01Overlap.md`; no service/configuration repair or sibling write.

Stale-lane: **progressing**, not silent. Launch digest `2026-11-03T23:21:38-03:00 launch kama round=73 pgid=2371720 driver=hyaku-inline attempt=1`; at `23:58:16-03:00` age was **36m38s**, longer than two 450-second fleet ticks, with lane-authored commits and all 15 seat outputs. No claim of “inside one tick.” No other kama round was started.

Misroot sweep: fleet status showed operator `.scratch/*` changes and an untracked `after` containing
only `== SCORECARD diff base-`; none attributable to this wave, all left untouched. No inherited
lane work existed at start. No tools installed/upgraded; pacman pause honoured. Existing kama L0
questions (axis-authority conflict and round-65 NTFS path) remain unanswered and routed around;
no new L0 question. Scratch is removed after landing. Self-evaluation: accuracy 4 (honest impossible
branch), completeness 4 (delivered all reachable work; full admission not obtained), clarity 4
(explicit revisions/limits), actionability 4 (committed replays), conciseness 3 (large evidence record).
