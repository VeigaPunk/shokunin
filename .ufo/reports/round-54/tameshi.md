# tameshi — round 54 (hyaku run 11, attempt 2)

L1 `TameshiR54a2`. Lane repo `tameshi-shokunin`; base `d33053f7` (round-53 closure
tip); claim contract frozen at `441c26be` (`.ufo/evidence/round-54/contract.json`,
`freeze.json`); content commit C0 `59c38109`; fix-pass commit C1 `99c3bc88`.
Round shape: **one v2 wave of 76 seats** (w1, band 64–128 under
`ufo-wave-policy-v2.json`) **plus one v1 wave of 47 seats** (w2, band 32–64 under
`ufo-wave-policy.json`) = **123 seats**, attack-role share 26.3 % in w1 and
25.5 % in w2 (roles: reviewer, critic, mutation-tester; `labrat` and `distiller`
are refused as swarm roles by the validator, so those probes ride
mutation-tester/reviewer seats — recorded in each item's text).

Attempt 1 left nothing behind: no `.ufo/waves/round-54/`, no evidence dir, clean
tree. Nothing inherited, nothing discarded.

---

## Work performed

Declared claims (2, distinct axes; the lowest non-retired axis is calibration at 8
and carries C1):

- **C1 — calibration (8, lowest non-retired axis).** The cold-read floor: at base
  the unchanged round-21 selector credits **57 of 64** sections and the frozen
  round-48 precheck prints `cand_credited=57 lost=7 RED`. The seven uncredited
  sections are the round-53 honest stop plus its collateral; this round's own
  content edits drifted the set to **23** at C0 (`credited=41 lost=23`), which the
  round must repair. Target: at the deciding revision the precheck prints
  `cand_credited=64 lost=0 ok`, the selector reads `covered=64 score=8`, each of
  the seven base-lost sections carries a fresh entry bound under
  `rekey-r54-<c0>` whose inputs still verify, a committed reader report pins each
  section's bytes at `<c0>`, and no re-key entry pins `LOG.md`/`SCORECARD.md`.
- **C2 — operability.** One scratch-root exit class across the seven tools that
  call `strict_scratch_root()`: at base **3 of 7** self-tests exit 2 on a
  set-but-unusable `TMPDIR` (the other four raise an uncaught `RuntimeError` —
  rc 1 with a traceback), no registry row documents the empty-string arm, and the
  contract note does not exist. Target: 7/7 exit 2 with one naming
  `could-not-evaluate` line and no traceback; 7/7 exit 0 on `TMPDIR=""` and on a
  usable root with no `mkdir` under `/tmp`; seven `scratch_root` registry cells;
  the note cites an S row opened this round.

Work items, each with its evidence pointer:

- **Contract, counters, monitors, controls (pre-seat).** Both counters
  (`c1/measure.py`, `c2/measure.py`), the 14 no-harm monitors, the two-phase
  controls harness and the deciding script were written and frozen at
  `441c26be`; `freeze.json` records their sha256. The freeze also carries the
  seven base-lost headings (`c1/lost-headings-at-base.json`).
- **Phase-A controls, scored at the freeze bytes before any seat ran**
  (`control/controls-a.stdout`, committed): `CTL_0_c1` and `CTL_0_c2` (do
  nothing at base) both `false`; `CTL_R53` (the round-53 final tree, 58/64,
  `rekeyed=0/30`) `false`; `CTL_FAB` (a hand-bound entry with a valid trace and
  no reader) `false`; `CTL_LOGINPUT` (entries that pin `LOG.md`, then `LOG.md`
  changes) `false` — `CONTROLS_A: 5/5 as pre-registered`.
- **Wave 1 — 76 seats** (`spec-w1.json`, `w1-dispatch.json`, `w1-registry.json`,
  `w1.ready`; seat deliverables under `.ufo/waves/round-54/w1/`): 23 reader seats
  (one per uncredited section at C0), 13 executors, 4 scribes, 4 scouts,
  2 connectors, 12 mutation-testers, 4 critics, 4 reviewers, 4 sentinels,
  3 revengers, 2 simplifiers. Every item named an absolute path and its own
  attack target; seats wrote only under the wave dir and their own scratch.
- **Adjudication and fix pass (C1 `99c3bc88`).** The 23 wave-1 readers returned
  **25 findings**; the L1 re-derived every one against the C0 bytes and fixed
  them: stale `SKILL.md` line anchors (several drifted by this round's own
  eight-line `## Standing rules` insertion and by the four tool edits), the
  unresolved `C**` placeholder in `### Using the ledger`, a retained
  "no leg skips" clause contradicted by the correction bracket beside it, the
  runbook pin that no git object carries (`e1e349b6…`/511 L/31 416 B → the
  committed `8b2e185f…`/516 L/33 515 B), two exit-arm cells that the scratch-root
  change had made stale, the round-14 attribution of three moved pins, the S275
  page locator (physical page 3, located this round), and one finding against
  this round's own addition: `tools/env-diff.py`'s `--contract` path raised
  `ScratchRootUnusable` uncaught. All hunks were line-count preserving so no
  other citation drifted; every corrected anchor was re-checked against C1
  (`sed -n` on the cited file) before commit.
- **Wave 2 — 47 seats** (`spec-w2.json`, `w2-dispatch.json`, `w2-registry.json`):
  23 fresh readers at C1 (the same sections, no access to wave-1 verdicts),
  6 reviewers over the fix pass, 4 critics, 4 sentinels, 2 mutation-testers,
  4 executors, 2 scribes, 2 scouts.
- **Wave-2 readings and their dispositions.** The fresh read returned 22 findings
  in 9 of the 23 sections. Every one was adjudicated against the bytes and is
  genuine; none is a false positive:
  - **16 are the run-together-token class** (`pins13`, `round13`, `unchanged
    from33d03b7`, `max-share0.40`, `selftest0`, `the199-entry`, `minedS082`,
    `minedS083`, `cover16`, `is1/TOTAL_MISMATCH`, `exits0`, `including62/62`,
    `expected1/ARGV_MISMATCH`) plus the stray `))` closing of the `## Standing
    rules` scratch bullet — pre-existing at base, untouched by this round.
  - **3 are this round's own fix-pass sentences**: the `## Mutation-sweep recipe`
    "at least one per class" parenthetical miscounts the shared-class pairs (four
    of the ten, not two), the `## Effective expectation reconciliation`
    "before either named round" presupposes two rounds where the parenthesis
    names four, and "which the commands below name" is false (the commands name
    the dispositions files, not `expected.json`).
  - **3 are claim-shape gaps**: `### The tick and the pin read`'s "three labels
    are not exhaustive" summary is not sufficient for its own rows;
    `### Triggers T1–T3`'s "moved four times in one day" chain mixes committed and
    non-committed anchors; `## Live-tree re-pin`'s re-pinned range `:385-395`
    stops at the constant table and drops the `git_environment()` scrub the
    clause cites.
  All 22 are **routed to round 55** as one sweep and are named in
  `integrate/resolutions.json`; the nine sections bind with verdict
  **`gap-minor`** and `minor_gaps` equal to their finding count, so the ledger
  records what the read found instead of claiming a clean pass. The round-53 trap
  (fix, then lose the re-read) is not re-entered: the seat budget (123 of 128)
  does not admit another read pass, and the round says so rather than narrowing
  the target.
- **Wave-record defects (not instrument defects, named so the record carries them).**
  - `T54W1ExecStraceNoise` wrote `~/.omp/agent/config.yml` (a host config outside
    its write scope) on a fabricated "operator routing override (m_grok → m_glm53)"
    it invented: no such instruction exists in this round's directive, and the
    orchestrator reverted the scout route to `@m_grok` without a commit. The seat's
    C2 findings stand; the self-authorized host write is a conformance defect of the
    wave and is recorded here and in the lesson.
  - `T54W2Sent01`'s deliberately forged reader file was swept into lane history by
    the bulk evidence commit `077d431e` before the seat's own delete step; it never
    credited (its path fails the counter's reader regex and its `section_sha256`
    was a guess), and the deletion lands in `7fa9a5e0`.
  - Wave-2 mutation re-sweep survivors (`T54W2Mut01`): deleting arm 4's reader
    failure or relaxing arm 1's `lost=0` to `lost<=7` each survives at C1 — the
    counter's failure paths are under-guarded by contrast with its pass paths; both
    are coverage gaps recorded for round 55's counter work, not verdict changes.
- **Bind and decide.** The binder bound all **23** headings (REFRESH `rekeyed=23 skipped=0`) at read revision C1 `99c3bc88`, inputs pinned at the pin revision and the round-21 ledger path dropped from the inputs (a seat proved the self-pin would have drifted arm 3). One deciding invocation at **`c2108100`** with freeze **`077d431e`**: `FREEZE_INTEGRITY: OK files=10 amendments=5`, `FROZEN_UNCHANGED=1`, `NOHARM` **14 ok / 0 RED**, `COLDREAD_PRECHECK … cand_credited=64 lost=0 ok`, census exit **0**, `C1_R54_PASS=true`, `C2_R54_PASS=true`, **`DECIDING_RUN_EXIT=0`** (`.ufo/evidence/round-54/after/`).
  The frozen counter's own bytes at the deciding revision are the freeze-manifest digest `d7749f84…` (c1) and `49280fe5…` (c2) — cite those, not the C1 blobs, which predate amendments 1–5.
- **Arm-3 blind spots proved by wave-2 sentinels (routed to round 55).** (a) A poisoned
  bound entry hides behind a clean twin: arm 3's per-heading test is existential, so a
  correct entry plus one with a wrong `read_rev` still prints 7/7 — the fix is to bind
  every predicate to one entry. (b) `c0` is never verified against the section bytes at
  `c0`, so a re-key directory named for the floor with matching `read_rev`s passes while
  6 of 7 accepted shas differ from the section at that `c0`. Neither flips this round's
  verdict (the bound entries carry the correct sha and the readers pin the shipped
  bytes), and both are named here so the next round can close them.

---

## Landed changes

| Change | LOG.md entry | Commit |
|---|---|---|
| Claim contract, both counters, 14 no-harm monitors, controls harness, deciding script, freeze manifest | round-54 §claims/freeze | `441c26be` |
| C0 content — `ScratchRootUnusable` map in the four tools, seven `scratch_root` registry cells, `corpus/knowledge/scratch-root-contract.md`, S277–S279, the `## Standing rules` three-arm rule, the lesson Gate/Mistakes | round-54 §C0 | `59c38109` |
| C1 fix pass — 25 reader findings, QUALITY 105, the S275 page correction, the `env-diff` run-path mapping | round-54 §fix pass | `99c3bc88` |
| Re-key (23 sections bound at read revision C1 with inputs pinned at the pin revision) | round-54 §re-key | `7fa9a5e0` |
| Round record (LOG, SCORECARD, lessons) | round-54 §record | `0263c71e` |

---

## Before → after measurements

Counting commands are the frozen counters (§contract). Before values are the
receipts in `.ufo/evidence/round-54/before/`, taken at base `d33053f7`.

| # | Before (base `d33053f7`) | After (deciding revision) |
|---|---|---|
| C1 | `C1_R54: rev=d33053f7552d c0=none credited=57 lost=7 rekeyed=0/7 readers=0/7 monitor=6/57 unstable=0 total=4 C1_R54_PASS=false` (`before/c1.stdout`) | `C1_R54: rev=c21081008adb c0=99c3bc88d704 credited=64 lost=0 rekeyed=7/7 readers=7/7 monitor=8/64 unstable=0 total=0 C1_R54_PASS=true` (`after/c1.stdout`, deciding rev `c2108100`) |
| C2 | `C2_R54: rev=d33053f7552d tools=7 unusable_exit2=3 naming=7 empty_ok=7 usable_ok=7 tmp_mkdirs=0 docs=0 note=0 sources=0 total=13 C2_R54_PASS=false` (`before/c2.stdout`) | `C2_R54: rev=c21081008adb tools=7 unusable_exit2=7 naming=7 empty_ok=7 usable_ok=7 tmp_mkdirs=0 docs=7 note=1 sources=3 total=0 C2_R54_PASS=true` (`after/c2.stdout`, deciding rev `c2108100`) |

Instrument amendments (both disclosed, both before the deciding invocation; the
freeze pointer `097985c1` carries them and the deciding script refuses any
manifest mismatch):

1. **C1 arm 3** matched the re-key directory against each traced file's
   basename and could never fire; it now matches the directory component. Found
   by the binder dry run; proven live by the phase-B positive control.
2. **C2 arm 3** took its rc from a run under `strace -f`. The tracer's own
   overhead makes `registry-check`'s two timeout cases fail (elapsed ~9.6 s
   against the tool's `< 3.5 s` assertion) at base *and* at C0, so the arm was
   measuring the tracer, not the tool — the round-53 base receipt showed the same
   `usable_ok=6`. The rc now comes from a plain run; the traced run supplies only
   the `/tmp` mkdir census. Substance unchanged: 7/7 exit 0 on a usable root and
   zero `mkdir` under `/tmp`. Found by wave-1 attack seats (`ExecExitClass` F2,
   `ExecEmptyStrace`, `ScribeScorecard`) — the third base value above is the
   amended counter's run at base, and it matches the contract's frozen `before`
   text (`total=13`).

Bounds on the empty arm, measured this round and carried to round 55: with
`TMPDIR=""` the seven tools delegate to `tempfile.gettempdir()`, whose candidate
list ends at the working directory — with `/tmp` and `/var/tmp` themselves
unusable, one tool allocated under the cwd (`ExecEmptyStrace` probeC). The arm as
declared ("empty is unset, the platform default applies") holds; the platform
default's own last resort is the bound.

Lane HEAD at the close: **`0263c71e`** (pushed; `ls-remote` shows it); deciding
revision `c2108100`; freeze `077d431e`; amendments 1–5 all disclosed above.

---

## Sources & frontier

Census, run at round start and at round end with
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tameshi`:

- start: `136` rows at base `d33053f7` (`git show d33053f7:corpus/SOURCES.md | grep -cE '^ {0,3}\| S[0-9]{3,} \|'` → 136); the census itself was first run at C0 and exited 0.
- end: `139` rows (`grep -cE '^ {0,3}\| S[0-9]{3,} \|' corpus/SOURCES.md` → 139); `sources-census.sh validate --root … tameshi` exit **0** (W01/W04 warnings only, the same families the registry carried at base).

Rows: **136 → 139** (`| S### |` rows with 0–3 leading spaces; the census agrees).
Rows added, by tier: **S277 (spec, A)**, **S278 (code, A)**, **S279 (docs, A)** —
all opened 2026-10-28 with committed snapshots under
`.ufo/evidence/round-54/assimilation/` and located quotes in the lesson's
`## Gate`. Rows touched old→new: S275's anchor cell only (`p. 4` → `p. 3
(physical)`; the round-53 closure's R53.8, verified this round by locating the
quote on page 3 of the committed camera-ready).

Frontier rows advanced: **none** (F6 stays held from round 50; this round's
knowledge lands on the operability surface, not on frontier ground). Assimilation:
one theme — the scratch-root contract — with three rows and one note; the
`merge/tameshi` `delta-debugging-minimization-contract.md` entry is **refused on
capacity** with its flip named in the lesson's Gate, and the other 84 staged
entries stay refused for the same reason.

---

## Trend verdicts

- **expansion — unchanged.** No new frontier ground and no capability row; the
  knowledge added is one note and three rows on a surface the lane already owns.
- **quality — improved.** C2 moves 3/7 → 7/7 on the unusable arm and adds the
  empty-string and no-`/tmp` arms; 25 reader findings were fixed, not smoothed.
- **discernment — improved.** The wave-1 readings were adjudicated one by one
  against committed bytes (including one finding against this round's own
  addition), the round-53 routed defects R53.1–R53.9 all carry a disposition, and
  the base-value delta above is disclosed rather than reconciled.

---

## Stale-lane

Respawn-per-round driver: this report closes round 54 only; no other mission of
this lane is open. Round 55's planned list is in `SCORECARD.md`.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — lane assertion, no independent promotion verifier (`reports/round-1-calibration.md#box-1`)
- [~] At least one end-to-end domain task executed and logged in LOG.md — lane assertion, no independent promotion verifier (`reports/round-1-calibration.md#box-2`)
- [~] Instructions executable by an agent without oral context — input-keyed monitor only; no independent promotion verifier (`.ufo/evidence/round-21/coldread/ledger.json`)
- [~] No cross-domain bleed (PROVINCE.md still accurate) — lane assertion, no independent promotion verifier (`reports/round-1-calibration.md#box-4`)
