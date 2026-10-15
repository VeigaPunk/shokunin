# FleetDeadPathAudit — Advisory Report

**Seat:** `FleetDeadPathAudit` (Connector)  
**Role:** UFO-FSD Connector — Fleet-level sweep across all six lane repos plus the fleet root for live dead-path citations, duplicate ownership, and cross-lane misrouting.  
**Advisory Status:** Data only. Not a native judge verdict, lane round report, receipt, or admission. Read-only audit; no lane file was edited, no commit was made, no push occurred, and no tests, builds, linters, or formatters were executed.  
**Commit Baseline Audited:**
- `kagi-shokunin`: `5b0d4b784624a15506d3c85c77c3ae619e07467f` (steered round 19)
- `kake-shokunin`: `59948314e9af5dd6ef81894fc1c422b353f10938` (steered round 19)
- `kama-shokunin`: `84a81304d7b0c77c84fe495f3bb728e8729faaff` (steered round 4)
- `kasegi-shokunin`: `a5cbf77cd21ed87d5a368a1f9456dfdc40faeadc` (steered round 20)
- `kengaku-shokunin`: `7153e671b1581a4b705583656883b6af158257df` (steered round 16)
- `kotoba-shokunin`: `b0c7cb2e248bccf692cf10e4d3c394e09944e83d` (steered round 19)
- `shokunin` (fleet root): `5ec4b4344e4fc0912d0ff10a2cfbf32fc2a1215b`
- `kumitate-shokunin` (adjacent boundary): `7a4c9a0` (SCORECARD rounds 18–31)

---

## 1. Substrate Truth (Exact Commands & Exit Codes)

Every candidate deleted path was measured directly on the host in this session. All commands executed from `/home/vgpnk/Projects/shokunin` without environment spoofing or network access:

| Command | Exit Code | Observed Output / Ground Truth |
|---|---:|---|
| `test -d /home/vgpnk/projects` | `1` | **ABSENT** (lowercase twin deleted; r16 inode 101125103 absorbed into `~/Projects`) |
| `test -d /home/vgpnk/Projects/shokunin` | `0` | **EXISTS** (canonical fleet root, inode 27238) |
| `test -d /home/vgpnk/Projects/origin-work` | `1` | **ABSENT** (deleted wholesale on/around 2026-10-12) |
| `test -d /home/vgpnk/Projects/ufo-fsd-alpha` | `0` | **EXISTS** (relocated canonical tree, HEAD `964f443e`) |
| `test -d /home/vgpnk/Projects/webzites` | `1` | **ABSENT** (including `repos/llm-wiki`, `bin/webzites.mjs`, `fleet.config.json`) |
| `test -d /home/vgpnk/Projects/ds4cc-marketplace` | `1` | **ABSENT** (source repo gone from host) |
| `test -d /home/vgpnk/Projects/plazir-15-site` | `1` | **ABSENT** (source repo gone from host) |
| `test -d /home/vgpnk/archive/bench-arena` | `1` | **ABSENT** (relocated archive directory deleted) |
| `test -d /home/vgpnk/bench-arena` | `1` | **ABSENT** (original bench-arena directory deleted) |
| `test -d /home/vgpnk/.bailian` | `1` | **ABSENT** (telemetry and model catalog tree deleted) |
| `test -x /home/vgpnk/.local/bin/the-janitor` | `1` | **ABSENT** (the-janitor CLI executable gone) |
| `test -d /home/vgpnk/.config/the-janitor` | `1` | **ABSENT** (`client.py`, `opencode.json`, `op.env` gone) |
| `test -d /home/vgpnk/.local/state/the-janitor` | `1` | **ABSENT** (locks, database, session-id gone) |
| `test -e /home/vgpnk/.config/systemd/user/qwen-coder.service` | `1` | **ABSENT** (systemd unit uninstalled/deleted) |
| `test -d /home/vgpnk/.local/share/the-musketeer` | `1` | **ABSENT** (shared burner chrome profile directory gone) |
| `git -C /home/vgpnk/projects/shokunin/kasegi-shokunin rev-parse HEAD` | `128` | `fatal: cannot change to '/home/vgpnk/projects/shokunin/kasegi-shokunin': No such file or directory` |
| `git -C /home/vgpnk/Projects/shokunin/kasegi-shokunin rev-parse HEAD` | `0` | `a5cbf77cd21ed87d5a368a1f9456dfdc40faeadc` |
| `ss -ltn` | `0` | Ports `:8080`, `:34113`, `:9222`, `:40961`, `:8791` have **zero** listeners |

---

## 2. Fleet-Wide Dead-Path Citations Sweep

### 2.1 Classification Rubric
- **live:** A present-tense instruction, runnable command, active surface table entry, or resolving claim asserting that the path exists or can be opened now, without a same-sentence or in-file absence marker.
- **labelled:** The line carries a qualifier (`[lost-base]`, `[lost-tree]`, `BASE-ABSENT`, fallback-order candidate, or table row named in an errata block), but is not an explicit standalone historical retraction.
- **marked-historical:** Explicitly dated past round log/lesson, past-tense narrative ("lived at", "at census time"), or under an explicit file/section header erratum declaring the tree absent/relocated.
- **unresolved:** Ambiguous reference, nickname/unit name rather than a filesystem path, or generator example string.

### 2.2 Census Summary Across All Repositories

| Repository | Scope / Context | Total Hits | Live Hits | Labelled | Marked-Historical | Unresolved |
|---|---|---:|---:|---:|---:|---:|
| `shokunin` (Fleet Root) | Root docs, `.ufo/prompts/`, `.ufo/reports/` | 1303 | **0** | 19 | 1284 | 0 |
| `kagi-shokunin` | Secrets & vault ops | 527 | **18** | 35 | 474 | 0 |
| `kake-shokunin` | Web properties & publishing | 393 | **8** | 48 | 337 | 0 |
| `kama-shokunin` | Local model serving & endpoint health | 140 | **46** | 12 | 80 | 2 |
| `kasegi-shokunin` | Bounty & security research | 163 | **22** | 76 | 50 | 15 |
| `kengaku-shokunin` | LLM research & evaluation | 588 | **61** | 14 | 513 | 0 |
| `kotoba-shokunin` | Prompt & skill craft | 96 | **10** | 4 | 82 | 0 |
| **Fleet Totals** | | **3210** | **165** | **208** | **2820** | **17** |

---

### 2.3 Detailed Repository Findings

#### A. Fleet Root (`/home/vgpnk/Projects/shokunin`)
- **Findings:**
  - Tracked core documents (`ROADMAP.md:73`, `LOG.md:539`, `SCORECARD.md:303`, `MANIFEST.json:577,1115,1243,1320,1344,1474`) cite vanished repos (`webzites`, `llm-wiki`, `bounties`, `origin-work`), but strictly as historical adjudication logs, defect records, or explicit notes of absence.
  - Historical prompts (`.ufo/prompts/aggregator-L1.md:1,10`, `aggregator-round-*.md`, `kagi-L1.md:1,5`, `kagi-round-*.md`, `kake-round-*.md`, `kotoba-round-*.md`, etc.) contain `Working dir: /home/vgpnk/projects/shokunin`. These are immutable historical artifacts of rounds 1–17; they do not function as current dispatch instructions.
  - `.ufo/l0-questions.md:17,20` documents the absorption and removal of lowercase `~/projects` into `~/Projects` as W6.
- **Live Violations:** **0**. All hits are marked-historical or labelled records.

#### B. Kagi (`kagi-shokunin` @ `5b0d4b7`)
- **Findings:**
  - `PROVINCE.md:11-12` and `LOG.md:726-729` explicitly mark `the-janitor` host paths absent (`~/.local/bin/the-janitor`, `~/.config/the-janitor`, `~/.local/state/the-janitor`, `tac-check`).
  - `SCORECARD.md:333` and `corpus/lessons/round-19-recensus.md:32-33` carry substrate absence as named carried debt (11 deferred ledger rows; unblock = reinstall the-janitor tree).
  - `PROVINCE.md:43` explicitly notes CDP `9222` + `~/.local/share/the-musketeer/chrome-profile` as contested with kake.
  - **Counterexamples (Live Hits):**
    - `SKILL.md:8, 23, 26-30, 32, 37-39, 42, 103, 139, 185-189, 222, 292, 311, 326, 357-358, 437, 462, 476-477, 479, 481, 488, 493, 495, 527, 560-563, 573, 576, 593, 607, 618, 645`: SKILL.md remains written as a live operator playbook giving runnable command recipes for `the-janitor` without an inline warning header marking the binary and configs absent on host.
    - `corpus/adjacency.tsv:19`: `# under ~/projects/shokunin/<lane>-shokunin/` (specification comment uses lowercase path).
    - `corpus/knowledge/adjacency-scope.md:92`: `basis: repo-relative path[:N|N-M], or lane:<lane>/<path>[:N|N-M] — the citation establishing the owner lane's claim; lane: resolves under ~/projects/shokunin/<lane>-shokunin/`.
    - `corpus/claim-ledger.tsv:22`: `...requires the fleet checkout layout (~/projects/shokunin/<lane>-shokunin)...`.
    - `corpus/README.md:25`: `~/projects/shokunin/CORPUS.md`.
    - `corpus/knowledge/surface-census.md:248`: `cd ~/projects/shokunin/kagi-shokunin`.
  - **Live Count:** **18** (5 lowercase fleet paths + 13 unhedged runnable SKILL sections).
  - **Owner:** `kagi-shokunin`.
  - **Unblock:** Append inline absence banner to `SKILL.md`; apply `FLEET-CASE` erratum to `adjacency.tsv:19`, `adjacency-scope.md:92`, and `claim-ledger.tsv:22` recording that `scope-gate.sh:91` derives `LANE_ROOT` from `SCRIPT_DIR/../..`.

#### C. Kake (`kake-shokunin` @ `5994831`)
- **Findings:**
  - Round 18 executed an extensive sweep: `freshness-pins.json:81-112` pins `pathsMissSet` (`~/Projects/webzites`, `~/Projects/ds4cc-marketplace`, `~/Projects/plazir-15-site`, `~/Projects/origin-work/*`, `~/projects`).
  - Across `corpus/knowledge/*.md`, citations carry `<!-- r18 re-census 2026-10-14: ~/Projects/webzites absent ... -->`.
  - Round 19 landed hermetic selftests in `scripts/freshness-sweep.mjs` and named PQ-2, PQ-14, and deleted binary names in `round-19-recensus.md:33-40`.
  - **Counterexamples (Live Hits):**
    - `SKILL.md:16-28`: Table of web properties presents `~/Projects/ds4cc-marketplace`, `~/Projects/plazir-15-site` as live source directories without inline absence qualifiers.
    - `SKILL.md:59`: `node ~/Projects/webzites/bin/webzites.mjs probe --all` (runnable command instruction to absent binary).
    - `SKILL.md:111`: `node ~/Projects/webzites/scripts/kimi-surface.mjs sync-check [<id>]` (runnable command instruction to absent script).
    - `SKILL.md:157`: `~/Projects/webzites/docs/SPEEDRUN-PROTOCOL.md` (unannotated text in checklist).
    - `SKILL.md:211-217`: Table commands `webzites probe <id>`, `webzites grokbot reconcile <id>`, `webzites grokbot tick`, etc., without top-of-section retraction.
    - `corpus/knowledge/freshness-sweep.md:43-53`: Copies pre-r18 pin literals without absence qualification.
  - **Live Count:** **8**.
  - **Owner:** `kake-shokunin`.
  - **Unblock:** Inline errata on `SKILL.md:16-28, 59, 111` marking webzites binaries and source checkouts absent on host; restore or retire web properties via operator.

#### D. Kama (`kama-shokunin` @ `84a8130`)
- **Findings:**
  - `tools/kama-probe.sh:529-547` correctly implements safe fallback: `$UFO_SRC` → `~/Projects/ufo-fsd-alpha` → `~/Projects/origin-work/ufo-fsd-alpha` → fail-closed.
  - `consumer-registry.md:30-80` provides errata re-anchoring `origin-work` and marking `webzites` rows historical.
  - **Counterexamples (Live Hits):**
    - `PROVINCE.md:10`: `| local model-serving processes & their ports | ~/.config/systemd/user/qwen-coder.service (llama-server, 127.0.0.1:34113) |` asserts the absent unit file as a concrete owned artifact on this host.
    - `corpus/knowledge/consumer-registry.md:111-119`: Rows 22–30 assert current citations under `~/projects/shokunin/...` (lowercase).
    - `corpus/knowledge/consumer-registry.md:191`: `~/projects/shokunin/kengaku-shokunin/PROVINCE.md:14`.
    - `corpus/knowledge/consumer-registry.md:332, 334, 337`: "Lane-level pin counts across `~/projects/shokunin`" and runnable command `grep -rn -E 'localhost:[0-9]+|127\.0\.0\.1:[0-9]+' ~/projects/shokunin \` which exits non-zero (directory not found).
    - `corpus/knowledge/listener-census.md:35, 37, 284, 285`: asserts `/home/vgpnk/projects` and runs `stat` / `find` against the lowercase root.
    - `corpus/lessons/round-1.md:46`: claims lowercase `/home/vgpnk/projects` is a live distinct directory.
    - `SKILL.md:76, 78, 79, 121, 222, 292`: presents `~/.local/bin/the-janitor:16-19` and `~/.config/the-janitor/opencode.json` as live consumer pins; item 12 (`:222`) instructs running `grep -rn ... ~/.config/the-janitor/opencode.json ~/.local/bin/the-janitor`.
    - `corpus/knowledge/cross-lane-scope.md:16, 47`: ownership table and repoint recommendation cite `/home/vgpnk/.local/bin/the-janitor:16-19` as live.
    - `corpus/knowledge/consumer-registry.md:119, 136, 179`: asserts `~/.local/bin/the-janitor` is a current consumer pin that "must remain covered".
    - `corpus/knowledge/listener-census.md:112, 177, 179, 294`: reconciles `~/.local/bin/the-janitor:19` as live drift.
    - `corpus/lessons/round-1-citations.md:72`: presents `~/archive/bench-arena/loop.sh:5` as the corrected current location (absent).
  - **Live Count:** **46**.
  - **Owner:** `kama-shokunin`.
  - **Unblock:** Append `FLEET-CASE` errata for rows 22–30 and lines 332–337; annotate `PROVINCE.md:10` that `qwen-coder.service` is currently absent; mark the-janitor consumer rows historical.

#### E. Kasegi (`kasegi-shokunin` @ `a5cbf77`)
- **Findings:**
  - `anchorcheck.py` and `resolve.py` derive candidate roots and cleanly classify absent base trees (`LOST-RECORDED=306`, `GONE`).
  - `SCORECARD.md:125`, `PROVINCE.md:18`, and `SKILL.md:27` explicitly record that `~/Projects/origin-work` disappeared on/around 2026-10-12.
  - **Counterexamples (Live Hits):**
    - `corpus/knowledge/citation-bases.md:72-73`: runnable command `git -C /home/vgpnk/projects/shokunin/kasegi-shokunin show fc6d398:SKILL.md` fails closed (`exit 128`).
    - `corpus/knowledge/triage-thresholds.md:12`: runnable command `git -C ~/projects/shokunin/kasegi-shokunin show fc6d398:SKILL.md | sed -n 'NNNp'` fails closed (`exit 128`).
    - `corpus/knowledge/submitted-registry.md:9, 10, 24, 26, 27, 42, 63, 66, 67, 123, 125, 127`: asserts `~/Projects/origin-work/open-bug-bounties/claim-packages/` as a "LIVE sibling tree" and "true home" of submission review receipts without an in-file loss marker.
    - `corpus/knowledge/intake-and-finalize.md:14, 18, 19, 22`: describes live data pipeline feeding `~/Projects/origin-work/open-bug-bounties/data/` into `bounty-map/programs/`.
    - `corpus/knowledge/ops-invariants.md:99, 100`: states board defaults to `/home/vgpnk/Projects/origin-work/open-bug-bounties` and requires `data/refresh_evidence.json`.
    - `corpus/knowledge/operator-queue.md:90`: cites `~/Projects/origin-work/open-bug-bounties/claim-packages/` receipt tree as live blind spot.
    - `SCORECARD.md:174`: Planned section asserts "surviving origin-work package" post-dating the absence annotation.
  - **Live Count:** **22**.
  - **Owner:** `kasegi-shokunin`.
  - **Unblock:** Point shell commands in `citation-bases.md:72` and `triage-thresholds.md:12` to uppercase `/home/vgpnk/Projects/shokunin/kasegi-shokunin`; append in-file loss erratum to `submitted-registry.md` and `intake-and-finalize.md`.

#### F. Kengaku (`kengaku-shokunin` @ `7153e67`)
- **Findings:**
  - `grader.py` is hermetic (733 checks pass, 0 mismatches, 0 origin-work or external paths in code).
  - Round 16 lesson acknowledges host surfaces are gone (`round-16-recensus.md:23-26`).
  - **Counterexamples (Live Hits):**
    - `SCORECARD.md:218-219`: asserts `~/archive/bench-arena — resolves; ~/Projects/webzites/repos/llm-wiki — resolves;`. **Direct contradiction with physical reality:** both directories are completely absent on disk (`exit 1`).
    - `LOG.md:22`: asserts `Resolving: ~/Projects/ufo-fsd-alpha, ~/archive/bench-arena, ~/Projects/webzites/repos/llm-wiki`.
    - `PROVINCE.md:12-14, 16-17`: Surface table claims `~/Projects/webzites/repos/llm-wiki` (SSOT for eval craft), `~/archive/bench-arena/` (local benchmark battery), `http://127.0.0.1:34113` (served local model via `qwen-coder.service`), `~/.bailian/telemetry.jsonl` are current surfaces.
    - `SKILL.md:3, 8, 11, 237, 323, 330, 451, 556-571`: asserts wiki as SSOT, lists `grade.sh` under `~/archive/bench-arena/grade.sh` as runnable command, and enumerates verified surfaces against vanished paths.
    - `corpus/README.md:4`: cites `~/projects/shokunin/CORPUS.md` (lowercase).
    - `corpus/evidence/round10-fleet/mutate_test.sh:9, 31`: defaults `REPO_ROOT` to `/home/vgpnk/projects/shokunin/kengaku-shokunin`.
    - 7 other evidence scripts (`recompute_r8.py`, `recompute_r9.py`, `schema_probe.py`, `analyze.py`, `test_harness.py`) hardcode `/home/vgpnk/projects/...`.
    - 10 knowledge files (`local-bench-arena.md:3`, `bench-arena-fresh-run.md:4, 8, 65, 67`, `bench-arena-round5-battery.md:104, 107`, `bench-arena-round6-stability.md:99`, `bench-arena-round7-scaffold-ablation.md:130`, `bench-arena-task27-timeout-anatomy.md:84`) cite or run `~/bench-arena` as live without absence annotation.
  - **Live Count:** **61**.
  - **Owner:** `kengaku-shokunin`.
  - **Unblock:** Append erratum striking round-15 "resolves" sentences in `SCORECARD.md:218` and `LOG.md:22`; annotate `PROVINCE.md:12-17` and `SKILL.md` that wiki, bench-arena, and bailian surfaces are absent on host.

#### G. Kotoba (`kotoba-shokunin` @ `b0c7cb2`)
- **Findings:**
  - Round 19 tightening of permission comparators landed cleanly in `verify_harness_claims.py`.
  - `SKILL.md:35` carries an accurate 2026-10-14 erratum for `origin-work/ufo-fsd-alpha`.
  - Pre-existing 601-line budget overrun on `verify_skill_checklist.py` is honestly reported as carried debt.
  - **Counterexamples (Live Hits):**
    - `SKILL.md:88`: `(dispatch prompts) are **host-observed** — no harness loads /home/vgpnk/projects/shokunin/.ufo/prompts/;`
    - `SKILL.md:97`: `| Dispatch prompt — spawn (L1/L2 lanes) | Ephemeral: consumed once by a subagent (**host-observed** — no harness loads /home/vgpnk/projects/shokunin/.ufo/prompts/`
    - `SKILL.md:106`: `2+ gives one hash — /home/vgpnk/projects/shokunin/*/AGENTS.md, re-verified round 7`
    - `SKILL.md:144`: `**Spawn dispatch-prompt anatomy** (from /home/vgpnk/projects/shokunin/.ufo/prompts/*-L1.md, nominal L1 prompt)`
    - `SKILL.md:153`: `.../home/vgpnk/projects/shokunin/.ufo/prompts/`
    - `SKILL.md:386`: `/home/vgpnk/projects/shokunin/.ufo/prompts/`
    - `SKILL.md:482`: `- /home/vgpnk/projects/shokunin/*/AGENTS.md (6 files) + ~/.agents/AGENTS.md`
    - `SKILL.md:484`: `- /home/vgpnk/projects/shokunin/.ufo/prompts/*-L1.md (8 files, 9–12 lines)`
    - `SKILL.md:486`: `- /home/vgpnk/projects/shokunin/.ufo/prompts/*-round-*.md (50 files, 3–11 lines)`
  - **Live Count:** **10**.
  - **Owner:** `kotoba-shokunin`.
  - **Unblock:** Append inline erratum to `SKILL.md:88-106` noting that the prompt and agent files resolve at uppercase `/home/vgpnk/Projects/shokunin/`.

---

## 3. Duplicate Ownership Audit

Across the 19 provinces and Kumitate's scorecard expansion, six distinct ownership collisions were identified:

```
                          ┌──────────────────────────────────────────────┐
                          │         ~/.kimi-code Substrate Tree          │
                          └──────────────────────┬───────────────────────┘
                                                 │
          ┌──────────────────────┬───────────────┴───────────────┬──────────────────────┐
          │                      │                               │                      │
          ▼                      ▼                               ▼                      ▼
  [kimi-webbridge/]     [config.toml:1284]               [skills/* symlinks]    [credentials/, oauth/]
    Tabi Owns:             Kaidoku Owns:                   Kotoba Owns:            Kagi Owns:
   Primary Substrate       REA Spawn Key                   Skill & Prompt Craft   Secret Hygiene Shape
          ▲                      ▲                               ▲                      ▲
          │                      │                               │                      │
          └──────────────────────┴───────────────┬───────────────┴──────────────────────┘
                                                 │
                                                 │ (Colliding Claim)
                                                 ▼
                                     Kumitate SCORECARD.md:568:
                              "Four families, disjoint, exhaustive"
```

| Collision ID | Substrate Surface | Primary Owner & Predicate | Colliding Owner & Claim | Defect Analysis | Resolution / Unblock |
|---|---|---|---|---|---|
| **DUP-01** | `~/.kimi-code/plugins/managed/kimi-webbridge/` | **tabi-shokunin** (`PROVINCE.md:6-8`): Owns primary substrate documentation, internals, and CDP verb discipline. | **kumitate-shokunin** (`SCORECARD.md:138, 568`): Counts member under K2 delegate plane as an exclusive family member toward `coverage:kimi-layer`. | **Subsumption Defect:** Kumitate claims exclusive "disjoint" ownership over the whole directory, absorbing Tabi's primary domain. Tabi already re-pinned the 3 member hashes (`webbridge-plugin-anatomy.md`). | Kumitate may count package presence in the K2 census, but predicate ownership of webbridge internals belongs strictly to Tabi. |
| **DUP-02** | `~/.kimi-code/config.toml` (Line 1284 vs File) | **kaidoku-shokunin** (`PROVINCE.md:41`): Owns REA MCP server spawn key (`line 1284`). | **kumitate-shokunin** (`SCORECARD.md:137, 570`): Counts `config.toml` under K1 config plane as an exclusive whole-file member. | **Predicate Collision:** Two lanes claim the same file without declaring partition boundaries. Kumitate's "disjoint" phrasing erases Kaidoku's line-scoped claim. | Declare shared-file partition: Kumitate owns provider/model registry sections; Kaidoku owns `[mcp_servers.rea]` spawn keys. |
| **DUP-03** | `~/.kimi-code/skills/*` | **kotoba-shokunin** (`PROVINCE.md:3-5`): Owns prompt & skill craft, trigger fidelity, and SKILL.md quality. | **kumitate-shokunin** (`SCORECARD.md:138, 560`): Counts 5 skill symlinks under K2 and documents trigger/mode machinery. | **Craft vs Mechanism Overlap:** Kumitate counts the symlinks as members without acknowledging Kotoba's authority over the skill bodies. | Partition: Kumitate owns resolution order (User > Extra > Built-in); Kotoba owns skill-body craft and trigger contracts. |
| **DUP-04** | `~/.kimi-code/credentials/`, `oauth/`, `server.token` | **kagi-shokunin** (Fleet Refusals): Mado (:14), Tabi (:16), Tsukuroi (:14), Kama (:17) route all secrets to Kagi. Kumitate cites "the kagi census discipline" (`SCORECARD.md:588`). | **kumitate-shokunin** (`SCORECARD.md:140, 586`): Counts them under K4 binary/secret plane. | **Contractual Void:** Kumitate cites Kagi's discipline, but Kagi's `PROVINCE.md` does not list `~/.kimi-code` secrets (it only listed Janitor paths). Kumitate acts as de facto sole claimant. | Kagi must officially declare shape-only census rows for `~/.kimi-code`, or ratify Kumitate's shape-only census under Kagi discipline. |
| **DUP-05** | Serving Plane `127.0.0.1:34113` / `qwen-coder.service` | **kama-shokunin** (`PROVINCE.md:6-16`): Explicitly owns local model-serving processes, port 34113, and endpoint identity. | **kengaku-shokunin** (`PROVINCE.md:24-25`): Declares the serving plane "Not owned ... no lane owns it", while absorbing unit restoration as Kengaku carried debt (`SCORECARD.md:213-216`). | **Direct Contradiction & Misrouting:** Kengaku asserts the plane is unowned despite Kama's rostered ownership, and absorbs host maintenance into eval debt. | Amend Kengaku `PROVINCE.md:24-25` to route endpoint identity to Kama; assign unit restoration to the operator. |
| **DUP-06** | Chrome Profile / CDP `127.0.0.1:9222` | **kagi-shokunin** (`PROVINCE.md:43`): Marks profile contested with kake. **kaidoku** owns self-launched CDP (:50). **tabi** owns webbridge CDP discipline (:9). | **kake-shokunin** (`SKILL.md:161`): References `the-musketeer` profile lease. | **Dormant Contest:** Profile directory and port 9222 are absent on host. No live collision occurs today. | Leave as dormant partition until profile or port is re-introduced by operator. |

---

## 4. Cross-Lane Misrouting Audit

Three architectural misrouting defects violate the fleet contract:

### 4.1 Kengaku Serving-Plane Misrouting & Debt Absorption
- **Defect:** Kengaku's `PROVINCE.md:24-25` states:
  > "- **Not owned:** the model-serving plane (llama-server flags, slot/batch config) — no lane owns it; escalate to the integrator instead of remediating."
  This directly contradicts `kama-shokunin/PROVINCE.md:6-10`, which explicitly owns local model serving processes and port 34113.
- **Second-Order Defect:** Kengaku's `SCORECARD.md:213-216` absorbs the dead `:34113` port as Kengaku's carried freshness debt:
  > "Carried debt, named: :34113 serving plane — unblock action = operator restores the qwen-coder.service unit + llama-server; until then the freshness/coverage rubric treats this as a declared-but-unresolvable surface..."
  This absorbs systemd unit restoration into an evaluation lane, violating Kengaku's own refusal rule.
- **Owner:** `kengaku-shokunin` (record amendment) and `kama-shokunin` (endpoint identity).
- **Unblock:** Route endpoint identity to Kama; route unit restoration to the operator.

### 4.2 Kumitate Substrate Absorption (`~/.kimi-code`)
- **Defect:** Kumitate's `SCORECARD.md:568` declares:
  > "Four families, disjoint, exhaustive over `~/.kimi-code`"
  Meanwhile, `kumitate-shokunin/PROVINCE.md` remains the 6-line seed that scopes only "OMP task/hub, ufo-fsd scripts & runtime" and refuses "anything outside this domain."
  By claiming disjoint exhaustiveness over `~/.kimi-code` without updating its province or recognizing sibling predicates (Tabi, Kaidoku, Kotoba, Kagi), Kumitate created a shadow province expansion that collides with four specialized lanes.
- **Owner:** `kumitate-shokunin` / integrator.
- **Unblock:** Add a qualifying clause to `SCORECARD.md:568` clarifying that the K-block is a census of filesystem members, not exclusive domain ownership.

### 4.3 Kama Owned-Artifact Dead Citation
- **Defect:** `kama-shokunin/PROVINCE.md:10` claims:
  > `| local model-serving processes & their ports | ~/.config/systemd/user/qwen-coder.service (llama-server, 127.0.0.1:34113) |`
  This asserts concrete artifact ownership of a file that does not exist on disk (`exit 1`). Kama's own `round-4-recensus.md:30` lists this as carried debt.
- **Owner:** `kama-shokunin`.
- **Unblock:** Append an absence annotation to `PROVINCE.md:10` stating the unit is currently uninstalled.

---

## 5. Claim-by-Claim Lane Record Verdicts

| Lane | Landed Claim / Assertion in Lesson | This Audit's Finding & Verdict | Evidence & Counterexample |
|---|---|---|---|
| **kagi** (`5b0d4b7`) | "No gate-default repair was warranted... lane censes the-janitor host surfaces" (`round-19-recensus.md:19-22`) | **AGREE** | Gates (`drift-pins.sh`, `surface-census.sh`, `scope-gate.sh`) have no `--src` or OMP tree dependencies. |
| **kagi** (`5b0d4b7`) | "Substrate absence (11 deferred ledger rows; six fail-closed live verdicts) ... Unblock: reinstall the-janitor tree" (`:32-33`) | **AGREE** | Re-measured absent (`test -x ~/.local/bin/the-janitor` exit 1). Defect is accurately named as debt. |
| **kagi** (`5b0d4b7`) | "`~/projects/shokunin` (lowercase) strings are deleted-path spellings; the resolver is script-derived (`scope-gate.sh:91`)" (`:38-39`) | **DISAGREE (Partial)** | The resolver derives `LANE_ROOT` from `SCRIPT_DIR/../..`, but `adjacency.tsv:19`, `adjacency-scope.md:92`, and `claim-ledger.tsv:22` still teach the lowercase path in prose without inline errata. |
| **kake** (`5994831`) | "`scripts/freshness-sweep.mjs`: `pins.probeHistoryAbsent` now SUSPENDS only canonical default" (`round-19-recensus.md:8-14`) | **AGREE** | Verified code diff in `5994831`. Selftest passes 13/13; explicit missing override exits 2 fail-closed. |
| **kake** (`5994831`) | "Bare online exit 1 stands: PQ-2 + PQ-14 ANOMALY (source repos gone) and §history SUSPENDED" (`:33-35`) | **AGREE** | `~/Projects/ds4cc-marketplace` and `~/Projects/plazir-15-site` measured absent (`exit 1`). |
| **kake** (`5994831`) | "Stale live prose recorded, not rewritten in place: `SKILL.md:59`/`:111` still name deleted webzites binaries" (`:37-40`) | **AGREE** | The lane honestly recorded that `SKILL.md:59, 111` remain live command citations to absent binaries. |
| **kama** (`84a8130`) | "`tools/kama-probe.sh consumers` → exit 0; `$UFO_SRC` rows resolve against `~/Projects/ufo-fsd-alpha`" (`round-4-recensus.md:8-9`) | **AGREE** | Fallback resolver correctly selects existing capital path. |
| **kama** (`84a8130`) | "`tools/kama-probe.sh check` → exit 2 (DEAD / connection-refused) — correct identity verdict" (`:10-11`) | **AGREE** | Ports 34113 and 8080 have 0 listeners (`exit 2` is ground truth). |
| **kama** (`84a8130`) | "Stale live prose recorded: `SKILL.md` still teaches live 11-row `MODEL_OK`; `PROVINCE.md:10-11` owns deleted host pins" (`:29-31`) | **DISAGREE (Under-listing)** | The lane noted SKILL and PROVINCE debt, but missed that `consumer-registry.md:111-119, 332-337` carry 19 live citations and runnable commands to lowercase `~/projects/shokunin`. |
| **kasegi** (`a5cbf77`) | "Both instruments already DERIVE their roots ... canonical absent" (`round-20-recensus.md:18-21`) | **AGREE** | `anchorcheck.py` and `resolve.py` cleanly handle missing origin roots. |
| **kasegi** (`a5cbf77`) | "`RECEIPT-STORE-LOST`, `MIRROR-SOURCE-LOST`, `ORIGIN-REPO-LOST` named debt" (`:25-28`) | **AGREE** | Store loss is named with operator unblock. |
| **kasegi** (`a5cbf77`) | "`BLOB-PIN-LOWERCASE-PATH`" named as debt (`:25-26`) | **DISAGREE (Under-listing)** | The lane named the class but did not name the specific lines (`citation-bases.md:72` and `triage-thresholds.md:12`), nor did it state owner/unblock. |
| **kengaku** (`7153e67`) | "`grader.py` is hermetic ... no `--src`/`UFO_SRC`" (`round-16-recensus.md:8-15`) | **AGREE** | `grader.py` exits 0 (733 checks, 0 mismatches) completely offline. |
| **kengaku** (`7153e67`) | "Host surfaces are gone: `webzites/repos/llm-wiki`, `archive/bench-arena`, `~/.bailian`, `:34113`" (`:23-26`) | **AGREE** | Measured absent on host (`exit 1`). |
| **kengaku** (`7153e67`) | "Round-15 'resolves' sentences for wiki/archive have no saved transcript ... current truth negative" (`:29-30`) | **DISAGREE (Record Contradiction)** | While the lesson admits current truth is negative, `SCORECARD.md:218-219` and `LOG.md:22` still assert that `~/archive/bench-arena` and `llm-wiki` resolve. The scorecard was not amended. |
| **kotoba** (`b0c7cb2`) | "`verifiers/verify_harness_claims.py` tightened from `at_least` to `equal`" (`round-19-recensus.md:8-14`) | **AGREE** | Vacuous permission assertions eliminated; selftest passes 10/10 assertions. |
| **kotoba** (`b0c7cb2`) | "`verify_skill_checklist.py` exit 1 (601 lines > budget 600) pre-existing on HEAD" (`:27-29`) | **AGREE** | Budget overrun verified pre-existing; honestly retained as carried debt. |
| **kotoba** (`b0c7cb2`) | "`SKILL.md` lowercase `/home/vgpnk/projects/...` cites remain" (`:30-31`) | **AGREE** | Accurately recorded as debt in lesson; live citations in `SKILL.md:88, 97, 106, 144, 153, 386, 482, 484, 486` confirmed. |

---

## 6. Affected Axes

| Axis | Movement | Evidence & Rationale |
|---|---|---|
| **Calibration** | **Improved** | Replaces false "resolves" assertions (`kengaku SCORECARD.md:218`) with verified negative observations. Separates historical pin records from runnable command procedures. Re-establishes explicit ownership boundaries across all 19 provinces. |
| **Adjacency** | **Improved** | Eliminates cross-lane contradictions: Kengaku's "unowned serving plane" claim is routed to Kama (identity) and operator (unit); Kumitate's K-block is partitioned so Tabi, Kaidoku, Kotoba, and Kagi retain their primary predicates. |
| **Freshness** | **Improved (Narrowly)** | Accurately censes deleted host paths across all 7 checkouts without fabricating replacements or re-pinning hashes to an empty host. |
| **Operability** | **Unchanged (Preserved)** | All safe gates (`grader.py`, `kama-probe.sh`, `freshness-sweep.mjs`, `claim-ledger.sh`, `verify_harness_claims.py`, `anchorcheck.py`) remain completely untouched and runnable. No script derivations or defaults are altered. |

---

## 7. Proposed Move (Connector Synthesis)

### One Bounded, Non-Obvious Move: Parent-Integrated `FLEET-ADJACENCY-ERRATA-V1`

To resolve duplicate ownership, cross-lane misrouting, and live dead-path citations simultaneously across the fleet without reopening settled gate code, editing immutable round logs, or retuning scorecard rubrics, the parent integrator shall land one append-only errata standard: `FLEET-ADJACENCY-ERRATA-V1`.

#### Clause A — K-Block is an Enumerable Census, Not Exclusive Ownership
Qualify Kumitate's `SCORECARD.md:568` ("Four families, disjoint, exhaustive over `~/.kimi-code`"):
1. **`~/.kimi-code/plugins/managed/kimi-webbridge/`:** Tabi owns plugin internals, behavior, and CDP discipline (`tabi-shokunin/PROVINCE.md:6-8`). Kumitate holds only the package-presence count in K2.
2. **`~/.kimi-code/config.toml`:** Kaidoku owns `[mcp_servers.rea]` spawn keys (`kaidoku-shokunin/PROVINCE.md:41`). Kumitate owns provider/model registry sections.
3. **`~/.kimi-code/skills/*`:** Kotoba owns skill craft, body contracts, and trigger discipline (`kotoba-shokunin/PROVINCE.md:3-5`). Kumitate owns discovery and resolution order.
4. **`~/.kimi-code/credentials/`, `oauth/`, `server.token`:** Managed under Kagi's secret hygiene discipline (shape-only, zero content-read). Kagi records shape census; Kumitate holds member counts.
5. **No Score Retuning:** Retain `coverage:kimi-layer = 10` on Kumitate. The score represents member count completeness (49/49), which is physically true on disk; the erratum corrects the legal exclusivity claim, not the arithmetic.

#### Clause B — `FLEET-CASE` Errata Standard for Lowercase Citations
Declare that `/home/vgpnk/projects` and `~/projects` are non-existent paths (absorbed into `~/Projects` as W6). Apply an inline erratum (not a table rewrite) to the specific lines offering runnable commands:
1. **kama:** `consumer-registry.md` rows 22–30 and lines 191, 332–337. Owner: `kama-shokunin`.
2. **kasegi:** `citation-bases.md:72` and `triage-thresholds.md:12`. Owner: `kasegi-shokunin`.
3. **kotoba:** `SKILL.md:88, 97, 106, 144, 153, 386, 482, 484, 486`. Owner: `kotoba-shokunin`.
4. **kagi:** `adjacency.tsv:19`, `adjacency-scope.md:92`, `claim-ledger.tsv:22`. Note that `scope-gate.sh:91` already derives `LANE_ROOT` dynamically. Owner: `kagi-shokunin`.
5. **kengaku:** `corpus/README.md:4`. Owner: `kengaku-shokunin`.
*Out of scope:* Historical logs, past lessons, and verifier fixtures quoting the old path as frozen audit records.

#### Clause C — Kengaku Serving-Plane & Vanished-Surface De-Confliction
1. **Retire "Unowned":** Replace Kengaku's `PROVINCE.md:24-25` ("no lane owns it") with an explicit routing to `kama-shokunin` (endpoint identity) and the operator (systemd service unit restoration).
2. **De-Absorb Carried Debt:** Transfer the `:34113` serving plane restoration debt from Kengaku's scorecard to the operator/kama debt register.
3. **Strike "Resolves":** Append an erratum to Kengaku's `SCORECARD.md:218-219` and `LOG.md:22` recording that `~/archive/bench-arena` and `~/Projects/webzites/repos/llm-wiki` are ABSENT on host (`exit 1`), falsifying the round-15 "resolves" sentence.
4. **Annotate Kama Province:** Append an absence note to `kama-shokunin/PROVINCE.md:10` recording that `qwen-coder.service` is currently uninstalled on host.

---

## 8. Second-Order Effects & Risks

1. **Rubric Invalidation Risk:** Dropping Kumitate's `coverage:kimi-layer` from 10 to a lower number would violate the pre-registered metric contract and disrupt cross-lane calibration. Clause A preserves the arithmetic while fixing the province contradiction.
2. **Provenance Corruption Risk:** Editing historical round logs (`LOG.md`), past audit lessons (`lessons/round-*.md`), or test fixtures in place would destroy the cryptographic audit trail of past waves. The move is strictly append-only.
3. **Hermeticity Risk:** Modifying gate scripts to add automatic path shims or fallbacks risks introducing non-deterministic behavior or breaking offline selftests. No script code is modified; all safe gates remain in their verified state.
4. **Host Assumption Fragility:** Relying on the operator to restore `the-janitor`, `qwen-coder.service`, or `webzites` before achieving green records would stall the fleet indefinitely. Marking absence honestly allows lanes to maintain high calibration despite missing host substrates.

---

## 9. Parent Verification Procedure (Post-Integration)

The parent integrator can verify the integrity of the fleet post-integration with these exact checks:

1. **Substrate State Verification:**
   ```bash
   test ! -d /home/vgpnk/projects && test -d /home/vgpnk/Projects/shokunin
   echo "Fleet Root Check: exit $?"  # Expect exit 0
   ```
2. **Kasegi Command Resolvability:**
   ```bash
   git -C /home/vgpnk/Projects/shokunin/kasegi-shokunin show fc6d398:SKILL.md >/dev/null
   echo "Kasegi Blob Pin Check: exit $?"  # Expect exit 0
   ```
3. **Kengaku Grader Hermeticity:**
   ```bash
   python3 /home/vgpnk/Projects/shokunin/kengaku-shokunin/grader.py
   echo "Kengaku Grader Check: exit $?"  # Expect exit 0, n=733 mismatches=0
   ```
4. **Kama Probe Safe Fail-Closed:**
   ```bash
   bash /home/vgpnk/Projects/shokunin/kama-shokunin/tools/kama-probe.sh check
   echo "Kama Probe Check: exit $?"  # Expect exit 2 (DEAD, correct identity verdict)
   ```
5. **Kake Freshness Selftest:**
   ```bash
   node /home/vgpnk/Projects/shokunin/kake-shokunin/scripts/freshness-sweep.mjs --selftest
   echo "Kake Selftest Check: exit $?"  # Expect exit 0 (13/13 passed)
   ```
6. **Kotoba Harness Verifier:**
   ```bash
   python3 /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/verify_harness_claims.py --self-test
   echo "Kotoba Harness Check: exit $?"  # Expect exit 0 (10/10 passed)
   ```
7. **K-Block Qualification Presence:**
   ```bash
   grep -n "disjoint, exhaustive over" /home/vgpnk/Projects/shokunin/kumitate-shokunin/SCORECARD.md
   # Verify that Clause A errata is present alongside the historical sentence
   ```

---

## 10. Unresolved Debt Ledger

| Debt ID | Affected Lane / Surface | Specific Debt Description | Owner | Unblock Condition |
|---|---|---|---|---|
| **DEBT-01** | `kumitate-shokunin` | Exclusive K-block claim (`SCORECARD.md:568`) overlapping Tabi, Kaidoku, Kotoba, and Kagi | Parent Integrator / `kumitate-shokunin` | Append Clause A errata to `SCORECARD.md:568`; retain `coverage:kimi-layer = 10`. |
| **DEBT-02** | `kengaku-shokunin` | Serving plane misrouted as "unowned" (`PROVINCE.md:24-25`) and absorbed as eval freshness debt (`SCORECARD.md:213-216`) | `kengaku-shokunin` | Append Clause C errata routing endpoint identity to Kama; assign unit restoration to operator. |
| **DEBT-03** | `kengaku-shokunin` | Stale "resolves" claims for absent `archive/bench-arena` and `llm-wiki` (`SCORECARD.md:218`, `LOG.md:22`) | `kengaku-shokunin` | Append Clause C absence errata striking the resolves claim. |
| **DEBT-04** | `kama-shokunin` | `PROVINCE.md:10` claims concrete ownership of deleted `qwen-coder.service` | `kama-shokunin` | Append absence annotation to `PROVINCE.md:10` noting service is uninstalled. |
| **DEBT-05** | `kama-shokunin` | `consumer-registry.md:111-119, 332-337` carry 19 live citations/commands to lowercase `~/projects/shokunin` | `kama-shokunin` | Apply `FLEET-CASE` errata block to `consumer-registry.md`. |
| **DEBT-06** | `kasegi-shokunin` | `citation-bases.md:72` and `triage-thresholds.md:12` offer failing `git -C /home/vgpnk/projects/...` commands | `kasegi-shokunin` | Apply `FLEET-CASE` errata pointing commands to uppercase checkout `/home/vgpnk/Projects/shokunin/...`. |
| **DEBT-07** | `kasegi-shokunin` | `submitted-registry.md` and `intake-and-finalize.md` describe `origin-work/open-bug-bounties` as live receipt store | `kasegi-shokunin` | Append in-file loss banner marking the data feeds `[lost-base]`. |
| **DEBT-08** | `kotoba-shokunin` | `SKILL.md:88, 97, 106, 144, 153, 386, 482, 484, 486` cite lowercase `/home/vgpnk/projects/shokunin` | `kotoba-shokunin` | Apply `FLEET-CASE` errata noting uppercase resolution under `/home/vgpnk/Projects/shokunin/`. |
| **DEBT-09** | `kagi-shokunin` | `SKILL.md` contains unannotated runnable recipes for absent `the-janitor` host substrate | `kagi-shokunin` | Append inline warning banner to `SKILL.md` noting the binary and configs are absent on host. |
| **DEBT-10** | `kagi-shokunin` | `adjacency.tsv:19`, `adjacency-scope.md:92`, `claim-ledger.tsv:22` cite lowercase `~/projects/shokunin` in prose | `kagi-shokunin` | Apply `FLEET-CASE` errata confirming `scope-gate.sh:91` derives `LANE_ROOT` from `SCRIPT_DIR/../..`. |
| **DEBT-11** | `kake-shokunin` | `SKILL.md:59, 111` name deleted webzites binaries in command steps | `kake-shokunin` | Append inline absence erratum to `SKILL.md:59, 111`. |
| **DEBT-12** | `kagi` / `kake` | Contested burner chrome profile lease (`~/.local/share/the-musketeer/chrome-profile` / `:9222`) | Operator / Integrator | Surface is completely absent on host (`exit 1`); leave dormant until restored by operator. |
| **DEBT-13** | Host Infrastructure | Substrate services absent on host (`the-janitor`, `qwen-coder.service`, `webzites`) | Operator (L0) | Reinstall or retire units permanently; not a lane code defect. |
