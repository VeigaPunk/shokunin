# Round 9 aggregator corpus verdict — kake

Measurement stamp: 2026-09-29 (session), kake landed HEAD `a209441`, worktree dirty count `0`; main HEAD at final coordination was `62fdfbe` (moving-wave notice). All primary rule cells below are for `a209441`; the required box-3 cold re-check is separately against `4c9a985`.

## Dirty-tree / revision attribution

The task's `4c9a985` DIRTY-5 state no longer exists. Immediate re-check: `git -C kake-shokunin rev-parse --short HEAD` → `a209441`; `git -C kake-shokunin status --porcelain=v1 | wc -l` → `0`. `4c9a985` is the prior aggregator-identity commit and an ancestor. `git diff --name-status 4c9a985..a209441` lists seven landed files: `LOG.md`, `SCORECARD.md`, `SKILL.md`, `corpus/knowledge/free-read-verbs.md`, `corpus/knowledge/keeper-timer-inert.md`, `corpus/knowledge/ops-automation.md`, `corpus/knowledge/publish-queue.md`. These are lane-owned round-14 changes, not aggregator or operator changes. The historical five uncommitted entries cannot be reconstructed from the clean tree; any claim about their exact former membership is `[INFERENCE]`. No decisive worktree-only claim remains at `a209441`; claims based only on the former dirty state would have been provisional.

## Rule checks (CORPUS.md numbering)

| Rule | Verdict | Command and observed result |
|---|---|---|
| 1 source on knowledge entries | **not conformant** | `find corpus/knowledge -type f | wc -l` → `16`; Python/awk marker sweep → `15` files with source/evidence/command/URL markers. One file lacks a detected source marker. |
| 2 lesson round + evidence | **conformant** | `find corpus/lessons -type f | wc -l` → `16`; marker sweep for `round-|commit|LOG.md|report|evidence` → `16` files matched. |
| 3 falsifiable/opinion | **not conformant** | The landed corpus retains unqualified historical claims; e.g. `corpus/knowledge/ops-automation.md`'s identity equation defect is recorded in ledger D-68 (`AGGREGATE.md:726`) as false on 11/76 rows. |
| 4 count carries command/date | **not conformant** | `grep -n '/tmp/\|total\|rows\|count' corpus/knowledge/*.md corpus/lessons/*.md` plus ledger D-68/D-58 review: D-68 records counts without a command/validity window; D-58 records kake SCORECARD rows lacking count-command+commit. |
| 5 negative carries sweep | **not conformant** | `git grep -n 'absent\|never\|zero\|no ' HEAD -- corpus` finds negative claims; ledger D-56 records a kake-style negative without its sweep in the lane file. |
| 6 quote names location | **not conformant** | `git grep -n '/tmp/' HEAD -- corpus` finds session-artifact pointers; ledger D-57 records committed kake evidence pointers under `/tmp`, which do not identify durable file locations. |
| 7 index row only after file exists | **conformant** | `find corpus -type f | wc -l` → `41`; corpus README coverage and all listed lesson/knowledge paths resolve in the landed tree (no missing index target observed). |
| 8 no credential material | **FAIL-literal / PASS-intent** | `git grep -n 'op://' a209441 -- corpus` → exactly 2 hits: `corpus/lessons/round-5-aggregator-audit.md:54` and `corpus/lessons/round-6-aggregator-audit.md:56`. Both are schematic sweep-pattern examples, not resolvable vault item/field paths; no secret value observed. Under literal CORPUS.md:43-46, examples still fail rule 8; this conflicts with inherited round-6 “pass” interpretation and is an integrator/operator amendment row. |
| 9 corrections append-only/no cross-lane edits | **not conformant** | `git log --all -- corpus/lessons/round-8-aggregator-box3-coldrun.md` shows aggregator-owned amendment history; ledger D-24/D-67 record future-dated evidence and D-50 records the cross-lane correction violation class. |
| 10 per-round verdict emitted | **conformant for this seat** | This file emits a named verdict against `a209441`; the canonical rule-10 baseline was `AGGREGATE.md:604`: kake `dd4eabf`, not conformant — rules 4,1, 5 majors/11 defects. |


## Box-3 re-check at required `4c9a985`
`git archive 4c9a985 | tar -x -C /tmp/kake-r9` → 41 files, 16 knowledge files, 16 lesson files. `git show 4c9a985:corpus/lessons/round-8-aggregator-box3-coldrun.md` retains `[x]` and states the 15-command battery: `command -v webzites` empty; 21 fleet rows; 18 snapshot rows; `status --json` exit 0; `grokbots --check` exit 1 with `FAIL lucario: no registry row`; 20 keepers/17 wrappers; probe-delta 6 events/0 phantom; dead-slot 404 sentinel; stale 2026-09-26 pin vs live 2026-09-28 beat. Each is **still provisional**, for one reason: the cold-run lesson itself says the decisive measurements were made against a moving dirty tree (`2a5502c` with dirty entries), not the committed `4c9a985` input snapshot; no committed gate/self-test or committed expected finding-id reran that battery at `4c9a985`. The current `a209441` lane landing makes the text stable, but does not retroactively make the required historical 4c9a985 measurement reproducible.
**Rule-10 verdict:** **not conformant — rules 1, 3, 4, 5, 6, 8, 9** at landed HEAD `a209441`; rules 2 and 7 pass. Rule 8 is intentionally **FAIL-literal / PASS-intent**: only schematic placeholders occur, but the contract says vault ref paths stay out, including examples. Rule 10 is satisfied by this emitted review, not a claim that the corpus itself is clean.

## Movement vs round-6 ledger

Baseline (`AGGREGATE.md:604`): kake at `dd4eabf`, **not conformant — 4,1**, **5 majors / 11 defects**, lesson `ab8c9e2`. Current: the verdict remains not conformant, but the failed-rule surface is remeasured as 1,3,4,5,6,9; the timer claim is corrected in landed `keeper-timer-inert.md`, and round-12/13/14 evidence is now committed. This is movement in evidence freshness and operability documentation, not a clean conformance result. Historical defects remain relevant: D-24, D-25, D-26, D-27, D-57, D-58, D-67, D-68, D-69 are cited in the ledger as kake-owned/open or routed.

## Report commit citations

Hash sweep over `.ufo/reports/round-13/kake.md` and `round-12/kake.md` found kake commits `0262681` and `a642f93`; `git cat-file -e` resolves both in kake and `git merge-base --is-ancestor 0262681 4c9a985` succeeds. Main report commit `9af7245` resolves in the main repo. Charter commits `b74190e`, `d69dd22`, `0c767c2`, `b9db4b1`, `a8f1e2b`, and `61d0ce6` resolve in the charter child repo, not kake; content hashes `0decd827`, `8c5bb8ca`, `93ddca9a` and cards `efc1830`/accounting token `f3d2ecd` do not resolve as git commits and are treated as artifact identifiers, not child commits. No cited kake commit was worktree-only at final clean HEAD.

## Keeper timer / freshness

Read-only commands: `systemctl --user is-enabled webzites-keeper.timer` → `disabled` (exit 1); `systemctl --user is-active webzites-keeper.timer` → `inactive` (exit 3); `systemctl --user show -p LastTriggerUSec webzites-keeper.timer` → `LastTriggerUSec=` empty; `systemctl --user list-timers --all | awk '/keeper/'` → no row. Journal sweep `journalctl --user -u webzites-keeper.service -u webzites-keeper.timer | awk 'END{print NR}'` → 1 (the no-entries diagnostic line, no firing record). The corpus freshness claim still holds for the timer itself: disabled, inactive, no last trigger, and no journal firing. The stronger “all logs are fresh/stale by exactly N days” claim is snapshot-relative and remains historical evidence from `/tmp/kake-r12`; it is not newly remeasured here.

## Attribution / limits

This is an aggregator-lane review of kake's own corpus; the reviewer is not non-author for kake's corpus artifacts. Mutating commands were not run. Numbers above include their command and observed output; unobserved exact historical dirty-file membership is explicitly not claimed.
