# souji — round 22 report

## Work performed

**One declared claim: C1, calibration (lowest non-retired axis, score7).** Repair three inherited acceptance-predicate defects: decoded scalar type confusion, successful summary output accepted with nonempty stderr, and cache checks counted rather than identified. Covered malformed shapes must return a mismatch rather than raise. Preregistration: `29c1f7e8df849be8ee1b2d62d2351e17ec9d21a8`, base `41553adb139d06511dc386bb3ce4326aebfba675`, `.ufo/waves/round-22/preregistration.txt`. No second-axis or exploratory claim.

**Verdict boundary:** original214 C1 measurement is demonstrated:60/214→214/214, positives20/20 both. Final258 measurement and52 listed mutant kills are reproduced by compliant `RevProbe258`. **Strict full-adequacy admission is unproven:** the final13 literal-vector reviewer wrote forbidden scratch files and is Q26-VOID. Its PASS is retained but supplies no evidence. Outside closure must not turn it into admission. These are separate evidence sets, not a substitute for the frozen target.

- **Resume reconstruction.** SoujiR22 died on a provider cyber_policy refusal; SoujiR22R later died with the host SIGHUP at2026-10-21 13:10:51 -03. Neither was revived. This replacement did not retry refused work and met no policy refusal. Inherited pushed tip: `81a2646d53f914a226b6faa96e69ee5d01e8d348`; operator checkpoint `b912328d00d19f26918240710d0b5e0f334880ff` remains historical.
- **Inherited/re-verified:**66/66 W1 auditor input digests match; audit919 calls,1 major/3 minor. Specs, assignments, reports and measurements were checked against durable bytes. `census/round-22/resume-verification.json` records bindings and report digests; `terminal-accounting.json` records a fresh L1 original214 regrade. The original implementation, oracle and source rows were inherited; no runner source change was made by this replacement.
- **Corrected accounting:** W1 has63 reports, not64. `SoujiR22.DraftLesson` has no report and died after Codex capacity retries. Its empty terminal output is not a report. The old64-reported/59-usable statements are explicitly corrected, not silently reused (`corpus/lessons/round-22.md`, Explicit errata).
- **Accepted residual falsifiers:** `CritMutation` found unlisted wrong-value/case-row mutants surviving225; `CritMeasure` found environment dependence and nonidentical RecursionError message bytes. The first20 appended vectors/20 mutants yielded245 cases, then `CritAdequacy245` found14 additional unlisted survivors. Both FAIL reports and pre-repair counterexamples remain intact.
- **Bounded repair:**13 further literal witnesses (deep dictionary, swapped phases, missing fields, empty stdout, malformed cases, blank stderr) and14 mutants resolve the named counterexamples. Final oracle258, current258/258, base99/258; final probe52 kills/7 evidenced equivalents. Receipts: `census/round-22/oracle258-*.json`, `mutation-adequacy-oracle258.json`. The59-mutant red-before receipt on245 retains14 non-equivalent survivors (`mutation-adequacy-listed59-oracle245.json`).
- **Environment/provenance:** probe and stdin receipts now bind probe SHA256, interpreter, soft stack bytes and actual depth100000 decoder outcome. Stack size alone does not predict the outcome; environment size shifts the flip. RecursionError message bytes vary, while decisions/digests reproduce (`CritMeasure245`, S108). The deep-dictionary witness separately depends on Python recursionlimit1000, recorded in prose but not machine receipt metadata.
- **Frontier:** S104–S107 inherited with opened-source evidence; S108 is an opened, append-only correction superseding S107's unqualified local depth observation. Q53 supersedes Q52 by a new row. Mistakes R22-M10–M12 include incomplete mutant inventories, environment overclaims and the repeated Q26 breach. No knowledge/frontier promotion.
- **Final review scope violation:** `RevVectors258`'s two grading commands created FOUR forbidden paths: `/tmp/cur.json`, `/tmp/cur.err`, `/tmp/base.json`, `/tmp/base.err`; later deletion cures neither write. Its report understates this as two files. Exact scope-only transcript calls: `census/round-22/q26-final-seat-scratch-evidence.json`. All its review findings are void, not rerun or replaced. Original Counter2/11/16/18 scratch-write evidence and ReviewHistoricalScope's relative-write evidence also remain void.
- **Not reused/discarded as support:** all six Q26-void outputs, unfinished reportless seats' transcripts, author-chosen-list saturation, exact-byte baseline reproduction, and universal stack thresholds. Files are retained as history/scope evidence rather than erased.

### Swarm accounting

L1 holds the canonical planner seat (SoujiR22→SoujiR22R→SoujiR22-2); it is not an extra dispatched identity.

| call | seats | role mix | reports / reportless |
|---|---:|---|---|
| inherited W1 |64|24 scout,20 reviewer,11 critic,4 revenger,3 executor,1 scribe,1 connector|63 /1|
| inherited W2 |64|23 scout,20 reviewer,11 critic,4 mutation-tester,4 revenger,1 connector,1 scribe|38 /26|
| inherited ordinary residual |6|3 reviewer,3 critic|4 /2|
| new245 residual |4|2 reviewer,2 critic|4 /0|
| new258 bounded resolution |2|2 reviewer|2 /0 (one Q26-VOID)|

**140 dispatched identities =111 retained reports +29 reportless/dead identities.** The6 Q26-void reports are a subset of111, disjoint from the29 reportless/dead identities (overlap0); never subtract them twice. No new64-seat wave was attempted below remaining budget. No dead or void seat was replaced. Specs/assignments: `.ufo/waves/round-22/w1-dispatch.json`, `w2-final-dispatch.json`, `w1-assignments.json`, `w2-assignments.json`; terminal accounting: `census/round-22/terminal-accounting.json`.

Reportless/dead names:
- W1: `SoujiR22.DraftLesson`; last error: “Retry budget exhausted after 5 retries: Codex error event: Codex is at capacity, please try again later (code=turn_rate_limit_exceeded)”.
- W2: `SoujiR22.Attack04–06`, `Attack30–35`, `Attack37–49`, `Attack61–64` (26). No individual last error; parent died. L1 mechanical residual is not independent review.
- inherited residual: `SoujiR22R.ResidAdequacyA-17`, `SoujiR22R.ResidAdequacyC-17`; host SIGHUP, no reports. Their items were not reissued.

Cap refusals: inherited6-seat residual had16 whole-call refusals before attempt17 spawned; new2-seat call had6 whole-call refusals before unchanged attempt7 spawned. Refusals spent zero seats. One requested async backoff sleep also hit the job cap; backoff was awaited in eval instead. Dispatch log: `.ufo/waves/round-22/residual-dispatch-attempts.txt`. W1/W2 slot receipts and new4-seat residual receipt: `wave-slot-receipts.txt`; inherited W2 release is absent because its parent died. New residuals are ordinary ≤8-seat calls, not padded waves.

## Landed changes

Every item below ties to a LOG entry; only helper-confirmed pushed hashes are cited for this replacement.

- `473e98a498dbdb7315604251ab5a19a0823e7818` — LOG “round22 second replacement (SoujiR22-2): resolve residual falsifiers”:33 appended witnesses,34 added mutants, environment-bound receipts, inherited/new residual reports, evidence digest verification, Q53, S108, SCORECARD/SKILL updates and lesson errata.
- `fe7590b3010bed9b9b808b79c2bf2be1a18bce2a` — same LOG entry and “Terminal resolution review and admission boundary”: final reviews, Q26-VOID disposition, scratch-write evidence, original/final measurement separation, final accounting and source search-log correction. **Final lane landed hash; ahead=0, behind=0, tracked changes0.** Only operator-owned sweep and inherited r21 pycache remain untracked.
- Inherited `095af0e3aa1f03d8f7bf9ce9383a14656a86eb6c` and `81a2646d53f914a226b6faa96e69ee5d01e8d348` — LOG “round22 replacement L1 (SoujiR22R) continuation”: L1-regenerated214/225 receipts, original mutation probe, Q52/S107, inherited waves and failure carries.
- Earlier round22 implementation/docs: `29c1f7e`, `36c78ba`, `3223172`, `4f83fd2`; LOG “round22 result-contract calibration”. Checkpoint `b912328` is operator-authored historical evidence, not a fresh lane repair.

## Before → after measurements

| evidence set | base summarizer | changed summarizer | authority / boundary |
|---|---:|---:|---|
| same original214 oracle |60/214,5 exceptions|214/214,0 exceptions|L1 regrade in terminal-accounting.json; compliant CritMeasure/CritMeasure245 reproduce;20/20 positives both|
| final same258 oracle |99/258,8 exceptions|258/258,0 exceptions|oracle258 receipts; compliant RevProbe258 reproduces;151 false greens+8 exceptions,20/20 positives both|
| same59-mutant inventory, oracle245→258 |38 demonstrated kills;14 non-equivalent survivors|52 demonstrated kills;0 non-equivalent survivors|listed59-oracle245.json→mutation-adequacy-oracle258.json;7 evidenced equivalents unchanged, NOT credited as kills|

Base: `41553adb139d06511dc386bb3ce4326aebfba675`. Changed runner bytes: `4f83fd222ffbd8825340221a8c426550ef891191`, unchanged at final lane tip. Original214 oracle revision: `b912328d00d19f26918240710d0b5e0f334880ff`, SHA256 `292442a6ec078b7cc20526b4ba7ab1300eb08bc9cc4dbaf9894472120dcd0651`. Final258 oracle at `473e98a`, SHA256 `970b7362a0f0db9636e4141b12f798ca339b29fe90d23fadb4736b9634098027`. Historical225 numbers69/225→225/225 remain historical receipts at095af0e, independently reproduced by compliant critics, not relabelled as final measurements.

Counting commands from `/home/vgpnk/Projects/shokunin/souji-shokunin`:

```sh
python3 -B tests/fixtures/r22-result-oracle.py --runner census/round-21/run-acceptance.py
#258/258, exit0
 git show 41553adb139d06511dc386bb3ce4326aebfba675:census/round-21/run-acceptance.py | python3 -B census/round-22/mutation-adequacy.py --grade-stdin
#99/258, exit1
python3 -B census/round-22/mutation-adequacy.py
#52 killed /7 equivalent /0 disagreements, exit0
```

Historical oracle regrade uses the same stdin-grading command with `--oracle <file exported from b912328:tests/fixtures/r22-result-oracle.json>` before `--grade-stdin`; changed runner source can likewise be supplied on stdin. L1's freshly executed in-memory214 regrade and exact hashes are recorded in `terminal-accounting.json`. Historical245 mutant reproduction requires245 oracle bytes (prefix restored to its original closing brackets); compliant RevProbe258 checked its hash and all59 mutant rows.

Environment: Python3.14.8, soft stack8388608 bytes, recursionlimit1000, direct depth100000 decode raises. At other stack/environment/recursion settings, catches or iterative-walk mutants may survive and the probe turns RED; these are observations, not thresholds. Baseline receipt decision fields reproduce; RecursionError message stack-use bytes do not. No real18-step replay or acceptance main was executed this round.

Seven evidenced equivalents, with reasons (also in lesson's table):
- `nonexact-keyin-get`: no null expected leaves in the frozen subset counter; absent→None cannot match its non-null expected value.
- `failed-checks-to-eq`: decoded JSON equals expected[] exactly when it is an empty list; conditional on expected[].
- `names-len-constant`: named-set equality plus len(checks)==E implies constant-name countE.
- `phases-len-constant`: exact phase sequence plus len(case_rows)==E implies constant phase countE.
- `baseline-guard-pass`: pinned baseline-group step also enforces baseline_mismatch_count, so None==count already forces False; conditional on pinned step.
- `checks-len-drop`: named-set equality plus constant-name countE implies len(checks)==E.
- `caserows-len-drop`: exact phase sequence plus constant phase countE implies len(case_rows)==E.
These are bounded equivalence justifications (CritMutation/CritAdequacy245/RevMutants245), not kills or global proofs.

Numeric axis score remains7 (delta0, legacy-unmapped). No other axis claimed. Strict full-adequacy admission remains **unproven** because final13 literal-want review is Q26-VOID; neither the52 kills nor its retained PASS erase that gap.

Final committed gate command:

```sh
python3 -B tools/souji-landing-gate.py --root /home/vgpnk/Projects/shokunin/souji-shokunin --rev fe7590b3010bed9b9b808b79c2bf2be1a18bce2a --round 22 --base 41553adb139d06511dc386bb3ce4326aebfba675 --fleet-root /home/vgpnk/Projects/shokunin
```

Observed exit0:
`SUMMARY findings=0 checked_reg=50 checked_changed=3 checked_pins=13 checked_measured=3 checked_markers=13 status_lines=79 carry_heading=1 checked_reports=111`.
The gate checks carries/pointers, not strict admission. Prior committed snapshot: `census/round-22/landing-473e98a.json` (109 reports before final two reports).

## Sources & frontier

Command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin souji`.

Round-start recorded stdout (SoujiR22, exit0; recovered from original transcript at2026-10-21T13:49:25.220Z):

```text
souji	W04	S035 duplicate url git-scm.com/docs/git-repo across scopes
souji	W04	S036 duplicate url git-scm.com/docs/git across scopes
souji	W04	S038 duplicate url www.gnu.org/software/coreutils/manual/html_node/timeout-invocation.html across scopes
souji	W04	S049 duplicate url git-scm.com/docs/git across scopes
souji	W04	S057 duplicate url git-scm.com/docs/git-config across scopes
souji	W04	S058 duplicate url git-scm.com/docs/git-worktree across scopes
souji	W04	S059 duplicate url git-scm.com/docs/gitattributes across scopes
souji	W04	S063 duplicate url git-scm.com/docs/git-gc across scopes
souji	W04	S065 duplicate url www.gnu.org/software/bash/manual/html_node/The-Set-Builtin.html across scopes
souji	W04	S072 duplicate url www.gnu.org/software/bash/manual/html_node/The-Set-Builtin.html across scopes
souji	W04	S073 duplicate url man7.org/linux/man-pages/man2/kill.2.html across scopes
souji	W04	S075 duplicate url man7.org/linux/man-pages/man5/proc_pid_stat.5.html across scopes
souji	W04	S076 duplicate url man7.org/linux/man-pages/man5/proc_pid_exe.5.html across scopes
souji	W04	S077 duplicate url man7.org/linux/man-pages/man2/open.2.html across scopes
souji	W04	S086 duplicate url man7.org/linux/man-pages/man5/proc_pid_fd.5.html across scopes
souji	W04	S087 duplicate url man7.org/linux/man-pages/man5/proc_pid_wchan.5.html across scopes
souji	W04	S088 duplicate url man7.org/linux/man-pages/man5/proc_pid_status.5.html across scopes
souji	W04	S089 duplicate url git-scm.com/docs/git across scopes
souji	W04	S090 duplicate url git-scm.com/docs/git-filter-branch across scopes
souji	W04	S091 duplicate url git-scm.com/docs/git-rev-parse across scopes
souji	W04	S092 duplicate url git-scm.com/docs/git-for-each-ref across scopes
souji	W04	S093 duplicate url git-scm.com/docs/git-diff across scopes
souji	W04	S094 duplicate url www.gnu.org/software/coreutils/manual/html_node/timeout-invocation.html across scopes
souji	W04	S095 duplicate url man7.org/linux/man-pages/man5/proc_pid_fd.5.html across scopes
souji	W04	S096 duplicate url man7.org/linux/man-pages/man5/proc_pid_fd.5.html across scopes
souji	W04	S097 duplicate url git-scm.com/docs/git-filter-branch across scopes
souji	W04	S098 duplicate url www.gnu.org/software/coreutils/manual/html_node/timeout-invocation.html across scopes
souji	W04	S099 duplicate url git-scm.com/docs/git-rev-parse across scopes
souji	ok	/home/vgpnk/Projects/shokunin/souji-shokunin/corpus/SOURCES.md
```

Round-end observed stdout (this replacement, exit0; warnings only):

```text
souji	W04	S035 duplicate url git-scm.com/docs/git-repo across scopes
souji	W04	S036 duplicate url git-scm.com/docs/git across scopes
souji	W04	S038 duplicate url www.gnu.org/software/coreutils/manual/html_node/timeout-invocation.html across scopes
souji	W04	S049 duplicate url git-scm.com/docs/git across scopes
souji	W04	S057 duplicate url git-scm.com/docs/git-config across scopes
souji	W04	S058 duplicate url git-scm.com/docs/git-worktree across scopes
souji	W04	S059 duplicate url git-scm.com/docs/gitattributes across scopes
souji	W04	S063 duplicate url git-scm.com/docs/git-gc across scopes
souji	W04	S065 duplicate url www.gnu.org/software/bash/manual/html_node/The-Set-Builtin.html across scopes
souji	W04	S072 duplicate url www.gnu.org/software/bash/manual/html_node/The-Set-Builtin.html across scopes
souji	W04	S073 duplicate url man7.org/linux/man-pages/man2/kill.2.html across scopes
souji	W04	S075 duplicate url man7.org/linux/man-pages/man5/proc_pid_stat.5.html across scopes
souji	W04	S076 duplicate url man7.org/linux/man-pages/man5/proc_pid_exe.5.html across scopes
souji	W04	S077 duplicate url man7.org/linux/man-pages/man2/open.2.html across scopes
souji	W04	S086 duplicate url man7.org/linux/man-pages/man5/proc_pid_fd.5.html across scopes
souji	W04	S087 duplicate url man7.org/linux/man-pages/man5/proc_pid_wchan.5.html across scopes
souji	W04	S088 duplicate url man7.org/linux/man-pages/man5/proc_pid_status.5.html across scopes
souji	W04	S089 duplicate url git-scm.com/docs/git across scopes
souji	W04	S090 duplicate url git-scm.com/docs/git-filter-branch across scopes
souji	W04	S091 duplicate url git-scm.com/docs/git-rev-parse across scopes
souji	W04	S092 duplicate url git-scm.com/docs/git-for-each-ref across scopes
souji	W04	S093 duplicate url git-scm.com/docs/git-diff across scopes
souji	W04	S094 duplicate url www.gnu.org/software/coreutils/manual/html_node/timeout-invocation.html across scopes
souji	W04	S095 duplicate url man7.org/linux/man-pages/man5/proc_pid_fd.5.html across scopes
souji	W04	S096 duplicate url man7.org/linux/man-pages/man5/proc_pid_fd.5.html across scopes
souji	W04	S097 duplicate url git-scm.com/docs/git-filter-branch across scopes
souji	W04	S098 duplicate url www.gnu.org/software/coreutils/manual/html_node/timeout-invocation.html across scopes
souji	W04	S099 duplicate url git-scm.com/docs/git-rev-parse across scopes
souji	W04	S106 duplicate url docs.python.org/3/library/json.html across scopes
souji	W04	S108 duplicate url docs.python.org/3/builtins/exceptions.html across scopes
souji	ok	/home/vgpnk/Projects/shokunin/souji-shokunin/corpus/SOURCES.md
```

Counting command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh census --root /home/vgpnk/Projects/shokunin souji` (end exit0). Before histogram was remeasured from base `41553adb:corpus/SOURCES.md`; after is the CLI output:

| | rows | A/B/C | mined/queued/rejected |
|---|---:|---|---|
| before |103|99/3/1|81/15/7|
| after |108|104/3/1|85/15/8|

Rows added:5, all tierA. S104 JSON conversions, S105 bool equality, S106 retained strict-as-schema rejection, S107 RecursionError, S108 environment-qualified correction superseding S107. Existing rows' status/recheck/used-by cells unchanged; no teaches cell rewritten. C1 cites S104/S105; environment boundary cites opened S108. Gate URLs, dates and located ≤25-word quotes are in the lesson. S108's official page specifies exception semantics; reviewed local experiments, not that page, supply resource observations.

Frontier rows advanced0; new knowledge pathnames0. Mistakes R22-M6–M12 and Q53 tie red-before receipts and Q26 failure to prevention. Sources-row growth is not knowledge expansion. No outside admit/reject discernment spot-check is claimed.

## Trend verdicts

- **expansion: unchanged.** No new knowledge pathname/frontier promotion; S104–S108 ground calibration and an explicit correction.
- **quality: improved, bounded measured C1.** Original21460→214 and preserved20 positives; final258/52 listed kills reproduced by compliant RevProbe258. Full independently reviewed adequacy remains unproven; no void review supplies authority.
- **discernment: unchanged pending outside check.** Falsifiers were accepted and Q53 grounded in them, but lane-dispatched reviewers are still the lane. No outside admit-and-reject spot-check is fabricated; strict admission is left to closure with the void evidence excluded.

## SHONEN

- [~] SKILL.md has real decision tables/error patterns/checklists/cited sources: r22-result-oracle and r22-mutation-adequacy rows, Q51–Q53, S104–S108. No promotion verifier.
- [~] End-to-end domain task executed/logged: inherited operator-task evidence at LOG.md:362; no new cleanup authority or real replay claimed.
- [~] Executable instructions: committed oracle/probe commands above; historical source grades in memory. Full-adequacy limit explicitly recorded rather than hidden.
- [~] No cross-domain bleed/PROVINCE accurate: result calibration only; credential/exposure decisions belong to Kagi/operator, host liveness to Mori. No [x] without an outside verifier.

**Holds / no-harm scope:** certification OFF, K5 HELD; reap, NAMESPACE pin, historical exposure remain operator-owned. F5 scanner, frozen inventory and pinned S1 receipt are byte-identical to base (CritScope). Pinned S1/S2/S3 outputs regrade18/18 on both runners and carry empty stderr, not proof of a fresh replay. Future interpreter warning RED needs diagnosis, never suppression. Deep observed JSON can fail final serialization (fail-closed, partial output possible), outside arbitrary-depth replay totality. Cache positives depend on unchanged live gate digest `dd279ba95eebd13a6674f79983cec286fd856aa6d7e0719bf551ae0fc08939d6`, not hashed by the oracle.

**Scope cleanliness:** NOT process-scope-clean: inherited bare-root read R22-M4, original five Q26 voids and terminal scratch violation remain disclosed. No live /proc, credentials, private TSVs or operator-sweep contents were used. Operator-owned `census/operator-sweep-20261019/` was not committed/moved/deleted. Inherited `census/round-21/__pycache__/` was not committed. Own temporary builder/oracle exports and newly generated r22 bytecode were removed; no other lane's scratch touched.

**Misroot sweep:** unfiltered fleet `git status --porcelain` showed driver state/watchdog, other writers' L0/round28 paths and this report. No souji seat misroots needed copying/removal; unrelated files untouched.

**Stale-lane:** respawn-per-round; no other mission of this lane is open; r23 was not started.

**Tool installs:** none by this replacement or its seats; no package transaction. Predecessor report also records none.

**Prior lessons:** round-21-verifier-spotcheck.md and operator-*.md lessons absent (bounded glob); nothing unreflected was silently skipped.

**Open L0 questions:** none new. Inherited souji r17 jj-keep-refs/operator-sweep disposition, r18 reap/NAMESPACE and r20 F5 historical-exposure questions remain operator-owned. No campaign claim/state/manifest was mutated by this replacement.
