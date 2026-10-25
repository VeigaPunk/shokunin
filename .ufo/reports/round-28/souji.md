# Souji round 28 — attempt 1

## Work performed

Declared claims: **C1 calibration** (lowest non-retired axis, score 7), **C2 coverage** (score 8), and **C3 operability** (score 8). They are frozen in `souji-shokunin/census/round-28/records/preregistration.txt` at base `3a2a80d0d18940a5e352ebc526da22a57dad83c4`.

- **C1 — Q57/Q59 calibration pointers:** externalized the four Q57 site selectors to `census/round-28/q57-sites.txt`, changed its mapping argument to committed `census/round-24/records/slice-verdicts.tsv`, and reworded the Q59 prose token without changing its surface-class criterion. Evidence: `souji-shokunin/corpus/QUALITY.md:141,143`; red-before gate receipt `souji-shokunin/census/round-28/records/c1-before.tsv`; Q57 checker output in `souji-shokunin/.ufo/waves/round-28/w1/SwarmExecutor01.md`.
- **C2 — F4 origin-record knowledge:** opened and pinned POSIX.1-2024 `open()`, `rename()`, and `fsync()` pages; admitted two F4 entries with per-entry Gate sections and appended S212–S214. Re-opened staged S119's zh-Hans git-fetch edition and admitted it as S215 (pin corrected before final commit). Evidence: `souji-shokunin/census/round-28/sources/SHA256SUMS`, `souji-shokunin/corpus/knowledge/origin-record-{exclusivity,durability}-r28.md`, `souji-shokunin/corpus/SOURCES.md:157-160`.
- **C3 — wave evidence operability:** added the capture tool and six-case fixture, captured round 26/27 wave evidence, restored 11 tracked round-26 wave files after capture, and added the three narrowly scoped `.gitignore` patterns. Captured completed round-28 wave bytes/results as well. Evidence: `souji-shokunin/tools/souji-wave-evidence-capture.sh`, `souji-shokunin/tests/fixtures/r28-wave-evidence-capture.sh`, `souji-shokunin/census/round-{26,27,28}/waves/`.
- **Frontier step:** added `corpus/lessons/round-28.md` with a Gate and one `stale-premise` mistake row; extended the F4 study path and SOURCES search log. Evidence: `souji-shokunin/corpus/lessons/round-28.md`, `souji-shokunin/corpus/SOURCES.md:162-174`.
- **Wave:** one validated v2 wave, `souji-r28-w1`, 64 seats. Role mix: executor 20, reviewer 12, scribe 8, critic 6, mutation-tester 6, scout 6, connector 2, sentinel 2, simplifier 2. All 64 returned result payloads. Scribe21 returned an aborted result due to conflicting evidence constraints; Scribe28 returned `[WAIT]` with no report; neither was replaced. Results: `souji-shokunin/census/round-28/waves/w1-results.json`. L1 performed the planner data-walk.
- **Inherited state:** inherited round-26/27 wave artifacts were captured byte-for-byte into committed census receipts; no operator-sweep contents were read or changed. `considerthese/` is absent. No tool installs or updates.

## Landed changes

- Frozen preregistration, baseline receipts and do-nothing controls — `0c96332932e66bbaf9cf1c246091d3275a0ab612`; recorded in `LOG.md` Round 28 entry.
- C1/C2/C3 implementation, F4 knowledge, SOURCES, lesson and round-26/27 capture receipts — `765fe8bd602ac679d01e7a0790711485209ab8bd`; recorded in `LOG.md` Round 28 entry.
- Final round records, source census after receipt, round-28 wave capture/results, and append-only wave result correction — `ed270c42161cd62829783a5e5d2ef4e27089331c`; recorded in `LOG.md` Round 28 entry and correction.
- Calibration prose pointer cleanup discovered at final gate re-run — `de478b483db66a8d8ff2d627cde1ccce6e21a014`; recorded in `LOG.md` Round 28 entry and scorecard.
- After-measurement receipts and SCORECARD pointers — `fec846dd1781a414ae3a7d71d2d8fa2fb17900eb`; measurements in `census/round-28/records/c1-after.tsv`, `c2-after.tsv`, and `c3-after.tsv`.

The final lane hash is `fec846dd1781a414ae3a7d71d2d8fa2fb17900eb`; `jj-lane.sh state` and `git ls-remote origin refs/heads/master` both showed this hash, ahead=0.

## Before → after measurements

- **C1 calibration — findings 2 → 0.** Counter: `python3 -B tools/souji-landing-gate.py --root <lane> --rev <full40> --round 28 --fleet-root <fleet>`. Before at `3a2a80d0d18940a5e352ebc526da22a57dad83c4`: `findings=2`, `checked_reg=52`, rc 2 (`census/round-28/records/c1-before.tsv`). After at final `de478b483db66a8d8ff2d627cde1ccce6e21a014`: SUMMARY `findings=0`, `checked_reg=52`, but overall rc 2 because no committed `.ufo/waves/round-28/*.md` reports are included in the lane revision (`COULD-NOT-EVALUATE`). No exemption was used. The frozen finding target is met; gate completion is not clean.
- **C2 coverage — F4 grounded entries 4 → 6; SOURCES 135 → 139.** Counts: `git grep -lE '^ground: F4' <rev> -- corpus/knowledge/ | wc -l` → 4 at base, 6 at final; `git show <rev>:corpus/SOURCES.md | grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'` → 135 at base, 139 at final. The frozen registry target is 138; S119's admitted S215 makes the result 139, so this claim fails as frozen. Additional checks at the final tree: Gate `entries=2 ok=2 slice_verdicts=8 slice_total=8 fail=0`; fleet `sources-census.sh validate` exit 0; coverage agreement reports global `grounded=13 mapped=13 dangling=0 mismatches=0`, not the frozen F4-only literal `6/6`. Measured against final code commit `ed270c42161cd62829783a5e5d2ef4e27089331c` (the later `de478b4` commit changes only Q59 evidence prose).
- **C3 operability — dirty wave paths 163 → 0.** Counter: `git status --porcelain=v1 --untracked-files=all | awk '$2 ~ /^\.ufo\/waves\// {n++} END{print n+0}'`; base receipt `c3-before.tsv` = 163; final committed state = 0. Fixture: `bash tests/fixtures/r28-wave-evidence-capture.sh` → `cases=6 pass=6 control=TAMPER-REJECTED`, rc 0. Round-26/27/28 manifests are present and the capture tool's internal verification passes. Limitation: independent `sha256sum -c census/round-26/waves/manifest.sha256` returns rc 0 but warns two newline-path records are improperly formatted; round-27 checks cleanly. Therefore full independent manifest verification is not claimed. Measured against `ed270c42161cd62829783a5e5d2ef4e27089331c`.

Owned scores remain calibration 7, coverage 8, operability 8; no scalar score delta.

## Sources & frontier

Census command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin souji`.

- Before: 135 rows, malformed 0, tiers A=128/B=5/C=2, status mined=111/queued=15/rejected=9, duplicate IDs=0, enum/tier-inflation=0, mined used-by missing=0; validate exit 0 with W04 warnings only. Full output: `souji-shokunin/census/round-28/records/c-frontier-before.txt`.
- After: 139 rows, malformed 0, duplicate IDs 0, enum/tier-inflation 0; tiers A=132/B=5/C=2; statuses mined=115/queued=15/rejected=9; validate exit 0 with W04 warnings only. Full output: `souji-shokunin/census/round-28/records/c-frontier-after.txt`.
- Added by tier: four mined tier-A rows S212–S215 (three POSIX specs and the zh-Hans docs row). Existing rows/status/recheck/used-by cells touched: none. Frontier row advanced to Core: 0; the F4 study path now records the newly explored POSIX primitives, while F4's existing README status remains frontier.
- Assimilation: one F4 origin-record-primitives theme from `merge/souji/`; S119 was re-opened and pinned, S215 admitted. Gate rejects S216 (F3 scope) and S138 (F1/F2 scope). `considerthese/` absent, so no proposal was available.

## Trend verdicts

- **expansion — improved:** two new admitted F4 knowledge entries were added with S212–S214 mined citations; F4 grounded entries increased 4→6. C2's frozen registry target misses at 139, so the coverage claim itself is not admitted.
- **quality — improved:** POSIX snapshots are digest-pinned, exact quotations are recorded, both entry Gate checks pass, the GLib snapshot recheck passed, and source census exits 0. The round-26 manifest newline-path limitation is disclosed, not counted as clean verification.
- **discernment — unchanged:** no independent non-author spot-check of one admit and one reject is on record; dispatched reviewers are lane advisory seats and cannot satisfy that duty. No new QUALITY criterion was claimed.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md` Decision tables / Error patterns / Checklists / Gate registry.
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md` Round 28; capture fixture receipt `census/round-28/waves/manifest.sha256`.
- [~] Instructions executable without oral context — `tools/souji-wave-evidence-capture.sh`, `tests/fixtures/r28-wave-evidence-capture.sh` (six cases).
- [~] No cross-domain bleed — `PROVINCE.md` Refuses / Adjacency; round-28 lesson Gate; source repo remained read-only.

**Stale-lane:** not stale; this was the steered souji round 28 mission. No tools installed or updated.
