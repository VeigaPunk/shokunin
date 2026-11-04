# kumitate — round 81 report

Lane `kumitate` (axes: operability + coverage — orchestration and tooling), round 81 of the run-15
hyaku block. Base tip `77c7a8b3fe7f3cebe681065da283de0ae38ddb5b` (the round-80 verifier spot-check,
the lane's remote tip). Frozen plan, counters, open receipts and pre-data controls at
`f8783f4be4d7e14aedf125e2c3323d46ce0da403`; wave payload `2ac1f34d9f6e7322602ae930f071dcf292d7dae5`;
scaffolding `d140f2883170cc1b0859ba5359bcdac3123a676e`. Amendment 1 (append-only, `plan.md`) records
the counter-fixture repairs and the CLI defect the frozen arm found, before any verdict.

## Work performed

The round declares **two claims on two axes**:

- **C1 — operability, capability acquisition `ready-handoff`.** The run-7 inline spawn handoff
  (`<wave>.ready` + the dispatch it names) is judged before the orchestrator takes it:
  `scripts/ready-handoff.mjs`, contract `kumitate-ready-handoff-v1`, 12 policy findings and six
  fail-closed refusals, one exit-bearing verdict, `--json`, a 34-case hermetic suite.
- **C2 — coverage:omp, the shape receipt becomes self-describing.** `kumitate-omp-shape-v2` =
  `{contract, captured_at, entries}`; `--snapshot` stamps the instant, `--shape` discloses
  `captured=<date> age_days=<n>`, `--max-age DAYS` is the opt-in staleness gate, `SHAPE_VERSION` and
  `SHAPE_CLOCK` are typed refusals, `--compare` still reads a legacy receipt, and the O score never
  reacts to age.

Work items, each with its evidence pointer:

- **Freeze** `f8783f4b`: `plan.md`, `probe/probe81-c1.mjs` (16 arms), `probe/probe81-c2.mjs` (15
  arms), the open receipts (`open/`), the pre-data controls (`controls/c1-base.txt` 0/16,
  `controls/c2-base.txt` 4/15, re-measured under `plan.md` Amendment 2) and the constant-printer
  controls (`controls/c1-stub.txt` 3/16, `controls/c2-stub.txt` 6/15).
- **Wave payload** `2ac1f34d`: `w1-spec.json` and the validator's `w1-dispatch.json` (14 seats) plus
  the committed `w1.ready`.
- **Scaffolding** `d140f288`: the new gate, `omp-census` v2, the `pin.ready-handoff` key in the
  proxy's gate-pin block, the stanza (`A=889 C=41 C2=201`), the SKILL registry row and two checklist
  items, and two sourced knowledge entries with committed captures.
- **C1 measured** — `node .ufo/waves/round-81/probe/probe81-c1.mjs --set c1` →
  `C81_C1: HELD held=16/16` exit 0 (`close/c1-probe.txt`); the round's own handoff reads
  `READY_HANDOFF: READY wave=w1 seats=14 attack=4/14 connector=1` exit 0
  (`close/handoff-admission.txt`); the suite is `READY_HANDOFF_SELFTEST: 34/34 pass`
  (`close/handoff-selftest.txt`).
- **C2 measured** — `node .ufo/waves/round-81/probe/probe81-c2.mjs --set c2` →
  `C81_C2: HELD held=15/15` exit 0 (`close/c2-probe.txt`); `--shape .ufo/pins/omp-shape.json` →
  `… captured=2026-11-04 age_days=0` exit 0, `--max-age 30` on a 45-day receipt →
  `SHAPE_STALE age_days=45 max_age=30` exit 1 (`close/census-shape.txt`); suite `PASS (98 cases)`
  (`close/census-selftest.txt`).
- **The 10th spotcheck recurrence** repaired with the lane's own tool and its transcript committed
  this time: `SPOTCHECK_ADOPT: ADOPTED corpus/lessons/round-80-verifier-spotcheck.md wrote=both` →
  `README_MAP: CLEAN files=199 rows=199 covered=199` exit 0 (`open/spotcheck-adopt.txt`), and at close
  `SPOTCHECK_COVERAGE: CLEAN spotchecks=47 uncovered=0` + `MAP: CLEAN` (`close/spotcheck-check.txt`).
- **Routed defects R80-1 … R80-12** answered: `corpus/lessons/round-80.md` §Errata items 1–5, 8–12;
  R80-6 fixed in place in `SKILL.md`; R80-7 reverted in place with the `used-by` change logged in
  the round lesson's `## Gate`; R80-10's practice applied (every round-81 control receipt carries
  `exit=`).
- **Quality criteria** — `corpus/QUALITY.md` Q74 (a Gate quote's stated word count is re-derived with
  `wc -w`), grounded on the r79-D4 / r80-R80-5 repeats.
- **Frontier step** — two sources opened and captured this round, two entries admitted, census
  start/end exit 0.

## Landed changes

Every change below is a path in the lane repo, carried by the commit named, with its LOG entry at
`LOG.md` §Round 81.

| change | commit | LOG |
|---|---|---|
| `scripts/ready-handoff.mjs` (new; `kumitate-ready-handoff-v1`, 34-case suite) | `d140f288` | Round 81 ¶C1 |
| `scripts/omp-census.mjs` shape v2 (`captured_at`, `age_days`, `--max-age`, `SHAPE_VERSION`, `SHAPE_CLOCK`, CLI-dispatch selftest case, `--work` mkdir, EPIPE guard) | `d140f288` + `13060d9b` | Round 81 ¶C2 |
| `scripts/proxy-check.mjs` — `pin.ready-handoff` key (gate-pin block) | `d140f288` | Round 81 ¶C1 |
| `SCORECARD.md` — stanza (`A=889 C=41 C2=202`), re-pins, capability row `ready-handoff`, §Round 81, §Planned r82 | `d140f288` + `13060d9b` | Round 81 |
| `SKILL.md` — registry row `ready-handoff`, `omp-census` v2 notes, two checklist items, R80-6 fix | `d140f288` + `13060d9b` | Round 81 |
| `corpus/SOURCES.md` S236/S237; `.ufo/pins/source-captures.json` + captures | `d140f288` | Round 81 §Gate |
| `corpus/knowledge/ready-handoff-admission.md`, `corpus/knowledge/self-describing-shape-receipt.md` + README rows/pin | `d140f288` + `13060d9b` | Round 81 §Gate |
| `corpus/lessons/round-81.md`; `corpus/lessons/round-80.md` §Errata; `corpus/QUALITY.md` Q74; `LOG.md` | `13060d9b` | Round 81 |
| `.ufo/waves/round-81/{plan.md,probe,open,controls,close,w1-spec,w1-dispatch,w1.ready,w1/}` | `f8783f4b`, `2ac1f34d`, `13060d9b` | Round 81 |

The close commit `13060d9b8db4b1c18cc0c46594dbf943d5f9ac03` is the work revision this report cites, and
it is the pushed lane tip at filing (`git ls-remote origin refs/heads/master` → `13060d9b8db4…`).

## Before → after measurements

**C1 — operability (`ready-handoff`).** Counting command:
`node .ufo/waves/round-81/probe/probe81-c1.mjs --set c1 [--tool DIR]`, measured at
`d140f2883170cc1b0859ba5359bcdac3123a676e` (the instrument bytes it scores are the ones pinned by
`pin.ready-handoff`).

| state | reading | receipt |
|---|---|---|
| base tree (`git archive 77c7a8b3` → `--tool`) | `C81_C1: UNMET held=0/16` exit 1 | `controls/c1-base.txt` |
| constant-printer control | `C81_C1: UNMET held=3/16` exit 1 | `controls/c1-stub.txt` |
| M (lane) | `C81_C1: HELD held=16/16` exit 0 | `close/c1-probe.txt` |

**C2 — coverage:omp (self-describing receipt).** Counting command:
`node .ufo/waves/round-81/probe/probe81-c2.mjs --set c2 [--tool DIR]`, measured at the same revision.

| state | reading | receipt |
|---|---|---|
| base tree | `C81_C2: UNMET held=4/15` exit 1 (Amendment 2 re-measure; freeze-time fixtures read 1/15) | `controls/c2-base.txt` |
| constant-printer control | `C81_C2: UNMET held=6/15` exit 1 | `controls/c2-stub.txt` |
| M (lane) | `C81_C2: HELD held=15/15` exit 0 | `close/c2-probe.txt` |

Axis integers are unchanged by design: operability stays 9 (terminal under `f_O`; `A=889`, `C=41`),
coverage:omp stays 10 (clean `65/65`). What moved is the surface: a new capability row entered the
repertoire table (`ready-handoff`), and the O receipt gained its capture instant.

## Sources & frontier

- **SOURCES rows: 173 → 175** (`node scripts/sources-check.mjs` →
  `SOURCES_CHECK: CLEAN (rows=175 tiers=A:149,B:16,C:10 status=… entries_with_source=34 legacy=38)`,
  `close/sources-check.txt`). Rows added by tier: **tier A +2** (S236, S237), tier B +0, tier C +0.
  Rows touched old→new: S117 and S118 `used-by` (extension to `corpus/knowledge/two-reading-verdicts.md`
  reverted — the entry cites only S119); S236/S237 `mined` on admission. Captures:
  `SOURCE_CAPTURE: CLEAN captures=67 exemptions=108` (`close/source-capture.txt`); duplicate-URL ratchet
  `SOURCE_DUPES: CLEAN groups=6 known=6` (`close/source-dupes.txt`); fleet census
  `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kumitate` exit 0, six carried
  W04 (`close/sources-census.txt`).
- **Frontier advanced.** The OMP-harness-contract frontier item gained the *pre-dispatch admission*
  surface: `corpus/knowledge/ready-handoff-admission.md` binds the `.ready` contract, the dispatch agreement,
  the policy arithmetic and the fail-closed set at internals level, and names what admission cannot
  prove. The OMP-agent-plane frontier item gains the *receipt's own time*:
  `corpus/knowledge/self-describing-shape-receipt.md` records v2, the age disclosure, the opt-in staleness
  gate, the cutover and the custody argument (the pin, not the field). `corpus/README.md` map
  198 → 202.
- **Assimilation: none** — no `merge/kumitate/` theme was taken this round; the two entries are the
  lane's own frontier work (the `considerthese` proposal used is Q74's ground, recorded in the
  criterion).

## Trend verdicts

- **expansion — improved.** Two entries on ground the map did not hold (pre-dispatch admission; a
  receipt that carries its capture instant), two new tier-A rows with committed captures, the README
  map at 202/202/202, and the capability table +1 (`ready-handoff`).
- **quality — improved.** Both instruments gained behavior their base trees and constant printers
  cannot reach (C1 0/16 → 16/16, stub 3/16; C2 4/15 → 15/15, stub 6/15); three selftest suites grew
  (ready-handoff 31, census 97 → 98, proxy 163); the frozen arm found a real CLI defect
  (`--max-age` dropped by `main()`) and its regression case now exists; the 10th spotcheck recurrence
  was repaired with a committed transcript; the wave's mutation battery killed 10 of 11 C1 mutants and
  all 6 C2 mutants, and the one survivor (`realpathSync`, no symlink arm) is disclosed rather than
  counted as coverage.
- **discernment — improved.** The round's own gate was re-read against rounds 79 and 80 (both DRIFT,
  both dispatched anyway) and the gap is the first §Limits item rather than a hidden assumption; the
  connector named the two shared surfaces (`Report:` trailer, `.ready` lane identity) instead of
  claiming no overlap; the C2 scout's four findings (suite cannot see the CLI, a green checklist item
  over a rejected receipt, `--work` ENOENT, the proxy never naming v2) were fixed or disclosed.

## SHONEN

`SHONEN.md` has four boxes; each line names the evidence pointer, and no `[x]` is written because no
non-author promotion review has run in this round.

- [~] **SKILL.md contains real decision tables, error patterns, checklists, cited sources** —
  `SKILL.md:618` (the `ready-handoff` registry row with its refusal vocabulary and exit map) and
  `SKILL.md:755-756` (the two new checklist items), both executed by
  `node scripts/surface-probe.mjs --checklists` → `CHECKLIST: 41/41 pass` (`close/checklists.txt`).
- [~] **At least one end-to-end domain task executed and logged** — this round's dispatch is the
  task: the gate admitted the lane's own 14-seat handoff (`close/handoff-admission.txt`) and the
  evidence is logged at `LOG.md` §Round 81.
- [~] **Instructions executable by an agent without oral context** — `plan.md` + the two counters +
  `corpus/knowledge/ready-handoff-admission.md` re-derive both claims from committed bytes
  (`close/c1-probe.txt`, `close/c2-probe.txt`).
- [~] **No cross-domain bleed** — `PROVINCE.md` unchanged; the two sources are OMP-dispatch-adjacent
  (admission, caching) and the entries stay inside the lane's province.

## Wave findings and integration

One v1 wave, 14 seats; every landed report is under `.ufo/waves/round-81/w1/`. What the wave changed
in the round, and what it left disclosed:

- **`K81ScoutReconC1`** (handoff-chain recon): nine findings — the gate is not in the take path
  (H; rounds 79 and 80 re-read `DRIFT` and were dispatched anyway), the counter fixture arm was
  stale (H; fixed by Amendment 1 before any verdict), the handoff predates the gate's final bytes
  by 6 s (H; disclosed, and the close receipt re-validates against the pinned bytes), no
  wave↔dispatch binding (M), `l1` liveness (M), report-path resolution/uniqueness (M),
  `ARTIFACT_KEYS` narrower than the fleet bridge (M), role-taxonomy divergence (M), band authority
  duplicated with the policy (M). F1/F4–F9 are §Limits and round-82 candidates; F2/F3 are answered.
- **`K81ScoutReconC2`** (receipt-surface recon): four findings, three fixed in this round — the
  97-case suite could not see its own CLI dispatch (fixed: `cli-max-age` case, 98 cases), the new
  checklist item read green over a receipt the tool rejects and made the tool die of `EPIPE` (fixed:
  exit-asserting command + stdout error guard), `--selftest --work <missing>` was an uncaught ENOENT
  (fixed: `mkdirSync`). The fourth (the proxy never names the v2 receipt) is routed.
- **`K81ConnOverlap`**: boundary table against seven neighbour gates; **no duplicate** — every
  neighbour is post-hoc (post-commit, post-spawn, post-report) and `ready-handoff` is the lane's only
  pre-dispatch content gate. Two shared surfaces are named rather than hidden: the `Report:` trailer
  grammar (also `scripts/wave-census.mjs`) and the `.ready` lane identity (also
  `scripts/inline-dispatch-evidence.mjs`), each a different rule over the same field.
- **`K81ReviewC1` / `K81CriticClaims`**: per-arm reachability is clean (Q73), but the adversarial
  matrix A1–A9 all survives: the gate judges structure, not intent (a negated lane-root mention, role
  strings that contradict the prompts, a ghost `l1`, identical task bodies, zero connectors, a `=`
  relative path, missing `Report:` lines, a lying scratch sentence), and `--band`/`--attack-pct` can
  loosen the defaults. Disclosed in the lesson §Limits; liveness, report uniqueness and a connector
  floor are round-82 candidates.
- **`K81ReviewC2`**: C2 holds as claimed — every arm re-derived, the 15/15 reading reproduced, the
  v1 cutover confirmed (`--compare` accepts, `--shape` refuses), and the `stale-does-not-score` arm
  passes against a 45-day receipt. Its one reproduced discrepancy (the `stale-does-not-score` arm
  reads `DRIFT` while the stanza is mid-edit) is the same transient the other seats saw; at the final
  bytes the receipt reads `MATCH`.
- **`K81ExecC1Fixtures`**: three fixtures the gate got wrong — a case-variant duplicate seat and a
  `.ready` symlink escaping the lane were accepted; both fixed (`SEAT_DUPLICATE` is case-insensitive;
  `READY_UNSAFE` for a non-regular or escaping ready path) with three new selftest cases (31 → 34). The
  third (a seat's task text may name an absolute path outside the lane) is a limit, not a defect.
- **`K81ExecC2Fixtures`**: the age boundary is inclusive-on-the-day (`stale iff age > max_age`; a
  30-day receipt passes `--max-age 30`), the v2 refusals hold on every malformed shape, and the
  98-case suite was re-counted (`99 SELFTEST ok` lines, one named assertion). No contradiction.
- **`K81ExecMutate`**: twelve `ready-handoff` mutants, ten killed by the frozen counter; the one
  survivor is the `realpathSync` containment guard (no arm feeds a symlink that lexically sits
  inside the wave dir and resolves outside) — disclosed as a real coverage gap with an exploit
  transcript. Six `omp-census` mutants, all killed.
- **`K81RevWrongReady`**: the dispatcher's actual acceptance boundary (poll → `.ready.partial` →
  `.ready.dispatched` → results) and a load-bearing / over-strict / results-cosmetic classification
  of every refusal. It confirms `WAVE_MISMATCH` protects the L1's results-path expectation rather
  than the spawn, and that `LANE_MISMATCH`/`ROUND_MISMATCH` are cosmetic to the dispatcher but keep
  the handoff self-describing.
- **`K81ScribeCorpus`**: drafted both entries against the landed files and the two captures; no
  correction was needed (its `.ufo/waves/round-81/w1/K81ScribeCorpus-captures/pre-existing-drafts.txt` records the comparison), and it made no lane
  write beyond its report and capture directory.

## Round shape, seats and residual calls

- Shape: **ONE v1 wave** under the fleet wave policy (band 8–16), plus the L1's
  canonical planner seat (the validator rejects `planner`).
- Wave 1: **14 seats** — scouts 2, connector 1, executors 3, mutation-tester 1, reviewers 2, critic 1,
  sentinel 1, scribes 2, revenger 1. Policy-attack seats (reviewer/critic/mutation-tester/labrat)
  4/14 = **29 %**; the sentinel is a fifth adversarial seat (5/14 = 36 % by the looser reading).
  Connectors 1 (cap 2).
- Residual calls: none. Round total: **14 seats**.
- Settlement: `WAVE-DONE kumitate r81 w1: all 14 seats settled`
  (`.ufo/waves/round-81/w1-results.json`, `seats: 14`, 14 result rows).
- **Dead seats: 2, never replaced.** `K81MutC1` (mutation-tester) and `K81Sentinel` (sentinel) each
  settled with an empty final output and wrote no report file at
  `.ufo/waves/round-81/w1/<name>.md`; neither was live at settlement. Their ground is partly covered
  by other seats — `K81ExecMutate` ran twelve C1 and six C2 mutants (so the mutation duty is met with
  a different seat's matrix, not the dead seat's), and `K81ExecC1Fixtures`/`K81ReviewC2` exercised the
  symlink, escape and path cases the sentinel would have attacked. Per QUALITY Q67 the settled-output
  count (14) and the report-file count (12) are stated separately, and the two exceptions are named
  here rather than inferred.
- Reports present (12): `K81ScoutReconC1`, `K81ScoutReconC2`, `K81ConnOverlap`, `K81ExecC1Fixtures`,
  `K81ExecC2Fixtures`, `K81ExecMutate`, `K81ReviewC1`, `K81ReviewC2`, `K81CriticClaims`,
  `K81ScribeCorpus`, `K81ScribeLesson`, `K81RevWrongReady`.
- Guards: every seat ran inside `/fast/scratch/hyaku/kumitate-r81/<seat>/` and removed its scratch;
  no seat wrote a runnable into the lane tree (`A` = 889 at close, measured twice).

## Stale-lane

`Stale-lane: respawn-per-round driver; no other kumitate mission is open.`

## Tool installs and L0

- Tool installs: none this round (no package manager, no binary fetched; the two captures are web
  pages, not tools).
- L0: no new question. The carried `kumitate | round-78` question (the K composite ruling) is
  unaffected: round 79 landed option (b) and this round does not move the K terms.

## Routed repairs, limits and open questions

R80-1 … R80-12 and the wave's findings are answered in `corpus/lessons/round-81.md` (§Routed-defect
answers, §Limits): the gate is advisory until the orchestrator calls it; no wave↔dispatch binding,
`l1` liveness or report-path uniqueness; `ARTIFACT_KEYS` narrower than the fleet bridge; role and band
authority duplicated between the gate and the validator/policy; `captured_at` is self-asserted; and
`plan-before-ready --round 81` reads `FAIL … MAP_DRIFT` because the plan was frozen before the
recurrence repair (the r80 D3 class). Each is a round-82 candidate in `SCORECARD.md` §Planned.
