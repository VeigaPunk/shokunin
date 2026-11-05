# souji round 64 — attempt 1: honest stop (no freeze, no claim admitted)

Lane repo: `/home/vgpnk/Projects/shokunin/souji-shokunin`, branch `master`. Lane tip at report time: `5888654e71cde8a00ba333d29335fd515e2171de` (`git ls-remote origin refs/heads/master` matches). Lesson: `corpus/lessons/round-64.md`. Base: `ae2f4ece2c936ecd8c4260632ad7330c84f7882d`.

## Work performed

**Declared claims (2, distinct axes; none frozen; neither admitted).**

- **C1, operability** — in-run content snapshot under `--allow-dirty`, a `GIT_INDEX_FILE` refusal (`RECEIPT-INDEX-ENV-SET`), and toplevel `:(top)`-scoped index reads for `tools/souji-receipt-write.py`. Candidate `46a9388b50c771707603b287a3f6948c88add322578267a0212efcccb619a63b` exists only in the gitignored wave dir (`.ufo/waves/round-64/w1/S64ExecWriter/`). Not landed.
- **C2, calibration (lowest owned axis, score 7)** — three SKILL.md statements against writer bytes, both directions. Not landed; the base do-nothing is red (below).

**Why no freeze.** The protocol's M1/M2 duties (probe every row against both writers before declaration; freeze before any candidate score) were not met:

- The design reviewer (`.ufo/waves/round-64/w1/S64ReviewerDesign.md` H1) reports that base refuses N4 at the instrument stage. The counter's own N4 fixture (`census/round-64/c1-counter.py`) gives `base=accept` (`census/round-64/controls/c1-do-nothing.txt`). The two fixtures disagree, so the 8/3 matrix count is unresolved and is not claimed.
- Seats executed the candidate, counters and mutants before any predicate existed (selftest, regress, five mutation kills, sentinel re-run). Those are diagnostic only (lesson M2).
- The C1 counter's `command=` receipt header was mangled (flags abspath-prefixed). Fixed in `census/round-64/c1-counter.py` (`shlex.quote` of argv as invoked; `import shlex` added); C1 do-nothing regenerated.
- C2 kind-only, positive-synthetic and decoy receipts cite revisions that exist only in a seat scratch clone (`census/round-64/controls/revs.txt`). Disclosed as out-of-lane evidence (lesson M4).

Work items with evidence:

1. **Frontier: S295 and S296 added** (git(1) `GIT_INDEX_FILE`; gitglossary(7) PATHSEC `top`), tier A, `mined`, located quotes with mechanical offset assertions (`census/round-64/sources/quote-check.txt`; captures and `probe-log.txt` alongside). Commit `04bc2769`. Evidence: `corpus/SOURCES.md` rows S295, S296; lesson `## Gate`.
2. **D2 applied:** S294 `used-by` duplicate `corpus/lessons/round-63.md, corpus/lessons/round-63.md` → `corpus/lessons/round-63.md` (logged old→new in the round-64 lesson `## Gate`). Commit `04bc2769`.
3. **D1 applied:** appended correction to `corpus/lessons/round-63.md` (original text not rewritten): S294 quote offsets are raw 109094 / txt 31190, not 109019 / 31053 (asserted by slicing). Commit `04bc2769`.
4. **Frontier mistakes mined** (`corpus/lessons/round-64.md` `## Mistakes`, M1–M7, each with class, evidence, captured-by and fix). The sweep for "closed in round 62" overreach is in the same section (`grep -c` → 1, base-bytes fact, routed).
5. **Controls and instruments landed:** `census/round-64/` (C1 and C2 counters, matrices, C2 population `c2-statements.tsv`, probe ledger `probes/probes.tsv`, controls). Commit `04bc2769` (instruments) and `a722b476` (controls).
6. **C2 do-nothing bound to the committed population** (`--tsv-rev 04bc2769…`) at base: red as required (commit `a722b476`).
7. **Lesson updated** with the reviewer's two named limits (mode-only in-run flip; wrapped child inherits `GIT_DIR`/`GIT_WORK_TREE`) and connector routes (C2 dead-token falsifier; env-redirect named-limit line). Commit `5888654e`.
8. **Round-63 spot-check D3 (planner seat)** recorded again as a named limit; L0 line appended (see Open L0).
9. **Not done, routed:** freeze; candidate landing; `tools/souji-freeze-check.py --chronology` (candidate in `.ufo/waves/round-64/w1/S64ExecFreeze/`, selftest 52/52 and historical sweep 46 preregs diffs=0 per the seat's report, not landed); C1 stub receipts (still carry the mangled header in the wave dir, not regenerated).

Evidence pointers (wave dir is gitignored and not in the pushed tree; see Named limits): `.ufo/waves/round-64/w1/S64*.md` (12 seat reports), `S64MutKill/kills.txt`, `S64ExecWriter/selftest.txt`, `S64ExecFreeze/`.

## Landed changes

| commit | paths | what | LOG.md entry |
|---|---|---|---|
| `04bc2769e14c5c5050a0c8b93a439e13adb8b69b` | `corpus/SOURCES.md`, `corpus/lessons/round-63.md`, `corpus/lessons/round-64.md`, `census/round-64/**` | S295, S296; S294 used-by fix (D2); D1 correction; round-64 lesson; C1/C2 instruments, matrices, population, probe ledger, captures | `## Round 64` |
| `a722b47664e6b03a21a53f9d34fa621feb67499a` | `census/round-64/controls/**`, `census/round-64/SHA256SUMS.txt`, `SCORECARD.md`, `LOG.md`, `corpus/lessons/round-64.md` | C1 do-nothing (fixed header); C2 do-nothing bound to `04bc2769`; SCORECARD round-64 measurements and r65 plan; LOG entry | `## Round 64` |
| `5888654e71cde8a00ba333d29335fd515e2171de` | `corpus/lessons/round-64.md` | reviewer named limits; connector routes | `## Round 64` |

Production bytes (`tools/`, `tests/`, `SKILL.md`, `corpus/knowledge/`, `PROVINCE.md`) are unchanged: `git diff ae2f4ece 5888654e -- tools SKILL.md corpus/knowledge PROVINCE.md` is empty (checked at closure).

## Before → after measurements

Both claims are **not admitted**. There is no after-state for either claim.

| claim | axis | before (do-nothing, base bytes) | after | counting command | measured commit |
|---|---|---|---|---|---|
| C1 in-run snapshot, env refusal, toplevel scope | operability 8 (not moved) | `census/round-64/controls/c1-do-nothing.txt`: `SUMMARY matrix=13 base_forgeries=8 base_honest=3 new_forgeries=8 new_honest=3 class_mismatches=8 regress=PASS`, `EXIT=1` | not measured on a frozen predicate. Seat-run on candidate `46a9388b` (diagnostic, pre-freeze): selftest 26/26, regress PASS | `python3 -B census/round-64/c1-counter.py --root . --matrix census/round-64/c1-matrix.tsv --base-rev ae2f4ece2c936ecd8c4260632ad7330c84f7882d --new-tool <bytes> --work <dir> --receipt <file>` | base `ae2f4ece`; controls `a722b476` |
| C2 SKILL.md agreement | calibration 7 (not moved) | `census/round-64/controls/c2-do-nothing.txt`: `SUMMARY rows=3 findings=1 verdict=FAIL` (`SCOPE-OVERREACH s2`), `EXIT=1`, population `04bc2769` | not measured (after-wording not landed) | `python3 -B census/round-64/c2-counter.py --root . --tsv census/round-64/c2-statements.tsv --tsv-rev 04bc2769e14c5c5050a0c8b93a439e13adb8b69b --rev <full40>` | base `ae2f4ece` |

Scores unchanged (calibration 7, coverage 8, operability 8). No capability row entered. No axis harmed (no production change).

## Sources & frontier

- **Registry before → after** (`scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin souji` exit 0 at `5888654e`):
  - rows: `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` → 217 (`ae2f4ece`) → 219 (`5888654e`);
  - tier histogram (`awk` census command): A=207 → 209, B=7 → 7, C=3 → 3;
  - status (`awk` census command): mined=179 → 181, queued=14 → 14, rejected=24 → 24;
  - malformed rows (NF≠13): 0 → 0; duplicate ids: none.
- **Rows added by tier:** A ×2 (S295, S296).
- **Rows touched old→new:** S294 `used-by`: `corpus/lessons/round-63.md, corpus/lessons/round-63.md` → `corpus/lessons/round-63.md`. No status, recheck or tier change.
- **Frontier rows advanced:** S295 and S296 (writer environment and pathspec scope). C1's evidence trail rests on both (sourced-claim duty).
- **Mined mistake:** M1–M7 in `corpus/lessons/round-64.md` `## Mistakes`.
- **Assimilation: none.** `considerthese/` absent (`ls` exit 2). `/home/vgpnk/Projects/shokuknow/merge/souji/MERGE-REPORT.md` read read-only by the connector seat; no theme matches the receipt-writer, index-flag or concealment surface.
- **Non-author spot-check:** pending for S295, S296 and the lesson's gate.

## Trend verdicts

- **expansion: unchanged.** Two sourced rows (S295, S296) were added, but no `knowledge/` entry was admitted on uncovered ground, and no capability entered. Evidence: `corpus/knowledge/` unchanged; SCORECARD capability rows "none entered".
- **quality: unchanged.** No admitted entry changed. A wrong offset record in round 63 (S294) was corrected by an appended section (D1), which is a quality-positive correction, but no quality criterion moved and no score changed. Evidence: `git diff ae2f4ece 5888654e -- corpus/knowledge QUALITY.md` empty; `corpus/lessons/round-63.md` appended section.
- **discernment: unchanged.** The round's own gate recorded two overclaims that the scout or design reviewer caught before commit (S296 `teaches` cell; the N4 "7 vs 8" count, now M1). Both were learned and mined, and no disagreement was left unlearned. The outside spot-check is still pending. Evidence: lesson `## Mistakes` M1, M6.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — SKILL.md Decision tables/Error patterns/Checklists/Gate registry; corpus/SOURCES.md S100-S103; corpus/lessons/round-21.md Gate (unchanged this round)
- [~] At least one end-to-end domain task executed and logged in LOG.md — LOG.md:362 (2026-10-19 operator sweep: 96 pushed-receipt artifacts quarantined, second-checked, removed)
- [~] Instructions executable by an agent without oral context — census/round-21/run-acceptance.py; census/round-21/accepted-matrix.json (unchanged this round)
- [~] No cross-domain bleed (PROVINCE.md still accurate) — PROVINCE.md Round21 privacy boundary; .ufo/waves/round-21/w1/ConnSiblingOverlap.md; corpus/lessons/round-21.md Boundaries

No box is checked: no non-author verifier has checked any box.

## Round shape, seats, dead seats

- **Shape:** one v1 wave, 12 seats, validated under `ufo-wave-policy.json` (band 8–16); `reportDir` `.ufo/waves/round-64/w1`; spec `w1-spec.json`, dispatch `w1-dispatch.json`, registry `w1/swarm-registry.json`, ready `w1.ready` (dispatched 2026-11-05 08:06:31).
- **Role mix:** scout 1 (`S64ScoutSources`), executor 4 (`S64ExecWriter`, `S64ExecCounterC1`, `S64ExecCounterC2`, `S64ExecFreeze`), mutation-tester 1, reviewer 2, critic 1, sentinel 1, scribe 1, connector 1. Attack seats (reviewer, critic, mutation-tester) = 4/12 = 33%, above the 25% floor; the sentinel and connector are not in that count.
- **Planner:** held by the L1 (the validator refuses a planner role; recorded in the lesson and routed as an L0 line).
- **Residual call:** none. **Round total:** 12 seats.
- **Dead seats:** none. All 12 seats delivered a report file in the wave dir; the connector and the reviewer each published a final message after a re-nudge.
- **Results-file caveat:** `w1-results.json` records `output: null` for every seat with the note "orchestrator kernel restarted mid-wave; seat output was delivered to the orchestrator session but not retained". Seat outputs were read from the wave-dir reports instead.
- **Answering model:** scout reported `minimax-code/MiniMax-M3.1-Flash`; other seats did not report one. Not relied on for any claim.

## Named limits and carried debt

- **Untracked visibility (MEDIUM, sentinel S64-F1).** `status.showUntrackedFiles=no` hides untracked files from the writer, and the writer accepts. The base has the same hole. Not applied (outside the frozen deltas; would newly refuse honest runs). Routed round 65 with its own predicate.
- **Mode-only in-run flip** (reviewer named limit): `chmod +x` on a dirty tracked file under `--allow-dirty` is accepted.
- **Child environment** (reviewer M2): the wrapped command inherits `GIT_DIR`/`GIT_WORK_TREE`.
- **Env redirects** (connector): `GIT_OBJECT_DIRECTORY`, `GIT_ALTERNATE_OBJECT_DIRECTORIES`, refs-replace are unread. Routed.
- **C2 dead-token blind spot** (connector, tabi round-62 polarity class): needle presence only. Routed.
- **`GIT_INDEX_FILE` edge cases** (probes P13/P14): nonexistent path → vacuous pass; empty file → exit 128; relative path not probed.
- **`:(top)` binding is code, not page** (S296 named limit).
- **Durability:** the wave dir `.ufo/waves/round-64/` is gitignored and not in the pushed tree. The candidate writer, selftest, mutation kills and reviewer attacks exist only on this host. Durable instruments and evidence are in `census/round-64/` and the lesson. Routed: any future evidence the lesson cites must be committed.
- **Pre-freeze diagnostic runs** are not admission evidence.

## Open L0 questions

- Appended to `.ufo/l0-questions.md`: planner seat (validator refuses the planner role; L1 holds it; third round running, round-63 D3).
- Still open from earlier rounds, routed around (not answered): MACHINE BLOCK for preregistrations; numeric axis mapping for calibration/operability; edge-class axis tie-break.

## Stale-lane

Stale-lane: respawn-per-round driver; no other mission of this lane is open.

## Tools

None installed or updated. No pacman transaction. No host sysctl touched. Seats were given the tooling directive and did not install anything I can see in their reports.

## Misroot sweep

`git -C /home/vgpnk/Projects/shokunin status --porcelain` at the fleet root shows one modified file, `.scratch/run15-state.json`. That is orchestrator-owned run state, not written by any souji seat, and was left untouched. No untracked fleet-root file from this round was found, so no copy-and-delete was needed.

## Pre-report gate

- `git -C souji-shokunin ls-remote origin refs/heads/master` → `5888654e71cde8a00ba333d29335fd515e2171de` (matches the lane tip).
- `jj-lane.sh state` → `local=5888654e… remote=5888654e… ahead=0 behind=0 tracked=0 untracked=0`.
- Round-end census: exit 0.
