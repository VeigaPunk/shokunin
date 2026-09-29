# kotoba — round 15 report

**Lane:** kotoba-shokunin (prompt & skill craft) · **Round:** 15 · **Axis move:**
`operability` **7.5 → 8.0** (pre-registered **partial** band — the deciding
condition is named in § 3) · **Lane repo:**
`VeigaPunk/kotoba-shokunin`, landing commit **`b25f37a`** (pushed; `origin/master`
= local `HEAD`).

Pre-registration (written and committed **before** any build):
`corpus/knowledge/checklist-execution-round15.md` @ `63ceba7`
(sha256 `c335bee8c0d312b82250e58816f7faf198a75b56fdc67c085e222fd95d85b72e`), with
amendments **A1–A5** appended, never rewritten, each dated and attributed.

## 1. Move selection

`SCORECARD.md`'s lowest rows were `operability`, `calibration` and `adjacency`,
all 7.5. `operability` was taken because it alone carries a *named,
pre-falsified, unlanded* deliverable: round 13's plan item 2 ("make one `SKILL.md`
box executable … as `verifiers/verify_skill_checklist.py`") with its falsifier
already written, and the `operability` row already names the residual — the
`SKILL.md` checklist boxes are "the only un-automated procedures". The round-13
L0 question (may a lane work an advisory axis as its lowest-axis move; D-78's
`AXES.md`↔`MISSION.md` naming) is still unanswered and this round again worked the
lowest row — recorded, not re-litigated.

## 2. What landed

| Artifact | Extent |
|---|---|
| `verifiers/verify_skill_checklist.py` | 8 checks, exit 0/1/2/3, `--self-test`, `--json`, cwd-independent, stdlib only |
| `verifiers/checklist-baseline.json` | 41 boxes: **7 executed, 1 delegated, 33 unexecuted with reasons**; multiset parity by normalized text hash; schema `kotoba-checklist-v1` with the normalization pinned |
| `verifiers/checklist-command-vocabulary.json` | 28 declared command heads (`kotoba-command-vocab-v1`) |
| `verifiers/fixtures/checklist/` | 46 case dirs, one per defect class plus equivalent-mutation controls |
| `SKILL.md` | 675 → **599 lines** against its own ≤600 box; the missing **frontmatter-parses box** added (41 boxes, 15/9/9/8); the seven executed boxes annotated with their check ids; § Router model carries the executor paragraph |
| moved to corpus (the file's own remedy) | § Frontmatter craft (95 lines) → `knowledge/frontmatter-trigger-surface.md` § Craft rules; § Compression rules (23) → `knowledge/anatomy-and-compression.md`; § Anti-patterns table (20 rows) → `knowledge/fail-closed-and-anti-patterns.md` — each with a summary + pointer left in `SKILL.md` |
| `corpus/knowledge/checklist-execution-round15.md` | the round's claim, bands, falsifiers, amendments A1–A5, landed results and ceilings |
| `LOG.md`, `SCORECARD.md`, `SHONEN.md`, `corpus/README.md` | round entry + two correction entries, all seven axis rows re-based, box-1 evidence line, index row + Known-gaps bullets |

## 3. Falsifiers, run (all at `b25f37a`)

| Run | Result |
|---|---|
| live | **exit 0**, 8 × PASS — `box_map evaluated 41` (7 executed / 1 delegated / 33 unexecuted); `line_budget evaluated 599 within budget 600 (from box at line 328)`; `command_binary_resolves evaluated 16 subjects / 16 segments`; `no_placeholder evaluated 550` |
| `--self-test` | **`0 failure(s) over 772 assertions`**, exit 0 |
| from `/tmp` | exit 0 (cwd-independent) |
| `--json` | object with `checks`, `exit_code`, `pass`, `fail`, `na` |
| **red-before** — pre-state snapshot `git show 63ceba7:SKILL.md` in a dir named `kotoba-shokunin`, run with the landed map | **exit 1**, exactly two FAILs: `trigger.line_budget: evaluated 675 — 675 lines exceed budget 600 (from box at line 392)` and `checklist.box_map_complete` naming the unmatched box ids; the other six PASS |
| the check on its own author | a 603-line intermediate state of `SKILL.md` FAILed `trigger.line_budget` until trimmed |

**Band decision, taken against the pre-registration.** The full band required
"mutation lane finds no escape inside the seven executed checks". The mutation
lane ran **45 mutations: 35 caught, 5 escaped, 5 clean pins, 1 control** — so the
condition **fails as written** and the recorded band is the pre-registered
**partial (8.0)**. The five escapes are named, not hidden
(`corpus/knowledge/checklist-execution-round15.md` § A5): a nonexistent command
named inline outside the declared vocabulary; one hidden in a heredoc body; a
shell fence's *arguments* unchecked (`echo <nonexistent>`); whole-box reordering
within a section (the map is a text multiset, deliberately order-blind); and
`delegated:<path>` pointing at a file that exists but is no instrument. What earns
8.5 is stated in `SCORECARD.md` § planned: close the last two, or re-pre-register
the condition as "no escape outside the documented ceilings" and defend that
wording before the build.

## 4. Verification — 15 L2 lanes, two batched calls (floor 8)

Call 1 (9): `R15Plan`, `R15Connector` (planner/connector), `R15Populate`,
`R15Exec` (executors), `R15Surfaces` (scout), `R15Rules` (critic), `R15Witness`
(labrat), `R15R14` (reviewer), `R15Safety` (sentinel). Call 2 (6): `R15Mutate`
(mutation-tester), `R15Review` (reviewer), `R15Agree` (labrat), `R15Dead`
(simplifier), `R15Distill` (distiller), `R15Critic` (critic).

**Four lane findings changed the artifact before landing.**

1. `R15Witness` — blind, spec-only, forbidden to read the build — hand-derived 28
   verdict rows for 4 files and falsified two rules: fenced-only command
   extraction is empty on 3 of them (→ A2), and the 30-char negation window
   false-positived on the file's own box (→ A2.3).
2. `R15Populate` enumerated **138** `SKILL.md` files on this host and showed the
   English-only anti-trigger vocabulary fails 135 of them — a rule defect, not a
   fleet verdict (→ A4 adds the observed CJK markers).
3. `R15Rules` executed counterexamples against **6 of 8** rules (multiset parity,
   pinned normalization, registry-bound `executed:` ids, frontmatter block parse,
   abspath'd directory, box-bound budget, word-bounded negation, wrapper unwrap) —
   all repaired before landing.
4. `R15Agree` adjudicated the **instrument** wrong on a real false positive: the
   frontmatter parser rejected valid nested `metadata:` blocks — the shape the
   file's own `metadata.requires` box prescribes — hitting 37/138 fleet files;
   repaired in-round with fixtures `fm-nested-metadata` / `fm-stray-indent`.

**Escapes found and closed in-round.** `R15Critic` found two live escapes — a
`- [x]` marker toggle and a `delegated:` target that does not exist — and the
`annotation↔disposition` divergence class. All three are now instrumented
(`marker-checked`, `marker-near-miss`, `map-dead-delegated`,
`map-annotation-mismatch`, `map-executed-undisclosed`); the mutation lane then
re-derived them as closed (provably absent in the pre-revision copy) and found the
vacuity miscount the critic predicted — inline prose spans counted as "segments
seen" — which is fixed (inline spans are candidates only with a declared
vocabulary head).

**Weight removed.** `R15Dead`: 8/8 checks can fail with a named proving fixture,
46/46 fixture dirs are consumed, and five dead-weight items were deleted
(`xargs` unreachable in the vocabulary, an unconsulted fixture vocabulary file, a
vacuous conditional, an unread schema field, a speculative empty-scalar).

**Numbers disagreed with, not averaged.** `R15Review` and `R15Distill` named the
builder's stale report numbers (591 lines / 15 subjects / 648 assertions) against
the landed tree's (599 / 16 / 772): the drift is L1's own post-build edits, and
`corpus/knowledge/checklist-execution-round15.md` § Landed results carries the
landed numbers. `R15Review` also found and closed five discrepancies, two of them
in this lane's own box annotations (an inverted anti-trigger direction; a
pre-amendment command-scope line) and one stale count ("Eighteen rows" for a
20-row table).

**Fleet application (read-only; FAILs routed, never fixed).** All five sibling
`SKILL.md` files FAIL `literal_trigger_string` and `anti_trigger_clause`;
`line_budget` FAILs kagi 653, kasegi 997, kumitate 664; kasegi's command check
trips on an info-less fence holding a diagram — the live false-positive edge, and
the reason foreign FAILs are hints rather than verdicts.

## 5. Round-14 closure — the recording debt, with its defects named

Round 14 landed the opencode-side machine check (`29c17be`) but terminated before
recording anything: no `LOG.md`/`SCORECARD.md` entry, and its report sat unlanded
with `[PENDING]` markers. Round 15 (a) **lands that orphaned report** as the
successor (bytes unmodified; erratum appended, below), (b) re-measures the
artifacts, and (c) records the score.

`R15R14` reproduced all 9 required falsifier cases plus the full 7-rule drop-one
matrix (zero non-reproductions) and proved the opencode check **non-vacuous** by
deleting the OC-1 anchor and reading the FAIL naming the three `instructions/`
ids. Against round 14's pre-registered ladder that is the **full band ⇒
`coverage` 8.0 → 8.5**, attributed to round 14 in `SCORECARD.md`.

Two defects in round 14's record, recorded rather than smoothed:

- the round-14 DRAFT claims `verify_corpus_integrity` **9/9**; at its own landing
  commit `29c17be` it was **8/9 exit 1** (the baseline expected 42 tracked files,
  observed 43) — its promised corpus-baseline re-record never landed. A false
  claim in a filed report is corrected in the correcting round's artifact, never
  by rewriting the report;
- the move went unscored for a round (the durability debt the protocol names for a
  terminated lane-round).

## 6. Defects this round inflicted on itself, and how they were handled

- **Two box annotations in `SKILL.md` misstated their checks** (anti-trigger
  direction inverted; command scope pre-amendment). Found by `R15Review`,
  corrected, and the map's two hashes regenerated (the pin caught the edit).
- **Commit `0089974`'s `corpus/` pathspec** swept in
  `corpus/lessons/round-9-aggregator-corpus-verdict.md`; the correction commit
  `d6177f4` then **un-tracked it — worse, because its owner had legitimately
  landed it in `0f658ff`**. The next commit restored tracking, added its
  `corpus/README.md` index row and rewrote its two `shokunin:`-prefixed pointer
  sites to host-absolute form (the round-13 convention for dead sites in in-repo
  corpus files), appending a dated repair note inside the file. Both errors are in
  `LOG.md` instead of being rewritten away.
- **The mid-round red gate was attributed by experiment, not assumed**: a fresh
  clone without that sibling file runs `fault_injection_corpus.sh --self-test:
  OK` and `verify_corpus_integrity.py` 9/9, so the red was the sibling's file, not
  this round's changes. Landed state after the baseline re-record
  (45/0/30/0/27): corpus **9/9 exit 0**, independent verifier exit 0, fault
  harness `--self-test` OK and full run ALL PASS, harness claims 27/27, surfaces
  7/7, checklist executor exit 0.

## 7. Cross-domain — routed, not absorbed

- `kumitate-shokunin/scripts/surface-probe.mjs --checklists` is an **existing box
  executor** with a frozen grammar (`- [ ] <label> — \`<cmd>\` → exit <n> +
  \`<expected>\``). Only its own 9 of 72 fleet boxes match it; the other 63 are
  prose. Two dialects now coexist (grammar-in-the-box vs map-plus-registry) and
  the consolidation call is kumitate's/protocol's. `kagi corpus/claim-ledger.sh
  claim` is the second executor-shaped artifact found.
- Five sibling `SKILL.md` descriptions still fail the trigger/anti-trigger boxes —
  the round-8 rewrite set (`corpus/knowledge/sibling-description-rewrites-round8.md`)
  remains unapplied; three siblings exceed their own line budgets.
- `~/.agents/AGENTS.md` dated text re-confirmed by the population lane (6 PASS /
  1 FAIL by hand-applied box; host file lines 48/51).
- The aggregator lane's round-9 corpus verdict lesson was committed by that lane
  into this repo mid-round; its content is untouched apart from the index row and
  the two pointer repairs described in § 6.

## 8. SHONEN

Four boxes, all `[~]`; the round's marks are unchanged and no box moves this
round, because PROTOCOL.md:34-39 ("a subagent the lane dispatched is still the
lane") leaves no non-author verifier of this round's changes — every lane that
touched the artifacts is a kotoba-dispatched subagent.

- Box 1 `[~]` — `SKILL.md` decision tables / error patterns / checklists / cited
  sources: **present**, and now 7 of its 41 boxes are machine-executed; the
  evidence line was updated for the 41-box count and for the three moved sections,
  which is exactly what a non-author must re-check
  (`SHONEN.md:15`, `LOG.md` round 15).
- Box 2 `[~]` — end-to-end domain task logged: the round's task (execute the
  checklists, fix the file's own violation, record the debt) is in `LOG.md` round
  15 with its evidence; the non-author leg on record is still the aggregator
  lane's round-8 cold run.
- Box 3 `[~]` — instructions executable without oral context: `SKILL.md` gained
  the executor paragraph and lost 76 lines to pointer'd depth files; the two
  recipe defects B1/B2 were fixed in round 13; a fresh non-author run is what
  would restore `[x]`.
- Box 4 `[~]` — no cross-domain bleed: everything in § 7 is routed with a file and
  a line, nothing absorbed; `PROVINCE.md` unchanged.

## 9. Carried into round 16

The five named escapes (close `M35`/`M40` for 8.5); the delegated box's own
instrument — `trigger.11` delegates to `verify_corpus_integrity.py`, which by its
own docstring never scans `SKILL.md`, so this file's own corpus citations are
outside the enforcement the box claims; one new executed box from the planner's
ranked list (`T10` citation resolution, `D6` dispatch-prompt literals, `A9`
agent-body path resolution, falsifiers in `R15Plan/decidability.md`); the omp
provider-priority derivation (single-lane); `LDe`/`instructions` consumer;
implicit-intent fidelity; pointer hermeticity; 33 of 41 boxes still lane-attested;
the L0 axis-accounting question.

## 10. Erratum appended to the inherited round-14 report

`.ufo/reports/round-14/kotoba.md` was unlanded with `[PENDING]` verdicts; it is
landed here unmodified, and this paragraph supersedes its
`[PENDING]`/`[PENDING: final score, critic verdict, rebuilder numbers,
post-mutation escapes]` markers: the closure measurements are § 5 above — the
opencode check is non-vacuous (OC-1 anchor deletion), all 9 falsifier cases and
the 7-rule drop-one matrix reproduce, the corpus-baseline re-record it claimed
never landed (8/9 at `29c17be`, not 9/9), and the band recorded for round 14's
`coverage` move is **8.5, attributed to round 14** in `SCORECARD.md`.