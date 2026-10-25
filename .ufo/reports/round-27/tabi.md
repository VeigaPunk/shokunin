# tabi — round 27 report (hyaku run 7)

## Work performed

This was an attempted resumption of round 26's three frozen claims, with the frozen-text drift discovered and disclosed rather than repaired after data. Baseline lane tip: `f185b4e7ab10cd9e8925e8ec614c9c111772357d`; final lane tip: `ef8aa4a3256cc6462a60d850d7ea21277aecd2a1`.

- **C1 calibration — failed.** The extended counter's final output is `mismatches=0`, but it falsely clears the real stale tally at `LOG.md:221` (claimed 8, measured oracle 12) from an unrelated 183-line paragraph that does not cite line 221. The frozen rule requires a correction citing the superseded line. The `m1` citation matcher accepts any `:N`, paragraph grouping merges adjacent correction bullets, and ambient fractions can satisfy the oracle. Do not accept the zero or alter the frozen claim after scoring. Evidence: `.ufo/waves/round-27/w1/CritC1Supersession.md`, `ExecC1Attacks.md`, `w2/RevFrozenFit.md`, `w2/MutC1Log.md`.
- **C2 depth — counter passes; inherited claim conformance is not established.** The corrected S106 gate returns `valid=true`, all fields true, and selftest 5/5. A missing receipt now yields could-not-evaluate/exit 2. However, the round-27 claim text dropped inherited fetch-failure and measurement-revision binding conditions; the receipt has no revision field, so that inherited requirement is unproved. The original gate defect was corrected at `5198e28` and the empty-fixture selftest fixed at `5ed6484`; these implementation changes do not rewrite the inherited claim.
- **C3 coverage — counter passes; frozen-text drift disclosed.** One entry cites S107; census is clean. The round-27 claim record differs from the inherited record. The 38-row quarantine slice was hand-checked: 35 absent/refuse, S171 unverifiable after 404, S114 and S140 present but not appended because frozen C3 admits only S107. The present-row/frozen-claim conflict is routed in L0 question `tabi | round-27`.

## Landed changes

Lane commits (all pushed through `jj-lane.sh`): C1 `fd722a7`; C2 gate `5577d1b`; C3 entry + S107 row `6ca3b89`; gate registry `ef7a274`, `024d60c`, `5a0178c`; initial wave evidence `8e07f0b`; records `336d5d1`; C2 corrections `5198e28`, `5ed6484`; integrated wave-2 evidence and accuracy corrections `bceb17d`; final quarantine, claim-drift and lesson dispositions `ef8aa4a3256cc6462a60d850d7ea21277aecd2a1`.

Other landed work: QUALITY criteria 67–68, the lane-local `scripts/report-contract.mjs`, corrected RFC 9110 entry/row wording, LOG and SCORECARD dispositions, and W1/W2/quarantine receipts. `claims.json` was not rewritten after data. The quarantine hand-check reports are under `.ufo/waves/round-27/quarantine/`.

## Before → after measurements

| Measure | Before | After / result |
|---|---|---|
| C1 `node scripts/check-selfassessment.mjs --rev <REV> --json` | At counter baseline `4ad4c77`: `mismatches=6` (five LOG-window findings plus live-tree m3); at round-27 baseline `f185b4e`: 5 | Final tip `ef8aa4a`: `mismatches=0`, `clean=true`, `counted=[]`, `couldNotEvaluate=92`, `superseded=10`. This numerical result is **invalid as claim evidence**: `LOG.md:221` is marked superseded without a citation to that line. Selftest: 13 → 17 (`node scripts/check-selfassessment.mjs --selftest`). |
| C2 `node scripts/check-s106-evidence.mjs --rev <REV> --json` | 0 gate at inherited pre-gate baseline; S106 bytes/receipt already committed at round-26 tip | Final tip `ef8aa4a`: `valid=true`; `sha_match`, `anchor_located`, `anchor_unique`, `byte_count_match` all true; decoded bytes 73,952; anchor line 187. Selftest 5/5. Inherited revision-binding requirement remains unverified. |
| C3 `git grep -lE '^source: S107 ' <REV> -- corpus/knowledge \| wc -l` | 0 at `f185b4e` | 1 at final tip; `SOURCES.md` registry 106 → 107 rows; `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tabi` → exit 0 (`tabi ok`, 16 pre-existing W04 warnings). |
| Gate registry | — | `node scripts/check-gate-registry.mjs --rev ef8aa4a3256cc6462a60d850d7ea21277aecd2a1 --json` → `nonconformant=0`, `clean=true`. |

Final claim measurements were run after the lane tree was clean. C1's apparent zero is still a false clear under the frozen predicate, not a calibration success.

## Sources & frontier

**S107 admitted:** HTTP Semantics, RFC 9110, https://www.rfc-editor.org/rfc/rfc9110.txt — accessed 2026-10-25, HTTP 200, 502,941 bytes, SHA-256 `21c1cdce…47232a`; committed bytes at `.ufo/waves/round-27/assimilation/rfc9110.txt`. Located quote, §10.2.3 lines 4805–4807: “Retry-After indicates the minimum time that the user agent is asked to wait before issuing the redirected request.” The admitted entry distinguishes 303 GET/HEAD retrieval, 301/302 POST→GET possibility, 307 MUST-NOT, and 308 as an inference supported by RFC 9110's historical note at 7260–7264; §15.4.9 does not repeat a status-specific normative MUST-NOT. No live browser redirect was run this round. Existing loopback evidence already records the 302→303→307 chain and 303→GET / 307 method-body preservation; real-site redirects remain untested.

Staged S124 was transformed to fleet schema; staged S125 and S142 were refused as rows with measured census/gate reasons in `corpus/lessons/round-27.md`. Quarantine results: 35 rows' recorded quotes were absent; S171 is unreachable/unverifiable (HTTP 404, not fabrication); S114 and S140 had present source text but were not appended because the frozen C3 claim admits only S107. The unresolved present-row rule conflict is in the L0 question. `considerthese/` is absent. RFC 9110 is shared by kake/mori/chousa; that source adjacency was reported, not absorbed. The report-contract tool remains lane-local.

## Trend verdicts

Axes at round start: depth 8, coverage 9, operability 8, freshness 8, calibration 9, adjacency 8. Lowest non-retired tie: depth/operability/freshness/adjacency at 8; intended C2 target depth. Saturation 8 / window 3; stagnation nudge inactive; no axis retired. No scalar axis score moved. C1 failed and calibration receives no claim credit; C2 and C3 counters pass but inherited claim-record drift prevents claiming compliant resumption. The new source vocabulary is a narrow documentation extension, not new runtime evidence. No capability promotion; evidence gates remain counters.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources
  `SKILL.md` §Approval table (`:697`), §Evidence ladder, §Runbook, `:1598-1617` kaika decision rows; prior `[x]` named lane-dispatched TABI-B4/TABI-R3-4 — not non-author (orchestrator ruling, kaika round 1)
- [~] At least one end-to-end domain task executed and logged in LOG.md
  `corpus/knowledge/multi-step-journey.md` §1–§2, §7 (4-page loopback journey, 2 cold runs byte-identical); logged in `LOG.md` round-3 entry
- [~] Instructions executable by an agent without oral context
  `corpus/knowledge/executor-test-sufficiency.md` §0, §4 (verdict SUFFICIENT; the executor was a lane-dispatched seat)
- [~] No cross-domain bleed (PROVINCE.md still accurate)
  `PROVINCE.md:3-19`; refusal routes revenger/kaidoku/kake/kagi held (`corpus/evidence/user-20261015-r02/boundary/refusal-receipt.txt`)

## Stale-lane

Respawn-per-round driver; round 27 is the only open tabi mission.

## Open items

- Keep C1's failed predicate intact; repair the matcher only under a new, pre-scored claim.
- Resolve the L0 question about S114/S140 quarantine-present rows versus frozen C3 scope.
- C2's inherited measurement-revision binding and source-content pinning remain unverified; no post-data claim rewrite was made.
- One W2 seat (`ScribeClaimRecordAudit`) completed without producing its assigned report. No seat was reported dead; W1 32/32 reports, W2 35/36 reports, residual audit 4/4 reports.

## Tool installs

None. Tooling rules were read; no tools were installed or upgraded. All pacman transactions remain paused.