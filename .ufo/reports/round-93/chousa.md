# chousa — round 93 report (2026-11-08)

Lane `chousa`, round 93, attempt 1. Base `206226dc9d9baef620e7d3d30bdac5f9194a459f` (round-92 landing + its
non-author spot-check, admitted). Freeze **F6 `3789608dc8c0eded67f1e5d3840caf0a27522a88`** (instruments,
expectations, leg table, claims, pins); carrier **C7 `9d03318527f8fe734e67d24f64ac5dce192d43fc`** (the six
committed scored receipts plus the 23-row pins table). Round shape: one v1 wave, 12 seats under
`ufo-wave-policy.json` band 8–16 (8 attack: 3 reviewer, 1 critic, 1 mutation-tester, 1 sentinel, 1 revenger,
1 mutation-adjacent executor = 3 executors total; 1 connector, 1 scout; the L1 holds the planner seat and a
bounded data-walk rode the scout). Wave registry `.ufo/waves/round-93/w1/swarm-registry.json`, dispatch
`.ufo/waves/round-93/w1-dispatch.json` (12 spawn, 0 resume), ready handoff `.ufo/waves/round-93/w1.ready`
(taken 2026-11-08T11:10:14). Residual call: none. Dead seats: see **§Wave settlement**.

## Work performed

Declared claims (three, three distinct axes, no exploratory claim; frozen set
`.ufo/waves/round-93/claims.md` + `.ufo/waves/round-93/claims.json`):

- **C1 `C1-DRIVER-R93` — operability** (lowest scored non-retired axis, historical 3/10): the pin walk takes
  the whole pins table as its population and pins the committed receipts; every driver input derives from
  `--root`, its own bytes from `--repo`.
- **C2 `C2-CURATION-R93` — calibration**: the whitespace-only quote is refused at the shape leg with a named
  reason and an independent population count, and the leg vocabulary is a committed, pinned side table.
- **C3 `C3-TALLY-R93` — freshness**: both historical tallies are derived from the receipts that ground them
  and must be present in scope; tallies before *and* after the `## Gates` scope are declared; the case-range
  leg binds the family's index set, not just its endpoints.

Work items, each with its evidence pointer:

- **C1 driver.** `corpus/evidence/round93/control-driver-r93.py`: `pin_report` walks every row of the pins
  table (`PIN_DISK_MISMATCH path=<rel>`, `PIN_MISSING path=<rel>`, `PIN_ROW_OUTSIDE path=<rel>`,
  `PIN_SELF_ROW_ABSENT path=<rel>`), `receipt_pins` pins each committed receipt (`RECEIPT_MISMATCH`,
  `RECEIPT_UNPINNED`, `RECEIPT_MISSING`), `self_pin` binds instruments at `--rev` and receipts + the pins
  table at `--receipts-rev`, and `main` derives `--expected/--receipts/--pins` from `--root` while resolving
  `__file__` against `--repo`. Before/after: `corpus/evidence/round93/evidence-before/c1-prior-accepts.txt`
  (r92 logic, tree-only form: `RECEIPT PINS OK 7/22`, both tampered trees `CONTROL_DRIVER_R92=PASS`, derive
  form `SETUP path escapes base`) → `corpus/evidence/round93/after/c1-verify.txt` (`PINNED_FILES=23/23`,
  `RECEIPT_PINS=6/6`, `CONTROL_DRIVER_R93=PASS`) and `after/c1-forgeries.txt`.
- **C1 battery.** `corpus/evidence/round93/forgeries-r93.py`: shared clones per tree (fresh legs need a git
  dir), two discriminating forgeries plus two wave-found regressions and the derivation class; final line
  `FORGERY_REFUSED=2/2 PRIOR_ACCEPTED=2/2 DERIVE_OK=1/1 REGRESSION_REFUSED=2/2 POSITIVE=pass`
  (`after/c1-forgeries.txt`).
- **C2 counter.** `corpus/evidence/round93/curation-r93.py`: `ws_quote_cell()` is one expression shared by
  the shape branch, the `WSQUOTE` leg and `witness()`; `controls/legs.txt` is the committed vocabulary
  (`LEG_FAIL LEGSET`, `LEG_FAIL ARITY`); `DECISION_WIDTH` prints per row. Before/after:
  `evidence-before/c2-prior-accepts.txt` (r92 `Q_SHAPE_FAIL=0` on a whitespace tree, refusing only at
  FLOOR/WARRANT/TFREQ) → `after/c2-counter.txt` (`LEGS_MEASURED=15/15 Q_WSQUOT=0 DETECTOR_WITNESS=13/13`).
- **C2 controls.** `corpus/evidence/round93/curation-controls-r93.py`: two whitespace trees bound to
  `Q_WSQUOT=1` **and** `LEG_FAIL WSQUOTE` (the stub probe `after/c2-m7-stub.txt` shows a disabled population
  prints neither), four carried r92 classes, the r90 regression line. `after/c2-controls.txt`.
- **C3 counter.** `corpus/evidence/round93/skill-tally-r93.py`: `HIST_SOURCES` derives the historical
  multisets from `corpus/evidence/round25-final-measure.log:53` and
  `corpus/evidence/round34/audit-dispositions.md:5` (`HIST_DERIVED`, `HIST_UNGROUNDED`), `HIST_PRESENT`
  requires presence in scope, `HEAD_DECLARED={}` + `TAIL_DECLARED={215:1,283:1}` with `HIST_SCOPE_BLEED
  head|tail`, and the case-range leg compares index sets over every `ok-case` line.
  `evidence-before/c3-prior-accepts.txt` (r92 green on a changed tail and an added tail) →
  `after/c3-counter.txt` (`LEGS=4/4 HIST_DERIVED=2/2 HIST_PRESENT=2/2 TAIL_OK=1`).
- **C3 controls.** `corpus/evidence/round93/skill-tally-r93-controls.py`: positive, three carried classes,
  tail-changed, tail-added, head-tally, interior-hole, ungrounded-receipt. `after/c3-controls.txt`.
- **Frontier (§2b).** `corpus/SOURCES.md` is byte-identical to base (`git diff 206226dc F6 --
  corpus/SOURCES.md` empty, 219 rows); two rows re-opened — `S070` (installed `sha256sum(1)`, sha256
  `93c17dff…403f` identical, decompressed line 11 quote re-read) and `S001` (rev-form `GATE-RECORD`
  verified at F6, `tools/research-gate.sh:9010`). No `status`/`recheck`/`used-by` change. Census exit 0 at
  start (`corpus/evidence/round93/census-start.txt`) and end (`census-end.txt`).
- **Mistake mined.** `corpus/lessons/round-93.md` `## Mistakes`: (1) a before-state asserted instead of
  measured (C2's first draft) — captured by the L1's own pre-freeze run, fixed by re-freezing as a
  classification claim with `WS_SHAPE_GREEN_R92` re-deriving the distinction; (2) a harness pair cut before
  its own legs ran (F `84998563`) — `self_pin` signature collision and archive trees that cannot host the
  fresh legs, fixed by re-cutting F2 and switching the battery to clones.
- **Amendments.** `corpus/evidence/round93/amendments.md` records all eleven amendments the wave and the
  L1's re-measurement forced. The frozen claims file keeps its F6 bytes; the two numbers that moved after
  scoring are named there (Amendment 5: `DETECTOR_WITNESS` 11→13; Amendment 12 below).
- **Wave.** `.ufo/waves/round-93/w1/` holds every seat report and receipt; the seat-level findings that
  changed the landing instruments are H1/H2/M1/M2 (`R93ReviewerC1`), F1–F6 (`R93ReviewerC2`), F1–F3
  (`R93ReviewerC3`), M7/M8 (`R93ExecMutations`), C2 stub (`R93CriticClaims`), F1a–F1c
  (`R93ScoutSources`), and the connector's C1 note.

## Landed changes

Every change is committed through `scripts/hyaku/jj-lane.sh commit … --as chousa` (lane) and is tied to the
LOG entry this round appended (`LOG.md`, `## Round 93 — 2026-11-08`).

| commit | carries | LOG tie |
|---|---|---|
| `84998563381d87a4082de439dd82572c6f87fac8` | F (superseded before scoring): first instrument set | LOG r93 bullet 1 (named as superseded) |
| `b7241252c2358613d3b22b7d0454d98c56dab373` | F2: instruments, expectations, claims, 16-row pins | LOG r93 Before bullet |
| `754b62fb6adc60e44e12375af5461a0ebe302994` | C2: receipts at F2 + pins | LOG r93 After bullet |
| `d740760e5e2bdb2355435bd9c2fd132ad825df41` | C3: forgery battery on shared clones + pins | LOG r93 After bullet |
| `d5c19c546e83992e8153292517f4b32f71a71793` | F3: driver resolves its own bytes against `--repo` | LOG r93 After bullet |
| `94fbf89222163757c43aa79a7467be707b05da77` | C4: receipts at F3 + pins | LOG r93 After bullet |
| `596eabc952f7dcd9bd27030af7dba54714f4af4c` | F4: wave findings applied (WSQUOTE witness, ARITY, tally head scan, index sets, claims narrowed) | LOG r93 After bullet |
| `881a541fc3fcfb8717959a47331720d8ebf6f892` | C5: receipts at F4 + pins | LOG r93 After bullet |
| `1362f4b285f698c0b728037245f8fbef5d1835db` | F5: self row required, pin rows contained by `--root`, battery regressions | LOG r93 After bullet |
| `c1ebb1d9c5878e8175b4ec865dc9513794ae0692` | C6: receipts at F5 + pins | LOG r93 After bullet |
| `3789608dc8c0eded67f1e5d3840caf0a27522a88` | F6 (freeze cited): leg vocabulary as a committed table, controls bind `Q_WSQUOT` | LOG r93 After bullet |
| `9d03318527f8fe734e67d24f64ac5dce192d43fc` | C7 (carrier cited): receipts at F6 + 23-row pins | LOG r93 After bullet |
| landing commit | lesson, LOG, SCORECARD, amendments, `after/`, `evidence-before/`, wave evidence | all round-93 LOG bullets |

Subject tools are untouched: `git diff 206226dc <landing> -- tools/ SKILL.md` is empty; the registry diff
is empty. No file outside the lane, the report path and `corpus/evidence/round93/` was written by this round.
Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` after the wave — see
**§Wave settlement** (no seat file landed at the fleet root).

## Before → after measurements

Counting commands (all from `/home/vgpnk/Projects/shokunin/chousa-shokunin`), measured at F6/C7:

| claim | counting command | before | after |
|---|---|---|---|
| C1 | `python3 -B corpus/evidence/round93/control-driver-r93.py verify --root . --repo . --rev 3789608d… --receipts-rev 9d033185… --work <scratch>` + `forgeries-r93.py --root . --repo . --rev 3789608d… --receipts-rev 9d033185… --work <scratch>` | r92 logic on the same fixtures: `PINNED_FILES=7` of 22, both tampered trees `PASS` (rc 0), derive form `SETUP path escapes base` (`evidence-before/c1-prior-accepts.txt`) | `PINNED_FILES=23/23 RECEIPT_PINS=6/6 CONTROL_DRIVER_R93=PASS`, `FORGERY_REFUSED=2/2 PRIOR_ACCEPTED=2/2 DERIVE_OK=1/1 REGRESSION_REFUSED=2/2 POSITIVE=pass` (`after/c1-verify.txt`, `after/c1-forgeries.txt`) |
| C2 | `python3 -B corpus/evidence/round93/curation-r93.py --root .` + `curation-controls-r93.py --root . --work <scratch>` | r92 on a whitespace tree: `Q_SHAPE_FAIL=0`, refusals only at FLOOR/WARRANT/TFREQ; no `Q_WSQUOT` field (`evidence-before/c2-prior-accepts.txt`) | `CURATION_R93=PASS LEGS_MEASURED=15/15 Q_SHAPE_FAIL=0 Q_WSQUOT=0 DETECTOR_WITNESS=13/13`; forged trees `Q_SHAPE_FAIL=1 Q_WSQUOT=1` + `LEG_FAIL QSHAPE`/`LEG_FAIL WSQUOTE`; `CONTROLS=PASS CARRIED_REFUSED_BOTH=4/4 WS_NAMED=2/2 WS_SHAPE_GREEN_R92=1/1 DUPCOUNT_1=1/1 PRIOR_REGRESSION=7/7` (`after/c2-counter.txt`, `after/c2-controls.txt`) |
| C3 | `python3 -B corpus/evidence/round93/skill-tally-r93.py --root . --selftest corpus/evidence/round93/controls/selftest-r93.txt` + `skill-tally-r93-controls.py --root . --work <scratch>` | r92: frozen literal multiset, tail ignored — changed tail rc 0, added tail rc 0, head tally rc 0 (`evidence-before/c3-prior-accepts.txt`) | `SKILL_TALLY_R93=PASS TALLY_ROWS=8 STALE_TALLIES=0/8 CASE_RANGE_OK=2/2 HIST_DERIVED=2/2 HIST_PRESENT=2/2 TAIL_OK=1 LEGS=4/4`; `CONTROLS=PASS … TAIL_REFUSED=2/2 HEAD_REFUSED=1/1 INTERIOR_REFUSED=1/1 HIST_UNGROUNDED_REFUSED=1/1` (`after/c3-counter.txt`, `after/c3-controls.txt`) |

Measured against F6 (`3789608d`) and C7 (`9d033185`). Amendment 12: the pin population is 23 rows, not the
22 the frozen C1 sentence names — the round-93 leg table (`controls/legs.txt`) is a pinned instrument, added
when M8 was killed; `PINNED_FILES=23/23` is the landing value and `22/22` was true only between F5 and F6.

## Sources & frontier

`SOURCES.md` rows before → after: **219 → 219**; rows added by tier: none; rows touched old → new: none
(no `status`, `recheck` or `used-by` cell changed); frontier rows advanced: none. Counting command and both
exits:

```sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin chousa
# start exit 0 (corpus/evidence/round93/census-start.txt), end exit 0 (census-end.txt); 5 × W04 pre-existing
```

`git diff 206226dc F6 -- corpus/SOURCES.md` is empty, so the registry is byte-identical to base. Two rows
were re-opened without a cell change: `S070` (installed `sha256sum(1)`; sha256 `93c17dff…403f` matches the
row; decompressed line 11 `Print or check SHA256 (256\-bit) checksums.`) and `S001` (rev-form `GATE-RECORD`
in `corpus/lessons/round-93.md` `## Gate`, verified by `tools/gate-records.py verify`, exit 0). The scout's
citation-precision findings are accepted: `S073` is the row that corrects S070's anchor label, and the
literal roff form is quoted above. The plan's "`recheck` cell moves 92 → 93" sentence is withdrawn — S001's
cell has read `on-release` in every commit that touched the registry. `Assimilation: none` (no skuknow
package entry admitted this round; wave-4 quarantine-first already ran and this round takes no adoption).

## Trend verdicts

- **expansion: unchanged** — knowledge entries 97 → 97 (`git diff 206226dc <landing> --stat --
  corpus/knowledge/` empty), registry 219 → 219; the round's gain is in the instruments, not the corpus.
- **quality: improved** — three instruments hardened with measured red-before witnesses and named kills:
  the pin walk's population grew 7 → 23 rows (`after/c1-verify.txt`), four wave-found forgery classes are
  refused with named codes (`after/c1-forgeries.txt` `REGRESSION_REFUSED=2/2`, `after/c2-m7-stub.txt`), and
  every fix has a failable control (`after/c2-controls.txt`, `after/c3-controls.txt`).
- **discernment: improved** — the wave fired all three claims' *sentences* (C1 battery dead on host python,
  C2's named limit false and its distinguishing field ungated, C3's scope claim wider than the code) and the
  lane published eleven amendments, four re-freezes and one target-number correction (Amendment 12) instead
  of filing the wider sentences; the two defects in the lane's own first harness are Amendment 1.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md` Gates
  table unchanged this round; `corpus/evidence/round93/after/*.txt` re-derive its tallies (`SKILL_TALLY_R93=PASS`).
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md` `## Round 93`; this round's
  end-to-end task is the three-counter re-measurement chain at F6/C7 (`corpus/evidence/round93/after/`).
- [~] Instructions executable by an agent without oral context — `bash tools/research-gate.sh --selftest`
  `PASS (283 cases, 0 skipped)`; every claim's counting command is pasted above and every receipt is committed.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` untouched; the connector seat's
  sibling scan is read-only and absorbed nothing (`.ufo/waves/round-93/w1/R93ConnectorSiblings.md`).

## Stale-lane

Respawn-per-round driver (`hyaku-inline`, attempt 1); no other mission of this lane is open. No tool installs
or upgrades were made this round (no `uv`, `npx`, `cargo` or `pacman` transaction).

## Wave settlement

One v1 wave, 12 seats, dispatched 2026-11-08T11:10:14 (`w1.ready.dispatched`); attack share 8/12. **All 12
seats wrote a report with a `VERDICT:` trailer** into `.ufo/waves/round-93/w1/` (committed at `d4f97cf7`):
ExecC1Repro, ExecC2Repro, ExecC3Repro, ExecMutations, RevPrior, ReviewerC1, ReviewerC2, ReviewerC3, CriticClaims,
SentinelScope, ConnectorSiblings, ScoutSources. No seat died: every report carries commands, receipts and exit
codes, and each seat's own scratch dir was removed before it yielded (checked in the reports' last sections).
Settlement handoff: `WAVE-DONE chousa r93 w1` received from the orchestrator with
`.ufo/waves/round-93/w1-results.json` (12 results, each with a non-empty output carrying its verdicts, 0
errors, 0 dead seats). That file is committed with this report's lane amendment.

Seat verdicts against the claims at the attacked bytes (F2/C2): C1 fired from `R93ExecC1Repro`,
`R93ReviewerC1`, `R93ExecMutations`, `R93SentinelScope`, `R93CriticClaims`, `R93ConnectorSiblings`
(the battery dead on host `python3` 3.14.8 via `tarfile.AbsoluteLinkError`; `FORGERY_REFUSED=0/2` under 3.13
from archive trees; the unguarded self row and row containment), and held from `R93RevPrior`; C2 fired from
`R93ReviewerC2` (false named limit, ungated `Q_WSQUOT`, machine-form tokens) and `R93CriticClaims` (stubbed
population), held from `R93ExecC2Repro` and `R93ScoutSources`; C3 fired from `R93CriticClaims` /
`R93ReviewerC3` / `R93SentinelScope` on the machine-form `TAIL_REFUSED` token and F2/F3, held from
`R93ExecC3Repro` (three independent derivation probes). Every fired item is closed at F3–F6 and re-measured in
`corpus/evidence/round93/after/`.

Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` (no pathspec) after the wave shows no
file naming chousa/round-93 outside `.ufo/reports/round-93/chousa.md` (this report, to be committed by
`fleet-commit.sh`); the other entries are `.scratch/` run state (orchestrator-owned) and other lanes' reports.
Nothing was copied or deleted at the fleet root.
