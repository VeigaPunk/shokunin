# souji — Round 26 report

## Work performed

Declared claims: C1 — calibration (7, lowest non-retired), integrate the r24 SCORECARD generation-scaffold payloads (markers 2→0, newest-first heading order, R3 dated note, capability rows); C2 — coverage (8), assimilate the F1 auto-maintenance trigger-set theme (two grounded entries, registry rows S128–S132); C3 — operability (8), the preregistration axis-of-surface checker instrument + 12-case falsification fixture (routed from R25-M1). All three verified; the round is admitted with trend verdicts below.

- C1: `SCORECARD.md` base 254 lines measured `markers=2` and headings `17 175 231` (r23, r24-fenced, r25-last, violating the file's own newest-first contract). Landed integration at `07f83e6`: `markers=0`, headings `17 44 78` (r25 < r24 < r23); byte-diff of all seven amendment-2 protected spans re-verified (search-based contiguous-block check). Wave seat ExecC1Surgery proved the first landing omitted the two r24 capability rows; appended (this round's own bug caught by its wave) and the `c1-after.tsv` receipt regenerated at the fix tip. Append-only corrections section (five superseded-by line targets mapped across r25 base/pre-cleanup/post-C1 layouts) added per wave scribe draft at the EOF.
- C2: entries `git-auto-maintenance-trigger-set.md` and `-r23.md` admitted with `ground: F1`; rows S128–S132 appended (S128 fetch manual OPTIONS switch, S129 five v2.56.0 `run_auto_maintenance` call sites, S130 `builtin/pull.c` child-spawn, S131 campaign fixture own-work re-grounded by sha256, S132 fleet worktree census). Both entries carry `## Gate` sections (opened/ADMIT/REJECT with reason, located ≤25-word snapshot quotes from `census/round-26/sources/`). K2 gate: `entries=2 ok=2 fail=0`; K4 coverage agreement base `grounded=7` → tip `grounded=9 mapped=9 dangling=0 mismatches=0 kill_tested=7 kill_violations=0`; real registry gate rc 0. The staged S-language edition corroboration (zh/ja docs, vendor page) was refused (edition alignment unprovable; vendor page cites a 2.16.x-era workflow) — recorded in the round lesson Gate. `considerthese/` is absent in this lane (one report line).
- C3: `tools/souji-axis-check.py` (R1 owned-axis, R2 surface-class consistency, R3 lowest-axis presence, R4 universal-clause scan) + `tests/fixtures/r26-axis-check.py` 12-case fixture (case 1 = r25-C2 replica discriminator; case 12 = integrated always-green stub control). K1 at base: tool absent; at tip self-hosted `claims=3 flags=0` rc 0; K2 `cases=12 pass=12 control=FALSE-GREEN-REJECTED` rc 0. Wave ExecAxisFixture delivered the frozen 12-case set; the L1 adopted it and corrected its own first 11-case fixture and the R4 scan (raw claim text; flag only when `enumerate:` absent AND a universal word is present). All receipts `verify=ok`.
- C1 counter blind spot (wave RevC1Counter, disclosed): K1 counts only two marker prefixes and K2 prints an unlabeled ascending triple, so neither alone proves scaffold removal or order; the byte-diff span check is the margin, and Heading mapping r25@17/r24@44/r23@78 is recorded. This is calibration debt carried to r27 (a counter extension).
- No tools were installed or updated. No L0 question was filed.
- **Round shape / swarm:** w1 spec 87 seats (role mix per `w1-spec.json`). The wave was queued behind the operator's 100-job cap (kasegi + kengaku waves held it) and spawned as slots freed; seats are still running at report time, with 16+ seat reports landed in `.ufo/waves/round-26/w1/` (ExecAxisTool, ExecAxisFixture, ExecC1Verify, ExecC1Surgery, ScribeSourceRows, MutC2Rows, LabGateCheck, RevC1Counter, RevPreregFreeze, ScribeEntryB, etc.). Assimilated findings: C1 capability-row omission (fixed), C2 Gate requirement (fixed), C3 12-case set (adopted), K2 blind spot (disclosed), staged-row id collisions/mirror gate (pre-empted by the scratch-mirror gate run before the real append).

## Landed changes

| lane commit | landed change |
|---|---|
| `965b869` | prereg amendment 2 (C1 kill rule clarified to byte-content spans) |
| `a529c76` | C1 integration (r24 payloads, newest-first, R3 note) — later corrected by `07f83e6` |
| `4453128` | C1 green receipt at first landing tip |
| `0833de9` | C3 tool + 11-case fixture; C2 sources snapshots + entries + registry rows (first pass) |
| `d2e6253` | C3 counter `--stub` arm (later replaced by integrated case 12) |
| `e0f8dcd` | C3 receipts (first pass) |
| `d6c13b0` | C2 before/after counter receipts |
| `d6fe8a1` | C1 append-only corrections section |
| `07f83e6` | C1 fix: append the two r24 capability rows; c1-after regenerated at `07f83e6` |
| `ba8b54b` | c1-after receipt commit |
| `c5949013` | C3 R4 fix + adopted 12-case fixture + counter fixture arm |
| `0c92c2e` | C3 receipts (absent@base; claims=3 flags=0; 12/12 FALSE-GREEN-REJECTED) |
| `33e6807` | C2 Gate sections on both entries |
| `9a6e0f1` | C2 receipts: c2-gate (ok=2), c2-k4-base/after (7→9 grounded) |
| `166baa1` | measurements block + planned bullet, lessons (Gate/findings/residuals/mistakes R26-M1), QUALITY Q59, wave w1 seat record |

Lane branch `master` pushed at `166baa18f808071bc385187691713044a26bd663`; `ls-remote` checked below. This fleet report is the final commit and is pushed separately.

## Before → after measurements

| claim | axis | before → after | counting command | measured commit |
|---|---|---|---|---|
| C1 | calibration (7) | `markers=2`, headings `17 175 231` → `markers=0`, headings `17 44 78`; seven protected spans byte-equal | `bash census/round-26/c1-counter.sh`, receipt `c1-after.tsv` | `07f83e6` |
| C2 | coverage (8) | `grounded_f1=0`, registry rows 127 → `grounded_f1=2`, rows 132; gate `entries=2 ok=2 fail=0`; K4 `grounded=7` → `9 mapped=9 kill_violations=0`; registry gate rc 0 | `bash census/round-26/c2-counter.sh`; `souji-gate-check.py`; `souji-coverage-agreement.py` | `9a6e0f1` |
| C3 | operability (8) | tool absent at base → claims-hosted `claims=3 flags=0` rc 0; fixture `cases=12 pass=12 control=FALSE-GREEN-REJECTED` rc 0 | `bash census/round-26/c3-counter.sh`; receipts `c3-before/after.tsv` | `0c92c2e` |

No 0–10 score mapping exists, and no numeric score changed.

## Sources & frontier

`scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin souji` — exit 0 (W04 warning-only unchanged class). Rows 127 → 132. Tier A=120/B=5/C=2 → A=122/B=5/C=2 plus two own-work A rows (S131/S132). Status mined 103/queued 15/rejected 9 → mined 107/queued 15/rejected 9. No prior status/recheck/used-by cells changed. F1 frontier advances from call-sites-only to measured trigger set; F2 stays frontier. Rejected staged S-language rows keep their reason/flip in the lesson Gate. Assimilation: two entries, five rows.

## Trend verdicts

- **expansion — improved (bounded).** The F1 trigger set and measured prune are new grounded ground; the fleet census re-derived (5 registrations, 0 prunable, 0 locked). Bound: `gc.worktreePruneExpire`/maintenance strategy scope remains unmeasured.
- **quality — improved (bounded).** Both entries are source-pinned (snapshots + SHA256SUMS) and gate-checked; S131/S132 are own-work re-verified by sha256. The C1 counter blind spot is disclosed and carried; no pre-existing admitted entry was found false.
- **discernment — improved (bounded).** C3 makes the axis-of-surface check mechanical (Q59), with the r25-C2 replica as discriminator; the always-green stub control is rejected. Q58's discipline was honored (amendment 2 pre-data; receipts at base revs).

The round is admitted: three claims verified on their declared axes, with disclosed debt carried (C1 counter blind spot, gate locator limits, S-language edition gap).

## SHONEN

[~] SKILL.md decision tables, error patterns and checklist — `SKILL.md`, `corpus/QUALITY.md` (Q59 added), round-26 fixtures. No non-author verifier checked this round.
[~] End-to-end domain task executed and logged — `LOG.md`-equivalent round records (lesson file receipts), candidate receipts verified (`verify=ok`); no cleanup/deletion action or operator handoff was performed.
[~] Instructions executable without oral context — `tools/souji-axis-check.py` + 12-case fixture are runnable; command sequences in the Frozen counter/measurement table are exact; limits remain explicit.
[~] No cross-domain bleed — no sibling source trees modified; `considerthese/` absent; read-only campaign sources opened under `census/round-26/sources/` only.

Stale-lane: mission progressing (lane commits and round artifacts landed; wave seats still running behind the job cap). Open L0 questions: none. Tool installs/updates: none.

## Wave completion addendum (WAVE-DONE)

W1 completed after report time: 87/87 seat results at `.ufo/waves/round-26/w1-results.json` (35 PASS, 14 PARTIAL, 5 FAIL, remainder informational). All FAIL/PARTIAL reviews targeted intermediate commits; the two substantive items were assimilated: (1) CritEntryB falsified Entry B's four-command claim (pull case runs `git fetch`; merge/rebase cases confounded by a plain `git commit`; merge is a fast-forward). Entry B was narrowed to the isolated fetch arm, the confounded rows are disclosed, `verified-at:` marks the campaign as measurer, and S131's teaches cell + lesson ownership phrase were corrected — K2 gate re-run green (`entries=2 ok=2 fail=0`) at `50443f5`, receipt `c2-gate.tsv` regenerated at `27065272`; (2) RevAssimRules/CritSourcedClaim/CritCoverageCredit reported red K2 + missing receipts at pre-Gate commits (`0833de9`/`9a6e0f1`); final tip carries Gate sections and all receipts (`33e6807`/`9a6e0f1`), all `verify=ok`. Mirror-gate evidence now committed at `.ufo/waves/round-26/assimilation/validate/` (sources-census `--file` rc 0). Lane final tip `27065272d12572dbc6a464ea938fbd59ad88275` (pushed).
