# kotodama — round 35 report (2026-10-19)

Regimen 2 (`REGIMEN.md`), loop 1, build 3 of 3 — the opencode-go build trio's
close. Declared allocation: 64 workers on `opencode-go-3/deepseek-v4.1-flash`.
**Observed route (named deviation):** keys 3, 4 and 5 all returned
`402 Insufficient account funds` with zero seats launched (three recorded
attempts, `telemetry/availability-attempt-{1,2,3}.json`); per the standing
live-key rule the batch dispatched on opencode-go key 1 and completed **64/64**
(`telemetry/observed-dispatch.json`). Live-key census: keys 1-2 funded, 3-5
dry, 6-7 presumed dry by pattern. Declared baseline `4a7aede` (expands to
`4a7aede22cd8395b01ce6dd9f46bcae364ca24e4`). Claims C/O/A on
coverage/operability/adjacency; freshness pause in force. Acceptance:
`python3 reports/round-35/run-validation.py` → `reports/round-35/validation.json`.

## Work performed

- **Coverage (claim C)** — ten sourced entries landed in the two thinnest
  partitions after a mid-wave allocation reconciliation (the plan landed after
  several seats had drafted; P01's swap rule governs; the seat-cited swap chain
  C01↔C06↔C05 and C03's partition placement are recorded in the C receipt):
  culture-material 18 → **24** (funerary, agrarian-fields, writing-media,
  bathing, furniture, fire-fuel-light) and myth-symbol 19 → **23** (world-end
  eschatology, sacred-kingship charter, death-afterlife doctrine,
  binding-speech); total 201 → **211**. Every entry gap-named, sourced,
  decision-record carrying; audited by three independent seat auditors
  (C13/C14/C17) with adversarial review (R01-R03). `corpus/README.md`
  reconciled to revision 2.0 — the round-28 sweep reports 211 rows == 211
  files, zero findings. C04's second draft (timekeeping) is routed as a named
  spare, not silently landed.
- **Operability (claim O)** — R34-N1 closed: the v3 e2e replay of a superseded
  baseline row now raises a named `E2E-READSET` diagnostic naming the
  unresolvable member (patch A + four selftest controls m13a/m13b/m14a/m14b);
  the r6-row counting command exits 1 with the named refusal — no traceback —
  while the preserved `E2E-DIGEST`/`E2E-BASELINE` paths are control-verified and
  the r7 default chain still exits 0 with packet `45f57132…` (zero freeze bytes
  moved). One honest repair during integration: a first control insertion
  included a driver fence and broke the v3 selftest; it was reverted and
  correctly re-applied (the selftest then measured the seat-predicted 44
  bullets).
- **Adjacency (claim A)** — the consolidated bleed-scope audit of every surface
  rounds 33-34 touched (`adj/audit-assembled.md`, from A08's assembly with the
  A07/A11 verifiers): 13 live/shared surfaces verdict-filed, zero unfiled
  cross-domain bleed, PROVINCE re-verified accurate at HEAD (`c53782a`), the
  r7 packet/adoption-tool/examples/SKILL/AGENTS/ceilings slices all GREEN or
  named-finding with owners; contested items remain routed-not-absorbed. Named
  findings K04-F1..F4 filed with owners (none blocks admission).

## Landed changes

- `corpus/knowledge/culture-material/` — six new entries; `corpus/knowledge/myth-symbol/` — four new; `corpus/README.md` — revision 2.0 reconciliation (sweep-green).
- `tools/exercise-handoff-e2e.py` — patch A (read-set roster guard, `E2E-READSET`) + four selftest controls (+42/−3 + controls; defaults untouched).
- `reports/round-35/` — the full round record (claims/targets, 64 seat fragments, the assembled adjacency audit, `run-validation.py`, telemetry).
- Filed bytes: **zero** writes to `reports/round-1..34/**`, the 201 baseline corpus entries (P1: byte-identical), `corpus/lessons/*.md` (33), `tools/gates/frozen/**`.

## Before → after measurements

Counting command: `python3 reports/round-35/run-validation.py` (exit 0 at close;
receipt `reports/round-35/validation.json`).

- **C / coverage:** partition census 21/19/18/29/20/94 = 201 → **21/23/24**/29/20/94 = **211** (command-carried); inventory `totals.files` 201 → 211; README 211 rows == 211 files, 0 missing/ghosts/duplicates/drift; 10/10 entries audited (three auditors, defects filed not smoothed); `to-verify` census reported in the receipt.
- **O / operability:** r6-row replay = unhandled KeyError → exit 1 `E2E-READSET` naming `reports/round-20/handoff/claims-map.md` (counting command, observed); v3 selftest carries m13a/m13b/m14a/m14b green; r7 chain exit 0, packet `45f57132…` == freeze.txt; battery 44/44, craft 18/18, D4 81/81, gate 16/16.
- **A / adjacency:** no consolidated r33/34-surface audit → 13-surface audit with zero unfiled bleed; PROVINCE byte-identical since `c53782a`; findings F1-F13 owner-assigned.
- **Cross:** coherence legs green (the opencode-go-3→key-1 route deviation recorded in CO); preservation byte-clean; language leg clean under the grant-frame scanner.

## SHONEN

All four boxes untouched this round; marks stay operator-owned
(`SHONEN.md:10-11`); nothing here is a promotion, canon, clearance or closure
verdict. Box 1's evidence stays current at digest `f9bd07c2…`; box 4's audit
adds no bleed class. The non-author reviewers are dispatched seats and do not
confer `[x]`; the promotion decision remains the operator's.
