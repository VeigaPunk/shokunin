# souji — round 82 report (attempt 1, L1 `SoujiR82`)

Lane repo `/home/vgpnk/Projects/shokunin/souji-shokunin`, base `488956c45166ed6edc21567e8588a8134413949e`
(r81 closed `admitted`). Landed lane tip **`44e074018b2acb89f6143195d34c5c90237e8655`**
(`ls-remote origin refs/heads/master` prints it; `jj-lane.sh state` `ahead=0`). Lane commits this round:
P `1cb7c7d1` (instruments/controls/prereg) → F `d302b4f3`/F2 `28fd32c0`/F3 `1ec433c6` (freeze path fixes) →
W1 `f5bc4197` (C1 counter) → W2 `73110f6f` (C2 tool) → A `9881676a` (records/knowledge/quality/skill/scorecard/log)
→ `7dc3c726` (wave w1 spec + dispatch) → **W3 `c5c3f087`** (wave reconciled: amendments, ledger, repair R1) →
**`44e07401`** (receipt binding).

## Work performed

Two declared claims, one axis-move each, causally separable (verified both ways by `S82Connector` §1: strace +
ref-free clone at W1/W2 — each claim verifies with the other's bytes absent).

- **C1 — calibration (7, the lowest owned non-retired axis): the pointer counter binds the token's own round tree.**
  Before: the r81 counter accepts the two own-tree decoy rows NF-F/NF-G
  (`census/round-82/controls/c1-K-a-r81-counter.txt`, `mismatches=2 accepted=2`). After: the r82 counter refuses
  NF-F/NF-G/NF-H/NF-I and keeps TF1–TF5 and PF-1 (`census/round-82/records/c1-after.txt`,
  `rows=32 mismatches=0 accepted=0 refused_true=0 errors=0`, EXIT=0). Delta delivered by `_owntree_ok`
  (`census/round-82/c1-pointer-counter.py:310-319`, fired at `:353`); five regression suites green (r78 22/22 +
  12/12, r77 35/35 + 7/7, r79 9/9, r80 18/18, r81 25/25).
- **C2 — operability (8): the vault tool kills the CLI's descendant tree on a caller's signal.**
  Before: with job control in the tool's environment the base leaves the CLI's own `sleep 600 &` grandchild
  (`census/round-82/controls/c2-K-a-do-nothing.txt` under `env SHELLOPTS=monitor`, `mismatches=4 orphans=4`; the
  base passes the default launch 16/16, `records/prefreeze/c2-base-default.txt` — the bounded baseline). After:
  `records/c2-after.txt` and `c2-after-monitor.txt`, `rows=16 mismatches=0 errors=0 orphans=0` EXIT=0 under both
  launches; selftest `57 checks, 0 failed`; r17 `total=37 failed=0 skipped=0`; probe D `arms=6 failed=0`.
- **Wave `w1` — 14 seats, one v1 wave** under `scripts/hyaku/ufo-wave-policy.json` (band 8–16), 8 attack seats
  (57 %: 1 reviewer, 2 critic, 2 mutation-tester, 1 sentinel, 2 connector), 2 scout, 3 executor, 1 scribe.
  Spec `w1-spec.json`, dispatch `w1-dispatch.json`, results `w1-results.json`; seat reports committed under
  `census/round-82/records/wave-w1/`. **One dead seat: `S82ExecC2`** (87-byte `Status: in progress` stub, no
  re-derivation, no error text — it wrote and never returned); C2 lost no conjunct because `S82Sentinel`,
  `S82MutTool` and `S82Connector2` each re-derived 16/0/0/0 under both launches independently.
  Round total **14 seats**; no residual call.
- **Both claims reproduced by non-author seats before any amendment:** `S82ExecC1` reproduced all 32 ROW lines,
  the three controls and all five regression receipts byte-for-byte; `S82Connector` §0 reproduced C1 and C2;
  `S82Sentinel`, `S82MutTool`, `S82Connector2` each reproduced C2 under both launches.
- **Pre-file falsification (Amendment 59).** The wave falsified six sentences of the frozen wording and I amended
  each down to the property the counter enforces, citing the artifact, before filing:
  own-tree branch order (`plans/round-82.md` A1), own-tree rule scope (A2), census-branch attribution (A3),
  control provenance (A4), identity-clause separability (A5), the C2 handler's `$!` rationale (A6), the `m1/m2`
  monitor label (A7), the tree-walk cost/reuse window (A8) and the noisy before-baseline (A9).
  Ledger `.ufo/waves/round-82/claim-falsification.tsv` (committed copy `census/round-82/records/wave-w1/`),
  claims `.ufo/waves/round-82/claims.json`: 8 attack seats reconciled, 8 rows, 7 `falsifies-wording` + 1 `neutral`.
- **One harm the round introduced, repaired before filing (W3 `c5c3f087`).** W2 replaced base's
  `local pid=${CLI_PID:-${!:-}}` with `local pid=${CLI_PID:-}`, so a signal arriving between `timeout … &`
  (`tools/souji-vault-verify.sh:290`) and `CLI_PID=$!` (`:291`) ran the handler with an empty pid: it printed
  `souji-vault-verify: SIG<name> … stopped it, no verdict` and exited 143 with the CLI subtree alive
  (`S82Sentinel` F-1: A/B 150 iterations, base 0 orphans vs W2 1; window measured 4.07 ms on the real tool; the
  prereg's rationale "`$!` is never the timeout pid here" is false — `:290` is the tool's only background launch).
  R1 restores the base expression; the frozen counter re-passes 16/0/0/0 under **both** launches on the repaired
  bytes (`census/round-82/records/repair-w3/`, tool sha256 `dd6d440e…`), with selftest 57/0, r17 37/0/0 and
  probe D 6/6.
- **A seat finding was rejected, not swallowed.** `S82Connector` F1 concluded "the mutant that would isolate the
  round's own new rule is absent" because the K-b variant is the r81 counter two docstring lines apart. Re-derived:
  removing `_owntree_ok` *yields* that counter (its other new branch is dead code), so K-b is exactly that
  isolation. A4 adopts the provenance observation and rejects the conclusion; the ledger row records both.
- **Source work.** One candidate opened and rejected: `procps-ng` pgrep(1) — the parent-lookup mechanism
  `cli_kill_tree` uses — refused as S330 because the lane already holds S075 for process identity and the
  mechanism is proven by the m1/m2 rows (`corpus/lessons/round-82.md` `## Gate`; `S82CriticDiscern` agrees and
  calls the flip condition sufficient). `Assimilation: none` (no `considerthese/` in this lane, no shokuknow
  theme fits the claims).
- **Tracked files corrected where the wave falsified their text:** `SKILL.md:954` (the `m1/m2` monitor clause),
  `corpus/knowledge/gate-signal-handling.md` r82 section (the `$!` drop replaced by the measured window + repair
  + four new limits), `corpus/QUALITY.md` Q150 (supersedes Q148's order clause and Q149's row clause) and Q151
  (new: a rule's shape names must be the shapes the real rows have), `SCORECARD.md` round-82 addendum.

## Landed changes

| change | LOG.md entry | commit |
|---|---|---|
| C1 counter `census/round-82/c1-pointer-counter.py` (own-tree binding) | Round 82 · C1 | `f5bc4197d426527adc6f5d52f2d7834c0f021f2e` |
| C2 tool `tools/souji-vault-verify.sh` `cli_kill_tree` | Round 82 · C2 | `73110f6fe56f2a8383baed0ea7dc77f8b7f6ba5e` |
| records, knowledge r82 section, QUALITY Q148/Q149, SKILL r82 rows, SCORECARD, LOG | Round 82 · records | `9881676ac21637c24d2e23363365e1aa67a693fd` |
| wave w1 spec/dispatch (14 seats) | Round 82 · Wave | `7dc3c7260fa19b2311d413597ad8f948c57be9c1` |
| `plans/round-82.md` A1–A9; `claim-falsification.tsv` + `claims.json` + seat reports committed under `census/round-82/records/wave-w1/`; **repair R1** in `tools/souji-vault-verify.sh`; `census/round-82/records/repair-w3/`; SKILL/knowledge/QUALITY Q150–Q151/SCORECARD/LOG/lesson corrections | Round 82 · Wave, Repairs, Corrected after the wave | `c5c3f087a3b33259b725da2b4e556703168fa65e` |
| W3 receipts bound to the repair commit and its tool digest | Round 82 · Repairs | `44e074018b2acb89f6143195d34c5c90237e8655` |

## Before → after measurements

**C1 — calibration.** Counting command and both ends measured against the branch tip `44e07401`:

```
python3 -B census/round-82/c1-false-row-harness.py --counter <counter> \
  --lane /home/vgpnk/Projects/shokunin/souji-shokunin --fleet-root /home/vgpnk/Projects/shokunin --work <empty scratch>
```

- before (r81 counter, `controls/c1-K-a-r81-counter.txt`): `SUMMARY rows=32 mismatches=2 accepted=2 refused_true=0 errors=0`, EXIT=1
- after (`records/c1-after.txt`, rev `73110f6f`): `SUMMARY rows=32 mismatches=0 accepted=0 refused_true=0 errors=0`, EXIT=0
- K-b (own-tree-removal mutant) `mismatches=2 accepted=2`, K-c (suffix→last-component) `mismatches=2 accepted=2`; regressions r78 `items=22 resolved=22` + `forged=12 matched=12 accepted=0`, r77 `items=35 resolved=35` + `forged=7 matched=7 accepted=0`, r79 9/9, r80 18/18, r81 25/25.

**C2 — operability.**

```
python3 -B census/round-82/c2-vault-signal-counter.py --tool tools/souji-vault-verify.sh --work <empty scratch>
# the same under: env SHELLOPTS=monitor
```

- before (Base `488956c4`, monitor launch, `controls/c2-K-a-do-nothing.txt`): `SUMMARY rows=16 mismatches=4 errors=0 orphans=4`, EXIT=1 — red in 5 of 5 runs, modal 4 (`S82Connector2` F4); base default launch 16/16 = bounded baseline
- after W2 (`records/c2-after.txt`, `c2-after-monitor.txt`, rev `73110f6f`): `rows=16 mismatches=0 errors=0 orphans=0`, EXIT=0 both launches
- after W3 repair (filed bytes, `records/repair-w3/`, tool sha256 `dd6d440e…`): `rows=16 mismatches=0 errors=0 orphans=0` EXIT=0 default **and** monitor; `selftest: 57 checks, 0 failed`; r17 `SUMMARY total=37 failed=0 skipped=0`; probe D `SUMMARY arms=6 failed=0`

Both claims carry stated limits, not claims: own-tree `wN/` over-refusal (C1), identity clause inseparable from a
suffix-only rule on this population (C1), per-node `pgrep -P` cost ≥12 descendants exceeding the 5 s settle,
snapshot→KILL reuse window, unguarded `pgrep`, `/var/tmp` default, untraced-only reproduction (C2). Full list:
`claims.json` → `stated_limits`; routing: `corpus/lessons/round-82.md` `## Routed to round 83`.

## Sources & frontier

- `SOURCES.md` rows **before → after: 252 → 252** (tier A 242, rejected rows 22 in both).
  Counting command: `grep -cE '^\|[[:space:]]*S[0-9]{3,}' corpus/SOURCES.md` (before read at
  `488956c45166ed6edc21567e8588a8134413949e`).
- Registry census before → after, both EXIT=0:
  `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin souji`
  (`records/census-before.txt`; after: `souji ok …/corpus/SOURCES.md`, `CENSUS_EXIT=0`).
- Rows added by tier: **0** (none in any tier). Rows touched old→new: **0** (`status`/`recheck`/`used-by`
  unchanged; registry agreement `k1=1 k2=1` at W2, both accepted-red and pre-dating this round,
  `records/registry-agreement-at-W2.txt`). Frontier rows advanced: **none** — the round's one candidate (S330,
  procps-ng pgrep(1)) was rejected under CORPUS rule 4 as a duplicate of S075's process-identity scope and is
  recorded with its flip in `corpus/lessons/round-82.md` `## Gate`.
- `S82CriticDiscern`'s proposed rule (a rejected candidate should also be a `rejected` registry row, not lesson
  prose only) is routed to round 83 rather than adopted mid-round.
- Sourced claim: C2 rests on S325/S326 (bash signal semantics, timeout's `setpgid`) as recorded in the prereg;
  the r82 rows are the instrument's, so no new row was opened.
- Assimilation: **none** (`corpus/` exists and the frontier step ran; no `considerthese/` in this lane and no
  `merge/souji/` theme fits C1/C2).

## Trend verdicts

- **expansion — unchanged.** No new corpus row, no new frontier ground, no new tool: the round deepens two
  existing instruments. The rejected S330 candidate is a deliberate non-expansion (CORPUS rule 4).
- **quality — improved.** Six frozen sentences that overstated what the instruments enforce are now amended to
  the enforced property with the falsifying artifact cited (`plans/round-82.md` A1–A9), two new criteria are
  mined from the wave (Q150 order/label, Q151 real-shape grounding), and a harm the round itself introduced is
  closed before filing (R1, re-measured on the filed bytes). Evidence: `claim-falsification.tsv`; `corpus/QUALITY.md`
  Q150–Q151; `corpus/lessons/round-82.md` M3–M6; `census/round-82/records/repair-w3/`.
- **discernment — improved.** A seat's MEDIUM that would have retracted a landed control was re-derived and
  rejected on the bytes (A4), a second seat's re-assertion of the falsified branch order was caught and recorded as
  non-corroboration (ledger row `S82CriticDiscern`), an unexplained dead seat is reported as dead rather than
  back-filled, and the round files narrowed claims instead of the wider frozen sentences.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — gate registry rows for
  both r82 instruments (`SKILL.md:954-955`), the r82 monitor clause corrected this round; S330 reject recorded in
  `corpus/lessons/round-82.md` `## Gate`. No named non-author verifier this round, so `[~]`, not `[x]`.
- [~] At least one end-to-end domain task executed and logged in LOG.md — the closest this round has is the real
  lane-surface probe set (frozen counters over committed bytes + the repaired tool's selftest/r17/probe-D run,
  `LOG.md` Round 82). Read-only; the historical operator-sweep domain task is `LOG.md:362`.
- [~] Instructions executable by an agent without oral context — `census/round-82/preregistration.txt` + the two
  gate rows in `SKILL.md` + `plans/round-82.md`; `census/round-82/rec.sh` makes the receipts replayable.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — the round touches only lane tooling, counters and
  corpus registers; `S82Connector` §2 documents eight sibling-lane `$(timeout …)` exposures read-only and modified
  no sibling file. `PROVINCE.md` unchanged.

## Wave, seats and round shape

14 seats in one v1 wave (`w1`), policy band 8–16, roles: 2 connector, 2 scout, 3 executor, 2 mutation-tester,
1 reviewer, 2 critic, 1 sentinel, 1 scribe. Attack share 8/14 = 57 % (floor 25 %); connector seats 2 (cap 2).
Planner seat held by the L1 (validator forbids a `planner` seat). Routes captured at spawn from
`task.agentModelOverrides`; no `model` argument passed anywhere. **Dead seat: `S82ExecC2`** — stub only.
Round total 14 seats, no residual call. Per-seat verdicts: `corpus/lessons/round-82.md` `## Wave`.

## Inherited state, misroot sweep, tooling

- **Inherited:** none. `jj-lane.sh state` at round start: `local=remote=488956c45166ed6edc21567e8588a8134413949e
  ahead=0 tracked=0 untracked=0`. The prereg records that earlier attempts of this round (watchdog
  `lane-dead-no-report` attempts 1–3 at 2026-11-07 07:15–07:17) ended before any commit — nothing inherited.
- **Misroot sweep** (`git -C /home/vgpnk/Projects/shokunin status --porcelain`): the only untracked additions are
  `.scratch/run15-wrapup/misroot-cff0b4cb/` and `plans/round-91.md`. Both are **another lane's** (round 91; no file
  names souji) and `.scratch/` is orchestrator-owned: **left untouched**, named here per protocol. No souji seat
  wrote into the fleet root this round (all seat scope was `.ufo/waves/round-82/w1/`).
- **Tooling:** none installed. No pacman (paused host-wide, untouched), no `uv`/`npx` install, no sysctl, sudo,
  kernel or host-service change. `scripts/hyaku/disk-guard.sh status` clean at every heavy pass.
- **Pre-file falsification gate:**
  `python3 /home/vgpnk/Projects/shokunin/scripts/hyaku/prefile-falsification.py --lane souji --round 82` →
  `PREFILE-FALSIFICATION: pass claims=2 rows=8 attack_seats=8 findings=0` (EXIT 0).
- **Stale-lane:** no — this is a respawn-per-round driver round; no other mission of this lane is open.
- **L0 questions:** none filed this round; earlier open items are unaffected.

```json
{"lane":"souji","round":82,"attempt":1,"verdicts":{"C1":"verified-narrowed","C2":"verified-narrowed-and-repaired"},"lane_head":"44e074018b2acb89f6143195d34c5c90237e8655","wave":{"shape":"one-v1-wave","seats":14,"attack_seats":8,"dead":["S82ExecC2"],"total":14},"ledger":{"rows":8,"attack_seats":8,"falsifies_wording":7,"neutral":1},"prefile_gate":"pass claims=2 rows=8 attack_seats=8 findings=0 (EXIT 0)","sources":{"rows_before":252,"rows_after":252,"census_exit_before":0,"census_exit_after":0},"report_commit":"this file, fleet-commit --as souji (its own hash is not knowable before landing)"}
```
