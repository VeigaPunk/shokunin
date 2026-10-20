# audit-kotodama — kotodama-shokunin at 4ad2683

Seat: KaikaAggregateR12.AuditKotodama · date 2026-10-19 · gate: `corpus-gate-v1`
(`.ufo/waves/round-9/corpus-gate.mjs`). Child repo treated read-only; this note is the
only write. No numeric score emitted.

## Identity (originals path, not a worktree)

```
$ git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin rev-parse HEAD
4ad26836552462d28a946ca3b067cab0b5ce3532                                    # exit 0
$ git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin status --porcelain
                                                                            # empty, exit 0
$ git -C ... log -1 --format='%H%n%ci%n%s'
4ad26836552462d28a946ca3b067cab0b5ce3532
2026-10-19 20:12:43 -0300
round-49 verifier spot-check (integrator, kaika): non-author admit/reject sample + adjudication
```

Working tree clean ⇒ working-tree bytes equal the committed tree; the `--snapshot`
verdict below is nonetheless derived from `git archive` of the named SHA.

## Verdict

**not conformant** at `4ad26836552462d28a946ca3b067cab0b5ce3532` — gate exit **1** (failed).

```
$ cd /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/fleet-aggregate
$ node .ufo/waves/round-9/corpus-gate.mjs --snapshot \
    /home/vgpnk/Projects/shokunin/kotodama-shokunin \
    4ad26836552462d28a946ca3b067cab0b5ce3532
# corpus-gate-v1 — CORPUS.md rules recomputed (aggregator lane round 9), round-selector=9
# expect kotodama-shokunin@4ad2683 ABSENT (no committed expected verdict for this revision)
# tree kotodama-shokunin revision=4ad26836552462d28a946ca3b067cab0b5ce3532 dirty=0 mode=snapshot
...
# verdict kotodama-shokunin failed findings=208 rules=r2,r4,r8,r10,shonen rules-implemented=r2,r4,r7,r8,r10,shonen
# process-exit 1 (failed)
EXIT=1
```

Failed rule IDs and counts: **r2 = 4, r4 = 199, r8 = 1, r10 = 1, shonen = 3** (208 total;
counts re-derived by parsing the `CR-` lines of a second identical run — stable across
four invocations). r7 produced no finding (two `# note` lines only: 1 backticked template
skipped; under-coverage 405/408, declared not-a-finding).

The `# expect … ABSENT` line means exit 1 is the live grading, not exit-3 expectation
drift.

### Round selector (explicit, because lane round ≠ aggregator round)

Gate default `--round 9` is documented in the registry block ("round selector `--round <N>`
(default 9); the round whose aggregator lesson r10 requires"). The lane's committed LOG
ends at lane round 49 (`LOG.md` tail: "Round 49 post-review corrections", 2026-10-19); the
aggregator round in flight is 12. All three selectors were run:

```
$ for n in 12 49; do node .../corpus-gate.mjs --snapshot <lane> <HEAD> --round $n; done
round 12 → CR-kotodama-shokunin-r10-1: no corpus/lessons/round-12-aggregator-*.md —
           the round-12 review duty has no emitted lesson (CORPUS.md:21)
           # verdict ... failed findings=208 rules=r2,r4,r8,r10,shonen ; # process-exit 1
round 49 → CR-kotodama-shokunin-r10-1: no corpus/lessons/round-49-aggregator-*.md —
           the round-49 review duty has no emitted lesson (CORPUS.md:21)
           # verdict ... failed findings=208 rules=r2,r4,r8,r10,shonen ; # process-exit 1
```

The verdict is selector-insensitive: `ls -1 corpus/lessons | grep -i aggregator` → no
match at all (0 aggregator lessons). Fleet context for the convention:
`for d in /home/vgpnk/Projects/shokunin/*-shokunin; do ls -1 $d/corpus/lessons | grep -c aggregator; done`
→ 0 in 15 of 21 lanes; kagi 8, kake 7, kasegi 7, kengaku 6, kotoba 6, kumitate 7
(rounds 1/4/5/6/8/9, incl. `round-9-aggregator-corpus-verdict.md` in all six).

## Findings, with reproduced evidence

### r2 — 4 `lessons/` files carry no accepted evidence pointer (CORPUS.md:19)

```
CR-kotodama-shokunin-r2-1: lessons/round-1-gates-and-triage.md carries no evidence pointer
CR-kotodama-shokunin-r2-2: lessons/round-12.md carries no evidence pointer
CR-kotodama-shokunin-r2-3: lessons/round-3-d2-build.md carries no evidence pointer
CR-kotodama-shokunin-r2-4: lessons/round-4-sol-fixes-and-audits.md carries no evidence pointer
```

Reproduced literally (same three accepted forms as the gate):
`grep -cE 'LOG\.md|\.ufo/reports/|\b[0-9a-f]{7,40}\b'` → **0** for each of the four files.

Adjudication nuance: this is a *form* failure, not always absence of evidence.
`round-3-d2-build.md:1-23` names `tools/gates/frozen/round-3/` and "`MANIFEST.tsv` pins
gate/input/output sha256s" — prose evidence pointers outside the gate's three accepted
forms. `round-1-gates-and-triage.md` (read in full) and `round-4-sol-fixes-and-audits.md`
(read in full) name no commit/report path at all.

### r4 — 199 count-claim findings over 95 distinct files (CORPUS.md:28)

Concentration (exact, from the `CR-` lines): `README.md` (corpus root) 18;
`lessons/round-4-audit/culture-material.md` 16; `lessons/README.md` 15;
`knowledge/linguistics/orality-formulaic-language.md` 7; `lessons/round-49.md` 7;
`lessons/round-11.md` 5; `lessons/round-10.md` 4; remainder ≤3 each.
By area, distinct files: `lessons/` 61, `knowledge/` 33, corpus `README.md` 1.

Sampled lines reproduced with the gate's own `COUNT_NOUN_RE` (no backtick on any of the
cited lines):

| finding | exact match token(s) | classification |
|---|---|---|
| `README.md:118` | `200 rows`, `200 files` | genuine count claim; per-line form failure — the backticked command `reports/round-28/readme/sweep.py` sits on line 116, two lines above |
| `README.md:99` | `7 note` (from "revision 1.7 note") | version-number false positive |
| `knowledge/civilizations/arabia-pre-islamic.md:82` | `291 call` (from "AWS 291 call her daughter") | citation-number false positive |
| `knowledge/civilizations/hopi.md:78` | `329, note` (from "(2009: 329, note 2)") | page-number false positive |
| `knowledge/linguistics/orality-formulaic-language.md:43` | `3,182 lines` (Beowulf edition count) | scholarly count, rule-literal hit |
| `lessons/README.md:7` | `1 stamp` (from "revision-1 stamp") | false positive |

### r8 — 1 literal credential-class occurrence (`knowledge/civilizations/aksum-ethiopia.md:120`, CORPUS.md:43)

```
CR-kotodama-shokunin-r8-1: credential-class kv-secret occurrences=1 lines=1 files=1
  owner=lane at 4ad2683 literal_shaped=1/1 :: classification=could-not-evaluate
  ... files=[knowledge/civilizations/aksum-ethiopia.md] first=knowledge/civilizations/aksum-ethiopia.md:120
  first4="secr" len=16
```

Reproduced with the gate's `kv-secret` regex on the committed blob: the 16-char match is
`secret: biblical`, inside ordinary prose on line 120:

> `- The gold need not be an insult or a political secret: biblical typology, saintly praise, and theological association also reward trained interpretation. Do not turn a literary practice into a national propensity to deceive. [HD; DL]`

`grep -n 'secret'` over the file returns only lines 120, 134, 191, all prose. **No
credential material is present.** The gate still prints this as a failed rule-8 finding
(its own note: literal-text occurrences "stand as failed"); schematic-vs-real
classification is declared could-not-evaluate and no vault read was attempted. Reading: a
false positive of the `secret\s*[=:]\s*\S{8,}` class, not a rule-8 content defect.

### r10 — 1 finding (see selector block above)

`CR-kotodama-shokunin-r10-1: no corpus/lessons/round-9-aggregator-*.md — the round-9 review duty has no emitted lesson (CORPUS.md:21)`

### shonen — 3 findings, SHONEN.md form only (PROTOCOL.md §File contract)

```
SHONEN.md:13 is neither the header block, a box line, nor an evidence line (blank line): ""
SHONEN.md:14 ... (prose): "Marks: `[~]` asserted by the lane itself (evidence pointer r"
SHONEN.md:15 ... (prose): "non-author verifier per **Promotion gates**."
```

Read the file: header block + exactly 4 boxes pass; the only defect is the 3-line "Marks:"
legend appended after the boxes. All four boxes are marked `[~]` (lane-asserted) with
evidence pointers; box 1 cites "census clean at `8c78e6b`", and
`git -C <lane> merge-base --is-ancestor 8c78e6b HEAD` → exit **0** (ancestor of HEAD), so
that citation is revision-bound to a real ancestor. Box truth and non-author verifier
independence are gate-declared not-evaluated.

## SOURCES.md structural observations (provisional — census NOT frozen)

`corpus/SOURCES.md` at 4ad2683, 169 lines. Sections (`grep -n '^#\+ '`): `## Registry` :26,
`## Paths` :78, `## Search log` :112, `## Leads (unopened)` :120.

- **Registry**: 47 rows `| S001 … S047 |`
  (`grep -cE '^\| S0[0-9][0-9] ' corpus/SOURCES.md` → **47**); indented source rows:
  **0** (`grep -cE '^[[:space:]]+\| S0[0-9][0-9] '` → 0) — the parent's in-flight census
  parser fix for indented rows has no target in this file's registry today.
- **Preamble** binds shape/rules to `SOURCES-CONTRACT-v1` (kaika, 2026-10-19); tiers
  A/B/C scoped per row, `community` never A; statuses `queued`/`mined`/`rejected`;
  append-only — only `status`, `recheck`, `used-by` change in place; a correction is a
  new row whose `teaches` opens `supersedes S0NN —`.
- **Census is deferred**: preamble says "the seven commands in the contract's `## Census`
  block; `python3 reports/round-49/run-validation.py` runs them". SOURCES.md contains no
  `## Census` block itself. No census command was run in this audit ⇒ **no totals are
  frozen here; any row counts above are provisional** pending the parent's
  `FINAL LANES READY` signal and the parser fix.
- **Scope drift noted, explained**: the preamble's row-range line still says
  "`lessons/round-49.md` for S001–S043", while the registry holds S001–S047. S044–S047 are
  the post-review supersession rows (S044→S034, S045→S038, S046→S039, S047→S029), matching
  the committed LOG entry "2026-10-19 — Round 49 post-review corrections" and
  `corpus/QUALITY.md` criterion 6 ("Correct a filed tier with a superseding SOURCES row,
  never an in-place tier edit"). Read in the file at :73-76 (S044 :73, S045 :74,
  S046 :75, S047 :76).
- `SOURCES.md` is **not** a canonical surface for r4/r7 (those read `corpus/README.md`,
  `knowledge/**`, `lessons/**` only), but r8 reads every text file under `corpus/`; r8
  reported no occurrence in `SOURCES.md` (its only file was the aksum entry).
- The `## Leads (unopened)` block states "A lead is not evidence and never a row". No lead
  was used as evidence in this note.

## Study path (directly evidenced)

`corpus/SOURCES.md:80-85`, first `## Paths` bullet, quoted verbatim:

> `- Typology evidence chain — S001 → S002 → S003 → S004: name the languoid in`
> `  Glottolog first (it fixes identity, family and the glottocode every other`
> `  dataset keys on), then take feature proportions from WALS, then check segment`
> `  plausibility against PHOIBLE inventories, then Grambank for grammatical design`
> `  space beyond what WALS covers.`

Resolution check: S001–S004 are registry rows (Glottolog, WALS, PHOIBLE, Grambank; S004
`queued`). Across all **15** Paths bullets, the 42 distinct referenced ids
(S001–S027, S031–S042) all resolve to registry ids (registry = S001–S047); no dangling id.
This is an ordered reading sequence with per-row `teaches`/`anchor` fields behind it, not a
bare link list.

## Provenance scan — bounded, per parent direction

Scope: every `corpus/knowledge/**/*.md` blob at 4ad2683
(`git ls-tree -r --name-only 4ad2683 corpus/knowledge` → **225** files), read through
`git show 4ad2683:<path>` (revision-bound, not worktree). Field parse:
`^-\s*(source|verified-at|recheck):`, whole blob.

- Field presence: `verified-at:` **225/225**; `recheck:` **225/225**; `- source:` **157/225**.
  The 68 without a `- source:` line all carry a `- sources:` block (verified 68/68).
- "Opens with" form deviation: first `verified-at:` after line 30 in **9** files; first
  `recheck:` after line 30 in **10** files (exact: mesoamerica-primary-sources 38/39,
  funerary-material-culture 40/41, writing-media-surface-economy 31/32, naming-systems
  34/35, phonetics-phonology 70/71, politeness-taboo-euphemism 35/36,
  register-strata-attestation —/32, sociolinguistics-registers 41/42,
  binding-speech-complex 35/36, sacred-kingship-mythic-charter 39/40).
- Newest files added 2026-10-19 (`git log --diff-filter=A`, 24 files): **all 24 carry all
  three fields**; the four with fields below line 30 are the funerary / writing-media /
  binding-speech / sacred-kingship entries above (all added in commit `ce103bf`).
- **Ephemeral `recheck:` values pointing into `.tower/worktrees` or `/tmp`: 0.** Whole-file
  scan of every `- recheck:` line for `\.tower/worktrees|/tmp\b|fleet-aggregate` → no
  match. No `recheck:` value is a filesystem path at all (the single "/"-bearing value is
  math notation in `cartography-and-mapmaking.md`).
- Adjacent, **outside** the flagged class, reported as observations only:
  `knowledge/verification/header-conformance-readings.md:6` —
  `- verified-at: 2026-10-17 — live re-measurement at 21:28–21:30Z on worktree `e3a1ec94…``
  (a worktree named without an ephemeral path and pinned by commit hash);
  `knowledge/verification/gate-frozen-run-standard.md:116` prose "worktree-only baseline is
  not evidence."; `:147` a `/tmp` worked-example drill target. None is a `recheck:` value.

Limits: field-line scan only; no semantic judgment of source quality; this is not a gate
rule and produces no rule verdict; nothing was written to the child repo.

## Gate limitations (named, not worked around)

Gate-declared not-evaluated: r1 (source citation is semantic), r3 (falsifiability), r5
(negative claim sweeps), r6 (quote location), r9 (corrections/rewrite — a `--snapshot`
`git archive` tree carries no history), box-3 non-author verifier, shonen claim truth, and
r8 schematic-vs-real classification (needs a vault read).

Observed in this run, beyond the declarations:

1. r4 is a per-line count-noun heuristic: it fires on version numbers ("1.7 note"), page
   numbers ("329, note"), citation numbers ("291 call") and revision stamps ("1 stamp"),
   and it fails genuine count claims whose command sits on an adjacent line
   (`README.md:118` vs command at `:116`). 199 findings are therefore not 199 measured
   count defects; the verdict is form-level.
2. r2 accepts only commit-hash / `.ufo/reports/` / `LOG.md`; a lesson citing committed
   frozen gate outputs and a MANIFEST sha256 pin still fails `round-3-d2-build.md`'s form.
3. r8's `kv-secret` class cannot distinguish credential syntax from prose word + colon
   (`secret: biblical`), so its one finding here is not credential material.
4. r10's round is the **aggregator's** round, not the lane's LOG round; for a lane with no
   aggregator lesson the finding is selector-insensitive (9/12/49 all fire).
5. r7 under-coverage (405/408 files without an index row) is printed as a note, not a
   finding; r7 skipped 1 backticked template. `SOURCES.md`/`QUALITY.md`/`SHONEN.md` are
   outside r4/r7's canonical surfaces.

## Audit limits

- Opened: `corpus/SOURCES.md` (1–169 in parts), `corpus/README.md` (96–100, 112–160,
  115–123, 128–137), `corpus/QUALITY.md` (full), `SHONEN.md` (full), the four r2 lessons
  (round-1 and round-4-sol full; round-3 :1–23; round-12 by regex only),
  `aksum-ethiopia.md:112–127` + `grep secret`, the flagged lines in
  `arabia-pre-islamic.md`, `hopi.md`, `orality-formulaic-language.md`, heads of
  `funerary-material-culture.md` and `hunting-foraging-subsistence.md`, and the 225
  knowledge blobs' field lines.
- The 199 r4 findings were **sampled**, not individually adjudicated (95 files); the six
  reproductions above are exact but not exhaustive.
- No builds, tests, lint, formatting, or network. `lsp` device unavailable
  (`read xd://lsp` → "No such tool: xd://lsp"; the mounted device list was returned), so
  no reference/definition/diagnostics analysis existed for these Markdown corpora; all
  checks are literal file reads and regex reproductions, not semantic proof.
- No gate/script/child-repo mutation; `mkdir -p` of the seats directory was required to
  write this note.
