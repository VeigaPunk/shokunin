# mori — round 29 report (attempt 1, L1 MoriR29)

Lane repo `/home/vgpnk/Projects/shokunin/mori-shokunin`, branch `master`. Entering tip `7118f320` (round 28 admitted).
Landed tip `b581173afd85d82283291492de12666d505eb58b` (pushed; `jj-lane.sh state`: `local=remote=b581173a… ahead=0
behind=0`). Contract `.ufo/waves/round-29/contract.md` (`8a45cefe`) with amendments A1 `3a147138`, A2 `66125164`, A3
`69349c2a`, A4 `c3216969`, each committed before the data it governs.

## Work performed

Declared claims (2):

- **C1 — calibration (5, tied lowest active axis):** the six rows of the `SCORECARD.md` `## Axes` table agree with
  the admitted closure record (fleet `MANIFEST.json` per-axis `verdicts` at pinned `63729047`), counted by
  `.ufo/waves/round-29/count-c1.sh`. **Met.**
- **C2 — operability (7), sourced (S153–S155):** the A2-07 in-scope dry-run and A2-10 stamp-less shapes routed by the
  round-28 spot-check are pinned by frozen writer-independent cases, counted by `.ufo/waves/round-29/count-c2.sh`.
  **Miss** (reported, not withdrawn).

Work items:

- Contract and four amendments from wave-1 critics before data: A1 (MANIFEST as closure authority, kinds 1–5, score
  basis must be a closure-stated `X → Y`) from CriticC1Design/CriticScorePolicy; A2–A4 (kind 2b, counted shape lines
  with decisive pins, provenance link to writer reports, fixed writer set, blindness gate as a miss condition) from
  CriticRoutingCoverage/CriticC2Design (`.ufo/waves/round-29/contract.md` tail).
- C1 counter (wave-1 BuildCountC1 plus L1 kind 2b and strict X→Y direction) committed `e1c6bbe7` before any table
  edit; Axes rows rewritten `420d05ad` (all six scores held: no admitted closure states a new number), corrected from
  wave-2 CriticC1Admission in `07b9a4b9`.
- C2: eight case writers (CaseA207a–d, CaseA210a–d) wrote 24 cases without reading the tool source or tool output;
  counter committed `221cbd8f`; case file frozen `d6d5cb0a` (sha256 `1c76ea1f…d252`), freeze hash logged `255b7051`
  before the first tool run (`evidence/c2-freeze-selftest.txt`: `FAIL 11/24`).
- Thirteen non-author wave-2 judges ruled the 13 mismatching cases (`.ufo/waves/round-29/w2/Judge01.md`…`Judge13.md`):
  12 `tool error`, Judge02 `mixed: tool error, unclear text`. Tool change for the judged tool errors landed
  `cdfcf66d` (`evidence/fix-landed.diff`): `PASS 32/32`, `32/32`, `30/30` kept on the older files; round-29 file
  `FAIL 21/24` (all 24 verdicts and exits match; three non-active cases fail on fields) (`evidence/c2-fix-selftest.txt`).
  Residual review of the landed change: `.ufo/waves/round-29/residual/{ReviewLandedFix,DiffLandedFix,CriticC2Verdict}.md`.
- Sources: rows S153 (systemd v262 `sd_journal_get_realtime_usec.xml`), S154 (systemd v262 entry-object monotonic
  stamp), S155 (earlyoom commit `ca2251fc` dry-run option), each re-opened by a wave-2 scout (`w2/ReopenS153–S155.md`,
  all hashes reproduced); Gate with eight reject rows (`corpus/lessons/round-29.md` `## Gate`).
- Round-28 routed defects (spot-check §6): late wave-2 outputs re-verified and committed as evidence (`e1c6bbe7`);
  QUALITY 85–87 (blind freeze, Gate rejects, tip-receipt header) appended (`8809a3fe`); census miscount corrected in
  `corpus/lessons/round-28.md` (`3a147138`); carried debt inventoried (`w1/ScoutCarriedDebt.md`).
- Inherited untracked paths (six): `.scratch/` left untouched (pre-round, not round work, ruled at r24);
  `round-28/wave1-run.err` (0 bytes) committed as evidence `3a147138`; `round-28/w1/FixR1Runway.md` disposed out of
  the lane to `/fast/scratch/hyaku/mori-r29/L1/disposed/` (withheld for privacy in r28; sha256 `da1e1bf4…b691`);
  `round-28/w2/MutCountC1Amended.md`, `MutHeadingCheck.md`, `MutTipReceiptCheck.md` committed as evidence `e1c6bbe7`
  after wave-1 re-verification (`w1/ReviewLate*.md`; findings reproduced, no verdict impact).
- Misroot sweep (`git -C /home/vgpnk/Projects/shokunin status --porcelain`): CaseA207c's report swept into the lane
  (`cmp` ok, sha256 `0fe85d0b…a0a`); a Judge06 draft at the misspelled fleet path `mori-shokuhin/…` copied byte-exact
  to `.ufo/waves/round-29/misroot/Judge06-draft-from-fleet-mori-shokuhin.md` (`cmp` ok, sha256 `16432f46…4186`) and
  deleted from the fleet; an empty `tools/fixtures/mori-oom-killers/` skeleton removed (`rmdir`). Final sweep shows only
  the five pre-round baseline files. `.ufo/waves/round-33/w2/ScoutPinsFlagAccuracy.md` (kake) was seen at the fleet
  root mid-round and is not mori's; untouched. Lesson M3, M10.
- Planner seat: held by the L1 (validator rejects `planner`); planning data-walks rode the Axis* scribes,
  ScoutCarriedDebt and ConnSiblingOverlap.

## Landed changes

| Commit | Change | LOG.md entry |
|---|---|---|
| `8a45cefe` | contract, round-start census | Round 29 declaration |
| `3a147138` | A1; round-28 census correction; `wave1-run.err` | Round 29 declaration |
| `66125164`, `69349c2a`, `c3216969` | A2, A3, A4 | Round 29 declaration |
| `e1c6bbe7` | C1 counter + before; blind check; tip-receipt maker; wave-1 reports; round-28 late outputs | Round 29 declaration |
| `420d05ad` | C1 fix: Axes rows | Round 29 declaration |
| `221cbd8f` | C2 counter + before; C1 after; wave-1 reports | Round 29 declaration |
| `d6d5cb0a` | C2 freeze: `cases-a2-r29.json`; pre-freeze blind-check receipt | Round 29 declaration |
| `255b7051` | LOG declaration with freeze hash | Round 29 declaration |
| `8809a3fe` | S153–S155, lesson draft, QUALITY 85–87, first tool run | Round 29 declaration |
| `cdfcf66d` | tool change for judged tool errors; Gate ids; SCORECARD declaration; wave-2 spec/reports | Round 29 outcome |
| `07b9a4b9` | C1 row corrections from wave 2 | Round 29 outcome |
| `67779aa8` | measured outcome, lesson corrections, LOG outcome, wave-2/residual reports, misroot, round-end census | Round 29 outcome |
| `b581173a` | tip receipts only, measured at parent `67779aa8` | Round 29 outcome |

## Before → after measurements

- **C1:** `bash .ufo/waves/round-29/count-c1.sh <rev> 63729047644f839fe4c8cc97abd0d8bf741a5787`. Before at `7118f320`:
  `mismatches=11`, `C1=unmet`, exit 1 (`evidence/c1-before.txt`). After at `67779aa8` (parent of the landed tip; the
  tip adds only receipts): `mismatches=0`, `C1=met`, exit 0 (`evidence/tip-c1.txt`). Calibration score held at 5.
- **C2:** `bash .ufo/waves/round-29/count-c2.sh <rev>`. Before at `7118f320`: file absent, `C2=unmet`, exit 1
  (`evidence/c2-before.txt`). After at `67779aa8`: `provenance=24/24 unselected=0`, `shape_a207=3/2`,
  `shape_a210=6/2`, `blind_violations=20`, `a2_r29_selftest=FAIL(exit=1)`, `C2=unmet`, exit 1 (`evidence/tip-c2.txt`).
  Substantive: tool `FAIL 11/24` at the freeze → `FAIL 21/24` after the judged change. **Miss**, for three independent
  reasons: Judge02's `unclear text`; the L1 declined the Judge11–13 tool errors (a choice the contract allows; dissent
  and residual CriticC2Verdict's counter-view in the lesson); A4's gate prints 20 at the freeze (all adjudicated false
  positives, `w2/AdjudicateBlindHits.md`; A4 requires 0).
- **No-harm:** retention metric 4 at `67779aa8` (`evidence/tip-retention.txt`), base 4 (`w1/RetentionBase.md`). Older
  self-tests keep `PASS 32/32`, `32/32`, `30/30`; pressure `PASS 12/12`, census selftest 134/134 (`w2/RetentionAtTip.md`).
  **Disputed harm (operability):** after `cdfcf66d`, an active unit with `ActiveEnterTimestampMonotonic` missing or 0,
  a real send, then a plain restart reads `KILLERS_UNKNOWN` instead of `KILLER_ACTED` (send kept in
  `earlier_invocation_send_lines`); residual CriticC2Verdict F4 calls it a harm, ReviewLandedFix F2 calls it what
  A2-05/A2-06/A2-07 decide (Judge03's frozen case pins the same outcome). Left for the closure to rule.
- QUALITY 84 check `.ufo/waves/round-28/check-tip-receipts.sh b581173a 29` prints `tip_receipts=unmet`: `tip-c1.txt`
  and `tip-c2.txt` are named in `SCORECARD.md` but not in `LOG.md` or the lesson, which the check reads (defect, not
  fixable without breaking the receipts-only last batch). QUALITY 87's header and receipts-only assertions hold for
  `b581173a` (three `ok` lines).

## Sources & frontier

- Census command `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin mori`:
  start (19:50:48Z) ten W04, `mori ok`, exit 0 (`evidence/census-start.txt`); end ten W04 (none new), `mori ok`,
  exit 0 (`evidence/census-end.txt`).
- Rows 152 → 155: +3, all tier A, status `mined` (S153 docs, S154 code, S155 code). No older row's `status`,
  `recheck` or `used-by` changed. Gate: 3 admit rows, 8 reject rows (duplicate URLs, 404s, a file that does not carry
  the fact).
- Sourced claim: C2 (case file top-level `sources: ["S153","S154","S155"]`; lesson "What the round learned").
- Mined mistakes: `corpus/lessons/round-29.md` `## Mistakes` M1–M4 plus wave-2 corrections M1–M10; M1's fix (C1
  counter) shown able to fail at `7118f320` and `e1c6bbe7`.
- Frontier rows advanced: none.

## Trend verdicts

- **expansion: improved** — three mined rows re-opened by non-authors with hashes reproduced (`w2/ReopenS153–S155.md`);
  two sourced facts in the lesson (dry-run is a send-site no-op; a monotonic stamp is meaningful only within its boot).
- **quality: unprovable-but-better** — C1 brings the self-assessment table into agreement with the closure record
  (11 → 0), and the judged tool change fixes 10 frozen cases outright without moving any older verdict; but C2 is a
  miss and the landed change carries one disputed harm shape. Not claimed as `improved`; the closure rules.
- **discernment: improved** — wave-1 critics overturned both counters before data (A1–A4); 13 independent judges
  ruled every mismatch, and their split (Judge02/Judge04) is reported, not resolved by the author; the L1 withdrew its
  own post-data escape clause and reports C2 as a miss (lesson M5).

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md:11-21` (decision
  table), `:23-45` (error patterns), `:149-154` (checklist); no non-author verified the core tables (`w1/ScoutShonen.md`).
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md:1838-1846` (round-26 live
  oom-killers run, receipt `.ufo/waves/round-26/evidence/c2-live-run.txt`).
- [~] Instructions executable by an agent without oral context — wave-1 ScoutShonen (non-author) ran
  `bash tools/mori-census.sh --selftest` → `PASS (134 cases)` from the documented entry; one unqualified citation
  (`SKILL.md:661`) found.
- [ ] No cross-domain bleed (PROVINCE.md still accurate) — no bleed found, but PROVINCE is stale in five places
  (`w1/ScoutShonen.md`: `PROVINCE.md:32`, `:236/:294/:359/:375`, `:68`, `:66`, `:44-57`); untouched this round.

## Round shape and seats

- Shape: default, two v1 waves plus one residual call. Wave 1 (`mori-r29-w1`): 35 seats — 13 executor, 10 scribe,
  4 reviewer, 4 critic, 3 scout, 1 connector. Wave 2 (`mori-r29-w2`): 36 seats — 21 reviewer, 6 scout, 4
  mutation-tester, 3 critic, 2 executor. Residual: 3 seats (2 reviewer, 1 critic) on the landed tool change. **Round
  total 74 seats; 0 dead; 0 refusals.** Each wave validated under policy v1 (`wave1-run.json`, `wave2-run.json`) and
  dispatched as one `task` call; the harness requires a `solutionSpace` field per task, so one generic line per role
  was added to the validator's `taskCall` (recorded in `wave1-dispatch.json`, `wave2-dispatch.json`).
- Seat gate: `wave-slot.sh acquire mori mori-r29-w1 35` and `mori-r29-w2 36` granted without wait; both released.
- Other: L0 questions none. Tool installs none (L1 and every seat reported none). Stale-lane: respawn-per-round
  driver; no other mission of this lane is open.
