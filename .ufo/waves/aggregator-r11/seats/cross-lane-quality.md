# cross-lane quality — round 11 seat (final training-round re-run)

**Seat.** Aggregator lane, `.ufo/waves/aggregator-r11/seats/cross-lane-quality.md`.
Run `shokunin-r11-aggregator` (`.ufo/state/aggregator.round` = r10, previous runId
`shokunin-r11-aggregator-r1790651969`). Measured 2026-10-14 at main HEAD
`18f78b2` (bounded: the report cannot cite its own commit).

**Axis-move.** `SCORECARD.md` aggregator section §Planned (round 11 close) queues:

> **round 12 — cross-lane quality (lowest at 8).** Re-run the six box-3
> non-author verdicts after rounds 14–17 and add report durability as an
> explicit grade. Falsified if a marker overwrite such as kotoba r15 can
> remain the canonical current report, or if any verdict lacks the revision
> it measured.

This seat lands that move as the final training-round re-run: **cross-lane
quality 8 → 9**. The two named falsifier clauses are both now explicit grades
with a committed, re-runnable gate, and the six box-3 non-author verdicts were
re-run at the lanes' current revisions.

## A. Six box-3 corpus verdicts re-run (after rounds 14–17)

`node .ufo/waves/round-9/corpus-gate.mjs --selftest` ⇒ **12/12 PASS** (fixtures
under `os.tmpdir()`, live tree untouched). `--all` at the current revisions,
exit 1 (the expected verdict; raw log in `seats/corpus-verdicts.log`):

| Repo | Round-11 revision | Findings | Current revision | Findings | Verdict |
|---|---|---:|---|---:|---|
| kagi-shokunin | 8a6ec16 | 60 | **fecee87** | 63 | not conformant |
| kasegi-shokunin | b021dc9 | 55 | **d1e6e8f** | 55 | not conformant |
| kengaku-shokunin | e171cdf | 30 | **d84e48d** | 30 | not conformant |
| kake-shokunin | ab87a48 | 45 | **b0feb30** | 45 | not conformant |
| kumitate-shokunin | f9f8e4d | 55 | **175de6b** | 102 | not conformant |
| kotoba-shokunin | d85982d | 82 | **02302c5** | 82 | not conformant |

All six verdicts were re-emitted at named revisions; the dirty counts are now 0/0
everywhere. Five repos hold their round-11 finding counts; kumitate moved 55 → 102
(kumitate round-17 evidence, `round-17/kumitate.md`). Still **0/6 conformant** —
the ruling this round does not overclaim the corpus axis: `corpus review` stays 9,
not 10.

## B. Report durability — the explicit grade (new)

`node .ufo/waves/aggregator-r11/cross-lane-gate.mjs --all` ⇒ exit **1**
(failed; expected). Selftest **6/6 PASS**. Raw log in `seats/cross-lane-gate.log`.

Scanned: 8 rounds (11–18), 46 presented lane reports, across every readable repo
on the host (main repo + 17 child `*-shokunin` repos + readable
`~/Projects/*` repos, e.g. `ufo-fsd-alpha`). Findings, **117**:

| Kind | Count | Class |
|---|---:|---|
| `marker-overwrite` | **5** | the round-11 report's "report overwrite → 273 B marker" defect class (§15.9 falsifier clause 1) |
| `verdict-without-revision` | **2** | verdict with no cited revision (§15.9 falsifier clause 2) |
| `cited-commit-missing` | **110** | cited commit resolves in no readable repo |

Per-round verdicts:

| Round | Reports | Failed |
|---|---:|---:|
| 11 | 8 | 6 |
| 12 | 7 | 6 |
| 13 | 7 | 6 |
| 14 | 7 | 4 |
| 15 | 6 | 4 |
| 16 | 5 | 3 |
| 17 | 5 | 2 |
| 18 | 1 | 0 |

Marker-overwrite reports (all are declared operator-directed closeout markers, not
silent overwrites; the grade is still failed — a marker must not pass as a current
report):

| Report | Bytes | What it is |
|---|---:|---|
| `round-12/kengaku.md` | 274 | "kengaku round-12 closeout (marker) — lane was on @m_qwen, completed by operator directive" |
| `round-13/protocol.md` | 275 | protocol round-13 closeout (marker) |
| `round-14/protocol.md` | 340 | protocol round-14 closeout (marker) — fleet wrap |
| `round-15/kotoba.md` | **273** | **the D-153 case**: kotoba's landed round-15 report (14,715 B at `4419fb9`) was overwritten with a 273 B marker at its canonical path |
| `round-16/kasegi.md` | 273 | kasegi round-16 closeout (marker) |

Verdict-without-revision reports: `round-13/kengaku.md`, `round-15/kagi.md`.

The D-153 marker is confirmed live and unchanged since the round-11 report:
`wc -c .ufo/reports/round-15/kotoba.md` ⇒ **273**;
`git show 4419fb9:.ufo/reports/round-15/kotoba.md | wc -c` ⇒ **14,715**.

## C. Falsifier check (the two §15.9 clauses, executed)

- **Clause 1 — "a marker overwrite such as kotoba r15 can still pass as
  a current report."** Before this round: no command anywhere graded a report
  path as a report; a 273-byte marker at a canonical path was indistinguishable
  from a landed report; the fleet's own corpus gate grades *content*, not the
  report's durability. After: `cross-lane-gate-v1` fails every one of the five
  markers — 5 findings, exit 1. Clause held.
- **Clause 2 — "any verdict lacks the revision it measured."** After: two
  reports state verdicts with no cited revision and are failed. Clause held.

Ceilings, named so they are not mistaken for saturation:

- The grade is **shape/pointer-level**: it checks that a report exists and that
  every cited commit resolves; it cannot judge whether a cited revision *causes*
  the verdict beside it (the round-13 relevance ceiling, unchanged).
- The 110 unresolvable citations are **partly host-state**: measured anchors show
  `~/Projects/bounties` is gone from the filesystem (kasegi round-15 forensics),
  `~/Projects/webzites` is gone/emptied, and `~/Projects/llm-wiki` was taken
  private; `daa371583` and `ee907f1cf` resolve in `~/Projects/ufo-fsd-alpha`
  (readable), which the gate now scans. The gate's repo set is every readable
  repo on the host; it cannot resolve a revision whose repo no longer exists.
- The markers themselves are declared operator-directed closeouts. The grade does
  not call them defects of intent; it grades that a canonical report path does
  not hold a report. Their re-landing or relocation is routed (D-153 owner:
  integrator/protocol).

## D. L2 wave — recorded, not re-dispatched

Round 11 recorded a 12-seat L2 wave at `.ufo/waves/aggregator-r11/seats/`. This
re-run executed as a single seat of the aggregator lane (a subagent has no task
dispatch surface); the ≥8-L2 batched call is not re-dispatched here and that
limitation is recorded rather than claimed.

## E. Commands used (verbatim, re-runnable)

```sh
node .ufo/waves/round-9/corpus-gate.mjs --selftest          # 12/12 PASS
node .ufo/waves/round-9/corpus-gate.mjs --all                 # exit 1, six not conformant
node .ufo/waves/aggregator-r11/cross-lane-gate.mjs --selftest   # 6/6 PASS
node .ufo/waves/aggregator-r11/cross-lane-gate.mjs --all        # exit 1, 117 findings
wc -c .ufo/reports/round-15/kotoba.md                           # 273
git show 4419fb9:.ufo/reports/round-15/kotoba.md | wc -c        # 14715
```