# Kama — round 62 (attempt 2)

## Work performed

Declared claims: **C1 operability** — lane-owned live `/v1/completions` request plane; **C2 calibration** — 12-capability self-assessment bound to live checks (lowest assigned axis, score 7).

- C1 implementation: `tools/kama-completion-live.py` runs a pinned llama.cpp b11755 completion lifecycle, checks the response envelope/accounting, performs a nonce-bound outside contact during a hold, and records teardown evidence; smoke output `REQUEST_OK`, all 16 checks true. The frozen counter's final measured output is below. Files and evidence landed in lane commits `65d7cad0` and `dc5e1010`; round log `kama-shokunin/LOG.md` §Round 62.
- C2 implementation: 12-row `registry/capability-claims-r62.tsv`, round-62 canonical list in `SCORECARD.md`, and frozen executable counter `tools/round62-c2-counter.py`. Final run at `e092f2b6` fails with four mismatches; C2 is **not verified**. The sensitivity calculation is vacuous (`pattern` is replaced before testing for the same pattern), so `sensitive=12/12` is not evidence of sensitivity (`corpus/lessons/round-62.md` §Mistakes).
- Frontier: opened pinned b11755 server README and added S526 for `/v1/completions`; `corpus/knowledge/completion-request-plane.md` distinguishes documented route scope from receipt-observed fields. Lesson Gate and mistakes are in `corpus/lessons/round-62.md`; row/entry/log changes landed through `dc5e1010` and `a25dd0d9`.
- One policy-v2 wave was dispatched via `.ufo/waves/round-62/w1.ready`, 64 seats, 32 attack-role seats. Role mix in the validated dispatch: mutation-tester 18, executor 16, critic 8, scout 6, scribe 6, reviewer 5, connector 4, sentinel 1. **Honest stop:** WAVE-DONE and the results JSON had not arrived by the report cut-off. The wave was dispatched but unsettled; no seat verdicts, dead-seat count, or final falsification finding is claimed, and no seat output is integrated.
- Attempt 1's pre-freeze stop is recorded in `.ufo/watchdog.log` (2026-10-28T08:59:38-03:00); its drafts were re-read and smoke-tested in attempt 2. Red-before defects and repairs are recorded at `kama-shokunin/.ufo/waves/round-62/measured/` and in the lesson. No tools were installed or updated; pacman was not used.
- No open L0 question was filed. No `merge/kama/` material was adopted. `considerthese/2026-10-26.md` proposal 3 was deferred: this round's one-shot C2 count is not the proposed longitudinal tally (lesson Gate gives the flip condition).

## Landed changes

All round changes are tied to the round-62 `LOG.md` entry and its appended corrections (`kama-shokunin/LOG.md:2507-2518`):

- Freeze, predicates, counters and red do-nothing receipts: `6c25a77e`.
- Completion tool, capability registry/canonical list, initial ledgers, S526 knowledge/source, lesson, LOG entry and validated wave spec/dispatch: `65d7cad0`, `dc5e1010`.
- Post-freeze counter repairs, scratch-root repair, final C1 receipt, and b11755 server-hash ledger correction: `dc5e1010`, `a837c8f7`.
- Final clean scanner evidence and SCORECARD measurements: `e092f2b6`; red-before receipts and append-only corrections: `a25dd0d9`.
- Final C2 measurement and honest-stop LOG correction: `77bfaaa5`, `10173704`.
- Final lane HEAD, pushed and verified before report filing: `101737047afeea3a97ceacb98b6d76fa174ed7e4` (`git ls-remote origin refs/heads/master` returned the same hash).

## Before → after measurements

- **C1 operability 8→8, provisional only:** base `a959fd9022b1ac1f3cb4dc2475d9cded8b2b01c3`: `tool_present=0`, exit 1 (`.ufo/waves/round-62/controls/c1-base.txt`). At committed tool/counter tip `dc5e1010cf2fb8168b7ecb0278a1452a8ed99504`, command `python3 tools/round62-c1-counter.py --repo <lane> --tip <tip> --work <scratch>`: `tool_present=1 live_ok=1/1 fake_rejected=2/2 stale_rejected=1/1 tamper_rejected=8/8 log_rejected=1/1 predead_rejected=1/1 sigterm_rejected=1/1 hold_rejected=1/1 outside_rejected=1/1 errors=0 met=True`, exit 0 (`.ufo/waves/round-62/measured/c1-final.out`; receipt `c1-final-receipt.json`). Because the falsification wave did not settle, this green is not admitted as a final claim verdict.
- **C2 calibration 7→7, not verified:** base `a959fd9022b1ac1f3cb4dc2475d9cded8b2b01c3`: `population=12 rows=0 covered=0/12 ... met=False`, exit 1 (`controls/c2-base.txt`). Final command `python3 tools/round62-c2-counter.py --repo <lane> --tip e092f2b6940a77395a9182e22f23cd4d9b06afe0 --work <scratch>`: `population=12 rows=12 covered=12/12 bound=12 eval_lines=12 sensitive=12/12 dead=0 mismatches=4 canonical=62 controls_rejected=8/8 errors=0 met=False`, exit 1 (`measured/c2-final.out`). The frozen predicate is missed; no calibration credit.

## Sources & frontier

- Manual row count `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'`: **265→266**; start/end census receipts `.ufo/waves/round-62/census/{start,end}.out`, both `sources-census.sh validate --root /home/vgpnk/Projects/shokunin kama` exit 0. Warnings: W04 102→103, W01 1→1, errors 0→0. The new W04 is S526's cross-scope duplicate URL; no same-scope duplicate was reported.
- Added tier A: **1** (S526); B: 0; C: 0. Rows touched old→new: none; status/recheck/used-by transitions: none. Frontier row advanced: S526, the previously unheld b11755 `/v1/completions` documentation surface. It is cited by the new knowledge entry and lesson.
- Digest/hexrun checks after the ledger correction at `a837c8f7`: digest `unknown=0 ledger_bad=0`, exit 0; hexrun `unknown=0 ledger_bad=0`, exit 0 (`measured/digest-ledger-final.out`, `hexrun-final.out`). The digest scan's red-before `unknown=1` for the b11755 server SHA and its correction are preserved in `measured/digest-ledger-before.out` and the lane lesson.
- Assimilation: none; staged `merge/kama/` package remains deferred pending source-by-source hand-check. `considerthese` proposal 3 is deferred, not adopted.

## Trend verdicts

- **Expansion — unchanged:** S526 and the new entry cover a previously unheld route, but the wave did not settle and no coverage-map row was advanced; this round does not claim admitted expansion.
- **Quality — unchanged:** no prior knowledge entry was re-verified or superseded; C1 is provisional and C2 fails its frozen predicate.
- **Discernment — unchanged:** no independent non-author admit/reject spot-check is on record; dispatched seats are still part of the lane.

## SHONEN

- [~] SKILL.md contains domain decision tables, error patterns and checklists — author assertion, `SKILL.md` §§ endpoint identity / round-31 chat adapter.
- [~] At least one end-to-end domain task executed and logged — `tools/kama-completion-live.py`, `measured/c1-final-receipt.json`, `LOG.md` §Round 62; independent review remains open.
- [~] Instructions executable without oral context — `corpus/knowledge/completion-request-plane.md` and its run/recheck command; author assertion only.
- [~] No cross-domain bleed — `PROVINCE.md` write boundary and request-surface scope; author assertion only.

Stale-lane: progressing through lane commits `6c25a77e`–`10173704`; W1 remained unsettled at report time. No other open lane mission was established. Dead seats: unknown because the WAVE-DONE/results handoff was absent. Open L0 questions: none.
