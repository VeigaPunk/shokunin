# Kama — round 63 (attempt 1)

## Work performed

Declared claims: **C1 operability** — strict, outside-bound live `/v1/completions` request plane (`tools/kama-completion-live.py` v2 + `tools/round63-c1-counter.py`); **C2 calibration** (lowest assigned axis, 7) — 12 frozen capabilities bound to live runs with a sensitivity test that can fail and the lane self-description reconciled (`registry/capability-claims-r63.tsv` + `tools/round63-c2-counter.py`). Both re-claim the round-62 claims that the round-62 closure rated unprovable. No exploratory claim.

- Freeze `.ufo/waves/round-63/controls/freeze.txt` at lane commit `675cac02c966b7db5429d335e6b91158c8dd59cf` (base `7ee8cbdf160f8c945954e4737e7a2f797e3b2987`). **Amendment 1** (`03a6a1d850902a66a13dfad33f89cf3a8b759a09`, committed before the wave was dispatched and before any seat scored; disclosed in the freeze file): the C1 control-credit rule gained a collateral cap (5 failing checks, 30 for the envelope break) and a 3-plant evaluator self-test, after my own mutant (a helper that stops re-sealing a capture hash) left 44/44 standing (`controls/c1-mutants-prewave.txt`). Seat KR05 notes the predicate sentence itself changed, not only the instrument.
- Red-before receipts: `controls/c1-base.txt` (`live_ok=0/1 met=False`), `c1-relabel.txt` (schema-relabelled v1 tool rejected), `c2-base.txt` (registry absent, `selfdesc_mismatches=8`), `c2-shortcut.txt` (registry + canonical list without the ledger repair: `mismatches=2`, controls credit withheld, "would be 12/12").
- C1 build: tool v2 adds headers, body bytes and truncation flag, request bytes with sha256, a `/tokenize` capture, nine checks, and the proxy-free opener. Seat EX06 measured the opener fix: with proxy variables set, the round-62 tool leaked both POSTs to the proxy (verdict FAIL) and the round-63 tool made 0 proxy connections (`REQUEST_OK`).
- C2 build: new counter with strip-until-absent sensitivity plus 4 planted defective verdict functions, targeted control families credited only on a met baseline, allowlisted environment, declared `host-busy` outcome for the context-capacity row, and the reconciler conjunct. Pre-freeze repairs: ollama nonce `ctrun`→`ctrun0001`, hexrun ledger row for the fleet commit the round-62 closure cites, SCORECARD head/PROVINCE re-derived (`tools/round42-selfdesc-reconcile.py` 8→0).
- One policy-v2 wave `w1` via `.ufo/waves/round-63/w1.ready` (dispatch `w1/w1-dispatch.json`): 64 seats, 37 attack-role. Role mix: mutation-tester 23, executor 10, critic 8, scribe 7, reviewer 6, scout 6, connector 3, sentinel 1. 61 completed; **3 scouts dead** (SC01ServerTask, SC02TokenizeDoc, SC03Considerthese) on provider error `Cursor USAGE_PRICING_REQUIRED: Weekly usage limit reached` (reported by the orchestrator), no report written; I did their three items myself and did not replace them. Planner seat = L1 (the validator rejects `planner`). No residual call. Round total 64.
- **Falsification result: C1 is falsified.** Seat MT15C1FakeConsistent: two forged tool clones (a canned answerer behind the real child's inherited listener fd; no llama-server at all) pass the frozen counter with `met=True 44/44` (`.ufo/waves/round-63/w1/MT15C1FakeConsistent.md`); KR03 S6/S7 (replayed captures, fake child) and MT14 agree. C2 survivors: tip-tree tools and the reconciler certify themselves (KR03 S1/S2, KR02 X/Y/F), no control exercises the reconciler conjunct or the quote floor (MT20/MT21), RV04 D1 (idle outcome of the context-capacity row scores a mismatch). Full lists: `corpus/lessons/round-63.md` §Wave results.
- Frontier: opened pinned llama.cpp `server-task.cpp` and `server-common.cpp` (raw bytes retained under `.ufo/waves/round-63/source/`), added S527 and S528; knowledge entry `corpus/knowledge/completion-request-plane.md` gained a per-field v2 grading section marking source-backed versus observed fields. Hand-checked the kama quarantine slice (7 rows: 4 staged quotes absent, 3 present); nothing adopted.
- Honest accounting of the three dead-scout items: done by L1, evidence in lesson Gate. Tools installed/updated: none; pacman not used. Open L0 questions: none filed.

## Landed changes

LOG entry `LOG.md` §Round 63 maps to these lane commits (pushed, `ls-remote origin refs/heads/master` = final hash below):
- `675cac02c966b7db5429d335e6b91158c8dd59cf` — freeze, v2 tool, counters, registry, ledger row, controls, SCORECARD round-63 section.
- `03a6a1d850902a66a13dfad33f89cf3a8b759a09` — freeze amendment 1 and re-run controls.
- `f7f1b37883b55899a37a20c463954e1b985d4d8a` — wave evidence (64 seats), S527/S528, knowledge, lesson, QUALITY KQ102–KQ106, SCORECARD head re-derived, PROVINCE note. **Measured tip.**
- `7a0e49f80efc989f288ef7b46d4914c5d415846a` — measurement receipts, census end, SCORECARD measured results and corrections, LOG entry. **Final lane HEAD** (pushed; `git ls-remote origin refs/heads/master` returned this hash).
Inherited state: a round-62 seat file misrouted to `kama-shokunin/.ufo/waves/round-62/w1/A04C1SchemaFuzz.md` was copied byte-exact to `.ufo/waves/round-63/inherited/` and the nested directory removed (SCORECARD correction appended: the freeze-time sentence "no untracked paths" was false). `non-authored` files (`corpus/lessons/round-62-verifier-spotcheck.md`, `.ufo/scopes/…`) were not edited.

## Before → after measurements

- **C1 operability 8→8 (falsified, not admitted):** base `tool_present=1 live_ok=0/1 controls_targeted=0/0 eval_selftest=0/3 errors=1 met=False` → measured tip `f7f1b378…`: `python3 tools/round63-c1-counter.py --repo <lane> --tip f7f1b37883b55899a37a20c463954e1b985d4d8a --work <scratch>` → `tool_present=1 live_ok=1/1 controls_targeted=44/44 eval_selftest=3/3 errors=0 met=True` (exit 0; `.ufo/waves/round-63/measured/c1-final.out`). Falsified by MT15 as above.
- **C2 calibration 7→7 (measured met, findings open):** base `population=12 rows=0 covered=0/12 … canonical=62 selfdesc_mismatches=8 controls_rejected=0/12 errors=2 met=False` → `python3 tools/round63-c2-counter.py --repo <lane> --tip f7f1b37883b55899a37a20c463954e1b985d4d8a --work <scratch>` → `population=12 rows=12 covered=12/12 bound=12 eval_lines=12 sensitive=12/12 dead=0 host_busy=1 mismatches=0 canonical=63 selfdesc_mismatches=0 sens_selftest=4/4 controls_rejected=12/12 errors=0 met=True` (exit 0; `measured/c2-final.out`). `tools/round42-selfdesc-reconcile.py` `mismatches=0 met=True` at the measured tip and at the final tip (base 8). `host_busy=1`: the K1 cell was not measured (foreign llama-servers running).
- Supporting: `digest-ledger` `unknown=0`, `hexrun-census` `unknown=0` (base `unknown=1`, `measured/hexrun-base.out`); stability: EX01 7 identical C1 runs, EX02 3 identical C2 runs; EX04 8 existing gates green.

## Sources & frontier

- Census start/end: `.ufo/waves/round-63/census/{start,end}.out`, both `sources-census.sh validate --root /home/vgpnk/Projects/shokunin kama` exit 0. `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`: **266→268**. Added tier A: 2 (S527, S528), B 0, C 0. Rows touched old→new: none; status/recheck/used-by changes: none. The census emits cross-scope duplicate-URL W04 warnings for S527/S528 (same repository host as S526/S036 rows, different files); no E-codes.
- Frontier rows advanced: S527 and S528 (the response-field set of non-streaming `/v1/completions` and the `timings` field list, previously observation-only); cited by the knowledge entry and lesson. Sourced claim: C1 (its new checks cite S527/S528).
- Mistakes mined into `corpus/lessons/round-63.md` §Mistakes (8 rows) with QUALITY KQ102–KQ106.
- Assimilation: none (quarantine slice hand-checked, 4 staged rows absent; no entry adopted). considerthese: proposal 3 re-judged — `tools/shortcut-tally.py` has existed since round 48 and reports `no-disclosure` for rounds 56–62; routed to Planned (round 64).

## Trend verdicts

- **Expansion — unchanged:** S527/S528 move two response surfaces from observation-only to source-backed inside a held entry, but C1 is falsified and no coverage-map row is advanced.
- **Quality — improved:** the round-62 vacuities (controls credited under a failing baseline, vacuous sensitivity) are repaired and shown able to fail (`controls/c2-shortcut.txt`, MT17 `sens_selftest=0/4`), the self-description now reconciles (8→0), and the proxy leak of the v2 tool's predecessor is closed (EX06); the wave's open survivors are recorded, not closed.
- **Discernment — unchanged:** the lane reversed its own round-62 considerthese verdict on a corrected premise, but no non-author spot-check of round 63 is on record.

## Stale-lane

Stale-lane: progressing; one lane mission, round 63 only. No other open mission. Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows no kama file at the fleet root (untracked entries belong to other lanes / `.scratch`).

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — author assertion only (`SKILL.md` unchanged this round); no non-author verifier.
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md` §Round 63, live runs `.ufo/waves/round-63/measured/c1-final.out`; falsified by MT15, no non-author verifier.
- [~] Instructions executable by an agent without oral context — `corpus/knowledge/completion-request-plane.md` §Round-63 and the counter commands in SCORECARD §Round-63 measured results; independent execution review open.
- [~] No cross-domain bleed — `PROVINCE.md` §Round-63 note (write boundary unchanged); no non-author verifier.
