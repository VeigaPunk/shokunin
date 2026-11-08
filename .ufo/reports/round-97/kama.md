# kama — round 97

Lane `kama` (operability + calibration; local model serving and endpoint health). L1 `KamaR97`.
Base `40763bd2ca1e3f99881247eaa9f5e3ef3b596653` (round-96 closure `rejected-honest-stop`). Freeze
`9e605d41`; amendments 1 `e057166e` (C2 host-speed parameter) and 2 `be590351` (wave-1 findings);
wave evidence `be590351`; measurements `ac014090`. Lane tip at filing:
`ac014090e99b3ef90d71e657b9173ee1a15e8e80` (`git -C kama-shokunin ls-remote origin refs/heads/master`).

## Work performed

**Declared claims (3, distinct axes, causally separable):**

- **C1 — calibration (lowest non-retired axis, 7):** the lane's graded self-assessments match the
  repo — SCORECARD's live `depth`/`adjacency` cells, the probe's ceiling comment and its charged
  sites, `SKILL.md`'s step-cost citations, S620/S621, the round-96 identity and receipt summaries,
  the round-97 counters' docstrings and count statements, and unique source ids.
- **C2 — operability (assigned axis):** the budget counter grades four probe forgeries the 13-cell
  round-96 set cannot see — per-header charging stopped, a constant 6 steps/header, `MAX_META`
  100 MiB, and the preamble charge dropped.
- **C3 — depth (lowest non-retired axis, 7):** `SKILL.md` §Round 97 correction states the six
  step-budget boundary rows for a KV-free, rank ≤ 4 file, each recomputed from `MAX_STEPS`.

**Work items:**

- **Frozen the round** (`9e605d41`): `plans/round-97-claims.md`, three counters
  (`tools/round97-self-assessment-audit.py`, `-router-budget.py`, `-depth-boundary-audit.py`), the
  corrected probe ceiling comment, `SKILL.md` §Round 97, S619/S620/S621, the refreshed SCORECARD
  `depth` row and `router-byte-decided` pointer, QUALITY KQ152, and every freeze-time control.
- **Wave 1, 13 seats** (attack 7: RV01, RV02 reviewers, CR01/CR02 critics, MT01 mutation-tester,
  SN01 sentinel, RV03 revenger, CN01 connector; scouts SC01/SC02; executors EX01/EX02; scribe SB01),
  dispatched through the inline handoff (`.ufo/waves/round-97/w1.ready` → `w1-dispatch.json`);
  reports in `.ufo/waves/round-97/w1/out/`; seat count and roles read from `w1-results.json`.
- **Amendment 1** (`e057166e`): the frozen C2 command gained the declared host-speed parameter
  `--slow-files 72` after the run at the freeze exited 2 (`W03 natural pass 55.0s`); no cell had
  scored.
- **Amendment 2** (`be590351`): the wave's blockers and gaps — the live "three vs four" count,
  the ungraded counter docstrings, the any-ancestor capability pointer, the literal-presence probe
  checks, the hardcoded formula, the unenforced six-row claim, the KV/rank class caveat — were
  repaired with `plans/round-97-amendment-2.md` and the counters re-frozen. Their artifacts are
  RV01SelfAssess §2.1–§2.12, CR01Boundary, CR02Wording, and SB01LessonDraft F1–F7.
- **Prefile falsification ledger:** `python3 /home/vgpnk/Projects/shokunin/scripts/hyaku/prefile-falsification.py --lane kama --round 97`
  → `PREFILE-FALSIFICATION: pass claims=3 rows=24 attack_seats=8 findings=0`, **exit 0**; the ledger is
  `.ufo/waves/round-97/claim-falsification.tsv` (24 rows; every attack seat read, every claim covered).
- **Frontier step:** `corpus/SOURCES.md` 358 → 361 rows (S619 rejected, S620 admitted, S621
  supersedes S618); `corpus/lessons/round-97.md` carries `## Gate` (four candidates), `## Mistakes`
  M1–M3, and the routed-defect answers.
- **Assimilation:** none from `merge/kama/`; `considerthese/2026-11-07.md` proposal 3 mined into
  `corpus/QUALITY.md` KQ152.

## Landed changes

| Change | LOG.md entry | Commit |
|---|---|---|
| Frozen plan, three counters, probe comment, SKILL §Round 97, S619–S621, SCORECARD refreshes, KQ152 | round-97 freeze entry | `9e605d41` |
| Amendment 1 (C2 host-speed parameter) and its receipt | round-97 freeze entry | `e057166e` |
| Amendment 2 (wave-1 repairs), re-frozen counters, wave evidence and the falsification ledger | wave-findings entry | `be590351` |
| Measurements, SCORECARD §Round 97, capability, controls re-run at the measured commit | measurements entry | `ac014090` |

## Before → after measurements

**C1 — calibration.** Counting command `python3 tools/round97-self-assessment-audit.py --repo . --rev <rev>`.

- Before (`controls/c1-base.out`, base `40763bd2`): `SELF_ASSESS97 checks=18 mismatches=10 met=False rev=40763bd2 skill_sha256=7b10579e…` — **exit 1** (the stale depth cells, the capability row's relative evidence path, the constant-6 sentence, missing ceilings and S620/S621, and the count/docstring surfaces).
- After (`measured/c1.out`, measured at `be590351`): `SELF_ASSESS97 checks=18 mismatches=0 met=True rev=be590351 skill_sha256=863eb35d…` — **exit 0**.
- The wave falsified the first version (RV01 §2.1 BLOCKER: a live "three vs four" count; §2.2–§2.4 false-shape passes; CR02 clause 5: green on a flat-6 parser); amendment 2 added checks 15–19 (docstrings, count statements, unique ids, the tensor-loop charge sites) and re-froze the counter, so each repaired surface is now graded.

**C2 — operability.** Counting command `python3 tools/round97-router-budget.py --repo . --rev <rev> --work <scratch> --slow-files 72` (amendment 1; the default count exits 2 on this host at 55.0 s).

- Before: the 13 round-96 cells pass all four mutants — `controls/c2-legacy-mutants.out`, `cells=13 cells_ok=13 … survived=1` for flat6, undercharge, maxmeta and nopreamble (receipts re-produced at the amendment commit).
- After (`measured/c2.out`, measured at `be590351`): `ROUTER_BUDGET97 cells=17 mismatches=0 positive_mismatches=0 load_cells=17 load_stable=1 budget=work probe=rev mutant=none slow_files=72 runs=2 probe_sha256=40ab387e… rev=be590351 w03_seconds=80.1 load1_nat=102.09` — **exit 0**
- Catch controls (`controls/c2-new-mutants.out`, re-produced at the amendment commit): real probe `cells=4 cells_ok=4 survived=1`; each mutant's named cell red — flat6 → `W15-700k-nd4 cell_ok=0 caught=1`, undercharge → `W14-900k-nd1`, maxmeta → `W16-maxmeta`, nopreamble → `W17-833333-nd1`.
- The wave falsified the first version (RV02 F2/MT01 F2: the shipped `nopreamble` patch was a fixed point that charged zero steps; RV03 F2: `--runs 0 --allow-clock` printed the frozen summary with nothing graded; RV02 F4/F7: receipts did not echo the flag and `KILL` was below the derived limit); amendment 2's addendum fixes the patch, refuses `--runs < 1`, echoes `slow_files`/`runs`/`entries`, and raises `KILL` to 3600.

**C3 — depth.** Counting command `python3 tools/round97-depth-boundary-audit.py --repo . --rev <rev>`.

- Before (`controls/c3-base.out`, base `40763bd2`): `DEPTH_BOUNDARY97 rows=0 mismatches=1 met=False rev=40763bd2` — **exit 1**.
- After (`measured/c3.out`, measured at `be590351`): `DEPTH_BOUNDARY97 rows=6 checks=10 mismatches=0 met=True rev=be590351` — **exit 0**.
- The wave falsified the first version's class width (CR01: KV-bearing files and `nd > 4` are outside the rows; CR02: "six rows" was not enforced); amendment 2 states the class caveat, requires the caveat tokens, and exits 1 when `rows != 6`.


## Sources & frontier

`SOURCES.md` rows before → after: **358 → 361**. Counting command:
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kama`
→ `kama ok …`, **exit 0** at round start (`controls/census-start.out`) and at round end
(`controls/census-end.out`); row tiers at HEAD: A 344, B 11, C 6; mined 324, queued 8, rejected 29.

- Rows added by tier: **2** A-tier rows — S620 (spec, ggml `57e2c2ca`, sha256 `1dead27b…`, quote
  "uint64_t dimensions[n_dimensions];" line 313) and S621 (code, `ggml.h` @ b12177, sha256
  `590e00a5…`, quote "nb[0] = ggml_type_size(type)" line 697, `teaches` opens `supersedes S618 —`);
  **1** rejected row — S619 (`gguf-py/README.md` @ b12177, docs, grounds no header cost).
- Rows touched old → new: none (`status`/`recheck`/`used-by` unchanged; S618 stays `mined` and S621
  is the append-only correction).
- Frontier rows advanced: the step-budget boundary now carries the two rank classes and the four
  graded probe forgeries; the disclosure surface now names the parser's charged sites, not only the
  formula string.
- Assimilation: none taken; `considerthese/2026-11-07.md` proposal 3 mined as KQ152.

## Trend verdicts

- **expansion: unchanged** — one spec row deepened a surface the probe already parses; no new
  admitted `knowledge/` entry and no new governed surface.
- **quality: improved** — C2 replaces a cell set that passed four probe forgeries
  (`controls/c2-legacy-mutants.out`), C1 replaces a self-assessment that described a 2254-line
  `SKILL.md` the repo no longer had and could stay green on a false count, and C3 adds the boundary
  decision with a class caveat; each has a red control.
- **discernment: improved** — the round's own wave falsified the freeze-time filings before filing:
  the count blocker (RV01 §2.1), the literal-presence probe checks (RV01 §2.2, CR02), the hardcoded
  formula and class width (CR01), and the unenforced six-row claim (CR02); amendment 2 answers each
  with a measurement and a re-frozen instrument.

## SHONEN

- [~] **SKILL.md contains real decision tables, error patterns, checklists, cited sources.** Author assertion:
  §Round 97 correction (six boundary rows, the four graded forgeries), §Round 96 step-cost table, §Listen
  port and slot-count setters, §Serving defaults, §Probe reason codes; sources S618/S620/S621 opened and
  quoted this round (`corpus/SOURCES.md:373-376`). No named non-author verifier.
- [~] **At least one end-to-end domain task executed and logged in LOG.md.** Author assertion: round 97
  executed the probe against the counter's fixtures at both host loads (`measured/c2.out`, 17/17 cells),
  the boundary flips at six `(T, nd)` classes (SN01StepFlips 12/12), and the four mutant controls; the
  LOG entry `round 97` records it with commit pointers. No named non-author verifier.
- [~] **Instructions executable by an agent without oral context.** Author assertion: the three counters
  re-run from their frozen commands and print the documented lines; the plans name every input, receipt
  and control path. No named non-author verifier.
- [~] **No cross-domain bleed (PROVINCE.md still accurate).** Author assertion: `PROVINCE.md` §Write
  boundary unchanged; CN01Overlap finds no sibling-ground absorption (its table cites the 8 closest
  sibling rows and says kama stays in its province); out-of-province findings (the host's non-lane Ollama
  listener, `round75-instruments`) stay reported, not absorbed. No named non-author verifier.


## Routed to round 98 (disclosed, not claimed)

1. `round75-instruments` red (`APPEND_DEBT … bad_rows=19`, L0 r87/r89 open).
2. The `round78-instruments` red from the host's non-lane Ollama listener on 127.0.0.1:8080
   (re-checked this round: still listening).
3. The slow `/props` verdict still decides the verdict (r94 SC02 F4).
4. The pass-level wrapper is still a wall clock (SC01).
5. The ctime memo shape is unobservable from the probe's public path (declared in the plan).
6. C1's checks 13–14 grade receipt needles, not every number in the round-96 headers (RV01 §2.10);
   the whole-row semantic truth beyond the 18 graded surfaces remains the non-author read's job.

**Stale-lane:** no — respawn-per-round driver; no other mission of this lane is open. Tool installs:
none this round.

---

## Erratum (appended in a new commit; supersedes no filed bytes, clarifies this report's Landed-changes column)

The Landed-changes table's "LOG.md entry" cells name three paragraphs, not three headings. `LOG.md`
has one `## round 97` section carrying, in order: the freeze paragraph (superseded by nothing;
`9e605d41`), the wave-1 paragraph and the amendment-2 paragraph (`be590351`), and the measurements
paragraph (`ac014090`). The table's cells "round-97 freeze entry", "wave-findings entry" and
"measurements entry" refer to those paragraphs; no separate headings exist. This erratum also
records that the wave evidence and the 24-row falsification ledger landed with `be590351`, and the
measurement-time receipts and controls re-run landed with `ac014090`.
