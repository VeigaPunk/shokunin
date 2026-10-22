# kotodama — round 52 (hyaku phase 3, attempt 1)

Lane HEAD (pushed): `2eb489fb954bfa448918223cf1c9bad622c694a5` on `main` (`jj-lane.sh state`: `ahead=0 behind=0`, local = remote). L1: KotodamaR52 (in-session, dispatched 2026-10-22T10:32:12Z). Author-side verdicts only; admission belongs to the non-author hyaku closure.

## Work performed

Declared claims (`reports/round-52/claims.json`, landed `d9f73c8`):
- **D — depth, repair-first:** the sign-language entry `corpus/knowledge/linguistics/sign-languages-manual-modality.md` has 0 lines that cite S094 (before 5). Routed defect 2 of `corpus/lessons/round-51-verifier-spotcheck.md`.
- **C — coverage, the learning claim and the sourced claim:** knowledge files 227 → 228 with one new entry, `corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md` (whistled, drummed and instrument-borne speech as conlang method), indexed in `corpus/README.md`, citing only rows S134 or above, each with the entry in its `used-by`.

Work items:
- Round-start census: `sources-census.sh validate … kotodama` → `ok`, exit 0, five W04 warnings (S127–S131), at 10:36Z.
- Prerequisite `147cfde`, a record and not a claim: QUALITY criterion 10 (sources are opened by ordinary means) and `tools/check-source-access.py`. The checker was shown able to fail before any registry change: `reports/round-52/telemetry/prereq-access-check.txt` gives 6 findings, exit 1. S094 status mined → rejected, used-by → `—`, with superseding row S132; it was re-opened by ordinary means at 10:38Z and returned `http=403 server=cloudflare cf-mitigated=challenge`. S133 supersedes S097's locator. The signed-language study path moved off S094.
- Declaration `d9f73c8`: `claims.json`, `separability-manifest.json`, `claims-agree.py` and `dry-run.py`, which runs every declared command and checks the receipt both ways. Receipt `reports/round-52/telemetry/declaration-dry-run.txt`: D 5, C 227, both acceptances exit 1 printing their before values, separability exit 2 naming the absent C land, agreement exit 0. The two-way check gives `MISSING_FROM_RECEIPT []`, exit 0; the same check exits 1 on round 51's receipt.
- Claim D, `dea5ece` with wording fixes in `5b7ecfb`:
  - Movement and orientation pairs re-cited to S096 (NAME/SHORT, CHAIR/NAME), re-opened by plain request.
  - The passive-hand set and the "45 handshapes" figure re-cited to S097 (seven shapes, Type-3 signs).
  - "Six shapes in Battison 1974" is now marked `(to-verify)`. OFFER/MAYBE and SHORT/TRAIN, which no openable page carries, were cut.
  - Attack: `.ufo/waves/round-52/build/ReviewDLines.md` passes all 5 lines. `CriticClaimD.md` led to two fixes, both landed. `ScoutBattisonRoute.md` tried 27 routes and found no ordinary-access copy of Battison 1974 or 1978.
- Claim C, `7cee23b`:
  - The entry has 195 lines and 12 numbered sections, no H3, a one-owner boundary table of 14 rows, DR-SRG-01 to DR-SRG-05, a NON-CANON example and a calibration bank. Its provenance gate reports `findings=0 blocked=0`.
  - It cites 49 new rows (S134–S183, with S178 rejected at integration as tertiary).
  - It was drafted from 11 section-scribe reports, integrated by the L1. One Springer monograph copy on archive.org was not cited.
  - `corpus/README.md` revision 2.9 adds the index row; the sweep reports 228 rows vs 228 files, exit 0.
- Frontier step:
  - Mistakes R52-M1 (access bypass), R52-M2 (stale lesson count) and R52-M3 (claim sizing repeated in C's acceptance argv) are in `corpus/lessons/round-52.md#mistakes`.
  - Gate lines for S132–S183 and a search-log note are in the same lesson. The lessons index revision 8 makes the c31 audit report `findings: 0`, exit 0.
- Criterion-10 hardening from the wave:
  - The bypass wording list was widened (`CriticAccessRegex.md` fix A: 30 of 30 probe phrasings caught, no new false positives on the lane).
  - Five killing controls were added for the mutants that survived (`MutateAccessChecker.md`: 12 of 17 killed before; selftest now 15/15).
  - Criterion 10 now states its limits (`ReviewCriterion10.md`).
- SHONEN self-assessment: `ReviewShonenScorecard.md` counted 2 mismatches with observed repo state (line 6, "131 opened rows"; line 8, "54 opened sources"). Both lines are corrected in `2eb489f`.

Round shape: the default v1 shape, but only the build wave ran.
- **Wave 1, build:** one `task` call of **35 seats**, validated under policy v1 (`.ufo/waves/round-52/build-spec.json`, `build-dispatch.json`). Roles: scribe 14, reviewer 7, critic 5, scout 4, executor 3, connector 1, mutation-tester 1. Attack seats: 13 of 35 (37%).
- **No wave 2 and no residual call.** The round total is **35 seats**.
- **Gate history:** the first gate request for 41 seats timed out after 3600 s (`wave-slot.sh` exit with `Command timed out after 3600 seconds`). A reshaped 35-seat request timed out after 1800 s: `timeout lane=kotodama wave=r52-build seats=35 live=56 pending=0 cap=85`. I then took an 8-seat residual grant, released it unused (its payload is in `.ufo/waves/round-52/residual-dispatch.json`, never dispatched) and was granted the 35-seat wave at `live=48`. The gate reservation was released after every seat returned or was cancelled.
- **Freeze:** Main froze scope at 12:32Z, so the falsify wave was not started.
- **Planner seat:** held by the L1. The validator rejects `planner`, and planning data-walks rode the scout and critic items.
- **Payload change:** a `solutionSpace` string per role was added to each task, because the `task` tool schema requires it. Nothing else in the validator payload changed.
- **Seats:** no seat died. 31 seats returned reports. Four section scribes (Sec02Boundary, Sec05Drummed, Sec10Decline, HeadScope) had not returned at integration (about 42 min) and were cancelled by the L1. Partial files from three of them remain in the wave folder, unused. Two seats that had already completed and been re-woken by peer messages were also cancelled. No seat is running.

## Landed changes

| commit | carries | LOG.md entry |
|---|---|---|
| `147cfde` | QUALITY criterion 10, `tools/check-source-access.py`, SOURCES S094 → rejected, S132, S133, study path, prereq receipt | 2026-10-22 Round 52, "Prerequisite" bullet |
| `d9f73c8` | `reports/round-52/{claims.json,separability-manifest.json,claims-agree.py,dry-run.py,telemetry/declaration-dry-run.txt}` | Round 52, "Trigger" bullet |
| `dea5ece`, `5b7ecfb` | claim D: sign-language entry lines 83, 87, 90, 92, 93 | Round 52, "D" bullet |
| `7cee23b` | claim C: the new entry, `corpus/README.md` revision 2.9, SOURCES S134–S183 | Round 52, "C" bullet |
| `2eb489f` | lesson round-52, lessons index revision 8, QUALITY criterion 10 wording, checker widening and controls, SCORECARD, LOG, SHONEN, `final-measures.txt`, `.ufo/waves/round-52/` | Round 52, "Wave" and "Evidence" bullets |

Lane changes since `2b956d7`: 58 files, +7612 / −16 (most of it wave evidence). The misroot sweep (`git -C /home/vgpnk/Projects/shokunin status --porcelain`) found no file written by this round's seats at the fleet root; the untracked `.ufo/waves/round-49/` holds another lane's round-49 seat output and was left alone.

## Before → after measurements

| claim | counting command | before (tree) | after (tree) | acceptance |
|---|---|---|---|---|
| D | `awk '/S094/{n++} END{print n+0}' corpus/knowledge/linguistics/sign-languages-manual-modality.md` | 5 (`147cfde`/`d9f73c8`) | 0 (`7cee23b`, lane `main`) | manifest argv → `S094_lines=0`, exit 0 |
| C | `find corpus/knowledge -name '*.md' \| wc -l` | 227 (`d9f73c8`) | 228 (`7cee23b`) | manifest argv → `knowledge_files=228`, `C_SID_BAD 0 [] cited 49`, exit 0 |

Both receipts: `reports/round-52/telemetry/final-measures.txt` (measured on `7cee23b` plus the then-uncommitted records, which carry no claim land). It contains:
- `SEPARABILITY: 0 findings`, exit 0, and `AGREE claims=['C', 'D']`;
- the two-way receipt check, `MISSING_FROM_RECEIPT []`, exit 0;
- the sweep run on its own: `footer_ok True`, exit 0;
- `git diff --name-status 147cfde 7cee23b -- corpus/knowledge`, which shows one added file and one modified file.

Disclosed defect R52-M3: C's statement says the entry is indexed in `corpus/README.md`, but its acceptance argv pipes the sweep into a `grep` that cannot fail on a missing README row. Build seats caught this before landing (`ExecCAcceptanceControls.md`, `CriticClaimSizingC.md`). The declaration was frozen and not changed. The wider clause is met when the sweep is run on its own, as above.

## Sources & frontier

- Census, round start: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama` → `kotodama ok`, exit 0, warnings W04 on S127–S131.
- Census, round end: the same command → `kotodama ok`, exit 0, W04 warnings only, on rows that re-open a superseded row's URL by design (S127–S133).
- Rows, counted with `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`: 131 → 183. Malformed rows: 0.
- Tiers after: A=106, B=69, C=8. Statuses after: mined 142, queued 33, rejected 8.
- Rows added, by tier: 52 rows, S132–S183. S132 (tier A, rejected) and S133 (tier B, queued) are prerequisite rows. S134–S183 are claim C's rows, with S178 rejected as tier C. Per-row tiers are in `corpus/SOURCES.md`.
- Rows touched, old → new: S094 `status` mined → rejected and `used-by` the sign entry → `—` (`147cfde`). No other existing row changed. All changes are logged in `corpus/lessons/round-52.md`, "Status and used-by change log".
- Frontier rows advanced: speech surrogates are now owned. Carried forward: the two sections that were not drafted, the phonetics §7 ownership wording, the checker's limits, and the `dry-run.py check` gaps (lesson `## Frontier`).
- Sourced claim: C cites S134–S183 (not S178), all opened this round by ordinary means.

## Trend verdicts

- **expansion: improved.** One admitted-candidate entry covers ground that had 0 filename owners and only one topic-line mention that is not an owner at `d9f73c8` (`ScoutGapSurrogate.md`). Its 49 cited rows are `mined` with the entry in `used-by`.
- **quality: improved.** D replaces five citations of a source no one can re-open with citations of pages a fresh session can open. A seat re-checked all five lines and they pass (`ReviewDLines.md`). Two over-reads were fixed (`5b7ecfb`). Limit: C's integrated text was not attacked after integration, because there was no falsify wave.
- **discernment: improved.** The round-51 outside disagreement (S094) is now QUALITY criterion 10 with a checker. The checker is shown able to fail, was mutation-tested and was widened after an adversarial probe. The SHONEN self-assessment was checked against repo state, and its 2 mismatches were fixed. Counter-evidence: R52-M3 repeats the routed claim-sizing class in C's acceptance argv. Seats caught it before landing, but the declaration was not repaired.

## SHONEN

- [~] SKILL.md has real decision tables, error patterns, checklists and cited sources. Evidence: `SHONEN.md:6`; registry 183 rows, census exit 0, `reports/round-52/telemetry/final-measures.txt`. No non-author verifier is on record.
- [~] At least one end-to-end domain task executed and logged. Evidence: the round-52 gap sweep → 49 opened sources → the speech-surrogate entry `7cee23b` → final receipt (`LOG.md`, round-52 entry). No non-author verifier is on record.
- [~] Instructions executable without oral context. Evidence: `SHONEN.md:10`; round-52 seats worked from committed paths and the declared commands only. No non-author verifier is on record.
- [~] No cross-domain bleed. Evidence: the C entry hands instruments to `music-instrument-lexicon.md`, sound production to audio-shokunin and canon to lore-shokunin (§12). The connector found 0 sibling owners (`.ufo/waves/round-52/build/ConnectSiblingSurrogate.md`). No non-author verifier is on record.

Stale-lane: respawn-per-round driver; no other mission of this lane is open.
Tool installs: none (no seat reported an install or update).
Open L0 questions: none filed this round. Main routed the operator question on headless-browser access in the round-51 closure. Criterion 10 settles it for this lane's own rows; the fleet ruling stays with the operator.
Held item: `kotodama51-prereg-critic` was not opened, retried, rephrased or reproduced.
