# kumitate — round 85 report

**Stale-lane:** respawn-per-round driver; no other mission of this lane is open.

**Declared claim (1): C1 — operability, capability acquisition `counter-receipt` v2**, on the
lowest non-retired axis (integer-terminal at 9 under `f_O`; the surface move is a discriminating
receipt check, not a scalar increment). The frontier step and the routed repairs ride this claim
cap; there is no second claim and no exploratory claim. **Verdict: UNMET — rejected honest stop**
(the frozen predicate reads green at M; the frozen kill rule fires on controls built after the
freeze; both facts are recorded below and neither is narrowed).

## Work performed

- **Frozen before any seat data** at `9db0c6b5`: `plan.md`, the 20-arm probe
  (`.ufo/waves/round-85/probe/probe85-c1.mjs`), three control tools and a same-path
  content-variation control under `.ufo/waves/round-85/controls/`, all committed with their
  receipts. Motive: round 84's acquisition stopped when a label-keyed no-reader reached
  `held=16/16` without opening a receipt (`corpus/lessons/round-84.md` `## Mistakes` row `vacuous`;
  round-84 non-author spot-check §2 C1).
- **Repair-before-freeze** `6663b3be` adopted the round-84 non-author spot-check's missing README
  map row (C2 213/214 → 214/214, `PROXY: MATCH`). Its map-**pin** half was missed, so
  `readme-map` read `covered=213 bad=1` and `plan-before-ready --round 85` read
  `FAIL reason=MAP_DRIFT` at the archived plan; the pin was repaired in the work commit and both
  gates read CLEAN afterwards (`close/map-repair.txt`). Mistake row 1.
- **The instrument**: `scripts/counter-receipt.mjs` v2, integrated from seat `K85ExecGate`'s
  candidate (`7659be6e…`) with the sentinel's S5 numeric-boundary fix; final sha256
  `f385bd7a9fbf1dc49d465c8d83fecfd07aae34f6bf619aca7d935eda14f238cd`. A derived
  `RECEIPT: bytes=… rows=… held=… findings=… sha256=…` line on every non-USAGE run, and a `--src`
  binding of the receipt's arm names, row count and declared `ARMS = <int>` to the counter source
  (`ARM_UNBOUND`, `SOURCE_ARITY`, `SOURCE_DECLARED`, fail-closed `SOURCE_UNREADABLE`,
  `SOURCE_ARMS_EMPTY`).
- **Wave**: ONE v1 wave of **13 seats, 13 settled, 0 dead** (`w1-results.json`), L1 holding the
  canonical planner seat (the prompt-sanctioned deviation; the fleet-wide question is open in
  `.ufo/l0-questions.md` from kake/kotodama). `w1-dispatch.json`: 13 spawn / 0 resume, gated
  `READY_HANDOFF: READY wave=w1 seats=13 resumes=0 total=13 attack=4/13 connector=1`. Roles:
  executor 5, scribe 1, scout 1, connector 1, reviewer 2, critic 1, mutation-tester 1, sentinel 1;
  no residual call. WAVE-DONE received before filing; seat reports in `.ufo/waves/round-85/w1/`,
  artifacts in `build/`.
- **Corpus**: `corpus/knowledge/counter-receipt-discrimination.md` (S245),
  `corpus/lessons/round-85.md` (method, Gate, four mistake rows), `corpus/QUALITY.md` **Q78**
  (pre-data control classes, grounded in the round-84 `vacuous` row), `corpus/SOURCES.md` S245
  admit / S246 reject, README rows, both map-pin halves, a source capture for S245 and a reasoned
  exemption for S246.
- **Skill**: `SKILL.md` gate row rewritten to `kumitate-counter-receipt-v2` plus one new executable
  checklist item (the frozen probe); the round-84 checklist item now cites the v2 note too
  (C 44 → 45).
- **Routed repairs from the round-84 spot-check**: R-planner (L1-held planner disclosed), R-timing
  (only this round's own work commits carry `round-85:`; report/tip order recorded), R-proxy
  (A-exclusion pre-registered for round 86, not re-baselined silently), R-cite (the three new dead
  citations are inside the non-author spot-check file this lane may not edit — L0 question filed;
  the lane's own files add none), R-checklist (`CHECKLIST: 41/45 pass`, `VERDICT: FAIL`, disclosed
  with its receipt).
- **Misroot sweep**: `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows only
  `.scratch/*` (orchestrator-owned), `.ufo/reports/round-84/kama.md`, `.ufo/tmp-census-r79.txt` and
  a dated `after` file from 2026-11-03 — none written by this round's seats. No misroot.
- **Tool installs**: none this round (no seat reported an install; nothing was needed).

## Landed changes

| change | LOG.md | commit |
|---|---|---|
| README map row + C2 pins for the r84 spot-check | `## Round 85 — the receipt check that must read` | `6663b3be` |
| frozen plan, 20-arm probe, three controls, same-path control | same entry | `9db0c6b5` |
| `scripts/counter-receipt.mjs` v2, `pin.counter-receipt`, SKILL row + checklist item | same entry | `a882a334` |
| knowledge note, lesson, Q78, S245/S246, README rows, map pins, capture/exemption | same entry | `a882a334` |
| SCORECARD stanza A/C/C2, capability row (marked unverified), move-log row, disposition, round-86 candidates | same entry | `a882a334` |
| C1 UNMET verdict + r84 checklist item cites the v2 note | same entry | `6e3e4749` |
| close receipts, 13 seat reports, scribe drafts, `w1-results.json` | same entry | `2688cc7f`, `de61175a` |
| `## Planned` pointer to the round-86 pre-registration | same entry | `602f1835` |
| this report | — | fleet `fleet-commit.sh --as kumitate` |

Lane tip at filing: `602f1835a46b6627ed9f0c0e139279f4b6212444`; `ls-remote origin
refs/heads/master` prints the same hash.

## Before → after measurements

Counting command, identical before and after, run from the lane root:

```
node .ufo/waves/round-85/probe/probe85-c1.mjs --lane <DIR> --work /fast/scratch/hyaku/kumitate-r85/L1/probe
```

| state | target | result | receipt |
|---|---|---|---|
| before | the v1 tool bytes (`controls/base/`, sha256 `190a4c1f…` = the round-84 pin) | `C85_C1: UNMET held=1/20`, exit 1 | `controls/base.txt` (committed before data) |
| control | constant-CLEAN printer | `UNMET held=0/20`, exit 1 | `controls/stub.txt` |
| control | label-keyed no-reader | `UNMET held=1/20`, exit 1 | `controls/noreader.txt` |
| after (M = `a882a334`) | integrated v2 | `C85_C1: HELD held=20/20`, exit 0 | `close/c1-probe.txt` |

Same-path content variation (`node .ufo/waves/round-85/controls/content-variation.mjs --lane <DIR>
--work DIR`): base `0/3`, stub `0/3`, no-reader `0/3`; integrated
`HELD held=3/3 distinct_sha=true` (`controls/cv-*.txt`, `close/content-variation.txt`). Selftest
`COUNTER_RECEIPT_SELFTEST: PASS held=60/60` (`close/selftest.txt`). Real task over committed bytes:
r83 `close/c1-probe.txt` → `DRIFT ARMS_TOTAL`; r83 `close/c1-repair.txt` (28/28, CLEAN under v1) →
`DRIFT SOURCE_DECLARED` with `SOURCE: sites=28 declared=27 receipt=28`; historical battery
`HISTORY: HELD held=28/28` (`close/history-v2.txt`); independent seat driver `HELD held=41/41`
(`build/K85ExecFixture/independent-candidate.txt`); mutant battery 11/11 mandated mutants killed
with three disclosed survivors (`build/K85Mutation/table.md`).

**Kill rule as declared:** "Any arm red, any control reaching 20/20, or a regression attributable
to this change means unmet/harmed, disclosed, never narrowed." Three attack seats independently
built controls that reach 20/20: a basename-keyed reader that reads the file only for
`bytes=`/`sha256=` (`build/K85Review/…`), a nonce-only replayer
(`build/K85Cheat/receipts/probe-c.txt`), and a content-keyed stateless map that also passes the
same-path control (`build/K85Critic/…/content-keyed/`). The critic cites the round-84 precedent
("no repair credit: keep C1 UNMET") and recommends the same. **The rule fires; C1 is UNMET.** The
instrument lands as code and history, not as admitted capability; the SCORECARD capability row is
marked unverified.

No axis harmed on the gate matrix: `HARM_MATRIX: CLEAN gates=36 held=30 repaired=1 carried=3
moved=2 new=0 gone=0 harm=0 harm_absent=0 new_red=0 unmeasured=1`, exit 0
(`close/harm-matrix.txt`). `PROXY: MATCH --strict` (A=972, C=45, C2=216/216; operability 9,
coverage 10, script/runtime/kimi/omp 10 each).

## Sources & frontier

- Census before: `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kumitate`
  → `kumitate ok …/corpus/SOURCES.md`, **exit 0** (six pre-existing W04 duplicate-URL warnings).
- Census after: same command → **exit 0**, same six warnings.
- Rows **182 → 184** (`grep -cE '^\| S[0-9]{3,} '`); by tier **A 155 → 157**, B 17, C 10; status
  **mined 146 → 147**, **rejected 23 → 24**, queued 13 (`SOURCES_CHECK: CLEAN (rows=184 …
  entries_with_source=40 legacy=38)`, `close/source-counts.txt`).
- Rows added: **S245** (mined, tier A — *Oracle-based Test Adequacy Metrics: A Survey*,
  arXiv:2212.06118v3 abstract opened 2026-11-04; capture 43275 B, sha256 `838d0715…`, located quote
  "it does not provide any insights into the quality or quantity of test oracles") and **S246**
  (rejected, tier A — ACM DL `10.1109/TSE.2014.2372785`, HTTP 403 on 2026-11-04 with no located
  text; flip condition and capture exemption recorded).
- Rows touched old→new: none — existing `status`/`recheck`/`used-by` cells unchanged.
- Frontier rows advanced: S245 is the sourced row C1 rests on this round; S246 is the in-round
  reject the Gate records. **Assimilation: none** (no staged package row appended; the
  `considerthese/` proposals are already Q75/Q76/Q68/Q69/Q72 or non-author formatting).
- Mistake mined: four `## Mistakes` rows (map-pin half; transport-vs-transcript; non-decimal `ARMS`
  declaration; survivor arms), each with fix and fail boundary; the map-pin class is shown able to
  fail by `--check` before/after (`close/map-repair.txt`).

## Trend verdicts

- **expansion — unchanged.** No repertoire row is admitted: the `counter-receipt` row is marked
  unverified and the claim stopped. The frontier moved into the instrument, not into the verified
  repertoire.
- **quality — improved.** The instrument now answers from the bytes it read and from the producer
  source, and it catches a real defect v1 cannot see (r83's `ARMS = 27` against 28 call sites reads
  `DRIFT SOURCE_DECLARED` on a v1-clean receipt). Offsets disclosed: A 908 → 972 (59
  wave-scaffolding files; R-proxy pre-registered), `CHECKLIST: 41/45 pass` with four live-host reds,
  three surviving mutant arms, three reachable adversary classes.
- **discernment — improved.** The round found and fixed its own freeze-order mistake, rejected a
  source with a reason and a flip, and — instead of narrowing its own kill rule after data —
  published the adversary that beats its predicate, kept the strict reading, and pre-registered the
  randomized-fixture fix for round 86 (`SCORECARD.md` `## Round 85 — pre-registration` items 5–7).

## SHONEN

`grep -c '^## SHONEN'` → 1; one line per box of `SHONEN.md`:

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — evidence:
  `SKILL.md` `counter-receipt` gate row (v2 contract, finding precedence, limits pointer) and 45
  executable checklist items; `CHECKLIST: 41/45 pass` (`close/checklists.txt`).
- [~] At least one end-to-end domain task executed and logged in LOG.md — evidence: the round-85
  LOG entry's real task (v2 over the committed r83 receipts, `close/history-v2.txt`) and the 13
  seat reports.
- [~] Instructions executable by an agent without oral context — evidence: every checklist item
  names a command, an accepted exit set and a verdict substring; the frozen probe runs from
  `SKILL.md`.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — evidence: `PROVINCE.md` unchanged this
  round; the connector's cross-lane scan (`w1/K85Connector.md`) finds the same control-class bar in
  nine sibling lanes and absorbs none of it.
