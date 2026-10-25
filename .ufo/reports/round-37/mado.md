# mado — round 37 report (attempt 2)

Lane repo `/home/vgpnk/Projects/shokunin/mado-shokunin`, branch `master`, base
`b4e47e980bfb0cbc8a4e788f59a41db858751fd8`, final lane hash
**`372a3efd82c22fdc0e6291d82686cc2f5cb4d194`** (pre-report gate:
`git -C /home/vgpnk/Projects/shokunin/mado-shokunin ls-remote origin refs/heads/master` →
`372a3efd82c22fdc0e6291d82686cc2f5cb4d194	refs/heads/master`).

## Work performed

Declared claims (2), frozen in `.ufo/waves/round-37/registration.md` (v1 `8f0a9e3`, re-frozen v2
`893a8aa` before any data):

- **C1 — coverage** (assimilation + sourced): two knowledge entries land on a new edge class under
  the held IPC contract — what Hyprland does to an event client that stops reading, and whether a
  removal is observable on this host.
- **C2 — operability** (capability acquisition): `tools/mado-eventq.py`, a read-only census of the
  compositor's event-socket subscribers.

Lowest-axis rule: every published axis tied at its maximum at base (`navigation 50/50`,
`calibration 48/48`, `operability 12/12`, `MADO_AXIS: checked=3 mismatched=0`,
`.ufo/waves/round-37/receipts/axis-base.txt`), so each is a lowest axis; C1 works coverage. The
stagnation nudge does not apply (capabilities entered in round 36). Attempt 1's draft calling
calibration "the lowest" is withdrawn (registration § Lowest-axis rule).

Work items:

- **Freeze, then a self-caught re-freeze.** Scoring my own v1 controls with the cheapest-control
  rule showed the v1 golden control was a token-only stub that met C1 (`admitted=2/2`) and that
  C2's live clause trusted a hand-writable receipt. Both counters were re-frozen as v2 before any
  seat ran (`893a8aa`; `receipts/controls.txt` v1 12/12, `receipts/controls-v2.txt` 13/13, where the
  old golden is now `c1-token-stub` → `TARGET_MISSED`).
- **Sources re-opened by the L1** (all 2026-10-25; digests in `corpus/lessons/round-37.md`
  `## Gate`): S189 EventManager.cpp and S201 Waybar backend.cpp (byte-identical to the lane's
  round-32/34 fetches), S212 Waybar workspaces.cpp, S214 Logger.cpp, S215 ConfigValues.cpp,
  S216 Compositor.cpp, S217 Logger.hpp (Hyprland v0.56.2 `efb50993…`, the host's exact commit),
  S213 host log-channel receipt (`.ufo/waves/round-37/fetch/`).
- **The central finding** (`corpus/knowledge/event-queue-observability-r37.md`): both removal
  markers ("Socket2 fd N overflowed event queue, removing", "… failed writing event") are
  core-logger lines; `debug:disable_logs` defaults to true (S215 `:629`) and reads 1 here (S213);
  the formatted log call returns before formatting while it is set (S217 `:23-24`, S214 `:48`).
  The session log's 21 core lines end at line 21; the journal and `hyprctl rollinglog` carry none.
  Zero marker counts on this host are a **null channel**.
- **C1 entries.** `corpus/knowledge/event-delivery-limits-r26.md`: the package entry re-grounded,
  with every sentence checked against bytes and five corrections (ids re-pointed by document; Waybar's
  `fgets` reads 1023 characters and a long event splits; removal needs the send buffer full and
  then 64 more events; "logged compositor-side" is false on a default install; the custom-module
  producer runs on its own thread). The second entry is lane-authored (above). Commit `3f42425`.
- **C2 tool.** Two independent executor candidates (`ExecEventqA`, `ExecEventqB`) both met
  10/10 in sandboxes; A was adopted after an out-of-fixture probe (reversed row order, missing
  `users`, two-tuple `users`, spaces in names). Live, read-only: `waybar` pid 935660 fd 21 and
  `socat` pid 2293 fd 5 on `.socket2.sock`, 0 markers, `markers_observable=no`
  (`.ufo/waves/round-37/receipts/eventq-live.txt`). An independent `/proc` census agrees on the two
  server inodes (`receipts/eventq-live-proc-crosscheck.txt`, `OVERALL: AGREE`).
- **Mined mistake, fixed and shown able to fail (M37-4).** Four lane gates inherited `GIT_*`:
  under `GIT_WORK_TREE=/dev/shm` the round-36 pointer gate read `inherited_dirty=8` (true 0);
  under `GIT_DIR` the axis gate read `mismatched=2`. Red before:
  `.ufo/waves/round-37/w1/scratch/ExecPointerEnv/red-green.txt`, `sweep.txt`. Green after:
  `receipts/git-env-green.txt` (byte-identical output plain and under both variables; plain
  output digests equal to the pre-fix ones). Residual `RevGitEnvFix`: removing the scrub restores
  the red; the scrub is the only delta.
- **Round-36 spot-check routed defects R1–R5**: R1 (untracked `DistillerFindings.md`) committed
  at `80b83c8`; R1–R4 errata in `LOG.md` `## Round 37` → `### Round-36 errata`; R5 (worktree
  observable) became QUALITY criterion 63. Criterion 62 (a zero count needs a positive probe on
  the same channel) comes from M37-2.
- **Attacks that landed against my own work, recorded rather than hidden:**
  - `CritAxisClaim`: the frontier row I first cited is the Walker launcher's socket item, so C1
    moves a new edge class and no frontier row (registration `## Erratum 1`; README and the
    entries' `ground:` lines corrected before the data commit).
  - `CritC1Cheap` / `RevC1Code`: C1 v2 is still reachable by a 19-line self-receipt crib.
  - `RevC2Code` F1/F4/F5 and `CritC2Cheap`: C2's live clause is reachable with a snapshot built
    from the counter's own fixture rows, and `lagging`/`--expect-client` lack a discriminating case.
  - The counters were frozen and seats had already scored, so the rule was not changed
    (kumitate r42). The limits are in the verdicts below and routed as M37-5.
  - `CritEntryE2`: four wording defects in E2, corrected at `f6ae0c3` and logged in LOG.md.

## Landed changes

All through `scripts/hyaku/jj-lane.sh`; each `landed <hash>` line was printed after remote
verification.

| Commit | What | LOG.md entry |
|---|---|---|
| `8f0a9e3f78120d00e5e9f32c909618d549f976b4` | freeze v1: registration, both counters, controls 12/12, source receipts, assimilation scratch | `## Round 37` (Freeze discipline) |
| `893a8aadc80ab19bc163e366d674a8ac32feacd0` | re-freeze v2 before data (Amendment 1), controls 13/13, before receipts | same |
| `80b83c856b8cad60b88e63d8d3ab06b1d8dfea5b` | inherited round-36 seat report (R1); wave-1 spec, prompts, dispatch, registry | `### Round-36 errata` R1 |
| `3f424257a1ea69cd2655770259ba00b423293f4f` | **data**: two entries, rows S212–S217, README map rows + route, QUALITY 62–63, lesson, `tools/mado-eventq.py` + live receipts, GIT_* scrub in four gates, Erratum 1 | `## Round 37` (C1, C2, M37-4) |
| `f6ae0c36ff4282e0e605e75212358890223eeafc` | records: LOG and SCORECARD round-37 sections, errata, residual E2 corrections, after receipts, wave-1 and residual reports and scratch | `### Round 37 — residual-call corrections …` |
| `372a3efd82c22fdc0e6291d82686cc2f5cb4d194` | tip receipts and the last seat report | (evidence only) |

Inherited state: attempt 1 left only an empty `.ufo/waves/round-37/assimilation/` directory, which was
reused and filled. The untracked round-36 `DistillerFindings.md` is lane-authored and was committed
(R1). Files I did not author and left untouched: `corpus/lessons/round-3{3..6}-verifier-spotcheck.md`.
The lane tree is clean at the final hash (`git status --porcelain` empty).

## Before → after measurements

| Claim | Counting command | Before (base `b4e47e9`) | After (data `3f42425`; re-run at records tip `f6ae0c3`) |
|---|---|---|---|
| C1 | `cd /home/vgpnk/Projects/shokunin/mado-shokunin && python3 -I quality/counters/c1-r37-event-ground.py --repo . --rev <rev>` | `PRED-C1-r37-v2 admitted=0/2 verdict=TARGET_MISSED` exit 1 (`receipts/before-c1-v2.txt`) | `admitted=2/2 verdict=TARGET_MET` exit 0 (`receipts/after-c1-v2.txt`, `after-c1-v2-records.txt`) |
| C2 | `cd /home/vgpnk/Projects/shokunin/mado-shokunin && python3 -I quality/counters/c2-r37-eventq.py --repo . --rev <rev>` | `fixtures=0/10 readonly=0 live=0 tool=absent verdict=TARGET_MISSED` exit 1 (`receipts/before-c2-v2.txt`) | `fixtures=10/10 readonly=1 live=1 tool=present verdict=TARGET_MET` exit 0 (`receipts/after-c2-v2.txt`, `after-c2-v2-records.txt`) |

Do-nothing and crib controls before data (`receipts/controls-v2.txt`): C1 do-nothing, package copy,
junk quotes, wrong digest, ungrounded token, unindexed, not-mined and token stub all score
`TARGET_MISSED`, and the golden-v2 scores `TARGET_MET`. C2 do-nothing, always-clean stub, grep-only stub
and socket-importing stub all score `TARGET_MISSED` (best 2/10). Axis table at the records tip:
`MADO_AXIS: checked=3 mismatched=0` (navigation 52/52, calibration 50/50, operability 12/12;
`receipts/axis-records.txt`).

Harm watch (residual `RevHarmAfter` against wave-1 `RevHarmBefore`): `MADO_SELFTEST: 460/460`;
`tools/mado-verify.sh` sha256 `050efc72…6703f1` unchanged; index 52/52, rows `errors=0 warns=3`
(the same 3); census identical; 15 config-file hashes identical (combined `89e214b8…ac3195`); 0
Hyprland coredumps; zero deleted files in `b4e47e9..3f42425`. **Not harmed**, all three axes.

## Sources & frontier

- Census command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin mado`.
  - Round start: seven pre-existing `W04` (S030, S042, S045, S097, S119, S120, S121), `mado ok`,
    **exit 0** (`receipts/census-before.txt`).
  - Round end: identical seven `W04`, `mado ok`, **exit 0** (`receipts/census-after.txt`; re-run at
    the records tip, exit 0).
- Rows **201 → 207** (`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`).
  - Added by tier: **A +6** (S212–S217: code ×5, own-work ×1), all `mined`, opened 2026-10-25.
  - Touched old→new: S189 `used-by` + `event-delivery-limits-r26.md`, `event-queue-observability-r37.md`;
    S201 `used-by` + `event-delivery-limits-r26.md` (lesson `## Gate`). No `status` or `recheck` changed.
- **Frontier:** a new edge class under the held IPC contract moves onto sourced ground (event
  delivery to a stalled client, and host observability as a measured negative); no Frontier row is
  moved (Erratum 1). Still open: no event was observed and no client stalled, the send-buffer size,
  and any removal before this reading.
- **Sourced claim:** both C1 entries rest on rows opened this round (S212–S217) and on S189/S201,
  re-opened this round.
- **Mined mistake:** M37-1…M37-5 in `corpus/lessons/round-37.md` `## Mistakes`. The M37-4 fix is
  shown able to fail.
- **Assimilation: one theme (event-socket delivery), 1 admitted, 2 refused.**
  - Admit `event-delivery-limits-r26.md` (re-grounded).
  - Refuse `event-queue-host-measurement-r28.md` and `event-queue-journal-measurement-r29.md`
    (null channel; flip: `debug:disable_logs = false` plus a re-count).
  - Id lists: reg-ids **201** (S001–S189, S196, S201–S211); staged-ids **147** (S203–S349);
    collisions **9** (S203–S211).
  - Guard proof: an indented `  | S002 |` scratch row is caught by the 0–3-space pattern (n=1) and
    missed by the column-zero one (n=0).
  - Renumber map, by document: package S214 (workspaces.cpp) → S212; merge-note S187 → S189;
    S188 → S201; staged S226 and S242 refused, not appended. No staged row was appended as-is.
  - Scratch validation: wave-1 `ScribeRows` mirror, `validate --file` exit 0.
  - Quarantine: the register's `round1 S189` row (EventManager.cpp, payload-absent) was
    hand-checked and its quote is **present** at `:128` (the register's escaping caused the miss).
    The other 12 slice rows name documents no admitted entry cites; they stay unappended and unchecked.
  - Evidence: `.ufo/waves/round-37/assimilation/`.
- **considerthese:** `considerthese/2026-10-24.md` proposal 4 ("suggest the next desktop table"),
  implemented as data by `ConnFrontier` and landed in the lesson's `## considerthese` section.
  Ranked next surfaces: the config-option table, monitor rules, window/layer rules.

## Trend verdicts

- **expansion: improved.** Two admitted knowledge entries with `source:` rows `mined` on ground
  unheld at base (`git grep` for `MAX_QUEUED_EVENTS` / `debug:disable_logs` in
  `corpus/knowledge` at `b4e47e9` is empty), plus one new capability row. The counter shown
  crib-reachable means the C1 verdict rests on the residual re-checks:
  - `RevAfterC1`: all 13 OBS lines hold, and every Gate digest re-fetched equal.
  - `CritEntryE1`: no FAIL items.
  - `CritRefusals`: refusals hold, and the ids were re-pointed by document.
- **quality: improved.**
  - A runnable domain tool lands (10/10 fixtures, independent `/proc` agreement).
  - Four gates stop trusting the caller's environment (red → green).
  - The package entry is corrected in five places against bytes.
  - Harm watch is green on every axis.
- **discernment: improved, with named limits.**
  - Two package readings are refused on source-backed grounds that four independent channels
    confirmed (`ScoutPkgRefuse`: refusal survived on rollinglog, crash reports, coredumps and the
    journal).
  - My own v1 golden was caught as a stub before data.
  - A false frontier provenance was corrected (Erratum 1).
  - Limit: both frozen counters remain crib-reachable after the freeze (M37-5), reported rather
    than re-scored.

Per-axis: coverage **improved** (C1; instrument limit named); operability **improved** (C2;
instrument limit named); calibration **unchanged** as an axis score (50/50 at tip, MATCH);
freshness, depth and adjacency **unchanged** (not claimed; adjacency boundaries recorded in the
SCORECARD capability row). Exploratory claim: none.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources. This
  round's evidence: `corpus/knowledge/event-delivery-limits-r26.md`. SKILL.md itself is unchanged
  this round. No non-author verifier is named.
- [~] At least one end-to-end domain task executed and logged in LOG.md:
  `receipts/eventq-live.txt` (a live read-only census of the event socket) and LOG `## Round 37`.
  Dispatched seats are not outside-lane verifiers.
- [~] Instructions executable by an agent without oral context:
  `corpus/knowledge/executor-test-sufficiency.md` (historical). No new no-oral-context test this
  round.
- [~] No cross-domain bleed (PROVINCE.md still accurate): wave-1 `ConnOverlap` (no sibling
  contests the ground; five adjacencies routed in the SCORECARD capability row). PROVINCE.md is
  unchanged.

## Round shape and other required lines

- Shape: default, one v1 wave plus a residual call.
  - Wave 1: **38 seats** in one batched `task` call, validated under
    `scripts/hyaku/ufo-wave-policy.json`: reviewer 7, scribe 7, scout 8, executor 5, critic 5,
    connector 2, mutation-tester 2, sentinel 1, simplifier 1.
  - Residual: one ordinary `task` call of **8** seats (reviewer 5, critic 3) attacking the
    landed data commit.
  - Wave 2 was not dispatched. After integration, fewer than 32 distinct attack items remained,
    and padding is forbidden.
  - **Round total 46.**
- The §3 planner seat is held by the L1, since the validator rejects `planner`. The planning
  data-walk rode `ConnFrontier` and the scouts.
- Dead seats: **none** (46/46 completed). Capacity refusals: none.
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows no file written by
  a mado seat. The fleet root's tracked-file deletions and untracked files predate this round and
  belong to other writers; they were not touched.
- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
- Tool installs or updates: **none** (no seat recorded one; pacman untouched).
- L0 questions: none opened.
- Counter routing: the simplifier's P1/P3/P4/P5 proposals (`w1/reports/SimplifyCounters.md`) are
  not applied, because the counters are frozen. They are routed to round 38 with M37-5's v3
  counters.
