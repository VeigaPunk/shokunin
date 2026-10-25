# Round 10 aggregator corpus verdict — kake

**Path convention (`D-128` forward fix).** `shokunin:<path>` resolves in the main repo
`/home/vgpnk/projects/shokunin`; `kake-shokunin:<path>` resolves in this checkout
`/home/vgpnk/projects/shokunin/kake-shokunin`; bare `corpus/…` and `SHONEN.md` are relative to this checkout's root.

**Round and evidence.** This is the **round 10** (refresh 8) `CORPUS.md` rule-10 review for kake, and it is the
artifact whose absence the gate reports as `r10`. Evidence homes: `shokunin:.ufo/reports/round-9/aggregator.md` §14.2
and §14.4 (the round-9 verdict and the literal rule-8 grading this one moves from),
`shokunin:.ufo/reports/round-10/aggregator.md` (this round's report; the L1 commits it at round close),
`shokunin:LOG.md` (round-10 lane entry), and the gate, `shokunin:.ufo/waves/round-9/corpus-gate.mjs` (id
`corpus-gate-v1`, read-only).

## 1. Revision measured

| cell | observed | command that produced it |
|---|---|---|
| live `HEAD` (short) | `4214101` | `git -C kake-shokunin rev-parse --short HEAD` |
| live `HEAD` (full) | `421410199fd5840cce64769a91a8fc7f6a265863` | `git -C kake-shokunin rev-parse HEAD` |
| worktree dirty count | 6 | `git -C kake-shokunin status --porcelain \| wc -l` |
| measurement stamp (UTC) | `2026-09-29T01:51:10Z` | `date -u +%Y-%m-%dT%H:%M:%SZ` |

The live run grades the **worktree**; its identity is the revision *plus* the dirty count observed with it. The dirty
count moved while the fleet ran — `shokunin:.ufo/waves/round-10/CONTEXT.md` stamped 0 at
`2026-09-29T01:44:38Z`, this measurement saw 6 at `2026-09-29T01:51:10Z`
(`git -C kake-shokunin status --porcelain | wc -l`). Both runs, quoted:

```
# tree kake-shokunin revision=421410199fd5840cce64769a91a8fc7f6a265863 (worktree) dirty=6 mode=live provisional=1 (worktree-only bytes differ from the cited revision)
# tree kake-shokunin revision=a2094411fe9051ebf3c10929ed33c1b6c032ea39 dirty=0 mode=snapshot
```

## 2. `CORPUS.md` rule-10 verdict

**`not conformant`** (gate exit 1). Failed rules and their finding counts, from the live run:

| failed rule | finding count | gate command (`--round 10`) |
|---|---:|---|
| r4 — a count carries its backticked command (`CORPUS.md:28`) | 35 | `node .ufo/waves/round-9/corpus-gate.mjs --repo kake-shokunin --round 10 --json` |
| r8 — credential material, literal text (`CORPUS.md:43`) | 1 | `node .ufo/waves/round-9/corpus-gate.mjs --repo kake-shokunin --round 10 --json` |
| r10 — the round's aggregator lesson is present (`CORPUS.md:21`) | 1 | `node .ufo/waves/round-9/corpus-gate.mjs --repo kake-shokunin --round 10 --json` |

The gate's verdict line and the per-rule census the counts above come from (the census command is the `sed`/`node`
pair in §7; both were executed):

```
# verdict kake-shokunin failed findings=37 rules=r4,r8,r10 rules-implemented=r2,r4,r7,r8,r10,shonen
CR-kake-shokunin-r10-1: no corpus/lessons/round-10-aggregator-*.md — the round-10 review duty has no emitted lesson (CORPUS.md:21)
{"r4":35,"r8":1,"r10":1}
```

r2 and r7 emit **0 findings** (every `lessons/` entry carries its round and an evidence pointer; no index row names an
absent file); the `shonen` check emits **0 findings** too, so `SHONEN.md` is in canonical form at this revision
(§6). The r8 cell carries the gate's declared abstention — `classification=could-not-evaluate (needs a
vault read; operator-gated)` — per cell.

## 3. Per-rule counts, and movement from the round-9 pinned revision

Live column: `node .ufo/waves/round-9/corpus-gate.mjs --repo kake-shokunin --round 10 --json`.
Before column: `node .ufo/waves/round-9/corpus-gate.mjs --snapshot kake-shokunin a209441 --round 9 --json`
(the first of the two round-9 pinned revisions for this repo in `shokunin:.ufo/waves/round-10/CONTEXT.md`).

| rule | live (`4214101`, dirty 6) | before (`a209441`, `--round 9`) | movement | live command | before command |
|---|---:|---:|---|---|---|
| r2 | 0 | 0 | flat | `node .ufo/waves/round-9/corpus-gate.mjs --repo kake-shokunin --round 10 --json` | `node .ufo/waves/round-9/corpus-gate.mjs --snapshot kake-shokunin a209441 --round 9 --json` |
| r4 | 35 | 35 | flat | `node .ufo/waves/round-9/corpus-gate.mjs --repo kake-shokunin --round 10 --json` | `node .ufo/waves/round-9/corpus-gate.mjs --snapshot kake-shokunin a209441 --round 9 --json` |
| r7 | 0 | 0 | flat | `node .ufo/waves/round-9/corpus-gate.mjs --repo kake-shokunin --round 10 --json` | `node .ufo/waves/round-9/corpus-gate.mjs --snapshot kake-shokunin a209441 --round 9 --json` |
| r8 | 1 | 1 | flat in count, **+1 occurrence** | `node .ufo/waves/round-9/corpus-gate.mjs --repo kake-shokunin --round 10 --json` | `node .ufo/waves/round-9/corpus-gate.mjs --snapshot kake-shokunin a209441 --round 9 --json` |
| r10 | 1 | 1 | flat (artifact — see note) | `node .ufo/waves/round-9/corpus-gate.mjs --repo kake-shokunin --round 10 --json` | `node .ufo/waves/round-9/corpus-gate.mjs --snapshot kake-shokunin a209441 --round 9 --json` |
| shonen | 0 | 0 | flat | `node .ufo/waves/round-9/corpus-gate.mjs --repo kake-shokunin --round 10 --json` | `node .ufo/waves/round-9/corpus-gate.mjs --snapshot kake-shokunin a209441 --round 9 --json` |

Both before-candidate revisions re-derive their frozen expectations
(`shokunin:.ufo/waves/round-9/corpus-gate.expected.json` `frozen["kake-shokunin@a209441"]`,
`frozen["kake-shokunin@4c9a985"]`):

```
# expect kake-shokunin@a209441 MATCH exit=1 ids=37
# expect kake-shokunin@4c9a985 MATCH exit=1 ids=34
```

The second pinned revision, `4c9a985` (the revision the round-9 seat brief named as kake's dirty HEAD), measures r4
32 — `node .ufo/waves/round-9/corpus-gate.mjs --snapshot kake-shokunin 4c9a985 --round 9 --json` → `{"r4":32,"r8":1,"r10":1}`.
So the r4 cell reads 32 → 35 (+3) across the round-9 seat revision to live, and 35 → 35 (flat) across the L1 pinned
revision to live.

**r10 note.** Both r10 cells are 1 but measure different duties: the live cell is *this lesson* not yet mirrored; the
before cell is the *round-9* lesson absent from the archived tree. The r8 class is the same one in both columns —
owner `aggregator` — its occurrence count rises 2→3 because the round-9 verdict lesson joined the two prior
aggregator lessons (`node .ufo/waves/round-9/corpus-gate.mjs --repo kake-shokunin --round 10` prints
`occurrences=3 lines=3 files=3 … files=[lessons/round-5-aggregator-audit.md,lessons/round-6-aggregator-audit.md,lessons/round-9-aggregator-corpus-verdict.md]`).
A count of 1 with a larger occurrence count is not a cleaner corpus; the gate's unit for r8 is occurrences.

r4's 35 findings concentrate on `kake-shokunin:corpus/knowledge/free-read-verbs.md` with 6, then
`kake-shokunin:corpus/knowledge/kimi-subpath-audit.md`, `kake-shokunin:corpus/knowledge/ops-automation.md`,
`kake-shokunin:corpus/lessons/round-4-aggregator-audit.md`, `kake-shokunin:corpus/lessons/round-6-aggregator-audit.md`
and `kake-shokunin:corpus/lessons/round-6.md` with 3 each
(`node .ufo/waves/round-9/corpus-gate.mjs --repo kake-shokunin --round 10 --json`). r7 is 0 findings on both sides —
the gate grades the phantom-row reading only and prints under-coverage as a note:

```
# note kake-shokunin r7: 1 backticked path template(s)/glob(s) skipped (contain *, <, {, ~, $ or …)
# note kake-shokunin r7 under-coverage (not a finding): 16/34 corpus files carry no index row
```

Hand-adjudicated round-9 verdict vs the gate-recomputable cells: `shokunin:.ufo/reports/round-9/aggregator.md` §14.2
graded kake `not conformant` on rules 1, 3, 4, 5, 6, 8-literal and 9. The gate cannot reproduce the rules it declares
not-evaluated (`r1 r3 r5 r6 r9 box-3`); its cells and that prose are complementary, not equal.

## 4. r4 adjudication

`node .ufo/waves/round-10/r4-adjudicate.mjs --live --repo kake-shokunin --round 10` was attempted at the stamp above
and **does not exist**: `ls -la shokunin:.ufo/waves/round-10/r4-adjudicate.mjs` → `No such file or directory`, and the
run exits 1 with `Error: Cannot find module '/home/vgpnk/projects/shokunin/.ufo/waves/round-10/r4-adjudicate.mjs'`
(`code: 'MODULE_NOT_FOUND'`). Only the raw count is published:

**raw r4 count = 35** — `node .ufo/waves/round-9/corpus-gate.mjs --repo kake-shokunin --round 10 --json`

adjudication: not-run at draft time (L1 re-measures after the mirror)

No false-positive/violation split is invented. The declared false-positive classes the round-10 axis-move closes are
the three named in `shokunin:SCORECARD.md` §Planned (round 10), including the rule-4/rule-9 collision routed as
`D-141`.

## 5. Ledger rows this verdict rests on

From `shokunin:.ufo/reports/AGGREGATE.md` §14.16 (rows `D-121`…`D-150`), the rows owned by **kake**
(`grep -n '^| D-1[2-5][0-9] ' shokunin:.ufo/reports/AGGREGATE.md` → the §14.16 table):

| row key | sev | what it says (paraphrase) | pointer it carries |
|---|---:|---|---|
| `D-121` | 4 | Scribe push gate failed for three ledger beats (`pushed:false`, pull timeout, grok-web empty/ceiling) — pushes stalled | `shokunin:.ufo/reports/round-12/kake.md:80-86` |
| `D-122` | 4 | `grokbots --check` tests registry-row existence, not wrapper presence; `botWrapperPath` unused ⇒ wrapper-missing blind spot | `shokunin:.ufo/reports/round-12/kake.md:92-95` |

Closure sweep — `grep -n 'D-121\|D-122' shokunin:.ufo/reports/AGGREGATE.md shokunin:LOG.md` — returns filing/analysis
mentions only, so both are **open** at the stamp above. Both are gate-shaped defects: a non-author cannot re-run a
push gate that stalls (`D-121`) or a `--check` that tests the wrong surface (`D-122`).

## 6. Box-3 / `SHONEN.md` canonical-form state

The gate's `shonen` check grades `PROTOCOL.md` §File contract canonical form and emits **0 findings** for kake (sweep
executed: `node .ufo/waves/round-9/corpus-gate.mjs --repo kake-shokunin --round 10 | grep -cE '^CR-kake-shokunin-shonen'`
→ 0). Zero findings means: header block canonical, exactly 4 canonical boxes, marks confined to the box character plus
at most one indented evidence line each, `[x]` lines carrying a `<verifier-id>` token, no other lines, trailing newline
present. It does **not** mean box 3 is sound: whether an `[x]` rests on a *non-author* verifier is declared
`not-evaluated` by the gate (`box-3`; the authorship graph is not in the graded tree), and
`shokunin:.ufo/reports/round-9/aggregator.md` §14.6 recorded kake's box-3 mark as **stays provisional** — the round-8
15-command battery was measured against a moving dirty tree and no committed gate with pinned expected finding-ids
re-runs it. The standing state is therefore: **form conformant, box-3 provisional (no pinned re-run)**.

## 7. Commands a reader re-runs

```bash
# identity of the cell (P-s: revision + dirty count + stamp)
git -C kake-shokunin rev-parse HEAD
git -C kake-shokunin status --porcelain | wc -l
date -u +%Y-%m-%dT%H:%M:%SZ

# live per-repo verdict and per-rule census at --round 10
node .ufo/waves/round-9/corpus-gate.mjs --repo kake-shokunin --round 10
node .ufo/waves/round-9/corpus-gate.mjs --repo kake-shokunin --round 10 --json | sed -n 's/^# json //p' | node -e 'let s="";process.stdin.on("data",d=>s+=d).on("end",()=>{const j=JSON.parse(s)[0];const c={};for(const f of j.findings)c[f.rule]=(c[f.rule]||0)+1;console.log(JSON.stringify(c))})'

# before column, both pinned revisions
node .ufo/waves/round-9/corpus-gate.mjs --snapshot kake-shokunin a209441 --round 9
node .ufo/waves/round-9/corpus-gate.mjs --snapshot kake-shokunin 4c9a985 --round 9

# r4 adjudication (absent at this stamp — the L1 re-runs it after the mirror)
node .ufo/waves/round-10/r4-adjudicate.mjs --live --repo kake-shokunin --round 10

# rule-8 sweep over this checkout's corpus, in a form that does not itself spell the banned literal
grep -rnE 'op:[/]{2}' kake-shokunin/corpus | wc -l

# this lesson's own rule-8 and rule-2 obligations
grep -cE 'op:[/]{2}|\bsk-|\bghp_|github_pat_|\bxox|\bAKIA|-----BEGIN' corpus/lessons/round-10-aggregator-corpus-verdict.md
grep -cE '\b[Rr]ound[-_ ]?10\b|\.ufo/reports/|LOG\.md' corpus/lessons/round-10-aggregator-corpus-verdict.md
```

**This lesson adds no finding to its own repo.** Measured on a throwaway tree
(`git -C kake-shokunin archive HEAD | tar -x -C /tmp/verify10/kake-shokunin`, then `git init` + one commit in `/tmp`,
never in the child repo), running `node .ufo/waves/round-9/corpus-gate.mjs --repo /tmp/verify10/kake-shokunin
--round 10 --json` before and after copying this file to `corpus/lessons/round-10-aggregator-corpus-verdict.md`:
r2 0→0, r4 35→35, r7 0→0, r8 1→1 (same occurrence count), shonen 0→0 and r10 1→0. The only cell that moves is the
duty finding this file discharges. The r7 under-coverage note denominator moves 34→35 corpus files (a note, not a
finding, by construction).