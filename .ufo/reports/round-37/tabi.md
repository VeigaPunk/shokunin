# tabi — round 37 report

Lane repo HEAD at filing: `f485cce10c8640eda64f5e555f99894ed4de7fb0` (branch `master`, verified on
the remote by `git ls-remote origin refs/heads/master` immediately before this report).
Round start baseline: `ed8ccfc00ad3784bc424aa118e056f8edf4ee803`. Freeze (before data):
`99437d29de036415a9f2d0524343617a3b19988a`.

## Work performed

Declared claims (2, both instrument repairs executing the round-36 verifier spotcheck's
eight routed defects; axes per the frozen `claims.json`):

- **C1 — adjacency** (lowest non-retired axis, 8): counter amendment v5 of the round-36
  adjacency sweep — B1 digest-binds the frozen delta-pins file
  (`810193620393f6e8b76faac4b606977508198de1b9ffd00d3a7440e8f1910655`); B2 parses a moved
  audit note's relocation only from its canonical `verbatim at :N` clause; B3 one predicate
  sentence byte-identical across claims.json, the counter constant and the counter header;
  the drift-audit build tool is repaired as v2 (40-hex kama pin + PINS resolvability guard).
- **C2 — operability** (9): counter amendment v3 of the Firefox BiDi counter —
  B1 `GIT_NO_REPLACE_OBJECTS=1` on every git read plus `refs/replace/*` enumeration
  refusal (grounded in S143, opened this round); B2 teardown survivor check with a
  `live.survivors == 0` predicate term; B3 binds the receipt's `runs[*].observed`
  decoration where derivable from the transcript record (everything else declared
  display-only); the measurement harness is repaired (absolute OUT, clone-relative
  numstat, `check-freshness --worktree --repo` per its usage contract).

Work items, each with an evidence pointer:

- Read the round-36 verifier spotcheck (`corpus/lessons/round-36-verifier-spotcheck.md`)
  and the round-36 L1 state; froze claims/counters/harness/controls before any seat data
  (freeze commit `99437d29`; ten control receipts in `.ufo/waves/round-37/baseline/`).
- Built both amended counters from the frozen predecessors with per-defect traced hunks
  (`.ufo/waves/round-37/counters/c1-adjacency-sweep-v5.mjs`,
  `c2-firefox-bidi-v3.mjs`, `c1-drift-audit-build-v2.mjs`), plus harness v2
  (`.ufo/waves/round-37/measure.sh`) and the controls driver
  (`.ufo/waves/round-37/baseline/run-controls.sh`).
- Ran the ten frozen controls (all receipts committed): c1r37-J1 v4 admits unfrozen pins
  (exit 0) / v5 refuses (exit 2, digest mismatch); c1r37-J2 v4 refuses a truthful decoy
  note (exit 1) / v5 admits (exit 0); c2r37-J1 v2 admits a replace-graft clone with a
  forged receipt (exit 0, predicate true) / v3 refuses (exit 2); c2r37-J2 v2 admits an
  observed-tampered receipt (exit 0) / v3 receipt-finds the exact tampered step (exit 1);
  both honest floors pass (v5 exit 0 predicate true; v3 exit 0, admitted 16, survivors 0,
  egress 0).
- Dispatched wave w1 via the inline spawn handoff (`.ufo/waves/round-37/w1.ready`,
  dispatch `.ufo/waves/round-37/w1-dispatch.json`): 34 seats (8 reviewer, 8 executor,
  5 critic, 4 mutation-tester, 3 scribe, 2 scout, 2 connector, 1 simplifier, 1 sentinel),
  Godspeed directive bytes exact from `skill://godspeed/directive.md`. All 34 seats
  produced reports (`.ufo/waves/round-37/w1/<Seat>/report.md`).
- Opened S143 (`https://git-scm.com/docs/git-replace`, 200, 38,351 B, sha256
  `46750b9f…`, 2026-10-27T13:30Z; quote located) and landed the registry row
  (`corpus/SOURCES.md`, row 143, gate-clean).
- Wrote the round lesson (`corpus/lessons/round-37.md`: Gate with the S143 admit and the
  assimilation/quarantine rejects; Mistakes M1 reference-drift, M2 hand-copied-constant,
  M3 surface-mismatch), the SCORECARD round-37 sections and the LOG entry.
- Measured at the integration tip `34ed508c47ca8727450d7f210bc440dadb61f883` with the
  frozen counters (`.ufo/waves/round-37/measure/`): both predicates TRUE; no-harm 28 legs
  exit 0; numstat and census-end receipts committed (`f485cce`).

## Landed changes

- `99437d29de036415a9f2d0524343617a3b19988a` — frozen claims, C1 v5 + C2 v3 counters,
  build tool v2, harness v2, ten control receipts (LOG round-37 freeze entry).
- `f76da094f0ff0ad9856d2232858241e3f7841379` — validated w1 spec, dispatch payload,
  ready handoff (`gen-w1-spec.py` is re-runnable evidence).
- `34ed508c47ca8727450d7f210bc440dadb61f883` — w1 seat evidence (34 reports), S143 row,
  round-37 lesson, SCORECARD round-37 sections, LOG entry.
- `5a2ebb6af9cbfe024c4a98d483dfe476a02e59f1` — measurement receipts at the integration tip.
- `f485cce10c8640eda64f5e555f99894ed4de7fb0` — end-of-round census receipt (exit 0).

## Before → after measurements

- **C1** — counting command
  `node .ufo/waves/round-37/counters/c1-adjacency-sweep-v5.mjs --rev <REV> --repo <clean clone> --fleet /home/vgpnk/Projects/shokunin --json`
  (measured at `34ed508c…`, counters from the freeze):
  before — v4 admits semantically-identical unfrozen pins (c1r37-J1-v4: exit 0,
  predicate true), refuses a truthful decoy-token moved note (c1r37-J2-v4: exit 1),
  build-tool kama pin 39 hex, predicate sentence not byte-identical;
  after — predicate **true** at the measured REV (unaccounted 0, drift auditCoverage
  307/307, auditFindings 0, staleFindings 0, delta unaccounted 0, screenFindings 0, pins
  digest `81019362…` bound), reordered-pins fixture refused exit 2, decoy-note fixture
  admitted exit 0, build tool v2 regenerates the ledger byte-identical with 20/20 pins
  resolving, one sentence byte-identical at its three sites. Verdict: **met**; adjacency
  held 8 → 8 (metric moved; no rubric authorizes an automatic bump — rounds 35–36
  discipline).
- **C2** — counting command
  `node .ufo/waves/round-37/counters/c2-firefox-bidi-v3.mjs --rev <REV> --repo <clean clone> --json`
  (measured at `34ed508c…`):
  before — v2 admits a replace-graft clone with a forged receipt (c2r37-J1-v2: exit 0,
  predicate true) and an observed-tampered receipt (c2r37-J2-v2: exit 0), no survivor
  check, harness wrote numstat to a stale path and invoked check-freshness outside its
  contract;
  after — predicate **true** at the measured REV (admitted 16, failing 0, survivors 0,
  egress 0, receiptFinding null, binding null), replace-graft refused exit 2,
  observed-tamper receipt-found exit 1, sentence byte-identical, harness v2 numstat +
  freshness legs green. Verdict: **met**; operability held 9 → 9 (recorded ceiling).

## Sources & frontier

Census before → after (frozen command
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tabi`):

- Round start: exit 0, 142 rows, tiers A:126/B:7/C:9, mined 118, queued 15, rejected 9,
  20 pre-existing W04 warnings (`.ufo/waves/round-37/baseline/census-start.txt`).
- Round end: exit 0, `tabi ok`, 143 rows, tiers A:127/B:7/C:9, mined 119
  (`.ufo/waves/round-37/measure/census-end.txt`).

Rows added: **1** (S143, tier A, mined, opened 2026-10-27, used-by the C2 v3 counter).
Rows touched old→new: none (no existing cell changed). Frontier rows advanced: S143 is new
this round. Assimilation: none — ScoutAssim found no staged `merge/tabi/` theme touching
the claim surfaces; the quarantine slice stays refused from rounds 22–23 verdicts
(re-counted, nothing adopted). No `considerthese/` directory exists in the lane.

## Trend verdicts

- **expansion: unchanged** — no new knowledge entry; one registry row grounds the C2
  instrument (instrument ground, not new domain coverage).
- **quality: improved** — all eight round-36 routed defects land as frozen amendments with
  red controls; the v4/v2 exit-0 attack receipts (unfrozen pins, decoy note, replace
  graft, observed tamper) become v5/v3 refusals/findings on the same fixtures.
- **discernment: unchanged** — no outside non-author admit/reject spot-check at filing;
  dispatched seats do not qualify (the lesson Gate records the S143 admit + the
  assimilation/quarantine rejects for the closure spot-check).

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md:697` approval table, §Evidence ladder, §Runbook; rounds 32–36 BiDi decision rows; verifiers were lane-dispatched (orchestrator ruling, kaika round 1).
- [~] At least one end-to-end domain task executed and logged in LOG.md — `corpus/knowledge/multi-step-journey.md` §1–§2 (LOG round-3 entry); rounds 32–36 add the BiDi runtime evidence chain (LOG rounds 32–36).
- [~] Instructions executable by an agent without oral context — `corpus/knowledge/executor-test-sufficiency.md` §0/§4 (verdict SUFFICIENT; executor was a lane seat).
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md:3-19`; refusal routes held (round-36 C1 maps sibling browser ground to tabi without absorbing it; ConnPattern this round reports, never absorbs).

## Stale-lane

Respawn-per-round driver; no other mission of this lane is open.

## Round shape, waves and conformance notes

- Shape: two v1 waves planned (build 32–64 + falsify 32–64, band 64–128 total).
- **w1: 34 seats dispatched** (31 at 10:34:54, 3 deferred on the fleet job cap, complete
  at 10:35:16 local); **34/34 reports on disk**; 18 seats returned `VERDICT ok`, 16
  returned finding-grade verdicts (residual/limit documentation: e.g. the v5 list-mode
  pins read is display-only; the survivor-mutation test gap; builder F1/F2 advisories —
  all named in the w1 reports).
- **w2 was NOT dispatched** (conformance defect, honestly reported): the orchestrator
  held w1 unsettled at filing time — all 34 seat reports are on disk but one seat process
  (LabratC1) remained alive, so WAVE-DONE w1 and `w1-results.json` were not delivered;
  the L1 was budget-force-stopped. The validated w2 spec generator is committed at
  `.ufo/waves/round-37/gen-w2-spec.py` (34 falsify items, one per w1 seat); the falsify
  wave and the 64-seat floor pass to round 37's closure/retry. Per the run-9 lesson the
  L1 did not file before WAVE-DONE for a *dispatched-but-unsettled* wave knowingly —
  this report discloses the settle-pending state instead of claiming w1 closure; no w2
  `.ready` was written.
- Dead seats: none observed (34/34 reports); one seat (ExecPinsBinding) was nudged to
  finalize and did so.
- Tool installs: none (no pacman transaction; no uv/npx installs).
- L0 questions: none open.
- Fresh-start: not applicable (round 36 was admitted; this is run-10 round 2 for tabi).

## Misroot sweep

`git status --porcelain` at the fleet root shows only other lanes' untracked files
(`.scratch/closure-mado-r50.json`, `.ufo/reports/round-53/tameshi.md`,
`.ufo/reports/round-56/mori.md`) — no tabi writes; nothing copied or deleted. No `.ready`
rewrite; one `.ready` per wave.

## No-harm

At `34ed508c` (vs baseline `ed8ccfc`): 28 of 29 no-harm legs exit 0 including all gate
self-tests; `check-selfassessment` mismatches 0; census exit 0. The two nonzeros:
`check-frontier-admission` exit 1 — pre-existing at the baseline (RevNoHarm verified);
and the retired r35-c1 counter leg reads exit 1 (predicate requires its round-35
newMapped quota, honestly stopped at 0) — **reproduced at the round-start baseline
`ed8ccfc` in a scratch clone** (exit 1, unaccounted 0, screenFindings []), so it is
pre-existing, not introduced. v4/v2 still admit the honest state (r36c1/r36c2 exit 0).
`diff ed8ccfc..f485cce --numstat` shows appends only across the append-only files plus
the one registry-row insert (10-line numstat receipt committed).
