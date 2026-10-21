# kagi — round 27

Commands run from `kagi-shokunin/`. Unprefixed corpus paths are relative to that lane; standalone wave-artifact names resolve under `kagi-shokunin/.ufo/waves/round-27/`.

Authorship: the round's work was done by L1 KagiR26 (session 01a15c83, killed by SIGHUP 2026-10-21 13:10:51 -03 while landing its last commit). This report and the final landing are by its replacement KagiR27-2 (session 3 resume), working from durable lane evidence only.

## Work performed

**Declared claims (`kagi-shokunin/plans/round-27.md`), both on tied-lowest axes (all six at 9; last capability round 25, so no stagnation waiver):**
- **C1 — calibration, 9 → 9:** current-tense numbers in `corpus/knowledge/*.md` brought under the R25-02 self-count binder (round-25 closure debt D2).
- **C2 — freshness, 9 → 9 (sourced S042/S043):** a release clock types a numerically older observation as `REGRESSED` (exit 1) instead of a fired release (round-26 FinalRearm's inherited limit).

Work items:
- C1: one BUILD scout inventoried each of the 25 knowledge entries (`build/Know*.md`); 22 `KN-*` bindings over eight entries landed in `corpus/self-counts.tsv` (lines 58ff); stale values corrected with history clauses (claim-ledger.md 72→170; op-ref-consumption 29→36 and 21→36; surface-census 19→20), never-true erratum values marked misstated, per-round counts written as ledger pointers, positional indexes named. Exclusion rule and named debt: `corpus/lessons/round-27.md:37-81`; old/new text: `knowledge-migrations.json`; criterion QM26 `corpus/QUALITY.md:133`.
- C2: `numeric_version`/`is_regression`/`feed_floors` in `corpus/release-clock.py` — below own anchor, below the feed's highest numeric anchor, or (observe) below the prior observation → `REGRESSED`; non-strict observations refused. Clock selftest 67 → 79. Lesson `corpus/lessons/round-27.md:83-98, 185-193`; criterion QM25 `corpus/QUALITY.md:132`.
- Frontier: S042 (SemVer 2.0.0 §11.2) and S043 (PyPA version specifiers) opened, captured and admitted tier A (`corpus/SOURCES.md:49-50`, gate `corpus/lessons/round-27.md:16-35`, captures `captures/metadata.json`).
- Mistakes mined: M27-1..M27-4 (`corpus/lessons/round-27.md:100-107`), M27-1/M27-2 with executed able-to-fail controls (final Gate below); M27-4 is the ScribeLesson seat misroot (`misroot-sweep.txt`).
- Residual falsification: 8 seats on candidate `144babcb`; accepted findings fixed (surviving major-component mutant, non-strict observations, observe without feed floor, doc overclaims), rejections kept as named limits (`corpus/lessons/round-27.md:178-226`, `residual/`).
- Final Gate executed in a clean clone of the measured revision (`final/invocations.json`).
- Replacement work (this session): verified and landed the predecessor's uncommitted census correction (below); misroot sweep; this report.

## Landed changes

All via `scripts/hyaku/jj-lane.sh`; LOG entry `kagi-shokunin/LOG.md:1496`, SCORECARD `kagi-shokunin/SCORECARD.md:1081` (+ appended measured outcome at `:1100`).
- `144babcb892f0a30154880a9f94aa59ca8ddf9c5` — candidate: KN bindings + knowledge corrections, REGRESSED rule, S042/S043, QM25/QM26 (LOG:1496 C1/C2 bullets).
- `3fb77271eeee797047c37871038b1db1247fa236` — residual falsifier fixes, doc corrections, BUILD/residual evidence; **measured revision** (LOG:1496 residual bullet).
- `29fa79b7a1109d8c766bc416c72fb8e635b3bf9b` — final Gate receipts, wave outcomes, measured-outcome text (LOG:1496 final bullet; SCORECARD:1100).
- `3553d499577084a6c98d7078906017840bbf7b28` — **inherited and landed by the replacement**: append-only census correction (`corpus/lessons/round-27.md:262-267`) plus its restamp (`corpus/stamps.tsv`). Re-verified before landing: `.ufo/waves/round-26/census-end.json` and `final/census-end.json` both carry 11 W04 lines, exit 0, S039–S041 already present at round-26 end; lesson sha256 `3a3ee417…` matched the pending stamp; `bash corpus/claim-ledger.sh verify` → `CLAIM_LEDGER: CLEAN (claims=65 deferred=0 stamped=90 ids=65 cited=55 labeled_ids=20 orphans=10 host_skipped=12)`. Helper output: `landed 3553d499577084a6c98d7078906017840bbf7b28`.
- Lane state after landing: `local=remote=3553d499577084a6c98d7078906017840bbf7b28 ahead=0 behind=0 tracked=0 untracked=0`.

## Before → after measurements

**BASE `0a47dd189356ea66ec83c3891eed54526e95b89b`; measured revision `3fb77271eeee797047c37871038b1db1247fa236`** (later commits are text/receipts/stamps only). Clean clone, `env -i PATH HOME=/fast/scratch LC_ALL=C PYTHONDONTWRITEBYTECODE=1`; argv/exits/tails in `final/invocations.json`.

| Claim | Counting command | Before → after |
|---|---|---|
| C1 | `python3 -I -B .ufo/waves/round-27/tools/c1-measure.py <docs-rev> <table-rev> <label> <out>` (final table over BASE docs, then final docs) | `SELF_COUNTS: STALE (claims=60 stale=4)` exit 1 → `CLEAN (claims=60 stale=0)` exit 0. Red controls: `--mutate <id>` for all 22 `KN-*` ids each exit 1 naming exactly that id (18 STALE, 4 UNLOCATED) — `final/c1-mutate-*.json`. |
| C2 | `python3 -I -B .ufo/waves/round-27/tools/c2-measure.py <rev> <label> <out>` | Downgrade fixtures accepted CLEAN 4/4 → 0/4; REGRESSED-exact 0/4 → 4/4 (lie S040; rollback S027/S028/S040/S041; un-fire S027/S028; non-numeric S012). Control and default `RELEASE_CLOCK: CLEAN (on_release=30 bound=30 unbound=0 observed=30 fired=3 derived=15)` at both; selftest PASS 67 → 79. `final/c2-before.json`, `final/c2-after.json`. |
| Separability | `python3 -I -B .ufo/waves/round-27/tools/separability.py <rev> <out>` | C1-only overlay: knowledge stale 0, selftest 67, downgrades still accepted 4/4. C2-only overlay: REGRESSED 4/4, selftest 79, zero `KN-*` rows, `SELF_COUNTS: STALE (claims=38 stale=2)` on SC/PV-CLOCK-SELFTEST only (the declared C2→C1 doc edge). `final/separability.json`. |

Regression outcomes at the measured revision: ledger (fleet layout) CLEAN as above; lone clone `INCOMPLETE` with exactly `LAYOUT-INCOMPLETE R11-08 exit=3` (inherited since round 25; C2-of-round-25 lone citations stay honestly INCOMPLETE, not a round-27 target).

## Sources & frontier

Registry **41 → 43** (`grep -c '^| S0' corpus/SOURCES.md` at BASE vs tip): +2 tier A (S042, S043), status mined, used-by `corpus/lessons/round-27.md`; existing rows' status/recheck/used-by: no changes. Two rejections recorded in the gate (spec-as-feed-completeness; lexical/date ordering). Frontier row added: version regression versus release (`corpus/SOURCES.md:64`, search log `:76`).

```sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kagi
```

**Start:** no round-27 start census was run or retained — a conformance defect, disclosed. The retained before reference is round-26's end receipt `.ufo/waves/round-26/census-end.json` (exit 0, 11 W04). The lesson's original "start had 8" was withdrawn by the correction landed in `3553d499` (`corpus/lessons/round-27.md:262-267`).

**End** (measured revision receipt `final/census-end.json`: exit 0, 11 W04; re-run by the replacement at `3553d499`, exit **0**):

```text
kagi	W04	S019 duplicate url www.1password.dev/brokered-access across scopes
kagi	W04	S020 duplicate url 1password.com/blog/1password-credential-broker-public-preview across scopes
kagi	W04	S021 duplicate url openbao.org/docs/concepts/tokens across scopes
kagi	W04	S022 duplicate url developer.hashicorp.com/vault/docs/auth/jwt across scopes
kagi	W04	S023 duplicate url developer.hashicorp.com/vault/docs/concepts/lease across scopes
kagi	W04	S025 duplicate url openbao.org/docs/auth/jwt across scopes
kagi	W04	S026 duplicate url openbao.org/docs/concepts/tokens across scopes
kagi	W04	S032 duplicate url www.1password.dev/brokered-access across scopes
kagi	W04	S039 duplicate url www.python.org/downloads/feed.rss across scopes
kagi	W04	S040 duplicate url docs.python.org/3/library/re.html across scopes
kagi	W04	S041 duplicate url docs.python.org/3/library/html.html across scopes
kagi	ok	/home/vgpnk/Projects/shokunin/kagi-shokunin/corpus/SOURCES.md
```

Warnings unchanged 11 → 11; S042/S043 added clean. Sourced claim: C2 rests on S042/S043. Outside admit/reject spot-check: pending the parent closure.

## Trend verdicts

- **expansion: unchanged** — two ordering-spec rows on held release-clock ground; no new knowledge entry, governed surface or capability (SCORECARD:1081 coverage row).
- **quality: improved** — knowledge-number staleness 4 → 0 with 22/22 red controls; silent numeric regression accepted 4/4 → 0/4, selftest 67 → 79 (`final/`).
- **discernment: unchanged** — QM25/QM26 learn real mined mistakes (M27-1/M27-2) and the round's critics caught L1 overclaims (M27-3), but no fresh outside admit/reject agreement exists yet; parent closure authoritative.

## SHONEN

- [~] Decision tables/error patterns/checklists/cited sources — `kagi-shokunin/SKILL.md`, QM25/QM26, S042/S043; author assertion, no named non-author verifier.
- [~] End-to-end domain task — historical `kagi-shokunin/LOG.md:20` remains the evidence; no live vault/handler operation this round.
- [~] Instructions executable without oral context — final Gate replayed in a clean clone from recorded argv (`final/invocations.json`); author-side.
- [~] No cross-domain bleed — `kagi-shokunin/PROVINCE.md`; five BUILD connector reports (`build/Conn*.md`); ConnKumitate's REGRESSED-token overlap named as debt.

## Concurrency, limits and conformance

Seat census (run by the replacement, exit 0):

```sh
python3 -c 'import json; from pathlib import Path; p=Path(".ufo/waves/round-27"); b=json.loads((p/"build-spec.json").read_text())["items"]; print("build seats=%d reports=%d dead=%s" % (len(b),sum((p/"build"/(x["name"]+".md")).is_file() for x in b),[x["name"] for x in b if not (p/"build"/(x["name"]+".md")).is_file()]))'; ls .ufo/waves/round-27/residual | wc -l
```
```text
build seats=67 reports=58 dead=['ClockSops', 'ClockVault', 'ClockOpenbao', 'ClockPython', 'ClockCurl', 'ClockQuotes', 'RevwLocator', 'RevwBookkeeping', 'RevwDocsAudit']
8
```

- **BUILD wave 67** (validated, one unchanged taskCall): 29 scout, 9 reviewer, 8 critic, 6 scribe, 5 connector, 4 executor, 2 mutation-tester, 2 revenger, 1 simplifier, 1 sentinel. Refused by the job cap 16 times, dispatched on try 17 (`build-refusals.json`); slot acquired/released. Planner seat held by the L1 (validator rejects `planner`).
- **Residual batch 8** (ordinary task call; <64 distinct attack items remained): 6 critic, 1 reviewer, 1 mutation-tester; 2 cap refusals, dispatched on try 3; 8/8 reports.
- **Total 75 seats, 66 reports, 9 dead, 0 replacements.** All nine dead were reviewers: `Devin stream error resource_exhausted: Reached free model rate limit ... (reset 15:51 or 17:06 UTC)` (`terminal-error-notices.json`). No seat was added after the coordinator's death; the replacement dispatched nothing (round work was complete; only landing remained).
- Inherited: all predecessor commits (`144babcb`, `3fb77271`, `29fa79b7`) and wave evidence, re-checked via the final receipts and a fresh ledger verify + census; the uncommitted correction re-verified and landed (`3553d499`). Discarded: nothing.
- Misroots: M27-4 (ScribeLesson, relocated byte-exact by the predecessor, `misroot-sweep.txt`). Replacement's fleet sweep (`git -C /home/vgpnk/Projects/shokunin status --porcelain`): only `.ufo/state/*` baselines, `watchdog.log` and `.ufo/reports/round-22/souji.md` — none kagi's; untouched.
- Disclosures: replacement did not re-run the full load order (landing-only scope). An earlier dev self-counts run printed SETUP once during a residual seat; clean-clone runs are CLEAN (lesson:255-257). Named debts (derived-anchor forgery, leading-zero equality, >4300-digit ValueError, branch-scoped rows) stay open in the lesson.
- **Tool installs/updates: none.** No pacman transaction or host-service action.
- **Stale-lane:** respawn-per-round driver; no other kagi mission open; round 28 not started or claimed.
- **Open L0 questions: none.**
