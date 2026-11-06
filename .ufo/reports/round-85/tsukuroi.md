# tsukuroi — round 85 report (attempt 1)

L1: TsukuroiR85. Lane `tsukuroi-shokunin`, branch `master`, pre-round tip `3ed94533d581aa542d330ce2c97a798983839348`,
final lane hash `92be75064a53aec359976eef7af890f7311b47ac` (pushed; `git ls-remote origin refs/heads/master` prints it).
L1 reading: C2 met its frozen target, but only some of its discrimination holds (details below). C1 is exploratory and
waits on the closure's non-author judgment. The operator or closure decides admission.

## Work performed

Declared claims (frozen at `66374a4d`, before any candidate file existed):
- **C2: operability, measured, sourced S343–S345.** The hibernate gate `tools/check-hibernate-resume.py` gains
  hibernation-*availability* rules A1–A3. It is scored by the new frozen battery `tools/resume-gate-battery-r85.py`
  (20 families, target 20/20 in three consecutive runs).
- **C1: depth, the tied-lowest axis at 8, exploratory, sourced S343–S345 + S336.** A new plane
  `corpus/knowledge/hibernation-availability-r85.md` (HA1–HA9), on ground no entry held.

Work items:
- Fresh-start read: MANIFEST tsukuroi r82/r83/r84 (`rejected-honest-stop` each) and `corpus/lessons/round-8{2,3,4}-verifier-spotcheck.md`.
  Root failures are stated in `SCORECARD.md` "Round 85 — declaration" (commit `66374a4d`).
- Freeze `66374a4db963e5c655506e64cb0fea2d67ec9d0d` contains:
  - the battery, sha256 `b30a7c1e…ba21`;
  - four pinned Linux v7.2 sources (`.ufo/waves/round-85/before/src/SHA256SUMS`);
  - the host receipt `before/host/receipt.txt`, showing lockdown `[none] integrity confidentiality`;
  - ten candidate-free controls run first (`before/controls/controls-receipt.txt`): K0 absent 0/20, **K1 r84 gate
    (do-nothing) 0/20**, K2 schema shim 13/20, K3a–e r84 forgers 0–13/20, K4 const-HEALTHY 2/20, K5 v2 order replay 0/20,
    K6 substring sniffer 14–15/20.
- Candidate `479d868b2fc8969a19a617cd55ced5c13edd84b6` adds:
  - three gate findings: HR-HIBERNATE-DISABLED, HR-LOCKDOWN-BLOCKS, HR-NORESUME-ARG;
  - the `hibernate=` prefix order, with `nohibernate` suppressing `noresume`;
  - availability findings kept when `resume=` is absent;
  - capture schema `resume-facts/2` with a `lockdown` key.
- Wave w1 had 13 seats and was integrated in the landing commits `ffae885f` and `6a8296f6`:
  - ExecReplicate: 20/20 in five runs; every control still `unmet`.
  - ExecCleanRoom: an independent gate reads 20/20 three times; 7200 fuzzed documents show 0 candidate-wrong disagreements.
  - MutGate: 25 of 28 mutants killed. M26–M28 survive.
  - MutBattery: F-1, an accept-v1 gate, reads 20/20 in 10 of 33 runs.
  - CriticClaims: five edge-deviating gates read 20/20.
  - ReviewGate: no defect; Limits L1–L4.
  - ScoutSources: 4/4 sources byte-identical; the cited regions are identical at v7.2.11.
  - ScoutHost: all four `hibernation_available()` conjuncts are false on this host, and rule 8 fires when hibernation is unavailable.
  - ReviewEntry: 7 supports and 1 partial (advisory; a seat is the lane).
  - ScribeEntry/ScribeFrontier produced drafts. ExecLints built two checks. ConnectorOverlap found no sibling conflict
    (mori declares sleep/hibernation diagnosis tsukuroi ground).
- Routed defects from the r84 spot-check, all dispositioned (`corpus/lessons/round-85.md` "Routed defects received"):
  - header lines added to the r84 entry;
  - the "non-author" wording corrected;
  - the r85 battery frozen with the r84 forgers as controls;
  - the provenance counter not cited;
  - commits cited in graph order.

## Landed changes

| Commit | Change | LOG.md |
|---|---|---|
| `66374a4d` | freeze: battery r85, controls K0–K6 + receipts, pinned sources, host base, SCORECARD declaration | "Round 85" §Freeze |
| `479d868b` | candidate: gate v2 + capture `lockdown` key | §Candidate |
| `ffae885f` | entry HA1–HA9 (+ .json); S343–S345 added and the S336 anchor extended; lesson M1–M4; QUALITY 120–122; `tools/check-nonauthor-label-r85.py`; r84 entry header and wording repair; SKILL registry rows; README coverage and frontier | §Landing |
| `6a8296f6` | wave w1 evidence, `after/measured-at-landing.txt`, SCORECARD outcome, LOG, ScoutHost rule-8 integration | §Landing |
| `92be7506` | ExecCleanRoom fuzz corpus receipt (4 MiB, named explicitly) | §Wave |

## Before → after measurements

- **C2.** Counting command: `python3 tools/resume-gate-battery-r85.py --gate tools/check-hibernate-resume.py`.
  - Before: the do-nothing candidate (K1) reads 0/20 at freeze `66374a4d`.
  - After: three consecutive runs read **20/20, `met`, rc 0** at `ffae885fc136596cca400bbed4e8f190693edfc2`
    (`.ufo/waves/round-85/after/measured-at-landing.txt`, `after/runs/cand-run{1,2,3}.json`). The battery
    sha256 is unchanged, and K0–K6 re-run at the tip read 0–14/20.
  - Not smoothed:
    - A gate implementing A1/A3 as exact tokens (`w1/CriticClaims/forgers/f1-literal-avail.py`; re-run by the L1: 20/20) also meets the target.
    - So does a four-deviation stack (`f7-mutant-stack.py`: first `resume_offset=`, `<=` headroom, first-swap-only sums).
    - An accept-`resume-facts/1` gate meets it in 10 of 33 runs (MALFORMED samples its kinds).
  - The declaration's sentence "must … parse `hibernate=` by the kernel's prefix order" is therefore false (lesson M4, QUALITY 122).
  - The battery certifies the availability arm on its documented tokens, the rule-1 change, precedence and
    multi-fault reporting. No candidate-free forger reaches the target.
- **C1** (exploratory): there is no counting command. New ground: `git grep -il 'lockdown_hibernation\|nohibernate\|hibernation_available' 3ed94533 -- corpus/knowledge`
  exits 1. At `ffae885f` the entry holds 9 rows, and every quote was checked verbatim at its pinned raw lines (L1 check).
  It needs the closure's non-author `unprovable-but-better` ruling. Depth stays 8.

## Sources & frontier

- Census: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tsukuroi`.
  - Round start: exit 0 (`.ufo/waves/round-85/before/census-before.txt`).
  - Round end: exit 0 (`tsukuroi ok`, W04 warnings only).
- Rows: `grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' corpus/SOURCES.md` 342 → 345.
  - Added by tier: A +3 (S343 hibernate.c, S344 security.h, S345 lockdown.c; code, `mined`, opened 2026-11-06).
  - Touched: S336 scope, anchor and used-by, logged old→new in the lesson's Gate section.
- Gate: 3 admits; 3 rejects, each with a reason and a flip condition (man7 `kernel_lockdown(7)`, two ArchWiki sentences).
- Sourced claim: C2's rules and C1's rows cite S343–S345.
- Mistakes mined: M1 (a seat labelled non-author → QUALITY 120 + check, red/green/mutant), M2 (an existing header gate
  was never run → QUALITY 121; rc 1 at `3ed94533`, rc 0 at `ffae885f`), M3 (sampled MALFORMED kinds, no edge legs),
  M4 (a "must" sentence with no near-miss control → QUALITY 122).
- Frontier rows advanced: `corpus/README.md` "Frontier (round-85 addition)".
- Assimilation: none. considerthese: none mined this round.

## Trend verdicts

- **expansion: unprovable-but-better.** New availability plane on ground no entry held (grep above). It rests on
  the closure's judgment, not a count.
- **quality: improved.** QUALITY 120–122 each landed with red evidence. Two r84 routed defects were repaired, and
  `check-knowledge-header.py` now reads rc 0 on 101/101 notes. Registry coverage passes 135/135. The census selftest
  passes 218/218 (no harm).
- **discernment: improved.** The lane's own critic and mutation seats falsified the declaration's discrimination
  sentence, and it is reported as a mistake (M3/M4) rather than hidden. Gate rejects carry reasons and flip
  conditions, and every r84 routed defect is dispositioned.

## SHONEN

- [~] SKILL.md decision tables / error patterns / checklists / cited sources — evidence: the registry rows for
  hibernate-resume, resume-gate-battery-r85 and nonauthor-label in `SKILL.md` (commit `ffae885f`). Non-author verification is owed.
- [~] End-to-end domain task logged in LOG.md — evidence: LOG.md "Round 85": host capture → `--live` HEALTHY
  → availability rows → operator actions (`corpus/knowledge/hibernation-availability-r85.md` §Operator actions).
- [~] Instructions executable without oral context — evidence: the gate and battery docstrings and the entry's
  `recheck:` line. No no-oral-context retest was run.
- [~] No cross-domain bleed — evidence: `.ufo/waves/round-85/w1/ConnectorOverlap.md` (no sibling conflict;
  PROVINCE.md unchanged).

## Round shape and extras

- Shape: one v1 wave, w1, with 13 seats (scout 2, executor 3, mutation-tester 2, reviewer 2, critic 1, scribe 2,
  connector 1). Attack seats: 5/13. No residual call; round total 13.
- Planner seat: held by the L1. Dead seats: 0 (`w1-results.json`: all 13 returned output).
- Misroot sweep: `git status --porcelain` at the fleet root shows only orchestrator `.scratch/` paths, so there is no misroot.
- Scratch `/fast/scratch/hyaku/tsukuroi-r85` was removed.
- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
- Tool installs: none. Open L0 questions: none.
