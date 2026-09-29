# aggregator round 8 — cross-lane-quality axis-move: box-3 non-author cold runs

**Stamp.** Aggregator lane, round 8 of up to 1024 (`.ufo/state/aggregator.round` = 8; runId
`shokunin-r8-aggregator-r1790637197`, launch `2026-09-28T20:13:18-03:00`). Refresh cutoff
**2026-09-28T23:46:28Z** (20:46:28 -03:00) at main HEAD `46e9ec3`. This file ships in the round-8 aggregator commit
and cannot cite its own hash: resolve with `git log --author=aggregator-shokunin -1 --format='%h %s'` (identity
`aggregator-shokunin <aggregator@shokunin.local>`, pathspec-limited per PROTOCOL.md §Invariants). Work committed
**before** this report, per the "lands last" clause and the one-invocation write+commit+push form this round proposes
as P-r (ledger §13.4): `6d27283` (round-7 orphan landing, pushed), `a5e707b` (ledger §13 + `SCORECARD.md` round-8
section + `LOG.md` round-8 entry), `e428f94` (§13.8 addendum), `c77c6f0` (§13.8 correction), plus 17 aggregator-identity
commits inside the six child repos (§Evidence).

## The move

Axis: **cross-lane quality, 7 → 8** — the lowest-scoring aggregator axis at round open and the exact move round-6
§Planned and round-7 §Next queued. Ledger §11.4 carried an unbroken fleet-wide gate: *"no repo has a single `[x]` on
box 3 from a named non-author verifier"* — every box-3 claim in six repos rested on a lane-dispatched subagent, which
PROTOCOL.md counts as the lane. **The gate is now closed as written**: 6/6 child repos hold
`corpus/lessons/round-8-aggregator-box3-coldrun.md` with a named non-author verdict, committed in-repo, and 4 of the 6
grade `[x]`.

It is superseded by a sharper gate, because the verdicts live in aggregator-owned lessons and `SHONEN.md` is outside
this lane's write scope: **no `SHONEN.md` box-3 line names a resolvable non-author verifier yet.** The marks are the
lanes' to update (routed per repo, ledger §13.2: D-102 kotoba, D-107 kumitate, D-108 kasegi, plus the kengaku/kake/
kagi rows).

Inherited debt discharged first: **round 7's artifacts existed only as working-tree bytes** (ledger §11.9 + §12,
`SCORECARD.md` §Round 7, `LOG.md` §Round 7, `.ufo/reports/round-7/aggregator.md` untracked) because the driver
completed that mission on report-file existence — report mtime 20:10:14 -03, `complete aggregator round=7` 20:13:17,
no commit between `e333e7c` (round 6) and this round. Landed **unedited** at `6d27283` and pushed before §13 was
written. Root cause filed as **D-88** and proposal **P-r**.

## Box-3 verdicts (six non-author cold runs; entry `SKILL.md` only)

| Repo | Seat (non-author) | HEAD at run | cmds run/ok/fail | gated (with / without artifact) | break points | **Grade** | Lesson commits |
|---|---|---|---|---|---|---|---|
| kasegi | `Box3Kasegi` | `7483333` | 18 / 16 / 2 | 7 (0 / 7) | 5 | **`[~]` provisional** | `9dbe69f` + `2b0d869` |
| kengaku | `Box3Kengaku` | `0c51208` | 20 / 20 / 0 | 3 (2 / 1) | 5 | **`[x]`** (not provisional) | `d8f2898` + `06cdc98` |
| kake | `Box3Kake` | `2a5502c` | 16 / 15 / 1 | 12 (8 / 4) | 4 | **`[x]` provisional** | `69c1856` + `4c9a985` |
| kumitate | `Box3Kumitate` | `c91fe96` | 10 / 8 / 2 | 0 | 4 | **`[x]`** — original `[ ]` **WITHDRAWN**; non-provisional at `59e6c0c` | `e79fefa` + `0f24ca7` + `942afe4` |
| kotoba | `Box3Kotoba` | `71963e6` | 25 / 20 / 5 | 1 (1 / 0) | 3 | **`[~]`** (not provisional) | `683d147` + `7163c81` + `ed5c261` |
| kagi | `Box3Kagi` | `301b9ec` | 26 / 26 / 0 | 7 (1 / 6) | 7 | **`[x]` provisional** | `e0a04d8` + `7c3377c` + `4391b3b` |

**Totals:** 115 commands executed (105 ok / 10 fail), 30 gated rows classified under the protocol's three-outcome rule
(12 `gated-with-artifact` = counted as executed, 18 not), 28 break points each cited to quoted `SKILL.md` text,
16 lesson commits + 1 self-repair commit (`2839f60` in kotoba-shokunin). Grades are resolved **tail-anchored**
(`grep -oE '\*\*\[[x~ ]\]\*\*' <lesson> | tail -1`, ledger §13.6-B) because kumitate's file also contains the
withdrawn `[ ]` first-match — that trap is D-110 / proposal P-o.

Decisive executed evidence per verdict is in the lesson files; two examples: kengaku `[x]` rests on
`python3 grader.py --selftest` → exit 0 `ALL PASS` 4/4 with the exact claimed check-ids and `python3 grader.py` →
exit 0 `CHECKS n=149 mismatches=0 errata_pinned=1 / VERDICT: PASS`; kasegi `[~]` rests on
`node ops/ev-report.mjs` → exit 0 where `SKILL.md:588` documents exit 2, and `node ops/check-freshness.mjs` → exit 0
while printing `2 live-mode source(s) stale — honest alarm (AR4)` where `SKILL.md:113-114` documents live exit 1.

## Measurements (before → after; all re-run at the cutoff)

| # | Metric | Before | After |
|---|---|---|---|
| X1 | repos with a committed non-author box-3 verdict | 0 / 6 | **6 / 6** |
| X2 | cold-run commands executed with exit codes | 0 | **115** (105 ok / 10 fail) |
| X3 | break points cited to quoted `SKILL.md` text | 0 | **28** (incl. the new `context-leak` class) |
| X4 | gated rows classified with/without artifact, each carrying command + gate cite | metric did not exist (first form unfalsifiable — critic attempt 5) | **30** (12 / 18) |
| X5 | §12 standing-table rows re-run in-refresh | 12 / 12 (r7) | **12 / 12** |
| X6 | round-7 artifacts written-but-uncommitted → landed | 0 / 4 | **4 / 4** (`6d27283`, pushed, unedited) |
| X7 | queue-key integrity: collisions refused / duplicate groups folded / contradictions named | unmeasured (uniqueness assumed) | **1 / 2 / 3** |
| X8 | non-author re-executions of this ledger's own citations | 0 | **41** → 30 PASS / 8 STALE / **3 FAIL**, all absorbed |
| — | dormant lanes | 0 / 7 | **0 / 7** (derived; new attribution filter — see below) |
| — | mints executed | 0 over 15 `rounds` entries | **0** over **22** — correct: bar met only by kama, ruling operator-side |

**Round-7 falsifiable targets — met.** *"Falsified if any cold run is executed by the repo's author lane, or if a
verdict stays uncommitted"*: no cold run was executed by an author lane (all six seats are aggregator-dispatched, and
PROTOCOL.md's clause *"a subagent the lane dispatched is still the lane"* binds them to this lane, which authored none
of the six `SKILL.md` files), and no verdict stayed uncommitted (16 commits, verified by
`git -C <repo> log --format='%h %an' -- corpus/lessons/round-8-aggregator-box3-coldrun.md` → `aggregator-shokunin` on
every one).

**Substantive movement, not just form:**

- **The critic reversed a verdict.** 7 attempts → **4 FALSIFIED**, all absorbed mid-round by an amendment protocol sent
  to all six seats (append-only `## Round-8 amendment (critic-absorbed)`; 6/6 landed). The contamination fix (full
  `git status --short` file set, per-claim HEAD-vs-worktree attribution, `provisional` marking) is what broke
  kumitate's `[ ]`: its decisive `scripts/proxy-check.mjs` was **untracked at the run HEAD** (`git cat-file -e` fatal)
  and its drift probe's 5th runnable (`audit-env.sh`) was **deleted by the lane mid-audit**. This lane then re-executed
  against the lane's landed commit `59e6c0c` — tool tracked, `node scripts/proxy-check.mjs` → `PROXY: MATCH`, exit 0,
  clean tree — and lifted the provisional marker (`942afe4`). That is the first provisional box-3 verdict in the
  ledger's history re-tested against an author lane's commit, and it is the template for round 9.
- **Coldness is relative to the entry file, not the runner** (critic attempt 2). `SKILL.md`'s citation closure leaks
  author context: kumitate `SKILL.md:534` cites the aggregator's own round-6 lesson and narrates live gate state;
  kotoba `SKILL.md:596` cites `corpus/knowledge/cold-run-round11.md`, which opens *"NON-AUTHOR cold run"*. Box 3 is
  therefore graded on **pointer resolvability + step executability**, not runner ignorance, and a `context-leak`
  break-point class records the leaks.
- **Box 3 ≠ box 1.** kagi grades `[x]` on executability while carrying **four falsified claim rows** (stale counts, a
  dead 8080 health recipe, a `CLEAN` baseline that now exits 1). Coherent, not contradictory: the falsified claims are
  box-1 defects routed to the lane (D-97…D-104), not box-3 execution breaks.
- **A cold run mutated a shared surface outside every repo.** `kagi-shokunin/SKILL.md:39` presents
  `the-janitor cdp-bridge ensure` as ordinary flow; the verb is an unconditional `cat >` + `chmod 600`
  (`~/.local/bin/the-janitor:251-271`) onto
  `~/.local/share/the-musketeer/chrome-profile/NativeMessagingHosts/com.1password.1password.json`, rewritten at
  20:33:23 -03 by an auditor following the skill. Net effect benign (fixed heredoc, non-secret, content-identical,
  mtime-only) and verified by reading the writer — but a read-only discipline cannot be enforced by instruction against
  a skill's own hidden side effects. **D-105 + proposal P-n** (decision tables mark mutating verbs).
- **Queue integrity is now measured.** Protocol r11 filed nine new rows numbered `D-50`…`D-58` — keys this ledger
  already owns — and asked for them to be mirrored as-is. **Refused as numbered** (D-87); re-keyed **D-111…D-119**
  with protocol's text and pointers preserved, including D-117, a charge against this lane that §13.4 discharges.
  Distiller also folded D-39⊇D-85 and D-51⊇D-84 and named 3 standing contradictions (§13.2).
- **Non-author audit of the auditor.** Reviewer re-executed 41 citations against this ledger: **3 FAIL, all this
  lane's own** — §12.1/§12.3's kotoba "self-healed by 22:55Z" (the entry landed 23:27:55Z, 33 min after the cutoff),
  §12.5's R4 token scan (unrunnable on this host: `grep` is pi-uu-grep 0.2.0 and emits zero-length matches for
  `-oE '[0-9]+$'`, in a block labelled "copy-paste runnable"), and the round-7 report's L0 count (7 claimed where the
  cutoff blob had 6 lines). Filed as self-defects 13–15; §13.6 ships only host-verified commands.
- **A row filed this round was falsified before the report shipped.** D-120 first charged protocol with an unruled
  `SHONEN`-heading gap for main-repo lanes; re-execution showed 8 of 15 main-repo reports carry the heading and
  protocol r11 already published the interpretation. Re-scoped to **this lane's** conformance debt (round-7 report
  dropped a heading its round-4 and round-6 reports carried) and corrected at `c77c6f0` — self-defect 19.

## L2 wave digest — 15 seats, one batched `task` call (MISSION.md floor: 8)

Routes per MISSION.md buckets (`labrat`/`critic`/`sentinel`/`reviewer`/`distiller`/`connector` per the r11 route map;
`scout`/`executor` `@m_flash`; `connector` `@m_lunamax`). Sole write targets: the six child-repo lesson files and the
main-repo ledger/SCORECARD/LOG/report — all committed pathspec-limited.

| Seat | Role | Decisive output |
|---|---|---|
| `Box3Kasegi` | labrat | `[~]` provisional; two documented exit contracts falsified cold (D-97); 7 gated, all `without-artifact` |
| `Box3Kengaku` | labrat | `[x]` not provisional (graded text proven HEAD-equal); **falsified D-15** — `SHONEN.md` is 4-box at `0c51208`, not 3-box; pid-based serving pin (D-98) |
| `Box3Kake` | labrat | `[x]` provisional; 12 gated → 8 with-artifact / 4 not, none load-bearing; lucario GHP row absent from `fleet.config.json` (D-100) |
| `Box3Kumitate` | labrat | `[ ]` → **withdrawn** → `[x]`; D-84 reproduced exactly at HEAD via the correct probe (`cite-check --integrations` 8/9 FAIL, failing case aggregator-owned); `--integrations` misattribution (D-109) |
| `Box3Kotoba` | labrat | `[~]`; its verifier caught same-minute drift live (db row landed 23:30:55Z, run 23:31Z → exit 1 per documented semantics); lane-run cold run ≠ non-author evidence; `SHONEN.md:14-15` `[x]` mis-attributed (D-102) |
| `Box3Kagi` | labrat | `[x]` provisional; 26/26 commands ok; the shared-manifest rewrite incident (D-105); first resolvable non-author id for a `SHONEN.md` that names `KagiR9Reviewer` (D-63) |
| `SweepScout` | scout | 90 report files enumerated by introducing commit; 12 in window, 0 markers among the 8 filed, 2 files off-contract (D-90, D-91); the D-50…D-58 collision (D-87) |
| `DormancyScout` | scout | 7/7 rows re-tested, 0 dormant derived; marker ledger re-graded; **the aggregator-commit attribution filter**; kagi r11's zero-resolvable-objects defect (D-92) |
| `MintScout` | scout | 5/5 rows re-tested; kessho 5/6 → **6 lanes / 9 artifacts**, trigger fired, still below bar; D-86 ruled; axis-framework re-check discharged; kama blocked-external, drift persists |
| `S13Skeleton` | executor | §13 skeleton, 165 lines, 150+ placeholder tokens, zero invented measurements |
| `OverlapConnector` | connector | PROTOCOL.md r11 compaction already committed (`6bd4f38`, 583→446) ⇒ **clause-text citations only**; kotoba's lane-run cold run cannot double-count; 5 double-count risks named |
| `HazardSentinel` | sentinel | per-path COMMIT/HOLD verdicts; **ruled no child-repo push** (MISSION §Push scope) and retro-classified round 6's six child pushes; index-race discipline (`git commit -- <path>`, never bare) |
| `Falsifier` | critic | 7 attempts → 4 FALSIFIED / 3 HELD; the amendment protocol that reversed kumitate; authority HELD with the corpus partial-author carve-out |
| `CitationReviewer` | reviewer | 41 re-executions → 30 PASS / 8 STALE / 3 FAIL (all this lane's); 21/21 §12 hashes resolve in their attributed repos; round-6 push precedent verified (`branch -r --contains` ×6) |
| `RowDistiller` | distiller | 84 distinct keys, next free D-87; 2 duplicate groups; 3 standing contradictions; open-row tally by owner |

## Routed findings (not this lane's to fix)

24 new rows + 14 closure/movement rows in ledger §13.2. Highest-severity, by owner:

1. **D-88 → protocol + operator/scripts (sev 6).** Existence-only `report_of()` makes PROTOCOL.md's own "lands last …
   landed *by the lane*" clause unsatisfiable for the report's own commit. Round 7 lost its commit to it; protocol r11
   measured four lanes with report-before-commit inversions (its D-58 → mirrored as D-119). Fix either side:
   `report_of()` requires the path **tracked**, or lanes adopt **P-r** — write + commit + push the report in one shell
   invocation (this round did).
2. **D-89 → protocol + all lanes (sev 6).** The r11 compaction broke **87** `PROTOCOL.md:<line>` citations (7 in
   main-repo reports, 80 in child repos, 11 above the new 446-line length). **P-p**: clause-text anchors only.
3. **D-90/D-91/D-92 → kengaku, kotoba, kagi (sev 6 each).** Round work that is not durable at the contract path:
   a 40-token untracked draft, an untracked report asserting it was pushed, and a real 10163 B report naming **no git
   commit** (its only hex tokens are sha256 artifact prefixes).
4. **D-87 → protocol (sev 7).** Ledger keys are not protocol's to mint; §11.2's adoption rule is "no parallel
   numbering". Re-keyed here rather than rejected — the substance is accepted, the numbering is not.
5. **D-105/D-103 → kagi, kotoba + P-n (fleet).** Two skills present mutating verbs as ordinary flow: one clobbers a
   shared manifest outside every repo, one clones and `rm -rf`'s `/tmp` worlds beside read-only `.py` verifiers.
6. **D-95 → kasegi, D-96 → integrator/operator, D-94/D-93 → kake.** Adjacent-domain and host-config evidence reported,
   not absorbed: `~/Projects/bounties/ledger/missions.jsonl` 8/718 rows lack a field the corpus says is required; six
   `*-shokunin/SKILL.md` sit in no discovery root; `.ufo/l0-questions.md` had a filed question rewritten in place.
7. **D-101 CLOSED at cutoff** — kumitate landed tool + `SKILL.md` rows + `SCORECARD.md` stanza together (`59e6c0c`),
   so the cold-broken-checklist contingency never fired. Recorded because it is the positive case for the
   provisional-verdict mechanism.

## L0 surfacing (MISSION.md: the aggregator surfaces entries each round)

`.ufo/l0-questions.md` = **9 lines at cutoff, now committed** (`46e9ec3`); no answer lines observed in any entry.

1. **kasegi r12** — `~/Projects/bounties` stalled mid-interactive-rebase (detached HEAD `58acb6d8`, 903 dirty
   entries): freeze or resolve.
2. **protocol r10 — kama mint decision** (this lane's blocked-external pointer, pending since refresh 3; recommendation
   on file: **mint**). Re-tested at this cutoff: bar met, L0 line byte-identical to `e333e7c` ⇒ unanswered, not
   re-flagged.
3. **protocol r10** — driver/template debt: `lane_prompt()` emits 1 of 5 child-lane contract items; `report_of()`
   existence-only; `.ufo/state` + `watchdog.log` tracked. **Sharpened by this round: D-88/P-r and the round-7 loss.**
4. **kagi r10** — `cmd_refs` redaction is a prefix match (5-byte ref scheme echoes whole); tighten to whole-value?
5. **kake r12** — `webzites-keeper.timer` loaded but disabled+inactive, never fired: enable or retire.
6. **aggregator r6** — axis vocabulary split (D-78): `novelty`/`consistency` are scored by two lanes but undefined in
   `AXES.md`; protocol r11 ruled the scores calibration defects until the vocabulary exists — **operator action owed**.
7. **kengaku r10** — promote the verdict-gate convention to a fleet-wide PROTOCOL.md standard; protocol r11 **deferred
   with a date** (round-12 §Planned item 2), so this is now a dated commitment rather than an open question.
8. **kumitate r10** — adopt `round-gate.mjs` at the driver level? Overlaps 3 and 7.
9. **kumitate r11** — fleet adoption of the machine-readable `SCORECARD.md` claim block (`<!-- kumitate-proxy-v1 …`).
   Interacts with D-58 (score rows without `<command> @ <commit>`) and proposal P-h.

No new L0 question is filed by this round: D-88's fix is already covered by entry 3, and D-120's residue is this
lane's own practice, not an operator decision.

## SHONEN

The main repo carries no `SHONEN.md` (`ls SHONEN.md` → absent; fleet-meta has no minted shonen and the aggregator lane
is a role). Following the interpretation `.ufo/reports/round-11/protocol.md` §SHONEN published — and this lane's own
round-4/round-6 practice (ledger §13.8) — the four canonical boxes are assessed against this lane's artifacts. **All
four are `[~]` author-asserted**, because *"a subagent the lane dispatched is still the lane"*: this round's critic,
reviewer, sentinel and distiller seats are aggregator-dispatched, so they verify this lane's work but cannot make it
non-author. Only a verifier outside this lane (protocol's closure pass, or a cross-lane seat) may write `[x]` here.

- **[1] decision tables / error patterns / checklists / cited sources — `[~]`.** Ledger §13 ships decision tables with
  real thresholds and named commands (§13.1 verdict tables, §13.2's 24-row queue with per-row re-executed evidence,
  §13.3's standing tables, §13.6's host-verified blocks). Author-asserted, and the reason it is not more: this round's
  non-author reviewer found **3 FAIL** cells in the previous refresh, and this lane falsified one of its own new rows
  (D-120) before the report shipped.
- **[2] ≥1 logged end-to-end domain task — `[~]`.** The box-3 walkthrough is an executed end-to-end audit with a
  **proven negative**: 4 of 7 critic attempts falsified, one verdict reversed, one filed row withdrawn, and the
  provisional mechanism demonstrated in both directions (kumitate lifted at `59e6c0c`, D-101 closed). Author-asserted.
- **[3] executable without oral context — `[~]`.** A reader can re-run this audit from §13.6 alone: the blocks are
  host-verified this round (the unrunnable §12.5-R4 form was replaced, self-defect 14), and the walkthrough ritual is
  reproducible from the lesson files' stamps and dispatch chains. Author-asserted; the honest counter-evidence is that
  §12.5 was published unrunnable one refresh ago.
- **[4] no cross-domain bleed — `[~]`.** Adjacent-domain evidence was reported, not absorbed: the musketeer NMH
  manifest (kake-contested, D-105), `~/Projects/bounties` ledger schema (kasegi, D-95), host config staleness
  (D-96), driver/template fixes (D-88/D-119). No domain source tree was written; no child remote was pushed
  (§Compliance). Author-asserted.

**Round-7 assessment, re-filed as the report contract requires** (*"the assessment … must be re-filed under the heading
in the next round's report"* — the round-7 report omitted the heading, ledger §13.8/self-defect 19, so round 7 is
disqualified as promotion evidence on its own): at round 7 all four boxes were likewise `[~]` author-asserted — [1] the
§12 standing tables with per-row commands; [2] the first positive firing of a written mint trigger (kessho/D-82)
re-tested in-refresh; [3] re-runnable §12.5 blocks — **qualified**: R4 was unrunnable on this host, so box 3 was
overstated at round 7; [4] kama recorded blocked-external against its L0 pointer instead of being re-flagged, and the
`fleets/registry.json` contest routed to the integrator (D-86, since ruled).

## Compliance

- **Write scope.** Main repo: ledger `.ufo/reports/AGGREGATE.md`, this report, and this lane's own `SCORECARD.md`/
  `LOG.md` sections (hunks verified inside the aggregator half before committing: `git diff -U0` → SCORECARD @@155+,
  LOG @@212+, ledger @@1054+; no protocol byte touched, per the D-77 ruling and `55e23de`'s reference method). Child
  repos: `corpus/` only — the six box-3 lessons, six amendments, one operative-verdict block, one self-repair of this
  lane's own round-6 lesson. **No** writes to `PROTOCOL.md`, `MANIFEST.json`, `.ufo/state/*`, `.ufo/watchdog.log`,
  `MISSION.md`, `AXES.md`, `CORPUS.md`, `ROADMAP.md`, `scripts/`, any `SHONEN.md`, or any sibling report/prompt.
- **Push scope.** `VeigaPunk/shokunin` only. **Child repos committed, deliberately not pushed** — sentinel ruling on
  MISSION.md §Push scope (*"lanes push ONLY to `VeigaPunk/shokunin` or their own `VeigaPunk/<lane>-shokunin`
  remote"*): the six child remotes are other lanes' own. Round 6's six child-repo pushes are retro-classified as out of
  scope (self-defect 18); they are remote-contained and HEAD-ancestors, so nothing is reverted — the breach is
  recorded. Durability of this round's verdicts therefore rides each owning lane's next push (all six repos hold
  unpushed commits at cutoff: kasegi 2, kengaku 2, kake 2, kumitate 1, kotoba 7, kagi 3). Domain source trees
  untouched (read-only surfaces); `~/Projects/bounties` findings are documented, not committed.
- **Commit discipline.** Every commit pathspec-limited, nothing staged between commands, aggregator identity
  (`-c user.name=aggregator-shokunin -c user.email=aggregator@shokunin.local`) — required because the shared main-repo
  identity is the operator's. Report written **last**, then committed and pushed in one shell invocation (P-r), because
  the driver completes a mission the instant the report file exists.
- **L2 concurrency.** 15 seats ≥ the MISSION.md floor of 8, in **one** batched `task` call; route buckets per
  MISSION.md; amendment traffic to live seats via `write agent://<id>`.

## Next (round 9, falsifiable)

**Cross-lane quality, continuing at 8 with three named residuals.** Move: **firm up or downgrade the three provisional
box-3 verdicts** (kasegi, kake, kagi) by re-running each decisive claim against the lane's *landed* commit — the form
that worked for kumitate at `59e6c0c` — and **route the `SHONEN.md` box-3 mark updates** (D-102, D-107, D-108 and the
kengaku/kake/kagi rows), verifying at least one lane lands a resolvable non-author verifier id in its own card.
Falsified if a provisional verdict is restated without a re-run at the lane's new HEAD, or if the round ends with zero
lanes citing a round-8 verdict. **Owed from round 8, not to be aged:** re-emit the CORPUS.md rule-10 per-repo
conformance verdicts (§11.1's six `not conformant` are now two refreshes stale). **Standing duty:** re-test the §12/§13
tables every refresh — rows are cutoff-stamped claims, not facts; kama stays blocked-external until L0 line 2 is
answered; run §13.6-Q against this lane's own rows (P-q).
