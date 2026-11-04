# tsukuroi — round 74 (attempt 2, hyaku run 15)

## Work performed

**Declared claims:** C1 **depth** (lowest tied, 8), a sourced systemd unit-fragment resolution
plane; C2 **freshness** (9), two round-73 routed repairs. **Author-side honest stop:** C1's
frozen alias set is false, despite its mechanical target passing; C2 repairs verify. No
replacement claim or retroactive predicate is substituted. Outside closure remains authoritative.

- **C1 real work:** six true UF rows landed in `corpus/knowledge/systemd-unit-fragment-plane-r74.md`,
  sourced S309-S311 (systemd v262 unit-file.c, load-fragment.c, unit-file.h). Rules cover priority
  registration, alias validation, the true service/socket/target/device/timer/path set, runtime
  states, perpetual-mask immunity and system-scope builtin fallback. R1Reviewer independently
  reviewed actual draft rows: six entailed, mechanically valid (`w1/R1Reviewer/report.md` §5,
  `rows-final-receipt.txt`). L1 corrected the draft's unsupported capture timestamp and narrowed
  its live-exercise prose; the six reviewed rows were unchanged.
- **C1 miss:** declaration `e51fb49d` says service/socket/target/device/**volume**, omitting timer/path.
  Pinned `unit-file.h:25-32` contradicts it. SCORECARD errata and QUALITY 106 explicitly refuse
  literal C1 credit. Correcting the note does not amend the frozen claim (R1Reviewer F1).
- **C2:** appended `corpus/lessons/round-73.md` Correction 3 (install.c:2383, superseding 2387;
  S304 :368-370, :237-238, :238-239) and LOG's count correction (final 13/14, superseding 12/11).
  LOG uses E2Routed **Form A**, an unheaded append inside its existing last Round-73 block:
  R2Reviewer HIGH-1 proves the unchanged checker shadows an EOF-headed correction.
- **Controls and instruments:** original real-base controls, source snapshots, host readings and both
  tools froze before note data (`before/`, declaration `e51fb49d`). Instruments remain unchanged:
  counter sha256 `94d46a5edfcdc00858a1b1c37bc459322fc7e337fba19cc38a85776d0dd36482`, checker
  `2da4ff1fd8e7ed1287230e43769a1d75233b992b9f04eeb77cc981f2677efd77`; selftests 13/13 and 6/6.
- **Other truthful limits:** declared full-base suffix was fabricated/mistyped; real parent is
  `d749a625b3054b7cb3435983fb9626ab3d0ed0c4`. Original controls used resolving short d749a625.
  Invalid full OIDs yield vacuous before numbers; QUALITY 107 now demands object existence.
  E1Counter's scripted non-reader/negation/unanchored-quote/duplicate-content controls pass the
  lexical C1 predicate; R2Reviewer's numeric-superstring, denial and wrong-instrument controls
  pass C2. These are named limits, not semantic admission (`w1/E1Counter/report.md`,
  `w1/R2Reviewer/report.md`, `w1/K1Critic/report.md`). C2 embeds an answer key in selftest.
- **Domain task:** read-only host search-path/mask/template/alias diagnosis; S1Scout independently
  re-fetched 3/3 snapshots and reports HOST_DELTAS=0 across 15 checks; a real timer alias was read
  (`w1/S1Scout/report.md`, `w1/E3HostProbe/receipt-a-live.txt`). No intentional mask, bad alias,
  builtin fallback selection, unit edit, reload, service restart or package transaction occurred.
- **Docs/frontier:** updated SKILL decision table, PROVINCE and corpus README; two QUALITY rules and
  eight mistake classes in `corpus/lessons/round-74.md`. Two r73 defects are repaired, not hidden.
- **Wave:** ONE validated v1 wave, 12 seats; scout 1, executor 3, scribe 3, connector 1, reviewer 2,
  critic 1, mutation-tester 1; strict attack 4/12=33%; connector 1; L1 held planner; residual 0.
  Dispatch `810daf13`; **WAVE-DONE received before this report**, results `w1-results.json`.
  Nine nonempty finals; SC1Entry, SC3Index and M1Mutation ended with empty finals. SC1Entry left
  the reviewed note draft; SC3Index left no completed doc drafts, so L1 integrated docs. Known
  SC1Entry/SC3Index provider error: HTTP 429 RESOURCE_EXHAUSTED, "Individual quota reached",
  reset around 2026-11-04T08:23Z (SC3Index wake reported 4h35m16s). M1Mutation has no final error
  text in results; no completed mutation battery is credited. No dead seat was replaced.
- **Conformance debt:** protocol loading completed late (after freeze/dispatch); initial wave context
  omitted explicit pacman/scratch guard paragraphs. No retroactive compliance claim. The counter's
  first synthetic control failed 12/13 and misleadingly printed PASS with exit 3, then was repaired
  before freeze; final 13/13 rc0 is the scored state. Frozen instruments retain lexical limitations.
- **Misroot sweep:** fleet `git status --porcelain` showed only orchestrator-owned `.scratch/` changes
  and the pre-existing `after` file; no round-74 seat misroot. Transient owned probe/scratch trees
  removed. Attempt 1 left no round-74 lane outputs when this attempt began; none reused/discarded.

All abbreviated wave pointers above are under lane `.ufo/waves/round-74/`.

## Landed changes

| Commit | Changes | LOG linkage |
|---|---|---|
| `e51fb49d1790ef283b6aad6752a8c12fac347377` | frozen claims, instruments, snapshots, controls | LOG Round 74 declaration pointer |
| `810daf137d865e6a6f64937adedfa1acb828f414` | validated 12-seat spec/dispatch | LOG Round 74 dispatch pointer |
| `dc5114c5eb8e6349780d7bca8eb6e7470ec55553` | true note, five registry rows, two repairs, docs, lesson, QUALITY, settled wave/results | LOG Round 74 |
| `c3faaef8c47be23a831f0f9310815549767e8112` | measured outcome and before/end census receipts | LOG Round 74 final measurement |

Lane final pushed hash **c3faaef8c47be23a831f0f9310815549767e8112**;
`git -C tsukuroi-shokunin ls-remote origin refs/heads/master` printed that exact hash.
Measured artifact revision is dc5114c5; subsequent commit adds outcome/receipts, not instrument or rule changes.

## Before → after measurements

Real base d749a625 was confirmed by `git cat-file -t` → `commit`, rc0.
Receipt: `.ufo/waves/round-74/after/measure-dc5114c5.txt`; unchanged instrument bytes at both revisions.

| Claim | Command | Before d749a625 | After dc5114c5 | Verdict |
|---|---|---|---|---|
| C1 depth | `python3 tools/count-uf-rows-r74.py --revision <REV>` | `UF_MAP absent`, rc128; note absent | `UF_ROWS=6 UF_VERIFIED=6 UF_SOURCES=3 UF_SNAPSHOTS=3 UF_MALFORMED=0 met=1`, rc0 | mechanical target met; **literal claim not verified** |
| C2 freshness | `python3 tools/check-r73-routed-r74.py --revision <REV>` | `ROUTED_STALE=2 ROUTED_OK=0/2`, rc1 | `ROUTED_STALE=0 ROUTED_OK=2/2`, rc0 | repairs verified; lexical limits disclosed |

Registry/knowledge counts: **308→313**, **91→92**, from `git show <REV>:corpus/SOURCES.md`
matching `^ {0,3}\| *S[0-9]+ *\|`, and `.md` names in `git ls-tree --name-only <REV>:corpus/knowledge`.
Depth **8→8**, freshness **9→9**, other axis scores unchanged; no capability row or admission uplift.
Main/L1 exercised final checks once after seats settled: counter selftest 13/13 rc0, checker 6/6 rc0,
and census rc0. No broad existing census selftest or unrelated suite was run.

## Sources & frontier

Command at start and end:
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tsukuroi`.
Both outputs ended:
```
tsukuroi	ok	/home/vgpnk/Projects/shokunin/tsukuroi-shokunin/corpus/SOURCES.md
exit_code=0
```
Both also printed the same W04 duplicate-URL warnings. Full outputs are committed in
`before/census-start.txt` (transcribed initial response, labelled) and `after/measure-dc5114c5.txt`.
Rows **308→313**; added tier **A×4, B×1**: mined S309-S311 (A/code); refused S312 (B/community),
S313 (A/code candidate, HTTP404/unreachable). No prior status/recheck/used-by cell changed.
The lesson Gate records URLs, access dates and located quotes; S313 cannot supply a source-content
quote because its payload is unavailable, explicitly disclosed rather than fabricated.

C1 is sourced by S309-S311 opened this round, even though its literal claim misses. Frontier advances
in the corpus's true code reading; live invalid aliases, conflicting host fragments, intentional
perpetual masking, builtin selection and effective merged directives remain untested. No sibling
scope absorbed (`w1/C1Connector/report.md`); sibling consumers are not owners of this plane.

**Assimilation: none** — unresolved round-64 L0 collision/quarantine remains open; no package adopted.
`considerthese/2026-10-26.md` reopened: scoreboard/correction-propagation ideas informed the mistake and
attack ledger, but no already-implemented proposal is credited as a new acquisition.

## Trend verdicts

- **expansion: improved (corpus, not frozen claim credit).** One true six-row note and three mined
  upstream sources plus two measured refusals; registry 308→313, notes 91→92; R1Reviewer entails the
  actual rows. Literal C1 still fails.
- **quality: improved.** Both routed r73 repairs now present; stale 2→0 on unchanged instrument;
  wrong frozen alias set and invalid base suffix explicitly rejected/corrected, QUALITY 106/107
  carry red/green evidence. No false volume rule was admitted into the note.
- **discernment: unchanged (author-side).** In-wave attacks found the literal claim error and the
  lexical channels; outside non-author source/claim admission remains owed. No self-attested uplift.

## SHONEN

- [~] Real decision tables/error patterns/checklists with cited sources — SKILL Round 74 table and
  UF1-UF6, S309-S311. Independent whole-skill promotion verification not claimed.
- [~] End-to-end domain task executed and logged — LOG Round 74; host read-only diagnosis and
  S1Scout/E3HostProbe receipts. Deliberate host write paths remain untested.
- [~] Instructions executable without oral context — SKILL commands and note limits; whole-skill
  no-oral-context retest remains unexecuted (open L0 round-60).
- [~] No cross-domain bleed / PROVINCE accurate — Round 74 boundaries and connector scan; no
  outside non-author promotion verifier named, so no [x].

**Stale-lane:** no — one dispatched round, no other lane mission started.
**Open L0:** inherited round-60 no-oral-context retest and round-64 assimilation quarantine; no ruling presumed.
**Tool installs/upgrades:** none; existing curl/git/python3/jj helpers sufficient. Pacman untouched.
