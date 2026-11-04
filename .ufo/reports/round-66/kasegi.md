# kasegi — round 66

## Work performed

**C1 only — depth:verifiability (lowest), sourced by S099:** restrict cat's non-final SIGPIPE exemption. **Finite predicate met; nominal score4→4, delta0 (R58).** No coverage or capability-acquisition claim. Final lane **51a5cb0d9ac8bf58f355c433a33a9ccc44fa34c2**; measured implementation **e8a865da49f3d1ff0e7222830006b3003d4577c0**.

- Pass each killed stage's decoded argv to its status rule. Multi-input/option-bearing cat SIGPIPE becomes stale; stdin/single-input positives remain green. Other heads retain the prior exemption. This deliberately refuses some successful truncated derives; it does **not** prove every newly stale input failed. Evidence: `SKILL.md:1224,1240`, `w1/ReviewCat.md` (43 independently predicted cases,18 intentional changes/25 controls).
- Commit no-work/forgery controls before freeze32a24002; final frozen counter prints **VERIFY12/0, exit0**. Evidence: `.ufo/waves/round-66/claims.json`, `controls/final-verification-r66.txt`. No postfreeze counter amendment.
- ONE v1 wave,9 seats:3 executor,1 reviewer,1 critic,1 mutation-tester,1 scout,1 connector,1 scribe; L1 planner. Assigned attack3/9 (completed2/8), one connector, no residual/replacement. WAVE-DONE preceded final measurement/report. Eight evidence reports; **one dead MutationCat**, no report/directory: `402 Upstream request failed: Insufficient account funds (type=server_error)`, observed by Main on opencode-go/deepseek-v4.1-flash. `w1-results.json` has null outputs/shared kernel-restart note; `seat-error-telemetry.json` supplies terminal accounting. L1's3-mutant battery is not dead-seat output.
- Curate S099, mine nine mistakes, append R92 and correct all six r65 routed record defects without rewriting history. Evidence: `corpus/lessons/round-66.md`, `corpus/QUALITY.md:498-502`. Reject connector compatibility-shim proposal; preserve clean callsite cutover. Source restoration/security boundaries remain unanswered.
- Real-domain **trial**, not new task credit: retained public curl CVE-2025-9086 package checker8/8 exit0; digest-defect control7/8, R-MANIFEST fail, exit1 (`controls/domain-trial-*`). No new discovery, live-target testing, submission or SHONEN box2 credit.

Wave/evidence paths abbreviated below are under `.ufo/waves/round-66/`. Scope adjudication: `w1/ScopeCat.md`; chousa research method, kengaku evaluation and kumitate orchestration remain adjacent, not absorbed. Its unsupported signature/package-list proposals were not adopted (`corpus/lessons/round-66.md` final adjudication).

## Landed changes

All hashes below are helper-reported landed commits, pushed to this lane. LOG ties are the actual Round66 bullets/lines, not invented labels.

| Commit | Change | LOG tie |
|---|---|---|
|1957407e22331c73aafe944da2b37c182f13583a|Measured baseline, census, validated handoff|LOG.md:2682-2684|
|6102c0e9fbfc9443a8817d9454d4d8222a2b56ed|S099/lesson/R92, candidate/control artifacts|LOG.md:2685-2686|
|d94a9ecdf3295f5ce8f5955e2c8696365c102fa8|Prefreeze resolver correction, failed trials retained|LOG.md:2687|
|0d5aef2f40dce3129e91419c34b6c46087089b94|Exact no-work/stand-in/forgery measurements|LOG.md:2688|
|32a24002c252ec052aa535c6893d53da3004e14f|Immutable C1 freeze after controls|LOG.md:2689|
|e8a865da49f3d1ff0e7222830006b3003d4577c0|Frozen production repair and live registry amendment|LOG.md:2690|
|51a5cb0d9ac8bf58f355c433a33a9ccc44fa34c2|Final measurements, wave settlement, documentation and corrected seat receipts|LOG.md:2691-2694|

The final commit adds documentation/receipts after the measured implementation; gate, counter, collector and pins are unchanged. `jj-lane.sh state`: local=remote=51a5cb0d…, ahead0/behind0, tracked0/untracked0. Required `git ls-remote origin refs/heads/master` printed **51a5cb0d9ac8bf58f355c433a33a9ccc44fa34c2**. Report lands last.

## Before → after measurements

C1 predicate: **VERIFY measurements=12 failures=0 and process exit0 on the exact committed-input counter.** Counter SHA256 `5962b7d6f7aa05d118a86387ffb527f1c5dfb6b3e7b18483d99fa7eeb1adad61`; candidate `51f299af…`, collector `d788bbc1…`, persisted pins `controls/driver-pins.json`.

```sh
python3 -B .ufo/waves/round-66/w1/ExecCatDriver/verify.py \
  --revision e8a865da49f3d1ff0e7222830006b3003d4577c0 \
  --controls-revision 0d5aef2f40dce3129e91419c34b6c46087089b94 \
  --cat-mutbat .ufo/waves/round-66/cat-mutbat.py \
  --work /fast/scratch/hyaku/kasegi-r66/L1/replay --final
```

Before actually used REV=b6db9e818d322726e39cb441f2179d34d4170275, controls=d94a9ecd…, omitted `--final`; exact argv/rc is in `controls/driver-base-final-prefreeze.txt`. Controls0d5aef2f adds receipts with identical counter/probe/pin bytes, not a changed instrument.

| Measure | Before | After |
|---|---|---|
|Complete committed-input counter|12 measurements/3 failures, exit1|12/0, exit0 at e8a865da|
|Public collector, candidate expectations|8 probes/3 mismatches (P1/P2/P8)|8/0; exact signal13 stale; single/stdin/grep/small-twin positives hold|
|Selftest|63/0|67/0|
|Retained mutation / new cat mutation|5/5; cat limb absent (setup2, not a semantic kill)|5/5;3/3, equivalent held, invalid rejected|
|Actual production ledger|35/35|35/35; red wrong-want still stale|
|Full-driver ID forgery control|12/6, exit1, before freeze|No changed target or late reclassification|

Raw child commands/outputs/rc: `controls/driver-*-final-prefreeze-children/`, `controls/final-children/`. The first construction driver had a rev:path peel defect (base12/4, stand-in12/1); those failed receipts remain, and the corrected driver/pair were committed **before** freeze. Final finite critic controls: ID/path/text/always-green/always-stale all fail, real candidate8/0 (`w1/CriticCat/opaque-final-summary.json`). This is not arbitrary semantic-emulator resistance.

No numerical score gain: `controls/score-gap-after.txt` reports82 rechecks,22 lost-base-gated,0 broken; actual citation-source restoration remains absent. Coverage8/density9 held; density not remeasured. Admission/conservative-refusal judgment belongs to the outside closure, not this lane.

## Sources & frontier

**Registry98→99:** S099 only, own-work/A/mined; A88→89, B5/C5 unchanged, mined80→81/rejected18 unchanged. Zero pre-existing row changes, no status/recheck/used-by transitions. Gate's dated located quotes ground S099 (`corpus/lessons/round-66.md`). No knowledge/frontier row advanced or capability acquired.

Counting command (executed literally as below; output/rc also `controls/source-counts.txt`):

```sh
python3 -B -c 'import collections,re,subprocess,pathlib
lane='"'"'/home/vgpnk/Projects/shokunin/kasegi-shokunin'"'"'
base='"'"'b6db9e818d322726e39cb441f2179d34d4170275'"'"'
def rows(t):
 return {c[0]:c for line in t.splitlines() if re.match(r'"'"'^ {0,3}\|\s*S[0-9]{3,}\s*\|'"'"',line) for c in [[x.strip() for x in line.strip().strip('"'"'|'"'"').split('"'"'|'"'"')]]}
a=rows(subprocess.check_output(['"'"'git'"'"','"'"'-C'"'"',lane,'"'"'show'"'"',base+'"'"':corpus/SOURCES.md'"'"'],text=True)); b=rows(pathlib.Path(lane+'"'"'/corpus/SOURCES.md'"'"').read_text())
for name,d in [('"'"'before'"'"',a),('"'"'after'"'"',b)]:
 print(name,'"'"'rows='"'"'+str(len(d)),'"'"'tiers='"'"'+str(dict(sorted(collections.Counter(v[3] for v in d.values()).items()))),'"'"'status='"'"'+str(dict(sorted(collections.Counter(v[7] for v in d.values()).items()))))
print('"'"'added='"'"'+'"'"','"'"'.join(sorted(b.keys()-a.keys())),'"'"'old_rows_changed='"'"'+str(sum(a[k]!=b.get(k) for k in a)))
'
```

```text
before rows=98 tiers={'A': 88, 'B': 5, 'C': 5} status={'mined': 80, 'rejected': 18}
after rows=99 tiers={'A': 89, 'B': 5, 'C': 5} status={'mined': 81, 'rejected': 18}
added=S099 old_rows_changed=0
exit=0
```

Census command, at start and end:

```sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kasegi
```

Before output (`controls/census-before.txt`):
```text
kasegi	W04	S028 duplicate url docs.hackerone.com/en/articles/8494502-safe-harbor-overview-faq across scopes
kasegi	W04	S029 duplicate url eur-lex.europa.eu/eli/reg/2024/2847/oj/eng across scopes
kasegi	W04	S072 duplicate url bughunters.google.com/about/rules/about-this-section across scopes
kasegi	W04	S076 duplicate url docs.github.com/en/code-security/concepts/vulnerability-reporting-and-management/repository-security-advisories across scopes
kasegi	W04	S080 duplicate url ossf.github.io/osv-schema across scopes
kasegi	W04	S085 duplicate url csrc.nist.gov/schema/nvd/api/2.0/cve_api_json_2.0.schema across scopes
kasegi	ok	/home/vgpnk/Projects/shokunin/kasegi-shokunin/corpus/SOURCES.md
exit=0
```
After output (`controls/census-after.txt`; same six inherited warnings):
```text
kasegi	W04	S028 duplicate url docs.hackerone.com/en/articles/8494502-safe-harbor-overview-faq across scopes
kasegi	W04	S029 duplicate url eur-lex.europa.eu/eli/reg/2024/2847/oj/eng across scopes
kasegi	W04	S072 duplicate url bughunters.google.com/about/rules/about-this-section across scopes
kasegi	W04	S076 duplicate url docs.github.com/en/code-security/concepts/vulnerability-reporting-and-management/repository-security-advisories across scopes
kasegi	W04	S080 duplicate url ossf.github.io/osv-schema across scopes
kasegi	W04	S085 duplicate url csrc.nist.gov/schema/nvd/api/2.0/cve_api_json_2.0.schema across scopes
kasegi	ok	/home/vgpnk/Projects/shokunin/kasegi-shokunin/corpus/SOURCES.md
exit=0
```

**Assimilation: none.** Read-only merge/kasegi package does not ground the local diagnostic. Unadopted package S099 is a different CNNVD document, not a reserved registry id; future adoption must re-id by document. Latest considerthese/2026-10-26.md read; proposal2 remains partially landed/domain-task-open, no proposal declared implemented. No campaign payload adopted.

## Trend verdicts

- **Expansion unchanged:** no new knowledge/frontier/repertoire; S099 is curation, not expansion.
- **Quality unchanged:** no knowledge entry superseded/re-admitted; instrument correctness moved only on the stated finite cases. Conservative refusals and broad residuals disclosed above.
- **Discernment improved:** outside r65 record disagreements became lesson/R92; actual prefreeze ID/path oracle and resolver defeats changed controls rather than being hidden. See lesson Mistakes and final adjudication. Outside admission/promotion remains owed.

Stale-lane: this round alone, progressing since launch17:04:56-03 through lane-authored commits; no other kasegi mission open. Open L0: existing r15 source/province, r57 R67/R69, r59/r60 security-boundary questions; no new question or assumed answer. Misroot sweep exit0 (`controls/fleet-misroot-sweep.txt`): operator/sibling/unknown pre-existing files untouched, no owned fleet misroot. Scratch `/fast/scratch/hyaku/kasegi-r66` removed after landing; command printed `kasegi-r66 scratch removed`. No tools installed/updated; pacman untouched. No inherited lane work at start; final lane clean.

## SHONEN

- [~] Decision tables/error patterns/checklists: `SKILL.md`, updated gate registry1224; author assertion, not promotion verification.
- [ ] New end-to-end domain task: none; retained disclosed-package trial is not proposal2 or box2 completion (`controls/domain-trial-scope.txt`).
- [~] Executable instructions: exact committed counter12/0, with22 lost-base-gated rechecks explicitly retained (`controls/final-verification-r66.txt`, `controls/score-gap-after.txt`).
- [~] Scope: PROVINCE unchanged, connector adjacency screen; no live-target testing or sibling ownership absorbed (`w1/ScopeCat.md`, lesson adjudication).
