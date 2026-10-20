# Kama — round 16

Lane repo `kama-shokunin`, start `20e392ea683a36bc223eb7cb45897acfb45456a3`, pushed HEAD
`ccc4bb31267f061c1d3cc4099eb9fb46ed48d004` (measured revision
`726f737a942f1606d66e032f1efbcbb6f689ccf1`). Hyaku phase 2, attempt 1; no
`lane-dead-no-report kama round=16` line, clean start tree, nothing inherited.

## Work performed

Declared claims (assignment operability + calibration, `shokunin.conf:52`; calibration 7 is the
lowest axis, no stagnation waiver):

- **C1 — calibration (lowest axis):** the probe graded a loading llama.cpp server
  `FOREIGN_SERVICE` / "non-2xx HTTP from a non-model service" (since round 1, `c6199a2`).
  It now grades the exact envelope `MODEL_LOADING` / `llamacpp-loading`, and every lane
  document that called the vocabulary fixed or the state foreign gets an appended correction.
- **C2 — operability, capability acquisition `live-llamacpp-lifecycle`:** a lane-owned,
  ephemeral llama.cpp b11755 run on an unregistered loopback port, with a receipt gate.

Work items:

- Smoke and premise check: a real b11755 server answered `GET /v1/models` with
  `503 {"error":{"message":"Loading model","type":"unavailable_error","code":503}}` while
  loading; the frozen probe graded a stub of that body `FOREIGN_SERVICE` exit 2 (`LOG.md`
  §round 16, first entry).
- Probe repair: `tools/kama-probe.sh` `body_is_llamacpp_loading()` and the 503 branch
  (exact message/type, integer code 503; python3 required, else fail closed), vocabulary,
  `listeners` counter and `diff_baseline` whitelist (commits `b8e485c`, `726f737`).
- Stub matrix and harness: `tests/probe-verdicts/check.py` + 9 literal families, 72 rows,
  17 `MODEL_LOADING`; counting command `.ufo/waves/round-16/measure.py` with frozen-snapshot
  verification, directional set equality, pinned matrix digest and counts.
- Doc-side ledger `.ufo/waves/round-16/stale-statements.py` (17 stale lane statements) and the
  corrections it checks: `corpus/knowledge/{endpoint-identity,consumer-registry,listener-census,served-identity-crosswalk,runtime-health-surface-matrix,snapshot-history}.md`,
  `SKILL.md` §Round-16 (lines 507-553), `corpus/README.md` round-16 section,
  `registry/endpoint-consumers.tsv:32`.
- Criterion `corpus/QUALITY.md` KQ19 (lines 100-109).
- Live capability: `tools/kama-llamacpp-live.py` (env allowlist, `--offline`, port refusal,
  child-owned listener before any capture, keep-alive `/v1/models` polling for the loading
  window, process-group teardown, receipt with tool/probe/install-tree digests) and gate
  `tests/llamacpp-live/check-receipt.py` (26-mutation selftest); receipts
  `.ufo/waves/round-16/live/{receipt,receipt-frozen-probe}.json`, controls
  `live/controls.txt`, captured-503 replay `live/replay-captured-503.{py,txt}`.
- Knowledge entry `corpus/knowledge/llamacpp-loading-lifecycle.md`; lesson
  `corpus/lessons/round-16.md`; SOURCES S035-S041; SKILL/README/PROVINCE/SHONEN/SCORECARD/LOG
  appends.
- Round-15 outside check (`corpus/lessons/round-15-verifier-spotcheck.md`): all five sampled
  decisions agreed, so no disagreement criterion is owed; routed defects 1-6 dispositioned in
  `corpus/lessons/round-16.md` §Routed defects (5: replay prose appended; 6: S012 note; 4:
  dispatch provenance recorded with environment bindings for both waves).
- Waves (validated under policy v2, one `task` call each, taskCall unchanged):
  - build: 81 seats — executor 16, scout 20, reviewer 14, critic 6, sentinel 2, connector 8,
    revenger 4, scribe 10, simplifier 1; 81 completed, 0 dead
    (`.ufo/waves/round-16/build/{spec,dispatch,validation,assignments,completion-summary}.json`).
  - falsify: 79 seats — reviewer 33, scout 10, executor 9, critic 8, connector 6,
    mutation-tester 4, revenger 3, scribe 3, sentinel 2, simplifier 1; 79 completed, 0 dead
    (`.ufo/waves/round-16/falsify/…`, `provenance-ledger.json`: argv, the three environment
    bindings, taskCall sha256 `72e81bc6…0812`, spawned attempt bound to it).
  - Round total 160 seats (≤ 200). Canonical planner seat: L1; bounded planning data-walk
    rode `RevengerPlannerWalk`. No refused task calls; no model parameter passed.
- Falsify-wave repairs (commit `726f737`): harness ownership proof at the first HTTP answer,
  loading capture, crash-safe receipt, no redirects; gate rebound to the producer's exact
  keys; measure breadth pin; two duplicate matrix rows replaced by rows pinning `code == 503`
  and the HTML body sniff; narrowed router/exit/OPTIONS/older-build wording. Remaining debt is
  named in the lesson §Falsify wave.
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` showed
  `.ufo/waves/round-16/falsify/advice/RevengerRunReceipts.md` (a kama seat's report); copied
  byte-exact into the lane (`cmp` ok, sha256 `993ac867…`), fleet copy and its empty dirs
  removed; recorded in the lesson (M4). `.ufo/state/kama.report-baseline` is driver state and
  was not touched. Seat `/tmp` scratch and three empty harness temp logs were removed.
- Process incidents (not evidence): a seat ran `measure.py` by accident and restored the
  receipts (M6); session-store traversals recurred in three seats (M7, none opened); several
  connector seats read beyond their file bound (M5). See lesson §Mistakes.

## Landed changes

| Change | LOG.md entry | Commit |
|---|---|---|
| `MODEL_LOADING` verdict, stub matrix + harness, measure command, live tool + gate, knowledge entry, corrections, KQ19, SOURCES S035-S041, SKILL/README/PROVINCE/SHONEN/SCORECARD appends | `## round 16 — loading-envelope verdict and live llama.cpp lifecycle (2026-10-20)` | `b8e485c` |
| Falsify-wave repairs: hardened harness and gate, breadth pin, matrix row swaps, doc-correction ledger, narrowed claims, pinned extra upstream sources | `## round 16 — committed measurement and bounded verdict (2026-10-20)` | `726f737` (measured) |
| Measured receipts (`acceptance.json`, run-*.json, live receipts, replay, census), lesson falsify dispositions, SCORECARD results + canonical capability list, LOG measured entry, falsify wave evidence | same entry | `ccc4bb3` |

All three commits carry `kama-shokunin <kama@shokunin.local>` and are pushed (`git status -sb`:
`## master...origin/master`). The operator commit `836b018` (considerthese) landed upstream
mid-round; the first push was rebased onto it, nothing of it edited.

## Before → after measurements

- **C1 (probe):** `python3 .ufo/waves/round-16/measure.py`, measured at `726f737`, exit 0.
  Frozen probe (sha256 `93ee4302…cd64` = blob `20e392e:tools/kama-probe.sh`): 72 rows,
  **55 pass / 17 fail** (exit 1) → current probe (`36b64978…`): **72 / 0** (exit 0). Changed
  verdicts = exactly the 17 `MODEL_LOADING` rows; matrix set sha256 `bf9068d8…1f32`, 72/17
  pinned (`.ufo/waves/round-16/measure-stdout.txt`, `run-before.json`, `run-after.json`).
- **C1 (docs):** `python3 .ufo/waves/round-16/stale-statements.py --rev REV`: **17 uncorrected
  at `20e392e` → 0 at HEAD** (`stale-before.txt`, `stale-after.txt`). Counts textual coverage
  only (KQ14); content was reviewed by falsify seats.
- **C1 no-harm:** `bash tools/test-snapshot.sh` `RESULT pass=30 fail=0` (was 24/0; the new
  cases fail 27/3 on the frozen probe); `check.py --selftest` 72/72 + 4/4 malformed rejected.
  Score: calibration **7 → 7**.
- **C2:** before: no lane tool could start a runtime (last real llama.cpp answer 2026-09-29,
  round 2). After, at `726f737`: `python3 tools/kama-llamacpp-live.py --server
  ~/.local/opt/llama-b11755/llama-server --model ~/.cache/kama-shokunin/models/stories260K.gguf
  --model-sha256 270cba1b…d256d --alias kama-stories260k --out …/live/receipt.json` → exit 0,
  **10/10 checks**; `check-receipt.py` with model/server/probe/tool pins → `VALID`;
  frozen-probe control 10/10 (separability); loading window captured live (38 exact-envelope
  503s on `/v1/models`), replayed as `MODEL_LOADING` (current) vs `FOREIGN_SERVICE` (frozen);
  controls: digest mismatch exit 3, ports 34113/8080/631 exit 2, no `llama-server` left.
  Score: operability **8 → 8**; capability row `live-llamacpp-lifecycle` (first-working round 16).

## Sources & frontier

Start (`.ufo/waves/round-16/sources-before-validate.txt`, `sources-before-census.txt`):

```text
$ /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kama
kama	W04	S031 duplicate url docs.ollama.com/api/tags across scopes
kama	ok	/home/vgpnk/Projects/shokunin/kama-shokunin/corpus/SOURCES.md
exit=0
rows 34, tier.A 31, tier.C 3, mined 24, queued 5, rejected 5
```

End (`sources-final-validate.txt`, `sources-final-census.txt`):

```text
$ /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kama
kama	W04	S031 duplicate url docs.ollama.com/api/tags across scopes
kama	ok	/home/vgpnk/Projects/shokunin/kama-shokunin/corpus/SOURCES.md
exit=0
rows 41, tier.A 38, tier.C 3, mined 31, queued 5, rejected 5
```

- Rows 34 → 41; added by tier: A +7 (S035 README @704366d76, S036 `server-http.cpp`, S037
  `server.cpp`, S038 release b11755, S039 HF fixture GGUF, S040 llm-d v0.10 superseding S021,
  S041 own-work live receipt), B +0, C +0. All seven opened this round; Gate quotes and URLs in
  `corpus/lessons/round-16.md` §Gate and §Gate locations.
- Rows touched old→new: S017 used-by `corpus/knowledge/runtime-health-surface-matrix.md` →
  same + `corpus/knowledge/llamacpp-loading-lifecycle.md`. S041 anchor/teaches amended
  before closure (row first committed this round). No earlier row's status/recheck changed;
  S021 stays queued, superseded by S040.
- Sourced claim: C1 rests on S036/S037 (opened this round); the knowledge entry cites them.
- Frontier advanced: "real-runtime proof for llama.cpp only, and stale" now has a re-runnable
  lane-owned sample on the current build. Still open: live probe grading during load (raw 503
  captured, verdict via replay), router mode and sleep (source only), other engines (leads,
  not rows), K05 context, registered consumers still `DEAD`.
- Mined mistake: M1 (the round-1 overreach), captured-by none, fix KQ19 + matrix shown able to
  fail (frozen 55/17).

## Trend verdicts

- **expansion — improved.** New knowledge entry on code-level loading behaviour
  (`corpus/knowledge/llamacpp-loading-lifecycle.md`, sourced S035-S041) and a demonstrated
  capability (`live-llamacpp-lifecycle`, receipt 10/10). Other-engine notes are labelled
  leads, not knowledge (KQ6).
- **quality — improved.** The round-11 reading that `/v1/models` answers 200 while loading was
  corrected against pinned code and a live capture; seven corpus files and SKILL corrected;
  stale-statement ledger 17 → 0.
- **discernment — unchanged.** No non-author admit/reject sample exists for round 16; all 160
  seats are lane-dispatched. Outside review pending.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources → `SKILL.md` §Round-16 (decision rows, error signature, four gate rows); no named non-author verifier.
- [~] At least one end-to-end domain task executed and logged in LOG.md → `LOG.md` §round 16 measured entry + `.ufo/waves/round-16/live/receipt.json` (10/10, pinned b11755 + 1.2 MB fixture, own alias); lane-owned control, not consumer reconciliation.
- [~] Instructions executable by an agent without oral context → `SKILL.md` §Round-16 registry rows (commands run as written per falsify seat `ReviewSkillSection.md`); no non-author execution review on record.
- [~] No cross-domain bleed (PROVINCE.md still accurate) → `PROVINCE.md` round-16 note (fixture exception pending L0); handoffs for kagi/kumitate/tsukuroi/souji advised in `.ufo/waves/round-16/falsify/advice/ConnectCrossLaneScope.md`, not absorbed.

Open L0 question: `kama | round-16 | Ratify or reject the lane-owned live llama.cpp fixture …`
(`.ufo/l0-questions.md`, appended this round): ratify the fixture exception, and keep or remove
the persistent install, PATH link and model cache. The round routes around it: the fixture runs
only inside steered rounds.

Tool installs (operator directive 2026-10-19; pacman paused, not used): llama.cpp **b11755**
(commit 704366d76, GitHub Pre-release), channel = official release asset
`llama-b11755-bin-ubuntu-x64.tar.gz` (sha256 `753bfa73…e226`, equal to the API digest)
extracted to `~/.local/opt/llama-b11755`, linked `~/.local/bin/llama-server`; reason C2. Model
`stories260K.gguf` (sha256 `270cba1b…d256d`) from Hugging Face `ggml-org/models-moved` into
`~/.cache/kama-shokunin/models/`. Seats reported no installs.

Stale-lane: respawn-per-round driver; no other kama mission is open.
