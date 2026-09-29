# Round-14 executor seat — Lifecycle / Promotion gates / Round-robin review

Author: `R14ExecLifecycle` (executor seat). Reader: protocol L1.
Scope: read-only review of the round-14 candidate `PROTOCOL.md`. No gate/test/self-test was run
(brief constraint); no source file was edited; nothing was written outside this file.

## Baseline (verified, per the parent's baseline correction)

| rev | `PROTOCOL.md` blob | lines / bytes |
|---|---|---|
| `310967c:PROTOCOL.md` (identical to `HEAD` and to `2d19a64`) | `338956d` | **541 / 50,603** |
| `f3cbdcf:PROTOCOL.md` (earlier source snapshot) | `a07e350` | 526 / 49,269 |
| worktree candidate (uncommitted) | — | 464 / 40,079 |

`git rev-parse 310967c:PROTOCOL.md HEAD:PROTOCOL.md 2d19a64:PROTOCOL.md` → `338956dfd94edbba771faefc67293bfa54ff9b70` three times; `git diff --stat 310967c HEAD -- PROTOCOL.md`
is empty; `f3cbdcf` differs by `2d19a64`'s +15-line sibling-mint commit.

All deltas below are **`310967c:PROTOCOL.md` vs the worktree candidate**. Method:
`git show 310967c:PROTOCOL.md > /tmp/base.md`, slice both files to the three sections
(base `1,320`; candidate `1,286`), `diff -u`, then a word-level `difflib.SequenceMatcher` pass to
separate re-wraps from real deletions.

## Finding — one material defect (introduced by this candidate)

**Clause.** `## Round-robin rounds` → "Integrator of record" → `PROTOCOL.md:163-164`.

Deleted against the baseline (`310967c:PROTOCOL.md:195-196`), the appositive:

> `— the statuses it wrote, or a statement of why none was writable —`

Provenance (observed):
- present in the baseline (`310967c:PROTOCOL.md:195-196`, `HEAD` today);
- introduced deliberately by `640a4c5` (round 10, *"closure actuator landed and executed"*),
  i.e. in the same commit that instantiated closure — `git log -S 'why none was writable' -- PROTOCOL.md` → `640a4c5` only;
- preserved by this round's own per-clause draft (`.ufo/waves/round-13/scout-compaction.md:686-702`,
  DRAFT C5, phrase at `:697`), and **absent from the landed candidate and from
  `.ufo/waves/round-13/PROTOCOL.compact.md:163`** — so the loss happened after the draft, silently.

Why the existing wording fails:
1. *Undefined term in a conformance rule.* The candidate's rule is "a protocol-lane report carrying
   no closure record is an incomplete report whatever else it contains" (`PROTOCOL.md:164`), and it
   is reused at `:167` ("The closure record is a gate, not prose"). The pair never says what a
   report must carry to **be** a closure record: the deleted half was that definition, and
   `grep -c 'closure record' PROTOCOL-APPENDIX.md` → `0`. [observed]
2. *The rule becomes unsatisfiable where it should be vacuous.* Step 4 writes an entry only when a
   lane-round terminates — "Write the entry for round `N` as soon as one lane's Nth lane-round
   terminates" (`:208`) — and a fabricated row is itself a defect ("A row contradicting evidence is
   a conformance defect of the entry", `:242`). So for a pass in which no lane-round terminated and
   no older row is unresolved there is no writable closure record, and the honest statement that
   none was writable no longer satisfies the clause. [observed premises; **inference** that the
   integrator's own report is then guaranteed `incomplete`, and infallibly so once the fleet is
   caught up]
3. *The move's own gate cannot see it.* Census row `R32`
   (`.ufo/waves/round-13/obligation-census-r13.tsv:40`) reduces this obligation to the predicate
   `incomplete report`, which the truncated sentence still matches; `anchor-phrases.txt` contains
   no phrase from the deleted half (`grep -c 'closure record\|writable'` → `0`); the appendix has no
   row for it. The already-green gate (8 checks, 169/169 predicates, 61/61 anchors) therefore
   reports clean while the obligation is narrowed — the exact class the appendix's own
   "Census blind mass" row (r13) warns about. [observed]

Material because the sentence gates the integrator's own report — the closure artifact every other
clause keys off — so the loss lands on this round's axis (protocol soundness) and feeds gate
integrity (the closure evidence it grades).

### Minimal replacement (this clause only)

old (`PROTOCOL.md:163-164`):
```
required template corrections are named in its report. Its closure artifact is its own round report:
a protocol-lane report carrying no closure record is an incomplete report whatever else it contains.
```
new:
```
required template corrections are named in its report. Its closure artifact is its own round report:
a protocol-lane report carrying no closure record — the statuses it wrote, or a statement of why
none was writable — is an incomplete report whatever else it contains.
```
Restores the deleted appositive verbatim from `310967c:PROTOCOL.md:195-197`; adds no new rule.
New line widths 96 / 70 (the file wraps ≤100; the untouched line 163 is 100).

## Checked clauses — no correction warranted

- **Lifecycle (`:7-39`).** Chain unchanged. *Shonen* mint bar (`:14-18`) unchanged, predicate
  intact (census `L1`). *Shokunin* (`:19-20`) / *Jin'i-ryu* (`:22-23`) unchanged in meaning
  ("with the main repo aggregating" → "the main repo aggregates"). *Sibling mint* (`:21-36`) is
  preserved from `2d19a64` — every content item of (a)–(d) survives, including the `MINT.md`
  payload and the write prohibition (census `L8`–`L18`); the added words "before roster rows
  exist" (`:30-31`) assert nothing the baseline's (d) did not already imply (see O2).
  *Dormancy* (`:37-38`) reworded to "Two consecutive dispatched-and-reported rounds with no `LOG.md`
  activity flag a shonen **dormant**"; same subject, same two-round test, same "review trigger,
  never an automatic retirement" (census `L2`). No correction.
- **Promotion gates (`:41-56`).** Preamble (`:43-44`) unchanged. *shonen → shokunin* (`:45-53`):
  the explicit four-box list is replaced by a reference — "the four boxes of the `SHONEN.md` seed
  below, rendered box-for-box and changeable only in the same edit as this gate text" — which is
  not a deletion of obligation: `310967c` already declared the seed the box-for-box rendering of
  that minimum, the seed block still holds exactly four boxes with the same
  change-in-the-same-edit binding (seed below, §File contract), and the `[x]`/`[~]` non-author rule
  is intact. *shokunin → jin'i-ryu* (`:54-56`) unchanged (latent gap → O3). The `MANIFEST.json`
  "rank is updated" clause names a field that exists (`roster[].rank` = `shonen` ×6, `MANIFEST.json`).
  No correction.
- **Round-robin rounds (`:58-285`).** All clauses re-read. Every other delta against `310967c` is a
  rationale, example, or superseded-form deletion, not an obligation — quoted so the L1 can audit
  them: "the driver's template is part of the contract's delivery mechanism … would void" (rationale;
  the `lane_prompt()`-text duty survives at `:67-68`); "and is skipped by the ones that don't" and
  "a prompt-fidelity defect named in round notes does not fix the template" (rationale);
  "a late-joining or respawning lane's `round-3` is not the same event as another lane's" (example);
  "because the driver completes the mission the instant the file reaches disk" (rationale);
  "and a lane whose report is still uncommitted when its mission completes has not satisfied this
  clause" (superseded form — the round-12 rule that replaces it is kept verbatim: "recorded on its
  termination evidence with the durability debt named; the next pass re-grades it `failed` for want
  of a landed report if the successor never lands it"); "a sweep is the last resort because it
  freezes the on-disk bytes, unfilled placeholders and all, into a permanent object" (rationale;
  appendix "Orphaned report"); the two stale-lane rationales, incl. "so the driver respawns it on a
  fresh prompt" and "the driver's respawn path is unreachable while its daemon is up (step 4), so
  nothing in this section terminates live work" (the load-bearing half, "recording `failed` is a
  ledger act, not a kill", is kept); "Waiting for all eight counters to reach `N` waits forever"
  (rationale — and "eight" is already stale: the fleet is nine lanes incl. `kama`);
  "its `lane-dead-no-report` retry path is unreachable" (rationale; appendix "Liveness probes");
  "the counter the lane actually held is what makes such a row falsifiable" (rationale);
  "(e.g. `round-2/AGGREGATE.md`)" (example). The two insertions ("Non-closure entry types",
  "History is pinned") are round-13 work already carried by appendix rows and by
  `closure-check.py` (m9 → `history_pin_unanchored`). No correction beyond the finding above.

## Observations (pre-existing or out-of-section; no draft text supplied)

- **O1 — the recorded "before" is the wrong snapshot.** `.ufo/waves/round-14/plan.md` (M1) and
  `data-walk.md` (§Scope and baseline) cite `f3cbdcf` = 526 lines / 49,269 bytes as the "current
  committed baseline". The pre-move baseline is `310967c` (= `HEAD`) = **541 / 50,603**; `f3cbdcf`
  predates `2d19a64`, which added the 15-line sibling-mint bullet. The file-level comparison is
  unaffected (the candidate is 464 lines either way), but a before→after booked as `526→464`
  understates the measured reduction, which is `541→464`. Fix belongs to the scribe/scorecard, not
  to `PROTOCOL.md`.
- **O2 — R1 vs the probational sibling (pre-existing).** `:60` scopes round-robin dispatch to
  "up to one swarm lane per rostered shokunin", while Lifecycle `:30-31` requires a lane-initiated
  sibling to be dispatched through "at least three verified rounds … before roster rows exist".
  Live support: `kama` is dispatched (`.ufo/state/kama.round`, kama-r1 commit `74768ab`) while
  `MANIFEST.json` `roster` still holds 6 ids and no `kama`, and `ROADMAP.md`'s table likewise (its
  one `kama` mention is the watchlist, not a row). Both halves exist in `310967c` (from `2d19a64`);
  the candidate only sharpens the non-rostered case by adding "before roster rows exist". The
  appendix's "Lane universe" row (r13) already records the closure gate failing to parse kama's
  dispatch line. Not drafted: one-clause scope, and it predates this move — L1's call whether to
  route it.
- **O3 — the jin'i-ryu gate names no verifier (pre-existing).** The section promises "every gate
  names its verifier and its evidence" (`:43-44`), but *shokunin → jin'i-ryu* (`:54-56`) names no
  verifier (its evidence is the `LOG.md` record). Identical in `310967c`, and latent rather than
  live: all six `roster[].rank` values are `shonen`, so no promotion has been made. Not drafted.
- **O4 — pointer only, outside the reviewed sections.** §Invariants (`:404-407`) enumerates the
  integrator's main-repo writes as `PROTOCOL.md`/`ROADMAP.md`/report plus `MANIFEST.json` `rounds`
  appends, without `PROTOCOL-APPENDIX.md` (new in this move) or `.ufo/history-pin.json` (the new
  sixth write declared at `:159`). Both are declared in §Round-robin (`:155`, `:159`), so the
  normative home exists; flagged for the L1/scribe, no draft (out of the Lifecycle / Promotion
  gates / Round-robin set). Complementary and non-overlapping: the gate seat
  (`.ufo/waves/round-14/scratch/gate-correction.md`) files the dropped `CORPUS.md` writer in the
  same enumeration with a replacement at `PROTOCOL.md:404`; nothing there touches the
  `:163-164` clause drafted above.

Verification limits: no gate, self-test, build, or formatter was run, and the candidate was not
modified — all statements above are from file and git reads only.