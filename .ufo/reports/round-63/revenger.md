# revenger — round 63 report (hyaku, attempt 1)

Lane HEAD (pushed): `a6f5c42145200d4c12510c5b0a6927c0111340b6` (main; clean, ahead=0).
Claim-measured revision: `f6ea293255d9263be24a8f100e8a5ad7490f26fa` (the revision
`reports/round-63/measure-after.log` was run against; later commits are
evidence/docs only). No inherited uncommitted round-63 work existed at launch.

## Work performed

Declared claims (frozen `reports/round-63/claims.md` @ `54ab973c`):

- **C1 — coverage K** (lowest criterion, 4.3): one independently gated new
  entry on C06 archives, K 6/14 → ≥7/14. Admitted:
  `corpus/knowledge/round-63-zip-central-directory-evidence.md` (sha256
  `b2660e60…e0086`) — byte-derived central-directory readout of the authored
  `archive-r2/fixture.zip` vs `truth.json` and the saved record, every value
  derived in-entry (Q11), scoped to one fixture. Evidence: 32-seat build wave +
  32-seat falsify wave (`.ufo/waves/round-63/`); named fresh-seat decisions:
  `W2AttackEntryQ01` PASS, `W2AttackEntryQ11` PASS (exact-hash + transition
  confirms), `W2AttackEntryScope` CLEAN, `W2AttackEntryIndependence` HOLDS,
  `W2SpotcheckDiscern` ADMIT-AGREE; adversary `W2ClaimsAdmission` NOT-FALSIFIED.
- **C2 — coverage F**: first firmware saved record from an authored inert
  known-truth fixture (`corpus/fixtures/firmware-r63/`, generator reproduces
  bytes), one real `npx -y rea-agents@6.5.0 inspect-firmware-regions` run
  (`corpus/live/runs/round-63/`, Evidence `ev_aae7529f…`, receipt, oracle
  `ORACLE OK`), F 4/8 → 5/8. Seat `W2VerifyC2Record` verified all three claim
  conditions incl. recomputing the Evidence ID from the shipped 6.5.0 package.
- **C3 — calibration** (round-61 routed debt): attributed forged-receipt kill
  on `verify_named_multi_icon_states.py` + `verify_icon_states.py`
  (`receipt_ok` + one in-script control each), 0/2 → 2/2 attributed. Seats
  `R63MutC3` (mutant bytes byte-identical to the frozen counter's own
  `mutate_c3()`), `W2MutC3Final`, `W2VerifyC3Patches` reproduced the kills.

Round shape: **v1 two waves, 64 seats total** (32 build + 32 falsify), both
validated under policy v1 (band 32–64) and each dispatched as exactly ONE task
call; zero dead seats, zero replacements; §3 L2 floor inside wave 1
(connector, 8 executors, 6 scribes, 3 scouts, 6 reviewers, 4 critics,
mutation-tester, sentinel, revenger, simplifier; L1 holds the planner seat).
Residual/follow-up work ran as messages to existing seats (round-62 pattern),
not new spawns.

## Landed changes

All via `scripts/hyaku/jj-lane.sh`, lane identity `revenger-shokunin
<revenger@shokunin.local>`:

- `54ab973c` — frozen claims + counting probe + red-before/do-nothing control.
- `2a34e455` — firmware fixture, saved record + receipt + oracle + LEDGER, C3
  patches, wave-1 evidence (`corpus/fixtures/firmware-r63`,
  `corpus/live/runs/round-63`, 2 verifier edits, `.ufo/waves/round-63/`).
- `db55bd64` — C1 candidate entry + S032/S033 + round-63 lesson (README still
  partial).
- `aaa04632` — corrected entry (H1–H7/N1–N3), S034/S035 rows, LEDGER
  receipt-pin fix (`…b`→`…d`), lesson updates.
- `3af3acb`, `34cfa243`, `f6c618ba` — final entry micro-fixes (wc-w 8→7,
  template tokens, embedded-row landed state), lesson Gate gaps closed.
- `f6ea2932` — README C06 `partial → held` (one line; names only the new
  entry).
- `98ad3a0c`, `aaa1790a`, `a6f5c421` — measure-after.log, final-verification,
  SCORECARD/LOG, wave-2 receipts, routed-debt table. Routed debt (13-item
  table `.ufo/waves/round-63/falsify/routed-debt.md` at the cited HEAD, 79
  pointers verified): frozen-counter semantics (K backed-regex prefix false
  positive, F presence-only, C3 attribution-string weakness, HOLDS_OK drift —
  probe frozen, fixes route to a later registered counter, next unused id
  S036); M35 both `stdout_sha256` conjuncts; C07 frontier-token legend
  staleness (cannot fix under frozen void conditions); evidence-ID transplant
  corollary (no committed check binds a receipt/Evidence ID to origin — Q09
  disclaimers carried, owner unassigned); round-58/59 PASS-count quotes (139)
  not reproducing after the C3 patch (142) — historical records left unedited,
  disclosed; freshness hold proves byte survival, not current-host truth.

LOG.md round-63 entries carry the narrative; every change above ties to one.

## Before → after measurements

Frozen counter `python3 -B reports/round-63/measure.py TREE` over `git archive
<commit> corpus`, cwd=/ (probe sha256 `3b7fba2d…`, frozen at pre-registration):

- C1: `K_HELD_BACKED` **6/14 → 7/14** (score 4.3 → 5.0), `K_ROW C06
  status=partial → held`. Before: `measure-before.log` @ base `55bcb6e`;
  after: `measure-after.log` @ `f6ea2932`. Counting command identical both ends.
- C2: `F_COVERAGE` **4/8 → 5/8** (5.0 → 6.2), `F_FAMILIES` gains `firmware`
  (exactly one `inspect_firmware_regions` record). Same command.
- C3: `C3_RECEIPT_KILLED_ATTRIBUTED` **0/2 → 2/2** (red-before: both frozen
  mutants exit 0 at base; after: both exit non-zero, last line `forged
  receipt`). Same command.
- Holds: C2 2/2 attributed, d2 2/2, controls 2/2, `HOLD_CALIBRATION 4/4`,
  `HOLD_REPLAY 10/10`, `FRESH_ROWS 18/18`, `HOLDS_OK=yes`, probe exit 0 at both
  ends. Causal separability re-verified on the final tip
  (`W2VerifySeparabilityFinal`).

## Sources & frontier

Census command: `scripts/sources-census.sh validate --root
/home/vgpnk/Projects/shokunin revenger` — **exit 0 at round start and round
end**. Rows **31 → 35** (`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'
corpus/SOURCES.md`): +S032 (PKWARE APPNOTE 6.3.10, tier A, opened this round),
+S033 (own-work archive bytes/record), +S034 (scoped APPNOTE re-open for
§4.3.7 local-header layout — a fourth disclosed W04 same-URL-different-scope,
intentional), +S035 (own-work ledger). Status flips queued→mined logged
old→new in the lesson; no old row content edited. Frontier: mistake M33 mined
(stale fixture premise, red-before = L1 binwalk pre-probe), M34
(counter-substitution, runnable falsifier = `W2AttackProbeK` do-nothing
receipts), M35 (both `stdout_sha256` conjuncts unguarded — routed, not
claimed). C1 is the sourced claim (rests on S032/S034 opened this round).
Search-log reconciliation and the sibling-count divergence are recorded, not
smoothed (`corpus/lessons/round-63.md`).

## Trend verdicts

- **expansion: improved** — one admitted sourced entry on previously-partial
  C06 ground plus the first firmware saved record; K 6/14→7/14 and F 4/8→5/8
  re-measured by L1 and independent seats.
- **quality: improved** — M33/M34/M35 mined with runnable red-befores; every
  admitted count re-derived by named fresh seats; two false printed values
  (wc-w, receipt pin) caught and corrected before admission; no admitted entry
  failed its re-check.
- **discernment: improved** — the in-lane admit/reject spot-check
  (`W2SpotcheckDiscern`) agrees on both samples with reasons; the falsify wave
  independently re-opened S032's source (byte-identical re-fetch) and both new
  rows; inherited round-61/62 disagreements are dispositioned in-lesson. The
  required non-author closure spot-check remains the integrator's duty.

## SHONEN

- [ ] SKILL.md decision tables/cited sources — still absent; no fresh verifier
  this round (round-62 routed debt stands).
- [~] End-to-end domain task — fixture-scoped saved-ledger replay only
  (`measure-after.log`, `W2VerifyC2Record` real-run verification); pointer:
  `reports/round-63/measure-after.log`.
- [~] Executable by an agent without oral context — lane-root CLI in README +
  frozen probe; no outside instruction verifier this round.
- [~] No cross-domain bleed — `W2ConnectorOverlap`/`W2MisrootSweep` clean;
  ADJ-06 remains reported-not-absorbed; no outside verifier this round.

**Stale-lane:** respawn-per-round driver; no other mission open.
**Tool installs:** none by L1 or any seat (binwalk 3.1.0, unblob 26.6.4,
npx/node, python3 already present; pacman paused host-wide, no transactions).

**Round total:** 64 seats across two validated waves (32+32), 0 dead, 0
residual calls; 3 claims all met at the measured revision; open L0 questions:
none.
