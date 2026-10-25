# audit-lore — aggregator round 12, lane lore-shokunin

- Date: 2026-10-19
- Lane (original path, per parent directive; not a retired worktree): `/home/vgpnk/Projects/shokunin/lore-shokunin`
- Graded revision: `6e804e2e5bff0edcc260c995a058dd724b0c98c0` — commit subject `round-103 verifier spot-check (integrator, kaika): non-author admit/reject sample + adjudication`
- Gate: `corpus-gate-v1`, script at `/home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/fleet-aggregate/.ufo/waves/round-9/corpus-gate.mjs`, `--snapshot` mode (grades a `git archive` of the named commit; the lane working tree is not graded)
- This note reports: gate verdict, SOURCES structural observations, one directly evidenced study path, and a bounded provenance-frontmatter scan. It is **not** a semantic corpus verdict and produces **no numeric score**.

## Revision and tree state (exact commands, observed outputs, exits)

1. `git -C /home/vgpnk/Projects/shokunin/lore-shokunin rev-parse HEAD`
   → `6e804e2e5bff0edcc260c995a058dd724b0c98c0`, exit 0.
2. `git -C /home/vgpnk/Projects/shokunin/lore-shokunin status --porcelain`
   → `?? .scratch/` (only untracked path), exit 0. Run before and after this audit; identical both times, so this audit did not mutate the lane.
3. `git -C ... log --oneline -6`
   → `6e804e2`, `dcfecc5`, `74384c9`, `3317313`, `6cec83a`, `1659a42`.
   `git rev-parse dcfecc57a^{commit}` → `dcfecc57a1d3d118a7022a07b54be4505d30b2e2`, exit 0 (the post-review commit cited by the lessons resolves).
4. `git -C ... ls-tree -r --name-only HEAD -- corpus/lessons`
   → `corpus/lessons/round-103-verifier-spotcheck.md`, `corpus/lessons/round-103.md` (2 files; neither matches `round-<N>-aggregator-*`).

Round-selector derivation: the committed `LOG.md` tail ends at
`## Round 103 — kaika campaign: declaration, gate and landing (2026-10-19)` and
`## Round 103 — post-review corrections (2026-10-19)`. Latest committed lane round = **103**, so the
primary gate run uses `--round 103`. The gate's default is 9. Sensitivity was tested at 9, 12, and 103:
the 16 r4 findings are byte-identical and r10 fires in all three runs (only the r10 key/text changes),
because no `corpus/lessons/round-*-aggregator-*.md` exists for any round at this revision.

## Verdict

**not conformant** at `6e804e2e5bff0edcc260c995a058dd724b0c98c0` — gate exit **1** with **17 findings
(r4 ×16, r10 ×1)**.

Primary command:

```
cd /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/fleet-aggregate \
  && node .ufo/waves/round-9/corpus-gate.mjs \
       --snapshot /home/vgpnk/Projects/shokunin/lore-shokunin \
       6e804e2e5bff0edcc260c995a058dd724b0c98c0 --round 103
```

Observed stdout (verbatim), then exit:

```
# corpus-gate-v1 — CORPUS.md rules recomputed (aggregator lane round 9), round-selector=103
# expect lore-shokunin@6e804e2 ABSENT (no committed expected verdict for this revision)
# tree lore-shokunin revision=6e804e2e5bff0edcc260c995a058dd724b0c98c0 dirty=0 mode=snapshot
CR-lore-shokunin-r4-1: knowledge/holder-assessment-boundary.md:21 count claim with no backticked command: "three times after that: round-87 seat C1 added the per-recor" (CORPUS.md:28)
CR-lore-shokunin-r4-2: knowledge/holder-assessment-boundary.md:321 count claim with no backticked command: "- Ambiguous SOURCE is not a stop cause. A source ID resolvin" (CORPUS.md:28)
CR-lore-shokunin-r4-3: knowledge/holder-assessment-boundary.md:606 count claim with no backticked command: "parity at r90; and the r90 fixture-only census (160 → 164 di" (CORPUS.md:28)
CR-lore-shokunin-r4-4: knowledge/holder-assessment-boundary.md:608 count claim with no backticked command: "five live r85 probes; it is a different scope. The r90 prove" (CORPUS.md:28)
CR-lore-shokunin-r4-5: knowledge/holder-assessment-boundary.md:646 count claim with no backticked command: "pasted-block replay, the r90 census, and CB1's scratch cause" (CORPUS.md:28)
CR-lore-shokunin-r4-6: knowledge/r102-freshness-sweep.md:107 count claim with no backticked command: "- full census (checker over all 174 fixture dirs) → 174 dirs" (CORPUS.md:28)
CR-lore-shokunin-r4-7: knowledge/r102-freshness-sweep.md:109 count claim with no backticked command: "- r5 table re-run (6 rows, all exact, quoted in the F1 adden" (CORPUS.md:28)
CR-lore-shokunin-r4-8: knowledge/r102-freshness-sweep.md:110 count claim with no backticked command: "- r93 heredoc replay → exit 0, 5/5 fields" (CORPUS.md:28)
CR-lore-shokunin-r4-9: knowledge/r102-push-synthesis-r95-r102.md:25 count claim with no backticked command: "- **r95–r98 — the deepseek-flash regimen (4 × 64 seats).** F" (CORPUS.md:28)
CR-lore-shokunin-r4-10: knowledge/r102-push-synthesis-r95-r102.md:93 count claim with no backticked command: "declared files each, schema-2 pin payload, guarded integrati" (CORPUS.md:28)
CR-lore-shokunin-r4-11: knowledge/r102-push-synthesis-r95-r102.md:95 count claim with no backticked command: "foreign paths). Census: 174 fixture directories (175 lines f" (CORPUS.md:28)
CR-lore-shokunin-r4-12: knowledge/r102-push-synthesis-r95-r102.md:164 count claim with no backticked command: "12. **The corpus remains examination, not canon:** 174 direc" (CORPUS.md:28)
CR-lore-shokunin-r4-13: knowledge/r102-push-synthesis-r95-r102.md:189 count claim with no backticked command: "brief and roster were V01–V19 (2 producers + 19 verifiers = " (CORPUS.md:28)
CR-lore-shokunin-r4-14: knowledge/r99-gate-blind-spot-table.md:383 count claim with no backticked command: "19 cases; replayed by seats V03/V05/V20 and the r101 adjudic" (CORPUS.md:28)
CR-lore-shokunin-r4-15: lessons/round-103.md:26 count claim with no backticked command: "- **r53** — LOG.md:908 — "its “496 files (all corpus JSON pl" (CORPUS.md:28)
CR-lore-shokunin-r4-16: lessons/round-103.md:67 count claim with no backticked command: "### Source gate records (contract rule 1 — URL, access date," (CORPUS.md:28)
CR-lore-shokunin-r10-1: no corpus/lessons/round-103-aggregator-*.md — the round-103 review duty has no emitted lesson (CORPUS.md:21)
# note lore-shokunin r7: 4 backticked path template(s)/glob(s) skipped (contain *, <, {, ~, $ or …)
# note lore-shokunin r7 under-coverage (not a finding): 1827/1858 corpus files carry no index row
# note lore-shokunin extracted with: git archive 6e804e2e5bff0edcc260c995a058dd724b0c98c0 | tar -x -C <tmp>
# verdict lore-shokunin failed findings=17 rules=r4,r10 rules-implemented=r2,r4,r7,r8,r10,shonen
# process-exit 1 (failed)
```

Exit: **1**.

Exact failed rule IDs:
- `CR-lore-shokunin-r4-1` … `CR-lore-shokunin-r4-16` — r4, count claim with no backticked command (CORPUS.md:28).
- `CR-lore-shokunin-r10-1` — r10, no `corpus/lessons/round-103-aggregator-*.md` (CORPUS.md:21).

Selector runs (same graded commit):
- Default (`--round` omitted → 9): identical 16 r4 lines; r10 text `no corpus/lessons/round-9-aggregator-*.md`; `# verdict … findings=17 rules=r4,r10`; exit 1.
- `--round 12`: identical 16 r4 lines; r10 text `no corpus/lessons/round-12-aggregator-*.md`; `# process-exit 1 (failed)`; exit 1.

No r2, r7, r8, or SHONEN finding at this revision. The two r7 notes are explicitly not findings. The line
`# expect lore-shokunin@6e804e2 ABSENT` means no frozen expected verdict exists for this revision; the
exit-3 drift path was not reached.

## Lesson lines implicated by the gate findings (read at source)

- `CR-lore-shokunin-r4-15` → `corpus/lessons/round-103.md:26`, inside `## Mistakes` → `### Outside checks
  that disagreed with the gate`. The line quotes the r53 erratum from `LOG.md:908` ("its “496 files (all
  corpus JSON plus checker)” is not the fixture-JSON count") and says the verifier miscounted from
  fixtures-cwd argv. The 496 figure is recorded as a rejected measurement, not asserted as a lane
  measurement; the literal rule still flags the line (count noun, no backticked command).
- `CR-lore-shokunin-r4-16` → `corpus/lessons/round-103.md:67`, the heading `### Source gate records
  (contract rule 1 — URL, access date, located quote ≤25 words)`. The count-noun match is `≤25 words`
  (a quote-length bound), not a measurement claim; this is a literal-mechanical match on heading prose.
- The other 14 r4 findings name `corpus/knowledge/*.md` lines (`holder-assessment-boundary.md` ×5,
  `r102-freshness-sweep.md` ×3, `r102-push-synthesis-r95-r102.md` ×5, `r99-gate-blind-spot-table.md` ×1).
  Those files were not re-read in this audit (inspect scope); the excerpts above are the gate's own
  evidence text.
- `CR-lore-shokunin-r10-1`: the lessons dir at HEAD contains only `round-103.md` and
  `round-103-verifier-spotcheck.md` (ls-tree above). No aggregator-authored lesson for round 103 (or
  any round) is present. r10 checks presence only; it does not judge the review's content.

## SOURCES structural observations — PROVISIONAL census

`corpus/SOURCES.md` at `6e804e2` is 78 lines; headings: `## Registry` :5, `## Paths` :42,
`## Search log` :52, `## Leads (unopened)` :64. Registry rows S001–S032 occupy lines 9–40 (32 rows).

**Provisional:** a census parser fix for indented Markdown source rows is in progress elsewhere
(parent direction), so these totals must not be frozen or published as final. They are the contract's
census block (CORPUS.md §Census), run from the lane root; that block matches only `^|` rows, and this
revision has **0** indented pipe rows, so the in-progress fix is not expected to change this lane's
count — stated as an expectation, not a frozen total.

Commands (cwd `/home/vgpnk/Projects/shokunin/lore-shokunin`) and observed output:

```
grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md          → 32
awk malformed rows (NF!=13; must be 0)                                       → 0
awk tier histogram                                                           → A=24 B=3 C=5
awk status histogram                                                         → mined=12 queued=17 rejected=3
awk duplicate ids | sort | uniq -d (must be empty)                           → (empty)
awk enum / tier-inflation check (must be empty)                              → (empty)
grep -cE '^[[:space:]]+\|' corpus/SOURCES.md                                 → 0
awk mined used-by paths, test -e each (must be empty)                        → (empty; no missing paths)
```

All commands exited 0; the three "must be empty" pipelines printed nothing.

Source-shape observations from the file itself:
- Registry confirmation of the post-review correction: S020–S023 are `queued`; S032 (tier A) opens its
  `teaches` with `supersedes S023 —`.
- `## Paths` (:42–51) has 6 reading sequences plus one correction bullet at :50: the In-world time path's
  related entry was rejected at re-grade and moved to
  `.ufo/waves/round-103/rejected/r103-in-world-dating-and-uncertain-time.md`; that path "stands as a study
  sequence only."
- `## Search log` (:52–63) has 8 prose notes, including the explanation that S012 and S017 share one URL
  by design (scoped tiers) and that append-only rule 2 forbids editing S017.
- `## Leads (unopened)` (:64–78) is explicitly unopened; **not used as evidence** in this note.

## Directly evidenced study path (from `corpus/SOURCES.md` §Paths)

`corpus/SOURCES.md:49` — **Supersession and canon status — S024 → S025 → S026 → S001 → S027**:
"statements-not-truth and ranks, then why deprecation keeps rather than deletes, then revision vs
invalidation vs alternate, then PROV-O as the lane's existing provenance vocabulary, ending with one
community illustration that tiers are declarations." Related admitted entry named on that line:
`corpus/knowledge/r103-canon-status-and-supersession.md`.

Evidence checked against the same HEAD:
- Registry rows all exist and are `mined`, `opened 2026-10-19`: S024 (tier A), S025 (B), S026 (A),
  S001 (A), S027 (C).
- `git cat-file -e HEAD:corpus/knowledge/r103-canon-status-and-supersession.md` → exit 0 (present).
- `grep -o 'S0[0-9][0-9]' <entry> | sort | uniq -c` → S024 ×6, S025 ×6, S026 ×9, S027 ×6 — the entry
  cites S024–S027 only, matching the parenthetical on the path line.
- Entry header lines 1–4: `source:` (S024–S027 with anchors), `verified-at: 2026-10-19`, `recheck:`
  (round sweep plus S024–S026 180d cadence), `coverage-row: CM-e`;
  `grep -c '^coverage-row: CM-e$' <entry>` → 1, exit 0 (the CM-e `verify` cell in `corpus/README.md`).
- The adjacent In-world time path (:48) is demoted by the :50 correction to study-sequence-only status and
  is not used here as an admitted reading path; its rejected entry file exists in the lane's
  `.ufo/waves/round-103/rejected/` directory (`ls` exit 0).

## Provenance frontmatter scan (bounded; parent addendum)

Scope: all `corpus/knowledge/*.md` at HEAD — 25 files; `find corpus/knowledge -mindepth 2 -name '*.md'`
→ 0, so `**/*.md` equals `*.md`. The round-103 addition in `corpus/` is
`r103-canon-status-and-supersession.md` (the CM-c entry was moved out of corpus at post-review).

Observed:
- Header-trio presence (line-start matches): `source:` 13/25, `verified-at:` 13/25, `recheck:` 12/25.
  Historical header debt is already recorded in `corpus/README.md` Known gaps.
- `grep -nE '^(source|verified-at|recheck):.*(\.tower/worktrees|/tmp)' corpus/knowledge/*.md`
  → **no matches**, exit 1. No frontmatter `recheck:` (or `source:`/`verified-at:`) value points into
  `.tower/worktrees` or `/tmp`.
- New entry's exact `recheck:` value (`corpus/knowledge/r103-canon-status-and-supersession.md:3`):

  ```text
  recheck: re-run `grep -rniE 'retcon|canon[ -](tier|status)|supersed' corpus/knowledge corpus/fixtures corpus/tools` each round and before integrating any cluster that declares a supersession, rank, or canon-tier record; re-open S024–S026 on a 180d cadence or before the lane encodes rank semantics in a checker.
  ```

  Lane-relative; no ephemeral path.
- Bounded extra observation (**body text, not frontmatter**; reported as a provenance/fidelity fact, not
  as a gate rule or semantic verdict): `/tmp` appears in 6 body lines across 2 files —
  `corpus/knowledge/holder-assessment-boundary.md:502` (`/tmp/cb1/probes2`, `/tmp/cb1/probes3`) and `:623`
  (`scratch under /tmp/cb1/`; the same note discloses at :503–504 that `/tmp` reached inode exhaustion);
  `corpus/knowledge/r91-c9-watch.md:105,118,131,144` (replay commands run against
  `/tmp/lore-X1-r92-*` directories). No `.tower/worktrees` occurrence anywhere under `corpus/knowledge`
  (grep exit 1).

## Gate limitations (explicitly named)

Per `corpus-gate-v1`'s own registry (echoed by `--registry`; read at the gate source):
- **Not evaluated:** r1 (source citation semantics), r3 (falsifiability/opinion), r5 (negative claim
  carries its sweep), r6 (quote names its location), r9 (corrections-are-new-entries / no lane edits
  another's corpus), box-3 (whether an `[x]` mark rests on a non-author verifier — needs an authorship
  graph the graded tree does not carry), shonen-semantics (whether a box's claim is true).
- **r8 classification** (schematic vs real vault ref) is declared could-not-evaluate; at this revision
  r8 reported zero literal occurrences, so there was nothing to classify. "No credential material" is a
  literal-text result only.
- **r7** grades phantom rows only; under-coverage (file without row) is a note, not a finding
  (1827/1858 at this revision).
- **Snapshot mode** grades a `git archive` tree with no `.git` history, so r9's authorship sub-check is
  unavailable by construction. r10 is a presence check, not a statement that the round review is
  adequate.
- The gate does not evaluate SOURCES.md contract rules; the structural census above is separate and
  provisional.
- No committed expected verdict exists for this revision (`# expect … ABSENT`); the exit-3 drift path was
  not exercised.
- This audit makes no claim about semantic corpus conformance, verifier independence, or SHONEN truth.
  No score is produced.

## Reproduction

```
git -C /home/vgpnk/Projects/shokunin/lore-shokunin rev-parse HEAD
git -C /home/vgpnk/Projects/shokunin/lore-shokunin status --porcelain
git -C /home/vgpnk/Projects/shokunin/lore-shokunin ls-tree -r --name-only HEAD -- corpus/lessons
cd /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/fleet-aggregate \
  && node .ufo/waves/round-9/corpus-gate.mjs \
       --snapshot /home/vgpnk/Projects/shokunin/lore-shokunin \
       6e804e2e5bff0edcc260c995a058dd724b0c98c0 --round 103
# selector checks: same command with no --round (default 9) and with --round 12
# census (from the lane root, provisional): see the command block in the census section
```
