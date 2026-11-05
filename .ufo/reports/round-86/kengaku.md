# kengaku — round 86 (hyaku run 15, attempt 1)

Lane `kengaku-shokunin`, branch `master`. Base `88651a72ef112ed9f5361e1c8c197babec691f96`;
claims freeze `61b0e074a44259c8c022aa2fda257182a0708346`; instrument bytes v1
`316811fa604eeef1d157bdbf62b5595891dc015a` (batteries), v2 `e23bec073e5aba45fee352dda79d49c7aaf09a57`
(the tip-measured bytes; see Corrections R86-V2); population-ledger row `f357e4c1`; receipt and tip
measurement `276abd46123974f31365866b173b329c641873cf`. One v1 wave, 12 seats, no residual call, zero dead seats.

## Work performed

The round declared **two claims**, each on a distinct axis and each causally separable:

- **R86-C1 — coverage** (the lowest non-retired axis, held at its L0 cap `kengaku | round-25/33/51`):
  the executed Terminal-Bench 2.0 grader population grows by exactly one member, `raman-fitting`
  (`file-artifact`, `numeric-band`, `serialization-schema`), by a located offline replay of that
  member's pinned captured grader over eight frozen schema-drift case shapes. Predicate label
  `PREDICATE R86-C1 pass`; counter `plans/round86_c1_replay.py`.
- **R86-C2 — calibration** (held at ceiling 10): the lane's own self-assessment mismatch count, as
  printed by `plans/state_check.py --summary`, falls 1 → 0, and the single repaired assertion
  (`P3c.box.4.pointer.1`: `SHONEN.md` box 4 pointed at `PROVINCE.md:129`) is re-derived from
  `PROVINCE.md` bytes rather than hand-edited. Predicate label `PREDICATE R86-C2 pass`; counter
  `plans/round86_c2_repin.py`.

No claim is exploratory; no claim is re-declared from a prior round; no target was narrowed after
landing; no frozen sentence, case table, leg list, control set or kill rule changed after the freeze.

Work items (each with its evidence pointer):

- **Freeze.** `plans/round-86-claims.md` states both claim sentences, both frozen predicates, both
  counting commands, both kill rules, the eight legs of C1 and the five legs of C2, the control sets,
  the honest limits, the separation argument and the sourced-row dependency — committed before any
  tip data existed (`61b0e074`, LOG round-86).
- **Instruments bound to the freeze.** `plans/round86_c1_replay.py` carries
  `FREEZE_REV = 61b0e074…`; `BASE_REV = 88651a72…` is in both counters (`877f6512`).
- **Pre-data battery, then BASE, then tip** (in that order, committed as evidence):
  `.ufo/waves/round-86/L1/freeze-battery.txt`, `base-runs.txt`, `c1-tip.txt`, `c2-tip.txt`.
- **C1 landing.** The population ledger row for `raman-fitting` moves to `executed`/`round 86`/this
  receipt/`tb2-header`/`cases` (`f357e4c1`); the receipt is minted at a clean committed tip
  (`276abd46123974f31365866b173b329c641873cf`), not re-used from the inherited attempt.
- **C1 replay evidence.** `corpus/evidence/round86/raman-fitting-probe.txt`: eight `CASE` lines,
  `cases=8 legs=24 mismatches=0`, `PREDICATE R86-PROBE pass`, exit 0, `WORKTREE clean`.
- **C2 repair, re-verified.** `SHONEN.md` box 4 points at `PROVINCE.md:151` and
  `plans/state_check.py`'s box-4 pin carries the same derived line (landed in the inherited attempt's
  `0481a6d3`, frozen and measured this round); `plans/state_check.py --summary` prints
  `mismatch=0`, `VERDICT: PASS`.
- **Source.** S274 admitted for the pinned `raman-fitting/tests/test_outputs.py` (`corpus/SOURCES.md`,
  fetched this round: HTTP 200, 2029 bytes, sha256 `171fae77…`, `cmp` silent against the round-52
  capture; quote `:36`, 8 words by `len(quote.split())`).
- **Criteria.** QUALITY Q63 (a self-test leg must exercise the same read path as the counter), Q64 (a
  fixture never writes through a hardlink), Q65 (a mutation battery declares necessity or names the
  catcher), each grounded in a mistake this round mined from its own battery (`981d6f19`).
- **Gates the round re-priced.** `SKILL.md`'s three class cells (executed counts 30, `numeric-band`
  3/10, `file-artifact` 22/76, `serialization-schema` 3/10) and the canonical surface row in
  `PROVINCE.md` (`rows=253` was three appends stale; now 266) — R79, R76 and R77 green again
  (`a571044c`).
- **Q20 outside-copy roster** from a shared clone at the tip: `grader.py` 733 checks PASS,
  `sources_adopt` 17 cases, R75 parity PASS, R79 `DEFECTS n=0`, R82 `DEFECTS n=0`, `defect_ledger`
  `mismatches=0`, `state_check --selftest` exit 0, C1 selftest 10/10
  (`.ufo/waves/round-86/L1/outside-gates.txt`).
- **Wave.** One v1 wave, 12 seats (roles below), validated under policy v1 (`maxLanes` 12 inside the
  8–16 band), dispatched through the inline handoff (`.ufo/waves/round-86/w1-spec.json`,
  `w1-dispatch.json`, `w1.ready` → `w1.ready.dispatched`). Seat evidence under
  `.ufo/waves/round-86/w1/`.

### Wave findings (attack seats)

The wave's attacks changed the report rather than being argued away. Each is routed with its
remediation; none voids a frozen predicate, and none is a BLOCKER.

- **ReviewerC186 F1 (moderate) — the claims' honest-limit sentence overstates L3.** A receipt whose
  `LANE_TIP` declares *any resolvable ancestor* (demonstrated with the round-85 BASE `88651a72`)
  reaches the full target, because L6 compares the tip-free observation block and discards the fresh
  stamp. The delivered claim is met; the narrow true statement is: "L3 excludes a tip that does not
  resolve in this repo or that is not an ancestor; it does not bind the receipt to the revision it
  was minted at." Carried in the lesson's definition horizon and in *Planned*.
- **ReviewerC186 F2 (minor) — `members=1` is a literal.** The counter never counts executed rows, so
  the "grows by exactly one member" clause is measured by hand (29 → 30, one changed row) and not by
  the instrument. Routed to the successor instrument.
- **ReviewerC186 F3 (trivial) — one frozen case-table `why` names a line that never evaluates**
  (`2D-null-value` fails at `G_peak["x0"]`, not at the cited arithmetic). The predicted vector is
  unaffected. Recorded, not edited (frozen file).
- **CriticR86 (eight MINOR findings, no BLOCKER).** Independently reproduced both claims at
  `a571044c` (both tips green, both BASE runs red, all eight controls refusing, both batteries
  reproducing their committed splits) and then priced the precision defects: L3 ancestry (same as
  ReviewerC186 F1), the literal `members`, a malformed-ledger traceback that exits 1 instead of a
  named `DEFECT`, a `--freeze` override that can make L4 compare a table with itself, and the
  fixture-mode (`--lane` without `--rev`) measuring the dirty worktree. The frozen counting command
  passes `--rev`; the rest are routed.
- **SentinelR86 (five findings, none voiding the delivered bytes).** F1 is the one this round
  repaired before the tip run: `P4-state`/`P5-selftest` read `plans/state_check.py` from the *lane
  worktree* even when a revision was measured, so a worktree edit could move a committed tree's
  verdict. The patch (`e23bec073e5aba45fee352dda79d49c7aaf09a57`) makes the measured tree's instrument authoritative and passes a fixed
  `env` to every `git`/`tar` child (its F4). F2 (ancestor tips), F3 (one stdout channel shared with
  the graded capture), and F5 (the sandbox ro-binds host `/etc` and `/usr`, no rlimits) are recorded
  with their remediations; the capture is byte-pinned, so none of them is a live attack surface this
  round.
- **MutTesterR86** added seven of its own mutants on top of the shipped batteries: the C1
  `executed-always-1`, `exit-nonzero-accepted`, `missing-stamp-field-accepted`,
  `predicate-absent-accepted`, `table-member-accepted` (and its deep variant) and the C2
  `derive-returns-stale-line`, `pin-line-lax`, `shonen-compares-to-stale`, `skip-p5-selftest`. The
  three C2 survivors are the same structural redundancy the round's own battery declares
  (`caught_by=P4-state`); on a clean tip the `derive-returns-stale-line` mutant turns the counter
  red, which is the direction a necessary check must move.
- **ExecGatesR86** ran the gate roster in an extracted tree and reported `FINDINGS: 0 count
  differences`; it also priced the counters' region limitation — run from a non-git extraction they
  exit 2 (`unresolved-revision master`), so the Q20 roster must run in a clone (done here).
- **ExecBaseR86 / ExecCensusR86** independently re-derived the receipt's digests (`TOOL_SHA`,
  `CASE_TABLE_SHA`, `SUBJECT_SHA`, ancestry: all `ok`), the freeze/base/instrument anchors, the
  census exit code and the row arithmetic.

## Landed changes

Every change is tied to the round-86 LOG entry and to the commit that carries it.

| change | LOG.md round-86 entry | commit |
|---|---|---|
| frozen claims, predicates, kill rules, control sets | "Base … freeze … instrument bytes" header + claim bullets | `61b0e074` |
| counters bound to the freeze revision | C1 bullet (frozen constants) | `877f6512` |
| battery repairs (Q63/Q64/Q65's executable halves) | "two battery legs were repaired before any tip run" | `316811fa` |
| pre-data receipt: both batteries green, both BASE runs red | C1/C2 bullets | `48a1ffbd` |
| wave spec, validated dispatch, ready handoff | wave bullet | `d5e67d9c` |
| ledger row `raman-fitting` → executed (round 86) | C1 bullet (population counts) | `f357e4c1` |
| S274, QUALITY Q63–Q65, class cells, README index, lesson | Source/Repairs/Frontier bullets | `981d6f19` |
| wave evidence (seat reports, swarm registry, dispatch marker, separation test) | wave bullet | `ab9da0d4` |
| `SKILL.md` self-test row backed by its entry path | operability bullet | `4d2a0ee8` |
| canonical surface row re-counted 253 → 266 | Repairs bullet | `a571044c` |
| receipt re-minted at a clean tip + tip measurement + separation result | C1/C2 bullets | `276abd46123974f31365866b173b329c641873cf` |
| SCORECARD section + LOG section | this entry | `25f68ca0b717afe677e6cae8e7583eaeeee99ad5` |

## Before → after measurements

**R86-C1 — coverage.** Counting command:

```sh
python3 plans/round86_c1_replay.py --lane . --rev <REV> --work <scratch>
```

- BASE `88651a72`: `TARGET members=1 cases=0 legs=0 mismatches=0 located=0 executed=0 defects=7`,
  `PREDICATE R86-C1 fail`, exit 1 (`.ufo/waves/round-86/L1/base-runs.txt`).
- Tip `276abd46123974f31365866b173b329c641873cf`: `TARGET members=1 cases=8 legs=24 mismatches=0 located=1 executed=1 defects=0`,
  `PREDICATE R86-C1 pass`, exit 0.

**R86-C2 — calibration.** Counting commands:

```sh
python3 plans/round86_c2_repin.py --lane . --rev <REV> --work <scratch>
python3 plans/state_check.py --summary
```

- BASE `88651a72`: `TARGET … state_mismatches=1 … defects=3`, `PREDICATE R86-C2 fail`, exit 1; the
  instrument itself prints `assertions=329 match=317 mismatch=1`, `VERDICT: FAIL`.
- Tip `276abd46123974f31365866b173b329c641873cf`: `TARGET … state_mismatches=0 … defects=0`, `PREDICATE R86-C2 pass`, exit 0; the
  instrument prints `mismatch=0`, `VERDICT: PASS`.

**Controls and batteries, run before the tip data existed** (`.ufo/waves/round-86/L1/freeze-battery.txt`):
C1 selftest 10/10, mutants `real=6 necessary=5 redundant=1`, four controls each
`target_reached=False`; C2 selftest 4/4, mutants `real=3 necessary=1 redundant=2` with the catcher
named for each redundant mutant, four controls each `target_reached=False`.

**Separation** (`.ufo/waves/round-86/L1/separation.txt`): reverting C1's receipt and ledger row leaves
C2 at `defects=0`; reverting C2's two-line repair leaves C1 at `defects=0`.

**Population movement** (`plans/round79_c1_population_ledger.py --lane .` → `replayed=30`, `DEFECTS n=0`):
executed 29 → 30; `serialization-schema` 2/10 → 3/10; `file-artifact` 21/76 → 22/76;
`numeric-band` 2/10 → 3/10.

## Sources & frontier

**Census, before → after.** Command (frozen in `CORPUS.md`, run at round start and round end):

```sh
sh /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kengaku
```

- Before: exit 0, `kengaku ok …/corpus/SOURCES.md`, 30 W04 warnings, 265 rows.
- After: exit 0, same last line, 30 W04 warnings, 266 rows.

Rows added by tier: **A +1** (S274, a pinned Terminal-Bench 2.0 grader under a frozen commit),
B +0, C +0. Rows touched old→new: none — S274 is the only change and no existing status, recheck or
`used-by` cell moved. Frontier rows advanced: the corpus/README *agentic benchmark task-spec audits*
thread, for one more Terminal-Bench 2.0 member's grader (member replay only; the task image, an oracle
and a harness run remain outside the performed work).

**Sourced claim.** R86-C1 rests on S274, opened this round: the pinned bytes were fetched and
byte-compared, and the receipt's `SUBJECT_SHA` is that digest.

**Assimilation: none.** `merge/kengaku/` stays blocked by L0 `kengaku | round-54` (mass id drift);
no package bytes were read into the lane and no id-collision check could be run against a package
this lane is not adopting. No `considerthese/` proposal was taken: `2026-10-26.md` §2 (a standing TB2
admission counter) is already Q61's open half and is listed in *Planned*.

**Operator questions.** No new L0 line was appended this round. Two remain open and are routed
around, not assumed answered: `kengaku | round-84` (Q13 checker shape — it keeps any one-wave
knowledge admission unconfirmable) and `kengaku | round-54` (assimilation package id drift).

## Trend verdicts

- **expansion — `unchanged`.** The population moved one member (29 → 30 executed; three class cells
  re-priced), but the axis's own expansion grade in `corpus/README.md` is `unchanged` because the
  round adds no new coverage ground outside the L0 cap and no new capability row: the replay method is
  rounds 83–85's.
- **quality — `improved`.** Three new criteria (Q63–Q65) with executable halves, two instrument legs
  repaired before any data, the canonical surface count repaired, and an outside-copy gate roster with
  zero count differences. Evidence: `corpus/QUALITY.md` Q63–Q65, `.ufo/waves/round-86/L1/freeze-battery.txt`,
  `.ufo/waves/round-86/w1/ExecGatesR86/gate-receipt.txt` (`FINDINGS: 0 count differences`).
- **discernment — `improved`.** The round's attacks changed the report: ReviewerC186's F1 shows the
  claims' honest-limit sentence overstates what L2+L3 exclude (a receipt declaring any resolvable
  ancestor tip reaches the target), F2 shows `members=1` is a constant rather than a population count,
  and F3 shows one frozen case-table `why` names a line that never evaluates. All three are carried
  into the lesson and the *Planned* list instead of being argued away.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — evidence:
  `SKILL.md` (two new gate rows `round86-c1-replay`, `round86-c2-repin` and one probe row
  `round86-raman-probe` added this round; the gate/probe registry carries 157 rows and R82 prices it
  green).
- [~] At least one end-to-end domain task executed and logged in LOG.md — evidence: `LOG.md` round-86
  entry with the replay, the ledger row, the receipt and the gate roster.
- [~] Instructions executable by an agent without oral context — evidence:
  `plans/round-86-claims.md` (counting commands, kill rules, controls) plus
  `.ufo/waves/round-86/L1/freeze-battery.txt`.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — evidence: `PROVINCE.md` canonical surface
  row re-counted this round and `plans/round77_c1_declared_surfaces.py` green (`agree=28 disagree=0`).

## Round shape

One v1 wave under policy v1 (band 8–16): 12 seats — scout 1, executor 3, scribe 2, reviewer 2,
critic 1, mutation-tester 1, sentinel 1, connector 1 (attack share 4/12 = 33 %). No residual call.
Dead or incomplete seats: **two** — `ScoutR86` never wrote a file and was still running its own C2
counter when the round closed, and `ReviewerC286` committed only a stub it itself labelled
"evidence collection in progress"; neither seat's work is claimed and no finding from either is used.
Ten seats delivered committed evidence under `w1/`, including the attack seats whose findings are
listed above. Round total: 12 seats. Lane tip at close: `25f68ca0b717afe677e6cae8e7583eaeeee99ad5`.

The L1 holds the canonical planner seat (the validator rejects `planner` as a swarm role); the
bounded planning data-walk rode the L1's own reads plus `ExecCensusR86`'s row arithmetic, because the
seat that was meant to carry it, `ScoutR86`, delivered nothing.

**Stale-lane:** no — respawn-per-round driver; no other mission of this lane is open.

**Tool installs:** none this round (no package was installed or upgraded).

**Inherited state:** the earlier attempt of this round left committed instruments, a case table and a
receipt (`0481a6d3`, `c939e6b5`, `bfda0472`, `9972c87c`). Reused after re-verification: the case
table, the probe, both counters and the box-4 re-pin. Discarded and re-minted: the receipt (it named
`LANE_TIP bfda0472` with `WORKTREE dirty`; the round minted its own at a clean tip). Nothing
uncommitted was inherited; `corpus/lessons/round-85-verifier-spotcheck.md` (non-author) was read and
indexed in `corpus/README.md` without editing it.
