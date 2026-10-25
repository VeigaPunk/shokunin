# mado — round 39 report (hyaku run 7, attempt 2)

Lane repo `/home/vgpnk/Projects/shokunin/mado-shokunin`, branch `master`, final lane hash
**`b6078c3ed9272be23932e00ee21ad29e3c1fdf9d`** (`git ls-remote origin refs/heads/master` prints it).
L1 attempt 2: `MadoR39a2`. Attempt 1 (`MadoR39`) froze `457d1b1`, dispatched wave `w1`, and
ended without a data commit; attempt 2 inherited and integrated it.

## Work performed

Declared claims (3):
- **C1 — calibration:** the repaired round-38 discrimination pair re-registered with a fresh
  freeze (re-frozen manifest + unchanged counters must score 19/19).
- **C2 — operability (capability acquisition):** `tools/mado-options.py`, the config-option
  ownership table (every option key → last declarer, owner file, line, layer; `--getoption`
  merge with the five divergence classes).
- **C3 — coverage (sourced):** `corpus/knowledge/config-option-table-r39.md` admitted with rows
  S218 (0.56.0 hyprlang page) and S219 (own-work), plus S220 (0.54.0 Keywords page).

Work items:
- Inherited attempt-1 state verified and reused: freeze `457d1b1` (registration, C1 manifest,
  base receipts, round-38 seat reports); w1 seat outputs (60 reports). Discarded/replaced:
  the uncommitted attempt-1 C2 counter draft (preserved byte-exact as
  `.ufo/waves/round-39/c2/c3-r39-options.v1-draft.py.txt`, sha256 `16544cbd…1c35`) and the seat
  drafts of the entry, rows, lesson and amendment (rewritten by the L1; their findings used).
- Attempt-2 freeze `d9b4e4a65ad63ddcd0b86d2468f41508a131b7fa`: `registration-a2.md`, C2 counter
  `PRED-C3-r39-v2` (8 trees generated from sha256(REV:i) + 2 merge trees + 1 FIFO tree, own
  reference model), C3 counter `PRED-C4-r39-v1`, controls `c2/ctl-*.txt` (base 0/11, wave-v1 tool
  1/11, first-declarer mutant 1/11, replay stub 0/11, empty stub 0/11) and `c3/c4ctl-*.txt`
  (N1–N8 each 0/1 on its targeted clause; fabricated self-consistent P 1/1 = declared residual).
- Tool defect found and fixed before data: the wave-built tool listed `binddr`, `bindeld`,
  `bindld`, `bindmd` and five `windowrule:*` fields as options on the host tree (79 rows, 70
  real; `c2/real-tree-diff.txt`). Exclusion now follows the host's handler table (S162
  `ConfigManager.cpp:601-623`, special categories `:518/567/591/595/626`) and hyprlang v0.6.8's
  allow-flags match (S173 `config.cpp:869`); two selftest assertions, each killing a one-line
  mutant (`c2/selftest-mutA.txt`, `c2/selftest-mutB.txt`: 69/71). Commit `4ec582e`.
- Every cited source re-opened by the L1 on 2026-10-25 (`.ufo/waves/round-39/fetch/`; S018, S162,
  S173, S196 byte-identical to their held receipts).
- C3 entry, rows S218–S220, used-by extensions S018/S162/S173, README index row, lesson Gate:
  commit `3783961`; S219 OBS rewrap: commit `3628472`.
- Assimilation (dispatcher theme) appended to the held
  `corpus/knowledge/dispatcher-surface-and-request-grammar-r26.md` (commit `3783961`).
- Records: lesson `corpus/lessons/round-39.md` (Gate, M39-1, M39-2), QUALITY criterion 64,
  SCORECARD/LOG round-39 sections, wave evidence (`w1/`, dispatch/spec/results): commit `b6078c3`.
- Round-38 closure items: C1 re-registration (C1); eventq live receipt regenerated census-only
  (`w1/ExecEventqSnapshot/eventq-live-census.txt`, counter `fixtures=14/14 … TARGET_MET`);
  inherited round-38 seat reports committed in `457d1b1`; SCORECARD "2 refused" → 3 corrected;
  round-38 report erratum below.
- Planner seat (§3): held by the L1 (validator rejects `planner`).
- Swarm: one v2 wave `w1`, **64 seats** (executor 16, scribe 11, reviewer 11, scout 6,
  connector 5, critic 4, mutation-tester 4, simplifier 3, revenger 2, sentinel 2); no residual
  call; **round total 64**. Dead seats: 3 with no report and no retained output —
  ExecAssimAppendBlock, ScrReportFrontier, MutC3Row (last error text not retained:
  `w1-results.json` notes "orchestrator kernel restarted mid-wave; seat output was delivered to the
  orchestrator session but not retained"); ScrReportMain wrote its draft without a report.
  Seat ExecNavAfter waited on the C3 landing and was unblocked by the L1
  (`w1/ExecNavAfter/nav-after.txt`: 56/56).

**Erratum to the fleet round-38 report** (`.ufo/reports/round-38/mado.md`, addendum item
"RevM37Routing"): the sentence "Refines the RevCommitChain errata: frozen C1 × fixed manifest =
19/19 — the `859d0cf` counter patch was not load-bearing; the frozen-pair failure is the
`c1-duprow` manifest control alone, narrowing the re-registration ruling" is superseded. Frozen
counter × frozen manifest = 18/19; 19/19 belongs to the repaired pair after the manifest
rewrite `b6c1d31`; `859d0cf` was a verdict no-op (lane LOG records `c46f868`, `f551b70`; this
round's `receipts/c1-redbefore.txt`).

## Landed changes

| Commit | Change | LOG entry |
|---|---|---|
| `457d1b125932c1e0d797061a2156b917bcd7edaa` | attempt-1 freeze: registration, C1 manifest, base receipts, round-38 seat reports | LOG.md "Round 39" bullet 1 |
| `d9b4e4a65ad63ddcd0b86d2468f41508a131b7fa` | attempt-2 freeze: C2 v2 + C3 v1 counters, controls, v1 draft preserved | bullet 3 |
| `4ec582e68acaae647911e31334f0b018b4c772bf` | C2 data: `tools/mado-options.py` + receipts | bullet 4 |
| `3783961452844c281d3aefb9d8cff167e3b2cd58` | C3 data: entry, S218–S220, used-by, index row, lesson; dispatcher amendment | bullets 5–6 |
| `362847279eccb77b22789a37cbbe3b83b205d49c` | C3 fix: S219 OBS line carries its quote | bullet 5 |
| `b6078c3ed9272be23932e00ee21ad29e3c1fdf9d` | records + after receipts + w1 evidence | bullets 7–9 |

## Before → after measurements

- **C1** — `cd /home/vgpnk/Projects/shokunin/mado-shokunin && python3 -I quality/check-r38-discrimination.py --c1 quality/counters/c1-r38-event-ground.py --c2 quality/counters/c2-r38-eventq.py --manifest .ufo/waves/round-39/c1/manifest.json --rev <rev>`
  Before (frozen r38 manifest at base `08be4eb`): `controls=19 correct=18/19 verdict=TARGET_MISSED`, exit 1.
  After: `controls=19 correct=19/19 verdict=TARGET_MET`, exit 0 at freeze `457d1b1` and tip `3628472`
  (`receipts/c1-after-freeze-L1.txt`, `receipts/c1-after-tip.txt`). Verdict: **met**.
- **C2** — `cd /home/vgpnk/Projects/shokunin/mado-shokunin && python3 -I quality/counters/c3-r39-options.py --repo . --rev <rev>`
  Before (base `08be4eb`): `fixtures=0/11 tool=absent verdict=TARGET_MISSED`, exit 1.
  After: `fixtures=11/11 tool=present verdict=TARGET_MET`, exit 0 at data `4ec582e` and tip `3628472`
  (`receipts/c2-before-base.txt`, `c2-after-data.txt`, `c2-after-tip.txt`). Verdict: **met under
  `PRED-C3-r39-v2`, frozen at `d9b4e4a` before data. As declared in registration.md (v1 = the
  docstring of a counter that was never in a freeze commit), C2 is an honest miss**: the v1 draft
  could not reach TARGET_MET for any tool. Operator to rule which predicate binds.
- **C3** — `cd /home/vgpnk/Projects/shokunin/mado-shokunin && python3 -I quality/counters/c4-r39-options-entry.py --repo . --rev <rev>`
  Before (base): `admitted=0/1 verdict=TARGET_MISSED`, exit 1. First data commit `3783961`:
  `admitted=0/1` (clause g; `c3/measure-first-data-commit.txt`). After `3628472`:
  `admitted=1/1 verdict=TARGET_MET`, exit 0 (`receipts/c3-after-tip.txt`). Counter unchanged
  between them. Verdict: **met at the data tip, with the first-data miss disclosed**.
- Harm watch at tip: `MADO_SELFTEST: 460/460` (`receipts/selftest-after.txt`); `indexed=56/56
  missing=0 dangling=0 duplicates=0`; `MADO_AXIS: checked=3 mismatched=0` at `b6078c3`
  (navigation 56/56, calibration 51/51, operability 12/12).

## Sources & frontier

Command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin mado`
- Round start (`receipts/census-before.txt`): `mado ok`, warnings W04 ×7 (S030, S042, S045,
  S097, S119, S120, S121) + W01 S277; exit 0.
- Round end (at `b6078c3`): identical warning set, `mado ok`, **exit 0**.
- Rows 211 → 214 (`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`);
  added by tier: A +3 (S218 docs, S219 own-work, S220 docs), B 0, C 0.
- Rows touched old→new: S018 used-by +dispatcher entry; S162 used-by +config-option entry;
  S173 used-by +config-option entry; S196 re-opened, unchanged (lesson Gate lists each).
- Frontier advanced: per-key option ownership moves from 6 hand-proved keys to the whole tree
  (70 keys; 18 not among the held 56 live pairs).
- Sourced claim: C3 cites S218/S219/S220 opened this round.
- Mined mistakes: M39-1 (counters named as predicates absent from the freeze; fix criterion 64,
  shown to fail at `457d1b1`), M39-2 (exact-keyword exclusion; fix shown by two killed mutants).
- **Assimilation: one theme** (dispatcher surface and request-socket resolution) — the package's
  amendment adopted re-grounded as a dated section; refused: the 0.56.0 Variables page as S218
  (Lua `hl.config()` era), a new S220 row for the Dispatchers page (held as S196); other package
  amendments not this theme. No staged row appended. Id collisions (§10 pattern): reg 214,
  staged 147, collisions 22 (S203–S221, S253, S258, S277); guard proof `  | S002 |` → S002.
  Quarantine slice 13 rows: present S189, S195, S201, S205, S228; refused S224 (absent);
  unverifiable S199, S200 (HTTP 521), S209, S222, S223, S225, S235 (no locator).
- **considerthese:** `2026-10-24.md` proposal 4 mined (C2/C3); `2026-10-25.md` proposal 3 served by C1.

## Trend verdicts

- **expansion: improved** — a new edge class (whole-tree option ownership, parser boundary from
  the host's handler table) with a new tool, entry and three rows (`3783961`, `4ec582e`).
- **quality: improved** — the C2 instrument rejects replay/hardcoding stubs (controls), the tool's
  boundary defect is fixed with mutation-killed assertions, criterion 64 closes the unfrozen-
  predicate class; against it, the C3 first data commit missed and C2's v1 predicate was
  unreachable — both disclosed, not re-labelled.
- **discernment: improved** — two candidate rows refused with reasons and flip conditions (era
  mismatch; duplicate URL), quarantine verdicts per row with L1 spot-checks, the wave's own
  counter draft rejected on evidence (`w1/CritC2Control.md`).

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — historical (`SHONEN.md:5`); no outside-lane verifier this round.
- [~] At least one end-to-end domain task executed and logged in LOG.md — this round's host-tree option table (`.ufo/waves/round-39/fetch/S219.receipt.txt`, LOG.md "Round 39"); no non-author verifier yet.
- [~] Instructions executable by an agent without oral context — `tools/mado-options.py --help`/`--selftest`; dispatched seats are not outside-lane verification.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — the round stays on the Hyprland config plane (`corpus/knowledge/config-option-table-r39.md`); no fresh outside-lane approval.

Stale-lane: respawn-per-round driver; no other mission of this lane is open.
Tool installs: none (L1); seats report none.
Open L0 questions: none.
