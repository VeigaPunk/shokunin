# kama — round 93 report (L1 KamaR93, attempt 1)

Lane repo `/home/vgpnk/Projects/shokunin/kama-shokunin`, branch `master`, final pushed hash `c0fbff4277119cd518aa0dbc5cc9fd5137590626`
(`git ls-remote origin refs/heads/master` prints it). Base `5af794958b0fc08f574aa2e67650282269549b02`; freeze
`0f272a3773be25a6cbdaf75f1a7a3ec293b60f8d`.

## Work performed

Declared claims (frozen in `plans/round-93-claims.md` at `0f272a37`, every control committed before the freeze):
**C1 — operability** (capability `router-file-repeat`): the probe's router model-file verdict does not change when a
listing repeats one model file (round-92 wave-1 SC02 F6: a listing that repeats one slow invalid GGUF flips
`MODEL_UNLOADED` to `MODEL_OK` at a load-dependent count). **C2 — depth** (lowest axis, 7; sourced S600–S603 opened
this round, S593/S596–S599 re-opened): `SKILL.md` §Listen port and slot-count setters (round 93 revision), one row per
port / slot-count line of the pinned llama.cpp b12177 server sources (P01–P48) and decisions R16/R17 superseding the
round-92 R01/R08 (closure R2/R3), K2 = a non-author read finds a misstating row or decision.

- Pre-freeze controls (`.ufo/waves/round-93/controls/`): C1 base `mismatches=5 positive_mismatches=0`, exit 1
  (`c1-base.out`, load 48: R02–R06 `MODEL_OK`); first run with the v0 counter `c1-base-v0.out` (R02 green at load 21);
  C1 battery 5/5 (`c1-forgeries.out`: P0 candidate 10/10; F1 fail-closed → P02 red; F2 path-string memo → R05 red;
  F3 per-file deadline → R04 red; F4 first-8 cap → P02 red). C2 base `rows=0 missing=48`, exit 1 (`c2-base.out`); C2
  battery 12/12 (`c2-forgeries.out`: P0 48/48 + decisions 2/2; V1 the round-92 R01/R08 decisions → `decisions_bound=0`;
  V2–V9 each red on its named check; V10 corrupt archive exit 2; L1 disclosed limit binds). Harm base all green
  (`harm-base.out`); sources opened (`sources-opened.out`, 9 files, raw digest = archive member digest); census start
  exit 0 (`census-start.out`).
- C1 implementation `fe5f031c` (`ROUTER_PY`: `gguf_state` memo `SEEN` keyed by file identity, raw parse
  `gguf_parse`); repaired in round at `b3765799` (`st_ctime_ns` added; wave-1 RV01 DEFECT-1). C2 implementation
  `ee19acbd` (SKILL section, S600–S603).
- Measured: C1 `measured/c1.out` 10/10 cells, `mismatches=0 positive_mismatches=0 probe=rev`, exit 0 at `fe5f031c`, and
  `measured/c1-M1b.out` the same at `b3765799`; harm unchanged at both (`harm-M.out`, `harm-M1b.out`: check.py 77/77,
  test-snapshot 30/0, r89 11/0/0, r90 13/0/0, r91 12/0/0, r92 15/0/0, router 1234 GET `MODEL_OK router-unloaded-autoload`);
  r90 reason receipt re-captured at both probes with 24 identical triples and current (`r90-reason-rows-tip.out`,
  `r90-reason-rows-tip-M1b.out`, KQ148); doubling `measured/c1-doubling.out` (512–16384 repeats: M1 1.2–2.2 s
  `router-model-invalid`, base `MODEL_OK` at the 8 s kill); RV01 DEFECT-1 reproduction `measured/c1-ctime-rewrite.out`
  (entry 2 wrong 3/3 at `fe5f031c`, right 3/3 at `b3765799`). C2 `measured/c2.out` `population=48 rows=48 bound=48
  unbound=0 missing=0 duplicates=0 fabricated=0 derived_checked=47 derived_disagree=0 decisions=2 decisions_bound=2
  … skill=rev`, exit 0 at `ee19acbd` (archive downloaded by the counter); tip re-measures `c1-tip.out`, `c2-tip.out`.
- **C2 not verified (author):** wave-1 reviewer RV02 (`w1/RV02SetterRows.md`) reports P05–P07 as misstating (labels
  `-`/`unrelated` on the non-server `--parallel` declaration, assignment and env declaration whose twins P02–P04 carry
  `n_parallel`/`declares`/`overrides`, against the section's own glossary) and R16's router-child clause defeated by a
  child preset carrying `--vision-gemma-*` (argv order: `std::map` by first option name puts it after `--port`; the
  child listens on 8014). That is K2. Dated correction `SKILL.md` §Round 93 correction; lesson M4, M6; QUALITY KQ151
  (`measured/kq151-twins.out`).
- Wave `w1`: ONE v1 wave, 12 seats under `ufo-wave-policy.json` (band 8–16) — reviewer 2 (RV01, RV02), critic 2 (CR01, CR02), mutation-tester 2 (MT01, MT02), executor 2 (EX01, EX02), scout 2 (SC01, SC02), connector 1 (CN01), scribe 1 (SB01); attack share 6/12; 11 seats settled with reports; SC02ProbeVerdictSweep still running (active scratch, no report) when the L1 filed under the operator's request-budget wrap-up — no `WAVE-DONE` and no `w1-results.json` received, so seat counts come from the report files, not results.json (`.ufo/waves/round-93/w1-results.json`). No residual call; round total 12. Reports `.ufo/waves/round-93/w1/*.md`. Findings: RV01 C1 holds on 58 single-candidate and every non-mutating shape, DEFECT-1 (stale state on a same-size rewrite with restored mtime) → repaired in round (`b3765799`, `measured/c1-ctime-rewrite.out` 0/3 → 3/3); RV02 K2 fired on C2 (P05–P07 labels; R16 router-child argv order); SC01 K2 again (a `config.ini` sets port 18099 / 7 slots on the pinned binary; `llama-cli` embedded server 1 slot on a free port; AIP inherited by a router child) — measured live; CR01 15/19 wrong probes pass the C1 counter (hard links, P02 edge, coarse keys), none falsifies M1, the gap shapes graded right at `b3765799` (`measured/c1-gapshapes.out`); CR02 20/38 forged C2 tables bind; MT01 4/16 probe mutants killed; MT02 10/26 counter mutants killed; EX01 no base-right/M1-wrong held-out cell (distinct-copies limit confirmed); EX02 live b12177 router: probe = oracle at both revisions, status.args shape matches the stub; CN01 no sibling contradiction of C1/C2, kama's own registry rows 35–37 cite no R16 setter (routed), kagi `SKILL.md:9-10` stale 8080 pin (reported); SB01 lesson corrections and dispositions applied (`00a0246d`); SC02 (probe verdict sweep): unsettled at filing, no findings counted.
- Planner seat: held by the L1 (validator rejects `planner`); no planning item rode a seat.

## Landed changes

| Commit | What | LOG.md |
|---|---|---|
| `0f272a3773be25a6cbdaf75f1a7a3ec293b60f8d` | freeze: plan, two counters, pre-freeze controls | LOG §Round 93 |
| `fe5f031cb1b9d33e1160360d892149b8ac3c7771` | C1 router model files parsed once per identity | LOG §Round 93, C1 bullet |
| `ee19acbdabc8ac572e82ae56459c364457895b06` | C2 SKILL setter section P01–P48, R16/R17, S600–S603 | LOG §Round 93, C2 bullet |
| `995fe9056ca3f411aa138264b54750d62cf9757e` | r90 reason receipt re-captured at the C1 probe (KQ148) | LOG §Round 93, C1 bullet |
| `4c4adc63b4d6a6cfe40533b4612d6d3e60760fc9` | measured receipts C1/C2, harm, wave spec and dispatch | LOG §Round 93 |
| `4854ce0405e5157fb1f0da39d058a95411f33751` | record: SCORECARD §Round 93, capabilities, head rows, planned r94; LOG, PROVINCE, README, QUALITY KQ150, lesson M1–M3 | LOG §Round 93 |
| `a7fa8f8a9f154b7cf8a8c5e422e801df040fc93b` | C1 doubling receipt, tip re-measures | LOG §Round 93 |
| `333ebf4713ffab8705d146b2146cf4b27cff1507` | PROVINCE names the setter-rows instrument | LOG §Round 93 |
| `b37657998858b6300fc8fbbbebb7e256239bf0f8` | C1 key adds `st_ctime_ns` (RV01 DEFECT-1) | LOG §Round 93, after-wave bullet |
| `8e9ecd636b31a8edaf612fe992c51f2375ac976f` | C1 re-measured after the fix, receipt re-captured | LOG §Round 93, after-wave bullet |
| `54b8578f0effa249596947bfc1081da902dc4bec` | C2 not verified: SKILL correction, lesson M4/M5, KQ151, corrections | LOG §Round 93, after-wave bullet |
| `b4e0011a1029ce92eec11ec966fe8283e24e877f` | SCORECARD head mirror 61→63 capabilities, depth row re-anchored | lesson Dispositions |
| `b56fe355eb31cf9488ee09edb3d60b1506ce3412` | coverage row re-anchored to PROVINCE.md | — |
| `00a0246d35d3e8d1b041a80a92c09bd94274b751` | lesson M6, corrections to M1–M4 (SB01), dispositions R1–R6 | lesson |
| `487e5b151112503d0ebc383015564864e75e227a` | wave-1 counter findings (CR01/CR02/MT02), C1 at the record tip | SCORECARD §Round-93 wave-1 counter findings |
| `f4fc40763cf0b897a560e226a844816575d39b4d` | C1 control replay (F4 named cell load-sensitive), lesson M7, CN01 notes | lesson M7 |
| `684cf97ea7326e01deeea488bb676886edb89463` | harm at the tip 7/7, C2 battery replay 12/12, census-end, MT01 findings | — |
| `e25b25748d010cb7b8eded4756ce3b0d995e29ae` | planned r94 items 5–6 from wave 1 | SCORECARD §Planned (round 94) |
| `042d3c0d26f94db364f81d1c2665666475a97f88` | C1 gap shapes (hard links, symlinks, collisions, 2048 valid-last) graded at base and `b3765799` | — |
| `1fc52d84baa09f6a95d9980e0fd8c0863a627c1f` | C1 counter 3× at the tip | — |
| `e7e92106f6d9fd474bb322eff66dead307d22a32` | C1 disclosed-limit receipt (distinct copies flip at n=8, load 43) | SCORECARD §Planned (round 94) item 2 |
| `b556f7353e63a9a40e255dedaf6e8822c4a3efe6` | SC01 K2 findings: SKILL second correction note, lesson M8 | lesson M8 |
| `3007a238e7d38e7d8e67b6ed48b349e51852300f` | depth row re-anchored | — |
| `d158c25f3cb36ef30808997036e873f801e9747c` | second C1 control replay (M7 reproduced at load 48) | lesson M7 |
| `45a0297319188dd086a9a6a9ba789b3a2a88195a` | round-94 item 1 baseline (`snapshot --json` 8–64 rows: 2.06/4.63/10.12/23.78 s) | SCORECARD §Planned (round 94) |
| `edc4eefa1d721856f7e2bb65dd6b5ae4f4e913b3` | fresh shared-clone replay of both counting commands (5/5 as recorded) | — |
| `d30f0e1e4a5835bef00fd15efdc42fcacbf11203` | wave w1 evidence (11 reports, out dirs, ready markers) | — |
| `c0fbff4277119cd518aa0dbc5cc9fd5137590626` | terminal gate receipt `measured/gate-final.out`: `PRE_REPORT round=93 arms=14 failed=4 uncommitted=1`, exit 1 — red arms: `round75-instruments` (carried, `APPEND_DEBT events=100 unaccepted=21 bad_rows=19`), `round78-instruments` (host 8080 listener), `round-scope`/`round-clean` (the receipt file itself was uncommitted while the gate ran) | — |

## Before → after measurements

| Claim | Counting command | Before (base `5af79495`) | After | Measured commit | Verdict (author) |
|---|---|---|---|---|---|
| C1 operability | `python3 tools/round93-router-repeat.py --repo . --rev <M1> --work <scratch>` | `cells=10 mismatches=5 positive_mismatches=0`, exit 1 (`controls/c1-base.out`) | `cells=10 mismatches=0 positive_mismatches=0 probe=rev`, exit 0 (`measured/c1.out`; repaired revision `measured/c1-M1b.out`; tip `c1-tip.out`) | `fe5f031cb1b9d33e1160360d892149b8ac3c7771` (repaired `b37657998858b6300fc8fbbbebb7e256239bf0f8`) | **verified** (K1 0, K2 harm unchanged and receipt current, K3 counter unchanged); RV01 DEFECT-1 repaired in round |
| C2 depth | `python3 tools/round93-setter-rows.py --repo . --rev <M2> --work <scratch>` | `population=48 rows=0 missing=48`, exit 1 (`controls/c2-base.out`) | `population=48 rows=48 bound=48 unbound=0 missing=0 … derived_disagree=0 decisions=2 decisions_bound=2`, exit 0 (`measured/c2.out`; tip `c2-tip.out`) | `ee19acbdabc8ac572e82ae56459c364457895b06` | **not verified** — predicate met, K2 fired (RV02: P05–P07, R16 router-child clause) |

## Sources & frontier

- Census command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kama`.
  Start: exit 0, `kama ok` (`.ufo/waves/round-93/controls/census-start.out`). End: exit 0, `kama ok`, W04 pre-existing only (`.ufo/waves/round-93/measured/census-end.out`).
- Rows 339 → 343 (`git show <rev>:corpus/SOURCES.md | grep -cE '^ {0,3}\| S[0-9]{3,}'` at `5af79495` vs tip). Added by
  tier: A +4 (S600 `common/http.h`, S601 `tools/server/server-connect.cpp`, S602 `tools/server/server-http.h`, S603
  `tools/server/server-models.h`, all llama.cpp @ b12177); B 0; C 0. Rows touched old→new: none (S593, S596–S599
  re-opened, digests equal, byte-identical). Rejections in the lesson Gate: `server-models-sched.cpp:423` as a listen-port
  setter; the codeload archive as a SOURCES row.
- Sourced claim: C2 rests on S600–S603 (opened this round) and S593/S596–S599 (re-opened).
- Frontier advanced: the port/slot decisions moved from "one default line" to "every population line of the pinned
  sources, labelled" with a counter that fails the round-92 R01/R08 decisions; frontier left: a label for setters the
  program never registers, the argv-order rule as rows, data-flow setters (L1), many distinct slow model files sharing
  one deadline (C1 limit).
- Mistakes mined: `corpus/lessons/round-93.md` `## Mistakes` M1 (alias cell below its forgery's threshold; KQ150;
  `measured/m1-v0-alias-F2.out`), M2 (range shorthand hid ids; `measured/m2-range-decision.out`), M3 (append-debt
  growth, carried R1), M4 (labels contradicted the section's glossary; KQ151; `measured/kq151-twins.out`), M5 (identity
  key without a mutation control; `measured/c1-ctime-rewrite.out`), M6 (R16 router-child argv order).
- Assimilation: none (no `merge/kama/` theme taken this round). considerthese: not mined this round.
- Previous closure `corpus/lessons/round-92-verifier-spotcheck.md`: dispositions R1–R6 in the lesson (R1 carried, R2
  answered in form / C2 not verified, R3 done for the R01/R08 class, R4 routed to r94, R5 report authored after the
  final push, R6 carried).

## Trend verdicts

- **expansion: improved** — four tier-A rows opened and mined (S600–S603); capability `router-file-repeat`
  demonstrated green at `fe5f031c`, `b3765799` and the tip; `setter-rows` entered as an instrument (its decision rows
  not admitted, C2 not verified).
- **quality: improved** — C1: a load-dependent false green (base `MODEL_OK` on 2048 repeats of an invalid file) is gone
  on every run, harm suites unchanged, and a wave-found stale-state regression in the fix was repaired in round with a
  failing-before reproduction. Offset: C2 not verified (three mislabelled rows, one decision clause).
- **discernment: improved** — the author records C2 not verified on the non-author read; six mistakes mined, two new
  criteria (KQ150, KQ151) each with a receipt that shows it able to fail; the pre-freeze battery killed a counter
  shape (M1) before data.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md` §Listen port and slot-count setters (round 93 revision) + §Round 93 correction; non-author read `w1/RV02SetterRows.md` found three mislabelled rows, so no `[x]`.
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md` §Round 93; `measured/c1.out` (probe graded 10 router listings, 3 runs each); `w1/EX02LiveRouterRepeat.md` (live b12177 router child, probe vs real completion oracle at base and M1).
- [~] Instructions executable by an agent without oral context — counting commands in `plans/round-93-claims.md` re-run by wave seats from text alone (`w1/RV02SetterRows.md`, `w1/CR02SetterCounter.md`, `w1/MT02SetterCounterMutants.md`) and from a fresh clone (`measured/fresh-clone-replay.out`).
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` round-93 lines; `w1/CN01SiblingOverlap.md` (no sibling contradiction of C1/C2; own registry rows 35–37 routed).

Stale-lane: respawn-per-round driver; no other mission of this lane is open.
Tool installs: none by the L1. Seats: none reported (CR02 npx-free; SC01 none).
Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows `.scratch/` (orchestrator-owned) and untracked `trail-ids.txt` (pre-existing since round 91, names no lane) — no kama seat file; nothing moved.
Host note: an Ollama listener on 127.0.0.1:8080 (systemd user unit, pid 134935, started 2026-11-06 23:08:39 -03, not
lane-owned) turned `round78-live-reconcile.py --selftest` red mid-round (registered-port refusal, fail-closed); the terminal gate records it red; not caused by round-93 bytes (the arm reads host listeners).
Upstream (read-only, documented here, not pushed): llama.cpp b12177 router children whose preset carries
`--vision-gemma-4b-default` or `--vision-gemma-12b-default` receive `--port <free>` before the preset option in argv
(`common/preset.cpp:44-51`, `common/arg.h:91-96`), so the preset's `params.port = 8014` wins and the child does not
listen on the port the router recorded (`server-models.cpp:316`, `1218`) [INFERENCE: not run on a live child].
Open L0 questions: none new; `round75-instruments` L0 (r87/r89) still open.

WAVE-DONE: not received for `w1` at filing (SC02 still running); filed early under the operator budget notice ("Wrap up now"), which supersedes the file-after-WAVE-DONE rule for this attempt — disclosed as a conformance defect.
Round shape: one v1 wave `w1`, 12 seats dispatched, 11 reports landed; round total 12; no residual call.
