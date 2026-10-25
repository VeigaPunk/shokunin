# Kasegi corpus verdict — round 9

Measurement stamp: 2026-09-28T21:49:15-03:00; main HEAD `62fdfbe`; landed kasegi revision `b7180b0` (`git show b7180b0` committed 2026-09-28T20:48:33-03:00). Immediate status command: `git -C kasegi-shokunin status --porcelain | wc -l` → `6`; therefore all verdict cells below grade the archived landed revision, and current worktree changes are **provisional**. Archive command: `git -C kasegi-shokunin archive b7180b0 | tar -x -C /tmp/kasegi-r9-kasegi`.

## Rule-10 verdict

| Rule | Verdict at `b7180b0` | Command and observed result |
|---|---|---|
| 1 | FAIL | `python3 /tmp/kasegi-r9-resolve.py /tmp/kasegi-r9-kasegi head` → 782 distinct / 1001 occurrences; 740 distinct path citations unresolvable, including 658 bounty-relative and 80 bounty-absolute. `~/Projects/bounties` independently: `ls -d /home/vgpnk/Projects/bounties` → exit 2, no such file. |
| 2 | PASS | `find /tmp/kasegi-r9-kasegi/corpus/lessons -name '*.md' -print0 | xargs -0 grep -L 'round-[0-9]\|Round: [0-9]'` → no output; lessons contain round identity and evidence references. |
| 3 | FAIL | `grep -RniE '592|1088|486|280|7227' /tmp/kasegi-r9-kasegi/corpus` → numerous claims whose sole live source was the vanished tree; no loss/anchor qualification exists in landed HEAD. They are not currently falsifiable. |
| 4 | FAIL | `git show b7180b0:corpus/knowledge/mission-ledger.md | grep -nE '[0-9]+ — '` → no output; `git show b7180b0:SCORECARD.md | grep -n '19.*knowledge'` → uncommanded count `19`. |
| 5 | FAIL | `git show b7180b0:corpus/knowledge/evidence-dir.md | grep -n -C1 george` → negative claim “Zero claims dirs reference it” has no sweep in the entry. |
| 6 | PASS | `git show b7180b0:corpus/knowledge/triage-thresholds.md | grep -cE ':[0-9]+'` → 23; sampled citations identify source file/line or script location. |
| 7 | PASS (minor disclosed gap) | `comm -23 <(git ls-tree -r --name-only b7180b0 corpus/knowledge | sed 's#corpus/##' | sort) <(git show b7180b0:corpus/README.md | grep -o 'knowledge/[A-Za-z0-9_-]*\.md' | sed 's#knowledge/##' | sort -u)` → no output; `README.md` now has `program-quirks.md`. The lessons range still spans a missing round-2 file, but the known-gaps paragraph explicitly discloses that absence. |
| 8 | FAIL-literal / PASS-intent | `git grep -n 'op://' b7180b0 -- corpus/` → 2 hits: `corpus/lessons/round-5-aggregator-audit.md:50` and `corpus/lessons/round-6-aggregator-audit.md:31`; both are sweep-description prose, not real vault paths. `git grep -E -i -n 'sk-|ghp_|github_pat_|xox|AKIA|BEGIN .*PRIVATE KEY' b7180b0 -- corpus/` → no hits. Literal CORPUS text bans every `op://` reference, so this is FAIL-literal despite PASS-intent; this interpretation is a routed operator/integrator defect. |
| 9 | FAIL (contested) | `git show b7180b0:corpus/README.md | grep -n 'repaired in place'` → r12 repairs explicitly described as in-place; `git log --oneline b7180b0 -- corpus/knowledge/` → repeated repair commits. This conflicts with “corrections are new entries”; lesson append-only practice remains intact. |
| 10 | PASS for this review; previously owed | `sed -n '1428,1455p' .ufo/reports/AGGREGATE.md` → residual review debt and no per-repo verdict table; this file emits the required per-repo verdict now. |

**Overall: not conformant.** Failed rules: 1, 3, 4, 5, 8 (literal), 9 (contested). Rule 10 is discharged by this evidence/lesson pair.

## Blast radius and PROVINCE contract

Extraction command (stdlib-only, deterministic, run twice): `python3 /tmp/kasegi-r9-resolve.py /tmp/kasegi-r9-kasegi head > /tmp/kasegi-r9-head-run1.txt; python3 /tmp/kasegi-r9-resolve.py /tmp/kasegi-r9-kasegi head > /tmp/kasegi-r9-head-run2.txt; diff /tmp/kasegi-r9-head-run1.txt /tmp/kasegi-r9-head-run2.txt` → `DETERMINISTIC`; totals `782 distinct`, `1001 occurrences`, `740 unresolvable`; input md5 `e67165be25c0bfd87a1a1deb5fb79b19`. Scope counts: `SKILL.md` 173 unresolvable distinct; `PROVINCE.md` 1; `corpus/**` 566 (README 47 + knowledge/lessons remainder). This is strict as-written resolvability; it does not silently substitute the frozen `the-bounty-hunter` mirror.

`git show b7180b0:PROVINCE.md` says domain surfaces “scopes ~/Projects/bounties”; `git -C kasegi-shokunin status --short -- PROVINCE.md` → empty; `git log -1 --format='%h %cI' b7180b0` → `b7180b0 2026-09-28T20:48:33-03:00`, before the disappearance window. Thus PROVINCE was not corrected per PROTOCOL §File contract. A corpus citing an absent source cannot pass rules 1/3/5 on a strict current-evidence reading: path citations do not resolve (1), claims are not falsifiable now (3), and negative sweeps cannot be re-run against the source (5). A contemporaneous command-output citation can preserve historical provenance only if it carries an as-of stamp and loss/anchor qualification; landed HEAD does not.

## Box-3 re-run at landed `b7180b0`

`ls -d /home/vgpnk/Projects/bounties/claims` → exit 2, absent. Consequently the live r8 command set cannot be rerun. The r8 provisional status remains **still provisional / could-not-evaluate**, not firm or broken: the evidence tree is gone. The committed text has changed since the r8 worktree reading: `git show b7180b0:SKILL.md | grep -nE 'exit 0 always|live exit 1|20/280|claim-anatomy-sample|program-quirks'` → `:94 program-quirks`, `:153 live exit 1`, `:383 claim-anatomy-sample`, `:392 20/280`, `:657 exit 0 always...`.

Mirror-only branch check (not a substitute for the lost live revision): copying `~/Projects/the-bounty-hunter/ops/ev-report.mjs` to `/tmp/ev-report-r9.mjs`, then `node /tmp/ev-report-r9.mjs` → exit 2, usage; `node /tmp/ev-report-r9.mjs nonexistent-program` → exit 2, missing file. This firms only the frozen mirror's behavior; it cannot firm the lost Sep-28 live tree. The committed 30/280 sampling claim is no longer worktree-only, but remains provisional as a measurement because its 280-package evidence tree is absent.

Per r8 claim: executable command set (rows 4–16) = **still provisional/could-not-evaluate**; documented `ev-report` exit contract = **break remains historically evidenced, live re-run impossible; mirror contradicts the historical live result**; `check-freshness` exit-1 claim = **still provisional/could-not-evaluate** (running it would mutate telemetry and its source tree is gone); wrong-path `program-quirks` cite = **firm break** (the cited bounties base is absent).

## Movement from ledger §11.1 round-6 row

Baseline: `not conformant — 4,5,7,9(contested),1/6; 7 majors / 11 defects` at `fb9ac8e`. Rule 1/6: **improved in corpus text through r12–r14 citation repairs, then regressed in current resolvability**: 740 distinct path citations are now unresolvable; net current status FAIL. Rule 4: **improved** (archive count corrected to 20 and SCORECARD now says 9→9), but mission-ledger count tables still lack commanded form, so remains FAIL. Rule 5: **unchanged/fail**: `evidence-dir.md` still has the un-swept george negative. Rule 7: **improved**: README now includes `program-quirks.md`; disclosed round-2 gap remains minor. Rule 9: **unchanged contested/fail**: corpus records in-place repairs, contrary to append-only correction wording. Rule 8 is a **new literal failure** (2 schematic `op://` hits), not part of the round-6 failed-rule list. Defect count/majority is not recomputable after source-tree loss; no false replacement number is asserted.

## Worktree-only provisional delta

Current dirty entries (`git status --porcelain | wc -l` → 6): `SKILL.md`, five corpus knowledge files/entries including untracked `source-tree-loss-2026-09-28.md` (the exact porcelain listing is the re-runnable source). The r15 loss record and re-anchoring repairs are not part of `b7180b0`; they may improve rules 1/3/5/6 if landed, but are provisional and not graded as landed evidence.
Post-write drift note: final verification `git -C kasegi-shokunin rev-parse --short HEAD` → `b7180b0` (unchanged), while `git -C kasegi-shokunin status --porcelain | wc -l` → `7`; the landed revision did not move, and all cells above remain measurements of `b7180b0`. The initial pre-measurement dirty count was 6 as stated.
