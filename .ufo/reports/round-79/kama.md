# kama round 79 — lane report

Lane: kama. Round: 79 (attempt 1). Base `ee53f1a25eab93a8ab55bbb877e49e2e731df535`; freeze
`331037039c30909aa2163b2d1de22a7964f90420` (the claims plan and the C1 counter). Sealed revision
C1 grades: `7a3cd98243b69fcbee0cc9e31878782bd8459320` (round 78's tip). Claim receipts measured at
`5ac1a8dd94b151548b5d5a6256938da381366e20`; the scored gate at
`b756571e435f3dda5697f8aa2eddd37abcb51797`. Final lane tip (remote-verified below):
`a9b4543f14625d0f37daa42ef664ee6f6ea975ea`. Assigned axes: operability + calibration
(`shokunin.conf`).

Round shape: ONE v1 wave of **14 seats** under `ufo-wave-policy.json` (band 8–16): 4 executor,
3 scribe, 2 scout, 1 connector, 1 reviewer, 2 critic, 1 mutation-tester; attack 4/14 = 29 %.
**11 of 14 seats returned output**; 3 returned empty and are recorded dead. No residual call;
round total 14.

## Work performed

Declared claims (frozen in `plans/round-79-claims.md` before any seat or counter produced data):

- **C1 — calibration** (lowest assigned axis, 7): six declared facts of the round-78 self-record
  re-derive at the sealed revision, or are answered by dated value-bound corrections.
- **C2 — operability**: the pre-report gate composes the three round-78 instrument selftests as
  its own arm, fail-closed on a red, malformed or absent instrument.
- **C3 — coverage**: the probe's `listeners` census names an unregistered serving listener as its
  own class, without admitting a registry row.

Work items:

- **C1 counter.** `tools/round79-selfrecord-round78.py`: `PREDICATE` is the plan's blockquote
  verbatim; six facts (F1 lowest-axis, F2 population, F3 wave shape, F4 dead seats, F5 tip
  accounting, F6 pre-correction receipt) read from `git show <sealed>:…`; corrections graded from
  `corpus/lessons/round-79.md` §Corrections (backticked bullet shape), each `new` value re-derived
  at the tip; nine selftest arms. Pre-freeze `SELFRECORD_R78_ENUM claims=6 stale=2 corrected=0`,
  exit 1 (`measured/before/c1-enum.out`). Evidence: `measured/after/c1-green.out`,
  `measured/after/c1-selftest.out` (`pass=9 fail=0`).
- **C1 corrections (two).** F5: the record calls ancestor `rev=22cce544` "the tip accounting";
  the sealed tip is `7a3cd982`. F6: the record says the pre-correction run is "in the lesson"
  while no committed blob under `.ufo/waves/round-78/` carries `mismatches=1`; the run was
  reproduced from the pre-fix module at `fa65ce2c` and committed
  (`measured/v2/c1-pre-correction.out`: `SELFRECORD_R77 claims=6 mismatches=1 corrected=4
  unbacked=0`, `EXIT=1`). Evidence: `corpus/lessons/round-79.md` §Corrections.
- **C2 arm.** `tools/pre-report-gate.py` gains arm 10 `round78-instruments`, running the three
  round-78 instrument selftests, each required to end with its own `<NAME>_SELFTEST pass=N
  fail=0`; absent → `missing <script>`, red or malformed → FAIL naming the instrument.
  `PREDICATE`, the docstring arm list and the `arms=` history text updated; four new selftest
  cases (red stub, absent module, green stubs, malformed summary) move the tally 22 → 26;
  `SKILL.md`'s pre-report-gate registry row re-anchored to ten arms / `pass=26` /
  `round78-instruments`. Evidence: `measured/after/c2-selftest.out`,
  `measured/after/c2-gate.out`.
- **C3 class.** `tools/kama-probe.sh listeners` appends a `registered` column (`yes`/`no`/`-`)
  and `governed`/`unregistered`/`registry` summary keys; registry declared ports are read
  tolerantly (an unreadable registry leaves `-` with a warning, never a probe error).
  `tools/round79-unregistered-census.py` starts the pinned `llama-b11755` child on a free
  unregistered loopback port, writes two scratch registries and grades the same listener both
  ways with `--port`, so no host listener enters the counts; four selftest arms plus a
  non-gating live-host leg. Evidence: `measured/after/c3-census.out`,
  `measured/after/c3-selftest.out` (`pass=4 fail=0`), control `measured/control/c3-base-probe.out`
  (`class_missing=1`, exit 1).
- **Frontier.** S553 admitted (llama.cpp router `GET /models` at `39febd2a`, HTTP 200, 135608
  bytes, sha256 `8fd5abde…`, 16-word located quote at line 2227); the INI-preset candidate
  (`docs/preset.md`, sha256 `3e664354…`) rejected with its flip; one knowledge entry
  (`unregistered-listener-census`) and its coverage-map row; KQ130 and KQ131 added from the
  round's three mined mistakes. Evidence: `corpus/SOURCES.md` S553 row,
  `corpus/lessons/round-79.md` §Gate/§Mistakes, `corpus/QUALITY.md`.
- **Round-78 routed defects.** V1 (tip receipts) — the gate receipt names `b756571` and the
  round-77 register counter is re-run at the tip (`measured/v1/registers-tip.out`). V2 — the
  pre-correction receipt is committed (above). V3 — `round78-selfrecord-round77.py --selftest`
  re-run at the tip (`measured/v3/c1-selftest.out`, `pass=8 fail=0`). V4 — the round-78 register
  counter re-run at the tip with `APPEND_REGISTERS_OUT_OF_POPULATION rows=1`
  (`measured/v4/c2-tip.out`). V5 — closed by supersession (round-78 receipts stay history; the
  round-79 C3 receipt carries its revision). V6/V7 — recorded as plan/report precision defects
  with the real controls named (`SCORECARD.md` §Round 79 §Routed defects).
- **Domain observation (not a claim).** Eight model-API listeners answer outside the registry at
  the measured revision (`127.0.0.1:1234` router with four LFM3 ids; broker ports `8788`, `8789`,
  `8790`, `8791`, `8793`, `8795`), and the count moved between two census legs
  (`model_endpoints` 8 → 9) — the reason the graded legs use `--port`. Evidence:
  `measured/after/c3-census.out` (`UNREGISTERED_CENSUS_LIVE`).
- **Wave integration.** MT01Mutation built five mutants and killed all five on the committed
  bytes (probe class ×3, gate arm ×2; its graded hashes equal the commit `5ac1a8d` bytes).
  EX01C1Facts' independent harness and SCT01Recon's hand derivations agree with all six C1 value
  strings, including F5/F6 stale. SCT02Source/SC01Sources confirmed the quote (16 words, line
  2227) and flagged the anchor's "Router mode" as a region label; the lesson's Gate carries the
  correction and the S479/S037 distinction. CN01Connector found no composed-selftest overlap and
  named two vocabulary/scope adjacencies (mado's `CHECK96 unregistered=`, kengaku's S178). RV01,
  CR01 and CR02 ran against the mid-flight tree and certify nothing. Evidence:
  `.ufo/waves/round-79/w1/` and `w1-results.json`.
- **Misroot sweep.** `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows only
  orchestrator-owned `.scratch/*`, sibling reports, `after` and `agent:/`; no kama round-79 seat
  file landed at the fleet root, so nothing was copied or deleted.

## Landed changes

Every change ties to the LOG §Round 79 entry (`LOG.md:3213`) and to the commit that carries it;
wave evidence is committed under `.ufo/waves/round-79/`.

| Change | Commit |
|---|---|
| Freeze: claims plan, C1 counter, pre-freeze receipts, census before | `3310370` |
| Wave 1 spec, dispatch (14 seats, attack 4/14) and ready handoff | `f7442de` |
| Lesson (three mined mistakes, two corrections), S553, census entry, coverage row, pre-correction receipt | `d6408a6` |
| C1/C2/C3 implementations, SCORECARD §Round 79, LOG, SKILL row, PROVINCE note, KQ130 | `5ac1a8d` |
| Claim receipts at `5ac1a8d`; filed lesson bytes restored + appended Gate correction | `9100605` |
| SCORECARD self-description repairs (planned section, retired/saturation/closure pointers) | `b574397` |
| Evidence hashes re-anchored at the round-79 tree | `f4a35f6` |
| Register-counter red disclosed; R78V6 plan paths named without the `measured/` prefix | `1cda045` |
| Wave evidence (seat outputs, dispatched marker) and the tip register-counter receipt | `1f82cc3` |
| Accepted-history rows added for the round's in-place edits (reverted as invalid, next row) | `078253d` |
| Register restored; the 38 post-introduction rows reverted | `5785cdf` |
| Disclosure ledger rows added (reverted: post-introduction), then restored | `c6ec06f`, `6fb6885` |
| Wave results and the settled seat reports | `b756571` |
| C2 honest stop recorded, mistake 3, KQ131, wave/dead-seat record, scanned gate receipt | `4af44f7` |
| Round-78 selftest receipts restored (dirtied by the gate's arm 10) and the defect routed | `a9b4543` |

Remote check: `git ls-remote origin refs/heads/master` →
`a9b4543f14625d0f37daa42ef664ee6f6ea975ea`, equal to local `master`.

## Before → after measurements

| Claim | Counting command (both sides) | Before | After | Measured revision |
|---|---|---|---|---|
| C1 calibration | `python3 tools/round79-selfrecord-round78.py --repo .` (before: `--enumerate`; control: `--tip 3310370…`) | exit 1 `SELFRECORD_R78_ENUM claims=6 stale=2 corrected=0` (`measured/before/c1-enum.out`); control exit 0-targeting run exit 1 `claims=6 mismatches=2 corrected=0` (`measured/control/c1-no-corrections.out`) | exit 0 `SELFRECORD_R78 claims=6 mismatches=0 corrected=2 unbacked=0` (`measured/after/c1-green.out`) — **VERIFIED** | `5ac1a8d` |
| C2 operability | `python3 tools/pre-report-gate.py --selftest`; `python3 tools/pre-report-gate.py --repo . --round 79 --tip master` | `ARM_ORDER` 9 arms, `PRE_REPORT_SELFTEST pass=22 fail=0` (`measured/before/c2-gate-arms.out`) | `PRE_REPORT_SELFTEST pass=26 fail=0` (`measured/after/c2-selftest.out`) and arm 10 green, but the scored line is `PRE_REPORT round=79 arms=10 failed=1 uncommitted=0` (`measured/after/c2-gate.out`) — **NOT VERIFIED (honest stop)**: inherited arm 8 `round75-instruments` is red on this round's own in-place edits (`APPEND_ACCEPTED unaccepted=5`) | `5ac1a8d` (selftest); `b756571` (gate) |
| C3 coverage | `python3 tools/round79-unregistered-census.py --repo .` (control: `--probe <base probe>`) | no class; base probe scored `class_missing=1`, exit 1 (`measured/control/c3-base-probe.out`) | exit 0 `UNREGISTERED_CENSUS port=<p> unregistered=1 governed=1 class_missing=0` (`measured/after/c3-census.out`) — **VERIFIED** | `5ac1a8d` |

Selftests: `SELFRECORD_R78_SELFTEST pass=9 fail=0`, `PRE_REPORT_SELFTEST pass=26 fail=0`,
`UNREGISTERED_CENSUS_SELFTEST pass=4 fail=0`. Controls that skip the claimed work are committed
(`measured/control/`, `measured/before/`). Freeze divergences are recorded in `SCORECARD.md`
§Round 79 and not rewritten: C3's legs first used a host-wide summary delta, then `--port` after
the host gained a listener mid-run (predicate, target and value strings unchanged).

## Sources & frontier

Rows before → after, same command both times
(`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh census --file corpus/SOURCES.md`, exit 0):

| Measure | Before (`3310370`) | After (`5ac1a8d`) |
|---|---|---|
| rows | 292 | 293 |
| tier A / B / C | 277 / 11 / 4 | 278 / 11 / 4 |
| status mined / queued / rejected | 263 / 8 / 21 | 264 / 8 / 21 |

Rows added by tier: **A 1** (S553, docs). Rows touched old→new (`status`/`recheck`/`used-by`):
**none**. Frontier rows advanced: S553 (router `GET /models` list semantics) into the coverage map
via `corpus/knowledge/unregistered-listener-census.md`; S553's scope is distinct from S479's
router model-listing code at the older pin and S037's `is_ready` ordering, and the three llama.cpp
pins (`engine-pins.tsv` b11755, kengaku S178 b7200, S553 `39febd2a`) are a recorded divergence.
Registry validate: `sources-census.sh validate --root /home/vgpnk/Projects/shokunin kama` → exit 0
(W04 duplicate-URL warnings only, all pre-existing). Rejected: `docs/preset.md` at the same commit
(HTTP 200, 4090 bytes, sha256 `3e664354…`) — the class reads the model list only and the probe
parses no preset; flip recorded in `corpus/lessons/round-79.md` §Gate. Assimilation: none this
round (`considerthese/2026-10-26.md` proposal 3 is already carried by KQ129; no other proposal was
mined and no `merge/kama/` entry fits the census class).

## Trend verdicts

- **expansion — improved.** One admitted entry on coverage-map ground the lane did not hold
  (`unregistered-listener-census`, `source: S553`, coverage row), a new source kind for this
  ground (router docs at a pinned build), and three capability rows demonstrated running
  (`selfrecord-round78`, `gate-arm-composition`, `unregistered-census`). Bound: one entry, one
  row, no package assimilation.
- **quality — improved, with a named regression.** Two stale self-descriptions repaired and
  re-derived; the gate now executes the three round-78 instruments at every scored run; the three
  claim controls are red on the base and committed; three mistakes mined into KQ130/KQ131. Bound:
  C2's scored gate is red on arm 8 because this round's own in-place record edits cannot be
  accounted by the lane's pre-introduction ledgers, and the round-77 register counter is red on
  the same events (disclosed, not hidden).
- **discernment — unchanged.** Two grounded criteria were added from the round's own mistakes, but
  no non-author spot-check exists yet; the closure's outside leg is what can move this verdict.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources → author evidence: `SKILL.md` §Decision table / §Error signatures / §Checklist; the pre-report-gate row now names arm 10 and `pass=26`; no named non-author verifier.
- [~] At least one end-to-end domain task executed and logged in LOG.md → `LOG.md` §Round 79 records the three claims' end-to-end runs (probe census with a live pinned child, gate with the round's own instruments); no non-author mark.
- [~] Instructions executable by an agent without oral context → `SKILL.md` §Checklist and `plans/round-79-claims.md` carry the commands verbatim; independent execution review remains open.
- [~] No cross-domain bleed (PROVINCE.md still accurate) → `PROVINCE.md` §Round-79 note and `corpus/knowledge/cross-lane-scope.md`; mado's `unregistered=` vocabulary collision and kengaku's shared listener are reported, not absorbed.

## Honest limits and open items

- **C2 is an honest stop.** The frozen target's second leg (`failed=0`) is not met:
  `PRE_REPORT round=79 arms=10 failed=1 uncommitted=0` at `b756571`, with arm 10 green and arm 8
  `round75-instruments` red (`APPEND_ACCEPTED events=58 accepted=53 unaccepted=5 bad_rows=0`).
  The five events are this round's own in-place edits; the accepted register and the disclosure
  ledger both refuse a commit at or after their introduction, and the register-restore event
  cannot be held without re-introducing 38 invalid rows. The target is not narrowed; the closure
  rules.
- **Round-77 register counter red at the tip** (`measured/v1/registers-tip.out`: `unaccounted=5`,
  the same population), disclosed in `SCORECARD.md` §Round 79 and mined as mistake 3.
- **Instrument hygiene defect routed:** `tools/round78-live-reconcile.py --selftest` writes its
  receipt into `.ufo/waves/round-78/measured/after/`, so every scored gate dirties two tracked
  files after its cleanliness arm passed. The bytes were restored; the fix (write under
  `TMPDIR`/`--scratch`) is round 80's, because changing an instrument after the measured gate
  would move the gate receipt's binding.
- **Gate receipt revision.** The gate ran at `b756571`; the delta to this record's tip touches
  record paths and the restored round-78 receipts only.
- **Stale-lane line.** Respawn-per-round driver; no other mission of this lane is open.
- **Open L0 questions.** None opened. The long-standing axes mismatch (`MISSION.md:29` operability
  + freshness vs `shokunin.conf` operability + calibration) remains open as filed.
- **Tool installs.** None (pacman stayed paused; no install or upgrade was needed).
