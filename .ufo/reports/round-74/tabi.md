# tabi — round 74 report

L1 `TabiR74`, attempt 1. Lane `/home/vgpnk/Projects/shokunin/tabi-shokunin`, branch `master`, base
`c72235d6aebca89269809050e983d53df36273f5`, final lane hash `1f60b113b87b7fc83f9d5f837d89e53fab6a99e5`
(`git ls-remote origin refs/heads/master` prints it; `jj-lane.sh state`: `ahead=0 behind=0 tracked=0 untracked=0`).
`.ufo/watchdog.log` shows only `launch tabi round=74 … attempt=1`: no earlier attempt, nothing inherited.

## Work performed

Declared claims (1): **C1 coverage**, a capability acquisition: `chromium-ime-composition-linux`, CDP
`Input.imeSetComposition` and `Input.insertText` on Chromium 155 headless. It is sourced from S187–S193,
opened this round before the freeze. The frozen predicate `C1-IMECOMPOSE-R74` (a)–(d) is in
`.ufo/waves/round-74/claims.json` (freeze `8faa903a`, digests commit D `ca30e1a3`).
**Verdict: all four legs hold on the frozen predicate.** R74Critic and R74Review1 falsified the frozen
`priorSet` and `limit` sentences. The correction is in SCORECARD (append-only). No instrument,
predicate or kill rule was changed. There is no exploratory claim. The lowest-axis obligation is met,
because all six axes tie at 9.

- Reads before the claim: the r71, r72 and r73 spot-checks (`corpus/lessons/round-7{1,2,3}-verifier-spotcheck.md`)
  and the r60–r62 root failures. Routed defect 3 of the r73 closure (the 1e-12 timeline escape) is
  closed for this generation: the near-match and quantum checks refuse it (`controls/c1/controls-summary.json`
  `replay-forged-1e-12`, exit 1 `replay-event-timeline`). Routed defects 1–2 (the pinch prior set and
  the R73Mut1 survivors) are carried, not claimed. The reason is in `corpus/lessons/round-74.md`
  `## Round-73 routed defects`.
- End-to-end domain work: four probe runs fixed the 16-leg shape (`controls/c1/probe/`). The first two
  full passes went red because of instrument bugs: a look-alike regex matched the driver's own
  readiness probe, and a carried "all events trusted" rule could not hold because `compositionend` is
  untrusted. Both are mined (Mistakes rows 1–2, `lesson-proof/prefreeze-defects.json`, exit 0).
- Instruments (pre-freeze commit `b70e0a27`):
  - `scripts/chrome-cdp-imecompose-round74.mjs`: the driver. It keeps the r73 plumbing and adds a new
    fixture and 16 legs.
  - `scripts/check-imecompose-r74.mjs`: the counter, 148 checks. It adds a near-match timeline with a
    tolerance under 0.05 ms, an `event-time-quantum` check (0.1 ms), `fixture-hash` bound to the
    pinned driver, and six cross-leg laws.
  - `scripts/negatives-imecompose-r74.mjs`: the battery, 239 cases.
  - `controls/c1/kill-power-r74.mjs`: 148 force-true and 26 semantic mutants, including M5.
- Pre-freeze executed controls (`b70e0a27`):
  - 9 cold repetitions. The counter, the battery and kill power all ran on every one, 9/9
    (`controls/c1/prefreeze-summary.json`, which fails closed).
  - Controls allOk (`controls/c1/controls-summary.json`):
    - no receipt: exit 2;
    - the r73 pinch receipt: exit 1;
    - no flags: exit 2;
    - replay and nonce+stamps rewrites: exit 1 with the replay ids;
    - 1e-12 forgery: exit 1;
    - full rewrite plus a 0.1 ms move: exit 0, the declared limit witness.
  - Three look-alike drivers exit 1, are labelled, and come out REFUTED.
- Leg (a): the L1 ran the post-D run with nonce `tabi-r74-l1-ca30e1a3b7b2`. Driver exit 0; counter
  exit 0, clean, 148 checks (`.ufo/waves/round-74/scored/c1-counter-a.json`). Receipt
  `corpus/evidence/round74/chromium-ime-composition/receipt.json`, landed `19c301da`.
- Leg (b): R74Exec1 cold run, nonce `tabi-r74-exec1-ca30e1a3b7b2`. Counter exit 0, clean, 148 checks,
  with PRE plus (a) as priors (`.ufo/waves/round-74/w1/R74Exec1/counter.json`). The L1 re-ran it
  through `scripts/selftest-r74-gates.mjs` `exec1-clean` (`scored/selftest-r74-gates.out`, 12/12, exit 0).
- Leg (c):
  - Battery exit 0, 239/239, coverage gap 0 (`scored/c1-negatives-a.json`).
  - Kill power holds: 148/148 force-true, 26/26 semantic, unmutated exit 0 (`scored/c1-kill-power-a.json`).
  - R74Exec1 re-ran both and they agree (`w1/R74Exec1/negatives-a.json`, `kill-power-a.json`).
- Leg (d): SCORECARD capability row 0 → 1 (`grep -c '^| \`chromium-ime-composition-linux\` |' SCORECARD.md` → 1).
  The note `corpus/knowledge/chromium-ime-composition-runtime-round-74.md` has a `source:` line that
  cites S187–S193.
- Post-freeze checks, frozen instruments run unchanged (`.ufo/waves/round-74/lesson-proof/postfreeze-checks.json`, allOk, exit 0):
  - With the three committed probe receipts added as priors, the (a), R74Exec1 and R74Exec2 d1–d3
    receipts stay clean. So none of this round's receipts is a relabel of a probe.
  - The critic's p2/p3 relabels are refused for the three replay ids.
  - The four scored kill-power rows that R74Review2 F1 flagged (no failing-case list) are genuine
    kills, each attributed to the mutated check.
- Falsified sentences (SCORECARD `## Round 74` correction; Mistakes rows 4–5):
  - `priorSet`: three probe receipts of the schema were committed outside PRE
    (`lesson-proof/prior-set-enumeration.txt`). Relabels of them pass legs (a)–(c)
    (`w1/R74Critic/min-p2.counter.json`, `min-p3.counter.json`, `bat-min-p2.json`, `kp-p2.json`).
  - `limit`: a receipt with one focus event added or removed escapes the equal-count near-match
    (`w1/R74Review1/b4-…`, `b5-…`, exit 0). The limit also does not say that "after D" goes unchecked.
- Wave findings integrated or routed (`corpus/lessons/round-74.md` `## Attack findings`):
  - R74Review2 F2: the battery does not require its laundered receipts. F4/F5: tolerance weakenings
    survive.
  - R74Mut1: 28 of 54 extra mutants survive, 19 of them with acceptance witnesses.
  - R74Review3 F1: the counter output does not record its prior set.
  - R74Scout located S194–S195. The L1 re-opened both and they now source the note's two
    measured-only mechanisms.
- Round shape: **one v1 wave `w1`, 11 seats**, validated under `ufo-wave-policy.json`
  (`.ufo/waves/round-74/w1-spec.json`, `w1-dispatch.json`). The orchestrator spawned it through the
  inline handoff (`w1.ready`, `w1.ready.dispatched`) and the results are in `w1-results.json`.
  - Role mix: executor 2, reviewer 3, critic 1, mutation-tester 1, scout 1, connector 1, scribe 1, revenger 1.
  - Attack share: 5/11 = 45% (3 reviewers, 1 critic, 1 mutation-tester).
  - Dead seats: 0. Residual call: none. Round total: 11.
  - The planner seat is held by the L1; the validator rejects `planner`.
  - Routing came from `task.agentModelOverrides`; no model was passed. Seat models were not recorded
    because no claim depends on them.
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows untracked
  `trail-ids.txt` and `.scratch/run15-wrapup/…`. `trail-ids.txt` is a 1-byte file with mtime
  2026-11-06 20:36, before this round's launch at 23:08, so no seat of this round wrote it; it is left
  untouched. `.scratch/` belongs to the orchestrator. No misroot.
- Scratch: `$HYAKU_SCRATCH/tabi-r74` removed after landing. `ls /fast/scratch/hyaku | grep -c tabi-r74` → 0.

## Landed changes

| Commit | Content | LOG.md entry |
|---|---|---|
| `b70e0a27` | Pre-freeze instruments; controls; 9 pre-freeze repetitions with summary; probe receipts; sources S187–S193 staged plus rows; note; lesson draft; QUALITY 139; census start; lesson proof | `## Round 74` bullets 2–4 |
| `8faa903a` | `claims.json` freeze (C1-IMECOMPOSE-R74) | bullet 4 |
| `ca30e1a3` | `freeze.txt` digests (commit D) | bullet 4 |
| `19c301da` | Scored run: receipt, counter, battery, kill power, `status-at-dispatch.txt` | bullet 5 |
| `db59ed42` | Wave spec and validated dispatch | bullet 7 |
| `503fde39` | Wave evidence (`w1/`, `w1-results.json`, ready markers); SCORECARD round-74 section with capability row and correction; LOG; SKILL.md `## Round 74 gate registry`; `scripts/selftest-r74-gates.mjs`; QUALITY 140; S194–S195; README coverage; lesson final; post-freeze checks; census end | bullets 6–7 |
| `1f60b113` | The two R74Connector hit files over 1 MiB, named explicitly | bullet 7 |

## Before → after measurements

- **C1** (measured at base `c72235d6` → lane tip `1f60b113`; the scored receipt landed at `19c301da`).
  - Counting command:
    `node scripts/check-imecompose-r74.mjs --receipt corpus/evidence/round74/chromium-ime-composition/receipt.json --expect-driver-sha256 afacee1b193ea2ba7ccab945956cee912eeed18cc5aa2fcacf5d65dc261dc2dc --expect-nonce tabi-r74-l1-ca30e1a3b7b2 <12 PRE --prior> --json`.
  - Before: no receipt → exit 2 `receipt-unreadable`. The r73 pinch receipt → exit 1.
  - After: exit 0, clean, 148 checks.
  - Capability row: `git show c72235d6:SCORECARD.md | grep -c '^| \`chromium-ime-composition-linux\` |'` → 0;
    at `1f60b113` → 1.
  - Knowledge notes citing `imeSetComposition`: `git grep -l imeSetComposition <rev> -- corpus/knowledge | wc -l`
    is 0 → 1.
  - Do-nothing control: `controls/c1/controls-summary.json` (allOk); the controls fail before the work
    and do not reach the target.
- Census: 186 → 195 rows. Command: `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tabi`,
  exit 0 at both ends; W04 warnings 25 → 27.

## Sources & frontier

- Census start: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tabi`
  → `tabi ok …/corpus/SOURCES.md`, exit 0, 186 rows, 25 W04 (`.ufo/waves/round-74/census/start.txt`).
- Census end: same command → `tabi ok`, **exit 0**, 195 rows, 27 W04 (`.ufo/waves/round-74/census/end.txt`).
  Counting command: `grep -cE '^\| S[0-9]{3} ' corpus/SOURCES.md`.
- Rows added (all tier A `code`, mined, recheck `on-release`):
  - Before the freeze, S187–S193: Input.pdl IME scope, input_handler.cc IME scope, input_method_controller.cc,
    event_target.cc, event_dispatcher.cc, scoped_event_queue.cc, editing_utilities.cc.
  - After the freeze, S194–S195: document.cc and frame_selection.cc. R74Scout located them; the L1
    re-opened them.
  - Each row has its URL, access time, ≤25-word located quote and sha256 in `corpus/lessons/round-74.md` `## Gate`
    and `.ufo/waves/round-74/sources/FETCH.txt`.
  - S187 and S188 are byte-identical to S173 and S174 with new scopes, which accounts for the two new W04 warnings.
- Rows touched old→new: none. No status, recheck or used-by cell of an existing row changed.
- Frontier advanced: IME composition moved frontier → core for this build (`corpus/README.md` `## Round 74 coverage`).
  The note's two measured-only mechanisms are now sourced (S194–S195).
  Still frontier: replacement ranges, IME text spans, and the editor links between the sourced ends.
- Sourced claim: C1 rests on S187–S193, opened this round. The note's `source:` line cites them.
- Mined mistakes: 5 rows (`corpus/lessons/round-74.md` `## Mistakes`). Each is shown able to fail:
  - rows 1–3: `lesson-proof/prefreeze-defects.json`, exit 0 only while the old rules fail;
  - row 4: `lesson-proof/prior-set-enumeration.txt`, 3 outside PRE;
  - row 5: R74Review1 b4/b5, exit 0.
  - QUALITY 139–140 were added.
- Admit/reject for spot-check: the IME note is admitted. Three claims are rejected: keyCode 229
  keydown from this producer, `imeCommitComposition` as a command, and "no focus means insertText does
  nothing". R74Scout's unopened intermediate editor links are also rejected.
- Assimilation: none. `merge/tabi/` adoption stays closed pending L0 `tabi | round-57`.
  `considerthese/`: no such directory in this lane.
- r73 verifier spot-check disagreements: none (agree on all four). Its routed defects are dispositioned
  in the lesson (3 closed for the new generation; 1, 2 and 4 carried).

## Trend verdicts

- **expansion: improved.** Capability `chromium-ime-composition-linux` admitted to the table (row 0 → 1).
  Knowledge 86 → 87 on ground the coverage map did not hold (`git ls-tree -r --name-only <rev> corpus/knowledge | wc -l`).
  Registry 186 → 195.
- **quality: improved, contested.** The round-73 1e-12 timeline escape is refused by the new
  generation (control `replay-forged-1e-12`). S194–S195 turn the note's inference into sourced
  statements. Every S187–S193 anchor re-lands (R74Scout, 27 checks) and the note's table re-derives
  with 0 mismatches (R74Scribe). R74Critic reads the false frozen `priorSet`/`limit` sentences as
  quality and calibration harm. They are corrected append-only, not deleted; the closure rules.
- **discernment: improved.** Five mistakes are mined with fail-able proofs (QUALITY 139–140). Attack-seat
  falsifications are recorded rather than argued away. The Gate carries one admit and three rejects
  for spot-check.
- Per-axis: coverage improved (C1). Calibration has no claim and is **contested**: R74Critic says
  harmed (the frozen sentences were false at the freeze); the L1 reads it as unchanged because the
  correction is on record. Operator or closure to rule. Depth, freshness, operability and adjacency are
  unchanged (R74Connector: overlap none, verdict adjacent).

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources. Pointer:
  `SKILL.md` `## Round 74 gate registry`, plus prior pointers in `SHONEN.md:5-6`. R74Revenger checked
  that the pointers resolve; a lane seat is not a non-author verifier.
- [~] At least one end-to-end domain task executed and logged in LOG.md: `LOG.md` `## Round 74`
  (IME composition, 9 + 1 + 1 + 3 cold runs).
- [~] Instructions executable by an agent without oral context: R74Exec1/R74Exec2 ran the driver and
  counter from the spec alone (`w1/R74Exec1/report.md`, `w1/R74Exec2/report.md`).
- [~] No cross-domain bleed (PROVINCE.md still accurate): `PROVINCE.md` untouched. R74Connector found
  overlap none (`w1/R74Connector/report.md`).

Stale-lane: respawn-per-round driver; no other mission of this lane is open.
Tool installs: none (RULES.md read; pacman untouched). No seat reported an install.
Open L0 questions: none new; `tabi | round-57` (register correction) stays open.
