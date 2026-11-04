# Round 90 — kake (attempt 1)

Lane `kake` · operability + freshness axes (calibration sub-axis) · lane repo `/home/vgpnk/Projects/shokunin/kake-shokunin` · branch `master`.
Attempt 1. No `lane-dead-no-report kake round=90` line exists, so nothing was inherited from an earlier attempt. One inherited lane-authored leftover, the untracked `baseclean.out` at the lane root (round-89 spot-check D89-1), was relocated byte-exact under this round's C1. Nothing was reverted.
Stale-lane: no (respawn-per-round driver; no other mission of this lane is open).
Tool installs or upgrades: none. No pacman. Network was limited to three RFC GETs.

## Work performed

**Declared claims (2, on distinct axes, frozen before any after-state data in `.ufo/waves/round-90/freeze.md`, freeze commit `4ee62b18`):**

1. **C1 — calibration**, the lowest owned non-retired axis (2 HOLD). The three defects routed by the round-89 outside spot-check close:
   - D89-1: scratch file at the lane root;
   - D89-2: unreceipted SCORECARD/LOG C1 statement at `f62e7954`;
   - D89-3: S463's scope says "not cache-key construction" while the row is used for construction.

   Before → after: `open=3 closed=0 met=false` → `open=0 closed=3 met=true`.
2. **C2 — operability, capability acquisition.** `scripts/cache_key_conformance.py` is a behavioural gate. It refuses the 57-subject non-conforming cache-key population and admits the 4 conforming subjects. Before → after: `gate=absent met=false` → `positives=4/4 negatives_refused=57/57 false_admits=0 met=true`. This is the round's sourced claim (S466, S468).

**Work items, with evidence:**
- Protocol load: MISSION/AXES, lane SCORECARD (planned-after-89), `corpus/lessons/round-89-verifier-spotcheck.md`, the round-89 report and lesson, QUALITY, README frontier, and `considerthese/2026-10-26.md`.
- Census before: exit 0, 26 × W04 (`.ufo/waves/round-90/controls/census-before.txt`).
- Pre-freeze controls (`controls/run_controls.sh`):
  - `controls/ctl-c1.txt`: the do-nothing run stays open=3. Seven forgeries (D1a, D1b, D2a, D2b, D2c, D3a, D3b) each leave their item open. A positive fixture reaches `open=0 closed=3`.
  - `controls/ctl-c1-v0-before-parse-fix.txt`: the first run's positive control exposed a parse defect in the counter. I fixed it before the freeze.
  - `controls/ctl-c2.txt`: no-gate, blanket-refuse, blanket-admit, hash-table and name-table gates all read `met=false`.
- Sources opened this round: RFC 9110, RFC 9111 and RFC 8259 plain text, retained at `.ufo/waves/round-90/L1/src/`. Digests and ≤25-word quotes are in `corpus/lessons/round-90.md` §Gate (3 admits, 3 rejects).
- C1 fixes, commit `e50c9566`:
  - `baseclean.out` moved to `.ufo/waves/round-90/inherited/baseclean.out`.
  - The frozen c89 counter was re-run at `f62e7954` (`controls/r89-c1-at-f62e7954.txt`: `open=5 closed=1`, but only item E is closed).
  - Correction tails were appended to SCORECARD.md and LOG.md.
  - S467 (`supersedes S463 —`) was added. S463 is byte-identical.
- C2 gate committed at carrier `7f6c68f1`:
  - 70 hand cases, one or more per contract clause.
  - 120 seeded generated cases.
  - An audit-hook sandbox.
  - An advisory line for contract gaps.
- Knowledge: new `corpus/knowledge/cache-key-conformance-gate.md`. `cache-key-construction.md` gains a round-90 ground update citing S467.
- Mistakes mined: `corpus/lessons/round-90.md` §Mistakes has 7 rows. One of them falsifies round-89 MutKey's claim that M37 is an equivalent mutant: `%` is a tchar, and the gate case `name-percent-absent` refuses M37.
- New QUALITY criterion: `corpus/QUALITY.md` §"Round 90 — a counter earns a `met` only after it has been shown able to say no". It is grounded on the round-89 spot-check's routed instrument-calibration item.
- considerthese: `2026-10-26.md` Part 2 proposal 3 (operator-decision queue) landed as a lesson section. It lists 10 open kake L0 items with the number of rounds each has waited.
- Wave w1: 13 seats, dispatched via `.ufo/waves/round-90/w1.ready`. WAVE-DONE was received ("all 13 seats settled"), and every seat report is in `.ufo/waves/round-90/w1/`.
  - Findings (full table in the lesson §Wave review):
    - The carrier gate's sandbox could be escaped through `_posixsubprocess.fork_exec`, frame-global or `gc` rebinding, or a spoofed `realpath` (ScoutGround, ExecSandbox, ReviewGate).
    - The carrier gate admitted 14/23 ExecStubs held-out stubs and 7/7 CriticClaims H-probes.
    - The output judge was stricter than the contract (ReviewGate F3).
    - My non-UTF-8 diagnosis was wrong; the cause was the gate's own locale (ReviewGate F4).
    - Both frozen counters admit forgeries (ReviewC1 F1–F4, MutC1, CriticClaims F1/F1b/F2, ScribeLedger).
    - MutGate killed 13/39 gate mutants with the frozen counter.
  - Response: I hardened the gate after the wave (`a4814f58`). Hook state is now bound at install time; process-spawning and native modules are denied; paths get a textual check plus `realpath`; stdin is decoded as strict UTF-8; 22 new hand cases; the judge follows the contract exactly; a `dup-json-member` advisory was added. The frozen counters were not changed.
  - Held-out result at the tip: `.ufo/waves/round-90/integration/heldout-tip.txt` shows positives 8/8 (including ReviewGate's independent contract-only implementations) and negatives refused 57/58. The one admit is S09, which refuses NUL, a behaviour the contract does not decide.
- Real domain trial: ExecTrial ran the gate on the shipped constructor over 5 seeds × 600 cases. It also ran 48 recorded Vary capture cases, and all agree with the gate's reference (`w1/ExecTrial.md`).

## Landed changes

LOG entry: `LOG.md` `## Round 90` (two sections: correction tail and round entry).

| Commit | Change | LOG tie |
|---|---|---|
| `4ee62b18` | Freeze: two counters, frozen population pins, two sandbox negatives, pre-freeze controls, base receipts, retained RFC bodies | Round 90 entry, "Controls before the freeze" |
| `7f6c68f1` | `scripts/cache_key_conformance.py` (C2 carrier); retained RFC 8259 body | Round 90 entry, C2 |
| `e50c9566` | D89-1..3 fixes: relocation, receipted correction tails, S466–S468, lesson Gate, gate knowledge entry | correction-tail section; Round 90 entry, C1 |
| `79e1aac2` | Carrier receipts, census after, wave spec and validated dispatch | Round 90 entry, wave w1 |
| `a4814f58` | Gate hardened from wave findings; SKILL/README/PROVINCE rows; QUALITY criterion; construction-entry ground update; lesson corrections; held-out receipts; assimilation id check | Round 90 entry, "hardened after the wave" |
| `f6915632` | Wave evidence (13 reports, results), tip receipts, SCORECARD/LOG round-90 sections, lesson wave review | Round 90 entry |
| `7134ef6b` | Final receipts at `f6915632` (C1, C2, census) | — |

## Before → after measurements

| Claim | Base `209027f4` | Carrier | Final tip `f6915632` | Counting command |
|---|---|---|---|---|
| C1 | `open=3 closed=0 met=false`, exit 1 (`controls/base-c1.txt`) | `e50c9566`: `open=0 closed=3 met=true`, exit 0 (`controls/after-c1-carrier.txt`) | `open=0 closed=3 met=true` (`controls/final2-c1-at-tip.txt`) | `python3 -B .ufo/waves/round-90/c90_defects.py --root . --revision <REV> --work <scratch>` |
| C2 | `gate=absent … met=false`, exit 1 (`controls/base-c2.txt`) | `7f6c68f1`: `positives=4/4 negatives_refused=57/57 false_admits=0 errors=0 anti_table=ok population=ok met=true`, exit 0 (`controls/after-c2-carrier.txt`) | same line, `met=true` (`controls/final2-c2-at-tip.txt`) | `python3 -B .ufo/waves/round-90/c90_gate.py --root . --revision <REV> --work <scratch>` |

All receipt paths are under `.ufo/waves/round-90/`. The counter bytes equal the freeze sha256 (ExecReplay §3; CriticClaims).

**Author verdicts:**
- **C1: measured met on the frozen predicate, but thin and on a forgeable instrument.** The fixes are real; ReviewC1 re-derived D89-2 byte-exact. However, the counter closes D1 when the file is ignored or staged, closes D2 on any receipted revision, and closes D3 on a case-variant scope. CriticClaims judges C1 bookkeeping-only.
- **C2: measured met on the frozen predicate, on a forgeable instrument.** The counter admits a pin-reading or allowlist gate and cannot tell an independent gate from one that wraps the candidate. The carrier gate itself was falsified as a conformance gate by held-out stubs and a sandbox escape. The post-wave tip gate closes those classes on 57/58 held-out negatives.
- Admission belongs to the outside closure.

## Sources & frontier

- `corpus/SOURCES.md` rows: 202 → 205. Tier A: 177 → 180. Knowledge `.md` files: 77 → 78. Commands:
  - `git show <rev>:corpus/SOURCES.md | grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'`
  - `git ls-tree -r --name-only <rev> -- corpus/knowledge | grep -c '\.md$'`
- Rows added by tier: A +3.
  - S466: RFC 9110 §5.5.
  - S467: RFC 9111 §2/§4.1, which supersedes S463.
  - S468: RFC 8259 §7/§8.1.
- Rows touched old → new: none. S463 is byte-identical.
- Census, `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kake`:
  - start: exit 0, `kake ok`, 26 × W04 (`controls/census-before.txt`);
  - end: exit 0, `kake ok`, 29 × W04 (`controls/census-final.txt`). The 3 new W04 are cross-scope URL duplicates of the plain-text RFC URLs.
- Frontier rows advanced: `corpus/README.md` gains "Cache-key conformance … r90 … S466 S467 S468". PROVINCE gains a round-90 ground section.
- Sourced claim: C2's every-header CR/LF clause and its advisory line cite S466 and S468, both opened this round.
- Mined mistake: `corpus/lessons/round-90.md` §Mistakes (7 rows).
- Assimilation: none. `merge/kake` still collides on 8 ids (`.ufo/waves/round-90/assimilation/collisions`).
- considerthese: proposal 3 of `2026-10-26.md` (above).

## Trend verdicts

- **expansion: improved (author-side).** One new knowledge entry sits on ground the map did not hold (cache-key conformance; field-value validity; JSON text encoding). It cites three mined tier-A rows opened this round, and the census is clean.
- **quality: improved (author-side).**
  - Round-89 defects D89-1..3 are corrected by appended tails and a superseding row, with no filed byte rewritten (`git diff --numstat 209027f4 7134ef6b` outside `.ufo/`: 0 deleted lines).
  - A false round-89 equivalence claim (M37) is falsified.
  - The gate entry's false sandbox claims were rewritten after the wave.
- **discernment: unchanged.**
  - For: the new QUALITY criterion, and pre-freeze controls that caught one counter defect.
  - Against: the attack seats again found forgeries that reach `met=true` on both frozen counters, plus a sandbox escape in the shipped carrier gate. My first draft did not foresee these.

## SHONEN

Count of `## SHONEN` headings: 1. No box is `[x]`; there is no named non-author verifier for a box this round.

[~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — pointer: `corpus/knowledge/shonen-ledger.json` row `box 1`; round 90 adds SKILL.md registry rows for `cache_key_conformance`, `c90 defects` and `c90 gate capability`, and `corpus/knowledge/cache-key-conformance-gate.md` (decision table, error patterns, runnable checklist, S466–S468).
[ ] At least one end-to-end domain task executed and logged in LOG.md — `shonen-ledger.json` row `box 2` stays `status=gap` (missing round-47 receipt); round 90 logs a real trial (`LOG.md` `## Round 90 … conformance gate`, `w1/ExecTrial.md`) but does not repair the ledger gap.
[~] Instructions executable by an agent without oral context — pointer: `corpus/knowledge/cache-key-conformance-gate.md` runnable checklist (expectations reproduced by ScoutGround at the carrier; updated to the tip lines `hand=92/92`, `advisory=2/4`).
[~] No cross-domain bleed (PROVINCE.md still accurate) — pointer: `PROVINCE.md` `## Round 90 — cache-key conformance gate`; ConnectorScope found no contested sibling PROVINCE. mori S594 holds the same RFC 9111 §4.1 digest and was reported, not absorbed.

## Wave shape

- Shape: one v1 wave of 13 seats, inside the 8–16 band. No second wave and no residual call. Round total: 13.
- Roles: scout 2 (ScoutGround, ScoutSources), executor 4 (ExecStubs, ExecSandbox, ExecReplay, ExecTrial), mutation-tester 2 (MutGate, MutC1), reviewer 2 (ReviewC1, ReviewGate), critic 1 (CriticClaims), scribe 1 (ScribeLedger), connector 1 (ConnectorScope).
- Attack seats: 5/13 (38 %).
- The L1 holds the canonical planner seat, and ScoutGround carried the bounded planning data-walk, because the validator forbids a planner swarm role (D84-4 is still open at L0).
- Dispatch: `w1.ready` at 19:13:42, `w1.ready.dispatched` at 19:14. WAVE-DONE was received from Main.
- Dead seats: none. All 13 reports are present and non-empty. `w1-results.json` carries no per-seat status or output, and per-seat answering models were not recorded. No claim depends on them.

## Honesty and limits

- Both frozen counters admit forgeries, as listed above. They were not repaired after scoring. Successor-counter requirements are in SCORECARD "Planned — after round 90".
- The C2 positive and negative labels were frozen before the gate existed. The gate's `reference()` agrees with the shipped candidate on every scored case. Its independence rests on ReviewGate's contract-only `mine.py` (0 disagreements over 20 000 fuzzed inputs), not on the counter.
- The post-wave gate changes came after the carrier measurement. They are additional, held-out evidence, not the frozen claim. The tip gate was not re-mutated (MutGate attacked the carrier bytes).
- Contract gaps routed as R90-1…R90-5: non-UTF-8 input; NUL in values; the raw form in example 5; the method missing from the key; duplicate JSON members.
- `controls/run_controls.sh` no longer replays at the tip, because it copies the lane-root `baseclean.out`, which has since moved (ExecReplay).
- Open L0 questions (not re-filed): kake round-86 D84-4 and the three kake round-89 lines. This round adds no new L0 question.

## Misroot sweep

`git -C /home/vgpnk/Projects/shokunin status --porcelain` shows the orchestrator's `.scratch/` state, a modified `.ufo/l0-questions.md` and `.ufo/reports/round-84/kama.md` (not written by this lane), and an untracked `after` dated 2026-11-03. None of them names kake round 90, so no misroot was recorded and nothing was copied or deleted. Scratch `/fast/scratch/hyaku/kake-r90` was removed.

## Pre-report gate

- `git ls-remote origin refs/heads/master` → `7134ef6b2d8cf171c4570672d8e58ba2e4b9e3a8`, the final lane hash.
- `grep -c '^## SHONEN'` → 1, followed by four box lines.
