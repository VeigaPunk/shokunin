# tabi — round 46 report

Lane repo: `C:/Users/jpvei/.zcode/workspace/95b1ba4d-5089-47a4-9fd8-54adebbce2ae/fleet/tabi-shokunin` (master).
Baseline `fe16cf6631e44ad0962cecf4c7c099b8d72efde5` → freeze `79b297f1d33df8c9b92bc423c2102d6712817662`
→ measured `951f70d33d9e3af208fb414e3079680c08dc66ba` → data corrections (frozen kill-rule flow:
sibling heads racing mid-measurement) `3b8a68dc47b0d578e67dcd0faaf42dd100cdc59a` →
`fd44a1b30e607bda0523f9464b6689399cbd651b` → **cited measured revision
`e2d59f729615e1c671ce44d1f4bed28e51f78a4f`** → integration tip `1eb1eb3fa59e9ce728cba25d2c5110bc83123c34`
→ round-close hygiene tip `9de5a79b31a9a164f7907763ed5ed7576d43e608` (lane head at filing; pushed;
instrument bytes byte-identical from freeze to cited revision — `git diff 79b297f1..e2d59f72 --
scripts/chrome-cdp-loopback-round46.mjs .ufo/waves/round-46/counters/ .ufo/waves/round-46/controls/`
is empty, receipt `measure/c1-committed-bytes-at-cited-rev.txt`).

## Work performed

- **Fresh-start discipline (binding §7).** The r41/r42/r43 rejected closures re-spot-checked in
  committed bytes: r41's untracked-receipt limb closed (`git ls-tree HEAD --
  corpus/evidence/round41/playwright-egress/` → `7b2ece05` + `5930d20f` are blobs at HEAD); r42's
  nonce-relabel/synthetic false-green class closed by the committed counter clause family (this
  round's counter selftest exercises 16 refusal mutants + 2 benign controls, verdict clean 18/18);
  r43's false-green/crash class closed via the committed D3 crash receipt. Ruled out for r46
  (reasons in `.ufo/waves/round-46/claims.json` `freshStartNote`): Firefox/BiDi (absent surface,
  PROVINCE r44 probe); any wave-settled claim (the r44 L0 line at fleet `.ufo/l0-questions.md:231`
  is still open — routed around, no wave clause in any predicate); knowledge/registry-count claims
  and the census-START receipt alone (do-nothing reachable — the receipt is carried as protocol
  work per the carry-in); the job-object variant as a second claim (same axis and fix family as
  C1 — two claims on one axis count as one — and the keyed PID-group route was taken because Node
  has no job-object surface here while a PowerShell Add-Type wrapper would move the launch outside
  the instrumented process; the carry-in sanctions either mechanism); re-running r45's receipts as
  r46 evidence (do-nothing reachable); reading the sweep green while a legacy control happens to
  show 0 orphans (the red limb is evidence-carried, never luck).
- **Carry-in item 1 — the teardown repair (C1, operability, sourced S155).**
  `scripts/chrome-cdp-loopback-round46.mjs` replaces the r45 teardown (SIGKILL the main child,
  then a `taskkill /T` that runs after the main is dead and walks nothing) with a **PID-group kill
  keyed to the launch**: a unique per-run profile token (12 fresh hex chars in the profile dir
  basename) that the browser and every helper carry verbatim in their command line; a pre-launch
  sweep must show 0 (fresh key, else refuse to start), a mid-run census must be nonempty (proof
  the token group binds the live launch), and the post-kill sweep kills each survivor BY PID and
  re-sweeps to 0, fail-closed at 15 rounds; the legacy `taskkill /T` attempt is recorded with its
  no-op output; `receipt.ok` requires `chromeTerminated` AND `postKillSweepCount === 0`. Red
  evidence: the live legacy control on Edge reproduced the r45 class — **16 launch processes
  outlived the legacy teardown** with the tree kill a no-op (exit 128) — and the deterministic
  mechanism fixture shows the same on real OS processes (1 survivor after the no-op tree kill).
  Green evidence: the keyed recovery swept the 16 to 0, and all three repaired full runs (edge,
  edge repro, chrome) ended at `postKillSweepCount: 0`. Counter
  `.ufo/waves/round-46/counters/chrome-cdp-receipt-r46.mjs` (selftest 18/18; refuses the r45
  receipt with 8 findings).
- **C2 (adjacency — the lowest owned axis, 8; nudge inactive, window position 2).** The 10 drifted
  map rows re-pinned at recorded snapshot heads with the full current line quoted (9 stale + 1
  moved → 0 stale, 0 moved; the 6 sibling-absent rows stay honestly absent); ledgers
  `corpus/adjacency-host-audit-r46.tsv` and `corpus/adjacency-host-delta-r46.tsv` regenerated at
  one snapshot; meter `.ufo/waves/round-46/counters/c1-adjacency-host-v6.mjs` re-grounded with a
  host-layer hardening this round's fleet state demands — all 16 sibling worktrees are dirty and
  heads move mid-round, so v6 reads every sibling byte through **git at a per-run snapshot head**
  (the worktree is never read) and prints the snapshot; the head binding then caught two real
  sibling moves mid-measurement (`lane-screen-head-mismatch` on shokunin-reverse-engineering;
  kama/kasegi in the corrections), each resolved by the frozen data-correction flow.
- **Carry-in item 3 — the census-START receipt committed** in the freeze
  (`.ufo/waves/round-46/measure/census-start.txt`; r45 had none).
- **Carry-in item 4 — the L2-floor L0** routed around, never treated as answered (the r44 line
  stands; the round ran L1-inline; no predicate carries a wave clause).
- **No-harm finding recorded with cause:** `scripts/check-adjacency.mjs` exits 2
  `could_not_evaluate` on this host — its `minimalEnv()` rebuilds PATH the Linux way (`:`-split,
  `/`-prefixed only), so git.exe cannot spawn on Windows (receipt
  `measure/c2-check-adjacency-hostbound.json`; the r44 legacy-gate class). Not silently patched;
  the gate's host-portable PATH repair is routed in the SCORECARD planned section. For every row
  this round changed, the quote-at-pinned-rev duty is carried by the v6 meter's full-line equality
  at the pinned rev (strictly stronger than the gate's substring check).
- **Round-close hygiene:** the committed sweep receipt (`measure/round-close-hygiene-sweep.json`)
  shows 0 tabi-r46 browser processes remain (the 4 command-line matches were this working
  session's own bash/node processes embedding the scratch path — left running, never killed);
  scratch deleted.

## Landed changes

| Commit | Content |
|---|---|
| `79b297f1…` | FREEZE (pre-data): claims.json (2 claims, predicates, kill rules, 6 frozen digests, 6 whole-line control bindings), r46 runner, counter + selftest, meter v6 + selftest, mechanism fixture, legacy control, 7 pre-data controls (edge/chrome probes with sweep fields, counter cross-refusal of the r45 receipt, meter baseline red 28 findings, legacy pilot, mech pilot), **census-START receipt committed**, S155 staged copy, both selftest receipts |
| `951f70d3…` | MEASURED CLAIMS: edge/chrome evidence pairs (receipt+shot, committed explicit files), edge repro receipt, live legacy control receipt (16 orphans → 0), mechanism red/green receipt, counter receipts x3, adjacency map re-pin + audit-r46 + delta-r46 |
| `3b8a68dc…` / `fd44a1b3…` | DATA CORRECTIONS under C2's frozen kill rule (sibling heads moved mid-measurement; instruments untouched) |
| `e2d59f72…` | DATA CORRECTION 3 — the cited measured revision: map refs, audit keys and delta rows regenerated at ONE fresh snapshot (correction 2 had rebound kama's map ref without regenerating the audit ledger; the meter caught it as `audit-missing`) |
| `1eb1eb3f…` | INTEGRATION: SCORECARD round-46 block (the **teardown repair listed explicitly** as the C1 row), SOURCES S155 (registry 154→155), knowledge note `chrome-cdp-teardown-round-46.md` (notes 62→63), README index row, lesson round-46 (Gate + 5 Mistakes), LOG entry, census end + check-sources clean (rows=155, findings=0) + selfassessment candidate reading (finding set identical to the baseline's — nothing introduced) + host-bound check-adjacency receipt + blob-equality receipt |
| `9de5a79b…` | ROUND-CLOSE: hygiene sweep receipt (0 browser processes remain) |

All commits made by the plumbing helper, pushed to origin master (`git ls-remote` ==
`9de5a79b…`). LOG.md entries: round-46 section appended (every change above is tied to it).

## Before → after measurements

- **C1 (operability — the teardown repair, sourced S155)**: at baseline `fe16cf66…` no keyed sweep
  exists in any instrument (`git grep -c Win32_Process fe16cf66… -- scripts` → 0) and
  `git ls-tree fe16cf66… -- corpus/evidence/round46 | wc -l` → 0. After: live red
  `node .ufo/waves/round-46/controls/legacy-teardown-control-r46.mjs --browser edge …` →
  `orphansAfterLegacyTeardown: 16`, `legacyTreeKillExit: 128`, recovery `finalSweepCount: 0`
  (receipt `measure/c1-legacy-edge.json`); mechanism fixture → `survivorsCount: 1` after the no-op
  tree kill, `postKeyedKillSweepCount: 0` (`measure/c1-mech-redgreen.json`); repaired runs → edge
  exit 0 (`midRunSweepCount: 16`, `postKillSweepCount: 0`, PNG 8,229 B sha `4e2c50b4…`), edge
  repro fresh launch-key `edge-profile-a8a4ad8890b4` with byte-identical screenshot, chrome exit 0
  (mid-run 10, sweep 0); counter exit 0 on all three committed byte sets, exit 1 with 8 findings
  on the r45 receipt, `--selftest` verdict=clean 18/18. Measured at `e2d59f72…` (blob equality of
  the counter-scored bytes verified, `measure/c1-committed-bytes-at-cited-rev.txt`).
- **C2 (adjacency)**: `node .ufo/waves/round-46/counters/c1-adjacency-host-v6.mjs --rev fe16cf66…
  --repo <lane> --fleet <fleet>` → exit 1, 28 findings (control
  `controls/c2-meter-red-at-baseline.json`); before-counts from the committed r45 audit at
  `0360b069…`: 9 stale + 1 moved + 6 sibling-absent. After: same command at `e2d59f72…` → exit 0,
  predicate true, 0 findings, `{roster:16, mapRows:16, auditRows:16, deltaLanes:12}`
  (`measure/c2-meter-green-at-measured.json`); `grep -c '^stale'
  corpus/adjacency-host-audit-r46.tsv` → 0; `grep -c '^moved'
  corpus/adjacency-host-audit-r46.tsv` → 0; `--selftest` verdict=clean 16/16.
- **Registry**: `grep -c '^| S[0-9]' corpus/SOURCES.md` 154 → 155. **Knowledge**:
  `ls corpus/knowledge/*.md | wc -l` 62 → 63. **Evidence**: round46 tree 0 → 4.
- **check-selfassessment at the candidate**: exit 1 with five pre-existing m1-selftest-tally
  readings whose set is IDENTICAL at the baseline (`measure/selfassessment-precommit.txt` carries
  both readings) — the round adds no new mismatch; nothing about this round's rows is flagged.

## Sources & frontier

SOURCES.md rows: 154 → 155 (command above). One row opened this round: **S155 — Win32_Process
class** (https://learn.microsoft.com/en-us/windows/win32/cimwin32prov/win32-process; curl raw
fetch, 104,251 B, sha256 `317f30f2…d253`; staged copy committed
`.ufo/waves/round-46/sources/win32-process.html`; located quote, 1 hit in the raw bytes:
"Command line used to start a specific process, if applicable." — the CommandLine property the
keyed sweep matches). Sourced claim: C1 rests on S155. Census: start exit 0 (receipt committed in
the freeze — the r45 carry-in) and end exit 0 (`measure/census-end.txt`, `tabi ok`, the same 21
pre-existing W04 warnings); `node scripts/check-sources.mjs` clean at the integration tip
(rows=155, findings=0, `measure/check-sources-at-integration.txt`).

## Trend verdicts

| Trend | Verdict | Evidence |
|---|---|---|
| expansion | unchanged | No new surface; the round's move repairs an owned instrument and re-pins ledger ground already held (notes 62 → 63 document the repair; registry 154 → 155 adds the enumeration-surface doc); no new capability row — a repair is not an acquisition (QUALITY 84). |
| quality | improved | The r45 carry-in defect closed in committed bytes with live red and green receipts (16 orphans reproduced live, then swept to 0; every repaired run ends at sweep 0, fail-closed); the v6 head-snapshot hardening turned the sibling head race into a caught finding twice; no admitted entry failed a re-check. |
| discernment | improved | The lane's own instruments refused its own outputs four times before admission (counter selftest 1/18 on a broken check; fixture survivors 0 on crashed helpers; two meter runs red on head/audit drift) and every refusal is recorded with its fix; the host-bound legacy gate is recorded with cause instead of silently patched; the red limb of C1 rests on evidence, not luck. |

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources
  `SHONEN.md` box unchanged this round; pointers resolve (`SKILL.md` §Approval table, §Evidence
  ladder, §Runbook, kaika decision rows); prior `[x]` was never non-author (orchestrator ruling)
- [~] At least one end-to-end domain task executed and logged in LOG.md
  `SHONEN.md` box unchanged; `corpus/knowledge/multi-step-journey.md` §1–§2, §7; this round adds a
  new logged end-to-end domain task class (launch→drive→teardown with sweep-to-0) in
  `corpus/evidence/round46/` and the LOG round-46 entry
- [~] Instructions executable by an agent without oral context
  `SHONEN.md` box unchanged; `corpus/knowledge/executor-test-sufficiency.md` §0, §4; this round's
  runner/counter/fixture usage lines are paste-able and were executed verbatim from the freeze
- [~] No cross-domain bleed (PROVINCE.md still accurate)
  `PROVINCE.md` untouched this round and still accurate (host surfaces corrected r44/r45); the
  round's only cross-lane readings are the adjacency ledger's own dispositioned rows — reported,
  not absorbed
