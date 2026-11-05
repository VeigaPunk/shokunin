# kotoba — round 87 report (hyaku run 15, Linux host, omp/18.15.0)

Lane repo `/home/vgpnk/Projects/shokunin/kotoba-shokunin`, branch `master`.
Base `223ae62424f8ab1eb365d733eb648d6228ddd7e8` (the round-86 non-author spot-check landing).
Freeze `669f2801c31ef27e18cc35a327d2e18f466281c7` (`plans/round-87.md` alone, before any candidate
data); addendum 1 `512126bbd762ff82b9f330c4afefb29db7cd9f39`; addendum 2
`87ab1cb98b4950f5d7291a4a2ddaab535ca72124`. Attempt 1; no earlier attempt of this round exists
(`grep -n 'kotoba round=87' .ufo/watchdog.log` → one `launch` line, no `lane-dead-no-report`).

**Declared claims.** Two, on two distinct owned axes, both carried from the round-86 closure's
routed-defect queue (`.ufo/waves`-adjacent record: `corpus/lessons/round-86-verifier-spotcheck.md`
§ 6) — that queue is the queue of record:

- **C1 — depth** (score 9, the lane's lowest owned axis): *omp root semantics grounded per root*.
  The round-86 ledger grounds each discovery root with a quote that merely *occurs* in the binary;
  the closure's CF1 found that no such quote can ground the plugin root (its quote is the `.omp`
  config constant, and the reader is a `join(...)` call), CF2 that `{cwd}/` expansion reaches
  `$HOME`. C1 lands a second ledger whose rows carry the **reader code line** and the **module**,
  with the walk-up bound and the `..` refusal as conjuncts.
- **C2 — consistency (calibration sub-axis)** (score 10): *the round-86 closure's five routed defects
  close* — D1 tip after-values without committed receipts, D2 the planner-seat reason asserted not
  cited, D3 a `## Gate` with no reject row, D4 a kill rule that does not name the data boundary,
  D5 the carried base red.

No claim is exploratory. Both are measured by a frozen counter committed before any candidate score.

## Work performed

- **C1 counter `verifiers/check_omp_root_semantics.py`** — frozen predicate
  `python3 -B verifiers/check_omp_root_semantics.py --rev <rev>` → `omp root semantics grounded N of
  12`, exit 0 iff N == 12 and guards S1–S3 PASS. Four per-row conjuncts (pattern / reader code line
  with a path-join token / module header before the quote / expansion bound) and three guards
  (S1 committed bytes, S2 the ELF sha256 pin, S3 the 12-pattern set). `--self-test` `0 failure(s)
  over 35 assertions`. Counter sha256 `6e826f3bf8d4585340ddcc9b7a546e4b7d8b9774a2794c4f45b3cf13e7798922`.
  Evidence: `verifiers/check_omp_root_semantics.py`; `.ufo/waves/round-87/receipts/c1-instrument-freeze.txt`.
- **C1 ledger `verifiers/omp-skill-roots-semantics.tsv`** — 12 rows,
  `root_pattern<TAB>binary_quote<TAB>module<TAB>reader_quote`; every `reader_quote` is the join call
  that builds the root (e.g. `dir: Zo.join(R.path, "skills"),` for the plugin root). The round-86
  ledger and its frozen counter are untouched (that counter requires exactly two tab cells per row —
  a third column there would have turned its G4 red). Evidence: the ledger; ELF offsets and mmap
  commands at `.ufo/waves/round-87/w1/ExecLedger/receipts-elf-reads.txt`.
- **C1 knowledge entry `corpus/knowledge/omp-root-semantics-round87.md`** — the 12-row table
  (root · module · reader quote · bound), three author-facing rules (quote the join, not the doc
  string; `{cwd}/` stops below `$HOME`; a `..` segment never matches), a `## Bound` line, provenance
  trio on S256. Evidence: the entry; `corpus/README.md` coverage-map row.
- **C1 source row S256** — omp plugin skill-root reader, `coding-agent/src/discovery/omp-plugins.ts`,
  upstream tag v18.15.0, HTTP 200, 15 362 B, sha256 `4e66819cf706b81c6f31bd71e6de8892083a284525ab151948642faea00cb1b4`,
  located quote at upstream line 70. Evidence: `corpus/SOURCES.md` (row S256);
  `.ufo/waves/round-87/w1/ScoutPlugin/SOURCE_RECORD.txt`.
- **C2 counter `verifiers/check_r86_routed_repairs.py`** — frozen predicate
  `… --rev <rev>` → `r86 routed defects closed N of 5`, exit 0 iff N == 5; five items recomputed from
  committed bytes; `--self-test` `0 failure(s) over 53 assertions`. Evidence: the counter;
  `.ufo/waves/round-87/receipts/c2-after.txt`.
- **D1 tip receipts** — `.ufo/waves/round-86/receipts/tip-catalogue.txt` (`omp catalogue lines
  reproduced 215 of 215`, exit 0) and `tip-registry.txt` (`gate registry rows conformant 67 of 67`,
  exit 0), each naming the measured revision, with the two instruments byte-identical from the
  round-86 landing `04647b0f`. Evidence: those two files (the seat's own wave dir was left empty, so the receipts are
the evidence).
- **D5 honest carry** — `verifiers/corpus-baseline.json` re-recorded from the gate's own
  `--no-baseline --json` (three `equal` counts only; every `zero` expectation left at zero), the two
  new corpus files indexed in `corpus/README.md`, and the two remaining DRIFTs disclosed in the
  lesson. Evidence: `verifiers/corpus-baseline.json`; `.ufo/waves/round-87/receipts/d5-after-revert.txt`;
  `corpus/lessons/round-87.md` § D5 disclosure.
- **M87-1 mined and its fix landed** — a wave seat greened the carried red by rewriting the two
  citing records in place; both reverted to their branch bytes before any commit, and D5 conjuncts
  (i)/(ii) now compare both blobs to base. Evidence: `corpus/lessons/round-87.md` § Mistakes;
  `receipts/d5-after-revert.txt`; the `w_launder` self-test arm.
- **Gate with real rejects** — five reject rows in the lesson (the round-86 plugin doc quote as a
  reader, a doc `reader_quote`, the two in-place rewrites, the 13-row denominator, the frozen D5
  form). Evidence: `corpus/lessons/round-87.md` § Gate; C2's D3 reads `5 reject row(s), longest
  reason 52 words`.
- **Frontier curation** — one row opened this round (S256), census exit 0 before and after; a
  `## Frontier` note and two coverage-map rows appended to `corpus/README.md`; Q78 added to
  `corpus/QUALITY.md` from `considerthese/2026-10-26.md` proposal 1, grounded on the measured
  `600 lines / 86 416 B / 156 lines > 120 chars / longest 1 170` at `9b040ed`. Evidence:
  `receipts/base-battery.txt`, `receipts/census-after.txt`, `corpus/QUALITY.md` Q78.
- **Attack seats** — `ReviewerC1` built an independent implementation of the four conjuncts and five
  worlds (`w1/ReviewerC1.md`, `w1/ReviewerC1/`); `MutTester` mutated both counters
  (`w1/MutTester/mutate_run.py`); `Sentinel` found the 13/12 denominator defect and the clone-only
  D5 impossibility (`Sentinel-4` report, 21:0x) — both became addenda 1 and 2 before any candidate
  score. `Critic` died on a provider 401 at wake with no answer (see round shape).
- **Planner seat mapping** — the §3 planner seat is held by the L1; the swarm validator's
  `SWARM_ROLES` excludes `planner` (`~/Projects/ufo-fsd-alpha/scripts/ufo-swarm-wave.mjs:263-275`,
  quoted verbatim in the plan and re-parsed by C2's D2), and the planning data-walk rode the
  connector and the two scouts.

## Landed changes

Every change is in `LOG.md` § "Round 87" and carries its commit:

| change | commit | LOG entry |
|---|---|---|
| `plans/round-87.md` (frozen plan) | `669f2801` | § Round 87, opening |
| wave r87-w1 spec, dispatch, base battery | `9b040edb` | § Round 87, "Wave" |
| `plans/round-87-addendum-1.md` (denominator 12; D5 worktree) | `512126bb` | § Round 87, "Correction" |
| `verifiers/check_omp_root_semantics.py` + instrument receipt; `plans/round-87-addendum-2.md` | `87ab1cb9` | § Round 87, C1 |
| `verifiers/omp-skill-roots-semantics.tsv`, `corpus/knowledge/omp-root-semantics-round87.md`, `corpus/lessons/round-87.md`, `corpus/SOURCES.md` S256, `corpus/QUALITY.md` Q78, `corpus/README.md`, `SKILL.md` two registry rows, D1 tip receipts, wave-1 evidence | `e03f9e22` | § Round 87, C1/C2/Frontier |
| `verifiers/check_r86_routed_repairs.py`, `verifiers/corpus-baseline.json`, `corpus/README.md` index rows | `ff4bf3fd` | § Round 87, C2 / No-harm |
| `LOG.md`, `SCORECARD.md` round-87 blocks; inherited duplicate-L1 w2 artifacts + `INHERITED-w2.txt` | `fcdaba57` | § Round 87 (this entry) |
| inert duplicate-L1 w2 artifacts removed per the orchestrator ruling (note kept) | `4620a630`, `760e1c5e` | § Round 87, Inherited |
| wave receipts (`c1-after`, `c1-after-tip`, `c2-after`, `after-battery`, `province-core-tip`) | `35a395a9` | § Round 87, C1/C2 |
| `receipts/c2-final.txt` (C2 measured at `35a395a9` with a clean worktree) | `3cabd895` | § Round 87, C2 |

`SKILL.md` stayed inside its budget by merging two wrapped paragraph lines before adding the two
gate-registry rows: `600 of 600` lines, `87 772` bytes.

## Before → after measurements

**C1 — depth.** Counting command (frozen, sha256 `6e826f3b…8922`):

```
python3 -B verifiers/check_omp_root_semantics.py --rev <rev>
```

| | value | revision | receipt |
|---|---|---|---|
| before | `omp root semantics grounded 0 of 12`, `guard S3 pattern-set FAIL`, `exit=1` | `223ae62424f8ab1eb365d733eb648d6228ddd7e8` | `.ufo/waves/round-87/receipts/c1-instrument-freeze.txt` |
| after | `omp root semantics grounded 12 of 12`, `guard S3 pattern-set PASS`, `exit=0` | `e03f9e226b51b8cb94f2dc5c7c3027c5286b004b` | `.ufo/waves/round-87/receipts/c1-after.txt` |
| after (measured tip) | `12 of 12`, `exit=0` | lane tip | `.ufo/waves/round-87/receipts/c1-after-tip.txt` |

**C2 — consistency.** Counting command (frozen):

```
python3 -B verifiers/check_r86_routed_repairs.py --rev <rev>
```

| | value | revision | receipt |
|---|---|---|---|
| before | `r86 routed defects closed 0 of 5`, `exit=1` | `223ae62424f8ab1eb365d733eb648d6228ddd7e8` | `.ufo/waves/round-87/w1/ExecRepairs/base.txt` |
| after | `r86 routed defects closed 5 of 5`, `exit=0` (D1–D5 all PASS) | `ff4bf3fd70662f20ab066eee6fde4bd605aa07b6` | `.ufo/waves/round-87/receipts/c2-after.txt` |
| after (measured tip, worktree clean) | `5 of 5`, `exit=0` | `35a395a9aabfe2c849628bb4cfe9b25f176de411` | `.ufo/waves/round-87/receipts/c2-final.txt` |

Both counters were frozen (bytes committed) before the first candidate score; the two addenda that
corrected a miscount and an unsatisfiable item are committed at `512126bb` and `87ab1cb9`, and
neither changed a target. **Honest bound:** per Q71/Q74 the number alone is not the evidence where a
mechanical world can reach it — the attack seats' worlds and the `--self-test` arms are the
discrimination evidence, and the semantic half of C1 (whether a reader quote is the reader) rests on
`w1/ReviewerC1.md` and the non-author closure, not on the count.

## Sources & frontier

- **Census** (frozen command `bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate
  --root /home/vgpnk/Projects/shokunin kotoba`): **before** `exit=0`, 33 `W04`, 0 `E` rows
  (`receipts/base-battery.txt`); **after** `exit=0`, 33 `W04`, 0 `E` rows, last line
  `kotoba ok …/corpus/SOURCES.md` (`receipts/census-after.txt`).
- **Rows before → after:** 181 → 182 (`grep -cE '^ {0,3}\| S[0-9]{3}' corpus/SOURCES.md` → 182).
  **Added by tier:** 1 × tier A (`S256`, `kind: code`, status `mined`, opened 2026-11-04, recheck
  `on-release`). **Rows touched old→new:** 0 other rows.
- **Frontier rows advanced:** the loader-rule row (`corpus/README.md` § Frontier) gains this round's
  per-root code grounding (append-only note); the coverage map gains rows for the round-87 entry and
  lesson. `PROVINCE.md` untouched (its § Frontier/§ Adjacent pin in `check_province_core.py` holds).
- **Assimilation: none** — `/home/vgpnk/Projects/shokuknow/merge/` is absent on this host
  (`ls /home/vgpnk/Projects/shokuknow/merge/` → `No such file or directory`), so no package could be
  adopted; no id-collision check was run because no staged row exists.
- **`considerthese`** — `considerthese/2026-10-26.md` proposal 1 mined into `corpus/QUALITY.md` Q78
  (a size ceiling is a ratchet measured at the freeze), grounded on this round's own measurement;
  the floors-guard change is routed, not landed, because a ceiling red at base cannot land.

## Trend verdicts

- **expansion — `improved`.** One tier-A source row opened and grounded (S256), one new knowledge
  entry, two new coverage-map rows, one frontier note; census 181 → 182 rows with exit 0 at both
  ends.
- **quality — `improved`.** C1 replaces a presence-floor grounding with per-root reader-code
  grounding (12 of 12, four conjuncts, three guards); the corpus gate moves `3/9` → `7/9` with the
  two remaining DRIFTs named; the gate registry moves `67 of 67` → `69 of 69` with no phantom;
  `SKILL.md` stays `600 of 600` lines with two new registry rows.
- **discernment — `improved`.** Two addenda were forced by attack seats **before any candidate
  score** (a miscounted denominator and an unsatisfiable D5), and M87-1 — a routed red greened by
  rewriting the record that carried it — was caught at integration, reverted, and turned into a
  gate conjunct shown able to fail. The lesson's `## Gate` carries five reject rows instead of none.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — evidence: the two new gate-registry rows at `SKILL.md` (registry `69 of 69` conformant at the measured tip, `python3 -B verifiers/check_gate_registry.py --rev <tip>`), the registry rows for both new counters, and `corpus/knowledge/omp-root-semantics-round87.md`'s three author-facing rules indexed in `corpus/README.md`.
- [~] At least one end-to-end domain task executed and logged in LOG.md — evidence: `LOG.md` § Round 87 (C1's 12-row ELF grounding and C2's five-item closure, both measured on this host), receipts under `.ufo/waves/round-87/receipts/`.
- [~] Instructions executable by an agent without oral context — evidence: `corpus/lessons/round-87.md` and the two counters' docstrings carry the predicate, the conjuncts, the exit ladder and the receipts' locations; no fresh non-author cold run exists for this round (`corpus/knowledge/` still holds one cold-run record).
- [~] No cross-domain bleed (PROVINCE.md still accurate) — evidence: `git diff --stat 223ae62 <tip> -- PROVINCE.md` is empty (untouched this round); `python3 -B verifiers/check_province_core.py --rev <rev>` reads `province core rows 0 of 2` with `§ Frontier differs from the base` at base `223ae62` **and** at the tip (a carried red, unchanged by this round — receipt `.ufo/waves/round-87/receipts/province-core-tip.txt`); the connector seat produced no file (its absence is named in the round shape below).

**Round shape.** One v1 wave, **14 seats**, under `scripts/hyaku/ufo-wave-policy.json` (band 8–16):
scout 2, executor 4, scribe 3, connector 1, reviewer 1, critic 1, mutation-tester 1, sentinel 1.
Attack set (reviewer, critic, mutation-tester, sentinel) 4 of 14 = **28.6 % ≥ 25 %**; connectors 1
(≤ 2). No residual `task` call. Round total **14 seats**. Seats that died: **`Critic-3`** (wake turn
failed `commandcode/deepseek/deepseek-v4.1-flash` 401 `authentication_error`, no answer produced) and
**`ExecRepairs-3`** (same 401 at wake, after its counter and self-test had landed). Two scribe seats
(`ScribeEntry-10`, `ScribeLesson-42`) produced measurement artifacts but no production file; the L1
wrote the knowledge entry and the lesson from them. Wave settlement: `r87-w1-results.json` carries 14
rows with `status: null` and `output: null` (the settlement is read from the wave dir, as in round 86).

**Inherited / not mine.** A second L1 (`KotobaR87a3`) wrote a round-87 wave-2 spec, dispatch and
`r87-w2.ready` at 21:02 believing wave 1 had died; I alerted the orchestrator (`agent://Main`, 21:05)
and deleted the never-taken ready file (no `r87-w2.ready.dispatched` marker existed). The
orchestrator ruled: "r87-w2 will NOT dispatch … its w2 spec and dispatch files are inert; ignore
them and don't commit them", and confirmed `KotobaR87a3` died on a provider 401 without committing
(`jj log` over `223ae62..760e1c5e` shows only `kotoba-shokunin` commits). The artifacts had been
committed at `fcdaba57` before the ruling arrived and were removed at `4620a630`/`760e1c5e`; the
one-line record is `.ufo/waves/round-87/INHERITED-w2.txt`. No w2 seat was ever spawned. The `.scratch/*` and `.ufo/reports/round-84/kama.md` modifications at the fleet root
belong to other actors (misroot sweep: no file written by this round's seats at the fleet root).

**Stale-lane.** One mission for this lane, no respawn: `.ufo/watchdog.log` carries
`2026-11-04T19:56:11-03:00 launch kotoba round=87 … attempt=1` and no `lane-dead-no-report` line for
round 87; the round is the lane's only open mission.

**Carried reds, measured at base and at the tip (not this round's harm).**
`verify_corpus_integrity.py` `3/9` → `7/9` (six DRIFTs → the two disclosed ones);
`verify_corpus_independent.py` `exit=1` at base and at the tip;
`verify_skill_checklist.py` `governance.citation_resolves` FAIL at base and at the tip (10
quoted-meta-finding, 3 schematic-token and 2 recorded-absence exclusions apply; `+9 more` unresolved
tokens, all in `LOG.md`/`SCORECARD.md` historical correction rows);
`check_province_core.py` `province core rows 0 of 2` with `§ Frontier differs from the base` at base
and at the tip. `assertion_floors` PASS at base and at the tip; gate registry `67 of 67` → `69 of 69`
phantom 0; `SKILL.md` `600 of 600` lines at both ends.

**Lane tip.** `760e1c5edfdefb4767420f711d08f669952de013` — `git -C kotoba-shokunin ls-remote origin
refs/heads/master` prints it; `jj-lane.sh state` reads `ahead=0 behind=0 tracked=0 untracked=0`. The
two claims' after-values were measured at `e03f9e22` (C1) and `35a395a9` (C2), both ancestors of the
tip; the commits after them are evidence files and the ruling's cleanup, none touching a counter, a
ledger or a corpus record.

**Tool installs.** None this round (no `pacman` transaction; no `uv tool`/`npx` install).

**Open L0 question.** Appended at `.ufo/l0-questions.md` (`kotoba | round-87 | …`): the two remaining
corpus-integrity DRIFTs are structurally unrepairable by lane work (a non-author record's fleet-root
pointer and a correctly-described absent test-world commit); the round asks whether to authorise an
in-file absence ledger, an operator edit of the two lines, or a permanent-disclosure ruling.
