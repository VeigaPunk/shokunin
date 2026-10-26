# Kasegi round 39

## Work performed

Declared claims: **C1 — depth:verifiability (score 4, lowest non-retired axis)**, to add a verifiable G1–G8 closure instrument; **C2 — coverage (score 7)**, to add one sourced frontier topic. C1 is not admitted; C2 verifies.

- **C1:** integrated `corpus/instruments/r39-closure.sh` and its G1–G8 selftests. At final judged head J=`ee5ae5e1739527f4cdb50babe2d694005607b44e`, the clean-scratch, clean-clone run printed `closed=7/8 exit=1` (G2 red); its selftest printed `cases=8 failures=1` (G2 positive red). The Y=`8371e7ac9f32cae5ed72f8c28205634603f836fa` diagnostic also printed `closed=7/8 exit=1`, selftest `cases=8 failures=1`. C1 is **harmed/unprovable**, score held at 4: wave-2 mutations show G2 accepts forged recorded payload values, and the committed receipt's values are not bound to captured output (`wave2/CritG2Exploit.md`, especially F2; `wave2/CritC1Kill.md`). G6 also depends on a quiescent scratch root; see `corpus/lessons/round-39.md:81-94` and final receipt `.ufo/waves/round-39/final-gates/all-gates.txt`. The final Y diagnostic is report-only, not a committed transcript.
- **C2:** admitted F22, “CISA When to Issue VEX Information,” with mined source S057 and the entry `corpus/knowledge/cisa-when-to-issue-vex.md`; rejected S056/S058/S059. Evidence: `corpus/lessons/round-39.md:20-31,68-70`, `corpus/README.md` F22 row, and source-recheck/harness outputs below.
- **Frontier and mistake learning:** opened S057 this round; recorded located quotes in the lesson Gate. M39-1–M39-4 are in `corpus/lessons/round-39.md:72-79`; wave-2 attacks and corrected evidence records follow at `:81-94`.
- **Swarm:** reused attempt-1 wave evidence; no wave was re-dispatched. Two validated v1 waves: build 49 (27 executor, 11 scribe, 6 reviewer, 2 scout, 2 critic, 1 connector) and falsify 37 (12 reviewer, 8 critic, 7 mutation-tester, 4 scout, 2 sentinel, 2 connector, 1 simplifier, 1 scribe), **86 total**. The L1 held the planner seat; wave 1 met the L2 role floor in one batch. Attack roles reviewer/critic/mutation-tester were 35/86 (40.7%). Results: `.ufo/waves/round-39/kasegi-r39-build-results.json` and `kasegi-r39-falsify-results.json`, each with all dispatched result entries and outputs; dead seats: 0.
- **Attempt-1 inheritance:** reused the frozen claims/controls and landed work at `dcd3170`, `1a139e0`, `57ea9ea`, `06632fa`, `46c66c2`, and `5006097`, then re-verified the 49-seat build results and settled 37-seat falsification results. Discarded the inherited all-gates-v3 receipt as final proof: its `run-utc=2026-10-26T21:35:00Z` post-dated its containing commit and wave 2 falsified its payload-proof assumption. Replaced it with the observed J3 transcript in `final-gates/all-gates.txt`; the intermediate dirty-worktree 6/8 output was not retained as the final measurement.
- **No misroot:** the required fleet-root `git status --porcelain` sweep was empty; no seat files were copied or deleted at the fleet root.
- **Assimilation:** none adopted from `shokuknow/merge/kasegi/`; the round's source/claim is S057, not package adoption. `considerthese/2026-10-26.md` proposal 1 was mined into the distance-to-next-score section; proposal 3 status was carried in the ledger.
- **Tooling:** no installs or updates; pacman was not used. No new L0 question. Existing kasegi round-15/16 domain-root restoration/re-scope questions remain open in `.ufo/l0-questions.md`.
- **Stale-lane:** progressing (lane-authored commits `3fa81ef`, `752e476`, `ee5ae5e`, `8371e7a` landed during this mission).

## Landed changes

- Claim and frontier work plus initial LOG entry: `LOG.md:1707-1717`, inherited commits `1a139e0` / `46c66c2` and evidence receipt `5006097`.
- Falsification integration, missing SKILL registry row, standalone LOG correction, wave-2 lesson, and all wave-2 artifacts: `LOG.md:1718-1719`, `corpus/lessons/round-39.md:81-94`, commit `3fa81ef5e7b558030903db71c3bb66cb0ea976a2`.
- Per-claim scorecard measurements and verdict: `SCORECARD.md:1563-1584`, `LOG.md:1719`, commit `752e476d8c5d0f74ef80ea89b6916e7af99a2721`.
- Explicit `report-only` labels for non-transcript J1 measurements (G3 coverage): commit `ee5ae5e1739527f4cdb50babe2d694005607b44e`.
- Final J3 run/selftest transcript and truthful UTC timestamp: `.ufo/waves/round-39/final-gates/all-gates.txt`, commit `8371e7ac9f32cae5ed72f8c28205634603f836fa` (Y; `git diff --name-only J Y` is the receipt alone).

## Before → after measurements

- **C1 — depth:verifiability, 4→4 (score held; claim harmed/unprovable).** Before at base `480b1a505a2dfc14a4f718d16d63808247214d0a`: instrument absent, R1–R5 open (`.ufo/waves/round-39/c1-controls/before.txt`). Frozen command at J: `bash corpus/instruments/r39-closure.sh --export-ref ee5ae5e1739527f4cdb50babe2d694005607b44e --lane /fast/scratch/hyaku/kasegi-r39/gates-work/lane --work /fast/scratch/hyaku/kasegi-r39/gates-work` → `closed=7/8 exit=1`; `--selftest` on the same ref → `selftest cases=8 failures=1` (both outputs are committed in the J receipt). Final-Y diagnostic (report-only): `bash corpus/instruments/r39-closure.sh --export-ref 8371e7ac9f32cae5ed72f8c28205634603f836fa --work /fast/scratch/hyaku/kasegi-r39/gates-work` → `closed=7/8 exit=1`; selftest → `cases=8 failures=1`. Base and r38 judged-head controls each printed `closed=2/8 exit=1`; plain run refused with exit 2. Measured J=`ee5ae5e1739527f4cdb50babe2d694005607b44e`, Y=`8371e7ac9f32cae5ed72f8c28205634603f836fa`. No C1 score increase is claimed.
- **C2 — coverage, 7→7 (verified; score held).** At base `480b1a505a2dfc14a4f718d16d63808247214d0a`: frontier 21, registry 55, S057 citations 0, knowledge entries 50, harness 24/24, binding 45/45, audit expected 50 (`.ufo/waves/round-39/c2-controls/before.txt`). At measured commit `3fa81ef5e7b558030903db71c3bb66cb0ea976a2`: `grep -cE '^\| F[0-9]+ \|' corpus/README.md` → 22; `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` → 59 (E1 corrects the frozen draft's 58); `grep -rlE '^source: S057' corpus/knowledge | wc -l` → 1; `python3 corpus/instruments/frontier-recheck-count.py` → `entries=25 pass=25 exit=0`; `source-recheck.py --manifest corpus/source-snapshots/round-39/manifest.json --source S057` exit 0; capture binding `records=46 bound=46 unbound=0`; recheck audit `expected=51 missing=0 unexpected=0 exit=0`; knowledge entries 51. F22 junk twin rejected (four `MISMATCH`, exit 1). Source census exit 0.

## Sources & frontier

Census command (both runs): `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kasegi`.

Before (from round-start `census-before.txt`), exit 0:
```text
kasegi  W04  S028 duplicate url docs.hackerone.com/en/articles/8494502-safe-harbor-overview-faq across scopes
kasegi  W04  S029 duplicate url eur-lex.europa.eu/eli/reg/2024/2847/oj/eng across scopes
kasegi  ok   /home/vgpnk/Projects/shokunin/kasegi-shokunin/corpus/SOURCES.md
exit=0
```
After (final run), exit 0; output was the same three lines and exit code.

SOURCES rows 55→59: added S057 (tier A, mined), S056 and S059 (tier A, rejected), S058 (tier B, rejected); status/recheck/used-by cells on prior rows touched: none. F22 advanced the frontier 21→22; C2's admitted entry cites the newly opened S057. Search-log addition and located quotes are recorded in `corpus/lessons/round-39.md:20-31,68-70`. Assimilation: none.

## Trend verdicts

- **expansion: improved** — F22 is the 22nd admitted frontier row and its entry cites opened/mined S057 (`corpus/README.md`, `corpus/knowledge/cisa-when-to-issue-vex.md`).
- **quality: unchanged** — S057's capture binding, source recheck and entry harness pass; no earlier knowledge entry was superseded or newly reverified. The separate C1 instrument defects are reported as a harmed claim, not hidden as corpus-quality gain.
- **discernment: unchanged** — all reviewers were dispatched by this lane and therefore are not non-author verifiers; no outside spot-check of an admit and reject was completed (`corpus/lessons/round-39.md:18-31`).

## SHONEN

- [~] Real decision tables, error patterns/checklists with cited sources — author assessment only; `SHONEN.md:193-194`; no non-author verifier.
- [~] End-to-end domain task executed and logged — no domain hunt ran; F22 capture and harness are the closest work; `SHONEN.md:195-196`.
- [~] Instructions executable without oral context — runnable F22/source/capture/census checks; C1 G2 does not verify its receipt payload; `SHONEN.md:197-198` and `wave2/CritG2Exploit.md`.
- [~] No cross-domain bleed; PROVINCE remains accurate — `SHONEN.md:199-200`, `PROVINCE.md:158`; no non-author verifier.
