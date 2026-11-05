# kaidoku round 94 — report

Lane: `kaidoku-shokunin`, attempt 1 (no earlier attempt; watchdog shows `launch kaidoku round=94 pgid=1693372 driver=hyaku-inline attempt=1`, no `lane-dead-no-report` for round 94). Lane final commit (pushed; `git ls-remote origin refs/heads/main` = final): `e1bf745edaa112ea65efce767553a04282e65c36`. Declaration (freeze) `dd4524916a0332bb65f83525532da1c1b8d709de`; base `8a40ceb6516bb38c19c37bcbff2bb3332f31c832`; landing `8a711726604688af399b2ed8b66c57178e4b6d8e`; bookkeeping `e1bf745edaa112ea65efce767553a04282e65c36`. Measured revisions: R94-C1 at `dd452491` (counter-read bytes unchanged at the landing: `git diff --stat dd452491 8a711726 -- tools/round-93 tools/round-92` empty, receipt `.ufo/waves/round-94/l1/scores/c1-unchanged-bytes-at-8a711726.txt`); R94-C2 at `8a711726`.

## Work performed

Declared claims (2, both frozen before scoring, `plans/round-94-claims.md`, `.ufo/waves/round-94/claims.json`), both on tied-lowest owned axes (all four owned proxies at 10.0; no stagnation waiver — a capability entered round 92):

- **R94-C1 — calibration (measured): VERIFIED.** The round-93 frozen counter's receipt writer crashes on the honest case (M93-e routed); the successor `tools/round-94/stop-boundary-repair-battery-v4.py` imports the frozen v3 verdict code by path (sha pinned `60026511…cbd4e3`) and changes only the receipt writer: bytes become `{"bytes": n, "sha256": hex}`, unknown types raise `TypeError` (no `str()` fallback), and the receipt is written to `<json-out>.tmp` and renamed only after `json.dump` returns. Target: `tools/round-94/c1-receipt-agreement.py` over the four frozen public runs (pos, F1, F2, F3) prints `counts_of_4` valid 4, agree 4, predicted 4, exit 0. Before-receipt (do-nothing: v3 at base): valid 2, agree 2, predicted 2 (`.ufo/waves/round-94/pre/c1-base-v3-agreement.json`).
- **R94-C2 — depth (measured): VERIFIED.** Craft block 33 (`SKILL.md:778-786`, marker `receipt-path-json-safe v1`) is a decision table for the receipt-path failure class, whose criteria cite new QUALITY rows 189 and 190 that state each row's rule, checked by the frozen keyword atoms in `.ufo/waves/round-94/manifests/block33-after.json` (sha `9d72f995…40ae`, frozen before the candidate existed). Before-receipt: block 33 missing at base (`pre/c2-base-block33-after-manifest.json` exit 1; depth v2/v3 `blocks 32 expect 33` exit 1).

Work items (each with an evidence pointer):

- Protocol load: `skill://shokunin`, `skill://swarm`, the fleet `MISSION.md`/`AXES.md`, canonical `PROTOCOL.md`/`CORPUS.md`/`LEARNING.md`, lane `SCORECARD.md`, `PROVINCE.md`, `corpus/lessons/round-{91,92,93}.md` and the round-91/92/93 verifier spot-checks (fresh-start read; the last three closures are all `ok` in `MANIFEST.json` — r93's entry records `admitted=false` for R93-C1 with an honest stop, not a rejection).
- Freeze discipline: pins validated pre-commit (9 sha pins match, `claims.json`), declaration committed before any candidate scoring (`dd452491`), candidate C1 measured only at that revision, C2's candidate landed after the freeze and measured at `8a711726`.
- Tools landed: `tools/round-94/stop-boundary-repair-battery-v4.py` (sha `c41d54d7…6272`), `tools/round-94/c1-receipt-agreement.py` (sha `dc384a44…36c9`), `tools/round-94/c1-landing-extra-checks.py` (advisory landing verification, 27 checks).
- Controls reused unchanged: the round-93 forgeries `.ufo/waves/round-93/controls/{table5-window,carrierread5,identity_noop}.py`; the round-92 repair tool (sha `ce1b1769…70c1`, verified unchanged in every receipt).
- Wave `r94-w1`: one v1 wave, ten seats (`.ufo/waves/round-94/r94-w1-spec.json`, `r94-w1-dispatch.json` — validator exit 0 under `ufo-wave-policy.json` band 8–16, `r94-w1.ready` → `.ready.dispatched`, `r94-w1-results.json`: 10 results, none dead). Findings the wave produced and this round acted on: CriticC1's label-binding/fabrication limits (→ landing extra checks 27/27 + M94-e), CriticC2's vocabulary-residual confirmation, MutationC1's 7/7 mutant kills (incl. the truncation-reproducing M3), SentinelWrite's symlink MED and the plan-prose ambiguity (→ M94-d erratum), ReviewerV4's five-contract PASS with an end-to-end re-execution, ExecC1Repro's independent reproduction, ScoutS319's byte-identical re-fetch with the version-label note, ConnectorOverlap's no-overlap verdict, the two scribes' census-verified drafts.
- Landing: craft block 33, QUALITY 189/190, `corpus/knowledge/2026-11-05-r94-receipt-path-json.md` (cites S319), registry row S319, lesson `corpus/lessons/round-94.md` (Gate/Mistakes/Census/Measured/Wave/Verdict), capability row, SCORECARD round-94 section (with the D-93-C correction line), LOG round-94 entry, WAVE-DONE marker `.ufo/waves/round-94/w1/WAVE-DONE.txt` (D-93-B).
- Frontier step: census before/after run and committed (exit 0 both, below); one mistake set mined (M94-a..f); one sourced claim (R94-C1's and R94-C2's knowledge entry cites S319, opened this round).
- Scratch: `$HYAKU_SCRATCH/kaidoku-r94/` dirs removed by seats before yield; L1 scratch removed after landing; no `/tmp` evidence cited (only the misroot sweep's transient diff).

## Landed changes

| commit | what | LOG entry |
|---|---|---|
| `dd4524916a0332bb65f83525532da1c1b8d709de` | declaration freeze: plan, claims.json (all pins), v4 counter, agreement counter, block-33 manifest, base do-nothing receipts (`pre/`) | round-94 entry, Declaration |
| `8a711726604688af399b2ed8b66c57178e4b6d8e` | C2 candidate: craft block 33 (`SKILL.md:778-786`), QUALITY rows 189/190, knowledge entry, S319 row, `c1-landing-extra-checks.py`, lesson, wave `r94-w1` evidence incl. `r94-w1-results.json` and the WAVE-DONE marker | round-94 entry, Wave |
| `e1bf745edaa112ea65efce767553a04282e65c36` | bookkeeping: SCORECARD round-94 section (+ capability row + D-93-C correction), LOG entry, lesson Measured/Census fill, landing receipts (`c2-*at-8a711726*`, `c1-unchanged-bytes-at-8a711726.txt`), census-after | round-94 entry |

Every LOG entry above is the round-94 entry in `LOG.md`; append-only, no rewrites.

## Before → after measurements

**R94-C1 (calibration).** Counting command: for each of pos/`tools/round-92/upx-stop-boundary-search-repair.py`, F1/`.ufo/waves/round-93/controls/table5-window.py`, F2/`…/carrierread5.py`, F3/`…/identity_noop.py`: `python3 -I -B tools/round-94/stop-boundary-repair-battery-v4.py --root . --repair-cmd <cmd> --work <scratch> --rev <measured> --expect 'repaired 12 of 12; wrong 0; unsafe 0; intact 6 of 6; far-refused 12 of 12; fresh-roundtrip 2 of 2' --json-out <receipt>` (capturing `.stdout`, `.stderr`, `.rc`), then `python3 tools/round-94/c1-receipt-agreement.py --dir .ufo/waves/round-94/l1/scores --prefix c1-v4`.

| arm | before (base `8a40ceb6`, frozen v3 — do-nothing) | after (`dd452491`, v4) |
|---|---|---|
| pos | rc 1, `TypeError: Object of type bytes is not JSON serializable`, receipt truncated 706 B invalid (`pre/c1-base-v3-pos.stderr/.json`) | met True exit 0, valid receipt, `output` = `{"bytes","sha256"}` (`l1/scores/c1-v4-pos.json`) |
| F1 | valid receipt, met False exit 1 | met False exit 1, valid (`l1/scores/c1-v4-F1.json`) |
| F2 | valid receipt, met False exit 1 | met False exit 1, valid (`l1/scores/c1-v4-F2.json`) |
| F3 | rc 1 `TypeError`, truncated 703 B invalid (`pre/c1-base-v3-F3.json`) | met False exit 1, valid (`l1/scores/c1-v4-F3.json`) |
| agreement counter | valid 2, agree 2, predicted 2 — met False exit 1 (`pre/c1-base-v3-agreement.json`) | valid 4, agree 4, predicted 4 — met True exit 0 (`l1/scores/c1-v4-agreement.json`) |

Independent non-author reproduction: ExecC1Repro (own clone at `dd452491`) — all four rcs, stdout lines, agreement 4/4/4 match (`.ufo/waves/round-94/w1/ExecC1Repro/`); ReviewerV4 re-executed from source with the same result and a missing-rc negative run (counter scored 4/0/0 rc 1). Landing extra checks (advisory, CriticC1 option 2): `python3 -I -B tools/round-94/c1-landing-extra-checks.py` → exit 0, 27 checks (labels↔counts recompute, label==frozen label on pos, forgery labels differ, revision fields full, verdict/counter/import/repair sha pins bind, provenance atoms true, fresh near cells repaired+roundtrip) — `.ufo/waves/round-94/l1/scores/c1-v4-landing-extra-checks.json`.

**R94-C2 (depth).** Counting commands at `8a711726`: `python3 -I -B tools/round-93/craft-citation-semantic.py --root . --manifest .ufo/waves/round-94/manifests/block33-after.json --block 33 --rev 8a711726…` (→ `.ufo/waves/round-94/l1/scores/c2-after-block33-at-8a711726.json`, exit 0 `ok`); `python3 -I -B tools/round-89/depth-blocks-v2.py --root . --rev 8a711726… --expect-blocks 33` (→ `c2-depth-v2-at-8a711726.txt`, exit 0 `blocks 33 resolved 33`); `python3 -I -B tools/round-91/depth-blocks-v3.py --root . --rev 8a711726… --expect-blocks 33 --shape-from 33` (→ `c2-depth-v3-at-8a711726.txt`, exit 0 `required-shaped 1/1`). Before at base: all three exit 1 (`pre/c2-base-*`). Checker selftest regression: 10 cases, 0 failures at `dd452491` (`c2-selftest-at-dd452491.txt`). The claim's headline is scoped to the frozen keyword atoms (vocabulary check) — CriticC2's keyword-stuffing fixture passes all three counters exactly as the named limit declares, and its prose/dropped-row/miscite fixtures are held (`w1/CriticC2/receipts/`).

## Sources & frontier

- Rows: S319 appended (tier A docs, `mined`, opened 2026-11-05, recheck `on-release`, used-by `corpus/knowledge/2026-11-05-r94-receipt-path-json.md` + `corpus/lessons/round-94.md`); no existing row edited. Counting command: `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kaidoku`.
- Census before (round start): exit 0, 223 rows, 31 `W04` (`.ufo/waves/round-94/census-before.txt`). Census after (round end, final tree): exit 0, 224 rows, 32 `W04` (`.ufo/waves/round-94/census-after.txt`). The one new `W04` is S319's URL shared with S050 across a different scope (expected; E04 correctly does not fire). E01–E12 for S319: none (ScribeKnowledge's scratch fleet-fixture run B exit 0).
- Rows added by tier: A 1 (S319). Rows touched old→new: none (no in-place edits). Frontier rows advanced: the receipt-path failure class moves from a routed round-93 defect to a named craft class (block 33) with a measured successor counter; `corpus/README.md` `## Frontier` not edited (the class sits on held ground).
- Gate (CORPUS.md rule 1): URL, access date (2026-11-05), HTTP 200, 116296 bytes, sha256 `8021264a…794c0` and the located quote for S319 are in `corpus/lessons/round-94.md` `## Gate`; ScoutS319 independently re-fetched twice (byte-identical) and re-located the quote with its anchors.
- Admit/reject: S319 admitted; the docs' example-`default()` TypeError sentence and the `JSONEncoder.default` subclass sentence rejected (example/encoder-subclass, not the `json.dump` parameter contract) — recorded in the lesson Gate for the closure's spot-check.
- Sourced claim: R94-C1's and R94-C2's knowledge entry cites S319 (opened this round); S319's census status is `mined`.
- Mistakes mined: `corpus/lessons/round-94.md` `## Mistakes` M94-a (the honest-case receipt crash, carried from M93-e, now fixed and measured), M94-b (truncated receipt as evidence, D-93-D), M94-c (selftest never exercised the public path), M94-d (ambiguous kill-rule prose in the frozen plan — erratum), M94-e (the agreement counter's label-binding/fabrication limits, found by CriticC1), M94-f (short `--rev` in the base receipts). The sweep was not empty.
- Assimilation: `Assimilation: none` (`merge/kaidoku/` absent; the lane has no `considerthese/` directory).

## Trend verdicts

- **expansion: unchanged.** One knowledge entry admitted, on ground the coverage map already holds (the stop-boundary battery family, Core); no new coverage-map ground; `corpus/README.md` untouched; one capability row entered (the v4 receipt battery) — the repertoire grew, the map did not.
- **quality: improved.** M93-e is fixed and measured by the frozen counting command (receipt↔stdout↔prediction agreement 4/4/4 with an independent reproduction); D-93-D is answered by the atomic writer (MutationC1's M3 reproduced the truncated leftover in the mutant only); craft block 33 + QUALITY 189/190 record the class with cited criteria; no admitted entry failed a re-check (S319 census clean; S271/S317/S318 untouched).
- **discernment: improved.** The wave's attacks became recorded limits and checks rather than hidden findings: the agreement counter's label-binding/fabrication limits (CriticC1) are M94-e plus a 27-check landing verification; the vocabulary-only C2 residual is confirmed and kept as the claim's declared scope; the plan-prose ambiguity is an erratum (M94-d); MutationC1 killed 7/7 mutants with the pristine bytes pin-verified after every run. The non-author closure spot-check is pending (no outside verdict yet); the exploratory-claim gate was not used (no exploratory claim).

## SHONEN

`[~]` lines are author-asserted with an evidence pointer; no `[x]` (no non-author verifier yet).

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md:778-786` (block 33, decision table citing QUALITY 189/190 and the receipt evidence); blocks 1–32 intact (depth v2/v3 33/33 at `8a711726`)
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md` round-94 entry; the frozen battery ran end-to-end at `dd452491` (four public runs, receipts `.ufo/waves/round-94/l1/scores/`)
- [~] Instructions executable by an agent without oral context — the counting commands in `## Before → after measurements`, `plans/round-94-claims.md`, and `corpus/lessons/round-94.md` `## Measured`; `tools/round-94/stop-boundary-repair-battery-v4.py --selftest` (3 cases rc 0)
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `.ufo/waves/round-94/w1/ConnectorOverlap.md` (no sibling claims the receipt-path or stop-boundary class; one method-only `default=str` hit in kama); PROVINCE.md not edited

## Round shape, seats, and dead seats

- Shape: one v1 wave `r94-w1`, 10 seats (band 8–16). Roles: executor 1, scribe 2, scout 1, connector 1, reviewer 1, critic 2, mutation-tester 1, sentinel 1. Planner seat held by the L1 (validator refuses `planner`). Attack share 5 of 10 = 50% (reviewer, critic ×2, mutation-tester, sentinel); one connector; L2 floor met (10 ≥ 8). No residual call.
- Dead seats: none (`r94-w1-results.json`, 10 results, each with final output). Seat-captured routes are recorded in the results file.
- WAVE-DONE received for `r94-w1` before this report was filed; committed pointer `.ufo/waves/round-94/w1/WAVE-DONE.txt` (D-93-B answered).

## Stale-lane, tools, misroot, inherited state

- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
- Tools: no tool installed or upgraded in this round (python3 3.14.8, upx 5.2.0, git, curl, jq, strace — already present; SentinelWrite used strace read-only). No pacman transaction, no sysctl or namespace change. Host need: none.
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` compared to the committed baseline `.ufo/waves/round-94/misroot-baseline.txt`: no file written by this round's seats at the fleet root. Baseline entries (not mine, untouched): `M .scratch/run15-state.json` (orchestrator-owned), `?? .ufo/closure-kaidoku-r92.json` (round-92 closure artifact), `?? cases_A.json` (another lane's eval fixture, since removed by its owner).
- Inherited state: the lane tree was clean at round start (`jj-lane.sh state` ahead=0 behind=0, no untracked); the round-93 truncated receipts named by D-93-D are kept as evidence, not rewritten.

## Open L0 question

`kaidoku | round-93` in `.ufo/l0-questions.md` remains open (operator ruling wanted on the R93-C1 stdout-form kill and successor approval). This round routed around it exactly as the lane recommended there: the successor counter is a new declaration with JSON-safe output fields and a selftest, the stdout-form position stands (a stdout transcript does not admit a receipt-bound claim), and the successor is measured and admitted on its own frozen predicate. No new L0 question this round.
