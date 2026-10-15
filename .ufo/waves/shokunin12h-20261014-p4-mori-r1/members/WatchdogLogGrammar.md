# Watchdog log line grammar (advisory data)

Seat: `WatchdogLogGrammar`. Read-only. Not a judge verdict, receipt, or admission. mori detects and reports; this file does not restart, kill, steer, or rewrite the log.

## Surface

| Fact | Value |
|---|---|
| Path | `/home/vgpnk/Projects/shokunin/.ufo/watchdog.log` |
| Measured | `2026-10-14T21:35:31-03:00` (`date -Is` immediately before the census `awk`) |
| Bytes | `19396` (`stat -c '%s %y'`) |
| mtime | `2026-10-13 16:44:48.524089950 -0300` |
| Lines | `294` (`wc -l`); `0` blank (`grep -c '^$'`) |
| SHA-256 | `c16382b5a59c956d57d96fddaeb288f429998b7693b029d058877d4ca0dc1798` (`sha256sum`) |
| Git | identical to `HEAD:.ufo/watchdog.log` (blob `5423397e46baee780490c1cda5754f822a6428a3`, commit `17c1fad`, `2026-09-29T00:19:02-03:00`) |
| Last event in the file | `2026-09-28T23:55:00-03:00 tick=3` (line 294) |
| Dates present | `2026-09-28` only. `grep -c '2026-09-29'` → `0`. `grep -c '2026-10'` → `0`. Measured `2026-10-14T21:35:56-03:00` |

Every line matches `YYYY-MM-DDTHH:MM:SS-03:00` plus one space. Non-`-03:00` offsets: `0`. NUL: `0`. CR: `0`.

**WDG-G-FILE-FROZEN.** mtime is 15 days after the last event, and the bytes match the `17c1fad` blob. This census is that frozen file, not a live tail. Lines other reports quote after `2026-09-28T23:55:00-03:00` are absent here (`unavailable` in this surface, not a failure). Do not reconstruct them.

Writer cited below is `scripts/shokunin-watchdog.sh` at HEAD, which matches the worktree (`git diff` empty; blob `6ade1aaebb0c09e7f9c7ab900b00c51821d77aed`). Header: `shokunin-watchdog v4`. `INTERVAL=450`. `MAX_ROUNDS=1024`. `LANES="protocol aggregator kasegi kengaku kake kumitate kotoba kagi kama"`.

## Prefix rule

**WDG-G-PREFIX-RULE.** After the timestamp, the grammar prefix is:

1. `watchdog tick` if the remainder starts with those two words (field 2 alone is `watchdog`).
2. `tick=` if the remainder is `tick=<digits>` (the integer is payload; a new `tick=40` is the same prefix).
3. Otherwise field 2, the first whitespace token (`launch`, `steer`, `complete`, `wrap`, …).

Naive field 2 without collapsing `tick=<N>` yields **44** tokens. That set is listed below so a later run can compare either reading. The grammar decomposition is the **6** prefixes. They cover `294/294` lines. No unlisted prefix.

Classify with field 2 (plus the two special cases). Do not classify by substring.

**WDG-G-COMPLETE-SUBSTRING.** `awk '$2=="complete"'` → `95`. `grep -c 'complete'` → `117`. The extra `22` are `wrap` lines, whose body contains the word `complete`. A substring search is not the completion prefix.

## Observed grammar prefixes

Census command (this is the count):

```sh
awk '
{
  ts=$1
  rest=substr($0, length(ts)+2)
  if (rest ~ /^watchdog tick /) p="watchdog tick"
  else if (rest ~ /^tick=[0-9]+$/) p="tick="
  else { split(rest, a, " "); p=a[1] }
  c[p]++
  if (!(p in first)) { first[p]=ts; firstline[p]=NR }
  last[p]=ts; lastline[p]=NR
  n++
}
END {
  print "lines", n
  print "grammar_prefixes", length(c)
  split("watchdog tick|steer|launch|complete|wrap|tick=", order, "|")
  print "PREFIX\tCOUNT\tFIRST_LINE\tFIRST_TS\tLAST_LINE\tLAST_TS"
  for (i=1; i<=6; i++) {
    p=order[i]
    printf "%s\t%d\t%d\t%s\t%d\t%s\n", p, c[p], firstline[p], first[p], lastline[p], last[p]
    delete c[p]
  }
  for (p in c) printf "UNLISTED\t%s\t%d\n", p, c[p]
}
' .ufo/watchdog.log
```

Run at `2026-10-14T21:35:31-03:00` from `/home/vgpnk/Projects/shokunin`. Output:

```
lines 294
grammar_prefixes 6
PREFIX	COUNT	FIRST_LINE	FIRST_TS	LAST_LINE	LAST_TS
watchdog tick	1	1	2026-09-28T15:44:59-03:00	1	2026-09-28T15:44:59-03:00
steer	15	2	2026-09-28T15:50:55-03:00	18	2026-09-28T15:52:38-03:00
launch	97	3	2026-09-28T15:50:56-03:00	268	2026-09-28T23:15:05-03:00
complete	95	20	2026-09-28T15:56:51-03:00	267	2026-09-28T23:15:03-03:00
wrap	22	270	2026-09-28T23:39:54-03:00	293	2026-09-28T23:55:00-03:00
tick=	64	10	2026-09-28T15:50:56-03:00	294	2026-09-28T23:55:00-03:00
```

No `UNLISTED` row. `1+15+97+95+22+64 = 294`.

| Id | Prefix | Count | Class | Not |
|---|---|---:|---|---|
| WDG-G-LAUNCH | `launch` | 97 | **launch** | not a completion; not a failure |
| WDG-G-COMPLETE | `complete` | 95 | **completion** | not a launch; not a failure; not a quality verdict |
| WDG-G-WRAP | `wrap` | 22 | **completion** (respawn suppressed) | not a launch; not a failure; not a kill |
| WDG-G-STEER | `steer` | 15 | neither | not a launch, completion, or failure |
| WDG-G-TICK | `tick=` | 64 | neither | not a launch, completion, or failure; a reset is not a failure |
| WDG-G-WATCHDOG-TICK | `watchdog tick` | 1 | neither | v1 heartbeat only |

**WDG-G-NO-FAILURE-PREFIX.** No observed prefix is a failure. `grep -cE 'launch-fail|lane-dead-no-report|marker-suspect'` → `0` (measured `2026-10-14T21:35:56-03:00`).

## Literal field-2 inventory

`awk '{ c[$2]++ } END { for (k in c) print c[k], k }' .ufo/watchdog.log | sort -k2`, same measurement window. 44 tokens. The 39 `tick=<N>` rows are one grammar prefix.

| field 2 | count | grammar prefix |
|---|---:|---|
| `complete` | 95 | `complete` |
| `launch` | 97 | `launch` |
| `steer` | 15 | `steer` |
| `watchdog` | 1 | `watchdog tick` |
| `wrap` | 22 | `wrap` |
| `tick=1` | 8 | `tick=` |
| `tick=2` | 4 | `tick=` |
| `tick=3` | 4 | `tick=` |
| `tick=4` | 3 | `tick=` |
| `tick=5` | 3 | `tick=` |
| `tick=6` … `tick=13` | 2 each (8 values, 16 lines) | `tick=` |
| `tick=14` … `tick=39` | 1 each (26 values, 26 lines) | `tick=` |

`tick=1` through `tick=39` are all present. No other field-2 token exists. `8+4+4+3+3+16+26 = 64`.

## Templates inside each prefix

Every line matched exactly one template (`awk` normalizer, same file, `2026-10-14T21:34:29-03:00`). Lane alternation used: `protocol|aggregator|kasegi|kengaku|kake|kumitate|kotoba|kagi|kama`. No other lane token.

| Count | Template | Class |
|---:|---|---|
| 1 | `watchdog tick (live-missions-in-last-status≈<n>)` | neither |
| 7 | `steer <lane> -> round <N>` | neither |
| 8 | `steer <lane> -> round <N> via <token>` | neither |
| 1 | `launch <lane> round=<N>` | launch (attempt; see below) |
| 3 | `launch <lane> round=<N> mission=<id>` | launch |
| 93 | `launch <lane> round=<N> runId=<id>` | launch |
| 95 | `complete <lane> round=<N>; respawning` | completion |
| 22 | `wrap <lane> round=<N> complete; NOT respawning (fleet-wrap)` | completion |
| 64 | `tick=<N>` | neither |

Suffixes are invariant in this file: every `complete` line ends `; respawning`; every `wrap` line ends `complete; NOT respawning (fleet-wrap)`. `mission=none`: `0`.

Id shapes observed, not a second prefix:

- `runId=` (93/93): `shokunin-r<N>-<lane>-r<unix>`.
- `mission=` (3/3): `m_` plus 32 hex digits. Example line 21, `2026-09-28T15:56:52-03:00`.
- `via` token (8): seven are the literal fallback `shokunin-r1-<lane>`; one (kagi, line 12) is `m_` plus 32 hex.

## What each prefix means

Meaning is the emitter that wrote that shape, not a health verdict. Where the log line precedes the commit that first contains the format string, the running script was ahead of git. Commit time is not the format epoch.

### `watchdog tick` — neither

**Emitter:** `3ff12e0` (`2026-09-28T15:37:24-03:00`) `scripts/shokunin-watchdog.sh:40`. v1 sleeps `INTERVAL` (450) first, counts `grep -c 'running'` on `ufo-sighting status --lite`, then appends:

```
watchdog tick (live-missions-in-last-status≈$live)
```

The `≈` is a fixed format character, not a rounding mark. The only payload is `64` (line 1). v1 logged this instead of per-lane events. It relaunched missing `r1:<lane>` titles and did not log those launches. Removed in `930502c`.

### `steer` — neither

**Not a launch.** v2 (`930502c:53-68`, commit `2026-09-28T15:50:39-03:00`) takes this branch only when `status` already contains `r1:<lane>`. It bumps the round counter and calls `ufo steer`. It does not check a report file and does not complete a mission.

- Bare form, 7 lines, `15:50:55`–`15:50:56`: emitter `930502c:68`, `steer ${lane} -> round ${next}`. No mission token.
- `via` form, 8 lines, all at `15:52:38`: format first committed in `9751cd4:71` (`2026-09-28T15:52:57-03:00`), 19 s after the lines. `via` is the string passed to `ufo steer`: state-file mission id, or the fallback `shokunin-r1-<lane>` when that file is missing (`9751cd4:69`). A `shokunin-r1-<lane>` token is the fallback literal, not evidence a mission id was read. Steer also ignores steer failure (`|| true`), so the line is not proof the steer call succeeded.

Last steer is line 18. No later line uses this prefix. Current v4 does not emit it.

### `launch` — launch

Three emitters, three shapes. All are launch-class. Only the later two are success-gated.

**WDG-G-BARE-LAUNCH-UNCONDITIONAL.** The one bare line (`launch kagi round=1`, line 3, `15:50:56`) matches `930502c:64`, which echoes `launch` after `ufo launch ... >/dev/null 2>&1 || true`. That shape means the driver attempted a launch because `r1:kagi` was absent. It does not mean the launch succeeded. No `complete` and no `wrap` exists for `(kagi, 1)` in this file. That absence is not a failure prefix.

`mission=` (3 lines, `15:56:52`–`15:56:54`, kengaku/kasegi/protocol round 4): `9751cd4:66` logs `launch ... mission=${mid:-none}` even when `mid` is empty. `655a41d:89` (`2026-09-28T15:57:01-03:00`, v3) logs `launch ... mission=${mid}` only when a `missionId` was parsed, else `launch-fail`. These 3 lines carry a real `m_` id, not `none`, and sit 7–9 s before `655a41d`. [INFERENCE] both emitters produce this shape when a mission id was parsed. Which binary wrote them is not unique. They are still launch lines.

`runId=` (93 lines, first line 28 at `16:02:12`): committed emitter begins at `c8f9f57:86-89` (`2026-09-28T16:29:51-03:00`) and is unchanged through HEAD (`scripts/shokunin-watchdog.sh:78-81`):

```sh
if printf '%s' "$out" | grep -q 'activeMissions\|"ok":true'; then
  echo "$(date -Is) launch ${lane} round=${n} runId=${rid}" >> "$SK/.ufo/watchdog.log"
```

`rid` is `shokunin-r${n}-${lane}-r${ts}` with `ts=$(date +%s)`. Of the 93 `runId=` lines, `18` have a timestamp before `2026-09-28T16:29:51` and `75` are at or after it (`awk` split on that timestamp, `2026-10-14T21:34:29-03:00`). The 18 predate the commit that contains the success grep. [INFERENCE] the running script already used this shape; do not treat those 18 as proof the committed grep matched. The 75 match the committed success branch's format. Zero `launch-fail` siblings means this file never recorded the else branch, not that every launch attempt succeeded.

### `complete` — completion

**Emitter:** v3 `655a41d:112-115`, still HEAD `scripts/shokunin-watchdog.sh:103-109`. Logged when the mission id is still in `status` and `report_of` is true, and (when fleet-wrap exists) the wrap branch was not taken, and `n < MAX_ROUNDS`. The driver then calls `ufo complete --note "round $n complete"` (`|| true`) and launches `n+1`.

This is the driver's completion signal: a report path existed. It is not a quality, SHONEN, or commit verdict.

`report_of` changed underneath the same prefix:

- `655a41d:39`: file exists at `round-$n/<lane>.md` **or** `round-$n/<lane>-shokunin.md`.
- `609ecb6:44` (`2026-09-28T17:38:25-03:00`) through HEAD:45: only `round-$n/<lane>.md`.

[INFERENCE] a `complete` line means "the driver's then-current `report_of` was true." It does not, by itself, say which of the two filenames, for lines before that predicate narrowed. All 95 observed lines share the suffix `; respawning`. `95` lines, `95` distinct `(lane, round)` pairs. This prefix does not repeat a pair in this file: the following `launch` advances the counter and replaces the mission id, so the next tick is not in the same branch.

Eight `complete` lines have no earlier `launch` of that same `(lane, round)` (the v2 steer era bumped the counter without a `launch` line): aggregator/kake/kotoba/kumitate round 3, kasegi/kengaku/protocol round 3, kagi round 2. Those completions are still `complete` lines. They are not evidence of a missing launch prefix.

### `wrap` — completion, respawn suppressed

**Emitter:** `f5d8507:103-106` (`2026-09-28T23:41:38-03:00`), same at HEAD:103-106. Branch: mission still live, `report_of` true, file `.ufo/fleet-wrap` exists. Calls `ufo complete` with note `fleet wrap: round $n landed, not respawning`, then logs wrap. Does not call `launch_lane`.

First wrap line is `270` at `2026-09-28T23:39:54-03:00`, 104 s before commit `f5d8507`. [INFERENCE] same pre-commit running-script gap as `runId=`. The format string matches that commit and HEAD.

**WDG-G-WRAP-MULTIPLICITY.** `22` lines, `9` unique `(lane, round)` pairs:

| pair | lines |
|---|---:|
| `aggregator round=10` | 2 |
| `kake round=16` | 2 |
| `kagi round=16` | 2 |
| `protocol round=14` | 1 |
| `kama round=1` | 3 |
| `kasegi round=17` | 3 |
| `kengaku round=13` | 3 |
| `kotoba round=16` | 3 |
| `kumitate round=16` | 3 |

The emitter sits in the per-tick loop and does not clear the condition, so the same pair is re-logged on later ticks while status still contains the mission id and the report file is still there. `22` is not `22` completions. A later comparison key is `(lane, round)`, not the line count. None of these 9 pairs also has a `complete` line. kama's only terminal prefix is `wrap` (launch 1, complete 0, wrap 3). That is a completion, not a failure and not a kill.

Earlier committed snapshot `609ecb6:.ufo/watchdog.log` (117 lines) has no `wrap` prefix (`42 complete`, `43 launch`, `15 steer`, `16 tick=`, `1 watchdog tick`). `17c1fad` shows `177` insertions and `0` deletions on this path. Current counts are the full file, not that snapshot.

### `tick=` — neither

**Emitter:** `930502c:71` onward, HEAD:114. Once per loop, after the lane sweep, before `sleep 450`. `tick` starts at `0` each process and increments first, so `tick=1` is the first heartbeat of a process, not round 1 and not a failure.

Eight `tick=1` lines (`awk '$2=="tick=1"' | wc -l` → `8`). Each is a process start of a script that emits this prefix. Inter-tick gaps are not a prefix. Several gaps are not 450 s (restarts, and ticks that include launch work). A gap is not `lane-dead-no-report`.

## Failure prefixes: defined, not observed

Current script, and every commit from `655a41d` through HEAD, can append two failure lines. Both counts in this file are `0`.

**WDG-G-LAUNCH-FAIL-ABSENT.** `launch-fail`. HEAD:83:

```sh
echo "$(date -Is) launch-fail ${lane} round=${n} :: $(printf '%s' "$out" | tail -2)" >> "$SK/.ufo/watchdog.log"
```

Class: **failure**. Else branch of the launch success grep (`activeMissions` or `"ok":true` absent from `ufo launch` output). v3 (`655a41d:91`) used the same prefix when no `missionId` was parsed. Not a launch line and not a completion line. The `::` tail is the last two lines of launcher output, unsanitized.

**WDG-G-LAUNCH-FAIL-MULTILINE.** `tail -2` keeps an internal newline, and `echo` writes it. One `launch-fail` event can occupy two physical lines; the second has no timestamp and would not match the prefix rule. Unobserved here (count `0`). A physical-line census equals an event census only while this prefix is absent. A later run that sees a non-timestamp line must join it to the preceding `launch-fail` before counting prefixes.

**WDG-G-LANE-DEAD-ABSENT.** `lane-dead-no-report`. HEAD:96-101. Class: **failure**. Mission id is not in `status`, and `report_of` is false. Comment in v3: mission gone before report. The line says `retry same round` and is followed by `launch_lane` of the same `n` (which may then log `launch` or `launch-fail`). It is not itself a launch or a completion. Count `0` in this file, and `0` in the `609ecb6` blob. Absence of this prefix is not proof no mission died: v2 did not emit it, and a death that coincided with a report file takes the relaunch path with no failure line.

## Not prefixes

**WDG-G-MARKER-SUSPECT-NOT-EMITTED.** `.ufo/reports/round-12/protocol.md:397` proposes `marker-suspect <lane> round=<N> bytes=<size>` inside a replacement `report_of()`. The report says `scripts/` is operator-side and the correction was not landed. `git log -S 'marker-suspect' -- scripts/shokunin-watchdog.sh` is empty. Count in the log: `0`. Not an observed prefix and not a current emitter. Do not treat a short report as this line.

Silent branches, also not prefixes (no line is written):

- Mission live, report not yet present: only the loop's `tick=` line. HEAD:96-112 does not log a per-lane waiting line.
- Report present, `n >= 1024`, and `.ufo/fleet-wrap` absent: the `elif [ "$n" -lt "$MAX_ROUNDS" ]` fails with no log line (HEAD:107-110). Max `round=` / `round ` integer in this file is `17` (`grep -oE 'round=?[0-9]+' | grep -oE '[0-9]+' | sort -n | tail -1`). That cap branch is not exercised here. [INFERENCE] no line was omitted for the cap.

## Lane × prefix

`awk` field split on the remainder, same file, `2026-10-14T21:34:29-03:00`. `tick=` and `watchdog tick` have no lane.

| lane | steer | launch | complete | wrap lines |
|---|---:|---:|---:|---:|
| protocol | 2 | 11 | 11 | 1 |
| aggregator | 2 | 7 | 7 | 2 |
| kasegi | 2 | 14 | 14 | 3 |
| kengaku | 2 | 10 | 10 | 3 |
| kake | 2 | 13 | 13 | 2 |
| kumitate | 2 | 13 | 13 | 3 |
| kotoba | 2 | 13 | 13 | 3 |
| kagi | 1 | 15 | 14 | 2 |
| kama | 0 | 1 | 0 | 3 |

kagi's launch/complete gap is `(kagi, 1)` bare launch with no terminal line, plus `(kagi, 16)` closed by `wrap` rather than `complete`, plus one steer-era `complete` of round 2 with no `launch` line. kama has no `complete` line; its round 1 is closed by `wrap`. Neither gap is a failure prefix.

## Observation / inference / unknown

**Observed.** Six grammar prefixes, 44 field-2 tokens, nine templates, counts and commands above. Failure prefixes and `marker-suspect` have count 0. File digest matches HEAD. Last event is `2026-09-28T23:55:00-03:00`.

**Inference.** Format lines that precede the commit containing that format string were written by a not-yet-committed script (`via` by 19 s, `mission=`/`complete` by about 10 s, `runId=` by about 27 min, `wrap` by 104 s). `wrap` line count overcounts completions. `complete` means the driver's file-existence check, not a good round. Eight `tick=1` lines are process starts.

**Unknown.** Which binary wrote the three `mission=` lines and the 18 early `runId=` lines. Whether any `launch-fail` or `lane-dead-no-report` line was written to a worktree tail that was never committed (this file and both committed blobs have none; reports that quote `2026-09-29` lines are not this surface). Whether a future append will use a seventh prefix. The cap-silence branch is unexercised, so its "no line" behavior is source-derived, not log-derived.
