# kengaku — round 43 report (hyaku run 9, 2026-10-26)

Lane `/home/vgpnk/Projects/shokunin/kengaku-shokunin`, branch `master`. Baseline as read `317148c4b918fb2645e46ec0225cac720a8a57e9`;
frozen claims `plans/round-43-claims.md` (freeze `02753f260805e2e45b05af22145da00f91671364`); first recorded probe run
`6b49694d2ff533135fc238a8400f3e0dc1c82026`; landing `77ea425ac217ebe2290490b2ebb3d0a60202ca9b`; final lane hash
`1838be94b355e40139d4231f743bc6946f77c1f6` (`git ls-remote origin refs/heads/master` → that hash). L1 agent id `KengakuR43`; the
L1 holds the canonical planner seat (the validator rejects `planner`; the round-44 data walk rode scout `R43PlanNext`).
Earlier attempts: none (`.ufo/watchdog.log` has no `lane-dead-no-report kengaku round=43` line; `.ufo/waves/round-43/` absent at start).

## Work performed

Declared claims (2), frozen with red controls before any `plans/battery43` fixture and before the first recorded probe run:

- **C1 — calibration (8):** the nine behaviours `plans/anchor_digest_check.py` and `plans/order_check.py` (both unedited)
  advertise that battery42 leaves undemonstrated — the round-42 wave-2 near-variants NA1 NA5 NA7 NA18 NA20 NA21 NO5 NO7
  NO22 (`F42XMutNear` §3–§4; 8 `direct`, 1 `indirect`). Counter `plans/round43_c1_verify.py` = round-42 counter + the
  `F42C1Hardened` repairs R1–R4 + three new legs: **g value attribution** (a kill needs the site record after the replaced
  span to differ from the reference's, reference traced twice), **h** symlink-escape refusal, **i** order argv blobs.
  `TOTAL = 9`, `FLOORS = {anchor: 6, order: 3}`.
- **C2 — coverage (lowest non-retired axis, 7, tied with novelty; frozen tie-break; capped by L0 `kengaku | round-33`):** the
  pinned Terminal-Bench 2.0 `feal-differential-cryptanalysis` grader admitted as
  `corpus/knowledge/tb2-feal-differential-cryptanalysis-grader.md` with a 12-case bubblewrap probe (`plans/feal_probe.py`),
  rows S129–S134 (tier A) + S136/S137 (tier B, executed Gate flips); counter `plans/round43_c2_verify.py` = round-42 V1–V9
  re-pointed + **V10 mechanism** (round-42 closure R5).

Work items:

- Protocol load: round prompt, `skill://godspeed`, SCORECARD `### Planned (round 43)`, round-42 report and spot-check
  (`corpus/lessons/round-42-verifier-spotcheck.md` §5 R1–R6), `F42CritPlanNext` D1–D5, `F42XMutNear`, `F42C1Hardened`,
  `considerthese/2026-10-26.md`.
- TB2 task files fetched by the L1 at pin `2fd12b88` 2026-10-26 18:40 -03 (twelve captures + `SHA256SUMS`,
  `corpus/evidence/round43/tb2-feal-differential-cryptanalysis/`).
- Freeze `02753f26`: claims, both counters, probe, spec `plans/pkg-spec-r43.json`, dry table (`cases=12 predicted_pass=8
  predicted_fail=4`), witness module, round-43 envelope (PATH-dir content digest, closure R6), controls
  (`.ufo/waves/round-43/claims/`): witness run 9/9 killed `value=differs`; C1 nothing `killed=0 survived=9` exit 1;
  witness-as-battery `PREDICATE C1 pass`; no-mutants fail; span-forced `unattributed=9`; value-forced `unattributed=9`;
  tool-edited `PINS mismatched=1`; relative-argv escape `SETUP … breaks the contract`; NA7 mislabel `SURVIVED
  exhibits=0>1,rc-mirror`; hostile h1–h6 each open under the round-42 counter and closed under round 43
  (`control-c1-hostile-h1…h6.txt`); C2 nothing `checks=10 defects=7`; informed filler `V10 DEFECT`, content `V10 ok`
  (`CONTROL-C2-INFORMED-FILLER red-as-required`); stage-check `cases=12 failed=0`; census-before exit 0.
- First recorded probe run `6b49694d`: `cases=12 observed_pass=8 observed_fail=4 mismatches=0`, `regrade cases=12 differ=0`;
  `order_check` → `ORDER RESULT PASS`.
- Wave 1 (spec/dispatch `d33350fd`, 38 seats, `.ufo/waves/round-43/build-results.json`): seven executors wrote
  `plans/battery43/` (42 fixtures; each mutant killed by ≥4 fixtures); C2 package from `R43PkgEntry`/`R43PkgRows`/
  `R43PkgProse`; prior art `R43ScoutPriorArt` (3 published as unmeasured statements, 3 adjacent); independent checks: real
  pytest under `uvx -p 3.13` 12/12 (`R43PytestParity`), re-derivation 12/12 + 3 (`R43CritIndep`), dishonest-battery
  vectors 9 blocked (`R43CritC1Counter`), value leg spurious 0 / vacuous 0 of 9 (`R43CritValueLeg`), verdict stable over 18
  runs (`R43RevSiteStable`), mutant rows 9/9 verbatim (`R43RevMutRows`). Limits found: V10's DECISIVE is readable in the
  counter, a copycat filler passes (`R43CritClaims` §1); R4/leg-i fence gaps (`R43SentinelCounter` F1–F3, `R43CritC1Counter`
  V2′; no battery43 fixture uses them); counter guards caught 8/15 (`R43MutC1Counter`), V9/V10 6/13 (`R43MutC2Counter`);
  envelope misses mode-only changes (`R43ReviewEnvelope` 3/4).
- Routed R1–R6 landed `77ea425a`: fibsqrt entry errata E1–E7 (`R43ErrataFibsqrt`); S128 Gate row + Dockerfile flip executed
  as S135 (`R43GateRowsR2`); `plans/gate_flip_check.py` + Q35 (`R43FlipCheck`, selftest 19/19); 44 routed-ledger rows
  (`R43RoutedQueue`, `R43R42Defects`), 13 closed by clean-clone observe at docs `8adf76cc`; round-42 wave-2 doc defects
  corrected by appends (20 of 22, 3 refuted); generator route-mix asserts (the attack assert fired once, 9/37).
- Landing measurement `integrate/measure-final.txt` (clean clone of `77ea425a`): C1 pass, C2 pass; final-tip re-measure
  `integrate/measure-tip.txt` (`2a3e29c6`): C1 pass, C2 pass, flip check `unresolved=0`, census ok.
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain --untracked-files=all` lists, beside orchestrator
  `.scratch/`/`.ufo/state/`, only `.ufo/waves/round-51/w1/Mo51*.md` (another lane's seats; not touched) — no kengaku
  round-43 seat file in the fleet root (misroot 0; `R43ScoutMisroot`: host writes 0, sentinel present).
- Scratch `/fast/scratch/hyaku/kengaku-r43` removed by the L1 after landing.

Round shape: **one v1 wave of 38 seats** — 11 executor, 7 scribe, 5 critic, 5 scout, 4 connector, 3 reviewer,
2 mutation-tester, 1 sentinel; m_flash roles 24/38, attack 10/38; 38 results, 37 reports on disk (`R43ConnClaims` returned
its output only in `build-results.json`, no report file); 0 dead. **Wave 2 (33 seats, validated, `falsify-dispatch.json`)
was not dispatched** — the run's request budget ended; round total **38 < 64**: conformance defect (lesson §Mistakes added
by the L1 at close). No residual call. Routing from the host table (run-8 map); no `model` passed. Report filed after
WAVE-DONE build (the only wave launched).

Stale-lane: respawn-per-round driver, no other mission of this lane open.

Tool installs: none by the L1. pacman not touched.

## Landed changes

| commit | what | LOG.md |
|---|---|---|
| `02753f26` | freeze: claims, C1/C2 counters, feal probe, spec, dry table, captures, controls, witness, envelope | round 43 entry ¶1 |
| `6b49694d` | first recorded probe receipt | C2 bullet |
| `d33350fd` | wave-1 spec and dispatch | ¶1 |
| `77ea425a` | battery43, feal package (entry, S129–S137, README/PROVINCE/SKILL), routed R1–R6, round-42 corrections, lesson | C1, C2, Routed bullets |
| `8adf76cc` | SCORECARD/LOG round-43 sections, routed closures, landing measurement, census | entry |
| `ac339b25` | wave-1 reports, registry rows `round43-c1-mutants`/`round43-c2`/`feal-probe`, wave-2 spec (not dispatched) | — |
| `2a3e29c6` | wave-1 results, entry/PROVINCE errata (L1 self-review) | — |
| `1838be94` | close-out: tip re-measure, lesson/SCORECARD close notes | — |

## Before → after measurements

- **C1 (calibration)** — `python3 plans/round43_c1_verify.py --lane .` on a clean clone.
  - Before (`claims/control-c1-nothing.txt`; `integrate/measure-baseline.txt` at `d33350fd`): `BATTERY fixtures=0`, `MUTANTS
    total=9 killed=0 survived=9 invalid=0 null_detected=0 unattributed=0`, `PREDICATE C1 fail`, exit 1.
  - After, at `77ea425a` (`measure-final.txt`) and `2a3e29c6` (`measure-tip.txt`): `BATTERY fixtures=42 wrong=0 tampered=0
    sidechannel=0`, `MUTANTS total=9 killed=9 survived=0 invalid=0 null_detected=0 unattributed=0`, `MUTANTS-BY-TOOL
    anchor=6/6 order=3/3`, `PREDICATE C1 pass`, exit 0.
  - Verdict: **frozen predicate met.** Score **8 → 8 held**. The counter cannot see intent (witness-as-battery passes);
    battery honesty rests on wave-1 attacks only (no wave 2).
- **C2 (coverage)** — `python3 plans/round43_c2_verify.py --lane .` on a clean clone.
  - Before (`claims/control-c2-nothing.txt`): `checks=10 defects=7`, exit 1; at `d33350fd` `defects=6`.
  - After, at `77ea425a` and `2a3e29c6`: `checks=10 defects=0`, `PREDICATE C2 pass`, exit 0; probe re-run byte-equal
    (`feal_probe exit=0 byte_equal=yes`).
  - Verdict: **frozen predicate met.** Score **7 → 7 held** (L0 cap). V10 is a fidelity gate against the counter's DECISIVE
    map, not proof of reading the captures (`R43CritClaims` §1).
- **No harm** (`measure-baseline.txt` vs `measure-final.txt`): only the round-43 counters (red → green), package-gate legs,
  index/knowledge counts 49 → 50, anchor check `rows=121 tokens=27` → `rows=130 tokens=36` (`defects=0`), `routed_open=10` →
  `52` (39 after closures) differ; rounds 36–42 counters, ledger-tip, tip receipts, four probes byte-equal, census exit 0,
  frozen digests r39–r43 OK; `order_check` r38 and round-38 C1 red as before.

## Sources & frontier

- Counting command: `grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` → 121 → 130. Tier A +6 (S129
  `tests/test_outputs.py`, S130 `instruction.md`, S131 `tests/feal_module.c`, S132 `tests/feal.c`, S133 `tests/test.sh`, S134
  `README.md`, feal-differential-cryptanalysis @ `2fd12b88`, opened by the L1 18:40 -03, re-fetched cmp-identical 19:07 -03);
  tier B +3 (S135 circuit-fibsqrt `environment/Dockerfile` — round-42 flip executed; S136 feal `environment/Dockerfile`, S137
  `environment/feal.py` — this round's flips fired at landing, re-opened by the L1 19:18 -03). All `mined`. Rows touched
  old→new: none (no cell edited).
- Census `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kengaku`: before
  exit 0, `kengaku ok`, 15 W04 (`claims/census-before.txt`); after exit 0, `kengaku ok`, 15 W04 (`integrate/census-final.txt`).
- Frontier advanced: README §Frontier TB2 clause narrowed for a ninth task (9 of 89); one graded-state class new to the
  executed sample (an agent-authored Python module imported into the grader's interpreter beside the answer-holding
  reference module). Knowledge files 49 → 50.
- Sourced claim: C2 (S129–S134 opened this round).
- Mined mistake (`corpus/lessons/round-43.md` §Mistakes): conditional Gate refusals whose flips fire unexecuted (round-42
  D3; 45 obligations in 18 lessons, none resolved) → `plans/gate_flip_check.py` red on round-42 lesson, green after the
  appended `Flip check` lines, Q35. Further: a stale-line anchored edit pre-freeze; a broken freeze control; V10's readable
  key; counter fence gaps; the 38-seat close; two wrong entry sentences + one PROVINCE miscount (appended errata).
- Assimilation: none — `merge/kengaku/` unchanged since 2026-10-24 (`R43MergeRescreen`: 0–3-space id-collision check
  `reg-ids=121 staged-ids=175 collisions=45`, guard proven on an indented `  | S002 |` fixture, quarantine slice S091/S105
  refused; renumber map: none). considerthese: `2026-10-26.md` proposal 3 → static TB2 class histogram 89/89, 11 classes
  (`R43ConsiderThese`), recorded in the lesson as the round-44 coverage selector.

## Trend verdicts

- **expansion — improved.** One admitted entry on Frontier ground (ninth TB2 grader; first whose graded artefact is a Python
  module imported into the grader's interpreter) citing six tier-A and two tier-B rows; three capability rows demonstrated
  (`value-attributed-mutant-kills`, `in-process-import-grader-probe`, `gate-flip-check`).
- **quality — unprovable-but-better.** Two gate tools carry nine more attributed kills under a stricter (value) rule and
  hardened sandbox; the round-42 routed queue is durable and partly closed by checks; round-42 errata landed in-round.
  Against that: no falsify wave ran, V10's key is readable, and three wrong sentences were caught only by the L1's re-read.
- **discernment — unprovable-but-better; the non-author closure decides.** The round-42 outside disagreement (D3) became a
  tool + criterion and two fired flips this round were executed (S136/S137); prior art kept honest (no novelty claimed).

## Open L0 questions

No new line filed. Still open: `kengaku | round-25` and `kengaku | round-33` (coverage cap). Routed around: coverage held at 7.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md` §In-process module-import TB2 grader — round 43 (decision table citing receipt cases) and registry rows `round43-c1-mutants`, `round43-c2`, `feal-probe`, `gate-flip-check`
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md` round 43 entry; `corpus/evidence/round43/feal-probe.txt` (12 cases; byte-equal re-run in `integrate/measure-final.txt`; pytest parity 12/12 `R43PytestParity`)
- [~] Instructions executable by an agent without oral context — `.ufo/waves/round-43/integrate/measure.sh` re-runs both claim counters and the no-harm set from a clean clone (`integrate/measure-final.txt`)
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` §Round43 partial frontier admission and its routing clause (cryptanalysis technique / Python import-system semantics unowned; `R43ConnSibling`)
