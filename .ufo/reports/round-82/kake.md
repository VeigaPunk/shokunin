# kake — round 82 (attempt 1)

Lane `kake-shokunin` (web properties & publishing) · hyaku run 15 · Linux/omp · 2026-11-04
Base `419866015b1f58e01f061cde9a77d490653d3c76` · frozen contract
`082b7dd39053e5f96ca6c463da47a3e4d83d4580`, no amendment · carrier
`8abeccca6d318e9addb14f93a64beae2d4bc0d8b` · final lane tip
`9635bf015d443b8984f86251b7c38564862b21d8` (pushed; `git ls-remote origin refs/heads/master`
prints it).

Two claims, each on a distinct axis: **C1 — calibration** (score 2, the lowest non-retired axis):
the round-81 routed-defect queue closes. **C2 — freshness** (score 10, held): a second dated
GET-only capture feeds a capture-to-capture drift gate whose record re-derives from committed bytes.
Scores are held; a claim moves evidence, not a scalar. Everything below is author-side — admission
belongs to the non-author closure.

## Work performed

**C1 (calibration 2): the eight routed defects of the round-81 non-author closure close.** Population
is exactly `D1` … `D8` filed at `corpus/lessons/round-81-verifier-spotcheck.md` §7, frozen before any
seat ran; none added or dropped. Predicate `met <=> open == 0`, decided by
`python3 -B .ufo/waves/round-82/c82_defect_queue.py --root <tree> [--revision <rev>]` from lane bytes
and the fleet repo read-only — every item carries a state conjunct re-derived from a non-lesson file
plus a row conjunct only prose can carry (the item table is `.ufo/waves/round-82/contract.md` §C1).
The eight corrections landed: the `S433` registry cells moved (`recheck 180d → 2027-05-03`,
`used-by` gained the round-81 lesson); the mislabelled measured revision is corrected to the receipt's
own token `498a0969…`; the in-place rewrite of the round-81 filed report is named as an erratum at
`7678247a`; the seat byte count is re-derived as 3801; the two dead receipt paths are named and the
live ones pointed at; the stale `18/18` tally is superseded by a criterion grounded on the committed
`22/22`; the standing ledger gate is re-run and committed; and the round-80 pointer is corrected by an
appended `[r82-correction]` row. Evidence: `corpus/lessons/round-82.md` §Corrections,
`controls/after-c1-final.txt`, `controls/after-c1-tip.txt`.

**C2 (freshness 10): a second dated capture and an offline drift gate.** Capture B — three GET-only
requests to the declared `ds4cc.com` surfaces (`/`, `/robots.txt`, `/sitemap.xml`), one each, frozen
population — was taken at `2026-11-04T13:00:27Z`/`13:00:28Z` and committed under
`.ufo/waves/round-82/capture/`, its manifest the mechanical join of the frozen declaration. The new
tool `scripts/capture_delta.py` verifies every receipt in two capture trees against its retained body
and prints one stable line per surface; the counter `.ufo/waves/round-82/c82_capture_delta.py`
re-implements that verification independently and re-derives the record at a measured revision. The
record (`controls/after-c2-delta.txt`) reads `surfaces=3 identical=0 changed=3 added=0 removed=0`:
all three bodies and statuses identical between the two instants, while the header mapping moved —
`date`, `x-fastly-request-id`, `x-served-by`, `x-timer` on all three and `x-cache` on two. The
connector's cache-fill decode sharpened what that means: `x-github-request-id`'s trailing hex is the
cache-fill epoch and `expires` is that epoch plus `max-age` (600 s), both identical A→B, so both
captures observed the **same stored objects**; `body=same` says the edge served identical bytes at two
instants, not that the origin was read twice. Evidence:
`corpus/knowledge/capture-drift-validators.md`,
`controls/after-c2-final.txt`, `controls/after-c2-tip.txt`,
`controls/ctl-c82-identical-capture.txt`, `controls/ctl-c82-tampered-capture.txt`,
`w1/ConnectorC/cachefill.txt`.

**Frontier step.** `corpus/SOURCES.md` 192 → 193 rows: **S455** (RFC 9110 §8.8.1 Weak versus Strong
and §8.8.3 ETag, tier A) admitted after a fresh GET of `https://www.rfc-editor.org/rfc/rfc9110.txt`
returned the lane's known 502,941-byte body (sha256 `21c1cdce…47232a`, `cmp -s` exit 0 against the
retained copy), with raw-substring spans located by line and a 24-word admission quote. New entry
`corpus/knowledge/capture-drift-validators.md` on previously uncovered ground (cross-instant drift
plus validator semantics), with the recorded delta appended after capture B and a cache-fill erratum.
Census exit 0 at round start and end, `W04` 21 → 22. `corpus/QUALITY.md` gained the D6 superseding
criterion; `PROVINCE.md`, `corpus/README.md` and `SKILL.md` gained the round-82 appends; the main
capabilities table gained the drift-gate row.

**Instruments registered and re-bound.** `SKILL.md` §Round 82 registers the two gates and the tool
with entry commands, verdict maps, selftests and pinned proofs. The standing instrument-receipt gate
was **red at base** (exit 1: four round-80 paths unbound and a stale digest); it is re-bound at
`70c8241b` with 30 instruments and `missing_frozen=0`, and `--check` at `576cf76c` exits 0. This is
upkeep, not a claim.

**Wave.** One v1 wave, **13 requested seats** inside the run-15 band 8–16: scout 2, executor 3,
scribe 3, reviewer 2, critic 1, mutation-tester 1, connector 1; requested attack share 4/13 = 30.8 %
over {reviewer, critic, mutation-tester, labrat}. Spec `w1-spec.json`, dispatch `w1-dispatch.json`,
ready `w1.ready`, results `w1-results.json`. The L1 held the canonical planner seat (the validator
refuses `planner` as a swarm role); the planning data-walk rode `ScoutRecon`. **Settlement fell short
of the attack floor**: 7 seats produced non-empty output (6 of them a deliverable), 6 returned empty,
and **0 of the 4 attack seats settled** — a conformance defect recorded under **Wave accounting**
and **Conformance defects**, not smoothed over.

**Attack work done by the L1 instead.** Because `ReviewC1`, `ReviewC2`, `CriticClaims` and `MutC`
never delivered, the L1 ran an author-side mutation probe after both claims were measured: 3/5 C1
mutants killed and 2 survivors (the D4 constant equals the fixture's number; no fixture carries
`undisclosed=0 met=false`); 1/5 C2 mutants killed, 1 equivalent mutant and 3 survivors (no
equal-instant fixture, no dropped-A-surface fixture, a hard-coded `selftest_ok` masked by other
failing conjuncts). The two killer fixtures per counter are routed to round 83, with a disclosed probe
defect (the first C2 run resolved the tool path relative to the mutant and died for the wrong reason).
Evidence: `corpus/lessons/round-82.md` §Author-side mutation probe.

**Assimilation and proposals.** `Assimilation: none` is re-derived at the base blob (see **Sources &
frontier**). Of `considerthese/2026-10-26.md` Part 2, #2 and #5 are already implemented; **#4 (the
gate-agreement ledger) is the single still-unimplemented proposal**, recorded with its exact future
criterion in `.ufo/waves/round-82/w1/ConnectorC.md` §3 and held for round 83 rather than landed
mid-round.

## Landed changes

Every change is tied to the round-82 `LOG.md` entry (`## Round 82 — 2026-11-04`, appended at
`70c8241b`) and to its commit:

| Commit | Carries |
|---|---|
| `082b7dd3` | freeze: contract, both counters, `scripts/capture_delta.py`, junk and identical-capture builders, frozen population, base and control receipts |
| `62061ff9` | wave `w1` spec and validated dispatch (13 seats, band 8–16) |
| `8abeccca` (carrier) | the eight C1 corrections (`corpus/SOURCES.md` `S433` cells, `corpus/QUALITY.md` D6 criterion, `corpus/lessons/round-80.md` `[r82-correction]`, `corpus/lessons/round-82.md`), S455 and `corpus/knowledge/capture-drift-validators.md`, capture B with its manifest, the delta record, the tampered control, the ledger receipt, the census pair, `w1.ready`, and the wave's seat reports |
| `70c8241b` | `SCORECARD.md` round-82 block and move log, `LOG.md` round-82 entry, `PROVINCE.md` append, `corpus/README.md` coverage row, `SKILL.md` §Round 82 registry, both after receipts at the carrier |
| `576cf76c` | `corpus/knowledge/instrument-receipts.json` re-bound at `70c8241b` (30 instruments, `missing_frozen=0`) |
| `21deab2b` | the drift gate's row in the `SCORECARD.md` capabilities table |
| `bde1d0b6` | lesson `Assimilation`, the held `considerthese` #4 row and the `[r82-note]` verdict-scope correction; the connector's report |
| `bd1dcac7` | final after receipts for both claims at `bde1d0b6` |
| `a30c08f2` | the author-side mutation-probe section |
| `b6ae0ba6` | cache-fill erratum in the lesson and the drift entry; the connector's §6 and `cachefill.py`/`.txt` evidence |
| `3aac1cbc` | `w1-results.json`, `seat-failures.json`, `w1-accounting.json`, `make_accounting.py` |
| `9635bf01` | tip after receipts for both claims at `3aac1cbc` (final lane tip) |

## Before → after measurements

**C1 — calibration.** Counting command
`python3 -B .ufo/waves/round-82/c82_defect_queue.py --root . --revision <rev>`.

- Before, base `41986601`: `C1v1 revision=419866015b1f58e01f061cde9a77d490653d3c76 items=8 open=8
  closed=0 met=false`, exit 1 — `.ufo/waves/round-82/controls/base-c82-defect-queue.txt`.
- After, carrier `8abeccca`: `items=8 open=0 closed=8 met=true`, exit 0 —
  `controls/after-c1.txt`; at tip `3aac1cbc`: `met=true`, exit 0 — `controls/after-c1-tip.txt`.
- Controls: selftest `selftest: 11/11 passed`, exit 0 (`controls/c82-selftest-c1.txt`); junk tree
  whose lesson asserts all eight closed in prose reads `open=8 closed=0 met=false`, exit 1
  (`controls/ctl-c82-junk-queue.txt`, `tree_sha256=d9302da6…7797` in two identical builds).

**C2 — freshness.** Counting command
`python3 -B .ufo/waves/round-82/c82_capture_delta.py --root . --revision <rev> --work <scratch>`.

- Before, base `41986601`: `C2v1 revision=419866015b1f58e01f061cde9a77d490653d3c76 declared=3
  surfaces_a=3 surfaces_b=0 manifest_ok=0 receipts_ok=0 order_ok=0 floor_ok=0 determinism=0
  record_equal=0 selftest_ok=0 met=false`, exit 1 — `controls/base-c82-capture-delta.txt`.
- After, carrier `8abeccca`: `surfaces_b=3 manifest_ok=1 receipts_ok=1 order_ok=1 floor_ok=1
  determinism=1 record_equal=1 selftest_ok=1 met=true`, exit 0 — `controls/after-c2.txt`; at tip
  `3aac1cbc`: `met=true`, exit 0 — `controls/after-c2-tip.txt`.
- Controls: counter selftest `selftest: 9/9 passed`, exit 0 (`controls/c82-selftest-c2.txt`); the
  tool's own selftest `selftest: 14/14 passed`, exit 0, re-run live as the counter's `selftest_ok`
  conjunct; identical-capture control `order_ok=0 floor_ok=0 met=false`, exit 1
  (`controls/ctl-c82-identical-capture.txt`); post-data tampered control `receipts_ok=0 met=false`,
  exit 1 (`controls/ctl-c82-tampered-capture.txt`).
- Delta record: `surfaces=3 identical=0 changed=3 added=0 removed=0`, two runs byte-identical
  (`sha256 d43c0231…bd644a`), committed byte-exactly at `controls/after-c2-delta.txt`.

## Sources & frontier

Counting command:
`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` → **192 before → 193 after**
(`controls/census-before.txt` and `controls/census-after.txt`, both
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin
kake`, exit 0, `W04` 21 → 22).

- Rows added by tier: **1 tier-A row** — S455 (RFC 9110 §8.8.1 + §8.8.3), `kind=spec`, `status=mined`,
  `opened 2026-11-04`, `recheck 365d`, `used-by corpus/knowledge/capture-drift-validators.md,
  corpus/lessons/round-82.md`, inserted at `corpus/SOURCES.md:202` immediately after S454 so no
  earlier row moves.
- Rows touched old→new: **S433** — `recheck 180d → 2027-05-03`, `used-by
  corpus/knowledge/response-header-expectations.md → …, corpus/lessons/round-81.md` (D1; logged
  old→new in the lesson). No row was deleted, renumbered or rewritten.
- Frontier rows advanced: the publisher response-header frontier's capture ground now holds a
  cross-instant instrument — `corpus/README.md` gained the round-82 coverage row and the capture-drift
  frontier line, `PROVINCE.md` the §Round 82 append, and the `SCORECARD.md` capabilities table the
  drift-gate row.
- Gate: one admit (S455) and two rejects (§8.8.3's trailer paragraph and §8.8.3.1 *Generation* as
  anchors for that row; the `merge/kake` package). Quotes, access times and digest are in
  `corpus/lessons/round-82.md` §Gate.
- **Assimilation: none.** At base `41986601` (registry blob `1ffc61f1…435f`) the `merge/kake` package
  holds 129 staged rows against the lane's 192: **8 ids collide** with the identical source cell
  (S312, S329, S367, S372, S373, S374, S390, S409), **19 further staged rows** stage a source the
  lane already holds under another id, and **102 are unscreened** in a package last touched
  2026-10-24 — so no staged row is both unheld and screened, and none was adopted. Re-derived by
  `w1/ConnectorC.md` §2 and `w1/ConnectorC/evidence.txt` §D; nothing was written into the package
  repo.

## Trend verdicts

- **expansion — improved.** One new admitted knowledge entry on ground the coverage map did not hold
  (cross-instant drift detection plus RFC 9110 validator semantics), its `source:` citing the `mined`
  S455 row opened this round; the coverage map and province gained the corresponding rows. No
  admitted entry fails its bar.
- **quality — improved.** Two instruments landed with base, junk/identical and tampered controls and
  green selftests; the D6 criterion supersedes a stale tally with a receipt-derived one; S455 is a
  fresh open of a body the lane already holds (digest-identical); the standing instrument-receipt gate
  went from red to green without moving any instrument byte; and the cache-fill erratum narrows the
  claim to what the record can support. The counters' mutation survivors and the C2 fabrication limit
  are stated, not hidden.
- **discernment — unchanged (author-side).** The round's Gate carries one admit and two rejects with
  located evidence for a non-author spot-check, but no non-author judgment has landed in-round and no
  attack seat delivered, so the lane's own gate cannot be scored against one. The mutation probe's
  survivors are routed, not repaired, because the counters are frozen and measured.

## SHONEN

- [~] **SKILL.md contains real decision tables, error patterns, checklists, cited sources.**
  `corpus/knowledge/shonen-ledger.json` row `box 1` (`status=evidenced`) — SKILL.md gained the
  §Round 82 registry with three instruments, their verdict maps, selftests and pinned proofs; the
  round's entry and lesson add located quotes and decision rows. No named non-author verifier for
  this round's bytes.
- [ ] **At least one end-to-end domain task executed and logged in LOG.md.** Box 2 stays `gap`:
  `shonen-ledger.json` row `box 2` records one named LOG receipt that does not exist at the
  revision (`…/round-47/verification/offline-sweep-r46-verdict-time.txt`); unchanged this round.
- [~] **Instructions executable by an agent without oral context.** `shonen-ledger.json` row `box 3`
  (`status=evidenced`) — each new registry row carries an entry command, a verdict map and a
  copy-pasteable selftest; the wave's own seats executed the contract from its files. Author-side.
- [~] **No cross-domain bleed; PROVINCE.md still accurate.** `shonen-ledger.json` row `box 4`
  (`status=evidenced`) — the new entry cites no sibling lane repository path, and the connector's
  sibling scan found no competing capture-to-capture gate outside kake; two unrecorded adjacencies
  (mori's `Vary`/cache-selection rule, kumitate's receipt-age rule) are reported and cited, not
  absorbed. Author-side.

## Wave accounting

- Shape: one v1 wave (`kake-r82-w1`), policy `ufo-wave-policy.json`, band 8–16, `maxLanes 13`,
  validated at `62061ff9`.
- Requested: 13 — scout 2 (`ScoutRecon`, `ScoutSources`), executor 3 (`ExecCapture`,
  `ExecRegistry`, `ExecDelta`), scribe 3 (`ScribeLesson82`, `ScribeKnowledge`, `ScribeRecord`),
  reviewer 2 (`ReviewC1`, `ReviewC2`), critic 1 (`CriticClaims`), mutation-tester 1 (`MutC`),
  connector 1 (`ConnectorC`). Requested attack share 4/13 = 30.77 %.
- Settled (non-empty output, the frozen rule): **7/13** — `ScoutRecon` (4,871 B), `ScoutSources`
  (7,888 B), `ExecCapture` (92 B, a one-line progress note, not a deliverable), `ScribeLesson82`
  (6,392 B), `ScribeKnowledge` (6,664 B), `ScribeRecord` (3,811 B), `ConnectorC` (13,375 B).
- Substantive deliverable (>= 200 B): **6/13**. Empty output: `ExecRegistry`, `ExecDelta`,
  `ReviewC1`, `ReviewC2`, `CriticClaims`, `MutC` — 6 dead seats.
- **Settled attack share: 0/7 = 0.0 %** (substantive 0/6 = 0.0 %) against the run-15 ≥ 25 % floor.
  A conformance defect, recorded below and in `w1-accounting.json`
  (`requested_share=0.3077`, `settled_share=0.0`, `substantive_share=0.0`).
- Round total: 13 seats. Residual call: none. Round total including the L1's own work: 13 seats.
- Planner mapping: the L1 held the canonical planner seat; the planning data-walk rode `ScoutRecon`
  (`w1/ScoutRecon.md` §4).
- Seat reports present: `w1/{ScoutRecon,ScoutSources,ScribeLesson82,ScribeKnowledge,ScribeRecord,ConnectorC}.md`;
  the four seat receipts dirs hold the connector's and the scouts' evidence.

## Conformance defects

- **Attack floor unmet.** All four attack seats (`ReviewC1`, `ReviewC2`, `CriticClaims`, `MutC`)
  returned empty; the round's falsification is the L1's author-side controls and mutation probe plus
  the non-author closure. The requested shape met the floor; the settled shape did not. This is
  reported as a defect, not repaired by relabelling seats.
- **Six dead seats, no replacements** (per protocol a dead seat stays dead in the evidence).
- **The L1 performed critical-path work itself** where a seat had not delivered: capture B, the
  manifest, the delta record, the tampered control, both after-receipt pairs, the `S433` cells, the
  ledger receipt. The seat writes that did land (`ScoutRecon`, `ScoutSources`, `ScribeLesson82`,
  `ScribeKnowledge`, `ScribeRecord`, `ConnectorC`) are cited where used.
- **C2 selftest pair is two subjects, not a contradiction.** The predicate's `selftest_ok` is the
  tool's live selftest (`14/14`); `controls/c82-selftest-c2.txt` is the counter's own nine-fixture
  selftest (`9/9`). The contract's control bullet names the second; the report records which is
  which rather than editing a frozen sentence.

## Routed (not fixed)

- Round-83 killer fixtures for the counters' mutation survivors (two for C1, three for C2, one
  equivalent mutant) — changing a fixture after the claims' after-state would break the
  receipt-to-bytes correspondence.
- C1's row conjuncts are textual by necessity (a records-only tree with arithmetically correct
  numbers reaches `open=0`); the non-author closure is what catches a transcription.
- C2 decides the chain, not the property; a well-formed fabrication with real digests passes, so
  provenance stays the capture transcript. The cache-fill erratum further narrows it: `body=same`
  compares stored objects, not origin reads.
- D3 reads the fleet repo's history because the filed round-81 report is outside this round's write
  scope; the round-80 fleet report's erratum is carried here, not in that file.
- `capture_delta.py` does not compare `userAgent` — nor `x-github-request-id` — across trees; the
  `[r82-note]`/`[r82-erratum]` record both, round 83 adds the check.
- Pre-existing debt, unchanged: the round-69 offline freshness sweep red (L0 `kake | round-69`), the
  round-72 dangling staged ids (L0 `kake | round-72`), and the round-71 attack-share set ambiguity
  (L0 `kake | round-71`).

## Stale-lane

Respawn-per-round driver; no other mission of this lane is open. Mission age at filing: under two
driver ticks, progressing (10 lane commits this round).

## Tooling

No tool installed or upgraded. pacman untouched; no publish, deploy, DNS or account action. Reads:
three GET-only requests to the declared `ds4cc.com` surfaces plus the sources seat's RFC GETs. Open L0
lines unchanged (`kake | round-24/25/35/45/58/59/65/67/69/71/72`).
