# Audit — audio-shokunin (aggregator round 12, seat KaikaAggregateR12.AuditAudio)

Read-only audit. No child repo was edited, staged, or committed; the only write is this note.
Lane path audited: `/home/vgpnk/Projects/shokunin/audio-shokunin` (original repo path, not a worktree).

## 1. Revision identity (observed 2026-10-19T23:44Z)

```
$ git -C /home/vgpnk/Projects/shokunin/audio-shokunin rev-parse HEAD
defbe128649268bfca75757cb3978be802696592          # exit 0
$ git -C /home/vgpnk/Projects/shokunin/audio-shokunin status --porcelain
                                                   # empty output, exit 0, 0 bytes
```

HEAD is `cleanup: drop regenerable round scratch/baseline snapshot trees` (2026-10-18). Working tree is
clean, so live-mode grading and snapshot-mode grading see the same content (gate reported `dirty=0`; no
untracked-corpus note was emitted).

**PROVISIONAL.** Audio round 101 is still in flight (no r101 artifacts exist in this repo: no
`reports/round-101/`, no `r101` string in `LOG.md`; the highest completed round on record is 100 —
`reports/round-100/` holds 13 files). Nothing here is frozen; a recheck is owed after the parent's exact
`FINAL LANES READY` signal.

## 2. Gate run — required `--snapshot` invocation

Command (cwd `/home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/fleet-aggregate`):

```
node .ufo/waves/round-9/corpus-gate.mjs --snapshot /home/vgpnk/Projects/shokunin/audio-shokunin defbe128649268bfca75757cb3978be802696592
```

Observed output (identical on two runs; second run at 2026-10-19T23:44:51Z):

```
# corpus-gate-v1 — CORPUS.md rules recomputed (aggregator lane round 9), round-selector=9
# expect audio-shokunin@defbe128649268bfca75757cb3978be802696592 ABSENT (no committed expected verdict for this revision)
# tree audio-shokunin revision=defbe128649268bfca75757cb3978be802696592 dirty=0 mode=snapshot
# note audio-shokunin git archive defbe128649268bfca75757cb3978be802696592 failed:
# verdict audio-shokunin could-not-evaluate findings=0 rules=none rules-implemented=r2,r4,r7,r8,r10,shonen
# process-exit 2 (could-not-evaluate)
```

**Exit 2 (could-not-evaluate) — twice, reproducibly.** The `--snapshot` path therefore yields **no
conformance verdict** for this lane, and no failed rule IDs from this invocation (there are none to
report: the grader never ran).

Gate-side root cause (not a lane defect, but it makes the required invocation unusable here): the gate
buffers the whole archive in memory at `corpus-gate.mjs:602` —
`spawnSync('git', ['-C', abs, 'archive', commit], { maxBuffer: 1 << 30 })` = 1,073,741,824 B — while this
lane's archive is larger:

```
$ git -C /home/vgpnk/Projects/shokunin/audio-shokunin archive defbe128649268bfca75757cb3978be802696592 | wc -c
1384069120            # 1.29 GiB > 1 GiB maxBuffer
```

The overflow leaves `status === null` with empty stderr, which the gate renders as
`git archive ... failed:` with an empty reason (checked against the gate source at line 602-603, not
guessed). Any lane whose archive exceeds 1 GiB will hit the same CNE.

## 3. Gate run — supplementary live-mode grading (same revision, clean tree)

Because the snapshot path aborts before grading, I graded the same content through the gate's live entry
point (still the existing gate, unmodified):

```
node .ufo/waves/round-9/corpus-gate.mjs --repo /home/vgpnk/Projects/shokunin/audio-shokunin
```

Observed: `# verdict audio-shokunin failed findings=19 rules=r4,r7,r8,r10,shonen
rules-implemented=r2,r4,r7,r8,r10,shonen` — **exit 1 (failed)**, reproduced twice (exit 1 both runs).
JSON form (`--json`, parsed from the `# json ` line):

```
stats.files = 49219   (corpus files walked)
stats.rules = { r2: 0, r4: 1, r7: 1, r8: 2, r10: 1, shonen: 14 }
revision    = defbe128649268bfca75757cb3978be802696592 (worktree), dirty = 0
```

### Round selector (derived, stated explicitly)

Lane round, from committed history: the highest completed lane round is **100** (`reports/round-100/`
holds 13 files; `LOG.md:1529` references r100), with r93/r98/r99/r100 fold bullets in `LOG.md`; **r101 is
not committed** (no `r101` string in `LOG.md`, no `reports/round-101/`). The gate's `--round` is *not* a
lane-round selector — it is the aggregator round, default **9**, as the gate's own header states
(`aggregator lane round 9`, `round-selector=9`). I did not pass `--round`; the default 9 is therefore the
explicit gate selector for both gate invocations in this note (snapshot §2, live §3).

### Verdict

**not conformant at `defbe128649268bfca75757cb3978be802696592`** under live-mode grading (exit 1, failed,
19 findings). The task's required `--snapshot` invocation cannot support any verdict at this revision: it
exits 2 (could-not-evaluate) before reading the corpus. Both statements hold simultaneously; neither is
substituted for the other.

### Exact failed rules and findings

- **r4 ×1** — `corpus/knowledge/2026-10-13-sox-validbits-codec-map.md:3`: count claim with no backticked
  command. Exact line bytes (`sed -n '3p' | cat -A`):
  `- Source: round-64 seat evidence M-bM-^@M-^T scribe's independent 85-variant sweep$` — no backtick on
  the line (the citations sit on the indented continuation lines 4-6). Mechanical rule CORPUS.md:28; the
  gate does not judge intent. Form-side check on the implicated lesson: all paths it cites resolve at HEAD
  (`corpus/live/r64-scribe/{results.tsv,manifest.sha256,gen_sweep.py,sweep.sh}`,
  `corpus/live/round-64/pair_valid_{8,25}.wav` all PRESENT via `git cat-file -e HEAD:<path>`).
- **r7 ×1** — `corpus/README.md is absent — no index exists (CORPUS.md:11,40)`. The gate's index surface
  is `corpus/README.md`; this lane has no such file at HEAD, so the r7 index check never parsed rows and
  the usual "under-coverage" note was not emitted.
- **r8 ×2** — literal credential-class occurrences, unit = occurrences:
  `cookie occurrences=54 lines=54 files=47 literal_shaped=31/54` and
  `kv-secret occurrences=9 lines=9 files=9 literal_shaped=0/9`; owner `lane`, revision
  `defbe12(worktree)`. The gate declares the schematic-vs-real classification itself
  could-not-evaluate (needs a vault read, operator-gated) and routes by owner; the literal occurrences
  stand as failed per CORPUS.md:43. Bounded sampling of the first hit of each family (shapes only, values
  not reproduced beyond what the gate already prints): `corpus/live/r73-simplifier/pactl-pwrt-down.txt:15`
  is a `pactl` probe header line `Cookie: 2a06:5f75`; `corpus/live/r90-verifier/runs/laws-v1.json:408` is a
  law-detail string `token='536870921'`. Sampled hits look like probe stdout / law JSON fields rather than
  live secrets — that is a sample of 2 of 63 occurrences, not a classification, and I did not read a
  vault.
- **r10 ×1** — `no corpus/lessons/round-9-aggregator-*.md — the round-9 review duty has no emitted lesson
  (CORPUS.md:21)`. The lane has **no `corpus/lessons/` directory at all** at HEAD, and no file named
  `*aggregator*` anywhere in the repo (`find . -path ./.git -prune -o -name '*aggregator*' -print` → no
  output). Consequence: **r2's clean result is vacuous** — the gate's rule list shows r2 implemented with
  0 findings only because `lessons/` contains no `.md` files to check.
- **shonen ×14** — `SHONEN.md` canonical-form deviations: header line is `# SHONEN — probation` where the
  canonical seed expects `# audio-shokunin — Promotion checklist` (modulo `<name>`); the four box texts
  deviate from the canonical seed wording; each of the four `[x]` boxes carries **no indented evidence
  line with a resolvable pointer** (evidence is inline on the box line, e.g.
  `` `audio-r1-verifier`; evidence: `.shokunin/reports/audio-r1-verifier.md` ``); and `SHONEN.md:8-9` carry
  trailing prose that is neither header, box, nor evidence line. This is form only — the gate's
  verifier-independence and box-truth checks are declared not evaluated (see §5).

## 4. SOURCES structural observations (separate from the gate verdict)

- **No `corpus/SOURCES.md` exists at HEAD.** `git cat-file -e HEAD:corpus/SOURCES.md` and
  `HEAD:SOURCES.md` both fail (ABSENT). Same for `QUALITY.md`, `corpus/QUALITY.md`, `SKILL.md`,
  `corpus/README.md`, and `corpus/lessons` (all ABSENT at HEAD; verified individually with
  `git cat-file -e`).
- **README claim vs tree.** `README.md` (present, tracked) declares under "What's here":
  `` `SKILL.md` `` (with an explicit caveat "absent on lanes still in shonen seed form"), `` `corpus/` —
  the craft record: `knowledge/` …, `lessons/` (per-round), `QUALITY.md` (the admission bar) ``. At this
  HEAD `corpus/lessons/` and `corpus/QUALITY.md` do not exist and carry no caveat — the README describes
  an admission bar and a per-round lesson tree the committed corpus does not contain. Recorded as a
  document/tree divergence at a named revision, not as a semantic judgment about the lane's work.
- **Where source provenance actually lives.** The only `SOURCES.md` files in the lane are per-round scout
  provenance records: `corpus/live/r91-scout/sources/SOURCES.md`, `corpus/live/r95-scout/sources/SOURCES.md`,
  `corpus/live/r98-scout/sources/SOURCES.md` (plus sibling `.sha256` ledgers such as `SOURCES.sha256`,
  `FETCHED-SOURCES.sha256`, `WP-LUA.sha256`). Their structure is consistent: title, version-match table
  against the installed packages, a fetched-files table with upstream URL + sha256 (r95 also a `used for`
  column), and key anchors as `file:line-range` with a one-line claim. r98 additionally keeps three
  wrong-path fetches (`adapter.c`, `audioconvert-adapter.c`, `impl-node-rt.c`) as explicit 88-line
  GitLab-404 artifacts and names the labrat that caught the corruption — a self-disclosed bad fetch, not a
  silent one.
- **Census-relevance (provisional).** The parent reports a census parser fix in progress for indented
  Markdown source rows. In this lane, none of the three `SOURCES.md` files contains an indented table or
  bullet row (`grep -nE '^[[:space:]]+[|*-]'` → no matches in all three); rows are column-0 table rows.
  The rows that could still confuse a naive row counter are the `…/1.6.8/…` URL abbreviations in the r91
  and r98 tables (the full URLs live only in the first row and in the `.sha256` ledgers). No census total
  from this lane should be frozen before the parent's fix lands and `FINAL LANES READY` is given.
- **Provenance frontmatter scan (`corpus/knowledge/**/*.md`, parent-requested, bounded).** These files use
  prose provenance bullets, not YAML frontmatter — no `source:`/`verified-at:`/`recheck:` keys exist.
  Counting `- Source:` / `- Verified at:` / `- Recheck when:` bullets per file
  (`for f in $(git ls-files corpus/knowledge); do git show HEAD:$f | grep -cE '^\- (Source|Verified at|Recheck when)|^(source|verified-at|recheck):'; done`):
  3 bullets each in the 9 sox_ng/transport lessons (`2026-10-13-sox-act-autodetect-predicate.md`,
  `2026-10-13-sox-ffmpeg-packet-residue.md`, `2026-10-13-sox-validbits-codec-map.md`,
  `2026-10-14-sox-autodetect-preemptor-ordering.md`, `2026-10-14-sox-extension-suffix.md`,
  `2026-10-14-sox-fifo-hold-bound.md`, `2026-10-14-sox-posttable-fallback.md`,
  `2026-10-14-sox-preemptor-map-complete.md`, `2026-10-14-sox-transport-axis.md`), and **0** in
  `2026-10-12-audio-checklist.md`, `2026-10-12-fixture-battery.md`,
  `2026-10-12-threshold-calibration.md`, `2026-10-14-ffmpeg-cross-decoder-transport.md`, `seed.md`.
  **Ephemeral-path fidelity finding: none in `corpus/knowledge`.** `git grep -E '\.tower/worktrees|/tmp/'
  HEAD -- corpus/knowledge` → 0 matches (0 files). So no `Recheck when:`/`Verified at:` value in this
  lane's knowledge tree points into a `.tower/worktrees` scratch tree or `/tmp`. For bounded context only
  (outside the requested knowledge scope, no verdict attached): 2283 files under `corpus/` mention such
  paths, first examples `corpus/fixtures/measure_audio.py`, `corpus/live/r67-critic/NOTES.md`,
  `corpus/live/r68-author/matrix-r68.json` — raw capture/probe artifacts, not provenance fields.

## 5. Study path / reading sequence

**No extractable study path from `corpus/SOURCES.md` — the file does not exist at this revision** (see §4),
so there is nothing to quote and I am not substituting a lead for evidence.

Nearest directly-evidenced in-lane sequence, quoted from a committed file I opened —
`corpus/knowledge/seed.md` (present at HEAD), section "Production map (candidate round claims, north to
south)":

```
sfx:    UI blips → impacts (layered noise+sine transients) → movement
        (footsteps: filtered noise bursts, variation via jitter) → ambience
        (looped brown-noise beds with slow LFO)
music:  motif → loop with clean seam → layered stems (base/drum/lead) →
        adaptive crossfade between intensity states
format: wav (master) → ogg (ship) → loop-point metadata; headless checks at
        each step
```

This is a production/skill progression, **not** a source-reading order; it is offered only because the
requested artifact is absent. The same file also carries the lane's verification discipline ("Every audio
claim is a measurement, not a listen") and a host toolchain census probed 2026-10-12.

## 6. Named gate limitations (what this audit does not establish)

1. The gate itself declares not evaluated: **r1, r3, r5, r6, r9**, verifier independence (`box-3`), and
   SHONEN box truth (`shonen-semantics`). Implemented and evaluated here: r2, r4, r7, r8 (literal text
   only), r10, shonen form.
2. **`--snapshot` is unusable for this lane** (exit 2 CNE, §2); the §3 verdict comes from live-mode
   grading of a clean tree, which is content-equivalent here but is not the same code path, and live mode
   can see untracked corpus files (none present: `status --porcelain` empty).
3. r8's schematic-vs-real classification is an exit-2-class abstention (needs a vault read, operator-gated);
   the 63 literal occurrences are unresolved as to whether any is a real credential.
4. A gate pass or a structurally clean SOURCES reading would not establish whole-corpus semantic
   conformance; here there is no gate pass to misread (exit 2 / exit 1), and the SOURCES observations in
   §4 are structural only.
5. `resume_continuity_v1`: the reviewer-role bullet does not apply to this lane — there is no
   resume/preflight path in its fixtures. My own `grep -rn resume_continuity -l .` hits only files under
   `reports/` (r72, r73, r76, r82, r83, r90), and the lane's own record says so explicitly:
   `reports/round-73/r73-reviewer.md:393-397` — "`resume_continuity_v1` is not applicable to this lane …
   Recorded as absence-of-surface, not as a pass." I did not re-derive the lane's internal claim beyond
   this path check.
6. Counts quoted here (findings=19, corpus files=49219, r8 occurrences 54/9, lane-wide ephemeral-file
   count 2283) are **provisional** revision-bound observations at `defbe128`, taken while r101 is
   unfinished and while the census parser fix is in flight. Do not publish them as final census totals.

## 7. Recheck owed after `FINAL LANES READY`

- Re-run §2 and §3 at audio r101's final HEAD (expected to differ from `defbe128`); do not carry this
  verdict forward to a later revision.
- Re-check whether r101 adds `corpus/lessons/` (would give r2 non-vacuous content). r10 will keep firing
  regardless of lane-round progress unless a `corpus/lessons/round-9-aggregator-*.md` exists: the gate's
  `--round` selector is the **aggregator** round (default 9), not the lane's own round, and I did not
  override it. Also re-check whether the README's declared `corpus/lessons/` + `corpus/QUALITY.md` are
  created or the README corrected.
- The `--snapshot` CNE is a gate-side limit (1 GiB maxBuffer, `corpus-gate.mjs:602`) and will persist at
  any revision of this lane; the parent may want to grade this lane via `--repo` deliberately, or the
  gate's buffer raised — either way the choice is the parent's, not mine to make.
