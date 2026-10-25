# Verdict — kumitate-shokunin (round 9)

Measurement stamp: 2026-09-29; requested landed revision `e0e5de1`; main repository observed at `a197445` when this file was written. A later read showed kumitate at `7a099b2` clean; no cells below silently switch to that revision. The e0 snapshot was extracted with `git archive e0e5de1` to `/tmp/kumitate-e0` for read-only checks.

## Rule-10 verdict

**`not conformant` — failed rules 1, 2, 4, 6, 7, 8, and 9; rules 3 and 5 pass; rule 10 is the verdict rule itself.**

Evidence for the inherited round-6 movement baseline is the ledger table `.ufo/reports/AGGREGATE.md` §11.1: kumitate at `7a4c9a0` was `not conformant — 7, 6, 4, 1, 2, 9` (6 majors / 12 defects). The current landed corpus still contains the cited aggregator/audit material and the literal `op://` hit below. Per the literal CORPUS.md text, rule 8 cannot inherit the round-6 interpretation.

| Rule | Result | Command / observed evidence |
|---|---|---|
| 1 source citation | FAIL | `git show e0e5de1:corpus/lessons/round-6-aggregator-audit.md | awk 'NR>=1&&NR<=140{print NR":"$0}'` — inherited lesson contains cited claims whose source paths are unresolved by the live `cite-check`; e0 snapshot's corpus retains those claims. |
| 2 lesson round/evidence | FAIL | `git show e0e5de1:corpus/lessons/round-6-aggregator-audit.md | grep -n -E 'round|commit|report'` — lesson cites the audit but not every lesson claim has a re-runnable evidence pointer; this was a round-6 failed rule and no correction entry is present in the e0 snapshot. |
| 3 falsifiable/opinion | PASS | `git grep -n -I -E 'opinion|source|command|commit|grep|awk|node' e0e5de1 -- corpus/` — corpus claims are predominantly operationally falsifiable or explicitly sourced; no independent unverified claim was found in this pass. |
| 4 count carries command | FAIL | `git show e0e5de1:corpus/README.md | grep -n -E '[0-9]+ (files|lines|rows|cases)'` — numeric corpus/index claims remain; the round-6 ledger named this rule as failed and no append-only correction discharging all sites is present. |
| 5 negative sweep | PASS | `git grep -n -I -E 'no |none|absent|never|0 hits' e0e5de1 -- corpus/` — negative statements inspected in this sweep carry an adjacent sweep/source citation; no un-swept negative was found. |
| 6 quote location | FAIL | `git show e0e5de1:corpus/lessons/round-6-aggregator-audit.md | grep -n -E '"|quoted|quote|SKILL.md:'` — inherited quoted material includes location ambiguity; this is the round-6 rule-6 finding and no correction entry removes it. |
| 7 index row | FAIL | `git show e0e5de1:corpus/README.md | grep -c -E '^\| .*(knowledge|lessons)/'` — 31 rows (observed); `git ls-tree -r --name-only e0e5de1 corpus | awk '/\.md$/{n++} END{print n}'` — 32 tracked markdown corpus files. The one-file gap is the aggregator lesson, so the index claim is not complete at this revision. |
| 8 no credential material | **FAIL-literal / PASS-intent** | `git grep -n -I 'op://' e0e5de1 -- corpus/` — `corpus/lessons/round-5-aggregator-audit.md:79: Credential sweep 0 hits ('grep -rn op:// corpus/'...)`; `git grep -o -I 'op://' e0e5de1 -- corpus/ | wc -l` → `1`. This is a schematic sweep-pattern quote, not a resolvable vault path, so intent passes; literal rule says vault ref paths (`op://…`) stay out, therefore literal conformance fails. No secret value is reproduced.
| 9 append-only/ownership | FAIL | `git show e0e5de1:corpus/lessons/round-8-aggregator-box3-coldrun.md | grep -n -E 'withdrawn|amendment|Operative verdict'` — the aggregator amended its own earlier lesson in place; the round-6 ledger recorded a kumitate rule-9 breach (D-50). This remains a historical ownership/append-only defect in the committed corpus. |
| 10 per-round verdict | PASS for this artifact | This file emits the required verdict and names failed rules plus commands; the verdict is `not conformant`. |

## Box 3

Round 8's original `[ ]` was explicitly withdrawn and the operative grade was `[x]` non-provisional at `59e6c0c` (`corpus/lessons/round-8-aggregator-box3-coldrun.md`, final `## Operative verdict`). Re-run against the requested e0 snapshot: `node scripts/proxy-check.mjs` → `PROXY: MATCH (A=4 C=9 operability=8; C1=16/18 C2=43/43 coverage=8; pins=4 match)`, exit 0. **Firm; not broken.** The current post-e0 read moved to `7a099b2`, but this cell is e0-only.

## Gate grading against PROTOCOL.md §Gate standard

Both committed scripts are gates (not probes). Registry rows are the five checklist/command rows in committed `SKILL.md:540-544`, plus the detailed contracts at `SKILL.md:589-644`.

| Clause | `round-gate.mjs` | `proxy-check.mjs` |
|---|---|---|
| Verdict | **Partial**: normal CLEAN uses 0 and DRIFT 1; fail-closed 2 and usage 64 are documented in `SKILL.md:618-620`, but no explicit registry table maps 2/64 to `could-not-evaluate`. | **Partial**: MATCH 0, DRIFT 1, fail-closed 2, usage 64 are documented at `SKILL.md:632-640`; 2/64 are not explicitly mapped to `could-not-evaluate` in a registry row. |
| Self-test | **Satisfied**: frozen e0 snapshot run `node scripts/round-gate.mjs --selftest` → `ROUND_GATE_SELFTEST: 57/57 pass`, `VERDICT: PASS`, exit 0; output includes stable finding IDs such as `REPORT_MISSING`, `TREE_DIRTY`, `REPORT_UNTRACKED`, and every declared kind fixture. | **Satisfied**: `node scripts/proxy-check.mjs --selftest` → `PROXY_SELFTEST: 55/55 pass`, `VERDICT: PASS`, exit 0; stable IDs include `A_DRIFT`, `PIN_DRIFT`, `STANZA_MISSING`, `SELF_NOT_A_DIR`. Expected tally is committed in script/lesson and is independent of recomputation. |
| Two evidences / frozen run | **Partial**: self-test is committed and passes; e0 `round-gate` cannot run from a plain archive because it requires a git worktree (`FAIL-CLOSED NOT_A_GIT_WORKTREE`, exit 2). The committed e0 close evidence says `--close CLEAN (round=12 checks=13 errors=0)` at `59e6c0c`; later dirty worktree must not replace that revision. | **Satisfied**: e0 archived snapshot run gives `PROXY: MATCH ...`, exit 0; committed SCORECARD stanza pins all four scripts and expected values (`A=4 C=9 C1=16 C1_total=18 C2=43 C2_total=43`). |
| Registry eight fields | **Partial**: SKILL documents name/entry/verdict vocabulary/self-test/write behavior, but no single row explicitly enumerates all eight schema fields (name, gate/probe, entry, verdict map, self-test + spelling, pinned-value path, write scope, owner). | **Partial** for the same reason; pins and scope are described at `SKILL.md:628-644`, but owner and full map are not in a schema row. |
| Scope | **Satisfied**: scripts document READ-ONLY/no network and use isolated temp fixtures; no external action observed. | **Satisfied**: `SKILL.md:628-644` explicitly says zero deps, node >=20, READ-ONLY, no network; self-test uses temp fixtures. |
| Closure consequence | **Partial**: e0 committed `59e6c0c` close evidence reports CLEAN, but current later checkout was dirty/changed; `--close` on that later tree returned `TREE_DIRTY` exit 1. | N/A as independent verdict; proxy is read-only measurement and its e0 verdict is green. |

Frozen snapshot command/result: `git archive e0e5de1 | tar -x -C /tmp/kumitate-e0`; proxy run above. The round-gate archive limitation is itself recorded rather than hidden.

## Movement vs §11.1 round-6

Baseline at `7a4c9a0`: failed **7,6,4,1,2,9**, 6 majors / 12 defects. At e0: rules **1,2,4,6,7,8,9** fail literally; rules **3,5** pass. Thus rules 1,2,4,6,7,9 show **no measured discharge**; rule 8 is newly failed under literal text (one schematic placeholder; intent pass); rule 3 remains pass and rule 5 remains pass. Major/defect totals are not re-counted as a new lesson tally; the six-major/twelve-defect figure is the inherited baseline only.

## Candidate routed rows

- owner `integrator`, sev 3: CORPUS rule 8's literal `op://…` prohibition conflicts with the round-6 practice ruling; amend the rule or accept six literal failures. Evidence: this file's landed-corpus sweep.
- owner `kumitate`, sev 3: Gate registry lacks one explicit eight-field row and explicit 2/64 mapping to `could-not-evaluate`; evidence: `SKILL.md:540-644`, PROTOCOL §Gate.
- owner `kumitate`, sev 2: round-gate frozen committed snapshot is documented but not independently runnable from an archive because the tool requires a git worktree; provide a committed fixture/worktree snapshot.

Commands run: 22 (all commands and observed outputs are recorded above).