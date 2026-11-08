# kagi — round 67 report

Lane: kagi (`kagi-shokunin`, secrets & vault ops). Round 67, attempt 1.
Claim BASE `076701a11a58e3eb58d996b4c76c5e18071fb179` (round-66 verifier
spot-check tip). Frozen predeclaration `plans/round-67.md` at
`aa8807e443166f45485e1aada2989f646efc707c`; Amendments A1–A5 appended in the
same file, each naming the seat that forced it. Lane tip after this round's
work: `c686b035f4dba398426222ee5bb7cba8aeee5e8c` (three commits: the round's work,
the scribe's four entry corrections, and the wave's results receipt); the lane
remote prints that hash.

## Work performed

The round declares **two claims on two distinct axes**:

- **C1 — freshness (capability acquisition):** the lane's own source census
  reads the bytes and the declared locator quote of every capture-path row.
  `C1_READTHROUGH` located 35 → 36, caught 0/6 → 6/6 (bound is 36 at BASE as a
  row property and 0 as a gate reading — Amendment A2.6 states both).
- **C2 — calibration:** the lane's record surfaces match the state they
  describe. `C2_FIDELITY` mismatches 7 → 0 over the seven surfaces the round-66
  non-author closure routed (its §6 items 1, 2, 3, 6, 7, 8).

Axis rationale: all six axes stood at 9 (the saturation line) and no capability
row had entered since round 61, so the **stagnation nudge** (`AXES.md`) waived
the lowest-axis obligation and the round is a capability move plus the
harmed-axis repair. Recorded in `SCORECARD.md` §Round 67 — pre-move.

Work items (each with its evidence):

- **Predeclaration and amendments.** Plan frozen alone at `aa8807e4`; A1 (the
  C2 leg 6 content rule and the out-of-lane routed items), A2 (the reviewer's
  five blocking findings: location shape, the narrowed C1 sentence, the
  `caught` map, population identity, guard venue), A3 (the sourced row's prose
  place in the frozen population), A4 (heading form), A5 (guard f, the
  counter's oracle) — `plans/round-67.md`.
- **The census gate learns to read captures.** `corpus/sources-census.sh`
  gains the `SC_CAPTURE` finding class (`capture-outside-root`,
  `capture-missing`, `capture-digest-mismatch`, `capture-bytes-mismatch`,
  `quote-not-located`), the `SOURCES_CAPTURES:` summary line, and 11 new
  selftest cases (78 → 89). Evidence: `bash corpus/sources-census.sh` ⇒
  `SOURCES_CAPTURES: CLEAN (path_rows=36 bound=36 located=36 prose=121)` +
  `SOURCES_CENSUS: CLEAN (rows=157 …)`; `--selftest` ⇒ `PASS (89 cases)`;
  receipts `.ufo/waves/round-67/final/sources-census-candidate.txt`.
- **The S115 quote re-cut.** The one declared quote that did not locate at
  BASE: the audit-device row's column 13 is now the 18-word sentence
  `Audit devices must be enabled by a root user using bao audit enable or using
  the audit stanza` (`RENDERED_TEXT_V1_LOCATE: count=1`; the same sentence with
  a terminal period reads `count=0` — the defect). Only column 13 changed;
  `corpus/source-fetches.tsv` sha256 `d2f050b6…` → `60fa5d10…`.
- **Two counters.** `plans/round-67-c1.sh` (sha256 `3aed2ac6…`, 1195 lines;
  selftest 50 cases) builds six one-defect mutations, reads the candidate
  gate's own stdout for each, and binds the population to the BASE blob;
  `plans/round-67-c2.sh` (sha256 `d4deb735…`, 1091 lines; selftest 24 cases)
  runs seven record legs. Evidence: `.ufo/waves/round-67/final/c1-*.txt`,
  `c2-*.txt`.
- **The sourced row and the entry.** S166 (RFC 9530 §1.2) registered tier A
  `mined`, capture `.ufo/waves/round-67/capture/S166.body` (67152 B, sha256
  `544dbb7d…`), quote `count=1` under `rendered-text-v1`; entry
  `corpus/knowledge/source-capture-binding.md` (two digest layers, seven bounds,
  eight falsifiers) is C1's sourced claim. Its fetch row's location is prose by
  design (Amendment A3), so the frozen capture population holds.
- **Seven record repairs (C2).** Scorecard round-66 operability cell → the
  honest stop its receipt shows; SKILL's round-66 C1 pin `cases=14` → `45`;
  the coverage-map row for the round-66 carrier entry; the `R66Sentinel` row in
  the round-66 falsification ledger; `claims.json` re-derived to
  `C1_CARRIER/C2_PREFILE/C3_CENSUS`; a reconstructed `c3-base.txt` whose header
  names BASE and the archive command; the round-66 lesson's `used-by` corrigendum
  (six changed cells + one new row, S113 named). Extra repairs found while
  doing it: the scorecard's round-66 C1 cell (`6a79a96d…`/43 → `d72f9712…`/45),
  four stale self-counts in `SKILL.md`, `PROVINCE.md` and `corpus/README.md`
  (all eight pre-date this round, measured identical at BASE).
- **Ledger migration.** `R21-03`'s selftest expectation 78 → 89 with
  `.ufo/waves/round-67/journals/expectation-migrations.json` ⇒
  `EXPECT_JOURNAL: CLEAN (changed=1 journaled=1)`.
- **Wave.** `kagi-r67-w1`, one v1 wave, **13 seats**: scout 1, executor 4,
  scribe 2, reviewer 1, critic 1, mutation-tester 1, sentinel 1, connector 1,
  revenger 1. Attack roles 5/13 (38 %), one connector; the L1 holds the
  canonical planner seat; no residual call. Spec `w1-spec.json`, dispatch
  `w1-dispatch.json`, seat reports under `w1/`. `R67ScribeEntry` (scribe) did
  not file a report; the deliverables it was assigned (the entry, S166's rows)
  were landed by the L1 instead — named here as a seat that did not report, not
  as a gap in the work. **All 13 seats settled, none died**
  (`kagi-r67-w1-results.json`). The results file's `output` fields are empty with
  the note that the orchestrator kernel restarted mid-wave and the seat outputs
  were not retained, so every seat claim in this report rests on the seat's own
  report file under `w1/`, not on the results envelope. Its four entry defects
  (an overstated RFC scope, an overstated identity bound, the F8 counter wording,
  a fetch claim with no committed receipt) were fixed in `cf26e146`; the fetch
  receipt is committed at
  `.ufo/waves/round-67/capture/S166.fetch.txt`.
- **Per-seat output that changed the round** (each forced an amendment or a
  fix): the reviewer's five blocking findings (A2), the sentinel's
  fake-normalizer exploit (A5 + guard f, and the gate's own-sibling rule), the
  scout's absent-receipt finding and strict-classifier measurement (A2.1, the
  receipt headers), the critic's L6 content-blindness (A1), the mutation
  tester's seven mutants and the revenger's nine-class bypass battery (ceilings,
  §Routed).

## Landed changes

| change | LOG.md entry | commit |
|---|---|---|
| plan, claims, declared-axis rows, scorecard pre-move | §Round 67 bullet 1–2 | `aa8807e4` |
| census capture read-through, S115 re-cut, both counters, S166 + entry, seven record repairs, ledger migration, wave evidence | §Round 67 bullets 3–11 | `e075fc50` |
| scribe's four entry corrections + fetch receipt + its seat report | §Round 67 (appended) | `cf26e146` |
| wave `kagi-r67-w1` results receipt | §Round 67 (appended) | `c686b035` |
| this report (fleet repo) | — | fleet commit by `fleet-commit.sh --as kagi` |

## Before → after measurements

### C1 — freshness (`C1_READTHROUGH`)

Counting command (the same one for both sides; the BASE side is a
`git archive 076701a` extraction, the candidate side is the lane tree):

```
bash plans/round-67-c1.sh --tree <TREE> --base-tree <BASE extraction> [--scratch DIR]
```

| side | measured | receipt |
|---|---|---|
| BASE `076701a` | `C1_READTHROUGH: bound=36 located=35 caught=0/6 guard=0` rc 1 | `.ufo/waves/round-67/final/c1-base.txt` |
| candidate `e075fc50` | `C1_READTHROUGH: bound=36 located=36 caught=6/6 guard=1` rc 0 | `.ufo/waves/round-67/final/c1-candidate.txt` |

The six mutations (repoint to a same-size different-digest body, truncate by
one byte, delete the body, absolute location, `..` location, non-locating
quote) each read `FAILED` with `FINDING SC_CAPTURE id=<mutated id> <expected
reason>` taken from the candidate gate's stdout. Guard legs: (a) the clean tree
prints the CLEAN summary with counts equal to the counter's own derivation;
(b) selftest 50 cases and the gate's 89; (c) the BASE gate is CLEAN on the
repointed tree — the blindness witness, `.ufo/waves/round-67/base/blind-gate.txt`
(that receipt is byte-identical to the clean-tree receipt by construction, so
its *header* carries the mutation); (d) the fleet wrapper reads `kagi ok`;
(e) the 120+1 prose rows produce no `SC_CAPTURE`; (f) the candidate's
`corpus/rendered-text-v1.py` hashes to the committed one — a tree shipping a
truthy normalizer reads `caught=5/6 guard=0` (measured; the exploit tree is
described in `.ufo/waves/round-67/w1/R67Sentinel.md` V-1).

### C2 — calibration (`C2_FIDELITY`)

```
bash plans/round-67-c2.sh --tree <TREE> [--scratch DIR]
```

| side | measured | receipt |
|---|---|---|
| BASE `076701a` | `C2_FIDELITY: mismatches=7 population=7 guard=1` rc 1 | `.ufo/waves/round-67/final/c2-base.txt` |
| candidate `e075fc50` | `C2_FIDELITY: mismatches=0 population=7 guard=1` rc 0 | `.ufo/waves/round-67/final/c2-candidate.txt` |

Legs L1–L7 (each prints `LEG L<n> verdict=…`): scorecard honest-stop cell,
SKILL pin vs instrument, coverage-map row, sentinel ledger row, claims.json
ids, reconstructed receipt vs a fresh BASE run (four findings re-derived),
`used-by` corrigendum. Two forgeries of the receipt (a false `findings=0` line;
a deleted finding) each read `mismatch` on L6 only.

## Sources & frontier

Census command, run at round start and at round end:

```
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kagi
```

| side | verdict | rows |
|---|---|---|
| start (BASE) | `kagi ok` rc 0 (receipt `.ufo/waves/round-67/base/census-start.txt`) | 156 |
| end (candidate) | `kagi ok` rc 0 (receipt `.ufo/waves/round-67/final/fleet-census-candidate.txt`) | 157 |

The lane's own gate reads `SOURCES_CENSUS: CLEAN (rows=157 A=140 B=2 C=15
queued=3 mined=137 rejected=17 entries_sourced=27 legacy=21 captures=157
inrow=16 inrow_only=0 inrow_nonreproducing=12)` at round end and
`SOURCES_CENSUS_SELFTEST: PASS (89 cases)`.

- **Rows added by tier:** one, tier A (`mined`): **S166** — RFC 9530, HTTP
  Digest Fields, §1.2, opened live 2026-11-08, capture 67152 B, quote
  `Receivers can validate the digest for integrity purposes.` located once
  under `rendered-text-v1`. No tier B; no tier C.
- **Rows touched old→new:** **S164** `used-by` gains
  `corpus/knowledge/source-capture-binding.md`; **S115**'s fetch row column 13
  re-cut from the terminal-period sentence (count=0) to the 18-word sentence
  (count=1). No `status` or `recheck` change; the round-66 `used-by` cells the
  round-66 closure routed are logged in `corpus/lessons/round-66.md`
  §Corrigendum (six changed, one row appeared, S113 named).
- **Frontier rows advanced:** capture read-through moves from frontier to core
  as the capability row "capture read-through in the source census"
  (`SCORECARD.md` §Capabilities, first-working round 67); the round-66
  "held-out instrument" and round-63 "negation scope" frontier rows are
  untouched. The new entry's ground (provenance binding, two digest layers)
  was not on the coverage map before this round.
- **Assimilation: none** — no theme from `/home/vgpnk/Projects/shokuknow/merge/kagi/`
  was opened or adopted this round; the round's claim budget went to C1's
  capability and C2's repair, and adopting a package would have added a
  population that no frozen counter of this round can measure. The consideration
  sweep (`considerthese/2026-10-26.md`) found proposal 2 already implemented as
  the `lane-status:` line, proposal 1 an operator-policy question, proposal 3 a
  defect-state qualifier with no live defect to name, and proposal 4 a file
  inside the operator-authored `considerthese/` (never edited) — none adopted,
  none edited.

## Pre-file falsification ledger

`.ufo/waves/round-67/claim-falsification.tsv`: 9 rows, all five columns,
C1 and C2 covered, every attack seat (R67Reviewer, R67Critic, R67MutGate,
R67Sentinel, R67Connector, R67Revenger) in the artifact column, three
`falsifies-wording` rows narrowing to `plans/round-67.md` (A2, A1, A5).

```
python3 /home/vgpnk/Projects/shokunin/scripts/hyaku/prefile-falsification.py --lane kagi --round 67 --wave kagi-r67-w1
PREFILE-FALSIFICATION: pass claims=2 rows=9 attack_seats=6 findings=0
EXIT=0
```

`--wave kagi-r67-w1` is required because the gate's default wave name is `w1`
and the driver wrote `kagi-r67-w1-results.json`; with the default it reads
`SETUP wave-missing`, which is a naming mismatch, not a missing artifact (the
receipt exists and is committed).

## Trend verdicts

- **expansion — improved.** A capability row entered (capture read-through),
  a knowledge entry landed on ground the coverage map did not hold, one tier-A
  row was admitted, and the map gained the two missing rows (the round-66
  carrier entry and this round's). The active documented scope is unchanged
  (PROVINCE.md helds); no sibling's ground is absorbed.
- **quality — improved.** The lane's census now reads bytes for 36 declared
  captures and refuses six defect classes it previously read `CLEAN` on; its
  selftest grew 78 → 89; two counters are self-witnessing (guard f, the
  stub-gate replay, the two receipt forgeries); the seven record surfaces the
  round-66 closure graded `harmed` now re-derive clean. Ceilings are named, not
  smoothed (below).
- **discernment — improved, with the caveat stated.** The wave's attack seats
  produced five blocking findings, each of which changed the frozen instrument
  or its wording before the report (A1, A2, A5 + two guard fixes); the round
  mined five mistakes into `corpus/lessons/round-67.md`, **three of them the
  L1's own** (a plan citing scratch receipts, a classifier no implementation
  could satisfy, a heading the declared-axis gate rejects) and two forced by
  the instruments' construction. A2 and A5 were recorded after the first lane
  reading of their claim — they record what the landed instrument must enforce
  and change no target, label or population; that ordering is stated here
  because a closure will ask.

## Ceilings and routed items

- **C1 ceilings:** a body rewritten together with its row passes; prose
  locations (121, 17 of them containing `/`) are counted and never opened;
  `located` is a presence property (a one-token quote locates); row identity is
  counter-guarded (A2.4), not gate-guarded.
- **Gate-level survivors** (revenger C1/C2/C3, sentinel V-4, mutgate survivors):
  the prose escape hatch (a trailing space or CR in a location cell, a
  comma-joined value, `//etc/passwd` and `~/path` all read `CLEAN` with
  `path_rows=35`; a whole-file CRLF save reads `path_rows=0`); an in-tree
  hardlink to an out-of-tree body binds until the external byte changes
  (point-in-time by design); column 15's normalized digest is never recomputed
  (the round-66 M66-10/QM92 class is still gate-blind); a tampered
  `corpus/rendered-text-v1.py` reads CLEAN through the gate when the gate ships
  in the audited tree (counter-side guard f binds it for this round's
  measurement; the gate cannot vouch for itself). Routed to round 68 as checked
  classes, with the revenger's proposed checks recorded in
  `w1/R67Revenger.md`.
- **C2 scope:** the two routed closure items that live in the fleet-root report
  (its §6.4 LOG pointers / uncited commits and §6.5 controls battery) are
  outside a lane's write scope and are not legs (Amendment A1 item 1).
- **Carried, not caused here:** `ADJACENCY_SCOPE: DEFECT` (the same breadth
  debt rounds 58–66 named: `breadth_drift=5 breadth_unverified=1`);
  `claim-ledger.sh cells` reads `SETUP` on an unrecognised historical heading
  `## Round 63 — planned` (present at BASE, line 2181) — measured at BASE and
  routed; `claim-ledger.sh citations` ⇒ `CITATION_GATE: BROKEN (cites=5226
  docs=172 unresolved=28 ephemeral=0 labeled=24)` — all 28 are in historical
  documents (round-61/64/65/66 lessons and spot-checks), none in a round-67
  document; the two round-67 references that read unresolved before the entry
  landed now resolve (measured this round).
- **Sentinel V-3** (a round-66 evidence file reconstructed under
  `.ufo/waves/round-66/`) is the L1's C2 leg L6, named in `plans/round-67.md`
  §C2 and Amendment A1; it is inside the lane's write scope by the plan, not a
  seat writing outside its bounds. **V-5** (the fleet-root `__pycache__`) is
  operator-side and still open.

## Stale-lane

Respawn-per-round driver; no other mission of this lane is open.

## SHONEN

[~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — pointers: `SKILL.md` §decision/failure tables and the gate registry; this round's census row now states `--selftest` 89 cases, re-derived by `python3 corpus/self-counts.py` (`SELF_COUNTS: POLICY (claims=63 stale=0 …)`, the two POLICY rows pre-existing).
[~] At least one end-to-end domain task executed and logged — pointer: `LOG.md` round-3 entry (stdin→lock→tmux→serve to the 1Password auth gate, exit 1) plus this round's instrument runs (`c1-candidate.txt`, `c2-candidate.txt`).
[~] Instructions executable by an agent without oral context — pointers: `corpus/sources-census.sh --selftest` 89 cases, `plans/round-67-c1.sh --selftest` 50, `plans/round-67-c2.sh --selftest` 24, `corpus/claim-ledger.sh docs` CLEAN; every command in this report was run this round.
[~] No cross-domain bleed (PROVINCE.md still accurate) — pointers: `bash corpus/scope-gate.sh` reads `ADJACENCY_SCOPE: DEFECT` (the carried breadth debt, named above); the connector sweep found no sibling claiming capture-binding or RFC 9530 (`w1/R67Connector.md`).

No box is `[x]`: no named non-author verifier has judged this round yet; the
closure's spot-check is that judgment.

## Tool installs

None this round — no seat installed or upgraded anything (sentinel's audit
records the same for the whole wave).
