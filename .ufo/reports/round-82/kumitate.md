# kumitate — round 82 report

Lane: **kumitate** — operability + coverage (orchestration and tooling: OMP task/hub dispatch,
ufo-fsd scripts, `crates/ufo-core-runtime`). Round 82, attempt 1, Linux run-15 host.
Lane repo `/home/vgpnk/Projects/shokunin/kumitate-shokunin`. Base
`0c23c4fca408591341f22bad58660ac81e1ec5ff` (the round-81 verifier spot-check, the lane's remote tip).
Freeze `97a630123a8980aa2dba4864998400ab5351dbe3`; scaffolding
`63b12695ca3599d92c6d128353ca987daf64365b` (tools + suites) and
`c4396021c31e5d631c3ec498b4fa81cef1b98b46` (wave payload, S238/S239 + captures); work revision
**M = `125287f347a0f2841abeaa37e03a3b2cd1fc15c9`**; close receipt set
`3355efb43eb4d0a14893c6e47ba6015f4802755c`; wave evidence and integration
`67be18f25e74d5bdae44211c211015d5ca6e0417` (**the lane tip this report cites and that
`git ls-remote origin refs/heads/master` prints**). This report is filed in the fleet repo under the round-82 report directory.

## Work performed

Round 82 declares **two claims on two axes**: **C1 operability** — the lane's lowest non-retired axis
(integer 9, terminal under `f_O`) — a capability deepening of `ready-handoff` to
`kumitate-ready-handoff-v2`; **C2 coverage:omp** (integer 10 held) — the OMP-plane evidence surface
gains the receipt's own age on the compare path.

- **C1 — the handoff gate binds what it judges.** `scripts/ready-handoff.mjs` now reads the seat band
  (`sighting.dispatch.swarm.waveMinLanes`/`waveMaxLanes`) and the seat-role vocabulary
  (`nativeProfiles.omp-native-v1.proposalRoles`) from `--policy` instead of restating them; refuses a
  dispatch whose basename is not `<wave>-dispatch` (`WAVE_BINDING`) or whose payload `wave` is not this
  slot or `-<slot>` (`DISPATCH_WAVE`); refuses two seats that resolve to one `Report:` destination
  (`REPORT_DEST_DUPLICATE`) or a destination outside the lane (`REPORT_DEST_OUTSIDE`); refuses
  `ready.l1` colliding with a seat (`L1_SEAT_COLLISION`) and resolves `l1` against a caller-supplied
  `--agents` registry (`L1_UNRESOLVED`, `AGENTS_ABSENT`/`AGENTS_MALFORMED` exit 2). Suite 34 → 54
  cases: `close/c1-suite.txt` → `READY_HANDOFF_SELFTEST: 54/54 pass`, `VERDICT: PASS`, exit 0. Frozen
  counter `close/c1-probe.txt` → `C82_C1: HELD held=22/22`, exit 0.
- **C2 — the receipt carries its age on the compare path.** `scripts/omp-census.mjs --compare` prints
  `receipt_captured=<date> age_days=<n>` (`captured=absent age_days=absent` for a legacy v1 receipt),
  gates an opt-in `--max-age DAYS` (`SHAPE_STALE_RECEIPT`, exit 1) and refuses to guess a legacy
  receipt's age (`SHAPE_AGE_UNKNOWN`, exit 2); the age never enters `coverage:omp`. Suite 98 → 105
  cases: `close/c2-suite.txt` → `VERDICT: PASS (105 cases)`, exit 0. Frozen counter
  `close/c2-probe.txt` → `C82_C2: HELD held=13/13`, exit 0.
- **The wave's own handoff is the real run**: `close/handoff-admission.txt` →
  `READY_HANDOFF: READY wave=w1 seats=14 attack=4/14 connector=1 roles=scout=2,executor=3,scribe=2,connector=1,reviewer=2,critic=1,mutation-tester=1,sentinel=1,revenger=1 policy=ufo-wave-policy.json agents=none`,
  exit 0.
- **The live compare path**: `close/census-shape.txt` →
  `OMP_SHAPE_COMPARE: IN_SYNC entries=65 receipt=65 added=0 removed=0 changed=0 transient=0 receipt_captured=2026-11-04 age_days=0`,
  exit 0 (and `OMP_CENSUS: CLEAN … captured=2026-11-04 age_days=0`).
- **Open repair before the freeze** (planned candidate 4): the 11th spotcheck-coverage recurrence
  (`corpus/lessons/round-81-verifier-spotcheck.md`) was adopted in the freeze commit —
  `open/spotcheck-map.txt` → `SPOTCHECK_COVERAGE: CLEAN spotchecks=48 uncovered=0`, `MAP: CLEAN`,
  `README_MAP: CLEAN files=203 rows=203 covered=203`.
- **Frontier step** (in the claim cap, not a third claim): S238 (Kubernetes *Validating Admission
  Policy*, tier A, **admit**) and S239 (Open Policy Agent docs, tier B, **reject** with reason and
  flip condition — R81-6's reject sample) opened this round with committed captures; two knowledge
  entries cite them; the lesson carries URL + access date + located ≤25-word quotes with re-derived
  counts (Q74).
- **considerthese**: `considerthese/2026-10-26.md` idea 1 ("every number has a transcript") mined into
  `corpus/QUALITY.md` **Q75**, grounded on the round-81 routed defects R80-8/R81-4; idea 3 is already Q68 and
  is not re-mined.
- **Routed defects R81-1 … R81-8** answered in `corpus/lessons/round-82.md` §Routed-defect answers;
  the round-81 lesson's open map reading corrected by an append-only erratum.
- **Wave**: one v1 wave, 14 seats (attack 4/14 = 29 % by the campaign policy's four attack roles;
  `sentinel` is a fifth adversarial seat, 5/14 by the looser reading), connector 1, executor 3,
  scribe 2, scout 2, revenger 1; the canonical planner seat is held by the L1 (the validator refuses
  `planner` as a swarm role).

## Landed changes

| commit | what | LOG entry |
|---|---|---|
| `97a63012` (freeze) | plan, both frozen counters (22 / 13 arms), four controls, open receipts, the 11th spotcheck adoption | `LOG.md` §Round 82 |
| `63b12695` | `ready-handoff` v2 + suite 34 → 49, `omp-census` compare age + suite 98 → 105, plan Amendment 1 | `LOG.md` §Round 82 |
| `c4396021` | report-destination parsing on the rendered trailer, wave-id prefix agreement (suite 50), wave payload (spec, dispatch, registry, ready + dispatched marker), S238/S239 + captures, Amendment A1.6 | `LOG.md` §Round 82 |
| `125287f3` (M) | the work revision: suite 54 with the containment rule, two knowledge entries, lesson (Gate, four mistakes, routed answers, limits, verification), `corpus/QUALITY.md` Q75, SCORECARD §Round 82 + stanza (A=891 C=42 C2=206, two re-pins), LOG entry, `corpus/README.md` origin-path repair, S237 `used-by`, Amendments 1–2 | `LOG.md` §Round 82 |
| `3355efb4` (close) | the close receipt set at M: both counters, both suites, proxy, checklists 42/42, harm matrix CLEAN, every source/map/census gate, plan-before-ready | `LOG.md` §Round 82 |

Every change is inside the lane repo; the only main-repo write is this report.

## Before → after measurements

Both claims were frozen before any data seat and controlled before data (`.ufo/waves/round-82/plan.md`
§Claims; `controls/`). A claim is **killed** if its frozen counter reads `HELD` on the base tree or on
a constant-answer stub — both measured, neither held.

| claim | before (base `0c23c4fc`) | after (M `125287f3`) | counting command |
|---|---|---|---|
| **C1** operability — `ready-handoff` v2 | `C82_C1: UNMET held=0/22` (`controls/c1-base.txt`; the v1 tool answers `unknown argument: --policy`, exit 64); constant-`READY` stub `held=6/22` (`controls/c1-stub.txt`) | `C82_C1: HELD held=22/22` exit 0 (`close/c1-probe.txt`); suite 34 → 54 (`close/c1-suite.txt`) | `node .ufo/waves/round-82/probe/probe82-c1.mjs --set c1 --lane .` |
| **C2** coverage:omp — the receipt's age on the compare path | `C82_C2: UNMET held=6/13` (`controls/c2-base.txt`: round 81's compare already holds the five plain-diff arms and `--shape --max-age`; none of the seven new arms); stub `held=4/13` (`controls/c2-stub.txt`) | `C82_C2: HELD held=13/13` exit 0 (`close/c2-probe.txt`); suite 98 → 105 (`close/c2-suite.txt`) | `node .ufo/waves/round-82/probe/probe82-c2.mjs --set c2 --lane .` |

Same-commit re-measure at M (`close/proxy-check.txt`): `PROXY: MATCH (A=891 C=42 operability=9;
C1=19/19 C2=206/206 coverage=10; S=88/88 coverage:script-layer=10; R=92/92 coverage:runtime-layer=10;
K=55/55 coverage:kimi-layer=10; O=1/1 O_members=65 O_findings=0 O_bound=35 coverage:omp=10; pins=6
match; src-rev=31c465f15669; source=snapshot)` exit 0. From the round-81 close: A 889 → 891 (the two
frozen counters), C 41 → 42 (the compare-age checklist item), C2/C2_total 202 → 206 (two knowledge
entries + the lesson + the adopted spot-check row), `pin.ready-handoff` `f8fc11f1…` → `7e9827ad…`,
`pin.omp-census` `ba7cbc8f…` → `92180f3c…`.

**No axis harmed**: `close/harm-matrix.txt` → `HARM_MATRIX: CLEAN gates=36 held=32 repaired=2 carried=1
moved=1 new=0 gone=0 harm=0 harm_absent=0 new_red=0 unmeasured=0 ancestor=yes … base=0c23c4fca408
tip=125287f3` exit 0.

## Sources & frontier

`corpus/SOURCES.md` rows **175 → 177** (`corpus/SOURCES.md`; counting command
`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` → `177`, and
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kumitate`
→ `kumitate ok …/corpus/SOURCES.md`, exit 0, six carried W04 warnings). Tier histogram
(`close/sources-check.txt`) `A:150,B:17,C:10` from `A:149,B:16,C:10`; status
`queued:13,mined:142,rejected:22` from `mined:141,rejected:21`.

- **Rows added by tier**: S238 (Kubernetes *Validating Admission Policy*, `docs`, tier **A**, `mined`,
  capture `.ufo/waves/round-82/build/L1/captures/vap.html` sha256 `ae87bdab…`) and S239 (Open Policy
  Agent *Introduction*, `docs`, tier **B**, **`rejected`** — "a runtime decision service the caller
  queries, not a static rule document a gate reads offline"; flip recorded, capture
  `…/opa-docs.html` sha256 `75ea1452…`). `SOURCE_CAPTURE: CLEAN captures=69 exemptions=108`
  (`close/source-capture.txt`); `SOURCE_DUPES: CLEAN groups=6 known=6` (`close/source-dupes.txt`).
- **Rows touched old → new**: S237 `used-by`
  `corpus/knowledge/self-describing-shape-receipt.md` →
  `corpus/knowledge/self-describing-shape-receipt.md, corpus/knowledge/receipt-age-on-the-compare-path.md`
  (logged in `corpus/lessons/round-82.md` §Gate). No `status` or `recheck` change. S237's `anchor`
  cells says §5.1/§4.2 while the quoted sentence lives in **§4.2.3** (capture lines 2294-2297) — a
  correction that must ride a superseding row (CORPUS rule 2 forbids editing the cell), recorded in
  the lesson.
- **Frontier rows advanced**: the orchestration/tooling frontier band gains the admission-binding and
  receipt-age ground through `corpus/knowledge/handoff-binding-and-liveness.md` and
  `corpus/knowledge/receipt-age-on-the-compare-path.md` (README map 203 → 206 files / rows / covered,
  `close/spotcheck-map.txt`). **Assimilation: none** this round — the two claims are discipline claims
  and the staged `merge/kumitate/` package needs its own id-collision + quarantine pass.
- **Sourced claim**: C1's evidence cites **S238** in the admitted entry that carries its Gate row and
  its captured quote; `CITE_SOURCES: CLEAN cited=226` (`close/cite-sources.txt`).

## Trend verdicts

- **expansion — improved.** Two admitted knowledge entries on ground the README map did not hold
  (handoff binding and liveness; the receipt's age on the compare path), each `source:` citing a row
  opened this round (S238 `mined`; S237 extended), two new rows with committed captures, and the map at
  206/206/206 (`close/spotcheck-map.txt`). The capability table gains no new *name* — `ready-handoff`
  and `omp-census` are deepened, which is quality, not expansion — so this trend rests on the corpus
  delta, which is real.
- **quality — improved.** Both instruments gained behaviour their base trees and constant printers
  cannot reach (C1 0/22 → 22/22, stub 6/22; C2 6/13 → 13/13, stub 4/13); both suites grew (54, 105);
  the wave's mutation batteries killed 11/12 C1 mutants and 7/8 C2 mutants, and the two survivors are
  named with their cause (`close/…`, lesson §Limits). Three defects were found and repaired in-round:
  the rendered-trailer parse (caught by the real handoff, not the suite), the unbounded report
  destination (caught by the C1 scout), and the refusal-token conflation (caught by the frozen arms).
  The 11th spotcheck recurrence was adopted before the freeze.
- **discernment — improved.** The round's own scout measured that the new destination rule bounded
  nothing and the repair landed with a case that fails without it; the revenger showed the role
  vocabulary is one authority gate↔policy but **not** validator↔policy (the validator hard-codes
  `SWARM_ROLES`), which the report states as a limit instead of claiming "one authority" outright; the
  C2 scout named eleven consumers of the compare line, two of which are revision-bound and no longer
  reproduce (disclosed); the Gate carries a considered-and-rejected source (R81-6).

## SHONEN

`SHONEN.md` has four boxes; each line names its evidence pointer, and no `[x]` is written because no
non-author promotion review has run in this round.

- [~] **SKILL.md contains real decision tables, error patterns, checklists, cited sources** —
  `SKILL.md:618` (the `ready-handoff` registry row, now v2: the eight judgments, the twelve refusal
  tokens, the policy-derived band and roles, the 54-case suite) and `SKILL.md:617` (the `omp-census`
  row with the round-82 compare-age clause); two checklist items (`SKILL.md:755`, `SKILL.md:756`) run
  both suites — `CHECKLIST: 42/42 pass`, `VERDICT: PASS` (`close/checklists.txt`).
- [~] **At least one end-to-end domain task executed and logged** — this round's dispatch *is* the
  task: the gate admitted the lane's own 14-seat handoff against the campaign policy
  (`close/handoff-admission.txt`), and the wave it admitted landed. Logged at `LOG.md` §Round 82.
- [~] **Instructions executable by an agent without oral context** — `.ufo/waves/round-82/plan.md` (claims, predicates,
  Amendments 1–2) + both frozen counters + the two entries re-derive every claim from committed bytes
  (`close/c1-probe.txt`, `close/c2-probe.txt`).
- [~] **No cross-domain bleed** — `PROVINCE.md` unchanged; the two sources are admission/caching
  primitives used inside this lane's own instruments; the revenger read the origin tree read-only and
  no sibling lane's file was touched.

## Round shape, seats and residual calls

One **v1 wave** (`w1`) of **14 seats** under `/home/vgpnk/Projects/shokunin/scripts/hyaku/ufo-wave-policy.json`
(band 8–16), validated by `ufo-swarm-wave.mjs run` and committed before dispatch
(`.ufo/waves/round-82/w1-spec.json`, `w1-dispatch.json`, `.ufo/waves/round-82/w1/swarm-registry.json`, `w1.ready` +
`w1.ready.dispatched`). Role mix: scout 2, executor 3, scribe 2, connector 1, reviewer 2, critic 1,
mutation-tester 1, sentinel 1, revenger 1. Attack share: **4/14 = 29 %** by the campaign policy's four
attack roles (reviewer, critic, mutation-tester, labrat — `labrat` cannot be a seat), **5/14 = 36 %**
counting the sentinel. Connector seats: 1 (cap 2). Residual calls: **none** — the wave alone is the
round (14 seats, inside the 8–16 band; the §3 L2 floor of 8 is met inside it). The canonical planner
seat is held by the L1: the validator refuses `planner` as a swarm role (orchestrator ruling
2026-10-19), so the §3 planner obligation rides the L1's own plan freeze and the wave's scouts.
Scratch root `/fast/scratch/hyaku/kumitate-r82/<seat>/`; the lane's own build scratch is removed.
**Settled 14/14, reports 11/14; dead seats 3** (`K82ReviewC1`, `K82MutCounters`, `K82Sentinel` —
settled with empty or partial output and no report, never replaced; their last text is in
`w1-results.json` and their ground is partly covered by `K82ReviewC2`, `K82CriticClaims` and the two
mutation batteries).

## Stale-lane

Lane round 82 launched `2026-11-04T07:45:55-03:00` (the fleet watchdog log line
`launch kumitate round=82 pgid=1970144 driver=hyaku-inline attempt=1`). Every lane write of the round
(`97a63012`, `63b12695`, `c4396021`, `125287f3`, `3355efb4`) falls after the launch, so the mission was
**progressing**, not silent; no earlier attempt of this round exists (no `lane-dead-no-report` line).
Respawn-per-round driver; no other mission of this lane is open.

## Tool installs and L0

No tool was installed or upgraded this round: no `uv`, `npx`, `npm`, `cargo` or `pacman` transaction
ran (pacman stays paused host-wide per the orchestrator ruling). L0: nothing appended this round —
the two open questions this lane carries (`kumitate | round-42` on the lane-owned gate-pins block and
`kumitate | round-78` on the Kimi composite) are unchanged and were routed around, not treated as
answered.

## Routed repairs, limits and open questions

- **Repairs landed, not claimed**: R81-1 … R81-8 answered in `corpus/lessons/round-82.md`; the
  round-81 lesson's open map reading corrected by an append-only erratum; `corpus/README.md`'s origin
  path corrected from `origin-work/ufo-fsd-alpha` (absent on this host) to
  `/home/vgpnk/Projects/ufo-fsd-alpha`; S237 `used-by` extended; the 11th spotcheck recurrence adopted
  before the freeze; considerthese idea 1 → `corpus/QUALITY.md` Q75; the wave scout's unbounded
  destination repaired as `REPORT_DEST_OUTSIDE` (plan Amendment 2).
- **Limits stated, not hidden** (`corpus/lessons/round-82.md` §Limits): the gate is advisory (the
  dispatcher's take path never calls it — orchestrator-owned); `--agents` liveness is opt-in and its
  registry shape does not match the validator`swarm-registry` shape (`.ufo/waves/round-82/w1/swarm-registry.json`); the band is policy-derived while
  the attack share and connector cap stay lane constants; the gate counts spawns where the validator
  bands on spawns + resumes (scout F1); role vocabulary is one authority gate↔policy, not
  validator↔policy (the validator hard-codes `SWARM_ROLES`; revenger V4); the compare age is
  self-asserted and never scores; the C2 counter has no arm for a future-dated compare receipt (the
  `c8` mutant survived); a constant printer can reach 7/22 and 7/13 (the plan's stub bounds describe
  the frozen fixtures only).
- **Open questions carried**: `kumitate | round-42` (lane-owned `kumitate-gate-pins-v1` block) and
  `kumitate | round-78` (Kimi composite) — both still unanswered; this round neither depends on them
  nor acts on them.

## Wave findings and integration

One v1 wave, 14 seats; all 14 settled (`w1-results.json`, `seats: 14`), **11 wrote a report** under
`.ufo/waves/round-82/w1/`, and **three settled without one, never replaced**: `K82ReviewC1` (empty
output), `K82MutCounters` (mapped both counters, no matrix) and `K82Sentinel` (started the census
read). Their ground is partly covered by the second reviewer, the critic and the two mutation
batteries; the gap is named, not papered over. What the wave changed in the round, and what it left
disclosed:

- **`K82ScoutReconC1`** (validator vs gate, 15 findings): **F7 (H→repaired)** the new
  `REPORT_DEST_DUPLICATE` bounded nothing — `/var/tmp` destinations read READY — closed by
  `REPORT_DEST_OUTSIDE` with a case that fails without it (plan Amendment 2 A2.1); F1 (H) the gate
  counts `taskCall.tasks` while the validator bands on spawns + resumes, so a validator-accepted wave
  can be refused and resume lanes are unjudged; F3/F4/F5/F6/F8/F10/F11 grammar and authority
  divergences (ceiling, role duplication, attack vocabulary, godspeed regex, trailer wording, band
  source, seat-name grammar, unread dispatch evidence fields) — all §Limits + round-83 candidates.
- **`K82ScoutReconC2`** (compare-line consumers): eleven consumers mapped; two are revision-bound and
  no longer reproduce after the suffix (`w1/…`-frozen round-78 probe uses full-line equality; a
  `receipt-evidence` record minted before this round cannot replay) — disclosed, not repaired; the
  round-81 knowledge template omitted `transient=` since round 79 and now also the age fields.
- **`K82ExecMutate`** (C1 battery): 12 single-defect mutants, **11 killed**; `m11` (the realpath
  containment) survived as behaviourally inert behind the lstat guard, exactly as Amendment 1 A1.2
  disclosed. Nine of the twelve are caught by a dedicated counter arm; two (`m9`, `m12`) only by the
  tool's own suite — which is itself frozen arm 22.
- **`K82ExecCensusMutate`** (C2 battery): 8 mutants, **7 killed**; `c8` (delete the `SHAPE_CLOCK`
  branch on the compare path) survived 13/13 — the counter has no future-dated arm. A counter gap,
  recorded for round 83, never closed by editing a frozen counter after data.
- **`K82ExecGates`** (17-row battery at M): every gate green except the close-in-flight red —
  `ROUND_GATE … SCORECARD_ROW_MISSING` (no `| 82 |` move-log row) and `SCORECARD_PLAN_MISSING`. Both
  are repaired in the integration commit (two move-log rows + the round-83 pre-registration); the
  gate now reads `ROUND_GATE: CLEAN (round=82 lane=kumitate checks=10 errors=0 warnings=0)`.
- **`K82ScribeEntry1` / `K82ScribeEntry2`**: the two knowledge entries. Entry 1's seat report states
  the S238 quote as 13 words where `printf … | wc -w` reads **12** (Q74's class, caught by the L1);
  entry 2 found that S237's `anchor` cell says §5.1/§4.2 while the quoted sentence lives in **§4.2.3**
  (`.ufo/waves/round-81/build/L1/captures/rfc9111.html:2294-2297`) — recorded for a superseding row.
- **`K82Connector`** (rule→copy tables): five rule families mapped with an authority column; one
  genuine landed repair — `corpus/README.md` pointed every reader at
  `/home/vgpnk/Projects/origin-work/ufo-fsd-alpha`, **absent on this host** (the origin tree is
  `/home/vgpnk/Projects/ufo-fsd-alpha`, HEAD `fb7157fc`) — and two drift risks named (the band's two
  sources; the `.ready` lane identity parsed by two tools).
- **`K82ReviewC2`** (C2 adversarial): 30+ fixtures; every promised refusal reproduced exactly
  (`SHAPE_AGE_UNKNOWN`, `SHAPE_STALE_RECEIPT`, `SHAPE_INVALID`, `ROOT_NOT_A_DIR`, usage 64); the
  boundary is strict `>` (`age == max-age` passes); sub-day future receipts are race-sensitive only
  because the process starts after materialisation, and the deterministic proofs are in its §3.
- **`K82CriticClaims`** (claim falsification): independent reproduction of the base (`0/22`, `6/13`)
  and M (`22/22`, `13/13`) readings; the kill rule holds — the strongest constant printers reach
  **7/22** and **7/13**, both far below the predicates; M2/M3 flag that the plan's stub bounds describe
  the frozen fixtures only (recorded in the lesson's limits); it also confirms the frozen control
  receipts still carry the pre-A1.2 arm name, which the `controls/*-rerun.txt` receipts answer.
- **`K82Revenger`** (validator internals): V1–V11 from the source — `SWARM_ROLES` is a hard-coded ten,
  the validator never reads `proposalRoles` (so the round's "one authority" is gate↔policy, **not**
  validator↔policy), it writes no dispatch file (the operator does), it copies `wave` as a free label,
  it bands on spawns + resumes, and the gate's `--agents` shape does not match the validator's
  `.ufo/waves/round-82/w1/swarm-registry.json` shape.
