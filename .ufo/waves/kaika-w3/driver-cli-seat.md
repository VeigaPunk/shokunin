# kaika driver CLI smoke — watchdog `7ea217c`

## Target and harness identity

| item | value |
|---|---|
| completed driver | `local://kaika-driver-7ea217c.sh` (copy of `.tower/worktrees/kaika/fleet-driver-retry/scripts/shokunin-watchdog.sh`) |
| driver commit | `7ea217c` |
| driver sha256 | `e56927e36cfdf0f886d48650729e5de364cb1e44a3ade58a2a3371c421071661` |
| actual census instrument | `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh` sha256 `a621fe0ec8a946430e4956353717c97a2029b9fa85b9a8721cf4f363e1beead7` |
| actual prompt template | `/home/vgpnk/Projects/shokunin/templates/round-prompt.md` sha256 `11fa6c68c1e2b01996b2c044da0e85ad9091c61454e9e28b637909574f6af27b` |
| reproducible probe | `local://kaika-driver-cli-probe.sh` sha256 `cf065d365d48974deeef207c9e3f7a32041c3571e78e7b8abce15811dec0102b` |

Run command (frozen driver copied to a filesystem path; the probe also accepts
`--repo`, `--keep`, or `WATCHDOG`):

```sh
KEEP=0 bash kaika-driver-cli-probe.sh --driver /path/to/kaika-driver-7ea217c.sh
```

Result: **46 PASS, 0 FAIL, elapsed 10 s, exit 0**, teardown reported
`leftover_owned=0 fleet_removed=yes`.

## Hypothesis and bounded scenario

Hypothesis: the CLI `main` loop, not just the sourced helpers/selftest, gates
round advancement on report **content digest**, retries the same round after the
real census returns 1, suppresses mtime-only changes, preserves report prefix
bytes, and terminates exactly the owned tagged lane group on a single advance.

Disposable fleet under `/tmp/kaika-verify/DriverCliSmoke` (unique `mktemp -d`):
`TICK_SECONDS=1`, `ROUND_CAP=2`, `MIN_REPORT_BYTES=400`, one lane
`alpha|alpha-shokunin|...`. The real `SUBSTRATE_CMD` launched a shell worker,
never `omp`. The driver and the actual census/template were copied into the
throwaway fleet; the repository was not written.

Worker sequence:

1. **Attempt 1** writes a 1015-byte report with a `## SHONEN` heading and a
   `Sources & frontier` section, plus `corpus/SOURCES.md` with an invalid
   `status=watch` enum, then exits 0.
2. The driver's real `sources-census.sh validate` returns **1** (`E07`), logs
   `sources-gate-fail`, records the report digest baseline, and relaunches the
   same round.
3. **Attempt 2** repairs only the registry enum (`watch` → `queued`), leaves the
   report bytes untouched, and waits for a release file.
4. While it waits, the probe observes ≥2 ticks, verifies round 1, the live
   tagged retry group, no completion, and that `touch -m` alone changes nothing.
5. Release makes attempt 2 append fresh report bytes and stay alive. The driver
   sees the new digest, passes the repaired census gate, TERMs the owned round-1
   group, logs exactly one advance, and launches round 2.
6. Round 2 writes no report and stays alive, so no cap completion is possible.
   Teardown kills only recorded/verified owned groups; an unrelated guard
   (`sleep 300` in its own session with a unique env tag) must survive.

## Observed output (verbatim from the final run)

```text
PASS	guard started in its own session (pid=3319108)
PASS	driver main loop started (pid=3319114 pgid=3319114)
PASS	attempt 1 worker ran and exited
PASS	real census gate failed round 1
PASS	driver logged same-round retry
PASS	second round-1 launch observed
PASS	attempt 2 repaired the registry and is waiting
PASS	actual census returns 1 for the invalid-enum registry
PASS	actual census returns 0 for the repaired registry
PASS	at least two further ticks elapsed while attempt 2 waited
PASS	round state still 1 while retry waits
PASS	attempt 2 process group is alive (pgid=3319278)
PASS	attempt 2 group carries SHOKUNIN_LANE=alpha and SHOKUNIN_ROUND=1
PASS	baseline records round 1 + the attempt-1 report digest
PASS	attempt-1 report is >= 400 bytes (1015)
PASS	attempt-1 report carries a SHONEN heading
PASS	no advancing completion was logged before release
PASS	no round-2 launch was logged before release
PASS	no cap completion was logged
PASS	at least two further ticks elapsed after mtime-only touch
PASS	mtime-only touch changed the mtime (1792455103 -> 1792455108)
PASS	mtime-only touch left report bytes unchanged
PASS	mtime-only touch left round at 1
PASS	mtime-only touch produced no completion
PASS	mtime-only touch produced no extra launch
PASS	driver advanced after fresh report bytes landed
PASS	round state became 2
PASS	round-2 worker started
PASS	exactly one completion line exists
PASS	exactly one round-2 launch line exists
PASS	round state file is 2
PASS	round-2 baseline resets to the empty-report digest
PASS	round-1 report gained fresh bytes
PASS	round-1 report prefix is byte-identical after append
PASS	attempt-2 / round-1 group was terminated (pgid=3319278)
PASS	round-2 group is alive (pgid=3319948)
PASS	round-2 group carries SHOKUNIN_LANE=alpha and SHOKUNIN_ROUND=2
PASS	unrelated guard survived the lane group kill
PASS	at least two ticks elapsed in round 2
PASS	round-2 worker left no report
PASS	no cap completion was logged after round 2
PASS	no round-2 completion was logged
PASS	round-2 worker is still alive with no report
=== identity ===
watchdog_sha256 e56927e36cfdf0f886d48650729e5de364cb1e44a3ade58a2a3371c421071661
census_sha256   a621fe0ec8a946430e4956353717c97a2029b9fa85b9a8721cf4f363e1beead7
template_sha256 11fa6c68c1e2b01996b2c044da0e85ad9091c61454e9e28b637909574f6af27b
worker_sha256   b36d50e34ee2e2aceb45d364941b8fb8980765d61d47748ec8a3ea0ab626ae01
fleet /tmp/kaika-verify/DriverCliSmoke/fleet.FsTbxf

=== census invalid fixture (actual instrument, rc=1) ===
alpha	E07	S001 status=watch

=== census repaired fleet (actual instrument, rc=0) ===
alpha	ok	/tmp/kaika-verify/DriverCliSmoke/fleet.FsTbxf/alpha-shokunin/corpus/SOURCES.md

=== worker markers ===
attempt1 pid=3319143 report_digest=c574a604396ca643e82d286e46486b4597e5645b018802319b9f22f4fc7b3709 registry_digest=b70d13ccc651e0cedae4d805d5b35fcc2696a363b5346c2f9823d32faa9064d6 at=1792455103873439231
attempt2 pid=3319281 pgid=3319278 registry_digest=0b281ce4ca6561e5d01abaf677d7c7283be1885ffe55cd1d4b6c53a8f8230adf report_digest_unchanged=c574a604396ca643e82d286e46486b4597e5645b018802319b9f22f4fc7b3709 at=1792455104900814603
attempt2 pid=3319281 appended_digest=67d923750f7c8467767c6961016f9ea281cc192a3dbd291a9751e2bc2dc05f8a at=1792455109955578446
round=2 pid=3319951 pgid=3319948 started=1792455111053389622

=== report/state ===
round_now 2
mission_now 3319948
report_size_attempt1 1015
report_digest_attempt1 c574a604396ca643e82d286e46486b4597e5645b018802319b9f22f4fc7b3709
report_digest_after_release 67d923750f7c8467767c6961016f9ea281cc192a3dbd291a9751e2bc2dc05f8a
prefix256_sha256 a078c3af6b5477ab725b183ec86c66ea90824f5fe2e24b15a0399f5c0ea91900
mtime_before_touch 1792455103
mtime_after_touch 1792455108
baseline_after_advance 2 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855

=== watchdog.log ===
2026-10-19T21:11:43-03:00 lane-dead-no-report alpha round=1; retry same round
2026-10-19T21:11:43-03:00 launch alpha round=1 pgid=3319140
2026-10-19T21:11:43-03:00 tick=1
2026-10-19T21:11:44-03:00 sources-gate-fail alpha :: alpha	E07	S001 status=watch
2026-10-19T21:11:44-03:00 advance-blocked alpha round=1 :: sources closure failed; retry same round
2026-10-19T21:11:44-03:00 launch alpha round=1 pgid=3319278
2026-10-19T21:11:44-03:00 tick=2
2026-10-19T21:11:45-03:00 tick=3
2026-10-19T21:11:46-03:00 tick=4
2026-10-19T21:11:47-03:00 tick=5
2026-10-19T21:11:48-03:00 tick=6
2026-10-19T21:11:49-03:00 tick=7
2026-10-19T21:11:51-03:00 complete alpha round=1; advancing to round=2
2026-10-19T21:11:51-03:00 launch alpha round=2 pgid=3319948
2026-10-19T21:11:51-03:00 tick=8
2026-10-19T21:11:52-03:00 tick=9
2026-10-19T21:11:53-03:00 tick=10
PASS	teardown left no owned process group, driver, or guard
PASS	disposable fleet removed
PASS	evidence directory removed

=== TEARDOWN ===
leftover_owned=0 fleet_removed=yes

=== RESULT ===
PASS=46 FAIL=0 elapsed=10s
```

Independent post-run check: `ps` found no `shokunin-watchdog`, `worker.sh`,
`SHOKUNIN_SMOKE_GUARD`, or `fleet.FsTbxf` process; `/tmp/kaika-verify/DriverCliSmoke`
was empty and the scratch run copies were removed.

## What each observation establishes

- **Real census, real rc:** `sources-census.sh validate` returned 1 on the
  invalid enum (`alpha E07 S001 status=watch`) and 0 on the repaired registry
  (`alpha ok ...`). The driver log independently shows the same E07 text in
  `sources-gate-fail`, followed by `advance-blocked ... retry same round` and a
  second `launch alpha round=1` at the same round number. No mock exit code was
  used.
- **Retry state:** during the wait, `alpha.round` remained `1`; the mission PID
  `3319278` was alive with both `SHOKUNIN_LANE=alpha` and `SHOKUNIN_ROUND=1` in
  its environ; the baseline was `1 c574a6...`; no `complete`/round-2 launch/cap
  line existed.
- **mtime is not evidence:** `touch -m` changed mtime `1792455103 → 1792455108`,
  while the report digest stayed `c574a6...`, round stayed 1, the launch count
  stayed 2, and no completion appeared across ≥2 further ticks.
- **Prefix and single advance:** after release the report digest became
  `67d923...`; the first 256 bytes stayed byte-identical (`cmp` and sha256
  `a078c3...`), exactly one `complete alpha round=1; advancing to round=2` line
  and exactly one round-2 launch appeared; `alpha.round` became `2`; the round-2
  baseline reset to the empty-stream digest `e3b0c4...`.
- **Group ownership:** the round-1 retry group `3319278` was gone after
  advancement; the round-2 group `3319948` was alive and tagged
  `SHOKUNIN_ROUND=2`; the unrelated guard stayed alive. Teardown then left no
  owned process group, driver, or guard.
- **No cap ambiguity:** round 2 wrote no report and remained alive through ≥2
  ticks; no `cap alpha` or round-2 completion was logged.

## Limitations

- The lane work is a controlled shell worker under the real `SUBSTRATE_CMD`
  launcher; this verifies driver CLI/gating/lifecycle behavior only, not an
  agent substrate or real lane content.
- The invalid-enum registry is deliberately synthetic (`status=watch`). The
  direct rc=1 capture uses a census root containing a byte-identical copy of the
  attempt-1 registry, because attempt 2 repairs the live fleet registry in the
  same tick window. The driver's own census invocation is still evidenced by
  the logged E07 output and the same-round retry.
- Timing is scaled down (`TICK_SECONDS=1`, `ROUND_CAP=2`, one lane, 90 s
  internal deadline). mtime is compared at whole-second resolution; the probe
  sleeps >1 s before the touch, then waits ≥2 ticks.
- Lifecycle is observed by sampling `/proc/<pid>/environ`, `ps` process-group
  membership, and state files at bounded instants. Zombie-only groups are
  treated as dead. All signalled groups are recorded from the driver's own
  mission file or launch log and tag-checked before teardown; no unrelated PID
  is discovered or killed.
- The driver's stdout/stderr were empty in this run; the lane's `alpha.out`
  contains only `Terminated sleep 0.1`, caused by the driver's TERM of the
  retry group.
- Earlier harness attempt note: the first harness version did not pre-create
  the lane repository directory, so the driver correctly logged
  `launch-fail ... cwd missing`; the harness now creates `alpha-shokunin/`
  before starting the driver. That failure was 100% harness setup, not a driver
  result, and is not part of the 46 PASS run above.
- No repository edits, commits, broad tests, or linters were performed. The
  disposable fleet and evidence were removed; use `--keep` to retain them for
  inspection.
