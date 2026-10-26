# kengaku — round 37 report (hyaku run 8, 2026-10-26)

Lane `/home/vgpnk/Projects/shokunin/kengaku-shokunin`, branch `master`. Baseline `3ea9a1d9005cc07d0a5ce69f4ebf53a81fbcecdd`;
frozen claims `plans/round-37-claims.md` (freeze `ca790460e9b74d4dc5870c878affd13cc9c4437a`); final lane hash
`dc90676b0a01bcb278dba3b5231b504fe2a9ff03` (`git ls-remote origin refs/heads/master` → that hash). L1 agent id `KengakuR37`;
the L1 holds the canonical planner seat (the wave validator rejects `planner`).

## Work performed

Declared claims (2), frozen with red controls before any battery fixture beyond a one-fixture API example and before the
first recorded probe run:

- **C1 — calibration (owned, 8):** the number of defect classes `plans/pkg_gate.py` advertises (its docstring,
  `corpus/QUALITY.md` Q24, the SCORECARD capability row `package-gate`) that no fixture demonstrates, measured by 55 frozen
  one-branch silence mutants in `plans/round37_c1_verify.py`. The gate itself is unedited (digest `ea638822…` at freeze and tip).
- **C2 — coverage (lowest non-retired axis, 7, tied with novelty; frozen tie-break):** the pinned Terminal-Bench 2.0
  `configure-git-webserver` grader admitted as `corpus/knowledge/tb2-git-webserver-grader.md` with an executed 22-case
  bubblewrap-sandbox probe (`plans/git_webserver_probe.py`), rows S111–S113 plus S114, a prior report from upstream.

Work items:

- Protocol load: the round prompt, `skill://shokunin`, `skill://swarm`, `skill://godspeed`, AXES/LEARNING, SCORECARD
  `### Planned (round 37)` (`SCORECARD.md:1231-1240` at baseline), and the round-36 non-author spot-check
  (`corpus/lessons/round-36-verifier-spotcheck.md` §5). Its routed items became the claims: item 1 became the frontier
  mistake, item 2 became C1, and item 3 became C2's V2/V7.
- Freeze `ca790460`: claims, both counters, the probe and its frozen case table
  (`corpus/evidence/round37/git-webserver-dry-cases-freeze.txt`, `cases=22 predicted_pass=9 predicted_fail=13`), six captures
  with `SHA256SUMS`, and controls in `.ufo/waves/round-37/claims/`. C1 nothing: `killed=5 survived=50`, fail. Gate edited:
  `invalid=55`. Mislabel: `wrong=1`. Example: `killed=6`. C2 nothing: `checks=7 defects=4`. C2 junk skip-control: `defects=1`,
  red on V2. Also frozen: `frozen-digests.txt`, census-before (exit 0, 15 W04). Disclosed in the claims (`:3-10`): the
  skip-control's gate P10 ran the frozen probe once at control time and threw the output away unread.
- First recorded probe run `5c7b34e9`: `cases=22 observed_pass=9 observed_fail=13 mismatches=0`; a second run was byte-equal.
- Wave 1 (spec/dispatch `44b7298a`, 40 seats): 40 reports, 0 dead (`.ufo/waves/round-37/build-results.json`; committed
  `67cbe7a4`).
- C1 battery (`a3163e67`): nine executor seats wrote `plans/battery37/` (9 modules, 50 single-defect fixtures). A reviewer
  priced all 55 mutants as killable, 0 equivalent (`build/R37RevMutants.md`). On a clean clone of `5c7d5d75`:
  `BATTERY fixtures=64 wrong=0 renamed_disagree=0`, `MUTANTS total=55 killed=55 survived=0 invalid=0 null_detected=0`,
  `PREDICATE C1 pass` (`integrate/measure-final.txt`).
- C1 limit found in wave 1: `build/R37CritC1Battery.md` showed the frozen counter is **gameable**. A two-module hostile
  battery whose `--rerun` probe detects the running gate copy reaches the same pass line. The L1 added a post-hoc audit,
  `plans/round37_c1_attribution.py` (`357deceb`). It finds the landed battery **55/55 attributed**
  (`integrate/c1-attribution.txt`). The hostile battery, under a frozen `PREDICATE C1 pass`, gets only `ATTRIBUTED 6/55
  UNATTRIBUTED=49` (`integrate/c1-attribution-hostile.txt`). This audit is not the frozen rule.
- C2 package (`c138da2b`): R37PkgDraft drafted the entry, rows and README additions. The L1 integrated them with the scope
  critic's fixes F1–F5, F7, F8, F9, F10, F12 (`build/R37CritScope/dropins.md`), the case-independence limits
  (`build/R37CritCases.md` §2) and the prior-art section for S114. Results: `checks=7 defects=0`, `PREDICATE C2 pass` at
  `5c7d5d75`. An independent re-implementation agreed 22/22 plus 3/3 extra cases (`build/R37IndepVerdicts.md`). The probe is
  deterministic, including the gate's uv path (`build/R37ProbeRerun.md`). The pins were re-opened 6/6 identical, with no
  drift on `main` (`build/R37ReopenPins.md`). The mutation tester caught 14/14 counter mutants (`build/R37MutC2Counter.md`).
- C2 limits found in wave 1: the counter admits an informed filler package, and its spec template is not digest-pinned by
  the counter (`build/R37CritC2Counter.md` v1, v4; `build/R37RevC2Counter.md` F1–F14). At the tip,
  `plans/pkg-spec-r37.json` equals its freeze digest `4c61d103…` (`measure-final.txt`). In the sandbox the git step never
  executes, and four case labels are weaker than they read (`R37CritCases`).
- Routed, not absorbed: `build/R37DockerOracle.md` ran the task's real image. The oracle passed, a static file passed and a
  `TEST PASSED` body passed, all with `reward.txt = 1`. Running the task image is outside PROVINCE's admitted instrument
  (`R37CritScope` F13).
- Frontier mistake (round-36 routed item 1, S110 digest with 63 hex): `plans/anchor_digest_check.py` from R37AnchorSweep.
  At the baseline it reports `defects=5`: S110 plus S070/S072/S073/S074, which are true digests with no committed bytes
  behind them. At the tip it reports `rows=107 tokens=15 defects=0`, after the S110 erratum line
  (`corpus/lessons/round-37.md` §Gate) and the byte captures in `corpus/evidence/round37/anchor-captures/`. New criteria
  Q26 and Q27 in `corpus/QUALITY.md`.
- Assimilation: `considerthese/2026-10-25.md` proposal 2(a) landed as `plans/ledger_tip.py`. At the tip it reports
  `rows=9 closed=9 observed_pass=9 mismatches=0`; 2(b) and 2(c) are not built. The `merge/kengaku/` re-screen gave 0 admit,
  3 hold, 7 refuse (`build/R37ScoutMergePkg.md`). No package row was appended. The staged ids S111–S113 collide with
  package rows, which is moot because only the lane's own rows were added.
- Docs: SKILL registry rows plus a service-class section (rewritten as observations, per F12); PROVINCE round-37 paragraph
  plus correction R37-P1; `tb2-regex-log-grader.md` §Errata (round 37) from `R37R36Absorb`; SCORECARD round-37 section with
  two capability rows; LOG entry; lesson `corpus/lessons/round-37.md`.
- No-harm: the pre-landing sweep was green 25/25 (`build/R37TipSweep.md`). At the tip, the round-36 C1/C2 counters still
  pass, census exit 0, and the frozen digests are unchanged (`measure-final.txt`).
- Wave 2 (falsify, 37 seats, `falsify-dispatch.json` validated against `357deceb`, ready marker `dc90676b`) was handed to
  the dispatcher after WAVE-DONE build. **I filed this report before WAVE-DONE falsify**, because the operator's request
  budget forced the round to close. No wave-2 finding is integrated, and the closure should read
  `.ufo/waves/round-37/falsify/*.md`.
- Misroot sweep: no fleet-root untracked file names kengaku round 37
  (`git -C /home/vgpnk/Projects/shokunin status --porcelain --untracked-files=all | grep -iE 'r37|round-37|R37|F37'` → only
  `kengaku-shokunin/`, which appears because the fleet `.gitignore` is deleted in the working tree). Six fleet-root tracked
  files show as deleted by another writer: `.gitignore`, `AGENTS.md`, `LOG.md`, `README.md`, `SCORECARD.md`,
  `.ufo/reports/round-1/kaidoku.md`. I did not touch them and reported them to Main.

Round shape: two v1 waves. Wave 1 has 40 seats: 16 executor, 8 scribe, 4 critic, 4 reviewer, 3 scout, 3 connector,
2 mutation-tester; m_flash roles 28/40, attack 10/40, 0 dead. Wave 2 has 37 seats: 16 critic, 8 reviewer, 6 executor,
4 mutation-tester, 2 connector, 1 scout; m_flash roles 22/37, attack 28/37; outcome not integrated. The round total is
77 seats, with no residual call.

Stale-lane: respawn-per-round driver, no other mission of this lane open.

Tool installs: none new. biopython 1.85 is used ephemerally via `uv run --with` for the gate's P10 (PyPI, uv cache).
bubblewrap 0.13.1 was already installed. One wave-1 seat pulled and removed the Docker image
`alexgshaw/configure-git-webserver:20251031`, leaving 0 B retained. pacman was not touched.

## Landed changes

| commit | what | LOG.md |
|---|---|---|
| `ca790460` | freeze: claims, C1/C2 counters, probe, captures, controls | round 37 entry ¶1 |
| `5c7b34e9` | first recorded probe receipt | ¶1, C2 bullet |
| `44b7298a` | wave-1 spec and dispatch | ¶1 |
| `a3163e67` | `plans/battery37/` (50 fixtures), working-tree C1 run | C1 bullet |
| `c138da2b` | C2 entry, S111–S114, README; anchor check, captures and S110 erratum; `ledger_tip.py`; Q26/Q27; SKILL; PROVINCE; regex-log errata; lesson | C2, Frontier and Assimilation bullets |
| `5c7d5d75` | SCORECARD and LOG round-37 sections, capability rows | entry |
| `aa3d6ead` | landing measurement `integrate/measure-final.txt` | Re-verification bullet |
| `188a2658`, `2a844a0d` | wave-2 spec and dispatch | — |
| `357deceb` | post-hoc C1 attribution audit, C1 limit recorded | SCORECARD round-37 limits |
| `67cbe7a4` | wave-1 reports and results | — |
| `dc90676b` | lesson close, wave-2 ready marker | — |

## Before → after measurements

- **C1 (calibration)** — `python3 plans/round37_c1_verify.py --lane .` on a clean clone.
  - Before, at freeze (`claims/control-c1-nothing.txt`, and on committed `44b7298a` in `claims/measure-before-committed.txt`):
    `BATTERY fixtures=14 wrong=0 renamed_disagree=0`, `MUTANTS total=55 killed=5 survived=50 invalid=0 null_detected=0`,
    `PREDICATE C1 fail`, exit 1.
  - After, at `5c7d5d75` (`integrate/measure-final.txt`): `BATTERY fixtures=64 wrong=0 renamed_disagree=0`,
    `MUTANTS total=55 killed=55 survived=0 invalid=0 null_detected=0`, `PREDICATE C1 pass`, exit 0.
  - Verdict: **frozen predicate met**, mismatch count 50 → 0. Score **8 → 8 held**: the counter alone is gameable, so the
    landing rests on the attribution audit (55/55).
- **C2 (coverage)** — `python3 plans/round37_c2_verify.py --lane .` on a clean clone.
  - Before (`claims/control-c2-nothing.txt`): `checks=7 defects=4`, exit 1.
  - After, at `5c7d5d75`: `checks=7 defects=0`, `PREDICATE C2 pass`, exit 0. Probe: `cases=22 observed_pass=9
    observed_fail=13 mismatches=0`.
  - Verdict: **frozen predicate met**. Score **7 → 7 held**, capped by the L0 question. The counter has documented
    false-green paths, so admission also rests on the wave-1 non-author-model re-reads and is pending the wave-2 re-reads.
- **Frontier:** `python3 plans/anchor_digest_check.py --lane .` gives `defects=5` at `3ea9a1d9` (AnchorSweep F0) → `rows=107
  tokens=15 defects=0` at `5c7d5d75`.

## Sources & frontier

- Counting command: `grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` gives 103 → 107. Tier A +3
  (S111, S112, S113: pinned configure-git-webserver files) and tier B +1 (S114, TB2.1 issue #133), all `mined`, all used by
  the new entry.
- Rows touched old→new: none rewritten. S110's digest is corrected by an appended erratum line, not by an edit.
- Census `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kengaku`:
  before exit 0 with 15 W04 (`claims/census-before.txt`). After, by the `--file` form on a clean clone of `5c7d5d75`: exit 0,
  15 W04, no new duplicate (`measure-final.txt`).
- Frontier advanced: the README §Frontier TB2 clause was narrowed for one more task (3 of 89 read), with one new executed
  edge class: a live HTTP service as the graded state.
- Sourced claim: C2 (S111–S114, opened 2026-10-26).
- Mined mistake: S110 anchor digest (lesson §Mistakes row 1). Its fix was shown able to fail (baseline `defects=5`).
- Assimilation: considerthese proposal 2(a) mined (`plans/ledger_tip.py`). `merge/kengaku`: adopted nothing.

## Trend verdicts

- **expansion — improved.** One admitted entry covers ground that the coverage map held as Frontier: a third TB2 grader, the
  first whose graded state is a live service. Four `mined` rows; two capability rows entered with demonstrations
  (`gate-mutation-harness`, `service-grader-probe`). This is one instance and one edge class, not breadth.
- **quality — improved.** Stale or false items were marked and re-verified rather than left. The S110 digest erratum is in
  place. Four true-but-unsupported digests now have committed captures. `tb2-regex-log-grader.md` gained errata for four
  mis-anchored `What decides it` cells and two non-independent rows. The round-36 spot-check's own off-by-one is recorded.
  No admitted entry failed its re-check at the tip: the round-36 C2 counter still passes. Caveat: the wave-2 re-reads were
  not integrated.
- **discernment — improved.** Last round's outside spot-check disagreement (the S110 digest) and its routed items 2 and 3
  became lesson rows. They are backed by grounded criteria: Q26 (anchor digests resolve to committed bytes) and Q27 (a gate
  class is held only when a fixture kills its silence mutant). This round's own counter weaknesses are recorded as lesson
  rows instead of being hidden. Discernment still needs the round-37 non-author closure.

## Open L0 questions

No new line was filed. Still open: `kengaku | round-25` (coverage cap, novelty conversion) and `kengaku | round-33` (the
decision packet for the coverage cap). Both are routed around: coverage is held at 7.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md` §Service-class TB2 grader — round 37 (decision table), registry rows for git-webserver-probe / round37-c1-mutants / round37-c2 / anchor-digest-check / ledger-tip
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md` round 37 entry; `corpus/evidence/round37/git-webserver-probe.txt` (22 cases, byte-equal re-run)
- [~] Instructions executable by an agent without oral context — `.ufo/waves/round-37/integrate/measure.sh` re-runs every claim counter from a clean clone
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` §Round37 partial frontier admission; real-image run routed out (`build/R37CritScope.md` F13)
