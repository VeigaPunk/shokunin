# souji round 86 — report

Lane `souji` (`/home/vgpnk/Projects/shokunin/souji-shokunin`), base `89d02c907d40cc09fedc9d420cf9509df685e143` (r85 closed
`admitted`). Attempt 1, L1 `SoujiR86`. Round shape: ONE v1 wave of **11 seats** (policy
`scripts/hyaku/ufo-wave-policy.json`, band 8-16): executor×3, mutation-tester, scribe, scout×2, connector,
reviewer, critic, sentinel. Attack seats 4/11 (36 %, floor 25 %); connectors 1 (cap 2); dead seats 0 (the
orchestrator reported all 11 settled; `w1-results.json` carries no per-seat `status` field, so the evidence of
delivery is the 11 reports themselves, force-tracked at `1c3a1d41`). Round total 11.

**Declared claims (2).**

- **C1 — calibration 7** (the lane's lowest owned non-retired axis): two clauses r85 measured *reachable but
  unrowed* (the census-in-tree branch, r85 A1/S85Scribe F1; the own-tree short-shape guard, r85 A4/S85MutCounter
  m14) get one frozen row and one single-edit mutant each, and the population's kill count moves 6 → 8 without
  losing any of the six r85 kills.
- **C2 — operability 8**: record-agreement K4, which r85 taught to re-hash status-clean paths, now also runs the
  receipt writer's index-flag sweep (so a gitlink entry concealed under `skip-worktree` is classed) and C-escapes
  `\n`/`\t`/`\r` in a record's detail (so a path name stays on one physical line). A wave-found fail-open on the
  sweep's config view was repaired in-round.

Both are causally separable: C1's files are `census/round-86/c1-*` and the r85 population; C2's are
`tools/souji-record-agreement.py` and `census/round-86/c2-k4-counter.py`; the only shared path is the frozen
preregistration (S86Connector §1, sweep output `C1 paths: 9, C2 paths: 6, Operational overlap: set()`).

## Work performed

- **Instruments frozen (P).** `census/round-86/c1-false-rows.tsv` = the r85 47 rows byte-for-byte (verified:
  `prefix identical: yes`, `census/round-86/records/instrument-deltas.txt`) plus NF-W and NF-Y at a new fixture
  revision R9; `c1-items.tsv` = the r85 three items plus `I86S` (`SCORECARD.md:1924`, token
  `census/round-83/c1-pointer-counter.py`, the first population item one component below its round);
  `c1-pointer-counter.py` differs from r85 by **one POPS entry plus its docstring** (diff classified in
  `records/instrument-deltas.txt` and by S86ExecC1 §4); `c1-ledger.tsv` byte-identical; `c1-mutants.json` = the six
  r85 mutants byte-identical plus `c7-census-in-tree` and `m14-short-shape`; `c2-k4-counter.py` = the r85 7 rows plus
  KG1 (a nested repository whose commit moved under `skip-worktree` on its gitlink entry) and KG2 (a same-size forge
  of a file whose name carries a newline); controls `c2-before-base-tool.py` (`0ade0751…`, byte-identical to the
  tool at the lane base, `records/control-binding.txt`) with a byte-identical writer copy beside it.
  P = `47602fa6`.
- **Freeze (F).** `census/round-86/preregistration.txt` alone, `d77b4258` (`git show --name-only` = one path).
- **C2 repair.** `truth_refusal` now runs the writer's `ls-files -v -z :(top)` sweep after its truth check, classing
  the row `index-flag-concealed` for the two flag classes, and C-escapes the detail — `2acbbfc8`
  (tool `4cc3b945…`). **Wave repair** after the sentinel's finding: `git_env()` also strips `GIT_INDEX_FILE`,
  `GIT_OBJECT_DIRECTORY`, `GIT_ALTERNATE_OBJECT_DIRECTORIES`, `GIT_REPLACE_REF_BASE`, the embedded writer subprocess
  runs with that environment, and the sweep pins `core.sparseCheckout=false` — `f5e196a2` (tool `cf875367…`,
  the filed bytes). Evidence `records/c2-env-route.txt`.
- **C1 measurement.** `records/c1-after.txt` (both arms, 8 mutants, 2 populations), `controls/c1-before-r85-population.txt`
  (the do-nothing control), `records/c1-regress-r83-r84.txt` (r83 36 rows and r84 44 rows stay green; `killed_r84=5`,
  i.e. the r84 baseline unchanged), `records/pin-refusals.txt` (both pin paths refuse, rc 2).
- **A dead clause measured.** The own-tree guard's `len(got) < 2` disjunct cannot be bound: dropping only it changes
  no verdict on either population (`records/a6-len-got.txt`, `killed_r85=0 killed_r86=0`, both pristine arms green),
  and S86MutCounter's independent `x5` agrees with a 67 081-pair sweep. The connector's proposed `NF-Z` row is
  declined for that reason (A3/A8).
- **C2 measurement.** `records/c2-after.txt` (9 rows, `mismatches=0`), `controls/c2-before-base-tool.txt` (9 rows,
  `mismatches=2`), `records/c2-real-lane.txt` (a `--shared` clone of the lane at the frozen revision reports **no K4
  row**, only the inherited K3 row), `records/c2-env-route.txt` (the sentinel's env route, before/after).
- **Wave.** 11 seats, 200 files under `.ufo/waves/round-86/w1/` (force-tracked at `1c3a1d41`, the R86-2 durability
  fix), spec/dispatch/results/claims/ledger at `90afc14a`. Seat verdicts that changed the round: S86Critic (C1-c
  weaker-rule 8/8; C2-b gitlink *entry*), S86ExecK4 (the flag class split; `FLAGFAIL` unreachable; real-lane clean),
  S86MutCounter (the c7 suffix test dead; the got-half dead; all kills are mismatches, `errors=0`), S86ExecEvade
  (int-normalised round comparison green at 8/8; the six-path naming cap), S86Sentinel (the config-view fail-open,
  repaired), S86Scribe (per-row attribution; the r85 "literal LF" wording corrected to the space-join),
  S86ScoutSources (all three source rows re-opened byte-exact; the `--assume-unchanged` gap taken as S345),
  S86Connector (separability, zero sibling overlap, prior-art function audit), S86ExecC1 (pin-exit drift),
  S86ScoutShapes (shape census).
- **Docs and amendments.** `plans/round-86.md` A0-A11, `corpus/lessons/round-86.md` (Gate + seven mistakes),
  `corpus/knowledge/own-tree-pointer-binding.md` r86 section, `corpus/knowledge/filter-filemode-witness.md` r86
  section plus the r85 wording correction, `corpus/QUALITY.md` Q158-Q160, `corpus/README.md` r86 frontier block,
  `SCORECARD.md` r86 rows + two capability rows + planned r87 — `12d320dc`.
- **Misroot sweep.** `git -C /home/vgpnk/Projects/shokunin status --porcelain` = 6 entries, none written by this
  lane's seats: three orchestrator `.scratch/` files, the fleet L0 file, another lane's report
  (`.ufo/reports/round-89/chousa.md`), and the orchestrator's wrap-up dir. Nothing copied or deleted.

## Landed changes

| commit | what it carries | LOG |
|---|---|---|
| `47602fa6` | P: instruments, populations, mutants, the 9-row K4 counter, both before receipts and the control writer copy | LOG.md `## Round 86` instruments bullet |
| `d77b4258` | F: `census/round-86/preregistration.txt` alone | same |
| `2acbbfc8` | C2 repair, `tools/souji-record-agreement.py` (`4cc3b945…`) | `## Round 86` claims bullet |
| `f5e196a2` | C2 wave repair (env route), tool `cf875367…` | same, second paragraph |
| `12d320dc` | after receipts, source captures `census/round-86/srcs/`, plans A0-A11, lesson, QUALITY Q158-Q160, README, SCORECARD, SOURCES S341-S345, both knowledge sections | `## Round 86` measured/narrowed/sources/docs bullets |
| `90afc14a` | wave evidence: spec, dispatch, results, ready, claims, falsification ledger (17 rows) | `## Round 86` wave bullet (shape recorded in the lesson) |
| `1c3a1d41` | 200 wave seat files force-tracked (R86-2 durability) | same |

LOG.md carries one `## Round 86 (2026-11-08)` entry (appended, never rewritten) naming every artefact above.

## Before → after measurements

**C1 — calibration 7.** Counting command (one, both ends):
`python3 -B census/round-86/c1-clause-battery.py --counter census/round-86/c1-pointer-counter.py --work WORK --only r85,r86 --expect-killed 14`
(after) and `--only r85 --expect-killed 6` (before).

| end | receipt | observed | exit |
|---|---|---|---|
| before (do-nothing: same counter, same 8 mutants, the r85 47 rows) | `census/round-86/controls/c1-before-r85-population.txt` | `ARM pristine pop=r85 rows=47 mismatches=0 errors=0`; six `killed=yes`; `c7-census-in-tree killed=no`; `m14-short-shape killed=no`; `SUMMARY mutants=8 sets=r85 pristine_r85=ok killed_r85=6 killed_total=6` | 0 |
| after (the r86 49 rows, both populations) | `census/round-86/records/c1-after.txt` | `ARM pristine pop=r85 rows=47 mismatches=0 errors=0`; `ARM pristine pop=r86 rows=49 mismatches=0 errors=0`; eight `killed=yes` on r86; `SUMMARY mutants=8 sets=r85,r86 pristine_r85=ok pristine_r86=ok killed_r85=6 killed_r86=8 killed_total=14` | 0 |

Measured against the instrument bytes at P `47602fa6` (counter `8278ea4d…`, harness `2dac2e81…`, mutants
`6f055ede…`, populations `1468236c…`/`79db70f6…`, items `5abf3b01…`). Each new row is the **sole** killer of its
clause and neither row is red for any of the six r85 mutants (S86MutCounter §6); every kill is a status mismatch
with `errors=0` (§7). Regressions: r83 36 rows and r84 44 rows both green, `killed_r84=5` (unchanged baseline).

**C2 — operability 8.** Counting command (one, both ends):
`python3 -B census/round-86/c2-k4-counter.py --tool tools/souji-record-agreement.py --work WORK` (after) and
`--tool census/round-86/controls/c2-before-base-tool.py` (before).

| end | receipt | observed | exit |
|---|---|---|---|
| before (lane-base tool `0ade0751…`) | `census/round-86/controls/c2-before-base-tool.txt` | `SUMMARY rows=9 mismatches=2 errors=0`; KG1 `k4=0` (no row), KG2 `k4=1 named=no`; the seven r85 rows unchanged | 1 |
| after (filed tool `cf875367…`) | `census/round-86/records/c2-after.txt` | `SUMMARY rows=9 mismatches=0 errors=0`; KG1 `k4rows=['.|index-flag-concealed']`, KG2 `named=yes`; the seven r85 rows unchanged | 0 |

Measured against the tool bytes at `f5e196a2` (writer `70bbf1c2…`, counter `6438c014…`). The kill-rule clause "no K4
row on the lane's own clean tree" is satisfied by `records/c2-real-lane.txt` (clone at `2acbbfc8`, one K3 row, no
K4 row) and by S86ExecK4 §4. The wave repair is measured outside the frozen counter (whose own env strips `GIT_*`):
`records/c2-env-route.txt` reads `k4_rows_with_env=0` on the base bytes and `1` on the filed bytes on the KG1 class.

## Sources & frontier

Counting command: `grep -cE '^\| *S[0-9]{3,}' corpus/SOURCES.md` → **263 → 268** (five rows added, one rejected,
zero removed). Census: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root
/home/vgpnk/Projects/shokunin souji` → `souji ok`, exit 0 before (`records/sources-census-before.txt`, 87 pre-existing
`W04` cross-scope duplicate-URL warnings) and after (`records/sources-census-after.txt`, 87 `W04`, no `E0x`, exit 0).

Rows added by tier: tier A ×5 (`docs` ×5), tier B ×0, tier C ×0. Rows touched: none in place — the five are new rows
(S341 git-ls-files(1) `-t` tag legend; S342 git-update-index(1) skip-worktree contract; S343 gitsubmodules(7) gitlink
content; S344 **rejected** git-ls-files `--stage`, reason + flip in its own row; S345 git-update-index(1)
`--assume-unchanged` promise sentence). Re-opened unchanged: S315, S316, S317, S335, S337, S339, S340. S86ScoutSources
re-opened all three admitted sources independently (captures byte-identical, quotes located and word-counted) and
confirmed the reject against S317+S327.

Frontier rows advanced: two. `knowledge/own-tree-pointer-binding.md` r86 section — the two r85-measured
reachable-and-unrowed clauses now have rows, and the file gains the third disposition (DEAD: no input flips the
verdict) for the guard's got-half and the c7 suffix test. `knowledge/filter-filemode-witness.md` r86 section — K4
carries the writer's flag sweep, the record format escapes path names, and the sweep's config view is pinned. Neither
promotes a frontier row to Core (PROVINCE.md unchanged; F1/F2/F3/F4/F5 statuses stand). `Assimilation: none` (no
`merge/souji/` theme taken; `considerthese/` does not exist in this lane — stated as the report line the prompt
requires).

## Trend verdicts

- **expansion — unchanged.** Five source rows and one new frontier paragraph are curation and instrument power, not
  breadth: `PROVINCE.md` is unchanged (0 lines diff at the report commit), no frontier row moves to Core, and the two
  knowledge sections extend ground the map already holds (`grep -c 'r86' corpus/README.md` = the one frontier block).
  The round's gain is discrimination (8/8 kills) and a closed fail-open, not new domain surface.
- **quality — improved.** C2's audit tool now refuses a class it could not see: the concealed-gitlink row goes from
  `k4=0` to `k4rows=['.|index-flag-concealed']`, a path name survives a newline in the record, and the config-view
  fail-open the sentinel found is closed and measured (`k4_rows_with_env` 0 → 1). C1's population now kills two clauses
  it left green, with the do-nothing control proving the delta is the row and not the rule, and every kill is a
  mismatch with `errors=0`. Limits are stated rather than claimed: one arm per clause, the c7 suffix test and the
  got-half dead, the five-path naming cap, the lying-writer delegation, the inherited K3 row.
- **discernment — improved.** The round's own wave falsified seven sentences of its frozen framing before filing and
  each is narrowed in `plans/round-86.md` with the artifact that killed it: A1 (flag-row class), A2 (gitlink entry vs
  commit), A3/A8 (one arm per clause; the suffix test dead), A4 (the lane's own K3 row), A5 (`FLAGFAIL` unreachable),
  A9 (five-path cap), A10 (int-round survivor; `w0/` domain), A11 (the config-view fail-open — **repaired**, not just
  disclosed), and the r85 section was corrected from "literal LF" to the space-join. Two of the round's own proposals
  were withdrawn on measurement (the connector's `NF-Z`; a first C2 control that failed closed for want of a writer,
  A0.1) and one instrument class bug was fixed before filing (A0.2).

## SHONEN

- `[~]` SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md` Decision tables /
  Error patterns / Checklists / Gate registry; `corpus/SOURCES.md` S341-S345; `corpus/lessons/round-86.md` Gate.
- `[~]` At least one end-to-end domain task executed and logged in LOG.md — LOG.md `## Round 86` (P/F/repair/wave
  commits, both arms, the env-route repair).
- `[~]` Instructions executable by an agent without oral context — `census/round-86/preregistration.txt` + the four
  counting commands re-run by S86ExecC1, S86Reviewer, S86MutCounter and S86Scribe; receipts under `census/round-86/`.
- `[~]` No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` unchanged; S86Connector §2 sibling sweep
  (21 `PROVINCE.md` files, zero contested scope) and `corpus/lessons/round-86.md` `## Gate`.

## Extras

- **Stale-lane:** respawn-per-round driver; this lane has no other open mission. Lane tip `1c3a1d41`, remote equal,
  `ahead=0 behind=0 tracked=0 untracked=0` at filing.
- **Tool installs: none.** No pacman (paused host-wide), no `uv`/`npx`/binary fetch, no sysctl, no sudo, no host
  service change. S86ScoutSources ran `pacman -Qi git` read-only to stamp `git 2.56.0-1`.
- **PREFILE-FALSIFICATION:** `python3 /home/vgpnk/Projects/shokunin/scripts/hyaku/prefile-falsification.py --lane
  souji --round 86` → `PREFILE-FALSIFICATION: pass claims=2 rows=14 attack_seats=5 findings=0`, exit 0 (run against this
  report, the committed claims.json and the 11-seat results).
- **Open routed items for r87** (also in `SCORECARD.md` planned and `plans/round-86.md`): the c7 suffix test and the
  guard's got-half (dead — delete or document as belts), `NF-L3`/m12/m16/m17, a positive QUARANTINED row, NX3 (the
  int-round case) and the `w0/` decision, the five-path naming cap, the `FLAGFAIL`/exit-code drift (lesson M6), the
  writer's 200-character stderr cut, a pinned writer digest so the delegation limit stops being load-bearing, the
  inherited K3 tally row, and the r83/r84 C2 carried list (pid-reuse, parent-before-child, termign-fork/p5-late-term,
  strace settle).
