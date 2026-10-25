# kaika W3 — non-author verification: mori round 12 (lane commit 1f07f1dd1)

Reviewer: W3ReviewMori (fresh task, orchestrator-dispatched). Verdict is a recommendation.
Scratch: `/tmp/kaika-verify/mori/` (base = `git archive 20e2255e7`, head = `git archive 1f07f1dd1`); deleted after this file was written.

## Verdict

**ADMIT WITH CORRECTIONS.** Claims 1 (depth) and 3 (coverage) reproduce exactly. Claim 2 (calibration) has reproducing counts, but the counted artifacts do not measure the calibration axis, so calibration should hold at 5. Corrections C1–C6 (section 8) are needed before the orchestrator records closure.

## 1. Provenance — PASS

Command: `git log --format='%h %an <%ae> | %cn <%ce> | %s' 20e2255e7..1f07f1dd1`
Output: one commit, `1f07f1d mori-shokunin <mori@shokunin.local> | mori-shokunin <mori@shokunin.local> | round-12: source registry …`.
`git rev-parse --abbrev-ref HEAD` → `kaika/round`; `git rev-parse 1f07f1dd1` → `1f07f1dd1eed59f10c4859726e2f780199190b22`. `git diff --numstat 20e2255e7..1f07f1dd1` → 25 files.

## 2. Append-only

Command: `git diff -U0 20e2255e7..1f07f1dd1 -- LOG.md corpus/lessons corpus/QUALITY.md | grep -nE '^-'`
Output: only `3:--- a/LOG.md`, `171:--- a/corpus/QUALITY.md`, `230:--- /dev/null` (file headers). **No deleted or modified prior line** in LOG.md, corpus/lessons/, or corpus/QUALITY.md. PASS.

Changed prior lines outside that set (listed for completeness, from `git diff --numstat`):
- `SKILL.md` 20 added / 8 deleted: in-place rewrites such as stale pointers ("56 → 65"→"56 → 66", `…T2210Z.json`→`…T2231Z.json`). The campaign binding says contract repair is "as appended corrections, never rewrites" (fleet prompt §6.4) → C5.
- `SHONEN.md` 1/1: title line only (`# mori — Promotion checklist` → `# mori-shokunin — …`).
- `corpus/evidence/README.md` 1/1: the "deleted" line is a trailing-newline fix. `git diff --ignore-all-space --numstat` → 18/0; no content removed.
- `tools/mori-census.sh` 214/6: code, outside append-only scope.
- `corpus/SOURCES.md`: new file, 55 added / 0 deleted.

## 3. Claims — counting commands re-run at base (20e2255e7) and head (1f07f1dd1)

Harness: `/tmp/kaika-verify/mori/counts.sh <tree>` (run in each extracted tree).

| claim / counter | command (run in each tree) | base 20e2255 | head 1f07f1d | report | verdict |
|---|---|---|---|---|---|
| 1 depth: SKILL distinct URLs | `grep -oE 'https?://[^ )>\|`]+' SKILL.md \| sort -u \| wc -l` | 0 | 5 | 0→5 | reproduced |
| 1: SKILL URLs absent or not A+mined | awk over SOURCES `$5`/`$9` per SKILL URL | no SOURCES.md | findings_lines=0 | 0 | reproduced |
| 1: knowledge headers resolving to A+mined rows | header-trio check (lines 1–3) + S-id tier/status lookup | 0 | 4 | 0→4 | reproduced |
| 1: SOURCES rows | `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` | absent | 33 | 33 | reproduced |
| 1: contract census | contract-v1 awk checks (malformed, dups, enums, missing used-by) | n/a | malformed=0, dups none, enum_findings=0, missing_used_by=0; A=30 B=2 C=1; mined=11 queued=21 rejected=1 | same | reproduced |
| 2 calibration: QUALITY criteria citing a lesson | `grep -cE '^[0-9]+\. .*lessons/' corpus/QUALITY.md` | 0 | 20 | 0→20 | reproduced (artifact count) |
| 2: `## Mistakes` rows | `grep -cE '^\| M[0-9]+ \|' corpus/lessons/round-12.md` | absent | 26 | 26 | reproduced |
| 2: rows with captured-by `none` | `grep -cE '^\| M[0-9]+ \|.*\| none \|' corpus/lessons/round-12.md` | absent | 5 | 5 | reproduced |
| 3 coverage: live `SURFACE lane.*` rows | `MORI_SHOKUNIN_ROOT=/home/vgpnk/Projects/shokunin bash tools/mori-census.sh \| grep -c '^SURFACE lane\.'` (run from each tree) | 9 | 23 | 9→23 | reproduced |
| 3: selftest | `bash tools/mori-census.sh --selftest` | PASS 66/66 | PASS 77/77 | 66→77 | reproduced |
| 3: oracle | `bash tools/mori-silence-cases.sh` (sha256 prefix 448f77238c73a5c9 at both trees) | matched=28 total=28 | matched=28 total=28 | 28/28, sha unchanged | reproduced |
| harm watch: live census wall time | 3× interleaved `date +%s%N` around census, each tree's own script | 1836 / 1782 / 1889 ms | 4361 / 4347 / 4299 ms | 1884/1830/1930 → 4345/4339/4278 | reproduced (≈2.3×) |

Per-claim verdicts:
- **Claim 1 (depth 4→5): verified.** Counts reproduce; SKILL URLs all resolve to A+mined rows; the four knowledge anchors reproduce (section 4/6). Caveat: a URL count measures citation presence; the depth evidence is the re-derived anchors, not the count.
- **Claim 2 (calibration 5→6): not-verified as an axis move.** The counted artifacts reproduce, but the counting command counts documents (criteria, lesson rows). AXES.md's calibration signal is "SHONEN.md/SCORECARD entries match observed repo state"; none of the counted items tests that. The report's own dissent says the claim "cannot read as improved without the outside spot-check" (`.ufo/reports/round-12/mori.md:117`), which contradicts its own table verdict "improved" (`:108`).
- **Claim 3 (coverage 5→6): verified.** 9→23 reproduces; selftest 77/77 and oracle 28/28 at unchanged oracle sha reproduce at head. Caveat: the 12-mutant battery ran on census `4fe9786d`, not final `3da5b098` (see M-gap, section 7).

## 4. SOURCES

Command: `bash /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/fleet-census/scripts/sources-census.sh validate /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/mori-shokunin`
Output: `mori-shokunin	ok	/home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/mori-shokunin/corpus/SOURCES.md`; exit 0. **PASS.**

Rows re-opened (curl; sha256 prefix compared to registry; quote grepped at location):
- **S003** (tier A, new, code, v7.2) — sha `452f1348e79c252e` = registry. `oom_kill.c` 935 `count_vm_event(OOM_KILL);` ✓; 936 `memcg_memory_event_mm(mm, MEMCG_OOM_KILL);` ✓; 447 `oom-kill:constraint=` ✓; 452 `task=%s,pid=%d,uid=%d` ✓; 945 `Killed process` ✓. Enclosing functions: 444 `dump_oom_victim`, 912 `__oom_kill_process`. **PASS.**
- **S004** (tier A, memcontrol c03c1a14) — sha `bdb6159cc2378c44` ✓; 1825 `pr_cont(",task_memcg=");` ✓; 4966 `atomic_long_read(&events[MEMCG_OOM_KILL])` ✓. Enclosing: 1815 `mem_cgroup_print_oom_context`, 4959 `__memory_events_show`. **PASS.**
- **S011** (tier A, oomd-util v261) — sha `2e94450aa337dd7d` ✓; 269 `increment_oomd_xattr(ctx->path, "user.oomd_ooms", 1)` ✓; 306 `"user.oomd_kill"` ✓; 252 `oomd_cgroup_kill`. **PASS.**
- **S013** (tier A, catalog cf8ebfc6) — sha `e53707db7e6963b2` ✓; 66 `fc2e22bc…` (coredump) ✓; 604 `fe6faa94…` "A process of @UNIT@ unit has been killed by the OOM killer." ✓; 884 `d989611b…` "systemd-oomd killed one or more processes in unit @UNIT@" ✓. **PASS.**
- **S002, S007, S008, S014, S015, S016, S032, S033, S001** (tier A) — digests reproduced for all nine (e.g. S007 `56460ffb24d7ea3c`, S015 `906e5d34b38913dd`). Quotes located: S007 "select a cgroup to terminate, and send SIGKILL to all processes in it."; S015 "not supposed to be parsed for metadata"; S033 "This is the total number of sectors written successfully."; S032 `COREDUMP_SIGNAL=11`; S016 README:26–27 "earlyoom checks the amount of available memory and free swap up to 10" / "times a second" (line-wrapped). **PASS.**
- **S021** (tier B, community, queued) — quote located: "This is an RFC patch set that is not intended to be applied in its current form."; LWN, May 1, 2025, Jonathan Corbet ✓. Registry digest `b5783e1a24467292` **not reproduced** (live HTML sha `928ee6916816ff26`); dynamic page (see L7).
- **S030** (tier C, rejected) — page read: contains `sudo systemctl enable --now systemd-oomd` and `journalctl -u systemd-oomd | grep -i "killed\|pressure\|swap"`, both matching the rejection rationale. Digest `13159dd208133f22` not computed (read tool does not expose bytes) — **unverified**.

Lesson Gate quotes: all re-opened quotes present at their locations (S002, S003, S013, S014, S015, S016, S021, S030). A tier-A new row (S003) and the rejected row (S030) were both re-opened, satisfying the sample requirement.

## 5. Discernment spot-check (LEARNING.md)

| # | row / candidate | gate decision (lesson `## Gate`) | what I re-checked | reviewer | reason |
|---|---|---|---|---|---|
| A1 | `corpus/knowledge/kill-classes-by-message-id-r12.md` | admitted (ART K3) | `journalctl -k -b all … --grep='^oom-kill:constraint='` → 5; victim records → 5; `d989611b` user 0 / system 0; `fe6faa94` user 7 / system 9 (`--output-fields=_BOOT_ID`, no MESSAGE output); catalog anchors 66/604/884 | **agree** | Counts and catalog anchors reproduce; "notice ≠ victim, scopes not summed" follows from the measured numbers; `[INFERENCE]` label on fan-out is honest. |
| A2 | `corpus/knowledge/userspace-oom-killers-r12.md` | admitted (ART K4 + earlyoom) | `oomd-util.c` 269/306/313–316; `systemctl is-active systemd-oomd.service` → inactive; `earlyoom.service` → inactive; `is-enabled systemd-oomd` → disabled; `d989611b` notices 0/0 | **agree** | "unavailable (inactive), never zero kills" is the correct reading of an inactive killer; no kill-count claim is made. |
| R1 | OneUptime systemd-oomd how-to, `S030` | rejected (tier C) | page: free-text `journalctl … grep -i "killed\|pressure\|swap"` and install/enable; S008 defaults 90% / 60% match the page's defaults | **agree** | Rejection reason (remediation how-to, free-text grep, repeats primary defaults) holds; flip condition is stated. |
| R2 | eBPF kill tracing / resident tracer (ART §6 R1) | rejected | rationale cites "free-lunch lesson :22-23" → quote present; but that lesson's own pointer `tools/mori-census.sh:21` resolves to a since-boot comment, and the phrase is at census `:186` ("Live mode writes nothing.") | **agree (with defect)** | Taste call is sound (resident/privileged tracer breaks the read-only gate). The cited pointer is dead → C1. |

Spot-check result: 2 admits and 2 rejects sampled; 4/4 agree.

## 6. New knowledge entries

- Header trio on lines 1–3: present in all four sourced entries and in `roster-truth-r12.md` (checked by `sed -n '1,3p'`).
- Recheck commands re-run and reproduced: oom_kill.c 935/936/447/452/945; memcontrol 1825/4966; oomd-util 269/306; catalog 66/604/884; journal counts (5/5/7/9/0/0); `/proc/vmstat` `oom_kill` key present (count 1); cgroup2 mount lacks `memory_localevents` (0), so memory.events is hierarchical as the entry states.
- Not re-run: `systemctl is-enabled earlyoom.service` (entry says `not-found`) — unverified.
- Claim matches source: confirmed for all four sourced entries (Section 4 anchors and Section 5 A1/A2).
- **roster-truth-r12.md** (local evidence): recheck reproduces (`MORI_SHOKUNIN_ROOT=… bash tools/mori-census.sh | grep -c '^SURFACE lane\.'` → 23; `roster_source=conf+state`). Header is non-compliant: line 1 is `source: FLEET/shokunin.conf; FLEET/scripts/shokunin-watchdog.sh:14; …`. `FLEET/` is not defined anywhere in the lane, and there is no `S###` row → M1.
- Version mismatch: `kill-classes-by-message-id-r12.md` and `kernel-oom-line-attribution-r12.md` cite systemd 262 man pages (S014/S015); host `journalctl --version` → `systemd 261 (261.2-1-arch)`, which the entries also record. Not reconciled → L8.

## 7. Credentials — PASS

Command: `git diff 20e2255e7..1f07f1dd1 | grep -nE 'op://[A-Za-z0-9]|BEGIN [A-Z ]*PRIVATE KEY|ghp_[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}|xox[baprs]-[A-Za-z0-9]'`
Output: no matching lines (`cred_exit=1`).

## 8. Report conformance and defects

Report `.ufo/reports/round-12/mori.md` (fleet-ledger worktree): sections in order at lines 9 Work performed, 71 Landed changes, 84 Before→after, 122 SHONEN, 129 Sources & frontier, 143 Mistakes, 158 Trend verdicts, 173 L0 questions, 178 Integrator notes. `[x]` count 0; SHONEN boxes `[~]` with pointers. Cites commit `1f07f1d` (4 occurrences). **Conformant.** Collision check: `/home/vgpnk/Projects/shokunin/.ufo/reports/round-12/mori.md` absent; base LOG has no round-12 close (grep count 0).

### Defects by severity

**Medium**
- **M1 — admitted entry violates the binding; expansion count overstated.** `corpus/knowledge/roster-truth-r12.md:1` opens `source: FLEET/shokunin.conf; FLEET/scripts/…` with no `S###` row. Fleet prompt §6.4 requires each entry to open with "its `S###` row, URL, anchor". Contract v1 rule 4 counts only entries "whose `source:` cites a `mined` row", so expansion is 4, not 5. The report lists it under Expansion (`mori.md:162`).
- **M2 — calibration verdict not supported; self-contradictory.** Table `mori.md:108` says "improved 5 → 6"; dissent `mori.md:117` says "Claim 2 cannot read as improved without the outside spot-check". The counting command measures artifacts, not self-assessment accuracy (see claim 2 above). Recommend the verdict be `not-verified`, score held at 5.

**Low**
- **L1 — dead pointer carried into a rejection rationale; criterion 9 violated.** `corpus/lessons/2026-10-15-free-lunch-measurements-counter-baselines.md:23` cites `"live mode writes nothing" (tools/mori-census.sh:21)`. At both base and head, `:21` is `#  since-boot write average per target device (/proc/diskstats)`; the phrase is at `tools/mori-census.sh:186` as "# Live mode writes nothing." (capital L). Pre-existing, not introduced by this round, but the round's rejection row (`round-12.md:113`) relies on it, and the round's pointer sweep (`round-12.md` §Pointer re-verification) did not catch it. QUALITY criterion 9 requires every pointer to resolve at the carrying commit.
- **L2 — false claim in Landed changes.** `mori.md:60`: "SHONEN.md regenerated byte-identical from the seed". `diff` of `.ufo/waves/round-13/shonen-seed.txt` vs head SHONEN.md: 18 differing lines (4-space indentation of the seed body vs dedented head; name placeholder filled). Git shows only the title line changed vs base.
- **L3 — adjacency verdict without a claim or count.** `mori.md:112`: "adjacency | improved | 6 held (unclaimed contract repair)". The same round says the repair has "no counting command and no score move" (SCORECARD round-12 section). An "improved" verdict with no measured move violates the verdict rule; recommend `unchanged`.
- **L4 — mutation evidence predates final census bytes.** `corpus/evidence/roster-r12-20261019T220912Z-mutation.md:4` header: "Mutant table — final census bytes `4fe9786d…`". The shipped census is `3da5b098…` (`sha256sum head/tools/mori-census.sh` → `3da5b098dc23aeb3`); only one mutant was run on `3da5b098` (`:35–37`). The report's "12/12 killed" is true for `4fe9786d` only.
- **L5 — in-place rewrites of contract-repair lines.** `SKILL.md` 8 deleted lines (stale pointers). Fleet prompt §6.4: contract repair "as appended corrections, never rewrites". LOG names the corrections, which mitigates.
- **L6 — ownership vs lowest-axis rule not reconciled.** `SCORECARD.md:3`: "Axes owned by this lane: **coverage + operability** (fleet-2)". Claims 1 (depth) and 2 (calibration) target axes not in that owned pair. Claim 1 is the lowest-scoring axis (4), which the fleet rule requires, so this is an unresolved conflict between two binding sources, not a lane defect. The report does not mention it. Route to orchestrator.
- **L7 — S021 digest not reproducible.** Registry `b5783e1a24467292` vs live `928ee6916816ff26`. Dynamic page; S021 is `queued` and supports no admitted entry, so impact is limited to provenance wording.
- **L8 — systemd doc/host version mismatch.** Entries cite systemd 262 docs (S014/S015) while the host and the entry header record systemd 261.2.

**Cosmetic / info**
- `corpus/evidence/README.md:785` trailing newline added (no content change).
- `ROSTER_SET_MISMATCH` and `+SURFACE:lane.*` drift tokens: consistent with the report (14 new lane rows, `--drift` exit 1 on the r10 pin). Full token classification not re-derived.

## 9. Recommended per-axis verdicts (lane scores all six)

| axis | score | recommended verdict | evidence |
|---|---|---|---|
| depth | 4 → 5 | **improved** | claim 1 reproduced; anchors re-derived (section 4, 6) |
| coverage | 5 → 6 | **improved** | claim 3 reproduced (9→23; selftest 77/77; oracle 28/28 at sha 448f7723) |
| calibration | 5 | **unchanged (hold 5)**; claim 2 `not-verified` | section 3, M2 |
| operability | 6 | **unchanged**; cost recorded for operator ruling | wall time ≈2.3× reproduced (section 3); AXES defines no runtime budget |
| freshness | 5 | **unchanged** | r10 pin still red (`--drift … baseline-r10-20261015T2231Z.json` → exit 1, 14 `+SURFACE:lane.*` tokens = new roster rows); no re-pin; classification file present |
| adjacency | 6 | **unchanged** (report's "improved" unsupported) | L3 |

## 10. Trend verdicts (LEARNING.md)

- **Expansion: improved.** Four admitted entries cite A+mined rows (`source:` lines verified) on ground the base lacked: base SKILL.md has 0 hits for `oomd|earlyoom|MESSAGE_ID` (`grep -cE` on `git show 20e2255e7:SKILL.md`); base knowledge mentions MESSAGE_ID only for the coredump class (`observability-census-r1.md:193`, `observability-surfaces-r2.md:193`). New kinds of source (kernel and systemd code at pinned revisions) enter the registry. Not counted: roster-truth (M1).
- **Quality: improved.** Re-executed rechecks reproduce; QUALITY criteria 6–25 each cite a lesson that exists (20/20 with lesson citations; 12 `round-12.md#M<n>` anchors resolve); the stale drift-pin path is marked by an append-only erratum (`drift-pin-r10.md`, +13 lines); no admitted entry failed its re-check. Offsetting: L1 dead pointer.
- **Discernment: improved** on this sample (n=4: 4/4 agree; section 5), by the LEARNING.md rule (agreement on admits and rejects). The report says "unchanged (pending)"; the orchestrator should record the spot-check result. Confidence is limited by n=4 and a single reviewer.

## 11. Admit / reject recommendation

**ADMIT WITH CORRECTIONS.**
- Admit: claim 1 (depth 4→5) and claim 3 (coverage 5→6), both verified as counts; four sourced knowledge entries; SOURCES registry (capability row).
- Hold: claim 2 (calibration). Artifacts (criteria, lessons) verified; calibration score held at 5 until a counting command measures self-assessment accuracy.
- Required corrections before closure:
  - **C1** repoint `…free-lunch…counter-baselines.md:23` from `tools/mori-census.sh:21` to `:186` (or quote matching text).
  - **C2** fix `roster-truth-r12.md:1` (`FLEET/` paths → real paths; add an S### row or reclassify as local evidence excluded from expansion); correct the expansion count to 4.
  - **C3** calibration verdict → `not-verified`, score held at 5; reconcile the table with the dissent.
  - **C4** adjacency verdict → `unchanged`.
  - **C5** correct `mori.md:60` ("byte-identical") and record the `SKILL.md` in-place corrections as appended corrections, or disclose them as a campaign-rule deviation.
  - **C6** run the 12-mutant battery on final census `3da5b098`, or disclose it as a gap in the report's trend verdicts.
- Operator to rule: operability cost (≈2.3× wall time, no budget); L6 ownership-vs-lowest-axis conflict.

## 12. Verification gaps (not checked)

- `godspeed/directive.md` verbatim-bytes requirement and the ≥8-seat single-batch dispatch (process claims) — not verifiable from the repo.
- S010, S022, S027–S029 quotes and digests not re-opened; S030 digest not computed; S021 digest not reproduced (L7).
- Full drift token classification not re-derived (only the 14 roster tokens counted).
- `earlyoom.service` `is-enabled` not re-run.
- LOG.md round-12 entry read only at its headings (`:542`, `:643`), not line by line.

## 13. Process notes

- Harness fault: a shell hook raised `error: command not found: __fnmcd` in many cells, sometimes swallowing the first command and leaving stale shell variables. Affected cells were re-run with explicit cwd and paths. One base-census loop was invalid (ran head script from base cwd); it was discarded and re-run correctly (base 9, head 23).
- I wrote `lwn.html` into the fleet root by mistake (cwd error). I moved it to scratch. `git -C /home/vgpnk/Projects/shokunin status --short` → 0 lines afterward; lane worktree status → 0 lines.
- All census and oracle runs were read-only with respect to the lane: live census writes nothing; selftest and oracle use temp dirs. No commits, edits, or branch changes.
