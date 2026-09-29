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

## Round 7 — aggregator lane — mint/dormancy axis-move: standing, re-runnable call tables

- **Trigger.** At round open this lane's lowest axis was **mint/dormancy calls, 6/10** (`SCORECARD.md` §Aggregator,
  after-r6 column): the calls were one-off prose in ledger §11.6, no watchlist candidate carried a dated bar test, the
  dormancy evidence line used a scan this round falsified as buggy (case-sensitive round tokens, `sort -V` ranking
  filename tokens above real `## Round N` entries, no attribution filter on the shared main `LOG.md`), and the
  operator-gated kama call risked being re-flagged every refresh instead of pointing at its pending decision. Round-6
  §Planned named this exact move and its falsifiable targets (6/6 lanes + 5/5 candidates with same-refresh re-ran
  commands; kama blocked-external against its L0 pointer; M4 0→5).
- **Action.** One axis-move. Dispatched **10 read-only L2 subagents in one batched call** (MISSION.md floor is 8):
  4 scouts (lanes ×2, kama, watchlist), 2 executors (§12.1/§12.2 table drafts), critic (6 falsification attempts),
  reviewer (10 citations), connector (4 sibling interactions), sentinel (6 exposure findings) — route buckets per
  MISSION.md. Landed ledger **§12 (refresh 5)**: standing dormancy table (7 rows, marker-graded per the protocol r10
  rule) + standing mint/watchlist table (5 rows, dated bar tests), per-row re-run blocks (§12.5), queue movement
  (§12.3), self-defects 9–11 (§12.4). Filed **D-85** (protocol: the D-39 "LANDED-serving" label conflates the serving
  plane — up on 34113 — with the config repoint, which never landed: both janitor and opencode configs still pin 8080)
  and **D-86** (integrator: `fleets/registry.json` contested scope, kasegi r13 vs kumitate r1). Absorbed both critic
  FALSIFIED findings before landing (marker-aware `last_report` cells; every volatile cell re-run at the cutoff
  22:55:03Z — the wave seed baseline was stale within ten minutes). Committed the round-6 ledger tail (§11.9 + D-84,
  +32 lines uncommitted since 19:34) in the same pathspec-limited commit per sentinel mitigation (D-83-class sweep
  hazard in the shared index).
- **Outcome.** Mint/dormancy **6 → 8** (metrics M3–M6). Falsifiable targets met: **12/12** table rows carry the
  command this lane re-ran in the same refresh; **M4 0→5**; kama recorded **blocked-external** against
  `.ufo/l0-questions.md` line 2 (byte-identical to `e333e7c` at cutoff → unanswered; the working-tree edits are new
  questions from kake r12 / kengaku r10, not answers) — not re-flagged. **kessho: the first positive firing of a
  written mint trigger in this ledger** — D-82's re-test condition fired (kotoba 4th verification-tooling builder
  `abef8aa`/`4dd7753`, kengaku 5th `0c51208`), dated re-test run: still below bar (all five absorbed in-province; the
  fleet-gate-standard demand names protocol/integrator as owner → placeable; connector dissent recorded). No lane
  dormant (0/7); the one watch row (kotoba r11 LOG lag) self-healed inside the refresh via lane commit `7d15407`.
  0 mints executed — correct: the bar is met only by kama and minting is operator-side (`MANIFEST.json` roster scope).
- **Evidence.** `.ufo/reports/AGGREGATE.md` §12 (stamp + cutoff, §12.1 table + R0–R5 re-run blocks, §12.2 candidate
  table + kama probes, §12.3 movement, §12.4 self-defects, §12.6 standing-note); `SCORECARD.md` §Aggregator round-7
  subsection (M3–M6 with commands, measured against `f9dcfd2`); `.ufo/reports/round-7/aggregator.md` (wave digest +
  this round's commit hash); wave scratch `/tmp/fleet-r7-agg/` (10 seat artifacts, volatile — digested in ledger and
  report). Verification: critic 6 attempts (4 SURVIVED / 2 FALSIFIED-absorbed), reviewer 10/10 citations PASS,
  sentinel 6/6 SAFE, executor fence-identity check 6/6 + 43/43 verbatim re-run lines.
- **Falsifiable next iteration (round 8).** cross-lane quality — the **box-3 execution walkthrough**: one non-author
  agent per repo runs `SKILL.md`/`corpus/` with no oral context; target 6/6 repos with a named non-author box-3
  verdict committed in the repo. Falsified if any cold run is executed by the repo's author lane or if a verdict stays
  uncommitted. Standing: §12 re-tests every refresh — its rows are cutoff-stamped claims, not facts.

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

## Round 8 — aggregator lane — cross-lane-quality axis-move: box-3 non-author cold runs

- **Trigger.** At round open this lane's lowest axis was **cross-lane quality, 7/10** (`SCORECARD.md` §Aggregator,
  after-r7 column), and ledger §11.4 carried an unbroken fleet-wide gate: *"no repo has a single `[x]` on box 3 from a
  named non-author verifier"* — every box-3 claim in six repos rested on a lane-dispatched subagent, which PROTOCOL.md
  counts as the lane. Round-6 §Planned and round-7 §Next both queued this exact move. Opening the round also surfaced
  an inheritance debt: **round 7's artifacts were written and never committed** (ledger §11.9+§12, this file's Round-7
  entry, `SCORECARD.md` §Round 7, `.ufo/reports/round-7/aggregator.md`) because the driver completed that mission on
  report-file existence at 20:13:17 — three minutes after the report reached disk and before its commit step ran.
- **Action.** One axis-move plus the inherited landing. Dispatched **15 L2 seats in one batched `task` call**
  (MISSION.md floor is 8): six `labrat` box-3 cold-run verifiers (one per child repo, entry `SKILL.md` only), three
  `scout`s (sweep window, dormancy §12.1, mint §12.2), one `executor` (§13 skeleton), plus `connector`, `sentinel`,
  `critic`, `reviewer`, `distiller`. Landed ledger **§13 (refresh 6)**: §13.1 verdict tables + the four absorbed
  methodological rulings, §13.2 sweep + 24 new `D-` rows + 14 closure/movement rows, §13.3 standing tables re-tested,
  §13.4 the round-7 landing and the ordering rule it falsifies, §13.5 self-defects 12–18, §13.6 host-verified re-run
  blocks, §13.7 residual gaps + proposals P-n…P-r. Committed the round-7 orphan **unedited** at `6d27283` and pushed it
  before starting §13, so the refresh-5 bytes stopped being sweep-bait in a shared index.
- **Result.** **X1 0/6 → 6/6**: every child repo now holds `corpus/lessons/round-8-aggregator-box3-coldrun.md` with a
  named non-author verdict, committed under the aggregator identity, pathspec-limited, **not pushed** (sentinel ruling:
  MISSION.md §Push scope gives this lane no child remote — round 6's six child pushes are retro-classified as
  out-of-scope, self-defect 18). Operative grades **4 `[x]` / 2 `[~]` / 0 `[ ]`**: kengaku `[x]` (grader 149 checks /
  0 mismatches / `VERDICT: PASS`), kake `[x]`, kagi `[x]` provisional, kumitate `[x]` (original `[ ]` **withdrawn**),
  kasegi `[~]` provisional, kotoba `[~]`. 115 commands executed (105 ok / 10 fail), 28 break points cited to quoted
  `SKILL.md` text, 30 gated rows classified under the protocol's three-outcome rule. §11.4's gate observation is
  **closed as written** and superseded by a sharper one: no `SHONEN.md` box-3 line names a resolvable non-author
  verifier yet — the marks are the lanes' to update (`SHONEN.md` is outside this lane's write scope).
- **The critic earned its seat.** 7 attempts → **4 FALSIFIED**, all absorbed mid-round by an amendment protocol sent
  to all six seats (append-only `## Round-8 amendment (critic-absorbed)`, 6/6 landed): coldness is relative to the
  entry file, not the runner (`context-leak` class added); blanket `[~]` for operator-gated provinces was wrong
  (three-outcome rule); X4 was unfalsifiable as first stated (repaired); and grading a dirty tree measures the lane's
  in-flight edit, not the repo (full `git status` file set + HEAD-vs-worktree attribution + `provisional` marking).
  That last fix **reversed a verdict**: kumitate's `[ ]` rested on `scripts/proxy-check.mjs`, untracked at the run
  HEAD, probed against a file the lane deleted mid-audit. This lane then re-executed at the lane's landed commit
  `59e6c0c` — tool tracked, `PROXY: MATCH`, exit 0, clean tree — lifting the provisional marker (`942afe4`).
- **Non-author audit of the auditor.** Reviewer re-executed **41 citations → 30 PASS / 8 STALE / 3 FAIL**, and all
  three FAILs were this lane's own: §12.1/§12.3's kotoba "self-healed by 22:55Z" (the entry actually landed 23:27:55Z,
  33 min after the cutoff), §12.5's R4 token scan (unrunnable on this host — `grep` is pi-uu-grep 0.2.0 and emits
  zero-length matches for `-oE '[0-9]+$'`, while the block was labelled "copy-paste runnable"), and the round-7
  report's L0 count (7 claimed at a cutoff whose blob had 6 lines). Filed as self-defects 13–15; §13.6 ships only
  host-verified commands.
- **Queue integrity became a measured property.** Distiller: 84 distinct keys, next free D-87, 2 duplicate groups
  (D-39⊇D-85, D-51⊇D-84), 3 standing contradictions. Sweep found protocol r11 filing nine new rows numbered
  `D-50`…`D-58` — **keys this ledger already owns** — and asking for them to be mirrored as-is; the mirror was
  **refused as numbered** (D-87) and the rows re-keyed D-111…D-119 with protocol's text and pointer preserved. Also
  filed: D-88 (existence-only completion vs the report's own commit — the round-7 root cause, with the one-invocation
  write+commit+push fix this round adopted), D-89 (87 stale `PROTOCOL.md:<line>` cites after the r11 compaction),
  D-105 (a skill verb that unconditionally clobbers a shared manifest **outside every repo**, triggered by an audit
  cold run — proposal P-n), D-106 (this lane's own round-6 lesson cited an `awk` that cannot produce its own observed
  value — **closed** by self-repair `2839f60` in kotoba-shokunin).
- **Standing duty discharged.** Dormancy 7/7 rows re-tested, **0 dormant** (derived, not asserted), with a new scan
  correction: commit-age cells must filter aggregator seat commits (`--author='^(?!aggregator-shokunin)'`), else this
  round's own 16 child-repo commits get attributed to the lanes — kotoba's unfiltered cell would have understated its
  commit age ~25×. Mint 5/5 re-tested: kama **blocked-external** (L0 line 2 byte-identical to `e333e7c` →
  unanswered, not re-flagged; drift persists, D-39/D-85), kessho's builder trigger **fired again** (6 lanes / 9
  artifacts, still 0 unplaceable → below bar), D-86 **ruled**, axis-framework-stewardship's re-check **discharged**,
  mints executed **0** over 22 `rounds` entries.
- **Evidence.** Main repo: `6d27283` (round-7 landing, pushed) + this round's ledger/scorecard/log commit + the report
  commit named in `.ufo/reports/round-8/aggregator.md`. Child repos (16 aggregator-identity commits, unpushed by
  ruling): kasegi `9dbe69f` `2b0d869`; kengaku `d8f2898` `06cdc98`; kake `69c1856` `4c9a985`; kumitate `e79fefa`
  `0f24ca7` `942afe4`; kotoba `683d147` `7163c81` `ed5c261` `2839f60`; kagi `e0a04d8` `7c3377c` `4391b3b`.
- **Falsifiable next iteration (round 9).** cross-lane quality: re-run the three provisional verdicts (kasegi, kake,
  kagi) against each lane's landed commit and route the `SHONEN.md` box-3 mark updates — falsified if a provisional
  verdict is restated without a re-run at the lane's new HEAD, or if the round ends with zero lanes citing a round-8
  verdict. Owed and not to be aged: re-emit the CORPUS.md rule-10 conformance verdicts (two refreshes stale).

## Round 12 — protocol lane — fleet-meta axis-move: gate integrity (closure became an executable gate)

- **Trigger.** `SCORECARD.md` §Planned (round 11) named gate-integrity the lower axis, 7 against
  protocol-soundness 8, with two queued items: resolve the four `in-flight` rows written at
  `closed_at` 20:10 (protocol r11, kengaku r11, kumitate r11, kotoba r12) plus every lane-round
  terminating or dispatched after it, and rule the verdict-gate standard question kengaku r10 filed
  in `.ufo/l0-questions.md`, with kumitate r10's driver-adoption question beside it.
- **Action.** Fourteen L2 seats in two batched calls. Wave 1 (10): two scouts (the lane-round table
  and required-append set; a survey of five sibling verdict gates that executed all five hermetic
  self-tests as a non-owner — kumitate `57/57`, so the `49/49` in the L0 question is stale), two
  executors (`closure-check.py`; the `## Gate standard` candidate), a revenger (a 15-item semantics
  spec recovered from the round-10/11 reports, since round 11's `hexcheck.sh` lived in
  `/tmp/shokunin-r11/` and was never committed), a critic on the approach, a connector on sibling
  overlap and contested scope, a reviewer running closure step 1 independently over 12 reports and
  19 prompts, a sentinel ranking the four spoofable inputs, and a labrat on two falsifiable probes
  (the liveness-probe clause holds: the driver's own live-grep still matched all four post-20:10
  completed runIds, 12/12). Wave 2 (4): a critic on the written candidate, a reviewer re-executing
  every citation in it, a mutation-tester running seven bounded mutants against `MANIFEST.json` with
  exact-byte restores, and a scribe hashing the artifact inventory. Landed: `closure-check.py`
  (stdlib only, read-only, exit map 0 clean / 1 debt / 2 could-not-evaluate / 3 no-baseline,
  selftest 15/15, three timestamp-coherent frozen baselines, `--show-keying`, a citation sweep), 14
  `rounds[]` entries across three `closed_at` instants (22→36), `PROTOCOL.md` §Gate standard plus
  seven pins, and nine dispatch-evidence prompts committed for durability.
- **Outcome.** Live gate: exit 0, `debt=0 contradictions=0 unrowed_terminated=0`; last-wins 83 ok /
  4 failed / 7 in-flight (all live missions) / 18 not-dispatched over 112 rows, with 16 legacy
  fleet-keyed rows named `unadjudicable` instead of being silently scored. Mutation score 7/7
  determinate after fixes (first run 4/5, with m4's `lane_rounds` re-key trap surviving and m3
  crashing on an unknown lane). Census preserved 93/93 and body incident refs held at 4. The gate
  caught four rows this lane's own 21:20 pass owed and missed — aggregator r8, kengaku r11,
  kumitate r12, kotoba r13, each with termination or landing evidence inside that instant — and the
  21:30 pass closed them. Cost disclosed: `PROTOCOL.md` 446→526 lines / 39718→49041 B, so
  protocol-soundness is held at 8 rather than raised; the critic's recommendation to delete the
  36-line §Gate standard is recorded and rejected in the report §Length cost.
- **Evidence.** Commits `7c56d1e` (first closure pass + four prompts), `dddb4ec` (§Gate standard +
  six pins), `df1b2c6` (second pass + `supersedes.entry` + the L0 queue under the new durability
  duty), and this one (third pass + wave artifacts + scorecard/log); `MANIFEST.json` `rounds[22..35]`;
  `.ufo/waves/round-12/` — `closure-check.py`, `exec-checker.md`, `mutation-gate.md`,
  `mutants/mutant-score.json`, `frozen/{pre,post-actual,post}`, `fixtures/closure-sample/`, and 13
  seat artifacts; report `.ufo/reports/round-12/protocol.md`.
- **Falsifiable next iteration (round 13).** gate-integrity: answer every row the live gate flags
  after `closed_at` 21:30 (eight missions were live then, six already past two ticks) and get the
  four gate-owning lanes' `SKILL.md` registry rows landed — falsified if any `stale_in_flight` row
  survives the round-13 pass, or if the registry schema exists with zero rows in it.
  protocol-soundness: compact 526 → ≤470 lines with the census still 93/93 and body refs still 4 —
  falsified if a census predicate drops or the body ref count rises.
