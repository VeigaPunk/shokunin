# audit-mado — mado-shokunin gate + SOURCES audit (aggregator round 12)

- Seat: `KaikaAggregateR12.AuditMado`
- Measured: 2026-10-19 ~20:44–20:52 −03 (host `date` at 20:45:20 −03 observed mid-run)
- Lane (original path, not a worktree): `/home/vgpnk/Projects/shokunin/mado-shokunin`
- Exact revision: `e3e6a8e6ca493e250fb357343816a88e844c4c63` (`master`)
- Instrument: `/home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/fleet-aggregate/.ufo/waves/round-9/corpus-gate.mjs`
  (+ `.ufo/waves/round-9/corpus-gate.expected.json`), gate id **corpus-gate-v1**
- Instrument digest: `e7d49942017a8c522e2b16f3de78e60d16a23ffad6838396a8c44897c12299c3` (sha256, `sha256sum` on that path)
- Runtime: `node --version` → `v24.21.0`
- Axes named: (1) gate conformance at a named revision, (2) SOURCES structural truth,
  (3) study-path usability, (4) repo identity / commit-read feasibility after the jj
  migration, (5) provenance frontmatter fidelity.
- No numeric score is emitted. This note is a recommendation, not an admission.

## Verdict

**`not conformant` at `e3e6a8e6ca493e250fb357343816a88e844c4c63`.**

Failed rule IDs from the gate: **r4, r8, r10** (80 + 1 + 1 = 82 findings). Gate process exit **1**
(`failed`). The verdict is identical under the default selector (`--round 9`) and under the
lane's own committed round (`--round 12`); only the r10 finding's round number changes.

## Commands and observed outputs

### Identity / cleanliness

```
$ git -C /home/vgpnk/Projects/shokunin/mado-shokunin rev-parse HEAD
e3e6a8e6ca493e250fb357343816a88e844c4c63
$ git -C /home/vgpnk/Projects/shokunin/mado-shokunin status --porcelain
(no output, zero lines)                                   EXIT=0
$ git -C ... rev-parse --abbrev-ref HEAD
master
$ git -C ... log -1 --format='%H%n%ci%n%s'
e3e6a8e6ca493e250fb357343816a88e844c4c63
2026-10-19 19:49:12 -0300
round-12 verifier spot-check (integrator, kaika): non-author admit/reject sample + adjudication
$ git -C ... status --porcelain | wc -l
0
$ git -C ... diff --stat HEAD                              (empty) EXIT=0
$ git -C ... ls-files --others --exclude-standard | wc -l
0
```

Note on authorship of HEAD: the tip commit is integrator-authored (subject above), and
`.git/logs/HEAD`'s last record is `e1d81d4… -> e3e6a8e… merge kaika/round: Fast-forward`.
A verdict taken here is therefore a verdict on an integrator-landed revision, not on a
lane-authored tip.

### Gate run — default selector (round 9)

```
$ cd /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/fleet-aggregate
$ node .ufo/waves/round-9/corpus-gate.mjs --snapshot \
    /home/vgpnk/Projects/shokunin/mado-shokunin \
    e3e6a8e6ca493e250fb357343816a88e844c4c63
```

Observed header and tail (verbatim):

```
# corpus-gate-v1 — CORPUS.md rules recomputed (aggregator lane round 9), round-selector=9
# expect mado-shokunin@e3e6a8e ABSENT (no committed expected verdict for this revision)
# tree mado-shokunin revision=e3e6a8e6ca493e250fb357343816a88e844c4c63 dirty=0 mode=snapshot
...
CR-mado-shokunin-r8-1: credential-class kv-secret occurrences=1 lines=1 files=1 owner=lane at e3e6a8e literal_shaped=0/1 :: classification=could-not-evaluate (needs a vault read; operator-gated) files=[knowledge/walker-deep.md] first4="toke" len=15 (CORPUS.md:43)
CR-mado-shokunin-r10-1: no corpus/lessons/round-9-aggregator-*.md — the round-9 review duty has no emitted lesson (CORPUS.md:21)
# note mado-shokunin r7: 4 backticked path template(s)/glob(s) skipped (contain *, <, {, ~, $ or …)
# note mado-shokunin r7 under-coverage (not a finding): 5/32 corpus files carry no index row
# note mado-shokunin r8 kv-secret/lane file-list: knowledge/walker-deep.md
# note mado-shokunin r8 classification=could-not-evaluate (exit-2-class abstention; never guessed) — the literal-text occurrence findings above stand as failed (CORPUS.md:43 reads "stay out of every corpus, including this one's examples")
# note mado-shokunin extracted with: git archive e3e6a8e6ca493e250fb357343816a88e844c4c63 | tar -x -C <tmp>
# verdict mado-shokunin failed findings=82 rules=r4,r8,r10 rules-implemented=r2,r4,r7,r8,r10,shonen
# process-exit 1 (failed)
```

`GATE_EXIT=1`.

Per-rule census (recomputed by parsing the same run's finding lines):
`1 r10, 80 r4, 1 r8` → 82. No r2 and no r7 finding; SHONEN produced no finding.

### Gate run — lane's committed round (round 12)

Round derivation from committed `LOG.md:656-661`: "**Round identity.** Steered round 12 (fleet-ledger
`.ufo/waves/kaika/steer.md`, prompt `.ufo/prompts/mado-round-12.md` @ ledger `12a5571`). Last admitted
round is 11." The lane's committed lessons are `round-1`, `round-10`, `round-12`,
`round-12-verifier-spotcheck`; no round-11 lesson exists. Selector 12 is therefore the lane's own
round at HEAD.

```
$ node .ufo/waves/round-9/corpus-gate.mjs --snapshot \
    /home/vgpnk/Projects/shokunin/mado-shokunin e3e6a8e6… --round 12
# corpus-gate-v1 — CORPUS.md rules recomputed (aggregator lane round 9), round-selector=12
# expect mado-shokunin@e3e6a8e ABSENT (no committed expected verdict for this revision)
CR-mado-shokunin-r10-1: no corpus/lessons/round-12-aggregator-*.md — the round-12 review duty has no emitted lesson (CORPUS.md:21)
# verdict mado-shokunin failed findings=82 rules=r4,r8,r10 rules-implemented=r2,r4,r7,r8,r10,shonen
# process-exit 1 (failed)
```

`R12_EXIT=1`. Finding count, rule set, and every r4/r8 id are unchanged; only the r10 id's round
differs. The verdict does not depend on which round selector is defensible.

## Finding detail (all failed rules)

### r8 — 1 finding: `CR-mado-shokunin-r8-1` (literal credential-pattern occurrence)

Exact source line implicated (`corpus/knowledge/walker-deep.md:124`, read via
`git show e3e6a8e:corpus/knowledge/walker-deep.md` and the worktree; worktree == HEAD):

```
| `force_keyboard_focus` (`:1`) | `true` | `false` (`:1`) | keyboard focus stays in walker; walker's own warning token: "windows might potentially not be focused if force_keyboard_focus is true" |
```

The gate's r8 `kv-secret` regex is
`/\b(password|passwd|api[_-]?key|access[_-]?token|auth[_-]?token|token|secret)\s*[=:]\s*\S{8,}/gi`
(`corpus-gate.mjs:282`). On line 124 it matches `token: "windows` = 15 characters, `first4="toke"`,
which exactly reproduces the printed `len=15`/`first4="toke"`. The "value" is the opening of a quoted
English sentence about walker's own warning text, not a credential value.

Frame this precisely, both ways:

- As a **mechanic**: the finding is a literal-text hit at `e3e6a8e` and the gate declares it stands as
  failed; `classification=could-not-evaluate` is an abstention, not a clearance. The verdict above
  therefore counts r8 as failed.
- As **content**: the single occurrence is the prose noun "token" followed by a quoted sentence. It is
  a pattern false positive, and I found no credential-shaped material in the one occurrence the gate
  reports. The gate's own note says the classification (real vs schematic) is not evaluated because it
  would need a vault read.

### r10 — 1 finding

`--round 9`: the lane carries no `corpus/lessons/round-9-aggregator-*.md`.
`--round 12`: the lane carries no `corpus/lessons/round-12-aggregator-*.md`.

Whole-history check (two independent sweeps, both zero):
`git rev-list --all --objects | grep -ci aggregator` → `0`;
`git log --all --format='%h %s' | grep -ci aggregator` → `0`.
So the lane has never carried a path, blob, or commit subject naming an aggregator lesson — the
absence is not a regression introduced by the round-12 landing or by the jj migration.

At the lane's own round, a round-12 outside-review lesson **is** committed, at HEAD, as
`corpus/lessons/round-12-verifier-spotcheck.md` (1824 B; its first line reads "Written by the
integrator, not the lane (CORPUS.md: corrections and outside reviews are new files; the lane owns
`round-12.md`)"). It does not match r10's regex `^lessons/round-<R>-aggregator-.+\.md$`
(`corpus-gate.mjs:445`). [INFERENCE] The `round-<N>-aggregator-*` naming is aggregator-owned (the
fleet round-9 CONTEXT records "Aggregator-owned lesson naming"), so the round-12 r10 finding most
plausibly routes to the aggregator/parent naming duty rather than to a lane writing defect; the
round-9 finding is a settled historical gap (three admitted rounds past). I did not read the parent's
round-12 ledger, so this routing statement is an inference, not an observation of ownership.

### r4 — 80 findings, distribution by file

Mechanic (`corpus-gate.mjs:450-465`): scan `README.md`, `knowledge/**.md`, `lessons/**.md`; skip fenced
blocks; skip any line containing a backtick; fire when `COUNT_NOUN_RE`
(`corpus-gate.mjs:267`, nouns `rows|files|lines|…|pins`) matches. The test is syntactic: it cannot
distinguish a measured count claim from a heading label or narrative prose.

| file | r4 findings |
|---|---|
| `knowledge/province-accuracy-selfaudit.md` | 9 |
| `knowledge/terminals-and-omarchy.md` | 6 |
| `knowledge/walker-deep-r9.md` | 6 |
| `knowledge/snapshot-diff-receipt-r9.md` | 6 |
| `knowledge/config-health-report-r3.md` | 6 |
| `knowledge/arc-synthesis.md` | 4 |
| `knowledge/closeout-r11.md` | 4 |
| `knowledge/gate-mutation-proof.md` | 4 |
| `knowledge/hyprland-config-plane.md` | 4 |
| `knowledge/waybar-walker-semantics.md` | 4 |
| `lessons/round-10.md` | 4 |
| `knowledge/executor-test-sufficiency.md` | 3 |
| `knowledge/hyprctl-verification-layer.md` | 3 |
| `knowledge/walker-deep.md` | 3 |
| `knowledge/gate-mutation-sweep-r8.md` | 2 |
| `knowledge/gate-standing-use.md` | 2 |
| `knowledge/remaining-planes-census.md` | 2 |
| `knowledge/theme-wallpaper-plane.md` | 2 |
| `knowledge/walker-live-surface.md` | 2 |
| `knowledge/waybar-walker-plane.md` | 2 |
| `knowledge/config-drift-r12.md` | 1 |
| `lessons/round-12.md` | 1 |

Sampled lines, re-read at HEAD to confirm the literal mechanic (all three are backtick-free lines
carrying a count noun and no command):

- `knowledge/terminals-and-omarchy.md:29` → `### alacritty.toml (28 lines)` (a heading label; the
  preceding line 27 is `Line numbers are from the Read view of each file.`, which is not a command).
- `lessons/round-10.md:3` → `Training round 10 (fleet "training r9"), wave-10 32-lane (1 lane rerouted`
  (matches `1 lane`; narrative wave composition, no command).
- `lessons/round-12.md:66` (the S012 registry row; the count noun lies later in the same line).

Judgment: r4 is implemented as declared ("a count on a line with no backticked command"), and these
are literal failures of that implemented test. It is not a judgment that the underlying numbers are
wrong; the mechanic's over-inclusion (headings, wave prose, cross-references) is a named limitation
of the check, and the representative count I checked by hand is genuinely count-without-command.

## SOURCES structural observations (`corpus/SOURCES.md` at `e3e6a8e`)

Row census: 39 registry rows = **27 `mined`, 9 `queued`, 3 `rejected`**
(`grep -oE '\| (mined|queued|rejected) \|' corpus/SOURCES.md | sort | uniq -c`;
`grep -c '^| S0' corpus/SOURCES.md` → 39). Recheck column distinct values: `17 on-release`,
`9 180d`, `7 90d`, `5 on-change`, `1 on-gate-change` (sum 39).

**Provisional, not a frozen census total.** Per the parent's round-12 direction, the indented-row
census parser fix is in flight and no `FINAL LANES READY` signal has arrived. The 39-row count above is
a revision-bound observation at `e3e6a8e` only, produced by the stated command; it must not be
published as a fleet census total or compared as a frozen baseline.

Structural observations:

1. **Anchor cells reproduce from git objects.** Two revision-bound digests verified byte-exact at
   their named revision:
   - S001 `corpus/lessons/round-10.md:63-123 @ a6528e6 (sha256 d7b4708e864fca29…)` →
     `git show a6528e6:corpus/lessons/round-10.md | sha256sum` =
     `d7b4708e864fca291c4bff92e234c97e5471d8c8c0870ddd31fe8a692583fa23` (prefix matches; the
     range is 61 lines, non-empty).
   - S002 `corpus/knowledge/arc-synthesis.md:290-307 §6 @ a6528e6 (sha256 a5b4833141461810…)` →
     `a5b48331414618108cdc9596cf6c7cc0dc78994ebcf61141c3e6d80428419d50` (prefix matches; lines
     290-307 open `## 6. The gap ledger — surfaces the arc never made verdict-bearing`).
   - S013 (`/home/vgpnk/Projects/gkeep/install.sh`): gkeep `HEAD` = `133b86717a02548aeaff3f1411bf301d936c5308`
     (matches the row) and worktree sha256 = `git show HEAD:install.sh` sha256 =
     `f17617de4060b3b18e7aa17a332cb732bd557dd08bf430238ba92de7f5b7d26`, so the row's "worktree SHA
     equals `HEAD:install.sh`" is true at measurement time.
2. **Stale rejected row inside a study path and an index row (observed inconsistency).** The Paths
   entry for U2 (`SOURCES.md:55`) ends `… → S029 → S030`, and the README index row for
   `hyprland-config-era-r12.md` (`corpus/README.md:35`) cites `source:` `S021–S030`; but S030's status
   is `rejected` in the same file (`SOURCES.md:41`), and the post-review errata appended below the
   search log records `status mined → rejected in place` for S030 with its `used-by` moved to S017.
   The path and the README row were not updated when S030's status changed, so the committed navigation
   surfaces still route a reader through a rejected duplicate. Counterweight: rejected rows are kept as
   taste evidence by the contract, and S030 is not sole support for that note (S021–S029 remain mined),
   so this is a navigation/staleness defect, not a sourcing gap. It is a SOURCES/README observation,
   not a gate finding (no r7 finding fired; r7 grades phantom rows, not status).
3. **Owed anchors are disclosed, not hidden.** The search-log errata says four `queued` rows (S006,
   S008, S009, S010) carry a section but only an access date, not a page revision, and states why the
   superseding row is deferred. This is an honest, self-named debt; no action taken here.
4. **Search-log arithmetic erratum is disclosed.** The same errata identifies the portal seat's
   "excluded 0" as having come from `printf '%s' '' | wc -l` (empty input, not a count), then restates
   the accounting (9 screened; 6 selected U3; 3 kept `queued`; 0 excluded). The correction preserves
   the old value, consistent with the lane's append-only errata rule.
5. **Index coverage (independent recomputation).** Across `knowledge/*.md` + `lessons/*.md`
   (30 files), the README coverage map references 26; unreferenced = the four lesson files
   (`round-1.md`, `round-10.md`, `round-12.md`, `round-12-verifier-spotcheck.md`); phantom
   README→file references = 0 (`LC_ALL=C comm` over `ls` vs `grep -ohE '(knowledge|lessons)/…'`).
   The gate's own r7 note reports `5/32` unindexed with its wider file universe (its denominator is
   `files.length - 1` after removing `README.md`, so its universe includes `SOURCES.md`/`QUALITY.md`);
   the difference in denominator, not a disagreement about phantoms. r7 produced zero findings either
   way, and under-coverage is declared non-finding by the gate.

### Extracted study path (directly evidenced, one sequence)

`SOURCES.md:54` — **Window-rule effects (U1)**:

> **Window-rule effects (U1)** — S002 → S018 → S019 → S020 → S016 → S017: start from the gap the arc
> named, read the tagged 0.56.2 handler before any doc, then the host capture and the host rule files,
> and only then the current (Lua-era) wiki pages; this order keeps pinned-source truth ahead of
> current-docs prose.

Evidence that the sequence is real at `e3e6a8e` (not a lead):

- All six rows are in the registry with status `mined` (S002, S016, S017, S018, S019, S020); none is
  `queued` or `rejected`. S002/S016/S017/S018/S019/S020 are the exact ids the README index row for
  `knowledge/window-rule-effects-getprop.md` (`corpus/README.md:34`) names as `source:`.
- Step S002 → `corpus/knowledge/arc-synthesis.md` §6, verified byte-exact at `a6528e6` (digest above).
- Step S018 → tagged source anchor `src/debug/HyprCtl.cpp` lines 1463-1645 at tag commit
  `efb50993780079460b0cbed1363e2166a2de1d9f` (URL; not re-opened — no network).
- Step S019 → both evidence files exist in the committed tree:
  `git ls-tree -r --name-only HEAD -- .ufo/evidence/round-12/` lists
  `.ufo/evidence/round-12/getprop-help.txt` and `.ufo/evidence/round-12/getprop-measure.txt`
  (42 round-12 evidence files tracked at HEAD).
- Step S020 → both host files exist read-only: `windows.conf` 681 B and `apps/terminals.conf` 235 B,
  mtime `Oct 3 17:42` (`ls -l`, exit 0).
- Steps S016/S017 are wiki URLs; not re-opened (no network), so their page content is unverified here.
  Their registry `anchor` cells name section and page revision date.

This is the usable path: it carries claimed order plus the reason for the order, every step is a
registry row with a status, and the first/last local steps resolve to committed bytes and existing
host files. The U4/U6 path (`SOURCES.md:58`) is deliberately *not* used as evidence here: its rows are
`queued`, and the lane's own rule is that queued rows are not citable as sole support.

## Provenance frontmatter scan (parent addendum)

Bounded scan of `corpus/knowledge/**/*.md` for `source:`, `verified-at:`, `recheck:` fields:

```
$ grep -nE '^\s*(source|verified-at|recheck)\s*:' knowledge/*.md | wc -l   # 22 hits
$ grep -rniE '(^|[^a-z])recheck[^a-z]' --include='*.md' . | grep -cE '\.tower/worktrees|/tmp/'
0
```

- No YAML `---` frontmatter block opens any file (`head -1` check); the three keys appear as plain
  header lines, e.g. `knowledge/window-rule-effects-getprop.md:3-5`,
  `knowledge/config-drift-r12.md:3-5`, `knowledge/xdg-portal-routing-r12.md:3-5`,
  `knowledge/hyprland-config-era-r12.md:3-5`, plus older notes (`arc-synthesis.md:3-9`,
  `closeout-r11.md:3-15`, `gate-standing-use.md:3-11,360`).
- **Zero `recheck:` values point into `.tower/worktrees` or `/tmp`.** Values are dates
  (`2027-01-17`), policies (`on-release`, `on-change`), or re-derivation commands
  (`sha256sum tools/mado-verify.sh`; `git show <commit>:tools/mado-verify.sh | sha256sum`).
  No provenance/fidelity finding on the parent's stated criterion.
- Related, and reported as an observation rather than a rule verdict: exactly one `.tower/worktrees`
  reference exists in the lane corpus — `SOURCES.md:22`, S011's **source** cell
  (`…/.tower/worktrees/kaika/fleet-ledger/MANIFEST.json`, tier C, status `rejected`). It is a source
  cell, not a `recheck:` value, and the same row pins content with
  `@ fleet-ledger 959b746 (sha256 1c8e4f11fd113e35…)`, so the bytes remain identifiable if the
  worktree path moves. Flagged as a durability smell only; the row is already rejected.
- 97 occurrences of `/tmp/` remain in historical body text (rounds 1–5 scratch receipts, e.g.
  `knowledge/config-health-report-r3.md:483-485`, `knowledge/waybar-walker-semantics.md:8,113,450`).
  The lane's own QUALITY.md criterion 13 states "`/tmp` records provenance only", and those lines are
  labelled scratch/ephemeral; not treated as recheck targets. Historical evidence left unchanged.

## Repo identity and commit-read feasibility after the jj migration

Identity:

- `git rev-parse --show-toplevel` → `/home/vgpnk/Projects/shokunin/mado-shokunin` (exit 0);
  `git rev-parse --absolute-git-dir` → `/home/vgpnk/Projects/shokunin/mado-shokunin/.git`.
  The audited path is the original lane repository, not a retired worktree.
- Colocated jj repo: `.jj/` exists; `.jj/repo/store/type` = `git`; `.jj/repo/store/git_target` =
  `../../../.git` → jj is backed by the same git object store. `.jj/working_copy/type` = `local`.
- `.jj` is not in the graded tree: `git ls-tree -r --name-only HEAD -- .jj` → 0 files; its contents are
  self-ignored by `.jj/.gitignore` = `/*` (root `.gitignore` holds only `.ufo/interactive-sessions/`,
  and `git check-ignore .jj` exits 1), which is why `git status --porcelain` stays empty.
- Refs: `refs/heads/master` = `e3e6a8e`; `refs/remotes/origin/master` and `origin/HEAD` = `e1d81d4`;
  `refs/jj/keep/{b911903, cd44585, e1d81d4, e3e6a8e}`. Remote `origin` =
  `https://github.com/VeigaPunk/mado-shokunin.git`.

Commit-read feasibility (the checks that matter for evidence reuse):

- `git cat-file -t e3e6a8e…` → `commit`; `git cat-file -s` → `330` bytes.
- Cited revisions resolve as commits: `a6528e6`, `e1d81d4`, `7cd7f33`, `f7bfc9f` all
  `git rev-parse --verify <rev>^{commit}` → full sha, exit 0.
- Blob-level reads at historical revisions work: `git show a6528e6:<path> | sha256sum` reproduced the
  S001/S002 digests exactly.
- The gate's own snapshot extraction succeeded post-migration: the run's note reads
  `# note mado-shokunin extracted with: git archive e3e6a8e… | tar -x -C <tmp>` (a `git archive` tree
  is exactly what `--snapshot` grades, and it produced a full 82-finding result).
- Two tokens that do **not** resolve as commits (`4bde28aa5eef9600`, `016ecd68`) are used in the lane's
  own text as *file* hashes (a plan sha and a SKILL sha), not as revision ids; I record their
  non-resolution so no reader mistakes it for a missing-history defect. No defect claimed.
- `git status --porcelain` remained 0 lines on a second run; `.git/index` mtime stayed
  `2026-10-19 20:38:01.315365932 −0300` (observed at 20:45:20), so this audit's read verbs caused no
  observed index rewrite. I ran no mutating git verb (no add/commit/checkout/reset/stash/clean) and no
  write into the lane tree.

Limits of this identity/feasibility statement:

- **I ran no `jj` command.** jj's read verbs (`jj status`, `jj log`) snapshot the working copy into a
  new commit/operation and would mutate repository state, so jj's own view of the working-copy commit
  was not queried. `.jj/working_copy/checkout` is a 75-byte binary record and was not parsed; the
  6637-byte `tree_state` was not decoded. Cleanliness is established for *worktree vs `HEAD`* via git
  only; I do not claim jj reports a clean working-copy commit.
- Push state is not established: local `master` (`e3e6a8e`) is ahead of the recorded
  `refs/remotes/origin/master` (`e1d81d4`), and no fetch/network call was made. Observation, not a
  defect.
- Historical revisions remain readable through the shared git store; whether jj will retain them under
  its own garbage-collection policy is not something this audit measured.

## Gate limitations (explicitly named, so a pass/fail is not over-read)

From the instrument's own registry block and the observed run:

- **Implemented**: r2, r4, r7, r8-literal, r10 presence, and SHONEN canonical **form**.
- **Declared not-evaluated**: r1 (source-ness is semantic), r3 (falsifiability is semantic), r5
  (negative-claim sweeps), r6 (quote locations need outside surfaces), r9 (corrections/new-entry
  history — structurally unavailable in `--snapshot`, which has no history), box-3 verifier
  independence, SHONEN truth, and the r8 schematic-vs-real classification (exit-2-class abstention
  because it needs a vault read).
- **No frozen expectation at this revision**: the run printed
  `# expect mado-shokunin@e3e6a8e ABSENT (no committed expected verdict for this revision)`. The
  result is a live recomputation; the gate's exit-3 "frozen expectation drift" branch was not
  exercised, and I did not run `--selftest` (out of this seat's scope).
- **Snapshot-mode scope**: `--snapshot` grades a `git archive` of the named commit, so untracked or
  worktree-only bytes are invisible by design; `dirty=0` in the header refers to the source tree
  state the snapshot was taken from.
- **r4 shape**: syntactic count-noun test with a backtick escape hatch — cannot distinguish a measured
  count from a heading or narrative count, and cannot judge whether a cited count is correct.
- **r7 shape**: phantom rows are the finding; missing rows are a note. Under-coverage is not a defect
  in this gate's model.
- **r8 shape**: unit is occurrences over every text file under `corpus/`; the mechanic is literal. The
  one finding here is a prose false positive by the regex, but the gate's declared rule is that the
  literal finding stands — hence the verdict above keeps r8 as failed rather than clearing it.
- **r10 shape**: pure filename presence. A committed round-12 outside-review lesson under a different
  name does not satisfy it (see r10 section).

Therefore: **`not conformant` at `e3e6a8e` is a rule-10 verdict backed by exit 1 and the named failed
rules r4/r8/r10.** It is not a statement that the corpus is semantically wrong on every axis: r1, r3,
r5, r6, r9, verifier independence, and SHONEN truth were not evaluated, and the r8 content is a
literal-pattern hit on prose.

## Write scope / what this audit did not do

- Only this note was written under
  `/home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/fleet-aggregate/.ufo/waves/kaika-aggregate/seats/`.
  Aggregation scratch went only to `/tmp` (`m_files.txt`, `m_refs.txt`, `mado-gate-round9.out`); no
  child-repo file, ref, index, or object was modified, and no fleet ledger/README/LOG/SCORECARD/report
  was touched.
- No network access: wiki/URL rows and release pages were not re-opened; only committed anchors,
  local files, and git objects were verified.
- No builds, tests, lint, or formatting were run; the only executable invoked besides git/`ls`/`grep`
  was the named gate script under `node v24.21.0`.
- Historical evidence in the lane (including the `/tmp` scratch references and the S030 rejection
  record) was left exactly as committed.
