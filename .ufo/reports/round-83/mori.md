# mori round 83 — report

lane: mori-shokunin · round 83 (attempt 1) · date 2026-11-04 · L1 `MoriR83`
entering revision: `68185d6e719054c55b107280085b05609e96165b` (branch `master`, pushed, clean)
freeze commit: `9075c72995095de97babb3d06e3f2d3b2f168062` · pre-data amendment A1: `d2987c67`
measured revision: `c4845c83244317bd85d047583c53d93263d84f31` (primary), re-run at `9cf7fda9`,
`405dc48c` · final lane tip: `8819c94c62f5d99ad9592ed965d37db4eab62d02` (pushed;
`ls-remote` prints it)

## Work performed

Declared claims (frozen in `.ufo/waves/round-83/contract.md` before any seat ran; one pre-data
amendment, disclosed below):

- **C1 — operability (7):** the r82 mutation probe's surviving counter mutants each get the
  failing arm it named, so the frozen 23-mutant population reads
  `C1=met mutants=23 killed=22 equivalent=1 survivors=0 total=23 pristine=green`.
- **C2 — calibration (5, tied lowest):** the round-82 drift classification is bound to its
  committed raw snapshot (exactly-one `# Snapshot:` / `# Snapshot-sha256:` / `# As-of:` lines,
  frozen path) and re-derived from snapshot bytes plus one live census reading.
- **C3 — depth (5, tied lowest):** the record sweep's revision arm scopes its byte occurrence test
  to the line carrying the binding's row anchor, with an `elsewhere` defeated fixture.

Work items and evidence:

- **Contract, three counters, do-nothing controls (L1).** `.ufo/waves/round-83/contract.md`,
  `count-c1.py`, `count-c2.py`, `count-c3.py`, `evidence/controls-r83.txt` — `9075c729`.
  Controls: at `68185d6e` the counter is absent (`C1=unmet harness=absent`), C2
  `snapshot=absent`, C3 `arm=absent`; at the freeze commit the population control reads
  `killed=3 equivalent=1 survivors=19` (the pre-amendment `survivors=20` reading is kept in the
  receipt, not deleted).
- **Amendment A1 (L1, pre-data).** `duplicates_accepted` is an equivalent mutant: `residual +=
  duplicates` subsumes the `duplicates == 0` clause, so no arm can observe a difference. The
  counter reports it `equivalent` only while that coupling occurs exactly once; target
  `killed=22 equivalent=1`. The seat arm map found the same mutant independently
  (`w1/Mo83Sc02Arms.md`), and the C1 reviewer re-proved the adjudication
  (`w1/Mo83R01C1.md` §2).
- **C1 arms, count-c1.py (seat `Mo83E01C1C1`).** Six arms (`pristine_fail_token_with_rc0`,
  `rc_only_kill`, `red_pristine_with_real_mutant`, `empty_population_unmet`,
  `unanchored_blocks_met`, `red_detector_never_passes`) plus a strengthened
  `duplicate_anchor_excluded`; selftest `pass=10 fail=0`; each survivor killed by its own mutated
  copy (`w1/Mo83E01C1C1.md`).
- **C1 arms, count-c2.py and count-c3.py (L1, dead seats).** `Mo83E02C1C2` and `Mo83E03C1C3`
  produced no output and no live process; the L1 implemented their assignments from scratch
  prototypes validated against every freeze mutant before application — 7 arms for count-c2 and
  7 for count-c3 (a lifted `met_verdict` gate, main-path fixtures, and the `elsewhere`-class
  stub arm). Both counters now read `pass=16 fail=0`.
- **C2 snapshot binding (seat `Mo83E04Snap`).** Header lines in
  `corpus/evidence/drift-classification-r82.txt` (`# Snapshot:`, `# Snapshot-sha256:
  6091bc46…`, `# As-of: 2026-11-04T07:45:13Z`), the `## Retired` row `drift-pin-r10` names the
  snapshot path, freshness cell byte-unchanged; the seat graded `C2=met` on a byte-faithful
  fixture (`w1/Mo83E04Snap.md`).
- **C3 anchored occurrence (L1, dead seat).** `Mo83E05Anchor` produced no output; the L1 landed
  `contains_anchored` (marker `ANCHORED_OCCURRENCE`) in `tools/mori-record-sweep.py`, four new
  arms, and the two r82 revision fixtures that had encoded the unanchored semantics (blob
  `pointers=240` → `| tool pointers=240 |`). Verified: `RECORD_SWEEP_SELFTEST pass=40 fail=0`,
  real bindings green (`bindings=3 revisions=0`), `elsewhere` caught by the new tool and green on
  the r82 tool (rc 0, `revisions=0`).
- **Routed defects D82-1/D82-2 (seat `Mo83E06D82`).** `SCORECARD.md` gains the named correction of
  record — 249 is the value at the r82 record commit `f02ad83b`, and the `075574c8`/237 label is
  historical and separated — and `.ufo/waves/round-83/evidence/c3-selftest-r83.txt` carries the
  post-repair C3 tallies (`w1/Mo83E06D82.md`).
- **Counter repairs (from the C2/C3 reviewer, seat `Mo83R02C23`).** The C2 header parse now
  requires exactly one of each provenance line and the frozen snapshot path; duplicate-header and
  foreign-path fixtures read `unmet` (two survivor bypasses closed before data). C3's remaining
  bypasses are named limits in QUALITY 169, not defects. The reviewer also reproduced the
  `elsewhere` shape live against the r82 tool (`w1/Mo83R02C23.md`).
- **Source and frontier (seat `Mo83Sc01Source`).** S598 pinned at
  `corpus/evidence/sources-r83/pitest-home.html` (sha256 `b0c7e050…`, 12023 bytes / 284 lines,
  three fetches byte-identical, ETag `"6a1fe9b2-2ef7"` revalidates 304, located quote at raw line
  114, 14 words); the mutators page refused with its flip condition; the seat measured the page's
  own "51 words" block at raw lines 106-114 and corrected the L1's first anchor
  (`w1/Mo83Sc01Source.md`).
- **Arm map (seat `Mo83Sc02Arms`).** Per-survivor arm map, anchor-uniqueness sweep, fake-arm traps,
  and the independent equivalent-mutant finding (`w1/Mo83Sc02Arms.md`).
- **C1 attack (seat `Mo83R01C1`).** Independent re-derivation of the 23-row population, per-mutant
  arm attribution with zero fake kills, both do-nothing controls reproduced, the A1 adjudication
  re-proven, and a 24th-mutant sweep (§6) that found two non-equivalent survivors outside the
  frozen population (`M24a`, `M24b`) and two provably equivalent ones (`M24c`, `M24d`) — carried
  to round 84, not amended into this claim (`w1/Mo83R01C1.md`).
- **Connector overlap scan (seat `Mo83K01Conn`).** Surface (a) counter mutation adequacy:
  *overlap-declared* (tameshi owns the generic craft; mori's frozen instance is distinct);
  surface (b) snapshot-bound classification: *distinct* (no sibling binds a derived classification
  to a committed snapshot by path + sha256 + as-of); surface (c) row-anchored occurrence inside
  `git show <rev>:<path>`: *contested at the boundary* — chousa, tabi and tameshi hold adjacent
  practices, the exact intersection is unheld (`w1/Mo83K01Conn.md`).
- **Mission-contract review (seat `Mo83C01Crit`, dead).** No output, never replaced; the claims
  were attacked by both reviewers, the arm map and the C1 reviewer's mutant sweep instead.
- **Lesson, frontier rows and the census (L1, dead scribe seat).** `corpus/lessons/round-83.md`
  (Mistakes, Census, Gate, measured after-block, wave and dead-seat record),
  `corpus/README.md` round-83 knowledge row, `corpus/QUALITY.md` 169, `corpus/SOURCES.md` S598 row
  plus the round-83 search-log block.

Round shape: **ONE v1 wave, 14 seats** under `ufo-wave-policy.json` (band 8–16): 6 executor,
2 scout, 2 reviewer, 1 scribe, 1 critic, 1 mutation-tester, 1 connector — attack share 4/14
(28.6 %), connectors 1, residual none, planner seat held by the L1. All seats routed through the
host table; no `model` was passed. `w1.ready` taken by the dispatcher at 08:20:40Z; settlement
`w1-results.json` committed. **Six seats produced no report** (`Mo83E02C1C2`, `Mo83E03C1C3`,
`Mo83E05Anchor`, `Mo83C01Crit`: empty output; `Mo83S01Lesson`: cut off after its census; and
`Mo83M01Mut`: cut off mid-probe — its partial message records driver defects and the mid-wave
counter edits, no tally). No seat was replaced; the L1 executed the dead seats' assignments as
described above, and the frozen counters grade the resulting bytes like any other seat's.

## Landed changes

| Change | LOG entry | Commit |
|---|---|---|
| Frozen contract, three counters, do-nothing controls | Round 83 §C1–C3 | `9075c729` |
| Pre-data amendment A1 (equivalent mutant) + re-taken control | Round 83 §C1 | `d2987c67` |
| Wave w1 spec, dispatch and handoff (14 seats) | Round 83 §L2 | `466d28bc` |
| Counter arms, anchored occurrence, snapshot binding, S598 row, knowledge entry, QUALITY 169, SCORECARD retired row and D82-1 correction | Round 83 §C1–C3, §Frontier, §D82 | `c4845c83` |
| Record: lesson, README row, SCORECARD round section and planned round 84, LOG entry, SKILL registry row 17, seat reports, wave receipts | Round 83 | `9cf7fda9` |
| Record-commit receipts and the volatile live reading | Round 83 §C2 | `405dc48c` |
| Final-tip measurement receipt | Round 83 §C1–C3 | `582604bf` |
| Wave settlement results | Round 83 §L2 | `8819c94c` |

## Before → after measurements

| Claim | Counting command | Before | After (measured at `c4845c83`; re-run at `405dc48c`) |
|---|---|---|---|
| C1 | `python3 -I .ufo/waves/round-83/count-c1.py <rev>` | `68185d6e`: `C1=unmet harness=absent` (rc 1); freeze `9075c729`: `C1=unmet mutants=23 killed=3 equivalent=1 survivors=19 total=23 pristine=green` (rc 1) | `C1=met mutants=23 killed=22 equivalent=1 survivors=0 total=23 pristine=green detector=green`, rc 0 (deterministic across runs) |
| C2 | `python3 -I .ufo/waves/round-83/count-c2.py <rev>` | `C2=unmet snapshot=absent` (rc 1) | `C2=met snapshot=bound asof=1 tokens=64 agreed=64 residual=0 live=derived live_tokens=63 live_agree=63`, rc 0; re-run at `405dc48c` reads `live_tokens=64 live_agree=64` |
| C3 | `python3 -I .ufo/waves/round-83/count-c3.py <rev>` | `C3=unmet arm=absent` (rc 1) | `C3=met arm=anchored defeated=2 fixtures=2/2 bindings=3 revisions=0 arms=40`, rc 0 |

Receipt: `.ufo/waves/round-83/evidence/after-r83.txt`. C2's live reading moved between runs: 63
tokens at `c4845c83` (the snapshot's `-FINDING:WATCHDOG_STALE` absent live) and 64 at `9cf7fda9`
and `405dc48c` (present again). It is reported as measured; `live=derived` means the run happened
and read red, and the classification is bound to the snapshot, so no class or claim moves with the
live census. The `elsewhere` defeated shape is proven twice: the r82 tool reads `RECORD_SWEEP
pending=0 pinned=0 carriers=1 bindings=1 revisions=0`, rc 0, on it, while the anchored tool reports
`REVISION_MISMATCH ... rev-bytes` (the frozen counter's `defeated=2`).

## Sources & frontier

`SOURCES.md` rows before → after: **370 → 371**
(`grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`). Rows added by
tier: **1 tier-A docs row** (S598). Rows touched old→new: **0** (no status, recheck or `used-by`
change on an existing row). Frontier rows advanced: `corpus/README.md` gains the round-83
knowledge addition row; the capability and gate-registry rows land with this round.

Census at round end: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root
/home/vgpnk/Projects/shokunin mori` → rc 0, `mori ok`, 371 rows, malformed 0, 35 tolerated W04
duplicate-URL warnings (the same tolerated class as entering).

The sourced claim is **C1**: its rule (a surviving mutant is a coverage finding about the suite;
the killed share gauges adequacy) rests on **S598**, opened and pinned this round
(`corpus/evidence/sources-r83/pitest-home.html`; sha256 `b0c7e050…`; 12023 bytes / 284 lines;
three independent fetches byte-identical, no redirect; ETag `"6a1fe9b2-2ef7"` revalidates 304;
located quote at raw line 114, 14 words). The lesson's `## Gate` records the admit, the
reject-class decision on the mutators page and its flip condition, and the seat's correction of
the page's own "51 words" block to raw lines 106-114.

Assimilation: **none**. `/home/vgpnk/Projects/shokuknow/merge/mori/` still collides with the lane
registry — 128 of 136 staged ids (registry S001–S598, staged S471–S606; `comm -12` = 128; evidence
`.ufo/waves/round-83/assimilation/{reg-ids,staged-ids,collisions}`), the mass-drift case the
addendum forbids repairing read-only; the r61 L0 stands and nothing was adopted. The collision
guard was re-proven on a scratch registry with an indented row (`  | S901 |` beside a staged S901
→ `collisions=1`, `assimilation/guard/`). `considerthese/`: the newest file (`2026-10-26.md`) was
re-read; suggestion 1 is standing QUALITY 167, suggestion 2 is the flagged-versus-fixed ledger,
suggestion 3 is the closure re-execution duty walked since r82, and suggestion 4 stays a proposal —
no new proposal was mined into a criterion this round (reason: the three claims already carry the
round's landing budget; the file is unchanged and re-verified present).

## Trend verdicts

- **expansion: improved** — one new admitted knowledge entry on ground the coverage map did not
  hold (counter mutation adequacy), `source: S598` opened, pinned and quoted this round; rows
  370 → 371, census rc 0; the coverage map gains the round-83 row
  (`corpus/README.md`, new section).
- **quality: improved** — three frozen instruments gained working arms (r82 counters: c1 4 → 10,
  c2 9 → 16, c3 8 → 16; the tool 36 → 40), the revision arm gained an anchored occurrence test
  with a defeated fixture, the classification gained an immutable snapshot binding, and the
  standing battery at the landed tip reads `BATTERY pass=57 setup=4 fail=0` (`BATTERY 57/61`),
  unchanged from the dispatch-tip run at the freeze bytes. Counterweights, routed: the live-reading
  volatility, C3's three named limits and the reviewer's two non-equivalent 24th-mutants.
- **discernment: improved** — two reviewers, the arm map, the connector and the L1 falsified the
  claims before data: R02 closed two C2 bypasses, Sc02 and A1 converged on the equivalent mutant,
  R01 found zero fake kills and re-proved both controls, and the round reports six dead seats and
  the L1 stand-in work rather than presenting their assignments as seat output. Named weakness:
  the critic seat and the mutation-tester produced no report, so the mission-contract attack and
  the counters' own mutation probe rest on the two reviewers and the seat's partial message.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md` gate registry row 17 (the r83 counter family with its verdict map and tallies); `corpus/QUALITY.md:1834` (QUALITY 169); `corpus/knowledge/counter-mutation-adequacy-r83.md` K1–K4.
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md` Round 83: three measured claims with receipts (`9075c729` … `582604bf`), the dead-seat record and the L1 stand-in work.
- [~] Instructions executable by an agent without oral context — `python3 -I .ufo/waves/round-83/count-c1.py --selftest` (6/6), `count-c2.py --selftest` (12/12), `count-c3.py --selftest` (9/9), `python3 -I tools/mori-record-sweep.py --selftest` (40/40); every keeper is one command from the lane root.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — the round writes lane counters, the lane's own record sweep, the lane's corpus and its SCORECARD; no sibling lane, fleet file or operator surface is written, and the knowledge entry's K4 keeps the source's claim separate from the lane's decisions.

## Round extras

- **Stale-lane:** respawn-per-round driver; this lane has no other mission open, and round 84 is
  the next intended round.
- **Open L0 questions** (routed around; none blocks this round): mori round-61 (staged
  `merge/mori` id collisions), round-62 (Windows-host L2 waiver; not in force here), round-65
  (loopback transport / instrument change), round-73 (word-count-label sweep instrument). No new
  L0 line was filed.
- **Tool installs:** none; no pacman transaction was run and every seat recorded "none needed".
- **Inherited state:** none. The lane entered clean (`tracked=0 untracked=0`); no round-82 product
  was left uncommitted.
- **Dead seats:** `Mo83E02C1C2`, `Mo83E03C1C3`, `Mo83E05Anchor`, `Mo83C01Crit` (empty output);
  `Mo83S01Lesson` and `Mo83M01Mut` (cut off; the latter's partial message records its driver
  defects and the mid-wave counter edits, no tally) — never replaced.
