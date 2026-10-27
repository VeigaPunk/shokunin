# kaidoku — round 43

## Work performed

Declared claims: **R43-C1 — calibration**, measuring the existing SquashFS v4 table with a generator that refuses unobserved tuple declarations; **R43-C2 — coverage**, making 18 host-local SOURCES paths resolvable from lane-owned copies.

- Fresh-start controls and the frozen predicates were prepared before data; canonical freeze `f3f8db389416d094b1ddeb1215ddcf914bfc0d1c`, control receipts `681360e6` (`plans/round-43-claims.md`, `.ufo/waves/round-43/controls/`). L1 held the planner seat because the wave validator rejects `planner` as a swarm role.
- R43-C1: corrected the predictor for C02 and the C05 legacy-damage/residue case, added post-run tuple refusal and `--tuple-check`; fresh data was produced from the freeze seed and scored 78/78 at `77d196c66f4fea00d7d543728b190ebdfaf6d0f0` (`tools/round-43/heldout-gen-v4r43.py`, `.ufo/waves/round-43/l1/heldout-generation.log`, score receipt `c1-at-77d196c6.json`). Counter selftest: 91/91 (`.ufo/waves/round-43/w1/artifacts/R43C1Counter/evidence/selftest.txt`); generator tuple selftest: 17/17 (`.ufo/waves/round-43/w1/artifacts/R43C1Gen/receipt-selftest-tuple.txt`).
- R43-C2: landed 17 copies plus the preserved S126 entry and map at `09ab56b8`; the gate and the committed copy-audit report green, but the frozen aggregate scorer stops on its exact numstat clause (`.ufo/waves/round-43/l1/scores/c2-at-77d196c6.json`; independently attacked in `w2/R43W2C2Score.md` and `R43W2C2Registry.md`).
- Round shape: wave 1 settled 32/32 (`r43-w1-results.json`); wave 2 settled 32/32 (`r43-w2-results.json`), total 64, 0 dead seats. W1 role mix: executor 9, reviewer 5, critic 4, scout 4, scribe 3, connector 3, mutation-tester 1, revenger 1, simplifier 1, sentinel 1. W2: reviewer 10, critic 8, mutation-tester 4, scout 4, connector 3, sentinel 2, scribe 1; 22/32 were attack roles. W2 falsified the C1 counter's source/provenance and ID-path assumptions and the C2 verifier's path-containment assumptions; see `.ufo/waves/round-43/w2/R43W2SentC1.md` and `R43W2SentC2.md`. R42-CL2 received its falsification wave.
- Frontier/assimilation: re-grounded and admitted `sasquatch-prebuilt-package-inventory`; retained the earlier compatibility rejection; hand-checked the five-row quarantine slice; collision guard found 29 staged-ID collisions (S106–S134); `considerthese/` is absent. Evidence: `corpus/lessons/round-43.md`, `.ufo/waves/round-43/assimilation/`, and `w1/R43AssimGround.md` / `R43Quarantine.md`.
- Pre-file gate: `tools/round-42/prefile-gate.py --root <lane> --round 43 --json` → GREEN, exit 0; committed receipt `.ufo/waves/round-43/l1/prefile-gate.json`.

## Landed changes

All lane changes are recorded in `LOG.md:3184-3196` and are committed on the lane's `main` branch:

- Claims, tools, source rows, SKILL status markers and wave-1 evidence: `eadcbfa5`; final control freeze: `f3f8db38`; scored freeze controls: `681360e6`.
- C2 copies/map: `09ab56b8`; C1 held-out data: `77d196c6`; C1 score, scored knowledge entry and evidence: `5856614a`.
- Scorecard/SHONEN and lesson: `80e27dc1`; wave-2 results, reports, README coverage-map row, LOG and lesson updates: `8de80f1d`; closure wording correction: `ade72749`; base census replay: `b4b917d7`; tooling provenance note: `ba97830a`.
- Final pre-file receipts: `1bc9aab6`, refreshed at `494b432c`, and `dadb1ef1`.
- Final lane commit: `dadb1ef1e3262d687d08496759b50e97b2a5b2fe`. `git ls-remote origin refs/heads/main` returned the same hash.

## Before → after measurements

- **R43-C1 (calibration) — met.** Before: at the freeze the counter exits 2, `no_manifest_at_rev` (do-nothing receipt). After: `matched=78/78`, all 45 bindings true, `observed_features_match_declared=true`, tuple-check 78 records (effective n=76; H25/H26 are disclosed out-of-domain cases), `combo_unseen_majority=21/24` with threshold 12, exit 0. Command: `python3 -I -B tools/round-43/c1-counter.py --root <LANE> --rev 77d196c66f4fea00d7d543728b190ebdfaf6d0f0 --freeze f3f8db389416d094b1ddeb1215ddcf914bfc0d1c --json-out <OUT>`. Measured at `77d196c6`; receipt `.ufo/waves/round-43/l1/scores/c1-at-77d196c6.json`.
- **R43-C2 (coverage) — not met; honest stop.** Before: gate at the freeze exits 1 with 18 failed rows. After: in the clean scored clone the gate exits 0 (`rows_checked=19`, `rows_total=137`, `rows_failed=[]`); the frozen C2 scorer exits 1 because `sources_numstat_three_additions=false`: actual BASE→REV `corpus/SOURCES.md` numstat is `4\t0`, not frozen `3\t0` (three appended rows plus a blank separator). Command as recorded in the receipt: `python3 -I -B tools/round-43/c2-score-r43.py --root /home/vgpnk/Projects/shokunin/kaidoku-shokunin --rev 77d196c66f4fea00d7d543728b190ebdfaf6d0f0 --freeze f3f8db389416d094b1ddeb1215ddcf914bfc0d1c --scratch /fast/scratch/hyaku/kaidoku-r43/l1-c2-score-final --upstream-dir /fast/scratch/hyaku/kaidoku-r43/l1-c2-inputs --tarball-67 /fast/scratch/hyaku/kaidoku-r43/l1-c2-inputs/tgz/rea6.7.0.tgz --tarball-65 /fast/scratch/hyaku/kaidoku-r43/l1-c2-inputs/tgz/rea6.5.0.tgz --json-out .ufo/waves/round-43/l1/scores/c2-at-77d196c6.json`. Measured at `77d196c6`; the frozen predicate was not changed. W2 could not recreate all upstream-backed copy-audit inputs after the L1 scratch was removed; its report separates embedded receipt evidence from independently rerun checks.

## Sources & frontier

- `corpus/SOURCES.md`: **134 → 137 rows**. Counting command: `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`. Baseline `6b9e64fe` is 134; final is 137. Start receipt `.ufo/waves/round-43/census-start.txt` and an exact base-clone replay `.ufo/waves/round-43/assimilation/census-base-replay.txt` both show `kaidoku ok`, exit 0. End command `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kaidoku` → `kaidoku ok`, exit 0, 13 pre-existing W04 warnings; receipt `.ufo/waves/round-43/l1/sources-census-end.txt`.
- Rows added by tier: **tier A: 3** — S135 (`docs`, unblob 26.6.4 LICENSE), S136 (`dataset`, sasquatch releases API), S137 (`docs`, rendered release page). No existing row status/recheck/used-by cells changed. No Frontier row moved to Core; sasquatch remains a packaging-inventory Frontier topic.
- One assimilation theme was re-grounded; the matrix entry is admitted and the compatibility candidate remains rejected. Quarantine: S150 fabrication-class/refused, S113/S136/S147 present with anchor caveats, S117 unverifiable; none of the five quarantine rows was appended. The indented ID guard found 29 collisions; normalized S136/S137 followed S135 rather than appending the staged package rows. `considerthese/`: no such directory.
- Conformance limits: the frozen S135 row contains a spliced quote and its opening timestamp differs from the scored entry's capture; S136/S137 row captures and the entry's captures are different retained fetches. W2 documented these source-provenance mismatches in `R43W2Closure.md` C6; frozen rows were not rewritten. The C1 counter also does not bind S135's URL/digest. These do not change the observed C1 score but remain provenance limitations.

## Trend verdicts

- **Expansion — improved.** One admitted sasquatch release-matrix entry on previously uncovered package-inventory ground, sourced to S136/S137; `.ufo/waves/round-43/w1/R43AssimGround.md` and the landed entry.
- **Quality — improved.** The generator now refuses mismatched observed tuples and the re-grounded matrix corrects earlier overclaims; C1's measured receipt is green. C2 remains an honest stop, not a green claim; its aggregate score is not overridden by the gate/linter child results.
- **Discernment — unprovable-but-better.** Wave-1 gate decisions and the internal critic's admit/reject review are recorded, but dispatched seats are the lane, not an outside verifier. Independent non-author spot-check remains required for closure.

## SHONEN

- [~] Box 1 — decision tables/error patterns/checklists and citations: `SKILL.md` rule block 21, `tools/round-42/sqfs-triage-v4.py --table-only`, `w2/R43W2SentC1.md`.
- [~] Box 2 — end-to-end task: 78 fresh fixture-built carriers and C1 score receipt at `77d196c6`; `LOG.md:3187`.
- [~] Box 3 — executable instructions: generator refusal (`--tuple-check` exit 3 red / exit 0 green), counter and pre-file gate receipts under `.ufo/waves/round-43/`.
- [~] Box 4 — province boundary: `PROVINCE.md` round-43 frontier note; `w1/R43ConnSib.md`; no compatibility/Core claim added.

**Stale-lane:** progressing — launch `2026-10-27T06:04:06-03:00`; lane commits landed through `dadb1ef1`; no other kaidoku mission is open. The round closed only after both wave settlements.

**Tooling:** no explicit L1 tool installation/upgrade and no pacman transaction. The generator ran `npx -y rea-agents@6.5.0`; the 6.5.0 package cache was absent during wave-1 reconnaissance and present at closure. `[INFERENCE]` npx may have hydrated the npm cache during the data run; the installation event/time is not retained. No other tool install/upgrade was observed.

**L0:** no kaidoku round-43 L0 question was opened. The existing host-recovery/pacman-pause question remains operator-owned and unanswered; no pacman transaction was attempted.

**Misroot sweep:** `git -C /home/vgpnk/Projects/shokunin status --porcelain` reported only `?? .scratch/closure-mado-r50.json` (orchestrator-owned run state); it was left untouched. No seat-authored R43 file was found misrooted in the fleet repo.
