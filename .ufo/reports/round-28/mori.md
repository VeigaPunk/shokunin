# mori — round 28 report (attempt 1, L1 MoriR28, hyaku in-session)

## Work performed

Declared claims (`mori-shokunin/.ufo/waves/round-28/contract.md`, declared at `079a47c6`, amendments A1 at
`763d3469` and A2 at `1c4c186e`, both before any data):
**C1 — freshness** (score 5, tied lowest): restore S096, S097, S101 to their first-published cells and supersede the
eight carried row defects (S096, S097, S101, S127, S128, S129, S131, S140) with rows re-opened this round, readers
repointed (sourced: S145–S152). **C2 — operability** (score 7): pin the ten round-26 amendment-A2 rules of
`tools/mori-oom-killers.py` with frozen cases written blind to the tool (r26 D7, re-declared; round 27 withdrew it).

- Declaration, C1 counter and before receipts: `079a47c6`; W1 correction appended to the round-27 contract (routed
  defect 1), re-bounded to committer time after wave-1 CriticRoutingCoverage (`763d3469`).
- Amendment A1 (CriticC1Design showed the declared C1 counter could print `C1=met` on copied defective rows in a
  sandbox): counter hardened — teaches must differ, `used-by` must cite the new id, a Gate line with sha256 per row,
  `readers_left=0`; `rejected` accepted only for a row superseding a rejected row; A2-07 field map corrected
  (CriticC2Design F1). Re-measured before: `readers_left=27`, `C1=unmet` (`evidence/c1-before-a1.txt`) — `763d3469`.
- Amendment A2 (CriticC2Design F6): mismatch rulings (tool error / case error / unclear text) by a non-author judge,
  fixed before the freeze — `1c4c186e`.
- S096, S097, S101 restored to first-published cells; live readers repointed in `SKILL.md`, `PROVINCE.md`,
  `corpus/README.md` and three knowledge entries — `1c4c186e`.
- Eight superseding rows S145–S152 drafted by eight wave-1 scribes, each source re-opened by curl with sha256 and a
  located quote (`corpus/lessons/round-28.md` `## Gate`) — `1c4c186e`, `f2de0eed`, `6b695b02`.
- C2: hardened counter `count-c2.sh` (wave-1 BuildCountC2; closes r27 CriticC2Counter F1–F8, F11) committed first
  (`7b75f45a`); 30 cases (3 per rule) from ten blind writer seats assembled unedited and frozen (`d21b8bd3`); first
  tool run after the freeze `PASS 30/30`, exit 0 (`evidence/c2-freeze-selftest.txt`, committed `f2de0eed`). Tool
  unchanged.
- QUALITY 83 (dated heading never after its commit's committer time) and 84 (tip receipts in the last batch) with
  checks that fail on round 27 (`check-heading-time.py`: W1 `FUTURE-DATED`, exit 1) — `1c4c186e`.
- Round-27 tip receipts (routed defect 2): `evidence/r27-tip-c1.txt` (`C1=met`, exit 0 at `df886be1`),
  `r27-tip-retention.txt` and `base-retention.txt` (metric 4 at `df886be1` and `6ebd518f`) — `1c4c186e`.
- Misroot sweep: the seven fleet-root files are mori round-27 seat fetches (sha256 prefixes cited by mori r27 w1
  reports; wave-1 MisrootProvenance: no other lane claims them, tsukuroi disowns them). Copied byte-exact into the
  lane root, `cmp` ok, fleet copies deleted at 18:01Z — `763d3469`; hash check 7 → 0 hits
  (`evidence/misroot-before.txt`, `misroot-after.txt`).
- Planner seat: held by the L1 (validator rejects `planner`); no planning data-walk rode another seat.

## Landed changes

| Commit (lane `master`) | What | LOG.md |
|---|---|---|
| `079a47c61691f2b891d35458057b294ca5a99e77` | declaration, C1 counter, before receipts, W1 correction | Round 28 declaration |
| `763d34696a527f26efbceafd64b8a8138fbd344b` | amendment A1, misroot sweep and hash check | A1 and misroot bullets |
| `1c4c186e703bd7f755cb01c3f1f29c26d6834f99` | amendment A2, restores, S145/S146/S151/S152, reader repoint, QUALITY 83–84, r27 tip receipts, wave-1 spec | measured-outcome bullet |
| `7b75f45a3a31da5044a29a654bbc4c9cb44dfaf9` | C2 counter and its before receipt | C2 counter bullet |
| `d21b8bd38b1bf72ec903a19ed543c615564e8278` | C2 freeze: `cases-a2.json` | C2 freeze bullet |
| `f2de0eedcd60d2e354da75265ea6122bc3896073` | first tool run on the frozen cases, S148–S150 | measured-outcome bullet |
| `6b695b02a28b5f7342b2cdaaa643c176839bf7db` | S147 (last C1 row) | measured-outcome bullet |
| `84abe93e6cde117b0bc86c46e163467596fa19a6` | measured outcome, lesson sections, after receipts, wave-2 spec | measured-outcome bullet |
| `ac696ad3037c3071584df60d84b5bf0af9818dd6` | wave-2 corrections: reader wording per S146/S150/S152, C2 blindness disclosure, freeze hash | wave-2 corrections bullets |
| `06d6a5be408f9098020109e3dbb66ca4734cf4fa` | wave-2 reports, lesson corrections (M6, M7), S147 Gate cell fix | (lesson) |
| `5ef4e8db397b57299616258cb2e1c045c46564e7` | last wave-2 report, closing LOG entry | wave-2 closed bullet |
| `1fc6bb0eaab40d9ea4fe996b64d140282b76337d` | **landed tip**: tip receipts only, measured at parent `5ef4e8db` | wave-2 closed bullet |

## Before → after measurements

| Claim | Command | Before (`6ebd518f`) | After (`6b695b02`) |
|---|---|---|---|
| C1 | `bash .ufo/waves/round-28/count-c1.sh <rev>` | `row_identity=rows=144 changed=3`, `superseding=0/8`, `readers_left=27`, `C1=unmet`, exit 1 | `row_identity=rows=152 changed=0 removed=0 bad=0`, `superseding=8/8`, `readers_left=0`, `C1=met`, exit 0 |
| C2 | `bash .ufo/waves/round-28/count-c2.sh <rev>` | `a2_schema=absent a2_cases=0`, `C2=unmet`, exit 1 | `freeze_commit=d21b8bd3`, `a2_cases=30 a2_rules_covered=10/10`, `a2_selftest=PASS 30/30`, `frozen32_selftest=PASS 32/32`, `C2=met`, exit 0 |

Receipts: `mori-shokunin/.ufo/waves/round-28/evidence/{c1-before-a1,c1-after,c2-before-r28,c2-after}.txt`; tip
receipts measured at `5ef4e8db`, the parent of the last batch `1fc6bb0e`: `evidence/tip-count-c1.txt` (`C1=met`,
exit 0), `tip-count-c2.txt` (`C2=met`, exit 0), `tip-retention.txt` (`"metric":4`, equal to the base 4 at `6ebd518f`).

## Sources & frontier

- Rows before → after: 144 → 152 (`grep -c '^| S[0-9]' corpus/SOURCES.md`); added by tier: A 8 (S145–S152, all
  `mined`, each superseding one carried row; S146 moves from the 404 page to the man-pages 6.20 tarball).
- Rows touched old → new: S096 `teaches`, S097 `anchor`+`teaches`, S101 `teaches` restored to first-published cells
  (logged in `corpus/lessons/round-28.md` "Row changes"); no `status`/`recheck`/`used-by` change on an older row.
- Census `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin mori`: start `mori ok`, exit 0, six
  W04; end `mori ok`, exit 0, nine W04 (new: S148, S149, S150 "duplicate url across scopes" — a superseding row keeps
  its old row's URL with a corrected scope).
- Frontier: no FR row advanced; C1 is freshness repair on FR10/FR12/harness sources. Sourced claim: C1 (S145–S152).
- Mistakes mined: M1–M5 in `corpus/lessons/round-28.md` `## Mistakes` (future-dated heading; misroot invisible to the
  name-based sweep; withdrawal shrinking admission; superseding rows no reader cites; no tip receipt), each fix shown
  able to fail.

## Trend verdicts

- **expansion: unchanged** — no new ground; eight rows supersede existing ones.
- **quality: improved** — eight carried row defects fixed with re-opened sources, QUALITY 81 holds at the tip
  (`changed=0`), A2 rules pinned by 30 frozen blind cases, two new criteria with failing checks.
- **discernment: improved** — wave-1 critics overturned both declared counters before data (A1, A2), and a
  non-author A2 judge per rule ruled all ten rules `holds`; wave-2 critics found and the round disclosed the C2
  blindness leak (CaseA2r03), reader wording defects (fixed in `ac696ad3`) and counter fail-opens (carried).

## SHONEN

- [ ] decision tables (not verified by a non-author this round)
- [~] end-to-end task logged — `LOG.md` round-28 measured outcome; `evidence/c2-freeze-selftest.txt`
- [ ] executable without oral context
- [~] no cross-domain bleed — wave-1 ConnSiblingOverlap (no shared rows; S151/S145/S152 scope notes)

## Round shape and seats

Shape: two v1 waves. Wave 1 (build + first falsifiers): 33 seats — executor 14, scribe 9, critic 3, reviewer 3,
scout 2, mutation-tester 1, connector 1; 0 dead at spawn; SupersedeS140 ended before writing and was resumed by
message (same identity). Wave 2 (falsify): 34 seats — reviewer 26, mutation-tester 4, critic 3, scout 1;
0 dead at spawn; four seats (MutCountC1Amended, MutHeadingCheck, MutTipReceiptCheck and wave-1 FixR5RoutedSelftest) had not returned at the last commit and their output is not evidence for this report. Round total 67 seats; no residual call. Wave-2 gate: first grant at 18:34Z released unused (artifacts
not ready), re-acquired and dispatched at 18:52Z.

## Wave-2 verdicts (attack revision `f2de0eed`; S147 landed one commit later in `6b695b02`)

- C2 judges A2-01…A2-10: **holds** ×10 (no failing case, tool unchanged; e.g. `w2/JudgeA2r07.md`, `w2/JudgeA2r10.md`).
  ReRunCountC2 **partial** (freeze hash absent from LOG until `84abe93e`/`ac696ad3`), MutCountC2 **holds** (0
  survivors of 7 vectors), ReviewToolChange **holds** (tool diff empty; pressure 12/12, runway 21/21, retention 21/21,
  routed-r24 held:4 unchanged), CriticC2Admission **partial** (blindness: CaseA2r03 read 45 lines of
  `w1/CriticC2Design.md` before writing — disclosed in `LOG.md` and the lesson M6; A2-07/A2-10 breach shapes found by
  wave-1 ReviewA2SpecVsTool are not covered by any frozen case).
- C1: Reopen S145, S148, S149, S151 **holds**; S146, S147, S150, S152 **partial** (S147 absent at `f2de0eed`, present
  from `6b695b02`; reader wording fixed in `ac696ad3`; S146 teaches self-contradiction frozen in its first-published
  cell, carried). ReRunCountC1 **breaks at `f2de0eed`** (`superseding=7/8`, S147 not yet landed); at `6b695b02` and at
  `5ef4e8db` the same command prints `C1=met`, exit 0. CriticC1Admission **partial** (rows are real re-opens; reader
  edits were id swaps — the three wording defects it named are fixed in `ac696ad3`). ReviewReaderSweep **partial**
  (24/26 lines hold; range citations and "opened this round" dating carried). MutCountC1 (wave 1, on the
  pre-A1 counter): F4, F5, F7, F8, F9 closed by A1; F1 (frozen check reads a fixed lane path), F2 (whitespace-only
  restore drift), F3, F6, F10 open.
- No-harm: RetentionAtTip **holds** (metric 4 = base 4; QUALITY 82 lint 0 hits over 58 added files), CensusAtTip
  **holds** (9 W04 = 6 base + S148–S150, exit 0), ReviewMisrootSweep **holds**, CriticLessonMistakes **partial**
  (corrections appended to the lesson: M1/M5 captured-by, M3 class, new M6 and M7). ReviewR1Patch / ReviewR5Patch:
  carrying R1 and R5 is right; defects reproduced open.

## Other

- Carried debt: r25 R1 and R5 (wave-1 drafts in scratch; no landed tool change); round-27 wave-2 findings named in the
  lesson "Seat notes"; S143/S144 readers (M4); old rows' `used-by` cells.
- Contested scope (wave-1 ConnSiblingOverlap): `oom-victim-selection-r27.md:199-201` vs tsukuroi
  `kill-event-deep-r8.md:142` — cited, not absorbed.
- Tool installs: none (all seats that reported say none).
- Lane leftovers at the tip: `.scratch/` (pre-round, 2026-10-21); `.ufo/waves/round-28/w1/FixR1Runway.md` withheld
  (quotes the live harness settings value; lesson disposition); `.ufo/waves/round-28/wave1-run.err` (validator stderr,
  not committed). Late seat outputs after `1fc6bb0e` are named in round 29's lesson.
- L0 questions: none.
- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
