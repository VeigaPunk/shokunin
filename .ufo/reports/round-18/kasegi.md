# Kasegi Shokunin — Round 18

## Axis and move

- Starting scores: `depth:density=9`, `depth:verifiability=4`, `coverage=7`. Selected lowest axis: **depth:verifiability**.
- Planned move completed: triage the 46 `MISSING-FILE` anchors visible to the round-17 checker, re-anchor only exact surviving sources, and mark a historical source `[lost-tree]` only when no exact equivalent survives.
- Round-18 checker work also exposed 36 previously invisible bad anchors. The move therefore triaged the complete broadened pre-edit surface: 82 bad anchor instances, not only the old 46.
- Score remains **4→4**. Four exact anchors became openable and the lane-wide corrected resolver rate improved, but honest denominator expansion lowered the SKILL-only fraction. No score is awarded for relabelling unavailable sources.

## Before → after evidence

### Anchor gate

| state | in-range | bad | distinct anchors | LOST-RECORDED | ORIGIN |
|---|---:|---:|---:|---:|---:|
| r17 matcher, pre-edit SKILL | 196 | 46 | 162 | 5 | 1 |
| broadened r18 matcher, same pre-edit bytes | 205 | 82 | 171 | 5 | 1 |
| final | **209** | **0** | **175** | **104** | **5** |

Final `PIN-BROKEN=0` and `OUTSIDE-BASE=0`. Every live corpus file in `corpus/README.md` and `corpus/knowledge/*.md` also returns zero `MISSING-FILE`, `PAST-EOF`, `OUTSIDE-BASE`, and `PIN-BROKEN`. Pre-round-16 `corpus/lessons/*.md` retain historical bad anchors under `corpus/knowledge/citation-bases.md` rule 6; they were not rewritten as if re-verified now.

The matcher had two observability defects: `strip('.,;:')` removed the leading dot from `.ufo/...` and `.omp/...`, and the CITE regex omitted lane-prefixed anchors plus `csv`, `jsonl`, `rst`, `txt`, `py`, and `ts`. `anchorcheck.py` now preserves leading dots, recognizes those forms, supports explicit `~/Projects/the-bounty-hunter/` anchors, confines origin and mirror realpaths to their configured roots, and names the correct root in traversal diagnostics.

### Resolver rate

Round 18 found two defects in `resolve.py`: it ingested its own generated `citation-survival.md`, and it also stripped leading dots. The instrument now excludes its generated report and strips trailing prose punctuation only. Its generated header names the committed instrument rather than deleted `/tmp/kasegi-r15/resolve.py`.

A complete scratch copy of the lane was overlaid with the executor's exact pre-edit SKILL/corpus Markdown snapshot. Both sides were then measured with the corrected instrument:

| scope | before | after | change |
|---|---:|---:|---:|
| SKILL | 228/488 = **46.72%** | 232/503 = **46.12%** | −0.60 pp; +4 openable tokens |
| corpus | 246/1145 = **21.48%** | 247/1144 = **21.59%** | +0.11 pp |
| lane | 427/1461 = **29.23%** | 432/1469 = **29.41%** | +0.18 pp |

Two consecutive final runs produced byte-identical stdout, Markdown, and TSV. Final census SHA-256: `4d3874706d7fd31a0fa9bcdde88ca2f531f12eb6abeca6798732f7c4bef5d46a` (Markdown), `95c6a2328a8ff35336470f843c17a797a4b2078e1c7313c04cc383be5b4602e4` (TSV).

The round-17 narrative's `480/1506` was also corrected: the unchanged old instrument reproduced `451/1506` = 107 RESOLVES + 224 MIRROR-EQUIVALENT + 120 INTERNAL. Its denominator and `222/486` SKILL row matched, so 480 was a transcription error rather than source drift.

### Non-target density guard

`density.py` remained unchanged. SKILL mean moved **152.9→153.9** and path-citation instances **623→645**, largely because ambiguous shorthand became explicit historical paths. No density credit is claimed.

## Triage and provenance

- Of the original 16 distinct `MISSING-FILE` paths, 15 are absent from the lane, frozen mirror, origin-work root, and the surviving repositories' Git histories. Only `queue.json` has an exact surviving counterpart.
- Across the broadened surface, the independent executor map classified 79 anchor instances as absent from all three declared bases. Context-explicit bare Pendle, Yahoo, 3CX, and WordPress citations were expanded to full historical paths and marked `[lost-tree]`.
- Name collisions were rejected after content reads. The mirror's `docs/example-claim-ready-index.md` is a 14-line, seven-row, 2026-09-05 generator output, not the cited 32+ line, 11-row, 2026-09-06 file. Groknight `WRAP.md`, packet completeness checklists, and origin-work reconciliation files are different artifacts.
- The stale quoted target-tree text `README.rst:706` has no retained source base. It was de-anchored while preserving the missing-base caveat, rather than mislabelled LOST-TREE.
- Four exact ORIGIN-WORK anchors now open and semantically support the receipt/no-resubmit claim:
  - `submission-receipts.csv:2`
  - `submission-receipts.csv:3`
  - `receipts/ld-node-stream-tls-bypass.json:5-6`
  - `queue.json:11-12`
- Those files are current, git-untracked bytes in the mutable origin-work tree. They are not durable pins. SHA-256 evidence: CSV `3ed3e6959fc9b005630461c93045f5a2887d64f3d436c69549e87c024ffb80b9`; queue `1fa7cb8b1aab2a74a214fc511e0393b72265cbeef023129a1a80365c5f1f676d`; LaunchDarkly receipt `49525f86053003af053a6ed7a56c1176777682a339bd1ba651189854dab3ce2e`.

The province remains bounty/security research. The deleted `~/Projects/bounties` root was not silently re-scoped; external roots were read-only and no network, credential, target, submission, or disclosure action occurred.

## Behavioral verification

- Full SKILL smoke: `python3 corpus/instruments/anchorcheck.py SKILL.md` → `209` in-range, `0` bad, `175` distinct, `LOST-RECORDED=104`, `ORIGIN=5`.
- Live corpus sweep: `corpus/README.md` plus every `corpus/knowledge/*.md` → zero bad anchors.
- Nine-case throwaway fixture: valid lane, `.omp` mirror, explicit mirror, origin CSV, and LOST-RECORDED cases; invalid MISSING-FILE, PAST-EOF, origin traversal, and mirror traversal cases. It caught the wrong-root mirror traversal diagnostic before the repair and passed afterward.
- Resolver smoke: corrected pre-edit scratch run, final run, then an unchanged repeat; final counts `distinct=1469 resolves=81 mirror=229 internal=122 gone=1037`, and both final output passes were byte-identical.
- Syntax smoke: Python AST parse succeeded for both changed instruments.
- Final SHA-256: `SKILL.md` `62582f91770bb8a3ad208a861ad735b9c052c635f84c18ab678413089bd3ec7d`; `anchorcheck.py` `443ff50f62f823977660d7d688f5070acaae1bf973f34b4be59ee84a05fe02e0`; `resolve.py` `b44247e1eeb192d23f9de9d92a38a031280b091b544532dad3999755ccbafee4`.

No permanent test was added: the behavioral matrix is a throwaway `/tmp` fixture, while the committed deterministic instruments and generated census are the repeatable checks.

## L2 review

Nine L2 agents were dispatched in one batched call: two scouts, critic, reviewer, revenger, executor, connector, labrat, and sentinel. All returned read-only reports under `/tmp/kasegi-r18/`.

- Census scout re-derived the 16-path missing set and exact-survivor boundary.
- Invisible-token scout found the leading-dot bug and the omitted anchored path families.
- Critic searched both survivor histories and rejected all proposed name-only equivalents; it also rejected a score increase.
- Reviewer read the four origin ranges and confirmed their semantics while flagging the files as untracked/current-byte evidence.
- Revenger reconstructed context-explicit bare names without expanding generic type mentions.
- Executor preserved the exact pre-edit Markdown snapshot and produced an independent 79-anchor edit map.
- Connector searched sibling surfaces and found no duplicate of the lost source artifacts.
- Labrat captured the old resolver baseline and checker behavior.
- Sentinel attacked traversal, prefix, extension, and false-positive boundaries; its diagnostic concern was reproduced and repaired.

## Routing relay and frozen contract

Effective configuration shows `modelRoles.m_swe=devin/swe-2:max` and `retry.fallbackChains.m_swe=null`. Daybreak is visible only as separate roles; the operator's intended exact `m_swe → openai-codex/gpt-daybreak-blue-latest:max` fallback chain is **not visible**. No genuine m_swe capacity failure occurred, so no fallback advancement was observed. No failure was forced, no config was written, and the frozen mission contract was not altered.

## Commit scope and continuity

The lane had no commits after round 9 even though round-16 and round-17 work remained in the working tree. This round's lane commit intentionally carries that verified continuity:

- Round 16: completed citation-base vocabulary and live-document anchor normalization, including new `corpus/knowledge/citation-bases.md`.
- Round 17: ORIGIN-WORK checker support, corrected receipt range, score/log/report evidence.
- Round 18: SKILL triage, checker/resolver repairs, generated census, scorecard, instrument docs, live-corpus corrections, and this log evidence.

Lane receipt: commit `ed44a92` (`round-18`), 33 files, pushed
`b021dc9..ed44a92` to `VeigaPunk/kasegi-shokunin` `master`.

No `__pycache__` or `/tmp` artifact belongs in the commit. Domain source repositories remain unmodified by this lane.

## Next move

Round 19 candidate remains **depth:verifiability** (4 < coverage 7): audit the 104 `LOST-RECORDED` instances for semantic support in the corpus-attested record. Delete claims whose only support vanished; do not replace primary sources with circular corpus citations. Start with the critic-flagged Airtable severity/decree claim, whose surviving origin-work package materially differs.
