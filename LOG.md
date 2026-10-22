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

## Round 9 — aggregator lane — corpus-review axis-move: verdicts re-emitted at named revisions, then made re-derivable

- **Trigger.** All three aggregator axes were tied at **8** (`SCORECARD.md` §Aggregator lane), so the lowest axis was
  decided by debt, not by the number: `CORPUS.md` rule 10 (*"each round's review emits a verdict per repo"*) went
  **unpaid at refresh 6** — ledger §13.7 named it owed, and §11.1's six `not conformant` verdicts were three refreshes
  stale, measured at HEADs that are now ancestors **6–17 commits back** (verified per repo with `cat-file -e`,
  `rev-list --count <h>..HEAD`, `merge-base --is-ancestor`). Round 8's §Planned had queued cross-lane quality for this
  round; the switch is recorded rather than smuggled (critic attempt A1 → self-defect 26), and the queued cross-lane
  residual was **not** dropped — the three provisional box-3 re-runs are inputs to the verdicts.
- **Action.** One axis-move, **15 L2 seats in one batched `task` call** (MISSION.md floor 8): six `labrat` per-repo
  verdict seats, two `scout`s (sweep window, standing tables), one `executor` (the gate), plus `critic`, `connector`,
  `reviewer`, `distiller`, `sentinel`, `revenger`. Landed ledger **§14 (refresh 7)**: §14.1 the revision-stamp method
  change, §14.2 the six verdicts, §14.3 the rule numbering published, §14.4 rule 8 on its literal text, §14.5 rule 7
  split, §14.6 box-3 re-runs, §14.7 the `SHONEN.md` census, §14.8 the gate-standard adoption matrix + this lane's gate,
  §14.9 standing tables, §14.10 sweep + queue, §14.11 the round-8 record corrected, §14.12 self-defects 20–26, §14.13 L0
  surfacing, §14.14 re-run blocks, §14.15 residuals + proposals **P-s…P-v**, §14.16 29 routed rows **D-121…D-149**,
  §14.17 the post-mirror re-run.
- **Result.** **6/6 rule-10 verdicts re-emitted, all `not conformant`, each naming the revision it measured** (kasegi
  `b7180b0`, kengaku `f09ff1f`, kake `a209441`, kumitate `e0e5de1`, kotoba `63ceba7`, kagi `4391b3b`; every one also
  re-checked at the newer HEAD it drifted to). **V2 0→1**: `.ufo/waves/round-9/corpus-gate.mjs` — exit map
  `0=clean 1=failed 2=could-not-evaluate 3=failed(frozen drift)`, 6 checks implemented, **7 declared `not-evaluated`
  with reasons** instead of faked, self-test **12/12** asserting exit code *and* ordered finding-ids against committed
  `corpus-gate.expected.json`, **8/8 frozen snapshots MATCH** re-run by the L1 itself. **V7**: the gate's teeth proved
  live — its six `r10` findings dropped to **0** across all six repos once the lessons were mirrored, with no edit to the
  gate. **V6 0/15 → 15/15**: the whole wave is committed, which is the structural fix for round 8's worst defect.
- **Two of this lane's own published cells were falsified by its own seats.** A `reviewer` re-executed 15 cells of the
  round-8 record: **5 PASS / 4 STALE / 6 FAIL** — X2 (115/105/10 → **99** indexed rows exist), X3 (28 break points →
  **17**), X4 (30 gated rows → uncountable from the committed tables), X8 (41 re-executions → **no committed cell
  ledger**; `.ufo/waves/round-8/` does not exist), the report's "17 child commits" vs its own 16/15, and §11.1's rule-8
  "clean everywhere". Root cause in one line: **round 8 committed the ledger and the report but not the wave**, so its
  aggregates were author-asserted over payloads nobody can reach. A `scout` also found §13.6-B's published resolver
  ("operative grade = last bold mark") returns kumitate's **withdrawn** `[ ]`, and §13.3's kessho cell "6 lanes / 9
  artifacts" carries no command and contradicts its own five-lane list (re-derived: 5 lanes / 15 harnesses).
- **The auditor is the fleet's dominant rule-8 offender.** Graded on the literal text of `CORPUS.md:43-46` (*"vault ref
  paths (`op://…`) stay out of every corpus, **including this one's examples**"*) at named revisions, **all six** corpora
  are FAIL-literal / PASS-intent (occurrences 2/1/2/1/3/77; no secret value observed or printed; classification declared
  `could-not-evaluate` because deciding it needs an operator-gated vault read). In **5 of 6** repos the hits sit in files
  **this lane authored** (`round-5-`, `round-6-aggregator-audit.md`) while refresh 4 published rule 8 as clean fleet-wide
  — self-defect 20. Related, and worse because a sibling can see it: **138 unqualified cross-repo citations** in this
  lane's mirrored lessons, **6 of which kagi's own citation gate counts `UNRESOLVED`** (`CITATION_GATE: BROKEN …
  unresolved=33`) — self-defect 25, fixed forward by a path-convention line + `shokunin:<path>` qualification (**9 → 0**
  in this round's six drafts, scanner re-run) and routed as **P-t**.
- **The critic earned its seat again.** 7 attempts → **4 FALSIFIED / 6 REPAIRED-BY-AMENDMENT / 1 SURVIVES**, all
  absorbed before landing: the axis switch must be recorded (A1); "re-derivable" means a frozen committed snapshot plus
  an exact-revision run, since self-test green is capability not measurement (A2); `stays provisional` is a legal third
  box-3 outcome and every cell needs its revision (A3); the gate is **unregistrable as written** for a main-repo lane —
  §Gate standard puts registry rows in "each lane's `SKILL.md`" and `ls SKILL.md` → absent — so it is routed (**D-127**,
  proposal **P-v**, the D-120 class repeating) and never called conformant (A4); `6/6` counts only literal
  conformant/not-conformant verdicts, so kasegi's missing province root yields an observable **failed citation** (740 of
  782 distinct path citations unresolvable), not an unevaluable repo verdict (A6); rule 8 is graded literally, not by
  inheritance (A7). Survives: `.ufo/waves/round-9/**` is inside this lane's write scope (A5, `PROTOCOL.md:434-435` plus
  the `closure-check.py` precedent).
- **Box-3 residual resolved, not restated.** kagi **breaks**: three of its own gates are red at **two** landed revisions
  (`claim-ledger verify` exit 1 `FAIL (claims=17 failed=1 stamped=33)`, `citations` exit 1 `BROKEN (unresolved=33)`,
  `transcript-scan` exit 1 `HITS=2` at `4391b3b` and `4b8c018`) while `drift-pins` (exit 0, `files=15 symbols=20`) and
  `surface-census --selftest` (exit 0, 16 cases) are green — so its `SHONEN.md` box-3 `[x]` is contradicted by its own
  tooling (**D-133**). kasegi is **could-not-evaluate** at every landed revision (`git ls-files ops/ | wc -l` → 0 at
  `b7180b0` and `0f2dca0`, and its input tree is gone). kake **stays provisional** with a named cause. kengaku **firms**
  (`CHECKS n=280 mismatches=0`, up from 149 at round 8) and kumitate **firms** (`PROXY: MATCH` at `e0e5de1` and
  `7a099b2`, its terms moving 16/18→18/19 and 43/43→45/45 and still matching). Round 8's residual is also **partly
  falsified**: kengaku's box-3 evidence line *does* name a resolvable non-author — but **0 of 6 `[x]` marks fleet-wide
  carry the `<verifier-id>`** the canonical form requires (§14.7, first-ever census: 3 trivially clean, 3 deviate).
- **Standing duty discharged.** 12/12 standing rows re-run, **all 12 moved** inside the hour; dormancy **0/7** with still
  no positive test case in seven refreshes; kama's bar is met and stays **blocked-external** — its L0 line is
  byte-identical to the `e333e7c` blob (md5 `643e7114dd5f9286cdf27a4a654bc800`) ⇒ unanswered, **not re-flagged**;
  endpoint drift persists (34113 → HTTP 200, 8080 → 404, both configs still pin 8080); kessho below bar; mints executed
  **0** over **36** `rounds` entries. L0 surfacing: 11 lines classified by git forensics — **0 operator answers ever**,
  1 **answered by protocol ruling** (kengaku r10 ← §Gate standard), 1 superseded (kasegi r12 ← r15), 9 open
  operator-only; **1 new line appended** (the `CORPUS.md` amendment set: D-125/D-126/D-141/D-142).
- **Evidence.** Main repo: ledger §14 + this entry + `SCORECARD.md` §Round 9 + `.ufo/waves/round-9/` (gate
  `68939d0c…cfb8`, expected `c358e79a…f9ba`, 15 seat files, 6 lesson drafts, `CONTEXT.md`, `l1-baseline.md`) + the
  round-9 dispatch prompt, in the commit named in `.ufo/reports/round-9/aggregator.md`. Child repos (six
  aggregator-identity lesson commits, single-file, **unpushed by ruling**): `b021dc9` `e171cdf` `4214101` `93b0567`
  `0f658ff` `baec94f`.
- **Falsifiable next iteration (round 10).** corpus review: make the verdicts non-author re-derivable end to end —
  resolve the gate's registry home (D-127/P-v) or record a reasoned rejection; close the `r4` heuristic's three declared
  false-positive classes (246 findings) until the cell is defensible as violations; re-run the gate at each lane's next
  landed revision and report per-rule movement. Falsified if the gate is called conformant while unregistrable, if the
  `r4` cell is restated without its FP classes, or if any verdict fails to name its revision. Owed and not to be aged:
  the round-8 X-cells are corrected in §14.11 but the round-8 section still reads as published (D-129), and D-133 must be
  re-tested at kagi's next landed revision.

## Round 11 — aggregator lane — mint/dormancy axis-move: first mint counted, probation + 8-lane dormancy

- **Trigger.** The three aggregator axes entered this round at 8/8/9
  (cross-lane quality / mint-dormancy / corpus review). Mint/dormancy won the
  tie on live evidence: `MANIFEST.json` now has the fleet's first
  `type:"mint"` entry (kama), while the standing census still inspected
  `rounds[].minted` truthiness and the table still treated kama as a blocked
  candidate.
- **Action.** One batched call dispatched 12 L2 seats: four scouts, executor,
  critic, connector, reviewer, sentinel, distiller, revenger, and a
  corpus-currency scout. The wave is durable at
  `.ufo/waves/aggregator-r11/seats/` (12 files, 2,449 lines, 262,860 bytes).
  The L1 re-ran the mint census, all eight dormancy rows, the corpus gate
  selftest and live verdict pass, queue keys, L0 forensics, report history,
  and the effective model config.
- **Result.** Mint/dormancy **8→9**. The census now keys on
  `type=="mint"`: **1** executed mint, kama. `rounds[36]` correctly records
  probation; the six-id roster remains correct until three verified rounds
  land. Kama has r1 complete and r2 live. Dormancy coverage moved **7→8**:
  **0/8 dormant**, with kengaku and kotoba one missing LOG entry short of the
  literal two-round trigger. The current-wave heading-only LOG matcher was
  rejected after returning zero for six of seven child repos; per-repo
  date-bullet/heading grammars reproduced every verdict.
- **Standing duties.** Corpus gate selftest **12/12 PASS**. Six original
  corpora remain not conformant at named revisions (55/30/45/55/82/60
  findings); kama's first verdict is not conformant because 3/5 lessons lack
  a commit or report pointer. L0 forensics classified 19 content lines:
  15 open, 3 superseded, 1 answered-by-event, 0 operator-answer markers.
- **Cross-lane findings.** `17c1fad` overwrote kotoba's real round-15 report
  (14,715 B at `4419fb9`) with a 273 B marker; the same commit staged
  `kama-shokunin/` as an embedded gitlink, reverted 13 seconds later by
  `8afbc8f`, while `.gitignore` still omits it. The closure ledger's latest
  `closed_at` is 22:23 -03; 17 distinct later `complete` lane-rounds include
  kama r1. Routed as D-151…D-155 in ledger §15.
- **Operator relay.** Effective config shows
  `modelRoles.m_swe=devin/swe-2:max` and
  `retry.fallbackChains.m_swe=null`; the requested final Daybreak fallback is
  not visible. No genuine m_swe capacity failure occurred, no failover is
  claimed, and no frozen route was changed.
- **Evidence.** `.ufo/reports/AGGREGATE.md` §15; `SCORECARD.md` §Round 11;
  `.ufo/waves/aggregator-r11/seats/`; dispatch prompt
  `.ufo/prompts/aggregator-round-11.md`; report
  `.ufo/reports/round-11/aggregator.md`.
- **Falsifiable next iteration (round 12).** Cross-lane quality: re-run the
  six box-3 verdicts after rounds 14–17 and add canonical report durability
  to the grade. Falsified if an overwritten marker remains a current report
  or any verdict lacks the revision it measured.

## Round 15 — protocol lane — fleet-meta axis-move: gate integrity

- **Trigger.** Both owned axes entered at 8. Gate integrity won the tie: the
  r13 successor still lost a log-only lane when its counter disappeared, did
  not recognize fleet-wrap termination, and silently skipped non-closure
  entries. The pinned pre-cutoff carried 17 closure findings.
- **Action.** Four implementation/review seats and one batched ten-seat final
  audit covered execution, snapshots, mutation, planning, scouting, criticism,
  connection, review, security, simplification, and evidence distillation.
  Commit `3687e5a` lands the 2060-line gate, 948-line snapshot generator,
  25 fixture repos plus two parser unit checks, seven mutants, two frozen
  snapshots, and `MANIFEST.json` rounds 48→74 (26 entries / 34 lane rows).
- **Outcome.** Gate integrity **8→9**. The universe now closes over roster,
  base ids, counters, log lines, and parseable prompt names; wrap termination,
  non-closure records, and could-not-evaluate classes are explicit. Final
  controls: checker 27/27, generator 37/37, mutations 7/7; gate sha256
  `0ac440f7…9a778c`. Frozen closure debt moves 17→0 with matching input
  digests at `00:34:00` and `01:27:10`.
- **Boundary.** This is a cutoff-bounded result, not a live-clean claim. The
  final smoke observed exit 1 / debt 10 from later terminations and generated
  prompts; protocol r15's report also lands after the post cutoff and rides
  the next correction. Frozen prompt indexes do not encode git trackedness.
  Effective config still showed `retry.fallbackChains.m_swe=null`; no genuine
  m_swe capacity failure or Daybreak advancement was observed.
- **Evidence.** `3687e5a`; `.ufo/waves/round-15/`; `MANIFEST.json`
  `rounds[48..73]`; `.ufo/reports/round-15/protocol.md`.
- **Next.** Protocol soundness (8): resolve the main-repo gate-registry home
  and register this gate at a revision. Falsified if a gate is called
  conformant while its registry still requires a nonexistent main `SKILL.md`.

## 2026-10-13 — fleet relaunch: remotes + repo split

- Fleet root merged with 2026-09-era remote `VeigaPunk/shokunin`
  (`--allow-unrelated-histories`): old lane artifacts preserved in
  ancestry + tree; MANIFEST union = 12 roster rows, 79 round records.
- Six current lanes extracted/confirmed as standalone repos under
  `~/Projects/shokunin/<id>-shokunin/`; remotes named `shokunin-<domain>`,
  all public. Prime lanes carry their full prymeagnt craft-branch history
  (filter-repo prefix extraction); kaidoku native since mint.
- Protocol docs re-vendored from live upstream `kimi-shokunin`
  (`812f1da`, 2026-10-13).
- Evidence: merge commit; `gh repo view VeigaPunk/shokunin-*`.

## 2026-10-13 — canon roster restored

- ROADMAP roster restored to the canonical `Shokunin | Domain | Rank`
  shape — the 2026-09 lanes are first-class canon, not an archived tier;
  the six 2026-10 lanes join under the same `<id>-shokunin` naming.
- kama-shokunin roster row landed — mint was sanctioned in
  `.ufo/l0-questions.md` (round-10 aggregator ruling, two unplaceable
  demand instances); remote `VeigaPunk/kama-shokunin` exists since
  2026-09-29. Evidence: merge ancestry + remote.
- Remote convention noted: `<id>-shokunin` (2026-09, private) vs
  `shokunin-<domain>` (2026-10, public); canonical name is always
  `<id>-shokunin`.

## 2026-10-13 — canon lanes reactivated locally

- All seven 2026-09-era lanes cloned to `~/Projects/shokunin/<id>-shokunin/`
  and declared in `shokunin.conf` LANES (owned axes per each lane's
  SCORECARD). They are current lanes, not archive: next rounds continue
  from their last commits (kasegi r18, kengaku r14, kake/kumitate/kotoba/kagi
  r17, kama r2). Prime lanes also declared for completeness.
- Evidence: `gh repo list`, lane clones, conf diff.

## 2026-10-13 — consolidation + canon lanes public

- prymeagnt `.shokunin/<lane>` replaced by symlinks → canonical repos at
  `~/Projects/shokunin/<lane>-shokunin/` (committed + pushed per lane
  remote). Verify paths keep resolving through the link.
- Seven 2026-09 canon lanes made public per operator decision.
- Craft-hours mechanism fully reverted everywhere (upstream, fleet,
  all 13 lanes) — history retains add+revert.
- Evidence: worktree commits; `gh repo view`; lane remotes.

## 2026-10-14 — round 11 (final training-round re-run): aggregator cross-lane quality 8 → 9

- Landed the round-11 report's declared next axis-move (cross-lane quality):
  committed `cross-lane-gate-v1` (`.ufo/waves/aggregator-r11/cross-lane-gate.mjs`,
  selftest **6/6**) grades report durability over the fleet's 46 presented
  reports (rounds 11–18): **117 findings** — 5 `marker-overwrite`
  (kengaku r12 274 B, protocol r13 275 B, protocol r14 340 B, kotoba r15
  273 B = the D-153 case, kasegi r16 273 B), 2 `verdict-without-revision`
  (kengaku r13, kagi r15), 110 `cited-commit-missing` (host-state class:
  several resolve in `~/Projects/ufo-fsd-alpha`; the rest cite revisions of
  repos gone from the host — `bounties`, `webzites`, `llm-wiki` absent);
  exit 1 (failed, expected). Gate, expected values and raw logs committed
  under `.ufo/waves/aggregator-r11/`.
- Re-ran the six box-3 corpus verdicts at the lanes' current revisions
  (kagi `fecee87` 63, kasegi `d1e6e8f` 55, kengaku `d84e48d` 30,
  kake `b0feb30` 45, kumitate `175de6b` 102, kotoba `02302c5` 82;
  still 0/6 conformant); `corpus-gate.mjs --selftest` 12/12 PASS.
- Falsifiers: both clauses of the round-11 report's falsifier are now explicit
  grades — the kotoba r15 marker (273 B now vs 14,715 B at `4419fb9`) fails
  as a current report, and verdicts without a measured revision fail.
- Evidence: `.ufo/waves/aggregator-r11/seats/cross-lane-quality.md`,
  `seats/cross-lane-gate.log`, `seats/corpus-verdicts.log`,
  `cross-lane-gate.expected.json`; `SCORECARD.md` §Round 11 (final re-run).
- Not pushed: no domain/child-repo bytes changed; the `kama-shokunin/`
  gitlink and live `.ufo/state/*` stay untouched and uncommitted.

## 2026-10-14 — operator program preflight: roster loading repaired; UFO dispatch blocked

- The requested 12-hour program opened the UFO Sighting wall but dispatched no
  L1/L2 mission. This is an operator-side preflight record, not a craft round,
  mint, promotion, native judgment, or saturation claim.
- Repaired `shokunin.conf`'s premature closing quote after revenger; all
  pre-existing declarations are now inside `LANES`. Before:
  `bash -n shokunin.conf` exited 2 at tameshi's row. After: syntax exit 0;
  actually sourcing the configuration returned the 17 existing child lanes
  plus protocol and aggregator, in their existing order, without duplicates.
  No watchdog was started and no lane was added.
  Receipt: `.ufo/scopes/shokunin-12h-20261014/evidence/config-load.json`.
- `@m_sol` is declared as Sol 6.1, but the requested composer-content /
  grok-scrutiny split is absent from the live global seat table. The saved
  32-scope Phase 1 plan validates structurally; its actual route preflight is
  unprobed and resolves 20 members to `m_mid`, 12 to `m_fast`. It was not
  rendered with `run`, registered, or dispatched. Global routing was not
  changed. Evidence:
  `.ufo/scopes/shokunin-12h-20261014/phase1-repair/plan.json`.
- Native Phase 0 is blocked: contract check exit 1, actual canonical
  self-iteration smoke exit 2, `allContractsReady: false`. Recorded: 18 missing
  generated targets, six dependency omissions, sighting-surface digest drift,
  and 74 routing-equivalence mismatches. The successful routing-health command
  has zero ledger rows and proves no provider health. Full outputs and parsed
  evidence: `.ufo/scopes/shokunin-12h-20261014/evidence/`.
- The fallback wave also remains blocked by the requested route split.
  Source-substrate repair belongs to its owner; no origin source, global
  configuration, secret value, session payload, or child-lane file was
  modified. No pushes or external fetches were performed.
- WWKD map, phase dependencies, stop rules and the explicit blocked state:
  `.ufo/scopes/shokunin-12h-20261014/l0-wwkd-plan.md`,
  `data-walk.md`, and `preflight.json`. Child-lane axes are not reassessed:
  there was no dispatched round or before/after lane measurement.

## 2026-10-14 — blocked operator program: report and ledger durability

- Preflight work landed in `14e836c` under protocol lane identity. The
  operator-readable disposition is
  `.ufo/reports/shokunin-12h-20261014-preflight.md`; its report-last commit
  appends a `type: ops` MANIFEST note with that path, not child-lane statuses,
  fictitious training rounds, or mint credit.
- All five execution phases remain undispatched. The report names the
  global routing and UFO source owners' prerequisite actions. The native
  failure is recorded without substituting a swarm or synthetic verdict.
  Mori/chousa repos were not created; neither mint is claimed.
- Ledger preservation is checked against
  `.ufo/scopes/shokunin-12h-20261014/evidence/manifest-before.json`;
  delivery receipt:
  `.ufo/scopes/shokunin-12h-20261014/evidence/ledger-integrity.json`.
  No completion command is issued: no program wall mission exists.

## 2026-10-14 — 12-hour program: phases 1-2 landed, mints scaffolded, honest stop

- Phase 1 (six-lane re-census) landed with an independent audit; Phase 2
  (kumitate round 32) landed with `PROXY: MATCH` and both layer axes moved
  (script 6→10 terminal, runtime 6→8). Phases 3 and 5 are specified and
  validated but undispatched; mori round 1 was dispatched and is still running.
- `mori` and `chousa` minted as shonen (seed commits `27acf40`, `02a615a`),
  wired into `shokunin.conf` (21 entries, syntax clean), MANIFEST `type: mint`
  entries appended, NO roster rows. Probation ≥3 verified rounds still owed.
- Global routing untouched: the requested composer/grok split and the later
  connector-on-Antigravity-with-ZAI-fallback instruction were applied as
  session-only alias selection and never saved.
- Full report: `.ufo/reports/shokunin-12h-20261014-fleet-report.md` (appended to
  `MANIFEST.json` `rounds[]` as a `type: ops` entry). Every claim in it is tied
  to a measured command; no promotion, roster row or native verdict is claimed.

- Conformance defect (found by the mori `WaveSettlement` audit, repaired):
  wave registries were persisted into the **read-only substrate** because the
  planner was invoked with the UFO checkout as cwd, so its `ROOT` resolved there.
  Six stray `.ufo/scopes/Shokunin12h*` dirs were moved into the fleet root and the
  substrate was left clean; assignments verified intact. Recorded in the fleet
  report. Future waves must set `UFO_PROJECT_ROOT` to the fleet root.

- Roster debt recorded (operator-owned, not edited): 6 of 13 `MANIFEST.json` roster
  rows name a `repo` path absent on disk (`shokunin-<domain>` public-remote style vs
  the canonical `<id>-shokunin` checkout). Consumers must resolve the live
  `<id>-shokunin` directory; the operator reconciles the six fields. Found by the
  mori `LaneSilence` audit, which also established that the silence baseline is each
  lane's own report mtime, not the shared round-directory mtime.

- Wave-registry invocation fixed and recorded: `UFO_PROJECT_ROOT=<fleet-root>` plus a
  relative `--registry` is the only form that writes into the fleet root (an
  absolute path is refused `invalid_registry_path`; omitting the env var writes into
  the read-only substrate). All six registries re-recorded at 32/32 assignments.
- Phase 5: chousa probation round 1 dispatched (`Shokunin12hP5ChousaR1`, 32 lanes,
  local-only survey of the research artifacts — no external fetches).

- Phase 5 chousa round 1 left **in-flight** at session close: 5/32 member
  reports delivered on disk, integration (QUALITY.md, corpus map, research-gate.sh)
  not performed. Recorded as in-flight debt in `MANIFEST.json`, never as a closed
  round. The 12-hour program's remaining blockers are listed in the fleet report:
  Phase 3 (kengaku) undispatched, mori round 2 undispatched, chousa round 1
  integration, chousa round 2.

## 2026-10-15 — fleet driver started: 21 lanes, 100+ round target

The operator asked to continue the program at >=100 rounds per lane with no budget.
That scale is what the respawn-per-round driver exists for, so the fleet is now
running under `kimi-shokunin/scripts/shokunin-watchdog.sh` (tick 450s, ROUND_CAP
1024) instead of hand-dispatched waves.

**Launch.** `SHOKUNIN_ROOT=/home/vgpnk/Projects/shokunin bash <canonical>/scripts/shokunin-watchdog.sh`.
All **21** rostered lanes launched on the first tick with prompts rendered from
`templates/round-prompt.md` (staged into the fleet root — the driver requires it
there and it was absent). No `launch-fail` on the real tick; 21 `omp -p` lane
processes observed; memory 20G/30G used, load 1.13.

**Three config defects found and fixed to get there:**

1. **`SUBSTRATE_CMD` dropped.** My first narrowing rewrote the conf from `LANES="`
   onward and deleted the launcher line, so every lane logged
   `launch-fail … :: SUBSTRATE_CMD unset`. The full roster is preserved at
   `shokunin.conf.full-roster-20261015`; the conf is now the full roster with the
   launcher intact.
2. **Axes strings break the prompt renderer.** `render_prompt` substitutes axes
   through `sed -e "s/{{AXES}}/$axes/g"`, so a `/` breaks the delimiter and an
   `&` expands to the match. kengaku's `LLM/model … & evaluation` produced
   `launch-fail kengaku round=13 :: prompt render failed`. Every lane's axes string
   is now `/`- and `&`-free (sanitized in both the conf and the backup).
3. **`templates/round-prompt.md` was absent** from the fleet root; staged from the
   canonical checkout.

**Counter conflation, recorded.** The driver's per-lane counters are the
authoritative round numbers (kagi 16, kake 16, kama 1, kasegi 17, kengaku 13,
kotoba 16, kumitate 17, protocol 14, aggregator 10). The "steered round 19/20/…"
labels used in this program's Phase-1 `MANIFEST.json` entries were **this
session's own numbering**, not the driver's counters. Both are recorded; the
ledger entries name the rounds they used.

**Also observed at launch:** lanes whose current-round report is a marker are
correctly re-launched by the driver (`lane-round-failed … marker/contentless report;
NOT advancing`) — kengaku r13 (274 B), kasegi r17, kama r1, kotoba r16 all re-ran
rather than advancing on a stub.

### Driver completion semantics — measured, with the one artifact named

The driver's completion signal is the report **path** plus content (a `SHONEN`
heading and >=400 bytes), with **no freshness check**. A lane whose counter points
at a pre-existing valid report therefore advances without doing new work. Measured
across the 21 lanes at launch: **4 such advances total** — kumitate 1 (report dated
10-13), kama 2 (10-13), mori 1 (10-14, and that report is genuinely this program's
filed round-1 report, so the advance is correct). The other 18 lanes do real work
from their next tick. Recorded because a larger pre-existing backlog would inflate
round counts without work, which I8 forbids.

## 2026-10-15 — Devin lanes removed; fleet attached to the Sighting wall

**Devin-owned lanes excluded.** `audio`, `game-dev-2d` and `game-dev-3d` are being
worked on Devin, so they were removed from `shokunin.conf` `LANES` (and from the
full-roster backup): the driver no longer launches them, their lane processes were
killed, and no process touches those repos now — verified 0. Their repos hold
Devin's in-flight work (465 / 77 / 3 dirty paths) which this program did **not**
touch. The fleet is now **18 lanes**.

**Wall attached and showing the lanes.** The wall session `ufo_sighting` (client
attached at `/dev/pts/5`) now carries a `shokunin` window with three panes,
registered as missions `shk-fleet-lanes`, `shk-fleet-driver`, `shk-fleet-health`:

| pane | shows | source |
|---|---|---|
| `shokunin · lanes` | per-lane round, running/idle, last output line | `.ufo/lane-watch.sh` (read-only) |
| `shokunin · driver log` | `launch` / `complete` / `tick=` stream | `tail -f .ufo/watchdog.log` |
| `shokunin · mori census` | fleet-health census, refreshed every 60s | `mori-shokunin/tools/mori-census.sh` |

Layout set to an even vertical stack (83x26 / 83x14 / 83x19) so the 18-row lane
table reads without wrapping.

## 2026-10-15 — round 10 aggregator relaunch: corpus-selection motivation

- Steered round is **10**, notwithstanding later-numbered historical entries.
  Existing report-marker bytes and all historical records remain untouched;
  this run appends its own dated evidence rather than relabeling history.
- Latest aggregator scores are tied at **9** (`SCORECARD.md:301-305`).
  Selected **corpus review**: the inherited actual gate measurement at
  `b598ce0e1d4fa8851d3e238ee6afde42bd57f787` represents **6 / 19**
  local direct child lanes and omits **13**. This L1 re-counted its metadata:
  command and observed output are in
  `.ufo/waves/aggregator-r10-resume/before.json`; original input is
  `.ufo/waves/aggregator-r10/before.json`.
- One native OMP batched craft dispatch launched nine named seats, including
  planner, connector, three executors, scribe, scout, reviewer and critic;
  receipt `.ufo/waves/aggregator-r10-resume/dispatch.json`.
  Taxonomy roles use the unchanged host table; this is not a generic UFO
  proposal wave, whose taxonomy excludes the required planner.
- Bounded move: replace the implicit fixed corpus list with local physical
  child discovery, retaining explicit selection and grading semantics.
  Numeric corpus score remains 9 unless stronger evidence warrants otherwise;
  full semantic conformance and an atomic live-tree snapshot are not claimed.
- The concurrent operator custody update above is respected: audio,
  game-dev-2d and game-dev-3d remain read-only, even though default local
  discovery must represent them. Their metadata verdicts belong in the fleet
  ledger; corpus lessons for the other children remain in aggregator scope.

## 2026-10-15 — round 14 protocol relaunch: registry-home cutover

- **Motivation / selected axis.** Protocol-soundness was the lower protocol
  axis (8 versus gate-integrity 9). `SCORECARD.md` queued the impossible
  main-repo registry home: both Registry and Delivery required a root
  `SKILL.md` that does not exist. Fresh baseline command/output/revision:
  `.ufo/waves/round-14/registry-home-rerun/before.json`, measured at
  `99efc52b3a6f3648f7d8e097d78460901ad3c91c`.
- **One move.** Define the registry home once in `PROTOCOL.md` Registry:
  child lanes retain their own `SKILL.md`; protocol and aggregator use their
  own explicitly lane-owned root `SCORECARD.md` registry sections. Delivery
  uses that definition. Append the `Registry home` incident to the required
  `PROTOCOL-APPENDIX.md`; register only the existing protocol closure gate.
  No new executable, copied expected values or root skill is introduced.
- **Batch / ownership.** One native task call dispatched the nine required
  role seats through the unchanged host table; receipt:
  `.ufo/waves/round-14/registry-home-rerun/dispatch.json`. All workers are
  author-lane workers, not promotion verifiers. The inherited
  `registry-home/` evidence is preserved and not counted as this dispatch.
- **Clean cutover.** Remove the obsolete G16/G26 source-wording predicates
  and universal-SKILL/old-Delivery anchors from the round-13 preservation
  inputs; do not re-pin wording tests. Historical gate implementation,
  fixture/frozen expectations, history pin and ledger remain unchanged.
  Parent integration rationale:
  `.ufo/waves/round-14/registry-home-rerun/integration.md`.
- **Evidence ceiling / routing.** The inherited live closure invocation
  crashed on historical `MANIFEST.json rounds[138].round:null`, with empty
  stdout and no emitted verdict; it was not rerun. No closure statuses are
  writable from that failure. Owner: protocol, next bounded gate-integrity
  repair. Existing selftests compare aggregate counts, not stable finding
  identities; full gate conformance is not asserted. Sources:
  `.ufo/waves/round-14/registry-home/live-closure.json` and
  `registry-home-rerun/critic.md` under the same round-14 wave directory.
- **Verification ordering.** This entry ships with the implementation.
  The following verification entry records actual CLI runs and after-count
  against that committed revision; no unrun result is claimed here. The
  filed report marker remains untouched until work is committed, then gets
  an appended erratum. Sibling LOG/SCORECARD bytes and runtime stay outside
  this lane's commit; see the integration record for shared-file isolation.


## Operator directive 2026-10-16 (fleet routing)

Standing model-route directive from the operator, effective immediately and
for future swarm rounds in this fleet: (1) stop using deepseek-v4.1-flash as
the default swarm seat — the default flash lane for all future AgentSwarm
dispatches is the zai bucket: `cascade/glm-5.3-flash`; (2) the capstone
pattern is kept for the next run of rounds: the 10th (final) round of the
next run dispatches on `openai-codex/gpt-6.1-sol` (max effort) with 32 seats,
as the last round. Both in-session round goals (mori r2-11, chousa r2-11)
completed under the previous routing; this directive governs what follows.

## Operator directive 2026-10-16 (routing amendment)

Amendment to the earlier same-day routing directive: the deepseek-v4.1-flash
swarm lanes are RE-ALLOWED — both cascade/deepseek-v4.1-flash and
cascade/glm-5.3-flash (zai) are permitted flash seats, and the operator will
switch between them by command per round/run (most recent switch: zai for the
kengaku r19 wave). Default until the operator says otherwise: zai bucket.
Also recorded: the kengaku 10-round run was stopped by the operator after
round 19; the instruction to chain another 10-round training is withdrawn.

## Operator directive 2026-10-16 (routing, second amendment)

The operator: "use more zai flash now; instead of the deepseek buckets."
Effective immediately: swarm seats go to the zai flash bucket
(`cascade/glm-5.3-flash`); the deepseek-v4.1-flash buckets are parked
(remain permitted but unused) until the operator switches again. No active
training run at this record; the directive binds the next dispatch.

## Operator directive 2026-10-16 (routing, third amendment)

The operator: "stop with the zai subagent fleet, go back to the deepseek."
Effective immediately: swarm seats return to the deepseek flash bucket
(`cascade/deepseek-v4.1-flash`); the zai bucket is parked (permitted, unused)
until the next operator switch. This amends the second amendment; the
capstone rule (10th round of a run on `openai-codex/gpt-6.1-sol` max, 32
seats) is unaffected.

## 2026-10-16 — operator amendment rollout: SCORECARD contract fields absorbed fleet-wide

Follow-up to the 15:55 operator amendment (commit `84bade0`, itself committed and
pushed): review found the amendment updated every dispatch surface (round prompt,
watchdog `lane_prompt`, 13 seat cards, README, MISSION/PROTOCOL/AXES/APPENDIX/
LEARNING) but no SCORECARD.md implemented the new contract — the commit message's
"SCORECARD.md gains a capabilities repertoire table + stagnation nudge" was text-only.
Rollout, committed as conformance changes (no axis claims advanced, no scores moved):
- fleet-root `SCORECARD.md`: added `## Capabilities` (empty repertoire table; rows
  enter only via demonstrated rounds) and `## Saturation` (line + stagnation window N
  left for the protocol lane to declare on its next round — declaring values here would
  be pre-claiming). `## Planned` / `## Retired` already existed and are unchanged.
- every lane repo's `SCORECARD.md`: same additive scaffold for whichever of the five
  contract fields (`AXES.md` §SCORECARD.md contract) were missing; lane LOG.md entries
  record per-lane what existed and what was added.
- `templates/round-prompt.md`: the stagnation-nudge pointer now cites `AXES.md`
  §The stagnation nudge (it named §Capabilities, where the nudge does not live).
- skill mirror (`~/Projects/myskills/shokunin/SKILL.md`): same pointer fix.

## 2026-10-19 — correction: root ledgers restored after the 31baf5c clobber (protocol round 16)

- **Incident.** Commit `31baf5c` (author kotodama-shokunin, 2026-10-19 17:03,
  "fleet backlog commit: rounds 33-42 .ufo/kotodama reports + LOG/SCORECARD/l0-questions
  bookkeeping catch-up (uncommitted artifact sweep)") replaced this repo's root
  `SCORECARD.md` and `LOG.md` wholesale with another lane's ledger bytes.
- **Evidence.** Both 31baf5c blobs are byte-identical to `kotoba-shokunin` commit
  `b7470d7` ("round 36", 2026-10-19 07:36): `SCORECARD.md` blob `3fc970db…`,
  `LOG.md` blob `99de619d…`. Numstat `12f2da5..31baf5c`: SCORECARD 165+/395-,
  LOG 1356+/845-. Headers flipped from the fleet titles (`# shokunin (main repo) —
  Scorecard` / `# shokunin (main repo) — Iteration log`) to the kotoba titles
  (`# kotoba-shokunin — Scorecard` / `# kotoba-shokunin — Iteration Log`).
- **Prior warning.** `ab707d9` (kotoba r42 breather, MANIFEST note, 2026-10-19)
  recorded the uncommitted overwrite of the fleet-root ledgers — mtime ~07:35,
  matching the b7470d7 capture — before it was swept into the backlog commit.
- **Restore source.** Restored to `12f2da5` blobs `37b5ffae…` (SCORECARD) and
  `faaf3bb8…` (LOG) — byte-identical to `0b1ac3b`, the last real edit of both files.
- **Carry-forward.** Zero. `.ufo/waves/round-16/clobber/classify.sh` (re-runnable,
  read-only; stdout at `classify.out` beside it) classifies all 41 hunks
  (40 SCORECARD + 1 LOG) `kotoba-bytes`: every one of the 165+1356 added lines is
  present verbatim in kotoba `b7470d7`, so no genuine fleet entry inside the
  clobber needed appending. 5 fleet `## ` SCORECARD headings and 26 LOG headings
  were absent verbatim at 31baf5c and are restored with the files.
- **Round-14 evidence restore.** `.ufo/waves/round-14/registry-home-rerun/`
  (12 files: contract, dispatch, before.json, planner/scout/critic/scribe notes,
  decision, integration, provenance, closure-scope, context) deleted by `e20f4fa`
  was restored from `b2f2efa`; it is cited by PROTOCOL-APPENDIX.md "Registry home",
  the round-14 LOG entry, and this scorecard's registry section.
- **Append-only honored.** The superseded text is the whole 31baf5c version of both
  files; the clobber itself was the rewrite, and this entry is the correction —
  earlier bytes are untouched.

## Round 16 — protocol lane — gate integrity (root-ledger restore + gate) + protocol soundness (the corpus loop enters the contract)

- **Claims.** (1) gate-integrity: restore the root ledgers after the `31baf5c`
  clobber (correction entry above) and make the clobber class a committed gate;
  (2) protocol-soundness (lowest axis, 8): the continuous loop builds the
  corpus every round. Steered round 16 (orchestrator steer table,
  `.ufo/waves/kaika/steer.md` on branch `kaika/ledger`); no report at
  `.ufo/reports/round-16/protocol.md` existed at `31baf5c` or in the fleet root.
- **Gate.** `.ufo/gates/root-ledgers.py` + pinned values
  `.ufo/gates/root-ledgers/expected.json` + 9 fixtures; exit map 0/1/2/64.
  Live clean after the restore; `--rev 31baf5c` → exit 1 (`scorecard_header_lost`,
  `log_header_lost`, `protocol_registry_lost`, `aggregator_section_lost`);
  `--rev 12f2da5` → 0; `--frozen` replays both, digest-pinned (tamper → 2);
  selftest 9/9; `.ufo/waves/round-16/gate/mutate.sh` kills 9/9. Registered in
  this repo's `SCORECARD.md` protocol registry. Runs: `.ufo/waves/round-16/gate/runs.md`.
- **Protocol text.** `PROTOCOL.md`: file-contract row `corpus/SOURCES.md`
  (points at `CORPUS.md` §"SOURCES.md — where a shokunin learns", contract v1;
  main-repo lanes hold no `corpus/`); round-contract **frontier step** (curate
  SOURCES, census before→after, mine one mistake or paste the sweep, ≥1 sourced
  claim — part of the round, never a claim of its own); report minimum content
  **Sources & frontier** (conformance only, never a `report_of()`/marker
  predicate); Invariants: root ledgers are fleet files, `root-ledgers` is the
  check. `PROTOCOL-APPENDIX.md`: 4 rows (Corpus sources, Frontier step,
  Sources & frontier, Root ledger identity). Essence untouched: per-axis
  verdicts, 1–3 claims, non-author verification, append-only, provenance.
- **Measurements.** `SCORECARD.md` G1–G7, P8–P11; before-values at `31baf5c`
  in `.ufo/waves/round-16/before.md`. Both scores held (9, 8): the restore
  recovers a recorded 9 rather than raising it, and the round-13 verifier is red
  on the same 3 inherited checks before and after, so a 9 for soundness would
  not be re-derivable.
- **Swarm.** One batched call, 9 seats (planner, connector, 3 executors,
  scribe, scout, reviewer, critic); two seats died on provider limits (critic at
  start, revived; gate executor mid-run, and its fresh re-dispatch at start) —
  the gate's last repairs were landed by L1 and are named in `runs.md`.
  Receipt: `.ufo/waves/round-16/dispatch.md`.
- **Next.** `SCORECARD.md` §Planned: round 17 makes the soundness verifier
  clean at a named commit; gate `LOG.md` append-only; closure-gate live crash.

## Aggregator round 12 — corpus-review coverage across 21 physical lanes

**Claim (one):** the standing per-repository review surface expands from the seven current verdicts recorded at the R11 final re-run to all 21 physical local lane repositories, each at a refreshed full commit, with a reusable SOURCES reading/curation index. The claim is revision-bound coverage, not a semantic conformance or source-quality claim.

- Current state: all 21 exact-HEAD R12 runs are **not conformant**; each reports the aggregator-owned missing `round-12-aggregator` lesson under r10. Other literal rule findings, exact full OIDs, command modes, and output lines are in `.ufo/reports/round-12/aggregator.md` and `.ufo/waves/kaika-aggregate/r12-gate-final.md`. Twenty used `corpus-gate.mjs --snapshot <original-path> <full-OID> --round 12`. Audio's 1,391,738,880-byte archive exceeded the existing snapshot wrapper's 1 GiB buffer; it was streamed and graded through the same gate's `--repo` interface against an exact temporary index/worktree, with original HEAD unchanged.
- SOURCES census: the corrected `scripts/sources-census.sh` at blob `3f314620b2395eeb70d8405410132027dfe608e4` ran `census`, `validate`, `shared`, and `overdue --today 2026-10-20` on 21 full-commit archives. Counts: **576** rows (tiers A/B/C=500/33/43; statuses mined/queued/rejected=307/220/49), no invalid/missing rows; validate 21 ok, 0 E codes, 7 W codes; 2 shared URL groups; 0 overdue among 557 cadence rows. Exact commands, pins, lane counts, warnings, and limits are in `.ufo/waves/kaika-aggregate/sources-census-final.md`.
- Curation index: `.ufo/reports/round-12/SOURCES.md` points into each lane's own `## Paths`, `## Search log`, and unopened `## Leads`, then selects a few transferable lane and W1 routes. It separates knowledge-expansion candidates from capability/navigation references. No lane source fact was copied or presented as independently verified, no unopened lead was treated as evidence, and no knowledge entry was created.
- Swarm: one batch of 32 read-only L2 seats (21 lane audits plus planner, connector, critic, source-curation, freshness, registry/README, adversarial source, index, history, count-reconciliation, and schema/provenance seats); task/evidence map `.ufo/waves/kaika-aggregate/dispatch.md`, unique notes `.ufo/waves/kaika-aggregate/seats/`. The seats are same-lane evidence, not an independent non-author verdict on aggregator taste.

**Axes:** corpus review stays **9**; cross-lane quality and mint/dormancy stay **9**. The R11 final re-run made the current three scores a tie; corpus review was selected for the unpaid per-repository duty. The older pre-rerun plan naming cross-lane quality at 8 is preserved as history and superseded by that later score state. No scalar aggregate score, new mint, dormancy label, or promotion is claimed.

**Trends:** expansion **unchanged** (no knowledge admission); quality **unchanged** (no semantic source/corpus revalidation or knowledge edit); discernment **unchanged** (the 32 seats belong to this aggregator lane, so they are not independent non-author verification).

**Mistakes and dissent:** the initial seat prompt confused the child's latest LOG round with the gate's aggregator-lesson `--round`; the critic caught it and all final calls use `--round 12`. The original census parser missed 1–3-space-indented Markdown rows; the parent integrated the corrected parser and reports 93 killed / 0 survivors plus the 96-check receipt. Two basename-only README edits resolved against the original fleet checkout rather than this worktree; the parent preserved the draft, restored the original, and transferred the corrected copy into the owned worktree (`.ufo/waves/kaika-w3/readme-ownership.md`, `readme-recovery.md`). The referenced `aggregator-r10-resume/before.json` was absent; the baseline is the R11 seven-verdict record, not a fabricated rerun. Critic and source-adversarial dissent is retained: structural row/path checks do not prove source opening, ID citation, anchor support, or `teaches` truth.

**Open evidence debt:** do not widen canonical enums to make legacy history pass. D5 runtime evidence validated the selected new closure shapes and all 45 `supersedes.entry` records, while the whole legacy ledger was 206/312 schema-valid; 106 historical rows retain legacy `type`, closed-status, or missing-field vocabulary. The current fleet HEAD's schema-provenance comparison is separately recorded in the round-12 report; the 45 protocol-valid entries are schema lag, not part of the 106 legacy rows. `MANIFEST.json`, schema enums, child corpora, and the 13-entry roster were not changed. The physical population remains 21 repositories, not 21 roster members.

### Round 12 — pre-publication provenance correction (integrator)

The governing canonical schema is `e737d2ea`, not the old `5eae1063` seat input.
At fleet cutoff `54a20d39`, the actual validator finds 214/320 valid entries and
106 distinct legacy-invalid rows; protocol-valid `supersedes.entry` is supported.
The preceding schema-lag wording is superseded, not a current release defect.
The indentation receipt has 93 checks; `canonical-final-checks.txt` has the final
96. These corrections change no corpus verdict, source total, score or claim.

## 2026-10-21 — operator maintenance: executable malformed-round closure handling

- The registered protocol checker `.ufo/waves/round-15/closure-check.py` previously
  had a documented live None/int ordering crash. The old live failure was accepted,
  not re-run merely to confirm it. One isolated executor worked at
  `/fast/scratch/hyaku/root-closure-null-round` on observed base
  `e82b86b8c02fdbb6282c1c459c032f43d16af9f8`; a separate reviewer advises Main.
- Current source SHA256:
  `c00fcbd079a1e8902f8bb480ce7b18387c93c15fbde3c8187966ce51d03ba118`.
  Invalid adjudicated round identity becomes typed `unknown_round`/unadjudicable evidence;
  it is never re-keyed from annotations, coerced to zero or treated as a clean status.
  A mixed malformed/integer fixture preserves a real valid status row and explicit CNE.
- Main integrated the exact source and seven byte-matched new fixture inputs, then actually
  ran selftest28/28, five original frozen replays (expected exits1,0,1,1,0), the public
  malformed-fixture CLI (exit2, typed finding, valid kagi1ok) and live CLI (exit1, JSON emitted,
  no traceback). Complete observed commands/results:
  `.ufo/waves/hyaku/native-checker-repair/parent-runs.json`.
- Live remains red:67debt,57contradictions,81CNE and zero history-pin findings at that
  observation. Existing closed-status, missing-report, keying and unknown-type debts were
  not normalized; old frozen inputs/expectations and canonical entry.round identity remain.
  Registration now lists the new CNE class and current28-case control; historical27/27
  measurements are not rewritten or re-pinned.
- Process deviation: the worker ran tests/probes despite the requested mid-flight skip.
  Its observations are not relabeled as Main's runs or claimed as full instruction compliance.
  This maintenance is not an invented protocol training round, global-clean ledger,
  child-claim admission, promotion or permission to retry any policy-held work.

## 2026-10-21 — closure-maintenance v2: hashable diagnostics without identity bypass

- The preceding v1 source/tally/run record is historical, not the current source.
  Main's full-path list/dict probes exposed unhashable diagnostic keys despite v1's
  successful live/null controls. The original isolated executor refined that same slice;
  a separate read-only reviewer closed S1/S3 and withdrew its proposed S2 exemption.
- Main integrated the bounded v2 delta, preserving existing return-mapping line wrapping
  rather than the worker's unrelated reflow. Final source SHA256 is
  `d8c1620df147d2e576f157f43e149ae4a1251a760b9f111f210b516744187a48`;
  the private worker source was `795974f2238ed95c8c0c721627f40d188253568f6d1add05c91c23a8fa980b6b`.
  One type-tagged hashable projection now serves diagnostic/legacy keys and lookups.
  Authoritative status rows still require integer `entry.round`; annotations never
  re-key a row, coerce null to zero or exempt an actual unrowed dispatch.
- The typed `unknown_round` finding is emitted before independent missing/unusable
  `lanes` exits. Main installed seven exact byte-pinned `malformed-round-shapes` inputs;
  the earlier null/mixed-round fixture and historical frozen expectations remain unchanged.
- Main actually exercised the final integrated public CLI: selftest29/29; five original
  frozen modes at expected exits1,0,1,1,0; original null fixture at exit2; new list/dict/
  missing-lanes fixture at exit1; live CLI at exit1. All nine commands emitted JSON without
  stderr/traceback. The new fixture reports three typed CNEs, one independent contradiction
  and one retained real kagi1ok row; live remains67debt/81CNE, not globally clean.
  Commands, full results and exact input hashes:
  `.ufo/waves/hyaku/native-checker-repair/v2-parent-runs.json`.
- The executor again ran mid-flight tests/gates despite explicit repeated prohibitions,
  acknowledged the deviation and froze its tree. Those runs are not Main's evidence.
  Historical27/27, interim28/28 and old mutation scores are not re-pinned; fresh current-
  source mutation controls remain a separate qualification item, not an invented gate.
  No training/admission/promotion credit or policy-hold clearance follows from this repair.

## 2026-10-21 — current-source mutation qualification and distinct freeze blocker

- Main prepared nine bounded mutation copies from the actual committed checker source
  `d8c1620df147d2e576f157f43e149ae4a1251a760b9f111f210b516744187a48`,
  then ran the pristine copy (29/29) before running each mutant's native selftest.
  Eight produce named consumer-visible fixture failures; M7's old prompt grammar raises
  TypeError in the shipped prompt-key unit and is **crash-only**, not a behavioral kill.
  There are zero survivors/construction refusals; old oracles and scores were not re-pinned.
- M8 suppresses typed round findings while leaving rows held out; both new fixtures fail.
  M9's actual null-to-zero read creates a phantom round0 row in the original null fixture;
  it does not coerce lists/dicts, so the shape fixture retains two CNEs rather than three.
  This corrects the preparer's prediction, not the unchanged consumer expectations.
  Exact edits/hashes and all parent-run outputs:
  `.ufo/waves/hyaku/native-checker-repair/mutation-{construction,control-run,parent-runs}.json`.
  The private preparation helper is a control scaffold, not another shipped gate.
- A new pre-closure snapshot exposed a separate default-generator projection defect.
  `freeze-snapshot.py` generated an unreviewed328-debt expectation from a materialized
  Gitless **live** mirror; the native **frozen** replay produces65debt/81CNE and MISMATCH.
  The exact difference is262phantom `prompt_untracked` plus one live history-pin finding;
  all65substantive triples and the exit agree. The live67-debt observation is a different
  input projection and is not equated to either snapshot result.
- Both failed fresh artifacts remain intact and explicitly unqualified:
  `native-checker-repair/pre-closure-{freeze,replay}.json` and the referenced new snapshot.
  No protected historical baseline was regenerated or overwritten to make this green.
  The existing generator correction is separately scoped to derive through the native
  frozen CLI and bind its input digests; Main must exercise/review it before further
  frozen-accounting claims. This is not a new trained round or child admission.

## 2026-10-21 — native frozen derivation cutover exercised

- The existing round-15 generator now invokes the same native frozen path used by replay,
  not the obsolete Gitless live mirror. Main's source SHA256:
  `7cc7b2f88a5a273e1d3c7cbe32380ade2fae03d8f773c04aeb2f7e8838596cdd`.
  Private reviewed v2 was `8d1fce4c6b80aaef0885d44ca3f2b7af5715d2d3a7f570fb30101fb36a9d2670`;
  Main corrected comments about analysis-before-comparison and preserved separators.
  The checker stays at `d8c1620d…`; no new gate, shim or historical oracle was introduced.
- Missing/incomplete native analysis is refused, not defaulted to empty debt/CNE and a
  false clean zero. Derivation distinguishes CLI3/no-baseline from the analyzed exit.
  Explicitly regenerated output clears stale producer-owned expectations/notes; only the
  six produced input files are pinned. Unrelated output leftovers are not inputs.
- Main actually ran generator38/38, including the independent flat-fixture derive/replay
  regression. Fresh default output contains65debt/81CNE, not263phantom live-only findings;
  its native replay matches the baseline and all six input hashes at exit1.
- Actual `--force` and explicit manual expected-value CLI paths both regenerate/replay at
  exit1/debt65 with six matching input hashes. Force removes the planted obsolete live
  note while leaving an unrelated leftover unpinned. A throwaway incomplete checker
  returns an incomplete JSON result; generation refuses at exit3 and leaves no fabricated
  expectation. The temporary checker and leftover were removed after observation.
- Main re-ran current checker29/29 and the five original frozen comparisons: expected
  exits1,0,1,1,0 and all `match`. Protected inputs/expectations and the original failed
  fresh328-debt snapshot remain unchanged. Commands/results:
  `.ufo/waves/hyaku/native-checker-repair/freeze-v2-{parent-initial,default-replay,parent-edges,native-controls}.json`.
- A stale expectation's tamper path already retained full analysis; no observed
  force-path false-zero is claimed. The corrected defects are projection mismatch,
  incomplete-result fallback, contradictory notes and unrelated input pinning.
  Derived output remains explicitly unreviewed/self-pinning. Frozen matching does not
  authenticate child measurements, imply a clean ledger or clear any source/policy hold.

## 2026-10-22 — Kaidoku25 ruler prerequisite landed before claims

- Main integrated only the four independently reviewed prerequisite paths and the
  serialized lane helper pushed `62feef9c0cbd5aadafa453456c55c28832175206`.
  Ruler SHA256 is `20fe3f3d3d68ba21c8d8bbfed175bb57db46a8618bd179b179acb6fda99d0532`;
  the three fixed oracle/contract/derivation digests stayed unchanged. The optional
  false-red preservation draft remains private and unlanded; no no-harm duty was waived.
- Main exercised the actual committed CLI against BASE `18e7eb6…`: exit2,
  `candidate_unavailable`, 34not_observed, executed0, exact0. These are not 34
  experimentally observed old failures. A separate wrong-digest invocation returned
  exit2 / `snapshot_tampered:oracle`, with no fabricated comparable result.
- No candidate, claim freeze, implementation approval, admission or score increase.
  QUALITY33's literal subject/instrument cyclic debt remains UNMET; the unchanged R24
  detector does not discover the proposed reports path, so its status is UNDETECTED,
  never a round-level CLEAN. R24's original9/11 and all safety holds remain intact.
- Exact commands, streams, exits and limits:
  `.ufo/waves/hyaku/kaidoku25-prerequisite/parent-{before-process,tamper-process,proof}.json`.
  Root-state guards attest named instants only, not continuous enforcement or a
  full no-harm certificate. No audited instrument, fixture or held item was executed.

