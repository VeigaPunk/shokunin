# kengaku — round 81 report (hyaku run 15, attempt 1)

Lane `kengaku-shokunin`, round 81, 2026-11-04. Base `4e833e9f` (round-80 verifier spot-check);
freeze `4d896e0d`; **final lane tip `ae03c4f6`** (pushed; `git ls-remote origin refs/heads/master`
prints it). Report filed after the wave's `WAVE-DONE` handoff (`w1-results.json`).

**Round shape:** one v1 wave, 14 seats — executor 6, scribe 2, reviewer 1, critic 1,
mutation-tester 1, sentinel 1, connector 1, scout 1 (attack roles 4/14 = 29 %, one connector; the
§3 L2 floor is met inside the wave). No residual call. Round total: 14 seats.

**Seat tally (from `w1-results.json` and the wave dir).** 10 seats filed a report
(`ScoutHostR81`, `EnvPinR81`, `ConnectorR81`, `ReviewerC1R81`, `SentinelReceiptsR81`,
`U4RedBeforeR81`, `SourcesScribeR81`, `ProbeVulnSecretR81`, `CriticClaimsR81`, `C2ChecksR81`);
`ProbeLogSummaryR81` delivered its instrument (`w1/ProbeLogSummaryR81.py`) with no report file;
`U1AnchorR81` delivered its measurements in its seat output (stamp block `2-12` in all six
receipts, `OBSERVATIONS_BEGIN` at 13/14) with no report file. **Two seats died with empty final
output: `LessonScribeR81` and `MutationGateR81`** — no report, no deliverable, no error text in
`w1-results.json`. Their assigned work was covered elsewhere (the L1 wrote the lesson; the gates'
own mutant batteries killed 10/10 and 4/4 and the reviewer/critic inspected the gates), but the
round has **no independent mutation pass by a mutation-tester seat** and says so here.

## Work performed

The round declares two claims on two distinct axes, frozen before data in
`plans/round-81-claims.md` (`4d896e0d`):

- **R81-C1 — coverage** (lowest non-retired axis, held at its L0 cap): two population members that
  were `unattempted` — `log-summary-date-ranges` and `vulnerable-secret` — become `executed` with
  located, reproducible receipts whose stamp pins the captured grader bytes, the instrument, and the
  replay environment (`HOST_PYTHON`, `HOST_OPENSSL`).
- **R81-C2 — calibration** (held at ceiling 10, exercised): the round-80 verifier spot-check's six
  routed defects `U1`…`U6` are discharged as `R80-U1`…`R80-U6` rows whose checks fail at the base
  revision.

Work items, each with its evidence pointer:

- The frozen selection rule derives the universe rather than listing it: eleven `unattempted`
  stdlib-only file-artifact/serialization-schema candidates, maximum captured-grader assert count 5,
  carried by exactly two members (`plans/round81_c1_new_members.py`, printed as `CANDIDATES n=11 …`
  on every run; `corpus/evidence/round81/c1-before.txt`; the reviewer re-derived the same set with
  its own script, `ReviewerC1R81.md` §1).
- Two new offline instruments replay the round-52 captures in bubblewrap sandboxes, 12 frozen cases
  each (4 predicted pass, 8 predicted fail), predictions derived from declared `violates=` tags:
  `plans/round81_log_summary_probe.py` and `plans/round81_vulnerable_secret_probe.py`. Both are
  deterministic across consecutive runs (`corpus/evidence/round81/determinism.txt`); the wave's two
  executors delivered independent implementations of the same instruments
  (`w1/ProbeLogSummaryR81.py`, `w1/ProbeVulnSecretR81.py`, the latter `cases=10 mismatches=0`).
- The mint driver ran every probe first, re-checked worktree cleanliness before writing, and stamped
  `LANE_TIP`, `HOST_PYTHON`, `HOST_OPENSSL`, `MINTED_BY_SHA` (`plans/round81_c1_remint.py`;
  receipts `corpus/evidence/round81/log-summary-date-ranges-probe.txt`,
  `vulnerable-secret-probe.txt`). The sentinel independently recomputed every stamp digest and
  replayed both instruments (14/14 observation lines equal, `SentinelReceiptsR81.md` §4).
- The ledger rows for both members flipped `unexecuted` → `executed` with `subject=tb2-header`,
  `verdict=predicate`, `round=81`; the round-79 population gate now prints `executed=26 unlocated=0`
  (`plans/grader-population-ledger.json`; independent census in
  `corpus/evidence/round81/ledger-census.txt` — `executed=26 of 88`, `file-artifact` 18 of 76).
- The file-artifact class cell in `SKILL.md` was re-derived from that ledger (16 → 18 of 76), which
  is what the population gate reads (`PREDICATE R79-C1 pass` at the final tip). The reviewer's
  finding F1 (the cell still reading 16 at `2fe3d8e6`, so the gate exited 1 there) is exactly this
  repair, landed at `ad37cf36`; the reviewer's snapshot predates it and says so.
- Six repair checks with a self-test that drops each repair's evidence in turn:
  `plans/round81_c2_checks.py --all` → `OK u1 … OK u6`; battery
  `SELFTEST cases=12 red=6 failures=0` (`corpus/evidence/round81/c2-checks-selftest.txt`). The
  wave's `C2ChecksR81.py` re-derives the same six contracts independently and prints `OK u1 … u6`.
- R80-U1: `corpus/SOURCES.md` gains S259, a superseding row opening `supersedes S258 —` with the six
  committed round-80 receipt sha256s and both stamp framings (the gate's REQUIRED block `2-12`,
  the spot-check's `3-12`); the superseded text (`7923b6dc…`, `lines 1-10`) is named in
  `corpus/lessons/round-81.md`.
- R80-U2: `SCORECARD.md`'s round-80 section carries a dated erratum naming `gates-clean.txt` at
  `e985e56a` as R80-C1's comparable measurement and `c1-after.txt` as the `WORKTREE dirty` run.
- R80-U3: `corpus/evidence/round81/census-rows.txt` records the frozen row-count command and its
  values — 249 at `dce7c275`, 250 at `507d249b`, 253 at the round-81 tip after three appends.
- R80-U4: `corpus/evidence/round81/r80-u4-red-before.txt` is the prefix-removed protein run
  (`exit code: 1`, `ModuleNotFoundError: No module named 'Bio'` at `tb2_grader_probe.py:145`), and
  `corpus/QUALITY.md` Q58 requires such a witness. The wave's `U4RedBeforeR81` reproduced it and
  additionally showed the round-80 gate printing `DEFECT REPRODUCTION-EXIT protein-assembly rc=1`.
- R80-U5: `SKILL.md`'s gate/probe registry gains rows for the two round-80 gates, the two round-81
  gates and the repair-check battery, with entry commands, verdict families, self-test spellings and
  write scopes.
- R80-U6: the lesson cites the six committed round-80 receipts instead of the quoted driver line, and
  the `corpus/README.md` lesson row names `M80-1/M80-2`.
- Frontier: `corpus/knowledge/tb2-file-artifact-replay-classes.md` (the two captures, the case
  tables, the environment pin), indexed in `corpus/README.md`; SOURCES rows S259/S260/S261 opened
  this round; `PROVINCE.md`'s declared registry count was stale at 249 and now reads 253 with the
  producing command; `considerthese/2026-10-26.md` proposal 3 is mined as `QUALITY.md` Q59 (a batch
  sweep is a freshness instrument with a flake-rate rider, never a coverage claim).
- Wave recon: `ScoutHostR81` re-probed every declared surface and fetched the pinned TB2 task
  documents (the `tasks/<member>/task.yaml` spine 404s — metadata is `task.toml` at top-level member
  directories); `ConnectorR81` ruled no sibling owns the host pin, the routed-findings shape or a
  TB2 grader replay; `EnvPinR81` showed the eigen probe's two `predicted=U` speed cases are still
  the only varying lines across six runs (projection invariant).
- Wave findings and their disposition: `corpus/evidence/round81/w1-findings.txt` — F1 discharged
  in-round; F2 (`COMMAND` substring), F3 (universe reads captures from the checked tree), F4
  (vacuous stdlib test), S1/S2 (mint guard OR, non-atomic writes) and the critic's four limits are
  named and routed to round 82, never laundered.

## Landed changes

Every change lands in the lane through `jj-lane.sh`; the substance is logged in `LOG.md`
§Round 81 (`LOG.md:3123`).

| commit | what it carries |
|---|---|
| `4d896e0d` | freeze: claims, two counters, probe table, before/selftest/mutant/control receipts |
| `ca9bfe79` | wave w1 spec, validator dispatch, swarm registry |
| `4ac8471b` | the two probe instruments, the repair-check battery, first repairs (U2/U3/U4/U5), index rows, PROVINCE count |
| `2fe3d8e6` | the two located receipts and the flipped ledger rows |
| `ad37cf36` | the derived `file-artifact` class cell (16 → 18 of 76) and wave evidence |
| `51b824c6` | lesson, knowledge entry, SOURCES S259–S261, routed-findings `R80-U1`…`U6`, index rows, C1 after receipt |
| `544dc98a` | SCORECARD round-81 section and the LOG entry |
| `6781dd00` | census before/after and the C2 after receipt |
| `94d54e0d` | declared registry count follows the three appended rows |
| `7a243564` | `QUALITY.md` Q59 mined from `considerthese/2026-10-26.md` |
| `604be350` | receipt stamper and the honest execution limit in the lesson |
| `f70fe5fa` | both after receipts re-minted with `LANE_TIP`/`WORKTREE`/`COMMAND`/`EXIT` in a clean clone |
| `f6d5b864` | real-tree control (ledger rows reverted → target fails) and the scratch-clone process slip |
| `4fe5ebea` | determinism and independent ledger-census receipts |
| `e7bc380f` | census receipt carries the post-append count (253) |
| `805a65c8` | every gate green at `e7bc380f` in a clean clone |
| `a54753e9` | the repair-check battery receipt |
| `60123c7f` | wave evidence: connector sibling scan, environment pin, host-state deliverable |
| `9b89275a` | wave findings and dispositions, lesson limits, round-82 plan |
| `92988480` | wave evidence: reviewer and sentinel reports, the first probe deliverable, the U4 red-before copy |
| `8a47722c` | findings note gains the build-seat corroborations |
| `8eb887a3` | wave deliverable: the second probe (independent implementation) |
| `e83963f8` | gates-clean block refreshed |
| `14e49f82` | independent C2-check deliverable and its corroboration note |
| `7ca49477` | S259 states both stamp framings; the sources seat's report |
| `03affddf` | findings note records the stamp-framing reconciliation |
| `0ed95bf1` | the vulnerable-secret probe seat's report |
| `70707d9d` | wave settled: critic and C2-check reports, `w1-results.json`, findings note |
| `39bbe9a4` | the probe deliverable at the seat's final revision (`sha256 aedcc297…`) |
| `ae03c4f6` | final gates block (all green at `39bbe9a4`) |

## Before → after measurements

**R81-C1 / coverage.** Counting command
`python3 plans/round81_c1_new_members.py --lane .` (and `--rev 4e833e9f` for the before):

- before (`corpus/evidence/round81/c1-before.txt`, measured against `4e833e9f`):
  `TARGET members=2 located=0 reproduced=0 ledger_flipped=0 defects=2`, `DEFECTS n=2`
  (`RECEIPT-UNTRACKED` ×2), `PREDICATE R81-C1 fail`, exit 1.
- after (`corpus/evidence/round81/c1-after.txt`, `LANE_TIP 604be350`, measured in a clean clone):
  `TARGET members=2 located=2 reproduced=2 ledger_flipped=2 defects=0`,
  `LEDGER-GATE rc=0 LEDGER rows=88 executed=26 unlocated=0 unexecuted=62`, `PREDICATE R81-C1 pass`,
  exit 0.

**R81-C2 / calibration.** Counting command
`python3 plans/round81_c2_spotcheck_debt.py --lane .` (and `--rev 4e833e9f` for the before):

- before (`corpus/evidence/round81/c2-before.txt`): six `DEBT-UNREGISTERED`,
  `INDEX corpus/lessons/round-80-verifier-spotcheck.md indexed=no`, `DEFECTS n=7`,
  `PREDICATE R81-C2 fail`, exit 1.
- after (`corpus/evidence/round81/c2-after.txt`, `LANE_TIP 604be350`): `TARGET ids=6 closed=6
  checks_passed=6 indexed=yes`, `DEFECTS n=0`, `PREDICATE R81-C2 pass`, exit 0; the mechanical
  sensitivity leg (each row's evidence reverted to `4e833e9f`) reports no
  `CHECK-NOT-REPAIR-SENSITIVE`.

**Controls (all lose, and would fail the claim if they did not).**
`c1-control-flip-ledger-only.txt` (`RECEIPT-UNTRACKED`, `target_reached=False`),
`c1-control-header-only.txt` (50 defects, thirteen codes, `target_reached=False`),
`c1-control-copy-observations.txt` (`REPRODUCTION-MISMATCH`, `target_reached=False`),
`c1-control-ledger-reverted.txt` (real tree, both rows reverted: `ledger_flipped=0 defects=3`,
exit 1), `c2-control-presence.txt` (`CHECK-TRIVIAL`, `CLOSE-NOT-REPAIR`, `SOURCE-LINE`,
`INDEX-MISSING`, `target_reached=False`). Batteries: `c1-selftest.txt` (`cases=11 red=10
failures=0`), `c1-mutants.txt` (`real=10 killed=10 survived=0`), `c2-selftest.txt` (9/8/0),
`c2-mutants.txt` (4/4/0), `c2-checks-selftest.txt` (12 cases, 6 drops, 0 failures).

**All gates at one tip** (`corpus/evidence/round81/gates-clean.txt`, fresh `--shared` clone at
`39bbe9a4`, `WORKTREE clean`): `grader.py` `CHECKS n=733 mismatches=0` / `VERDICT: PASS`; R79-C1
`replayed=26 located=26 unlocated=0 unexecuted=62`, pass; R75-C1 index parity 75/135/72 indexed,
pass; R77-C1 `total=28 unlisted=0 agree=28 disagree=0`, pass; R81-C1 pass; R81-C2 pass; the six
repair checks `OK`; `routed_open` `ROWS total=117 open=31 blocked=1 closed=83 refused=2`. Every
block `EXIT 0`.

## Sources & frontier

Census command (the round contract's): `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh
validate --root /home/vgpnk/Projects/shokunin kengaku` → exit 0 **before** and **after**
(`corpus/evidence/round81/census-before.txt`, `census-after.txt`; 28-line receipts, 26 `W04`
warnings each, no `E..` finding). Registry rows: **250 → 253** by the frozen count
(`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`; `census-rows.txt` records
249 at `dce7c275`, 250 at `507d249b`, 253 at the tip).

- **Rows added:** 3, all tier A — S259 (own-work, supersedes S258), S260 (own-work: the round-81
  instrument set and the two receipts), S261 (docs: the pinned TB2 task documents at `2fd12b88`,
  fetched 2026-11-04T08:26:13Z, HTTP 200; the executing seat re-fetched the same tree independently
  and reports matching digests).
- **Rows touched old→new:** S258 → S259 (the S258 anchor's six pre-amendment digests and its
  `lines 1-10` range are superseded; S258's bytes are not edited). No other status/recheck/used-by
  change.
- **Frontier rows advanced:** `log-summary-date-ranges` and `vulnerable-secret` move
  `unattempted → executed` (the record is `plans/grader-population-ledger.json` plus the independent
  census `corpus/evidence/round81/ledger-census.txt`), and the `file-artifact` class row moves
  `16 of 76 → 18 of 76`.
- **Rejected source this round:** the `tasks/<member>/task.yaml` spine — fetched, 404, and the
  pinned tree's own recursive listing shows 0 `task.yaml` of 1446 entries (a wrong-locator class,
  not a source).
- **Assimilation:** none — `merge/kengaku/` id drift is still open at L0 (`kengaku | round-54`);
  nothing from the package is adopted this round.
- **considerthese:** `considerthese/2026-10-26.md` (2026-10-26) proposal 3 is mined as
  `QUALITY.md` Q59.

## Trend verdicts

- **expansion: improved.** Two population members move `unattempted → executed` (24 → 26 of 88
  members), the `file-artifact` class cell moves 16 → 18 of 76, three sourced rows land (S259–S261),
  a knowledge entry enters the index, and a capability enters `SCORECARD.md` with a demonstrated
  command (`host-pinned-first-receipt`). Evidence: `ledger-census.txt`, `c1-after.txt`,
  `SCORECARD.md` §Round-81 capabilities.
- **quality: improved.** The replay predicate gained the environment pin round 80's plan asked for,
  the mint driver refuses a dirty worktree before and after the probes, the repair checks carry a
  self-test that drops each repair's evidence in turn, and two new gates land with
  selftest/mutant/control batteries (10/10 and 4/4 mutants killed). A real-tree control shows the
  claim is not reachable by receipts alone (`c1-control-ledger-reverted.txt`), and independent
  implementations corroborate both the instruments and the six repair contracts.
- **discernment: improved.** Six outside findings (R80-U1…U6) are closed with checks that fail at
  base rather than restated; the stale PROVINCE count (249 vs the measured 250, now 253) was found
  by the round's own gate and corrected; the reviewer's F1 is discharged with its commit order; and
  the round names what it cannot close — the `COMMAND`/tool-provenance trust boundary, the universe's
  capture-vs-base read, the env pin's string granularity, the mint guard's OR and non-atomic writes,
  the C2 commit-ancestry branch — plus two seats that died with empty output
  (`corpus/evidence/round81/w1-findings.txt`).

## SHONEN

- `[~]` SKILL.md contains real decision tables, error patterns, checklists, cited sources —
  `SKILL.md` (the grader-class table's `file-artifact` cell re-derived 18 of 76; registry rows added
  for the round-80 and round-81 gates).
- `[~]` At least one end-to-end domain task executed and logged in LOG.md — `LOG.md:3123`
  §Round 81 (two graders replayed offline, six repairs discharged).
- `[~]` Instructions executable by an agent without oral context — `plans/round81_c1_new_members.py`
  and `plans/round81_c2_spotcheck_debt.py` carry their usage, selection rule and verdict map in
  their docstrings, and both run from a clean clone with no L1 context (`gates-clean.txt`).
- `[~]` No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` (registry count corrected;
  no surface absorbed; `ConnectorR81.md` rules every sibling overlap adjacent-but-different).

## Extras

- **Stale-lane:** none — respawn-per-round driver; no other mission of this lane is open.
- **Tool installs:** none (pacman paused host-wide; no channel needed). The wave's seats report no
  installs either.
- **Open L0:** `kengaku | round-54` (assimilation id drift) and `kengaku | round-80` (whether
  pre-landing amendments are acceptable) stay open; this round routes around both — no assimilation,
  and the round-81 predicate is a successor, never an amendment of round 80's.
