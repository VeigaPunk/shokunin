# kasegi — round 83 report (attempt 2)

Lane HEAD `795f24da00348ee290378f679e4b23b5a5c80138` (master, pushed; `git ls-remote origin refs/heads/master` prints it). Base `834bf78eaca70a69294f2ecfefa89b73c3fa85b8`, freeze `0cd499dbdfc0bf9ce3095681af9bc76588d76f31` (attempt 1), landing `795f24da` (attempt 2; it also carries the wave evidence and results).

## Work performed

Declared claims (frozen in `.ufo/waves/round-83/claims.json` at `0cd499db`; history read before the freeze: the r82 closure and `corpus/lessons/round-82-verifier-spotcheck.md`, routed defects 1–7):
- **C1 — depth:verifiability (lowest non-retired axis, 4, nominal per R58):** land the recheck-cwd census successor `343b21e4…08c9` (adds checks `bucket-other`, `bucket-over`, `main-verbose`, closing the r82 MutC1Hunt gaps G1–G4). It is scored by an r83 counter (constant `mutbat-t-` run directories, nonce-keyed decoys D1/D2, a single-anchor D3 decoy, `extra` sites) over a 67-row table. Forgeries F9 (path label), F10 (decoy-hash whitelist) and F11 (missing-anchor count) score rc 0 under the r82 counter and must exit 1 under r83. F8 (AST embedding) is the recorded limit. **VERIFIED (P1–P8).**
- **C2 — coverage (8):** admit Frontier F59 `corpus/knowledge/osv-faq-post-import-record-lifecycle.md` on S117 (OSV.dev FAQ, opened 2026-11-06; the round's sourced claim). The r83 entry gate's G6 tie limb must reject three rule forgeries (filler, crosscite, copyrule) that the r82 gate passes. **VERIFIED (B0–B8).**

Work items:
- Attempt 1 (L1 `KasegiR83`) did the freeze, the controls, wave `w1` and every landing edit. It ended mid-receipt (watchdog `lane-dead-no-report kasegi round=83`, 20:22:53 -03). Its partial receipt is kept: `.ufo/waves/round-83/l1/L1-landing-r83-attempt1-partial.txt`, which stops at P4.
- Attempt 2 (this L1) inherited the uncommitted tree. It re-verified the tree with the unchanged `l1/landing-r83.sh`, which prints 11× `FROZEN-OK` and shows that every P and B predicate holds (`.ufo/waves/round-83/l1/L1-landing-r83.txt`). Nothing inherited was discarded. Attempt 2 dispatched no new wave and changed no frozen byte.
- Controls were executed before scoring and committed in the freeze (`.ufo/waves/round-83/controls/`):
  - r82 bytes under the r83 counter: `baseline=bad killed=60 survived=4`, rc 1 (`c1-donothing-r83.txt`).
  - Check-name stub: G1–G4 `SURVIVED`, rc 1 (`c1-stub-r83.txt`).
  - Candidate: `killed=64 neutral_ok=3/3 decoy=ok`, rc 0 (`c1-candidate-r83.txt`).
  - F9–F11: rc 0 under r82 and rc 1 under r83 (`c1-forgeries-r83.txt`).
  - G6 forgeries: rc 0 under the r82 gate and rc 1 `untied=1` under r83 (`c2-g6-controls-r83.txt`).
- S117 capture: `corpus/source-snapshots/round-83/S117.txt` (sha256 `0a5fa51c…e53e`) with a six-quote manifest. B0 prints six `OK occurrences=1`.
- D3 decoy probe: all 39 eligible rows are clean (`l1/d3-exhaustive-r83.txt`, `D3-EXHAUSTIVE eligible=39/64 clean=39 broken=0`).
- Wave findings that falsify parts of the claims' prose. They are recorded rather than turned into verdict changes, because the frozen kill rules route them to r84 (`corpus/lessons/round-83.md` § L1 verdicts):
  - CriticClaims F12 (marker-aware forgery) and F13 (F11 plus comment strip) pass the r83 counter. "Count forgeries" holds for F11's bytes, not for the whole count class.
  - G6 is lexical: six echo rules pass it, and admitted F57 Claim 2 fails it. This is recorded as M83-2 and backs QUALITY R134.
  - MutCounter M09: the `extra` limb is not exercised by `--selftest`.
  - MutEntryGate: 8 of 16 mutants survive.
  - MutC1Hunt: 12 survivors beyond the table.
  - ReviewC1 Major 1: latent f-string issue in `comment_lines`.
- Entry fixes from ReviewC2 (Medium 1–2, Low 1–3) were applied to F59 before landing. B8 was re-run afterwards: `untied=0`, pass.

## Landed changes

| Change | LOG.md entry | Commit |
|---|---|---|
| Freeze: claims, C1 candidate/counter/table/builder, C2 G6 gate, controls, S117 snapshot + manifest, S117 row `queued` | LOG.md `## Round 83` bullets 1–2 | `0cd499dbdfc0bf9ce3095681af9bc76588d76f31` |
| `corpus/instruments/recheck-cwd-census.py` → `343b21e4…`; SKILL.md and instruments/README pin rows `cases=27` | LOG.md `## Round 83` bullets 4, 6 | `795f24da00348ee290378f679e4b23b5a5c80138` |
| F59 entry; S117 `mined`; knowledge-expected; README F59 rows; PROVINCE F59 line | LOG.md `## Round 83` bullet 5 | `795f24da` |
| `corpus/lessons/round-83.md` (M83-1, M83-2, routed-defect table, attempt-2 note); QUALITY R134; SCORECARD `## Round 83`; wave spec/dispatch/results/13 seat reports; L1 receipts | LOG.md `## Round 83` bullets 3, 7, 10 | `795f24da` |

## Before → after measurements

- **C1** (measured at landing `795f24da`). Counting command: `python3 -B .ufo/waves/round-83/c1/mutbat.py --target corpus/instruments/recheck-cwd-census.py --table .ufo/waves/round-83/c1/mutant-table.json --expect-cases 27 --work $SCRATCH`
  - Before (base `834bf78e`, r82 bytes `81677e9d`): `baseline=bad rows=67 killed=60 survived=4 … neutral_ok=0/3 decoy=broken`, rc 1, with G1–G4 SURVIVED
  - After: `baseline=ok rows=67 killed=64 survived=0 miskilled=0 dirty=0 notderived=0 neutral_ok=3/3 decoy=ok decoy_hidden=63/64`, rc 0
  - Selftest `cases=24` → `cases=27 failures=0`
  - F9/F10/F11: rc 0 under the r82 counter → rc 1 under r83 (F9 `killed=0`; F10 and F11 `decoy=broken`)
  - F6/F7: rc 1 under both counters
  - F8: rc 0 under r83 (recorded limit)
  - P5 lane conformant, rc 0
  - P8 pin rows `cases27=1 cases24=0`
  - Score 4 → 4 (nominal per R58)
- **C2** (measured at landing `795f24da`). Counting command: `python3 corpus/instruments/frontier-recheck-count.py | grep FRONTIER-CENSUS ; ls corpus/knowledge/*.md | wc -l ; grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`
  - Before (freeze `0cd499db`): `rows=58`, knowledge 96, registry 117, S117 `queued`
  - After: `FRONTIER-CENSUS rows=59 admitted=59 closed=59 problem-rows=0 registry=117`, `FRONTIER-PASS F59 ids=S117`, knowledge 97, S117 `mined`
  - B4 `unbound=0`
  - B5 foreign-cwd rc 0
  - B6 `literal_sweep_total 0 files 96`
  - B8 `ruleless=0 untied=0` pass; the three forgeries are rc 0 under r82 and rc 1 `untied=1` under r83
  - Score 8 → 8 (the coverage denominator is operator-owned)
- **No axis harmed:**
  - depth:density SKILL.md mean 272.8 → 273.2 (receipt § harm)
  - SCORECARD and LOG changes are additions only
  - R133 placeholder count on the lesson Gate is 0

## Sources & frontier

- **Census command:** `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kasegi`
  - Round start: `kasegi ok`, six inherited W04 (S028 S029 S072 S076 S080 S085), rc 0 (`.ufo/waves/round-83/controls/census-start-r83.txt`)
  - Round end: `kasegi ok`, the same six W04, rc 0 (`.ufo/waves/round-83/l1/census-end-r83.txt`)
- **Registry rows:** 116 → 117 (same `grep -cE` command as above). One row added, tier A `docs`: **S117**, OSV.dev FAQ, opened 2026-11-06, HTTP 200.
- **Rows touched (old → new):** S117 status `queued` → `mined`; used-by `—` → `corpus/knowledge/osv-faq-post-import-record-lifecycle.md`. Logged in the SOURCES registry-changes block and in the lesson.
- **Frontier advanced:** F58 → F59. This answers the post-import ground of the r82 lead "Managing the Perishability of OSV Records". ScoutPerish found no public copy of that document: repo tree, issue and commit search, five candidate paths, all negative (`w1/ScoutPerish.md`).
- **Sourced claim:** C2 rests on S117.
- **Mistakes mined** (`corpus/lessons/round-83.md` § Mistakes):
  - M83-1 `claim-prose-names-one-residual-class`: the fix fails and passes on the F9–F11 controls.
  - M83-2 `gate-tie-limb-measures-stems`: run A fails and run B passes; backs QUALITY R134.
- **Assimilation: none.** 87 staged-id collisions (`w1/ConnectorOverlap.md`); the r77 L0 question is still pending.
- **considerthese:** scanned by ConnectorOverlap; no proposal adopted this round.

## Trend verdicts

- **expansion: improved.** F59 adds OSV.dev's own post-import record-lifecycle statements: withdrawn exclusion, deletion handling with the 10 % abort threshold, `modified_id.csv`, and alias recomputation bumping `modified`. Literal sweep over the 96 other entries = 0. Frontier 58 → 59, knowledge 96 → 97.
- **quality: improved.**
  - The landed gate kills 64/64 case-matched rows, including G1–G4, which the r82 bytes and a check-name stub both let survive.
  - The counter rejects F9–F11, which the r82 counter accepted.
  - Carried limits, recorded rather than hidden: F8, F12, F13, G6 lexicality, M09.
- **discernment: improved.**
  - r82 routed defects 1, 2, 3 and 6 are answered in the lesson's routed-defect table; 4 is partly answered; 5 and 7 are carried.
  - Wave falsifications of the claims' own prose (F12/F13, G6 false positive on F57) are written up as M83-1 recurrence and M83-2/R134, not hidden.
  - Needs the non-author closure check.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — evidence: SKILL.md recheck-cwd pin row updated to `cases=27` this round; author assertion.
- [ ] At least one end-to-end domain task executed and logged in LOG.md — untouched (`corpus/lessons/round-61.md`).
- [~] Instructions executable by an agent without oral context — evidence: `corpus/lessons/round-47-verifier-spotcheck.md`; F59 `recheck:` runs from a foreign cwd (B5 rc 0).
- [~] No cross-domain bleed (PROVINCE.md still accurate) — evidence: `PROVINCE.md` F59 line appended within OSV ground (ConnectorOverlap: no sibling holds it).

## Round shape and other items

- **Shape:** one v1 wave `w1` of 13 seats, dispatched in attempt 1 via the inline handoff (`w1.ready` l1=`KasegiR83`; `w1-results.json`: `seats 13`, 13 outputs).
  - Roles: executor×4, scribe×1, scout×1, reviewer×2, mutation-tester×3, critic×1, connector×1.
  - Attack seats: 6/13.
  - Dead seats: 0.
  - No residual call. Round total: 13.
- **Planner seat:** held by the L1, because the validator rejects `planner`.
- **Inherited state (attempt 2):** reused after re-verification:
  - freeze `0cd499db`
  - wave `w1` results
  - every uncommitted landing edit: 10 modified files, the F59 entry, the lesson, the wave dir
  - Nothing was discarded. The attempt-1 partial receipt was renamed and kept.
- **Routed to round 84:**
  - rename-based D3 decoy
  - F12/F13 as counter controls
  - a selftest row for `extra` (M09)
  - the `comment_lines` f-string fix
  - MutC1Hunt r83 gaps
  - a non-lexical G6 per R134
  - stated-output instrument review/landing
  - lead: OSV data-quality initiatives post
- **Misroot sweep:** `git status --porcelain` on the fleet root shows only orchestrator `.scratch/` entries; no kasegi misroots. Scratch `/fast/scratch/hyaku/kasegi-r83` was removed after landing.
- **Stale-lane:** respawn-per-round driver; no other mission of this lane is open.
- **Tool installs:** none.
- **Open L0 questions:** r77 staged-package id collisions (R-77-E) and the source-recheck anchor window (R-77-D), both carried and not re-filed.
