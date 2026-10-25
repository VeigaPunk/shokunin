# Round-9 L1 baseline — measurements the aggregator lane ran itself (not seat-reported)

Author: aggregator L1, round 9. Purpose: the before-column of the round-9 axis-move plus three
measurements no seat was scoped to make. Every cell carries the command that produced it and the
revision it was measured against (`PROTOCOL.md` §Gate standard: *"A verdict names the revision it
was measured against"*). Host: `/home/vgpnk/projects/shokunin`. `grep` here is pi-uu-grep 0.2.0, so
extraction uses `python3`/`awk`.

## 0. Revision stamps — the fleet moved during this wave (three independent stamps)

| Stamp (wall clock) | main | kasegi | kengaku | kake | kumitate | kotoba | kagi |
|---|---|---|---|---|---|---|---|
| ~21:2x -03 (task text written) | `91d0178` | `b7180b0` clean | `f09ff1f` clean | `4c9a985` dirty 5 | `e0e5de1` clean | `3ea0e08` clean | `4391b3b` dirty 20 |
| 2026-09-29T00:47:17Z | `62fdfbe` | `b7180b0` dirty 6 | `f09ff1f` dirty 1 | `a209441` clean | `e0e5de1` dirty 7 | `63ceba7` clean | `4391b3b` dirty 21 |
| ~00:5x Z (this file) | see §0.1 | `b7180b0` dirty 7 | `f09ff1f` dirty 1 | `a209441` clean | `7a099b2` clean | `63ceba7` dirty 2 | `4b8c018` clean |

Command: `date -u +%Y-%m-%dT%H:%M:%SZ; git rev-parse --short HEAD; for d in kasegi kengaku kake
kumitate kotoba kagi; do git -C $d-shokunin rev-parse --short HEAD; git -C $d-shokunin status
--porcelain | wc -l; done`

**4 of 6 child repos changed HEAD inside one wave** (kake `4c9a985`→`a209441`, kotoba
`3ea0e08`→`63ceba7`→dirty 2, kumitate `e0e5de1`→`7a099b2`, kagi `4391b3b`→`4b8c018`), and main moved
at least twice (`91d0178`→`62fdfbe`). Consequence, and the round-9 methodological move: **a
fleet-wide cutoff timestamp cannot be the identity of a cell.** Round 8 stamped every table to one
cutoff (`2026-09-28T23:46:28Z`) and then had to disclose that main HEAD moved three times inside the
wave and that kasegi's report landed two minutes after its own cutoff (§13.7). This refresh every
verdict cell names its revision; the wall-clock stamp is a reading time, not the measured tree.
Routed as proposal **P-s**.

Measured cost of not doing this, inside this wave: three sibling seats reported three different kagi
`op://` counts — 53 (`git -C kagi-shokunin grep -n 'op://' HEAD -- corpus/ | wc -l`, matching
**lines**, at `4391b3b`), 54 (substring **occurrences**, at `4391b3b`), 55 (worktree-inclusive) — and
the L1's own measurement at `4b8c018` gives 75 lines / 77 occurrences / 26 files. All four numbers
are correct for their own unit-and-revision pair; none is comparable to another (§1).

### 0.1 Volatile cells re-measured while writing this file

| Cell | Value | Command |
|---|---|---|
| `MANIFEST.json` `rounds` entries | 30 at 21:2x -03 → 36 at ~00:5xZ | `python3 -c "import json;print(len(json.load(open('MANIFEST.json'))['rounds']))"` |
| `.ufo/l0-questions.md` | 11 lines, sha256 `6ca2a358cbfcdfff50ea27ba73a322843cfee049b9214849a523646ffce1e15f`, clean vs HEAD (protocol committed it at `df1b2c6`), 0 answer markers | `wc -l`; `sha256sum`; `git status --porcelain .ufo/l0-questions.md`; `grep -c 'ANSWER\|L0 answer\|operator:'` → 0 (exit 1) |
| `.ufo/waves/round-12/` tracked | 116 files (protocol r12's gate/closure evidence is durable; `closure-check.py` + `fixtures/` + `frozen/` + `mutants/` included) | `git ls-files .ufo/waves/round-12 \| wc -l` |
| committed corpus gate before this round | **0** | `git ls-files \| grep -c 'corpus-gate'` → 0; `find . -name '*corpus-gate*' -not -path './.git/*'` → empty before the wave |

## 1. Rule-8 (`op://`) counts with a declared unit, revision and authorship

Unit = **occurrences** of the literal substring `op://` in tracked files under `corpus/` at the named
revision; lines and file counts given too, because the fleet's three divergent numbers were a unit
confusion. Scanner (read-only, landed bytes only — `git show <rev>:<path>`, never the worktree):

```python
# python3, run from /home/vgpnk/projects/shokunin
import subprocess
for r in ["kasegi","kengaku","kake","kumitate","kotoba","kagi"]:
    repo=r+"-shokunin"
    h=subprocess.run(["git","-C",repo,"rev-parse","--short","HEAD"],capture_output=True,text=True).stdout.strip()
    files=subprocess.run(["git","-C",repo,"ls-tree","-r","--name-only",h,"corpus/"],capture_output=True,text=True).stdout.split()
    lines=occ=0; hits=[]
    for f in files:
        b=subprocess.run(["git","-C",repo,"show",f"{h}:{f}"],capture_output=True).stdout.decode('utf-8','replace')
        c=b.count("op://")
        if c: occ+=c; hits.append((f,c)); lines+=sum(1 for l in b.split("\n") if "op://" in l)
    print(r,h,len(files),lines,occ,len(hits),hits[:6])
```

| Repo | Revision | corpus files scanned | lines | **occurrences** | files with hits | hit files (owner) |
|---|---|---|---|---|---|---|
| kasegi | `b7180b0` | 42 | 2 | 2 | 2 | `lessons/round-5-aggregator-audit.md`, `lessons/round-6-aggregator-audit.md` (**aggregator**) |
| kengaku | `f09ff1f` | 119 | 1 | 1 | 1 | `lessons/round-5-aggregator-audit.md` (**aggregator**) |
| kake | `a209441` | 34 | 2 | 2 | 2 | `lessons/round-5-aggregator-audit.md`, `lessons/round-6-aggregator-audit.md` (**aggregator**) |
| kumitate | `7a099b2` | 46 | 1 | 1 | 1 | `lessons/round-5-aggregator-audit.md` (**aggregator**) |
| kotoba | `63ceba7` | 44 | 3 | 3 | 2 | `knowledge/sibling-description-rewrites-round8.md` (2, **kotoba**), `lessons/round-5-aggregator-audit.md` (1, **aggregator**) |
| kagi | `4b8c018` | 48 | 75 | 77 | 26 | lane-owned `knowledge/*` + `corpus/drift-pins.sh` (**kagi**; its province *is* vault ops) |

**Finding (self-defect, this lane).** In **5 of 6** repos every literal `op://` hit except kotoba's
two lives in a file **this lane authored** (`round-5-aggregator-audit.md`,
`round-6-aggregator-audit.md`). `CORPUS.md:43-46` anticipated exactly that: *"Secret values, session
tokens, cookies, and vault ref paths (`op://…`) stay out of every corpus, **including this one's
examples**."* Yet refresh 4 graded rule 8 *"Clean everywhere, verified not assumed"* (§11.1, ledger
line 624) on the interpretation that such hits are "prose/schematic placeholders". So the fleet's
dominant rule-8 offender is the auditor's own lessons, and the auditor ruled itself clean.

Classification of the hits (sampled, never printing a value): all are schematic or sweep-pattern
text — e.g. kagi `corpus/knowledge/handler-on-disk-state.md` *"Verified clean: the committed TSVs
contain 0 `op://` refs"*, `corpus/drift-pins.sh:22` *"plus op:// refs) is pinned by mode+lines only"*,
kagi `janitor-command-surface.md:17` describing the `refs` verb. No resolvable vault item/field path
was demonstrated by any seat. Grade therefore: **FAIL-literal / PASS-intent** per repo, with the
literal-vs-intent conflict routed to the integrator (amend rule 8 to distinguish a secret value from
a pointer to one, or strike the quoted sweep patterns in future entries — rule 9 forbids rewriting
the existing ones). Deciding `real-vault-path` vs `schematic` mechanically would need a vault read,
which is operator-gated → the gate declares that sub-check `could-not-evaluate`.

## 2. `SHONEN.md` canonical-form conformance — 0/6 measured before, 6/6 measured now

`PROTOCOL.md` §File contract: the seed must diff byte-identical modulo `<name>`, and *"marks are
confined to the box character plus one indented evidence line per box — `[x] <verifier-id>` or `[~]`
with a resolvable pointer; no other prose, added boxes, or removed boxes"*. Checker (corrected —
the L1's first pass compared each box body to a **prefix** of the canonical text and reported a
phantom verifier-id deviation on all 24 boxes; that bug is recorded here so the corrected numbers are
not confused with it):

```python
# python3 — canonical-form check; deviations printed per repo
import re
BOX=["SKILL.md contains real decision tables, error patterns, checklists, cited sources",
     "At least one end-to-end domain task executed and logged in LOG.md",
     "Instructions executable by an agent without oral context",
     "No cross-domain bleed (PROVINCE.md still accurate)"]
# require: lines[:4] == ["# <name> — Promotion checklist","","Promotion to shokunin requires all of:",""]
# then exactly 4 '^- \[(.)\] (.*)$' lines whose text == BOX[i] exactly and char in 'x~ ',
# each optionally followed by at most one '^\s+\S' evidence line, nothing else, trailing newline;
# marked box requires its evidence line; '[x]' requires a <verifier-id> token on the mark line.
```

| Repo | marks (boxes 1–4) | evidence lines per box | deviations | Canonical form |
|---|---|---|---|---|
| kasegi | `[ ] [ ] [ ] [ ]` | 0/0/0/0 | none | **clean** (trivially: nothing marked) |
| kengaku | `[~] [~] [x] [~]` | 1/1/1/1 | box 3 `[x]` carries **no `<verifier-id>`** on the mark line | deviates (1) |
| kake | `[ ] [ ] [ ] [ ]` | 0/0/0/0 | none | **clean** (trivially) |
| kumitate | `[ ] [ ] [ ] [ ]` | 0/0/0/0 | none | **clean** (trivially) |
| kotoba | `[~] [~] [~] [~]` | 10/5/13/1 | 8 non-box prose lines at 38–45 ("Verifier note: …"), 25 evidence lines beyond the one-per-box allowance | deviates (9) |
| kagi | `[x] [x] [x] [x]` | 1/1/1/1 | no trailing newline; `[x]` marks carry **no `<verifier-id>`** | deviates (2) |

**Fleet consequence, measured:** of the 6 `[x]` marks in the fleet (kengaku box 3, kagi boxes 1–4),
**0 carry the `<verifier-id>` the canonical form requires** — so no `[x]` in the fleet is
form-conformant, including kengaku's box 3, whose *evidence line* does name a genuine non-author
(*"tested 2026-09-28T23:31–23:33Z at HEAD `0c51208` by the aggregator's non-author cold run
(`corpus/lessons/round-8-aggregator-box3-coldrun.md`, aggregator-committed `06cdc98` + amendment
`d8f2898`)"*). That **partly falsifies** round 8's residual as written — *"No `SHONEN.md` box-3 line
names a resolvable non-author verifier yet"* (§13.7, line 1440): 1 of 6 now names one in its evidence
line (kengaku), while 0 of 6 satisfy the mark-line form. kagi's `[x]` marks name only
lane-dispatched seats (`KagiR10Reviewer`, `R11ScoutGates`), which `PROTOCOL.md` counts as the lane →
not non-author. kotoba **downgraded its own** box 3 from `[x]` to `[~]` at round 13 for exactly that
reason (its evidence line: *"the round-12 `[x]` rested on `ReviewSHONEN` (lane-dispatched)"*) — the
rule working as intended, in a lane, unprompted.

## 3. Before-column for the round-9 axis-move (corpus review)

| # | Metric | Before (measured now, commands below) |
|---|---|---|
| V1 | repos whose rule-10 verdict is measured at a revision that still exists as their HEAD | **0 / 6** — §11.1's audited HEADs are ancestors 6–17 commits back: kasegi `fb9ac8e` 6 behind `b7180b0`; kengaku `f147a27` 7 behind `f09ff1f` (`1bd17ec` 4); kake `dd4eabf` 7 behind `a209441`; kumitate `7a4c9a0` 14 behind `7a099b2` (`31f09cd` 10); kotoba `8e22a41` 17 behind `63ceba7`; kagi `e64e81b` 6 behind `4b8c018`. All exist, all ancestors (verified, not assumed) |
| V2 | committed re-runnable corpus-conformance gate | **0** (`git ls-files \| grep -c 'corpus-gate'` → 0) |
| V3 | box-3 verdicts resting on a provisional (worktree-only) grade | **3** — ledger §13.7 line 1437: *"3 of 6 box-3 verdicts are provisional (kasegi, kake, kagi)"* |
| V4 | `SHONEN.md` files measured against the canonical form | **0 / 6** (no prior measurement exists in the ledger; §11.2's D-11/D-28 rows graded two files' *seed* only, at round 6) |
| V5 | repos whose rule-8 grade rests on the literal text at a named revision | **0 / 6** — §11.1 graded rule 8 clean fleet-wide on an inherited interpretation |
| V6 | `SHONEN.md` `[x]` marks carrying the required `<verifier-id>` | **0 / 6** (§2) |
| V7 | lane reports in the sweep window citing a round-8 aggregator artifact | 3 of 12 window reports (`round-12/kagi.md`, `round-12/kumitate.md`, `round-14/kasegi.md`) + kengaku's `SHONEN.md` box-3 evidence line → **4 consumption sites**, so round 8's falsification condition (*"the round ends with 0 lanes citing a round-8 verdict"*) is **not** met — the round-8 move survives |
| V8 | ledger queue keys: distinct / max / next free | 116 `^\| D-` definition rows, 118 distinct keys mentioned, max `D-120`, next free **`D-121`**; 14 keys appear in more than one row (status-movement rows across refreshes, not collisions); L1 cross-check of the distiller seat's tally |

Commands for V1 (per repo, `<h>` = the §11.1 audited hash):

```
git -C <repo> cat-file -e <h>^{commit}; echo $?                                  # existence
git -C <repo> rev-list --count <h>..HEAD                                          # commits behind
git -C <repo> merge-base --is-ancestor <h> HEAD; echo $?                          # ancestry
```

Commands for V3/V7/V8: `grep -n 'provisional' .ufo/reports/AGGREGATE.md | wc -l` → 18 mentions, the
operative statement at line 1437; `grep -rl 'round-8-aggregator\|AGGREGATE.md\|ledger §13\|round-8/aggregator'
.ufo/reports/round-1[2-9]/*.md`; `python3 -c "import re,collections;t=open('.ufo/reports/AGGREGATE.md').read();…"`.

## 4. CORPUS.md rule numbering — verified against the file, and the gap it exposes

`awk 'NR==18||NR==19||NR==20||NR==21||NR==28||NR==33||NR==36||NR==40||NR==43||NR==47||NR==55{printf "%d: %.90s\n",NR,$0}' CORPUS.md`
reproduces the mapping in `.ufo/waves/round-9/CONTEXT.md` line for line (1 `knowledge/` cites a
source, 2 `lessons/` cite round+evidence, 3 falsifiable-or-opinion, 4 a count carries its command,
5 a negative claim carries its sweep, 6 a quote names its location, 7 an index row is a claim,
8 no credential material, 9 corrections are new entries, 10 a verdict per repo; L21 is the unnumbered
aggregator-duty bullet).

**Defect (owner integrator/operator, sev 3):** `CORPUS.md` does not number its own rules, but every
verdict this ledger has ever emitted cites a number (*"not conformant — 4, 5, 7, 9 (contested), 1/6"*,
§11.1). A non-author cannot re-derive which bullet "rule 4" is without this table, and two
independent numbering schemes are one edit apart from diverging (the first four bullets vs the seven
added at round 1/2 make an off-by-one trivially available). Routed: number the bullets in
`CORPUS.md` (operator-side file), or adopt this table as the canonical mapping by reference from
`PROTOCOL.md` §File contract's `corpus/` row. Until then the mapping above is published here and in
`.ufo/waves/round-9/CONTEXT.md` so any reader can resolve a verdict.
