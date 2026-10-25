# Souji round 27 — honest stop

## Work performed

Declared claims: C1 calibration (lowest non-retired axis, score 7), C2 coverage (score 8), C3 operability (score 8). C1 did not verify; therefore this round is not admitted.

- C1: the frozen landing-gate count remained at 2; no exemption was added because the Q57 composite S118 site also carries a stale classification. Receipts: lane `census/round-27/records/c1-before.tsv`, `c1-after.tsv`; base `e78ac7c4837b81b634db4a927605a751a7f006ba`, candidate `6cb22dc20c9fdb3c7a49eaa1accabca339054c17`.
- C2: admitted two GLib 2.84.0 F4 implementation entries, with pinned snapshots, normalized SOURCES rows S152/S210/S211, an 8-row re-opened slice, and a committed 24-ID alias/reject/quarantine map. Entry gates, census, counts and collision proof: `corpus/knowledge/origin-record-*-r27.md`, `corpus/SOURCES.md`, `census/round-27/`.
- C3: added and ran the read-only pre-report gate and four-case fixture; the dirty-tree case fails and the always-pass control is rejected. Code: `tools/souji-pre-report-gate.sh`, `tests/fixtures/r27-pre-report-gate.sh`; receipt `census/round-27/records/c3-after.tsv`.
- Frontier/lesson: `corpus/README.md` maps both new entries on F4; `corpus/lessons/round-27.md` records ADMIT/REJECT decisions, eight slice verdicts, and the R26-M1 dirty-worktree mistake.
- Round shape: one v2 wave, 79 seats. Roles: executor 25, reviewer 12, scout 11, critic 10, scribe 8, mutation-tester 6, connector 3, simplifier 3, revenger 1. Main/L1 held the planner seat. No residual call. Dispatch/results: `souji-shokunin/.ufo/waves/round-27/w1-dispatch.json`, `w1-results.json`; all 79 seats returned final outputs; no dead seat was recorded.
- Attempt 1 ended `lane-dead-no-report`; attempt 2 reused the same frozen claims. `considerthese/` is absent. No tools installed or updated.

## Landed changes

- C2 source entries, rows, snapshots, mapping, README frontier, and C3 gate/fixture/registry landed in lane commit `6cb22dc20c9fdb3c7a49eaa1accabca339054c17`.
- Measurement receipts, Round 27 lesson, SCORECARD and LOG landed in lane commit `c973d1a1c2d8aa1679adc61b2c76634d50e0c1c0` (final pushed lane tip). Scores remain calibration 7, coverage 8, operability 8; no round admission is claimed.

## Before → after measurements

- C1 calibration — `python3 -B tools/souji-landing-gate.py --root . --rev <full40> --round 27 --fleet-root /home/vgpnk/Projects/shokunin`: base `findings=2` (rc 2) → candidate `findings=2` (rc 2), `checked_reg=52`; target 0 failed. No exemption was committed. Receipt paths above.
- C2 coverage — row grep `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`: 132→135; `grep -rlE '^ground: F4' corpus/knowledge/ | wc -l`: 2→4; gate `entries=2 ok=2 slice_verdicts=8 slice_total=8 fail=0`; sources census exit 0 (35 warning-only W04 findings, including one duplicate-URL-across-scopes warning for S210). Measured at `6cb22dc20c9fdb3c7a49eaa1accabca339054c17`; receipt `census/round-27/records/c2-after.tsv`.
- C3 operability — `git cat-file -e e78ac7c4837b81b634db4a927605a751a7f006ba:tools/souji-pre-report-gate.sh` absent at base; at `6cb22dc20c9fdb3c7a49eaa1accabca339054c17`, the gate exists and `bash tests/fixtures/r27-pre-report-gate.sh` → `cases=4 pass=4 control=FALSE-GREEN-REJECTED`, rc 0. Receipt `census/round-27/records/c3-after.tsv`.

## Sources & frontier

`SOURCES.md` rows 132→135; 3 rows added at tier A, status `mined` (S152, S210, S211); no pre-existing row fields changed. New rows are cited by the two admitted F4 entries. The census returned rc 0. Recheck cadence is `365d`. The derived source-register slice contains 8 rows: 7 accepted and S118 unverifiable; full decisions are in `census/round-27/records/slice-verdicts.tsv`. The 24 collisions S109–S132 are mapped in `census/round-27/assimilation/renumber-map.tsv`; the three new IDs are outside that collision set. Assimilation: the F4 origin-record writer/mechanism theme was assimilated from `merge/souji/`; S119 remains rejected pending a decision-time pinned snapshot. F4 now has reference writer/mechanism entries; the normative receipt format and any staging-tool change remain operator decisions. No other frontier row advanced.

## Trend verdicts

- **expansion — improved:** two admitted knowledge entries added on F4 ground, with same-landing coverage-map entries and fresh source rows.
- **quality — improved:** both entries re-grounded against SHA-256 and Git-blob-verified GLib 2.84.0 snapshots; source gate and census passed; C3's tested read-only gate adds a runnable pre-report check.
- **discernment — unchanged:** S119 was rejected for missing decision-time pin, but C1's calibration counter did not reach its target and the round is not admitted.

## SHONEN

[~] SKILL.md decision tables, error patterns, checklists, cited sources — `SKILL.md` gate registry row for `souji-pre-report-gate`.
[~] At least one end-to-end domain task executed and logged — `LOG.md` Round 27 entry; C3 fixture 4/4.
[~] Instructions executable by an agent without oral context — `tests/fixtures/r27-pre-report-gate.sh` and its 4-case output.
[~] No cross-domain bleed — C2 is scoped to F4 implementation references; `PROVINCE.md` unchanged.

Stale-lane: one respawn-per-round driver; no other lane mission is open. No tool installs/updates. Pacman guard respected.

## Conformance residuals

- The lane helper refuses `.ufo/` paths. Thus the required W1 spec/registry/results and 36 inherited r26 W1 leftovers could not be landed through `jj-lane.sh`; they remain under `.ufo/waves/round-{26,27}/`. R26 leftovers were catalogued in `w1/ExecInheritedResolve.md` and left untouched rather than bypassing the helper or deleting another author's files.
- The final lane is pushed at `c973d1a1c2d8aa1679adc61b2c76634d50e0c1c0`. The pre-report gate's remote, report, SHONEN and prereg checks pass, but the clean-worktree check fails on those inherited `.ufo` artifacts and other pre-existing lane leftovers. No unrelated worktree files were changed or removed.
- No admission: the frozen C1 target failed. C2 and C3 pass their counters, but the round's all-claims admission rule is unmet.
