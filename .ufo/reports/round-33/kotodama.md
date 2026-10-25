# kotodama — round 33 report (2026-10-19)

Regimen 2 (`REGIMEN.md`, repo root), loop 1, build 1 of 3. One 64-worker batch
on `opencode-go/deepseek-v4.1-flash` (key 1 of the per-round key round-robin;
observed 64/64 seats completed — `reports/round-33/telemetry/observed-dispatch.json`).
Declared baseline `139e3b662900557afe54f632b468619593dc9fcb`
(`reports/round-33/claims.json:8`). Claims O/C/A on
operability/calibration/adjacency; freshness axis-move claims paused
(`claims.json:18`). Acceptance: `python3 reports/round-33/run-validation.py`
→ `reports/round-33/validation.json` (`acceptance_checks_passed: true` at
close; counting command cited in each claim row).

## Work performed

- **Operability (claim O)** — the round-32 routed operability debt, landed.
  (a) Lessons index reconciled: `corpus/lessons/README.md` revision 3
  (integrator-applied from `op/O02-readme-delta.md`; seven new rows for
  round-26..32 lessons, 29 new open-question queue rows, arithmetic
  corrected; applied bytes SHA-256 `f752e1d79…` byte-equal to the seats'
  verified reconstruction; receipt `op/lessons-reconciliation-receipt.json`).
  Drafted by seats K02/O01-O04, adversarially reviewed by R01-R03. (b) The
  round-32 "falsifier audit filename mismatch (substance 5/5)" debt located
  (F-X16-3): `SKILL.md`'s close-what-you-open one-liner tested a snapshot
  filename that exists nowhere and false-fired on five closed records;
  dispositioned at `op/O05-falsifier-disposition.md` with a content-keyed
  re-key draft, applied by the integrator (now `SKILL.md:724-727`), proven by
  a 7-scenario control harness (`O05 §4`, live OLD 5 rows → NEW 0 rows).
  Scout/executor/reviewer chain: K01/K02, O01-O08, R01-R03.
- **Calibration (claim C)** — the dossier's twelve standing open items
  dispositioned (`calib/open-items-ledger.json`, 12/12 rows; finalized from
  `calib/C15-ledger-draft.json` with integrator flips). Canonicalization by
  K03 with honest count provenance (the numeral "12" is reconstructed, not
  quoted — F-C15-1 carried); per-item seats C01-C12; consistency C13 (green
  for the twelve; re-keys recorded); fix drafts C14 (Fixes 1-4) + C05's
  FD-N4/N5, all applied by the integrator with controls; verifiers R04-R06.
  Four rows flipped fixed-with-evidence (OI-04/05/06/12); eight carried with
  owners, reasons and next touches. Membership ruling F-C13-4 recorded:
  K03's twelve stand; box-4 readings 3a/3b/3c are out-of-set corroboration.
- **Adjacency (claim A)** — the consolidated regimen-2 opening boundary
  audit at `adj/audit-assembled.md`: A01-A14 all verdicts filed (green or
  named-finding with owner), backed by executors A01-A10, verifiers
  A11-A14 (every cited command independently re-run), reviewers R07-R08 and
  the connector X00. PROVINCE accuracy re-verified at HEAD (`c53782a`,
  sha256 `05b34a57…`); handoff boundary green on the current pair
  (16/16 + 20/20 + 105/105 links + 27 claims, live re-run); scope watch
  clean at the final reading; zero unfiled bleed; contested items
  (bilateral read, contract-digest ratification, freshness ruling)
  restated routed-not-absorbed.
- **Cross-claim** — X00 connector collision matrix; X01 trade hunter
  (no axis-harm pathway filed); X02 conformance (one named in-flight
  incident, below); X03 protocol; X04 honesty (`to-verify` census). The
  round's acceptance runner `run-validation.py` implements the S04 leg spec
  (CO/O/C/A/X legs, 16/16 selftest controls).

## Landed changes

- `corpus/lessons/README.md` — revision 3 (integrator-applied; drafted by
  O01/O02; the only filed-index-family byte moved; filed lesson files
  untouched). Supersedes the r26 runner README blob pin and the r25 receipt
  `input_sha256` pin — recorded as new LOG rows, never rewrites.
- `SKILL.md` — the O05 availability-close re-key (`:724-727`), C14 Fix 1
  (loanword cites `:30-31,63`/`:59,63`), Fix 2 (contract mis-cite repoint to
  `packet_uncertainty.py`), Fix 3 (dangling anchors + verdict-word errata),
  Fix 4 (N1 expected-verdict errata), FD-N4/N5 (cold-run operands). 715 →
  732 lines; new digest `f9bd07c2…`; box-1 survey re-run green 28/28.
- `corpus/knowledge/linguistics/register-lexicon-ceilings.md` — §12
  append-only errata (discharges A07-F2 / r29's A29-ADJ-EVID-01).
- `examples/` — six stale `50c4c2f2…` contract-digest repoints to the live
  `5f4c02bf…` (incl. `culture-d3/README.md:104`, F-I33-1).
- `AGENTS.md` — the round-31 drafting residue (orphan fence + heading)
  excised per A07-F1; 42 → 40 lines; logged.
- New round-33 records: `calib/open-items-ledger.json`,
  `adj/audit-assembled.md`, `adj/contract-read-record.md` (OI-08 lane-side
  half), `calib/r18-d4-adapter-successor.md` (OI-12),
  `telemetry/r25-28-devin-reading-errata.json` (OI-11), the O06 harness
  amendment + integrator re-run receipt (11/11), `run-validation.py`,
  `validation.json`, telemetry `observed-dispatch.json` +
  `availability-close-33.json`.
- Filed bytes: **zero** writes to `reports/round-1..32/**`,
  `corpus/lessons/*.md` lesson files, `tools/gates/frozen/**`. Named
  incident **F-C13-1**: during the wave, `reports/round-{5,6,7}/validation.json`
  were written in-tree (03:53:25Z-03:55:27Z) by a historical-runner re-execution
  (guard-adoption gap: those runners rewrite their own receipts without the
  receipt-guard; probable writer C05, `to-verify`) and restored byte-exact
  by 03:55:27Z (digests == HEAD). Recorded in LOG.md; no filed byte changed.

## Before → after measurements

Counting command for all rows: `python3 reports/round-33/run-validation.py`
(exit 0, `validation.json.acceptance_checks_passed: true`, measured at close).

- **O / operability:** lessons audit
  `python3 -B reports/round-25/audit/c31-lessons-index-audit.py` exit 1,
  33 files vs 26 rows, findings 2 (`C31-1` unindexed round-26..32.md,
  `C34-2` stated [26,26] vs measured [26,33]) → exit 0, 33/33/78, findings 0,
  all six checks PASS; `--selftest` 28/28; applied bytes SHA-256
  `f752e1d79…` equal to the seats' two-instrument verified reconstruction.
  Falsifier leg: `SKILL.md:715` one-liner printed 5 false rows (100% of the
  records it could see) → re-keyed audit prints 0 rows live, 7/7 fixture
  scenarios as designed (O05 §4).
- **C / calibration:** no ledger → `calib/open-items-ledger.json` 12/12 rows,
  every status-quo pointer re-verified at HEAD, classes in the licensed
  two-value vocabulary, C13 consistency green, K03 canonical set equal.
  Fixed rows carry applied drafts + green controls (`d2-typed-labels`
  163/163, `box1-survey` 28/28, `packet_uncertainty` 19/19, R06 pointer
  checker 46/0). Carried rows name owner + reason + next touch each.
- **A / adjacency:** no consolidated audit since r29 → `audit-assembled.md`
  with A01-A14 verdicts (two green, twelve named-finding, every finding
  owner-assigned); handoff gate live re-run exit 0 (`fields=16/16
  glossary-entries=20 findings=0`); scope watch: 2655 tracked paths at
  baseline and at close, protected roots (rounds 1-32, lesson files, frozen)
  zero modified rows; language scan clean (A08 two-pass, 17/17 selftest).
- **Regressions (O8 legs):** battery selftest 44/44 + battery mode
  7/0/0 with 10/10 coverage; craft 10/10 + 18/18; D4 81/81; c31 selftest
  28/28; handoff 16/16 — all re-run at close, counts parsed, no shrinkage.

## SHONEN

All four boxes untouched this round; marks stay operator-owned
(`SHONEN.md:10-11`); nothing here is a promotion, canon, clearance or
closure verdict.

- `[ ]` box 1 (decision tables/errors/checklists/sources): conditions
  OI-04/05/06 (the three citation defects) **fixed this round** via C14 with
  controls; the r24 non-author verdicts stand as filed.
- `[ ]` box 2 (end-to-end domain task): standing design debts OI-01/02/03
  (12 garment holds, `head2`, RL-3 ceiling) carried — design, not defect.
- `[ ]` box 3 (cold-run executability): N1/N4/N5 fixed (Fix 4 + FD-N4/N5);
  N7 carried (parent-owned reading pin).
- `[ ]` box 4 (no bleed / PROVINCE accurate): this round's audit adds no
  bleed class; PROVINCE byte-identical since `c53782a`.

Verifier note: the round's non-author reviewers are the dispatched seats
(R01-R08, A11-A14), which per `SHONEN.md:10-11` do not confer `[x]`; the
promotion decision remains the operator's.
