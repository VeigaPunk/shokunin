# mado — round 25 report (attempt 3, L1 `MadoR25A3`)

Lane tip `16e57dac26cb97e36e44a3b0552d1e4c27479dfc` (pushed). Base `41cc04c8d593837a0d5078bffaacdaa163d12897`.

## Work performed

There are two claims. **C1 is operability, a capability acquisition (sourced):** a static Hyprland v0.56.2 bind-table resolver, `tools/mado-binds.py`. **C2 is calibration and exploratory:** a ledger of the current state of every SCORECARD capability row. Routed repairs from the round-24 closure are repairs, not claims.

- **Earlier attempts.** Attempts 1 and 2 landed `04051723`, `7228299d` and `a258c6ae` (counters v1–v3 and the v1 control receipts). I re-checked the v1/v2/v3 pins: `count-v3.py` is byte-identical to the `a258c6ae` `count.py`. Attempt 2 left untracked scratch: a dead control wave under `w1/`, `controls/v3/` and `w1-*.json`. I read only its item list and verdict lines, for orientation. None of it is cited, and it is deleted (`registration.md` "Attempt 3").
- **Counter v4 (`1ed41fa8`).** v1–v3 took the expected table for each generated case from the counter's own line model, so a transcription of that model would meet them by construction. v4 keeps v3's generator, which `ExecReplayIdentity` re-checked: 41/41 trees per seed for 3 seeds. Every expected table now comes from Hyprland itself: a nested instance per case, read back with `hyprctl -i <inst> binds -j`. `ORACLE_CHECK` compares the oracle with the live table on every run. `ExecOracleDeterminism` found 41/41 identical results across repeat runs. `RevCounterV4` found one minor fail-closed defect: a crash exits 1. A registration note made before data says a run with no PRED line is a setup failure.
- **Pre-data control wave a3w1 (40 seats).** Ten shortcut shapes were scored under v4, and the receipts landed at `459dd17f` (07:29:16Z), before the a3w2 data registry `createdAt` (07:31:20Z). None met the target. Scores were 0/41 for do-nothing, `[]`, junk, echo, shell-out, grep and no-reader; easy-grammar scored 4/41, encoded table 31/41, label-keyed 37/41 (`controls/v4/*.md`). `RevChronology` reports `ordered`.
- **Sources.** S169–S172 were opened and S162/S167 gained `used-by` entries. Six re-open seats agreed: `a3w2/reports/Reopen*.md`.
- **Data wave a3w2 (34 seats).** `ExecBindToolA` and `ExecBindToolB` each wrote an independent resolver, and both reached 41/41 on three fresh seeds. A landed, by the first-returned rule, at `ef94763c`. `ScribeBindNote` drafted `corpus/knowledge/bind-table-r25.md`. Ten control re-measures were all `not met`; the strengthened encoded-table control reached 37/41. Twelve C2 row re-checks all agreed.
- **Measurement (single run).** `python3 -I .ufo/waves/round-25/c1/count.py ef94763c` gave `PRED-C1 (v4) cases_pass=41/41 embed_hits=0 verdict=TARGET_MET`, exit 0, seed `ed0d8a943980d2f2` (`evidence/c1-after-v4-ef94763c.txt`). v1 33/33, v2 37/37 and v3 41/41 are reported only.
- **Residual call (8 reviewer/critic seats).**
  - `ResC1Remeasure`: a fresh re-measure gave 41/41. 9 of 10 hand-made trees outside the generator agree; the miss is `{{…}}` arithmetic.
  - `ResToolAblation`: all 8 feature-ablation mutants were killed.
  - `ResCounterMutantsLive`: 2 of 4 counter mutants were killed. `skip-oracle-check` and `embed-threshold` survive.
  - `RevToolProvenance`: no embedded operator data, and A and B agree on 5/5 trees. The finding is that the tool follows absolute and `$VAR` source paths and seeds variables from the environment; `PROVINCE.md` now carries a correction. The tool also splits the dispatcher literal `"resize" "windowpixel"`, which dodges the plain-string embed check. It is a grammar entry, not operator data; this is disclosed in lesson 25.
  - `RevBindNote`: 58/58 quotes are verbatim; 10 sentences go beyond their quotes, now listed in the note's errata.
  - `RevNoHarm`: no axis harmed.
  - `RcMutationRegression311`: agree.
  - `RevC2Judgment`: C2 is `unprovable-but-better`, with errors F1–F5.
- **Routed repairs (`2896dc4a`).** R1/R2 add QUALITY criterion 36 and `quality/check-control-receipts.py`. The check is red on round 24 (`quality/q36-red-round24.txt`, receipts 1083 s late) and green on round 25 (`q36-green-round25.txt`). R3: A18 in-row correction plus errata. R4: S161 correction. R5: receipt-chronology corrections in the lesson and the round-24 registration. R6: SCORECARD pointers. `RevRepairs`: 5 of 6 closed. R2's population-equality clause is still open (M25-4).
- **R7 (report SHONEN boxes).** Each box below carries a resolvable pointer.
- **R8 (carried).** Hold H2 and QUALITY 33–35 survivors open.

## Landed changes

| Commit | What | LOG.md |
|---|---|---|
| `1ed41fa8` | counter v4, v3 pin, registration "Attempt 3", before receipt | Round 25 entry |
| `2896dc4a` | repairs R1–R6, a3w1 spec | same |
| `459dd17f` | 10 control receipts plus the a3w1 reports, before data | same |
| `fa466833` | SOURCES S169–S172, used-by, registration note, a3w2 spec | same |
| `ef94763c` | `tools/mado-binds.py`, `corpus/knowledge/bind-table-r25.md` (measured commit) | same |
| `90224671` | measurement receipts, PROVINCE row, C2 ledger, Q36 green | same |
| `16e57dac` | lesson 25, LOG, SCORECARD results and C2 errata, PROVINCE correction, README index, note errata, residual reports, end census | same |

## Before → after measurements

- **C1.** `python3 -I .ufo/waves/round-25/c1/count.py REV` (v4 sha256 `323a3849…42e2`).
  - Before, at `41cc04c8`: `tool=MISSING_TOOL`, 0/41, exit 1 (`evidence/c1-before-v4-41cc04c8.txt`).
  - After, at `ef94763c`: 41/41, `embed_hits=0`, `TARGET_MET`, exit 0.
  - No control met v4 before data.
- **C2.** Exploratory, no counting command. The named non-author reviewer `RevC2Judgment` (`a3res/reports/RevC2Judgment.md`) judged it `unprovable-but-better`.
  - Reason: the ledger covers all 15 identities with fresh runs at base, versus 12 transcribed rows before. It marks `:437` and `:1342` as failing, observes the live arm of `:309` for the first time, and names four documentation defects.
  - Its errors F1–F5 are recorded in an appended errata block, not edited into the judged rows. One disclosure: I edited the ledger's receipt sentence while the review was running (M25-5).

## Sources & frontier

- Census at start: `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin mado` gave `mado ok` with 7 pre-existing W04 warnings, exit 0 (`evidence/sources-start-a3.txt`). At end: same result, exit 0 (`evidence/sources-end-a3.txt`).
- Rows: 168 → 172, all tier A. New: S169 (hyprctl client), S170 (aquamarine Backend.cpp), S171 (Hyprland main.cpp), S172 (hyprlang wiki).
- Rows touched: S162 and S167 `used-by` changed from `rule-attribution-r24.md` to `+ bind-table-r25.md`. The old→new change is logged in `corpus/lessons/round-25.md` § Gate.
- Frontier advanced: the new surface is P1 Hyprland binds, now static prediction (README "Round-25 bind-table route").
- Sourced claim: C1's note and tool docstring cite S162, S167, S169–S172.
- Mined mistakes: M25-1 to M25-5 in lesson 25.

## Trend verdicts

- **expansion: improved.** A new runnable tool covers a surface the lane had never instrumented, measured against Hyprland's own tables, plus a sourced note. Closure judgment is pending.
- **quality: improved.** The counter's self-model was replaced by an oracle. Five of six repairs closed, with checks shown red and green. A note errata and a PROVINCE correction come from non-author reviews.
- **discernment: improved.** Controls came before data. The weaknesses are disclosed rather than amended: the mountinfo label leak (M25-2), the weak Q36 check (M25-3), and two surviving counter mutants.

## Gate

The real rejects, with reasons:

1. **Counter v3 rejected as the claim's rule before data.** Its expected values came from the lane's own model (M25-1).
2. **ExecBindToolB not landed.** The first-returned rule selected A.
3. **Duplicate-URL rows for S162 and S167 rejected.** Their `used-by` cells were extended instead.
4. **WikiVariablesKeywords source unopened.** Every candidate URL returned 404.

## Round shape

- Shape: two v1 waves plus one residual call.
  - a3w1: 40 seats (critic 6, mutation-tester 6, sentinel 1, executor 17, reviewer 1, scribe 7, scout 1, connector 1).
  - a3w2: 34 seats (executor 2, scribe 1, critic 5, mutation-tester 6, reviewer 20).
  - Residual: 8 seats (critic 3, reviewer 5).
  - Round total: 82. No dead seats.
- The gate was granted in chunks of 20+20 and 17+17.
- The L1 holds the planner seat.
- Install: none.
- Oracle side effect: nested Hyprland windows briefly opened on the live session.
- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
- Open L0 questions: H2 (`.ufo/l0-questions.md:103`); no new question this round.

## SHONEN

- [~] SKILL.md decision tables / cited sources — `corpus/knowledge/bind-table-r25.md` (S162, S167, S169–S172); SKILL.md unchanged.
- [~] End-to-end domain task logged — LOG.md "Round 25" entry; `evidence/c1-after-v4-ef94763c.txt`.
- [~] Executable without oral context — `python3 -I tools/mado-binds.py --home DIR` (PROVINCE row and docstring).
- [~] No cross-domain bleed — PROVINCE.md row plus round-25 correction; `a3res/reports/RevNoHarm.md` (round-23 C3 = 0 at `90224671`).
