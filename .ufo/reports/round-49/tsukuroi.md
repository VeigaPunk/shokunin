# tsukuroi — round 49 (hyaku run 11, attempt 1)

Lane: `tsukuroi-shokunin` (host operability & system repair). L1: `TsukuroiR49`.
Base `6256760d1382ce4ce20fcba830d4b2912cfbf12b` → freeze `55c07cd3f8bff2e12117c34d57b4c618de74d85c`
→ spec/dispatch `32a85560` → controls `d7cfc273` → C3 fix `07329036` → integrated `823425c5` → receipts
`5510d6ad` → cells `0ec92fc2` → outcome `59cc42aa` → final lane tip `ff9169722d41bebf0e1192571bc13ee757882d92`
(`git ls-remote origin refs/heads/master` prints it).

Round shape: **one v2 wave (`w1`), 73 seats** under policy v2 (band 64–128): reviewer 18, critic 15, scout 13,
executor 10, scribe 7, mutation-tester 4, sentinel 4, connector 2; attack roles 37/73 = 50.7 %. 73 dispatched,
73 `results` entries, 73 reports, **0 dead seats**, no residual call. The L1 holds the canonical planner seat (the
validator rejects `planner` as a swarm role; a bounded planning walk rode the connector and scout items).

## Work performed

Declared claims (1–3, frozen at the freeze commit; `.ufo/waves/round-49/frozen/FROZEN.md`):

1. **C1 — depth (lowest tied axis, 8):** apply the seven corrections the round-48 counted seats named to
   `corpus/knowledge/btrfs-scrub-grounding-r45.md` GR1/GR2, then re-read the rows with a fresh 18-seat cohort
   (`R49RevGR{1,2,3}{a,b,c}`, `R49CritGR{1,2,3}{a,b,c}`). Counter `tools/check-scrub-admission-r49.py`.
2. **C2 — adjacency (lowest tied axis, 8):** the `PROVINCE.md` ADJ-01..07 **Ownership source** cells stop citing
   bare sibling line ranges (9 at base) and cite the portable `OUT-0NN` anchors that carry each class's pinned
   sibling commit, heading and ≤25-word quote. Counter `tools/check-adjacency-table-r49.py`, with the existing
   `tools/check-adjacency-anchors.py` as the content leg.
3. **C3 — operability (sourced: S255, re-opened this round):** `tools/tsukuroi-census.sh`'s alias resolver records
   `ST_BASE_ERR` and `--selftest` prints a named descriptor-band diagnostic instead of failing silently; the stale
   `builds a /tmp fixture tree` comment is gone; one `(R49-C3)` case proves the exhausted-band path (166 → 167
   cases). Counter `tools/check-fd-band-r49.py`.

Work items (73, each with a report under `.ufo/waves/round-49/w1/`):

- **C1 corrections and verification** — `R49ExecGRCorr` (seven corrections verified against the r48 seat reports,
  `supports`), `R49RevCorr` (independent re-read, `supports`), the 18 counted seats (17 `holds`, one bound `partly`:
  `w1/R49CritGR2b.md` defect 1 — the `[inference]` mark still claims the ioctl side is unpinned although S240 pins
  `ioctl.c` and the row cites `ioctl.c:3132`/`:3190`).
- **C1 counter attacks** — `R49CritCounter` (10 of 22 cheat scenarios PASS the frozen counter, including 9
  fabricated cohorts; receipts `w1/R49CritCounter/`), `R49MutCounterA/B` (mutants, `supports`/`defect-found`),
  `R49SentForge` (forgery probe, `defect-found`), `R49LabParse` (report-parser edge cases, `defect-found`),
  `R49RevCounter`, `R49RevMarks`.
- **C2 work** — `R49ExecAnchorA` (`supports`: all nine anchors re-derived from the registry and sibling blobs),
  `R49ExecAnchorB`/`R49RevAdjB`/`R49CritAdjA` (`defect-found`: the predicate was false at the freeze revision
  because the census edit shifted IN-109 and the repin landed one commit later; the counter is a shape test that a
  stub table can pass; H1–H5/M1–M2 fixture defects), `R49ScoutAdjLl`, `R49RevAdjA`, `R49CritAdjB` (drift table:
  pinned vs current sibling tips), `R49MutAdj` (`supports`).
- **C3 work** — `R49ExecFdA` (behaviour matrix, `defect-found`), `R49ExecFdB`, `R49RevFdA` (**D1 HIGH**: the new
  case made `--selftest` FAIL whenever the caller's TMPDIR needs the alias — reproduced by the L1 and fixed in
  `07329036`), `R49RevFdB`, `R49CritFdA`, `R49CritFdB` (a 19-line "liar" census PASSes the counter),
  `R49MutFd`, `R49LabFd` (`supports`).
- **Sources (opened this round)** — `R49ScoutCmd` (S246), `R49ScoutIoctl` (S240), `R49ScoutSysfs` (S243),
  `R49ScoutDevRepl` (S247), `R49ScoutKillXml` (S248), `R49ScoutProcFd` (**falsifies**: `proc_pid_fd(5)` does not
  state `/proc/self/fd/<n>/<child>` traversal), `R49ScoutBashRedir` (S255, no new row), `R49ScoutReject` (admit/reject
  sample), `R49ScoutSources` (registry census), `R49ExecSelfAssess` (self-assessment at freeze + a pre-existing
  census-case self-contradiction, `§4`).
- **Frontier / conformance / process** — `R49ScoutConsider`, `R49ScoutQuality`, `R49ConnWave`, `R49ConnClaims`,
  `R49ScribeLesson`, `R49ScribeLog`, `R49ScribeScore`, `R49ScribeSkill`, `R49ScribeReadme`, `R49ScribeAssim`,
  `R49CritAssim`, `R49SentScopeA/B`, `R49SentSeat`, `R49Distill`, `R49Simplify`, `R49ExecGates`,
  `R49ExecLiveCensus`, `R49ScoutHost`, `R49ScribeCoverage`.

Pre-data controls (frozen counters, scored before the wave was dispatched; receipts
`.ufo/waves/round-49/controls/battery-summary-r49-c{1,2,3}.jsonl`): C1 K0/K1/K2/K3/K4/K5/K6 FAIL and K-pass PASS;
C2 K0/K1/K2/K3 FAIL and K-pass PASS; C3 K0/K1/K2 FAIL and K-pass PASS. Two control-fixture bugs were found while
scoring and fixed before data (recorded in the lesson); no claim byte changed.

## Landed changes

| Change | LOG.md entry | Commit |
|---|---|---|
| Freeze: three claims, three frozen counters, the seven r48-named GR corrections, pending gate heading, FROZEN.md, SCORECARD declaration, LOG entry, start census | round 49 entry (declaration) | `55c07cd3` |
| w1 spec (73 items) + validated dispatch + IN-109 repin 2642→2660 | round 49 entry (Freshness) | `32a85560` |
| Pre-data control batteries + FROZEN control addendum | round 49 entry (controls) | `d7cfc273` |
| C3 regression fix (`R49RevFdA` D1/D5), `fd-band-invalid` for a malformed band (D3/D4), usage text (D2), S255 `used-by` | round 49 entry (C3 + Freshness) | `07329036` |
| Wave integration: 73 reports + `w1-results.json`, lesson, SCORECARD axes/capabilities restatement, SKILL/README notes, IN-109 repin 2660→2671 | round 49 entry (measured outcome) | `823425c5` |
| Measured receipts (C1/C2/C3 final, base receipts, end census, r48 TMPDIR counter) | round 49 entry (measured outcome) | `5510d6ad` |
| Self-assessment cell corrections (SKILL 4572, README 500, `--identity landed`, `formal overlap table present`) | round 49 entry (calibration) | `0ec92fc2` |
| Measured outcome section + LOG `Measured` block | round 49 entry (measured outcome) | `59cc42aa` |
| Calibration receipt pinned (27 checks, 0 mismatches) | round 49 entry (calibration) | `0c2d6678` |
| Interim self-assessment receipt (superseded by the above) | — | `ff916972` |

## Before → after measurements

| Claim | Counting command | Before (base `6256760d`) | After (measured `823425c5`) | Verdict |
|---|---|---|---|---|
| C1 depth | `python3 tools/check-scrub-admission-r49.py --revision <REV>` | `structural_ok 1, corr_ok 0, quotes_ok 3, verdicts_ok 0, seats_ok 0, marks_ok 0` → FAIL (`.ufo/waves/round-49/before/c1-at-base.json`) | `structural_ok 1, corr_ok 1, quotes_ok 3, verdicts_ok 0, seats_ok 18, marks_ok 0` → FAIL (`.ufo/waves/round-49/after/c1-final.json`) | **FAIL** |
| C2 adjacency | `python3 tools/check-adjacency-table-r49.py --revision <REV>` | `adj_rows 7, linked_rows 0, bare_ranges 9, anchors_ok 0, registry_ok 0` → FAIL (`.ufo/waves/round-49/before/c2-at-base.json`) | `adj_rows 7, linked_rows 7, bare_ranges 0, anchors_ok 7, registry_ok 7, anchors_checker_rc 0` → PASS (`.ufo/waves/round-49/after/c2-final.json`) | **PASS** |
| C3 operability | `python3 tools/check-fd-band-r49.py --revision <REV>` | `stale_ok 0, diag_ok 0, band_ok 0, cases 166` → FAIL (`.ufo/waves/round-49/before/c3-at-base.json`) | `stale_ok 1, diag_ok 1, band_ok 1, cases 167` → PASS (`.ufo/waves/round-49/after/c3-final.json`) | **PASS** |
| C3 regression (not a claim) | `python3 tools/score-selftest-tmpdir-r48.py --revision <REV> --cases 167` | the round's own fix made a dirty-TMPDIR `--selftest` FAIL (`R49RevFdA` D1, reproduced by the L1) | `pass_ok 4, loc_ok 4, clean_ok 4, failfast_ok 2, term_ok 1, static_ok 1` → PASS (`.ufo/waves/round-49/after/r48-tmpdir-counter-at-e1.json`) | regression **closed** |
| Calibration | `python3 tools/check-self-assessment.py --revision <REV>` | 4 mismatches before the restatement (K08, K11, K14, K15 — all created by this round's appends; 2 at freeze, K13/K17, so the declaration's "3" was wrong) | `checked 27, mismatches 0, PASS` (`.ufo/waves/round-49/after/calibration-final.json`) | **PASS** |

C1's FAIL is reported, not narrowed: (a) `R49CritGR2b`'s bound `partly` blocks GR2 by the frozen rule, and (b) the
frozen counter's citation leg rejects any `path.ext:NNN` outside the pinned snapshots, so 17 of 18 real reports are
unbound for credit although their file verdicts are 17 `holds` / 1 `partly`. Both causes are in
`.ufo/waves/round-49/after/c1-final.json` (`per_row[*].blocking`, `seat_notes`).

## Sources & frontier

Counting command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tsukuroi`
— **exit 0 at round start** (`.ufo/waves/round-49/before/sources-census-start.txt`) and **exit 0 at round end**
(`.ufo/waves/round-49/after/sources-census-end.txt`). Registry rows: **255 before → 255 after**; rows added by
tier: **none** (0 A, 0 B, 0 C); rows touched old→new: **S255 `used-by`** `corpus/lessons/round-48.md` →
`corpus/lessons/round-48.md, corpus/lessons/round-49.md`; every other row unchanged. Rows opened this round: S246,
S247, S248, S243, S240, S249 (live re-open by seats, byte-identical to their pins), S251 (re-opened; unchanged),
S255 (re-opened by the L1, sha256 `78d0eefb…` identical). Gate sample (admit and reject): **admit** the mktemp(1)
page as a duplicate of S252 for the narrow question it names, and the POSIX Issue 8 word-expansion section
reconfirmed as S253; **reject** the community Q&A (S254, tier C, glosses quoting, cites superseded Issue 6).
**Refused source:** `proc_pid_fd(5)` was opened and refused as the source for `/proc/self/fd/<n>/<child>` traversal
— it documents the symlink and the `type:[inode]` text and nowhere states a child path component, so that mechanism
stays `[inference]` (`R49ScoutProcFd`, `corpus/lessons/round-49.md` Gate).

Frontier rows advanced: **none**. C2 changes how ownership is cited, not who owns what (ADJ-06's kaidoku/revenger
arbitration stays with the integrator); C3 is a diagnostic inside the existing census surface. New carried debt:
the fd-alias traversal's sourcing, and the anchor drift table `R49CritAdjB` produced.
`Assimilation: none` — the staged `merge/tsukuroi` package still collides with the lane registry (53 → 56 collisions,
0 same-document) and this round's claims needed no new entry; nothing was appended from it. `considerthese/`: one
proposal mined by `R49ScoutConsider`; no QUALITY criterion landed from it this round.

## Trend verdicts

- **expansion — unchanged.** No knowledge entry admitted, no new registry row, no Frontier ground moved.
- **quality — improved.** C2 and C3 measured PASS against frozen predicates with base receipts; the GR rows were
  re-read `holds` 6/6 (GR1, GR3) by an 18-seat cohort where round 48 could bind none; the round's own HIGH regression
  was found by a seat, fixed, and re-verified by the predecessor counter.
- **discernment — improved.** The cohort caught a real overreach the author had just written (GR2's `[inference]`
  mark), three seats demonstrated the frozen C1/C2/C3 counters can be forged or stubbed past, and the calibration
  table restates to zero mismatches at the final revision.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md:4548-4572` adds
  the round-49 scrub-cohort section (hashes, cohort, the named GR2 defect, the counter's forgery limit) and the
  census descriptor-band section; every claim there points at `corpus/lessons/round-49.md`,
  `.ufo/waves/round-49/{frozen,after}/` or `tools/check-*.py`. Non-author verification of the whole SKILL remains
  owed.
- [~] At least one end-to-end domain task executed and logged in LOG.md — the round's measured outcome block in
  `LOG.md` (round 49) drives the three counters from base receipts to final receipts, and the C3 path was executed
  end to end (`07329036` fix → `823425c5` PASS → predecessor counter PASS). Author-side evidence only.
- [~] Instructions executable by an agent without oral context — `.ufo/waves/round-49/frozen/FROZEN.md` plus the
  wave `context` carried every path, hash and binding format; 73 seats produced 73 reports with no oral handoff
  (`.ufo/waves/round-49/w1-results.json`). The no-oral-context retest of the whole SKILL remains unexecuted.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` ADJ-01..07 keep their boundaries; the
  round-49 note under `## Round 49 — the ownership-source column now cites portable anchors` states that the change
  is a locator repair, grants no write authority, and leaves the kaidoku/revenger arbitration open; `R49CritAdjB`
  reports sibling drift without repairing a sibling file.

## Stale-lane

Respawn-per-round driver; no other mission of this lane is open. No tool installs this round (`pacman` pause
respected). Fleet-root strays `o.bin`, `oldrep1.out`, `oldrep2.out` predate this round (2026-10-27/28 morning,
round 47/48 artifacts) and were left untouched; no round-49 seat misrooted a file into the fleet root.
