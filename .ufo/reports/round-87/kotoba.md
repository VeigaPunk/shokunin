# kotoba — round 87 report (hyaku run 15, Linux host, omp/18.15.0)

Lane repo `/home/vgpnk/Projects/shokunin/kotoba-shokunin`, branch `master` (jj-colocated; git backend).
Base `223ae62424f8ab1eb365d733eb648d6228ddd7e8` (the round-86 non-author spot-check landing).
Freeze `669f2801c31ef27e18cc35a327d2e18f466281c7` (`plans/round-87.md` alone, before any candidate
data); addendum 1 `512126bbd762ff82b9f330c4afefb29db7cd9f39`; addendum 2
`87ab1cb98b4950f5d7291a4a2ddaab535ca72124`. Lane tip after this attempt: `74048151100e49ce2c628926c88f8b055a52026d`
(pushed; `git ls-remote origin refs/heads/master` prints it).

**Attempt history (from `.ufo/watchdog.log`).** Round 87 was launched eight times before this
attempt: `19:56`, `20:35`, `20:44`, `21:02` (cycle 1) and `22:29`, `22:31`, `22:32` (cycle 2), with
five `lane-dead-no-report kotoba round=87` lines; the round's work and its first report (fleet commit
`d752fdbe9cdf82a6faff730d44f44c6fa3e3eb00`, 21:24) were landed by an earlier instance. This attempt
(`launch … 23:51:44 … attempt=1`) inherited that work whole — the lane worktree was clean,
`local == remote == 760e1c5e` — re-verified it, and lands what the re-verification found. Nothing
inherited was discarded; nothing uncommitted existed.

**Declared claims (frozen; unchanged by this attempt).** Two, on two distinct owned axes. Neither is
exploratory; no target was narrowed, re-worded or re-scored after data.

- **C1 — depth** (the lane's lowest owned axis, score 9): *omp root semantics grounded per root.*
  `python3 -B verifiers/check_omp_root_semantics.py --rev <rev>` → `omp root semantics grounded N of
  12`, exit 0 iff N == 12 and guards S1–S3 PASS. Target 12 of 12; base 0 of 12.
- **C2 — consistency** (the calibration sub-axis, score 10): *the five routed round-86 defects close.*
  `python3 -B verifiers/check_r86_routed_repairs.py --rev <rev>` → `r86 routed defects closed N of 5`,
  exit 0 iff N == 5. Target 5 of 5; base 0 of 5 (a committed earlier measurement, see below).

## Work performed

The round's claims are carried unchanged from the freeze; this attempt re-derived both counters at the
tip, attacked them with twelve L2 seats, and landed the one thing the re-derivation found plus the
criteria it implies.

- **Both counters re-derived at the tip.** At `760e1c5e` C1 reads `12 of 12`, `exit=0`, guards S1–S3
  PASS; C2 reads `4 of 5`, `exit=1` (D1–D4 PASS, D5(i)/(ii)/(iv) PASS, **D5(iii) FAIL**). Evidence:
  `.ufo/waves/round-87/w3/l1/c1-tip.txt`; `.ufo/waves/round-87/w3/l1/q79-control.txt`; the seats'
  independent runs in `.ufo/waves/round-87/w3/ExecTipR87/SUMMARY.json`.
- **C2's D5(iii) failure diagnosed to one external file.** `.ufo/reports/round-84/kama.md` landed on
  the fleet repo at 22:47 today (fleet commit `5b052020a13b37340c1054286d65b2514c7133d5`), healing the
  corpus gate's `report_dead` DRIFT; the frozen D5(iii) wanted exactly two reds, so the item flipped
  after the round's own 5-of-5 receipt (`receipts/c2-final.txt`) was written. Evidence:
  `.ufo/waves/round-87/w3/ExecMirrorR87/gate-lane.json` vs `gate-clone.json` (the same bytes in a
  relocated clone still read two reds, with the detail at `corpus/lessons/round-81.md:29`).
- **Q79 and its control landed.** `corpus/QUALITY.md` Q79 (a counter conjunct that executes a lane gate
  inherits the gate's resolution set and must be monotone in the direction of repair) plus the
  three-world control `.ufo/waves/round-87/w3/l1/q79_location_control.py`, which reads
  `q79 control: FAIL (same bytes, world-dependent verdict: 2 distinct readings)`, `exit=1`, and also
  runs the pinned world that reproduces the lane. Evidence: `w3/l1/q79-control.txt`.
- **C1's `{cwd}/` bound observed on the real client (new capability).** `ExecProbeBoundR87` enumerated
  the installed client under a scratch `HOME` with `omp skill list --json`: the cwd-chain skill reads
  `"source":"agents:project"`, the skill under the scratch `HOME` reads `"source":"agents:user"`, and
  from a cwd outside `$HOME` only the user scopes appears; `strace` shows zero `.agents/skills` opens
  above `$HOME` and zero `..` probes. Evidence: `.ufo/waves/round-87/w3/ExecProbeBoundR87/skill_list_json.txt`,
  `strace_skilllist.txt`, `skill_list_outside.txt`, and the capability row in `SCORECARD.md`
  § Capabilities (first working round 87).
- **C1's counter is a presence-and-ordering test, not a semantic one.** `CriticSemanticsR87` confirmed
  every honest `reader_quote` is executable code inside its own module chunk, then built four forgery
  worlds (a row's quote replaced by another root's reader, by `Zo.join(R.path, "commands")`, by another
  module's quote, and by a markdown template whose `Array#join` satisfies the token set) and **all four
  read `12 of 12`, exit 0**. Evidence: `.ufo/waves/round-87/w3/CriticSemanticsR87/forgery-worlds.txt`,
  `forgery-ledger-diffs.txt`, `attribution.txt`.
- **C1's conjunct 4 is dead at scoring.** The scoring path calls `run(...)` with `chain=FROZEN_CHAIN`,
  so conjunct 4's `expected` and `actual` are the same computation; only the self-test's `w_bound`
  world exercises it. Confirmed in `verifiers/check_omp_root_semantics.py` and by
  `SentinelEvidenceR87` (F-1). Evidence: `.ufo/waves/round-87/w3/SentinelEvidenceR87.md` § Verdict.
- **Coverage gap measured: 18 roots, 12 in the ledger.** `ScoutPatternsR87` re-derived the skill-root
  set from the ELF before reading either ledger and found six joins neither ledger carries
  (`~/.claude/skills` @173840218, `~/.codex/skills` @173882129, `~/.config/opencode/skills`
  @172785499, `~/.omp/skillshare/@scope/*/*` @173923798, two plugin-marketplace roots). The L1 re-read
  those offsets over the ELF independently; they are joins, not doc strings. Evidence:
  `.ufo/waves/round-87/w3/ScoutPatternsR87/three-way-table.md`,
  `.ufo/waves/round-87/w3/ScoutPatternsR87/derived-roots.txt`.
- **Two further instrument gaps named by the scouts.** The counter parses each row's `binary_quote`
  cell for arity but never matches it against the ELF, so a row could carry a wrong quote and still
  read GROUND (`w3/ScoutPatternsR87.md`); and the coverage hole is an asymmetry the ledgers themselves
  expose — rows 5/6 keep `~/.codex/skills` and `~/.config/opencode/skills` inside their
  `binary_quote` text while their `root_pattern` cell carries only the `{cwd}` half
  (`w3/ScoutPatternsR87/three-way-table.md`).
- **S256 re-opened and re-verified.** `ScoutSourceS256R87` re-fetched the row's URL: HTTP `200`,
  15 362 B, sha256 `4e66819cf706b81c6f31bd71e6de8892083a284525ab151948642faea00cb1b4` (matches the row's
  pin), quote located at upstream line 70. Evidence:
  `.ufo/waves/round-87/w3/ScoutSourceS256R87/02-fetch.txt`,
  `.ufo/waves/round-87/w3/ScoutSourceS256R87/03-reader-vs-doc.txt`.
- **Independent re-implementations of both claims.** `ReviewC1R87` wrote the four conjuncts from the
  plan alone and scored `reimpl grounded 12 of 12`, no per-row disagreement; `ReviewD1D5R87` re-checked
  D1–D5 from committed bytes and reports `C2 at tip: 4 of 5`. Evidence:
  `.ufo/waves/round-87/w3/ReviewC1R87.md`, `ReviewD1D5R87.md`.
- **Mutation pass.** `MutateR87` reports `C1 killers: 5/5; C2 killers: 2/3`, the survivor being the
  proposed subset form of D5(iii), which the tally pin (`7/9`) masks — i.e. the r88 repair must relax
  both conjuncts. Evidence: `.ufo/waves/round-87/w3/MutateR87.md`, `MutateR87/base/d5-forms.txt`.
- **Evidence audit and record corrections.** `SentinelEvidenceR87` found 5 findings (2 high, 2 medium,
  1 low) and confirmed the `/tmp`, credential, ready-file and confinement axes clean; `ScribeIndexR87`
  indexed 129 files and named five dangling pointers. Four record defects were fixed this attempt
  (a false `exit=0` in my own base receipt, a missing census receipt, a dangling `w1/Sentinel.md`
  pointer, and the Q73 sweep the plan promises as a separate receipt when it lives in the
  `q73_sweep` section of `receipts/base-battery.txt`). Evidence:
  `.ufo/waves/round-87/w3/SentinelEvidenceR87.md`, `ScribeIndexR87/INDEX.md`,
  `corpus/lessons/round-87.md` § Record corrections.
- **Cross-lane and staged-package overlap.** `ConnectOverlapR87`: no sibling lane holds the omp loader
  semantics; the staged `merge/kotoba/` package is real (mtime 2026-10-24 23:33, rounds 1–16) and its
  id space **collides** with the lane's (staged `S256` is the `agentskills.io` row the lane holds as
  `S002`; the lane's `S256` is the omp reader row). Evidence:
  `.ufo/waves/round-87/w3/ConnectOverlapR87.md`.
- **Correction to the first report.** Its `Assimilation: none` line said
  `/home/vgpnk/Projects/shokuknow/merge/` was absent; it exists and has since 2026-10-24 23:33
  (`stat -c '%y %n'`). The true statement is narrower: no staged material overlaps this round's
  claims, and the freeze admits one `SOURCES.md` row, so nothing was adopted.

## Landed changes

| change | commit | LOG entry |
|---|---|---|
| attempt-1 work (ledger, counters, knowledge entry, S256, Q78, receipts) | see that attempt's block (`760e1c5e` tip) | `LOG.md` § Round 87 |
| Q79 in `corpus/QUALITY.md`; attempt-2 lesson block, M87-2, record corrections; `LOG.md` and `SCORECARD.md` attempt-2 blocks; wave r87-w3 spec/dispatch/registry; L1 receipts and the Q79 control | `d1c031833c37af99196f72f84a6643f84eec129a` | `LOG.md` § Round 87, attempt 2 |
| wave r87-w3 seat evidence (the 10 seat reports that had landed) and the final lesson edits (forgery, coverage, dead-conjunct findings) | `3c8902a7f2bd6977a7f9520a363013248a08b127` | `LOG.md` § Round 87, attempt 2 |
| `SCORECARD.md` § Capabilities capability annotation (installed-client skill-channel probe); all 12 w3 seat reports; counters re-pinned at the tip | `3c8902a7f2bd6977a7f9520a363013248a08b127`, `e4b76dd00d054cc47f82f2bc75f7bd97e08870ad` | same |
| wave settlement `r87-w3-results.json` (12 of 12 seats) | `49b7d1b43ae23ae997a2d3110247b50e004c277a` | same |
| counter receipt at the settlement tip (run against `49b7d1b4`) | `74048151100e49ce2c628926c88f8b055a52026d` | same |

The two frozen counters, their ledgers, `corpus/SOURCES.md` and `SKILL.md` are **byte-unchanged** this
attempt (`git diff --stat 760e1c5e 3c8902a7 -- verifiers/check_omp_root_semantics.py
verifiers/check_r86_routed_repairs.py verifiers/omp-skill-roots-semantics.tsv corpus/SOURCES.md
SKILL.md` is empty). The frozen instruments were not amended.

## Before → after measurements

**C1 — depth.** Counting command (frozen, sha256 `6e826f3bf8d4585340ddcc9b7a546e4b7d8b9774a2794c4f45b3cf13e7798922`):

```
python3 -B verifiers/check_omp_root_semantics.py --rev <rev>
```

| | value | revision | receipt |
|---|---|---|---|
| before | `omp root semantics grounded 0 of 12`, `guard S3 pattern-set FAIL`, `exit=1` | `223ae62424f8ab1eb365d733eb648d6228ddd7e8` | `.ufo/waves/round-87/w3/l1/base-both.txt` |
| after (attempt 1) | `12 of 12`, `exit=0` | `e03f9e226b51b8cb94f2dc5c7c3027c5286b004b` | `.ufo/waves/round-87/receipts/c1-after.txt` |
| after (this attempt) | `12 of 12`, `exit=0`, S1–S3 PASS | `760e1c5e` (start), `3c8902a7`, and `49b7d1b4` (the settlement tip; the receipt is committed at `74048151`) | `.ufo/waves/round-87/w3/l1/c1-tip.txt`, `counters-at-3c8902a7.txt`, `counters-at-final-tip.txt` |

**Honest bound (Q71/Q74, measured this attempt):** the number is reachable by a mechanical world. Four
forged ledgers each read `12 of 12`, `exit=0` (`w3/CriticSemanticsR87/forgery-worlds.txt`), and
conjunct 4 is dead at scoring (`w3/SentinelEvidenceR87.md` F-1). So C1's evidence is not the count: it
is the byte-level attribution of all twelve quotes to their own module chunks
(`w3/CriticSemanticsR87/attribution.txt`), S256's byte-identical upstream pin
(`w3/ScoutSourceS256R87/02-fetch.txt`), the independent re-implementation (`w3/ReviewC1R87.md`) and
the live probe for the bound (`w3/ExecProbeBoundR87.md`). The counter is also 12 of an **18-root**
surface: six further joins exist that no ledger carries (`w3/ScoutPatternsR87/three-way-table.md`), so
the round moves depth on a 12-row object, and the coverage hole is routed.

**C2 — consistency.** Counting command (frozen, sha256 `26daaa137136f25b098fc2c3ff8c126114a2537c0a77557ceed8c22561b4ee9a`):

```
python3 -B verifiers/check_r86_routed_repairs.py --rev <rev>
```

| | value | revision | receipt |
|---|---|---|---|
| before | `0 of 5` (pre-addendum counter, sha `a2455a22…`; the frozen counter refuses the base, `exit=2`) | `223ae62424f8ab1eb365d733eb648d6228ddd7e8` | `.ufo/waves/round-87/w1/ExecRepairs/base.txt`; the refusal is re-measured in `.ufo/waves/round-87/w3/l1/c2-base-clone.txt` |
| after (attempt 1) | `5 of 5`, `exit=0` | `35a395a9aabfe2c849628bb4cfe9b25f176de411` | `.ufo/waves/round-87/receipts/c2-final.txt` |
| at the tip (this attempt) | **`4 of 5`**, `exit=1` — D1–D4 PASS, D5(i)/(ii)/(iv) PASS, D5(iii) FAIL | `760e1c5e`, `3c8902a7` and `49b7d1b4` (same reading at all three) | `.ufo/waves/round-87/w3/l1/q79-control.txt`, `counters-at-3c8902a7.txt`, `counters-at-final-tip.txt`; `w3/ExecTipR87/SUMMARY.json` |
| re-run at `35a395a9` | `could-not-evaluate` (D5(iii)'s tip pin) | `35a395a9aabfe2c849628bb4cfe9b25f176de411` | `w3/ReviewD1D5R87.md` |

The tip reading is recorded, not re-worded: the frozen acceptance is 5 of 5, C2 is **4 of 5 at the
tip**, and the miss is the healed external DRIFT (`.ufo/reports/round-84/kama.md` landed at 22:47),
which Q79 now names as an instrument defect rather than a corpus regression. The same bytes in a
relocated clone read two reds but a different detail site, so the conjunct is path-dependent too.

The lane tip advanced twice inside the wave (760e1c5e → d1c03183 → 3c8902a7); the counters were
re-read at the final tip, and any reading that names `760e1c5e` as "the tip" in an earlier receipt is
stale by design (`w3/l1/counters-at-3c8902a7.txt`).

**No harm (measured at `d1c03183`, re-read at `49b7d1b4` and `74048151`).** `verify_corpus_integrity.py` `8/9` — up from the round's `7/9`,
the only red being the carried `commit_unresolvable` (`corpus/lessons/round-81.md:8`); the `report_dead`
DRIFT is gone, not carried. `check_gate_registry.py` `69 of 69`, phantom 0;
`check_correction_sweep.py` `exit=0`; `check_assertion_floors.py` all rows PASS (`exit=0`, standalone
run after the battery's 280 s harness timeout, `.ufo/waves/round-87/w3/l1/floors-standalone.txt`);
`verify_skill_checklist.py`, `verify_corpus_independent.py` red only on the carried
`citation_resolves`/`commit_unresolvable` reds, both present at base; `SKILL.md` untouched
(`600 of 600` lines). Battery receipt: `.ufo/waves/round-87/w3/l1/battery-at-d1c03183.txt`.

## Sources & frontier

- **Census** (frozen command `bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate
  --root /home/vgpnk/Projects/shokunin kotoba`): **before** (attempt 1, base) `exit=0`, 33 `W04`, 0 `E`
  rows (`receipts/base-battery.txt`); **after** (this attempt, lane tip) `exit=0`, 33 `W04`, 0 `E` rows,
  last line `kotoba ok …/corpus/SOURCES.md` (`.ufo/waves/round-87/w3/l1/census-now.txt`).
- **Rows before → after:** 182 → 182 this attempt (181 → 182 in attempt 1, when S256 was added);
  `grep -cE '^ {0,3}\| S[0-9]{3}' corpus/SOURCES.md` → `182`. **Added by tier:** 0 this attempt
  (attempt 1 added 1 × tier A, `S256`). **Rows touched old→new:** 0. **Frontier rows advanced:** the
  loader-rule row (S256 re-opened and re-verified byte-identical at the pin); the coverage map is
  unchanged because no new knowledge entry landed this attempt.
- **Assimilation: none**, with the corrected reason — `/home/vgpnk/Projects/shokuknow/merge/kotoba/`
  **exists** (188 staged rows, 88 entries, mtime 2026-10-24 23:33) but the freeze's touch list admits
  one `SOURCES.md` row, and the staged id space collides with the lane's at `S256`; adoption is
  routed to r88 with an id-collision run first (`w3/ConnectOverlapR87.md`).
- **`considerthese`** — mined in attempt 1 (`considerthese/2026-10-26.md` proposal 1 → Q78); nothing new
  this attempt.

## Trend verdicts

- **expansion — `unchanged`.** No new source row and no new knowledge entry this attempt; the census
  holds at 182 rows and the S256 row was re-opened, not extended.
- **quality — `improved`.** The bound rule is now observed on the real client instead of inferred
  (`w3/ExecProbeBoundR87.md`), a new verification capability enters the table, and two instrument
  defects are named with executable evidence (the non-monotone, path-dependent D5(iii) via Q79 and the
  dead conjunct 4 via `w3/SentinelEvidenceR87.md`).
- **discernment — `improved`.** Two attack seats falsified things the round had accepted: four forged
  ledgers reach C1's target, and C2's 5 of 5 is no longer re-derivable at the tip. The round records
  both, refuses the laundering and amendment routes in `## Gate — attempt 2`, and routes the repairs
  with their measured shapes.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — evidence: the two attempt-1 gate-registry rows (`69 of 69` conformant at `3c8902a7`, `python3 -B verifiers/check_gate_registry.py --rev 3c8902a7`), `corpus/knowledge/omp-root-semantics-round87.md`, and this attempt's `w3/CriticSemanticsR87.md` § 1–2 which verifies both the quotes and the module attribution byte-wise.
- [~] At least one end-to-end domain task executed and logged in LOG.md — evidence: `LOG.md` § Round 87 attempt 2 (the 12-seat verification of both claims); receipts under `.ufo/waves/round-87/w3/`, including the live client probe (`w3/ExecProbeBoundR87.md`).
- [~] Instructions executable by an agent without oral context — evidence: `w3/ExecProbeBoundR87.md` § Verdict carries the exact `env -i` command and the deciding output; `w3/MutateR87.md` and `w3/q79_location_control.py` are re-runnable from the record. No fresh non-author cold run of the whole lesson exists.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — evidence: `PROVINCE.md` untouched this round (`git diff --stat 760e1c5e 3c8902a7 -- PROVINCE.md` empty); `w3/ConnectOverlapR87.md` finds no sibling corpus holding the loader semantics; `check_province_core.py` reads `province core rows 0 of 2` with `§ Frontier differs from the base` at base and tip (a carried red).

**Round shape.** Two dispatches, both v1 waves under `scripts/hyaku/ufo-wave-policy.json` (band 8–16).
Attempt 1: `r87-w1`, **14 seats** (scout 2, executor 4, scribe 3, connector 1, reviewer 1, critic 1,
mutation-tester 1, sentinel 1), attack set 4 of 14 = 28.6 %; `Critic-3` and `ExecRepairs-3` died on a
provider 401 at wake. This attempt: `r87-w3`, **12 seats** (scout 2, executor 3, reviewer 2, critic 1,
mutation-tester 1, sentinel 1, scribe 1, connector 1), attack set 4 of 12 = 33.3 %, connectors 1
(≤ 2), residual `task` call none. The §3 planner seat is the L1's (the validator's `SWARM_ROLES`
excludes `planner`; the planning data-walk rode the two scouts and the connector). Round total across
both attempts **26 seats**. Dead seats in `r87-w3`: **none** — 12 of 12 seats returned output and each wrote its report file (`r87-w3-results.json`, 12 rows, every output non-empty).

**Misroot sweep.** `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows
`.scratch/run15-state.json` (orchestrator-owned), `.ufo/reports/round-86/kama.md` (another lane's
untracked report) and an empty `mo.tip` at the fleet root; no file names this lane or round, so
nothing was copied or deleted.

**Stale-lane.** One mission for this lane, no respawn: the round is the lane's only open mission;
this attempt is the third instance the driver launched for it after two provider-failure cycles.

**Carried reds (not this round's harm).** `verify_corpus_integrity.py` `commit_unresolvable 1`
(`corpus/lessons/round-81.md:8`); `verify_skill_checklist.py` `governance.citation_resolves` FAIL
(base and tip); `check_province_core.py` `province core rows 0 of 2` with `§ Frontier differs from the
base` (base and tip).

**Tool installs.** None (no `pacman` transaction; no `uv tool`/`npx` install).

**Open L0 questions.** Two appended to `.ufo/l0-questions.md`: whether r88 may adopt the staged
`merge/kotoba/` package under its own freeze with a committed id-collision run (the package's ids
collide at `S256`), and whether D5(iii) should be stated monotonically in a new r88 counter rather than
amended post-data.
