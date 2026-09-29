# Verdict — kengaku-shokunin

Stamp: 2026-09-29; landed child revision `f09ff1f` (`git -C kengaku-shokunin rev-parse --short HEAD` → `f09ff1f`). The child worktree was dirty during measurement (initially 1, later 2 untracked entries); tracked bytes equal `f09ff1f` (`git diff --quiet f09ff1f --` exit 0). All verdict cells below are for the landed commit, not the in-flight evidence directories.

## Rule-10 verdict

**NOT CONFORMANT — failed rules 8 and 10; rule 10 is the emitted-verdict obligation itself.** Rule 8 is a literal-text failure: one corpus occurrence of `op://` is present, even though it is only a quoted sweep pattern and not a resolvable vault path (`corpus/lessons/round-5-aggregator-audit.md:56`, `git grep -n 'op://' f09ff1f -- corpus/` → that one line). Under the round-9 amendment, this is **FAIL-literal / PASS-intent**, not a real secret-path finding. Rule 10 is not conformant because the prior round-6 verdict is stale and no round-9 per-repo verdict was present at the corpus-review cutoff; this file is the re-emission.

| Rule | Result | Command and observed result at landed `f09ff1f` |
|---|---|---|
| 1 source citation | PASS | `git show f09ff1f:corpus/README.md | grep -c '^| \`knowledge/'` → 22; `git ls-tree -r --name-only f09ff1f -- corpus/knowledge | wc -l` → 22. The source column is populated for indexed knowledge entries; spot sweep of all 22 file heads found source markers. |
| 2 lesson provenance | PASS | `git show f09ff1f:corpus/README.md | grep -c '^| \`lessons/'` → 13; `git ls-tree -r --name-only f09ff1f -- corpus/lessons | wc -l` → 13. Python sweep over all 13 lesson blobs found both `round` and evidence markers in every file. |
| 3 falsifiable/opinion | PASS (observed corpus practice) | Python sweep over all 35 knowledge/lesson blobs found explicit `opinion` markers in 4 where appropriate; remaining entries are evidence-backed. The committed `grader.py` and cited run bytes provide re-derivation for the numeric probe claims. |
| 4 count carries command | PASS-after-correction for the known round-6 defect; residual style debt noted | `git show f09ff1f:corpus/knowledge/bench-arena-round7-noise-n25.md | sed -n '13p;23,24p'` shows the corrected `0/17` denominator and the appended erratum. The prior `0/12` falsified count is no longer present in the landed blob. |
| 5 negative claim carries sweep | PASS | `git grep -n -E '0 hits|none found|absent|no source|NO' f09ff1f -- corpus/knowledge corpus/lessons` → claims are accompanied in their surrounding entries by grep/find/search commands; no unswept negative was found in the landed review corpus. |
| 6 quotes name location | PASS | `git grep -n -E 'frontmatter|body|header|script|installed skill|:line|lines?' f09ff1f -- corpus/knowledge corpus/lessons` → location-qualified quote conventions are present; the round-6 audit's sampled citation sweep passed this class. |
| 7 index row | PASS | `git show f09ff1f:corpus/README.md | grep -c '^| \`knowledge/'` = 22 and `git ls-tree ... corpus/knowledge | wc -l` = 22; corresponding lessons counts are 13 and 13. Both directions match for the committed tree. |
| 8 no credentials | **FAIL-literal / PASS-intent** | `git grep -n 'op://' f09ff1f -- corpus/` → exactly one hit: `corpus/lessons/round-5-aggregator-audit.md:56`, text is the quoted sweep command `grep -rn 'op://' corpus/ SKILL.md SHONEN.md LOG.md`, classified `schematic-placeholder`/sweep-pattern, not `real-vault-path`. Secret-class sweep `git grep -nE 'sk-|xox|bearer|password=|token=' f09ff1f -- corpus/` found no credential value. Literal CORPUS text still says every `op://` reference is out, so this is a rule-8 failure and an integrator/operator amendment candidate. |
| 9 append-only/no cross-lane rewrite | PASS for landed corpus | `git show f09ff1f:corpus/lessons/round-6-aggregator-audit.md | grep -n 'Post-audit re-measurement'` → appended section present; README contains the previously missing aggregator lesson rows. The historical LOG rewrite is documented as a defect, not a new corpus rewrite in this landed tree. |
| 10 per-round verdict | **FAIL at cutoff; re-emitted here** | `git show HEAD:.ufo/reports/AGGREGATE.md` (round-8 §13.7) says corpus verdicts were not re-emitted and §11.1's six verdicts were stale. This evidence file now emits the kengaku verdict with commands and landed revision. |

## Box 3

Round-8 box-3 was **firm/non-provisional** at `0c51208`: the committed cold run recorded `python3 grader.py --selftest` exit 0 with expected IDs and `python3 grader.py` exit 0, `CHECKS n=149 mismatches=0`, `VERDICT: PASS`; `SHONEN.md` had the four boxes and the text was landed. Re-executed against the landed `f09ff1f`: `python3 grader.py --selftest` → exit 0, S0–S6 ALL PASS (each mutation exit 1 plus expected finding-id); `python3 grader.py` → exit 0, `CHECKS n=280 mismatches=0 errata_pinned=1`, `VERDICT: PASS`; frozen `git archive f09ff1f | tar -x` run → same exit 0 / 280 / 0 / PASS. **Firm, not broken.**

## Gate conformance against PROTOCOL §Gate standard

- **Verdict: satisfied.** `SKILL.md:420-424` declares exits 0/1/2; `grader.py` returns 0 clean, 1 mismatch, 2 input error. The 2→could-not-evaluate class is semantically clear from the declared “missing/unreadable input” but is not literally named; minor registry wording gap.
- **Self-test: satisfied.** `SKILL.md:429-436` documents `python3 grader.py --selftest`, isolated temp copies, and exit plus expected finding-id checks. Re-run observed S0–S6 all pass.
- **Two evidences: satisfied.** Seven evidence inputs are committed and md5-pinned in `grader.py`; frozen archive run at `f09ff1f` reproduced exit 0, 280 checks, zero mismatches. The committed SKILL text records the 149→280 extension and expected all-match behavior.
- **Registry: partial.** `SKILL.md:405-449` is a prose gate section, not a schema row. Name, gate designation, entry/self-test commands, exits, and pinned evidence paths are present; explicit code→`clean|failed|could-not-evaluate`, explicit write scope, and explicit owner fields are absent.
- **Scope: satisfied.** `SKILL.md:407-408,429` says stdlib-only/no network/endpoint and temp-copy self-test; observed commands performed no writes to the child repo. The worktree-only directories were not used for the landed verdict.
- **Revision naming: partial.** The frozen evidence run is explicitly this stamp (`f09ff1f`), but the gate's stdout itself does not print the revision; callers must record it.

## Movement from round-6 ledger row

Round-6 row (`f147a27`) was **not conformant — rules 7, 9, 4; 5 majors / 12 defects**. At `f09ff1f`, rule 7 moved to PASS (22/22 knowledge and 13/13 lesson index rows); the rule-4 survivor (`0/12`) was corrected by an appended erratum to `0/17`; rule 9's historical rewrite is documented and the corpus lesson is append-only. The box-3 gate moved from no box/unchecked to `[x]` firm and now passes the expanded 280-check gate. Residual conformance debt is the literal rule-8 failure, the incomplete registry schema, and the newly owed rule-10 re-emission. This is lane-authored artifact review by an aggregator-dispatched seat; it is not non-author evidence for kengaku's own artifacts.

## Non-contract draft defect

The requested `.ufo/reports/round-11/kengaku-DRAFT.md` was previously observed by the round-8 corpus sweep as untracked, 15,922 bytes, with 40 `{{…}}` tokens, and absent from the contract path `round-11/kengaku.md` (ledger D-90). The current contract path now contains the landed `kengaku.md`; the draft is not in the current filesystem listing. The durable defect remains: an untracked/non-contract draft cannot satisfy report durability. **Owner: kengaku; severity 6.** Evidence: prior sweep quoted in `.ufo/reports/AGGREGATE.md` §13.2/D-90; current `ls -la .ufo/reports/round-11/` shows `kengaku.md` and no draft.
