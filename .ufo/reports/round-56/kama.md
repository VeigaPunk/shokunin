# kama — Round 56 (attempt 1)

## Work performed

Round 56 declared C1, an **operability** claim (the replay counter rejects the `LD_AUDIT` environment name), and C2, a **calibration** claim (the battery roster matches preregistration). C1 verifies narrowly; C2 is not admitted, and the round does not meet the all-claims admission gate.

- Froze two claims and red base controls before data; C1 pins the counter bytes by SHA-256. Freeze commit: `efc6b3ec6fb6ea308c15855e9b8b62856f4255b7`; preregistration `.ufo/waves/round-56/preregistration.json`.
- Ran one v2 wave, `kama-r56-w1`, 64 seats; all 64 settled and none died. Mix: reviewer 16, critic 8, mutation-tester 8, executor 8, scout 8, sentinel 4, revenger 4, scribe 4, connector 2, simplifier 2. The strict falsification share (reviewer+critic+mutation-tester) was 32/64=50%; including sentinel+revenger, 40/64. Validator topology excludes planner; L1 held the planning seat. No residual call or second wave. Results: `.ufo/waves/round-56/w1/w1-results.json`; dispatch/spec/validation are under `.ufo/waves/round-56/w1/`.
- Integrated the exact-field comparator correction and a negative `undetected` selftest after reviewer/mutator findings. The frozen C1 counter/predicate were not changed; battery/helper source was not separately hash-pinned in preregistration, so this post-wave integration is a conformance limit, not concealed as part of the frozen counter. Receipts: `.ufo/waves/round-56/measured/comparator-selftest.out` and `comparator-mutation-selftest.out`.
- C2's no-op control exposed a vacuous target: a fixture with the exact `ROSTER` literal but `main(): return 0` (no battery entries run) still returns `met=True`. The same counter checks only a declarative roster, not actual invocations or a SCORECARD/SHONEN mismatch. Receipt `.ufo/waves/round-56/measured/c2-noop-control.out`; the frozen C2 predicate was not changed after data.
- Mission binding is also unresolved: `MISSION.md:29` assigns kama **operability + freshness** and §1 says mission files win, while the prompt, `shokunin.conf` and the lane SCORECARD say operability + calibration. The existing L0 question `kama | round-35` remains open. C2 was frozen as calibration, not silently reclassified; no freshness claim was made. Thus C2 fails both the MISSION-axis and §9 calibration-counter requirements.
- Routed round-55 defects: corrected the substring-comparator survivor with exact equality and a negative selftest; recorded exits; added S514/S515 as append-only source-anchor corrections for S510/S511; re-anchored SCORECARD depth/calibration labels and the 42-spotcheck count; preserved 305 inherited round-55 late seat outputs/results and all round-56 seat outputs/results. The stale round-55 missing-receipt statement is preserved as history with an appended correction; the two first-composition receipts were recovered byte-exactly.
- The round-55 append-only deletion (33 lines) was restored byte-exactly; the final audit reports that event restored. Audit outcome and residual historical issues are below and in `corpus/lessons/round-56.md`.
- Neighbor scan (Q06) found kaidoku owns adjacent local model-serving/endpoint-health work; it found no duplicated LD_AUDIT audit claim. No sibling source or fleet tool was edited.
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` found only `.scratch/closure-mado-r50.json`, `.ufo/reports/round-76/kotoba.md`, `.ufo/waves/round-75/`, and `kotoba-shokukin/`; a content search for `kama|round-56|kama-r56` found no matches. No files were moved or deleted. S01 reported only `.git/index` stat-cache and one jj snapshot metadata side effect (no content/ref change); it also found X03 `/tmp` artifacts. I removed `/tmp/x`, `/tmp/x.out`, `/tmp/gs.out`, `/tmp/gc.out`, then removed `/fast/scratch/hyaku/kama-r56/` after landing.
- Broader operability routes not claimed remain planned: host-library package-byte provenance/count, fully config-hermetic Git environment, and attribute-free archive extraction. No capability was added.

## Landed changes

Every item is tied to `LOG.md` §Round 56, landed in commit `dd690b1c73d7e2af925095ea291e182b4e32adfc`; follow-up bytes/evidence are preserved in the subsequent commits listed here.

- Freeze and controls: `efc6b3ec6fb6ea308c15855e9b8b62856f4255b7`.
- Wave outputs and 305-file round-55 late-artifact sweep: `750e76b9363bfc679fdf134340675c3c925772b6`.
- Counter/battery implementation and frozen-claim measurements: `b9d5a091d25676e6c5078d330ebd6abd21a4fc7d`.
- Round-56 LOG/SCORECARD/lesson, no-op result and final wave receipts: `dd690b1c73d7e2af925095ea291e182b4e32adfc`.
- Exact lesson recovery: `7ff24f78ae2578174a0dde8e5887f5398783bf11`, then `14da0e4e55559bd8d891ba2cc0d39e5d9dd71fcf`; append-only correction history and audit receipts: `784d02551b2b3f18b3741555ab43d184d0040182` and final `6e706d1532bd0c3ea2036e471dff11cb350ddcbb`.

## Before → after measurements

- **C1 — operability 8→8 (verified within the frozen synthetic-child scope).** Command: `python3 tools/round56-env-leg-battery.py`; measured implementation commit `b9d5a091d25676e6c5078d330ebd6abd21a4fc7d`, base `e10b6d39af450e8d652be9ac2986768b531fe13f`. Before/old counter: `ld_audit=missed`, exit 0. After: `ld_audit=detected`, exit 0. Deleting `LD_AUDIT` from `BAD_ENV` misses; the mutant observation exits 0 but the positive-target assertion exits 1. The exact comparator rejects `expected=detected field=undetected` (`accepted=False`). Frozen counter SHA-256: `fc3d4b63a3020cf37e6f4080e25c9d693a8b177c4f84cae6688b2e445444ff6f`. Receipts: `.ufo/waves/round-56/controls/base-c1.out` and `.ufo/waves/round-56/measured/{base-c1,build-c1,m-drop-ldaudit,m-drop-ldaudit-target-fails,comparator-selftest}.out`. Limit: a variable-name rejection in a synthetic child, not successful audit-DSO injection, live endpoint health, or model-server readiness.
- **C2 — claimed calibration 7→7; not admitted.** Command: `python3 tools/round56-prereg-check.py --repo <lane clone> --tip b9d5a091d25676e6c5078d330ebd6abd21a4fc7d`; base `e10b6d39`: `present=0 roster_match=0 met=False`, exit 1; measured tip `b9d5a091`: `present=1 roster_match=1 kills=1 controls=2 met=True`, exit 0. Frozen checker SHA-256: `c7b0d787f348691bbc057114b455545f5abfb0c70ec497e1ad695591f1489853`. But the do-nothing fixture at `e6417941404e7f03a48df7ed955d2746fa3ca96f`—same ROSTER literal, no executed entries—also yields `present=1 roster_match=1 kills=1 controls=2 met=True`, exit 0 (`c2-noop-control.out`). The target is reachable without the claimed work, and the counter does not count SCORECARD/SHONEN mismatches as §9 requires. No post-data predicate change is claimed as a fix; no axis score changed.

## Sources & frontier

The census command was `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kama`.

- Before: exit 0; 252 rows; tiers A/B/C 239/9/4; statuses mined/queued/rejected 228/8/16. Complete 99-line stdout is committed verbatim at [start.out](../../../kama-shokunin/.ufo/waves/round-56/census/start.out) (97 W04, 1 W01, final `ok`).
- After: exit 0; 256 rows; tiers A/B/C 242/10/4; statuses mined/queued/rejected 231/8/17. Complete 102-line stdout is committed verbatim at [end.out](../../../kama-shokunin/.ufo/waves/round-56/census/end.out) (100 W04, 1 W01, final `ok`); exit receipt `.ufo/waves/round-56/census/end.exit`.
- Added: tier A=3 (S512, S513, S514), tier B=1 (S515); status mined=3, rejected=1. Existing row touched: S512 `used-by` old `corpus/lessons/round-56.md` → new `corpus/lessons/round-56.md, tools/round56-replay-code-audit.py`; no existing status/recheck cell changed. S514/S515 are append-only superseding revisions for S510/S511. Frontier rows advanced: none.
- S512 was opened live from `rtld-audit(7)` and grounds the LD_AUDIT variable-name surface; its ≤25-word located quote and use are in `corpus/lessons/round-56.md` §Gate. S513 (`ld.so(8)`) was rejected as overlapping the dedicated source, with a flip condition. S514/S515 were also opened live and their Gate entries record URL, date, located quotes and why they supersede the omitted revision facts.
- Assimilation: none. `considerthese/2026-10-26.md` proposal 4 remains pending; no proposal was edited.

## Trend verdicts

- **Expansion — unchanged.** No knowledge entry or capability was admitted; S512–S515 are curated source rows, not expansion credit (`CORPUS.md` rule 4).
- **Quality — improved.** The C1 classifier now detects LD_AUDIT; the exact-field negative control catches the `undetected` substring false positive; sourced corrections and append-only recovery are recorded. This does not credit C2 or imply endpoint-health coverage.
- **Discernment — unchanged.** No outside non-author admit/reject spot-check of this round is filed. Dispatched reviewers/critics are lane seats, not outside judgment; independent closure remains required.

## SHONEN

- [~] Decision tables, error signatures, checklist and sources — author assertion in `SKILL.md` §§Decision table, Error signatures, Checklist; no named non-author verifier.
- [~] End-to-end domain task logged — `LOG.md` §§round 1–3, 16 and 56; round-16 live receipt remains narrowly scoped; no named non-author verifier.
- [~] Instructions executable without oral context — `SKILL.md` §Checklist and `corpus/knowledge/snapshot-history.md` §Run it; independent execution review remains open.
- [~] No cross-domain bleed — `PROVINCE.md` §Write boundary and `corpus/knowledge/cross-lane-scope.md`; Q06 boundary scan recorded above; no independent verifier.

Stale-lane: respawn-per-round; no other mission of this lane is open.

## Audit, open decisions, and tooling

- Final append-only audit: `python3 tools/append-only-audit.py --repo <isolated scratch clone> --to 6e706d1532bd0c3ea2036e471dff11cb350ddcbb --json`, exit 1. Summary: `commits=382 files=106 events=126 restored=75 partial=0 unrestored=2 ungraded=44 disclosed=5 permitted_lines=60 disclosed_lines=10 bad_disclosures=0 ungraded_lines=227 regressed=0 vanished=0 unmatched=0 binary=0 bad_declarations=4`. The round-55 lesson event `c2c05e30` is restored 33/33. The only unrestored events are inherited SCORECARD head rederivations `e81d90e6` and `4bd7521a`, each with one graded line; four invalid `declared_at` bindings are detailed in `corpus/lessons/round-56.md` §Append-only audit closure and receipts `.ufo/waves/round-56/measured/append-only-audit-at-{14da,784}.out`. No round-56-origin event remains unrestored; audit exit 1 is not presented as a pass.
- Open L0s: `kama | round-35` asks which authority owns the lane axis pair (MISSION says operability+freshness; prompt/config/SCORECARD say operability+calibration); `kama | round-54` forwards the still-open `ed135b3c` craft-hours reversion ruling (with round-53 wording correction). Neither was edited or silently answered.
- Tool installs/upgrades: none. `/home/vgpnk/.omp/agent/RULES.md` was read; pacman remained paused.
- Admission: C1 is verified only within its named scope; C2 is unadmitted because the frozen counter is no-op reachable, does not meet §9 calibration evidence, and uses an axis that conflicts with MISSION. No scalar score or capability changed; independent non-author closure and operator ruling remain outstanding.

## Census stdout (verbatim)

The complete census outputs are included below; both commands exited 0.

### Before — exit 0 (`start.out`, 99 lines)

```text
kama	W04	S031 duplicate url docs.ollama.com/api/tags across scopes
kama	W04	S043 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server.cpp across scopes
kama	W04	S056 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/common/arg.cpp across scopes
kama	W04	S060 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-context.cpp across scopes
kama	W04	S064 duplicate url docs.python.org/3.14/library/subprocess.html across scopes
kama	W04	S065 duplicate url docs.python.org/3.14/library/sys.html across scopes
kama	W04	S067 duplicate url man7.org/linux/man-pages/man8/ld.so.8.html across scopes
kama	W04	S071 duplicate url git-scm.com/docs/git-cat-file across scopes
kama	W04	S077 duplicate url docs.python.org/3.14/library/os.html across scopes
kama	W04	S078 duplicate url man7.org/linux/man-pages/man8/ldconfig.8.html across scopes
kama	W04	S079 duplicate url man7.org/linux/man-pages/man8/ld.so.8.html across scopes
kama	W04	S080 duplicate url nix.dev/manual/nix/2.34/protocols/nix-archive across scopes
kama	W04	S081 duplicate url go.googlesource.com/mod/+/refs/tags/v0.42.0/sumdb/dirhash/hash.go across scopes
kama	W04	S082 duplicate url git-scm.com/docs/gitrevisions across scopes
kama	W04	S083 duplicate url git-scm.com/docs/git-cat-file across scopes
kama	W04	S084 duplicate url docs.jj-vcs.dev/latest/cli-reference across scopes
kama	W04	S085 duplicate url git-scm.com/docs/git-log across scopes
kama	W04	S086 duplicate url tldp.org/HOWTO/Program-Library-HOWTO/shared-libraries.html across scopes
kama	W04	S087 duplicate url docs.python.org/3.14/builtins/functions.html across scopes
kama	W04	S088 duplicate url docs.python.org/3.14/library/os.html across scopes
kama	W04	S093 duplicate url git-scm.com/docs/git-log across scopes
kama	W04	S097 duplicate url docs.python.org/3.14/library/subprocess.html across scopes
kama	W04	S100 duplicate url git-scm.com/docs/git-config across scopes
kama	W04	S103 duplicate url git-scm.com/docs/partial-clone across scopes
kama	W04	S105 duplicate url docs.python.org/3.14/builtins/stdtypes.html across scopes
kama	W04	S108 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server.cpp across scopes
kama	W04	S109 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-context.cpp across scopes
kama	W04	S110 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/common/arg.cpp across scopes
kama	W04	S112 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/README.md across scopes
kama	W04	S114 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-context.cpp across scopes
kama	W04	S115 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-context.cpp across scopes
kama	W04	S116 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-context.cpp across scopes
kama	W04	S117 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-context.cpp across scopes
kama	W04	S118 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-context.cpp across scopes
kama	W04	S119 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-context.cpp across scopes
kama	W04	S120 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-context.cpp across scopes
kama	W04	S121 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-context.cpp across scopes
kama	W04	S122 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-context.cpp across scopes
kama	W04	S123 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-context.cpp across scopes
kama	W04	S124 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-context.cpp across scopes
kama	W04	S125 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-context.cpp across scopes
kama	W04	S127 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-common.cpp across scopes
kama	W04	S129 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/ggml/src/gguf.cpp across scopes
kama	W04	S130 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/src/llama-context.cpp across scopes
kama	W04	S131 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/common/fit.cpp across scopes
kama	W04	S132 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/src/llama-context.cpp across scopes
kama	W04	S133 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-context.cpp across scopes
kama	W04	S134 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/README.md across scopes
kama	W04	S135 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/src/llama-kv-cache.cpp across scopes
kama	W04	S137 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-common.cpp across scopes
kama	W04	S141 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-schema.cpp across scopes
kama	W04	S142 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-schema.cpp across scopes
kama	W04	S143 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-schema.cpp across scopes
kama	W04	S144 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-schema.cpp across scopes
kama	W04	S145 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-schema.cpp across scopes
kama	W04	S146 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-schema.cpp across scopes
kama	W04	S147 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-schema.cpp across scopes
kama	W04	S148 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-schema.cpp across scopes
kama	W04	S149 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-schema.cpp across scopes
kama	W04	S150 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-schema.cpp across scopes
kama	W04	S151 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-schema.cpp across scopes
kama	W04	S152 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-schema.cpp across scopes
kama	W04	S153 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-schema.cpp across scopes
kama	W04	S154 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-schema.cpp across scopes
kama	W04	S155 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-schema.cpp across scopes
kama	W04	S156 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-schema.cpp across scopes
kama	W04	S157 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-schema.cpp across scopes
kama	W04	S158 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-schema.cpp across scopes
kama	W04	S159 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-schema.cpp across scopes
kama	W04	S160 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-schema.cpp across scopes
kama	W04	S161 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-schema.cpp across scopes
kama	W04	S162 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-schema.cpp across scopes
kama	W04	S163 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-schema.cpp across scopes
kama	W04	S164 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-schema.cpp across scopes
kama	W04	S165 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-schema.cpp across scopes
kama	W04	S166 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-schema.cpp across scopes
kama	W04	S167 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-schema.cpp across scopes
kama	W04	S168 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-schema.cpp across scopes
kama	W04	S169 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-schema.cpp across scopes
kama	W04	S170 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-schema.cpp across scopes
kama	W04	S171 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-schema.cpp across scopes
kama	W04	S172 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-schema.cpp across scopes
kama	W04	S173 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-schema.cpp across scopes
kama	W04	S181 duplicate url raw.githubusercontent.com/ggml-org/llama.cpp/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-common.cpp across scopes
kama	W04	S182 duplicate url raw.githubusercontent.com/ggml-org/llama.cpp/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-common.cpp across scopes
kama	W04	S183 duplicate url raw.githubusercontent.com/ggml-org/llama.cpp/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-common.cpp across scopes
kama	W04	S184 duplicate url raw.githubusercontent.com/ggml-org/llama.cpp/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-common.cpp across scopes
kama	W04	S185 duplicate url raw.githubusercontent.com/ggml-org/llama.cpp/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-common.cpp across scopes
kama	W04	S186 duplicate url raw.githubusercontent.com/ggml-org/llama.cpp/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-common.cpp across scopes
kama	W04	S187 duplicate url raw.githubusercontent.com/ggml-org/llama.cpp/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-common.cpp across scopes
kama	W04	S188 duplicate url raw.githubusercontent.com/ggml-org/llama.cpp/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-common.cpp across scopes
kama	W04	S189 duplicate url raw.githubusercontent.com/ggml-org/llama.cpp/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-common.cpp across scopes
kama	W04	S191 duplicate url raw.githubusercontent.com/ggml-org/llama.cpp/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-schema.cpp across scopes
kama	W01	S481 tierC mined used-by=corpus/knowledge/runtime-health-surface-processes.md, corpus/lessons/round-43.md, corpus/knowledge/runtime-health-surface-matrix.md, corpus/knowledge/endpoint-health-probe-conventions.md, corpus/knowledge/served-model-id-resolution.md, corpus/knowledge/engine-pin-watch.md
kama	W04	S499 duplicate url man7.org/linux/man-pages/man5/proc_pid_exe.5.html across scopes
kama	W04	S509 duplicate url raw.githubusercontent.com/ggml-org/llama.cpp/b11909/ggml/src/ggml-backend-reg.cpp across scopes
kama	W04	S510 duplicate url git-scm.com/docs/git across scopes
kama	W04	S511 duplicate url git-scm.com/docs/git-config across scopes
kama	ok	/home/vgpnk/Projects/shokunin/kama-shokunin/corpus/SOURCES.md
```

### After — exit 0 (`end.out`, 102 lines)

```text
kama	W04	S031 duplicate url docs.ollama.com/api/tags across scopes
kama	W04	S043 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server.cpp across scopes
kama	W04	S056 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/common/arg.cpp across scopes
kama	W04	S060 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-context.cpp across scopes
kama	W04	S064 duplicate url docs.python.org/3.14/library/subprocess.html across scopes
kama	W04	S065 duplicate url docs.python.org/3.14/library/sys.html across scopes
kama	W04	S067 duplicate url man7.org/linux/man-pages/man8/ld.so.8.html across scopes
kama	W04	S071 duplicate url git-scm.com/docs/git-cat-file across scopes
kama	W04	S077 duplicate url docs.python.org/3.14/library/os.html across scopes
kama	W04	S078 duplicate url man7.org/linux/man-pages/man8/ldconfig.8.html across scopes
kama	W04	S079 duplicate url man7.org/linux/man-pages/man8/ld.so.8.html across scopes
kama	W04	S080 duplicate url nix.dev/manual/nix/2.34/protocols/nix-archive across scopes
kama	W04	S081 duplicate url go.googlesource.com/mod/+/refs/tags/v0.42.0/sumdb/dirhash/hash.go across scopes
kama	W04	S082 duplicate url git-scm.com/docs/gitrevisions across scopes
kama	W04	S083 duplicate url git-scm.com/docs/git-cat-file across scopes
kama	W04	S084 duplicate url docs.jj-vcs.dev/latest/cli-reference across scopes
kama	W04	S085 duplicate url git-scm.com/docs/git-log across scopes
kama	W04	S086 duplicate url tldp.org/HOWTO/Program-Library-HOWTO/shared-libraries.html across scopes
kama	W04	S087 duplicate url docs.python.org/3.14/builtins/functions.html across scopes
kama	W04	S088 duplicate url docs.python.org/3.14/library/os.html across scopes
kama	W04	S093 duplicate url git-scm.com/docs/git-log across scopes
kama	W04	S097 duplicate url docs.python.org/3.14/library/subprocess.html across scopes
kama	W04	S100 duplicate url git-scm.com/docs/git-config across scopes
kama	W04	S103 duplicate url git-scm.com/docs/partial-clone across scopes
kama	W04	S105 duplicate url docs.python.org/3.14/builtins/stdtypes.html across scopes
kama	W04	S108 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server.cpp across scopes
kama	W04	S109 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-context.cpp across scopes
kama	W04	S110 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/common/arg.cpp across scopes
kama	W04	S112 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/README.md across scopes
kama	W04	S114 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-context.cpp across scopes
kama	W04	S115 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-context.cpp across scopes
kama	W04	S116 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-context.cpp across scopes
kama	W04	S117 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-context.cpp across scopes
kama	W04	S118 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-context.cpp across scopes
kama	W04	S119 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-context.cpp across scopes
kama	W04	S120 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-context.cpp across scopes
kama	W04	S121 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-context.cpp across scopes
kama	W04	S122 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-context.cpp across scopes
kama	W04	S123 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-context.cpp across scopes
kama	W04	S124 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-context.cpp across scopes
kama	W04	S125 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-context.cpp across scopes
kama	W04	S127 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-common.cpp across scopes
kama	W04	S129 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/ggml/src/gguf.cpp across scopes
kama	W04	S130 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/src/llama-context.cpp across scopes
kama	W04	S131 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/common/fit.cpp across scopes
kama	W04	S132 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/src/llama-context.cpp across scopes
kama	W04	S133 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-context.cpp across scopes
kama	W04	S134 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/README.md across scopes
kama	W04	S135 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/src/llama-kv-cache.cpp across scopes
kama	W04	S137 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-common.cpp across scopes
kama	W04	S141 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-schema.cpp across scopes
kama	W04	S142 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-schema.cpp across scopes
kama	W04	S143 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-schema.cpp across scopes
kama	W04	S144 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-schema.cpp across scopes
kama	W04	S145 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-schema.cpp across scopes
kama	W04	S146 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-schema.cpp across scopes
kama	W04	S147 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-schema.cpp across scopes
kama	W04	S148 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-schema.cpp across scopes
kama	W04	S149 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-schema.cpp across scopes
kama	W04	S150 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-schema.cpp across scopes
kama	W04	S151 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-schema.cpp across scopes
kama	W04	S152 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-schema.cpp across scopes
kama	W04	S153 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-schema.cpp across scopes
kama	W04	S154 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-schema.cpp across scopes
kama	W04	S155 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-schema.cpp across scopes
kama	W04	S156 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-schema.cpp across scopes
kama	W04	S157 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-schema.cpp across scopes
kama	W04	S158 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-schema.cpp across scopes
kama	W04	S159 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-schema.cpp across scopes
kama	W04	S160 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-schema.cpp across scopes
kama	W04	S161 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-schema.cpp across scopes
kama	W04	S162 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-schema.cpp across scopes
kama	W04	S163 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-schema.cpp across scopes
kama	W04	S164 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-schema.cpp across scopes
kama	W04	S165 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-schema.cpp across scopes
kama	W04	S166 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-schema.cpp across scopes
kama	W04	S167 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-schema.cpp across scopes
kama	W04	S168 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-schema.cpp across scopes
kama	W04	S169 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-schema.cpp across scopes
kama	W04	S170 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-schema.cpp across scopes
kama	W04	S171 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-schema.cpp across scopes
kama	W04	S172 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-schema.cpp across scopes
kama	W04	S173 duplicate url github.com/ggml-org/llama.cpp/blob/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-schema.cpp across scopes
kama	W04	S181 duplicate url raw.githubusercontent.com/ggml-org/llama.cpp/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-common.cpp across scopes
kama	W04	S182 duplicate url raw.githubusercontent.com/ggml-org/llama.cpp/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-common.cpp across scopes
kama	W04	S183 duplicate url raw.githubusercontent.com/ggml-org/llama.cpp/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-common.cpp across scopes
kama	W04	S184 duplicate url raw.githubusercontent.com/ggml-org/llama.cpp/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-common.cpp across scopes
kama	W04	S185 duplicate url raw.githubusercontent.com/ggml-org/llama.cpp/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-common.cpp across scopes
kama	W04	S186 duplicate url raw.githubusercontent.com/ggml-org/llama.cpp/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-common.cpp across scopes
kama	W04	S187 duplicate url raw.githubusercontent.com/ggml-org/llama.cpp/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-common.cpp across scopes
kama	W04	S188 duplicate url raw.githubusercontent.com/ggml-org/llama.cpp/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-common.cpp across scopes
kama	W04	S189 duplicate url raw.githubusercontent.com/ggml-org/llama.cpp/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-common.cpp across scopes
kama	W04	S191 duplicate url raw.githubusercontent.com/ggml-org/llama.cpp/704366d76f8748cf9ad3df62a464bfcc8d1ae6ad/tools/server/server-schema.cpp across scopes
kama	W01	S481 tierC mined used-by=corpus/knowledge/runtime-health-surface-processes.md, corpus/lessons/round-43.md, corpus/knowledge/runtime-health-surface-matrix.md, corpus/knowledge/endpoint-health-probe-conventions.md, corpus/knowledge/served-model-id-resolution.md, corpus/knowledge/engine-pin-watch.md
kama	W04	S499 duplicate url man7.org/linux/man-pages/man5/proc_pid_exe.5.html across scopes
kama	W04	S509 duplicate url raw.githubusercontent.com/ggml-org/llama.cpp/b11909/ggml/src/ggml-backend-reg.cpp across scopes
kama	W04	S510 duplicate url git-scm.com/docs/git across scopes
kama	W04	S511 duplicate url git-scm.com/docs/git-config across scopes
kama	W04	S513 duplicate url man7.org/linux/man-pages/man8/ld.so.8.html across scopes
kama	W04	S514 duplicate url git-scm.com/docs/git across scopes
kama	W04	S515 duplicate url git-scm.com/docs/git-config across scopes
kama	ok	/home/vgpnk/Projects/shokunin/kama-shokunin/corpus/SOURCES.md
```

