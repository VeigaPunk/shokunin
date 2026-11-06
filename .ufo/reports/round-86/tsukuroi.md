# tsukuroi — round 86 report (attempt 1)

L1: TsukuroiR86. Lane `tsukuroi-shokunin`, branch `master`. Pre-round tip `3f56789829b84a97b2a8aa786618022195ef53cb`.
Final lane hash `1d4bf1e8a153b383c5b819f2c2dca9dfb9891ded`: pushed, and `git ls-remote origin refs/heads/master`
prints it. My reading as L1: C1 met its frozen target, but its discrimination is partial (see below). C2 is
exploratory and waits on the closure's non-author judgment. Admission is for the closure or the operator to decide.
This round also caused a **host incident**: one seat rewrote both UKIs in `/boot`. An L0 question is filed; see the
extras section.

## Work performed

Declared claims, frozen at `2f67de80` before the candidate was scored:
- **C1 — operability, measured, sourced S346–S348.** Change `tools/check-hibernate-resume.py` to parse boot tokens
  the way Linux v7.2 does:
  - a `__setup` option matches any token that starts with it, with `-` and `_` treated as equal;
  - `noresume` and `nohibernate` ignore any value attached to them;
  - when `resume=` appears more than once, the last one wins, and an empty `resume=` counts as absent;
  - a `resume_offset=` value with no leading digit is skipped, as sscanf does.

  The change is scored by the new frozen battery `tools/resume-gate-battery-r86.py`: 30 families, target 30/30 in
  each of three consecutive runs at the landed tip. This answers r85 routed defects 2 and 4.
- **C2 — depth, exploratory, sourced S346–S348 + S343.** Depth is tied for the lowest axis at 8. The claim is a new
  knowledge entry, `corpus/knowledge/hibernation-boot-parse-r86.md` (+ `.json`), rows BP1–BP8.

Work items:
- **Inputs read:** the r85 closure (`admitted`) and `corpus/lessons/round-85-verifier-spotcheck.md` §5. All five routed
  defects are dispositioned (`corpus/lessons/round-86.md` "Inputs read").
- **Freeze `2f67de803484c3a0b42efd0041f78ceb9828e3a8`:**
  - the battery, sha256 `a49a18aa…fbc21`;
  - five Linux v7.2 sources pinned in `.ufo/waves/round-86/before/src/SHA256SUMS`;
  - controls, each run three times (`before/controls/controls-summary.txt`):
    - K1 do-nothing (the r85 gate): 26/30;
    - near-miss N01–N12 (candidate draft minus one property each): 26–29/30, each failing exactly its own family;
    - the r85 forgers f1–f10, MutGate M26–M28 and k1–k6, carried over: 0–25/30;
  - battery `--selftest` PASS 4/4.
- **Candidate `dc8849494cefe92c4a562de07fee667c4ec0bcc8`:** the gate parse described under C1, plus `--selftest` with 13 fixtures.
- **Entry `1e1caabcdd740a6429dd31d7aba3b725ff8c677d`:**
  - rows BP1–BP8;
  - SOURCES S346–S349;
  - the r85 entry's Limits now cite the pinned S346 and S349 (r85 routed defect 5);
  - host receipt `before/host/receipt.txt`.
- **Wave w1** (14 seats). All of them are integrated, in `b96dc4be` and `1d4bf1e8`:
  - ExecReplicate reproduced 30/30 three times in a clean clone; every control matched to the family (`w1/ExecReplicate.md`).
  - MutGate: 22 of 24 mutants killed. M19 survives and is routed. M06EQ is equivalent (`w1/MutGate.md`).
  - MutBattery: every round-86 family is load-bearing (`w1/MutBattery.md`).
  - CriticClaims: the near-miss forger `f4-shortcut` reads **30/30**, which makes discrimination partial (`w1/CriticClaims.md` §1). The N01–N12 sentences hold 12 of 12 (§4).
  - CriticKernel found six divergences from the kernel, all outside the frozen families. They are routed as R86-R1 and R86-R2 (`w1/CriticKernel.md`).
  - ReviewGate found no defect (`w1/ReviewGate.md`).
  - ReviewEntry (advisory; a seat is the lane): 6 rows support, 2 partial (BP7, BP8). Both rows were reworded at `b96dc4be`.
  - ScoutPrefix checked 758 v7.2 `__setup`/`early_param` registrations and found no first-match collision. The entry's Limits line now records this.
  - ScoutSources re-fetched all five pins live (sha256 equal); the cited regions are identical at v7.2.11. It also found S346 `used-by` incomplete, which is now fixed.
  - ScoutHost read the host cmdline through the new rule; it is consistent with the receipt. **This seat caused the host incident.**
  - ExecSelftests wrote `nonauthor-label --selftest`, which is landed. It also found battery selftest defects D1 and D2, routed as R86-R4.
  - ExecLints found that the registry row was missing at the entry commit. It was closed at landing.
  - ScribeLesson drafted M1 and QUALITY 123, both landed.
  - ConnectorOverlap: no sibling holds `obsolete_checksetup` or `parameqn` ground; mori's kernel-parameters.txt pin is the same file but a disjoint claim.
- **Mistakes mined** (`corpus/lessons/round-86.md`):
  - M1: a divergence disclosed in Limits shipped as a gate rule. This adds QUALITY 123.
  - M2: the new rules were never composed with other faults; captured-by QUALITY 119.
  - M3: `objcopy` was used as a read-only probe.

## Landed changes

| Commit | Content | LOG.md entry |
|---|---|---|
| `2f67de803484c3a0b42efd0041f78ceb9828e3a8` | freeze: battery r86, pinned sources, controls, SCORECARD declaration | "Round 86" **Freeze** |
| `dc8849494cefe92c4a562de07fee667c4ec0bcc8` | candidate gate parse + `--selftest` | **Candidate** |
| `1e1caabcdd740a6429dd31d7aba3b725ff8c677d` | entry BP1–BP8, S346–S349, r85 Limits repoint, host receipt | **Entry** |
| `b96dc4beb8b826dab80ff07411b07c549c7a1b17` | lesson (Gate, M1–M2, routed), QUALITY 123, entry fixes, `nonauthor-label --selftest`, registry rows, README frontier | **Landing** |
| `1d4bf1e8a153b383c5b819f2c2dca9dfb9891ded` | wave w1 evidence + results, measured outcome, S346 used-by, lesson M3, host-incident LOG note | **Landing** / host incident |

## Before → after measurements

- **C1:** counting command `python3 tools/resume-gate-battery-r86.py --gate tools/check-hibernate-resume.py`.
  - **Before:** the do-nothing K1 reads 26/30 in all three runs at the freeze `2f67de80`
    (`before/controls/receipts/K1-r85-gate-do-nothing-run{1,2,3}.json`).
  - **After:** 30/30 `met`, rc 0, in all three runs at the landed tip `b96dc4be`
    (`.ufo/waves/round-86/after/measured-at-landing.txt`, `after/runs/cand-run{1,2,3}.json`).
  - Battery bytes equal the freeze manifest. Gate bytes have not changed since `dc884949`, and the tip `1d4bf1e8`
    changes no tool.
  - K1 at the tip: 26/30. Its rc was not captured by the shell; the receipt notes this.
  - **Partial discrimination:** `w1/CriticClaims/forgers/f4-shortcut.py` reads 30/30 at the tip as well. A 30/30
    therefore does not certify two clauses of the predicate sentence:
    - a suffixed `noresume`/`nohibernate` token combined with chain faults;
    - a skipped offset on a faulty base.

    The candidate answers both correctly (`w1/CriticClaims/counter/transcript.txt`). This is not prettified. The
    lesson records it as M2, and the battery patch is routed to round 87 as R86-R3.
- **C2:** exploratory, so it has no counting command. Prior state:
  `git grep -n -i 'obsolete_checksetup\|parameqn' 3f567898 -- corpus/knowledge` finds a single Limits line,
  `hibernation-availability-r85.md:56`, and no sourced row. After: eight rows, BP1–BP8, at `1d4bf1e8`.

## Sources & frontier

- Census command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tsukuroi`.
  - Start: exit 0, rows 345, 52 W04 (`.ufo/waves/round-86/before/census-before.txt`).
  - End: exit 0, `tsukuroi ok`, rows 349, 52 W04, no E code.
  - Row count: `grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' corpus/SOURCES.md`.
- Rows added: 4, all tier A code — S346 `init/main.c`, S347 `kernel/params.c`, S348 `lib/vsprintf.c`,
  S349 `kernel/power/main.c`.
- Rows touched, old→new:
  - S343 `used-by` gains `hibernation-boot-parse-r86.md`;
  - S346 `used-by` gains `hibernation-availability-r85.md`.
- The Gate records 5 admits and 1 reject (man7 `bootparam(7)`, a whole-name lookup that contradicts the v7.2 code).
- Sourced claims: both C1 and C2 rest on S346–S348, opened this round.
- Frontier rows advanced: README "Round 86" (the r85 tokenizer frontier bullet is closed). Opened: tokenizer `--`
  and quoting, device class, battery composition.
- Assimilation: none. considerthese: none mined this round.

## Trend verdicts

- **expansion — unprovable-but-better.** New sourced ground: the boot-parse plane, plus 4 tier-A rows (345 → 349).
  New ground is a judgment, not a count.
- **quality — improved.**
  - Three gates gained `--selftest`; each can fail (`w1/ExecSelftests/receipts/02-*`, `w1/MutGate.md` selftest column).
  - Registry 136/136 and header gate 102/102 at `1d4bf1e8`.
  - QUALITY 123 landed.
  - Two false-HEALTHY paths from r85 are fixed: `noresume=1`/`nohibernate=1` and an empty `resume=`.
- **discernment — improved.**
  - The lane's own critic falsified the certification breadth of C1, and the report says so (M2) rather than smoothing it.
  - The r85 reject class was applied again (bootparam(7)).
  - The near-miss controls were certified sentence by sentence (12/12).

## SHONEN

- [~] SKILL.md decision tables / error patterns / checklists / cited sources. Evidence: registry rows for
  `hibernate-resume`, `resume-gate-battery-r86`, `nonauthor-label` in `SKILL.md` at `b96dc4be`. Non-author verification is owed.
- [~] End-to-end domain task logged in LOG.md. Evidence: LOG.md "Round 86": host cmdline → kernel parse rule → gate
  `--live` HEALTHY, plus the entry's Operator actions.
- [~] Instructions executable without oral context. Evidence: the gate's and battery's docstrings and `--selftest`
  modes, and the entry's `recheck:` line. No no-oral-context retest was run.
- [~] No cross-domain bleed. Evidence: `.ufo/waves/round-86/w1/ConnectorOverlap.md` (no conflict; PROVINCE.md unchanged).

## Round shape and extras

- **Shape:** one v1 wave, w1, with 14 seats: scout 3, executor 3, mutation-tester 2, critic 2, reviewer 2, scribe 1,
  connector 1. Attack seats: 6 of 14. No residual call; the round total is 14. Dead seats: 0 (`w1-results.json`, 14 settled).
- **Planner seat:** held by the L1, because the validator refuses `planner`.
- **HOST INCIDENT.** Seat ScoutHost ran `sudo objcopy --dump-section` on `/boot/EFI/Linux/*.efi` at 18:11 -03, and
  objcopy rewrote both UKIs in place.
  - Damage: 5 PE header bytes in each file; the seat reports the payloads unchanged.
  - L1 check, read-only: the `/boot/limine.conf` BLAKE2b pins now mismatch — `b990d8c6…` vs `57f5eb94…` on disk, and
    `a68c281d…` vs `eff78d32…`.
  - The lane did not repair it, because the boot chain belongs to the operator.
  - L0 question appended (`tsukuroi | round-86 | HOST INCIDENT …`). Main was messaged. Lesson M3.
- **Misroot sweep:** fleet `git status --porcelain` shows only `.scratch/` and my L0 append. There is no misroot.
- **Scratch:** `/fast/scratch/hyaku/tsukuroi-r86` was removed after landing.
- **Stale-lane:** respawn-per-round driver; no other mission of this lane is open.
- **Tool installs:** none.
- **Open L0 questions:** the round-86 host incident above.
