# StateCounterAudit

Advisory observation. Not a judge verdict. No process was restarted, completed, or written except this report.

**Result:** 9/9 `.ufo/state/*.round` counters agree with the watchdog log. Mismatch count is 0 under the driver write rule below. A comparison against the last `complete` verb, or against report files above the counter, is a different question and is not a counter/log mismatch.

## Agreement rule

Observed in `scripts/shokunin-watchdog.sh` (current tree, v4 header):

- `launch_lane` writes the counter only after a successful launch: `echo "$n" > "$SK/.ufo/state/$lane.round"` at line 80, then appends `launch <lane> round=<n> runId=<rid>` at line 81. `launch-fail` (line 83) does not write the counter.
- `complete <lane> round=<n>; respawning` (line 109) does not write the counter. The following `launch_lane` of `n+1` does.
- `wrap <lane> round=<n> complete; NOT respawning (fleet-wrap)` (line 106) does not write the counter. The wrapped round stays the counter.

So the on-disk counter is the last successful launch round. After a wrap of that same round, it also equals the last wrap round. It is not "completed rounds" and it is not `last complete + 1` once wrap has stopped respawn.

v3 (`655a41d`) used the same write site (`echo "$n" > …/$lane.round` only inside successful `launch_lane`) and logged `mission=` instead of `runId=`. v2 (`930502c`) wrote the counter in `bump` on both launch and steer (`next=$((n+1)); bump`). Those early lines are in the log; later successful launches overwrote the counters to the values below.

## Measurement

| Item | Observation |
|---|---|
| Measured | `2026-10-14T21:35:33-03:00` (`date -Is`) |
| Counter bytes | `od -An -tx1 .ufo/state/*.round` at `2026-10-14T21:30:29-03:00`; values re-read via `sha256sum` at `21:35:33` |
| Log | `.ufo/watchdog.log` — 294 lines, 19396 bytes, raw sha256 `c16382b5a59c956d57d96fddaeb288f429998b7693b029d058877d4ca0dc1798` |
| Log mtime | `2026-10-13 16:44:48.524089950 -0300` (`stat -c '%y'`) — same nanosecond as every `*.round` file |
| Log span | first line `2026-09-28T15:44:59-03:00 watchdog tick …`; last line `294: 2026-09-28T23:55:00-03:00 tick=3` |
| Git | worktree blob == `HEAD` blob for all 9 counters and the log at `2026-10-14T21:32:59-03:00` (`git rev-parse HEAD:<path>` vs `git hash-object`). Last commit touching them: `17c1fad` `2026-09-29T00:19:02-03:00`. HEAD at the `21:35:33` snapshot was `61ba9b8def3c` and did not change these blobs (log sha256 unchanged from the `21:32:59` read). |
| Driver process | `ps -eo pid,lstart,cmd \| awk '/shokunin-watchdog/ && !/awk/'` at `21:35:33` printed no lines. `shokunin-watchdog.sh` was not observed. |
| `fleet-wrap` | absent (`[ -e .ufo/fleet-wrap ]` at `21:35:33`) |
| Parse | 294/294 lines matched `timestamp verb rest`. Verbs: `launch` 97, `complete` 95, `wrap` 22, `steer` 15, `launch-fail` 0, `lane-dead-no-report` 0, plus `watchdog` 1 and `tick=N` lines. No unparsed line. |

Lane set in the script (`LANES`, line 14) is exactly the nine `*.round` files. No extra `*.round`. No log lane lacks a counter file.

## Per-lane agreement

Command shape: walk `.ufo/watchdog.log`; for each lane keep the last `launch`, `complete`, and `wrap` line; compare the round field to `tr -d '[:space:]' < .ufo/state/<lane>.round`.

| Lane | Counter | Bytes | sha256 | Last launch | Last `complete` | Last wrap | Match |
|---|---:|---|---|---|---|---|---|
| aggregator | 10 | `31 30 0a` | `917df3320d778ddbaa5c5c7742bc4046bf803c36ed2b050f30844ed206783469` | L247 `round=10` `shokunin-r10-aggregator-r1790645840` | L246 `round=9` | L286 `round=10` | yes |
| kagi | 16 | `31 36 0a` | `e6c21e8d260fe71882debdb339d2402a2ca7648529bc2303f48649bce0380017` | L257 `round=16` `shokunin-r16-kagi-r1790647154` | L256 `round=15` | L292 `round=16` | yes |
| kake | 16 | `31 36 0a` | same as kagi (`16\n`) | L255 `round=16` `shokunin-r16-kake-r1790647152` | L254 `round=15` | L289 `round=16` | yes |
| kama | 1 | `31 0a` | `4355a46b19d348dc2f57c046f8ef63d4538ebb936000f3c9ee954a27460dd865` | L249 `round=1` `shokunin-r1-kama-r1790646247` | none | L293 `round=1` | yes |
| kasegi | 17 | `31 37 0a` | `54183f4323f377b737433a1e98229ead0fdc686f93bab057ecb612daa94002b5` | L266 `round=17` `shokunin-r17-kasegi-r1790648100` | L265 `round=16` | L287 `round=17` | yes |
| kengaku | 13 | `31 33 0a` | `1a252402972f6057fa53cc172b52b9ffca698e18311facd0f3b06ecaaef79e17` | L268 `round=13` `shokunin-r13-kengaku-r1790648103` | L267 `round=12` | L288 `round=13` | yes |
| kotoba | 16 | `31 36 0a` | same as kagi (`16\n`) | L261 `round=16` `shokunin-r16-kotoba-r1790648057` | L260 `round=15` | L291 `round=16` | yes |
| kumitate | 16 | `31 36 0a` | same as kagi (`16\n`) | L252 `round=16` `shokunin-r16-kumitate-r1790646699` | L251 `round=15` | L290 `round=16` | yes |
| protocol | 14 | `31 34 0a` | `9a92adbc0cee38ef658c71ce1b1bf8c65668f166bfb213644c895ccb1ad07a25` | L264 `round=14` `shokunin-r14-protocol-r1790648098` | L263 `round=13` | L285 `round=14` | yes |

Launch rounds are strictly increasing by 1 wherever two `launch` lines exist for the same lane, except kagi's launch verbs jump `1 → 3` because round 2 is a `steer`, not a `launch` (see below). Every `complete N` is preceded by a dispatch of N (`launch` or `steer`) and followed by `launch N+1` before any later `complete`. Every `wrap N` equals that lane's last `launch N`. No `launch` round field disagrees with a `runId=shokunin-r<N>-` prefix.

Paired write check (not a second authority): each `.ufo/state/<lane>.mission` file at `21:35:33` is exactly the `runId` on that lane's last `launch` line. v4 writes mission and round in the same success branch (lines 79–80).

kama has zero `complete` lines. Its completion evidence is `wrap kama round=1` (three times: L274, L283, L293). That matches the counter. It is not a missing completion.

## Not mismatches

**Off-by-one against `complete`.** For the eight lanes that have a `complete` line, the last `complete` round is `counter - 1`. That is what the script does: complete N, then launch N+1, which stores N+1. After wrap, the counter stays on the wrapped round, so it matches `wrap`, not the previous `complete`. Treating `complete` as the counter would manufacture 8 false mismatches and would mark kama unmatched. Rejected.

**Repeated wraps.** Wrap counts are protocol 1, aggregator/kagi/kake 2, kama/kasegi/kengaku/kotoba/kumitate 3. v4 re-enters the wrap branch on every tick while the mission is still in `ufo status`, the report file exists, and `fleet-wrap` exists. Wrap does not rewrite the counter. Unequal wrap counts are not counter drift.

**Identical sha256 on kagi/kake/kotoba/kumitate.** All four files are the two bytes `16` plus newline. Same hash is the same content, not a copied lane identity. Mission files and last-launch runIds differ.

**mtime is not the launch time.** All nine counters and the log share mtime `2026-10-13 16:44:48.524089950 -0300`. Log event times are `2026-09-28`. The committing revision of these bytes is `17c1fad` at `2026-09-29T00:19:02-03:00`. Inference: the shared mtime is a later restore of committed bytes, not nine separate launch writes. The integers still match the log. Do not use mtime as a counter-update timestamp. Finding id `SCA-MTIME-BULK` (10 files). Not a value mismatch.

## Log holes that do not move the current counter

These are gaps inside the log. They do not make any current counter disagree with its last launch or last wrap.

**`SCA-LOG-R2-HOLE` (7 lanes).** No `steer` and no `launch` of round 2 for aggregator, kake, kotoba, kumitate, kengaku, kasegi, protocol. Each has `steer <lane> -> round 1` at `2026-09-28T15:50:56-03:00` and `steer <lane> -> round 3 via shokunin-r1-<lane>` at `2026-09-28T15:52:38-03:00`, then `complete <lane> round=3` before the first `launch` of round 4. v2 bumps by exactly 1 per steer (`930502c`, `next=$((n+1)); bump`). A logged steer of round 3 with no logged steer/launch of round 2 means the step that would have stored 2 is not in this log. Cause not observed (unlogged bump, lost line, or a write outside the logger). Unknown which. The current counters were overwritten by later `launch` lines and match those lines.

The `via shokunin-r1-<lane>` suffix is in the log. The committed v2 logger at `930502c` emits `steer ${lane} -> round ${next}` without `via`, and its launch run-id is hard-coded `shokunin-r1-${lane}` even when the round number is higher. Which bytes added `via` was not found in the committed script. That does not change the round integers.

**kagi is not in that hole.** `launch kagi round=1` (L3, no `runId`/`mission` field), then `steer kagi -> round 2 via m_574d9f1f956e499dabaa59de9834bdc0` (L12), then `complete kagi round=2` (L29), then `launch kagi round=3`. Launch-verb gap `1 → 3` is filled by a steer. Terminal counter 16 still matches L257.

**`SCA-SHARED-MISSION` (1 pair, historical).** L21 `launch kengaku round=4 mission=m_5ddf2cabcef146ccb3eb1328dd1bfc8a` and L23 `launch kasegi round=4 mission=m_5ddf2cabcef146ccb3eb1328dd1bfc8a` share one mission id. v3 stores that id and stores the round from the launch argument separately, so both counters could still be 4. Current mission files are the later unique runIds in the table, not this id. Not a current counter mismatch.

**Failure verbs.** `launch-fail` 0, `lane-dead-no-report` 0. No logged failed dispatch left a counter behind an attempted round.

## Adjacent surface — not the agreement rule

Report files are what `report_of` tests (`[ -f .ufo/reports/round-$n/$lane.md ]`, line 45). They are not dispatch/completion lines. Walked at `2026-10-14T21:32:59-03:00` (`[ -f ]` + `stat`). Not re-walked at `21:35:33`.

For every lane, a report file exists at `counter+1`, and several lanes have still higher report files, with no `launch`/`complete`/`wrap` of those rounds in this log:

| Lane | Counter | Higher report present at 21:32:59 | Log line for that round |
|---|---:|---|---|
| aggregator | 10 | round 11 (14359 B, mtime `2026-10-14 18:50:11 -0300`) | none |
| kagi | 16 | round 17; also round 19 (3164 B, mtime `2026-10-14 21:21:34 -0300`) | none |
| kake | 16 | round 17; also round 19 | none |
| kama | 1 | round 2; also round 4 (mtime `2026-10-14 21:21:34 -0300`); round 3 missing | none |
| kasegi | 17 | round 18; also round 20 | none |
| kengaku | 13 | round 14; also round 16; round 15 missing | none |
| kotoba | 16 | round 17; also round 19 | none |
| kumitate | 16 | round 17; rounds 18 and 19 missing | none |
| protocol | 14 | round 15; rounds 16 and 17 missing | none |

`.ufo/reports/round-11/aggregator.md` lines 3–5 stamp `.ufo/state/aggregator.round` = 11 and `runId shokunin-r11-aggregator-r1790651969`, measurements `2026-09-29T03:26:00Z–03:38:20Z`. `grep -F 'shokunin-r11-aggregator-r1790651969' .ufo/watchdog.log` returned no match. The current counter is 10 and the log's last aggregator launch is round 10. The report text and the counter/log pair disagree with each other. That is not a disagreement between the counter and the log.

Inference, not an observation of a write: either that stamp was not a retained driver append, or a later log and counter write were replaced by the `17c1fad` snapshot now on disk. Which one is unknown. This audit does not promote report-lead into `SCA-COUNTER-LOG-MISMATCH`.

Round-2 report files are missing for the seven `SCA-LOG-R2-HOLE` lanes and present for kagi and kama. kama's round-2 report has no log dispatch; the counter is 1, which still matches the log.

## Stable ids

| Id | Count | Produces it |
|---|---:|---|
| `SCA-COUNTER-LOG-MATCH` | 9 | counter equals last `launch` round and last `wrap` round |
| `SCA-COUNTER-LOG-MISMATCH` | 0 | counter differs from last `launch` round, or from last `wrap` round when a wrap exists |
| `SCA-LOG-R2-HOLE` | 7 | no dispatch line for round 2; current counter unaffected |
| `SCA-SHARED-MISSION` | 1 pair | two round-4 `launch` lines share one `mission=` id; current mission files do not |
| `SCA-MTIME-BULK` | 10 files | counters and log share one mtime that is not a launch/wrap timestamp |
| `SCA-REPORT-LEAD` | 9 lanes | a report file exists above the counter with no log dispatch/completion; excluded from the match rule |

## Residual

- The driver script was not observed running at `21:35:33`, and `fleet-wrap` was absent. If that script were started later, v4's dead-mission branch (lines 96–98) would launch `counter+1` whenever `round-<counter>/<lane>.md` exists, and would then write a new counter. That has not happened in this log. Not a current mismatch. Not acted on.
- Log coverage of intermediate v2 bumps is incomplete (`SCA-LOG-R2-HOLE`). A later run that requires a dispatch line for every integer in `1..counter` will fail that stricter test even though the terminal integers match. This audit does not use that stricter test.
- Report files above the counter were not re-stated after `21:32:59`. A file added in that three-minute gap is unmeasured.
