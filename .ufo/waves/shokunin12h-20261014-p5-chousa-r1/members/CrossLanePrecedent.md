# CrossLanePrecedent — Cross-Lane Citation Precedents for chousa's Research Gate

**Member:** `CrossLanePrecedent` (connector)  
**Wave:** `shokunin12h-20261014-p5-chousa-r1`  
**Lane:** `chousa-shokunin` (shonen probation round 1: research-craft survey)  
**Domain Contract:** Deep-research method (調査) — question framing, source hierarchy, citation chaining, claim-vs-source verification.  
**Role:** UFO-FSD connector — deliver one non-obvious move (compatible synthesis across the round's proposals and fleet precedents) improving declared axes without harming another. Data only; not a verdict.  
**Declared Axes:** `coverage` · `depth` · `calibration`  
**Boundaries Enforced:** Leaf member (no subagents). Read-only local evidence; **NO external network or live fetches**. Secrets shape-only.  
**Ground-Truth Repositories Inspected:**
- Fleet root: `/home/vgpnk/Projects/shokunin`
- Precedent 1: `/home/vgpnk/Projects/shokunin/kagi-shokunin` (`corpus/claim-ledger.sh`, `corpus/knowledge/claim-ledger.md`, `corpus/stamps.tsv`, `corpus/claim-ledger.tsv`)
- Precedent 2: `/home/vgpnk/Projects/shokunin/kasegi-shokunin` (`corpus/instruments/anchorcheck.py`, `corpus/knowledge/citation-bases.md`, `corpus/instruments/resolve.py`)
- Precedent 3: `/home/vgpnk/Projects/shokunin/kumitate-shokunin` (`scripts/cite-check.mjs`)
- Survey artifacts: `/home/vgpnk/Projects/shokunin/research/` (`README.md`, `deep-research-2026-09-28/A-shokunin-tradition.md`, `B-multiagent-knowledge.md`, `C-rank-taxonomy.md`)

---

## 1. Evidence (Ground Truth & Precedent Audit)

The shokunin fleet already enforces rigorous mechanical citation disciplines across three mature lanes (`kagi`, `kasegi`, `kumitate`). Each lane developed specialized tooling to solve specific calibration collapses in its history. This audit examines the mechanisms, file:line anchors, and observed behaviors of those three precedents to establish the architectural blueprint for `chousa-shokunin`'s research gate (`tools/research-gate.sh`).

### 1.1 Kagi Precedent: `claim-ledger.sh` (Calibration Gate & Docs Mode)
**Source:** `kagi-shokunin/corpus/claim-ledger.sh` (1319 lines), documented in `kagi-shokunin/corpus/knowledge/claim-ledger.md:1-60`.

#### A. Historical Failure Mode & Origin
In Round 10, kagi's calibration score collapsed to 7 because:
1. The round report made 62 claims that had to be reviewed by hand (49 VERIFIED / 9 STALE / 4 UNCHECKABLE) because no claim carried an executable verification command (`claim-ledger.md:19-22`).
2. Two committed citations pointed to ephemeral session-scoped scratch (`local://round-10/connector.md` and `local://round-10/critic.md`) that could not resolve in any clean future session (`claim-ledger.md:23-27`).
3. Scorecard cells were self-scored with prose arguments rather than verifiable pointers (`claim-ledger.md:28-31`).

#### B. Architectural Mechanics in `claim-ledger.sh`
1. **Revision Stamps (`stamps.tsv`, L14-23, L224-284)**:
   - Format: `path <TAB> sha256 <TAB> lines <TAB> bytes`.
   - `verify` recomputes hash and line counts, detecting `STALE` or `MISSING` artifacts (`L45-48`).
   - Anti-shrink guard: regenerating via `stamp PATH...` replaces the whole row set; running against fewer paths than currently recorded is rejected (exit 2) unless `--prune` is explicitly supplied (`L19-23, L40-41`).
2. **Claim Ledger & The Final-Line Rule (`claim-ledger.tsv`, L24-30, L377-427)**:
   - Format: `id <TAB> command <TAB> expect <TAB> exit <TAB> timeout <TAB> note`.
   - The command runs under a strict timeout. It passes ONLY when BOTH:
     - The process exit code matches the expected code (`exit`).
     - The expected regex matches the **LAST non-empty output line** (`L26-30`). This prevents a command that prints a verdict-shaped string and subsequently crashes from falsely passing.
3. **Citation Durability & Ephemeral Marker Discipline (L31-46, L430-493)**:
   - Normalizes whitespace tokens by stripping backticks, quotes, parens, `./`, and line refs (`:N`, `:N-M`, `#anchor`, `?query`, `'s`) (`L469-493`).
   - Resolves target paths across shapes: `corpus/...`, `knowledge/...`, `lessons/...`, `<lane>-shokunin/...`, `ufo/...` (`L434-438`).
   - Rejection of ephemeral URIs: tokens matching `(local|artifact|agent|proc)://` fail closed as `EPHEMERAL` (exit 1), **UNLESS** the citing line carries an explicit marker:
     `scratch | ephemeral | relocat | formerly | no longer | removed | renamed | historical` (`L439-446`).
   - Rule: *"A dead citation must be labelled dead where it is cited, not no dead citations ever"* (`L44-46`).
4. **Knowledge Entry Audit (`docs` mode, L53-65, L817-935)**:
   - Every `corpus/knowledge/*.md` entry must declare how its fact base is re-verified on exactly ONE line (`L53-57, L860-877`).
   - Two strict syntax forms (`L55-57, L878-920`):
     - `Reverify: R<id>, R<id>` (runnable claims executed by `verify`).
     - `Reverify: by-hand: <class> — <reason ≥24 chars>`.
   - Four closed by-hand classes (`L59-60, L829`): `control-plane-scratch | opencode-internal | interactive-only | vault-refusal`.
   - Duplicate-reason rejection (`L908-917`): identical by-hand reasons across different files are flagged as `DUPLICATE-REASON` to stop rubber-stamping.
   - Ratio floor (`L61-62, L931-933`): `DA_FLOOR = (DA_N + 1) / 2`. The audit fails if fewer than 50% of knowledge entries carry automated claim rows. The manual escape cannot swallow the rule.
   - Revision pin enforcement (`L58, L924-927`): every knowledge entry must itself be recorded in `corpus/stamps.tsv` (`UNPINNED` defect).
5. **Command Safety Policy (L87-96, L156-186)**:
   - Allowlist for first token: `^(bash|grep|sha256sum|wc|test)$` (`L158`).
   - Zero shell metacharacters: `[;&|<>$`]` rejected (`L160`).
   - Quote-stripped verb deny list: `op`, `git`, `rm`, `curl`, `wget`, `sudo`, `ssh`, etc. cannot be bypassed via quoting (`g''it` or `g\it`) (`L93-94, L164`).
6. **Empirical Host Verification**:
   - `bash kagi-shokunin/corpus/claim-ledger.sh --selftest` → **PASS (97 cases, exit 0)**.
   - `bash kagi-shokunin/corpus/claim-ledger.sh docs` → **CLEAN (entries=21, row_linked=18, by_hand=3, floor=11, exit 0)**.
   - `bash kagi-shokunin/corpus/claim-ledger.sh citations` → **CLEAN (cites=925, docs=54, unresolved=0, ephemeral=0, labeled=13, exit 0)**.

---

### 1.2 Kasegi Precedent: `anchorcheck.py` & `citation-bases.md` (Base Vocabulary & Loss Discipline)
**Source:** `kasegi-shokunin/corpus/instruments/anchorcheck.py` (283 lines) and `kasegi-shokunin/corpus/knowledge/citation-bases.md:1-120`.

#### A. Historical Failure Mode & Origin
In Round 15-19, kasegi's external domain roots repeatedly vanished from the host:
- `~/Projects/bounties` was deleted on 2026-09-28.
- The frozen code mirror `~/Projects/the-bounty-hunter` and origin tree `~/Projects/origin-work` vanished on 2026-10-12 (`citation-bases.md:20-45, anchorcheck.py:67-74`).
- Naive citation checkers failed hundreds of citations as broken files (`MISSING-FILE` / `PAST-EOF`), tempting agents to delete historical evidence or forge fake passes.

#### B. Architectural Mechanics in `anchorcheck.py` & `citation-bases.md`
1. **Explicit Base Namespaces (`citation-bases.md:9-81`)**:
   - `LANE`: Active repository root (`SKILL.md`, `corpus/...`).
   - `MIRROR`: Frozen code mirror at git snapshot `1cfbd86`.
   - `ORIGIN-WORK`: Mutable data root (`~/Projects/origin-work/open-bug-bounties`).
   - `LOST-TREE`: Historical deleted tree (`~/Projects/bounties`).
   - `LOST-BASE`: Trees deleted after genesis (`MIRROR`, `ORIGIN-WORK`).
   - `BLOB-PIN`: Specific git blob hashes when live line numbers move.
2. **Dynamic Root Derivation (`anchorcheck.py:67-98`)**:
   - Avoids hardcoded host paths: `_derive_root()` inspects environment overrides (`KASEGI_MIRROR`, `KASEGI_ORIGIN_ROOT`, `KASEGI_LANE_ROOT`), falls back to candidate tuples, and preserves canonical expected paths on failure.
3. **Explicit Loss-Attribution Prefixes (`anchorcheck.py:103, L144-149, L231-234`)**:
   - Historical citations carry prefixes inside backticks: `` `[lost-tree] ops/claim-check.mjs:174-199` `` or `` `[lost-base] ops/validate.mjs:28` ``.
   - Verdict: Classified as `LOST-RECORDED` (or `BASE-ABSENT` when an entire tree directory is absent), **not** `MISSING-FILE` or `PAST-EOF`.
   - Calibration rule: `LOST-RECORDED` and `BASE-ABSENT` are counted separately and never contribute to the verified numerator, but do **not** fail the gate (`anchorcheck.py:59-61, L270-276`).
4. **Range-Valid vs. Semantic Validity Split (`anchorcheck.py:53-56, L222-229`)**:
   - Mechanical check: verifies file existence and line range boundaries ($b \le n$, $a \ge 1$, $b \ge a$).
   - Semantic verification: `anchorcheck.py` extracts and prints the exact text slice (`' ⏎ '.join(x.strip()[:100] for x in lines[a-1:b])`) on stdout (`L227`). The tool provides the text; semantic verification (does the cited line support the claim?) is an L2 audit task.
5. **Git Blob Pinning (`anchorcheck.py:22-25, L102, L118-128, L155-163`)**:
   - Exact syntax: plain HTML comment `<!-- pin: <relpath> <hex> -->`.
   - Verifies against `git show <hash>:<relpath>` in the lane repository (`L118-127`), surviving subsequent local edits.
6. **Rejection of Comma Anchor Lists (`citation-bases.md:104-106`)**:
   - Comma lists (e.g. `file.md:83,104,118`) defeat range resolution and classify as broken; each cited anchor must be a discrete backticked token.
7. **Empirical Host Verification**:
   - `python3 kasegi-shokunin/corpus/instruments/anchorcheck.py kasegi-shokunin/SKILL.md` → **7 in-range instances, 0 bad; 7 distinct anchors; LOST-RECORDED=306, BASE-ABSENT=0 (exit 0)**.

---

### 1.3 Kumitate Precedent: `cite-check.mjs` (Grammar, Resolution Ladder & Test Partitioning)
**Source:** `kumitate-shokunin/scripts/cite-check.mjs` (2538 lines, contract `kumitate-cite-check-v1.5`).

#### A. Historical Failure Mode & Origin
In rounds 16-28, kumitate identified multiple parser defects in doc verification:
- Code fences (```) containing backticks coupled with prose backticks, causing wide multiline phantom spans (R16 defect, `L473-516`).
- Unpaired backticks crossed newline boundaries, corrupting downstream scans (R23 defect, `L584-632`).
- False positives on non-path tokens (extension lists `.mjs/.rs`, runtime locks `.session-retention.lock`, strings dump symbols) triggered spurious gate failures (R27 defect, `L380-467`).

#### B. Architectural Mechanics in `cite-check.mjs`
1. **Masked Code Fence & Span Grammar (L14-29, L471-554)**:
   - Symmetric code fence detection: ```` ``` ```` closes ```` ``` ````, `~~~` closes `~~~`; cross-closing is rejected (`L28-29, L480-494`).
   - `maskFences()`: fences are overwritten with whitespace (preserving line lengths and newline offsets) *before* token extraction (`L507-516`). Code block contents can never pair with inline prose backticks.
   - Verbatim quote spans (`«…»`): supports multiline quotes without duplicating nested spans (`L16-21, L538-554`).
   - Line-local backtick pairing: odd backticks remain unpaired and never span past `\n` (`L22-25, L602-632`).
2. **Sticky Owner Attribution (L30-36, L691-746)**:
   - Line refs (`:N`, `:N-M`, `L<N>`, `/`-chains `:7681/:7817`) outside fences bind to immediately adjacent path tokens; otherwise they attach to the file's "sticky owner" (the most recent explicit source path) (`L31-34`).
   - An ownerless ref is reported as `ORPHAN_REF` (warning), preventing silent drops (`L35-36`).
3. **Four-Step Resolution Ladder (L41-47, L897-1112)**:
   - Priority 1: `file-relative` (relative to containing doc's directory).
   - Priority 2: `self` (kumitate doc tree).
   - Priority 3: `fleet` (fleet parent docs and sibling lane repos).
   - Priority 4: `src` (source tree root, applying exact match -> context -> suffix -> precedence).
4. **Non-Source Namespace Exemptions (L48-58, L380-467)**:
   - Exact-shape exemptions prevent false positives: `extension-list` (`.mjs/.rs`), `runtime-artifact` (`.lock`, `.json`), `binary-internal` (`src/...` in string dumps).
   - Negative guard: real dead source paths matching these shapes still error (`L428-467`).
5. **Strict Suite Partitioning: Hermetic `--selftest` vs. Live `--integrations` (L73-86, L1841-2504)**:
   - `--selftest`: runs ONLY hermetic synthetic test fixtures in a temporary directory (`L74-76`). It never accesses live repos and passes reliably in any repo state.
   - `--integrations`: runs assertions against live repository trees (`L77-80`).
   - Exits: `0` CLEAN, `1` DRIFT, `2` fail-closed setup error (missing target directories, empty scan sets, zero resolutions) (`L69-71`).
6. **Empirical Host Verification**:
   - `node kumitate-shokunin/scripts/cite-check.mjs --selftest` → **62/62 cases passed (hermetic), VERDICT: PASS (exit 0)**.

---

### 1.4 The Central Research Artifact Contradiction: Chat Exports Under No-Fetch
**Source:** `research/README.md:1-17`, `research/deep-research-2026-09-28/A-shokunin-tradition.md`, `B-multiagent-knowledge.md`, `C-rank-taxonomy.md`.

An empirical audit of the survey material reveals the fundamental tension of chousa's probation round 1:
1. **Artifact Substrate**: The three artifacts are raw chat-export transcripts from browser sessions (`research/README.md:6-8`). They contain UI noise ("Skip to content", "ChatGPT", "New chat", "You said:", "Worked for 1m 33s"), prompt text, and unstructured model responses.
2. **Citation Nature**: Citations inside the artifacts consist of:
   - External web URLs (e.g. `site.nihonkiin.or.jp`, `arxiv.org`, blogs).
   - Bare academic paper titles and author names.
   - Secondary model summaries of Japanese cultural/craft concepts (`shokunin katagi`, `nenki-ake`, `ichininmae`).
3. **Contract Constraints**:
   - **NO EXTERNAL FETCHES**: No live network requests, no web page fetches, no live-target research.
   - Any rule requiring an external source must be marked `proposal`.
   - Admitted rules must cite local artifacts (`path:line`).
   - The artifacts' citations are **unverified chat exports** — this is the round's central finding.

#### The Contradiction in Naive Gate Design
If `tools/research-gate.sh` is built as a standard citation checker:
- **Crash/Drift Failure**: If it requires all cited external URLs and academic papers to resolve to local files, the gate emits `UNRESOLVED` on every citation in the research survey, forcing an immediate, un-clearable `RESEARCH_GATE: DRIFT` (exit 1).
- **Dishonest Suppression Failure**: If agents paper over this by treating the chat transcript text as the "primary source" (e.g. citing `A-shokunin-tradition.md:47` as proof of historical artisan guild practices), they commit a catastrophic calibration failure: **treating an LLM chat transcript as primary historical evidence**, violating chousa's core hierarchy (`SKILL.md:18,28`).
- **Blind-Spot Failure**: If the gate simply ignores external citations and only checks markdown headers, it leaves citation chaining and claim-vs-source verification completely unenforced.

---

## 2. Affected Axes

| Axis | Pre-Move Tension in Round 1 Design | Post-Synthesis State (With Precedent Integration) |
|---|---|---|
| **`coverage`** | Naive gate either checks only local repo files (0% coverage of external literature cited in artifacts) or fails when encountering external URLs and paper references. | Covers the complete 3-tier citation reality: local repo files, raw chat transcripts, and external literature references via formal base namespaces (`LANE`, `[unverified-transcript]`, `[unfetched-external]`). |
| **`depth`** | Superficial syntax check (does the file exist?) or ungrounded scalar scoring. Fails to distinguish primary sources from aggregator transcripts or track broken hops in chains. | Implements multi-tier research verification: mechanical range check (Kasegi), citation-chain hop resolution with broken-hop provenance, and executable claim verification with the final-line rule (Kagi). |
| **`calibration`** | High risk of either hallucinated authority (treating GPT-6 chat exports as primary historical sources) or spurious gate failures on legitimate un-fetched literature citations. | Ruthless truth in labeling: unverified transcripts are tagged as aggregators, external citations are tagged `EXTERNAL_PENDING_APPROVAL`, broken hops are recorded as evidence, and ratio floors prevent escape abuse. |

---

## 3. Proposed Move: The Research Citation & Verification Ladder (RCVL)

**One non-obvious move synthesizing Kagi's Reverify/Marker grammar, Kasegi's Base/Loss vocabulary, and Kumitate's Resolution Ladder/Hermetic testing into `tools/research-gate.sh`:**

The research gate must not treat citation checking as binary (file exists / file missing). It must implement a **Three-Tier Research Citation & Verification Ladder (RCVL)** that directly reflects the epistemic status of research artifacts under an offline contract.

```
+-----------------------------------------------------------------------------------------+
|                               RESEARCH CITATION LADDER (RCVL)                           |
+-----------------------------------------------------------------------------------------+
| Tier 1: LOCAL / LANE       --> Mechanically verified path:line against local git tree   |
|                                (Kasegi range-valid + Kumitate ladder rungs 1-3)         |
+-----------------------------------------------------------------------------------------+
| Tier 2: CHAT TRANSCRIPTS   --> Base `[unverified-transcript]` path:line                 |
|                                Carrier only (Aggregator rank; never primary evidence)   |
+-----------------------------------------------------------------------------------------+
| Tier 3: EXTERNAL SOURCES   --> Base `[unfetched-external]` <url|doi|arxiv>              |
|                                Tagged `EXTERNAL_PENDING_APPROVAL` (info/note)           |
|                                Bound to APPROVAL.md row; never fails gate offline       |
+-----------------------------------------------------------------------------------------+
| Broken Chain Hops          --> Marked `broken-hop | paywall | dead-link | unindexed`    |
|                                Classified as CHAIN_HOP_BROKEN_RECORDED (Kagi marker)   |
+-----------------------------------------------------------------------------------------+
```

### 3.1 Explicit Research Base Vocabularies (Synthesized from Kasegi `citation-bases.md`)
In `tools/research-gate.sh`, define four canonical citation base namespaces:

1. **`LANE` / `LOCAL` (Local Repository Files)**:
   - Syntax: `` `chousa-shokunin/corpus/knowledge/*.md:10-25` `` or `` `research/README.md:6-8` ``.
   - Verification: Resolves via dynamic root derivation (`CHOUSA_LANE_ROOT`, `SHOKUNIN_ROOT`). Evaluates path existence and verifies line boundaries ($b \le n$, $a \ge 1$, $b \ge a$).
   - Verdict: `OK` (`IN-RANGE(LOCAL)`), `MISSING-FILE`, or `PAST-EOF`.
2. **`[unverified-transcript]` (Chat-Export Transcripts)**:
   - Syntax: `` `[unverified-transcript] research/deep-research-2026-09-28/A-shokunin-tradition.md:47` ``.
   - Semantics: Explicitly acknowledges that the file is an LLM chat transcript. The carrier line is verified mechanically for range bounds, but its epistemic rank is strictly **Aggregator / Carrier**. It can evidence what the chat export *contains*, but NEVER serves as primary evidence for external factual claims.
   - Verdict: `OK(TRANSCRIPT)` (in-range transcript carrier), or `TRANSCRIPT-PAST-EOF`.
3. **`[unfetched-external]` (External Sources Awaiting Operator Approval)**:
   - Syntax: `` `[unfetched-external] https://arxiv.org/abs/2305.16291` `` or `` `[unfetched-external] doi:10.1145/...` ``.
   - Semantics: Identifies external primary or secondary literature cited in the survey that cannot be fetched under the offline contract.
   - Gate Action: Checked against syntax regex. Verified that it corresponds to an entry in `APPROVAL.md` (`status: pending`). Emits finding `EXTERNAL_PENDING_APPROVAL` at severity `info` (or `note`). It does **NOT** trigger `DRIFT` or fail the gate.
4. **`[broken-hop]` (Broken Citation Chain Hops)**:
   - Syntax: `` `[broken-hop] https://... (marker: dead-link | paywall | unindexed | unverified-chat)` ``.
   - Semantics: Derived from Kagi's labeled line rule (`claim-ledger.sh:42-46`) and Kasegi's `[lost-tree]` prefix. A citation hop that fails to resolve is recorded as forensic evidence of a broken chain, emitting `CHAIN_HOP_BROKEN_RECORDED`, rather than an unhandled `CHAIN_HOP_UNRESOLVED` defect.

---

### 3.2 Dual-Track `Reverify:` Declaration for Research Notes (Synthesized from Kagi `docs` Mode)
Every research synthesis entry in `chousa-shokunin/corpus/knowledge/*.md` must declare its verification path on exactly ONE header line (enforced by `research-gate.sh docs`):

```markdown
Reverify: hermetic-local: R01-01, R01-02
```
or
```markdown
Reverify: external-deferred: APP-01 — External paper fetch pending operator window
```
or
```markdown
Reverify: uncheckable-transcript — LLM chat export contains unsourced assertion
```

#### Enforcement Rules (Imported from Kagi `claim-ledger.sh:833-935`):
1. **Exactly One Declaration**: Zero lines = `UNDECLARED` (exit 1); $\ge 2$ lines = setup error (exit 2).
2. **Strict Classes**: `hermetic-local`, `external-deferred`, or `uncheckable-transcript`.
3. **Detailed Reason Requirement**: Deferred or uncheckable declarations require a reason separator ` — ` and a minimum description length of $\ge 24$ characters.
4. **Anti-Rubber-Stamping**: Identical reasons across different research notes trigger `DUPLICATE-REASON` (exit 1).
5. **Ratio Floor**: In any research corpus, at least 50% of knowledge entries must carry `hermetic-local` claim rows (`DA_FLOOR = (DA_N + 1) / 2`). Blanket hand-waving is mechanically prohibited.

---

### 3.3 Two-Stage Gate Verification Pipeline (Synthesized from Kumitate & Kagi)
`tools/research-gate.sh verify` must execute two strictly separated verification stages:

```
STAGE 1: Mechanical Addressability & Hierarchy Audit
  ├── Mask code fences (```, ~~~) using Kumitate's maskFences()
  ├── Extract backticked tokens and «...» verbatim quotes
  ├── Resolve LOCAL tokens against repo line counts (Kasegi range-valid)
  ├── Resolve [unverified-transcript] tokens against chat exports
  ├── Validate [unfetched-external] tokens against APPROVAL.md table
  └── Enforce Hierarchy: reject any unverified-transcript cited as primary

STAGE 2: Executable Claim Ledger & Verdict Matching
  ├── Load tools/claim-ledger.tsv (id, command, expect, exit, timeout)
  ├── Validate commands against Kagi allowlist (bash|grep|sha256sum|wc|test)
  ├── Execute each command under timeout
  └── Enforce Kagi Final-Line Rule:
        Process exit == expected exit AND
        Expected regex matches LAST non-empty stdout line
```

---

### 3.4 Strict Execution Policy & Hermetic Selftest Architecture
Following Kagi (`claim-ledger.sh:87-96`) and Kumitate (`cite-check.mjs:73-86`):
1. **Command Allowlist**: In `tools/claim-ledger.tsv`, the executable command must start with `bash|grep|sha256sum|wc|test`. Shell metacharacters (`[;&|<>$`]`) and command chaining are prohibited.
2. **Quote-Stripped Deny Words**: Prohibit verbs that mutate disk or touch network (`curl`, `wget`, `git`, `rm`, `mv`, `ssh`).
3. **Hermetic `--selftest`**: `tools/research-gate.sh --selftest` must create a clean temporary directory (`/tmp/chousa-gate-selftest-XXXXXX`), populate synthetic fixtures (valid records, missing questions, unranked sources, broken hops, malformed reverify declarations), run the audit, and verify expected exit codes and stable finding IDs. It must **never** read live repo files during selftest and must pass in any host environment.

---

## 4. Risks & Mitigations

| Risk | Consequence | Mitigation |
|---|---|---|
| **Escape Abuse via `[unfetched-external]`** | An agent marks all dubious claims as `[unfetched-external]` to achieve an easy green gate without performing local verification. | Enforce Kagi's **Ratio Floor**: at least 50% of claims in any research synthesis must be `hermetic-local` (`DA_FLOOR = (N + 1) / 2`). Furthermore, every `[unfetched-external]` citation must bind to a unique row in `APPROVAL.md` with explicit justification. |
| **Carrier vs. Authority Confusion** | A researcher cites `[unverified-transcript] A-shokunin-tradition.md:47` and presents the AI's explanation of `shokunin katagi` as verified historical fact. | The gate's Hierarchy Checker inspects the record's Source Table: if a source is tagged `[unverified-transcript]`, its declared tier CANNOT be `primary`. It is forced to `aggregator`. An attempt to rank it as `primary` emits `HIERARCHY_INVERSION` (exit 1). |
| **Parsing Collisions on Complex Tokens** | URLs containing colons, query parameters, or anchors (e.g. `https://arxiv.org/abs/2305.16291:2`) collide with line-number anchor parsers. | Apply Kumitate's token normalization and fragment classification: URLs with protocol prefixes (`http://`, `https://`) are stripped of query/fragments before matching and are classified as `external-url` rather than file-path anchors. |
| **Code Fence Collision with Prose Backticks** | Prompts and LLM transcripts quoted in research notes contain stray backticks and markdown fences, causing parser desynchronization. | Adopt Kumitate's symmetric fence masking (`maskFences()`) prior to span extraction. Fenced blocks are masked with whitespace, completely isolating prose citations from quoted prompt blocks. |

---

## 5. Verification

### 5.1 Local Precedent Execution Verification
Executed all three precedent tools directly on host `plazir27` (`Linux 7.2.3-arch1-3`, 2026-10-14):

1. **Kagi Claim Ledger Selftest & Modes**:
   - Command: `bash kagi-shokunin/corpus/claim-ledger.sh --selftest`
   - Result: `ok-case 1 .. ok-case 97`, `SELFTEST: PASS (97 cases)`, Wall time: 2.01s.
   - Command: `bash kagi-shokunin/corpus/claim-ledger.sh docs`
   - Result: `DOC_AUDIT_RATIO: row_linked=18/21 floor=11 by_hand=3 duplicate_reasons=0`, `DOC_AUDIT: CLEAN`, exit 0.
   - Command: `bash kagi-shokunin/corpus/claim-ledger.sh citations`
   - Result: `CITATION_GATE: CLEAN (cites=925 docs=54 unresolved=0 ephemeral=0 labeled=13)`, exit 0.
2. **Kumitate Citation Checker Selftest**:
   - Command: `node kumitate-shokunin/scripts/cite-check.mjs --selftest`
   - Result: `62/62 cases passed (hermetic)`, `VERDICT: PASS`, exit 0.
3. **Kasegi Anchor Gate Verification**:
   - Command: `python3 kasegi-shokunin/corpus/instruments/anchorcheck.py kasegi-shokunin/SKILL.md`
   - Result: `7 in-range cite instances, 0 bad; 7 distinct anchors; LOST-RECORDED=306 PIN-BROKEN=0 ORIGIN=0 OUTSIDE-BASE=0 BASE-ABSENT=0`, exit 0.

---

### 5.2 Fixture Verification Contract for `tools/research-gate.sh --selftest`
The research gate design must include the following explicit test matrix in its hermetic `--selftest` suite:

| Case ID | Fixture Description | Expected Exit | Expected Finding / Verdict |
|---|---|:---:|---|
| `tc-01-clean-record` | Valid research record: declared question, ranked sources (primary > secondary > aggregator), resolved local hops, valid `Reverify: hermetic-local` header. | `0` | `RESEARCH_GATE: CLEAN` |
| `tc-02-no-question` | Research record omitting `# Question:` framing header. | `1` | `NO_QUESTION` |
| `tc-03-unranked-source` | Source table row with missing or invalid rank. | `1` | `UNRANKED_SOURCE` |
| `tc-04-hierarchy-inversion` | Source table classifies an `[unverified-transcript]` as `primary`. | `1` | `HIERARCHY_INVERSION` |
| `tc-05-unresolved-hop` | Citation chain hop fails to resolve and lacks an inline marker. | `1` | `CHAIN_HOP_UNRESOLVED` |
| `tc-06-marked-broken-hop` | Citation chain hop fails but is labeled `(marker: broken-hop — paywall)`. | `0` | `CHAIN_HOP_BROKEN_RECORDED` (info) |
| `tc-07-unfetched-external` | External URL tagged `[unfetched-external]` bound to `APPROVAL.md` row. | `0` | `EXTERNAL_PENDING_APPROVAL` (info) |
| `tc-08-unpointed-claim` | Claim in record carries prose evidence but no resolvable pointer. | `1` | `CLAIM_UNPOINTED` |
| `tc-09-final-line-fail` | Claim command prints success string on line 1, then crashes on line 2. | `1` | `CLAIM_VERDICT_MISMATCH` |
| `tc-10-policy-metachar` | Claim command in ledger contains `;` or `|` or `$`. | `2` | `POLICY_REFUSAL(metacharacter)` |
| `tc-11-doc-no-reverify` | Knowledge entry lacks a `Reverify:` declaration. | `1` | `UNDECLARED` |
| `tc-12-doc-ratio-fail` | Knowledge entries carry $<50\%$ automated claim rows. | `1` | `DOC_AUDIT_RATIO_FAIL` |
| `tc-13-empty-surface` | Directory scanned has zero research entries. | `2` | `EMPTY_SURFACE_REFUSAL` |

---

## 6. Synthesis & Routing to Wave Peers

To ensure smooth integration across the wave, the architectural findings of this report route directly to the designated owners:
- **To `ResearchGateDesign` (`tools/research-gate.sh`)**: Incorporate the two-stage verification pipeline (§3.3), the allowlist command policy (§3.4), and the ratio floor logic from Kagi's `doc_audit`.
- **To `FindingIds`**: Adopt the stable findings specified in §5.2 (`EXTERNAL_PENDING_APPROVAL`, `CHAIN_HOP_BROKEN_RECORDED`, `HIERARCHY_INVERSION`, `POLICY_REFUSAL`).
- **To `GateFixtureDesign`**: Implement test cases `tc-01` through `tc-13` directly in the hermetic `--selftest` harness.
- **To `ApprovalTable`**: Ensure the approval table schema includes an `Approval-ID` (`APP-XX`) matching the `Reverify: external-deferred: <Approval-ID>` declaration format.
- **To `PrimarySourceHierarchy`**: Codify the rule that `[unverified-transcript]` carrier tokens are strictly restricted to the `Aggregator` rank.
