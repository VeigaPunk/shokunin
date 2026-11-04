# kama — round 84 (2026-11-04)

## Work performed

Declared claims: **C1 operability** — subject-round note binding, disclosed register rotation and thirteen-arm gate; **C2 calibration** (lowest assigned axis7) — eight sealed selfrecord facts answered; **C3 freshness** — five document-backed relation rechecks. **C1 numeric predicate verifies, but its auxiliary disclosure-row instruction is missed; C2/C3 verify within their frozen populations. No unconditional admission.** Scores unchanged8/8/7/9/7/7.

- Integrated subject-round binding, two selftest arms, ten archived ungraded-population rows and one round83 acceptance. The frozen premise incorrectly called the archived event restored; audit actually says ungraded. An event-loss disclosure row would fabricate evidence, so none was appended. Narrative disclosure and byte-exact archive remain (`registry/append-only-late-r83-restored.tsv`, `w1/out/EX02Registers/EX02Registers.md`).
- Composed gate arm13 from pending-falls/pin-rechecks selftests and registered all three round83 verdict scripts plus the new selfrecord instrument (`tools/pre-report-gate.py`, `SKILL.md:1738`). Terminal gate is green at its named measured revision; intermediate red receipts retained.
- Corrected six stale values, preserved two holding direction tests, repaired actual live SCORECARD cells, appended KQ136 and the blame last-modification correction (`corpus/lessons/round-84.md`, `corpus/QUALITY.md:652`, `corpus/knowledge/register-row-introduction.md:36`).
- Opened eight document URLs and independently matched all nine retained extract ranges; relation3 now holds at b7200. Added SGLang readiness/ping distinction without endpoint claims (`measured/after/all-anchor-reopens.json`, `corpus/knowledge/runtime-health-surface-matrix.md`, S572–S575).
- ONE validated v1 wave, **12 settled seats**, zero dead seats: executor5, scribe1, scout1, connector1, reviewer1, critic2, mutation-tester1; attack4/12. No residual call. L1 planner mapping, not dispatched planner. Validator rejected labrat before dispatch; critic CR02Probes replaced it. WAVE-DONE arrived before integration/report (`w1-results.json`). Routing selected by host overrides; no model argument supplied.
- Attacks retained: spec-binding mutants M1/M5 killed, M2/M3/M4 survived; study did not certify the eventual EX01 file. C2 indented-heading/unrelated-token backing escapes and fabricated-but-hash-consistent C3 extracts remain explicit limitations (`w1/out/MT01Binding/mutations.md`, `w1/out/CR01Controls/CR01.md`). Actual source origin was checked independently, never inferred from hashes alone.

Evidence paths abbreviated `w1/` and `measured/` above/below are under lane `.ufo/waves/round-84/`. No inherited uncommitted round84 state. No installs/updates, pacman transactions, service/config/credential edits. Misroot sweep found no owned round84 misplaced output; unrelated fleet files and `.scratch/` untouched (`measured/after/fleet-misroot.out`). Stale-lane: this single steered kama mission progressed; no second kama mission owned. Existing L0 questions remain open (notably fixture ratification and historical record rulings); none newly filed or treated as answered. Connector preserved kengaku S178 attribution; kama's independent serving-document read absorbs no evaluation province (`w1/out/CON01Siblings/overlap.md`).

## Landed changes

Final lane tip **`ad370d57656a259c428db3052388659897c8e076`**, branch master; `git ls-remote origin refs/heads/master` printed that exact hash before report creation. Every commit below is tied to `LOG.md` **Round84**, lines3524–3530, including the subsequent measurement/terminal paragraphs. Only `jj-lane.sh` landed/pushed lane work.

| Commit | Landed work |
|---|---|
| `2d49bf705a2f2f8b45da973407cbb0b2ce2f8fd2` | frozen claims, fixture, before receipts |
| `eb03a64bcd8e2faab0f4f9bcdc55bfc5c1ed2c85` | controls and pre-seat red-before description amendment |
| `3e93febb0f40955b08dc80367e8ef658eaccdfd6` | settled wave, implementations, register/knowledge/source/record integration |
| `65665250e58f5deec028ad53809296e08373818a` | measured receipts, calibration run-fact shape, preserved misses |
| `ffb5f797f5cac099ddf3b1de81ca3480062c40e0` | axis-specific runnable head facts and census receipts |
| `4454f4478707c465cd4fd7a9bb2c9e525452f3cf` | inherited saturation vector through round83 |
| `723253c3882105a56585f84085ddeef0e57f3d57` | canonical next-plan heading and red receipt |
| `c0d7fbd842b66d56483e7ca05b62752341c8b3c4` | truthful latest-measured-round84 marker |
| `b53cd336e0cb204cf71246e95fdf7494babeafa4` | five fully qualified axis receipt paths; final green measured tree |
| `ad370d57656a259c428db3052388659897c8e076` | terminal gate/provenance receipts and append-only dispositions |

## Before → after measurements

| Claim / counting command | Before → after; measured revision |
|---|---|
| C1: `python3 tools/pre-report-gate.py --repo . --round 84 --tip master` | independent clean no-work replay: `arms=12 failed=3 uncommitted=0`, exit1; final at `b53cd336e0cb204cf71246e95fdf7494babeafa4`: `PRE_REPORT round=84 arms=13 failed=0 uncommitted=0`, exit0 (`gate-final-green.out`). Original control had failed5/uncommitted5 from transient receipts; not claimed byte-reproducible. |
| C1 conjunction: `python3 tools/round81-append-debt.py --repo . --round 84`; same with `--late .ufo/waves/round-84/fixtures/late-wrong-subject.tsv` | freeze real register: unaccepted1/bad10 exit1. At `3e93febb`: real unaccepted0/bad0 exit0; fixture exactly one `note-wrong-deletion-round`, bad1, exit1 versus zero binding findings before. Fixture has two uncovered events by design; exit alone is insufficient. Gate's final debt has events76/accepted53/late23/**pending3**/unaccepted0/bad0. C1 auxiliary event-loss disclosure instruction remains **missed**, not waived by numeric success. |
| C2: `python3 tools/round84-selfrecord-round83.py --repo .` | initial instrument with no corrections: claims8/mismatches6/corrected0/unbacked6 exit1 → claims8/mismatches0/corrected6/unbacked0 exit0 at `3e93febb`, repeated at `65665250e58f5deec028ad53809296e08373818a`. `--no-corrections` restores six mismatches, exit1; selftest16/0 exit0. `c2.out`, `c2-final.out`, `c2-red.out`, `c2-selftest.out`. |
| C3: `python3 tools/round83-pin-rechecks.py --repo . --register registry/engine-pin-relations.tsv --rows registry/pin-recheck-rows.tsv` | graded4/ungraded1 → `PIN_RECHECK rows=5 graded=5 holds=5 reworded=0 moved=0 drifted=0 ungraded=0 bad=0`, exit0 at `3e93febb`, repeated at `65665250`; `c3.out`, `c3-final.out`. Eight URLs reopened, nine extract ranges independently equal fetched bytes; no moved/drifted verdict fabricated. |

Gate selftest35/0; debt selftest31/0; round83 selftests pending7/0 and pin14/0. Commands and true exits in retained receipts. Later publication edits are record-only; no green gate is attributed to an unmeasured publication tip. Frozen target values unchanged. Predicate strings abbreviate fields rather than contiguous rendered substrings (C1 field order, C3 interposed verdict fields); locator/token serialization divergences are recorded in lesson. Honest C1 auxiliary miss prevents an unqualified admission request.

## Sources & frontier

Census command at start and end:

```sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kama
```

Before terminal output: `kama ok /home/vgpnk/Projects/shokunin/kama-shokunin/corpus/SOURCES.md`, **exit0**. After identical terminal output, **exit0** (`measured/after/census-after.out`); W01 S481 and W04 cross-scope duplicate-URL warnings remain warnings, not silently suppressed. Counts command `scripts/sources-census.sh census --file corpus/SOURCES.md`: rows **311→315**, A296→300/B11→11/C4→4; mined279→283/queued8→8/rejected24→24 (`census-counts.out`; base committed registry is aca4f33a). New rows S572–S575: four A/mined, opened2026-11-04, located quotes in lesson Gate. Existing status/recheck/used-by changes: **none**. Scratch append census exit0 before append; `python3 tools/sources-append-only.py --from aca4f33ac1e2a8cf815d97daab3b3a5cfa0d78e0 --to 3e93febb0f40955b08dc80367e8ef658eaccdfd6` exits0.

Frontier advanced: formerly ungraded b7200 document and SGLang `/ready` versus `/ping` pause semantics; real appended coverage-table rows correct round83's Frontier-only placement. No new knowledge file or repertoire entry, so rows alone earn no expansion claim. Genuine reject: b7200 examples/server path HTTP404, response line1 “404: Not Found”; flip requires a retrievable revision-specific document. Admit S572 plus that reject are available for outside sampling; no dispatched seat is called outside verifier. Mistake mined: terminal receipts superseded interim success but live cells stayed stale; KQ27 failed to prevent it, KQ136 grounds the repair and `--no-corrections` shows it can fail. Assimilation: **none** — package/proposal fit inspected, no staged entry or unimplemented proposal adopted. No package IDs appended.

## Trend verdicts

- **expansion: unchanged** — new source rows and a documentary extension, but no net new admitted knowledge file or repertoire entry; rows are not knowledge-count credit.
- **quality: improved** — five genuine relation comparisons, registered scripts, green thirteen-arm measurement and corrected terminal cells; formal C1 auxiliary miss and counter limitations remain disclosed, not admitted away.
- **discernment: improved on learned prior disagreement** — round83's outside stale-cell finding becomes six re-derivable corrections plus grounded KQ136; this round's outside admit/reject sample remains pending closure.

## SHONEN

- [~] Decision tables/error patterns/checklists with cited sources — `SKILL.md`, `corpus/QUALITY.md`; author assertion only.
- [~] End-to-end domain task executed — `LOG.md` round16 fixture and round84 documentary recheck receipts; no registered-consumer health asserted.
- [~] Executable instructions — registered commands and terminal gate receipt at b53cd336; no promotion review claimed.
- [~] Province boundary retained — `PROVINCE.md`, `w1/out/CON01Siblings/overlap.md`; operator service/config gates untouched.

Report-attribution audit exercised before fleet commit: `python3 tools/report-landing-audit.py --rounds 10-83 --report 84=/home/vgpnk/Projects/shokunin/.ufo/reports/round-84/kama.md` → `round=84 required=10 post_report=0 defects=0`; overall `summary reports=75 defects=94 corrected=9 uncorrected=85 errata_unmatched=0 errata_invalid=0 status=failed`, **exit1**, from historical report debt. No historical files were rewritten and no overall audit pass is claimed. SHONEN heading count1, assessment lines4. Round scratch `/fast/scratch/hyaku/kama-r84` removed after receipts were retained.
