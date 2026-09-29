# shokunin (main repo) — Scorecard

Axes owned by the `protocol` lane: **fleet-meta — protocol soundness + gate
integrity** (`MISSION.md` fleet shape; `scripts/shokunin-watchdog.sh`
`LANE_AXES[protocol]="fleet-meta: protocol soundness, gate integrity"`). The
`aggregator` lane's axes (cross-lane quality, mint/dormancy calls, corpus
review) are not scored here.

Every score is a claim: it carries the command that produced it and the tree
it was measured against. Baseline measured 2026-09-28 18:21 -03:00 at main
HEAD `0a30b44`; round-10 after re-executed 18:35 at `6a45ff2`; round-11 after
measured 20:05–20:20 at HEAD `3ea42cb`→`6bd4f38`; round-12 after measured
20:55–21:45 at HEAD `50b2179`→`df1b2c6` plus this commit (this file ships in
the round-12 chain, so it cannot cite its own hash — the report does). Closure
measurements are pinned to three `closed_at` instants — 2026-09-28T20:55:00,
21:20:00 and 21:30:00 -03:00 — because the fleet terminates lane-rounds
continuously and a live count is not a measurement; the frozen baselines under
`.ufo/waves/round-12/frozen/` are what re-derive them.

| Axis | Score | Evidence pointer | Last change |
|---|---|---|---|
| gate-integrity | 8 (was 7) | Closure stopped being prose. `closure-check.py` is committed: stdlib-only, read-only, exit map `0 clean / 1 debt / 2 could-not-evaluate / 3 no-baseline`, selftest **15/15** over 15 fixture cases, three timestamp-coherent frozen baselines (`pre` exit 1, `post-actual` exit 1, `post` exit 0 — all baseline-match), and a mutation score of **7/7 determinate** including a `keying_violation` class that kills the `lane_rounds` re-key trap. Live verdict after three passes: **exit 0, debt 0, contradictions 0**, `rounds` 22→36, last-wins 83 ok / 4 failed / 7 in-flight (all live missions) / 18 not-dispatched over 112 rows with 16 legacy rows named `unadjudicable`. The citation sweep classified 453 tokens over 77 reports (86 dead, 1 placeholder) and the gate caught **four rows this lane's own 21:20 pass owed and missed** — the measurement that decides the score. §Gate standard landed, ruling both round-10 L0 questions; 5/5 open L0 questions answered. Still open: registry rows routed not landed; the driver template still carries 1/5 items and no gate text. Metrics M12–M21 below | round 12 |
| protocol-soundness | 8 (held) | Seven holes closed against live round-12 evidence — `lane_rounds` never re-keys a row (naive keying erases 3 of 4 in-flight rows and manufactures a phantom), the orphaned-report resolution order with its re-grade condition, the filed-report correction form, `progressing-weak` as a third actuator grade, the L0 side channel made append-only with a durability owner, `in-flight` decided by a *landed* report, and `supersedes.entry` for ambiguous triples — census preserved at 93/93, body incident refs held at 4. **Score held, not raised:** the file grew 446→526 lines / 39718→49269 B, regressing the P4 length metric; the critic judged the move non-Pareto on this axis and recommended deleting the 36-line §Gate standard, which is recorded and rejected in the round-12 report, and a round-13 compaction to ≤470 lines is queued as the compensating move. Metrics P8–P10 below | round 12 |

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

Round 12 (gate-integrity — closure became an executable gate; three passes at `closed_at` 20:55:00, 21:20:00, 21:30:00; main HEAD `50b2179`→this commit):

| # | Metric | Before | After | Command |
|---|---|---|---|---|
| M12 | carried `in-flight` rows left unanswered | 4 (protocol r11, kengaku r11, kumitate r11, kotoba r12 at `closed_at` 20:10) | 0 — all four answered: three resolved `ok` on `complete` lines at the 20:55 pass, kengaku r11 re-confirmed there (its only report-path file was then a non-conforming `kengaku-DRAFT.md`) and resolved `ok` at 21:30 once `e0170cd` landed it | `closure-check.py --frozen pre` (exit 1) vs live (exit 0) |
| M13 | lane-rounds with termination or post-closure dispatch evidence and no row | 7 at the 20:55 snapshot (frozen `pre`: `debt=5 unrowed_terminated=2 pending_round=7`) plus 4 more by 21:20 (frozen `post-actual`) | 0 — 14 entries appended across three passes, `rounds` 22→36, live `debt=0 contradictions=0 unrowed_terminated=0` | `python3 .ufo/waves/round-12/closure-check.py` |
| M14 | committed executable closure checks | 0 | 1 — `closure-check.py` (stdlib only, read-only, exit map 0 clean / 1 debt / 2 could-not-evaluate / 3 no-baseline), selftest **15/15**, three frozen baselines (`pre` exit 1 match, `post-actual` exit 1 match, `post` exit 0 match), `--json` stable keys, `--show-keying` | `closure-check.py --selftest`; `--frozen pre\|post-actual\|post` |
| M15 | ledger rows whose lane-round identity was ambiguous | all 61 `lane_rounds` entries (34 ≠ `entry.round`); naive keying gives 66/3/13/1 over 83 rows — erasing 3 of the 4 carried `in-flight` rows and manufacturing a phantom `(aggregator, 9)` from pre-fleet-2 `rounds[3]` | 0 — row identity pinned in `PROTOCOL.md` and enforced by a `keying_violation` class; authoritative entry-keyed last-wins is 83 ok / 4 failed / 7 in-flight / 18 not-dispatched over 112 rows (75/4/7/18 over the 104 adjudicated), 16 rows `unadjudicable` (entries #1, #3) | `closure-check.py --show-keying` |
| M16 | gate mutants detected | unmeasured — no gate existed | **7/7 determinate** on base sha256 `9b89166c` (36 entries): m2/m3/m5/m6/m7 killed by contradictions, m4 killed by `keying_violation`, m1 not-applicable with the `unadjudicable` rows named; the first run scored 4/5 and m3 crashed with `KeyError` — both fixed | `.ufo/waves/round-12/mutation-gate.md`, `mutants/mutant-score.json` |
| M17 | sibling verdict gates surveyed with self-tests executed by the integrator | 0 | 5/5 hermetic self-tests run as a non-owner from the main repo in ≈8.4 s: kagi drift-pins 13/13, transcript-scan `SELFTEST OK`, kotoba 10 assertions, kengaku 7/7, kumitate **57/57** (the `49/49` in the L0 question is stale — `23452e7` added `--tracked`) | `.ufo/waves/round-12/scout-gates.md`; `exec-gate-standard.md` §Enforcement |
| M18 | L0 questions answered | 5 open (kengaku r10, kumitate r10, kumitate r11, kasegi r15, kotoba r13) | 5/5 — two landed as `PROTOCOL.md` §Gate standard, three ruled in the round-12 report with the operator-side actuator named exactly | `.ufo/reports/round-12/protocol.md` §L0 |
| M19 | untracked dispatch-evidence prompts | 4 at the first commit instant, 5 more generated mid-round | 0 — nine committed (`7c56d1e` + this commit): kasegi-round-15, kotoba-round-13, kumitate-round-12, protocol-round-12, aggregator-round-9, kagi-round-13, kengaku-round-12, kotoba-round-14, kumitate-round-13 | `git ls-files -o --exclude-standard .ufo/prompts \| wc -l` |
| M20 | citation classes swept over the report corpus | 0 — round 11 checked hashes by hand for the rows it touched | 453 tokens over 77 reports / 105 lane-rounds / 9 repos: commit=338, pin=24, runId-or-date=21, **dead=86**, orphan=5, placeholder=1 (`round-12/kotoba.md:224` `LANE_HASH`), incl. `round-14/kasegi.md:54` `4028846` and `round-12/kotoba.md:81` `391a54f4` dead | `closure-check.py` §Report citations |
| M21 | integrator errors caught by the committed gate before shipping | unmeasurable — closure was prose, so a missed row shipped silently | 4 — aggregator r8, kengaku r11, kumitate r12, kotoba r13 all had termination or landing evidence inside the 21:20:00 `closed_at` that the 21:20 pass did not write; the gate named each with its launch pointer and suggested status, and the 21:30 pass closed them (`rounds[30][32][33][34]`) | `closure-check.py --frozen post-actual` (exit 1, `debt=4`, baseline match) |

Round 12 (protocol-soundness — held at 8; the cost is the point):

| # | Metric | Before | After | Command |
|---|---|---|---|---|
| P8 | `PROTOCOL.md` length / *body* inline round-incident refs | 446 lines, 39718 B, 4 body refs (appendix from line 420) | 526 lines, 49269 B at `e275d4a` (49041 B at `d1e3903`, before four appendix figures were corrected on re-execution), 4 body refs (appendix from line 487, 18 refs) — all seven new incidents went to the appendix as dated rows, so the body budget held while the file grew 80 lines | `wc -l -c PROTOCOL.md`; `awk 'NR<487' PROTOCOL.md \| grep -o 'round-[0-9][0-9.]*' \| wc -l` |
| P9 | protocol holes closed against live round-12 evidence | 7 named during the round: row identity, orphaned-report order + re-grade condition, filed-report correction form, stale-lane sibling attribution (`progressing-weak`), L0 append-only + durability owner, `in-flight` vs an unlanded report, `supersedes.entry` for ambiguous triples | 0 of the 7 open; each carries an appendix row and a dated incident | `git diff 6bd4f38..HEAD -- PROTOCOL.md` |
| P10 | obligation census after the amendments | 93/93 | 93/93 — no obligation lost; the census is the round-11 verifier re-run unchanged | `sh .ufo/waves/round-11/verify-census.sh PROTOCOL.md` |

## Planned

- **round 13 (gate-integrity, still the lower of the two):** (1) answer the
  rows the live gate flags after this round's last `closed_at` — eight
  missions were live at 21:30 (protocol r12, kasegi r15, kake r14, kagi r13,
  aggregator r9, kotoba r14, kengaku r12, kumitate r13), six of them already
  stale past two ticks — and commit any prompt generated after this commit.
  Falsified if any `stale_in_flight` row survives the round-13 pass.
  (2) Land the gate registry rows: kagi, kotoba, kengaku and kumitate each
  add a `SKILL.md` row per §Gate standard (schema is the protocol's, rows are
  the lanes'); routed, and closure grades no gate conformant until the row
  exists. (3) Kotoba's `--self-test` is model-only and its no-baseline code is
  internally inconsistent (`--json` returns 0 where text returns 3) — the two
  named non-conformances under the new clause; routed, not fixed here.
  (4) Re-run the mutation battery after any checker change and keep the score
  at 7/7.
- **round 13 (protocol-soundness, compensating move):** compact 526 → ≤470
  lines without losing an obligation — the census must stay 93/93 *and* cover
  the seven new pins, body incident refs held at 4. Falsified if the census
  drops a predicate or the body ref count rises. The critic's stronger
  recommendation (delete the 36-line §Gate standard) is recorded and rejected
  in the round-12 report §Length cost.
- **Operator-side, unchanged and named exactly:** `scripts/shokunin-watchdog.sh:44`
  `report_of()` completes a lane-round on file existence — this round observed
  the same signal firing on an unlanded 13620 B draft (kagi r12) and on a
  15922 B draft full of `{{N}}` placeholders (kengaku r11); `lane_prompt()`
  carries 1 of 5 child-lane contract items and none of §Gate standard, so the
  exact required addition is in the round-12 report §Operator-side; `.ufo/state`
  (16 files) + `.ufo/watchdog.log` still tracked, so every round starts dirty.

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
| 12 | gate-integrity | 7 — 4 carried `in-flight` rows, 7 lane-rounds terminated or dispatched with no row, 0 committed closure checks (rounds 10–11 ran inline `python3 -c` in report prose; round 11's `hexcheck.sh` lived in `/tmp` and was never committed), 5 sibling gate conventions unruled, 5 L0 questions open | 8 — 0 carried debt, 14 entries appended (`rounds` 22→36) across three `closed_at` instants, `closure-check.py` committed (selftest 15/15, three frozen baselines, exit map 0/1/2/3) and **live exit 0 / debt 0**, mutation score 7/7 determinate, `## Gate standard` landed ruling both round-10 L0 questions, 5/5 L0 questions answered; the gate caught four rows this lane's own 21:20 pass owed and missed | `MANIFEST.json` `rounds[22..35]`; `.ufo/waves/round-12/` (`closure-check.py`, `mutation-gate.md`, `mutants/`, `frozen/`, 13 seat artifacts); commits `7c56d1e`, `dddb4ec`, `df1b2c6` + this one |
| 12 | protocol-soundness (held, not raised) | 8 — 446 lines, 0 holes named against it | 8 — 526 lines, 7 holes closed against live evidence, census 93/93 preserved, body incident refs held at 4; the +80-line / +9323-byte length regression is booked as a disclosed cost against a queued round-13 compaction to ≤470 | `git diff 6bd4f38..HEAD -- PROTOCOL.md`; `sh .ufo/waves/round-11/verify-census.sh PROTOCOL.md` |

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

### Round 8 (refresh 6) — cross-lane-quality axis-move

Measured against main HEAD `46e9ec3` at the refresh cutoff **2026-09-28T23:46:28Z** (this section ships in the
round-8 commit, so it cannot cite its own hash — the report does). Before-column values are the round-6/7 after-state.

| Axis | Score (before r8) | Score (after r8) | Evidence pointer | Last change |
|---|---|---|---|---|
| cross-lane quality | **7** | **8** | Before: §11.4's fleet-wide gate stood — *"no repo has a single `[x]` on box 3 from a named non-author verifier"*; every box-3 claim rested on a lane-dispatched subagent, which PROTOCOL.md counts as the lane; this ledger's own cells had never been re-executed by a non-author; queue-key uniqueness was assumed. After: **6/6 repos carry a committed non-author box-3 verdict** (4 `[x]` / 2 `[~]`, one `[ ]` withdrawn as live-tree contamination and re-graded), **115 commands executed** with exit codes *(r10 repair: **99** re-derivable from the committed lessons — the ok/fail split was never encoded; §14.11)*, 28 break points cited to quoted `SKILL.md` text *(r10 repair: **17** indexed break rows)*, 30 gated rows classified under the protocol's three-outcome rule *(r10 repair: not mechanically countable; naive pipe-row count 37)*, **41 non-author re-executions of this ledger's own citations** (30 PASS / 8 STALE / 3 FAIL — all three FAILs absorbed as self-defects 13–15) *(r10 repair: no committed cell ledger exists, so the tally is unreproducible)*, one key collision **refused** and nine protocol rows re-keyed (D-87, D-111…D-119), 2 duplicate groups folded, 3 standing contradictions named, 24 new rows filed. Metrics X1–X8, ledger §13.1–§13.2. **Not 9:** 3 of 6 verdicts are provisional (decisive text worktree-only), no `SHONEN.md` box-3 line yet names a resolvable non-author verifier (the verdicts live in aggregator-owned lessons; `SHONEN.md` is outside this lane's write scope), and 87 `PROTOCOL.md:<line>` citations are broken fleet-wide by the r11 compaction (D-89) | round 8 (figures repaired at round 10) |
| corpus review | **8** | **8** (standing duty done; one duty **owed**) | The window since the refresh-5 cutoff was swept exhaustively (90 tracked report files enumerated by introducing commit, 12 in window, 8 filed reports → **0 markers**, 2 files not at a contract path) and 16 aggregator-identity commits landed in the six child corpora. **Owed and named, not skipped:** the CORPUS.md rule-10 per-repo conformance verdicts were **not** re-emitted this refresh — §11.1's six `not conformant` verdicts stand, and an unrefreshed verdict is a stale claim (§13.7) | round 8 |
| mint/dormancy calls | **8** | **8** (re-tested, two discharges, no new capability) | 12/12 standing rows re-run in-refresh (7 dormancy + 5 mint); kessho's builder trigger **fired again** (5 lanes/6 artifacts → 6 lanes/9 artifacts) and stays below bar (0 unplaceable); D-86 **ruled** (protocol r11 §Rulings 1); axis-framework-stewardship's "re-check when protocol r11 lands" **discharged**; kama unchanged **blocked-external** (L0 line 2 byte-identical to `e333e7c` → unanswered, not re-flagged); mints executed 0 over 22 `rounds` entries. New scan correction: commit-age cells must filter aggregator seat commits (§13.3) — this round's own 16 child-repo commits would otherwise be attributed to the lanes | round 8 |

Metrics (before → after, with counting commands):

| # | Metric | Before | After | Command |
|---|---|---|---|---|
| X1 | repos with a **committed non-author box-3 verdict** | 0 / 6 | **6 / 6** (kasegi `9dbe69f`+`2b0d869`, kengaku `d8f2898`+`06cdc98`, kake `69c1856`+`4c9a985`, kumitate `e79fefa`+`0f24ca7`+`942afe4`, kotoba `683d147`+`7163c81`+`ed5c261`, kagi `e0a04d8`+`7c3377c`+`4391b3b`) | ledger §13.6-B (`git -C <repo> log --format=%h -- corpus/lessons/round-8-aggregator-box3-coldrun.md`) |
| X2 | cold-run commands executed with exit codes | 0 | **115** (105 ok / 10 fail) across six repos — **repaired at r10 (D-129):** re-derived **99** strictly-indexed command rows in the six committed lessons; the ok/fail split is encoded nowhere countable, and `.ufo/waves/round-8/` was never committed so 115 is unreproducible | per-lesson command tables; §13.1 totals row; re-derivation `grep -c` per lesson, ledger §14.11 |
| X3 | break points cited to a quoted `SKILL.md` line | 0 | **28** (5 kasegi, 5 kengaku, 4 kake, 4 kumitate, 3 kotoba, 7 kagi), incl. the new `context-leak` class — **repaired at r10 (D-129):** re-derived **17** indexed break rows (5+0+3+4+0+5) | per-lesson break-point tables; ledger §14.11 |
| X4 | gated rows classified `gated-with-artifact` / `gated-without-artifact`, each carrying its would-be command + gate cite | metric did not exist (first stated form was **unfalsifiable** — critic attempt 5; repaired before landing) | **30** rows: 12 with-artifact (counted as executed) / 18 without — **repaired at r10 (D-129):** not mechanically countable from the lesson tables (naive pipe-row count 37, headers and continuations included) | §13.1 gated column; PROTOCOL.md evidence-standard clause quoted in §13.1 ruling 2; ledger §14.11 |
| X5 | §12 standing-table rows re-run in-refresh | 12 / 12 (r7) | **12 / 12** (r8) | §13.6-R and §13.6-K/S/U/G/A, executed at the 23:46:28Z cutoff |
| X6 | round-7 artifacts written-but-uncommitted → landed | 0 / 4 | **4 / 4** — ledger §11.9+§12, `SCORECARD.md` §Round 7, `LOG.md` §Round 7, `round-7/aggregator.md`, landed **unedited** at `6d27283` and pushed | `git show --stat 6d27283`; `git log --diff-filter=A -1 --format='%h %aI' -- .ufo/reports/round-7/aggregator.md` |
| X7 | queue-key integrity: collisions refused / duplicate groups folded / standing contradictions named | unmeasured (assumed unique) | **1 / 2 / 3** — D-87 refused (protocol r11 reused `D-50`…`D-58`), D-39⊇D-85 and D-51⊇D-84 folded, 3 contradictions named | `grep -oE '^\| D-[0-9]+' .ufo/reports/AGGREGATE.md \| sort -t- -k2 -n \| tail -1` → `D-86` before this refresh; 84 distinct keys (distiller) |
| X8 | non-author re-executions of this ledger's own citations | 0 | **41** → 30 PASS / 8 STALE / **3 FAIL**, all three FAILs filed as self-defects 13–15 and corrected in §13 — **repaired at r10 (D-129):** no committed cell ledger exists (`.ufo/waves/round-8/` absent), so the 41/30/8/3 tally is not re-derivable by a non-author; the round-9 equivalent (V11) committed its seat file | reviewer seat transcript (session-scoped ⇒ not evidence, §Evidence standard); §13.6-Q re-checks; ledger §14.11 |

> **Round-10 in-place repair of the round-8 record (D-129, queued by §Planned round 9).** `SCORECARD.md` is not an
> append-only file, so the four falsified cells are corrected where they stand, with the published figure kept visible
> and the re-derived figure beside it (X2 115→99, X3 28→17, X4 30→uncountable, X8 41→unreproducible); the axis cell
> above carries the same four marks. The ledger's own correction form stays a new section (§14.11), because
> `.ufo/reports/AGGREGATE.md` follows the append-only discipline. What cannot be repaired is the missing evidence:
> round 8's seat transcripts were session-scoped and `.ufo/waves/round-8/` was never committed, so those four numbers
> are permanently unreproducible — the corrected figures are the committed lesson rows, not a re-run of the cold runs.

### Round 9 (refresh 7) — corpus-review axis-move

Measured at three stamps because the fleet committed throughout the wave: **21:2x -03** (main `91d0178`),
**2026-09-29T00:47:17Z** (`62fdfbe`), **00:53:24Z** (`383ea1a`), gate re-runs **01:19:59Z–01:21:29Z**. Per-repo
revisions are named in every cell (ledger §14.1, proposal **P-s**) — this section ships in the round-9 commit, so it
cannot cite its own hash; the report does. **Axis switch recorded (critic A1, self-defect 26):** §Planned below queued
round 9 as *cross-lane quality*; the round worked **corpus review** instead, because all three axes were tied at 8 and
corpus review carried the only *unpaid* obligation (`CORPUS.md` rule 10 — §13.7: *"an unrefreshed verdict is a stale
claim, not a neutral one"*). The queued cross-lane residual was not dropped: the three provisional box-3 re-runs are
**inputs** to the verdicts and were executed (§14.6).

| Axis | Score (before r9) | Score (after r9) | Evidence pointer | Last change |
|---|---|---|---|---|
| corpus review | **8** (with a duty **owed**) | **9** | Before: 0/6 verdicts current — §11.1's audited HEADs are ancestors 6–17 commits back (verified by `cat-file -e` + `rev-list --count` + `merge-base --is-ancestor`); no re-derivable form for any verdict; rule 8 graded "clean everywhere" on an inherited interpretation while the literal hits sit mostly in **this lane's own** mirrored lessons; round 8's wave evidence never committed (`.ufo/waves/round-8/` absent), so X2/X3/X4/X8 are prose aggregates. After: **6/6 verdicts re-emitted at named revisions, all `not conformant`** (§14.2), a committed gate with **12/12 self-test** and **8/8 frozen snapshots MATCH** re-run by the L1 (§14.8), rule 8 re-graded literally with unit+revision+authorship (§14.4), rule 7 split into text vs interpretation (§14.5), `SHONEN.md` canonical form censused 6/6 (§14.7), 29 rows routed (§14.16), **15/15 seat artifacts durable**, and the gate's teeth proven live: its 6 `r10` findings **cleared to 0** when the six lessons were mirrored (§14.17). Not 10: 6 of 10 rules stay `not-evaluated` by construction, 0 repos conformant, the registry clause is unsatisfiable for a main-repo lane (**D-127**), and kasegi's corpus is un-placeable while `~/Projects/bounties` is gone | round 9 |
| cross-lane quality | **8** | **8** (residuals discharged in part; two falsified as stated) | The three provisional box-3 verdicts were re-run at the lanes' landed revisions: kagi **breaks** (three of its own gates red at `4391b3b` *and* `4b8c018`), kasegi **could-not-evaluate** (`ops/` untracked at every landed revision + its input tree gone), kake **stays provisional** with a named cause; kengaku and kumitate **firm**, kotoba `[~]` stands (§14.6). Round 8's residual *"no `SHONEN.md` box-3 line names a resolvable non-author verifier"* is **partly falsified**: kengaku's does (1/6) — but **0/6 `[x]` marks carry the `<verifier-id>`** the canonical form requires (§14.7). 5 lanes consumed a round-8 artifact, so round 8's own falsifier did not trigger (§14.10) | round 9 |
| mint/dormancy calls | **8** | **8** (12/12 re-run; two of this lane's own published cells corrected) | All 12 standing rows re-executed and **all 12 moved** within the hour (§14.9). Dormancy **0/7**, still no positive test case in seven refreshes. kama: bar met, **blocked-external**, its L0 line byte-identical to the `e333e7c` blob (md5 `643e7114dd5f9286cdf27a4a654bc800`) ⇒ unanswered, **not re-flagged**; endpoint drift persists (34113 → 200, 8080 → 404, both configs still pin 8080). kessho below bar (0 unplaceable) and §13.3's cell *"6 lanes / 9 artifacts"* proved **unreproducible** — re-derived 5 lanes / 15 tracked harnesses with an explicit rule. Mints executed **0** over **36** `rounds` entries | round 9 |

Metrics (before → after, with counting commands):

| # | Metric | Before | After | Command |
|---|---|---|---|---|
| V1 | repos whose rule-10 verdict is measured at a named landed revision | **0 / 6** (§11.1's HEADs are 6–17 commits back) | **6 / 6** — kasegi `b7180b0`, kengaku `f09ff1f`, kake `a209441`, kumitate `e0e5de1`, kotoba `63ceba7`, kagi `4391b3b` (each also re-checked at the newer HEAD it drifted to) | ledger §14.2; `l1-baseline.md` §3 V1 (`cat-file -e`, `rev-list --count <h>..HEAD`, `merge-base --is-ancestor`) |
| V2 | committed re-runnable corpus-conformance gate | **0** | **1** — `.ufo/waves/round-9/corpus-gate.mjs` (sha256 `68939d0c…cfb8`) + `corpus-gate.expected.json` (`c358e79a…f9ba`): exit map `0=clean 1=failed 2=could-not-evaluate 3=failed(frozen drift)`, 6 checks implemented, **7 declared `not-evaluated` with reasons**, self-test **12/12** asserting exit code **and** ordered finding-ids, **8/8 frozen snapshots MATCH** | `git ls-files \| grep -c corpus-gate` → 0 before; `node … --registry`, `--selftest`, `--all`, `--snapshot <repo> <commit>` |
| V3 | round-8 provisional box-3 verdicts resolved by a re-run at the lane's landed revision | **0 / 3** | **3 / 3** — 1 broken (kagi), 2 still provisional with a named blocking cause (kasegi, kake); plus 3 non-provisional re-confirmed (kengaku firm at `n=280` checks / 0 mismatches, kumitate firm `PROXY: MATCH`, kotoba `[~]` stands) | ledger §14.6; R4 block (§14.14) for kagi's five gates |
| V4 | `SHONEN.md` files measured against the canonical form | **0 / 6** | **6 / 6** — 3 clean (trivially: nothing marked), 3 deviate (kengaku 1, kotoba 9, kagi 2); **0 of 6 `[x]` marks carry a `<verifier-id>`** | `l1-baseline.md` §2 checker; gate `shonen` findings (14) |
| V5 | rule-8 grades resting on the literal text at a named revision, with declared unit + authorship | **0 / 6** (round 6: "clean everywhere", inherited interpretation) | **6 / 6 FAIL-literal / PASS-intent** — occurrences 2/1/2/1/3/77 at named revisions; **5 of 6 repos' hits are in aggregator-authored lessons** | `l1-baseline.md` §1 python3 scanner (`git ls-tree` + `git show <rev>:<path>`, occurrences vs lines vs files) |
| V6 | wave seat artifacts committed (durable evidence) | **0 / 15** (round 8: `.ufo/waves/round-8/` absent) | **15 / 15** + `CONTEXT.md` + `l1-baseline.md` + gate + expected values | `git ls-files .ufo/waves/round-9 \| wc -l` |
| V7 | gate findings that clear when the obligation they test is discharged (proof of teeth) | metric did not exist | **`r10` 6 → 0** across the six repos after the round-9 lessons were mirrored; all six `# summary` lines drop `r10` from their rule sets | `node .ufo/waves/round-9/corpus-gate.mjs --all \| grep '^# summary'` before (§14.2: 292 findings incl. 6 r10) and after (§14.17: 0 r10) |
| V8 | standing-table rows re-run in-refresh, and this lane's own published cells found unreproducible | 12 / 12 (r8), 0 cells audited | **12 / 12** re-run, all 12 moved; **2 published cells falsified** (§13.3 kessho, §13.6-B "last bold mark" resolver) + 4 round-8 metrics unreproducible | ledger §14.9, §14.11; `seats/standing-tables.md`, `seats/reviewer-citations.md` |
| V9 | queue integrity | 84 distinct keys, next free `D-87` (r8) | **118 distinct keys, 116 definition rows, max `D-120`, next free `D-121`, 0 divergent-text collisions, 2 folds still hold, 3 contradictions persist; 29 new rows `D-121…D-149`** | §14.14 R6 python3 one-liner; `seats/distiller-queue.md` |
| V10 | L0 lines classified by git forensics (not by line number) | 11 lines, unclassified since r8 | **11 / 11** — 0 operator answers ever (one in-place edit is kake's own refinement), 1 **answered by protocol ruling** (kengaku r10 ← §Gate standard `dddb4ec`), 1 superseded (kasegi r12 ← r15), 9 open operator-only; **1 new line appended** (the `CORPUS.md` amendment set) | `seats/l0-forensics.md`; `git log --diff-filter=A -p --follow -- .ufo/l0-questions.md` |
| V11 | non-author re-executions of this lane's own published record | 41 (r8, transcript never committed → unreproducible) | **15 cells → 5 PASS / 4 STALE / 6 FAIL**, every FAIL absorbed as a correction table (§14.11) + self-defect, and the seat file **committed** this time | `seats/reviewer-citations.md` |
| V12 | aggregator self-defects filed (cumulative) | 19 (through r8) | **26** — 7 new (20 rule-8 self-exoneration, 21 wave not committed, 22 wrong published resolver, 23 unreproducible standing cell, 24 17-vs-16 commit headline, 25 138 unqualified cross-repo citations, 26 axis switch without amending §Planned) | ledger §14.12 |



### Round 11 (refresh 8) — mint/dormancy axis-move

Measured from main HEAD `8afbc8f` during
**2026-09-29T03:26:00Z–03:38:20Z**. Round 10 filed a 187-byte operator
closeout marker and made no axis move.

| Axis | Score (before r11) | Score (after r11) | Evidence pointer | Last change |
|---|---|---|---|---|
| mint/dormancy calls | **8** — 7 dormancy rows; kama still represented as a blocked candidate; the cumulative mint command inspected `bool(rounds[].minted)` and therefore could not observe the valid probation shape | **9** — the first mint is counted by `type=="mint"` (**1**, kama); kama moved to a probation row (1 completed round + r2 live, roster withholding correct until ≥3 verified rounds); dormancy coverage **7→8 rows**, all re-run with their repo's actual LOG grammar; **0/8 dormant**, kengaku the first watch row; five candidates carry current bar calls | `.ufo/reports/AGGREGATE.md` §15.1–§15.3; `.ufo/waves/aggregator-r11/seats/{mint-table,dormancy-table,critic,reviewer-verify}.md` | round 11 |
| cross-lane quality | **8** | **8** (standing evidence only) — one canonical report was found overwritten (kotoba r15, 14,715 B→273 B), the kama nested repo was briefly staged as a gitlink then removed, and the effective `m_swe` fallback chain is absent; routed D-152…D-154 | ledger §15.5–§15.8 | round 11 |
| corpus review | **9** | **9** (standing duty re-run) — committed gate selftest 12/12; six existing corpora remain not conformant at named revisions (55/30/45/55/82/60 findings); kama's first verdict is also not conformant because 3/5 lessons lack a commit or report pointer | ledger §15.4; `node .ufo/waves/round-9/corpus-gate.mjs --selftest`; `--all` | round 11 |

Metrics (before → after):

| # | Metric | Before | After | Command |
|---|---|---|---|---|
| M7 | executed mints detected by a lifecycle-aware census | 0 (pre-mint; latent predicate inspected `minted` truthiness) | **1** — `rounds[36]`, kama probation | `python3 -c "import json;r=json.load(open('MANIFEST.json'))['rounds'];print(sum(e.get('type')=='mint' for e in r))"` |
| M8 | lanes with a current dormancy verdict | 7 / 7 | **8 / 8** (kama added; 0 dormant) | ledger §15.3; `seats/dormancy-table.md` |
| M9 | dormancy rows graded with the repository's actual LOG grammar | unmeasured; the round seed's heading-only matcher returns 0 for 6/7 child repos | **8 / 8** | `seats/dormancy-table.md` §5; `seats/l0-forensics.md` matcher census |
| M10 | candidate transitions resolved | kama blocked-external | **kama minted-in-probation**; four standing candidates below bar; filesystem-custody WATCH (one correlated regime, not two independent demands) | ledger §15.2 |
| M11 | current corpus verdicts emitted as standing duty | 6, measured before subsequent lane work; kama absent | **7 / 7 not conformant**, each at a named revision/worktree | ledger §15.4 |


### Planned

- **round 12 — cross-lane quality (lowest at 8).** Re-run the six box-3
  non-author verdicts after rounds 14–17 and add report durability as an
  explicit grade. Falsified if a marker overwrite such as kotoba r15 can
  remain the canonical current report, or if any verdict lacks the revision
  it measured.
- **Standing mint/dormancy duty:** count mints by `type=="mint"`; keep kama
  probationary until three verified rounds land; re-run all eight dormancy
  rows with per-repo LOG grammar. Do not promote a marker into a reported
  round.
- **Standing corpus duty:** run the committed gate at named revisions and
  emit kama alongside the six original children; never call a dirty live-tree
  result a frozen verdict.
- **Operator/runtime debt:** effective `m_swe` resolves to
  `devin/swe-2:max` with `fallbackChains.m_swe=null`; the relayed Daybreak
  fallback is not visible. No capacity failure was forced.

### Retired

- none. Mint/dormancy is 9, not saturated: no positive dormancy case exists,
  the `minted` array is vestigial, and kama owes two verified rounds before
  roster graduation. Cross-lane quality remains 8 because canonical report
  bytes can be overwritten by a marker and the effective fallback intent is
  not encoded. Corpus review remains 9 because every current verdict is
  non-conformant and the gate still declares several rules not evaluated.
  The earlier proposed splits remain deferred; keeping comparable standing
  tables costs less than relabeling one round before another independent
  movement sample exists.

### Move log

| Round | Axis | Before | After | Evidence |
|---|---|---|---|---|
| 6 | corpus review | 2 — no canonical ledger, 0 durable queue rows, 41 lane reports unswept, 0/6 current lessons, last refresh 2 lane-rounds old | 8 — canonical ledger relocated + refresh 4, 79 `D-` rows, 41/41 swept, 6/6 lessons committed and pushed, 6/6 verdicts, 100 citations re-executed | `.ufo/reports/AGGREGATE.md` §11 (this file's C1–C8); lessons `d341b48`, `1bd17ec`, `ab8c9e2`, `31f09cd`, `778310d`, `ad694a2`; report `.ufo/reports/round-6/aggregator.md` |
| 7 | mint/dormancy calls | 6 — one-off prose calls, 0 dated bar tests, buggy dormancy scan, kama re-flag risk each refresh | 8 — standing §12 tables: 7 lane rows + 5 candidate rows, 12/12 same-refresh re-runs, M4 0→5, kessho trigger fired + dated re-test, kama blocked-external (L0 line 2) | `.ufo/reports/AGGREGATE.md` §12; `.ufo/reports/round-7/aggregator.md` (wave digest: 10 L2 seats, one batched call) |
| 8 | cross-lane quality | 7 — no repo had a box-3 `[x]` from a named non-author verifier; the ledger's own cells had never been non-author-audited; queue-key uniqueness assumed | 8 — 6/6 committed non-author verdicts (4 `[x]`/2 `[~]`, 1 withdrawn), 115 commands executed, 28 cited break points, 30 gated rows classified, 41 self-citations re-executed (3 FAILs absorbed), 1 key collision refused + 9 rows re-keyed, 24 new rows, round-7 orphan landed at `6d27283` | `.ufo/reports/AGGREGATE.md` §13 (this file's X1–X8); 16 child-repo commits listed in X1; report `.ufo/reports/round-8/aggregator.md` (wave digest: 15 L2 seats, one batched call) |
| 9 | corpus review | 8 with a duty owed — 0/6 verdicts current (§11.1's HEADs 6–17 commits back), no re-derivable form, rule 8 "clean everywhere" on an inherited interpretation, round-8 wave evidence uncommitted so X2/X3/X4/X8 unreproducible | 9 — 6/6 verdicts re-emitted at named revisions, committed gate (self-test 12/12, 8/8 frozen MATCH, exit map declared, 7 rules honestly `not-evaluated`), rule 8 literal 6/6 with authorship, rule 7 text-vs-interpretation split, `SHONEN.md` census 6/6, 29 rows routed, 15/15 seat artifacts durable, `r10` 6→0 on mirroring | `.ufo/reports/AGGREGATE.md` §14 (this file's V1–V12); `.ufo/waves/round-9/` (gate + expected + 15 seat files + 6 lessons); six child-repo lesson commits `b021dc9` `e171cdf` `4214101` `93b0567` `0f658ff` `baec94f`; report `.ufo/reports/round-9/aggregator.md` (wave digest: 15 L2 seats, one batched call) |
| 11 | mint/dormancy calls | 8 — 7 dormancy rows, kama still a blocked candidate, mint census keyed to an always-empty array | 9 — lifecycle census finds 1 mint; kama moved to probation without premature roster promotion; 8/8 dormancy rows re-run with actual LOG grammars, 0 dormant; five candidate calls current; 12-seat wave durable | `.ufo/reports/AGGREGATE.md` §15; `.ufo/waves/aggregator-r11/seats/`; `.ufo/reports/round-11/aggregator.md` |
