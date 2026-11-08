# tsukuroi round 94 report

## Work performed

Two declared claims, each on a distinct axis, plus the frontier step:
**C1 (depth 8)** — the `limine-pins` battery's refusal/probe-shape sampling: two new families,
`REFUSAL-VERSIONS-10DIGIT` and `AUTO-PROBE-SHAPES`, on a 98-family roster, with four one-clause
bends N01-N04. **C2 (operability 9)** — the gate's era-selection default: `auto` becomes the default
of `--limine-version` (V4), so `--live` with no flag probes the installed `limine --version` and
records `limine_version` + `limine_version_source: probe`. Frontier: S386-S388 (v12.9.6 pins,
byte-identical to their v12.9.5 counterparts), QUALITY 139, and the r93 routed defects dispositioned.

Wave `w1`: 14 seats, 43% attack (ReviewGate, ReviewBattery, CriticClaims, CriticForgers, MutDigit10,
MutProbe), 1 connector. Dead seats 0. One wave, one `.ready`, dispatched to the orchestrator;
`WAVE-DONE tsukuroi r94 w1` received before this report was filed. Planner seat: the L1 holds it.

- **Telemetry**: `w1-results.json` — 14/14 settled, 0 dead. Receipts: `w1/ExecReplicate/c1-gate.json` ×3,
  `w1/ExecReplicate/N01-x3.json`, `N02-x3.json`, `N03-x3.json`, `N04-x3.json`; `w1/ExecBends/landed.json`,
  `w1/ExecBends/N01.json`, `N02.json`, `N03.json`, `N04.json`, `dn93.json`, `dn94.json`, `usage.log`;
  `w1/ExecLints/01-gate-selftest.txt`, `02-battery-selftest.txt`, `02b-battery-reference.txt`,
  `03-live-noflag.txt`, `04-live-flag1296.txt`; `w1/ExecLive/leg1-probe.json`, `leg3-strace.log`;
  `w1/ScoutSource/pin-table.tsv`; `w1/MutDigit10/results-r94.json`; `w1/MutProbe/evidence/summary.json`.
- **Canonical L1 receipts** (the L1's own ×3 runs at the frozen tip, same bytes): `after/c1-canonical.json`
  (98/98 `met` ×3, 0 error rows, `count-runs.py` exit 0 on both families), `after/bend-N01.json`,
  `after/bend-N02.json`, `after/bend-N03.json` (`97/98 unmet` with the named family), `after/bend-N04.json`
  (`98/98 met` with `failed_families []`), `after/live-c2.json` (explicit `auto`, unprivileged rc 2,
  `error: conf unreadable…`), `after/live-c2-flagfree.json` (no flag, rc 2, same fields),
  `after/live-c2-root.json` (root `sudo -n`, rc 1, `error: null`, findings `LP-MISMATCH line 30/38`),
  `after/gate-selftest.txt` (`PASS 39/39`), `after/battery-selftest.txt` (`PASS 5/5`),
  `after/battery-reference.txt` (`PASS 18/18`, reference-gate 98/98), `after/usage-check.txt`
  (`met`, 15/15), `after/dn94-r93gate.json` (`97/98 unmet`, `AUTO-PROBE-SHAPES` only),
  `after/dn93-r93battery.json` (`96/96 met` on the r93 roster).
- **Corpus**: SOURCES 385 → 388 (`S386` `config.c` v12.9.6, `S387` ChangeLog v12.9.6, `S388`
  `host/limine.c` v12.9.6), census exit 0; QUALITY 139 lands in this round (`corpus/QUALITY.md`);
  `corpus/knowledge/limine-auto-default-r94.md` (the `auto`-default entry, citing S386-S388);
  `corpus/lessons/round-94.md` (`## Gate` with the S385 rule-1 row supplied, M1-M4).
- **Executable check**: `python3 tools/check-limine-pins.py --selftest` → `selftest PASS 39/39` rc 0
  (`after/gate-selftest.txt`); `python3 tools/limine-pin-battery-r94.py --selftest` → `PASS 5/5`;
  `--selftest --reference tools/check-limine-pins.py` → `PASS 18/18` with `reference-gate PASS
  families_passed=98` (the r93-routed unfinished `--reference` leg, closed this round).
- **Telemetry**: `w1/ReviewBattery/ReviewBattery.md` F1-F2 (the `12.9.6.1` shape unexercised at
  battery level; the accepted 9-digit boundary certified only by the `usage_check` roster) and
  `w1/MutProbe/MutProbe.md` (M02/M04/M07 survive the battery+selftest pair, killed only by the
  ad-hoc probes).
- **Telemetry**: `w1/CriticClaims.md` F1-F6 (SCORECARD froze `102/102`; N04's sentence unsatisfiable
  by its own decoy; the plan's digit10 and AUTO-PROBE-SHAPES enumerations did not match the
  battery's; one pre-freeze N02 `met` receipt against the `×3` sentence; C2's kill sentence false of
  the unprivileged receipt).
- **Telemetry**: `w1/ExecLive/leg3-strace.log` (the probe's `O_RDONLY`-only SYSV trace — the
  mechanism certified here, not by the battery).

## Landed changes

Every change committed through `jj-lane.sh` and pushed (`ls-remote` shows `ef1dd190`), tied to
`LOG.md`'s "Round 94" entries:

| lane commit | content |
|---|---|
| `eb3b3e51` | freeze: gate V4 (`auto` default, `(?![\w.-])` guard), battery r94 (98 families), `make-r94-bends.py`, corpus (`knowledge/limine-auto-default-r94.md`, lesson r94, QUALITY 139, README frontier, SOURCES S386-S388 + S385 `used-by`), plan + `claims.json` + both manifests |
| `a85796ac` | amendment A2: roster total `102/102` → `98/98` (plan + `claims.json`) |
| `b6447374` | wave spec + dispatch (14 seats, 98 families) |
| `ef1dd190` | settle: wave evidence (14 seats), A3 narrowings (C1-1…C1-4, C2-1), SCORECARD outcome table, `claim-falsification.tsv`, canonical `after/` receipts |

No lane commit was left off-branch at filing: `git ls-remote origin refs/heads/master` printed
`ef1dd190`, the same hash `jj-lane.sh state` reports as `remote=`, and `git status --porcelain` in
the lane is empty. No tool was installed or upgraded this round (pacman paused host-wide; nothing
needed installing — the battery's `bwrap` sandbox was already present). ScribeLesson's drafts
(QUALITY-139 row, S385 rule-1 row, M1/M3 prose) are adopted in the lesson and QUALITY as written,
not rewritten.

## Before → after measurements

One counting command per claim, both re-derivable from committed bytes (no other lane wrote the
lane repo's files during the round; the SCORECARD table's arithmetic is the roster literal `98`).

**C1 — depth 8 (tied lowest non-retired axis with adjacency 8).**

| Before | After | Counting command | Commit measured against |
|---|---|---|---|
| r93 battery (96 families): none of the two families (`grep -c` over its roster is 0); r93 gate reads `met` on the r93 roster but answers a verdict for `12.9.6-rc1` and for the stderr fake | Landed gate `98/98 met` ×3 both layouts; N01/N03 `97/98 unmet failed REFUSAL-VERSIONS-10DIGIT` ×3; N02 `97/98 unmet failed AUTO-PROBE-SHAPES` ×3; **N04 `98/98 met` ×3 with `failed_families []`** | `python3 tools/limine-pin-battery-r94.py --gate <GATE> --runs 3 --work <scratch> --json <out>` then `.ufo/waves/round-94/before/controls/count-runs.py <json> --family REFUSAL-VERSIONS-10DIGIT --family AUTO-PROBE-SHAPES` (exit 0 on the landed gate) | `ef1dd190` |

Verdict: **NOT MET as worded — honestly stopped.** On the frozen bytes, three independent executions
agree: the landed gate reads `98/98 met` 0 error rows both layouts; N01/N02/N03 read `unmet` with
their named family; **N04 reads `met` everywhere** — the decoy assigns `_stale_default` and never
reads it, so the target's "each of the four bends reads `unmet`" fails on the fourth. The kill rule
fires (`unmet` if any named bend does not read `unmet` in all three runs), so C1 cannot verify.
**F1 (SCORECARD froze `102/102`)** is an erratum served by plan A2/A3, not a rewrite. N04's miss is
the round's own attack artifact (`w1/CriticClaims.md` F2; ExecReplicate's `N04-x3.json` ×3 `met`).
**N04 is the deliverable's named open item**: a decoy that does not bite cannot close a family; the
next freeze's stale-tree bend must read the env value it substitutes (`LIM_STD_VERSION=12.9.6` +
`12.9.6-rc1` on `AUTO-ERA-B`).

**C2 — operability 9 (assurance arm; capability `installed-version-probe` becomes the default).**

| Before | After | Counting command | Commit measured against |
|---|---|---|---|
| r93 gate: defaults `--limine-version` to `12.9.4` (a hand-typed host-package default) | `auto` is the default (`ap.add_argument("--limine-version", default="auto")`, `tools/check-limine-pins.py:503`); flag-free live prints `limine_version 12.9.4` with `limine_version_source probe` and era `pre-12.9.5` on both live shapes; gate selftest `PASS 39/39`; usage roster `met` 15/15 | `python3 tools/check-limine-pins.py --live` and `python3 tools/check-limine-pins.py --selftest` | `ef1dd190` |

Verdict: **met**, on the privilege-qualified reading recorded as plan amendment C2-1. The predicate's
rc-1 parenthetical is the root receipt (`after/live-c2-root.json`, findings lines 30/38,
`error: null`); the unprivileged receipt (`after/live-c2-flagfree.json`) prints the same version /
source / era fields with `error: "conf unreadable: [Errno 13] …"` and rc 2. The kill sentence's
"`error` non-null" is false of the unprivileged receipt the predicate itself blesses (CriticClaims
F6) — the reading that binds is the field, not its nullness. The do-nothing control discriminates on
the source field: the r93 gate on the r94 roster reads `97/98 unmet` (`AUTO-PROBE-SHAPES` only, from
`dn94-r93gate.json`), and the r93 gate's own `--selftest` also passes 39/39 — the discriminant is
`limine_version_source: "probe"` vs `flag` in the receipt, not the selftest count.

## Sources & frontier

`SOURCES.md` rows before → after: **385 → 388** (S386, S387, S388; all A/`mined`).
Census: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tsukuroi`
→ exit 0 both before (385 rows) and after (388 rows); the only new warnings are the standing W04
duplicate-URL family (`S374/S375` vs `S386`-class duplicates pre-date this round; S386-S388 add two
new W04s of the same standing class, not new debt). `S385`'s `used-by` gained
`corpus/knowledge/limine-auto-default-r94.md, corpus/lessons/round-94.md` (old → new in the lesson;
CORPUS rule 2). The S385 rule-1 row (URL, 2026-11-08, ≤25-word located quote) is now in the round-94
lesson `## Gate` (r93 spot-check routed 2, closed).

Rows added by tier: three A-tier (`S386` `config.c` v12.9.6, `S387` ChangeLog v12.9.6, `S388`
`host/limine.c` v12.9.6). The first two files re-pin upstream; the ChangeLog carries the #700
documentation note ("A config whose first line is an entry has had no global options since 12.9.5").

Frontier rows advanced: QUALITY 139 (`R94-BOUND-CERTIFIED-ONLY-ABOVE`) — a numeric bound is
certified at its boundary, not only above it (the `999999999.0.0` accepted row in the usage roster
certifies the 9-digit cap from inside; the `<= 8` over-strict mutant is killed by that row in
`w1/ReviewBattery/ReviewBattery.md`, and the digit10 family kills `<= 10`/`<= 11` from the other
side). The r93 routed defects: 1 (this report's table is built from `git log --format` over the
freeze range), 2 (S385 rule-1 row), 3 (the `--reference` leg — `after/battery-reference.txt` reads
`PASS 18/18` with `reference-gate PASS families_passed=98`), 4 (the ten-digit enumeration and the
probe-shape family name M13/M12/M03-M05/M11), 5 (the not-word-char suffix guard and
`REFUSAL-VERSIONS-10DIGIT`), 6 (contested kaidoku/revenger RE scope reported, not absorbed).

Assimilation: none. The lane carries no `merge/tsukuroi/` adoption this round; the round's one new
`SOURCES.md` admission is three freshly opened upstream files, not staged package material.

`considerthese/`: the lane repo has no `considerthese/` directory (`ls considerthese/` → absent);
there is no still-unimplemented proposal to mine under §10.

Trend verdicts (author-side, pending the non-author closure):

- **expansion: improved** — one admitted knowledge entry on ground the coverage map did not hold
  (`corpus/knowledge/limine-auto-default-r94.md`) whose `source:` cites three `mined` rows opened
  this round (S386-S388); SOURCES 385 → 388, census exit 0.
- **quality: improved** — the `installed-version-probe` capability row is advanced from "opt-in" to
  "the default" (r94 V4); the r93 battery's survivor M13 is killed at family level by
  `REFUSAL-VERSIONS-10DIGIT`; the battery's `--reference` leg now reads `PASS 18/18`. One honesty
  note: C1 is **honestly stopped** (N04 reads `met` everywhere); the stop is recorded as the round's
  own evidence, not hidden.
- **discernment: improved** — the attack seats falsified one claim's wording (CriticClaims F1-F6)
  and the round narrowed it rather than filing it. The one S385 Gate-row gap from r93 is closed in
  the r94 lesson `## Gate` (row and quote both present).
## SHONEN
Four lines, author-side `[~]`, no non-author verifier; the promotion gate is owed to the closure,
never attested by the lane:

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — see `SHONEN.md` box 1 and its line evidence.
- [~] At least one end-to-end domain task executed and logged in LOG.md — see `SHONEN.md` box 2.
- [~] Instructions executable by an agent without oral context — see `SHONEN.md` box 3.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — see `SHONEN.md` box 4.

## Pre-file falsification ledger

`python3 /home/vgpnk/Projects/shokunin/scripts/hyaku/prefile-falsification.py --lane tsukuroi --round 94`
→ `PREFILE-FALSIFICATION: pass claims=2 rows=14 attack_seats=7 findings=0` (exit 0), run before
filing. Three `falsifies-wording` rows name amendments in `.ufo/plans/round-94.md` (A3: C1-1…C1-4
and C2-1; the C2 row's narrowing also traces the CriticForgers `f2`/docstring leakage sentence, and
the C1 ReviewBattery row traces F1/F2's next-freeze routes). The header row of the ledger is
excluded from the counts the gate reports.

## Stale-lane

Yes — this is the respawn-per-round driver's take: the previous attempt (r93) closed `admitted`
and this round is the next live dispatch. This lane's only mission otherwise is round 94 (rounds
95-100 remain under the same session's block scheduling but are not this round's work).
