# Tsukuroi round 20 — recovery continuation

## Work performed

Round20 claims: **C1** adjacency/attributed ownership clarification; **C2** operability/object-only landed revision selectors; **C3** calibration of the actual operative live audit map. This is the inherited tsukuroi round20 claim, not a round19 restart. Baseline: `0cbc34dd6b20896085a8fb07943e3ea4027d8472`.

- Read the round19 non-author spot-check and corrected the routed defects without rewriting the historical round19 record: the operative `boot-chain-audit` table, the SKILL historical-prefix exception, OUT-009 attribution scope, and rule4's unsupported no-write assertion. Evidence: `corpus/lessons/round-20.md:31-48`; `corpus/knowledge/contract-corrections-r20.md`; `corpus/knowledge/boot-writers-r19.md`.
- C1 appends only the bounded OUT-009 sibling-declaration clarification; Kaidoku/Revenger arbitration and write authority remain unresolved. The opt-in metric is pinned to the exact correction-file bytes and digest, an exact appendix after the preserved baseline, and same-revision registry/census evidence; the field is absent from default output. Evidence: `PROVINCE.md:148-152`; `.ufo/waves/round-20/ownership-correction.txt` (SHA-256 `23289c7a8fa558c0249ff56b53ccddf9dcae522ef6dcd3064dc3ce607453fc2a`); `tools/check-adjacency-anchors.py`; final `c1-after.stdout`.
- The final C1 evaluator exposed a stale lane-owned inbound locator `IN-101` (`found_line=62` named `def clean_env`, while the quote is line63). Only the local record was corrected to line63; no sibling source was edited. The final C1 and legacy-mode gates both pass. Evidence: `corpus/knowledge/adjacency-anchors-r19.json` IN-101; first-run failure `measure/final-r20/c1-after.stdout`; final receipts `measure/final-r20c/{c1-after,adjacency-legacy}.stdout`.
- C2 uses the shared object-first binder and a separate finite original-nine consumer evaluator. It rejects hex-looking branch/tag aliases, tests real object IDs against ref shadows, preserves case-insensitive hex and annotated-tag-to-commit resolution, and grades CANNOT rows by status/finding rather than mistaking a full requested-SHA echo for an accepted binding. The C2 claim remains bounded to the preregistered per-consumer matrix. Supplementary shared-binder selftests add a stored non-empty tree, tags to blob/tree and nested tag-to-commit; these additions do not change the frozen `object_selector_tools` metric. Evidence: `tools/_revision.py`; `tools/check-revision-binding.py`; `build/BindTagObject.md`; `measure/final-r20c/c2-after.stdout`.
- C3's opt-in audit reads the highest operative Markdown table outside fences and checks a unique `boot-chain-audit` row, exact live/selftest invocations and map, and no-write scope; generic registry coverage remains unchanged. Evidence: `SKILL.md:2096-2118`; `tools/check-registry-coverage.py`; `measure/final-r20c/c3-after.stdout`.
- The exec-log systemctl classifier is finite and read-only, including known read verbs/options and bounded wrapper/shell recursion. BusyBox recursion follows recognized shell applets; `busybox echo -c` is not treated as shell execution. It is not a shell-equivalence, filesystem-write, or host-safety proof. Evidence: `tools/check-recheck-commands.py`; `measure/final-r20c/selftest-check-recheck-commands.stdout`.
- Curated sources S077-S080: Git object-prefix documentation, the exact sibling declaration, the committed live audit summary, and the historical no-write rule. S080 is rejected as support; no new ownership award or boot-readiness claim is inferred. Evidence: `corpus/SOURCES.md:142`; `corpus/lessons/round-20.md:20-29`.
- Read-only safety boundary held: no pacman, service, bootloader, initramfs, reboot, target command, or tool-install action. Next-boot readiness remains unknown; no host claim is made.
- Two validated 64-seat waves ran, total128 spawned. Build roles: executor4, reviewer28, scout16, critic5, connector4, scribe4, revenger3; 13 provider-rate-limit seats have no reports and were not replaced. The parked `BindTagObject` original seat later completed its first report. Falsify roles: reviewer32, scout16, critic8, mutation-tester4, connector4; all64 reports exist; no seat was replaced. Reports/specs/registries/dispatches are under `.ufo/waves/round-20/{build,falsify}`. Two earlier build task-call attempts were refused before spawn; the third unchanged call spawned64. Slot reservations were recorded/released.
- Process-role limitation: L1 held the frozen planner seat, but neither validated wave contains a separately planner-tagged L2 item (`ConnPlanner` is connector). No extra wave or role substitution is claimed. The strict round20 L2 planner-role floor is therefore not fully met.

## Landed changes

| Lane commit | Changes | LOG evidence |
|---|---|---|
| `7f4231401e4918146c4442e8633334231c7d88d6` | Integrated the four inherited worktree candidates, bounded BusyBox fix, round20 documentation, and both wave evidence sets. | `LOG.md` — round20 declaration and dispatch/review correction |
| `a90cefef43198d8593c7c862bc6d6868e5171d16` | Corrected the lane-owned IN-101 locator, C2 refusal-field interpretation, and rerunnable smoke output path. | `LOG.md` — first evaluator red and bounded repairs; C2 refusal echo retest |
| `fc2a0085088cedb3ab59dc3fff16523c0f42a6b4` | Final C2 judge/oracle corrections, parent-decoy fail-closed behavior, supplementary object-type selftests, final claim measurements and retained smoke/suite outputs. | `LOG.md` — resumed C2 target-type review and final R20 measurements |
| `82e519203e676c532b1dc5ea91a85671f2286e7b` | Final scorecard, SKILL/lesson/log outcomes, and the first, intermediate and final measurement receipts. | `SCORECARD.md:614-630`; `LOG.md` final R20 measurements |

All lane landings were produced by `jj-lane.sh`; cited hashes are its final `landed` lines. The report is the last fleet-path change.

## Before → after measurements

All after measurements are pinned to lane code commit `fc2a0085088cedb3ab59dc3fff16523c0f42a6b4`; full outputs are in `.ufo/waves/round-20/measure/final-r20c/`.

| Claim | Counting command | Before | After |
|---|---|---|---|
| C1 | `python3 tools/check-adjacency-anchors.py --revision <REV> --ownership-corrections` | Exit1; `ownership_corrections=0`; `OWNERSHIP-CORRECTION-MISSING` | Exit0; `ownership_corrections=1`; no findings |
| C2 | `python3 tools/check-revision-binding.py --tools-revision <REV> --object-selectors` | Exit1; `object_selector_tools=0/9` | Exit0; `object_selector_tools=9/9`; `original-nine-continuity` also exits0 |
| C3 | `python3 tools/check-registry-coverage.py --revision <REV> --audit-live-map` | Exit1; `audit_live_map_errors=1` on the selected row | Exit0; `audit_live_map_errors=0` |

The final suite ran all17 repository selftest commands with exit0. Named counts: `_revision`57/57, revision-binding62/62, adjacency25/25, recheck-commands95/95 and registry-coverage23/23. The changed-path smoke at the same commit (`measure/smoke-final2/results.json`) passed all five declared tool paths; `round20-prefixes=True`; adjacency legacy mode and registry coverage exit0. The initial failed evaluator outputs (`final-r20`, `final-r20b`) are retained alongside the final receipt as evidence of the targeted repairs.

## Sources & frontier

`SOURCES.md`: **76→80 rows** (S077–S080); added-by-tier **A4**, mined3/rejected1. Earlier immutable rows and their status/recheck/used-by fields touched: **0**. Frontier rows advanced: **0**; the remaining leads stay unopened. Counting/validation command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tsukuroi`. End census exited0 and retained eight existing W04 duplicate-URL warnings in `.ufo/waves/round-20/measure/final-r20c/census-end.stdout`.

## Trend verdicts

- **Expansion: improved** — four source rows were added and screened (three mined, one rejected), with exact scoped quotes and no new frontier claim. Evidence: `corpus/SOURCES.md:142`; end census receipt.
- **Quality: improved** — all three finite claim measurements reached their preregistered outcomes, the 17-command selftest suite and changed-path smoke passed, and the IN-101/C2 judge defects were retained, fixed and remeasured. Scope-gate reds and bounded C2 coverage remain explicit, not converted into a global safety claim. Evidence: `measure/final-r20c/results.json`, `SCORECARD.md:620-629`.
- **Discernment: unprovable-but-better** — the falsify wave identified predicate-specific C1/C2/C3 weaknesses and the final code preserves rejected S080, unresolved ownership arbitration, C2 type limits and malformed seat declarations. All reviews remain author-dispatched; no outside claim closure or non-author SHONEN verification occurred. Evidence: `.ufo/waves/round-20/falsify/`, `corpus/lessons/round-20.md`.

## SHONEN

- [~] SKILL.md contains decision tables, error patterns, checklists and cited sources — `SKILL.md:2096-2118`; non-author verification remains owed.
- [~] At least one end-to-end domain task executed and logged — C1/C2/C3 evaluator receipts and `LOG.md`; no host task was run.
- [~] Instructions executable without oral context — bounded gate/selftest evidence in `measure/final-r20c/`; whole-SKILL no-oral-context retest remains unverified.
- [~] No cross-domain bleed — `PROVINCE.md:148-152` and read-only boundary in this report; no ownership arbitration or external write permission is claimed.

Stale-lane: respawn-per-round driver; no other mission of this lane is open.

Tool installs: none.

## Open defects / L0

- `seat-scope-build` exits1 with13 `SCOPE-REPORT-MISSING` rows corresponding to known provider-rate-limit deaths; `seat-scope-falsify` exits1 with20 `SCOPE-TRAILER-MALFORMED` period-appended `Scope: executed=none.` trailers. Both report0 unauthorized and0 undeclared declarations, but those self-reports do not prove execution absence. No reports or trailers were rewritten; no dead seat was replaced.
- The two wave specs lack a separately planner-tagged L2 seat; the frozen L1 planner does not erase that process-contract gap. Candidate source digests were not pinned per read at dispatch, so reviewer reports against mutable scratch paths remain predicate/snapshot-specific.
- C2's frozen original-nine per-consumer matrix does not include tree or tag-to-noncommit selectors. The shared binder selftest covers these additional cases, but universal consumer/type coverage is not claimed; the evaluator's resolver is still algorithmically similar to the binder for untested Git object classes.
- Ownership arbitration for OUT-009 remains unresolved. Host next-boot readiness remains unknown: the existing round17 urgent safety question and its corrections/errata remain at fleet `.ufo/l0-questions.md:60-64`; this round added no L0 and ran no host/boot action.
