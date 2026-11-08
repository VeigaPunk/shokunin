# tsukuroi — round 98 report

Lane: `tsukuroi-shokunin` (operability + freshness; host operability and repair). Campaign: hyaku,
run 15. Round 98, attempt 1. Pre-round tip `b3be3f90c2e32400d4e2692b2656ec9a1ba14a8a`; freeze
`1cfeb5d5089097fdffef761ad0e2b8dfa75a2793`; the wave's evidence is committed with the settle
`270ca298d7aac4a3bd11c75900e3a9faa21098f7` (this round has no separate wave commit: the wave dir
was staged with the settle after the wave settled at 10:27:05), plus the ledger repair
`839954b79d8cda9564e181b1bd7dbe3bc9f51e77`. Lane tip at filing —
`git ls-remote origin refs/heads/master` prints `839954b79d8cda9564e181b1bd7dbe3bc9f51e77`.

Declared claims — **C1 depth 8** (the tie-lowest non-retired axis): the two r97 families assert the
JSON metadata their own cases emit (the r97 A7 limit closed) and the LZ docstring's text-comparer
sentence is corrected (R97-D3/A6); **C2 freshness 9**: the registry-content checker binds the
comma-span form and its selftest covers the non-contiguous `VARIANTS` branch (the r97 MutRegistry
M08 survivor). Adjacency (8, tied lowest) carried no claim: the kaidoku/revenger
reverse-engineering ownership is operator-owned and unruled.

## Work performed

- **C1 — depth.** `tools/limine-pin-battery-r98.py` keeps the r97 roster at 105 and sets
  `check_echo` + `check_era` on `REFUSAL-VERSIONS-9DIGIT-Z` and `LEADING-ZERO-NORMALIZE`, so each
  case asserts `limine_version` (the flag spelling verbatim, source `flag`) and `visibility_era`
  (the label the whole tuple selects); `fam_leading_zero_normalize`'s docstring now names the real
  text-comparer discriminator (`12.000000009.000000005`, text orders era A while `int()` reads
  12.9.5). `tools/make-r98-bends.py` emits the two one-clause bends `N07-era-field-lie` (label
  swapped for every Z/LZ spelling) and `N08-echo-norm` (echo replaced by the numeric tuple).
  Evidence: `before/dev/c1-gate-runs3.json` (`105/105 met` x3), `w1/ExecGateRuns/` (landed gate x3
  canonical + x3 clone, 0 error rows, `c1-usage.json` met 19/19), `w1/ExecBends/` (N07 `103/105` x3
  canonical + x3 clone; N08 `104/105` x3 both layouts; 0 error rows), `w1/ExecDoNothing/` (r97
  control `met 105/105` x3 on the gate and both bends; control `e678c34f…` = `b3be3f90:tools/limine-pin-battery-r97.py`),
  `w1/ReviewBattery/` (six attack gates: era-lie-everywhere `102/105`, fixed-echo `100/105`,
  X-cap-only lie `104/105`, source-lie `102/105`, echo-truncation `100/105`, **Y-cap-only era lie
  `105/105` = survivor**), `w1/MutRegistry/` (B01-B05).
- **C2 — freshness.** `tools/check-registry-content-r98.py` extends the `RC-BEND-SPAN` capture to
  `N<digits>-N<digits>|N<digits>(,N<digits>)+` and adds `span-gap` / `span-gap-lie` selftest cases
  (12 → 14). Evidence: `before/dev/c2-selftest-r98.txt` (`PASS 14/14`), `c2-selftest-r97.txt`
  (`PASS 12/12`), `c2-m08-selftest.txt` (M08 `FAIL 12/14`, exactly the two gap cases red),
  `w1/ExecRegistry/` and `w1/ReviewRegistry/` (D1 `FAIL` one `RC-VALUE-MISMATCH` vs r97
  `RC-CELL-MISSING`; D2 `PASS` with M08 `FAIL`; D2lie inverts both; coverage `PASS 157/157
  findings 0` on every doctored revision), `w1/MutRegistry/` (M01-M10: 7/8 killed, M07 survives).
- **Frontier step.** S394 opened and admitted (own-work: the gate's report contract at its MAIN
  return, bytes 16931/17037, with the early-return copies at 11230/11344 — S394 *supersedes* S393,
  whose anchor labelled the early-return pair as the main return; found by `w1/ScoutSources`, §2);
  S392 re-opened byte-identical (`d92580dd…`, 331022 bytes, offsets 157767/153202/159315 re-measured
  with `grep -abo`); one candidate rejected (`limine` v12.9.6 `CONFIG.md`: HTTP 200, 27609 bytes,
  `f44f3a19…`, zero occurrences of the gate's JSON fields, of `echo` and of `version`).
  `corpus/lessons/round-98.md` carries `## Gate` (2 admits + 1 reject + the in-place change table),
  five mined mistakes (R98-FIELD-NOT-ASSERTED with a PROPOSED QUALITY criterion plus the four
  below), the census block, the counter-attack scoreboard (QUALITY 115), `## Frontier moved this
  round` and the routed table; `corpus/README.md` gains § "Round 98".
- **Wave.** One v1 wave, 14 seats under `ufo-wave-policy.json` (band 8-16): 5 executors, 2 scouts,
  2 scribes, 2 reviewers, 1 critic, 1 mutation-tester, 1 connector; attack roles by the prefile
  gate's set = 5/14 = **36 %** (floor 25 %), connector seats 1 (limit 2). Validator counts
  **14 spawn / 0 resume / 14 total**, `w1-validate.err` 0 bytes; `.ready` taken 10:02:04; settled
  10:27:05 with **14/14 settled, 0 dead** (`w1-results.json`). Residual call: none (14 ≥ the 8
  protocol floor). Two seats' long children (the battery's `--selftest --reference` leg, ~50 min
  under fleet load) were stopped host-side so the wave could settle; both seats recorded the leg as
  `not completed — time-bounded` and the capability it covers is carried by the landed-gate legs and
  the r97 analogue.
- **Ledger.** `.ufo/waves/round-98/claim-falsification.tsv`, 18 rows: 3 `falsifies-wording` (A1, A3,
  A4), 1 `falsifies-number` (A2), 14 `neutral`, covering C1 and C2 and every attack seat
  (`ReviewBattery`, `ReviewRegistry`, `CriticClaims`, `MutRegistry`, `ConnectorOverlap`). Gate
  output pasted below.
- **Stale-lane:** respawn-per-round driver; no other mission of this lane is open. The wave's
  `.ready` was taken 10:02:04 and every seat settled before filing.
- **Inherited state.** No uncommitted lane-authored leftovers from an earlier attempt; this round's
  own work only. No `round-*-aggregator-*` or `round-*-verifier-spotcheck.md` file was edited.
- **Misroot sweep.** `git -C /home/vgpnk/Projects/shokunin status --porcelain` → 11 paths; none
  names tsukuroi or round 98 (`.scratch/*` is orchestrator-owned, `.ufo/reports/round-68/kagi.md`
  and `.ufo/reports/round-89/tabi.md` are other lanes' reports, `scripts/hyaku/__pycache__/*.pyc`
  predates this round and is not lane-authored). Nothing was copied or deleted.
- **Tool installs:** none (python3 3.14.8, git 2.56.0, curl 8.23.0, bwrap already present; pacman
  untouched and paused; no `sudo`).
- **L0:** no new question. The r86 host-incident line stays open (operator-owned repair of the two
  UKI digests); nothing in this round touches /boot.

## Landed changes

| change | LOG entry | commit |
|---|---|---|
| freeze: r98 battery + bends generator + r98 checker, plan, claims, controls, bends, doctored-fixture recipe, dev receipts, S393 + knowledge-entry draft | `Round 98 — freeze` | `1cfeb5d5` |
| settle: wave w1 evidence (14 seats, 0 dead, `w1-results.json`), S394 supersedes S393 + entry narrowed (PC1-PC4), lesson (5 mistakes + scoreboard + frontier), README § Round 98, SCORECARD declaration + measured rows, three registry rows, amendments A1-A7, falsification ledger | `Round 98 — settle` | `270ca298` |
| ledger repair: artifact paths and duplicate rows so the prefile gate passes (18 rows, 0 findings) | `Round 98 — settle` | `839954b7` |

Both commits are `jj-lane.sh` `landed <hash>` lines after remote verification; the lane tip equals
`git ls-remote origin refs/heads/master` (below). The wave's dispatch/ready/results and every seat
receipt are inside `270ca298` under `.ufo/waves/round-98/`.

## Before → after measurements

### C1 (depth 8)

Counting command: `python3 tools/limine-pin-battery-r98.py --gate <GATE> --runs 3 --work <scratch>
--json <out>`, parsed by `python3 .ufo/waves/round-95/before/controls/count-runs.py <out> --family
REFUSAL-VERSIONS-9DIGIT-Z --family LEADING-ZERO-NORMALIZE`; bends via
`before/controls/bends/<bend>.py`; do-nothing via `before/controls/do-nothing-battery-r97.py`.

| leg | before (r97 instrument `e678c34f…`) | after (r98) | receipt |
|---|---|---|---|
| landed gate, canonical | `met 105/105` x3, 0 error rows | `met 105/105` x3, `[]`, 0 error rows | `before/dev/c1-gate-runs3.json`; `w1/ExecGateRuns/c1-gate-canonical.json` |
| landed gate, clone | — | `met 105/105` x3, 0 error rows | `w1/ExecGateRuns/c1-gate-clone.json` |
| `N07-era-field-lie` | `met 105/105` x3 (blind) | `103/105` x3 both layouts, `[LEADING-ZERO-NORMALIZE, REFUSAL-VERSIONS-9DIGIT-Z]`, 0 error rows | `w1/ExecBends/c1-bend-N07-era-field-lie-{canonical,clone}.json` |
| `N08-echo-norm` | `met 105/105` x3 (blind) | `104/105` x3 both layouts, `[LEADING-ZERO-NORMALIZE]`, 0 error rows | `w1/ExecBends/c1-bend-N08-echo-norm-{canonical,clone}.json` |
| roster | 105 | 105 (`len(FAMILY_ROSTER)=105`, `tuple(FAMILIES)==FAMILY_ROSTER True`, `cases 420`) | `w1/ExecGateRuns/02-roster.txt`, `10-per-run.txt` |

### C2 (freshness 9)

Counting command: `python3 tools/check-registry-content-r98.py --revision <REV> --json <out>` and
`--selftest`; the doctored legs are reproduced by
`sh .ufo/waves/round-98/before/fixtures/build-doctored-fixture-r98.sh`.

| leg | before (r97 checker `2daf5926…`) | after (r98) | receipt |
|---|---|---|---|
| landed revision `b3be3f90` | `PASS 7/7` | `PASS 7/7` | `before/dev/c2-content-landed-{r97,r98}.txt` |
| selftest | `PASS 12/12` | `PASS 14/14` | `before/dev/c2-selftest-{r97,r98}.txt` |
| M08 one-fault mutant | `PASS 12/12` on the r97 checker (survives) | `FAIL 12/14` on the r98 checker (`span-gap` + `span-gap-lie` red) | `w1/MutRegistry/receipts/M08-on-r97-selftest.txt`; `before/dev/c2-m08-selftest.txt`; `w1/ExecRegistry/report.md` |
| D1 (row `N01-N04` → `N01,N03`) | `RC-CELL-MISSING` | `FAIL` exactly one `RC-VALUE-MISMATCH` (derives `N01-N04`) | `before/dev/c2-D1-*.txt`; `w1/ReviewRegistry/03-D1*` |
| D2 (keys `N01,N03`, row `N01,N03`) | `RC-CELL-MISSING` | `PASS 7/7`; M08 `FAIL` one | `before/dev/c2-D2-*.txt`; `w1/ExecRegistry/D2-*` |
| D2lie (keys `N01,N03`, row `N01-N03`) | `RC-VALUE-MISMATCH` | `FAIL` one; M08 `PASS` | `before/dev/c2-D2lie-*.txt` |
| coverage on each doctored revision | `PASS 157/157` | `PASS 157/157 findings 0` (blindness leg holds) | `before/dev/c2-D*-coverage.json` |
| settled tip `270ca298` | coverage `PASS 157/157` | content `PASS 7/7`; coverage **`PASS 160/160 findings 0`**; header gate `114/114`; census exit 0 | `after/c2/` receipts; the four gate outputs in the transcript |

Instrument integrity at scoring: `sha256sum -c before/instruments.sha256` → 27 OK (gate
`7d79ac29…`, battery-r98 `8198bd84…`, checker-r98 `5bb1441e…`, bends `2d8f4f6e…` / `45d8d00d…`,
controls `e678c34f…` / `7d79ac29…` / `2daf5926…`). The r97 battery and checker keep their landed
bytes and are the round's do-nothing controls.

## Sources & frontier

Census (frozen command `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin
tsukuroi`): before `git show b3be3f90:corpus/SOURCES.md` → exit 0, 392 rows
(`grep -cE '^\|[[:space:]]*S[0-9]{3,}'` → 392); after the landed tree → **394 rows, exit 0, 0 E
findings** (57 W04 + 1 W01, the standing warning set). Rows added by tier: two A (own-work: S393
and its supersession S394). Rows touched old→new: S393 `status` `mined` → `queued` and `used-by`
`corpus/knowledge/limine-metadata-assertions-r98.md` → `—` (both logged in the lesson's in-place
table; S394 carries the citations). Frontier rows advanced: the r97 Frontier's A7 (field/echo
coverage of the new members) and M08 (selftest case) are closed; the wave added named limits
(hybrid comma cell F1, duplicate same-cell mention F2, spaced/lowercase forms A3, Y-cap field lies
A4, the X-cap's single-case field coverage A5, unbound rows now 153/157 at the base and 156/160 at
the tip A6, the successor's unchanged JSON schema token A7, M07's untested ancestor branch, and the
battery selftest's missing echo/era lie kind) — all in `corpus/README.md` § "Frontier (round-98
addition)" and routed to r99. Assimilation: none this round (`merge/tsukuroi/` unchanged;
`considerthese/2026-10-26.md` was surveyed by the connector — "Cross-note correction propagation
map" implemented under QUALITY 108, "Downstream patch-offset check" partial).

## Trend verdicts

- **expansion — improved.** Two admitted own-work rows (S393 and its correction S394) and one new
  knowledge entry (`corpus/knowledge/limine-metadata-assertions-r98.md`, PC1-PC4 + limits) on
  ground the coverage map did not hold (the gate's *reported* metadata, which no lane entry
  covered); S392 re-opened byte-identical; net +2 rows (392 → 394), none removed.
- **quality — improved.** The r97 A7 limit is closed by two bends the r97 instrument is blind to
  (`met 105/105` → `103/105` / `104/105`), the r97 M08 survivor is killed by two selftest cases and
  a doctored revision pair that inverts under the mutant, and the r97 docstring defect (second
  instance of its class in two rounds) is corrected in the successor with its manifest relation
  stated. No admitted entry fails its re-check.
- **discernment — improved.** The lane's own anchor was caught by a seat (S393's byte pair named
  the early return; S394 states both sites), the reviewer found two false-PASS shapes in the new
  capture plus a survivor the claim's universal sentence did not cover (Y-cap fields, amendment
  A4), a wave receipt that measured a *different* mutant than the one it named is recorded as A2
  instead of being cited for the M08 kill, and two seats' kill/survive direction was corrected from
  the receipts (B01/B02 are killed, not survivors). Five mistakes are mined with
  red-before/green-after pairs.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — evidence:
  the health-verdict decision table (`SKILL.md:38-50`), the update-safety checklist
  (`SKILL.md:90-141`), the error-pattern list (`SKILL.md:2028-2036`), the registry section the round
  extends (`SKILL.md:5777-5946`); non-author verification still owed.
- [~] At least one end-to-end domain task executed and logged in LOG.md — evidence: the C1
  certification runs (`w1/ExecGateRuns/`, `w1/ExecBends/`, `w1/ExecDoNothing/`) and the C2 doctored
  legs (`w1/ExecRegistry/`, `w1/ReviewRegistry/`) are end-to-end executions of the lane's own gates;
  `LOG.md` "Round 98" entries.
- [~] Instructions executable by an agent without oral context — evidence: the three r98 instruments
  carry their contract in their docstrings and registry rows (`SKILL.md:5944-5946`), and 14 seats
  executed them from those instructions alone; the whole-SKILL replay remains unexecuted.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — evidence: `PROVINCE.md` unchanged this
  round; the connector's 20-sibling sweep found no duplicate or contradictory claim
  (`w1/ConnectorOverlap/report.md`); kaidoku/revenger ownership stays operator-owned and unruled.

## Prefile falsification gate

`python3 /home/vgpnk/Projects/shokunin/scripts/hyaku/prefile-falsification.py --lane tsukuroi
--round 98` → `PREFILE-FALSIFICATION: pass claims=2 rows=18 attack_seats=5 findings=0` (exit 0).
