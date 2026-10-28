# kama — round 61 report (2026-10-28)

## Work performed

Declared claims (2), both repairs of the round-60 falsifications:

- **C1 — operability** (`tools/round61-c1-counter.py`): fresh-nonce hold-mode v2 live Ollama
  run at the tip, the counter's verifier accepting only after its own live HTTP contact in the
  hold window, classifier re-execution on receipt bytes, manifest/blob re-hash, graded
  `/api/show`, 16/16 controls rejected. Sourced on S519/S525.
- **C2 — calibration** (`tools/round61-c2-counter.py`): the 18-line frozen population covered by
  `registry/ollama-live-claims-r61.tsv` — 17 bound rows over manifest triples with located
  quotes, flip-test sensitivity, amendment ledger — evaluated by a bounded DSL evaluator,
  9/9 control families rejected.

Work items:

- Froze both predicates pre-data: `.ufo/waves/round-61/controls/freeze.txt`; do-nothing base
  receipts `c1-base.txt` (`tool_present=0`, exit 1) and `c2-base.txt` (`header` error, exit 1)
  at base `a107b75f3650981d191d73fde73987415e292e14`.
- `tools/kama-ollama-live.py` v2: `--hold-dir` outside-verifier window, `PR_SET_PDEATHSIG`,
  graded `/api/show`, evidence replay records, `teardown.child_pre_dead` (+136 lines).
- Fresh committed receipt `.ufo/waves/round-61/live/receipt.json` (nonce `r61live01`, port
  47887, `MODEL_OK`, outside verifier contact then release, clean SIGTERM teardown).
- Counters `tools/round61-c{1,2}-counter.py` (new) + `registry/ollama-live-claims-r61.tsv`
  (28 rows) + `corpus/knowledge/ollama-live-amendment-r61.md`.
- Docs: `corpus/knowledge/ollama-live-lifecycle.md` v2 section, `corpus/lessons/round-61.md`
  (Gate + Mistakes), KQ101 in `corpus/QUALITY.md`, SCORECARD round-61 section, LOG.md entry,
  SOURCES row S525 (Ollama OpenAPI yaml, mined, opened 2026-10-28).
- Wave: one v2 wave `w1`, 68 seats validated under `ufo-wave-policy-v2.json`
  (spawn 68, executor 22, mutation-tester 14, reviewer 10, scribe 6, scout 6, connector 5,
  critic 4, sentinel 1 — 31/68 attack-share roles). Spec/dispatch `.ufo/waves/round-61/w1/`.

## Landed changes

- `7848fbeadf476a4e29ff583e53baa5d30c62cf61` — v2 harness, both counters, registry, amendment,
  freeze + do-nothing receipts, committed live receipt, wave spec/dispatch/ready, docs.
- `9df34a7854b8a7bd179831646d08e79fc6bc8e44` — SOURCES S525.
- `85ee660ce576564fc74bbbf7ea0b3f6471850955` — tip measurements `.ufo/waves/round-61/measured/`.
- `d691c7ba2f4bbe7765f936ad66225a3a32605406` — final tip measurements
  (`measured/c1-final.txt`, `c2-final.txt`).

## Before → after measurements

- C1: base `tool_present=0 live_ok=0/1 met=False` (exit 1) → tip
  `live_ok=1/1 fake_rejected=2/2 stale_rejected=1/1 tamper_rejected=6/6 log_rejected=1/1
  predead_rejected=3/3 show_rejected=1/1 sigterm_rejected=1/1 pdeath_ok=1/1 errors=0 met=True`
  at `d691c7ba2f4bbe7765f936ad66225a3a32605406` (identical output at `9df34a78…`).
  Command: `python3 tools/round61-c1-counter.py --repo <lane> --tip <rev> --work <scratch>`;
  receipts `.ufo/waves/round-61/measured/c1-final.txt`, `c1-tip.txt`.
- C2: base `population=18 rows=0 covered=0/18 met=False` (exit 1) → tip
  `population=18 rows=28 covered=18/18 bound=17 eval_rows=17 eval_lines=7 sensitive=17/17
  dead=0 contradicted=0 amended=0/0 receipt_ok=1 controls_rejected=9/9 errors=0() met=True`
  at `d691c7ba2f4bbe7765f936ad66225a3a32605406`.
  Command: `python3 tools/round61-c2-counter.py --repo <lane> --tip <rev>`;
  receipts `.ufo/waves/round-61/measured/c2-final.txt`, `c2-tip.txt`.

## Sources & frontier

`SOURCES.md` rows 264 → 265: +S525 (Ollama OpenAPI spec, docs, tier A, mined, opened
2026-10-28, used-by lifecycle doc + lesson + registry). Census:
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kama`
— before: exit 0 (warnings only); after: exit 0 (same warning class, none new).
Frontier: KQ101 added; `considerthese` ledger mined (2026-10-25/-26 files; proposal
"counter-shortcut trend" adopted by C2's control family); assimilation — quarantine slice
regenerated at `.ufo/waves/round-61/assimilation/quarantine-slice` (7 rows, all
`payload-absent`); merge/kama package recon only, no adoption this round (verdicts in the
lesson Gate).

## Trend verdicts

- expansion: **improved** — new SOURCES row S525, new registry artifact class
  (`ollama-live-claims-r61.tsv`), v2 harness capabilities added to the lifecycle doc.
- quality: **improved** — both frozen counters verified `met=True` at the measured tip with
  full control rejection; KQ101 criterion added.
- discernment: **improved** — the round-60 falsification classes were converted into explicit
  counter controls (unrelated-predicate registry, post-capture death, stubbed replay,
  ungraded show); the lesson records the mistake classes with captured-by and fix.

## Round shape

One v2 wave (policy `ufo-wave-policy-v2.json`, band 64–128): spec `w1-spec.json` holds 68
seats (executor 22, mutation-tester 14, reviewer 10, scribe 6, scout 6, connector 5,
critic 4, sentinel 1; 31/68 attack-share roles), validated clean — `w1-dispatch.json`
records `spawn 68, resume 0, total 68`. `w1.ready` was written at 03:19:16 -03 for the
inline spawn handoff (l1 `KamaR61`); **at report time (~05:30 -03, >2h later, host idle)
the orchestrator dispatcher has not consumed it — no `.dispatched` marker, no seat jobs,
no WAVE-DONE**. The stall is filed as an L0 question (`.ufo/l0-questions.md` kama
round-61 row); the L1 never spawns seats itself per protocol. Round total 0 seats run
(68 validated and queued); dead seats 0.

## Stale-lane

Respawn-per-round driver; no other mission of this lane is open.

## Tooling

No installs this round (pacman paused per guard; nothing needed).

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md` decision table + probe exits; non-author verifier: r57 spot-check.
- [~] At least one end-to-end domain task executed and logged — round 61 v2 live receipt `.ufo/waves/round-61/live/receipt.json` + `LOG.md` round-61 entry (author-dispatched; outside verification pending).
- [~] Instructions executable by an agent without oral context — `tools/kama-ollama-live.py` runs bare per its usage block; receipts in wave dir.
- [~] No cross-domain leakage — no writes outside the lane; PROVINCE boundaries kept (registered consumers untouched).
- [ ] Promotion: pending the non-author round-61 closure.

## Inherited state

Round-60's `.ufo/scopes/kama-r57-w1/swarm-registry.json` remains untouched (not authored this
round). No `lane-dead-no-report kama round=61` line in `.ufo/watchdog.log` — this is attempt 1.

## Open L0 questions

None new this round (the r60 ephemeral-child ratification question remains open).
