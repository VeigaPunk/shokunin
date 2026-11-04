# mori — round 80 report (L1 MoriR80, attempt 1)

Lane repo `mori-shokunin` @ `44bc941a0e3e9676fa33a882b43d6e9793cbf74d` (branch `master`, pushed:
`git -C /home/vgpnk/Projects/shokunin/mori-shokunin ls-remote origin refs/heads/master` prints that
hash). Entering `d58889220d3c6a18d461f2d31b5ab162ffef1e4e`. Fleet report commit: this file.

**Declared claims (frozen in `57451ecb` before any data — contract
`.ufo/waves/round-80/contract.md`, three counters each selftested at the frozen bytes,
do-nothing controls in `.ufo/waves/round-80/evidence/controls-r80.txt`):**

- **C1 — calibration (5, the lowest non-retired axis), capability acquisition:** the
  self-assessment claim sweep `tools/mori-claim-sweep.py` lands and resolves the lane's own
  axes/capabilities/checklist claims against committed bytes, taking the mismatch count from the
  r79 closure's D79-1 stale tally to zero. Target `C1=met`.
- **C2 — operability (7), sourced by S595:** `.ufo/waves/round-79/count-c2.py` gains one selftest
  arm per surviving mutant the r79 mutation seat named, so the frozen six-mutant harness reads
  `survivors=0`. Target `MUTATION_C2 survivors=0 killed=6 total=6`.
- **C3 — coverage (6):** `PROVINCE.md` names every committed `tools/*.py|*.sh` instrument with
  class, registry row and purpose, taking named instruments from 14 of 55 to every committed
  instrument. Target `C3=met missing=0 extra=0`.

Three axes, three frozen predicates, causally separable (each counter grades only its own
artifacts; the C1 counter needs the sweep blob and the corrected row, the C2 harness needs only
the counter's selftest, the C3 counter needs only PROVINCE's tokens). No axis score moves —
no closure states a new number and this round claims none; the verdicts are the trends below.

## Work performed

- **Protocol load and freeze.** Read the round prompt, `skill://shokunin`, `MISSION.md`,
  `AXES.md`, `CORPUS.md` (SOURCES contract v1), the lane SKILL/PROVINCE/SCORECARD/SHONEN,
  `corpus/README.md` Frontier, `corpus/QUALITY.md`, the r79 verifier spotcheck in full and the
  r79 lesson, the run-15 addendum and `scripts/hyaku/ufo-wave-policy.json`. The r79 spotcheck's
  routed defects are this round's spine: D79-1 → C1, D79-2 → C2, D79-3 re-verified rather than
  "fixed" (below), D79-4 recorded as QUALITY 166, D79-5 left conditional (the registered guard's
  selftest is not touched; mori | round-65 stays open).
- **Freeze (commit `57451ecb`).** `.ufo/waves/round-80/contract.md` with P-C1/P-C2/P-C3 stated as
  the same sentence that the counters implement and the receipts print; three counters
  (`count-c1.py`, `mutate-c2.py`, `count-c3.py`) with selftests; the do-nothing controls receipt.
  Corrected before the wave: the contract's first C2/C3 before-values were the r79 seat's prose
  (3 of 6; 15 of 55); the measured entering values are `survivors=2` and `named=14 present=55
  missing=41`. The predicate is unaffected and the report states both readings.
- **Before-states (controls, `evidence/controls-r80.txt`).** Sweep blob absent at entering
  (`git cat-file -e d5888922:tools/mori-claim-sweep.py` rc 128, `C1=unmet tool=absent` rc 1);
  `MUTATION_C2 survivors=2 killed=4 total=6`; `C3=unmet named=14 present=55 missing=41`.
  The receipt obeys the r79 guard it will be cited beside (`unbound=0`).
- **C1 build.** `tools/mori-claim-sweep.py` — a read-only gate over SCORECARD's `## Axes` table,
  every capabilities-table data row and SHONEN's checklist: lane-pointer resolution
  (`corpus/`, `tools/`, `.ufo/` tokens; `:line`, `:line-line` and `@rev` suffixes stripped; a
  `*`/`?` token resolved by globbing at least one existing path; fenced blocks ignored), pinned
  live-selftest tallies, and named stale literals. 30 selftest arms. Its first real run found
  the arm over-broad on three wildcard citation tokens (see the lesson's second mistake) — fixed
  with two arms and re-measured. Registered at SKILL's gate registry (row 14) and in the
  SCORECARD capabilities table (first-working round 80), and it dogfoods the r79 guard on this
  round's own receipts.
- **D79-1 correction.** `SCORECARD.md`'s control-receipt capabilities row corrected 18 → 19 (the
  landed arm count), its Evidence cell's `18/18` annotated as the r79 wave freeze superseded by
  the landed `19/19`, and a `## Round-80 correction (D79-1, calibration)` paragraph appended;
  `grep -c 'selftest 18 in-memory cases' SCORECARD.md` → 0.
- **D79-3 re-verified, not changed.** The r79 spotcheck asked the adjacency Evidence cell to
  point at "the committed MANIFEST row pointer it already names". It resolves:
  `git -C /home/vgpnk/Projects/shokunin cat-file -e 63729047:MANIFEST.json` rc 0 and
  `rounds[398]` is `mori 19 adjacency improved admitted`. The cell's premise (a citation of a
  non-existent `corpus/lessons/round-19-verifier-spotcheck.md`) does not hold at the graded bytes
  — the cell discloses the absence instead. No pointer was rewritten.
- **C2 build.** Three arms added inside `count-c2.py`'s `selfcheck()` only: a non-admitted round
  below the ceiling must not win; a verdict word after the first `;` must not count; a later
  `round N` must not win. `git diff -U0` shows every hunk inside the selftest region; predicate,
  CLI and output grammar byte-identical. The harness also refuses to grade unless the unmutated
  selftest is green (the critic's clause, adopted).
- **C3 build.** An append-only `## Instrument inventory (round 80)` section at `PROVINCE.md` EOF:
  56 rows (every committed `tools/*.py|*.sh`, including this round's new instrument), each with
  class, registry row and a one-line purpose grounded in the file or its registry row. The
  counter grades names-and-paths only; class/registry/purpose cells are the scribe's reading, not
  a counter verdict (named limit).
- **Frontier step.** S595 opened (`https://arxiv.org/abs/2102.11378v2`, "Practical Mutation
  Testing at Scale"), pinned, quoted and cited by `corpus/knowledge/mutation-adequacy-r80.md`
  (K1–K4 + Limits/Boundaries), which grounds C2's criterion. QUALITY 165 (survivor-as-lead),
  166 (the D79-4 limit beside the guard) and 167 (`considerthese/2026-10-26.md` suggestion 1: a
  tally is stale only when the instrument ran) landed.
- **Independent attacks (wave).** The critic (C01) found the C2 vacuous-kill hole and the C3
  overreach risk — both adopted or bounded as described; the mutation tester (M01) killed 5/6 on
  the sweep at the tested bytes and 1/3 on the C3 counter, with three survivors routed to r81;
  the paired-tree reviewer (R02) falsified the round's first sweep bytes (the wildcard arm) and
  confirmed the unresolved arm distinguishes a planted dead pointer; the connector (Cn01) found
  no duplicate ground and named the closest sibling instruments; the scout (Sc01) independently
  enumerated the pointer population (194 pointers, 191 resolving, the same 3 wildcard tokens).
- **The gate bit its own author.** The sweep grades `LOG.md` as a carrier; the Round 80 LOG
  section first quoted the retired 18-arm literal verbatim, so `count-c1` read `stale=1` at
  `2a826f17`. The sentence was reworded at `97ce0c96` (the four carriers now read `stale=0`), and
  the incident is recorded in the lesson rather than hidden — a stale literal in a carrier is the
  class, whoever wrote it. Named limit: the stale arm grades the four carriers only; the lesson
  legitimately reproduces the literal as evidence.
- **No-harm receipts.** The standing 13-instrument battery is 13/13 rc 0 at the landed bytes
  (`evidence/battery-r80.txt`); the source census is rc 0 before (367 rows) and after (368 rows);
  no registered tally-pinned instrument byte changed except the r79 wave-dir counter whose
  selftest region this round extends.

## Landed changes

| Change | LOG entry | Commit |
|---|---|---|
| Contract, three frozen counters, do-nothing controls | `LOG.md` Round 80 (freeze paragraph) | `57451ecb` |
| `tools/mori-claim-sweep.py` (30 arms) + `claim-pins.json` + SKILL row 14 + SCORECARD capabilities row + the D79-1 correction | `LOG.md` Round 80 C1 | `8108dfcc` |
| `count-c2.py` three selftest arms (selfcheck region only) | `LOG.md` Round 80 C2 | `8108dfcc` |
| `PROVINCE.md` instrument inventory (56 rows) incl. the sweep row | `LOG.md` Round 80 C3 | `8108dfcc` |
| S595 row (`SOURCES.md:376`) + pin `corpus/evidence/sources-r80/` + entry + README index row | `LOG.md` Round 80 frontier step | `8108dfcc` |
| QUALITY 165/166 (scribe) and 167 (considerthese suggestion 1) | `LOG.md` Round 80 frontier step | `8108dfcc`, `2a826f17` |
| Round lesson (`corpus/lessons/round-80.md`: Gate, two mistakes, census) + after/battery receipts | `LOG.md` Round 80 | `2a826f17`, `97ce0c96` |

## Before → after measurements

Counting commands are paste-ready; every after-value was re-measured at the final tip
`97ce0c96c779278baa8e8bb45ade642f9fabf1e2`. The build revision is `8108dfcc`; the tip
carries the lesson, the LOG section and the receipts, plus one precision fix to the LOG
prose (below).

**C1 — calibration.**

```
$ python3 -I .ufo/waves/round-80/count-c1.py d58889220d3c6a18d461f2d31b5ab162ffef1e4e
C1=unmet tool=absent sweep=- mismatches=- row_tally=- live_tally=- rev=d58889220d3c      (rc 1)
$ python3 -I .ufo/waves/round-80/count-c1.py 97ce0c96c779278baa8e8bb45ade642f9fabf1e2
C1=met tool=present sweep=0 mismatches=0 unresolved=0 tallies=0 stale=0 row_tally=19 live_tally=19 rev=97ce0c96c779   (rc 0)
```

**C2 — operability (sourced S595).**

```
$ python3 -I .ufo/waves/round-80/mutate-c2.py --rev d58889220d3c6a18d461f2d31b5ab162ffef1e4e
MUTATION_C2 survivors=2 killed=4 total=6 rev=d58889220d3c                                  (rc 1)
$ python3 -I .ufo/waves/round-80/mutate-c2.py --rev 97ce0c96c779278baa8e8bb45ade642f9fabf1e2
unmutated survived rc=0 C2_COUNTER_SELFTEST pass=7 fail=0
MUTATION_C2 survivors=0 killed=6 total=6 unmutated=green rev=97ce0c96c779                  (rc 0)
```

**C3 — coverage.**

```
$ python3 -I .ufo/waves/round-80/count-c3.py d58889220d3c6a18d461f2d31b5ab162ffef1e4e
C3=unmet named=14 present=55 missing=41 extra=0 rev=d58889220d3c                           (rc 1)
$ python3 -I .ufo/waves/round-80/count-c3.py 97ce0c96c779278baa8e8bb45ade642f9fabf1e2
C3=met named=56 present=56 missing=0 extra=0 rev=97ce0c96c779                              (rc 0)
```

The C3 population grows by one because the round lands an instrument; the predicate (no
missing, no extra) is unchanged. `named=14` at entering includes 14 lane tools (a sibling lane's
`tools/...` path named in PROVINCE is excluded by the counter and by an arm).

## Sources & frontier

- Census command, run from the lane root:
  `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin mori`
  — **before** rc 0 (`mori ok`, 35 tolerated W04 duplicate-URL warnings); **after** rc 0, same
  warning class, no `E` findings. Rows
  (`grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`): **367 → 368**;
  malformed (`NF!=13`): 0 → 0.
- **Rows added by tier:** 1 new row — S595, tier **A** (original paper, scope narrowed to what
  the abstract states). Malformed 0; the id is the next unused after S594.
- **Rows touched old→new:** none. S595 is new; no `status`/`recheck`/`used-by` cell of an existing
  row changed this round (S01 verified the pre-fetch duplicate sweep against the entering
  registry: 0 hits for the URL, for `2102.11378`, and for `mutation test`).
- **Frontier rows advanced:** no FR row is closed. FR3/FR11/FR12/FR15 are untouched; the round's
  coverage move is PROVINCE's own surface, which closes the r30-named gap for *tools* (56 named,
  previously 14) and leaves the six fixture directories unnamed (named limit, not claimed).
- **Assimilation: none.** `/home/vgpnk/Projects/shokuknow/merge/` does not exist on this host
  (`ls` fails); the r61 L0 on the staged package's 94/136 id collisions also stands, so no
  package row was adopted. `considerthese/2026-10-26.md` re-mined: its suggestion 1 lands as
  QUALITY 167; the rest stay behind the round-62/65/73 L0s.

## Adversarial findings and their disposition

The reviewer seat (Mo80R01Counter) attacked the counters and the tools they grade; its report is
`.ufo/waves/round-80/w1/Mo80R01Counter.md`. Dispositions:

- **HIGH-1 (fixed, verified)** — the sweep's stale arm was tripped by this round's own LOG
  append at `2a826f17` (`stale=1`); the sentence was reworded at `108ec314` and the tip
  re-measured `mismatches=0`. The same class was then found in two counter docstrings that still
  restated the pre-fix entering values (`survivors=3`, `named=15/missing=40`) — a "corrected fact
  left standing in a sibling carrier" inside this round's own bytes. Fixed at `97ce0c96`.
- **HIGH-2 (named limit, not fixed)** — P-C1's second conjunct (red at `d5888922`) is graded by
  running the same counter at the entering revision; the tip run does not re-derive it. The
  receipt for that conjunct is `evidence/controls-r80.txt` (`C1=unmet tool=absent` rc 1). The
  same holds for C2 (harness at `d5888922`: `survivors=2`) and C3 (`named=14 present=55
  missing=41` rc 1).
- **MEDIUM-3 (disclosed)** — all three counters were amended after the freeze and before the
  after-grading, in response to the critic's clauses and the mutation seat's survivors: C1 gained
  the "all four summary fields are zero" condition and the inconsistent-summary arm; C2 gained
  the "unmutated selftest must be green" refusal; C3 gained the sibling-lane exclusion and one
  arm. None of the three *targets* moved; the C3 exclusion narrowed the population definition
  before the after-value existed, and both readings fail the entering predicate (0 vs 1 extra),
  so no claim's truth changed. The freeze commit remains the predicate contract; this paragraph
  is the correction of record.
- **MEDIUM-4/5 (fixed)** — the two docstring restatements; see HIGH-1.
- **MEDIUM-6/7/8, LOW-9/10/11/12 (routed to r81, not fixed)** — the C3 token's missing left
  boundary (`<dir>/tools/<name>` counts as naming), C1 trusting the summary against its own
  MISMATCH lines and repeated summaries, C1's row-tally first-match reading, the sweep's refusal
  of `--scratch` (the contract's clause is about child work dirs, which the sweep does not
  create), the counter's shell-string export, C3's sibling exclusion also dropping the lane's own
  prefixed path, and a `tools/<name>.py` directory counting as `extra`. None changes a graded
  value at the tip (all three counters read met and their fixtures pass), and none is silently
  kept: each names its fixture in the reviewer's report.

## Trend verdicts

- **expansion: improved** — one new admitted knowledge entry (`mutation-adequacy-r80.md`) on
  ground the coverage map did not hold (test-adequacy as a measurable criterion), citing a
  `mined` S595 opened, pinned and quoted this round; rows 367 → 368 with malformed 0 and census
  rc 0. No package adoption was possible.
- **quality: improved** — a new 30-arm gate whose own survivors were found and repaired in-round;
  the r79 D79-1 class turned into a repeatable check; the r79 counter's two surviving mutants
  killed; the standing battery 13/13 rc 0; both receipt families conform to the r79 guard
  (`unbound=0`). Counterweights, named: the C1 sweep's class/registry claims are unverified by
  its own counter, and three mutants survive on the new tools (routed to r81).
- **discernment: improved** — two mistakes mined with class/evidence/captured-by/fix, the second
  one (an over-broad arm) found by the round's own first run rather than by a seat; three routed
  defects accepted as r81 work instead of being widened into this round's predicate; D79-3
  re-verified and reported as a closure premise that does not hold rather than "fixed".

## SHONEN

`SHONEN.md` has four boxes; one line each (`[~]` = author-asserted with a resolvable pointer; no
named non-author verifier has signed any box this round):

- [~] SKILL.md holds real decision tables, error patterns and cited sources — the round adds
  gate-registry row 14 (the claim sweep) with its eight fields and a Round79/Round80 registry
  home; rule text in `corpus/QUALITY.md` 165–167; sources cited by `S595` and the entry.
- [~] At least one end-to-end domain task executed and logged — the three claims are logged in
  `LOG.md` Round 80 with their measured commits (`57451ecb`, `8108dfcc`, `2a826f17`, `97ce0c96`).
- [~] Instructions executable by an agent without oral context — the frozen contract plus three
  selftesting counters and `evidence/after-r80.txt` make the round re-derivable with no session
  context; each counter's `--selftest` runs from the lane root.
- [~] No cross-domain bleed — detection and report only: the new sweep reads four files and
  prints; it writes nothing, opens no socket, and spawns only the pinned tools' read-only
  `--selftest` children; PROVINCE gains an inventory of the lane's own instruments, not of any
  other lane; the arXiv material is corpus ground, not OS state.

## Round shape and mechanics

- **One v1 wave, 14 seats** under `scripts/hyaku/ufo-wave-policy.json` (band 8–16), validated by
  `ufo-swarm-wave.mjs run` (`w1-spec.json` → `w1-dispatch.json`, `counts.total=14`), dispatched
  through the inline handoff (`w1.ready` written at 03:07, `w1.ready.dispatched` present).
- Role mix: 4 executor, 3 scribe, 2 scout, 1 connector, 2 reviewer, 1 critic, 1 mutation-tester →
  **attack share 4/14 = 28.6 %** (≥25 %), connectors 1 (≤2). The planner seat is held by the L1
  (the validator rejects `planner`); a bounded planning data-walk rode the scout `Mo80Sc01Recon`.
  Residual call: none. **Round total 14 seats.**
- Seat reports: 14 of 14 at `.ufo/waves/round-80/w1/<name>.md`; `w1-results.json` carries 14
  settled rows (one per seat, each with a non-empty output) and the orchestrator's WAVE-DONE
  arrived at 03:2x. **Dead seats: none.** Seat count and roles come from `w1-results.json`, not
  from this prose.
- Route table: no `model` parameter was passed anywhere; the host's `task.agentModelOverrides`
  decided the routes. One seat's role had to be changed at validation time (`labrat` is not a
  swarm role), which is why the probe item rides a reviewer.
- Tooling: **no tool was installed or upgraded** this round; no `pacman` transaction was run (the
  host-wide pause stands).
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows only the
  orchestrator's `.scratch/` entries and a 24-byte `after` file dated 2026-11-03 20:05 (not this
  lane's; left untouched). No seat wrote outside the lane.

## Open L0 questions / carried disclosures

- The three open mori L0 lines (round-62 wave-surface waiver, round-65 instrument-change ruling,
  round-73 label-sweep instrument) were re-verified present and unanswered and routed around; no
  new L0 line was filed.
- Carried defects, named for r81 (not silently kept): three surviving mutants — the sweep's
  `mismatches`-counts-only-`unresolved` shape (repaired in-round at the L1's direction, so the
  remaining survivors are the C3 counter's `drop_sibling` and `count_directories`, both now
  covered by a new arm and re-measured only for the sibling case), and the two instruments whose
  selftests print `pass=0 fail=0` at rc 0 with `TMPDIR` unset (`mori-disk-rate.py`,
  `mori-round41-calibration.py`) — recorded as QUALITY 167 and left byte-untouched behind the
  round-65 L0.
- Inherited, not mine: the fleet root's `after` file and `.scratch/` state; the three r76 foreign
  receipt files stay disk-only under the standing leave-for-operator ruling.
- Stale-lane: this lane has no other mission open; the respawn-per-round driver picks the next
  round after this closure.
