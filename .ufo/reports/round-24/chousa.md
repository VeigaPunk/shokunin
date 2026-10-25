# chousa — round 24 report (kaika campaign; steered round 24 = the pre-registered r24)

Lane commit: **`6572827a39760f293c5401cabf08a5ce387af073`** (branch `kaika/round`, worktree
`.tower/worktrees/kaika/chousa-shokunin`, base `ab19cff`, author `chousa-shokunin
<chousa@shokunin.local>`). Gate `b5d0f93d…` → `752e4e38…`. Self-verdicts below wait on
non-author verification by the orchestrator.

Round identity: the fleet-root `.ufo/reports/round-24/` held only `kotodama.md`, and lane
`LOG.md` had no round-24 close, so there was no collision. The round-24 opening
(`LOG.md:816-820`, commits `798b37d`/`098f5e6`) is honored first and given its disposition
(below).

## Work performed

Declared claims (3, distinct axes, causally separable):

1. **operability** (the lowest *scored* non-retired axis; the other five are deliberately
   unscored, `SCORECARD.md:9-13`): the pre-registered `--json` manifest delimiter edge.
2. **coverage + capability `source registry`**: `corpus/SOURCES.md` per contract v1, plus
   three current-art method entries admitted through it. This is one claim. The critic
   showed that the registry and the entries are not separable if split.
3. **calibration**: the lane's own mistakes are mined into `corpus/lessons/round-24.md`
   `## Mistakes`, and every unlearned class gets a `QUALITY.md` criterion that cites it.

Disposition of the pre-registration (QUALITY 11): the planned 64-seat opencode-go-7 wave and
the luna dispatch recorded at `LOG.md:820` left no seat report anywhere, and nothing from them
is used. The pre-registered depth slot (manifest-format note) landed as claim 1's record and
is not claimed separately: its before→after is claim 1's (critic finding 7).
`SCORECARD.md:1234-1252`.

Work items:

- **Gate fix, landed in three steps.** Motivating evidence was measured live:
  `MANIFEST_LINES=1 INVALID_JSON_LINES=1` at `b5d0f93d`.
  - Step 1, first draft: `$(tail -c1)` probe.
  - Step 2: a hex `od` probe. My NUL control showed a NUL-terminated manifest was still
    glued, because bash drops NUL in command substitution.
  - Step 3: a non-empty unreadable manifest is refused before any write. The L2 reviewer
    reproduced a mode-0200 manifest still being glued.
  - Code: `tools/research-gate.sh:2376`, `:2490-2503`; cases 134–136 at `:5189-5192`.
  - The case-135 oracle needed `grep -a`, because GNU grep reads NUL as a line break in a
    binary file (`:5166`).
- **Receipts.** `corpus/evidence/json-r24-20261019T213117Z-{selftest,demo,battery,drift}.log`:
  - selftest `PASS (136 cases, 0 skipped)`, cases 1–133 `cmp`-identical vs r23;
  - three single-edit mutants (m1 prefix arm off, m2 old probe, m3 refusal off) each FAIL
    their pinning case;
  - masked battery ALL IDENTICAL;
  - drift `none`.
- **Records for claim 1.**
  - Note: `corpus/knowledge/json-delimiter-r24.md`.
  - Ledger addendum closing r16 seats 24 and 26: `corpus/knowledge/verification-r16.md:79`.
- **SOURCES registry.** `corpus/SOURCES.md`: Registry `:7`, Paths `:30`, Search log `:46`,
  Leads `:72`. Each of the 18 rows was opened this round by L2 `R24ExecSources`. The Gate
  quotes are in `corpus/lessons/round-24.md:39`.
- **Three method entries from current art.** Each was written by an executor who re-opened
  its sources:
  - `corpus/knowledge/claim-support-states-r24.md`
  - `corpus/knowledge/citation-chain-fidelity-r24.md`
  - `corpus/knowledge/contextual-source-admission-r24.md`
- **SKILL fold, minimal:**
  - 2 decision rows at `SKILL.md:22-23`;
  - a pointer to `corpus/SOURCES.md` at `:35`;
  - 1 error row at `:45`;
  - the selftest count 133 → 136 in the 7 gate rows (`:70-76`).
- **Mistakes and criteria.** `corpus/lessons/round-24.md` `## Mistakes` has 14 classes, and
  every pointer was re-run. The scribe corrected four dossier pointers (M-4, M-8, M-10,
  M-13). `corpus/QUALITY.md:9-54` adds criteria 6–12, each citing its lesson. Criterion 13
  was folded into 11 after the critic called it duplicate padding.
- **Index and records.**
  - `corpus/README.md`: coverage rows `:49-54`, count correction `:60`, Frontier `:491`.
  - `corpus/evidence/README.md:938`: the round-24 section.
  - `SCORECARD.md:1272` (capabilities row) and `:1282` (Planned round 25).
  - `LOG.md:822`.
- **Measurement script.** `corpus/evidence/round24-measure.sh`, with
  `round24-measure-{before,after}.log`.
- **L2 swarm.** One batched `task` call, 10 members:
  - planner `R24Planner-2`, connector `R24Connector-2`, scout `R24Scout-2`;
  - executors `R24ExecSources-2`, `R24ExecSupport-2`, `R24ExecChain-2`, `R24ExecAdmission-2`;
  - scribe `R24Scribe-2`, reviewer `R24Reviewer-2`, critic `R24Critic-2`.

  The first identical batch was refused whole (`Background job limit reached (100)`) and was
  retried unchanged as one batch. All 10 completed. No executor died of provider exhaustion,
  so no re-dispatch was needed. Models came from the session route table; none was passed.
  Every prompt led with `/skill:godspeed` plus the verbatim `directive.md` bytes.

Critic and reviewer findings acted on before commit:

- claims restructured for separability;
- the C2 counter strengthened to mined row + `used-by` + coverage row;
- an S006 model-evaluation result ("fact-check low across 14 models/130 queries") removed
  from admitted knowledge, as kengaku province;
- S006 and S007 scopes narrowed;
- write-only and NUL holes closed;
- QUALITY 9, 10 and 12 made checkable;
- the misattributed rejection quota corrected.

## Landed changes

All changes are in commit `6572827` and are logged in `LOG.md:822-831` ("Round 24 — landing"):

| Change | LOG.md entry line | Files |
|---|---|---|
| `--json` delimiter fix + cases 134–136 | :826 | `tools/research-gate.sh`, `corpus/knowledge/json-delimiter-r24.md`, `corpus/knowledge/verification-r16.md`, `corpus/evidence/json-r24-*` |
| Source registry + 3 method entries + SKILL fold | :827 | `corpus/SOURCES.md`, `corpus/knowledge/{claim-support-states,citation-chain-fidelity,contextual-source-admission}-r24.md`, `SKILL.md` |
| Mistakes mined → QUALITY 6–12 | :828 | `corpus/lessons/round-24.md`, `corpus/QUALITY.md` |
| Critic-driven corrections | :829 | the files above |
| Records | :830 | `SCORECARD.md`, `corpus/README.md`, `corpus/evidence/README.md`, `corpus/evidence/round24-measure*` |

## Before → after measurements

Counting command for all three claims: `bash corpus/evidence/round24-measure.sh <tree> [<bar>]`.

- **Before** was measured on `git archive ab19cff`, and claim 3 against
  `ab19cff:corpus/QUALITY.md`. Log: `corpus/evidence/round24-measure-before.log`.
- **After** was measured on `git archive 6572827` (the commit itself). Its output is the same
  as `corpus/evidence/round24-measure-after.log`.

| Claim | Before (ab19cff) | After (6572827) |
|---|---|---|
| 1 operability | `MANIFEST_LINES=1 INVALID_JSON_LINES=1`; selftest `PASS (133 cases)` | `MANIFEST_LINES=2 INVALID_JSON_LINES=0`; selftest `PASS (136 cases, 0 skipped)` (re-run on the commit archive) |
| 1, score re-derived per QUALITY 12 | `VERDICT_BEARING_EXPORTS=3/3` (score 3) | `VERDICT_BEARING_EXPORTS=3/3` (score 3, unchanged) |
| 2 coverage + registry | `EXPANSION_ADMITTED=0/3`; `corpus/SOURCES.md absent` | `EXPANSION_ADMITTED=3/3`; rows 18, malformed 0, tiers A=14 B=1 C=3, status mined=8 queued=7 rejected=3, dup `[]`, enum/inflation `[]`, missing-used-by `[]`, sections 4/4 |
| 3 calibration | `MISTAKE_CLASSES=14 CAPTURED_BY_CRITERION=3 UNCAPTURED=11` | `MISTAKE_CLASSES=14 CAPTURED_BY_CRITERION=13 UNCAPTURED=1` (M-8: disclosed in its own verdict, `none` by reason) |

No axis was harmed:

- masked battery ALL IDENTICAL (`json-r24-…-battery.log`);
- `GATE_DRIFT: none` vs the r12 baseline;
- r1 `3/3`;
- cases 1–133 byte-identical.

Per-axis self-verdicts are in `SCORECARD.md:1260-1267`:

| Axis | Self-verdict |
|---|---|
| operability | improved |
| coverage | improved |
| calibration | improved |
| depth | unchanged (not claimed) |
| freshness | unchanged |
| adjacency | unchanged |

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md:13-45` (two r24 decision rows and one error row, each citing a sourced entry) and `corpus/SOURCES.md`.
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md:822-831`: question → opened sources (`lessons/round-24.md:39`) → admitted entries → counted result.
- [~] Instructions executable by an agent without oral context — `corpus/evidence/round24-measure.sh` reproduces every number in this report from a bare tree.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `corpus/knowledge/claim-support-states-r24.md` §Limits keeps the S006/S007 system results out (kengaku); connector table in agent output `R24Connector-2`.

## Sources & frontier

- **SOURCES rows: 0 → 18.** Command: `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`
  (file absent at `ab19cff`).
- **Rows added by tier:**
  - **A = 14**: own-work S001, specs S002/S009/S013/S017, docs S003/S004/S008, and papers
    S005/S006/S007/S010/S011/S012. The preprints are A only for their own framework or
    statement.
  - **B = 1**: S018, a survey.
  - **C = 3**: all rejected — S014 OCEBM 2011 used as a universal ladder, S015 vendor launch
    page, S016 Wikipedia.
  - By status: 8 mined, 7 queued, 3 rejected.
- **Rows touched old→new:** none, because the registry is new. Before commit I narrowed four
  cells without re-opening the source; this is logged in `lessons/round-24.md` §Gate:
  - S006/S007 `scope` and `teaches`;
  - S002/S009 `recheck` `on-revision` → `365d`;
  - S001 `anchor`.
- **Frontier rows advanced:** `corpus/README.md:491`. This is the first frontier move off
  gate-hardening ground since round 2: claim-support states, citation-chain fidelity, and
  contextual source admission.
- **Study paths:** `SOURCES.md:30`. **Search log:** 3 bounded sweeps at `:46`.

## Mistakes

- **Classes mined:** 14 — M-1..M-12 from the STATE dossier §4, plus M-13 (metadata not
  machine-checkable) and M-14 (capability table vs LOG divergence).
- **Captured before → after:** 3 → 13.
- **Criteria added (each cites its lesson), mapped to the classes they capture:**

  | Criterion | Captures |
  |---|---|
  | 6 metadata header | M-13 |
  | 9 one home per number/finding | M-3, M-4, M-6, M-12 |
  | 10 no placeholder; dated snapshots | M-5, M-7 |
  | 11 plan, claim and table agree | M-1, M-14 |
  | 12 kept score re-derived or frozen | M-11; applied this landing |

- **Criteria 7 and 8** come from current art (scoped tier; four support states). They cite the
  admitted entries, not mistakes.
- **Repeated shape:** "a record restates a fact owned elsewhere and drifts" (6 of the 11 that
  had been uncaptured).
- **Mistakes made inside the round, recorded in the lesson:**
  - the fix shipped twice before it was right;
  - a test oracle (GNU grep on NUL) lied the same way the code did;
  - inserting index rows shifted README and SKILL line pointers. I repaired my own new
    pointers to heading anchors, and the lesson records the SKILL shift map.

## Trend verdicts

| Trend | Self-verdict (pending non-author verification) | Evidence |
|---|---|---|
| expansion | **improved** | 3 admitted entries on uncovered ground citing mined rows (`EXPANSION_ADMITTED=3/3`). The scout found these topics covered only as gate mechanics. |
| quality | **improved** | The gate class was closed with three mutant-killed arms and an identical battery. Admission bar 5 → 12 criteria, each checkable or command-backed. |
| discernment | **improved** | 3 rejected sources with flips. Tiers are scoped to claims, and the critic's tier and province findings were acted on before commit. Mistake capture went 3 → 13 of 14. |

## L0 questions

- `chousa | round-24 | PROVINCE.md refuses "external live-target research without operator approval"; the kaika binding (§6.5) let L2s read public documentation and papers. Is documentation-only reading of public papers standing approval for future chousa rounds, or a per-campaign exception? Model-quality results in those papers (S006/S007) were routed to kengaku and not admitted.`
- `chousa | round-24 | The operability score (3/10) measures a round-1 three-archive construct and was re-derived unchanged (3/3). Should the lane re-define the operability scale (round-25 candidate), or keep scoring only that construct and leave the other five axes deliberately unscored?`

## Integrator notes

- **Fleet-wide JSONL append hazard (connector).** Any appender that writes `printf '%s\n'`
  onto a file whose last byte is not `\n` glues two objects. Candidate surfaces named by the
  connector:
  - kasegi `ledger/missions.jsonl`
  - kengaku `results.jsonl`
  - kaidoku `wire.jsonl`

  This report does not verify those surfaces; the integrator should route it.
- **`cd` hazard.** In this harness, `cd` failed in one of my commands (`__fnmcd`), and that
  command was read-only. I checked and found no stray files from this lane in the fleet root.
  The receipt and measure scripts guard `cd`.
- **Shell `grep` is not GNU grep.** The session shell's `grep` is a builtin wrapper, not GNU
  grep: it reports Rust-style errors and handles binary files differently. Counting commands
  should run in a fresh `bash` (as `round24-measure.sh` does), or receipts may differ.
- **Contract census exit status.** SOURCES-CONTRACT-v1's missing-`used-by` census prints
  `missing:` lines but exits 0 (critic). "Clean" has to mean "no output", or the contract
  needs a nonzero exit.
- **Fleet MANIFEST undercount.** `MANIFEST.json` `lane_rounds.chousa` stops at 14 while craft
  rows reach 23 (STATE D-1). This is owned by the protocol/aggregator lanes.
- **Push.** No push. The standing operator rule "No push" takes precedence over MISSION.md's
  commit-then-push; operator-gated artifacts are committed, not pushed. The ledger report is
  uncommitted, for the integrator to commit with `--author="chousa-shokunin <chousa@shokunin.local>"`.

## Post-review erratum

The non-author critic found that `corpus/knowledge/citation-chain-fidelity-r24.md:9` labels as
"Falsifier" an altered-but-resolving hop, which actually confirms the entry's claim. That
breaks `corpus/QUALITY.md` criterion 1.

The fix is lane commit **`095b90c51aa666bbda26eb42421ff5818138b121`**:

- It appends an `## Erratum` block to the entry. Line 9 is unchanged.
- The block states a real refuting observation for each part of the claim:
  - **Part A:** a resolution-only check that agrees with fidelity on every hop of a labelled
    altered-hop set.
  - **Part B:** dispositions made without the per-hop comparison agree with dispositions
    made with it as often as two independent comparisons agree with each other.
- It re-checks the entry against QUALITY 1–12; criterion 1 is now met.

Re-run after the erratum: `round24-measure.sh` still reports `EXPANSION_ADMITTED=3/3`. No other
file changed, and there are no new claims.
