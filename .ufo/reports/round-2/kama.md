# kama-shokunin — round 2 report

- **Lane:** kama (local model serving & endpoint health; shonen, probation round 2)
- **Commit:** `83bee7f` (`round-2`) in `VeigaPunk/kama-shokunin`, pushed to `master`
- **Axis moved:** **freshness 6 → 7**; operability remains 8
- **Axes:** operability = runnable identity gate; freshness = re-verifiable state + drift history
- **Round shape:** round 1 could classify the current endpoint state but retained no predecessor. Round 2 adds durable invocation-to-invocation comparison without overstating it as scheduled monitoring.

## What landed

| Artifact | Verifiable measure |
|---|---|
| `tools/kama-probe.sh` | 1051 lines, 0755, md5 `61e82ee22dc89292175c5431f1ed6dc1`; new `snapshot` + `--history`; `bash -n` and `shellcheck -S warning` clean |
| `tools/test-snapshot.sh` | 171 lines, 0755, md5 `860f26ac05938cdfc1a8816eff1570b4`; `RESULT pass=24 fail=0` |
| `registry/history/latest.tsv` | tracked normalized 11-row baseline; sha256 `fd98f07a2d845a31cdf0582aa0faf9180e0903754b33248897a7e4211d9843da` |
| `registry/history/DELTA.md` | tracked append-only field/row transition ledger; sha256 `493afecbd6dd85df0f08f4541ecd340b03dc5df797a73bf8744cfd94edebab5a` |
| `registry/history/.gitignore` | ignores local dated JSON, lock, and temporary baseline files |
| `corpus/knowledge/snapshot-history.md` | command, schema, transition semantics, persistence boundary, scheduling handoff, measured runs |
| `corpus/lessons/round-2.md` | claim boundary, implementation traps, persistence threat model, runtime calibration |
| Existing lane docs | `SKILL.md`, `PROVINCE.md`, `SHONEN.md`, `SCORECARD.md`, `LOG.md`, corpus index, consumer registry, citation errata updated |

Commit measure: 15 files, +831/-89. No domain source tree was modified.

## Before → after

**Before:** `check` sampled 11 registry rows and returned the correct current gate status, but two identical exit-2 runs could not distinguish stable debt from a new transition. Freshness depended on a human retaining prior output.

**After:**

```text
$ bash tools/kama-probe.sh snapshot
snapshot=20260929T043044Z prev=- rows=11 model_ok=3 drift=8 transitions=0 exit=2
$ bash tools/kama-probe.sh snapshot
snapshot=20260929T043052Z prev=20260929T043044Z rows=11 model_ok=3 drift=8 transitions=0 exit=2
```

The first run created a baseline. The unchanged run wrote a local dated JSON but left both tracked files byte-identical at the sha256 values above. `snapshot --json` emitted valid `kama-probe/v2` with summary `{rows:11, model_ok:3, drift:8, transitions:0, exit:2}`. Exit 2 is the endpoint gate result, not a persistence failure.

Final unchanged gate:

```text
registry_rows_evaluated=11 model_ok=3 drift=8 exit=2
CHECK_EXIT=2
```

The eight 8080 rows remain `FOREIGN_SERVICE/html-non-model`; the three 34113 rows remain `MODEL_OK/matched`. Round 2 did not rewrite operator-owned pins.

## Transition contract and behavioral proof

`latest.tsv` retains only `id`, verdict, reason, normalized served-model basename, port, and file-match. `DELTA.md` records changes to those five state fields plus row additions/removals. A dated JSON must validate before tracked state advances. Stable state does not mutate tracked bytes.

`bash tools/test-snapshot.sh` exercised the actual CLI against an ephemeral HTTP model fixture:

- first baseline and valid/redacted JSON stdout + file;
- unchanged rerun with byte-stable baseline and ledger;
- `MODEL_OK → DEAD` plus reason/served-id transitions;
- served-id-only change;
- row addition and row removal;
- malformed-baseline warning, rebaseline, audit note, and no phantom transition;
- `snapshot --port` rejection;
- symlinked history-root rejection.

Result: `pass=24 fail=0` in 1.15 s. Live `check` remained 11/3/8/2 after the refactor.

## Persistence and write-boundary review

Sentinel review found four risks in the draft: credential-shaped URL/userinfo/query bytes, control characters corrupting TSV, symlink escape, and torn/concurrent baselines. The shipped path:

- excludes resolved URLs, registry notes, raw evidence, query/userinfo, and full model paths from tracked state;
- strips control characters and normalizes served ids to model basenames;
- refuses symlinked history roots and tracked outputs;
- serializes with `flock` and atomically replaces the baseline;
- validates dated JSON before ledger/baseline advancement;
- writes only below the selected history directory; consumer configs and services remain read-only.

A redundant `index.jsonl` draft was removed: dated filenames + JSON payloads + `latest.tsv` derive the same index. Keeping it created a second consistency surface with no new signal.

## Freshness audit of round-1 evidence

Reviewer re-derived every load-bearing live fact. Endpoint state is unchanged: 8080 is Jitsi/non-model, 34113 is the expected llama.cpp model, registry = 11 rows, gate = 3 ok / 8 drift. Three citation-state changes were recorded:

1. `enabled_providers: ["qwen-local"]` is at `~/.config/the-janitor/opencode.json:5-7`; line 16 is the 8080 `baseURL`. The round-1 fact was right; its line attribution was wrong.
2. `~/bench-arena/loop.sh:5` moved to `~/archive/bench-arena/loop.sh:5`; the stale `:8080/metrics` default is unchanged.
3. The round-1 listener census preserved 23 point-in-time rows; the refresh observed 20 due ephemeral listener churn.

Corrections live in `corpus/lessons/round-1-citations.md` and `consumer-registry.md`. The filed round-1 report/log was not rewritten.

## Runtime calibration

Only llama.cpp is installed. Neither `vllm` nor `ollama` binary/Python package exists. Scratch servers shaped like vLLM and Ollama model-list responses classified `MODEL_OK`; a plain JSON status look-alike classified `FOREIGN_SERVICE`. This proves parser compatibility only. Real vLLM/Ollama integration remains an explicit gap.

## Scheduling: claim boundary and L0 handoff

Critic verdict on the draft headline: **overclaim**. `snapshot` makes drift diffable per invocation; it does not make invocation periodic.

L1 re-verification found three active user timers (`ai-usage`, `webzites-probe`, `charter-scribe`) and no `crontab`, `crond`, `cron`, `at`, `atd`, or `anacron`. No timer invokes kama. `PROVINCE.md` forbids this lane from installing/enabling systemd units.

Filed in `.ufo/l0-questions.md`:

> Should the operator create/enable a systemd user timer for `snapshot` (`Type=oneshot`, `Persistent=true`, `SuccessExitStatus=2`, operator-chosen cadence), or keep per-round/manual invocation?

Until answered, a transition that begins and ends between invocations is invisible. This unresolved cadence is why freshness moves conservatively from 6 to 7, not 8.

## L2 batch and disposition

Eleven L2 agents were dispatched in one batched call, satisfying the ≥8 requirement.

| Agent | Role | Finding kept |
|---|---|---|
| `KamaPlannerSnap` | planner | Minimal state fields, first-run/stable/transition/recovery milestones |
| `KamaLabratRuntime` | labrat | vLLM/Ollama-shaped parser evidence; real runtimes absent |
| `KamaExecutorDocs` | executor | Operator-facing artifact and exit-code contract |
| `KamaCriticClaims` | critic | “Periodic” rejected; “invocation history” retained |
| `KamaConnectorSib` | connector | No sibling or existing timer owns this endpoint identity check |
| `KamaReviewerFresh` | reviewer | Bad line citation, moved path, transient count, mid-edit defects |
| `KamaSentinelSnap` | sentinel | Persistence minimization, control-char, symlink, lock/atomic-write requirements |
| `KamaMutationSnap` | mutation tester | Transition, row-set, corruption, and refusal scenarios |
| `KamaRevengerHist` | revenger | 8080→34113 migration/cutover reconstruction; scheduler surface inventory |
| `KamaScribeReport` | scribe | Report skeleton and evidence slots |
| `KamaSimplifier` | simplifier | Removed derivable index and dead helper |

L1 integrated findings from `/tmp/kama-r2`, fixed raced/mid-edit defects, and reran the final harness. Scratch prose was not treated as authority.

## Operator relay: effective model fallback

This was explicitly requested and is out of kama's endpoint-health province, so it is reported rather than absorbed.

Observed effective config:

- `modelRoles.m_swe = devin/swe-2:max`;
- `modelRoles.m_daybreak = openai-codex/gpt-daybreak-blue-latest:max`;
- `retry.modelFallback = true`, but `fallbackChains.m_swe = null` and `fallbackChains.m_daybreak = null`.

Therefore the exact `m_swe → openai-codex/gpt-daybreak-blue-latest:max` chain is **not visible/configured**. This session recorded nine genuine `Devin stream error resource_exhausted` events from `03:35:54Z` through `03:49:17Z`; no model-change event accompanied them. Model-change telemetry shows `devin/swe-2` at `03:19:34Z` and a later direct Daybreak selection at `04:13:34Z`, both `resolvedModelIsFallback:false`. Observed outcome: capacity failures did not advance a configured fallback; the later Daybreak switch was direct/non-fallback. No failure was forced and no route or mission config was edited.

**Handoff:** kumitate/protocol own route/fallback behavior if the operator wants this chain added.

## Residual gaps / next move

1. Invocation cadence remains operator-owned and unscheduled.
2. Declared-vs-served context drift (`limit.context=32768` vs live server 16384) is not in the snapshot schema; planned freshness move for round 3.
3. A transition that flaps entirely between samples is invisible.
4. Real vLLM/Ollama runtime behavior remains unmeasured.
5. Operator-owned stale 8080 pins remain live; the round-1 repoint question is unresolved.

- **Blockers:** none for the round-2 deliverable.
- **Promotion:** not claimed; this is verified probation round 2 of the required ≥3.
- **Push scope:** only `VeigaPunk/kama-shokunin` and this report/L0 line in `VeigaPunk/shokunin`; no domain source tree was written or pushed.
