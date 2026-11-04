# kaidoku — round 80 report

- **Lane:** kaidoku (`/home/vgpnk/Projects/shokunin/kaidoku-shokunin`), round 80, attempt 1
- **Round shape:** ONE v1 wave (`r80-w1`) of 15 seats; no residual call; round total **15 seats**,
  **0 dead**, **0 notes**
- **Lane tip at filing:** `72f8c6e9ff2e2c740cee8ef96ffe4791c7d66366` (`ls-remote` prints it)
- **Stale-lane:** no; this is the respawn-per-round driver's round-80 seat, and no other mission of
  this lane is open.

## Work performed

The round declares **three claims on three distinct axes**, each a capability acquisition with a
frozen predicate, a kill rule and a frozen control:

- **R80-C1 — calibration — the delimited-token pointer rule.** A declared pin binds only where every
  occurrence is delimited by a slice edge or a character outside `[A-Za-z0-9._-]`, and a record that
  declares one client cell twice is counted (`checks_total 6`) and reported in `duplicates` instead of
  being collapsed last-wins.
- **R80-C2 — freshness (entering owned axis) — the receipt-provenance sweep.** Every landing-class
  receipt of rounds 60–79 must carry an `instrument.sha256` equal to a **committed** blob of its
  `instrument.path`; a working-tree-only digest or a symbolic rev is a defect, and round 69's forged
  instrument is the declared negative control.
- **R80-C3 — depth — clause-to-case binding with isolation proof.** Each of the nine
  `validate_receipt()` refusal clauses owns one SKILL decision-table row and one declared selftest case
  that must be present and failing when the clause is deleted in a copy.

Work items, each with its evidence pointer:

- **The four instruments and their base arms** — `tools/round-80/pointer-bind.py`,
  `strictness-battery.py`, `receipt-provenance.py`, `guard-battery.py`; base arms at the base revision
  in `.ufo/waves/round-80/l1/scores/{c1,c2,c3}-at-base.json` (commit `253fc817`).
- **The gate revision and the decision table** — eight new isolating cases in
  `tools/round-78/attack-gate.py` (29 → 37) plus the nine-row `SKILL.md` block (commit `b8260107`);
  mutant table at `.ufo/waves/round-80/w1/ExecGate/mutants.json` (`isolating true` on all nine).
- **The round-79 landing-receipt repair** — `.ufo/waves/round-79/l1/scores/c2-at-landing.json`
  re-taken at its own record rev with the committed instrument bytes (`40905d39…`) and a disclosed
  `instrument_supersessions` entry (commit `b00419fb`, corrected text in `6037f599`).
- **The wave** — 15 seats, evidence under `.ufo/waves/round-80/w1/` and
  `r80-w1-results.json` (15 seats, 15 non-empty outputs, 0 dead). Independent re-derivations:
  `ExecBinder` (its own binder, scored `candidate_false_greens 0` by this round's battery),
  `ExecProv` (its own sweep: base `receipts 34, flagged 2, unexpected 1`), `ExecGuard` (its own
  battery: base `guards 9, rows 0, survivors 9`), `ExecGate` (the nine cases and the mutant table),
  `ReviewerC1` (independent C1 scorer; found the landed duplicate-cell defect), `ReviewerC3`
  (independent clause enumeration; base 8 survivors / 1 killed), `ScoutGate`, `ScoutRecord`,
  `MutInstruments`, `SentinelScope`, `CriticClaims`, `ScribeSources`, `ScribeKnowledge`,
  `ScribeLesson`, `ConnectorSibling`.
- **Source curation** — S298 landed (tier A), S049 re-opened and its `used-by` extended, RFC 8259 §4
  refused as a duplicate of S049, one Wikipedia rejection with reason and flip, one
  Cloudflare-blocked candidate recorded as unreachable; census 202 → 203 rows, exit 0
  (`.ufo/waves/round-80/l1/census-end.txt`).
- **The record** — `SCORECARD.md` round-80 section with the three claim rows and the four capability
  rows, the `freshness` axis row, `corpus/README.md` coverage row, `LOG.md` entry, knowledge entry
  `corpus/knowledge/2026-11-04-r80-strict-tokens-and-provenance.md`, lesson
  `corpus/lessons/round-80.md` (seven mistake rows, one admit-side refusal) — commit `6037f599` and
  `c935b543`.
- **In-round repairs the wave forced** (all disclosed in `.ufo/waves/round-80/claims.json`
  `counter_repairs`): the C1 record arm now requires the Rule's conjunction; a symbolic declared rev
  is its own C2 defect class; the C3 printed command carries `--expect-sha256`; and the binder's
  duplicate cells carry a `base_id` so both bind. Predicates, targets and kill rules unchanged; every
  arm re-taken with the final instrument bytes.

## Landed changes

| commit | what | LOG entry |
|---|---|---|
| `84d68e90` | `plans/round-80-claims.md` (three predicates, kill rules, controls), the frozen strictness fixture set, the wave spec/dispatch/ready and the start census | `## 2026-11-04 — round 80: …` |
| `253fc817` | the four round-80 instruments, their selftests, the three base arms, the sources notes and the guard-table draft | same |
| `b8260107` | `tools/round-78/attack-gate.py` + eight isolating cases (37) and the `SKILL.md` decision table + four registry rows | same |
| `b00419fb` | the round-79 landing receipt re-taken with committed bytes; the registry rows' seven-cell fix | same |
| `6037f599` | the record: SCORECARD, LOG, corpus (S298, S049 `used-by`, knowledge entry, lesson, coverage row), `claims.json`, the C1/C3 landing receipts, the end census | same |
| `c935b543` | the wave's evidence (15 seats), the strengthened counters, the binder's `base_id` fix, the re-taken arms, the repair disclosures | same |

Every change above is carried by the LOG entry `## 2026-11-04 — round 80: the record's tokens bind
whole, a receipt names a committed blob, and every refusal clause owns a case` and its sub-bullets
(including `Round 80 — in-round repairs the wave forced`).

## Before → after measurements

All receipts are in `.ufo/waves/round-80/l1/scores/`; each records its own instrument digest,
`checked_at` and a 40-hex revision, and each `--validate` is defect-free. Base revision
`16dfa009bf143080dfcdfc5f9ec34bd359536d90`.

**R80-C1 — calibration** (measured at base `16dfa009` and at the landing `c935b543`):

<!-- counting-command: C1 -->
```sh
python3 -I -B tools/round-80/strictness-battery.py --root $ROOT --impl tools/round-80/pointer-bind.py --control-impl tools/round-79/pointer-bind.py --work $WORK --json-out $OUT
```
<!-- /counting-command -->

- Base arm (`c1-at-base.json`, `--impl tools/round-79/pointer-bind.py`):
  `cases 4`, `green_cases 2`, **`candidate_false_greens 4`**, `control_false_greens 4`,
  `candidate_green_refusals 0`, `ok false`, `validate` defects `[]`, exit 1.
- Landing (`c1-at-landing.json`): **`candidate_false_greens 0`**, `control_false_greens 4`,
  green refusals 0/0, `ok true`, `validate` defects `[]`, exit 0.
- Live arm (`tools/round-80/pointer-bind.py --root . --rev 16dfa009…`): `checks_total 5`,
  `matched 5`, `mismatches 0`, `unparsed 0`, `duplicates []`, `--validate` `{"checks": 5,
  "defects": []}`.
- **4 → 0** false greens on the frozen fixture set, with the control arm still 4 (the do-nothing
  control cannot reach the target), and no regression of the five live cells.

**R80-C2 — freshness** (base arm at `16dfa009`, landing arm at the record `6037f599`):

<!-- counting-command: C2 -->
```sh
python3 -I -B tools/round-80/receipt-provenance.py --root $ROOT --rev $REV --from-round 60 --to-round 79 --json-out $OUT
```
<!-- /counting-command -->

- Base (`c2-at-base.json`): `receipts 34`, **`flagged 2`**, `expected_control_flags 1`,
  **`unexpected 1`** naming `.ufo/waves/round-79/l1/scores/c2-at-landing.json`, `validate` defects
  `[]`, exit 1.
- Landing (`c2-at-landing.json`): `receipts 34`, **`flagged 1`**, `expected_control_flags 1`,
  **`unexpected 0`**, `validate` `{"defects": [], "flagged": 1, "receipts": 34, "unexpected": 0}`,
  exit 0.
- **1 → 0** unexpected unprovable receipts; the one remaining flag is the declared negative control
  `prov-forged-instrument.json`, so "flag nothing" is not the target.

**R80-C3 — depth** (base arm at `16dfa009`, landing arm at the gate/table commit `b8260107`):

<!-- counting-command: C3 -->
```sh
python3 -I -B tools/round-80/guard-battery.py --root $ROOT --rev $REV --expect-sha256 df6fb85670549ff1a03f925a3bed456cc3b64a311ae8681754c8efcc567149d6 --work $WORK --json-out $OUT
```
<!-- /counting-command -->

- Base (`c3-at-base.json`): `guards 9`, **`rows 0`**, `bound 0`, **`survivors 9`**, `pristine 29/0`,
  `--validate` defects `[]`, exit 1.
- Landing (`c3-at-landing.json`): `guards 9`, **`rows 9`**, `bound 9`, **`survivors 0`**,
  `pristine 37/0`, `target_pin.matched true` (`expected == actual == df6fb856…`), `--validate`
  defects `[]`, exit 0.
- **9 → 0** unpinned clauses, with the nine mutants each failing exactly their declared case
  (`w1/ExecGate/mutants.json`, `other_cases_failed []` on all nine).
- Naming: the receipt's numeric survivor count is `survivors_count` and `survivors` is the (empty)
  list; the frozen sentence's `survivors 0` reads as both.

**Counting commands as printed run** — all three blocks above were executed verbatim, from a
committed lane copy (`.ufo/waves/round-80/l1/counting-commands.md@a3e22df4`, byte-identical to this
report's blocks), under a four-key child environment with `$ROOT`/`$REV`/`$WORK`/`$OUT` substituted.
Each exits 0 with its declared counter: `.ufo/waves/round-80/l1/scores/verbatim-{C1,C2,C3}.json`
(`candidate_false_greens 0`, `unexpected 0`, `survivors_count 0`). `tools/round-76/plan-command.py`
could not run them: it refuses any script outside its own hardcoded `tools/round-76/` prefix
(`REFUSED: script outside tools/round-76/`, `.ufo/waves/round-80/l1/scores/plan-command-<block>.json`),
which is that instrument's limit and is routed, not hidden.

## Sources & frontier

SOURCES: 202 → 203 rows (census `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kaidoku` → **exit 0**, 203 rows, 24 `W04` duplicate-URL warnings: 23 pre-existing plus S298's documented re-anchor).

- **Rows before → after:** 202 → 203; counting command as above (start `.ufo/waves/round-80/l1/census-start.txt` 202 rows/23 W04, end `census-end.txt` 203 rows/24 W04).
- **Rows added by tier:** A: 1 (`S298`); B: 0; C: 0.
- **Rows touched old → new:** `S049` `used-by` `corpus/lessons/round-21.md` →
  `corpus/lessons/round-21.md, corpus/knowledge/2026-11-04-r80-strict-tokens-and-provenance.md`
  (recorded old → new in `corpus/lessons/round-80.md` `## Mistakes` M80-6). No `status` or `recheck`
  change.
- **Refused in-round:** RFC 8259 §4 as a *new* row — `S049` already holds that exact URL and scope
  (`.ufo/waves/round-80/l1/pre-append-url-check.txt` prints S049 and S289 for the RFC, S143 and S298
  for the `re` page); the Wikipedia `JSON` article (tertiary, and its ECMA-404 quotation undercuts the
  rule it appears to illustrate; flip recorded); a Cloudflare-blocked Stack Overflow page
  (`unreachable`, not fabrication).
- **Frontier rows advanced:** none. No `PROVINCE.md` frontier bullet moved this round; the new
  knowledge entry is on the lane's instrument layer, which the coverage map records as *held*, not a
  new carrier class (row `Instrument and record layer, round 80`). Coverage self-check at the tip:
  163/163 stems mapped, `mismatches 0`, `stem_score 10.0`
  (`tools/round-66/coverage-selfcheck.py --rev c935b543 --selfcheck`).
- **Assimilation:** `Assimilation: none` — the shokuknow package was not adopted this round (the
  round's claim budget went to the three routed defect families).

## Trend verdicts

- **expansion: unchanged.** No frontier → core move and no new source kind; the knowledge entry and
  the coverage-map row record instrument-layer ground already marked *held*. Counting command:
  `tools/round-66/coverage-selfcheck.py --root . --rev c935b543 --selfcheck` → `population 163`,
  `mapped 163`, `mismatches 0`, the same 10.0 as round 79.
- **quality: improved.** Two real defects in the lane's own evidence apparatus were found and fixed
  with receipts: the round-79 landing receipt named an instrument digest matching no committed blob
  (4 → 0 unexpected flags over 34 receipts), and the new binder gave a false unbound reason to a
  duplicate cell (`matched 5` → `matched 6`, `mismatches 1` → `0` on the frozen fixture). The gate
  gained eight isolating cases and the registry's two stale tallies are corrected (26 → 37 and 19 →
  21). Four counter under-enforcement paths the wave's seats found are repaired and disclosed, with
  the predicates, targets and kill rules unchanged.
- **discernment: improved.** The outside seats' findings are all answered and none is prettified:
  `CriticClaims`/`ReviewerC1` (the C1 disjunction and the symbolic-rev path) → two counter repairs
  with selftest cases; `SentinelScope` (the C3 printed command could not reproduce
  `target_pin.matched true`) → the command repaired; `ReviewerC1` §7 (a landed defect with a false
  reason) → the `base_id` fix; the remaining class (a case may kill two clauses; the instrument's
  population-relative `ok`) is routed with the landed one-to-one evidence. The round also refused a
  source it had opened (RFC 8259 §4 as a duplicate of S049) instead of appending it.

## SHONEN

`[~]` SKILL.md contains real decision tables, error patterns, checklists, cited sources — this round
added the nine-row `validate_receipt` decision table plus four registry rows with their verdict maps
(`SKILL.md`, section `Round-80 receipt-guard table`); a non-author verifier has not attested it, so the
box is partial, not `[x]`.

`[~]` At least one end-to-end domain task executed and logged in LOG.md — three counter runs
execute end-to-end on committed bytes at a pinned revision (base arms → landing arms → live arms),
logged under `## 2026-11-04 — round 80`; the artefacts are instrument-layer, and no promotion is
claimed from them.

`[~]` Instructions executable by an agent without oral context — the three counting commands are
printed in `counting-command` blocks in this report and were executed verbatim by
the L1 runner (`l1/scores/verbatim-{C1,C2,C3}.json`, exit 0, counters 0); `tools/round-76/plan-command.py`
refuses any script outside its own `tools/round-76/` prefix, and that refusal is recorded in
`plan-command-<block>.json`. The registry rows carry each instrument's entry command. Not `[x]` because no non-author has re-run them from the report alone.

`[~]` No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` was not edited this round;
its five pointer cells were re-read live and bind 5/5 (`c1-at-landing` live arm), and the round's
surfaces are the lane's own record and evidence layer, with no claim about an inspected target.

## Wave shape, seats and round total

- **One v1 wave** (`r80-w1`) under `/home/vgpnk/Projects/shokunin/scripts/hyaku/ufo-wave-policy.json`
  (band 8–16; validator exit 0, `counts.spawn 15`): **15 seats** — 4 executor, 2 scout, 3 scribe,
  2 reviewer, 1 critic, 1 mutation-tester, 1 sentinel, 1 connector. **Attack roles 4/15 = 26.7 %**
  (≥ 25 %); one connector (≤ 2).
- **Planner mapping:** the L1 held the canonical §3 planner seat; the validator rejects a `planner`
  role, and a bounded planning data-walk rode the scout/connector items (recorded here, per the
  orchestrator ruling of 2026-10-19).
- **Round total: 15 seats** (the wave alone; **no residual call**), **0 dead seats**, 0 notes;
  `r80-w1-results.json` reports 15 results with non-empty outputs (3.6 kB–11.9 kB).
- **Godspeed lead:** every seat prompt opens with `/skill:godspeed` and the verbatim directive bytes.

## Inherited state, misroot sweep, tooling

- **Inherited state:** none. `.ufo/watchdog.log` shows no `lane-dead-no-report kaidoku round=80`
  line (attempt 1 is the first), the lane tree was clean and pushed at round start
  (`ahead=0 behind=0 tracked=0 untracked=0`), and no uncommitted lane leftovers were found.
- **Misroot sweep:** `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows only
  orchestrator-owned `.scratch/*`, `scripts/hyaku/*` and `after` — no untracked file written by this
  round's seats at the fleet root; no file was copied or deleted, and no misroot is recorded.
- **Tooling:** no install or upgrade this round; no pacman transaction was attempted (host-wide
  pause respected).

## Limits and routed

- `--validate` remains internal consistency, not authenticity: a hand-authored receipt consistent
  with itself passes (rounds 78–79), and `SentinelScope` reproduced that limit for all three
  instruments.
- The C1 battery has no *green record* control; a candidate that reports `duplicates` on every record
  fails only the separate live arm (`duplicates []`), which a hardcoded receipt could fake.
- The C3 binding rule does not forbid one case killing two clauses; the landed set is one-to-one
  (`w1/ExecGate/mutants.json`), but the rule permits the weaker case.
- The `guard-battery.py` `ok` is population-relative (`guards > 0`, `rows == bound == guards`); the
  frozen predicate's literal `guards 9` is what pins the population for this claim.
- The six pre-existing eight-cell registry rows of rounds 77–79 (`cells>7`, plus `pinned-empty` on
  `tools/round-78/surface-recheck.py`) are routed, not rewritten; listed in the SCORECARD section.
- `MutInstruments` scored the wave's *candidate* files (hashed at 10:46), not the landed instruments
  written afterwards; its 15 survivors are holes in those candidates' selftests, answered by the
  landed implementations and by `ReviewerC1`/`ReviewerC3`'s independent runs, and are routed here.
- Seat-evidence defect: `w1/ExecProv/selftest.txt` was stale when `SentinelScope` read it (19 cases,
  3 failures at 10:46:24, vs 0 failures for the 10:46:52 instrument); nothing in the landed tree
  depends on it, and the seat's own receipt is the live record.
