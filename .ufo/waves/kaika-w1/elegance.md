# kaika W1 — Elegance & bloat census (read-only)

Author: W1Elegance · Date: 2026-10-19 · Scope: fleet root `/home/vgpnk/Projects/shokunin` (root + 21 `*-shokunin` lanes) and `/home/vgpnk/Projects/kimi-shokunin` (upstream plugin, not a lane).
Method: local census only; `web_search` not needed. No repo file was edited, moved, deleted, staged, or committed. The shell's `cd` was unreliable in this session, so every command below uses absolute paths.

## 0. Commands behind the counts

- Sizes: `wc -c <lane>/SKILL.md <lane>/LOG.md <lane>/SCORECARD.md <lane>/PROVINCE.md` (lines: `wc -l`).
- Contract presence: `for f in SKILL.md PROVINCE.md SHONEN.md AGENTS.md corpus/README.md corpus/QUALITY.md corpus/lessons corpus/knowledge corpus/SOURCES.md; do test -e <lane>/$f || echo MISSING $f; done`.
- Tracked strays: `git -C <lane> ls-files | grep -cE '\.out$'`, same for `\.log$`, `err`, media `\.(wav|png|mp3|pdf|html|plot)$`, and `^\.ufo/`.
- Repo weight: `git -C <lane> count-objects -v` (size-pack, KiB); tracked bytes = sum of `stat` over `git -C <lane> ls-files -z`.
- Empty dirs: `find <lane> -path '*/.git' -prune -o -type d -empty -print | wc -l`.
- Roster: `jq -r '.roster[].name' /home/vgpnk/Projects/shokunin/MANIFEST.json`; ledger rows per lane: `jq '[.rounds[] | .lane] | group_by(.) | map({k:.[0],n:length})'` (rows lacking `.lane` counted separately).
- Frontmatter: `sed -n '1,8p' <lane>/SKILL.md` and count quoted trigger strings and anti/sibling wording in `description:`.
- Generic advice: `grep -ciP '(?<!un)readab|\bmaintainab|\bclean code|\belegan|best practice|\byou are (a|an|the)\b|\bbe (concise|thorough|careful|helpful)\b|\bhigh[- ]quality\b|\bedge cases?\b' <lane>/SKILL.md`.
- Pointers: regex `(?:[A-Za-z0-9_.-]+/)+[A-Za-z0-9_.-]+\.(md|sh|py|json|tsv|toml|mjs|ts|js|txt|csv|yml|yaml)(:\d+(-\d+)?)?` over `SKILL.md`, `PROVINCE.md`, `corpus/README.md`; each hit tested for existence relative to lane root, doc dir, fleet root, and every sibling lane. Line-range validity was NOT checked.

## 1. Per-lane document sizes (bytes / lines)

| lane | SKILL.md | LOG.md | SCORECARD.md | PROVINCE.md | SHONEN.md |
|---|---|---|---|---|---|
| audio | MISSING | 466,689 / 1585 | 131,581 / 915 | 4,738 / 31 | 1,131 / 9 |
| chousa | 40,280 / 434 | 86,788 / 820 | 85,467 / 1232 | 880 / 17 | 354 / 8 |
| game-dev-2d | MISSING | 336,796 / 1324 | 49,593 / 366 | 825 / 12 | 404 / 9 |
| game-dev-3d | 24,496 / 199 | 284,959 / 1500 | 53,455 / 345 | 2,683 / 47 | 561 / 9 |
| kagi | 57,062 / 663 | 68,885 / 963 | 77,831 / 621 | 8,172 / 53 | 4,695 / 11 |
| kaidoku | 35,022 / 427 | 111,338 / 1683 | 137,290 / 2027 | 20,188 / 162 | 1,327 / 12 |
| kake | 33,229 / 375 | 57,570 / 598 | 20,249 / 156 | 334 / 6 | 361 / 8 |
| kama | 25,627 / 342 | 32,059 / 514 | 13,022 / 188 | 4,339 / 52 | 956 / 11 |
| kasegi | 81,063 / 1012 | 72,359 / 1044 | 23,857 / 301 | 1,570 / 25 | 363 / 8 |
| kengaku | 51,245 / 640 | 51,906 / 206 | 65,792 / 558 | 8,670 / 93 | 1,521 / 12 |
| kotoba | 34,111 / 521 | 418,078 / 2298 | 108,084 / 264 | 326 / 6 | 6,685 / 50 |
| kotodama | 88,286 / 732 | 252,395 / 3945 | 107,271 / 952 | 1,636 / 31 | 505 / 11 |
| kumitate | 51,131 / 782 | 102,828 / 1409 | 148,094 / 1586 | 326 / 6 | 365 / 8 |
| lore | 18,840 / 103 | 803,535 / 3634 | 83,297 / 694 | 802 / 11 | 1,422 / 12 |
| mado | 116,306 / 1580 | 45,226 / 654 | 30,029 / 219 | 891 / 18 | 1,036 / 12 |
| mori | 17,364 / 219 | 32,423 / 540 | 44,143 / 592 | 942 / 18 | 352 / 8 |
| revenger | MISSING | 195,343 / 764 | 26,965 / 156 | 1,902 / 32 | 1,177 / 12 |
| souji | 6,985 / 106 | 25,075 / 451 | 4,085 / 57 | 2,010 / 45 | 502 / 11 |
| tabi | 125,194 / 1595 | 39,496 / 460 | 34,018 / 391 | 1,020 / 21 | 2,588 / 40 |
| tameshi | 99,223 / 1476 | 38,842 / 549 | 25,087 / 173 | 1,049 / 20 | 827 / 12 |
| tsukuroi | 144,943 / 1636 | 29,536 / 362 | 20,757 / 170 | 6,531 / 73 | 1,330 / 12 |
| kimi (`skills/shokunin/SKILL.md`) | 12,136 | — (no root LOG) | — | — | — |

Totals (sum of the `wc -c` column above; re-derive with `cat */SKILL.md | wc -c` over the 18 present files): SKILL.md ≈ 1.05 MB; LOG.md ≈ 3.55 MB; SCORECARD.md ≈ 1.29 MB.
Fleet root: `MANIFEST.json` 306,760 B; `LOG.md` 131,795 B; `SCORECARD.md` 59,226 B; `PROTOCOL.md` 44,449 B.

Largest SKILL.md: tsukuroi 144,943 · tabi 125,194 · mado 116,306 · tameshi 99,223 · kotodama 88,286 · kasegi 81,063.
Largest LOG.md: lore 803,535 · audio 466,689 · kotoba 418,078 · kotodama 252,395 · game-dev-2d 336,796.

## 2. Contract-required files missing per lane

Contract sources: `PROTOCOL.md` §File contract (SKILL, PROVINCE, LOG, SHONEN, AGENTS, corpus/, SCORECARD); wave brief adds `corpus/QUALITY.md`, `corpus/lessons/`, `corpus/SOURCES.md` (wave 2 creates SOURCES).

| file | missing in |
|---|---|
| SKILL.md | audio, game-dev-2d, revenger (3) |
| PROVINCE.md | none |
| SHONEN.md | none (all 21 present; MANIFEST rank `shonen` for the 13 rostered) |
| AGENTS.md (PROTOCOL file contract) | audio, game-dev-2d, lore, revenger (4) |
| corpus/README.md | audio, revenger (2) |
| corpus/QUALITY.md | audio, game-dev-2d, game-dev-3d, kagi, kasegi, kengaku, kotoba, kumitate, lore, revenger, souji (11) |
| corpus/lessons/ | audio, lore (2) |
| corpus/SOURCES.md | all 21 (expected until wave 2) |
| kimi-shokunin | no lane files at root by design; it is the upstream plugin (`skills/shokunin/`, `templates/mint/`), no `corpus/` |

Three lanes (audio, game-dev-2d, revenger) have no SKILL.md, so PROTOCOL's "scoped SKILL.md + PROVINCE.md" seed is incomplete there. Revenger's `corpus/` root also holds 10 `verify_*.py` scripts that belong under `tools/` or `scripts/`, not the corpus root.

## 3. Stray artifacts

| item | evidence (command) | tracked? | class |
|---|---|---|---|
| Root dir named `bash: ` (nested dirs mirroring the path inside the error string `bash: /home/vgpnk/…/souji-verify.sh: No such file or directory`; one 10,139-byte file) | `find 'bash: ' -printf '%y %s %p\n'`; contents are a shell error string used as a path | not in `git ls-files`; `git status --porcelain` at root reports nothing for it — unexplained, verify before any action | souji hygiene |
| Root `.scratch/`: 10 `*.out` (115–127 B each) + `goal-…-2d-training.md` (8.3 KB) + empty `r23-replay-mirrors/` | `ls -la .scratch` | 11 files tracked (`git ls-files .scratch \| wc -l`) | souji hygiene |
| Root empty dirs `local/fleet-analysis/`, `reports/` | `find local reports -maxdepth 1 -type d -empty` | no files | souji hygiene |
| souji `err4.z2`, `err4.nl2` (67 B each: "souji-census: compare file header mismatch (want 7 census columns)") | `cat souji-shokunin/err4.*` | tracked | souji hygiene |
| souji `tools/`: 120 entries, 111 are candidate/versioned copies (`cand-*-verify.sh` ×16, `souji-vault-verify.impl-NN.sh` ×9, `souji-verify.impl-09…16.sh`, `*.r9-s18.sh`), 3 symlinks (`impl-21.sh`, `impl-39.sh`, `souji-census.impl-40.sh`) | `ls souji-shokunin/tools \| grep -cE 'cand-\|\.impl-\|r9-s18\|^impl-'` = 111 | tracked | souji hygiene |
| souji `census/`: 11 round dirs, 507 tracked files, 55 MB | `git -C souji-shokunin ls-files \| grep -c '^census/'` | tracked | souji hygiene (historical evidence) |
| audio root `Timing1–5.plot`, `Timings.html` (ignored by `.gitignore:4`, present on disk); `generate_timings.sh` tracked | `git check-ignore -v Timing1.plot` | plot/html ignored; generator tracked | souji hygiene (regenerable) |
| audio `corpus/live/`: 1,538 `.out`, 5,678 `.log`, 3,336 media (wav/png/mp3/pdf/html/plot); 1,320.9 MB tracked | `git ls-files \| grep -cE …` | tracked | souji hygiene / lane policy |
| game-dev-2d `corpus/live/`: 2,236 `.out`, 893.9 MB tracked | same | tracked | souji hygiene / lane policy |
| game-dev-3d `reports/`: 406.0 MB tracked; 4,483 `.log` | same | tracked | souji hygiene |
| kaidoku `.ufo/waves/`: 2,052 `.out`; `.ufo` 14,731 files / 132.4 MB tracked | same | tracked | souji hygiene |
| kotoba `.ufo/`: 9,527 files / 93.2 MB tracked; lore `.ufo/`: 3,468 files / 31.0 MB tracked; root `.ufo/`: 2,128 files tracked | same | tracked | souji hygiene (policy question) |
| kotodama `.scratch/`: 62 GB apparent, gitignored (`.scratch/` in lane `.gitignore`), ~83k subdirs | `du -sh --apparent-size kotodama-shokunin/.scratch` | ignored | souji hygiene (highest disk win) |
| kotodama nested `kotodama-shokunin/kotodama-shokunin/reports/round-29/…` (directories only, 0 files) and empty `out/` | `find … -type f \| wc -l` = 0 | not tracked | souji hygiene |
| Empty directories: audio 576, game-dev-2d 134, game-dev-3d 50, kama 15, kotodama 12, kaidoku 11, kotoba 24, lore 9, souji 6, kake 1, tameshi 1 | `find <lane> -path '*/.git' -prune -o -type d -empty -print \| wc -l` | none | souji hygiene |
| `.tower/worktrees/kaika`: 43 GB at first read, 68 GB at second (live, changing); `.tower/` excluded only via `.git/info/exclude` | `du -sh --apparent-size .tower/worktrees` | excluded | NOT a candidate while the wave runs — operator/tower decision |
| Repo packs: audio `size-pack` 293,533 KiB; game-dev-2d 260,765; game-dev-3d 52,343; kaidoku 25,171; kotoba 22,226; lore 18,093; kotodama 17,677; souji 8,791 | `git -C <lane> count-objects -v` | — | context for the tracked-artifact moves |

Removing tracked artifacts from HEAD does not shrink `.git`; shrinking packs needs history rewrite, which is an operator decision.

## 4. Generic agent advice in SKILL.md

Result: no clear instance found. The pattern sweep (`grep -ciP`, §0) hit six lines in tsukuroi and two each in kotodama and kagi, but on reading they are domain claims ("unreadable probe → BLOCKED", "maintainable" in a pacman-state definition, "machine-readable pattern/output pair" in kotodama). kimi-shokunin `skills/shokunin/SKILL.md` (12,136 B) has zero hits.

The actual SKILL-file defect is frontmatter conformance, which PROTOCOL.md (§File contract, `SKILL.md` row) requires to carry quoted trigger strings, an anti-trigger, and a sibling-arbitration note. Ten lanes fail (description length, quoted triggers, anti/sibling wording):

| lane | description chars | quoted triggers | anti/sibling |
|---|---|---|---|
| kagi | 120 | 0 | no |
| kake | 119 | 0 | no |
| kama | 141 | 0 | no |
| kasegi | 121 | 0 | no |
| kengaku | 259 | 0 | no |
| kumitate | 131 | 0 | no |
| mado | 73 | 0 | no |
| tabi | 78 | 0 | no |
| tameshi | 73 | 0 | no |
| tsukuroi | 79 | 0 | no |

Eight lanes pass (chousa, game-dev-3d, kaidoku, kotoba, kotodama, lore, mori, souji). kimi has 416 chars, 3 quoted, no anti/sibling.

## 5. Dead internal pointers

Full scan (not a sample) of pointers in SKILL.md, PROVINCE.md, corpus/README.md: 2,868 tokens.
- 2,181 resolve in-lane.
- 61 resolve in another lane or fleet root (cross-lane references, e.g. tabi→kaidoku, tameshi→kumitate/kagi). These are path-base errors, not missing files.
- 38 classified IN-LANE-DEAD: the first path component exists in the lane but the target does not.
- 588 unverifiable: 401 are kasegi (see below); the remainder are external-repo paths (kake `src/…`, kumitate `.omp/`, `config/`) or placeholders.

In-lane dead, by lane (verified by `ls`):

- **kasegi (SKILL.md, 4 in-lane + 401 absent-root):** SKILL.md cites `ops/` (228), `claims/` (58), `docs/` (49), `fleets/` (23), `evidence/` (11), `ledger/` (10), `bounty-map/` (9), `submit/` (5); none exist in the lane (`ls`: `.git .gitignore .ufo AGENTS.md LOG.md PROVINCE.md SCORECARD.md SHONEN.md SKILL.md corpus plans`). PROVINCE.md:4-12 records the scope roots removed 2026-09-28 and absent again ~2026-10-12; `ls /home/vgpnk/Projects` shows no `bounties`, `the-bounty-hunter`, or `origin-work`. The SKILL is therefore ungrounded; the lane must annotate or retire it. Operator ruling is pending in `.ufo/l0-questions.md` (kasegi round-15 row, cited by PROVINCE.md).
- **kumitate (15):** SKILL.md:18–54 cite `scripts/ufo-swarm-wave.mjs` (absent; `ls scripts` has `cite-check.mjs claims-check.mjs kimi-census.mjs proxy-check.mjs round-gate.mjs surface-probe.mjs`), `scripts/ufo-sighting-lib/surface.mjs`, `scripts/run-omp-native-trial.mjs`, `scripts/ufo-swarm-collect.mjs`.
- **mado (5):** `corpus/knowledge/arc-closeout.md` cited at SKILL.md:1458–1558; the file is `closeout-r11.md`.
- **kake (3):** `scripts/kimi-surface.mjs` (SKILL.md:219, 332); `ls scripts` = `freshness-sweep.mjs probe-delta.mjs`.
- **tabi (1):** `references/operations.md` (SKILL.md:65) — no `references/` dir; plus `corpus/knowledge/training-closeout.md` (SKILL.md:1341) absent.
- **tsukuroi (2):** `corpus/knowledge/oom-event-baseline.tsv` (SKILL.md:1140; file is `oom-event-plane.md`); `plans/round-1.plan.md` (SKILL.md:1416).
- **tameshi (2):** `plans/round-N.plan.md` / `round-N-record-draft.md` (SKILL.md:1393) — template placeholders, likely intentional.
- **lore (1):** SKILL.md:26 `corpus/knowledge/cross-cluster-contradictions.md`; file is `r89-cross-cluster-contradiction.md`.
- **mori (1):** SKILL.md:78 `corpus/evidence/baseline-r10-20261015T2210Z.json` absent.
- **kengaku (1):** SKILL.md:490 `corpus/evidence/round11-power/results-r11.json` absent.
- **chousa (1):** SKILL.md:113 `corpus/fixtures/claims-r2.json`; the lane has `claims-r2.jsonl`.
- **game-dev-3d (1):** SKILL.md:71 `corpus/knowledge/unreal-mcp/.manifest.d/audit-reference.sh`; the dir holds only `audit-reference.sha256`.
- **kotoba (1):** `corpus/README.md:44` `corpus/nope.md` — probably an illustrative negative example; verify before treating as dead.

Other: tabi SKILL.md:401–403 and tameshi SKILL.md:317–321 cite other lanes' files; these resolve in the sibling lane (cross-lane class) and are correct only if the sibling path is the canonical one.

## 6. Identity and ledger (fleet-root, not lane)

- MANIFEST `roster` has 13 entries. Eight lanes on disk are not in the roster: chousa, kotodama, mado, tabi, tameshi, tsukuroi (each with 5–10 ledger rows carrying a `lane` key), and mori, souji (no `lane`-keyed ledger rows). PROTOCOL requires the MANIFEST rank to be updated on promotion, so these lanes have no recorded rank.
- Roster `repo` field differs from local dir for six lanes (GitHub remote names: audio→`shokunin-game-audio`, game-dev-2d→`shokunin-godot-2d`, game-dev-3d→`shokunin-3d-engines`, lore→`shokunin-world-bible`, revenger→`shokunin-binary-forensics`, kaidoku→`shokunin-reverse-engineering`). `README.md:90` states canonical names are `<id>-shokunin`. Remote names are not dead pointers, but the identity mapping is undocumented in one place.
- Ledger: 294 `rounds[]` entries, 24 distinct key shapes; 214 entries have no single `lane` key (they carry `lanes`/`lane_rounds`). Counting rows per lane from `.lane` alone undercounts.
- All 21 lanes still carry SHONEN.md; no lane has been promoted. Promotion evidence was not evaluated.

## 7. Elegance moves, ranked by value × risk

Class key: **[souji]** = souji hygiene action (dry-run census first, per souji's removal flow); **[lane-R]** = lane round claim (exploratory or operability; needs before→after counting command); **[fleet]** = fleet-root integrator or operator decision, not a lane claim.

| # | move | class | value | risk | evidence | measure (before → after) |
|---|---|---|---|---|---|---|
| 1 | Reclaim kotodama `.scratch/` (62 GB, gitignored, ~83k subdirs) | [souji] | very high (disk) | low–med: confirm no LOG/SKILL pointer into `x58/`, `r22-*` | §3 | `du -sh --apparent-size kotodama-shokunin/.scratch` 62G → 0 |
| 2 | Resolve kasegi SKILL grounding: annotate ~400 absent-root pointers as `absent-source` or retire sections | [lane-R] after operator ruling in `.ufo/l0-questions.md` | very high (SKILL unexecutable as written) | high: rewriting grounding without the ruling would be re-scoping | §5 | count of pointers to absent roots 401 → 0 (annotated) |
| 3 | Untrack live captures and `.out`/`.log` from git (audio `corpus/live` 1.32 GB; game-dev-2d 894 MB; game-dev-3d `reports` 406 MB) | [souji] + [fleet] (history rewrite is operator) | high (clone size) | med–high: evidence pointers; untracking does not shrink `.git` | §3 | `git ls-files \| wc -l` and tracked bytes before/after |
| 4 | Untrack `.ufo/` runtime evidence (kaidoku 14,731 files; kotoba 9,527; lore 3,468; root 2,128) | [souji] + [fleet] policy | high | med: LOG and SKILL cite `.ufo/` paths (kasegi already dead there) | §3 | `git ls-files .ufo \| wc -l` 14,731 → 0 (kaidoku) |
| 5 | Frontmatter conformance on 10 lanes (quoted triggers, anti-trigger, sibling note) | [lane-R] | high (routing) | low (frontmatter only) | §4 | count of lanes passing grep 8 → 18 |
| 6 | Split long SKILL.md: tsukuroi 145 KB, tabi 125 KB, mado 116 KB, tameshi 99 KB; move round-history tables to `corpus/knowledge/`, keep decision tables and checklists in SKILL | [lane-R] | high (per-load context) | med: pointer churn; fix dead pointers in the same round | §1 | `wc -c SKILL.md` before → after; pointer check §0 |
| 7 | Fix in-lane dead pointers (38): kumitate 15, mado 5, kasegi 4, kake 3, tabi/tsukuroi/tameshi/lore/mori/kengaku/chousa/game-dev-3d/kotoba 1–2 each | [lane-R] per lane | med | low | §5 | in-lane dead 38 → 0 (tameshi placeholders excepted) |
| 8 | Missing `corpus/QUALITY.md` in 11 lanes; `AGENTS.md` in 4; `corpus/README.md` in 2; `corpus/lessons/` in 2 | [lane-R] (exploratory; authored per lane, not copied) | med | low | §2 | file-presence table §2 |
| 9 | Author SKILL.md for audio, game-dev-2d, revenger (3 lanes with no craft file) | [lane-R] (exploratory; multi-round) | high (no executable craft) | med: must cite sources, not generic advice | §2 | `test -e SKILL.md` 3 → 0; SHONEN box 1 verifier |
| 10 | Empty dirs and nested-empty trees (audio 576; game-dev-2d 134; game-dev-3d 50; kotoba 24; kama 15; kotodama 12 + nested `kotodama-shokunin/kotodama-shokunin/`; kaidoku 11; lore 9; souji 6; root `local/fleet-analysis`, `reports`) | [souji] | low | very low (directories only) | §3 | `find … -type d -empty \| wc -l` |
| 11 | Root `bash: ` tree and root `.scratch/*.out` (10 tracked) and souji `err4.*` (2 tracked) | [souji] | low (clarity; removes misleading paths) | very low; first confirm why git status omits `bash: ` | §3 | `find 'bash: ' -type f \| wc -l` 1 → 0 |
| 12 | audio root `Timing1–5.plot`, `Timings.html` (ignored) — regenerate via `generate_timings.sh`, or move out | [souji] | low | very low | §3 | `ls audio-shokunin/*.plot \| wc -l` 5 → 0 |
| 13 | souji `tools/` candidate copies: 111 of 120 → keep canonical `souji-verify.sh`, `souji-vault-verify.sh`, `souji-verify.spec.md`; archive numbered copies | [souji] (self-referential: souji owns it) | med (120 → ~9 files) | med: LOG may cite `impl-NN` by number; grep first | §3 | `ls souji-shokunin/tools \| wc -l` 120 → 9 |
| 14 | souji `census/`: 507 tracked files, 57 MB across 11 round dirs → keep summaries, archive per-seat JSON with a manifest | [souji] | med | med: historical evidence | §3 | tracked bytes of `census/` 57 MB → summary-only |
| 15 | Reconcile MANIFEST roster with the 8 unrostered lanes and document the remote-name mapping (6 lanes) | [fleet] integrator | med (identity) | med: append-only ledger | §6 | roster count 13 → 21 |
| 16 | `LOG.md` growth: lore 803 KB, audio 467 KB, kotoba 418 KB — rotate to archive files | [fleet] protocol amendment; not a lane claim | med (agent load) | high: append-only rule | §1 | `wc -c LOG.md` (lore 803,535 → hot file only) |
| 17 | kimi-shokunin upstream sync: fleet `PROTOCOL.md` is 44,449 B and differs by 20 changed lines from `skills/shokunin/protocol/PROTOCOL.md` (43,570 B) | [fleet] canonical-sync (wave 2) | low–med | low | `diff … \| grep -c '^[<>]'` = 20 | diff lines 20 → 0 |
| 18 | `.tower/worktrees/kaika` (43–68 GB) | [fleet]/operator; NOT hygiene while the wave runs | very high (disk) | high while live | §3 | do not move; revisit after wave close |

Reading of the ranking: 1, 2, and 5 have the best value/risk ratio among what can be done now. 2 is blocked on the operator; 1 is the largest disk win but the riskiest to get wrong, so run souji's dry-run first. 3 and 4 are largest for clone size, but the git-history question is an operator decision, not a lane claim.

## 8. Not verified / limits

- I did not check the line-range validity of `file:line` pointers, only existence.
- I did not evaluate the SCORECARD claims, promotion evidence, or LOG content.
- I did not confirm whether LOG or SKILL cite souji `impl-NN` numbers (move 13) or `.ufo/` paths (move 4); those need a grep before action.
- The root `bash: ` tree is absent from `git ls-files --others --exclude-standard` yet present on disk; the cause is unexplained.
- Counts in §1 totals are sums of the per-lane `wc -c` values above, not a separate command run.

## 9. Not moved, not deleted

Nothing in the fleet was moved, deleted, staged, or committed. The artifacts above are candidates; souji's dry-run census decides removal.
