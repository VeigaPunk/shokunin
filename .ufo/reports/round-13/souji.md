# Souji — round 13 (attempt 1)

## Work performed

Declared claims: **C1 calibration** (lowest non-retired axis, legacy score 7): executable declared-evidence consistency and demonstrated rejection of historical overclaims; **C2 operability**: bounded quarantine staging/digests with fail-closed diagnostics; **C3 coverage**: a sourced, bounded F2 repository-structure census. All three author verdicts are **improved**, numeric deltas 0 (the legacy 7/8/8 scores have no calibrated conversion). Independent round admission remains the outside closure duty; this report does not manufacture that verdict.

**Pushed lane HEAD: `15d95e380ca9ab61495448e3901899bcb276d4b3`.** Lane work was committed and pushed before this report was written.

- C1 adds `tools/souji-cert-evidence.py`, external black-box fixture and digest-pinned synthetic frozen inputs. It validates declared artifact/evidence digests, nonempty manifests, fragment ownership labels, paths, exit/verdict consistency and frozen input pins. Observed: embedded **36/36**, external **5/5**, frozen run clean with seven pins; actual historical wrong-byte and candidate substitutions reject with exact findings, exit 2. Evidence: lane `census/round-13/verification.json`, `replay-{wrong-bytes,candidate}.json`, `tests/fixtures/r13-cert-frozen/expected.json`; LOG.md:562.
- C1 expressly does **not** prove installed-location identity, authenticated author independence, command execution or complete defect-class coverage. The overwritten historical `census/round-10/cert-16.json:2618-2620` remains unchanged; its candidate CERTIFIED claim is explicitly superseded as authority for installed tools in LOG.md:514 and `corpus/lessons/round-13.md`, R13-M6. **Deletion certification stays OFF.**
- C2 bounds effective staging/digest/inspection operations, removes shadowed unbounded helpers and the implicit `cand-merge-verify.sh` fallback, refuses special files/descendants and cross-device staging, and reports source/quarantine/index-lock residue without removing locks. The same corrected fixture gives baseline **1/5 PASS, four failures including two hangs**, versus changed tool **5/5 PASS, no hangs**. Evidence: `tests/fixtures/r13-quarantine-bounds.sh`, `verification.json` entries quarantine-red-before/quarantine-bounds; LOG.md:562.
- C2 does not claim the historical M43 timeout's cause was established: serial 450-second holds are another explanation. Stable FIFO guarding partly existed already; the improvement is explicit bounds and diagnostics, not fictitious first acquisition of every refusal. Extra stage-5 deletion timeouts were rejected during integration because interruption can leave partial deletion; no new bounded-delete capability is claimed. Evidence: round-13 lesson First integrated verification and corrections; `.ufo/waves/round-13/w1/AttackBounds.md`, SafetyPaths.md and BoundQuarantine.md.
- C3 adds `tools/souji-repo-structure.sh`, an isolated write-safety fixture and `corpus/knowledge/git-repo-structure-readonly.md` citing S035/S036/S037. Observed **5/5** includes positive manifest-detector controls, persistent state equality, exact synthetic-repository metrics, bogus-repository refusal and configured partial/promisor refusal. Actual partial-clone lazy-fetch observations from AttackCoverage were accepted, not rerun merely to confirm them. The wrapper disables lazy fetch and refuses marked partial/promisor repositories; metrics are refs-rooted and common-store scoped, not reclaimable disk space. Evidence: verification.json, `.ufo/waves/round-13/w1/AttackCoverage.md`; LOG.md:514/562.
- Previous-round routed items are dispositioned in `corpus/lessons/round-13.md`, Routed previous-round items. K5 remains HELD; Q16 still withdraws the circular Q15 exception. Q17/Q18 learn the missing-fixture and relay failures; Q19 replaces Q8's spelling-count test with behavioral discrimination. SKILL.md contains the complete eight-field gate/probe registry, and SHONEN retains four author `[~]` marks. Evidence: QUALITY.md Q17–Q19, SKILL.md Gate registry, ReviewSHONEN.md erratum §8.
- No live hygiene removal, history rewrite, credential operation or sibling mutation was performed. The initial and final sole untracked path is **`census/operator-sweep-20261019/`, OPERATOR-authored**: never edited, moved, committed or deleted. No lane-authored leftovers were inherited. BaselineMeasures disclosed an overly broad read-only search emitting sweep matches; L1 did not inspect sweep content or authorize its inclusion. Evidence: before.json, baseline-measures.md, final lane status after push.

## Landed changes

All paths below are lane-relative, except this fleet report. Every change belongs to LOG.md:514 (declared round work), :562 (measured closing evidence), or :605 (ending source census).

| Commit | Landed work | LOG binding |
|---|---|---|
| `6ed10a7cd6c7b26f8068dd6e02497e860f9c4317` | Three tool/fixture slices, synthetic frozen inputs, domain instructions, quality criteria, source corrections, F2 entry, claim/baseline records, validated wave spec/dispatch/registry and all seat reports | LOG.md:514 |
| `6f8ee0f38a14a3cb599ee606c486a55ec64e8ae6` | Correct underscore finding parsing; isolate target SHA/move shims; fix warning-level findings; isolate fixture Git identity; preserve the complete failing first pass; updated implementation handoffs | LOG.md:562; lesson First integrated verification and corrections |
| `23014d40e48e52031939f124ce0ed215ca932c6f` | Final SCORECARD axes/capabilities and r14 plan; observed verdicts; revision-bound claim census; current coverage/admission corrections and source-introduction provenance correction | LOG.md:562 |
| `15d95e380ca9ab61495448e3901899bcb276d4b3` | Ending source census with exact source digest/revision, advisory-output correction and final evidence scope | LOG.md:605 |

Commits use `souji-shokunin <souji@shokunin.local>`, confirmed `git -C <lane> rev-parse --show-toplevel`, explicit matching add/commit pathspecs and `-c maintenance.auto=false`. Exact scope: `census/round-13/commit-scope.json`. Push succeeded to the lane origin, `31984f4..15d95e3`; final status showed only the protected operator sweep. Fleet report durability uses only `scripts/hyaku/fleet-commit.sh`.

## Before → after measurements

Baseline is `31984f473ce4bdab61a99b16cca194b28108cb81`. Exact commands, outputs and revisions are committed in `census/round-13/counts.json` and `verification.json`.

### C1 — calibration: declared-consistency discrimination

Counting command:

```sh
python3 census/round-13/count-claims.py 31984f4
python3 census/round-13/count-claims.py 6f8ee0f
```

Evidence gate absent **0→1** is only an inventory measure. The gain rests on exercised discrimination, not file existence:

```sh
python3 tools/souji-cert-evidence.py --selftest
python3 tests/fixtures/r13-cert-evidence.py
python3 tools/souji-cert-evidence.py --frozen tests/fixtures/r13-cert-frozen
python3 tools/souji-cert-evidence.py --root "$PWD" --manifest census/round-13/replay-wrong-bytes.json
python3 tools/souji-cert-evidence.py --root "$PWD" --manifest census/round-13/replay-candidate.json
```

At `6f8ee0f`, selftest **36/36**, external **5/5**, exit 0. The frozen run at `6ed10a7` was clean, seven inputs pinned. Historical replays at `6ed10a7` reject respectively `artifact-digest-mismatch` and `artifact-candidate`, exit 2. The actual stale candidate digest `60aef4c0…` differs from installed census `6a000c59…`. The later code change only repaired the selftest finding-id parser; retained observations are explicitly revision-tagged, not described as rerun. C1 is not broad tool certification. Verdict: **improved**, score 7→7.

### C2 — operability: same-fixture red before and green after

```sh
bash tests/fixtures/r13-quarantine-bounds.sh --tool <baseline-copy>
bash tests/fixtures/r13-quarantine-bounds.sh --tool "$PWD/tools/souji-quarantine.sh"
```

`census/round-13/run-verification.py` regenerates the baseline copy from `git show 31984f4:tools/souji-quarantine.sh` under an isolated `/var/tmp` directory and supplies the same installed receipt engine to both arms. At fixture revision `6f8ee0f`, baseline output is `SUMMARY total=5 failed=4 hung=2`, exit 1; changed output is `SUMMARY total=5 failed=0 hung=0`, exit 0. Failure reasons include the missing move/digest bounds, not a missing engine or live-fleet guard.

Regression commands, executed with `TMPDIR=/var/tmp`, synthetic Git author/committer identity and the advisory CLI disabled:

```sh
bash tools/souji-verify.sh --selftest
bash tools/souji-vault-verify.sh --selftest
bash tools/souji-quarantine.sh --selftest
bash tools/souji-census.sh --selftest
shellcheck -S warning tools/souji-quarantine.sh tools/souji-repo-structure.sh tests/fixtures/r13-quarantine-bounds.sh tests/fixtures/r13-repo-structure.sh
```

Observed at `6f8ee0f`: **40 / 51 / 91 / 36 checks**, all zero failures; warning-level ShellCheck exit 0. These embedded suites do not establish complete safety-class coverage. Verdict: **improved**, score 8→8.

### C3 — coverage: F2 held as bounded knowledge

The revision-bound count command above reports admitted knowledge **4→5**, F2 entry **0→1**, source rows **33→37**. HELD K5 is excluded.

```sh
bash tests/fixtures/r13-repo-structure.sh --selftest --probe tools/souji-repo-structure.sh
```

At `6ed10a7`: `selftest=PASS ids=5/5`, exit 0, Git 2.55.0. The normal synthetic repository's compared path/content/type/mode/size/mtime manifests are unchanged; detector controls first observe deliberate content and mtime changes. Atime, ctime, transient writes, arbitrary configurations, real partial-clone completeness, linked/bare/alternate/corrupt/concurrent stores and future versions are not proven. Wider F2 ground remains frontier. Verdict: **improved**, score 8→8.

The first full pass was not green: gate parser 35/36, nested external fixture 4/5, bounds 4/5, missing synthetic identity in legacy fixture commits, and ShellCheck warnings. It is preserved at `verification-attempt-1.json`. Only failed checks were rerun after fixes, plus the baseline pair because its fixture changed. No warning or failed observation was silently discarded.

## Sources & frontier

Contract census command, at start and end:

```sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin souji
```

Before (`before.json`, baseline 31984f4), exit **0**:

```text
souji	ok	/home/vgpnk/Projects/shokunin/souji-shokunin/corpus/SOURCES.md
```

After (`end-sources.json`, revision 23014d4 with exact source SHA-256), exit **0**:

```text
souji	W04	S035 duplicate url git-scm.com/docs/git-repo across scopes
souji	W04	S036 duplicate url git-scm.com/docs/git across scopes
souji	ok	/home/vgpnk/Projects/shokunin/souji-shokunin/corpus/SOURCES.md
```

The W04 lines are advisory and intentional: S035/S036 correct S005/S006 through new rows instead of rewriting immutable historical cells. No census failure is hidden.

- Rows **33→37**; tiers **A 29→33, B 3→3, C 1→1**; statuses **mined 16→20, queued 15→15, rejected 2→2**. Counting command: `count-claims.py` at the two revisions above; raw outputs in counts.json.
- Added by tier: **four A, zero B/C**. S034 is installed primary GNU timeout documentation (the web fetch timed out); S035/S036 are narrowed primary Git documentation corrections; S037 is tagged Git v2.55.0 source. Every new row's URL/access date/located ≤25-word quote is recorded in the round-13 lesson Gate.
- Existing rows have **no net in-place changes**. Mid-flight S005/S006 queued→mined and used-by changes were reversed after review; the old→new→old history is logged in the lesson. Their original opening dates and immutable cells remain unchanged.
- S035–S037 are mined by the new F2 entry; S034 is mined by the round lesson. The bounded source search, exclusion reasons and stop rationale are in SOURCES.md Search log and the opener reports. The old r12 `mined=18 queued=13` census predates the K5 hold and was not reused as the before state.
- Frontier advanced: bounded F2 structure-census capability only. Reclaimable-space attribution, unreachable-object accounting, shared-store aggregation and comprehensive certification remain outside this demonstrated slice. **One** admitted F2 knowledge entry, not four source rows, is the expansion gain.

## Trend verdicts

- **Expansion — improved:** one newly admitted, sourced F2 knowledge entry and demonstrated bounded capability on previously uncovered ground; counts.json, structure-selftest, README current coverage map.
- **Quality — unchanged:** operability and regression evidence improve, and source overstatements are corrected, but no separate stale sweep or supersession of an existing admitted knowledge entry is claimed under the strict LEARNING quality bar. K5 remains visibly HELD; nothing is forced into admission.
- **Discernment — improved:** the outside r12 K5 disagreement becomes lesson R13-M1, grounded Q17 and executable missing-evidence rejection. Q18 separates integrity from safety; Q19 rejects marker-only enforcement claims. Evidence: round-12-verifier-spotcheck.md, round-13 lesson, QUALITY.md and evidence-selftest output. The lane's seats are not independent non-author verifiers; fresh r13 admit/reject sampling remains for closure.

Owned axes calibration/operability/coverage: improved on the bounded measurements. Unworked depth/freshness/adjacency: unchanged; no harm claimed outside the exercised scope. Numeric scores are unchanged, not a synthetic scalar admission score.

## SHONEN

- [~] Decision tables/error patterns/checklists/sources: SKILL.md and its Gate registry; corpus/SOURCES.md; round-13 Gate. Author assertion only.
- [~] End-to-end domain task: historical operator sweep LOG.md:362; this round executes isolated domain-tool fixtures, not a new live removal. No new non-author box verification.
- [~] Executable instructions: SKILL.md Repository structure census and Checklists; tests/fixtures/r13-repo-structure.sh; verification.json. Author assertion only.
- [~] Province boundaries: PROVINCE.md Round 13 boundary refinement; `.ufo/waves/round-13/w1/Overlap.md`. Author assertion only.

No `[x]` was added. The extra Marks paragraph was removed because it is unindented protocol commentary, not part of the canonical indented seed; the reviewer withdrew its contrary range-extraction claim in ReviewSHONEN.md §8.

### Round conduct and handoff

- Wave: **one validated 32-seat batched taskCall**, dispatched unchanged. Roles: **7 executor, 4 scout, 2 connector, 8 reviewer, 4 critic, 2 sentinel, 2 revenger, 3 scribe**. L1 holds the planner seat because the validator excludes planner swarm roles. No model parameter. Spec, dispatch and assigned registry: lane `.ufo/waves/round-13/`.
- Several source/attack seats performed isolated exploratory probes despite the author-only/no-mid-flight-verification direction. Those handoffs are not substituted for the main agent's recorded final checks. The overbroad read-only operator-sweep search is disclosed above. No seat committed or mutated sibling/driver/operator files.
- **Stale-lane:** respawn-per-round; no other mission of this lane is open. This round progressed through the named lane commits; no silent stale mission is claimed.
- Tool installs/updates: **none**. Existing tools were used; authorization and official-channel rules were passed to all seats.
- Open L0 questions: **none**. No L0 append was required.
- Orchestrator actions: perform fresh non-author r13 admit/reject spot-check, verify committed evidence without executing a sibling's gates, append closure/ledger entry, and decide admission. Deletion certification remains OFF; no promotion or next round is started here.
