# mado — round 79 report (hyaku run 15, attempt 1)

Lane: mado-shokunin · round 79 · base `e4b153dfa4a67ca56f7ec65cb6639082451626a7` · freeze
`5eb8f20fe291603c74973fa94cc55723ac8089a4` · repair tips `d6be05ef` (R1), `cf5f09b9` (R2) and `999a4a3f` (R3) ·
measured `999a4a3f` (both claims; the C1 counter's own bytes last changed at `52178de1`) · landing
tip `2b3c9c6b` · report filed after WAVE-DONE (`w1-results.json`, 14/14 seats).

## Work performed

**Declared claims (2, frozen before data; `.ufo/waves/round-79/claims-declaration-r79.md`):**

1. **C1 — coverage.** The static `monitor = NAME, addreserved, TOP, BOTTOM, LEFT, RIGHT` reserve
   composes with the bar's own band: the monitor's usable box starts after the static reserve
   (`CReservedArea::apply`), the bar is arranged inside it, and
   `expected = static[edge] + extent + opposite margin` (`CReservedArea::calculate` sums the static
   initial box with the layer delta). The rule walk follows `handleMonitor`; twenty-three frozen
   cases (the eighteen round-78 cases carried unchanged plus five), twelve named mutants, the held
   round-78 tool as the do-nothing control.
2. **C2 — operability.** The read-only runbook executes per-row bindings: twenty-two cases on
   twenty-two distinct `SKILL.md` rows whose command cell equals the case's command, four
   documented model refusals (a `mode` preset, a scaled monitor, the `background` layer, a spaced
   output pattern) over committed fixtures, and the `omarchy menu keybindings --print` row bound by
   shape; nine matcher mutants, the held r78 fixed-value rule as the control on the five new rows.

- **C1 instrument and evidence.** `tools/mado-barfoot.py` `r79-v1` adds `--rules` (the Hyprland
  config carrying the joined monitor's rules), the static-reserve walk, the usable-box arrangement
  and the composed expectation; it refuses a `source =` line, a `$`-bearing rule, a non-integer
  `addreserved` field and a static reserve that leaves no usable box. `quality/counters/c1-r79-reserve.py`
  extracts the tool at `--rev` and `--base-rev`, asserts the eighteen carried cases, scores the
  twenty-three cases, kills twelve single-anchor mutants and scores the base tool:
  `receipts/measurement-final-r79.txt` (repaired bytes at `999a4a3f`: `correct=23 killed=12
  base_correct=18/23 carried=18/18 tool_selftest=50/50 TARGET_MET`, tool sha256 `9e274157…`),
  `receipts/measurement-c1-r79.txt` (the frozen run at `5eb8f20f`, same counts on the pre-repair
  bytes, tool sha256 `c9aa1391…`), `receipts/control-c1-r79-at-base.txt` (`correct=18 killed=4
  base_correct=18/23 TARGET_MISSED`).
- **Repair R1 (wave-found, post-freeze).** The wave's entry scribe re-derived the rule walk and
  found that an `addreserved` line with **no same-selector rule ahead of it** drops its area
  (`ConfigManager.cpp:1331` writes into an existing rule; `:1341` falls through to
  `add(parser.rule())`, and the parser holds only the selector, `Parser.cpp:92-101`). The frozen
  model credited the area and four fixtures presupposed the prior rule. Repaired: the tool now
  leaves a zero reserve on the fall-through (selftest 43 → 44 assertions) and the four fixtures
  carry the positional rule their expectation presupposes; no expectation, label, mutant or target
  moved. Red/green: `receipts/repair-r79-c1-fallthrough.txt` (frozen tool `expected=52 DIFFER`
  where the repaired tool reads `expected=26 CLEAN` on a rules file whose only line is
  `addreserved`), and `receipts/repair-r79-c1-oldfixtures.txt` (the pre-repair fixtures score
  `correct=20/23` against the repaired tool — the fixture change is load-bearing). Named limit: the
  fall-through is asserted in the tool selftest only; no frozen case covers it.
- **C2 instrument and evidence.** `quality/counters/c2-r79-runbook.py` parses the new SKILL.md
  section (escaped-pipe cells), binds each case to exactly one row, refuses a shared binding, binds
  the working tree to `--rev` by sha256 (SKILL.md, tool, every fixture), executes each row verbatim
  from the lane root, and scores live output plus committed churn/negative samples:
  `receipts/measurement-final-r79.txt` (`cases=22 executed=22 matched=22 shapes=17/17 anchors=22/22
  rows=22/22 control_new=0/5 mutants=9 killed=9 TARGET_MET, tree=bound`, `control_all=15/22` as
  an observation), `receipts/control-c2-heled-instrument-at-base.txt` (the held r78 instrument exits 2
  on the successor set) and `receipts/control-c2-r79-at-base.txt` (rc 2: the working tree is not
  the base revision's bytes — the declared before state).
- **Knowledge and frontier.** `corpus/knowledge/bar-footprint-reserve-r79.md` supersedes the r78
  static-`addreserved` limit; registry rows **S465** (`src/output/Monitor.cpp`, `setStatic` +
  `logicalBoxMinusReserved`) and **S466** (`ReservedArea.cpp`, `calculate`'s static-plus-dynamic
  sum) admitted, **S467** (the Hyprland wiki Monitors page) rejected — it documents the line syntax
  only, not the summation, and the live URL 404s; `used-by` gains the new entry on S303, S457, S458
  and S459. Index row and frontier bullet in `corpus/README.md`; the round-78 frontier bullet's
  re-opened-row count is corrected in the new bullet.
- **Host ground (read-only).** `--rules ~/.config/hypr/monitors.conf` joins CLEAN: `STATIC … top=0
  right=0 bottom=0 left=0 source=rules`, box `0,0,3440,26`, `reserved=EQ band=26 expected=26`
  (`receipts/live-join-r79.txt`); `~/.config/hypr/hyprland.conf` is refused (`source =` line 4);
  the whole `~/.config/hypr/**` tree declares no `addreserved` (wave seat R79ScoutHost). No config
  tree, compositor state or service was written.
- **Wave.** One v1 wave, 14 seats (2 scouts, 1 connector, 4 executors, 2 scribes, 2 reviewers,
  1 critic, 1 mutation-tester, 1 sentinel; attack share 5/14), validated by `ufo-swarm-wave.mjs
  plan` (`spawn=14`, band 8-16) and dispatched through the inline handoff (`w1.ready`). Outcomes in
  **Wave disclosures**; evidence under `.ufo/waves/round-79/w1/`.

## Landed changes

| change | LOG entry | commit |
|---|---|---|
| freeze: `--rules` + static-reserve composition, both counters, 23/22-case control sets and generators, refusal fixtures, declaration, control baselines, runbook rows, registry and ledger rows | round-79 | `5eb8f20f` |
| the static-reserve entry, SOURCES (S465/S466/S467), README index + frontier, lesson, QUALITY 136, SCORECARD, LOG, PROVINCE | round-79 | `03e76ee9` |
| record corrections from the wave's source and case re-derivations (S465 anchor precision, the fetch manifest without its self-line, the carried-wording correction, lesson M79-5) | round-79 | `3b8af34c` |
| repair R1: the `addreserved` fall-through drops its area; four fixtures gain the prior positional rule; declaration amendment, entry and lesson M79-6 | round-79 | `d6be05ef` |
| scorecard and log at the R1 measurement | round-79 | `8696c4dd` |
| repair R2: layout origin, negative clamp, `desc:`/empty refusal, band overflow, `transform` slot (wave R79ScoutModel); declaration amendment, entry, lesson M79-7 | round-79 | `cf5f09b9` |
| scorecard, log and declaration at the R2 measurement | round-79 | `c4e71f98` |
| the S303 fetch pin, the C1 counter's `p > 0` selftest floor, the counter-mutation limits and the SCORECARD corrections | round-79 | `52178de1` |
| final measurement, census (start/end) and harm-watch receipts | round-79 | `89924c1e` |
| repair R3: `O_NOFOLLOW` reads, the executed-argv-equals-row assertion, the controls sha line (wave R79Sentinel) | round-79 | `999a4a3f` |
| scorecard, log, declaration and entry at the R3 measurement | round-79 | `c5187d98` |
| wave w1 evidence (spec, validated dispatch, ready handoff, 14 seat results and 13 written reports) and the round's remaining receipts | round-79 | `2b3c9c6b` |

## Before → after measurements

| claim | counting command | before | after (measured commit) |
|---|---|---|---|
| C1 coverage | `python3 -I quality/counters/c1-r79-reserve.py --repo . --rev REV --base-rev e4b153df… --controls .ufo/waves/round-79/controls/c1-cases-r79.json --carried .ufo/waves/round-78/controls/c1-cases-r78.json --scratch-root DIR` | at `e4b153df`: `cases=23 correct=18 mutants=12 killed=4 base_correct=18/23 carried=18/18 tool_selftest=28/28 verdict=TARGET_MISSED` rc 1 (`receipts/control-c1-r79-at-base.txt`) | `cases=23 correct=23 mutants=12 killed=12 base_correct=18/23 carried=18/18 tool_selftest=44/44 verdict=TARGET_MET` rc 0 at `d6be05ef` (`receipts/measurement-final-r79.txt`); the frozen run at `5eb8f20f` printed the same counts on the pre-repair bytes (`receipts/measurement-c1-r79.txt`), reproducible only with the frozen counter bytes (declaration §"How to re-produce") |
| C2 operability | `python3 -I quality/counters/c2-r79-runbook.py --repo . --rev REV --controls .ufo/waves/round-79/controls/c2-runbook-cases-r79.json --carried .ufo/waves/round-78/controls/c2-runbook-cases-r78.json --scratch-root DIR` | at `e4b153df`: rc 2, `SKILL.md in the working tree is not the measured revision's bytes`; the held r78 instrument on the successor set rc 2 (`control set carries 22 cases, frozen target expects 17`) — `receipts/control-c2-r79-at-base.txt`, `control-c2-heled-instrument-at-base.txt` | `cases=22 executed=22 matched=22 shapes=17/17 anchors=22/22 rows=22/22 control_new=0/5 mutants=9 killed=9 verdict=TARGET_MET tree=bound` rc 0 at `999a4a3f`; the counter also prints
`MADO_R79_CONTROLS: sha256=50a18041…` (`receipts/measurement-final-r79.txt`) |
| — | `quality/check-index.py` | 97/97 at base | 98/98 at the records tip |
| — | `bash tools/mado-verify.sh --selftest` | 460/460 | 460/460 (gate bytes unchanged) |
| — | `quality/check-tool-ledger.py` | 142 rows | 144 rows, uncovered 0 |

## Known limits (named, not smoothed)

- The counter cannot detect a tampered artifact set: its internal checks (carried prefix, exact
  `base_correct`, anchor-absent branch, refusal stage, selftest clause) are each load-bearing only
  under tampering, which the frozen bytes make unnecessary; a wave seat demonstrated every one with
  a tamper probe, and the one real defect (`selftest_ok` accepting `0/0`) is repaired with a
  `p > 0` floor.
- No current tool mutant is separated by `band` or `expected` alone — those fields are printed but
  not load-bearing in any verdict today.
- The `addreserved` fall-through (no prior same-selector rule) is asserted in the tool selftest,
  not in a frozen case; a mutant crediting it would survive the case set.
- The carried `exclusive-false` case leaves `expected` unpinned (its expectation predates the ask;
  adding the key would break the parsed-equality carry).
- The runbook's 14 `hyprctl` rows depend on `HYPRLAND_INSTANCE_SIGNATURE` that the counter injects
  and the table does not show (wave seat R79ScoutHost measured 8/22 passing without it); the
  `omarchy-theme` row is an exact string and fails on a theme switch; `monitors-reserved` is
  `int4` and cannot see the reserved-band drift C1 models.
- The four `refuse-*` rows certify refusal plumbing over committed fixtures, not scenario
  modelling.
- The C1 join still does not model a second layer-surface consumer, scaled/transformed outputs,
  `desc:` selectors (refused wholesale), or sourced config files (refused).
- **The predicate certifies behaviour on the frozen set, not the absence of a lookup.** The wave
  critic built a tool that fingerprints the case fixtures (route B,
  `w1/R79CritClaims/cheat-b-fingerprint-alias.py`) and scored `correct=23 killed=12 TARGET_MET`
  without implementing the composition; the honest counterexample is on record. The mitigation
  for round 80 is a generated shadow set (permuted static values, expectations re-derived inside
  the counter) — adding it now would change the frozen predicate after data.
- C1's "green tool selftest" clause is self-reported: a fabricated `p/n` would satisfy it
  (`p > 0`, `p == n`); the tool is the lane's committed artifact, not an external oracle.
- C2's `matched=22` depends on host posture exactly as `control_all` does (both are live probes);
  `control_all` is an observation while `matched` is a predicate — stated, not hidden. Its
  re-derivation window is time-boxed to a working tree equal to the measured revision
  (`tree=bound`); the counter refuses foreign bytes rather than silently scoring them.
- The counter's internal checks are load-bearing only under tampering (above); the frozen bytes
  are the defense, not the checker.

## Planned (round 80; intent only)

1. C1: a second *layer-surface* consumer with its own level, attributed from the live capture or
   named as unreachable; scaled-output handling if a grounded conversion exists.
2. C2: a chord grammar for the keybindings row instead of an arrow shape; the
   `systemctl --user is-active` row; the env-contract rows made explicit in the table.
3. Widen `quality/check-cited-revisions.py` to the rows a round moves (the r77 planned item; the
   round-79 block is probe-green, the SCORECARD-wide invocation is not its contract).
4. `considerthese/2026-10-28.md` proposal 4 (the live-tool table) stays available.

## Sources & frontier

Counting command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root
/home/vgpnk/Projects/shokunin mado` — exit 0 at round start (401 rows, `census-start-r79.txt`) and
exit 0 at round end (404 rows, `census-end-r79.txt`), both with the standing W04 duplicate-URL
warnings and one W01.

- **Rows added by tier:** +2 A (S465, S466), +1 B (S467, rejected); status histogram mined
  378 → 380, rejected 13 → 14, queued 10 unchanged; tier histogram A 386 → 388, B 7 → 8, C 8.
- **Rows touched old→new:** four `used-by` cells, each appending
  `corpus/knowledge/bar-footprint-reserve-r79.md`: S303 (monitor-rule parser), S457 (renderer
  arrange), S458 (monitors `reserved` print), S459 (parent/child band). S461 stays unchanged (the
  entry does not cite it); S462's raw URL 404'd on re-fetch and its r78 byte-identical pin is
  reused (not load-bearing this round).
- **Frontier rows advanced:** the r78 `NOT_MODELLED` static-`addreserved` limit moves to core; the
  new entry's "what is not claimed" names the remaining frontier (a second layer-surface consumer,
  scaled outputs, `desc:` selectors, sourced config files).
- Admit/reject sample for the non-author spot-check: admit S465 and S466, reject S467.

## Trend verdicts

- **expansion — improved.** One net-new admitted entry (`bar-footprint-reserve-r79.md`) on ground
  the coverage map did not hold (the r78 entry named it `NOT_MODELLED`), citing two rows opened
  this round (S465, S466) plus four re-opened ones; index 97/97 → 98/98.
- **quality — improved.** The weaker r78 limit is superseded by a stronger entry; the wave's
  source re-derivation exposed a model defect that was repaired with a red/green pair
  (`repair-r79-c1-fallthrough.txt`, `repair-r79-c1-oldfixtures.txt`); QUALITY 136 was added for the
  instrument self-description class; the fetch manifest was repaired; no admitted entry fails its
  re-check.
- **discernment — improved.** Every wave disagreement became a committed repair or a named limit
  (repair R1, the M79-5 manifest, the C2 scope caveats); the Gate's admit/reject sample (S465/S466
  admit, S467 reject) is on record for the closure's outside spot-check. The round does not claim
  the outside verdict itself.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — the
  runbook section (22 executed rows) and the static-reserve decision table are this round's
  additions; no outside-lane verifier has judged them yet (§ `corpus/knowledge/bar-footprint-reserve-r79.md`,
  `SKILL.md:231-264`).
- [~] At least one end-to-end domain task executed and logged in LOG.md — the live read-only join
  with `--rules` (`receipts/live-join-r79.txt`) and the 22-row runbook execution
  (`receipts/measurement-final-r79.txt`); the outside-lane verification is the closure's.
- [~] Instructions executable by an agent without oral context — the runbook was executed from its
  documented cells by two independent seats (R79ScoutHost 22/22, R79ExecC2Runbook 22/22 with an own
  parser); the non-author promotion judgment is not this lane's.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — PROVINCE's round-79 refinement names the
  one new read-only input and adds no write surface; the connector's sibling scan reports in the
  wave disclosures.

## Wave disclosures

One v1 wave, 14 seats, dispatched through `w1.ready`; all 14 settled (`w1-results.json`), 13 with a
written report and one partial seat (disclosed below). No seat is backfilled: a seat that returns
nothing stays an evidence gap.

- **R79ScoutModel (scout, source).** Rebuilt the composition from the pins (static and dynamic
  bands sum; the box is arranged inside `logicalBoxMinusReserved()`), then attacked it and found
  five reachable classes: the monitor's layout origin was ignored; a negative `addreserved` field
  was not clamped; `desc:`/empty selectors were silently skipped although the docstring promises a
  refusal; a band that overflows the usable axis was still expected; and `transform` with no rule
  created a phantom slot. Repair R2 (`receipts/repair-r79-c1-model-r2.txt`, one red/green pair per
  class). Its corroborating fetches (ConfigManager, MonitorRuleManager, Parser, ReservedArea.hpp,
  hyprutils Box) are named in its §7; Parser.cpp is pinned as `S468`/`S469` in the round fetch dir.
- **R79ScoutHost (scout, host).** The live join with `--rules ~/.config/hypr/monitors.conf` reads
  CLEAN (`STATIC … all-zero source=rules`, `band=26 expected=26`); `~/.config/hypr/**` declares no
  `addreserved` and the main config is refused at its `source =` line 4. All 22 runbook rows
  executed twice, byte-identical, max 0.076 s. Env matrix: 14/22 rows fail without
  `HYPRLAND_INSTANCE_SIGNATURE` (the counter injects it), 3 without the omarchy PATH, 1 without
  `OMARCHY_PATH`; change matrix: a workspace switch breaks no row, a waybar restart transiently
  breaks `layers-namespaces`/`waybar-process`, a theme switch breaks the exact `omarchy-theme` row,
  a gaps toggle breaks `gaps-out`.
- **R79ConnSiblings (connector).** No sibling lane claims the reserve/band ground or a C2-shaped
  runbook. Its three record findings are the ones this report carries: the shipped successor
  counter cannot re-print the frozen measurement (the frozen counter bytes can; declaration
  §"How to re-produce"), the C1 tool sha printed by the counter is the *extracted* revision's
  bytes, and the ledger row still said "byte-identically" (fixed).
- **R79ExecC1Cases (executor).** Derived the five new expectations from the sources before running
  the tool: its five derivations agree with the frozen expectations (60/26/52/52/refusal). Its
  adversarial fixtures were run against the frozen bytes; the one at variance (A1a) re-derives the
  R1 class, which repair R1 superseded.
- **R79ExecC2Cases (executor).** Confirmed all four refusal fixtures are genuine `stage=model`
  exit-3 refusals with distinct reasons and none is a setup error dressed as a refusal; all four new
  matcher mutants are killed; `lines-any-line` shares its killer samples with
  `lines-min-lines-dropped` (no sample is unique to it).
- **R79ExecC2Runbook (executor).** Extracted the 22 cells with its own parser, executed every one
  verbatim: 22/22 matched; the binding is 1:1 and the anchor equals the executed command; its
  tamper run proves the tree binding refuses a foreign working tree (a real stale-tree event, rc 2).
- **R79ScribeEntry (scribe).** Its source re-derivation found the `addreserved` fall-through defect
  (repair R1) with the parser source (`Parser.cpp:92-101`, `ConfigManager.cpp:1331/1341`); its draft
  supplied the entry's worked-case structure.
- **R79ScribeSources (scribe).** Verified the two new rows against the registry's 11-column shape,
  the byte-identical quotes and the digests; found the S465 anchor's one-line offset (entry
  corrected), the fetch manifest's self-referential last line (repaired), and the expected duplicate
  URL pattern (S465/S306, S466/S459).
- **R79RevC1 (reviewer).** Reproduced the frozen measurement byte-identically from a clean scratch;
  judged the post-freeze repair necessary, source-grounded and re-measured green, with the freeze
  receipt kept as the before-state record; found the `0/0` selftest hole (repaired with a `p > 0`
  floor).
- **R79RevC2 (reviewer).** Reproduced C2 from a clean scratch; the binding grammar, refusal matcher
  and tree binding fail closed under every attack it tried; caveats recorded above (structural
  rows/anchors, vacuous-by-construction `control_new`, four rows certifying plumbing, host-dependent
  mutant kills).
- **R79MutC1 (mutation-tester).** Mutated the counter's own checks one at a time: each survivor was
  demonstrated load-bearing with a tamper probe (so the checks are unexercised, not absent), except
  the `0/0` selftest hole; found that no current tool mutant is separated by `band`/`expected` alone
  and that four mutants rely on a single separator case (named limits).
- **R79Sentinel (sentinel).** Eight findings; three repaired in R3 (the `--rules` lstat/open race
  via `O_NOFOLLOW`+`fstat`, the missing executed-argv-equals-row assertion, the missing control-set
  sha on the C2 receipt); the rest named (symlinked scratch parent, PATH-resolved `python3` in the
  documented refusal rows, inherited child env, the stale waybar pid inside the carried `frozen`
  value).
- **R79CritClaims (critic).** Built the counterexample that matters: a fixture-fingerprinting tool
  scores `correct=23 killed=12 TARGET_MET` without the composition (`cheat-b-fingerprint-alias.py`);
  judged C1 a PASS with two weak clauses and C2 MIXED (host-dependent `matched`, tree-bound
  re-derivation), and confirmed the two claims do not share an axis.
- **R79ExecC1Tool (executor) — partial seat, disclosed.** It settled without a written report: its
  output is a progress narrative and its battery lives in `w1/R79ExecC1Tool/out.txt` (73 `OK`, 0
  `FAIL`, run against the pre-R2 tool). Its own oracle for the negative-static class was the tool
  formula, and it noted the divergence from the clamped constructor in the case note — the class
  R2 closes. The battery is not backfilled into a report; the seat's missing report is an evidence
  gap, not a pass.

## Stale-lane

Respawn-per-round driver; this lane has no other open mission. Open L0 questions (r57–r60, the L2
floor, the host-recovery pacman pause, the r37/r38 session-material history) stay operator-owned;
no new L0 question this round. No tool installed or upgraded; no pacman transaction.
