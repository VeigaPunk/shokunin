# kumitate — round 94 report (hyaku run 15, attempt 1)

Lane `kumitate-shokunin`, branch `master`. Base `a6e4da96e828e900150c08d0a801266a53caab63` (r93 closure spot-check
tip); final lane hash `180cc338af3b528add875554f4dafe12aaeafbd6`. L1 `KumitateR94` (holds the §3 planner seat; the validator refuses `planner`).
No earlier attempt of this round (`.ufo/watchdog.log`: no `lane-dead-no-report kumitate round=94`).

## Work performed

Declared claims (1): **C1 — operability** (lowest non-retired axis; integer 9, terminal under `f_O`):
`scripts/round-gate.mjs` resolves SOURCES-declared upstream commit pins (routed defect, round-93 spot-check §5
item 2). Sourced on S271 (gitrevisions `<sha1>`, opened this round) and S033 (GitHub permalinks, re-opened).
Claim type: instrument repair on the lowest axis; no capability row.

- Load + claim choice: MISSION/AXES, prompt §6, SCORECARD `## Round 94 pre-registration`, round-93 lesson and
  spot-check. Sweep of all 77 filed reports with the base gate: 8 rounds read `COMMIT_CITED_UNRESOLVED`
  (12 46 53 57 61 62 63 93); only round 93's tokens are registry pins (`.ufo/waves/round-94/K94Reviewer/`,
  `K94ScribeLesson/red-rounds.md`).
- Freeze `73317eca18c3927fc3c92fe492cd882dc4cda953` (20:40:25-03:00): `plan.md` (frozen rule, predicate, K1–K4),
  counter `probe/probe94-c1.mjs`, control generator `probe/make-controls94.py`, 8 pre-data controls
  (`controls/ctl-*.txt`), open receipts (`open/round-gate-r93-before.txt`, `open/census-before.txt`).
- Wave w1 spec + validated dispatch `791b1fdd1b131ff67452ceea9ea3754fc8bfa548`; `w1.ready` written by the L1;
  WAVE-DONE received; `w1-results.json` 11/11 seats returned output.
- Late adoption of the r93 spot-check `54add172b5613e98e32d8761c2efd549e240baf2` (mistake M94-1).
- Integration M `d21decd2c0cf2f320938efd4570196ec19e683b1`: K94ExecTool's rule (`341726f3…`) + L1 bounded registry
  read (K94Sentinel: FIFO hang, `/dev/zero` abort) + text-mode `info COMMIT_CITED_DECLARED` line (K94CriticB 1c);
  S271/S272; S033/S269 `used-by`; knowledge `corpus/knowledge/round-gate-declared-pins.md`;
  `seat-route-retry-fields.md` cites S272 (M93-2 closed).
- M2 `2cba824a172ec2c2bcda78be5b4d421750504271`: four selftest arms killing K94Mutation survivors m07/m08/m10/m16
  (`close-l1/survivor-remut.txt`); `pin.round-gate` → `11f83a1a…`.
- Close: lesson `corpus/lessons/round-94.md`, QUALITY Q88, LOG r94, SCORECARD move-log row 94 + disposition +
  round-95 pre-registration (`03083e8798d1c0ddc595df1a511211c31afd9da7`); wave evidence
  (`2e7d64de84007c1567c7551c3adcd1f135530243`); proxy stanza re-declared, `PROXY: MATCH`
  (`e0d5600e9af76ae36147e248023e7f4ddcf23183`, `close/battery-final.txt`).

Round shape: ONE v1 wave (`ufo-wave-policy.json`, band 8–16), **11 seats**: executor ×2 (K94ExecTool,
K94ExecHarm), scribe ×2 (K94ScribeSources, K94ScribeLesson), scout (K94Scout), connector (K94Connector), sentinel
(K94Sentinel), reviewer (K94Reviewer), critic ×2 (K94CriticA, K94CriticB), mutation-tester (K94Mutation). Attack
seats 4/11 = 36 %. Dead seats: 0. Residual call: none. Round total: 11.

## Landed changes

| change | LOG.md entry | commit |
|---|---|---|
| freeze: plan, counter, controls, open receipts | LOG r94 section | `73317eca18c3927fc3c92fe492cd882dc4cda953` |
| w1 spec + validated dispatch | LOG r94 section | `791b1fdd1b131ff67452ceea9ea3754fc8bfa548` |
| r93 spot-check adopted into README map (late, M94-1) | LOG r94 section | `54add172b5613e98e32d8761c2efd549e240baf2` |
| M: round-gate declared pins + hardening; S271/S272; knowledge entry | LOG r94 section | `d21decd2c0cf2f320938efd4570196ec19e683b1` |
| lesson, Q88, LOG, SCORECARD, close receipts | LOG r94 one-line | `03083e8798d1c0ddc595df1a511211c31afd9da7` |
| M2: survivor-killing arms, re-pin | LOG r94 addendum | `2cba824a172ec2c2bcda78be5b4d421750504271` |
| wave w1 evidence, M2 receipts | LOG r94 addendum | `2e7d64de84007c1567c7551c3adcd1f135530243` |
| proxy stanza re-declare, final battery | LOG r94 addendum | `e0d5600e9af76ae36147e248023e7f4ddcf23183` |
| Q88 run for round 94 (`close/q88-r94.txt`: `Q88: PASS`) | LOG r94 addendum | `180cc338af3b528add875554f4dafe12aaeafbd6` |

## Before → after measurements

**C1** — counting command (frozen, committed at `73317eca`):

    git -C kumitate-shokunin show <rev>:scripts/round-gate.mjs > T
    node .ufo/waves/round-94/probe/probe94-c1.mjs --tool T --work <scratch> --freeze 73317eca18c3927fc3c92fe492cd882dc4cda953

- Before (base bytes `09d4d792…` = do-nothing control): `C94_C1: UNMET a=0/1 b=7/7 c=77/77 d=1/2 e=1/1`
  (`.ufo/waves/round-94/controls/ctl-nothing.txt`); live `node scripts/round-gate.mjs --round 93` →
  `DRIFT … unresolved=2 [79fa222e 79fa222e8390…]` exit 1 (`open/round-gate-r93-before.txt`).
- Forgery controls: blanket `UNMET b=0/7 c=70/77 d=0/2 e=0/1`; substring/anyline/contains/norejfilter/slashonly
  `UNMET d=1/2`; positive control `HELD`.
- After, measured at M `d21decd2`: `C94_C1: HELD a=1/1 b=7/7 c=77/77 d=2/2 e=1/1 tool_sha256=158062f8…` twice
  (`close/probe1.txt`, `close/probe2.txt`); at M2 `2cba824a` (final bytes): `… HELD … tool_sha256=11f83a1a…` twice
  (`close/probe-m2-1.txt`, `close/probe-m2-2.txt`). Live: `ROUND_GATE  info  COMMIT_CITED_DECLARED declared=2` +
  `ROUND_GATE: CLEAN (round=93 …)`. Selftest 61 → 79.
- Kill rules K1–K4 not fired (`close/kill-and-harm.txt`, `close/battery-final.txt`).
- Caveat (K94CriticA): 7 of 12 wrong-but-plausible gates also reach HELD — five rule clauses are latent in the
  counter's real-report and fixture inputs; routed to round 95. K94Mutation: READY bytes 11/16 killed, 4
  survivors + 1 equivalent; the survivors are killed at M2.

Verdict (lane's reading, pending the non-author closure): **C1 HELD**. Axes: operability 9 unchanged
(terminal), coverage rows all 10, `PROXY: MATCH` — no axis harmed.

## Sources & frontier

Counting command (`sources-census.sh validate --root /home/vgpnk/Projects/shokunin kumitate`):
- round start: `kumitate ok …/corpus/SOURCES.md`, exit 0, 7 × W04 (`open/census-before.txt`).
- round end: `kumitate ok …/corpus/SOURCES.md`, exit 0, 8 × W04 (new: S271 vs S253, same gitrevisions page,
  different entry).

Rows: 208 → 210 (`grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' corpus/SOURCES.md`). Added by tier: A +2 (S271
gitrevisions `<sha1>`; S272 oh-my-pi `retry-fallback-chains.ts` at `79fa222e…`, closes M93-2). Touched old→new:
S033 `used-by` `corpus/lessons/round-38.md` → `+ corpus/knowledge/round-gate-declared-pins.md`; S269 `used-by`
`…seat-route-retry-fields.md` → `+ corpus/knowledge/round-gate-declared-pins.md`. Refused: the drafted duplicate
GitHub-permalinks row (same URL as S033; S033 re-opened instead). Frontier: the citation-resolution surface of the
gate gains a sourced rule (knowledge entry). Sourced claim: C1 rests on S271 (opened this round).
Mistakes mined: M94-1 (spot-check adopted after the freeze; `plan-before-ready` FAIL MAP_DRIFT receipt), M94-2
(r93 filed with its own gate red; Q88 shown able to fail). considerthese: `2026-11-06.md` idea 3 is the M94-1
class (mined as the mistake). Assimilation: none (no `merge/kumitate/` theme touches gate citation pins).

## Trend verdicts

- expansion: **improved** — new knowledge entry `round-gate-declared-pins.md` sourced on S271/S033; SOURCES 208 → 210.
- quality: **improved** — the lane gate no longer reports a registry-declared pin as an error while the seven real
  reds stay red (counter b=7/7, c=77/77); the new read is bounded (FIFO/symlink/oversize arms); selftest 61 → 79,
  all seven rule-shape forgeries and all four reported survivors killed.
- discernment: **unchanged** — the lane's own gate rejected two seat claims (counter pins the rule; declared
  means opened) and refused one source row; the counter's latent clauses (K94CriticA) show the instrument did not
  discriminate as much as the plan implied. Outside judgment is the closure's.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — pointer: `SKILL.md`
  round-gate registry row and checklist item 724 (`node scripts/round-gate.mjs` → `ROUND_GATE: CLEAN`), which now
  passes on round 93 (`close/battery-final.txt`).
- [~] At least one end-to-end domain task executed and logged in LOG.md — LOG.md `## Round 94` (77-report gate sweep,
  wave, integration, counter at M and M2).
- [~] Instructions executable by an agent without oral context — `node scripts/round-gate.mjs --selftest` →
  `ROUND_GATE_SELFTEST: 79/79 pass`.
- [ ] No cross-domain bleed (PROVINCE.md still accurate) — untouched this round.

Stale-lane: respawn-per-round driver; no other mission of this lane is open.
Tool installs: none. L0 questions: none opened.
Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` → `?? .ufo/reports/round-88/tsukuroi.md`,
`?? trail-ids.txt` — neither names kumitate or a round-94 seat; not touched.
