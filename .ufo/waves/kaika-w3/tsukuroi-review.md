# kaika W3 — non-author verification: tsukuroi round 1

Reviewer: W3ReviewTsukuroi (fresh orchestrator-dispatched; not a lane seat). Round head `343fa0db1`; measured commit `549ec0c1394cfa96702a457a19de672cc1754b2f`; base `9b70381c5`. Lane tree read-only; counts re-run on `git archive` copies under `/tmp/kaika-verify/tsukuroi/{base,head}` (deleted at end). Commands are given inline; `counts.sh` = the lane's counting commands from `after.md`/`before.md` run against each tree.

## 0. Recommendation

**Do not admit round 1 as submitted. Return to lane for a round-1 amendment (not a new round).**
- Verified: provenance, append-only, credentials, SOURCES census and sampled rows, claim C counts, claim B capability row, no-harm (selftest, tools/).
- Not verified: claim A (adjacency 7→8) — conditional and partly self-authored; claim B coverage move — the four new surfaces are not declared in PROVINCE.md.
- Discernment: one admit disagrees with the gate's own QUALITY statement (open; becomes `harmed` if left unlearned at close).

## 1. Provenance (check 1) — PASS

`git log --format='%h %an <%ae> | %cn <%ce> | %s' 9b70381c5..343fa0db1`
```
343fa0d tsukuroi-shokunin <tsukuroi@shokunin.local> | tsukuroi-shokunin <tsukuroi@shokunin.local> | round-1: pin measured commit 549ec0c in LOG and SCORECARD
549ec0c tsukuroi-shokunin <tsukuroi@shokunin.local> | tsukuroi-shokunin <tsukuroi@shokunin.local> | round-1: adjacency ledger re-check + lifecycle states; ...
```
Both commits: author and committer = lane identity. `git branch -r --contains 343fa0db1` → 0 (not pushed; consistent with "No push").

## 2. Append-only (check 2) — PASS with two disclosed in-place edits

`git diff --numstat 9b70381c5..343fa0db1 -- LOG.md corpus/lessons corpus/QUALITY.md corpus/SOURCES.md`
```
47  0  LOG.md
121 0  corpus/lessons/round-1.md
9   0  corpus/QUALITY.md
73  0  corpus/SOURCES.md   (new file)
```
Zero deleted lines in all four. Hunks: `LOG.md @@ -360,3 +360,50`; `QUALITY.md @@ -6,3 +6,12`; `lessons/round-1.md @@ -17,3 +17,124` — context only.
Repo-wide deletions (`--numstat` with deletions>0): `SCORECARD.md 36/1` (placeholder row "— none yet —" replaced; disclosed); `SKILL.md 25/1` and 15 base notes at 1/1 — each is the unterminated final line gaining a newline; base bytes are a prefix (verified by byte-prefix loop: no NOT-PREFIX for any note or SKILL). `corpus/README.md` and the adjacency JSON: 0 deletions (insertions mid-file). `tools/`: `git diff --name-only 9b70381c5..343fa0db1 -- tools | wc -l` → 0.

## 3. Claims (check 3)

### Claim A — adjacency 7→8 — **not-verified**

| metric (command) | base 9b70381c5 | head 343fa0db1 | note |
|---|---|---|---|
| `jq '[.routes[]\|select(has("state"))]\|length'` | 0 | 7 | labels written by the lane; jq reads stored strings |
| `jq .source_pin_recheck.anchors_hold_count` | null | 8 | stored integer; equals `[.pins[]\|select(.anchors_hold)]\|length` = 8 but is **not recomputed** by the command |
| pins matching original (`source_pins` vs `git show HEAD:PROVINCE.md \| sha256sum`) | — | **4/8 now** (kama, kaidoku, revenger, tameshi DRIFT; kagi, mado, mori, kumitate MATCH) | lane recorded 5/8 at `checked_at 22:07:49Z`; tameshi `PROVINCE.md` last changed `c7986cd 2026-10-19 19:15:33 -0300` (after the check) |

Anchor re-read (my grep on sibling HEAD): kama:12 ✓, kagi:3 ✓ and kagi:32 ✓ (`pinned by **shape**, never by content`; my plain grep missed it because of bold markup), mado:3 ✓, mori:3 ✓, mori:12 ✓ (`**Refuses:** dispatch and orchestration mechanism`, line break in source), kumitate:3 ✓, tameshi:3 ✓, revenger:3 ✓, kaidoku:3 ✓. Anchors hold 8/8 — **verified**.

Why not verified:
1. Claim is conditional: ADJ-04 becomes `reported` only "on the integrator's commit" (`LOG.md` A bullet). `git -C fleet-ledger status` → `?? .ufo/reports/round-1/tsukuroi.md` (uncommitted). Per AXES, a round is admitted only if every claim verifies.
2. Receipt sweep scope is wrong. `after.md` swept `/home/vgpnk/Projects/shokunin/*-shokunin` (main checkouts) and found 0 hits. The live kaika worktrees were not swept: `.tower/worktrees/kaika/mori-shokunin` HEAD `1f07f1d` (2026-10-19 19:41 -0300) contains a received-packet record — `PROVINCE.md:58` "Received packet TSUKUROI-F1-MEM-01 (ADJ-04):", `SCORECARD.md:614`, `LOG.md:676` (`grep -rln TSUKUROI-F1-MEM-01 .tower/worktrees/kaika/`). The report's "Acknowledgement/acceptance: none observed" is therefore stale or scope-limited.
3. The counting commands read lane-written state; they do not measure adjacency behaviour. The move 7→8 is two lane-authored labels plus a re-hash whose result is already drifting (4/8 now).

### Claim B — coverage 8→9 + capability `sources-registry`

| metric (command) | base | head | verdict |
|---|---|---|---|
| `grep -c '^\| \`' corpus/README.md` | 10 | 15 | verified |
| SOURCES rows `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` | 0 (no file) | 34 | verified |
| contract census, 7 commands (run by me on head) | — | rows 34; malformed 0; `A=31 B=1 C=2`; `mined=26 queued=5 rejected=3`; dups, enum/inflation, missing: no output | verified |
| `grep -rliE 'archlinux\.org/news\|arch news\|informant' corpus SKILL.md PROVINCE.md \| wc -l` | 0 | 5 | verified (as counted) |
| pacnew `pacnew\|pacsave\|pacdiff` | 0 | 6 | verified (as counted) |
| recovery (`rescue.target…init=/bin/sh`) | 0 | 3 | verified (as counted) |
| ALA / sandbox / DAC(knowledge) | 0 / 0 / 0 | 1 / 1 / 2 | verified (as counted) |
| `sources-registry` capability (census runs clean, row demonstrated) | — | `sources-census.sh validate` exit 0 | **verified** |

Axis move — **not-verified**. AXES.md defines coverage as "PROVINCE.md lists every surface; none unexplored without reason." PROVINCE.md at head declares Core = pacman, systemd, drivers/firmware, journal/boot (`PROVINCE.md` `## Core`, lines 6–25). `grep -niE 'news|pacnew|pacsave|initramfs|mkinitcpio|snapper|limine|recovery|rollback' PROVINCE.md` → no hit in Core or Frontier (only ADJ/boot lines). The four new admitted surfaces (news gate, pacnew, initramfs/recovery, snapper/limine rollback net) sit outside the declared province, with no `LOG.md` province move. The keyword sweeps are also self-satisfied: the new notes are what make the counts non-zero.

### Claim C — freshness 8→9 — **verified** (with caveats)

| metric (command) | base | head |
|---|---|---|
| `grep -lE '^## Erratum \(2026-10-19, fleet round 1\) — D[1-5]' corpus/knowledge/*.md \| wc -l` | 0 | 7 |
| `grep -L '^source:' corpus/knowledge/*.md \| wc -l` | 6 | 0 |
| `grep -L '^verified-at:' …` | 11 | 0 |
| `grep -L '^recheck:' …` | 11 | 0 |
| last `^recheck:` date/cadence, over the 25 base notes (`git ls-tree 9b70381c5`) | 0 | 25 |

Errata spot-checks against sources (quotes located):
- D2 (`degraded-triage-r4.md`): S007 "hooks in later directories taking precedence over hooks in earlier directories" — found in `pacman.conf(5)` (fetched; count 1). Host: `pacman-conf HookDir` → `/etc/pacman.d/hooks/`.
- D3 (`degraded-triage-r4.md`): S028 "Capabilities listed will be included in the bounding set, all others are removed" — found in `systemd.exec(5)` (count 1). Host: `systemctl cat limine-snapper-sync.service` → `14:CapabilityBoundingSet=CAP_SYS_ADMIN`; `stat -c '%a %U:%G' /` → `555 root:root`.
- D5 (`journal-boot-plane.md`): S014 "Drop-in configuration files are also supported" — found in Mkinitcpio wiki (count 1). Host: `omarchy_hooks.conf:1:HOOKS=(… btrfs-overlayfs)`, `omarchy_resume.conf:1:HOOKS+=(resume)`.
- D1 (`update-safety-note.md`) and D4: see §4 (S010 quote verified; S009 re-read by lane).

Caveats: keys are appended at file end, not opening lines (disclosed; the LEARNING.md "opens with" wording is not met for 25 legacy notes); `recheck:` cadence values are lane-assigned; the adjacency-recheck note has no `## QUALITY check` (§5).

### Other stated numbers (checked)
- Selftest: `bash tools/tsukuroi-census.sh --selftest | tail -1` → `TSUKUROI_CENSUS_SELFTEST: PASS (80 cases, 80 passed, 0 failed)`, rc=0 on **both** base and head. Operability 9 unchanged — **verified**.
- SKILL: `wc -l SKILL.md` → 1636 → 1660 (+24) — **verified**.
- Mistakes table: `grep -c '^| [MD][0-9]' corpus/lessons/round-1.md` → 19; QUALITY criteria `grep -cE '^[0-9]+\.' corpus/QUALITY.md` → 5 → 13 — **verified**.
- D1 bare-`-Sy` count: `grep -rnE 'sudo pacman -Sy|[Oo]perator `-Sy`|then `-Sy`|`-Sy` then|`-Sy` and re-run' corpus/knowledge | wc -l` → **9 (base) → 14 (head)**. The round's trend text says advice "superseded"; the count rises under the same command. New hits are prohibitions and quoted errata (e.g. `snapper-eacces-mechanism.md:45`, `initramfs-v42-sysroot-recovery.md:41`, `arch-news-gate-2026.md:60`, `QUALITY.md:10`). Unexplained in `after.md`; the 6 D1 erratum blocks are real.

## 4. SOURCES (check 4) — PASS

`bash …/fleet-census/scripts/sources-census.sh validate …/tsukuroi-shokunin` → `tsukuroi-shokunin	ok	…/corpus/SOURCES.md`, **rc=0**.
Reverse-cite (every `mined` row's `used-by` path contains its id): no output. Rejected rows: 3 (S029, S030, S033), each `REJECTED: … flip: …`.

Rows re-opened (quote and anchor checked at source):
| row | tier | source opened | quote / anchor | result |
|---|---|---|---|---|
| S010 | A | ArchWiki System maintenance `?oldid=885170` (Revision 06:06, 7 Sep 2026) | § Avoid certain pacman commands: "never run `pacman -Sy`; instead, **always** use `pacman -Syu`." | found |
| S002 | A | archlinux.org news 2026-09-22 | "If you configured the systemd hook and unlock LUKS partitions, that depend on these values, you need to re-enroll the TPM2 in use." | found (verbatim) |
| S020 | A | limine-snapper-sync unit, raw master | "### Security hardening" block: `CapabilityBoundingSet=CAP_SYS_ADMIN` | found |
| S034 | A | man.archlinux.org access(2), DESCRIPTION | "for the root user, the check uses the set of permitted capabilities rather than the set of effective capabilities" | found |
| S029 | **rejected** | security.archlinux.org (fetched) | AVG-2893, `systemd 257.6-1`, Medium, Vulnerable; AVG-2904 present | found; reject reason holds (host `pacman -Q systemd` → `261.2-1`) |
| S007/S008/S028/S014 (quoted by erratum and lesson) | A | man pages / Mkinitcpio wiki | §5 quotes | all 6 quotes found |

Gate check for other rows: `S006 "Download files to a temporary directory owned by DownloadUser"` and `S033 "A root directory mounted read-only (mode 555) will prevent subvolume creation."` are in the Gate table; not re-opened (S033 rejection checked in §5).

## 5. Discernment spot-check (check 5, LEARNING.md)

| # | decision | sampled artifact | my check | verdict |
|---|---|---|---|---|
| 1 | admit | `corpus/knowledge/arch-news-gate-2026.md` | `curl … news \| grep -cE '<td>20(25\|26)…'` → 20; `pacman-conf --repo-list` → 5 repos (matches); TPM2 item N/A because HOOKS have no `systemd` (`grep -Hn '^HOOKS' /etc/mkinitcpio.conf*` shows busybox `encrypt`) | **agree** |
| 2 | admit | `corpus/knowledge/pacnew-plane.md` | `grep -cE 'installed as .*\.pacnew' /var/log/pacman.log` → 3; `…saved as .*\.pacsave` → 0 | **agree** |
| 3 | admit | `corpus/knowledge/adjacency-recheck-2026-10-19.md` | `grep -c '^## QUALITY check'` → **0**; the lesson Gate says "Each entry … carries a `## QUALITY check`" (corpus/lessons/round-1.md § Gate). Also a receipt/ledger note rather than a knowledge claim. | **disagree** — gate statement false for this entry; needs section or corrected Gate; lesson should record it |
| 4 | reject | R6 "pre-existing `@.snapshots` explains EACCES" (snapper-eacces-mechanism.md § Rejected readings) | `journalctl -g 'create subvolume failed' \| grep -ci 'already exists'` → 0; `grep -c errno:13` → 8 | **agree** |
| 5 | reject | R5 "TPM2 news applies" (initramfs-v42 § Rejected readings) | HOOKS busybox, no `systemd` (see #1) | **agree** |
| 6 | reject | S033 "mode 555 = read-only mount" | `findmnt -no OPTIONS /` → `rw,relatime,…,subvol=/@`; 555 is DAC mode bits (S027) | **agree** |
| 7 | reject | S029 tracker row | §4 | **agree** |

Totals: admits 2 agree / 1 disagree; rejects 4 agree. The disagreement has no QUALITY criterion gap (criteria 1–13 cover it); the entry simply did not meet the bar its Gate claims. Per LEARNING.md, leaving it unlearned counts as `harmed`.

## 6. New knowledge entries (check 6)

Header trio (`grep -nE '^(source|verified-at|recheck):'`): present in all 5 (`arch-news-gate-2026`, `pacnew-plane`, `initramfs-v42-sysroot-recovery`, `snapper-eacces-mechanism`, `adjacency-recheck-2026-10-19`), lines 1–3. Recheck runs (all re-run by me on the host or sibling HEAD):
- arch-news: feed count 20 ✓, repo list ✓ (see §5).
- pacnew: 3 / 0 ✓.
- initramfs: `grep -n '/new_root' /usr/lib/initcpio/hooks/*` → btrfs-overlayfs:4, plymouth:11, usr:5/18 (usr not configured — claim says 2 configured runtime hooks ✓); v42 init `/new_root` count 0, `sysroot` 7 ✓.
- snapper: `stat -c '%a %U:%G' /` → `555 root:root` ✓; errno:13 count 8 ✓; `systemctl cat … CapabilityBoundingSet` ✓; `snapper list-configs` → header-only (Config│Subvolume + ruled line) ✓.
- adjacency-recheck: pin rehash (4/8 now, §3A); anchors 8/8 (§3A).
Claims vs source: match where checked (§4, §5). Minor: `initramfs` S015 source cites the GitLab API URL, the registry row cites the releases page (same resource, not a defect).
Defect: `adjacency-recheck-2026-10-19.md` lacks `## QUALITY check` (`grep -c` → 0) despite the Gate claim.

## 7. Credentials (check 7) — PASS

`git diff 9b70381c5..343fa0db1 | grep -nE 'op://[A-Za-z0-9]|BEGIN [A-Z ]*PRIVATE KEY|ghp_[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}|xox[baprs]-[A-Za-z0-9]'` → no output (grep rc=1).

## 8. Report (check 8) — PASS with defects

`/home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/fleet-ledger/.ufo/reports/round-1/tsukuroi.md` (144 lines, untracked `??` in ledger; fleet-root `.ufo/reports/round-1/tsukuroi.md` absent — fail-closed check passes).
- Sections (`grep -nE '^## '`): Work performed, Landed changes, Before → after measurements, SHONEN, Sources & frontier, Mistakes, Trend verdicts, L0 questions, Integrator notes — all present, in order.
- SHONEN: 4 lines; `SHONEN.md` has 4 boxes; all `[~]`; `grep -c '\[x\]'` → 0. No `[x]` without a verifier.
- Cites round commits `549ec0c`, `343fa0d` ✓. Named non-author verifier: none claimed (correct).
- Stale statements: "receipt sweep … 0 hits" and "acknowledgement none observed" (see §3A); "SCORECARD axes" text in the report and LOG are self-assessed. The report's "bare -Sy superseded" trend omits the 9→14 count.
- Not verifiable from the worktree: the 12-seat L2 dispatch and godspeed-prefixed directive bytes (no prompt files in the tree; evidence files `.ufo/evidence/round-1-kaika/*` exist — 9 files).

## 9. Recommended per-axis verdicts

| axis | lane claim | recommended | evidence |
|---|---|---|---|
| depth | unchanged (8) | **unchanged, 8** | no depth claim; SKILL +24 lines are update-gate rows |
| coverage | 8→9 | **hold 8** (B-counts verified; axis move not-verified) | §3B: PROVINCE does not declare the four new surfaces |
| operability | unchanged (9) | **unchanged, 9** | selftest 80/80 rc=0 base and head; tools/ 0 diff |
| freshness | 8→9 | **9 (verified, caveated)** | §3C counts; errata spot-checked (§3C) |
| calibration | unchanged (9) | **unchanged, 9** | no calibration claim; discernment §5 open item |
| adjacency | 7→8 (conditional) | **hold 7** (not-verified) | §3A: conditional on integrator commit; lane-authored counts; sweep scope; 4/8 pins now |

## 10. Trend verdicts (LEARNING.md vocabulary)

- **Expansion — improved.** Evidence: SOURCES rows 0→34 (census clean); README coverage rows 10→15; four admitted entries on 0-hit ground (sweeps 0→5/6/3/1/1/2). Caveat: keyword sweeps are satisfied by the new notes themselves; PROVINCE.md not extended, so "surface" growth is not recorded.
- **Quality — improved.** Evidence: 7 erratum blocks, D2/D3/D5 re-verified against sources and host (§3C); contract keys 25/25; date-or-cadence recheck 25/25. Caveats: D1 count 9→14 under identical command; `adjacency-recheck` lacks QUALITY section; keys appended, not opening (legacy exception stated).
- **Discernment — unchanged, one open disagreement.** Spot-check (§5): 6 agree, 1 disagree (`adjacency-recheck` admit). Becomes `harmed` if not learned at close.

## 11. Defects by severity

**High (blocks admission of A/B-coverage)**
1. Claim A: conditional on an uncommitted report; counting commands read lane-written stored fields (`state`, `anchors_hold_count`) rather than measuring; not verified as stated.
2. Claim A receipt sweep excluded `.tower/worktrees/kaika/*`; mori HEAD `1f07f1d` holds a receipt for TSUKUROI-F1-MEM-01 (`PROVINCE.md:58`, `SCORECARD.md:614`, `LOG.md:676`). Report's "0 hits / none observed" is scope-limited and now stale.
3. Coverage axis move: four admitted surfaces absent from PROVINCE.md Core/Frontier (AXES coverage definition is PROVINCE-based; no province move logged).

**Medium**
4. `adjacency-recheck-2026-10-19.md` admitted without `## QUALITY check`, contrary to the Gate's own claim; a gate-execution miss (discernment disagreement #3).
5. D1 count 9→14 under the same command; trend "superseded" lacks a count that separates advice from prohibitions/quotes; not explained in `after.md`.
6. Pin drift is time-dependent: tameshi `PROVINCE.md` changed at 19:15 -0300 (after the lane's 19:07 check); the 5/8 figure is 4/8 now. Ledger needs re-stamping or a recheck note.

**Low**
7. Freshness keys appended at file end, not opening lines (LEARNING.md "opens with"); disclosed exception; integrator should decide whether legacy notes need an opening-line key or a recorded waiver.
8. SCORECARD axes table still shows coverage 8, adjacency 7, freshness 8 with no last-change round; round moves appear only in the claim table. Update only on verdicts.
9. S030 is a `tier C` row for a fleet dossier's synthesized answer (not a source). Rejected, so harmless; contract rule 1/"a lead is never a row" is arguable.
10. `corpus/knowledge/adjacency-recheck` is a receipt ledger admitted as knowledge; classification question for integrator.

## 12. Admit / reject recommendation

**REJECT as submitted; return for round-1 amendment.** Required before re-review:
- (F1) Add the four surfaces to PROVINCE.md Frontier or Core with a `LOG.md` province-move entry, or drop the coverage move.
- (F2) Re-run the receipt sweep over `/home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/*-shokunin` as well as main checkouts; restate ADJ-04 status with mori `1f07f1d`; make the adjacency counts recompute (derive `state`/pin match from the ledger and `git show HEAD:PROVINCE.md`), or label them lane-recorded and drop the 7→8 claim. Adjudicate A only after the integrator commits the report.
- (F3) Add `## QUALITY check` to `adjacency-recheck-2026-10-19.md` or correct the Gate sentence; record the disagreement in `corpus/lessons/round-1.md`.
- (F4) Explain or correct the D1 9→14 count and the "superseded" trend text.
- (F5) Re-stamp the pin table with the time of re-check (tameshi drift).
Keep: provenance, append-only, credentials, SOURCES (34 rows, census clean), the sources-registry capability, claim C counts, the four admitted entries (subject to F3 for the fifth).

## 13. Verification gaps (not performed or not verifiable)

- Could not verify the 12-seat L2 dispatch or godspeed directive bytes from the worktree (no prompt artifacts in tree).
- Did not re-open all 34 SOURCES rows; sampled 5 registry rows + 6 quoted erratum sources (≥3 requirement met: S010, S002, S034 new tier A; S029 rejected).
- Did not re-run every knowledge-entry recheck for the 25 base notes; re-ran the counting commands for C and spot-checked two errata per the sample.
- Anchor greps for kama/mado/tameshi/kaidoku/kumitate/revenger/mori done on sibling HEAD at 2026-10-19 (time-stamped; tameshi has since changed).
- Push state: none; `git branch -r --contains 343fa0db1` → 0 remote-tracking branches.

Scratch `/tmp/kaika-verify/tsukuroi/` removed at end of run.
