# kama — round 96

Lane `kama` (operability + calibration; local model serving and endpoint health). L1 `KamaR96`.
Base `5d43528badc31ad6c0ca1848c00561f531924e4d` (round 95 admitted). Freeze `58001b71`; amendments
`e2fed9f5`, `fb5cd3cd`/`4a0f6a35`, `b3289c18`, `20317286`, `bb4a997a`, `f175a902`; wave evidence and
measurements `f6122036`.

## Work performed

**Declared claims (3, distinct axes, causally separable):**

- **C1 — operability:** the probe's step budget decides the files it prices (a 700 000-tensor file graded
  `-` → loadable at `MAX_STEPS = 4 000 000`; it decides at 5 000 000), and the instrument cannot pass
  without load evidence or without the cap being load-bearing.
- **C2 — depth (the lowest non-retired axis, 7):** the step-cost table states the arithmetic the parser
  enforces (`5 + nd` steps per tensor header, per-rank ceilings), so a reader can decide a candidate's
  decidability without re-reading the parser.
- **C3 — calibration:** every disclosure the lane repeats (the probe's ceiling comment, the counter's
  docstring formula and budget, the `router-byte-decided` capability pointer) matches the bytes beside it.

**Work items:**

- **Frozen the round** (`58001b71`): `plans/round-96-claims.md`, three counters
  (`tools/round96-router-budget.py`, `-depth-audit.py`, `-disclosure-audit.py`), the probe's
  `MAX_STEPS` raise, the S618 row, and every freeze-time control
  (`controls/{census-start,c1-base,c2-base,c3-base}.out`).
- **Wave 1, 12 seats** (attack 5 = RV01 reviewer, CR01/CR02 critics, MT01 mutation-tester, SN01 sentinel;
  connectors 1; scouts 2; executors 2; scribe 1), dispatched through the inline handoff
  (`.ufo/waves/round-96/w1.ready` → `w1-dispatch.json`), all settled; reports in `.ufo/waves/round-96/w1/out/`.
- **Six amendments**, each answering a wave finding with a measurement rather than a re-wording —
  `plans/round-96-amendment-{1..6}.md`; the round's own filings were corrected five times (W12 fixture
  twice, the per-header cost, the nd=3 ceiling, the identity clause, the W03 count).
- **Amendments 1–6 repairs:** anchored `MAX_STEPS` regex (1); `5 + nd` table, 833,332 ceiling,
  `positive_mismatches` widened off the `W0` prefix, counter docstring budget (2); interleaved W12 elements
  and the W03 count as a host-speed parameter (3); nd=3 ceiling 624,999 plus a per-rank arithmetic check
  (4); identity clauses bound to the amended commits (5); **W13-budget-kill**, the cell MT01 proved missing
  (6).
- **Measured all three claims** with their do-nothing controls; the records are
  `.ufo/waves/round-96/{measured,controls}/*.out`.
- **Frontier step:** `corpus/SOURCES.md` 357 → 358 rows (S618 admitted from
  `ggml/include/ggml.h` @ b12177, digests measured; S619 rejected as docs; `ggml/src/gguf.cpp` rejected as
  S129's duplicate); `corpus/lessons/round-96.md` carries `## Gate` and `## Mistakes` M1–M5.
- **Sourced claim:** C2 rests on S618, opened this round, which grounds the per-rank header cost.

## Landed changes

| Change | LOG.md entry | Commit |
|---|---|---|
| Frozen plan, three counters, probe `MAX_STEPS` 4 M → 5 M, S618, step-cost table v1 | round-96 freeze entry | `58001b71` |
| Anchored `MAX_STEPS` regex in the depth/disclosure audits + amendment 1 record | freeze entry | `e2fed9f5`, `bbdfc930` |
| Amendment 2: `5 + nd` table, 833,332 ceiling, W12 9-byte elements, `positive_mismatches` predicate, docstring budget | wave-findings entry | `fb5cd3cd`, `4a0f6a35` |
| Amendment 3: interleaved W12 elements (54 000 049 B), W03 count as host-speed parameter, margin message | wave-findings entry | `b3289c18` |
| Amendment 4: nd=3 ceiling 624,999; per-rank arithmetic checks in the depth audit | wave-findings entry | `20317286` |
| Amendment 5: identity clauses bound to amended commits; the round lesson | wave-findings entry | `bb4a997a` |
| Amendment 6: W13-budget-kill (`cells=13`) | wave-findings entry | `f175a902` |
| Wave-1 findings (12 seats) into LOG.md | wave-findings entry | `f3fd922e` |
| Measurements, SCORECARD §Round 96 + capabilities + round-97 plan, census end, wave evidence | measurements entry | `f6122036` |

## Before → after measurements

**C1 — operability.** Counting command
`python3 tools/round96-router-budget.py --repo . --rev <rev> --work <private> --slow-files 96`.

- Before (`controls/c1-base.out`, probe at `5d43528b`, amended counter, two natural passes):
  `ROUTER_BUDGET96 cells=13 mismatches=1 positive_mismatches=1 load_cells=13 load_stable=1 budget=work
  probe=rev probe_sha256=b49d961a… rev=5d43528b w03_seconds=46.3` — **exit 1**, W11-700k
  `ok=0 run1=MODEL_OK/router-unloaded-autoload` (the false green), every other cell green.
- After (`measured/c1.out`, measured at `f175a902`):
  `ROUTER_BUDGET96 cells=13 mismatches=0 positive_mismatches=0 load_cells=13 load_stable=1 budget=work
  probe=rev probe_sha256=11e5b01b… rev=f175a902 w03_seconds=161.4 load1_nat=9.44 burners=0` — **exit 0**;
  W11-700k `MODEL_UNLOADED/router-model-invalid`, W13-budget-kill `MODEL_OK/router-unloaded-autoload`.
- Separate mechanism check (MT01's mutant, re-run by the L1): the same `budgetkill.gguf` grades
  `MODEL_UNLOADED` with `MAX_STEPS = 10**12`, so the cap is now graded, not assumed.

**C2 — depth.** Counting command `python3 tools/round96-depth-audit.py --repo . --rev <rev>`.

- Before (`controls/c2-base.out`, `5d43528b`): `DEPTH_AUDIT checks=14 mismatches=14 met=False` — exit 1.
- After (`measured/c2.out`, `20317286`): `DEPTH_AUDIT checks=14 mismatches=0 met=True` — exit 0. The checks
  are the table's presence, each of the five per-rank ceilings against `(MAX_STEPS - 4) // (5 + nd)`, the
  probe's `MAX_STEPS`, and S618's Registry status.

**C3 — calibration.** Counting command
`python3 tools/round96-disclosure-audit.py --repo . --rev <rev>`.

- Before (`controls/c3-base.out`, `5d43528b`): `DISCLOSURE_AUDIT checks=6 mismatches=3 met=False` — exit 1.
- After (`measured/c3.out`, `20317286`): `DISCLOSURE_AUDIT checks=6 mismatches=0 met=True` — exit 0.

## Sources & frontier

`SOURCES.md` rows before → after: **357 → 358**. Counting command:
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kama`
→ `kama ok …`, **exit 0** at round start (`controls/census-start.out`) and at round end
(`controls/census-end.out`).

- Rows added by tier: **1** A-tier code/mined row — S618 `ggml/include/ggml.h` @ b12177
  (sha256 `590e00a522b8791235353a8c7388d67ff2fe929554f1834c58528b82afd67392`, quote
  "nb[0] = ggml_type_size(type)" line 697); **2** rejections recorded — S619 `gguf-py/README.md`
  (docs; grounds no header cost) and `ggml/src/gguf.cpp` (duplicate of S129).
- Rows touched old → new: none (`status`/`recheck`/`used-by` unchanged).
- Frontier rows advanced: the unloadable-file rule's ceiling (round 89's `-` → loadable rule) now carries
  the measured per-rank arithmetic; the step budget itself is no longer an unstated constant.

## Trend verdicts

- **expansion: unchanged** — one row deepened an existing surface (the GGUF header the probe already
  parses); no new knowledge entry and no new governed surface this round.
- **quality: improved** — C1 replaced a budget that left 700 000-tensor files loadable and an instrument
  that could pass without load evidence or without the cap being load-bearing (W13 measured against an
  uncapped mutant); C2 and C3 replaced a table and a set of filings that stated figures the code did not
  enforce. Evidence: `measured/c1.out`, `measured/c2.out`, `measured/c3.out` and their red controls.
- **discernment: improved** — the wave falsified six of the round's own filings and one core instrument
  (four mutants survived all twelve cells), and each was answered by a repair with a measured control
  rather than a re-wording: RV01 F1/F2/F3, CR01 B1 (same blocking defect found independently), SC02's
  binary search over every ceiling row, MT01 G1→W13, CR02 B1→amendment 5. The counter was also caught
  twice running the wrong side of its own control (base-at-tip, shared-scratch collision), both repaired
  and recorded as lesson M3/M4.

## SHONEN

- [~] **Every claim carries a counting command and a red control.** `SCORECARD.md` §Round 96 rows quote
  the commands; the controls are `.ufo/waves/round-96/controls/*.out` (C1 `mismatches=1`, C2 `mismatches=14`,
  C3 `mismatches=3`).
- [~] **Wave floor met, one batched wave.** `.ufo/waves/round-96/w1-results.json` — 12 seats, 5 attack
  (RV01, CR01, CR02, MT01, SN01), 1 connector, 2 scouts, 2 executors, 1 scribe, all settled.
- [~] **Frontier step:** census 357 → 358, exit 0 at both ends; lesson carries `## Gate`, `## Mistakes`
  M1–M5, each with a captured-by and a fix shown able to fail.
- [~] **Non-author verification is pending, as the protocol requires.** No `[x]`: this report is the
  author's; the closure judge and its spot-check own the admit/reject. The wave's own non-author reads are
  cited where they caught the author (RV01, CR01, SC02, MT01, CR02, SN01).

## Routed to round 97 (disclosed, not claimed)

1. **MT01 G2:** a probe that stopped charging per header still passes every cell — needs a cell between the
   833 332-header ceiling and `MAX_TENSORS = 1 000 000` (≈5.4 M steps of CPU; time it first).
2. **MT01 G3/G4 (round-95 NOTE):** `MAX_META` lowered to 100 MiB and ctime removed from the memo key both
   survive; a >100 MiB header and a same-process rewrite are the shapes.
3. **r94 SC02 F4:** a slow `/props` answer still decides the verdict; the vocabulary for an unread autoload
   flag is unsettled.
4. **CR02 B2–B5:** the C3 instrument grades literal presence — a comment naming 1 000 000 as *non-binding*,
   a docstring disagreeing on a different number, and a capability pointer to any resolvable ancestor all
   pass. Grade the binding claim, not the string.
5. **SC01** staged held-out listings (many small files, a 600k+700k mix, exact-`MAX_STEPS` work, deep
   string-array nesting) were designed but not run as cells this round.
6. **Carried:** `round75-instruments` (`APPEND_DEBT … bad_rows=19`, L0 r87/r89 open); the
   `round78-instruments` red from the host's non-lane Ollama listener on 127.0.0.1:8080 (re-checked, still
   listening).
