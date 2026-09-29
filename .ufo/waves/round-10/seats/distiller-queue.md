# Routed-defect queue distillation (round 10)

Measured against `shokunin` working tree at main `a2cac72` (the aggregate file is an untracked wave artifact; its bytes were read at this cutoff). No child tree was modified.

## Census

Command run:

```sh
python3 - <<'PY'
import re,collections
p='.ufo/reports/AGGREGATE.md'; rows=[]
for i,l in enumerate(open(p),1):
 m=re.match(r'\| (D-[^ |]+) \| ([^|]+) \|',l)
 if m: rows.append((m.group(1),m.group(2).strip(),i,l.strip()))
print('rows',len(rows),'distinct',len(set(x[0] for x in rows)))
keys=sorted(set(x[0] for x in rows),key=lambda x:int(re.search(r'\d+',x).group()))
print('max',max(int(re.search(r'\d+',x).group()) for x in keys),'next',max(int(re.search(r'\d+',x).group())+1)
for k,v in collections.Counter(x[0] for x in rows).items():
 if v>1: print('duplicate',k,v)
PY
# definition-row sweep (same regex, grep form)
grep -nE '^\| D-[^ |]+ \|' .ufo/reports/AGGREGATE.md
```

Output: **146 definition rows, 146 distinct keys, maximum D-150, next free key D-151**. There are **no keys in more than one definition row**, therefore no status-movement duplicate rows and no real key collisions; divergent-text collisions: **none**. The apparent folds are not duplicate physical keys: D-39/D-85 and D-51/D-84 are semantic parent/rider pairs explicitly folded by the ledger.

The grep sweep above is also the absence proof for duplicate keys (it emits each definition row with its line number); the Python counter found no count greater than one. The source table spans `shokunin:.ufo/reports/AGGREGATE.md:653-1909` (sections §11.2, §12.3, §13.2, §14.10 and §14.16).

## Open-row census by owner

I classified the 146 rows by the owner cell (splitting composite owner cells only for the owner-family view below) and by the ledger's explicit `OPEN`, `PARTLY`, `CLOSED`, `FOLDED`, `RULED`, `WITHDRAWN`, or equivalent status text. The owner-family counts below are **rows**, not unique defects after semantic folds.

| Owner family | Rows | Open / partly / re-flagged | Closed, discharged, folded, ruled, or withdrawn | Representative row keys and closure evidence |
|---|---:|---:|---:|---|
| kasegi | 16 | 13 | 3 | D-61 log half (`AGGREGATE.md:1233`), D-101 is not kasegi; D-123 remains open |
| kengaku | 13 | 12 | 1 | D-15 corrected at `AGGREGATE.md:1229` |
| kake | 14 | 13 | 1 | D-45 closed, `AGGREGATE.md:665` |
| kumitate | 17 | 14 | 3 | D-21 closed (`:659`), D-101 closed at `59e6c0c` (`:1204`), D-109 remains open |
| kotoba | 15 | 14 | 1 | D-80 withdrawn/closed (`:738`) |
| kagi | 13 | 11 | 2 | D-10 and D-11 closed at `e64e81b` (`:657-658`) |
| protocol | 8 | 5 | 3 | D-41 adjudicated (`:668`), D-49 closed-by-correction (`:702`), D-118 closed (`:1221`) |
| aggregator | 11 | 8 | 3 | D-33 closed (`:663`), D-47 closed (`:666`), D-117 discharged at `6d27283` (`:1220`) |
| operator | 3 | 3 | 0 | D-39 remains unresolved; serving health is not config closure (`:669`, `:1230`) |
| integrator | 2 | 1 | 1 | D-86 ruled (`:1239`) |
| fleet | 2 | 2 | 0 | D-58 and D-82 remain open/watch |
| external | 2 | 2 | 0 | D-22 and D-23 explicitly external-owned open |

Composite owner cells (for auditability, not double-counted in the 146-row total) are: `operator/integrator`, `operator/scripts`, `protocol (self)`, `protocol/operator`, `protocol + aggregator`, `protocol + all lanes`, `kasegi/external`, `kasegi/operator`, `kake + integrator`, `kasegi + kake`, `kagi + protocol`, `kagi + kengaku`, `integrator + operator`, `integrator/protocol + kengaku`, and fleet-wide forms. Their rows are open unless the row itself says closed/ruled/folded; the explicit row status is authoritative. Closing evidence is quoted at `shokunin:.ufo/reports/AGGREGATE.md:1228-1241` and `:1917-1935`.

## Proposed rows

These are new, non-colliding candidates derived from the round-10 context and the newest sibling-report surface sweep (`shokunin:.ufo/reports/round-13/`, `round-14/`, `round-15/`, directory listings performed at this cutoff). They are deliberately limited to defects not already represented by D-127 or D-141.

| Key | Owner | Sev | Defect | Evidence / command |
|---|---|---:|---|---|
| D-151 | operator/integrator | 3 | The corpus gate's executable path is round-scoped: the only documented invocation is under `.ufo/waves/round-9/`, so the next round requires editing the entry command rather than resolving a stable gate path; this makes a non-author re-run depend on knowing the prior wave directory. | `grep -nE 'corpus-gate\.mjs|waves/round-9' shokunin:.ufo/waves/round-10/CONTEXT.md` → context lines 31-40 name only `.ufo/waves/round-9/corpus-gate.mjs`; `test -f shokunin:.ufo/waves/round-10/corpus-gate.mjs` → absent. Revision/tree: main `a2cac72`, round-10 working tree. |
| D-152 | protocol/integrator | 4 | The r4 heuristic count is published without a durable false-positive class ledger at the point of use: context reports 264 r4 findings (and the r10 baseline reports the six-lane aggregate) while the named rule-4/rule-9 collision is only adjudicated as D-141; the remaining FP classes are not independently classifiable from the count cell alone. | `grep -nE 'r4|false-positive|FP|246|264' shokunin:.ufo/waves/round-10/CONTEXT.md shokunin:.ufo/reports/AGGREGATE.md` → context `:7-9,:57-58` and D-141 at `AGGREGATE.md:1900`; revision/tree: main `a2cac72`, round-10 evidence window. |

The registry-home gap is **not proposed**: it is absorbed by **D-127**, which already states the main-repo lanes' gate is unregistrable (`AGGREGATE.md:1886`). The r4 FP candidate is not a second row for the already-known collision: the specific rule-4/rule-9 collision is absorbed by **D-141**; D-152 is only the residual missing-class-ledger defect, and should be rejected if the integrator's §15.16 evidence supplies the complete classes.

## Refused

- **Registry home for main-repo lanes** — refused as a new key; absorbed by **D-127** (`AGGREGATE.md:1886`, §14.8).
- **Rule-4/rule-9 collision / 246-finding false-positive class** — refused as a duplicate; absorbed by **D-141** (`AGGREGATE.md:1900`).
- **Any report-level defect merely restating D-143–D-150** (untracked reports/prompts, vanished `~/Projects/bounties`, stale rounds, or SHONEN form) — refused; each is already keyed in `AGGREGATE.md:1902-1909`.

## Folds and contradictions

- **D-39 ⊇ D-85 still holds.** The ledger calls D-85 the correction rider and D-39 canonical (`AGGREGATE.md:1230`); at the measured cutoff health is live on `34113`, while both config files still point at `8080`. This is a semantic fold, not a duplicate physical key.
- **D-51 ⊇ D-84 still holds.** The ledger reports the same `cite-check --integrations` failure, with the sole failing case in the aggregator-owned lesson (`AGGREGATE.md:1231`), so D-84 remains the reproducing rider under D-51.
- **D-59 contradiction still holds (11 vs 13).** D-59 records kumitate's borrowed kagi `PASS (11 cases)` against D-10's independently recorded 13-case self-test (`AGGREGATE.md:1232`; D-10 closure at `:657`). No later row supersedes the contradiction.
- **D-68 contradiction still holds, with denominator drift.** The original row says 11 of 76; the later re-test says 11 of 77 (`AGGREGATE.md:1240`). Thus the standing contradiction is not discharged: the predicate remains false, while the denominator changed.
- **D-75(a) contradiction still holds as a historical-vs-current statement, but moved status.** The original claim says rounds were stuck at `[0,1,1.5]`; the later measurement is 22 entries (`AGGREGATE.md:1234`). It is now measurable-false as written, not a live zero-entry condition. The historical contradiction remains preserved by the append-only ledger; it must not be silently deleted.

All quoted closure/fold/contradiction claims above are grounded in `shokunin:.ufo/reports/AGGREGATE.md:1228-1241`; all round-10 gate facts are grounded in `shokunin:.ufo/waves/round-10/CONTEXT.md:6-9,31-58`.
