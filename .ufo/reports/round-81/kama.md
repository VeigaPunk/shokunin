# kama — round 81

Lane: kama (local model serving / endpoint health). Axes: **operability + calibration** (`shokunin.conf`).
Base revision `e7d2fd729cf8204c89c32534303bc9f2a97fcee4` (round-80 non-author closure tip). Frozen plan
`plans/round-81-claims.md` (freeze commit `2c1faed0354dbb3cb9f869cb1af4a9302dfcfd4e`). Two declared
claims, two distinct axes:

- **C1 — calibration (lowest assigned axis, 7):** the round-80 self-record's six declared facts
  re-derive at the sealed revision `a2af1af59faf6cf66fe854559293c4e4b441aff3` or are answered by dated
  value-bound corrections.
- **C2 — operability (held 8; capability `append-debt`):** the append-only acceptance population is
  graded under a late-acceptance rule, and every pre-round undeclared deletion event is repaid by a
  committed late row.

## Work performed

- **C1 counter built and run.** `tools/round81-selfrecord-round80.py` derives six facts from committed
  blobs (`git show`), grades one `corrected F<n> old=… new=… at=… date=…` block per stale fact in
  `corpus/lessons/round-81.md` §Corrections, and requires the appended `#### round-81 correction` record
  block to name each superseded value. All six facts are stale at the base: F1/F2/F3/F4 are the
  pre-hardening selftest tallies (`pass=9`, `pass=6`) against their own receipts (`pass=11`, `pass=12`);
  F5 is the coverage row's round-79 last-change cell against its round-80 evidence; F6 is the head
  calibration row's round-79 closure pointer against the round-80 closure at the tip.
  Evidence: `SCORECARD.md` §Round 81 C1 row; `.ufo/waves/round-81/measured/before/c1-enum.out`,
  `measured/after/c1-green.out`, `measured/after/c1-selftest.out`, `measured/control/c1-no-corrections.out`.
- **Record repaired value-bound (append-only, no filed byte rewritten).** `SCORECARD.md` gains the
  appended `#### round-81 correction` block naming C1-selftest 9→11, C3-selftest 6→12, calibration-row
  9→11, coverage last-change 79→80 and the newest closure 79→80; `LOG.md` gains the appended
  `LOG-CORRECTION round=80 selftest tallies pass=9/pass=6 -> pass=11/pass=12` entry. The head
  calibration and coverage rows and the head banner are re-anchored in place (round-81 pending edits).
  This disposes routed defect **R80V1** and **R80V6**.
- **C2 counter and register built.** `tools/round81-append-debt.py` grades the frozen audit's acceptance
  population under the late-acceptance rule (a row introduced by a later round binds by strict commit
  ancestry, `N > M` round order, exact hash/count/class and base population; the graded round's own
  events are `pending`, visible and unaccepted). `registry/append-only-late.tsv` carries 88 rows over
  the ten round-79/80 events, generated deterministically by `tools/round81-late-rows.py` whose
  `--check` re-derives every cell. Evidence: `.ufo/waves/round-81/measured/before/debt-base.out`,
  `measured/after/debt-green.out`, `measured/after/debt-selftest.out`, `measured/after/late-check.out`.
- **The frozen rule's unsatisfiability is proved, not asserted.** The wave's cutoff probe appended a
  syntactically perfect row for `4af44f78303f…` to a fixture clone's frozen register and the frozen
  counter answered `APPEND_ACCEPTED_FINDING post-introduction … commit is not an ancestor of the
  register's introduction commit`; the disclosure ledger has the same cutoff. Receipt:
  `.ufo/waves/round-81/w1/EX02CutoffProbe/receipts/03-accepted-after-row.out` (exit 1) and
  `intro-and-descendants.txt`.
- **Gate arm 8 re-pointed; arm 11 added.** `tools/pre-report-gate.py` composes
  `round81-append-debt.py --repo <repo> --round <N>` as arm 8's third member (replacing the frozen
  `round75-append-accepted.py`) and gains arm 11 `round81-instruments` running the new module's own
  selftest. `--selftest` grows from 25 to 26 cases (a new red/absent case pair for arms 8+11), and the
  gate's arms now print `arms=11`. The frozen counter, its predicate and its red round-80 receipt stay
  byte-intact as history. The vacuous-green control is executed: the new counter at the base revision
  with no late register prints `unaccepted=10`, exit 1 (`w1/EX03GateArmProbe/EX03-06-…`), so the
  re-point alone cannot buy green.
- **Pre-report gate green.** `python3 tools/pre-report-gate.py --repo . --round 81 --tip master` prints
  `PRE_REPORT round=81 arms=11 failed=0 uncommitted=0`, exit 0 at `e20d89c7`
  (`measured/after/gate.out`, whose header names that revision): all eleven arms green, arm 8's composed
  line carries `APPEND_DEBT … unaccepted=0 bad_rows=0 bad_declarations=0 out_of_population=0`, arm 11
  `APPEND_DEBT_SELFTEST pass=22 fail=0`, and the gate's own selftest `PRE_REPORT_SELFTEST pass=26 fail=0`
  (`measured/after/gate-selftest.out`).
- **Independent wave verification.** A seat re-derived the debt inventory from the audit JSON without
  reading the new tools: 88 rows, 0 duplicate keys, 0 cell mismatches, 0 note-grammar violations, the
  register's introducing commit a strict descendant of all ten event commits
  (`w1/SC01DebtInventory/LATE_DIFF.json`); another seat fetched every SOURCES URL and located each quote
  (`w1/SC05Fetch/evidence/`). The gate-arm control seat proved the green is carried by the 88 committed
  rows and not by the re-point — same module blob, late register absent → `late=0 unaccepted=10` exit 1,
  present → `late=10 unaccepted=0` exit 0 — and that arm 11's fixture-pure selftest cannot launder it
  (`w1/EX03GateArmProbe/EX03GateArmProbe.md`). A fourth seat showed the frozen counter is now red at the
  tip too (`unaccepted=11`, the round's own first event), so the re-point was structurally necessary
  (`w1/EX03GateArmProbe/EX03-12-round75-tip-4f4bf2d2.txt`). The connector seat found **no sibling lane
  cites S557** and no sibling holds an acceptance instrument (kama owns the rule), and confirmed
  `souji`'s by-content binding of `tools/append-only-audit.py` (`sha256 2b9285bf…f38ff4ee`, `def
  numstat` line 465) still holds because that file was not edited (`w1/CN01SiblingScan.md`). The
  knowledge seat caught S560's scope overreach, which `S562` now supersedes
  (`w1/SC04Knowledge.md` finding 3). The C1 critic seat re-derived the whole round-80 record and found a
  **seventh** stale declared fact the six graded facts do not cover — the head operability row's
  round-79 cell stated `PRE_REPORT round=79 arms=10 failed=0` while the receipt it names prints
  `failed=1` — repaired in the appended correction block and a `LOG-CORRECTION round=81` entry, with no
  claim change (the counter's six facts, predicate and target are frozen; the seventh is recorded as an
  ungraded stale location, `w1/CR01C1Critic/CR01.md` §3–4).
- **Mutation battery (L1-run, because the dedicated mutation-tester seat did not spawn).** Six named
  mutants of `tools/round81-append-debt.py`, each a single semantic change, run against the module's own
  selftest: **four escaped** the 16-arm selftest — a frozen-register row with the wrong mechanical class,
  a frozen row naming an out-of-population event, the population split's pending class, and the base
  cross-check. Each escape became an arm (`frozen-wrong-class`, `frozen-out-of-population`,
  `split-pending`, `resolve-base-*`), the selftest grew **16 → 22 arms**, and the battery's remaining two
  mutants are equivalent (`count=0` is unreachable under the `[1-9][0-9]*` regex; a frozen-row
  `covered.add` reorder moves no graded bucket) while a `graded_keys=set(events)` mutant is
  self-defeating (it makes the counter stricter, never greener). Receipts: the mutated runs are not
  committed as files (they are throwaway copies under the scratch root, deleted on exit); the outcome is
  recorded in `corpus/lessons/round-81.md` §Hardening notes and in the module's new selftest arms.
- **Frontier step (not a claim).** Registry 297 → 302 rows: `S558` supersedes `S557` with the corrected
  Ollama URL (routed defect **R80V2**, whose dead URL returns 404 over 14 bytes); `S559` `git-merge-base`
  grounds C2's ancestry rule; `S560` `git-diff-tree` grounds `-z`; `S562` supersedes `S560`'s scope
  (the audit reads `--numstat -z --no-renames`, not `--name-status`) after the wave's knowledge seat
  proved the overreach; `S561` files the vLLM v0.33.0 quickstart rejection with its flip. One admitted knowledge entry
  (`corpus/knowledge/late-acceptance-rule.md`, source S559/S560) with its coverage-map row;
  `corpus/QUALITY.md` KQ133 from the mined `number-drift` mistake; the S557 Gate erratum closes **R80V3**;
  **R80V4**'s warning inventory is stated; **R80V5** is recorded (the round-80 receipt names its
  measurement revision, not the tip).
- **Assimilation (§10):** none. `merge/kama/` (shokuknow `corpus-expansion-1`) was not adopted this
  round. `considerthese/2026-10-26.md` proposal 1 ("flag deletions in append-only files the morning
  after they happen") is taken up by C2 — the new counter grades every undeclared deletion the audit
  reports and its `pending` line names the round's own edits; proposal 4 (daily pin gap) stays pending
  (no `pin-watch` run this round).
- **Misroot sweep.** `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows no untracked file
  naming kama or round 81 (the one stale `after` file predates this round and names no lane); nothing to
  re-root.

## Landed changes

| Change | LOG entry (§Round 81) | Commit |
|---|---|---|
| Frozen plan with two claims, predicates and controls | pre-round freeze | `2c1faed0` |
| `registry/append-only-late.tsv` (88 rows), `tools/round81-late-rows.py`, `tools/round81-append-debt.py` | C2 | `f6cb5303` |
| `tools/round81-selfrecord-round80.py`, the six corrections, `S558`–`S561`, `late-acceptance-rule.md`, KQ133, README row, head rows | C1 + frontier | `7eeae5bc` |
| `tools/pre-report-gate.py` arm 8 re-point + arm 11, measured receipts | C2 | `88b35ea5` |
| Head self-description: banner, `### Planned (round 82)`, capability `append-debt` in the round-81 canon, closure pointer, coverage cell | C1 (record) | `cf28c470`, `436ea857` |
| `PROVINCE.md` round-81 instrument note | C2 | `4f4bf2d2` |
| Coverage row re-anchored to the round-81 PROVINCE digest | C1 (record) | `1b96317f` |
| Rows moved inside the registry + assimilation section + the placement mistake | frontier | `37484391` |
| `S562` supersedes `S560`'s record-shape scope; knowledge entry, lesson erratum and Frontier line follow | C2 (frontier) | `50c711ec` |
| Cited `pending` value corrected in the banner and LOG with its receipt revision | C2 (record) | `93cdfd60` |
| Gate predicate sentence polished; gate selftest receipt (`pass=26 fail=0`) | C2 | `38d39b1e` |
| Seventh stale declared fact repaired (head operability row's round-79 gate verdict) after the C1 critic seat | C1 (record) | `f6174815`, `7c197ef7` |
| Debt counter hardened 16 → 22 selftest arms after the L1 mutation battery; receipts refreshed | C2 | `017c34ca` |
| Wave-1 results and all seat evidence (11 produced, 3 dead) | C1/C2/frontier verification | `e20d89c7` |
| Final pre-report gate receipt (`arms=11 failed=0 uncommitted=0`) bound to `e20d89c7` | C2 | `1b64f66d` |

## Before → after measurements

| Claim | Counting command | Before (revision) | After (revision) |
|---|---|---|---|
| C1 | `python3 tools/round81-selfrecord-round80.py --repo .` | exit 1 `SELFRECORD_R80_ENUM claims=6 stale=6 corrected=0` (`--enumerate`, freeze tip `2c1faed0`) | exit 0 `SELFRECORD_R80 claims=6 mismatches=0 corrected=6 unbacked=0` (`measured/after/c1-green.out`) |
| C2 | `python3 tools/round81-append-debt.py --repo . --round 81` | exit 1 `APPEND_DEBT round=81 base=e7d2fd729cf8 events=63 accepted=53 late=0 pending=0 unaccepted=10 bad_rows=0 bad_declarations=0 out_of_population=0` (freeze tip `2c1faed0`, no late register) | exit 0 `APPEND_DEBT round=81 base=e7d2fd729cf8 events=63 accepted=53 late=10 pending=<p> unaccepted=0 bad_rows=0 bad_declarations=0 out_of_population=0` (`measured/after/debt-green.out`; `p` is the round's own post-base events — 4 at the recorded receipt revision, rising with each later record commit; the graded buckets are the claim) |

Controls (committed, each red for the named reason): C1 `--no-corrections` prints `mismatches=6` exit 1
(`measured/control/c1-no-corrections.out`); the counter selftest's outside-container, wrong-`at`,
wrong-`new`, wrong-`old`, missing, duplicate and missing-marker cases are all red
(`SELFRECORD_R80_SELFTEST pass=13 fail=0`). C2's selftest kills same-round, same-commit,
non-descendant, short-count, wrong-class, note-without-round, out-of-population and duplicate cases
(`APPEND_DEBT_SELFTEST pass=16 fail=0`); the base run with no late register is the red-before state.

## Sources & frontier

Census command (frozen manual census, run from the lane root):

```sh
grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md
awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ {t=$5; gsub(/[[:space:]]/,"",t); n[t]++} END{for(k in n) printf "%s=%d ", k, n[k]; print ""}' corpus/SOURCES.md
awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ {s=$9; gsub(/[[:space:]]/,"",s); n[s]++} END{for(k in n) printf "%s=%d ", k, n[k]; print ""}' corpus/SOURCES.md
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kama
```

- **Rows 297 → 302** (base blob `e7d2fd72` 297, A 282 / B 11 / C 4, mined 267 / queued 8 / rejected 22;
  tip 302, A 287 / B 11 / C 4, mined 271 / queued 8 / rejected 23); malformed rows 0; the maintained
  validator exits 0 (`corpus/SOURCES.md`, receipt `measured/after/census-validate.out`; the `W04`
  duplicate-URL set is the pre-existing inventory plus round 80's `S555`, and the four new rows add no
  warning category).
- **Rows added by tier:** 4 tier-A `mined` (`S558`, `S559`, `S560`, `S562`), 1 tier-A `rejected`
  (`S561`).
- **Rows touched old→new:** `S558` is a new row whose `teaches` opens `supersedes S557 —` and `S562`
  one whose `teaches` opens `supersedes S560 —` (S557's and S560's bytes are untouched, contract v1
  rule 2: a correction is a new row, never an in-place rewrite); `S559`/`S560`/`S562` enter `mined` with
  `used-by corpus/knowledge/late-acceptance-rule.md`; `S561` enters `rejected` with reason and flip,
  `used-by —`. No existing row changed status or recheck.
- **Frontier rows advanced:** one admitted knowledge entry (`late-acceptance-rule`) on ground the
  coverage map did not hold (append-only acceptance policy), citing the two rows opened this round; one
  coverage-map row; KQ133; the Gate records 3 admits + 1 reject with URL, access date and a ≤25-word
  located quote each, plus the S557 Gate erratum and the S560 scope erratum.
- **Assimilation:** `considerthese/2026-10-26.md` proposal 1 taken up (recorded in
  `corpus/lessons/round-81.md` §Assimilation); proposal 4 remains pending.

## Trend verdicts

| Trend | Verdict | Evidence |
|---|---|---|
| expansion | **improved** | one admitted knowledge entry on uncovered coverage-map ground (`late-acceptance-rule`, source S559/S560 both opened this round); registry +4 rows with 3 admits and 1 reject; the capability `append-debt` enters the round-81 canonical table with a demonstrated run |
| quality | **improved** | six stale self-record facts repaired value-bound without rewriting filed bytes; the frozen acceptance counter's structural unsatisfiability is proved executably and its arm replaced by a rule the lane can satisfy; `LATE_ROWS check=ok rows=88`; KQ133 |
| discernment | **improved, bound** | two mistakes mined with capturing rules (the record's stale tallies → KQ133; SOURCES rows outside the registry → the census `E12` rule), and the Gate's 3 admits + 1 reject each carry their own fetch receipt; bound: the non-author admit/reject spot-check of this round's gate is the closure's, not this report's |

## SHONEN

`[~]` SKILL.md decision tables / error patterns / checklists with cited sources — author assertion, `SKILL.md` §§Decision table, Error signatures, Checklist; no named non-author verifier.
`[~]` At least one end-to-end domain task executed and logged — `LOG.md` §Round 81 C2 runs the acceptance counter end to end against the frozen audit (`measured/after/debt-green.out`, exit 0); the live-serving tasks remain the round 16/61 receipts; no non-author mark.
`[~]` Instructions executable by an agent without oral context — `corpus/knowledge/late-acceptance-rule.md` §The late-acceptance rule gives the rule, the check and its limits; `plans/round-81-claims.md` is a runnable plan; independent execution review remains open.
`[~]` No cross-domain bleed (`PROVINCE.md` accurate) — `PROVINCE.md` §Round-81 instrument note names the new instruments; sibling-owned repair/routing/credentials remain out of province; no non-author mark.

## Round shape, seats and dead seats

- **Shape:** one v1 wave under `ufo-wave-policy.json` (band 8–16), `maxLanes` 16, **14 seats**, no residual
  call.
- **Role mix:** 3 executor, 3 scribe, 2 scout, 1 connector, 2 reviewer, 2 critic, 1 mutation-tester;
  attack seats 5/14 = 36 % (≥25 %), connector seats 1 (≤2).
- **Seats:** 14 dispatched in one v1 wave; **11 produced output and artifacts**, **3 died without
  output** — `RV02C2Attack` (reviewer), `CR02C2Critic` (critic) and `MT01Mutants` (mutation-tester) —
  each with an empty final output, no note and no seat directory (never spawned or returned nothing;
  `.ufo/waves/round-81/w1-results.json` records `output` empty for all three). No error text exists to
  quote; they stay dead in the evidence.
- **Attack coverage, honestly:** the declared attack seats were 5/14 (36 %); **2 produced**
  (`RV01C1Attack` — 9/9 attacks caught, `w1/RV01C1Attack/RV01C1Attack.md`; `CR01C1Critic` — the
  seventh-fact sweep, `w1/CR01C1Critic/CR01.md`). C2's dedicated reviewer/critic/mutation-tester seats
  did not spawn, so C2's falsification came from the non-attack seats that attacked it
  (`EX02CutoffProbe`'s executable proof, `EX03GateArmProbe`'s vacuous-green control,
  `SC01DebtInventory`'s independent 88/88 inventory) plus the L1 mutation battery above and the
  module's 22-arm selftest — recorded as this round's weakest leg.
- **Round total:** 14 seats (11 producing + 3 dead).

## Extras

- **Stale-lane:** mission launched 2026-11-04 08:35 -03 and is **progressing** (commits by this lane,
  latest `1b64f66d`); it is inside the two-driver-tick window at this writing.
- **Tool installs/upgrades:** none this round (no package installed, no tool upgraded).
- **L0 questions:** none opened by this round; no open question blocks it.
- **Measured commit for the report's claim lines:** `1b64f66ddea89c57b71165eacd14b0e1d6f24e11` (lane
  tip after the gate-receipt commit; branch `master`, remote-verified — `git ls-remote origin
  refs/heads/master` prints it).
