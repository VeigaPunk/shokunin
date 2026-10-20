# audit-game-dev-2d — aggregator round 12 seat note (READ-ONLY lane audit)

Seat: KaikaAggregateR12.AuditGameDev2d. Scope: `/home/vgpnk/Projects/shokunin/game-dev-2d-shokunin` only.
Date observed: 2026-10-19. Lane worktree unmodified (`status --porcelain` empty). No child bytes were
edited; the only file written is this note.

**PROVISIONAL — do not freeze.** (a) game-dev-2d r105 is still in flight; this HEAD predates the
round's close. (b) A census-parser fix for indented Markdown source rows is in progress elsewhere;
no census totals are published here. Any number below is a gate finding at one named revision, not a
baseline total. **Recheck owed at the post-FINAL-LANES-READY revision** (re-run the two commands in §1/§2).

## 0. Revision

```
$ git -C /home/vgpnk/Projects/shokunin/game-dev-2d-shokunin rev-parse HEAD
e89905162b3a630a599607279681b30572010724        # exit 0
$ git -C /home/vgpnk/Projects/shokunin/game-dev-2d-shokunin status --porcelain
                                                # empty output, exit 0 — clean tree
```
HEAD top commit: `e8990516 round-104 record (work 5f924226)`; r104 landed as work commit `5f924226`.
Committed LOG.md ends at `- ROUND 104 …` (LOG.md:1311). No r105 entry is committed yet.

## 1. Gate command (canonical invocation, gate default round selector = 9)

```
$ cd /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/fleet-aggregate
$ node .ufo/waves/round-9/corpus-gate.mjs --snapshot /home/vgpnk/Projects/shokunin/game-dev-2d-shokunin e89905162b3a630a599607279681b30572010724
```

Exact stdout (verbatim, complete; exit code **1**):

```text
# corpus-gate-v1 — CORPUS.md rules recomputed (aggregator lane round 9), round-selector=9
# expect game-dev-2d-shokunin@e899051 ABSENT (no committed expected verdict for this revision)
# tree game-dev-2d-shokunin revision=e89905162b3a630a599607279681b30572010724 dirty=0 mode=snapshot
CR-game-dev-2d-shokunin-r4-1: knowledge/seed.md:6 count claim with no backticked command: "corpus/ + round reports). Local copy: corpus/fixtures/ (29 f" (CORPUS.md:28)
CR-game-dev-2d-shokunin-r4-2: lessons/r101-export-capability.md:3 count claim with no backticked command: "Godot's export path was exercised end-to-end on a scratch pr" (CORPUS.md:28)
CR-game-dev-2d-shokunin-r4-3: lessons/r101-ytrans-dead-flag.md:56 count claim with no backticked command: "correct one while |offy| ≤ half the collider height (measure" (CORPUS.md:28)
CR-game-dev-2d-shokunin-r4-4: lessons/r101-ytrans-dead-flag.md:57 count claim with no backticked command: "0 hits at 21 for a 40×40 body). Choose |offy| ≫ half-extent." (CORPUS.md:28)
CR-game-dev-2d-shokunin-r4-5: lessons/r101-ytrans-dead-flag.md:79 count claim with no backticked command: "## Integration fold (2026-10-18, run 1 → run 2)" (CORPUS.md:28)
CR-game-dev-2d-shokunin-r4-6: lessons/r103-simp-gaps-and-print-law.md:9 count claim with no backticked command: "(−10 lines total)." (CORPUS.md:28)
CR-game-dev-2d-shokunin-r4-7: lessons/r103-simp-gaps-and-print-law.md:54 count claim with no backticked command: "| row signature substring (the graded class) | preserved | 2" (CORPUS.md:28)
CR-game-dev-2d-shokunin-r4-8: lessons/r103-simp-gaps-and-print-law.md:59 count claim with no backticked command: "The SP2/SP3 fold deletes 5 lines above those sites, so the s" (CORPUS.md:28)
CR-game-dev-2d-shokunin-r4-9: lessons/r104-evasion-probe-and-disposition.md:92 count claim with no backticked command: "CASES pin and re-check the pin — **2160 rows checked, 0 flip" (CORPUS.md:28)
CR-game-dev-2d-shokunin-r4-10: lessons/r104-evasion-probe-and-disposition.md:146 count claim with no backticked command: "gate variants loaded, 0.059 s to load and 0.039 s to audit a" (CORPUS.md:28)
CR-game-dev-2d-shokunin-r4-11: lessons/r104-gate-boundary-tabpass.md:130 count claim with no backticked command: ""foreign line in span" residual is closed only for the 224 r" (CORPUS.md:28)
CR-game-dev-2d-shokunin-r4-12: lessons/r104-resource-loader-uid.md:65 count claim with no backticked command: "| 6 rows | 153 B | 6 | 4 + Σ(12 + len(path)) = 4 + 12·6 + Σl" (CORPUS.md:28)
CR-game-dev-2d-shokunin-r4-13: lessons/r104-resource-loader-uid.md:66 count claim with no backticked command: "| 2 rows | 70 B | 2 | 4 + 24 + 42 = **70** |" (CORPUS.md:28)
CR-game-dev-2d-shokunin-r4-14: lessons/r104-resource-loader-uid.md:78 count claim with no backticked command: "(5/6/9 rows with the file ending exactly after the rows). Ei" (CORPUS.md:28)
CR-game-dev-2d-shokunin-r4-15: lessons/r47-hslider-reconnect.md:19 count claim with no backticked command: "Tracked branch asserts connection-state transitions, all nin" (CORPUS.md:28)
CR-game-dev-2d-shokunin-r4-16: lessons/r66-rejection-clause-surface.md:87 count claim with no backticked command: "In-run (author receipt, replayed independently): 39 rows / 4" (CORPUS.md:28)
CR-game-dev-2d-shokunin-r8-1: credential-class kv-secret occurrences=2 lines=2 files=2 owner=lane at e899051 literal_shaped=1/2 :: classification=could-not-evaluate (needs a vault read; operator-gated) files=[live/r66-scribe/observations.md,live/r94-verifier/probes/discriminate.py] first=live/r66-scribe/observations.md:161 first4="toke" len=15 (CORPUS.md:43)
CR-game-dev-2d-shokunin-r10-1: no corpus/lessons/round-9-aggregator-*.md — the round-9 review duty has no emitted lesson (CORPUS.md:21)
CR-game-dev-2d-shokunin-shonen-1: SHONEN.md:1 header line deviates from the canonical seed: got "# SHONEN — probation", expected "# game-dev-2d-shokunin — Promotion checklist" (modulo <name>=game-dev-2d-shokunin)
CR-game-dev-2d-shokunin-shonen-2: SHONEN.md:3 box 1 text deviates from the canonical seed: got "Real decision tables/error patterns/checklists with cited sources."
CR-game-dev-2d-shokunin-shonen-3: SHONEN.md:3 header line deviates from the canonical seed: got "- [ ] Real decision tables/error patterns/checklists with cited sources.", expected "Promotion to shokunin requires all of:" (modulo <name>=game-dev-2d-shokunin)
CR-game-dev-2d-shokunin-shonen-4: SHONEN.md:4 box 2 text deviates from the canonical seed: got "End-to-end domain task executed and logged; non-author verifier required."
CR-game-dev-2d-shokunin-shonen-5: SHONEN.md:4 header line deviates from the canonical seed: got "- [ ] End-to-end domain task executed and logged; non-author verifier required.", expected "" (modulo <name>=game-dev-2d-shokunin)
CR-game-dev-2d-shokunin-shonen-6: SHONEN.md:5 box 3 text deviates from the canonical seed: got "Instructions executable without oral context."
CR-game-dev-2d-shokunin-shonen-7: SHONEN.md:6 box 4 text deviates from the canonical seed: got "No cross-domain bleed; PROVINCE remains accurate."
CR-game-dev-2d-shokunin-shonen-8: SHONEN.md:7 is neither the header block, a box line, nor an evidence line (blank line): ""
CR-game-dev-2d-shokunin-shonen-9: SHONEN.md:8 is neither the header block, a box line, nor an evidence line (prose): "Each box may be checked only by a named non-author verifier "
CR-game-dev-2d-shokunin-shonen-10: SHONEN.md:9 is neither the header block, a box line, nor an evidence line (prose): "pointer; self-attestation counts as [~]."
# note game-dev-2d-shokunin r7 under-coverage (not a finding): 40930/40988 corpus files carry no index row
# note game-dev-2d-shokunin r8 kv-secret/lane file-list: live/r66-scribe/observations.md live/r94-verifier/probes/discriminate.py
# note game-dev-2d-shokunin r8 classification=could-not-evaluate (exit-2-class abstention; never guessed) — the literal-text occurrence findings above stand as failed (CORPUS.md:43 reads "stay out of every corpus, including this one's examples")
# note game-dev-2d-shokunin extracted with: git archive e89905162b3a630a599607279681b30572010724 | tar -x -C <tmp>
# verdict game-dev-2d-shokunin failed findings=28 rules=r4,r8,r10,shonen rules-implemented=r2,r4,r7,r8,r10,shonen
# process-exit 1 (failed)
```

## 2. Verdict

**NOT CONFORMANT** (gate class `failed`) at `e89905162b3a630a599607279681b30572010724`, per
`corpus-gate-v1` exit 1. Failed rule IDs: **r4 (16)**: `CR-game-dev-2d-shokunin-r4-1…16`;
**r8 (1)**: `CR-game-dev-2d-shokunin-r8-1`; **r10 (1)**: `CR-game-dev-2d-shokunin-r10-1`;
**shonen (10)**: `CR-game-dev-2d-shokunin-shonen-1…10`. No exit-2 (could-not-evaluate) and no
exit-3 (drift) component; the drift cross-check was unavailable for this revision
("expect … ABSENT" line). This is a mechanically-derived verdict only — see §6 limitations; it is
not a statement about corpus semantics, verifier independence, or SHONEN claim truth.

Round selector: gate default **9** is what the canonical invocation above used (header
`round-selector=9`). Selector sensitivity was checked because the lane's own landed round is 104:

```
$ node .ufo/waves/round-9/corpus-gate.mjs --snapshot <lane> e89905162b3a630a599607279681b30572010724 --round 104
# corpus-gate-v1 — CORPUS.md rules recomputed (aggregator lane round 9), round-selector=104
CR-game-dev-2d-shokunin-r10-1: no corpus/lessons/round-104-aggregator-*.md — the round-104 review duty has no emitted lesson (CORPUS.md:21)
# verdict game-dev-2d-shokunin failed findings=28 rules=r4,r8,r10,shonen rules-implemented=r2,r4,r7,r8,r10,shonen
# process-exit 1 (failed)        -> exit=1
$ ... --round 105
# … round-selector=105
CR-game-dev-2d-shokunin-r10-1: no corpus/lessons/round-105-aggregator-*.md — the round-105 review duty has no emitted lesson (CORPUS.md:21)
# process-exit 1 (failed)        -> exit=1
```

r10 fails under **every** selector at this HEAD — checked directly:

```
$ git -C <lane> ls-files corpus/lessons | grep -cE 'round-[0-9]+-aggregator'
0        # 0 of 212 lesson files; gate key changes with --round, the verdict does not
```

## 3. Finding detail (reviewer read, per-finding)

r4 (CORPUS.md:28 "a count carries its command"): 16 mechanical findings. Exact triggering substrings
(re-derived with the gate's own `COUNT_NOUN_RE` via `grep -noE` over the flagged files; the gate
skips whole lines containing a backtick, which is why other count instances in the same files are
not findings):

| id | location | trigger substring | read |
|---|---|---|---|
| r4-1 | knowledge/seed.md:6 | `29 files` | real count, no command/date on the line; commit `c32adb1` is cited 1 line below but not in `<n> — <command> <date>` form. Minor. |
| r4-2 | lessons/r101-export-capability.md:3 | `2 scripts` | prose count; exact `godot --headless …` command table exists later in the same file (line 10+). Formatting-level. |
| r4-3 | lessons/r101-ytrans-dead-flag.md:56 | `5 hits` | measured boundary counts (pitfall 2); commands live elsewhere in file. Minor. |
| r4-4 | lessons/r101-ytrans-dead-flag.md:57 | `0 hits` | same as r4-3. |
| r4-5 | lessons/r101-ytrans-dead-flag.md:79 | `18, run` | **check artifact**: matched through the date `2026-10-18, run 1 → run 2` (fold header). Not a count claim. |
| r4-6 | lessons/r103-simp-gaps-and-print-law.md:9 | `10 lines` | real (−10 lines fold); diff-derived, no inline command. Minor. |
| r4-7 | lessons/r103-simp-gaps-and-print-law.md:54 | `7 rows` | real (28/28 receipts = 7 rows × pre/post × 2 reps). Minor. |
| r4-8 | lessons/r103-simp-gaps-and-print-law.md:59 | `5 lines` | real (fold deletes 5 lines). Minor. |
| r4-9 | lessons/r104-evasion-probe-and-disposition.md:92 | `2160 rows` | real probe count; command context in file (results JSON). Minor. |
| r4-10 | lessons/r104-evasion-probe-and-disposition.md:146 | `4343 rows` | real cost-audit count. Minor. |
| r4-11 | lessons/r104-gate-boundary-tabpass.md:130 | `224 rows` | real region-reach count. Minor. |
| r4-12 | lessons/r104-resource-loader-uid.md:65 | `6 rows` | real table row (size arithmetic shown inline). Minor. |
| r4-13 | lessons/r104-resource-loader-uid.md:66 | `2 rows` | same as r4-12. |
| r4-14 | lessons/r104-resource-loader-uid.md:78 | `9 rows` | real (5/6/9-row rebuilds). Minor. |
| r4-15 | lessons/r47-hslider-reconnect.md:19 | `1 run` | **near-artifact**: matched inside `a tainted 1/1 run` in a long prose paragraph. Count-claim status borderline. |
| r4-16 | lessons/r66-rejection-clause-surface.md:87 | `39 rows` | real (39/40 dead-entry census). Minor. |

Net: mostly formatting-level gaps (count in prose, command elsewhere in the same lesson); two
flagged lines (r4-5 `18, run`; r4-15 `1/1 run`) are regex-shape artifacts rather than unbacked
counts. All 16 stand as the gate's exact output anyway.

r8-1: the raw matches were read in full. Both are non-secret text, so this is a shape-level
false positive at the mechanical layer; the gate's own classification remains
could-not-evaluate by design:
- `corpus/live/r66-scribe/observations.md:161` — matched text `token: residual` (len 15, first4
  `toke`) inside the prose line `4. Evasion is bounded to splits inside the token: residual
  \`ERROR:\`-bearing …`; value `residual` is an English word.
- `corpus/live/r94-verifier/probes/discriminate.py:51` — matched `TOKEN = re.compile(r"(?P<name>…)")`;
  identifier + Python regex literal.
No credential material found in these two lines; nothing to scrub. (Directive honored: reported as
shape fact, not overridden into a gate pass.)

r10-1: no aggregator lesson exists at this HEAD for any round (see §2). This is the same class as
the lane's own corpus layout gap — recent rounds (r101–r104) landed lane-authored lessons but no
`round-<N>-aggregator-*.md` anywhere.

shonen (1–10): form divergence, exact. Lane `SHONEN.md` at HEAD (9 lines):

```
# SHONEN — probation

- [ ] Real decision tables/error patterns/checklists with cited sources.
- [ ] End-to-end domain task executed and logged; non-author verifier required.
- [ ] Instructions executable without oral context.
- [ ] No cross-domain bleed; PROVINCE remains accurate.

Each box may be checked only by a named non-author verifier with an evidence
pointer; self-attestation counts as [~].
```

Canonical seed (`/home/vgpnk/Projects/shokunin/PROTOCOL.md:439-448`) is
`# <name> — Promotion checklist` / `Promotion to shokunin requires all of:` / four boxes with
different texts; verification is declared mechanical: "the seed block … must diff byte-identical
modulo `<name>` … marks are confined to the box character plus one indented evidence line per box…;
no other prose, added boxes, or removed boxes" (PROTOCOL.md:432). The lane file's header, all four
box texts, and lines 8–9 (prose) diverge; PROTOCOL.md:432 also says the owning lane regenerates
`SHONEN.md` verbatim on its next steered round. All boxes are unchecked, so no verifier-id issue
arises. (Ownership note: SHONEN.md is not corpus; regenerating it silently would violate the
lane's write scope — flag to the parent/operator, do not fix from this seat.)

## 4. SOURCES / index structural observations (not gate rules)

- `corpus/SOURCES.md` is **absent** at HEAD:
  `test -f corpus/SOURCES.md` → absent; `git ls-files | grep -cE '(^|/)[Ss][Oo][Uu][Rr][Cc][Ee][Ss]'` → `0`.
  Per fleet `PROTOCOL.md` §File contract (line 435) it is a declared contract file ("the curated
  source registry, contract v1"), and per `CORPUS.md` §"SOURCES.md — where a shokunin learns" it
  would carry Registry / Paths / Search log / Leads. **No study-path or reading sequence can be
  extracted from it at this HEAD — the surface does not exist.** Leads were not used as evidence.
- `QUALITY.md` is **absent** at HEAD too (`test -f QUALITY.md` → absent), although CORPUS.md's
  layout names it; the lane LOG already carries the routed note "QUALITY.md scribe note (file
  absent — census routed)" (LOG.md r102 ROUTED block).
- `corpus/` splits present: `README.md`, `fixtures/`, `knowledge/`, `lessons/`, `live/`.
  No `corpus/evidence/`, no `corpus/handoffs/` (both are index-eligible subdirs in the gate, so no
  phantom-row risk arose).
- Nearest committed reading path (labelled as such, **not** a SOURCES.md §Paths): `corpus/README.md`
  (24 lines) is an ordered, annotated tour of lessons r1→r19 only — e.g. row
  `lessons/r1-headless-verification.md` ("decision table, observed errors, reproduction checklist
  and source pointers"), `lessons/r3-ui-headless.md` ("synthetic UI signal-to-Label decision
  boundaries and independent 19/19 replay; production/rendered UI remains unprobed"), up to
  `lessons/r19-stream-attribution.md`. It reads as: seed/provenance → per-round capability lessons
  r1–r19, each paired with a verifier JSON. Indexing stops at r19 while 75 `.md` lessons exist
  (`git ls-files 'corpus/lessons/*.md' | wc -l` → 75); the gate counts 40930/40988 corpus files
  unindexed (note, not finding). A usable reading path currently requires the `lessons/` listing
  itself, not an index.
- r7: zero phantom rows at this HEAD (no finding); all index rows that exist resolve.

## 5. Provenance / fidelity scan (parent addendum — bounded to `corpus/knowledge/**/*.md`)

```
$ git -C <lane> ls-files corpus/knowledge
corpus/knowledge/2026-10-12-production-checklist.md
corpus/knowledge/seed.md
$ find corpus/knowledge -type d
corpus/knowledge                                   # no nested dirs
$ grep -nE '^[-* ]*(source|verified-at|recheck) *:' corpus/knowledge/*.md
                                                   # no matches, grep exit 1
$ grep -nE '\.tower/worktrees|/tmp' corpus/knowledge/*.md
                                                   # no matches, grep exit 1
$ git log --diff-filter=A --format='%h %ad %s' --date=short -- corpus/knowledge
0d1e5d71 2026-10-12 Mint game-dev-2d lane (operator directive): books, seed corpus from games research, MANIFEST r21
$ git log -2 --format='%h %ad %s' --date=short -- corpus/knowledge
587561c1 2026-10-13 game-dev-2d r59: verify headless audio bus resolution
c47ab5da 2026-10-13 game-dev-2d r58: verify save across Godot processes
```

Both files are mint-era (`0d1e5d71`, 2026-10-12), last touched 2026-10-13; **no knowledge file was
added in r104/r105**, so the scan is complete for the current HEAD rather than a sample.

Findings (provenance/fidelity class, not a gate rule or semantic verdict):
- **0 of 2** knowledge files carry any of `source:` / `verified-at:` / `recheck:` — the trio rule
  ("A new knowledge entry opens with its provenance trio", CORPUS.md kaika section) is unmet by
  both files. `seed.md` does cite its upstream repo + commit `c32adb1` in prose; the checklist
  cites verifier JSON paths in its table but no frontmatter trio.
- **Exact `recheck:` values pointing into ephemeral `.tower/worktrees` or `/tmp`: the set is
  empty** — there are no `recheck:` lines at all in this lane's knowledge files (checked with the
  two commands above). So no ephemeral-provenance item to route for this lane; reported as
  checked-and-none.
- Whether the trio duty retroactively binds these two pre-kaika files (seed inherited 2026-10-11/12;
  checklist mint-dated 2026-10-12) is a parent/curator call — recorded as observation, not adjudicated.

## 6. Gate limitations (explicit, so nothing above is over-read)

- r2 implemented but **vacuous for this lane**: the check only evaluates lessons whose filename
  matches `round-(\d+)`; this lane names lessons `r<N>-*`, so 0 of 75 `.md` lessons were evaluated
  (`git ls-files corpus/lessons | grep -cE 'round-[0-9]'` → `0`). Zero r2 findings = zero coverage.
- r4 is same-line and whole-line: any backtick anywhere on the line suppresses the check;
  adjacent-line/table-context commands still fail, and date-adjacent tokens (`18, run`) can fire.
- r7 grades phantom rows only; under-coverage is a note (98.8% here).
- r8's real-vs-schematic classification is declared could-not-evaluate (needs a vault read,
  operator-gated); the gate never guesses it, and the literal-text findings "stand as failed" by
  design even where (as read in §3) both matches are prose/identifier text.
- r10 is round-selector-dependent (key/`--round`), and `--snapshot` grades a `git archive` tree with
  no history — r9's authorship sub-check is unavailable by construction; r1/r3/r5/r6/r9 are declared
  not-evaluated. Verifier independence and SHONEN claim truth are not evaluated.
- No frozen expectation covers `e899051` (`expect … ABSENT`): a pass here would not have been
  cross-checked against `corpus-gate.expected.json`, and exit-3 drift could not fire.
- SHONEN check grades canonical FORM only; box content is prose. Label is the directory basename,
  and the observed failure is independent of that naming (`# SHONEN — probation` ≠ any `<name>`
  form).
- Gate pass/fail ≠ whole-corpus semantic conformance: r1/r3/r5/r6/r9, verifier independence, and
  SHONEN truth remain declared not-evaluated.

## 7. Residual risk / recheck owed

- HEAD is provisional: r105 in flight; the 16 r4 + 10 shonen + r10 findings are cheap to re-run —
  re-run §1 command verbatim after **FINAL LANES READY** and re-check r4 counts (a fold may already
  fix formatting), SHONEN regeneration (PROTOCOL.md:432 duty), and any new `round-105-aggregator` lesson.
- r8-1 will persist as long as the two non-secret matches exist; if the fleet wants a cleaner r8
  signal, that is a gate/pattern refinement question (aggregator-side), not lane cleanup.
- `corpus/SOURCES.md` absent + `QUALITY.md` absent are structural gaps against the fleet file
  contract (PROTOCOL.md:435; CORPUS.md layout): they will keep any round-12 SOURCES-structural
  census zero for this lane until landed. No census totals published from this seat (parser fix
  pending elsewhere).