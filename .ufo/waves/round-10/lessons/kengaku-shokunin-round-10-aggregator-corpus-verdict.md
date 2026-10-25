# Round 10 aggregator corpus verdict — kengaku

**Path convention (`D-128` forward fix).** `shokunin:<path>` resolves in the main repo
`/home/vgpnk/projects/shokunin`; `kengaku-shokunin:<path>` resolves in this checkout
`/home/vgpnk/projects/shokunin/kengaku-shokunin`; bare `corpus/…`, `SHONEN.md`, `evidence/…` and `.ufo/…` are
relative to this checkout's root.

**Round and evidence.** This is the **round 10** (refresh 8) `CORPUS.md` rule-10 review for kengaku, and it is the
artifact whose absence the gate reports as `r10`. Evidence homes: `shokunin:.ufo/reports/round-9/aggregator.md` §14.2,
§14.4 and §14.7 (the round-9 verdict, the literal rule-8 grading, and the `SHONEN.md` census this one moves from),
`shokunin:.ufo/reports/round-10/aggregator.md` (this round's report; the L1 commits it at round close),
`shokunin:LOG.md` (round-10 lane entry), and the gate, `shokunin:.ufo/waves/round-9/corpus-gate.mjs` (id
`corpus-gate-v1`, read-only).

## 1. Revision measured

| cell | observed | command that produced it |
|---|---|---|
| live `HEAD` (short) | `e171cdf` | `git -C kengaku-shokunin rev-parse --short HEAD` |
| live `HEAD` (full) | `e171cdfbdb350ee90bfc1c66dac54106a3a5e2ca` | `git -C kengaku-shokunin rev-parse HEAD` |
| worktree dirty count | 4 | `git -C kengaku-shokunin status --porcelain \| wc -l` |
| measurement stamp (UTC) | `2026-09-29T01:51:10Z` | `date -u +%Y-%m-%dT%H:%M:%SZ` |

The live run grades the **worktree**; its identity is the revision *plus* the dirty count observed with it:

```
# tree kengaku-shokunin revision=e171cdfbdb350ee90bfc1c66dac54106a3a5e2ca (worktree) dirty=4 mode=live provisional=1 (worktree-only bytes differ from the cited revision)
# tree kengaku-shokunin revision=f09ff1fc4d9e1e106d07c02b5bf9c148579175df dirty=0 mode=snapshot
```

## 2. `CORPUS.md` rule-10 verdict

**`not conformant`** (gate exit 1). Failed rules and their finding counts, from the live run:

| failed rule | finding count | gate command (`--round 10`) |
|---|---:|---|
| r4 — a count carries its backticked command (`CORPUS.md:28`) | 25 | `node .ufo/waves/round-9/corpus-gate.mjs --repo kengaku-shokunin --round 10 --json` |
| r8 — credential material, literal text (`CORPUS.md:43`) | 3 | `node .ufo/waves/round-9/corpus-gate.mjs --repo kengaku-shokunin --round 10 --json` |
| r10 — the round's aggregator lesson is present (`CORPUS.md:21`) | 1 | `node .ufo/waves/round-9/corpus-gate.mjs --repo kengaku-shokunin --round 10 --json` |
| shonen — `PROTOCOL.md` §File contract canonical form | 1 | `node .ufo/waves/round-9/corpus-gate.mjs --repo kengaku-shokunin --round 10 --json` |

The gate's verdict line and the per-rule census the counts above come from (the census command is the `sed`/`node`
pair in §7; both were executed):

```
# verdict kengaku-shokunin failed findings=30 rules=r4,r8,r10,shonen rules-implemented=r2,r4,r7,r8,r10,shonen
CR-kengaku-shokunin-r10-1: no corpus/lessons/round-10-aggregator-*.md — the round-10 review duty has no emitted lesson (CORPUS.md:21)
{"r4":25,"r8":3,"r10":1,"shonen":1}
```

r2 and r7 emit **0 findings** here: every `lessons/` entry carries its round and an evidence pointer, and no index row
names an absent file. The r8 cell carries the gate's declared abstention — `classification=could-not-evaluate (needs a
vault read; operator-gated)` — per cell, never folded into the repo verdict.

## 3. Per-rule counts, and movement from the round-9 pinned revision

Live column: `node .ufo/waves/round-9/corpus-gate.mjs --repo kengaku-shokunin --round 10 --json`.
Before column: `node .ufo/waves/round-9/corpus-gate.mjs --snapshot kengaku-shokunin f09ff1f --round 9 --json`
(the round-9 pinned revision for this repo in `shokunin:.ufo/waves/round-10/CONTEXT.md`).

| rule | live (`e171cdf`, dirty 4) | before (`f09ff1f`, `--round 9`) | movement | live command | before command |
|---|---:|---:|---|---|---|
| r2 | 0 | 0 | flat | `node .ufo/waves/round-9/corpus-gate.mjs --repo kengaku-shokunin --round 10 --json` | `node .ufo/waves/round-9/corpus-gate.mjs --snapshot kengaku-shokunin f09ff1f --round 9 --json` |
| r4 | 25 | 25 | flat | `node .ufo/waves/round-9/corpus-gate.mjs --repo kengaku-shokunin --round 10 --json` | `node .ufo/waves/round-9/corpus-gate.mjs --snapshot kengaku-shokunin f09ff1f --round 9 --json` |
| r7 | 0 | 0 | flat | `node .ufo/waves/round-9/corpus-gate.mjs --repo kengaku-shokunin --round 10 --json` | `node .ufo/waves/round-9/corpus-gate.mjs --snapshot kengaku-shokunin f09ff1f --round 9 --json` |
| r8 | 3 | 1 | **+2** | `node .ufo/waves/round-9/corpus-gate.mjs --repo kengaku-shokunin --round 10 --json` | `node .ufo/waves/round-9/corpus-gate.mjs --snapshot kengaku-shokunin f09ff1f --round 9 --json` |
| r10 | 1 | 1 | flat (artifact — see note) | `node .ufo/waves/round-9/corpus-gate.mjs --repo kengaku-shokunin --round 10 --json` | `node .ufo/waves/round-9/corpus-gate.mjs --snapshot kengaku-shokunin f09ff1f --round 9 --json` |
| shonen | 1 | 1 | flat | `node .ufo/waves/round-9/corpus-gate.mjs --repo kengaku-shokunin --round 10 --json` | `node .ufo/waves/round-9/corpus-gate.mjs --snapshot kengaku-shokunin f09ff1f --round 9 --json` |

The before run re-derives the gate's frozen expectation
(`shokunin:.ufo/waves/round-9/corpus-gate.expected.json` `frozen["kengaku-shokunin@f09ff1f"].stats`):

```
# expect kengaku-shokunin@f09ff1f MATCH exit=1 ids=28
# verdict kengaku-shokunin failed findings=28 rules=r4,r8,r10,shonen rules-implemented=r2,r4,r7,r8,r10,shonen
```

**r10 note.** Both r10 cells are 1 but measure different duties: the live cell is *this lesson* not yet mirrored; the
before cell is the *round-9* lesson absent from the archived `f09ff1f` tree. The real movement is r8 **+2**; r2, r4,
r7 and shonen are flat.

The r8 movement is fully attributable to the round-9 verdict lesson landing after the pinned revision. Before
(`--snapshot f09ff1f --round 9`) the cell held one class and one file; live it holds three classes —
`node .ufo/waves/round-9/corpus-gate.mjs --repo kengaku-shokunin --round 10` prints:

```
CR-kengaku-shokunin-r8-1: credential-class kv-secret occurrences=1 lines=1 files=1 owner=aggregator at e171cdf(worktree) literal_shaped=0/1 :: classification=could-not-evaluate (needs a vault read; operator-gated) files=[lessons/round-9-aggregator-corpus-verdict.md] first=lessons/round-9-aggregator-corpus-verdict.md:20 first4="pass" len=17 (CORPUS.md:43)
CR-kengaku-shokunin-r8-2: credential-class kv-secret occurrences=1 lines=1 files=1 owner=lane at e171cdf(worktree) literal_shaped=0/1 :: classification=could-not-evaluate (needs a vault read; operator-gated) files=[evidence/round12-fleet/grader_r12_draft.py] first=evidence/round12-fleet/grader_r12_draft.py:2224 first4="toke" len=17 (CORPUS.md:43)
CR-kengaku-shokunin-r8-3: credential-class op-ref occurrences=5 lines=3 files=2 owner=aggregator at e171cdf(worktree) maxseg=0 :: classification=could-not-evaluate (needs a vault read; operator-gated) files=[lessons/round-5-aggregator-audit.md,lessons/round-9-aggregator-corpus-verdict.md] first=lessons/round-5-aggregator-audit.md:56 first4="op:/" len=5 (CORPUS.md:43)
```

The aggregator-owned growth sits in `kengaku-shokunin:corpus/lessons/round-9-aggregator-corpus-verdict.md` — a prior
lesson of this lane that spelled the banned scheme literal and a value-class assignment while describing its own sweep
(`node .ufo/waves/round-9/corpus-gate.mjs --repo kengaku-shokunin --round 10 --json` → 5 occurrences over 2 files).
Rule 9 forbids rewriting it; the fix is forward-only, and this lesson spells neither (§7 self-sweep). The lane-owned
`kv-secret` hit is in `kengaku-shokunin:corpus/evidence/round12-fleet/grader_r12_draft.py:2224`
(`node .ufo/waves/round-9/corpus-gate.mjs --repo kengaku-shokunin --round 10 --json`), classified
`could-not-evaluate`, not adjudicated here.

r4's 25 findings concentrate on `kengaku-shokunin:corpus/knowledge/telemetry-run-design.md` and
`kengaku-shokunin:corpus/lessons/round-5-aggregator-audit.md` with 4 each, then a tail of 1–2 per file
(`node .ufo/waves/round-9/corpus-gate.mjs --repo kengaku-shokunin --round 10 --json`). r7 is 0 findings on both sides
— the gate grades the phantom-row reading only and prints under-coverage as a note:

```
# note kengaku-shokunin r7: 8 backticked path template(s)/glob(s) skipped (contain *, <, {, ~, $ or …)
# note kengaku-shokunin r7 under-coverage (not a finding): 125/160 corpus files carry no index row
```

Hand-adjudicated round-9 verdict vs the gate-recomputable cells: `shokunin:.ufo/reports/round-9/aggregator.md` §14.2
graded kengaku `not conformant` on rules 8-literal and 10, and rules 4, 7, 9 "cleared". The gate cannot reproduce the
rules it declares not-evaluated (`r1 r3 r5 r6 r9 box-3`); its cells and that prose are complementary, not equal.

## 4. r4 adjudication

`node .ufo/waves/round-10/r4-adjudicate.mjs --live --repo kengaku-shokunin --round 10` was attempted at the stamp
above and **does not exist**: `ls -la shokunin:.ufo/waves/round-10/r4-adjudicate.mjs` → `No such file or directory`,
and the run exits 1 with `Error: Cannot find module
'/home/vgpnk/projects/shokunin/.ufo/waves/round-10/r4-adjudicate.mjs'` (`code: 'MODULE_NOT_FOUND'`). Only the raw
count is published:

**raw r4 count = 25** — `node .ufo/waves/round-9/corpus-gate.mjs --repo kengaku-shokunin --round 10 --json`

adjudication: not-run at draft time (L1 re-measures after the mirror)

No false-positive/violation split is invented. The declared false-positive classes the round-10 axis-move closes are
the three named in `shokunin:SCORECARD.md` §Planned (round 10), including the rule-4/rule-9 collision routed as
`D-141`.

## 5. Ledger rows this verdict rests on

From `shokunin:.ufo/reports/AGGREGATE.md` §14.16 (rows `D-121`…`D-150`), the rows naming **kengaku**
(`grep -n '^| D-1[2-5][0-9] ' shokunin:.ufo/reports/AGGREGATE.md` → the §14.16 table):

| row key | sev | what it says (paraphrase) | pointer it carries |
|---|---:|---|---|
| `D-137` | 3 | `SKILL.md:405-449` gate registry is prose: no explicit code→class map, no write scope, no owner field (eight-field row required) | `git show f09ff1f:SKILL.md \| sed -n '405,449p'` |
| `D-150` | 3 | The vanished `~/Projects/bounties` root is cited outside kasegi too — kengaku 26 occurrences / 23 lines / 13 files at `f09ff1f`, incl. `PROVINCE.md:15,75` | `shokunin:.ufo/waves/round-9/seats/connector.md` §C4 |

Closure sweep — `grep -n 'D-137\|D-150' shokunin:.ufo/reports/AGGREGATE.md shokunin:LOG.md` — returns filing/analysis
mentions only, so both are **open** at the stamp above. `D-137` is why this lane's `could-not-evaluate` cells stay
open: a registry that is prose cannot be re-run by a non-author.

## 6. Box-3 / `SHONEN.md` canonical-form state

The gate's `shonen` check grades `PROTOCOL.md` §File contract canonical form and emits **1 finding** for kengaku
(sweep executed: `node .ufo/waves/round-9/corpus-gate.mjs --repo kengaku-shokunin --round 10 | grep -cE
'^CR-kengaku-shokunin-shonen'` → 1). Quoted verbatim:

```
CR-kengaku-shokunin-shonen-1: SHONEN.md 1 [x] mark line(s) at 9 carry no <verifier-id> token after the box text — the canonical form requires one (§Promotion gates: only a non-author may write [x])
```

So the standing state is: canonical header, 4 canonical boxes and one evidence line per marked box are clean, but the
`[x]` at `SHONEN.md:9` carries no `<verifier-id>`, i.e. the mark's independence is unattested in the file — the
`D-134` class. Whether any mark rests on a *non-author* verifier is declared `not-evaluated` by the gate (`box-3`;
the authorship graph is not in the graded tree), so this cell is **form-failed on one line, semantics not evaluated**.

## 7. Commands a reader re-runs

```bash
# identity of the cell (P-s: revision + dirty count + stamp)
git -C kengaku-shokunin rev-parse HEAD
git -C kengaku-shokunin status --porcelain | wc -l
date -u +%Y-%m-%dT%H:%M:%SZ

# live per-repo verdict and per-rule census at --round 10
node .ufo/waves/round-9/corpus-gate.mjs --repo kengaku-shokunin --round 10
node .ufo/waves/round-9/corpus-gate.mjs --repo kengaku-shokunin --round 10 --json | sed -n 's/^# json //p' | node -e 'let s="";process.stdin.on("data",d=>s+=d).on("end",()=>{const j=JSON.parse(s)[0];const c={};for(const f of j.findings)c[f.rule]=(c[f.rule]||0)+1;console.log(JSON.stringify(c))})'

# before column, pinned revision
node .ufo/waves/round-9/corpus-gate.mjs --snapshot kengaku-shokunin f09ff1f --round 9

# r4 adjudication (absent at this stamp — the L1 re-runs it after the mirror)
node .ufo/waves/round-10/r4-adjudicate.mjs --live --repo kengaku-shokunin --round 10

# rule-8 sweep over this checkout's corpus, in a form that does not itself spell the banned literal
grep -rnE 'op:[/]{2}' kengaku-shokunin/corpus | wc -l

# this lesson's own rule-8 and rule-2 obligations
grep -cE 'op:[/]{2}|\bsk-|\bghp_|github_pat_|\bxox|\bAKIA|-----BEGIN' corpus/lessons/round-10-aggregator-corpus-verdict.md
grep -cE '\b[Rr]ound[-_ ]?10\b|\.ufo/reports/|LOG\.md' corpus/lessons/round-10-aggregator-corpus-verdict.md
```

**This lesson adds no finding to its own repo.** Measured on a throwaway tree
(`git -C kengaku-shokunin archive HEAD | tar -x -C /tmp/verify10/kengaku-shokunin`, then `git init` + one commit in
`/tmp`, never in the child repo), running `node .ufo/waves/round-9/corpus-gate.mjs --repo
/tmp/verify10/kengaku-shokunin --round 10 --json` before and after copying this file to
`corpus/lessons/round-10-aggregator-corpus-verdict.md`: r2 0→0, r4 25→25, r7 0→0, r8 2→2, shonen 1→1 and r10 1→0.
The only cell that moves is the duty finding this file discharges. The r7 under-coverage note denominator moves
160→161 corpus files (a note, not a finding, by construction).