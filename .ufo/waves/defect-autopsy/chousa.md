# Chousa defect autopsy — rejected rounds 78–83 (6× `rejected-honest-stop`)

Fleet root: `/home/vgpnk/Projects/shokunin`. Read-only. Evidence pointers are `file:line`, command + output, or commit hash.

## Round-by-round

### Round 78 — C1 operability + C2 calibration (both falsified)

**Rejection reason, verbatim** — `.ufo/reports/round-78/chousa.md:22`:
> "**Claim outcomes — both frozen kill rules fired, and that is the round's honest result:**"

Closure ruling, `chousa-shokunin/corpus/lessons/round-78-verifier-spotcheck.md:240`:
> "`admitted: false` — both claims fail their own frozen kill rules and the lane says so itself. Verdict `rejected-honest-stop`"

**Claim vs measured.** Report `.ufo/reports/round-78/chousa.md:112-113`: C1 `FORGE_BATTERY=FAIL forgers_handled=0/4` exit 1 → `FORGE_BATTERY=PASS forgers_handled=4/4 positive=1/1` exit 0. Report `.ufo/reports/round-78/chousa.md:133-134`: C2 `SELFCHECK=FAIL unresolved=3/3` → `SELFCHECK=PASS unresolved=0/3` exit 0. Kill, report `.ufo/reports/round-78/chousa.md:24-31`:
> "C1: the predicate holds; the kill rule fires. … a *content normalizer* … reaches the exact predicate line at exit 0 while scoring nothing. … C1 lands **falsified by its own kill rule**"

C2 kill, `.ufo/reports/round-78/chousa.md:33-35`:
> "R78ReviewB cloned the lane, restored all three routed defects and wrote three hollow repair lines; the counter printed `SELFCHECK=PASS unresolved=0/3` at exit 0"

**Class.** (a) green-but-unprovable-wording, 2/2 claims. Both counters green on committed controls; the claim wording covers a channel (content normalization; hollow presence-only repair lines) the frozen controls never enumerate.

### Round 79 — C1 operability + C2 calibration (both falsified)

**Rejection reason, verbatim** — `.ufo/reports/round-79/chousa.md:9`:
> "kill rules fired on inputs the predicates do not enumerate — the round's admission is false on the rules declared before data."

Closure ruling, `chousa-shokunin/corpus/lessons/round-79-verifier-spotcheck.md:283-284`:
> "`admitted: false` — both claims fail their own frozen kill rules and the lane says so itself. Verdict `rejected-honest-stop`"

**Claim vs measured.** Report `.ufo/reports/round-79/chousa.md:125`: C1 `FORGE_BATTERY=FAIL 5/6` → `FORGE_BATTERY=PASS 6/6` exit 0. C2 `SELFCHECK2=FAIL 3/3` → `SELFCHECK2=PASS 0/3` exit 0 (`.ufo/reports/round-79/chousa.md:127`). Verdicts, `.ufo/reports/round-79/chousa.md:133-134`:
> "**Verdicts:** C1 — predicate holds, **kill rule fired** (`a10` forger). C2 — predicate holds, **kill rule fired** (duplicate criterion number in a newer block)."

**Class.** (a) 2/2. C1 wording counts six forgers while the kill clause says "if **any** forger is FORGED" (`.ufo/reports/round-79/chousa.md:79`); the payload-decode forger is outside the six. C2 wording audits every block while a re-used criterion number overwrites the earlier body in `criteria()`.

### Round 80 — C1 operability + C2 calibration (both falsified)

**Rejection reason, verbatim** — `.ufo/reports/round-80/chousa.md:117`:
> "verdict: **falsified by its own kill rule — honest stop.** The predicate is draw-dependent"

**Claim vs measured.** C1 after receipt `.ufo/reports/round-80/chousa.md:115-116`: `BATTERY=PASS forgers_rejected=11/11 positive=2/2 … fresh_positive=2/2 …` exit 0; measured FAIL draws `1/2+1/2`, `0/3+0/3` (`.ufo/reports/round-80/chousa.md:117-119`). C2 after `.ufo/reports/round-80/chousa.md:136-137`: `GATE_GROUNDING=PASS unresolved=0 superseded_resolved=3`. Kill, `.ufo/reports/round-80/chousa.md:138-139`:
> "verdict: **falsified by its own kill rule — honest stop** on the frozen third clause: a `GATE-RECORD` line naming bytes the counter never opened still yields `unresolved=0`"

**Class.** (a) 2/2. C1 is a draw-dependence variant: the frozen predicate ("exits 0 and prints exactly …") cannot be a stable property when the scored set is drawn per run. C2 is the pure (a) form: the counter parses a record but never opens the bytes it names.

### Round 81 — C1 depth + C2 operability (both falsified)

**Rejection reason, verbatim** — `.ufo/reports/round-81/chousa.md:87`:
> "**honest stop**: K1 and K2 held. The counter accepts filler entries (a §9 cheapest-control defect, now QUALITY 162), and one table row contradicted its cited source (K3 in spirit, repaired)"

Closure ruling, `chousa-shokunin/corpus/lessons/round-81-verifier-spotcheck.md:92`:
> "Admission: **false** (`rejected-honest-stop`): neither claim verifies, and both were stopped by their own kill rules."

**Claim vs measured.** C1 `DEPTH_R81 entries=0 FAIL` → `entries=2 fresh_rows=5 located_quotes=14 PASS` rc 0; C2 `CHECKLIST_RUN=3/6 0/3 FAIL` → `6/6 3/3 PASS` rc 0 (`.ufo/reports/round-81/chousa.md:87-88`). Filler proof, `round-81-verifier-spotcheck.md:50`:
> "The critic's filler control is evidence-verified … `entries=2 fresh_rows=4 located_quotes=6` `DEPTH_R81=PASS` rc=0. The counter therefore does not separate depth from filler."

**Class.** (a) 2/2. C1 is the source-text-derived depth form exactly matching kama 3/3: the counter checks located-quote binding, not content or warrant; two 10-line filler entries reach PASS and a table row contradicts its own cited source. C2: item-4 passes flip `-`, `n/a` or `none`; item-2 passes undeclared sweep ids and `n/a` locations (`.ufo/reports/round-81/chousa.md:88`).

### Round 82 — C1 operability + C2 depth (both falsified)

**Rejection reason, verbatim** — `.ufo/reports/round-82/chousa.md:86`:
> "**falsified by K2 and K3 (honest stop)**"

Closure ruling, `chousa-shokunin/corpus/lessons/round-82-verifier-spotcheck.md:10`:
> "Verdict: **status ok, not admitted (`rejected-honest-stop`)**. Both declared claims are falsified by their own frozen kill rules"

**Claim vs measured.** C1 `K2_GATE=PASS 11/11 9/9 24/24 6/6` rc 0; C2 `DEPTH_R82 entries=1 ok_entries=1 rows=9 located_quotes=11 PASS` rc 0 (`.ufo/reports/round-82/chousa.md:86-87`). K2, `.ufo/reports/round-82/chousa.md:46-47`:
> "Records with a repeated `##` heading pass, because `load_sections` keeps only the last body"

C2 K3, `.ufo/reports/round-82/chousa.md:53`:
> "**C2 K3 fired** on row 1's Never cell"

Closure agrees on static read of `load_sections()` line 870 (`SEC_BODY` reset on repeated heading, `round-82-verifier-spotcheck.md:69-74`).

**Class.** (a) 2/2. C1 wording is a parser property (duplicate-heading invisibility), not a vocabulary the frozen 24-form set models. C2 wording asserts a Never that the source itself contradicts (PICO/PECO endorsed for maps preceding an SR, `MANIFEST.json` rounds[82] `verification.rechecks`).

### Round 83 — C1 depth (VERIFIED) + C2 operability (falsified)

**Rejection reason, verbatim** — `.ufo/reports/round-83/chousa.md:50` (C2 row):
> "**falsified by its own kill rules — honest stop**: K2 `line=2٢٢` prints OK (Unicode `\d` …); K3 genuine rev record with a leading `\"` refused"

Closure ruling, `chousa-shokunin/corpus/lessons/round-83-verifier-spotcheck.md:10`:
> "Verdict: **status ok, not admitted (`rejected-honest-stop`)**. C1 depth verifies on closure's own re-run; C2 operability is falsified by its own frozen kill rules K2 and K3"

**Claim vs measured.** C1 `entries=1 ok_entries=1 rows=10 located_quotes=16 fresh_sources=3 PASS` rc 0, all kills held (`.ufo/reports/round-83/chousa.md:49`). C2 `TOOL=present POSITIVE=15/15 FORGED_REFUSED=198/198 … PASS` rc 0 (`.ufo/reports/round-83/chousa.md:50`). Round still rejected because one claim falsified: `.ufo/reports/round-83/chousa.md:81-83`:
> "operability improved narrowly, claim falsified (no capability row enters) … one claim verified, one falsified, so by the contract the round does not admit."

**Class.** C2 (a) 1/1 falsified; C1 verifies (0). C2 wording (`line=<n>`, rev quote to end of line) is unprovable as coded: Unicode `\d` accepts `2٢٢` and a genuine leading-quote record is refused (`gate-records.py` line 76 and line 117, per `MANIFEST.json` rounds[83] `verification.rechecks`).

## Counts per class

| Class | Falsified claims (of 11) | Rounds (of 6) |
|---|---|---|
| (a) green but unprovable wording | **11/11** | **6/6** |
| (b) instrument never green | 0/11 | 0/6 |
| (c) before/after did not re-derive | 0/11 | 0/6 |
| (d) non-author re-run disagreed | 0/11 | 0/6 |
| (e) structural defect nothing in the lane could see | 0/11 | 0/6 |

Total claims declared: 12 (2 per round). Falsified: 11. Verified: 1 (R83 C1 depth). Every falsified claim's instrument printed green on its frozen predicate at the claimed revision; every kill was committed by the lane's own wave and disclosed by the lane before closure. No closure disagreed with a lane verdict; spot-checks agreed with every honest stop.

**Recurrence: yes — same class every round.** Chousa matches tameshi (9/9 (a)), kama (3/3 (a)) and tsukuroi (3/3 (a)). Difference of shape, not of class: chousa declares two claims per round and falsifies both in 5/6 rounds (only R83 C1 verifies), and its (a) has a documented surface change at round 81 — rounds 78–80 kill on forger/counter oracle inputs (normalizer, payload decode, hollow and unopened records), rounds 81–83 kill on semantic overstatement the binding counter cannot see (filler entries, Never-row contradiction, leading-quote and Unicode grammar). [INFERENCE] Round 80 C1 draw-dependence is the one sub-form that fails closed (MISS/MISS) rather than false-green, but it is still (a): the wording asserts a deterministic predicate over a stochastic draw.

## Pre-file gate

**Yes.** A lane-side pre-file gate could have caught every falsification before filing, because in each round the killing artifact existed in lane custody (wave receipt or committed source) before the report. What it must check, all computable from lane-held evidence before freezing:

1. **Cheapest-content control.** The frozen depth/operability counter must refuse hollow/filler entries by name (r81 filler pair `r09`, r78 hollow repair lines, r80 hollow/unopened records). A PASS on any hollow input is a freeze failure. The lane already named this class itself at QUALITY 162 but never made it a freeze gate.
2. **Kill-clause/predicate enumeration match.** The kill rule's clause count must equal the predicate's counted set (r79 "any forger" vs six counted is the canonical mismatch). Any input class the kill clause names that the predicate does not enumerate blocks the freeze.
3. **Parser-property and grammar controls.** Duplicate-heading, blank-window, mixed-carrier, Unicode-digit and leading-quote mutants must be in the frozen control set and refused by name (r79 duplicate-116, r81 placeholder cells, r82 duplicate `##`, r83 `2٢٢` and leading `"`). Closure already routed this at r82 ("r83's gate claim must include duplicate-heading, fenced and commented table records").
4. **Draw-stability.** A per-run drawn predicate must be frozen as a distribution (pass rate over N draws), not a single receipt line; a FAIL draw on committed receipts blocks the filing as verified.

## Dominant mechanism

Chousa's failure is class (a) at 11/11 falsified claims (6/6 rounds; (b)/(c)/(d)/(e) all 0/11): the frozen counter goes green on the channels it enumerates while the claim's wording covers at least one channel or semantic property the lane's own wave then counterexamplets in the same round.

| (a) | 11/11 claims, 6/6 rounds |
| (b) | 0/11 |
| (c) | 0/11 |
| (d) | 0/11 |
| (e) | 0/11 |

Strongest verbatim quotes:

- `.ufo/reports/round-79/chousa.md:9`:
  > "kill rules fired on inputs the predicates do not enumerate — the round's admission is false on the rules declared before data."
- `chousa-shokunin/corpus/lessons/round-81-verifier-spotcheck.md:50`:
  > "The counter therefore does not separate depth from filler."
- `.ufo/reports/round-81/chousa.md:17`:
  > "Every frozen predicate in that run was falsified by the next forger, and depth, coverage and freshness stayed `unchanged` throughout."
