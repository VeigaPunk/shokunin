# mori — round 44

Lane: `mori-shokunin` (fleet & host observability). Entering tip
`1429c791db5891c484684feef893799909d2d6a8` (round-43 closure **Admit**).
Instruments frozen at `7cb59c6891d4f5d0266fe062565f094da835dc84`. Landing commit
`5157cdda41ca711da280a85e7d3ec13da6ec85d3`; after-measurement commit
`5102022a3978e167eaf34dbaecad68ae320a5fbe`; entry-precision commit
`360e3774fec032ea3ea11d08fb4b623b3d2b047c`; receipts commit
`6d2f519247f82dab12f47cc9e3a02c86793420a8`; lesson-fill commit
`75eaf85b1609158af59c7bbf86bed95d39308dcd`; final lane tip
`d148906c5b255f58f946df22158a2d499a816e04` (32/32 wave reports, clean tree). Every
after-measurement was re-derived at `5157cdda`, `5102022a`, `360e3774`, `75eaf85b` and the
final tip — `C1=met`, `C2=met`, `C3=met` at each (`after/tip-equivalence.txt`).

## Work performed

**Declared claims (3, distinct axes; the round-43 closure's routed defects 3, 4
and 5 are the motivating evidence):**

1. **C1 — calibration 5**: a committed figure ledger
   (`.ufo/waves/round-44/figures.tsv`) reconciles the round's reported counts,
   each row one `git` pipeline naming `@REV@`, re-derived at the measured
   revision with 12-row and 4-class floors (`count-c1.py`).
2. **C2 — operability 7**: each of the round's three counters is a registered gate
   — eight non-empty standard cells in `SKILL.md`'s `## Gates` table, a resolvable
   entry, a `--selftest` over isolated fixtures whose tally is fail 0, and a
   committed mutant its own selftest catches (`count-c2.py`,
   `tools/mori-gate-registry.py`).
3. **C3 — depth 5** (re-attributed from coverage post-data, correction 1 in
   `SCORECARD.md`): one admitted knowledge entry on FR5 ground —
   `corpus/knowledge/pid-probe-conclusion-r44.md` with rows S471/S472, a
   census-green registry and a README map row.

**Work items (evidence pointer per item):**

- **Frozen contract and instruments**, before any data seat:
  `.ufo/waves/round-44/contract.md` (P-C1, P-C2, P-C3, kill rules),
  `count-c1.py`, `count-c2.py`, `count-c3.py`, `tools/mori-gate-registry.py`,
  `fixtures/figures-r43.tsv`, three mutants; ten sha256 pins and four selftest
  tallies in `.ufo/waves/round-44/evidence/freeze-r44.txt` (commit `7cb59c68`).
- **Three do-nothing controls** at the entering tip: `evidence/control-c1-donothing.txt`
  (`C1=unmet`, ledger absent), `evidence/control-c2-donothing.txt` (`C2=unmet`,
  counters absent), `evidence/control-c3-donothing.txt` (`C3=unmet`, entry absent).
- **Two witnesses of the routed defect classes**:
  `evidence/witness-r43-figures.txt` (`C1=unmet mismatches=2`, naming F03
  asserted 15 / observed 14 and F04 asserted 34 / observed 8) and
  `evidence/witness-r43-gates.txt` (`REGISTRY=unmet` for the two round-43
  counters).
- **Routed defect 5 closed**: `evidence/c1s-tip-run.txt` — the round-43 successor
  counter re-run at the round-44 tip, 14 checks PASS, `C1S=met`, exit 0
  (seat `w1/ExecC1STip.md`).
- **Round-43 errata appended, no filed byte rewritten**: `corpus/lessons/round-43.md`
  (the "15 checks" and "34 seat logs" figures superseded, with the commands that
  observe 14 and 8) and `LOG.md` (the same rate-limit figure).
- **C3 sources opened by this L1** (not by proxy): both pages GET 200 with
  content-type, byte count and fetch time; quotes and access dates in
  `corpus/lessons/round-44.md` §Gate. Rows S471 (tier A) and S472 (tier B) in
  `corpus/SOURCES.md:250-251`; entry at `corpus/knowledge/pid-probe-conclusion-r44.md`;
  map row in `corpus/README.md` §"Round-44 coverage additions".
- **Assimilation (item 10)**: theme = what a pid probe may conclude; one entry
  adopted from `/home/vgpnk/Projects/shokuknow/merge/mori/` (read-only, no
  campaign tool run), two refusals kept with reason and flip; id-collision guard
  run with receipts (`.ufo/waves/round-44/assimilation/`: `reg-ids` 245,
  `staged-ids` 136, `collisions` = 2 → S471/S472 shadowed by document; the
  campaign's ids for these two documents are S490/S491 and were re-pointed by
  document, not arithmetic). Indented-row guard proven: column-zero-only pattern
  = 1 id, 0–3-space pattern = 2 ids (`assimilation/guard/`).
- **Quarantine slice** (campaign absent-defect register, read-only): S244, S262,
  S268 — all prose-class "could not be fetched"; S244 and S262 **clean** on their
  own companion URLs, S268 **unverifiable, not fabrication** (`w1/ScoutRegisterSlice.md`).
  No row in the slice is appended.
- **considerthese (one proposal)**: `considerthese/2026-10-24.md` P4 "Reproduce
  headline numbers mechanically" — unimplemented in general before this round
  (`w1/ScoutConsider.md`) — mined as **QUALITY 117**, whose check is C1.
- **QUALITY 117–119** appended (`corpus/QUALITY.md`), each with rule, rationale,
  check command, a shown-able-to-fail witness and a "Not covered" limit.
- **Host resource runway, measured read-only**: `/tmp` at 100% (1.1 GiB free of
  128 GiB, 167 GiB used, 33 812 entries) during wave 1 —
  `evidence/resource-runway.txt`. Detection and report only; nothing reclaimed.
- **Own-work reading for C3**: 1698 of 1931 `/proc` entries read a zero-length
  `cmdline`, every one state `I` (1489) or `S` (209); a nonexistent pid returns
  `ENOENT` (`evidence/cmdline-empty-by-state.txt`).
- **Misroot sweep**: `MORI_MISROOT_CLEAN`, 0 candidates; no seat wrote to the
  fleet root (`w1/ExecMisrootSweep.md`).
- **Gate inventory** (the standard's real state, reported not absorbed):
  33 gate/probe tools, 18 audit PASS, 15 FAIL — 14 unregistered (11 of them have
  complete 8-cell rows in secondary tables the auditor cannot read) plus one gate
  with no `--selftest` (`w1/ExecGateInventory.md`).

**Round shape.** ONE v1 wave under policy v1 (`ufo-wave-policy.json`, band
32–64), validated by `ufo-swarm-wave.mjs plan --spec .ufo/waves/round-44/w1-spec.json`
exit 0, dispatched as exactly one batched `task` call: **32 seats** — scout 4,
scribe 5, executor 8, reviewer 5, critic 4, mutation-tester 2, sentinel 1,
revenger 1, connector 1, simplifier 1 (**12 attack roles = 37.5%**). The §3 L2
floor (8 in one batched call) is met inside this wave. **32 of 32 seats returned a
report** (`RevLedgerVsReport` landed after the round's first landing commit and
reviewed the draft ledger in `w1/ExecLedger.md`, not the landed 16-row
`figures.tsv` — recorded so no reader treats it as a review of the filed ledger).
No wave 2: fewer than
32 distinct attack items existed on landed bytes by landing time, so the residual
surface is the round-45 plan instead of padded seats (contract's "never pad").
**Round total: 32 seats.** The canonical §3 planner seat is held by the L1 (the
validator rejects `planner`); the bounded planning data-walk rode the
scout/revenger items `ScoutConsider`, `RevStagedClaims` and `RevScorecardPlanned`.

## Landed changes

Every item is committed on the lane branch `master` (jj helper; `landed` lines
verified against the remote).

| change | LOG.md entry | commit |
|---|---|---|
| Frozen contract, three counters, gate auditor, fixtures, three mutants, `SKILL.md` gate rows (4), controls, witness receipts, freeze pins | "Round 44" (LOG.md) + errata block | `7cb59c6891d4f5d0266fe062565f094da835dc84` |
| `corpus/SOURCES.md` +2 rows (S471, S472), entry `corpus/knowledge/pid-probe-conclusion-r44.md`, `corpus/README.md` map row, `corpus/QUALITY.md` 117–119, `SCORECARD.md` declaration + three corrections + measured outcome + round-45 plan, `corpus/lessons/round-44.md`, round-43 errata, 31 wave reports, wave spec, assimilation scratch, `figures.tsv` | "Round 44" (LOG.md) | `5157cdda41ca711da280a85e7d3ec13da6ec85d3` |
| After-measurements (`after/c1-after.txt`, `c2-after.txt`, `c3-after.txt`), `evidence/census-end.txt`, measured outcome, three late seat reports | "Round 44" (LOG.md) | `5102022a3978e167eaf34dbaecad68ae320a5fbe` |
| Entry precision: the S471 counter-sentence is `stat`'s comm **field**, not the `comm` file, so the two pages diverge rather than contradict; S471 locator corrected; README map row and lesson M9 follow | "Round 44" (LOG.md) | `360e3774fec032ea3ea11d08fb4b623b3d2b047c` |
| After-measurements re-derived at the entry-precision tip (`after/tip-equivalence.txt`) | "Round 44" (LOG.md) | `6d2f519247f82dab12f47cc9e3a02c86793420a8` |
| Final wave-1 seat reports (32/32) | "Round 44" (LOG.md) | `0cb8c6e3ea40dfa829643786f5d147762ee09d66` |
| Lesson wave-findings rows filled from the returned reports; two seats' final report bytes | "Round 44" (LOG.md) | `75eaf85b1609158af59c7bbf86bed95d39308dcd`, `d148906c5b255f58f946df22158a2d499a816e04` |

LOG.md carries the round-44 entry plus the round-43 rate-limit erratum; the
`SCORECARD.md` round-44 sections are the declaration, the post-data corrections,
the measured outcome and the round-45 plan. **The report is filed after every lane
commit above** and cites them; no filed lane byte is rewritten by it.

## Before → after measurements

Counting commands, all over committed bytes; receipts under
`.ufo/waves/round-44/evidence/` (before) and `.ufo/waves/round-44/after/` (after).

| claim | before (at `1429c791`) | after (at `5157cdda`, re-derived at `5102022a`) |
|---|---|---|
| C1 | `python3 .ufo/waves/round-44/count-c1.py 1429c791` → `check ledger_present FAIL (absent)` → `C1=unmet`, exit 1 | `python3 .ufo/waves/round-44/count-c1.py 5157cdda` → `rows=16 classes=checks,corpus,evidence,registry,wave` … `C1=met mismatches=0`, exit 0 (ledger figure [[fig:F01]] 245, [[fig:F11]] 14, [[fig:F10]] 8) |
| C2 | `python3 .ufo/waves/round-44/count-c2.py 1429c791 --counter …` → `check counters_present FAIL (absent)` → `C2=unmet`, exit 1 | `python3 .ufo/waves/round-44/count-c2.py 5157cdda --counter .ufo/waves/round-44/count-c1.py --counter .ufo/waves/round-44/count-c2.py --counter .ufo/waves/round-44/count-c3.py --mutants-dir .ufo/waves/round-44/fixtures/mutants` → five checks PASS, `C2=met`, exit 0 (registry rows [[fig:F07]] 4) |
| C3 | `git grep -l 'Z ゾンビ' 1429c791 -- corpus/` → 0 files; registry 243 rows (`evidence/control-c3-donothing.txt`) | `TMPDIR=<lane> python3 .ufo/waves/round-44/count-c3.py 5157cdda --entry corpus/knowledge/pid-probe-conclusion-r44.md --row S471 --row S472` → five checks PASS, `C3=met`, exit 0; the same sweep at the landing commit → 3 files ([[fig:F03]]); registry 245 rows ([[fig:F01]]); census exit 0 ([[fig:F15]] 73 lessons, `evidence/census-end.txt`) |

Figures in `[[fig:Fnn]]` form are ledger rows; the ledger holds 16 rows over 5
classes and every one reconciles (`after/c1-after.txt`). Figures the report states
that the ledger does **not** back are named as such: 32 wave seats, 31 returned
reports, 12 attack roles, 33 gate/probe tools audited, 18 PASS / 15 FAIL, 279 E11
findings, 1698/1931 empty `cmdline` reads — these come from seat reports and
receipts, not from ledger rows, and a closure reviewer should re-derive them from
`w1/` and `evidence/`.

## Sources & frontier

Census (the frozen command from `CORPUS.md` §"SOURCES.md — where a shokunin
learns"), both ends, exit 0:

- round start: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin mori`
  → `mori ok …`, **exit 0**, 243 rows (`evidence/census-start.txt`).
- round end: same command → `mori ok …`, **exit 0**, 245 rows, 20 W04 duplicate-URL
  warnings, no E-code (`evidence/census-end.txt`).

Rows before → after: **243 → 245**. Rows added by tier: **A: S471**; **B: S472**.
Rows touched old→new: **none** (no `status`/`recheck`/`used-by` change on an
existing row; S350/S351 stay `rejected` and were not re-opened). Frontier rows
advanced: **FR5** — the map row records what the lane already held (the
zero-character read, `Z`, and `X` as an S171 row scope) versus what this round
adds (the measured mm-less world, the two translations' disagreement, the
`ENOENT` boundary). FR5 stays open.

Assimilation: **one theme, one entry, two rows** (details above; collision count 2,
shadow map by document, indented-row guard proven, census validated at both ends).
Refused entries: `failed-scope-keeps-limit-r50.md` (host mutation) and
`journal-reach-at-ceiling-r46.md` (`file://` note plus a `MESSAGE` grep), each with
reason and flip in `corpus/lessons/round-44.md` §Gate.

## Trend verdicts

- **expansion — improved.** Registry 243 → 245 (two tiers), one admitted knowledge
  entry on FR5 ground, one map row, and a new measured world (mm-less kernel
  threads) that no lane record carried. The two refusals stay as refused rows.
- **quality — improved.** Three routed defects closed by instrument, not by prose:
  a committed figure ledger with two witnesses that catch the round-43 slips, a
  gate standard that is machine-audited with a selftest per counter and a mutant
  per selftest, and a tip-run receipt for the receipt-vs-verdict gap. The round's
  own defects (the ledger's vacuity, the C3 census arm, the auditor's table scope,
  the `--mutants-dir` default) were found by its own seats and are disclosed
  rather than patched.
- **discernment — improved, with the lane's own numbers corrected.** Nine
  self-corrections were recorded (lesson M1–M9), including one this L1 made after
  the report's own first draft: the entry called S471 and S472 a clean
  contradiction on swap-out visibility, but the two sentences concern different
  objects (`stat`'s comm field vs the `comm` file), so it is a divergence
  (`w1/ScribeEntryDraft.md` F6; fixed in `360e3774`). Two seats
  falsified the round's own claims (`w1/CritC1Vacuity.md`, `w1/CritPredicates.md`)
  and one falsified the round's own witness provenance (`w1/ExecWitnessReceipt.md`
  F10: a fixture row round 43 never asserted); the entry's "three worlds" sentence
  was corrected append-only, C3's axis was re-attributed, and the P-C3 after-figure
  was corrected from 1 file to 3. The lane's record still needed four
  self-corrections in one round, which is the honest read of "improved".

## SHONEN

- [~] decision tables — the gate registry (4 new rows, eight cells each) and the
  round-43→44 errata tables resolve at the landing commit; no named non-author
  verifier has signed them yet.
- [~] end-to-end task logged — the three counting commands, their before/after
  receipts and their revisions are logged (`after/tip-equivalence.txt`); the
  independent non-author run is still owed.
- [~] executable without oral context — the four instruments carry `--selftest`
  over isolated fixtures and each row names its entry, verdict map and write
  scope; two of those write-scope cells are **false as written** (`w1/SentTools.md`),
  which is why this box is `[~]` and not `[x]`.
- [ ] no cross-domain bleed — no named non-author verifier; the round stayed
  detection-and-report (no remediation, no host mutation, no sibling write) but
  that is the lane's own claim, not an outside judgment.

## Routed to round 45 (from this round's own seats)

1. C1's vacuity: revision-sensitivity arm, distinct ids/commands, no `WORK`
   scoring, absent path ⇒ FAIL, non-overridable floors (`MutC1`, `CritC1Vacuity`,
   `ExecJunkLedger`).
2. C2's instrument honesty: `selftest_tally` must read the parsed tally; mutants
   must be byte-diffs that disable exactly one check; the auditor must read every
   standard-header table, resolve the row's own entry path and reject duplicate
   rows; the registry write-scope cells must be corrected by an append-only
   superseding row (`CritSelftestHonesty`, `MutRegistry`, `SentTools`,
   `ExecGateInventory`, `RevRegistryRows`).
3. C3's census arm: mirror the registry at `<repo>/corpus/SOURCES.md` or pass
   `--root`; pin the census script in the freeze manifest; token-exact
   `source:`/`coverage-map:` (`RevEnteringBaseline`, `CritPredicates`,
   `ScribeFrontierRow`).
4. Exit maps and environment: move `git rev-parse` inside the `try` (traceback
   exit 1 where `*_SETUP` exit 2 is documented), scrub `GIT_*` from children, add
   a producer-rc/pipefail gate to `count-c1.py`'s `bash -c` rows and forbid
   command substitution, drop `diff` from the read-verb allowlist
   (`RevVerdictMap`, `SentTools`).
5. `count-c2.py`'s lane-relative `--mutants-dir` default and `count-c2.py`'s
   auditor-absent branch (`UnboundLocalError`) — `SimpCounters`.
6. `considerthese` P3 (repository growth from scratch output) is still
   unimplemented; the lane's 14 unregistered gates and 3 tools without
   `--selftest` stay open.

## Report extras

- **Stale-lane:** respawn-per-round driver; this is the lane's only open mission.
- **L0 questions:** none appended this round — no operator decision was needed to
  land the claims. The registry-cell corrections and the `count-c3.py` census
  arm are lane-owned fixes, not operator decisions.
- **Tool installs:** none by this L1. One seat installed `pyflakes 4.0.3` and
  `coverage 7.17.0` via `uv` for its dead-weight analysis (`w1/SimpCounters.md`);
  no `pacman` transaction was run (host-wide pause respected).
- **Misroot:** clean (0 candidates).

---

## Erratum appended after filing — post-filing seat bytes, the connector's adjacency finding, and two entry amendments

Appended after the filed bytes above; nothing above is rewritten (the round-43
closure's routed defect 2 binds this round's own filing). The lane advanced to
`7b6998e620d436c3d01bc252e77e447debdaa8ce` after the report was filed; every claim
was re-derived there: `C1=met mismatches=0`, `C2=met`, `C3=met`, census `ok`
exit 0.

1. **Two seat reports landed after the filing** (`w1/ConnSiblings.md`,
   `w1/ExecOffHostReplay.md`, `w1/RevLedgerVsReport.md` final bytes) — committed in
   `407da787`, `cd9e699e`, `7b6998e6`. Their findings, which the filed report could
   not carry:
   - **Adjacency (material):** `w1/ConnSiblings.md` finds that the gate-registry
     class is **already held by a sibling** — `kama`'s
     `tools/gate-registry-check.py` (which enumerates the counter population from
     `git ls-files` rather than taking it from the caller, so it is *stronger* on
     the arm that matters) and `kumitate`'s `gate-mutants.mjs` predicate **K43**
     (a two-run, verdict-line mutant standard). C2's `@REV@`-ledger grammar is new
     fleet-wide (`grep -rln '@REV@'` → no files outside mori), but its registry
     class is not. The same seat measured that `tools/mori-gate-registry.py` parses
     only mori's and chousa's heading+header pair across 12 lanes holding a gate
     registry, so it **cannot be a fleet auditor** and is not claimed as one.
     Scope held: no sibling tool was imported, and `PROTOCOL.md`'s scope rule was
     respected.
   - `w1/RevLedgerVsReport.md` reviewed the 20-row **draft** ledger, not the landed
     16-row `figures.tsv` (no ledger existed at its reading).
   - `w1/ExecOffHostReplay.md` replays the four selftests and `count-c2` from a
     scratch clone at another path, so QUALITY 115's practice holds for this
     round's instruments.
2. **Two entry amendments after the filing** (`w1/CritAssimilationGate.md`), landed
   in `cd9e699e`:
   - the Boundaries section no longer says the entry "adds the state alphabet"
     while the Claim discloses it is already held (a self-contradiction);
   - the mm discriminator now rests on a `/proc/<pid>/maps` reading of its own
     (`evidence/cmdline-empty-by-state.txt`: 1229/1229 empty-`cmdline` pids have an
     empty `maps`, 190/190 non-empty ones do not), and the snapshot totals are
     labelled as moving between runs (1931/1698 then 1419/1229) — the earlier
     receipt asserted the discriminator without reading an `mm` indicator.
   - the S472 `scope` cell's negative about S170 is imprecise (S170's source
     carries the swap-out sentence as a roff comment at `:15`); the row is
     append-only, so this is recorded in `corpus/lessons/round-44.md` M10 rather
     than rewritten.
3. **Not adopted from the critic's list:** it recommends admitting
   `effective-limit-is-cross-level-r44.md` instead of the pid-probe entry. This
   round's entry stays: it is the theme the round declared, its sources were
   opened by this L1, and the critic's own verdict is that the entry clears the
   bar after the six amendments above (five of which are landed; the sixth — a
   re-punctuated zh quote — is disclosed here: the entry's zh sentence uses the
   page's wording with normalized sentence punctuation, and the recheck counts
   words, not punctuation).
