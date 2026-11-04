# tameshi-shokunin — round 77 report (hyaku run 15, attempt 1)

Lane repo: `/home/vgpnk/Projects/shokunin/tameshi-shokunin`, branch `master`,
tip `678f8c88d4434144418ba6bfa9d9b5125762e7a8` (`origin/master` equal; clean
tree, `ahead=0`). Base `ac6baf7a46df613b171b4c1ab834c888cd6321b9` (the
round-76 non-author closure verdict commit). Round range
`ac6baf7a^..678f8c88` inclusive = 9 commits (base 1 + round 8).

**Stale-lane:** respawn-per-round driver (hyaku-inline, attempt 1); no other
mission of this lane is open.

**Round shape.** ONE v1 wave (`w1`) under `scripts/hyaku/ufo-wave-policy.json`
(band 8–16): **12 seats**, 4 executor · 1 scribe · 1 scout · 2 reviewer ·
1 critic · 1 mutation-tester · 1 connector · 1 sentinel; **attack seats 4 =
33.3 %** (reviewer, reviewer, critic, mutation-tester); 1 connector seat;
`labrat` is a frozen-topology seat the validator rejects, so none exists and
the planner seat stays with the L1 (orchestrator ruling 2026-10-19). 12
dispatched, **12 settled, 0 dead**, 12 non-empty seat reports; no residual
call, round total **12**. `w1-results.json` records 12 seats and 12 results;
`w1-dispatch.json` `counts={spawn:12,resume:0,total:12}`, no `model` key on
any task. Tool installs this round: **none** (no install, no upgrade, no
pacman transaction — the host pause was respected).

## Work performed

Two claims, each an axis-move with its own falsifiable before→after, frozen in
`plans/round-77.plan.md` at `d39be4b04474bf393fee24ee2ac47de58e0159fd` before
any seat ran and before the first content edit:

- **R77-C1 — operability (sourced on S305, opened this round):** the round-76
  wave's recursion survivor becomes measured arm20 of
  `tools/wave-reconcile.py`.
- **R77-C2 — calibration (the lowest scored axis at 8):** the cold-read credit
  the record claims is the monitor's reading at the revision the record names.

- Freeze + design evidence: `plans/round-77.plan.md` (predicates, counters,
  kill matrix, kill rule, control, `coldread_forecast`) with the design-phase
  candidate, the extended spec, every battery stream and the base survivor
  control committed in the same commit (`d39be4b0`; evidence
  `.ufo/evidence/round-77/design/`).
- **C1 work** — `tools/wave-reconcile.py` gains
  `arm20-nested-listing-recursion` (`SELFTEST_ARMS` 19 → 20): a real git
  fixture (`mkdtemp` + `git -C init`, toplevel realpath-verified, removed in
  `finally`, TMPDIR-honoured) holding `wave/one.md` + `wave/nested/two.md`,
  measured through the production `GitReader`; `tools/wave-reconcile-mutants.spec`
  gains the eighth defect `git-listing-recursion-removed` (the exact single
  edit, first seven blocks byte-identical). Evidence: the landed selftest
  header (rev + tool sha256 `67d3a4cc2e75…`) and the battery
  (`.ufo/evidence/round-77/c1-landed-selftest-wr.txt`,
  `c1-landed-battery.txt`); base control
  `.ufo/evidence/round-77/base-survivor-r77.txt`.
- **Sourced ground** — S305 appended to `corpus/SOURCES.md` (git-scm
  `git-ls-tree`: `-r` "Recurse into sub-trees.", page line 1664; "directory
  name (without -r) will behave differently", page lines 1631-1632; snapshot
  `.ufo/evidence/round-77/sources/s305-ls-tree.html`, sha256 `ff06fbc8…`).
  Census exit 0 before and after (165 rows at the tip).
- **C2 work** — three settlement batches of the lane's own rekey machinery
  (`coldread-rekey-rebind-r77.py`, the round-76 tool copied and patched for
  the round-77 trace path; union plan from `union-plan.py`; manifest generated
  by `gen-manifest-r77.py`, every verification a real `git show PIN:PATH`
  regex count). Batch 1 at the content tip `1d91c384` rekeyed the monitor's
  **14** uncredited sections (ledger 930 → 944); batch 2 at the records commit
  `aa8b00c6` rekeyed the **2** sections that commit staled (944 → 946);
  batch 3 at the disclosure commit `e80961b6` rekeyed the same **2** sections
  (946 → 948). Each batch's section set equals the monitor's measured
  uncredited set at its pin — nothing added, nothing dropped
  (`rekey-plan.json` per batch, `REBIND OK` summaries).
- **Routed payments** (round-76 closure §6): §6.1 cold-read receipt scope paid
  by C2 plus the append-only correction of the mislabelled "at the landing tip
  (`b2b0f82a`)" sentence; §6.2 every selftest receipt this round carries the
  measured rev and tool sha256; §6.3 the standing sweeps have combined tip
  receipts (`.ufo/evidence/round-77/standing-sweep-wr-r77.txt`,
  `standing-sweep-ss-r77.txt`); §6.4 the report gives the base revision and an
  explicit inclusive range; §6.5 carried with written reasons (below).
- **New criterion** — `corpus/QUALITY.md` criterion 128 (a settlement's
  restored credit is measured at the settlement commit; a record never names a
  pre-settlement revision as the tip), grounded in the round-76 defect and
  in `considerthese/2026-10-28.md` proposal 1 (mined, read-only).
- **Wave** — 12 seats re-derived and attacked both claims: E1/E2/M1/R1
  replicated the 20/20 and the 8/8 kill matrix independently (identical kill
  sets); E3 rehearsed the whole settlement in a sandbox clone and established
  the ordering with a negative control; E4 reproduced the standing sweeps,
  the range arithmetic and the registry population; S1 drafted the lesson and
  criterion shape; SC1 opened S305 and the ledger pins; R2 verified the base
  counter, both uncredited headings and the box3/probe contracts; C1 falsified
  the plan's language in five places; CN1 found no sibling duplicate and gave
  `Assimilation: none`; SN1 found no misroot, no secret and no TMPDIR
  violation in the new arm. All findings adopted (below).

## Landed changes

| Lane commit | What it carries | LOG.md entry |
|---|---|---|
| `d39be4b0` | frozen plan + design-phase candidate, spec, battery, base control | round-77 measured block (declaration) |
| `1d91c384` | C1 tool + eighth spec defect, S305 row, QUALITY criterion 128, round lesson, landed receipts | "Round 77 — measured" |
| `29a1a7d0` | settlement batch 1 (14 sections; ledger 930 → 944, traces-b1) | same block (C2 after) |
| `aa8b00c6` | records: SCORECARD measured block (both claims, no-harm, round-76 correction), LOG block, lesson after-line, after-receipt | same block |
| `af754b92` | settlement batch 2 (2 sections; 944 → 946, traces-b2) | same block (ordering) |
| `e80961b6` | wave disclosures: nudge off-by-one, C1 scalar, C2 counter scope, separability correction, two named survivors, provenance limit | "Round 77 — appended: wave disclosures" |
| `b3147174` | settlement batch 3 (2 sections; 946 → 948, traces-b3) — the last content-bearing commit | same appended block |
| `678f8c88` | wave evidence: 12 seat reports, dispatch/spec/ready, census end, tip cold-read receipt | — (evidence) |

## Before → after measurements

**R77-C1 — operability.** Counting command (run from the lane repo; the
selftest line names the arm count, the battery line names the surviving
registered defects — the claim's scalar):

```sh
python3 -I -X utf8 tools/wave-reconcile.py --selftest | tail -1
bash tools/mutate-and-run.sh --target tools/wave-reconcile.py \
  --defects tools/wave-reconcile-mutants.spec \
  --suite 'python3 -I -X utf8 "$MUTANT" --selftest' \
  --workdir "$HYAKU_SCRATCH/tameshi-r77/l1/battery" --label wave-reconcile-arms-r77
```

- Before (base `ac6baf7a`): `WAVE_RECONCILE_SELFTEST: 19/19 pass`; the
  `git-listing-recursion-removed` mutant on base bytes also reads `19/19
  pass` — **1 surviving registered defect** on this surface, and the seven
  existing defects are the only scored kills (`.ufo/evidence/round-77/base-survivor-r77.txt`).
- After (measured commit `1d91c384`, re-verified at the tip):
  `WAVE_RECONCILE_SELFTEST: 20/20 pass` exit 0; battery
  `MUTATE: DONE (target=wave-reconcile-arms-r77 defects=8 killed=8 survived=0
  inconclusive=0 kill-rate=100%)` with `CONTROL: GREEN` and `MUTATE_RESTORE:
  OK` byte-identical (tool sha256 `67d3a4cc2e75ef7211a8588e43dcaf3874aaec66c3eea1d59a2b43b5a35e4e84`)
  — **0 surviving registered defects**. Kill matrix as frozen: `m2` →
  arm13+arm16; `span-rule-removed` → arm14+arm17+arm18; `seat-reports-any-depth`
  → arm15+arm20 (disclosed intrinsic collateral); `mc-record-bound` → arm16;
  `roles-bypass` → arm17; `attack-bypass` → arm18; `adv-seatreports-…` →
  arm19; `git-listing-recursion-removed` → arm20 only.

**R77-C2 — calibration.** Counting command:

```sh
python3 -I -X utf8 tools/coldread-precheck-portable.py --repo . --rev <REV> \
  --work <scratch> --out <json>
# then read measure.sections_covered / sections_total / box3_full_page from <json>
```

- Before (base `ac6baf7a`): `COLDREAD_PORTABLE rev=ac6baf7a46df credited=63/65
  elapsed=2.7s probe_sampled=20 probe_mismatches=0`;
  `sections_covered=63 sections_total=65 box3_full_page=false`; the two
  uncredited headings are `## Standing rules` and `## Mutation-sweep recipe —
  numbered steps; bounded cold-read evidence`
  (`.ufo/evidence/round-77/coldread-base-r77.json`).
- After (settlement commit `b3147174`; the same line re-read at the final tip
  `678f8c88`): `COLDREAD_PORTABLE rev=678f8c88d443 credited=65/65
  elapsed=3.5s probe_sampled=20 probe_mismatches=0`;
  `sections_covered=65 sections_total=65 box3_full_page=true`
  (`.ufo/evidence/round-77/coldread-tip-r77.json`). The records commit that
  follows each settlement is priced: batches 2 and 3 exist because the
  SCORECARD/LOG appends stale exactly those two sections (measured before each
  batch, never assumed).

**Routed defect payment, measured.** `git rev-list --count 451ed5cb..d2d00e3f`
= 11 and `git rev-list --count '5b7bbe1a^..d2d00e3f'` = 11 — the round-76
report's "11 lane commits, `5b7bbe1a..d2d00e3f`" names a 10-commit range
(§6.4 paid here by writing the base and an explicit inclusive range).

## Sources & frontier

Census (the frozen command) before and after, exit codes included:

```sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate \
  --root /home/vgpnk/Projects/shokunin tameshi
```

- Before `ac6baf7a`: exit 0, `tameshi ok …/corpus/SOURCES.md`, 20 output lines
  (18 × `W04` duplicate-url warnings + 1 × `W01 S101` + the ok line)
  (`.ufo/evidence/round-77/census-start.txt`).
- After `678f8c88`: exit 0, same warning set, ok line
  (`.ufo/evidence/round-77/census-end.txt`).

Rows: **164 → 165**. Added by tier: **A +1** (S305), B +0, C +0. Rows touched
old→new: none — S006's `used-by` from round 76 is unchanged this round; the
only registry delta is the appended S305 row (`status: mined`,
`opened 2026-11-04`, `recheck 365d`, `used-by corpus/lessons/round-77.md`).
Status counts 132 mined / 22 queued / 10 rejected → 133 / 22 / 10.
Frontier rows advanced: none — `corpus/README.md` is untouched; F1–F11 stand
as round 76 left them. **Assimilation: none** — `T77W1CN1` opened
`/home/vgpnk/Projects/shokuknow/merge/tameshi/MERGE-REPORT.md`,
`SOURCES.append.md` and all 81 staged knowledge files read-only; none touches
Git listing recursion or cold-read settlement, and the nearest candidate
(`survivor-classification.md`, staged S166/S156 with unresolved provenance) is
already held in substance. `considerthese/2026-10-28.md` proposal 1
(receipts that do not measure what they claim) was mined and landed as
criterion 128's rule, not as a note.

## Trend verdicts

- **expansion — unchanged.** No `corpus/knowledge/` entry, no capability row
  entered (C1 is an arm on an existing capability, C2 a settlement on an
  existing run-book), no frontier move (`corpus/README.md` byte-identical),
  registry 164 → 165 with the single sourced row above. Consequence named:
  rounds 75 and 76 had already filled the stagnation window (N = 2), so the
  nudge was active at round-77 start and stays active — round 78 should be the
  capability round.
- **quality — improved.** A named survivor becomes a measured arm with a frozen
  eight-defect matrix, control GREEN and byte-identical restore; the cold-read
  credit the record claims is restored and re-measured at the revision the
  record names (63/65 → 65/65, `box3_full_page` false → true) with the
  ordering validated by a sandbox negative control; criterion 128 captures the
  class; every receiver in this round names its measured revision and tool
  sha256; the standing sweeps read `WAVE_RECONCILE: rows=6 met=6
  unexpected=0` and `SELFSTATE: rows=20 match=18 stale=2 unexpected=0` at the
  content tip.
- **discernment — improved.** The wave's falsifiers were adopted rather than
  argued away: the plan's stagnation sentence (off-by-one), C1's multi-value
  after-state (scalar named, admission defect kept), C2's counter scope (the
  record half measured by a separate grep), the false "neither counter reads
  the other's files" sentence (C2's `needed_paths` pins
  `tools/wave-reconcile.py`), and the provenance limit (the monitor does not
  authenticate `read_rev`). Two survivors are carried with their fixtures for
  round 78: arm20's `finally` cleanup (green suite, one leaked fixture per run)
  and `git-listing-uses-head`. The round-76 closure's disputed claims are
  corrected append-only, and no claim target was narrowed after landing.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — lane assertion; this round adds no `SKILL.md` bytes; standing pointer `reports/round-1-calibration.md#box-1` (no independent promotion verifier).
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md` round-77 measured block; tasks: arm20 build + battery, three settlement batches; pointer `LOG.md` "Round 77 — measured" (lane assertion, no independent promotion verifier).
- [~] Instructions executable by an agent without oral context — the frozen plan, the round lesson and the wave's 12 seat reports were executed from committed bytes alone this round (`.ufo/waves/round-77/w1/`); standing pointer `.ufo/evidence/round-21/coldread/ledger.json` (lane assertion, no independent promotion verifier).
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` byte-identical base→tip; the wave's connector found no sibling duplicate and absorbed nothing; `T77W1CN1` §2 (lane assertion, no independent promotion verifier).

## Carries and open questions

- Carried with reasons (lesson `## Findings and carries`): the two
  bash-instrument gaps (`MUTATE_SELFTEST: 107/107`, `REGRESSION: PASS
  (cases=10 …)`) need a selfstate runner widening plus a frozen tuple table;
  the registry gap (17 of the 44 `--selftest`-carrying **Python** tools — `T77W1E4`
  re-derived the population, 45/28/17 when `.sh` sources are included).
- Named survivors for round 78: arm20's cleanup (`T77W1M1`) and
  `git-listing-uses-head` (`T77W1E2`).
- L0 questions: none new. No operator decision blocks this round.

## Errors and self-corrections

- The round's own first draft of the SCORECARD/LOG blocks said the stagnation
  nudge "fires for round 78"; the wave critic caught the off-by-one and the
  record carries an append-only correction rather than a silent edit.
- The plan's separability sentence was wrong; it is corrected in the record
  and named here, not quietly dropped.
- `tools/rekey-cost.py`'s forecast (`at_risk=14 predicted_lost=14`) matched the
  measured batch-1 set exactly; the two later batches were not forecast in the
  plan text (the plan priced one rekey batch). The extra two batches are an
  ordering consequence of appending records after a settlement, priced per
  commit and measured before each run.
- The `union-plan.py` prefetch cache landed under
  `.ufo/evidence/round-77/rekey/work-analyze/` in the lane worktree; the L1
  removed it before the evidence commit (a cache, not evidence).
- A fleet-root file `after` (24 bytes, "== SCORECARD diff base-", mtime
  2026-11-03 20:05) predates this round and names neither the lane nor the
  round; it is not this round's misroot and was left untouched. The fleet
  repo's other untracked entries (`.scratch/*`, `.ufo/reports/round-76/kumitate.md`)
  are orchestrator- or sibling-owned and untouched.
