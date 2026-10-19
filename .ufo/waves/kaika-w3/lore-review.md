# kaika W3: non-author verification of lore round 103

Reviewer: W3ReviewLore (non-author; dispatched by orchestrator). Verdict is a recommendation.
Lane HEAD `74384c94b` (round work `33173138d2ece2ea1060ac6fbb1200a3c76f6ebd`, ledgers `74384c94`); base `6cec83aed`; branch `kaika/round`.
Scratch clone `/tmp/kaika-verify/lore/clone` (detached checkouts of both revs; deleted at end). Lane worktree was read-only; nothing committed, staged or switched.

## 0. Recommendation

- **Do not close round 103 as landed on the current head.** Hold for a short correction commit, then re-run the census.
- Counts for C1, C2 and C3 re-run exactly as reported (verified).
- The two admissions (CM-c, CM-e) and the CM-a rejection agree with the Q06 bar. CM-c is a clean admit. CM-e rests on qE5; its qE2 grade is weak (§5).
- Required corrections, in order:
  1. Fleet census `validate` exits 1 (E04, E09, W01). The report's "census is clean" (report line 22) and the SCORECARD C3 wording "census clean" are not true under the tool. Fix E09 (`recheck: annual` is outside contract v1's grammar), dispose of E04 (S017 repeats S012's URL), and record W01 as a tool-vs-contract disagreement.
  2. S023 row (SOURCES.md:31) and CM-c line 1 misstate the ISO lifecycle ("confirmed 2024-12-05").
  3. Five SCORECARD pointers in lesson M07/M08 (and Q07/Q08) sit one line early at head.
  4. Restate expansion and quality as `unchanged` (contract v1 rule 4 counts uncovered ground; no existing entry was re-verified).
  5. Make the CM-e recheck reproducible: its stated `0` does not come out of the stated pipeline (90 lines at head).

## 1. Provenance: PASS

Command: `git -C <lane> log --format='%h %an <%ae> | %cn <%ce> | %s' 6cec83aed..74384c94b`
```
74384c9 lore-shokunin <lore@shokunin.local> | lore-shokunin <lore@shokunin.local> | round-103: SCORECARD/LOG ledgers, capability row, receipt count correction
3317313 lore-shokunin <lore@shokunin.local> | lore-shokunin <lore@shokunin.local> | round-103: QUALITY bar from mined mistakes, SOURCES registry, coverage map; admit CM-c/CM-e, reject CM-a on sealed evidence
```
Both round commits carry the lane identity as author and committer. The report's `33173138` is an 8-character prefix of `33173138d2ece2ea1060ac6fbb1200a3c76f6ebd`; `git rev-parse` resolves the full hash and `git log` names it `3317313` at its default 7-character width. Citations are sound.

## 2. Append-only: PASS (scoped files); one out-of-scope rewrite

Command: `git -C <lane> diff --numstat 6cec83aed..74384c94b -- LOG.md corpus/lessons corpus/QUALITY.md corpus/SOURCES.md`
```
21	0	LOG.md
28	0	corpus/QUALITY.md
74	0	corpus/SOURCES.md          (new file at base)
103	0	corpus/lessons/round-103.md (new file at base)
```
No prior line was deleted or modified in LOG.md, QUALITY.md, or the lesson. `corpus/SOURCES.md` is new, so no status/recheck/used-by cell changed in place.

Whole-diff deletions (`git diff ... | grep -nE '^-[^-]'`): four lines, all in `SHONEN.md` (diff lines 1633, 1636, 1639, 1642). Each removes a "Lane assertion, not external promotion verification" disclaimer and rewrites the Evidence line. SHONEN.md is outside the append-only set, and the report says it was regenerated from the canonical seed. I could not locate that seed, so this is unverified. Recommend the orchestrator check the seed.

## 3. Claims: re-run counts

Commands: `bash .ufo/waves/round-103/measure.sh 74384c94b` and `… 6cec83aed` (run with the lane as cwd, read-only). Working-tree mode in the scratch clone at head gave identical output.

| claim | metric | base 6cec83aed | head 74384c94b | report says | verdict |
|---|---|---|---|---|---|
| C1 | CM rows, corpus/README.md | 0 | 19 | 0→19 | verified (counts) |
| C1 | CM-a..g governed rows | 0 | 2 | 0→2 | verified (counts) |
| C1 | knowledge entries with coverage-row | 0 | 2 | 0→2 | verified |
| C1 | Frontier headings / rows | 0 / 0 | 1 / 5 | 0→1 / 0→5 | verified |
| C1 | PROVINCE Core/Frontier/Adjacent | 0 | 3 | 0→3 | verified |
| C2 | Q rows / citing lesson | 0 / 0 | 10 / 10 | 0→10 | verified |
| C2 | lesson M rows / captured | 0 / 0 | 10 / 10 | 0→10 | verified |
| C2 | lesson `## Gate` admitted+rejected headers | 0 | 2 | 2 admit, 1 reject | verified (headers; decisions in §5) |
| C3 | SOURCES rows | 0 | 31 | 0→31 | verified |
| C3 | admitted entries fully traced | 0/0 | 2/2 | 0/0→2/2 | verified (near-tautological: the lane wrote both sides; see L4) |
| C3 | "census clean" | file absent | validate exit 1 | "census clean" | **not-verified** (§4) |

The coverage-verify cells replayed at head (19/19, from the lane root):
```
CM-01 exit=0  CM-02 exit=1  CM-03 exit=1  CM-04 exit=1  CM-05 exit=0  CM-06 exit=1
CM-07 exit=0  CM-08 exit=0  CM-09 exit=0  CM-10 exit=0  CM-11 exit=0  CM-12 exit=0
CM-a exit=1  CM-b exit=0  CM-c exit=0  CM-d exit=0  CM-e exit=0  CM-f exit=1  CM-g exit=1
```
All match the documented exits. CM-b's cell is a copy of CM-09's (`grep -c 'R10' corpus/knowledge/r101-r10-register-first-entry.md`), a weak test for a row marked `partial`.

Checker harm battery: `git diff --stat 6cec83aed..74384c94b` shows no change under `corpus/fixtures/`, `corpus/tools/`, or any `.py`, so the battery is unchanged by construction. I did not rerun the base battery.

## 4. SOURCES: FAIL

Command (fleet tool, snapshot `sha256 4d828033…f0950` of `fleet-census/scripts/sources-census.sh`; the file is untracked and was being edited during my review, so I used the snapshot): `TZ=UTC bash sources-census.sh validate <clone>`
```
clone	E04	S017 duplicate url arxiv.org/html/2603.05890
clone	E09	S023 recheck=annual
clone	W01	S027 tierC mined used-by=corpus/knowledge/r103-canon-status-and-supersession.md
exit=1
```
Under the host TZ (America/Sao_Paulo) the same command also prints `E08 opened=2026-10-19` for all 31 rows. That is a tool false positive: `iso_epoch()` uses gawk `mktime(…,1)` (UTC midnight = 1792368000), while the row check uses local `date -d` (1792378800). I confirmed both numbers.

Interpretation:
- E09 is a real contract violation. Contract v1 allows an ISO date or `NNd` / `on-release`; `annual` is not in the grammar.
- E04 is tool-enforced. S017 is a different section of the same paper as S012 and has no `supersedes` tag. The lane must dispose of it (for example, a scope note in S012 instead of a second row, or a tool exemption with a recorded decision).
- W01 is stricter than contract v1. The contract says tier C is "lead only — never sole support", not "never mined". CM-e cites S027 alongside tier-A rows, so the lane is contract-compliant; the tool is not. Record as a tool disagreement.
- The header comment in `sources-census.sh` says warnings "do not affect clean lanes", but `validate` sets `findings=1` on any W code. The tool, not the lane, is wrong here.

Contract block (the rule-level census in SOURCES-CONTRACT-v1 §Census), run at head:
```
rows: 31 · malformed (must 0): 0 · tier A=23 B=3 C=5 · status mined=16 queued=12 rejected=3
dup ids: (empty) · enum/inflation: (empty) · mined used-by missing: (empty)
```
These are true. The broad "census is clean" is not (report line 22; SCORECARD round-103 C3 row).

Re-opened rows (≥3 required; ≥1 new tier A and ≥1 rejected):

| row | tier | re-open source | result |
|---|---|---|---|
| S020 OWL-Time (new, tier A) | A | `https://www.w3.org/TR/owl-time/` (CRD 2022-11-15 abstract) | quote verbatim: "Time positions and durations may be expressed using either the conventional (Gregorian) calendar and clock" |
| S021 EDTF | A | Wayback `web/20241231122647` | quote verbatim, "Qualification of a date (complete)", Level 1 |
| S023 ISO 8601-2 | A | Wayback `web/20241230054021` | abstract quote verbatim. **Lifecycle misstated**: the row and CM-c line 1 say "confirmed 2024-12-05". The capture shows `90.93 2024-06-05 International Standard confirmed` and `90.92 2024-12-05 International Standard to be revised`, with `ISO/AWI 8601-2` as replacement under development. The string "confirmed 2024-12-05" does not appear. |
| S016 LongStoryEval (rejected) | C | `aclanthology.org/2025.acl-long.799/` | gate quote verbatim (abstract); rejection reason consistent with the abstract (reader-rated aspects) |
| S025 Wikidata Help:Ranking | B | `wikidata.org/wiki/Help:Ranking` | quotes verbatim ("Marking erroneous statements…", "not a way of asserting your view…") |
| S024 Wikibase Primer | A | `mediawiki.org/wiki/Wikibase/DataModel/Primer` | quotes verbatim (§Statements; §Ranks, oldid 8399774) |
| S022 TEI att.datable | A | `tei-c.org/…/ref-att.datable.html` | attribute row verbatim; revision 113e933e2 matches |
| S026 PROV-DM | A | `curl https://www.w3.org/TR/prov-dm/` (HTML, grep) | revision, invalidation and alternate quotes present verbatim; section numbers not checked |
| S027 Holocron | C | `en.wikipedia.org/wiki/Star_Wars_expanded_to_other_media` | "The Holocron was divided into five levels of canon (in order of precedence)" verbatim |

Nine rows re-opened; every gate quote I checked exists at its source except S023's lifecycle. Lesson gate anchors resolve.

## 5. Discernment spot-check (LEARNING.md)

| sample | lane decision | my verdict | reason |
|---|---|---|---|
| CM-c `r103-in-world-dating-and-uncertain-time.md` | admit (qC2 DIFFERENT) | **agree** | Baseline answer, `R103Adjudicator.md` row qC2: "no tick arithmetic or dependency". Proposal adds a `depends_on` edge (`R103SealedC-proposal.md`). That is a checker-visible record change. Caveat: the difference follows the entry's own instruction; no seeded case where the baseline decides wrongly. Q06 as written is satisfied. |
| CM-e `r103-canon-status-and-supersession.md` | admit (qE2 DIFFERENT, qE5 DIFFERENT) | **agree on admit; disagree on qE2 grade** | qE5 (baseline defers to L0, proposal creates a convention record) is a real routing difference. qE2 is weak: the baseline already records the amendment as a docket-2 event with a `depends_on` to docket-1 (`R103SealedE-baseline.md`, qE2). The proposal's "separate sourced statement or `supersedes`-type relation" is explicitness, which QUALITY.md:17 says is not a delta. Admit stands on qE5; record qE2 as a lesson. |
| CM-a aliases (rejected, Q06) | reject (qA1–qA5 SAME) | **agree** | Baseline and proposal both add one sourced alternate-name claim, add no alias field, mint no entity, leave identity unresolved and leave the checker unchanged (`R103SealedA-baseline.md`, `…-proposal.md`). No record or routing decision differs. The preserved file's header still names SXA1–SXA4 (L2). |
| S016 (rejected row) | reject | **agree** | The abstract rates reader-facing aspects; it does not establish contradiction detection. |
| S017 (rejected row) | reject | not re-opened | Reason is plausible; not checked against §2.3. |

Discernment verdict (recommended): improved (bounded), conditional on the lane recording the qE2 disagreement in its lesson. The sample agrees on both decisions, but a grade-level disagreement is not yet learned.

## 6. New knowledge entries

- Header trio: CM-c lines 1–3 (`source:`, `verified-at:`, `recheck:`) and CM-e lines 1–3 present; `coverage-row:` on line 4 of both. PASS.
- CM-c recheck: `grep -rniE 'calendar|notBefore|notAfter|EDTF|era' corpus/fixtures/check_bible.py` runs; 4 hits, all `enumerate` substrings (lines 67, 156, 212, 397), as the entry predicts. PASS.
- Path-existence (CM-c/CM-e cited lane paths): two misses, `corpus/knowledge/culture-material/…` (CM-c) and `corpus/knowledge/cross-cluster-contradictions.md` (CM-e). The first is `kotodama-shokunin/`-prefixed in the entry's own Adjacent section; the second is stated as "not yet created". Both acceptable.
- CM-e recheck: the header command `grep -rniE 'retcon|canon[ -](tier|status)|supersed' corpus/knowledge corpus/fixtures corpus/tools` returns **98** lines; the body's filtered sweep (line 18, "returns 0 in-world governance hits") returns **90** lines with its own `grep -vE 'editorial|addendum|ledger convention|debt ledger'` filter. The `0` is a manual judgment, not a pass/fail. Make the recheck reproducible.
- Claims vs sources: S020, S021, S022, S023 (abstract), S024, S025, S026, S027 quotes verified. S023's lifecycle is misstated (§4). CM-c's "ISO 8601-2 explicitly excludes non-Gregorian calendars" holds.

## 7. Credentials: PASS

`git diff 6cec83aed..74384c94b | grep -nE 'op://[A-Za-z0-9]|BEGIN [A-Z ]*PRIVATE KEY|ghp_[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}|xox[baprs]-[A-Za-z0-9]'` printed nothing (exit 1).

## 8. Report (`fleet-ledger/.ufo/reports/round-103/lore.md`)

- Required sections present in order: Work performed, Landed changes, Before→after, SHONEN, Sources & frontier, Mistakes, Trend verdicts, L0 questions, Integrator notes. PASS.
- No `[x]`; all four SHONEN boxes `[~]`, each with a pointer; the pointers I sampled resolve (for example `.ufo/waves/round-93/deepseek/F24.md`, `.ufo/waves/round-103/seats/R103Connector.md`).
- Cites round commit `33173138` (full hash resolves) and `74384c94`. PASS.
- Defects in the report: line 22 "its census is clean" (false under validate); the expansion verdict `improved` rests on "partial" ground (§9); the SHONEN, Sources and Mistakes sections repeat the S023 and pointer issues.

## 9. Per-axis and trend verdicts (recommended)

| axis | report | recommended | evidence |
|---|---|---|---|
| depth | improved (bounded), contested | improved (bounded) | Two entries with concrete decision tables (CM-c lines 21–31; CM-e lines 44–52). Nine SOURCES rows re-opened with located quotes. The capability row is registry bookkeeping (the critic's point stands) and should not enter until §4 passes. |
| coverage | improved (bounded) | improved (bounded) | Counts verified (§3). CM-c/CM-e were `partial` before the round per the lane's own map, not `uncovered`. CM-a stays uncovered. |
| calibration | improved (bounded) | unchanged, not confirmed improved | The Q-bar and the sealed gate are real. But the round's own statements conflict with observed output: "census clean" (§4); S023 lifecycle misstatement (§4); five stale SCORECARD pointers (M2). Re-evaluate after the corrections. |
| operability | unchanged | unchanged (not harmed) | No tool, fixture or checker change; 19/19 coverage cells replay. |
| freshness | unchanged | unchanged (not harmed); harmed if M2 pointers are not corrected | Dead seat-scratch pointers: K16 count 24 at base and 24 at head (`git grep` over the README's pipeline). The five pointer drifts are introduced in-round. |
| adjacency | unchanged | unchanged (not harmed) | PROVINCE Adjacent names chousa, kotodama and game-dev-2d; no absorption. |

Trend verdicts:

| trend | report | recommended | reason |
|---|---|---|---|
| expansion | improved (bounded) | **unchanged** | Contract v1 rule 4 counts admitted entries on *uncovered* ground. CM-c and CM-e were `partial` before the round. LEARNING.md's "improved" bar is also "uncovered ground". If the orchestrator reads "partial" as "not held", this is `improved (bounded)`; the contract wording does not support that. |
| quality | improved (bounded) | **unchanged** | No pre-existing entry was re-verified or superseded (none existed to re-verify). The 12 rows are new openings. The S023 misstatement is a false statement left in the round's own entry header. |
| discernment | improved (bounded) | improved (bounded), conditional | Spot-check agrees on both decisions (§5). Record the qE2 disagreement. |

## 10. Defects by severity

**High**
- H1. Fleet census `validate` exits 1 (E04, E09, W01); the report's "census is clean" (report line 22) and the SCORECARD C3 "census clean" are not true under it. Check 4 fails. Fix: E09 `annual` → `365d` or `on-release`; E04 disposition for S017; W01 recorded as tool-vs-contract.

**Medium**
- M1. S023 lifecycle misstatement: SOURCES.md:31 and CM-c line 1 say "confirmed 2024-12-05". Capture (`web/20241230054021`) shows 2024-12-05 = "International Standard to be revised", and the standard is to be replaced by ISO/AWI 8601-2. The row's own "live 2026 status unverified" is honest; the misquote is not.
- M2. Stale lesson pointers at head (the capability row insert at SCORECARD.md:80 shifted all later lines by +1 in `74384c9`):
  - SCORECARD:356 → text now at 357 ("r89 calibration is **harmed**…"); cited by M07 (lesson line 17) and Q07.
  - SCORECARD:383 → 384 ("32 tool-terminal `completed` labels…"); cited by M08 (line 18).
  - SCORECARD:600 → 601 and :667 → 668 ("ROSTER ERRATUM…"); cited by M08.
  - SCORECARD:634 → 635 ("First closing-pair round…"); `R103Reviewer-pre.md:66` already records this as SHIFTED; the lesson was not corrected.
  The lesson says every pointer was "re-verified in this worktree". At head that is not true for these five. LOG.md pointers (54, 205, 232, 633, 840, 1398, 1530, 3603) all verified verbatim.
- M3. Expansion and quality overstated (§9).
- M4. CM-e recheck not reproducible: 98 raw lines; 90 after the body's filter; the body's `0` is judgment (§6).
- M5. CM-e qE2 grade rests on explicitness (§5); Q06 excludes explicitness.
- M6. SHONEN.md: four disclaimer lines deleted and Evidence lines rewritten (§2); seed not located; unverified.

**Low**
- L1. Fleet census tool (out of lane scope; W4FixCensus was editing it during my review): (a) E08 false positive under non-UTC TZ (§4); (b) header says warnings don't affect clean lanes, code says they do; (c) file changed between my reads (lines 12 and 26), so I used a snapshot.
- L2. `rejected/r103-aliases-and-name-variants.md` lines 1–2 keep SXA1–SXA4; the lesson renumbered these to S028–S031. The preserved rejection cannot be found by its registry IDs.
- L3. CM-b verify cell duplicates CM-09's; weak test for a `partial` row.
- L4. C1/C2/C3 "before" values are self-referential: base has no map, QUALITY.md or SOURCES.md, so the 0→N moves measure existence, not effect (§3). The sealed gate is the non-tautological evidence.

No defect found in: provenance, append-only for scoped files, credentials, the coverage-verify exits, the sealed-receipt sealing checks, the CM-c recheck command, or the LOG.md pointers.

## 11. Admit / reject recommendation

| item | recommendation | condition |
|---|---|---|
| C1 coverage (counts) | verified; admit | restate expansion as unchanged |
| C2 calibration (counts, Q-bar, gate) | verified; admit the bar and the gate | record qE2 disagreement; fix S023; fix pointers |
| C3 depth capability (source-traced admission) | **hold** | H1 must pass (`validate` exit 0, or a recorded tool disagreement) and "census clean" wording corrected before the capability row enters |
| CM-c admission | **admit** | correct S023 line 1 |
| CM-e admission | **admit** | record qE2 disagreement; make recheck reproducible |
| CM-a rejection | **reject (agree)** | none |
| Round closure | **return for correction**, not reject | five corrections in §0 |

## Commands used (all read-only except scratch)

- `git -C <lane> log --format=… 6cec83aed..74384c94b`; `git -C <lane> diff --numstat 6cec83aed..74384c94b -- LOG.md corpus/lessons corpus/QUALITY.md corpus/SOURCES.md`; `git -C <lane> diff 6cec83aed..74384c94b | grep -nE '^-[^-]'`; `git -C <lane> rev-parse 33173138d2ece2ea1060ac6fbb1200a3c76f6ebd`.
- `git -C <lane> show 6cec83aed:<path>` for base files; `git clone --no-hardlinks <lane> <scratch>` plus detached checkouts of both revs.
- `bash .ufo/waves/round-103/measure.sh {74384c94b,6cec83aed}` (cwd = lane); working-tree mode in the clone.
- Contract-block census commands (SOURCES-CONTRACT-v1 §Census) at head.
- `TZ=UTC bash sources-census.sh validate <clone>`; `bash sources-census.sh census <clone>`; gawk `mktime` comparison for E08.
- Coverage verify cells replayed in the clone (`corpus/README.md:49-73`).
- `git grep` K16 count (dead seat-scratch pointers) at base and head: 24 and 24.
- Web fetches: W3C OWL-Time; PROV-DM (HTML via curl); Wayback captures for LoC EDTF and ISO 8601-2; ACL Anthology; Wikidata Help:Ranking; Wikibase Primer; TEI att.datable; Wikipedia Star Wars article.
- Credential grep: no output.

Scratch `/tmp/kaika-verify/lore/` and `/tmp/kaika-census-head.sh` deleted at the end of the review.
