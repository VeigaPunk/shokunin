# mori round 82 — fleet & host observability (森)

Lane: mori (detection and report only). Round: 82, attempt 1. Date: 2026-11-04.
Entering revision: `ebcf2c72df203c855cfafb5223c6e22b1e12c481` (branch `master`, pushed, clean).
Freeze commit `20551e56`; integration/measured revision `f02ad83bf9c66722afa1de8ff974d57d2b57d3a2`;
record commit `19d21175cd040ed7e3dc35dd5c0f6240991ab7d9`; measurement tip `d083c5fc`; lane tip at
filing `f573c946a3abee04153537ccea69d5e228ea897f` (a receipt-only commit above `d083c5fc`, which
`git ls-remote origin refs/heads/master` prints).

**Declared claims (1–3, distinct axes).**
1. **C1 — operability (7), capability acquisition.** The r81 five-survivor mutation set becomes a
   committed, revision-agnostic harness: `python3 -I .ufo/waves/round-82/count-c1.py <rev>` reads
   `C1=met harness=present killed=11 survivors=0 total=11 pristine=green detector=green`, red
   `C1=unmet harness=absent` at entering. The delta is the harness (r81's was scratch-only and
   deleted, D81-3); the eleven kills confirm r81's closure at current bytes, not new kills.
2. **C2 — freshness (5, tied lowest).** The red round-10 drift pin is retired as an acceptance
   predicate, with every live drift token classified from the baseline bytes
   (`corpus/evidence/drift-classification-r82.txt`), while the same `--drift` run stays red:
   `C2=met tokens=64 classified=64 agreed=64 residual=0 stale=0 retired=1 cell=1`, red
   `C2=unmet tokens=64 classified=0 … retired=0 cell=0` at entering.
3. **C3 — depth (5, tied lowest).** `tools/mori-record-sweep.py` gains the `revision` arm — a
   record row's stated `key=value` must exist in `git show <rev>:<path>` bytes — plus three frozen
   historical bindings: `C3=met tool=present arms=36 defeated=1 fixtures=3/3 bindings=3
   revisions=0`, red `C3=unmet tool=present arm=absent` at entering.

Frozen authority: `.ufo/waves/round-82/contract.md` (freeze `20551e56`) plus pre-data amendment A1
(binding population) and its wording note (all three original bindings superseded). Do-nothing
controls: `.ufo/waves/round-82/evidence/controls-r82.txt`. After receipt:
`.ufo/waves/round-82/evidence/after-r82.txt`.

## Work performed

- **Claims and freeze.** C1/C2/C3 frozen with their counters and a committed do-nothing control
  before any seat ran: `C1=unmet harness=absent`, `C2=unmet tokens=64 classified=0 agreed=0
  residual=0 stale=0 retired=0 cell=0`, `C3=unmet tool=present arm=absent`, all rc 1
  (`.ufo/waves/round-82/evidence/controls-r82.txt:1-31`; contract `20551e56`).
- **Planar seat (L1).** The validator refuses a `planner` role; the L1 held the canonical §3
  planner seat and the data walk (mutant-anchor verification, baseline token derivation, binding
  population checks) rode the L1's own reads plus scout/connector items.
- **CZ1 harness capability.** `.ufo/waves/round-82/count-c1.py` re-derives the anchored mutant
  population at any revision, runs each mutated copy's own `--selftest` in scratch, reports a
  verdict per mutant and a 4-arm detector selftest (`MUTANT … killed|survived`; `C1=met|unmet
  harness=present killed=K survivors=S total=T pristine=green|red detector=green|red`).
  Measured at `f02ad83b`: `.ufo/waves/round-82/evidence/after-r82.txt:5-18`.
- **C1 negative control.** A committed simulator proves the harness can fail: deleting a committed
  arm from a scratch copy yields `survivors=1` (`Mo82E01C1Regress`,
  `.ufo/waves/round-82/evidence/regression-sim-r82.txt`; script
  `.ufo/waves/round-82/simulate-regression.sh`).
- **C2 drift ledger.** The live run and its raw output are retained
  (`.ufo/waves/round-82/evidence/drift-r82-live.txt`), and every token is classified with the
  frozen derivation table (`corpus/evidence/drift-classification-r82.txt`, 64 lines: 45
  `added-since-r10`, 19 `value-changed`). `Mo82E04C2Drift`; independently re-derived by the L1
  (0 disagreements), by `Mo82R02C2` and by the counter itself.
- **C2 record.** `SCORECARD.md:60` retires `drift-pin-r10` with the reason and both paths; the
  freshness Axes cell (`SCORECARD.md:13`) names the retirement, the classification file and the
  still-red baseline run; PROVINCE records the boundary (`PROVINCE.md`, round-82 note).
- **C3 arm.** `tools/mori-record-sweep.py` gains `revisions` bindings, `--git`, the four failure
  tokens, all-bindings grading and 36 selftest arms (`Mo82E02C3Arm`;
  `RECORD_SWEEP_SELFTEST pass=36 fail=0`).
- **C3 bindings.** `.ufo/waves/round-82/record-pins.json` holds the three frozen historical rows;
  each was verified independently by read-only git with the defeated shape as a negative control
  (`.ufo/waves/round-82/evidence/c3-bindings-r82.txt`).
- **Record maintenance.** D81-1: the r80 capability row now states the landed `pointers=249` with
  a named correction recording that 240 holds at `482dc48d` and that `075574c8` grades 237
  (`SCORECARD.md:4038`). D81-2: the C2 after-run is committed at `f02ad83b`. D81-3: the harness is
  committed and re-runnable. D81-4: the route map and seat routes are recorded in this report.
  D81-5: the sourced claim is labelled C3/S597 and the Gate records the refused candidates.
  D81-6: the entering revision is the pre-round HEAD `ebcf2c72`.
- **Registry and criteria.** `SKILL.md` registry row 16 (revision-precision arm); QUALITY 168 (a
  value labelled with a revision must exist in that revision's bytes, with its limits);
  `PROVINCE.md` round-82 scope note; `corpus/README.md` round-82 knowledge row.
- **Frontier step.** S597 admitted from the git project's own bytes: scout
  `Mo82Sc01Source` (`corpus/evidence/sources-r82/`, two byte-identical fetches, ETag =
  `git hash-object`). Knowledge entry `corpus/knowledge/record-revision-precision-r82.md`
  (`Mo82S02Knowledge`); lesson `corpus/lessons/round-82.md` (`Mo82S01Lesson` + L1 addendum).
- **Adversarial seats.** Two reviewers (`Mo82R01C1`, `Mo82R02C2`), a contract critic
  (`Mo82C01Contract`), an independent mutation prober (`Mo82M01Mutants`), a git-primitive probe
  (`Mo82R03GitPrimer`) and a sibling-overlap connector (`Mo82K01Connector`); their defects are
  listed under Landed changes and routed debt.
- **No-harm battery.** `BATTERY pass=60 setup=4 fail=0` at the dispatch tip
  (`.ufo/waves/round-82/evidence/battery-r82.txt`); the four are the inherited lane-scoped scratch
  setup refusals.

## Landed changes

Every change is carried by the LOG.md round-82 entry (`LOG.md`, "## Round 82 (2026-11-04, L1
MoriR82)") and one of the commits below.

| Change | LOG.md entry | Commit |
|---|---|---|
| Frozen contract, three counters, do-nothing controls | Round 82 §C1–C3 | `20551e56` |
| Wave spec, dispatch, validator receipts | Round 82 §L2 | `08e13729` |
| `tools/mori-record-sweep.py` revision arm; pins; classification file; S597; QUALITY 168; SKILL row 16; PROVINCE note; SCORECARD Retired row + freshness cell + capability rows; lesson; knowledge entry; seed wave evidence | Round 82 §C1–C3, §Frontier step | `f02ad83b` |
| SCORECARD Round-82 table + Planned (round 83); LOG round-82 entry; lesson L1 addendum; counter repairs; all 15 seat reports; after receipt | Round 82 (whole) | `19d21175` |
| Wave results, coverage-map row, knowledge `source:` fix, final-tip receipt | Round 82 §L2, §Frontier step | `d083c5fc` |
| Final-tip measurement appended to the after receipt (`after-r82.txt`) | Round 82 §C1–C3 | `f573c946` |

Counter repairs landed in `19d21175`, all made before any after-value existed and all filed by
wave seats against the frozen sentence (predicate, kill rule and target byte-unchanged):
C1 marker identity + unanchored-is-unmet + in-run detector selftest (`Mo82C01Contract` D1/D2,
`Mo82R01C1`); C2 "anything else" token class and duplicate-classification counting
(`Mo82R02C2`); C3 committed-pins grading, exact population with uniqueness, three independent
fixtures and tool markers (`Mo82C01Contract` D4/D5/D6).

## Before → after measurements

All three counters export and grade the revision under test, so the entering control and the
after-value are the same command. Receipts: `controls-r82.txt` (entering) and `after-r82.txt`
(after). The after values were measured at `f02ad83b` and re-derived unchanged at `19d21175` and at
the lane tip `d083c5fc`.

| Claim | Counting command (lane root) | Before (`ebcf2c72`) | After (`f02ad83b`, re-run at `d083c5fc`) |
|---|---|---|---|
| C1 | `python3 -I .ufo/waves/round-82/count-c1.py <rev>` | `C1=unmet harness=absent`, rc 1 | `C1=met harness=present killed=11 survivors=0 total=11 pristine=green detector=green`, rc 0 |
| C2 | `python3 -I .ufo/waves/round-82/count-c2.py <rev>` | `C2=unmet tokens=64 classified=0 agreed=0 residual=0 stale=0 retired=0 cell=0`, rc 1 | `C2=met tokens=64 classified=64 agreed=64 residual=0 stale=0 retired=1 cell=1`, rc 0 |
| C3 | `python3 -I .ufo/waves/round-82/count-c3.py <rev>` | `C3=unmet tool=present arm=absent`, rc 1 | `C3=met tool=present arms=36 defeated=1 fixtures=3/3 bindings=3 revisions=0`, rc 0 |

Do-nothing reachability was attacked, not assumed: a print-stub harness is refused
(`markers=missing`), a hardcoded kill tally fails the detector selftest (`pass=3 fail=1`), a
partially unanchored population is unmet, a counterfeit revision tool is refused (`arm=absent`),
the all-`added-since-r10` classification scores `agreed=45` of 64, and a single or triplicated
binding fails the population check. Each attempt was executed during the round.

## Sources & frontier

`SOURCES.md` rows: **369 → 370**, one row added, zero rows removed or edited.

```text
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin mori
# before (inherited from the r81 lesson, not rerun at entering): 369 rows, exit 0, 35 W04 warnings
# after:  rc 0, `mori ok`, 370 rows, 35 tolerated W04 duplicate-URL warnings, malformed 0
grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md
# 370
```

- Rows added by tier: **1 tier-A** (`docs`), S597 — gitrevisions(7), git v2.56.0, pinned
  `corpus/evidence/sources-r82/gitrevisions.7.git-2.56.0.body.adoc` (sha256 `b23a9eb1…`, 424
  lines / 17266 bytes) + shell `…adoc` (sha256 `afe4cab8…`, 36 lines / 824 bytes); quote at body
  lines 220-223, 24 words.
- Rows touched old→new: `S597 absent → mined` (new); no `status`/`recheck`/`used-by` change to any
  existing row.
- Frontier rows advanced: **none** in `PROVINCE.md`'s Frontier table. C3 extends an existing
  instrument (record sweep) with an arm; the coverage map gains the r82 row
  (`corpus/README.md`, "Round-82 knowledge addition"). FR1–FR14 are untouched.
- Refused: `git-show(1)` (uses revision parameters but never states the `<rev>:<path>` grammar or
  an exit status; flip: a page stating both); `git-cat-file(1)` uses the form once in SYNOPSIS
  without defining it — uses-without-defining, no row.
- **Assimilation:** none — `/home/vgpnk/Projects/shokuknow/merge/mori/` staging is still behind the
  r61 L0 (id collisions with the lane registry). `considerthese/` re-checked: the newest file's
  remaining suggestions stay behind the r62/r65/round-73 L0s; nothing new mined.

## Trend verdicts

- **expansion: improved** — one new admitted knowledge entry on ground the coverage map did not
  hold (record revision precision as a byte fact, with its decision table and its stated limits),
  grounded on a row opened, pinned and quoted this round (S597), with the coverage-map row landed
  in the same round; census 369 → 370, rc 0.
- **quality: improved** — the record sweep gains a graded arm with 36 arms and three independent
  fixtures; the lane's revision-labelled values are now checkable against the bytes they name
  (QUALITY 168); the r81 five-survivor closure is re-derivable by a committed instrument; the
  battery reads `pass=60 setup=4 fail=0` and both pins arms are green at the landed value
  (`pointers=249`, `pending=0 pinned=0`). Counterweights, routed: the mutation prober's
  `MUTANTS killed=18 total=38 survivors=20` (16 counter mutants survive; the counters grade their
  helpers, not themselves), C2's live-reading immutability and C3's occurrence ambiguity — all
  three registered in `SCORECARD.md` `## Planned (round 83)`.
- **discernment: improved** — the r81 closure's D81-1..D81-6 are discharged against receipts; two
  reviewers and a critic attacked the frozen counters *before* measurement and every filed defect
  (stub harness, unanchored population, hardcoded tally, uncommitted pins, population identity,
  count-keyed fixture, token class, duplicates) was repaired and re-measured, with each attempt
  shown failing; the retirement keeps the round-21 retained-evidence blocker explicitly visible and
  claims no acceptance. Named weakness: C1's delta is the harness plus a confirmation, not new
  kills, and the report says so rather than dressing it up.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources —
  registry row 16 (`SKILL.md:1368`) names the revision arm's verdict map and its pinned
  `pass=36 fail=0`; QUALITY 168 states the rule and its limits (`corpus/QUALITY.md`).
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md` "## Round 82
  (2026-11-04, L1 MoriR82)" records C1–C3 with their keepers and measured values; the domain task is
  the drift classification of all 64 live tokens and the revision-arm grading of three real
  bindings (`.ufo/waves/round-82/evidence/after-r82.txt`).
- [~] Instructions executable by an agent without oral context — every keeper runs from the lane
  root with one command; the harness, both sweep arms and the classification file carry their own
  `--selftest`/receipts (`count-c1.py --selftest` 4/4, `count-c2.py --selftest` 9/9, `count-c3.py
  --selftest` 8/8, `tools/mori-record-sweep.py --selftest` 36/36).
- [~] No cross-domain bleed (PROVINCE.md still accurate) — the round reads only lane record
  carriers and git objects; the retirement and the arm are recorded in `PROVINCE.md`'s round-82
  note with the detection/report boundary and the round-21 non-acceptance statement intact; no
  dispatch, OS, credential or serving ground is touched.

Stale-lane: respawn-per-round driver; no other mission of this lane is open.

## Round shape, seats and limits

- ONE v1 wave (`w1`, validated under `scripts/hyaku/ufo-wave-policy.json`, band 8–16; dispatch
  `.ufo/waves/round-82/w1-dispatch.json`, `counts.spawn=15`): **15 seats** — 5 executor, 2 scribe,
  2 scout, 2 reviewer, 1 critic, 1 mutation-tester, 1 connector, 1 revenger. Attack share
  4/15 = 26.7 % (reviewer ×2, critic, mutation-tester); connectors 1; residual call: none; round
  total 15. Ready file `w1.ready` (04:41) taken by the orchestrator at 04:42 with all 15 names.
- Dead seats: **none** — all 15 seats returned non-empty output
  (`.ufo/waves/round-82/w1-results.json`, `seats: 15`, every `output` non-empty); the results file
  carries a null `status` per seat, recorded here as an observation rather than read as a verdict.
- Routing: no `model` field was passed in any of the 15 tasks; the route table
  (`~/.omp/agent/config.yml`, operator-owned) decides. Per-seat answering models are not recorded
  by the harness this round (D81-4 remainder) — the report states the gap rather than asserting a
  map.
- Tool installs: none. No pacman transaction was run; no tool was upgraded.
- Open L0 lines re-verified present and unanswered: mori round-62 (wave-surface waiver), round-65
  (instrument-change ruling), round-73 (label-sweep instrument), round-61 (`merge/mori` package
  collisions). Routed around, not treated as answered; no new L0 line was filed.
