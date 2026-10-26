# tsukuroi — round 42 report (hyaku run 9, attempt 1)

L1: `TsukuroiR42`. Lane repo `tsukuroi-shokunin`, branch `master`. Base `c8efaa3f120834541f8de1e5e0367e8d1593bae6`
(the tip at round start per `jj-lane.sh state`). Final lane hash `12421a73b2816d7f9ed91ea25f230d9389452341`: pushed,
and `git ls-remote origin refs/heads/master` prints that hash. Evidence root: `tsukuroi-shokunin/.ufo/waves/round-42/`
(called `W/` below). Stale-lane: respawn-per-round driver; no other mission of this lane is open. No earlier attempt
of this round (`.ufo/watchdog.log` has no `lane-dead-no-report tsukuroi round=42`), so nothing was inherited.

## Work performed

The round declared two claims (`SCORECARD.md` "Round 42 — declaration", frozen at `a84fc9de` before any seat ran):
- **C1, operability.** The census's early-reader pipelines under `set -o pipefail`, on the packages and update-safety
  planes. Routed defect R41-CENSUS-PIPEFAIL-692.
- **C2, depth (sourced on S237-S239).** The btrfs scrub status record, rows SC1-SC5, a storage-integrity Frontier line.
  The lowest axes are depth and adjacency, tied at 8. C2 takes depth. Adjacency is not claimed.

Work items:
- **Freeze, controls, before receipts.** I wrote both counters and their batteries myself before any seat:
  - `tools/score-size-invariance-r42.py` (sha256 `c511104a…`) is a metamorphic oracle with no answer key. Ten small/large fixture twins, plus three `unshare -rm` production-path legs.
  - `tools/check-scrub-record-r42.py` (sha256 `dbe933ec…`) binds verdicts through `w2-dispatch.json`, `w2-results.json` and the committed report, which answers routed defect R41-GUARD-BYPASS.
  - Batteries: `W/controls/` (C1 K0-K8, C2 K0-K5). Both summaries read `should_fail_accepted 0` and `control_accepted 1` (`battery-summary-c1.jsonl`, `-c2.jsonl`).
  - Before receipts: `W/before/c1-before.jsonl` (invariant 3, FAIL) and `c2-before.jsonl` (rows 0, FAIL). Both finished at 19:29:59Z and 19:30:01Z, before the implementation commit at 19:32:12Z. This answers routed item N3.
- **C1 implementation.** First fix at `44766208` (here-strings, `awk NR`). Able-to-fail receipt: `W/impl/c1-able-to-fail.txt`.
- **C1 hardening from wave 1, at `78abb8b5`:**
  - The here-strings were replaced by an awk full-consumer test. Reason: a large here-string is a temporary file, and on a full TMPDIR the error sample read HEALTHY (`W/w1/C1RevFix.md` D1). Shown gone in `W/w2/C1FinalENOSPC.md`.
  - The `:743` baseline lookup was changed to a full read.
  - Two `-Sup` selftest cases were added (`W/w1/C1MutSelftest.md`). The selftest went from 128 to 132 cases.
- **C2 entry.** `corpus/knowledge/btrfs-scrub-record-r42.md`, drafted at `f50c28d8`. I revised it before wave 2 using the wave-1 first reads (all five rows read `holds`) and `W/w1/C2CritNovelty.md`. After the counted wave-2 reads I appended a "Corrections — round-42 wave 2" section.
- **Routed defects of round 41, all five dispositioned** in `corpus/lessons/round-42.md` "Round-41 routed defects":
  - PA6 now reads `holds` as corrected (`W/w1/PA6Verdict.md`).
  - The base is named from the `jj-lane.sh state` local value.
- **Frontier step.** Rows S237, S238 and S239 were opened this round. The lesson's `## Mistakes` section has 12 rows. The new QUALITY criteria are 90 (observed-channel controls; anchored verdict binding) and 91 (adopted text is verified before a counted read).
- **considerthese.** I took the `2026-10-26.md` proposal "Downstream patch-offset check":
  - Grounded by `W/w1/ConsiderPatchOffset/patch-offset.py`, which checked 108 pins and found 15 that drift.
  - Landed as appended notes in the r38, r39 and r41 pacman entries and in a SKILL note.
- **Routed out of round scope:**
  - `tools/boot-chain-audit.sh:480-487`: `find -quit | grep -q` under pipefail fails open (`W/w1/C1SweepSites.md`).
  - Single-line probe readers.

## Landed changes

Every commit below was landed by `jj-lane.sh` as `tsukuroi-shokunin`. The LOG.md entry "Round 42 — hyaku run 9" lists them.

| Commit | What it carries |
|---|---|
| `a84fc9de` | Declaration, both counters, pinned btrfs-progs v7.1 snapshots and host capture, S237-S239 (queued), control runners |
| `44766208` | C1 first fix and two selftest cases; able-to-fail receipt; before receipts |
| `f50c28d8` | C2 entry draft; S237-S239 changed from queued to mined |
| `87c4f7c6` | Control batteries scored with the frozen counters; w1 spec and dispatch |
| `78abb8b5` | w1 integration (43 seats): awk test, `:743`, `-Sup` cases, entry revision, SKILL sections, registry rows, QUALITY 90, PROVINCE/README notes, r39/r41 packaging notes, IN-109 anchor |
| `a968393c` | C1 after receipt at `78abb8b5`; w2 spec and dispatch (34 seats) |
| `342d1049` | w2 reports and orchestrator results |
| `e2407a9d` | Measured outcome, entry wave-2 corrections, r38 note, SKILL notes, lesson, QUALITY 91, LOG entry, axes table, after receipts |
| `12421a73` | Self-assessment receipt (27 checked, 0 mismatches) |

## Before → after measurements

**C1** — `python3 tools/score-size-invariance-r42.py --revision <REV> --scratch <DIR>`, frozen at `a84fc9de`.

| | Base `c8efaa3f` | After `44766208` | After `78abb8b5` |
|---|---|---|---|
| invariant | 3 (P2, P4, P5) | 10 | 10 |
| ns_invariant | 0 | 3 | 3 |
| selftest_pass | 1 | 1 | 1 (132 cases) |
| default_equal | 1 | 1 | 1 |
| Verdict | FAIL | PASS | PASS |
| Receipt | `before/c1-before.jsonl` | `W/w1/C1ExecRerun/c1-after-4476620.jsonl` | `W/after/c1-after-78abb8b.jsonl`; re-run by `W/w2/C1FinalRerun.md` |

Census bytes have not changed since `78abb8b5`. Kill rules, none fired:
- every hunk lies in the three allowed functions (`W/w2/C1RevIntegration.md`);
- the round-41 C1 counter still PASSes at `78abb8b5` (`W/after/r41-c1-counter-78abb8b.jsonl`).

**Author verdict: verified under the frozen predicate, and the counter's sufficiency is falsified.** These variants also PASS the counter:
- a census fixed only under `TSUKUROI_FIXTURE` or uid 0;
- a census fixed only for the fixed fixture package names;
- a census behind a padding-grammar filter.

Evidence: `W/w1/C1CritNsView.md`, `C1CritEvasion.md`, `ConnClaims.md`, rebuilt on the tip in `W/w2/C1CritFinalEvasion.md`. A production-identity leg outside the predicate (uid 1000 via `setpriv`) shows the tip really fixed and the gated arm not fixed (`W/w2/C1FinalProdIdentity.md`). Ordinal stays 9 → 9.

**C2** — `python3 tools/check-scrub-record-r42.py --revision <REV>`, frozen at `a84fc9de`.
- Before, at `c8efaa3f`: `rows 0`, FAIL.
- After, at `342d1049`: `rows 5, quotes_ok 5, novelty_ok 5, host_ok 5, sources_ok 1, verdicts_ok 1, novelty_base_hits 0`, FAIL. `transcripts_bound` is 8 of 8. Receipt: `W/after/c2-after-342d104.jsonl`.

Bound verdicts per row:

| Row | Reviewer | Critic |
|---|---|---|
| SC1 | unbound (its final output carried no verdict line) | fails |
| SC2 | holds | holds |
| SC3 | fails | fails |
| SC4 | unbound | partly |
| SC5 | holds | partly |

**The declared kill rule fired: C2 is not verified.** This is an honest stop, and the depth ordinal stays 8 → 8. Two of the false sentences in SC3 were wave-1 notes I adopted without checking them against the source (Mistake R42-ADOPTED-UNREAD, QUALITY 91).

## Sources & frontier

SOURCES before → after: 236 → 239 rows. Census command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tsukuroi`.
- Start: exit 0, `tsukuroi ok`, 40 W04, on a base export (`W/before/sources-census-start.txt`).
- End: exit 0, `tsukuroi ok`, 40 W04 (`W/after/sources-census-final.txt`).
- Malformed rows: 0 (manual census awk).

Registry changes:
- Rows added: tier A — S237 (code, btrfs-progs v7.1 `cmds/scrub.c`), S238 (docs, v7.1 `CHANGES`), S239 (own-work host capture). No B or C rows.
- Rows touched, old → new: S237-S239 `status` changed from queued to mined, and `used-by` from `—` to the entry. Each change is logged in the lesson Gate.
- The sourced claim is C2 (S237, S238). It did not verify.

Frontier rows advanced: none. The scrub-record line stays Frontier. It is deepened from source and its promotion condition is unchanged (`PROVINCE.md` and `corpus/README.md` round-42 notes).

Assimilation: none. The `merge/tsukuroi/` btrfs entries were evaluated but nothing was adopted (`W/w1/AsmGate.md`):
- Admit candidate: P1, the ioctl-number table. Not adopted because of the QUALITY 14 blocker.
- Reject: P2, the claim that the ioctl surface is closed. Its own `scrub.c` uses the scrub ioctls, so the claim is false.

Census exit 0 is met at round end.

## Trend verdicts

- **expansion: unchanged.** The entry deepens a Frontier line held since round 26 and adds no uncovered coverage-map ground. Its claim did not verify, and no capability row was added (`W/w2/CritTrendFinal.md`).
- **quality: unprovable-but-better (author view; the closure rules).**
  - For it: stale line pins in the r38, r39 and r41 entries are now marked with the Arch packaging offsets. Two census verdict defects (R41-692 and the `-Sup`/`:743` arms) are fixed with red-before evidence. The false C2 sentences are withdrawn in place, not left standing.
  - Against it: no prior entry is superseded by a re-verified stronger one, and `W/w2/CritTrendFinal.md` argued `harmed` at `78abb8b5`. That argument rested on the unmarked r38 pin, which is now marked at `e2407a9d`.
  - If the closure finds any drifted pin still unmarked, the verdict is `harmed`.
- **discernment: improved (pending the outside spot-check).** Both counters' new bypasses and the adopted-unread failure became lessons, and each lesson backs a grounded QUALITY criterion (90 and 91). The counted reads also caught a sentence the author got wrong.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — round 42 adds the pipefail
  signature table and the scrub-record observation → reading → action table (`SKILL.md` "Census early readers under
  pipefail — round 42", "Scrub status record — round 42", read through "Round-42 notes"); no non-author verification yet.
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md` "Round 42 — hyaku run 9" (census
  defect found, fixed, shown red-before and re-measured); non-author replay pending.
- [~] Instructions executable by an agent without oral context — the round-42 sections carry paste-ready read-only
  commands (`btrfs scrub status /` replayed unprivileged by `W/w1/C2ExecHostRecheck.md`); whole-SKILL retest unexecuted.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `W/w1/ConnSiblings.md` found no contested scope. The census
  edit moved mori's `PROVINCE.md:287` line pin; this is reported here and not absorbed (`W/w2/AdjMoriPin.md` has the
  corrected coordinates).

## Round shape, seats, routing, incidents

- **Shape:** two v1 waves under policy `ufo-wave-policy.json`.
  - w1: 43 seats — 10 executor, 11 reviewer, 9 critic, 3 mutation-tester, 3 connector, 3 scribe, 2 sentinel, 1 scout, 1 simplifier.
  - w2: 34 seats — 12 reviewer, 10 critic, 7 executor, 2 connector, 1 mutation-tester, 1 sentinel, 1 simplifier.
  - No residual call. Round total: 77 seats. Dead seats: 0; every seat settled with a report (`w1-results.json`, `w2-results.json`).
  - m_flash roles were 25/43 and 19/34 of the seats; attack roles were 23/43 and 23/34.
- **Routing:** the run-8 map from `~/.omp/agent/config.yml`. No model was passed.
- **Planner seat:** held by the L1 (orchestrator ruling 2026-10-19).
- **Spawn:** every wave was spawned inline by the orchestrator from my `.ready` files.
- **Incidents:**
  - Seat `C1RevIntegration` left an empty `/tmp/tiny` directory. It was not a mount. I removed it.
  - Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows only `?? .ufo/reports/round-42/kengaku.md`, which belongs to another lane and was not touched. No lane-42 misroot.
- **Tool installs:** none, by me or by any seat that reported.
- **L0 questions:** none opened.
