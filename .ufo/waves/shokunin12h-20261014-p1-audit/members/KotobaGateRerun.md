# KotobaGateRerun

Seat: safe-gate rerun only. Read-only against `/home/vgpnk/Projects/shokunin/kotoba-shokunin`. No lane file edited. No commit. Live `python3 verifiers/verify_harness_claims.py` was not run (it reads `~/.omp` session JSONL). Full fault-injection matrix (no `--self-test`) was not run.

Compared to the lane lesson, not to the lesson's own arithmetic. Lesson: `corpus/lessons/round-19-recensus.md`. SCORECARD move-log row 19 and `LOG.md` §19 do not restate scalars; they defer to that lesson.

## Run context

- Captures hashed at `2026-10-14T21:19:14-03:00` (`date -Iseconds` immediately after the six commands returned).
- cwd: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`
- `git rev-parse HEAD`: `b0c7cb2e248bccf692cf10e4d3c394e09944e83d`
- `git log -1 --format=%s`: `round-19: OMP-era freshness re-census (measured gates; records + scoped repair)`
- Commit time: `2026-10-14 21:15:36 -0300`
- That HEAD is the wave's named lane-identity commit.
- Parent: `02302c521b933c55fc4be79193e61537e3380751`. `git show` of that parent’s `SKILL.md` is 601 lines. This commit does not touch `SKILL.md` (`git show --name-status` lists only `LOG.md`, `SCORECARD.md`, `corpus/lessons/round-19-recensus.md`, `verifiers/verify_harness_claims.py`).
- Tracked gate inputs were clean: `git status --porcelain -- LOG.md SCORECARD.md SKILL.md corpus verifiers` printed nothing.
- Worktree noise not in the committed clone: `?? plans/wwkd-round-19-recensus.md`. Integrity reported `tracked=48`, not 49, and named the committed lesson as the unindexed file. The untracked plan is not the red-gate cause.
- Interpreter: `/usr/bin/python3`, `Python 3.14.7`. Lesson does not pin an interpreter. Not a claimed-number mismatch.
- stderr for all six commands: 0 bytes.
- Fault self-test worlds: none left (`ls -d /tmp/round12-faults.*` found none).

## Claim-by-claim

| Claim (lane record) | Observed | Label |
|---|---|---|
| Lesson L18: `python3 verifiers/verify_corpus_integrity.py` → exit 0, `9/9 checks pass` | exit 1; last line `7/9 checks pass; DRIFT: corpus.index.tracked_files, corpus.index.unindexed` | disagree |
| Lesson L19: `python3 verifiers/verify_surfaces.py` → exit 0 (7/7 checks) | exit 0; seven `PASS` lines; no `7/7` summary line is printed | agree |
| Lesson L20: `python3 verifiers/verify_corpus_independent.py` → exit 0 | exit 1; last line `exit 1` | disagree |
| Lesson L21: `bash verifiers/fault_injection_corpus.sh --self-test` → OK | exit 1; last line `self-test: BROKEN` | disagree |
| Lesson L22–23: `python3 verifiers/verify_harness_claims.py --self-test` → 0 failures over 10 assertions; live run excluded | exit 0; last line `self-test: 0 failure(s) over 10 assertions`; live run not executed | agree |
| Lesson L27–29: `verify_skill_checklist.py` → exit 1, sole named FAIL `trigger.line_budget: evaluated 601 — 601 lines exceed budget 600`, pre-existing | exit 1; the 601/600 FAIL is present; last line is a second FAIL the lesson does not record; parent `SKILL.md` is also 601 lines | partial |
| Lesson L6–14: one file, two lines; `oc.permission.skill_lines` and `oc.permission.skill_allow` move `at_least` → `equal`; baseline JSON `"mode"` stays unread | `git show` of `verifiers/verify_harness_claims.py` is exactly those two tuples. `evaluate()` takes `mode` from `CHECKS` (`verify_harness_claims.py:557`) and `expect` from the baseline. `verifiers/baseline.json` still has `"mode": "at_least"` and `"expect": 0` for both ids | agree (source). The safe self-test does not instantiate `CHECKS` |
| SCORECARD row 19 / `LOG.md` §19: verdicts recorded per gate, see the lesson | The row and log entry add no scalar. The lesson they defer to does not match this rerun on three green claims | disagree with the deferred green verdicts; no independent scalar to disagree with |

The parenthetical “(7/7 checks)” is a gloss. The program prints one status line per check id. Seven `PASS` lines and exit 0 make the gloss true. Not recorded as a mismatch.

“0 failures over 10 assertions” is a paraphrase of the printed `0 failure(s) over 10 assertions`. The number matches. Not recorded as a mismatch.

## Commands

### 1. `python3 verifiers/verify_corpus_integrity.py`

- argv: `python3` `verifiers/verify_corpus_integrity.py`
- cwd: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`
- exit: `1`
- stderr: empty (0 bytes)
- stdout sha256: `4ad79e6ca84e23cc21fb6e53fc86106bec1a0b6d64808d7d81cb61929cd180ed`
- last line: `7/9 checks pass; DRIFT: corpus.index.tracked_files, corpus.index.unindexed`
- stdout:

```
corpus.index    tracked=48 unindexed=1 stale=0 missing=0  (60 FILE-column patterns over 48 md files)
corpus.pointers report_dead=0/32 commit_total=27 unresolvable=0 nonhash=0 (shapes [relative=0, absolute=31, tilde=1, bare=0], quoted-excluded=2, pointer-excluded=8; sites in --json)
           unindexed: corpus/lessons/round-19-recensus.md
           report_pointers_excluded: corpus/knowledge/cold-run-round11.md:100: .ufo/reports/round-1/<lane>.md
           report_pointers_excluded: corpus/knowledge/cold-run-round11.md:142: .ufo/reports/round-1/<lane>.md
           report_pointers_excluded: corpus/knowledge/cold-run-round11.md:148: <repo>/.ufo/reports/round-11/kotoba.md
           report_pointers_excluded: corpus/knowledge/cold-run-round11.md:280: .ufo/reports/round-1/<lane>.md
           report_pointers_excluded: corpus/knowledge/cold-run-round11.md:66: .ufo/reports/round-1/<lane>.md
           report_pointers_excluded: corpus/knowledge/corpus-integrity-round11.md:116: .ufo/reports/round-1/<lane>.md
           report_pointers_excluded: corpus/knowledge/corpus-integrity-round11.md:218: .ufo/reports/round-1/<lane>.md
           report_pointers_excluded: corpus/knowledge/dispatch-prompt-audit-round7.md:42: .ufo/reports/round-1/<lane>.md
           commit_quoted: corpus/knowledge/claim-census-round12.md:95: 4dd7753 (quoted meta-finding)
           commit_quoted: corpus/lessons/round-6-aggregator-audit.md:45: round-N (quoted meta-finding)
DRIFT   corpus.index.tracked_files: observed=48 expected=47
DRIFT   corpus.index.unindexed: observed=1 expected=0 / empty
7/9 checks pass; DRIFT: corpus.index.tracked_files, corpus.index.unindexed
```

### 2. `python3 verifiers/verify_surfaces.py`

- argv: `python3` `verifiers/verify_surfaces.py`
- cwd: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`
- exit: `0`
- stderr: empty (0 bytes)
- stdout sha256: `549f90ff6ecf70c74a132d3914384f629e909eb219c4c084b93d2fb2a4e10660`
- last line: `PASS surfaces.excluded_reason: 9 excluded entries, all reasoned and listed in the inventory`
- stdout:

```
PASS surfaces.literal_present: 38 loader-kind entries verified against the dumps
PASS surfaces.no_uncovered_class: all 8 extracted loader class(es) declared
PASS surfaces.opencode_extract: opencode extraction 5/5 declared class(es) from 6/6 rules (OC-1, OC-2, OC-3, OC-4, OC-5, OC-6)
PASS surfaces.table_parity: inventory id set == baseline id set (38 ids)
PASS surfaces.literal_parity: 38 inventory row literal(s) match the baseline per id
PASS surfaces.kind_parity: 38 inventory row kind(s) match the baseline per id
PASS surfaces.excluded_reason: 9 excluded entries, all reasoned and listed in the inventory
```

This command runs `strings -n 4` on the host binaries named in the script. It does not read session JSONL.

### 3. `python3 verifiers/verify_corpus_independent.py`

- argv: `python3` `verifiers/verify_corpus_independent.py`
- cwd: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`
- exit: `1`
- stderr: empty (0 bytes)
- stdout sha256: `4000b59c21835f4a32f29ee3629a9e64da1652cfa0a52d90d1e7e427a04d7501`
- last line: `exit 1`
- stdout:

```
corpus independent derivation: /home/vgpnk/Projects/shokunin/kotoba-shokunin (HEAD b0c7cb2)
index   tracked_files=48 index_tokens=61 (outside coverage map=0) unindexed=1 stale=0 missing=0
points  candidates=40 checked=32 excluded=8 quoted=0 dead=0 shapes={'absolute': 31, 'tilde': 1, 'relative': 0, 'bare': 0}
commits candidates=29 citations=27 hex=27 quoted=2 nonhash=0 unresolvable=0
  corpus.index.tracked_files             observe  observed=48 INFO
  corpus.index.unindexed                 zero     observed=1 DRIFT
  corpus.index.stale_patterns            zero     observed=0 PASS
  corpus.index.missing_paths             zero     observed=0 PASS
  corpus.pointers.report_total           observe  observed=32 INFO
  corpus.pointers.report_dead            zero     observed=0 PASS
  corpus.pointers.commit_total           observe  observed=27 INFO
  corpus.pointers.commit_unresolvable    zero     observed=0 PASS
  corpus.pointers.commit_nonhash         zero     observed=0 PASS
  ! corpus/lessons/round-19-recensus.md
  ! corpus/knowledge/cold-run-round11.md:100: .ufo/reports/round-1/<lane>.md [angle-bracket]
  ! corpus/knowledge/cold-run-round11.md:142: .ufo/reports/round-1/<lane>.md [angle-bracket]
  ! corpus/knowledge/cold-run-round11.md:148: <repo>/.ufo/reports/round-11/kotoba.md [angle-bracket]
  ! corpus/knowledge/cold-run-round11.md:280: .ufo/reports/round-1/<lane>.md [angle-bracket]
  ! corpus/knowledge/cold-run-round11.md:66: .ufo/reports/round-1/<lane>.md [angle-bracket]
  ! corpus/knowledge/corpus-integrity-round11.md:116: .ufo/reports/round-1/<lane>.md [angle-bracket]
  ! corpus/knowledge/corpus-integrity-round11.md:218: .ufo/reports/round-1/<lane>.md [angle-bracket]
  ! corpus/knowledge/dispatch-prompt-audit-round7.md:42: .ufo/reports/round-1/<lane>.md [angle-bracket]
  ! corpus/knowledge/claim-census-round12.md:95: 4dd7753
  ! corpus/lessons/round-6-aggregator-audit.md:45: round-N
exit 1
```

The two corpus instruments agree with each other (`tracked=48`, `unindexed=1`, the same lesson file, `report_dead=0`) and disagree with the lesson’s exit-0 / 9/9 record.

### 4. `bash verifiers/fault_injection_corpus.sh --self-test`

- argv: `bash` `verifiers/fault_injection_corpus.sh` `--self-test`
- cwd: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`
- exit: `1`
- stderr: empty (0 bytes)
- stdout sha256: `52e2330f92d0603242db89b2a2f61d7414a767bb8673c15e9b2f42d1b85f7f3d`
- last line: `self-test: BROKEN`
- stdout:

```
self-test: building fixture worlds under /tmp/round12-faults.1319282
self-test T1 must-fire assertion fires on planted (a): PASS
self-test T2: FAIL (exit=1)
self-test T4 plant guard rejects unmutated world (marker absent): PASS
self-test T3: FAIL
self-test: BROKEN
```

T1 and T4 passed. T2 and T3 are the clean-world assertions (`fault_injection_corpus.sh` self-test: an unmutated clone must exit 0). `new_world` clones committed state only. [INFERENCE] those two FAILs are the committed unindexed lesson, not the untracked `plans/` file: the working tree’s integrity exit 1 names that tracked file, and a committed-only clone includes it and excludes `plans/`. This seat did not keep the clone JSON (`--keep-worlds` was not passed).

### 5. `python3 verifiers/verify_harness_claims.py --self-test`

- argv: `python3` `verifiers/verify_harness_claims.py` `--self-test`
- cwd: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`
- exit: `0`
- stderr: empty (0 bytes)
- stdout sha256: `0367caaac4041033681ed421144846853413972d9b848d04a53e0fb67b147edf`
- last line: `self-test: 0 failure(s) over 10 assertions`
- stdout is that single line.

`self_test()` (`verify_harness_claims.py:580-616`) checks preview truncation and frontmatter chomping only. It returns before any session, log, or binary read. It does not execute `CHECKS`, so exit 0 does not corroborate the `at_least` → `equal` edit. The live command was not run.

### 6. `python3 verifiers/verify_skill_checklist.py`

- argv: `python3` `verifiers/verify_skill_checklist.py`
- cwd: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`
- exit: `1`
- stderr: empty (0 bytes)
- stdout sha256: `542915d972cc5de174331e85935c633a1c8d6acf6947b48faeb5cc709804d288`
- last line: `FAIL governance.citation_resolves: evaluated 131 — LOG.md:974: '.ufo/waves/shokunin12h-20261014-p1-repair/members/' does not resolve from /home/vgpnk/Projects/shokunin/kotoba-shokunin; 6 quoted meta-finding(s), 3 schematic token(s) excluded`
- stdout:

```
PASS checklist.box_map_complete: evaluated 41 — 41 boxes mapped (8 executed, 0 delegated, 33 unexecuted)
PASS trigger.frontmatter_parses: evaluated 4 — frontmatter parses: name='kotoba-shokunin', description 814 chars
PASS trigger.name_directory: evaluated 1 — name 'kotoba-shokunin' == directory 'kotoba-shokunin'
PASS trigger.literal_trigger_string: evaluated 1 — description carries literal 'Triggers:'
PASS trigger.anti_trigger_clause: evaluated 1 — exclusion marker 'Anti-triggers' present (vocabulary test, not semantics: a vacuous 'Never use this skill.' passes and an unlisted real exclusion fails)
FAIL trigger.line_budget: evaluated 601 — 601 lines exceed budget 600 (from box at line 329)
PASS trigger.no_placeholder: evaluated 552 — no placeholder markers in 552 scanned lines
PASS trigger.command_binary_resolves: evaluated 19 — 15 segments; 19 command subject(s) resolve
PASS trigger.citation_resolves: evaluated 42 — 42 repo-rooted citation token(s) resolve from the repo root
FAIL governance.citation_resolves: evaluated 131 — LOG.md:974: '.ufo/waves/shokunin12h-20261014-p1-repair/members/' does not resolve from /home/vgpnk/Projects/shokunin/kotoba-shokunin; 6 quoted meta-finding(s), 3 schematic token(s) excluded
```

`SKILL.md` is 601 lines (`wc -l` and a newline count). The binding box is `SKILL.md:329` (`File ≤ 600 lines`). The lesson’s quoted FAIL line omits ` (from box at line 329)`. The 601 and the budget 600 match.

## Counterexamples

1. Committed lesson is outside the coverage map. `git ls-files` lists `corpus/lessons/round-19-recensus.md`. A search of `corpus/` for `round-19` / `recensus` hits that file and not `corpus/README.md`. `verifiers/corpus-baseline.json` pins `corpus.index.tracked_files` expect `47` (equal) and `corpus.index.unindexed` expect `0` (zero-mode; the baseline note says zero-mode ignores `expect`). Observed: tracked 48, unindexed 1, that file named. This is why integrity is 7/9 exit 1 and independent is exit 1.
2. Fault self-test is not OK on this HEAD. T2 printed `FAIL (exit=1)`. T3 printed `FAIL`. Last line `self-test: BROKEN`.
3. Checklist is not a single carried line-budget FAIL. `governance.citation_resolves` also FAILs, and it is the last line. `LOG.md:974` backticks `.ufo/waves/shokunin12h-20261014-p1-repair/members/`. That path is absent under `kotoba-shokunin` (`test -e` → ABSENT). The same directory exists at `/home/vgpnk/Projects/shokunin/.ufo/waves/shokunin12h-20261014-p1-repair/members` (directory; 5 names matching `Kotoba*.md`; contents not read). The lesson’s own copy of that family (`round-19-recensus.md:4`) includes `*`, which `citation_subjects` drops, and governance scans only `LOG.md` and `SCORECARD.md`, so the lesson copy is invisible to this gate.

Not a counterexample: surfaces 7/7 exit 0; harness self-test 0/10 exit 0; line-budget 601/600 exit 1 as a count.

Not run, and not a counterexample: live `python3 verifiers/verify_harness_claims.py`; `bash verifiers/fault_injection_corpus.sh` without `--self-test`.

## Named debt

1. Unindexed round-19 lesson, plus a stale tracked-file pin. Owner: kotoba. Evidence: integrity DRIFT lines and independent `! corpus/lessons/round-19-recensus.md`. Unblock: add a coverage-map row for `corpus/lessons/round-19-recensus.md` (zero-mode `unindexed` cannot be baselined away) and re-record `corpus.index.tracked_files` expect 47 → 48, then re-run integrity, independent, and `fault_injection_corpus.sh --self-test`. Do not raise the pin while the file stays unindexed.

2. Live citation that does not resolve from the lane root. Owner: kotoba. Site: `LOG.md:974`, introduced in `b0c7cb2` (that commit modifies `LOG.md`). Token: `.ufo/waves/shokunin12h-20261014-p1-repair/members/`. It is not a deleted fleet path; it is a fleet-root path written as repo-rooted. `citation_resolve` accepts a leading `../` hop (max 3) and existence-tests it (`verify_skill_checklist.py:1117-1138`). Unblock: cite a form that exists from this repo, such as `../.ufo/waves/shokunin12h-20261014-p1-repair/members`, then re-run `python3 verifiers/verify_skill_checklist.py`. Same-line double quotes would exclude it as a meta-finding rather than make it navigable; that is not an unblock if the pointer is meant to be live.

3. Carried line budget. Owner: kotoba. `SKILL.md` is 601 lines; box at line 329 binds 600. Pre-existing on parent `02302c52` (also 601) and not touched by this commit. The lesson’s “pre-existing” claim agrees. Unblock: trim `SKILL.md` to ≤600. Do not raise the budget to go green.

Lesson-named prose debt (v1 opencode model still taught in `SKILL.md`; lowercase `/home/vgpnk/projects/...` cites; stale harness-verifier count prose) was not re-measured here. Outside the safe gate set. This seat neither confirms nor clears it.
