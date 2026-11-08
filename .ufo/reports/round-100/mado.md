# mado round 100 — the unset-PATH default branch as a measured case class (coverage), the harm watch's per-leg cap measured (operability)

- Lane: `mado`, repo `/home/vgpnk/Projects/shokunin/mado-shokunin`, branch `master`
- Round: 100 (hyaku run 15, attempt 1) · base `43309e6af9a3b57f1bc839a826bef1f8eb7495e4`
- L1: `MadoR100` · declaration `.ufo/waves/round-100/claims-declaration-r100.md` · frozen claims `.ufo/waves/round-100/claims.json`
- Round shape: ONE v1 wave `w1` of **16 seats** (2 scouts, 6 executors, 1 scribe, 2 reviewers, 1 critic, 2 mutation-testers, 1 connector; attack roles 5/16 = 31 %), no residual call, no dead seats, round total 16. The planner seat is the L1 (the validator freezes `planner` as a non-swarm role); the bounded planning data-walk rode the two scouts and the connector.

## Work performed

**Declared claims (2, distinct axes, causally separable).**
- **C1 — coverage:** the PATH-unset default branch of `g_find_program_for_path` (`gutils.c:376-389`,
  the literal `/bin:/usr/bin:.`) becomes a **measured** case class instead of a modelled constant.
  Frozen predicate `PRED-C1-r100-v1`.
- **C2 — operability:** the harm watch's per-leg cap becomes **measured** (per-leg elapsed becomes a
  gate output; the panel cap is re-frozen from the lane's own timing pass). Frozen predicate
  `PRED-C2-r100-v1`.

**Work items (each with its evidence pointer).**

- **C1 case class built and measured.** `.ufo/waves/round-100/controls/launchenv-cases-r100.json`
  (77 cases / 35 classes; **10 new `path-default-*` cases in 4 classes**, every label measured twice
  against `/usr/bin/gio` `d2164260…cfc462`, agreeing) — `receipts/c1-cases-r100.txt`,
  `receipts/c1-cases-remeasure-r100.txt`. The class separates the unset default from an empty `PATH`
  (argv0 `{root}/./probe` against `{root}/probe`), from a case-private `PATH` (`load` refusal against
  a launch) and carries `TryExec` as the system-directory arm (`pd-dot-root`, `pd-empty-root`,
  `pd-private-unset`, `pd-private-onpath`, `pd-sysbin-unset`, `pd-sysbin-empty`, `pd-wd-unset`).
- **C1 candidate extended.** `tools/mado-launchenv.py` keeps its CLI and model and gains five
  branch checks in `--selftest` (`MADO_LAUNCHENV_SELFTEST: checks=95 failed=0`) —
  `receipts/c1-tool-r100.txt`.
- **C1 counter.** `quality/counters/c1-r100-launchenv-path.py` (seven conjuncts, six anchored
  mutants, seeded fresh generator, the `unset-as-empty` control, `--selftest` 9/9). It carries one
  contract correction the wave found before the counter existed: a `path: null` case is scored with
  `PATH` **absent** from the candidate's environment, not `PATH=""` (`w1/R100MMutPath.md` finding 1).
  Receipt `receipts/c1-measured-r100.txt`; base refusal `receipts/c1-at-base-r100.txt`.
- **C1 mutation matrix.** `.ufo/waves/round-100/controls/launchenv-mutants-r100-probe.txt`: six
  mutants of the program lookup, each killed by at least one case; **`m1` (default without its
  trailing `.`) and `m2` (unset read as empty) survive the round-99 case set alone** — the measured
  proof that the class is load-bearing (`w1/R100MMutPath.md`).
- **C1 ground re-measured independently.** `w1/R100MLabratUnset.md` (H1 not falsified over 7
  hand-built cases plus 7 oracle repeats) and `w1/R100MScoutPath.md` (branch-by-branch read of
  `tools/mado-launchenv.py`, the oracle's `path_string`, and the three files' predicates).
- **C2 gate.** `quality/harm-watch.py` prints `elapsed_ms` on every `LEG` line and per leg in
  `--json` (setup, spawn-failed and timeout legs included), `--selftest` **33/33** —
  `receipts/c2-gate-r100.txt`. A defect the mutation seat found in the round's own first draft was
  fixed during integration: the timeout-elapsed check substring-matched `"elapsed_ms=1"`, so a leg
  reporting `elapsed_ms=10` passed it (mutant `h3b`, `w1/R100MMutHarm.md`); it now parses the value
  and requires `>= 1000`, and `h3b` dies with two selftest failures.
- **C2 timing pass.** `receipts/panel-timing-r100.txt`: all 28 legs timed individually under a
  pinned `--timeout 7200`, worst `r92_gate_defects` at **708,014 ms** (one leg above the old 600 s
  cap; round 99 measured two), whole loop 2,810 s at load average 249-260 on 32 cores.
- **C2 re-frozen panel.** `.ufo/waves/round-100/controls/harm-panel-r100.json`: `timeout_s` 600 →
  **3600** (2.5× the measured worst leg), the 28 leg rows byte-identical to the round-99 panel
  (parsed row comparison, `receipts/c2-gate-r100.txt`).
- **C2 counter.** `quality/counters/c2-r100-harm-watch.py` (nine conjuncts; parses the timing
  receipt and requires its `TIMING-DONE` marker; derives `max_elapsed_ms` and the 600 s control;
  runs the gate's selftest and the full panel; prints the gate's own leg lines) — `--selftest` 9/9.
  Receipts: `receipts/c2-measured-run1-r100.txt`, `receipts/c2-measured-r100.txt`,
  `receipts/c2-leg-r97c1-standalone-r100.txt`, `receipts/c2-control-no-done-r100.txt`.
- **Reconnaissance (read-only).** `w1/R100MScoutHarm.md` (the gate's timing surface, the output
  contract, its consumers, and that the round-99 counter reads the gate from `--rev` so it is not
  harmed by the change), `w1/R100MScoutPath.md`.
- **Attacks.** `w1/R100MReviewC1.md` (`falsifies-wording` + `falsifies-number`), `w1/R100MReviewC2.md`
  (six neutral items, four residual risks), `w1/R100MCriticClaims.md` (seven C1 narrowings, six C2
  narrowings), `w1/R100MMutHarm.md` (the 3-column gate/counter/panel mutant matrix and the survivors),
  `w1/R100MConnector.md` (sibling sweep + assimilation sweep + the considerthese grounding).
- **Record repairs routed by the round-99 spot-check.** 6.1 the off-by-one `find_program` pointer
  corrected append-only in `corpus/lessons/round-99.md` (`## Errata`) and `corpus/QUALITY.md`
  (172a); 6.2 the attack share is stated as attack roles only (5/16 = 31 %); 6.3 the C2 cap repair
  is this round's C2; 6.4 the C1 A8 residual is this round's C1; 6.5 every measured line lands with
  its receipt in the same commit.
- **Considerthese.** `considerthese/2026-11-07.md` proposal 3 mined into `corpus/QUALITY.md`
  criterion **173** (a library-semantics re-implementation carries an exhaustive small-domain sweep
  against the shipped library), grounded on `corpus/lessons/round-95.md` M95-1 — the pointer was
  re-opened and resolves (`w1/R100MConnector.md` §3.2).
- **Pre-file falsification ledger.** `.ufo/waves/round-100/claim-falsification.tsv` (9 rows, every
  attack seat read) and the gate run, reported at the end of this section:

  `PREFILE-FALSIFICATION: pass claims=2 rows=9 attack_seats=6 findings=0` (exit 0;
  `python3 scripts/hyaku/prefile-falsification.py --lane mado --round 100`)

**Pre-file amendments (recorded in `plans/round-100.md`, each naming its forcing artifact).**
A1 the three prose separations are not conjuncts and separation 3 was false as worded (an empty
`PATH` also finds the working-directory program; the difference is the argv0 shape) — narrowed,
and entry *order* declared unobservable. A2 the before-state locator named a range that does not
hold the literal (`:388` in `:376-389`). A3 the numeric conjuncts count labels, not reachability —
the filed sentence says so and moves the causal claim to the measured mutant matrix. A4
`base_set_default_cases == 0` is a label count; the before-state rests on the r99 cases' absolute
`Exec` bytes. A5 the round's surface is the branch **as exercised by frozen cases** (it was already
modelled at base by `tools/mado-mime.py:466`). B1 `elapsed_ms` is a printed field whose truth the
selftest carries (mutant `h2` — a wall clock — survives every lane instrument and is named as a
limit). B2 the cap is relative to the timing receipt's values, whose own cap (`--timeout 7200`) and
revision are pinned in its header; no upper bound. B3 the 600 s control is a derivation and the panel
is "of this census shape". B4 "committed bytes" is `--rev` `ae537dbe…`, pins re-derived there. B5 one
run is an event, not durability.

## Landed changes

Every row is a commit on `master` by the lane helper (`landed <hash>` lines).

| commit | what | LOG.md entry |
|---|---|---|
| `219e14f4a89075005b3c4dfa87651356b1e9719c` | the plan and the frozen declaration, the C1 case file / fresh generator / mutants, `tools/mado-launchenv.py` (five branch selftest checks), `quality/harm-watch.py` (`elapsed_ms`), both round-100 counters, the wave controls and receipts, and the round-99 record errata | round-100 C1/C2 bullets |
| `f94f7a9453bb91fc4a0356c2d5b079e70254dc19` | the record layer: `corpus/knowledge/gio-launch-path-default-r100.md`, `corpus/lessons/round-100.md`, `corpus/QUALITY.md` 173, the `corpus/README.md` coverage row and frontier bullet, S533's `used-by`; and the harm-watch timeout check now **parses** its value (kills mutant `h3b`) | round-100 "a defect the round found" bullet |
| `18bce79049ed99d895fc9a327b7fa36b479065c7` | the tool-ledger rows for the two new counters (the ledger gate flagged `uncovered=2`) | round-100 frontier bullet |
| `ae537dbe361e0d10247dbdd822bdb22fbc41464d` | the C2 counter prints the gate's own leg lines and summary (a receipt that hides which leg failed is not evidence); `SKILL.md` round-100 registry prose; the LOG entry | round-100 C2 bullet |
| `d73a0648540e735ddcd457f84b0d450d39b11e64` | the C2 counter keeps the panel scratch at one short level under the caller's root and warns on depth (the measured cause of runs 1-2) | round-100 "a defect the round found" bullet |
| `f791d3c0536cfb3c842cc4df61cff4ba35e39b76` | the round record: the SCORECARD row, the LOG entry, the frozen claims with their measured values, the falsification ledger and every round receipt plus the wave results | round-100 (all bullets) |
| `37913833a278837f9b892944ba4be95e5ef9a04a` | the pre-file amendments A1-A5 / B1-B5 in `plans/round-100.md` and the wave build drafts (the seats' counters and scribe drafts) as wave evidence | round-100 amendments bullet |

Lane tip at filing: **`37913833a278837f9b892944ba4be95e5ef9a04a`**, equal to
`git ls-remote origin refs/heads/master` (the pre-report gate).

## Before → after measurements

**C1 — coverage.** Counting command (frozen verbatim in `.ufo/waves/round-100/claims.json`):

```
python3 -I quality/counters/c1-r100-launchenv-path.py --repo . --rev 219e14f4a89075005b3c4dfa87651356b1e9719c \
  --base-rev 43309e6af9a3b57f1bc839a826bef1f8eb7495e4 \
  --cases .ufo/waves/round-100/controls/launchenv-cases-r100.json --expect-cases-sha256 7aba8a0f…df4a9 \
  --mutants .ufo/waves/round-100/controls/launchenv-mutants-r100.json --expect-mutants-sha256 4f6667be…698d7 \
  --genseed .ufo/waves/round-100/controls/launchenv-fresh-r100.py --expect-genseed-sha256 18005e07…fc6b \
  --expect-tool-sha256 3b29dc65…fb228 --expect-execargv-sha256 49f7fecd…f713 \
  --expect-gio-sha256 d2164260…cfc462 --scratch-root DIR
```

- **Before** (`43309e6a`): the branch is modelled; **0** frozen cases reach it — the r99 file's two
  `path-unset` cases give `Exec = {root}/probe.sh` (absolute) and return at `gutils.c:332-357`
  before the PATH source is read. Measured: `receipts/c1-at-base-r100.txt` (the counter refuses:
  `SETUP_ERROR tool sha256 a63c20c8… != pinned 3b29dc65…`, exit 2; and the r99 file's
  `path-default` label count prints **0**).
- **After** (`219e14f4`): `cases=77 classes=35 default_cases=10 default_classes=4 cases_correct=77/77
  fresh=60/60 (seed drawn at measurement) mutants=6/6 killed control_unset_as_empty=75
  base_set_default_cases=0` → `MADO_C1_R100: TARGET_MET`, exit 0
  (`receipts/c1-measured-r100.txt`). **Verdict: improved.**

**C2 — operability.** Counting command:

```
python3 -I quality/counters/c2-r100-harm-watch.py --repo . --rev ae537dbe361e0d10247dbdd822bdb22fbc41464d \
  --base-rev 43309e6af9a3b57f1bc839a826bef1f8eb7495e4 \
  --panel .ufo/waves/round-100/controls/harm-panel-r100.json --expect-panel-sha256 6d259164…65ac \
  --timing .ufo/waves/round-100/receipts/panel-timing-r100.txt --expect-timing-sha256 e7280b53…1e5d \
  --expect-gate-sha256 acecb0ea…3f1f --scratch-root DIR
```

- **Before** (`43309e6a`): the gate records no per-leg time (`grep -n elapsed quality/harm-watch.py`
  at the base: no hit) and the panel's 600 s cap is exceeded by one leg on this host
  (`r92_gate_defects` 708,014 ms), so `mismatches == 0` was unreachable — round 99's honest stop
  (`receipts/panel-timing-r100.txt` is this round's own measurement of that).
- **After** (`ae537dbe`): eight of nine conjuncts hold — `panel_legs=28`, `legs_run=28`,
  `gate_elapsed_emitted=28/28` (human and `--json`), `timing_legs_timed=28`,
  `max_elapsed_ms=708014 > 600000`, `panel_timeout_s*1000=3600000 >= 2*1416028`,
  `control_600s_would_mismatch=1`, `selftest_failed=0`. **The `mismatches == 0` conjunct is unmet**:
  runs 1 and 2 (deep scratch roots) each recorded one mismatch (`LEG r97c1_filetype rc=2 expect=0`,
  ~2 s), and the cause was then measured: that round-97 leg binds an **AF_UNIX** fixture inside its
  own scratch, and a `sun_path` over 108 bytes makes it fail closed. The same leg standalone is
  green (`receipts/c2-leg-r97c1-standalone-r100.txt`: `rc=0`, 417,819 ms), a direct 28-leg panel run
  through the gate is green (`receipts/c2-panel-direct-r100.txt`: `legs=28 ok=28 mismatch=0`), run 3
  from a shallow scratch root is `TARGET_MET` (`receipts/c2-measured-run3-shortroot-r100.txt`), and
  **run 4 — the committed counter, with the panel scratch kept at one short level under the
  caller's root and a depth warning — holds all nine conjuncts**: `panel_legs=28`, `legs_run=28`,
  `mismatches=0`, `gate_elapsed_emitted=28/28` (human and `--json`), `timing_legs_timed=28`,
  `max_elapsed_ms=708014 > 600000`, `panel_timeout_s*1000=3600000 >= 2*1416028`,
  `control_600s_would_mismatch=1`, `selftest_failed=0` → `MADO_C2_R100: TARGET_MET`, exit 0
  (`receipts/c2-measured-r100.txt`, measured at `d73a0648`). **Verdict: improved**, with runs 1-2
  disclosed and their cause named; the scratch-depth fragility is routed to round 101 (the round-97
  leg should bound its AF_UNIX fixture path, and the panel should refuse a leg path that long).

**C1's sourced claim** rests on S533 re-opened this round (HTTP 200, sha256 `65086c29…3771`, the
literal at `gutils.c:388`).

## Sources & frontier

- Census **before** (round start, 04:35Z):
  `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin mado` → exit **0**,
  `rows=469`, warnings W04/W01 only (duplicate URLs across scopes, expected and declared).
- Census **after** (round end): same command → exit **0**, `rows=469`, same warning set. Row count
  unchanged: this round **adds no row** — S533 already held the scope (`gutils.c:300-500`,
  "the PATH source and its default"), so the entry cites it and S533's `used-by` gains
  `corpus/knowledge/gio-launch-path-default-r100.md` (old → new logged here). Tier-A rows added by
  tier: **0**. Rows touched old → new: **1** (S533 `used-by`).
- Read-back gate at the records tip: `SOURCES_READBACK: rows=469 entries=121 findings=0` (entries
  120 → 121).
- Frontier row advanced: the round-99 bullet's "the unset-PATH default is modelled but no frozen case
  exercises it (A8)" is closed — a new bullet and a coverage-map row were added to `corpus/README.md`.
- **Assimilation:** `Assimilation: none` — the `merge/mado/` sweep (`grep -niE
  'launch|/bin:/usr/bin|PATH default|elapsed|per-leg|spawn'` over `MERGE-REPORT.md` and
  `SOURCES.append.md`, `.ufo/waves/round-100/assimilation/connector-sweep-r100.txt`) returns 9 hits,
  all historical round-6/7 Hyprland dispatcher/waybar/uwsm/idle material; the one `elapsed` hit is
  rejected with reason and flip condition in `corpus/lessons/round-100.md` `## Gate`.
- **considerthese:** `considerthese/2026-11-07.md` proposal 3 landed as `corpus/QUALITY.md` 173.
- **Sourced claim:** C1 (S533, opened and quoted this round).

## Trend verdicts

- **expansion — improved.** One knowledge entry on ground the lane's coverage map did not hold
  (`corpus/knowledge/gio-launch-path-default-r100.md`: the unset-PATH default branch, its argv0
  shapes, the load-time consequence and the named limits), a new capability row demonstrated by a
  receipt (77 cases / 10 on the branch / 6 mutants killed), and a frontier bullet that closes the
  round-99 A8 residual. Evidence: `receipts/c1-measured-r100.txt`, `corpus/README.md` (row + bullet).
- **quality — improved.** The gate now measures its legs (`elapsed_ms`, 33/33 selftest) and its cap
  is derived from a 28-leg timing receipt instead of guessed (708,014 ms → `timeout_s` 3600);
  the round's own first-draft defect was found and closed (`h3b`, `f94f7a94`); the round-99 pointer
  errata are corrected append-only; the ledger/index/readback gates are green at the tips
  (`indexed=121/121`, `uncovered=0`, `findings=0`). The unmet `mismatches == 0` conjunct is reported,
  not prettified.
- **discernment — improved.** The wave's attack seats falsified both claims' wording before filing
  (A1–A5, B1–B5, each naming its artifact), the mutation seat found a selftest that certified its own
  blind spot and a counter environment that modelled the neighbour of the case it scored, and both
  were fixed rather than argued away. The ledger gate's verdict is printed above.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md:2983-2986` registry rows plus the round-100 prose at `:3025-3032`; the lane's own `quality/check-index.py` and `check-tool-ledger.py` are green at `18bce790` (`121/121`, `uncovered=0`); no non-author promotion verdict this round.
- [~] At least one end-to-end domain task executed and logged in LOG.md — the end-to-end task is the launch-path default: a desktop file's load gate and spawn resolved against the installed `gio` over 77 frozen cases plus a 60-case fresh leg (`receipts/c1-measured-r100.txt`), logged in `LOG.md` round 100; no outside-lane verdict.
- [~] Instructions executable by an agent without oral context — the wave's 16 seats rebuilt the cases, the mutants, the counters and the matrices from the declaration and the wave context alone (`w1/*.md`); a dispatched seat is not an outside-lane verifier, so this stays `[~]`.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — every artifact this round is GLib/GIO launch or the lane's own instruments; the connector's sibling sweep found no other lane holding this surface and no absorbed foreign defect (`w1/R100MConnector.md` §1); no outside-lane re-audit of `PROVINCE.md` this round.

## Extras

- **Stale-lane:** respawn-per-round driver; no other mission of this lane is open.
- **Tool installs:** none this round (no `pacman` transaction; the pacman pause was respected).
- **Dead seats:** none (16/16 seats reported; `w1-results.json` per the orchestrator's handoff).
- **Inherited state:** none — `.ufo/waves/round-100/` did not exist at round start (no earlier attempt
  of this round; `.ufo/watchdog.log` shows no `lane-dead-no-report mado round=100`).
- **Misroot sweep:** `git -C /home/vgpnk/Projects/shokunin status --porcelain` at report time —
  the only untracked file this lane wrote at the fleet root is `.ufo/reports/round-100/mado.md`
  (this report); every other entry is orchestrator-owned (`.scratch/`, `.ufo/l0-questions.md`). No
  misroot, nothing copied back, nothing deleted.
