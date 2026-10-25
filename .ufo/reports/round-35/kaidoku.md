# kaidoku — round 35

## Work performed

Declared claims: **R35-C1 / coverage** — assimilate the `.jsc → source mapping` PROVINCE frontier using jsc2js sources S125/S129; **R35-C2 / calibration** — close four round-34 verifier-routed record defects D1–D4. The claims and kill rules are in lane `plans/round-35-claims.md` and canonical snapshot `kaidoku-shokunin/.ufo/waves/round-35/claims-canonical.json` (freeze commit `2323d197456f1328459d9420aff025cffbcb3e27`). The three owned proxies were tied at 10, none retired, so both axes were lowest; no stagnation waiver.

- Built and self-tested frozen counters for C1/C2; C1 green/red selftest `green=0 red=1`, C2 green/red selftest `green=0 red=1`. These demonstrate only the selftest fixtures, not claim validity (`kaidoku-shokunin/tools/round-35/c1-coverage-counter.py`, `c2-calibration-counter.py`; counter pins and freeze-gate receipt under `.ufo/waves/round-35/`).
- Ran the frozen do-nothing controls before claim data: C1 exit 1 (both entries, rows, province/map references absent); C2 exit 1 (census/lesson/trio/registry conditions absent). Receipts: `kaidoku-shokunin/.ufo/waves/round-35/controls/c1-do-nothing.json`, `c2-do-nothing.json`; commit `3ecf42981a0b63414de90ade643040d609dbb8a5`.
- Opened and captured jsc2js README and release pages for the `.jsc` frontier: `kaidoku-shokunin/.ufo/waves/round-35/prep/jsc-sources/`; sources are S125 and S129 package rows. Independent seat reopens verified the README’s matching-V8 prerequisite and approximate-reconstruction caveat (`w1/R35ScribeJscGate.md:25-51`) and the release enumeration (677 releases on 7 API pages; `w1/R35Audit02.md:40-48`, `R35Audit18.md:15-22`).
- Hand-checked the five kaidoku quarantine rows. S150 is refused as payload-absent: the registered heading is absent from the live article, while a different real body passage exists (`w1/R35Audit26.md:5-18`). S113, S136 and S147 are locatable/reachable now; S117 remains unverifiable/unreachable, not fabrication (`kaidoku-shokunin/corpus/lessons/round-35.md`, `assimilation/quarantine-verdicts.md`).
- Proved the 0–3-leading-space ID extractor on an indented S002 collision fixture. Real registry has 106 rows, staged package 132 rows, one ID collision (`S106`); no rows were appended because the selected entries were not safely admitted (`assimilation/id-guard-proof/`, `assimilation/{reg-ids,staged-ids,collisions}`).
- Mined M35-1 through M35-4 in `kaidoku-shokunin/corpus/lessons/round-35.md`: cross-claim coupling; substring-only counter checks; historical registry/table shape mismatch; and freeze setup-order error. Motive and evidence are attached to each lesson row.
- Ran the required census before and at round end. Both exit 0 with 9 pre-existing W04 duplicate-URL warnings; manual source-row count is 106 both times. Captures: `assimilation/census-start.txt` and `census-end.txt`.
- Dispatched one validated **v2 build/attack wave of 64 seats** via `w1.ready`; plan/spec/dispatch are committed under `kaidoku-shokunin/.ufo/waves/round-35/`. At report cutoff, the orchestrator had not yet delivered `w1-results.json` / `WAVE-DONE`, so settled/dead seat counts and actual role accounting are **not yet verified**; I do not claim the swarm floor is settled. The intended mix from the spec was 27 executor, 11 scribe, 8 mutation-tester, 7 reviewer, 5 critic, 3 scout, 2 connector, 1 sentinel; these are planned roles, not result-derived seat counts.
- No `considerthese/` directory exists in the lane. Assimilation theme selected: `.jsc → source mapping` from `merge/kaidoku/`; no staged content was copied wholesale.
- Fleet-root sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` showed operator state files plus unrelated `?? .ufo/waves/round-30/` and `?? corpus/knowledge/journalctl-v262-field-filter-r36.md`; neither names kaidoku round 35, and neither was touched. No tool installs or updates.

## Landed changes

All lane hashes below were printed as `landed <hash>` by `jj-lane.sh` and are pushed to the lane remote.

| Change | LOG / lesson evidence | Lane commit |
|---|---|---|
| Instruments-first plan, counters, start census, ID guard proof, source captures and quarantine evidence | `LOG.md` round-35 entry; `corpus/lessons/round-35.md` | `d2729cba895b8664f3ccb27196091494f3cda83b` |
| Claims draft / freeze setup and explicit intermediate freeze-path disclosure | `corpus/claim-freezes.tsv`; `kaidoku-shokunin/.ufo/waves/round-35/freeze-status.md` | `a85ca674b92fbb433f9abbeba07b6aee91149433` |
| Canonical claim snapshot and frozen instrument pins | `kaidoku-shokunin/.ufo/waves/round-35/claims-canonical.json`; freeze-integrity exit 0 at `2323d197` | `2323d197456f1328459d9420aff025cffbcb3e27` |
| Do-nothing control receipts | `controls/c1-do-nothing.json`, `controls/c2-do-nothing.json` | `3ecf42981a0b63414de90ade643040d609dbb8a5` |
| Round-35 lesson, SCORECARD verdicts, LOG, census end and wave-1 evidence reports | `corpus/lessons/round-35.md`; `LOG.md`; `SCORECARD.md` | `ee0c865c878492c26fb43aa1c0beaee7b6388f63` |

## Before → after measurements

- **C1 / coverage:** frozen command `python3 -I -B tools/round-35/c1-coverage-counter.py --root <LANE> --freeze <freeze-rev> --rev <measured-rev>`. Before at base `aa04633a`: do-nothing exit 1, 8 named missing conditions (`controls/c1-do-nothing.json`). No post-freeze claim measurement was run. The C1 attack found its PROVINCE/README scope checks are substring-anywhere, not tied to the intended coverage-map/Core table (`w1/R35CriticClaims.md:53-54`); the claim is **unprovable / stopped**, not improved. No score delta.
- **C2 / calibration:** frozen command `python3 -I -B tools/round-35/c2-calibration-counter.py --root <LANE> --base <base-rev> --freeze <freeze-rev> --rev <measured-rev>`. Before at base `aa04633a`: do-nothing exit 1, named missing conditions (`controls/c2-do-nothing.json`). Falsification: all other C2 conditions green but no post-base SOURCES change produces `D1_no_sources_change_after_base`; synthetic `rows=106 EXIT=0 W04` can pass without exact warning count or pin verification; D3 accepts `S1060`; and D4 section/table shape is incompatible with current historical layout (`w1/R35CriticClaims.md:9-45`). Under the unchanged kill rule, C2 is **unprovable / honest stop**. No score delta.
- Freeze integrity: `python3 -I -B tools/round-34/freeze-integrity.py --root <LANE> --round 35 --rev 2323d197456f1328459d9420aff025cffbcb3e27 --claims .ufo/waves/round-35/claims-canonical.json` → `CLEAN pins=4`, exit 0. An earlier draft attempt failed; it remains disclosed in `freeze-status.md` and the freeze ledger rather than being silently erased.

## Sources & frontier

- `corpus/SOURCES.md`: rows **106 → 106**, command `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`. Census command `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kaidoku`: start exit 0, end exit 0; both emit 9 W04 warnings and `kaidoku ok`. No row added by tier; no existing status/recheck/used-by cell changed.
- ID collision: 106 current IDs, 132 staged IDs, collision count 1, `S106`; no renumber map because no row was appended. The collision guard’s indented S002 fixture produced a nonempty collision.
- Frontier rows advanced: none. C1 package adoption was withheld after its counter scope defects and before modifying the registry. Assimilation theme selected but not admitted. S150 remains refused pending a corrected located quote; S117 unverifiable; S113/S136/S147 are now locatable but not adopted because no entry cites them.
- `considerthese/` absent. Assimilation is not complete; this is recorded rather than treated as a pass.

## Trend verdicts

- **expansion: unchanged** — no new knowledge entry or SOURCES row was admitted; C1 stopped.
- **quality: improved** — the round surfaced and durably recorded specific counter/record-quality defects and a concrete quarantine quote mismatch; no claim that these repairs changed the corpus quality score.
- **discernment: unprovable-but-better** — a fresh wave seat disagreed with the frozen C2 predicate based on executable counterexamples, and the lesson captured the disagreement; the required non-author closure spot-check has not yet landed. This remains an unproven trend judgment pending outside confirmation.

## SHONEN

- [~] Decision tables/error patterns/checklists with citations — author assessment only; `SKILL.md:42-79,68-80`, no promotion verifier this round.
- [~] End-to-end domain task executed and logged — historical libjq work at `corpus/lessons/2026-10-15-round-1.md`; round 35 did not run a new REA task.
- [~] Instructions executable without oral context — historical recipes and current round evidence, not independently executed by a non-author this round.
- [~] No cross-domain bleed / PROVINCE accurate — `PROVINCE.md` scope and the bounded `.jsc` frontier; kaidoku/revenger arbitration remains open.

Stale-lane: only kaidoku round 35 is in scope; no other lane mission is open. Round-35 wave has not settled at filing cutoff, so the seat-result ledger and independent non-author claim closure remain outstanding. No tools installed or updated.
