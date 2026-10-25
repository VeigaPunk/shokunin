# kagi — round 15 (operability 8 → 9) — DRAFT

> **Draft status.** This file is a *section skeleton* for L1 to paste into
> `.ufo/reports/round-15/kagi.md` and fill. Every `{{…}}` token is an unfilled
> fact. Provenance rules used below: `[measured]` = this drafter executed the
> command at the revision named; `[L1 live run]` = L1 reported the run and this
> drafter did not execute it (only those values carry that label); everything
> unlabelled is prose. §Gate first-contact record is live evidence (with artifact
> hashes) that belongs in the report's defects table and in `LOG.md`, not in the
> after-state. Read `## TODO for L1` at the bottom first.

Repo: `VeigaPunk/kagi-shokunin`, commit **`round-15`** (`{{ROUND15_COMMIT}}`).
Working dir at open: `HEAD` `2486643` (round-14 close, clean tree). `[measured]`

## Goal — why operability

Axis chosen: **operability 8 → 9**. Round 14 closed with `operability`,
`depth`, `coverage` and `adjacency` tied at 8 under `freshness` 9 and
`calibration` 9 (`SCORECARD.md:176-180`), so the mandated rule (*pick the
lowest-scoring axis*, `AXES.md` §Working an axis; `MISSION.md:24-32`) admits four
candidates and the round has to show why this one is the reachable cell:

- **depth (8)** — capped by a scope **refusal**, not by exhaustion: the remaining
  increments (masking of *ref-resolved* values, the mask token, `op inject`/`op
  read` execution) each require a resolved reference, i.e. the vault
  (`SCORECARD.md:223-225`, `PROVINCE.md`). Round 12 already re-measured that
  sentence once and it survived.
- **coverage (8)** — moves only when a *path* surface exists to declare; the
  census declaration is complete over the host as it stands
  (`SURFACE_CENSUS: CLEAN (assets=20 runtime=15 scanned=4 ok=34 absent=2
  skipped=0)`), so a coverage move needs a host change this lane cannot make.
- **adjacency (8)** — the contested-scope residue (CDP 9222 / musketeer profile ↔
  kake, `~/.agents/AGENTS.md` ↔ kotoba) is an **integrator** decision; the lane
  can only report and name owners, which it has done for six rounds
  (`SCORECARD.md:180`).
- **operability (8)** — the only candidate whose binding increment sits entirely
  in this lane's own repo artifacts. Its named ceiling in four successive
  scorecards is twofold: *nothing schedules the gates* and *the checklist's
  judgement items remain judgement* (`SCORECARD.md:28, 40, 62, 74, 84, 95, 106,
  118, 177`). The scheduling half is operator scope (systemd/cron). The second
  half — the checklist itself — is not, and it is exactly `AXES.md`'s own
  definition of the axis: *"Runnable artifacts: **checklists that are
  executable**"*, signal *"A checklist item can be run and produces the stated
  outcome"*.

So the move is the prose half, not the scheduling half: the 16-item
credential-hygiene checklist stops being prose and becomes a gate that executes
one check per item and prints a verdict, with the genuinely un-mechanisable items
counted as an explicit **by-hand** class (class + unique reason) rather than a
silent remainder. The round claims 9 and not 10 because the scheduling half is
untouched.

## The finding

`SKILL.md` §Credential-hygiene checklist holds **16** `- [ ]` items — 8 under
"Evidence production", 8 under "Handler operation". `[measured]` The contract in
force from round 9 onward was an *author count*: "**12** of the checklist items
are still operator judgement, not commands" (`SCORECARD.md:28`, repeated at
`:40, 62, 74, 84, 95, 106, 118, 177`), against a history where round 9 made
*item 1* a runnable command (`SCORECARD.md:28`) and round 10 recorded **three**
runnable gates behind it while still counting 12 judgement items
(`SCORECARD.md:62`).

Measured at `2486643` instead of quoted:

- **0** files under `corpus/` read the checklist at all: `grep -rln
  'Credential-hygiene\|hygiene checklist' corpus/*.sh` ⇒ no match. `[measured]`
- **0** `corpus/checklist*` artifacts exist. `[measured]`
- **5** of 16 items *name* an executable command (item 1 `bash
  corpus/surface-census.sh` + `drift-pins.sh` + `claim-ledger.sh verify`; item 5
  `bash corpus/op-ref-probe.sh`; item 6, which names `the-janitor run` only
  inside a prohibition; item 9 `client.lock` `flock`; item 15
  `corpus/transcript-scan.sh`). `[measured]`

Naming a command is not a verdict: no command in the repo answered *"is this
checklist item still satisfied?"*, so all 16 items were, mechanically, prose —
including the ones whose text quotes a gate. The 12/4 split was a **writer's
reading** of its own checklist, never a run. That is the round-14 lesson
repeating (`corpus/lessons/round-14.md`: *"an author's sentence about what is
reachable is itself a measurement"*), and it is why this round's by-hand set is a
counted set with a gate-measured size (`{{BY_HAND_M}}`) instead of a prose count.

The count itself had never been measured either, and the record is worse than
"stale". Re-running the section-scoped census over every `SKILL.md`-touching
commit reads `10, 12, 13, 14, 16` — **no revision ever held 15** — while
`SCORECARD.md:16` calls the checklist "a 15-item hygiene checklist" (wrong by two
at `ea77bf0`, where the count was 13; stale by three now) and the three "12 … are
still operator judgement" cells (`SCORECARD.md:40/62/84`) each sit against a
14-item revision. `SCORECARD.md:209` had already named **"the checklist item
count"** as the round-15 falsifiable target, so this round closes a gap the lane
named for itself. `[measured]`

Two defects in **committed rows** fell out of the same census — not prose slips,
and each a place where the round's own surface audited worse than it read
`[measured]`:

- **The lock is filed under a file that does not contain it.** `PROVINCE.md:12`
  (`client.py` … "HTTP client, lock, session-id") and `corpus/surface-census.tsv`
  (row `22`, `$HOME/.config/the-janitor/client.py` … "HTTP client: lock, …") both
  attribute the lock to `client.py`, but the flock lives in
  `~/.local/bin/the-janitor` (`LOCK_FILE=`, `exec 9>"$LOCK_FILE"`, `flock 9`) —
  so checklist item 9's serialization mechanism was documented in the wrong file,
  in two committed rows, for several rounds. Fix: `{{LOCK_FIX_LINES}}`.
- **Four symbols the checklist names are pinned nowhere.** `grep -c -- '<sym>'
  corpus/*.sh corpus/*.tsv` at the pre-move revision: `autoupdate`,
  `target_authority_conferred`, `40961`, `OPENCODE_SERVER_PASSWORD` have no pin
  (the sole `9222` hit is a digit run inside a sha256 in `corpus/stamps.tsv`), so
  items 8, 11, 13 and 16 read as covered while their named host facts were
  unmonitored. Disposition: `{{UNPINNED_SYMBOL_DISPOSITION}}`.

## What landed

> The shapes below are the contract in force (L1's design); the counts in this
> section are **placeholders to be filled from the tool**, not claims by this
> drafter. Nothing here was executed at draft time — `corpus/checklist-run.sh` did
> not exist at `2486643`.

- **`corpus/checklist.tsv`** — one row per checklist item. **Landed schema**
  (draft-time read of the file, `sha256
  3a5f4225…b261`): `id<TAB>class<TAB>lead<TAB>check<TAB>expect_exit<TAB
  >expect_last<TAB>reason<TAB>note`. `class ∈ {runnable, by-hand}`.
  `lead` is an ERE matched against the item's text, and the row↔item mapping is
  a **bijection over the 16 items** (a row matching nothing, an item no row
  matches, and two rows on one item are all defects). `runnable` rows run
  `check` as a shell command at repo root under `CHECKLIST_TIMEOUT`
  (default 240 s) and pin the exit code (integer or `A|B`) **and** an ERE
  against the last non-blank stdout line; `reason` must be `-`. `by-hand` rows
  put `-` in every mechanical column and carry
  `reason = "<class>: <text>"` with the class from the **closed** set
  `{authoring-duty, runtime-behavior, cross-lane, manual-change, operator-scope}`
  and `text` ≥24 chars **unique across rows**. At the draft-time snapshot the
  file held **{{TSV_ROWS}}** rows, **{{RUNNABLE_K}} runnable / {{BY_HAND_M}}
  by-hand**.
- **`corpus/checklist-run.sh`** — modes: default **verify**, `--list`,
  `--only <id>`, `--selftest`, `--help`, plus `--tsv F --skill F` (the selftest
  harness's alternate declaration/checklist pair). `--list` prints a `ROW …`
  line per row and closes with `CHECKLIST_LIST: rows={{ITEM_COUNT}}
  runnable={{RUNNABLE_K}} by_hand={{BY_HAND_M}}`, run nothing.
  - verdict `CHECKLIST_RUN: CLEAN (items={{ITEM_COUNT}} runnable={{RUNNABLE_K}}
    by_hand={{BY_HAND_M}} failed=0)`, exit 0; *(landed form — note it carries no
    `skipped=` field: {{SKIPPED_FIELD_CLAUSE}})*
  - `CHECKLIST_RATIO: runnable={{RUNNABLE_K}}/{{ITEM_COUNT}} floor={{FLOOR_F}}
    by_hand={{BY_HAND_M}}` (floor mirrors round 14's `ceil(n/2)`: {{FLOOR_CLAUSE}});
  - defects exit **1**: `ITEM-FAIL <id> (exit a want b)`,
    `ITEM-LASTLINE <id> (…)`, `ITEM-FAIL <id> (TIMEOUT)`, `UNDECLARED`, `EXTRA`,
    `UNMATCHED-ITEM`, `UNMATCHED-LEAD`, `DUPLICATE-LEAD`, `DUPLICATE-REASON`,
    `RATIO (runnable=K floor=F)`;
  - shape/policy exit **2**: `POLICY` (unknown class, runnable row carrying a
    reason, by-hand row carrying a check, short/duplicate note, non-ERE
    `expect_last`, malformed row) and `SETUP` (nothing executed);
  - `--selftest` ⇒ `CHECKLIST_SELFTEST: PASS ({{SELFTEST_CASES}} cases)`, exit 0
    (at the draft-time snapshot it printed **FAIL (10/24 cases)** — see the
    snapshot section below; the shipped count must come from the re-run).
- **Landed-vs-brief divergence** (recorded, not smoothed): the brief specified a
  6-column row (`cmd`/`expect_lastline`) and a verdict carrying `skipped=0`; the
  landed gate is 8 columns (`lead`, `reason` as `"<class>: <text>"`) with a
  row↔item **bijection** enforced by `lead` EREs, and a verdict with no
  `skipped=` field. The landed shape is stricter; the report must describe what
  shipped. {{DIVERGENCE_DISPOSITION}}
- **Hard constraints on every row** — enforced by the gate's `DENY_CHECK` as a
  **POLICY** refusal, not by convention: no row may name `op.env`, `op
  run`/`op read`/`op inject`, a handler start/stop, `the-janitor run`, or
  `corpus/claim-ledger.sh`; no row resolves a reference; and the one row that
  scans for ref-shaped tokens prints **counts only** (printing the matched line
  would be the very leak item 4 forbids). {{POLICY_ROW_EVIDENCE}}
- Docs: `SKILL.md` §Credential-hygiene checklist now points at the gate
  (`{{SKILL_POINTER_LINES}}`), `PROVINCE.md` / `corpus/README.md` gate table
  (`{{README_LINES}}`), `corpus/knowledge/{{ENTRY_NAME}}.md` (schema, verdict
  table, bounds, reproduction), `SCORECARD.md` round-15 pre/post,
  `corpus/lessons/round-15.md`, `LOG.md`, `corpus/claim-ledger.tsv` row
  `{{R15_ROW_ID}}` (+ re-pinned counts `{{REPINNED_ROWS}}`).

## Gate first-contact record — two real defects, both fixed before shipping

> **L1: this section is `LOG.md`/lesson material and the round's own
> defects-found-in-first-implementation table — it is *not* the report's
> after-state.** Every line is a live execution with its artifact hash and, where
> marked, `[L1 live run]`. The `{{…}}` in the sections above are still filled from
> L1's own confirming run.

### Phase 1 — the gate aborted on its own bijection guard (fixed during drafting)

`sha256 26b5cbc5aa749b3750a96db55fe84f662b1926e47fc25104190f08adc20e5dab  corpus/checklist-run.sh`

```
bash corpus/checklist-run.sh          → exit 1, **0 bytes stdout, 0 bytes stderr**
bash corpus/checklist-run.sh --list   → CHECKLIST_LIST: rows=16 runnable=9 by_hand=7      exit 0
bash corpus/checklist-run.sh --selftest → CHECKLIST_SELFTEST: FAIL (10/24 cases)
bash -x corpus/checklist-run.sh       → stops immediately after `+ dup_reasons=`
```

One defect class, two sites, `set -euo pipefail` at `:50` — the round-14
`nrows: unbound variable` class (a guard that aborts the run while its selftest
case passes anyway):

| Site | Why it aborts |
|---|---|
| `:209` `((hits == 0)) && defect "UNMATCHED-ITEM …"` | when a row **does** match (`hits ≥ 1`) the AND-list returns 1 and, as the loop body's last command under `set -e`, kills the script |
| `:212-213` `dup_reasons=$(for …; do [[ class == by-hand ]] && printf …; done \| sort \| uniq -d)` | the substitution's loop body ends on a false `[[ ]]` for the first **runnable** row, so the subshell exits 1 and the assignment fails under `set -e` — this is the abort the trace shows |

**L1 fixed this during drafting** (next hash) and the selftest went 10/24 → 28/28.

### Phase 2 — the two live item defects (both real, both fixed before shipping)

`sha256 750181362bbc62f13affd39afbf8a359b5728070e49acc20011bca14916ad9ed  corpus/checklist-run.sh`

```
bash corpus/checklist-run.sh
  → ITEM-FAIL E4 (exit 1 want 0)
      | REF_PATH_SCAN: hits=3
  → ITEM-FAIL H4 (exit 1 want 0)
      | JANITOR_PERMS: DEFECT (entries=1 steps=4)
  → CHECKLIST_RATIO: runnable=9/16 floor=8 by_hand=7
  → CHECKLIST_RUN: BROKEN (items=16 runnable=9 by_hand=7 failed=2)                     exit 1
bash corpus/checklist-run.sh --selftest → CHECKLIST_SELFTEST: PASS (28 cases)           exit 0
```

Both were **false defects**, diagnosed by re-running the row's own probe read-only
(ref tokens redacted by shape; no secret material printed), and both are now
fixed — the landed tree runs green (`[L1 live run]`):

| Row | What the row asserted | What was actually true | Disposition |
|---|---|---|---|
| `H4` (item 12, "never widen `janitor` permissions") | `entries=1` — the map lost an entry | the host front matter **was** correct (`"*": deny` + `janitor_auth: allow`); the parse `^permission:\n((?:[ \t]+.*\n)+)` could not match the **front matter's last line** (no trailing `\n`) and captured `"*": deny` alone | fixed ⇒ `JANITOR_PERMS: OK (entries=2 steps=4)`; the host was never touched |
| `E4` (item 4, "ref paths stay out of artifacts") | 3 undeclared ref-shaped literals | all three were the documented `vault` placeholder form (item segment 4 chars, **no 26-char id**) in `corpus/knowledge/op-env-refs.md:14`, `corpus/lessons/round-5-aggregator-audit.md:19`, `corpus/transcript-scan.sh:202` — the round-8 "prose collision" class | fixed by declaring the exclusion as a **placeholder-vault-name allowlist** (`vault|FakeVault|wal`), **which L1 names as this class's weak point** — see §Risks |

Also closed during landing (each named by L1 as a real fix): the `uniq -d` silent
death at the `dup_reasons`/`dup_ids` sites (the phase-1 abort), last-line
extraction moved to `awk 'NF{l=$0} END{print l}'` so empty output no longer kills
the run, `DENY_CHECK` extended to refuse `the-janitor run` and
`corpus/claim-ledger.sh` inside a row's check, `DUPLICATE-ITEM` added beside
`UNMATCHED-ITEM` (the bijection is now closed in **both** directions), and the
selftest rewritten to rebuild each fixture from scratch (28 cases, no
`sed`-on-fixture).

This is the round's own *defects-found-in-its-own-first-implementation* table, and
it must be reported as such: the gate's first contact with the host found **no
escaped secret and no widened permission** — it found two rows whose checks did
not measure what their items say, one false defect per direction of error. A
runnable row is only as good as its check, and neither check had ever been run
against the host before this round.

### Verified values (this drafter's run at the current revision, agreeing with `[L1 live run]`)

`sha256 76c0b83647703f1e844ccb440fa0b825209fe7bf3b070896f7a3cbb18e1aaf2e  corpus/checklist-run.sh`
`sha256 bc65aca8ef10780ef3b1e16cddebc8fcfcdf412f5aeaa43077d9070da42e7990  corpus/checklist.tsv`

```
bash corpus/checklist-run.sh            → CHECKLIST_RATIO: runnable=9/16 floor=8 by_hand=7
                                        → CHECKLIST_RUN: CLEAN (items=16 runnable=9 by_hand=7 failed=0)   exit 0
                                          (whole gate: 2.35 s real — the 240 s per-row timeout has wide headroom)
bash corpus/checklist-run.sh --selftest → CHECKLIST_SELFTEST: PASS (28 cases)                          exit 0
bash corpus/checklist-run.sh --list     → CHECKLIST_LIST: rows=16 runnable=9 by_hand=7                 exit 0
```

So `{{ITEM_COUNT}}`=16, `{{RUNNABLE_K}}`=9, `{{BY_HAND_M}}`=7, `{{FLOOR_F}}`=8,
`{{SELFTEST_CASES}}`=28, `{{TSV_ROWS}}`=16. **L1 re-runs at the committed revision
and pastes; the values above are from an uncommitted working tree.**

Snapshot class split (re-derive after any further row edit): `E1, E4, E5, E8, H1,
H3, H4, H7, H8` runnable; `E2, E3, E6, E7, H2, H5, H6` by-hand (4 ×
`authoring-duty`, 1 × `manual-change`, 1 × `runtime-behavior`, 1 × `cross-lane`).
Of the 9 runnable rows, 4 re-run commands the prose already named (`E1` delegates
to `surface-census.sh` + `drift-pins.sh`; `E5` `op-ref-probe.sh`; `H1` the flock
census; `H7` `transcript-scan.sh`, `expect_exit 0|1`) and **5 are new checks the
prose never had** (`E4` ref-shaped-token scan, `E8` `handoff-status.json`
boundaries, `H3` the config overlay, `H4` the `janitor.md` front matter, `H8` the
control-plane port/password census). That is the real before→after, and it is why
the axis moves — together with the finding that a fresh runnable row can be wrong
in both directions until it is exercised against the host.

## Before → after

| Quantity | Before (`2486643`) | After (`round-15`) |
|---|---|---|
| `corpus/checklist.tsv` rows | **0** (no such file — measured) | `{{POST_TSV_ROWS}}` |
| checklist items **executed by a gate** | **0** of 16 (measured: no gate read the checklist) | `{{POST_RUNNABLE}}` of {{POST_ITEMS}} |
| items carried as explicit **by-hand** | **0** (no class existed; the "12 … operator judgement" prose count was never a run) | `{{POST_BY_HAND}}` (gate-measured, class + unique note) |
| rows that run a command the prose never named | n/a | `{{NEW_CHECK_ROWS}}` (of which `{{NEW_CHECK_LIST}}`) |
| verdict line for the checklist | none — `bash corpus/checklist-run.sh` ⇒ `No such file or directory`, exit 127 `[scribe lane]` | `CHECKLIST_RUN: CLEAN (items={{ITEM_COUNT}} runnable={{RUNNABLE_K}} by_hand={{BY_HAND_M}} failed=0)`, exit 0 |
| ratio line | none | `CHECKLIST_RATIO: runnable={{RUNNABLE_K}}/{{ITEM_COUNT}} floor={{FLOOR_F}} by_hand={{BY_HAND_M}}` |
| selftest | n/a | `CHECKLIST_SELFTEST: PASS ({{SELFTEST_CASES}} cases)`, exit 0 |

Axis table (`SCORECARD.md`): the five non-moved cells say in-cell that the
increment is claimed under operability and name their ceilings.

| Axis | Before | After | Pointer |
|---|---|---|---|
| operability | 8 | **9** | `{{R15_ROW_ID}}`; `{{CHECKLIST_EXIT_ROW_ID}}` |
| freshness | 9 | 9 | `R14-01` |
| calibration | 9 | 9 | `R13-03` |
| depth | 8 | 8 | `PROVINCE.md` refusal (`SCORECARD.md:{{DEPTH_CEILING_LINE}}`) |
| coverage | 8 | 8 | `R11-01`, `R11-11` |
| adjacency | 8 | 8 | `corpus/README.md`; `corpus/lessons/round-15.md` |

## L2 wave ({{L2_LANE_COUNT}} lanes, one batched dispatch)

> **PLACEHOLDER — L1 fills from `LOG.md`** (and the lanes' scratch artifacts).
> Do not ship this table with any `{{…}}` left in it. One line per lane, in the
> round-14 style: *what it attacked → executed or reasoned → disposition*.

Dispatch roster observed in this session: `CheckPlanner`, `SiblingConnector`,
`ItemsScout`, `HostScout`, `EntryDraftExecutor`, `ReportDraftExecutor` (this
draft), `LogScribe`, `ItemReviewer`, `ClassCritic`, `PolicySentinel`,
`LiveLabrat`, `TsvMutator`, `DedupeSimplifier`, `WaveDistiller` — **14 names**,
which matches by count and by role the scribe's draft line *"14 L2 lanes in one
batched call (planner, connector, 2 scouts, scribe, 2 executors, reviewer,
critic, sentinel, labrat, mutation-tester, simplifier, distiller)"*. Confirm both
against the spawn record before printing the count — round 13 was 12 lanes in two
calls and a forward-copied number is exactly the defect this lane keeps finding.

| Lane | What it attacked | Disposition |
|---|---|---|
| `{{LANE_1}}` | `{{LANE_1_FINDING}}` | `{{LANE_1_DISPOSITION}}` |
| `{{LANE_2}}` | `{{LANE_2_FINDING}}` | `{{LANE_2_DISPOSITION}}` |
| `{{LANE_3}}` | `{{LANE_3_FINDING}}` | `{{LANE_3_DISPOSITION}}` |
| … | … | … |
| `{{LANE_N}}` | `{{LANE_N_FINDING}}` | `{{LANE_N_DISPOSITION}}` |

Open during drafting, to be answered by the wave or dropped honestly:
`{{WAVE_OPEN_QUESTIONS}}` — e.g. whether a row whose `check` is `true`/`printf`
passes `verify` (the by-construction row: predicted, must be **executed** before
it is reported), and whether 16 identical by-hand notes are refused (the
round-14 `DUPLICATE-REASON` class, now at row granularity, and now a landed
defect code).

Lanes L1 named as still open at draft time (do not print these as findings until
their `evidence:` blocks are transcribed): `TsvMutator` + `LiveLabrat` — mutation
and live-lab runs against the landed gate; `ItemReviewer` + `ClassCritic` — attack
on the **9/7 split** (the planner's stricter duty-vs-premise reading measured
**3 runnable / 13 by-hand** against the shipped criterion "is there a command
whose verdict is a defect signal for this item"); `PolicySentinel` — the printed-
output allowlist (`DENY_CHECK` terms and the counts-only ref sweep). Two of these
are the strongest candidates for the report's §L2 wave table.

## Adjacency (reported, not absorbed)

The closest sibling is **kotoba `verifiers/verify_skill_checklist.py`** (1208
lines, present at `kotoba-shokunin/verifiers/verify_skill_checklist.py`
`[measured]`): it forces every live `- [ ]` box in a SKILL.md to be
`executed:<check-id>` | `delegated:<instrument-path>` | `unexecuted:<reason>`,
against a baseline map (`verifiers/checklist-baseline.json`, schema
`kotoba-checklist-v1`) pinned by each box's normalised-text sha256, requires
every live box mapped exactly once (two-way parity), and floors the run at ≥1
valid `executed:` entry. That is the *same unit of work as this round* — a
SKILL.md checklist item mapped to a disposition — and it is **adjacent, not
duplicate**, on three axes:

| | kotoba `verify_skill_checklist.py` | kagi `checklist-run.sh` (round 15) |
|---|---|---|
| unit | box text (normalised, sha256-pinned) → disposition | item id → row |
| disposition vocabulary | `executed:` / `delegated:` / `unexecuted:<free-form reason>` | `runnable` (executed in-process) / `by-hand:<closed class> + unique ≥24-char note` |
| execution | **does not run a box's command** — its command check only *resolves* command heads (`safe_resolve`, `:549-565`); it runs its own static/file predicates | runs the row's command and pins **exit code + last stdout line** |
| floor | ≥1 `executed:` disposition | `CHECKLIST_RATIO` line, `floor={{FLOOR_F}}` |
| failure mode | reworded/added/removed box fails (box text sha256) | `ITEM-FAIL` (exit mismatch / TIMEOUT) · `ITEM-LASTLINE` via the last-line ERE, plus `UNMATCHED-ITEM`/`UNMATCHED-LEAD` for the bijection |

The connector lane read the sibling sources (source inspection only, no sibling
verifier run — `scratch/SiblingConnector.md`) and its verdict sharpens the map:
**no sibling implements `item → runnable command → per-item verdict`**, so this
gate duplicates nothing fleet-wide. Its three answers for the integrator, relayed
not absorbed: (1) *no duplicate*; (2) the useful shared shape is a **stable-ID
outcome ledger** — a stable id plus an explicit disposition/result and an
unambiguous exit status — with kotoba's hash-pinned item→disposition map and the
other tools' named check ids as precedent, **without** reusing `executed:` to mean
arbitrary command execution or forcing kagi's TSV schema onto siblings; (3) relay
list: kasegi `anchorcheck.py` prints `MISSING-FILE`/`PAST-EOF` findings but
**never exits on `bad`** (exit 0 on detected findings) — an owner-side issue, not
kagi's; kake `scripts/probe-delta.mjs` is a history report, not a gate; any
cross-lane citation/evidence defect goes to its owner. Two honest divergences stay
unsmoothed: (a) kotoba has a third class (`delegated:`) this gate does not model;
(b) kotoba's `unexecuted:` reason is free-form while the by-hand reason here is a
closed class plus a uniqueness constraint — stricter on the class, weaker on the
wording. Unchanged from round 14: kumitate `scripts/proxy-check.mjs` counts
checklist-box lines as a *proxy term* (`C`) and recomputes scorecard ratios — it
checks no disposition and runs no row command; kumitate `scripts/round-gate.mjs`
checks round artifacts; kengaku `grader.py` replays committed experiment evidence.
The shared-contract question stays with the integrator; this round imports
nothing and pushes nothing into a sibling repo.

## Risks & ceilings (why 9, not 10)

- **No scheduling (operator scope, unchanged).** The gate answers when invoked.
  Nothing schedules it — the half of the operability ceiling that names
  systemd/cron is untouched by this round, by design: that decision touches host
  state and is not a lane-only move.
- **Premise-vs-duty relevance (the round-14 ceiling, translated).** A runnable
  row proves *its command ran and produced the expected last line*; it does
  **not** prove the command is the right reading of the item's prose. A
  true-by-construction row (`true`, `printf …`) paired with a strict-looking item
  would pass. The by-hand reason class records *why* an item is
  un-mechanisable, not that an attempt was made — the same shape as "a
  declaration is a pointer, not relevance" (`claim-ledger.md` bound 17) and "the
  floor is coverage, not evidence" (bound 19). {{LABRAT_BYCONSTRUCTION_RESULT}}
- **Last-line pinning is a narrow contract.** `expect_lastline` matches the last
  non-empty stdout line only; a check whose verdict appears mid-stream cannot be
  pinned by it — a design decision to state, not a defect to hide.
- **240 s timeout** caps any check that would need longer; the longest runnable
  row is `{{LONGEST_ROW_RUNTIME}}` (the existing deep probe/census paths are the
  reference for what a heavy check costs — `OP_REF_PROBE` ≈ 25 s).
- **The hygiene frame is the rows' own hard constraint**: items that would need a
  handler start/stop, a vault read, an `op` exec or an `op.env` read cannot be
  mechanised at all, so the Handler-operation half is expected to hold most of
  the by-hand rows — that is the *reason* the split is the shape it is, and the
  class vocabulary is what makes it auditable instead of silent.
- **No recursion**: no row may invoke `corpus/claim-ledger.sh`, even though
  checklist item 1 names `claim-ledger.sh verify` — the ledger's self-audit skip
  and this gate's row set are disjoint by construction.
- **A runnable row can be a false defect** — measured twice in the gate's own
  first contact: `H4`'s front-matter parse missed the last line (reporting a
  correct host as widened) and `E4`'s sweep caught three documented placeholder
  literals (reporting prose as a leak). A row is only as strong as its check, and
  the report must not treat `failed=N` as a host verdict without reading the
  check.
- **The `E4` exclusion is a name allowlist** (`vault|FakeVault|wal`) — L1 names
  this as the class's weak point: any *other* placeholder vault name trips the
  row, and a real ref whose vault happened to be named `vault`/`FakeVault`/`wal`
  would be invisible to it. The robust test (item-id shape/width) is not what
  shipped; that gap is stated, not hidden. {{E4_ALLOWLIST_DISPOSITION}}
- **The 9/7 split is criterion-dependent, and two readings disagree.** The shipped
  criterion is *"is there a command whose verdict is a defect signal for this
  item"*, with the remaining operator duty named in the row's `note`; the planner
  lane's stricter duty-vs-premise reading measured **3 runnable / 13 by-hand**.
  Both are recorded; the report quotes the shipped number and the dissent, and
  does not claim the split is the only honest reading. {{SPLIT_DISSENT_LINE}}
- **The forbidden sentence stays unwritten**: this round never claims the
  checklist items are *verified* or *machine-checked*; it claims {{POST_RUNNABLE}}
  of 16 items produce a verdict when run, and that the remaining
  {{POST_BY_HAND}} are a named, counted, reasoned set.

## Evidence commands

```
# the new gate (shipped revision — all lines below are PLACEHOLDERS for the green re-run)
bash corpus/checklist-run.sh
  → CHECKLIST_RUN: CLEAN (items={{ITEM_COUNT}} runnable={{RUNNABLE_K}} by_hand={{BY_HAND_M}} failed=0)   exit 0
  → CHECKLIST_RATIO: runnable={{RUNNABLE_K}}/{{ITEM_COUNT}} floor={{FLOOR_F}} by_hand={{BY_HAND_M}}
bash corpus/checklist-run.sh --list
  → CHECKLIST_LIST: rows={{ITEM_COUNT}} runnable={{RUNNABLE_K}} by_hand={{BY_HAND_M}}   exit 0
  → {{LIST_SAMPLE_LINE}}                       (one representative ROW line only)
bash corpus/checklist-run.sh --only {{DEMO_ID}}
  → {{ONLY_OUTPUT_LINE}}                                                                exit 0
bash corpus/checklist-run.sh --selftest
  → CHECKLIST_SELFTEST: PASS ({{SELFTEST_CASES}} cases)                                 exit 0

# pre-move proof (the same surface at 2486643): there was no gate to run
ls corpus/checklist*                     → No such file or directory
bash corpus/checklist-run.sh             → No such file or directory, exit 127
grep -rln 'Credential-hygiene\|hygiene checklist' corpus/*.sh   → no match (0 files)
# item census at 2486643, and over every SKILL.md-touching commit (never 15)
awk '/^## Credential-hygiene checklist/{f=1;next} f&&/^## /{exit} f&&/^- \[ \]/{c++} END{print c}' SKILL.md
  → 16
# lock attribution + unpinned symbols (the two committed-row defects)
grep -n 'lock' PROVINCE.md ; grep -n 'client.py' corpus/surface-census.tsv
for s in autoupdate target_authority_conferred 40961 OPENCODE_SERVER_PASSWORD; do grep -c -- "$s" corpus/*.sh corpus/*.tsv; done
  → 0 pins each at 2486643 (the sole 9222 hit is a sha256 digit run in corpus/stamps.tsv)

# siblings unchanged — RE-RUN and paste the actual lines; the values below are
# the round-14 close readings and must be replaced by this round's own output
bash corpus/surface-census.sh            → SURFACE_CENSUS: CLEAN (assets=20 runtime=15 scanned=4 ok=34 absent=2 skipped=0)  exit 0
bash corpus/drift-pins.sh                → DRIFT_PINS: CLEAN (files=15 symbols=20)     exit 0
bash corpus/op-ref-probe.sh              → OP_REF_PROBE: CLEAN (checks=44 oprun=12 refs=7 divergent=5 edge=10 sig=6)  exit 0
bash corpus/transcript-scan.sh           → TRANSCRIPT_SCAN: HITS=2                     exit 1 by design
bash corpus/claim-ledger.sh verify       → CLAIM_LEDGER: CLEAN ({{LEDGER_VERIFY_SUMMARY}})   exit 0
bash corpus/claim-ledger.sh cells        → CELL_AUDIT: CLEAN ({{CELLS_SUMMARY}})            exit 0
```

## Hygiene

No vault access, no `op` vault/item read, no read of `$CONFIG_DIR/op.env`, no
handler start/stop, no CDP/Chrome, no `op run`; the gate's own rows carry the
same prohibition, and `OP_*` values in any probe are fabricated. No secret value,
vault ref path, session token, cookie or transcript row in any artifact. All L2
execution was scratch-only; the only repo writes were L1's.
{{OUTPUT_DIR_AND_HYGIENE_CHECK_LINES}}

## TODO for L1 — facts still missing

1. **`{{ROUND15_COMMIT}}`** — `round-15` hash in `kagi-shokunin`.
2. **Gate numbers, taken from the run (never from this draft)**: `{{ITEM_COUNT}}`,
   `{{RUNNABLE_K}}`, `{{BY_HAND_M}}`, `{{FLOOR_F}}`, `{{TSV_ROWS}}`,
   `{{SELFTEST_CASES}}`, `{{LONGEST_ROW_RUNTIME}}`; the mode outputs
   `{{LIST_OUTPUT_LINES}}`, `{{ONLY_OUTPUT_LINE}}` (with `{{DEMO_ID}}`), and — if
   `--only` exists in the shipped surface — confirm the flag spelling. Also
   `{{LEDGER_VERIFY_SUMMARY}}` / `{{CELLS_SUMMARY}}` if the sibling ledger lines
   are quoted in §Evidence commands.
3. **The by-hand roster**: the ids in the by-hand class, each with its class and
   its ≥24-char note (the report should name them the way round 14 named the 3
   `Reverify: by-hand` entries).
4. **Which checklist items got a runnable row** — id → the command it runs, so a
   reader can see *which* of the 16 prose items became executable, and confirm
   the 5 command-naming items above are or are not among them.
5. **Pre-state execution of the gate path**: whether any `ITEM-FAIL` /
   `ITEM-LASTLINE` / `ITEM-FAIL … TIMEOUT` fired during landing, and the exact
   line if so.
6. **Ledger integration**: new row id `{{R15_ROW_ID}}` (the `CHECKLIST_RUN`
   summary as the claim) and which counted rows were re-pinned
   (`{{REPINNED_ROWS}}`: ledger row count, stamps rows, selftest count `R11-09`,
   README/PROVINCE lines).
7. **§L2 wave**: the dispatched lane list from `LOG.md` and one
   finding→disposition line per lane; the count `{{L2_LANE_COUNT}}` from the LOG,
   not from the roster in this draft. Replace every template row
   (`{{LANE_1}}`…`{{LANE_N}}` and their `{{LANE_N_FINDING}}` /
   `{{LANE_N_DISPOSITION}}` cells) — the
   shipped table must contain no `{{…}}`.
8. **Adversarial results that must be *executed* before reporting**: a
   true-by-construction row (`{{LABRAT_BYCONSTRUCTION_RESULT}}`), 16 duplicate
   by-hand notes (`{{DUPLICATE_NOTE_RESULT}}`), a row whose last line drifts
   (`ITEM-LASTLINE` proof), a denied-surface row (`POLICY` refusal), a genuinely
   failing row (`ITEM-FAIL`), and the recursion refusal
   (`{{RECURSION_REFUSAL_LINE}}`).
9. **Doc pointers**: `{{SKILL_POINTER_LINES}}`, `{{README_LINES}}`,
   `{{ENTRY_NAME}}` (the new `corpus/knowledge/*.md` entry, if there is one) and
   its `Reverify:` declaration; `{{DEPTH_CEILING_LINE}}` for the unchanged depth
   cell.
10. **Adjacency**: the connector lane's round-15 sibling sweep
    (`{{CONNECTOR_ROUND15_FINDING}}`) — and whether kotoba's
    `checklist-baseline.json` covers kagi's SKILL.md (it should not; confirm).
11. **Ceiling artefacts**: `{{LONGEST_ROW_RUNTIME}}`,
    `{{OUTPUT_DIR_AND_HYGIENE_CHECK_LINES}}`, and the exact `SCORECARD.md` line
    numbers this draft quoted (`:28`, `:176-180`, `:223-225`) — re-read them
    after the round-15 sections are appended, since appending shifts offsets
    below the insert point.
12. **The remaining §Before → after cells** — the *before* column is filled with
    this drafter's own measurements (`0` file, `0` executed items, `0` by-hand
    classes, `exit 127`); the *after* column stays placeholders:
    `{{POST_TSV_ROWS}}`, `{{POST_ITEMS}}`, `{{POST_RUNNABLE}}`, `{{POST_BY_HAND}}`,
    `{{NEW_CHECK_ROWS}}`, `{{NEW_CHECK_LIST}}`, `{{CHECKLIST_EXIT_ROW_ID}}`,
    `{{WAVE_OPEN_QUESTIONS}}`. If the pre-move measurement moved (the SKILL
    checklist edited), re-measure and say so.
13. **Re-measure the three pre-state numbers in §The finding** at the frozen
    pre-move revision if the SKILL checklist itself was edited during the round
    (16 items / 5 naming a command / 0 gates reading it); if the checklist prose
    changed, say so and give both readings.
14. **Gate evidence — CONFIRM, then paste.** `[L1 live run]` already reports
    `CHECKLIST_RUN: CLEAN (items=16 runnable=9 by_hand=7 failed=0)` exit 0,
    `CHECKLIST_RATIO: runnable=9/16 floor=8 by_hand=7`,
    `CHECKLIST_SELFTEST: PASS (28 cases)`,
    `CHECKLIST_LIST: rows=16 runnable=9 by_hand=7`. Re-run at the shipped
    revision and paste; take `--only <id>` and one `ROW …` line from the same
    run. The two phase-1/phase-2 defects (`:209`, `:212-213` aborts; `H4` parse;
    `E4` sweep) are **fixed** and belong in the report's own defects table, not
    in the TODO.
15. **Resolve the remaining landed-vs-brief tokens**: `{{SKIPPED_FIELD_CLAUSE}}`
    (the shipped verdict has **no** `skipped=` field — say where the brief's form
    was superseded), `{{FLOOR_CLAUSE}}` (state the floor expression the code
    implements, observed `floor=8 = ceil(16/2)`), `{{DIVERGENCE_DISPOSITION}}`,
    `{{POLICY_ROW_EVIDENCE}}` (the `DENY_CHECK` refusal actually exercised),
    `{{NEW_CHECK_ROWS}}` / `{{NEW_CHECK_LIST}}` (snapshot read: 5 — `E4 E8 H3 H4
    H8`), `{{LIST_SAMPLE_LINE}}`, `{{UNPINNED_SYMBOL_DISPOSITION}}`,
    `{{LOCK_FIX_LINES}}`, `{{LONGEST_ROW_RUNTIME}}`, `{{E4_ALLOWLIST_DISPOSITION}}`,
    `{{SPLIT_DISSENT_LINE}}` (CheckPlanner's 3/13 reading vs the shipped 9/7).
16. **Posture/hygiene lines**: `{{OUTPUT_DIR_AND_HYGIENE_CHECK_LINES}}` — if any
    lane read `$CONFIG_DIR/op.env`, started/stopped the handler or launched
    Chrome, name it here instead of writing the standing posture sentence; the
    gate's own `E4` sweep is the artifact-side proof that no ref path was
    printed.
17. **Process note to record**: *this* draft's author deleted a `##` heading
    (`## Before → after`) by anchoring an edit on it and not reproducing it — the
    exact round-14 trap, caught here by a heading census and restored. L1's
    landing edits hit the same class from the other side (a parse anchored on a
    regex that assumed a trailing newline). Recording both is the point.