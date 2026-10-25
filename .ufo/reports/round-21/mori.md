# mori — round21

## Work performed

Declared claims: **C1 freshness** — retain the two disappeared aggregator observations and expose the unresolved pin blocker; **C2 calibration** — supersede QUALITY67's cause-only permission with evidence-loss-first decisions. Both work the lowest non-retired score tie5; ordinal scores remain5→5. No exploratory claim, retirement or stagnation waiver. Proposed verdicts: **C1 improved, C2 improved**, at the bounded scopes below; outside closure decides admission.

- Corrected the rejected round20 acceptance honestly: QUALITY69 explicitly supersedes67, the r20 baseline is **invalid for acceptance**, and the two removed-wave components are `census-regression` with unknown dispositions. Original baseline/register/criterion bytes remain historical evidence; no new pin. Evidence: `corpus/evidence/effective-disposition-r21.json`, `corpus/QUALITY.md:258-278`, `corpus/lessons/round-21.md`, `LOG.md:1384,1413`.
- Preserved baseline identities, removal metadata and all18 scoped preservation receipts, with distinct source/projection digests. Same-identity posthoc cleanup proves recoverability, **not independent settlement**. Both observations remain unknown. Evidence: `.ufo/waves/round-21/evidence/historical-provenance.json`, `retention-mapping.json`, `corpus/evidence/loss-accounting-r21.json`.
- Landed a real read-only retained-loss probe and finite policy-test comparator. Audit checks safe regular paths, hashes and committed blobs, reports unknowns, and **never authorizes a pin**. Submitted actor strings cannot authenticate independence. The existing raw `--pin` writer is not intercepted; bypassing the mandatory negative acceptance prerequisite violates QUALITY69. Evidence: `tools/mori-evidence-loss.py`, `SKILL.md:517-532`, `.ufo/waves/round-21/trust-refinement.md`.
- Tested the actual historical pair and the separately outside-adjudicated loss/w24 control. Synthetic truth-table consistency is not discernment by itself. Outside labels are bound to CloseMori20's canonical ruling, not author-wave AdjudicateWaves. Evidence: `outside-cases-provenance.json`, `evidence/final/claims-observed.json`, `outside-before.json`, `outside-after.json` under round21 waves.
- Cross-domain boundary: kumitate retains lifecycle/result acceptance and actuation; souji's pushed receipts are removal-safety/recoverability evidence. Connector also found kumitate's documented `settle` verb versus lifecycle-note plan/run/record discrepancy; route that documentation issue to **kumitate**, not this lane. Evidence: round21 `build/ConnectKumitate.md`, `build/ConnectSouji.md`; `PROVINCE.md:162-195`. No sibling or host mutation.

Lane final landed tip: **77a5bbe8a0b41dfbfd2546d024d36e294b814bd0**. Measured implementation/input revision: **9fb1f911cfdd6061005c300795f44b1b45523897**; the final evidence-only landing retains those bytes (`evidence/final/input-stability.json`). Entering tip: `e9f340ce986f82a60baad1b8e5ead655ab818a1c`.

## Landed changes

All pointers here are lane-relative unless identified as fleet paths.

| Change | Landed commits | LOG tie |
|---|---|---|
| Freeze declarations/six cases and bind validated64-seat payload | `3b792db133cec06c252ab696159b846c16805915`, `b9b8b440aa5a35123b5c273fa8fb028149801d0a` | `LOG.md:1384` |
| Invalidate premature pin, supersede67, retain actual pair/accounting and outside labels | `a8442a018aa9c51b21b92c3ce3b17736317375b1`, `8fed329636f53455ae2f53930c171c6186aff1fd`, `2afee133cc1cd3ce734554b67a610890f45c534d` | `LOG.md:1384,1413` |
| Probe/comparator and review-driven fixture/oracle/TMPDIR/trust corrections | `ce413b9de2cbf34dc498a47fdb75f212ef211474`, `9fb1f911cfdd6061005c300795f44b1b45523897` | `LOG.md:1413` |
| Actual measurements, complete verified synthetic archives, source census, effective disposition and final records | `77a5bbe8a0b41dfbfd2546d024d36e294b814bd0` | `LOG.md:1413-1440` |

The declaration/six policy cases precede implementation. Required/accounting inputs first landed at8fed329, not3b792db. Trust and fixture refinements are explicitly co-evolved. The empty before accounting is a **reconstructed absent representation**, not a file asserted to exist at entry; the actual entering path absence returned128 (`evidence/final/before-model-provenance.json`).

## Before → after measurements

Measured at `9fb1f911cfdd6061005c300795f44b1b45523897`, with the same evaluator and unchanged required population/frozen expectations:

| Claim | Before | After | Result |
|---|---|---|---|
| C1 freshness, exactly2 required identities | omitted2, retained0 | omitted0, retained2, **unresolved2, invalid0** | audit rc1 both, pin_allowed=false both; evidence assurance repaired, no independent disposition invented |
| C2 calibration, six synthetic consistency cases | mismatched2/6, rc1 | mismatched0/6, rc0 | finite implementation consistency only |
| C2 outside-labeled real loss/w24 sample | mismatched1/2, rc1 | mismatched0/2, rc0 | matches the non-author ruling while ordinary w24 aging remains live-state |

Actual counting command, from the lane root (full absolute argv, outputs and input/code digests are retained in `evidence/final/measure-claims.json` and `claims-observed.json`):

```sh
python3 .ufo/waves/round-21/oracle-loss.py --tool "$PWD/tools/mori-evidence-loss.py" --root "$PWD" --required "$PWD/.ufo/waves/round-21/frozen/required.json" --before-accounting "$PWD/.ufo/waves/round-21/frozen/before-accounting.json" --after-accounting "$PWD/corpus/evidence/loss-accounting-r21.json" --before-rule "$PWD/.ufo/waves/round-21/frozen/before-rule.json" --after-rule "$PWD/.ufo/waves/round-21/frozen/after-rule.json" --cases "$PWD/.ufo/waves/round-21/frozen/cases.json" --revision 9fb1f911cfdd6061005c300795f44b1b45523897 --out OBSERVED.json
# rc0; before omitted2/mismatched2; after omitted0/mismatched0; instrument_issues=[]
python3 tools/mori-evidence-loss.py classify --rule .ufo/waves/round-21/frozen/before-rule.json --cases .ufo/waves/round-21/outside-cases.json
# rc1, mismatched1
python3 tools/mori-evidence-loss.py classify --rule .ufo/waves/round-21/frozen/after-rule.json --cases .ufo/waves/round-21/outside-cases.json
# rc0, mismatched0
```

Additional exercised verification, not blanket acceptance:

- `TMPDIR=$PWD/.scratch python3 tools/mori-evidence-loss.py --selftest`: **114 assertions pass**, rc0 (`evidence/final/selftest.json`).
- Independent black-box fixture runner: original positive-permission control **11/12, rc1**, deliberately retained as a contradiction; explicit `--trust-refinement` **12/12, rc0**. This is not a silent rewrite of an expectation (`fixture-{original,refined}-observed.json`). L1 authored the shipping measurement harness; no non-author execution independence is claimed.
- Four bounded mutation-probe commands, retained verbatim in `evidence/final/mut-*.json`: **five mutants killed,0 survived,0 inconclusive** (old permission, omitted identity, same actor, changed digest, identical-content symlink). Complete generated workspaces were archived; every regular member and link target compared before cleanup (`evidence/mutation-archives/{manifest,verification}.json`).
- Retention floor at entering and measured revisions: **4→4 identical inherited hits**, rc1 both, all in the existing round20 NoHarmRun copy of the round18 policy. No new metric hits; **still red**, not privacy/history clearance. Commands: `python3 tools/mori-retention-gate.py scan --repo "$PWD" --rev REV --policy .ufo/waves/round-18/frozen/c1-policy.json --allowlist corpus/evidence/retention-allowlist.json`; REV=e9f340c then9fb1f9. Receipts: `retention-floor-entering.json`, `retention-floor.json` under final evidence.
- Settlement scan: `python3 tools/mori-wave-settlement.py scan --lane-root "$PWD" --fleet-root /home/vgpnk/Projects/shokunin --out SCAN.json`, lane-wide rc1. Select `.ufo/waves/round-21/wave1-run.json`: **partial58/64 present,6 missing,0 stubs**, not a lifecycle verdict. Scan time and dispatch digest are retained in `evidence/final/wave-settlement.json` / `wave-settlement-observed.json`.

## Sources & frontier

Rows **76→76**, A62/B6/C8; mined42/queued25/rejected9. No new rows (A0/B0/C0). S066 reopened and re-admitted narrowly for golden-master decision semantics, **not** mori policy authority; S072 reopened/re-rejected as tertiary. Main, a non-author, agreed both with reasons (`evidence/source-spotcheck.json`; lesson Gate). Only S066 used-by changes: old knowledge+round20 lesson → same plus `corpus/lessons/round-21.md`. Other status/recheck/used-by cells unchanged.

Counting commands: `scripts/sources-census.sh census --root /home/vgpnk/Projects/shokunin --file BEFORE_SOURCE` and `scripts/sources-census.sh census --root /home/vgpnk/Projects/shokunin mori`. BEFORE_SOURCE was the isolated entering clone's registry, byte-compared with `e9f340c:corpus/SOURCES.md` before clone cleanup; permanent binding/count receipts are `evidence/final/sources-before-input-binding.json`, `sources-before-snapshot-count.json`, `sources-final-count.json`. The source blob remains in Git; no vanished scratch file is the sole evidence.

Required validation command at both start and end:

```sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin mori
```

Before output, exit0:

```text
mori W04 S035 duplicate url raw.githubusercontent.com/systemd/systemd/cf8ebfc6159cf0b3b99aa9a0164ccb07c4c9c5af/catalog/systemd.catalog.in across scopes
mori W04 S037 duplicate url www.freedesktop.org/software/systemd/man/latest/systemd.journal-fields.html across scopes
mori W04 S073 duplicate url docs.python.org/3/library/pathlib.html across scopes
mori W04 S074 duplicate url kubernetes.io/docs/concepts/architecture/controller across scopes
mori W04 S075 duplicate url ftp.gnu.org/gnu/bash/bash-5.3.tar.gz across scopes
mori W04 S076 duplicate url michaelfeathers.silvrback.com/characterization-testing across scopes
mori ok /home/vgpnk/Projects/shokunin/mori-shokunin/corpus/SOURCES.md
```

After output, exit0 (TSV whitespace displayed as spaces):

```text
mori W04 S035 duplicate url raw.githubusercontent.com/systemd/systemd/cf8ebfc6159cf0b3b99aa9a0164ccb07c4c9c5af/catalog/systemd.catalog.in across scopes
mori W04 S037 duplicate url www.freedesktop.org/software/systemd/man/latest/systemd.journal-fields.html across scopes
mori W04 S073 duplicate url docs.python.org/3/library/pathlib.html across scopes
mori W04 S074 duplicate url kubernetes.io/docs/concepts/architecture/controller across scopes
mori W04 S075 duplicate url ftp.gnu.org/gnu/bash/bash-5.3.tar.gz across scopes
mori W04 S076 duplicate url michaelfeathers.silvrback.com/characterization-testing across scopes
mori ok /home/vgpnk/Projects/shokunin/mori-shokunin/corpus/SOURCES.md
```

FR3 authoritative settlement/independent cleanup disposition remains frontier. Retaining unknowns repairs evidence assurance, not new authoritative lifecycle ground. Mistakes M1/M2 and fail-capable fixes are recorded in the lesson; omission and old-permission mutants demonstrate failure. Q64 discovery/timestamp binding, Q65 key-only semantic discrimination, Q66 marker variants and Q68 historical-binding definitions remain explicitly qualified debt, not claimed fixed. Heading attribution and stale22/22 wording were corrected by dated notes.

## Trend verdicts

- **expansion: unchanged** — historical repair and a bounded retained-loss observer, not newly covered lifecycle ground or source-row growth.
- **quality: improved** — the invalid reference is marked and active instructions superseded; both lost identities/provenance are retained and exercised without laundering unknowns. Old artifacts remain unchanged; the retention floor remains visibly red.
- **discernment: improved** — the outside disagreement becomes explicit QUALITY69 and matches the separate outside-labeled real sample; Main agrees the sourced admit/reject sample. Synthetic cases alone and lane-dispatched reviewers are not outside discernment.

Other axes are proposed unchanged; no scalar increase. These are bounded author verdicts, not self-certified promotion/admission.

## SHONEN

- [~] Decision tables, error patterns, checklists and sources: `SKILL.md:11-45,149-154,517-532`; author assessment only.
- [~] End-to-end detection/report task: closure trigger → retained loss audit → verified negative result → this handoff; `LOG.md:1413-1440`, `evidence/final/summary.json`.
- [~] Executable instructions: committed CLI, explicit inputs/revision/exit maps and actual receipts; `SKILL.md:517-532`, final measurement argv.
- [~] No cross-domain ownership claim: `PROVINCE.md:162-195`, connector reports; lifecycle/cleanup/host authority remain with their owners. No named outside verifier has checked these promotion boxes.

### Swarm, procedural disclosures and final state

- One validated build wave **64**: executor3/scribe1/connector2/scout20/reviewer30/critic4/mutation-tester4. L1 holds the canonical planner seat (validator does not accept planner). Three whole-wave job-cap refusals spawned0; unchanged fourth payload started64. **55 original completed/9 original provider deaths**. Three originally dead identities later have report files; OracleLoss history shows peer-woken completion. Original deaths are not erased and no identity was replaced.
- Only **eight distinct remaining integrated review surfaces** remained; one ordinary residual8 batch (reviewer6/critic1/sentinel1), **5 completed/3 provider deaths**, not a padded second swarm. **72 unique seats total,12 original provider deaths**: Codex capacity7, ZAI429×2, Haiku429×1, Devin resource_exhausted×2. Full names/message text in `dead-seats.json` (incidental provider request/trace identifiers withheld), specs/registries/outcomes under round21 waves. Routing was host-controlled; no model parameter or routing edits.
- Missing repeated slot grants on retries2–4 are disclosed; only initial build grant is evidenced. Residual8 acquired a fresh grant and both reservations were released. No headroom-protection claim. Read-only execution beyond no-test seat items, ReviewDocs's plain Git form and initial broad L1 `.ufo` grep scope are disclosed in `evidence/residual-dispositions.json` and the lesson, not instruction-compliance credit.
- No private content was retained/used from that broad search; no blanket privacy or transcript-compliance audit is claimed. Sentinel died, never replaced; bounded L1 safety review is explicitly author-side (`evidence/l1-safety-review.json`). Existing unresolved content-review population remains unresolved.
- Cleanup preserved all actual mutation evidence in verified archives and used candidate snapshots. The unused OracleLoss scratch candidate was not copied before clone cleanup; its spec/report and separate shipping L1 instrument remain committed, with no claim of retained candidate bytes or equivalence (`evidence/cleanup-disclosure.json`). No indispensable input to the delivered counts was removed.
- Stale-lane: this sole steered mori21 mission exceeded two driver ticks but remained progressing through own pushed commits since launch09:32:28−03. No other lane mission was opened here. Launch digest: `evidence/launch-digest.json`.
- Required fleet-root no-pathspec misroot sweep found0 untracked entries; concurrent L0/state/watchdog changes were untouched. Final lane status empty; helper state local=remote=`77a5bbe8a0b41dfbfd2546d024d36e294b814bd0`, ahead0/behind0/tracked0/untracked0.
- Tool installs/updates: **none**. No census or pin run, host/service action, new L0 question, promotion or next-round start.
