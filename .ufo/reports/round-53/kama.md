# kama round 53 report

## Work performed

Declared claims: **C1 operability 8→8**, byte-level identity for code executed by the replayed llama.cpp server; **C2 calibration 7→7**, resolving or disclosing cited repository paths.

- C1: added executable-mapping records to the live receipt, replay checks against release archive members, and a counter that compares mapped executable ranges from `/proc/<pid>/mem` with its own archive download. Sources S506/S507 were admitted and opened; S508 was rejected for unprivileged `map_files` access. Evidence: `tools/kama-llamacpp-live.py`, `tools/kama-live-replay.py`, `.ufo/waves/round-53/measured/c1-build.out`, and `corpus/SOURCES.md:259-261`.
- C1 adversarial evidence: a post-check library swap and a forged replay record are caught by the frozen counter (`.ufo/waves/round-53/w1/out/J1SwapChecked.md`, `J2SwapUnchecked.md`, `J3ForgedReceipt.md`); omitted-library control is caught (`J4OmitLib.md`). Limits include root-owned outside-tree code accepted as host code (`J5Preload.md`), byte-identical host-install code, skipped executable memfd mappings in the frozen counter, and non-executable/model bytes (`SCORECARD.md`, “What `met=True` does not show”).
- C2: created a cited-path parser/counter, a correction ledger, fixed two SKILL.md citations in place, and appended SCORECARD correction records. Evidence: `tools/round53-cited-path-check.py`, `registry/cited-path-corrections.tsv`, `SCORECARD.md:3027-3031`.
- C2 falsification: hiding dead SKILL.md citations and removing their rows still yields `met=True` (`.ufo/waves/round-53/w1/out/J12Hide.md`); an upstream URL with HTTP 200 but wrong bytes also passes (`J11BadFixed.md`). C2 is **not verified/admitted** despite the counter's build result; its declared kill rule fails.
- Round-52 closure R1 corrected by appended S509; S505 remains unchanged (`corpus/SOURCES.md:258-262`, `corpus/lessons/round-53.md` §Gate, `S2Anchor.md`).
- Round-52 R4: seat X9Immut delivered a 13/13 selftested tool and found 8 rewritten reports plus one restored in rounds 46–52 (`.ufo/waves/round-53/w1/out/X9Immut.md`); it was not installed as a lane tool before the wrap.
- One considerthese proposal was reflected as QUALITY KQ97; shokuknow assimilation is none (`corpus/QUALITY.md:477`, `A1Assim.md`).
- The sources census ran at start and end, both exit 0; the end result is `.ufo/waves/round-53/census/end.out`.
- Lane commits and push: build/evidence `e81d90e64b043cc18fe0a52fe151b298c73f3c33`; late M3Live/M6Ledger seat evidence `96615c35e6606b155358f01d8970a9f29e5bbb68` and `2a7b3ba2b7e46cfd51e98065565b4c7784ddf143`. `git ls-remote origin refs/heads/master` and `jj-lane.sh state` confirm final lane tip `2a7b3ba2b7e46cfd51e98065565b4c7784ddf143`. LOG entry at `LOG.md:2435-2443`.

## Landed changes

| Change | LOG.md entry | Lane commit |
|---|---|---|
| C1 live receipt `code_mappings`, replay archive/member verification, required-library and executable-memfd hardening/selftests | `LOG.md` round 53, C1 paragraph and integration results | `e81d90e64b043cc18fe0a52fe151b298c73f3c33` |
| C1/C2 frozen counters, preregistration, base controls, wave spec/results collected by wrap, build measurements, start/end census | `LOG.md` round 53, freeze/build/wave paragraph | same |
| C2 cited-path counter, ledger, SKILL fixes, SCORECARD correction and counter-limit errata | `LOG.md` round 53, C2 paragraph | same |
| Sources S506–S509, lesson with Gate/Mistakes/Errata, QUALITY KQ94–KQ97, README frontier, SCORECARD axes re-anchors and round-53 section | `LOG.md` round 53, closure and lesson pointers | same |
| L0 question and two append-only wording corrections for the ed135b3c ruling | Fleet commits `ee9f7341`, `d2a6c59a`, and `70df4d76` | lane report records the unresolved operator question |
| Late M3Live mutation and M6Ledger attack receipts written after the user-directed wrap | No new LOG entry; supplementary wave artifacts | `2a7b3ba2b7e46cfd51e98065565b4c7784ddf143` |

## Before → after measurements

- **C1 operability 8→8**, frozen counter `tools/round53-replay-code-audit.py`, measured against build commit `c22602bd8d83ab26349d1087e916ca537ee4f9d1`: `python3 tools/round53-replay-code-audit.py --repo <clone> --tip <full-commit> --scratch <dir> --out <receipt>`. Base: `bind=1 sealed=1 code=0 teardown=1 newrow=0`, `coderuns=0/3`, `met=False`, exit 1. Build: `bind=1 sealed=1 code=1 teardown=1 newrow=1`, `bound=3/3 sealedruns=3/3 coderuns=3/3`, `met=True`, exit 0. Receipts: `.ufo/waves/round-53/controls/base.c1.out` and `measured/c1-build.out`.
- **C2 calibration 7→7**, frozen counter `tools/round53-cited-path-check.py`, measured against the same build: `python3 tools/round53-cited-path-check.py --repo <clone> --tip <full-commit> --scratch <dir> --out <receipt>`. Base: `cited=679 unresolved=16 undisclosed=16 met=False`, exit 1. Build: `cited=682 unresolved=14 disclosed=14 undisclosed=0 bad=0 stale=0 dropped=0 met=True`, exit 0. However `J12Hide` returns `met=True` after hiding SKILL.md evidence citations; the kill criterion is falsified, so this claim is not admitted. Receipts: `.ufo/waves/round-53/controls/base.c2.out` and `measured/c2-build.out`.

## Sources & frontier

- Census before: `.ufo/waves/round-53/census/start.out`, exit 0 (`kama ok`). Census after: `.ufo/waves/round-53/census/end.out`, exit 0 (`kama ok`; W04 duplicate-URL warning for S509).
- Added four tier-A rows: two mined (S506, S507); two rejected/correction records (S508, S509). No existing row status/recheck/used-by changed. Frontier: executable archive-library code is now byte-compared in the sampled replay; host libraries, model/data mappings, download provenance and other stated limits remain frontier. No knowledge entry admitted.
- Assimilation: none from shokuknow. One `considerthese/2026-10-26.md` proposal (proposal 2) was reflected in KQ97; it is not a new axis claim.

## Trend verdicts

- **Expansion — unchanged.** No knowledge entry or new covered-domain ground was admitted; registry rows alone do not count as expansion.
- **Quality — harmed.** C1's replay check improved, but C2's frozen counter admits hiding SKILL.md citations and accepts upstream HTTP 200 without matching bytes; Sen4Fixture also found inherited Git environment can redirect its scratch fixture. These are material measurement-integrity defects.
- **Discernment — unchanged.** No independent outside closure/spot-check was received; swarm seats are still lane work, not the non-author verifier.

## SHONEN

- [~] Skill contains decision tables, error patterns, checklists, cited sources — `SKILL.md` §§Round-53 instrument registry and post-wave limits.
- [~] At least one end-to-end domain task executed and logged — `LOG.md` round 53; replay evidence in `.ufo/waves/round-53/measured/c1-build.out`.
- [~] Instructions executable without oral context — `SKILL.md` registry; independent outside execution review remains open.
- [~] No cross-domain bleed — `PROVINCE.md` unchanged; `N1Overlap.md` finds no ownership conflict.

Stale-lane: no other lane mission is open. Tool installs: none.

**Wave status / wrap:** one validated v2 wave, 66 seats, role mix executor 23, mutation-tester 6, reviewer 7, critic 8, sentinel 4, scout 8, scribe 5, connector 3, simplifier 1, revenger 1; attack share 21/66 (31.8%). The user-directed wrap arrived before `WAVE-DONE`; final settled statuses and dead-seat tally were unavailable at filing. The report does not claim wave completion or round admission. The L0 question on restored ed135b3c history remains unanswered.
