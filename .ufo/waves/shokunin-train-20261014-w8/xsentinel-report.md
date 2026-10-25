# xsentinel report — wave-8 adversarial hygiene/security census (cross-lane, early-wave)

Wave: shokunin-train-20261014-w8 · Dispatch commit `621b92c` (2026-10-14 07:47:11 -0300, `devin-fleet`) · Census taken ~07:48–08:00 -0300 **while seats are spawning** — earliest census yet; 20/24 domain seat dirs present, baselines mid-write. Treat sizes as bounded snapshots; several verdicts are in-flight and flagged for closeout re-check.
Scope: fleet `~/Projects/shokunin`, lane repos `audio-shokunin` / `game-dev-2d-shokunin` / `game-dev-3d-shokunin`, worktrees `~/Projects/prymeagnt{,/audio,/game-dev-2d,/game-dev-3d}`.
Scratch: `.ufo/waves/shokunin-train-20261014-w8/xsentinel-scratch/` (identity-census.txt, live-sizes.txt, secrets-tracked.txt, secrets-untracked.txt).
Continuity: fourth consecutive sentinel census; w7 findings F1–F5 re-checked below.

## Verdict line

No exploit-grade finding: zero real credentials, zero broken/tampered symlinks, zero stashes, no post-dispatch commits, LEAF discipline holding. **One explicit-brief violation is live**: g3d's r77 baseline seat froze a populated working-tree copy (incl. 1,264 untracked `node_modules` files) instead of the mandated `git archive`-only artifact — audio r69 and g2d r68 baselines comply. The `*tree*/` broadening is verified against every tree-class name on disk but the non-tree side-channel remains open (`runs-extracted/` unignored on disk today; g3d reviewers minted `head/` again this wave). Identity drift worsened: **all three worktrees** now default to foreign-lane `games-engine-mechanics-shokunin`.

## 1. >50MB blobs & snapshot embedding — PASS on tracked paths; archive-compliance split

**Tracked paths clean of new giants.** Largest tracked: fleet 240K (`.ufo/reports/AGGREGATE.md`); lanes unchanged — g2d's pre-existing 7× 73,703,800 B `fixture.x86_64` under `corpus/live/r25-*` (≈516M committed, flagged w6) still tracked; `git ls-files` shows zero `node_modules` in any lane.

**w8 baseline compliance (the w7-F2 archive-only mandate is in all three briefs verbatim):**
| lane | dir | form | verdict |
|---|---|---|---|
| audio `r69-baseline/frozen/` | `head-7b8d423.tar` **169M** + `archive-manifest.txt` + `archive-sha256.txt` | archive-only, proofs landed | **COMPLIANT** |
| g2d `r68-baseline/frozen/` | `HEAD-1101cb37e8c44b084d6ce6f8f8209919a2f59bd5.tar` **626M** only | archive-only | **COMPLIANT** |
| g3d `r77-baseline/frozen/` | **1,561 extracted files, 26M, zero `.tar`** | populated tree | **VIOLATION** |

**g3d violation is exact, not cosmetic.** `comm` of the frozen file list vs `git ls-files`: all 297 tracked files present, **plus 1,264 extra files — every one under `corpus/fixtures/three/node_modules/`** (untracked vendor mass). So the seat did not run `git archive` at all; it copied the working tree, breaching two explicit brief clauses at once: "archive output only (no populated-tree extraction)" and "NEVER recursively embed … node_modules". Still in flight (created 07:49, receipts landing 07:54) — parent should verify at integration whether it persists or was transient scratch.

**w7-F1 `*tree*/` broadening — verified, with residual gap.** `git check-ignore` on `corpus/live/` paths:
- COVERED (audio `a0958a9`, g2d `3a53258`): `tree/`, `head-tree/`, `pretree/`, `pretree-runs/`, `work-tree/`, `worktree/` — every `*tree*` dir on disk matches `live/*/*tree*/`. All snapshot dirs minted so far this wave are covered (`frozen/` by name-exact; no new tree-class names).
- **NOT covered:** `snapshot/`, `head/`, `extracted/`, `runs-extracted/`, `base/` — verified `check-ignore` exit 1 in audio+g2d. Live proof on disk: `g2d corpus/live/r66-simplifier/runs-extracted/` **1.1M, unignored**. g3d reviewers minted `head/` again this wave (`r76-reviewer/head` 524K, `r77-reviewer/head` 540K) — harmless there only because g3d blanket-ignores `live/`; the same habit landing in audio/g2d would be unignored. The remediation narrowed the class but did not close it.

**Recursion contained.** g2d's tar is `git archive`-sourced (untracked baselines can't embed). g3d's extraction contains zero nested `r7*-baseline` dirs (its own `live/` ignore means nothing under `live/` is tracked/archived). Audio r68's w7 frozen tree carries tracked `corpus/live/r6*-*/` dirs — tracked-evidence embedding, not snapshot recursion. No `.shokunin` inside any snapshot → no link cycles.

## 2. Findings

### F1 — MEDIUM: g3d r77-baseline violates the archive-only mandate (working-tree copy + untracked node_modules)
- **Evidence:** `game-dev-3d-shokunin/corpus/live/r77-baseline/frozen/` = 1,561 files / 26M, no archive file; 1,264 members under `corpus/fixtures/three/node_modules/` (untracked; `git ls-files | grep -c node_modules` = 0). Created 07:49 post-dispatch → this wave's seat.
- **Exploit/failure path:** brief-noncompliance is the direct failure; second-order: a dirty freeze is not a clean tracked-files oracle — replay receipts on it can differ from true HEAD state (untracked vendor code reachable from fixtures), and if the same copy method recurs in audio/g2d it would embed prior untracked baselines (the original exponential-recursion vector the mandate was written to kill).
- **Impact:** provenance/validity of the r77 baseline replay is weaker than its siblings; 26M is small but the method scales badly.
- **Smallest remediation:** at r77 integration, confirm seat intent vs residue; baseline brief already carries the clause — add "frozen/ must contain only `*.tar` + manifest/proofs; `comm -23 <(find frozen -type f) <(git ls-files)` must be empty" as a verifiable receipt line. Owner: g3d parent/operator.

### F2 — MEDIUM: commit-identity drift persists and widened to all three worktrees
- **Fleet repo:** last 15 commits span **3 identities** — `shokunin-fleet` 9 / `devin-fleet` 4 / `ci` 2. w7-closeout+w8-dispatch recorded as `devin-fleet`, w6-closeout+w7-dispatch as `ci`. Static config: `ci <ci@local>` — still identity-by-shell-override.
- **Lane repos:** all three static configs are now `ci <ci@local>` (audio integration commits `7b8d423`, g2d `1101cb3`, g3d `e417365`/`8a67f71` all authored `ci`). g2d's last 15 commits carry **5 distinct authors** incl. foreign-lane `games-engine-mechanics-shokunin` (`a0a9c4bc`, flagged w7). Email thrash continues: audio `audio@`↔`audio-shokunin@`, g3d `g3d@`↔`game-dev-3d@`↔`game-dev-3d-shokunin@`.
- **Worktree defaults escalated:** w7 found `games-engine-mechanics-shokunin` as fallback only in `prymeagnt/game-dev-2d`; now **all three worktrees** (`audio`, `game-dev-2d`, `game-dev-3d`) static-config to that foreign lane identity. A LEAF slip or operator commit in any worktree writes cross-lane provenance.
- **Exploit path / impact:** unchanged from w7 — author-keyed provenance is unverifiable; any shell-reaching principal commits as `ci` or `games-engine-mechanics` indistinguishably. Correctness defect, not intrusion (subjects/timestamps coherent).
- **Smallest remediation:** pin `user.name`/`user.email` per repo (fleet→`shokunin-fleet`, lanes→lane identity, worktrees→own lane). Unchanged since w7; now blocking 7 wrong-default surfaces instead of 5.

### F3 — MEDIUM: baseline mass still ~linear; per-round shrink but no bound; w6/w7 cleanup items still on disk
- **Trajectory:** `corpus/live` totals — audio 883M→**1,272M** (+389M), g2d 2.5G→**3,640M** (+1.1G), g3d 182M→**268M** (+86M). Snapshot mass share: audio 1,040M/1,272M (82%), g2d 2,740M+120M/3,640M (**79%**), g3d 201M/268M (75%).
- **Archive-only did shrink the unit cost**: g2d per-baseline 712M extracted (r67) → **626M tar** (r68); audio 184M → 169M. But every wave still re-embeds the 516M fixture set into a new artifact (the tar stores the same tracked bytes git already holds) — ~0.9–1.1G/wave sustained, now accruing as uncompressed tarballs.
- **Still on disk (3rd census flagging):** `g2d corpus/live/r63-baseline/tree/` 684M (untracked since `2efaae2`), `r65-boundary/edge-verdicts.json` 117M, `r66`+`r67` extracted frozen 1.4G — 2.2G of explicitly-flagged dead mass in g2d alone.
- **Impact:** waste trajectory, not exhaustion (`/home` 854G free); every census/scan re-walks ~5G.
- **Smallest remediation:** post-adjudication delete of r63 tree + edge-verdicts + extracted `r66/r67` frozen (keep tars/manifests); consider `git archive | zstd` or hash-only freeze receipts.

### F4 — LOW: residual ignore gap for non-tree snapshot names; live unignored specimen on disk
- **Evidence:** `git check-ignore` exit 1 for `live/*/snapshot`, `live/*/head`, `live/*/extracted`, `live/*/runs-extracted`, `live/*/base` in audio and g2d. Real specimen: `g2d corpus/live/r66-simplifier/runs-extracted/` 1.1M unignored/untracked. g3d's `head/` naming recurred this wave (r77-reviewer) — covered only by g3d's blanket `live/`.
- **Exploit/failure path:** identical to w7-F1 — a seat minting a non-`tree`/`frozen` snapshot dir in audio/g2d is swept in by `git add -A` at integration.
- **Smallest remediation:** finish the generalization (`live/*/frozen/` + `live/*/*tree*/` + `live/*/*{extract,snapshot,head,base}*/` is still whack-a-mole) — better: adopt g3d's posture (`live/` ignored + explicit allowlist for committed receipts) or a per-seat prefix convention (`live/rNN-<seat>/**` ignored except `receipt*`/`*.tsv`).

### F5 — LOW: audio r69-scout wrote outside its scope into a doubled `corpus/live/corpus/live/r69-scout/` path
- **Evidence:** `audio-shokunin/corpus/live/corpus/live/r69-scout/{runs,logs}` created 07:49; log files carry **literal `*` filenames** (`*.file.stderr`, `*.fifo_path.stderr` — an unexpanded glob in a redirect target). Real `corpus/live/r69-scout/logs/` has correctly-named `nm_*.stderr` — the stray tree is a path-relative write bug producing a partial second copy. 20K, audio-only (other lanes clean), **unignored** → commit-sweep + evidence-fork risk at integration.
- **Smallest remediation:** delete `corpus/live/corpus/` at integration; seat harness should anchor scratch paths to the lane root, not cwd.

### F6 — LOW: stale tracked `.shokunin/reports/` mirror in worktrees (persists, still frozen)
- Newest tracked mirror files unchanged: audio round-61, g2d round-59, g3d round-68; **zero writes since Oct 13** (canonical reports land in `*-shokunin/reports/`). Divergence is stable-frozen; w7 remediation (`git rm -r --cached` or README pointer) not taken. Risk unchanged: a reader inside the prymeagnt clone sees truncated history.

### F7 — LOW: wave scratch dirs accumulate unignored (now 8 + this one)
- `??` in fleet repo: w4–w7 `xconnector-scratch`+`xsentinel-scratch` (8 dirs) + this wave's two in flight. Fleet `.gitignore` still only `*-shokunin/` — same blanket-add vector as F4, one level up.
- **Smallest remediation:** `.ufo/waves/*/*-scratch/` ignore rule, or sweep at closeout.

## 3. Clean checks (PASS)

- **Secrets:** 0 real credentials. Tracked hits: `round-9/corpus-gate.mjs:660` labeled-synthetic `ghp_` fixture ("never real"), `aggregator-r11/seats/sentinel.md` matching `sk-` in a *description of a scan pattern* — both meta/fixture, not credentials. Untracked w7+w8 wave dirs and all in-flight `r69/r68/r77` seat scratch: 0 strict-pattern hits; generic `token|key|password[:=]` hits are prose (`observations.md:161` "inside the token:") and minified three.js inside snapshots — false-positive class.
- **Symlink integrity:** `.shokunin/{audio,game-dev-2d,game-dev-3d}` committed blob (mode 120000) **byte-identical to on-disk `readlink`** for all three; **zero broken symlinks** across fleet + worktrees; no `.shokunin` links inside any snapshot.
- **LEAF/process hygiene:** 0 stashes in all 5 repos; all three lane HEADs are their w7 report-last commits (pre-dispatch) — **zero post-dispatch lane commits**; worktrees clean (0 porcelain); only fleet commit after w7-closeout is the w8 dispatch itself.
- **Uncommitted tracked-worthy reports:** none stale. All w4–w7 wave reports/specs/registries tracked; w8 dir tracked (`spec.json`/`tasks/`/`dispatch.json`/`swarm-registry.json` in `621b92c`); only in-flight `xconnector-report.md` (landed 07:52) + this report pending — the designed LEAF→parent flow.
- **Lane HEAD vs registry:** lane HEADs `7b8d423`/`1101cb3`/`e417365` match the w7 closeout report-last commits; `dispatch.json` seat fields are 8-hex session IDs (not base SHAs — no base pinning, same as prior waves).

## 4. INFO

- `dispatch.json` `dispatched_at` "2026-10-14T10:45Z" is **true UTC** (commit 10:47:11 UTC) — the w7 local-mislabeled-Z flip did **not** recur; spawn-mtime-before-commit skew persists (~2min).
- Absolute-path symlinks inside snapshots (resolve today, break on repo relocation): g2d `r67-simplifier/del-measure/fixtures/*` (~35 links → `corpus/fixtures/`), `r66-simplifier/tree/lessons`, g3d `r76/r77-reviewer/head/.../node_modules` → live repo node_modules. All targets in-repo; no escapes, no cycles.
- g3d `head/` snapshots link `node_modules` rather than copy — cheaper than baseline's copy; both are outside-archive methods.
- Audio `corpus/live/runs/` flood in flight (~2 dirs/sec at 07:5x): r69-reviewer ledger replay receipts; `runs/` carries 4,670 tracked files already — normal receipt flow, unignored by design.
- 20/24 domain seat dirs present at census; audio `r69-author`, g2d `r68-author`, g3d `r77-{author,critic,scout}` not yet spawned — wave still mid-spawn.

## Severity summary

| # | severity | item |
|---|---|---|
| F1 | MEDIUM | g3d r77-baseline: populated working-tree copy + 1,264 untracked node_modules — archive-only brief violated (audio/g2d comply) |
| F2 | MEDIUM | identity drift: fleet 3 authors in 15 commits; all lane configs `ci`; **all 3 worktrees** now default to `games-engine-mechanics` |
| F3 | MEDIUM | ~1G/wave regenerable mass continues (archives now, still unbounded); 2.2G flagged dead mass still on disk in g2d |
| F4 | LOW | `*tree*/` verified for tree-class; non-tree names (`runs-extracted` 1.1M live, `head`, `snapshot`, `extracted`) still unignored in audio/g2d |
| F5 | LOW | audio stray `corpus/live/corpus/live/r69-scout/` — path bug, literal-`*` filenames, unignored |
| F6 | LOW | stale tracked `.shokunin/reports/` mirror in worktrees (frozen, diverged) |
| F7 | LOW | 8+ wave scratch dirs unignored in fleet repo |
| — | INFO | `dispatched_at` correctly UTC this wave; absolute-path fixture/node_modules symlinks in snapshots; wave mid-spawn at census |
| — | PASS | 0 real secrets; symlinks committed==on-disk, 0 broken; 0 stashes; no post-dispatch commits; archive-compliance 2/3 |

Read-only census. No mutations performed; report + `xsentinel-scratch/` only, per scope. In-flight items (F1 residue, F5 stray dir, baseline tars) should be re-verified at w8 integration/closeout.
