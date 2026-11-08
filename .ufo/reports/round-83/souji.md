# souji — round 83 (attempt 1)

Lane: `souji-shokunin`, base `1e870403c5d806a5cf9ac93b00da7a928359608f` (r82 closed `admitted`; spot-check
`corpus/lessons/round-82-verifier-spotcheck.md`). Round shape: one v1 wave of 12 seats under
`scripts/hyaku/ufo-wave-policy.json` (band 8-16); 6 attack seats (reviewer, critic, 2 mutation-testers, sentinel,
connector = 50 %). Driver: `2026-11-08T01:28:58-03:00 launch souji round=83 pgid=3657907 driver=hyaku-inline
attempt=1`; wave spawned `02:06:37` after a host-gate deferral (a foreign seat's 192 `while True: pass` load burners
held load1 ≈ 250; the operator session reaped them).

## Work performed

The round's declared claims (frozen in `census/round-83/preregistration.txt`, F `fbf0ae5e`):

- **C1 — calibration 7 (the lane's lowest non-retired axis): the pointer counter binds a MOVED token's own-round-tree
  target to a real wave directory of this lane plus the token's remaining path, per branch.** Before, the r82 rule
  named `waves/|wave/|records/wave-<w>/` while the lane's own wave trees are `w1/` (65), `w2/` (19), `w3/`, `a2w1/`,
  `assimilation/` (4) — so it refused a genuine own-tree move into a real wave directory (r82 A2 stated limit,
  S82Connector2 F1, spot-check routed defect 5 / lesson route 1).
- **C2 — operability 8: `cli_kill_tree` walks the CLI descendant tree once, fork-free, and re-checks each pid's
  starttime before signalling it.** Before, the r82 walk forked one `pgrep -P` per tree node, each a full `/proc`
  scan (F-2), and snapshotted the tree before the TERM/KILL split (F-3, spot-check route 4 / lesson route 4).

Work items, each with its evidence pointer:

- **Instruments and do-nothing controls (P `1014143d`).** New 36-row C1 population
  (`census/round-83/c1-false-rows.tsv`: the r82 32 byte-for-byte + TF6 `w2/`, TF7 `w1/`, NF-J duplicated middle dir,
  NF-K flattened round-root copy at fixture R6) and harness; new 20-row C2 population (`c2-population.tsv`: the r82
  16 with a `launch`/`children` column plus four deep rows) and counter; byte-identical r82 tool control
  (`controls/c2-K-a-r82-tool.sh`, sha256 `dd6d440e…`); the real wave-directory census
  (`census/round-83/records/wave-dirs.txt`). Control receipts: `controls/c1-K-a-r82-counter.txt` (`mismatches=2
  accepted=0 refused_true=2`, EXIT 1, TF6/TF7 refused) and `controls/c2-K-a-r82-tool.txt` (`mismatches=4
  orphans=4`, EXIT 1).
- **Freeze (F `fbf0ae5e`)** — the preregistration alone (`git show --name-only fbf0ae5e` = one path; P does not
  contain it, verified by the reviewer).
- **Pre-data instrument correction (A0 `51b50c94`).** The first `deep` stub wrote its mark before its fan-out, so a
  correct fast walk measured the stub's fork speed (16/24 survivors on `d24-monitor-group` in the L1's reference run);
  the stub now fans out first and marks last, and the control was re-run red for the same reason. Predicates, rows,
  target and commands unchanged (A0).
- **C1 candidate (W1 `bbffe6a0`, cleaned before filing).** `census/round-83/c1-pointer-counter.py`: the r82 capture
  branch (`_capture_ok`) plus a wave-directory branch (`w[0-9]+/`, `a2w1/`, `assimilation/`) compared by the
  token's remaining path below its own first below-round component (full suffix, in order). After cleanup: the three
  unreachable capture alternates and the unreachable `tt == tk` disjunct removed, the contradictory r82 branch-order
  comment corrected (A1/A3).
- **C2 candidate (W2 `9994af61`; guarded and total-parsed before filing).** `tools/souji-vault-verify.sh`: one
  `/proc` pass — every stat read WHOLE and stripped after the last `)` of the whole content (field 4 ppid, field 22
  starttime, arity-guarded), rooted at the `timeout` wrapper's pid (never signalled) — a reverse map, and a DFS
  that TERMs each descendant as discovered and re-checks its starttime before TERM and before KILL. A9 adds the
  `[ "$#" -ge 20 ] || continue` belt (S83Reviewer F3 / S83ExecC2 F1) and A10 the whole-file read (S83Sentinel F1
  CRITICAL: a newline in the untrusted CLI's own comm could truncate a first-line parse and hide the subtree).
- **Independent reproduction.** `S83ExecC1` reproduced the C1 candidate byte-identically (36/36 + five regressions +
  predicate probes); `S83MutTool`/`S83ExecEvade`/`S83Reviewer`/`S83Scribe` each ran the C2 counter on the candidate
  bytes (20/0/0/0 at 0.9-1.0 s on the seat's own candidate; 0.3-0.4 s on the landed one); `S83Reviewer` re-ran C1
  K-a byte-for-byte and the C2 candidate three times; `S83Scribe` derived the 108-invocation pgrep total from the
  tree shape (N+2 nodes per tree) and matched the shim's count.
- **Sources and registry.** S330 (pgrep(1)) opened as `rejected` with a grounded flip; S331 (own-work
  wave-directory census at `1e870403`) and S332 (kernel `fs/proc/array.c` v6.17, captured at
  `census/round-83/srcs/linux-array.c-v6.17`) admitted and cited by the two knowledge entries; `corpus/knowledge/
  own-tree-pointer-binding.md` added, `corpus/knowledge/gate-signal-handling.md` extended.
- **Wave falsification and narrowing (Amendment 59).** The wave falsified eight sentences of the frozen wording; all
  were narrowed in `plans/round-83.md` A1-A9 before filing (six-shape over-specification, one-component suffix
  depth, dead identity clause, layout-not-move, host-dependent C2 control count, unrowed safety code, the pgrep
  shim's real instrument, the undisclosed foreground fallback), and the three further findings (recorded in A9).
  The pre-file ledger is `.ufo/waves/round-83/claim-falsification.tsv`; the gate line is below.

## Landed changes

| change | LOG.md entry | commit |
|---|---|---|
| P: C1/C2 instruments (36/20-row populations, harness, counter, real-shape census) and both do-nothing controls | `## Round 83` (sources/registry, C1/C2 bullets) | `1014143d5cb3ecad23329c8f63cb72328ff30061` |
| F: preregistration (frozen claims) | `## Round 83` (first bullet) | `fbf0ae5e4ac54eec16b9ef5f2439de2a44dfb7b0` |
| A0: deep-stub hang point after its fan-out; K-a receipt refreshed | `## Round 83` C2 bullet (A0) | `51b50c94d0d9a5baf3e6564d1b5dbc48b970053c` |
| W1: C1 candidate counter + receipts | `## Round 83` C1 bullet | `bbffe6a0d1221766b76acbf78c649a5783ac9def` |
| W2: C2 candidate tool + receipts | `## Round 83` C2 bullet | `9994af61565ec87913152cf1102c61ac9a75b04d` |
| Integration/bookkeeping: C1 cleanup, C2 arity guard, regenerated receipts, SOURCES 252→255, knowledge entries, Q152/Q153, SKILL registry rows, lesson, SCORECARD, plan, wave evidence | `## Round 83` (all bullets; append-only correction of the r82 `$!` sentence) | `802a41e71520b3b4feb300421cb1a6475c01d9d0` |
| Ledger, S333 provenance correction, wave results, lesson pointer fix | `## Round 83` | `523e372d6b4aac03bb0d76f502746f62dcf9c6a1`, then `d5e325b6fa22a5371d2591d6f3c773ad69236c5c` (wave results + final ledger) |

The r82 report's Landed-changes chain omitted `51a5e7fa` (the r82 freeze receipt + lesson M1/M2); it is named here
because the r82 spot-check routed it (defect 3). The r82 LOG C2 bullet that says the tool "drops the stale `$!`" is
corrected in the r83 LOG entry (R1 restored `local pid=${CLI_PID:-${!:-}}`).

## Before → after measurements

**C1 — calibration 7.** Counting command:
`python3 -B census/round-83/c1-false-row-harness.py --counter <counter> --lane <lane> --fleet-root <fleet> --work <empty>`

| end | receipt | line |
|---|---|---|
| before (r82 counter, `census/round-82/c1-pointer-counter.py`) | `census/round-83/controls/c1-K-a-r82-counter.txt` | `SUMMARY rows=36 mismatches=2 accepted=0 refused_true=2 errors=0`, EXIT 1; the two refusals are TF6 (`w2/`) and TF7 (`w1/`) |
| after (candidate, counter sha256 `052c4f3f…`) | `census/round-83/records/c1-after.txt` | `SUMMARY rows=36 mismatches=0 accepted=0 refused_true=0 errors=0`, EXIT 0 |

Measured at W1 `bbffe6a0` and re-derived after the cleanup on the filed bytes (`052c4f3f…`). Regressions with the
candidate: r77 `items=35 resolved=35` + `forged=7 matched=7`, r78 `items=22 resolved=22` + `forged=12 matched=12`,
r79 harness 9/9, r80 harness 18/18, r81 harness 25/25, r82 harness 32/32 (`census/round-83/records/c1-regress-*.txt`).

**C2 — operability 8.** Counting command:
`python3 -B census/round-83/c2-tree-walk-counter.py --tool <tool> --work <empty>`

| end | receipt | line |
|---|---|---|
| before (r82 tool, sha256 `dd6d440e…`) | `controls/c2-K-a-r82-tool.txt` (load1 ≈ 250) | `SUMMARY rows=20 mismatches=4 errors=0 orphans=4`, EXIT 1 |
| before, low load (same bytes) | `records/c2-before-pgrep.txt` (load1 ≈ 56) | `mismatches=1 orphans=1`, EXIT 1; five reviewer executions: 0, 2, 2, 2, 4 |
| after (candidate, sha256 `72a405f2…`, whole-file read) | `records/c2-after.txt`, `c2-after-run2.txt`, `c2-after-pgrep.txt` | `SUMMARY rows=20 mismatches=0 errors=0 orphans=0`, EXIT 0, three runs; deep rows 1.2-1.6 s, 0 survivors; the guarded-but-line-read bytes (`b0a5b662…`) were green at 0.3-0.4 s and the non-author `S83ExecC2/c2-lane-b0a5b66.txt` green while a short-remainder pid was live (the `9994af61` bytes `d4826cce…` scored `mismatches=2 orphans=2` there — the `${20}` abort, repaired) |

Structural discriminators: `pgrep` invocations 106-108 (r82 tool) → 0 (candidate), external shim
(`census/round-83/probes/pgrep-shim/pgrep`, log variable `R83PGREP_LOG`); deep-row seconds 1.8/2.0/3.8/4.6 idle and
≥5 under load (r82) → 0.3-0.4 (candidate). Selftest 57/0, r17 `total=37 failed=0`, probe D `arms=4 failed=0` (all on `72a405f2…`).
The r82 control is a load-dependent race, so the round claims no fixed before-count (A5) and measures at
W2 `9994af61`, re-derived on the guarded bytes (`b0a5b662…`).

## Sources & frontier

Counting command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root
/home/vgpnk/Projects/shokunin souji`

- before (round start): `census/round-83/records/sources-census-before.txt` → `souji ok …/corpus/SOURCES.md`,
  EXIT 0, 88 lines (87 pre-existing `W04` cross-scope duplicate-URL warnings); rows
  `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` = 252.
- after: `census/round-83/records/sources-census-after.txt` → `souji ok …`, EXIT 0, 0 E-findings; rows = 255.
- rows added by tier: **S330** `docs` tier A, `rejected` (procps-ng pgrep(1); the rejection rests on redundancy —
  S075 governs process identity — and its flip is now a token the page contains: `-a`, `-o`, `-n`, `-f`);
  **S331** `own-work` tier A, `mined` (the lane's wave-directory census; scope narrowed to `.ufo/waves/` only);
  **S332** `code` tier A, `mined` (kernel `fs/proc/array.c` v6.17; emission order and the unescaped comm branch);
  **S333** `own-work` tier A, `mined` (supersedes S331's provenance: the census is a working-tree count, not a
  revision count — `.ufo/waves/` is gitignored). Three mined rows, one rejected row; no row changed
  `status`/`recheck`/`used-by` in place this round.
- rows touched old→new: none (all three rows are new this round; S075 was re-opened but its cells are unchanged).
- frontier rows advanced: none — F1-F4 are unchanged (`corpus/README.md` `## Frontier`); the round deepens two
  existing instruments on ground the lane already holds (pointer binding, signal handling), not frontier ground.
- Assimilation: none (`/home/vgpnk/Projects/shokuknow` untouched; no `merge/souji/` theme taken).
- `considerthese/`: no such directory in this lane.

## Trend verdicts

- **expansion: unchanged** — two knowledge artifacts (a new entry on own-tree pointer binding and a new section in
  `gate-signal-handling.md`) on ground the coverage map already holds, plus three registry rows; no frontier row
  advanced, no new kind of source, no capability on uncovered ground. The round's gains are instrument depth, not
  breadth, and it says so.
- **quality: improved** — the pointer counter now binds the lane's real wave shapes instead of a plausible fixture
  (Q151's failure mode) and the vault tool's signal path costs one `/proc` pass instead of one fork per node (10× on
  the deep rows, 108 → 0 short-lived `pgrep` processes); two defects the wave found are repaired on the filed bytes
  (the `${20}` abort, the dead identity disjunct/false comment), and Q152/Q153 record the two criteria the wave
  mined. Nothing already admitted was found false; no entry was left stale.
- **discernment: improved** — the wave falsified eight sentences of the round's own wording and all eight were
  narrowed before filing rather than defended (A1-A9); the S330 rejection was re-adjudicated by a source seat that
  corrected an ungrounded flip token (`NSpid`); the r82 spot-check's routed form defect is closed with a row; a
  seat's MEDIUM that would have rewritten the rule was re-derived and only its observation adopted (A1); the three
  seats whose first read left a skeleton delivered full reports before the wave settled (no seat was dead, and none
  was back-filled).

## SHONEN

- `[~]` SKILL.md contains real decision tables, error patterns, checklists, cited sources — SKILL.md r83 gate
  registry rows (last two rows) cite the 36-row harness, the 20-row counter and their controls; corpus/SOURCES.md
  S330-S332; corpus/lessons/round-83.md `## Gate`.
- `[~]` At least one end-to-end domain task executed and logged in LOG.md — LOG.md `## Round 83` (the C1/C2
  candidates, controls and measurements); the historical sweep remains LOG.md:362.
- `[~]` Instructions executable by an agent without oral context — the preregistration, `plans/round-83.md` A0-A9
  and the two SKILL gate rows; `census/round-83/records/c1-after.txt`, `c2-after.txt` are the re-runnable receipts.
- `[~]` No cross-domain bleed (PROVINCE.md still accurate) — PROVINCE.md unchanged this round; the kernel `array.c`
  row is scoped to the stat emission order the tool parses, not to kernel ownership; S83Connector's sibling scan
  records `tools/souji-proc-census.sh` as the lane's own overlap, not absorbed scope.

## Extras

- **Stale-lane:** respawn-per-round driver; this r83 is the lane's only open mission.
- **Tool installs: none.** No pacman (paused host-wide), no uv/npx/binary fetch, no sysctl/sudo/kernel change.
- **Wave:** 12 seats spawned, 12 settled, **0 dead** (`w1-spec.json`, `w1-dispatch.json`, `w1-results.json`);
  roles executor×3, scribe, scout×2, connector, reviewer, critic, mutation-tester×2, sentinel; attack 6/12 = 50 %.
  All twelve delivered substantive reports; three delivered after the first read (`S83ExecC2`, `S83ScoutDirs`,
  `S83Sentinel`) and their first-read skeletons are named in the wave evidence. `S83ExecC2` found the C2 `${20}`
  abort independently (F1), with a live-host reproducer and a green non-author run of the guarded bytes
  (`S83ExecC2/c2-lane-b0a5b66.txt`); the L1's two earlier green runs on `d4826cce…` were luck (the hazard needs a
  paren-carrying comm). `S83Sentinel` then delivered F1 CRITICAL (a newline in the untrusted CLI's own comm could
  hide the subtree from a first-line parse), F3 (the read→signal window measured at 16-126 µs), F4 (the root is the
  `timeout` wrapper) and F5 (post-pass forks) — all narrowed into A10 or carried as stated limits; the final bytes
  read each stat whole.
- **Misroot sweep:** `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows only other lanes' files
  (`.scratch/run15-*`, `.ufo/reports/round-85|92`, `.ufo/l0-questions.md`, fleet-root `plans/round-91.md`); no file
  of this round's seats landed at the fleet root.
- **Landing gate:** `tools/souji-landing-gate.py --round 83` at the final tip `9d927f80` → `SUMMARY findings=24
  checked_reg=198`, rc 2 (the gate's findings exit); none is this round's (at `802a41e7` it was 27, the three extra
  being the not-yet-landed ledger pointer twice and a historical draft path once, all fixed by the later commits).
  The 24 are pre-existing historical pointer rows (`$k`/`..` recipes, round-73/74/79 receipts, `tools/corpus/…`),
  unchanged. `COULD-NOT-EVALUATE no .md reports under .ufo/waves/round-83/`: the seat reports live one level deeper,
  in `w1/`, so the gate's report-carry check did not run (named, not hidden).
- **Open L0 questions:** none new this round; the host-gate incident was reported to the operator session and reaped
  there (not routed as an L0).
- **PREFILE-FALSIFICATION:** `python3 scripts/hyaku/prefile-falsification.py --lane souji --round 83` →
  `PREFILE-FALSIFICATION: pass claims=2 rows=12 attack_seats=6 findings=0`, exit 0.

Lane tip at filing: `d5e325b6fa22a5371d2591d6f3c773ad69236c5c` (`master`, `local=remote`, ahead 0); this report is
committed on the fleet repo by `fleet-commit.sh --as souji` immediately after it.
