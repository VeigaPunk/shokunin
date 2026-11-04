# tameshi — round 80

Lane: `tameshi-shokunin` (verification-fixture craft; axes depth + calibration).
Round 80 (attempt 1), hyaku run 15, L1 agent `TameshiR80`. Base
`dd2b9e2c44df680174a829901829fe86a2185185` (= `origin/master`, the round-79
non-author closure and its spot-check commit). Declaration
`ae591d5a2cf5d08cafad68a4c6ffaa62e0d3f608` (plan, candidate tool bytes, design
receipts, controls). Landing `01ca77cd1bdac3d991e0319644146ace3970b30d`.
Records `f45c133230424ef89087af860bf89df0d22e5efa`. Cold-read rekey
`3e310e2b75b8976602f67a37eea08e786c6a9c8d` and correction
`93991f1a1f89fca863624c75f86a42f3ea46ecf2`; final lane tip
`9d5422bd3414b0dd1c6fa1a1c45fd9da51dee692`. Lane pushed; `ls-remote
origin refs/heads/master` prints `9d5422bd…`.

**Declared claims (1–3, each one axis-move with its own falsifiable
before→after, frozen before any wave data in `plans/round-80.plan.md`):**

1. **R80-C1 — calibration, capability acquisition.** The registry home's
   printed gate figures equal the figures their instruments print now.
2. **R80-C2 — coverage.** The four survivors the round-79 wave named become
   fixture coverage (selfstate arms 15–17, wave-reconcile arm24).
3. **R80-C3 — operability.** The receipt population covers the declared tree,
   including the declared non-committed (design) class.

Saturation at round start: scored axes depth 10, calibration 8, freshness 9;
round 79 entered a capability, so the stagnation nudge did not fire and C1
works calibration (the lowest scored axis).

## Work performed

Round shape: **one v1 wave, 13 seats** under
`scripts/hyaku/ufo-wave-policy.json` (band 8–16), attack seats 4/13 = 30.8 %
(reviewer 2, critic 1, mutation-tester 1). Roles: executor 4 · scribe 1 ·
scout 2 · reviewer 2 · critic 1 · mutation-tester 1 · connector 1 ·
sentinel 1. `labrat` is a frozen-topology seat the validator rejects; the §3
planner seat is held by the L1 (a bounded planning data-walk rode the scouts).
No residual `task` call; round total 13. 13 seats settled, **0 dead**.

- C1 — designed `tools/registry-figure-bind.py` + a 7-row manifest over two
  surfaces (the last same-named markdown row in `SKILL.md`; a
  `tools/registry.json` row), with `match`/`stale`/`absent`/`error`, per-row
  `expect`, exactly-one figure token on each side, and repo-contained paths.
  Landed the `SKILL.md` round-80 registry section and refreshed
  `tools/registry.json`. Evidence: `c1-before-sweep.txt`, `c1-after-sweep.txt`,
  `c1-selftest.txt` under `.ufo/evidence/round-80/design/`.
- C2 — added selfstate arm15 (both decode refusals), arm16 (argv-varying
  cache), arm17 (`sys.flags.utf8_mode`), wave-reconcile arm24 (`record.root`
  refusal, fail-visible when the guard is deleted); both mutant specs extended.
  Evidence: `c2-control-*.txt`, `c2-landed-*.txt`, `noharm-*-arms.diff`.
- C3 — the design receipt block as a measured class (marker required, base
  resolvable, mixed/malformed/duplicate/CRLF/Windows-path forms refused), plus
  a standing `receipt-bytes-tree` registry row. Evidence:
  `c3-before-sweep.txt`, `c3-after-sweep.txt`, `c3-selftest.txt`.
- Frontier — opened S308 (PEP 540), appended S309 (the round-79 refused
  `sys.html` row), re-opened S289; census before/after exit 0 (167 → 169 rows);
  lesson `corpus/lessons/round-80.md` with `## Mistakes` and `## Gate`.
- Wave — 13 seat reports under `.ufo/waves/round-80/w1/` (evidence only; the L1
  judged every claim). Findings folded (see `corpus/lessons/round-80.md`
  `## Wave findings`).

## Landed changes

| Change | LOG entry | Commit |
|---|---|---|
| `tools/registry-figure-bind.py` + `.json` (new), `SKILL.md` round-80 registry section, `tools/registry.json` refreshed rows, `SCORECARD.md` capability row, `tools/selfstate-freshness.json` row | Round 80 (2026-11-04) entry, bullets 1 and 4 | `01ca77cd` |
| `tools/selfstate-freshness.py` arms 15–17 + spec, `tools/wave-reconcile.py` arm24 + spec | Round 80 entry, bullet 2 | `01ca77cd` |
| `tools/receipt-bytes-bind.py` design class + hardened parser, `receipt-bytes-tree` row | Round 80 entry, bullet 3 | `01ca77cd` |
| Wave evidence `.ufo/waves/round-80/` (spec, dispatch, results, 13 seat reports) and design/control receipts `.ufo/evidence/round-80/` | Round 80 entry | `01ca77cd` |
| `SCORECARD.md` round-80 declared/measured blocks + Planned 81, `LOG.md` entry, `corpus/QUALITY.md` criteria 76–77, `corpus/SOURCES.md` S308/S309 + S289 re-open, `corpus/lessons/round-80.md` | same LOG entry; evidence pointers in each row | `f45c1332` |
| Cold-read rekey: 18 uncredited sections re-read/rebound at `f45c1332`, traces + summary under `.ufo/evidence/round-80/rekey/`, round-21 ledger 990 → 1008 | Round 80 entry, Cold-read line | `3e310e2b` |
| Rekey correction: the new registry section's entry carries its 7-file input union and `rekey_round: 80`; ledger 1008 → 1009 | Round 80 appended Cold-read entry; lesson `## Mistakes` 3 | `93991f1a` |
| Post-rekey monitor receipt (`66/66`, score 8, box3 true) + rekey LOG/lesson records | Round 80 appended Cold-read entry | `9d5422bd` |

## Cold-read monitor and rekey

The forecast (`rekey-cost.py`, plan receipt `rekey-cost-full-r80.txt`) priced
`REKEY_COST sections=65 planned=12 at_risk=17 predicted_lost=17`. Measured at
the records tip `f45c1332`: `sections_covered=48` of **66** (SKILL.md grew one
section this round), `calibration_restraint_score=6`, `box3_full_page=false`
(`.ufo/evidence/round-80/coldread-at-f45.json`) — an 18-section loss, one more
than predicted because this round's own registry section is new.

The rekey batch (round-79 run-book, corrected trace path) re-read all 18
uncredited sections at the pin, pinned each section's all-entry input union,
ran one verification per new section and 14 carried verifications, and appended
18 input-keyed ledger entries: `REBIND OK sections=18 entries_added=18
ledger_before=990` (`coldread-rekey-rebind-r63.py`, manifest + union plan +
traces under `.ufo/evidence/round-80/rekey/`). Committed at `3e310e2b`; that
reading was 65/66 because the new section's union is empty
(`inputs-unrecorded`), so an appended entry carrying its 7-file input union and
`rekey_round: 80` landed at `93991f1a` (ledger 1008 → 1009). The copied
run-book's round-79 label and its accepted-but-unwritten `--entries-out` are
recorded as lesson `## Mistakes` 3, not rewritten in the committed entries.
Final reading at `93991f1a` (receipt committed at `9d5422bd`):
`sections_covered=66` of 66, `calibration_restraint_score=8`,
`box3_full_page=true` (`.ufo/evidence/round-80/coldread-after-rekey.json`) —
the same score and page coverage as the base reading, so C1/C2/C3's record
edits cost no calibration credit once the rekey is paid.

## Before → after measurements

Measured commit for every after-state: `01ca77cd` (doc, registry, manifest and
tool bytes all live there; the records commit changes no counter input). Work
root: `.ufo/evidence/round-80/design/`.

### R80-C1 — verifies (measured)

```sh
python3 -I -X utf8 tools/registry-figure-bind.py --selftest | tail -1
python3 -I -X utf8 tools/registry-figure-bind.py --repo . | tail -1
```

| | value |
|---|---|
| Before (base docs/registry, declaration instrument) | `REGISTRY_BIND: rows=7 match=0 stale=5 absent=2 error=0 unexpected=7`, exit 1 — five stale rows (wave-record reconciliation 19/19 vs 23/23 and self-state freshness 11/11 vs 14/14 on both surfaces; the registry sweep row `rows=20 match=18` vs `22/20`) and two absent rows (`receipt-bytes binding sweep` on both surfaces) |
| After | `REGISTRY_BIND: rows=7 match=7 stale=0 absent=0 error=0 unexpected=0`, exit 0; `REGISTRY_BIND_SELFTEST: 11/11 pass` |
| Do-nothing control | the base reading itself (append nothing to either surface); independently reproduced by seat `T80W1E4` from pinned clones |

Kill rule (plan): (i) base = the named row set, PASS; (ii) after = 7/7, PASS;
(iii) selftest 11/11, PASS; (iv) an injected stale row and the boundary /
duplicate-token / empty-declaration cheats measure `stale` or `absent`
(`ARM3` legs, measured in `--selftest`), PASS; (v) no `error` row, PASS;
(vi) population exactly 7, PASS. **Disclosed coupling (critic `T80W1C1`):**
the predicate is figure equality and would hold with the base tokens
(23/23, 14/14, 10/10); the landed rows carry the round's final figures
(24/24, 17/17, 13/13), so the authored byte set names C2/C3's tools. The
predicate is separable; the content is coupled and is reported, not argued
away.

### R80-C2 — verifies (measured)

```sh
python3 -I -X utf8 tools/selfstate-freshness.py --selftest | tail -1
python3 -I -X utf8 tools/wave-reconcile.py --selftest | tail -1
bash tools/mutate-and-run.sh --target tools/selfstate-freshness.py \
  --defects tools/selfstate-freshness-mutants.spec \
  --suite 'python3 -I -X utf8 "$MUTANT" --selftest' --workdir "$WORK/ss" \
  --label selfstate-arms-r80
bash tools/mutate-and-run.sh --target tools/wave-reconcile.py \
  --defects tools/wave-reconcile-mutants.spec \
  --suite 'python3 -I -X utf8 "$MUTANT" --selftest' --workdir "$WORK/wr" \
  --label wave-reconcile-arms-r80
```

| | value |
|---|---|
| Before (control: base bytes + the new defects) | `defects=3 killed=0 survived=3` (selfstate, tool sha `ca8acdd9…`) and `defects=1 killed=0 survived=1` (wave-reconcile, sha `d9336fcd…`); `CONTROL: GREEN`, byte-identical restore |
| After | `SELFSTATE_SELFTEST: 17/17 pass`; `WAVE_RECONCILE_SELFTEST: 24/24 pass`; `defects=4 killed=4 survived=0` and `defects=13 killed=13 survived=0`, `CONTROL: GREEN`, byte-identical restore |
| Kill matrix | `ss-bom-strip`→arm15, `ss-cache-key-drops-argv`→arm16, `python-utf8-dropped`→arm17, `python-isolation-dropped`→arm14 (unchanged), `record-unknown-root-check-removed`→arm24; wave defects 1–12 keep their round-79 arms (re-derived by `T80W1SC2`, confirmed by `T80W1R2`) |
| No-harm | `noharm-ss-arms.diff` = exactly `14a15,17`; `noharm-wr-arms.diff` = exactly `23a24`; every base arm outcome identical |

Sourced on **S308** (PEP 540). Locale limit (measured, `T80W1SC2`): under
`LC_ALL=C` the POSIX locale enables UTF-8 mode, so arm17 pins
`en_US.UTF-8` for the CLI it spawns; on a host without a non-POSIX UTF-8
locale the arm fails visibly (the pristine run prints 0/1), never vacuously.

### R80-C3 — verifies (measured)

```sh
python3 -I -X utf8 tools/receipt-bytes-bind.py --selftest | tail -1
python3 -I -X utf8 tools/receipt-bytes-bind.py --repo . --root .ufo/evidence | tail -1
```

| | value |
|---|---|
| Before (base instrument, sha `8d9f9d76…`) | `RECEIPT_BIND: receipts=22 bound=14 corrected=8 unbound=0`, exit 0, **no design field** — seven round-79 design receipts invisible |
| After | `RECEIPT_BIND: receipts=29 bound=14 corrected=8 design=7 unbound=0`, exit 0; `RECEIPT_BIND_SELFTEST: 13/13 pass`; the seven added rows are exactly the round-79 design receipts (`T80W1E3` independently: "original 22 row lines unchanged") |
| Kill rule | base 22/no-design PASS; after 29/design 7 PASS; selftest 13/13 PASS; marker-absent, duplicate-marker, all-malformed, CRLF, Windows-path, mixed-block and unresolvable-base forms measured (arms 1/6/10/12/13) PASS |
| No-harm | `noharm-rb-arms.diff` (base arms 1–10 vs landed arms 1–10) is empty |

Documented limits: the 64 KiB header window; manifest argv/instruments are
trusted executable input (no shell, inherited env, no process-group
guarantee); CFRL is normalised, not refused.

## Sources & frontier

Census command (both runs, exit codes pasted):

```sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tameshi
```

- **Before:** exit 0, `tameshi ok …/corpus/SOURCES.md`, 167 rows
  (`census-before.txt`; run against a base mirror so the exit code is the
  base state's).
- **After:** exit 0, `tameshi ok …/corpus/SOURCES.md`, 169 rows
  (`census-after-append.txt`).

Rows added by tier: **2, both tier A** — S308 (PEP 540, `mined`, opened
2026-11-04, quote "This mode is disabled by default and enabled by the POSIX
locale.", 12 words, page line 220) and S309 (`docs.python.org/3.15/library/sys.html`,
`rejected`, the round-79 refused candidate, quote "Changed in version 3.4:
Added isolated attribute for -I isolated flag.", 11 words, page line 999, flip
recorded). Rows touched old→new: **S289** re-opened 2026-11-04 07:28:43 GMT,
byte-identical to the round-79 snapshot, `used-by` `… round-61.md,
round-64.md, round-79.md` → `… round-64.md, round-79.md,
round-80.md` (no other cell). Registry status now: 136 mined · 22 queued ·
11 rejected; tiers A 151 · B 14 · C 4.

Frontier rows advanced: **none** — round 80 is a capability/coverage move, not
a frontier→core entry (no new `corpus/knowledge/` entry, so no coverage-map row
is owed). Scope nuance recorded: cat-file(1) defines `<type>`/`<object>`;
`:<path>` spelling lives in gitrevisions[7] (S091), so C3's binding sentence
names both.

**Assimilation: none.** Connector `T80W1CN1` re-derived the staged package:
103 staged rows, 8 id collisions (`S153`–`S160`, same ids / different
documents), 95 id-disjoint rows (`S161`–`S255`) that are a namespace fact, not
an adoption-ready subset; no staged bytes were touched. `considerthese/2026-10-28`:
proposals 1–3 and 5 are implemented; proposal 4's second point (backlog
burn-down rate on the pinned 81-entry denominator) stays open as the bounded
later-round move.

## Trend verdicts

- **expansion — improved.** A capability row enters `SCORECARD.md`
  (`registry-home figure binding`, first-working round 80, evidence
  `c1-after-sweep.txt` + `c1-selftest.txt`) and the registry gains two opened
  tier-A rows (one mined, one rejected) on ground the lane did not hold; no
  frontier row moved and no entry claimed a bar it failed.
- **quality — improved.** Two counters and one verifier were hardened and
  measured: `rows=7 match=0→7`, `defects 0/4 → 4/4` and `0/13 → 13/13`, design
  class `22 → 29` with `design=7`; the wave's nine bypass findings (CRLF,
  malformed/marker duplicates, live ambiguity, manifest confinement, Windows
  paths, empty declarations, population blind spots) are folded into existing
  arms with the frozen counts intact and re-measured; base arms byte-identical.
- **discernment — improved.** Non-author seats disagreed productively: the
  critic recorded the C1 separability disagreement and the frozen-count
  objection, resolved by folding (not by changing the rule); the sentinel's
  must-fix set F1–F5 was folded and its report stays scoped to its pinned
  hashes; the mutation-tester's two real survivors are named for round 81
  rather than hidden; the scout corrected the S308 word count and the S289
  two-source ground; the rejected row is on record. Outside promotion review
  is still owed — no promotion is claimed.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SHONEN.md` box 1 pointer resolves (`reports/round-1-calibration.md#box-1`); lane assertion, no independent promotion verifier.
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md` Round 80 entry; lane assertion (`SHONEN.md` box 2 pointer), no independent promotion verifier.
- [~] Instructions executable by an agent without oral context — input-keyed cold-read monitor; `.ufo/evidence/round-80/coldread-after-rekey.json` (66/66 sections, score 8, box3 true at `93991f1a`) is the evidence; no independent promotion verifier.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` unchanged; C2's S308 and C3's S289 are in-province; sibling overlap reported (kama's `round43-registry-audit.py` holds a related primitive; tameshi C1 is a distinct cross-surface population). Lane assertion.

## Round extras

- **Stale-lane:** no other mission of this lane is open; the driver is
  respawn-per-round.
- **Seats / dead seats:** 13/13 settled, 0 dead, no replacement.
- **Residual call:** none.
- **Tool installs:** none (python3 3.14.8, git, node, curl already present;
  pacman pause respected).
- **Misroot sweep:** `git -C /home/vgpnk/Projects/shokunin status --porcelain`
  shows only orchestrator-owned `.scratch/` and a foreign `after` file (dated
  2026-11-03, another lane); no tameshi seat wrote into the fleet root.
- **Inherited state:** the lane was clean at base; no inherited leftovers.
- **Open L0 questions:** none.
