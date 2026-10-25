# mori — round 16

## Work performed

**Declared claim C1 — coverage / capability acquisition:** add bounded, read-only, MESSAGE-free journal record observation after an exact retained anchor, for one explicit scope and the anchor's boot. Coverage6 is the lowest owned non-retired axis versus operability7; scores are held. This is a new standalone probe, **not a census cutover**. The claim is verified by L1 at its finite scope; independent non-author closure remains pending. Execution is **not fully conformant**.

- Added `tools/mori-journal-window.py`: fixed single-scope argv, inclusive cursor query, exact first-record cursor/boot acceptance, anchor exclusion, same-boot/unique-cursor checks, four separate validated-positive subsets, and unavailable without numeric totals on unsafe capture. Both streams have byte/time bounds; cursor state is never advanced. Source chain: S014/S015/S039/S040 → `corpus/knowledge/journal-cursor-window-r16.md`; evidence `.ufo/waves/round-16/evidence/capability-after/run-manifest.json` in the lane.
- Added the registered finite regression gate, input digest table and16 packs/64 cases. Added the static context gate; original instruction text goes red and a context-only correction goes green. Neither text conformance nor author-seat approval establishes runtime prevention (`evidence/context-{original,corrected,selftest}.json`).
- Corrected all five routed round-15 items: L1 owns the omitted broadcast restriction; the omitted `/tmp/mori-r15-expected-probe-final.json` write is disclosed; implementing selftests did not authorize executing them; active r15 hidden-flag registry prose is corrected; the old red drift pin stays unre-pinned. Append-only dispositions: `corpus/lessons/round-16.md` C15-1…C15-5, Q37–Q42, and LOG round16. The historical report, lessons and verifier files were not rewritten.
- Retained victim/authentication/access/retention limits and F01 whole-function/F02 reconstructed-prefix witness qualifications. Existing census/oracle/r13–r15 gates and r10 baseline match all6 entering byte pins (`evidence/preservation.json`); their old committed gate evidence was verified statically, **not re-executed**.
- Ran one authorized bounded live observation per user/system scope: both OK, both anchor-only with0 after-anchor records and0 positive subsets. These are not positive live load, no-event conclusions, complete access, or live vacuum/alias tests (`evidence/live-window-{user,system}.json`, `live-window-manifest.json`). Raw live anchors were temporary in-lane inputs, removed before landing; committed receipts contain safe hashes/boot and aggregates only.
- Wave1 dispatched64 seats as one unchanged validated native task payload. Role mix:20 executor /10 scout /8 scribe /6 connector /10 reviewer /8 critic /2 sentinel. L1 held the canonical planner seat. All64 reports are retained. **Operator wrap-up ordered no more workers: planned wave2=32 was never validated or dispatched and is skipped. Round total=64.** Evidence: `wave1-{spec,dispatch,assignments,record,task-response}.json`, `build/swarm-registry.json`, `operator-wrapup.json` under lane round16 waves. No worker was spawned after wrap-up.
- Required fleet misroot sweep found only two mori reports in fleet `round-16/build`: FieldDocs and ReviewLesson. L1 attributed their headers, copied byte-exact to the lane, `cmp` exited0, then deleted only those two fleet copies under the prompt exception. Unrelated hyaku artifacts were untouched (`evidence/misroot-sweep.json`, lesson M33).

**Procedural debt, not hidden by green tests:** seats made unauthorized live/synthetic probes, `/tmp` or `/run/user` staging writes, and background waits. ReviewCounts also overwrote the lesson with a placeholder; its owner restored the authored lesson and L1 inspected the restored sections. These observations are excluded from acceptance. Initial context lacked an explicit live-journal ban despite its general no-checks rule; corrected text is an undispatched comparison fixture, not a retroactive dispatch repair. The lesson's Mistakes table preserves attribution and read-time/removal qualifications. `/tmp/sc.tsv` was reported not removed, and an empty temporary directory has no retained pathname; L1 did not expand scope to remove outside-lane artifacts. No runtime-prevention claim is made.

## Landed changes

Lane repo: `/home/vgpnk/Projects/shokunin/mori-shokunin`.
**Pushed lane HEAD before this report was written:** `9de05bdbc914d3b1ac4898dc529c7884ae993dd0`.
`git push` advanced origin master from `b83edc6` to `9de05bd`; required pre-report lane porcelain was empty.

| Carrying commit | Changes tied to LOG |
|---|---|
| `114ebe5e141805a72d704e05c618a5f2be3927da` | settled window tool, finite/context gates, fixture packs, wave evidence, source/knowledge/frontier work, routed correction criteria and active registry; LOG “Round16” and “integration and operator wrap-up” |
| `685c8735658a23bf821c47c67b8f92c52a1e3543` | retain actual first measurement failures; repair selftest layout and omitted refusal-want handling without changing fixture bytes; LOG “first authorized measurement and setup repairs” |
| `87a57c13dbb1fc2d3e049bba98aca1739822b8c9` | committed expected digest table plus successful repaired gate-selftest/pin receipts; the C1 input measurement commit |
| `9de05bdbc914d3b1ac4898dc529c7884ae993dd0` | finite/live/count/preservation receipts,64 reports including relocated misroots, measured SCORECARD capability, append-only lesson/knowledge corrections and final LOG “delivered measurements and landing” |

All lane commits use the configured mori identity. SHONEN boxes and rank were not changed. Entering tree was clean; there was no inherited round16 work to discard. Protected non-author verifier artifacts were read, not edited.

## Before → after measurements

### C1 — finite capability, not historical production defects

Entering revision: `b83edc6ee3db6822382ab673d7e6e984e420f22f`; the window tool is absent there (`frozen/entering-capability.json`, `git cat-file -e` exit128).
Final gate/probe/pack/expected bytes measured at `87a57c13dbb1fc2d3e049bba98aca1739822b8c9`, unchanged in delivered HEAD.

Same gate/pack/expected table, before `--tool .../frozen/absent-mori-journal-window.py`, after `--tool tools/mori-journal-window.py`:

```sh
python3 tools/mori-round16-regressions.py --fixtures .ufo/waves/round-16/fixtures --expected .ufo/waves/round-16/expected.json --tool <before-or-after-tool> --output <isolated-evidence-dir>
jq -s '[.[] | {verdict,total:.summary.total,matched:.summary.matched,capability_absent:.summary.capability_absent,mismatched:.summary.mismatched,unmet:(.summary.capability_absent + .summary.mismatched)}]' .ufo/waves/round-16/evidence/capability-before/run-manifest.json .ufo/waves/round-16/evidence/capability-after/run-manifest.json
```

Executed counting command exit0 (`evidence/c1-count.json`):

```json
[
  {"verdict":"capability_absent","total":64,"matched":0,"capability_absent":64,"mismatched":0,"unmet":64},
  {"verdict":"ok","total":64,"matched":64,"capability_absent":0,"mismatched":0,"unmet":0}
]
```

Strict gate exits1→0. Before means64 absent capability requirements and zero target executions, **not64 defects reproduced in old code**. After partitions into30 OK /31 unavailable /3 setup expectations; every case matches. Expected table SHA `89b1b5c997c43c5ad5f2bc1bdbd96b4846ac8cf5abb1c09f948c16e611faef15`, gate SHA `e70ed67ce502a7b25fdaa3dac562589df3e4fce02f770ec0adf21f47a1921fce`, probe SHA `d61e0d220a1825d738e2b9526b2bdd92047e39a4543d0ca0a040795d84ba0aeb`. All declared input digests match start/end; real HEAD and exact porcelain are retained. Evidence-output paths make the whole tree dirty, so no whole-tree-clean measurement is claimed.

| Authorized check | Observed result | Receipt / measured bytes |
|---|---|---|
| window `--selftest` | exit0,16 cases/16 passed/0 failed; producer's predicted17 is superseded by observation | `evidence/window-selftest.json`, `114ebe5` probe bytes unchanged afterward |
| regression `--selftest`, first | exit1: child gate rejects output under stub parent | `evidence/gate-selftest.json`, `114ebe5` |
| regression `--pin-fixtures`, first | exit2: legitimate refusal omitted optional `want` | `evidence/pin.json`, `114ebe5` |
| same regression selftest after repair | exit0,6 named arms: pin, green, absent, tool drift, wrong-want mismatch, pack drift | `evidence/gate-selftest-fixed.json`, `685c873` gate bytes unchanged afterward |
| same pin command after repair | exit0,16 packs/64 cases persisted | `evidence/pin-fixed.json`, `685c873` |
| context selftest | exit0,15 isolated arms | `evidence/context-selftest.json` |
| original → context-only corrected snapshot | exit1 `CONTEXT_MISSING no_live_journal_queries` → exit0 `CONTEXT_OK` | `evidence/context-{original,corrected}.json`; corrected snapshot never dispatched |
| live user / live system | exit0 / exit0, each0 records after anchor and all four subsets0 | `evidence/live-window-{user,system}.json`, `87a57c1` |
| old production artifacts |6/6 SHA-256 equal to entering pins; prior red drift evidence retained | `evidence/preservation.json`; old gates not rerun |

Initial gate-setup failure text is committed and the same commands go green after the narrow repair; those failures are not production behavioral red. Bound configuration is local10s and8MiB per stream, with owned-child termination/reap. No latency distribution, marginal speedup, event completeness or authenticated-emitter claim is made.

Per-axis verdicts: **coverage improved (6 held); operability unchanged (7 held); depth unchanged (5 held); freshness unchanged (5 held); calibration unchanged (5 held); adjacency unchanged (6 held)**. No code-axis harm is established; procedural breaches remain nonconformance, not a waived pass. The operator/non-author closure decides admission.

## Sources & frontier

The source count is knowledge provenance, not an improvement quota. One admitted-by-lane note and a working capability advance only FR11's exact retained anchor-boot window. Alias resolution, missing/vacuumed cursors, cross-boot ordering, inaccessible/removed records and completeness remain unknown/unavailable; the production census is unchanged.

Required command at start and end:

```sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin mori
```

Before output, exit0 (`sources-before.json`):

```text
mori W04 S035 duplicate url raw.githubusercontent.com/systemd/systemd/cf8ebfc6159cf0b3b99aa9a0164ccb07c4c9c5af/catalog/systemd.catalog.in across scopes
mori W04 S037 duplicate url www.freedesktop.org/software/systemd/man/latest/systemd.journal-fields.html across scopes
mori ok /home/vgpnk/Projects/shokunin/mori-shokunin/corpus/SOURCES.md
```

After output, exit0 (`evidence/sources-after.json`):

```text
mori W04 S035 duplicate url raw.githubusercontent.com/systemd/systemd/cf8ebfc6159cf0b3b99aa9a0164ccb07c4c9c5af/catalog/systemd.catalog.in across scopes
mori W04 S037 duplicate url www.freedesktop.org/software/systemd/man/latest/systemd.journal-fields.html across scopes
mori ok /home/vgpnk/Projects/shokunin/mori-shokunin/corpus/SOURCES.md
```

Static before→after census (`evidence/sources-count.json`, exit0; exact executable Python argv retained there) reads entering committed SOURCES and delivered SOURCES, selects `^\|\s*S\d{3,}\s*\|` rows, splits11 cells and counts tier/status:

```text
rows38→40; A35→37/B2→2/C1→1; mined17→19/queued20→20/rejected1→1.
Rows added by tier: A2/B0/C0. New S039 seek-cursor and S040 test-cursor: docs/A/mined.
```

For a concise recount of the retained measurements: `jq '{before,after,new_ids,changes}' .ufo/waves/round-16/evidence/sources-measurement.json`.
Only S014/S015 final `used-by` cells extend to the new note; their full old→new strings are in lesson “Measured Gate decision”. No entering immutable/status/recheck cell changed. Temporary S013/S035/S037 extensions were reverted. The new-row URLs, access date2026-10-20, located23-word/12-word quotes and candidates/rejects are under lesson `## Gate`; L1 opened both official pages. The knowledge note appends a named correction superseding the obsolete combined-S039 drafting discussion. Historical seat summaries remain read-time evidence, not current registry authority.

Mistakes M1–M4 learn the outside r15 findings; M31/M32 retain actual failing setup witnesses and M33 records the misroot fix. Instruction breaches are not repaired by admonition or a passing static gate. The old drift-pin red is carried without re-pin, and F01/F02 causal qualifications remain unchanged.

## Trend verdicts

- **expansion: improved.** New S014/S015/S039/S040-sourced `journal-cursor-window-r16.md`, FR11 coverage-map ground and an actually demonstrated capability; finite64/64 and live2/2 OK, not source-row growth alone.
- **quality: improved.** Active hidden-flag contradiction is corrected; exact-start/access/alias boundaries are explicit; two actual gate-setup failures are preserved and repaired. Prior production inputs remain byte-identical. Old drift is still red debt, not a full freshness pass.
- **discernment: unchanged.** Prior outside findings became grounded criteria and corrections, but current outside admit/reject sampling is pending. Repeated seat breaches show instruction text is not runtime prevention; no discernment improvement credit is taken for64 author-lane advisers.

Stale-lane: respawn-per-round; no other mori mission is open. This steered round progressed through committed lane work and ends here; no round17 was started.
Tools: **no install or update** by L1 or reported seats. Pacman transactions stayed paused; no separate omp CLI, credential/agent.db access, host-service change or remediation was performed by L1. No new L0 question was appended; operator host-recovery decisions remain outside this lane.

## SHONEN

- [~] Real decision tables/error patterns/checklists/cited sources — `SKILL.md`, new knowledge note and `corpus/QUALITY.md`; author assertion only.
- [~] End-to-end domain task executed/logged — LOG round16 trigger→bounded read→safe receipt→handoff; `evidence/live-window-manifest.json`.
- [~] Executable instructions — registered CLI interfaces, committed expected table, delivered selftests and finite receipts; not blanket conformance or an outside certification.
- [~] No domain-ownership expansion — `PROVINCE.md`, standalone probe and unchanged production pins; unauthorized staging/probes remain disclosed procedural violations, not authorized scope.

All four canonical SHONEN boxes remain `[ ]`; promotion and independent closure are operator-owned. Orchestrator action: retain the outside-verification queue, old red pin and procedural debt; wave2 was explicitly skipped by wrap-up, and no additional workers should be launched for this run.
