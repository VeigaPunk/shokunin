# kama — round 26 report

Lane: kama (local model serving and endpoint health). Round 26, attempt 1,
dispatched 2026-10-23T03:13Z (orchestrator session note; watchdog line
`2026-10-23T00:13:17-03:00 launch kama round=26 ... attempt=1`, no
`lane-dead-no-report` line, so nothing was inherited from an earlier attempt).
Base `1560e4d83f42b04f40336357de6f9637eafa0f4b`. Lane tip at report time:
`eb09e742bd10b62a5e14d93dd96318492765b97f` (`jj-lane.sh state`: local = remote,
ahead 0, behind 0, tracked 0, untracked 0). One commit in the range is the
operator's, not the lane's: `c5acd52` "considerthese: 2026-10-22 daily
reflection" (João Pedro Veiga, parent = base).

## Work performed

Declared claim (one; `.ufo/waves/round-26/preregistration.json`, pre-data
amendments A0 and A1):

- **C1 — depth (lowest axis, 7).** Surface: a new SKILL.md section
  "## Round-26 live error signatures" of llama-server b11755 error signatures,
  each reproduced live on the lane fixture, verbatim in a pinned 704366d source
  line and cited by a new SOURCES row. Counter
  `.ufo/waves/round-26/count-c1.py` (sha256 `6501737c…6588`), target
  `counted >= 12`. The rejected streak (rounds 23-25) worked calibration and the
  report-landing auditor; this round worked depth on the serving runtime.

No exploratory claim. Repair-first items (round-25 outside spot-check routed
defects 1-7) are repair work, not claims.

Work items:

- Repair-first: read `corpus/lessons/round-25-verifier-spotcheck.md` and
  `round-24-verifier-spotcheck.md`; dispositions in `corpus/lessons/round-26.md`
  §Routed defects. Defect 1: 42 late round-25 `git status` entries (220 added,
  2 modified, 1 deleted files) committed at `a4a159c3`, plus a 1.4 MB log the
  directory commit skipped, committed at `7e5ff9b5`. Defect 2: KQ36 "landed tip"
  qualification (`corpus/QUALITY.md`, appended) and the round-25 §Mistakes
  row-2 erratum (`corpus/lessons/round-25.md`, appended). Defect 3: KQ31
  supersession rows S131-S135. Defect 4: `corpus/knowledge/context-capacity.md`
  errata (appended). Defect 5: raw-hash binding in
  `.ufo/waves/round-25/count-c2.py` (wave-1 ExecC2RawBinding; the unpatched
  counter accepted all 5 receipt mutants of MutationC2Receipts; wave-2
  MutC2Binding: the landed counter rejects all 5 and kills all 3 binding-code
  mutants; open limit: cell values are still read from the receipt). Defect 6:
  SCORECARD round-25 trend correction (appended in the round-26 section).
  Defect 7: each wave's gate reservation released only after every seat of that
  wave returned (release lines below). Defect 8: C1 works depth.
- Freeze before data: counter, preregistration, pinned sources
  (`.ufo/waves/round-26/sources/llama.cpp-704366d/`, 13 files, then 3 more after
  wave 2), before receipt `before/c1-base.out` (`registered 0 counted 0 target
  12 met False`). A0 (`a12850c5`, before any control or data seat): clause (g)
  hardened against splitting one message into rows.
- Pre-freeze control call (6 seats): KamaR26CtlAllFalse **broke** the A0 counter
  (12 of 14 with CLI help text after an invalid option value;
  `controls/KamaR26CtlAllFalse/REPORT.md`). A1 (`a23c0e04`, before any data
  seat) excluded `--help`/`--version` text; the same patch scores 0 of 14
  (`controls/A1-rescore/invalid-flag-usage-A1.out`). Three critic control seats
  died and two mutation-tester control items were refused; the L1 ran the
  do-nothing, cosmetic, headline-only, junk, generic-string, fabricated-source
  and fake-binary controls itself (`controls/L1-dead-seat-controls/`): 0, 0, 0,
  0/14, 0/14, 3/14 (three genuine faults), 0/14 and could-not-evaluate (sha pin).
  The echo shortcut was **not** covered before data (see Gate and Mistakes).
- Wave 1 (36 seats): 18 fault-family executors and a fault-survey scout found
  candidates (57 executor entries in `w1-build/out/*/candidates.json`; 3 more
  only in `ScoutFaultSurvey/survey.md`); scribes drafted SOURCES rows, SKILL
  prose, routed repairs and mistakes; a reviewer found counter limits F1-F14
  (`w1-build/out/ReviewerCounterCode/findings.md`), including F4 (at most 19
  runnable rows). The L1 registered 17 rows (`registry/error-signatures-r26.json`)
  and rejected or held back the rest with reasons (lesson §Gate).
- Integration (`7f84cd0e`): SKILL section with 17 rows E26-01..E26-17, SOURCES
  S114-S130 (one per signature line), S131-S135 (supersessions), lesson,
  SCORECARD, LOG, `corpus/README.md` frontier disposition, mined-mistake tool
  `tools/prereg-time-check.py` (exit 1 at `a4a159c3` and `a12850c5`, exit 0 at
  `f071209a`; `final/prereg-time-check.out`).
- Wave 2 (34 seats): one attack seat per E26 row (re-run twice live; F1-F3
  checks; source re-open; prose check), counter re-run at the tip, five source
  re-opens, Gate-quote and census check, axis/harm and shortcut critics,
  mutation of the count-c2 binding and of the timestamp tool, applied-repair,
  lesson, SKILL-prose and self-assessment reviews, misroot sweep, adjacency
  connector. Corrections landed at `fd48f9a3` (row prose for 15 rows, header,
  lesson, SCORECARD/LOG); signature, id and source cells unchanged.
- **Post-data finding that decides C1:** wave-2 critic CriticShortcutRows met
  the frozen counter from the base tree with no error knowledge:
  `registered 12 counted 12 target 12 met True`
  (`.ufo/waves/round-26/w2-falsify/out/CriticShortcutRows/`), by echoing source
  literals through `server-common.cpp:1375` with `\u00XX`-escaped request bytes
  (counter limit F2). It judged none of the 17 landed rows to be of a shortcut
  type; every row attack seat that returned re-ran its row live.
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain`
  shows no untracked file naming kama or round 26 and no
  `.ufo/waves/round-26` at the fleet root; four wave-2 seats (AttackE2616,
  AttackE2606, ReopenS131, ReopenS132) had first written their report there and
  moved it into the lane themselves (lesson §Mistakes). The L1's own
  `/tmp/kama-r26-frozen.py` (an A0 counter copy) was deleted. No llama-server
  left running (`pgrep -af llama-server`: none).

## Landed changes

All through `jj-lane.sh`; LOG.md "Round 26" entry covers every item.

| Commit | What |
|---|---|
| `a4a159c39967e88a89b0808dcd201c79c474efd1` | freeze: counter, preregistration, pinned sources, before receipts; round-25 late paths (defect 1) |
| `a12850c5cbc1013e60cc5bba2d6800d1cd634499` | pre-data amendment A0 |
| `f071209a0f956680b5722e09242e784a1644e216` | preregistration timestamps corrected (L1 clock guesses) |
| `a23c0e042114016a909eb15173aa6df74b5b7eb0` | control receipts, pre-data amendment A1, wave-1 spec |
| `84ec083bb9697aa1bc6db4cee86ad73d8f9eb8ef` | wave-1 dispatch record |
| `7f84cd0e7662432b7b93e7586f86a40b06e5fdae` | C1 integration (SKILL, registry, S114-S135), repairs 2-6, lesson, LOG, SCORECARD, README, `tools/prereg-time-check.py` |
| `7e5ff9b5454dd27f0520cb36a3cbc3a995e48162` | refused control outputs marked held; skipped round-25 log |
| `3550523024f24b61460164e400d6f63fae0c0928` | landed-tip receipts at 7e5ff9b5 |
| `f4066979096e3452ae731c0e09e50155c6d8258a` | LOG candidate count; wave-1 final outputs |
| `fd48f9a3b7ca9dc7be342d9e7ce56844f0a21e50` | falsify-wave corrections, 3 snapshot files, wave-2 evidence |
| `eb09e742bd10b62a5e14d93dd96318492765b97f` | final landed-tip receipts at fd48f9a3 |

`git diff --stat fd48f9a3 eb09e742 -- SKILL.md registry corpus
.ufo/waves/round-26/count-c1.py .ufo/waves/round-26/sources` is empty, so the
fd48f9a3 receipts measure the bytes at the lane tip (KQ36 as qualified this
round).

## Before → after measurements

| Claim | Counting command | Before (base `1560e4d8`) | After | Measured commit |
|---|---|---|---|---|
| C1 depth | `python3 .ufo/waves/round-26/count-c1.py --out <receipt>` (from the tree root, under `flock /fast/scratch/hyaku/kama-r26/counter.lock`) | `registered 0 counted 0 target 12 met False not-counted []`, exit 0 (`before/c1-base.out`; re-run by wave-2 RerunC1AtTip, `w2-falsify/out/RerunC1AtTip/`) | `registered 17 counted 17 target 12 met True not-counted []`, exit 0 (`.ufo/waves/round-26/final/c1-final-tip.out`) | `fd48f9a3b7ca9dc7be342d9e7ce56844f0a21e50` (also `7e5ff9b5` and `f4066979` by RerunC1AtTip, same line) |
| shortcut control on the same counter (post-data) | same command in a base-tree extract with 12 echo rows | — | `registered 12 counted 12 target 12 met True` | base tree `1560e4d8` + scratch rows (CriticShortcutRows) |
| KQ36 re-run of the round-25 C2 command (repair 5) | `python3 .ufo/waves/round-25/count-c2.py` | `registered 14 observed 14 bound True missing []` at base (unbound to raw files) | `registered 14 observed 14 bound True missing []`, exit 0, with raw-hash binding (`final/c2-kq36-final-tip.out`) | `fd48f9a3` |

**C1 verdict (author): target met under the frozen predicate, claim not
established.** A shortcut that skips the claimed work also meets the frozen
counter, so under prompt §9 the counter or target is wrong; the rule was not
changed after data. The 17 rows themselves held under the per-row wave-2
attacks (wording corrections only). No score promotion: depth stays 7
(SCORECARD round-26 row). The outside closure decides.

## Gate

Real rejects, each with its reason (full table in `corpus/lessons/round-26.md`
§Gate):

- `This server does not support metrics endpoint...` (server-context.cpp:5304):
  rejected although the counter would accept it; the lane already held it in
  round-16/18 wave evidence (CriticAxisFit's caveat on clause b).
- `"authentication_error"` (ExecApiKey) and `invalid_request_error`
  (ExecSlotActionNoPath): rejected as error-type labels, not signatures; auth
  is kagi's scope.
- `exceeds the available context size (`, `couldn't bind HTTP server socket`,
  `error: invalid argument: `: rejected as already held in earlier wave
  evidence.
- Ten per-flag argument messages (ExecBadArgs): rejected, one validation pattern
  per flag.
- Router-model errors (ExecRouterModels, empty candidate list): unreachable with
  `-m`.
- Falsify finding rejected: AttackE2610 said the receipt's `tree=7e5ff9b5` is
  another commit's tree; `git cat-file -t 7e5ff9b5454dd27f0520cb36a3cbc3a995e48162`
  prints `commit`.
- Held back, genuine: 26 live-confirmed messages (incl. 17 chat-completions
  messages from ExecChatFormat), only because of the counter's 19-row limit.

## Sources & frontier

- Census command at round start and end:
  `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kama`.
  Start: exit 0, `kama ok`, W04 duplicate-URL warnings only
  (`.ufo/waves/round-26/before/census-validate.out`). End: exit 0, `kama ok`,
  W04 only, empty stderr (`.ufo/waves/round-26/final/census-validate-final.out`).
- Rows before → after: `git show <rev>:corpus/SOURCES.md | grep -cE
  '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'` → 113 at `1560e4d8`, 135 at
  `fd48f9a3`.
- Rows added by tier: 22, all tier A (S114-S130 code, mined, one per signature
  line; S131-S133 and S135 code and S134 docs, KQ31 supersession rows). Each
  was opened this round from a fresh fetch at 704366d; URL, access date
  2026-10-23 and a ≤25-word located quote per row are in the lesson §Gate
  (wave-2 ReviewerGateQuotes re-checked S114-S130; ReopenS131-S135 re-checked
  the supersessions).
- Rows touched old → new: none. S106, S107, S109, S112 and S113 keep every cell;
  their corrections are new rows. Open row defects found by wave 2 (S134 teaches
  self-contradiction and line 168/170 citation, S133 anchor 1834 vs 1835, S135
  92 vs 93) are recorded in the wave-2 advice and routed to a later KQ31 row.
- Frontier advanced: live serving-runtime error signatures moved into SKILL.md
  core (README "Frontier disposition — round 26"); still frontier: router-mode
  errors, the 26 held-back signatures, the `--embeddings` SIGSEGV seen once.
- Sourced claim: C1's rows cite S114-S130, opened this round.
- Mined mistakes: `corpus/lessons/round-26.md` §Mistakes (false timestamp a
  third time, with `tools/prereg-time-check.py` shown able to fail; A0 counter
  met by a control before data; data dispatched without a shortcut receipt and
  the counter then met by a shortcut after data; counter limits F1-F14 found
  after data; the round's own false "before" statement; seat misroots).

## Trend verdicts

- **expansion: unchanged.** No coverage surface or capability was claimed; the
  new SKILL section deepens a surface the lane already owns.
- **quality: unchanged.** The 17
  rows are new, sourced and re-run live by separate seats, and 15 rows' prose
  was corrected by the falsify wave; but the claim's counter does not
  discriminate them from a shortcut, so the gain is not established by the
  round's own measure. No non-author `unprovable-but-better` judgment exists.
- **discernment: unchanged.** For: the A0 break caught and closed before data;
  rejects and hold-backs with reasons; a wave-2 calibration check found and the
  round corrected a false statement in its own SCORECARD/LOG. Against: the
  frozen counter is met by a post-data shortcut, and the shortcut receipt was
  missing when data was dispatched.

No axis is harmed at the final bytes in the author's reading: the false
"before" statement landed at `7f84cd0e` and was corrected at `fd48f9a3`
(CriticAxisAndHarm read the uncorrected HEAD as calibration-harmed and verified
the correction). The closure decides.

## Round shape, seats and holds

- Shape: default two v1 waves, plus one pre-freeze control call of 6 seats
  (counted in the round total). Round total **76** seats.
- Control call (6): critic 3, mutation-tester 3. Gate:
  `granted lane=kama wave=kama-r26-ctl seats=6` → `released lane=kama
  wave=kama-r26-ctl` after all 6 returned.
- Wave 1 (36, policy v1, validator `taskCall` plus `solutionSpace`): executor
  21, scribe 8, scout 2, reviewer 2, connector 1, critic 1, mutation-tester 1.
  Gate: `granted lane=kama wave=kama-r26-w1-build seats=36 live=29 pending=12
  cap=256` → `released lane=kama wave=kama-r26-w1-build` after the 36th seat.
- Wave 2 (34, policy v1): reviewer 15, scout 10, critic 6, mutation-tester 2,
  connector 1 (88% attack roles). Gate: `granted lane=kama
  wave=kama-r26-w2-falsify seats=34 live=48 pending=0 cap=256` → `released
  lane=kama wave=kama-r26-w2-falsify` after all 34 returned. No seat was
  cancelled at a deadline.
- §3 floor: planner = the L1 (the validator rejects `planner`); connector,
  ≥3 executors, scribe, scout, reviewer and critic are in wave 1.
- Dead seats (not replaced): KamaR26CtlDoNothing, KamaR26CtlJunk,
  KamaR26CtlNoReader — `Cloud Code Assist API error (429): Individual quota
  reached ... Resets in 59h6m24s` (gemini-4-argon-high, reset
  2026-10-25T14:27:28Z).
- Holds (provider refusal or safety switch; item ended, findings not evidence,
  not retried or rerouted): KamaR26CtlShortcut and KamaR26CtlCounterMutants
  (`Codex error event: This content was flagged for possible cybersecurity
  risk ... (code=cyber_policy)`), AttackE2617 (`Claude Opus 5.5 hit a safety
  filter, and the conversation was automatically switched to Claude Opus 4.8`).
  Their directories carry `HELD.md`.
- Routing: no `model` passed; roles routed by the host table.

## Open items at report time

- C1 admission is the closure's; the author's reading is honest stop (counter
  met by a shortcut).
- Next counter (round 27): per-row healthy control with the same argv, decoded
  request and file-content echo checks, port reuse, a pin on
  `libllama-server-impl.so`, a cleared environment; one committed receipt per
  control class before data.
- count-c2.py still reads cell values from the receipt (defect 5 limit).
- L0 questions: none added.
- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
- Tool installs: none by the L1; no seat reported an install.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources → `SKILL.md` "## Round-26 live error signatures" (E26-01..E26-17, S114-S130); no named non-author verifier of the box.
- [~] At least one end-to-end domain task executed and logged in LOG.md → `LOG.md` "Round 26"; `.ufo/waves/round-26/final/c1-final-tip.out` (17 live triggers on the pinned b11755 fixture); no non-author mark.
- [~] Instructions executable by an agent without oral context → the counter command in the SKILL section header and `registry/error-signatures-r26.json`; wave-2 seats re-ran rows from them; no non-author mark.
- [~] No cross-domain bleed (PROVINCE.md still accurate) → SKILL section "Cited, not absorbed" note (kagi, kengaku, tsukuroi, kumitate); wave-2 ConnectorAdjacency; no non-author mark.
