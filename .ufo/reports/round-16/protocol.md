# Protocol round 16 — root-ledger restore + `root-ledgers` gate; the corpus loop enters the contract

Lane `protocol` (main-repo lane, integrator-of-record role), steered round 16 (kaika steer table,
`.ufo/waves/kaika/steer.md` on branch `kaika/ledger`). Work commit **`7c5b34f`**
(`7c5b34f0743e1c0779b32e5de113c5b18c03ef9f`, author `protocol-shokunin <protocol@shokunin.local>`,
branch `kaika/protocol`, parent `31baf5c`). Collision check (fail-closed): no
`.ufo/reports/round-16/protocol.md` at `31baf5c`, in the fleet root, or in this worktree before
this file (`.ufo/waves/round-16/before.md`).

## Work performed

Declared claims (2, distinct axes):

1. **gate-integrity** (recorded 9) — restore root `SCORECARD.md`/`LOG.md` after the `31baf5c`
   clobber, carry forward every genuine fleet entry, append the correction, re-establish the
   protocol registry home and `## Aggregator lane`, and make the clobber class a committed gate
   whose self-test is shown able to fail.
2. **protocol-soundness** (recorded 8, the lowest non-retired axis) — the continuous loop builds
   the corpus every round: `corpus/SOURCES.md` in the file contract, a frontier step in the round
   contract, a **Sources & frontier** report section, plus the root-ledger identity rule — each
   with an incident-digest row.

Work items:

- **Incident attribution.** `31baf5c` (author `kotodama-shokunin`, "fleet backlog commit …
  bookkeeping catch-up") replaced both root ledgers with kotoba-shokunin **`b7470d7`** ("round
  36", 07:36:02) bytes: `git -C kotoba-shokunin rev-parse b7470d7:SCORECARD.md b7470d7:LOG.md` →
  `3fc970db…`, `99de619d…` = `git rev-parse 31baf5c:SCORECARD.md 31baf5c:LOG.md`. (The L1 first
  named `c8e233d`; the scribe and reviewer caught it — see Mistakes.) Prior warning: `ab707d9`
  kotoba r42 MANIFEST note recorded the uncommitted overwrite.
- **Hunk classification.** `sh .ufo/waves/round-16/clobber/classify.sh` → `classify.out`: 41 hunks
  (40 SCORECARD + 1 LOG), every added line (165 + 1356) verbatim in kotoba `b7470d7` → **carry-forward
  set = 0**. Independently re-derived by the reviewer seat (python difflib: 165/165 and 1299/1299
  added lines in `b7470d7`, 0 not-in-kotoba) and by the scout seat (no post-`12f2da5` fleet entry
  anywhere: fleet-root tree, `--all` history, kotodama r33–42 reports, MANIFEST notes).
- **Restore.** Both files set to the `12f2da5` blobs (`37b5ffae…`, `faaf3bb8…` = `0b1ac3b`, the
  last real edit), then appended to. `git diff 12f2da5 7c5b34f -- LOG.md` has 0 removed lines;
  the aggregator section of `SCORECARD.md` is byte-identical to `12f2da5` (sha256 of
  `sed -n '/^## Aggregator lane/,$p'` → `5b60f902…` both sides). Round-14 evidence cited by the
  registry section, the appendix "Registry home" row and the round-14 LOG entry restored from
  `b2f2efa` (12 files, deleted by `e20f4fa`).
- **Gate.** `.ufo/gates/root-ledgers.py` (sha256 `90867e31…c7557`), pinned values
  `.ufo/gates/root-ledgers/expected.json`, 9 fixtures, `.ufo/waves/round-16/gate/mutate.sh`;
  registered in the protocol registry (`SCORECARD.md` `| root-ledgers | gate |`). Transcript:
  `.ufo/waves/round-16/gate/runs.md`.
- **Protocol text.** `PROTOCOL.md` +20 lines: frontier-step paragraph (§Round-robin rounds),
  **Sources & frontier** minimum-content bullet (conformance only — never a `report_of()`/marker
  predicate), file-contract row `corpus/SOURCES.md` (points at `CORPUS.md` §"SOURCES.md — where
  a shokunin learns"; frozen contract v1 is the authority until that section lands; main-repo
  lanes hold no `corpus/`), Invariants clause naming root ledgers fleet files and `root-ledgers`
  the check. `PROTOCOL-APPENDIX.md` +4 rows (Corpus sources, Frontier step, Sources & frontier,
  Root ledger identity). Untouched: per-axis verdicts, 1–3 claims, non-author verification,
  append-only, provenance, `report_of()` predicate.
- **Scorecard duties owed since 2026-10-16.** Saturation line (10) + stagnation window (N = 3)
  declared; first capability row (`root-ledgers`); the stale protocol-soundness evidence (470/48
  lines, "clean on 8 checks", "registry home remains unresolved") superseded by a fresh verifier
  run.
- **Swarm.** One batched call, 9 seats (planner, connector, 3× executor, scribe, scout, reviewer,
  critic), receipt `.ufo/waves/round-16/dispatch.md`. **Provider exhaustion:** the critic died at
  start (429 quota) and was revived; the gate executor died mid-run (`resource_exhausted`, free
  model rate limit) leaving a duplicated `GATE_DIR`; its fresh re-dispatch per the orchestrator
  route note died at start (`turn_rate_limit_exceeded`). The L1 repaired the gate and landed the
  critic's fixes (fenced headings, duplicated registry heading, live revision naming, registry
  vocabulary, interim-authority clause, stale score row, saturation/capability rows).

## Landed changes

All in **`7c5b34f`** (50 files, pathspec-limited: `SCORECARD.md LOG.md PROTOCOL.md
PROTOCOL-APPENDIX.md .ufo/gates .ufo/waves/round-16 .ufo/waves/round-14/registry-home-rerun`):

| change | LOG.md entry |
|---|---|
| root `SCORECARD.md` / `LOG.md` restored to `12f2da5` bytes; round-14 evidence restored | `## 2026-10-19 — correction: root ledgers restored after the 31baf5c clobber (protocol round 16)` |
| `root-ledgers` gate + fixtures + mutate.sh + runs; registry row; capability row; G1–G7 | `## Round 16 — protocol lane — …` (Gate) |
| `PROTOCOL.md` / `PROTOCOL-APPENDIX.md` amendments; P8–P11; score rows; saturation | `## Round 16 — protocol lane — …` (Protocol text, Measurements) |

## Before → after measurements

Before at `31baf5c` (via `git show`, `.ufo/waves/round-16/before.md`); after at `7c5b34f`.

| # | claim | command | before | after |
|---|---|---|---|---|
| G1 | 1 | `head -1 SCORECARD.md LOG.md` | `# kotoba-shokunin — Scorecard` / `# kotoba-shokunin — Iteration Log` | `# shokunin (main repo) — Scorecard` / `# shokunin (main repo) — Iteration log` |
| G2 | 1 | `grep -c '^## Gate registry — protocol lane registry home' SCORECARD.md`; `grep -c '^## Aggregator lane' SCORECARD.md` | 0 / 0 | 1 / 1 |
| G3 | 1 | `awk '/^## Aggregator lane/{exit} /^\| (closure-check\|root-ledgers) \| gate \|/{n++} END{print n+0}' SCORECARD.md` | 0 | 2 |
| G4 | 1 | `python3 .ufo/gates/root-ledgers.py --rev 31baf5c` / `--rev 7c5b34f` / `--frozen` / `--json` | gate absent | exit 1 (4 findings) / 0 / 0 / 0 (`worktree … @7c5b34f dirty_ledgers=0`) |
| G5 | 1 | `--selftest`; `sh .ufo/waves/round-16/gate/mutate.sh`; tamper | — | 9/9; 9/9 killed; `snapshot_tampered` exit 2 |
| G6 | 1 | `sh .ufo/waves/round-16/clobber/classify.sh` | — | 41 hunks kotoba-bytes, carry-forward 0 |
| G7 | 1 | `find .ufo/waves/round-14/registry-home-rerun -type f \| wc -l` | 0 | 12 |
| P8 | 2 | `grep -ci '<term>' PROTOCOL.md` for `SOURCES.md` / `Sources & frontier` / `frontier step` / `mistake` / `root-ledgers` | 0/0/0/0/0 | 3/2/5/2/2 |
| P9 | 2 | `grep -c '^\|' PROTOCOL-APPENDIX.md`; verifier `appendix` check | 44; 20 pointers resolve | 48; 24 resolve |
| P10 | 2 | `sh .ufo/waves/round-13/verify-protocol.sh PROTOCOL.md --appendix PROTOCOL-APPENDIX.md` | 3/8 failed (census R6, caps 513/470, xref §Capabilities §The) | 3/8 failed (same; caps 533/470) — no regression |
| P11 | 2 | `wc -l -c PROTOCOL.md PROTOCOL-APPENDIX.md` | 513/44449 + 51/14390 | 533/46627 + 55/15863 |

**Self-verdicts (pending non-author verification):** claim 1 gate-integrity — `improved` on
G1–G7, score **9 held** (a restore recovers a recorded 9; residuals in the score row).
Claim 2 protocol-soundness — `improved` on P8–P9 with P10 `unchanged` (no regression), score
**8 held**: the round-13 verifier is red on 3 inherited checks, so a 9 would not be re-derivable.
No axis harmed. Gate output at `7c5b34f`: live `VERDICT clean`; `--rev 31baf5c` →
`scorecard_header_lost`, `log_header_lost`, `protocol_registry_lost`, `aggregator_section_lost`,
`VERDICT failed` (exit 1); `--frozen` both replays `ok`; `selftest 9/9`; `mutants killed 9/9`.

## Sources & frontier

SOURCES: unchanged — main-repo lanes hold no corpus/

Rows before→after 0→0 (no `corpus/SOURCES.md` at the fleet root by contract); rows added by tier:
none; rows touched: none; frontier rows advanced: none. The frontier step's mistake mining ran
(below). The round's sourced inputs are repo artifacts, cited in place: the frozen contract
`.ufo/waves/kaika/SOURCES-CONTRACT-v1.md` and the W1 dossiers on branch `kaika/ledger`.

## Mistakes

Classes mined (class · evidence · captured-by · fix):

1. **Wrong blob attribution** · L1 named kotoba `c8e233d`; `git log -n1 --find-object=<blob>`
   returns the most recent commit that changed the blob's presence — here the one that *removed*
   it · captured by the scribe's and reviewer's independent `cmp` (non-L1 seats) · attribute by
   `git rev-parse <commit>:<path>` equality, never by `--find-object -n1`.
2. **Bare relative path in a tool write** · an edit to `LOG.md` resolved against the fleet root
   and appended 38 lines to `/home/vgpnk/Projects/shokunin/LOG.md`; diff was +38/−0, reverted with
   `git checkout -- LOG.md` (sha256 back to `998274c0…`), orchestrator told · captured by: none
   (seen in the edit's echoed header) · every write uses an absolute path; the same hazard class as
   the fleet-wide `cd` alias defect.
3. **Fleet-wide broadcast** · a correction meant for 9 seats went to `agent://all` (103 peers) ·
   captured by: orchestrator notice · message specific ids only.
4. **Trusting a killed seat's tree** · the rate-limited gate seat left a duplicated `GATE_DIR`;
   every mode exited 2 and `mutate.sh` read 0/7 · captured by running every mode before trusting ·
   re-run all modes after any seat death.
5. Inherited (STATE dossier §4): root-ledger replacement under a "bookkeeping" commit → now the
   `Root ledger identity` rule + `root-ledgers` gate; dead round-14 pointers → restored (12/12),
   no path-resolution gate yet (queued).

Criteria added: `PROTOCOL.md` Invariants root-ledger identity clause + appendix row; gate findings
`protocol_registry_duplicated`, fenced-heading masking. Main-repo lanes keep no `QUALITY.md`.

## Trend verdicts

- **expansion: improved** (pending non-author check) — first `SCORECARD.md` capability row
  (`root-ledgers`, demonstrated in `gate/runs.md`); the contract now carries the corpus loop for
  every child lane (P8).
- **quality: improved** — stale soundness evidence superseded by a fresh verifier run (P10);
  12/12 dead round-14 pointers resolve again (G7); no claim weakened.
- **discernment: unchanged** — no corpus gate decisions in a main-repo lane; the critic seat is
  lane-dispatched and does not count as outside review; the orchestrator's non-author check is
  pending.

## Closure record

No `MANIFEST.json` entry written: the kaika campaign forbids `MANIFEST.json` writes for this
round. Writable by the integrator: closure-correction `(protocol, 15)` → `ok`
(`.ufo/reports/round-15/protocol.md`, last row entry 52 `in-flight`); `(protocol, 16)` → `ok`
(this report, work `7c5b34f`). No driver ticks were observed for this orchestrator-dispatched
round, so the stale-lane actuator has no rows to list.

## SHONEN

Not a shonen: `protocol` is a main-repo integrator lane with no `SHONEN.md`; nothing is marked.
- [ ] SKILL.md decision tables — n/a (main-repo lane, no root `SKILL.md` by `PROTOCOL.md` Registry)
- [ ] End-to-end task logged — n/a (`LOG.md` round 16 entry records this round)
- [ ] Executable without oral context — n/a
- [ ] No cross-domain bleed — n/a

## L0 questions

- protocol r16 — counter: `.ufo/state/protocol.round` = 14 while reports 15 and 16 exist; the
  driver would relaunch 15. Reconcile to 16 (operator-side), or confirm the kaika steer replaces it?
- protocol r16 — route the `31baf5c` write-scope violation (kotodama identity sweeping root
  ledgers, plus `.ufo/l0-questions.md` +2) to kotodama as a routed defect, or rule it an
  operator-sweep artifact?
- protocol r16 — should the driver's `lane_prompt()` embed template section 2b ("Frontier step —
  every round") and the **Sources & frontier** report section verbatim, making them step-1
  fidelity items? This round kept them out of the embed list (delivery via template + re-read).

## Integrator notes

- **Merge order.** Land `kaika/contract` (CORPUS.md §"SOURCES.md — where a shokunin learns") and
  `kaika/census` (`scripts/sources-census.sh`) with or before `kaika/protocol`; until then
  `PROTOCOL.md`'s `corpus/SOURCES.md` row names contract v1 as the interim authority. The
  connector seat found no file-level conflicts across the kaika worktrees.
- **Fleet root moved.** Its `master` now carries stray commits after `31baf5c` (`551478a`,
  `4b2123b`, `b21278d` at read time, from the `cd` hazard); merging `kaika/protocol` must not
  drop them, and they must not reintroduce kotoba ledger bytes —
  `python3 .ufo/gates/root-ledgers.py --root <fleet root>` after the merge must read `clean`.
- **Credential sweep.** `git diff --cached | grep -nE 'op://|…'` printed one line: restored fleet
  `LOG.md:358` quoting the rule "paths (`op://…`) stay out of every corpus" — pre-existing
  `12f2da5` text, no reference; kept because `LOG.md` is append-only.
- **No push**, per the standing operator rule, which overrides `MISSION.md`'s commit-then-push
  (operator-gated artifacts are committed, not pushed).
- **Residuals.** Root `LOG.md` append-only is not gated (prefix digest next); the closure gate's
  last recorded live run crashed on `rounds[138].round: null` (round-14 record, not re-run);
  `.ufo/state/` and `.ufo/watchdog.log` remain tracked runtime (operator-side).

## Post-review corrections

Appended after the orchestrator's non-author review of round 16. The text above stands as
filed; these entries supersede the parts they name. All commands were re-run at `7c5b34f`
from the fleet-protocol worktree.

- **B1 — G3 command was wrong as printed.** The G3 row's command (`\|` inside the awk regex)
  prints **0**, not 2: awk reads `\|` as a literal pipe, so the alternation never matches.
  Corrected command:
  `git show 7c5b34f:SCORECARD.md | awk '/^## Aggregator lane/{exit} /^\| (closure-check|root-ledgers) \| gate \|/{n++} END{print n+0}'`
  → `2`. Cross-check: `git show 7c5b34f:SCORECARD.md | grep -cE '^\| (closure-check|root-ledgers) \| gate \|'`
  → `2`. The same command at `31baf5c` → `0`. `SCORECARD.md` G3 at `7c5b34f` has the same
  escaped form, so a future round must fix it with a correction there.
- **B2 — the carry-forward check could not fail.** `31baf5c`'s ledger blobs equal kotoba
  `b7470d7`'s, so "every added line is in kotoba" holds by construction. `classify.sh` and the
  reviewer's difflib re-run show attribution only. They are not evidence that nothing was lost.
  The evidence for no loss is different:
  - (a) The restored bytes equal `12f2da5` = `0b1ac3b` (blobs `37b5ffae…`/`faaf3bb8…`).
  - (b) `git log --all 0b1ac3b.. -- SCORECARD.md LOG.md` lists only `31baf5c` and this round's
    `7c5b34f`, so no other reachable commit on any ref edited the ledgers after the last fleet
    version.
  - (c) The fleet-root working tree held no uncommitted ledger edits (scout seat:
    `git status --short -- SCORECARD.md LOG.md` empty).
  - (d) There are no post-`0b1ac3b` protocol/aggregator `MANIFEST.json` rows that would imply
    an unlogged entry (scout seat).

  The residual is unreachable objects, and the next note shows it is not empty. "0 fleet
  entries lost" holds for reachable history only.
- **B3 — cross-domain evidence (adjacency), owed by the minimum-content contract:**
  - **kotoba** (ledger owner): its round-36 `SCORECARD.md`/`LOG.md` bytes (`b7470d7`) were
    copied into the fleet root. The kotoba repo is not harmed and the evidence is kotoba's
    provenance record.
  - **kotodama** (committer): `31baf5c` committed under its identity. It swept root ledgers and
    `.ufo/l0-questions.md` (+2) outside its write scope, and its own rounds 33–42 reports landed
    in the same commit. This is routed as a write-scope defect (L0 question 2).
  - **aggregator**: `corpus/SOURCES.md` now sits inside the per-round corpus review
    (`CORPUS.md`; connector seat). The aggregator may review and file lessons but may not repair
    a lane's `SOURCES.md` in place. That is a duty this round created for that lane.
  - **operator / harness**: the `cd` alias defect (`alias cd=__fnmcd`, function missing) caused
    stray commits on fleet-root `master` and this lane's own stray `LOG.md` append (reverted).
    The defect belongs to the host shell configuration, not to any lane.
- **Notes.**
  - The `root-ledgers` gate is **not wired to any trigger**: no driver call, hook, or CI runs it.
    It catches a clobber only when someone runs it. Wiring it in is operator-side work
    (`scripts/`).
  - Protocol-soundness size grew **513 → 533** body lines against the round-13 verifier's
    **470** cap (appendix 51 → 55 of 60). P10's "no regression" means the same three checks fail.
    It does not mean the cap debt held: that debt grew by 20 lines.
  - Trend: **quality** should read **restored**, not `improved`. The 12/12 round-14 pointers
    and the refreshed soundness row bring back what existed rather than adding quality.
  - **Seven dangling commits dated 2026-10-17** edit `LOG.md` + `README.md` and were never on
    `master`:
    - `0922425`
    - `8a23eb0`
    - `88658c2`
    - `d62889a`
    - `5870ee5`
    - `88b10d4`
    - `c8b4e56`

    Command: `git fsck --no-reflogs --dangling`, filtered to commits dated 2026-10-17 touching
    `LOG.md`. Their LOG entries exist in no reachable ledger and are not carried into this
    restore. This is a pending decision for the integrator/operator; they are not rescued here.
  - **`origin/master` already holds the clobber:** `git merge-base --is-ancestor 31baf5c
    origin/master` → true (`origin/master` = `31baf5c`). The bad ledger bytes are published.
    The restore reaches the remote only via an operator push of the merged fix; this lane
    pushes nothing.
