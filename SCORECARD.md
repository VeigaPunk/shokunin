# shokunin (main repo) — Scorecard

Axes owned by the `protocol` lane: **fleet-meta — protocol soundness + gate
integrity** (`MISSION.md` fleet shape; `scripts/shokunin-watchdog.sh`
`LANE_AXES[protocol]="fleet-meta: protocol soundness, gate integrity"`). The
`aggregator` lane's axes (cross-lane quality, mint/dormancy calls, corpus
review) are not scored here.

Every score is a claim: it carries the command that produced it and the tree
it was measured against. Baseline measured 2026-09-28 18:21 -03:00 at main
HEAD `0a30b44`; round-10 after re-executed 18:35 at `6a45ff2`; round-11 after
measured 20:05–20:20 at HEAD `3ea42cb`→`6bd4f38` (this file ships in the
round-11 commit chain, so it cannot cite its own hash — the report does).

| Axis | Score | Evidence pointer | Last change |
|---|---|---|---|
| gate-integrity | 7 (was 6) | Closure machinery executed against the live fleet: in-flight debt 7→0 (every carried row resolved by appended `closure-correction`), 16/16 lane-rounds terminated between passes recorded with step-1 verification (hash ancestry, SHONEN heading, ordering, marker screen — 0 new markers), `rounds` 15→22 entries, last-wins 73 ok / 4 failed / 4 in-flight (all live missions at `closed_at`) / 23 not-dispatched; canonical ledger `.ufo/reports/AGGREGATE.md` committed by the aggregator (`e333e7c`, refresh 4, 79 rows) — the routing queue is durable again. Still open, operator-side: prompt fidelity 1/5 — now with a measured consequence, 4 lanes filing report-before-commit — and the `report_of()` content check. Metrics M1–M11 below | round 11 |
| protocol-soundness | 8 (was 6) | Compaction landed: `PROTOCOL.md` 583→446 lines (`wc -l`) with the obligation census 93/93 green (verifier committed at `.ufo/waves/round-11/`), SHONEN seed byte-identical, 30 duplicate clusters collapsed to canonical homes, ~125 incident/measurement lines moved into a 32-row dated appendix digest, contradictions (a) driver-vs-ledger, (b) ledger queue-of-record, (c1–c3) resolved, in-flight still-live re-confirmation rule added, operator push-scope rule carried as a `MISSION.md` pointer. Disclosed cost: body rewrapped ~78→100 cols; bytes 38649→39264 (+615: appendix pointer column + 2 new clauses). Metrics P1–P7 below | round 11 |

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
| M8 | unresolved `in-flight` rows carried across closure passes | 7 | 0 | last-wins tally over `MANIFEST.json` `rounds` (22 entries): the 4 remaining in-flight rows are live missions at `closed_at` 20:10 (protocol r11, kengaku r11, kumitate r11, kotoba r12) |
| M9 | lane-rounds terminated between passes with a recorded terminal status | 16 terminated 18:27:54–20:05:46, unrecorded | 16 / 16 | `complete` lines in the round-11 report §Dispatch digest vs `rounds[15..21]` |
| M10 | report files added under a lane identity | 1 of 62 tracked (round-10's "0 of 62" claim falsified on re-execution — kumitate `9a2e9fb` 18:37:14 predates it) | 5 of 71 self-landed (kumitate `9a2e9fb`, protocol `025b2e3`, kengaku `8ec7a56`, kagi `ade32e4`, kotoba `f9dcfd2`) + 3 durability sweeps under protocol identity (`3ea42cb`) | `for f in .ufo/reports/round-*/*.md; do git log --diff-filter=A --format='%an <%ae>' -1 -- "$f"; done \| sort \| uniq -c` |
| M11 | child-lane reports missing the `SHONEN` heading (live count) | 45 / 52 at 18:57 | 50 / 60 at 20:05 (lane debt, routed; new reports WITH heading: kengaku r9/r10, kotoba r10/r11, aggregator r6) | same grep as M6 |

Protocol soundness:

| # | Metric | Before | After | Command |
|---|---|---|---|---|
| P1 | mission-required artifacts ungoverned by `PROTOCOL.md` | 4 (`SCORECARD.md`, main-repo `LOG.md`, `.ufo/prompts` durability, axis-score evidence) | 0 | `grep -c SCORECARD PROTOCOL.md` 1 → 3; file-contract row added |
| P2 | protocol-text vs repo-reality contradictions | 3 (`.ufo/state` "stay untracked" vs 16 tracked files; lane write scope vs the main-repo `SCORECARD.md`/`LOG.md` duty; fleet-completion precondition vs per-lane counters) | 0 | `git ls-files .ufo/state \| wc -l` → 16; `git ls-files .ufo/watchdog.log \| wc -l` → 1 |
| P3 | `rounds[]` rows whose lane-round is unidentifiable | 8 of 8 in the round-9 entry (fleet-keyed statuses for lanes on other counters) | 0 (`lane_rounds` required on `not-dispatched`; `ok` falsifiable by the derivable report path) | `MANIFEST.json` round-9 entry vs `.ufo/reports/round-9/` (3 files) |
| P4 | `PROTOCOL.md` length / inline round-incident references | 583 lines / 30 (round-10 after; 387 / 12 at round 9) | 446 lines / 14 (appendix rows carry dated pointers as `rN`) | `wc -l PROTOCOL.md`; `grep -o 'round-[0-9][0-9.]*' PROTOCOL.md \| wc -l` |
| P5 | SSOT precedence defined (`MISSION.md` vs `PROTOCOL.md`) | no | yes | Fleet-2 conventions, precedence bullet |
| P6 | compaction obligation preservation | — | 93 / 93 census predicates + seed byte-diff empty + quoted anchor phrases findable single-line | `sh .ufo/waves/round-11/verify-census.sh PROTOCOL.md`; anchors per `.ufo/waves/round-11/protocol-reference-sweep.md` |
| P7 | unresolved contradictions inside `PROTOCOL.md` | 5 — (a), (b), (c1), (c2), (c3) named by the round-11 dupes audit | 0 | `.ufo/waves/round-11/protocol-dupes.md` §Contradictions vs the compacted text: both halves of (a) named; single conditional ledger statement; normative/descriptive embed split; log citations by timestamp+text; measurements dated in the appendix |

## Planned

- **round 12 (gate-integrity, lowest after this move):** (1) resolve the 4
  `in-flight` rows written at `closed_at` 20:10 (protocol r11, kengaku r11,
  kumitate r11, kotoba r12) plus lane-rounds terminating after it — including
  the kagi r11 report-durability debt if the lane did not land it, and the
  kake r13/r14 + kasegi r13/r14 band. (2) Rule the verdict-gate standard
  question kengaku r10 filed (`.ufo/l0-questions.md` line 6): one exit-code
  convention + in-repo pinned expected values across the three sibling gates
  (kagi drift-pins/transcript-scan, kotoba verify_harness_claims, kengaku
  grader) — land it in `PROTOCOL.md` or record a reasoned rejection; evidence
  `kengaku-shokunin/corpus/evidence/round10-fleet/r10-connector.md`.
  (3) Operator-side unchanged: template 5 items + marker-aware `report_of()`;
  the report-before-commit pattern (4 lanes this round) is the measured
  consequence to cite.

## Retired

- none. Neither fleet-meta axis is saturated. Protocol-soundness's compaction
  debt is cleared (round 11); what remains on both axes is operator-side
  actuators (prompt-template items, marker-aware `report_of()`, state/log
  untracking) and lane-side debt (SHONEN headings, lane-identity commits) —
  this lane can route those, not land them.

## Move log

| Round | Axis | Before | After | Evidence |
|---|---|---|---|---|
| 10 | gate-integrity | 2 — 2/11 rounds closed, 8/58 lane-rounds recorded, 5 contradicted rows, 4 unrecorded markers, 8 untracked prompts | 6 — 11/11, 58/58, 0, 0, 0 | `MANIFEST.json` `rounds` (15 entries), `.ufo/reports/round-10/protocol.md` §Closure + §Dispatch digest |
| 10 | protocol-soundness (enabling) | 4 — 4 ungoverned artifacts, 3 contradictions, unidentifiable round-9 rows | 6 — 0, 0, 0; cost: +189 lines | `PROTOCOL.md` step 4 semantics, marker clause, precedence bullet, file-contract `SCORECARD.md` row |
| 11 | gate-integrity | 6 — 7 in-flight rows unresolved, 16 terminations unrecorded, canonical ledger absent | 7 — 0 carried debt, 16/16 recorded with step-1 verification, ledger committed by the aggregator | `MANIFEST.json` `rounds[15..21]`; round-11 report §Closure record + §Dispatch digest |
| 11 | protocol-soundness | 6 — 583 lines, 30 inline incident refs, 5 contradictions, 30 dupe clusters | 8 — 446 lines, census 93/93, contradictions 0, clusters collapsed; cost disclosed: 100-col rewrap, +615 bytes | `PROTOCOL.md` at `6bd4f38`; `.ufo/waves/round-11/verify-census.sh` re-run |

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

### Round 7 (refresh 5) — mint/dormancy axis-move

Measured against main HEAD `f9dcfd2` at the refresh cutoff **2026-09-28T22:55:03Z** (this section ships in the
round-7 commit, so it cannot cite its own hash — the report does). Before-column values are the round-6 after-state.

| Axis | Score (before r7) | Score (after r7) | Evidence pointer | Last change |
|---|---|---|---|---|
| mint/dormancy calls | **6** | **8** | Before: calls were one-off prose (ledger §11.6); 0 candidates carried a dated bar test; the dormancy evidence line used a scan falsified this round as buggy (case-sensitive tokens, `sort -V` filename ranking, shared-LOG attribution — self-defect 9); the kama call risked re-flagging each refresh instead of pointing at its pending decision. After: standing ledger §12 tables — 7 lane rows (marker-graded per the protocol r10 rule) + 5 candidate rows, **12/12 rows carry the command this lane re-ran in the same refresh**; M4 0→5; kama **blocked-external** against `.ufo/l0-questions.md` line 2 (byte-identical to `e333e7c` at cutoff → unanswered; not re-flagged); kessho's D-82 re-test condition **fired** and got a dated re-test (still below bar — 5 builders all absorbed in-province; the gate-standard demand names protocol/integrator as owner → placeable). Residual gaps (why not 9–10): the dormancy rule has never been tested against a genuinely dormant lane (0/7 positive cases); the kama ruling remains external; re-runnability is demonstrated in exactly one refresh. | round 7 |

Metrics (before → after, with counting commands):

| # | Metric | Before | After | Command |
|---|---|---|---|---|
| M3 | rows with a dormancy assessment on record | 6 (prose, buggy scan, stale within the hour) | 7 / 7 (6 lanes + aggregator self-row), marker-graded, commands inline | `AGGREGATE.md` §12.1 table; re-run blocks R1–R5 (§12.5) |
| M4 | candidates with a dated bar test | 0 | 5 (kama, kessho, umihotaru, kagemusha, axis-framework-stewardship — all 2026-09-28) | `AGGREGATE.md` §12.2 bar-verdict column |
| M5 | table rows whose re-run command this lane executed in the same refresh | 0 | 12 / 12 | §12.5 blocks R0–R5 + K/S/U/G/A, re-run at the 22:55:03Z cutoff pass |
| M6 | written mint triggers fired and re-tested in-refresh | 0 | 1 (kessho/D-82: kotoba 4th builder `abef8aa`/`4dd7753`, kengaku 5th `0c51208`; re-tested, below bar) | §12.2 kessho row + §12.5-S |

### Planned

- **round 8 — cross-lane quality (queued at round 6 §Planned; the highest-value move available).** The box-3
  execution walkthrough: one **non-author** agent per repo runs `SKILL.md`/`corpus/` with no oral context; target
  6/6 repos with a named non-author box-3 verdict committed in the repo (ledger §11.4's fleet-wide `[~]` → `[x]`).
  Falsified if any cold run is executed by the repo's author lane, or if a verdict stays uncommitted.
- **Standing duty (every refresh):** re-test the ledger §12 tables — rows are cutoff-stamped claims, not facts;
  re-check axis-framework-stewardship when the protocol r11 report lands; kama stays **blocked-external** until
  `.ufo/l0-questions.md` line 2 is answered — never re-flag it as new.

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
| 7 | mint/dormancy calls | 6 — one-off prose calls, 0 dated bar tests, buggy dormancy scan, kama re-flag risk each refresh | 8 — standing §12 tables: 7 lane rows + 5 candidate rows, 12/12 same-refresh re-runs, M4 0→5, kessho trigger fired + dated re-test, kama blocked-external (L0 line 2) | `.ufo/reports/AGGREGATE.md` §12; `.ufo/reports/round-7/aggregator.md` (wave digest: 10 L2 seats, one batched call) |
