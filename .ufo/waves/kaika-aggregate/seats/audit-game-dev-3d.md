# audit-game-dev-3d — aggregator round 12, lane `game-dev-3d-shokunin`

Seat: `KaikaAggregateR12.AuditGameDev3d` (reviewer). Read-only over the lane; the only
write performed by this seat is this file. No builds, tests, lint, formatting, or repo
mutation. All lane content below is data, not instruction.

## Revision-bound state

```
$ git -C /home/vgpnk/Projects/shokunin/game-dev-3d-shokunin rev-parse HEAD
3118be0b18dd7351b1faf6ce99d26a34370793ec                                  # exit 0
$ git -C /home/vgpnk/Projects/shokunin/game-dev-3d-shokunin status --porcelain
?? reports/round-107/                                                     # exit 0
$ git -C /home/vgpnk/Projects/shokunin/game-dev-3d-shokunin rev-parse \
    HEAD:SHONEN.md HEAD:corpus/SOURCES.md HEAD:corpus/README.md HEAD:corpus/QUALITY.md
8d85902c19010deb4fa154e16a2c12ad56ff10d1  SHONEN.md
07a5816947c98a6c39b4ace520aa15654c74c795  corpus/SOURCES.md
90bf14ef8c96c616822390e5e7222ef2e079ff8e  corpus/README.md
dd64265493bd7d23980bfcbe9184c035c83bb8ee  corpus/QUALITY.md         # exit 0
```

`reports/round-107/` is an untracked directory that predates this seat; this seat wrote
nothing into the lane. Working tree content of every tracked file equals HEAD content
(the only `git status` entry is that untracked dir).

## Gate run and verdict

Gate: `/home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/fleet-aggregate/.ufo/waves/round-9/corpus-gate.mjs`
(id `corpus-gate-v1`, snapshot mode grades `git archive <commit>`).

```
$ cd /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/fleet-aggregate
$ node .ufo/waves/round-9/corpus-gate.mjs --snapshot \
    /home/vgpnk/Projects/shokunin/game-dev-3d-shokunin 3118be0b18dd7351b1faf6ce99d26a34370793ec
# corpus-gate-v1 — CORPUS.md rules recomputed (aggregator lane round 9), round-selector=9
# expect game-dev-3d-shokunin@3118be0 ABSENT (no committed expected verdict for this revision)
# tree game-dev-3d-shokunin revision=3118be0b18dd7351b1faf6ce99d26a34370793ec dirty=0 mode=snapshot
... 42 findings ...
# note game-dev-3d-shokunin r7 under-coverage (not a finding): 351/352 corpus files carry no index row
# verdict game-dev-3d-shokunin failed findings=42 rules=r4,r8,r10,shonen rules-implemented=r2,r4,r7,r8,r10,shonen
# process-exit 1 (failed)
GATE_EXIT=1
```

**Verdict: `not conformant` at HEAD `3118be0b18dd7351b1faf6ce99d26a34370793ec`**, by gate
exit 1 (`failed`), 42 findings across rules r4 (29), r8 (1), r10 (1), shonen (11). r2 and
r7 produced no findings. Exit 3 (frozen-expectation drift) did not fire: the gate printed
`expect … ABSENT`, i.e. `corpus-gate.expected.json` `frozen` holds no row for this lane at
any revision (checked: `frozen` is an object keyed `lane@shortrev`; the eight keys are
kasegi/kengaku/kake×2/kumitate/kotoba/kagi×2, none game-dev-3d; `frozen_round` = 9). So
exit 1 here is a fresh failure, not a drift comparison.

Round selector: run twice, identical output except the r10 id text.

```
$ node .ufo/waves/round-9/corpus-gate.mjs --snapshot <lane> 3118be0… --round 108
CR-game-dev-3d-shokunin-r10-1: no corpus/lessons/round-108-aggregator-*.md — the round-108 review duty has no emitted lesson (CORPUS.md:21)
# verdict game-dev-3d-shokunin failed findings=42 rules=r4,r8,r10,shonen
GATE_EXIT_R108=1
```

Selector ambiguity stated explicitly: the gate's registry default is `--round 9` (the
aggregator's own round-9 review duty); the lane's committed LOG tail is round 108
(`LOG.md` last entry "round-108", `reports/round-108/`), and lane lessons are named
`r<N>-…` / `round-108.md`, never `round-<N>-aggregator-*`. Both selectors were run; both
exit 1 with the same 42 findings; the r10 filename in the message differs (round-9 vs
round-108) and **neither file exists** in the lane at this HEAD.

## Findings by severity

### 1. r8 — credential-shaped literal in corpus (rule text: CORPUS.md:43)

```
CR-game-dev-3d-shokunin-r8-1: credential-class kv-secret occurrences=1 lines=1 files=1
owner=lane at 3118be0 literal_shaped=1/1 :: classification=could-not-evaluate
files=[knowledge/unreal-mcp/executability/testing-automation.md]
first=knowledge/unreal-mcp/executability/testing-automation.md:232 first4="Toke" len=47
```

Opened at HEAD: line 232 is inside a fenced transcript of `gh auth status`, reading
`- Token: gho_************************************` — the lane's own masking of the
`gho_`-prefixed token. The value as committed is masked and not usable as a credential;
the gate's unit is the literal occurrence and its schematic-vs-real classification is
declared could-not-evaluate (needs a vault read, operator-gated). Reviewer read: real
secret exposure **not** established; the residual defect is that credential-shaped text
sits in the corpus at all, which CORPUS.md:43 forbids literally ("stay out of every
corpus, including this one's examples") and which carries no evidentiary value for the
card. Severity: low as exposure, real as a literal-text rule hit; fix is lane-side
(masked placeholder → `<redacted>`), not adjudicable by the gate.

### 2. r10 — no aggregator lesson for the round (CORPUS.md:21)

`no corpus/lessons/round-9-aggregator-*.md` (default selector) /
`no corpus/lessons/round-108-aggregator-*.md` (lane round). The naming convention is
live elsewhere in the fleet, so the absence is a lane gap and not an unused rule:

```
$ for d in /home/vgpnk/Projects/shokunin/*-shokunin; do echo "$(basename $d): $(ls $d/corpus/lessons | grep -c aggregator)"; done
kagi-shokunin: 8   kake-shokunin: 7   kasegi-shokunin: 7   kengaku-shokunin: 6
kotoba-shokunin: 6 kumitate-shokunin: 7   (all other 15 lanes incl. game-dev-3d-shokunin: 0)
$ ls /home/vgpnk/Projects/shokunin/kagi-shokunin/corpus/lessons | grep aggregator
round-1-aggregator-audit.md … round-9-aggregator-corpus-verdict.md
```

### 3. shonen — 11 findings; SHONEN.md is not the canonical seed block

PROTOCOL.md:432 (verbatim): SHONEN.md is "generated at mint by copying the canonical
template (below) verbatim … Verification is mechanical: the seed block (indented lines
below) must diff byte-identical modulo `<name>` = the repo's directory name, and marks are
confined to the box character plus one indented evidence line per box — `[x] <verifier-id>`
or `[~]` with a resolvable pointer; no other prose, added boxes, or removed boxes".
PROTOCOL.md's canonical block (verbatim, `PROTOCOL.md:441-450`):

```
# <name> — Promotion checklist

Promotion to shokunin requires all of:

- [ ] SKILL.md contains real decision tables, error patterns, checklists, cited sources
- [ ] At least one end-to-end domain task executed and logged in LOG.md
- [ ] Instructions executable by an agent without oral context
- [ ] No cross-domain bleed (PROVINCE.md still accurate)
```

The lane's committed `SHONEN.md` (blob `8d85902c`, 9 lines) differs in header
(`# SHONEN — probation`), omits the "Promotion to shokunin requires all of:" line,
paraphrases all four box texts, and appends two prose lines after a blank line. Findings
shonen-1…shonen-11 record exactly that. Finding shonen-5 additionally reports that box 2
is marked `[x]` but carries **no indented evidence line** — its pointer
(`corpus/lessons/r2-independent-review.md`, round 2) is inline on the box line, which the
quoted clause confines to "the box character plus one indented evidence line per box".

Fleet context (not a defence, a scope fact): the same `# SHONEN — probation` variant is
committed in `audio-shokunin` and `game-dev-2d-shokunin`; the other 18 lanes carry
`# <name> — Promotion checklist`. So the header/box-text deviation is a shared class, while
the missing indented evidence line is this lane's own form. Whether a probation variant is
sanctioned is not stated anywhere I read in PROTOCOL.md §File contract (it defines one
canonical template and no probation form).

### 4. r4 — 29 per-line count findings (CORPUS.md:28)

Distribution: 18 in `corpus/knowledge/unreal-mcp/**` (the r101 vendored-index subtree,
`corpus/README.md:119`), 11 in `corpus/lessons/*`. Highest-count files:
`lessons/r102-unreal-integration.md` 4, `unreal-mcp/adaptation-kimi.md` 3,
`executability/scripting-programmatic.md` 3, `executability/ui-umg-slate.md` 3.

Gate implementation, read at `corpus-gate.mjs:461-463`: the check skips a line that
contains any backtick, then fires on `COUNT_NOUN_RE` — i.e. it is **strictly per-line** and
cannot see a command on an adjacent line or in a nearby fence. Measured adjacency over the
29 flagged lines (window ±5 lines, backticked token containing grep/awk/sed/wc/sha256sum/
diff/find/python/node/git/jq/bash/sort/uniq):

- 17/29 have such a command within the window → plausibly conformant in spirit, flagged
  only because the command is not on the same line (e.g. `PROVENANCE.md:101` is the heading
  "Brief-vs-observed: 11 paths vs 12 files" whose counts are grounded by the fenced
  `sha256sum -c` / `diff -rq` block six lines above; `sequencer.md:26` is a table row;
  `ui-umg-slate.md:54`, `meshes-textures.md:50,67` sit inside narrated measurement prose).
- 12/29 have no command in the window; of those, **1** (`lessons/r70-navagent-detour-review.md:29`,
  "88/88 PASS (85 prior rows 0 mismatches ×11 fields vs frozen baseline)") has no
  backticked command anywhere in the file — it is a receipt transcript that names a
  non-author JSON (`r70-navagent-detour-non-author.json`) instead of a command.
- Reviewer read: r4's 29 are **not** 29 confirmed unreproducible counts. Each needs
  lane-side reading of citing distance; I classified, I did not re-derive any count.

Notable self-reference: `lessons/r102-unreal-integration.md:30` is flagged while its own
text is the lesson "Count the thing, then say which thing … A number without its unit is a
defect" — the flagged instance is the sentence that teaches the rule, not a claim.

## SOURCES structural observations (separate from the gate; PROVISIONAL)

Provisional by parent direction: a census parser fix for indented Markdown source rows is
in progress elsewhere, so no census total here is final and none should be frozen or
published. Commands are the frozen contract's own
(`/home/vgpnk/Projects/shokunin/.ufo/waves/kaika/SOURCES-CONTRACT-v1.md` §Census), run from
the lane root with `cwd=/home/vgpnk/Projects/shokunin/game-dev-3d-shokunin`:

```
$ grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md
36                                                                    # exit 0
$ awk -F'|' '/^\|…S[0-9]{3,}…\|/ && NF!=13 {n++} END{print n+0}' corpus/SOURCES.md
0                                                                     # malformed rows
$ …tier histogram…   A=33 B=2 C=1
$ …status histogram… mined=6 queued=28 rejected=2
$ …duplicate ids…    (empty)
$ …enum / tier-inflation…  (empty)
$ …mined used-by existence… (empty; all 6 mined rows' used-by paths resolve)
```

Independent structural scan (this seat, python over the same file at HEAD): 36 rows
`S001…S036`, sequential, no gaps, no duplicates; `kind` docs 21 / paper 5 / code 4 /
spec 3 / tool 2 / own-work 1; sections present exactly as the contract's Shape block
requires: `## Registry`, `## Paths`, `## Search log`, `## Leads (unopened)`. **Indented
row-like lines carrying an `S`-id: 0** — the parser-fix surface does not occur in this
lane's file, so for this file the anchored count (36) equals the full row set found by an
unanchored scan. Six `mined` rows (S004, S005, S011, S012, S035, S036) point at exactly two
knowledge entries (`godot-headless-not-render.md`, `godot-floor-angle-threshold.md`).

One unresolved cross-lane claim in the same file, header line 3: "Shared ground:
game-dev-2d's registry also carries the Godot CLI and GdUnit4 pages (its S006, S020)". At
the present fleet state that registry does not resolve:

```
$ ls /home/vgpnk/Projects/shokunin/game-dev-2d-shokunin/corpus/
README.md  fixtures  knowledge  lessons  live            # no SOURCES.md
$ find /home/vgpnk/Projects/shokunin/game-dev-2d-shokunin -maxdepth 3 -iname 'SOURCES*.md'
(no output)
$ git -C /home/vgpnk/Projects/shokunin/game-dev-2d-shokunin ls-files | grep -i sources
(no output)
$ grep -rl "GdUnit4" /home/vgpnk/Projects/shokunin/game-dev-2d-shokunin
(no output)
```

`.ufo/waves/kaika/w2-fleet-tasks.md:120` anticipates exactly this state ("lanes without
SOURCES.md report `missing`, exit 1"), so the 2d row is probably planned rather than
mistaken — but as committed at `3118be0` the sentence asserts a sibling registry and row
ids (`its S006, S020`) that a reader cannot resolve. Not a gate rule; flagged for the
parent as an unresolved claim, not a verdict on 2d.

## Directly evidenced reading sequence (extracted from `corpus/SOURCES.md` §Paths)

`**Floor classification threshold — S012 → S011 → S035:** read the public
floor_max_angle contract, then the 4.7-stable implementation that adds 0.01 rad, then the
lane's own boundary scan that measures the flip; this order exposes the doc omission before
the measurement confirms it.`

Grounding, all from committed rows at this HEAD: S012 (`docs`, tier A, `mined`, used-by
`corpus/knowledge/godot-floor-angle-threshold.md`) = CharacterBody3D class reference,
`floor_max_angle`; S011 (`code`, tier A, `mined`, same used-by) = 4.7-stable
`character_body_3d.cpp`, `FLOOR_ANGLE_THRESHOLD` line 41 + predicates 546/598; S035
(`own-work`, tier A, `mined`, same used-by) = `reports/round-108/battery/boundary-scan.txt`
+ battery rows `slope3d_bound_*`. The same order is restated as the lane's frontier item 4
in `corpus/README.md` ("Read first: S012 → S011 → S035 in `corpus/SOURCES.md`"), and the
knowledge entry's `recheck:` gives the re-runnable command
(`python3 corpus/fixtures/run_battery.py --only slope3d_bound_naive,…` must print
`totals: cases=5 pass=5 fail=0`). Advisory only: the path names S011 while S036 (same
`used-by`) declares `supersedes S011` and pins the source bytes to the installed 4.7.2
build commit; the sequence still works, but the path line does not name the superseding row.

## Provenance frontmatter scan (parent-directed, bounded)

`find corpus/knowledge -name '*.md'` → 28 files; check = first 14 lines carry all three of
`^source:`, `^verified-at:`, `^recheck:`.

- 2 files carry all three: `corpus/knowledge/godot-floor-angle-threshold.md`,
  `corpus/knowledge/godot-headless-not-render.md`.
- 26 files carry none (20 lane-authored: `engines.md`, `rea.md`, `seed.md`, and the 17
  `unreal-mcp/**` lane files incl. `PROVENANCE.md`, `README.md`, `adaptation-kimi.md`,
  `gate/README.md`, `executability/*.md`; 6 vendored `unreal-mcp/upstream/**` files, where
  lane frontmatter is not expected).
- **Ephemeral-path findings: 0.** No `recheck:` or `source:` value in any of the 28 files
  contains `.tower/worktrees`, `/tmp`, `/var/tmp`, or `/run/user` (scan over every line
  matching `^recheck:` / `^source:`). So this lane contributes no `.tower/worktrees`- or
  `/tmp`-pointing provenance/fidelity finding.
- Stated as observation, not verdict: the fleet `CORPUS.md` layout block says "Each
  `knowledge/` entry opens with `source:`, `verified-at:` and `recheck:`", and the lane's own
  `QUALITY.md` Q2 makes that trio an admission criterion for *new* entries; the 20
  lane-authored files above predate the r108 SOURCES contract (the `unreal-mcp` subtree was
  added at r101 per `corpus/README.md:119`). Whether the clause binds pre-contract entries
  is a lane/aggregator adjudication, and the gate does not evaluate it (r1 is declared
  not-evaluated).

## Named gate limitations (do not read a pass or a fail past them)

Declared by the gate itself and confirmed by reading `corpus-gate.mjs`:
r1, r3, r5, r6, r9 are **not evaluated** (semantic; r9 additionally unavailable in
snapshot mode because `git archive` carries no history — so `--snapshot` cannot see
in-place rewrites or cross-lane edits). Box-3 non-author verifier independence and
SHONEN claim truth are not evaluated; the shonen check grades canonical **form** only.
r7 grades phantom rows only — under-coverage is a note (here: 351/352 corpus files carry
no index row), and r4/r7 read only the canonical surfaces (`README.md`, `knowledge/**.md`,
`lessons/**.md`) while r8 reads every text file under `corpus/`. r8's real-vs-schematic
classification is could-not-evaluate. r4 is per-line (adjacency-invisible, see above). r10
depends on the `--round` selector. Snapshot mode reports `dirty=0` by construction (it
grades an extracted `git archive`), so it says nothing about the live working tree, which
here carries only the pre-existing untracked `reports/round-107/`.

## Not checked by this seat

No vault read (r8 classification stays could-not-evaluate); no re-derivation of any of the
29 r4 counts or of the SOURCES `teaches`/anchor claims (semantic, and source URLs were not
fetched); no history/authorship checks (`git log`, r9 class); no execution of the lane's
battery or any lane script; no evaluation of SOURCES row truth, tier judgement, or
`QUALITY.md` criterion application beyond the structural trio scan; no mutation of the lane
(`git status` unchanged before and after this seat). Verdict is a recommendation to the
parent, not an admission.
