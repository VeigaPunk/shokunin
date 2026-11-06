# kama — round 90 report

L1 `KamaR90` (also holds the §3 planner seat). Lane repo `kama-shokunin`, branch `master`. Base
`99cdb4d6270455494dd27901efe84a0f3b342062` (round 89 admitted, `corpus/lessons/round-89-verifier-spotcheck.md`).
Final lane hash **`db247186b43e66f399cf277f13aa8748676cd90d`**. `git ls-remote origin refs/heads/master` prints it;
`jj-lane.sh state` → `ahead=0 behind=0 tracked=0 untracked=0`. Attempt 1; no earlier attempt
(`.ufo/watchdog.log` has no `lane-dead-no-report kama round=90`).

## Work performed

Declared claims (frozen at `6f6d7873dac936ba407398ce81b464d77d0fcf32`, `plans/round-90-claims.md`):

- **C1, operability** (lane axis; sourced S587, S588). Hostile listener answers stay bounded and cannot break
  probe output. Capability `hostile-answer-bounds`. This works routed r89 R4 (SN01 F3/F4).
- **C2, depth** (lowest-scoring axis, tied at 7). The probe's reason codes become a `SKILL.md` table, each row
  bound to a captured probe answer. Capability `probe-reason-table`.

Work items:

- Closure history was read before declaring: the r89 spot-check (admitted, R1–R5) and the r88 spot-check
  (rejected: a canned expectation copied from prose). Both counters grade observed output only.
- Pre-freeze controls were executed and committed with the freeze (`6f6d7873`, `.ufo/waves/round-90/controls/`):
  - C1 base: `mismatches=8 positive_mismatches=0`, exit 1 (`c1-base.out:14-15`).
  - C1 forgeries: F1 blanket refusal `6/5`, F2 over-sanitizer `9/1`, F3 64 KiB cap `7/1`, all exit 1
    (`c1-f1-blanket-refusal.out`, `c1-f2-over-sanitizer.out`, `c1-f3-tiny-cap.out`).
  - C2 base: `documented=0 missing=23`, exit 1 (`c2-base.out:24-25`).
  - C2 forgery battery: `rows=5 bound=2 unbound=3 duplicates=1`; stale receipt `bound=0`; prose-only table
    `documented=23 bound=0 unbound=23`; all exit 1 (`c2-forgeries.out`).
  - Harm baselines: `harm-base-probe-verdicts.out` 77/77, `harm-base-test-snapshot.out` 30/0,
    `harm-base-r89-cells.out` 11/0/0, `harm-base-operator-1234.out` `MODEL_OK router-unloaded-autoload`.
- C1 implementation `f968fb19` in `tools/kama-probe.sh`:
  - `curl --max-filesize 4194304` on `fetch`, `router_autoload` and `probe_short`, plus a written-size re-check.
  - rc 63 → `FOREIGN_SERVICE body-too-large`.
  - `jstr` escapes U+0001–U+001F and DEL.
  - `served_ids` prints C0/DEL/C1 controls as `\uXXXX` text.
  - `strip_ctl` on the `Server:`/`Content-Type` headers, curl error text and `probe_short`.
- C1 wave-1 repair `a09effae`. Wave seats RV01 (reviewer) and EX03 (executor) found four defects at M:
  - a router entry whose id held a control character was dropped. A `loading` router then read
    `MODEL_OK` for a wildcard consumer, where base gave `MODEL_LOADING`. This was held-out harm.
  - a non-UTF-8 `Server:` byte made `--json` exit 1;
  - a 401 response with an oversize body was graded `FOREIGN_SERVICE`;
  - the grep fallback passed raw control bytes.

  All four are repaired at `a09effae`. Re-run: `.ufo/waves/round-90/repair/rv01-matrix-base-M-Mprime.out`.
- C2: added SKILL §"Probe reason codes" (24 rows) at `2ee0b55f`. The receipt producer is
  `tools/round90-reason-capture.py` (24 stub cells), receipt `measured/reason-cells.jsonl`. A second run was
  byte-identical. After the C1 repair the receipt was re-captured and the RV02 prose corrections applied
  (`1f8eed67`); only the probe hash changed in the re-capture.
- Frontier step:
  - Knowledge entry `corpus/knowledge/probe-answer-bounds.md` (cites S587–S591).
  - SOURCES rows S587–S591.
  - QUALITY criterion KQ145 (a sanitizer escapes the item, never drops it).
  - Lesson `corpus/lessons/round-90.md`: Gate block plus mistakes M1–M5.
  - README round-90 coverage section, PROVINCE round-90 paragraph, LOG §Round 90, SCORECARD §Round 90,
    §Planned (round 91), capability rows, head banner.
- Pre-report gate: `measured/gate-final.out` → `PRE_REPORT round=90 arms=14 failed=1 uncommitted=0`. The one
  failing arm is the carried `round75-instruments` arm (R1, `bad_rows=19`, L0 still open).

## Landed changes

All commits landed through `jj-lane.sh` and are tied to LOG.md §"Round 90 — 2026-11-06":

| Hash | Change |
|---|---|
| `6f6d7873dac936ba407398ce81b464d77d0fcf32` | freeze: plan, both counters, every control receipt |
| `f968fb19bb2a0c2afe271bfe606f11b52d10823f` | C1 probe change (M) |
| `2ee0b55f4d3fd0cb3157d26b03280c1d21e27b2d` | C2 SKILL table, capture tool, receipt; C1 measured at M (M2) |
| `a09effae1f3780797a4d706f469a1d2b33361aa4` | C1 wave-1 repair (M′) + repair matrix |
| `1f8eed67def8ebf2e8a5ac4cb34ef7f50bc330f4` | C2 receipt re-captured at M′, SKILL prose fixes; C1 final receipts (M2′) |
| `8f8211a2d9218115af82488e7e9ee7aeadddc08e` | record: SCORECARD, knowledge entry, SOURCES S587–S591, KQ145, lesson, LOG, README |
| `f1b12a20673313f2f623fddb136e0220810e446b` | wave-1 evidence (13 seat reports + out dirs, results.json), PROVINCE |
| `8213ed0ac0088f2620d27e136a1931baa5e08c42` | SCORECARD saturation and retired lines |
| `546cb40c7e9e6db24ff2cb92675badf342238c0f` | SCORECARD head banner (round 90) |
| `d45ede25de1f1c1405911dbabb53284f111fba93` | tip re-measurements of C1/C2, census-end |
| `db247186b43e66f399cf277f13aa8748676cd90d` | terminal gate receipt (final lane hash) |

## Before → after measurements

| Claim | Counting command | Before (base `99cdb4d6`) | After (measured commit) |
|---|---|---|---|
| C1 operability | `python3 tools/round90-hostile-answers.py --repo . --rev <R> --work <scratch>` | `HOSTILE_ANSWERS cells=13 mismatches=8 positive_mismatches=0 probe=rev`, exit 1 (`controls/c1-base.out`) | M `f968fb19`: `cells=13 mismatches=0 positive_mismatches=0 probe=rev`, exit 0 (`measured/c1.out`). M′ `a09effae`: same, exit 0 (`measured/c1-final.out`). Tip `546cb40c`: same (`measured/c1-tip.out`). Counter sha256 `345b12b3…` equals freeze (`measured/c1-counter-hash.out`). |
| C2 depth | `python3 tools/round90-reason-rows.py --repo . --rev <R>` | `REASON_ROWS population=23 documented=0 rows=0 … missing=23`, exit 1 (`controls/c2-base.out`) | M2 `2ee0b55f`: `documented=23 rows=24 bound=24 unbound=0 missing=0 duplicates=0 additional=1`, exit 0 (`measured/c2.out`). M2′ `1f8eed67`: same (`measured/c2-final.out`). Tip: same (`measured/c2-tip.out`). Counter sha256 `fa4c3177…` equals freeze. |

Harm (C1 K2), base → M′ (`measured/harm-final.out`), all unchanged:

- `tests/probe-verdicts/check.py` 77/77.
- `tools/test-snapshot.sh` 30/0.
- `round89-unloadable-cells` 11/0/0.
- Operator router 1234 (GET only): `MODEL_OK router-unloaded-autoload`.

Held-out cells:

- EX01 at M: FIX 6 / AGREE 6 / HARM 0 / LIMIT 2 (`w1/EX01HeldOutCells.md`).
- The RV01 harm rows at M are repaired at M′. In the M′ re-run, every row that differs from base is either a
  base defect or the declared oversize-`/props` rule (`repair/rv01-matrix-base-M-Mprime.out`).

My verdicts as author:

- **C1** meets its predicate at M, but it is **not clean at M**: three held-out harm rows. It is clean at M′,
  which is the final measured commit. This follows the r89 precedent: a repaired M′ was measured and admitted.
  I leave the ruling to the closure.
- **C2** meets its predicate at M2 and M2′.

## Sources & frontier

Census command: `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kama`.

- Start: exit 0, `kama ok` (`controls/census-start.out`).
- End: exit 0, `kama ok` (`measured/census-end.out`). The only non-W04 warning is the pre-existing W01 on S481.

Registry rows, base → tip (awk over `corpus/SOURCES.md` registry rows):

| | Before | After |
|---|---|---|
| rows | 326 | 331 |
| tier A | 311 | 315 |
| tier B | 11 | 11 |
| tier C | 4 | 5 |
| mined | 291 | 295 |
| queued | 8 | 8 |
| rejected | 27 | 28 |

Rows added this round:

- Tier A, mined: S587 curl `max-filesize.md` @ `curl-8_23_0`; S588 RFC 8259 §7; S589 RFC 8259 §8.1;
  S590 curl `lib/sendf.c` @ `curl-8_23_0`.
- Tier C, rejected: S591 curl `max-filesize.d` @ `curl-8_3_0`, with a flip condition.

Every row was opened this round. S589–S591 were found by scout SC01 and re-opened by me, with sha256 matching
the seat's values. Gate block: `corpus/lessons/round-90.md` `## Gate` (≥1 admit, 1 reject). No existing row
changed `status`, `recheck` or `used-by`.

- Frontier advanced: the probe's answer boundary moved from frontier to core (README "Coverage and frontier —
  round 90").
- Sourced claim: C1 rests on S587/S588 (also S589/S590). The entry `probe-answer-bounds.md` cites them.
- Mined mistakes (`round-90.md` `## Mistakes`):
  - M1: a non-discriminating counter cell, caught by the base control.
  - M2: a broken stub, caught by the positive cells.
  - M3: a miscounted control label.
  - M4: a sanitizer that dropped items and changed the verdict. Captured-by: the held-out rule. Fix: KQ145.
  - M5: a new branch ordered before the auth branch, plus a header that let non-UTF-8 through.

  Each mistake names an evidence pointer and a fix shown able to fail.
- Assimilation: none. considerthese: not mined this round. The `2026-11-06.md` proposals target calibration
  gauges, not this round's claims.

## Trend verdicts

- **expansion: improved.** A new knowledge entry covers ground the lane did not hold. The KQ143 sweep found
  one prior-art hit (`snapshot-history.md:51`, the snapshot path only), cited in the entry. Four new A-tier
  rows, and two capabilities entered the table.
- **quality: improved.** Three base defects are fixed with failing-before controls: a 64 MiB answer graded
  `MODEL_OK`, unparseable `--json` on control bytes, and table column forging. The wave-found M harm was
  repaired in-round and re-run. Limits are disclosed (CR01/MT01: the counter certifies the property, not the
  named implementation; SN01: no time bound).
- **discernment: unprovable-but-better.** One reject (S591) and four admits went through re-opening.
  KQ145 came from a wave disagreement. No non-author spot-check exists yet, so this is not marked improved.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources → author assertion: `SKILL.md` §"Probe reason codes" (24 rows bound to captured probe answers, `measured/c2-final.out`); `corpus/knowledge/probe-answer-bounds.md` decision rows (S587–S590); no named non-author verifier.
- [~] At least one end-to-end domain task executed and logged in LOG.md → author assertion: `LOG.md` §Round 90; probe exercised against 13 + 24 stub listeners and live lane-owned b12177 router children (`measured/harm-final.out`); no non-author mark.
- [~] Instructions executable by an agent without oral context → author assertion: seats RV02/MT02 re-ran the capture and counter unaided, byte-identical (`w1/RV02ReasonTable.md`); seats are the lane, not non-authors.
- [~] No cross-domain bleed (PROVINCE.md still accurate) → author assertion: `PROVINCE.md` round-90 paragraph; `w1/CN01SiblingOverlap.md` found corroboration only (chousa/kotodama/kagi body caps, souji/tameshi control-character refusal), no contested scope.

## Round shape and seats

- Shape: one v1 wave under `ufo-wave-policy.json` (band 8–16), dispatched through the inline handoff
  (`.ufo/waves/round-90/w1.ready` → `w1.ready.dispatched` → `w1-results.json`, WAVE-DONE received). No residual
  call. Round total: **13 seats**.
- Role mix: reviewer 2, critic 2, mutation-tester 2, executor 3, sentinel 1, scout 1, connector 1, scribe 1.
  Attack share is 6/13 (46 %). The §3 planner seat is held by the L1; the validator rejects `planner` as a
  swarm role.
- Dead seats: 0. All 13 settled with reports in `.ufo/waves/round-90/w1/`.
- Answering models: not recorded in `w1-results.json` (r88 D4 class, still open). Routes are as the run-15
  amendment-46 map assigns them.
- Each seat's verdict:

| Seat | Verdict | Main finding |
|---|---|---|
| RV01 | falsified (at M) | harm, repaired |
| RV02 | holds | 4 prose defects, fixed |
| CR01 | partial | counter forgeable by a 1 MiB-cap probe; `sent` proxy time-truncated |
| CR02 | holds | counter is a form judge; 14 new codes + 4 new mappings |
| MT01 | partial | 8/13 killed |
| MT02 | holds | 8/8 killed |
| EX01 | holds | HARM 0 |
| EX02 | holds | harm unchanged; ≤10 % latency |
| EX03 | partial | python-free path, fixed |
| SN01 | partial | no time bound, present at base |
| SC01 | holds | |
| CN01 | holds | |
| SB01 | drafts | used as input |

## Limits, L0, misroots, other

- The C1 counter is satisfied by other implementations: a 1 MiB cap, a probe without `jstr`'s loop, or rc 63
  mapped to `DEAD` all score 0/0. The wire bound needs curl ≥ 8.4.0. The answer boundary has no time bound:
  207 s for a 4 MiB answer of 200k ids, present at base. The C2 counter binds hidden or blank rows and any
  receipt with the right probe hash. All of these are routed to SCORECARD §Planned (round 91).
- Gate `round75-instruments` is red (R1, `bad_rows=19`, carried since r87). The L0 question at
  `.ufo/l0-questions.md:381` is still open. No new L0 question this round.
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows only orchestrator-owned
  `.scratch/` entries. None are mine, and none were touched.
- Scratch `/fast/scratch/hyaku/kama-r90/` was removed.
- Tool installs: none.
- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
