# kotodama — round 93 (attempt 1)

Lane repo `kotodama-shokunin`, lane tip `80614d0f30f20791dc47a95ad9437088a00e4fce` (pushed, origin/main). Round base `8b2ce60a7bbf015f42a6c9e5c45e994e4c2f7742`; freeze `174fd5a8e05b3919a7854a4495c2fe0f28080775` (revision 2); lands `95e7a5cff1687b21d982607ab0bfd8e381c3036c`.

## Work performed

Declared claims (2, one per axis, both frozen in `reports/round-93/claims.json`):

1. **O — operability** (measured successor move): grader v4 of `tools/check-advance-evidence.py` refuses the round-92 counterfeit survivors on named legs, pins each entry-mode negative to the leg it names, and keeps the round-92 positive control green.
2. **C — coverage** (sourced claim): a dedicated entry on greeting and leave-taking formulae, which had zero filename owners at base, over four sourced registry rows opened 2026-11-05.

Work items (evidence pointers):

- Protocol load: `skill://shokunin`, fleet `MISSION.md`, `AXES.md`, `CORPUS.md`, `LEARNING.md`, lane `SKILL.md`, `SCORECARD.md`, `corpus/QUALITY.md`, `corpus/README.md`, newest lessons and the round-92 spot-check (`corpus/lessons/round-92-verifier-spotcheck.md`, eight routed items, all addressed or routed below).
- Grader v4 built and iterated: `tools/check-advance-evidence.py` sha `9799a96cf473278a75d19f51d93c4552cc94a611f7b008b36ef928c914ffaae7`; selftest 114/114 (`--selftest --work <dir>`); the first v4 mutation run scored 80/83 and the three survivors were fixture masking, fixed by exact-leg pins (lesson R93-M1).
- Round-92 counterfeit battery re-run against v3 (base) and v4 (lands): `reports/round-93/controls/v3-base-counterfeits.txt` (16 survivors plus an unnamed traceback) and `reports/round-93/battery93.py` (lands: one survivor, A1).
- Round-92 positive control graded by v4 at its landed revision `1473606b`: 9/9 (`reports/round-93/final/lands-C.txt` POSITIVE).
- Frozen counter `reports/round-93/measure93.py` (legs O: MATERIALIZE, TOOL, SELFTEST, OKCOUNT, REFUSALS, STABILITY, MUTATION, MUTRECEIPT, BATTERY, STUB; legs C: MATERIALIZE, ENTRY, POSITIVE, INDEX, CENSUS, APPENDONLY). Counter revision 1 to 2 (census leg reads the fleet-root script in file mode) was made before any data; see `reports/round-93/counter-revisions.md`. Do-nothing controls: `reports/round-93/controls/O-base-refusal.txt`, `C-base-refusal.txt`, `C-freeze-rev1.txt` (superseded), `C-freeze-rev2.txt` (C fails on ENTRY and APPENDONLY, as declared).
- Sources: four rows opened by ordinary HTTP on 2026-11-05 (`reports/round-93/evidence/S961.html`–`S964.html`, `manifest.json`); quotes located by the frozen grader's own normalization; a fresh re-open by ScoutReopen located all four quotes (`.ufo/waves/round-93/w1/ScoutReopen.md`). Unreachable candidates not rows: MDPI (HTTP 403, `unreachable-mdpi-403.raw`), Esan/àlago (TLS verification failure, not bypassed).
- Entry `corpus/knowledge/linguistics/greeting-leave-taking-formulae.md` (21043 B): drafted by ScribeEntry; one paraphrase corrected ("shortened" to "brief", per the S963 capture); cited-lines lint 0 findings; design sections labelled "(design, not sourced)".
- Claim-vs-source checks of the entry's riskier table cells against the captures: S964 familiarity, time elapsed and anticipated separation are verbatim in the capture; S963 brevity and the age-divided judgments are verbatim.
- Wave: one v1 wave, 10 seats, results in `.ufo/waves/round-93/w1-results.json` (all ten settled with output). ReviewerRows finding RR-1 applied before landing (S963 teaches cell).
- Lesson `corpus/lessons/round-93.md`: Gate (four admit lines copied byte-exact from the frozen list; search log with a reason per excluded candidate), Mistakes, Corrections (round-92 Signifiances description and the claim-C premise erratum, append-only), Quarantine (round-91 verdicts stand, nothing adopted), Assimilation (none; `considerthese/` absent; no `operator-*.md` lessons exist), Routed to round 94 (appended after landing).
- QUALITY criterion 37 (reason on record; title-only triage is not an exclusion): red-before on round-92 (its exclusions are one prose paragraph, no per-candidate bullets, zero reason tokens across fifteen named candidates); on round 93, 31 excluded bullets, zero without a reason token (command in the criterion).
- Records: `SCORECARD.md` round-93 section, `LOG.md` round-93 entry, `reports/round-93/final/lands-O.txt` and `lands-C.txt`.

Seat findings and dispositions (ten seats, all settled):

- ReviewerRows (reviewer): RR-1 applied (S963 teaches). Rows PASS otherwise.
- CriticClaims93 (critic): three survivors, two unnamed tracebacks, one wrong-leg refusal, one wrong-direction parse on new counterfeit classes. Routed to round 94 with recipes (lesson `## Routed to round 94`). The frozen O predicate does not claim these classes; v4 is not weakened against v3 on any of them.
- MutationTesterV4 (mutation-tester): five of ten new mutants survive (script/style strip, comment strip, entity unescape, disposition case flag, base-row `opened` identity cell). The shipped tool does perform each check; these are selftest pin gaps. One channel is narrow and real (unanchored lowercase verdict outside line start). Routed to round 94; not patched because a tool change after seats scored the frozen bytes would move the claim's rule.
- ConnectorOverlap (connector): the entry is the owner the lane's own cross-references pointed at (`culture-material/adornment-body-codes.md:5`, `costume-semiotics.md:143`) but `politeness-taboo-euphemism.md` holds no greeting line; those cross-references remain dangling and are routed.
- ExecRegistryRows, ExecIndexRow, ExecCounterReplay (executors): census file-mode rc 0 with zero E-findings and no S961–S964 findings; index tool OK 265/265; claim-C do-nothing and refusal behaviour replayed (matches receipts).

Not done this round (disclosed): the three round-92 re-decisions (Awetí 2015, Zulu Lexikos 2011, Turkish Signifiances 2020) on their captured text, and the 16 title-only exclusions, remain open; the L0 question on the round-92 overlap (`ideophones-mimetics.md` vs `sound-symbolism.md` §6) remains unanswered.

## Landed changes

| change | commit | LOG / SCORECARD |
|---|---|---|
| Round-92 residue: committed the dispatch-renamed wave marker | `3c81f922` | LOG round 92 residue (not a round-93 claim) |
| Freeze revision 1 (grader v4, counters, claims, controls, captures) | `1928e00d` (superseded before data) | superseded by revision 2; see `counter-revisions.md` |
| Freeze revision 2 (census leg path; do-nothing receipts) | `174fd5a8` | LOG round 93 |
| Land claims O and C (entry, S961–S964 rows, search-log note, README index, lesson, QUALITY 37) | `95e7a5cf` | LOG round 93 |
| Records (SCORECARD, LOG, lesson addendum, final counter receipts) | `9778ccc2` | SCORECARD round 93 |
| Wave-1 evidence (spec, dispatch, registry, seat reports, stage outputs, ready handoff) | `80614d0f` | — |

Corpus and tool bytes landed: `tools/check-advance-evidence.py` (v4), `reports/round-93/*` (counter, instrument, mutants, claims, evidence), `corpus/knowledge/linguistics/greeting-leave-taking-formulae.md`, `corpus/SOURCES.md`, `corpus/README.md`, `corpus/lessons/round-93.md`, `corpus/QUALITY.md`.

## Before → after measurements

**Claim O — operability (verifies on the frozen predicate).** Base `8b2ce60a` with v3 (sha `905be2fe`) vs lands `95e7a5cf` with v4 (sha `9799a96c`).

| measure | before (v3) | after (v4) | command |
|---|---|---|---|
| selftest | 89/89 | 114/114, four concurrent runs 114/114 | `python3 -B tools/check-advance-evidence.py --selftest --work <dir>` |
| round-92 counterfeit battery | 16 SURVIVOR + 1 unnamed traceback | 1 SURVIVOR (A1, forged committed capture: residual) | `python3 -B reports/round-93/battery93.py` with `R93_ROOT`, `R93_WORK` |
| mutation | 60/60 (round 92, not re-run) | 83/83, receipt `reports/round-93/mutation-score.txt` | `python3 -B reports/round-93/mutants.py --root . --work <dir> --out reports/round-93/mutation-score` |
| round-92 positive control | — | 9/9 | `reports/round-93/final/lands-C.txt` POSITIVE |

Counter: `python3 -B reports/round-93/measure93.py --root <lane> --lands 95e7a5cf… --freeze 174fd5a8… --claim O --work <dir>` → `MEASURE93-O: PASS legs=10/10` (`reports/round-93/final/lands-O.txt`).

**Claim C — coverage (verifies on the frozen predicate).** Base `8b2ce60a` vs lands `95e7a5cf`.

| measure | before | after | command |
|---|---|---|---|
| greeting or leave-taking filename owners in `corpus/knowledge` | 0 | 1 | `git ls-tree -r --name-only <rev> corpus/knowledge \| grep -ci greet` |
| linguistics files | 37 | 38 | `git ls-tree -r --name-only <rev> corpus/knowledge/linguistics \| wc -l` |
| registry rows | 884 | 888 | `git show <rev>:corpus/SOURCES.md \| grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'` |
| mined A rows | 522 | 526 | awk on column 5 and column 8 of the registry table |

Counter: `python3 -B reports/round-93/measure93.py --root <lane> --lands 95e7a5cf… --freeze 174fd5a8… --claim C --work <dir>` → `MEASURE93-C: PASS legs=6/6` (`reports/round-93/final/lands-C.txt`).

## Sources & frontier

- Registry before → after: 884 → 888 rows (command above, measured at `8b2ce60a` and `95e7a5cf`); rows added by tier: A 4 (S961, S962, S963, S964), B 0, C 0; rows touched old→new: none (BASEROWS and APPENDONLY pass; `git diff --numstat 8b2ce60a 95e7a5cf -- corpus/SOURCES.md` adds rows and a search-log note only).
- Census: `scripts/sources-census.sh validate --file <lands corpus/SOURCES.md>` rc 0 at lands (counter CENSUS leg); E-findings 0; W-findings are pre-existing (W04 duplicate URLs across scopes, W01 tierC mined) and not introduced by this round. Round-start census (`reports/round-93/census-start.txt`) rc 0.
- Status changes old→new: none on base rows. New rows: `mined` (four).
- Frontier rows advanced: greeting and leave-taking formulae moved from frontier to core (entry plus S961–S964); the entry names its own unheld ground (Limits section) and the design procedure is marked as design.
- Search log: `corpus/SOURCES.md` `## Search log` note (round 93) and the lesson's `## Gate` (five DOAJ queries, a reason for each excluded record).
- Assimilation: none (no package adoption; quarantine verdicts from round 91 stand; `considerthese/` absent; no `corpus/lessons/operator-*.md` teachings).

## Trend verdicts

- **expansion: improved.** A dedicated entry on ground with zero filename owners; four new mined A rows cited by it; per-claim sources located in captures (`reports/round-93/final/lands-C.txt`, `.ufo/waves/round-93/w1/ScoutReopen.md`).
- **quality: unchanged.** No admitted entry was re-verified, deepened or superseded (criterion 20: instrument and record repairs are not quality observables).
- **discernment: improved.** A closure disagreement (round-92 spot-check §4: title-only exclusions) became lesson R93-M2 and a grounded QUALITY criterion (37), which LEARNING.md names as the improved condition. The three specific re-decisions remain open and are not claimed.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — pointer: `SKILL.md` decision and error tables (unchanged this round; no non-author verification).
- [~] At least one end-to-end domain task executed and logged in LOG.md — pointer: `LOG.md` round 93 (entry plus registry rows plus instrument, measured at lands `95e7a5cf`).
- [~] Instructions executable by an agent without oral context — pointer: `tools/check-advance-evidence.py --selftest` 114/114 and `reports/round-93/mutation-score.txt` 83/83 at `9799a96c`; residuals routed to round 94.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — pointer: `.ufo/waves/round-93/w1/ConnectorOverlap.md` (owner list, dangling `politeness-taboo-euphemism.md` cross-references routed; no sibling content absorbed).

No box is `[x]`: no non-author verifier has checked this round.

## Round shape, seats and tooling

- Shape: one v1 wave of 10 seats (2 scribe, 3 executor, 1 scout, 1 connector, 1 reviewer, 1 critic, 1 mutation-tester); attack seats 3/10 = 30%; connector seats 1; the L1 holds the planner role (the validator rejects planner as a seat). Round total 10; no residual call.
- Dead seats: none. All ten settled with output (`.ufo/waves/round-93/w1-results.json`).
- Seat answering models: per the route table for each role; not individually recorded.
- Stale-lane: no other mission of this lane is open; the driver's round-93 launch is the only one.
- Tooling: no installs or upgrades by this round (no tool was needed beyond the existing `python3`, `curl`, `node`, `git`, `jj`). Host state untouched: no pacman transaction, no sysctl change (the operator note on `user.max_user_namespaces` is acknowledged; no seat required a sysctl).
- L0 questions: none appended this round. Open from before: kotodama round-11 and round-89 (freshness pause), round-92 (overlap of `ideophones-mimetics.md` with `sound-symbolism.md` §6).
- Misroot sweep: `git status --porcelain` at the fleet root shows no file written by a round-93 seat. Pre-existing fleet-root entries (`.scratch/run15-state.json` modified; `.ufo/closure-kaidoku-r92.json` untracked) belong to the orchestrator and another lane and were not touched.
- Lane pre-report gate: `git ls-remote origin refs/heads/main` must print `80614d0f30f20791dc47a95ad9437088a00e4fce` (checked before this report was committed).

## Errata

- The round-92 lesson's Signifiances description and the round-92 claim-C premise are corrected append-only in `corpus/lessons/round-93.md` `## Corrections`.
