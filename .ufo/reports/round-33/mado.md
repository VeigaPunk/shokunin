# mado — round 33 report (hyaku inline campaign, attempt 1)

Identity: `Kimi fresh L1`. Lane tip (measured, pushed): `69f72100bee31a60b811f8fbbe7796db883e17b3`
on `master` (`jj-lane.sh state`: `local=69f72100 remote=69f72100 ahead=0 behind=0`).
Round-start tip: `de8fe248579520ee9af0f6a6f2db9d116bd55aeb`. This report does not edit the
filed round-32 report and does not rewrite round-32 predicates.

## Work performed

Two new claims, frozen in `.ufo/waves/round-33/registration.md` before any corpus append
(landed `9a46ccf3282117f960b8d53cd71599a91f388ee3`). They are not a re-score of round 32.

- **C1 — coverage.** A new surface, the Waybar event-socket client and the compositor's
  64-event removal, measured by `PRED-C1-r33-v1`. The round-32 IPC entries stay landed and
  are not this claim.
- **C2 — calibration** (tied for lowest: every scored axis is 1.0, and a capability entered
  in round 32, so the stagnation nudge does not waive). The published round-32 C1 row must
  match a re-run of the frozen round-32 counter.

Work items:

- Pre-data controls scored before any corpus append — `.ufo/waves/round-33/controls/RECEIPT.md`.
  Skip-the-work trees print `TARGET_MISSED`. A golden scratch tree prints `TARGET_MET`.
  An extra `source:` line still prints `TARGET_MET` (the round-32 false-negative does not recur).
- A wave-1 critic then built a symlink crib that the frozen counter accepts
  (`.ufo/waves/round-33/w1/reports/CriticC1Junk.md`, tree kept at
  `.ufo/waves/round-33/scratch/CriticC1Junk/`). The entries were not appended. The predicate
  was not rewritten after seats scored it.
- A scratch copy `.ufo/waves/round-33/c1/count-symlink-fix.py` rejects that crib
  (`TARGET_MISSED`) while the frozen counter prints `TARGET_MET`
  (`.ufo/waves/round-33/controls/c1-symlink-fix-demo.txt`). The frozen counter was not replaced.
- C2's correction line was appended to `SCORECARD.md`, not written over the false row.
  Re-run after that append: `claim_mismatch=0 ... verdict=TARGET_MET` exit 0.
- `quality/check-axis-scores.py` no longer treats a quoted marker as the publication and
  no longer cuts the window at 400 characters. Re-measured after the repair: base
  `256222890d935212874a09751ff9b7869943c2d7` still `mismatched=2` exit 1; tip
  `d9ed38166cc3be8ef4c52b41d66ad94010feb047` still `mismatched=0` exit 0. Selftest
  `18/18`. The gate is registered in `SKILL.md`.
- Round-32 K2 controls reproduced in a sandbox clone of `d9ed3816` and committed at
  `.ufo/waves/round-32/c2/controls/k2-a.txt` (`mismatched=3` exit 1), `k2-b.txt`
  (`mismatched=0` exit 0), `k2-c.txt` (`mismatched=1` exit 1).
- Five inherited round-30 paths re-verified (scout report `ScoutRound30.md`, not a blind
  sweep) and committed: they are real late seat reports. Revert would drop the only record
  of the mid-wave instrument churn.
- Sources S190, S191, S197 re-opened 2026-10-24. Digests match the frozen file. S189's
  queue-cap quote is at line 169 of the already-committed fetch. Staged line ranges for
  S190 do not cover the buffer (scout disagree on ranges, agree on identity).

## Landed changes

| Commit | Change | LOG.md tie |
|---|---|---|
| `9a46ccf3282117f960b8d53cd71599a91f388ee3` | frozen predicates, counters, fetch bytes, pre-data control receipts, collision guard | round-33 LOG entry |
| `d40b35f90ad8bf630ad9404d25aeee1d9737f300` | SCORECARD correction line, gate locator repair, SKILL registry rows, lesson, K2 receipts, five round-30 reports | round-33 LOG entry |
| `69f72100bee31a60b811f8fbbe7796db883e17b3` | wave-1 spec, taskCall, dispatcher, 31 seat reports, critic junk tree | round-33 LOG entry |

Lane commits carry `mado-shokunin <mado@shokunin.local>` through `scripts/hyaku/jj-lane.sh`.
The `landed` lines above are the citable hashes. A seat's 547 MB `ExecK2Receipts` scratch
clone was not committed.

## Before → after measurements

**C1 — coverage. Honest stop.**

```sh
python3 -I .ufo/waves/round-33/c1/count.py --root . --frozen .ufo/waves/round-33/c1/frozen.json
```

- Before and after (tip `69f72100bee31a60b811f8fbbe7796db883e17b3`): `closed_entries=0 closed_rows=0 open_cites=4 verdict=TARGET_MISSED` exit 1. The entries were not appended after the counter was killed.
- Frozen counter on the critic's symlink crib: `closed_entries=2 closed_rows=4 open_cites=0 verdict=TARGET_MET` exit 0.
- **Verdict: unprovable.** The kill rule is not a certification. The target was not narrowed and the predicate was not rewritten.

**C2 — calibration. Target met.**

```sh
python3 -I .ufo/waves/round-33/c2/count.py --repo . --scorecard SCORECARD.md
```

- Before (no verdict line): `claim_mismatch=1 reason=absent verdict=TARGET_MISSED` exit 1.
- After (tip above): `claim_mismatch=0 reason=match published=7 measured=7 verdict_word=honest-stop rev=d9ed38166cc3be8ef4c52b41d66ad94010feb047 verdict=TARGET_MET` exit 0.
- A junk line `cited_entries=3 verdict=target-met` prints `published=3 measured=7 verdict=TARGET_MISSED` exit 1.
- **Verdict: target met.** This does not claim that round 32 met its target. The measured 7 is the frozen round-32 counter.

## Sources & frontier

Census, both ends, exit 0:

```sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin mado
```

- before: exit 0, `mado ok`, 190 rows, seven pre-existing `W04` warnings.
- after: exit 0, same 190 rows, same seven `W04` warnings. No row appended.
- Rows added: 0. Rows touched: none. Frontier rows advanced: none.
- Sourced claim: none landed. C1 was the candidate and was killed before append. That is a conformance defect, recorded here, not hidden.
- **Assimilation: opened and refused append.** One theme examined (Waybar as an event-socket client). Province review marked both staged entries IN. They were not appended because the only counter that would score them also scores a symlink crib, and that counter was not rewritten after seats scored it. Flip is in `corpus/lessons/round-33.md`. Content reject: `two-literature-drift-r26.md` (outside province; tier-C sole support). Quarantine: 13-row slice re-derived; S189, S201, S205 hand-checked PRESENT; S189's register mark is a false negative and the row was already adopted in round 32 after that cleared-then-adopted flow; the other slice rows stay unappended. `considerthese/2026-10-24.md` proposal 5 mined, file not edited.
- Id collision: reg 190, staged 132, collisions exactly the five rows round 32 already adopted (S186–S189, S196). S190, S191, S197 do not collide. Indented `  | S002 |` fixture is nonempty; column-zero extractor is empty.
- Mistake mined: `corpus/lessons/round-33.md` §Mistakes. The symlink-crib fix is shown able to fail. The frozen counter was not replaced.

## Trend verdicts

- **expansion — unchanged.** No knowledge entry and no registry row was appended. The round-32 IPC entries remain. The examined theme was not moved into core.
- **quality — improved.** The false "target met" row was corrected by append, not rewrite. The axis-score locator no longer shadows on a quoted marker, and the round-32 before/after measurements still hold. No admitted entry failed a re-check, because none was appended.
- **discernment — improved.** The critic's kill was recorded and the predicate was not laundered into a target-met row. A fix was shown able to fail without being substituted for the frozen rule. No `QUALITY.md` criterion was added: that would move the round-31 resolved-active count and stale the published calibration row.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources → the gate-registry rows added this round are executable commands, not a new decision table. Evidence: `SKILL.md` section "Round 33 — published-axis gate and claim-verdict gate". Asserted by the author.
- [~] At least one end-to-end domain task executed and logged in LOG.md → the calibration correction was executed and logged. The coverage append was refused. Evidence: `LOG.md` round-33 entry and the C2 command output above. No named non-author verifier.
- [~] Instructions executable by an agent without oral context → the wave context carried absolute paths, the write bound, the pacman pause, and the frozen predicates. 31 seats returned a report. Evidence: `.ufo/waves/round-33/w1-spec.json`. Asserted by the author.
- [~] No cross-domain bleed (PROVINCE.md still accurate) → `two-literature-drift-r26.md` was refused again; the two examined entries were marked IN and not appended. Evidence: `.ufo/waves/round-33/w1/reports/ReviewProvince.md`. Asserted by the author.

## Round shape, seats, repairs

**Shape: one v1 wave, 32 seats, band 32–64, policy `scripts/hyaku/ufo-wave-policy.json`.**
Validator `plan`: `counts.spawn=32`, `dispatch.calls=1`, exit 0. No wave 2: the killed
counter was the finding, and a second wave would have scored a rule that seats had already
killed. No residual task call.

- Role mix: scout 7, reviewer 6, executor 5, scribe 4, critic 4, connector 2, revenger 1,
  sentinel 1, mutation-tester 1, simplifier 1. Attack roles as named in the prompt
  (reviewer, critic, mutation-tester): 11/32 = 34.4%. Counting revenger and sentinel as
  r32 did: 13/32 = 40.6%. Either reading is above 25%. `planner` is the L1.
- **Host mapping:** this seat has no AgentSwarm tool. The validated `taskCall` was one
  batched launch of 32 concurrent `omp -p` processes (`dispatch-w1.sh`). The parent stayed
  alive until `wait` returned. The 600-second background timeout was not used
  (`disable_timeout`). Slot: `granted lane=mado wave=r33-w1 seats=32 live=28 pending=0 cap=256`,
  released after settlement.
- **Dispatched: 32. Reports: 31. Dead seats: 1.** `ScribeLesson` exit 1, log
  `Working...` / `Deadline exceeded`, no report. Not replaced.
- A seat wrote a 547 MB clone under `.ufo/waves/round-33/scratch/ExecK2Receipts`. It was
  not committed. The K2 receipts in the lane are the L1 sandbox runs, not that clone.

**Round-32 routed defects, dispositioned here:**

1. False SCORECARD C1 row — correction line appended. Row not rewritten.
2. Report timeline — erratum, not an edit of the filed report. The data commit is
   `f5910876` at 20:22:50, not 20:05:38. `20:05:38` was the collision-guard commit
   `50e6a8f`.
3. "187 MB" — not supported. This lane re-measured `git ls-tree -r -l f5910876` of
   `.ufo/waves/round-32` as 893 blobs / 17,789,566 bytes. The closure measured committed
   scratch as 11.6 MB / 554 blobs and the `48f9fe09` deletion as 130 files. This lane
   confirms the deletion is 130 files. None of those figures is 187 MB.
4. Gate unregistered — `mado-axis-scores` and `mado-r33-claim-verdict` rows added to
   `SKILL.md`.
5. K2 receipts missing — committed at the path the round-32 registration named.
6. CriticC2 dead attacks — locator ignores a marker preceded by a quote or backtick;
   window is 2000 characters; navigation and operability perturbations are in the
   selftest. Round-32 before/after did not move.
7. Five round-30 paths — re-verified and committed in `d40b35f`. Not a blind sweep.
8. Budget note — the round-32 report's "~35 minutes over" does not match the watchdog
   span 19:56:38→20:33:30 (36m52s), which is under `ROUND_MAXTIME=170m`. The note was wrong.
9. Hash `25622288` — unresolvable. The full hash is
   `256222890d935212874a09751ff9b7869943c2d7`, named in the correction.
10. Omitted commits — `b1b740d` (id-collision guard) and `50e6a8f` (ExecCollisionGuard
    report) are lane commits between the round-start tip and `f5910876`. The round-32
    report's commit list skipped them.
11. S189 wording — round 32's "no quarantined row was appended" was imprecise. S189 was
    a quarantine-slice row, hand-checked PRESENT, then adopted. This round's hand-check
    again found the quote present. The register's payload-absent mark is a false negative.
12. Missing pre-freeze junk control — this round scored junk and do-nothing controls
    before data. A later seat showed a symlink crib the first junk tree did not cover.
    That kill is the honest stop, not a rewritten predicate.

## Extras

- **Stale-lane:** none. Respawn-per-round. No round 34 was started.
- **L0 questions:** none appended.
- **Tool installs:** none. Pacman stayed paused. No host service was restarted.
- **Misroot sweep:** `git -C /home/vgpnk/Projects/shokunin status --porcelain` showed driver
  files and other lanes' artifacts. No mado round-33 file was at the fleet root. Nothing
  of another lane was touched.
- **Untracked left in the lane:** the 547 MB `ExecK2Receipts` scratch tree, and the
  pre-data control scratch trees under `.ufo/waves/round-33/controls/` other than the
  receipt text files. Named, not swept.
