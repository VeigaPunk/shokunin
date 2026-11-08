# kama — round 98

Lane `kama` (operability + calibration; local model serving and endpoint health). L1 `KamaR98`.
Base `681c80a4e3c745c22559f74b2c2a1917bdc66fc6` (round-97 closed `ok`). Freeze `34ad44e9`; amendment 1
`3185c257`; measurement candidate `160e22dd`; wave evidence `380982b1`. Lane tip at filing:
`git -C kama-shokunin ls-remote origin refs/heads/master` → `380982b12b2b93463bec89f9a34f6d51391163b8`.

## Work performed

**Declared claims (3, distinct axes, causally separable):**

- **C1 — calibration (lowest non-retired axis, 7):** the lane's **20 named** self-assessment surfaces
  match the repo, heading included — SCORECARD's live `depth`/`adjacency` cells, the probe's ceiling
  comment and charged sites, the §Round 96 table, S620/S621/S622, the round-96 identity and receipt
  quotes, count agreement (six cells / five mutants / `cells=19`), the named overcharge surface, and
  the §Round 97 heading's count word with exactly one live heading.
- **C2 — operability (assigned axis):** the budget counter grades the **+1/header overcharge** probe
  the 17 round-97 cells cannot see — two new cells inside the window where the real parse decides
  `invalid` and a uniform +1 parse cannot.
- **C3 — depth (lowest non-retired axis, 7):** `SKILL.md` §Round 97 correction states the two
  overcharge-window rows and the four-preamble grounding from S622, all recomputed from `MAX_STEPS`.

**Work items:**

- **Froze the round** (`34ad44e9`): `plans/round-98-claims.md`; three counters
  (`tools/round98-self-assessment-audit.py`, `-router-budget.py`, `-depth-boundary-audit.py`);
  S622 (GGUF `gguf_header_t`, the four preamble fields) and rejected S623 (naming convention);
  `claims.json`; the 12-seat wave spec; every freeze-time control under
  `.ufo/waves/round-98/controls/` (census start exit 0, `c1-base` 4 mismatches exit 1, `c3-base`
  4 mismatches exit 1, `c2-legacy-mutants` `cells=17 cells_ok=17 survived=1`, `c2-new-mutants`
  six cells and five named catches).
- **Wave 1, 12 seats** dispatched through the inline handoff (`.ufo/waves/round-98/w1.ready` →
  `w1-dispatch.json` → `spawned kama 98 w1 12` at 10:26:02); all 12 settled and 12 reports exist in
  `.ufo/waves/round-98/w1/`. Attack seats 7 (58%): RV01/RV02 reviewers, CR01/CR02 critics, MT01
  mutation-tester, SN01 sentinel, RV03 revenger, CN01 connector; building seats 5: SC01/SC02 scouts,
  EX01/EX02 executors. Seat roles and counts read from `w1-results.json` (12 seats, 0 dead).
- **Amendment 1** (`3185c257`), recorded **before any measurement** (`measured/` was empty): the C1
  count term that no edit could satisfy (`adds (\w+) cells` vs a docstring saying "new set = six
  cells"), the `+1/header` probe both audits were blind to (now a graded term in C1 check 18 and
  C3), the numeral-heading false red and duplicate-heading hole, the window's lower-edge off-by-one,
  the false `W11` lower-bound clause, the over-wide C1 headline, and lesson M2's attribution. Its
  artifacts are `SN01StepFlips`, `RV01SelfAssess`, `CR02Wording`.
- **Prefile falsification ledger:** `python3 /home/vgpnk/Projects/shokunin/scripts/hyaku/prefile-falsification.py --lane kama --round 98`
  → `PREFILE-FALSIFICATION: pass claims=3 rows=24 attack_seats=8 findings=0`, **exit 0**;
  `.ufo/waves/round-98/claim-falsification.tsv` (24 rows; every attack seat read; every
  `falsifies-wording` row names `plans/round-98-amendment-1.md`).
- **Frontier step:** `corpus/SOURCES.md` 361 → 363 rows (S622 admitted, S623 rejected), census
  exit 0 at round start and at round end; `corpus/lessons/round-98.md` carries `## Gate` (one admit,
  one reject, with URL, access date, digest and located quote) and `## Mistakes` M1–M3.
- **Assimilation:** none from `merge/kama/`; `considerthese/2026-11-08.md` proposal 1 (gate-receipt
  continuity) is recorded as a lesson note only, per §10.

## Landed changes

| Change | LOG.md entry | Commit |
|---|---|---|
| Frozen plan, three counters, S622/S623, `claims.json`, wave spec, freeze-time controls | round-98 freeze paragraph | `34ad44e9` |
| Amendment 1: reachable count term, overcharge term in C1/C3, single-heading rule, window edges, M2 | round-98 amendment paragraph | `3185c257` |
| M1 candidate: SKILL eight boundary rows + five forgeries + S622, SCORECARD depth row re-anchored | round-98 measurements paragraph | `160e22dd` |
| Measurements, SCORECARD §Round 98, two capability rows, LOG, falsification ledger, lesson | round-98 measurements paragraph | `3b71d098` |
| Wave evidence: 12 seat reports, `w1-results.json`, dispatch, census end, ledger and lesson corrections | round-98 wave paragraph | `380982b1` |

`LOG.md` carries one `## round 98` section with the freeze, amendment, measurement and wave
paragraphs; the table's cells name those paragraphs, not separate headings.

## Before → after measurements

**C1 — calibration.** Counting command
`python3 tools/round98-self-assessment-audit.py --repo . --rev <rev>`.

- Before (`controls/c1-base.out`, base `681c80a4`): `SELF_ASSESS98 checks=20 mismatches=4 met=False`
  — **exit 1** (the heading word `three`, the count surfaces at four/17, W18/W19 absent, the
  overcharge name absent).
- After (`measured/c1.out`, `160e22dd`): `SELF_ASSESS98 checks=20 mismatches=0 met=True
  rev=160e22dd skill_sha256=3021fc5d…` — **exit 0**.
- Amendment-1 control (`controls/c1-amendment1-overcharge.out`): the same instrument on a scratch
  clone whose probe adds one `steps[0] += 1` in the tensor loop → `mismatches=1`, **exit 1**; the
  honest probe is green. The wave produced this: SN01 measured the pre-amendment instrument green on
  that probe.

**C2 — operability.** Counting command
`python3 tools/round98-router-budget.py --repo . --rev <rev> --work <scratch> --slow-files 72`.

- Before: the 17 round-97 cells pass the overcharge mutant —
  `controls/c2-legacy-mutants.out`, `cells=17 cells_ok=17 … survived=1`, **exit 0**.
- After (`measured/c2.out`, `160e22dd`): `ROUTER_BUDGET98 cells=19 mismatches=0
  positive_mismatches=0 load_cells=19 load_stable=1 budget=work probe=rev mutant=none slow_files=72
  runs=2 probe_sha256=40ab387e… base_sha256=27065a5c… rev=160e22dd w03_seconds=85.9`, **exit 0**
  (`load1_nat=141.68`; the loaded leg ran under the counter's own 64 burners).
- Catch controls (`controls/c2-new-mutants.out`): real probe `cells=6 cells_ok=6 survived=1`; each
  mutant's named cell red — flat6 → W15-700k-nd4, undercharge → W14-900k-nd1, maxmeta →
  W16-maxmeta, nopreamble → W17-833333-nd1, overcharge → W18-800k-nd1 (`cells_ok=4`) and →
  W19-520k-nd4 (`cells_ok=4`), each `cell_ok=0 caught=1 ok=1`.

**C3 — depth.** Counting command
`python3 tools/round98-depth-boundary-audit.py --repo . --rev <rev>`.

- Before (`controls/c3-base.out`, `681c80a4`): `DEPTH_BOUNDARY98 rows=6 checks=13 mismatches=4
  met=False` — **exit 1** (two required rows missing, S622 absent).
- After (`measured/c3.out`, `160e22dd`): `DEPTH_BOUNDARY98 rows=8 checks=13 mismatches=0 met=True
  rev=160e22dd` — **exit 0**.

**Independent re-derivation (wave):** MT01's six own mutants — KV steps doubled, flat 6, `MAX_META`
100 MiB, −1/header, +1/header, +2/header — reproduce the expected matrix
(`.ufo/waves/round-98/w1/out/MT01Forgeries/matrix_final.json`): +1 survives 13/13 and 17/17 and is
caught only by W18/W19; −1 is caught by W14/W17; +2 is caught by W11 and by W18/W19; the KV-doubling
mutant survives all three sets and is exactly the disclosed limit (a). SN01 measured all four window
fixtures `invalid` as predicted, with the step budget (not the size guard, not `MAX_TENSORS`)
deciding.

## Sources & frontier

`SOURCES.md` rows before → after: **361 → 363**. Counting command:
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kama`
→ `kama ok …`, **exit 0** at round start (`controls/census-start.out`) and at round end
(`controls/census-end.out`). Tiers at both ends: A 345 (after: S622 admitted A; base 344), B 11,
C 7 (after: S623 rejected C; base 6); statuses after: mined 325, queued 8, rejected 30.

- Rows added by tier: **1** A-tier row — S622 (spec, ggml `57e2c2ca`, sha256 `1dead27b…`, quote
  "struct gguf_header_t {" line 277, grounding the four preamble steps); **1** rejected row — S623
  (the spec's naming-convention section, line 23 quote, grounds no header cost).
- Rows touched old → new: none (`status`/`recheck`/`used-by` unchanged on every existing row).
- Frontier rows advanced: the boundary table now carries the overcharge window and cites the header
  struct; the self-assessment surface now grades a section heading and the charged sites of the
  parser's tensor loop.
- Both new rows share S620's URL with a different anchor — a standing `W04` duplicate-URL warning
  (cross-scope), the same situation as round-97's S619.
- Assimilation: none taken from `merge/kama/`; `considerthese/2026-11-08.md` proposal 1 is a lesson
  note, not an adoption.

## Trend verdicts

- **expansion: unchanged** — one spec row grounds a term the lane already priced; no new admitted
  `knowledge/` entry and no new governed surface. No coverage regression.
- **quality: improved** — C2 replaces a cell set that passed the +1/header forgery with one that
  reddens on it in two independent cells and keeps all 17 old cells green; C1 replaces an audit that
  could not see its own section heading with one that grades the heading, requires a single live
  heading and fails on an overcharging parser; C3 adds the overcharge-window rows and grades the
  tensor loop's charge sites. Each carries a red-before control.
- **discernment: improved** — the wave falsified the freeze-time filings before filing: the
  unreachable count term and the overcharge blindness (SN01), the numeral/duplicate-heading shapes
  (RV01), the false `W11` clause and over-wide headline (CR02); amendment 1 answers each with a
  re-frozen instrument and a measured control.

## SHONEN

- [~] **SKILL.md contains real decision tables, error patterns, checklists, cited sources.** Author
  assertion: §Round 97 correction (eight boundary rows, five graded forgeries, the overcharge
  window), §Round 96 step-cost table, §Serving defaults, §Probe reason codes; sources S620/S621/S622
  opened and quoted (`corpus/SOURCES.md:375-378`). No named non-author verifier.
- [~] **At least one end-to-end domain task executed and logged in LOG.md.** Author assertion: the
  round executed the probe through the counter's stub against 19 fixtures at both host loads
  (`measured/c2.out`, 19/19, `load_stable=1`), the six-mutant matrix (MT01), the four window fixtures
  end to end (SN01), and the three counters at base and candidate; LOG §round 98 records them with
  commit pointers. No named non-author verifier.
- [~] **Instructions executable by an agent without oral context.** Author assertion: each counter
  re-runs from its frozen command and prints the documented line; the plan, amendment and lesson
  name every input, receipt and control path. No named non-author verifier.
- [~] **No cross-domain bleed (PROVINCE.md still accurate).** Author assertion: `PROVINCE.md` §Write
  boundary unchanged; CN01Overlap finds no sibling-ground absorption and SC01SiblingScan finds the
  two shapes in six sibling lanes without adopting any; out-of-province findings (the host's non-lane
  Ollama listener, `round75-instruments`) stay reported, not absorbed. No named non-author verifier.

## Routed to round 99 (disclosed, not claimed)

1. `round75-instruments` red (`APPEND_DEBT … bad_rows=19`, L0 r87/r89 open).
2. The `round78-instruments` red from the host's non-lane Ollama listener on 127.0.0.1:8080.
3. The slow `/props` verdict still decides the verdict (r94 SC02 F4).
4. The pass-level wrapper is still a wall clock (SC01).
5. The ctime memo shape remains unobservable from the probe's public path.
6. C2 limit (a): a probe that doubles the KV/string-element charge survives all three cell sets
   (MT01 `A_kv2x`); a KV-step cell is the next shape.
7. C1 check 16/19 grade counts by word (`WORDS` stops at nine) — a numeral or ≥10 population would
   need the parser widened (RV01 shape b).
8. The `--control` path never compares `n` to the selected-set size, so a short cell set prints
   `survived=1` and exits 0 (CR02 M2 finding); the counter-level fix belongs to the next successor.
9. The two late seats wrote `w1/<Name>.md` while the rest wrote `w1/out/<Name>/`; one output
   convention in the brief is routed to the next wave (lesson M3).

**Stale-lane:** no — respawn-per-round driver; no other mission of this lane is open. Tool installs:
none this round.
