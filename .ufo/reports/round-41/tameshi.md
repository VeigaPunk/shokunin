# tameshi — round 41

lane: tameshi-shokunin · round: 41 · attempt 2 · date: 2026-10-25
lane tip: `b8e39564b0a83817d99d341de12112de454fc32a` · measured commit:
`2ae00eb750b86eba6c9b54b36b1a6e875e9fd8a6`; both counters are green at the tip as well
(receipts produced at `b14ff110`: `.ufo/evidence/round-41/after/c1-at-b14ff110.stdout` and
`…/c2-at-b14ff110.stdout`; re-run at the tip, both exit 0)
base: `a3d6c690bcbf8914551d4f4e8e1612784c1c2046` · freeze: `d4ee4e63a0a4402bd8628fbc80f06bbd8f37d937`

## Work performed

Two claims, distinct axes. Calibration (measured 6) is the lane's lowest non-retired axis and
carries C1; the stagnation nudge does not fire because round 40 added a capability inside the
window N=2.

- **C1 — calibration (axis move on the lowest axis).** The lane's self-assessment records must agree
  with observed repo state across four declared classes: m6 the standing `sources-registry` count,
  m7 cited S-ids the registry does not hold as mined, m8 cited repo paths that do not resolve at the
  measured revision, m9 the round-40 quarantine-summary contradiction. Evidence: the counter
  `.ufo/evidence/round-41/calibration/measure.py`, the base receipt
  `.ufo/evidence/round-41/before/c1-at-base.stdout` (`m6=1 m9=1 total=2`, exit 1) and the deciding
  receipt `.ufo/evidence/round-41/after/c1-at-baa18b7b.stdout` (`total=0`, exit 0).
- **C2 — depth, capability acquisition.** `tools/write-path-census-v3.py` resolves a write
  destination held in a variable through up to four assignment/`os.path.join`/`+`/`/`/f-string hops
  and classifies it as expected-value, scratch or update-flagged. Evidence: the tool at
  `095924a7a165be96e69ff9dad67d3e513d23ba6737c35a0537f898482eef0279`, fixtures
  `.ufo/evidence/round-41/census/fixtures.json`, counter `.ufo/evidence/round-41/census/measure.py`,
  deciding receipt `.ufo/evidence/round-41/after/c2-at-baa18b7b.stdout`.
- The two live sites the capability resolves are `tools/repeat-control.py:811` (a variable
  destination that v2 records as a write site with no expected-value destination) and `:820`
  (`os.symlink`, which v2 does not see at all). Both are scratch fixtures, so the round claims
  visibility of the destination, not a new open write path.
- Records repaired for C1: the standing `sources-registry` row restated to the registry's real count
  (`SCORECARD.md`), and the round-40 quarantine-summary correction appended to
  `corpus/lessons/round-41.md` — the round-40 file itself is untouched.
- Frontier: S153 (`ast`) and S154 (`Path.write_text`) opened 2026-10-25, each pinned to a committed
  snapshot under `.ufo/evidence/round-41/sources/`; one knowledge entry admitted
  (`corpus/knowledge/r41-variable-destination-writes.md`) with a `corpus/README.md` coverage row and
  `corpus/QUALITY.md` criterion 80.
- Wave 1: one v1 wave, 40 seats, dispatched as exactly one batched `task` call from the validator's
  `taskCall` (`.ufo/waves/round-41/dispatch-w1.json`). Role mix: connector 1, scout 6, executor 8,
  scribe 7, reviewer 10, critic 5, mutation-tester 3; attack roles 18/40 = 45 %. Dead seats: 0 — all
  40 reports are present and non-empty (`.ufo/waves/round-41/w1/`, registry
  `.ufo/waves/round-41/w1/swarm-registry.json`). The L1 holds the canonical planner seat (the
  validator rejects `planner`); the bounded planning data walk rode the connector and scout items.
- Residual call: one ordinary `task` call of 8 reviewer/critic seats attacking the final state (no
  wave 2 — wave 1's output yielded 8 further distinct attack items, fewer than the 32 a wave 2
  requires). Round total 48 seats, inside the 32–128 band; the 8 are enumerated in
  `.ufo/waves/round-41/residual/spec.json` with `.ufo/waves/round-41/residual/receipt.json` for
  report presence.
- Attempt inheritance: attempt 1 ended `lane-dead-no-report tameshi round=41` (watchdog,
  2026-10-25T03:23:08-03:00). Nothing was inherited: `git -C tameshi-shokunin status --porcelain`
  was empty and `.ufo/waves/round-41/` did not exist at attempt-2 start. No file was discarded.

## Landed changes

| change | LOG.md entry | commit |
|---|---|---|
| freeze: contract, v3 tool, fixtures, both counters | round-41 entry, first bullet set | `d4ee4e63a0a4402bd8628fbc80f06bbd8f37d937` |
| C1 records reconciliation, C2 census v3, S153/S154 rows, knowledge entry, lesson, QUALITY 80, README row, amendments A1–A4 | `LOG.md` `## 2026-10-25 — round 41` | `b37ce974b6efb8c465626d7346149549a3300a4b` |
| wave-1 evidence (40 seat reports), settlement receipt, record corrections, A2/A5 rule declarations | same entry, wave and corrections bullets | `baa18b7bdd637ff175255e82b6bee3c85df0881e` |
| deciding-run receipts and the after sections | same entry, deciding-runs bullet | `2ae00eb750b86eba6c9b54b36b1a6e875e9fd8a6` |
| confirmation receipts at the measured commit, round-end census | same entry | `0c8e1bebaac3c09b916127de5413440429663506` |
| late seat report, census end exit code | same entry | `812ee0d11d267e131be3dc8db0b71253cbae9234` |

Pre-data amendments, all in the contract with `before_data: true`: A1 the m7 status column index
(9 → 8; without it every cited S-id would fail m7), A2 the symlink fixture root plus a third
recognizer mutant, A3 a record rephrasing for a staged-set range endpoint, A4 directory-path
resolution in m8, A5 m9's correction words derived from the round-40 table instead of two hardcoded
strings. A2 and A5 are declared `rule_changed: true` — both stricter, neither relaxing a target, the
predicate's scope or the kill rule. No default-mode run preceded them.

## Before → after measurements

Counting commands, run from the lane repo (`LANE=/home/vgpnk/Projects/shokunin/tameshi-shokunin`):

```
python3 .ufo/evidence/round-41/calibration/measure.py --lane LANE --rev REV
python3 .ufo/evidence/round-41/census/measure.py --lane LANE --rev REV
```

**C1 calibration.** Before, at the base `a3d6c690bcbf8914551d4f4e8e1612784c1c2046`:

```
MISMATCH m6 SCORECARD standing row says 103 rows, SOURCES.md has 107
MISMATCH m9 round-40 quarantine summary says (1, 7, 9), its table counts (1, 6, 10) (no round-41 correction)
C1_R41: m6=1 m7=0 m8=0 m9=1 total=2 records=0 sources_rows=107 rev=a3d6c690bcbf8914551d4f4e8e1612784c1c2046 C1_R41_PASS=false
```

exit 1. After, at `2ae00eb750b86eba6c9b54b36b1a6e875e9fd8a6`:

```
C1_R41: m6=0 m7=0 m8=0 m9=0 total=0 records=3 sources_rows=109 rev=2ae00eb750b86eba6c9b54b36b1a6e875e9fd8a6 C1_R41_PASS=true
```

exit 0. Delta: two live mismatches → zero, and the two record-audit classes (m7, m8) measured at
zero on this round's three records. Do-nothing control: the base run itself — m6 and m9 survive any
edit that does not touch them, so no do-nothing path reaches `total=0`.

**C2 depth.** Before, at the base:

```
C2_R41: tool_absent=1 var_expected=0 symlink_expected=0 rev=a3d6c690bcbf8914551d4f4e8e1612784c1c2046 C2_R41_PASS=false
```

exit 1. Negative control, `--control` on the same fixtures:

```
C2_R41_CONTROL: v2_var_expected=0 v2_symlink_sites=0 C2_R41_CONTROL_PASS=false
```

exit 1 (the declared control value). After, at `2ae00eb750b86eba6c9b54b36b1a6e875e9fd8a6`:

```
C2_R41: tool_absent=0 tool_sha_ok=1 v2_sha_ok=1 selftest_exit=0 var_unflagged=1 var_expected=1 symlink_unflagged=1 symlink_expected=1 literal_unflagged=1 scratch_var_unflagged=0 v2_var_expected=0 v2_symlink_sites=0 live_var_lineno=811 live_var_resolved_v3=1 live_var_scratch_v3=1 live_var_sites_v2=1 live_var_expected_v2=0 live_symlink_lineno=820 live_symlink_resolved_v3=1 live_symlink_scratch_v3=1 live_symlink_sites_v2=0 mutant_resolve_killed=1 mutant_symlink_killed=1 mutant_symlink_arg_killed=1 rev=2ae00eb750b86eba6c9b54b36b1a6e875e9fd8a6 C2_R41_PASS=true
```

exit 0. Both counters were run again at the lane tip
`b14ff1100f5bb330fc2fa2873d38bf69c165b5e2` and printed the same counts and pass bit, exit 0 each,
receipted in `.ufo/evidence/round-41/after/c1-at-b14ff110.stdout` and `…/c2-at-b14ff110.stdout` (the
`rev=` field echoes the revision the run read, so it differs by design); both counters read a
revision and write nothing to the lane, so the second run is the same measurement.

**Numeric guardrails** (`.ufo/evidence/round-41/census/command-d.stdout`, canonical commands at the base, the measured commit and the tip):
command D `recorded_cases=9 depth_score=9` (depth 9 → 9, no ledger leg added); command C
`boxes=4 checked=0 asserted=4 untouched=0 asserted_mark_upper_bound=8`; the round-21 coldread monitor prints
`calibration_restraint_score: 6` at the base and at the round commit, so the carried `8` is
superseded as an upper bound and calibration is 6 → 6. No axis is harmed.

Negative control for the C1 parse, receipted in `.ufo/waves/round-41/w1/CriticR40Discharge.md`: the
round-40 table counts `(1, 6, 10)` while its summary says `(1, 7, 9)`, so a counter that cannot see
the contradiction cannot print `m9=1` at the base; the seat also re-derived those counts
independently.

## Sources & frontier

Census command, run at round start and round end:

```
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tameshi
```

- Round start: exit 0, 9 × W04 + 1 × W01, zero E codes
  (`.ufo/evidence/round-41/census/start.stdout`); the row count is in
  `.ufo/evidence/round-41/census/row-counts.stdout` because the census script prints `ok`/warnings,
  not a row field.
- Round end: exit 0, the same warning set, zero E codes
  (`.ufo/evidence/round-41/census/end.stdout`), 109 rows by the same row-count receipt.
- Rows added: 2, both tier A / `docs` / `mined` / opened 2026-10-25 / recheck 180d — S153 (`ast`,
  CPython; snapshot `183a4f8c…5317`, 362029 B) and S154 (`Path.write_text`, CPython; snapshot
  `0044cae6…4f093`, 271189 B). Both pages title themselves "Python 3.15.1 documentation". Each row
  parses as 13 awk fields and carries no pipe.
- Rows touched old→new: none. No existing row's `status`, `recheck` or `used-by` cell changed.
- Frontier rows advanced: F4 (golden / snapshot fixture discipline) — the write-path half gains a
  destination-resolution tool and an admitted entry; `cmp` and `git diff --exit-code` remain
  unmeasured. Nothing moves to PROVINCE Core by self-attestation.
- **Id lists (item 10), pasted in full.** Two lists, both pasted as comma-separated tokens;
  `w1` evidence files hold the same bytes (`reg-ids-base` 107 lines, `reg-ids` 109 lines,
  `staged-ids` 103 lines, `collisions` 2 lines, under `.ufo/waves/round-41/assimilation/`).
  - Registry at the base/freeze revision (107 ids, `.ufo/waves/round-41/assimilation/reg-ids-base`):
    S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S040, S041, S042, S043, S044, S045, S046, S047, S048, S049, S050, S051, S052, S053, S054, S055, S056, S057, S058, S059, S060, S061, S062, S063, S064, S065, S066, S067, S068, S069, S070, S071, S072, S073, S074, S075, S076, S077, S078, S079, S080, S081, S082, S083, S084, S085, S086, S087, S088, S089, S090, S091, S092, S093, S094, S095, S096, S097, S099, S100, S101, S102, S103, S104, S105, S106, S107, S108, S132, S152
  - Registry as landed by this round (109 ids, the file above plus `S153` and `S154`, which are this
    round's two rows; `.ufo/waves/round-41/assimilation/reg-ids`):
    S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S040, S041, S042, S043, S044, S045, S046, S047, S048, S049, S050, S051, S052, S053, S054, S055, S056, S057, S058, S059, S060, S061, S062, S063, S064, S065, S066, S067, S068, S069, S070, S071, S072, S073, S074, S075, S076, S077, S078, S079, S080, S081, S082, S083, S084, S085, S086, S087, S088, S089, S090, S091, S092, S093, S094, S095, S096, S097, S099, S100, S101, S102, S103, S104, S105, S106, S107, S108, S132, S152, S153, S154
  - Staged ids (103, `.ufo/waves/round-41/assimilation/staged-ids`):
    S153, S154, S155, S156, S157, S158, S159, S160, S161, S162, S163, S164, S165, S166, S167, S168, S169, S170, S171, S172, S173, S174, S175, S176, S177, S178, S179, S180, S181, S182, S183, S184, S185, S186, S187, S188, S189, S190, S191, S192, S193, S194, S195, S196, S197, S198, S199, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S222, S223, S224, S225, S226, S227, S228, S229, S230, S231, S232, S233, S234, S235, S236, S237, S238, S239, S240, S241, S242, S243, S244, S245, S246, S247, S248, S249, S250, S251, S252, S253, S254, S255
  - Collision count: the `collisions` file is exactly `S153` and `S154` — **2** against the landed
    registry (`reg-ids`), **0** against the base/freeze registry (`reg-ids-base`), because the
    package's first two ids now name this round's own rows. Renumber map: **empty** — no staged row
    was adopted, so nothing was renumbered. The next id above the registry's last is `S155`
    (`corpus/SOURCES.md`); the first id absent from both lists is `S256`, so a future adoption must
    renumber in scratch against documents, not arithmetic.
  - Duplicate *content*, not only duplicate ids: the staged `S153`/`S154` are POSIX `diff` and
    `google/golden`, which the registry already holds as S105 and S106 — a next round must refuse or
    merge against those rows rather than append the staged ones.
- **Assimilation: none adopted.** The package's two staged F4 gate-census entries
  (`r4-gate-write-path-audit`, `r5-gate-write-site-census-corrected`) cite the lane's own tree at
  revision `31687496` as their source, so they are same-ground rows, not expansion (CORPUS rule 4).
  The staged row the round-40 Gate refused keeps that refusal: its flip condition names `31687496`
  and `tools/write-path-census.py` is absent there.
- **considerthese**: `considerthese/2026-10-24.md` proposal 1 (pin blast-radius report before a tool
  edit) mined as `corpus/QUALITY.md` criterion 80, whose falsifier is verified at three revisions
  (`d16f9b5` exit 0, `691bb51` exit 1, `5829676` exit 0). The file was not edited.
- Quarantine slice (read-only, item-10 recipe): 17 rows, every line carrying an S-id; 15 of the 17
  ids are not registry rows, so the slice is named by path and count, never by listing its ids
  (`corpus/lessons/round-41.md`). The register was not edited and no campaign tool was run.
- Census at round start: exit 0 (107 rows). At round end: exit 0 (109 rows).

## Trend verdicts

- **expansion: improved.** One admitted knowledge entry on F4 ground the coverage map did not hold
  (destination resolution as a write-path class), with the two sources that supply its mechanism,
  a `corpus/README.md` row and `corpus/QUALITY.md` criterion 80. Two registry rows added, and the
  frontier note states exactly what stays unmeasured.
- **quality: improved.** The C2 capability is load-bearing in its own instrument: v3's selftest
  fails when name resolution, the symlink branch or the symlink destination argument is removed
  (three mutants, `.ufo/waves/round-41/w1/ExecV3Selftest.md`, `MutFixtureVar.md`), a constant
  classifier cannot pass (`MutConstantClassifier.md`), and A2's re-rooted fixtures were tightened
  after a seat proved the old ones could not see an argument swap. C1's two live mismatches are
  closed with committed receipts, and the round's records were corrected from seat findings rather
  than from its own draft.
- **discernment: improved.** One admit, three refuses and one prior-art citation, each with a
  reason: the assimilation package was refused as same-ground rather than absorbed, the round-40
  refusal was re-checked instead of inherited, and a connector seat's discovery that
  `kotodama-shokunin` already resolves write destinations landed as adjacency (cited, not absorbed,
  no novelty claimed). The instrument's own defects were disclosed with severity and routed rather
  than quietly repaired after data.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — lane
  assertion, no independent promotion verifier this round; the round did not edit `SKILL.md`.
- [~] At least one end-to-end domain task executed and logged in LOG.md — this round's two claims
  are logged with receipts (`LOG.md` `## 2026-10-25 — round 41`).
- [~] Instructions executable by an agent without oral context — input-keyed monitor only
  (`.ufo/evidence/round-21/coldread/measure.py`, score 6 at the measured commit); no independent
  promotion verifier.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` was not edited; the
  `kotodama-shokunin` prior art is cited as adjacency and the lane's own tools only were measured.

SHONEN census at the measured commit: `boxes=4 checked=0 asserted=4 untouched=0`. No box was
promoted this round and no `[x]` was written.

## Round shape, waves and settlement

- Shape: default two-stage — one v1 wave-1 of 40 seats (band 32–64 under
  `scripts/hyaku/ufo-wave-policy.json`) plus one residual `task` call of 8 reviewer/critic seats.
  No wave 2 was dispatched: wave 1's output yielded 8 further distinct attack items, below the 32 a
  wave 2 requires. Round total: 48 seats (≤128).
- Wave 1 role mix: connector 1, scout 6, executor 8, scribe 7, reviewer 10, critic 5,
  mutation-tester 3. Dead seats: 0. Reports: 40 of 40, none empty.
- Settlement receipt: `.ufo/waves/round-41/settlement-receipt.json` (registry 40, reports 40, dead 0,
  40 of 40 seat terminals mapped from the `Session exit recorded` lines whose `sessionFile` names the
  seat) with `.ufo/waves/round-41/settlement-receipt.stdout`. `tools/wave-parent-settle.py` classifies
  it `UNSETTLED detail=parent_exit_unix missing`, and that is reported as it stands: the wave parent is
  this still-running L1, so it has no exit line yet. It is a missing-parent-exit classification, not
  the round-38 parent-exit-before-seats shape — every seat terminal precedes the last report the L1
  read, and all 40 reports were on disk before that read.

## Open items and routed defects

- C1's counter has no self-pin clause, m7/m8 are vacuous without records, m8 covers four path
  prefixes plus a root-file list, m9 reads the whole lesson; C2's counter imports the measured tool
  in-process, reads its pin from the same revision's contract and checks the live sites without
  reading the `resolved` text. All are disclosed in `SCORECARD.md` and `corpus/lessons/round-41.md`
  `## Holds`; a successor pair (self-pin, `records >= 1`, out-of-process tool execution,
  counter-side digest constant, `resolved` inspection, exit-plus-FAIL-line kill oracle) is routed to
  round 42.
- `tools/context-capture.py:1682` and `:1685` are false positives in v3's `unflagged` column (their
  base is a non-folding call over `self.root`); `tools/registry-replay.py:123` writes `expected.json`
  under an explicit `--out` and is counted because an explicit output flag is not in the update-flag
  pattern. Both are in the entry's disclosed class; the fix is routed.
- Sibling prior art: `kotodama-shokunin/tools/harness/{round_runner_conformance,receipt_guard_adoption}.py`
  already resolve write destinations (depth 8 / 6, landing 2026-10-19). This lane's tool is a subset
  and claims no novelty; absorbing the code is refused by `PROVINCE.md`.
- L0 questions: none filed this round. The round-38 question `d0531d78` was not re-filed.
- Tool installs or upgrades this round: **none** (pacman left paused per the orchestrator ruling;
  nothing was needed).
- Stale-lane: respawn-per-round driver; this lane has no other mission open.
