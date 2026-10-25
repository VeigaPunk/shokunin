# Round 14 registry-home design review

Scope: advisory, bounded design review for the assigned registry-home cutover. This is not a top-level round plan, an implementation, a score, a promotion review, or a closure verdict. Only this file is authored by this worker. Parent owns integration and verification; no gate, build, lint, test, self-test, formatter, commit, push, or live-crash reproduction was run.

## Observations and proposed axes

- **Protocol-soundness (the one move):** give every lane category an explicit, owner-resolvable registry home, make Registry and Delivery agree, and register the existing protocol closure gate without creating a root skill. Evidence: `MISSION.md:9-29`; `PROTOCOL.md:382-402,444-450`; `SCORECARD.md:93-105,132-138`; rerun `context.md:2-10`.
- **Gate-integrity (held constraint, not a second move):** preserve the executable, pinned inputs, expected verdicts, history, ownership, and distinction between registration and conformance. No implementation repair is authorized. Evidence: `PROTOCOL.md:361-381,388-404`; rerun `context.md:5-13`.
- **Fresh baseline, not a new measurement by this worker:** rerun `before.json:4-13` records commit `99efc52b3a6f3648f7d8e097d78460901ad3c91c`, command `python3 -c` with the literal script at line 9, return code 0, stdout `protocol_registered_closure_gates=0\nroot_SKILL_exists=False\n`, and empty stderr. Its counter is deliberately scoped to the protocol portion before `## Aggregator lane`; it is not a fleet-wide gate inventory or a conformance counter.
- **Concrete contradiction:** Registry currently sends every lane to its `SKILL.md` (`PROTOCOL.md:382-387`); Delivery independently requires the same path before calling a gate conformant (`399-402`). Protocol and aggregator are main-repo roles (`MISSION.md:21-22`), root `SKILL.md` is absent according to the fresh baseline, and both already share root `SCORECARD.md` through lane ownership (`PROTOCOL.md:449-450`; `SCORECARD.md:132-138`). Fixing only Registry would leave Delivery impossible.
- **Last-known-good bounded measurement:** `SCORECARD.md:15-20,85-90` describes two round-15 frozen instants, not a current live verdict. Their committed expected files independently contain pre exit 1 with 17 debt triples and post exit 0 with no debt. Both pin six inputs. The scorecard's historical self-test tally is a recorded claim, not an execution performed here.

## One source-grounded data walk: protocol closure-check

1. **Identity → owner.** Start with roster/mission role `protocol`, not the folder basename, script location, or the lane whose report happens to be under inspection. `MISSION.md:21` assigns protocol to the fleet root; `PROTOCOL.md:191-208` makes that role integrator of record and names committed closure checking. `.ufo/waves/round-15/closure-check.py:2,95-97` identifies the existing executable and the two main-repo lane roles. No new gate is needed.
2. **Owner → home.** Under the proposed amended rule, resolve `protocol` to its explicitly lane-owned registry subsection in root `SCORECARD.md`, wholly before `## Aggregator lane`. A proposed heading is `### Gate registry — protocol lane`; the exact heading is an executor choice, but ownership and placement are acceptance conditions. This is the canonical row, not a pointer to an absent root skill and not a copy in `.ufo/reports/AGGREGATE.md`. The rerun contract supplies this destination; it is not yet established by the source text inspected above.
3. **Home → callable interface.** Record the existing script with an explicit fleet-root working-directory convention. `closure-check.py:1984-2006` supports `--repo`, `--json`, `--selftest`, and qualified `--frozen`. `MAIN_LANES` and `lane_repo()` (`95-97,707-710`) explain why a main-repo role does not imply a `protocol-shokunin/` child path. Registry commands must remain usable from the documented cwd, with no reliance on a worker's session path.
4. **Interface → persisted expectations.** `do_selftest()` reads committed fixtures under `fixtures/closure-sample/` (`1850-1900`). `do_frozen()` resolves the chosen snapshot and reads its `expected.json` (`1783-1825`); `_compare_baseline()` compares exit and canonical `(lane, lane_round, class)` debt triples (`1828-1847`). Qualified names select the intended wave; bare-name ambiguity fails closed (`HELP_EPILOG:171-173`, Registry:386-387).
5. **Persisted expectations → bounded evidence.** The pre file `.ufo/waves/round-15/frozen/r15-pre-003400/expected.json:2-97` names 17 debt triples, exit 1, and hashes for `CLOSED_AT.txt`, `MANIFEST.json`, `prompts-index.txt`, `reports-index.txt`, `state-counters.txt`, and `watchdog.log`. The post counterpart `r15-post-012710/expected.json:2-10` pins the same input names, exit 0, and an empty debt set. A successful replay must compare both expected verdict and exact debt set with input digests matching; the pre's intentional nonzero verdict is not a failed replay. This says nothing about today's live ledger.

### Minimal eight-field registration skeleton

Proposed row contents, not an assertion that the row has landed:

| Field | Value / condition |
|---|---|
| name | `closure-check` |
| kind | `gate` — the existing verdict-producing script; this is registration, not certification |
| entry command | From fleet root: `python3 .ufo/waves/round-15/closure-check.py --repo .` (documented live entry; do **not** run in this move because of the known crash) |
| verdict map | `0 → clean`; `1 → failed` (gate-native debt/contradiction); `2 → could-not-evaluate`; `3 → could-not-evaluate` (gate-native no-baseline). Unexpected/unmapped nonzero results remain could-not-evaluate under the outer contract. |
| self-test command / spelling | `python3 .ufo/waves/round-15/closure-check.py --selftest`; spelling `--selftest`, not `--self-test` |
| pinned-value path | `.ufo/waves/round-15/fixtures/closure-sample/*/expected.json`; `.ufo/waves/round-15/frozen/r15-pre-003400/expected.json`; `.ufo/waves/round-15/frozen/r15-post-012710/expected.json` |
| write scope | Read-only inputs; stdout/stderr output only as declared by script lines 7-20,77. A caller's capture file belongs under this rerun directory; registering the script grants no ledger/history/runtime write authority. |
| owner | `protocol` lane, fleet-root registry subsection; not aggregator, host runtime, or whichever child is being graded |

Source for the exit map: script `64-75,90-93`; source for outer normalization: `PROTOCOL.md:364-368`. The TypeError traceback's OS exit 1 is not the script's structured debt verdict: there was no stdout verdict. Never convert that crash into a clean run, a normal failed gate result, or derived lane statuses.

## Generalization: all homes and ownership boundaries

| Case | Canonical home after the proposed cutover | Ownership / verification condition |
|---|---|---|
| Protocol main-repo lane | Root `SCORECARD.md`, explicitly protocol-owned registry subsection before `## Aggregator lane` | Protocol owns its rows; command and pins are fleet-root-relative. Only the registry executor inserts this subsection; parent owns score changes. |
| Aggregator main-repo lane | Root `SCORECARD.md`, inside its explicitly aggregator-owned section | Same schema and Delivery eligibility rule, but no protocol ownership over its rows. Preserve the complete existing aggregator section byte-for-byte in this move. Generalize the rule now; do not invent, migrate, or add aggregator inventory now. |
| Any child lane | Its own `<lane>-shokunin/SKILL.md` | Child remains the sole gate-row owner. Commands/pins resolve in that owning repo's documented cwd. A missing child skill is a missing required registry home, **not** permission to fall back to root scorecard. No child migration in this move. |
| Unknown identity / wrong section / unowned row | No valid fallback | A protocol-owned script placed in the aggregator section, a child row placed in root scorecard, or a row with no identifiable owner does not satisfy registration. Shared filesystem cwd never merges lane identity. |
| Root skill absent, or a root skill later appears | Main-repo homes remain their lane-owned scorecard sections | This is an identity-based rule, not a runtime `if SKILL exists` fallback. Do not manufacture root `SKILL.md`, `SHONEN.md`, or `PROVINCE.md`. |
| Tool that cannot fail | Same owner's declared registry home, classified `probe` | Do not advertise a probe as a conformant gate. Retain honest capability/unsupported-field descriptions; no fabricated self-test or baseline evidence. |
| Fleet index / aggregator ledger | Index may point to canonical owner rows; ledger remains defect queue | Neither becomes a second gate inventory or copied expected-value store. Defects may route through the queue without transferring ownership. |

Aggregator concrete illustration: `.ufo/waves/aggregator-r11/cross-lane-gate.expected.json:2-9` declares owner `aggregator`, entry `node .ufo/waves/aggregator-r11/cross-lane-gate.mjs --all`, and selftest spelling `--selftest`. Under the general rule, its eventual row belongs in the aggregator's root scorecard section, not in the new protocol subsection and not in the ledger. These fields are inspected declarations, not a current execution or conformance finding.

The home rule grants only row placement. Existing invariants still control every other write. In particular, aggregator's child-corpus exception (`PROTOCOL.md:310-325`) does not permit child `SKILL.md` registry edits, and child gates cannot publish, approve vault work, alter driver state, or define host stop conditions (`388-392,444-468`). Host routing is unchanged; mission taxonomy selects already configured routes, never model selectors.

## Ordered minimal acceptance skeleton and evidence gates

1. **Repair the two contradictory clauses together.** Registry defines the eight-field schema plus child/main-repo destination split; Delivery references that declared lane-owned home, not unconditional `SKILL.md`. Preserve the self-test, frozen-digest, verdict, scope, and closure-consequence obligations. Append the motivating incident to `PROTOCOL-APPENDIX.md` with rerun baseline evidence. Evidence gate: semantic inspection of both clauses and their incident pointer; root `MISSION.md`/`AXES.md` remain binding. Archived literal/source-text checks are not behavioral authority; flag overfit rather than re-pin obsolete wording.
2. **Register just the representative gate.** Insert one complete `closure-check` row in the new protocol subsection before the aggregator boundary. Evidence gate: the same protocol-scoped counting method stored in rerun `before.json` must report one rather than zero on the integrated revision; root `SKILL.md` remains absent; each of the eight fields resolves to the script or committed expectations above. Do not count the markdown header or prose as a gate row.
3. **Check every home branch without migrating other owners.** Walk the ownership table above against Registry and Delivery. Evidence gate: neither clause strands aggregator at root `SKILL.md`, relocates children, makes the ledger an inventory, or turns shared root ownership into cross-lane editing rights. Hash all bytes from the existing `## Aggregator lane` heading through EOF, not just a selected table. Rerun `before.json:21` records expected SHA-256 `7abc0478efcb16d0d2e4bbe57271d52c00da08a8eb33bc76edc272ae5b5cfccf` for that protected section.
4. **Parent-only bounded executable evidence, once after integration.** Proposed commands (not executed here):
   - `python3 .ufo/waves/round-15/closure-check.py --selftest --json`
   - `python3 .ufo/waves/round-15/closure-check.py --repo . --frozen round-15/r15-pre-003400 --json`
   - `python3 .ufo/waves/round-15/closure-check.py --repo . --frozen round-15/r15-post-012710 --json`
   Capture command, measured revision, stdout, stderr, and actual exit under `registry-home-rerun/`. Required frozen outcomes: both `baseline_inputs.status=match` with six files and `baseline.status=match`; pre exit 1 with the exact 17 expected triples, post exit 0 with the empty expected set. Treat an exception, missing output, changed expectations, unpinned inputs, or a missing baseline as failure of that evidence gate, not a reason to alter the executable or pins here. Self-test must report what actually ran, not inherit a historical tally. No live command is authorized by this skeleton.
5. **Parent-only preservation and honest record.** Compare protected artifacts to rerun `before.json:14-21`, while treating the filed round-14 report specially: its old bytes stay an exact prefix and only a post-commit erratum may extend it. Preserve all inherited `registry-home/` artifacts. Record registration separately from observed frozen replay/selftest results; record no writable closure statuses and route the known live defect. Evidence gate: revision-qualified measurements, append-only LOG/report handling, no MANIFEST/history repair, and no root promotion-file invention. Workers in this batch are not non-author promotion verifiers.

## Registration is necessary, not sufficient for conformance

The cutover's narrow acceptance is **a coherent home rule plus one complete owner-resolvable registration**. Gate conformance additionally depends on the unchanged Gate standard: executable verdict semantics; isolated self-invocation asserting exits and stable expected finding identifiers; independent committed expectations; snapshot pinning; revision-qualified measured evidence; permitted scope; and closure handling. A registry count of one or a green selftest cannot establish all of these.

A specific static caution is already visible: `closure-check.py:1880-1900` compares selected numeric counts and exit codes in fixture selftest mode; e.g. `fixtures/closure-sample/counter-deleted-dispatch-only/expected.json` expects one `unrowed_terminated` count, while `ok/expected.json` expects zero debt. This loop does not compare a stable expected finding-id as demanded by `PROTOCOL.md:369-373`. Frozen replay separately compares exact debt triples (`1828-1847`), but that is not proof that the required self-invocation assertion is satisfied. Do not silently weaken the clause, label counts as IDs, or repair the gate in this move. Any blanket conformance claim requires a separate, source-grounded resolution of this gap; registration can be truthful without that claim.

## Precise falsifiers

**Against the proposed protocol-soundness improvement:**

- Either Registry or Delivery still demands root `SKILL.md` for protocol/aggregator, or resolves them to different homes.
- The new row is outside the protocol-owned portion, any required field is absent/nonresolving, its owner differs from protocol, its commands rely on an unspecified cwd, or the protocol-scoped row count is not exactly one.
- The rule moves child registries to root, chooses homes by file existence rather than lane identity, creates a fake root craft/promotion file, copies gate inventory/expected values into the aggregator ledger, or permits unowned/ambiguous fallback rows.
- Registration is presented as gate conformance, the known crash is presented as a structured verdict, or historical snapshot output is represented as a current live result.

**Against holding gate-integrity:**

- Protected executable or expected baseline bytes change; a frozen input is edited/re-pinned; history pin or historical ledger is repaired to make this round look clean; or evidence is written into inherited `registry-home/`.
- Either frozen replay lacks matched input digests and exact expected debt/exit, but is described as matching. In particular, accepting pre exit 0, post debt greater than zero, or a no-baseline/tampered run as clean changes the meaning of the historical evidence.
- The complete aggregator suffix changes, filed report bytes are rewritten instead of retained as a prefix, or scope expands into scripts, runtime, routing, domain trees, or sibling repos.
- Gate redness or a process traceback is used to rewrite lane terminal status outside the existing marker/round rules, or the registry is made a host judge/stop-condition override.

## Blockers and unverified assumptions

- **Known blocker to live-derived closure:** rerun `context.md:7` is authoritative: inherited `registry-home/live-closure.json` records a TypeError comparing `NoneType` and `int` with historical `round:null`. Static source `closure-check.py:1143` and the inherited traceback agree on the sort site. The historical capture records exit 1, empty stdout, and no closure verdict/statuses. It is read-only failure evidence from an earlier dispatch, not this worker's run. Do not reproduce or fix it here. This blocks claiming live-clean closure, not the registry-home correction.
- **Known obstacle to blanket gate conformance:** the selftest count-versus-finding-id distinction above. Route separately; do not broaden this registry-home improvement.
- **Unverified assumptions:** the parent will integrate on a named revision without unrelated owner edits; protected bytes still match when the parent checks them; and the proposed bounded replays will match. None is established by this review. No resume-continuity proof or inherited worker authority is claimed; this review uses the fresh rerun assignment and baseline, not prior planner/critic recommendations.
- No missing prerequisite prevents this bounded design deliverable. The parent must supply actual integrated-revision verification evidence before making any acceptance or conformance judgment.
