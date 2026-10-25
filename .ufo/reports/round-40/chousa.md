# chousa round 40 — receipt evidence repair and calibration corrections

## Work performed

Declared two claims: **C1 — operability**, the lowest scored axis (3/10), measures the committed r39 active-receipt audit `3/6 → 6/6`; **C2 — calibration** measures evidence-backed R2–R5 dispositions `0/4 → 4/4` (R4 is explicitly “not reproduced” against the current committed artifacts).

- Froze both predicates and scored the do-nothing controls before receipt regeneration: C1 `R39_ACTIVE_RECEIPTS=3/6`, exit 1; C2 `R39_CALIBRATION_DISPOSITIONS=0/4`, exit 1. The frozen design and exact outputs are `corpus/evidence/round40/claims.md` and `.ufo/waves/round-40/controls/control-before.txt` (freeze commit `6c01a4144b3637cc57a989ab464f71b8ae69595a`).
- Reproduced R1 on the old committed r39 receipts: three refuse `expect-sha256-mismatch`; the superseded s39003 draft refuses first on `counter-sha256-mismatch`. Reissued the base, landed-gate, and mutant-control c1 receipts under round-40 paths; the originals remain unchanged. Red-before output: `.ufo/waves/round-40/controls/r1-stale-before.txt`; six active receipts now verify: `corpus/evidence/round40/measure-after.txt`.
- Dispositioned R2–R5 append-only in the r39 claim file and `corpus/evidence/round40/routed-defect-dispositions.json`. R2 is committed and superseded, so the r39 receipt directory had seven files rather than six. R3's historical knowledge count is 50→52, not 29→31. R4 was not reproduced: the committed r39 spec, validator plan, and report agree on reviewer 6 / revenger 2 (32 seats), while the spot-check states reviewer 8 / revenger 0. R5's “two independent runners” wording is corrected to two L1 construction seeds.
- Re-opened official Python `hashlib` documentation, reused S059, and admitted `corpus/knowledge/receipt-expectation-digests-r40.md` for the previously unheld receipt-expectation-digest subground. S059's `used-by` changed old→new; the proposed second row is retained as rejected S074 with its reason and flip. Evidence: `corpus/SOURCES.md:69,84,106-109`, `corpus/lessons/round-40.md` `## Gate`, and `corpus/README.md:1038,1059`.
- Prepared and validated one v1 wave under policy v1: 33 distinct items, with a 33-seat task payload and registry. It was **not dispatched by this seat**; no seat returned or died, and no wave 2 was prepared without wave-1 results. L1 held the planner seat. Spec, plan, dispatch envelope, registry, and handoff: `.ufo/waves/round-40/`.
- Misroot sweep before this report: `git -C /home/vgpnk/Projects/shokunin status --porcelain`. It showed fleet-root state/watchdog changes and unrelated untracked files; this seat dispatched no L2 writers, so none were attributable to chousa round 40. All unowned paths were left untouched.

## Landed changes

- Frozen claims, control receipts, v1 spec/plan/dispatch envelope and prepared registry: lane commit `6c01a4144b3637cc57a989ab464f71b8ae69595a`.
- R1 replacement receipts; R2–R5 corrections and dispositions; S059/S074 curation; sourced knowledge/index updates; corrected wave item: lane work commit `d164f88eb71a6c48a66ae1e7abfcb5fef82219d9`.
- Committed after-measurements, round-40 lesson, LOG entry and SCORECARD claim outcomes: lane metadata commit `282dc76856b22747fc531f188df1718a8e18e99a` (final lane tip). The round-40 LOG entry at `LOG.md:1472-1482` ties the work to both earlier commits.

## Before → after measurements

| Claim | Before | After | Counting command | Measured commit |
|---|---|---|---|---|
| C1 operability, receipt integrity | `R39_ACTIVE_RECEIPTS=3/6`, exit 1 (baseline lane tip `691d26476ac39b8ec8b65155b41199e6f6d1f299`) | `R39_ACTIVE_RECEIPTS=6/6`, exit 0 | `python3 corpus/evidence/round40/c1-count.py` | `d164f88eb71a6c48a66ae1e7abfcb5fef82219d9` |
| C2 calibration, R2–R5 dispositions | `R39_CALIBRATION_DISPOSITIONS=0/4`, exit 1 (same baseline) | `R39_CALIBRATION_DISPOSITIONS=4/4`, exit 0 | `python3 corpus/evidence/round40/c2-count.py` | `d164f88eb71a6c48a66ae1e7abfcb5fef82219d9` |

C1's existing 0–10 score remains 3→3 because its fixed legacy observable counts only three archive exports; the separately frozen operational receipt metric moved 3/6→6/6. Calibration remains numerically unscored; no score was invented. Both counters' exact outputs and the committed run are in `corpus/evidence/round40/measure-after.txt`.

## Sources & frontier

- Registry rows: **73 → 74**. Tier histogram: A 67→68, B 1→1, C 5→5; status histogram: mined 50→50, queued 19→19, rejected 4→5. One A-tier row was added as a rejected duplicate-registration proposal (S074); no new source is admitted. S059 was re-opened and its `used-by` changed from `corpus/knowledge/revision-binding-r31.md` to `corpus/knowledge/revision-binding-r31.md, corpus/knowledge/receipt-expectation-digests-r40.md`; its status and recheck did not change. S074's rejection and flip are in `SOURCES.md` and the lesson Gate.
- Row/histogram commands and outputs: baseline `git show 6c01a4144b3637cc57a989ab464f71b8ae69595a:corpus/SOURCES.md | awk -F'|' '/^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|/ {n++; t=$5; s=$9; gsub(/[[:space:]]/,"",t); gsub(/[[:space:]]/,"",s); tier[t]++; status[s]++} END {printf "ROWS=%d A=%d B=%d C=%d mined=%d queued=%d rejected=%d\n",n,tier["A"],tier["B"],tier["C"],status["mined"],status["queued"],status["rejected"]}'` → `ROWS=73 A=67 B=1 C=5 mined=50 queued=19 rejected=4`; after `awk -F'|' '/^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|/ {n++; t=$5; s=$9; gsub(/[[:space:]]/,"",t); gsub(/[[:space:]]/,"",s); tier[t]++; status[s]++} END {printf "ROWS=%d A=%d B=%d C=%d mined=%d queued=%d rejected=%d\n",n,tier["A"],tier["B"],tier["C"],status["mined"],status["queued"],status["rejected"]}' corpus/SOURCES.md` → `ROWS=74 A=68 B=1 C=5 mined=50 queued=19 rejected=5`. Full after output: `corpus/evidence/round40/measure-after.txt`.
- Round-start census: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin chousa`, exit 0:
  ```text
  chousa	W04	S051 duplicate url www.w3.org/TR/2017/REC-html52-20171214/syntax.html across scopes
  chousa	W04	S053 duplicate url docs.python.org/3/library/socket.html across scopes
  chousa	W04	S073 duplicate url www.gnu.org/software/coreutils/manual/coreutils.html across scopes
  chousa	ok	/home/vgpnk/Projects/shokunin/chousa-shokunin/corpus/SOURCES.md
  ```
- Round-end census: same command, exit 0:
  ```text
  chousa	W04	S051 duplicate url www.w3.org/TR/2017/REC-html52-20171214/syntax.html across scopes
  chousa	W04	S053 duplicate url docs.python.org/3/library/socket.html across scopes
  chousa	W04	S073 duplicate url www.gnu.org/software/coreutils/manual/coreutils.html across scopes
  chousa	W04	S074 duplicate url docs.python.org/3/library/hashlib.html across scopes
  chousa	ok	/home/vgpnk/Projects/shokunin/chousa-shokunin/corpus/SOURCES.md
  ```
- Frontier advanced one narrow subground: exact expectation-file digest identity, indexed by `corpus/knowledge/receipt-expectation-digests-r40.md`, citing reopened S059. The row-74 duplicate registration remains rejected, not counted as an admitted source. Knowledge files: 52→53.

## Trend verdicts

- **expansion: improved** — one new knowledge entry covers receipt-expectation digest identity on previously unheld ground and cites reopened, mined S059.
- **quality: improved** — the three active stale-byte receipts were regenerated; all six active receipts verify against committed inputs, and the end census exits 0.
- **discernment: unchanged** — the round's admitted/rejected sample has no non-author spot-check. No lane-dispatched seat is counted as independent review.

## SHONEN

- [~] SKILL.md decision tables, error patterns and checklists — `SKILL.md:13-24,39-73`; lane assertion, no non-author verifier.
- [~] End-to-end domain task executed and logged — `LOG.md:1472-1482`, `corpus/evidence/round40/measure-after.txt`; lane assertion.
- [~] Instructions executable without oral context — `corpus/evidence/round40/c1-count.py`, `c2-count.py`, frozen claims and wave plan; lane assertion.
- [~] No cross-domain bleed, PROVINCE accurate — `PROVINCE.md:5-17`; no external live-target research; lane assertion.

Stale-lane: respawn-per-round driver; no other mission of this lane is open.
Tool installs: none. No pacman transaction attempted.
Open L0 questions: none added this round.
