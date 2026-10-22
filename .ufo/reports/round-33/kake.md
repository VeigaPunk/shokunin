# kake — round 33 report

L1 `KakeR33` (hyaku in-session, attempt 1). Lane `/home/vgpnk/Projects/shokunin/kake-shokunin`.
Base `5777d5af79cac1ebf9144b348a9d274099e77338`. Lane tip (pushed) `93359ff0924bf622acc51eb15c2afa3cd2743022`.
No earlier attempt of this round (`.ufo/watchdog.log` has only the `launch kake round=33 … attempt=1` line). No inherited leftovers: lane status was clean at start.

## Work performed

Declared claims (`SCORECARD.md` "Round 33 — declared claims", commit `bc6c4a8`, both counters frozen in that commit before any run):

- **C1 — operability (routed repair, round-32 spot-check items 2 and 3):** the hostile selftest's P6 check keys on a structured refusal `code`, not message text. Counter `c1_code_probe.py`: met 2 → 4 of 4, guard_ok true.
- **C2 — freshness (sourced, learning claim, different surface from the citing-set gate):** the corpus' ds4cc-marketplace source pin advances from `1fbdb8ed` to upstream head `7fc6aa2f` (one commit: three `/magga/frostbite/` pages, sitemap 97 → 100 locs). Four files retained by path, mode and blob id. New row S065. A superseding entry section whose stated loc count and three canonical verdicts the counter re-derives. Counter `c2_pin_count.py`: met 0 → 4 of 4.

Work items:
- C1 build: the runner has `CaseRefusal`/`SetupRefusal` and a `code` on every row and failure entry. The hostile selftest has a `reason_code` key and P6 uses it (`b1752a2`). The new probe gates kills on `guard_ok` and records a timeout as a verdict (round-32 item 3), `.ufo/waves/round-33/c1_code_probe.py`.
- C1 strict supplement, added after wave-1 `CriticC1RepairScope` built a commit (`489714be`) that scores the frozen probe 4 by putting the code into the message text. Supplement: 0/4 at base, 4/4 at `b1752a2`…`3abfc44`, 1/4 on `489714be` (`.ufo/waves/round-33/c1_strict_supplement.py`, `verification/c1-strict-at-*.json`).
- C2 build: retained bytes `.ufo/waves/round-33/sources/ds4cc-7fc6aa2f/`, S065 (`corpus/SOURCES.md:73`), section "Round-33 ds4cc source pin 7fc6aa2f" in `corpus/knowledge/sitemap-orphan-audit.md` (`b1752a2`).
- Freshness learning from wave 1, landed at `e490381`, all in `corpus/knowledge/sitemap-orphan-audit.md` "Round-33 wave-1 additions":
  - S066: GitHub's record of the Pages deploy run for `7fc6aa2f` (success) and an apps-sdk test workflow that failed on its six latest main pushes.
  - Sitemap-to-tree parity (100/100 mapped).
  - Older 93/96/97 counts marked historical.
  - Stale `freshness-pins.json` values flagged.
  - Wave-2 corrections section added at `3abfc44`.
- Grounded SKILL.md table "Upstream source moved after a pin — round 33" (7 rows; wave-2 `ReviewSkillPinTable`: all grounded).
- Routed repairs outside the claims:
  - Per-run private default scratch: concurrent `citing_set.py --selftest` went from 3 of 4 failing at base to 0 of 4 (`verification/concurrency-*.txt`).
  - `read_expected` OSError catch. This is defensive: no tried shape escaped at base.
  - Stray fixture-root files and FIFOs now exit 2; symlinks stay per-case refusals (`3abfc44`).
  - Hostile spec-dir strays, whitespace-only keys and an unreadable spec directory now exit 2.
  - PROVINCE five → six correction.
- Frontier step:
  - SOURCES curated: S065 and S066 opened this round.
  - Census before/after recorded.
  - One mistake mined, plus one misroot row.
  - QUALITY "Round-33 criteria" added: two criteria with checks shown able to fail (`.ufo/waves/round-33/criteria/`).
- Round-32 spot-check routing: all seven items are dispositioned in `corpus/lessons/round-33.md` "Round-32 routed defects — disposition":
  - Fixed: items 2, 3, 5 and 6, plus two of the three parts of item 7.
  - Item 4: the old counter is not reused; a replacement counter and a QUALITY criterion were added.
  - Item 1 (Git-pin mutants m3d/m3f/m3g): not killed. m3d/m3f are equivalent under the setup vocabulary. m3f/m3g change a gate finding that the runner does not code (`w1/ExecPinMutantsP7.md`).
  - Item 7, duplicated option tables: the proposed patch was rejected because it breaks temp-path runner copies (confirmed by `w2/CriticOptionTableRejection.md`).
- Holds `KakeR31.CriticC1Counter` and `KakeR31.CriticSandboxThreatModel` were not recreated. Both wave contexts fenced them off, and two seats stopped at that boundary.

## Landed changes

All landed through `jj-lane.sh` (`landed` lines). Each is tied to the round-33 LOG.md entry:

| commit | content |
|---|---|
| `bc6c4a8` | declaration + frozen counters |
| `b1752a2` | C1 build; C2 build; before receipts |
| `e490381` | runner repairs; S066; entry wave-1 additions; strict supplement; after receipts; lesson draft |
| `1cf452e` | hostile selftest hardening; QUALITY round-33 criteria and checks; SKILL/PROVINCE/README sections; lesson mistakes and dispositions |
| `0a0acfb` | SCORECARD measured results + wave-1 corrections; LOG entry |
| `d2ed431` | wave-1 reports + registry; P7 wording; runner docstring; PROVINCE network-read correction |
| `3abfc44` | wave-2 repairs (stray symlinks per-case, unreadable spec dir); corrections in SKILL, SCORECARD, entry |
| `93359ff` | wave-2 reports + registry; receipts at `3abfc44`; census after; lesson wave-2 corrections; LOG wave 2 |

## Before → after measurements

| claim | command | before | after |
|---|---|---|---|
| C1 | `python3 -B .ufo/waves/round-33/c1_code_probe.py --rev <rev>` | `5777d5a`: met 2/4, guard_ok true | `b1752a2`, `e490381`, `1cf452e`, `3abfc44`: met 4/4, guard_ok true, benign 45/0; `93359ff`: 4/4 (run, not committed) |
| C2 | `python3 -B .ufo/waves/round-33/c2_pin_count.py --rev <rev>` | `5777d5a`: met 0/4 | same revisions: met 4/4 |

- Receipts are in `.ufo/waves/round-33/verification/`.
- Wave-2 re-runs reproduced every receipt field for field (`w2/RerunC1After.md`, `w2/RerunC2After.md`, `w2/RerunC1Strict.md`).
- Disclosed counter limits, in SCORECARD "Round 33 — measured results" and its corrections:
  - C1's frozen probe accepts a code-in-text commit; the strict supplement covers that case.
  - C2 scores 4 on a junk S065 row with the right id, status, date and hash plus copied metrics. It passes the new hollow-control criterion: the hollow commit scores 0/4 (`w2/ExecCounterControlOnR33.md`).
- Declaration timing: the declaration time is the committer time of `bc6c4a8` (19:52:44Z). Pre-declaration screening of C2's inputs is fully disclosed (`w2/CriticDeclarationCorrection.md`).

## Sources & frontier

- Census command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kake`
  - Round start: exit 0 (`.ufo/waves/round-33/census-before.txt`).
  - Round end: exit 0 (`census-after.txt`).
  - Output both times: `W04 S033 duplicate url` (pre-existing) and `ok`.
- Rows: 64 → 66 (`git show <rev>:corpus/SOURCES.md | grep -c '^| S0'`). Census mode after (`census-mode-after.txt`): A55 / B1 / C10; mined 51, queued 6, rejected 9.
- Rows added by tier: tier A +2.
  - S065, `code`: the upstream commit's sitemap and three pages.
  - S066, `dataset`: GitHub Actions run records.
- Rows touched old → new:
  - S065: `—` → `mined`, opened 2026-10-22, recheck 90d, used-by `corpus/knowledge/sitemap-orphan-audit.md`.
  - S066: same values.
  - No other row changed (`w2/ReviewLessonGate.md`).
- Gate with URLs, access dates and ≤25-word located quotes: `corpus/lessons/round-33.md` `## Gate`.
- Sourced claim: C2 cites S065, and the wave-1 additions cite S066.
- Frontier advanced: ds4cc upstream pin; publishing-run record as a freshness source; the SKILL decision table for a moved pin.
- Mistakes mined (lesson `## Mistakes`):
  - A repair counter accepted a faked repair at its after-value. Fix: QUALITY criterion plus check, shown failing on the bundled round-32 hollow commit (`verification/criterion-counter-control-r32-c2.txt`, exit 1).
  - A seat report was misrooted. It was moved byte-exact from the fleet root into the lane and the fleet copy deleted (see below).

## Trend verdicts

- **expansion: improved.**
  - New knowledge of the property's current upstream state (S065, S066).
  - A grounded decision table for a moved pin.
  - Publishing-run evidence the corpus never held, including the apps-sdk failure streak.
  - Evidence: `corpus/knowledge/sitemap-orphan-audit.md` round-33 sections, `SKILL.md` round-33 table.
- **quality: improved.**
  - The P6 refusal is pinned by code. A reworded runner passes, and the m3 and recoded variants are killed (C1).
  - Concurrency collision fixed.
  - Entry facts re-derivable from retained bytes: wave-2 found 26/26 sentences supported and all seven single-condition mutations detected.
- **discernment: improved.**
  - Two QUALITY criteria with checks shown able to fail.
  - One option-table patch rejected with a confirmed reason.
  - Wave-2 overclaims corrected by append, not hidden: PROVINCE network reads, code scope, stray-symlink behaviour, declaration screening.
  - The non-author outside check is still owed to the closure.

## SHONEN

- [~] SKILL.md has real decision tables, error patterns, checklists and cited sources — `SKILL.md` "Upstream source moved after a pin — round 33" (wave-2 `ReviewSkillPinTable`: 7/7 rows grounded).
- [~] At least one end-to-end domain task executed and logged in LOG.md:
  - Owned property source re-pinned and audited offline: canonical, base-path and parity checks plus the forge deploy record (LOG.md round 33, `corpus/knowledge/sitemap-orphan-audit.md`).
  - No live serving was observed.
- [~] Instructions executable by an agent without oral context — round-33 probe, supplement and criteria commands are written with arguments in SCORECARD/QUALITY/SKILL; wave-2 re-ran each from those strings.
- [~] No cross-domain bleed (PROVINCE.md accurate):
  - PROVINCE count corrected and the round-33 step appended.
  - Network-read overclaim corrected (`PROVINCE.md` round-33 sections; `w2/ReviewProvinceReadme33.md`).

## Round shape and seats

- Shape: two v1 waves (policy `ufo-wave-policy.json`), each validated and dispatched as one `task` call with the validator's `taskCall` unchanged. Seat gate `wave-slot.sh` granted both waves and both were released.
  - Wave 1 `kake-r33-w1`: 35 seats — 11 executor, 6 scribe, 6 reviewer, 5 scout, 3 critic, 2 mutation-tester, 1 connector, 1 revenger.
  - Wave 2 `kake-r33-w2`: 34 seats — 17 reviewer, 6 executor, 5 critic, 4 mutation-tester, 2 scout.
  - Round total: 69 seats. No residual call.
- Dead seats: none. Refusal holds: none this round.
- Planner seat: held by the L1. The planning data-walk rode `ReviewSpotcheckRoutingMap` (reviewer) and `ConnectorSiblingOverlap` (connector).
- Registries: `.ufo/waves/round-33/w{1,2}/swarm-registry.json` (agent ids recorded). Routing: the role routes from `task.agentModelOverrides`; no `model` was passed.
- Misroot: wave-2 `ScoutPinsFlagAccuracy` wrote its report under the fleet root. It was copied byte-exact into the lane (`cmp` identical) and the fleet copy and its empty directories deleted. Recorded under `## Mistakes`.
- Other untracked fleet-root files are not this lane's (no kake content) and were left untouched: `AGENTS.md`, `live_s228.html`, `nama.html`, `tf_bavelas.html`, `write`.

## Other

- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
- Tool installs: none by the L1. Seats report none. `gh 2.102.0` was already present; pacman was not used.
- Open L0 questions: none added.
- Carried open (lesson): Git-pin mutants; duplicated option tables; NUL-byte runner crash (pre-existing); `freshness-pins.json` re-pin (three values); unqualified ds4cc counts listed in the entry; round-31 QUALITY F1–F3.
