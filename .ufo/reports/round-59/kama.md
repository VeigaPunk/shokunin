# kama — round 59

## Work performed

Claims declared before data: **C1 operability 8→8**, a per-leg battery outcome binding (sourced on S517), and **C2 calibration 7→7**, replacing the typed closure count and pinned manifest revision with a measured-tip derivation (calibration 7 is the lowest assigned axis). Both claims are **not verified**; no claim is admitted.

- Froze the claims, predicates, controls and kill rules before the swarm at lane commit `5d957d24e77bef5cb2e7c658060b2d98a37c96c5`; full text: `kama-shokunin/.ufo/waves/round-59/controls/freeze.txt`.
- Added `tools/round59-battery-outcome-check.py`, `tools/round59-c1-counter.py`, five outcome-mutant fixtures, and the dynamic calibration counter `tools/round59-c2-counter.py`; added the calibration-row derivation command. Commits `494c165759a644a56ec81bb51a7837b028817d89`, `2c7443abb8d6edb8a5b0f91dfee9f81b824f6d35`, `aca8d0067ea25627c5015c2193c843965148bc8e`, `9552e547b6ed099bf8ed607ac250317863662be7`, `dfe42d00923ba6ff63761d3f2e5dd7bf54ec531a`, `ad7f1d6239c7fecf83a9a7a69b0367ad26a894fa` and `286281109b9aced74fa452a8a0ee644bdaf914c0` are recorded in `kama-shokunin/LOG.md` §Round 59.
- The v2 wave settled 64 result entries; the JSON has null `note` for each but no per-seat status/dead fields. M08AlwaysReject returned unfinished instructions and has no report artifact, so it is incomplete/unverifiable; I do not infer a dead-seat count. Role mix: reviewer 16, critic 14, mutation-tester 12, executor 12, scout 6, connector 2, scribe 2; 42/64 attack roles. The L1 held the planner seat. One wave; no residual call. Dispatch/spec/registry/results: `kama-shokunin/.ufo/waves/round-59/w1/`.
- **C1 falsification:** R04's one-call `python3 other-script --counter ...` battery is accepted by the measured checker (`runs=5 passed=5/5 errors=0 met=True`, exit 0), despite the frozen sentence requiring that routing to fail. R15 also ran a checker keyed only to fixture directory names; the frozen counter accepted it. K02 found the checker synthesizes observed output from `BAD_ENV` source text. Evidence: `w1/out/R04DecoyArgv.md`, `R15CounterGaming.md`, `K02PredicateParity.md`.
- **C2 falsification:** K05 appended a static assertion to a scratch-only calibration row and the C2 counter still returned `mismatches=0 met=True`; M12 dropped each of the eight mismatch clauses individually and every mutant still returned met=True. The expected outside S517/S518 review is absent. Evidence: `w1/out/K05C2Noop.md`, `M12C2Clauses.md`, `S04CurrentClosure.md`.
- Re-opened S517 and S518, rechecked the S513/S512 scope distinction, and hand-checked all seven quarantine IDs. No new source row or knowledge entry was admitted. S517's `used-by` changed old→new to include this lesson; `corpus/SOURCES.md` remains at 259 rows. Lesson: `corpus/lessons/round-59.md`.
- Added KQ99 to `corpus/QUALITY.md` from the observed decoy/name-oracle failure. This is a future admission bar, **not** a repair or retroactive pass. No tools were installed or updated.

## Landed changes

- Freeze/prescribed start evidence: `5d957d24e77bef5cb2e7c658060b2d98a37c96c5`; record: `LOG.md` §Round 59.
- C1/C2 instruments, fixtures and dynamic calibration-row edit: `494c165759a644a56ec81bb51a7837b028817d89`; C1 frame/fault instrumentation fixes: `2c7443abb8d6edb8a5b0f91dfee9f81b824f6d35`, `aca8d0067ea25627c5015c2193c843965148bc8e`; record: `LOG.md` §Round 59.
- Pre-data controls: `114fdf78d77f140494b5ccbe1f29b3dd42216dab`; validated spec/dispatch: `4a541190b6d494a4e99116249632e99aab80adcc`; WAVE-DONE results and seat files: `22b5916cb0ae0203312a2a165e64a71194905bb6`; record: `LOG.md` §Round 59.
- Claim verdict, lesson, source/quality edits, SCORECARD reconciliation facts and final measurements: `0e2e4ea18facfacad5b64394820d1611aa25c0ae`, `9552e547b6d494a4e99116249632e99aab80adcc`, `dfe42d00923ba6ff63761d3f2e5dd7bf54ec531a`, `e7f16ee05ad09906f2ff2283bd32b9a3c8fafbcb`, `ad7f1d6239c7fecf83a9a7a69b0367ad26a894fa`, `286281109b9aced74fa452a8a0ee644bdaf914c0`, `f1cd775ebb57ecd5bcf02ebcc16a68dba99527fc`; record: `LOG.md` §Round 59 and its final remeasure bullet.

Final lane HEAD: `f1cd775ebb57ecd5bcf02ebcc16a68dba99527fc`; `git ls-remote origin refs/heads/master` returned the same hash. Final lane state: `ahead=0 behind=0`.

## Before → after measurements

- **C1 operability 8→8:** at the same lane tip `aca8d0067ea25627c5015c2193c843965148bc8e`, the prior r58 checker scored `genuine=1/1 benign=3/3 noop_rejected=13/16 errors=0 met=False` (exit 1); the r59 checker scored `genuine=1/1 benign=3/3 noop_rejected=16/16 errors=0 met=True` (exit 0). Commands: `python3 tools/round59-c1-counter.py --repo <repo> --tip aca8d0067ea25627c5015c2193c843965148bc8e --checker tools/round58-battery-exec-check.py --work <scratch>` and the same without `--checker`. Receipts `controls/c1-oldchecker-final.out`, `controls/c1-candidate-final.out`; final replay at lane tip `ad7f1d6239c7fecf83a9a7a69b0367ad26a894fa` is `measured/c1-final.out`. **The claim is falsified by R04/R15 despite that finite counter pass; no operability score credit.**
- **C2 calibration 7→7:** base lane tip `8f7f58cd161f2b7dfa1709450c3ae79599c12833` → `rows=44 mismatches=3 met=False` (exit 1); edited lane tip `2c7443abb8d6edb8a5b0f91dfee9f81b824f6d35` → `rows=44 mismatches=0 met=True` (exit 0), fleet ref `0f99f606120d0c884656c6e7a290f0e8f33c2181`. Command: `python3 tools/round59-c2-counter.py --repo <repo> --tip <lane-tip> --fleet-repo /home/vgpnk/Projects/shokunin --fleet-ref 0f99f606120d0c884656c6e7a290f0e8f33c2181`. Base/after receipts: `controls/c2-base-current-head.out`, `controls/c2-after-current-head-latest.out`; final replay at lane `ad7f1d6239c7fecf83a9a7a69b0367ad26a894fa`, fleet `a41c6644b749e8b1289be73d10706217fa070357`, is `measured/c2-final.out`. K05/M12 falsified the counter's semantic target; no calibration credit.
- `python3 tools/round42-selfdesc-reconcile.py --repo <repo> --tip ad7f1d6239c7fecf83a9a7a69b0367ad26a894fa` → `r41=0 ... rel=0 mismatches=0 maxN=59 met=True`, exit 0 (`measured/selfdesc-final.out`). This does not cure either claim's counterexample.

## Sources & frontier

- Start validation: `sources-census.sh validate --file corpus/SOURCES.md` → exit 0; stdout's final line is `file\tok\t/home/vgpnk/Projects/shokunin/kama-shokunin/corpus/SOURCES.md` and all W04 warnings are retained in `kama-shokunin/.ufo/waves/round-59/census/start.out` (`start.exit`). Start rows: `git show 8f7f58cd161f2b7dfa1709450c3ae79599c12833:corpus/SOURCES.md | grep -cE '^ {0,3}\\|[[:space:]]*S[0-9]{3,}[[:space:]]*\\|'` → **259**.
- End validation: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kama` → exit 0; stdout's final line is `kama\tok\t/home/vgpnk/Projects/shokunin/kama-shokunin/corpus/SOURCES.md` and W04 warnings are retained in `census/end-final.out` (`end-final.exit`). End rows by `grep -cE '^ {0,3}\\|[[:space:]]*S[0-9]{3,}[[:space:]]*\\|' corpus/SOURCES.md` → **259**. The initial round-start attempt mistakenly used the lane itself as `--root` (exit 2, no `shokunin.conf`); the lane-file validator above was used for the start baseline.
- Rows added by tier/status: none. Touched row: S517 `used-by` old→new adds `corpus/lessons/round-59.md`; status/recheck unchanged. Frontier rows advanced: none. Quarantine dispositions: S200/S210/S211 quote absent; S202 present but not appended (no admitted entry cites it); S206 present and already mined as S206; S224 compound quote unsupported; S230 present and already covered by S329. Details/anchors are in `corpus/lessons/round-59.md` and `w1/out/S05Quarantine.md`.
- Assimilation: none from `merge/kama/`; no source/knowledge entry admitted from that package. `considerthese/2026-10-26.md` was opened; proposal 3 does not fit the frozen claims and remains unimplemented.
- S517 was reopened at https://docs.python.org/3/library/sys.html#sys.setprofile on 2026-10-27; located quote and scope are recorded in the lesson. The claim cites this existing row. No new registry IDs were created.

## Trend verdicts

- **expansion — unchanged:** no new `corpus/knowledge/` entries or uncovered ground admitted; registry count stayed 259.
- **quality — improved (narrow):** KQ99 adds a lesson-backed admission bar for battery gates after the R04 one-call decoy and R15 name-keyed checker. It is a bar only; the checker/counter defect remains and no corpus entry was newly admitted.
- **discernment — unchanged:** no non-author admit/reject spot-check of S517/S518 is recorded; swarm seats are lane authors. MANIFEST current at fleet HEAD `a41c6644b749e8b1289be73d10706217fa070357` still has kama r57 as the latest closure (`rejected-honest-stop`). The watchdog records `complete kama round=58`, but no corresponding r58 MANIFEST closure row was present at filing.

## SHONEN

[~] Box 1 — `SHONEN.md:5-6`; author assertion, no named non-author verifier this round.
[~] Box 2 — `SHONEN.md:7-8`; historic task evidence is cited there, not independently re-executed this round.
[~] Box 3 — `SHONEN.md:9-10`; author assertion, no independent instruction replay this round.
[~] Box 4 — `SHONEN.md:11-12`; author assertion, no independent province audit this round.

Stale-lane: **progressing** — watchdog launch `2026-10-27T17:13:51-03:00 launch kama round=59` (`.ufo/watchdog.log`); lane-authored round-59 commits landed through `f1cd775ebb57ecd5bcf02ebcc16a68dba99527fc`. No `complete kama round=59` or `lane-dead-no-report kama round=59` entry was present at filing. This is the only kama mission for the respawn-per-round driver.

Open L0: the previously filed round-35 axis-authority conflict remains (`.ufo/l0-questions.md:145`); no new operator decision was needed. Tool installations/updates: **none**.
