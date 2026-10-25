# chousa — round 37 report

Attempt 5 of the round (5 watchdog `lane-dead-no-report chousa round=37` lines, orchestrator
deaths, not refusals). Attempt 4 landed the freeze `b905217a7dfdcf58be1f0a4c0bf5f2d2d32a2d65`
and dispatched wave 1 before dying; attempt 5 inherited its spec/dispatch/8 seat reports,
re-verified them, dispatched the residual falsify call, and landed everything below.
Lane tip at report: `e85ea218deaf7deb6c46721572e71889c359d1b6` (pushed; cited per claim).
Landed gate: `tools/research-gate.sh` SHA-256 `9fcac047ddadd616fcf171534f6e6557f3e68271e353a79d81b218832321cf39`.

## Work performed

Declared claims (frozen at `corpus/evidence/round37/claims.md`, commit `b905217`):

- **C1 — operability** (lowest scored axis, 3/10): a claim's `sha256` revision pin is hashed
  through one pinned absolute `sha256sum` and never through the caller's PATH.
- **C2 — freshness**: a `--pin` baseline is independent of the caller's `BASH_ENV` (the capture
  child runs `env -u BASH_ENV`).

Work items:

- Re-verified the inherited wave-1 evidence (8 of 39 seats returned; 31 dead by orchestrator
  death, never replaced): base re-derivations (`w1/ExecC1BaseRederive.md` 2/7 on seeds
  37101/37123; `w1/ExecC2BaseRederive.md` 3/7 on 37201/37223), landed re-derivations
  (`w1/ExecC1LandedRederive.md` 7/7 on 37111/37133; `w1/ExecC2LandedRederive.md` 7/7 on
  37211/37311), single-hunk gate mutants proving separability (`w1/ExecMutGateC1.md` C1 2/7
  while C2 7/7; `w1/ExecMutGateC2.md` C2 3/7 while C1 7/7), counter-expectation mutants
  (`w1/ExecMutC1Counter.md`, both 6/7 exit 1).
- L1 re-derivation on fresh seeds 37701/37721 with committed receipts
  (`corpus/evidence/round37/receipts/c1-after-s37701.json`, `c2-after-s37721.json`).
- L1 no-harm battery with the recorded commands verbatim: selftest PASS 267 cases 0 skipped;
  claims 17/17 CLEAN; chain 17/22 CLEAN; broken control 1/2 DRIFT; archives
  `VERDICT_BEARING_EXPORTS=3/3`. The wave seat `w1/ExecNoHarmPin.md` ran the battery with
  `--root .` instead of `--root ..` and read the refusals as harm — a lesson mistake
  (QUALITY 53), not gate harm.
- Residual falsify call (one `task` call, 8 seats: 4 reviewer + 4 critic; details in the
  wave section): re-derived both predicates on fresh seeds 41377/52819 (C1) and 38101
  (C2), audited all 14 receipts byte-level, reproduced the no-harm root cause, attacked both
  kill rules (28 C2 vectors; 6 C1 vectors), re-proved separability with a both-reverted
  mutant, and reviewed the frontier against contract v1.
- Frontier: opened S071 (coreutils `env(1)` `-u` semantics, local man page, no network);
  two knowledge entries; lesson `corpus/lessons/round-37.md` (3 mistakes); QUALITY 53-54;
  README r36+r37 index rows; census 70 → 71 rows, validate exit 0 both ends.

## Landed changes

All in lane commit `e85ea218deaf7deb6c46721572e71889c359d1b6`, each tied to a LOG.md entry
(## Round 37):

- `tools/research-gate.sh` C1/C2 fixes, selftest 262-267 — freeze commit `b905217` (inherited,
  re-verified this attempt): the pinned-absolute-sha256sum claim-pin call and the
  `env -u BASH_ENV` capture scrub.
- `corpus/evidence/round37/receipts/` — six after-receipts committed (c1 37901/37921/37701,
  c2 37941/37961/37721), all `predicate_holds=true`, all `gate_sha256=9fcac047…`.
- `corpus/evidence/round37/claims.md` — §Errata 4-6 appended (receipt-audit scoping; C2
  narrowed for `BASH_FUNC_*` function inheritance; C1 falsified beyond PATH-independence via
  unprivileged `LD_PRELOAD`).
- `corpus/knowledge/claim-pin-provenance-r37.md`, `corpus/knowledge/pin-capture-env-r37.md` —
  the two claim notes with provenance trios.
- `corpus/lessons/round-37.md` — 3 mistakes (no-harm mis-invocation; dispatched-vs-returned
  count drift; claim-text overreach), ## Gate with S071 and the census receipt.
- `corpus/QUALITY.md` 53-54; `corpus/README.md` r36+r37 index rows + frontier paragraph;
  `corpus/SOURCES.md` S071 + S068/S070 used-by bindings (old→new logged in the lesson);
  `SCORECARD.md` round-37 verdicts + planned-38; `LOG.md` round-37 entry.
- `.ufo/waves/round-37/` — inherited wave spec/dispatch/registry + 8 seat reports, residual
  call's 7 seat reports (CritNoHarm died on a provider `cyber_policy` refusal; dead seat stays
  dead in the evidence).

## Before → after measurements

- C1 (measured at `b905217` for the before, `e85ea218` for the after):
  `CLAIM_PIN_PROVENANCE_MATCH` **2/7 → 7/7**.
  Command (lane root): `python3 corpus/evidence/round37/c1-count.py --gate tools/research-gate.sh --seed N --receipt F`.
  Before receipt: `corpus/evidence/round37/receipts/c1-base-s37001.json` (base gate
  `a7d3922c…`, re-derived by the wave on seeds 37101/37123). After: committed receipts on
  seeds 37001/37701/37901/37921 + report-only wave runs 37111/37133 + residual runs
  41377/52819 (`residual/RevC1FreshSeed.md`). Residual critic: PATH-only subclaim survives a
  clean control, but unprivileged `LD_PRELOAD` moved verdicts 4/7 (forge) and 3/7 (false
  stale) on the landed gate — claim text falsified beyond PATH-independence (§Erratum 6);
  predicate P1 stands on every committed receipt.
- C2: `PIN_CAPTURE_ENV_MATCH` **3/7 → 7/7**. Same command shape with `c2-count.py`.
  Before: `corpus/evidence/round37/receipts/c2-base-s37021.json` (re-derived 37201/37223).
  After: committed receipts on seeds 37021/37721/37941/37961 + report-only 37211/37311 +
  residual 38101. Residual reviewer: a startup file's `export -f date` reaches the capture
  child through `BASH_FUNC_date%%` and embeds a receipt line with phantom drift — claim text
  narrowed to variable re-export independence (§Erratum 5); predicate P2 stands, and 28
  adjacent vectors otherwise held or confirmed named limits (`residual/CritC2Kill.md`).
- No-harm (after gate, `e85ea218`): claims 17/17, chain 17/22, broken 1/2, archives 3/3,
  selftest 267 cases — commands verbatim in `w1/SentNoHarm.md` lines 22-25 and the SCORECARD
  archive one-liner.

## Sources & frontier

- Census before → after: `sources-census.sh validate --root /home/vgpnk/Projects/shokunin chousa`
  → exit 0 both ends. Before: 70 rows (A 64/B 1/C 5; mined 47/queued 19/rejected 4). After:
  71 rows (A 65/B 1/C 5; mined 48/queued 19/rejected 4), malformed 0, standing W04 ×2
  (S051/S053).
- Rows added: **1** — S071, tier A, `env(1)` `-u`/`--unset` semantics, opened locally from
  `/usr/share/man/man1/env.1.gz` 2026-10-23 (no network); located quote (5 words): "remove
  variable from the environment" (decompressed line 28).
- Rows touched old→new: S068 used-by += `pin-capture-env-r37.md`; S070 used-by +=
  `claim-pin-provenance-r37.md` (both logged in the lesson §Gate; found by the residual
  reviewer as H1 and fixed pre-commit). Draft-time corrections before S071's first commit:
  anchor label `OPTIONS`→`DESCRIPTION, -u option entry`, canonical URL added (reviewer L1/L2).
- Frontier rows advanced: S071 enters `mined` at creation; no recheck changes.
- Sourced claim: **C2** rests on S071 (opened this round; `pin-capture-env-r37.md` cites it
  as the `-u BASH_ENV` mechanism source). C1 additionally cites S070 (round 36).
- Mistakes mined: 3 (lesson ## Mistakes). Rejected source candidates: 2 (recorded in the
  lesson §Gate). Non-author spot-check: pending (the hyaku closure's), marked pending in the
  lesson.

## Trend verdicts

- **expansion: improved** — two new knowledge entries on new measured ground (pin digest
  provenance; capture-environment independence), README index + frontier updated, S071 opened
  and mined.
- **quality: improved** — both gate fixes measured 2/7→7/7 and 3/7→7/7 across six+ seeds and
  three independent runners; selftest 261→267; and the residual wave did real falsification
  work: two claim-text kills caught, named, and frozen as errata with fix directions rather
  than absorbed.
- **discernment: improved** — the lane's first in-round falsifications of its own frozen
  claims (LD_PRELOAD into the pin child; `BASH_FUNC_*` into the capture child), recorded
  honestly with the predicates' standing receipts distinguished from the falsified general
  wordings; QUALITY 54 captures the class.

## SHONEN

- [~] SKILL.md decision tables/error patterns/cited sources — `SKILL.md` Gates table;
  `corpus/knowledge/claim-pin-provenance-r37.md` (lane assertion; no non-author verifier)
- [~] End-to-end domain task executed and logged — LOG.md rounds 9/25/37 batteries (lane
  assertion)
- [~] Instructions executable without oral context — `bash tools/research-gate.sh --selftest`
  (267 cases PASS at `e85ea218`)
- [~] No cross-domain bleed, PROVINCE.md accurate — PROVINCE.md unchanged; zero network;
  residual seats wrote only in-lane (lane assertion)

All boxes remain `[~]`: promotion holds for a non-author review; the hyaku closure's
spot-check is the pending external check.

## Wave shape, seats, residual

- Shape: **v1, two waves declared; wave 2 downgraded to a residual call** — wave 1 returned
  8 reports, yielding fewer than 32 distinct attack items, so per the round contract the
  residuals went into one ordinary `task` call of ≤8 reviewer/critic seats (never pad).
- Wave 1 (inherited dispatch, `w1-dispatch.json`): **39 seats** — roles: executor 10, scout 7,
  reviewer 6, critic 5, mutation-tester 3, sentinel 2, revenger 2, scribe 2, connector 1,
  simplifier 1; planner seat held by the L1 (its data-walk rode the inherited LabSeat-class
  evidence). **8 returned, 31 dead** (orchestrator deaths; never replaced). §3 floor met
  inside it.
- Residual call: **8 seats dispatched, 7 returned, 1 dead** — CritNoHarm, provider
  `cyber_policy` refusal (same class as round 36's CritC1Swap); the L1 had already run that
  battery verbatim. Returned: RevC1FreshSeed (P1 holds, 2 fresh seeds; receipt-binding
  findings F1-F5 named as debt), RevC2FreshSeed (P2 holds on 38101; BASH_FUNC kill; trust
  analysis), RevReceiptAudit (14 receipts clean; doc scoping fixed pre-commit), CritC1Kill
  (**C1 claim text killed** via LD_PRELOAD, C27/C18), CritC2Kill (28 vectors, no in-scope
  kill; five named-limit confirmations; `noexec` false-success witnessed), RevSeparability
  (holds; both-reverted mutant reproduces base exactly; two low findings), RevFrontier
  (NOT CONFORMANT → all findings fixed pre-commit: H1 used-by bindings, M1 quote count, M2
  line pointer, L1/L2 anchor+URL, L4 provenance anchors; L3 README heading structure carried).
- Round total: **47 seats** (39 + 8), within the ≤128 cap.
- Routing: roles through the host route table; no per-seat model pins. Seats' answering
  models not individually recorded (no claim depends on a specific answering model).

## Report extras

- **Stale-lane:** none — respawn-per-round driver; no other mission of this lane is open.
- **Tool installs:** none this round (no seat installed anything; sources opened from installed
  man pages).
- **Inherited state:** attempt 4's freeze commit, wave spec/dispatch, 8 seat reports and
  receipts reused after re-verification (named above); nothing discarded.
- **L0 questions:** none.
- **Operator ruling requested:** the admission is ADMIT-with-errata — both frozen predicates
  verify on every committed receipt and no axis is harmed (both falsified claim-text clauses
  describe defects that pre-exist the round's changes), but the claims as first written do
  not stand; §Errata 5-6 freeze the narrowings and the round-38 fix directions.
