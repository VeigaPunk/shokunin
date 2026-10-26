# Kasegi round 40 (attempt 2)

## Work performed

Declared claims: **C1 — depth:verifiability (score 4, lowest non-retired axis, held)** — land the r40-closure.sh H1–H10 suite closing the round-39 verifier routed defects R1–R7 and the round-39 instrument attack findings (G2/G6); **C2 — coverage (7 → 8)** — decide the nine queued registry rows (S016/S017/S019/S020/S021/S022/S023/S024/S025), open S060+ rows, admit frontier F23 (CycloneDX analysis subtree).

Attempt 1 (KasegiR40) was force-stopped at the request budget after wave 1 settled 54/54 and J5 `3074c767` was committed; its receipt stayed uncommitted and wave 2 was never dispatched. Attempt 2 resumed: inherited and re-verified the wave-1 evidence, dispatched the rendered 35-seat falsify wave, integrated its findings, committed Y (J7 + receipt) and Z (closure blocks), and filed this report. Attempt-1 changes retained: freeze `5e985b7`; J2–J5 `bfca9ae`, `8717b8b`, `94abbff`, `3074c767`.

- **C1:** `corpus/instruments/r40-closure.sh` H1–H10 (suite+registry row, R2 corrections, R5 criterion, R6 Gate rows, H5 forgery rejection, H6 scratch-family scan, H7 receipt transcript, H8 negative controls, H9 declared blocks, H10 no-harm guard). At Y: `closed=10/10 exit=0`; graded `--selftest cases=10 failures=0`. Base `a7af2ce` and r39 judged head `8371e7a` exports are red (H8: base=3/10 exit 1, r39=2/10 exit 1). Receipt `.ufo/waves/round-40/final-gates/all-gates.txt` at Y is the teed transcript with `time-basis=ref-commit` — `run-utc` read from the ref commit, never wall-clock (M40-1 fix).
- **C2:** seven of the nine queued rows mined (S016/S017/S019/S020/S021/S023/S025) with entries citing each; S022 and S024 rejected with reason+flip in the round-40 lesson Gate, and restored in-row in `corpus/SOURCES.md` after wave 2 found the first integration had dropped the delivered teaches rewrite. New rows S060 (mined, ground F23), S061/S062 (rejected). Frontier F23 admitted (22 → 23). Harness `entries=26 pass=26 exit=0`; capture binding `records=54 bound=54 unbound=0`; census exit 0; measure 43/43 = 1.000.
- **Wave 2 falsification:** C1 green at Y, not at J before receipt: `closed=9/10 exit=1`, `selftest cases=10 failures=1` with H7 fail-closed, as the suite requires; at Y the receipt is byte-identical to the invocation transcript and forged/future-dated/different-ref/summary-only/tampered-H7 receipts reject. Routed to round 41 without changing frozen counter: H2 substring match accepts `closed=7/80`/`failures=10`; H3 accepts fenced M39-2; H6 misses case/separator, nested and dot-prefixed leftovers, and 4/8 H6 mutants; H9 symlink escape; H1 registry row that merely mentions the suite; H5 count-relative forgery and H7 payload-value mutant isolation; 7 kill-rule escape states. Full findings: `corpus/lessons/round-40.md` §Wave-2 falsification and `.ufo/waves/round-40/wave2/` (e.g. `RevC1Counters.md`, `RevC2Decisions.md`, `MutH6H10.md`, `CritKillRule.md`, `LabExportClean.md`).
- **Swarm:** two v1 waves. Build `kasegi-r40-build` 54 seats (executor 18, reviewer 12, scout 11, scribe 6, critic 3, mutation-tester 2, connector 1, sentinel 1); falsify `kasegi-r40-falsify` 35 seats (reviewer 12, scout 8, critic 7, mutation-tester 6, connector 1, sentinel 1) = **89 total** (64–128 band). Attack roles reviewer/critic/mutation-tester were 17/54 in wave 1 and 25/35 in wave 2 (42/89 overall). The L1 held the canonical planner seat (frozen topology; not a swarm role). Role routing per run-8 map; never passed `model`. Dead seats: 0 in both waves. Results: `.ufo/waves/round-40/kasegi-r40-build-results.json` and `kasegi-r40-falsify-results.json`.
- **Frontier step:** census before/after (below); mistake M40-1 mined (attempt-1 receipt: future-dated `run-utc`, forged 8/8 tally) with H5/H7 fix shown able to fail; C2 is sourced on S060+ opened this round (`corpus/knowledge/cyclonedx-analysis-subtree.md` cites S060).
- **Assimilation:** id-collision rerun (0–3-space extractor, read-only vs shokuknow): lane reg-ids 59, staged ids 94, `comm -12` = 29 collisions (28 true id collisions + S042 same-URL). Quarantine slice (7 kasegi rows of absent-defect-register): 2 payload-verified but quote-shape-defective (S037, S054), 1 document already held (S068 = lane S040), 1 payload-verified but refused on ground/Q3 (S065), 3 unreachable (S048 HTTP 404; S069/S070 0-byte body). **Adopted 0; adoptable 0; no renumber map filed.** Indented S002 proof: 0–3-space extractor reports 1 collision; column-zero-only reports 0.
- **considerthese:** 2026-10-26 proposal 2 (run one end-to-end domain task round) mined: a claim-package exemplar built from a public disclosed report and logged (SHONEN box 2 pointer).
- **Misroot sweep:** required `git -C /home/vgpnk/Projects/shokunin status --porcelain` before filing was empty; no seat files at fleet root. No copies/deletions.
- **Tooling:** no installs or updates; pacman not used (guard). No new L0 question; standing kasegi round-15/16 domain-root restoration/re-scope questions remain open.
- **Stale-lane:** progressing; attempt-2 commits Y through Z landed during this mission.

## Landed changes

- Claim freeze and controls: `5e985b74075dd3813a63d7750966bf8abf693465`.
- Wave-1 integration (C1 suite, C2 nine-row decisions, F23/S060+, frontier, lesson, corrections): `4766b9d`; J2–J5 append-only closure corrections: `bfca9ae`, `8717b8b`, `94abbff`, `3074c767`.
- Wave-2 results, reports, falsification lesson section, and restored S022/S024 teaches cells: `8040db9baaeedb1dc9632e76e27fc37ba0bd97ea`.
- Refreshed H9 whole-tail declarations for wave-2/lesson bytes (293 text declarations; all 293 verified against H9 tail hash + numstat + zero deletions; binary artifacts are excluded because the frozen H9 declaration schema hashes text tails): J7 `c7aea5ef97902f38289cbdc1cf267068876a62dd`.
- Y receipt only: `d0fe34d3fa27ff4de745a0c54c203fa8bf7141e5`; `git diff --name-only J7 Y` = `.ufo/waves/round-40/final-gates/all-gates.txt` alone.
- Per-claim scorecard rows, LOG.md r40 entry, and SHONEN r40 boxes/correction: Z `b01cbd50d514bb7f8e154b40e0e608be3e6cf217`.
- Final lane tip = **`b01cbd50d514bb7f8e154b40e0e608be3e6cf217`**, pushed and remote-verified.

## Before → after measurements

- **C1 — depth:verifiability, 4 → 4 (held; verified).** Before at base `a7af2ce` (`.ufo/waves/round-40/c1-controls/before.txt`): suite absent; R2/R5/R6 open; G2/G6 flaws standing; r39-l1 scratch leftover removed. At Y `d0fe34d`: `bash corpus/instruments/r40-closure.sh --export-ref d0fe34d3fa27ff4de745a0c54c203fa8bf7141e5 --work /fast/scratch/hyaku/r40gates/w --scratch-root /fast/scratch/hyaku/r40gates` → `closed=10/10 exit=0` (receipt transcript; H9 `declared=293,valid=293,tail=293,pure=1,paths=1,diff-read=ok`); `--selftest --export-ref d0fe34d…` → `selftest cases=10 failures=0` exit 0; base export → `closed=3/10 exit=1`; r39-head export → `closed=2/10 exit=1`; plain run refused exit 2. J7 `c7aea5e` was measured as receipt `export-ref` because a commit cannot contain its own hash; Y adds only the receipt.
- **C2 — coverage, 7 → 8 (verified).** Before at base (`.ufo/waves/round-40/c2-controls/before.txt`): queued 9, mined among nine 0, entries citing nine 0, S060+ 0, frontier 22, harness 25/25, registry 59, measure 42/51 = 0.824. After at Y `d0fe34d`: queued 0; mined among nine 7; entries citing nine 7; S060+ 3 (S060 mined, S061/S062 rejected); entries citing S060+ 1; frontier 23; harness `entries=26 pass=26 exit=0`; binding `records=54 bound=54 unbound=0`; census exit 0; measure 43/43 = 1.000. Commands re-run at Y: nine-row `awk` queued count → 0; same `awk` mined count → 7; `grep -rlE '^source: S0(16|17|19|20|21|22|23|24|25)' corpus/knowledge | wc -l` → 7; `grep -cE '^\|[[:space:]]*S06[0-9][[:space:]]*\|' corpus/SOURCES.md` → 3; `grep -rlE '^source: S06[0-9]' corpus/knowledge | wc -l` → 1; `grep -cE '^\| F[0-9]+ \|' corpus/README.md` → 23; `python3 corpus/instruments/frontier-recheck-count.py` → entries=26 pass=26 exit=0; `python3 corpus/instruments/capture-binding-check.py` → records=54 bound=54; `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kasegi` → exit 0.

## Sources & frontier

Census command (both runs): `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kasegi`.

Before (round-start `census-before.txt`), exit 0:
```text
kasegi  W04  S028 duplicate url docs.hackerone.com/en/articles/8494502-safe-harbor-overview-faq across scopes
kasegi  W04  S029 duplicate url eur-lex.europa.eu/eli/reg/2024/2847/oj/eng across scopes
kasegi  ok   /home/vgpnk/Projects/shokunin/kasegi-shokunin/corpus/SOURCES.md
exit=0
```
After (final run at Y), exit 0; output was the same three lines and exit code.

SOURCES rows **59 → 62**: added S060 (tier A, mined), S061/S062 (tier A/B, rejected); the nine decided rows' status cells changed (7 queued → mined, 2 queued → rejected) and seven mined rows' `used-by` changed from `—` to their entries; S022/S024 `teaches` cells were restored with rejected reason+flip after wave-2 caught the dropped writer output. Search-log bullet added. Frontier advanced: F23 (22 → 23) admitted; C2 entry cites opened/mined S060. Assimilation: **none adopted** (collision runs + quarantine verdicts recorded; staged package unchanged). Lesson `round-40.md` §Gate includes the new S060/S061/S062 URLs, access dates, located ≤25-word quotes and rejected flips; all status/recheck/used-by changes are logged there.

## Trend verdicts

- **expansion: improved** — F23 is the 23rd admitted frontier row; its entry cites opened/mined S060 (`corpus/README.md` F23 row, `corpus/knowledge/cyclonedx-analysis-subtree.md`).
- **quality: improved** — C1 closes the round-39 routed defects R1–R7 and G2/G6 instrument attacks; H5/H6/H7 and H9/H10 limbs have green runs and negative fixtures. Wave-2 survivors are explicitly routed to round 41, not concealed as closed.
- **discernment: unchanged** — all reviewers were dispatched by this lane and are not non-author verifiers; no outside spot-check completed this round (`corpus/lessons/round-40.md` Gate).

## SHONEN

- [~] Real decision tables, error patterns/checklists with cited sources — author assessment only; `SHONEN.md` round-40 box 1; no non-author verifier.
- [~] End-to-end domain task executed and logged — no live domain hunt ran (refused); closest work is the claim-package exemplar built from a public disclosed report (considerthese proposal 2) and C1 suite; `SHONEN.md` round-40 box 2.
- [~] Instructions executable without oral context — r40 suite at Y closed=10/10, selftest cases=10 failures=0; harness 26/26, binding 54/54, census exit 0; `SHONEN.md` round-40 box 3.
- [~] No cross-domain bleed; PROVINCE remains accurate — F23 amendment appended; sibling sweep found no F23 ground; `SHONEN.md` round-40 box 4.

## Stale-lane

Progressing.
