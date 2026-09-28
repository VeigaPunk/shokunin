# shokunin (main repo) — Scorecard

Axes owned by the `protocol` lane: **fleet-meta — protocol soundness + gate
integrity** (`MISSION.md` fleet shape; `scripts/shokunin-watchdog.sh`
`LANE_AXES[protocol]="fleet-meta: protocol soundness, gate integrity"`). The
`aggregator` lane's axes (cross-lane quality, mint/dormancy calls, corpus
review) are not scored here.

Every score is a claim: it carries the command that produced it and the tree
it was measured against. Baseline measured 2026-09-28 18:21 -03:00 at main
HEAD `0a30b44`; after-measurement re-executed 18:35 on the round-10 working
tree at HEAD `6a45ff2` (this file ships in the round-10 commit, so it cannot
cite its own hash — the report does).

| Axis | Score | Evidence pointer | Last change |
|---|---|---|---|
| gate-integrity | 6 (was 2) | Closure actuator landed and executed: 11/11 report-bearing rounds now carry a `MANIFEST.json` `rounds` entry (was 2/11), 58/58 terminated lane-rounds carry a correct terminal status (was 8/58), 0 rows contradict evidence under last-wins (was 5), 0 marker reports unrecorded (was 4). Metrics M1–M6 below. Still open: prompt fidelity 1/5 items and the driver's contentless-marker completion signal — both operator-side | round 10 |
| protocol-soundness | 6 (was 4) | Round-entry semantics defined for a per-lane-counter driver, marker-vs-report boundary, SSOT precedence, main-repo lane write scope + commit identity, `SCORECARD.md` in the file contract, mint bar stated once, ledger fallback named. Metrics P1–P4 below. Cost paid: `PROTOCOL.md` grew 387 → 576 lines (`wc -l`), so the concision sub-metric worsened; compaction is the round-11 move | round 10 |

## Metrics (before → after, with counting commands)

Gate integrity:

| # | Metric | Before | After | Command |
|---|---|---|---|---|
| M1 | report-bearing rounds with a closure entry | 2 / 11 | 11 / 11 | `python3 -c` over `MANIFEST.json` `rounds` vs `ls .ufo/reports/round-*/` — see the round-10 report §Closure for the exact script |
| M2 | terminated lane-rounds with a correct recorded terminal status | 8 / 58 | 58 / 58 | last-wins over `rounds[].lanes`; 58 = 66 dispatched (`.ufo/watchdog.log` launch/steer lines) − 8 live at `closed_at` |
| M3 | `rounds[]` rows contradicting durable evidence | 5 | 0 | round-1 kagi/aggregator, round-9 kake/kumitate/aggregator, each against a log line or report path |
| M4 | marker reports satisfying the driver's completion signal, unrecorded | 4 | 0 | `.ufo/reports/round-5/aggregator.md` (254 B), `round-7/kumitate.md` (122 B), `round-8/kengaku.md` (101 B), `round-8/kotoba.md` (120 B) |
| M5 | untracked dispatch-evidence prompt files | 8 / 58 | 0 / 58 | `git ls-files -o --exclude-standard .ufo/prompts \| wc -l` |
| M6 | child-lane reports missing the `SHONEN` heading | 41 / 45 | 41 / 47 (unchanged — lane debt, routed) | `grep -rLE '^#{1,6} *SHONEN' .ufo/reports/round-*/*.md \| grep -vE 'protocol\|aggregator\|AGGREGATE' \| wc -l` |
| M7 | child-lane contract items in the fleet-2 prompt template | 1 / 5 | 1 / 5 (operator-side, unchanged) | `scripts/shokunin-watchdog.sh` `lane_prompt()` heredoc; `grep -l SHONEN .ufo/prompts/*.md` → 1 file, a file-list mention |

Protocol soundness:

| # | Metric | Before | After | Command |
|---|---|---|---|---|
| P1 | mission-required artifacts ungoverned by `PROTOCOL.md` | 4 (`SCORECARD.md`, main-repo `LOG.md`, `.ufo/prompts` durability, axis-score evidence) | 0 | `grep -c SCORECARD PROTOCOL.md` 1 → 3; file-contract row added |
| P2 | protocol-text vs repo-reality contradictions | 3 (`.ufo/state` "stay untracked" vs 16 tracked files; lane write scope vs the main-repo `SCORECARD.md`/`LOG.md` duty; fleet-completion precondition vs per-lane counters) | 0 | `git ls-files .ufo/state \| wc -l` → 16; `git ls-files .ufo/watchdog.log \| wc -l` → 1 |
| P3 | `rounds[]` rows whose lane-round is unidentifiable | 8 of 8 in the round-9 entry (fleet-keyed statuses for lanes on other counters) | 0 (`lane_rounds` required on `not-dispatched`; `ok` falsifiable by the derivable report path) | `MANIFEST.json` round-9 entry vs `.ufo/reports/round-9/` (3 files) |
| P4 | `PROTOCOL.md` length / inline round-incident references | 387 lines / 12 | 576 lines / ~30 | `wc -l PROTOCOL.md`; `grep -o 'round-[0-9][0-9.]*' PROTOCOL.md \| wc -l` |
| P5 | SSOT precedence defined (`MISSION.md` vs `PROTOCOL.md`) | no | yes | Fleet-2 conventions, precedence bullet |

## Planned

- **round 11 (protocol-soundness, lowest after this move on the concision
  sub-metric):** compact `PROTOCOL.md` 576 → ≤450 lines without dropping an
  obligation — collapse the 17 duplicated rule pairs the round-10 simplifier
  audit named, move dated incident prose into a single appendix that cites
  `.ufo/reports/round-*/protocol.md`, and resolve the remaining
  contradictions it listed (`round open indefinitely` vs `missing report
  never holds a round open`; three ledger-path statements). Before→after:
  `wc -l PROTOCOL.md`, obligation count preserved (each deleted clause mapped
  to its surviving canonical home). Also owed: the round-11 closure pass must
  resolve the 7 `in-flight` rows this round wrote plus the lane-rounds that
  terminated after `closed_at` (kake r10, kagi r9, kasegi r12 — listed in the
  round-10 report).

## Retired

- none. Neither fleet-meta axis is saturated: gate integrity still has two
  operator-side actuators outstanding (prompt template items, marker-aware
  `report_of()`), and protocol soundness has an open compaction debt created
  by this round's own additions.

## Move log

| Round | Axis | Before | After | Evidence |
|---|---|---|---|---|
| 10 | gate-integrity | 2 — 2/11 rounds closed, 8/58 lane-rounds recorded, 5 contradicted rows, 4 unrecorded markers, 8 untracked prompts | 6 — 11/11, 58/58, 0, 0, 0 | `MANIFEST.json` `rounds` (15 entries), `.ufo/reports/round-10/protocol.md` §Closure + §Dispatch digest |
| 10 | protocol-soundness (enabling) | 4 — 4 ungoverned artifacts, 3 contradictions, unidentifiable round-9 rows | 6 — 0, 0, 0; cost: +189 lines | `PROTOCOL.md` step 4 semantics, marker clause, precedence bullet, file-contract `SCORECARD.md` row |
