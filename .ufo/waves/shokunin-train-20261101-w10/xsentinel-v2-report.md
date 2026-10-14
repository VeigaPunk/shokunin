# xsentinel-v2 — wave-10 post-landing hygiene audit

Seat: fleet-xsentinel-v2 (LEAF). Scope audited: audio-shokunin (r71), game-dev-2d-shokunin
(r70), game-dev-3d-shokunin (r79), fleet dir `.ufo/waves/shokunin-train-20261101-w10/`.
Audit window: 2026-10-14 ~11:05–11:30 local. **The wave was landing live during audit**:
audio `5415115 report-last`, g2d `16d003c` + `d9ae207`, g3d `3f9e070` all committed
mid-audit, so findings distinguish swept-vs-residual states with commit refs.

## Findings

### F1 — HIGH — closeout `git add -A` swept regenerable snapshot/scratch residue into committed history (ignore-list name side-channel, again)

Repos' own declared policy: `corpus/.gitignore` comments say snapshot trees are
"regenerable; never track" and iteratively ban `tree/frozen/*tree*/head/snapshot/base/
*extract*`. Two names still evade the list, and bytecode has never been covered:

- **audio-shokunin `5415115` (report-last, 1923 files / +344k lines)** swept:
  - `corpus/live/r70-baseline/measure-env/` — **776 files**, a full repo snapshot
    (copies of `corpus/fixtures/*.py`, `corpus/artifacts/*.wav`, nested `corpus/live/runs/*`,
    `round-60/executor/…`). `measure-env` matches no ignore rule
    (`git check-ignore` → exit 1). Same class as w8-F4's `head/snapshot/base/extract` bans;
    the committed `corpus/live/r69-baseline/measure-env/` and `r69-verifier/measure-env/`
    (tracked in HEAD) show this is now the *second* wave it landed.
  - `corpus/live/runs/` — 352 receipt dirs swept wholesale (audio has no
    `corpus/live/.gitignore`; g2d has `runs/` in one, audio does not).
  - `corpus/live/r70-simplifier/replica/{battery.py,battery-results.txt}` — `replica`
    still matches no rule; its inner `replica/tree/` (299M total dir) was ignored, so a
    **truncated snapshot** committed — references files absent from the tree.
    Precedent: `corpus/live/r65-simplifier/replica/` is already tracked in HEAD.
  - 15 `__pycache__/*.pyc` (see F3).
- **game-dev-2d-shokunin `16d003c` (a *work* commit, "r70 splice arm", 2640 files)**
  swept all untracked w9+w10 seat dirs mid-diff: 1473 files under run-dir name variants
  the `runs/` ignore rule does not match — `runs-landed/` (393), `runs-preland/` (390),
  `runs-landed-flagged/` (199), `runs-landed-flagless/` (196), `runs-flagged/` (196),
  `runs-flagless/` (194), `runs-livectl/` (194), `fault-runs/` (56), `pretree`/`pretree-runs`
  subtrees — plus 12 `.pyc`. The ignore policy treats `runs/` as scratch; renaming the dir
  (`runs2`, `runs-flagless`, `runs-landed-*`, `fault-runs`) defeats it.
- g3d clean: `corpus/.gitignore` covers `live/`+`__pycache__/`+`*.pyc`; report-last
  `3f9e070` = LOG.md + one frontier report only.

Exploit/failure path: every wave adds a new snapshot/scratch dir name → ignore list is
name-exact whack-a-mole → next `git add -A` commits a partial repo snapshot or generated
fixture tree → provenance noise (committed copy shadows live source) + repo growth.

Impact: committed bytecode and truncated repo snapshots in permanent history;
r70-baseline/measure-env now committed as 776-file duplicate of corpus/; g2d sweep
landed inside an evidence commit, mixing authored diff with 2640 junk files.
Smallest remediation: switch the blocklist to positive matching — e.g. ignore
`live/` wholesale (g3d already does) or add `__pycache__/`, `*.pyc`, `live/*/replica/`,
`live/*/measure-env/`, `live/**/runs*/`, `live/**/fault-runs/`; keep sweep commits
separate from evidence commits; `git rm -r --cached` the swept `.pyc`/snapshots.

### F2 — MED-HIGH — 83 stale probe processes orphaned to systemd-user, FIFO-blocked readers pose measurement-contamination hazard

Census (`ps -eo pid,ppid,stat,etime,args`, /proc/*/wchan sampled): all sampled ffmpeg
PIDs in `wait_for_partner`, PPID=1573 (`/usr/lib/systemd/systemd --user`) — parents
exited, children reparented = orphaned.

| era | signature | count | oldest elapsed |
|---|---|---|---|
| r67 | ffmpeg on `corpus/live/r67-boundary/probes/.fifo_probe` / `.race_fifo`, `r67-author/fifo/pair_preempt_act.wav` | 17 | ~9h05m |
| r67 | ffmpeg on `/tmp/{r67rev_fifo,f_act,r67b.wav,r67c.wav,r67test.wav}` | 7 | ~9h |
| r67 | `timeout`+`strace`+`sox` wrappers (PIDs 1965371/2, 1970028/9), `bash -c` mkfifo loops (2238073, 2238077) | 6 | ~9h — `timeout 10` never fired |
| r68 | ffmpeg `probes/.fifo_act.wav` (cwd r68-boundary) | 2 | ~4h |
| r69 | ffmpeg `/tmp/r69-starve-*` | 8 + 1 strace | ~3h10m |
| r70 | ffmpeg `/tmp/r70simp-*` (20), `/tmp/holdladder-oneshot-*` (10), `/tmp/open2-hold-*` (4), `/tmp/fifo-hold-r70-*` (1) | 35 | ~2h05m |
| w10 | ffmpeg `/tmp/r71-scout-fifo-zlcngrf_/txw_piperefuse.wav` (3927781), `/tmp/r71b-trunc-*` | 2 | 37m |

Total: **76 ffmpeg + 3 strace + 2 expired `timeout` + 2 bash loops = 83 stale procs**
(w10-era active seats `run_ledger.py`, `watch.sh`, `edge_probes.py`, frontier pw-cat
excluded — live work, not orphans). No `love`, `blender`, `bpy`, `godot` remnants (0).
Per brief: counted, not killed.

Hazard mechanism: `/proc/1930577/fd` shows no fifo fd — it is blocked *inside* `open()`
on `.fifo_probe`, a path now deleted from disk (`ls corpus/live/r67-boundary/probes/`
has no `.fifo_probe`). If a future round `mkfifo`s that path, the 10 stale readers wake
instantly: open-for-write returns immediately, so any "writer-hold"/"reader-attach"
timing probe (the exact r70/r71 measurement class) reads a fabricated instant-attach.
Also 20 residual fifo device files on disk in `corpus/live/r68-scout/fifo/` (17) and
`corpus/live/frontier-pipewire/fifo{1,2,3}`.
Smallest remediation: operator kills the orphan set; harness rule — every fifo probe
must spawn writer+reader under one timeout group and reap children (pattern exists in
`hold_ladder.py` `fifo_feed` — reuse it).

### F3 — MED — committed `.pyc` inventory drifts vs committed sources

- audio: 22 tracked `.pyc` (`git ls-files '*.pyc'`). `corpus/live/r66-author/__pycache__/compare_receipts.cpython-314.pyc` header records src `mtime=1791945156 size=5163` but the committed `compare_receipts.py` is 1725 bytes — stale bytecode inside a single tree (tree is not self-consistent; replay-from-HEAD cannot explain it). 3 more `.pyc` inside committed snapshots (`r65-simplifier/replica`, `r69-*/measure-env`) show same class. During audit `corpus/fixtures/__pycache__/measure_audio.cpython-314.pyc` was worktree-dirty until `5415115` committed the regen (Bin 127256→139552).
- g2d: 28 tracked `.pyc`; `corpus/fixtures/__pycache__/run_battery.cpython-314.pyc` header expects src_size=215328 but committed `run_battery.py`=215377 → stale committed bytecode; 13 tracked `.pyc` under `r6*-author/fault-runs/*/scratch/` have no committed source at all (MISSING).
- g3d: 0 tracked `.pyc` (ignore covers — correct end state).
Remediation: `git rm -r --cached` all `__pycache__` + add `__pycache__/`/`*.pyc` to
audio/g2d ignores.

### F4 — LOW — post-commit drift: live processes still mutate committed files

- `corpus/live/r71-simplifier/watch.sh` (PID 3917477, 240×20s ≈ 80min budget, 43min
  elapsed) appends to `corpus/live/r71-simplifier/watch.log`, now TRACKED by `5415115`
  → repo goes ` M` on each poll that sees a change, after report-last. Observed ` M`
  mid-audit, later clean (append only on hash change).
- g2d: ` M corpus/live/frontier-lovephysics/{out/run-1.txt,phys_probe/main.lua}` —
  frontier-b seat mutated files already committed in `16d003c` (committed mid-write).
- In-flight uncommitted (will presumably land next commit, not counted as defects):
  audio `?? corpus/live/r71-critic/test.{aac,au,caf,flac,wma,mp3}` +
  `?? reports/round-71/r71-boundary.md`.
Remediation: seats must stop background writers before report-last; closeout should
assert `git status` clean after the commit, not before it.

### F5 — LOW — stray `.devin/skills/flashseat/SKILL.md` at fleet root

Untracked, not ignored (`git check-ignore` → none), created 10:42 in the w10 window —
outside every seat's declared write scope; would sweep into the parent repo at the next
`git add -A`. Content is a benign `deepseek-v4-1-flash-max` model pin; parent history
shows an identical artifact was already dropped once (`67625e6 drop stray ds-probe
profile copy`). Remediation: move pin skills to `~/.config/devin/agents/` or ignore `.devin/`.

### F6 — LOW — ~7 GB ignored snapshot residue accumulates on disk (never swept, never cleaned)

- audio ≈ 1.35 G: `corpus/live/r{64..70}-baseline/{tree,frozen}`, `r{67..70}-simplifier/tree`, `r70-simplifier/replica` (299M).
- g2d ≈ 5.4 G: `r69-baseline/frozen` 1.3 G alone; rounds keep BOTH `frozen/` and `frozen-extract/` duplicates of the same HEAD (`r69-baseline` 1.3G+731M; `r70-baseline` 637M+731M; `r63-baseline/tree` 682M; `r66/r67/r68-baseline/frozen` ~700M ea).
- g3d ≈ 250 M: `r7*-baseline/{tree,frozen,frozen-extract}` + `r7*-{reviewer/head,simplifier/base}`.
- Also invisible-in-status residue (untracked, contents fully ignored): g2d
  `corpus/live/{integ-r67,integ-r67b,integ-r68,integ-r69,adj-r66-spot,adjud-r67,r57-parent-integrated,r61-integration}` — 8 nonstandard dirs, `tracked=0`.
Remediation: baseline seats should `rm -rf frozen-extract/` after replay verification;
periodic operator sweep of `live/*/{frozen,tree,frozen-extract}` — regenerable by `git archive`.

### F7 — INFO — orphaned seat reports land only by accidental sweep

g2d `reports/round-68/{r68-boundary,r68-verifier}.md` sat untracked since w8 (round-68
report-last committed without them) until `16d003c` swept them two waves late. Audio has
no `r70-author.md` on disk or in history (operator-substituted author; LOG.md documents
the substitution) — a declared report path that silently never existed.
Remediation: closeout should diff `tasks/*.txt` Report paths vs `git ls-files` and flag
missing/orphaned reports explicitly.

### F8 — INFO — secrets scan clean

Strict-pattern scan (`PRIVATE KEY|ghp_|github_pat_|sk-|AKIA|hf_|xox|AIza|api_key=…`)
over all 2563 `*scratch*`+w10 seat dirs + wave dir: only hit is `ghp_9f2b7c1d…` inside
`.ufo/waves/shokunin-train-20261014-w9/xsentinel-scratch/secrets.txt` — a prior sentinel's
notes quoting `.ufo/waves/round-9/corpus-gate.mjs:660`, which is labeled "never real".
No credentials in w10 scratch, committed sweep content, or env dumps
(`r70-baseline/env-proofs.txt` et al. are sha256 file-manifests, not `env` output).

### F9 — INFO — wave overlap during audit

`shokunin-train-20261101-w11` minted 14:30Z; w11 g2d seats already created
`corpus/live/r71-{boundary,critic,reviewer,scribe,simplifier}` inside
game-dev-2d-shokunin (11:18–11:19) with live `watch.sh` pollers — in-scope per w11
briefs (g2d w11 round = r71/pygame), not violations; noted so w10 findings aren't
misattributed to w11 traffic.

## Non-findings (checked, clean)

- No fifo device files committed (`git ls-tree -r HEAD` modes all 100644; fifos only on disk).
- g3d: `git status` clean, zero tracked `.pyc`, no out-of-scope dirs; only ignored residue (F6).
- Wave dir contains only declared files + my `xsentinel-scratch/` (gitignored via
  `.ufo/waves/*/*-scratch/`).
- No cross-lane writes detected; no `node_modules` remnants.
- Parent repo: `.ufo/reports/round-7{0,1},7{8,9}/*` committed (`7ad0141`); only `?? .devin/` (F5).

## Evidence appendix (commands)

- `git show --name-only 5415115` (audio report-last) → /tmp/xsen-5415.txt this session;
  counts: 1923 total, 776 `measure-env`, 352 `^corpus/live/runs/`, 15 `.pyc`, 2 `replica`.
- `git show --name-only 16d003c` (g2d) → 2640 files; per-dir counts above.
- `.pyc` headers parsed via `struct.unpack('<II', hdr[8:16])` vs `os.stat` source.
- Proc census: `ps -eo pid,ppid,stat,etime,args` + `/proc/<pid>/wchan` (all `wait_for_partner`),
  `/proc/1930577/fd` (no fifo fd — blocked in open()).
- Sizes: `du -sh` per dir; untracked-byte sums via `git status --porcelain -uall`.
- Ignore checks: `git check-ignore -v` per path (measure-env/replica/runs → exit 1 = not ignored).
