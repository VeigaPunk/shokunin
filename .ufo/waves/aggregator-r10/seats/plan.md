# CorpusPlan — round-10 planning evidence

## Scope and observations

Planning advice for L1's round plan; not judgment, admission, promotion, integration, or shipment. This seat changed only this file. No build, test, formatter, frozen replay, or live corpus-gate invocation was run by this seat. The only runtime measurement parsed the already-recorded baseline. No domain corpus content or credential finding text is reproduced here.

Binding inputs inspected: MISSION.md:38–60, AXES.md:6–39, SCORECARD.md:293–337, CORPUS.md:17–61, LEARNING.md:23–43, PROTOCOL.md:310–338 and 359–402, and matching canonical shokunin protocol sections. The host binding maps the required shokunin swarm to OMP tasks; this plan neither invokes UFO orchestration nor changes substrate/routes. Supplied taxonomy roles, not model parameters, determine routing.

- SCORECARD.md:301–305 gives the latest aggregator axes as cross-lane quality 9, corpus review 9, and mint/dormancy calls 9. This is an all-9 tie, not permission to claim saturation. Select exactly one move: corpus review, because default-selection omission is directly falsifiable.
- The recorded baseline `.ufo/waves/aggregator-r10/before.json:1–50` names fleet revision `b598ce0e1d4fa8851d3e238ee6afde42bd57f787`, exit 1, 19 local direct child lane directories, six summary rows and 13 omitted lanes. This is historical evidence, not a claim about the post-edit worktree.
- At inspection, `.ufo/waves/round-9/corpus-gate.mjs:165–172` fixes the default list to kasegi, kengaku, kake, kumitate, kotoba and kagi. At lines 851–860, `--all` chooses explicit `o.repos` or that fixed list. `MAIN_ROOT` derives from the script location (line 113), so selection must not depend on the caller's current directory.
- Existing flow is selection → `runLive` → revision stamp → `gradeCorpus` → result/notes → one summary per selected repo → process exit. Preserve this grading pipeline and ordered finding identifiers. Exit map is 0 clean, 1 failed, 2 could-not-evaluate, 3 failed/frozen drift; cross-result precedence is 2 > 3 > 1 > 0 (lines 116–118, 801–803, 884–886).
- `revisionStamp` (lines 488–495) does not check the Git top-level. A child directory with corpus but no own repository can inherit the fleet repository. Main acknowledged the need for a default-discovery-only root identity check; valid Git worktrees with a `.git` file must remain eligible. This is a source-derived failure hypothesis, not a fixture result from this seat.
- CORPUS.md:26,60–61 and PROTOCOL.md:310–325 require per-corpus review/verdicts and ledger refresh. Selecting every local child is necessary but does not fulfill semantic review, lesson filing, or missing configured-path coverage by itself.
- `.ufo/reports/round-10/aggregator.md:1–4` is the historical closeout marker. Preserve all its bytes and append the new complete report section. No root SHONEN.md is supplied: L1's final report must carry the canonical four-box assessment without self-awarded promotion marks.

Recorded-baseline measurement executed by this seat:

```sh
node -e 'const fs=require("node:fs");const b=JSON.parse(fs.readFileSync(".ufo/waves/aggregator-r10/before.json","utf8")); console.log(JSON.stringify({measured_commit:b.measured_commit,direct_children:b.direct_child_lanes.length,covered:b.covered,omitted:b.omitted.length,summary_count:b.summaries.length,representative_omitted:b.omitted.includes("kama-shokunin"),exit:b.exit}));'
```

Observed: direct_children=19, covered=6, omitted=13, summary_count=6, representative_omitted=true, exit=1, at the recorded revision above. No baseline verdict was rerun.

## Concrete data walk, then generalization

Representative omitted lane: **kama-shokunin**. The baseline omitted list includes it (`before.json:34`), while the fixed selector does not. Its current directory listing contains `corpus/README.md`, `corpus/knowledge/`, `corpus/lessons/`, and SHONEN.md. SCORECARD.md:318–320 already names the standing duty to emit kama alongside the original six, but default `--all` still cannot reach it through the inspected selector. None of these observations predicts kama's current finding count or verdict.

Smallest representative path: discover the physical direct child kama-shokunin → include its name in sorted default selection → confirm its own Git root → feed the unchanged live grader → emit a kama summary and honest live-tree revision/dirty metadata → combine its exit with all other selected results. A failure to evaluate is still a selected, visible result, not a reason to drop the lane.

Generalize the exact same path to every matching physical direct child, not a one-off addition of kama or another hardcoded nineteen-name list. Discovery is nonrecursive, excludes symlinks, and uses `/^[a-z0-9][a-z0-9-]*-shokunin$/`. Missing corpus or child Git does not remove a discovered lane: emit a per-lane exit-2 result. Zero discoveries emits an explicit coverage note and process exit 2, never vacuous clean. Do not source mutable shokunin.conf.

## Proposed round axes and honest notation

Keep the existing three aggregator axes stable within this round; corpus review is the sole selected axis-move. Proposed observables, not issued verdicts:

| Axis | Direction/observable | Proposed notation after L1 evidence gate |
|---|---|---|
| corpus review | Maximize exact local-directory selection coverage; minimize omission and duplicate summary counts without weakening any grade rule | `9 → 9 (held, not saturated); local selection 6/19 → 19/19, omissions 13 → 0` if the current census is still nineteen. Per-axis `improved` is proposed only if the acceptance gate supports it. |
| cross-lane quality | Preserve existing report/grading semantics; this move does not repair report or citation classes | `9 → 9 (unchanged by this move)`; do not claim this seat reran standing-duty evidence. |
| mint/dormancy calls | Preserve lifecycle and dormancy evidence; no mint or positive dormancy case is supplied | `9 → 9 (unchanged by this move)`; no promotion or lifecycle inference from selection. |

A broad `corpus review 9 → 10` would imply unsupported saturation: SCORECARD.md:333–334 explicitly retains semantic limits, and the gate declares seven not-evaluated categories (r1, r3, r5, r6, r9, box-3 independence, shonen-semantics). It also declares only partial rule coverage: r10 presence is not substantive review; r7 phantom-row detection is not complete index coverage; r8 literal detection is not authorized real-vs-schematic classification. Dynamic discovery changes none of these facts.

L1's recorded scoring decision: retain corpus review `9 → 9` numerically, while the independently measured local-selection delta `6/19 → 19/19` can support an `improved` per-axis verdict after L1's acceptance gate. Cross-lane quality and mint/dormancy remain 9, unchanged by this move. An after score need not be an integer increase: the improvement is the bounded coverage measurement, not an invented numeric rubric. No new subscore, axis split, retirement, or saturation claim is proposed. L1 owns the actual judgment; this seat supplies the evidence conditions only.

Learning trends must remain separate from gate selection. This move proposes expansion unchanged (no admitted domain knowledge), quality unchanged at the corpus-content level (no entry re-verification or supersession by this seat), discernment unchanged (no independent admit-and-reject spot-check or QUALITY.md criterion grounded by one). L1 must name any contrary evidence rather than substitute selection coverage for these LEARNING.md observables. No actual trend verdict is issued here.

## Ordered skeleton and per-step evidence gates

1. **Pin selection contract and before state.** Use the recorded baseline revision and counts above; L1 declares the three axes and corpus-review tie choice. Evidence: MISSION.md/AXES.md, SCORECARD.md:301–305, before.json. Continuity assumption: the recorded baseline is relevant to this repair; it is not proof of the current tree. This is not an orchestration-resume attestation; a true runtime resume would require canonical `resume_continuity_v1` rather than treating prior report/cache prose as authority.
2. **Replace only implicit default selection.** Discover sorted physical matching children beneath script-derived MAIN_ROOT. Keep explicit `--repos` behavior (including supplied ordering, relative/absolute paths, and its existing parsing), `--repo`, and `--snapshot` unchanged. Default-discovery-only child-Git identity handling must not migrate into explicit modes. Evidence: implementation diff confined to selector/coverage handling and owned documentation; no child/domain/config/state changes.
3. **Carry the representative case through unchanged grading.** Kama gets exactly one summary even when its grading fails. Every discovered lane follows the same path, including missing-corpus or missing-child-Git exit 2. Evidence: L1's summary-only runtime measurement; no raw findings copied into seat/report artifacts.
4. **Exercise acceptance after integration once, by parent.** Isolated fixtures cover direct-directory naming, sorted uniqueness, symlink/nested exclusion, missing corpus, missing child Git in a fixture beneath a Git parent, valid Git worktree, empty/unreadable discovery, and explicit override preservation. Preserve all historical expected snapshots and unchanged rule identifiers/exit semantics. Evidence: actual executed fixture results with code and stable identifiers/coverage notes, plus existing selftest/frozen replay results only if parent executes them.
5. **Record bounded result without promotion claims.** Append L1-owned LOG, SCORECARD and AGGREGATE evidence and append the complete report after its immutable marker. Record revision/worktree provenance, count command, unresolved semantic categories, three separate trends, unchanged axes, and four canonical SHONEN boxes. Evidence: landed paths and parent-run outputs, not this plan's predictions.

## Concrete acceptance invariants and falsifier

- Default `--all` summary labels equal exactly the sorted set of matching direct physical child-directory names at MAIN_ROOT. Exactly one summary per member; no symlink or descendant members. Equal counts alone are insufficient: a duplicated original lane could conceal an omission.
- A new qualifying local lane becomes visible without source/config edits; a removed lane disappears from this bounded filesystem universe. This intentionally does not detect configured-but-missing paths.
- A matching directory is selected even if corpus or its own Git root is missing, and produces exit 2; any such lane forces combined exit 2. Empty discovery also has explicit coverage diagnostic and exit 2, in both text and JSON-compatible execution paths without fake lane identities.
- Valid worktree Git roots count; a parent's repository is not evidence that an otherwise unversioned child owns a Git revision.
- `--all --repos ...`, `--repo`, and `--snapshot` preserve existing semantics. Existing frozen expected values are not refreshed merely to make replays match.
- Every selected lane's grading rules, ordered finding identifiers, exit classification, and dirty/live-vs-snapshot metadata remain unchanged except the necessary default-selection missing-child-Git failure.
- Falsifier: any qualifying direct physical local lane absent from default summaries; any extra/duplicate label; a symlink/nested lane selected; a missing-corpus/Git child silently skipped or graded clean; empty discovery returning 0; an explicit override replaced by discovery; a changed existing rule/exit/frozen result. Any one defeats the bounded coverage claim.

## Exact commands for parent evidence collection (not run here)

Expected local denominator, nonrecursive and excluding symlinks, from fleet root:

```sh
node -e 'const fs=require("node:fs");const n=fs.readdirSync(".",{withFileTypes:true}).filter(e=>e.isDirectory()&&/^[a-z0-9][a-z0-9-]*-shokunin$/.test(e.name)).map(e=>e.name).sort();console.log(JSON.stringify({count:n.length,lanes:n}));'
```

Contract's summary count command (a count, not proof of process success or label identity):

```sh
node .ufo/waves/round-9/corpus-gate.mjs --all --round 10 | grep -c '^# summary '
```

Safer one-invocation evidence collector retaining gate exit and emitting only identifiers/counts, never raw findings; use after integration, once:

```sh
node -e 'const fs=require("node:fs"),cp=require("node:child_process");const expected=fs.readdirSync(".",{withFileTypes:true}).filter(e=>e.isDirectory()&&/^[a-z0-9][a-z0-9-]*-shokunin$/.test(e.name)).map(e=>e.name).sort();const r=cp.spawnSync(process.execPath,[".ufo/waves/round-9/corpus-gate.mjs","--all","--round","10"],{encoding:"utf8",maxBuffer:1<<30});const summaries=(r.stdout||"").split("\n").filter(l=>l.startsWith("# summary "));const actual=summaries.map(l=>l.split(" ")[2]);console.log(JSON.stringify({gate_exit:r.status,signal:r.signal,spawn_error:r.error?r.error.code:null,expected,actual,expected_count:expected.length,summary_count:actual.length,omitted:expected.filter(n=>!actual.includes(n)),extra:actual.filter(n=>!expected.includes(n)),duplicates:actual.filter((n,i)=>actual.indexOf(n)!==i),ordered_exact:JSON.stringify(expected)===JSON.stringify(actual),summaries}));'
```

The collector itself is not the gate: its own exit cannot replace `gate_exit`; an empty exact-set comparison does not waive the required exit-2/coverage-note invariant. Persist only its redacted metadata under L1's allocated evidence paths. This seat did not execute these commands.

## Limits, unverified assumptions, hard blockers

No hard blocker to planning or the bounded selector repair was found. Child counts and live-tree contents can change after the recorded baseline: L1 must measure the final current denominator, not bake nineteen into implementation. Finding-count increases from selecting previously omitted lanes are expected detection changes, not proof of content deterioration or rule changes. No current kama verdict, post-edit fleet exit, regression result, frozen MATCH, or saturation claim is established by this plan. Configured paths absent from disk, semantic source correctness, history/ownership independence, true promotion claims, missing QUALITY/frontmatter/Gate-section checks, and other declared rule limitations remain outstanding and outside this move. Parent owns final evidence and judgment.
