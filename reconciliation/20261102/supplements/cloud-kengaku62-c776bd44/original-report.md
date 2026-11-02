# Kengaku round62 — manual evaluation knowledge, partial claim outcome

## Work performed

Declared claims: **C1 / coverage**—repeated-trial evaluation estimands and
missing-outcome interpretation; **C2 / calibration**—round61 precision defects.
Lowest axis coverage remains capped7; TB2 remains17/89. **C1's revised manual
knowledge claim is independently admitted. C2 factual corrections verify, but
its original stronger durable-discharge claim is UNMET under canonical Q23.
No all-claims-pass or whole-round admission is asserted.**

- Source-grounded distinction between discovery pass@k, all-attempt pass^k,
  fixed-task macro aggregation, and sharp missing-outcome bounds:
  `corpus/knowledge/repeated-trial-estimands.md`, sources S226–S229.
- Ten independently frozen panels answered by hand before oracle release;
  reviewer agreed10/10. Evidence `corpus/evidence/round62/manual-answers.md`,
  `.ufo/waves/round-62/review/{REVIEW,manual-challenge,manual-oracle-released}.md`.
  Negative interpretations—metric swaps, plug-in powers, pooled task estimates,
  dropped unresolved outcomes and fabricated n<k scores—rejected with exact
  counterexamples. These are not executed mutants or model-performance results.
- Original executable proposal blocked by strict-envelope smoke:
  `bwrap --ro-bind / / --unshare-net --unshare-pid -- /bin/true` exited1 with
  `NETLINK_ROUTE socket: Operation not permitted`. Receipt
  `.ufo/waves/round-62/recon/envelope-smoke.txt`; proposal amended before manual
  scoring. No flags removed, alternate route, benchmark/provider execution,
  credentials/security change, paid call or real-target action.
- C2 re-read corrected two data rows plus separator, pointer98 versus byte226,
  and registry272→274 lines. It also rejected the old review's erroneous511
  diff-line total: the exact Git command returns546. Original records preserved.
  Evidence `recon/precision-before.txt` and `review/C2-independent.md` under
  `.ufo/waves/round-62/`; appended old lesson/claims errata; successor S230.
- Durable pending sidecar records R61-D1/D2/D3, not closed. Existing checker
  maps unknown checks to observed failure and cannot represent unexecuted/pending;
  no fake canonical check inserted and no gate altered. `corpus/defects-pending.jsonl`.
- All-axis/trend/source metadata completed. Independent final inspection:
  `.ufo/waves/round-62/review/FINAL-INTEGRATION.md`. No cross-domain ownership
  absorbed; operational provider routing and fleet policy remain outside lane.

## Landed changes

Lane branch `cloud-hyaku-20261102`; base
`c55a3f8868f352280538cf7d786135d34ac6542f`. Final author work HEAD:
**`5410cfb344a37a43eb76b712a345a38b19d72903`**, clean when report staged.
All commits use kengaku-shokunin / kengaku@shokunin.local, pathspec-limited.
LOG.md round62 records each work stage (proposal LOG was appended after pause/resume,
not falsely claimed present in initial proposal commit).

| commit | change tied to LOG.md round62 |
|---|---|
| `8eeeb5301b885204d89a273c06dcb5121456d4f4` | proposal, primary code captures, baseline/census/disk reconnaissance |
| `21d46b6c94cc4e0540e1b64a4c34219dcc35c7b7` | amended manual scope, frozen answers, source papers, draft knowledge, blocked-envelope and precision receipts |
| `bdb936eed65745dd8fd08fe64ff97aa60e92949a` | independently admitted entry+index+coverage map+SKILL/PROVINCE/SCORECARD, sources/lesson and append-only precision corrections, pre-returned reviewer evidence |
| `45a662f97ea4c253d52d395f9476d1dfbc49edde` | honest pending defect sidecar, explicit canonical-Q23 gap, read-only metadata receipts |
| `5410cfb344a37a43eb76b712a345a38b19d72903` | final independent integration report, commit-bound metadata and disk receipt |

No new executable capability or registry row. Existing gate code, canonical
`corpus/defects.jsonl` and SHONEN.md unchanged. Reviewer confirms all seven
old append-oriented document prefixes and218preexisting source rows unchanged.
No history rewrite, no old failed run erased. No round63 or promotion.

## Before → after measurements

**C1:** baseline `git cat-file -e
c55a3f8868f352280538cf7d786135d34ac6542f:corpus/knowledge/repeated-trial-estimands.md`
exits128 (absent); same path at content commit
`bdb936eed65745dd8fd08fe64ff97aa60e92949a` exits0. This measures discoverability,
not truth. Truth is supported by primary-source scrutiny and independent manual
answers: `grep -c '^| [0-9]' corpus/evidence/round62/manual-answers.md` gives10;
reviewer hand comparison agrees10/10, not an authored scoring counter.
Read-only receipt `.ufo/waves/round-62/recon/metadata-content-tip.txt` names
content commit and honestly records the receipt itself as untracked during capture.

**C2:** before false factual assertions remain in historical text; after append-only
corrections land at bdb936ee and independently verify. Commands:
`git diff --numstat f97e5b7b 215a7029 -- corpus/SOURCES.md` →274/272;
`git diff --numstat f97e5b7b b9920576 -- corpus/SOURCES.md` →2/0;
`git show REV:corpus/SOURCES.md` byte census →LF272/274/274, CR0/274/0.
Full hashes/digests in `recon/precision-before.txt`. No measured perpetual-check
before/after exists. Three pending records at45a662f9 are tracking, not closure.
C1 derivations do not depend on these errata; C2 reads old blobs/index independently
of C1. No revert-test execution is claimed; separation is artifact/source-based.

All-axis verdicts, bounded to touched content: depth9 held (sourced derivation),
coverage7 held (knowledge frontier, TB2 unchanged), operability10 historical score
not revalidated (no runtime improvement claim), freshness10 held (sources reopened),
calibration10 held (corrections/limits), adjacency9 held (no scope absorption),
novelty8 historical mapping held (canonical mathematics, not new phenomenon).
No observed touched-content harm; this is not a whole-repo executable revalidation.

## Sources & frontier

SOURCES218→223, new5tierA (two code, two canonical papers, one correction index).
TierA189→194, B24unchanged, C5unchanged; mined197→202, queued8unchanged,
rejected13unchanged. Exact commands/output `recon/source-counts.txt`; row command:
`git show REV:corpus/SOURCES.md | grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'`.
S226–S229 draft queued→mined and used-by —→knowledge+lesson; S230 queued→mined,
used-by —→lesson; recheck unchanged180d. All old rows, including S225, unchanged.
Every new row opened this round, anchored quote≤25words in lesson Gate, scoped tier,
and valid used-by path. Source rows alone are not expansion credit: one distinct
admitted knowledge entry and coverage-map row establish frontier progress.

Independent admit/reject spot-check by parent-appointed `/root/judge_kengaku_round62`
agrees on entry and rejected interpretations; source reviews returned before
admitting commit. Initial reviewer283-panel machine oracle lacked Q32 envelope,
was disclosed and excluded; only separately frozen manual oracle supports results.
Lesson mines number-drift, pointer confusion and host-envelope failure, using
existing QUALITY rules rather than inventing an untested new criterion.

Original census command at start/end:
`PATH=/workspace/scratch/e2fdad13233f/shokunin-training/tooling/bin:$PATH bash
/workspace/scratch/e2fdad13233f/shokunin-training/shokunin/scripts/sources-census.sh
validate /workspace/scratch/e2fdad13233f/shokunin-training/lanes/kengaku`.
Both exit0; existing duplicate-URL warnings retained, new S230 warning intentional.
Full recorded outputs follow.

Before:
```text
kengaku	W04	S040 duplicate url arxiv.org/abs/2301.09633 across scopes
kengaku	W04	S048 duplicate url aclanthology.org/2020.acl-main.442 across scopes
kengaku	W04	S057 duplicate url arxiv.org/abs/2405.11874 across scopes
kengaku	W04	S058 duplicate url github.com/UKGovernmentBEIS/inspect_ai/blob/63e45cc52d39b873b944124613da21fdad6f6dcc/src/inspect_ai/scorer/_pattern.py across scopes
kengaku	W04	S059 duplicate url www.rfc-editor.org/rfc/rfc8259 across scopes
kengaku	W04	S064 duplicate url spec.commonmark.org/0.31.2 across scopes
kengaku	W04	S065 duplicate url docs.python.org/3/library/json.html across scopes
kengaku	W04	S066 duplicate url doi.org/10.1017/S0950268810000385 across scopes
kengaku	W04	S067 duplicate url doi.org/10.1017/S0950268810000385 across scopes
kengaku	W04	S068 duplicate url raw.githubusercontent.com/web-arena-x/webarena/dce04686a56253aefba7b18a4fa0937cf1dc987b/config_files/test.raw.json across scopes
kengaku	W04	S069 duplicate url raw.githubusercontent.com/web-arena-x/webarena/dce04686a56253aefba7b18a4fa0937cf1dc987b/evaluation_harness/evaluators.py across scopes
kengaku	W04	S071 duplicate url docs.python.org/3/library/json.html across scopes
kengaku	W04	S075 duplicate url docs.python.org/3/library/json.html across scopes
kengaku	W04	S076 duplicate url docs.python.org/3/library/json.html across scopes
kengaku	W04	S100 duplicate url github.com/laude-institute/terminal-bench-2 across scopes
kengaku	W04	S213 duplicate url raw.githubusercontent.com/harbor-framework/terminal-bench-2/2fd12b88aafdd04a52c298e3940bcb189f9766d6/chess-best-move/tests/test_outputs.py across scopes
kengaku	W04	S214 duplicate url raw.githubusercontent.com/harbor-framework/terminal-bench-2/2fd12b88aafdd04a52c298e3940bcb189f9766d6/configure-git-webserver/tests/test_outputs.py across scopes
kengaku	W04	S215 duplicate url raw.githubusercontent.com/harbor-framework/terminal-bench-2/2fd12b88aafdd04a52c298e3940bcb189f9766d6/configure-git-webserver/tests/verify.sh across scopes
kengaku	W04	S216 duplicate url raw.githubusercontent.com/harbor-framework/terminal-bench-2/2fd12b88aafdd04a52c298e3940bcb189f9766d6/configure-git-webserver/instruction.md across scopes
kengaku	W04	S217 duplicate url raw.githubusercontent.com/harbor-framework/terminal-bench-2/2fd12b88aafdd04a52c298e3940bcb189f9766d6/feal-linear-cryptanalysis/environment/task-deps/gen.py across scopes
kengaku	W04	S222 duplicate url raw.githubusercontent.com/harbor-framework/terminal-bench-2/2fd12b88aafdd04a52c298e3940bcb189f9766d6/openssl-selfsigned-cert/instruction.md across scopes
kengaku	ok	/workspace/scratch/e2fdad13233f/shokunin-training/lanes/kengaku/corpus/SOURCES.md
RUNNER_EXIT=0
```
After:
```text
kengaku	W04	S040 duplicate url arxiv.org/abs/2301.09633 across scopes
kengaku	W04	S048 duplicate url aclanthology.org/2020.acl-main.442 across scopes
kengaku	W04	S057 duplicate url arxiv.org/abs/2405.11874 across scopes
kengaku	W04	S058 duplicate url github.com/UKGovernmentBEIS/inspect_ai/blob/63e45cc52d39b873b944124613da21fdad6f6dcc/src/inspect_ai/scorer/_pattern.py across scopes
kengaku	W04	S059 duplicate url www.rfc-editor.org/rfc/rfc8259 across scopes
kengaku	W04	S064 duplicate url spec.commonmark.org/0.31.2 across scopes
kengaku	W04	S065 duplicate url docs.python.org/3/library/json.html across scopes
kengaku	W04	S066 duplicate url doi.org/10.1017/S0950268810000385 across scopes
kengaku	W04	S067 duplicate url doi.org/10.1017/S0950268810000385 across scopes
kengaku	W04	S068 duplicate url raw.githubusercontent.com/web-arena-x/webarena/dce04686a56253aefba7b18a4fa0937cf1dc987b/config_files/test.raw.json across scopes
kengaku	W04	S069 duplicate url raw.githubusercontent.com/web-arena-x/webarena/dce04686a56253aefba7b18a4fa0937cf1dc987b/evaluation_harness/evaluators.py across scopes
kengaku	W04	S071 duplicate url docs.python.org/3/library/json.html across scopes
kengaku	W04	S075 duplicate url docs.python.org/3/library/json.html across scopes
kengaku	W04	S076 duplicate url docs.python.org/3/library/json.html across scopes
kengaku	W04	S100 duplicate url github.com/laude-institute/terminal-bench-2 across scopes
kengaku	W04	S213 duplicate url raw.githubusercontent.com/harbor-framework/terminal-bench-2/2fd12b88aafdd04a52c298e3940bcb189f9766d6/chess-best-move/tests/test_outputs.py across scopes
kengaku	W04	S214 duplicate url raw.githubusercontent.com/harbor-framework/terminal-bench-2/2fd12b88aafdd04a52c298e3940bcb189f9766d6/configure-git-webserver/tests/test_outputs.py across scopes
kengaku	W04	S215 duplicate url raw.githubusercontent.com/harbor-framework/terminal-bench-2/2fd12b88aafdd04a52c298e3940bcb189f9766d6/configure-git-webserver/tests/verify.sh across scopes
kengaku	W04	S216 duplicate url raw.githubusercontent.com/harbor-framework/terminal-bench-2/2fd12b88aafdd04a52c298e3940bcb189f9766d6/configure-git-webserver/instruction.md across scopes
kengaku	W04	S217 duplicate url raw.githubusercontent.com/harbor-framework/terminal-bench-2/2fd12b88aafdd04a52c298e3940bcb189f9766d6/feal-linear-cryptanalysis/environment/task-deps/gen.py across scopes
kengaku	W04	S222 duplicate url raw.githubusercontent.com/harbor-framework/terminal-bench-2/2fd12b88aafdd04a52c298e3940bcb189f9766d6/openssl-selfsigned-cert/instruction.md across scopes
kengaku	W04	S230 duplicate url encoding.spec.whatwg.org/index-windows-1252.txt across scopes
kengaku	ok	/workspace/scratch/e2fdad13233f/shokunin-training/lanes/kengaku/corpus/SOURCES.md
RUNNER_EXIT=0
```

Original diskguard check start/end exit0; `du -sk` round-local source evidence2912KiB,
wave evidence76KiB at final disk receipt (later final-review copy adds a fewKiB),
well below1GiB; no scratch clones or model artifacts. Existing host-deployment
sequential author/reviewer override used, not an invented eight-agent swarm,
Zcode/GLM/provider execution, or legacy watchdog route.

## Trend verdicts

- **expansion: improved** — independently admitted repeated-trial event/aggregation
  and missingness knowledge, not an eighteenth grader or source-row quota.
- **quality: improved** — supported exact errata and explicit estimand boundaries;
  old reviewer error corrected rather than blindly copied.
- **discernment: improved** — independent admit/reject agreement, frozen manual
  answers, blocked execution and incomplete durable discharge kept explicit.

These content judgments are independently supported, not all-claims-pass.
**Remaining limitation:** canonical Q23 requires red-at-entry/perpetual tip checks
and canonical defect entries. The approved pending sidecar is honest mitigation,
not conformance. C2 stronger durable discharge stays UNMET. Parent owns disposition.
Standing operator cap questions round25/33/51 and host/ledger questions round56
remain unanswered; no numeric cap lift inferred.

## SHONEN

- [~] Decision tables/error patterns/checklists/sources: SKILL.md new repeated-trial
  table and `corpus/knowledge/repeated-trial-estimands.md`; no promotion check claimed.
- [~] End-to-end bounded source-analysis task logged: LOG.md round62 and frozen
  manual answers; not runtime benchmark execution.
- [~] Written derivation instructions and examples independently read:
  `.ufo/waves/round-62/review/FINAL-INTEGRATION.md`; executable criterion not newly verified.
- [~] Province boundary retained: PROVINCE.md round62; parent-appointed reviewer
  found no touched-content scope harm, but no formal promotion-box signoff.
