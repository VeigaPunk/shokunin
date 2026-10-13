# DistillerSeat — queue-key integrity and harvest

Measurement stamp: 2026-09-29 (session); main repository HEAD observed immediately before measurement: `git log -1 --format='%h %aI'` (parent supplied current main `62fdfbe`). Child stamps from the required immediate sweep: `kasegi b7180b0 dirty=7`, `kumitate e0e5de1 dirty=8`, `kake a209441 dirty=0`, `kotoba 63ceba7 dirty=0`, `kengaku f09ff1f dirty=1`, `kagi 4391b3b dirty=21`. Per the moving-tree rule, this evidence uses landed HEADs where a verdict is needed; dirty-tree-only effects are provisional and are not used to mint a key.

## Key integrity

The canonical extraction was run with Python (avoids host `grep -oE`):

```sh
python3 - <<'PY'
import re,collections
p='.ufo/reports/AGGREGATE.md'; rows=[]
for n,l in enumerate(open(p),1):
 m=re.match(r'\|\s*(D-(\d+(?:/D-\d+)*))\s*\|\s*(.*)',l)
 if m: rows.append((n,re.findall(r'D-\d+',m.group(1)),m.group(3).strip()))
by=collections.defaultdict(list)
for n,ks,t in rows:
 for k in ks: by[k].append((n,t))
keys=sorted(by,key=lambda x:int(x[2:]))
print('rows',len(rows)); print('distinct',len(keys)); print('max',keys[-1])
print('next',f'D-{max(map(lambda x:int(x[2:]),keys))+1:02d}')
for k,v in by.items():
 if len(v)>1 and len({t for _,t in v})>1: print('collision',k,v)
print('duplicate-key-groups',sum(1 for v in by.values() if len(v)>1))
PY
```
Observed output: `rows 116`, `distinct 118`, `max D-120`, `next D-121`, no `collision` lines, `duplicate-key-groups 0`. A second independent count is the ledger's row-key set cardinality: `python3 -c "import re; s=open('.ufo/reports/AGGREGATE.md').read(); print(len(set(re.findall(r'\\bD-\\d+\\b',s))))"` (must be interpreted as all references, not definitions; therefore not used for the definition count).

The earlier refresh's `84 / D-87` is reproduced as historical text at `AGGREGATE.md:1083`; current definitions extend through D-120. The two prior duplicate folds still hold exactly as recorded at `AGGREGATE.md:1230-1231`: **D-39 ⊇ D-85** (endpoint-repoint label/correction rider) and **D-51 ⊇ D-84** (cite-check gate reading auditor-owned lesson). No additional duplicate-key group exists; semantic duplicate candidates harvested below are explicitly marked against their existing key rather than minted.

Standing contradictions re-tested from the ledger: (1) D-59 says kumitate's card prints kagi self-test 11 cases while D-10's re-executed proof says 13 (`AGGREGATE.md:1232`); (2) D-68's row says 11/76 while the re-test says 11/77 and identifies the list-concatenation wording hazard (`:1240`); (3) D-75(a)'s older “rounds stuck at 15” statement is contradicted by the re-test of `MANIFEST.json` showing 22 entries (`:1234`). These are standing contradictions, not resolved by choosing a side.

## Harvested candidate rows

Sweep sources read: `.ufo/reports/round-12/{kumitate,kagi,kotoba,kake}.md`, `.ufo/reports/round-13/{kake,kasegi,kotoba}.md`, `.ufo/reports/round-14/kasegi.md`, untracked `.ufo/reports/round-12/{kagi,kotoba}.md`, and `git show dddb4ec -- PROTOCOL.md`. The requested `round-11/kengaku-DRAFT.md` is absent at this sweep; the durable successor is discussed in protocol r12 at `round-12/protocol.md:238-240`.

| Proposed key | owner | sev | claim | evidence | command | duplicate / disposition |
|---|---:|---:|---|---|---|---|
| D-121 | kake | 4 | Scribe push gate failed for the last three ledger beats: `pushed:false`, pull timeout, and `grok-web empty or ceiling response`; pushes are stalled. | round-12/kake.md:80-86 | `python3`/read of the cited ledger plus `awk` over the report; source report names three timestamps and statuses | No matching D-key found by Python substring sweep; new candidate. |
| D-122 | kake | 4 | `grokbots --check` checks registry-row existence but never checks wrapper presence (`botWrapperPath` is unused), leaving a wrapper-missing blind spot. | round-12/kake.md:92-95 | `grep`-equivalent structural sweep: report citation `cli.mjs:354-391,427`; verify with `git show`/read of cited source | New claim, not a ledger row; distinct from D-100's lucario canonical-row defect. |
| D-123 | kasegi | 4 | Two DONE packages remain unfiled and the operator queue is stale: 11 rows on disk versus 12 after live regeneration. | round-14/kasegi.md:114-117 | `python3`/`find` over the package and queue sources, then compare counts; report supplies package names | No matching D-key found; new candidate. |
| D-124 | kotoba | 3 | Sibling trigger gap remains: 0/5 sibling SKILL descriptions carry a quoted trigger or arbitration clause; prior drop-in rewrites are unapplied. | round-12/kotoba.md:153-157 | `python3` sweep of sibling `SKILL.md` descriptions for trigger/arbitration text; report states measured 0/5 | No matching D-key found; new candidate. |
| D-125 | kagi | 4 | `transcript-scan.sh` has no in-gate pin; expected values live only in an external claim ledger, and default mode returns `HITS=2`. | round-12/protocol.md:292-294 (routing); round-12/kagi.md:209-211 | `bash corpus/transcript-scan.sh` plus `git grep` for its pin/claim-ledger reference | Semantic overlap with D-104 (same HITS=2 baseline defect); do not mint as independent key — duplicate D-104. |
| D-126 | protocol | 4 | Gate standard requires every gate to have a committed fixture self-test asserting exit code + stable finding-id and a committed-snapshot run naming the measured revision; model-only self-tests are non-conforming. | `git show dddb4ec:PROTOCOL.md` Gate standard, diff hunk; round-12/protocol.md:134-149 | `git show dddb4ec -- PROTOCOL.md` (observed 77-line change, §Gate standard added) | Normative protocol change, not a defect row by itself; route only concrete lane failures (D-103 already covers kotoba's model-only self-test). |
| D-127 | kasegi | 3 | Vanished `~/Projects/bounties` root leaves the province path and roughly 376 SKILL citations needing correction/disposition. | round-12/protocol.md:278-280; context fleet event | `test -e ~/Projects/bounties; python3` citation census | Duplicate/continuation of existing D-76 / fleet vanished-tree ruling; do not mint. |

The untracked round-12 kagi/kotoba reports are real sweep inputs (`git status --porcelain` showed `??` for both); their unlanded status is already ledgered by D-91 and the kagi unlanded-report routing. The missing `kengaku-DRAFT.md` is not harvested as a fresh defect because protocol r12 records that it was superseded by the landed `round-11/kengaku.md`.

## Proposed numbering and open-owner tally

Proposed keys are assigned from the measured next-free key (`D-121`) in owner order, while duplicate/non-defect rows are retained in the table for auditability and explicitly not minted. If only genuinely new defect rows are minted, D-121–D-124 are the four candidates; D-125–D-127 are duplicate/routing/non-row items. The refresh-6 pre-new-row tally remains **46 open rows / 12 owners**, with the exact ledger-stated breakdown at `AGGREGATE.md:1450-1452`: kasegi 12, protocol 10, kumitate 9, kake 8, kengaku 8, operator 7, kagi 6, fleet 4, external 3, aggregator 2, integrator 1, kotoba 1. This is the available recomputed owner tally in the current ledger; the 24 rows subsequently filed in refresh 6 are not silently added to that historical “before new rows” denominator.

Aggregator-owned open debt is explicit and must not be re-keyed: **D-81 is OPEN** (the kagi ref-shape sweep changed from 0 to 1 and owes an append-only annotation); D-106 is CLOSED and D-117 is CLOSED. D-88's root cause is operator-side and D-120's practice residue is addressed in the addendum. This lane must not silently rename D-81. The report/commit-order debt is also represented by D-88/D-119's aggregator-side consequence; §13.5 records the aggregator's report-before-commit defect and §13.7 says it is routed, not erased.

All numbers in this file are accompanied by the commands or source locations above; worktree-only child changes are provisional under the stamped revisions and were not used to close or mint rows.

## Rule-8 literal-text amendment

Per the L1 amendment, I ran the landed-HEAD sweep `for d in kasegi-shokunin kumitate-shokunin kake-shokunin kotoba-shokunin kengaku-shokunin kagi-shokunin; do printf '%s ' "$d"; git -C "$d" grep -n 'op://' HEAD -- corpus/ 2>/dev/null | wc -l; done`. Observed counts: kasegi **2**, kumitate **1**, kake **2**, kotoba **3**, kengaku **1**, kagi **53**. This agrees with SentinelSeat's counts after lane-order normalization (2/1/2/1/3/55 differs only because Sentinel's kagi sweep included two additional worktree/unlanded hits; landed HEAD is the authoritative cell here). The file:line classification and literal rule-8 grade require the full `git grep -n` listing; no secret values are reproduced. This is a routed operator/integrator amendment candidate: literal `op://` text may be schematic, but rule 8 as written does not distinguish schematic placeholders from real vault paths, so schematic-only corpora are **FAIL-literal / PASS-intent** pending amendment; any resolvable real-vault path is literal FAIL.
