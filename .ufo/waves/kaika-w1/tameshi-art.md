# kaika W1 — ART dossier · lane `tameshi` (verification-fixture craft)

- Author: W1ArtTameshi (scout, read-only) · 2026-10-19 · lane repo `/home/vgpnk/Projects/shokunin/tameshi-shokunin`.
- Read in the lane (ART scope only): `corpus/README.md`, `PROVINCE.md`, `corpus/QUALITY.md`, `SKILL.md` headings plus the specific lines cited below, `corpus/knowledge/` filenames; everything else by counting sweep.
- Tools: `web_search` available and used. Every SOURCES row in §3 was opened in this session. One fetch failed: ACM DL `https://dl.acm.org/doi/fullHtml/10.1145/3476105` returned HTTP 403, so it stays under Leads.
- Prompt-injection check: no opened page carried instructions addressed to an agent. Four repos ship agent config (`shrinkray/.claude`, `shmutant/.claude`, `shmutant/agents.toml`, `mutate4bash/SKILL.md`). None of them was opened or followed.
- Labels: **O** observed (read or ran it) · **I** inference · **U** unknown.
- Tiering rule used: an arXiv preprint is tier A when it is an original multi-author empirical study. S012 is tier B because the paper itself says it covers one system and has one author.

---

## 1. Uncovered ground — what the lane already holds

### 1.1 Held (O)

- Domain: "verification-fixture craft — the reusable method of honest checks: hermetic suites, mutation testing, fail-closed arms, verdict-line discipline" (PROVINCE.md:3-5).
- Generality rule: "a pattern is admitted from evidence in TWO independent lanes before it is claimed general" (PROVINCE.md:15-16). External art does not count as lane evidence. It can inform a pattern but cannot promote it to general.
- Knowledge notes: 19 — `ls corpus/knowledge/*.md | wc -l`. They are arm-class-matrix, closeout-r11, executor-test-sufficiency, fleet-kill-rate-ledger, fleet-suite-census, gates-survey-kagi, gates-survey-kumitate, mutation-case-{kagi-census, kagi-checklist, kimi-census, kumitate-claims, mado-verify, tsukuroi-census}, operator-runbook, self-hardening-r6, service-{limits, optin-protocol, standing-state} and verification-patterns-fleet.
- Lessons: 2 — `ls corpus/lessons/*.md | wc -l` (round-1, round-10).
- Admission criteria: 5 — `grep -cE '^[0-9]+\. ' corpus/QUALITY.md`.
- SKILL.md H2 sections: 21 — `grep -c '^## ' SKILL.md`. The method spine is:
  - Gate-shape decision table (:58), mutation bar (:94), Mutation-sweep recipe (:131), Defect-taxonomy templates (:246), Kill-rate bands (:314).
  - Restore discipline (:375), Cross-language divergence (:405), No-permissiveness audit (:466), Fail-closed arm taxonomy (:497).
  - Appendix A/B worked cases (:527, :594), Third case (:668), Mutation service (:794), Leg ledger (:921).
  - Re-sweep cadence (:1010), first tick + service limits (:1155), Operator runbook (:1272), Final pointers (:1365), Promotion calibration (:1464).
- Coverage map: 9 rows — ``grep -cE '^\| `knowledge/' corpus/README.md``. They cover 6 distinct notes — ``grep -oE '^\| `knowledge/[^`]+`' corpus/README.md | sort -u | wc -l``.
- Method elements the lane already holds and that current art extends (O):
  - Single-exact-edit mutants behind a count==1 uniqueness gate (corpus/README.md:15).
  - A red control is a setup failure: "A red control has no denominator" (SKILL.md:148).
  - Killed requires a red run AND the full case count (SKILL.md:191-194).
  - Inconclusive includes timeout, and inconclusive runs are excluded from the rate (SKILL.md:208-212).
  - A manual non-equivalence probe for every survivor (SKILL.md:214-223).
  - "One defect per class per sweep" (SKILL.md:249).
  - Zero-work refusal (SKILL.md:506).
  - Deferral only through a data-file tag plus a both-paths selftest (SKILL.md:507).
  - "a rate is bounded by its defect vocabulary" (SKILL.md:860-861).
  - T1: "never an edit of the recorded table" (SKILL.md:1071-1072).

### 1.2 The held corpus is entirely fleet-internal (O, negative sweep)

Command, run from the lane root:

```
for t in 'LANG=|LC_ALL|LANGUAGE=|TZ=|HOME=' 'witness' 'no.?coverage' 'incremental' 'golden' 'flak' 'snapshot test|snapshot-test' 'property.based' 'Stryker|mutmut|cargo-mutants|pitest' 'shrink(ray|er)|delta.debug|ddmin|test-case reduc' 'https?://' 'accidental'; do printf '%s\tfiles=%s\tlines=%s\n' "$t" "$(grep -rEil -- "$t" SKILL.md PROVINCE.md corpus | wc -l)" "$(grep -rEih -- "$t" SKILL.md PROVINCE.md corpus | wc -l)"; done
```

- All 12 terms returned files=0 and lines=0. The lane cites no external URL at all.
- Anchored-oracle terms: 0 — `grep -rEih 'state-anchored|specification-anchored|anchored oracle' SKILL.md PROVINCE.md corpus | wc -l`.
- `oracle`: 2 lines — `grep -rEih 'oracle' SKILL.md PROVINCE.md corpus | wc -l`. Both use "offline guessing oracle" in the secret-hash sense (gates-survey-kagi.md:182, service-limits.md:125). The lane has no test-oracle concept.
- `determinis`: 7 lines — `grep -rEih 'determinis' SKILL.md PROVINCE.md corpus | wc -l`. All are gate-level, for example proxy-check's determinism case (gates-survey-kumitate.md:178, fleet-suite-census.md:284). None is in the sweep recipe.

### 1.3 The frontier is undeclared (O)

- `## Frontier` in corpus/README.md: 0 — `grep -c '^## Frontier' corpus/README.md`.
- Core/Frontier/Adjacent markers in PROVINCE.md: 0 — `grep -ciE '^(\*\*|#+ )?(core|frontier|adjacent)' PROVINCE.md`.
- External-source terms in QUALITY.md: 0 — `grep -Eic 'tier|SOURCES|recheck|url|external' corpus/QUALITY.md`.
- Notes missing from the coverage map: 13 of 19 — `for f in corpus/knowledge/*.md; do b=$(basename "$f"); grep -qF "knowledge/$b" corpus/README.md || echo "$b"; done | wc -l`.

### 1.4 Uncovered ground (I, from 1.1–1.3)

1. External mutation-score semantics and report interop. The lane has no Stryker, cargo-mutants, mutmut or PIT vocabulary and no NoCoverage state.
2. Witness-scoped kill verdicts (0 `witness`, 0 `accidental`).
3. A determinism precondition, and flaky-test research in general (0 `flak`).
4. Golden and snapshot fixture discipline (0 `golden`, 0 `snapshot test`).
5. Property-based testing as a fixture generator (0 `property based`).
6. Fixture and test-case reduction (0 hits).
7. Hermetic environment normalization (0 env pins).
8. Incremental re-sweep granularity (0 `incremental`). The cadence work (SKILL.md:1010-1153) works at pin level (I).
9. Oracle anchoring as a survivor class (0).
10. LLM-era mutant generation and equivalence detection. The lane only has the manual probe (SKILL.md:214-223).

---

## 2. Current art 2025–2026 the corpus does not hold

1. **LLM mutation aimed at one concern, plus LLM equivalence filtering, in production.** Meta ACH (arXiv 2501.12862, 2025-01-22) makes few mutants, each specific to an issue and currently undetected, then writes tests that kill them.
   - Its equivalent-mutant agent scored "precision of 0.79 and a recall of 0.47 (rising to 0.95 and 0.96 with simple pre-processing)" (Abstract).
   - 9,095 mutants became 571 tests, and engineers accepted 73% of those tests. → S007.
   - Contrast (O): tameshi hand-writes about 10 defects per sweep, one per class (SKILL.md:246-250), and probes equivalence by hand (SKILL.md:214-223).
2. **Bash mutation tooling with a written verdict contract.** shmutant had 239 commits and 0 stars when opened.
   - It separates killed-on-witness from accidental kills, and has separate `unapplied` and `baseline` verdicts.
   - It refuses a non-unique old literal and writes a tab-separated verdict stream.
   - It runs only the selected tests per row. Its own CI figures, unverified: 940 s for the per-row pass, against more than 10 h if the whole suite ran for every row. → S006.
3. **mutmut 3.7–3.8.**
   - 3.7.0 added per-function source hashing and cross-call invalidation.
   - 3.8.0 fixed mutants stopped by the CPU-time limit "being reported as killed instead of timed out".
   - 3.8.0 also fixed false survivors when a test clears `os.environ`, and added fork-server process isolation. → S005.
4. **Incremental reuse rules, written down.**
   - StrykerJS incremental mode reuses a verdict only if the killing test is unchanged, or if no new test covers the mutant. Its docs list blind spots: env vars, dependencies and `.snap` changes. → S003.
   - cargo-mutants `--in-diff` and `--iterate` come with explicit cautions. → S004.
   - The canonical root is Google's diff-scoped mutation (2021). → S008.
5. **A cross-tool report schema.** mutation-testing-report-schema has a status enum of 8 values (Killed, Survived, NoCoverage, CompileError, RuntimeError, Timeout, Ignored, Pending). It also records `killedBy`, `coveredBy` and `statusReason`. → S002.
6. **Agentic PBT.** Maaz, DeVoe, Hatfield-Dodds and Carlini (arXiv 2510.09907, 2025-10-10): an agent infers properties, writes Hypothesis tests and reflects on the results before reporting. 56% of its reports were valid bugs. → S021. PBT-Bench (arXiv 2605.15229, 2026-05-13) benchmarks the same skill; it was opened but not given a row.
7. **PBT practice baselines.**
   - Python (EMSE, online 2026-08-24): 367 PBTs; Test Oracle is the largest category at 29.97%; Ghostwriter fully automates only 18.23%. → S020.
   - Jane Street interviews (ICSE 2024). → S019.
8. **Oracle anchoring.** Canedo (arXiv 2608.17214, 2026-08-17): an expectation that is state-anchored, meaning it flows from the code under mutation, cannot fail. Re-anchoring one oracle recovered 8 of 46 mutants without touching production code. → S012.
9. **Reducers whose LLM proposals still have to pass the interestingness test.** shrinkray uses calendar versioning from 2025–2026. Its LLM mode is on by default, but a proposal is accepted only if the interestingness test still passes. → S023.
10. **CI-mode defaults for expected values.**
    - Jest 30.5 `--ci` fails on a new snapshot instead of writing it.
    - Jest `--collectTests` counts tests without running them, and the count matches a run in which every selected test passes. (I) That gives a second, non-executing count to cross-check tameshi's "executed summary line is the only honest count" (corpus/README.md:7). → S013.
    - insta's `INSTA_UPDATE=auto` resolves to `no` in CI. → S014.
    - Hypothesis has a built-in `ci` profile (derandomized, no example database). → S018.
    - Hypothesis `@example(...).xfail()` "allow[s] you to check that your test does fail on some examples". This is the PBT-side analog of tameshi's load-bearing bar (SKILL.md:94-97).
11. **Environmental flakiness.**
    - Hashemi et al. (arXiv 2602.19098, 2026-02-22) found 65 environment-flaky JS projects across OS, Node.js version and browser. → S027.
    - Systemic flakiness (arXiv 2504.16777, 2025) was opened but not given a row.

Older sources kept because they are still authoritative:

- S009 TCE is still the cheapest equivalence filter.
- S010 is the subsumption validity threat.
- S011 is the only paper here that joins flakiness to mutation verdicts.
- S025 is the first extensive flaky study, by its own claim.
- S026 gives industrial flakiness rates.
- S008 is Google's diff-scoped mutation.
- S022 explains internal reduction.
- S015 and S016 are transcript-style and txtar fixtures.
- S028 is normative and current.

---

## 3. `SOURCES.md` rows

| id | source | kind | tier | teaches | status | opened | recheck | used-by |
|---|---|---|---|---|---|---|---|---|
| S001 | Mutant states and metrics (Stryker Mutator docs) — https://stryker-mutator.io/docs/mutation-testing-elements/mutant-states-and-metrics/ | docs | A | 8 mutant states; score = detected/valid x100 with detected = killed + timeout; compile and runtime errors excluded; a separate score on covered code; test states killing, covering, not covering | queued | 2026-10-19 | 180d | — |
| S002 | mutation-testing-report-schema.json (stryker-mutator/mutation-testing-elements) — https://raw.githubusercontent.com/stryker-mutator/mutation-testing-elements/master/packages/report-schema/src/mutation-testing-report-schema.json | spec | A | JSON Schema for cross-tool mutation reports: per-mutant id, mutatorName, location, status enum of 8, killedBy, coveredBy, statusReason, testsCompleted; a ready shape for exporting a kill-rate ledger | queued | 2026-10-19 | on-release | — |
| S003 | Incremental (StrykerJS docs) — https://stryker-mutator.io/docs/stryker-js/incremental/ | docs | A | when a prior verdict may be reused (killed: culprit test exists and is unchanged; not killed: no new covering test and no test changed); the dry run is still required; declared blind spots are env vars, deps and .snap files | queued | 2026-10-19 | 180d | — |
| S004 | cargo-mutants book: Using the results (also chapters in-diff.html and iterate.html) — https://mutants.rs/using-results.html | docs | A | outcomes caught, missed, unviable, timeout, with unviable = inconclusive; tests must first pass reliably in a copied tree; --in-diff runs no mutants for test-only diffs; --iterate assumes changes never reduce coverage | queued | 2026-10-19 | on-release | — |
| S005 | mutmut changelog HISTORY.rst (boxed/mutmut) — https://raw.githubusercontent.com/boxed/mutmut/main/HISTORY.rst | code | A | harness bugs the maintainers recorded, read as method lessons: CPU-time-limited mutants misreported as killed (fixed 3.8.0); env-clearing tests produced false survivors (fixed 3.8.0); per-function hash invalidation (3.7.0) | watch | 2026-10-19 | on-release | — |
| S006 | shmutant README (BWBama85/shmutant) — https://github.com/BWBama85/shmutant | code | A | bash/POSIX mutation contract: a row is old literal, replacement, witness; verdicts killed vs accidental, unapplied, baseline, plus aborted, timeout, unsettled, lost; a non-unique literal is refused; an empty table fails. Authoritative only for its own semantics (0 stars at open) | watch | 2026-10-19 | 90d | — |
| S007 | Mutation-Guided LLM-based Test Generation at Meta (Foster, Gulati, Harman et al.; arXiv 2501.12862) — https://arxiv.org/abs/2501.12862 | paper | A | concern-specific LLM mutants that are currently uncaught, then tests that kill them; LLM equivalent-mutant agent at precision 0.79 recall 0.47, or 0.95/0.96 with simple pre-processing; 9,095 mutants, 571 tests, 73% accepted | queued | 2026-10-19 | 365d | — |
| S008 | Practical Mutation Testing at Scale (Petrović, Ivanković, Fraser, Just; arXiv 2102.11378) — https://arxiv.org/abs/2102.11378 | paper | A | diff-scoped mutation at code review; mutants filtered and capped per line and per review; operators chosen by historical productivity; evaluated with 24,000+ developers on 1,000+ projects | queued | 2026-10-19 | 365d | — |
| S009 | Trivial Compiler Equivalence (Papadakis, Jia, Harman, Le Traon; ICSE 2015) — https://discovery.ucl.ac.uk/id/eprint/1499169/ | paper | A | identical compiled output marks a mutant as equivalent or duplicate; on large programs this discards over 7% equivalent and 21% duplicated mutants; it finds about 30% of all equivalents | queued | 2026-10-19 | 730d | — |
| S010 | Threats to the validity of mutation-based test assessment (Papadakis, Henard, Harman, Jia, Le Traon; ISSTA 2016) — https://discovery.ucl.ac.uk/id/eprint/1508136/ | paper | A | mixing subsuming and subsumed mutants distorts scores: Type I errors about 62% of the time without countermeasures; 68% of the surveyed studies were exposed | queued | 2026-10-19 | 730d | — |
| S011 | Mitigating the Effects of Flaky Tests on Mutation Testing (Shi, Bell, Marinov; ISSTA 2019) — https://mir.cs.illinois.edu/awshi2/publications/ISSTA2019.pdf | paper | A | kill verdicts assume determinism: scores varied about 4 points between runs, 9% of mutant-test pairs were unknown, 22% of statements were covered nondeterministically with zero observed failures; reruns cut unknown mutants by 79.4% | queued | 2026-10-19 | 730d | — |
| S012 | Oracles That Cannot Fail (Canedo; arXiv 2608.17214) — https://arxiv.org/abs/2608.17214 | paper | B | names state-anchored oracles, whose expectation flows from the code under mutation so the comparison cancels out; measured on one system (366 mutants); a preprint with one author, by its own statement | watch | 2026-10-19 | 90d | — |
| S013 | Jest CLI Options (Jest 30.5) — https://jestjs.io/docs/cli | docs | A | --ci fails on a new snapshot instead of writing it; --randomize with --seed reproduces order-dependent failures; --collectTests counts tests without running them | queued | 2026-10-19 | on-release | — |
| S014 | insta: Advanced Features (also /docs/redactions/) — https://insta.rs/docs/advanced/ | docs | A | INSTA_UPDATE=auto writes .snap.new locally and nothing in CI; --unreferenced=auto rejects orphan snapshots in CI; redactions replace volatile values by selector (static, dynamic, sorted, rounded) | queued | 2026-10-19 | on-release | — |
| S015 | Cram: It's test time — https://bitheap.org/cram/ | docs | A | shell-transcript golden tests: each output line is matched literally first, with opt-in (re), (glob), (no-eol), (esc) suffixes; the runner resets TMPDIR, LANG/LC_ALL/LANGUAGE=C, TZ=GMT, COLUMNS=80; exit 80 = skipped | queued | 2026-10-19 | 365d | — |
| S016 | testscript package doc (rogpeppe/go-internal) — https://raw.githubusercontent.com/rogpeppe/go-internal/master/testscript/doc.go | code | A | txtar scripts carry commands plus fixture files; each runs in a fresh $WORK with HOME=/no-home and TMPDIR=$WORK/.tmp; a ! prefix asserts failure; [net] and [exec:prog] conditions gate cases | queued | 2026-10-19 | 365d | — |
| S017 | bats-core: Writing tests — https://bats-core.readthedocs.io/en/stable/writing-tests.html | docs | A | each test runs in its own process (the file is evaluated n+1 times); focus mode forces exit 1 so that a committed bats:focus tag cannot silently run a subset in CI | queued | 2026-10-19 | on-release | — |
| S018 | Hypothesis API Reference — https://hypothesis.readthedocs.io/en/latest/reference/api.html | docs | A | a built-in ci profile activates whenever CI is set: derandomize=True, deadline=None, database=None, print_blob=True; @example(...).xfail() checks that a test can fail; shared read-only example databases | queued | 2026-10-19 | on-release | — |
| S019 | Property-Based Testing in Practice (Goldstein, Cutler, Dickstein, Pierce, Head; ICSE 2024) — https://harrisongoldste.in/papers/icse24-pbt-in-practice.pdf | paper | A | 30 Jane Street interviews: PBT pays off on complex code; its weaknesses are generator effort and no visible feedback on test effectiveness; names shrinking interfaces and effectiveness evaluation as open problems | queued | 2026-10-19 | 730d | — |
| S020 | Property-based testing in Python: empirical insights (de Oliveira, Corgozinho, Rocha, Valente; EMSE 2026) — https://link.springer.com/article/10.1007/s10664-026-10953-w | paper | A | 367 PBTs from 244 projects sorted into nine property categories (Test Oracle 29.97%); data generation is the main difficulty (36.62% of SO posts); Ghostwriter fully automates 18.23% | queued | 2026-10-19 | 365d | — |
| S021 | Agentic Property-Based Testing (Maaz, DeVoe, Hatfield-Dodds, Carlini; arXiv 2510.09907) — https://arxiv.org/abs/2510.09907 | paper | A | an LLM agent infers properties from code and docs, writes Hypothesis tests and reflects before reporting: 56% of reports were valid bugs; ranking lifts top-21 validity to 86% | watch | 2026-10-19 | 180d | — |
| S022 | Test-Case Reduction via Test-Case Generation: Insights from the Hypothesis Reducer (MacIver, Donaldson; ECOOP 2020) — https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ECOOP.2020.13 | paper | A | internal reduction shrinks the generator's choice sequence, so every reduced case is one the generator could have produced (sidestepping the test-case validity problem); compared with C-Reduce and delta debugging | queued | 2026-10-19 | 730d | — |
| S023 | Shrink Ray README (DRMacIver/shrinkray) — https://github.com/DRMacIver/shrinkray | code | A | a reducer driven by any executable interestingness test (exit 0 = interesting); parallel multi-format passes; local LLM proposals accepted only when the interestingness test still passes | watch | 2026-10-19 | 90d | — |
| S024 | Reducing Failure-Inducing Inputs (The Fuzzing Book, Zeller et al.) — https://www.fuzzingbook.org/html/Reducer.html | book | B | a runnable delta-debugging reducer: a Runner returns FAIL only on the precise error, and the input is cut to the minimum that still reproduces it | queued | 2026-10-19 | 365d | — |
| S025 | An Empirical Analysis of Flaky Tests (Luo, Hariri, Eloussi, Marinov; FSE 2014) — https://mir.cs.illinois.edu/marinov/publications/LuoETAL14FlakyTestsAnalysis.pdf | paper | A | 201 flaky-fix commits: the top causes are Async Wait, Concurrency and Test Order Dependency; 78% of flaky tests are flaky when first written; 74% of order-dependency fixes clean shared state | queued | 2026-10-19 | 730d | — |
| S026 | Flaky Tests at Google and How We Mitigate Them (John Micco, Google Testing Blog, 2016) — https://testing.googleblog.com/2016/05/flaky-tests-at-google-and-how-we.html | docs | A | about 1.5% of test runs are flaky; about 84% of pass-to-fail transitions involve a flaky test; a fail-3-in-a-row flaky mark cuts false positives but teaches people to ignore flakiness | queued | 2026-10-19 | 730d | — |
| S027 | A Systematic Evaluation of Environmental Flakiness in JavaScript Tests (Hashemi, Tahir, Shi, Rasheed, Blagojevic; arXiv 2602.19098) — https://arxiv.org/abs/2602.19098 | paper | A | varying OS, Node.js version and browser exposed 65 environmentally flaky JS projects (28 OS, 5 Node, 16 both, 17 browser); its sanitizer skips and reports such tests instead of failing them | watch | 2026-10-19 | 180d | — |
| S028 | Test encyclopedia (Bazel) — https://bazel.build/reference/test-encyclopedia | spec | A | normative hermetic test contract: the outcome depends only on declared inputs; the exit code alone decides and PASS or FAIL on stdout means nothing; LANG unset and TZ=UTC required; TEST_PREMATURE_EXIT_FILE catches early exits | queued | 2026-10-19 | 365d | — |
| S029 | mutate4bash README (lukasa1993/mutate4bash) — https://github.com/lukasa1993/mutate4bash | tool | C | rejected: 8 commits, 0 stars, and its semantics are documented only as exit codes (1 for timeout, syntax or compile error; 2 for survivors); no verdict contract to learn from; S006 covers the same ground | rejected | 2026-10-19 | 180d | — |
| S030 | LLMShot: Reducing snapshot testing maintenance via LLMs (Kaynak et al.; arXiv 2507.10062) — https://arxiv.org/abs/2507.10062 | paper | B | rejected for this lane: VLM triage of visual iOS UI snapshot diffs, while tameshi fixtures are the text verdict lines of CLI gates; an adjacent UI domain to report, not absorb | rejected | 2026-10-19 | 365d | — |

Counts. Set `F` to this file (`kaika-w1-tameshi-art.md` in the session `local/` directory) and run:

- Rows: 30 — `grep -cE '^\| S[0-9]{3} ' "$F"`.
- Tiers: A 26 · B 3 · C 1 — `grep -E '^\| S[0-9]{3} ' "$F" | awk -F'|' '{gsub(/ /,"",$5); print $5}' | sort | uniq -c`.
- Status: queued 22 · watch 6 · rejected 2 — `grep -E '^\| S[0-9]{3} ' "$F" | awk -F'|' '{gsub(/ /,"",$7); print $7}' | sort | uniq -c`.

**Contract defect (fleet D3/D4).** The draft example row `|S001|Title — …|` has no spaces around its cells, so the contract's own counting regex misses it:

- `printf '|S001|Title — https://example.org/page|docs|A|x|queued|2026-10-19|90d|—|\n' | grep -cE '^\| S[0-9]{3} '` → 0.
- The same row with spaces → 1.
- The rows above use the spaced form.

### Opened but not given a row (30-row cap) — wave 2 may promote these

- Just et al., *Are Mutants a Valid Substitute for Real Faults in Software Testing?* (FSE 2014) — https://homes.cs.washington.edu/~rjust/publ/mutants_real_faults_fse_2014.pdf. Canonical result: mutant detection correlates with real-fault detection independently of coverage (357 real faults, 5 applications). No row because tameshi reads kill rates as admission readings, not as a fault proxy.
- Parry, Kapfhammer, Hilton, McMinn, *Systemic Flakiness* (arXiv 2504.16777, 2025). 75% of 810 flaky tests fall into co-failure clusters (mean size 13.5), mostly caused by networking and external dependencies. Lower fit for hermetic suites.
- Jing et al., *PBT-Bench* (arXiv 2605.15229, 2026). 100 problems with 365 injected bugs; recall 42.1–83.4% across 8 LLMs. It measures agents, not fixtures.
- Tian et al., *LLMs for Equivalent Mutant Detection* (arXiv 2408.01760, 2024). 3,302 Java mutant pairs; LLM techniques beat prior ones by +35.69% F1 on average. S007's production numbers supersede it for this lane.
- trycmd docs — https://docs.rs/trycmd/latest/trycmd/. `[..]` and `...` elision plus `TRYCMD=overwrite`. Overlaps S015.
- Jest Snapshot Testing guide — https://jestjs.io/docs/snapshot-testing. "The snapshot artifact should be committed alongside code changes, and reviewed". Overlaps S013.
- Hypothesis settings tutorial — https://hypothesis.readthedocs.io/en/latest/tutorial/settings.html. Overlaps S018.
- prysk README, the maintained Cram fork — https://github.com/prysk/prysk. It also replaces the tmp directory with `$TMPDIR` in output. Overlaps S015.
- Go `go/printer` tests — https://go.dev/src/go/printer/printer_test.go:28 has `var update = flag.Bool("update", false, "update golden files")`. This is the Go stdlib convention of updating golden files only behind an explicit flag. Overlaps C4.

### Leads (unopened)

- *A Survey of Flaky Tests* (Parry, Hilton, Kapfhammer, McMinn; TOSEM 2021) — https://dl.acm.org/doi/10.1145/3476105 (HTTP 403 when tried).
- Zeller & Hildebrandt, *Simplifying and Isolating Failure-Inducing Input* (TSE 2002) — doi:10.1109/32.988498.
- Regehr et al., *Test-Case Reduction for C Compiler Bugs* (PLDI 2012) — doi:10.1145/2254064.2254104.
- MacIver, Hatfield-Dodds et al., *Hypothesis: A new approach to property-based testing* (JOSS 2019) — doi:10.21105/joss.01891.
- Petrović et al., *Does mutation testing improve testing practices?* (ICSE 2021) — arXiv 2103.07189.
- *LLMorpheus: Mutation Testing using Large Language Models* — https://arxiv.org/pdf/2404.09952.
- *A Comprehensive Study on Large Language Models for Mutation Testing* — https://arxiv.org/abs/2406.09843.
- *Mutation-Guided Unit Test Generation with a Large Language Model* — https://arxiv.org/abs/2506.02954.
- *Detecting Trivial Mutant Equivalences via Compiler Optimisations* (TSE 2018) — https://orbilu.uni.lu/bitstream/10993/31623/1/07882714.pdf.
- Cruz, Rocha, Valente, *Snapshot testing in practice: Benefits and drawbacks* (JSS 2023) — doi:10.1016/j.jss.2023.111797.
- Fujita, Kashiwa, Lin, Iida, *An empirical study on the use of snapshot testing* (ICSME 2023).
- *Flaky Tests in a Large Industrial Database Management System (SAP HANA)* — https://arxiv.org/abs/2602.03556.
- *On the Flakiness of LLM-Generated Tests for DBMS* — https://arxiv.org/abs/2601.08998.
- *230,439 Test Failures Later: flaky failure classifiers* — https://arxiv.org/abs/2401.15788.
- PIT incremental analysis — https://pitest.org/quickstart/incremental_analysis/.
- C-Vise — https://github.com/marxin/cvise.
- pbt-bibliography, a collaborative PBT bibliography and candidate learning hub — https://github.com/ngernest/pbt-bibliography.
- *Trace-Guided Synthesis of Effectful Test Generators* — https://arxiv.org/abs/2604.04345; *PROGRESS* — https://arxiv.org/abs/2607.27359.
- *Fuzzing with Agents? Generators Are All You Need* — https://arxiv.org/abs/2604.01442.
- Nelson Elhage, *Two kinds of testing* (linked from the Hypothesis settings tutorial) — https://blog.nelhage.com/post/two-kinds-of-testing/.
- HypoFuzz — https://hypofuzz.com/.
- *What Are Developers Actually Discussing When Visual Regression Tests Fail?* — https://arxiv.org/abs/2608.07020 (adjacent UI domain).

---

## 4. Candidate knowledge entries (6)

These are proposed `## Frontier` rows for `corpus/README.md`. F1–F6 each have an entry below. F7–F10 are reserve rows with no entry this round:

- F7 incremental re-sweep granularity (S003, S004, S005, S008).
- F8 oracle anchoring as a survivor class (S012).
- F9 LLM-era mutant generation and equivalence detection (S007, S009).
- F10 PBT generators for gate fixtures (S018–S021).

All recheck commands below were run on 2026-10-19; the arrow shows the count observed.

### C1 `mutation-score-semantics`

**Claim (falsifiable).**

- O: Stryker scores `detected / valid * 100`, where Detected = killed + timeout and Valid = detected + undetected. Compile and runtime errors are excluded (S001 `## Metrics`).
- O: cargo-mutants reports 4 outcomes and calls unviable mutants inconclusive (S004 `## Mutant outcomes`).
- O: tameshi's kill rate is killed / (killed + survived), and timeouts are Inconclusive, so they are excluded (SKILL.md:208-212).
- I: take k kills, s survivors (NoCoverage counted inside s) and t timeouts. Stryker's (k+t)/(k+s+t) is always ≥ tameshi's k/(k+s), and the two are equal exactly when t = 0.
- O: rounds 2 and 3 recorded "no inconclusive run" (corpus/README.md:13-14). Both rounds therefore read 80% under either formula.
- I: round-3 survivor B5 ("fixture-absent arm — no case reaches it", corpus/README.md:14) is what Stryker calls NoCoverage. D2, D10 and B10 are Survived. Stryker's covered-code score for round 3 would read 8/9 ≈ 88.9%, against 80% overall.
- U: B5's NoCoverage status holds only if a coverage trace of the selftest shows the arm never executes.

**Source, location, quote.**

- S001 `## Metrics`: "**Mutation score** `detected / valid * 100`".
- S001 `## Mutant states` (Timeout): "It is counted as "detected"."
- S004 `## Mutant outcomes`: "This is inconclusive about test coverage and no action is needed".
- S002: `"enum": ["Killed", "Survived", "NoCoverage", "CompileError", "RuntimeError", "Timeout", "Ignored", "Pending"]`.

**Fills.** SKILL.md `## Kill-rate bands` (:314), which lacks any external comparison; Frontier F1 (external score semantics and report interop).

**Recheck.**

- `curl -fsSL https://stryker-mutator.io/docs/mutation-testing-elements/mutant-states-and-metrics/ | grep -c 'detected / valid'` → 1.
- `curl -fsSL https://mutants.rs/using-results.html | grep -c 'inconclusive about test coverage'` → 1.
- `curl -fsSL https://raw.githubusercontent.com/stryker-mutator/mutation-testing-elements/master/packages/report-schema/src/mutation-testing-report-schema.json | grep -c '"NoCoverage", "CompileError", "RuntimeError", "Timeout"'` → 1.

**QUALITY.md.**

1. Falsifiable: the formulas and the recorded tallies can be recomputed.
2. Anchored: URL, section and recheck command, plus SKILL.md:208-212 and corpus/README.md:13-14.
3. O, I and U are separated as above.
4. Nothing to correct yet.
5. The rejected sibling candidate R3 (timeout counted as a kill) is kept in §6.

### C2 `witness-scoped-kill-verdict`

**Claim.**

- O: in shmutant a row carries a name, an old literal, a replacement and a witness (S006 `## The three verdicts`, `## How a row is run`).
  - `killed` requires the run to go red on its witness; red anywhere else is `accidental`.
  - `unapplied` and `baseline` are separate verdicts.
  - A non-unique old literal is refused, and an empty table is a hard failure.
- O: tameshi counts a kill when the run is red AND the suite still reports its full case count (SKILL.md:191-194).
- O: tameshi records failing-case labels after the run (SKILL.md:230-232). 0 lines in the lane mention witness or accidental (§1.2 sweep).
- I: tameshi's "killed" is the union of shmutant's killed and accidental. Tameshi already holds equivalents of shmutant's other guards:
  - the count==1 gate (corpus/README.md:15) matches the non-unique refusal;
  - a red control as setup failure (SKILL.md:148-149) matches `baseline`;
  - the full-count guard matches `SHMUTANT_COUNTS=1`.
- Next measurement (falsifiable): declare one witness per defect before re-running a recorded manifest.
  - Before: the number of accidental kills is undefined.
  - After: a count of killed-on-witness and accidental kills that sums to the recorded kills (8 in round 2).
- This extends the fleet's P1 rule, "declared falsifiable claim before the move" (corpus/README.md:9), to single defects.

**Source, location, quote.**

- S006 `## The three verdicts`: "The suite went red, but not on its witness. Caught by accident, not by the assertion that claims to cover it."
- S006 `## How a row is run`, step 1: "A row whose old literal occurs more than once in its target there is refused".

**Fills.** SKILL.md `## Mutation-sweep recipe` step 7 (:191-213) and the manifest columns in `## Defect-taxonomy templates` (:246); Frontier F2 (witness-scoped kills, bash mutation tooling).

**Recheck.** `curl -fsSL https://raw.githubusercontent.com/BWBama85/shmutant/main/README.md | grep -c 'not on its witness'` → 1.

**QUALITY.md.**

1. Falsifiable: the semantics are documented, and the future count is defined.
2. Anchored: README sections plus the sweep command.
3. O, I and U are separated.
4. U: shmutant's adoption (0 stars, 239 commits at open) and its self-reported CI timings are unverified. It is tier A only for its own semantics.

### C3 `determinism-precondition`

**Claim.**

- O: Shi et al. found that mutation scores vary between repeated executions (S011 Abstract).
  - Suites with no observed failure still covered statements nondeterministically: 113,356 statements, 22%, across 30 projects and 17 runs (S011 §2.1 Table 1).
  - Their reruns cut unknown mutants by 79.4% (Abstract).
- O: cargo-mutants requires a tree whose tests pass "reliably" when copied (S004).
- O: Luo et al. found 78% of flaky tests are flaky from the moment they are written (S025, F.2).
- O: tameshi's recipe requires a green control before mutants (SKILL.md:145-149) and says "Control first: run the unmutated copy" (SKILL.md:179-180).
- O: the corpus has one gate-level determinism case (gates-survey-kumitate.md:178) and no sweep-level repetition rule. In the §1.2 sweep, `determinis` gives 7 lines and none is in the recipe.
- U: whether `tools/mutate-and-run.sh` repeats the control. The tool was not read in ART scope.
- Proposal (falsifiable): require N ≥ 3 control runs whose per-case lines are byte-identical after the volatile scrub.
  - Before: one named control run.
  - After: N control runs.

**Source, location, quote.**

- S011 Abstract: "mutation scores vary by four percentage points on average between repeated executions, and 9% of mutant-test pairs have an unknown status".
- S011 §2.1: "We observe no test failures in any of the runs, and hence, to the casual observer, there are no flaky tests."
- S004 `## Tests fail in an clean tree?`: "cargo-mutants can’t do anything until you have a tree where `cargo test` passes reliably when copied to a temporary directory."

**Fills.** SKILL.md `## Mutation-sweep recipe` steps 1 and 6 (:138-149, :179-182); Frontier F3 (determinism precondition, flaky-aware verdicts).

**Recheck.** `curl -fsSL https://mir.cs.illinois.edu/awshi2/publications/ISSTA2019.pdf | pdftotext - - | grep -c 'mutant-test pairs'` → 33. Also citable by DOI 10.1145/3293882.3330568.

**QUALITY.md.** Falsifiable through N identical controls; anchored as above; the open question about the tool is kept explicit (U).

### C4 `expected-values-never-written-in-ci`

**Claim.**

- O: three fixture tools default to not writing expected values in CI.
  - Jest `--ci` fails on a new snapshot instead of storing it (S013 `--ci`).
  - insta's default `INSTA_UPDATE=auto` means `no` in CI and `new` (writing `.snap.new`) locally. `--unreferenced=auto` rejects orphan snapshots in CI (S014 §Controlling Snapshot Updating, §Handling Unused Snapshots).
  - Hypothesis activates its `ci` profile whenever CI is set, with `derandomize=True` and `database=None` (S018, settings profiles).
- O: tameshi's ledger rule "never an edit of the recorded table" (SKILL.md:1071-1072) is the same principle applied to the kill-rate ledger.
- I: gate selftests that hard-code expected verdict lines, such as `KIMI_CENSUS_SELFTEST: 43/43 pass` (SKILL.md:146), are golden values. By the external rule, those lines should change only through an explicit, reviewed act.
- U: how fleet gates update their expected lines (sibling code, not read here). A round could measure the count of update paths that write expected values without an explicit flag.

**Source, location, quote.**

- S013 `### --ci`: "Instead of the regular behavior of storing a new snapshot automatically, it will fail the test and require Jest to be run with `--updateSnapshot`."
- S014 §Controlling Snapshot Updating: "`auto`: the default. `no` for CI environments or `new` otherwise".
- S018: "If the `CI` environment variable is set to any value, the `ci` profile is active by default."

**Fills.** Frontier F4 (golden and snapshot fixture discipline), where the lane has 0 `golden` and 0 `snapshot test` lines.

**Recheck.**

- `curl -fsSL https://jestjs.io/docs/cli | grep -c 'storing a new snapshot automatically'` → 1.
- `curl -fsSL https://insta.rs/docs/advanced/ | grep -c 'for CI environments'` → 1.
- `curl -fsSL https://hypothesis.readthedocs.io/en/latest/reference/api.html | grep -c 'If running on CI, the default is'` → 3.

**QUALITY.md.** Falsifiable per tool and version (Jest docs 30.5); anchored; O, I and U separated.

### C5 `hermetic-env-normalization`

**Claim.**

- O: three runners normalize the environment before a test runs.
  - Bazel's normative spec requires LANG and LANGUAGE unset and TZ=UTC, recommends HOME=$TEST_TMPDIR, confines writes to $TEST_TMPDIR, and lets only the exit code decide (S028 §Initial conditions, §Role of the test runner).
  - Cram resets TMPDIR, TEMP and TMP, and sets LANG/LC_ALL/LANGUAGE=C, TZ=GMT and COLUMNS=80 (S015 §Usage).
  - testscript runs each script in a fresh $WORK with HOME=/no-home and TMPDIR=$WORK/.tmp (S016).
- O: tameshi defines a hermetic suite only by where its fixtures live: "fixtures under `mkdtemp` only, cleaned in `finally`; no live path read" (SKILL.md:62).
- O: 0 lines across SKILL.md, PROVINCE.md and corpus/ set LANG=, LC_ALL, LANGUAGE=, TZ= or HOME= (§1.2 sweep).
- O: tameshi's verdict rule is stricter than Bazel's. It needs the expected exit AND the expected ERE on the last non-empty line (corpus/README.md:8).
- I: output that depends on locale or timezone, such as sort order or dates, can make a "hermetic" selftest depend on the host. Kagi's live gate already showed host-state dependence (`--falsify` 16/18, corpus/README.md:8).
- Measurement (falsifiable): run each surveyed selftest under `env -i PATH="$PATH" LANG=C LC_ALL=C TZ=UTC HOME="$(mktemp -d)"` and again under the host environment.
  - Before: unmeasured.
  - After: N/N identical summary lines, or the gates that differ, by name.
- Related (O): Bazel's TEST_PREMATURE_EXIT_FILE is an external analog of tameshi's zero-work refusal (SKILL.md:506).

**Source, location, quote.**

- S028 §Background: "Tests should be *hermetic*: that is, they ought to access only those resources on which they have a declared dependency."
- S028 §Role of the test runner: "writing any of the strings `PASS` or `FAIL` to stdout has no significance to the test runner."
- S015: "`LANG`, `LC_ALL`, and `LANGUAGE` are set to `C`."
- S016: "Each script runs in a fresh temporary work directory tree, available to scripts as $WORK."

**Fills.** The hermetic row of SKILL.md `## Gate-shape decision table` (:62); Frontier F5 (hermetic environment normalization).

**Recheck.**

- `curl -fsSL https://bazel.build/reference/test-encyclopedia.md | grep -c 'TEST_PREMATURE_EXIT_FILE'` → 1.
- `curl -fsSL https://bitheap.org/cram/ | grep -c 'is set to <code>GMT</code>'` → 1.
- `curl -fsSL https://raw.githubusercontent.com/rogpeppe/go-internal/master/testscript/doc.go | grep -c 'HOME=/no-home'` → 2.

**QUALITY.md.** The negative claim carries its sweep, the measurement is defined before and after, and the sources are anchored.

### C6 `survivor-probe-reduction`

**Claim.**

- O: shrinkray reduces with any executable as its interestingness test, where exit 0 means interesting. It accepts LLM-proposed candidates only through that same test (S023 §Usage, §LLM mode).
- O: a reducer cuts the input to "the minimum that still reproduces the failure" (S024 §Synopsis).
- O: internal reduction keeps every reduced case one the generator could produce, which mitigates the test-case validity problem (S022 Abstract).
- O: tameshi's survivor step needs a probe input outside the suite's fixtures on which the mutant's output differs from pristine (SKILL.md:214-223). B5's probe is a host tree plus census, shapes and baseline files (SKILL.md:622).
- I: an interestingness test that says "pristine still exits inside its valid lattice AND pristine and mutant outputs differ" turns a reducer into a generator of minimal killing fixtures. The validity problem (S022) is why the pristine-side condition is needed.
- Experiment (falsifiable): reduce B5's probe fixture in scratch.
  - Before: the probe's size (files, bytes).
  - After: the reduced size, plus a check that the reduced fixture, added as a case, kills B5 in a scratch copy (mutant red, pristine green).

**Source, location, quote.**

- S023 §Usage: "`is_interesting.sh` can be any executable that exits with `0` when a test case passed to it is interesting and non-zero otherwise."
- S023 §LLM mode: "they're only accepted if your interestingness test still passes, so a bad model costs time but never correctness."
- S022 Abstract: "ensuring that any reduced test case is one that could in principle have been generated".

**Fills.** Frontier F6 (fixture minimization for survivors), where the lane has 0 reduction lines.

**Recheck.**

- `curl -fsSL https://raw.githubusercontent.com/DRMacIver/shrinkray/main/README.md | grep -c 'when a test case passed to it is interesting'` → 1.
- `curl -fsSL https://www.fuzzingbook.org/html/Reducer.html | grep -c 'still reproduces the failure'` → 1.
- S022 by DOI 10.4230/LIPIcs.ECOOP.2020.13.

**QUALITY.md.** The source facts are observed. The technique stays an inference (I) until the experiment runs, and the experiment states its before and after.

---

## 5. Paths

- **Mutation verdict semantics and validity** — S001 → S002 → S004 → S006 → S011 → S010 → S009 → S007. Learn the vocabulary first (states, schema, outcomes), then the verdict grammar (witness). Then learn what makes a verdict untrustworthy (flakiness, subsumption). Finish with equivalence, from the cheapest filter (TCE) to an LLM agent.
- **Golden and hermetic fixtures for CLI gates** — S015 → S016 → S017 → S028 → S013 → S014 → S018. Start with shell-transcript golden tests, then txtar fixtures in a fresh $WORK, then bash runner isolation and the focus guard. Read the normative hermetic spec next. End with how JS, Rust and Python tools refuse to write expected values in CI.
- **Reduction and generation of fixtures** — S024 → S022 → S023 → S019 → S020 → S021 → S012. Do delta debugging by hand, then learn internal reduction and the validity problem, then a modern reducer whose LLM proposals still pass through the interestingness test. Move on to PBT practice and its Python baseline, then agentic PBT. End with why a generated oracle can still never fail.

---

## 6. Rejected candidates (with reasons)

- **R1 — S029 mutate4bash (source).** The README documents semantics only as exit codes, the repo has 8 commits and 0 stars, and there is no verdict contract to learn from. S006 covers the same ground with a written contract.
- **R2 — S030 LLMShot (source).** It triages visual iOS UI snapshot diffs. Tameshi's fixtures are the text verdict lines of CLI gates, so this belongs to an adjacent UI/visual domain: report it, do not absorb it (PROVINCE.md:20).
- **R3 — candidate rule "count Timeout as detected" (Stryker's rule).** Tameshi names a timeout inconclusive, "Not a kill" (SKILL.md:208-209), and its kills require the full case count (SKILL.md:191-193). A timeout reports no count, so adopting the rule would admit kills with no denominator evidence. It stays a comparison (C1), not a rule change.
- **R4 — candidate rule "skip and report environment failures"** (S027's js-env-sanitizer). Its runtime classification turns a red run into a skip with no declared tag. Tameshi's and kagi's deferral needs the tag in the data file plus a both-paths selftest (SKILL.md:507), which is the stronger form. S027 is kept only as evidence of environmental-flakiness rates.
- **R5 — candidate metric "PBT-Bench bug recall as a lane measure".** It benchmarks LLM agents, not fixtures. The paper itself says the hardest bugs "prove model-specific" (abstract, arXiv 2605.15229), so it is out of province.

---

## 7. Mistakes mined from current art (external failure modes and how tameshi captures them)

| # | Mistake class | External evidence | Tameshi capture | Proposal if not captured |
|---|---|---|---|---|
| M1 | A timeout scored as a kill | S005 3.8.0: "Fix mutants stopped by the CPU-time limit being reported as killed instead of timed out" | Captured: Inconclusive includes timeout, "Not a kill" (SKILL.md:208-209) | — |
| M2 | The harness's mutant switch is silently disabled, producing false survivors | S005 3.8.0: false survivors when a test uses `patch.dict(os.environ, ..., clear=True)` | Captured by construction: every mutant is a separate file and the recipe asserts its sha256 ≠ pristine (SKILL.md:179-182) | — |
| M3 | A red run anywhere counted as a kill (accidental kill) | S006 `accidental` verdict | Not captured: Killed = red + full count (SKILL.md:191-194); `witness` has 0 lines (§1.2) | Declare a witness case for each defect before the run, and score killed vs accidental (C2) |
| M4 | A defect that injected nothing still gets scored | S006 `unapplied` verdict | Captured: count==1 uniqueness gate (corpus/README.md:15) plus sha ≠ pristine (SKILL.md:182) | — |
| M5 | One green control taken as proof of determinism | S011 Abstract and §2.1; S004 clean-tree rule | Partial: a red control is a setup failure (SKILL.md:148-149), but only one control run is named (SKILL.md:179-180); the tool's repeat count is U | N ≥ 3 identical control runs (C3) |
| M6 | Incremental reuse blind to env changes and test-only changes | S003 limitations; S004 in-diff and --iterate cautions | Partial (I): legs re-pin by trigger (SKILL.md:1069-1090), and embedded selftests move with the gate's own pin; host and env drift are not pinned (kagi host-state dependence, corpus/README.md:8) | Record an env fingerprint (LANG, TZ, tool versions) in every leg receipt |
| M7 | Re-running until green masks real failures | S026: a flaky mark reports failure "only if it fails 3 times in a row" | Partial: "Re-run it; keep every record" (SKILL.md:209) | A re-run never overwrites an earlier record; both records count |
| M8 | Duplicate or subsumed mutants inflate the rate | S010; S009 (21% duplicates) | Partial: "One defect per class per sweep" (SKILL.md:249); "a rate is bounded by its defect vocabulary" (SKILL.md:860-861); there is no duplicate check | (I) Flag mutant pairs that the suite cannot tell apart (identical per-case verdict vectors) before tallying |
| M9 | An accidental subset run passes CI | S017 focus-mode exit override; S028 premature-exit file | Captured: full-count guard (SKILL.md:191-193) and zero-work refusal (SKILL.md:506) | — |
| M10 | The expectation is derived from the code under test (anchored oracle) | S012 | Not captured: 0 test-oracle lines (§1.2) | Add an "anchored oracle" class to the survivor taxonomy beside "reported-but-unasserted" and "fixture-absent arm" (F8) |

Tally: 10 classes mined. 4 are captured (M1, M2, M4, M9), 4 are partial (M5, M6, M7, M8) and 2 are not captured (M3, M10).

---

## 8. Defects found (ART scope)

- **DF1.** 13 of the 19 knowledge notes are missing from the coverage map. Command in §1.3.
- **DF2.** corpus/README.md has no `## Frontier` section: `grep -c '^## Frontier' corpus/README.md` → 0.
- **DF3.** PROVINCE.md has no Core, Frontier or Adjacent sections: `grep -ciE '^(\*\*|#+ )?(core|frontier|adjacent)' PROVINCE.md` → 0.
- **DF4.** QUALITY.md has no admission criterion for external sources: `grep -Eic 'tier|SOURCES|recheck|url|external' corpus/QUALITY.md` → 0.
- **DF5.** The lane cites 0 external URLs: `grep -rEih -- 'https?://' SKILL.md PROVINCE.md corpus | wc -l` → 0.
- **DF6.** In the fleet draft of the SOURCES contract, the example row fails its own counting regex (0 vs 1; see §3).

---

## 9. Recommendations

1. **Open the registry and the frontier.**
   - Create `corpus/SOURCES.md` from §3 (rows 0 → 30) and a `## Frontier` section (rows 0 → 10, F1–F10).
   - Add a 6th QUALITY criterion: an external claim needs a tiered SOURCES row and a recheck command, and a tier-C row is never the sole support.
   - Admit C1 and C2 first. Both re-read rounds that are already recorded (C1's 80% check needs no new sweep), and both sit on the lane's core.
2. **Turn two zero-hit sweeps into counted preconditions.**
   - Determinism: N ≥ 3 identical control runs before any mutant (C3).
   - Environment: an env-differential selftest run (C5).
   - Each goes from "unmeasured" to a number that a non-author can replay.
3. **Make fixture minimization a measured technique.**
   - Pilot a reducer on B5's survivor probe (C6) and keep the before and after sizes plus the kill check.
   - Keep the fast-moving tools (shmutant, mutmut, shrinkray) and the 2025–2026 preprints on `watch` with their stated recheck cadence.
