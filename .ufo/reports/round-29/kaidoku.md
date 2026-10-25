# kaidoku — round 29 report

L1: in-session hyaku lane subagent `KaidokuR29`, attempt 1. Lane repo `/home/vgpnk/Projects/shokunin/kaidoku-shokunin`, base `bacbe9cc31d09b5e58e265b0138bd75d0cdb6b47`, landed tip `33570c3ab8e4c9748fa48ae4609113c561e20e05` (`jj-lane.sh state`: local = remote, ahead 0). Dispatched 19:46Z; freeze at 20:03Z; wave 20:20–20:40Z; filed about 20:46Z, inside the 21:46Z scope freeze.

## Work performed

Declared claims (frozen together at `dbd87cfa09eb89306c4e07d3171a4556eb732024`, `.ufo/waves/round-29/claims.json`, before any REA run, lookup or fetch):

- **R29-C1 — coverage** (learning claim; PROVINCE Frontier "EVM bytecode (extended)", the planned field `SCORECARD.md:3128`): the round-25 primary EVM naming rule scored, unchanged, on 16 fresh hex-screened carriers and 152 selectors that appear nowhere in the lane at the base, plus an entry citing S088.
- **R29-C2 — depth** (learning claim, sourced): Sourcify's `filterResponse` rule (S084, re-opened this round as S087) predicts openchain's `filtered` flag on 178 selectors with no openchain response in the lane at the base, plus an entry citing S087.

Work items:
- Repair first. Screens before the freeze, targets sized to the screened sets: hex screen `carriers=16 fail=0` (`.ufo/waves/round-29/before/hex-screen-c1.txt`); pre-seen screens `overlap=0` for C1 (`before/preseen-c1-name.txt`, every 8-hex word in every tracked file) and C2 (`before/preseen-c2-flag.txt`); 26 of 178 ABI selectors and 10 of 36 canonical keys dropped before the freeze (`before/select-heldout.txt`). No pre-freeze probe.
- Instruments: `tools/round-29/c1-fresh-naming.py` (22 selftest cases) and `tools/round-29/c2-filtered-unseen.py` (19 cases), both requiring the claim's own SOURCES row (routed defect 6, QUALITY row 45); C2 also requires a predicted-false branch. Producers `make-carriers.py` (solcjs 0.8.37), `select-heldout.py`, `preseen.py`, `collect-c1.py`, `collect-c2.py` (frozen retry policy; every request answered 200 on the first try). Freeze commit `dbd87cfa`.
- Data, once, after the freeze: 16/16 REA 6.5.0 runs exit 0, 304 lookups, 178 fetches (`4fcea97875a7fe1d816fb871cbc60a1c3632efa0`).
- Entries: `corpus/knowledge/2026-10-22-r29-evm-fresh-selector-naming.md`, `corpus/knowledge/2026-10-22-r29-openchain-filtered-unseen.md` (`18be864a`, corrected from the wave in `2f18996d`). New finding, labelled as a post-fetch reading: 6 of the 31 kept canonical signatures do not hash to their key (`.ufo/waves/round-29/after/canonical-keyhash.txt`).
- Inherited state: `.ufo/waves/round-28/a2w/ExecR27SelftestFix.md` (rewritten by a round-28 seat after that round's filing) settled by committing it unedited as evidence in `7431096bb16e7dd3c37e08f7307952e231b94cf8`. No `lane-dead-no-report kaidoku round=29` line; no earlier attempt to inherit.
- Round-28 spot-check routed defects (`corpus/lessons/round-28-verifier-spotcheck.md:84-91`): (1) seat report committed, pre-file gate added (M29-1, M29-4); (2) r27 selftest patch re-verified (sha256 `1c8259a8…636783`, every line outside `selftest()` byte-identical) and applied in `7431096b`; selftest `cases=6 failures=1` exit 1 → `failures=0` exit 0 (`before/r27-c2-xpin-selftest-unpatched.txt`, `after/r27-c2-xpin-selftest-patched.txt`); INSTRUMENT_REVISED disclosed under `instrument_supersessions` in `.ufo/waves/round-27/claims.json` and in the `round-27` ledger row (`18be864a`); (3) hex screen before the freeze; (4) real held-out `filtered` test = R29-C2; (5) `tools/round-29/freeze-gate.py` audits every `claims*.json` (19 freezes vs 16), ledger `corpus/claim-freezes-v2.tsv`; (6) claim-specific Gate row in both counters.
- Ledger repair: the round-24 gate with `--disclosures` was red at the round-26, 27 and 28 filing commits (`after/prefile-gate-at-filings.txt`); round-26 and round-28 rows corrected (`18be864a`).
- Wave 1, 44 seats, findings integrated (`SCORECARD.md`, "Round-29 wave findings"): both counters re-run and independently re-derived; entries corrected for every wording defect the reviewers and critics found (factory() carrier n06, separation scope, branch breakdown, mis-keyed scope, held-out wording, round-25 unit, source line); pointers appended to the round-25 and round-28 entries; mistakes M29-1 and M29-2 rewritten and M29-4 added after `w1/CriticMistakes.md`.
- Hygiene: PROVINCE `:95` annotation; SKILL.md `### Round-29 measurement registry`; QUALITY rows 45–47; README map, index and lesson rows (`2f18996d`).

## Landed changes

All commits by `kaidoku-shokunin <kaidoku@shokunin.local>` through `jj-lane.sh`, each printing `landed`:

| commit | content | LOG.md |
|---|---|---|
| `dbd87cfa09eb89306c4e07d3171a4556eb732024` | freeze: claims.json, counters, selftests, frozen carriers and selector lists, producers, before receipts | round-29 entry, "Freeze" |
| `7431096bb16e7dd3c37e08f7307952e231b94cf8` | r27 selftest patch, r28 seat report, round-29 freeze gate | "Round-28 routed defects" |
| `4fcea97875a7fe1d816fb871cbc60a1c3632efa0` | C1 and C2 data | "Measured" |
| `18be864a528873b2b70d8c94e31f880290249e90` | entries, S087–S088, lesson, QUALITY 45–47, README, r27 supersession, ledgers, pre-file check | "Learned", "Mistakes mined" |
| `2f18996ddbe4c098adb43a3883b9af61e3994729` | wave reports and dispatch records, entry corrections, pointers, PROVINCE, SKILL, SCORECARD, LOG | "Wave" |
| `33570c3ab8e4c9748fa48ae4609113c561e20e05` | after receipts at `2f18996d`, census after | "Measured" |

## Before → after measurements

| claim | counting command | before (at `bacbe9cc`) | after (at `2f18996d`, receipt committed in `33570c3a`) |
|---|---|---|---|
| R29-C1 | `python3 -I -B tools/round-29/c1-fresh-naming.py --root /home/vgpnk/Projects/shokunin/kaidoku-shokunin --rev <REV>` | `PIN pinned input absent`, exit 2 (`before/c1-at-bacbe9cc.txt`) | `runs_ok=16/16 rows_complete=152/152 tally_equal=1 entry_ok=1`, exit 0 (`after/c1-at-2f18996d.txt`; same at `18be864a`, `after/c1-at-18be864a.txt`) |
| R29-C2 | `python3 -I -B tools/round-29/c2-filtered-unseen.py --root /home/vgpnk/Projects/shokunin/kaidoku-shokunin --rev <REV>` | `PIN pinned input absent`, exit 2 (`before/c2-at-bacbe9cc.txt`) | `responses_complete=178/178 entries=252 mismatches=0 predicted_true=38 predicted_false=214 entry_ok=1`, exit 0 (`after/c2-at-2f18996d.txt`) |

Frozen targets: C1 `16/16, 152/152, 1, 1, exit 0`; C2 `178/178, entries>=1, mismatches 0, predicted_true>=1, predicted_false>=1, entry_ok 1, exit 0`. Both met as measured, with no edit to any frozen file after the freeze (`w1/CriticTargets.md`). Observed C1 triple: named 122, right 122, wrong 0, no name 30. Limits: C1 has a completeness target, not an accuracy bar, and its names were author-selected (a score on public names, not a blind test; `w1/CriticHeldOutC1.md`); in C2 only `mismatches` tests the rule, and 37 of its 252 entries test the name comparison (`w1/CriticHeldOutC2.md`). Both freeze gates FLAG round 29 `INSTRUMENT_UNPINNED` for a script named in the C1 rule text (M29-3, disclosed in both ledgers).

## Sources & frontier

- Census command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kaidoku`. Round start (`before/census.txt`, SOURCES.md equal to base): `kaidoku ok`, six W04 (S033, S047, S054, S062, S069, S083), exit 0. Round end at `2f18996d` (`after/census.txt`): `kaidoku ok`, the same six W04, exit 0.
- Rows 86 → 88 (`grep -cE '^\| S[0-9]{3,} \|' corpus/SOURCES.md`). Added by tier: A 2 (S087 code, Sourcify `handlers.ts` and canonical list at staging `0966a3bc`; S088 docs, ERC-4626 at ethereum/ERCs `3c0f7076`). Both opened 2026-10-22; URL, access time, sha256 and ≤25-word located quote in `corpus/lessons/round-29.md` `## Gate`; search-log entry added. Both re-opened and admitted by non-author seats (`w1/ReopenS087.md`, `w1/ReopenS088.md`).
- Rows touched old→new: none. S085's teaches cell is wrong for 11 of 36 keys; rows are not edited in place, so the correction is a lesson Gate note plus the pointer appended to the round-28 entry.
- Sourced claims: R29-C2 rests on S087, R29-C1's entry cites S088; both counters require those exact rows.
- Frontier: "EVM bytecode (extended)" annotated at `PROVINCE.md:95`; status unchanged.
- Mined mistakes: M29-1..4 in `corpus/lessons/round-29.md` `## Mistakes`. M29-2 and M29-4 have a fix shown able to fail on the real round-26/27/28 filing states (`after/prefile-gate-at-filings.txt`, exit 1). M29-1 and M29-3 are recorded as not shown able to fail.

## Trend verdicts

- **expansion: improved.** Knowledge files 112 → 114, map 114/114 (command A at `18be864a`, `w1/ReviewReadmeRows.md`); SOURCES 86 → 88; the naming rule now covers 16 published interfaces, and the flag rule covers all 26 canonical keys the lane had never fetched.
- **quality: improved.** A sourced rule predicted on never-fetched selectors (0 of 252 mismatches), and every number in both entries was re-derived by independent seats. A new data defect in the list was found, with a receipt. The round-27 instrument is repaired and the round-26/28 ledger disagreements are corrected.
- **discernment: unprovable-but-better.** The wave found real overreach and it was corrected before filing: held-out wording, separation scope, mis-keyed scope, and two mined mistakes whose fixes could not fail. One recurrence (M29-3) was self-flagged. This needs the outside spot-check to rule on.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md` `### Round-29 measurement registry` (`2f18996d`); no promotion verifier.
- [~] At least one end-to-end domain task executed and logged in LOG.md — 16 REA `inspect-evm-interface` runs → lookups → tally, `LOG.md` round-29 entry; `corpus/evidence/round-29/c1/`.
- [~] Instructions executable by an agent without oral context — both counters were re-run from their recheck lines by fresh seats (`w1/ExecRecountC1.md`, `w1/ExecRecountC2.md`); author-dispatched seats, not outside verifiers.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md:95` annotation; `w1/ConnectorSiblings.md` (revenger overlap cited, not absorbed).

## Round shape and seats

- Shape: default v1, one wave. `w1` had 44 seats (executor 15, reviewer 10, critic 7, mutation-tester 5, scout 3, scribe 3, connector 1), validated under `ufo-wave-policy.json` and dispatched as one task call at 20:20:36Z. The spec, dispatch, exact payload with the added `solutionSpace` string, task result and registry are in `.ufo/waves/round-29/`. Seat gate: `wave-slot.sh acquire kaidoku kaidoku-r29-w1 44 3600` → `granted … live=81 … cap=128`; released after all seats settled.
- No wave 2: wave 1 already carried the attack items, and fewer than 32 distinct new attack items remained. No residual call. Round total: 44 seats.
- §3 L2 floor met inside w1: connector, 15 executors, 3 scribes, 3 scouts, 10 reviewers, 7 critics. Planner mapping: the L1 held the canonical planner seat; the planning data walk rode the three scouts.
- Dead seats: 1, `KaidokuR29.CriticAxisFit`, error "Cursor OPENAI: Unable to reach the model provider: We're having trouble connecting to the model provider." Not replaced; its axis-fit question remains for the outside reviewer. No refusals or holds. Item `U064N008Hf47eb933` stays excluded and was not touched.
- Seats settled before filing: the session job listing at about 20:44Z shows no `KaidokuR29.*` job running. `tools/round-29/prefile-check.sh` at `33570c3a`: `prefile: tree clean`; round-24 gate `--disclosures` exit=0; round-29 gate `--disclosures` exit=0; `prefile: PASS`, exit 0.
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows untracked `AGENTS.md`, `live_s228.html`, `nama.html`, `tf_bavelas.html` and staged `write`. None names kaidoku or round 29 (`grep -l -i -E 'kaidoku|R29|round-29'` → 0 each), so none are this lane's; left untouched.
- Disclosures:
  - The L1 ran plain `git status --porcelain` and `git diff` in the lane early in the round, before adding `GIT_OPTIONAL_LOCKS=0`, which can refresh `.git/index`. No tracked content changed.
  - The freeze commit's author time (19:30:33Z) is jj's working-copy creation time; its committer time, 20:03:06Z, is the one the counters use (`w1/CriticTargets.md`).
  - `before/census.txt` was run at 20:07Z, after the freeze, over a SOURCES.md still equal to base.

## Report extras

- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
- Tool installs: none by the L1. Seats installed pycryptodome 4.1.0 with `uv pip` into scratch venvs to compute keccak independently (`ExecIndependentC1`, `ReopenS087`, `CriticHeldOutC2`, `ScoutProvinceFrontier`). No pacman transaction.
- L0 questions: none opened.
- Admission: not asserted here. Both claims met their frozen targets as measured, and no owned axis row changed. The verdict belongs to the non-author closure.
