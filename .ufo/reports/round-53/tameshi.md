# Tameshi round 53 — cold-read floor repair (calibration, honest stop) + tools scratch hygiene (operability, verified)

L1 TameshiR53a2, hyaku run 10, attempt 2 (attempt 1 died at its first model call
on a provider quota limit; nothing inherited). Lane base `6db1d220` (round-52
closure salvage). Freeze `7d8aaac6` (amendments 1–7, all before the data they
govern; `.ufo/evidence/round-53/freeze.json`). Final lane revision: see the
`jj-lane.sh` push check below (branch `master`).

## Work performed

Claims (frozen at `e62d9971`, contract `.ufo/evidence/round-53/contract.json`):

- **C1 (calibration — the round-52 closure's harmed axis):** re-key the cold-read
  sections the round left credit-lost (19 inherited R52.1 + 11 drifted by this
  round's own C2 edits = 30 frozen headings) and restore the frozen floor to
  64/64 GREEN. **Verdict: honest stop — 58/64** (`credited=58 lost=6` on the
  frozen monitor at the final revision `88afa941`; `.ufo/evidence/round-53/`
  receipts). 28 of 30 sections re-keyed, trace-bound to 30 fresh reader reports
  across three read revisions (C* `a41195df`, C4 `a977394`, C5 `651773ab`),
  inputs pinned at C7 `8f474419`; `## Standing rules` and `### Using the ledger`
  forfeited (their genuine reader findings were fixed at C6 `7c10fa7`, but the
  fresh re-read their re-key requires could not land before budget); four
  collateral sections the round's own edits drifted (`### The boundaries`,
  `### The operator's runbook — …`, `### Round-14 historical registry`,
  `### Round-26 gate/probe registry`) carry stale read-revision shas. Before →
  after: 45 → 58 credited.
- **C2 (operability):** every `dir="/tmp"` hardcode under `tools/` now honours
  TMPDIR via a strict scratch-root helper in 7 tools (a set-but-unusable TMPDIR
  is could-not-evaluate, never a silent `/tmp` fallback — the frozen counter's
  CR47 arm caught the first fix's gettempdir() fallback; the helper repaired
  it), selftests pass under redirected TMPDIR, registry-check's selftest scratch
  failure maps to exit 2, and SKILL.md names no stale /tmp invocation.
  **Verdict: verified** — the frozen counter printed `C2_R53_PASS=true`
  (`tmp_hits=0`, `registry_selftest=PASS`, `envdiff_selftest=9/9`, `cr47=rc=2`,
  `docs=ok`) at every candidate from C** on, including the final revision.

Work items (evidence): freeze + controls 2/2 as pre-registered
(`control/controls.stdout`, `a36d3e51`); fix pass 1 `218bc6b5`; assimilation
S275/S276 with both sources re-opened by the L1 this round (snapshots + quotes
`.ufo/evidence/round-53/assimilation/`, mirror census exit 0 before append,
renumber S161/S162 → S275/S276); considerthese proposal 1 mined as
`verify-freeze.sh` (executed, `FREEZE_INTEGRITY: OK`); fix pass 2 `5b703c6f`;
wave 1 (44 seats: 30 readers + 14 specialists) and wave 2 (40 seats: 21
re-readers + 19 attack/audit); residual re-reads w2r/w2r2/w2r3 (7 seats); two
QUALITY-104-class falsities fixed at C6; round-15 verifier re-pin at C7 (R52.5
class, seat T53W1ExecRegCheck); re-key across `rekey-r53-*`; phase-A controls
and L1 adjudications `integrate/resolutions.json` (5 over-reach adjudications,
evidence-backed, all disclosed). No tool installs (host tools sufficed; pacman
guard respected).

## Landed changes

Every change above is committed via `jj-lane.sh` and tied to LOG.md's round-53
entry (commits `cf872769` … `88afa941`, listed in `git log`); the wave specs,
dispatches, results and seat reports are committed under
`.ufo/waves/round-53/`; the counters, controls and receipts under
`.ufo/evidence/round-53/`.

## Before → after measurements

- C1: `bash .ufo/evidence/round-48/quality/coldread-precheck.sh LANE ef19d8e1 REV`
  — base `6db1d220`: `cand_credited=45 lost=19 RED`; candidate `218bc6b5`:
  `34/64 lost=30`; final `88afa941`: `credited=58 lost=6` (frozen monitor via
  `.ufo/evidence/round-21/coldread/measure.py`). Counting command:
  `python3 .ufo/evidence/round-53/c1/measure.py --lane LANE --rev REV --work EMPTY`.
  Target `cand_credited=64` not reached — reported, not narrowed.
- C2: `python3 .ufo/evidence/round-53/c2/measure.py --lane LANE --rev REV --work EMPTY`
  — base: `C2_R53_PASS=false` (2 hits + docs); final: `C2_R53_PASS=true`
  (receipt quoted above; probes at `5b703c6f` and the final revision).
  Do-nothing controls false at base for both counters (phase A 2/2).

## Sources & frontier

Census before: exit 0, 134 rows (`census-start.*`); after: exit 0, 136 rows
(S275, S276 appended; mid and end checks both clean). Rows added by tier: A ×2
(S275 Change-Aware Mutation Testing, camera-ready, DOI 10.1145/3540250.3558911;
S276 Long-Standing Mutants, arXiv 2212.11762). Rows touched: none besides the
append + bookkeeping line. Frontier: F7 gains its first sourced policy ground
(`corpus/knowledge/change-aware-resweep-cadence.md`, `corpus/README.md`
round-53 note) — the F7 row stays open (classification unmeasured).
Assimilation: one theme, one entry admitted, 85 deferred (capacity, flip named
in the lesson's Gate). considerthese: proposal 1 mined (verify-freeze.sh);
2–5 deferred.

## Trend verdicts

- expansion: **unchanged** — S275/S276 mined into one entry on existing F7
  ground; no new capability or coverage surface.
- quality: **improved** — 45 → 58 credited sections; 21+12+3 reader findings
  fixed; two QUALITY-104 falsities corrected; 7 tools' scratch semantics
  repaired; the round's own two false claims (dash-form boundary, skipped-count
  bracket) were caught by wave-2/residual readers and fixed, not smoothed.
- discernment: **improved** — every reader finding adjudicated in writing
  (`integrate/resolutions.json`, 5 over-reach with evidence, fixed ones
  committed); the two sections whose findings could not be re-read this round
  were forfeited rather than falsely recorded at zero.

## SHONEN

- [~] SKILL.md decision tables/cited sources — unchanged this round; evidence `SHONEN.md:5-8`, no promotion claimed.
- [~] End-to-end domain task logged — round-53 entry `LOG.md`; no promotion claimed.
- [~] Executable without oral context — the round-53 instruments run from frozen bytes; no independent verifier.
- [~] No cross-domain bleed — PROVINCE boundary held (sibling lanes read-only; overlaps reported by T53W1ConnOverlap/T53W2ConnSources).

Stale-lane: respawn-per-round driver; no other lane mission is open.
L0 questions: none new this round.
Tool installs: none.
Waves: w1 44 seats (30 scribe-readers, 4 executors, 2 reviewers, 2 critics,
2 scouts, 1 connector, 1 mutation-tester), w2 40 seats (23 scribes, 6
reviewers, 4 critics, 2 executors, 3 scouts, 1 mutation-tester, 1 connector),
w2r/w2r2/w2r3 residual 7 seats; planner seat held by the L1 (validator-frozen
topology). Dead/straggler seats: wave-1 specialists ExecR523/ExecTmpVerify and
wave-2 specialists landed late or were superseded by later fixes; their
reports are committed and audited in wave 2 where still relevant. Round total:
44 + 40 + 7 = 91 seats (band 64–128; the three residual waves are the §6
residual calls). The deciding-run.sh orchestration was not executed before
budget exhaustion; the frozen counters were run directly at the final revision
and quote the honest C1 stop above.
