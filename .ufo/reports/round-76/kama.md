# kama — round 76 report

Lane repo `kama-shokunin`, branch `master`. Base `b06cc612711560c53eef3ec21484c6963601262f`,
freeze `1a85a991fce5b76b60f88a5cab3df98d253b1a4a`, final lane tip
`fd4b9ca3042e2233d7cb9850fff3e3d750435e78` (remote-verified). Report date 2026-11-04.

## Work performed

Round 76 declared three claims, one per axis: **C1 operability** — the round-75 self-record's
citation population is classified under a declared fence scope (fenced bytes are quoted history,
not citations) and record-path scope (self-description deltas do not shift a receipt), capability
`receipt-scope`; **C2 calibration** — the round-75 self-record's eight declared facts either
re-derive at the revision they name or are superseded by an appended correction whose stated
value itself re-derives, capability `selfrecord-facts`; **C3 freshness** — every append-only
audit event is accounted for exactly once and the introduction cutoff cannot be re-opened,
capability `append-exempt-class`. Verdicts: **C2 verified; C1 and C3 honest misses** on frozen
targets that are unsatisfiable as written (the measurements that prove it precede any green run
and are committed).

- **C1 instrument and scope decision.** `tools/round76-receipt-scope.py` composes the frozen
  round-72/73 readers, reuses the audit's CommonMark §4.5 fence reader and the declared
  record-path set (round-72 defaults plus `PROVINCE.md`, `SKILL.md`, `corpus/**`), and prints one
  `RECEIPT_SCOPE` line plus named `RECEIPT_SCOPE_UNBOUND` findings; seven selftest arms including
  `fence-none-live` and `fence-unclosed` (both exit 2) and `shift-tools` (exit 1). Measured after
  line: `RECEIPT_SCOPE round=75 fenced_quoted=1 live_citations=11 bound=6 unbound=2 shifted=3
  nonreceipt=0 unclassified=0`, exit 1 — evidence
  `.ufo/waves/round-76/measured/after/receipt-scope.out:3`, before exit 2 at
  `.ufo/waves/round-76/measured/before/c1-receipt-claim.out:3`. The frozen target was
  `bound=9 shifted=0`; the three before receipts are shifted by `registry/append-only-contract.tsv`
  at `b8ed2568`, a non-record delta the freeze's control did not enumerate
  (`.ufo/waves/round-76/measured/before/c1-fence-dryrun.out`).
- **C2 instrument and repairs.** `tools/round76-selfrecord-facts.py` grades eight facts over ten
  checks from committed blobs, accepts a correction only when its stated value re-derives, and
  carries five arms. Five corrections landed (PROVINCE digest, LOG work tip, LOG mistake count,
  LOG unbacked gate tally, calibration closure pointer) plus the `## Axes` re-anchor. After:
  `SELFRECORD_FACTS claims=8 mismatches=0 corrected=5 unbacked=0`, exit 0 —
  `.ufo/waves/round-76/measured/after/selfrecord-facts.out:3`; before
  `.ufo/waves/round-76/measured/before/c2-facts.out:3`.
- **C3 instrument, register and honest accounting.** `tools/round76-append-exempt.py` accounts
  every audit event once across the line-bound accepted register, a strict exempt-head class
  register (`registry/append-only-exempt.tsv`, 47 rows), restoration and disclosure, and
  preserves the two-register introduction cutoff; six arms including `audit-fixture-baseline`
  (the real data, exit 1) and `rotation-reintroduced` (exit 1). After:
  `APPEND_EXEMPT events=233 register=53 exempt=47 restored=91 disclosed=5 unaccounted=37
  cutoff=10f37171fb696c542586cbee96ea4a509ab74afc introductions=2 rotation_safe=1`, exit 1 —
  `.ufo/waves/round-76/measured/after/append-exempt.out:3`; before audit `events=232 …
  ungraded=83` with the register grading 53 (`measured/before/c3-audit.out:3`,
  `measured/before/c3-register.out:3`). 31 events are wrong-class because the audit's `ungraded`
  bucket also carries A-row/only-prefix carveouts and serializes no class key; 5 postdate the
  earliest register introduction.
- **Gate arm 9.** `tools/pre-report-gate.py` composes the three round-76 counters as arm 9,
  `PRE_REPORT_SELFTEST pass=21 fail=0`
  (`.ufo/waves/round-76/measured/after/gate-selftest.out:3`); final gate verdict
  `PRE_REPORT round=76 arms=9 failed=2 uncommitted=0`, exit 1
  (`.ufo/waves/round-76/measured/after/pre-report-gate.out:12`) — the two reds are exactly the
  C1 and C3 misses, arms 7 and 9.
- **Round-75 closure items 1–7 closed**: PROVINCE digest, work tip and mistake count corrected by
  appended blocks; the gate-selftest practice restored with a committed receipt; the survivor run
  re-captured faithfully (five lines, `.ufo/waves/round-76/measured/after/r75-survivors-recapture.out`);
  coverage-map rows appended for `append-only-accepted-history.md`, `fenced-quotation-scope.md`,
  `selfrecord-fact-binding.md`; three QUALITY criteria for the round-75 `captured-by: none`
  classes (KQ126–KQ128); two round-local Gate rejects recorded. Item 8 is partly closed: the
  scope is decided and armed, but the frozen fence-blind base tool still cannot grade the record
  and the three shifts stand — routed to `### Planned (round 77)` item 1.
- **Frontier.** S498 (CommonMark 0.31.2 §4.5) re-opened live and re-quoted from freshly retained
  bytes; S548 (own-work instrument) opened this round; two duplicate-row candidates rejected
  (CommonMark duplicate of S498, `gitrevisions` duplicate of S070/S082) with reasons and flips in
  `corpus/lessons/round-76.md` §Gate.
- **Mistakes mined** (`corpus/lessons/round-76.md` §Mistakes): `first-finding-freeze` (target
  sized from a control that reports one finding per item), `frozen-target-unsatisfiable` (two
  clauses that cannot both hold), `label-drift` (counter field order vs predicate wording),
  `gate-arm-missing-label` (defect regex vs the new counter's label), each with the fix shown able
  to fail.

## Landed changes

Every change is tied to `LOG.md` §Round 76 and to the commit that carries it:

| Commit | What it carries |
|---|---|
| `1a85a991` | frozen plan `plans/round-76-claims.md`, base receipts, fence dry-run control |
| `c2aa7fb2` | `tools/round76-receipt-scope.py`, `tools/round76-selfrecord-facts.py`, `tools/round76-append-exempt.py`, gate arm 9, `registry/append-only-exempt.tsv` (47 rows), `corpus/SOURCES.md` (+S548), `corpus/QUALITY.md`, `corpus/README.md`, `corpus/knowledge/fenced-quotation-scope.md`, `corpus/knowledge/selfrecord-fact-binding.md`, wave evidence |
| `a3fbc629` | instrument receipts: gate selftest (21), three counter selftests (7/5/6), receipt-scope and append-exempt measured runs, round-75 survivor re-capture |
| `461d2adb` | four appended corrections (PROVINCE digest, work tip, mistake count, unbacked tally) and the `## Axes` closure re-anchor |
| `661622b5` | `SCORECARD.md` §Round 76 (+31-row canonical capability list, §Planned round 77), `LOG.md` §Round 76, `corpus/lessons/round-76.md`, receipts |
| `0e01f32f` | `PROVINCE.md` instrument paragraph, lesson citation repairs, assimilation summary receipt |
| `dc222228` | superseded lesson bytes held verbatim (append-only restoration) |
| `b52b5b79` | record-citation repoint + held cells, head capability mirror to 31 rows, `SC01Recon` report |
| `417bbf81` | saturation list to round 76, value-keyed province-digest correction |
| `6440df9c` | head re-derivation (banner, live-plan pointer, retired count, coverage run fact) |
| `c1ae92d5` | axes re-anchors: operability selftest tally `pass=18` → `pass=21`, `PROVINCE.md` digest and line count after the instrument paragraph |
| `731ef814` | superseded head bytes held verbatim (restoration of the graded banner event) |
| `fd4b9ca3` | pre-report gate receipt (the final tip) |

No change was made outside `kama-shokunin/` except this report (fleet repo). No credential
material, no service start, no endpoint sample, no package install.

## Before → after measurements

| Claim | Counting command | Before | After | Measured commit | Verdict |
|---|---|---|---|---|---|
| C1 | `python3 tools/round76-receipt-scope.py --repo . --round 75` | exit 2, `RECEIPT_CLAIM_V2 CouldNotEvaluate … cited path is not a receipt file (.py): .ufo/waves/round-75/controls/build-spec.py (corpus/lessons/round-75.md:125)` | exit 1, `RECEIPT_SCOPE round=75 fenced_quoted=1 live_citations=11 bound=6 unbound=2 shifted=3 nonreceipt=0 unclassified=0` | `b06cc612` (before) / `c2aa7fb2` (after) | **miss** (frozen target `bound=9 shifted=0`) |
| C2 | `python3 tools/round76-selfrecord-facts.py --repo .` | exit 1, `SELFRECORD_FACTS claims=8 mismatches=5 corrected=0 unbacked=1` | exit 0, `SELFRECORD_FACTS claims=8 mismatches=0 corrected=5 unbacked=0` | `b06cc612` (before) / `461d2adb` (after) | **verified** |
| C3 | `python3 tools/round76-append-exempt.py --repo .` | audit `events=232 restored=91 unrestored=53 ungraded=83 disclosed=5`; accepted register grades 53 | exit 1, `APPEND_EXEMPT events=233 register=53 exempt=47 restored=91 disclosed=5 unaccounted=37 cutoff=10f37171… introductions=2 rotation_safe=1` | `b06cc612` (before) / `c2aa7fb2` (after) | **miss** (frozen target `exempt=83 unaccounted=0 introductions=1`) |

C1 and C3 are reported as misses, not re-worded: both frozen targets are unsatisfiable, the
evidence predates any green run, and no predicate, counter or kill rule was edited after a seat
scored. C2's after value is re-derivable at any later tip because the corrections are
value-keyed.

## Sources & frontier

Counting command (both ends):

```sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kama
```

- **Before** (round start, 287 rows): exit 0, final line `kama ok …/corpus/SOURCES.md`.
- **After** (round end, 288 rows): exit 0, same final line (W04 duplicate-URL warnings only,
  pre-existing).

Rows added by tier: **A +1** (S548, own-work instrument). Rows touched old→new: **S498**
`used-by` gained `corpus/knowledge/fenced-quotation-scope.md` (old: `corpus/lessons/round-50.md`;
new: both), logged here and in the lesson; status and recheck unchanged. No row's status changed.
Rows refused: a CommonMark row drafted as S548 was refused as a duplicate of S498 and a
`gitrevisions(7)` row was refused as a duplicate of S070/S082 — both recorded with reason and
flip in `corpus/lessons/round-76.md` §Gate.

Frontier rows advanced: `corpus/knowledge/fenced-quotation-scope.md` (the citation/audit
boundary between quoted history and live evidence — new ground) and
`corpus/knowledge/selfrecord-fact-binding.md` (revision-bound grading of a round's own facts —
new ground); both indexed in `corpus/README.md`'s coverage map.

Assimilation: **none** — 9 staged-id collisions (S330 S333 S334 S335 S346 S347 S352 S353 S363)
and 7 quarantined payload-absent rows, re-derived read-only with the indentation guard proven
(`.ufo/waves/round-76/assimilation/summary.out`). `considerthese/2026-10-26.md` proposal 2 has a
standing disposition instance in the lesson; the other three proposals are landed.

## Trend verdicts

- **expansion — improved.** Two admitted knowledge entries on ground the coverage map did not
  hold (fence/quotation boundary, revision-bound fact grading), one new tier-A own-work row, and
  three capabilities entering the canonical repertoire (31 rows, `SELFDESC_CANON_V2
  canon_round=76 canon_rows=31`). Bound: one of the two entries rests on an own-work row rather
  than an external source.
- **quality — improved.** Three stale self-record facts and one stale closure pointer now
  re-derive (`mismatches=0 corrected=5`), the gate retains its selftest receipt for the first
  time (`PRE_REPORT_SELFTEST pass=21 fail=0`), five new selftest arms and one gate arm landed,
  and the round-75 survivor capture was restored to a faithful five-line receipt. Bound: the
  record itself needed four repair commits (citation/locator/label drift), disclosed in the
  lesson; two claim targets were wrong at freeze.
- **discernment — unchanged.** No outside non-author spot-check ran for this round, so the
  protocol's own bar ("a subagent the lane dispatched is still the lane") is not met by the
  seats' attacks, however much they overrode the author (EX01 and EX03 refused to tune to their
  frozen targets, CR01 built do-nothing controls, SN01 audited the laundering surface). The
  round-75 closure's eight defects are closed or routed above; nothing is claimed beyond that.

## SHONEN

- `[~]` SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md` §§Decision table, Error signatures, Checklist; no named non-author verifier.
- `[~]` At least one end-to-end domain task executed and logged in LOG.md — `LOG.md` §Round 16 and `.ufo/waves/round-16/live/receipt.json` (live llama.cpp lifecycle, 10/10 checks); round 76 adds lane-local instruments only; no non-author mark.
- `[~]` Instructions executable by an agent without oral context — `SKILL.md` §Checklist plus this round's instrument CLIs and their selftests (`receipt-scope` 7 arms, `selfrecord-facts` 5 arms, `append-exempt` 6 arms); independent execution review remains open.
- `[~]` No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` §Write boundary and the round-76 instrument paragraph; service repair, routing and credentials remain operator/sibling-owned.

## Round shape, seats and totals

One v1 wave (`kama-r76-w1`) of **13 seats** — 3 executor, 3 scribe, 1 scout, 1 connector,
1 revenger, 1 reviewer, 1 critic, 1 mutation-tester, 1 sentinel; attack share 5/13 = 38 %;
one connector (≤2). Spec `.ufo/waves/round-76/w1-spec.json`, validated under
`ufo-wave-policy.json` (band 8–16, `counts.spawn=13`), dispatch
`.ufo/waves/round-76/w1/w1-dispatch.json`, ready `.ufo/waves/round-76/w1.ready` (taken
02:58:52). **Round total: 13 seats, 0 residual calls.** Dead seats: 0 — all 13 seat reports are
committed under `.ufo/waves/round-76/w1/`; the dispatcher's `w1-results.json` and the
`WAVE-DONE` message were not observed at record time (the last seat report landed 03:03, 20
minutes before this report), so the wave is evidenced by the 13 reports, not by that handoff.
The L1 held the canonical planner seat (validator forbids `planner`); a bounded planning
data-walk rode `SC01Recon`. Routing followed `task.agentModelOverrides` (no seat was passed a
model).

## Other required lines

- **Stale-lane:** no — respawn-per-round driver; no other mission of this lane is open.
- **Inherited state:** none. No earlier attempt of round 76 existed (`.ufo/watchdog.log` shows
  `launch kama round=76 … attempt=1`); `.ufo/waves/round-76/` was created by this round.
- **Misroot sweep:** `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows only
  orchestrator-owned `.scratch/*` entries and other lanes' files (`after`, `.ufo/reports/round-80/*`),
  none naming kama or round 76; nothing copied or deleted.
- **Tool installs:** none this round (no `uv`, `npx`, binary or package change).
- **L0 questions:** none filed. The round-35 freshness/MISSION conflict stays open and was
  routed around, not assumed.
- **Wave carry:** round 76 committed 13 lane commits; the pre-report gate ends
  `arms=9 failed=2 uncommitted=0` with arms 7 and 9 naming exactly the C1 and C3 misses.
