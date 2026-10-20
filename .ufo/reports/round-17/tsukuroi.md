# tsukuroi — round 17 report (2026-10-20)

Lane HEAD before `6923fe0bd3add04fc90f3bc3522895b27cf44bbe`; landed `dd15c183f2f2481db67d0234038117a0d5b7034c` (integration), `90037c2d67bc076db79e4d4396f0140e3505dabd` (wave-2 repairs, measured), `c53adeede00c09f77f6d6c941789f383d0817f1f` (final evidence; lane tip). Every lane commit went through `scripts/hyaku/jj-lane.sh`; cited hashes are its `landed` lines.

## Work performed

Declared claims (three, distinct axes, causally separable — each counting command reads only its own files):
- **C1 depth** (tied-lowest axis, 8): a next-boot verdict for every limine kernel entry from extracted boot images.
- **C2 freshness**: dated R17 notices on current-use host statements made stale by the 09:15 `pacman -Syu`.
- **C3 operability**: revision tools bound to landed branch commits (routed jj-w1 audit findings R1/R2).
- Capability (inside C1): `boot-chain-audit` live audit.

Work items:
- **Priority — next-boot safety, read-only.** The sudo journal attributes all 13 pacman runs 07:45–09:39 to account `vgpnk` (4 of 13 from `~/Documents/nvhelpme`). The 09:15:30 `-Syu` upgraded mkinitcpio 41.1-1→42.2-1, linux→7.2.11, systemd→262, plymouth→-3, limine-mkinitcpio-hook→1.40.0-2, nvidia-open-dkms→615.78.08, and installed linux-lts 6.18.57-2. `limine-update` at 09:26:11 rebuilt both UKIs outside pacman. Reboot at 09:56; boot 0 started 09:57:09 on 7.2.11. Evidence: `tsukuroi-shokunin/.ufo/waves/round-17/l1-capture/boot-chain-capture.txt:44-97,124-125`.
- **Image extraction.** Every UKI was copied with `sudo -n cat`/objcopy and unpacked with `lsinitcpio` under /tmp; nothing was written to `/boot`. The 42.2 init uses `/sysroot` (7 refs, 0 `/new_root`), and both late hooks still name `/new_root`. In 42.2 images `/new_root` is a symlink to `sysroot` (`overlay-emulation.txt:51-66`). An unprivileged namespace emulation shows the btrfs-overlayfs path steps succeed through that symlink (`overlay-emulation.txt:40-48`). Firmware `LoaderEntrySelected=Omarchy.linux` (`supplement-capture.txt:113-115`).
- **Verdict.**
  - Default `//linux`: BOOTED-OBSERVED.
  - `//linux-lts`: UNTESTED; it shares the same initramfs, so it is no fallback for a hook problem.
  - Snapshot #2 (`linux` and `linux-lts`): PATH-ALIASED-EMULATED; the overlay is expected but not boot-tested.
  - Snapshot #1: CONSISTENT-PRE42 (41.1 image); it is the only pre-upgrade rollback.
  - The EFI fallback is the Limine binary itself.

  Sources: `tsukuroi-shokunin/corpus/knowledge/boot-chain-r17.md` and `.json`. An independent live run reproduces all six verdicts (`l1-capture/audit-live.txt`, `TSUKUROI_BOOTCHAIN: CONSISTENT`, rc 0).
- **L0 thread.** Read the fleet `.ufo/l0-questions.md` tsukuroi round-17 lines in order:
  - The first line (`ac792a7`) predicted degraded snapshot boots. This was the L1's error: the image listing was type-blind.
  - It was corrected by `6fe9984` within 28 minutes.
  - An erratum followed (`f92afc1`, plus precision note `6a5c8bc`), covering attribution, dkms 7.2.3, the backup's secrecy, and withdrawal of option (b).
- **C2.** 48 records in `corpus/knowledge/freshness-recheck-r17.json` cover six entries, all with append-only notices. Five `recheck:` lines that invoked pacman are now superseded by `## R17-RECHECK — steer-safe procedure` blocks.
- **C3.** All five revision tools now take only 7–64 hex resolving to a commit landed on master (and pushed): `HEAD`, `@-`, ref names and `""` are rejected, and the output carries `branch`/`branch_tip`. `tools/check-revision-binding.py` now probes `@-`, `master`, a short tip, a landed parent and not-pushed across all nine `--revision` tools. This fixes JjAuditTsukuroi R1/R2. Not fixed by the lane: fleet-helper findings and S5/S7/S8/R3 (`build/JjDocSweep.md`).
- **New gates** (all selftests pass at `90037c2`, `measure/final/selftests.txt`): `check-boot-chain.py` (61), `check-freshness-r17.py` (53), `check-recheck-commands.py` (40), `check-seat-scope.py` (42), `check-revision-binding.py` (28), `boot-chain-audit.sh` (45).
- **Routed r16 spot-check debts:**
  1. The falsify wave was run (wave 2 below).
  2. Godspeed bytes: 72/72 and 81/81 dispatched tasks start with `/skill:godspeed\n\n` plus the 429 directive bytes, sha256 `db88963c…`.
  3. QUALITY24 was shown able to fail: r16 build gives 64 SCOPE-UNDECLARED; r17 build gives 30 SCOPE-EXEC-UNAUTHORIZED and r17 falsify 16.
  4. `frozen-cases.SUPERSEDED.md` was added.
  5. W04 rows are kept with reason (8 now; S058 is a contract `supersedes` row).
- **Waves.** Planner seat: held by the L1 (validator rejects `planner`), with a planning data-walk on connector ConnPlannerWalk.

  | Wave | Seats | Role mix | Outcome |
  |---|---|---|---|
  | 1 build | 72 (dispatched 12:57 after one job-cap refusal) | scout 20, executor 11, reviewer 10, scribe 9, connector 8, critic 6, revenger 4, simplifier 2, sentinel 2 | 72 delivered. 5 were parked by the L1 session's 429 exit; the L1 revived them by message, same identities, and they delivered. |
  | 2 falsify | 81 (dispatched 14:17 after ~20 min of job-cap waits; `falsify/dispatch-attempts.log`) | reviewer 42, scout 13, critic 7, connector 7, mutation-tester 4, sentinel 3, revenger 3, simplifier 2 | 29 delivered reports. 36 dead: m_zfl `429 Rate limit reached` after 10 retries, mostly reviewers. 16 still running at landing. Not respawned (`falsify/outcome.json`). |

  Round total: 153 seats. A residual 4-executor repair call was refused by the job cap, so the L1 made those repairs itself.

## Landed changes

| Commit | Change | LOG.md entry |
|---|---|---|
| `dd15c18` | boot-chain-r17 entry/JSON; captures; 48 freshness records; R17-RECHECK blocks; rebinding of the five tools; 5 new gates + audit tool; QUALITY 25–27; lesson; SOURCES S051–S057; SKILL/README/SCORECARD; wave-1 evidence | “round17 boot chain after the 09:15 `pacman -Syu`” |
| `90037c2` | wave-2 repairs: typed `/new_root` witness (BOOTCHAIN-UNTYPED); 3 gate mutants killed; harness probes and 9-tool denominator; empty-revision guard; audit mtime bound to copied bytes, `TMPDIR=$WORK`, `set -f`; recheck wording; S058; operator checks; L0-overclaim mistake | “round17 wave-2 falsify findings and repairs” |
| `c53adee` | measured outcome in SCORECARD; falsify/measure evidence | same |

Fleet commits: L0 lines `ac792a7`, `6fe9984`, `f92afc1`, `6a5c8bc`.

## Before → after measurements

All measured with the same evaluator from a fresh clone at `90037c2d67bc076db79e4d4396f0140e3505dabd`, against baseline `6923fe0`. Outputs are in `tsukuroi-shokunin/.ufo/waves/round-17/measure/final/`.

- **C1:** `python3 tools/check-boot-chain.py --revision <commit>` gives `verdicted_kernel_entries` **0 → 5** (exit 1 BOOTCHAIN-MISSING → 0 PASS). `--revision HEAD` gives exit 2 E-REVISION-INVALID.
- **C2:** `python3 tools/check-freshness-r17.py --revision <commit>` gives `resolved_records` **0 → 48** (exit 1 R17-FRESH-MISSING → 0). Baseline proof: `--revision 6923fe0 --registry-from 90037c2` → 48 STALE-UNFLAGGED.
- **C3:** `python3 tools/check-revision-binding.py --tools-revision <commit>` gives bound tools **legacy 0/5 → 5/5; all 0/9 → 9/9** (exit 1 → 0).
- **Frontier fix:** `python3 tools/check-recheck-commands.py --revision <commit>` gives 5 flagged → 0 (5 resolved).

## Sources & frontier

- **Census:** `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tsukuroi` exited 0 at round start (7 W04) and 0 at round end (8 W04, the new one being S058).
- **Rows:** 50 → 58 by `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`.
- **Added (all tier A, mined):**
  - own-work: S051, S052, S055, S056
  - docs: S053
  - code: S054, S057, S058 (S058 supersedes S054's `teaches`)
- **Touched:** `used-by` on S015, S016, S021, S022 (old → new logged in `corpus/lessons/round-17.md`). Re-opened unchanged: S021, S022.
- **Frontier:** the README Frontier bullet “Pending mkinitcpio 42 upgrade strands two `/new_root` hooks” is superseded for this host by `corpus/README.md` § Round 17.
- **Sourced claim:** C1 cites S051–S057.
- **Mined mistakes:** R17-TYPE-BLIND, R17-L0-OVERCLAIM, R17-STEER-SCOPE, R17-JJ-REVISION and R17-SEAT-EXEC, in `corpus/lessons/round-17.md` § Mistakes, each with a fix shown able to fail.
  - R17-STEER-SCOPE: the L1 ran `pacman -Q` once at round start despite the steer.

## Trend verdicts

- **expansion: unchanged.** The boot ground was already held. The new capability row (`boot-chain-audit`) widens the repertoire, not the coverage map.
- **quality: improved.** 48 stale current-use statements carry validated notices, five recheck procedures became steer-safe, and the boot-chain gate now requires typed evidence. Wave 2 listed further un-noticed stale statements, which are planned for next round.
- **discernment: improved, on outside evidence only.** QUALITY27 turns the outside jj-w1 audit R1/R2 into a gate (0/5 → 5/5), and QUALITY24 now fails on evidence for the r16 spot-check's routed seat-scope defect. The seat-found L0 error is mined as a mistake, not counted as credit (critic FxCritCalibration).
- **No-harm caveat:** critic FxNoHarm judged **calibration harmed** (residual, correctable): an urgent wrong L0 line stood for 28 minutes, and three overclaims stood until the erratum. Reported for the operator and closure to rule; the author does not claim “no axis harmed”.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md` § Round 17 (pre-reboot procedure, registry, revision contract)
- [~] At least one end-to-end domain task executed and logged in LOG.md — live boot-chain audit, `l1-capture/audit-live.txt`; LOG round17 entries
- [~] Instructions executable by an agent without oral context — `tools/boot-chain-audit.sh --live` procedure; not verified by a context-naive agent
- [~] No cross-domain bleed (PROVINCE.md still accurate) — PROVINCE unchanged; sibling-overlap seat FxConnSibling died (429), so this box is unverified this round

## Open L0 questions and other notes

- **Open L0 question:** tsukuroi round-17 rollback policy. Optional operator action: pin snapshot #1, since the only pre-upgrade image may rotate out. No decision is required for the default boot.
- **Stale-lane:** respawn-per-round driver; no other mission of this lane is open.
- **Tool installs:** none, by the L1 or reported by seats.
- **Inherited state:** the worktree was clean at start; no earlier attempt of this round. No misroots: the fleet `git status` shows only driver `.ufo/state/*` and `watchdog.log`.
- **Non-author files read, not edited:** `corpus/lessons/round-16-verifier-spotcheck.md`, `considerthese/2026-10-20.md`.

## Addendum — late wave-2 results (after the report's first landing)

- **Delivered and survived:**
  - FxGodspeedW2: 81/81 and 72/72 tasks carry the exact directive bytes.
  - FxBindSectCita: C3 binding for section-citations holds; all pre-round finding IDs are preserved.
  - FxC2Rerun: 48/48 reproduced from a fresh clone.
- **Delivered and failed — FxOwnS055:** S055's `teaches` overreached its capture, and the C1 gate accepted the emulation's own echo line as an image witness. Repaired and landed `ed2ddd40dbc02ba9ccb2f3fcb81659773e400229` (lane tip):
  - S059 supersedes S055.
  - The symlink witness now requires an `lrwx… new_root -> sysroot` mode line; gate selftest 62/62.
  - The entry wording was corrected.
  - The citation-scope erratum was appended.
- **Re-measured at `ed2ddd4`:** C1 5, C2 48, recheck 0 flagged (all exit 0). The census exits 0 with 8 W04 warnings.
- **Late dead seats (m_zfl 429):** FxFreshUpdaSafeV3, FxRevengerSwitchRoot, FxBindSourScopCorr, FxReadmeFrontier, FxRecheckRerun, FxRevengerSnapperCopy, FxSeparability. Separability and the README frontier supersession therefore have no outside attack this round. The remaining running seats are reported as undelivered.
