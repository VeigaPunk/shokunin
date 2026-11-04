# kake round 78 — attempt 1

## Work performed

Declared claims: **C1 calibration** — population-bound SHONEN self-assessment;
**C2 freshness** — clean evaluated offline paths with a red planted-citation control;
**C3 operability/capability** — offline page-level robots declarations.

**Verdicts:** C1 measured met; C2 measured met within its offline scope; C3's explicit
finite table measured met, but the **combined contract remains unprovable** because its
g26 expectation and general nosnippet/video-collapse prose conflict. No post-score
expectation was changed to conceal this. This is an honest stop, not self-admission.

- Added population declarations and floor-aware grading; the counter executes the committed
  c77 dependency and checks four examined boxes. Evidence: lane
  `.ufo/waves/round-78/controls/after-c1-population.txt`, `w1/ReviewC1.md`, `w1/CriticC.md`.
- Repaired sixteen missing citation annotations through the line-sha-bound freshness
  sidecar, preserving historical corpus prose, then pinned the lowercase absent target.
  The wrapper now measures archived revision bytes and hashes its path-decision inputs.
  Evidence: `w1/ExecC2Annotate.md`, `w1/ReviewC23.md`, `controls/after-c2-counter.txt`.
- Implemented expectation-free HTML audit, opaque oracle-free matrix inputs, fixed case
  identities, three-field grading, selftest conjunct, constants and sibling-label control.
  Evidence: `controls/after-c3-matrix.txt`, `w1/ExecC3Tool/realrun.txt`.
- Opened documentation, admitted one knowledge entry, corrected the previous sitemap
  coverage omission, mined mistakes and added grounded criteria. Evidence:
  `corpus/lessons/round-78.md`, `corpus/QUALITY.md`, `PROVINCE.md`, `corpus/README.md`.
- Re-cut evidence and recorded prior-round errata, without rewriting filed reports.
  Evidence: `w1/ExecReceipts/sentinel-f1-recut.txt`, `controls/doc-quote-truth-final.txt`.

Round shape: **one v1 wave, fourteen seats**, requested and settled. Roles: scout 2,
executor 5, scribe 2, reviewer 2, critic 1, mutation-tester 1, connector 1; attack share
4/14; L1 holds planner. No residual call. Parent delivered **WAVE-DONE** before this
report; handoff `w1-results.json` contains fourteen nonempty outputs, no failed output.
No original dispatched seat is recorded dead. A later auxiliary wake failed with provider
402 insufficient_balance. Bare-name follow-ups also woke old round-77 CriticC/MutC
identities alongside current CriticC-2/MutC-2, causing a documented report/scratch
collision; those are not invented replacement seats. See the retained critic/mutation
reports; official wave accounting comes from the handoff.

Stale-lane: progressing through pushed lane commits; no other kake mission is claimed.
No tools installed/upgraded, pacman untouched, no publication/deployment or domain-source
write. Fleet misroot sweep showed only orchestrator state, other-lane report and pre-existing
`after`; none was identified as this wave's misplaced output or removed.

Self-evaluation: accuracy 3 (g26 specification contradiction disclosed), completeness 4
(all requested round artifacts landed; no combined-contract admission claimed), clarity 4
(explicit measured-versus-unprovable distinction), actionability 4 (committed commands and
receipts), conciseness 3 (large inherited evidence surface); average 3.6. Highest-impact
next improvement is a new pre-data claim resolving g26, not a retarget of this scored round.

## Landed changes

All work ties to **LOG.md, Round 78**.

- Freeze: `78711a628ad7e1c23cefcb9f9e345a0cc240c25b` — contract, controls, counters,
  validated spec/dispatch. Terms amendments: `c758904c15c21a3c0287737c47e193ea7f08d766`,
  `a5d7b7a5ebed5a366612a4a4da5756f693e6ae02`,
  `715795eb134cc4e623240a01a4df943285b71a0d`,
  `e409f6c1f16d2ab72fb1ff53a4b438aa9b6583b7`.
- Measured implementation carrier: **`82c3d02c39d16ae99c6cd34238fa3ec6ea089fb9`** —
  ledger/sidecar/pin, tool/cases/matrix, sources/knowledge and lesson.
- Settled receipts, SCORECARD/LOG/QUALITY and final documentation:
  `406021c765fd77acd93aa17bc2df5c981b634aec`.
- Final quote receipt: **`b9419b4668fb0dfb29da2a9d28953a7ea912f0ad`** — final lane tip.

Pre-report remote proof, command `git -C <lane> ls-remote origin refs/heads/master`:

```
b9419b4668fb0dfb29da2a9d28953a7ea912f0ad	refs/heads/master
```

An accidental L1 edit briefly deleted LOG.md locally; it was restored byte-exactly from
master immediately, before any commit. No historical LOG entry was deleted in landed work.

## Before → after measurements

Measured implementation revision for the three after receipts:
`82c3d02c39d16ae99c6cd34238fa3ec6ea089fb9`; base:
`fe50945399a386b48678b1f2051fdbe8a77b10bd`. Later commits record evidence/docs.

### C1 — calibration, score 2 → 2 HOLD

Command: `python3 -B .ufo/waves/round-78/c78_shonen_population.py --root . --revision <rev>`.
Base: no row declares its population; counter exits 1 (`controls/base-c1-population.txt`).
After, full receipt line:

```
C1v1 revision=82c3d02c39d16ae99c6cd34238fa3ec6ea089fb9 rows=4 rows_with_population=4 undeclared=0 stale_populations=0 exact_mismatches=0 floor_violations=0 growth_tolerated=4 met=true
```

Exit 0; selftest nine cases passed. Population snapshots remain exact; growing
count-at-least observations are floors. A wrong population and missing declaration fail.
Box two remains a genuine gap. The counter does not yet establish semantic equivalence
between a declared population path and the surface its checks scan.

### C2 — freshness, score 10 → 10 HOLD

Command: `python3 -B .ufo/waves/round-78/c78_sweep_truth.py --root . --revision <rev> --work <scratch>`.
Base: sweep exit 1, one drift and one new-missing token; pin-only control remains red.
After, `controls/after-c2-counter.txt`:

```
C2v1 revision=82c3d02c39d16ae99c6cd34238fa3ec6ea089fb9 sweep_exit=0 drift=0 new_missing=0 paths_ok=true skipped=2 control_exit=1 control_drift=1 tree_identity=fd15d86be09fcf50 met=true
```

Exit 0. Standing sweep selftest remains 36/36; wrapper selftest 6/6. Remote armed checks
are skipped and history suspended: neither is a pass, and this is not a complete publishing
check. The existing round-69 operator question is not treated as an operator ruling.

### C3 — operability, score 10 → 10 HOLD; bounded repertoire demonstrated

Command: `python3 -B .ufo/waves/round-78/c78_meta_robots_matrix.py --root . --tool-revision <rev> --cases .ufo/waves/round-78/cases --consts .ufo/waves/round-78/consts --work <scratch>`.
Base tool absent (`controls/base-c3-absent.txt`, cat-file exit 128).
After, `controls/after-c3-matrix.txt`:

```
C3v1 revision=82c3d02c39d16ae99c6cd34238fa3ec6ea089fb9 cases=36 decided=36 correct=36 wrong=0 constants_failed=4/4 met=true
selftest_ok=true selftest=94/94 selftest_exit=0 selftest_tail=["selftest: 94/94 passed"]
```

Matrix exit 0; its own selftest 16/16. Four constants fail 32, 8, 25 and 36 cases;
sibling-expect reader rejected. Tool digest:
`886e88618f7064fb32b95f469ce825bd405b5ae943ba3e100bc0c645cf560ba3`.
Real run uses eight previously retained pages out of twelve named surfaces, validates
retained digests and exits 0; it is not a fresh live fetch or site-correctness claim.

**Limit/admission:** g26 retains video:-1 beside synthesized nosnippet, while generic prose
says nosnippet suppresses video limits. The explicit table is measured; the combined
specification cannot be proven. ReviewC23 also demonstrated a non-ASCII agent-casefold
mutant surviving both matrix and selftest. Date-order/weekday mutants are guarded only
by tool selftest. These remain disclosed, not silently closed by post-score cases.

Final record quote check at `406021c7`, `--rounds 78`, exit 0:

```
C1v2 revision=406021c7 rows=20 receipt_files=8336 spans=0 exempted=0 corrections=0 findings=0 met=true
```

This reports its actual span population, not universal prose verification.

## Sources & frontier

Command at start and end:
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kake`.

Start retained observation (`controls/census-start.txt`):

```
kake	ok	/home/vgpnk/Projects/shokunin/kake-shokunin/corpus/SOURCES.md
CENSUS_EXIT=0
```

End full output: `controls/census-end.txt`, exit 0, ending:

```
kake	ok	/home/vgpnk/Projects/shokunin/kake-shokunin/corpus/SOURCES.md
```

Spacing-tolerant row count: `grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`:
186 → 189. Three new tier-A mined rows: S449 Google directives, S450 WHATWG head/meta,
S451 RFC3339 scoped to this audit. Inherited status/recheck/used-by cells unchanged.
Warning rendering (from the named census runs): 17 → 19 W04; new cross-scope URL
warnings S450 and S451. Both sources were opened this round; lesson Gate names dates,
locations and short quotes for all new rows, plus rejects with flips.

One new knowledge entry moves page-directive ground into held publisher-side audit
coverage. PROVINCE/README also receive the round-77 sitemap format correction that
previous round's report overstated. No crawler behaviour, browser-driving or indexing
result is absorbed from adjacent lanes; connector evidence is `w1/ConnectorC.md`.

Assimilation: none. Registry/staged counts 186/129 at collision check, eight collisions,
no adoption or renumber map; retained lists in `w1/ConnectorC/`. considerthese latest
proposal statuses are measured in `w1/ConnectorC.md`; this round records instrument
status rather than silently claiming every proposal implemented.

## Trend verdicts

- **expansion — improved, bounded:** one admitted sourced knowledge entry plus a
  demonstrated local-file repertoire, with coverage row; no complete-contract claim.
- **quality — improved locally:** sidecar freshness repair, revision-bound measurement,
  stronger oracle isolation and explicit correction of stale documentation. The
  g26 inconsistency remains visibly marked rather than left as an unqualified fact.
- **discernment — unchanged pending outside check:** lane seats drove substantive
  corrections and grounded criteria, but they are still the lane. An independent
  non-author must spot-check an admit and reject; none is invented here.

Open operator items remain in the fleet L0 ledger: keeper enable/retire, calibration
ownership and CJK quote rules, historical trust-boundary questions, host-related
questions and staged-id disposition. No new operator decision is required to retain
this honest-stop report; no historical question is silently answered.

## SHONEN

- [~] Decision tables/checklists/sources — `corpus/knowledge/shonen-ledger.json` box 1;
  measured declarations and `SKILL.md` registry. Author-side, no promotion tick.
- [ ] End-to-end task evidence gap — ledger box 2; historical missing verdict-time
  receipt remains absent, and a rerun cannot retroactively prove it.
- [~] Executable instructions within the declared scope — ledger box 3; unresolved
  historical external commands remain explicitly excluded, not claimed repaired.
- [~] No cross-domain citation bleed within the declared scope — ledger box 4;
  sixty-five knowledge Markdown files at the measured carrier; PROVINCE boundaries
  retained. Outside verification is owed.
