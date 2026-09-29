# Round 10 aggregator corpus verdict — kasegi

**Path convention (`D-128` forward fix).** `shokunin:<path>` resolves in the main repo
`/home/vgpnk/projects/shokunin`; `kasegi-shokunin:<path>` resolves in this checkout
`/home/vgpnk/projects/shokunin/kasegi-shokunin`; bare `corpus/…`, `SHONEN.md` and `.ufo/…` are relative to this
checkout's root.

**Round and evidence.** This is the **round 10** (refresh 8) `CORPUS.md` rule-10 review for kasegi, and it is the
artifact whose absence the gate reports as `r10`. Evidence homes: `shokunin:.ufo/reports/round-9/aggregator.md` §14.2
(the round-9 verdict this one moves from), `shokunin:.ufo/reports/round-10/aggregator.md` (this round's report; the L1
commits it at round close), `shokunin:LOG.md` (round-10 lane entry), and the gate itself,
`shokunin:.ufo/waves/round-9/corpus-gate.mjs` (id `corpus-gate-v1`, read-only over every surface it grades).

## 1. Revision measured

| cell | observed | command that produced it |
|---|---|---|
| live `HEAD` (short) | `b021dc9` | `git -C kasegi-shokunin rev-parse --short HEAD` |
| live `HEAD` (full) | `b021dc925f5cc17702ebff6ffa25c3b6e4efcf7b` | `git -C kasegi-shokunin rev-parse HEAD` |
| worktree dirty count | 1 | `git -C kasegi-shokunin status --porcelain \| wc -l` |
| measurement stamp (UTC) | `2026-09-29T01:51:10Z` | `date -u +%Y-%m-%dT%H:%M:%SZ` |

The live run grades the **worktree**, so its identity is the revision *plus* the dirty count observed with it; the
gate says so itself (quoted, both runs):

```
# tree kasegi-shokunin revision=b021dc925f5cc17702ebff6ffa25c3b6e4efcf7b (worktree) dirty=1 mode=live provisional=1 (worktree-only bytes differ from the cited revision)
# tree kasegi-shokunin revision=b7180b0303755212ea4b60e52152aa8bf010c5b0 dirty=0 mode=snapshot
```

## 2. `CORPUS.md` rule-10 verdict

**`not conformant`** (gate exit 1). `CORPUS.md:21` requires a per-repo verdict for the round's review; this is it, and
it names the revision above. Failed rules and their finding counts, from the live run:

| failed rule | finding count | gate command (`--round 10`) |
|---|---:|---|
| r2 — `lessons/` cites its round and evidence (`CORPUS.md:19`) | 3 | `node .ufo/waves/round-9/corpus-gate.mjs --repo kasegi-shokunin --round 10 --json` |
| r4 — a count carries its backticked command (`CORPUS.md:28`) | 49 | `node .ufo/waves/round-9/corpus-gate.mjs --repo kasegi-shokunin --round 10 --json` |
| r8 — credential material, literal text (`CORPUS.md:43`) | 3 | `node .ufo/waves/round-9/corpus-gate.mjs --repo kasegi-shokunin --round 10 --json` |
| r10 — the round's aggregator lesson is present (`CORPUS.md:21`) | 1 | `node .ufo/waves/round-9/corpus-gate.mjs --repo kasegi-shokunin --round 10 --json` |

The gate's own verdict line, its four `r10`-adjacent facts, and the per-rule census the counts above come from
(the census command is the `sed`/`node` pair in §7; both were executed):

```
# verdict kasegi-shokunin failed findings=56 rules=r2,r4,r8,r10 rules-implemented=r2,r4,r7,r8,r10,shonen
CR-kasegi-shokunin-r10-1: no corpus/lessons/round-10-aggregator-*.md — the round-10 review duty has no emitted lesson (CORPUS.md:21)
{"r2":3,"r4":49,"r8":3,"r10":1}
```

The `r10` finding is the pre-mirror state and is discharged by this file; it is a duty finding, not a corpus defect.
The r2 findings are three lesson files that carry no evidence pointer — `lessons/round-10.md`, `lessons/round-12.md`,
`lessons/round-13.md` (gate finding ids `CR-kasegi-shokunin-r2-1..3`), a lane-owned class, not this lesson's.
The r8 cell carries the gate's declared abstention: `classification=could-not-evaluate (needs a vault read;
operator-gated)` — schematic-vs-real is never guessed, per cell.

## 3. Per-rule counts, and movement from the round-9 pinned revision

Live column: `node .ufo/waves/round-9/corpus-gate.mjs --repo kasegi-shokunin --round 10 --json`.
Before column: `node .ufo/waves/round-9/corpus-gate.mjs --snapshot kasegi-shokunin b7180b0 --round 9 --json`
(the round-9 pinned revision for this repo in `shokunin:.ufo/waves/round-10/CONTEXT.md`).

| rule | live (`b021dc9`, dirty 1) | before (`b7180b0`, `--round 9`) | movement | live command | before command |
|---|---:|---:|---|---|---|
| r2 | 3 | 3 | flat | `node .ufo/waves/round-9/corpus-gate.mjs --repo kasegi-shokunin --round 10 --json` | `node .ufo/waves/round-9/corpus-gate.mjs --snapshot kasegi-shokunin b7180b0 --round 9 --json` |
| r4 | 49 | 44 | **+5** | `node .ufo/waves/round-9/corpus-gate.mjs --repo kasegi-shokunin --round 10 --json` | `node .ufo/waves/round-9/corpus-gate.mjs --snapshot kasegi-shokunin b7180b0 --round 9 --json` |
| r7 | 0 | 0 | flat | `node .ufo/waves/round-9/corpus-gate.mjs --repo kasegi-shokunin --round 10 --json` | `node .ufo/waves/round-9/corpus-gate.mjs --snapshot kasegi-shokunin b7180b0 --round 9 --json` |
| r8 | 3 | 1 | **+2** | `node .ufo/waves/round-9/corpus-gate.mjs --repo kasegi-shokunin --round 10 --json` | `node .ufo/waves/round-9/corpus-gate.mjs --snapshot kasegi-shokunin b7180b0 --round 9 --json` |
| r10 | 1 | 1 | flat (artifact — see note) | `node .ufo/waves/round-9/corpus-gate.mjs --repo kasegi-shokunin --round 10 --json` | `node .ufo/waves/round-9/corpus-gate.mjs --snapshot kasegi-shokunin b7180b0 --round 9 --json` |
| shonen | 0 | 0 | flat | `node .ufo/waves/round-9/corpus-gate.mjs --repo kasegi-shokunin --round 10 --json` | `node .ufo/waves/round-9/corpus-gate.mjs --snapshot kasegi-shokunin b7180b0 --round 9 --json` |

**r10 note (measurement honesty).** Both r10 cells are 1, but they measure different things: the live cell is *this
lesson* not yet mirrored; the before cell is the *round-9* lesson absent from the archived `b7180b0` tree (the lesson
lands after the pinned revision). The gate's frozen expectation records the same before cell —
`shokunin:.ufo/waves/round-9/corpus-gate.expected.json` `frozen["kasegi-shokunin@b7180b0"].stats.r10` = 1 — and the
before run re-derives it:

```
# expect kasegi-shokunin@b7180b0 MATCH exit=1 ids=49
# verdict kasegi-shokunin failed findings=49 rules=r2,r4,r8,r10 rules-implemented=r2,r4,r7,r8,r10,shonen
```

The real movement is r4 +5 and r8 +2; r2, r7 and shonen are flat. r7 is 0 findings on both sides — the gate grades
the phantom-row reading only and prints under-coverage as a note (quoted, live run):

```
# note kasegi-shokunin r7: 5 backticked path template(s)/glob(s) skipped (contain *, <, {, ~, $ or …)
# note kasegi-shokunin r7 under-coverage (not a finding): 26/51 corpus files carry no index row
```

r4's growth concentrates on three surfaces (live run): `knowledge/ufo-workspaces.md` 12 findings, `README.md` 5,
`knowledge/target-checkouts.md` 4 — all count lines with no backticked command on the line (`CORPUS.md:28`).

## 4. r4 adjudication

`shokunin:.ufo/waves/round-10/r4-adjudicate.mjs` was attempted at draft time —
`node .ufo/waves/round-10/r4-adjudicate.mjs --live --repo kasegi-shokunin --round 10` — and **does not exist at the
stamp above**: `ls -la shokunin:.ufo/waves/round-10/r4-adjudicate.mjs` → `No such file or directory`, and the run
exits 1 with `Error: Cannot find module '/home/vgpnk/projects/shokunin/.ufo/waves/round-10/r4-adjudicate.mjs'`
(`code: 'MODULE_NOT_FOUND'`). So only the raw r4 count is published here:

**raw r4 count = 49** — `node .ufo/waves/round-9/corpus-gate.mjs --repo kasegi-shokunin --round 10 --json`

adjudication: not-run at draft time (L1 re-measures after the mirror)

No split (false-positive vs violation) is invented. The declared false-positive classes the round-10 axis-move is
closing are the three named in `shokunin:SCORECARD.md` §Planned (round 10) — including the rule-4/rule-9 collision
routed as `D-141` (a falsified count quoted inside a correction entry, which rule 9 requires, trips rule 4 as
written); 246 r4 findings were the round-9 fleet total carried by that class set
(`shokunin:.ufo/reports/round-9/aggregator.md` §14.2 fleet tally).

## 5. Ledger rows this verdict rests on

From `shokunin:.ufo/reports/AGGREGATE.md` §14.16 (rows `D-121`…`D-150`), the rows owned by **kasegi**, each re-read
at that section with `grep -n '^| D-1[2-5][0-9] ' shokunin:.ufo/reports/AGGREGATE.md`:

| row key | sev | what it says (paraphrase) | pointer it carries |
|---|---:|---|---|
| `D-123` | 4 | Two DONE packages unfiled; operator queue stale (11 rows vs 12 after live regeneration) | `shokunin:.ufo/reports/round-14/kasegi.md:114-117` |
| `D-135` | 2 | `PROVINCE.md` still names the absent `~/Projects/bounties`; `SKILL.md` 40 hits at `0f2dca0`; 740/782 distinct citations unresolvable | `git -C kasegi-shokunin grep -c 'Projects/bounties' 0f2dca0 -- PROVINCE.md SKILL.md` |
| `D-136` | 2 | Box-3 decisive harness untracked at every landed revision (`git ls-files ops/ \| wc -l` → 0 at `b7180b0` and `0f2dca0`) | `shokunin:.ufo/reports/round-9/aggregator.md` §14.6 |

Closure sweep for the three keys — `grep -n 'D-123\|D-135\|D-136' shokunin:.ufo/reports/AGGREGATE.md
shokunin:LOG.md` — returns filing/analysis mentions only (no row marked closed or resolved), so all three are
**open** at the stamp above. `D-136` is why this lane's `could-not-evaluate` cells persist: the decisive harness is
untracked, so a non-author cannot re-run it at any landed revision.

## 6. Box-3 / `SHONEN.md` canonical-form state

The gate's `shonen` check grades `PROTOCOL.md` §File contract canonical form. For kasegi it emits **0 findings**
(sweep, executed):

`node .ufo/waves/round-9/corpus-gate.mjs --repo kasegi-shokunin --round 10 | grep -cE '^CR-kasegi-shokunin-shonen'` → 0

Zero `shonen` findings means: header block canonical, exactly 4 canonical boxes, marks confined to the box character
plus at most one indented evidence line each, `[x]` lines carrying a `<verifier-id>` token, no other lines, trailing
newline present. It does **not** mean box 3 is sound — whether an `[x]` rests on a *non-author* verifier is declared
`not-evaluated` by the gate (`box-3`: the authorship graph is not in the graded tree), and for kasegi `D-136` says
the decisive harness cannot be re-run by anyone but its author. The standing state is therefore: **form conformant,
box-3 non-author verifiability blocked on `D-136`**.

## 7. Commands a reader re-runs

```bash
# identity of the cell (P-s: revision + dirty count + stamp)
git -C kasegi-shokunin rev-parse HEAD
git -C kasegi-shokunin status --porcelain | wc -l
date -u +%Y-%m-%dT%H:%M:%SZ

# live per-repo verdict and per-rule census at --round 10
node .ufo/waves/round-9/corpus-gate.mjs --repo kasegi-shokunin --round 10
node .ufo/waves/round-9/corpus-gate.mjs --repo kasegi-shokunin --round 10 --json | sed -n 's/^# json //p' | node -e 'let s="";process.stdin.on("data",d=>s+=d).on("end",()=>{const j=JSON.parse(s)[0];const c={};for(const f of j.findings)c[f.rule]=(c[f.rule]||0)+1;console.log(JSON.stringify(c))})'

# before column, pinned revision
node .ufo/waves/round-9/corpus-gate.mjs --snapshot kasegi-shokunin b7180b0 --round 9

# r4 adjudication (absent at this stamp — the L1 re-runs it after the mirror)
node .ufo/waves/round-10/r4-adjudicate.mjs --live --repo kasegi-shokunin --round 10

# rule-8 sweep over this checkout's corpus, in a form that does not itself spell the banned literal
grep -rnE 'op:[/]{2}' kasegi-shokunin/corpus | wc -l

# this lesson's own rule-8 and rule-2 obligations
grep -cE 'op:[/]{2}|\bsk-|\bghp_|github_pat_|\bxox|\bAKIA|-----BEGIN' corpus/lessons/round-10-aggregator-corpus-verdict.md
grep -cE '\b[Rr]ound[-_ ]?10\b|\.ufo/reports/|LOG\.md' corpus/lessons/round-10-aggregator-corpus-verdict.md
```

**This lesson adds no finding to its own repo.** Measured on a throwaway tree
(`git -C kasegi-shokunin archive HEAD | tar -x -C /tmp/verify10/kasegi-shokunin`, then `git init` + one commit in
`/tmp`, never in the child repo), running `node .ufo/waves/round-9/corpus-gate.mjs --repo /tmp/verify10/kasegi-shokunin
--round 10 --json` before and after copying this file to `corpus/lessons/round-10-aggregator-corpus-verdict.md`:
r2 3→3, r4 49→49, r7 0→0, r8 3→3, and r10 1→0. The only cell that moves is the duty finding this file discharges.
The r7 under-coverage **note** denominator moves 51→52 corpus files (a note, not a finding, by construction —
`corpus-gate.mjs` prints it as `# note … (not a finding)`).