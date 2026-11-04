# souji round 58 — bounded fresh start

## Work performed

Declared **C1 calibration** (lowest owned score, 7): correct two r57 SCORECARD assessment discrepancies, measured mismatches **2→0**. Declared **C2 operability** (8): five receipt-interface refusals plus three preserved honest receipts, **3/8→8/8**. Distinct files/surfaces; no exploratory claim or Markdown-parser repair. Both finite predicates verify; independent non-author closure decides admission. Scores remain 7/8/8 (no invented scale mapping).

- Read the last three rejected closures and spot-checks (r55/r56/r57), preserving their rejected-harmed history; authorized fresh start does not retroactively admit them. Frozen claim/control: `census/round-58/preregistration.txt`, commit `e7f64f30324e8ddb3f2266302daa9066054cdbb3`.
- C1 appends evidence-derived corrections: 34 identical rows, not 33; count each matrix separately (10,8), not the combined awk total 18. `SCORECARD.md:1462`, `census/round-58/c1-final.txt`; deleting either note fails its independent fixture (`census/round-58/wave/w1/S58Executor5/results.json`).
- C2 confines static absolute/traversal/intermediate-symlink escapes before content reads, rejects raw tag-object OIDs, and refuses conflicting standalone revision headers. Current gate `census/round-58/c2-gate.py`, SHA256 `56f2a31163035726f1190db3e6b827fc121602377e187d16a54a6ae8f15af543`; independent frozen oracle `census/round-58/c2-acceptance.py`.
- One validated v1 wave **12 seats**: scout1, connector1, executor3, scribe1, reviewer2, critic1, mutation-tester1, sentinel1, revenger1. L1 holds planner (validator exception). Attack roles reviewer/critic/mutation-tester = **4/12**, connector1; residual0, round total12, dead0 (twelve settled outputs). Main delivered **WAVE-DONE before this report**. Dispatch/results and all reports committed under `census/round-58/wave/`; `census/round-58/wave-SHA256SUMS` pins 154 copied artifacts.
- Sentinel caught proposed caller-subtree deletion and arbitrary expected-output overwrite; both removed before landing. Reviewer/critic/mutator rescored final digest. Seven listed mutants killed, not exhaustive adequacy: `census/round-58/wave/w1/S58Mutationtester10.md`; ownership proof/limits `census/round-58/wave/w1/S58Sentinel11.md`.
- Connector inspected sibling mechanisms only; no sibling execution/edits or authority absorption. `census/round-58/wave/w1/S58Connector2.md`. All installs/updates: **none**. Host observed Git2.56.0, Python3.14.8, Node24.21.0, jj0.45.1.
- Stale-lane: respawn-per-round; no other souji mission open. Start tree clean at `83d3813257648e99fb4ab2ddef217124f39cf324`; no inherited r58 attempt. Required fleet misroot sweep found operator `.scratch` state and preexisting 24-byte `after` (2026-11-03 20:05, already in r57 closure); untouched. Owned round scratch removed after evidence landing.

## Landed changes

Every row ties to `LOG.md` **Round 58**, lines2775–2786, and the pushed lane commit named below.

| Landed commit | Change / LOG tie |
|---|---|
| `e7f64f30324e8ddb3f2266302daa9066054cdbb3` | Predicate freeze, C1 instrument/control, source-census start; LOG2777 |
| `dccdc469f4c2e0415e1a1dcc317364e1b4d3191e` | Two append-only SCORECARD corrections; LOG2778/2780 |
| `1880343ed04337379c5478f91408c30c8fbd4b77` | Independent C2 acceptance and unchanged-gate before control; LOG2781 |
| `b1c2bb9f762baa8142eaeaa5d4f472765b09dd32` | S284/S285, sourced lesson/README, C1 bound receipts/table; LOG2782/2783 |
| `5e4b8f14572d7051537b167dece4541bed7d2bab` | Final reviewed gate/expected table, SKILL current interface, Q117/Q118, twelve-seat evidence; LOG2784/2785 |
| `81d556e7f94569ae5f24b38458f157b153188191` | Integrated measurement receipts, end census, SCORECARD measurements/r59 plan, lesson close-out; LOG2786 |

All lane landings through `jj-lane.sh --as souji`. Final required remote proof: `git -C /home/vgpnk/Projects/shokunin/souji-shokunin ls-remote origin refs/heads/master` printed `81d556e7f94569ae5f24b38458f157b153188191 refs/heads/master`.

## Before → after measurements

Measured code revision **`5e4b8f14572d7051537b167dece4541bed7d2bab`**; final lane commit adds evidence/bookkeeping only.

| Claim | Counting command | Before/control | After |
|---|---|---|---|
| C1 calibration | `python3 -B census/round-58/c1-counter.py --root LANE --rev FULL40` | input `83d3813257648e99fb4ab2ddef217124f39cf324`: `assertions=2 mismatches=2 carry_identical=34 exit_zero=10,8`, EXIT1; bound receipt `census/round-58/c1-control-binding.txt` | input `5e4b8f14572d7051537b167dece4541bed7d2bab`: same counts, `mismatches=0`, EXIT0; `census/round-58/c1-final.txt` |
| C2 operability | `python3 -B census/round-58/c2-acceptance.py --tool census/round-58/c2-gate.py --root LANE --work DIR --selftest` (before: select `census/round-57/c2-counter.py`) | five required refusals incorrectly clean, three honest clean = **3/8**; `census/round-58/before-arm.json`, oracle frozen `1880343ed04337379c5478f91408c30c8fbd4b77` | five named refusals + three honest clean = **8/8**, EXIT0; always-clean and always-refuse stubs rejected; `census/round-58/c2-after.json` binds revision/oracle/argv |

Gate selftest: `python3 -B census/round-58/c2-gate.py --selftest --work DIR` → **17/17**, exact case set, rc/full normalized findings, EXIT0 (`census/round-58/c2-selftest.txt`). Seat idempotence and deleted-note controls retained under committed wave evidence; L1 exercised integrated acceptance/selftest/C1/end census once after all seats settled. No repository-wide build/lint/legacy-suite pass inferred.

Limits: C1 is a two-site declared-evidence comparison, not omission discovery, fixture-identity enforcement or Markdown visibility; it has no self-invocation certification (external fixture provides discrimination). C2 hash normalization is not exact digest-value validation, pathname checks are not atomic descriptor confinement, manifest/regular-file reads remain unbounded legacy hazards, subprocess timeout does not prove descendant cleanup. Header precedence preserves SUMMARY body tokens and does not authenticate execution. No new harm observed on the declared surface; no universal no-harm/safety claim. Historical visibility, recorder dirty/overwrite and capture-meta-test debts remain open. Certification OFF, K5 HELD; existing L0 holds routed around, no new L0 question.

## Sources & frontier

**207→209 registry rows**, additions **A2/B0/C0** (one mined, one rejected), unchanged old status/recheck/used-by cells. S284 official cat-file `-t` raw type admitted; S285 rejects raw-identity inference from recursive peeling (not the document itself). Both opened by L1 this round, 11/14-word located quotes/URLs/access dates in `corpus/lessons/round-58.md` Gate continuation and `census/round-58/source-opening.txt`; S58Scribe6 re-open agrees (lane-dispatched, not non-author). C2 is sourced by S284. No new knowledge entry or frontier promotion; source rows are not expansion credit.

Counting: committed registry row matcher `^ {0,3}\|\s*S[0-9]{3,}\s*\|` gave207 at base and209 after; census command below ran at both ends. W04 duplicate-URL warnings62→64 (new distinct scopes), exit0 at both ends, not hidden. Mistake red-before/green-after C1 and safety proposal findings recorded in lesson Mistakes/wave safety sections. Independent admit/reject spot-check remains closure-owned.

Assimilation: **none** (open r46 mass-id-drift hold); **considerthese/: no such directory**. No shokuknow adoption, sibling edit, or source-row bulk append.

Command at both ends:
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin souji`

Before output (`census/round-58/sources-before.txt`):
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
souji	W04	S123 duplicate url git-scm.com/docs/git-worktree across scopes
souji	W04	S124 duplicate url git-scm.com/docs/gitrepository-layout across scopes
souji	W04	S125 duplicate url git-scm.com/docs/git across scopes
souji	W04	S126 duplicate url git-scm.com/docs/git-worktree across scopes
souji	W04	S210 duplicate url raw.githubusercontent.com/GNOME/glib/2.84.0/gio/glocalfile.c across scopes
souji	W04	S216 duplicate url man7.org/linux/man-pages/man2/statx.2.html across scopes
souji	W04	S225 duplicate url man7.org/linux/man-pages/man5/proc_pid_fd.5.html across scopes
souji	W04	S232 duplicate url git-scm.com/docs/git-worktree across scopes
souji	W04	S236 duplicate url git-scm.com/docs/git across scopes
souji	W04	S237 duplicate url git-scm.com/docs/git across scopes
souji	W04	S238 duplicate url git-scm.com/docs/git-config across scopes
souji	W04	S240 duplicate url git-scm.com/docs/git-cat-file across scopes
souji	W04	S241 duplicate url man7.org/linux/man-pages/man7/fifo.7.html across scopes
souji	W04	S242 duplicate url man7.org/linux/man-pages/man2/open.2.html across scopes
souji	W04	S244 duplicate url git-scm.com/docs/git-merge-base across scopes
souji	W04	S245 duplicate url man7.org/linux/man-pages/man2/open.2.html across scopes
souji	W04	S246 duplicate url man7.org/linux/man-pages/man7/pipe.7.html across scopes
souji	W04	S250 duplicate url git-scm.com/docs/gitrevisions across scopes
souji	W04	S251 duplicate url git-scm.com/docs/git-merge-base across scopes
souji	W04	S255 duplicate url docs.python.org/3/library/inspect.html across scopes
souji	W04	S256 duplicate url docs.python.org/3/library/codecs.html across scopes
souji	W04	S257 duplicate url raw.githubusercontent.com/GNOME/gvfs/1.62.0/daemon/trashlib/trashitem.c across scopes
souji	W04	S261 duplicate url docs.python.org/3/library/subprocess.html across scopes
souji	W04	S262 duplicate url man7.org/linux/man-pages/man2/symlink.2.html across scopes
souji	W04	S265 duplicate url docs.python.org/3/library/collections.html across scopes
souji	W04	S266 duplicate url docs.python.org/3/builtins/stdtypes.html across scopes
souji	W04	S267 duplicate url docs.python.org/3/builtins/stdtypes.html across scopes
souji	W04	S270 duplicate url git-scm.com/docs/git-clone across scopes
souji	W04	S272 duplicate url docs.python.org/3/library/functions.html across scopes
souji	W04	S275 duplicate url git-scm.com/docs/git across scopes
souji	W04	S276 duplicate url git-scm.com/docs/gitignore across scopes
souji	W04	S280 duplicate url spec.commonmark.org/0.31.2 across scopes
souji	ok	/home/vgpnk/Projects/shokunin/souji-shokunin/corpus/SOURCES.md

EXIT=0
```

After output (`census/round-58/sources-after.txt`):
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
souji	W04	S123 duplicate url git-scm.com/docs/git-worktree across scopes
souji	W04	S124 duplicate url git-scm.com/docs/gitrepository-layout across scopes
souji	W04	S125 duplicate url git-scm.com/docs/git across scopes
souji	W04	S126 duplicate url git-scm.com/docs/git-worktree across scopes
souji	W04	S210 duplicate url raw.githubusercontent.com/GNOME/glib/2.84.0/gio/glocalfile.c across scopes
souji	W04	S216 duplicate url man7.org/linux/man-pages/man2/statx.2.html across scopes
souji	W04	S225 duplicate url man7.org/linux/man-pages/man5/proc_pid_fd.5.html across scopes
souji	W04	S232 duplicate url git-scm.com/docs/git-worktree across scopes
souji	W04	S236 duplicate url git-scm.com/docs/git across scopes
souji	W04	S237 duplicate url git-scm.com/docs/git across scopes
souji	W04	S238 duplicate url git-scm.com/docs/git-config across scopes
souji	W04	S240 duplicate url git-scm.com/docs/git-cat-file across scopes
souji	W04	S241 duplicate url man7.org/linux/man-pages/man7/fifo.7.html across scopes
souji	W04	S242 duplicate url man7.org/linux/man-pages/man2/open.2.html across scopes
souji	W04	S244 duplicate url git-scm.com/docs/git-merge-base across scopes
souji	W04	S245 duplicate url man7.org/linux/man-pages/man2/open.2.html across scopes
souji	W04	S246 duplicate url man7.org/linux/man-pages/man7/pipe.7.html across scopes
souji	W04	S250 duplicate url git-scm.com/docs/gitrevisions across scopes
souji	W04	S251 duplicate url git-scm.com/docs/git-merge-base across scopes
souji	W04	S255 duplicate url docs.python.org/3/library/inspect.html across scopes
souji	W04	S256 duplicate url docs.python.org/3/library/codecs.html across scopes
souji	W04	S257 duplicate url raw.githubusercontent.com/GNOME/gvfs/1.62.0/daemon/trashlib/trashitem.c across scopes
souji	W04	S261 duplicate url docs.python.org/3/library/subprocess.html across scopes
souji	W04	S262 duplicate url man7.org/linux/man-pages/man2/symlink.2.html across scopes
souji	W04	S265 duplicate url docs.python.org/3/library/collections.html across scopes
souji	W04	S266 duplicate url docs.python.org/3/builtins/stdtypes.html across scopes
souji	W04	S267 duplicate url docs.python.org/3/builtins/stdtypes.html across scopes
souji	W04	S270 duplicate url git-scm.com/docs/git-clone across scopes
souji	W04	S272 duplicate url docs.python.org/3/library/functions.html across scopes
souji	W04	S275 duplicate url git-scm.com/docs/git across scopes
souji	W04	S276 duplicate url git-scm.com/docs/gitignore across scopes
souji	W04	S280 duplicate url spec.commonmark.org/0.31.2 across scopes
souji	W04	S284 duplicate url git-scm.com/docs/git-cat-file across scopes
souji	W04	S285 duplicate url git-scm.com/docs/gitrevisions across scopes
souji	ok	/home/vgpnk/Projects/shokunin/souji-shokunin/corpus/SOURCES.md

EXIT=0
```

## Trend verdicts

- **expansion: unchanged** — no new admitted knowledge on uncovered ground, capability acquisition or frontier advancement; two curated source rows only (`corpus/README.md` r58 frontier).
- **quality: improved** — final receipt gate repairs five observed incorrect clean results, preserves three real receipts, selftest17/17; prior proposal regressions removed before landing. Evidence `census/round-58/c2-after.json`, sentinel final-digest review. Legacy hazards explicitly unclosed.
- **discernment: improved** — outside r57 spot-check's assessment/type/confinement defects become measured append-only corrections and grounded Q117; Q118 captures in-wave safety findings. C1 red2→green0, C2 red-control3/8→8/8. This is lesson-backed correction of outside disagreement, not a claim that lane-dispatched seats are non-author verifiers.

## SHONEN

- [~] Decision tables/error patterns/checklists/sources: `SKILL.md`, current r58 receipt registry, `corpus/SOURCES.md` S284/S285; author assertion, no non-author promotion claim.
- [~] End-to-end domain evidence-hygiene task executed/logged: `LOG.md` Round58 and `census/round-58/c2-after.json`; prior physical cleanup evidence remains SHONEN's LOG362 pointer, no new removal claimed.
- [~] Executable without oral context: frozen `census/round-58/preregistration.txt`, current SKILL commands, acceptance driver and revision-bound final receipts.
- [~] No cross-domain bleed: `PROVINCE.md` unchanged; list/check-only repairs, connector read-only sibling review, operator cleanup/credential/process holds unchanged.

## Append-only timing disclosure and final-tip correction

Parent scout flagged prerequisite timing after this report draft was written. Preserve the distinction between a finite target succeeding and admission prerequisites being satisfied; the parent closure judge owns the latter. No frozen statement, target, oracle or old harm was rewritten.

- Predicate/headerless C1-control freeze `e7f64f30324e8ddb3f2266302daa9066054cdbb3`: 2026-11-04 **11:44:19 -03:00**.
- C1 correction `dccdc469f4c2e0415e1a1dcc317364e1b4d3191e`: **11:46:25**.
- C2 executable oracle/before-control retention `1880343ed04337379c5478f91408c30c8fbd4b77`: **11:50:15**, after freeze and C1 correction. This proves late retention, not that it followed C2 scoring.
- C1 bound re-execution receipt `census/round-58/c1-control-binding.txt` retained in `b1c2bb9f762baa8142eaeaa5d4f472765b09dd32`: **11:55:37**. The original before file existed at freeze but had no command/revision/digest header; the later receipt does not backdate that metadata.
- C2 implementation/selftest development ran concurrently with the control builder. **Exact first development-selftest versus before-control generation order is not independently established. Do not credit a claim that all C2 implementation/scoring followed the control.** Final-candidate reviewer/critic rescoring and L1 integrated after-measurement followed the retained oracle/control; this does not erase the timing limitation.
- Prior spot-check pointers read for fresh-start preparation: r55 `fafe371694fea41c5d23f63083865d5ccf3f1d36`, r56 `b4ef0bc84ada3fb3aefd6a0b1a841a6517b84acd`, r57 `83d3813257648e99fb4ab2ddef217124f39cf324`, each at its standard `corpus/lessons/round-N-verifier-spotcheck.md` path.

This disclosure landed in lane **`8743010706b399dbc4121c09985d4ebfb85fb797`**, tied to `LOG.md:2787` and lesson Prerequisite timing disclosure. It supersedes the earlier description of `81d556e7f94569ae5f24b38458f157b153188191` as the final lane tip (that hash remains the evidence close-out ancestor). Required fresh `ls-remote origin refs/heads/master` now prints **`8743010706b399dbc4121c09985d4ebfb85fb797`**. Measurements remain at code revision `5e4b8f14572d7051537b167dece4541bed7d2bab`, unchanged. All original/inherited visibility-parser, recorder dirty-tree/overwrite, capture-meta-test, atomic-read/resource and diagnostic harms remain OPEN; C1 is not a Markdown repair.
