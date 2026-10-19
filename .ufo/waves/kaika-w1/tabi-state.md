# kaika W1 — STATE dossier: lane `tabi` (browser & web-interaction craft)

- Author: W1StateTabi (scribe, leaf — no subagent dispatch). Date: 2026-10-19.
- Scope: read-only over `/home/vgpnk/Projects/shokunin/tabi-shokunin` + fleet-root ledgers; the only write is this file.
- Live verification performed this session: `node scripts/check-freshness.mjs --worktree` → `verdict=clean matched=34 unique=34 lane=31 public=3`, exit 0, at HEAD `40a6de8` (all 34 pin witnesses hold; SKILL.md is pinned at its declared `pre-append@c24eaea` revision per the gate's own rule, `scripts/check-freshness.mjs:96`).

## 1. Identity

| Item | Value | Evidence / command |
|---|---|---|
| Domain | browser & web-interaction craft (旅, journey) — "driving real browsers against real sites with evidence discipline" | `PROVINCE.md:3-4` |
| Rank | shonen; probation completed round 3 (SHONEN 4/4) but promotion never granted — `MANIFEST.json` `promotions[]` empty, and tabi has **no roster row** (roster = 13 entries, none tabi: `python3 -c "import json;print(len(json.load(open('MANIFEST.json'))['roster']))"` → 13) | `SHONEN.md` (4 checked boxes, named verifiers); fleet `MANIFEST.json` roster |
| Stale annotation | `SKILL.md:4` still reads "Rank: shonen (probation)" — probation ended at round 3 | `head -4 SKILL.md` |
| Git | branch `master`; HEAD `40a6de87f72b78d90ea627ad89717e55f219001e` ("cleanup: untrack 1 bytecode cache files", 2026-10-18); 52 commits, all authored `tabi-shokunin <tabi@shokunin.local>` | `git branch --show-current`; `git rev-parse HEAD`; `git log --format='%an <%ae>' | sort | uniq -c` → 52 |
| Working tree | clean — `git status --porcelain | wc -l` → 0 | same |
| Lane rounds (own LOG) | round 0 (mint) + training rounds 1–11 (all 2026-10-14) + fleet-round-1 attempt (2026-10-15, **blocked, not admitted**) + **16 admitted continuation rounds** (pstack-20261015-r01…r10, user-20261015-r01…r06) + a 2026-10-16 conformance entry (not a round) | `grep -c '^- 2026' LOG.md`; `LOG.md` entries |
| Last admitted round | user-20261015-r06 — freshness 7→8, work commit `1229098dae56c2d193c01203ff93651da2853f6e`, report `reports/user-20261015-r06.md`, non-author reviewer agrees | `LOG.md` (user-20261015-r06 entry) |
| Fleet ledger vs lane | Fleet `MANIFEST.json` tabi rows = mint(0) + train rounds **2–11 only**; **no tabi round-1 row**, **no rows for any 2026-10-15 continuation round**, no roster row. The "max recorded round 11" hint is true of the fleet ledger and false of the lane's own ledger (16 admitted rounds beyond 11). Lane's own closeout already knew: "nine `lane: \"tabi\"` train entries at rounds 2–10" — `closeout-r11.md:13` | `python3` scan of `MANIFEST.json` rounds/roster |
| Next round number | **Unresolved namespace.** Continuation naming is `<driver>-<date>-rNN`; last admitted user-20261015-r06; an executed **user-20261015-r07** wave (32/32 PASS) has no record (§5). L0 `:34` asks the operator to ratify the namespace — unanswered | `ls corpus/evidence/user-20261015-r07/`; fleet `.ufo/l0-questions.md:34` |

## 2. Axes

Current scores = the continuation tables' last row (after user-20261015-r06); training-final = the axes table's last explicitly measured values (`SCORECARD.md`).

| Axis | Now | Training-final | Evidence pointer |
|---|---|---|---|
| depth | 8 | 7 | `SCORECARD.md` user-swarm table r05 (paragraph receipt); training r9 state-changing matrix (`state-changing-matrix-r9.md`) |
| coverage | 8 | 5 | user-r04 note admit (`user-public-observation.md`); training r11 23 notes / 45 groups |
| operability | **7 (lowest)** | 5 | user-r01 + pstack-r06 self-test receipts; training r5 archive mechanism |
| freshness | 8 | 3 | user-r06 + pstack-r10 replay receipts; clause (c) closed 2026-10-15 by witness `c5e25208` (epoch 1792041388) |
| calibration | 8 | 6 | user-r03 pin-compare; training r11 four gate stamps |
| adjacency | 8 | 5 | user-r02 boundary refusal receipt; training r10 loopback-perimeter synthesis |

- Lowest non-retired axis: **operability 7** — unique minimum (`SCORECARD.md` user-swarm continuation table, last row).
- Saturation line + stagnation window N: **not declared** — owed: "to be declared by the lane on its next round per `AXES.md` §The stagnation nudge" (`SCORECARD.md` §Saturation).
- Capabilities count: **0** rows — table reads "— none yet —" (`SCORECARD.md` §Capabilities); rows enter only through a round demonstrating the capability running.
- Planned / retired: planned none (historical "chain ends" wording superseded by the 2026-10-15 continuation steer); retired none (`SCORECARD.md` §Planned / retired).
- No axis saturated; nothing retired.

## 3. Corpus

| Quantity | Value | Command |
|---|---|---|
| Knowledge notes | 26 / 7,322 lines | `ls corpus/knowledge/*.md \| wc -l` → 26; `wc -l corpus/knowledge/*.md \| tail -1` → 7322 |
| Lessons | 26 files, all with `## Gate` | `ls corpus/lessons \| wc -l` → 26; `grep -l '^## Gate' corpus/lessons/*.md \| wc -l` → 26 |
| Training lessons | rounds 1–10 only; **`round-11.md` missing** | `ls corpus/lessons/round-11.md` → No such file |
| QUALITY criteria | 5 (probation draft) | `corpus/QUALITY.md` (8 lines) |
| Evidence groups | 64 / 2,584 files / 11,737,007 B | `ls -d corpus/evidence/*/ \| wc -l` → 64; `find corpus/evidence -type f \| wc -l` → 2584; `du -sb corpus/evidence` |
| Reports | 23 (7 training audits r4–r10 + 10 pstack + 6 user) | `ls reports/*.md \| wc -l` → 23 |
| Plans | 18 files (round-2…11 plans + record drafts r4–r10 + completion-evidence) | `ls plans \| wc -l` → 18 |
| Scripts | 7 gate/harness `.mjs` (all with self-test entrypoints) | `ls scripts` |
| SOURCES.md | **absent** (wave-2 deliverable; not a lane defect) | `ls corpus/SOURCES.md` → missing |

- **Coverage map is stale-by-declaration**: header frozen at "Held at round 3 (2026-10-14): 8 knowledge notes, 1944 lines" (`corpus/README.md:5`) with 8 mapped rows + 3 appended addition rows (example-domain-observation, loopback-pin-stability, user-public-observation) → **15 of 26 notes unmapped**. Debt O3, still open (`closeout-r11.md` O3).
- **Frontier rows** (`corpus/README.md` §Frontier): extension↔daemon handshake (`extension_connected:false` throughout; bundle 1.11.3 vs daemon/extension 2.0.23); native WebMCP in chromium 152 unprobed; rate/ToS surfaces unmeasured (C6 deciding evidence still an absence); real-site journeys/POST/CSRF classes (approval-gated); evidence-byte archival (historical text says "thirteen `/tmp` groups" — superseded by the 45-group archive; the Frontier block itself is stale).
- **Front-matter contract adopted late**: only 2/26 notes open with `source:` / `verified-at:` / `recheck:` (`arc-synthesis.md`, `closeout-r11.md`). `grep -L '^source:' corpus/knowledge/*.md | wc -l` → **24**. The other 24 use HTML-comment headers + in-note anchors (the r1–r9 convention).
- **Overdue rechecks: zero by date** — no note carries a dated `recheck:` value (both existing `recheck:` fields are prose procedures, `arc-synthesis.md:7`, `closeout-r11.md:7`); 24 notes have no recheck at all. Pin integrity instead verified by the freshness gate (34/34 this session).
- Note shape is strong: every note opens with an assignment/method comment, scope + refusal lines, and carries per-claim anchors; several carry appended `VERIFIED — pin refresh` blocks (e.g. `multi-step-journey.md` tail).

## 4. Mistakes (mined from LOG/SCORECARD/reports/closeout)

| # | Class | Instance + evidence pointer | Already captured? | Proposed criterion if not |
|---|---|---|---|---|
| M1 | Anchor/citation slips | census `operations.md` cite off-by-4 (round-2 errata, `LOG.md` round-2); SKILL §Pins "297 lines" vs `wc -l` → 298 (round-3 LOG); malformed 37-hex HEAD pin still live at `carried-debt-closure-r8.md:5` (closeout O13); annotation drifts: "8-field `/status`" vs 9 keys, "4-line" vs 3-line edit (O15) | Yes — QUALITY #2 (anchor per claim) + §Pins staleness rule + append-only errata (QUALITY #4); sweep = re-derive pins (gate 34/34 this session) | — |
| M2 | Over-claimed observation | cdp launch-window extension-target sighting admitted then downgraded to non-replayable (round-2 errata, `LOG.md` round-2) | Yes — QUALITY #1/#3 + evidence ladder's first rule (closeout §1.1, `SKILL.md:361-367`) | — |
| M3 | Honest-stop on time-gated claim | clause (c) of the round-5 four-clause claim carried **IN FORCE 3/4** — never claimed closed on a same-day witness; closed 2026-10-15 by committed witness `c5e25208` (epoch 1792041388 ≥ 1792022400) | Yes — QUALITY #1 + the four-stamps gate (`LOG.md` round-11) | — |
| M4 | Tooling safety defect | freshness gate v1 "could hash an arbitrary host file if both metadata and table were changed" (`SKILL.md` §Safety erratum, ~`:1580`); corrected: fixed public identities, `O_NOFOLLOW`, symlink refusal; 12-case self-test supersedes 8-case; original preserved | Partially — SKILL §Safety erratum + gate registry capture it; no QUALITY criterion governs tooling | "A lane-owned gate pins its inputs (no mutable-path dereference), refuses symlink/non-regular files, and its self-test asserts the refusals." |
| M5 | Inherited-work misattribution | stopped headless attempt's artifacts inherited uncommitted; README erratum: "retained provenance, not this interactive session's capture" (`corpus/README.md` §Interactive reconciliation erratum) | Yes — QUALITY #3 + the erratum itself | — |
| M6 | Process gaps | round 11 ran with "no AUD-B11 seat observed" (`LOG.md` round-11); `round-11.md` lesson still owed; **user-20261015-r07 executed unrecorded** — 32/32 PASS aggregate + operability receipt, zero mentions in LOG/SCORECARD/reports/lessons (`grep -rn 'user-20261015-r07' LOG.md SCORECARD.md reports/ corpus/lessons/ \| wc -l` → 0) | No — QUALITY governs corpus claims, not round records | "An executed wave's aggregate lands in that round's LOG entry in the same integration commit, or is explicitly retired with a reason." |
| M7 | Redundant reject re-runs | Brave-not-installed reject re-ran 11 consecutive training rounds and again in pstack/user rounds; loopback≠real-site reject re-run ~10× (`LOG.md` passim) | No (diligence, not error — but wasteful) | "A reject verified ≥3 consecutive rounds may be pinned once and spot-checked on cadence instead of re-run every round." |
| M8 | Environment/state events handled honestly | daemon OOM-death (round 4; operator stop debt became moot); revival assessed, not executed (round 6) — never-set held all rounds | Yes — SKILL §Approval table (start doc-authorized / stop operator-only) + disposition notes | — |

No `harmed` verdict anywhere in the lane's records; every recorded round's three trends read `improved` or `unchanged` (`SCORECARD.md` verdict tables; fleet `MANIFEST.json` tabi rows).

## 5. Contract defects

1. **Required files**: all present — SKILL.md, PROVINCE.md, SCORECARD.md, LOG.md, SHONEN.md, MINT.md, AGENTS.md, corpus/README.md, corpus/QUALITY.md, corpus/knowledge/ (26), corpus/lessons/ (26). Missing: `corpus/lessons/round-11.md` (O5 residue); `corpus/SOURCES.md` (wave-2 deliverable).
2. **Identity defects**: `SKILL.md:4` "(probation)" stale; no tabi roster row in fleet `MANIFEST.json` (13 entries, none tabi) despite SHONEN 4/4 + 27 recorded rounds; no tabi round-1 train row in the fleet ledger; no fleet rows for any 2026-10-15 continuation round. All fleet-side (operator/integrator-owned; lane cannot fix).
3. **Orphan evidence — the significant one**: `corpus/evidence/user-20261015-r07/` (37 files: spec, dispatch, 32 seat results all PASS, `aggregate.json`, `operability/selftest-receipt.txt` ending `USER_ROUND_CONTRACT_SELFTEST verdict=clean cases=4`) with **no LOG entry, no report, no lesson, no SCORECARD row**. Also `corpus/evidence/pstack-20261015/` (aggregate `baseline-census.tsv` only) unexplained by any round row. Report-only; not touched.
4. **Bloat** (with commands): repo 35M (`du -sh .`); SKILL.md **125,194 B / 1,595 lines** (`wc -c SKILL.md`; `wc -l SKILL.md`) — 9 append-only errata sections accreted since round 4, including three superseded pin blocks; plans/ 500K across 18 files (largest: `round-11.plan.md` 48.1KB, `round-10-record-draft.md` 47.4KB — record drafts duplicate content that also lands in LOG); corpus 20M of which evidence 11.7M/2,584 files (the archive **is** the corpus by design — "Archive or it didn't happen", `cdp-evidence-patterns.md:92`); .git 11M; .ufo 3.3M (interactive-sessions 3.0M, gitignored).
5. **Dead pointers**: none found. Repo-relative sweep over LOG/SCORECARD/README/PROVINCE/SHONEN/SKILL/knowledge/lessons → all hits were prose globs (`w10-*`, `round-N.md`, `reports/r4..r10`) or fleet-root-relative cites (`.ufo/l0-questions.md`, `scripts/shokunin-watchdog.sh` — both exist at fleet root); 4 kaidoku sibling cites resolve (4/4); `/tmp` cites are volatile-by-design and declared stale. Confirmed expired: `/tmp/w8-tabi-b81` gone → O2's closing surface has expired; the tranche is unrecoverable (R1 residue stands). Minor: the VER-B11 `VERDICT.md` file itself was not archived (`corpus/evidence/w11-ver-b11-poll/` holds 15 verifier artifacts, no VERDICT file; verdict text survives via LOG/SCORECARD quotes).
6. **Stray artifacts**: none — `find . -name '*.pyc' -o -name '__pycache__' -o -name 'node_modules' -o -name '.DS_Store' -o -name '*.tmp` → empty (the 2026-10-18 commit already untracked 1 bytecode cache file). `.gitignore` covers `.ufo/interactive-sessions/` only.
7. **Uncommitted changes**: none (`git status --porcelain | wc -l` → 0).
8. **Fleet-side carried item** (reported, never absorbed — O14): watchdog roster omits tabi — `scripts/shokunin-watchdog.sh:14` `LANES="protocol aggregator kasegi kengaku kake kumitate kotoba kagi kama"`.
9. **Standing operator asks, both unanswered** (fleet `.ufo/l0-questions.md:25` approval packet R1/R2/R3 — sha `94dc63f5fb9e…`, filed 2026-10-14T17:05Z; `:34` namespace/dispatch ratification). Consequence: the loopback-only anti-claim remains in force; no external-site work is admissible.

## 6. Proposed round (next lane round)

**Pre-action (ledger hygiene, not a claim):** record or explicitly retire the executed user-20261015-r07 wave (M6) before any new round number is taken.

All three claims are loopback/metadata-only — no external sites (L0 packet unanswered), no daemon action, no secrets.

| # | Axis | Falsifiable before→after | Counting command |
|---|---|---|---|
| C1 | **operability 7→8 (lowest axis)** | The three shipped contract gates are cold-runnable from the repo alone and a combined-suite receipt lands in the corpus. Before: no combined receipt exists (`ls corpus/evidence/gate-suite-r1 2>/dev/null \| wc -l` → 0). After: one evidence group whose receipt shows all three self-tests green — `FRESHNESS_SELFTEST verdict=clean cases=12`, `ROUND_CONTRACT_SELFTEST verdict=clean cases=4`, `USER_ROUND_CONTRACT_SELFTEST verdict=clean cases=4` (all read-only; verified runnable this session for the freshness gate) | `git ls-tree -r --name-only <work-commit> \| grep -c gate-suite-r1/receipt.txt` → 0 before, 1 after |
| C2 | freshness | Every knowledge note is re-checkable on a stated cadence: dated `recheck:` anchors appended as append-only errata blocks to the 24 notes lacking them (front-matter stays untouched above append points). Before: `grep -l '^recheck:' corpus/knowledge/*.md \| wc -l` → 2; after → 26 | same grep at before/after commits |
| C3 | calibration | First **measured** rate boundary: a token-bucket limit on the lane's own loopback fixture (requests → 429 + `Retry-After` honored), turning the C6 deciding evidence from an asserted absence into a measurement. The r6 fixture already serves a shape-instrument 429 (`external-class-fixture-v2.md:337-338`) but measures only the stop predicate, not a rate boundary | `grep -rl 'token-bucket' corpus/knowledge/ \| wc -l` → 0 before, 1 after (new note `loopback-rate-limit-boundary.md` + coverage row) |

- SOURCES.md / knowledge mapping: C3 → new knowledge entry + tier-A SOURCES rows (MDN 429 / RFC 6585 — spec tier); C1 → own-work SOURCES rows (the three gate scripts) + a lesson `## Gate`; C2 → no new entry; it populates SOURCES.md's `recheck`/`used-by` columns for all 26 notes.
- Also owed in the same round (housekeeping, not claims): declare the saturation line + stagnation window N (§Saturation), populate ≥1 Capabilities row (the runbook capture chain qualifies — demonstrated rounds 2–4), refresh the coverage-map header (O3), and append the O12/O13 errata (arc-synthesis F1–F3; the malformed 37-hex pin).

## Session verification trail (commands actually run)

`git branch --show-current`; `git rev-parse HEAD`; `git log -1`; `git status --porcelain | wc -l`; `git log --format='%an <%ae>' | sort | uniq -c`; `ls corpus/knowledge | wc -l`; `wc -l corpus/knowledge/*.md | tail -1`; `ls corpus/lessons | wc -l`; `grep -l '^## Gate' corpus/lessons/*.md | wc -l`; `ls -d corpus/evidence/*/ | wc -l`; `find corpus/evidence -type f | wc -l`; `du -sb corpus/evidence`; `ls reports | wc -l`; `ls plans | wc -l`; `ls scripts`; front-matter greps (`grep -c/^L '^source:'`, `'^recheck:'`); `node scripts/check-freshness.mjs --worktree` (exit 0, 34/34); dead-pointer sweeps (repo-relative, sibling-relative, fleet-root); fleet `MANIFEST.json` roster/rounds scans; `/tmp` survival checks (`w8-tabi-b81`, `w11-ver-b11-poll` gone; archive groups present); watchdog `LANES` read; L0 file read (both tabi lines unanswered).
