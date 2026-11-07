# mado — round 98 report

Lane `mado-shokunin`, hyaku run 15, round 98, attempt 1 (`MadoR98`). Lane repo
`/home/vgpnk/Projects/shokunin/mado-shokunin`, branch `master`, base
`35f3ce808788b11c063309b1b5ad0192754795ea` → lane tip `6f61eff075243f564d1e7eed4823d7c521388a42`
(pushed; `ls-remote` prints it). Report committed by `fleet-commit.sh --as mado`.

## Work performed

The round declared **two claims** (`.ufo/waves/round-98/claims-declaration-r98.md`, frozen at the
artifacts commit `06b6bf2a`, its `## Freeze block` carrying every pin):

- **C1 — coverage (capability, new surface):** the sequence of argv vectors GIO 2.90.1 builds and
  spawns from a desktop entry's `Exec` key and a file/URI list. Tool `tools/mado-execargv.py`,
  counter `quality/counters/c1-r98-execargv.py`, 88 frozen cases over 20 classes, 79 counted mutants,
  a seeded fresh leg.
- **C2 — operability:** the SOURCES registry's citation read-back. Gate
  `quality/check-sources-readback.py`, counter `quality/counters/c2-r98-sources-readback.py`, and the
  21 unacknowledged entry→row citations it found, repaired row → entry.

Work items (each with its evidence pointer):

- **C1 surface modelled and measured.** `tools/mado-execargv.py` (`49f7fecd…f713`) answers the launch
  sequence: the load gate and its five refusal shapes (`no-exec`, `desktop-file`, `exec-parse`), the
  byte walk with the selector byte consumed, the twelve field codes and `%%`, `force_file_uri` and
  `X-GIO-NoFuse`, the head-pointer no-substitution `%f` append, `g_shell_quote`, the
  `g_shell_parse_argv` grammar, and the `do { } while (dup_uris != NULL)` loop that spawns once per
  URI for the single-consuming codes. Measured `TARGET_MET` at `a3471631`:
  `.ufo/waves/round-98/receipts/c1-measured-r98.txt` — `cases=88 correct=88 classes=20/20`,
  `mutants=79 killed=79/79 class_kills=20/20`, `fresh=60/60` at seed `f00d3edcdb285ac0`,
  `control_naive=4/88 control_fieldcode=47/88 memoriser_fresh=0/60`, `selftest checks=38 failed=0`.
- **C2 gate and repair.** `quality/check-sources-readback.py` (`f1000bf1…d8f5`) reports R1 (a repo path
  in a `recheck` cell), R3 (a dangling `used-by`), R4 (a `mined` row an entry cites but whose
  `used-by` does not name the entry), R5 (a cited id with no row) and R6 (a duplicate id). Measured
  `TARGET_MET` at `a3471631`: `.ufo/waves/round-98/receipts/c2-measured-r98.txt` — base
  `base_mismatches=21` (pinned), rev `gate findings=0` over 466 rows / 119 entries, `repaired=21/21`,
  `added_paths=21`, `planted=5/5`, `stub_flagged=1`, `census=ok`, gate selftest `checks=21 failed=0`,
  counter selftest `checks=18 failed=0`.
- **The 21-cell repair** (`corpus/SOURCES.md`, commit `06b6bf2a`): 16 `used-by` cells over 21 paths,
  plus `S504`/`S506`/`S527` gaining `corpus/knowledge/gio-exec-argv-r98.md`; the old → new log is
  `.ufo/waves/round-98/controls/readback-repair-log-r98.json` (derived base → final, 23 changed cells,
  24 added paths). The two disowned citations (S030 `rejected`, S132 `queued`) are recorded in the
  lesson with their entries' sentences and are **not** repaired.
- **Entry and index.** `corpus/knowledge/gio-exec-argv-r98.md` (690 lines; every rule cites a located
  line of S528-S531/S504/S506/S527 or an oracle-labelled probe row); `corpus/README.md` index row and
  frontier bullet; `corpus/README.md` coverage `119/119` (`MADO_INDEX … coverage=10.0000/10`).
- **Registry.** SOURCES 462 → 466 rows: S528 (`gdesktopappinfo.c` launch expansion), S529 (`gshell.c`
  quoting/tokenizer), S530 (the Desktop Entry Specification's Exec section), S531 (the installed
  `gio(1)` `launch` scope), all tier A; census start rc 0 / end rc 0
  (`receipts/census-start-r98.txt`, `receipts/census-end-r98.txt`).
- **Records.** `SCORECARD.md` round-98 section (two TARGET_MET rows, capability row, named limits,
  round shape); `LOG.md` round-98 entry; `corpus/lessons/round-98.md` (M98-1…M98-12, Gate block,
  census); `PROVINCE.md` round-98 refinements (C1 and C2, read-only, no new write surface);
  `SKILL.md` registry rows for the four instruments; `quality/tool-ledger.md` four rows
  (`LEDGER: population=195 ledger_rows=195 uncovered=0` at `020af865`).
- **Round-97 routed defects:** D1 (report ordering) — this report lands after the lane tip; D2 (role
  census) — reported from the registry below; D3 (dead-seat line) — no dead seats this round, and the
  round-97 seat reports exist; D4 (D7/D9 closure) — closed append-only in `corpus/lessons/round-98.md`
  §Gate (D7: the r96 declaration's rationale text is corrected by the round-98 C2 restatement; D9: the
  census is reported from the registry, and the round-97 w1 registry holds 6 executors, not 3); D5
  (S523 old→new log) — logged in the lesson; the read-back gate is the requested instrument; D6 (fleet
  leftovers) — `f.txt` and `trail-ids.txt` swept byte-exact into `.ufo/waves/round-98/misroot/` and the
  fleet copies deleted (M98-6); D7 (carried r95 defects 1/2/4/5) — still open, re-flagged below.

## Landed changes

| Change | LOG entry | Commit |
|---|---|---|
| `tools/mado-execargv.py`, `quality/check-sources-readback.py`, `quality/counters/c1-r98-execargv.py`, `quality/counters/c2-r98-sources-readback.py`, the frozen cases/mutants/fresh/probe/planted controls, the frozen declaration, the 21-cell registry repair | LOG round 98, C1/C2 bullets | `06b6bf2ab0e60b37db6ec1aadeb91ecf9f30289f` |
| The file-URI encoding fix (`g_filename_to_uri`'s path-safe set) and the re-frozen tool/mutant pins | LOG round 98, C1 bullet (the fresh-leg gap) | `a347163144215d4a05573a5672327aa0cf8daa93` |
| The entry, index, SOURCES rows and repair log, the lesson, SCORECARD/LOG/PROVINCE/SKILL/ledger records, the measured receipts | LOG round 98, all bullets | `020af865da6621eaa869ade6f7f8d0713e53452a` |
| The wave's build drafts and the harm watch at the records tip | LOG round 98, harm bullet | `24ced668adb244dbf9153433136825bd9d116352` |
| The first harm run's completed receipt and both receipts' nonzero-leg notes | LOG round 98, harm bullet | `b3c8e134973769099564b331f292ef1d20ec29fc`, `fa4445af451baadb402e7c40695473d3a512f694` |
| The round-97 spot-check's D5/D6/D7/D9 closure block in the lesson | LOG round 98, routed-defects bullet | `6f61eff075243f564d1e7eed4823d7c521388a42` |

## Before → after measurements

**C1 — coverage.** Counting command (the declaration's C1 block, verbatim pins):

```
python3 -I quality/counters/c1-r98-execargv.py --repo . --rev a3471631… --base-rev 35f3ce80… \
  --cases .ufo/waves/round-98/controls/execargv-cases-r98.json --expect-cases-sha256 21cccc3a… \
  --mutants .ufo/waves/round-98/controls/execargv-mutants-r98.json --expect-mutants-sha256 32c207b3… \
  --genseed .ufo/waves/round-98/controls/execargv-fresh-r98.py --expect-genseed-sha256 b7bc137a… \
  --expect-tool-sha256 49f7fecd… --expect-gio-sha256 d2164260… --scratch-root DIR
```

Before: at base `35f3ce80` no lane tool answers a launch argv (`git cat-file -e
35f3ce80:tools/mado-execargv.py` → absent; the counter prints `base: tools/mado-execargv.py absent at
base-rev …`). After: `TARGET_MET` at `a3471631` — 88/88 cases, 20/20 classes, 79/79 mutants, 20/20
class kills, 60/60 fresh, controls behind, selftest green. Receipt `receipts/c1-measured-r98.txt`.

**C2 — operability.** Counting command:

```
python3 -I quality/counters/c2-r98-sources-readback.py --repo . --rev a3471631… --base-rev 35f3ce80… \
  --expect-gate-sha256 f1000bf1… --expect-base-mismatches 21 \
  --planted-dir .ufo/waves/round-98/controls/readback-planted \
  --fleet-root /home/vgpnk/Projects/shokunin --scratch-root DIR
```

Before: at base no read-back gate exists (`git cat-file -e
35f3ce80:quality/check-sources-readback.py` → absent) and the status-aware R4 rule counts 21
unacknowledged citations (`receipts/c2-base-mismatches-r98.txt`). After: `TARGET_MET` at `a3471631` —
gate findings 0, repaired 21/21, added_paths 21, planted 5/5, stub flagged, census ok. Receipt
`receipts/c2-measured-r98.txt`.

**Separability.** C1 counter at the base → `SETUP_ERROR … tools/mado-execargv.py absent at 35f3ce80`
(`receipts/c1-at-base-r98.txt`, rc 2); C2 counter at the base → `SETUP_ERROR gate-absent-at-rev`
(`receipts/c2-at-base-r98.txt`, rc 2). Each instrument fails without its own artifact and passes with
it; the shared artifacts commit is a landing convenience, not a dependency.

**Harm watch.** `receipts/harm-final-r98.txt` at `fa4445af`: the round-97 leg set replayed at the
records tip (gate selftest, file plane, index, ledger, every tool selftest, the gate kill-sets, the
prior counters), with `r90c1_portal_routing` the declared `rc=2` SETUP_ERROR since round 93, and four harness/pin
legs explained in the receipt's note (two r95 legs have no counting-command argv in the harness, the
r96 C1 leg carries its known stale pin, and the r97 C2 leg's argv carries an unfilled
`SKILL-AT-MEASURED-REV` placeholder). No axis harmed.

## Sources & frontier

Census: `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin mado` — start rc 0 at
base `35f3ce80` (462 rows, 62 W04 warnings, no E-codes; `receipts/census-start-r98.txt`), end rc 0
(466 rows, 64 W04 warnings, no E-codes; `receipts/census-end-r98.txt`).

- Rows added by tier: **4 tier-A rows** — S528 (GLib 2.90.1 `gdesktopappinfo.c`, the launch expansion
  and spawn loop), S529 (`gshell.c`, `g_shell_quote` and the tokenizer), S530 (Desktop Entry
  Specification, "The Exec key"), S531 (installed `gio(1)`, the `launch` scope).
- Rows touched old → new: 23 changed cells, 24 added `used-by` paths
  (`controls/readback-repair-log-r98.json`): 16 repaired cells over 21 paths (S457, S459, S460, S464,
  S465, S466, S470, S481, S484, S485, S493, S501, S502, S511, S512, S517), plus S504/S506/S527 gaining
  the C1 entry, plus the four new rows. S030 and S132 stay unrepaired (disowned citations, quoted in
  the lesson). S523's round-97 repair is logged old → new in the lesson.
- Frontier rows advanced: the launch argv (the frontier half of "launch" named since round 91) moves
  into core; whether the process starts, `Terminal=true`, `Path=` as cwd, DBus activation and the
  portal path stay frontier.
- Assimilation: none (the staged `merge/mado/` package has no entry on the launch plane; the id
  collision check is not applicable because nothing is adopted). considerthese: no
  still-unimplemented proposal matched this round's surface.

## Trend verdicts

- **expansion — improved.** A new admitted entry (`corpus/knowledge/gio-exec-argv-r98.md`) on ground
  the coverage map did not hold (the launch plane's argv half), index 119/119, four new tier-A rows,
  and a capability row entered with the demonstrated run (88/88, 79/79, 60/60).
- **quality — improved.** C1 replaces "no lane tool answers a launch argv" with a measured sequence
  model and four controls behind it (naive 4/88, field-code 47/88, memoriser 0/60 fresh, and the
  oracle's two-measurement label rule); C2 replaces "no read-back" with a gate, five planted controls
  and a 21-cell repair. The harm watch replays every prior instrument at the records tip.
- **discernment — improved.** Twelve mistakes are mined with a witness each (M98-1…M98-12, including
  the oracle's shared-file race, the counter/oracle materialisation drift, a refusal label that could
  not be materialised, the launch-order race, and the declaration's `%i` guard); the wave reversed
  seven of the L1's own sentences before the freeze (the `#` branch, `Hidden`, the selector byte, the
  non-local URI rules, the head-pointer fallback, the icon strip, the order rule), and the fresh leg
  caught a model gap the frozen cases did not (the file-URI encoding) — fixed and re-measured.

## SHONEN

- `[~]` SKILL.md contains real decision tables, error patterns, checklists, cited sources — the four
  round-98 registry rows name the instruments and their verdict maps (`SKILL.md:2979-2982`); the
  outside-lane promotion authority is still absent.
- `[~]` At least one end-to-end domain task executed and logged in LOG.md — the C1 measurement is an
  end-to-end run of the tool against the installed oracle (`receipts/c1-measured-r98.txt`, LOG round
  98); no outside-lane verifier has ruled on it.
- `[~]` Instructions executable by an agent without oral context — the declaration's shared contracts
  and the entry's sections carry the commands; a dispatched seat is still the lane's own work.
- `[~]` No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` gains the two round-98
  refinements (read-only, no new write surface); the connector's 20-lane sweep found no sibling claim
  on either surface (`w1/R98MConnector.md`).

## Round shape, seats and limits

One v1 wave `w1` of **11 seats** (registry census: 4 executor, 2 mutation-tester, 1 scout, 1 scribe,
1 connector, 1 reviewer, 1 critic; attack 4/11 = 36 %). No residual call. No dead seats (all 11
reports exist in `.ufo/waves/round-98/w1/`). Round total 11. The L1 holds the §3 planner seat (the
validator rejects `planner`); a bounded planning data-walk rode the scout/connector items.

Tool installs: none (no pacman transaction, no `uv`/`npx` install; `flock` and `gio` were already
present).

Stale-lane: the lane is driven by the respawn-per-round driver; no other mission of this lane is open.

## Routed defects (status-neutral; next round)

1. `quality/counters/c2-r98-sources-readback.py` is not idempotent on a reused `--scratch-root`
   (`FileExistsError … planted-r1/corpus`; M98-12) — clear or version its planted dirs.
2. The C1 counter's `FRESH_MISMATCH` line truncates the JSON (the mismatch is not readable from the
   receipt) — print the differing launch index and the two vectors.
3. Carried round-95 defects 1, 2, 4 and 5 remain open (the `mado-mime.py` HOME edges, the
   `mado-mimeglob.py` docstring citation, the gate's own selftest guard, and the QUALITY 158
   instrument gap).
4. `tools/mado-mako.py`, `tools/mado-mimesniff.py` and `tools/mado-verify.sh` remain without kill-sets
   with the gate's structural reason measured (QUALITY 153/155).
