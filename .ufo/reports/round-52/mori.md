# mori — round 52 report (attempt 1, L1 MoriR52)

Lane `mori-shokunin`, branch `master`. Entering tip `4f266ef2fdf74d8b046f5b4f5a5c4945f65b966d`; freeze
`d3a8ea5957b73bddbde750a8c0af2fba8da8b7c2`; data `8524904adb25e44f24d9f25aac7eae909625c18c`; wave spec
`075436b1346ca659afb8be7a46f0e67e4170aa83`; measured revision `e7e056b8a17e54516a3c17798221c30e9902c250`; final lane tip `37af57f263cf0f035fa6d19f666d2de7790b63b7` (receipts commit; `git ls-remote origin refs/heads/master` prints it). Report commit `[FILL]`.

## Work performed

Declared claims (frozen at `d3a8ea59`, `.ufo/waves/round-52/contract.md`): **C1 — calibration**: at R the
self-assessment agrees with the fleet `MANIFEST.json` (mori rounds ≤ 51, verdict exactly `admitted`), with the
instruments (SHONEN tally pins rerun at R with round-52 receipts) and with its own pointers (Axes rows, SHONEN
boxes, quoted strings and `proposed A → B` pairs); K4 is taken beyond SHONEN to the living command-tally pins of
`corpus/QUALITY.md` and `corpus/README.md` — every pin runs today or is superseded by a later line, never rewritten
(routed defect 4 of the round-50 closure). **C2 — depth** (a lowest axis, tied at 5): what `/proc/meminfo`'s
`CommitLimit` and `Committed_AS` are at kernel v7.2: the overcommit ledger, its three modes, where the limit is
enforced (mode 2 only), the reserves and the refusal log line. Entry
`corpus/knowledge/overcommit-commit-limit-r52.md`, rows S497–S501. C2's entailment arm is the round-51 arm
hardened per the round-51 closure §5 item 2: ≥ 2 distinct non-author ENTAILMENT voters per row, unfenced lines,
frozen voter list `Mo52Ent01`–`Mo52Ent12`, `REPLACE` authorship signal.

- Census at round start: rc 0, 23 W04 (`.ufo/waves/round-52/evidence/census-start.txt`).
- Five source copies fetched and pinned by sha256 (`corpus/evidence/sources-r52/`); sweep at `4f266ef2`: thirteen
  overcommit terms have 0 hits; `merge/mori/` has 0 files on the theme (`evidence/sweep-overcommit.txt`).
- Freeze `d3a8ea59` before any seat ran: contract, both counters with `--selftest` (`C1_SELFTEST pass=42 fail=0`,
  `C2_SELFTEST pass=45 fail=0`), the C1 data applier and control builder, eight C1 control receipts (do-nothing,
  axes-only, receipts-only, living-only, rewrite-in-place, delete-stale-pins, repeat-stale-tally, witness),
  `control-c2-do-nothing.txt`, `freeze-sha256.txt` (24 files).
- Data `8524904a`: C1 Axes cells lead with round 51 (operability, depth), SHONEN round-52 receipts, QUALITY
  141–142, README `## Round-52 corrections`, freshness locator `:1771` → `:1781`, entry + S497–S501. At data:
  `C1=met … mismatches=0 … lane_writes=0` (`evidence/c1-at-data.txt`); `C2=unmet … failed=entailment`
  (`evidence/c2-at-data.txt`).
- Wave `w1`: 68 seats, policy v2, validated rc 0 (first validation refused the `labrat` role — `evidence/w1-validate-refused.txt` — fixed by the copy-on-change wrapper `build-w1-spec-amend.py`). Voters voted 28/28 rows; row 3 drew two `overclaim` votes; rows 27/28 were reworded to the literal `SZ_128K`/`SZ_8K` caps after `RevNoHarm` found the MiB wording conflated documented intent with the byte constant. New texts re-voted by non-author voters (row 3: Ent02/Ent03/Ent04; rows 27/28: Ent10/Ent11/Ent12). Reports in `.ufo/waves/round-52/w1/`, results in `w1-results.json`.
- Integration `2f245af7d6dd6878de266f3436d12f47df900144`: SKILL `## Round52`, SHONEN boxes, QUALITY 143 (supersedes 140's “Not covered”), LOG and SCORECARD round 52, README coverage block, lesson `round-52.md`, erratum `round-51-erratum.md`, round-39 scratch residue removal. Wave close `e7e056b8a17e54516a3c17798221c30e9902c250` (Mo52MutC1Controls report, `w1-results.json`); receipts `37af57f263cf0f035fa6d19f666d2de7790b63b7`.
- Planner seat: held by the L1 (the validator rejects `planner`); bounded planning rode the L1 and wave items.

## Landed changes

| commit | what | LOG.md |
|---|---|---|
| `d3a8ea59` | freeze: contract, counters, controls, receipts, census-start, sweep, source copies | Round 52 header |
| `8524904a` | data: C1 cells/receipts/living pins/locator; C2 entry + S497–S501 | Round 52 C1/C2 bullets |
| `075436b1` | wave spec (amended), dispatch, receipts at data | Round 52 header |
| `2f245af7` | integration: SKILL/SHONEN/QUALITY 143/LOG/SCORECARD/README/lesson/erratum/wave reports (67) | Round 52 (`LOG.md:2807-2860`) |
| `e7e056b8` | wave close: Mo52MutC1Controls report, `w1-results.json` | Round 52 |
| `37af57f2` | receipts at landed tip: `c1-at-landed.txt`, `c2-at-landed.txt`, `census-end.txt` | Round 52 |
| `[FILL]` | receipts at landed tip: `c1-at-landed.txt`, `c2-at-landed.txt`, `census-end.txt` | Round 52 |

## Before → after measurements

- **C1**: `python3 .ufo/waves/round-52/count-c1.py R [--scratch DIR]`.
  - Before (`4f266ef2`): `C1=unmet items=37 axes=6 pins=2 boxes=4 living=4 superseded=1 locators=25 mismatches=8
    errors=0 hidden=0 lane_writes=0 … failed=mismatch`, exit 1 (`evidence/control-c1-do-nothing.txt`).
  - After (`e7e056b8`): `C1=met items=43 axes=6 pins=2 boxes=4 living=7 superseded=4 locators=28 mismatches=0
    errors=0 hidden=0 lane_writes=0 manifest=6209bdb8e400`, exit 0 (`evidence/c1-at-landed.txt`). Two earlier runs at the integration tip read `lane_writes=1` because the wave close wrote `Mo52MutC1Controls.md` / `w1-results.json` mid-run; the receipt is the quiescent run.
  - Controls: do-nothing 8, axes-only 5, receipts-only 6, living-only 5, rewrite-in-place 3, delete-stale-pins
    3, repeat-stale-tally 3 — all unmet; witness met (feasibility, disclosed).
- **C2**: `python3 .ufo/waves/round-52/count-c2.py R`.
  - Before (`4f266ef2`): `C2=unmet claims=0 … pins=bad … failed=entry_absent,pins`, exit 1
    (`evidence/control-c2-do-nothing.txt`). At data: `failed=entailment`.
  - After (`e7e056b8`): `C2=met claims=28 located=28 quote_missing=0 bad_rows=0 sources=5 source_rows=ok pins=ok
    provenance=ok entailed=28 dissent=0`, exit 0 (`evidence/c2-at-landed.txt`).
- Named limits (contract; wave-confirmed): receipts are pure text (a handwritten receipt passes — `CritC1Junk`);
  the newest closure file is trusted verbatim for scores; a `supersedes` line quoting a stale span needs no
  replacement pin tied to the subject; arm A's verdict comparison is pinned only to `admitted` (M4 survivor) and
  `superseded()` accepts the pin's own criterion (M8 survivor); `lane_writes` measures working-tree churn, so
  final runs use a quiescent tree; the locator arm covers the Axes rows and SHONEN boxes only (QUALITY/README hold
  78 more pointers); C2 voter distinctness is by filename and a REPLACE line is the only authorship signal.

## Sources & frontier

- Census `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin mori`: start rc 0, 23 W04
  (`evidence/census-start.txt`); end rc 0, 23 W04 (`evidence/census-end.txt`). Rows 269 → 274 (S497–S501, tier A, mined,
  opened 2026-10-26).
- Rows touched old→new: S497 anchor `45`→`48`, `83-84`→`83-85`; S499 anchor `901-1006`→`901-1003`,
  `806-834`→`806-840`; S501 anchor `1585-1619`→`1579-1619`; S501 teaches (literal KiB caps), logged in the
  lesson's Gate table.
- Frontier: the overcommit entry covers commit-ledger ground the coverage map did not hold (sweep: 0 hits; README
  round-52 block); FR8 stays open (no threshold proposed).
- Sourced claim: C2 rests on S497–S501.
- Assimilation: none (`merge/mori/` holds no overcommit staging). considerthese: suggestion 3 (re-execute what
  closures only evidence-verified) — the round-51 counters were rerun at `70e68cdd` and reproduced their landed
  receipts field for field (`w1/Mo52ExecR51C1Rerun.md`, `w1/Mo52ExecR51C2Rerun.md`).

## Trend verdicts

- **expansion: improved.** One entry on commit-ledger ground the lane did not hold (13-zero-term sweep); five
  mined tier-A rows; the README coverage block lands.
- **quality: improved.** K4 closes three stale living pins without rewriting them; the locator arm caught the
  `:1771`/`:1781` drift; two overclaim rows and two unit-conflation rows were replaced and re-voted; the
  round-51 counter reruns agree byte for byte.
- **discernment: unprovable-but-better.** The two-voter non-author entailment arm and the replacement votes are
  recorded leave the non-author closure to judge; the admit (5 pinned v7.2 copies) and reject (rendered `latest`
  page) decisions are in the lesson Gate.

## SHONEN

[~] SKILL.md decision tables, error patterns, checklists with sources — `SKILL.md:1143` (Round52); `corpus/QUALITY.md:1252-1373`
[~] an end-to-end domain task executed and logged — `LOG.md:2807` (Round 52); `.ufo/waves/round-52/evidence/c2-at-landed.txt`
[~] instructions executable without oral context — `python3 tools/mori-pin-check.py --selftest` (125/125); `python3 tools/mori-unlanded-check.py --selftest` (17/17); receipts `.ufo/waves/round-52/evidence/selftests/`
[~] no cross-domain bleed — `corpus/knowledge/overcommit-commit-limit-r52.md:68-75` Boundaries (entry Boundaries); `w1/Mo52ConnSiblings.md`

## Extras and defects

- Round shape: one v2 wave `w1` of 68 seats (reviewer 12, critic 12, executor 21, mutation-tester 4, connector 2,
  sentinel 3, revenger 2, scribe 9, scout 2, simplifier 1; flash-eligible 36, attack 28). Dead seats: 0.
  `w1-results.json` holds all 68 seat results; the last seat's report landed with the wave close. Residual calls: 0
  (replacement votes appended in place by the seeded voters). Round total: 68.
- Misroots: fleet root clean at sweep (`w1/Mo52ExecMisrootSweep.md`); no mori round-52 misroot. Seat scratch
  `/fast/scratch/hyaku/mori-r52` removed after landing.
- Round-51 closure routed defects: 1 → both counters ship `--selftest`; 2 → P-C2 arm; 3 → C1 survivors routed
  (M4/M8); 4 → C1; 5 → erratum `round-51-erratum.md`; 6 → no frozen file edited; 7 → literal receipts; 8 →
  in-lane writers inventoried and routed with a successor-freeze design.
- Stale-lane: respawn-per-round driver; no other mori mission is open.
- Tool installs: none.
- Open L0 questions: none.
