# Gate movement — round-10 seat (aggregator lane, part C)

Seat: `gate-movement` (scout). Deliverable: `shokunin:.ufo/waves/round-10/seats/gate-movement.md`.

Part C of the round's axis-move: re-run `shokunin:.ufo/waves/round-9/corpus-gate.mjs` at each lane's
*next landed revision* and report movement per rule. Read-only: no gate file, no fixture, no child
repo, no ledger surface was written; nothing was committed or pushed; no working tree was mutated.

Gate under test — its sha256 is the identity of every number below:

```
cd /home/vgpnk/projects/shokunin
sha256sum .ufo/waves/round-9/corpus-gate.mjs .ufo/waves/round-9/corpus-gate.expected.json
68939d0c70b6dc5ee9e2667b78e2d04e70c9b9b1368d42d3653653932b82cfb8  .ufo/waves/round-9/corpus-gate.mjs
9af28e2e00f8f80256856765a0c692457bdc3f26b893981e96bc000672f2043a  .ufo/waves/round-9/corpus-gate.expected.json
```

Both match the prefixes CONTEXT.md records (`68939d0c70b6dc5ee9e2667b…` / `9af28e2e00f8f80256856765…`),
so the round-9 gate measured here is the gate the L1 baseline was measured with.

Exits seen in this seat: `1` (`failed` — the graded revision violates an implemented rule) many times,
`3` (frozen drift) **never**, `2` (could-not-evaluate) **never**.

## 0. Measured revision set and stamps

The fleet was live and committing throughout this seat's window; every cell below names the revision
**and** the dirty count it measured (`P-s`: an audit cell's identity is the revision it measured).

| stamp | UTC | main `HEAD` | what it measured |
|---|---|---|---|
| A | `2026-09-29T01:52:21Z`–`01:52:22Z` | `2d19a64` | child `HEAD`s; all 8 frozen re-runs (§2); first movement pass (§3) |
| B | `2026-09-29T01:54:36Z` | `3069841` | dirty-file listing, live-worktree runs |
| C | `2026-09-29T02:07:24Z`–`02:07:45Z` | `b5fff81` | re-measurement after `kotoba` and `kagi` advanced |
| D | `2026-09-29T02:09:00Z` | `b5fff81` | final dirty-file listing (§6) |
| E | `2026-09-29T02:09:33Z`–`02:09:34Z` | `b5fff81` | **the frozen set used by §1, §3, §6** for kasegi/kengaku/kake/kumitate/kagi + `kotoba@d6177f4` |
| F | `2026-09-29T02:10:08Z` | `b5fff81` | `kotoba` re-measured at its newest commit (`6d1fbff`) — the `kotoba` row of §3 |

Frozen revision set (§3, §6):

| child repo | measured `HEAD` at stamp | snapshot `--round 9` findings | live `--round 9` findings | dirty / under `corpus/` |
|---|---|---:|---:|---:|
| kasegi-shokunin | `b021dc9` (E) | 55 | 55 | 2 / 2 |
| kengaku-shokunin | `e171cdf` (E) | 28 | 29 | 4 / 2 |
| kake-shokunin | `88a4f4e` (E) | 36 | 36 | 0 / 0 |
| kumitate-shokunin | `637d181` (E) | 40 | 47 | 10 / 5 |
| kotoba-shokunin | `6d1fbff` (F) | 83 | 82 | 1 / 1 |
| kagi-shokunin | `587fda0` (E) | 58 | 58 | 0 / 0 |

Two repos advanced **inside** this seat's own window and one advanced twice — §9.2 records the
superseded revisions with their measured counts, so no measured cell is lost.

## 1. Live revisions and dirty state (step 1)

```bash
cd /home/vgpnk/projects/shokunin
for r in kasegi-shokunin kengaku-shokunin kake-shokunin kumitate-shokunin kotoba-shokunin kagi-shokunin; do
  printf '%s HEAD=%s dirty=%s dirty_corpus=%s\n' "$r" \
    "$(git -C "$r" rev-parse HEAD)" \
    "$(git -C "$r" status --porcelain | wc -l)" \
    "$(git -C "$r" status --porcelain -- corpus | wc -l)"
done
```

Output at stamp E (`2026-09-29T02:09:33Z`), verbatim:

```
kasegi-shokunin HEAD=b021dc925f5cc17702ebff6ffa25c3b6e4efcf7b dirty=2 dirty_corpus=2
kengaku-shokunin HEAD=e171cdfbdb350ee90bfc1c66dac54106a3a5e2ca dirty=4 dirty_corpus=2
kake-shokunin HEAD=88a4f4e2155bbc3ee358c0fc4f50627535056296 dirty=0 dirty_corpus=0
kumitate-shokunin HEAD=637d1815bef717c9275d142fe746e51f68660063 dirty=10 dirty_corpus=5
kotoba-shokunin HEAD=d6177f41afd7034708329d8911a4caf76c9aeca9 dirty=4 dirty_corpus=1
kagi-shokunin HEAD=587fda0470f2b8144618068839997756c65ddde2 dirty=0 dirty_corpus=0
```

`kotoba` re-stamped at F (`02:10:08Z`): `HEAD=6d1fbff… dirty=1 dirty_corpus=1`.

| child repo | live `HEAD` (short) | dirty @E / D | dirty under `corpus/` | round-9 pinned rev(s) (CONTEXT.md) | commits `<pin>..HEAD` @E/F |
|---|---|---:|---:|---|---:|
| kasegi-shokunin | `b021dc9` | 2 | 2 | `b7180b0` | 3 |
| kengaku-shokunin | `e171cdf` | 4 | 2 | `f09ff1f` | 1 |
| kake-shokunin | `88a4f4e` | 0 | 0 | `a209441` (alt `4c9a985`) | 2 (alt 3) |
| kumitate-shokunin | `637d181` | 10 | 5 | `7a099b2` | 3 |
| kotoba-shokunin | `6d1fbff` | 1 | 1 | `63ceba7` | 4 |
| kagi-shokunin | `587fda0` | 0 | 0 | `4b8c018` (alt `4391b3b`) | 3 (alt 4) |

Commit counts (stamp E/F):

```bash
cd /home/vgpnk/projects/shokunin
for k in kasegi-shokunin:b7180b0 kengaku-shokunin:f09ff1f kake-shokunin:a209441 kake-shokunin:4c9a985 \
         kumitate-shokunin:7a099b2 kotoba-shokunin:63ceba7 kagi-shokunin:4b8c018 kagi-shokunin:4391b3b; do
  repo=${k%%:*}; rev=${k##*:}; printf '%s %s count=%s\n' "$repo" "$rev" "$(git -C "$repo" rev-list --count "$rev"..HEAD)"
done
```

Output: `kasegi b7180b0 count=3`, `kengaku f09ff1f count=1`, `kake a209441 count=2`,
`kake 4c9a985 count=3`, `kumitate 7a099b2 count=3`, `kotoba 63ceba7 count=4`,
`kagi 4b8c018 count=3`, `kagi 4391b3b count=4`.

**Which pin is "the" pin.** `git -C <repo> merge-base --is-ancestor <pin> HEAD` returns 0 for all
eight pins (measured). Inside each dual-pin pair the later revision is `a209441` (kake) and `4b8c018`
(kagi):

```bash
for k in kake-shokunin:4c9a985:a209441 kagi-shokunin:4391b3b:4b8c018; do
  repo=${k%%:*}; rest=${k#*:}; old=${rest%%:*}; new=${rest##*:}
  printf '%s %s->%s ancestor=%s\n' "$repo" "$old" "$new" \
    "$(git -C "$repo" merge-base --is-ancestor "$old" "$new" && echo yes || echo no)"
done
```

→ `kake 4c9a985->a209441 ancestor=yes`, `kagi 4391b3b->4b8c018 ancestor=yes`. §3 uses those as the
primary pinned column and reports the earlier pin as a secondary block.

Ghost `corpus/lessons/round-9-aggregator-corpus-verdict.md` in kotoba's worktree: at stamp F kotoba's
live tree carries it **untracked** (`?? corpus/lessons/round-9-aggregator-corpus-verdict.md`) while
its committed tree at `6d1fbff` does not contain it — §9.3.

## 2. Frozen re-run — the 8 committed expectations (step 2)

```bash
cd /home/vgpnk/projects/shokunin
for k in kasegi-shokunin:b7180b0 kengaku-shokunin:f09ff1f kake-shokunin:a209441 kake-shokunin:4c9a985 \
         kumitate-shokunin:7a099b2 kotoba-shokunin:63ceba7 kagi-shokunin:4b8c018 kagi-shokunin:4391b3b; do
  repo=${k%%:*}; rev=${k##*:}
  echo "---- $repo@$rev"
  node .ufo/waves/round-9/corpus-gate.mjs --snapshot "$repo" "$rev" | grep -E '^# (expect|process-exit)'
done
```

Verbatim lines, one key at a time, in `corpus-gate.expected.json` `frozen`'s committed key order
(stamp A):

```
---- kasegi-shokunin@b7180b0
# expect kasegi-shokunin@b7180b0 MATCH exit=1 ids=49
# process-exit 1 (failed)
---- kengaku-shokunin@f09ff1f
# expect kengaku-shokunin@f09ff1f MATCH exit=1 ids=28
# process-exit 1 (failed)
---- kake-shokunin@a209441
# expect kake-shokunin@a209441 MATCH exit=1 ids=37
# process-exit 1 (failed)
---- kake-shokunin@4c9a985
# expect kake-shokunin@4c9a985 MATCH exit=1 ids=34
# process-exit 1 (failed)
---- kumitate-shokunin@7a099b2
# expect kumitate-shokunin@7a099b2 MATCH exit=1 ids=36
# process-exit 1 (failed)
---- kotoba-shokunin@63ceba7
# expect kotoba-shokunin@63ceba7 MATCH exit=1 ids=75
# process-exit 1 (failed)
---- kagi-shokunin@4b8c018
# expect kagi-shokunin@4b8c018 MATCH exit=1 ids=51
# process-exit 1 (failed)
---- kagi-shokunin@4391b3b
# expect kagi-shokunin@4391b3b MATCH exit=1 ids=46
# process-exit 1 (failed)
```

**MATCH 8 / DRIFT 0.** Every run exited `1`; no run exited `3`, so no committed expected verdict is
stale against this tree. The id counts `49 / 28 / 37 / 34 / 36 / 75 / 51 / 46` reproduce the
`expect_findings` lengths committed in `shokunin:.ufo/waves/round-9/corpus-gate.expected.json`
`frozen[*]` (checked with
`python3 -c "import json;d=json.load(open('.ufo/waves/round-9/corpus-gate.expected.json'));[print(k,len(v['expect_findings'])) for k,v in d['frozen'].items()]"`).

The two dual-pin repos both reproduce at **both** revisions, which is what makes them pins: kake 37 at
`a209441` and 34 at its parent `4c9a985`; kagi 51 at `4b8c018` and 46 at its ancestor `4391b3b`
(`git -C kagi-shokunin log --format='%h %an' 4391b3b..HEAD` lists `4b8c018` as a lane commit, so the
46→51 step is the lane's own round-13 landing).

## 3. Movement at each lane's next landed revision (steps 3–4)

Counting command — parses the gate's `# json` line and counts findings by the rule token inside the id
(`CR-kasegi-shokunin-r4-7` → `r4`):

```bash
cd /home/vgpnk/projects/shokunin
count() {  # count <repo-dir> <rev> <round>
  node .ufo/waves/round-9/corpus-gate.mjs --snapshot "$1" "$2" --round "${3:-9}" --json | python3 -c '
import sys,json,re,collections
d=json.loads([l for l in sys.stdin if l.startswith("# json ")][0][7:])
for r in d:
    c=collections.Counter(re.search(r"-(r[0-9]+|shonen)-[0-9]+$",f["id"]).group(1) for f in r["findings"])
    print(r["repo"], r["revision"][:7], "dirty=%s"%r["dirty"], "n=%d"%len(r["findings"]), dict(sorted(c.items())))
'
}
count kagi-shokunin 587fda0 9
```

Output of that single call (stamp E):

```
kagi-shokunin 587fda0 dirty=0 n=58 {'r2': 8, 'r4': 44, 'r8': 4, 'shonen': 2}
```

Pinned side, same command (stamp A; pins cannot move, they are hashes):

```
kasegi-shokunin b7180b0 dirty=0 n=49 {'r10': 1, 'r2': 3, 'r4': 44, 'r8': 1}
kengaku-shokunin f09ff1f dirty=0 n=28 {'r10': 1, 'r4': 25, 'r8': 1, 'shonen': 1}
kake-shokunin a209441 dirty=0 n=37 {'r10': 1, 'r4': 35, 'r8': 1}
kumitate-shokunin 7a099b2 dirty=0 n=36 {'r10': 1, 'r2': 1, 'r4': 33, 'r8': 1}
kotoba-shokunin 63ceba7 dirty=0 n=75 {'r10': 1, 'r4': 61, 'r8': 2, 'shonen': 11}
kagi-shokunin 4b8c018 dirty=0 n=51 {'r10': 1, 'r2': 8, 'r4': 36, 'r8': 4, 'shonen': 2}
kake-shokunin 4c9a985 dirty=0 n=34 {'r10': 1, 'r4': 32, 'r8': 1}
kagi-shokunin 4391b3b dirty=0 n=46 {'r10': 1, 'r2': 8, 'r4': 31, 'r8': 4, 'shonen': 2}
```

`HEAD` side, same command, `--round 9` (stamp E except kotoba, re-run at stamp F):

```
kasegi-shokunin b021dc9 dirty=0 n=55 {'r2': 3, 'r4': 49, 'r8': 3}
kengaku-shokunin e171cdf dirty=0 n=28 {'r4': 25, 'r8': 2, 'shonen': 1}
kake-shokunin 88a4f4e dirty=0 n=36 {'r4': 35, 'r8': 1}
kumitate-shokunin 637d181 dirty=0 n=40 {'r2': 1, 'r4': 38, 'r8': 1}
kotoba-shokunin 6d1fbff dirty=0 n=83 {'r10': 1, 'r4': 69, 'r8': 2, 'shonen': 11}
kagi-shokunin 587fda0 dirty=0 n=58 {'r2': 8, 'r4': 44, 'r8': 4, 'shonen': 2}
```

`dirty=0` is snapshot mode's own stamp: `--snapshot` grades `git archive <rev> | tar -x -C <tmp>`, so
the committed tree is what was graded and the live dirty counts of §1/§6 cannot enter §3's numbers.

`--round 10` at the same revisions (`count "$repo" "$rev" 10`) prints one extra `'r10': 1` everywhere
except kotoba, which shows `'r10': 1` under **both** selectors (its round-9 lesson is absent from the
committed tree, its round-10 lesson does not exist either): totals 56 / 29 / 37 / 41 / 83 / 59.

### 3.1 Movement table (primary pins, `--round 9` on both sides)

`p→h (Δ)`. `—` = the rule produced no id in either run.

| repo | rev pair | r2 | r4 | r7 | r8 | r10 | shonen | total |
|---|---|---|---|---|---|---|---|---|
| kasegi | `b7180b0`→`b021dc9` | 3→3 (0) | **44→49 (+5)** | — | **1→3 (+2)** | **1→0 (−1)** | 0→0 (0) | 49→55 (+6) |
| kengaku | `f09ff1f`→`e171cdf` | 0→0 (0) | 25→25 (0) | — | **1→2 (+1)** | **1→0 (−1)** | 1→1 (0) | 28→28 (0) |
| kake | `a209441`→`88a4f4e` | 0→0 (0) | 35→35 (0) | — | 1→1 (0) | **1→0 (−1)** | 0→0 (0) | 37→36 (−1) |
| kumitate | `7a099b2`→`637d181` | 1→1 (0) | **33→38 (+5)** | — | 1→1 (0) | **1→0 (−1)** | 0→0 (0) | 36→40 (+4) |
| kotoba | `63ceba7`→`6d1fbff` | 0→0 (0) | **61→69 (+8)** | — | 2→2 (0) | 1→1 (0) † | 11→11 (0) | 75→83 (+8) |
| kagi | `4b8c018`→`587fda0` | 8→8 (0) | **36→44 (+8)** | — | 4→4 (0) | **1→0 (−1)** | 2→2 (0) | 51→58 (+7) |
| **fleet** | | 12→12 (0) | **234→267 (+33)** | 0→0 (0) | **12→13 (+1)** | **6→1 (−5)** | 14→14 (0) | **276→300 (+24)** |

† kotoba's r10 moved `1→0→1` inside the window: absent at the pin, landed by the aggregator commit
`0f658ff` (so 0 at `0f658ff`/`0089974`), then **deleted** by the lane commit `d6177f4` (§9.3), so 1 at
`d6177f4` and `6d1fbff`. Both ends of the table read `1`; the intermediate zero is measured and
reported rather than netted away.

Fleet sums: pinned r2 3+0+0+1+0+8 = 12, r4 44+25+35+33+61+36 = 234, r8 1+1+1+1+2+4 = 12,
r10 1×6 = 6, shonen 0+1+0+0+11+2 = 14, total 49+28+37+36+75+51 = 276.
`HEAD` r2 12, r4 49+25+35+38+69+44 = 260, r8 3+2+1+1+2+4 = 13, r10 1, shonen 14,
total 55+28+36+40+83+58 = 300. `276 + (6+0−1+4+8+7) = 300` ✓.

Secondary (earlier) pins, same command:

| repo | rev pair | r2 | r4 | r7 | r8 | r10 | shonen | total |
|---|---|---|---|---|---|---|---|---|
| kake | `4c9a985`→`88a4f4e` | 0→0 (0) | 32→35 (+3) | — | 1→1 (0) | 1→0 (−1) | 0→0 (0) | 34→36 (+2) |
| kagi | `4391b3b`→`587fda0` | 8→8 (0) | 31→44 (+13) | — | 4→4 (0) | 1→0 (−1) | 2→2 (0) | 46→58 (+12) |

### 3.2 Selector effect at the measured `HEAD`s (`--round 9` vs `--round 10`)

| repo | r9 | r10 | added finding |
|---|---:|---:|---|
| kasegi | 55 | 56 | `CR-kasegi-shokunin-r10-1: no corpus/lessons/round-10-aggregator-*.md — the round-10 review duty has no emitted lesson (CORPUS.md:21)` |
| kengaku | 28 | 29 | `CR-kengaku-shokunin-r10-1` — same template, repo label substituted |
| kake | 36 | 37 | `CR-kake-shokunin-r10-1` — same template, repo label substituted |
| kumitate | 40 | 41 | `CR-kumitate-shokunin-r10-1` — same template, repo label substituted |
| kotoba | 83 | 83 | none added: its round-9 lesson is already missing from the committed tree, so the r10 slot is occupied under both selectors (under `--round 10` the same finding names `round-10`) |
| kagi | 58 | 59 | `CR-kagi-shokunin-r10-1` — same template, repo label substituted |

The template is the gate's own string (`corpus-gate.mjs:403`); `corpus-gate.mjs:52-55` fixes it for
round `<R>`. Five repos show the expected in-flight state (round 10's aggregator lesson does not exist
yet, round 9's does); kotoba is the exception, and that exception is the whole point of §9.3.

### 3.3 r7 — the zero row is a check that ran, not a skipped check

Sweep over the 12 pinned/`HEAD` runs:

```bash
cd /home/vgpnk/projects/shokunin
for k in "kasegi-shokunin b7180b0 9" "kengaku-shokunin f09ff1f 9" "kake-shokunin a209441 9" \
         "kumitate-shokunin 7a099b2 9" "kotoba-shokunin 63ceba7 9" "kagi-shokunin 4b8c018 9" \
         "kasegi-shokunin b021dc9 9" "kengaku-shokunin e171cdf 9" "kake-shokunin 88a4f4e 9" \
         "kumitate-shokunin 637d181 9" "kotoba-shokunin 6d1fbff 9" "kagi-shokunin 587fda0 9"; do
  set -- $k
  node .ufo/waves/round-9/corpus-gate.mjs --snapshot "$1" "$2" --round "$3" --json | grep -o 'CR-[A-Za-z-]*-r7-[0-9]*'
done | sort | uniq -c     # empty output = no r7 finding in any run
```

Output: **empty** — no `CR-*-r7-*` id in any of the 12 runs, hence r7 = 0/0 in both columns for all six
repos. That the check executed is visible in the notes and the verdict line:

```bash
node .ufo/waves/round-9/corpus-gate.mjs --snapshot kagi-shokunin 587fda0 --round 9 | grep r7
# note kagi-shokunin r7: 10 backticked path template(s)/glob(s) skipped (contain *, <, {, ~, $ or …)
# note kagi-shokunin r7 under-coverage (not a finding): 13/49 corpus files carry no index row
# verdict kagi-shokunin failed findings=58 rules=r2,r4,r8,shonen rules-implemented=r2,r4,r7,r8,r10,shonen
```

`rules-implemented` lists r7 in every run; `rules=` lists only rules with findings, which is why a
correct reading of the verdict line cannot mistake "r7 implemented, zero findings" for "r7 not
evaluated". The r7 under-coverage notes at the measured `HEAD`s: 25/50 (kasegi), 84/119 (kengaku),
16/34 (kake), 0/48 (kumitate), 3/43 (kotoba at `6d1fbff`), 13/49 (kagi) — reported as `# note`, not a
finding, deliberately (`CORPUS.md:40` makes the phantom row the defect, under-coverage is not).
The **live** kumitate tree is the one place an r7 finding appears in this seat (§6).

## 4. Cited examples — one per nonzero delta (step 4)

Each example is the **full** `text` field of the finding from the same run as its table cell, plus the
`file:line` it points at and the line re-read independently from the graded tree with

```bash
git -C <repo> show <rev>:corpus/<path> | sed -n <line>p
```

(`<path>` relative to `corpus/`, which is the gate's base; verified example in §7 block 6.)

Two r8 examples carry the gate's `first4=` fingerprint field. Where the class is secret-shaped
(`kv-secret`, `bearer`) I withhold that field's four characters and mark it, because the round's
contract forbids propagating credential-shaped material; every other character is the gate's own text.
The `op-ref` lines keep `first4="op:/"` — a scheme prefix, not material, already published at
`shokunin:.ufo/waves/round-9/seats/gate-draft.md:248`.

### 4.1 kasegi r4 44→49 (+5), r8 1→3 (+2) — at `b021dc9`

```
CR-kasegi-shokunin-r4-17: knowledge/source-tree-loss-2026-09-28.md:186 count claim with no backticked command: "against 41 lines) — both are mirror-backed name matches with" (CORPUS.md:28)
CR-kasegi-shokunin-r4-42: lessons/round-15.md:84 count claim with no backticked command: "reported the cross-lane blast radius (339 references across " (CORPUS.md:28)
CR-kasegi-shokunin-r8-1: credential-class kv-secret occurrences=2 lines=2 files=2 owner=lane at b021dc9 literal_shaped=0/2 :: classification=could-not-evaluate (needs a vault read; operator-gated) files=[instruments/density.py,instruments/resolve.py] first=instruments/density.py:52 first4=<4 chars withheld> len=34 (CORPUS.md:43)
CR-kasegi-shokunin-r8-3: credential-class op-ref occurrences=1 lines=1 files=1 owner=lane at b021dc9 maxseg=0 :: classification=could-not-evaluate (needs a vault read; operator-gated) files=[instruments/citation-survival.tsv] first=instruments/citation-survival.tsv:206 first4="op:/" len=5 (CORPUS.md:43)
```

- `git -C kasegi-shokunin show b021dc9:corpus/knowledge/source-tree-loss-2026-09-28.md | sed -n 186p`
  → `against 41 lines) — both are mirror-backed name matches with lost content.`
- `git -C kasegi-shokunin show b021dc9:corpus/lessons/round-15.md | sed -n 84p`
  → `reported the cross-lane blast radius (339 references across 8 lane repos; no`
- New-prose proof: `git -C kasegi-shokunin cat-file -e b7180b0:corpus/knowledge/source-tree-loss-2026-09-28.md`
  **fails** and `… b7180b0:corpus/lessons/round-15.md` **fails** — neither path exists at the pin
  (both are added by `eb5b590`, §5).
- The r8 delta is a class change, not a count wobble: the pin's single r8 finding was
  `CR-kasegi-shokunin-r8-1: credential-class op-ref occurrences=2 lines=2 files=2 owner=aggregator at b7180b0 maxseg=0 :: classification=could-not-evaluate (needs a vault read; operator-gated) files=[lessons/round-5-aggregator-audit.md,lessons/round-6-aggregator-audit.md] first=lessons/round-5-aggregator-audit.md:50 first4="op:/" len=5 (CORPUS.md:43)`,
  and `HEAD` has three: a `kv-secret` class in the lane's new `instruments/*.py`, the aggregator
  `op-ref` class grown 2→6 occurrences over 3 files (third file = the newly landed
  `lessons/round-9-aggregator-corpus-verdict.md`), and a lane `op-ref` in the new
  `instruments/citation-survival.tsv` (`… | sed -n 206p`).
- The 6 r4 findings that left the set are line-shifts in the same files: `CR-kasegi-shokunin-r4-1`
  moves `README.md:83`→`:42`; the pin's `CR-kasegi-shokunin-r4-17`
  (`knowledge/submitted-registry.md:171`) reappears as `CR-kasegi-shokunin-r4-22`
  (`knowledge/submitted-registry.md:217`) — pinned blob 215 lines, `HEAD` blob 223
  (`git -C kasegi-shokunin show <rev>:corpus/knowledge/submitted-registry.md | wc -l`).

### 4.2 kengaku r8 1→2 (+1) — at `e171cdf`

```
CR-kengaku-shokunin-r8-1: credential-class kv-secret occurrences=1 lines=1 files=1 owner=aggregator at e171cdf literal_shaped=0/1 :: classification=could-not-evaluate (needs a vault read; operator-gated) files=[lessons/round-9-aggregator-corpus-verdict.md] first=lessons/round-9-aggregator-corpus-verdict.md:20 first4=<4 chars withheld> len=17 (CORPUS.md:43)
```

Same single-field withholding as §4.1. The pin had exactly one r8 finding —
`CR-kengaku-shokunin-r8-1: credential-class op-ref occurrences=1 lines=1 files=1 owner=aggregator at f09ff1f maxseg=0 :: classification=could-not-evaluate (needs a vault read; operator-gated) files=[lessons/round-5-aggregator-audit.md] first=lessons/round-5-aggregator-audit.md:56 first4="op:/" len=5 (CORPUS.md:43)`
— so the +1 is the `kv-secret` class the newly landed aggregator lesson introduced at
`corpus/lessons/round-9-aggregator-corpus-verdict.md:20`
(`git -C kengaku-shokunin show e171cdf:corpus/lessons/round-9-aggregator-corpus-verdict.md | sed -n 20p`).
kengaku's r4/`shonen` cells are unchanged (25 and 1), i.e. this window's single commit moved the
credential surface and nothing else.

### 4.3 kumitate r4 33→38 (+5) — at `637d181`

All five are net-new (`NEW=5, GONE=0`), in two files that are **absent at the pin**
(`git -C kumitate-shokunin cat-file -e 7a099b2:corpus/knowledge/member-claims-gate.md` fails;
`git -C kumitate-shokunin cat-file -e 7a099b2:corpus/lessons/round-14.md` fails):

```
CR-kumitate-shokunin-r4-2: knowledge/member-claims-gate.md:73 count claim with no backticked command: "would have called 7 rows' sections anchor-less (false — meas" (CORPUS.md:28)
CR-kumitate-shokunin-r4-3: knowledge/member-claims-gate.md:94 count claim with no backticked command: "rebuilt all 19 rows with its own probe — identical verdict, " (CORPUS.md:28)
CR-kumitate-shokunin-r4-4: knowledge/member-claims-gate.md:100 count claim with no backticked command: "- **Topic-form rows stay prose.** The 9 rows above have no m" (CORPUS.md:28)
CR-kumitate-shokunin-r4-29: lessons/round-14.md:17 count claim with no backticked command: "fleet at the file; the census lane then re-derived all 19 ro" (CORPUS.md:28)
CR-kumitate-shokunin-r4-30: lessons/round-14.md:58 count claim with no backticked command: "constants and 1 case had to be re-derived; the one case that" (CORPUS.md:28)
```

Read-back: `git -C kumitate-shokunin show 637d181:corpus/knowledge/member-claims-gate.md | sed -n 73p`
→ `would have called 7 rows' sections anchor-less (false — measured by`; `… | sed -n 94p` →
`rebuilt all 19 rows with its own probe — identical verdict, `;
`git -C kumitate-shokunin show 637d181:corpus/lessons/round-14.md | sed -n 17p` →
`fleet at the file; the census lane then re-derived all 19 rows independently`.

### 4.4 kotoba r4 61→69 (+8) — at `6d1fbff`

`NEW=8, GONE=0` against the pin (measured at `0089974`, whose r4 count is identical to `6d1fbff`'s),
so all eight are newly authored lines in three files the kotoba lane rewrote:

```
CR-kotoba-shokunin-r4-6: knowledge/anatomy-and-compression.md:88 count claim with no backticked command: "lines. Past ~600 lines, split: decision surface stays in SKI" (CORPUS.md:28)
CR-kotoba-shokunin-r4-9: knowledge/checklist-execution-round15.md:248 count claim with no backticked command: "- **33 of 41 boxes are still read by a human.** They are map" (CORPUS.md:28)
CR-kotoba-shokunin-r4-10: knowledge/checklist-execution-round15.md:251 count claim with no backticked command: "89 canonical + 3 fixture files, AGENTS.md-class 7 files)." (CORPUS.md:28)
CR-kotoba-shokunin-r4-27: knowledge/frontmatter-trigger-surface.md:73 count claim with no backticked command: "adds the drift: cache coverage 5/17 → 17/17 rows, so the tru" (CORPUS.md:28)
CR-kotoba-shokunin-r4-29: knowledge/frontmatter-trigger-surface.md:137 count claim with no backticked command: "10. **Verify the render by reproduction, not assumption.** H" (CORPUS.md:28)
```

Read-back at the graded revision:
`git -C kotoba-shokunin show 6d1fbff:corpus/knowledge/anatomy-and-compression.md | sed -n 88p` →
`   lines. Past ~600 lines, split: decision surface stays in SKILL.md, depth goes`;
`git -C kotoba-shokunin show 6d1fbff:corpus/knowledge/checklist-execution-round15.md | sed -n 248p` →
`- **33 of 41 boxes are still read by a human.** They are mapped with reasons, not`;
`git -C kotoba-shokunin show 6d1fbff:corpus/knowledge/frontmatter-trigger-surface.md | sed -n 122p` →
`   catalogue* — coverage is time-varying (5/17 rows at round 7; 17 rows at round`.
All three files exist at the pin (`git -C kotoba-shokunin cat-file -e 63ceba7:corpus/knowledge/<file>`
→ exit 0) and grew (91 / 318 / 155 lines at `HEAD`).

kotoba's r8 cell is 2→2 but its composition changed twice inside the window: at the pin
`CR-kotoba-shokunin-r8-1` was `op-ref occurrences=1 … files=[lessons/round-5-aggregator-audit.md]`,
at `0089974` it was `occurrences=3 … files=[lessons/round-5-aggregator-audit.md,lessons/round-9-aggregator-corpus-verdict.md]`,
and at `6d1fbff` it is back to

```
CR-kotoba-shokunin-r8-1: credential-class op-ref occurrences=1 lines=1 files=1 owner=aggregator at 6d1fbff maxseg=0 :: classification=could-not-evaluate (needs a vault read; operator-gated) files=[lessons/round-5-aggregator-audit.md] first=lessons/round-5-aggregator-audit.md:83 first4="op:/" len=5 (CORPUS.md:43)
CR-kotoba-shokunin-r8-2: credential-class op-ref occurrences=2 lines=2 files=1 owner=lane at 6d1fbff maxseg=0 :: classification=could-not-evaluate (needs a vault read; operator-gated) files=[knowledge/sibling-description-rewrites-round8.md] first=knowledge/sibling-description-rewrites-round8.md:141 first4="op:/" len=5 (CORPUS.md:43)
```

— i.e. the count is flat while the underlying occurrences rose and fell with the aggregator lesson
file's presence in the tree (§9.3).

### 4.5 kagi r4 36→44 (+8) — at `587fda0`

`NEW=20, GONE=12` against the pin. The 12 gone are line-shifts in the same files (e.g.
`drift-gate.md:16`→`:18`, `handler-on-disk-state.md:79`→`:81`, `transcript-hygiene.md:121`→`:123`); the
net `+8` sits in files **absent at the pin** plus newly authored lines:

```
CR-kagi-shokunin-r4-1: knowledge/checklist-execution.md:150 count claim with no backticked command: "8. **The gate echoes a failing row's output** (≤6 lines) — s" (CORPUS.md:28)
CR-kagi-shokunin-r4-27: lessons/round-14.md:28 count claim with no backticked command: "counts cells holding ≥1 stamp token, including cells that al" (CORPUS.md:28)
CR-kagi-shokunin-r4-32: lessons/round-15.md:66 count claim with no backticked command: "14 lanes, one batched call: planner, connector, 2 scouts, sc" (CORPUS.md:28)
CR-kagi-shokunin-r4-3: knowledge/drift-gate.md:18 count claim with no backticked command: "kagi pins verifiable for only 2 of 13 files (the two whose h" (CORPUS.md:28)
```

- `git -C kagi-shokunin cat-file -e 4b8c018:corpus/knowledge/checklist-execution.md` **fails**
  (`190` lines at `HEAD`); `… 4b8c018:corpus/lessons/round-15.md` **fails** (`109` lines at `HEAD`);
  `… 4b8c018:corpus/lessons/round-14.md` **fails**.
- Read-back: `git -C kagi-shokunin show 587fda0:corpus/knowledge/checklist-execution.md | sed -n 150p`
  → `8. **The gate echoes a failing row's output** (≤6 lines) — so every row must be`;
  `git -C kagi-shokunin show 587fda0:corpus/lessons/round-15.md | sed -n 66p` →
  `14 lanes, one batched call: planner, connector, 2 scouts, scribe, 2 executors,`;
  `git -C kagi-shokunin show 587fda0:corpus/knowledge/drift-gate.md | sed -n 18p` →
  `kagi pins verifiable for only 2 of 13 files (the two whose hashes happened to be`.
- File growth at the two revisions: `claim-ledger.md` 374 lines at `4b8c018` → 472 at `587fda0`;
  `drift-gate.md` 199→201; `transcript-hygiene.md` 147→149
  (`git -C kagi-shokunin show <rev>:corpus/<file> | wc -l`).
- kagi's r8 cell is 4→4 with composition drift: lane `op-ref` grew 66→69 occurrences, 22→23 files
  across the window (`CR-kagi-shokunin-r8-4` at `4b8c018` vs at `587fda0`), and the aggregator `op-ref`
  class grew 11→13 occurrences, 4→5 files (the fifth being `lessons/round-9-aggregator-corpus-verdict.md`),
  while the count stayed at 4 findings.

The secondary-pin row (`4391b3b`→`587fda0`, r4 +13) is the same cause over one extra commit
(`4b8c018`, the lane's round-13 landing, whose file list is
`git -C kagi-shokunin log --name-only --format='--- %h %an' 4391b3b..HEAD` — it rewrote `drift-gate.md`,
`handler-on-disk-state.md`, `op-cli-surface.md`, `surface-census.md`, `transcript-hygiene.md` and added
`lessons/round-12.md` / `lessons/round-13.md`).

### 4.6 kake r10 1→0 (−1), and the rest of kake is flat

kake's only nonzero delta is the r10 clearing. r4 stays 35 and r8 stays 1 across `a209441`→`4214101`
→`88a4f4e` even though the lane landed `88a4f4e` (`corpus/knowledge/mirror-pitfalls.md`,
`publish-channels.md`, `publish-queue.md`, `SKILL.md`, `LOG.md`, `SCORECARD.md`): that round's prose
carries its counts with backticked commands and adds no credential-shaped literal. Measured at
`4214101` too (`count kake-shokunin 4214101 9` → 36, r4 35 / r8 1), so the whole window is flat apart
from r10. No citation is owed for a zero delta; the two examples of *id* churn without count change are
`CR-kake-shokunin-r8-1`'s text (the `at <rev>` field moves with the revision).

### 4.7 r10 1→0 (−1) in five repos — one cause, five times

The finding that vanished. Verbatim (present in the six pinned runs; absent at the five `HEAD`s other
than kotoba's):

```
CR-<repo>-r10-1: no corpus/lessons/round-9-aggregator-*.md — the round-9 review duty has no emitted lesson (CORPUS.md:21)
```

(`<repo>` ∈ the six rostered repos; the id is `…-r10-1` in every run, e.g. `CR-kasegi-shokunin-r10-1`,
and the text is one template from `corpus-gate.mjs:403`.)

It cleared because one aggregator commit per repo added exactly
`corpus/lessons/round-9-aggregator-corpus-verdict.md`:

| repo | commit that landed the round-9 lesson | `git -C <repo> log -1 --format=%h -- corpus/lessons/round-9-aggregator-corpus-verdict.md` |
|---|---|---|
| kasegi-shokunin | `b021dc9` (`aggregator-shokunin`, `2026-09-28T22:19:05-03:00`) | `b021dc9` |
| kengaku-shokunin | `e171cdf` (`aggregator-shokunin`, `2026-09-28T22:19:06-03:00`) | `e171cdf` |
| kake-shokunin | `4214101` (`aggregator-shokunin`, `2026-09-28T22:19:06-03:00`) | `4214101` |
| kumitate-shokunin | `93b0567` (`aggregator-shokunin`, `2026-09-28T22:19:06-03:00`) | `93b0567` |
| kagi-shokunin | `baec94f` (`aggregator-shokunin`, `2026-09-28T22:19:06-03:00`) | `baec94f` |
| kotoba-shokunin | `0f658ff` (`aggregator-shokunin`, `2026-09-28T22:19:06-03:00`) — **later deleted** by `d6177f4` (`kotoba-shokunin`, `23:08:46`) | `0f658ff`; `git -C kotoba-shokunin log --diff-filter=D -1 --format='%h %an %s' -- corpus/lessons/round-9-aggregator-corpus-verdict.md` → `d6177f4 kotoba-shokunin round-15: correction — the aggregator's uncommitted corpus file is untracked again` |

Each aggregator commit's diff carries that path and nothing else
(`git -C <repo> log --name-only --format='--- %h %an' <pin>..HEAD`). Existence cross-check:
`git -C <repo> cat-file -e HEAD:corpus/lessons/round-9-aggregator-corpus-verdict.md` → exit 0 for
kasegi/kengaku/kake/kumitate/kagi and **non-zero for kotoba**, whose committed tree lacks it — the
predicate `corpus-gate.mjs:400-404` tests.

## 5. Attribution (step 5)

```bash
cd /home/vgpnk/projects/shokunin
for k in kasegi-shokunin:b7180b0 kengaku-shokunin:f09ff1f kake-shokunin:a209441 kake-shokunin:4c9a985 \
         kumitate-shokunin:7a099b2 kotoba-shokunin:63ceba7 kagi-shokunin:4b8c018 kagi-shokunin:4391b3b; do
  repo=${k%%:*}; rev=${k##*:}
  echo "--- $repo $rev..HEAD count=$(git -C "$repo" rev-list --count "$rev"..HEAD)"
  git -C "$repo" log --format='%h %aI %ae'
done
```

Verbatim output (stamp E/F):

```
--- kasegi-shokunin b7180b0..HEAD count=3
b021dc9 2026-09-28T22:19:05-03:00 aggregator@shokunin.local
0f2dca0 2026-09-28T22:10:19-03:00 jpveigao10@gmail.com
eb5b590 2026-09-28T22:06:22-03:00 jpveigao10@gmail.com
--- kengaku-shokunin f09ff1f..HEAD count=1
e171cdf 2026-09-28T22:19:06-03:00 aggregator@shokunin.local
--- kake-shokunin a209441..HEAD count=2
88a4f4e 2026-09-28T22:52:13-03:00 jpveigao10@gmail.com
4214101 2026-09-28T22:19:06-03:00 aggregator@shokunin.local
--- kake-shokunin 4c9a985..HEAD count=3
88a4f4e 2026-09-28T22:52:13-03:00 jpveigao10@gmail.com
4214101 2026-09-28T22:19:06-03:00 aggregator@shokunin.local
a209441 2026-09-28T21:42:41-03:00 jpveigao10@gmail.com
--- kumitate-shokunin 7a099b2..HEAD count=3
637d181 2026-09-28T22:19:59-03:00 jpveigao10@gmail.com
93b0567 2026-09-28T22:19:06-03:00 aggregator@shokunin.local
dffbf0e 2026-09-28T22:18:45-03:00 jpveigao10@gmail.com
--- kotoba-shokunin 63ceba7..HEAD count=4
6d1fbff 2026-09-28T23:09:58-03:00 kotoba@shokunin.local
d6177f4 2026-09-28T23:08:46-03:00 kotoba@shokunin.local
0089974 2026-09-28T23:07:06-03:00 kotoba@shokunin.local
0f658ff 2026-09-28T22:19:06-03:00 aggregator@shokunin.local
--- kagi-shokunin 4b8c018..HEAD count=3
587fda0 2026-09-28T22:56:34-03:00 jpveigao10@gmail.com
2486643 2026-09-28T22:27:11-03:00 jpveigao10@gmail.com
baec94f 2026-09-28T22:19:06-03:00 aggregator@shokunin.local
--- kagi-shokunin 4391b3b..HEAD count=4
587fda0 2026-09-28T22:56:34-03:00 jpveigao10@gmail.com
2486643 2026-09-28T22:27:11-03:00 jpveigao10@gmail.com
baec94f 2026-09-28T22:19:06-03:00 aggregator@shokunin.local
4b8c018 2026-09-28T21:50:42-03:00 jpveigao10@gmail.com
```

Identity split over the eight windows (`git -C <repo> log --format='%ae' <pin>..HEAD | sort -u`):

| repo | window | `aggregator@shokunin.local` | `jpveigao10@gmail.com` | `<lane>@shokunin.local` |
|---|---|---:|---:|---:|
| kasegi | `b7180b0..HEAD` | 1 (`b021dc9`) | 2 (`0f2dca0`, `eb5b590`) | 0 |
| kengaku | `f09ff1f..HEAD` | 1 (`e171cdf`) | 0 | 0 |
| kake | `a209441..HEAD` | 1 (`4214101`) | 1 (`88a4f4e`) | 0 |
| kumitate | `7a099b2..HEAD` | 1 (`93b0567`) | 2 (`dffbf0e`, `637d181`) | 0 |
| kotoba | `63ceba7..HEAD` | 1 (`0f658ff`) | 0 | **3** (`0089974`, `d6177f4`, `6d1fbff`) |
| kagi | `4b8c018..HEAD` | 1 (`baec94f`) | 2 (`2486643`, `587fda0`) | 0 |

- `aggregator-shokunin <aggregator@shokunin.local>` = the aggregator lane: all six of its commits here
  carry the subject `corpus: round-9 aggregator corpus-verdict lesson (rule-10 re-emitted at <rev>,
  canonical-form + rule-8 literal findings, routed rows)` and change only
  `corpus/lessons/round-9-aggregator-corpus-verdict.md` (`git -C <repo> show --name-only <sha>`).
- `Joao Pedro Veiga <jpveigao10@gmail.com>` = the identity the lane work landed under in four repos.
  Its subjects are lane round work (`round-15: …`, `round-14: …`), and the same string is what
  `PROTOCOL.md:539` names "operator identity" for a lane sweep:
  `git show -s --format='%h %an <%ae>' 46e9ec3` in the main repo → `46e9ec3 Joao Pedro Veiga
  <jpveigao10@gmail.com>` with subject `reports: kumitate round-11 (+ L0 question on the proxy claim
  block)`, the commit that ledger line describes as "kumitate r11, operator identity".
  [INFERENCE] Whether a given one of these commits was typed by the operator or by a lane process
  running under the operator's git identity is **not decidable from the tree**; the identity string,
  timestamp and changed paths are.
- `kotoba-shokunin <kotoba@shokunin.local>` = the kotoba lane's own identity, and it authored the
  three commits `0089974`, `d6177f4`, `6d1fbff` of its window — the only lane-identity authorship in
  any of the eight windows. The other lane identities exist historically
  (`git -C <repo> log -60 --format='%ae' | sort | uniq -c` counts `kengaku@shokunin.local` 3,
  `kake-shokunin@local` 1, `kumitate@shokunin.local` 2, `kagi@shokunin.local` 1,
  `shokunin@local` 1–4 per repo) but authored nothing inside these windows.

Which commit plausibly caused which delta — with the commit that last touched each cited file
(`git -C <repo> log -1 --format=%h -- corpus/<file>`):

| repo | delta | cited finding(s) | file(s) | last-touch | plausible cause |
|---|---|---|---|---|---|
| kasegi | r4 +5 | `CR-kasegi-shokunin-r4-17`, `-r4-42`, `-r4-1` | `knowledge/source-tree-loss-2026-09-28.md`, `lessons/round-15.md`, `README.md` | `eb5b590`, `eb5b590`, `eb5b590` | lane commit `eb5b590` ("round-15: depth re-anchor after PROVINCE-root loss…", `22:06:22-03:00`) added both files and rewrote `README.md`; `0f2dca0` (PROVINCE.md) and `b021dc9` (lesson file only) touch no r4 surface |
| kasegi | r8 +2 | `CR-kasegi-shokunin-r8-1`, `-r8-3` | `instruments/density.py`, `instruments/resolve.py`, `instruments/citation-survival.tsv` | `eb5b590` ×3 | same lane commit `eb5b590` (new `instruments/` files); `b021dc9` fed the existing `op-ref/aggregator` class instead |
| kengaku | r8 +1 | `CR-kengaku-shokunin-r8-1` | `lessons/round-9-aggregator-corpus-verdict.md` | `e171cdf` | aggregator commit `e171cdf`: its line 20 carries the `kv-secret` the gate counts |
| kumitate | r4 +5 | `CR-kumitate-shokunin-r4-2`, `-r4-3`, `-r4-4`, `-r4-29`, `-r4-30` | `knowledge/member-claims-gate.md`, `lessons/round-14.md` | `dffbf0e`, `dffbf0e` | lane commit `dffbf0e` ("round-14: operability — the registry 'yes' claim becomes a gate…", `22:18:45-03:00`) added both files; `93b0567` (lesson file) and `637d181` (LOG/SCORECARD/README) add no r4 finding |
| kotoba | r4 +8 | `CR-kotoba-shokunin-r4-6`, `-r4-9`, `-r4-10`, `-r4-27`, `-r4-29` | `knowledge/anatomy-and-compression.md`, `knowledge/checklist-execution-round15.md`, `knowledge/frontmatter-trigger-surface.md` | `0089974` ×3 | lane commit `0089974` ("round-15: the SKILL.md checklists become executable…", `kotoba@shokunin.local`, `23:07:06-03:00`) rewrote all three; `d6177f4`/`6d1fbff` touch LOG/SCORECARD/`verifiers/` only and leave r4 at 69 |
| kagi | r4 +8 | `CR-kagi-shokunin-r4-1`, `-r4-27`, `-r4-32` | `knowledge/checklist-execution.md`, `lessons/round-14.md`, `lessons/round-15.md` | `587fda0`, `2486643`, `587fda0` | two lane commits: `2486643` added `lessons/round-14.md` (5 findings) and grew `claim-ledger.md` 374→472; `587fda0` added `knowledge/checklist-execution.md` + `lessons/round-15.md` (the +2 over stamp A); `baec94f` added only the lesson file |
| five repos | r10 −1 | `CR-<repo>-r10-1` (gone) | `lessons/round-9-aggregator-corpus-verdict.md` | `b021dc9` / `e171cdf` / `4214101` / `93b0567` / `baec94f` | the aggregator commits of §4.7 |
| kotoba | r10 0 (1→0→1) | `CR-kotoba-shokunin-r10-1` | same | `0f658ff` added, `d6177f4` deleted | §9.3 |

Nothing in any window *repaired* an r4/r8 finding: the gone r4 texts are identical snippets at earlier
line numbers. The deltas are exactly `new − gone` per rule (kasegi 11−6 = +5, kumitate 5−0 = +5,
kotoba 8−0 = +8, kagi 20−12 = +8).

## 6. Dirty trees, and why the gate's mode changes the number

```bash
cd /home/vgpnk/projects/shokunin
for r in kasegi-shokunin kengaku-shokunin kake-shokunin kumitate-shokunin kotoba-shokunin kagi-shokunin; do
  echo "== $r HEAD=$(git -C $r rev-parse --short HEAD) dirty=$(git -C "$r" status --porcelain | wc -l) dirty_corpus=$(git -C "$r" status --porcelain -- corpus | wc -l)"
  git -C "$r" status --porcelain
done
```

Output at stamp D (`2026-09-29T02:09:00Z`), verbatim:

```
== kasegi-shokunin HEAD=b021dc9 dirty=2 dirty_corpus=2
 M corpus/instruments/anchorcheck.py
?? corpus/knowledge/citation-bases.md
== kengaku-shokunin HEAD=e171cdf dirty=4 dirty_corpus=2
 M SKILL.md
 M grader.py
?? corpus/evidence/round12-fleet/
?? corpus/evidence/round12-ladder/
== kake-shokunin HEAD=88a4f4e dirty=0 dirty_corpus=0
== kumitate-shokunin HEAD=637d181 dirty=10 dirty_corpus=5
 M LOG.md
 M SCORECARD.md
 M SKILL.md
 M corpus/README.md
 M corpus/knowledge/executable-scorecard.md
 M scripts/claims-check.mjs
 M scripts/proxy-check.mjs
?? corpus/knowledge/layer-axes.md
?? corpus/knowledge/runtime-remainder-census.md
?? corpus/lessons/round-15.md
== kotoba-shokunin HEAD=d6177f4 dirty=4 dirty_corpus=1
 M LOG.md
 M SCORECARD.md
 M verifiers/corpus-baseline.json
?? corpus/lessons/round-9-aggregator-corpus-verdict.md
== kagi-shokunin HEAD=587fda0 dirty=0 dirty_corpus=0
```

So five of six trees are dirty, and in five of six at least one dirty path is under `corpus/`
(kasegi 2/2, kengaku 2/4, kumitate 5/10, kotoba 1/4 — the untracked aggregator lesson, kagi clean,
kake clean). That matters because the gate grades whatever it is pointed at:

```bash
cd /home/vgpnk/projects/shokunin
for r in kasegi-shokunin kengaku-shokunin kake-shokunin kumitate-shokunin kotoba-shokunin kagi-shokunin; do
  node .ufo/waves/round-9/corpus-gate.mjs --repo "$r" --round 9 | grep -E '^# (tree|verdict)'
done
```

Snapshot (committed tree) vs live (worktree), `--round 9`, same revisions:

| repo | `HEAD` | dirty / corpus | snapshot n | live n | live-only difference |
|---|---|---:|---:|---:|---|
| kasegi | `b021dc9` | 2 / 2 | 55 | 55 | none — counts and composition identical; only the gate's own `at <rev>(worktree)` stamp differs |
| kengaku | `e171cdf` | 4 / 2 | 28 | 29 | +1 r8: `CR-kengaku-shokunin-r8-2` is a `kv-secret` in the untracked `corpus/evidence/round12-fleet/grader_r12_draft.py:2224` (that run's note: `live tree has 42 untracked corpus file(s) — graded as present`) |
| kake | `88a4f4e` | 0 / 0 | 36 | 36 | none (clean tree; only the stamp differs) |
| kumitate | `637d181` | 10 / 5 | 40 | **47** | +1 r7, +6 r4: the untracked `corpus/README.md` edit makes an index row name `lessons/round-16.md` (absent), and the untracked `corpus/knowledge/layer-axes.md:248`, `corpus/knowledge/runtime-remainder-census.md:1/14/572`, `corpus/lessons/round-15.md:66/80` add the six r4 findings |
| kotoba | `6d1fbff` | 1 / 1 | 83 | 82 | **−1 r10**: the worktree carries the aggregator lesson untracked, so the live run counts the round-9 lesson as present while the committed tree does not (§9.3); the aggregator `op-ref` class also reads 1→3 occurrences in live mode |
| kagi | `587fda0` | 0 / 0 | 58 | 58 | none (clean tree; only the stamp differs) |

Live per-rule, same command with `--json` and the §3 counter
(`node … --repo "$r" --round 9 --json`), stamp E/F:

```
kasegi-shokunin   rev=b021dc9 dirty=2  n=55 {'r2': 3, 'r4': 49, 'r8': 3}
kengaku-shokunin  rev=e171cdf dirty=4  n=29 {'r4': 25, 'r8': 3, 'shonen': 1}
kake-shokunin     rev=88a4f4e dirty=0  n=36 {'r4': 35, 'r8': 1}
kumitate-shokunin rev=637d181 dirty=10 n=47 {'r2': 1, 'r4': 44, 'r7': 1, 'r8': 1}
kotoba-shokunin   rev=6d1fbff dirty=1  n=82 {'r4': 69, 'r8': 2, 'shonen': 11}
kagi-shokunin     rev=587fda0 dirty=0  n=58 {'r2': 8, 'r4': 44, 'r8': 4, 'shonen': 2}
```

The one live-only r7 finding of this seat (kumitate):

```
CR-kumitate-shokunin-r7-1: index row names lessons/round-16.md — absent from the graded tree (README.md:67, CORPUS.md:40)
```

and the gate's own live-mode warnings for that run:

```
# note kumitate-shokunin r7: 4 backticked path template(s)/glob(s) skipped (contain *, <, {, ~, $ or …)
# note kumitate-shokunin r7 under-coverage (not a finding): 0/51 corpus files carry no index row
# note kumitate-shokunin live tree has 3 untracked corpus file(s) — graded as present (a snapshot of this commit would not see them)
```

Consequences for reading this file: §3's numbers are **committed-tree** numbers and pair with a
revision; the live numbers carry `dirty=N` and, when >0, the gate's own
`provisional=1 (worktree-only bytes differ from the cited revision)` marker on the `# tree` line. The
two must never be quoted as each other. The L1's `--all` baseline in CONTEXT.md is a worktree
measurement at a different dirty state (`kumitate` 6 dirty there vs 10 here; `kagi` 6 vs 0), which is
why its totals (304 / 310) differ from the snapshot totals above (276 pinned → 300 at the measured
`HEAD`s → 305 with `--round 10`).

## 7. Re-run commands (copy-paste from `/home/vgpnk/projects/shokunin`)

Every block below was executed from `/home/vgpnk/projects/shokunin` while writing this file; none
writes to a child repo or to the main tree (`--snapshot` extracts into `os.tmpdir()` and removes its
tree before exit).

**Block 1 — live revisions and dirty state (§0, §1, §6).**

```bash
cd /home/vgpnk/projects/shokunin
for r in kasegi-shokunin kengaku-shokunin kake-shokunin kumitate-shokunin kotoba-shokunin kagi-shokunin; do
  printf '%s HEAD=%s dirty=%s dirty_corpus=%s\n' "$r" \
    "$(git -C "$r" rev-parse HEAD)" \
    "$(git -C "$r" status --porcelain | wc -l)" \
    "$(git -C "$r" status --porcelain -- corpus | wc -l)"
  git -C "$r" status --porcelain
done
```

**Block 2 — the 8 frozen expectations (§2).**

```bash
cd /home/vgpnk/projects/shokunin
for k in kasegi-shokunin:b7180b0 kengaku-shokunin:f09ff1f kake-shokunin:a209441 kake-shokunin:4c9a985 \
         kumitate-shokunin:7a099b2 kotoba-shokunin:63ceba7 kagi-shokunin:4b8c018 kagi-shokunin:4391b3b; do
  repo=${k%%:*}; rev=${k##*:}
  echo "---- $repo@$rev"
  node .ufo/waves/round-9/corpus-gate.mjs --snapshot "$repo" "$rev" | grep -E '^# (expect|process-exit)'
done
```

**Block 3 — per-rule counts by id token, pinned and `HEAD` (§3).**

```bash
cd /home/vgpnk/projects/shokunin
count() {  # count <repo-dir> <rev> <round>
  node .ufo/waves/round-9/corpus-gate.mjs --snapshot "$1" "$2" --round "${3:-9}" --json | python3 -c '
import sys,json,re,collections
d=json.loads([l for l in sys.stdin if l.startswith("# json ")][0][7:])
for r in d:
    c=collections.Counter(re.search(r"-(r[0-9]+|shonen)-[0-9]+$",f["id"]).group(1) for f in r["findings"])
    print(r["repo"], r["revision"][:7], "dirty=%s"%r["dirty"], "n=%d"%len(r["findings"]), dict(sorted(c.items())))
'
}
for k in "kasegi-shokunin b7180b0" "kengaku-shokunin f09ff1f" "kake-shokunin a209441" "kumitate-shokunin 7a099b2" \
         "kotoba-shokunin 63ceba7" "kagi-shokunin 4b8c018" "kake-shokunin 4c9a985" "kagi-shokunin 4391b3b"; do
  set -- $k; count "$1" "$2" 9
done
for k in "kasegi-shokunin b021dc9" "kengaku-shokunin e171cdf" "kake-shokunin 88a4f4e" \
         "kumitate-shokunin 637d181" "kotoba-shokunin 6d1fbff" "kagi-shokunin 587fda0"; do
  set -- $k; count "$1" "$2" 9; count "$1" "$2" 10
done
```

**Block 4 — the r7 absence sweep over the 12 runs (§3.3).**

```bash
cd /home/vgpnk/projects/shokunin
for k in "kasegi-shokunin b7180b0 9" "kengaku-shokunin f09ff1f 9" "kake-shokunin a209441 9" \
         "kumitate-shokunin 7a099b2 9" "kotoba-shokunin 63ceba7 9" "kagi-shokunin 4b8c018 9" \
         "kasegi-shokunin b021dc9 9" "kengaku-shokunin e171cdf 9" "kake-shokunin 88a4f4e 9" \
         "kumitate-shokunin 637d181 9" "kotoba-shokunin 6d1fbff 9" "kagi-shokunin 587fda0 9"; do
  set -- $k
  node .ufo/waves/round-9/corpus-gate.mjs --snapshot "$1" "$2" --round "$3" --json | grep -o 'CR-[A-Za-z-]*-r7-[0-9]*'
done | sort | uniq -c     # empty = no r7 finding in any run
```

**Block 5 — attribution (§5).**

```bash
cd /home/vgpnk/projects/shokunin
for k in "kasegi-shokunin b7180b0" "kengaku-shokunin f09ff1f" "kake-shokunin a209441" "kake-shokunin 4c9a985" \
         "kumitate-shokunin 7a099b2" "kotoba-shokunin 63ceba7" "kagi-shokunin 4b8c018" "kagi-shokunin 4391b3b"; do
  set -- $k; repo=$1; rev=$2
  echo "--- $repo $rev..HEAD count=$(git -C "$repo" rev-list --count "$rev"..HEAD)"
  git -C "$repo" log --format='%h %aI %ae'
  git -C "$repo" log --format='--- %h %aI %an' --name-only "$rev"..HEAD
  git -C "$repo" log --format='%ae' "$rev"..HEAD | sort -u
done
for r in kasegi-shokunin kengaku-shokunin kake-shokunin kumitate-shokunin kotoba-shokunin kagi-shokunin; do
  echo "== $r identities"; git -C "$r" log -60 --format='%ae' | sort | uniq -c
done
```

**Block 6 — last-touching commit for a cited path, and read-back of a cited line (§4).**

```bash
cd /home/vgpnk/projects/shokunin
git -C kagi-shokunin log -1 --format=%h -- corpus/knowledge/claim-ledger.md
git -C kagi-shokunin show 587fda0:corpus/knowledge/checklist-execution.md | sed -n 150p
git -C kumitate-shokunin show 637d181:corpus/knowledge/member-claims-gate.md | sed -n 73p
git -C kotoba-shokunin show 6d1fbff:corpus/knowledge/anatomy-and-compression.md | sed -n 88p
git -C kasegi-shokunin cat-file -e b7180b0:corpus/knowledge/source-tree-loss-2026-09-28.md; echo "pin-absent exit=$?"
git -C kasegi-shokunin cat-file -e HEAD:corpus/knowledge/source-tree-loss-2026-09-28.md; echo "head-present exit=$?"
git -C kotoba-shokunin cat-file -e 6d1fbff:corpus/lessons/round-9-aggregator-corpus-verdict.md; echo "kotoba-lesson-in-committed-tree exit=$?"
git -C kotoba-shokunin log --diff-filter=D --format='%h %an %s' -1 -- corpus/lessons/round-9-aggregator-corpus-verdict.md
```

**Block 7 — the live-worktree run (§6).**

```bash
cd /home/vgpnk/projects/shokunin
for r in kasegi-shokunin kengaku-shokunin kake-shokunin kumitate-shokunin kotoba-shokunin kagi-shokunin; do
  echo "==== $r"
  node .ufo/waves/round-9/corpus-gate.mjs --repo "$r" --round 9 | grep -E '^# (tree|verdict|process-exit)'
done
```

## 8. Limits — what this file does not decide

- **not-run:** `--selftest` (12/12) and `--registry`. Both are gate commands CONTEXT.md lists; neither
  is in this seat's brief, and neither is needed for a movement cell.
- **Not decided here:** whether any r4 finding is a true violation or a heuristic false positive — part
  B's seat owns that. The +33 r4 movement above is reported as gate output with a cited, re-readable
  line per delta, and no classification.
- **Not decided here:** r8 routing consequence, and whether the `kv-secret`/`bearer`/`op-ref` literals
  are schematic or real. The gate declares that `could-not-evaluate` without a vault read, and this
  file repeats that abstention rather than guessing.
- **Not decided here:** any rule the gate declares not-evaluated (`r1 r3 r5 r6 r9 box-3
  shonen-semantics`, reasons at `corpus-gate.mjs:65-91`). A clean cell in §3 means "no finding under
  the implemented checks", never "CORPUS.md-conformant".
- **Revision risk:** the fleet committed throughout this seat's window (two repos twice, kotoba three
  times). Every cell names its revision; a later re-run at a newer `HEAD` will legitimately differ.

## 9. Mid-round scope change and fleet drift (measured, not assumed)

The L1 sent a scope update at `2026-09-29T01:59:54Z` (main `HEAD` `b5fff81`) listing four facts. Three
are reproduced here by my own commands; one does not match the tree I measured. All measurements below
are mine, at `2026-09-29T02:02:33Z`–`02:10:08Z`.

### 9.1 A seventh lane was minted (`kama-shokunin`)

```bash
cd /home/vgpnk/projects/shokunin
git -C kama-shokunin rev-parse HEAD; git -C kama-shokunin ls-tree -r HEAD --name-only
git -C kama-shokunin status --porcelain
node .ufo/waves/round-9/corpus-gate.mjs --repo kama-shokunin --round 10 | grep -E '^# (tree|verdict|process-exit)'
```

- `kama-shokunin` exists at `9cee9fc01f600dd64b259b0a58af4f85814df586` with **7** tracked paths
  (`AGENTS.md LOG.md MINT.md PROVINCE.md SHONEN.md SKILL.md corpus/README.md`) — `corpus/knowledge/`
  and `corpus/lessons/` are untracked.
- Live gate at my stamp: `# tree kama-shokunin revision=9cee9fc… (worktree) dirty=9 mode=live
  provisional=1`, `# verdict kama-shokunin failed findings=11 rules=r2,r4,r7,r8,r10`, exit `1`; per
  rule by id token: **r2 2, r4 6, r7 1, r8 1, r10 1**. The L1 reported 12 findings (r4 7) at its own
  `02:0xZ` stamp with the same `dirty=9`: the lane was editing between the two stamps, and a live cell's
  identity is revision + dirty count, so both readings can be true. I report mine with its stamp.
- Its `r7` finding is a literal phantom index row, quoted verbatim:
  `CR-kama-shokunin-r7-1: index row names lessons/round-1.md — absent from the graded tree (README.md:18, CORPUS.md:40)`.
- **No snapshot can re-derive that verdict**: `node .ufo/waves/round-9/corpus-gate.mjs --snapshot
  kama-shokunin 9cee9fc --round 10` prints **1** finding (`CR-kama-shokunin-r10-1` only) against the
  live run's 11, because the graded `git archive` tree carries no `corpus/knowledge/` or
  `corpus/lessons/` and the README row that produces r7-1 is an uncommitted worktree edit.
- Scope statement for this file: **every table above is the six repos rostered in `MANIFEST.json` at
  the round-10 cutoff.** kama has no round-9 pinned revision and no entry in
  `corpus-gate.expected.json` `frozen`, so no movement row can exist for it; adding one requires a
  pinned revision and a frozen expectation first, and its corpus is currently untracked.

### 9.2 `MANIFEST.json` — what the mint commit actually changed (divergence)

```bash
cd /home/vgpnk/projects/shokunin
python3 -c "import json;d=json.load(open('MANIFEST.json'));print('rounds_len=',len(d['rounds']));print('roster_len=',len(d['roster']));print([r['id'] for r in d['roster']])"
git show --stat --format='%h %aI %an %s' 2d19a64
```

Measured at `b5fff81`: `rounds_len= 48` (matches the L1's 48), `roster_len= 6`, ids
`['kasegi','kengaku','kake','kumitate','kotoba','kagi']` — **no `kama` roster row**. The word `kama`
appears in `MANIFEST.json` only inside the `rounds[36]` note
(`{round: 11.5, date: 2026-09-28, type: "mint"}`), verbatim:
`sibling-mint allowance landed in PROTOCOL.md Lifecycle; kama-shokunin minted in probation (local model
serving & endpoint health — aggregator mint-eligible r4/r6/r7, demand instances: kagi r3 + kengaku r4
endpoint-drift 8080->34113). Roster row withheld until >=3 verified self-iteration rounds per the new
clause; lane wired into watchdog (m_flash, axes operability+freshness).`
`2d19a64` (`integrator`, `2026-09-28T22:44:21-03:00`) shows `MANIFEST.json | 914 ++++---` and
`PROTOCOL.md | 15 +`, i.e. a reformat plus the probation entry, not a roster row. Reported as measured;
the L1's phrasing ("added `kama` to `MANIFEST.json` `roster`") does not match the file at `b5fff81`.

`git status --porcelain | grep -c '^??'` → **17** untracked paths at `02:02:33Z` (the L1 measured 14 at
its stamp — both are live counts of a still-moving tree). `grep -n shokunin .gitignore` lists only the
six repos (`kasegi-shokunin/` … `kagi-shokunin/`), and `git ls-files kama-shokunin | wc -l` → **0**, so
kama shows as an untracked nested repo in the main tree — both as the L1 stated.

### 9.3 Cross-lane attribution citations I verified (and the kotoba r10 regression)

```bash
cd /home/vgpnk/projects/shokunin
git log --diff-filter=A --format='%h %aI %an' -1 -- .ufo/waves/round-10/CONTEXT.md
git log --diff-filter=A --format='%h %aI %an' -1 -- .ufo/waves/round-9/corpus-gate.mjs
git ls-tree -r a2cac72 --name-only .ufo/waves/round-9 | wc -l
```

→ `fcefcf5 2026-09-28T22:56:28-03:00 protocol-shokunin` (round-10 `CONTEXT.md`);
`6415a9b 2026-09-28T22:29:46-03:00 aggregator-shokunin` (`corpus-gate.mjs`);
`25` (paths under `.ufo/waves/round-9` at `a2cac72`). The third command contradicts the claim that
round-9's wave was uncommitted: at `a2cac72` the round-9 tree was committed, and the gate file was
added at `6415a9b`, before the L1's own cut revision.

**kotoba's round-9 lesson: landed, then deleted.** Measured chain (all in kotoba's own window):

| revision | author | snapshot `--round 9` | `corpus/lessons/round-9-aggregator-corpus-verdict.md` in the committed tree |
|---|---|---:|---|
| `63ceba7` (pin) | `kotoba-shokunin` | 75 (`r10 1`) | absent |
| `0f658ff` | `aggregator-shokunin` | 74 (`r10 0`) | present (added here) |
| `0089974` | `kotoba-shokunin` | 82 (`r4 69`, `r10 0`) | present |
| `d6177f4` | `kotoba-shokunin` | 83 (`r10 1`) | **deleted** (`round-15: correction — the aggregator's uncommitted corpus file is untracked again`) |
| `6d1fbff` (measured `HEAD`) | `kotoba-shokunin` | 83 (`r10 1`) | absent |

and at the same time the **worktree** keeps the file untracked
(`?? corpus/lessons/round-9-aggregator-corpus-verdict.md`, stamp F), so kotoba's live run reports
`r10 0` (82) while its committed tree reports `r10 1` (83). That divergence — a committed-tree rule-10
violation masked in the worktree by an untracked copy of another lane's artifact — is the
snapshot-vs-live trap of §6 in its sharpest form, and it is why this file reports kotoba's r10 row as
`1→1` with the intermediate `0` spelled out rather than netted.

### 9.4 Fleet drift inside this seat's own window (superseded cells, kept)

| repo | revision | stamp | dirty | snapshot `--round 9` |
|---|---|---:|---:|---:|
| kake | `4214101` | A | 6 | 36 (r4 35, r8 1) |
| kotoba | `0f658ff` | A | 11 | 74 (r4 61, r8 2, shonen 11) |
| kagi | `2486643` | A | 12 | 56 (r2 8, r4 42, r8 4, shonen 2) |
| kotoba | `0089974` | C | 0 (snapshot) | 82 (r4 69, r8 2, shonen 11) |
| kotoba | `d6177f4` | E | 4 | 83 (r4 69, r8 2, r10 1, shonen 11) |

All five are measurements with a named revision and dirty count; the §3 table uses the newest measured
revision per repo, so a reader who re-runs at a later `HEAD` should expect legitimate differences, not
drift against this file.