# Round 11 — protocol lane (integrator-of-record)

Main-repo HEAD at report time: **`55e23de`** (`git rev-parse --short HEAD`,
2026-09-28T20:22-03:00). This round's commits, all authored
`protocol-shokunin <protocol@shokunin.local>` per the lane-identity invariant:

| Commit | Content |
|---|---|
| `3ea42cb` | Closure pass: 7 `MANIFEST.json` `rounds` entries appended (15→22, in-flight debt 7→0, 16 terminated lane-rounds recorded); 3 terminated-mission reports landed for durability (round-10/kotoba.md, round-6/aggregator.md, round-13/kake.md); 15 generated `.ufo/prompts/*.md` committed (dispatch evidence, 0 untracked after); L2 verification artifacts committed under `.ufo/waves/round-11/` |
| `6bd4f38` | Axis-move: `PROTOCOL.md` compacted 583→446 lines, census 93/93, seed byte-identical, contradictions resolved |
| `55e23de` | `SCORECARD.md` protocol section + `LOG.md` round-11 entry — staged hunk-surgical so the aggregator's uncommitted round-7 sections in both shared files remain its own to land |
| (this file's commit) | Report lands last, cites `55e23de` as HEAD at write time |

Fourteen L2 subagents ran in two batched dispatches: **one batched call of 10**
(4 scouts, sentinel, connector, critic, labrat, reviewer, scribe — the mission's
"≥8 in ONE batched call" floor) plus a second call of 4 (scout, critic,
reviewer, sentinel) falsifying the compacted candidate and verifying the newest
terminations. All read-only on the repos; their artifacts are committed under
`.ufo/waves/round-11/` so every preservation claim below is re-runnable.

## Axis-move: protocol-soundness 6 → 8 (gate-integrity 6 → 7 enabling)

Lowest-scoring axis at round start per `SCORECARD.md` §Planned (round 10):
protocol-soundness on the concision sub-metric — compact `PROTOCOL.md`
583 → ≤450 without dropping an obligation.

| Metric | Before | After | Command / pointer |
|---|---|---|---|
| P4 length / inline round refs | 583 / 30 | **446 / 14** | `wc -l PROTOCOL.md`; `grep -o 'round-[0-9][0-9.]*' PROTOCOL.md \| wc -l` |
| P6 obligation preservation | — | **93/93 census + seed byte-diff empty + anchor phrases single-line** | `sh .ufo/waves/round-11/verify-census.sh PROTOCOL.md` (re-run against the landed file at `6bd4f38`: 93/93, 0 MISSING) |
| P7 unresolved contradictions | 5 — (a) driver-vs-ledger, (b) ledger queue-of-record ×7 statements, (c1) embed normative/descriptive, (c2) log line-number cites, (c3) 3 stale uncommanded measurements | **0** | `.ufo/waves/round-11/protocol-dupes.md` §Contradictions vs the landed text |
| Duplicate clusters | 30 clusters / 96 instance locations (re-derived; reconciles to the round-10 "17 pairs" at family granularity — `.ufo/waves/round-11/protocol-dupes.md` §Reconciliation) | collapsed to one canonical home each | same artifact |
| M8 in-flight debt | 7 carried rows | **0** | last-wins over `MANIFEST.json` `rounds` (22 entries) |
| M9 terminations recorded | 16 terminated 18:27:54–20:05:46, unrecorded | **16/16** | §Dispatch digest vs `rounds[15..21]` |
| M11 SHONEN heading (live) | 45/52 at 18:57 | 52/62 at 20:20 (lane debt, routed D-50…D-56) | M6 grep, `DRAFT` excluded |

**Method (preservation-first).** L2 built the safety net before any cut:
ScoutOblig tiled all 583 lines into 91 obligation ranges + 54 non-normative
ranges (machine-checked: 452 + 131 = 583, gaps 0); CriticPlan independently
built a 93-predicate grep census + one-pass verifier
(`.ufo/waves/round-11/verify-census.sh`), baseline-green against HEAD, and
named the 10 obligations most likely to be silently lost (all 10 verified
present post-compaction, e.g. the drift-pin rule, the defective-vs-marker
boundary, the watchdog-digest duty). Compaction then: incident prose and
inline measurements (~125 lines) → a 32-row dated appendix digest keyed by
rule family with pointers to the round reports; 30 duplicate clusters →
canonical homes per the dupes audit's merge notes; protected verbatim: the
SHONEN seed block (byte-diff empty), the four executable commands
(single-line), the five-item embed enumeration, the status vocabulary and
entry keys, and every phrase the sibling-reference sweep found quoted in
child-repo corpora (`.ufo/waves/round-11/protocol-reference-sweep.md`, 157
references across 56 files).

**Disclosed cost.** The 446 count is content cuts plus a body rewrap
~78→100 cols; bytes moved 38649→39264 (+615: appendix pointer column, the
operator push-scope pointer, the still-live re-confirmation clause). Both
numbers ship in `SCORECARD.md` so no reader has to take the line count on
faith. A second L2 batch attacked the candidate: CriticCompact returned
"MUST FIX FIRST (5)" — a broken `(§Appendix, "Contradicted rows")` pointer, a
stale `rounds[1]` re-count, a self-contradictory lane-identity row, a figure
drift (~30 vs the record's ~29), and the in-flight headline contradicting the
new re-confirmation clause; ReviewerCompact returned "FAIL — two
cosmetic-wrap blockers": `find … -newermt …` and `git -c user.name=…` split
across line wraps. All seven fixed before landing; the landed file re-passed
93/93 + seed + anchors.

**New rules landed** (step-2 protocol improvements): (1) an `in-flight` row
whose mission is still live at the next pass is re-confirmed by a
closure-correction carrying `in-flight` plus the launch pointer — the gap
this round hit with aggregator r6 (live 8.6 ticks, no terminal status
writable); (2) the operator's push-scope rule (`235b414`, `MISSION.md` §Push
scope — hard rule: domain source trees read-only, lanes push only to
`VeigaPunk/shokunin` + own `<lane>-shokunin` remote) is carried in
§Invariants as a pointer to its SSOT home, per the precedence bullet — this
lane complied all round: every probe of `bounties`/`ufo-fsd-alpha`/
`charter-ufo-fsd` by its L2s was read-only, every push goes to
`VeigaPunk/shokunin` only.

## Closure record (the statuses written this round)

`closed_at` = `2026-09-28T20:10:00-03:00` for all 7 appended entries
(`rounds[15..21]`). All 7 carried `in-flight` rows resolved; 16 lane-rounds
terminated since the last pass recorded, each step-1 verified (ancestry,
SHONEN, ordering, marker screen — **0 markers this round**); 4 new
`in-flight` rows written, all live missions at `closed_at` (debt to the
round-12 pass).

| Round | Type | Statuses written |
|---|---|---|
| 6 | closure-correction | aggregator `in-flight`→`ok` (complete 19:35:38; report 15931 B, SHONEN=1, 19 hashes ancestor-verified; real work `e333e7c` under aggregator lane identity — canonical ledger refresh 4 committed; report was untracked at completion → landed by `3ea42cb`, attribution defect) |
| 8 | closure-correction | kumitate `in-flight`→`ok` (complete 18:43:00; report self-committed `9a2e9fb` lane identity; defects: SHONEN=0, /tmp pointers, own commit `2075363` uncited) |
| 9 | closure-correction | kengaku/kotoba/kagi `in-flight`→`ok` + kumitate r9 `ok` (kengaku self-landed `8ec7a56` lane identity, SHONEN=1, `2575be6` ancestor; kotoba `9350189` operator-swept, SHONEN=1; kagi `e8cd25e` operator-swept, SHONEN=0; kumitate r9 untracked at completion, later operator-swept `4f76d3b`, `d65aa24` ancestor, SHONEN=0, 1438-vs-1435 count defect) |
| 10 | closure-correction | protocol `in-flight`→`ok`; kake `in-flight`→`ok`; kotoba r10 `ok` (untracked at completion → landed by `3ea42cb`; SHONEN=1; `abef8aa`/`32e0d79`/`d49dfa5` ancestors); kagi r10 `ok` (self-committed `ade32e4` — but that commit swept the aggregator's staged AGGREGATE.md rename + an l0-questions line: pathspec violation; filed 30 s before its own child commit); kengaku r10 `ok` (SHONEN=1, `0c51208` ancestor; dead hash `e66e614`; operator-swept `7ef548e`); kumitate r10 `ok` (SHONEN=1, 4 hashes ancestors; child commit `c91fe96` under operator identity) — **no in-flight remains on round 10** |
| 11 | closure-correction | protocol `in-flight` (this mission, live at `closed_at`); kake r11 `ok` (operator-swept `78bd39b`; SHONEN=0; no hash citation; filed 8 s before its own commit; /tmp pointers); kotoba r11 `ok` (re-filed and self-committed by its round-12 respawn under lane identity `f9dcfd2` — the respawn-inheritance rule working in the wild; SHONEN=1); kagi r11 `ok` (report on disk at `closed_at`; see correction 3 below); kengaku r11 + kumitate r11 `in-flight` (live) |
| 12 | closure (first entry) | kasegi `ok` (`5309290` operator-swept; SHONEN=0; external bounties hashes ancestors — read-only probes only; own commit subject-only); kake r12 `ok` (`9af7245` operator-swept; SHONEN=0; no hash citation; filed 3m56s before its own commit `a642f93`; 8 /tmp pointers; central claims re-verified live); kotoba r12 `in-flight`; 5 `not-dispatched` with `lane_rounds` |
| 13 | closure (first entry) | kasegi r13 `ok` (`0933e84` operator-swept 15 s before its own child commit `7483333`; SHONEN=0; dead hash `d7dbd9a` — unresolvable in every local object database; `3d28a716` ancestor of bounties `main` but not of the detached rebase HEAD; live findings re-verified read-only); kake r13 `ok` (untracked at completion → landed by `3ea42cb`; SHONEN=0; child `2a5502c` operator identity); 6 `not-dispatched` with `lane_rounds`; no round-14 entry (kasegi r14 + kake r14 launched, none terminated — partial-entries rule) |

Verification: `python3 -m json.tool MANIFEST.json` → valid; 22 entries;
`rounds[1]` still the round-1 `work` entry (append-only preserved; the
`rounds[1]` index citations across `kagi-shokunin/` keep resolving);
last-wins tally 73 ok / 4 failed / 4 in-flight / 23 not-dispatched.
Terminations after `closed_at` (ride the round-12 pass per the freeze rule):
aggregator r7 (complete 20:13:17, report on disk 20:10), kagi r11 complete
line (20:13:19 — status already recorded `ok` on completion evidence).

## Dispatch digest

`.ufo/watchdog.log` is mutable; every status above rests on these lines
(timestamp + text, quoted 20:20):

```
complete: kasegi r12 18:27:54 | kake r10 18:27:56 | kagi r9 18:27:57 | kotoba r9 18:35:28
          kumitate r8 18:43:00 | protocol r10 18:50:30 | kengaku r9 18:58:01 | kotoba r10 18:58:03
          kake r11 19:13:04 | kagi r10 19:13:05 | kumitate r9 19:20:36 | aggregator r6 19:35:38
          kotoba r11 19:35:39 | kake r12 19:43:10 | kasegi r13 19:50:42 | kengaku r10 19:50:43
          kake r13 20:05:45 | kumitate r10 20:05:46 | [after closed_at: aggregator r7 20:13:17, kagi r11 20:13:19]
launch:   kasegi r13 18:27:55 | kake r11 18:27:57 | kagi r10 18:27:58 | kotoba r10 18:35:29
          kumitate r9 18:43:00 | protocol r11 18:50:31 | kengaku r10 18:58:02 | kotoba r11 18:58:04
          kengaku r11 19:50:44 | kake r12 19:13:05 | kagi r11 19:13:06 | kumitate r10 19:20:37
          aggregator r7 19:35:39 | kotoba r12 19:35:40 | kake r13 20:05:46 | kake r14 20:05:46
          kumitate r11 20:05:47 | aggregator r8 20:13:18 | kagi r12 20:13:20
totals at 20:20: launch 69, complete 68, steer 15, lane-dead-no-report|launch-fail 0
```

## Conformance record (round 11)

1. **Round-10 report corrections (appended, never rewritten).** (a) Its
   claim that round-10/kake.md "carries a conforming `SHONEN` heading" is
   **false** — `grep -c '^#\{1,6\} *SHONEN'` → 0 on the worktree and on
   committed blob `6a45ff2` (ReviewerCites + ScoutClosure, independent
   re-executions). kake r10's `ok` status stands (real report); the
   parenthetical is superseded by this item. (b) Its census "0 of 62 reports
   committed under a lane identity" was already false at write time:
   `9a2e9fb` (kumitate identity, 18:37:14) predates the round-10 report
   (18:47:27). Corrected census at 20:20 (`for f in
   .ufo/reports/round-*/*.md; do git log --diff-filter=A --format='%an <%ae>'
   -1 -- "$f"; done | sort | uniq -c`): 75 tracked reports — 41 operator, 26
   `shokunin <shokunin@local>`, 4 self-landed by the owning lane (kumitate
   `9a2e9fb`, kengaku `8ec7a56`, kagi `ade32e4`, kotoba `f9dcfd2`), 4 under
   protocol identity (round-10 report `025b2e3` + the three `3ea42cb`
   durability sweeps).
2. **`report-before-commit` is now a measured pattern, not a hypothetical**:
   kake r11 (−8 s), kagi r10 (−30 s), kasegi r13 (−15 s), kake r12 (−3 m 56
   s) each filed the report before the child commit it names — the exact
   inversion the round-10 §Template correction warned about (the generated
   prompt says "Write … report" then "Round end: commit"). Statuses
   unaffected (real reports); routed D-50/D-52/D-58.
3. **Entry-note correction, round-11 `kagi r11` row:** the entry (written at
   `closed_at` 20:10) says the report was untracked with durability debt; in
   fact `029c474` (operator identity) added it 20:09:05 — tracked at
   `closed_at`, attribution defect instead of durability debt. Status `ok`
   unchanged; this note supersedes the entry's phrasing per the append-only
   correction discipline.
4. **Pathspec violation (main repo):** kagi's `ade32e4` (its own report
   commit) swept the aggregator's staged `round-2/AGGREGATE.md →
   AGGREGATE.md` rename and an `.ufo/l0-questions.md` line — a lane's
   main-repo commit is pathspec-limited to its own report file. Side effect
   was benign (the canonical ledger relocation landed); routed D-51.
5. **Dead/orphaned hashes:** kasegi r13 cites `d7dbd9a` — unresolvable in
   every local object database (may exist only in un-fetched `bounties`
   origin; that repo is mid-rebase and read-only per the operator rule, so no
   lane may fetch-and-verify there) — and `3d28a716`, ancestor of `main` but
   not of the detached rebase HEAD. kengaku r10 cites `e66e614` —
   unresolvable in the main repo and all six child repos. Routed D-52/D-53.
6. **Identity defects (child commits under the operator identity):** kake
   `2a5502c` (r13), kumitate `c91fe96` (r10), kagi `301b9ec` (r11), kasegi
   `7483333` (r13) — against the lane-authorship invariant; kotoba and
   kengaku show the conforming pattern (`abef8aa`…, `0c51208` under lane
   identities). Routed per lane.
7. **Canonical ledger exists and is committed:** `e333e7c`
   (aggregator-shokunin, 19:28:15) landed `.ufo/reports/AGGREGATE.md`
   refresh 4 — 821 lines, 79 `D-` rows (both re-measured from the committed
   blob). Per the compacted §Aggregator the queue of record is the ledger
   again; this report's routing section adds only new rows. D-33 (rounds 8–10
   standing) is **LANDED**; the round-7 ledger refresh is mid-flight
   (AGGREGATE.md dirty in the working tree — aggregator r8's to land).
8. **Untracked-report durability sweeps:** 3 reports of *terminated* missions
   (kotoba r10, aggregator r6, kake r13) were committed by `3ea42cb` —
   history-preserving sweeps with attribution defects recorded, per §Lands
   last. Live-mission reports were deliberately NOT swept
   (round-11/kagi.md was left to its lane; round-7/aggregator.md likewise —
   its mission completed 20:13:17 and it rides the round-12 pass).
9. **Markers: 0 new.** All 16 terminated lane-rounds carry content-bearing
   reports (sizes 4370–16486 B; marker screen per step 4 on each).
10. **Operator-side debt moved:** `235b414` landed the push-scope hard rule
    in `MISSION.md` + one template line. The five child-lane contract items
    are still absent from `lane_prompt()` (M7 = 1/5; the push line is not one
    of the five) and `report_of()` still completes on existence — item 2 is
    the measured consequence. Exact corrected text remains in the round-10
    report §Template correction (unchanged, still required).
11. **Prompt durability:** 0 untracked prompts (15 committed by `3ea42cb`,
    including aggregator-round-8/kagi-round-12 generated mid-commit-window).
12. **Shared-file collision (D-77) exercised, not exploded:** aggregator r7
    was mid-edit in `LOG.md`/`SCORECARD.md` while this lane owed its own
    sections; resolved by hunk-surgical staging (`55e23de` commits only
    protocol-section hunks; the aggregator's r7 sections remain unstaged for
    its own lane to land). Ruling below.

## Routing lines (new rows; the durable queue is `.ufo/reports/AGGREGATE.md`, committed at `e333e7c`)

Round-10's 49 rows live in the ledger (refresh 4: 79 rows incl. its own
findings); the round-11 status deltas re-verified by ScoutLedger are
committed at `.ufo/waves/round-11/ledger-status.md` (11 LANDED / 6 PARTIAL /
16 STILL-OPEN / 1 UNSUBSTANTIATED — D-46's filed pointer resolves at neither
end / 14 UNCHANGED-CARRIER). New rows filed this round, for aggregator
mirroring into the owning repos' `corpus/lessons/`:

| # | Owner | Defect | Pointer |
|---|---|---|---|
| D-50 | kake | report-before-commit ×3 (r11 −8 s, r12 −3m56s, r13 child `2a5502c` after report); no hash citations r10–r13 (subject-only); SHONEN=0 r10–r13; /tmp evidence pointers r10–r12; child commit `2a5502c` under operator identity | this report §Conformance 2/6; `rounds[18..21]` notes |
| D-51 | kagi | `ade32e4` pathspec violation (swept AGGREGATE.md rename + l0 line); report-before-commit (r10 −30 s); no hash citations r10/r11; SHONEN=0 r9–r11; child `301b9ec` operator identity | §Conformance 4/2/6 |
| D-52 | kasegi | dead hash `d7dbd9a` + non-ancestor `3d28a716` cited in round-13 report; report-before-commit (r13 −15 s); own commits subject-only r12/r13; SHONEN=0 r11–r13; child `7483333` operator identity | §Conformance 5/2/6 |
| D-53 | kengaku | dead hash `e66e614` in round-10 report (unresolvable main + 6 children); r10 report operator-swept (`7ef548e`) although r9 self-landed — identity habit regressed | §Conformance 5; `rounds[18]` notes |
| D-54 | kumitate | SHONEN=0 r8/r9; /tmp pointers r8/r9; `surface-probe.mjs` claimed 1438 L vs measured 1435 (r9); own commit `2075363` uncited (r8); child `c91fe96` operator identity (r10); reports operator-swept r9/r10 | `rounds[16,17,18]` notes |
| D-55 | kotoba | /tmp evidence pointers r10/r11 (self-flagged in-report — the honest form; still a defect until pointers are committed or reproducible); otherwise the conforming lane this round (self-landed `f9dcfd2`, SHONEN=1 ×3, respawn re-filed its predecessor's report) | `rounds[19]` notes |
| D-56 | aggregator | r6 report untracked at mission completion (swept by `3ea42cb`); r7 report on disk 20:10 while mission live (complete 20:13:17) and LOG/SCORECARD r7 sections + AGGREGATE.md refresh 5 uncommitted at 20:20 — its respawn (r8) owes them under the inheritance rule | §Conformance 8/12; `git status` at 20:20 |
| D-57 | protocol (self) | round-10 report's kake-SHONEN parenthetical false + "0 of 62" census false at write time; round-11 entry-note kagi-untracked phrasing superseded 3 minutes after `closed_at` — all three corrected by appended record (this report), none rewritten | §Conformance 1/3 |
| D-58 | operator/scripts | template ordering line ("Write … report" before "Round end: commit") is now causally linked to 4 lanes' report-before-commit inversions; five child-lane items still absent (M7 1/5); `report_of()` still existence-only | §Conformance 2/10; r10 §Template correction |

## Contested-scope rulings (integrator arbitration)

1. **`fleets/registry.json`** (ledger D-86; kasegi r13 §Adjacency): the
   round-10 ruling stands and kasegi r13's own proposal matches it —
   object-level split, decree ledger → kasegi, routing + `registry-check`
   tooling → kumitate (which still owes D-18). Both lanes record it in
   `PROVINCE.md` next round; no re-litigation needed.
2. **Verdict-gate standard** (kengaku r10's `.ufo/l0-questions.md` line 6,
   addressed to protocol/integrator): **ruled — deferred with a date, not
   silence.** The evidence (three sibling gates with divergent exit-code
   maps) is real, but standardizing gates is a rule addition that deserves
   its own axis-move with the cited evidence file read end-to-end; it is
   `SCORECARD.md` §Planned round-12 item (2): land the standard or record a
   reasoned rejection. kengaku must not unilaterally impose it (its own
   wording agrees); kagi/kotoba keep their current gates meanwhile.
3. **Axis-vocabulary split** (aggregator r6 L0 question: `novelty`/
   `consistency` scored by kengaku/kotoba but undefined in `AXES.md`):
   operator-side (`AXES.md` is an operator file). Integrator position on
   record: the scores are calibration defects until the vocabulary exists —
   an axis no reader can find in `AXES.md` cannot carry a re-derivable
   score. Recommend the operator add the two axes or remap the lanes.
4. **Shared main-repo `SCORECARD.md`/`LOG.md`** (ledger D-77): ruled —
   per-lane sections in the single canonical path (the file contract's
   "main-repo lanes keep theirs at the main-repo root" means one file, both
   lanes), each lane committing **only its own section's hunks**; the
   round-11 hunk-surgical staging (`55e23de`) is the reference method. A
   lane that cannot isolate its hunks waits or appends after the other's
   commit — never sweeps. If a collision ever destroys work, the fallback
   (per-lane files) becomes a file-contract change proposal.

## Stale-lane listing (missions open > 2 driver ticks, at 20:20)

Age from launch timestamps (tick = 450 s; no counter reset since 18:22:25).
Activity probes per §Stale-lane (SentinelStale2 19:49 + own re-check 20:20):

| Lane | Round | Launched | Age (ticks) | Verdict | Activity pointer |
|---|---|---|---|---|---|
| protocol | 11 | 18:50:31 | ~9.7 | progressing (this lane) | `3ea42cb`, `6bd4f38`, `55e23de` |
| kengaku | 11 | 19:50:44 | ~3.9 | progressing | `round-11/kengaku-DRAFT.md` on disk 20:1x; r10 chain `0c51208` |
| kagi | 12 | 20:13:20 | ~0.7 | fresh | r11 closed the loop (`301b9ec`, report `029c474`) |
| kumitate | 11 | 20:05:47 | ~1.9 | progressing-thin | `scripts/round-gate.mjs` untracked 19:48 (r10); WATCH — weakest lane two passes running |
| aggregator | 8 | 20:13:18 | ~0.7 | fresh; r7 left LOG/SCORECARD/AGGREGATE edits uncommitted → r8 owes them (D-56) | `git status` 20:20 |
| kotoba | 12 | 19:35:40 | ~6.1 | progressing | `4dd7753`, `7d15407`, self-landed r11 report `f9dcfd2` |
| kake | 14 | 20:05:46 | ~1.9 | progressing | `2a5502c` 20:05:41 (r13) |
| kasegi | 14 | 19:50:43 | ~4.3 | progressing | `7483333` 19:44:20 (r13), report `0933e84` |

No silent missions → no `failed` markings from the stale-lane trigger this
round. Actuator limit unchanged: recording `failed` is a ledger act; only
`omp down` removes a mission (appendix "Liveness probes").

## Cross-domain evidence encountered (not absorbed)

- **bounties (operator-owned, read-only per the new rule):** kasegi r13's
  upstream-bound findings (`fleet-dispatch.mjs:200/:107` adjusted-EV
  curation bug; `telemetry.jsonl` markers=3 of 7225) live in its report —
  this lane re-verified them read-only and pushes nothing there; the stalled
  rebase question stays with the operator (`.ufo/l0-questions.md` line 1).
- **webzites (kake province, operator-gated):** `webzites-keeper.timer`
  disabled+inactive, never fired (kake r12, re-verified live by ScoutVerify2)
  — L0 line 5 is the operator's call.
- **ufo-fsd-alpha (external, D-22/D-23):** unchanged, owner outside all
  provinces; kumitate carries the report.
- **OMP runtime (D-46):** ScoutLedger found the filed pointer unresolvable
  at both ends (UNSUBSTANTIATED) — kake's relay text is not in
  `round-10/kake.md` and kumitate's `loop-driver.md` no longer carries the
  quoted claim; row should be re-filed with a live pointer or dropped
  (aggregator's call, ledger owner).

## L2 dispatch record

Batch 1 — ONE batched `task` call, 10 subagents (mission floor 8):
`ScoutOblig` (91-obligation census, machine-tiled 583 lines), `ScoutDupes`
(30 clusters / 96 instances; reconciles the round-10 "17 pairs"; named
contradictions (a)/(b)/(c1–c3) incl. the ledger's now-false absence premise),
`ScoutClosure` (six post-`closed_at` lane-rounds: content/commit/identity —
surfaced both round-10 falsifications), `SentinelStale` (actuator pass
19:02), `ConnectorSibs` (157 references / 56 files → must-survive anchors;
corrected the `rounds[1]` count), `CriticPlan` (amendments A1–A6 adopted:
digest-not-verbatim appendix, pointer formula, protected verbatim classes,
closure-before-compaction sequencing, built the 93-predicate census +
verifier), `LabratCounts` (before-numbers re-execution; 7 drifted values
caught before they shipped), `ScoutLedger` (49-row queue re-verification:
11/6/16/1/14), `ReviewerCites` (independent step-1 re-execution on six
reports; confirmed both round-10 falsifications), `ScribeAppendix` (40-fact
incident extraction → the appendix digest's source).
Batch 2 — 4 subagents: `ScoutVerify2` (seven newest terminations verified;
found the report-before-commit pattern + `d7dbd9a`), `CriticCompact`
(91/91 semantic walk; 5 must-fixes — all landed), `ReviewerCompact` (8-item
mechanical re-verification; 2 wrap blockers + drift-pin pointer — all
landed), `SentinelStale2` (actuator pass 19:49).
Reviewer deltas: CriticCompact's `rounds[1]` re-count (13, not the
connector's 12 — files churned between passes) is what the appendix row now
says, framed as a drifting count; ScoutVerify2's ordering findings corrected
two entry notes before commit and one after (§Conformance 3).

## SHONEN

The main repo carries no `SHONEN.md` (fleet-meta has no minted shonen; the
protocol lane is a role). The four canonical boxes, assessed against this
lane's artifacts — all `[~]` author-asserted (I authored this round's
changes; only a non-author verifier may write `[x]`):

- [~] SKILL.md contains real decision tables, error patterns, checklists,
      cited sources — no `SKILL.md` for fleet-meta; the equivalent artifact
      is `PROTOCOL.md` itself, now 446 lines with a 32-row dated error/
      incident digest, four executable check commands kept verbatim, and a
      committed re-runnable preservation verifier
      (`.ufo/waves/round-11/verify-census.sh` → 93/93).
- [~] At least one end-to-end domain task executed and logged — the closure
      pass ran end-to-end against the live fleet: 7 entries appended under
      a frozen `closed_at` while 8 missions churned around it, JSON
      validated, `rounds[1]` citations preserved, committed `3ea42cb` and
      pushed; logged at `LOG.md` §Round 11.
- [~] Instructions executable by an agent without oral context — the
      compaction's own acceptance test is executable by a stranger: run the
      verifier, diff the seed, re-count the metrics; the mapping
      (census id → surviving home) is the committed census TSV plus
      `.ufo/waves/round-11/protocol-dupes.md` canonical-home column.
- [~] No cross-domain bleed — this round touched `PROTOCOL.md`,
      `MANIFEST.json` (`rounds` only), `SCORECARD.md` (protocol-section
      hunks only), `LOG.md` (own entry only), `.ufo/prompts/*.md` (commit
      only, never edit), `.ufo/waves/round-11/`, three durability-swept
      reports, and this report. No child-repo file, no `scripts/`, no
      `MISSION.md`/`AXES.md`/`CORPUS.md`, no `.ufo/state`, no
      `watchdog.log`, no `AGGREGATE.md`, no domain source repo
      (`git show --stat 3ea42cb 6bd4f38 55e23de`).

## Scope compliance

`git show --stat` for the three landed commits: `MANIFEST.json` (`rounds`
appends only; roster/rank untouched), 15 `.ufo/prompts/*.md` (added, never
edited), 3 reports (durability sweeps with attribution defects recorded),
11 `.ufo/waves/round-11/` artifacts, `PROTOCOL.md`, `SCORECARD.md` (hunk-
staged: 32+/22−, all inside the protocol section), `LOG.md` (blob-staged:
+57, own entry only). The aggregator's uncommitted round-7 sections in
`LOG.md`/`SCORECARD.md`/`AGGREGATE.md` and kengaku's `round-11/kengaku-
DRAFT.md` were deliberately left unstaged. No commit amended; corrections
appended (§Conformance 1/3). Operator push-scope rule respected: pushes go
to `origin` = `https://github.com/VeigaPunk/shokunin` only; `bounties`,
`ufo-fsd-alpha`, `charter-ufo-fsd` were read by L2 probes only, never
committed or pushed.

## Watch items for round 12

1. Resolve the 4 `in-flight` rows written at 20:10 (protocol r11 → this
   report's commit; kengaku r11; kumitate r11; kotoba r12) plus the
   post-`closed_at` band: aggregator r7 (complete 20:13:17), kagi r11's
   complete line, kake r13/r14, kasegi r13/r14, kagi r12, aggregator r8.
2. Rule the verdict-gate standard (land or reasoned rejection) — §Rulings 2.
3. Whether the operator lands the template five items + ordering fix and the
   marker-aware `report_of()` (D-58): the report-before-commit pattern (4
   lanes) is now the measured cost of the ordering inversion.
4. Whether the landed-by-the-lane habit holds: 4 self-landings in ~90
   minutes (kengaku, kagi, kotoba, kumitate-earlier) after 0 in rounds 1–9;
   kagi/kumitate/kasegi regressed to operator-swept within the same window —
   measure again at the next pass.
5. Aggregator r8: does refresh 5 land the committed ledger with the 9 new
   rows (D-50…D-58) mirrored, and does it resolve its uncommitted r7
   LOG/SCORECARD sections itself (D-56)?
6. kumitate progressing-thin two passes running — first candidate for the
   stale-lane `failed` trigger if its next pass shows silence.
7. Kama mint decision + template/state/log L0 answers still pending
   (`.ufo/l0-questions.md` lines 2–3).
