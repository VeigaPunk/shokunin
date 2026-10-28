# Souji round 35 — attempt 1

## Status

STATUS: PARTIAL — the sourced F1 census claim was measured and passed its six-leg counter, but C1/C2 final outcomes and the wave closure were not obtained. W1 was dispatched (40 seats) and only two reviewer reports had arrived at wrap-up; W2 was not dispatched. No round admission or score increase is claimed.

## Evidence

- Base `1e9cad0b553891c41fe5b7ad1686decc147d76d4`; instrument `d1c940414087b606503662e4d115f51cb0fba40c`; freeze `4e9c295e9339cc2b13f7a0dd5ec9fc8213a9e18e`. C3 parser amendment A1 is commit `8788d5565f9e1cbc8cd6e4fe84222b5d6483612c`; fixed C3 at `fedfa4068801164ac2e189029137ebe87a1d94d3`.
- C1 do-nothing at instrument revision: `SUMMARY items=60 agree=37 unresolved=23 mismatches=23 withdrawn=0 restated=5`, rc 1 (`souji-shokunin/census/round-35/records/controls-c1-do-nothing.txt`). No final C1 measurement or row integration is claimed.
- C2 control: legs absent at the pre-instrument tip, `COULD-NOT-EVALUATE`, rc 2. J1 junk fixture: `cases=5 pass=5 control=STUB-REJECTED`. Feasibility: W1 and N4 passed; N3 failed (`cases=12 pinned=True summary=False`); W2 failed (`CASE=20 summary=SUMMARY total=20 failed=1`); W3/W4 remain unmeasured. Receipts are under `souji-shokunin/census/round-35/records/`. No full C2 pass is claimed.
- C3: `SUMMARY entries=1 legs=6 fail=0`, rc 0, at `fedfa4068801164ac2e189029137ebe87a1d94d3` with frozen list `4e9c295e9339cc2b13f7a0dd5ec9fc8213a9e18e` (`census/round-35/records/c3-at-current.txt`). The entry records 26 repositories, 27 worktree registrations, and 0 immediately prunable; census receipt `prune-census.tsv` and git-worktree(1) snapshot are committed. The historical 40/14 figure is dated, not falsified.
- A1 was triggered by C3's first frozen-list check: it found `cells[8]` (`opened`) used in place of `cells[7]` (`status`) in SOURCES registry parsing. The correction changed no target or predicate; the red and repaired receipts are committed.
- W1 dispatch spec has 40 distinct seats; dispatch output reports `spawn=40,resume=0,total=40`, `taskCall` present. `.ufo/waves/round-35/w1/` contained two reviewer reports at wrap-up. W1 was not declared complete; no WAVE-DONE notice was received and no W2 was launched.
- No tool installs/updates or pacman transactions occurred. Scores remain calibration 7, operability 8, coverage 8; certification OFF, K5 HELD, NAMESPACE hold unchanged.

## Findings

1. **C3 passes after A1.** The F1 coverage entry and both provenance rows passed the frozen six-leg counter at the measured commit.
2. **C1 remains unresolved.** The control demonstrates a red-before state, but final correction/withdrawal validation and full-width counter reading were not completed.
3. **C2 remains unresolved and has known red legs.** N3 and W2 failures are retained; unmeasured W3/W4 were not silently dropped.
4. **The swarm round is incomplete.** The required second falsification wave, complete W1 results, integration, and non-author closure are outstanding. This report is intentionally partial and must not be read as a completed round/admission.

## Attack log

- W1 is in progress under `souji-shokunin/.ufo/waves/round-35/`; only the two arrived reviewer reports are included in the committed wave tree. The dispatch capture is `w1-spec.json`, `w1-dispatch.json`, `w1-render.out`, and `w1.ready`.
- Feasibility failures are preserved verbatim in `n3-feas-test.txt` and `w2-feas-test.txt`; no failure was relabeled as a pass.

## Deliveries

- Frozen contract and amendments: `souji-shokunin/census/round-35/preregistration.txt`.
- F1 entry and source registry: `souji-shokunin/corpus/knowledge/fleet-prune-numerator-r35.md`, `souji-shokunin/corpus/SOURCES.md`; README frontier update at `souji-shokunin/corpus/README.md`.
- Round lesson and partial measurements: `souji-shokunin/corpus/lessons/round-35.md`, `souji-shokunin/SCORECARD.md`.
- Lane tip committed and pushed: `01dc784134ac03bf04db280383d0c70c39ac4837` (`jj-lane.sh push` returned `landed`); `git ls-remote origin refs/heads/master` confirmed the same hash.

## SHONEN

SHONEN unchanged: no promotion checklist mutation or promotion decision was made. Certification remains OFF and K5 HELD.
