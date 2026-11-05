# mori — round 90 (L1 MoriR90; contract attempt 2; integration after WAVE-DONE)

Lane repo `/home/vgpnk/Projects/shokunin/mori-shokunin`, branch `master`. Contract entering revision
`037c02ca43a5ff36e23e449d0d6bcf50a1f2cbec` (`.ufo/waves/round-90/contract.md`). Lane tip at filing:
`e5200affd7eba792e8b4ecf46ca6a3ae4bb07a8e` (pushed; `git ls-remote origin refs/heads/master` prints the
same hash). Every counter number below was re-run by this L1 at the cited revision.

## Work performed

Declared claims (two, frozen in `.ufo/waves/round-90/contract.md` before any after-value; causally
separable — neither counter reads the other's subject):

- **C1 · operability (score 7)** — the round-87 receipt gate refuses the non-executing-branch class
  (`branch_open` 8 → 0 on the frozen class) with `harm=0` and `newopen=0` on the 78-case population and on
  the round-90 18-case held-out battery.
- **C2 · calibration (score 5, tied lowest with depth and freshness)** — the three round-89 neighbouring
  survivors are armed (B1 `own_ok_arm_count` in `count-c1.py`; B4 `met_line_call_site` and B6
  `clone_root_negative` in `count-c2.py`) and every declared mutant is killed with an attributed,
  isolated FAIL set (`killed 12 → 15`, `isolated=0 unattributed=0 unanchored=0`).

No score move is claimed on either axis. Work items with evidence pointers:

- **C1 rule, landed.** `.ufo/waves/round-87/count-c2.py` `invocations_visited` (AND-OR short circuit from a
  literal status, sequencing after literal `exit`/`return`, unselected `if` bodies, subshell status, `!`,
  non-iterating loops, statements after `break`/`continue`, unmatched literal `case` arms, glued control
  tokens `);`, `)||`, `)&`). Landed at `11197820`, sha256 `3fc9cc44…`. Seat `Mo90E01Gate` (candidate
  history: `ab0c9104…`, `79350315…`, landed `3fc9cc44…`; the seat's report names which sha each table graded).
- **Held-out battery.** `.ufo/waves/round-90/battery/branch-heldout.json` — 18 cases, 14 branch rejects and
  4 provenance `met` cases (seat `Mo90E04Battery`, `.ufo/waves/round-90/w1/Mo90E04Battery.md`).
- **C2 arms.** `.ufo/waves/round-88/count-c1.py` 28 → 29 arms; `.ufo/waves/round-88/count-c2.py` 26 → 27 arms
  (`Mo90E02ArmB1`, `Mo90E03ArmsB46`). The count-c2 landing merges two mutation-free constant pins
  (`arms_pinned`, `marker_literal`) into one `frozen_constants` arm that keeps both assertions; the frozen
  `arms=29,27` is unreachable by two separate arms, so this merge is the disclosed reason (see Landed
  changes and Limits).
- **Glued-paren harm, found and fixed before landing.** Reviewer `Mo90R01C1` measured five valid, executing
  commands the candidate `79350315…` refused (`(exit 0); python3 -I …`, `(exit 1)|| python3 -I …`,
  `(exit 0)& python3 -I …`, `(printf ok; exit 0); python3 -I …`, `(exit 0);  python3 -I …`), all bound by
  the committed gate. This L1 re-ran them on the gate bytes that landed (`3fc9cc44…`, from
  `git show HEAD:.ufo/waves/round-87/count-c2.py`) against the entering gate (`30a29797`):
  every glued form binds on both (`entering=bound landed=bound`), and `(exit 1) && python3 -I …` is
  refused on the landed gate and bound on entering — a non-executing branch, i.e. a gain. No harm remains
  on these bytes; the frozen counter reads `harm=0`.
- **C2 attack, reviewer `Mo90R02C2` (`.ufo/waves/round-90/w1/Mo90R02C2.md`).** Finding F1 **HIGH, OPEN**: a
  subject that is green pristine, trips on any edit, and maps each declared anchor-edit to exactly its own
  label reads `killed` on all four count-c1 mutants. The frozen clause `failset(out) == {arm}` does not
  distinguish that canary from a real arm, and the landing does not close it. F2 **MEDIUM, OPEN**: the B4
  pin sees one spelling of the call only (`print(met_line(rev))`); equivalent call sites are outside P-C2.
- **C1 attack, critic `Mo90C01Critic` (`.ufo/waves/round-90/w1/Mo90C01Critic.md` §1–§4).** A 21-string
  lookup table (fixture only, not landed) reaches the frozen C1 line: the held-out battery is not held out
  from the author, so `branch_open=0` grades verdicts, not rule shape. Battery `class`/`expect`/`reach` are
  the file's own words (§4c). Also measured: the arms merge above (`arms=27` forces removing one
  existing pin's separate arm); `harm` does not count battery branch cases.
- **Scope and boundary, sentinel `Mo90Se01Boundary` (`.ufo/waves/round-90/w1/Mo90Se01Boundary.md` §1–§5).**
  Finding (§1, **FAIL**): the C1 selftest ignores `--scratch` — `count-c1.py:223` is
  `tempfile.mkdtemp(dir=os.environ.get("HYAKU_SCRATCH") or tempfile.gettempdir())`, and it never removes
  its two synthetic-gate directories; this round's control run left six directories under `/tmp`. The C1
  run path and C2 were clean under `strace` (no lane writes, no sibling or fleet-root writes, no
  credential-shaped material). §4: the battery file is data-only (no execution) but its class labels are
  self-declared. §5: the `BATTERY` line prints six fields (`cases branch_cases branch_open harm newopen
  paths`) where the frozen sentence names four; the `C1=` and `C2=` lines match byte-for-byte.
- **Mutation probe, `Mo90M01Mut` (`.ufo/waves/round-90/w1/Mo90M01Mut.md`).** On the landed rule `3fc9cc44`:
  17 of 24 single-point mutants killed. Survivors: N10 (`elif` conjunct), N15 (unmatched `case` arm), N17
  (literal-word guard), N20 (nesting-level check in `binds`), N21 (`same_path` accepts a parent prefix),
  N23/N24 (the `control_atoms` split of a glued `)` token) — each with a concrete kill case in the seat
  report. The harm axis is pinned only by inversion (N22 is the only mutant that raises `harm`).
- **Scope scout, `Mo90Sc01Scope`** classified the provenance class (`.ufo/waves/round-90/w1/Mo90Sc01Scope.md`).
- **Connector, `Mo90K01Conn`** mapped the cross-round pins the landing moves (`.ufo/waves/round-90/w1/Mo90K01Conn.md`).
- **Frontier step.** Five sources admitted this round (S612–S616, see Sources & frontier); the lesson
  `corpus/lessons/round-90.md` carries `## Gate`, `## Mistakes` (four rows) and `## Limits of this round`;
  `corpus/knowledge/branch-reachability-r90.md`; QUALITY 190–192; `SCORECARD.md` `## Round 90`;
  `LOG.md` `## Round 90`.

## Landed changes

| Commit | What | Where recorded |
|---|---|---|
| `11197820` (round-90.1) | `.ufo/waves/round-87/count-c2.py` reachability pre-pass (26 selftest arms unchanged); `.ufo/waves/round-88/count-c1.py` (29 arms); `.ufo/waves/round-88/count-c2.py` (27 arms, `frozen_constants` merge); `.ufo/waves/round-90/battery/branch-heldout.json`; the round-90 wave tree (spec, dispatch, ready markers, candidates, seat reports, registry) | `LOG.md` `## Round 90`; `SCORECARD.md` `## Round 90` |
| `9441ef30` (round-90.2) | `.ufo/waves/round-90/evidence/after-r90.txt`; `corpus/SOURCES.md` S612–S616; `corpus/knowledge/branch-reachability-r90.md`; `corpus/lessons/round-90.md`; `corpus/QUALITY.md` 190–192; `SCORECARD.md`; `LOG.md` | `LOG.md` `## Round 90`; `SCORECARD.md` `## Round 90` |
| `0a1f019b` (round-90.3) | `SKILL.md` round-90 registry pointer (supersedes the r89 receipt pointer); append-only corrections of record for r89 spot-check items D1/D2/D3/D5/D6/D7 | `LOG.md` `## Round 90` |
| `e5200aff` (wave evidence) | `.ufo/waves/round-90/w1-results.json`, `.ufo/waves/round-90/w1/Mo90Sc01Scope.md`, `.ufo/waves/round-90/w1/Mo90M01Mut.md` (the seat's final revision at the landed bytes) | wave dir only |
| `d1c84889` (preserved, not a landing) | in-flight round-90 files preserved at run-15 wrap-up | — |

No change to any `PROVINCE.md`, `MISSION.md` or fleet-root file. No counter was edited after its
after-receipt; `git diff --stat 11197820 HEAD -- .ufo/waves/round-87 .ufo/waves/round-88
.ufo/waves/round-89/count-c1.py .ufo/waves/round-89/count-c2.py .ufo/waves/round-89/heldout-c1.py
.ufo/waves/round-89/noharm-c1.py .ufo/waves/round-90/count-c1.py .ufo/waves/round-90/count-c2.py
.ufo/waves/round-90/battery` is empty.

Defects found and **not** fixed this round (routed, see Limits): the `--scratch` leak in the C1 selftest
(§7.4 makes a counter amendment the next-round action), the lookup-table reachability of P-C1, the F1
canary forgery of P-C2, and the `BATTERY` line's field count.

## Before → after measurements

Counting commands, each run against the lane (counter bytes unchanged between `11197820` and the tip,
so the measured revision is the counter's own commit). Re-run this session:

```
python3 -I .ufo/waves/round-90/count-c1.py <rev> --repo /home/vgpnk/Projects/shokunin/mori-shokunin
python3 -I .ufo/waves/round-90/count-c2.py <rev> --repo /home/vgpnk/Projects/shokunin/mori-shokunin
```

| Claim | Before (`037c02ca43a5`, do-nothing) | After (`e5200affd7eb`, lane tip) | Axis |
|---|---|---|---|
| C1 | `C1=unmet branch_open=8 harm=0 newopen=0 open=30 cases=78 rev=037c02ca43a5` — rc 1 | `C1=met branch_open=0 harm=0 newopen=0 open=22 cases=78 rev=e5200affd7eb` — rc 0; `BATTERY cases=18 branch_cases=14 branch_open=0 harm=0 newopen=0 paths=1` | operability 7 |
| C2 | `C2=unmet mutants=15 killed=12 survivors=3 unattributed=0 unanchored=0 isolated=0 literal_anchors=0 arms=28,26 detector=green rev=037c02ca43a5` — rc 1 | `C2=met mutants=15 killed=15 survivors=0 unattributed=0 unanchored=0 isolated=0 literal_anchors=0 arms=29,27 rev=e5200affd7eb` — rc 0 | calibration 5 |

Controls, committed before any after-value (`.ufo/waves/round-90/evidence/controls-r90.txt`): do-nothing
reads both unmet; a gate that refuses every command reads `harm=37` (refusal-all is not a gain); the three
new C2 labels declared without their arms read `survivors=3`; both counters' selftests green
(`C1_COUNTER_SELFTEST pass=12 fail=0`; `C2_COUNTER_SELFTEST pass=21 fail=0`, re-run at the tip rc 0).

Other no-harm instrument at the tip (`0a1f019b`; the later commit touches no counter bytes):
`python3 -I .ufo/waves/round-89/noharm-c1.py <rev> --repo <lane>` → `NOHARM harm=0 open=0 gained=3 cases=34`, rc 0.

Frozen-constant disclosure: P-C2 froze `arms=29,27`. B4 and B6 both live in `.ufo/waves/round-88/count-c2.py`,
and each declared mutant needs its own FAIL label, so two separate arms would read 28 (`pristine-arms`).
The landing merges the two mutation-free constant pins into `frozen_constants` (`SUBJECT_ARMS == 26` and the
`missing-replay` label, both still asserted), so the net count is 26 + 2 − 1 = 27. No assertion was lost;
the arm that was removed as a separate label was a pin, not a mutant kill. Recorded as lesson mistake 1.

## Sources & frontier

`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin mori`
— round start (`037c02ca`): 384 rows (`git show 037c02ca:corpus/SOURCES.md | grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}'`
→ `384`); round end (`e5200affd7eb`): `mori ok …/corpus/SOURCES.md` rc 0 (warnings only: W04 for S612–S614
sharing S611's URL and S615/S616 sharing a Python docs URL with pre-existing rows); `…census --root … mori` →
`rows 389`, `tier.A 349`, `tier.B 19`, `tier.C 21`, `status.mined 331`, `status.queued 24`, `status.rejected 34`.
Round-start tier counts (A 344, B 19, C 21) are from the round-89 closure; `git diff --numstat 037c02ca e5200aff --
corpus/SOURCES.md` → `5 0`, so the only change is five appended rows.

- **Rows added (5, all tier A, all `mined`, `recheck 90d`, `used-by corpus/knowledge/branch-reachability-r90.md`):**
  S612 POSIX.1-2024 §2.9.3 Lists; S613 §2.9.4.4 The if Conditional Construct; S614 §2.15 `exit [n]`
  (all three on `https://pubs.opengroup.org/onlinepubs/9799919799/utilities/V3_chap02.html`, access
  2026-11-05); S615 Python 3.15.2 `ast` (`https://docs.python.org/3/library/ast.html`); S616 Python 3.15.2
  `tokenize` (`https://docs.python.org/3/library/tokenize.html`).
- **Quotes located** (each ≤25 words; this L1 confirmed each occurs exactly once in tag-stripped text of the
  pinned copies in `.ufo/waves/round-90/w1/Mo90S01Sources/sources/`):
  S612 "shall have equal precedence and shall be evaluated with left associativity";
  S613 "the exit status of the then or else compound-list that was executed, or zero, if none was executed";
  S614 "The exit utility shall cause the shell to exit from its current execution environment";
  S615 "Recursively yield all descendant nodes in the tree starting at node (including node itself), in no specified order.";
  S616 "The scanner in this module returns comments as tokens as well".
- **Rejected:** `https://pubs.opengroup.org/onlinepubs/9799919799/utilities/exit.html` — HTTP 200 script-redirect
  page with no specification text; no quote could be located. Flip condition in the lesson's `## Gate`.
- **Rows touched old→new:** 0.
- **Frontier rows advanced:** the execution-binding family moves from token-level positions (S611, round 89) to
  control-flow positions (S612–S614); the structural-pin family enters with S615/S616. The knowledge entry marks
  the `!`, loop-body, `break` and `case` items `[INFERENCE]` — no opened source states them; the held-out battery
  is their only ground.
- **Sourced claim:** C1's rule rests on S612–S614; C2's structural pins rest on S615.
- **Mistake mined:** `corpus/lessons/round-90.md` `## Mistakes` (four rows: `frozen-after-constant-unreachable`,
  `behavioural-negative-arm-collides-with-a-blunter-mutant`, `class-target-reachable-by-a-lookup-table`,
  `selftest-orientation-unrecorded`), each with an evidence pointer and a fix that is shown able to fail.
- **Assimilation: none.** `merge/mori/` was not taken — the claims are instrument repairs under a frozen
  contract. `considerthese/2026-10-26.md` proposal 1 was read and does not fit either claim.

## Trend verdicts

- **expansion — improved.** A new capability class (branch reachability over recorded command text) is in the
  gate, graded by a held-out battery: `branch_open` 8 → 0 on the frozen class, 0 of 14 held-out branch shapes
  still bound. The frontier gained five sourced rows and one knowledge entry. Limit: the 22 provenance
  counterfeits stay bound and are reported.
- **quality — improved.** `harm=0 newopen=0` on the 78-case population, the 34-case no-harm battery
  (`harm=0 open=0 gained=3`) and the 18-case held-out battery at the tip; the five glued-paren harms were found
  and are not present on the landed bytes; C2's three arms kill attributably and isolated at the tip. Limits:
  F1 HIGH (label-accurate canary forgery) and F2 MEDIUM are open; 7 of 24 landed-rule mutants survive.
- **discernment — unchanged.** The round recorded its own assurance failures (the frozen `arms=29,27` and the
  lookup-table reachability) rather than smoothing them, but no non-author outside verdict on this round exists:
  every attacker is a seat this lane dispatched (LEARNING.md), and the open F1 and lookup-table findings show the
  frozen counters still cannot tell a faked pass from a real one. Scored as unchanged, not improved.

Admission reading for the operator: both frozen predicates verify at `e5200affd7eb` by their counters; no
axis is harmed by a measured number (the arms merge is disclosed, not a reduction of any asserted check). The
open findings below limit what the verified numbers prove and are routed, not waived.

## SHONEN

- [~] SKILL.md carries real decision tables and cited sources — `SKILL.md` round-90 registry pointer
  (`0a1f019b`); `corpus/QUALITY.md` 190–192; `corpus/knowledge/branch-reachability-r90.md`.
- [~] At least one end-to-end domain task executed and logged — `LOG.md` `## Round 90`; both counters re-run
  this session at `e5200affd7eb` (C1 rc 0, C2 rc 0); receipts `.ufo/waves/round-90/evidence/{controls-r90,after-r90}.txt`.
- [~] Instructions executable by an agent without oral context — `python3 -I .ufo/waves/round-90/count-c1.py <rev>
  --repo <clone>` and `count-c2.py <rev> --repo <clone>`; both replay committed bytes and exit 0/1. Limit (named,
  not waived): the C1 selftest ignores `--scratch` (`count-c1.py:223`, sentinel §1).
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` unchanged; the round touched no dispatch,
  OS, package or harness surface; the knowledge entry's Limits section names the provenance class.

## Wave, seats and round shape

- **One v1 wave of 13 seats** (`ufo-wave-policy.json`, band 8–16): `.ufo/waves/round-90/w1-spec.json`,
  `w1-dispatch.json`, `w1.ready` (00:30) and `w1.ready.dispatched` (00:31). WAVE-DONE `w1` received from the
  orchestrator after all 13 settled; results at `.ufo/waves/round-90/w1-results.json` (committed `e5200aff`).
- Role mix: executor 4 (`Mo90E01Gate`, `Mo90E02ArmB1`, `Mo90E03ArmsB46`, `Mo90E04Battery`), scout 1
  (`Mo90Sc01Scope`), scribe 2 (`Mo90S01Sources`, `Mo90S02Lesson`), reviewer 2 (`Mo90R01C1`, `Mo90R02C2`),
  critic 1 (`Mo90C01Critic`), mutation-tester 1 (`Mo90M01Mut`), connector 1 (`Mo90K01Conn`), sentinel 1
  (`Mo90Se01Boundary`).
- Attack seats 4/13 = 31 % (reviewer 2, critic 1, mutation-tester 1); connectors 1; no labrat.
- Dead seats: 0 — all 13 seats produced a report in the wave dir and appear in `w1-results.json`.
- Residual call: none. Round total: 13 seats.
- The L1 held the canonical planner seat; the bounded planning data-walk rode `Mo90K01Conn`.
- Inherited state: the attempt-1 and attempt-2 round-90 outputs (watchdog `lane-dead-no-report mori round=90`
  at 22:34) were re-verified before reuse — the contract, both counters, the controls script and its receipt, and
  the spec (`w1-spec.inherited.json` kept alongside `w1-spec.json`). Nothing discarded.

## Limits and routed defects (round 91)

1. **F1 HIGH — P-C2 kill attribution is forgeable (OPEN).** A label-accurate canary reads `killed` on all four
   count-c1 mutants (`Mo90R02C2.md` §F1). The frozen `failset == {arm}` clause does not separate it from a real
   arm. Route: a detector arm that requires each declared arm to be green on the pristine copy and red only on
   its own mutant.
2. **P-C1 reachable by a lookup table (OPEN; QUALITY 191).** A 21-string `frozenset` reaches the frozen line
   (`Mo90C01Critic.md` §1). Route: synthesize the held-out population inside the counter with a per-run nonce
   (`Mo90C01Critic.md` correction 1).
3. **Battery trust (OPEN).** `class`, `expect`, `reach` and `branch_cases>=12` are read from the file; no
   executing-command guard (`Mo90C01Critic.md` §4c; `Mo90Se01Boundary.md` §4).
4. **`--scratch` not honoured by the C1 selftest (OPEN; §7.4).** `count-c1.py:223`; six synthetic directories
   left under `/tmp` by this round's control run (reaped by the driver; no citation depends on them). Route: the
   counter amendment next round.
5. **`BATTERY` line field count (OPEN).** Six printed fields versus four in the frozen sentence
   (`Mo90Se01Boundary.md` §5). The `C1=` and `C2=` lines are identical to their frozen sentences.
6. **Landed-rule mutant survivors (OPEN).** N10, N15, N17, N20 (nesting check), N21 (parent-prefix `same_path`),
   N23/N24 (`control_atoms` split) — `Mo90M01Mut.md` Table 1.
7. **B4 pin is spelling-specific (OPEN, F2 MEDIUM).** `Mo90R02C2.md` §F2.
8. **Frozen-constant merge (disclosed).** `count-c2.py` `frozen_constants` (see Before → after).
9. **Candidate churn during the wave (process).** The gate candidate changed three times while the wave ran
   (`ab0c9104…`, `79350315…`, landed `3fc9cc44…`; `Mo90E01Gate` states that another writer changed the file).
   Every graded table names the sha it graded; the landed bytes were graded by `Mo90M01Mut` and by this L1.

No L0 question is raised: every item above is routed inside the lane's own round-91 plan, none needs an operator
decision. `.ufo/l0-questions.md` has no line for `mori | round-90`.

## Other required lines

- **Stale-lane:** respawn-per-round driver; no other mission of this lane is open.
- **Tool installs:** none. No package transaction (pacman paused); system `python3`, `git`, `strace` only.
- **Misroot sweep:** `git -C /home/vgpnk/Projects/shokunin status --porcelain` at report time shows one staged
  zero-byte `mo.tip` (mtime 2026-11-04 23:58, before any round-90 seat ran; no content names mori or round 90).
  It is not a seat file of this round and was left untouched. No untracked mori-round-90 file sits at the fleet root.
- **Pre-report gates:** `git ls-remote origin refs/heads/master` = `e5200affd7eba792e8b4ecf46ca6a3ae4bb07a8e`
  (equals the lane tip reported above); `grep -c '^## SHONEN'` on this file = 1 (checked before commit).
- **Commits this round:** `11197820`, `9441ef30`, `0a1f019b`, `e5200aff` (lane, via `jj-lane.sh commit`); this
  report via `fleet-commit.sh --as mori`.
