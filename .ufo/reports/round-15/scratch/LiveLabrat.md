# Round-15 LiveLabrat host probes

## Port check

Command: `shuf -i 20000-65000 -n 1`

Observed: `43313`.

Started only a scratch listener in `/tmp`:

```
python3 -m http.server 43313 --bind 127.0.0.1 --directory /tmp
Serving HTTP on 127.0.0.1 port 43313 (http://127.0.0.1:43313/) ...
```

Exact listener detection:

```
ss -ltn 'sport = :43313'
State Recv-Q Send-Q Local Address:Port Peer Address:Port
LISTEN 0 5 127.0.0.1:43313 0.0.0.0:*
```

Exact gate-style detection while the scratch listener was up:

```
ss -ltnH | awk '$4 ~ /:43313$/ {n++} END{print "43313-listeners=" n+0}'
43313-listeners=1
```

40961 absent today, using the same form:

```
ss -ltnH | awk '$4 ~ /:40961$/ {n++} END{print "40961-listeners=" n+0}'
40961-listeners=0
ss -ltn 'sport = :40961'
State Recv-Q Send-Q Local Address:Port Peer Address:Port
ss -tn 'dport = :40961'
State Recv-Q Send-Q Local Address:Port Peer Address:Port
```

No HTTP request was made to 40961. The handler was never started or stopped.

Cleanup command and proof:

```
pkill -TERM -f 'http.server 43313'
```

Both scratch service slots reported stopped; afterward:

```
ss -ltn 'sport = :43313'
State Recv-Q Send-Q Local Address:Port Peer Address:Port
```

The post-kill socket listing was empty. A final `pgrep -af 'http.server'` showed an unrelated pre-existing listener on port 40993; it was not started by this probe and was not touched.

## Aggregate gate timings

All commands ran from `/home/vgpnk/projects/shokunin/kagi-shokunin`, as `bash -c 'time bash corpus/<gate>.sh'`:

```
surface-census.sh: exit 0; real 0m0.261s
SURFACE_CENSUS: CLEAN (assets=20 runtime=15 scanned=4 ok=34 absent=2 skipped=0)

drift-pins.sh: exit 0; real 0m0.080s
DRIFT_PINS: CLEAN (files=15 symbols=20)

op-ref-probe.sh: exit 0; real 0m0.245s
OP_REF_PROBE: CLEAN (checks=44 oprun=12 refs=7 divergent=5 edge=10 sig=6)

transcript-scan.sh: exit 1; real 0m1.208s
TRANSCRIPT_SCAN: HITS=2 (cells=888 patterns=32+5 warns=2 schema-absent=0) db=/home/vgpnk/.local/state/the-janitor/xdg-data/opencode/opencode.db
```

The transcript-scan exit 1 is its documented hit verdict. Default checklist verify was also timed:

```
real 0m2.229s
CHECKLIST_RATIO: runnable=9/16 floor=8 by_hand=7
CHECKLIST_RUN: CLEAN (items=16 runnable=9 by_hand=7 failed=0 skipped=0)
```

## Scheduler survey

`systemctl --user list-timers --all` listed exactly:

```
ai-usage.timer       ai-usage.service
webzites-probe.timer webzites-probe.service
charter-scribe.timer charter-scribe.service
3 timers listed.
```

`systemctl --user cat ai-usage.timer webzites-probe.timer charter-scribe.timer` showed those three unrelated service targets. `grep` over `/home/vgpnk/.config/systemd/user/` for `corpus|kagi-shokunin|shokunin` returned `No matches found`.

Observed cron/at facts:

```
crontab -l: error: command not found: crontab
atq: error: command not found: atq
type -a anacron: type: anacron: not found
dpkg -l 'cron*' ... installed count: 0
```

`/etc/crontab`, `/etc/cron.d`, `/etc/cron.daily` were absent. `/etc/cron.hourly` contained only `snapper`; no repo gate references were found. `/var/spool/cron` and `/var/spool/atjobs` were absent. Therefore no observed systemd user timer, cron entry, or at-job schedules any `corpus/*.sh` gate.

## Checklist gate selftest and list

Gate landed before these commands.

From repo root:

```
bash corpus/checklist-run.sh --selftest
CHECKLIST_SELFTEST: PASS (28 cases)
exit=0
```

The same relative command from `/tmp` and `/home/vgpnk` returned exit 127 (`bash: corpus/checklist-run.sh: No such file or directory`), because the relative path is cwd-relative. Using the absolute gate path, from two different foreign cwds:

```
cd /tmp && bash /home/vgpnk/projects/shokunin/kagi-shokunin/corpus/checklist-run.sh --selftest
CHECKLIST_SELFTEST: PASS (28 cases)
exit=0

cd /home/vgpnk && bash /home/vgpnk/projects/shokunin/kagi-shokunin/corpus/checklist-run.sh --selftest
CHECKLIST_SELFTEST: PASS (28 cases)
exit=0
```

Additional absolute-path selftests from `/` also passed with the identical line. Wall times were 1.68–1.71s. This establishes cwd-independent gate behavior when invoked by its absolute path.

`--list` from repo root:

```
bash corpus/checklist-run.sh --list
CHECKLIST_LIST: rows=16 runnable=9 by_hand=7
exit=0
```

Default verify from repo root and absolute-path verify from `/tmp` both exited 0 with:

```
CHECKLIST_RATIO: runnable=9/16 floor=8 by_hand=7
CHECKLIST_RUN: CLEAN (items=16 runnable=9 by_hand=7 failed=0 skipped=0)
```
