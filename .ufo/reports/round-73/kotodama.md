# kotodama round 73 — conlang-scholarship assimilation + calibration ledger

Lane: kotodama-shokunin · base `8841ad3` · lane HEAD `c1b5b4761b6ae5ef9ffd81267c3e5e2189ed428d` (`git ls-remote origin refs/heads/main` prints it) · 2026-10-25, hyaku run 7, L1 KotodamaR73, attempt 1. Round shape: two v1 waves — w1 37 seats (policy v1) + w2 33 seats = 70 seats (≤100); no residual `task` call. Planner seat = the L1 (validator rejects `planner`).

## Work performed

Declared claims (2, frozen pre-data at `reports/round-73/claims.json`, freeze commit `af65165`): **C** (coverage, assimilation-sourced — shokuknow `merge/kotodama` conlang-scholarship theme: two entries, five rows) and **Ca** (calibration, records — eight-pair self-assessment-vs-repo ledger plus round-72 routed defects R1–R3). Lowest-axis obligation: SCORECARD holds no numeric scores and freshness is paused under L0 `kotodama | round-11` (`.ufo/l0-questions.md:47`); no nudge waiver claimed.

- Wave 1 (37 seats: 11 scout, 6 scribe, 6 executor, 5 critic, 4 reviewer, 2 connector, 1 mutation-tester, 1 sentinel, 1 simplifier; 19 m_flash-class, 10 attack) re-opened every source, drafted entries/counters/ledger, and attacked the draft claims; 34 reports, **3 dead seats not replaced: ConnectorSiblings, ScribeMistakes, ExecScratchMirror** (no report; results.json shows output lost to an orchestrator kernel restart). Applied as `pre_data_corrections` in claims.json.
- Freeze `af65165`: claims, `ledger.json`, counters, do-nothing controls (`controls-c.txt` 1/11, `controls-ca.txt` 5/9), selftests (C 29/29; Ca 9 scenarios), evidence captures, scratch-mirror receipt, collision guard proof.
- Ca landing `e62d731`/`3537899`: SCORECARD `## Corrections — round 73`, SHONEN pointers, SKILL.md gate rows, R2 rerun receipt `reports/round-73/telemetry/measures-ca72-rerun.txt`, round-72 seat reports tracked.
- C landing `85f17eb` (+ shape repairs `0316b88`): entries `corpus/knowledge/linguistics/conlang-scholarship.md` and `.amend-2026-10-23.md`, rows S876–S880, `corpus/lessons/round-73.md`, QUALITY 22/23, README footer.
- Wave 2 (33 seats: 8 critic, 6 scout, 4 reviewer, 4 executor, 4 mutation-tester, 2 connector, 2 scribe, simplifier, revenger, sentinel; 17 m_flash-class, 16 attack): 32 of 33 reports returned; **RevengerOrigins returned no report by filing time** (no WAVE-DONE received; not replaced). Findings repaired in `7aa8f99`/`2d1cd91`: false statements in the admitted amendment (parody/sign/graphic; "could not say what any taxonomy contains"), locators one page early, base header extraction method and 15 uncited pages, S894 Gate ground ("no Wayback capture" — false: canonical page has two 200 captures), SKILL rows (selftest count, exit-2 claims, `--fleet-root`, `legs=<n>/11`). Lessons: QUALITY 22, 23, 24.
- Evidence pointers: `corpus/lessons/round-73.md` (`## Gate`, `## Mistakes` R73-M1..M8, `## Corrections`), `.ufo/waves/round-73/w1/`, `w2/`, `reports/round-73/`.

## Landed changes

Every change is tied to the `LOG.md` round-73 entry: `af65165` freeze · `e62d731`, `3537899` Ca · `85f17eb`, `0316b88` C · `7aa8f99`, `2d1cd91` wave-2 repairs · `c1b5b47` LOG + SCORECARD (`## Axes — round 73`). Lane pushed: `c1b5b4761b6ae5ef9ffd81267c3e5e2189ed428d`.

## Before → after measurements

- **C** — before (base `8841ad3`): `find corpus/knowledge -iname '*conlang-scholarship*' | wc -l` = 0; 799 registry rows, 0 naming the five source hosts (`reports/round-73/telemetry/gap-sweep.txt`). After: `python3 -B reports/round-73/accept-c.py --root . --lands 2d1cd9140d3a6c42296d71e4f29587582a4a88c0` → `ACCEPT-C-73: PASS legs=11/11`; 804 rows; 247 knowledge files.
- **Ca** — before: 8/8 ledger pairs red, 2 files untracked (`controls-ca.txt`). After: `python3 -B reports/round-73/accept-ca.py --root . --lands 2d1cd9140d3a6c42296d71e4f29587582a4a88c0 --fleet-root /home/vgpnk/Projects/shokunin` → `ACCEPT-CA-73: PASS legs=9/9` (counter r3; r1→r3 disclosed in `reports/round-73/counter-revisions.md`, one bug fix + one guard, predicate unchanged).
- **Honest limits:** wave-2 mutation/junk seats show counter survivors (junk landings pass 11/11; config read from graded tree; ledger constant-printers via `python3 -c`; SEPARABLE wider than the frozen wording) — frozen predicates not amended, hardening routed to round 74. Claim verdicts are author-side; non-author closure rules.

## Sources & frontier

`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama`: exit 0 at start (799 rows, `census-start.txt`) and end (804 rows, `census-end.txt`). Rows added: 5, all tier B, all mined (S876–S880; S877 tier B not the scout's A). Rows touched old→new: none. Frontier ground entered: constructed-language scholarship. Assimilation: ADOPTED one theme (conlang-scholarship), two entries; collision guard 0–3-space proved (`guard-proof/`), staged→lane map by document (S881→S876, S882→S877, S892→S878, S893→S879, S901→S880), scratch-mirror census exit 0 before append. Not adopted: the remaining staged conlang amendments and the naming/calendar/era/verification families (reason+flip in the lesson). Known open defect: the S879 row's durability clause is false (the capture carries the span); the superseding row is routed because the frozen ROWS leg admits five rows. `considerthese/`: absent for this lane (no such directory).

## Trend verdicts

- **expansion: improved** — two admitted files on one newly entered ground, citing five rows mined this round (caveat: an amendment co-admitted with its base is one ground).
- **quality: unchanged** — no existing entry re-verified/deepened/superseded; repairs were to this round's own entries and records (criterion 20).
- **discernment: unchanged** — QUALITY 22/23/24 are lane-authored from lane-internal measurements; no outside spot-check of this round's gate yet.

## SHONEN

- [~] Box 1 — SKILL.md decision tables/error patterns/checklists; pointers corrected to `SKILL.md:505`/`:564` (ledger L04/L05); no non-author verifier on record.
- [~] Box 2 — end-to-end domain task: five sources re-opened live, rows and entries landed with evidence captures (`reports/round-73/evidence/`); wave-2 per-sentence fact-checks (`.ufo/waves/round-73/w2/CritFact*.md`); no non-author verifier on record.
- [~] Box 3 — executable by an agent without oral context: counters re-run from fresh clones by wave-2 `ExecRerunC`/`ExecRerunCa`; no non-author verifier on record.
- [~] Box 4 — no cross-domain bleed: scope check `.ufo/waves/round-73/w2/ConnectorAdjacency.md`, gap sweep over 20 sibling lanes (`telemetry/gap-sweep.txt`); no non-author verifier on record.

Stale-lane: none (respawn-per-round driver). Tool installs: none. Open L0 questions: none appended. Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` showed no round-73 stray from this lane's seats (only driver state file `.ufo/state/kotodama.report-baseline`, untouched).
