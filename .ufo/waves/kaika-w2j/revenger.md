# kaika W2j — jj colocate probe: revenger-shokunin

- Live repo: `/home/vgpnk/Projects/shokunin/revenger-shokunin`, branch `main`, HEAD `8bbcb4e3` ("revenger: ignore interactive session logs")
- Scratch: `/home/vgpnk/Projects/shokunin/.tower/jj-probe/revenger-shokunin` — `git clone --local --no-checkout` + `git checkout main`; 6.9 MiB checkout (`.git` 1.8M, `.jj` 292K after init). **Deleted after probe.**
- Live repo verified unchanged afterwards: `git status --porcelain` = 0 lines, `rev-parse HEAD` = `8bbcb4e3…`, abbrev-ref = `main`.

## 1. Baseline gates (pristine clone)

Repo gates = Python verifiers discovered via `git ls-files | grep -E '\.(py|sh)$'` and README-named entry points. No `tools/`/`scripts/` dir; no git calls inside any gate (grep for `rev-parse|symbolic-ref|git status|git diff|git add|git stash` across all `.py`/`.sh` → 0 hits); no `.git/hooks` beyond samples.

| Gate | exit |
|---|---|
| `corpus/verify_evm_evidence.py` | 0 |
| `corpus/verify_icon_languages.py` | **1** (`AssertionError: r47: artifact`) |
| `corpus/verify_icon_states.py` | 0 |
| `corpus/verify_js_graph_delta.py` | 0 |
| `corpus/verify_multi_icon_states.py` | **1** (`AssertionError: r42: artifact`) |
| `corpus/verify_named_multi_icon_states.py` | 0 (139 checks, 2/2 forgeries rejected) |
| `corpus/verify_pe_resources.py` | 0 |
| `corpus/verify_saved_evidence.py` | 0 |
| `corpus/verify_semantic_trace.py` | 0 |
| `corpus/verify_shape_evidence.py` | 0 |
| `reports/round-1/replay_scenarios.py` | 0 (`all_acceptance_met: true`, self-cleans its `/tmp` workdir) |

Both failures reproduce **on the live checkout** (`python3 -B corpus/verify_icon_languages.py` → 1; `verify_multi_icon_states.py` → 1): pre-existing lane debt, not a clone or jj artifact. Note `verify_named_multi_icon_states.py` reads `HIST=/home/vgpnk/Projects/prymeagnt/revenger/.shokunin/revenger/corpus` (exists; read-only use).

## 2. `jj git init --colocate` (jj 0.45.1)

- Init: `Done importing changes… Initialized repo in "."` — instant.
- First `jj st`: **9 ms** (`time` → real 0m0.009s). Working copy `@` = `780fd129` empty on `8bbcb4e3` (main tip).
- `jj diff --stat -r @` → `0 files changed` — nothing new snapshotted (checkout was clean; only untracked files were git-ignored `.ufo/interactive-sessions/`).
- `git status` after init → clean; `git rev-parse --abbrev-ref HEAD` → `main`.
- `.jj/` is git-ignored without `.gitignore` edits: `.jj/.gitignore` contains `/*` (shown by `git check-ignore -v .jj/repo` → `.jj/.gitignore:1:/*`).

## 3. Gates after jj init

All 11 gates re-run → **exit codes identical to baseline** (same two pre-existing exit-1s). No branch- or index-dependence.

## 4. Lane-identity commit flow

- `jj --config 'user.name=revenger-shokunin' --config 'user.email=revenger@shokunin.local' commit -m test <path>`:
  `git log -1` → `Joao Pedro Veiga <jpveigao10@gmail.com> | revenger-shokunin <revenger@shokunin.local>` — **author stayed machine default** (peer caveat confirmed; author is fixed when `@` was created).
- Fix A (verified): `JJ_USER=revenger-shokunin JJ_EMAIL=revenger@shokunin.local jj metaedit --update-author -r @-` → `%an|%cn` both `revenger-shokunin <revenger@shokunin.local>`.
- Fix B (verified, preferred): `jj config set --repo user.name revenger-shokunin` + `jj config set --repo user.email revenger@shokunin.local` (writes `.jj/repo/config.toml`, repo-local); subsequent `jj commit` produced `%an|%cn` = lane identity with no env vars.
- `jj bookmark create jj-probe-test -r @-` → `git branch --list` shows `jj-probe-test`; `git rev-parse jj-probe-test` resolves. Bookmark ↔ branch mapping works.

## 5. Hazards

- **Detached HEAD**: after `jj commit` / `jj new`, `git rev-parse --abbrev-ref HEAD` prints `HEAD` and `git symbolic-ref HEAD` fails (`ref HEAD is not a symbolic ref`); `git branch --list` shows `* (HEAD detached at refs/heads/main)`. Any tool reading the current branch must be re-run only when `@` is a bookmark tip — jj attaches HEAD then, but commits made via `jj commit` leave it detached. All revenger gates ignore this (no git deps), but fleet tooling (watchdogs, ledger scripts) that calls `git symbolic-ref`/`rev-parse --abbrev-ref` will break inside a jj-managed checkout.
- **Special files**: `find -xdev -not -type f -not -type d -not -path '*/.git/*'` → none. No FIFOs/sockets/symlinks.
- **Untracked >1 MiB**: none (`git status --porcelain -uall` = 0; the 1.48 MB `.ufo/interactive-sessions/*.jsonl` is git-ignored → never snapshotted). `snapshot.max-new-file-size` (default 1 MiB) is moot here.
- **Credentials**: `find -iname '*secret*|*credential*|*.pem|*.key|*token*|*password*|*.env*'` → 0 hits.
- `.tower/` (probe root) confirmed covered by fleet-root `.git/info/exclude:8:.tower/`.

## Verdict: safe-with-config

Required: `jj config set --repo user.name/email` per lane (or `metaedit --update-author` before every `jj commit`). jj ops run in 2–9 ms; zero gate impact; `.jj/` self-ignores. Top hazard: `jj commit`/`new` detach git HEAD — any fleet tool that runs `git symbolic-ref`/`rev-parse --abbrev-ref` inside the checkout must tolerate detached HEAD or run only at bookmark tips.
