# kasegi — round 35 report (2026-10-26)

Lane: `kasegi-shokunin` (bounty & security research; axes depth + coverage). Lane base `3266c9937b03062d9bbc2f436e20820115ed179c`; claims-freeze `617496b9c6e92bc671e7e78b83df69a04470d0e9`; wave-1 spec/dispatch `da2d3c687f82a9814ee71c91c930cb733050d37c`; L1 integration D4/D6/D7 `aa6ad99bb90c4fe30dc5c326adf2f82d8ec84b1b`; final lane commit `0aee0ef105395a2f1d6ace7eaeef13871bb26988` (pushed; `ls-remote origin refs/heads/master` prints it). Stale-lane: respawn-per-round driver; no other mission of this lane open.

## Work performed

The round declares **two claims**, frozen before dispatch in `.ufo/waves/round-35/claims.json` (sha256 `fe0dae8957c38f9c697b1b851a528bdf516f949f6ee3ba1ca2846e61d1ea2982`):

- **C1 — depth:verifiability (score 4, held):** the seven round-34 verifier-routed defects D1–D7 land with runnable closure checks: `corpus/instruments/r35-defect-closure.sh` prints `closed=7/7 exit=0` and `--selftest` prints `cases=7 failures=0`; SCORECARD.md `filled by the L1` count 0 with an appended correction naming `c1c6a5f`; an appended round-34 depth:density-row erratum naming the corrected mean 201.2; SKILL.md Gates & probes registry registers `r-defect-closure.sh` + `kill-rule-check.py`; `wave1-results.json` tracked with a provenance note beside it; `claims-erratum-d5.md` carries the discriminating-invocation and per-id occurrences statements; `L1Integration.md` stale dead-seat sentence corrected; QUALITY supersedes-R22/R23 rows present.
- **C2 — coverage (score 7, held):** Frontier F18 admitted 17 → 18 (CISA Known Exploited Vulnerabilities catalog — exploitation-status-based prioritization distinct from CVSS severity; row S052, registry 51 → 52, opened 2026-10-26), one knowledge entry citing `source: S052`, harness `entries=21 pass=21 exit=0` incl. `PASS F18 ids=S052`, source-recheck S052 exit 0, census exit 0 (W04 S028/S029 only).

**Wave.** One v2 wave `kasegi-r35-build`, 64 seats (`spawn 64 / resume 0`), dispatched via the inline spawn handoff (`wave1.ready` → `wave1.ready.dispatched`): executor 18, scribe 12, reviewer 10, scout 6, mutation-tester 5, critic 5, connector 4, sentinel 2, simplifier 2 — attack share 20/64 = 31.2 %; m_flash roles 39/64 = 60.9 %. Receipts under `.ufo/waves/round-35/wave1/`; planner seat = L1 (orchestrator ruling 2026-10-19), its data-walk rode `ScoutDatawalk`. No dead seat observed at wrap; the dispatcher's `wave1-results.json` finalizes after the wave settles (seat-level receipts are the cited evidence).

**Work items by area** (evidence under `.ufo/waves/round-35/wave1/`):

- **C1 build** — `ExecClosureSuite` (r35-defect-closure.sh), `ExecSelftestFixtures` (r35-fixtures/ D1–D7 + clean + two-defect), `ExecD1Markers`, `ExecD2DensityRow`, `ExecD3SkillRegistry`, `ExecD4ResultsTrack`, `ScribeErratumD5`, `ScribeQualityDraft` (D7 block).
- **C1 attack/review** — `RevClosureSuite`, `RevSelftestFixtures`, `RevD1D2`, `RevD3D4`, `RevD5D6D7`, `MutFixturesLimbs`, `CritC1Kill` (16 clause mutants, gaps F-1…F-5 recorded), `ExecBeforeReceipts` (all before-controls MATCH on the freeze export), `ExecDoNothingReject`.
- **C2 build** — `ExecC2Capture` (feed capture + manifest), `ScribeEntryF18` (entry), `ScribeSOURCESRow` + `ExecRegistryAppend` (S052 row, search-log bullet, R8 lines), `ExecExpectedListSync` (knowledge-expected 47), `ExecCensusAfter`, `ExecScoreGap` (considerthese proposal 2).
- **C2 attack/review** — `ScoutKEVLive` (live re-open 0 differing lines; BOD 22-01 revocation finding), `ScoutSiblingSweep` + `ConnSibling` (20/20, no contested scope), `RevEntryF18` (REFUSE→repair→ADMIT), `RevRowS052`, `RevC1BeforeAfter`/`RevC2BeforeAfter`, `MutC2Entry`, `MutJunkTwin`, `MutCounterBase`, `CritC2Kill`, `CritOverclaim`.
- **Non-claim frontier items** — assimilation: `ExecIdCollisions`, `ExecQuarantineSlice` + `ScoutQuarantine`, `ScoutPackageThemes`, `ScribeGateAssimilation`; mistakes: `ScribeMistakesDraft`; scope/credential: `SentCred`, `SentScopeFinal`, `CritBoundary`, `SimplifierCleanup`, `SimplifierDocs`.

## Landed changes

Every change is tied to the round-35 `LOG.md` entry (heading `## Round 35`; appended in `0aee0ef`) and to the commits:

| Change | Commit |
|---|---|
| Claims freeze (`claims.json`, `census-before.txt`, `c1-controls/`, `c2-controls/`) | `617496b9` |
| Wave spec/dispatch (`build-spec.py`, `wave1-spec.json`, `wave1-dispatch.json`, `wave1.ready`) | `da2d3c68` |
| C1 counter `corpus/instruments/r35-defect-closure.sh` + `corpus/instruments/r35-fixtures/` | `0aee0ef` |
| D1/D2: SCORECARD placeholder substitution + appended round-34 depth:density erratum | `0aee0ef` |
| D3: SKILL.md `## Round-35 Gates & probes registry addition` | `0aee0ef` |
| D4: `.ufo/waves/round-34/wave1-results.json` + `.provenance.md` | `aa6ad99` |
| D5: `.ufo/waves/round-35/claims-erratum-d5.md` | `0aee0ef` |
| D6/D7: `L1Integration.md` correction; QUALITY Round-35 supersession (R26/R27) | `aa6ad99` |
| C2: `corpus/knowledge/cisa-kev-catalog.md`, `corpus/SOURCES.md` S052 row + search-log bullet + R8 lines, `corpus/README.md` F18 row, `corpus/source-snapshots/round-35/{S052.txt,manifest.json}`, `knowledge-expected.txt` 47 | `0aee0ef` |
| Round close: SCORECARD round-35 section, SHONEN.md, `corpus/lessons/round-35.md`, LOG.md entry, wave receipts, assimilation artifacts | `0aee0ef` |

## Before → after measurements

### C1 — depth:verifiability, seven defects

| defect | before (freeze, `c1-controls/before.txt`) | after (landed bytes) |
|---|---|---|
| D1 placeholder | `filled by the L1` = 1; `c1c6a5f` = 0 | `filled by the L1` = 0; `c1c6a5f` = 3; `<LANE_HASH>` 0 |
| D2 stale density row | `201.7` = 2; `201.2` = 0 | appended erratum names 201.2 (`201.2` ×2); stale row bytes untouched (`row-bytes=1`) |
| D3 gates unregistered | `r-defect-closure` = 0, `kill-rule-check` = 0 | 4 and 4 (registry rows, SKILL.md +13/0) |
| D4 results after `complete` | tracked = 0; provenance note = 0 | tracked = 1 (`git ls-files` → 1); note 5639 B beside it |
| D5 predicate wording | `claims-erratum-d5.md` absent | present; `discriminating invocation` ×5, `per-id occurrences` ×5 |
| D6 stale dead-seat sentence | `did not file a receipt (dead seat` = 1 | 0; `Correction (round 35)` present |
| D7 QUALITY grounding | `supersedes R22` = 0, `supersedes R23` = 0 | 1 and 1 (R26/R27 rows) |

Suite readings: `bash corpus/instruments/r35-defect-closure.sh` → `closed=7/7 exit=0`; `--selftest` → `selftest cases=7 failures=0` exit 0; base export (`git archive 3266c993`) → `closed=0/7 exit=1`; forged summaries rejected 4/4 (`judge=fake-suite rejected=1`, `judge=fake-plain rejected=1`, `judge=short-report rejected=1`, `judge=complete-report accepted=1`). Do-nothing controls: `c1-controls/fake-suite.sh` prints `closed=7/7` while checking nothing — rejected by the selftest discriminator; `c2-controls/junk-f18.md` fabricated quotes pinned against the capture print `MISMATCH reason=quote-not-found` exit 1, and the twin is nowhere admitted (harness counts 21, not 22). Other instruments: `recheck-audit.py --quiet` → `lines=47 total=47 pass=47 fail-closed=24 parse_fail=0 cwd_fail=0 paths_fail=0 exit=0` and `expect=present expected=47 missing=0 unexpected=0 exit=0`; `anchorcheck.py SKILL.md` → 0 bad, `LOST-RECORDED=306`, `PIN-BROKEN=0`, exit 0.

### C2 — coverage, F18 / S052

| counter (frozen command) | before | after |
|---|---|---|
| `grep -cE '^\| F[0-9]+ \|' corpus/README.md` | 17 | **18** (F18 at `corpus/README.md:388`) |
| `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` | 51 | **52** (S052 at `:58`; rows=52 malformed=0) |
| `grep -cE '^\|[[:space:]]*S052[[:space:]]*\|' corpus/SOURCES.md` | 0 | **1** |
| `grep -lE '^source: S052 ' corpus/knowledge/*.md \| wc -l` | 0 | **1** |
| `python3 corpus/instruments/frontier-recheck-count.py` | `entries=20 pass=20 exit=0` | **`entries=21 pass=21 exit=0`** incl. `PASS F18 knowledge/cisa-kev-catalog.md ids=S052 exit=0` |
| `python3 corpus/instruments/source-recheck.py --manifest corpus/source-snapshots/round-35/manifest.json --source S052` | manifest UNAVAILABLE, exit 2 | all five assertions `occurrences=1`, `sha256 OK`, exit 0 |
| `scripts/sources-census.sh validate --root … kasegi` | exit 0, W04 S028/S029 | exit 0, W04 S028/S029 |
| `ls corpus/knowledge/*.md \| wc -l` | 46 | **47** |

Capture: `corpus/source-snapshots/round-35/S052.txt` — 200, 1479694 B, 27870 lines, sha256 `d69349e86c5cce17146ccb4a4d514272d5ef47cb9586d06085113cf6779e8826`, `fetched_utc 2026-10-26T06:32:40Z`, request URL = final URL `https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json` (the root `.json` URL 404s — recorded in the search log); manifest `06bfcc71e6df494b0b54f489077b6bf747aeb4294f412e4deae64a2ac747f6ee`; parsed shape `count=1756`, `catalogVersion 2026.10.23`, 12 per-record keys, `cvss` 0 occurrences. Live re-open: 0 differing lines, same sha256; every quote exactly-once.

## Sources & frontier

`corpus/SOURCES.md` before → after: **51 → 52 rows**. Rows added by tier: **1 × A** (S052 — CISA KEV JSON feed, kind dataset, tier A scoped to CISA's own catalog statements, status mined, opened 2026-10-26, recheck 90d, used-by `corpus/knowledge/cisa-kev-catalog.md`, anchor pinned to the round-35 capture). Tier histogram after: A 49 / B 1 / C 2. Rows touched old→new: none — no status/recheck/used-by cell changed on any pre-existing row (S001–S051 untouched, logged). Frontier rows advanced: **F17 → F18** (`corpus/README.md:388`). Search log: round-35 bullet at `corpus/SOURCES.md:79` plus two R8 corrections (`:111` supersession note toward the wider `ScribeSearchLog.md` §5 draft; `:112` scope correction for the `KEV 0` pre-state sweep — the token pre-existed at `corpus/lessons/round-22.md:91`). Census before → after: both exit 0, W04 S028/S029 only. Sourced claim: C2 rests on S052 opened this round. Assimilation: **none adopted** (id collisions 22 post-C2; quarantine slice 7 rows: 4 present-and-located incl. S068 duplicate of S040, 2 prose-class-unverifiable, 1 unreachable, 0 adopted; standing refusals flips unmet). `Assimilation: none` — reasons in the lesson Gate.

## Trend verdicts

- **expansion: improved** — one admitted knowledge entry on ground the coverage map did not hold (exploitation-status prioritization vs severity/ladder ground S001/S002/S046/S047/S043/S044/S049/S050/S051), frontier 17→18, registry 51→52 at tier A, entry cites mined `source: S052`, harness 21/21. No new capability row (capability window not restarted; last entry round 33).
- **quality: improved** — seven routed defects closed with a fail-closed counter (base 0/7 → 7/7, selftest 7/7 with clean/two-defect controls and four forged reports rejected); `recheck-audit` strict pass=47/47, expect=present 47/47; anchorcheck 0 bad; no admitted entry failed its re-check (S052 re-opened live, byte-identical).
- **discernment: improved** — the gate refused correctly (RevEntryF18 Q2 REFUSE → repaired to ADMIT; assimilation adopted nothing while producing four located anchors and two description-class refusals; S068 recognized as an existing-row duplicate; S069/S070 policy-scoped verdicts; junk twin rejected by the counter it was built to fool; score distance reported instead of a move: `gap: 24 of 47 rechecks still gated on a lost base; score 5 needs 0 gated unsupported claims`). Recorded gaps: `CritC1Kill` shows suite clauses are file-wide literal greps (negation/mention satisfies D2/D3/D7) and nothing pins the counter's own bytes.

## SHONEN

- [~] SKILL.md decision tables/error patterns/checklists/cited sources — round-35 registry rows (D3), anchorcheck 0 bad, density ≈ 201.2 held (`SHONEN.md:5-11`).
- [~] End-to-end domain task executed and logged — none new; closest executed measurement: KEV capture + source-recheck + C1 suite (`SHONEN.md:21-27`).
- [~] Instructions executable without oral context — recheck-audit 47/47 + r35 suite 7/7; all rechecks `bash -n`-clean, cwd-invariant (`SHONEN.md:34-40`).
- [~] No cross-domain bleed — PROVINCE untouched; sibling sweep 20/20 no contested scope (`SHONEN.md:54-60`).

**Tooling:** no installs or upgrades; no pacman transactions (host-wide pause). **Open L0:** kasegi round-15 (PROVINCE re-point), round-16 (second root loss), round-32 (re-dispatch vs L1-only landing ruling) remain open; none blocks this round.

---

**Erratum (appended after filing):** the final lane commit is `8ce6fb4f2a33a6e1fb0963021905fb20dd58cc05` (a D1 closure fix: the SCORECARD round-35 block's closing-commit sentence used the literal `filled by the L1`, re-opening D1; reworded to name the integration commit — `r35-defect-closure.sh` re-reads `closed=7/7 exit=0`). The earlier cited `0aee0ef` remains an ancestor.

**Erratum 2 (appended after filing):** final lane commit is `5a253372d7ccda2fd7829932489481218c3b0efb` — wave leftovers committed (S052 capture named file, SKILL.md registry, control fixtures, ready markers, receipts); export replay of HEAD now reads `closed=7/7 exit=0` and `source-recheck S052` exit 0. Earlier cited 8ce6fb4f remains an ancestor.
