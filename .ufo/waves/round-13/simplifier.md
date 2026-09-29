# Round-13 YAGNI audit: `PROTOCOL.md`

## Axes and method

Axes: **protocol soundness** (remove no obligation) and **gate integrity** (retain
machine-checkable closure meaning). This is an audit, not an edit. All counts below
were run from `/home/vgpnk/projects/shokunin` on 2026-09-28.

## 1. Deletable-with-zero-loss candidates (ranked)

These are conservative candidates: deletion removes explanation or an exact
restatement, not the operative rule. “Falsifier” is the cheap test that would reject
the cut before landing it.

| rank / saving | quoted span and lines | why behaviour survives | falsifier |
|---|---|---|---|
| 1 / 40 lines | `## Appendix — incident digest (why these rules exist)` through the final incident row, `PROTOCOL.md:487-526`; quote: “One line per dated incident or measurement motivating a rule above” | The body sections already state the rules; the appendix is explicitly a motivation digest, not a new MUST/REQUIRED clause. Search command `grep -nE 'MUST|REQUIRED|SHOULD|NEVER|AVOID|may not|must not' PROTOCOL.md:487-526` has no normative keyword output (observed: no output). | Any report or checker cites an appendix row as the sole source of an obligation, or removing it makes the round-11 census lose a required predicate. Run `grep -Rni 'Appendix\|incident digest\|Lands last\|Gate standard' .ufo/reports/round-*/ .ufo/waves/round-1*/ *-shokunin` and `bash .ufo/waves/round-11/verify-census.sh`; either nonzero citation evidence or a census failure rejects the cut. |
| 2 / 8 lines | `PROTOCOL.md:371-374`: “**Scope.** Read-only over surfaces it does not own … never stands in for the native judge.” | The same local-first and operator-owned restriction is already stated in **Invariants**, quoted at `PROTOCOL.md:442-449` (“domain-facing actions are operator-owned” and domain source trees are read-only). The gate's scope is still retained as a short registry obligation; only this explanation is cut. | A gate-owning lane report cites §Gate standard §Scope rather than **Invariants** as the authority, or a checker/reviewer treats a gate verdict as a host stop condition. Search `grep -RniE 'Gate standard.*Scope|native judge|driver mutation' .ufo/reports/round-*/ .ufo/waves/round-1*/ *-shokunin`; a unique operational citation means retain it. |
| 3 / 7 lines | `PROTOCOL.md:348-351` plus the final sentence at `PROTOCOL.md:356`: “A gate is a committed, re-runnable verdict script…” and “so no working gate breaks on adoption.” | The registry row and closure evidence rules define the consumed interface; `closure-check.py` parses closure evidence and frozen results, while each lane owns the executable. Keep the one-line gate/probe definition, cut only the adoption rationale. | A gate is accepted by closure despite lacking a committed rerunnable command, or a probe is accepted without a failure path. Run the gate's self-test and frozen command for each registry row plus `python3 .ufo/waves/round-12/closure-check.py --no-citations`; any acceptance unsupported by the retained definition falsifies the cut. |
| 4 / 5 lines | `PROTOCOL.md:14-17`: “two documented unplaceable demand instances … or an explicit operator directive — the mint bar, stated once here; closure step 3 applies it.” | Step 3 at `PROTOCOL.md:217-219` explicitly says minting occurs only for an unserved domain and gives the Lifecycle mint bar. Removing the earlier parenthetical leaves Lifecycle as the sole authority and eliminates the self-reference. | A mint review or census finds the two-instance/operator-directive threshold only at lines 14-17, not at Lifecycle/step 3. Run `grep -RniE 'unplaceable|explicit operator directive|mint bar' .ufo/reports/round-*/ .ufo/waves/round-1*/ *-shokunin`; a sole external citation to the removed span rejects the cut. |

**Mechanical boundary.** `closure-check.py` does enforce structural status vocabulary,
entry-keyed ledger/debt classification, report/marker checks, hash and attribution
checks, SHONEN-heading presence, dispatch/termination evidence, and frozen-result
comparison. It does *not* enforce prose such as the gate definition, local-first
scope, mint threshold, or the reason appendix rows exist. Therefore mechanical
coverage justifies deleting explanations, never deleting the corresponding rule.
The source points are `closure-check.py:57-75` (status/marker regexes), `:350-446`
(ledger), `:702-1060` (analysis), and `:1329-1366` (frozen comparison); command:
`grep -nE 'STATUSES|RE_SHONEN|RE_PLACEHOLDER|def build_ledger|def analyze|def do_frozen|def _compare_baseline' .ufo/waves/round-12/closure-check.py` observed output:
`57:STATUSES`, `74:RE_SHONEN`, `75:RE_PLACEHOLDER`, `350:def build_ledger`, `702:def analyze`, `1329:def do_frozen`, `1354:def _compare_baseline`.

## 2. Clauses with no observable consumer

Reproducible heading sweep (reports, aggregate, round-1* waves, and all eight
`*-shokunin` paths):

```sh
roots='.ufo/reports/round-*/protocol.md .ufo/reports/AGGREGATE.md .ufo/waves/round-1*/ *-shokunin'
for s in Lifecycle 'Promotion gates' 'Round-robin rounds' 'Evidence standard' 'Gate standard' 'File contract per shokunin repo' Invariants 'Fleet-2 conventions'; do
  n=$(grep -Roh -- "## $s\|§$s\|$s" $roots 2>/dev/null | wc -l)
  printf '%s\t%s\n' "$s" "$n"
done
```
Observed output: `Lifecycle 276`, `Promotion gates 247`, `Round-robin rounds 504`,
`Evidence standard 451`, `Gate standard 631`, `File contract per shokunin repo 126`,
`Invariants 576`, `Fleet-2 conventions 135`. This pattern is intentionally broad
and counts prose mentions, not only citations; it is a reproducible upper-bound
sweep, not proof that every hit is a consumer.

Named-clause sweep for the gate registry fields:

```sh
grep -RniE 'entry command|verdict map|self-test|selftest|pinned-value|pinned value|write scope|owner' \
 .ufo/reports/round-*/protocol.md .ufo/reports/AGGREGATE.md .ufo/waves/round-1*/ *-shokunin 2>/dev/null | wc -l
```
Observed output: `5619` matches. This is not zero because ordinary domain prose
uses “gate”, “owner”, and “self-test”; it does not establish registry rows.
A stricter row-shape sweep is:

```sh
for d in kasegi kengaku kake kumitate kotoba kagi; do
  grep -Ein '^(gate|probe|entry command|verdict map|self-test command|pinned-value path|write scope|owner):|\| *(gate|probe) *\|' "$d-shokunin/SKILL.md" 2>/dev/null
 done
```
Observed output: **no lines** (zero registry-shaped rows across the six existing
child repos; the roster has six child repos plus the two main-repo lanes, whose
`SKILL.md` does not exist). Therefore the clause is a candidate for “aspirational
in current fleet”, not dead by citation count: its contract is still load-bearing
because §Gate standard: “closure grades no gate conformant until its registry row
exists”. A zero citation means “candidate for removal or compaction”, not proof of
no effect; the ruling itself is an intended consumer.

## 3. §Gate standard, re-argued on round-13 evidence

The four gate-owning lanes named by the round-12 record are kagi, kengaku, kotoba,
and kumitate. The exact row-shape command above found zero rows for all six child
repos, including those four. The broader `grep -Ein 'gate|probe' .../SKILL.md`
sweep did find ordinary craft prose (for example `kagi-shokunin/SKILL.md:42-43`
contains `--selftest` and `kengaku-shokunin/SKILL.md:405-435` describes a hermetic
grader), but none declares all registry fields. Thus the operational evidence says
**landed registry: 0**; the standard is aspirational in implementation, not
redundant in meaning.

The round-12 ruling remains load-bearing in three operative parts: (1) verdict-class
mapping, (2) naming the revision measured, and (3) closure consequence. A smallest
safe replacement is 9 lines (instead of the current 40-line section):

```text
## Gate standard
A gate is a committed, rerunnable verdict script; a non-failing tool is a probe.
Registry rows in each lane's `SKILL.md` name the command, `gate|probe`, code→
`clean|failed|could-not-evaluate` map, self-test command and spelling, pinned-value
path, write scope, and owner. Every verdict names the measured revision and gates
that read mutable fleet state provide a committed-input run with its expected
verdict. A red gate is a routed, status-neutral conformance defect unless the
round rules say `failed`; marker-versus-report grading happens first. Closure
verifies committed self-test/frozen evidence and the named revision; it does not
execute sibling gates.
```
This keeps the ruling's three operative parts and the registry schema while deleting
long rationale. It does **not** claim rows already exist; the zero-row measurement
above is exactly why closure must continue to reject unregistered gates.

## 4. Independent ≤470-line budget

Starting count command and observed output: `wc -l PROTOCOL.md` → `526 PROTOCOL.md`.
My competing budget is:

| cut | lines |
|---|---:|
| Appendix incident digest (`487-526`) | -40 |
| duplicate mint-bar parenthetical (`14-17`, retaining the lifecycle rule at step 3) | -5 |
| Gate §Scope explanation (`371-374`, retaining Invariants and the registry obligation) | -8 |
| Gate adoption rationale / repeated delivery prose (`356`, `381-384`; retain the registry requirement and closure consequence) | -7 |
| **total cut** | **-60** |
| **result** | **526 - 60 = 466** |

The resulting 466-line file is 4 lines under the 470-line ceiling. This budget is
independent of the 9-line gate rewrite proposal: if the integrator chooses the
rewrite, it has additional headroom, but it must not count that headroom twice.
Before landing any cut, rerun `.ufo/waves/round-11/verify-census.sh` and the
citation/falsifier commands above; no edit was made by this artifact.
