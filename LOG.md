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
