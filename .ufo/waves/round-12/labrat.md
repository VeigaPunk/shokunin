# labrat r12 — two read-only falsification probes (H1 liveness clause, H2 round-14 termination)

## H1 — the liveness-probe clause still holds

**Claim under test** (PROTOCOL.md:224-226): «Liveness probes are not evidence of an open mission:
`ufo-sighting status --lite` still lists a mission after the driver `complete`d it (§Appendix,
"Liveness probes"), so the driver's `live` test can never fail while its daemon is up and its
`lane-dead-no-report` retry path is unreachable.»

**Verb discovery.** The brief's guesses miss: `command -v ufo-sighting` → empty; `type -a ufo-sighting`
→ `not found` (exit 1); `ls ~/projects` → no `ufo*` dir (only cowremakerpg, memes, pocketmonstah,
shokunin, urf). The real verb is pinned by the driver itself, `scripts/shokunin-watchdog.sh:8`:
`UFO=/home/vgpnk/Projects/origin-work/ufo-fsd-alpha/scripts/ufo-sighting` — exists:
`-rwxr-xr-x 1 vgpnk vgpnk 12096 Sep 27 15:39`. The driver's live test is `shokunin-watchdog.sh:89,92`:
`status=$("$UFO" status --lite 2>/dev/null || true)` then
`live=0; [ -n "$mid" ] && printf '%s' "$status" | grep -q "$mid" && live=1`, where `$mid` is the
**runId** written to `.ufo/state/<lane>.mission` at launch (`:78`) — it greps raw JSON, not status.

**Probe** (read-only `status --lite`; exact reproduction of the driver's grep against all 12
post-20:10 runIds — 4 completed + 8 live):

```
$ /home/vgpnk/Projects/origin-work/ufo-fsd-alpha/scripts/ufo-sighting status --lite | <grep loop>
MATCH   shokunin-r7-aggregator-r1790634938   (complete @20:13:17, log:189)
MATCH   shokunin-r11-kagi-r1790633585        (complete @20:13:19, log:191)
MATCH   shokunin-r11-protocol-r1790632230    (complete @20:28:20, log:195)
MATCH   shokunin-r12-kotoba-r1790634939      (complete @20:28:22, log:197)
MATCH   shokunin-r14-kasegi-r1790635842      (live, log:179)
MATCH   shokunin-r11-kengaku-r1790635843     (live, log:181)
MATCH   shokunin-r14-kake-r1790636745        (live, log:185)
MATCH   shokunin-r11-kumitate-r1790636746    (live, log:187)
MATCH   shokunin-r8-aggregator-r1790637197   (live, log:190)
MATCH   shokunin-r12-kagi-r1790637199        (live, log:192)
MATCH   shokunin-r12-protocol-r1790638100    (live, log:196)
MATCH   shokunin-r13-kotoba-r1790638102      (live, log:198)
```

All four missions the driver `complete`d after 20:10 **still match** the driver's live grep. The
`completed` array retains them verbatim, e.g.:

```json
{ "missionId": "m_9e47463dc8834f5ebb13ee91cf3affff", "title": "r11:protocol",
  "runId": "shokunin-r11-protocol-r1790632230", "sessionId": "sess-protocol-1790632230",
  "completedAt": "2026-09-28T23:28:20.555Z", "finalNote": "round 11 complete",
  "status": "completed", "missionLive": false, "phase": "completed", ... }
```

`completedAt` 23:28:20.555Z ≡ 20:28:20-03:00 — exactly the watchdog's `complete protocol round=11`
line (log:195). Same for the other three (23:13:17Z, 23:13:19Z, 23:28:22Z). Header counts verbatim:
`"statusCounts": {"stopped": 3, "completed": 50, "running": 18}`, `"missionCount": 18`, windows:
`"shokunin" activeMissions 8` (= the 8 live launches). Dead-lane counter still zero:
`grep 'lane-dead-no-report' .ufo/watchdog.log` → No matches found (200 lines now; tick=23 @20:35:53).

**Caveat:** retention is budget-bounded, not eternal — header shows `"manifestBudget": {"evictedCompleted": 182, "at": "2026-09-28T23:37:08.470Z"}`. Under eviction pressure a completed runId could fall out and `live` could go 0; today all 4 recent + even round-5-era completions (`r5:aggregator`) are still listed, so the clause holds in practice.

**H1: CONFIRMED** — the r10 appendix row stands; the driver's `live` test is blind to completion while the daemon is up (`:95` `elif [ "$live" -eq 0 ]` branch unreachable for this failure mode).

## H2 — no round-14 lane-round has terminated

- `grep 'complete .*round=14' .ufo/watchdog.log` → **No matches found**. The only `round=14` lines
  are the two launches: `179|…19:50:43-03:00 launch kasegi round=14 runId=shokunin-r14-kasegi-r1790635842`
  and `185|…20:05:46-03:00 launch kake round=14 runId=shokunin-r14-kake-r1790636745`.
- Reports: `glob .ufo/reports/round-14/**` → **No files found** (both `*` and `**` patterns). The
  directory exists but empty — it is launch-time scaffolding: `lane_prompt()` runs
  `mkdir -p "$SK/.ufo/reports/round-$n"` at every launch (`shokunin-watchdog.sh:48`). Control:
  `.ufo/reports/round-13/` holds exactly `kake.md`, `kasegi.md` — the two lanes whose r13 completed
  (log:178 kasegi @19:50:42, log:184 kake @20:05:45).
- Counters agree: `cat .ufo/state/kasegi.round .ufo/state/kake.round` → `14` / `14` (counter==N means
  round N launched, `:79`; termination would show counter passing to 15). No other lane is at r14.

**Conclusion:** per PROTOCOL (write the `rounds[]` entry for round N as soon as one lane's Nth
lane-round terminates) — **no `rounds[14]` entry is warranted yet**. kasegi r14 (~50 min in) and
kake r14 (~35 min in) are still open; an empty round-14 report dir must not be misread as progress.

## Verdicts

- H1 | confirmed | all 4 post-20:10 completed runIds (incl. `shokunin-r11-protocol-r1790632230`, completedAt 23:28:20Z) still MATCH the driver's own `status --lite` grep — Closure pass may keep treating `in-flight` as absence-of-complete-line/report, never a status probe.
- H2 | confirmed (no termination) | `complete .*round=14` → no matches; `round-14/` empty; counters kasegi/kake = 14 — no `rounds[14]` entry in this closure pass.

## Gaps

- Full `status --lite` is 3,151 lines; I verified via the driver's exact grep (`grep -q "$rid"`) plus verbatim sampled entries, not a line-by-line read of every mission row (full output preserved in artifact://85).
- `lane-dead-no-report`=0 confirms unreachability only observationally; I did not (and may not) run `complete`/`steer`/`remove`/`kill` to exercise the dead-lane branch.
- Eviction-pressure behavior (`evictedCompleted: 182`) is untested — whether `live` can eventually go 0 for a completed lane under manifest budget churn is unresolved and only matters if eviction outpaces respawn.
- watchdog.log is concurrently appended (200 lines at probe time, tick=23 @20:35:53); counts are as-of that instant, later ticks may add lines.
