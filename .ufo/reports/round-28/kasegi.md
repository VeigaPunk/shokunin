# kasegi — round 28

## Work performed

Declared claims: **C1 depth:verifiability** — make `anchorcheck.py` fail closed on unverifiable citations, recognize the absent `~/Projects/bounties/` base, and provide isolating selftests; **C2 coverage** — admit F12, the Japanese state-coordinated disclosure workflow, on round-28 captures of S041/S042.

- Re-froze the unexecuted round-27 C1/C2 under round 28 and re-ran the committed r27 fixtures; before receipts and census: `.ufo/waves/round-28/claims.json`, `.ufo/waves/round-28/c1-controls/`, `.ufo/waves/round-28/c2-controls/`, `.ufo/waves/round-28/census-before.txt` (freeze commit `c9f8b115a098c65356e4b3b6048af45a37ab8395`).
- Dispatched one v2 wave, `kasegi-r28-build`, with 69 seats. Role mix: executor 18, scribe 16, reviewer 12, scout 5, critic 5, mutation-tester 5, connector 3, revenger 2, sentinel 2, simplifier 1; m_flash roles 35/69 (50.7%), attack roles 22/69 (31.9%). Results: `.ufo/waves/round-28/wave1-results.json` (69 final outputs, 0 dead seats). L1 held the frozen planner seat because the validator rejects planner as a swarm role. The role route table was read at `~/.omp/agent/config.yml:350-366`; actual answering-model identity is not present in the results schema, so no provider is claimed.
- C1 implementation: fail-class exit handling, BOUNTIES root derivation/confinement, `BOUNTIES-ABSENT`, and nine isolated selftest cases in `corpus/instruments/anchorcheck.py`; reviewer, critic, and mutation evidence: `.ufo/waves/round-28/wave1/ExecImplC1.md`, `RevImplC1.md`, `CritC1Kill.md`, `MutSelftestC1.md`.
- C2 assimilation: re-opened the IPA intake process and JPCERT/CC guideline; captured S042 and re-captured S041 under `corpus/source-snapshots/round-28/`; admitted `corpus/knowledge/japanese-domestic-disclosure-workflow.md` as F12; normalized and appended S042, and updated S041 `used-by`. Gate quotes and old→new row changes: `corpus/lessons/round-28.md` §Gate; capture pins and located quotes: `corpus/source-snapshots/round-28/manifest.json`.
- Closed the expected-list debt after the entry landed: `corpus/instruments/knowledge-expected.txt` now has 40 entry lines / 42 physical lines; `recheck-audit.py` reports `expected=40 missing=0 unexpected=0 exit=0`.
- Reproduced and fixed a selftest isolation defect under `GIT_DIR`; appended corrections without editing frozen claims: `.ufo/waves/round-28/claims-erratum-1.md` §§Erratum 2–3; the reproduction/fix is mined as `M28-13` in `corpus/lessons/round-28.md`.
- Assimilated one considerthese proposal: `considerthese/2026-10-25.md` proposal 1 became QUALITY criterion R14, `corpus/QUALITY.md`; the wave used receipts/digests and removed oversized raw quarantine-fetch bodies rather than retaining full source blobs (`.ufo/waves/round-28/wave1/SimplBloat.md`).
- Prompt-conformance defect: wave task prompts included `/skill:godspeed` but omitted the host's verbatim directive bytes from `~/.agents/skills/godspeed/directive.md`; recorded as M28-15 in `corpus/lessons/round-28.md`. The wave was not re-dispatched; this is reported, not hidden.

## Landed changes

- C1 instrument and documentation (`corpus/instruments/anchorcheck.py`, `corpus/instruments/README.md`, append-only `SKILL.md` gate row); C2 knowledge, capture manifest, source registry, and F12 index; expected-list regeneration; R14; round lesson, LOG, SCORECARD, claims errata, and all wave evidence. These changes are tied to the round-28 LOG entry and lane commit **`1265fe111bc0684d4dac004d803aa5b683c6b833`**; the post-commit verification receipt was added in lane commit **`32f694b38e02b3dccbc696ba7ea1e52a928101cf`**.
- Claims freeze and before receipts: **`c9f8b115a098c65356e4b3b6048af45a37ab8395`**. Validated wave specification and dispatch: **`94f387cbee71a532a51ce075f01701a557231e85`**. Canonical C1 receipt index: `.ufo/waves/round-28/c1-receipt-index.txt`, instrument sha256 `23818c1204c38ee8d1bb0c6d449dd0ffb3c9181271f14fb3d7aab25a73ee7396`.
- Lane identity/push evidence: `git ls-remote origin refs/heads/master` returned `32f694b38e02b3dccbc696ba7ea1e52a928101cf`; `jj-lane.sh state` reported local=remote at that hash, ahead=0, and lane status was clean.

## Before → after measurements

**C1 — depth:verifiability, lowest owned axis (score held 4).** Baseline instrument sha256 `c2a9e6c6088015968b3c6ea7f12a0ea66699c3ecb2a21db362659db8e95ef748`, re-run from committed r27 fixtures at freeze `c9f8b115`: bad-fixture exit **0** with `BASE-ABSENT`; BOUNTIES lines **0**; `--selftest` absent (`FileNotFoundError`, exit 1); SKILL.md exit 0, bad=0, LOST-RECORDED=306. At final lane commit `32f694b38e02b3dccbc696ba7ea1e52a928101cf` (production instrument commit `1265fe111bc0684d4dac004d803aa5b683c6b833`), instrument sha256 `23818c1204c38ee8d1bb0c6d449dd0ffb3c9181271f14fb3d7aab25a73ee7396`: bad-fixture exit **1**; BOUNTIES-ABSENT lines **1**; `--selftest` prints `selftest cases=9 failures=0`, exit 0; SKILL.md exit 0, bad=0, LOST-RECORDED=306, other fail classes 0. The same selftest passes under `GIT_DIR=/tmp/nonexistent` after the isolation fix. Post-commit evidence: `.ufo/waves/round-28/post-commit-recheck.txt` and `.ufo/waves/round-28/c1-receipt-index.txt`.

The frozen counter's `sed` limb for extracting `bad=` is malformed and emits no value; the summary line itself was directly re-read and reports `0 bad` both before and after. CritGlobal F5 and the round lesson disclose this counter defect; no counter was silently substituted. The frozen `corpus_disclosure` prediction was also false: four `source:` provenance trailers are not backticked TOK tokens. Errata 1 and 3 scope the corrected no-verdict-movement finding to the Markdown input surface; the four named files were rechecked, with 0/0/0/15 LOST-RECORDED lines before and after.

**C2 — coverage (score held 7).** Frozen counters at `c9f8b115` → final lane commit `32f694b38e02b3dccbc696ba7ea1e52a928101cf` (production commit `1265fe111bc0684d4dac004d803aa5b683c6b833`): admitted Frontier rows **11→12**; entries citing S042 **0→1**; S042 registry rows **0→1** and registry total **41→42**; `frontier-recheck-count.py` **14/14→15/15**, exit 0; sources census exit **0→0**. Separate `source-recheck.py --source S041` and `--source S042` runs each exit 0; both captures are pinned in the round-28 manifest, and S041's `used-by` change is logged old→new. Frozen C2 commands are in `.ufo/waves/round-28/claims.json`; post-commit outputs are in `.ufo/waves/round-28/post-commit-recheck.txt`.

**Density guard (no score move claimed).** On base `c9f8b115`, density was mean 150.3 / 20 blocks / 652 citations. After the append-only SKILL.md row, final `density.py` result is mean 160.2 / 20 blocks / 656 citations (final lane commit `32f694b38e02b3dccbc696ba7ea1e52a928101cf`). No density score increase is claimed.

## Sources & frontier

- Census command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kasegi`.
- Before: **exit 0**, 41 rows; warnings W04 S028 and S029 (saved `.ufo/waves/round-28/census-before.txt`). After: **exit 0**, 42 rows; the same pre-existing W04 S028/S029 warnings only. No malformed rows; source census gate passed.
- Added by tier: **one A-tier row**, S042, IPA intake-process page, opened 2026-10-25, status mined, `used-by` exactly the F12 entry. S041 is not a new row; its `used-by` changed from the two F11 entries to those two plus the F12 entry. No status/recheck cells changed.
- Frontier advanced: F12, “Japanese state-coordinated disclosure workflow”, admitted; cites S041 and S042. The staged S043 was mapped by URL to existing lane S041 and not re-registered. The package's S042 row was normalized rather than appended as-is.
- Assimilation: one theme and one entry from `merge/kasegi/`, plus considerthese proposal 1 → R14. The new claim is sourced by S042, opened this round. The kasegi quarantine slice contained 7 rows (S037, S054, S048, S065, S068, S069, S070); none was adopted, and each verdict/reason is recorded in `corpus/lessons/round-28.md` §Gate. The staged S042/S043 sources were opened and grounded by located quotes in the lesson Gate.
- Registry rows before→after: 41→42; opened rows added this round: A=1, B=0, C=0; touched row: S041 `used-by` old→new above; frontier rows advanced: F12.

## Trend verdicts

- **Expansion — improved.** F12 adds one admitted, sourced entry on ground absent from F01–F11; overlap scan is `.ufo/waves/round-28/wave1/ConnOverlap.md`.
- **Quality — improved.** Anchorcheck now fails closed on the declared unverifiable verdict classes; nine selftest cases pass, including the reproduced `GIT_DIR` isolation fault; F12's two round-grounded captures and 12 manifest quote assertions pass recheck. No admitted F12 recheck failed. Evidence: canonical C1 index, `corpus/source-snapshots/round-28/manifest.json`, and the census/harness outputs above.
- **Discernment — unchanged.** The Gate made an admit and rejects and records located quotes, but no outside non-author spot-check of this round's admit/reject sample is present. The in-wave reviewers are lane-dispatched seats, not independent non-authors; no discernment improvement is claimed. Independent closure verification remains required.

## SHONEN

[~] SKILL.md decision tables/error patterns/checklists — `density.py SKILL.md --label r28-final`: mean 160.2, 20 blocks, 656 citations; anchorcheck SKILL.md summary in `.ufo/waves/round-28/c1-receipt-index.txt`.
[~] End-to-end domain task executed/logged — LOG.md round-28 entry, C1/C2 receipts and committed lane hash `32f694b38e02b3dccbc696ba7ea1e52a928101cf`.
[~] Instructions executable without oral context — F12 recheck from foreign cwd and `frontier-recheck-count.py` 15/15; `corpus/instruments/recheck-audit.py` exit 0.
[~] No cross-domain bleed; PROVINCE remains unchanged — `PROVINCE.md` and `.ufo/waves/round-28/wave1/ConnOverlap.md`.

**Stale-lane:** respawn-per-round driver; no other kasegi mission is open. No open L0 question. Tool installs/upgrades: none; no pacman transaction attempted.
