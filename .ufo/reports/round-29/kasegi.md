# kasegi round 29 report

- Lane: `kasegi-shokunin` — bounty & security research (SHONEN: F, C, A, U, G, I, R, D, E; boxes 1/4/5/6 B, 2/3/7/8/9/10 P).
- Round: 29, attempt 1. Wave: one v2 wave `kasegi-r29-build` (spawn 64, resume 0), dispatched via inline handoff (ready `wave1.ready`, dispatcher log `kasegi/kasegi-r29-build: spawned 64/64`).
- Base `7a6591c1…` → freeze `f28ff5d…` → dispatch `46e07f6…` → integration commit `0ab89298d1d85969f978c25baa98242d8434ec7d` (all counters re-run at this hash, post-commit-recheck).
- L1: KasegiR29. Seats: 64 (scout 5, connector 3, executor 20, scribe 13, reviewer 11, critic 4, mutation-tester 4, sentinel 1, revenger 1, simplifier 2). Route mix: m_flash 41/64 (64.1%), attack (reviewer+critic+mutation+labrat-defined share) 19/64 (29.7%) — run-7 lane addendum thresholds met. Dead/empty seats at close: 4 outputs missing at rollup time (ExecHarnessC2, ScribeScorecard, RevNoHarmC1, RevKillTry); three were supplied by peer receipts/other seats (harness numbers in `ExecCanonC2`, no-harm numbers in `ExecDensityNoHarm`, scorecard written by L1); `RevKillTry` was still finalizing; its attack evidence is not required by any kill rule. 60/64 seat receipts present.

## Claims

### C1 — depth:verifiability (lowest non-retired axis, score held 4)
- Surface: `anchorcheck.py --selftest` completeness + hermeticity (round-28 CritC1Kill gaps).
- Before: `selftest cases=9 failures=0`, no `limbs=` assertion, git-free PATH run exit 1 `FileNotFoundError: 'git'` (`c1-controls/before.txt`).
- After (instrument `d0f35f8…`): `selftest cases=12 failures=0`, `limbs=9 covered=9`, exit 0; git-free run `SKIP pin-broken (git not found)`, `skip=1`, `limbs=9 covered=8`, exit 0. Nine declared limbs each have an isolating failing fixture (incl. new mirror-OOB, origin-OOB, origin-BA); coverage is asserted by name, not statically.
- Truthfulness correction (post-wave, L1): per `RevC1Instrument`/`CritGlobal` the no-git run no longer counts the skipped pin-broken limb as covered. Canonical receipt `.ufo/waves/round-29/wave1/c1-receipt-index.txt`.
- Kill rule PASS; do-nothing control (base bytes) cannot meet target. SKILL no-harm: 7/0/306, `skill_exit=0`; density 167.5/659/22 (disclosed, not claimed).

### C2 — coverage (score held 7), sourced
- Frontier F13 admitted 12→13: `program-severity-ladders-and-reward-scales.md` citing S043 (HackerOne standard program policy set), S044 (Bugcrowd VRT README), S045 (Bugcrowd VRT CWE crosswalk) — all rows first registered this round (registry 42→45).
- Counters at integration commit: frontier=13, entries citing S04[3-5]=1, rows=3, census_exit=0 (W04 S028/S029 only), harness `entries=16 pass=16 exit=0` incl. `PASS F13 … ids=S043,S044,S045`, per-id source-recheck exit 0 each, manifest `910608e6…` all 12 assertions exactly-once (Q9).
- Kill rule PASS. Do-nothing control at base cannot meet target.

## Frontier step / assimilation
- Census before `census-before.txt` (42 rows, exit 0) → after 45 rows, exit 0.
- Mistake mine: `corpus/lessons/round-29.md` §Mistakes M29-1…M29-9 (incl. M28-5 persistence: frontier harness crashes with uncaught traceback on an admitted row without its entry; mid-wave S043 occurrences=12/Q9 blind spot; M28-3 counter-emission er; M28-12 digest drift).
- Assimilation: theme “program severity ladders and reward scales” from `merge/kasegi/` (read-only). By-document renumber: staged S031→S043, S032→S044, S033→S045; numeric collisions 12 (S031–S042) pasted; guard proof with indented fixture; quarantine slice 7 rows hand-checked this round (verdicts per row in lesson Gate: e.g. S065 fetched quote-located, S037/S054 fetched no-quote, S048/S069/S070 unfetchable, S068 already-mined-by-document S040); none adopted, flip conditions recorded. Spots: F13 admit re-opened by non-author `RevC2Entry` (partial agree; Q8/Q10 stand) and a refusal re-checked (agree).
- considerthese: proposal 5 landed as `QUALITY.md` R15 (open-defects ledger with runnable closure checks), citing `considerthese/2026-10-25.md` + date; proposals-status ledger in lesson.

## Tools / installs
- None installed or upgraded by L1 or seats (stdlib + committed instruments only; pacman untouched per the addendum guard).

## SHONEN
- Box 2: P (no end-to-end domain task executed this round; claim pipeline absent since the lost-root era).
- Box 8: B (score held; no score improvement). Box 4: B (new capability row). Box 10: B (no proof submitted).

## Next step
- Continue depth:verifiability (4): close M28-5 (harness names the missing row instead of traceback) and make the Q9 occurrence gate fail-closed on non-1 counts (M29-3); consider making the frozen counters emit `bad=`-less values only.
- Coverage 7: F13 entry’s suggested-baseline rule is the proposed next-step cell; candidate F14 from the remaining staged entries (program scope rules and asset boundaries) after quarantine re-checks.
