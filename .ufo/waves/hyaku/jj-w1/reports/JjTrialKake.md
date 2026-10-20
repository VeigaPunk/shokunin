# JjTrialKake — jj colocation empirical trial, lane `kake`

Seat: JjTrialKake-2 · jj 0.45.1 (`~/.local/bin/jj`) · sandbox `/fast/scratch/jj-wave/JjTrialKake/` · lane `/home/vgpnk/Projects/shokunin/kake-shokunin` (branch `master`, remote `https://github.com/VeigaPunk/kake-shokunin.git`). Live repo touched read-only (clone/rsync source, status/grep only). No installs this run.

## Findings

### Step 1 — sandbox build

- `git clone --bare …/kake-shokunin …/remote.git` + `git clone …/remote.git …/lane` → clean clone, branch `master`.
- `rsync -a --exclude=.git --exclude=.jj …/kake-shokunin/ …/lane/` → `git -C lane status --porcelain | wc -l` = **0**.
- Live lane working tree is **completely clean**: `git status --porcelain | wc -l` = 0; `git status --porcelain --ignored` = 1 entry, `!! .ufo/interactive-sessions/` (ignored by tracked `.gitignore` line 1: `.ufo/interactive-sessions/`; confirmed `git check-ignore -v`).
- 10 largest untracked-or-ignored files (all under `.ufo/interactive-sessions/`):
  1. `2387804  __advisor.jsonl` (2.28 MiB)
  2. `2119824  <session>.jsonl` (2.02 MiB)
  3. `14155    2.bash-original.log`
  4. `3522     11.bash-original.log` — only 4 files exist; no other untracked content.
- Tracked hazards inventory (from live repo): 254 tracked files; no nested `.git` dirs; no symlinks; no `.gitattributes`/LFS pointers (git-lfs 3.8.0 installed but unused); no non-sample hooks; largest tracked file `.ufo/waves/round-21/anchors-fixed.json` = 2,355,487 bytes (2.25 MiB, already committed); `.ufo/` is a partially-tracked generated tree (round/wave state committed, `interactive-sessions/` ignored).

### Step 2 — helper init

- `HYAKU_STATE=…/state jj-lane.sh init …/lane kake` → exit 0; state line:
  `state branch=master local=7c61c8cc… remote=7c61c8cc… ahead=0 behind=0 head=attached tracked=0 untracked=0`
- Init warnings (stderr, non-fatal): two identical
  `Warning: This setting will only impact future commits. The author of the working copy will stay "Joao Pedro Veiga <jpveigao10@gmail.com>". To change the working copy author, use "jj metaedit --update-author".`
  (one per `config set user.name`/`user.email`; cosmetic — @ author is stamped correctly by `commit` via metaedit).
- Repo config confirmed (`.jj/repo/config.toml`):
  `snapshot.auto-track = "none()"`, `user.name = "kake-shokunin"`, `user.email = "kake@shokunin.local"`, `revset-aliases."trunk()" = "master@origin"`.
- `git symbolic-ref -q HEAD` → `refs/heads/master` (attached right after init).
- `git status --porcelain` after init: 0 lines — identical to pre-init. Every prior state preserved; the only ignored dir stayed `!!` (now `!! .jj/` appears too, jj-internally ignored).
- `jj status` ×3 (bash `time`, real): **0.007s, 0.008s, 0.007s** — `@` empty, parent `7c61c8cc master`.

### Step 3 — default auto-track alternative

- `cp -a lane lane-autotrack` (jj warned `Your repo appears to have been copied` — informational only) + `config set snapshot.auto-track '"all()"'` → `jj status`: **0.009s, 0 files added** because tracked `.gitignore` covers the only ignored tree (`.ufo/interactive-sessions/`, containing the two >1 MiB jsonl files — never attempted).
- After planting `seat-scratch.txt` (untracked) and `seat-scratch-big.bin` (2,000,000 bytes):
  `jj status` = **0.017s**; snapshotted **1 file** (`A seat-scratch.txt`) into @; emitted
  `Warning: Refused to snapshot some files: seat-scratch-big.bin: 1.9MiB (2000000 bytes); the maximum size allowed is 1.0MiB (1048576 bytes)`
  and listed it as `? seat-scratch-big.bin` (left untracked, warning-only, exit 0).
- So under default auto-track the 2.3/2.0 MiB `.ufo` session logs would produce the same per-command warning noise on every jj invocation (if `.gitignore` ever lapsed) and any scratch ≤1 MiB would silently enter @. `auto-track="none()"` eliminates both.

### Step 4 — round commit via helper + concurrent-push recovery

- Prepared: appended `- round-999 jj trial line` to LOG.md; created `corpus/lessons/round-999-jjtrial.md`; left `seat-scratch.txt` (`do not commit me`) untracked. `git status` before: ` M LOG.md`, `?? corpus/lessons/…`, `?? seat-scratch.txt`.
- `jj-lane.sh commit … --as kake -m "round-999: jj trial" -- LOG.md corpus/lessons/round-999-jjtrial.md` → exit 0:
  `committed 292856fc9a116b391308fa55644365e5260e960a` / `pushed 292856fc…`
- Verified on pushed hash `292856fc`:
  - author AND committer: `kake-shokunin <kake@shokunin.local>`;
  - `git log -1 --format=%H -- LOG.md` = `292856fc…` (matches pushed hash);
  - `git merge-base --is-ancestor 292856fc master` → success;
  - `jj-lane.sh state` → `ahead=0 behind=0 head=detached tracked=0 untracked=1` (HEAD detached as documented);
  - sandbox `remote.git` `git log -1 master` = `292856fc… round-999: jj trial`;
  - `seat-scratch.txt` still `??`, content `do not commit me` intact.
- Operator-push simulation: second clone `operator/` committed `considerthese/operator-push.md` (`0bbd308`, pushed to sandbox remote master). Then appended `- round-999 second commit` to lane LOG.md and re-ran the helper commit:
  - `committed 118f381b…` then push rejected → helper fetched, rebased the unpushed commit onto `master@origin`, retried → `pushed c3f7a87747293ff4914b3428f8c19eb3caf1030d` (exit 0).
  - Remote log after: `c3f7a87 kake-shokunin round-999: after operator push` → `0bbd308 operator` → `292856f round-999` → `7c61c8c`. Linear history preserved; the pushed (rebased) hash is the one `pushed` printed — correct cite semantics.
  - Rebased commit `c3f7a877` retains `kake-shokunin <kake@shokunin.local>` as author and committer; `git show c3f7a877:LOG.md` tail contains both trial lines.
  - Note: `committed` vs `pushed` hashes **differ on the rebase path** — reporters must cite only the `pushed` hash.
- HEAD-vs-working-copy semantics confirmed: after `jj commit`, git HEAD is detached; with a dirty tracked file (extra uncommitted LOG.md line), @ is a child commit (`uqumwztu`) but git HEAD stays on the pushed tip → `git rev-list --count origin/master..HEAD` = 0 in both plain clone and colocated repo. Tools using `HEAD` for "unpushed" remain correct while @ is descendant-or-equal of the tip; tools using `@{u}` or `rev-parse --abbrev-ref HEAD` (`HEAD` now literal `HEAD`, not `master`) will misbehave.

### Step 5 — lane git-touching checks (300s timeout each)

Registry (`SKILL.md` §Owned freshness gate registry): only `freshness-sweep` invokes `git` (`execFileSync git -C <pins.plazirSourceDir|pins.pq2Dir> ls-remote/rev-parse/rev-list` at `freshness-sweep.mjs:699-701,852-855`) — against **external** source repos, never the lane itself; `--offline` skips the plazir block, `pq2` gets `skipped(offline)`. `corpus-contract.mjs` selftest spawns only `node` children; `probe-delta.mjs` invokes no git.

| Check | jj-colocated lane | plain clone | Verdict |
|---|---|---|---|
| `node scripts/freshness-sweep.mjs --offline` | exit 1 — `VERDICT: DRIFT — §paths: 3 unannotated miss · 0 NOT in pins.pathsMissSet (exit 1, partial: offline)` | exit 1, **byte-identical** verdict body (only generated-line repo path/timestamp differ) | pre-existing lane drift, not colocation |
| `node scripts/freshness-sweep.mjs --selftest` (HOME, KAKE_SELFTEST_DIR, TMPDIR isolated to sandbox dirs) | exit 0 — `selftest: 15/15 passed` | exit 0 — `15/15` | identical |
| `node scripts/corpus-contract.mjs --selftest` (TMPDIR isolated) | exit 0 — `selftest: 7/7 passed` | exit 0 — `7/7` | identical |

No check failure is attributable to colocation. The one failure (`--offline` exit 1) reproduces exactly in a pure-git clone.

## PASS/FAIL table (steps 2–5)

| Step | Criterion | Result |
|---|---|---|
| 2 | init exit 0; state line sane; config keys set; HEAD attached post-init; `git status` unchanged | **PASS** |
| 3 | auto-track measurement recorded; big-file refusal observed | **PASS** (measured: 1 file added, 1.9MiB refused w/ warning, 0.017s) |
| 4 | commit prints committed+pushed; lane identity; ancestor-of-master; state ahead=0; remote has commit; scratch preserved; rejected-push recovery via fetch+rebase | **PASS** (all verified; recovery pushed `c3f7a877` linear over `0bbd308`) |
| 5 | ≤3 git-touching checks run in sandbox, colocation failures separated | **PASS** (3 run; only failure identical in plain clone → pre-existing) |

## Colocation hazards specific to lane `kake`

1. **Detached HEAD after every jj mutation** — `git symbolic-ref -q HEAD` fails post-commit; any lane workflow or external gate that uses `@{u}`, `rev-parse --abbrev-ref HEAD`, or assumes an attached HEAD will break. `git rev-parse master` / explicit refnames are unaffected. The lane's own gates don't read HEAD of the lane repo — but operator-side copies of plazir/ds4cc (`git -C <dir> rev-list origin/main..HEAD`) would miscount if those repos were ever colocated too.
2. **`jj commit`-tracked-paths via `file track --include-ignored` bypasses size limits** — a named file >1 MiB is force-tracked into the commit (e.g. a 2.4 MiB `__advisor.jsonl` named explicitly would be committed despite the snapshot.max-new-file-size refusal under auto-track). Pathspec-limited commits plus callers never naming `.ufo/interactive-sessions/` files is the only guard.
3. **`.ufo/` is a partially-tracked generated tree** — `.ufo/round-*/`, `.ufo/waves/` are committed; `interactive-sessions/` is ignored. A `jj file track <dir>` on a mixed `.ufo/` dir tracks non-ignored entries like `git add` — same semantics as git, so risk is equal, not new.
4. **Big-file warning noise under any non-none() auto-track** — the two >1 MiB session jsonls (and the tracked 2.25 MiB `anchors-fixed.json` precedent) mean any auto-track snapshot would warn/refuse per invocation if `.gitignore` coverage ever lapsed.
5. **`committed` ≠ `pushed` hash on the rebase path** — citation discipline must use the `pushed` line only (verified above).
6. **Working-copy author stays stale after init** — the init warnings show @ keeps the original git author until first commit; helper's metaedit stamps correctly, but a bare `jj describe`/`jj new` by a human would carry `Joao Pedro Veiga <jpveigao10@gmail.com>` — [INFERENCE] acceptable since all protocol commits go through the helper.
7. **Copied `.jj` warns but works** — `cp -a` of a colocated repo yields a functional repo with a relocation warning; irrelevant to lanes but noted for sweep/backup tooling.
8. No nested `.git` dirs, no symlinks, no `.gitattributes`/LFS, no hooks — none of these hazard classes exist in this lane.

## Recommendations — per-lane config/ignore for `kake`

Exactly what the helper's init already sets; no lane additions required:

```toml
# .jj/repo/config.toml (set by jj-lane.sh init kake)
snapshot.auto-track = "none()"
user.name  = "kake-shokunin"
user.email = "kake@shokunin.local"
revset-aliases."trunk()" = "master@origin"
```

Optional belt-and-suspenders (not required, evidence-based):
- Keep `.gitignore:1` `.ufo/interactive-sessions/` — it is the only barrier keeping the 2.3/2.0 MiB session logs out of any accidental `file track <dir>` or auto-track slip. [INFERENCE] If session logs should be protected even harder, add them to `.git/info/exclude` too — but tracked `.gitignore` already suffices for both git and jj.
- Never name `.ufo/interactive-sessions/*` or other >1 MiB files in helper `commit` pathspecs — `--include-ignored` force-tracks them past the size guard.
- Cite only the `pushed` hash; treat `committed` as a local placeholder (rebase path verified above).
- No `snapshot.max-new-file-size` bump needed: the lane has no legitimate >1 MiB commit candidates (the only large tracked file predates colocation and is already committed).

## Tooling installs

None. jj 0.45.1 and git-lfs 3.8.0 already present; `/usr/bin/time` absent — used bash `time` instead.

## Sandbox

`/fast/scratch/jj-wave/JjTrialKake/` — removable; no cited failure depends on it (the `--offline` DRIFT failure reproduces in any clone). Contents: `remote.git` (bare mirror + trial commits), `lane/` (colocated), `lane-autotrack/` (auto-track measurement), `plain/` (no-jj control), `operator/` (concurrent-push clone), `state/` (HYAKU_STATE locks).
