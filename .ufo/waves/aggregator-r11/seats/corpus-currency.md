# Seat: corpus-currency (aggregator-r11) — corpus-review standing duty, minimal

**Stamp: all live measurements below executed at `2026-09-29T03:26:01Z`–`2026-09-29T03:27:50Z` (UTC); main-repo HEAD `8afbc8fe8750e330bf74abd8a03d88a9e30b8b3c`.** Every command is copy-paste runnable from the main repo root.

**Scope discipline.** This is the *standing* corpus-review duty, not the round axis-move (mint/dormancy is the move). I did **not** run `corpus-gate.mjs` (presence check only, per brief). I did **not** open the mint/dormancy verdicts beyond the cross-check note in §5 — no keys proposed there either.

## 0. Local rule definitions (state them, so the table is falsifiable)

No N is defined by any fleet document I could find for "verdict older than N commits" — §14.2 of the ledger only went as far as *"0/6 current"*. I therefore **define material staleness, not a raw commit count**, because a raw count is provably wrong for this fleet (kengaku's only post-verdict commit is the **aggregator's own** verdict lesson; kotoba's round-15 commits include pointer-repairs of an aggregator file):

- `lane` = commits in `<verdict-rev>..HEAD` whose `%ae` does **not** contain `aggregator` (the contract's author filter, applied to verdict currency — commit-age cells must exclude aggregator-authored seat commits).
- **`fresh`** = `lane` = 0 → the measured revision is still the newest *lane* state; the verdict's subject has not moved.
- **`stale-minor`** = `lane` ≥ 1 but 0 lane commits touching `corpus/` or `LOG.md`.
- **`stale-material`** = ≥ 1 lane commit touching `corpus/` or `LOG.md` → the verdict describes a corpus that no longer exists at HEAD.

Bounded round-token scan (per §12.1 correction 3, `awk '$1<=99'`) is used in §5; unbounded token scans are contaminated (`kake` → "round 2026", `kumitate` → "round 42").

## 1. Verdict-staleness table (6 pre-kama child repos)

Round-9 verdict revisions are the ones published in `.ufo/reports/AGGREGATE.md` §14.2 — all six matched the brief's list exactly (`sed -n '1550,1555p' .ufo/reports/AGGREGATE.md`).

Command (one line, produces every numeric cell below for a given repo):

```bash
for l in kasegi kengaku kake kumitate kotoba kagi; do h=$(git -C ${l}-shokunin rev-parse HEAD); echo "== $l HEAD=$h"; git -C ${l}-shokunin rev-list --count <verdict-rev>..HEAD; git -C ${l}-shokunin log --format='%ae' <verdict-rev>..HEAD | grep -vc aggregator; git -C ${l}-shokunin log --format='%ae' <verdict-rev>..HEAD -- corpus/ | grep -vc aggregator; git -C ${l}-shokunin log --format='%ae' <verdict-rev>..HEAD -- LOG.md | grep -vc aggregator; done
```

| repo | verdict rev (r9) | HEAD (03:26Z) | commits behind | of which lane | lane commits touching `corpus/` | lane commits touching `LOG.md` | verdict age (h, at 03:27:14Z) | **stale flag** |
|---|---|---|---|---|---|---|---|---|
| kasegi | `b7180b0` | `b021dc925f5cc17702ebff6ffa25c3b6e4efcf7b` | 3 | 2 | 1 | 1 | 3.64 | **stale-material** |
| kengaku | `f09ff1f` | `e171cdfbdb350ee90bfc1c66dac54106a3a5e2ca` | 1 | **0** | 0 | 0 | 3.20 | **fresh** |
| kake | `a209441` | `ab87a485bb5a118eb7d8c99b4b2c866af6f18ee2` | 3 | 2 | 2 | 2 | 2.74 | **stale-material** |
| kumitate | `e0e5de1` | `f9f8e4deb13019315981f46b021813634bb9beb3` | 9 | 8 | 5 | 7 | 3.18 | **stale-material** |
| kotoba | `63ceba7` | `d85982db069bf1871b7f7f735fb979688c2ee289` | 9 | 8 | 5 | 4 | 2.71 | **stale-material** |
| kagi | `4391b3b` | `587fda0470f2b8144618068839997756c65ddde2` | 4 | 3 | 3 | 3 | 3.80 | **stale-material** |

**Totals: 6/6 revisions still ancestors of HEAD · 0/6 re-measured this refresh · 1/6 `fresh` (kengaku) · 5/6 `stale-material`.**

Ancestry proof for all six (all `yes`):

```bash
for p in "kasegi b7180b0" "kengaku f09ff1f" "kake a209441" "kumitate e0e5de1" "kotoba 63ceba7" "kagi 4391b3b"; do set -- $p; git -C $1-shokunin merge-base --is-ancestor $2 HEAD && echo "$1 yes" || echo "$1 NO"; done
```

### 1.1 The one genuinely notable cell: kengaku

`f09ff1f..e171cdf` = **one commit, authored by `aggregator-shokunin`** (`corpus/lessons/round-9-aggregator-corpus-verdict.md`, 34 lines, authored `2026-09-28T22:19:06-03:00`). Kengaku produced **no lane commits at all** between its verdict revision and its HEAD. A raw commit-count staleness read (which the brief's naive `rev-list --count` produces) flags kengaku "1 behind"; under the contract's own author filter it is the **only current verdict of the six**. Whoever re-keys the table should not put a non-zero "commits behind" in front of the operator for kengaku without this line.

### 1.2 What actually moved in the 5 stale repos (names of the drift, so the next refresh can judge materiality)

```bash
git -C <repo> log --format='%h %aI %s' <verdict-rev>..HEAD
```

- **kasegi** — `eb5b590` round-15 depth re-anchor after `~/Projects/bounties` loss; `0f2dca0` round-15 late PROVINCE annotation; + aggregator lesson `b021dc9` (= **HEAD**). Interacts with the r9 verdict's rules 1/3 failures (740/782 unresolvable path citations): the lane has since committed `corpus/instruments/`. Worktree additionally dirty (see §1.3).
- **kake** — `88a4f4e` round-15, `ab87a48` round-16 (freshness 9→10; claim sweep 160 → 117 HOLD/15 STALE/7 UNVERIFIABLE); + aggregator lesson `4214101`. Touches `corpus/knowledge/freshness-pins.json`, `corpus/lessons/round-1-aggregator-audit.md`, `scripts/freshness-sweep.mjs`.
- **kumitate** — 8 lane commits, rounds 13-close through round-16 fixups (`ed991d0`…`f9f8e4d`); + aggregator lesson `93b0567`. Includes the pre-pinned `7a099b2` that §14.2 recorded as "the repo advanced mid-measurement".
- **kotoba** — 8 lane commits (`0089974`…`d85982d`), including `911b870`/`b25f37a` "restore + index the aggregator's committed corpus lesson" and two baseline re-records — i.e. the r9 verdict's rule-7 under-coverage reading (40 indexed / 43 tracked) has been actively re-baselined.
- **kagi** — `2486643` round-14, `587fda0` round-15 (operability axis-move, credential-hygiene checklist → executed declaration, 34-case selftest); + aggregator lesson `baec94f`. The r9 verdict's surviving failures (rule 4, rule-8-literal) sit on exactly the surfaces this drift touches.

### 1.3 Worktree dirt at stamp (verdicts are claims about a tree; the trees are not clean)

```bash
for l in kasegi kengaku kake kumitate kotoba kagi kama; do printf "%-9s mod=%s untracked=%s total=%s\n" "$l" "$(git -C ${l}-shokunin status --porcelain | grep -c '^ M\|^M')" "$(git -C ${l}-shokunin status --porcelain | grep -c '^??')" "$(git -C ${l}-shokunin status --porcelain | grep -c .)"; done
```

| repo | modified | untracked | total dirty |
|---|---|---|---|
| kasegi | 27 | 2 | **29** |
| kengaku | 2 | 3 | 5 |
| kake | 2 | 0 | 2 |
| kumitate | 1 | 0 | 1 |
| kotoba | 0 | 0 | 0 |
| kagi | 0 | 0 | 0 |
| kama | 1 | 0 | 1 |

kasegi's §14.2 parenthetical read *"worktree r15 dirty 6–7 → provisional"*; at this stamp it is **dirty 29**, and **`LOG.md` itself is one of the dirty files** (see §5). kotoba and kagi are now byte-clean, which retires the "landed clean at stamp; later worktree dirty 2–9" caveat for kotoba.

Any rule-10 verdict re-emitted this refresh must name the revision *and* the worktree state, or it is measuring a tree the reader cannot reconstruct.

## 2. kama corpus assessment (minted lane, round 1)

```bash
ls kama-shokunin/corpus/                       # README.md + knowledge/ + lessons/
git -C kama-shokunin ls-files | head -30
git -C kama-shokunin ls-files 'corpus/*.md' | wc -l    # 13
grep -c '^| `' kama-shokunin/corpus/README.md          # 12 index rows
git -C kama-shokunin log --format='%h %aI %an %s'      # 9cee9fc seed, c6199a2 round-1
```

**Corpus exists and is non-empty: 13 tracked `corpus/*.md` (README + 7 knowledge + 5 lessons), 0 non-md corpus files.** A minted lane with *no* corpus would owe a rule-10 verdict immediately; that contingency does **not** fire for kama. HEAD `c6199a2542440db77d69918599e5a378ee116337` (`kama-shokunin round-1: operability axis`, `2026-09-28T23:15:05-03:00`), MINT.md present, 2 commits total.

| CORPUS.md requirement (layout, L14-21) | observed | verdict |
|---|---|---|
| `corpus/README.md` index | present, 2395 B | ✓ |
| `corpus/knowledge/` domain facts | 7 files | ✓ |
| `corpus/lessons/` training lessons | 5 files | ✓ |
| rule 7 — "an index row is a claim" | index rows 12 = tracked corpus md minus README **12** (exact bijection, verified by row list vs `ls-files`) | ✓ at HEAD |
| rule 8 literal — `op://` occurrences | `grep -rno 'op://' kama-shokunin/corpus/ \| wc -l` → **0** | ✓ clean |
| rule 1 — knowledge cites a source | sampled: `consumer-registry.md` 56 path/command-bearing lines, `listener-census.md` 68, `endpoint-identity.md` 13 | ✓ sampled (not gate-run) |
| rule 4 — a count carries its command | 6 count-sites; all 6 observed adjacent to their producing command, e.g. `consumer-registry.md:234` `"# 310 lines total"` sitting on the `ss -tanp > /tmp/ssa.txt; grep …` block; `listener-census.md:100/186/251/342/373` row counts inline with `sudo -n ss -ltnp` / `ss -ltn` | ✓ sampled |
| rule 2 — lessons cite round **and** evidence | `round-1.md` (2 hashes, 2 dates, 3 round-words) and `round-1-citations.md` (3 hashes, 1 report pointer) cite; **`round-1-critic.md`, `round-1-safety.md`, `probe-mutation-matrix.md` carry 0 commit hashes and no report pointer** (`probe-mutation-matrix.md:3` says only *"re-verified on 2026-09-28"*) | **partial — 3/5 lessons version-less** `[moderate]`; needs the gate to confirm, my matcher is heuristic |

**Two live-artifact findings (both checkable, both minor):**

1. **Registry TSV has no trailing newline at HEAD** — D-72-class (kotoba's D-72 precedent, closed there):
   ```bash
   git -C kama-shokunin show HEAD:registry/endpoint-consumers.tsv | awk 'END{print NR}'   # 43
   git -C kama-shokunin show HEAD:registry/endpoint-consumers.tsv | wc -l                 # 42
   ```
   43 content lines (31 comments + header + 11 data rows), last byte `r`, no terminating `\n`. The **row count itself is honest**: 11 data rows = `grep -vE '^\s*(#|$)' | wc -l` 12 minus the header line (the file's own header comment declares "the 'id' header row is skipped"), consistent with `registry_rows_evaluated=11` in `LOG.md:21`.
2. **Round-1 close evidence is HEAD-true but not worktree-true** — the flagship artifact has an uncommitted 26/3-line delta:

   | artifact | `LOG.md`/`SCORECARD.md`/`SKILL.md` claim | at HEAD `c6199a2` | worktree at stamp |
   |---|---|---|---|
   | `tools/kama-probe.sh` | 788 lines, md5 `932ea3dc365e066e740731cf6a939506` | 788 lines (`wc -l`), md5 `932ea3dc…` — **claim MATCHES** | 811 lines, md5 `e53e6fcbb1196509056eb9e678fc2dc0`, `git diff --stat` 26 insertions/3 deletions |

   ```bash
   md5sum kama-shokunin/registry/endpoint-consumers.tsv   # 87eb156b7cc36e98f3cbfb37c00f5351 == LOG.md:14 claim ✓
   git -C kama-shokunin show HEAD:tools/kama-probe.sh | md5sum   # 932ea3dc… ✓
   md5sum kama-shokunin/tools/kama-probe.sh                      # e53e6fcb… (worktree, dirty)
   ```
   Mode claim verified: worktree `755`, git index `100755`. **Not a falsification** — the count/hash claims reproduce at the named revision; it is a currency fact (kama round 2 is live and the artifact is mid-edit uncommitted, the D-129 durability class this lane has itself filed against).

**Rule-10 verdict owed:** yes, and note the mint hole from the round-9 verbatim query:

```bash
python3 -c "import json;m=json.load(open('MANIFEST.json'));print([r['id'] for r in m['roster']], len(m['rounds']))"
# ['kasegi','kengaku','kake','kumitate','kotoba','kagi'] 48
```

Kama is absent from `roster`, so the r9 "6/6 verdicts" set does not cover it **by construction** — the round-9 corpus-review axis moved past the exact lane that postdates it. Proposed routable text (L1 assigns any key; I propose none): *"kama-shokunin is a corpus-bearing lane (13 tracked `corpus/*.md`) dispatched at round 1 and 2 with no rule-10 verdict in any ledger refresh, and no `minted` record in `MANIFEST.json` (roster = 6). The standing tables must carry a 7th corpus-review row keyed to the lane's own rounds, not to the roster."*

## 3. Frozen-snapshot gate presence (not run)

```bash
ls -la .ufo/waves/round-9/; git ls-files .ufo/waves/round-9/ | wc -l; git status --porcelain .ufo/waves/round-9/ | grep -c .
sha256sum .ufo/waves/round-9/corpus-gate.mjs .ufo/waves/round-9/corpus-gate.expected.json
git log -1 --format='%h %aI %an %s' -- .ufo/waves/round-9/corpus-gate.mjs
node --version
```

| check | result |
|---|---|
| `.ufo/waves/round-9/corpus-gate.mjs` exists | yes, 46236 B, `-rwxr-xr-x` (executable bit intact) |
| still committed | **yes** — tracked (`git ls-files` returns the path); blob at HEAD is **byte-identical** to the worktree (`git diff --quiet HEAD -- .ufo/waves/round-9/corpus-gate.mjs` → clean) |
| tracked files in the frozen dir | **25** — 4 top-level (`CONTEXT.md`, `corpus-gate.mjs`, `corpus-gate.expected.json`, `l1-baseline.md`) + 15 seat files + 6 lessons; 0 uncommitted entries in the dir |
| last commit touching the gate | `6415a9b` `2026-09-28T22:29:46-03:00` aggregator-shokunin (the refresh-7 commit), i.e. the gate has not been touched since the r9 verdict set |
| `sha256` for later re-verification | gate `68939d0c70b6dc5ee9e2667b78e2d04e70c9b9b1368d42d3653653932b82cfb8` · expected `9af28e2e00f8f80256856765a0c692457bdc3f26b893981e96bc000672f2043a` |
| Node available | **`v24.19.0`** (`node --version`) — the gate could run; **not run** per brief |

## 4. Aggregator-identity commits since round 9 (cutoff `2026-09-29T01:21:29Z`)

```bash
git log --author='aggregator' --oneline --since='2026-09-29T01:21:29Z'
for l in kasegi kengaku kake kumitate kotoba kagi kama; do echo "== $l"; git -C ${l}-shokunin log --author='aggregator' --oneline --since='2026-09-29T01:21:29Z'; done
```

**Main repo — 3 commits, all the round-9 tail (nothing newer):**

| commit | authored | files | content |
|---|---|---|---|
| `6415a9b03e1d6c8a2b0679e1dbb80876218e31ea` | `2026-09-28T22:29:46-03:00` | 29 | round-9 ledger refresh 7 (`AGGREGATE.md` +436, `SCORECARD.md` +79/-19, `LOG.md` +82, `.ufo/l0-questions.md` +1, the whole `.ufo/waves/round-9/` snapshot incl. gate + expected) |
| `cc6d9d434cc664ac3ea0a20ea26bd7a31ff6b0e6` | `2026-09-28T22:34:10-03:00` | 2 | round-9 aggregator lane report (`round-9/aggregator.md` 201 lines) + `AGGREGATE.md` §14.18 addendum (+29) |
| `a2cac727986f1053c591ef9ef779548476d517cb` | `2026-09-28T22:35:27-03:00` | 1 | round-9 connector seat durability commit (+20/-2) |

**Child repos — 0 aggregator-authored commits since the cutoff, 7/7.** But the round-9 verdict lessons landed **~2 minutes before** it, and they are the newest aggregator writes in every child repo:

```bash
git -C <repo> log -1 --author='aggregator' --format='%h %aI %s'
```

| repo | last aggregator commit | authored | file (tracked) | bytes | = HEAD? |
|---|---|---|---|---|---|
| kasegi | `b021dc9` | `22:19:05-03:00` | `corpus/lessons/round-9-aggregator-corpus-verdict.md` | 5398 | **yes (HEAD)** |
| kengaku | `e171cdf` | `22:19:06-03:00` | same path | 5172 | **yes (HEAD)** |
| kake | `4214101` | `22:19:06-03:00` | same path | 2351 | no |
| kumitate | `93b0567` | `22:19:06-03:00` | same path | 2419 | no |
| kotoba | `0f658ff` | `22:19:06-03:00` | same path | 4059 | no |
| kagi | `baec94f` | `22:19:06-03:00` | same path | 2437 | no |
| kama | **none** | — | — | — | n/a (no aggregator commit exists in kama at all) |

Two consequences worth carrying: (a) for kasegi and kengaku, **HEAD *is* an aggregator-authored commit**, so any commit-age/ownership cell measured without the author filter attributes the aggregator's own lesson write to the lane; (b) the child-repo aggregator lessons are 2.4–5.4 KB (all real, none marker-grade) and would each count as the aggregator's per-repo round-9 corpus-review artifact if a later refresh ever needs to re-derive that.

Non-aggregator activity since the same cutoff, for contrast: main `0`; kasegi `0`, kengaku `0`, kake `2`, kumitate `4`, kotoba `8`, kagi `2`, kama `2`.

## 5. Cross-check for the dormancy re-key (advisory — L1 assigns keys; I propose none)

The contract's LOG token scan is specified as `^#{2,3} Round [0-9]+` (case-sensitive heading). **Measured literally, that pattern matches 9 lines in kotoba's `LOG.md` and 0 lines in every other repo** — the other five lanes write round entries as date-prefixed bullets, and kama writes a *lowercase* heading:

```bash
for l in kasegi kengaku kake kumitate kotoba kagi kama; do printf "%-9s bullet=%-3s headUpper=%-3s headLower=%-3s\n" "$l" "$(grep -cE '^- [0-9]{4}-[0-9]{2}-[0-9]{2} — round [0-9]+' ${l}-shokunin/LOG.md)" "$(grep -cE '^#{2,3} Round [0-9]+' ${l}-shokunin/LOG.md)" "$(grep -cE '^#{2,3} round [0-9]+' ${l}-shokunin/LOG.md)"; done
```

| repo | bullet-form entries | `## Round N` | `## round N` | effective last round (bounded, `awk '$1<=99'`, **committed** LOG) |
|---|---|---|---|---|
| kasegi | 16 | 0 | 0 | **15** (worktree LOG = 17 — dirty, see below) |
| kengaku | 16 | 0 | 0 | 11 |
| kake | 16 | 0 | 0 | 16 |
| kumitate | 17 | 0 | 0 | 16 |
| kotoba | 8 | 9 | 0 | 16 (mixed form) |
| kagi | 18 | 0 | 0 | 16 |
| kama | **1** | 0 | **1** | **1** |

`grep -nE '^#{2,3} Round [0-9]+|^#{2,3} round [0-9]+' kama-shokunin/LOG.md` → only `7:## round 1 — operability axis (measured via freshness)`. **Under the published regex kama's LOG reads as zero round activity — a fresh post-mint lane that would score as never-active.** This is the same class as §12.1 correction 1 (self-defect 9: "`## Round 10` never matches"); the pattern needs per-repo form detection before kama enters any dormancy pair.

Second caveat: **kasegi's `LOG.md` is dirty at stamp** — its committed max round is 15, the worktree carries round 16 and 17 entries (`grep -nE '^- … — round [0-9]+' kasegi-shokunin/LOG.md | tail -2` → `:517` r15, `:684` r17). Any LOG-counter cell read from the worktree attributes uncommitted rounds; read the committed blob (`git -C kasegi-shokunin show HEAD:LOG.md`) or name the dirt.

## 6. Could-not-evaluate / limits

- **Rule 2 for kama** — `could-not-evaluate` as a *verdict-grade* cell: my matcher (hash/report-pointer regex) is heuristic; the archived `corpus-gate.mjs` is the arbiter and I was instructed not to run it. Reported as a sampled `[moderate]` finding, not a defect grade.
- **Rule 3/5/6 for kama** (falsifiable-or-opinion, negatives carry sweeps, quotes name locations) — not measured; they need the gate. My brief was the *minimal* standing sweep; the deep per-rule matrix is a gate run, which is r9-frozen and was out of scope.
- **Verdict staleness threshold N** — no fleet document defines N; I replaced the raw count with a stated materiality rule (§0) rather than inventing an integer.
- **Volatile**: every number above is a statement about revisions and worktrees at `2026-09-29T03:26:01Z`–`03:27:50Z`; lanes are live (kama round 2 in flight, kotoba/kasegi worktrees dirty), so the staleness table expires within hours — the commands are the durable artifact.