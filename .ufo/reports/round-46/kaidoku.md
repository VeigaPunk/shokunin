# kaidoku — round 46

**Lane tip at filing: `c0112995817b4d8caddd86705b08e89bdac99640`** (`git -C kaidoku-shokunin ls-remote
origin refs/heads/main` prints it). Eight untracked files remain under
`.ufo/waves/round-46/w1/` from seats still writing when the budget closed; they are wave evidence,
not round work in flight.

**Claims declared (2, distinct tied-lowest axes, frozen before any score existed at
`332f48849966073e2f165c13f952eb4c8e165e39`; the freeze travelled through four earlier commits — see
*Freeze integrity* below):**

- **R46-C1 / depth** — `SKILL.md` `## Queue-drain craft` rule block 23, the freeze-integrity
  **discrimination** matrix: thirteen rows, each naming a defect the round-45 closure routed
  (R45-CL13 a–f, R45-CL14 a–f), the v1 clause that let it pass, and the round-46 arm that now fails
  it; every citation line-selected and resolving; the interpreter pinned by sha256.
- **R46-C2 / calibration** — the `SKILL.md` instrument registry, widened from six rows to the
  **38-instrument census** (`tools/round-46/census.json`, generated from the round-41..46 claim
  files), bound by two markers, exact cell-0 equality, verdict maps that bind 0/1/2, and
  `absent_at_rev` proving each named tool exists at the measured revision.

Both predicates are **met by their frozen counters** at `58eb04b6` against freeze `332f4884`: C1 exit 0 with
`rule_blocks 23`, `rows 13`, `refs 9`, `unresolved []` and the battery
`forgeries_total 9 / v1_green 9 / v2_green 0 / genuine_green 1`; C2 exit 0 with
`scope_size 38`, `registry_rows 38`, `unregistered []`, `thin []`, `absent_at_rev []` and the
battery `forgeries_total 7 / v1_green 7 / v2_green 0 / genuine_green 1`. **The point of the round
is the last three numbers of each line**: round 45's artefacts were genuine but its measures
accepted forgeries, so round 46's counters are required to score their own mutated copies red
while the genuine artefact stays green.

## Work performed

- **Freeze, then four corrections, all before any score existed.** `plans/round-46-claims.md` and
  `tools/round-46/{gate,attest,registry,census}.py` + `census.json` landed at `3182047`; the
  instruments were corrected at `50862e4a` (a guard returned an int where the caller unpacked a
  tuple), `65678df0` (the battery referenced a renamed regex, so it could only fail; the v1 port's
  header/row-floor/selector clauses; a battery selftest case) and `04252247` (the v1 registry
  profile applied the v2 strict cell/exit/presence checks), and `332f4884` (wave 1 found that the
  frozen set was derived at the measured revision and could be shrunk by it, and that the counters
  executed from the worktree with no dirty arm — both HIGH, both closed there). **The freeze is
  therefore a series of five commits, and its own plan says "the commit that first contains this
  file"** — the defect is mined as M46-3 and stated, not absorbed.
- **The instruments.** `gate.py` derives the frozen set from the claims file and feeds one set to
  the merge-aware history arm (`-m --diff-merges=first-parent`, closing R45-CL6), an independent
  blob arm, the restored classifier (R45-CL18 by construction) and the dirty scope, and refuses a
  `--json-out` inside the graded or frozen set (R45-CL22) and a temporary-partition scratch root
  (R45-CL20). `attest.py` and `registry.py` each carry a `--profile v1` port of the round-45 clause
  set plus the `--profile v2` hardened check and a mutation battery built from the landed bytes.
  Selftests: `ATTEST_SELFTEST cases=18 failures=0`, `REGISTRY_SELFTEST cases=12 failures=0`.
  Receipts under `.ufo/waves/round-46/l1/`.
- **R46-C1 landed** at `227d6982`; A1 `87578656` removed two path-like tokens the citation sweep
  read as citations; A2 `6e018068` re-pinned the interpreter to the measured freeze; A3 `7bf33e31`
  added a `corpus/knowledge/` citation, without which command A read `citation_resolved_rules
  22/23` — the depth claim would have harmed the depth proxy it claims to raise (M46-4: the
  round-45 A1 defect, one round later; now `QUALITY.md` row 77).
- **R46-C2 landed** at `781e19ae`: the `<!-- instrument-registry v2 -->` section with 38 rows.
  Thirty-five rows were drafted by twelve wave-1 executor seats from the tools' sources (receipts
  `.ufo/waves/round-46/w1/R46W1Reg*/`); the three the last seat did not produce were written by the
  L1 from source as a fallback when the last seat was still empty; that seat then landed
  source-derived rows and found two errors in the L1's own row for `tools/round-43/c1-counter.py`
  (exit 1 also covers a pair miss with all bindings true; the key is `bindings_false`, not
  `failing`), so amendment B1 `47b5e265` replaced all three with the seat's rows and re-measured
  both claims with identical values.
- **Sources opened:** S142 (`git-log` `--diff-merges=first-parent`), re-fetched twice by a wave-1
  seat with a stable page sha256, a located 19-word quote and a deterministic merge fixture that
  shows the arm is **order-sensitive** (routed as R46-CL6).
- **Record:** `LOG.md` round-46 entry + claim ledger; `SCORECARD.md` `## Round 46`;
  `corpus/lessons/round-46.md` (M46-1..M46-4, `## Gate`, R46-CL1..CL6); `corpus/QUALITY.md` row 77.
- **Misroot sweep:** `git -C /home/vgpnk/Projects/shokunin status --porcelain` read before this
  report: no untracked fleet-root file names this lane or this round (`o.bin`, `oldrep*.out`,
  `.scratch/*` and two other lanes' reports predate or belong to their owners); nothing copied,
  nothing deleted.

## Landed changes

| change | LOG entry | commit |
|---|---|---|
| `plans/round-46-claims.md` + `tools/round-46/` (the two predicates, the batteries, the census, the shared gate) | round-46 claim ledger | `3182047` → `332f4884` |
| control receipts at the measured freeze (both do-nothing arms exit 1; v1 covers 6 of 38; both v1 fidelity receipts reproduce round 45) | round-46 entry, "controls" bullet | `c0ca5392`, re-scored at `17a72375` |
| `SKILL.md` rule block 23 (13 rows, 9 citations, interpreter pin) + `corpus/lessons/round-46.md` + S142 | round-46 entry, C1 bullet | `227d6982`, `87578656`, `6e018068`, `7bf33e31` |
| `SKILL.md` `<!-- instrument-registry v2 -->` section, 38 rows | round-46 entry, C2 bullet | `781e19ae`, rows corrected at `47b5e265` |
| two HIGH instrument defects closed (frozen-set union at both ends; dirty frozen path refuses a score) | round-46 amendment | `332f4884` |
| block 23 re-pinned and the R45-CL19 exit cell corrected | round-46 amendment | `58eb04b6` |
| C1/C2 measurements and the v1-gap receipt | round-46 entry, "measured" bullet | `1e32827b` |
| lesson M46-3/M46-4 + `corpus/QUALITY.md` row 77 | round-46 entry, "learned" bullet | `49e6cac4`, `21b55a8f` |

## Before → after measurements

Counting commands, each run from `/home/vgpnk/Projects/shokunin/kaidoku-shokunin` with
`HYAKU_SCRATCH=/fast/scratch/hyaku`:

```sh
python3 -I -B tools/round-46/attest.py   --root . --freeze 332f48849966073e2f165c13f952eb4c8e165e39 --rev 58eb04b6e5e886078121bb5e13fb95c687fe41bc
python3 -I -B tools/round-46/registry.py --root . --freeze 332f48849966073e2f165c13f952eb4c8e165e39 --rev 58eb04b6e5e886078121bb5e13fb95c687fe41bc
```

| claim | before | after | receipt |
|---|---|---|---|
| R46-C1 | at the freeze: exit 1, `marker_occurrences 0`, `block_present 0`, `rule_blocks 22`; and the round-45 clause set accepts every one of the nine forgeries | exit 0, `marker_occurrences 1`, `rows 13`, `refs 9`, `unresolved []`, `pin` matches the bytes at rev, `dirty []`, battery `9/9/0/1` | `controls/ctl-c1-0-do-nothing.json`, `l1/scores/c1-at-A4.json` |
| R46-C2 | at the freeze: the round-45 counter covers **6 of the 38** census instruments; the v1 clause set accepts all seven forgery classes | exit 0, `registered` 38 of 38, `thin []`, `absent_at_rev []`, `dirty []`, battery `7/7/0/1` | `controls/ctl-c2-1-v1-scope.json`, `l1/scores/c2-at-A4.json` |
| R46-C1/C2 across the amendments (`0425224`, `47b5e265`, `58eb04b6`) | — | identical values (`rule_blocks 23`, `rows 13`, `refs 9`; `scope_size 38`, `registered` 38, battery `7/7/0/1`); `c1-at-A2.json` is the one exception that the round repaired (`citation_resolved_rules 22/23`) | `l1/scores/c1-at-{F4,B1}.json`, `c2-at-{F4,B1}.json` |
| command A (depth proxy) | `rule_blocks 22`, `citation_resolved_rules 22/22`, `depth_score 10.0` | `rule_blocks 23`, `citation_resolved_rules 23/23`, `depth_score 10.0`, `knowledge_files 138`, `mapped 138`, `missing []`, `dangling []`, `coverage_score 10.0` | run at `7bf33e31`; output quoted in the LOG entry |

**Fidelity (the v1 port is not a straw man).** `--spec r45 --profile v1` at
`f762b727..f59565b7` reproduces round 45's receipts exactly: `rule_blocks 22`, `block_present 1`,
`rows 10`, `refs 8`, `unresolved []`, exit 0; and `registry_rows 45`, `scope_size 6`,
`registered 6`, `unregistered []`, `thin []`. Receipts `controls/ctl-c1-fidelity.json`,
`controls/ctl-c2-fidelity.json`.

## Sources & frontier

- **Census before → after.** Round start: 141 rows
  (`git show 3182047:corpus/SOURCES.md` piped to `sources-census.sh validate --file`, which reports
  `E11 S140/S141 missing used-by` because `--file` mode cannot resolve `used-by` targets — a mode
  limitation, recorded not hidden). Round end:
  `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kaidoku`
  → `kaidoku ok`, exit 0, 15 `W04` warnings (14 inherited + S142's same-URL different-scope row,
  which the Gate explains). Rows: 141 → 142.
- **Rows added by tier:** one (`S142`, `docs`, tier A). **Rows touched old→new:** none (no
  `status`/`recheck`/`used-by` cell of an existing row changed).
- **Frontier rows advanced:** none — this round adds no domain ground; S142 is instrument
  documentation, and `corpus/README.md` `## Frontier` is byte-unchanged.
- **Assimilation: none.** No `merge/kaidoku/` theme or `considerthese/` proposal applies to an
  instrument-discrimination round; `considerthese/` is absent in this lane; the round-44 quarantine
  refusals stand.

## Discrimination limits (what the measure still cannot see)

The round's purpose was to replace a measure that a forgery satisfied. Sixteen forgery classes are
now caught, but three blind spots remain and are stated rather than absorbed:

- **Two instrument bypasses were found and closed before this report (R46-CL9, R46-CL10).** The
  frozen set was derived at the measured revision, so one commit that rewrote its own
  `## Frozen paths` section to a decoy and edited a frozen tool read `exit 0 met_target true`; and
  the counters execute from the worktree while reading objects, with `gate.dirty()` written but
  never called although the claims file promised the dirty scope — a replaced worktree `gate.py`
  flipped red to green with zero commits. Both are closed in `332f4884` (union at both ends; a dirty
  frozen path refuses the score) with one selftest case each. The residual is stated: the executing
  bytes are not pinned, only the examined ones.
- **A contentless registry row passes (HIGH, R46-CL7).** Reproduced by the L1 at `47b5e265`: three
  rows whose `purpose`, `self-test`, `pinned-value` and `write-scope` cells are empty and whose
  verdict map reads `0=banana; 1=nope; 2=whatever` score `met_target: true`, exit 0, with the
  seven-forgery battery still green. The clause binds the digits, not their meanings — the same
  class as R45-CL14 (d), one level down.
- **The merge arm is correct only by flag order (R46-CL6).** `-m --diff-merges=first-parent` is
  right; `--diff-merges=first-parent -m` prints a merge twice and restores the blindness
  R45-CL6 was about. Nothing in the code enforces the order.
- **The mutation denominator is a count, not a digest (R46-CL4).** Deleting a mutation from
  `MUTATIONS` changes what `forgeries_total` means; the equality still holds against the new list.

C1 has no analogous content hole that this round found: its rows must name a routed id and an arm
token, and the arm token is a substring test (`blobberish` satisfies `blob`, R46-CL2).

## Trend verdicts

- **expansion — unchanged.** No admitted knowledge entry and no coverage-map ground: the two claims
  move instruments, not the domain. `knowledge_files 138`, `mapped 138` at both ends of the round.
- **quality — improved.** Both counters now score their own forgeries red (16 forgery classes across
  the two claims, each built by mutating the landed bytes) while the genuine artefacts stay green,
  and both reproduce round 45's verdicts on the round-45 artefact. Block 23 adds a decision table
  that names each routed defect and the arm that closes it, with every citation resolving
  (`23/23`). The bound: this is the *instrument* improving, not new reverse-engineering ground.
- **discernment — improved.** The round found four of its own defects before the operator did
  (M46-1 a control that named a measurement that could not exist at the freeze; M46-2 a frozen
  denominator the code does not pin; M46-3 four freeze commits; M46-4 the depth-proxy harm), and
  turned two of them into `corpus/QUALITY.md` row 77. It also reports the sharpest limit it found:
  the counters check that a registry row is present and well-formed, never that its prose is true
  (R46-CL5), and the merge arm's correctness depends on flag order (R46-CL6).

## Freeze integrity (disclosure)

The frozen set is derived from `plans/round-46-claims.md` `## Frozen paths (exact)`
(`plans/round-46-claims.md`, `tools/round-46/`) and feeds both the history arm and the blob arm, so
the pathspec boundary of R45-CL18 cannot exist here. The declared freeze is
`332f48849966073e2f165c13f952eb4c8e165e39`; `git log --name-status <freeze>..<tip> --
tools/round-46 plans/round-46-claims.md` is empty at every measurement above. **The freeze moved four
times after its first commit** (`3182047` → `50862e4a` → `65678df0` → `04252247` → `332f4884`).
Three of the moves are one class: the first commit did not contain bytes that could produce a
verdict, because the selftest ran every case with the battery disabled, so the scored path was never
executed (M46-3, gated by `QUALITY.md` row 77). The fifth move is the process working: wave 1 found
two HIGH bypasses in the arm itself (a shrinkable frozen set; an unpinned executing worktree) and
the round closed them before this report.

## SHONEN

- `[~]` **SKILL.md contains real decision tables, error patterns, checklists, cited sources** —
  block 23 (13 rows, 9 line-selected citations, `SKILL.md` `## Queue-drain craft`) and the
  38-row registry; command A `citation_resolved_rules 23/23` at `7bf33e31`.
- `[~]` **At least one end-to-end domain task executed and logged in LOG.md** — no domain task this
  round (instrument and record work); the standing evidence is the round-42 SquashFS v3 recursion
  (LOG round-42 entry, `eb8215ac`), unchanged.
- `[~]` **Instructions executable by an agent without oral context** — block 23's rows are executed
  by `tools/round-46/{gate,attest,registry}.py`; `attest.py --selftest` prints
  `cases=16 failures=0` and the battery scores the nine forgery classes from committed bytes.
- `[~]` **No cross-domain bleed (PROVINCE.md still accurate)** — `PROVINCE.md` is byte-unchanged
  this round; no Core row, capability or adjacency claim was added.

## Wave record

- Shape: **one v1 wave of 40 seats** under `ufo-wave-policy.json` (band 32–64), dispatch
  `w1-dispatch.json` with `counts {spawn: 40}`. **Wave 2 was specified and validated
  (`w2-spec.json`, `w2-dispatch.json`, 40 seats, 35 attack seats) but not dispatched**: the run
  budget closed first, and filing a report after launching a wave it cannot settle is worse than
  reporting the shortfall. **Round total 40 seats, below the 64–128 band — a round-shape defect,
  stated rather than padded.**
- Wave-1 role mix (40 dispatched): 17 executor, 5 reviewer, 4 critic, 3 mutation-tester, 4 scout,
  3 scribe, 1 sentinel, 1 revenger, 1 simplifier, 1 connector (12 attack seats, 30 %).
- Settlement: **32 of 40 seats produced a report**; the eight that did not are `R46W1CritC1`,
  `R46W1CritBattery`, `R46W1CritDenominator`, `R46W1MutC1Checks`, `R46W1MutGate`, `R46W1SentTools`,
  `R46W1SimplInstruments`, `R46W1ProbeCost`. No `w1-results.json` ledger was written for this wave,
  so the settlement is read from the seat report files at
  `.ufo/waves/round-46/w1/<name>.md`; the eight are recorded as producing nothing, and none was
  replaced.
- Settled attack seats: 5 reviewer, 1 critic, 1 mutation-tester, 1 revenger — 8 of 32 (25 %).
- The §3 L2 floor (≥8 seats in one batched swarm, with planner, connector, executors, scribe,
  scout, reviewer and critic) is met inside wave 1; the L1 holds the canonical planner seat (the
  validator rejects `planner`), with bounded data-walks riding `R46W1ScoutCraftTail`,
  `R46W1ScoutSiblingReg` and `R46W1ConnFleet`.

## Admission position

Both frozen predicates are met at the measured freeze by their own counters, and both counters
demonstrably score their own forgeries red while the genuine artefact stays green — the property
round 45 could not show. **What this round did not do:** wave 2 was not dispatched (round total 40,
below the band), and eight wave-1 seats produced nothing, so the falsification is one wave's worth,
not two. The honest bounds: the freeze is a series of four commits rather than one
(M46-3); the registry validates shape, not truth (R46-CL5); the merge arm is correct only because
two flags are in the right order (R46-CL6); and the mutation list is a fixed count no digest pins
(R46-CL4). Driver completion is not admission; the independent non-author verification remains.

## Open questions (L0)

None this round. The round-45 L0 items stand and were not re-opened: the dispatcher/ledger
question (L0-0) and the freeze-gate placement question (L0-1) are integrator/operator property, not
lane work.

## Stale-lane

None — the round was dispatched once (`.ufo/watchdog.log` line
`2026-10-28T13:36:07-03:00 launch kaidoku round=46 pgid=3728525 driver=hyaku-inline attempt=1`) and
this is its only mission.

## Tool installs

None. No pacman transaction; the host-wide pause was respected; nothing installed via `uv tool`,
`npx` or a release binary.
