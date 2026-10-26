# kengaku — round 42 report (hyaku run 9, 2026-10-26)

Lane `/home/vgpnk/Projects/shokunin/kengaku-shokunin`, branch `master`. Baseline as read `d69452cfa4ea8f95a43caf3727a7c797ba390b6c`;
frozen claims `plans/round-42-claims.md` (freeze `bc856d803576e182b6c3c12afc6b23f392071c25`); first recorded probe run
`523b27806be0df26d2235089d845265a29f8cedf`; landing `ff14d76d32d662f7b7073a2acb049594cb740d84`; final lane hash `f9bbee69b711677487515cf14d5c30f80658427f`
(`git ls-remote origin refs/heads/master` → that hash). L1 agent id `KengakuR42`; the L1 holds the canonical planner seat (the
validator rejects `planner`; the round-43 data walk rode scout `R42PlanNext`, which ended without a report — see below).
Earlier attempts: none (`.ufo/watchdog.log` has no `lane-dead-no-report kengaku round=42` line; `.ufo/waves/round-42/` absent at start).

## Work performed

Declared claims (2), frozen with red controls before any `plans/battery42` fixture and before the first recorded probe run:

- **C1 — calibration (owned, 8):** what `plans/anchor_digest_check.py` and `plans/order_check.py` (both unedited) advertise and
  battery40 leaves undemonstrated — the 14 directional round-40 near-variants (anchor X1 X3 X6 X7 X9 X12 X13 X14 X15; order XO1
  XO3 XO5 XO6 XO7; 13 `direct`, 1 `indirect`); counter `plans/round42_c1_verify.py` = round-41 counter + the five
  `F41C1Hardened` repairs + a new **attribution** leg (a kill counts only if a traced re-run executes the replaced span);
  `TOTAL = 14`, `FLOORS = {anchor: 9, order: 5}`.
- **C2 — coverage (lowest non-retired axis, 7, tied with novelty; frozen tie-break; capped by L0 `kengaku | round-33`):** the
  pinned Terminal-Bench 2.0 `circuit-fibsqrt` grader admitted as `corpus/knowledge/tb2-circuit-fibsqrt-grader.md` with a 16-case
  bubblewrap probe (`plans/fibsqrt_probe.py`), rows S125/S126/S127 (+S128 tier B prior art); counter `plans/round42_c2_verify.py`
  (round-41 V1–V8 re-pointed + **V9 content**, round-41 closure R3).

Work items:

- Protocol load: round prompt, `skill://godspeed`, AXES, SCORECARD `### Planned (round 42) — corrected`, round-41 report and
  spot-check (`corpus/lessons/round-41-verifier-spotcheck.md` §5 R1–R5), `R41PlanNext.md`, `F41C1Hardened.md`,
  `considerthese/2026-10-26.md`, run-9 goal file.
- TB2 task files fetched by the L1 at pin `2fd12b88` 2026-10-26 17:05 -03 (nine captures + `SHA256SUMS`,
  `corpus/evidence/round42/tb2-circuit-fibsqrt/`); raw URLs re-fetched sha-equal 17:08 -03.
- Freeze `bc856d80`: claims, both counters, probe, spec `plans/pkg-spec-r42.json`, dry table (`cases=16 predicted_pass=7
  predicted_fail=9`), captures, freeze modules `claims/witness/w_{anchor,order}.py`, Q32 envelope wrapper, controls
  (`.ufo/waves/round-42/claims/`): witness run 14/14 killed and attributed; C1 do-nothing `killed=0 survived=14` exit 1;
  freeze-modules-as-battery `PREDICATE C1 pass`; emptied list `MUTANTS total=0 … fail`; span-forced attribution
  `unattributed=14 … fail`; tool-edited `PINS mismatched=1`, 9 invalid; relative-argv escape → `SETUP … breaks the contract`
  exit 2; direction-mislabel copy (round-40 labels for XO5/XO6) → `XO5/XO6 SURVIVED exhibits=0>1,rc-mirror`; C2 do-nothing
  `checks=9 defects=6`; C2 filler → `V9 DEFECT`, measured content → `V9 ok`; stage-check `cases=16 failed=0`; census-before exit 0.
- First recorded probe run `523b2780`: `cases=16 observed_pass=7 observed_fail=9 mismatches=0`, `regrade cases=16 differ=0`;
  `order_check` → `ORDER RESULT PASS`.
- Wave 1 (spec/dispatch `fda71ae0`, 39 seats, `.ufo/waves/round-42/build-results.json`): five executors wrote
  `plans/battery42/` (29 fixtures); C2 package from `R42PkgEntry`/`R42PkgRows`/`R42PkgProse`/`R42RegistryRows`, with the
  `R42CritProbe` D1 mechanism correction folded in and a `## Wave-1 integration` section appended to the entry (D2–D5,
  Harbor cwd = `/app` per `R42ScoutHarborCwd`, prior art 2/6 per `R42ScoutPriorArt`). Independent checks: real pytest
  parity 16/16 (`R42CritPytest`), re-derivation 16/16 + 3 (`R42CritIndep`), probe mutants 12/12 (`R42MutProbe`), C2 counter
  mutants 228/237 (`R42MutC2Counter`), no-harm baseline 24/24 green (`R42ExecNoHarm`).
- C1 limits found in wave 1 (frozen counter not edited, routed to round 43): a dishonest battery reached the predicate with
  three substitute fixtures (`R42CritC1Counter` §1); the span check is vacuous for 8/14 (`R42CritAttribution`);
  `R42SentinelCounter` V1 HIGH — `log.showSignature`+`gpg.program` in a fixture `.git/config` runs a program inside the order
  tool's run, falsifying the frozen sentence "these two tools run no fixture code" (no fabricated kill shown; battery42 carries
  no such key); V2/V3 builder copy readable, hidden lane writable; `core.worktree` redirect (V1b); counter guards caught 7/22 by
  committed controls (`R42MutC1Counter`); 12/14 `adv` cells verbatim (`R42RevMutRows`). C2: an informed filler passes 7/9
  (`R42CritClaims`) — V9 is a consistency check, not a content check.
- Landing `ff14d76d`: battery42, entry + S125–S128, README index row / coverage bullet / §Frontier "8 of 89", PROVINCE
  §Round42 (digital-logic and C-simulator semantics unowned), SKILL registry rows + addendum + decision table, QUALITY
  Q33/Q34, routed rider +6 rows, R5 `round_close.py` re-run fix (red→green `integrate/r5-round-close-check.txt`), R2
  `plans/scratch_guard.py` (selftest 36/36). Measured on a clean clone (`integrate/measure-final.txt`): C1 pass, C2 pass.
- Docs `508434ad` (SCORECARD/LOG/lesson); wave-1 evidence + planned round 43 + wave-2 spec `445e81f8`; tip re-measure at
  `508434ad` verdict-equal (`integrate/measure-tip2.txt`); lesson addendum `3e8a2e5e`.
- Wave 2 (falsify; spec/dispatch `445e81f8`, 33 seats, 33 results, `.ufo/waves/round-42/falsify-results.json`; integrated in
  `f9bbee69`): battery42 reviewed honest 29/29, substitutes 0 (`F42RevBat*`); site-value attribution 8/8 for the span-vacuous
  mutants (`F42C1StrongAttrib`); landed battery 14/14 under a hardened copy whose four repairs each bite (`F42C1Hardened`);
  C1 re-run byte-equal, modules load-bearing 5/5; gpg vector real but cannot change any of the 14 verdicts (`F42GpgVector`);
  C2 re-run pass, probe byte-equal 3/3; quotes 24/24; rows 4/4 re-opened, no wrong cell; cwd claim confirmed (9/16 move off
  `/app`); compiler flags do not move the receipt; separability holds; no harm 277/277 verdict lines equal (`F42NoHarm`). Not
  integrated this round, routed with the reports as evidence (SCORECARD `### Wave 2 outcome`): 4 entry sentences, 9 C2-package
  defects, 8 lesson defects, 6 Q33/Q34 defects, 5 rider defects, 2 adv errata, 1 SCORECARD mismatch, 1 drift, 1 wrong
  sentence, 5 plan-43 defects; V9 admits 2/4 attack shapes, V9 mutants caught 7/16. `F42ConnFrontier` returned no verdict line.
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain --untracked-files=all` lists, beside orchestrator
  `.scratch/`/`.ufo/state/`, only this report — no kengaku round-42 seat file in the fleet root (misroot 0; `R42ScoutMisroot`,
  `F42ScoutMisroot`: host writes 0, sentinel present at start and end).
- Scratch `/fast/scratch/hyaku/kengaku-r42` removed by the L1 after landing (`.ROUND-ROOT-SENTINEL` present throughout).

Round shape: two v1 waves. Wave 1: 39 seats — 11 executor, 6 scribe, 6 scout, 5 critic, 4 connector, 3 mutation-tester,
2 sentinel, 2 reviewer; m_flash roles 24/39, attack 10/39; 38 reports, 1 seat ended without a report (`R42PlanNext`, scout:
its final output is mid-reasoning text, "Could mean control executed now is required…"; raw data files only). Wave 2: 33
seats — 10 reviewer, 9 critic, 5 executor, 3 mutation-tester, 3 scout, 3 connector; m_flash roles 14/33, attack 22/33; 33/33
reports (one, `F42ConnFrontier`, without a verdict line); 0 dead. Round total 72 seats, no residual call. Wave 2 dispatched
after WAVE-DONE build; report filed after WAVE-DONE falsify.
Routing from the host table (run-8 map); no `model` passed. **Conformance defect:** wave 2 carries 14/33 m_flash-routed
seats, below the ≥50 %-per-wave rule (lesson §Mistakes added by the L1).

Stale-lane: respawn-per-round driver, no other mission of this lane open.

Tool installs: none by the L1. pacman not touched. Envelope note: the L1's Q32 envelope v1 (home read-only) broke `uv`'s cache
lock for every C2-class counter (`integrate/measure-baseline-v1.txt`); v2 overlays `~/.cache` from scratch.

## Landed changes

| commit | what | LOG.md |
|---|---|---|
| `bc856d80` | freeze: claims, C1/C2 counters, fibsqrt probe, spec, dry table, captures, controls, freeze modules | round 42 entry ¶1 |
| `523b2780` | first recorded probe receipt | C2 bullet |
| `fda71ae0` | wave-1 spec and dispatch | ¶1 |
| `ff14d76d` | battery42, C2 package (entry, S125–S128, README/PROVINCE/SKILL), registry rows, Q33/Q34, routed rows, R5 fix, scratch guard, baselines | C1, C2, Frontier/routed bullets |
| `508434ad` | SCORECARD/LOG round-42 sections, lesson, landing measurement, census | entry |
| `445e81f8` | wave-1 reports/results, planned round 43, wave-2 spec/dispatch | Frontier bullet |
| `3e8a2e5e` | tip re-measure, lesson mistake (wave-2 route mix) | Mistakes bullet |
| `f9bbee69` | wave-2 reports/results, SCORECARD wave-2 outcome, tip re-measure at `3e8a2e5e` | — |

## Before → after measurements

- **C1 (calibration)** — `python3 plans/round42_c1_verify.py --lane .` on a clean clone.
  - Before (`claims/control-c1-nothing.txt`; `integrate/measure-baseline.txt` at `fda71ae0`): `BATTERY fixtures=0`, `MUTANTS
    total=14 killed=0 survived=14 invalid=0 null_detected=0 unattributed=0`, `MUTANTS-BY-TOOL anchor=0/9 order=0/5`, `PREDICATE C1
    fail`, exit 1.
  - After, at `ff14d76d` (`integrate/measure-final.txt`) and `508434ad` (`measure-tip2.txt`): `PINS total=2 mismatched=0`,
    `BATTERY fixtures=29 wrong=0 tampered=0 sidechannel=0`, `MUTANTS total=14 killed=14 survived=0 invalid=0 null_detected=0
    unattributed=0`, `MUTANTS-BY-TOOL anchor=9/9 order=5/5`, `PINS-AFTER mismatched=0`, `PREDICATE C1 pass`, exit 0.
  - Verdict: **frozen predicate met.** Score **8 → 8 held**. The counter is forgeable and its attribution is vacuous for 8/14,
    so admission also rests on wave 2's non-author battery review: honest 29/29, substitutes 0, site-value attribution 8/8,
    hardened-copy 14/14 (`F42RevBat*`, `F42C1StrongAttrib`, `F42C1Hardened`).
- **C2 (coverage)** — `python3 plans/round42_c2_verify.py --lane . --work <dir>` on a clean clone.
  - Before (`claims/control-c2-nothing.txt`): `checks=9 defects=6` (V2 V3 V4 V7 V8 V9), exit 1; at `fda71ae0` `defects=5`.
  - After, at `ff14d76d` and `508434ad`: `checks=9 defects=0`, `PREDICATE C2 pass`, exit 0; probe `cases=16 observed_pass=7
    observed_fail=9 mismatches=0`, re-run byte-equal (`fibsqrt_probe exit=0 byte_equal=yes`).
  - Verdict: **frozen predicate met.** Score **7 → 7 held** (L0 cap). V9 admits an informed filler (7/9 for the full counter,
    `R42CritClaims`; `F42CritV9` 2/4); wave-2 reviewers found quotes 24/24 verbatim and 4 unsupported entry sentences
    (`F42EntryQuotes`), routed to round 43 (not adjudicated by the L1 this round).
- **No harm** (`measure-final.txt` / `measure-tip2.txt` vs `measure-baseline.txt`): only the round-42 counters (red→green), the
  anchor check (`rows=117 tokens=24` → `rows=121 tokens=27`, `defects=0`), routed rider (`routed_open=5` → `10`) and
  registry/knowledge counts differ; rounds 36–41 counters, ledger-tip, tip receipts (`receipts=28 byte_equal=8 differ=0`),
  constraints/db-wal probes byte-equal, census exit 0, frozen digests r39–r42 OK, `order_check` r38 exit 1 (pre-existing),
  r39–r42 exit 0, `round_close.py --round 41/42` exit 0.

## Sources & frontier

- Counting command: `grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` → 117 → 121. Tier A +3 (S125
  `circuit-fibsqrt/tests/test_outputs.py`, S126 `instruction.md`, S127 `tests/sim.c`, terminal-bench-2 @ `2fd12b88`, opened by the
  L1 2026-10-26 17:08 -03), tier B +1 (S128 OpenAgents issue #9645, closed 2026-09-25, located by `R42ScoutPriorArt`, re-opened by
  the L1 17:35 -03); all `mined`, all used by the new entry. Rows touched old→new: none (no in-place edit; Q34).
- Census `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kengaku`: before
  exit 0, `kengaku ok`, 15 W04 (`claims/census-before.txt`); after exit 0, `kengaku ok`, 15 W04 (`integrate/census-final.txt`).
- Frontier advanced: README §Frontier TB2 clause narrowed for an eighth task (8 of 89 read); one executed edge class new to the
  lane (a data artefact executed by a simulator the grader compiles at grading time, scored on a fixed 28-row table).
  Knowledge files 48 → 49.
- Sourced claim: C2 (S125–S128 opened this round).
- Mined mistakes (`corpus/lessons/round-42.md` §Mistakes): XO5/XO6 directions carried mislabelled from the round-40 table (fix:
  re-derivation through the frozen counter, shown able to fail by `control-c1-direction-mislabel.txt`; Q33); a kill credited to a
  lane-clone fixture (`R42CritEquiv` §4); an envelope that changed the instrument's result (v1 receipt); a frozen attack-surface
  sentence falsified by git config (`R42SentinelCounter` V1); an L1 edit slip before freeze; wave 2 under the m_flash floor.
- Assimilation: none — `merge/kengaku/` unchanged since 2026-10-24 (`R42MergeRescreen`: id-collision check with the 0–3-space
  pattern, guard proven on an indented `  | S002 |` fixture, quarantine slice derived; nothing appended, renumber map: none).
  considerthese: `2026-10-26.md` proposal 2 (filler-control half) → V9 + `claims/control-c2-filler.txt`.

## Trend verdicts

- **expansion — improved.** One admitted entry on Frontier ground (an eighth TB2 grader, the first whose graded artefact is a
  data file executed by a simulator the grader compiles) citing four `mined` rows; three capability rows demonstrated
  (`attributed-mutant-kills`, `compiled-simulator-grader-probe`, `scratch-root-guard`). One instance, not breadth.
- **quality — improved.** Two more gate tools carry a standing battery killing 14/14 frozen near-variants with attribution;
  the C2 counter gained a content-consistency check with a red filler control; the entry's mechanism was corrected in-round
  from a falsifier's measurement before landing; residual counter limits routed with named remediations.
- **discernment — unprovable-but-better at most; the non-author closure decides.** Directions re-derived (the round-40
  mislabel caught by control), prior art kept honest (S128 published; no novelty claimed). Against that: a frozen sentence
  about the tools' attack surface was false (V1), the counter is again forgeable, and wave 2 was cut under the route-mix rule.

## Open L0 questions

No new line filed. Still open: `kengaku | round-25` and `kengaku | round-33` (coverage cap). Routed around: coverage held at 7.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md` §Simulator-executed data-artefact TB2 grader — round 42 (decision table citing receipt cases) and three new registry rows (`round42-c1-mutants`, `round42-c2`, `fibsqrt-probe`)
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md` round 42 entry; `corpus/evidence/round42/fibsqrt-probe.txt` (16 cases; byte-equal re-runs in `integrate/measure-final.txt`, `measure-tip2.txt`; pytest parity 16/16 `R42CritPytest`)
- [~] Instructions executable by an agent without oral context — `.ufo/waves/round-42/integrate/measure.sh` re-runs both claim counters and the no-harm set from a clean clone (`integrate/measure-final.txt`)
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` §Round42 partial frontier admission and its routing clause (digital-logic / C-simulator semantics unowned; fleet grep `R42ConnSibling`, `R42PkgProse`)
