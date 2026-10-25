# JjTrialAudio — jj colocation trial for lane `audio`

Seat: JjTrialAudio-2 · Date: 2026-10-20 · jj 0.45.1 (~/.local/bin/jj) · git 2.56.0
Sandbox: /fast/scratch/jj-wave/JjTrialAudio/ (remote.git = sandbox bare clone; no real remote touched — `git remote -v` verified before every push).
No tools installed this wave; jj/git already present.

## Findings (observed, each with exact command + output)

### Step 1 — Sandbox build

Commands:
```
git clone --bare /home/vgpnk/Projects/shokunin/audio-shokunin remote.git
git clone remote.git lane
rsync -a --exclude=.git --exclude=.jj /home/vgpnk/Projects/shokunin/audio-shokunin/ lane/
git -C lane status --porcelain | wc -l        → 0
git -C lane status --porcelain --ignored     → 18 lines, all `!!`
```

Observed:
- Live lane working tree is **completely clean**: 0 `??` untracked, 18 ignored paths (all `Timing*.plot`/`Timings.html`, ~4 KiB each, matching root .gitignore).
- The 10 largest ignored/untracked files are the Timing*.plot/Timings.html group — all 4.0 KiB (`du -h` on each of the 18 `!!` paths). No untracked large files exist.
- Big files are **tracked**, not untracked: `git ls-files` = 50,574 entries, `git count-objects` size-pack 287.74 MiB. Top tracked blobs (`git ls-files -z | xargs -0 du -b | sort -rn | head`): `corpus/live/r89-reverify/runs/cot-r1-t3.receipt.json` 24.6 MB, `cot-r1-t2.receipt.json` 24.4 MB, `corpus/live/r76-boundary/out/pin_ff_n_8s.wav` 20.4 MB, `held-foreign.receipt.json` 17.1 MB, `r85-boundary/tags/tone60.wav` 11.5 MB.
- The rsync overlay also copied **runtime special files** git never reports: 24 FIFOs/sockets (`corpus/live/frontier-pipewire/fifo1-3`, `corpus/live/r74-boundary/rt-fb*/pipewire-0`, `pulse/native`, `r76-boundary/rt/`, `r97-boundary/run3/pipewire-0*`, etc. — `stat` shows `fifo`). `git status --porcelain` never lists them (git untracked = regular files/symlinks/dirs only), but **jj status lists all 24 as `?` untracked paths** — a real git-vs-jj status divergence.

### Step 2 — Helper init

Command: `HYAKU_STATE=/fast/scratch/jj-wave/JjTrialAudio/state scripts/hyaku/jj-lane.sh init .../lane audio` → EXIT=0.

- State line: `state branch=main local=0462a544… remote=0462a544… ahead=0 behind=0 head=attached tracked=0 untracked=0`
- Init warning (stderr): **none** — no "already tracks added paths" warning. jj itself printed `Done importing changes…`, `Initialized repo in "."`, and two harmless metaedit hints ("The author of the working copy will stay 'Joao Pedro Veiga <jpveigao10@gmail.com>'" — visible evidence why the helper's `metaedit --update-author` exists; the git side of HEAD then still carried the operator's personal identity, see step 4).
- Repo config confirmed (`.jj/repo/config.toml`): `snapshot.auto-track = "none()"`, `user.name = "audio-shokunin"`, `user.email = "audio@shokunin.local"`, `revset-aliases."trunk()" = "main@origin"`.
- `git symbolic-ref -q HEAD` → `refs/heads/main` (attached right after init, matching the spec).
- `git status --porcelain | wc -l` → 0: **unchanged vs step 1**; no intent-to-add entries appeared.
- `jj status` timing from the lane dir: **31 ms / 29 ms / 30 ms** over 3 runs (date+%s%N). Output shows only the 24 fifo/socket `?` paths; `@` empty.

### Step 3 — Default auto-track ("all()") on a copy

```
cp -a lane lane-autotrack
jj --ignore-working-copy config set --repo snapshot.auto-track '"all()"'
jj status   → 38 ms, 0 files snapshotted, 0 refusals ("The working copy has no changes.")
```
With zero untracked *regular* files in this lane, default auto-track snapshots nothing — the real risk only materializes when scratch exists. Measured that by adding fixtures:

```
head -c 2500000 /dev/urandom > scratch-tone.wav
head -c  500000 /dev/urandom > scratch-small.bin
jj status   → 99 ms
```
Output: `Warning: Refused to snapshot some files: scratch-tone.wav: 2.4MiB … maximum size allowed is 1.0MiB`; `A scratch-small.bin` entered the working-copy commit; `git status --porcelain` then showed ` A scratch-small.bin` (**intent-to-add staging produced by a read-only `jj status` under default config** — the exact bug the helper's init order prevents) and `?? scratch-tone.wav`.

Also verified: `jj file track --include-ignored -- scratch-tone.wav` overrides the 1 MiB new-file limit (file then shows `A scratch-tone.wav`), matching the helper's deliberate `--include-ignored` on named files. `jj file track` on a fifo path silently no-ops (0 `A` entries — special files can't enter trees).

### Step 4 — Round-commit simulation

```
echo "- … round-999 …" >> LOG.md
mkdir -p corpus/lessons; echo … > corpus/lessons/round-999-jjtrial.md
echo "seat scratch - do not commit" > scratch-seed.txt
jj-lane.sh commit lane --as audio -m "round-999: jj trial" -- LOG.md corpus/lessons/round-999-jjtrial.md
→ committed 25e3d803136bcbff048f0eb3e0594deb2a3f9a90
→ pushed    25e3d803136bcbff048f0eb3e0594deb2a3f9a90   EXIT=0
```

Verifications (all in the colocated lane):
- `git log -1 --format='author=%an <%ae> committer=%cn <%ce>'` → `audio-shokunin <audio@shokunin.local>` **for both** author and committer (metaedit --update-author worked).
- `git log -1 --format=%H -- LOG.md` = `25e3d803…` = pushed hash.
- `git merge-base --is-ancestor 25e3d803… main` → 0.
- `jj-lane.sh state` → `… ahead=0 behind=0 head=detached tracked=0 untracked=1` — HEAD detached as documented after the first jj mutation; `git rev-parse HEAD` = pushed hash.
- Sandbox remote: `git -C remote.git log -1 main` = `25e3d803… round-999: jj trial`; `cat-file -t` = commit.
- `scratch-seed.txt` still `??` with content intact.
- After init+commit, the helper's own `state` correctly reports `head=detached` while `detect_branch` still resolves `main` via `origin/HEAD` — protocol tooling unaffected.

**Operator-push recovery** (simulated):
```
git clone remote.git op-clone; cd op-clone
mkdir considerthese; echo "# operator note" > considerthese/2026-10-20-op.md
git add . && git commit -m "considerthese: operator push" && git push origin main   → 070b5dc7…
# back in lane:
append LOG.md; create corpus/lessons/round-999b-jjtrial.md
jj-lane.sh commit lane --as audio -m "round-999b: jj trial after remote move" -- LOG.md corpus/lessons/round-999b-jjtrial.md
→ committed 722b726fce19235053b6375e66743c1fd035d6fd
→ pushed    af3c8d60957a1ab8f4e63154cef22b418ba3cd33   EXIT=0
```
The first push was rejected, the helper fetched, rebased only the unpushed commit onto the moved `main@origin`, and retried — `committed` ≠ `pushed` because the pushed hash is the *rebased* commit. Verified `git log origin/main`: `af3c8d60` on top of `070b5dc7` (operator commit preserved, never rewritten), which sits on `25e3d803`. `git merge-base --is-ancestor 070b5dc7 main` → 0. **Any hash cited in a report must be the `pushed` line, never the `committed` line.**

### Step 5 — Lane git-touching checks

`audio-shokunin` has **no SKILL.md, no tools/, no scripts/** (shonen-seed form; `ls` of lane root confirms). The only git invocations in the lane are read-only probes inside `corpus/live/*/…sh` watcher/archival scripts: 26× `git rev-parse`, 12× `git status`, 9× `git log`, 6× `git archive`, 6× `git ls-tree`, 5× `git apply`, 4× `git diff`, 3× `git hash-object` (`grep -rhoE 'git [a-z-]+' corpus/live --include='*.sh'`). **Zero `git add`/`checkout`/`stash`/`fetch`/`push`/`commit`/`@{u}` anywhere in lane scripts.**

Ran 3 representative checks in the colocated lane (300 s timeouts), replicating script commands by hand:

| Check | Command (in lane) | Colocated lane | Plain-clone control |
|---|---|---|---|
| r80 `archive-tree.sh` equality | `git archive HEAD \| tar -x`; `ls-tree` vs extracted `comm -3` | exit 0; ls_tree=50,577 vs extracted=50,575, symdiff=2 | identical 2 — both are **mode-120000 symlinks** (`corpus/live/r80-simplifier/artifacts`, `…/folded/build_artifacts.py`); `find -type f` skips them by design of the checker, not jj |
| r74 `watch.sh` probes | `git log --oneline -1`; `git status --porcelain -uno`; `git hash-object corpus/fixtures/measure_audio.py` | all exit 0 on detached HEAD; hash `dfc2f877…` | identical |
| r74/r75 `git diff` probes | `git diff --name-only HEAD -- corpus/fixtures/measure_audio.py` | exit 0, 0 lines | identical |

Divergence found outside lane scripts but relevant to the fleet: `git rev-parse --abbrev-ref '@{u}'` → `fatal: HEAD does not point to a branch` (exit 128) on the colocated lane vs working upstream resolution in the plain clone — expected detached-HEAD consequence; no audio-lane script uses `@{u}`.

**Index-reset hazard (measured, lane-specifically relevant if any seat stages with plain `git add`):**
```
touch idxtest2.log && git add idxtest2.log   → 'A  idxtest2.log'
jj new                                       → '?? idxtest2.log'   # staged entry destroyed
```
But: a plain `jj log`/`jj status` snapshot did **not** clear a staged entry (`A  idxtest.log` survived; ` M LOG.md` still shown). The reset happens when jj *materializes a different tree into the index* (@-moving mutations: new/commit/restore), not on passive snapshots.

## PASS/FAIL table (steps 2–5)

| Step | Criterion | Result |
|---|---|---|
| 2 | init exits 0, state line sane, no init warning | PASS |
| 2 | config auto-track=none(), lane identity, trunk()=main@origin | PASS |
| 2 | git HEAD attached after init | PASS (detaches only after first mutation — documented) |
| 2 | `git status --porcelain` unchanged vs step 1 | PASS (0 → 0) |
| 2 | `jj status` fast | PASS (29–31 ms ×3) |
| 3 | default auto-track would snapshot everything | PASS — hazard confirmed on scratch fixtures (intent-to-add ` A` + 1 MiB refusal); benign on this lane's current clean tree |
| 4 | helper commit prints committed + pushed hash, correct identity | PASS |
| 4 | pushed hash = `git log -1 -- LOG.md`, ancestor of main, in remote, state ahead=0, scratch intact | PASS |
| 4 | fetch+rebase recovery after operator push | PASS (committed 722b726f → pushed af3c8d60; operator commit untouched) |
| 5 | 3 lane git checks identical under colocation vs plain clone | PASS (no colocation-caused failure; symdiff=2 is pre-existing symlink semantics) |

## Colocation hazards specific to lane `audio`

1. **50,574 tracked files / 287 MiB pack** — every jj snapshot walks the tree; observed `jj status` 29–31 ms warm, `jj file track`+`commit` of 2 paths well under 2 s including flock. No performance hazard at current size, but receipt.json pairs are 24 MiB each — if a seat ever drops such a file *untracked*, default auto-track would refuse it (>1 MiB) while the helper's `--include-ignored` would happily commit it if named; pathspec discipline is what keeps LOG/lessons commits clean.
2. **24 runtime FIFOs/sockets under `corpus/live/`** (pipewire/pulse sockets, named pipes — audio-domain debris). Git ignores them in status; **jj lists all as `?` untracked** forever. Cosmetic noise in `jj status`, but a seat reading jj output may misread the lane as dirty. `jj file track` on them silently no-ops (safe). Recommend ignoring them.
3. **2 tracked symlinks (mode 120000)** — handled identically by jj; the `archive-tree.sh` symdiff=2 is a checker artifact, not colocation damage.
4. **Detached HEAD after first jj mutation** — breaks `@{u}`, `git rev-parse --abbrev-ref HEAD` (→ `HEAD`), and any `git push`/`git pull` typed by hand. No lane script uses these; fleet helpers use `refs/heads/<branch>` explicitly and are unaffected.
5. **Git index destroyed on @-moving jj mutations** (`jj new`, `jj commit`, `jj restore`): `git add`-staged entries become `??`. If seat scripts ever `git add` before calling the helper, staging is lost — helper does its own `jj file track`, so this only bites hand-staging.
6. **No hooks, no .gitattributes/LFS, no nested .git dirs** in this lane (`find` verified). `.git/hooks/` contains only samples.
7. **`committed` ≠ `pushed` hash on remote-move recovery** — reports must cite the `pushed` line or the cited commit won't exist on the remote (its pre-rebase form stays only in jj's op log).

## Recommended per-lane config/ignore additions

Add to `audio-shokunin/.gitignore` (covers fifo/socket noise for both git scanners and jj):
```
# runtime transport debris (pipewire/pulse sockets, named pipes)
corpus/live/**/rt/
corpus/live/**/rt-fb*/
corpus/live/**/*.fifo
corpus/live/**/fifo/
corpus/live/**/pipewire-0*
corpus/live/**/pulse/
```
(No repo jj config change needed — the helper already sets `snapshot.auto-track="none()"`, lane identity, and `trunk()=main@origin`. `snapshot.max-new-file-size` should stay at the 1 MiB default: the lane's big committed files all arrived via explicit paths.)

## [INFERENCE]

- [INFERENCE] The fifo/socket noise means `jj status` output should not be used as a lane-cleanliness signal for `audio` unless the ignores above land; `jj-lane.sh state` (pure git) is already immune since it counts only `git status --porcelain`.
- [INFERENCE] Pre-existing `.jj` warning path (init's "already tracks N added paths") did not trigger here, so `audio` is a clean colocation candidate — the lightest-risk lane profile seen: clean tree, read-only scripts, no hooks/LFS.
- [INFERENCE] The only behavioral risk for this lane is human/operator muscle memory (`git add`, `@{u}`, `git pull`), not the lane's own tooling.

## Blockers

None. Sandbox preserved at /fast/scratch/jj-wave/JjTrialAudio/ (contains lane, lane-autotrack, op-clone, plain-clone, remote.git, state/) for reproducibility; safe to delete.
