# kagi — round 64 (attempt 2)

Lane: kagi (secrets & vault ops). Round 64, attempt 2. Claim BASE
`09cbee831d57be7c4edfbe77bf238f46bf729047` (round-63 verifier spot-check tip).
Predeclaration `dff0929c0e084822b0fe32e0d164534c768f97fe` (`plans/round-64.md`, including
**Amendment A1**), landed before any candidate work. Wave `kagi-r64-w1`, 16 seats, one v1
wave. Lane HEAD on landing: `525c69de649424011276dc05cba24c891ebf7ad0` (round commit
`6593f7213334b5eb87f182b1693a48e2ae992e6d`; then the two >1 MiB capture bodies in
`e5668ffc…`, the end census in `4aab7fa6…`, the ledger-verify receipt in `6178d472…` and
its final-tree correction in `525c69de…`; `git ls-remote origin refs/heads/master` prints
`525c69de…`, `ahead=0`).

## Work performed

**Declared claims** (both frozen before any candidate work):

- **C1 — calibration.** A held-out fixture set, sealed before the hardening, is measured
  against `plans/round-61-c1-check.py`: `C1_HELDOUT` **heldout 8 → 0** over population 8
  (five held-out forgeries rejected, three held-out benign rewrites accepted), with the A4
  lookup-table vehicle refused on the held-out set. Target axis: the mismatch between the
  lane's self-assessment (the checker implements a polarity grammar) and observed
  behaviour (a fixture-lookup checker reached `accepted=0 rejected=0` on the committed
  tables).
- **C2 — operability.** The C2 counter terminates end-to-end and prints one verdict line:
  `C2_REFUSAL … terminates` **0 → 1** with `killed=5 population=5 guard=1` inside
  `timeout 1200`; `C2_RECURSION_BOUND=0` still does not terminate inside 240 s.

Work items:

- **Amendment A1 — the pre-amendment held-out census was wrong (`.ufo/waves/round-64/base/census-a1.md`).**
  The L1 re-measured all 19 rows at an extracted `09cbee8` tree before building anything:
  F1/F5/F9/B3 were already rejected at BASE, F3/F4 were accepted *correctly* (hedge and
  idiom), P1/P2/P3/P5 were already accepted, P4 was an unmeasured slim-tree artifact, and
  B4 was accepted (so it could not be a control). The frozen population was therefore
  re-cut to the five forgeries the checker genuinely accepts (F2, F6, F8, F10, B4) and the
  three benign rewrites it genuinely rejects (P6, B5, P7 — P7 added), resealed at
  `b0f51e2a7e7b5b62efa17c91761e24e01fe1a3ff384181e468b628544faa93c2`, with the
  superseded sha retained for audit. The guard legs, target and POP are unchanged.
- **C1 instrument.** `plans/round-61-c1-check.py` hardened with the six mechanisms A1 names
  — I7 pair assertion (a denial after the pair), the single-mechanism rule (I5), the
  `NO_NEW` assertion (I4), the every-pair-own-subject rule, the subject-negatedness guard,
  and parenthetical/em-dash masking in the binding window, plus the `not less than` idiom.
  `C1_CHECK_SELFTEST: PASS (cases=111)`; the re-derived BASE line is
  `C1_ROUTED: value=0 population=7 …` on the unmodified copy.
- **C1 counter.** `plans/round-64-c1.sh` — measures the sealed table (`sha256sum` checked
  first; a mismatch is SETUP), H at `value=0` and Q at `value>=1`, with guard legs `real`,
  `selftest`, `resid` (the round-63 counter re-run), `stub` and `vehicle` (the A4
  lookup-table checker built from the plan's description, required to read
  `accepted=0 rejected=0` on the round-63 tables and `heldout>=1` on the sealed set).
  `C1_HELDOUT_SELFTEST: PASS (cases=23)`.
- **C2 counter.** `plans/round-64-c2.sh` — the round-63 five legs plus `terminates=` and
  `bound=` fields and the explicit `C2_RECURSION_BOUND` flag: at 1 the l3/l4 battery
  delegation runs with `R63_CONTROLS_FIXTURE_ONLY=1` and never re-enters a counter; at 0 it
  delegates to the full battery (the old behaviour). `C2R64_SELFTEST: PASS (cases=21)`.
  `plans/round-63-c2.sh` gains the one-line pass-through; its selftest still reads
  `PASS (cases=13)`.
- **Controls battery.** `plans/round-64-controls.sh` — the two counter stubs (C1-F9,
  C2-F7), the **C2-BOUND refutation control** (bound off ⇒ no verdict line inside 240 s),
  the BASE-census NOWORK controls, the positive controls and the round-63 battery
  re-emitted as `PRIOR-*` rows. `CONTROLS_SELFTEST: PASS (cases=36)`.
- **Routed receipt.** `plans/round-64-routed.sh` — `ROUTED: d1=1 d2=1 d3=0` (see *Routed
  defects*).
- **Frontier step.** Twenty pages opened live 2026-11-08 (`capture/notes.md`, 27 locate
  probes): four admits (S145 the ISSTA '24 equivalent-mutant paper, S146 the *Advances in
  Computers* survey chapter, S147 Stryker's tool-level page, S148 the BioC deposit
  re-opened and superseding S143) and six rejects with reasons and flips (S149 Wikipedia,
  S150 PIT mutators, S151 PIT FAQ, S152 arXiv 1909.02196, S153 a 404 docs path, S154 the
  OpenBao tree sweep). Six further OpenBao pages opened this round are carried by S154's
  sweep cell instead of being minted as rows (the sweep is one absence claim).
- **Corpus + records.** Entry `corpus/knowledge/claim-instrument-heldout.md` (provenance
  trio, `source: S145`, 45 entries row-linked); `corpus/QUALITY.md` QM85/QM86;
  `SKILL.md` three gate-registry rows; `corpus/lessons/round-64.md` (Gate over 20 pages,
  Mistakes M64-1…M64-4, corrections, routed dispositions, wave); `corpus/README.md`
  coverage row; `corpus/claims-declared.tsv` round-64 rows; three new ledger rows
  (R64-01…R64-03) and a 161-row re-stamp of every artifact this round changed.
- **Attack seats.** The critic re-derived the whole census and produced 16 findings
  (`.ufo/waves/round-64/build/R64Critic/critique.md`); the reviewer built 12 new forgery
  and 6 new benign trees; two mutation-testers covered the checker and both counters; the
  sentinel and connector audited the round's artifacts and the sibling lanes; the
  revenger drew the C2 recursion graph and measured its depth.

## Landed changes

| path | change |
|---|---|
| `plans/round-64.md` | frozen plan + Amendment A1 (census re-measured, seal re-cut) |
| `plans/round-64-heldout.tsv` | the sealed held-out table (20 rows, sha `b0f51e2a…`) |
| `plans/round-61-c1-check.py` | the six hardening mechanisms + 9 class selftest cases (2154 lines) |
| `plans/round-64-c1.sh` | the `C1_HELDOUT` counter (seal check, five guard legs) |
| `plans/round-64-c2.sh` | the bounded `C2_REFUSAL` counter (`terminates=`, `bound=`) |
| `plans/round-63-c2.sh`, `plans/round-63-controls.sh` | the `R63_CONTROLS_FIXTURE_ONLY` pass-through |
| `plans/round-64-controls.sh` | the pre-freeze battery (+ `C2-BOUND`) |
| `plans/round-64-routed.sh` | the D-63-1/D-63-2/D-63-3 receipt |
| `corpus/knowledge/claim-instrument-heldout.md` | new entry (held-out rule, bounds, falsifiers) |
| `corpus/QUALITY.md` | QM85, QM86 appended |
| `corpus/SOURCES.md`, `corpus/source-fetches.tsv` | S145–S154 (+10 rows, +10 captures) |
| `corpus/lessons/round-64.md` | the round lesson |
| `corpus/README.md` | coverage row + frontier line |
| `corpus/stamps.tsv`, `corpus/claim-ledger.tsv`, `corpus/claims-declared.tsv` | 161 re-stamps; R64-01…R64-03; round-64 claim rows |
| `SKILL.md` | three gate-registry rows (with the fail-closed SETUP rule pinned) |
| `LOG.md`, `SCORECARD.md` | the round entry, the pre-move and post-move sections, the next-round plan |

Every change is logged in `LOG.md` §"Round 64" and carried by the round commit
`6593f7213334b5eb87f182b1693a48e2ae992e6d` (with `e5668ffc359930417c0c6cc43703b1de75b9cd82`
for the two >1 MiB capture bodies); the lane tip is `525c69de…`. Wave evidence (`w1-spec.json`, `w1-dispatch.json`,
`w1.ready`, `w1-results.json`, `w1/`, `build/`, `capture/`, `base/`, `final/`,
`claims.json`, `claim-falsification.tsv`) is committed with it.

## Before → after measurements

**C1 — counting command and measured commits**

```
bash plans/round-64-c1.sh 09cbee831d57be7c4edfbe77bf238f46bf729047      # BASE
bash plans/round-64-c1.sh --tree .                                     # candidate
```

- before (measured against `09cbee8`): `C1_HELDOUT: heldout=8 population=8 guard=0
  (real=1 selftest=0 resid=1 stub=1 vehicle=1)` rc 1 — 508 s
  (`.ufo/waves/round-64/final/c1-base-counter.txt`).
- after (candidate): `C1_HELDOUT: heldout=0 population=8 guard=1 (real=1 selftest=1
  resid=1 stub=1 vehicle=1)` rc 0 — 670 s, per fixture
  `F2=value1 F6=value1 F8=value1 F10=value1 B4=value1 P6=value0 B5=value0 P7=value0`,
  unmodified `value=0 bits=i1..i7=1`, `resid` `C1_RESIDUAL: accepted=0 rejected=0
  population=10/6 guard=1`, the stub refused, the vehicle `heldout=5`
  (`.ufo/waves/round-64/final/c1-heldout.txt`).
- L1 census that founded the population: `.ufo/waves/round-64/base/census-a1.md`
  (per-fixture table, 19 rows re-measured); the independent seat re-derivation is
  `.ufo/waves/round-64/w1/R64ScoutPreState.md` §2 (agrees: heldout 8).

**C2 — counting command and measured commits**

```
timeout 240  bash plans/round-63-c2.sh --tree .                        # BASE instrument
timeout 1200 bash plans/round-64-c2.sh --tree .                        # candidate
C2_RECURSION_BOUND=0 timeout 240 bash plans/round-64-c2.sh --tree .    # refutation
```

- before (BASE): rc 124 at 240 s, no verdict line; the round-63 receipt is 7 bytes
  (`.ufo/waves/round-63/final/c2-refusal.txt`), and the round-63 L1 measured rc 124 at
  900 s and 1500 s (`.ufo/waves/round-64/base/c2-e2e-head.txt`).
- after (candidate): exactly one line —
  `C2_REFUSAL: killed=5 population=5 guard=1 (l1=1 l2=1 l3=1 l4=1 l6=1 selftest=1 real=1
  terminates=1 bound=1)` — rc 0 in 285 s, inside `timeout 1200`
  (`.ufo/waves/round-64/final/c2-refusal.txt`).
- refutation: `C2_RECURSION_BOUND=0 … timeout 240` ⇒ rc 124, no line
  (`.ufo/waves/round-64/final/c2-bound-off.txt`); the battery's `C2-BOUND` control reads
  `match` (`.ufo/waves/round-64/final/controls.txt`).

**Pre-freeze battery** `bash plans/round-64-controls.sh` on the candidate ⇒
`CONTROLS: match=3 mismatch=6`, rc 1: the two stub counters refused, `C2-BOUND` and both
positive controls `match`, the two NOWORK controls `mismatch` because the battery's NOWORK
populations are the BASE census (pre-freeze semantics — the same shape round 63 recorded).

**Gates on the candidate** (receipts under `.ufo/waves/round-64/final/`):

| gate | reading |
|---|---|
| `corpus/sources-census.sh` | `SOURCES_CENSUS: CLEAN (rows=153 A=137 B=2 C=14 queued=3 mined=134 rejected=16 entries_sourced=24 legacy=21 captures=153 inrow=16 inrow_only=0 inrow_nonreproducing=12)` |
| `corpus/claim-ledger.sh docs` | `DOC_AUDIT: CLEAN (entries=45 row_linked=42 by_hand=3 undeclared=0 missing_ids=0 unpinned=0 duplicate_reasons=0)` |
| `python3 corpus/release-clock.py` | `RELEASE_CLOCK: CLEAN (on_release=32 bound=32 unbound=0 observed=32 fired=14 derived=17)` |
| `corpus/claims-declared.sh` | `CLAIMS_DECLARED: CLEAN (claims=53)` |
| `corpus/scope-gate.sh` | `ADJACENCY_SCOPE: DEFECT` — unchanged, the carried `breadth_drift=5 breadth_unverified=1`, named not absorbed |
| `corpus/claim-ledger.sh citations` | `CITATION_GATE: BROKEN (cites=4939 docs=163 unresolved=22 ephemeral=0 labeled=24)` — 22 unresolved, **all pre-existing** (round-34/35/43/44/51/53/54/58/59/62-era historical documents and two absent `.ufo/waves/round-59/final/` paths); none in a round-64 document |
| `corpus/claim-ledger.sh verify` | `CLAIM_LEDGER: POLICY (claims=99 policy=5 stamped=161)` with 20 FAIL rows (R11-08 … R62-06), all pinning historical counts (`stamps=125`, `rounds=73`, `entries=38`, `rows=114`) — pre-existing drift; the round's own rows R64-01/R64-02/R64-03 pass, every artifact this round changed was re-stamped (161 rows), and `DOC_AUDIT` is CLEAN |
| selftests | checker `cases=111`; `round-64-c1.sh` `cases=23`; `round-64-c2.sh` `cases=21`; `round-64-controls.sh` `cases=36`; `round-63-c2.sh` `cases=13`; `round-63-controls.sh` `cases=25` |

## Sources & frontier

`SOURCES: 143 → 153 rows` — counting command
`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` (before `143` at
`09cbee8`, after `153`), census
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root
/home/vgpnk/Projects/shokunin kagi` ⇒ `kagi ok … rc 0` both at round start
(`.ufo/waves/round-64/base/census-start.txt`) and at the end
(`.ufo/waves/round-64/final/sources-census.txt`).

- **Rows added by tier**: tier A +3 (S145 ISSTA '24 paper, S146 survey chapter, S147 Stryker
  tool page), tier A +1 superseding (S148 `supersedes S143 —` the BioC deposit re-opened),
  tier C +6 rejects (S149 Wikipedia, S150 PIT mutators, S151 PIT FAQ, S152 arXiv
  1909.02196, S153 a 404 docs path, S154 the OpenBao tree sweep). Status: `mined` +2
  (S145, S148), `queued` +2 (S146, S147), `rejected` +6.
- **Rows touched old→new**: none — no `status`, `recheck` or `used-by` cell changed in
  place this round. S143 keeps its row and its pin: the re-open measured its served body
  differing by **exactly one byte** (the service's `<date>` stamp 20261107→20261108,
  `cmp -l` at offset 127; `<passage>` 182 and `<text>` 180 unchanged), so the *shape* did
  not change and the plan's "supersede only if the XML shape changed" condition was not
  met by the content. S148 records the measurement rather than asserting the old digest
  still holds.
- **Frontier rows advanced**: S145 moves the equivalent-mutant ground behind the C2 kill
  contract from three statements (S137/S139/S140) to a second peer-reviewed attestation
  from a different group and venue; S148 moves the ConText carrier from "pinned but
  re-opened once" to "re-verified with a measured delta"; S154 records the lane's own
  product domain as silent on mutation testing (0 of 6363 paths).
- **Census before → after**: exit 0 at both ends (rows 143 → 153). Six further OpenBao
  pages opened this round are deliberately not rows: their shared finding is one absence
  claim, carried by S154's sweep cell, and pricing seven near-identical rejects as seven
  rows would be row inflation (CORPUS rule 4).
- **Assimilation: none** — no `merge/kagi/` theme was taken this round; the round's
  expansion is its own frontier (stated per the §10 contract).
- **Sources quoted in the lesson's Gate**: the twenty opened pages, each with URL, the
  2026-11-08 access date, a ≤25-word located quote and an admit/reject with its flip
  (`corpus/lessons/round-64.md` §Gate).

## Trend verdicts

- **expansion: improved** — the registry gains four admissible carriers (three tier A new,
  one superseding) and the entry `corpus/knowledge/claim-instrument-heldout.md` opens
  ground the lane did not hold: *on what evidence may a claim that an instrument
  implements a rule rest*. Counting: rows 143 → 153, entries 44 → 45
  (`DOC_AUDIT entries=45`), coverage map +1 row.
- **quality: improved** — the round's two instruments are the first in the lane whose
  *population was re-derived before it was frozen* (Amendment A1) and the first C1 claim
  whose test set is not the instrument's own tables; the C2 defect the round-63 spot-check
  routed is closed with a live refutation leg rather than a leg composition. Counting:
  `heldout` 8 → 0, `terminates` 0 → 1, both re-measured by the L1 at integration.
- **discernment: improved** — nine rows were priced against a bar (3 admits, 6 rejects with
  flips), the round's own census was falsified by measurement and re-cut, and the critic's
  C1-1 finding exposed a real process breach (the census file carried fixture strings) that
  the claim's wording now narrows and the census redacts. Ceiling: the reviewer's and
  critic's open findings (C1-3 through C1-10, C2-3 through C2-6) are routed, not closed,
  and no non-author closure has judged this round yet.

## Routed defects (work items, not claims)

- **D-63-1 closed**: `ROUTED: d1=1` — the A4 vehicle reads `accepted=0 rejected=0` on the
  round-63 tables (so it *is* the vehicle) and `heldout=5` on the sealed set (so the guard
  sees the lookup).
- **D-63-2 closed**: `ROUTED: d2=1` — one bounded `C2_REFUSAL:` line inside 1200 s, and
  none under `bound=0` inside 240 s.
- **D-63-3 open**: `ROUTED: d3=0` — the round-63 spot-check's D-B names six receipts under
  `.ufo/waves/round-63/final/`; the tree holds five (`ls` shows no `controls.txt`). The leg
  reads the tree it has and the missing receipt is routed to round 65 rather than
  reconstructed. This is a **record defect in the round-63 spot-check**, found by this
  round's receipt leg.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources
  Evidence: the round adds three gate-registry rows with verdict maps, falsifiers and
  pinned digests (`SKILL.md` §Gate registry — round-64 additions); `CITATION_GATE` reading
  and its pre-existing unresolved set are named above; no non-author verifier has signed
  this round yet.
- [~] At least one end-to-end domain task executed and logged in LOG.md
  Evidence: the two instruments run end-to-end on real candidate bytes —
  `C1_HELDOUT: heldout=0 population=8 guard=1` (670 s) and `C2_REFUSAL: killed=5 … 
  terminates=1 bound=1` (285 s) — with receipts under `.ufo/waves/round-64/final/` and the
  LOG entry citing them. The lane's operator-owned end-to-end vault task remains the round-3
  entry (`LOG.md:20`).
- [~] Instructions executable by an agent without oral context
  Evidence: four new runnable gates with self-invocations (`plans/round-64-c1.sh
  --selftest` `cases=23`; `round-64-c2.sh` `cases=21`; `round-64-controls.sh` `cases=36`;
  `round-64-routed.sh`), each named in `SKILL.md` with its exit map; the wave's 16 seat
  prompts were executed by seats that had no conversation context.
- [~] No cross-domain bleed (PROVINCE.md still accurate)
  Evidence: the round touches instrument and record surfaces only; the mutation-testing
  ground is cited from external peer-reviewed rows (S145/S146) and the lane's own domain was
  swept and found silent (S154); `ADJACENCY_SCOPE: DEFECT` is unchanged and the carried
  breadth debt is named, not absorbed (`.ufo/waves/round-64/build/R64Connector/sweep.md`).

## Round shape, seats, dead seats, totals

- One v1 wave, 16 seats, band 8–16 (`w1-spec.json`; `w1-dispatch.json`): 2 scout, 5
  executor, 2 scribe, 1 reviewer, 1 critic, 2 mutation-tester, 1 connector, 1 sentinel,
  1 revenger. Attack share 4/16 = 25 % on the addendum's literal list (reviewer, critic,
  mutation-tester ×2; no labrat seat exists), 5/16 = 31.25 % counting the sentinel.
- The L1 holds the canonical planner seat (the validator rejects `planner`); no residual
  `task` call was made — the round total is 16.
- Dead seats: **0** — 16 of 16 result records carry a non-empty final output
  (2108–16377 B, `w1-results.json`). One seat (`R64ExecControls`) delivered its receipts
  plus its final output instead of a `R64ExecControls.md` file; its
  `build/R64ExecControls/controls.md` states `SEAT-STATUS: complete`.
- Provider blocks: none this round.

## Inherited state (attempt 1)

Attempt 1 left three uncommitted items: `plans/round-64.md`,
`plans/round-64-heldout.tsv` and `.ufo/waves/round-64/{base,controls}/`. All three were
re-used and re-verified: the plan and the table were re-measured and amended (A1) before
being committed; `base/cheap-census.txt` was kept as attempt 1's start census; the
zero-byte `base/c1-base.txt` was discarded (it carried no reading) and the C2 head receipt
was written fresh. Nothing else was inherited.

## Stale-lane

`Stale-lane: no` — this is the lane's respawn-per-round driver's round 64 (attempt 2); the
round started at 02:06 and landed inside the mission window, and no other mission of this
lane is open.

## Tool installs

None this round (no package, binary or tool was installed or upgraded by the L1 or by any
seat; the pacman guard stayed in force and nothing routed around it).

## Open L0 questions

None opened this round. Carried and unanswered: `kagi | round-28` (the operator HOLD; the
lane's rounds run regardless), the `ADJACENCY_SCOPE` breadth debt, and — new this round —
the round-63 spot-check's D-B receipt population (routed to round 65 in SCORECARD §Round
64 — planned, item 2, because it is lane-repairable, not an operator decision).

## Limits of this report

- The two verdicts are single runs on this host under fleet load. C2's `real-attempts=`
  field exists because the seat measured its real-trial leg failing at load averages
  130–157 and passing at ~100; the integration run passed first attempt at 285 s of a
  1200 s budget, which is a termination claim on this load, not a liveness proof.
- C1's `killed`-style numbers are the counter's own; the vehicle leg is the only witness
  against a lookup table, and a lookup carrying one fresh entry per class would still pass
  (the plan's named ceiling, unchanged).
- The critic's C1-1 breach is recorded: the held-out fixture *strings* were reachable
  through the census file the checker seat was told to read. The census is redacted, the
  class-only prototype (`.ufo/waves/round-64/base/c1-fix-reference.md`) reproduces the same
  readings from mechanism descriptions alone, and the checker contains no string→verdict
  table — but the process claim ("the builder never saw a fixture") is not true of this
  round and is not made.
- No non-author closure has judged this round; admission is the closure session's call.
