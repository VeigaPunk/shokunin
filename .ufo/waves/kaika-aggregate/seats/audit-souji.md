# audit-souji — aggregator round 12 lane audit (read-only)

Seat: KaikaAggregateR12.AuditSouji. Date: 2026-10-19.
Lane audited: `/home/vgpnk/Projects/shokunin/souji-shokunin` (original path; no retired worktree used).
Method: read-only observation. No file in the child was modified. Read surfaces:
`corpus/SOURCES.md`, `corpus/README.md`, `corpus/QUALITY.md`, the gate-flagged lessons,
`SHONEN.md`, `LOG.md` (head/tail), plus bounded existence/pattern checks (ls/grep) needed to
characterize findings. Working tree clean at HEAD, so working-tree content == HEAD content.

## 1. Revision stamps

```
$ git -C /home/vgpnk/Projects/shokunin/souji-shokunin rev-parse HEAD
31984f473ce4bdab61a99b16cca194b28108cb81

$ git -C /home/vgpnk/Projects/shokunin/souji-shokunin status --porcelain
(no output, exit 0)
```

## 2. Gate run (corpus-gate-v1, script at `.ufo/waves/round-9/corpus-gate.mjs`)

Lane round derived from committed `LOG.md`: the tail carries `## 2026-10-19 — round 12
closing note (measured commit)` (work commit `d7266c5e9493a3c78687af68d438c2584f75b3c0`) and
`## 2026-10-19 — round 12 post-review fixes (orchestrator adjudication)`. Lane round = 12.
Both the script default (`--round 9`) and the derived lane round (`--round 12`) were run; the
only output difference is the round number inside the r10 finding text. Findings set and
exit are identical.

Exact commands (cwd `/home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/fleet-aggregate`):

```
$ node .ufo/waves/round-9/corpus-gate.mjs --snapshot /home/vgpnk/Projects/shokunin/souji-shokunin 31984f473ce4bdab61a99b16cca194b28108cb81
$ node .ufo/waves/round-9/corpus-gate.mjs --snapshot /home/vgpnk/Projects/shokunin/souji-shokunin 31984f473ce4bdab61a99b16cca194b28108cb81 --round 12
```

Both: `process-exit 1 (failed)`; per-run verdict lines:

```
# verdict souji-shokunin failed findings=18 rules=r2,r4,r10,shonen rules-implemented=r2,r4,r7,r8,r10,shonen
# process-exit 1 (failed)
```

Shared preamble (both runs):

```
# corpus-gate-v1 — CORPUS.md rules recomputed (aggregator lane round 9), round-selector=9|12
# expect souji-shokunin@31984f4 ABSENT (no committed expected verdict for this revision)
# tree souji-shokunin revision=31984f473ce4bdab61a99b16cca194b28108cb81 dirty=0 mode=snapshot
```

Notes: no committed expected verdict exists for this revision, so the DRIFT class (exit 3) is
not exercised; `dirty=0` and `mode=snapshot` mean the graded tree is `git archive` of the
named commit with no working-tree content and no git history.

## 3. Verdict

**`not conformant`** at HEAD `31984f473ce4bdab61a99b16cca194b28108cb81` per corpus-gate-v1
exit 1 (18 findings: r2 x7, r4 x7, r10 x1, shonen x3).

Failed rule IDs and items:

### r2 (CORPUS.md:19, lessons cite round + evidence) — CR-souji-shokunin-r2-1..7

Flagged lessons: `lessons/round-1.md`, `round-10.md`, `round-11.md`, `round-2.md`,
`round-4.md`, `round-7.md`, `round-9.md` — each reported as "carries no evidence pointer
(commit hash, .ufo/reports/ path, or LOG.md)".

Literal-check characterization (gate source, `corpus-gate.mjs` r2 block):
`evidenceCited = /\b[0-9a-f]{7,40}\b/ || /\.ufo\/reports\// || /LOG\.md/` over the whole file
text. Supporting check I ran: per-lesson count of tokens matching exactly that pattern:

```
$ for f in corpus/lessons/*.md; do printf '%s: %s\n' "$f" "$(grep -cE '\b[0-9a-f]{7,40}\b|\.ufo/reports/|LOG\.md' "$f")"; done
round-1.md: 0   round-10.md: 0   round-11.md: 0   round-12-verifier-spotcheck.md: 3
round-12.md: 32 round-2.md: 0    round-3.md: 1    round-4.md: 0    round-5.md: 2
round-6.md: 1   round-7.md: 0    round-8.md: 1    round-9.md: 0
```

So "no evidence pointer" means literally: no 7–40-char lowercase-hex token, no
`.ufo/reports/`, no literal `LOG.md` in the file. The check accepts any hex-shaped token —
`round-6.md` passes on the string `sha 11bf9cdf…` alone. The check does NOT accept
`census/…`, `tests/results/…`, or bare report names, which is how several flagged lessons
actually cite evidence; and some flagged lessons cite no path at all (round-1.md names
seats/ids and counts only). The flagged lessons' underlying evidence is not adjudicated here;
only the literal absence is a gate fact. For calibration, cited evidence that does exist
in-tree for flagged lessons: `tests/results/INSTALL.json` (871 B, round-2.md) and
`census/round-9/dissent-24.md` (round-9.md), both verified present.

### r4 (CORPUS.md:28, a count carries its command) — CR-souji-shokunin-r4-1..7

Fired on lines with the count-noun regex and no backtick on the line (outside fences).
Recorded line, trigger as the gate excerpted it:

| id | site | excerpt (gate) | my classification |
|---|---|---|---|
| r4-1 | lessons/round-12.md:19 | "row S031 (32 rows, same checks). Counts:" | real count claim ("32 rows"); adjacent lines :20-21 carry backticked commands but not one counting this row |
| r4-2 | lessons/round-12.md:68 | "| M06 | process | Fixture/segment schema chaos — 2/10 cases " | real counts ("2/10 cases"; also "4 shards … 3 schemas" on the same row); row cites evidence `corpus/lessons/round-2.md:12 + round-3.md:25`, no command |
| r4-3 | lessons/round-12.md:85 | "| M23 | process | 32/128 seat failures (waits + provider lim" | real count ("32/128") |
| r4-4 | lessons/round-12.md:147 | "| K1 admit | agree | every cited v2.55.0 line checks | — |" | tokenizer artifact: "0 line checks" fires on the version string `v2.55.0`; not a count claim |
| r4-5 | lessons/round-12.md:341 | "- ART: agrees with ART §6 item 1, which was not a §3 row the" | tokenizer artifact: "3 row" fires on the section reference `§3 row`; not a count claim |
| r4-6 | lessons/round-6.md:8 | "- 32/128 seat failures (waits + provider limits) gutted the " | real count; no command on that line or in the bullet |
| r4-7 | lessons/round-9.md:27 | "- rubric-final.md banked (S13-based merged scorer, 12/12 che" | real count ("12/12 checks"); no command |

So of 7 findings: 5 are count claims without an inline backticked command; 2 are literal-regex
artifacts on version/section tokens. The rule's intent ("written as `<number> — <command>
<date>`") and whether a same-file command elsewhere satisfies it are semantic questions the
gate does not decide.

### r10 (CORPUS.md:21, the round's review lesson) — CR-souji-shokunin-r10-1

- Default run: "no corpus/lessons/round-9-aggregator-*.md — the round-9 review duty has no emitted lesson".
- Lane-round run: "no corpus/lessons/round-12-aggregator-*.md — the round-12 review duty has no emitted lesson".

Supporting checks (read-only, fleet-wide): six sibling lanes carry round-9 aggregator
lessons (`kagi`, `kake`, `kasegi`, `kengaku`, `kotoba`, `kumitate` —
`.../corpus/lessons/round-9-aggregator-corpus-verdict.md`); souji carries none under any
name; and `ls /home/vgpnk/Projects/shokunin/*-shokunin/corpus/lessons/*round-12-aggregator*`
→ "No such file or directory" for the whole fleet. Per CORPUS.md:21/43 the aggregator lesson
is aggregator-authored ("the aggregator writes only `lessons/round-<N>-aggregator-*.md`"),
so under `--round 12` this fires fleet-wide pending the aggregator's own emission; under the
default selector it is a souji-specific absence relative to six siblings.

### shonen (PROTOCOL.md §File contract) — CR-souji-shokunin-shonen-1..3

`SHONEN.md:13` blank line, `:14-15` prose:

```
13:
14: Marks: `[~]` asserted by the lane itself (evidence pointer required), `[x]` only with a named
15: non-author verifier per **Promotion gates**.
```

The gate's canonical-form check (`checkShonen`) accepts only: header lines 1-4 (byte-identical
modulo `<name>=souji-shokunin`), exactly 4 box lines with canonical seed text, marks in
`{x,~,space}`, at most one indented evidence line per box, `[x]` lines with a verifier-id
token, and no other lines. Observed: all four boxes (lines 5/7/9/11) carry canonical text and
exactly one evidence line each (6/8/10/12), marks are `[~]`, trailing newline present — the
sole deviations are the three flagged lines. This is a FORM check only; box truth and
verifier independence are not evaluated.

### Rules with zero findings in this run

r7: no findings. Notes printed: "2 backticked path template(s)/glob(s) skipped (contain *,
<, {, ~, $ or …)" and "r7 under-coverage (not a finding): 12/21 corpus files carry no index
row". r8: no findings — the literal credential-material sweep over every text file under
`corpus/` reported zero occurrences at this revision.

## 4. SOURCES.md structural observations (not gate-graded; separate from §3)

- Header: `Contract: SOURCES-CONTRACT-v1 (kaika, frozen 2026-10-19)`; "Every row below was
  opened on 2026-10-19 in round 12; the per-row URL, access date and grounding quote are in
  `census/round-12/sources-gate.md`" — that file exists (`census/round-12/` listing includes
  `sources-gate.md` and `sources-census.sh`).
- Registry (`## Registry`, line 5): rows S001–S033.
  `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` → `33`.
  Status distribution: `grep -oE '\| (mined|queued|rejected|held) \|'` → 16 mined, 15 queued,
  2 rejected (S030, S032), 0 held. **This count is provisional**: per parent direction a
  census parser fix for indented Markdown source rows is in progress elsewhere; no final
  census totals are frozen or published here.
- `## Paths` (line 43) holds F1/F3/F4 reading sequences; `## Search log` (line 49) holds three
  entries (ART re-open sweep; revision pinning with the exclusion of RelNotes-2.55.0 vs master
  at line 88; two named negative sweeps with their exact commands); `## Leads (unopened)`
  (line 56) is explicitly unopened and is not evidence.
- Every row id cited by the three Paths resolves to a registry row: all 21 ids
  (F1: S002,S001,S009,S003,S004,S010,S011; F3: S017,S016,S019,S018,S020,S021;
  F4: S029,S022,S023,S025,S024,S026,S027,S028) verified present.

### Extracted study path (directly evidenced) — F1, `corpus/SOURCES.md:45`

`F1 git-native housekeeping — S002 → S001 → S009 → S003 → S004 → S010 → S011`, rationale in
the same line: "the docs give intent and defaults; the tagged source shows what actually runs
on `--auto`; worktree gives the lock and porcelain controls; repack gives object-level holds;
release notes and BreakingChanges track drift."

Row-level evidence for the sequence (each from its registry row, opened 2026-10-19):
S002 git-gc(1) grace periods (mined) → S001 git-maintenance(1) worktree-prune/geometric
(mined) → S009 git/git v2.55.0 source anchors in builtin/gc.c, worktree.c, run-command.c,
builtin/commit.c (mined) → S003 git-worktree(1) lock/prune/porcelain (mined) → S004
git-repack(1) `--expire-to` (mined) → S010 release notes 2.50.0–2.56.0 with per-file line
anchors (mined) → S011 BreakingChanges §Git 3.0 (queued — a tracked but not-yet-mined row).
The F1 rows' `used-by` links feed the two admitted knowledge entries named in README's F1
coverage row (`knowledge/git-auto-maintenance-prunes-worktrees.md`,
`knowledge/git-grace-periods-and-expire-to.md`). F2 has no path in `## Paths`; F3/F4
sequences exist as quoted above if needed.

## 5. Knowledge frontmatter provenance scan (parent addendum)

Bounded scan of `corpus/knowledge/**/*.md` (5 files, flat dir). All five carry
`source:`, `verified-at:`, `recheck:` on lines 1-3 (matches the lane's own README count
command; provisional under the census-parser caveat).

- `.tower/worktrees` pointers in any of the three keys: **none**.
- `/tmp` (or `/dev/shm`) literals, exact sites:
  - `corpus/knowledge/quarantine-same-filesystem-rename.md:3` `recheck:` — full value:
    `bash -c 'd=$(mktemp -d /var/tmp/souji-k5-XXXXXX); s=$(mktemp -d /dev/shm/souji-k5-XXXXXX); trap "rm -rf -- $d $s" EXIT; stat -c "%d %m %n" /var/tmp /tmp "$s"; mkdir "$d/a" "$d/b"; echo x >"$d/a/f"; strace -e trace=rename,renameat,renameat2,unlink,unlinkat mv "$d/a/f" "$d/b/f" 2>&1 | grep -c "rename.*= 0$"; strace -e trace=rename,renameat,renameat2,unlink,unlinkat mv "$d/b/f" "$s/f" 2>&1 | grep -cE "EXDEV|unlinkat\(AT_FDCWD, \"$d/b/f\", 0\) = 0"; mv --no-copy "$s/f" "$d/f"; echo no-copy-exit=$?; /usr/bin/rm --help | grep -c -e --one-file-system -e "preserve-root\[=all\]"'   # expect: devices, 1, 2, "Invalid cross-device link", no-copy-exit=1, 2`
    Provenance/fidelity finding: this recheck's only non-`/var/tmp` write target is a
    `mktemp -d /dev/shm/...` dir (removed by its trap); `/tmp` appears only as a `stat -c %d %m`
    comparison subject, not as a storage location. The lane itself already records this entry
    as HELD, not admitted, with the reason stated: README "Corrections (r12 post-review)"
    ("`knowledge/quarantine-same-filesystem-rename.md` is HELD … its `/dev/shm` device relied
    on QUALITY Q15, withdrawn by Q16") and QUALITY.md Q16 ("Q15 … WITHDRAWN … a cross-device
    fixture needs a lesson-grounded criterion before it can be admitted"). Reported here as a
    provenance observation on a held entry, not as a gate rule and not as a semantic verdict.
  - Other four knowledge files: no `/tmp`, `/dev/shm`, or `.tower/` token in `source:`/
    `verified-at:`/`recheck:`.

## 6. Gate limitations (explicit, from the gate's own registry + observed behavior)

Not evaluated by construction: r1 (source citations), r3 (falsifiability/opinion), r5
(negative-claim sweeps), r6 (quote locations), r9 (append-only/no-rewrite — in snapshot mode
the graded `git archive` tree carries no history, so the one mechanical sub-check is exactly
unavailable here); "box-3" verifier independence; shonen-semantics (box truth). r8 literal-only:
schematic-vs-real classification declared could-not-evaluate (no r8 findings observed anyway).
r2 and r4 are literal tests, not semantic judgments (see §3). r10 is a presence check only —
it does not grade any review content. r4/r7 read canonical surfaces only (README.md,
knowledge/**.md, lessons/**.md); r7 grades phantom rows only, under-coverage is a note;
`corpus/evidence/**` and corpus-root data files are outside the declared layout. Exit
precedence 2 > 3 > 1 > 0; observed exit 1, no exit-2/3 condition. The `expect … ABSENT` line
means no frozen expectation exists for this revision, so a gate pass/fail here is a fresh
recomputation, not a drift check. A gate verdict is NOT whole-corpus semantic conformance;
SOURCES.md is not structurally graded by this gate at all (only swept by r8's literal
credential scan).

## 7. Limits of this audit

- Read, not executed: no fixtures, no builds/tests/lint, no gate `--selftest`.
- Only the surfaces named above were opened; census/ file bodies were not audited (existence
  checks only, e.g. `census/round-12/sources-gate.md`).
- Census/row-count figures are provisional (parser fix in progress elsewhere; final census
  waits for the parent's FINAL LANES READY signal).
- Child repo untouched; this note is the seat's only write.