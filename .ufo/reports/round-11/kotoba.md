# kotoba — round 11 report

Lane: `kotoba` (`~/projects/shokunin/kotoba-shokunin`). Axis move: **consistency**
(this lane declares it a `calibration` sub-axis; `AXES.md` has no `consistency`
row — the mismatch is the protocol lane's, filed in round 10). Round 11 also
answers round 10's stated falsifier ("make the depth evidence non-author
verifiable") with a committed non-author cold-run record.

Scope compliance: every write this round is inside `kotoba-shokunin` (own lane
repo) or this report in `VeigaPunk/shokunin`. Domain source trees
(`ufo-fsd-alpha`, `bounties`, `webzites`, `llm-wiki`) were read-only surfaces for
this round's census/sentinel lanes (`git cat-file`, `git log`, `test -e` only);
nothing upstream-bound was touched, and no upstream push is requested.

## Trigger — three zeros, two counting commands that could not count

Round 10's consistency row claimed three zeros (non-hash commit pointers 0,
unindexed corpus files 0, unresolved report pointers 0) with one hand-run command
each. Two of the three commands could not express the class they named:

1. `grep` with token class `round-[0-9]` — exactly one digit, so it can never
   match `round-10`. On the defect-bearing blob it prints **0 with the defect
   present** (`git show HEAD:corpus/README.md | grep -cE "commit \`round-[0-9]\`"` → 0;
   `…[0-9]+\`` → 1).
2. `comm -13` over a README-token sweep whose regex `[A-Za-z0-9._-]+` cannot
   tokenize the brace row `lessons/round-{1,4,5}-aggregator-audit.md` — it lists
   three *indexed* files as unindexed. Copied from the markdown table its escaped
   pipes make the left side match nothing: it prints all 33 tracked files.
3. A `grep '\.\./\.ufo/reports/round-'` count also matches `../../.ufo/…`: it
   printed 9 before **and** 9 after the repair.

A claim whose counting command cannot express its scope is calibration debt even
when the number is right.

## Move

Landed `verifiers/verify_corpus_integrity.py` (9 checks, exit 0 agree / 1 drift
naming the firing ids / 2 environment unreadable / 3 no baseline, `--json`,
`--self-test`, `--no-baseline`, `--baseline`, `--repo`) and
`verifiers/corpus-baseline.json`, then fixed every defect the new check and the L2
census found:

| Defect | Sites | Before → after |
|---|---|---|
| dead report pointers `../.ufo/reports/round-N/kotoba.md` | 9 rows in `corpus/README.md` | dead → resolving |
| dead bare report pointer `.ufo/reports/round-3/kotoba.md` | `corpus/lessons/round-3.md:5` | dead → resolving |
| non-hash commit citation `commit \`round-10\`` | `corpus/README.md:38` | → `abef8aa` (real commit) |
| md5 printed with commit notation `@ \`143fe473…\`` | `corpus/README.md:35`, `corpus/knowledge/claim-scope-audit-round9.md:15` | → `@ md5 \`143fe473…\` (commit \`3b029b8\`)` |

Check ids: `corpus.index.{tracked_files,unindexed,stale_patterns,missing_paths}`,
`corpus.pointers.{report_total,report_dead,commit_total,commit_unresolvable,commit_nonhash}`.
Scope: tracked `corpus/*.md`; six false-positive shapes are excluded by design and
pinned in `--self-test`.

## Measured before → after

Before-state is a real clone (`git clone --no-hardlinks . /tmp/before-clone-r11`,
HEAD `d49dfa5`), never `git show` text — an uncommitted repair reads as "agree" to
any check that reads the working tree:

```
$ python3 verifiers/verify_corpus_integrity.py --repo /tmp/before-clone-r11 --no-baseline ; echo exit=$?
corpus.index    tracked=33 unindexed=0 stale=0 missing=0  (32 FILE-column patterns over 33 md files)
corpus.pointers report_dead=10/19 commit_total=18 unresolvable=0 nonhash=1
                (shapes [relative=9, absolute=8, tilde=1, bare=1], quoted-excluded=1, pointer-excluded=1)
7/9 checks pass; DRIFT: corpus.pointers.report_dead, corpus.pointers.commit_nonhash
exit=1

$ python3 verifiers/verify_corpus_integrity.py ; echo exit=$?
9/9 checks pass
exit=0
```

Report pointers 10 dead → 0; non-hash commit tokens 1 → 0 (`round-6-aggregator-audit.md:45`'s
`commit \`round-N\`` stays as a *quoted* meta-finding, counted in context);
unresolvable hex pointers 0; unindexed corpus files 0 (raw 1 = the index's own
`README.md`); stale index rows 0; missing FILE-column paths 0.

Method notes that cost time and are now recorded:

- A synthetic before-tree (`git archive | tar -x` + `git init && git add && git
  commit`) reports `commit_unresolvable=18` — history that does not exist. Clones
  only.
- `/tmp/round11` was wiped mid-round by disk-quota pressure; the census lane
  recreated its instrument and re-pinned every number. Scratch state is not
  evidence — every number above is re-runnable from the repo + a clone.

## Verification of the verifier itself

- `--self-test` → `0 failure(s) over 80 assertions`, exit 0 (brace expansion,
  brace+glob coverage, four pointer shapes, exclusion shapes, quoted citations,
  hash classification). One earlier revision was **red** (`FAIL
  pointer/no-match/glued`) while the live run was green in the same revision — the
  episode is why the self-test exists.
- Exit codes probed on real inputs: perturbed baseline (`commit_total` expect →
  18) → exit 1 naming exactly that id; `--repo /tmp/notgit` → exit 2; baseline
  removed → exit 3.
- Red-before on the clone → exit 1 with exactly the two ids that were repaired.
- Non-author cold run: **cold-run status filled below**.

## Non-author cold run (round 10's falsifier, restated)

Requirement: a lane that neither authored the script nor re-ran the author's
script records path + command + exit code + independent spot-checks.

Result (full record: `corpus/knowledge/cold-run-round11.md`; runner `ColdRunRecord`,
which authored neither the script nor the baseline):

- sha256 gate on the shipped script (`631569277d…`, re-gated after L1's
  comment-only edit at `2f07179c…`), `--json` and plain runs captured verbatim
  with exit codes from `/tmp` (outside the repo), and a coherence guard
  (`md5sum corpus/README.md` + `git status --porcelain` hashed before/after the
  capture window — `GUARD: coherent`).
- Three independent spot-checks in the runner's own Python: the FILE-column
  pattern and tracked-file counts (`33`/`36`), every checked report pointer
  resolved with `test -e` (`dead=1` at the mid-landing instant, the README row
  advertising a report not yet written), every `commit` citation through
  `git cat-file -e <hex>^{commit}` (`21 checked, 0 nonhash, 0 unresolvable`).
- `Discrepancies: none found`; the mid-landing DRIFTs it flagged
  (`stale_patterns=2`, `report_dead=1`, `report_total expected=None`) are real
  tree state at that instant and are all cleared at the landing commit.

## Cross-domain (audited, routed, not absorbed)

- Sibling trigger gap unchanged: 0/5 sibling `*-shokunin/SKILL.md` descriptions
  carry quoted triggers or an arbitration clause; bodies grew today (kagi
  322 → 497 lines) so the round-8 drop-in rewrites
  (`corpus/knowledge/sibling-description-rewrites-round8.md`) remain producer-ready
  and unapplied. Owner: whoever owns the mint template (unassigned; filed in
  round 7).
- Fleet commit-identity class: `kumitate 7a4c9a0` and `kagi ea77bf0` now resolve
  **in their own repos** and are authored `shokunin <shokunin@local>`; the
  non-lane identity defect is real and cross-verifiable. Reported, not repaired.
- Sibling mechanism overlap (connector lane): kumitate ships
  `scripts/cite-check.mjs` — a schema'd citation/pin resolver with its own
  self-test and `git commit` pin resolution. Kotoba's checker is repo-local and
  narrower (corpus index + pointer classes); the overlap is a fleet-level
  question (per-corpus review is `CORPUS.md`-assigned to the aggregator). No
  sibling `verifiers/` directory exists. Routed, not merged.
- Stale always-on text still present outside this province: `~/.agents/AGENTS.md`
  procedures at `:55/:57`, dated TAC text at `:48/:51`; `~/.config/opencode/agents/ufo.md:7`
  `cascade_note` 30 days past its own expiry.
- No MCP/plugin surface exists on this host; the surface class is absent, not
  unsurveyed.

## Honest gaps and the standing ceiling

- The checked pointer population is 19, of which 18 are host-absolute: correct
  here, brittle across hosts.
- `corpus.index.tracked_files` and `corpus.pointers.{report_total,commit_total}`
  are change detectors; corpus growth needs a deliberate baseline re-record.
- Report pointers and commit citations in `LOG.md`/`SCORECARD.md`/`SKILL.md` are
  **not** checked (the verifier scans `corpus/*.md`).
- `SKILL.md`'s 39 checklist boxes (13/9/9/8 by section) remain lane-attested: this
  round machine-checked *counting*, not *execution*. No verifier in this repo runs
  a box.

## L2 lanes (13 dispatched, two batched `task` calls; MISSION floor 8)

Batch 1 (round start): `ScoutIndexBefore` (before-state instrument; reproduced the
`comm` defect), `ScoutPointerCensus` (four-form pointer census, exclusion list,
three iterations after peer falsification), `ExecVerifierDraft` (script draft +
fixture red-before), `ExecArtifactDrafts` (prose drafts + landing-state audits),
`PlanRound12`, `ConnectorSiblingOverlap`, `CriticPreFalsify` (band-9 strict
ruling: a cold run of a *broken* instrument would launder error), `SentinelCrossDomain`,
`ReviewTraceability` (27 checks mapped to 38 claims, 14 uncovered).

Batch 2 (after landing): `ColdRunRecord` (non-author cold run),
`FaultInjection`, `CheckFalsifiability`, `CriticPostFalsify`.

## Falsifiable next iteration (round 12)

`consistency` 9 → 10 (band 10 = repeated non-author verification in the opposite
direction): a lane that did not author the checker re-derives the corpus verdicts
from the files alone (its own code, its own before → after on a clone) and
publishes the result in-repo, adjudicating any disagreement rather than explaining
it away. Falsified by: no in-repo non-author derivation, or a derivation whose
verdicts disagree with `python3 verifiers/verify_corpus_integrity.py` on the live
tree. Second candidate: turn one of the four `SKILL.md` checklists into a check
with a fixture fault (falsifier: the fixture must exit 1 while the live tree exits 0).

## Artifacts

- `verifiers/verify_corpus_integrity.py`, `verifiers/corpus-baseline.json`
- `corpus/knowledge/corpus-integrity-round11.md`, `corpus/lessons/round-11.md`
- `corpus/knowledge/cold-run-round11.md` (non-author)
- `corpus/README.md` (2 new index rows), `SKILL.md` (citation rule made
  executable; Sources rows), `SCORECARD.md` (consistency row + planned), `LOG.md`
- Commit: `4dd7753` (landed by the round-12 respawn; see the landing note in this
  report) in `kotoba-shokunin`; this report committed + pushed in the main repo.

## Landing note (round-12 respawn)

The round-11 mission ended with its working tree complete but uncommitted. The
round-12 process resolved it as `4dd7753` with two declared presentation edits
(reported-absent tokens rewritten as prose; one bare pointer re-presented as the
host-absolute path it names), so the landed tree runs green: `python3
verifiers/verify_corpus_integrity.py` → `9/9 checks pass`, exit 0; `--self-test` →
`0 failure(s) over 80 assertions`; exit codes 2/3 re-probed. `verifiers/corpus-baseline.json`
was re-recorded at landing (all nine ids, including `corpus.pointers.report_total`,
which the draft omitted) and its `measured_against` names the parent commit plus
the dirty list that *is* this commit's tree — see the file's `note`.

## SHONEN

- `[~]` SKILL.md decision tables / error patterns / checklists / cited sources —
  carried from round 10; round 11 added the executable-verifier source rows
  (`SKILL.md` § Sources) and made the citation rule checkable.
- `[x]` end-to-end domain task in LOG.md — round-11 verifier + its non-author cold
  run (runner `ColdRunRecord`); the `[x]` is the reviewer's, not this lane's;
  promoted in round 11.
- `[~]` instructions executable without oral context — round-10/11 verifiers are
  the evidence; the 39 `SKILL.md` checklist boxes remain lane-attested.
- `[~]` no cross-domain bleed — the four routed cross-domain defects above were
  re-verified and reported, not repaired; `PROVINCE.md` unchanged.

All four lines are transcribed from `kotoba-shokunin/SHONEN.md` at the landing
commit; the round-11 report was filed without this heading, which the report
contract requires, so it is supplied here at filing time.