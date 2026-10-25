# kotodama — round 34 report (2026-10-19)

Regimen 2 (`REGIMEN.md`), loop 1, build 2 of 3. One batch on
`opencode-go-2/deepseek-v4.1-flash` (key 2 of the round-robin): 63 seats
authored in `targets.json` and 63 dispatched/completed (the declared
`seat_count: 64` vs 63 authored rows is recorded as the named CO4 deviation —
the file is digest-pinned, so the deviation stands as data, not an edit).
Declared baseline `da68a6d` (short id; expands to
`da68a6d705e41f369f21e8607bfaab5b54077f84`). Claims D/O/C on
depth/operability/calibration; freshness pause in force. Acceptance:
`python3 reports/round-34/run-validation.py` → `reports/round-34/validation.json`.

## Work performed

- **Depth (claim D)** — A02-H1 closed. The wave proved the staleness is
  structural: the renderer copies the twelve D4 claim rows verbatim from filed
  `reports/round-20/handoff/claims-map.md` (`tools/exercise-handoff-e2e.py:184`,
  `:2289-2320`) and hard-codes OQ-V3-05, so a re-render reproduces the stale
  packet byte for byte (D16's isolated-copy proof; D10's S1′ simulation). The
  landed fix: a successor claims-map at
  `reports/round-34/handoff/declared-in-r7/claims-map.md` (filed round-20 map +
  D15's ten replacements + D03's three sweep-finds; 12 rows re-parse under the
  renderer's own regex) and six renderer edits (CLAIMS_MAP re-point, docstring
  and artifact-manifest followers, scope cell twelve→thirteen, OQ-V3-05 rewrite,
  the coupled default-pair move). `declared-in-r7` frozen: packet `45f57132…`,
  gate 16/16 + 20/20 + findings 0, links 105/105, claims 27 (16/7/4), e2e exit 0;
  D16's live-truth audit reports CLEAN. Re-pin cascade in
  `reports/round-34/handoff/repin.json` (new rows only; filed r2..r6 bytes
  untouched; r6 row refuses replay, exit 1 via an unhandled KeyError — named
  finding R34-N1, routed to renderer hardening).
- **Operability (claim O)** — capability acquired:
  `tools/harness/receipt_guard_adoption.py` (selftest green) inventories every
  filed round runner's receipt-guard adoption: 29 runners — 17 `guarded-refresh`,
  11 `unguarded-in-place` (r5/r6/r7 among them), 1 `guard-referenced-only`
  (this round's own runner). Durable inventory
  `reports/round-34/op/adoption-inventory.json`; routing receipt
  `reports/round-34/op/O05-routing.md` (unguarded runners → isolated-copy-only
  protocol). K03's evidence corrects the round-33 F-C13-1 record: r26 **is**
  guard-adopted (`:1855`, `:1906`) — errata filed append-only in LOG.md.
- **Calibration (claim C)** — box-1 evidence pinned durable at the post-round-33
  digest: `reports/round-34/craft/box1-resurvey-durable.json` (28/28 executables
  resolve at SKILL.md `f9bd07c2…`, survey re-verified at HEAD) and the A09 anchor
  reissue table at `reports/round-34/craft/anchor-reissue.md` (built from the
  line-level citation census; C09-F2 guards against phantom rows; the seven live
  stale cites re-issued as superseded readings, filed bytes untouched).

## Landed changes

- `tools/exercise-handoff-e2e.py` — six edits (five sites + the coupled default
  pair); sha256 `a5e4a8c5…` → `34c85f57…`; renderer selftest green.
- `tools/harness/receipt_guard_adoption.py` — new instrument (claim O).
- `reports/round-34/handoff/declared-in-r7/` — packet.md, twin.json,
  expected.json, freeze.txt, run.log, claims-map.md (new revision; filed r6 row
  named superseded, never edited).
- `reports/round-34/handoff/repin.json`, `craft/box1-resurvey-durable.json`,
  `craft/anchor-reissue.md`, `op/adoption-inventory.json` — new records.
- `LOG.md` — append-only entries (integration-progress note with the r26
  errata; the admission entry follows this report in the same close pass).
- Filed bytes: **zero** writes to `reports/round-1..33/**`,
  `corpus/lessons/*.md`, `tools/gates/frozen/**` (P1 leg: 0 moved protected
  paths). Seat fragments: 61 of 63 landed; D17 and X00 never landed — their
  substance was covered by D18-D20/X01-X02/R08 and is recorded in
  `missing_dependencies`.

## Before → after measurements

Counting command: `python3 reports/round-34/run-validation.py` (exit 0 at close;
receipt `reports/round-34/validation.json`).

- **D / depth:** default pair `declared-in-r6` (shape-green, seven+ stale
  figures incl. the claim-unnamed 50/50 at packet.md:151) → `declared-in-r7`
  with every D4/OQ figure equal to a measured live value (audit CLEAN); gate
  16/16 + 20/20 + 0; links 105/105; e2e `--quiet` exit 0, packet_sha256
  `45f57132…` == freeze.txt; r6 row refuses replay (exit 1, KeyError mechanism
  named); preservation 0 rows.
- **O / operability:** no adoption inventory, the F-C13-1 gap uninstrumented →
  29-runner inventory, selftest green, counts matching K03's independent census
  (17/11), four named hazards classified (r5/r6/r7 unguarded; r26 guarded per
  the errata), routing table covers every unguarded runner, zero in-tree runner
  execution (r5/r6/r7 receipt digests == HEAD).
- **C / calibration:** box-1 evidence current only as console output at the old
  digest → durable receipt 28/28 at `f9bd07c2…` + anchor reissue covering the
  citation census (seven live stale cites re-issued; C09-F2 phantom-row guard).
- **Cross:** coherence legs pass (the 64-vs-63 seat deviation recorded, not
  edited); preservation leg 0 moved paths; language leg clean under the
  verdict-frame scanner (evidence-prose token mentions allowed, grant frames
  refused); telemetry digests match the live declaration.

## SHONEN

All four boxes untouched this round; marks stay operator-owned
(`SHONEN.md:10-11`); nothing here is a promotion, canon, clearance or closure
verdict.

- `[ ]` box 1: the round-33 citation fixes stand; this round's box-1 evidence is
  now pinned durable at the current digest (claim C).
- `[ ]` box 2: standing design debts unchanged (12 garment holds, `head2`,
  RL-3 ceiling — carried in the round-33 ledger).
- `[ ]` box 3: N1/N4/N5 fixed at round 33; N7 carried; no change this round.
- `[ ]` box 4: no new bleed class; contested items remain routed-not-absorbed.

Verifier note: non-author reviewers are the dispatched seats (R01-R08, the
verifier seats); per `SHONEN.md:10-11` they do not confer `[x]`. The promotion
decision remains the operator's.
