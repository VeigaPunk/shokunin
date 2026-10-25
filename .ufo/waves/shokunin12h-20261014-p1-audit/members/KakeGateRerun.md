# Kake gate re-run (independent)

Observer: KakeGateRerun. Read-only. Lane files not edited. No commit. No bare/live sweep (that path fetches). Substrate: `kake-shokunin` HEAD `59948314e9af5dd6ef81894fc1c422b353f10938` (matches the assigned lane identity). `git status --porcelain` at open and after the probe: `?? plans/` only. Script sha256 before and after the scratch probe: `19817629c5a41dadd076ac0da1d56bb5d4d7a1c28e01a3f54a7f6f3ec723b2ae`. Host clock on the four gate runs: `2026-10-15T00:17:29Z`, `node v24.21.0`. cwd: `/home/vgpnk/Projects/shokunin/kake-shokunin`.

Compared against `corpus/lessons/round-19-recensus.md` §Verdict lines (measured), not against SCORECARD historical `10/10` rows.

## Claim vs observed

| Lesson claim | Observed | Verdict |
|---|---|---|
| `node scripts/freshness-sweep.mjs --selftest` → exit 0, 13/13 passed | exit 0; last line `selftest: 13/13 passed` | agree |
| case `e` marks `B19,B1083,E1139,B1298,E1300,B1318,E1320`, 0 write sites outside the region | printed got-line matches that string exactly | agree on the printed string; disagree that it proves normal-path confinement (counterexample below) |
| `--offline` → exit 0, `VERDICT: OK (exit 0, partial: offline)`; §history `SUSPENDED` (pin-declared); §armed `skipped(offline)` | exit 0; last line exact; history line and skipped line match the paraphrase | agree |
| `KAKE_PROBE_HISTORY=<missing>` → exit 2 | contract argv (below) exit 2; JSON `code` 2, `ok` false, error `cannot read /tmp/does-not-exist.jsonl`, not suspended | agree on exit 2 |
| no `$HOME/.kake-freshness-selftest-*` after `--selftest` | count 0 before the selftest, 0 after it, 0 after the scratch probe | agree |
| `--json --offline` (safe set; lesson quotes no JSON line) | exit 0; program last line `}`; `ok` true, `code` 0, `complete` false | no quoted number to mismatch |

No quoted exit code or verdict line in the lesson disagreed with this re-run. The mismatch is what case `e`'s `0 outside` is allowed to mean.

## Commands (argv, exit, last program line)

Residue glob: `$HOME/.kake-freshness-selftest-*`.

1. `node scripts/freshness-sweep.mjs --selftest`
   - residue before: 0
   - exit 0
   - last line: `selftest: 13/13 passed`
   - case `e` got-line: `0 outside (regions B19,B1083,E1139,B1298,E1300,B1318,E1320)`
   - residue after: 0
   - cases printed, all PASS: a, b, f, g, h1, h2, c, j, k, l, i, d, e (13)

2. `node scripts/freshness-sweep.mjs --offline`
   - exit 0
   - last line: `VERDICT: OK (exit 0, partial: offline)`
   - line above: `skipped(offline): §armed (all remote checks) · §history (probe-history source absent — pin-declared) — complete=false, never counted as pass`
   - history line: `§history  SUSPENDED — probe-history source absent by declaration (pins.probeHistoryAbsent): /home/vgpnk/Projects/webzites/state/probe-history.jsonl — section suspended until a history source is re-anchored`
   - armed: `all remote checks skipped(offline) — NOT counted as pass (complete=false)`
   - also printed, not a drift predicate: `set-delta files: +1 / -0 — added: corpus/lessons/round-19-recensus.md`; `~/Projects children: 30 (informational)` with 16 added names against the 14-name pin (`omegag` and `omegag-*`). §paths: 41 files, 305 occurrences, 68 unique tokens, resolve 5, declaredAbsent 55, drift 0, unresolved 8, new miss 0. Pins header: round 18, updated 2026-10-14.

3. `node scripts/freshness-sweep.mjs --json --offline`
   - exit 0
   - last line: `}`
   - verdict fields: `complete` false, `ok` true, `code` 0, `reasons` `[]`, `skipped` `["§armed (all remote checks)", "§history (probe-history source absent — pin-declared)"]`
   - `sections.history.historySuspended` true; `sections.armed.ok` null (skipped, not a pass)

4. `KAKE_PROBE_HISTORY=/tmp/does-not-exist.jsonl node scripts/freshness-sweep.mjs --section=history --json`
   - `/tmp/does-not-exist.jsonl` was absent before the run
   - exit 2
   - last line: `}`
   - verdict fields: `ok` false, `code` 2, `complete` true (this flag is `!offline`, not "every section ran"), `reasons` `["§history cannot read /tmp/does-not-exist.jsonl"]`, `skipped` `[]`
   - history object: `file` `/tmp/does-not-exist.jsonl`, `error` `cannot read /tmp/does-not-exist.jsonl`, `code` 2, no `historySuspended`

Bare `node scripts/freshness-sweep.mjs` was not run. It would exercise §armed remote checks. Excluded on purpose. The lesson's "bare online exit 1" sentence was not re-measured here.

## Counterexample (case `e` confinement)

Lesson treats the printed region marks plus `0 outside` as measured proof that write sites sit only in the selftest regions. The scanner opens a region on any line containing `SELFTEST-WRITES-BEGIN` and does not skip comments. Line 19 is the header comment `the SELFTEST-WRITES-BEGIN/END region`. That substring opens a region; it does not contain `SELFTEST-WRITES-END`, so the region stays open until the real fixture `SELFTEST-WRITES-END` at line 1139. Call-site matching does skip `//` lines. A write in the normal path (lines 20–1138) is inside the false region and cannot fail case `e`.

Scratch copies only, under `/tmp/kake-gate-rerun-scratch/`, deleted after the probe. Lane file not written. Detector: the copy's own `--selftest` (same case `e`).

- Pristine copy: exit 0, last line `selftest: 13/13 passed`, case `e` `0 outside (regions B19,B1083,E1139,B1298,E1300,B1318,E1320)`. Baseline green.
- Mutant: first statement of `verdictOf` set to `fs.writeFileSync('/tmp/kake-gate-rerun-mutant-write', 'normal-path');`. Expected if confinement were real: case `e` FAIL. Observed: exit 0, last line `selftest: 13/13 passed`, case `e` PASS `0 outside (regions B19,B1084,E1140,B1299,E1301,B1319,E1321)`. Verdict: **survived**.
- Control, same call inserted on the first non-comment line after the real fixture `SELFTEST-WRITES-END` (before `const envA`). Observed: exit 1, last line `selftest: 12/13 passed`, case `e` FAIL `1 outside: 1140: fs.writeFileSync('/tmp/kake-gate-rerun-mutant-write', 'outside'); (regions B19,B1083,E1139,B1299,E1301,B1319,E1321)`. Verdict: **killed**. The detector is not globally inert; it is blind inside the comment-opened span.
- Restoration: scratch directory removed; `/tmp/kake-gate-rerun-mutant-write` removed; lane script hash unchanged (above); residue count 0; porcelain still only `?? plans/`.

## Named debt (not fixed)

1. Case `e` does not confine normal-path writes. Owner: kake, `scripts/freshness-sweep.mjs` region scanner. Unblock: do not treat the line-19 prose sentinel as `BEGIN` (comment-aware scan, or stop embedding the sentinel in that comment). A normal-path `writeFileSync` must then fail case `e`. Do not re-pin `13/13` to hide this. This audit did not patch it.
2. Lesson-recorded, still the right reading of the offline run, not re-opened: PQ-2 (`~/Projects/ds4cc-marketplace` gone), PQ-14 (`~/Projects/plazir-15-site` gone), §history suspended on the canonical `probe-history.jsonl`. Unblock remains the lesson's: restore the source or declare the watch dead; point `KAKE_PROBE_HISTORY` at a surviving history or declare the probe-timer era ended. Bare exit 1 was not re-run (fetch exclusion).
3. Stale live prose the lesson already names, still present on read: `SKILL.md:59` still cites `~/Projects/webzites/bin/webzites.mjs`; `SKILL.md:111` still cites `~/Projects/webzites/scripts/kimi-surface.mjs`. Offline sweep lists both `declaredAbsent`, drift 0. `freshness-sweep.md:43-53` still carries pre-r18 literals (`pathsMissSet` 10 entries, `projectsChildrenSet` 36, charter pin `2026-09-26`). `SCORECARD.md:20` still says 14 `~/Projects` children; this run printed 30. Agree with the lesson's 30. Those lines are describe-don't-pin, not a red gate.
4. Informational only, not a lesson-number miss: `pathsFiles` does not list `corpus/lessons/round-19-recensus.md`, so offline prints file-set `+1/-0`. Runbook P3 says file-set delta is not fatal. Exit stayed 0. Owner if anyone wants the footer quiet: kake, same commit as a future pin edit. Not a reason to call the offline gate red.
