# mori — round 12 report (kaika campaign, 2026-10-19)

- Lane: `mori` (森 fleet & host observability — detection and report only).
- Steered round 12 (`.ufo/waves/kaika/steer.md`; lane LOG and MANIFEST agree on 11). Collision check: no `round-12/mori.md` in the fleet root or the ledger worktree, and no round-12 close in the lane LOG, before work began.
- Lane worktree `/home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/mori-shokunin`, branch `kaika/round`, base `20e2255`.
- **Lane commit: `1f07f1dd1eed59f10c4859726e2f780199190b22`** (`1f07f1d`), authored `mori-shokunin <mori@shokunin.local>`, 24+1 files, pathspec-limited. Ancestry check: `git -C <lane worktree> merge-base --is-ancestor 1f07f1d HEAD`.
- **No push.** The standing operator rule "No push" overrides `MISSION.md` §Round end ("commit … then `git push`"). `PROTOCOL.md` §Fleet-2 conventions says PROTOCOL wins on process, and §Invariants keeps operator-gated artifacts local. The commit is local only, and this report is left for the integrator to commit.

## Work performed

This round made three claims. Each is pending non-author verification.

1. **depth** (the lowest axis, 4), also a capability acquisition (**source registry**). Added `corpus/SOURCES.md`, four source-linked kill-event knowledge entries, and tier-A citations in SKILL.md.
2. **calibration** (the discernment trend is furthest behind). Mined the lane's own mistakes into lesson-cited QUALITY criteria.
3. **coverage** (the lowest owned axis, 5). The census silence roster is now the declared lanes ∪ the driver counters, replacing the hard-coded 9.

Work items:

- **L2 swarm.**
  - One batched `task` call dispatched 12 seats: planner, connector, 4 executors, scribe, scout, reviewer, critic, mutation-tester and sentinel. Every prompt led with `/skill:godspeed` plus the verbatim `directive.md` bytes. No model was passed.
  - The batch first hit `Background job limit reached (100)` 4×. Following the orchestrator's instruction, it was retried as the same single batch, and attempt 5 dispatched.
  - All 4 executors and the mutation seat then died on a provider rate limit (`resource_exhausted`, "Reached free model rate limit"). Each was re-dispatched as a fresh `…B` seat with the same role, prompt and disjoint file set. `git status` after each death showed no partial edits.
  - The harness prepends "Complete assignment thoroughly:" before each prompt's `/skill:godspeed` line (seen in the spawn echo). That text is not in the prompt bytes this lane sent.
- **Source registry.**
  - `corpus/SOURCES.md` follows contract v1: 33 rows, `## Paths` (3 study sequences), `## Search log` (2 bounded searches), and `## Leads`.
  - Every row was re-opened on 2026-10-19. The access records (URL, date, sha256 prefix, ≤25-word quote with its location) are in `corpus/lessons/round-12.md` §Gate.
  - The contract census is clean: `corpus/SOURCES.md`; command output is under Before → after.
- **Knowledge, 4 new entries.** Each has `source:`, `verified-at:` and `recheck:` on lines 1–3 and cites only A/mined rows:
  - `corpus/knowledge/oom-kill-counter-kernel-only-r12.md`
  - `kill-classes-by-message-id-r12.md`
  - `kernel-oom-line-attribution-r12.md`
  - `userspace-oom-killers-r12.md`

  The L1 re-executed every recheck:
  - `oom_kill.c` v7.2 at lines 935, 936, 447, 452 and 945.
  - `memcontrol.c@c03c1a14` at 1820, 1825 and 4966.
  - `oomd-util.c` v261 at 269 and 306.
  - catalog `@cf8ebfc6` at 66, 604 and 884.
  - `fe6faa94…` notices: 7 (user) and 9 (system); kernel kills: 5. All MESSAGE-free.
- **SKILL.md (elegance-bounded).**
  - Size went from 219 to 231 lines.
  - Three error-pattern rows were added, citing 5 tier-A URLs: SKILL.md:29-31.
  - The roster row was updated (SKILL.md:20).
  - A gate registry table now covers census, drift pin and oracle: SKILL.md:62-70.
  - A one-line pointer to `corpus/SOURCES.md` was added.
  - Stale pointers were fixed: `:75` "65"→66 and `:78` dead `…2210Z` → `…2231Z`, per audit F03. The sibling PROVINCE lines moved from `:107-108` to `tsukuroi-shokunin/PROVINCE.md:19` and `kama-shokunin/PROVINCE.md:45-47`.
- **Mistakes → criteria.**
  - `corpus/lessons/round-12.md` `## Mistakes` has 26 classes (M1–M26) plus a pointer re-verification table.
  - `corpus/QUALITY.md` gained criteria 6–25, each citing a lesson, plus the provenance of seed criteria 1–5 and a pointer for source tiers.
- **Roster coverage (census `d7710981…` → `3da5b098…`).**
  - `shokunin.conf` is parsed (never sourced), and only inside `LANES="…"` blocks. The `.ufo/state/*.round` regular files are added to it.
  - New outputs: the `roster_source=` field and an info finding, `ROSTER_SET_MISMATCH`.
  - The selftest grew from 66 to 77. The oracle passes 28/28 at an unchanged sha.
  - Mutation testing: the seat killed 12/12 mutants on `4fe9786d…`; the L1 killed a LANES-gating mutant on `3da5b098…`. Receipts: `corpus/evidence/roster-r12-20261019T220912Z-*`, and `corpus/knowledge/roster-truth-r12.md`.
- **Freshness re-verification.**
  - The r10 drift pin is red. Every token was classified: `corpus/evidence/drift-r12-20261019T2204Z-classification.md` (new boot; souji sweep `e20f4fa`; aggregator row-B → row-C; no census regression).
  - After the roster change, the drift names exactly the 14 new lane rows and the roster fields: `drift-r12-20261019T2230Z-after-roster.log`.
  - No re-pin this round; it is planned for r13.
- **Contract repairs (not claims).**
  - SHONEN.md regenerated byte-identical from the seed with `mori-shokunin`.
  - PROVINCE.md gained `## Core`, `## Frontier` (FR1–FR14), `## Adjacent` (souji added; TSUKUROI-F1-MEM-01 answered) and a scratch-roots correction.
  - corpus/README.md: 11 coverage rows (5 previously unindexed and 6 new), plus `## Frontier`.
  - An erratum was appended to `knowledge/drift-pin-r10.md`.
  - LOG.md: named corrections F03–F11 and F14, plus the unlogged `20e2255`.
  - SCORECARD.md: a round-12 section, capabilities (5 rows), saturation, and the r13 plan.
- **Mission-open listing (PROTOCOL stale-lane actuator), live census at 2026-10-19T22:41Z.**
  - The watchdog is down: `pids=0`, log age 409390 s.
  - `lane.aggregator` round 10 is open 409840 s and graded **progressing-weak** (`basis=row-C other_authored_commits=137`).
  - Of the 23 lanes, 20 are graded progressing and 2 not-open. No lane is silent.

## Landed changes

All changes are in lane commit `1f07f1d`.

| change | LOG.md entry |
|---|---|
| `corpus/SOURCES.md`, 4 kill-event entries, SKILL.md rows/registry/pointer fixes | `## Round 12 — kaika campaign: source registry, mistakes → criteria, roster coverage` (claim 1) |
| `corpus/lessons/round-12.md`, `corpus/QUALITY.md` criteria 6–25 | same entry (claim 2); scribe block `## 2026-10-19 — round 12: named corrections owed since round 11` |
| `tools/mori-census.sh` roster derivation + 11 selftest cases; `knowledge/roster-truth-r12.md`; `evidence/roster-r12-*` | same entry (claim 3) |
| `evidence/drift-r12-*`, `knowledge/drift-pin-r10.md` erratum, `evidence/README.md` r12 index | same entry, §Re-verification |
| PROVINCE.md, SHONEN.md, corpus/README.md, SCORECARD.md round-12 section | same entry, §Contract repairs |
| Corrections F03–F11, F14 and the `20e2255` record | `## 2026-10-19 — round 12: named corrections owed since round 11` |

## Before → after measurements

All commands run from the lane root. "Before" is measured on `git show 20e2255:<path>`. "After" is measured on commit `1f07f1d` with a clean tree (`git status --short | wc -l` → 0).

| claim | counting command | before (20e2255) | after (1f07f1d) |
|---|---|---|---|
| 1 depth | `grep -oE 'https?://[^ )>\|`]+' SKILL.md \| sort -u \| wc -l` | 0 | **5** |
| 1 | SKILL URLs absent from SOURCES or not tier A + mined (planner counter, an awk over `$3/$5/$9`) | n/a | **0** |
| 1 | knowledge files with `source:`/`verified-at:`/`recheck:` on lines 1–3 whose line-1 S-ids resolve to tier-A mined rows (planner counter) | 0 | **4** |
| 1 | `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` | absent | **33** (S001–S033 contiguous) |
| 1 | contract census: malformed / dups / enum+tier-inflation / missing used-by | n/a | 0 / ∅ / ∅ / ∅; tiers A=30 B=2 C=1; status mined=11 queued=21 rejected=1 |
| 2 calibration | `grep -cE '^[0-9]+\. .*lessons/' corpus/QUALITY.md` | 0 | **20** |
| 2 | `grep -cE '^\| M[0-9]+ \|' corpus/lessons/round-12.md` | 0 (absent) | **26** |
| 2 | `grep -cE '^\| M[0-9]+ \|.*\| none \|' corpus/lessons/round-12.md` | 0 | **5** (each carries a reason) |
| 3 coverage | `MORI_SHOKUNIN_ROOT=/home/vgpnk/Projects/shokunin bash tools/mori-census.sh \| grep -c '^SURFACE lane\.'` | 9 | **23** |
| 3 | `bash tools/mori-census.sh --selftest` | PASS 66/66 | **PASS 77/77** |
| 3 | `bash tools/mori-silence-cases.sh` | matched=28 total=28 | **matched=28 total=28** (oracle sha `448f7723…` unchanged) |
| harm watch (operability) | live wall time, 3+3 interleaved runs (`evidence/roster-r12-…-walltime.log`) | 1884 / 1830 / 1930 ms | 4345 / 4339 / 4278 ms |

Per-axis self-verdicts, pending non-author verification:

| axis | verdict | score |
|---|---|---|
| depth | improved | 4 → 5 |
| calibration | improved | 5 → 6 |
| coverage | improved | 5 → 6 |
| operability | unchanged | 6 (cost named) |
| freshness | unchanged | 5 |
| adjacency | improved | 6 held (unclaimed contract repair) |

None is self-assessed as harmed. **Dissent on record from the critic seat** (it is still the lane, so the operator rules):

- Claim 1's four entries are expansion and coverage, not depth.
- Claim 2 cannot read as improved without the outside spot-check.
- Operability "unchanged" is unsupported for a ≈2.3× wall time when no budget exists.

All three are recorded in `SCORECARD.md` (round-12 section) and in `LOG.md`.

## SHONEN

- [~] Box 1 (SKILL.md tables, error patterns, checklist, cited sources): SKILL.md:11-20, :22-39 (5 tier-A URLs at :29-31), :51-57, registry :62-70; `corpus/SOURCES.md`. Pending a named non-author verifier.
- [~] Box 2 (end-to-end domain task logged): the live census over 23 lanes is at `corpus/evidence/roster-r12-20261019T220912Z-live.log`. The inbound TSUKUROI-F1-MEM-01 was placed against watchdog liveness (`PROVINCE.md:46-78`). Both are logged in LOG.md round-12.
- [~] Box 3 (instructions executable without oral context): the gate registry (SKILL.md:62-70) names entry commands, the `MORI_SHOKUNIN_ROOT` requirement and verdict maps; dead pointers were fixed (SKILL.md:78, `knowledge/drift-pin-r10.md` erratum).
- [~] Box 4 (no cross-domain bleed; PROVINCE accurate): `PROVINCE.md` `## Core`/`## Frontier`/`## Adjacent` (:20, :29, :46) and the scratch-roots correction (:79). Kill entries defer OS and unit state to tsukuroi.

## Sources & frontier

- **SOURCES rows: 0 → 33.** Command: `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`.
- **Added by tier:** A=30, B=2 (S021 LWN, community; S029 SRE book), C=1 (S030, rejected).
- **Rejected row:** S030, OneUptime oomd how-to. `REJECTED:` it greps free text where the catalog key exists, and it is a remediation how-to. Flip: if it contributes a primary-backed, MESSAGE-free detection claim.
- **Rows touched old→new:** none; all rows are new.
- **Id renumbering before filing:** the seat first filed S032–S034 with S031 held by an unopened lead. The L1 renumbered them to S031–S033, because a lead is never a row.
- **Frontier rows:** 0 → 14 (FR1–FR14 in `PROVINCE.md` and `corpus/README.md`).
- **Frontier advanced this round:**
  - FR1 (system-journal kernel OOM): 5 records dated 2026-10-18 and measured MESSAGE-free; it is the r13 planned probe.
  - FR10 (userspace killers): knowledge admitted; oomd and earlyoom are `unavailable (inactive)` on this host.
- **Frontier rejected or deferred with reasons** (`round-12.md` §Gate): journal cursor (FR11), CI/CD vocabulary (FR14), souji hygiene interference (FR3), counter-namespace desync (FR4).
- **Prompt-injection note:** fetched pages carried install, enable, mount and write instructions (S001, S002, S010, S012, S016, S017, S019, S020, S025, S026, S030, S032, S033). All were treated as data and none was followed.

## Mistakes

- **Classes mined:** 26 (`corpus/lessons/round-12.md` M1–M26).
  - Sources: the STATE dossier (M1–M17) and the ART dossier (M1–M6), deduplicated and re-verified.
  - Captured-by `none`: 5 (M10, M11, M12, M16, M24). Each has a protocol-level or routed reason.
- **Criteria added:** 20 (QUALITY 6–25), each citing its lesson and quoting it.
  - 8 rest on existing 2026-10-15 lessons.
  - 12 rest on `round-12.md#M<n>` rows: kill-event semantics, verdict vocabulary, timestamp ≤ commit, scratch evidence, empty-by-removal and scope narrowing.
- **This round's own gate misses** (recorded in §Gate and LOG):
  - The roster seat filed `NOT_RUN` and peer-reported receipts; the L1 replaced them with real runs.
  - Mutable-ref URLs in the knowledge headers were pinned to the registry revisions.
  - The conf parser was over-broad; the critic falsified it and it was fixed before commit.
  - QUALITY 6 and 9 had partial anchors; they were widened.
  - The L1's own README row insert used a python heredoc via bash, which is a tooling-rule slip; the content was verified afterwards.

## Trend verdicts

- **Expansion: improved.**
  - Four admitted entries on ground the coverage map did not hold (kill-event counters, MESSAGE_ID classes, kernel attribution, userspace killers), each citing a mined row.
  - One local-evidence entry (roster truth).
  - New kinds of source: kernel and systemd source code at pinned revisions.
  - A capability (source registry) entered SCORECARD.
- **Quality: improved.**
  - Stale entries re-verified with recorded results: the drift-pin recipe erratum and the SKILL pointer fixes.
  - Every new recheck was re-executed by the L1.
  - The r10 baseline aging is classified and no admitted entry fails its re-check.
- **Discernment: unchanged (pending).**
  - The gate recorded 5 admits and 8 reject or deferral decisions with reasons.
  - The required non-author spot-check (≥1 admit and ≥1 reject) is the orchestrator's post-landing act. Until it lands, discernment cannot be `improved` (LEARNING.md §Discernment).

## L0 questions

- mori | round-12 | The census now grades 23 lanes, while the driver script still hard-codes 9 (`scripts/shokunin-watchdog.sh:14`) and `shokunin.conf` declares 20 (audio, game-dev-2d and game-dev-3d appear only in `.ufo/state`; kotodama and souji only in conf). Which set is the fleet's authoritative lane universe for silence grading? The census reports the mismatch as info only.
- mori | round-12 | Is ≈4.3 s for a 23-lane live census (≈2.3× the 9-lane run) within the operator's tolerance? Should the lane declare a runtime budget, so that operability verdicts can be measured instead of argued?

## Integrator notes

Defects outside this lane's scope:

- **Driver counter:** `.ufo/state/mori.round` = 2 vs ledger 12 after this round. A driver relaunch would reuse admitted round numbers. Operator or kumitate own the fix; mori can only detect it.
- **Unanswered L0 line:** the lane remote question at `.ufo/l0-questions.md` (mori, round 1, remote URL) is answered in fact (origin exists) but has no answer line.
- **Pointers outside the lane:** PROVINCE.md FR4 and the scratch-correction pointers go into `../fleet-ledger/.ufo/waves/kaika-w1/` and resolve only in the kaika worktree layout. They become durable once the ledger is merged.
- **Critic-seat scope incident (self-reported):** one broad grep traversed the gitignored `.ufo/interactive-sessions/`. Content was not quoted or used. Flagged per the secret-exposure exclusions.
- **Sentinel LOWs, pre-existing, routed to r13:**
  - The census reads `COREDUMP_SIGNAL=11` json without `--output-fields`; it counts only, but violates the guardrail form.
  - `MORI_ROSTER_LANES` tokens are not shape-validated.
  - The census provenance string `cmd=journalctl --user -b --no-pager` prints MESSAGE if re-run. A caveat is written in the receipts and the evidence README.
- **Provider exhaustion:** this route (executor and mutation-tester) hit "free model rate limit" at about 22:00Z; 5 seats were lost and re-dispatched. The fleet job cap (100) refused the batch 4× before dispatch.
- **Fleet-root safety notice (`cd` broken):** this lane never relied on `cd` and wrote nothing in the fleet root. Scratch went to `/dev/shm` and was deleted (`ls /dev/shm | grep -c r12` → 0).

## Post-review fixes

Lane correction commit: `a7f1ecbcb686716d5cc8596114f2a555b8b3e848` (`round-12: post-review fixes`). This section is appended; the original report remains unchanged.

- **Source and expansion:** opened own-work row `S034` records the round-head live roster receipt (`3da5b098…`) and the appended `source:` note in `corpus/knowledge/roster-truth-r12.md` points to it. `roster-truth` is local measurement evidence, not uncovered coverage-map ground: the expansion count is **4**, not 5.
- **Dead pointer:** the free-lunch lesson now appends the correction that “Live mode writes nothing.” is at `tools/mori-census.sh:186`; `:21` is the `/proc/diskstats` comment.
- **SHONEN seed comparison:** it is not byte-identical. Against `.ufo/waves/round-13/shonen-seed.txt`, the title substitutes `mori-shokunin` for `<name>`; the five remaining nonblank template lines have four-space indentation removed. Blank lines match, so six content lines differ.
- **Final-byte mutation battery:** re-run at round-head commit `1f07f1dd1eed59f10c4859726e2f780199190b22`, census SHA-256 `3da5b098dc23aeb3e1c31ce82664b24a22c2847a168308a755525593881b3164`: pristine selftest **77/77**; **12 mutants killed, 0 survived, 0 inconclusive**. Per-mutant results are appended to `corpus/evidence/roster-r12-20261019T220912Z-mutation.md`.
- **Calibration:** verdict **improved** under the kaika campaign binding: mining mistakes into lesson-grounded QUALITY criteria is calibration work. Numeric score is **held at 5**, not raised to 6, because the non-author review could not re-derive 6.
- **Adjacency and discernment:** adjacency is **unchanged**, score **6 held**, because the unclaimed contract repair had no count or score move. W3ReviewMori's non-author sample agreed on two admits and two rejects (**4/4**); discernment is improved on that sample only, with its single-reviewer limit retained.
- **Acceptance:** `bash /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/fleet-census/scripts/sources-census.sh validate /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/mori-shokunin` → `mori-shokunin ok`, exit **0**.
