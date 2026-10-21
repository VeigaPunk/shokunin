# Kama shokunin — round 21 report

## Work performed

**Declared claims.** C1 targets calibration (7→7): a report-landing audit, `tools/report-landing-audit.py`, detects spliced/unresolvable hashes and Landed-changes omissions in kama fleet reports. C2 targets operability (8→8): a soname-aware install identity (`install_links` + canonical-JSON digest, fail-closed producer, gate checks, grid). Both are author-supported at bounded scopes; scores are held; admission is the closure's decision.

- Wrote and committed the draft (`a29bb84abbb8b4d328f5970a89e448330a3a42ac`), then ran a validated 86-seat build wave (`kama-shokunin/.ufo/waves/round-21/build/`). Integrated its findings in `1471344b4c8ba4dcd20405f500741eab9b3c1183`: scrubbed git environment, exit-2 paths, batch-check lookup, author-time cutoff, canonical injective links digest, fail-closed producer, DT_NEEDED grid cells. Details: `kama-shokunin/corpus/lessons/round-21.md` §Wave-1 integration.
- First official measurement at `b76727f31e522763ce24e43d6ec86d21b507a11f` met 28/28 declared exits and captured a live v3 receipt with 10 links (`runs/b76727f3/`). The server was ephemeral and torn down.
- Ran a validated 67-seat falsify wave. Integrated its findings in `7054dba144ec04b0ffb3c427783f3ece85b5adc4`. Changes: C1 reads committed fleet bytes; `landed-ambiguous` was unreachable and is now fixed; C2 narrows refusal to loader-relevant entries and records other subdirectories in `install_unpinned` (the OpenVINO layout still runs); the gate rejects orphan digests and bad link keys; a new `tests/llamacpp-live/unpinnable-e2e.py`; SOURCES wording corrections are appended. Details: lesson §Falsify-wave integration.
- Final measurement at `7054dba144ec04b0ffb3c427783f3ece85b5adc4` met 33/33 declared exits (`kama-shokunin/.ufo/waves/round-21/runs/7054dba1/commands.json`).
- Round-20 closure follow-ups are closed. Line 7's spliced hash and the four Landed omissions are detected and corrected by ledger rows (`kama-shokunin/registry/report-landing-errata.tsv`). The same detector also covers earlier rounds (r18 ×3, r10 ×1). This report's Landed list is generated from `git log`, and it was audited before commit (below).

## Landed changes

Generated from `git -C kama-shokunin log --reverse --format='%H %s' 7a6bc911f9eb7dbea9e3b81f5f2449ecda10096d..master`. Every commit is summarized in `kama-shokunin/LOG.md` §round 21 and in the round-21 lesson.

- `a29bb84abbb8b4d328f5970a89e448330a3a42ac`: draft report audit, errata ledger, install-links pin, gate and grid.
- `1471344b4c8ba4dcd20405f500741eab9b3c1183`: build-wave integration, S066–S074, KQ28–29, SKILL rows and lesson, plus build evidence.
- `4e75d9e85ba4bb26e17fb6a5e48922c349e2a19b`: official recipe and runner.
- `b76727f31e522763ce24e43d6ec86d21b507a11f`: late build advice (RevengeSpliceOrigin), the first measured tree.
- `a6617149722c73d90e142fbdc8154d6967055f7e`: first measurement (28/28) and the live receipt.
- `7054dba144ec04b0ffb3c427783f3ece85b5adc4`: falsify integration, corrections, final recipe and wave evidence. This is the final measured tree.
- `a0050a4c1af3ab91e07cf1d24dc8e680abae96b4`: final measurement (33/33) and late falsify advice. **Lane HEAD:** local equals remote, ahead 0.

Pre-commit audit of this report: `python3 kama-shokunin/tools/report-landing-audit.py --rounds 10-20 --report 21=.ufo/reports/round-21/kama.md`. Result: exit 0, `summary reports=12 defects=9 corrected=9 uncorrected=0 errata_unmatched=0 errata_invalid=0 status=clean`; round 21 alone (`--rounds 21 --no-errata`): `required=7 post_report=0 defects=0`. Late falsify report C1SelftestReview (in `a0050a4c`) found `uncommitted-draft-uses-now` vacuous and the GIT_DIR case crash-only — open selftest debt, detector unaffected.

## Before → after measurements

| Claim | Before → after | Counting command | Measured commit |
|---|---|---|---|
| C1 report-landing detector (calibration 7→7) | Instrument absent at round start (`git cat-file -e 7a6bc911:tools/report-landing-audit.py` exit 128). After: 9 defects over the 11 reports of rounds 10–20 (1 unresolved full hash, 8 Landed omissions; 42 required and 4 post-report commits). Hand recounts by 11 build and 11 falsify seats found 0 FP and 0 FN. The ledger run reports uncorrected 9→0, which is bookkeeping and not credited. Selftest 36/36. | `python3 tools/report-landing-audit.py --rounds 10-20 --no-errata --json` exits 1; with the ledger, exit 0 | `7054dba144ec04b0ffb3c427783f3ece85b5adc4` |
| C2 soname-aware install identity (operability 8→8) | Real b11755 tree, 21 cells. Frozen arm (install_tree at 7a6bc911): link 0/13, subdir 0/3, regular 3/3, type 1/1, null 0/1. Current arm: link 13/13, subdir 3/3, controls 4/4, null 0/1; the tree is gate-clean and `install_tree_sha256` is unchanged. Gate selftest 6+1/77 → 12+1/99. Pre-launch refusals 3/3. All three R18 legacy receipts are VALID, and INVALID under `--require-install-links`. | `python3 tests/llamacpp-live/install-links-grid.py --arm frozen --json` exits 1; `--arm current --json` exits 0; `tests/llamacpp-live/unpinnable-e2e.py` exits 0 | `7054dba144ec04b0ffb3c427783f3ece85b5adc4` (live receipt: `b76727f31e522763ce24e43d6ec86d21b507a11f`) |

The no-harm reruns in the same recipe met their declared exits: error census, install-tree grid, GGUF selftest/measure, citation provenance, the SOURCES append-only check (9 rows appended, no violations), and the snapshot selftest. C2's 0→N detection holds by construction against a regular-file-only arm. Its scope is the flat b11755 install.

## Sources & frontier

Census command: `scripts/sources-census.sh census --root /home/vgpnk/Projects/shokunin kama`. Validation used the same command with `validate`. Both exited 0 at round start and at round end (`runs/7054dba1/fr-*`).

| | Rows | A / B / C | mined / queued / rejected |
|---|---:|---:|---:|
| Before | 65 | 62 / 0 / 3 | 52 / 6 / 7 |
| After | 74 | 70 / 1 / 3 | 60 / 7 / 7 |

- Added 8 tier-A rows: S066–S073, all mined. S066–S069 ground C2 (ldconfig, ld.so, Nix NAR, Go dirhash counterexample). S070–S073 ground C1 (gitrevisions, cat-file batch output, jj metaedit, git-log).
- Added 1 tier-B row: S074 (TLDP), queued.
- No existing row was touched. Falsify re-opens corrected the wording of S066–S074 in an appended section; the rows themselves are unchanged.
- Validation now prints 8 W04 duplicate-URL warnings, including S067 (ld.so, also S057) and S071 (cat-file, also S033).
- Mined mistakes M1–M5 are in lesson §Mistakes. C1's fix is shown able to fail: the raw run exits 1 and names all 9 defects.

## Trend verdicts

- **Expansion: unchanged.** The source rows and the instruments refine existing surfaces, and no capability row was added (falsify TrendCritic; build CapabilityRuleReader).
- **Quality: improved (narrow).** Two lane additions are evidence-backed: the knowledge supplement on soname identity (S066–S068) and KQ28/KQ29. The C1 detector and the C2 grid are measured above.
- **Discernment: unchanged.** No non-author admit/reject sample was taken this round. All review was author-dispatched.

## SHONEN

- [~] Decision tables, error patterns, checklist, cited sources — `kama-shokunin/SKILL.md` round-21 rows, checklist and decision row; no non-author verifier.
- [~] End-to-end domain task — live v3 receipt `kama-shokunin/.ufo/waves/round-21/runs/b76727f3/live-receipt.json` (gate VALID pinned with `--require-install-links`).
- [~] Instructions executable without oral context — SKILL checklist addition; the falsify `RecipeFreshClone` rerun matched 23/25 exits, and its 2 C1 exit-2 results came from the clone being outside the fleet (expected could-not-evaluate).
- [~] No cross-domain bleed — the fleet repo was read only; no sibling, service or host edits.

## Waves, dead seats, L0 and extras

- **Build:** 86 spawned on attempt 6. Attempts 1–5 were refused with `Background job limit reached (100)`, spaced about 180 s apart. Roles: scout 30, executor 13, reviewer 10, scribe 10, connector 6, critic 5, mutation-tester 4, revenger 4, sentinel 2, simplifier 2. Reports: 85. `RegressSkillGates` was still running at close and left no report. Verdicts: 45 confirm, 35 partial, 4 refute, 1 nonconformant (MistakeSweep, which had no VERDICT line).
- **Falsify:** 67 spawned on the first attempt. Roles: reviewer 30, scout 10, critic 8, executor 5, mutation-tester 4, scribe 4, sentinel 2, connector 2, revenger 2. Reports: 63. Dead: 1, `ConnectorSiblingReports`, with `google-antigravity/gemini-3.8-flash 429 RESOURCE_EXHAUSTED … Resets in 96h16m54s`. C1EnvSentinel and C2DigestSentinel were still running at close (no report); C1SelftestReview reported after the final lane commit (its file is uncommitted lane advice).
- **Round total:** 153 seats, no replacements. Accounting: `kama-shokunin/.ufo/waves/round-21/{build,falsify}/{completion-summary,verdict-count}.json`.
- **Planner seat:** held by the L1 (frozen topology).
- **Mistake M4:** a build seat wrote a blank line into the lane checkout. It was reverted from `master`.
- **Misroot sweep:** no kama seat files at the fleet root (falsify MisrootSweep and the L1's `git status`).
- **Open L0:** the round-17 question on `~/.local/opt/llama-b11755-bin-ubuntu-x64.tar.gz` remains open. No new L0.
- **Tool installs:** one, by build seat SrcGoDirhash: Go go1.27.3, official sha256-verified release, installed to `~/.local/opt/go1.27.3` with `~/.local/bin/go` and `gofmt` symlinks, used to execute the dirhash probe. No pacman transaction, and no persistent server or host change.
- **Stale-lane:** respawn-per-round driver; no other kama mission is open; round 22 was not started.
