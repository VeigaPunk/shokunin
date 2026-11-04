# tameshi — round 75 (attempt 1)

## Work performed

Declared claims: **R75-C1 — operability**, install three discriminating arms for
M-C and the roles/attack-share binding bypasses; **R75-C2 — calibration**,
reduce mismatches on the **16 declared capability figures**, with one frozen
red row. Calibration (8) is the lowest numeric axis; depth=10, freshness=9.

**Measured implementation targets reached; admission is not self-certified.**
The original C1 text incorrectly required exclusive kills for all six mutants;
old broad mutants necessarily fail additional new arms. Correction 1 disclosed
this. Correction 2 followed the critic's scored loose-token counterexample:
it freezes membership/regex/instrument tuples, rather than merely the row count.
These are frozen-contract defects, not retroactively pre-data changes. The
lesson's settlement errata supersede its earlier broad “pre-data” wording.
A non-author closure must judge the original predicates, not just the green
implementation receipts (`plans/round-75.plan.md`, lesson settlement errata,
`.ufo/waves/round-75/w1/T75W1C1.md`).

- Landed arms 16–18 and six-defect battery; new mutants fail only their named
  arms; legacy mutants retain their named kills with disclosed collateral
  failures (`.ufo/evidence/round-75/c1-landed-battery.txt`).
- Landed self-state re-derivation tool, exact 17-row manifest, and ambiguous
  figure refusal; seven in-population and two out-of-population cell repairs
  (`tools/selfstate-freshness.py`, `tools/selfstate-freshness.json`,
  `.ufo/evidence/round-75/apply-repairs-r75.py`).
- Restored cold-read credit 48/64 → 64/64 through 16 genuine input-keyed
  re-reads; ledger 883 → 899, EOL-preserving merge
  (`.ufo/evidence/round-75/rekey/rebind-stdout-r75.txt`).
- Re-opened S006, mined mistakes into QUALITY criterion 125, and disclosed the
  round-74 SCORECARD EOL conversion (LOG “round-74 closure defect 1 erratum”).
- Updated two registry needles and added two self-state rows. Hermetic registry
  run: `held=57/59 superseded=7`, exit 1; the same inherited red rows remain
  (`sources-census`, `verify-round15`), baseline `55/57`, not a full green gate
  (`.ufo/evidence/round-75/registry-check-tip-r75.txt`, scout §3).

Round shape: **one validated v1 wave, w1, 12 seats**, 4 executor + 1 scribe +
1 scout + 2 reviewer + 1 critic + 1 mutation-tester + 1 connector + 1 sentinel;
4/12 attack seats (33.3%), one connector, zero residual calls, zero dead seats.
The L1 held the planner seat. Every dispatched task leads with the Godspeed
binding; no model keys were passed. Orchestrator **WAVE-DONE received after all
12 settled**, before this report. Evidence:
`.ufo/waves/round-75/{w1-spec.json,w1-dispatch.json,w1-results.json}`.

## Landed changes

Final pushed lane tip: **`587ee30e20fa540f255474223d40da70c1339349`**.
All rows below tie to LOG “Round 75 — declared”, its correction paragraphs,
“Round 75 — measured”, or its EOL erratum; verification/settlement commits
retain the evidence supporting those entries.

| Commit | Landed work / LOG relation |
|---|---|
| `640d3fccfba7f6fab8e0341723b0fe6dbc200570` | declaration, plan and pre-data controls; LOG declaration |
| `7745d0e01e5a9bab781e73be566b28c41cd9483e` | kill-rule correction, L1 candidate battery, mutant evidence; LOG correction 1 |
| `82f7a809b21d0457209b92660c2e9db4bec0a5ca` | tuple freeze/control-4 and matrix disclosure; LOG correction 2 (timing caveat above) |
| `4e610748c3e5a0706767eb5569a08d426abc73b2` | tools/spec/manifest and nine row-scoped cell repairs; LOG measured |
| `08f09759d283c109f6fbf0a2b203947865809ded` | lesson, SCORECARD, SOURCES, QUALITY 125, registry; LOG measured + EOL erratum |
| `a9e6eef4f5f8df09e9fd0a84eab9928cd5a48a17` | rekey 16 sections; evidence for LOG measured no-harm restoration |
| `72b1ef6cd2420f2d7977ae4999443155aa3423ae` | all settled wave reports/results, green receipts, append-only settlement errata |
| `587ee30e20fa540f255474223d40da70c1339349` | exact subprocess exits and hermetic registry receipt |

`jj-lane.sh` printed `landed` for each; final `ls-remote origin
refs/heads/master` printed `587ee30e20fa540f255474223d40da70c1339349`.
Final helper state: ahead=0, behind=0, tracked=0, untracked=0.

## Before → after measurements

### R75-C1 — operability

Command (lane root):

```sh
python3 -I -X utf8 tools/wave-reconcile.py --selftest
bash tools/mutate-and-run.sh --target tools/wave-reconcile.py \
  --defects tools/wave-reconcile-mutants.spec \
  --suite 'python3 -I -X utf8 "$MUTANT" --selftest' \
  --workdir "$HYAKU_SCRATCH/tameshi-r75/l1/battery" --label wave-reconcile-arms-r75
```

Base `21ef81e9`: **15/15**, all three new mutants survive.
Tool commit `4e610748`: **18/18**, `defects=6 killed=6 survived=0
inconclusive=0 kill-rate=100%`, control GREEN and byte-identical restore.
New mutants → arm16/17/18 only, 17/18 each. Legacy m2 → arm13+16 (16/18);
span deletion → arm14+17+18 (15/18); any-depth → arm15 (17/18).
Arms 1–15 unchanged on the pristine candidate; baseline diff committed.
The landed receipt names target SHA256 `bf10c0e4…`, not the earlier L1 scratch
candidate (`c1-landed-battery.txt`, `c1-arms1-15-diff.txt`).
**Implementation verifies; original exclusivity wording fails literally.**

### R75-C2 — calibration

```sh
python3 -I -X utf8 tools/selfstate-freshness.py --repo . \
  --manifest tools/selfstate-freshness.json --doc-rev REV
python3 -I -X utf8 tools/selfstate-freshness.py --selftest
```

At base REV=`21ef81e99966198cf8cdb2c6d8e56aa3c482da56`:
`SELFSTATE: rows=17 match=9 stale=8 unexpected=7`, **exit 1**.
At repair commit `4e610748` and final measured content REV=`72b1ef6c`:
`SELFSTATE: rows=17 match=16 stale=1 unexpected=0`, **exit 0**;
`SELFSTATE_SELFTEST: 10/10 pass`.
Seven current assertions repaired; the historical red row still measures stale.
See `c2-after-r75.txt` and **`exact-final-exits.json`**. The earlier
`c2-before.txt` mistakenly printed the pipeline's `tail` exit 0; exact subprocess
capture corrects that record to exit 1. The counter population is bounded, not
all 24 capability rows. No new repertoire-table row was entered; no capability
acquisition credit is claimed despite SCORECARD's intent language.
**Measured mismatch reduction verifies; the post-score tuple freeze remains
an admission defect.**

No-harm command:

```sh
python3 -I -X utf8 tools/coldread-precheck-portable.py --repo . \
  --rev REV --work "$HYAKU_SCRATCH/tameshi-r75/l1/final-monitor"
```

Base 21ef81e9: credited=64/64. Records tip 08f09759: 48/64. Rekey tip
a9e6eef4 and settled content tip 72b1ef6c: **64/64, probe_mismatches=0**.
Pinned-input bytes are unchanged in final receipts-only commit 587ee30e.
Evidence: `coldread-red-r75.out`, `coldread-tip-r75.out`, `exact-final-exits.json`.

## Sources & frontier

Census command (both runs):

```sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tameshi
```

Before output:
```text
# round-75 census at round start (base 21ef81e9)
2026-11-04T02:23:20Z
tameshi	W04	S047 duplicate url pitest.org/quickstart/incremental_analysis across scopes
tameshi	W04	S048 duplicate url pitest.org/quickstart/incremental_analysis across scopes
tameshi	W04	S075 duplicate url man7.org/linux/man-pages/man1/strace.1.html across scopes
tameshi	W04	S076 duplicate url docs.jj-vcs.dev/latest/git-compatibility across scopes
tameshi	W04	S077 duplicate url man7.org/linux/man-pages/man2/PR_SET_CHILD_SUBREAPER.2const.html across scopes
tameshi	W04	S078 duplicate url man7.org/linux/man-pages/man2/open.2.html across scopes
tameshi	W04	S081 duplicate url bazel.build/reference/test-encyclopedia across scopes
tameshi	W04	S092 duplicate url bazel.build/remote/caching across scopes
tameshi	W01	S101 tierC mined used-by=corpus/knowledge/witness-equivalence-rule.md
tameshi	W04	S104 duplicate url cgit.git.savannah.gnu.org/cgit/bash.git/plain/doc/bashref.texi?id=b8c60bc9ca365f8261fa97900b6fa939f6ebc303 across scopes
tameshi	W04	S160 duplicate url stryker-mutator.io/docs/mutation-testing-elements/equivalent-mutants across scopes
tameshi	W04	S265 duplicate url testing.googleblog.com/2016/05/flaky-tests-at-google-and-how-we.html across scopes
tameshi	W04	S266 duplicate url pitest.org/quickstart/incremental_analysis across scopes
tameshi	W04	S267 duplicate url github.com/containers/bubblewrap/blob/v0.13.1/bwrap.xml across scopes
tameshi	W04	S268 duplicate url www.tensorflow.org/federated/golden_tests?hl=zh-cn across scopes
tameshi	W04	S274 duplicate url bazel.build/basics/hermeticity across scopes
tameshi	W04	S288 duplicate url www.atlassian.com/incident-management/handbook/postmortems across scopes
tameshi	W04	S293 duplicate url git-scm.com/docs/git-cat-file across scopes
tameshi	W04	S303 duplicate url www.gnu.org/software/sed/manual/sed.html across scopes
tameshi	ok	/home/vgpnk/Projects/shokunin/tameshi-shokunin/corpus/SOURCES.md
exit=0
```
After output:
```text
# round-75 census at round end
2026-11-04T02:47:01Z
tameshi	W04	S047 duplicate url pitest.org/quickstart/incremental_analysis across scopes
tameshi	W04	S048 duplicate url pitest.org/quickstart/incremental_analysis across scopes
tameshi	W04	S075 duplicate url man7.org/linux/man-pages/man1/strace.1.html across scopes
tameshi	W04	S076 duplicate url docs.jj-vcs.dev/latest/git-compatibility across scopes
tameshi	W04	S077 duplicate url man7.org/linux/man-pages/man2/PR_SET_CHILD_SUBREAPER.2const.html across scopes
tameshi	W04	S078 duplicate url man7.org/linux/man-pages/man2/open.2.html across scopes
tameshi	W04	S081 duplicate url bazel.build/reference/test-encyclopedia across scopes
tameshi	W04	S092 duplicate url bazel.build/remote/caching across scopes
tameshi	W01	S101 tierC mined used-by=corpus/knowledge/witness-equivalence-rule.md
tameshi	W04	S104 duplicate url cgit.git.savannah.gnu.org/cgit/bash.git/plain/doc/bashref.texi?id=b8c60bc9ca365f8261fa97900b6fa939f6ebc303 across scopes
tameshi	W04	S160 duplicate url stryker-mutator.io/docs/mutation-testing-elements/equivalent-mutants across scopes
tameshi	W04	S265 duplicate url testing.googleblog.com/2016/05/flaky-tests-at-google-and-how-we.html across scopes
tameshi	W04	S266 duplicate url pitest.org/quickstart/incremental_analysis across scopes
tameshi	W04	S267 duplicate url github.com/containers/bubblewrap/blob/v0.13.1/bwrap.xml across scopes
tameshi	W04	S268 duplicate url www.tensorflow.org/federated/golden_tests?hl=zh-cn across scopes
tameshi	W04	S274 duplicate url bazel.build/basics/hermeticity across scopes
tameshi	W04	S288 duplicate url www.atlassian.com/incident-management/handbook/postmortems across scopes
tameshi	W04	S293 duplicate url git-scm.com/docs/git-cat-file across scopes
tameshi	W04	S303 duplicate url www.gnu.org/software/sed/manual/sed.html across scopes
tameshi	ok	/home/vgpnk/Projects/shokunin/tameshi-shokunin/corpus/SOURCES.md
exit=0
```

Rows **164 → 164**; zero added by tier, no frontier row advanced. Count:
`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` → 164.
S006 re-opened 2026-11-04, status `mined` → `mined`, recheck `90d` → `90d`;
used-by old → new:
`corpus/knowledge/witness-scoped-kill-verdict.md, corpus/knowledge/mutation-score-semantics.md, corpus/lessons/round-12.md`
→ the same plus `corpus/lessons/round-75.md`.
Gate records URL/date/located quotes (6, 12, 21 tokens); fresh README sha256
`96057728…`, 13,970 bytes. Admit = S006 re-open; reject = duplicate new README
row, with reason/flip in the lesson Gate (pre-staging refusal, no rejected row
added). Independent non-author admit/reject spot-check remains for closure;
our wave seats do not supply it.

**Assimilation: none.** No package payload adopted. `considerthese/2026-10-28.md`
proposal 4 was measured, not implemented as a standing burn-down capability:
81 staged `new-file` payloads, 12 corresponding lane paths, zero byte-identical,
69 path-level backlog; four amendment targets have no staged payload file.
Commands and literal outputs are in `w1/T75W1E4.md` §4 and its receipt; actual
payload location is `merge/tameshi/knowledge/corpus/knowledge/`, not a direct
`knowledge/*.md` glob. Path presence is not adoption.

Cross-domain: connector found analogous current-number re-derivation in kagi,
souji and kumitate; the exact 17-row predicate remains lane-specific. No sibling
or source repo was edited (`w1/T75W1CN1.md`). Mistakes and fixes are in lesson
`## Mistakes`; QUALITY 125 cites that lesson.

## Trend verdicts

- **expansion — unchanged:** no knowledge entry/frontier move or repertoire
  row entered; one runnable instrument demonstrated, not acquisition credit.
- **quality — improved (measured):** three new discriminating arms, six kills,
  seven in-population assertions repaired, ambiguous figures refused; cold-read
  credit restored. Known survivors are recorded, not treated as kills.
- **discernment — unchanged pending outside judgment:** attacks exposed the
  freeze/control gaps and were learned into criterion/errata. Our own seats
  cannot supply the required independent admit/reject agreement.

Open carries: doc-rev-ignored mutant survives the landed **10/10** selftest
(4/5 instrument mutants killed, **not** five); printed-less seat_reports bypass
survives 18/18; attack printed-value and delimiter/duplicate-span cases remain
unmeasured. Six older instrument registry homes and SKILL registry fields stay
open. Two dated-literal cells (pin/evidence disposition) and the r17 supersession
figures are stale. r73 plan/report and r74 S294 old→new lesson repair remain
open. Correction to r73 report: 23 round commits, not its 22-row table;
census warnings are 18 W04, not 19. r74 green receipt measured **f5e9f9e2**, not
ef57dc2a; this round supplies an independently pinned green monitor receipt.

Operational defects: several seats used small `/tmp/tameshi-r75` scratch dirs
when HYAKU_SCRATCH was unset rather than the required `/fast` default; cleaned
by those seats and disclosed. The L1's live registry check generated red r15
residue; hashed then removed, final hermetic run used `--rev`. Final fleet
misroot sweep found no tameshi seat files; `.scratch/*`, `after`, and
`ns-arm-r73s02.txt` are unrelated/operator or sibling state and untouched.
No installations/upgrades; pacman untouched. Required skill/rules loading was
not fully in the requested order; recorded as a procedural defect, not a pass.
Stale-lane: respawn-per-round; no other tameshi mission open. No new L0 question.

## SHONEN

- [~] Box 1 — cited decision tables/error patterns/checklists in `SKILL.md`;
  assertion only, no non-author promotion verifier (`reports/round-1-calibration.md#box-1`).
- [~] Box 2 — end-to-end mutant injection/run/restore logged under LOG Round 75;
  `c1-landed-battery.txt`; no independent promotion verifier.
- [~] Box 3 — input-keyed monitor 64/64 at **72b1ef6c**, exact exit receipt
  `exact-final-exits.json`; not a blind cold-read or promotion verification.
- [~] Box 4 — PROVINCE ownership unchanged; connector read-only overlap scan;
  no independent promotion verifier (`w1/T75W1CN1.md`).

Self-evaluation: accuracy 3 (freeze-timing and pipeline-exit errata), completeness
3 (measured delivery landed, admission defects explicit), clarity 4 (bounded
populations and survivors named), actionability 4 (commands/commits resolve),
conciseness 3 (large evidence record). Priority: freeze exact tuples and controls
before dispatch; use hermetic registry execution; preserve exact subprocess exits.
