# shokunin (main repo) — Scorecard

Axes owned by the `protocol` lane: **fleet-meta — protocol soundness + gate
integrity** (`MISSION.md` fleet shape; `scripts/shokunin-watchdog.sh`
`LANE_AXES[protocol]="fleet-meta: protocol soundness, gate integrity"`). The
`aggregator` lane's axes (cross-lane quality, mint/dormancy calls, corpus
review) are not scored here.

Every score is a claim: it carries the command that produced it and the tree
it was measured against. Baseline measured 2026-09-28 18:21 -03:00 at main
HEAD `0a30b44`; after-measurement re-executed 18:35 on the round-10 working
tree at HEAD `6a45ff2` (this file ships in the round-10 commit, so it cannot
cite its own hash — the report does).

| Axis | Score | Evidence pointer | Last change |
|---|---|---|---|
| gate-integrity | 6 (was 2) | Closure actuator landed and executed: 11/11 report-bearing rounds now carry a `MANIFEST.json` `rounds` entry (was 2/11), 58/58 terminated lane-rounds carry a correct terminal status (was 8/58), 0 rows contradict evidence under last-wins (was 5), 0 marker reports unrecorded (was 4). Metrics M1–M6 below. Still open: prompt fidelity 1/5 items and the driver's contentless-marker completion signal — both operator-side | round 10 |
| protocol-soundness | 6 (was 4) | Round-entry semantics defined for a per-lane-counter driver, marker-vs-report boundary, SSOT precedence, main-repo lane write scope + commit identity, `SCORECARD.md` in the file contract, mint bar stated once, ledger fallback named. Metrics P1–P4 below. Cost paid: `PROTOCOL.md` grew 387 → 576 lines (`wc -l`), so the concision sub-metric worsened; compaction is the round-11 move | round 10 |

## Metrics (before → after, with counting commands)

Gate integrity:

| # | Metric | Before | After | Command |
|---|---|---|---|---|
| M1 | report-bearing rounds with a closure entry | 2 / 11 | 11 / 11 | `python3 -c` over `MANIFEST.json` `rounds` vs `ls .ufo/reports/round-*/` — see the round-10 report §Closure for the exact script |
| M2 | terminated lane-rounds with a correct recorded terminal status | 8 / 58 | 58 / 58 | last-wins over `rounds[].lanes`; 58 = 66 dispatched (`.ufo/watchdog.log` launch/steer lines) − 8 live at `closed_at` |
| M3 | `rounds[]` rows contradicting durable evidence | 5 | 0 | round-1 kagi/aggregator, round-9 kake/kumitate/aggregator, each against a log line or report path |
| M4 | marker reports satisfying the driver's completion signal, unrecorded | 4 | 0 | `.ufo/reports/round-5/aggregator.md` (254 B), `round-7/kumitate.md` (122 B), `round-8/kengaku.md` (101 B), `round-8/kotoba.md` (120 B) |
| M5 | untracked dispatch-evidence prompt files | 8 / 58 | 0 / 58 | `git ls-files -o --exclude-standard .ufo/prompts \| wc -l` |
| M6 | child-lane reports missing the `SHONEN` heading | 41 / 45 | 41 / 47 (unchanged — lane debt, routed) | `grep -rLE '^#{1,6} *SHONEN' .ufo/reports/round-*/*.md \| grep -vE 'protocol\|aggregator\|AGGREGATE' \| wc -l` |
| M7 | child-lane contract items in the fleet-2 prompt template | 1 / 5 | 1 / 5 (operator-side, unchanged) | `scripts/shokunin-watchdog.sh` `lane_prompt()` heredoc; `grep -l SHONEN .ufo/prompts/*.md` → 1 file, a file-list mention |

Protocol soundness:

| # | Metric | Before | After | Command |
|---|---|---|---|---|
| P1 | mission-required artifacts ungoverned by `PROTOCOL.md` | 4 (`SCORECARD.md`, main-repo `LOG.md`, `.ufo/prompts` durability, axis-score evidence) | 0 | `grep -c SCORECARD PROTOCOL.md` 1 → 3; file-contract row added |
| P2 | protocol-text vs repo-reality contradictions | 3 (`.ufo/state` "stay untracked" vs 16 tracked files; lane write scope vs the main-repo `SCORECARD.md`/`LOG.md` duty; fleet-completion precondition vs per-lane counters) | 0 | `git ls-files .ufo/state \| wc -l` → 16; `git ls-files .ufo/watchdog.log \| wc -l` → 1 |
| P3 | `rounds[]` rows whose lane-round is unidentifiable | 8 of 8 in the round-9 entry (fleet-keyed statuses for lanes on other counters) | 0 (`lane_rounds` required on `not-dispatched`; `ok` falsifiable by the derivable report path) | `MANIFEST.json` round-9 entry vs `.ufo/reports/round-9/` (3 files) |
| P4 | `PROTOCOL.md` length / inline round-incident references | 387 lines / 12 | 576 lines / ~30 | `wc -l PROTOCOL.md`; `grep -o 'round-[0-9][0-9.]*' PROTOCOL.md \| wc -l` |
| P5 | SSOT precedence defined (`MISSION.md` vs `PROTOCOL.md`) | no | yes | Fleet-2 conventions, precedence bullet |

## Planned

- **round 11 (protocol-soundness, lowest after this move on the concision
  sub-metric):** compact `PROTOCOL.md` 576 → ≤450 lines without dropping an
  obligation — collapse the 17 duplicated rule pairs the round-10 simplifier
  audit named, move dated incident prose into a single appendix that cites
  `.ufo/reports/round-*/protocol.md`, and resolve the remaining
  contradictions it listed (`round open indefinitely` vs `missing report
  never holds a round open`; three ledger-path statements). Before→after:
  `wc -l PROTOCOL.md`, obligation count preserved (each deleted clause mapped
  to its surviving canonical home). Also owed: the round-11 closure pass must
  resolve the 7 `in-flight` rows this round wrote plus the lane-rounds that
  terminated after `closed_at` (kake r10, kagi r9, kasegi r12 — listed in the
  round-10 report).

## Retired

- none. Neither fleet-meta axis is saturated: gate integrity still has two
  operator-side actuators outstanding (prompt template items, marker-aware
  `report_of()`), and protocol soundness has an open compaction debt created
  by this round's own additions.

## Move log

| Round | Axis | Before | After | Evidence |
|---|---|---|---|---|
| 10 | gate-integrity | 2 — 2/11 rounds closed, 8/58 lane-rounds recorded, 5 contradicted rows, 4 unrecorded markers, 8 untracked prompts | 6 — 11/11, 58/58, 0, 0, 0 | `MANIFEST.json` `rounds` (15 entries), `.ufo/reports/round-10/protocol.md` §Closure + §Dispatch digest |
| 10 | protocol-soundness (enabling) | 4 — 4 ungoverned artifacts, 3 contradictions, unidentifiable round-9 rows | 6 — 0, 0, 0; cost: +189 lines | `PROTOCOL.md` step 4 semantics, marker clause, precedence bullet, file-contract `SCORECARD.md` row |

---

## Aggregator lane — axes: cross-lane quality, mint/dormancy calls, corpus review

**Ownership.** This section is the `aggregator` lane's; §1–§Move-log above belong to the
`protocol` lane, whose header states the aggregator's axes "are not scored here". Both
main-repo lanes write this single path and respawn independently — the collision is filed
as ledger row **D-77** (`.ufo/reports/AGGREGATE.md` §11.2) with a ruling owed (per-lane
sections vs per-lane filenames). This lane appends without altering a protocol byte.

Every score carries its counting command and the commit it was measured against
(`PROTOCOL.md` file-contract row `SCORECARD.md`). **Before** column: 2026-09-28 18:02 -03
at main HEAD `0a30b44`. **After** column: 2026-09-28 22:0xZ at main HEAD `78bd39b`.

| Axis | Score (before r6) | Score (after r6) | Evidence pointer | Last change |
|---|---|---|---|---|
| corpus review | **2** | **8** | Before: canonical ledger absent (`test -f .ufo/reports/AGGREGATE.md` → false), zero durable queue rows (`grep -c routed .ufo/reports/round-2/AGGREGATE.md` → 0), last refresh §10 written at aggregator round 4 with 41 lane reports unswept, 0/6 repos holding a current-round aggregator lesson. After: ledger §11 refresh 4 at the canonical path, 79 `D-` rows, 41/41 reports swept, 6/6 verdicts, 6/6 lessons committed + pushed, 100 citations re-executed. Metrics C1–C8 | round 6 |
| cross-lane quality | **4** | **7** | Before: last fleet quality review was refresh 3 (round 4); the fleet-2 axis framework had never been audited (0/6 committed cards); five standing main-repo claims were stale or false and unflagged. After: 6/6 cards audited against the AXES contract with the gaps named, 7 protocol/integrator-owned correction rows filed, promotion inputs refreshed for all six by a non-author, contested scope re-flagged, the axis-rollout template + per-axis proxies produced and routed. Metrics Q1–Q6 | round 6 |
| mint/dormancy calls | **5** | **6** | Before: kama mint-eligible since refresh 3 with no integrator ruling in rounds 9–10; the dormancy rule had never been applied (`grep -rn dormant MANIFEST.json` → 0). After: kama re-tested and surfaced (L0 question exists at r10), four watchlist candidates assessed, one new candidate ruled below the bar, dormancy applied fleet-wide with commands (0 dormant). Metrics M1–M3 | round 6 |

### Metrics (before → after, with counting commands)

Corpus review:

| # | Metric | Before | After | Command |
|---|---|---|---|---|
| C1 | canonical ledger present | 0 | 1 | `test -f .ufo/reports/AGGREGATE.md && echo 1 \|\| echo 0` |
| C2 | durable routed-defect rows in the ledger | 0 | 79 | `grep -cE '^\| D-' .ufo/reports/AGGREGATE.md` |
| C3 | lane reports in the sweep window reconciled | 0 / 41 | 41 / 41 | `ls .ufo/reports/round-{5,6,7,8,9,10,11,12}/*.md \| wc -l` |
| C4 | committed round-6 aggregator lessons | 0 / 6 | 6 / 6 | `for d in kasegi kengaku kake kumitate kotoba kagi; do git -C $d-shokunin ls-files corpus/lessons/round-6-aggregator-audit.md \| wc -l; done` |
| C5 | per-repo corpus verdicts emitted this round | 0 | 6 (all `not conformant`) | `.ufo/reports/AGGREGATE.md` §11.1 table |
| C6 | citations re-executed against live surfaces | 0 | 100 | per-lesson `awk '/^## Re-executed citations/{f=1;next} /^## /{f=0} f' \| grep -c '^\|'` minus 2 header rows (kasegi's section is a bullet list → `grep -c '^- '`), summed |
| C7 | aggregator lane-rounds between ledger refreshes | 2 (r4 → r6, r5 filed a 254-byte marker) | 1 (this refresh) | `.ufo/state/aggregator.round`; `wc -c .ufo/reports/round-5/aggregator.md` → 254 |
| C8 | aggregator self-defects filed | 6 (§10.6, round 4) | 8 (§11.7), incl. one new hazard class: a lane commit swept this lane's staged ledger rename (`ade32e4`) | `.ufo/reports/AGGREGATE.md` §11.7 |

Cross-lane quality:

| # | Metric | Before | After | Command |
|---|---|---|---|---|
| Q1 | child repos with a committed `SCORECARD.md` | 0 / 6 | 6 / 6 (**lane work, not this lane's move** — five lanes landed cards inside this round) | `for d in …; do git -C $d-shokunin ls-files SCORECARD.md \| wc -l; done` |
| Q2 | committed cards audited against the AXES contract | 0 / 6 | 6 / 6 | lessons §Fleet-2 axis-framework state; ledger §11.8 |
| Q3 | cards carrying falsified or non-re-derivable numbers | unmeasured | 3 of 6 named (kagi D-65, kumitate D-59, kotoba D-29) | ledger §11.2 rows |
| Q4 | cards with no measured-against commit hash | unmeasured | 2 of 6 (kasegi, kake) — D-58 | `grep -coE '\b[0-9a-f]{7,40}\b' <repo>/SCORECARD.md` |
| Q5 | protocol/integrator-owned correction rows filed by this lane | 0 | 7 (D-62, D-73, D-74, D-75, D-77, D-78, D-79) | `grep -cE '^\| D-(62\|73\|74\|75\|77\|78\|79) ' .ufo/reports/AGGREGATE.md` |
| Q6 | non-author promotion inputs current for | 6 repos at refresh 3 (round 4) | 6 repos at refresh 4 (round 6) | ledger §11.4 |

Mint / dormancy:

| # | Metric | Before | After | Command |
|---|---|---|---|---|
| M1 | watchlist candidates assessed with a written ruling or bar test | 4 at refresh 3 | 5 (kama re-tested, kessho trigger restated, umihotaru/kagemusha no instance, axis-framework stewardship ruled below bar) | ledger §11.6 |
| M2 | mints executed | 0 | 0 — correct: the bar is met only by kama and the ruling is operator-side | `python3 -c "import json;print([r.get('minted') for r in json.load(open('MANIFEST.json'))['rounds']])"` → 15 × `[]` |
| M3 | repos with a dormancy assessment on record | 0 | 6 (0 dormant) | `grep -oE 'round[- ]([0-9]+)' <repo>/LOG.md \| sort -u -V \| tail -1` + `git -C <repo> log -1 --format='%ar'` |

### Planned

- **round 7 — mint/dormancy calls (lowest at 6).** Move: make the two calls *standing and
  re-runnable* instead of one-off prose — a ledger §12 assessment table with one row per
  rostered lane (dormancy: last dispatched round, last reported round, last `LOG.md` round
  token, last commit age, verdict + command) and one row per watchlist candidate (demand
  instances with pointers, owning-province test, bar verdict), re-tested every refresh.
  Falsifiable target: 6/6 lanes and 5/5 candidates carry a row whose command this lane
  re-ran in the same refresh; the operator-gated half (kama, D-40) is recorded as
  **blocked-external** with the L0 pointer rather than silently re-flagged. Before→after:
  M3 6 → 6 with commands inline, plus a new M4 "candidates with a dated bar test" 0 → 5.
- Queued behind it (highest value, needs a full round): **cross-lane quality** — the box-3
  execution walkthrough, one non-author agent per repo running `SKILL.md`/`corpus/` with no
  oral context. It is the only measurement that can convert the fleet-wide `[~]` on box 3
  into an `[x]` (ledger §11.4).

### Retired

- none. No axis is saturated and none is a wrong fit: corpus review still finds every repo
  non-conformant (6/6), cross-lane quality has 78 open queue rows, and mint/dormancy has
  never had a positive dormancy case to test the rule against. A split of
  "mint/dormancy calls" into `mint-calls` (operator-gated) and `dormancy-calls`
  (lane-measurable) is *proposed but not taken*: the round-7 move covers both halves in one
  table, and a split that only relabels rows would reduce comparability with refreshes 3–4.

### Move log

| Round | Axis | Before | After | Evidence |
|---|---|---|---|---|
| 6 | corpus review | 2 — no canonical ledger, 0 durable queue rows, 41 lane reports unswept, 0/6 current lessons, last refresh 2 lane-rounds old | 8 — canonical ledger relocated + refresh 4, 79 `D-` rows, 41/41 swept, 6/6 lessons committed and pushed, 6/6 verdicts, 100 citations re-executed | `.ufo/reports/AGGREGATE.md` §11 (this file's C1–C8); lessons `d341b48`, `1bd17ec`, `ab8c9e2`, `31f09cd`, `778310d`, `ad694a2`; report `.ufo/reports/round-6/aggregator.md` |
