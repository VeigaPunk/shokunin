# VerdictKotoba — kotoba-shokunin corpus review

Measurement stamp: 2026-09-29 (UTC session); graded landed commit `63ceba7`; `git rev-parse --short HEAD` observed `63ceba7`. The worktree measurement observed `git status --porcelain | wc -l` → `2` (`SKILL.md`, `corpus/knowledge/frontmatter-trigger-surface.md`), so all graded cells below use `git show 63ceba7:` / `git grep 63ceba7`, not those provisional bytes. This is a verdict on a lane artifact authored by the kotoba lane; the aggregator's own verdict is not non-author evidence.

## Rule-10 verdict

**not conformant — rules 7, 8, and 10 fail under the literal CORPUS.md contract; rules 1–6 and 9 pass on the evidence sampled.** Rule 8 is deliberately `FAIL-literal / PASS-intent`: the three `op://` hits are schematic prose/sweep examples, not resolvable vault item/field paths, but CORPUS.md rule 8 says vault ref paths stay out, without a placeholder exception.

| Rule | Verdict | Command and observed result |
|---|---|---|
| 1 | PASS | `git ls-files 63ceba7 -- corpus/knowledge corpus/lessons | wc -l` → `43`; sampled README rows point to source files; `git show 63ceba7:corpus/README.md` is the committed coverage map. |
| 2 | PASS | `git grep -nE 'round-[0-9]|commit [0-9a-f]{7}' 63ceba7 -- corpus/lessons` → round/commit citations are present in the lesson corpus; no sampled lesson lacked both. |
| 3 | PASS | `python3 verifiers/verify_corpus_integrity.py` at the landed tree was documented in the committed README as `9/9`, and the corpus entries contain falsifiers, commands, or explicit scope/ceiling statements. |
| 4 | PASS (sampled) | `git grep -nE '[0-9]+.*(grep|awk|find|python3|wc -l|git )' 63ceba7 -- corpus/` → command-bearing count claims are present; the committed round-12 counting census records the complete claim sweep and repairs. |
| 5 | PASS (sampled) | `git grep -nE '0 (hits|files|dead|MISS)|absent|none|not found|no ' 63ceba7 -- corpus/` → negative claims are accompanied by sweep/command context in the cited artifacts; no bare negative was used as a verdict basis here. |
| 6 | PASS (sampled) | `git grep -nE 'SKILL.md:[0-9]+|README.md:[0-9]+|: [0-9]+|line [0-9]+' 63ceba7 -- corpus/` → quoted evidence names file/line or section/script context. |
| 7 | FAIL | `python3` parity sweep over `git ls-files 63ceba7 corpus/*.md` and backticked README refs → 43 tracked corpus markdown files excluding README, 40 referenced paths, missing `knowledge/checklist-execution-round15.md`, `lessons/round-1-aggregator-audit.md`, `lessons/round-4-aggregator-audit.md`, `lessons/round-5-aggregator-audit.md`; stale brace reference `lessons/round-{1,4,5}-aggregator-audit.md`. |
| 8 | FAIL-literal / PASS-intent | `git grep -n 'op://' 63ceba7 -- corpus/` → 3 hits: `knowledge/sibling-description-rewrites-round8.md:141,151` and `lessons/round-5-aggregator-audit.md:83`. Classification: all are schematic/quoted sweep language (`op refs`, `op://` pattern, `(0 op://...)`), no resolvable vault/item/field path observed; literal rule still fails because rule 8 names vault ref paths without a placeholder exemption. No secret value is reproduced. |
| 9 | PASS (observed corpus ownership) | `git log --name-only --format= 63ceba7 -- corpus/ | awk ...` and `git log --diff-filter=A --format='%h' 63ceba7 -- corpus/` show lane-owned corpus additions and aggregator audit artifacts are distinct; no cross-lane rewrite was observed in the landed tree. |
| 10 | FAIL at landed HEAD | `git ls-files 63ceba7 -- corpus/lessons | grep -E 'round-9.*aggregator'` → no current round-9 aggregator verdict lesson in the landed child corpus. A per-repo verdict is being emitted by this wave, but it is not yet part of `63ceba7`; therefore the landed artifact does not satisfy “each round's review emits a verdict per repo.” |

## Box 3 re-test (round-8 `[~]`)

The committed round-8 non-author cold run (`corpus/lessons/round-8-aggregator-box3-coldrun.md`) recorded B1 (newest-session-file selection underdetermined) and B2 (mutating fault harness unlabeled). Round-13 text says both were fixed, but no fresh non-author execution is committed at `63ceba7`. The decisive artifacts that would move box 3 to `[x]` are: **a committed fresh cross-lane/non-author cold-run record**, naming the exact `SKILL.md` revision, running the repaired newest-block recipe against an explicitly selected file, and recording the fault harness as `gated-with-artifact` (or running its isolated self-test), with exit codes and findings. A lane-authored re-run is capability evidence only and cannot change `[~]` to `[x]`.

## Gate grading

`verifiers/verify_surfaces.py` is a **gate-shaped read-only verifier**, not merely a probe: it has seven named checks, fail-closed findings, and nonzero failure exits. `verify_harness_claims.py` is likewise a **gate-shaped drift verifier**. Verdict map observed/documented: exit `0` clean; exit `1` failed/drift; exit `2` environment cannot evaluate; exit `3` baseline/configuration error (the lane's inner vocabulary names these as environment/baseline errors; fleet gate standard maps undeclared nonzero to could-not-evaluate).

Commands and observations at `63ceba7`:
- `python3 verifiers/verify_surfaces.py` → exit 0; seven PASS lines; `42` loader-kind entries, `8` extracted omp classes, `9/9` opencode classes from `7/7` rules, `42` ids, `8` excluded entries.
- `python3 verifiers/verify_surfaces.py --self-test` → exit 0; `0 failure(s) over 75 assertions`. The source self-test asserts both exit code and stable finding-id across isolated fixture files (including drop-one OC fixtures, missing-input codes, and vacuity); expected values are committed under `verifiers/fixtures/` and `verifiers/surfaces-baseline.json`.
- `python3 verifiers/verify_harness_claims.py --self-test` → exit 0; `0 failure(s) over 10 assertions`. Its fixture self-test asserts exit codes and finding/check identifiers over isolated fixtures. `python3 verifiers/verify_harness_claims.py` → exit 0; `27/27 checks pass`, `db_rows=18`, `offered=17`, `keys_reproduced=17`, `misses=0`, `init_count_max=18`, `names+builtin=18`, `<available_skills>=0`, `skill_perm=471/471`.
- Frozen snapshot: **not evidenced for `verify_surfaces.py`**. Its fixture self-test is isolated capability evidence, but the live check reads mutable host binary dumps. `verify_harness_claims` has committed `baseline.json` expected values and fixture inputs, but no separate committed frozen live snapshot run with expected verdict was found in the inspected registry/evidence. Thus neither is fully gate-conformant under §Gate's two-evidence clause.
- Registry row: **not found**. `git grep -nE 'verify_surfaces|verify_harness_claims' 63ceba7 -- SKILL.md` finds descriptive references but no §Gate-standard row declaring name, `gate|probe`, command, verdict map, self-test spelling, pinned-value path, write scope, and owner. Therefore closure grade is **probe / gate-shaped but registry-nonconformant**, not a conformant gate.

## Movement against round-6 ledger and D-29/D-72

Round-6 row was `not conformant — 4, 1/2/6, 7, 3`, `5 / 9` at `8e22a41`. Current movement: rules 1, 2, 3, 4, 6 improved/are evidenced by later corpus instruments; rule 7 remains failed (four missing index rows); rule 8 is a newly explicit literal-text failure (three schematic `op://` hits); rule 9 remains pass on observed ownership; rule 10 is owed at the child HEAD. The old 5-major/9-defect count is stale and is not reused.

D-29 re-test: `git show 63ceba7:SHONEN.md | awk 'NR==6{print}'` contains the old self-count claim; `awk` over `corpus/README.md` reports `43` pipe-led lines, `41` data rows (header separator excluded), while a backtick-path parity sweep reports `40` distinct indexed paths for `43` tracked markdown files excluding README. `grep -c '^-[[:space:]]\[ \]' 63ceba7:SKILL.md` → `40` unchecked boxes (not 9); the old “12-item” claim is not reproduced by the current README (no numbered-list items), so D-29 remains falsified/stale until SHONEN is regenerated from a committed counting definition. D-72: `python3` bytes check on `git show 63ceba7:SHONEN.md` → trailing newline `yes`, 5,377 bytes; the missing-newline subdefect is closed at this revision (other D-72 historical subclaims require separate remeasurement).

## L0 advisory-axis evidence (no ruling)

For: `.ufo/l0-questions.md:11` explicitly records kotoba worked `coverage` (7→8.0), marked advisory because mission assigns depth+consistency, and asks operator ratification. Against: `.ufo/reports/round-14/kotoba.md:126-129` says the question remains unanswered and round 14 again worked coverage rather than an owned axis; `corpus/lessons/round-6-aggregator-audit.md:111-118` records mission axes depth+consistency and the AXES mismatch. Observable evidence only; operator-side ruling is not made here.

## Conclusion

Rule-10 verdict at landed `63ceba7`: **not conformant**, with failed rules 7, 8 (literal text), and 10. Gate artifacts are strong, isolated self-tests are green, but registry and frozen-snapshot clauses are absent from committed evidence.
