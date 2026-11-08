# tsukuroi — round 95 report (hyaku run 15)

Lane tip before the round: `c0a20cef641ada6feeab1ca107ea62c1848d1da0`. Round commits: `2abddda5`
(freeze), `a2ed6eee` (freeze A1), `b66e6be5` (C2 rows), `884ed06b` (wave dispatch, A2), `a302e688`
(registry row corrections), `0afeb7d9` (settle), `b8f878c8` (A1 development runs preserved). Final lane tip `b8f878c8`
(`ls-remote origin refs/heads/master` → `b8f878c88fa795fbf20d6129807dfc5222e5fadf`; `jj-lane state`
ahead=0 behind=0, tracked=0 untracked=0).

## Work performed

**Declared claims (2).** C1 — *depth* (tied lowest non-retired axis, with adjacency; no adjacency move
is declarable, see below): the accepted leg of the gate's published 1-9-digit component bound, a new
battery family `REFUSAL-VERSIONS-9DIGIT` plus the one-clause bend `N05-strict-8`. C2 — *operability*
(assurance arm): the lane's own registry gate is red at the tip, and this round makes it green with
four new rows and two repaired cells. Full declaration and amendments A1-A4: `.ufo/plans/round-95.md`.

- **C1 instrument.** `tools/limine-pin-battery-r95.py` (99 families; the r94 roster byte-for-byte plus
  `REFUSAL-VERSIONS-9DIGIT`, `fam_refusal_versions_9digit` at `:1707-1715`, `REFUSAL_DIGIT9` at
  `:1694` now referenced — the r94 "declared and unused" defect), `tools/make-r95-bends.py` (one
  one-clause emitter), frozen controls under `.ufo/waves/round-95/before/controls/` (the r94 battery
  and gate copies, the bend, `count-runs.py`), all pinned in
  `.ufo/waves/round-95/before/instruments.sha256` (`sha256sum -c` → 9 × OK; receipt
  `w1/ExecBattery/hash-before.txt`, re-checked after every run). Commit `2abddda5`.
- **C1 landed-gate leg.** Canonical `python3 tools/limine-pin-battery-r95.py --gate
  tools/check-limine-pins.py --runs 3` → `99/99 met` in each run, `failed_families []`, 0 error rows
  (`after/c1-canonical.json`, `after/c1-canonical.log`); the same from a `git clone --shared` at
  `884ed06b` with the clone's own battery and gate → `99/99 met` ×3, 0 error rows
  (`w1/ExecBattery/c1-clone.json`, `clone-head.txt` = `884ed06b`, tool hashes equal to the freeze).
  The four `REFUSAL-VERSIONS-9DIGIT` rows of one run were printed verbatim
  (`w1/ExecBattery/c1-canonical-9digit-rows.txt`): `want`/`got` equal, rc 1, `DEGRADED`, the LP-MISMATCH pin with
  consequence `panic`, `999999999.9.9`, source `flag`, `error null`.
- **C1 near-miss leg.** `diff -u tools/check-limine-pins.py before/controls/bends/N05-strict-8.py` →
  exactly one changed line (`len(p) <= 9` → `<= 8`; `w1/ExecBend/n05-diff.txt`), re-derived in scratch
  and `cmp`-identical to the frozen bend (`n05-rederive.txt`). `--gate N05-strict-8 --runs 3` →
  `98/99 unmet` in each run, canonical (`after/n05-canonical.json`) and clone
  (`w1/ExecBend/n05-clone.json`), `failed_families` exactly `["REFUSAL-VERSIONS-9DIGIT"]`, four rc-64
  error rows (the bend's refusal, `bad-output: JSONDecodeError rc=64 stderr=… --limine-version must be
  X.Y.Z or auto`). The r95 roster's other 98 families still pass on the bend.
- **C1 do-nothing legs.** The r94 battery (byte-identical to `tools/limine-pin-battery-r94.py`,
  `d66b4a59…`) on `N05-strict-8` → `met 98/98` ×3, 0 error rows, 0 `REFUSAL-VERSIONS-9DIGIT` rows
  (`after/dn-n05-canonical.json`, `w1/ExecDoNothing/dn-n05.json`); on the landed gate → `met 98/98`
  ×3, 0 nine-digit rows (`after/dn-gate-canonical.json`, `w1/ExecDoNothing/dn-gate.json`). The r94
  **family roster** is blind to the bend; its `--usage-check` leg is not (A4).
- **C1 mutation evidence.** Eight one-clause gate mutants, each emitted from the landed bytes with an
  exact-once guard (`w1/MutBound/mutants/`): M01 (`<= 8`), M03 (reject the exact member) and M07
  (era forced above 1000) die with `failed_families` exactly `["REFUSAL-VERSIONS-9DIGIT"]`; M02
  (`<= 10`) and M05 (no bound) on the refused leg; M04 (`>` era split) on `ERA-EXACT-125`; M08
  (refusal message on stdout) on the refusal families. **M06 survives** (echo a wrong
  `limine_version` for an explicit `--limine-version`) — a coverage gap, recorded (`w1/MutBound.md`
  §4, `w1/ConnectorOverlap.md` §1).
- **C2 registry repair.** Four rows added to the operative table — `limine-pin-battery-r94`,
  `make-r94-bends`, `limine-pin-battery-r95`, `make-r95-bends` — and the `limine-pins` row's cells
  repaired (`default auto`, `(39 fixtures`, receipt pointer `round-94/after/live-c2-*.json`, the
  64 cell naming the probe-failure refusal). Commit `b66e6be5`; the wave's row findings then forced
  corrections (`build-r94-bends` kind `library` and its honest per-variant exit cell, both emitters'
  fabricated `2` removed, both battery scope cells no longer naming an unread `$HYAKU_SCRATCH`),
  commit `a302e688`.
- **C2 measurement.** `python3 tools/check-registry-coverage.py --revision c0a20cef…` → `status FAIL`,
  findings 2 (the two r94 tools), missing 2, `tools_total 149`, `registered 147`
  (`after/c2-before-c0a20cef.json`); at `b66e6be5`, `884ed06b` and `a302e688` → `status PASS`,
  findings 0, missing 0, `tools_total 151`, `registered 151` (`after/c2-after-b66e6be5.json`,
  `w1/ExecRegistry/`, `w1/CriticClaims/registry-tip-884ed06b.json`). Gate selftest `PASS (23 cases,
  23 passed, 0 failed)`; `limine-pins` selftest `selftest PASS 39/39`.
- **Wave w1.** One v1 wave, 13 seats, 31 % attack roles, 1 connector, 0 dead. Spec/dispatch/ready:
  `.ufo/waves/round-95/w1-spec.json`, `w1-dispatch.json` (validator `counts` 13 spawn / 0 resume /
  13 total, `w1-validate.err` empty), `w1.ready` + `w1.ready.dispatched` (the r94 routed-2 artifact
  debt). Seat reports under `.ufo/waves/round-95/w1/`.
- **Sources.** S389 opened this round (Python 3 `stdtypes` integer string conversion length
  limitation; pinned 815447 bytes, sha256 `6bf2ce2b…`, quotes at bytes 785297 and 782228) and S386/
  S387/S388 re-opened byte-identically (`w1/ScoutSources/receipts/`). Census before and after below.
- **Corpus.** `corpus/knowledge/limine-bound-9digit-r95.md` (new entry, cites S389 and the re-opened
  Limine rows), `corpus/lessons/round-95.md` (integrated from the `ScribeLesson` draft plus the late
  seat findings and A3/A4), `corpus/SOURCES.md` row S389, `corpus/README.md` round-95 section and
  Frontier bullets, `SCORECARD.md` round-95 declaration and measured outcome.
- **Routed defects from the r94 spot-check.** 1 (registry rows) closed by C2; 2 (`.ready` artifact)
  closed — `w1.ready` and `w1.ready.dispatched` are committed this round; 3 (freeze manifest vs plan)
  closed-by-design — the frozen plan copy is `before/plan-frozen.md` and the live plan is not pinned,
  so post-freeze amendments cannot invalidate the manifest (verified: `sha256sum -c` → 9 × OK after
  A3/A4); 4 (do-nothing arithmetic and the stderr clause) corrected in this report and the lesson —
  the r93 gate reads `97/98 unmet` on the r94 roster and refuses a stderr-only fake like the V4 probe
  (`p.stdout` only); 5 (report prose counts) — every count here is copied from a named artifact and
  re-counted before filing; 6 (uncited final commit) — `029f6629` is named here; 7 (r93 routed-item
  mapping) — the r93 queue is mapped by its own text in the lesson, and routed 4's M12 timeout survivor
  and routed 5's `VERDICT-INCOMPLETE` stay **open and named**; 8 (battery docstring vs fixture) — the
  declared-and-unused `REFUSAL_DIGIT9` is now referenced by the r95 family (closed); the docstring's
  stderr sentence is left as r94 wrote it and the correction is recorded in the lesson; 9 (coverage
  gaps) — the over-strict `<= 8` blindness is closed by C1, the `12.9.6.1` extra-component shape stays
  on the Frontier; 10 (contested scope) — carried, operator-owned, not absorbed
  (`w1/ConnectorOverlap/contested-scope-item2.txt`).

## Landed changes

| Change | LOG entry | Commit |
|---|---|---|
| `tools/limine-pin-battery-r95.py` (99 families; `REFUSAL-VERSIONS-9DIGIT`) | `Round 95 — freeze` | `2abddda5` |
| `tools/make-r95-bends.py` + frozen bend `N05-strict-8` + do-nothing controls + `claims.json` + `plan-frozen.md` + `instruments.sha256` | `Round 95 — freeze` | `2abddda5` |
| `claims.json` C1 target narrowed to the instruments' real error/roster behaviour (A1) | `Round 95 — freeze` | `a2ed6eee` |
| Four registry rows + `limine-pins` cells `auto`/`39` (C2) | `Round 95 — C2` | `b66e6be5` |
| Wave w1 spec/dispatch/ready + C2 before/after receipts (A2) | `Round 95 — wave` | `884ed06b` |
| Registry row corrections from the wave (emitter kinds/exits, battery scope cells, `limine-pins` receipt pointer and 64 cell) | `Round 95 — settle` | `a302e688` |
| `corpus/knowledge/limine-bound-9digit-r95.md`, `corpus/lessons/round-95.md`, `corpus/SOURCES.md` S389, `corpus/README.md`, `SCORECARD.md`, `LOG.md`, wave receipts, `claim-falsification.tsv`, `w1-results.json`, `w1.ready.dispatched` | `Round 95 — settle` | `0afeb7d9` |
| `before/dev-runs/dev-n05-r{94,95}.json` — the two development runs A1's plan pointer names, preserved under the wave dir (development output, never receipts) | `Round 95 — settle` | `b8f878c8` |

## Before → after measurements

**C1 — depth 8 (tied lowest), accepted leg of the published component bound.**

```sh
python3 tools/limine-pin-battery-r95.py --gate tools/check-limine-pins.py --runs 3 \
  --work <scratch> --json .ufo/waves/round-95/after/c1-canonical.json
python3 .ufo/waves/round-95/before/controls/count-runs.py \
  .ufo/waves/round-95/after/c1-canonical.json --family REFUSAL-VERSIONS-9DIGIT
```

Measured at `884ed06b` (gate and battery bytes pinned by the freeze manifest; the gate is unchanged
from `7d79ac29…`). Before: the r94 roster has **98** families and **0** in-bound 9-digit cases —
`do-nothing-battery-r94.py --gate N05-strict-8 --runs 3` reads `met 98/98` with 0
`REFUSAL-VERSIONS-9DIGIT` rows (`after/dn-n05-canonical.json`). After: **99** families, landed gate
`99/99 met` ×3 canonical and ×3 clone with `failed_families []` and 0 error rows; `N05-strict-8`
`98/99 unmet` ×3 in both layouts with `failed_families` exactly `["REFUSAL-VERSIONS-9DIGIT"]`
(`after/n05-canonical.json`, `w1/ExecBend/n05-clone.json`). Mutants: M01/M03/M07 die on the new
family alone (`w1/MutBound/receipts/summary-table.txt`). Verdict **met**; the score stays 8 (a sharper
arm, no ordinal uplift).

**C2 — operability 9, the lane's registry gate.**

```sh
python3 tools/check-registry-coverage.py --revision c0a20cef641ada6feeab1ca107ea62c1848d1da0
python3 tools/check-registry-coverage.py --revision a302e6888e338f5e6ceb342dd17d7b7ea87b8463
```

Before, at the pre-round tip: `status FAIL`, `findings 2`, `missing 2`, `tools_total 149`,
`registered 147` (the two findings name `tools/limine-pin-battery-r94.py` and
`tools/make-r94-bends.py`; `after/c2-before-c0a20cef.json`). After, at `b66e6be5` (the C2 commit),
`884ed06b` (wave dispatch), `a302e688` (row corrections), `0afeb7d9` (settle) and `b8f878c8` (final tip): `status PASS`, `findings 0`,
`missing 0`, `tools_total 151`, `registered 151` (`after/c2-after-b66e6be5.json`,
`w1/CriticClaims/registry-tip-884ed06b.json`). Selftests: registry `PASS (23 cases, 23 passed,
0 failed)`, `limine-pins` `selftest PASS 39/39`; the `limine-pins` row reads ``default `auto` `` and
`(39 fixtures` and no longer names `default 12.9.4` (`w1/ExecRegistry/rows-inspect.json`,
`w1/ReviewRegistry/`). Verdict **met**; the score stays 9 (assurance repair, no ordinal uplift).

## Sources & frontier

**SOURCES census.** Round start (2026-11-08T06:45Z), `scripts/sources-census.sh validate --root
/home/vgpnk/Projects/shokunin tsukuroi` → exit **0**, `tsukuroi ok …/corpus/SOURCES.md`, 388 rows
(`git show c0a20cef:corpus/SOURCES.md | grep -cE '^\|[[:space:]]*S[0-9]{3,}'` → 388), 57 W04 + the
pre-existing W01 on S381. Round end (same command, receipt
`.ufo/waves/round-95/after/census-after.txt`) → exit **0**, `tsukuroi ok …/corpus/SOURCES.md`,
389 rows (`grep -cE '^\|[[:space:]]*S[0-9]{3,}' corpus/SOURCES.md` → 389), 57 W04, 1 W01, **0
E-findings** (no E11: the new row's `used-by` files exist).

**Rows added, by tier:** 1 row — `S389`, tier **A** (Python 3 `stdtypes`, integer string conversion
length limitation; pinned 815447 bytes, sha256 `6bf2ce2b…`, located quotes at byte 785297 and byte
782228, access 2026-11-08). **Rows touched old→new:** none in place; S389 is new. S386/S387/S388 were
re-opened read-only and their digests reproduced their frozen copies byte-for-byte
(`w1/ScoutSources/receipts/receipt-02-limine-reopen.txt`), so no `status`/`recheck`/`used-by` cell
changed. **Frontier rows advanced:** the `<= 8`-blindness gap named by the r94 Frontier (an
over-strict bound reading `met`) is closed by `REFUSAL-VERSIONS-9DIGIT` + `N05-strict-8`; the
per-component accepted boundary (9-digit Y/Z), the `visibility_era` mechanism, the echoed
`limine_version` (M06 survivor) and the registry gate's lack of name→path/content binding are the new
Frontier rows (`corpus/README.md` § "Frontier (round-95 addition)").

## Trend verdicts

- **expansion — improved.** One admitted knowledge entry on ground the lane did not hold
  (`corpus/knowledge/limine-bound-9digit-r95.md`: the accepted leg of a published numeric bound), one
  new SOURCES row (S389), SOURCES 388 → 389 with census exit 0, and the README Frontier advances the
  old blind spot into named limits.
- **quality — improved.** `tools/limine-pin-battery-r95.py` (99 families) closes a certified-blind
  gate class: 7 of 8 one-clause mutants die, including three that die on the new family alone
  (`w1/MutBound/receipts/summary-table.txt`); the lane's own registry gate goes from FAIL 2/149 to
  PASS 0/151 at the landed tip. C1's stop on the per-component leg is recorded as a limit, not as
  quality credit.
- **discernment — improved.** Three wave artifacts forced three honest narrowings before filing —
  A3 (ReviewBattery F1: "largest in-bound member" false under a per-component cap), A4 (ExecDoNothing:
  the blindness is the roster's, not the instrument's; ExecRegistry/ReviewRegistry: the registry
  gate's PASS does not certify row content), and the ledger keeps `falsifies-wording`/`falsifies-number`
  rows with their amendment pointers instead of a clean bill. M06's survival is reported, not hidden.

## SHONEN

- [~] `SKILL.md` contains real decision tables, error patterns, checklists, cited sources — pointer:
  the operative registry table now carries the r94/r95 battery rows and the repaired `limine-pins`
  row (SKILL.md operative table, `w1/ExecRegistry/rows-inspect.json`); non-author verification of the
  whole file remains owed.
- [~] At least one end-to-end domain task executed and logged in LOG.md — pointer: `LOG.md`
  "Round 95 — settle" and the C1/C2 receipts above; the end-to-end task is the battery certification
  run (`after/c1-canonical.json`), not a host-health report.
- [~] Instructions executable by an agent without oral context — pointer: the wave's 13 seats ran the
  frozen instruments from the spec alone (`w1/*.md`), including two clean-room clones; the
  whole-SKILL no-oral-context retest remains unexecuted and no non-author has replayed it.
- [~] No cross-domain bleed (`PROVINCE.md` still accurate) — pointer:
  `w1/ConnectorOverlap/contested-scope-item2.txt`: no sibling duplicate or contradiction across 20
  sibling repos; the kaidoku/revenger reverse-engineering ownership stays unruled and operator-owned,
  reported not absorbed.

## Round shape, seats, and wave evidence

One v1 wave (run-15 band 8-16, policy `scripts/hyaku/ufo-wave-policy.json`, `waveMinLanes 8` /
`waveMaxLanes 16`): **13 seats** — `ExecBattery`, `ExecBend`, `ExecDoNothing`, `ExecRegistry`
(executor ×4), `ScoutSources`, `ScoutDrift` (scout ×2), `ScribeKnowledge`, `ScribeLesson` (scribe ×2),
`ReviewBattery`, `ReviewRegistry` (reviewer ×2), `CriticClaims` (critic), `MutBound`
(mutation-tester), `ConnectorOverlap` (connector). Attack roles 4/13 = **31 %** (≥25 %); connector
counts as the fifth adversarial read for the pre-file ledger. **Dead seats: 0.** Residual call: none.
The §3 planner seat is held by the L1 (the validator rejects `planner`); the bounded planning
data-walk rode `ScoutDrift`, as the plan records. Evidence: `w1-spec.json`, `w1-dispatch.json`
(`counts` 13 spawn / 0 resume / 13 total; `w1-validate.err` empty), `w1.ready` +
`w1.ready.dispatched`, and the 13 seat reports under `w1/` (with `w1/ScoutDrift/` receipts).

## Pre-file falsification ledger

`python3 scripts/hyaku/prefile-falsification.py --lane tsukuroi --round 95` — line and exit code
pasted below (the ledger is `tsukuroi-shokunin/.ufo/waves/round-95/claim-falsification.tsv`):

```
PREFILE-FALSIFICATION: pass claims=2 rows=21 attack_seats=5 findings=0
```
exit **0**. All five attack seats (2 reviewer, 1 critic, 1 mutation-tester, 1 connector) appear in
the artifact column; the four `falsifies-wording` rows point at A2/A3/A4 and the one
`falsifies-number` row at A1; every artifact resolves under `.ufo/waves/round-95/`.

## Stale-lane

Respawn-per-round driver (`respawn-per-round`: the round ends when this report lands and the watchdog
starts round 96); no other mission of this lane is open. Round 94's closure is `rejected-honest-stop`
(one, not three in a row — the 3-rejection gate does not apply).

## Tool installs

None. No seat installed, upgraded or removed a package; no `pacman` transaction was attempted
(pacman stays PAUSED per the addendum guard), no `uv`/`npm`/`npx` install, no host sysctl, service or
kernel-parameter change. Every seat recorded the same in its report.

## L0 questions

None opened this round. Carried, operator-owned: the r86 HOST INCIDENT line in
`.ufo/l0-questions.md` (the UKI BLAKE2b pins in `/boot/limine.conf` no longer match after the r86
`objcopy` in-place rewrite; repair is the operator's and is not attempted here). The contested
kaidoku/revenger reverse-engineering ownership remains unruled and is reported, not absorbed.

## Inherited state

At round start the lane was clean: `jj-lane.sh state` → `branch=master local=c0a20cef… remote=c0a20cef…
ahead=0 behind=0 tracked=0 untracked=0`; no uncommitted lane-authored leftovers, nothing to resolve or
revert. The r94 wave artifacts are committed by round 94. One r94 report defect is corrected here:
its final commit `029f6629ab67402bea2f0651ea104912f948f324` (claim-falsification path shape) was cited
in no report; it is named in this report (and no earlier report is rewritten). No watchdog line
`lane-dead-no-report tsukuroi round=95` exists for this attempt.

## Honesty and limits

- The gate `tools/check-limine-pins.py` is **unchanged** this round (`7d79ac29…`, the same bytes as
  the r94 control copy). The round buys measurement capability, not gate behaviour; the gate's
  answers are identical except where the new family certifies them.
- C1 is **X-certified only**: the cap is per component, the true maximum
  `999999999.999999999.999999999` is untested, and a Y-bound bend reads `met` 99/99
  (`w1/ReviewBattery.md` F1). The era *mechanism* (`visibility_era`) and the echoed `limine_version`
  for explicit versions are not asserted (F2/F3; M06 survives). These are Frontier rows, not claims.
- C2's registry gate certifies **row presence**, not cell content; the `limine-pins` cells are
  certified by a direct `git show` grep plus the gate's own `selftest PASS 39/39` (A4). Its PASS also
  cannot catch a name↔path swap or an inverted verdict map (`w1/ExecRegistry.md` §6).
- Every number in this report is copied from a committed receipt or re-derived by the command shown;
  no check was run that is not cited. The wave's attack seats found four wording defects (A1-A4) and
  one survivor (M06); all are recorded, none is papered over.
- The freeze is the last **pre-dispatch** byte set (`884ed06b`): A1 and A2 re-pinned
  `before/plan-frozen.md` before the wave existed, so the manifest verifies by construction rather
  than by a single immutable commit (`w1/ScoutDrift.md` F6). No instrument byte changed after
  dispatch (`w1/ExecBattery/hash-before.txt` vs `hash-after.txt`, 9 × OK).
- `w1-spec.json`'s top-level `axes` list omits `adjacency` while the `ConnectorOverlap` item carries
  it (ScoutDrift F7); cosmetic, recorded, not re-dispatched.
- The r93 routed-5 label in the plan's disposition 7 and the lesson's first draft (`VERDICT-INCOMPLETE`)
  was wrong; the lesson now names r93 routed 5 as probe-grammar leniency (ScoutDrift F2), and the
  `fam_auto_probe_shapes` stderr sentence is carried open in the lesson rather than "corrected"
  (ScoutDrift F3). The plan's disposition-7 sentence is historical and not rewritten.
