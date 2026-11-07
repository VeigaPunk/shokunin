# kumitate — round 95 report (hyaku run 15, attempt 1)

L1 `KumitateR95` (holds the §3 planner seat; the validator refuses `planner`). Lane repo
`/home/vgpnk/Projects/shokunin/kumitate-shokunin`, branch `master`, base `12aa450f` → final `03b2eb4fadb51403096a1209fd1214daf4168adf`.

## Work performed

Declared claim (one): **C1 — operability** (lowest non-retired axis; integer 9, terminal under `f_O`):
`scripts/round-gate.mjs` reads a `corpus/SOURCES.md` registry row's cells only in the census shape
(`line.split('|')` = 13 fields, CORPUS.md `NF==13`); any other registry row declares no pin and is listed by id, in
file order, in the always-present `--json` `citations.malformedRows`. Routed defect: r94 spot-check §5 item 3 /
K94Sentinel S94-5 (a truly `rejected` row with an unescaped `|` still declared its pin). Not exploratory; no
capability row. Sourced on S273 (GFM tables) and S274 (POSIX awk), both opened this round.

- Pre-freeze adoption of the round-94 spot-check into the README map (M94-1 ordering): `eadd519d`,
  `.ufo/waves/round-95/close-l1/adopt-r94-spotcheck.txt` (map DRIFT → CLEAN before the freeze).
- Freeze `ee8479be` — `plan.md`, frozen counter `probe/probe95-c1.mjs`, generator `probe/make-controls95.py`,
  8 pre-data controls (`controls/`), open receipts (`open/`).
- Wave w1 spec + validated dispatch `65c3374d` (`w1-spec.json`, `w1-dispatch.json`, v1 policy).
- Integration M `ce58e03e`: K95ExecTool candidate (READY `c5a2f8ac…`) + L1 changes (r94 text line kept; new
  `SOURCES_ROWS_MALFORMED` info line; arm (xviii) fixed to 14 fields; clause arm (xxi) + text arm), selftest 79 → 88;
  S273/S274 rows; knowledge `corpus/knowledge/round-gate-registry-shape.md`; QUALITY Q89; `SKILL.md:610` round-gate
  exit-code → verdict map (r94 spot-check §5 item 6); re-mutation 15/15 (`close-l1/integration-remut.txt`).
- Close `89215d7a`: lesson `corpus/lessons/round-95.md`, LOG r95, SCORECARD move-log/disposition/r94 word-count
  correction (r94 spot-check §5 item 4)/r96 pre-registration, `close/probe1.txt`, `close/probe2.txt`, `close/battery-M.txt`.
- M2 `a59fbedc` (after K95Mutation): arm (xxii) kills survivor `checkafterreject`, selftest 89/89
  (`close-l1/survivor-remut.txt`); counter at M2 HELD twice (`close/probe-m2-{1,2}.txt`).
- Wave evidence `abceb43b`; proxy re-declaration + final battery `1eb57084` (`close/battery-final.txt`);
  own-round gate receipt (Q88) `03b2eb4fadb51403096a1209fd1214daf4168adf` (`close/q88-r95.txt`).
- Round shape: ONE v1 wave, 10 seats — executor ×2 (K95ExecTool, K95ExecHarm), scribe ×2 (K95ScribeSources,
  K95ScribeLesson), scout (K95Scout), connector (K95Connector), reviewer (K95Reviewer), critic ×2 (K95CriticA,
  K95CriticB), mutation-tester (K95Mutation). Attack seats 4/10 = 40 %. No residual call; round total 10. Dead seats:
  0 (`w1-results.json`, all 10 settled with reports in `w1/`). Routes per `task.agentModelOverrides` (Amendment 48);
  no claim depends on a seat's answering model.

## Landed changes

| change | LOG.md entry | commit |
|---|---|---|
| r94 spot-check adopted pre-freeze | LOG `## Round 95` ("adopted … before the freeze") | `eadd519d` |
| freeze (plan, counter, controls, open) | LOG `## Round 95` "Declared … frozen at `ee8479be`" | `ee8479be` |
| wave spec + dispatch | LOG `## Round 95` "Wave w1: 10 seats" | `65c3374d` |
| round-gate rule + S273/S274 + knowledge + Q89 + SKILL row | LOG `## Round 95` "M = `ce58e03e`" | `ce58e03e` |
| lesson, LOG, SCORECARD close, README map | LOG round-95 one-line record | `89215d7a` |
| M2 arm (xxii), re-pin | LOG round-95 addendum | `a59fbedc` |
| wave evidence + M2 receipts | LOG round-95 addendum ("Wave w1: 10 seats, 0 dead") | `abceb43b` |
| proxy re-declaration + final battery | LOG round-95 one-line record (harm battery) | `1eb57084` |
| Q88 own-round receipt | LOG round-95 one-line record | `03b2eb4fadb51403096a1209fd1214daf4168adf` |

## Before → after measurements

C1 (frozen counter `node .ufo/waves/round-95/probe/probe95-c1.mjs --tool <gate bytes> --work <scratch> --freeze ee8479be66acd906f1d2b5f24f1b75a3d9172c1b`):

| measurement | before | after |
|---|---|---|
| counter on BASE bytes (`11f83a1a…`, do-nothing control, measured against `eadd519d`) | `C95_C1: UNMET a=0/1 b=0/1 c=0/78 d=1/1` (`controls/ctl-nothing.txt`) | — |
| counter at M `ce58e03e` (`7aaf0082…`) | — | `C95_C1: HELD a=1/1 b=1/1 c=78/78 d=1/1` twice (`close/probe1.txt`, `close/probe2.txt`) |
| counter at M2 `a59fbedc` = shipped bytes (`aba737dc…` = `pin.round-gate`) | — | `C95_C1: HELD a=1/1 b=1/1 c=78/78 d=1/1` twice (`close/probe-m2-1.txt`, `close/probe-m2-2.txt`) |
| fixture registry, BASE vs shipped | BASE `declared=[okA shiftB escC shortD indentF longG plainH]`, no `malformedRows` | `declared=[okA indentF plainH]`, `malformedRows=["S002","S003","S004","S007"]` = census awk ids |
| six forgery controls | all `UNMET a=0/1` (`controls/`) | shipped selftest kills all six + 9 K95CriticA constructions (15/15) + survivor `checkafterreject` |
| `node scripts/round-gate.mjs --selftest` | `79/79 pass` | `89/89 pass` |
| `node scripts/proxy-check.mjs --strict` | DRIFT (bookkeeping, `open/battery-before.txt`) | `PROXY: MATCH … operability=9 … coverage=10` (`close/battery-final.txt`) |

Kill rules: K1 not fired (HELD); K2 satisfied (all six forgery shapes killed by the shipped selftest); K3 harm battery
CLEAN at M and final; K4 `git diff --stat ee8479be ce58e03e -- plan.md probe controls open` empty.
Caveat (M95-2, K95CriticA): 9 rule-violating constructions reach HELD on the counter — its fixture draws each clause
once; the shipped bytes rest on the selftest arms and the reviewer's hand read. Framing (K95CriticB *sound*,
K95Scout): 0 malformed rows in 21 lanes and in all 74 kumitate registry revisions — a prospective fail-closed
agreement with the census, not a live defect.

## Sources & frontier

Census command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kumitate`.
- Round start: `kumitate ok …/corpus/SOURCES.md`, exit 0, 8 × W04 (`open/census-before.txt`), 210 rows.
- Round end: `kumitate ok …/corpus/SOURCES.md`, exit 0, 8 × W04 (`close/battery-final.txt`), 212 rows.
- Rows added by tier: A +2 (S273 spec, S274 spec), B 0, C 0. Rows touched old→new: none (no status/recheck/used-by change).
- Frontier rows advanced: S273, S274 (both `mined`, used by `corpus/knowledge/round-gate-registry-shape.md`; the
  sourced claim C1 cites them). Re-opened by the L1: `close-l1/l1-reopen-s273-s274.txt` (HTTP 200, sha256 matches the seat).
- Mistake mined: M95-1 (quote word counts not recounted; fix Q89 shown able to fail on r94 rc=1, pass on r74/r93,
  own lesson `WORDCOUNT: CLEAN pairs=2`, `close-l1/q89-round-95.txt`); M95-2 (counter clause coverage).
- Assimilation: none (no `merge/kumitate/` theme fits a gate parse repair). considerthese: not mined this round.

## Trend verdicts

- expansion: **improved** — new knowledge entry `round-gate-registry-shape.md`; SOURCES 210 → 212 (S273, S274 opened).
- quality: **improved** — the gate no longer reads cells of malformed registry rows (S94-5 closed), selftest 79 → 89
  with every forgery shape, construction and the mutation survivor killed; r94 word-count slips corrected append-only.
- discernment: **unchanged** (lane's self-grade; the outside closure grades it) — one admit/reject set on record
  (GFM-aware parsing rejected, counter-certifies-clauses rejected).

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md:610` round-gate row now carries its exit-code → verdict map (`ce58e03e`); checklist 723–725 run in `close/battery-final.txt`.
- [~] At least one end-to-end domain task executed and logged in LOG.md — LOG `## Round 95` (gate repair end to end: freeze → wave → M → M2 → battery).
- [~] Instructions executable by an agent without oral context — `node scripts/round-gate.mjs --selftest` → `89/89 pass`, `VERDICT: PASS`.
- [ ] No cross-domain bleed (PROVINCE.md still accurate) — PROVINCE.md untouched this round.

## Notes

- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
- Inherited state: none (lane clean at start, `jj-lane.sh state` tracked=0 untracked=0); no earlier attempt of r95.
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows only `trail-ids.txt` (1 byte, mtime
  20:36, before this round launched at 21:27) — not written by this round's seats; left untouched.
- Tool installs: none. L0 questions: none open from this round.
