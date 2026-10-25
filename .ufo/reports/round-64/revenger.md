# revenger — round 64 report (hyaku, attempt 1)

Lane HEAD (pushed): `add65837d82750303ba57c059ab424f48fc8b268` (main; clean, ahead=0).
Claim-measured revision: `782bd020c65ea4287382c5ffd8dfbd24ef25f76d` (the revision
`reports/round-64/measure-after.log` was run against; later commits are
evidence/docs only). No inherited uncommitted round-64 work existed at launch.

## Work performed

Declared claims (frozen `reports/round-64/claims.md` @ `3bb430f9`, one
pre-measurement amendment of the HOLDS_OK_V2 diagnostic wording @ `671e3a18`,
recorded in the lesson):

- **C1 — coverage K** (lowest criterion, 5.0): one independently gated admitted
  entry on C07 firmware, K 7/14 → ≥8/14. Admitted:
  `corpus/knowledge/round-64-firmware-region-byte-evidence.md` (sha256
  `9bf21e50…e0ebf`) — blind byte-derived readout of the authored
  `fixtures/firmware-r63/firmware-r63.bin` (padding spans, zlib members at
  512/1024, decompressed digests; complement-first padding rule; 25-oracle /
  13-record correspondence with recorded-vs-derived splits) against the saved
  round-63 record (observation layer; Q09 disclaimers; cross-lane ADJ-06 fence).
  Fresh-seat admission decisions on landed bytes: Q01+Q02 PASS
  (`R64ReviewEntryQ01`), Q03 PASS (`R64ReviewEntryScope`), Q06 PASS
  (`R64ReviewEntryQ06`), Q09 PASS ×6 (`R64ReviewEntryQ09`), Q10 PASS
  (`R64ReviewEntryScope` delta), Q11 PASS (`R64ReviewEntryQ11`), 24/24 in-entry
  commands re-run MATCH (`R64EntryCommands`), recheck mutation kill attributed
  (`R64MutEntry`). Routed input discharged: C07 legend staleness repaired
  (`frontier → held` with the Gate decision in the same revision).
- **C2 — calibration** (round-63 M35 routed debt): attributed forged-stdout kill
  on `verify_icon_languages.py` (`a2fd347e…`) + `verify_multi_icon_states.py`
  (`9345cb8c…`), one in-script control each (6 insertions/0 deletions;
  existing controls retained), `C4_RECEIPT_KILLED_ATTRIBUTED` 0/2 → 2/2.
  Verified by `R64MutC4` (frozen mutants), `R64ReviewC4Lang`/`R64ReviewC4Multi`
  (PASS), `R64MutIcon` (C2/C3 regression), `R64MutProbe` (attribution
  integrity: loose messages rejected), `R64SimplifierDrift` (minimality).
  Mid-wave hazard caught and repaired: the first languages patch replaced an
  existing control (self-test green, C2 regressed 1/2) — flagged by
  `R64ReviewC4Lang`/`R64CriticHarms`, restored by L1, re-verified on final bytes.
- Frontier step (inside the claim cap): S036 (REA firmware guide, pinned tag
  `rea-agents-6.5.0`, snapshot `e422b481…`, re-fetch byte-identical) + S037
  (own-work bundle) opened and landed mined; M36 mined (token-vs-legend drift;
  fix = the registered `README_TOKEN_LEGEND_MISMATCH` counter label, shown able
  to fail with value 1 at base); C1 is the sourced claim (S036/S037).
- Routed inputs dispositioned (full table `corpus/lessons/round-64.md`):
  frozen-counter semantics → this round's probe registers `K_HELD_BACKED_STRICT`,
  `README_TOKEN_LEGEND_MISMATCH`, `HOLDS_OK_V2` (routed fix registered, not
  scored); transplant corollary owner named (`R64RevengerLedger` 6-prong check,
  attack: self-consistent receipt re-signing with ID reuse); r58/59 139→142
  quotes non-reproduction receipt (`R64ScoutHistory`), historical files
  unedited; freshness wording frozen in the contract; SHONEN box 1: SKILL.md
  landed (39098 B, `bfd92057…`), named non-author verifier `R64ReviewSkill`
  re-stated `[x]`-ready = YES on final bytes, checklists executed
  (`R64ExecSkillRun`).

Round shape: **one v2 wave, exactly 64 seats** (operator override), validated
under policy v2 (band 64–128, `plan` exit 0, `dispatch.calls == 1`) and
dispatched as exactly ONE task call; attack roles 41/64 = 64% (reviewer 16,
critic 9, mutation-tester 6, scout 10); role mix: connector 1, executor 11,
scribe 8, scout 10, reviewer 16, critic 9, mutation-tester 6, sentinel 1,
revenger 1, simplifier 1; §3 L2 floor inside the wave; L1 holds the planner
seat (validator rejects planner as a swarm role). First dispatch attempt
exceeded the single-message output limit; fixed by moving seat briefs into
committed lane files and re-validating — one validated wave, one task call.
Dead seats: 1 — `R64CriticC4` (provider cyber-policy flag on the m_sol route;
error text recorded in the lesson; its attack angle covered by
R64MutC4/R64MutProbe/R64CriticCounter). Zero residual calls; all corrections
and re-reviews ran as messages to existing identities (round-62/63 pattern).
Round total: 64.

## Landed changes

All via `scripts/hyaku/jj-lane.sh`, lane identity `revenger-shokunin
<revenger@shokunin.local>`:

- `3bb430f9` — frozen claims + counting probe + red-before do-nothing control.
- `a3d063f2` — validated v2 wave spec, 64 seat briefs, validator plan.
- `671e3a18` — C4 patches, C07 candidate entry, S036/S037 rows, lesson,
  claims V2 wording amendment, wave build evidence.
- `8c27f1b2` — corrected entry bytes (Q11 re-review PASS).
- `cab8085a` — C1 admission: README C07 `held` + Gate decision; SKILL.md;
  all re-review reports.
- `782bd020` — S036/S037 registry placement fix (census E12 caught by the
  census-after gate).
- `add65837` — final measurement, SCORECARD/LOG/SHONEN, cohort receipt.

LOG.md round-64 entries carry the narrative; every change ties to one.

## Before → after measurements

Frozen counter `python3 -B reports/round-64/measure.py TREE` over `git archive
<commit> corpus`, cwd=/ (probe sha256 `b8e68d32…`, frozen at pre-registration):

- C1: `K_HELD_BACKED` **7/14 → 8/14** (score 5.0 → 5.7), `K_ROW C07
  status=frontier → held`. Before: `measure-before.log` @ base `666ea84b`;
  after: `measure-after.log` @ measured revision `782bd020`. Same command both
  ends; independent reproduction of the red-before byte-identical
  (`R64LabDoNothing`).
- C2: `C4_RECEIPT_KILLED_ATTRIBUTED` **0/2 → 2/2** (both frozen mutants exit 0
  at base; exit non-zero, last line ending `forged receipt stdout accepted`,
  after). Same command.
- Holds/v2 diagnostics: `K_HELD_BACKED_STRICT` 7/14 → 8/14 (equals BACKED both
  ends); `README_TOKEN_LEGEND_MISMATCH` **1 → 0**; `C2/C3` attributed 2/2 → 2/2;
  `HOLD_CALIBRATION` 4/4, `HOLD_REPLAY` 10/10, `FRESH_ROWS` 18/18,
  `F_COVERAGE` 5/8 — all unchanged; `HOLDS_OK=yes` and `HOLDS_OK_V2=yes`,
  probe exit 0 at the measured revision. Causal separability proven on the
  frozen counter (`R64ReviewSeparability`, 17 runs over 19 trees).
- Preservation: 452/452 files under `corpus/live` + `corpus/fixtures`
  byte-identical to the wave-start manifest.

## Sources & frontier

Census command: `scripts/sources-census.sh validate --root
/home/vgpnk/Projects/shokunin revenger` — **exit 0 at round start and round
end** (an E12 placement defect introduced at the append was caught by the
round-end gate and fixed before landing; final exit 0). Rows **35 → 37**
(`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'`): +S036 (REA
firmware-analysis guide, pinned tag, tier A route-scope only; the round-63
zipfile-docs note reconciled as first-use-wins), +S037 (own-work firmware-r63
bundle). Status flips queued→mined logged old→new in the lesson; no old row
edited. Frontier: M36 mined; mistake sweep for "no mistake" not needed. C1 is
the round's sourced claim (S036 opened and re-fetched byte-identical by a
non-opener seat).

## Trend verdicts

- **expansion: improved** — one admitted sourced entry on previously-`frontier`
  C07 ground; K 7/14 → 8/14 re-measured by L1 and independent seats; record
  substrate (round-63) re-verified end-to-end (`R64ReviewRecord`).
- **quality: improved** — M36 mined with a runnable fix shown failing at base;
  every admitted count re-derived by named seats; two false printed claims
  (Unblob sentence; derived-vs-recorded counts) and one patch defect caught
  pre-admission and corrected with preserved history; no admitted entry failed
  re-check.
- **discernment: improved** — the in-lane admit/reject spot-checks ran on both
  claims (Q09/Q11 FAIL → corrected → PASS; critic counter-spoof exhibits
  reproduced and dispositioned); routed debt named with owners. The required
  non-author outside closure remains the integrator's duty.

## SHONEN

- [x] SKILL.md decision tables/cited sources — landed (39098 B, `bfd92057…`);
  named non-author verifier `revenger-r64.R64ReviewSkill`: `[x]`-ready = YES
  re-stated on final bytes (`.ufo/waves/round-64/R64ReviewSkill.md`); 0 phantom
  citations (`R64ReviewSkillCites`); executed verbatim (`R64ExecSkillRun`).
- [~] End-to-end domain task — `measure-after.log`; record verification
  `R64ReviewRecord`; no producer rerun this round.
- [~] Executable without oral context — `R64ExecSkillRun` transcript (census
  4/4, replay 10/10, oracle ORACLE OK, counter exit 0); no outside verifier.
- [~] No cross-domain bleed — entry cross-lane note + README parenthetical;
  `R64ConnectorOverlap`; ADJ-06 reported-not-absorbed; no outside verifier.

**Stale-lane:** respawn-per-round driver; no other mission open.
**Tool installs:** none by L1 or any seat (pacman paused host-wide, no
transactions; host binwalk 3.1.0 / unblob 26.6.4 already present and matching
the pinned REA requirements per `R64ScoutHost`).

**Round total:** 64 seats, one validated v2 wave, one task call, 1 dead seat
(recorded), 0 residual calls; 2 claims both met at the measured revision
`782bd020`; open L0 questions: none.
