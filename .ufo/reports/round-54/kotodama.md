# kotodama — round 54 report (hyaku phase 3, attempt 2, L1 KotodamaR54a2)

Lane repo `/home/vgpnk/Projects/shokunin/kotodama-shokunin`. The lane tip after landing is `e17bc2bc14168e16873580c52d03e9ec1d462e67` (jj-lane helper `landed`). The claim base is `260c68d`, the declaration is `7fa37fb` and the original base `e0bfb13e` is unchanged. The scope freeze arrived at 18:41Z and this report was filed at about 19:04Z.

## Work performed

**Declared claims (1): C — coverage.** C is a learning claim and the round's sourced claim. It adds one new culture-material entry, `corpus/knowledge/culture-material/masks-masquerade.md`, on masks and masquerade as worn object, embodied presence and licensed voice. Knowledge files go from 229 to 230. Acceptance is `python3 -B reports/round-54/accept-c.py` (seven legs). No second claim was declared (`reports/round-54/claims.json` `single_claim_note`). The drift sentinel asked for a different frontier area, so the round worked culture-material ground instead of the linguistics surface of rounds 52–53. Critic note (`.ufo/waves/round-54/build-a2/CriticSingleClaim.md`): round 51's D was also culture-material, and C keeps the round-53 claim shape, so the area differs by partition and topic, not by claim form.

- **Inherited attempt-1 input, re-verified.**
  - Pushed commits reused:
    - `d761ee8`: prerequisite with the round-53 routed fixes. It is not a claim.
    - `4b2299b` and `260c68d`: claim instruments.
    - `1ec84db` and `7fa37fb`: declaration, criterion-11 controls receipt and dry run.
  - Re-verification:
    - ExecDryRunCensus: 12/12 commands match the declaration (`.ufo/waves/round-54/build-a2/ExecDryRunCensus.md`).
    - ExecControlsReplay: the criterion-11 receipt replays byte-identical (sha256 `7e006e22…`), 13/13 controls, and all five instrument hashes match (`.ufo/waves/round-54/build-a2/ExecControlsReplay.md`).
- **Inherited untracked leftovers (5), all committed as dead-wave evidence at `5757c45`:** `.ufo/waves/round-54/build-dispatch.json`, `build-sent-payload.json`, `build-spec.json`, `build/swarm-registry.json` and `gen-build-spec.py`.
  - These are the records of attempt 1's 36-seat build wave. Its seats died in the omp restart at 17:26Z with no reports.
  - `gen-build-spec.py` was adapted in place for attempt 2 before that commit, so the committed bytes are the attempt-2 generator. Attempt 1's generator survives only as its JSON output (`build-spec.json`).
  - Reverted: none.
  - Attempt-1 seat scratch (`/fast/scratch/hyaku/kotodama-r54/`, 8082 files) was not used as evidence (`.ufo/waves/round-54/build-a2/ScribeInheritedState.md`).
- **Build wave `kotodama-r54-a2-build`, 42 seats.** It was validated under policy v1 and dispatched as one `task` call at 18:34Z. The seat-slot grant came after a wait at the 85-seat cap. Evidence: the spec, dispatch and sent payload in `.ufo/waves/round-54/build-a2-*.json`, committed in `5757c45`.
  - 24 source scouts opened 70+ candidate sources by ordinary means.
  - Connectors mapped 132 in-lane hits and 20 sibling lanes; no sibling owns a mask method.
  - Critics and reviewers attacked the gap premise, the restricted traditions, the entry contract, the routed fixes and the Gate splits.
  - 4 executors built the Gate-quote checker and re-verified the inherited state.
  - 2 scribes drafted the inherited-state section and the spot-check routing.
- **Entry integration (L1).** 153 lines. It cites 46 rows, S239 and above, each opened this round. Draft ids were mapped to S-ids in order of first citation (`/fast/scratch/hyaku/kotodama-r54-a2/idmap.tsv`); `tools/check-draft-ids.py` reports 0 findings. §2 points one-way to 12 owners, and restricted traditions are handled only through community statements (§4).
- **Residual falsify call, 8 seats** (7 reviewer, 1 critic), payload `.ufo/waves/round-54/residual-sent-payload.json`, reports in `.ufo/waves/round-54/residual/`.
  - CriticClaimC: the mechanical legs hold. Four review-clause failures were found: Kòmò construction detail, a Phillips over-read, two one-case generalisations and a boundary-cell over-read.
  - Row reviewers (all 6 slices): 85 of 102 checked citing items CARRIED, 9 WRONG-LOCATOR, 8 OVER-READ.
  - All entry findings were fixed at `58b2fae`, and the late ReviewRows247to254 slice was fixed at `e17bc2b`. Carried to round 55: the S256 vs S258 tier harmonisation, which needs a superseding row, and the S248 and S254 anchor-cell locators.
- **Frontier mistake fix:** `tools/check-gate-quotes.py` (R54-M1). It exits 1 on `corpus/lessons/round-53.md` with 12 findings and on round-52 with 7; it exits 0 on `round-54.md`. Mutation-tested by ReviewGateQuoteTool: 3 of 3 mutants killed, and 5 escape classes were recorded.

## Landed changes

All commits were landed by the jj-lane helper after remote verification.

| commit | what | LOG.md entry |
|---|---|---|
| `5757c45118771d8baac238b52aa5e95fc18cbd54` | attempt-1 dead-wave dispatch records; attempt-2 build-a2 spec, generator, dispatch and payload; census at attempt-2 start | round 54 (attempt 2) |
| `6a658ca4fe9230f70eaa3b421e6c9d78da5c1633` | claim C lands: entry, `corpus/README.md` (revision 2.11, row, 28→29, totals and footer), `corpus/SOURCES.md` rows S239–S284 | round 54, C |
| `58b2faed54b3a12dde3db0a6a3185b34e8b9e9a6` | residual falsify fixes (entry wording and locators; PNW cell; community-row tier notes) | round 54, C |
| `e17bc2bc14168e16873580c52d03e9ec1d462e67` | late-slice fixes (S251 section locator, S248 paragraph, S247 and S253 over-reads); lesson falsify row; lessons-index pin; slice report | round 54, C |
| `25375f1481f148a7b5295142f0b2795c53311315` | records: `corpus/lessons/round-54.md`, `corpus/lessons/README.md` (row and revision 11), `tools/check-gate-quotes.py`, SCORECARD, LOG, SHONEN line 6, `reports/round-54/telemetry/final-measures.txt`, build-a2 and residual wave reports | round 54 |

## Before → after measurements

- **C:** `python3 -B reports/round-54/accept-c.py`
  - Before, measured at `7fa37fb` (receipt `reports/round-54/telemetry/declaration-dry-run.txt`, re-run by ExecDryRunCensus): exit 1. SET FAIL (count 229), SWEEP FAIL (rows 229 files 229) and FLOOR FAIL (cited 0); RANGE, STATUS and USEDBY pass vacuously; ACCESS PASS.
  - After, measured at `58b2fae` and `25375f1` (`reports/round-54/telemetry/final-measures.txt`), and re-run by the L1 at `e17bc2b`: exit 0. SET PASS (count 230, added [masks-masquerade.md], removed []). SWEEP PASS (rows 230 files 230, missing 0). FLOOR PASS (cited 46). RANGE, STATUS and USEDBY PASS. ACCESS PASS (exit 0). The census at `e17bc2b` also exits 0.
  - Also exit 0 at `6a658ca`, re-run in a clone by CriticClaimC.
- Separability: `python3 -B tools/check-claim-separability.py reports/round-54/separability-manifest.json` → 0 findings, exit 0.

## Sources & frontier

- **Census at round start:** `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama` → exit 0 (9 W04 warnings on older rows; `reports/round-54/telemetry/census-start-a2.txt`).
- **Census at round end:** same command → exit 0, same 9 W04 warnings, `ok` (`reports/round-54/telemetry/final-measures.txt`).
- **Rows:** 238 → 284. S239–S284 were added, all `mined`, with `used-by` naming the masks entry. By tier: A 22, B 24, C 0. By kind: docs 19, paper 14, book 10, community 3. Status totals moved from 194/34/10 to 240/34/10 (mined/queued/rejected).
- **Rows touched old → new:** none before S239 changed in attempt 2. Within this round's rows, the scope notes of S254, S265 and S266 now mark the seat's tier-A note as superseded; the tier cells stay B. Prerequisite `d761ee8` (attempt 1) changed S145 mined → rejected, S185 queued → mined and S225's access note. All of this is logged in `corpus/lessons/round-54.md`, section *Status and used-by change log*.
- **Gate:** 46 lines, each with URL, access date and one ≤25-word located quote (`check-gate-quotes.py` → 0 findings).
- **Mined mistakes:**
  - R54-M1 is the Gate quote-cap class. Captured-by: none. Fix: `tools/check-gate-quotes.py`, shown able to fail.
  - R54-M2 is a literal `|` in a registry cell, caught before landing.
- **Sourced claim:** C cites S239–S284.
- **Frontier rows advanced:** masks and masquerade is now owned. Sources that were opened but not cited (Gule Wamkulu, Egungun, Talchum, Noh, Cham, Yup'ik, Parachicos and Oruro, Mexica, mummering) are listed in the lesson's Frontier.
- **Misroot sweep:** `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows no untracked file written by this round's seats. `live_s228.html`, `tf_bavelas.html` and `nama.html` were already present at round start, were not written by attempt-2 seats and were left untouched.

## Trend verdicts

- **expansion: improved.** One new owner for previously unowned ground (0 filename owners at base), 230 files, and 46 new mined rows.
- **quality: improved, bounded.** All seven acceptance legs pass. The residual reviewers found 17 locator or over-read defects in citing sentences and 4 review-clause failures; all were fixed at `58b2fae` and `e17bc2b`. Three registry-cell items are carried (S256 vs S258 tier, and the S248 and S254 anchors).
- **discernment: improved.** The Gate-quote checker turns an outside verifier's routed defect into a mechanical check that kills three mutants and caught 3 of this round's own draft Gate lines before filing. Restricted traditions follow only community statements, after the critic removed a Kòmò construction detail.

## SHONEN

- [~] SKILL.md decision tables, error patterns, checklists, cited sources — `SHONEN.md:6` corrected to 284 rows, 240/34/10 (`reports/round-54/telemetry/final-measures.txt`); no non-author verifier on record.
- [~] End-to-end domain task logged in LOG.md — `LOG.md`, round-54 entry (sources → entry → residual falsify → fixes `58b2fae`).
- [~] Instructions executable without oral context — seats worked from committed paths only (`.ufo/waves/round-54/residual/CriticClaimC.md`, re-run in a clone).
- [~] No cross-domain bleed — `.ufo/waves/round-54/build-a2/ConnectSiblingMasks.md`: 0 sibling mask-method owners, and canon stays with lore (entry §14).

## Round shape and seats

- **Shape:** default two-v1-wave plan, cut short by the scope freeze.
  - Wave 1 (build) ran with 42 seats: scout 26, critic 4, reviewer 4, executor 4, connector 2, scribe 2.
  - Wave 2 (falsify) was not dispatched; the freeze came before it was built.
  - The falsify step ran as one residual `task` call of 8 seats (reviewer 7, critic 1).
  - Round total: 50 seats.
- **§3 L2 floor:** met inside wave 1. The L1 holds the canonical planner seat; the planning data-walk rode ScoutEntryMechanics and ConnectInLaneMasks.
- **Dead seats:** none; no refusals or holds. Two build seats, ExecIntegrateRows and ScribeSpotcheckRouting, were still running at the report deadline. Their outputs are not integrated or cited, and no commit includes their reports. The L1 did the integration and the spot-check routing instead (lesson sections). `kotodama51-prereg-critic` stays excluded.
- **Tool installs:** none, by the L1 or any reporting seat; pacman pause respected.
- **Stale-lane:** respawn-per-round driver; no other mission of this lane is open.
- **Open L0 questions:** none new. The round-11 freshness question stays open.
