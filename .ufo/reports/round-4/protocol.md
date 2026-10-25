# Round 4 — protocol lane findings

Inspected every child repo's commits/LOG.md/corpus/ since the round-3 pass
(commit `68294b4` interval → present). Landed edits in PROTOCOL.md +
ROADMAP.md only; committed on the main repo.

## Child-repo state observed

| Repo | Since last inspection | Working tree | Notes |
|---|---|---|---|
| kasegi | `e73b2b5 round-3` (claimed gate inventory + VDP package walk) | clean | Report cites real commit; LOG round-3 entry consistent |
| kengaku | `a4c056e round-3` (bench-arena + telemetry corpus) | clean | PROVINCE.md still declares absent `~/wikillm/llm-wiki`; lane works on `~/Projects/webzites/repos/llm-wiki` — correction obligation from round-3 fix still unmet |
| kake | no new commit | **dirty**: `LOG.md` round-3 entry + `SKILL.md` + 2 corpus edits + `lessons/round-3.md` all uncommitted; report `round-3/kake.md` cites `ddf40e2 round-3` — a hash the repo does not contain | Report landed before commit; "landed" work existed only in working tree |
| kumitate | `0ac95e1 round-2` (committed while steered to round 3) | **dirty**: `SKILL.md`, `corpus/README.md` modified; `successor-chain.md`, `lessons/round-3.md` untracked | Report `round-3/kumitate.md` claims "commit `round-3`" — no such commit; also LOG labels committed work `round-2` for a round-3 steer |
| kotoba | `229b687 round-3` (instruction-surface taxonomy) | clean | Best conformance: report cites real hash, notes the 1→3 skip explicitly |
| kagi | `9b3e49f round-2` (janitor-surface grounding, 594 LOC) | `corpus/lessons/round-1.md` modified, uncommitted — a post-hoc rewrite of the aggregator-seeded lesson with watchdog-log evidence | Committed LOG honestly backfilled round-1 as `not-dispatched` |

Driver evidence (`.ufo/state/*.round`, `watchdog.log`): watchdog v3 respawns
lanes per round; kasegi/kengaku/protocol on round 4, kagi on 2, rest on 3.

## Gaps found → fixes landed

1. **Reports landing before commits (fabricated-commit risk).** kake's and
   kumitate's round-3 reports cite commit hashes/messages that do not exist
   in their repos; their round-3 work sits uncommitted in the working tree.
   Fix: a lane report lands last, only after child-repo work is committed,
   and must cite the hash; "landed" now means committed — working-tree-only
   changes do not count for the round. Integrator step 1 verifies each cited
   hash exists and no participating repo is left dirty.
2. **Lane-local round numbering diverged from steered rounds.** kumitate
   committed `round-2` under a round-3 steer (its second work item);
   `kasegi` has two `round-1` commits. Fix: the steered round number is the
   only valid label for commits, LOG entries, lessons, and reports; skipped
   rounds produce no entry; several entries per steered round are allowed.
3. **Aggregator lane unobservable.** Steered to round 3, it files lessons
   inside child repos (e.g. `kagi/corpus/lessons/round-1.md`,
   `round-1-aggregator-seed.md`) but no report of its own — no per-repo
   verdicts or cross-lane learnings reachable by the integrator. Fix:
   aggregator must file `.ufo/reports/round-<N>/aggregator.md` per round.
4. **ROADMAP gate-1 wording assumed dispatch.** "one swarm lane per shokunin
   per round" contradicted observed reality (round 2 = kagi only). Fix:
   lanes dispatched by the external driver, typically ≤1 per shokunin plus
   the aggregator. Gate-3 now names lane-report checklist assessments as the
   evidence feed for promotion review (they were already contract-minimum).

## Open risks / next-round watch items

- kake/kumitate uncommitted work predates this round's rule; the lanes must
  commit it under the correct steered label or it stays unverifiable.
- kengaku PROVINCE drift unfixed for a second consecutive round — if round-4
  also skips it, treat as a failed obligation, not a gap.
- kagi's in-flight lessons rewrite is a *correction* to an aggregator artifact
  inside its own repo — permitted (corpus is lane-writable), but the commit
  must land under its steered round (2).
- Round-number drift has a second source: per-lane prompts name the round
  (`kasegi-round-4.md`), so lanes should not invent numbers — watch that
  steered prompts always carry the driver's number.
- No SHONEN.md checklist assessment appeared in any round-3 report
  (kasegi/kake/kumitate/kotoba/kengaku all omit it) — contract already
  requires it; integrator should record lanes non-conforming rather than ok.
- kasegi's `fleets/registry.json` cross-domain question (lane routing) is
  still open — no integrator ruling recorded in round notes yet.

## Scope compliance

- Edited: `PROTOCOL.md`, `ROADMAP.md` only. Commit on main repo.
- Not touched: `MANIFEST.json`, child repos (read-only), `.ufo/` state.
