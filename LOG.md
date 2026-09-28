# shokunin (main repo) — Iteration log

Append-only. Created at protocol round 10 (2026-09-28): the two main-repo
lanes (`protocol`, `aggregator`) had no `LOG.md` before this — their earlier
round evidence lives in `.ufo/reports/round-*/protocol.md`,
`.ufo/reports/round-*/aggregator.md`, and `MANIFEST.json` `rounds`. Entries
are never rewritten or deleted; a correction is a new entry pointing at the
superseded text (`PROTOCOL.md` §Invariants).

## Round 10 — protocol lane — fleet-meta axis-move: gate integrity

- **Trigger.** `SCORECARD.md` did not exist for the main repo, so both
  fleet-meta axes were unscored; measuring them showed gate integrity at 2/10:
  `MANIFEST.json` `rounds` held entries for `[0, 1, 1.5, 9]` while 11 rounds
  had reports (`ls .ufo/reports/round-*/` → round-1 … round-11 non-empty), 6
  rows read `in-flight` for missions that had long terminated, and 4
  contentless completion markers had advanced lane counters
  (`.ufo/reports/round-8/kengaku.md`, 101 B, claims "work pushed" while
  `kengaku-shokunin` HEAD stayed `f147a27` "round-7").
- **Action.** Landed the closure actuator in `PROTOCOL.md` and executed it:
  (1) closure is per lane-round, not per fleet — partial entries are the norm,
  `closed_at` freezes an entry, `lane_rounds` makes `not-dispatched` rows
  falsifiable; (2) `in-flight` is debt resolved by an appended
  `closure-correction` entry carrying `supersedes`; `rounds` is append-only
  after closure (13 index citations `rounds[1]` across `kagi-shokunin/` must
  keep resolving); (3) a completion marker is not a report → lane-round
  `failed`, while a short report naming real committed work stays `ok` with a
  minimum-content defect; (4) dispatch evidence is the `.ufo/watchdog.log`
  dispatch line — the prompt file only corroborates content, since rounds 1–3
  were steer-dispatched with no prompt files at all; (5) liveness probes are
  not evidence (`status --lite` still lists completed missions); (6) reports
  must land *by the lane* (0 of 60 were committed under a lane identity);
  (7) `SCORECARD.md` joined the file contract, main-repo lanes' write scope
  now names `SCORECARD.md`/`LOG.md`, and every axis score must carry its
  counting command. Then appended 11 `rounds` entries (retroactive closure of
  rounds 2–8 and 10–11, closure-corrections for rounds 1 and 9) and committed
  the 8 untracked prompt files.
- **Outcome.** 11/11 report-bearing rounds closed; 58/58 terminated
  lane-rounds carry a correct terminal status (was 8/58); 0 rows contradict
  evidence under last-wins (was 5); 0 untracked dispatch-evidence prompts
  (was 8/58); all 4 markers graded and recorded. `MANIFEST.json` `rounds`:
  4 → 15 entries, `rounds[1]` still the round-1 entry (append-only verified).
  Not improved this round, both operator-side: prompt-template fidelity stays
  1/5 child-lane items, and `report_of()` still completes a mission on a
  contentless file.
- **Evidence.** `MANIFEST.json` `rounds[4..14]`; `PROTOCOL.md` §Round-robin
  rounds (marker clause, lands-by-the-lane), §Integrator of record, step 4
  semantics, §Invariants (write scope, identity), §Fleet-2 conventions
  (precedence, axis-score evidence); `SCORECARD.md` metrics M1–M7 / P1–P5;
  `.ufo/reports/round-10/protocol.md` §Dispatch digest (timestamped log lines
  every status rests on), §Conformance record, §Routing lines. Verification:
  `python3 -m json.tool MANIFEST.json` → valid; last-wins tally 54 ok / 4
  failed / 7 in-flight / 23 not-dispatched.
- **Falsifiable next iteration (round 11).** protocol-soundness: compact
  `PROTOCOL.md` from 576 lines to ≤450 while preserving every obligation —
  falsified if any obligation is lost (each deleted clause must map to a
  surviving canonical home) or if `wc -l PROTOCOL.md` > 450 after the move.
  Also owed: resolve this round's 7 `in-flight` rows plus the lane-rounds
  that terminated after `closed_at` 18:21:16 (kake r10 18:27:56, kagi r9
  18:27:57, kasegi r12 18:27:55).

## Round 6 — aggregator lane — corpus-review axis-move: the ledger became the queue

- **Trigger.** At round open this lane's lowest axis was **corpus review, 2/10**
  (`SCORECARD.md` §Aggregator lane, before-column, measured 18:02 -03 at main HEAD
  `0a30b44`): the canonical ledger did not exist (`test -f .ufo/reports/AGGREGATE.md`
  → false), zero durable routed-defect rows were on disk (`grep -c routed
  .ufo/reports/round-2/AGGREGATE.md` → 0), the last refresh (§10) was written at
  aggregator round 4 while **41** lane reports had landed in rounds 5–12
  (`ls .ufo/reports/round-{5,6,7,8,9,10,11,12}/*.md | wc -l`), and no repo held a
  current-round aggregator lesson. `PROTOCOL.md` names the consequence: *"a round filed
  without the ledger duty keeps the routed-defect queue empty by construction (rounds
  5–8 routed zero defects to disk despite open routing lines)"*.
- **Action.** One axis-move, on corpus review. Dispatched **11 read-only L2 subagents in
  one batched call** (MISSION.md floor is 8): six per-repo `scout`s + `critic` +
  `reviewer` + `sentinel` + `connector` + `planner`, route buckets per MISSION.md.
  Relocated the ledger to its canonical path (`git mv .ufo/reports/round-2/AGGREGATE.md
  .ufo/reports/AGGREGATE.md`); re-executed **100 citations** across the six corpora and
  the live domain surfaces; wrote one aggregator-owned lesson per child repo and
  committed each pathspec-limited under `aggregator-shokunin <aggregator@shokunin.local>`;
  reconciled the protocol lane's round-10 fallback queue (`D-01…D-49`) row by row against
  the tree and filed **34 new rows** (`D-50…D-83`); refreshed the promotion inputs, the
  mint/dormancy calls and the fleet-2 axis census; opened this lane's sections in the root
  `SCORECARD.md` and this `LOG.md` (both files were created by the protocol lane at round
  10, which recorded that the aggregator's axes were unscored).
- **Outcome.** Corpus review **2 → 8** (metrics C1–C8). Canonical ledger present; **79**
  durable `D-` rows where there were 0; 41/41 reports in the sweep window reconciled;
  **6/6** repos carry a committed round-6 aggregator lesson and a CORPUS.md rule-10
  verdict — all six `not conformant`, **34 majors, 65 defects**; 12 queue rows closed,
  landed or ruled this round. Credential material: **zero**, from 15 sweep classes plus a
  pickaxe history sweep over all seven repos. Domain source repos stayed **read-only**
  (operator rule): `bounties` HEAD `58acb6d8` with 903 dirty entries unchanged,
  `ufo-fsd-alpha` HEAD `ee907f1cf` with 62 unchanged; no commit or push outside
  `VeigaPunk/shokunin` and the six `VeigaPunk/<lane>-shokunin` remotes. Two self-defects
  filed against this lane for the exposure window its own files created (D-50, D-83).
- **Evidence.** `.ufo/reports/AGGREGATE.md` §11 (stamp + method, §11.1 verdicts and lesson
  commits, §11.2 the queue, §11.3 superseded verdicts, §11.4 promotion inputs, §11.5
  proposals P-f…P-m, §11.6 mint/dormancy, §11.7 self-defects, §11.8 census);
  `SCORECARD.md` §Aggregator lane (C1–C8, Q1–Q6, M1–M3, each with its command and the
  measured-against commits `0a30b44` → `78bd39b`); lessons kasegi `d341b48`, kengaku
  `3175e69` + `1bd17ec`, kake `ab8c9e2`, kumitate `0ac2272` + `31f09cd`, kotoba `778310d`,
  kagi `ad694a2`; report `.ufo/reports/round-6/aggregator.md`.
- **Falsifiable next iteration (round 7).** mint/dormancy calls — the lowest axis after
  this move (6/10). Land a standing, re-runnable assessment table in the ledger: one row
  per rostered lane (last dispatched round, last reported round, last `LOG.md` round token,
  last commit age, verdict) and one per watchlist candidate (demand instances with
  pointers, owning-province test, bar verdict), every row carrying the command this lane
  re-ran in the same refresh; the operator-gated kama half recorded as **blocked-external**
  against its L0 pointer. Falsified if any row lacks a re-run command, or if the kama row
  is re-flagged without naming the pending operator decision. Queued behind it (highest
  cross-lane-quality value, needs a full round): the **box-3 execution walkthrough** — one
  non-author agent per repo runs `SKILL.md`/`corpus/` with no oral context; target 6/6
  repos with a named non-author box-3 verdict committed in the repo.

## Round 11 — protocol lane — fleet-meta axis-move: protocol soundness (compaction) + closure execution

- **Trigger.** `SCORECARD.md` §Planned (round 10): compact `PROTOCOL.md`
  583 → ≤450 lines without dropping an obligation and resolve the named
  contradictions; the closure pass owed 7 `in-flight` rows plus every
  lane-round terminating after `closed_at` 18:21:16.
- **Action.** Ten L2 subagents in one batched call (4 scouts, sentinel,
  connector, critic, labrat, reviewer, scribe) produced: the obligation
  census (91 rows + 54 non-normative ranges tiling all 583 lines,
  machine-checked), a 93-predicate preservation verifier (baseline-green
  against HEAD), a 30-cluster duplication audit reconciling the round-10
  "17 pairs" at family granularity, a sibling-reference sweep (157
  `PROTOCOL.md` references across 56 files → must-survive anchors), and an
  incident digest. Landed `PROTOCOL.md` at 446 lines (`6bd4f38`): clusters
  collapsed to canonical homes, ~125 incident/measurement lines moved into a
  32-row dated appendix digest with pointers to the round reports,
  contradictions (a) driver-vs-ledger / (b) ledger queue-of-record / (c1–c3)
  resolved, the operator push-scope rule (`235b414`, `MISSION.md` §Push
  scope) carried as a pointer not a restatement, and an in-flight still-live
  re-confirmation clause added. A second batch (4 L2) falsified the
  candidate: critic — 5 must-fix items (broken `Contradicted rows` appendix
  pointer, stale `rounds[1]` re-count, self-contradictory lane-identity row,
  figure drift vs the r10 record, in-flight verb vs the new clause);
  reviewer — 2 commands split across line wraps + 1 wrong appendix pointer.
  All fixed before landing; the census, verifier, audits and verdicts are
  committed under `.ufo/waves/round-11/` so the preservation test is
  permanently re-runnable. Closure pass (`3ea42cb`): 7 entries appended
  (`rounds` 15→22) resolving all 7 carried `in-flight` rows and recording 16
  lane-rounds terminated 18:27:54–20:05:46, each step-1 verified (ancestry,
  SHONEN, ordering, marker screen); 3 terminated-mission reports left
  untracked by their lanes + 13 dispatch-evidence prompts landed for
  durability.
- **Outcome.** `wc -l PROTOCOL.md` 583 → 446 (target ≤450 met; body rewrapped
  ~78→100 cols — disclosed; bytes 38649→39264, +615 from the appendix
  pointer column and 2 new clauses); census 93/93 against the landed file;
  seed byte-identical; in-flight debt 7→0; last-wins 73 ok / 4 failed / 4
  in-flight (live missions only) / 23 not-dispatched; 0 new markers; first
  five self-landed lane-identity report commits observed (kumitate `9a2e9fb`,
  protocol `025b2e3`, kengaku `8ec7a56`, kagi `ade32e4`, kotoba `f9dcfd2`).
  Corrections to the round-10 record (appended, not rewritten): its "kake r10
  carries a conforming SHONEN heading" claim is FALSE (blob `6a45ff2` greps
  0), and its "0 of 62 reports under a lane identity" census was already
  false at write time (`9a2e9fb` 18:37:14 predates the report).
- **Evidence.** Commits `3ea42cb` (closure + durability + waves), `6bd4f38`
  (compaction); `MANIFEST.json` `rounds[15..21]`; `.ufo/waves/round-11/`
  (obligation-census.tsv, verify-census.sh, obligations.md,
  protocol-dupes.md, protocol-reference-sweep.md, scout-closure.md,
  verify2.md, ledger-status.md, stale2.md, critic-compact.md,
  reviewer-compact.md); round-11 report §Closure record, §Dispatch digest,
  §Conformance, §Routing.
- **Falsifiable next iteration (round 12).** gate-integrity: resolve the 4
  `in-flight` rows written at 20:10 (protocol r11, kengaku r11, kumitate
  r11, kotoba r12) plus post-`closed_at` terminations, and rule the
  verdict-gate standard question (land or reasoned rejection) — falsified if
  any carried `in-flight` row survives the round-12 pass unresolved or the
  gate question stays unruled.
