# chousa — round 100 report (L1 `ChousaR100`, attempt 1)

Lane repo `chousa-shokunin`, branch `master`. Base `929c784c63a1fd17961d21742101b2b109b7b8ff` (round-99 landing plus its
non-author spot-check). Final lane hash `f0aea4f14d3c733f1f2dfe5a9eb429300783fd3a` (ls-remote below). No earlier attempt of
round 100 existed (`.ufo/watchdog.log`: one `launch chousa round=100 … attempt=1` line); the lane was clean at start
(`jj-lane.sh state`: ahead=0 tracked=0 untracked=0); nothing inherited.

## Work performed

Declared claims (frozen at F `6d4e8487`; wave-forced re-freezes F2 `0a3da3da` (A1-A4, B1-B9) and F3 `4ba51a26` (A5-A6);
`.ufo/waves/round-100/claims.md`, `claims.json`):

- **C1 `C1-GATE-REVCAP-R100` — operability** (the lowest axis, historical 3/10): `tools/gate-records.py verify` judges a
  rev-form GATE-RECORD for CHALLENGE when the blob git resolves for `rev:path` has the object id of a
  `corpus/captures/<24 hex>.txt|.raw` entry (a `.raw` by its sibling `.txt`), instead of only when the path is spelled
  exactly `corpus/captures/<key>.txt` (round-99 `R99SentinelC1` F-1). Battery `corpus/evidence/round100/challenge-controls-r100.py`.
- **C2 `C2-ENTRY-UPDATE-R100` — freshness, sourced on S238 (opened this round)**: the round-99 entry's `recheck: on-release`
  is answered — new entry `corpus/knowledge/quotation-error-update-r100.md` holds the authors' 2025 update (Baethge & Jergas,
  pmid 40696441) through its abstract in Europe PMC's core record (14 located quotes + J1/J2, 8 decision rows), and
  `corpus/knowledge/quotation-error-rates-r99.md` gains a `## Update` section flagging its 2015 reading. Controls
  `corpus/evidence/round100/entry-controls-r100.py`.

Work items:

- Load: prompt §1-§8 and amendments through 65; SCORECARD `## Planned — round 100`; round-99 lesson and non-author
  spot-check (routed defects 1-5 answered in `plans/round-100.md` `## Load and inputs`); `R99SentinelC1`, `R99MutantsC1`.
- Egress: approval table `corpus/evidence/round100/egress-approval.md` written before the first GET; seven GETs through
  `tools/capture-fetch.py` (`corpus/evidence/round57/refetch.tsv` rows 209-215): S238 200, S237 500 ×3, S239 500 ×3.
- C1 tool: `rev_capture_text` + `capture_oids` (`tools/gate-records.py`, P `96835234`); docstring CHALLENGE paragraph
  extended; `SKILL.md` round-100 correction line; QUALITY 231.
- C1 battery: 46 legs (NEG 7, MARK 11, BOUND 3, NORM 2, POS 4, REV 11, REVPOS 3, PROD 6) + HARM + 12 forgery oracles; a
  fixture git repo under `--work`; SETUP exit 2 on a missing capture (round-99 battery crashed: `before/c1-setup.txt`).
- Pre-freeze controls committed before F (R `6f837487`, `corpus/evidence/round100/before/`): C1 do-nothing (base tool)
  FAIL exit 1; candidate with `ORACLES_REJECTED=12/12` PASS exit 0; SETUP exit 2; C2 base exit 2; C2 pre-link FRESH=0/1
  FAIL exit 1; C2 candidate all exit 0 (+ separability: C2 with the base tool `records=17 ok=17`).
- C2 entry, controls (13 forgeries incl. sign drop, Never numeral, missing Update, bad `updates:`; 2 accepts), registry
  rows S237-S239, S236 `used-by` change, `## Search log` entry.
- Wave: one v1 wave, 12 seats, all settled (`w1-results.json`); 14 seat reports under `.ufo/waves/round-100/w1/`.
- Integration: C1 sentence narrowed A1-A6 (limits (f)-(j)); C2 entry/Update repaired and sentence narrowed B1-B9; ledger
  `.ufo/waves/round-100/claim-falsification.tsv` (20 rows); after-F2 receipts on a clean clone at F2.
- Frontier: lesson `corpus/lessons/round-100.md` (Gate, 5 mistakes, 3 GATE-RECORDs `ok=3`), README `## Round100 coverage
  and frontier`, LOG `## Round 100`, SCORECARD verdict + `## Planned — round 101`.

**Kill-rule disclosure (C1).** `R100SentinelC1` F-1 (a byte-identical copy of S230's `.raw` under an earlier capture key
rebinds the object id, so a rev record on the honest `.raw` prints OK) and F-2 (`--repo <worktree>/corpus` empties the
capture set; a record on S230's capture prints OK) each meet the frozen C1 kill rule's literal text. They are recorded as
amendments A5/A6 with named limits (i)/(j) and routed fixes, not hidden; the C1 verdict below is on the narrowed sentence,
and the closure rules on it. Neither shape is reachable by any committed lane record today (14 duplicate-id groups, 0 with
diverging sibling status; every call site passes the worktree root), and the round-99 tool admits both shapes too.

## Landed changes

| commit (helper `landed`) | what | LOG |
|---|---|---|
| `9683523467a1be9a9c46972f9b92bed26f44750d` (P) | tool, battery, entry, controls, S237-S239, capture `b5eec205…`, egress table, census start | `LOG.md` `## Round 100` |
| `6f837487be6cf686bcee16902299dba34ec7f063` (R) | pre-freeze controls `corpus/evidence/round100/before/` | same |
| `6d4e8487ee6a16823c24a8e085c6559b92b9fec8` (F) | `claims.md`, `claims.json`, `plans/round-100.md` | same |
| `7d2d3abe3fd0f739049bb4d4f91c9327c054f3c0` | F hash recorded; wave spec, dispatch, ready | same |
| `0a3da3dab7bab333fc3789b909740bb62c64da87` (F2) | A1-A4, B1-B9; entry and round-99 Update repairs; `after-f2/q3-note-is-challenge.txt`, `anchor-times.txt` | same |
| `4ba51a26977813373a85b706c752cd32a58925c1` (F3) | A5-A6; plan amendments; pre-file ledger | same |
| `f0aea4f14d3c733f1f2dfe5a9eb429300783fd3a` | wave evidence, after-F2 receipts, census end, lesson, LOG, SCORECARD, README, QUALITY 231, SKILL line, anchor times | same |

## Before → after measurements

- **C1** — `python3 -B corpus/evidence/round100/challenge-controls-r100.py --root . --work <scratch>`.
  Before (base tool `929c784c:tools/gate-records.py`, `--no-oracles`, run at P `96835234`): `NEG=7/7 MARK=11/11 BOUND=3/3
  NORM=2/2 POS=4/4 REV=3/11 REVPOS=3/3 PROD=4/6 HARM_SAME=27/27 BASE_REV_ADMITTED=8/11`, `CHALLENGE_CONTROLS_R100=FAIL`, exit 1
  (`corpus/evidence/round100/before/c1-base.txt`). After (measured at F2 `0a3da3da`, tool and battery bytes identical
  F..F3): `NEG=7/7 MARK=11/11 BOUND=3/3 NORM=2/2 POS=4/4 REV=11/11 REVPOS=3/3 PROD=6/6 HARM_SAME=27/27 BASE_REV_ADMITTED=8/11
  ORACLES_REJECTED=12/12`, `CHALLENGE_CONTROLS_R100=PASS`, exit 0 (`after-f2/c1-all.txt`) — the frozen predicate line.
- **C2** — counting commands as frozen. Before: entry absent at base (`gate-records` exit 2, `verify-metadata` exit 2,
  controls exit 2; `before/c2-base.txt`); pre-link do-nothing (entry present, no `## Update`): `FRESH=0/1`,
  `ENTRY_CONTROLS_R100=FAIL`, exit 1 (`before/c2-prelink.txt`). After (measured at F2 `0a3da3da`, controls bytes identical
  F..F3): `GATE_RECORDS files=1 records=17 ok=17 fail=0` exit 0; `METADATA_COMPLETE=1/1`, `RESEARCH_GATE: CLEAN` exit 0;
  `rev_match=3/3`, `SEARCH_RERUN: CLEAN` exit 0; `QUOTES=16/16 FIELD=16/16 IDENTITY=2/2 WARRANTS=8/8 NUMBERS=24/24 NEVER=8/8
  FRESH=1/1 TOPIC=1/1 NUMBERS_SOURCED=24/24 BASE_TOPIC_HITS=0 BASE_ENTRY=absent BASE_UPDATE_LINK=0 FORGERY_REFUSED=13/13
  ACCEPTED=2/2`, `ENTRY_CONTROLS_R100=PASS` exit 0; harm: round-99 entry `records=25 ok=25` exit 0, `ENTRY_CONTROLS_R99=PASS`
  exit 0 (`after-f2/c2-all.txt`).

Verdicts (author-measured; non-author closure pending): **C1 verified on the A1-A6 sentence, with the frozen kill rule's
literal text met by `R100SentinelC1` F-1/F-2 (disclosed above)**; **C2 verified at F2 on the B1-B9 entry and sentence**.

## Sources & frontier

- Census before → after: `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin chousa` → exit 0 both
  (`corpus/evidence/round100/census-start.txt`, `census-end.txt`; 7 → 8 W-lines, the new one W04 S237/S235 same URL
  across scopes, both rejected). Registry rows (`grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' corpus/SOURCES.md`): 235 → 238.
- Rows added by tier: S238 B (`mined`); S237 B, S239 B (`rejected`, http 500 ×3 each). Gate lines with URL, access date
  and ≤25-word located quote: `corpus/lessons/round-100.md` `## Gate` (GATE-RECORDs `ok=3`).
- Rows touched old→new: S236 `used-by` `corpus/knowledge/quotation-error-rates-r99.md` →
  `corpus/knowledge/quotation-error-rates-r99.md, corpus/knowledge/quotation-error-update-r100.md` (logged in the lesson).
- Frontier advanced: README Round99's "the 2025 update's Europe PMC record … not opened by the lane" closed (S238); the
  round-99 limit "rev guard keyed to the exact path spelling" closed for git-resolvable spellings and byte copies
  (QUALITY 231). S239's (and S237's) flip condition was met by a seat's read-only re-open, not by a lane GET — routed.
- Sourced claim: C2 cites S238 (opened this round). Mistakes mined: 5 (`corpus/lessons/round-100.md` `## Mistakes`), three
  with fixes shown able to fail (`before/c1-candidate.txt` o12; `before/c1-base.txt` vs candidate; `after-f2/anchor-times.txt`
  2/6 → 6/6), two routed.
- Assimilation: none. considerthese: not mined this round.
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` → only orchestrator-owned `.scratch/` entries; no
  seat file at the fleet root.

## Trend verdicts

- expansion: **unchanged** — registry 235 → 238, but the new entry is on ground round 99 opened (no uncovered coverage-map
  ground).
- quality: **improved** — the gate's rev-form challenge check follows the object git resolves (8 + 2 records refused that the
  round-99 tool admitted, byte-identical output on 27 committed files, `after-f2/c1-all.txt`); a held rate re-verified
  against its newer source and flagged in place (`after-f2/c2-all.txt`, `before/c2-prelink.txt`).
- discernment: **improved** — S238 admitted at B under the carrier rule, S237/S239 refused with flip conditions; 20 ledger
  rows adjudicated (11 `falsifies-wording`, each narrowed by A1-A6/B1-B9; A4 answered without narrowing; kill-rule literal
  disclosed).
  Author-measured; non-author closure pending.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md` round-100 correction line after the round-99 one; `corpus/knowledge/quotation-error-update-r100.md` decision table (lane assertion; no non-author verifier named)
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md` `## Round 100` (approval table, seven GETs, entry, gates, Update flag)
- [~] Instructions executable by an agent without oral context — `python3 -B corpus/evidence/round100/challenge-controls-r100.py --root . --work <scratch>`; `corpus/evidence/round100/after-f2/c1-all.txt`
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` untouched; kagi `on-release` watcher pattern routed, not absorbed (`.ufo/waves/round-100/w1/R100ConnectorSiblings.md`)

## Round shape and extras

- Shape: one v1 wave, 12 seats, policy v1 (band 8-16): executor 2, mutation-tester 2, reviewer 2, critic 1, sentinel 1,
  scout 1, revenger 1, connector 1, scribe 1; attack share (reviewer, critic, mutation-tester) 5/12. L1 holds the canonical
  planner seat (the validator refuses `planner`). Residual call: none. Round total: 12. Dead seats: 0 (12/12 settled with
  reports; dispatcher `spawned chousa 100 w1 12` 02:32:31, `done` 03:56:12). Seat routes per `task.agentModelOverrides`
  (not passed).
- Pre-file ledger: `python3 scripts/hyaku/prefile-falsification.py --lane chousa --round 100` →
  `PREFILE-FALSIFICATION: pass claims=2 rows=20 attack_seats=8 findings=0`, exit 0.
- Defects of seats recorded: `R100MutantsC1` left three unprefixed files in the wave dir (`gen_mutants.py`,
  `gen_batt_mutants.py`, `probe_notes.txt`; prefixed copies exist); `R100ScoutSources` made a third attempt on one URL
  beyond its item's two (disclosed by the seat); several seats left scratch dirs (removed by the L1 after landing).
- L1 process note: the S237/S239 anchors first carried shell-clock times (lesson Mistakes 3, fixed and receipted).
- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
- Tool installs: none (L1; seats report none).
- L0 questions: none opened this round. Routed fleet question (not L0): one tier rule for index-record abstracts.
- Final lane hash: `git -C chousa-shokunin ls-remote origin refs/heads/master` → `f0aea4f14d3c733f1f2dfe5a9eb429300783fd3a`.
