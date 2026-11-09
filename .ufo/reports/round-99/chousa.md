# chousa — round 99 report (L1 `ChousaR99`, attempt 1)

Lane repo `chousa-shokunin`, branch `master`. Base `47ed34fa785288837f84cde9db15c41300854a78` (round-98 landing plus its
non-author spot-check). Final lane hash `ab280f6c9b9f381085583daedbad6ff0a6b85fe1` (ls-remote below). No earlier attempt of
round 99 existed (`.ufo/watchdog.log`: one `launch chousa round=99 … attempt=1` line); nothing inherited.

## Work performed

Declared claims (frozen at F `d41f4cd8`; wave-forced re-freezes F2 `96d761ee` (A1-A7, B1-B2) and F3 `c3bad643` (B3-B6);
`.ufo/waves/round-99/claims.md`, `claims.json`):

- **C1 `C1-GATE-CHALLENGE-R99` — operability** (the lowest axis, historical 3/10): `tools/gate-records.py verify` gains a
  CHALLENGE code — a url/admit record, or a rev record on `corpus/captures/<24 hex>.txt`, fails when its capture text has at
  most 200 words and carries one of 11 frozen challenge markers. Battery `corpus/evidence/round99/challenge-controls-r99.py`.
- **C2 `C2-ENTRY-R99` — coverage, sourced on S236 and S233 (both opened this round)**: new entry
  `corpus/knowledge/quotation-error-rates-r99.md` — how often a cited source fails its citing sentence (Jergas & Baethge
  2015 abstract via Europe PMC; Mogull 2017 PLoS One full text), 23 located quotes, 8-row decision table. Controls
  `corpus/evidence/round99/entry-controls-r99.py`.

Work items:

- Fresh-start rule: not bound (MANIFEST closures r91-r98 admitted). Round-98 spot-check routed defects: 1 (claims.json F3
  placeholder) → convention in `plans/round-99.md` `## Freeze` and lesson Mistakes 2; 2 (R32) → SCORECARD `## Planned — round
  100` item 3; 3 (gate admits challenge page) → C1.
- Approval table before the first GET: `corpus/evidence/round99/egress-approval.md` (one row appended between GETs, disclosed
  in the file); five GETs, `corpus/evidence/round57/refetch.tsv` rows S232-S236.
- Do-nothing controls committed at F: `corpus/evidence/round99/before/c1-base.txt` (base tool: `NEG_REFUSED=0/7
  PROD_REFUSED=0/4`, FAIL, exit 1), `before/c2-base.txt` (entry absent, gate exit 2, controls exit 2, 0 base topic hits).
  Forgery/detection controls are in the batteries (C1 oracles o1-o5 incl. QUALITY 126 detection forgers o4/o5; C2 forgeries
  f1-f10 and accept edits a1-a2), committed at F.
- Pre-freeze change P0 (`plans/round-99.md`): CHALLENGE extended to rev records on capture paths, with two rev PROD legs.
- One v1 wave, 12 seats (`.ufo/waves/round-99/w1-dispatch.json`, validated under `scripts/hyaku/ufo-wave-policy.json`);
  seat reports `.ufo/waves/round-99/w1/R99*.md`; results `.ufo/waves/round-99/w1-results.json` (12/12).
- Wave-forced amendments with seat artifacts (`claims.md` `## Amendments`; `plans/round-99.md` `## Amendments (F2)`/`(F3)`):
  C1 A1 (28-word fixture), A2 (battery docstring o3-o5), A3 (separability: battery reads two C2 captures and the C2 entry;
  probe `corpus/evidence/round99/after-f2/c1-separability.txt` PASS with C2 deleted), A4 (rev guard keyed to path spelling,
  `R99SentinelC1` F-1), A5/A7 (markers, bound, rev whole-blob check not shown live by the battery, `R99MutantsC1` 13/28
  survive), A6 (committed marker-less zh challenge page admitted, `R99RevenPrior`); C2 B1 (Never cells and number sense
  unchecked), B2 (tameshi holds Europe PMC records of both papers), B3-B6 (entry scope sentence, row 1, 27-vs-28 studies,
  spelled-out numbers; `R99ScoutSources`).
- Falsification ledger `.ufo/waves/round-99/claim-falsification.tsv` (16 rows, every attack seat; 10 falsifies-wording,
  each narrowed in `plans/round-99.md`). Gate line below.

## Landed changes

| commit | what | LOG.md |
|---|---|---|
| `d41f4cd8b857c6de683e7be5c5e8125b32763a8e` | freeze F: tool, batteries, entry, S232-S236, captures, refetch rows, before receipts, census start, egress table, plan, claims | Round 99 |
| `f8f480ffd738cda9b427e0fe8fa8e79c78fb409d` | carrier: F hash in plan, after receipts at F, wave spec, dispatch, ready | Round 99 |
| `96d761eec0c006d3df100b1a5d41686568d6d1e1` | re-freeze F2: A1-A7, B1-B2, battery docstring, separability probe | Round 99 (corrections at F2) |
| `c3bad643c42ecd1f04620bd6acfddb01d69c4aa3` | re-freeze F3: B3-B6 (entry prose, named limits); C1 receipt at F2 | Round 99 (F3) |
| `7fa312acaa266913bda8a34cc751f1eafe01eb52` | landing: C2 receipt at F3, census end, lesson, LOG, SCORECARD, QUALITY 230, README, SKILL correction, ledger, seat reports, wave results | Round 99 |
| `ab280f6c9b9f381085583daedbad6ff0a6b85fe1` | sentinel strace receipt (gzip of a 12.9 MB seat file, `zcat \| cmp` verified) | Round 99 |

## Before → after measurements

**C1** (measured at F2 `96d761ee`; tool bytes identical F..HEAD; `corpus/evidence/round99/after-f2/c1-all.txt`)

    python3 -B corpus/evidence/round99/challenge-controls-r99.py --root . --work <scratch>

- before (base tool `47ed34fa` under the battery, `--no-oracles`; `before/c1-base.txt`): `NEG_REFUSED=0/7 POS_ADMITTED=4/4
  PROD_REFUSED=0/4 HARM_SAME=25/25 BASE_NEG_ADMITTED=7/7`, `CHALLENGE_CONTROLS_R99=FAIL`, exit 1.
- after: `NEG_REFUSED=7/7 POS_ADMITTED=4/4 PROD_REFUSED=4/4 HARM_SAME=25/25 BASE_NEG_ADMITTED=7/7 ORACLES_REJECTED=5/5`,
  `CHALLENGE_CONTROLS_R99=PASS`, exit 0.

**C2** (measured at F3 `c3bad643`; `corpus/evidence/round99/after-f3/c2-all.txt`; first measured at F, `after/c2-all.txt`)

    python3 -B tools/gate-records.py verify --root . corpus/knowledge/quotation-error-rates-r99.md
    bash tools/research-gate.sh verify-metadata corpus/knowledge/quotation-error-rates-r99.md --root .
    python3 -B tools/search-rerun.py verify corpus/knowledge/quotation-error-rates-r99.md --root .
    python3 -B corpus/evidence/round99/entry-controls-r99.py --root .

- before (`before/c2-base.txt`): entry absent, `GATE_RECORDS_ERROR missing …` exit 2; controls exit 2; no knowledge entry at
  base contains "quotation error" (0).
- after: `GATE_RECORDS files=1 records=25 ok=25 fail=0`; `METADATA_COMPLETE=1/1`, `RESEARCH_GATE: CLEAN`; `rev_match=4/4`,
  `SEARCH_RERUN: CLEAN`; `QUOTES=23/23 FIELD=9/9 IDENTITY=2/2 WARRANTS=8/8 NUMBERS=6/6 TOPIC=1/1 NUMBERS_SOURCED=6/6
  BASE_TOPIC_HITS=0 BASE_ENTRY=absent FORGERY_REFUSED=10/10 ACCEPTED=2/2`, `ENTRY_CONTROLS_R99=PASS`; all exit 0.

## Sources & frontier

- Census before → after: `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin chousa` → exit 0 both
  (`corpus/evidence/round99/census-start.txt`, `census-end.txt`; warnings identical, 7 W-lines). Registry rows
  (`grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' corpus/SOURCES.md`): 230 → 235.
- Rows added by tier: S233 A (`mined`), S236 B (`mined`); S232 A, S234 A, S235 B (`rejected`: 403; http-200 "Client
  Challenge" page; 500). Gate lines with URL, access date and ≤25-word located quote: `corpus/lessons/round-99.md` `## Gate`
  (GATE-RECORDs verify `ok=4`).
- Rows touched old→new: none.
- Frontier advanced: README Round98's "gate-records admits a quote from an http-200 challenge page" closed for the 11 marker
  wordings (QUALITY 230); claim-vs-source verification gains its empirical side (`corpus/README.md` `## Round99 coverage and
  frontier`). S235's flip condition was met by a seat's re-open (not a lane GET), routed.
- Sourced claim: C2 cites S236 and S233 (opened this round). Mistakes mined: 4 (`corpus/lessons/round-99.md` `## Mistakes`).
- Assimilation: none. considerthese: not mined this round.
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` → only orchestrator-owned `.scratch/` entries; no
  seat file at the fleet root.

## Trend verdicts

- expansion: **improved** — one knowledge entry on ground no entry or capture held (`before/c2-base.txt` 0 hits); registry
  230 → 235.
- quality: **improved** — the gate refuses 11 challenge-page records the round-98 gate admitted, with byte-identical output on
  25 committed files (`after-f2/c1-all.txt`).
- discernment: **improved** — S234 (http 200 challenge page) and S232/S235 refused with reasons, S236 graded B under the
  carrier rule (tameshi grades the same carrier A: routed), ten wave findings narrowed before filing. Author-measured;
  non-author closure pending.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md` round-99 correction line after the round-98 one (lane assertion; no non-author verifier named)
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md` `## Round 99` (search, five GETs, entry, gates)
- [~] Instructions executable by an agent without oral context — `python3 -B corpus/evidence/round99/challenge-controls-r99.py --root . --work <scratch>`; `corpus/evidence/round99/after-f2/c1-all.txt`
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` untouched; tameshi overlap routed (`R99ConnectorSiblings`)

## Round shape and extras

- Shape: one v1 wave, 12 seats, policy v1 (band 8-16): executor 2, mutation-tester 2, reviewer 2, critic 1, sentinel 1,
  scout 1, revenger 1, connector 1, scribe 1; attack share (reviewer, critic, mutation-tester) 5/12. L1 holds the canonical
  planner seat (the validator refuses `planner`). Residual call: none. Round total: 12. Dead seats: 0 (12/12 settled with
  reports). Seat routes per `task.agentModelOverrides` (not passed).
- Pre-file ledger: `python3 scripts/hyaku/prefile-falsification.py --lane chousa --round 99` →
  `PREFILE-FALSIFICATION: pass claims=2 rows=16 attack_seats=8 findings=0`, exit 0.
- Defects of seats recorded: `R99ExecC1Repro` left its scratch dir (removed by the L1 after landing); `R99MutantsC2` wrote
  receipts without its seat prefix (`w1/M01-…`); `R99SentinelC1` wrote a 12.9 MB strace receipt (committed gzipped).
- L1 process note: one README wording edit was made with `sed -i` instead of the edit tool (content verified by grep).
- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
- Tool installs: none (L1; seats report none).
- L0 questions: none opened this round. Routed fleet question (not L0): one tier rule for index-record abstracts.
- Final lane hash: `git -C chousa-shokunin ls-remote origin refs/heads/master` → `ab280f6c9b9f381085583daedbad6ff0a6b85fe1`.
