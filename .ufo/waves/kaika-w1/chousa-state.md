# chousa — STATE dossier (kaika W1, read-only)

Lane: `chousa-shokunin` — domain "deep-research method (調査) — the reusable craft of source
research" (`PROVINCE.md:3`). Fleet root: `/home/vgpnk/Projects/shokunin`. Lane root used for
every command below: `/home/vgpnk/Projects/shokunin/chousa-shokunin`.

Boundary of this dossier: STATE is lane-internal. `web_search` was available and **not used**;
the lane's own rule bars external live-target research without operator approval, and this
probe needs no external evidence. The only write in this session is this artifact. No repo
edit, git mutation, install, commit, or push was performed. `git status --porcelain` prints 0
lines (clean tree). Numbers below were measured this session; the one derived counter
(`.ufo/interactive-sessions/`, ignored) is reported, not touched.

Date of measurement: 2026-10-19. All commands run from the lane root unless prefixed `../`.

---

## 1. Identity

- **Domain:** deep-research method — question framing, source hierarchy, citation chaining,
  claim-vs-source verification (`PROVINCE.md:3-8`). Refuses bounty scope (kasegi), model
  quality (kengaku), orchestration (kumitate), external live targets without approval
  (`PROVINCE.md:10-16`).
- **Rank:** `shonen` — `SKILL.md:5` (`Rank: shonen`). No roster row: fleet roster ids are
  `kasegi, kengaku, kake, kumitate, kotoba, kagi, kama, audio, game-dev-2d, game-dev-3d, lore,
  revenger, kaidoku` — 13 entries, no `chousa`; no top-level `promotions` key, and the closure
  entries carry `promotions: []`
  (`python3 -c 'import json;m=json.load(open("../MANIFEST.json"));print([r["id"] for r in
  m["roster"]]);print(m["promotions"] if "promotions" in m else "no top-level promotions")'`
  → 13 ids, `no top-level promotions`). The mint recorded probation `>=3 verified rounds` with the roster row
  withheld (`MINT.md`, "Probation" line: "Probation: >=3 verified rounds before a roster row.
  Roster row withheld."). `SHONEN.md` has 0/4 boxes checked (`grep -c '^- \[x\]' SHONEN.md` →
  0).
- **Branch + HEAD:** `master`; `ab19cff53c0d4c1254d9d877a616e0cdbc3de993`, 2026-10-19
  17:05:46 -0300, "Merge remote-tracking branch 'origin/master'"
  (`git branch --show-current`; `git log -1 --format='%H %ci %s'`). History: 97 commits
  (`git rev-list --count HEAD`), 58 of them on 2026-10-19
  (`git log --since='2026-10-19 00:00' --oneline | wc -l`).
- **Last admitted round: 23**, admitted 2026-10-19. Evidence: `SCORECARD.md:1185`
  (`## Round 23 verdict — 2026-10-19`, `ADMIT`); `LOG.md:804` (`round-23: direct integration`);
  fleet ledger craft rows for `lane:"chousa"`, rounds 15–23, each `verdict:"ADMIT"`
  (`python3 -c 'import json;m=json.load(open("../MANIFEST.json"));print([(x["round"],x["verdict"]) for x in m["rounds"] if x.get("lane")=="chousa"])'`
  → 9 tuples, rounds 15–23, all `ADMIT`). Round-23 report: `.ufo/reports/round-23/chousa.md` (3,183 B).
- **Admitted-round count:** 23 verdict blocks — `grep -cE '^## Round [0-9]+ verdict' SCORECARD.md`
  → 22, plus the distinct `## Round-1 per-axis verdicts` heading (`SCORECARD.md:36`) → 23.
  Rounds 2–11 landed 2026-10-15/16; rounds 12–23 all landed 2026-10-19 (`SCORECARD.md` verdict
  headings).
- **Next round: 24 is open and dispatched, not landed.** `SCORECARD.md:1221` pre-registers
  round 24 (64 seats, `opencode-go key 7`); `LOG.md:816` opens it with claims corrected and a
  wave dispatched on `openai-codex gpt-6-luna-max` after opencode-go-7 "interrupted at 17
  seats" (`LOG.md:818-819`; commits `798b37d`, `098f5e6`). No report and no verdict: `ls
  .ufo/reports` → 13 entries ending `round-23`; no `## Round 24 verdict` heading
  (`grep -c '^## Round 24 verdict' SCORECARD.md` → 0). So: next round to land = 24; next round
  number only if 24 is recorded abandoned = 25.
- **Report layout is split.** Rounds 1 and 12–23: `.ufo/reports/round-<N>/chousa.md` (13 dirs,
  `ls .ufo/reports | wc -l` → 13). Rounds 2–11: `.ufo/round-<N>/chousa-goalwave.md` (10 dirs,
  `ls -d .ufo/round-* | wc -l` → 10). Both exist on disk.
- **Fleet ledger identity defect:** `lane_rounds.chousa` max = 14, while the lane records 23
  admitted rounds and the fleet's own craft rows carry 15–23. See §5, D-1.

## 2. Axes

Six axes are defined fleet-wide (`../AXES.md:9-16`). The lane's own table scores only one:

| axis | score | evidence pointer | last-change round |
|---|---:|---|---:|
| operability | 3 | `SCORECARD.md:7` — gate commit `31b4683…`, A/B/C each exit 1 with one DRIFT summary; `.ufo/evidence/round-1/acceptance.json` | 1 |
| depth | unscored | `SCORECARD.md:9-13` — "No expertise scores are invented for the other five axes" | — |
| coverage | unscored | same | — |
| freshness | unscored | same | — |
| calibration | unscored | same | — |
| adjacency | unscored | same | — |

- **Lowest non-retired axis: operability (3).** It is the only scored axis
  (`grep -n '^| operability |' SCORECARD.md | head -1` → `7:| operability | 3 | …`); the
  saturation predicate counts an unscored axis as *not* at/above the line
  (`SCORECARD.md:481-487`).
- **Saturation line: 8.0 on the six axes; stagnation window N = 3 landed rounds; nudge
  `dormant`** (`SCORECARD.md:469-495`; line 471: "Saturation line: **8.0 on this Scorecard's six
  axes**"; line 475: "Stagnation window: **N = 3 landed lane rounds**"; line 494: "Nudge
  verdict: **dormant**"). The 8.0 is borrowed from `../souji-shokunin/SCORECARD.md:44`
  ("Saturation line: 8 per axis; stagnation window 3 rounds", verified at `:43-45`); the lane
  says it has no rubric of its own that derives 8.0.
- **The one score never moves.** Rounds 2–23 record operability `improved` 19 times
  (`grep -c '| operability | \*\*improved\*\*' SCORECARD.md` → 19) while the table still reads 3
  with `Last-change round 1`. `last-change` is therefore a false column, and "lowest axis"
  selection is circular: every round since 12 works coverage/operability by construction. Not a
  harmed axis, but a calibration finding (§4, M-11).
- **Capabilities: 5 real rows** (r12 ×3, r13, r14) —
  `awk '/^## Capabilities/{f=1;next} /^## /{f=0} f && /^\|/ && !/^\|---/ && !/^\| Capability/' SCORECARD.md | wc -l`
  → 6 including the placeholder `| — none yet — |`, so 5 real. Headings at
  `SCORECARD.md:461,596,670,727` (last addition r14). **LOG claims 8 further capability
  acquisitions** (rounds 15,17,18,19,20,21,22,23) — `grep -c 'Capabilities +1' LOG.md` → 10
  (includes r13/r14) — with **no SCORECARD row**. 8 missing rows (§5, D-2).
- **Planned claims for round 24** (`SCORECARD.md:1221-1232`, `LOG.md:818`): coverage/operability
  = `--json` manifest delimiter edge (a non-newline-terminated manifest gets the next JSON object
  concatenated onto the previous line); depth = the manifest-format note. The same LOG entry
  records a **claim correction**: the `--drift` truncated-baseline item is "measured as NOT a
  defect: every truncation form produces `GATE_DRIFT: <tokens>` exit 1" (`LOG.md:818`;
  commit `098f5e6`).

## 3. Corpus

| item | count | command |
|---|---:|---|
| knowledge notes | 24 | `ls corpus/knowledge/*.md | wc -l` |
| lessons | 11 | `ls corpus/lessons/*.md | wc -l` |
| evidence files | 88 | `ls corpus/evidence | wc -l` |
| fixture files (flat) | 22 | `ls corpus/fixtures/*.md corpus/fixtures/*.jsonl | wc -l` |
| archives-r9 tree | 5 + 8 controls | `ls corpus/fixtures/archives-r9 | wc -l`; `ls corpus/fixtures/archives-r9/controls | wc -l` |
| tracked files | 235 | `git ls-files | wc -l` |

- **Coverage map:** 23 knowledge rows, 10 lesson rows —
  `grep -cE '^\| `knowledge/' corpus/README.md` → 23; `grep -cE '^\| `lessons/' corpus/README.md`
  → 10. Two files are unindexed: `knowledge/audit-r11.md` and
  `lessons/2026-10-19-hardlink-alias-boundary.md`
  (`LC_ALL=C comm -23 <(ls corpus/knowledge | sed 's/^/knowledge\//' | LC_ALL=C sort) <(grep -oE
  '`knowledge/[^`]+`' corpus/README.md | tr -d '`' | LC_ALL=C sort -u)`; same for lessons).
- **Stale index line:** `corpus/README.md:50` says "Count: 20 entries, ten knowledge notes and
  ten lessons" (`grep -c 'Count: 20 entries' corpus/README.md` → 1) against 24 + 11 files.
- **Frontier ends at round 10.** 9 round paragraphs (`grep -cE '^Round [0-9]+' corpus/README.md`
  → 9, rounds 2–10) and **zero** for rounds 11–23
  (`grep -cE '^Round (1[2-9]|2[0-3])' corpus/README.md` → 0). `## Frontier` starts at
  `corpus/README.md:306`; the last round paragraph is round 10, then the "Still open" tail.
- **Metadata contract:** 21 of 24 entries carry `source:`, `verified-at:`, `recheck:`; 3 lack the
  `recheck:` key — `archives-verified-r9.md`, `audit-r11.md` (has `recheck (from the lane cwd…`
  without the colon, `audit-r11.md:22`), `gate-baseline-r8.md`. Command:
  `for f in corpus/knowledge/*.md; do s=$(grep -c '^source:' "$f"); v=$(grep -c '^verified-at:'
  "$f"); r=$(grep -c '^recheck:' "$f"); printf '%s %s %s %s\n' "$f" "$s" "$v" "$r"; done` →
  `conforming=21`, 3 missing.
- **No `recheck:` value is a date or cadence.** 0 of 21 —
  `grep -h '^recheck:' corpus/knowledge/*.md | grep -cE '[0-9]{4}-[0-9]{2}-[0-9]{2}|[0-9]+d|on-release'`
  → 0. Every value is a command, so "overdue (before 2026-10-19)" is not computable from the
  registry as written. (Entries with `recheck:` as a folded key: 7 —
  `grep -l '^recheck:$' corpus/knowledge/*.md | wc -l` → 7; see the sweep above.)
- **QUALITY.md:** 5 criteria, 300 B (`wc -c < corpus/QUALITY.md`), header "probation draft"
  (`corpus/QUALITY.md:1`). Criteria: falsifiability, measured anchor, observation/inference/
  unknown separation, append-only errata, kept rejections (`grep -cE '^[0-9]+\. ' corpus/QUALITY.md`
  → 5). It says nothing about metadata fields (`grep -cE 'source:|verified-at|recheck'
  corpus/QUALITY.md` → 1, the word "source" in criterion 2).
- **Lessons shape deviates:** `round-<N>.md` convention is used only by `round-1.md`; the other
  10 are date-titled. `## Gate` is present in 7 of 11 (`grep -lE '^## Gate' corpus/lessons/*.md |
  wc -l` → 7; absent in `2026-10-16-archive-scale-controls-and-ledger.md`,
  `2026-10-16-gate-behavioral-baseline.md`, `2026-10-16-verifying-conversion-not-original.md`,
  `2026-10-19-hardlink-alias-boundary.md`).
- **Known gaps** (`corpus/README.md:139`) are explicit about what CLEAN does not prove, per mode,
  and end with the open operator items: receipt identity, non-author spot-check, frozen replay
  (`corpus/README.md:471-476`).
- **Sizes (bloat signal):** `wc -lc` → `LOG.md` 86,788 B/820 lines; `SCORECARD.md` 85,467/1232;
  `corpus/README.md` 77,240/476; `SKILL.md` 40,280/434; `tools/research-gate.sh` 223,477/5217.

## 4. Mistakes (mined, with disposition status)

| # | class | instance + evidence pointer | already captured? | proposed criterion when not |
|---|---|---|---|---|
| M-1 | pre-registered wave not dispatched | Round 23 planned "one 16-seat AgentSwarm call, **devin swe-2**" (`SCORECARD.md:1174-1176`); landed as "direct integration (no wave — claim's before→after already measured by the r20 wave's live reproduction)" (`LOG.md:804`); commit `77bcfd1` subject adds "per honest-stop" | No. QUALITY.md criterion 1 requires falsifiability, not that the registered dispatch shape is the one executed. `PROTOCOL-APPENDIX.md:50` defines honest stop only for unjudged *exploratory* claims | "A registered wave that is not dispatched closes with a LOG line naming the substituted evidence and a `disposition:` row on the planned block; `honest stop` names only exploratory claims." |
| M-2 | claim registered before its before-state | Round-24 opening registered `--drift` truncated-baseline detection; re-measurement found every truncation exits 1, not `none`; corrected in the same landing (`LOG.md:818`; commit `098f5e6`) | Yes — QUALITY.md 1 (falsifiable) + 3 (observation vs unknown); it is the method working | — |
| M-3 | stale open finding in the skill | `SKILL.md:432-434` — "the one live finding (`A-r9.md:50` row C3 cites `A:76` while its span occurs at `A:86`) remains open pending fix-or-absorb." The fixture now cites `:86` (`corpus/fixtures/archives-r9/A-r9.md:50`); the r11 audit errata mark F1 closed at r12 (`corpus/knowledge/audit-r11.md:312-326`) | No. QUALITY.md has no freshness clause for skill text; the lane's own `LOG.md` and note are correct | "A closed finding is closed everywhere in the same landing; the skill carries no live open finding older than one round, and a correction is an appended erratum." |
| M-4 | restated ledger numbers diverge | `SKILL.md:376-378` says 71 rows / "by-design 38 · carried 23 · closed 7 · finding 0 · operator 3, queue 26", then the same paragraph says "27-item round-11 audit queue"; `SKILL.md:430-434` repeats "38 · carried 22 · closed 3 · finding 1 · operator 4" with the one live finding — a variant matching **no** recorded revision (pre-r12 §3.9: 38·25·3·1·4 / 30-item; r12: 38·23·7·0·3 / 26; r13: 38·22·8·0·3 / 25; r14: 38·21·9·0·3 / 25). `hardening-r10.md` revisions: r12 (`:486`), r13 (`:493`), r14 (`:512`) | No. QUALITY.md 2 requires *a* source, not one source of truth per number | "One number, one home: a restated count names the owning file + revision and is re-derived by a command, never copied by hand." |
| M-5 | unfilled template placeholder shipped | `corpus/knowledge/hardening-r10.md:488` — "Gate `91a01695…` → `${GSHA}…`" (`grep -c '\${GSHA}' corpus/knowledge/hardening-r10.md` → 1) | No | "No `${VAR}` template placeholder ships; a placeholder in a record is a defect, and the substitution command is part of the receipt." |
| M-6 | limit ledger stale by 8 rounds | `hardening-r10.md` addenda: 3 (`grep -cE '^### Round-1[0-9] addendum' …` → 3 = r13, r14, r15); **0** for r16–r23 (`grep -cE '^### Round-(1[6-9]|2[0-3]) addendum' …` → 0), although rounds 16–23 closed boundary classes (root `//` at r16; the r20 wave's ptr/denylist/fence classes at r21–r23) and added named limits, none is dispositioned there; the SKILL calls this file the one disposition home (`SKILL.md:430`) | Partly — those closures are in their round notes; the ledger is not updated | "Every closing round appends its disposition to the owning ledger in the same landing." |
| M-7 | stale daily reflection committed | `considerthese/2026-10-19.md:3` "4 commits, all between Oct 16 22:40 and Oct 17 12:56 BRT; nothing since." Measured: 8 commits in `2026-10-17 12:56 -0300` → `2026-10-19 09:07 -0300` (`git log --since='2026-10-17 12:56 -0300' --until='2026-10-19 09:07 -0300' --oneline | wc -l` → 8). `:16` cites "the hardening-r10 ledger (68 rows), the 27-item … queue"; `:11` repeats the C3 finding as awaiting fix. Note committed `efd9ba0` 2026-10-19 09:06:17 -0300, i.e. after round-12's dispatch commits (07:32–08:25 -0300) and minutes before the round-12 work commit `5691bf5` (09:12:19) | No. QUALITY.md 3 (observation/inference/unknown) does not bind a dated snapshot to its own window | "A dated reflection is a claim about its measurement window; it carries the exact `git log` command and window, and any later conflict gets an appended erratum, not silence." |
| M-8 | uncommitted prior-session work absorbed mid-wave | `tok_span_at` rewrite + `claims-cap-eof` case 123 absorbed and recorded (`SCORECARD.md:1040-1043`) | Yes — recorded explicitly in the round-20 verdict | — |
| M-9 | receipt cut withdrawn after a comparator artifact | first controls cut `20261016T054941Z` withdrawn; comparator ran against a receipt with no case lines (`corpus/evidence/README.md:928-932` Notes) | Yes — QUALITY.md 3 + 4 (unknown separated; append-only errata); the withdrawn cut is kept as a note | — |
| M-10 | seat deficit / not-dispatched wave, recorded not backfilled | r14 63/64 (seat 54 provider 400, `SCORECARD.md:683-684`); r22 antigravity "failed 24 seats on provider errors + 8 aborted" → luna (`SCORECARD.md:1138-1140`); r1 5/32 reports recorded `in-flight` (fleet `MANIFEST.json`, closure `round 1`, `lanes.chousa:"in-flight"`) | Yes — QUALITY.md 5 (rejection/deficit kept) | — |
| M-11 | calibration: score frozen while 19 verdicts say improved | `SCORECARD.md:7` operability 3, last-change round 1; rounds 2–23 record operability improved 19 times (`grep -c '| operability | \*\*improved\*\*' SCORECARD.md` → 19) | Partly — the lane deliberately refuses scalar scores (`SCORECARD.md:9-13`), but the one score it does keep is never re-derived | "A scored axis is re-derived by its own counting command at every landing, or explicitly marked `frozen at rN` with the reason." |
| M-12 | path/index misfiling | r12–r23 receipt rows (43) live inside `## Round-8 gate-baseline receipts` (`corpus/evidence/README.md:580`), which has no round-12+ headings (`grep -n '^## ' corpus/evidence/README.md` → headings end at Round-10, `:830`) | No | "An index row lands in the section for its round; a section heading is created before its rows." |

## 5. Contract defects

**D-1 — fleet ledger undercounts the lane (identity).** Fleet `rounds[]` holds 9 chousa craft
rows (15–23, all `ADMIT`) and closures whose `lane_rounds.chousa` reaches only **14**; no closure
entry exists for 15–23 (`python3 -c 'import json;m=json.load(open("../MANIFEST.json"));print([(x["round"],(x.get("lane_rounds") or {}).get("chousa")) for x in m["rounds"] if "chousa" in (x.get("lane_rounds") or {})])'`
→ last value 14). Lane records 23 admitted. **Conflict, verbatim:** fleet hint "max recorded
round 23" is true for craft rows, false for the lane counter; the lane's `LOG.md`/`SCORECARD.md`
agree with 23, not 14.

**D-2 — capability table and LOG diverge.** 5 SCORECARD rows vs 13 acquisitions claimed by LOG
(3 at r12 + 1 r13 + 1 r14 + 8 at r15/17/18/19/20/21/22/23). `AXES.md` §Capabilities says rows
enter only through a round that demonstrates the capability running — the demonstrating rounds
exist; the rows do not.

**D-3 — missing required corpus file for the wave-2 contract.** No `corpus/SOURCES.md`
(`ls corpus/SOURCES.md` → "No such file or directory"). The contract in this wave creates it;
the lane's frontier (source hierarchy, citation chaining) is the natural first consumer.

**D-4 — skill text vs artifacts (three separate contradictions).** See M-3/M-4/M-5. The skill is
the lane's teaching surface; a reader acting on `SKILL.md:434` would chase a finding that is
already closed, and on `:430-434` would cite a ledger variant that predates the r12 revision and
matches no recorded one.

**D-5 — stale indexes.** `corpus/README.md:50` count line; `## Frontier` stops at round 10
(`corpus/README.md:306-471`); two unindexed files; evidence index has no r12+ sections (M-12).

**D-6 — metadata registry not machine-checkable.** 3 notes lack `recheck:`; 0 `recheck:` values
are dates, so the "overdue (before 2026-10-19)" sweep has no input. `QUALITY.md` (5 criteria,
300 B, "probation draft") does not mention the fields.

**D-7 — clean tree, one ignored path.** `git status --porcelain` → 0 lines; `git status
--porcelain --ignored` → one entry, `.ufo/interactive-sessions/` (ignored at `.gitignore:1`). No
stray tracked artifacts.

**D-8 — size.** Gate script 5,217 lines / 223,477 B for a method lane; `SKILL.md` 434 lines of
mostly prose history (the lane's own reflection proposes a distillation pass,
`considerthese/2026-10-19.md:18`). `LOG.md` + `SCORECARD.md` + `corpus/README.md` = 249,495 B
(`wc -c LOG.md SCORECARD.md corpus/README.md`).

**D-9 — terminology.** Round-23's commit uses "honest-stop" (`77bcfd1`), a term the protocol
defines only for exploratory claims (`PROTOCOL-APPENDIX.md:50`: "unjudged, they land
`unprovable` and honest stop applies"). Round 23 is a measurable claim, not exploratory; the
report instead says "No wave" (`.ufo/reports/round-23/chousa.md:40`).

**D-10 — round 24 is an open registration with no report.** Claims + before-receipts + a
dispatched 64-seat wave (`LOG.md:816-819`) and no verdict or report. Under the lane's own
append-only rule this is neither admitted nor closed; the next landing must disposition it
before a fresh round number is used.

## 6. Conflicts verbatim (for the canonical judge)

1. `SCORECARD.md:1174-1176`: "one 16-seat AgentSwarm call, **devin swe-2**" — vs `LOG.md:804`:
   "direct integration (no wave — claim's before→after already measured by the r20 wave's live
   reproduction)" — vs commit `77bcfd1`: "round-23: report (no wave — direct integration per
   honest-stop)".
2. `SKILL.md:432-434`: "the one live finding … remains open pending fix-or-absorb" — vs
   `corpus/fixtures/archives-r9/A-r9.md:50` (row C3 cites `:86`) and
   `corpus/knowledge/audit-r11.md:312-326` ("finding closed; 18/19 is the pre-fix measurement").
3. `SKILL.md:376-378`: "71 rows at the r12 revision (by-design 38 · carried 23 · closed 7 ·
   finding 0 · operator 3, queue 26" and same paragraph "the 27-item round-11 audit queue" — vs
   `hardening-r10.md:512`: "71 rows … by-design 38 · carried 21 · closed 9 · finding 0 ·
   operator 3; round-11 queue **25 → 25**".
4. `considerthese/2026-10-19.md:3`: "4 commits, all between Oct 16 22:40 and Oct 17 12:56 BRT;
   nothing since." — measured 8 commits in that window and 12 commits between 09:06 and 12:00
   -0300 on 2026-10-19 (`git log --since='2026-10-19 09:06 -0300' --until='2026-10-19 12:00
   -0300' --oneline | wc -l` → 12).
5. Fleet `MANIFEST.json` `lane_rounds.chousa` max 14 — vs 23 admitted in `SCORECARD.md` and 9
   craft rows 15–23 in the same ledger.
6. `SCORECARD.md:1221-1224`: "opencode-go key 7 / deepseek-v4.1-flash … Seats: 64" — vs
   `LOG.md:819`: "**openai-codex gpt-6-luna-max** (opencode-go-7 interrupted at 17 seats; luna
   per the fallback ladder)".
7. `corpus/README.md:50`: "Count: 20 entries, ten knowledge notes and ten lessons" — vs 24
   knowledge and 11 lesson files on disk.

## 7. Proposed round (next fresh number; r24 must be dispositioned first)

Assumes round 24 closes (landed or recorded abandoned) and the next landing is round 25. The
lane's rule is 1–3 falsifiable claims on distinct axes, ≥1 on the lowest non-retired axis
(operability, 3). The three claims below are causally separable: each verifies without the
others landing.

**Claim 1 — operability (lowest non-retired axis): a metadata screen for corpus notes.**
New `verify-meta <file|dir>` (or a `verify` extension) checks the three opening keys
`source:` / `verified-at:` / `recheck:` on `corpus/knowledge/*.md` and emits named findings
(`META_SOURCE_MISSING`, `META_VERIFIED_AT_MISSING`, `META_RECHECK_MISSING`, warn, drift).
Before: `grep -c 'verify-meta\|META_RECHECK' tools/research-gate.sh` → 0, so the missing key is
invisible to every mode (not measured by running `verify` on those three notes — [INFERENCE]
that they close CLEAN, since they share the verified note's record shape; only
`archived-export-intake.md` has a recorded `verify` run).
After: the three would DRIFT naming their finding; the 21 conforming notes stay CLEAN; selftest
133 → 133+k with cases 1–133 `cmp` byte-identical vs the
r23 receipt (`fanchor-r23-20261019T192000Z-selftest.log`). Landed note:
`corpus/knowledge/meta-fields-r25.md` (field contract, the 3 measured absences, limits: it
checks presence/shape, not truth — QUALITY.md 5 already says a source anchor is required).
`SOURCES.md`: two `own-work` rows (gate; this dossier) — no external source is needed for a
lane-internal format.

**Claim 2 — freshness: re-derive the indexes.** `corpus/README.md` count line becomes a command
output; Frontier gains rows for rounds 11–23; the two unindexed files gain rows; the evidence
index gains `## Round-12…23` sections. Before: `grep -c 'Count: 20 entries' corpus/README.md` →
1; `grep -cE '^Round (1[2-9]|2[0-3])' corpus/README.md` → 0; unindexed files = 2; evidence
headings for r12+ = 0. After: 0 / ≥12 / 0 / ≥11. Landed note: `corpus/knowledge/index-derivation-r25.md`
(the counting commands, the 2-file census, why an index row is a claim).
`SOURCES.md`: `own-work` rows for the gate receipts each Frontier row cites (r12–r23).

**Claim 3 — calibration: reconcile the record, append-only.** Append an erratum block to
`SKILL.md` (or a `corpus/knowledge/errata-r25.md` cited from it) that closes the A-r9 C3 finding
in the skill text, replaces the three ledger-total statements with one line naming
`hardening-r10.md`'s current revision, and substitutes the `${GSHA}` placeholder; extend the
hardening addenda through r23 in one block. Before: `grep -c 'open pending fix-or-absorb'
SKILL.md` → 1; `grep -c '\${GSHA}' corpus/knowledge/hardening-r10.md` → 1;
`grep -cE '^### Round-(1[6-9]|2[0-3]) addendum' corpus/knowledge/hardening-r10.md` → 0. After:
0 / 0 / ≥8 (or 1 block covering r16–r23 with the same count of dispositions). Axis: calibration
— self-assessment matches observed state (`AXES.md:15`).

Not proposed: any external-source research. That needs an operator-approved window; none is on
file (`PROVINCE.md:14-15`; `MINT.md` "Secrecy guard" — "Pending is not approval").
`corpus/SOURCES.md`'s first rows should therefore be `own-work` + fleet `docs`
(`PROTOCOL.md`, `AXES.md`, `MANIFEST.json`); external methodology rows wait for approval.

## 8. Limits of this dossier

- Every number was read from files or git; no gate mode was executed and no selftest was re-run
  (the wave is read-only; receipts on disk were used instead: `corpus/evidence/fanchor-r23-*.log`
  carries `PASS (133 cases`). The one live check available (`bash tools/research-gate.sh
  --selftest`) was deliberately not run.
- "Overdue recheck" is reported as not computable, not as zero overdue: 0 `recheck:` values are
  dates (command above).
- Fleet-side claims are limited to `MANIFEST.json`; fleet `LOG.md`, `SCORECARD.md`, `CORPUS.md`
  contain 0 occurrences of "chousa" (`grep -c 'chousa' ../LOG.md ../SCORECARD.md ../CORPUS.md`
  → 0/0/0), so no fleet narrative cross-check was possible.
- Counts of the fleet roster and promotions come from `../MANIFEST.json` at this HEAD; the roster
  has no `promotions` key at top level (checked).
