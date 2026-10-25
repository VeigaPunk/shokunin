# stale2 — round-11 stale-lane actuator pass

Capture epoch: 1790635754 = 2026-09-28 19:49:14 -03:00. Tick = 450 s; stale = age > 2 ticks (900 s).
Live-set derivation: `.ufo/watchdog.log` (177 lines) launch lines at :140,:153,:156,:164,:167,:171,:173,:176; grep for `complete (kasegi round=13|kake round=13|protocol round=11|kengaku round=10|kagi round=11|kumitate round=10|aggregator round=7|kotoba round=12)` = **0 matches**; no launches newer than the set; log ends `2026-09-28T19:43:11-03:00 launch kake round=13 runId=shokunin-r13-kake-r1790635390` / `19:43:11 tick=16`.

## Mission table

| lane | round | launch | age | ticks | stale | verdict | activity pointers |
|---|---|---|---|---|---|---|---|
| kasegi | 13 | 18:27:55 | 4879s | 10 | YES | progressing | commit `7483333` 19:44:20 (depth 8→9, 705/708 audit); `corpus/lessons/round-13.md` 19:40; `LOG.md` 19:42; report committed in main repo `0933e84` 19:44:22 |
| protocol | 11 | 18:50:31 | 3523s | 7 | YES | progressing | scratch `/tmp/shokunin-r11/`: `protocol-100.md` 19:49:31, `h-{head,cand}.txt` 19:50:00; main-repo root `LOG.md` 19:27, `MISSION.md` 19:24; likely-lane commit `235b414` 19:25:03 (MISSION.md + scripts/shokunin-watchdog.sh) |
| kengaku | 10 | 18:58:02 | 3072s | 6 | YES | progressing | commit `0c51208` "round-10" 19:42:50; `LOG.md` 19:42, `SCORECARD.md` 19:40; 20+ files under `corpus/evidence/round10-fleet/` 19:30 |
| kagi | 11 | 19:13:06 | 2168s | 4 | YES | progressing | **0 commits** since launch but working tree hot: `corpus/claim-ledger.sh` 19:49, `corpus/{stamps.tsv,claim-ledger.tsv,knowledge/op-cli-surface.md}` 19:48, `lessons/round-11.md` 19:41; 10 modified + 4 untracked paths (commit sparsity ≠ silence) |
| kumitate | 10 | 19:20:37 | 1717s | 3 | YES | progressing (thin) | exactly ONE file newer than launch: untracked `scripts/round-gate.mjs` mtime 19:48:10.950 (≈65 s before capture); no commits since launch; WATCH — else silent for 28 min |
| aggregator | 7 | 19:35:39 | 815s | 1 | no | silent (so far) | zero aggregator-attributed writes: `.ufo/reports/round-7/aggregator.md` absent; `AGGREGATE.md` mtime 19:34:14 predates launch (round-6's uncommitted edit). corpus/ files newer than launch exist (19:35–19:49) but are child lanes' own rounds (kagi 19:49, kotoba 19:45–46, kake 19:37–39, kasegi 19:35–40). Age 1 tick — within round-6's ~32-min completion norm; not an alarm |
| kotoba | 12 | 19:35:40 | 814s | 1 | no | progressing | commits `4dd7753` 19:45:58 + `7d15407` 19:46:41; `verifiers/verify_corpus_integrity.py` 19:49; report landed main-repo `f9dcfd2` 19:47:54 |
| kake | 13 | 19:43:11 | 363s | 0 | no | progressing | commit `a642f93` 19:46:14 "round-12: remaining free-read verbs live-executed" (late r12 commit, post-launch); no file mtimes newer than launch yet |

## Direct answers

**Untracked files under `.ufo/reports/` right now** (`git status --porcelain .ufo/reports/`):
```
 M .ufo/reports/AGGREGATE.md
?? .ufo/reports/round-10/kotoba.md
?? .ufo/reports/round-6/aggregator.md
?? .ufo/reports/round-9/kumitate.md
```

**`complete kasegi round=13` fired?** NO. Grep across all 177 log lines returns 0 matches; no complete line has fired for ANY of the 8 live rounds and no newer launch exists. kasegi r13 (launched `2026-09-28T18:27:55-03:00 launch kasegi round=13 runId=shokunin-r13-kasegi-r1790630874`) is the oldest live mission at 10 ticks stale but demonstrably progressing (commit 19:44:20).

## Anomalies / notes

1. `AGGREGATE.md` mtime (19:34:14) predates aggregator r7 launch (19:35:39) and is an uncommitted modification from round-6 — r7 has not begun writing its dedicated paths.
2. kumitate r10 is the weakest lane: 1 file in 28 min. If next pass still shows only `round-gate.mjs` with no commit, escalate.
3. kagi r11: 4 ticks with zero commits but sustained file activity — do NOT flag silent.
4. All 6 lanes' stale flags are mechanical (age > 2 ticks); per this fleet's rhythm (completion windows 8–38 min) staleness at 3–10 ticks is normal pre-completion residency, not a hang signal. Only kumitate shows a near-silent pattern.
