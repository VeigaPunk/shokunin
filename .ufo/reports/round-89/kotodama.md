# kotodama — round 89 report

Lane `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, branch `main`, final
lane hash `bd4153ff1f67650487edcdcd98af74cd30280899` (`git ls-remote origin
refs/heads/main` prints it). Base `42816d2533c44f1d19f38a12fc5f5040d01a2fd3`.
Attempt 1. No `lane-dead-no-report kotodama round=89` line existed, so nothing
was inherited. L1 agent: KotodamaR89.

## Work performed

The round declared two claims:

- **F / freshness** (the lowest non-retired axis, worked directly). Live re-verification of the 16 URL-bearing rows in the registry's upcoming-recheck queue.
- **C / coverage** (the sourced claim). A dedicated entry, `corpus/knowledge/linguistics/evidentiality-epistemic-marking.md`.

Work items:

- **Freeze before data.** `1cbd0efc56edaa9394e3532fc5d8ef924f122f01` carries:
  - `reports/round-89/claims.json` (sha256 `cd74cfc2…`);
  - counter `reports/round-89/measure89.py` (sha256 `6bc14bcd…`);
  - the executed controls `reports/round-89/controls/controls.txt`. All 9 rows matched their expectation:
    - do-nothing F 3/5 and C 2/8;
    - bump-only, wrong-capture, fabricated-id, sourceless and gate-without-capture each fail their named leg;
    - two declared known survivors: forged captures for F and for C.
  - counter selftest `counter-selftest.txt`, PASS 21/21, keeping raw child stdout/stderr/rc (QUALITY35);
  - the selftest's red-before `selftest-redbefore.txt`: with BACKED forced true, the selftest scores 18/21 and exits 1;
  - `quality-oneliners.txt`: the QUALITY25 and QUALITY28 shape checks both exit 0;
  - `census-start.txt` (exit 0) and `recheck-queue-base.txt` (`0 due / 20 upcoming / 16 on-release / 859 rows`);
  - the SCORECARD "Planned / frozen — round 89" table, in the same commit.
- **Do-nothing at the freeze.** `reports/round-89/at-freeze-{F,C}.txt` score F 3/5 and C 2/8. These landed at `9ad00be1a48d33a4f54e1663a1d46e4590cc3438`, together with the wave spec and dispatch.
- **Claim F.** ExecRecheckA/B fetched all 16 rows live with curl, which included Wayback for S142's own snapshot URL and Crossref negotiation for S032. Every row is LOCATED with a quote that supports its teaches cell.
  - ReviewerRefetch fetched the same rows independently with python urllib. Each executor quote also occurs in the independent captures: 16/16 (`reports/round-89/rechecks/refetch-agreement.json`).
  - Recheck changed 90d→2027-02-03, which keeps the 90-day cadence. Each change is logged old→new in `corpus/lessons/round-89.md` `## Gate`.
  - Captures and manifest are in `reports/round-89/rechecks/`.
- **Claim C.** ScribeEvidentiality opened WALS chapters 77 and 78, de Haan 1999 (abstract only), Tournadre & LaPolla 2014 and the SIL glossary. These became S936–S940. Glottopedia was opened and rejected as S941.
  - The entry is 19,901 B with 10 headings and a 5×6 coding table. It contains a NON-CANON micro-design, refusals and open questions.
  - Its 8-word shingle overlap with five neighbouring entries is 0 (`reports/round-89/final/honest-landing-audit.json`).
  - Captures are in `reports/round-89/evidence/`. The README index has the row, linguistics heading (34) and a footer block. `check-corpus-index` reports OK 261.
- **Attacks (wave):**
  - ReviewerCounter: shadow duplicate rows, site-chrome quotes, any-year Wayback, off-topic filler, capture = graded file, and NOT-LOCATED spelling variants all pass the frozen counter (`.ufo/waves/round-89/w1/ReviewerCounter.md`).
  - MutationCounter: the selftest kills 10 of 41 non-equivalent mutants (`MutationCounter.md`).
  - CriticClaims: the round-11 pause conflict, the C surface understating the base, title-quote and copied-section landings (`CriticClaims.md`).
  - Because of these, `reports/round-89/audit89.py` audits the real landing against every class found: `structural_classes_clear: true` (`final/honest-landing-audit.json`).
- **Separability.** `reports/round-89/separability89.py` (from ExecSeparability, authored after dispatch) builds deterministic overlay commits at the freeze. The F overlay passes 5/5 and the C overlay 8/8 (`final/separability.json`).
- **R88 routed defects.** V1 through V7 are each dispositioned in the lesson (`## R88 routed-defect dispositions`). V3 is documented in `SKILL.md` and SCORECARD. V2 is repaired prospectively by the r89 counter selftest. V5 is handled by the reproducible overlay procedure.
- **SKILL.md.** New section "Source re-verification — the recheck queue", the method this round learned.
- **QUALITY.md.** Criterion 36, grounded in the wave's executed survivors; it binds round 90.
- **First-measure defect, disclosed.** At `590c20671f38dff203fdd879235fd61b61a9aff7`, F failed BACKED 4/5 on S105. The S104 lesson prose named S105, so the counter picked S104's line. Only that prose was changed, at `aac9cca8`. The receipt is kept as `reports/round-89/final/lands-F-first.txt`.

## Landed changes

| commit | content | LOG.md entry |
|---|---|---|
| `1cbd0efc56edaa9394e3532fc5d8ef924f122f01` | freeze: claims, counter, controls generator and receipts, selftest + red-before, census start, queue base, SCORECARD plan | LOG round 89 |
| `9ad00be1a48d33a4f54e1663a1d46e4590cc3438` | wave spec/dispatch/registry, do-nothing counter runs at freeze | LOG round 89 |
| `590c20671f38dff203fdd879235fd61b61a9aff7` | SOURCES (16 recheck cells, S936–S941), new entry, README, lesson, QUALITY36, SKILL, rechecks/, evidence/, separability89.py | LOG round 89 |
| `aac9cca80d12077eb3026b202c835c0d6135bc08` | lesson prose fix (S104 line) + first F receipt | LOG round 89 |
| `bd4153ff1f67650487edcdcd98af74cd30280899` | final receipts, audit89.py, census end, SCORECARD axes, LOG, lesson settlement, settled wave evidence (11 seat reports, stage, w1-results.json, ready markers) | LOG round 89 |

Fleet: L0 question commit `7b398ea8a73f4e159bf035aafbb66bb2f058e12c`.

## Before → after measurements

Every count below comes from the frozen counter in a `git clone --shared` checkout of the lands commit `aac9cca80d12077eb3026b202c835c0d6135bc08`, with freeze `1cbd0efc56edaa9394e3532fc5d8ef924f122f01`. That lands commit is the measured revision. bd4153ff only adds records on top of it.

- **F:** `python3 -B reports/round-89/measure89.py --root <clone> --freeze 1cbd0efc56edaa9394e3532fc5d8ef924f122f01 --lands aac9cca80d12077eb3026b202c835c0d6135bc08 --claim F --work <existing-dir>`
  - Before: 3/5 at the freeze (ADVANCED 0, DISPOSED fail). The auditor showed `0 due / 20 upcoming`.
  - After: **rc0 `ACCEPT-F-89: PASS legs=5/5`**: ADVANCED 16, BACKED 16/16, DISPOSED, OTHERCELLS (`reports/round-89/final/lands-F.txt`). The auditor at lands shows `0 due / 4 upcoming / 16 on-release / 865 rows` (`final/recheck-queue-lands.txt`).
- **C:** the same command with `--claim C`.
  - Before: 2/8 at the freeze; the entry was absent and linguistics had 33 files.
  - After: **rc0 `ACCEPT-C-89: PASS legs=8/8`**:
    - ENTRY: 19901 B, 10 headings;
    - TABLE: [5,6];
    - NEWIDS: S936–S940;
    - GATE, CAPTURE, INDEX (tool rc 0), APPENDONLY.
  - Receipt: `final/lands-C.txt`.
- **Separability:** the F overlay passes 5/5 and the C overlay 8/8 (`final/separability.json`).

## Sources & frontier

- **Rows: 859 → 865.** Command: `git show <rev>:corpus/SOURCES.md | awk -F'|' '/^ {0,3}\| *S[0-9]{3,}/…'` (`reports/round-89/final/registry-counts.txt`).
  - By tier: A 507→511, B 328→329, C 24→25.
  - By status: mined 757→762, queued 58→58, rejected 44→45.
- **Added this round:** S936–S939 (tier A, mined), S940 (B, mined), S941 (C, rejected; flip condition stated).
- **Rows touched old→new:** the `recheck` cell of 16 rows, 90d→2027-02-03: S009 S012 S020 S021 S031 S032 S033 S084 S104 S105 S106 S107 S142 S157 S163 S875. Each change is logged in the lesson Gate. No status or used-by cell changed.
- **Frontier rows advanced:** the 16 rechecks. Stale findings were flagged and carried to round 90, not fixed:
  - S142 anchor reads "by", the source reads "for";
  - S012 and S021 now have newer arXiv versions;
  - S104's children appear only in the page script;
  - S157's biomes have grown.
- **Census:** `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama` exits 0 at start and at end (`reports/round-89/census-start.txt`, `census-end.txt`). The final line is `kotodama ok`.
- **Sourced claim:** C rests on S936–S940, opened 2026-11-04.
- **Mined mistakes:** R89-M1 through M7 in `corpus/lessons/round-89.md` `## Mistakes`.
- **Assimilation:** none. There is no considerthese directory in this lane.

## Trend verdicts

- **expansion: improved.** One admitted knowledge entry on ground the registry did not hold: there were no evidentiality or WALS-chapter rows at base. The surface is contested. Base already had sub-sections in semantics-pragmatics §4 and syntax-typology §4, which the frozen surface text understated (R89-M4). The new content (coding axis, counts, access/egophoric, areal) does not overlap them (shingle overlap 0).
- **quality: improved.** 16 registry rows were re-verified live, with 16/16 independent agreement. The lane's 20-row recheck queue dropped to 4. QUALITY36 and the SKILL re-verification method were added.
- **discernment: improved.** S941 was rejected with a flip condition. The wave's survivor findings were recorded against the lane's own counter rather than hidden. This verdict is author-side and still needs the non-author closure.

## Round shape and seats

- **Wave:** one v1 wave, `kotodama-r89-v1`, 11 seats in a single dispatch.
- **Role mix:**
  - executor 3: ExecRecheckA, ExecRecheckB, ExecSeparability;
  - scribe 2: ScribeEvidentiality, ScribeLesson;
  - scout 1: ScoutOverlap;
  - connector 1: ConnectorSiblings;
  - reviewer 2: ReviewerRefetch, ReviewerCounter;
  - critic 1: CriticClaims;
  - mutation-tester 1: MutationCounter.
- **Attack share:** 4/11 = 36 %.
- **Round total:** 11 seats. All 11 delivered reports and none died. There was no replacement and no residual call.
- **Planner:** the L1 holds the planner seat, because the validator rejects planner as a role. ScoutOverlap ran the bounded data-walk.
- **Wave results:** WAVE-DONE was received before the report. `w1-results.json` carries no per-seat status or id (the same gap as R88-M6). Delivery is evidenced by the 11 report files.
- **Routing:** the host route table, `task.agentModelOverrides`. No model was passed.

## Open questions and limits

- **L0 `kotodama | round-89`:** does F fall inside the round-11 freshness pause? F is measured, and admission is left to the closure and the operator (R89-M7).
- **Inherited and still open:** the formal L2-planner conflict, the R86-C1 numeric-mapping debt, the r84 cited-record red, and the L0 questions from rounds 51 and 69.
- **Counter limits (R89-M5/M6):** the frozen counter's mutation score is 10/41, and several undeclared survivor classes exist. Those classes are audited on this landing only.
- **Stale-lane:** respawn-per-round driver; no other mission of this lane is open.
- **Tools installed or upgraded:** none by L1. Every seat report also says none.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources. Pointer: SKILL.md "Source re-verification — the recheck queue" and the R88-V3 note; the entry's table cites S936–S940. No non-author verifier yet.
- [~] At least one end-to-end domain task executed and logged in LOG.md. Pointer: LOG.md round 89, 16 live re-verifications plus the evidentiality entry with a NON-CANON design. No lore handoff accepted.
- [~] Instructions executable by an agent without oral context. Pointer: `reports/round-89/measure89.py --selftest` 21/21; the declared commands carry `--work`; separability89.py is reproducible.
- [~] No cross-domain bleed (PROVINCE.md still accurate). Pointer: `.ufo/waves/round-89/w1/ConnectorSiblings.md` finds no sibling overlap, and lore CM-d is handed off; PROVINCE.md is unchanged.
