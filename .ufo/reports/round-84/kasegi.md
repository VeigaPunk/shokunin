# kasegi — round 84 report (attempt 1)

Lane HEAD is `e4593d6c992bd8e8668abf5be8503f86424be82d` on master, pushed: `git ls-remote origin refs/heads/master` prints it.
- Base: `a089ff3d601b4d53a5515e52720ba27e5ec72c3d`
- Freeze: `7f76b7eb690cd6e75e7f3e7729cedcb15611b34b`
- Landing: `c91c944fde0b2c9d62db14901c0aec2edb072950`
- Receipts and bookkeeping: `e4593d6c`

## Work performed

Declared claims are frozen in `.ufo/waves/round-84/claims.json` at `7f76b7eb`. The r83 closure and `corpus/lessons/round-83-verifier-spotcheck.md` (routed defects 1–8) were read before the freeze.

- **C1 — depth:verifiability** (lowest non-retired axis; nominal 4 per R58).
  - **What lands:** the recheck-cwd census successor `e5f2e4bd…`, with six new checks: noprefix-only, summary-fields, entry-bare-pass, argv-values, verbose-order, entry-set.
  - **Kill target:** all 76 non-neutral rows of a 79-row table. That includes the twelve r83 MutC1Hunt survivors H01–H12, which both the r83 bytes and a check-name stub let survive.
  - **Counter limbs:** the r84 counter's selftest limbs fail three counter mutants (M09, M10, M12) that the r83 selftest passes.
  - **Result: VERIFIED (P1–P8).**
- **C2 — coverage (8).** Admit Frontier F60, `corpus/knowledge/osv-gcs-data-dump-layout.md`, on S118 (the OSV.dev Data sources page, opened 2026-11-06). This is the round's sourced claim. **Result: VERIFIED (B0–B8).**

Work items:

- **Controls** (executed before scoring and committed in the freeze, `.ufo/waves/round-84/controls/`):
  - `c1-donothing-r84.txt`: r83 bytes under the r84 counter give `killed=64 survived=12`, H01–H12 SURVIVED, rc 1.
  - `c1-stub-r84.txt`: the check-name stub gives `survived=12`, rc 1.
  - `c1-candidate-r84.txt`: the candidate gives `killed=76 neutral_ok=3/3 decoy=ok`, 76 counted per-row lines, 12 H rows KILLED, rc 0.
  - `c1-counter-mutants-r84.txt`: M09/M10/M12 give `selftest=ok` under r83 and `FAIL` under r84; result `as-expected`.
  - `c2-prefreeze-r84.txt`: B0 OK; literal sweep 0 over 97 entries; do-nothing state FRONTIER-CENSUS rows 59, S118 queued; the r83 gate passes the draft.
  - `c2-draft-v0-r84.txt`: the first draft fails G6 with `untied=2`, rc 1.
- **S118 capture:** `corpus/source-snapshots/round-84/S118.txt` (sha256 `e824a735…5359`). The six-quote manifest's B0 check prints six `OK occurrences=1`.
- **Wave `w1`** (12 seats, 0 dead). Integrated into F60 before landing; the six pins are unchanged and the gate still passes:
  - ReviewC2 M1: Claim 5's "finds nothing" overreach.
  - ReviewC2 M2: Claim 4 disclosed as a second-source pin of F59 ground.
  - ReviewC2 L1: the not-claimed carve-out.
  - CriticClaims B5: Claim 1's field attribution.
  - ScoutSource §3.4: the live bucket still serves 30 frozen colon-suffixed directories. This is recorded in Limits only.
- **Wave findings that do not change a verdict** (routed to r85 in `corpus/lessons/round-84.md` § Routed to round 85):
  - MutC1Hunt: 22 new survivors over the frozen candidate.
  - MutCounter: 5 semantic survivors in the counter.
  - CriticClaims A1: a table-lookup forgery of the F12 class passes under the r84 counter; P2/P3's `target_sha256` pin is the identity limb.
  - ExecC1RealTree: exit 1 rather than 2 on an unreadable root.
- **CriticTrend axis-label finding (recorded, not hidden):** the scored depth:verifiability meter (`resolve.py`/`anchorcheck.py`) does not read this instrument. C1 is gate hardening with no meter move, and the lowest-axis obligation has moved only nominally since r70. Round 85 is planned to make a meter move or a recorded retire/split (`SCORECARD.md` § Round 84, "Planned round 85").
- **SHONEN evidence pointers corrected** (CriticTrend 1–2): `SHONEN.md:6,8`.
- **Landing receipt over the cited commit** (r83 routed defect 7): `.ufo/waves/round-84/l1/landing-r84.sh` extracts `c91c944f` with `git archive` and runs P1–P8 and B0–B7 on that extract (`l1/L1-landing-r84.txt`). B8 printed `header=bad` on the extract: the r83 gate takes the manifest path relative to `--lane`, so the extract cannot match. B8 was re-run in the worktree after `cmp` showed the entry, manifest, snapshot and gate equal to the landing bytes: `ENTRY-GATE-RESULT pass`, rc 0 (same receipt, appended section).

## Landed changes

| Change | LOG.md entry | Commit |
|---|---|---|
| Freeze: claims, C1 candidate/counter/table/builder, controls, S118 snapshot + manifest, S118 row `queued` | LOG.md `## Round 84` bullets 1–2 | `7f76b7eb690cd6e75e7f3e7729cedcb15611b34b` |
| `corpus/instruments/recheck-cwd-census.py` → `e5f2e4bd…`; SKILL.md and instruments/README pin rows `cases=33` | LOG.md `## Round 84` bullets 1, 4 | `c91c944fde0b2c9d62db14901c0aec2edb072950` |
| F60 entry; S118 `mined`; knowledge-expected; README F60 block; PROVINCE F60 line | LOG.md `## Round 84` bullets 4–5 | `c91c944f` |
| Lesson `corpus/lessons/round-84.md` (M84-1, M84-2, routed-defect table); QUALITY R135; SHONEN pointer fixes; wave spec, dispatch, results and 12 seat reports | LOG.md `## Round 84` bullets 3, 6, 8 | `c91c944f` |
| Landing receipt, census-end receipt, SCORECARD `## Round 84`, LOG `## Round 84` | LOG.md `## Round 84` bullet 4 | `e4593d6c992bd8e8668abf5be8503f86424be82d` |

## Before → after measurements

- **C1** (measured at landing `c91c944f`, over the git-archive extract).
  - Counting command: `python3 -B .ufo/waves/round-84/c1/mutbat.py --target corpus/instruments/recheck-cwd-census.py --table .ufo/waves/round-84/c1/mutant-table.json --expect-cases 33 --work $SCRATCH`
  - Before (base r83 bytes `343b21e4`): `baseline=bad rows=79 killed=64 survived=12 … neutral_ok=0/3 decoy=broken`, rc 1, H01–H12 SURVIVED; selftest `cases=27`.
  - After: `MUTBAT target_sha256=e5f2e4bd… baseline=ok rows=79 killed=76 survived=0 miskilled=0 dirty=0 notderived=0 neutral_ok=3/3 decoy=ok decoy_hidden=75/76`, rc 0; `killed_lines=76 h_killed=12`; selftest `cases=33 failures=0`.
  - P4: `mutbat selftest ok`, `r84_limbs` all True.
  - P5: `as-expected`.
  - P6: lane tree (98 entries) conformant, rc 0.
  - P7: both controls end rc=1 with 12 H rows SURVIVED.
  - P8: `cases33=1 cases27=0` in both pin rows.
  - Score 4 → 4 (nominal).
- **C2** (measured at landing `c91c944f`).
  - Counting command: `python3 corpus/instruments/frontier-recheck-count.py | grep FRONTIER-CENSUS ; ls corpus/knowledge/*.md | wc -l ; grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`
  - Before (freeze `7f76b7eb`): rows=59, knowledge 97, registry 118, S118 `queued`.
  - After: `FRONTIER-CENSUS rows=60 admitted=60 closed=60 problem-rows=0 registry=118`, `FRONTIER-PASS F60 ids=S118`, knowledge 98, S118 `mined`.
  - B1: one row pair (S118).
  - B4: `unbound=0`.
  - B5: recheck line exact; foreign rc 0.
  - B6: `literal_sweep_total 0 files 97`.
  - B7: rc 0.
  - B8: `ruleless=0 untied=0` pass.
  - Score 8 → 8 (the denominator is operator-owned).
- **Harm check:**
  - depth:density: SKILL.md mean 273.2 → 273.2.
  - SCORECARD and LOG: additions only.
  - R133 Gate placeholder count: 0.

## Sources & frontier

- **Census command:** `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kasegi`
  - Round start: `kasegi ok`, six inherited W04 (S028 S029 S072 S076 S080 S085), rc 0 (`.ufo/waves/round-84/controls/census-start-r84.txt`).
  - Round end: `kasegi ok`, rc 0 (`.ufo/waves/round-84/l1/census-end-r84.txt`).
- **Registry rows:** 117 → 118, counted with the `grep -cE` command above. One row added, tier A `docs`: **S118**, OSV.dev Data sources, https://google.github.io/osv.dev/data/, opened 2026-11-06, HTTP 200.
- **Rows touched (old → new):** S118 status `queued` → `mined`; used-by `—` → `corpus/knowledge/osv-gcs-data-dump-layout.md`. Logged in the SOURCES registry-changes block and in the lesson Gate.
- **Frontier advanced:** F59 → F60. This opens r83 ScoutPerish lead 2. Lead 1 (data-quality initiatives post) stays a lead; its r83 quote spans two lines and was rejected as a pin (lesson § Gate).
- **Sourced claim:** C2 rests on S118.
- **Mistakes mined** (`corpus/lessons/round-84.md` § Mistakes):
  - M84-1 `rule-paraphrase-drifts-from-quote-vocabulary`: v0 fails rc 1, v1 passes rc 0. The G6 pass is not cited as rule quality, per R134.
  - M84-2 `rule-consequence-contradicts-own-limits`: captured-by none. The fix is QUALITY R135, whose check prints 1 on the draft and 0 on the landed entry (`.ufo/waves/round-84/l1/r135-check-r84.txt`).
- **Assimilation: none.** The staged-id collision check found 88 collisions (S031..S118), with the guard proven on an indented fixture (`w1/ConnectorOverlap-receipts/assimilation/`). The r77 L0 question is still open.
- **considerthese:** `considerthese/2026-10-26.md` proposal 2's open half (one end-to-end domain task) was identified. It is not adopted this round and is planned for r85.

## Trend verdicts

- **expansion: improved.**
  - F60 adds OSV.dev's own export-layout statements: withdrawn records in the full zip, the [EMPTY]/ directory, the per-ecosystem csv prefix rule, colon-suffixed folding, and the stopped prefixed exports.
  - Frontier 59 → 60, knowledge 97 → 98, registry 117 → 118 (S118 mined).
  - Claim 4 is disclosed as a second-source pin of F59 ground.
- **quality: improved.**
  - The landed census kills 76/76, including H01–H12, which the r83 bytes and the stub let survive.
  - The counter selftest now kills M09/M10/M12.
  - The landing receipt is measured over the cited commit.
  - Carried limits are recorded: F8/F12/F13, 22 MutC1Hunt r84 survivors, and 5 MutCounter semantic survivors.
- **discernment: improved.**
  - Wave falsifications were integrated before landing: Claim 5 overreach, F59 overlap, Claim 1 attribution.
  - The axis-label critique is recorded in SCORECARD rather than claimed away.
  - Two mistakes were mined, giving R135.
  - The SHONEN self-assessment mismatches were fixed.
  - Needs the non-author closure check.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources. Evidence: `corpus/lessons/round-47-verifier-spotcheck.md:94` (non-author); pin row updated to `cases=33` this round.
- [ ] At least one end-to-end domain task executed and logged in LOG.md. Untouched; considerthese proposal 2 is planned for r85 (`SHONEN.md:8`).
- [~] Instructions executable by an agent without oral context. Evidence: `corpus/lessons/round-47-verifier-spotcheck.md`; F60's `recheck:` exits 0 from a foreign cwd (B5).
- [~] No cross-domain bleed (PROVINCE.md still accurate). Evidence: `PROVINCE.md` F60 line; ConnectorOverlap found no sibling lane holding the ground (`w1/ConnectorOverlap.md` §1).

## Round shape and other items

- **Shape:** one v1 wave `w1` of 12 seats, dispatched via the inline handoff (`w1.ready` with l1=`KasegiR84`; `w1-results.json` reports `seats 12`).
  - Roles: executor×3, mutation-tester×2, reviewer×2, critic×2, scout×1, scribe×1, connector×1.
  - Attack seats: 6/12.
  - Dead seats: 0.
  - No residual call. Round total: 12.
- **Planner seat:** held by the L1, because the validator rejects `planner`.
- **Inherited state:** none. The lane was clean at `a089ff3d` and there was no earlier attempt of r84.
- **Push incident:** the freeze push hit GitHub `remote: Internal Server Error` twice. A later `jj-lane.sh push` landed `7f76b7eb`. The seats read the committed freeze bytes locally.
- **Misroot sweep:** fleet `git status --porcelain` shows `.scratch/` entries and `trail-ids.txt`. `trail-ids.txt` is 1 byte (`,0`), mtime 20:36, before this round's wave dispatch at 20:46, and does not name kasegi. It is not this lane's file and was not touched. No kasegi misroots. Scratch `/fast/scratch/hyaku/kasegi-r84` was removed after landing.
- **Stale-lane:** respawn-per-round driver; no other mission of this lane is open.
- **Tool installs:** none.
- **Open L0 questions:** r77 staged-package id collisions (R-77-E) and the source-recheck anchor window (R-77-D). Both are carried and were not re-filed.
