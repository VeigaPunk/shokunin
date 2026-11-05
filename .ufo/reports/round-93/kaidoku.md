# kaidoku round 93 — report

Lane: `kaidoku-shokunin`, attempt 1 (no earlier attempt; watchdog shows `launch kaidoku round=93 attempt=1`, no `lane-dead-no-report` for round 93). Lane final commit (pushed, `git ls-remote origin refs/heads/main` = final): `a894611e5a43f441983de06bc58719f4453095ef`. Declaration `92a240521bd1bf2213b75d18d9b176a8dafdc67c`; base `0a2a23da5eb50410a8a0df90c031d9f4fdadb024`; measured revisions `ca5aa6a2` (R93-C1) and `0dbdf69375475223b22cbbde63fe4b488ae6ecd1` (R93-C2).

## Work performed

Declared claims (2, both frozen before scoring, `plans/round-93-claims.md`, `.ufo/waves/round-93/claims.json`):

- **R93-C1 — calibration (measured overreach): verdict NOT VERIFIED.** The round-92 repair label admits two five-carrier forgeries that derive nothing (pinned-image table F1; carrier-read F2). Claim: a fresh-pack held-out arm (nonce-marked `/usr/bin/env`, packed fresh at measure time) rejects both while admitting the honest repair. Pre-freeze do-nothing receipts: `.ufo/waves/round-93/pre/r93-do-nothing-r92label-F1.json` and `…-F2.json` (both met True, exit 0 at base). Kill rule fired at the measured revision: the frozen positive command with `--json-out` exits 1 with `TypeError`, so no receipt is written (`.ufo/waves/round-93/l1/scores/c1-pos-json-stderr-at-ca5aa6a2.txt`).
- **R93-C2 — depth (measured): verdict VERIFIED on the frozen predicate, headline narrowed.** Craft block 31 row 3 cites QUALITY 169 for the intact-input rule; row 169 does not state it (D-91-3, `corpus/lessons/round-91-verifier-spotcheck.md:169`). Claim: block 32 and a semantic check on the citation's keywords. Before-receipt at base: exit 1 with the named atom (`.ufo/waves/round-93/pre/r93-c2-block31-before.json`).

Work items (each with an evidence pointer):

- Protocol load: `skill://shokunin`, `skill://swarm`, `skill://godspeed`, the fleet `MISSION.md`/`AXES.md`, the canonical `PROTOCOL.md`, `CORPUS.md`, `LEARNING.md`, the lane `SCORECARD.md`, `PROVINCE.md`, `corpus/lessons/round-92.md` and `round-92-verifier-spotcheck.md` (the D-91-3 routing and the M92-c/M92-d limits).
- Census before (frontier step §2b): `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kaidoku` exit 0, 222 rows, 30 `W04` (`.ufo/waves/round-93/census-before.txt`).
- Tools: `tools/round-93/stop-boundary-repair-battery-v3.py` (C1 counter; imports the round-92 battery and v2 by path; sha256 `60026511…d4e3`), `tools/round-93/craft-citation-semantic.py` (C2 counter; sha256 `34cf6579…5340`; `--selftest` 10 cases, 0 failures, `.ufo/waves/round-93/l1/scores/c2-selftest-at-ca5aa6a2.txt`).
- Controls: `.ufo/waves/round-93/controls/{table5-window.py (F1), carrierread5.py (F2), identity_noop.py (F3)}`; the F2 wrapper was rewritten before freeze to patch the verdict function the round-92 tool actually calls (M93-d).
- Wave `r93-w1`: one v1 wave, 11 seats (`.ufo/waves/round-93/w1-spec.json`, `r93-w1-dispatch.json`, `r93-w1.ready` → `.ready.dispatched`, `r93-w1-results.json`). Seat reports under `.ufo/waves/round-93/w1/<Seat>.md`. Findings the wave produced and this round acted on: the S318 teaches-cell marker (ScribeQuality F2), the Row 188 pointer (ScribeQuality F3), the block 32 `no-citation` depth failure (ExecC2, CriticClaims C2-6), the `--json-out` crash (ReviewerOracle F5-a, MutCounter, SentinelTools HIGH-1, ScribeKnowledge HIGH-1), the S318 caller count (ten, not eight: ScribeKnowledge finding 3), and the vocabulary-only C2 check (SentinelTools MED-1/MED-2, CriticClaims C2-4).
- Landing: craft block 32 (`SKILL.md:767-777`), QUALITY Row 188 with its semantic-atom and pointer continuations (`corpus/QUALITY.md:319-321`), registry rows S318 (appended) and `used-by` extensions on S271 and S317 (`corpus/SOURCES.md:188,233,234`), knowledge entries `corpus/knowledge/2026-11-05-r93-fresh-pack-oracle.md` and `…-r93-citation-semantics.md`, lesson `corpus/lessons/round-93.md`, SCORECARD round-93 section, LOG round-93 entry.
- Measurements at `ca5aa6a2` and at HEAD (receipts under `.ufo/waves/round-93/l1/scores/`; full table in `## Before → after measurements`).
- Premise and falsification by seats: ExecPremise (probes 1–4, exploratory), ExecCounterAudit (8 of 8 pins match; pre-freeze receipts reproduce), ReviewerOracle, MutCounter (mutants M1–M7 and checker mutants), CriticClaims, SentinelTools (HIGH-1, HIGH-2, MED-1..4, LOW-1..8), ConnectorOverlap (no sibling claims the surfaces; `.ufo/waves/round-93/w1/ConnectorOverlap.md`).
- Scratch: `$HYAKU_SCRATCH/kaidoku-r93` removed after landing; no `/tmp` evidence cited.

## Landed changes

| commit | what | LOG entry |
|---|---|---|
| `92a240521bd1bf2213b75d18d9b176a8dafdc67c` | declaration freeze: claims, claims.json, both counters (v3, checker), controls, manifests, pre-freeze do-nothing receipts | round-93 entry, `## Motive` / `## Declaration` |
| `2d4c89f9b82ca4e2898476c97a76dfa1a082d21e` | craft block 32 (`SKILL.md:767-777`); QUALITY Row 188; S318, S271/S317 `used-by`; two knowledge entries; lesson with Mistakes; wave evidence | round-93 entry, `## Work commits` |
| `ca5aa6a2ca65ff14f11707c3a376a96879458248` | Row 188 semantic-atom statement (the C2 after-manifest pins the phrase; the first landing failed it, see Before→after) | round-93 entry |
| `0dbdf69375475223b22cbbde63fe4b488ae6ecd1` | bookkeeping: SCORECARD round-93 section, LOG entry, lesson Gate/Measured/seat results/verdict, census-after, S318 teaches-cell fix, Row 188 pointer correction, knowledge pointer corrections | round-93 entry, `## Corrections` |
| `f8422396ccc72a5c954a475fa4bed7d89d4ca496` | measured-revision correction (C2 at HEAD; C1 unchanged-bytes argument) | SCORECARD and lesson correction paragraphs |
| `a894611e5a43f441983de06bc58719f4453095ef` | wave r93-w1 settled evidence (`r93-w1-results.json`, seat reports for ReviewerOracle and ScribeQuality) | — |

Not landed: R93-C1's successor counter. The pinned counter may not change after seats scored (see M93-e); round 94 gets a declared successor.

## Before → after measurements

**R93-C1 (calibration).** Counting command (stdout form, no `--json-out`):
`python3 -I -B tools/round-93/stop-boundary-repair-battery-v3.py --root <clone@ca5aa6a2> --repair-cmd <F|repair> --work <scratch> --rev ca5aa6a2ce0d5e8a7c5b5b0f2d9f0eb9a0e4a0f2 --expect 'repaired 12 of 12; wrong 0; unsafe 0; intact 6 of 6; far-refused 12 of 12; fresh-roundtrip 2 of 2'`

| arm | before (base `0a2a23da`, round-92 label) | after (`ca5aa6a2`, v3, stdout form) | after, `--json-out` form |
|---|---|---|---|
| F1 pinned-image table | met True, exit 0 (admitted) | `repaired 10 of 12; …; intact 5 of 6; far-refused 12 of 12; fresh-roundtrip 0 of 2` met False exit 1 | exit 1, receipt written |
| F2 carrier-read | met True, exit 0 (admitted) | `repaired 10 of 12; …; intact 6 of 6; far-refused 12 of 12; fresh-roundtrip 0 of 2` met False exit 1 | exit 1, receipt written |
| F3 identity no-op (negative) | met False, exit 1 | `repaired 0 of 12; …; far-refused 0 of 12; fresh-roundtrip 0 of 2` met False exit 1 | exit 1, `TypeError`, no receipt |
| positive (round-92 repair) | met True, exit 0 | `repaired 12 of 12; wrong 0; unsafe 0; intact 6 of 6; far-refused 12 of 12; fresh-roundtrip 2 of 2` met True exit 0 | exit 1, `TypeError`, no receipt |

Receipts: `.ufo/waves/round-93/l1/scores/c1-{pos,F1,F2,F3}-stdout-at-ca5aa6a2.txt`, `…-json-stdout-…`, `…-stderr-…`, `…-json-at-ca5aa6a2.json` (F1, F2). Verdict: the kill rule "any receipt missing" fires (positive control); the predicate outcomes match the claim's prediction. Not verified.

**R93-C2 (depth).** Counting command: `python3 -I -B tools/round-93/craft-citation-semantic.py --root <clone> --manifest .ufo/waves/round-93/manifests/block32-after.json --block 32 --rev <rev>` (and `block31-before.json --block 31`); `python3 -I -B tools/round-89/depth-blocks-v2.py --root <clone> --rev <rev> --expect-blocks 32`; `python3 -I -B tools/round-91/depth-blocks-v3.py --root <clone> --rev <rev> --expect-blocks 32 --shape-from 32`.

| check | before (base `0a2a23da`) | after `ca5aa6a2` | after `0dbdf693` (HEAD) |
|---|---|---|---|
| after-manifest, block 32 | (block 32 absent) | exit 0 `ok` | exit 0 `ok` |
| before-manifest, block 31 (must stay red) | exit 1, `QUALITY 169 lacks [...]` | exit 1, same atom | exit 1, same atom |
| depth v2 | `blocks 31 resolved 31` | `blocks 32 resolved 32` exit 0 | exit 0 |
| depth v3 | `blocks 31 resolved 31` | `required-shaped 1/1` exit 0 | exit 0 |
| checker selftest | — | `SELFTEST cases=10 failures=0` exit 0 | — |

A first landing (`2d4c89f9`) failed the after-manifest with `QUALITY 188 lacks ['semantic atom']`: the frozen keyword phrase was missing from my Row 188 text (the scribe's draft carried it, my landing edit dropped it). The correction commit `ca5aa6a2` restored it; the failure and the fix are both in the history.

## Sources & frontier

- Rows: S318 appended (`tier A`, `mined`, opened 2026-11-05, supersedes S313 in the teaches cell); S271 and S317 `used-by` extended; S313 not edited. Census before: exit 0, 222 rows, 30 `W04` (`.ufo/waves/round-93/census-before.txt`). Census after (round-end, `.ufo/waves/round-93/census-after.txt`; command `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kaidoku`): exit 0, 223 rows, 31 `W04`. The one new W04 is S318's URL, shared with S316 under a different scope (expected). E01/E03/E04: none.
- Rows added by tier: A 1 (S318). Rows touched old→new: S271 `used-by` `corpus/lessons/round-69.md` → `…, corpus/knowledge/2026-11-05-r93-fresh-pack-oracle.md`; S317 `used-by` `…r92-stop-boundary-repair.md` → `…, …r93-citation-semantics.md, …r93-fresh-pack-oracle.md`. Status and recheck unchanged on both.
- Gate (CORPUS.md rule 1): URL, access date (2026-11-05), HTTP 200, bytes, sha256 and located quotes for S318, S317 and S271 are in `corpus/lessons/round-93.md` `## Gate`.
- Frontier rows advanced: the craft-citation rule (D-91-3) moves from routed to landed on the frozen predicate; the caller map of `unpackExtent` moves from the S313 wording to the S318 call-site form. `corpus/README.md` `## Frontier` not edited.
- Sourced claim: R93-C1's knowledge entry cites S318 (opened this round) and S317, S271 (re-opened this round).
- Mistakes mined: `corpus/lessons/round-93.md` `## Mistakes`: M93-a (D-91-3, captured by none), M93-b (S313 caller claim from memory), M93-c and M93-d (caught before freeze), M93-e (the frozen v3 `--json-out` crash; captured by none; not fixed: pinned counter, seats scored; routed to round 94), M93-f (a draft's depth clause and pointer), M93-g (caller count from memory). The sweep was not empty.
- Assimilation: `Assimilation: none` (`merge/kaidoku/` absent; no `considerthese/` directory).

## Trend verdicts

- **expansion: unchanged.** Two knowledge entries admitted, on the stop-boundary class already held in Core (`corpus/knowledge/2026-11-05-r92-stop-boundary-repair.md`) and on the craft-citation rule; no new coverage-map ground.
- **quality: improved.** D-91-3 superseded by craft block 32 with a frozen keyword check (`corpus/QUALITY.md` Row 188); S313's over-broad caller wording superseded by S318 (ten call sites grounded by `grep -n unpackExtent` on the fetched bytes); the seats' attack findings written up as limits, not hidden.
- **discernment: improved.** Disagreements became criteria and lessons: the vocabulary-only C2 check is stated in Row 188 and the lesson limits; the C1 headline failure is recorded as not verified rather than narrowed to the stdout form. The non-author spot-check is pending (no outside verdict yet).

## SHONEN

`[~]` lines are author-asserted with an evidence pointer; no `[x]` (no non-author verifier yet).

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md:767-777` (block 32, decision table with QUALITY citations)
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md` round-93 entry; the counters run at `ca5aa6a2` and HEAD (`.ufo/waves/round-93/l1/scores/`)
- [~] Instructions executable by an agent without oral context — the counting commands in `## Before → after measurements` and `corpus/lessons/round-93.md` `## Measured`; `tools/round-93/craft-citation-semantic.py --selftest`
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `.ufo/waves/round-93/w1/ConnectorOverlap.md` (no sibling claims the stop-boundary or craft-citation surfaces); PROVINCE.md not edited

## Round shape, seats, and dead seats

- Shape: one v1 wave `r93-w1`, 11 seats (band 8–16). Roles: executor 3, scout 1, scribe 2, reviewer 1, critic 1, mutation-tester 1, sentinel 1, connector 1. Planner seat held by the L1 (validator refuses `planner`). Attack share 4 of 11 = 36% (reviewer, critic, mutation-tester, sentinel); one connector; L2 floor met (11 ≥ 8). No residual call.
- Dead seats: none (`r93-w1-results.json`, 11 of 11 returned output). Seat-captured routes are recorded in the results file.
- WAVE-DONE received for `r93-w1` before this report was filed.

## Stale-lane, tools, misroot, inherited state

- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
- Tools: no tool installed or upgraded in this round (python3, upx 5.2.0, jq, git, curl, sha256sum were already present). No pacman transaction, no sysctl or namespace change. Host need: none.
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows two entries, neither written by round-93 seats: `M .scratch/run15-state.json` (orchestrator-owned run state; not touched) and `?? .ufo/closure-kaidoku-r92.json` (the round-92 closure artifact; not touched, not committed here). No misroot to copy.
- Inherited state: the round-92 closure artifact above is untracked at the fleet root; round-92's lane tree was clean at round start (`jj-lane.sh state`: `ahead=0 behind=0`, no untracked).

## Open L0 question

Appended to `.ufo/l0-questions.md`: `kaidoku | round-93 | …` (the v3 `--json-out` crash; operator ruling on whether a stdout-form receipt may admit a claim, and approval of a round-94 successor counter as a new declaration). The lane routes around it: no block.
