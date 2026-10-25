# Souji round 14 — retained-evidence eligibility and credential-store census boundaries

## Work performed

Declared claims (two, causally separable): **C1 calibration**, the lowest non-retired axis, acquires digest-bound eligibility and enforces it in the actual retained-result consumer; **C2 operability** fences census root/compare/Git/worktree paths before protected-namespace access. Both are bounded measured improvements, not comprehensive deletion certification. Numeric scores stay calibration 7 / operability 8 / coverage 8, delta 0, legacy-unmapped (`souji-shokunin/SCORECARD.md:11–15`).

- C1: added the local eligibility gate, 48-case self-invocation, 22-case black-box fixture and digest-pinned frozen snapshot. It rejects stale, legacy, malformed and unsafe input, preserves the original declared revision, and explicitly cannot authenticate historical execution or discover complete dependencies. Evidence: `souji-shokunin/tools/souji-evidence-cache.py`; `tests/fixtures/r14-evidence-cache.py`; `tests/fixtures/r14-cache-frozen/`; `census/round-14/verification-attempt-1.json`, cache-selftest/cache-fixture/cache-frozen results, measured at `48f8945780adeb259cff0ef7dd9b7efbf1544ec7`.
- C1 caller migration: replaced blind retention in `census/round-13/run-verification.py`; its entry now requires explicit round/new output and refuses default invocation before work. Historical JSON is never overwritten. The actual old `run()` branch is isolated from committed baseline source and demonstrated retaining a stale green; the actual migrated decision function refuses it. Main's first run caught a real fallthrough bug, fixed without weakening the fixture. Evidence: `census/round-14/cache-demonstration.py`; `verification-attempt-1.json` versus `verification.json`, cache-consumer-red-green and historical-runner-default-refusal; lesson R14-M4.
- C2: implemented lexical-first/componentwise refusal, HOME plus passwd/PI protected roots, bounded Git-store/alternate/worktree checks, inherited Git/config fencing and operator-sweep exclusions. Same isolated fixture proves forbidden-access observations on baseline versus zero assertion failures after the change, with ordinary positive controls. Evidence: `tools/souji-census.sh`; `tests/fixtures/r14-census-boundary.py`; `census/round-14/verification.json`, census-boundary-red-before/census-boundary.
- Frontier/mistakes: corrected S034's vendor line locator with new S038 and a named lesson erratum; opened local implementation S039 and Python path semantics S040. Added grounded Q20/Q21 and demonstrated source-anchor rejection/acceptance. Evidence: `corpus/SOURCES.md`; `corpus/QUALITY.md:45–50`; `corpus/lessons/round-14.md`, Mistakes/Gate; `census/round-14/check-timeout-anchor.py`.
- Preserved explicit limits: certification OFF; K5 HELD; r13's unexercised operation sites remain unproved. No live census, quarantine/removal, history rewrite, sibling write or real credential-store probe occurred. Evidence: round-14 lesson Final measured gate decisions; `PROVINCE.md:82–93`; both verification manifests' scope and unchanged-artifact observations.

Wave: exactly one campaign-policy-validated, unchanged `taskCall` of **32 leaf seats**: executor 5, scout 5, connector 3, reviewer 8, critic 4, scribe 3, sentinel 2, revenger 2. L1 holds the canonical planner seat; the validator excludes planner as a swarm role. Evidence: `souji-shokunin/.ufo/waves/round-14/w1-spec.json`, `w1-dispatch.json`, `w1/swarm-registry.json`. No per-seat model parameter or routing edit. Absolute seat paths and lane-relative Report trailer resolution were embedded in the context.

Process deviations are not concealed: SafetyCredential and BoundaryAttack ran prohibited mid-flight synthetic empirical probes; SafetyCache ran a synthetic kernel-open probe. Their reports retain the observations and deviation notes. Main did not rerun those probes to confirm them or use them as acceptance; committed final L1 fixtures supply acceptance. Early missing-artifact reviews were concurrent design advice, not dead seats. Unexercised proposed case counts, statistical-independence assertions and “100% legacy preservation” were not admitted. Adjudication: `corpus/lessons/round-14.md`, Process deviations and advisory disagreements.

Stale-lane: respawn-per-round driver; no other mission of this lane is open. This mission progressed through lane-authored source, correction and evidence commits; this report closes only round 14. Initial state had no lane-authored leftovers. The sole untracked `census/operator-sweep-20261019/` is OPERATOR-authored, remains unread/unedited/unmoved/uncommitted/undeleted, and is excluded from staging. Final status showed only that directory; ahead count was 0 after push.

Tool installs/updates: **none**. The later host partial-upgrade safety gate was relayed to the two then-live seats; no packages or services were changed. No new or open souji L0 question was found by the bounded `^souji \|` queue search. Sibling/operator boundaries were reviewed in `w1/SiblingOverlap.md`; this is a refusal fence, not kagi credential hygiene or kumitate fleet orchestration.

## Landed changes

All lane commits carry `souji-shokunin <souji@shokunin.local>`, confirmed owning toplevel, identical named add/commit pathspecs and `-c maintenance.auto=false`. Scope evidence: `census/round-14/commit-scope.json`. No amend/history rewrite.

| Commit | Landed work | LOG binding |
|---|---|---|
| `48f8945780adeb259cff0ef7dd9b7efbf1544ec7` | source gate, consumer migration, census fence, fixtures/frozen inputs, opened source rows, Q20/Q21, validated wave and initial lesson/docs | `souji-shokunin/LOG.md:618–655`, round-14 motivation; `:657–669`, historical-runner provenance |
| `552cae4204b3ab818419ad8adbfef3a4da29a3e0` | actual stale-retention fallthrough fix, alternate fixture setup repair, quoted ShellCheck literal, preserved failing evidence and targeted measurement runner | LOG round-14 measured closure evidence, `:671–714`; lesson First integrated measurement and corrections |
| `42d0b7b177b05889589009d94314cb3d7231ac25` | successful targeted observations, before/after counts, final scorecard/capabilities, bounded documentation and adjudication | LOG `:671–714`; `census/round-14/verification.json`, `counts.json` |
| **`69c1604474494fc2746e091fd545c5d283c02cba`** | ending source census and complete lesson/log | LOG `:716–724`; `census/round-14/end-sources.json` |

**Pushed lane HEAD: `69c1604474494fc2746e091fd545c5d283c02cba`.** `git push` advanced the lane remote master from a31642d to 69c1604; `git rev-list --count '@{u}..HEAD'` returned 0. This report was written only afterward, with no uncommitted lane work (operator sweep excluded). The historical r13 JSON digest is unchanged in both measured runs; reproducing its old retry command requires its cited old revision, not the current migrated runner.

## Before → after measurements

Inventory command, both exact revisions:

```sh
python3 -B census/round-14/count-claims.py a31642d14006830ec62edf40b0354c3699728c4a
python3 -B census/round-14/count-claims.py 552cae4204b3ab818419ad8adbfef3a4da29a3e0
```

Both exited 0; complete stdout is committed in `souji-shokunin/census/round-14/counts.json`.

| Claim | Falsifiable before → after | Executed counting/behavior command and measured revision | Verdict |
|---|---|---|---|
| C1 calibration / capability | gate and external fixture absent 0→present 1; authentic baseline retains a stale green without invoking producer → actual migrated caller returns no retained source on exit 1. First integrated consumer 32/33 → corrected 33/33, with exact stale finding and original declared revision preserved | inventory above; `python3 -B tools/souji-evidence-cache.py --selftest` → 48/48, external fixture → 22/22, `--frozen tests/fixtures/r14-cache-frozen` → reusable/two pinned inputs at **48f8945**; `python3 -B census/round-14/cache-demonstration.py` → status ok, 33 true checks, no failed checks at **552cae4** | **improved**, declared-byte eligibility and caller enforcement only |
| C2 operability | identical corrected fixture on baseline tool: 2/12 pass, 10 contract/access failures, exit 1 → changed tool: 12/12 pass, exit 0; ordinary/scratch positive controls pass both | `python3 -B tests/fixtures/r14-census-boundary.py --tool <baseline-or-installed-path>` at **552cae4**, baseline tool extracted from **a31642d**. Both exact commands, digests, access traces and case outputs in `verification.json` | **improved within the tested namespace cases** |

Other exercised checks:

- `python3 -B census/round-13/run-verification.py` without explicit round/output: exit 2 before matrix execution, at both source revisions. Historical evidence unchanged.
- `bash tools/souji-census.sh --selftest`: 38 checks, zero failures at 552cae4, including linked worktree dirty/absent flags and comparison exits 0/3.
- `shellcheck -S warning tools/souji-census.sh`: exit 0 at 552cae4; the earlier SC2100 failure remains in first-pass evidence.
- Same `python3 -B census/round-14/check-timeout-anchor.py <row>`: S034 mismatch/exit 1; S038 match/exit 0, at 48f8945. Corrected anchors are 15319–15320 and 15365, not 15316–15317/15349.

Main first ran `python3 -B census/round-14/run-verification.py` at 48f8945 (exit 1, preserved, not called green). After corrections, `python3 -B census/round-14/run-targeted.py` at 552cae4 exited 0. Only failed checks and green checks whose subject bytes changed were repeated. Unchanged passing observations remain solely in the first manifest at their actual revision; no cached pass was relabelled as a later execution. Both manifests record unchanged measured artifacts and historical r13 evidence.

No universal no-harm/configuration claim is inferred. Local includes/filters/hooks/attributes/excludes, alternateRefsCommand, promisor/partial-clone or worktreeConfig settings may now refuse the whole census as unsupported. Hardlinked object files, work-tree content symlinks, bind/mount replacement, relocated stores and guard/use races are residuals. These restrictions are exposed for independent closure/operator judgment. Preserved ordinary/linked/comparison controls show no measured harm on that bounded surface; depth/coverage/freshness/adjacency are unworked/unchanged. Full deletion certification and the previously unexercised quarantine sites are not acquired.

## Sources & frontier

Census before→after: **37→40 rows**, tier A/B/C **33/3/1→36/3/1**, mined/queued/rejected **20/15/2→23/15/2**, from the committed counting command above. Added **three A** rows (two primary vendor/docs, one local implementation code); no B/C additions. Existing S001–S037 status/recheck/used-by cells are unchanged. New rows are absent→mined with `corpus/lessons/round-14.md` used-by:

- **S038** supersedes S034's immutable locator, not its historical bytes. Installed coreutils 9.11 vendor source reopened; exact ≤25-word quote/access date in lesson Gate.
- **S039** opens the pinned local implementation, source SHA-256 `dd279ba95eebd13a6674f79983cec286fd856aa6d7e0719bf551ae0fc08939d6`; quote/anchor in Gate. C1 cites it as primary implementation evidence, not execution proof.
- **S040** opens Python 3.15.0 pathlib documentation, pure computation versus filesystem-aware resolution; located quote/access date in Gate. C2 cites it.

Required command, run at round start and end:

```sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin souji
```

Start at a31642d, **exit 0**, full stdout (`census/round-14/before.json`):

```text
souji	W04	S035 duplicate url git-scm.com/docs/git-repo across scopes
souji	W04	S036 duplicate url git-scm.com/docs/git across scopes
souji	ok	/home/vgpnk/Projects/shokunin/souji-shokunin/corpus/SOURCES.md
```

End at 42d0b7b, **exit 0**, full stdout (`census/round-14/end-sources.json`):

```text
souji	W04	S035 duplicate url git-scm.com/docs/git-repo across scopes
souji	W04	S036 duplicate url git-scm.com/docs/git across scopes
souji	W04	S038 duplicate url www.gnu.org/software/coreutils/manual/html_node/timeout-invocation.html across scopes
souji	ok	/home/vgpnk/Projects/shokunin/souji-shokunin/corpus/SOURCES.md
```

W04 notices are advisory retained correction-URL duplicates, not failed exit conditions. End registry digest `312a028ab7077fa04445d22d605c822ac187477561017da4da5edc7a2d49ba8d` is persisted; no source/executable bytes changed afterward.

No new coverage-map ground advanced and admitted knowledge stays **5→5**, HELD **1→1** (`counts.json`). Two demonstrated capabilities enter SCORECARD; rows are not counted as knowledge. Mistakes R14-M1–M4 include the outside retention caveat, citation drift, unenforced input boundary and this round's real caller fallthrough; the Gate records admits and rejects. K5 remains HELD. Independent non-author admit/reject sampling is still the orchestrator's closure duty, never self-assigned to these seats.

## Trend verdicts

- **Expansion — improved:** two demonstrated repertoire capabilities enter SCORECARD with actual running evidence, while knowledge/coverage ground is honestly unchanged. Evidence: SCORECARD capabilities, verification manifests and counts.json; no source-row-growth proxy.
- **Quality — unchanged:** no separate existing-admitted-knowledge freshness/supersession sweep is claimed. The source locator correction and bounded tool improvements do not silently become such a sweep; K5 remains visibly HELD.
- **Discernment — improved:** prior outside retention/citation findings become a named erratum, grounded Q20/Q21 and discriminating negative evidence; the real caller integration failure is preserved and fixed, not outvoted or suppressed. Evidence: round-13 non-author spotcheck, round-14 Mistakes/Gate, both verification manifests. Current outside sampling remains pending.

Author claim verdicts are bounded improvements, not an independent admission or promotion decision. Calibration/operability improve on the stated tests; numeric score deltas remain 0; other axes unchanged. The independent closure must judge the explicitly disclosed configuration refusals and evidence limits.

## SHONEN

- [~] Real decision tables, error patterns, checklists and cited sources: `souji-shokunin/SKILL.md`, Gate registry/Retained evidence and protected census paths; SOURCES S038–S040. Author assertion only.
- [~] End-to-end domain task executed/logged: existing `souji-shokunin/LOG.md:362` operator-owned artifact handoff/removal record; no new live removal asserted this round.
- [~] Instructions executable without oral context: actual cache selftest/black-box/frozen/consumer and census fixture/legacy observations in both round-14 verification manifests; explicit refusal/output instructions in SKILL. Author assertion, not universal configuration support.
- [~] No cross-domain bleed: `souji-shokunin/PROVINCE.md:82–93`, `w1/SiblingOverlap.md`, round-14 lesson limits; credential operations remain kagi's and fleet orchestration kumitate's. No `[x]` or promotion is written by this lane.
