# audit-kaidoku — kaidoku-shokunin at 1170f71 (aggregator round 12)

Verdict: **not conformant** at the named HEAD, by gate exit **1** (failed).
Everything below is revision-bound to `1170f717c4ffeb3d0a9fd24522d8fb42f78fa837`.
All commands used the ORIGINAL lane checkout
`/home/vgpnk/Projects/shokunin/kaidoku-shokunin` (not a worktree). All reads only;
no child write. The gate is read-only by construction.

Census caveat: **no corpus totals are frozen here.** The only counts recorded below are
(a) the gate's own revision-bound finding counts and (b) bounded measurements of the
index/provenance surfaces, both marked provisional until the parent emits
`FINAL LANES READY` (census parser fix for indented Markdown source rows is in progress
elsewhere).

## 1. Revision and cleanliness

```
$ git -C /home/vgpnk/Projects/shokunin/kaidoku-shokunin rev-parse HEAD
1170f717c4ffeb3d0a9fd24522d8fb42f78fa837
$ echo $?
0
$ git -C /home/vgpnk/Projects/shokunin/kaidoku-shokunin status --porcelain
(no output)
$ echo $?
0
```

Working tree clean at the named revision. Committed corpus size (provisional):
`git ls-tree -r --name-only HEAD corpus/ | wc -l` = **107**; `corpus/knowledge/` = 92;
`corpus/lessons/` = 13.

## 2. Gate result

Command (run from the fleet-aggregate worktree, script and lane both absolute):

```
cd /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/fleet-aggregate && \
node .ufo/waves/round-9/corpus-gate.mjs \
  --snapshot /home/vgpnk/Projects/shokunin/kaidoku-shokunin \
  1170f717c4ffeb3d0a9fd24522d8fb42f78fa837 --round 12
```

Observed header/verdict lines (verbatim):

```
# corpus-gate-v1 — CORPUS.md rules recomputed (aggregator lane round 9), round-selector=12
# expect kaidoku-shokunin@1170f71 ABSENT (no committed expected verdict for this revision)
# tree kaidoku-shokunin revision=1170f717c4ffeb3d0a9fd24522d8fb42f78fa837 dirty=0 mode=snapshot
# verdict kaidoku-shokunin failed findings=90 rules=r2,r4,r8,r10,shonen rules-implemented=r2,r4,r7,r8,r10,shonen
# process-exit 1 (failed)
```

Exit `1`. Finding split (parsed from the 90 `CR-kaidoku-shokunin-*` lines and
independently re-checked): **r2 = 3, r4 = 82, r7 = 0, r8 = 1, r10 = 1, shonen = 3.**

Round-selector derivation: the lane's committed `LOG.md` carries
`## 2026-10-19 — arc3-loop1-round12` (LOG.md:1685) and
`corpus/lessons/round-12.md` exists at HEAD, so **round 12** is the relevant lane round.
The default selector is 9 (`--round <N>`, default 9). A second run without `--round`
produced the SAME 90 findings and exit 1; the only textual difference is the r10 finding
(`no corpus/lessons/round-9-aggregator-*.md` instead of `round-12-...`). So the verdict is
selector-insensitive for this lane apart from the r10 lesson name.

`--json` note: `--json` appends a single `# json <array>` line after the human output
(gate lines 960-971); it does not replace the human lines. My first attempt to pure-JSON
parse stdout failed on the header line — that was my wrapper's assumption, not a gate
defect. All counts above come from the human finding lines plus independent re-derivation.

## 3. Rule-by-rule evidence

### r2 — lessons cite round + evidence: 3 findings (CR-kaidoku-shokunin-r2-1..3)

Flagged: `lessons/2026-10-13-round-2.md`, `lessons/2026-10-13-round-3.md`,
`lessons/2026-10-13-round-4.md` (all `#missing-evidence-pointer`).
The implemented test (gate:439) accepts only one of: a bare `\b[0-9a-f]{7,40}\b`,
a `.ufo/reports/` path, or the literal `LOG.md`.

Direct reads (and a per-file pattern test) show:

| lesson | hash-like token | `.ufo/reports/` | `LOG.md` | other evidence |
|---|---|---|---|---|
| 2026-10-13-round-2.md | none | no | no | cites `Evidence: fleet .ufo/waves/kaidoku-r2/*.md` — a real pointer, but a **glob under `.ufo/waves/`, not `.ufo/reports/`**, so the rule misses it |
| 2026-10-13-round-3.md | none | no | no | 2 `ev_` ids (`ev_bf0875fae37e…`, `ev_95ccd1f3…`) — session-scoped ids, not resolvable files/commits |
| 2026-10-13-round-4.md | none | no | no | 2 `ev_` ids (`ev_8efa2368`→`ev_50038b96`) |

Controls: `2026-10-13-round-1.md` (LOG.md), `2026-10-15-round-1.md`
(hash + `.ufo/reports/` + LOG.md), `round-12.md` (`4072ebb`), and
`round-12-verifier-spotcheck.md` (`2a0d6c1`) all pass. So the r2 debt is a frozen
2026-10-13-wave artifact, not current practice. Two of the three (round-3, round-4)
carry **no** resolvable pointer at all; round-2's is a shape mismatch against the
gate's declared pointer forms.

### r4 — count claim on a line with no backticked command: 82 findings (r4-1..82)

This is 91% of the finding mass. I re-read each flagged source line and matched the
gate's own `COUNT_NOUN_RE` against it. Bounded mechanical classification (my heuristic,
not a gate re-score):

- **23/82 are identifier-context artifacts**: the fired substring is the numeric part of
  an identifier. Examples: `corpus/README.md:190` → `"1 entries"` inside `round-1 entries`;
  `knowledge/2026-10-13-r2-doctor-reverify-r2.md:71` → `"2 lanes"` in `round-2 lanes`;
  `knowledge/2026-10-13-r4-07-jsc-bytecode.md:37,60,85,110,138` → `"4 lane"` ×5 in
  `round-4 lane`; `knowledge/2026-10-14-r12-02-queue-b-ledger.md:139` → `"02 pin"` in
  `r4u-02 pin`; `lessons/2026-10-13-round-1.md:18` → `"04 hit"` in `Lane 04 hit`.
- Additional non-claim contexts observed among the other 59: code/schema text
  (`knowledge/2026-10-13-r4u-04-dnfile-il.md:90` → `"24, row"` from
  `token>>24, row = token&0xffffff`; `knowledge/2026-10-14-r11-01-queue-ops.md:131` →
  `"4, column"` from `original_position:{line:4, column:9,...}`;
  `knowledge/2026-10-14-r10-02-queue-ops-2.md:194` → `"185 run"`;
  `knowledge/2026-10-13-r4u-03-unblob-extract.md:11` → `"0 run"` in `binwalk 3.1.0 run`),
  and quoted third-party command output (`"Analyzed 1 file for 85 file signatures"`,
  `"14,417 rows across 17"`, `"At most 20000 fields or enum members..."`).
- **Genuine unbacked count claims remain in the set** — the class the rule targets:
  e.g. `knowledge/2026-10-13-crash-evidence.md:62` (`175 entries / 174 present`),
  `knowledge/2026-10-13-pe-surface.md:9` (`413 files`),
  `knowledge/2026-10-13-r4-05-signal-asar.md:7` (`1,866 entries`),
  `lessons/2026-10-18-wave-dispatch-counting.md:5` (`64 seats`) and `:10` (`60 seat items`).

Density (provisional, not a score): `knowledge/2026-10-14-r12-02-queue-b-ledger.md` 7;
`knowledge/2026-10-14-r14-02-final-sweep.md` 6; five files at 5 each
(`r4-07-jsc-bytecode`, `r4-13-pwntools-persist`, `r4-16-frontier-rescan`,
`r4u-04-dnfile-il`, `r5-02-call-targets-jq`). 47 distinct files carry at least one.

### r8 — credential material on literal text: 1 finding, 5 occurrences

Verbatim: `credential-class kv-secret occurrences=5 lines=5 files=5 owner=lane at 1170f71
literal_shaped=2/5 ... first=knowledge/2026-10-13-r4u-04-dnfile-il.md:88
first4="toke" len=43`.

Independent re-derivation with the gate's exact pattern
`/\b(password|passwd|api[_-]?key|access[_-]?token|auth[_-]?token|token|secret)\s*[=:]\s*\S{8,}/gi`
over all 105 text-extension files under `corpus/`:

- 5 occurrences total, **all with label `token`** (`labels={"token":5}`); no
  password/secret/api_key/access_token/auth_token occurrence anywhere.
- `knowledge/2026-10-13-r4u-04-dnfile-il.md:88` — value 36 chars, literal_shaped false:
  it is the dnfile field name `pe.net.struct.EntryPointTokenOrRva` ("Entry token: ...").
- `knowledge/2026-10-14-r14-02-final-sweep.md:24` — 27 chars, literal_shaped false:
  a coverage-map token.
- `knowledge/2026-10-19-arc3-r10-rust-evidence-id-domain.md:1` — 46 chars, false:
  "coverage-map token".
- `knowledge/2026-10-19-arc3-r8-vyper-optimizer-dispatch-shapes.md:5` — 51 chars, true:
  "Proposed EVM-map token" (`2026…`, a corpus bookkeeping token).
- `knowledge/2026-10-19-arc3-r9-viair-fallback-miss.md:5` — 39 chars, true: same class.

Reconciliation of the shape fields: the gate prints `first4`/`len` of the **raw match**,
so `len=43` = `"token: "` (7) + the 36-char dnfile value; `literal_shaped=2/5` matches the
two literal-shaped bookkeeping tokens. So the finding stands as a literal-text occurrence
(CORPUS.md:43 reads "stay out of every corpus") but the content class is a **naming
collision on the word "token" used for corpus bookkeeping and a .NET field name** — no
identified credential. The gate's own `classification=could-not-evaluate` on this is
correct and I do not upgrade it to a semantic judgment either way.

### r10 — round aggregator lesson absent: 1 finding

`no corpus/lessons/round-12-aggregator-*.md` at 1170f71. Confirmed: no
`round-*-aggregator-*.md` exists under `corpus/lessons/` (listing: 11 `.md` files, none
matching). Under the default selector the finding names round 9 instead. This is the only
part of rule 10 the gate can decide; the rule-10 verdict itself is the `# verdict` line.

### r7 — index rows vs tree: 0 findings, 1 note

Observed note: `r7 under-coverage (not a finding): 106/106 corpus files carry no index row`.

This note is a **naming-convention artifact, not evidence of a missing index**.
`corpus/README.md` indexes entries by extension-less entry name
(`2026-10-13-mcp-registrations`, `2026-10-13-doctor-taxonomy`, …), while the r7 walker
only registers backticked spans ending in a graded extension (`INDEX_EXT_RE`), so `indexed`
stays empty and every file counts as unindexed. Measured directly on the committed README:

- 521 backticked spans; only 17 end in a graded extension.
- 101 distinct extension-less spans resolve to an existing `.md` basename under
  `knowledge/` + `lessons/` (103 `.md` files total).
- Only **2** existing basenames are not named by an extension-less span:
  `round-12.md` and `round-12-verifier-spotcheck.md` — i.e. the index has not been
  extended for the newest round's two lessons.

Because the walker sees zero rows, r7's actual target (a phantom row naming a file that
does not exist) had nothing to bite on; 0 r7 findings cannot be read as "index verified".
Note also the parent's in-progress census parser fix concerns indented Markdown source
rows, which is adjacent to this same naming/shape mismatch — treat any index totals as
provisional.

### shonen — canonical form: 3 findings

Verified by direct read of `SHONEN.md` (HEAD):

1. `SHONEN.md:1` — got `# kaidoku — Promotion checklist`; the gate expects
   `# kaidoku-shokunin — Promotion checklist` because it substitutes the **directory
   basename** as `<name>`. The lane's own self-name is `kaidoku` (used throughout
   PROVINCE/LOG), so this is a naming-convention disagreement at the header, not a missing
   header. Not adjudicated by me.
2. `SHONEN.md:13` — blank line outside header/boxes/evidence.
3. `SHONEN.md:14` — prose: "Correction to box 1, 2026-10-19 (arc3-loop1-round12; appended
   at EOF so the pinned box lines keep their numbers; box-1 text above kept): …".

The four canonical boxes, their `[~]` marks, one indented evidence line per box, and the
trailing newline all pass (no box-count/box-text/mark/evidence/verifier/trailing-newline
findings). The two form findings (2, 3) are one deliberate act: the lane appended an
append-only correction at EOF *precisely to preserve pinned line numbers* — the text says
so itself. That is a real, documented trade-off: correction discipline vs canonical form.
`shonen-semantics` (whether the claims are true) is declared not-evaluated by the gate and
by me.

## 4. SOURCES.md — structural observations (not a gate rule)

**`corpus/SOURCES.md` does not exist at HEAD.**

```
$ git -C /home/vgpnk/Projects/shokunin/kaidoku-shokunin cat-file -e HEAD:corpus/SOURCES.md
fatal: path 'corpus/SOURCES.md' does not exist in 'HEAD'
$ echo $?
128
$ find /home/vgpnk/Projects/shokunin/kaidoku-shokunin -name 'SOURCES.md' -not -path '*/.git/*' | wc -l
0
```

It is nonetheless a **recorded, committed debt** (so this is not an unflagged gap):

- `corpus/lessons/round-12-verifier-spotcheck.md:17`: "Debts carried to round 13:
  create `corpus/SOURCES.md`; give the C1 entry an `S###` source row; disclose the unpaired
  custody legs in the entry."
- `SCORECARD.md:2110` (Planned r13): "Also: create `corpus/SOURCES.md` per sources
  contract v1 (opened rows only; first leads: Ghidra GP-6528 / `GoRttiMapper.java`, RARE,
  Decompile-Diverge, V8-snapshot surface — connector scan, kaika W1 ART dossier)".
- `.ufo/waves/arc3-loop1-round12/integration/records-draft.md:123`: "create
  `corpus/SOURCES.md` per contract v1 — opened rows only, honest tiers, `## Paths` and
  `## Search log`; its capability row enters only if every census command runs clean".

**Therefore no study-path/reading sequence can be extracted from `corpus/SOURCES.md` at
this revision.** The nearest committed artifact names four items but calls them
"first leads"; per the assignment, leads are not evidence, and none of the four is an
opened row. I record the absence rather than invent a sequence.

The directly evidenced reading surfaces that DO exist at HEAD are the index and the
quality bar (section 5), not a SOURCES-style path.

## 5. corpus/README.md and corpus/QUALITY.md observations

- `corpus/README.md` (190 lines) is an index of record, not a reading order: a coverage
  map whose rows are `section | entries | state`, with extension-less entry names, plus
  `.md:line-range` citations inside the state prose. It states "A row is written when its
  file exists, never before." Its last line (190) is the Criterion-5 erratum note, which is
  what the gate flags as r4-1 (`round-1 entries` → identifier artifact).
- `corpus/QUALITY.md` carries **15 admission criteria** (rows 1-15; row 15 supersedes 14;
  row 14 is retained, not deleted — consistent with the file's "replaced by a new row
  naming the row it supersedes, never rewritten") and **6 weak-material signals**
  (21 numbered table rows total). Criterion 6 (cite Evidence ID or exact reproducing call)
  and criterion 13 (`grep -o … | wc -l`, never `grep -c`) are the two most directly
  load-bearing for the r2/r4 finding classes above.

## 6. Provenance frontmatter scan (parent addendum, bounded)

Scope: `corpus/knowledge/**/*.md` — **91 files**, parsed line-wise for
`source:`, `verified-at:`, `recheck:` (the lane uses bullet-style metadata lines such as
`- verified-at: 2026-10-13`, not YAML frontmatter).

Counts: `source:` 455, `verified-at:` 452, `recheck:` 19.
`verified-at:` date distribution: 2026-10-13 ×345, 2026-10-14 ×79, 2026-10-16 ×7,
2026-10-19 ×9, 2026-10-18 ×2, 2026-09-21 ×1, and 9 lines with no date in the value.

**`recheck:` values naming ephemeral roots — 6 of 19 (exact values, trimmed only where
noted):**

1. `corpus/knowledge/2026-10-16-l7-01-inspect-go-binary.md:5` —
   starts `cd /tmp && npm_config_cache=/tmp/kaidoku-luna-round-6-npm-cache TMPDIR=/tmp
   npx -y rea-agents@6.5.0 mcp` (literal `/tmp` scratch).
2. `corpus/knowledge/2026-10-19-arc3-r1-evm-real-solc.md:7` — `mkdir -p
   /var/tmp/cr2-recheck && TMPDIR=/var/tmp/cr2-recheck …`; input carrier is the durable
   original-repo path `/home/vgpnk/Projects/shokunin/kaidoku-shokunin/.ufo/waves/arc3-loop1-round1/…`.
3. `corpus/knowledge/2026-10-19-arc3-r3-evm-optimizer-shapes.md:7` — `/var/tmp/cr3-recheck`,
   same shape.
4. `corpus/knowledge/2026-10-19-arc3-r4-evm-vyper-leg.md:7` — `/var/tmp/r4-recheck`.
5. `corpus/knowledge/2026-10-19-arc3-r6-viair-dispatch-shape.md:12` — `/var/tmp/r6-recheck`.
6. `corpus/knowledge/2026-10-19-arc3-r7-evm-evidence-id-domain.md:5` — `/var/tmp/kaidoku-ex3-r7-recheck`,
   and it also pins a node path inside an npx content-hash cache:
   `/home/vgpnk/.npm/_npx/a1722018f28f9df2/node_modules/rea-agents/scripts/rea.mjs`.

Reading: 1 value is literally `/tmp`; 5 use `/var/tmp/<round>-recheck`. Those five carry
their own rationale inline — "on this host a `/tmp`-defaulted run fails EDQUOT (errno
-122); a disk-backed `TMPDIR` is required" — so the `/var/tmp` choice is deliberate and
documented, but it is still a non-repo scratch root that will not survive host cleanup.
**Zero `recheck:` values point into `.tower/worktrees`.**

`.tower/worktrees` in the whole committed corpus: exactly **one** occurrence —
`corpus/lessons/round-12.md:5`: "kaika W1 STATE dossier
(`/home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/fleet-ledger/.ufo/waves/kaika-w1/kaidoku-state.md` §4)".
That path resolves today (existence check: YES) but it is an ephemeral worktree dossier
cited as prior-round scope, so it is a fidelity risk of the class the parent flagged, in a
lesson rather than knowledge frontmatter.

`source:` resolvability (provisional, bounded to the first absolute path appearing in each
`source:` value): 45 exist, **171 absent**, 239 values contain no absolute path. The
absent set is heterogeneous and must NOT be read as 171 broken citations: it includes
deliberate fixtures (`/nonexistent`), rotated system state
(`/var/lib/systemd/coredump/core.waybar.…zst`, `/var/crash`), and scratch captures
(`/tmp/obsidian-app-analysis.json`, `/tmp/view-*.json`). Of the 455 `source:` values, 169
name `/tmp` scratch output. Historical evidence was left unchanged; this is a fidelity
observation only.

## 7. Gate limitations — explicitly named

Declared by the gate itself (registry `not_evaluated` rows, gate:178-184):

- **Not evaluated: r1** (is a token a source — semantic), **r3** (falsifiable/opinion —
  semantic), **r5** (negative claim carries its sweep — needs negation+proximity),
  **r6** (quote names its location — quoted surface lives outside the repo), **r9**
  (corrections append-only / cross-lane edits — history-dependent; snapshot mode grades a
  `git archive` tree with no history).
- **box-3**: whether an `[x]` rests on a non-author verifier needs the authorship graph of
  past rounds; the form check only sees a verifier-id token. This lane has no `[x]` boxes,
  so the question does not arise here, but the hole is real.
- **shonen-semantics**: whether a box's claim is true — prose, not form.

Observed/inferred behavior limits (mine, from reading the implementation):

- **Snapshot mode loses history**, so r9 and any append-only check are structurally
  unavailable in the exact mode whose verdict names a revision. `dirty=0` is a snapshot
  fact, not a live-tree fact.
- `# expect … ABSENT` means there is **no committed expected verdict** for 1170f71; the run
  is not being compared against a frozen expectation, so exit 3 (drift) could not fire.
- **r8 classification is could-not-evaluate** by design (needs a vault read,
  operator-gated); the occurrence findings stand as literal-text hits only.
- **r4's detector is shape-only** (`COUNT_NOUN_RE` + "line contains no backtick"): it
  fired on 23/82 identifier contexts and on code/schema/quoted-output text (section 3).
  A finding is not proof of an unbacked human count claim.
- **r7's index model requires extension-terminated corpus-relative paths**, so this lane's
  extension-less entry-name index registers as zero rows; 0 r7 findings is not "index
  verified", and the 106/106 note is not a coverage measurement.
- **shonen header label = directory basename**, which differs from the lane's self-name.
- A gate pass/fail is mechanical only: `rules-implemented=r2,r4,r7,r8,r10,shonen` is not
  whole-corpus semantic conformance, and a pass would not prove it either.

## 8. Verdict and what it does not mean

- At `1170f717c4ffeb3d0a9fd24522d8fb42f78fa837`, worktree clean: **not conformant** —
  `corpus-gate-v1 --snapshot … --round 12` exits **1** with **90** findings on
  **r2 (3), r4 (82), r10 (1), shonen (3)** plus the single r8 occurrence finding.
- It does **not** mean the corpus is semantically wrong, that the lessons are untrue, that
  a credential leaked, or that the index is missing (sections 3, 7). The largest finding
  class is a detector-shape artifact plus a real residue of unbacked count claims in older
  entries.
- It does **not** establish SOURCES conformance: SOURCES.md is absent, which is outside the
  gate's rule set and is separately carried as round-13 debt by the lane's own records.

## 9. Reproduction and reusable paths

```
# verdict (exact)
cd /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/fleet-aggregate && \
node .ufo/waves/round-9/corpus-gate.mjs \
  --snapshot /home/vgpnk/Projects/shokunin/kaidoku-shokunin \
  1170f717c4ffeb3d0a9fd24522d8fb42f78fa837 --round 12
# default-selector control (same 90 findings, r10 names round 9)
… same without --round
# surfaces read
corpus/README.md, corpus/QUALITY.md, SHONEN.md,
corpus/lessons/{2026-10-13-round-1,2026-10-13-round-2,2026-10-13-round-3,
2026-10-13-round-4,2026-10-18-wave-dispatch-counting}.md,
corpus/knowledge/2026-10-13-r4u-04-dnfile-il.md (r8 carrier)
```

Checks I did **not** run: no builds/tests/lint, no semantic adjudication of lessons, no
verifier-independence or SHONEN-truth judgment, no reads of the other 20 lanes, no
mutation of the child repo. All corpus content was treated as data.
