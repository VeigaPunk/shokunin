# UFO-FSD Connector Note — Aggregator Round 12

**Seat:** `KaikaAggregateR12.ConnectorRound12`  
**Date:** 2026-10-19  
**Execution Context:** `/home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/fleet-aggregate`  
**Target Surface:** 21 physical local lane repositories under `/home/vgpnk/Projects/shokunin/<repo>` (strictly READ-ONLY).  
**Single Permitted Write:** This unique scratch note under `.ufo/waves/kaika-aggregate/seats/connector.md`.  
**Status Banner:** All baseline totals and census numbers cited are PROVISIONAL pending parent's `FINAL LANES READY` signal and ongoing indented-row parser fix (`CensusIndentFix`). No numeric scores proposed or modified.

---

## 1. Evidence: Cross-Lane Patterns in Reading Paths and Limitation Language

Across the 17 child repositories carrying `corpus/SOURCES.md`, the canonical SOURCES contract in worktree `CORPUS.md` (`.ufo/waves/kaika/SOURCES-CONTRACT-v1.md`), the 4 named W1 art dossiers (`art-curation.md`, `art-learning.md`, `art-mistakes.md`, `art-apprenticeship.md`), and the round-12 seat scratch notes (`audit-lore.md`, `audit-souji.md`, `audit-audio.md`, `audit-game-dev-3d.md`, `audit-game-dev-2d.md`, `audit-tameshi.md`, `audit-kama.md`, `audit-kumitate.md`, `audit-kaidoku.md`, `audit-kengaku.md`, `audit-kake.md`, `source-count-reconciliation.md`, `planner.md`), the following recurring patterns and counterexamples were directly observed.

### 1.1 Reading-Path Organization (`## Paths`)

Contract v1 defines the shape as:
`## Paths — ordered study sequences: <topic> — S003 → S010 → S014: why this order`

Across the evaluated lanes, reading paths fall into three structural patterns:

#### Pattern A: Epistemic Inversion Sequences ("Normative Contract → Implementation Mechanics → Empirical Measurement → Boundary/Rejection")
In the strongest lanes, study paths are structured dialectically rather than as flat bibliographies. They move from normative standards down to runtime mechanics, then to lane-specific measurements, ending on negative boundaries or rejected counter-models:
- **`kotoba-shokunin`** (`corpus/SOURCES.md:28`): `S001 → S008 → S003 → S002 → S011`. Moves from normative open spec (S001) to YAML plain-scalar mechanics (S008), vendor rules (S003), client loader behavior (S002), and terminates on the rejected tutorial (S011) to demonstrate the taste rule it violates.
- **`game-dev-3d-shokunin`** (`corpus/SOURCES.md:48`): `S012 → S011 → S035`. Moves from public API contract (S012) to engine C++ source (S011) to the lane's own boundary-scan measurement (S035), directly exposing a documentation omission before measurement confirms it. Its second path (`S033 → S034 → S027 → S029 → S028 → S031 → S030`) terminates on the rejected LLM-agent testing paper (S030) as an oracle caution.
- **`souji-shokunin`** (`corpus/SOURCES.md:45, 46`): F1 moves from manual docs (S002, S001) to tagged C source (S009), worktree/repack controls (S003, S004), and release-drift tracking (S010, S011). F3 moves from failure modes (S017) to tagging original files (S016), tool caveats (S019, S018), and act-time verification code (S020, S021).
- **`revenger-shokunin`** (`corpus/SOURCES.md:35`): `S009 → S010 → S011 → S013`. Moves from PE format spec (S009) to Unicode UTF-16 conformance (S010), Python codecs behavior (S011), and terminates on a saved parser run that accepted an ill-formed surrogate (S013).
- **`chousa-shokunin`** (`corpus/SOURCES.md:32, 36`): `S008 → S002 → S004 → S003` ("Question first, authority last") and `S003 → S005 → S006 → S007 → S010` (tracing context, measuring hop-by-hop fidelity loss, separating relevance from support, and evaluating full retrieval context).
- **`kotodama-shokunin`** (`corpus/SOURCES.md:107`): `S041 → S031 → S033 → S032`. Moves from archaeological burial evidence (S041) to ethnographic sample (S031), authors' own correction (S033), and the counter-critique (S032).
- **`tabi-shokunin`** (`corpus/SOURCES.md:46`): `S002 → S001 → S004 → S003`. Moves from CDP support posture to published profile refusal, Chromium C++ branding gate, and testing build isolation.
- **`kake-shokunin`** (`corpus/SOURCES.md:30`): `S003 → S004 → S001 → S008 → S002 → S006`. Moves from publishing mode to artifact contract, pinned action YAML, GNU tar pattern matching, dotfile change changelog, and Jekyll contrast.

*Grounding:* This matches the methodology in `art-curation.md` D03 ("primary does not mean proven") and `art-apprenticeship.md` §Study paths (ordering from mechanism to measurement challenge to preregistered reanalysis to preserve disagreement rather than flatten it).

#### Pattern B: The Two-Phase Bifurcation (Mined Evidence vs. Queued Frontier Plan)
Paths frequently bridge from currently grounded knowledge into the frontier:
- In **`tameshi-shokunin`** (`audit-tameshi.md` §4; `corpus/SOURCES.md:59`): Path 1 (`S001 → S002 → S004 → S006 → S011 → S010 → S009 → S007`) has hops 1–4 `mined` (feeding `mutation-score-semantics.md` and `witness-scoped-kill-verdict.md`), while hops 5–8 are `queued` (unmined frontier plan). Paths 2 and 3 are 100% `queued`.
- In **`kama-shokunin`** (`audit-kama.md` §7; `corpus/SOURCES.md:46`): `S001 → S004 → S006 → S020 → S017 → S021`. Hops 1–5 are `mined` (feeding `runtime-health-surface-matrix.md`), while hop 6 (S021, llm-d probes) is `queued` ("external probe vocabulary last, not yet imported").
- In **`kengaku-shokunin`** (`audit-kengaku.md` §4; `corpus/SOURCES.md:52, 54`): `contamination audit` ends on S022 (`queued`), and `agentic evidence` includes S020 and S021 (`queued`).

#### Counterexamples in Reading Paths
1. **Linear Survey / Flat Catalogue (`kasegi-shokunin`)**:
   In `kasegi-shokunin/corpus/SOURCES.md:38`, the CVD path strings together 12 consecutive sources (`S003 → S004 → S005 → S018 → S019 → S020 → S021 → S022 → S023 → S024 → S016 → S017`) as an exhaustive policy-and-coordinator survey rather than a tight, pedagogical sequence.
2. **Explicit Frontier-Key Tagging (`tsukuroi-shokunin`)**:
   `tsukuroi-shokunin/corpus/SOURCES.md:44-46` explicitly ties each path to project milestones/frontier IDs: `Rollback net on this host (U1/J4)`, `Update gate without -Sy (U2)`, `Boot repair on busybox + LUKS + Limine UKI (U3/J3)`.
3. **Explicit Destination Anchoring (`tabi-shokunin`)**:
   `tabi-shokunin/corpus/SOURCES.md:46-48` ends every path with a mandatory terminal pointer: `Ends at knowledge/chrome-remote-debugging-profile-boundary.md`.
4. **Quarantine Decoupling (`lore-shokunin`)**:
   `lore-shokunin/corpus/SOURCES.md:48, 50` preserves the `In-world time` path as a valid study sequence even after its produced entry was rejected during orchestrator adjudication and quarantined to `.ufo/waves/round-103/rejected/...`. Lore explicitly notes: "The path stands as a study sequence only."
5. **Absent Registry Surface (`audio`, `game-dev-2d`, `kaidoku`, `kumitate`)**:
   At the audited committed HEADs, 4 of the 21 physical lanes have no `corpus/SOURCES.md` file at all (`source-count-reconciliation.md` §0). In `kumitate-shokunin`, the file exists on in-flight branch `kaika/round` (`0acb775`), where it defines 3 paths ("OMP delegation contract", "Kimi MCP plane", "Multi-agent design judgment").

---

### 1.2 Exact Limitation Language across Lanes

Across scopes, anchors, teaches, rejection reasons, and search logs, lanes converged on four distinct linguistic formulas to delimit claims:

#### Formula 1: "Does not establish / cannot alone evidence" (Separating Observation from State)
- **`mori-shokunin`**: S009 (`oomctl dump reports current contexts held by oomd without equating that state with a kill count`); S034 (`observes roster_source=conf+state, roster_n=23... it does not establish complete fleet-universe coverage`).
- **`tsukuroi-shokunin`**: S003 (`does not establish whether the incident remained active on 2026-10-19`); S013 (`does not by itself establish a safe rollback plan`); S016 (`code-level anchor, not evidence that every third-party hook was migrated`); S018 (`configuration is distinct from proof of a working rollback`); S022 (`code alone does not establish the impact of that path mismatch`).
- **`kama-shokunin`**: S011 (`availability is distinct from running state`); S016 (`reference list shape... does not establish local-server health or loaded weights`); S020 (`release note is not a local defect observation`); S023 (`example's scrape... is not evidence of monitoring installed on this host`); S027 (`request and user comments do not establish released API behavior`).
- **`game-dev-3d-shokunin`**: S004 (`Separates headless simulation and state checks from evidence that pixels were rendered`); S016 (`no_renderer... cannot evidence rendered pixels`); S023 (`validation report... as a format check, not as proof of engine import`); S032 (`release note is not general stability evidence`).
- **`lore-shokunin`**: S001 (`PROV entities may be imaginary, so a lore record can carry provenance without that provenance asserting canon`); S018 (`reproducible evidence of schema, citation and tick-order integrity only; it never certifies prose support, semantics or canon`); S019 (`byte integrity only, not semantics`).
- **`tabi-shokunin`**: S012 (`translation layer... proves no individual command`); S023 (`Role locators are user-facing semantic selectors and explicitly not an accessibility audit`); S024 (`structural evidence, not pixels`); S028 (`that this host's unbranded Chromium does not enforce it is an inference from source, never observed by a launch`).
- **`kake-shokunin`**: S009 (`says nothing about which server GitHub Pages runs`).
- **`revenger-shokunin`**: S006 (`defines hash behavior, not provenance or completeness`); S015 (`saved receipt hashes and Evidence IDs were rejected as proof of producer origin; they show internal consistency only`).

#### Formula 2: "Never sole support / never tier A" (Curation vs. Proof)
Enforced identically across `chousa` (S016, S018), `kengaku` (S026), `lore` (S027, S031), `mado` (S010), `kotoba` (S011), `kotodama` (line 19), `tameshi` (S046), and `revenger` (S012).

#### Formula 3: Claim-Scoped Authority ("Scoped to X only; not an assertion about Y")
- `chousa` S006: "the evaluation framework this preprint defines (its own dimensions), not its results about evaluated systems"; S007: "what this paper itself states... not its benchmark results".
- `kengaku` S005/S006: "what OpenAI reports about its own evaluation"; S002: "its own controlled reasoning-model contamination experiments".
- `kake` S009: "nginx's own ETag format only; not an assertion about the GitHub Pages backend".
- `lore` S004/S005: "ETCSL's English prose translation... (not the Sumerian original, not cultural fact; rights undetermined)"; "1913 secondary retelling; not the Popol Vuh text, not authority on K'iche' belief".
- `kotodama` S008/S009/S035: "conlang craft method (not linguistic evidence)"; "census of what conlangers build, never evidence of natural-language typology"; "bibliographic identity of the article only; its typology and wording are unread".

#### Formula 4: Canonical Rejection/Flip Syntax
Every conforming rejected row strictly obeys:
`REJECTED: <reason>; flip: <what would change the verdict>`
Observed in 43 rows across 12 lanes (`chousa` S014–S016; `kengaku` S003, S023, S026; `kake` S017, S018; `souji` S030, S032; `kama` S024, S026–S028, S030; `revenger` S008, S012; `lore` S015–S017; `kotoba` S011; `kotodama` S028–S030, S043, S047; `game-dev-3d` S010, S030; `tsukuroi` S029, S030, S033; `tameshi` S029, S030, S046).

#### Counterexamples and Anomalies in Limitation Language
1. **`kagi-shokunin` (Cell Bloat)**:
   In `kagi-shokunin/corpus/SOURCES.md`, kagi routinely appends `Quote: “...”` and `Fetch sha256: <hash>` into the `teaches` cell across almost every row (e.g. S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016). Contract v1 specifies that quote and fetch verification belong in the round lesson's `## Gate`, not inside the 11-column registry table.
2. **`mado-shokunin` (The Retrospective Rejection Trap)**:
   In `mado-shokunin/corpus/SOURCES.md:41`, row S030 has `status = rejected`, but its `teaches` cell remains `Current Lua window-rule syntax`, omitting `REJECTED: ...; flip: ...`. Mado's search log explicitly documents why: Rule 2 forbids in-place editing of `teaches`, so when the orchestrator spot-check rejected S030 post-review, mado could not add the rejection text to `teaches` without violating Rule 2.
3. **`tsukuroi-shokunin` (Rowing and Rejecting AI Tool Output)**:
   In `tsukuroi-shokunin/corpus/SOURCES.md:36, 39`, rows S030 and S033 row synthesized web_search answers from a prior ART dossier and the L1 seat, assign kind `tool`, and reject them explicitly with flip conditions (`asserted CAP_DAC_OVERRIDE despite S020 listing CAP_SYS_ADMIN`; `calls mode 555 a read-only mount`). Tsukuroi deliberately uses the registry as an epistemic firewall against AI hallucinations.

---

## 2. Contradictions Across Contract, Runtime, and Verification Surfaces

Tracing second-order effects reveals four explicit contradictions across the active corpus:

### Contradiction 1: Rule 2 Immutability vs. Rejected Row Shape Requirement
- **Contract Tension:** `CORPUS.md` lines 101–102 mandate that rejected rows read `REJECTED: <reason>; flip: <what would change the verdict>` in `teaches`. Simultaneously, Rule 2 (lines 116–118) dictates that only `status`, `recheck`, and `used-by` change in place, and corrections must be new rows opening `supersedes S0NN —`.
- **Observed Collision:** When a row opened as `queued` or `mined` is rejected upon later review or spot-check (e.g. `mado` S030), the lane faces an impossible choice:
  - Edit `teaches` in place → violates Rule 2 (append-only immutability).
  - Leave `teaches` unchanged and change only `status` → violates the Rejected row shape requirement (causing a gate/census form finding).
  - Append a new superseding row → causes duplicate-URL warnings (`W04` in `validate`) or errors (`E04`), as seen in `lore` (S012/S017) and `kotodama` (S044–S047).

### Contradiction 2: The Fleet-Wide `r10` Gate Asynchrony Trap
- **Contract vs. Gate Execution:** `corpus-gate.mjs` checks rule `r10` (`no corpus/lessons/round-<R>-aggregator-*.md`).
- **Observed Failure:** In every child lane audited by the round-12 seats (`lore`, `souji`, `tameshi`, `kama`, `kengaku`, `kake`, `kumitate`, `kaidoku`, `game-dev-3d`, `game-dev-2d`), `r10` fails under the lane's actual round (e.g. 12, 20, 24, 33, 103, 108).
- **The Catch-22:** CORPUS.md:53-56 and PROTOCOL.md:205-212 state that aggregator lessons are strictly *aggregator-authored* and *child repos are read-only to lanes during aggregate reviews*. A lane cannot create `round-<R>-aggregator-*.md` itself without violating ownership rules (CORPUS.md:53), but the gate marks the lane `failed` (exit 1) for its absence! When run under the gate's default `--round 9`, only the 6 historical round-9 lanes pass, while the other 15 lanes fail.

### Contradiction 3: The 1 GiB MaxBuffer Snapshot Failure on Large Repositories
- **Contract Requirement vs. Runtime Substrate:** The aggregator brief mandates running `.ufo/waves/round-9/corpus-gate.mjs --snapshot <lane> <exact-HEAD>`.
- **Observed Failure:** In `audio-shokunin` (`audit-audio.md` §2), `git archive defbe128...` produces 1.29 GiB (1,384,069,120 bytes), which exceeds Node's `spawnSync` `maxBuffer: 1 << 30` (1,073,741,824 bytes) at `corpus-gate.mjs:602`. The command aborts with exit 2 (`could-not-evaluate`).
- **Second-Order Effect:** The audit seat was forced to fall back to supplementary `--repo` mode (live grading), which reads working-tree files rather than the committed snapshot. Any lane whose archive exceeds 1 GiB will permanently fail `--snapshot`.

### Contradiction 4: Line-Local `r4` Check vs. Multi-Line Table/Prose Formatting
- **Contract Intent vs. Regex Implementation:** Rule 4 requires counts to carry reproducible commands (`<number> — <command> <date>`).
- **Observed Failure:** Across all audited lanes (`kengaku` 69, `kake` 52, `kaidoku` 82, `kumitate` 94, `tameshi` 81, `game-dev-3d` 29, `game-dev-2d` 16, `lore` 16, `kama` 12, `souji` 7), `r4` accounts for >85% of all gate findings.
- **Root Cause:** As proven by `audit-kengaku.md`, `audit-kake.md`, and `audit-kaidoku.md`, `corpus-gate.mjs:450-466` checks strictly line-by-line: any line containing a backtick is exempt; any line without a backtick that matches `COUNT_NOUN_RE` fails. Consequently:
  - Table headers like `quote (≤25 words)` fail (`lore` r4-16, `kake` r4-37, `tameshi` r4-81, `kengaku` r4-58).
  - Identifier/round names like `round-16 citation`, `round-1 entries`, `round-4 lane`, `18, run` fail (`kake`, `kaidoku`, `kengaku`, `game-dev-2d`).
  - Legitimate counts where the backticked command is in a fenced block 2 lines above or below fail (`kake` 33/52, `game-dev-3d` 17/29).

---

## 3. Affected Axes

1. **`corpus review` (Aggregator lane primary axis):**
   - **Improved.** The aggregator must not confuse mechanical regex artifacts (r4 line-local hits, r10 aggregator-asynchrony hits) or un-evaluated rules (r1, r3, r5, r6, r9) with semantic corpus quality. Formalizing the path typology and rejection lifecycle gives the aggregator an honest, evidence-based curation lens.
2. **`calibration` & `gate integrity`:**
   - **Improved.** Disentangles false gate failures from real defects. Replaces ambiguous interpretations of unmined hops in `## Paths` with clear boundaries between evidenced chains and frontier study plans.
3. **No Harm to Other Axes:**
   - **`freshness` / `operability` / `verifier independence`:** Unharmed. Child repos remain 100% read-only; no code, gates, or report schemas are mutated.

---

## 4. Proposed Move: Unified Reading-Path Typology and Rejection Lifecycle Bridge

The aggregator must not create a new universal research method (chousa owns that per Rule 3) and must not edit child repositories or report files. Instead, the aggregator can make one non-obvious, high-leverage synthesizing move in its round-12 curation and defect-routing deliverables:

### Part 1: Codify the Two-Tier Reading-Path Schema for the Aggregator Index
In the round-12 aggregate curation index, classify every path across the 17 present registries into:
1. **Evidenced Reading Chains (Closed Loops):** Paths where 100% of referenced rows are `mined` and each row's `used-by` cell points to a committed, verified `corpus/knowledge/*.md` file (e.g. `kotoba` SKILL authoring, `game-dev-3d` floor classification, `souji` F1/F3, `revenger` PE decoding, `kake` GHP served-set, `chousa` citation chain).
2. **Frontier Study Sequences (Open Trajectories):** Paths that contain `queued` or `rejected` hops (e.g. `tameshi` mutation validity, `kama` health & readiness, `kengaku` contamination audit, `lore` in-world time). These represent grounded pedagogical study plans and negative boundary cautions.
*Impact:* This prevents reviewers and future automated checkers from treating unmined hops in `## Paths` as "broken dependencies", recognizing them instead as documented frontier plans.

### Part 2: Resolve the Retrospective Rejection Paradox (Route to Parent / Contract v2)
Formally route the resolution of Contradiction 1 to the parent for SOURCES Contract v2:
- **Rule Formulation:** When a row's status transitions from `queued`/`mined` to `rejected` post-review (Rule 2 in-place status edit), the lane is NOT required to rewrite `teaches` in place.
- **Standardized Handling:** The rejection reason and flip condition MUST be logged in the round lesson's `## Gate` and noted in the `## Search log` (adopting `mado-shokunin`'s clean precedent).
- **Census Validator Tolerance:** Update `scripts/sources-census.sh` validate mode so that a row with `status=rejected` without a `REJECTED:` prefix in `teaches` does NOT emit an error IF an explicit `supersedes` or search-log rationale is present.

### Part 3: Address the `r10` and `maxBuffer` Aggregator Defect Routing
- **Route `r10` Selector Defect:** The aggregator round-12 report must formally note that `r10` failures across the 15 non-round-9 lanes are aggregator emission debts, NOT child-lane conformance failures.
- **Route `maxBuffer` Fix for `corpus-gate.mjs`:** Route a targeted fix for line 602 of `corpus-gate.mjs` to stream or increase buffer size (or use `--repo` for archives > 1 GiB), resolving the crash on `audio-shokunin`.

---

## 5. Second-Order Risks and Mitigations

| Surface | Risk | Second-Order Consequence | Mitigation |
|---|---|---|---|
| **Runtime** | Automated checkers fail on queued hops in paths | Lanes might artificially rush to create premature `knowledge/` stubs just to mark rows `mined`. | Formally declare in Aggregator round-12 documentation that `## Paths` may include `queued` and `rejected` hops as valid pedagogical sequences. |
| **Contract** | Duplicating chousa's method (Rule 3) | Aggregator oversteps into prescribing research workflows. | The move defines only curation classification and contract defect routing; question framing, source hierarchy, and admission remain strictly chousa's and lane `QUALITY.md`. |
| **Substrate** | Accidental mutation of child repositories | Disqualification of the aggregator round. | Strictly zero child repo writes. All classifications live in aggregator scratch and final aggregate reports. |
| **Verification** | In-progress census parser changes skew numbers | Publishing provisional numbers as final truths. | Keep all census totals under the provisional banner; rerun only after parent's `FINAL LANES READY` signal. |

---

## 6. Verification and Reproduction

The evidence and classifications in this note can be verified with the following read-only commands:

### 1. Verify Path Typology & Hops Resolution across Key Exemplars
```sh
# Verify tameshi's two-phase path (4 mined, 4 queued)
grep -A 3 'Mutation verdict semantics' /home/vgpnk/Projects/shokunin/tameshi-shokunin/corpus/SOURCES.md
# Verify game-dev-3d's closed loop path terminating on own-work measurement
grep -A 2 'Floor classification threshold' /home/vgpnk/Projects/shokunin/game-dev-3d-shokunin/corpus/SOURCES.md
# Verify lore's quarantined path note
grep -A 3 'Correction 2026-10-19 (round 103 post-review)' /home/vgpnk/Projects/shokunin/lore-shokunin/corpus/SOURCES.md
```

### 2. Verify Limitation Formulations and Rejection Syntaxes
```sh
# Verify Formula 1 ("does not establish / cannot alone evidence")
grep -E 'does not establish|cannot alone|availability is distinct|byte integrity only|never observed by a launch' \
  /home/vgpnk/Projects/shokunin/{mori,tsukuroi,kama,game-dev-3d,lore,tabi,revenger}-shokunin/corpus/SOURCES.md

# Verify Formula 4 (Canonical REJECTED/flip syntax)
grep -c 'REJECTED:.*flip:' /home/vgpnk/Projects/shokunin/*-shokunin/corpus/SOURCES.md
```

### 3. Verify Contradictions (r10, maxBuffer, and mado's retrospective rejection)
```sh
# Verify r10 failure across non-round-9 lanes
cd /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/fleet-aggregate
node .ufo/waves/round-9/corpus-gate.mjs --snapshot /home/vgpnk/Projects/shokunin/lore-shokunin 6e804e2e5bff0edcc260c995a058dd724b0c98c0 --round 103 | grep 'CR-.*-r10'

# Verify audio-shokunin maxBuffer overflow (exit 2 CNE)
node .ufo/waves/round-9/corpus-gate.mjs --snapshot /home/vgpnk/Projects/shokunin/audio-shokunin defbe128649268bfca75757cb3978be802696592; echo "EXIT=$?"

# Verify mado S030's unchanged teaches cell under Rule 2
grep 'S030' /home/vgpnk/Projects/shokunin/mado-shokunin/corpus/SOURCES.md
grep -A 4 'S030 duplicated S017' /home/vgpnk/Projects/shokunin/mado-shokunin/corpus/SOURCES.md
```
