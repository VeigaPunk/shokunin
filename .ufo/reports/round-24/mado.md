# mado — round 24 report (attempt 1)

Lane `/home/vgpnk/Projects/shokunin/mado-shokunin`, base `8e5d93691e2f7baa3d4a0a61c9428e5acb5d2122`, landed tip
`b02cf2946373a5343ef86876e5688b3210849137` (jj-lane `landed b02cf294…`, `state … ahead=0 behind=0`). Claims measured at
`eb14fa3d53d42c1568dd3fe2708c64eaf2024364`; the tip only appends the SCORECARD results section and the tip receipts.

## Work performed

Declared claims (registration `.ufo/waves/round-24/registration.md`, landed `8efd00af`, before any data seat):
- **C1 — coverage (sourced):** move the corpus/README frontier item "rule *attribution*" to a sourced route,
  `corpus/knowledge/rule-attribution-r24.md`, built on SOURCES rows opened 2026-10-23.
- **C2 — calibration (lowest axis, round-17 rubric 7.1875):** count mismatches between SCORECARD's capability tables
  and what each capability's frozen re-demonstration command actually does.

Anti-loop: rounds 20–23 all worked the tripwire classifier; this round changes nothing under `tools/`.

- Repair first: all seven defects routed by `corpus/lessons/round-23-verifier-spotcheck.md` §7. 1) Appended a
  correction to lesson 23 (`d9fec1d3`). 2) Added a README pointer to the withdrawal (`d9fec1d3`). 3) Added QUALITY
  criteria 33–35, which cite M23-4/5/7, plus two checks that fail on round-23 bytes
  (`.ufo/waves/round-24/quality/`, `39c59630`). 4) Every sha256 now carries a `sha256:` label. 5) Re-opened S149: its
  span is `:1014-1015`, not the closure's `:1013-1014` (lesson 24, wave-2 dispositions). 6) Froze 28 regression
  fixtures from round 23 as `.ufo/waves/round-24/carry/` with no classifier change (`39c59630`). 7) H2 is not
  repaired; the L0 question at fleet `.ufo/l0-questions.md:103` is still open.
- Inherited leftovers: two round-23 seat reports were modified after that round closed, and a third report was
  never committed. Copies are kept at `.ufo/waves/round-24/inherited/r23-post-close-*.md` (`8efd00af`). The original
  paths were reverted to their committed bytes. This is recorded as lesson M24-3.
- Frozen counters: C1 `c1/count.py` v1 (`d9fec1d3`) and v2 (`c9b76646`, sha256:`b2f37c57…efc66`). C2 `c2/count.py` plus
  `manifest.json` (`4f21d995`, built by executor seat ExecC2Counter; sha256:`a2809501…`, `e02c76d1…`).
- Control wave (12 fresh seats, before data, receipts `.ufo/waves/round-24/controls/`, landed `464a0245`): the
  CtlC1LabelShortcut and CtlC1OffTopic controls both met counter v1 (`TARGET_MET`). Counter v2 adds a claim-anchor
  clause and was landed before any data seat; it scores both of those controls 0. No control met v2 or C2.
- C1 data: 17 source-opener seats plus scouts. The note answers the question: no channel in v0.56.2 maps an applied
  property back to the rule that set it. The usable route is a unique `tag` effect, read from `hyprctl clients`.
  SOURCES S153–S168 were added (S161 is queued); landed `cf86f9e0`.
- C2 data: the `### Capability status (round 24 re-demonstration)` table in SCORECARD (`81955bd5`). One
  capability's row now says `fails`: `tripwire evidence marker`, L 15/18 at present against the claimed 17/18
  (harm H2 from round 21).
- Wave-2 corrections (appended only, `eb14fa3d`): an errata section in the note, a C2 scope note in SCORECARD,
  README index rows for three notes left unindexed since rounds 21–23, and lesson M24-5 plus the wave-2 dispositions.
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows untracked fleet-root files
  (`bm.json`, `*.html`, `s395.txt`, `write`, `.ufo/state/*`, `scripts/hyaku/*.bak`). All of them are older than this
  round and none mentions mado, so none were moved.

## Landed changes

| Change | LOG.md entry | Lane commit |
|---|---|---|
| Registration, C1 counter v1, inherited copies | round 24 | `8efd00af` |
| C1 lane-path override; routed defects 1–2 | round 24 | `d9fec1d3` |
| C2 counter, manifest and base smoke | round 24 | `4f21d995` |
| C1 counter v2 | round 24 | `c9b76646` |
| Control receipts | round 24 | `464a0245` |
| C2 status table | round 24 | `81955bd5` |
| C1 note, S153–S168, README row and frontier bullet | round 24 | `cf86f9e0` |
| QUALITY 33–35, carry population, wave-1 reports | round 24 | `39c59630` |
| Lesson 24, LOG | round 24 | `87429be6` |
| Wave-2 dispositions (errata, scope note, index rows, reports) | round 24, wave 2 | `eb14fa3d` |
| SCORECARD results, end census, tip receipts | round 24 | `b02cf294` |

## Before → after measurements

| Claim | Command | Before @ `8e5d9369` | After @ `eb14fa3d` | Author verdict |
|---|---|---|---|---|
| C1 | `python3 -I .ufo/waves/round-24/c1/count.py REV` (counted re-fetch mode) | PASS_ROW 0, note absent, exit 1 (`evidence/c1-before-v2-8e5d9369.txt`) | PASS_ROW 23/26 from 14 sources, README indexed, `TARGET_MET`, exit 0 (`evidence/c1-after-eb14fa3d.txt`) | met under the frozen rule, but the rule is weak. Reviewer RevRegistration, critic CritC1Predicate and critic AtkC1Coverage each built a generic, non-attribution note that also reaches `TARGET_MET`. Of the 23 passing rows, 12 carry attribution content. The closure must judge the note itself. |
| C2 | `python3 -I .ufo/waves/round-24/c2/count.py REV` | `mismatches=1/12`, exit 1 (`c2/smoke/base-8e5d9369.txt`, `controls/CtlC2DoNothing.md`) | `mismatches=0/12`, exit 0 (`evidence/c2-after-eb14fa3d.txt`) | met over the 12 rows under `Capabilities` headings. The predicate's wording ("capability table") literally covers 15 rows: 3 have no command and one of those is stale. The landed table records the observed column, and two clean base runs were identical. |

No-harm at `eb14fa3d`:
- `tools/` is byte-identical to base.
- Round-23 C3 counter = 0; round-23 C2 counter = 3/3.
- Sources census exits 0.
- No lines were removed from LOG, SCORECARD, QUALITY, README or SOURCES; PROVINCE, SHONEN and SKILL are unchanged.

Wave-2 seat AtkNoHarm confirmed the same at `39c59630`.

## Sources & frontier

Command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin mado`.
At start and at end it printed the same 7 W04 lines (S030, S042, S045, S097, S119, S120, S121, all pre-round), then
`mado ok …/corpus/SOURCES.md`, rc=0 both times (`evidence/sources-start.txt`, `evidence/sources-end.txt`).

- Registry rows: 152 → 168 (`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`).
- Added: 16 rows, all tier A — 15 `mined` plus S161 `queued`. Twelve are Hyprland v0.56.2 code (`efb50993…`) and four
  are hyprland-wiki docs (`c66e8de2…`).
- Changes to existing rows: none.
- Lesson 24 `## Gate` gives a URL, the access date and a located quote of at most 25 words for every new row.
- Frontier: the round-12 item "Still open: rule *attribution*" is now on documentary sourced ground. Still open:
  attribution observed on this host, and plugin-side match recording.
- Sourced claim: C1 rests on S153–S168. Mistakes mined: lesson 24 M24-1..M24-5.

## Trend verdicts

- **expansion: improved.** A new entry covers the rule-attribution frontier and cites 15 `mined` rows opened this
  round. All 16 new rows were re-opened in wave 2 and every one held. Caveat: the counted rows overstate the depth of
  coverage (12 of 23 are attribution content).
- **quality: improved.** Routed defects 1–6 were repaired. QUALITY 33–35 come with checks that fail on round-23
  bytes, though wave 2 left survivors. Three notes that had gone unindexed are indexed again. Wave-2 errata correct
  five prose errors in the new note.
- **discernment: improved.** The pre-data controls caught a counter flaw (v1), which was fixed before data. Wave 2's
  own attacks found the remaining counter weaknesses in C1 and C2, and both are reported as lesson rows rather than
  fixed after data.

## Gate

Real rejects:
- Counter v1 was rejected because two controls met it (lesson M24-1).
- Row S161 was demoted to `queued`: its only quote breaks the table.
- WikiTags, SrcMatchEngine and ScoutWikiEra rows, plus the Lua query row, were not registered: they are not
  attribution content.
- The closure's S149 span `:1013-1014` is rejected against the bytes (the span is `:1014-1015`).

## Round shape

Default two v1 waves plus a pre-freeze control call:
- W0: 1 executor (C2 counter).
- Controls: 12 seats (7 mutation-tester, 5 critic).
- W1: 35 seats (21 scribe, 5 scout, 4 executor, 3 critic, 1 connector, 1 reviewer).
- W2: 40 seats (15 reviewer, 12 critic, 10 scout, 3 mutation-tester).
- Total: 88 seats. Dead seats: none. Cancelled seats: none.

Planner: the L1 holds the planner seat; ScoutPriorNotes did the planning data-walk. Routing was by role, with no
`model` passed. Tool installs: none.

`Stale-lane`: respawn-per-round driver; no other mission of this lane is open.

Process error: during the control wave the L1 sent a one-character message (`x`) to `agent://all`. It reached 101
peers. I acknowledged it to Main at once; it is recorded as lesson M24-4.

Open L0 questions: `.ufo/l0-questions.md:103` (H2, round 23), still open; none added.

## SHONEN

- [~] SKILL.md decision tables / error patterns / cited sources — unchanged this round (`SHONEN.md`).
- [~] End-to-end domain task logged — unchanged; no new end-to-end desktop task.
- [~] Instructions executable without oral context — unchanged.
- [~] No cross-domain bleed (PROVINCE accurate) — PROVINCE unchanged. ConnSiblingOverlap found that no sibling lane
  owns rule attribution (`.ufo/waves/round-24/w1/reports/ConnSiblingOverlap.md`).
