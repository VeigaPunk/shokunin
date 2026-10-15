# Aggregator round 10 — integration contract

## Goal

One move: corpus review, tied lowest at 9 with cross-lane quality and mint/dormancy (SCORECARD.md:301-305). Fix the six-name default of `.ufo/waves/round-9/corpus-gate.mjs` so default `--all` selects all physical direct child directories matching `/^[a-z0-9][a-z0-9-]*-shokunin$/` under script-derived MAIN_ROOT. Current inherited baseline `.ufo/waves/aggregator-r10/before.json` at b598ce0e1d4fa8851d3e238ee6afde42bd57f787 records 6 of 19 represented, 13 omitted, gate exit 1. That is authoritative historical measurement; do not rerun the old live gate merely to confirm it.

## Contract

Read MISSION.md + AXES.md, canonical shokunin skill/protocol, and relevant sections of SCORECARD.md / CORPUS.md / PROTOCOL.md. Existing uncommitted `.ufo/waves/aggregator-r10/` evidence is inherited, not our dispatch; preserve it. Useful prior plan/falsifiers are its seats/plan.md and seats/critic.md. New evidence belongs only under `.ufo/waves/aggregator-r10-resume/`. Parent owns integration, records, commit, push and final judgment. No child delegation. Skip ALL builds, lint, tests and formatters mid-flight; parent runs checks once after integration. Do not source live configuration. No global routing edits, model pins, counters, driver changes, domain writes, push, or commit by L2.

Discovery is nonrecursive, excludes symlinks and regular files, sorts deterministic names, and rediscovers each invocation. Missing corpus or own Git root produces visible per-lane could-not-evaluate (exit 2), not silent omission; prevent inheritance of fleet Git metadata in default-only discovery and allow legitimate `.git` worktree files. Empty/failed discovery must explicitly report coverage failure with exit 2. Preserve explicit --repos (including order and legacy empty list), --repo, --snapshot, grading rules, finding IDs, historical expected snapshots and exit precedence 2 > 3 > 1 > 0. No second hardcoded lane list. No semantic rules added this move.

No root SHONEN.md exists; final report uses four canonical PROTOCOL.md:425-428 boxes. Author-dispatched seats are not independent promotion verifiers. Broad corpus score stays 9 (not saturation); concrete directory coverage can improve. Cross-lane quality and mint/dormancy stay 9 unchanged. Full CORPUS conformance, configured-but-missing dirs and atomic live-tree snapshots are explicitly not established. Parent must emit per-repo verdict lessons and refresh append-only AGGREGATE ledger; child commits restricted to aggregator-owned corpus files, never child pushes.

Report path already contains a historical marker; preserve all bytes and append a complete dated section after committing work. Preserve historical LOG/SCORECARD/ledger bytes; append correction/current assessment. Never leak corpus text, credential values, references, finding snippets, or session material: metadata, IDs, rule names, pathnames and counts only.

## Interfaces and ownership

- Selection executor alone edits existing corpus-gate.mjs. No exported symbol change; LSP reports no configured language servers.
- Regression executor alone creates `selection-regression.mjs`, standalone isolated actual CLI behavioral tests, accepts optional `--gate <source>` for before/after replay.
- Census executor alone creates `measure-corpus.mjs`, actual CLI capture reduced to redacted metadata JSON (source commit/digest, direct dirs, summary membership, missing/extra/duplicates, per-lane revision/dirty/exit/findings/rule counts), never raw gate output. Parent captures stdout to evidence.
- All other seats write only their assigned evidence file. Read final code when available; review is advisory, never a shipping authority.

## Acceptance

Default summary membership equals sorted direct local child names, one each; changes in local lanes need no code/config edit. Empty discovery and missing corpus/Git fail visibly; explicit modes preserve prior behavior. Parent runs regression before/after on isolated trees, existing selftest and frozen expectations, actual local gate via redacted collector, then creates per-repo lessons, measures named committed code, records all artifacts and pushes fleet only.

## Operator custody update

LOG.md:701-708 was appended concurrently by the operator: audio, game-dev-2d and game-dev-3d are Devin-owned, removed from the driver and hold unrelated in-flight work. They remain physical corpus discovery members, not configured-fleet members. This parent will keep all three child repos read-only: metadata verdicts stay in the fleet report; no lesson, commit or push in those repos. The remaining child-corpus lesson duty proceeds under the canonical aggregator exception. Do not conflate nineteen physical children with the now-eighteen configured lanes.
