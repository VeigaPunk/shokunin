# scribe seat — aggregator round 10 (L1 round-10 continuation)

Role: UFO-FSD scribe. This file records evidence facts, the required report shape, the
append-only handling of the historical marker, the canonical four SHONEN rows, and the open L0
queue. It asserts **no** promotion, verdict, or axis-move authority.

Measurement host: `/home/vgpnk/Projects/shokunin`, main HEAD `b598ce0e1d4fa8851d3e238ee6afde42bd57f787`
(`git rev-parse HEAD`), which is the `measured_commit` in `.ufo/waves/aggregator-r10/before.json`.
All reads below are read-only; no build/lint/test/formatter was run mid-flight beyond the
read-only gate invocations described (runtime measurement, not a test re-run).

---

## 1. Required report shape (`PROTOCOL.md` §Round reports / §File contract)

A file at `.ufo/reports/round-<N>/<id>.md` is a **report**, not a completion marker, only if it
carries all of:

| # | Requirement | Source |
|---|---|---|
| R1 | `SHONEN` heading (any level) with one `[x]` / `[ ]` / `[~]` line per box | `PROTOCOL.md` ~L147, ~L178 |
| R2 | Minimum substance: work performed with at least one evidence pointer (path / command / diff) | `PROTOCOL.md` ~L145-147, ~L178 |
| R3 | Changes landed in the child repo, each tied to a `LOG.md` entry | `PROTOCOL.md` ~L146 |
| R4 | Cross-domain evidence named with the domain it belongs to | `PROTOCOL.md` ~L147 |
| R5 | A checkable commit-hash citation | `PROTOCOL.md` ~L178 |

Machine grading (committed gate `cross-lane-gate-v1`,
`.ufo/waves/aggregator-r11/cross-lane-gate.mjs`): `MIN_REPORT_BYTES = 1024` (`:62`); kind
`marker-overwrite` fires below it (`:160`); kind `cited-commit-missing` for each referenced hash not
resolvable in the round's revision set; kind `verdict-without-revision` when a verdict word appears
with zero referenced hashes. Driver-side completion uses a looser bar (`SHONEN` heading + >=400 B,
`LOG.md` tail "Driver completion semantics — measured", no freshness check).

## 2. Historical marker vs. this appended round-10 continuation

These are **two distinct events** and must not be conflated.

**Previous (historical) failure — a closeout marker, already ledger-closed.**
- Path `.ufo/reports/round-10/aggregator.md`; **187 bytes**; md5 `75eaefe096ac72d22598809416888cfd`.
- Tracked; introduced by commit `f5d8507` ("fleet-wrap: sentinel + aggregator r10 closeout;
  respawn-per-round halted at current round per lane"). `git ls-files` confirms it is tracked.
- Verbatim body: "aggregator round-10 closeout (marker) / Fleet wrap: lane completed by operator
  directive before its report landed. In-flight work survives in the main repo working tree. Not
  respawning."
- Graded now by the committed gate (read-only re-measure):
  `node .ufo/waves/aggregator-r11/cross-lane-gate.mjs --report .ufo/reports/round-10/aggregator.md`
  -> `# finding XL-marker-overwrite marker-overwrite report=.ufo/reports/round-10/aggregator.md bytes=187`
  -> `# report … failed findings=1`. 187 < 1024, so the class is `marker-overwrite`.
- Ledger of record (`MANIFEST.json`): the original round-10 `closure` entry (entry 13,
  `closed_at 2026-09-28T18:21:16-03:00`) had `lanes.aggregator = "not-dispatched"` with
  `lane_rounds.aggregator = 6`. A later `closure-correction` (round 10, `closed_at
  2026-09-29T00:34:00-03:00`, `supersedes {round:10, entry:13}`) set `lanes.aggregator = "failed"`
  with `lane_rounds.aggregator = 10`, resting on driver lines: dispatch `2026-09-28T22:37:21-03:00`
  and completion `2026-09-29T00:19:29-03:00`, terminated with a marker. So the prior attempt is a
  ledger-recorded **`failed`** lane-round: a completion marker is not a report.

**This continuation — a new section appended, never an overwrite.**
- Contract (`# Contract`): the existing 187-byte file is an **immutable historical marker**; the
  round-10 wave appends a complete new report section and must not rewrite the old bytes.
- Byte-level acceptance: after the append, the first 187 bytes must still hash to
  md5 `75eaefe096ac72d22598809416888cfd` and the file must begin with the exact marker text quoted
  above. Evidence to capture post-append (L1-owned): `head -c 187 <path> | md5sum`.
- Because the appended section is what makes the path a report, the round-10 wave's own report must
  satisfy R1–R5 above; otherwise the path remains `marker-overwrite` for round 10 regardless of the
  append.

**Prior-marker-is-not-this-round evidence.** `before.json` records the *current* gate state:
`exit: 1`, `covered: 6`, `omitted: 13` (list in `before.json.omitted`). The marker's provenance
(`f5d8507`, 2026-09-29 00:19:29 -03) predates this wave (wave dir created 2026-10-15 01:46).

## 3. Canonical SHONEN four rows (`PROTOCOL.md` §File contract, canonical seed ~L419)

The seed has exactly four boxes; `<name>` is the only substitution. Canonical rows:

| Box | Text | Minimum bar (`PROTOCOL.md` §Promotion gates ~L70-74) |
|---|---|---|
| B1 | `[ ]` SKILL.md contains real decision tables, error patterns, checklists, cited sources | >=1 decision table, error-pattern list, and checklist, each citing a resolvable source |
| B2 | `[ ]` At least one end-to-end domain task executed and logged in LOG.md | an end-to-end task executed and logged |
| B3 | `[ ]` Instructions executable by an agent without oral context | `SKILL.md`/`corpus/` instructions self-contained with resolvable pointers |
| B4 | `[ ]` No cross-domain bleed (PROVINCE.md still accurate) | no cross-domain bleed; `PROVINCE.md` accurate |

Marks (`PROTOCOL.md` §File contract / §Promotion gates): `[~]` = asserted by the lane itself
(evidence pointer required); `[x]` **only** with a named non-author verifier (`[x] <verifier-id>`).
An `[x]` carrying no named non-author verifier is author attestation and **counts as `[~]` for the
gate**. Canonical form requires marks confined to the box char plus at most one indented evidence
line, no added/removed boxes, byte-identical seed modulo `<name>`, trailing newline.

### 3a. Why `[x]` cannot be granted by this wave

1. **No promotion authority in the wave.** The contract states L2s dispatched by the author are not
   independent promotion verifiers and "no `[x]` promotion claims" are permitted; this is a
   scribe seat with no verdict/promotion authority.
2. **The gate bars author attestation itself.** `[x]` requires a *named non-author* verifier. Boxes
   whose mark line carries no `<verifier-id>` are `[~]` by operation of the gate text, not by this
   seat's judgement.
3. **No SHONEN.md exists for the aggregator lane.** `ls SHONEN.md` at MAIN_ROOT -> No such file or
   directory. The four boxes grade *child* shokunin repos; the aggregator/protocol lanes are
   fleet-meta and own no child `SHONEN.md`. So the box-3-style assessment in this round belongs in
   the final report only, as the canonical four-box fleet assessment, and grants nothing.
4. **`[x]` independence is not machine-checkable from the graded tree** (`corpus-gate.mjs`
   `not_evaluated` entry `box-3`: verifying that an `[x]` rests on a non-author verifier needs the
   authorship graph of past rounds, which the graded tree does not carry; the shonen check sees a
   verifier-id token, not its independence).

### 3b. Canonical-form census (read-only, counts only)

`grep -c '^- \[' <lane>/SHONEN.md` (boxes) and `grep -c '^- \[x\]'` (`[x]` counts), over the 19
direct child directories:

| Lane | boxes | `[x]` | `[x]` mark line carries an inline named verifier-id? |
|---|---|---|---|
| audio-shokunin | 4 | 4 | yes (named non-author per box) |
| chousa-shokunin | 4 | 0 | n/a |
| game-dev-2d-shokunin | 4 | 0 | n/a |
| game-dev-3d-shokunin | 4 | 1 | yes (named reviewer id) |
| kagi-shokunin | 4 | 4 | **no** — bare `[x]`, evidence prose on continuation lines only |
| kaidoku-shokunin | 4 | 4 | **no** — bare `[x]` |
| kake-shokunin | 4 | 0 | n/a |
| kama-shokunin | 4 | 4 | **no** — bare `[x]` (explicitly marks "Promotion not claimed" below) |
| kasegi-shokunin | 4 | 0 | n/a |
| kengaku-shokunin | 4 | 1 | **no** — bare `[x]` |
| kotoba-shokunin | 4 | 0 | n/a |
| kumitate-shokunin | 4 | 0 | n/a |
| lore-shokunin | 4 | 0 | n/a |
| mado-shokunin | 4 | 4 | yes (`VER-M3`, `VER-M4B` style named verifier ids) |
| mori-shokunin | 4 | 0 | n/a |
| revenger-shokunin | 4 | 4 | yes (named non-author `revenger-promotion-review`) |
| tabi-shokunin | 4 | 4 | **no** — bare `[x]` |
| tameshi-shokunin | 4 | 4 | **no** — bare `[x]` |
| tsukuroi-shokunin | 4 | 0 | n/a |

All 19 direct child repos carry exactly **4** boxes (no added/removed boxes). Box counts add to
4x19 = 76. Lanes whose `[x]` marks bear no inline `<verifier-id>` (kagi, kaidoku, kama, kengaku,
tabi, tameshi) therefore count as `[~]` for the gate on those boxes. This is a form observation
only; whether a box claim is *true* is prose and is `not_evaluated` by the machine check
(`corpus-gate.mjs` `shonen-semantics`).

## 4. Open L0 questions, by topic and owner

`.ufo/l0-questions.md` is append-only (25 lines; 18 question lines; sections: pre-2026-10 body,
then `--- 2026-10 relaunch ---`, then the L0 grammar line). Cite by owner + round + opening words,
**never** by line number (numbers move). No new unreachable operator decision was found this wave,
so **no line is appended** by this seat.

| Topic | Owner | Round | Question (opening words) |
|---|---|---|---|
| Repo custody / stalled git state | kasegi | 12 | `bounties` stalled mid-interactive-rebase; is the stall intentional or should it be resolved, by whom? |
| Province-root loss (FS prune regime) | kasegi | 15 | `~/Projects/bounties` — the kasegi PROVINCE root — is gone from the filesystem |
| Second in-round source loss | kasegi | 16 | open-bug-bounties `.ufo-missions/groknight` lost 8 mission dirs |
| Corroboration of the prune regime | kake | 15 | same-window FS drift hit kake citation base |
| Corroboration update (escalating) | kake | 16 | five distinct deletion/mutation instants inside round-16 |
| FS-cleanup/prune regime W6 | kake | 17 | lowercase `~/projects` absorbed into `~/Projects` and removed |
| Mint decision | protocol | 10 | kama mint decision (pending since round 2/4) — recommendation: mint |
| Operator-side driver/template debt | protocol | 10 | `lane_prompt()` emits 1 of 5 contract items; `report_of()` completes on file existence; `.ufo/state` tracked |
| Secret redaction correctness | kagi | 10 | `cmd_refs` redaction is a prefix match; tighten to whole-value? |
| Timer state / automation retirement | kake | 12 | `webzites-keeper.timer` never fired — enable or retire the keeper-tick path? |
| Axis vocabulary split (D-78) | aggregator | 6 | `novelty` / `consistency` not defined in `AXES.md` yet worked by lanes |
| Gate convention fleet-wide | kengaku | 10 | promote the gate convention (exit 0/1/2 + `--selftest`) into `PROTOCOL.md`? |
| Driver-level round gate | kumitate | 10 | adopt `round-gate.mjs` at the driver level (a)/(b)/(c)? |
| Machine-readable scorecard block | kumitate | 11 | fleet adoption of the `<!-- …-proxy-v1 … -->` claim block? |
| Axis-accounting ratification | kotoba | 13 | (1) may a lane work an advisory axis as its lowest-axis move; (2) D-78 still open |
| `CORPUS.md` amendment set | aggregator | 9 | rule 8 literally bans vault-ref-scheme paths that all six child corpora carry; four measured conflicts |
| Local model endpoint drift | kama | 1 | pins on `127.0.0.1:8080` vs the live server on a different port; three appended lines |
| Snapshot scheduling | kama | 2 | should the operator create/enable a systemd user timer for `kama-probe.sh snapshot`? |
| Operator approval request | tabi | 5 | R1/R2/R3 by ID (third-party read-only URL, operator's own site, budget) |

Owner counts: kasegi 4, kake 4, kama 3, protocol 2, aggregator 2, kumitate 2, kagi 1, kengaku 1,
kotoba 1, tabi 1.

## 5. Route-table evidence pointer (no alias strings copied)

- **Pointer:** `~/.omp/agent/config.yml:318-332`. That range is the `agentModelOverrides` mapping:
  14 taxonomy role ids (`connector, critic, distiller, executor, labrat, main, mutation-tester,
  planner, revenger, reviewer, scout, scribe, sentinel, simplifier`) each bound to a route alias.
- Per the contract, the aliases/model strings are **not** reproduced in this lane repo; only the
  file path + line range and the role-id set (already public in `PROTOCOL.md`/`MISSION.md`) are
  cited. A reader resolves the aliases at the pointer.
- Binding rule (`MISSION.md` §Fleet shape): each lane declaration carries a `route` **resolved
  through the host model route table, never a bare model alias**; all L1 lanes dispatch on the
  `swe`-class route. `MISSION.md` §L2 concurrency maps role *classes* to route *buckets*
  (planner/connector -> heavy-reasoning; executor/scribe/scout -> fast-execution;
  reviewer/critic/sentinel/revenger/labrat/mutation-tester/simplifier/distiller -> economy with
  fast-execution fallback).
- Two conformance notes (reported, not ruled):
  - The host routes via **each supplied taxonomy role**, never via model parameters; a normal
    batched task is the OMP mapping for the required heterogeneous shokunin swarm, **not** a UFO
    wave. The UFO-wave path is prohibited by its own separate validator, and `planner` is
    prohibited by that validator.
  - `MISSION.md` mentions a *route override file* alongside `shokunin.conf`; this wave did not read
    it (out of scope) and names it as unverified.

## 6. Conformance defects identified (report-only; no authority to rule)

1. **Corpus-gate `--all` coverage defect (the selected move).** `DEFAULT_REPOS` is hardcoded to 6
   lanes at `.ufo/waves/round-9/corpus-gate.mjs:165-172` and used at `:852` (`o.repos || DEFAULT_REPOS`).
   MAIN_ROOT has **19** direct child directories; `--all` covers 6, omits 13 (`before.json`:
   `covered: 6`, `omitted: [audio, chousa, game-dev-2d, game-dev-3d, kaidoku, kama, lore, mado,
   mori, revenger, tabi, tameshi, tsukuroi]-shokunin`). The selection regex
   `/^[a-z0-9][a-z0-9-]*-shokunin$/` matches all 19 (verified with `node -e`, including the
   digit-bearing `game-dev-2d`/`game-dev-3d`). Falsifiable coverage failure: 13 of 19 lane
   directories are unreported by the default fleet command.
2. **Missing-directory handling is already exit-2-class.** `.ufo/waves/round-9/corpus-gate.mjs:856`
   pushes `EXIT.CNE` (=2) for an absent discovered dir; `:328` returns `EXIT.CNE` when `corpus/` is
   absent or not a directory. So the selection contract's "missing corpus/git becomes explicit
   exit-2, never silent" is consistent with the existing exit map (`0 clean / 1 failed / 2 CNE /
   3 drift`, precedence `2 > 3 > 1 > 0`) — an axis the fix must preserve, not change.
3. **Frozen expected snapshots must stay intact.** `.ufo/waves/round-9/corpus-gate.expected.json`
   holds `frozen_round 9`, **8** frozen keys (kasegi@`b7180b0`, kengaku@`f09ff1f`, kake@`a209441`,
   kake@`4c9a985`, kumitate@`7a099b2`, kotoba@`63ceba7`, kagi@`4b8c018`, kagi@`4391b3b`) and **12**
   selftest cases; the file is hand-authored and read-only to the gate (`_what`). Re-ran
   `node .ufo/waves/round-9/corpus-gate.mjs --selftest` -> `# selftest tally 12/12 PASS`.
4. **Historical marker is a live conformance defect on the round-10 path.** The 187-byte file is
   graded `marker-overwrite` (Section 2). Until a real report section lands appended, round 10's
   aggregator path is non-conformant.
5. **No root `SHONEN.md`.** `ls SHONEN.md` -> absent. The canonical four-box assessment for the
   fleet-meta lanes has no lane file to attach to and must live in the final report.
6. **SHONEN mark-form gaps** (Section 3b): 6 lanes' `[x]` marks carry no inline `<verifier-id>` and
   therefore count as `[~]`; reported as form, not as truth claims.
7. **Wave-dir untracked.** `git status --short` shows `?? .ufo/waves/aggregator-r10/` at HEAD
   `b598ce0`. `.ufo/waves/` artifacts are committed with the round's integration commit
   (`PROTOCOL.md` §Invariants); L1 owns the commit — this seat does not commit.

## 7. Non-claims / limits

- No axis score is asserted; no verdict is emitted; no promotion is proposed.
- No scalar/blended verdict was computed or is proposed (per contract).
- The `corpus-gate` `--all` fix, the append, and any main-repo commit are L1 work; this seat
  supplies measured facts only.
- Route aliases were read once at the pointer to confirm the role set; no alias/model string is
  reproduced here.