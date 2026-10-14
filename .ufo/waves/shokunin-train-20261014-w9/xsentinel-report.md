# xsentinel report — wave-9 adversarial hygiene/security census (cross-lane, early-wave)

Wave: shokunin-train-20261014-w9 · Dispatch commit `35813cc` (2026-10-14 08:58:09 -0300, `ci`) · Census taken ~09:00–09:20 -0300 **while seats are spawning** — earliest stage yet again: only 6 seat dirs exist in lanes (`audio r70-{critic,scribe}`, `g2d r69-scribe`, `g3d r78-{boundary,scribe,simplifier}`), **no r70/r69/r78 baseline dirs minted yet**. Verdicts on in-flight items are flagged for closeout re-check.
Scope: fleet `~/Projects/shokunin`, lane repos `audio-shokunin` / `game-dev-2d-shokunin` / `game-dev-3d-shokunin`, worktrees `~/Projects/prymeagnt{,/audio,/game-dev-2d,/game-dev-3d}`.
Scratch: `.ufo/waves/shokunin-train-20261014-w9/xsentinel-scratch/` (identity-census.txt, check-ignore.txt, shokunin-links.txt, sizes-blobs.txt, secrets.txt).
Continuity: fifth consecutive sentinel census; w8 findings F1–F7 re-checked below.

## Verdict line

No exploit-grade finding: zero real credentials, zero broken symlinks (all 3 worktree `.shokunin/<lane>` links committed==on-disk), zero stashes, no post-dispatch lane commits, LEAF discipline holding. **w8 remediations verified landed**: F4 ignore broadening is in tree (`audio 939fe47`/`g2d 5d66b4d` — all five flagged names now covered), F7 fleet `*-scratch/` ignore works, F5 doubled-path did not recur. **Persistent**: identity drift (F2) now spans **4 worktrees** incl. the prymeagnt root itself; ~2.2G flagged dead mass still on disk (F3, 4th census); worktree `.shokunin/reports/` mirrors still frozen (F6). **New this census**: tracked `__pycache__`/`*.pyc` files swept in by `git add -A` (audio 22, g2d 27, fleet 3 — g3d 0 thanks to its `__pycache__/` rule; causal contrast proven). F1 (g3d archive-only) **cannot be re-judged yet** — w9 baselines unminted; the w8-violation tree persists on disk per closeout decision.

## 1. >50MB blobs & snapshot embedding — PASS on tracked paths; F1 verdict deferred to closeout

**Tracked paths clean of new giants.** Fleet: none (largest ~240K `.ufo` reports). Audio/g3d: none. g2d: the same 7× 70.3MB `fixture.x86_64` under `corpus/live/r25-{export-scout,export-critic,pair-reviewer}` (≈492M committed) — pre-existing mass flagged since w6, no new members. Zero tracked `node_modules` in all lanes.

**Baseline compliance — w9 seats have not minted baselines.** `r70-baseline` (audio), `r69-baseline` (g2d), `r78-baseline` (g3d) all absent at census time. The F1 re-check is therefore **deferred to w9 closeout**. What is verifiable now:
- The w8 violation's residue persists: `g3d corpus/live/r77-baseline/frozen/` is still the 1,680-file / 27M populated working-tree copy (incl. untracked `node_modules` content) — kept per w8 closeout ("replay still valid — blanket-ignored"). It is ignored on disk (g3d `live/` blanket) so it cannot be swept in, but it remains a non-archive freeze on record.
- **The w8-suggested remediation landed in the briefs**: all three w9 baseline briefs now carry verbatim the receipt check `comm -23 <(find frozen-extract -type f | sort) <(git ls-files | sort)` must be EMPTY, plus "archive output only (no populated-tree extraction)". The clause g3d violated in w8 is now a stated, verifiable receipt line — recurrence this wave is brief-violation on a self-check, not ambiguity.
- Archive-only form held where minted: audio `r69-baseline` = `head-7b8d423.tar` 169M+manifest+sha256 (w8, compliant); g2d `r68-baseline` = `HEAD-1101cb3...tar` 626M (w8, compliant).

## 2. Findings

### F1 — MEDIUM (carried, unverifiable this census): g3d archive-only baseline mandate — w9 recurrence pending
- **Evidence:** w9 `r78-baseline/` absent (seats mid-spawn); w8 violation tree `r77-baseline/frozen/` still on disk (1,680 files, 27M, ignored). The w9 g3d baseline brief (tasks/g3d-baseline.txt:21,23) carries the strengthened mandate + `comm -23` emptiness receipt.
- **Exploit/failure path:** unchanged — a populated-tree freeze is not a clean tracked-files oracle (untracked vendor code reachable from fixtures), and if the copy method recurs in audio/g2d it re-opens the untracked-baseline recursion the mandate was written to kill.
- **Smallest remediation:** at w9 integration, verify `r78-baseline/frozen/` contains only `*.tar`(+manifest/proofs) — now directly receipt-checkable via the brief's own `comm -23` clause; if extracted form recurs, treat as repeat brief-violation, not a new finding. Owner: g3d parent/operator.

### F2 — MEDIUM (persists, one surface wider): commit-identity drift across fleet, lanes, and all worktrees
- **Fleet:** static config `ci <ci@local>`; last 15 commits span **3 identities** — `ci`×5 (incl. w9 dispatch `35813cc` + w8 closeout `af15cf2`), `devin-fleet`×4, `shokunin-fleet`×6.
- **Lanes:** all three static configs `ci <ci@local>`; last-15 author spread — audio 3 identities (name-stable `audio-shokunin`, email thrash `audio-shokunin@local` vs `audio@shokunin.local`), g2d 3, g3d **4** (`game-dev-3d-shokunin` under three emails: `g3d@`, `game-dev-3d-shokunin@`, `game-dev-3d@`).
- **Worktrees: now all four** — `prymeagnt` root itself plus `audio`, `game-dev-2d`, `game-dev-3d` all static-config `games-engine-mechanics-shokunin <games-engine-mechanics@shokunin.local>`. A LEAF slip or operator commit in any worktree writes foreign-lane provenance.
- **Impact:** author-keyed provenance unverifiable; any shell-reaching principal commits as `ci`/`games-engine-mechanics` indistinguishably. Correctness defect, not intrusion (subjects/timestamps coherent). Now 8 wrong-default surfaces (4 worktrees + 3 lanes + fleet).
- **Smallest remediation:** pin `user.name`/`user.email` per repo (fleet→`shokunin-fleet`, lanes→lane identity, worktrees→own lane). Unchanged since w7.

### F3 — MEDIUM (persists, 4th census): baseline mass trajectory + 2.2G flagged dead mass still on disk
- **Totals:** audio 1,272M→**1,521M** (+249M; r69-baseline 217M incl. tar is the bulk), g2d 3,640M→**3,671M** (+31M), g3d 268M→**288M** (+20M). No w9 baseline mass yet — the +X G/wave step lands at integration.
- **Dead mass re-check — all four items still present:** `r63-baseline/tree` 682M, `r65-boundary/edge-verdicts.json` 117M, `r66-baseline/frozen` (extracted) 700M, `r67-baseline/frozen` (extracted) 711M ≈ **2.2G in g2d alone**, flagged in every census since w6/w7 and still on disk.
- **Impact:** waste trajectory, not exhaustion (`/home` ample); every census/scan re-walks ~5.5G.
- **Smallest remediation:** post-adjudication delete of the four flagged items (keep tars/manifests/receipts); consider `git archive | zstd` or hash-only freeze receipts.

### F4 — LOW→RESOLVED-named, residual class open: ignore broadening verified; tail names still uncovered
- **Verified landed:** audio `corpus/.gitignore` and g2d `corpus/.gitignore` (commits `939fe47`/`5d66b4d`) add `live/*/head/`, `live/*/snapshot/`, `live/*/base/`, `live/*/*extract*/`. `git check-ignore` battery: every w8-flagged name (`tree`, `head-tree`, `pretree`, `worktree`, `frozen`, `snapshot`, `head`, `extracted`, `runs-extracted`, `base`) now IGNORED in audio+g2d; the live `runs-extracted/` specimen class is covered by `*extract*/`. g3d blanket `live/` still covers everything.
- **Residual uncovered names (verified exit-1 in audio+g2d):** `archive/`, `snap/`, `backup/`, `tmp/`, `HEAD/` (case-sensitive vs `head/`), `head.tar` (file, not dir), and the doubled prefix `corpus/live/corpus/`. `out/`+`runs/` unignored in audio by design (tracked receipt flow); `runs/` ignored in g2d.
- **Impact:** narrower than ever but still whack-a-mole — a seat minting any residual name in audio/g2d is swept in by `git add -A`.
- **Smallest remediation:** stop enumerating names — per-seat prefix convention (`live/rNN-<seat>/**` ignored except `receipt*`/manifests) or g3d's blanket+allowlist posture.

### F5 — RESOLVED this wave: doubled `corpus/live/corpus/` path did not recur
- No top-level `corpus/live/corpus` in any lane; zero literal-`*` filenames anywhere under `corpus/live`. The nested `frozen/corpus/` hits are embedded tracked-evidence inside snapshot trees (expected, ignore-covered). No audio-side stray writes from w9 seats so far. Watch item closed unless it recurs at scale.

### F6 — LOW (persists, frozen): stale tracked `.shokunin/reports/` mirrors in worktrees
- Newest tracked mirror files unchanged since w8: audio round-61, g2d round-59, g3d round-68 — zero writes since Oct 13; canonical reports land in `*-shokunin/reports/`. Stable-frozen divergence; remediation (`git rm -r --cached` or README pointer) not taken. Same risk: a reader inside the prymeagnt clone sees truncated history.

### F7 — RESOLVED: fleet `*-scratch/` ignore works
- `.gitignore:3` `.ufo/waves/*/*-scratch/` (commit `31c8f61`) verified matching w8+w9 scratch dirs via `check-ignore -v`. Fleet `git status --porcelain` is clean — all 8 prior scratch dirs now ignored (still on disk, but no commit-sweep vector). Wave dir tracking correct: `spec.json`/`dispatch.json`/`swarm-registry.json`/`tasks/` all committed in `35813cc`.

### F8 — LOW (new): tracked `__pycache__`/`*.pyc` swept in by integration `git add -A`; still accumulating unignored
- **Evidence:** tracked `.pyc` files — audio **22** (incl. w8-round dirs `r69-author/baseline/boundary/verifier` — swept at w8 integration), g2d **27** (r61–r68 seat dirs incl. `fault-runs/*/scratch/`), fleet **3** (`.ufo/waves/round-1{2,3}`), g3d **0**. The contrast is causal: g3d's `corpus/.gitignore` carries `__pycache__/`+`*.pyc`; audio/g2d/fleet carry no pycache rule anywhere (no lane-root `.gitignore` exists in any lane). **~25 more unignored `__pycache__` dirs sit in audio+g2d live paths right now** (verified `check-ignore` exit 1; audio porcelain already shows `?? corpus/live/r68-author/__pycache__/`).
- **Exploit/failure path:** same commit-sweep vector as F4/F5 — nondeterministic bytecode lands in tracked evidence (embeds absolute build paths + timestamps → provenance noise; silently replays stale code if a `.pyc` outlives its `.py`). Low mass (~10–20K each) but the sweep recurs every integration.
- **Smallest remediation:** add `__pycache__/` + `*.pyc` to audio+g2d `corpus/.gitignore` (one-line, proven by g3d) and to the fleet `.gitignore`; `git rm -r --cached` the 52 tracked `.pyc` files at next integration.

## 3. Clean checks (PASS)

- **Secrets:** 0 real credentials. Tracked strict-pattern hits remain the two known fixtures (`round-9/corpus-gate.mjs:660` labeled-synthetic `ghp_`; `aggregator-r11/seats/sentinel.md` describing a scan pattern). Zero strict hits in w9 wave dir, w9 seat dirs, or untracked lane files.
- **Symlink integrity:** `.shokunin/{audio,game-dev-2d,game-dev-3d}` committed gitlinks (mode 120000) **byte-identical to on-disk `readlink`** in all three worktrees; **zero broken symlinks** across fleet + lanes + worktrees (`find -xtype l` empty). No `.shokunin` inside any w8/w9-era snapshot.
- **LEAF/process hygiene:** 0 stashes in all 7 repos; lane HEADs `939fe47`(08:48)/`5d66b4d`(08:48)/`71818b7`(08:56) all pre-date the w9 dispatch commit (08:58:09) — **zero post-dispatch lane commits**; all 4 worktrees 0-porcelain; only fleet commit after w8-closeout is the w9 dispatch itself.
- **Lane HEAD vs registry:** lane HEADs match w8 closeout report-last + the two F4 ignore commits; `dispatch.json` seats are 8-hex session IDs (no base pinning, as designed).

## 4. INFO

- `dispatch.json` `dispatched_at` "2026-10-14T11:56Z" = true UTC (commit 11:58:09 UTC; ~2min spawn-before-commit skew, same as w8) — the local-mislabeled-Z bug has not recurred in two waves.
- Absolute-path symlink inside a w8 snapshot: g3d `r77-reviewer/head/corpus/fixtures/three/node_modules` → `/home/vgpnk/Projects/shokunin/game-dev-3d-shokunin/corpus/fixtures/three/node_modules` (in-repo target; resolves today, breaks on repo relocation — same class as w8's g2d fixture links).
- g2d untracked `reports/round-68/r68-boundary.md` + `r68-verifier.md` — legitimate w8 seat reports pending parent commit (not stale-bad; commit at w9 integration).
- Wave spawn state at census: 6/24 domain seat dirs; audio `r70-critic` minted empty (mid-spawn), g3d `r78-boundary`/`scribe` carrying only `scratch/{project.godot,smoke.gd}`-scale files; g2d only `r69-scribe` so far.
- Historical `.shokunin` **real dirs** embedded inside g2d `r35/r36-baseline-reviewer` frozen trees (pre-symlink-era captures, ignore-covered, not link cycles) — noted for completeness only.

## Severity summary

| # | severity | item |
|---|---|---|
| F1 | MEDIUM (deferred) | w9 baselines unminted — archive-only recurrence unverifiable; w8 violating tree persists (ignored); brief now self-checks via `comm -23` |
| F2 | MEDIUM | identity drift: fleet 3 authors/15 commits, all lane configs `ci`; **all 4 worktrees** incl. prymeagnt root default `games-engine-mechanics` |
| F3 | MEDIUM | baseline mass ~linear (audio +249M this wave); 2.2G flagged dead mass still on disk, 4th census |
| F4 | LOW→resolved-named | w8-flagged names all covered; residual tail (`archive/ snap/ backup/ tmp/ HEAD/ head.tar`, doubled prefix) still whack-a-mole |
| F5 | resolved | doubled `corpus/live/corpus/` absent; zero literal-`*` filenames |
| F6 | LOW | worktree `.shokunin/reports/` mirrors frozen at r61/r59/r68, unchanged |
| F7 | resolved | fleet `*-scratch/` ignore verified via `check-ignore` |
| F8 | LOW (new) | 52 tracked `*.pyc` (audio 22/g2d 27/fleet 3, g3d 0 — causal rule contrast); ~25 unignored `__pycache__` dirs still accumulating in audio+g2d live |
| — | INFO | `dispatched_at` correctly UTC again; abs-path node_modules symlink in g3d r77 snapshot; wave mid-spawn (6/24 dirs) |
| — | PASS | 0 real secrets; symlinks committed==on-disk, 0 broken; 0 stashes; no post-dispatch commits; no new >50MB tracked blobs |

Read-only census. No mutations performed; report + `xsentinel-scratch/` only, per scope. In-flight items (w9 baseline form, g2d report commits) should be re-verified at w9 integration/closeout.
