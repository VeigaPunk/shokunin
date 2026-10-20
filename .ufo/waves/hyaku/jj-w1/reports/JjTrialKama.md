# JjTrialKama — jj colocation trial for lane `kama`

Date: 2026-10-20 · jj 0.45.1-7c41cdeb (`/home/vgpnk/.local/bin/jj`) · sandbox `/fast/scratch/jj-wave/JjTrialKama` (removed after evidence capture) · live repo `kama-shokunin`, branch `master`, never mutated (read-only cat/grep/git-log only). Helper `scripts/hyaku/jj-lane.sh` read, never edited.

## Step 1 — sandbox build

Commands:
```
git clone --bare /home/vgpnk/Projects/shokunin/kama-shokunin /fast/scratch/jj-wave/JjTrialKama/remote.git
git clone remote.git lane
rsync -a --exclude=.git --exclude=.jj /home/vgpnk/Projects/shokunin/kama-shokunin/ lane/
```
- `git -C lane status --porcelain | wc -l` → **19** (11 `M`, 8 `??`). All inside `.ufo/waves/round-16/` plus `corpus/SOURCES.md`, `corpus/knowledge/llamacpp-loading-lifecycle.md` — the overlay captured an in-flight round-16 wave.
- 10 largest untracked/ignored files (`git status --porcelain --ignored` + `stat`):
  | bytes | path | kind |
  |---:|---|---|
  | 1,593,314 | `.ufo/interactive-sessions/20261015T050057Z/…jsonl` | ignored |
  | 882,353 | `.ufo/interactive-sessions/20261015T050057Z/…/__advisor.jsonl` | ignored |
  | 369,263 | `.ufo/waves/round-16/falsify/spawn-result.json` | untracked |
  | 109,521 | `.ufo/waves/round-16/falsify/dispatch.json` | untracked |
  | 83,402 | `.ufo/waves/round-16/falsify/spec.json` | untracked |
  | 26,926 | `.ufo/waves/round-16/falsify/make_spec.py` | untracked |
  | 22,719 | `.ufo/waves/round-16/falsify/advice/MutateLiveRefusal.md` | untracked |
  | 19,647 | `.ufo/waves/round-16/falsify/advice/MutateMatcher.md` | untracked |
  | 17,254 | `.ufo/waves/round-16/falsify/advice/ConnectCrossLaneScope.md` | untracked |
  | 17,254 | `.ufo/waves/round-16/falsify/advice/CriticMistakesFailCapable.md` | untracked |
- `.gitignore` contains exactly `.ufo/interactive-sessions/` (27 bytes). `.ufo/state/` does **not** exist in this lane today and is not ignored.

## Step 2 — helper init

Command: `HYAKU_STATE=…/state scripts/hyaku/jj-lane.sh init lane kama`

- State line: `state branch=master local=726f737a… remote=726f737a… ahead=0 behind=0 head=attached tracked=11 untracked=8`
- Init warnings (stderr, expected): `Setting the revset alias trunk() to master@origin`; `Hint: … jj bookmark track master@origin`; twice `Warning: This setting will only impact future commits. The author of the working copy will stay "Joao Pedro Veiga <jpveigao10@gmail.com>"` — cosmetic; the helper re-stamps author via `metaedit --update-author` at commit time (verified in step 4). No "already tracks N added paths" warning (fresh `.jj`, no inherited scratch).
- Repo config confirmed via `jj config list --repo`:
  ```
  revset-aliases."trunk()" = "master@origin"
  snapshot.auto-track = "none()"
  user.name = "kama-shokunin"   user.email = "kama@shokunin.local"
  ```
- `git symbolic-ref -q HEAD` → `ref: refs/heads/master`, exit 0 → **HEAD attached** right after init. (An earlier `symbolic-ref exit=1` reading in my session was a false alarm: the `cat` in the `&&` chain failed and `git symbolic-ref` never ran; the exit echoed was `cat`'s.)
- `git status --porcelain` post-init `diff`ed vs step-1 capture → **STATUS UNCHANGED**, all 8 untracked still `??`.
- `jj status` ×3: **11 ms, 9 ms, 8 ms** (snapshots a 32 MB working tree; `auto-track=none()` keeps it cheap).

## Step 3 — default `auto-track "all()"` measurement

Commands: `cp -a lane lane-autotrack`; `jj --ignore-working-copy config set --repo snapshot.auto-track '"all()"'`; `jj st`.
- jj would snapshot **94 added + 11 modified** paths into `@` (`jj --ignore-working-copy diff --summary -r @ | sort|uniq -c` → `94 A, 11 M`). Git then shows all 94 as intent-to-add ` A` — exactly the mado-14 failure shape.
- `new file too large` refusals: **none** — the only >1 MiB file is gitignored (`interactive-sessions/…jsonl`, 1.59 MB; `jj file list -r @` counts 0 interactive-sessions entries); largest untracked non-ignored is 369 KB < 1 MiB default `snapshot.max-new-file-size`.
- Snapshot+status time: **124 ms** one-shot (vs 8–11 ms under `none()`).

## Step 4 — round-commit simulation

Prepared: appended one line to `LOG.md`, created `corpus/lessons/round-999-jjtrial.md`, left `jjtrial-scratch.txt` untracked.

Commit: `jj-lane.sh commit lane --as kama -m "round-999: jj trial" -- LOG.md corpus/lessons/round-999-jjtrial.md` →
`committed ddd7f0cb120986ea832b70708a6465777e402ab4` / `pushed ddd7f0cb…` (exit 0).

Verified:
- `git log -1 --format='author=… committer=…' ddd7f0cb…` → `author=kama-shokunin <kama@shokunin.local>` / `committer=kama-shokunin <kama@shokunin.local>` ✔
- `git log -1 --format=%H -- LOG.md` → `ddd7f0cb…` = pushed hash ✔
- `git merge-base --is-ancestor ddd7f0cb… master` → exit 0 ✔
- `jj-lane.sh state lane` → `ahead=0 behind=0 head=detached tracked=11 untracked=9` ✔ (HEAD detached post-mutation, as documented; `git rev-parse @{u}` → `fatal: HEAD does not point to a branch`)
- `git -C remote.git log -1 master` → `ddd7f0cb… round-999: jj trial` ✔
- `jjtrial-scratch.txt` still `??`, content intact ✔

**Operator-push recovery**: second clone `operator` pushed `710c931a… "operator: considerthese jjtrial"` onto remote master. Lane then committed `plans/jjtrial-second.md`:
```
committed 84353747171f2f2f9e040c6a7de4c9ff86dc07b2
pushed    6201a5a14629d2b68961f7c727702d5a78c7e32a
```
The push was rejected, helper fetched + rebased the unpushed commit onto `710c931a`, retried, and printed the **rebased** pushed hash — `git -C remote.git log master` shows `6201a5a1 (kama-shokunin) → 710c931a (operator-sim) → ddd7f0cb`. Pre-push `84353747` exists only in the local object store (`git -C remote.git cat-file -t` → `fatal: could not get object info`). The cite-the-pushed-hash protocol is what makes this safe; a report citing `84353747` would cite a hash that is not on the remote. `state` → `ahead=0`. Also observed: jj-exported commits carry a `change-id …` header line inside the commit object (informational; `git log` unaffected).

## Step 5 — lane's own git-touching gates

`grep -l 'git '` over the registry: only `.ufo/waves/round-12/fidelity.py` (rev-parse + cat-file blob), `.ufo/waves/round-13/measure.py` (cat-file blob), `.ufo/waves/round-16/measure.py` (cat-file blob). `tools/kama-probe.sh` has **no** git calls. Ran each in the colocated lane and a plain `git clone remote.git plain`, 300 s timeout:

| Gate | colocated | plain | verdict |
|---|---:|---:|---|
| `python3 .ufo/waves/round-12/fidelity.py --selftest` | 0 (11 passed, 0 failed) | 0 | identical PASS |
| `python3 .ufo/waves/round-13/measure.py --selftest` | 0 | 0 | identical PASS |
| `python3 .ufo/waves/round-16/measure.py` | 0 ("before red (17 failures), after green … result: PASS") | 0 | identical PASS |

No colocation-caused failure observed. All three gates pin specific revisions/blobs, so detached HEAD is harmless to them.

## PASS/FAIL table

| Step | Result |
|---|---|
| 2 init (config, HEAD attached, status unchanged, ~10 ms status) | **PASS** |
| 3 auto-track measurement (94 A + 11 M, no size refusal, 124 ms) | **PASS** (measured; confirms `none()` is required) |
| 4 commit/push/verify + operator-push rebase recovery | **PASS** (all 6 verifications green; pushed≠committed hash handled correctly) |
| 5 gates identical colocated vs plain | **PASS** (0/0/0 vs 0/0/0) |

## Extra hazards probed this lane

- **Index reset on mutation (real, refined):** `git add staged-probe.txt` → `A `; after `jj st` (snapshot) → still `A `; after `jj describe` (mutation) → back to `??`. So: read-only snapshots keep the index; **any jj mutation resets the git index**, destroying in-progress `git add` staging. Seats must never `git add` in a colocated lane.
- **Detached HEAD after any mutation:** `@{u}`, `git branch --show-current` (empty), and tools that require a checked-out branch break; `git rev-parse <branch>`/`master` always works. Helper's `detect_branch` handles it, but ad-hoc seat commands using `HEAD` as branch name will silently resolve to the working-copy commit instead.
- **`commit-id` header:** jj adds `change-id` inside commit objects — visible via `git cat-file -p`, harmless.
- **Repo-copy warning:** `cp -a` of a colocated repo prints "repo appears to have been copied" — informational only.
- Lane-specific: `.ufo/waves/round-*/` holds large generated JSON/logs (up to 1.6 MB single files); with `none()` this is inert, with `all()` it is the 94-file flood above. No hooks (samples only), no nested `.git`, no symlinks, no `.gitattributes`/LFS in this lane.
- `.ufo/state/` guard works: `jj-lane.sh commit … -- .ufo/state/foo` → exit 64 "driver runtime is never committed by a lane".

## [INFERENCE]

- Detached HEAD is the main integration risk for kama specifically: its lanes' humans/scripts may run `git commit`, `git add -p`, or `@{u}` shortcuts between rounds. Under colocation those fail or misbehave; the fix is documentation/lint, not git compatibility (all measured gates are fine).
- The `.gitignore` for this lane is thin (one line). `.ufo/state/` and `registry/history/*.json` unignored-but-runtime content relies entirely on pathspec discipline — already true under git; jj changes nothing there because `none()` never auto-tracks.
- `snapshot.auto-track="none()"` is load-bearing and measured: 124 ms and 94 phantom adds vs ~10 ms and zero additions. Keep it mandatory in `init`.

## Recommendations

1. Keep helper `init` exactly as-is for kama: `snapshot.auto-track="none()"`, `trunk()=master@origin`, lane identity. No lane-side config additions needed.
2. Add to `kama-shokunin/.gitignore` (belt-and-suspenders, also protects plain-git seats): `.ufo/state/` and `registry/history/.lock` — both are runtime artifacts currently protected only by pathspec discipline.
3. Consider documenting in the lane AGENTS.md: "colocated — never `git add`/`git commit`/`git stash`/`git checkout`; use `jj-lane.sh` for writes, `git log`/`show`/`cat-file` for reads."
4. No `snapshot.max-new-file-size` override needed for kama today (largest commit-eligible file 369 KB), but if waves start producing >1 MiB commit-eligible artifacts, `jj file track --include-ignored` already covers it.

Tooling: no installs this wave (jj 0.45.1 already present at `~/.local/bin/jj`). Sandbox `/fast/scratch/jj-wave/JjTrialKama` retained until report write, then removed (all cited evidence reproduced inline above; `operator` and `plain` clones included).
