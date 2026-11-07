# kama — round 92 report (L1 KamaR92, attempt 1)

Lane repo `/home/vgpnk/Projects/shokunin/kama-shokunin`, branch `master`, final pushed hash `378220d3777b62de849847585bf0da7200b3b1c7`
(`git ls-remote origin refs/heads/master` prints it). Base `ed018ca0fa956c5052b3dc6b714a2cb72973da21`; freeze
`309eadafd4d0557a056c1bf61455c59778cf5e1d`.

## Work performed

Declared claims (frozen in `plans/round-92-claims.md` at `309eadaf`, every control committed before the freeze):
**C1 — depth** (lowest axis, 7; sourced S596, S597): `SKILL.md` §Serving defaults (round 92 revision), 15 rows R01–R15
superseding the round-91 table T01–T14 under KQ146 (each llama.cpp option row equals the pinned `--help` default),
K2 = a non-author read finds a misstating row. **C2 — operability** (capability `linear-probe-paths`): the three
super-linear probe paths round-91 wave-1 SC02 measured (`jstr`, `router_refine` `cand`, `served_persist`) run in
linear time, output byte-equal to base on 9 differential cells.

- Pre-freeze controls (`.ufo/waves/round-92/controls/`): C1 base `rows=0` exit 1 (`c1-base.out`); C1 battery 9/9 as
  expected (`c1-forgeries.out`: P0 positive exit 0, V1 round-91 T07 transplant `help-default=-1`, V2–V6 exit 1, V7
  `TYPE_CHECKING` line binds = disclosed limit, V8 unpinned binary exit 2); C2 base `mismatches=6` exit 1 (`c2-base.out`:
  L1–L5 killed at 120 s, L6 54 s; D1–D9 equal); C2 forgeries F1–F3 each fail their named cell (`c2-forgeries.out`);
  harm base all green (`harm-base.out`); sources re-opened (`sources-opened.out`). Counter amendments before freeze are
  recorded with their v0 receipts (`c2-base-v0.out`, `c1-forgeries-v0.out`).
- C2 implementation `fa8aedb7` (`tools/kama-probe.sh`: `AWK_JSTR` one pass with a no-fork fast path, `cand` array,
  `served_persist` awk); C1 implementation `18153ebb` (SKILL R01–R15, S596/S597, knowledge §Round 92 revision, S593/S595
  dated correction = round-91 R2).
- Measured: C1 `measured/c1.out` 15/15 bound, help 7/0, supersedes 14, exit 0; C2 `measured/c2.out` 15 cells 0/0, exit 0,
  slowest 3.43 s at load 79; harm `measured/harm-M.out` unchanged (check.py 77/77, test-snapshot 30/0, r89 11/0/0,
  r90 13/0/0, r91 12/0/0, router 1234 GET `MODEL_OK router-unloaded-autoload`); tip re-measure at `da9b0d90`
  (`measured/c1-tip.out`, `measured/c2-tip.out`, both exit 0).
- L1 equivalence fuzz (`measured/c2-fuzz-equivalence.out`, `c2-fuzz-classify.out`, `c2-fuzz-diff-repro.out`): `jstr` 0
  diffs in 15 000+ cases; `served_persist` differs only on invalid-UTF-8 ids in a UTF-8 locale, where base `normalize_id`
  returned random memory bytes (5 runs, 5 outputs) or split differently from `LC_ALL=C`; M2 equals base under `LC_ALL=C`.
- Harm found and repaired (lesson M3, repeat of round-91 M4): the C2 probe change staled the round-90 reason receipt
  (`measured/r90-reason-rows-stale.out`, exit 1); re-captured with identical 24 triples and re-bound 24/24 at `d5a06431`
  (`measured/r90-reason-rows-tip.out`); QUALITY KQ148.
- **C1 not verified (author):** wave-1 scout SC01 (`w1/SC01SourceReopen.md`), re-read by the L1
  (`measured/kq149-setter-sweep.out`), shows R01's and R08's decision cells overstate the binary — presets
  (`--embd-gemma-default`: port 8011, 32 slots), `AIP_MODE=PREDICTION` (S598), router children on a free port (S599) —
  although the designated reviewer RV02 passed all 15 rows. Dated correction `SKILL.md` §Round 92 correction; lesson
  M4; QUALITY KQ149 (`da9b0d90`).
- Wave `w1`: ONE v1 wave, 12 seats under `ufo-wave-policy.json` — reviewer 2 (RV01, RV02), critic 2 (CR01, CR02),
  mutation-tester 2 (MT01, MT02), executor 2 (EX01, EX02), scout 2 (SC01, SC02), connector 1 (CN01), scribe 1 (SB01);
  attack share 6/12; 0 dead (`.ufo/waves/round-92/w1-results.json`, 12 settled; orchestrator note: its kernel restarted
  mid-wave, outputs delivered). No residual call; round total 12. Reports `.ufo/waves/round-92/w1/*.md`. Findings: RV01
  no reachable behaviour change; RV02 15/15 rows hold; SC01 R01/R08 overstate (→ C1 not verified); CR01 five C2 counter
  forgeries pass, M2 correct on each; CR02 14 wrong C1 tables pass, MT02 16/23 counter mutants exit-identical; MT01 7/19
  probe mutants killed, 4 real gaps (identical at base); EX01 no held-out harm; EX02 no-python and gawk/busybox/mawk
  parity; SC02 F1–F3 linear at M2 plus a new quadratic path outside C2 (`json_array`, routed); CN01 no sibling
  contradiction. L1 doubling at M2: `measured/c2-doubling.out` (≈2× per doubling on all three shapes).
- Planner seat: held by the L1 (validator rejects `planner`); no planning item rode a seat.

## Landed changes

| Commit | What | LOG.md |
|---|---|---|
| `309eadafd4d0557a056c1bf61455c59778cf5e1d` | freeze: plan, two counters, pre-freeze controls | LOG §Round 92 |
| `fa8aedb73d18448383c7a4d75405aba448fe8e38` | C2 probe paths linear | LOG §Round 92, C2 bullet |
| `18153ebb5f9e2ae83f53e7fef57ee579bc409331` | C1 SKILL R01–R15, S596/S597, knowledge revision, S593/S595 correction | LOG §Round 92, C1 bullet |
| `83f9e3d495303aec41a29f0439bd23d0404955f5` | measured receipts, harm at M2, wave spec/dispatch | LOG §Round 92 |
| `d5a064313522392bf7f8498d1a54c0cfd0ad314b` | r90 reason receipt re-captured (M3) | LOG §Round 92, last bullet |
| `54a2c9acfd3ee023d30235bf4e9f76d2cb1a10e3` | record: SCORECARD §Round 92, capability, head rows, planned r93; LOG, PROVINCE, README, QUALITY KQ147/148, lesson, fuzz receipts | LOG §Round 92 |
| `a0e117b3e6543a71db608dab83fed57218cda4d6` | S596/S597 used-by (census E11), retired count, planned path | lesson Gate |
| `da9b0d90dfdc94fa1e4fb55fa0773a78336c9fbb` | C1 not verified: SKILL correction, S598/S599, KQ149, M4, corrections | LOG §Round 92, C1-not-verified bullet |
| `e2e5fd9bdda08b852db50e0e0272032b280a3373` | tip re-measurements, doubling receipt, lesson wave findings | lesson §Wave-1 findings |
| `98c3b1a882a5b0bfad7b46e9d42259b548a59995` | SC02 `json_array` routed (planned r93), fuzz seeds 4–7 | lesson §Wave-1 findings |
| `1da530bf9195ecaa898bba207c190621df92e2cf` | wave w1 evidence (reports, out dirs, results) | — |
| `796964ef57c0199b4ad9d43194f785ea21dc3514` | census-end receipt | — |
| `378220d3777b62de849847585bf0da7200b3b1c7` | terminal gate receipt `measured/gate-final.out`: `PRE_REPORT round=92 arms=14 failed=1 uncommitted=0`, exit 1, sole red arm the carried `round75-instruments` (`bad_rows=19`, L0 open since r87) | — |

## Before → after measurements

| Claim | Counting command | Before (base `ed018ca0`) | After | Measured commit | Verdict (author) |
|---|---|---|---|---|---|
| C1 depth | `python3 tools/round92-server-defaults.py --repo . --rev <M1> --binary /home/vgpnk/.local/opt/llama-b12177/llama-server` | `rows=0`, exit 1 (`controls/c1-base.out`) | `rows=15 bound=15 unbound=0 duplicates=0 engines=3 fetch_failures=0 help_checked=7 help_disagree=0 supersedes=14`, exit 0 (`measured/c1.out`; tip `measured/c1-tip.out`) | `18153ebb5f9e2ae83f53e7fef57ee579bc409331` | **not verified** — predicate met, but R01/R08 decisions overstate the binary (SC01; K2 substance) |
| C2 operability | `python3 tools/round92-linear-paths.py --repo . --rev <M2> --work <scratch>` | `cells=15 mismatches=6 positive_mismatches=0`, exit 1 (`controls/c2-base.out`) | `cells=15 mismatches=0 positive_mismatches=0 probe=rev`, exit 0 (`measured/c2.out`; tip `measured/c2-tip.out`) | `fa8aedb73d18448383c7a4d75405aba448fe8e38` | verified (K1 0, K2 harm unchanged, K3 counter unchanged); counter limits disclosed (CR01 five forgeries pass, MT01 4 gaps) |

Do-nothing and forgery controls ran before the freeze and are committed with it: `controls/c1-base.out`,
`c1-forgeries.out` (9/9), `c2-base.out`, `c2-forgeries.out` (F1–F3 3/3), `harm-base.out`.

## Sources & frontier

- Census command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kama`.
  Start: exit 0, `kama ok` (`.ufo/waves/round-92/controls/census-start.out`). End: exit 0, `kama ok`, warnings W04/W01
  pre-existing only (`.ufo/waves/round-92/measured/census-end.out`). One mid-round E11 (S596/S597 used-by written as
  prose) was fixed in `a0e117b3`.
- Rows 335 → 339 (`git show <rev>:corpus/SOURCES.md | grep -cE '^ {0,3}\| S[0-9]{3,}'` at `ed018ca0` vs tip). Added by
  tier: A +4 (S596 llama.cpp `common/arg.cpp` @ b12177, S597 `tools/server/server.cpp`, S598 `tools/server/server-http.cpp`,
  S599 `tools/server/server-models.cpp`); B 0; C 0. Tier totals now A 323, B 11, C 5
  (`sources-census.sh census --file corpus/SOURCES.md`). Rows touched old→new: S596/S597 `used-by` prose → comma paths
  (same round, logged in the lesson Gate); S593–S595 byte-identical, re-opened (digests equal) with an appended dated
  correction (round-91 R2). Rejections in the lesson Gate: `envs.py:26/111` (TYPE_CHECKING declaration) and
  `common.h:464` as the server slot-count anchor.
- Sourced claims: C1 rests on S596/S597 (opened this round); the correction on S598/S599.
- Frontier advanced: the serving defaults moved from "struct line" to "line the binary uses" (KQ146 counter, help-checked
  7/7) and the setter sweep (KQ149) is now the bar for decision cells; frontier left: a counter that reads run-time
  readers and derivations (V7, CR02), Ollama/vLLM against pinned binaries, SGLang defaults.
- Mistakes mined: `corpus/lessons/round-92.md` `## Mistakes` M1 (differential cell compared a clock; KQ147; shown able to
  fail by `controls/c2-base-v0.out`), M2 (line number from prose; `controls/c1-forgeries-v0.out`), M3 (round-91 M4 fix
  not carried; KQ148; `measured/r90-reason-rows-stale.out`), M4 (decision universalised over other setters; KQ149;
  `measured/kq149-setter-sweep.out`).
- Assimilation: none (no `merge/kama/` theme taken this round). considerthese: not mined this round.
- Previous closure `corpus/lessons/round-91-verifier-spotcheck.md`: R2 fixed (SOURCES §Round-92 correction), R3 applied
  (per-seat scratch roots in `w1-spec.json`), R4 worked by C1 (still open for R01/R08), R5 worked by C2, R1 carried.

## Trend verdicts

- **expansion: improved** — four tier-A rows opened and mined (S596–S599), the knowledge entry gains the round-92
  revision and its setter-sweep correction, and one capability (`linear-probe-paths`) is demonstrated green at
  `fa8aedb7` and the tip (`measured/c2.out`, `c2-tip.out`).
- **quality: improved** — C2: three super-linear probe paths that killed the base at 120 s now finish ≤ 3.5 s with
  differential output byte-equal to base and every harm suite unchanged; the round-90 reason receipt staled by the change
  was re-bound with identical triples. Offset: C1 is not verified (R01/R08 decision cells overstate the binary).
- **discernment: improved** — the author records C1 as not verified on a scout's finding the designated reviewer missed,
  instead of taking the favourable reading of K2; four mistakes mined, each with a criterion (KQ147–KQ149) and a receipt
  that shows it able to fail; the pre-freeze base-against-base control caught a counter defect (M1) before any data.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md` §Serving defaults (round 92 revision) + §Round 92 correction; no non-author verifier named.
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md` §Round 92; `.ufo/waves/round-92/measured/c2.out` (probe graded on 15 stub listeners, snapshot persisted on two).
- [~] Instructions executable by an agent without oral context — counting commands in `plans/round-92-claims.md` re-run by wave seats from text alone (`w1/RV02DefaultRows.md`, `w1/CR01LinearCounter.md`, `w1/CR02DefaultsCounter.md`).
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md` round-92 line; `w1/CN01SiblingOverlap.md` (no sibling contradiction of R01–R15).

Stale-lane: respawn-per-round driver; no other mission of this lane is open.
Tool installs: none persistent. EX02 fetched busybox 1.35.0 (official static binary, busybox.net) and built mawk 1.3.4-20250131 (invisible-island.net tarball) into its own scratch only, to test awk portability; CR02 ran `npx --yes markdown-it` 15.0.3 (npx cache). No pacman.
Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows `.scratch/` (orchestrator-owned) and
untracked `trail-ids.txt` (present since round 91, names no lane) — no kama seat file; nothing moved.
Open L0 questions: none new; `round75-instruments` L0 (r87) still open.
