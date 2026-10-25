# Round 10 aggregator corpus verdict — kumitate

**Path convention (`D-128` forward fix).** `shokunin:<path>` resolves in the main repo
`/home/vgpnk/projects/shokunin`; `kumitate-shokunin:<path>` resolves in this checkout
`/home/vgpnk/projects/shokunin/kumitate-shokunin`; bare `corpus/…` and `SHONEN.md` are relative to this checkout's
root.

**Round and evidence.** This is the **round 10** (refresh 8) `CORPUS.md` rule-10 review for kumitate, and it is the
artifact whose absence the gate reports as `r10`. Evidence homes: `shokunin:.ufo/reports/round-9/aggregator.md` §14.2,
§14.6 and §14.17 (the round-9 verdict, the box-3 re-run and the post-mirror gate re-run this one moves from),
`shokunin:.ufo/reports/round-10/aggregator.md` (this round's report; the L1 commits it at round close),
`shokunin:LOG.md` (round-10 lane entry), and the gate, `shokunin:.ufo/waves/round-9/corpus-gate.mjs` (id
`corpus-gate-v1`, read-only).

## 1. Revision measured

| cell | observed | command that produced it |
|---|---|---|
| live `HEAD` (short) | `637d181` | `git -C kumitate-shokunin rev-parse --short HEAD` |
| live `HEAD` (full) | `637d1815bef717c9275d142fe746e51f68660063` | `git -C kumitate-shokunin rev-parse HEAD` |
| worktree dirty count | 7 | `git -C kumitate-shokunin status --porcelain \| wc -l` |
| measurement stamp (UTC) | `2026-09-29T01:51:10Z` | `date -u +%Y-%m-%dT%H:%M:%SZ` |

The live run grades the **worktree**; its identity is the revision *plus* the dirty count observed with it. The dirty
count moved while the fleet ran — `shokunin:.ufo/waves/round-10/CONTEXT.md` stamped 6 at
`2026-09-29T01:44:38Z`, this measurement saw 7 at `2026-09-29T01:51:10Z`
(`git -C kumitate-shokunin status --porcelain | wc -l`). Both runs, quoted:

```
# tree kumitate-shokunin revision=637d1815bef717c9275d142fe746e51f68660063 (worktree) dirty=7 mode=live provisional=1 (worktree-only bytes differ from the cited revision)
# tree kumitate-shokunin revision=7a099b2b7df98a23f8f443763bec05ee8593403c dirty=0 mode=snapshot
```

## 2. `CORPUS.md` rule-10 verdict

**`not conformant`** (gate exit 1). Failed rules and their finding counts, from the live run:

| failed rule | finding count | gate command (`--round 10`) |
|---|---:|---|
| r2 — `lessons/` cites its round and evidence (`CORPUS.md:19`) | 1 | `node .ufo/waves/round-9/corpus-gate.mjs --repo kumitate-shokunin --round 10 --json` |
| r4 — a count carries its backticked command (`CORPUS.md:28`) | 43 | `node .ufo/waves/round-9/corpus-gate.mjs --repo kumitate-shokunin --round 10 --json` |
| r8 — credential material, literal text (`CORPUS.md:43`) | 1 | `node .ufo/waves/round-9/corpus-gate.mjs --repo kumitate-shokunin --round 10 --json` |
| r10 — the round's aggregator lesson is present (`CORPUS.md:21`) | 1 | `node .ufo/waves/round-9/corpus-gate.mjs --repo kumitate-shokunin --round 10 --json` |

The gate's verdict line and the per-rule census the counts above come from (the census command is the `sed`/`node`
pair in §7; both were executed):

```
# verdict kumitate-shokunin failed findings=46 rules=r2,r4,r8,r10 rules-implemented=r2,r4,r7,r8,r10,shonen
CR-kumitate-shokunin-r2-1: lessons/round-9.md carries no evidence pointer (commit hash, .ufo/reports/ path, or LOG.md) (CORPUS.md:19)
CR-kumitate-shokunin-r10-1: no corpus/lessons/round-10-aggregator-*.md — the round-10 review duty has no emitted lesson (CORPUS.md:21)
{"r2":1,"r4":43,"r8":1,"r10":1}
```

r7 emits **0 findings** and `shonen` emits **0 findings**. The r2 finding is a lane-owned lesson,
`kumitate-shokunin:corpus/lessons/round-9.md` (not this file, which cites both its round and evidence). The r8 cell
carries the gate's declared abstention — `classification=could-not-evaluate (needs a vault read; operator-gated)` —
per cell.

## 3. Per-rule counts, and movement from the round-9 pinned revision

Live column: `node .ufo/waves/round-9/corpus-gate.mjs --repo kumitate-shokunin --round 10 --json`.
Before column: `node .ufo/waves/round-9/corpus-gate.mjs --snapshot kumitate-shokunin 7a099b2 --round 9 --json`
(the round-9 pinned revision for this repo in `shokunin:.ufo/waves/round-10/CONTEXT.md`).

| rule | live (`637d181`, dirty 7) | before (`7a099b2`, `--round 9`) | movement | live command | before command |
|---|---:|---:|---|---|---|
| r2 | 1 | 1 | flat (same file) | `node .ufo/waves/round-9/corpus-gate.mjs --repo kumitate-shokunin --round 10 --json` | `node .ufo/waves/round-9/corpus-gate.mjs --snapshot kumitate-shokunin 7a099b2 --round 9 --json` |
| r4 | 43 | 33 | **+10** | `node .ufo/waves/round-9/corpus-gate.mjs --repo kumitate-shokunin --round 10 --json` | `node .ufo/waves/round-9/corpus-gate.mjs --snapshot kumitate-shokunin 7a099b2 --round 9 --json` |
| r7 | 0 | 0 | flat | `node .ufo/waves/round-9/corpus-gate.mjs --repo kumitate-shokunin --round 10 --json` | `node .ufo/waves/round-9/corpus-gate.mjs --snapshot kumitate-shokunin 7a099b2 --round 9 --json` |
| r8 | 1 | 1 | flat in count, **+1 occurrence** | `node .ufo/waves/round-9/corpus-gate.mjs --repo kumitate-shokunin --round 10 --json` | `node .ufo/waves/round-9/corpus-gate.mjs --snapshot kumitate-shokunin 7a099b2 --round 9 --json` |
| r10 | 1 | 1 | flat (artifact — see note) | `node .ufo/waves/round-9/corpus-gate.mjs --repo kumitate-shokunin --round 10 --json` | `node .ufo/waves/round-9/corpus-gate.mjs --snapshot kumitate-shokunin 7a099b2 --round 9 --json` |
| shonen | 0 | 0 | flat | `node .ufo/waves/round-9/corpus-gate.mjs --repo kumitate-shokunin --round 10 --json` | `node .ufo/waves/round-9/corpus-gate.mjs --snapshot kumitate-shokunin 7a099b2 --round 9 --json` |

The before run re-derives the gate's frozen expectation
(`shokunin:.ufo/waves/round-9/corpus-gate.expected.json` `frozen["kumitate-shokunin@7a099b2"].stats`):

```
# expect kumitate-shokunin@7a099b2 MATCH exit=1 ids=36
# verdict kumitate-shokunin failed findings=36 rules=r2,r4,r8,r10 rules-implemented=r2,r4,r7,r8,r10,shonen
```

**r10 note.** Both r10 cells are 1 but measure different duties: the live cell is *this lesson* not yet mirrored; the
before cell is the *round-9* lesson absent from the archived `7a099b2` tree. The real movement is r4 **+10**; r2, r8
and shonen are flat (the r8 class is the same owner, `aggregator`, with its occurrence count rising 1→2 as the
round-9 verdict lesson joined `kumitate-shokunin:corpus/lessons/round-5-aggregator-audit.md` —
`node .ufo/waves/round-9/corpus-gate.mjs --repo kumitate-shokunin --round 10` prints
`occurrences=2 lines=2 files=2 … first=lessons/round-5-aggregator-audit.md:79`).

r4's growth is the dominant movement. Its 43 findings at this revision concentrate on
`kumitate-shokunin:corpus/knowledge/route-probe-cluster.md` with 5, then
`kumitate-shokunin:corpus/knowledge/remaining-scripts-census.md`, `kumitate-shokunin:corpus/lessons/round-12.md` and
`kumitate-shokunin:corpus/lessons/round-13.md` with 4 each
(`node .ufo/waves/round-9/corpus-gate.mjs --repo kumitate-shokunin --round 10 --json`). r7 is 0 findings on both
sides — the gate grades the phantom-row reading only and prints under-coverage as a note; here it is the fleet's
cleanest index:

```
# note kumitate-shokunin r7: 4 backticked path template(s)/glob(s) skipped (contain *, <, {, ~, $ or …)
# note kumitate-shokunin r7 under-coverage (not a finding): 0/50 corpus files carry no index row
```

Hand-adjudicated round-9 verdict vs the gate-recomputable cells: `shokunin:.ufo/reports/round-9/aggregator.md` §14.2
graded kumitate `not conformant` on rules 1, 2, 4, 6, 7, 8-literal and 9. The gate cannot reproduce the rules it
declares not-evaluated (`r1 r3 r5 r6 r9 box-3`). One round-9 provenance detail still binds: §14.17 records that the
round-9 lesson mirror landed as `93b0567` and the repo advanced to `637d181` about 2 s later, so the summary revision
and the lesson's pinned revision differ — this round's lesson pins the revision it measured (§1).

## 4. r4 adjudication

`node .ufo/waves/round-10/r4-adjudicate.mjs --live --repo kumitate-shokunin --round 10` was attempted at the stamp
above and **does not exist**: `ls -la shokunin:.ufo/waves/round-10/r4-adjudicate.mjs` → `No such file or directory`,
and the run exits 1 with `Error: Cannot find module
'/home/vgpnk/projects/shokunin/.ufo/waves/round-10/r4-adjudicate.mjs'` (`code: 'MODULE_NOT_FOUND'`). Only the raw
count is published:

**raw r4 count = 43** — `node .ufo/waves/round-9/corpus-gate.mjs --repo kumitate-shokunin --round 10 --json`

adjudication: not-run at draft time (L1 re-measures after the mirror)

No false-positive/violation split is invented. The declared false-positive classes the round-10 axis-move closes are
the three named in `shokunin:SCORECARD.md` §Planned (round 10), including the rule-4/rule-9 collision routed as
`D-141`.

## 5. Ledger rows this verdict rests on

From `shokunin:.ufo/reports/AGGREGATE.md` §14.16 (rows `D-121`…`D-150`), the rows owned by **kumitate**
(`grep -n '^| D-1[2-5][0-9] ' shokunin:.ufo/reports/AGGREGATE.md` → the §14.16 table):

| row key | sev | what it says (paraphrase) | pointer it carries |
|---|---:|---|---|
| `D-138` | 2 | `round-gate.mjs` cannot satisfy §Gate standard's frozen-snapshot clause: a `git archive` tree fail-closes `NOT_A_GIT_WORKTREE` exit 2 ⇒ no re-runnable frozen evidence | `cd /tmp/kumitate-e0 && node scripts/round-gate.mjs` |
| `D-139` | 3 | Registry rows at `SKILL.md:540-544` are not a single eight-field row; exits 2/64 not mapped to `could-not-evaluate` | `git show e0e5de1:SKILL.md \| sed -n '540,644p'` |

Closure sweep — `grep -n 'D-138\|D-139' shokunin:.ufo/reports/AGGREGATE.md shokunin:LOG.md` — returns filing/analysis
mentions only, so both are **open** at the stamp above. `D-138` is the sharpest of the two for this verdict: a gate
that fail-closes on a `git archive` tree cannot produce the frozen revision-named evidence `CORPUS.md` rule 10 is
supposed to rest on.

## 6. Box-3 / `SHONEN.md` canonical-form state

The gate's `shonen` check grades `PROTOCOL.md` §File contract canonical form and emits **0 findings** for kumitate
(sweep executed: `node .ufo/waves/round-9/corpus-gate.mjs --repo kumitate-shokunin --round 10 | grep -cE
'^CR-kumitate-shokunin-shonen'` → 0). Zero findings means: header block canonical, exactly 4 canonical boxes, marks
confined to the box character plus at most one indented evidence line each, `[x]` lines carrying a `<verifier-id>`
token, no other lines, trailing newline present. It does **not** mean box 3 is sound: whether an `[x]` rests on a
*non-author* verifier is declared `not-evaluated` by the gate (`box-3`). `shokunin:.ufo/reports/round-9/aggregator.md`
§14.6 firmed kumitate's box-3 by a non-author cold run at the landed revision, and §14.17 records the lesson mirrored
under the aggregator identity. The standing state is therefore: **form conformant, box-3 firmed in the round-9
record, `D-138` still blocks a re-runnable frozen form**.

## 7. Commands a reader re-runs

```bash
# identity of the cell (P-s: revision + dirty count + stamp)
git -C kumitate-shokunin rev-parse HEAD
git -C kumitate-shokunin status --porcelain | wc -l
date -u +%Y-%m-%dT%H:%M:%SZ

# live per-repo verdict and per-rule census at --round 10
node .ufo/waves/round-9/corpus-gate.mjs --repo kumitate-shokunin --round 10
node .ufo/waves/round-9/corpus-gate.mjs --repo kumitate-shokunin --round 10 --json | sed -n 's/^# json //p' | node -e 'let s="";process.stdin.on("data",d=>s+=d).on("end",()=>{const j=JSON.parse(s)[0];const c={};for(const f of j.findings)c[f.rule]=(c[f.rule]||0)+1;console.log(JSON.stringify(c))})'

# before column, pinned revision
node .ufo/waves/round-9/corpus-gate.mjs --snapshot kumitate-shokunin 7a099b2 --round 9

# r4 adjudication (absent at this stamp — the L1 re-runs it after the mirror)
node .ufo/waves/round-10/r4-adjudicate.mjs --live --repo kumitate-shokunin --round 10

# rule-8 sweep over this checkout's corpus, in a form that does not itself spell the banned literal
grep -rnE 'op:[/]{2}' kumitate-shokunin/corpus | wc -l

# this lesson's own rule-8 and rule-2 obligations
grep -cE 'op:[/]{2}|\bsk-|\bghp_|github_pat_|\bxox|\bAKIA|-----BEGIN' corpus/lessons/round-10-aggregator-corpus-verdict.md
grep -cE '\b[Rr]ound[-_ ]?10\b|\.ufo/reports/|LOG\.md' corpus/lessons/round-10-aggregator-corpus-verdict.md
```

**This lesson adds no finding to its own repo.** Measured on a throwaway tree
(`git -C kumitate-shokunin archive HEAD | tar -x -C /tmp/verify10/kumitate-shokunin`, then `git init` + one commit in
`/tmp`, never in the child repo), running `node .ufo/waves/round-9/corpus-gate.mjs --repo
/tmp/verify10/kumitate-shokunin --round 10 --json` before and after copying this file to
`corpus/lessons/round-10-aggregator-corpus-verdict.md`: r2 1→1, r4 38→38, r7 0→0, r8 1→1 (same occurrence count),
shonen 0→0 and r10 1→0. The only cell that moves is the duty finding this file discharges. (The fixture grades the
committed `HEAD` archive, so its r4 reads 38 where the live worktree reads 43 — the difference is carried by the dirty
and untracked bytes, which the fixture does not contain; the **delta** is what this cell measures, not the level.) The
r7 under-coverage note denominator moves 50→51 corpus files (a note, not a finding, by construction).