# CounterVsLog — kama round counter vs report file vs log

**Lane checked:** `kama` only. Not a fleet grade. Not a `MORI_CENSUS` verdict.
**Role:** detect and report. No counter write, no launch, no wrap, no remediation.
**Measured:** `2026-10-14T21:34:10-03:00` through `2026-10-14T21:37:28-03:00` (host local, `date -Iseconds`).
**Repo:** `/home/vgpnk/Projects/shokunin`.

## Result

Split. Do not collapse these into one boolean.

| Join | Result | Stable id |
|---|---|---|
| `.ufo/state/kama.round` vs last `launch`/`wrap` in `.ufo/watchdog.log` vs the counter's own report `.ufo/reports/round-1/kama.md` | **AGREE at round 1** | `CVL-DRIVER-AGREE` |
| Same counter vs later report files and `kama-shokunin/LOG.md` | **MISMATCH** | `CVL-REPORT-BEYOND-COUNTER`, `CVL-LANELOG-BEYOND-COUNTER`, `CVL-LANELOG-REPORT-GAP` |

Catalog id `STATE_COUNTER_LOG_MISMATCH` (FindingIds: counter ≠ last watchdog `launch`/`complete`/`wrap`) does **not** fire. Sibling `StateCounterAudit.md` already recorded `SCA-COUNTER-LOG-MATCH` for kama and deferred report-lead. This file is that deferred join for one lane, re-measured, plus the lane `LOG.md` the sibling did not read.

## Predicate

Source, not a live driver run. `scripts/shokunin-watchdog.sh`:

- L3–5: a round ends when `.ufo/reports/round-<N>/<lane>.md` exists.
- L43: counter is the bytes of `.ufo/state/<lane>.round` (missing file reads as 0; this file is present).
- L45: `report_of` is `[ -f .ufo/reports/round-$N/$lane.md ]`.
- L80–81: a successful launch writes the counter to `N` and appends `launch <lane> round=N`.
- L104–106: fleet-wrap logs `wrap <lane> round=N` and does **not** increment the counter.
- L107–110: `complete` of `N` then `launch` of `N+1` is the only advance path in this script.

**Driver agreement** here means: counter integer = last `launch` round = last `wrap` round, mission file = that launch `runId`, and `round-<counter>/kama.md` exists and names that round.

**Mismatch** means a report file or a lane-log round heading names an integer the counter and the watchdog log do not.

## Observations

Commands were read-only. Event times below are log timestamps or `git log` committer times. File mtime `2026-10-13 16:44:48 -0300` on the counter, the log, and the round-1/round-2 reports is a shared later touch (same observation as `SCA-MTIME-BULK`). It is not a launch time.

### Counter and mission

At `2026-10-14T21:35:12-03:00`:

```text
od -An -tx1 .ufo/state/kama.round    → 31 0a
wc -c .ufo/state/kama.round          → 2
```

Bytes are `1\n`. sha256 `4355a46b19d348dc2f57c046f8ef63d4538ebb936000f3c9ee954a27460dd865` (sha256sum, `21:36:06`).

`wc -c .ufo/state/kama.mission` → 29. Content `shokunin-r1-kama-r1790646247` plus newline. sha256 `d0ef2b6204c1496eff7f462d4c12f90fc6eda21c83e8549bed1ab192c150e2d8`.

`git log --format='%h %aI %s' -- .ufo/state/kama.round` (no `--follow`, `21:37:19`) has one commit: `17c1fad` `2026-09-29T00:19:02-03:00`. `git show HEAD:.ufo/state/kama.round | od -An -tx1` → `31 0a`. `git diff -- .ufo/state/kama.round | wc -c` → 0. Working tree matches that commit. No later commit stores 2, 3, or 4.

`stat` at `21:34:10`: counter mtime `2026-10-13 16:44:48.524089950 -0300`, same second as `.ufo/watchdog.log`.

### Watchdog log (kama lines only)

File read in full: 294 lines, 19396 bytes (`wc`, `21:36:06`). `grep -n kama .ufo/watchdog.log` at `21:36:22` returned exactly four lines:

| Line | Text |
|---:|---|
| 249 | `2026-09-28T22:44:08-03:00 launch kama round=1 runId=shokunin-r1-kama-r1790646247` |
| 274 | `2026-09-28T23:39:57-03:00 wrap kama round=1 complete; NOT respawning (fleet-wrap)` |
| 283 | `2026-09-28T23:47:29-03:00 wrap kama round=1 complete; NOT respawning (fleet-wrap)` |
| 293 | `2026-09-28T23:55:00-03:00 wrap kama round=1 complete; NOT respawning (fleet-wrap)` |

Verb tally (`grep` + `uniq -c`, same minute): `launch 1` ×1, `wrap 1` ×3. Zero `complete`, zero `launch-fail`, zero `lane-dead-no-report`, zero `round=2`, `round=3`, or `round=4` for kama. Last log line of the file is L294 `tick=3` at `2026-09-28T23:55:00-03:00`. The launch `runId` equals the mission file.

At `21:36:06`, `[ -e .ufo/fleet-wrap ]` was false (`ABSENT`). The wrap lines name that file as the reason they did not respawn. Current absence does not rewrite those lines. Whether the file existed at `23:39:57` was not re-proved.

### Report files

Existence at `21:35:12` (`[ -f ]` + `stat`) and identity at `21:36:06` (`wc`, `sha256sum`):

| Round | Path | At 21:35:12 | Bytes / lines | sha256 | Self-identity | Git |
|---:|---|---|---:|---|---|---|
| 1 | `.ufo/reports/round-1/kama.md` | present, mtime `2026-10-13 16:44:48.520190387 -0300` | 10144 / 145 | `89bb6ec9c075773737a9d4237833e04131badad396db42aee49e2705165849b1` | L1 `# kama-shokunin — round 1 report` | `74768ab` `2026-09-28T23:15:55-03:00` `round-1: kama lane report…` |
| 2 | `.ufo/reports/round-2/kama.md` | present, mtime `2026-10-13 16:44:48.523046791 -0300` | 9909 / 148 | `4d283741e21d0de7e3ca12aa768fd39a39799a36ab4280f3adaa2eef41c35dab` | L1 `# kama-shokunin — round 2 report`; L3 `probation round 2` | `ee1f621` `2026-09-29T01:36:12-03:00` `round-2: kama report` |
| 3 | `.ufo/reports/round-3/kama.md` | absent | — | — | — | `ls` at `21:36:06`: `No such file or directory` (exit 2) |
| 4 | `.ufo/reports/round-4/kama.md` | present, mtime `2026-10-14 21:21:34.082179579 -0300` | 3074 / 55 | `2fa411d7444ff1bb1c882bdbe3c16a62ee45a1bb06c022cfd723ffe913adcc01` | L1 `# round-4 — kama · OMP-era freshness re-census`; L3 `Steered round: 4` | `cb3c103` `2026-10-14T21:24:03-03:00` |
| 5 | `.ufo/reports/round-5/kama.md` | absent | — | — | — | not claimed by the log headings below |

`git ls-files` at `21:35:12` tracks round 1, 2, and 4. `git status --short` on those three paths plus the counter, mission, and watchdog log was empty.

Round-1's introducing commit (`23:15:55`) is before the first wrap line (`23:39:57`). The path that `report_of` tests was in git before wrap, and the working tree matched HEAD at measure time. That is why wrap at round 1 is consistent with the file, not evidence the counter should have moved.

Round 2 and round 4 commits are after the log's last line (`23:55:00` on `2026-09-28`). No watchdog line names them.

### Lane log

`kama-shokunin/LOG.md`, 271 lines, 16755 bytes, working-tree sha256 `b12a48e5be34fd7340fd5716f2a45fd7c6974d2948c98fbc96bb4a944a05ed16` (`21:36:06`). At `21:37:28`, `git -C kama-shokunin hash-object LOG.md` = `git rev-parse HEAD:LOG.md` = `295d0a2cc738f2564238b584756fafe39772e762`, and `status --short -- LOG.md` was empty. Last commit that touches it: `47f3aed` `2026-10-14T21:23:34-03:00`. Lane HEAD at `21:36:22` was `117c4b2` `2026-10-14T21:31:49-03:00` (`plans: WWKD re-census plan for this round`); that commit is not the LOG commit.

`grep -nE '^## ' kama-shokunin/LOG.md` at `21:35:36`:

| Line | Heading | Names round |
|---:|---|---:|
| 5 | `- 2026-09-28 — round 0: minted as shonen` (not a `##` heading; included so it is not dropped) | 0 (mint, not a steered round) |
| 7 | `## round 1 — operability axis (measured via freshness)` | 1 |
| 100 | `## round 2 — freshness axis` | 2 |
| 203 | `## round 3 — re-census: substrate relocation + box teardown (freshness axis)` | 3 |
| 266 | `## 4 — re-census round (freshness axis-move)` | 4 |
| 268 | `2026-10-14 · steered round 4 · axis: freshness · 32-lane fleet wave + parent integration.` | 4 |

Round 4 is **not** spelled `## round 4`. A scanner that only matches `^## round ` stops at 3 and misses the steered-round line at L268. Both forms were read.

Lane commits whose subjects name those rounds (`git -C kama-shokunin log -- LOG.md`, `21:35:36`): `c6199a2` `2026-09-28T23:15:05-03:00` `round-1`; `83bee7f` `2026-09-29T01:34:16-03:00` `round-2`; `ea72c3e` `2026-10-14T09:46:23-03:00` `round-3: re-census…`; `84a8130` `2026-10-14T21:15:36-03:00` `round-4: OMP-era freshness re-census…`. Those are log-history observations, not driver counter writes.

### Prompt files (adjacent; not the counter)

`ls .ufo/prompts/kama-round-*.md` at `21:35:12`: `kama-round-1.md` (1540 bytes), `kama-round-2.md` (1561 bytes). Round-2 prompt L1 is the watchdog template: `You are the kama L1, round 2 of up to 1024.` Introduced by `896660a` `2026-09-29T01:22:57-03:00` (`git show --stat`: 11 insertions, that path only in the pathspec). That is after the log ended and before the round-2 report commit. There is still no `launch kama round=2` line.

At `21:36:06`, `kama-round-3.md` and `kama-round-4.md` were absent (`ls` exit 2).

## Exact mismatch

Counter and watchdog log stop at **1**. Everything below is past that integer, or is a hole between claimed rounds.

| Integer | Counter | Watchdog kama line | Report file | Lane LOG heading |
|---:|---|---|---|---|
| 1 | `1\n` | launch L249, wrap L274/L283/L293 | present, names round 1 | L7 `## round 1` |
| 2 | not stored | none | present, names round 2 | L100 `## round 2` |
| 3 | not stored | none | **absent** | L203 `## round 3` |
| 4 | not stored | none | present, `Steered round: 4` | L266 `## 4` + L268 `steered round 4` |

Deltas a later run can diff:

- `CVL-DRIVER-AGREE` subject `lane=kama` payload `counter=1 launch=1 wrap=1 report=round-1/kama.md mission=shokunin-r1-kama-r1790646247`
- `CVL-REPORT-BEYOND-COUNTER` subject `lane=kama` payload `rounds=2,4` (files exist; log and counter do not name them)
- `CVL-LANELOG-BEYOND-COUNTER` subject `lane=kama` payload `rounds=2,3,4`
- `CVL-LANELOG-REPORT-GAP` subject `lane=kama;round=3` payload `log_heading=L203 report=absent`

Round 3 is a missing **file**, recorded as absent, not as an unhealthy lane. It is a gap only relative to the lane log heading. The driver never claimed round 3, so this is not `LANE_REPORT_ABSENT` under FindingIds (that id requires the counter or the driver log to say round N). It is also not `STATE_COUNTER_LOG_MISMATCH`.

## Inference

Separated from the tables above.

- The v4 script would leave the counter at 1 after a fleet-wrap of round 1. The three wrap lines and the unchanged `1\n` match that branch. They do not explain rounds 2–4.
- Rounds 2 and 4 were recorded by report commits and by `LOG.md` after this watchdog log's last line, without a logged launch and without a counter rewrite. The writer of those files is not identified here.
- The round-2 prompt matches the watchdog template and landed in `896660a` with no matching log line. A crashed `launch_lane` (prompt write at L69, log append at L81) is one way that can happen. A non-driver copy of the template is another. Neither was observed. Not chosen.

## Unknown

- Whether `.ufo/fleet-wrap` existed at `2026-09-28T23:39:57-03:00`. It is absent now.
- Who wrote `.ufo/prompts/kama-round-2.md`. The introducing commit message is `round-14: kengaku report`. That is a label, not a mechanism.
- Whether a driver log outside `.ufo/watchdog.log` exists. This script appends only that path. A host-wide search was not run. No second `watchdog.log*` was opened.
- `git log --follow -- .ufo/state/kama.round` pairs this path with a fixture `.ufo/waves/round-12/fixtures/closure-sample/failed/.ufo/state/kagi.round` at similarity 100%. Both files are the two bytes `1\n`. That is rename detection, not evidence the kama counter was copied from the fixture. Ignored for the integer.
- Other lanes were listed at `21:34:45` (`find .ufo/reports -name '<lane>.md'`) only to choose this lane. Their counter-round report files were present. Their `LOG.md` files were not joined. `StateCounterAudit.md` already owns the nine-lane counter/log match and names `SCA-REPORT-LEAD` for all nine. This report does not re-grade them.
- Round-4 report bytes were not re-hashed after `21:36:06`. The file's git commit is `cb3c103` at `21:24:03`, before that hash.

## Limits

- One lane, one advisory file. No census gate was run. No process was restarted. No state file was written except this member report.
- Agreement is about integers and file presence plus the report's own round title. It is not a quality grade of round-1/2/4 prose.
- A later run compares the four `CVL-*` ids above. If the counter is still `1` and round-2/4 reports plus LOG headings 2–4 remain, those three mismatch ids persist. If a launch line for round 4 appears and the counter becomes `4`, `CVL-DRIVER-AGREE` clears and must be re-measured; it does not silently update.
