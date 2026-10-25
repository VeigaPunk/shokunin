# xsentinel report — wave-7 adversarial hygiene/security census (cross-lane, mid-wave)

Wave: shokunin-train-20261014-w7 · Dispatch commit `6d60ab4` (2026-10-14 06:48:51 -0300) · Census taken ~06:50–07:10 -0300 **while seats are in flight** (`godot r76s_window`, `run_battery r67-scribe`, audio r68-baseline writer all live during the walk) — mid-wave numbers move; treat sizes as bounded snapshots.
Scope: fleet `~/Projects/shokunin`, lane repos `audio-shokunin` / `game-dev-2d-shokunin` / `game-dev-3d-shokunin`, worktrees `~/Projects/prymeagnt{,/audio,/game-dev-2d,/game-dev-3d}`.
Scratch: `.ufo/waves/shokunin-train-20261014-w7/xsentinel-scratch/` (fleet-identities.txt, live-sizes.txt).
Continuity: this is the third consecutive sentinel census; w6 findings F1–F4 are re-checked below.

## Verdict line

No exploit-grade finding: zero real credentials, zero broken/tampered symlinks, base SHAs consistent with w6 closeout, zero stashes/pushes. **The durable posture improved since w6** (edge-verdicts ignore landed, audio gained `corpus/.gitignore`). The live risks are three MEDIUMs: a fresh ignore-pattern gap (`head-tree/`, 42M, unignored), ~0.9G/wave of regenerable baseline snapshot mass (now ignored but disk-unbounded, re-embedding 516M of committed binaries each round), and orchestration/lane commit-identity drift that makes wave provenance ambiguous.

## 1. >50MB blobs & frozen/tree embedding — PASS on tracked paths, FAIL on trajectory

**Tracked paths are clean of new giants.** Largest tracked file in the fleet repo is 240K (`.ufo/reports/AGGREGATE.md`); largest tracked in lanes is pre-existing legacy (g2d lane repo carries 7× 73,703,800 B `fixture.x86_64` ≈ 516M committed under `corpus/live/r25-*`, flagged by w6 — still tracked, `git archive HEAD` ≈ 644M).

**Untracked >50MB — all in g2d `corpus/live`, all now durably ignored:**
- `r67-baseline/frozen/` **712M, written this wave at 06:36** — the recurrence continues per wave exactly as w6-F3 predicted.
- `r66-baseline/frozen/` 701M, `r63-baseline/tree/` 684M (untracked since `2efaae2` but **never deleted from disk** — w6-F3 open item persists).
- `r65-boundary/edge-verdicts.json` 117M — **w6-F1 remediated**: `check-ignore -v` matches `corpus/.gitignore:5 live/*/edge-verdicts.json`.

**Recursive embedding check — contained, not recursive.** Each baseline `frozen/` is a lane-root snapshot (`corpus/`, `LOG.md`, `SCORECARD.md`, `reports/`…). `r67-baseline/frozen/corpus/live/` *does* contain `r66-baseline/` and `r63-baseline/` dirs — but pruned to ~12K stubs (e.g. only `battery.stdout`); fixture count stays 7 per snapshot. **No exponential recursion; growth is linear ≈ live-corpus size per baseline round.** No `.shokunin` or symlink inside any snapshot → no link cycles. New wrinkle: audio r68's `frozen` now embeds `corpus/live/round-*/` report dirs too.

**New blobs this wave:** audio `r68-baseline/frozen` 180M (in flight; `head.tar` 160M observed transient at 06:50 then deleted — seats archive, don't hoard), g3d `r76-baseline/frozen` 26M, g2d `r67-baseline/frozen` 712M — all covered by ignore rules (verified `check-ignore`).

## 2. Findings

### F1 — MEDIUM: `head-tree/` escapes the fresh ignore patterns; 42M unignored at integration window
- **Evidence:** `audio-shokunin/corpus/live/r67-simplifier/head-tree/` = 42M (many small files — no single >5M member). `git check-ignore corpus/live/r67-simplifier/head-tree/x` → **exit 1**; `git status` shows `?? corpus/live/r67-simplifier/head-tree/`. It is the only `head-tree/` dir in all three lanes.
- **Exploit/failure path:** audio's `corpus/.gitignore` (added `f4621f9`, remediating w6-F2) covers exactly `live/*/tree/` + `live/*/frozen/` — name-exact patterns. The r67-simplifier seat minted a new directory name; at r68 integration a blanket `git add corpus/live/r67-simplifier/` or `git add -A` commits 42M of tree snapshot — the same r63 incident class, through a naming side-channel. Any future `*-snapshot`/`backup-*`/`scratch-*` dir has the same gap; g2d and g3d have the identical weakness for non-`tree`/`frozen` names (g3d's blanket `live/` is immune).
- **Impact:** repo bloat recurrence; demonstrates ignore-by-name is fragile against seat-chosen paths.
- **Smallest remediation:** in `audio-shokunin/corpus/.gitignore` and `game-dev-2d-shokunin/corpus/.gitignore`, generalize to `live/*/*-tree/` (plus keep `live/*/tree/`, `live/*/frozen/`) — or adopt g3d's posture `live/` + explicit allowlist for receipts. Delete or ignore `r67-simplifier/head-tree/` at integration. Owner: audio parent/operator.

### F2 — MEDIUM: baseline snapshots re-embed the committed 516M fixture set every round; ~0.9G/wave of regenerable mass
- **Evidence:** snapshot mass (`*/frozen`, `*/tree`, `*/head-tree`) = **72–84% of each lane's live corpus**: audio 743M/883M (84%), g2d 1.8G/2.5G (72%), g3d 148M/182M (81%). g2d baseline rounds: r63 684M → r66 701M → r67 712M (each re-copies the same seven `fixture.x86_64`). Audio baseline rounds: r64 119M → r65 135M → r66 141M → r67 169M → r68 ~182M. g3d: steady ~26M/round ×7.
- **Exploit/failure path:** not a commit-risk (all three lanes now durably ignore snapshot dirs — verified), but a resource failure: linear-unbounded growth of copies of bytes that already exist as git objects + canonical files; every census/secret-scan re-walks ~4.3G; backup and checkout surface inflates. `r63-baseline/tree` (684M) has been dead weight on disk since `2efaae2` untracked it.
- **Impact:** ~+0.9G/wave sustained (854G free → slow, but pure waste); scan cost grows per wave.
- **Smallest remediation:** freeze by reference, not copy — `git archive`/`head.tar`-style artifact (audio already produces `archive-manifest.txt`/`frozen-proofs.txt`, keep only those) or `cp -al` hardlinks for the r25 fixtures. Delete `r63-baseline/tree` and `r65-boundary/edge-verdicts.json` post-adjudication. Owner: baseline-seat brief + operator cleanup.

### F3 — MEDIUM: orchestration + lane commit-identity drift; provenance depends on the committing shell
- **Fleet repo (`~/Projects/shokunin`):** last 4 orchestration commits span 3 identities — `shokunin-fleet <fleet@shokunin.local>` (w4–w5 dispatch+adjudication) → `devin-fleet <fleet@shokunin.local>` (`7e2b35c` w5 closeout, `c6dea73` w6 dispatch) → `ci <ci@local>` (`b190b08` w6 closeout, `6d60ab4` **w7 dispatch**). Repo static config is `ci <ci@local>` — i.e., fleet identities exist only as per-commit shell overrides; whoever ran the w6-closeout/w7-dispatch without the override recorded the raw default.
- **Lane repos:** author *name* is stable (`<lane>-shokunin`), but email thrashes across three forms in ~6 commits: audio `audio@shokunin.local` → `audio-shokunin@local` → **reverted** `audio@shokunin.local` (`bd5e1fe`); g2d `game-dev-2d-shokunin@local` → `g2d@shokunin.local` (`4a4def9`); g3d same → `g3d@shokunin.local`. w6 read this as a one-way migration; w7 shows it oscillating.
- **Worktree defaults:** `prymeagnt/game-dev-2d` static config is `games-engine-mechanics-shokunin` — a **foreign lane's identity is the fallback author in g2d's own worktree**, and it already authored a lane commit (`a0a9c4bc`, "game-dev-2d r60 … (devin host)"). A LEAF seat that violates the no-commit rule (or an operator slip) writes cross-lane provenance.
- **Exploit path:** any principal that can reach the shell commits as `ci` or `games-engine-mechanics` indistinguishably from legitimate fallback paths — provenance checks keyed on author would either false-alarm on real commits or pass forged ones; wave attribution (`who dispatched w7`) is unverifiable from the log alone.
- **Impact:** audit-trail ambiguity, not intrusion (all subjects/timestamps coherent; no unexpected author). Correctness defect on the provenance axis.
- **Smallest remediation:** pin `user.name`/`user.email` per repo — fleet repo to `shokunin-fleet`, each worktree to its own lane identity — so the default is correct instead of relying on per-commit env.

### F4 — LOW: stale *tracked* `.shokunin/reports/` mirror in the prymeagnt worktrees
- **Evidence:** `.shokunin/reports/round-*/<lane>.md` is committed in each lane worktree (audio 61, g2d 59, g3d 68 tracked files) but has **0 writes since Oct 13 ~17:04** (symlink consolidation); canonical reports now land in `*-shokunin/reports/` (round-67/67/75) — e.g. `g2d reports/round-67/r67-baseline.md` arrived this wave, untracked pending parent integration. Two committed report locations, permanently diverged; also `.shokunin/<lane>` symlink + `MANIFEST.json` + `mints/` tracked in worktree repos dangle on foreign clones.
- **Exploit path:** a reader/verifier resolving "the lane's reports" inside the prymeagnt clone gets silently truncated history (audio stops at r61, g2d at r59, g3d at r68); a confused seat could write new reports into the dead mirror and have them committed but invisible to adjudication.
- **Impact:** provenance fork; confused evidence.
- **Smallest remediation:** `git rm -r --cached` + delete `.shokunin/reports` in the three worktrees (or leave frozen with a README pointer to the canonical root); do not let it resume receiving writes.

### F5 — LOW: six leftover `xconnector-scratch`/`xsentinel-scratch` dirs (w4–w6) permanently untracked, unignored
- **Evidence:** `git status` `??` noise only: w4 (4K/8K), w5 (8K/460K), w6 (8K/1.6M) — never cleaned, not covered by `.gitignore` (fleet repo's only rule is `*-shokunin/`). This report's `xsentinel-scratch/` joins the pile.
- **Exploit path:** a future `git add -A` in the fleet repo sweeps arbitrary scratch (including future large/sensitive scratch) into history — the same blanket-add vector as F1, one level up.
- **Impact:** permanent status noise; latent commit surface.
- **Smallest remediation:** add `x*-scratch/` (or `.ufo/waves/*/*-scratch/`) to fleet `.gitignore`, or sweep scratch post-adjudication.

## 3. Clean checks (PASS)

- **Secrets:** 0 real credentials anywhere scanned — tracked content: only labeled-synthetic fixtures (`ghp_9f2b…` "never real" in `round-9/corpus-gate.mjs:660`, `Bearer jt-test-pw` test); untracked w4–w7 wave dirs+scratch: 0 hits; **8,239 today-new lane files** (text <10M, excl. snapshots/`node_modules`/`.git`): 0 hits on key/token/password-assignment patterns.
- **Symlink integrity:** `.shokunin/{audio,game-dev-2d,game-dev-3d}` all resolve to `~/Projects/shokunin/<lane>-shokunin`; **committed symlink blob (mode 120000) byte-identical to on-disk `readlink` for all three** — no swapped link. Zero broken symlinks fleet-wide; no `.shokunin` inside any frozen/tree snapshot → no recursion via links. INFO: `r66-simplifier/tree/lessons` is an absolute-path symlink (breaks on repo relocation, resolves today).
- **Lane identity of HEADs:** fleet `6d60ab4` = w7 dispatch commit; lane HEADs `bd5e1fe` / `4a4def9` / `cb6bf7b` match the w7 registry's own closeout note exactly.
- **Process hygiene:** 0 stashes across all 5 repos; no push/fetch/merge/rebase evidence mid-wave; only post-dispatch commit anywhere is the dispatch commit itself; LEAF discipline holding (seat writes confined to `corpus/live/rNN-<seat>/` + `reports/round-NN/`).
- **Uncommitted-but-tracked-worthy reports:** only in-flight ones (`g2d reports/round-67/r67-baseline.md` so far) — the designed LEAF→parent-integration flow, not strays. w7 `spec/dispatch/registry` committed; all w4–w6 reports tracked.

## 4. INFO

- `dispatch.json`/`swarm-registry.json` `dispatched_at` "Z" convention flipped between waves: w6 `05:01:28Z` is true UTC (commit 02:01:28 -0300); w7 `06:55Z` reads as **local time mislabeled Z** (commit 06:48:51 -0300 = 09:48:51 UTC). Cross-wave timeline arithmetic breaks by ±3h. Earliest w7 seat mtimes (~06:36 local) also precede the dispatch commit (~06:48) — spawn precedes registry commit.
- `.ufo/waves` report naming drift: w1–w3 `x-connector.md`/`x-sentinel.md` vs w4+ `xconnector-report.md`/`xsentinel-report.md` — cosmetic.
- Worktree `.git` dirs are `gitdir:` files into `prymeagnt/.git/worktrees/{r12,r1,game-dev-3d}` — worktree names `r12`/`r1` don't match lane names (operator-confusion potential only).
- Disk: `/home` 72G used / 854G free — trajectory is a waste problem, not an exhaustion problem at current cadence.

## Severity summary

| # | severity | item |
|---|---|---|
| F1 | MEDIUM | audio `head-tree/` 42M unignored — fresh `corpus/.gitignore` pattern gap, commit-risk at r68 integration |
| F2 | MEDIUM | ~0.9G/wave regenerable baseline snapshots (72–84% of live); 516M fixture set re-embedded each g2d round; r63 tree still on disk |
| F3 | MEDIUM | orchestration identity `shokunin-fleet`→`devin-fleet`→`ci`; lane email thrash; g2d worktree fallback = `games-engine-mechanics` |
| F4 | LOW | stale tracked `.shokunin/reports/` mirror in worktrees — diverged provenance fork |
| F5 | LOW | six leftover wave scratch dirs unignored/uncommitted — `add -A` sweep risk |
| — | INFO | `Z`-timestamp flip w6→w7; absolute `tree/lessons` symlink; worktree-name↔lane-name mismatch |
| — | PASS | 0 real secrets; symlinks committed==on-disk; base SHAs consistent; LEAF discipline; ignore rules verified live |

Read-only census. No mutations performed; report + `xsentinel-scratch/` only, per scope.
