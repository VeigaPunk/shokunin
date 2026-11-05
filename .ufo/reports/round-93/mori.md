# mori — round 93 (attempt 1) report

Lane: mori (fleet and host observability, 森). L1: MoriR93. Lane final hash on `origin/master`:
`8edbb86d6384a12c73cc656041c1a8843a4b2ff7` (verified with `git ls-remote`). Landing revision measured:
`1fc921cf75afa6650b9dc9451b33a2ec0610ae0a`.

## Work performed

Declared claims (2, distinct axes; both verified as frozen; calibration reading left to the closure):

- **C1 — calibration** (score 5, tied lowest non-retired): the round-92 lesson's sentence "each `verified-at`
  names the admission commit of its file" is true of the 19 round-92 trio files. Met as frozen at the landing.
  The attack seat `Mo93R03Atk` reads the repair as bookkeeping, not calibration (LEARNING.md accepts commit or
  date; the sentence was lesson prose); the axis verdict is left for the closure.
  - Before (`7b3fe9d5`): `python3 -I .ufo/waves/round-93/count-c1.py 7b3fe9d5 --repo <lane> --report` →
    `C1_REPORT rev=7b3fe9d540c9 trio=98 claim_r92_true=0 files=19 adm_ok=7 adm_fail=12 patched12=0/12 seven_same=7/7 census_rc=0`
    (`.ufo/waves/round-93/evidence/measure-c1-entering.txt`).
  - After (`1fc921cf`): `C1=met trio=98 claim_r92_true=1 files=19 adm_ok=19 adm_fail=0 patched12=12 seven_same=7 census=ok`
    (`.ufo/waves/round-93/evidence/after-c1-1fc921cf75afa6650b9dc9451b33a2ec0610ae0a.txt`).
- **C2 — operability** (score 7): no tool under `tools/` hardcodes a host home path. Met as frozen at the landing.
  - Before (`7b3fe9d5`): `C2=unmet home_literals=18 vgpnk_refs=18 tools=3 selftests=3/3 census=ok`
    (`.ufo/waves/round-93/evidence/measure-c2-entering.txt`).
  - After (`1fc921cf`): `C2=met home_literals=0 vgpnk_refs=0 tools=3 selftests=3/3 census=ok`
    (`.ufo/waves/round-93/evidence/after-c2-1fc921cf75afa6650b9dc9451b33a2ec0610ae0a.txt`).

Work items, each with its evidence pointer:

- Frozen contract, counters and controls committed before dispatch: `.ufo/waves/round-93/contract.md`,
  `count-c1.py`, `count-c2.py`, `controls-r93.sh`, `evidence/controls-r93.txt` (every frozen control unmet at entering,
  with `checks_failed` named), committed at `6d82b8d7`.
- Premise checks (QUALITY 196), committed in the contract: P1 wrapped lesson sentence at `corpus/lessons/round-92.md:51-52`;
  P2 host-literal count (`git grep -c vgpnk 7b3fe9d5 -- tools` = 12 lines; byte count 18; regex count 18);
  P3 rule 2 refusal of in-place digest completion; P4 zero recheck cadence rows due at 2026-11-05.
- Wave `w1` spec, dispatch and registry, committed at `d8a9b28c`: `.ufo/waves/round-93/w1-spec.json`,
  `w1-dispatch.json`, `w1/swarm-registry.json`; `plan` and `run` under the v1 policy
  (`scripts/hyaku/ufo-wave-policy.json`, band 8–16), one `taskCall` of 12 spawn members.
- Seat outputs (all 12 returned; none dead; `w1-results.json`, `w1/*.md`, `w1/patches/*.patch`); findings used below:
  - `Mo93E01Vgpnk` (executor): C2 repair patch; `C2=met` at its commit; selftests 3/3.
  - `Mo93E02Verif` (executor): C1 data patch; `C1=met` at its commit; per-file old/new lines in its note.
  - `Mo93E03Equiv` (executor): equivalence harness `w1/equiv-c2.sh`; proof 1 A=B identical rc 0; proof 2
    able-to-fail (one-character `--help` change) → `different`, rc 1.
  - `Mo93S01Lesson` (scribe): drafts for the round-92 correction and the Mistakes table (used after review).
  - `Mo93Sc01Src` (scout): S622 (git-log documentation) and S623 (Python `-I` documentation) opened, quotes
    located, rows drafted (`w1/Mo93Sc01Src.md`, `w1/patches/Mo93Sc01Src.patch`).
  - `Mo93R01Atk` (reviewer): C2 host-path forms. Concatenation, relative `../../<user>`, Windows/macOS and
    trailing-dot forms were not caught by the regex conjunct; forms carrying the username are caught by the
    byte conjunct; the forged one-file repair reads `unmet`. Named limit extended (see Routed defects).
  - `Mo93R02Atk` (reviewer): C1 re-derivation matches the receipt (set difference empty); forged repairs caught
    (body edit: `patched12=11`; another file's hash: `adm_fail=12`). Found a plain-substring weakness (R02, routed).
  - `Mo93R03Atk` (reviewer): calibration definition. Repair judged bookkeeping; sentence was prose; `7/98` true before.
  - `Mo93R04Sweep` (reviewer): premises re-checked at `7b3fe9d5`; found the spec was committed separately (disclosed)
    and a host path in the counters' CENSUS constant (routed).
  - `Mo93K01Crit` (critic): P3 correct (drop was right); C2 a narrow real operability move; named the one trust element.
  - `Mo93M01Mut` (mutation-tester): six mutants; three survived the frozen battery (m1, m4, m6), two were flipped by
    their claim's control. The gaps are closed by the extension (below).
  - `Mo93Conn01` (connector): cross-lane facts (`w1/Mo93Conn01.md`); host-path and verified-at conventions measured.
- Wave outcome and landing: repairs integrated by `git apply` of the two non-overlapping patches; landed at `1fc921cf`
  with the wave reports and patches as evidence (`jj-lane.sh` commit). Both counters re-run at the landing (above).
- Post-freeze control extension (disclosed; the frozen counters and frozen controls are byte-identical to `6d82b8d7`):
  `.ufo/waves/round-93/controls-r93-ext.sh`, three controls on the landed base, each must read unmet:
  wrong-hash (`C1=unmet adm_fail=12 checks=admission`), census-break (`C1=unmet checks=census`),
  bare-username (`C2=unmet vgpnk_refs=1 checks=vgpnk_refs`) (`evidence/controls-r93-ext.txt`). Mutant kill:
  under m1 the wrong-hash control reads `C1=met`; under m4 the census-break control reads `C1=met census=rc1`;
  under m6 the bare-username control reads `C2=met vgpnk_refs=1` (`evidence/mutant-kill-ext-r93.txt`).
- Read-window demonstration: 4096 bytes → `trio 97`, 65536 bytes → `trio 98` at `7b3fe9d5`
  (`evidence/window-demo-r93.txt`).
- Round-92 correction of record, appended (lines 51-52 not edited): `corpus/lessons/round-92.md` (last section).
- Lesson: `corpus/lessons/round-93.md` (Claims, Work, Mistakes M1–M6, Routed defects, Gate, Assimilation, Trend, Planned).
- SCORECARD round-93 section and capability row; LOG round-93 entry (`SCORECARD.md`, `LOG.md`).

## Landed changes

| Change | LOG entry | Commit |
|---|---|---|
| Frozen contract, counters, controls, entering receipts | LOG.md `## Round 93` | `6d82b8d7` |
| Wave spec, dispatch, registry | (evidence) | `d8a9b28c` |
| Landing: `tools/mori-blind-check.sh`, `tools/mori-misroot-sweep.py`, `tools/mori-round17-context-check.py` (host literals derived); 12 `corpus/knowledge/*.md` `verified-at:` lines; `corpus/QUALITY.md` 198–201; wave `w1` reports and patches | LOG.md `## Round 93` | `1fc921cf` |
| Post-freeze evidence: `controls-r93-ext.txt`, `window-demo-r93.txt`, `mutant-kill-ext-r93.txt`, after-receipts | LOG.md `## Round 93` | `2d14e493` |
| `corpus/SOURCES.md` S622, S623; `corpus/lessons/round-93.md`; `corpus/lessons/round-92.md` correction (appended); `SCORECARD.md`; `LOG.md`; `.ufo/waves/round-93/controls-r93-ext.sh` | LOG.md `## Round 93` | `aade1775` |
| Wave evidence: `w1-results.json`, `w1/Mo93Sc01Src.md`, scout patch, equivalence receipt | (evidence) | `8edbb86d` (final lane hash) |

Pushed: `git ls-remote origin refs/heads/master` → `8edbb86d6384a12c73cc656041c1a8843a4b2ff7`.

## Before → after measurements

Counting commands, each run on the revision it names:

- C1 (`7b3fe9d5`): `python3 -I .ufo/waves/round-93/count-c1.py 7b3fe9d5 --repo <lane>` → `C1=unmet trio=98 claim_r92_true=0 adm_ok=7 adm_fail=12 patched12=0`, exit 1.
- C1 (`1fc921cf`): same command → `C1=met trio=98 claim_r92_true=1 adm_ok=19 adm_fail=0 patched12=12 seven_same=7 census=ok`, exit 0.
- C1 (`aade1775`, final): `C1=met … rev=aade1775e0a8`, exit 0.
- C2 (`7b3fe9d5`): `python3 -I .ufo/waves/round-93/count-c2.py 7b3fe9d5 --repo <lane>` → `C2=unmet home_literals=18 vgpnk_refs=18 tools=3 selftests=3/3 census=ok`, exit 1.
- C2 (`1fc921cf`): same → `C2=met home_literals=0 vgpnk_refs=0 tools=3 selftests=3/3 census=ok`, exit 0.
- C2 (`aade1775`, final): `C2=met … rev=aade1775e0a8`, exit 0.
- Equivalence (`bash .ufo/waves/round-93/w1/equiv-c2.sh 7b3fe9d5 1fc921cf <dir>`): `--help` and `--selftest` output identical for all three repaired tools; the harness verdict is `different` only because it lists each tool's own source bytes (`tree/tools/<t>`); recorded as `evidence/equiv-c2-entering-vs-landing.txt`.

## Sources & frontier

- Registry rows (`grep -cE '^ {0,3}\| ?S[0-9]{3,} ?\|' corpus/SOURCES.md`): before **393** (`7b3fe9d5`), after **395** (`aade1775`).
- Rows added by tier: tier A 2 (S622 git-log documentation; S623 Python `-I` documentation). Tier B and C: 0.
- Rows touched old→new: none (no status, recheck or used-by changed on any existing row).
- Status histogram at `aade1775` (`awk` over the Registry, command in `corpus/SOURCES.md` census note): mined 335, queued 25, rejected 35 (S622 and S623 are `mined`, counted in 335).
- Frontier rows advanced: none of FR1–FR14 was advanced this round (the round's ground is the registry hygiene and the host-path portability of tools; `corpus/README.md` `## Frontier` unchanged).
- Sourced claim: C1's admission-commit derivation rests on S622 (git-log `--diff-filter=A` and `%h`), opened this round (`Mo93Sc01Src`), cited in `corpus/lessons/round-93.md` Gate.
- Assimilation: none (`merge/mori/` not opened this round; the claims are not matched against a staged theme).
- considerthese: none mined. `considerthese/2026-10-26.md` records its suggestions 1–3 as adopted (QUALITY 123, 127, round 49) and its status line (item 4) says so; no proposal is still unimplemented.
- Census validate: `bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin mori` → `mori ok`, exit 0. W04 duplicate-URL warnings: S615/S619 and S235/S349 pre-existing; S622 shares its URL with S059 (tier C, a different scope, pre-existing; a warning, not an error); S623 has no duplicate.

## Trend verdicts

- **expansion: unchanged.** Two source rows admitted; no knowledge entry added on uncovered ground.
- **quality: unchanged.** 12 `verified-at` lines now name a git-checkable admission commit; no admitted entry was superseded or re-verified against its source. The reading "improved" is left to the closure.
- **discernment: unchanged.** Gate decisions (S622 and S623 admit; the lesson's Gate) are the lane's own seats, not an outside spot-check; no non-author verdict exists yet.

## Routed defects and named limits

- **R02 (routed, not fixed).** `count-c1.py` tests `ac[:7] in va` as a plain substring with no word boundary. No current file triggers it (`other7=0`), but it is a real false-pass path. The counter is frozen; the fix is a new counter revision with an embedding control (round 94).
- **Counter-owned host path (routed).** `count-c1.py` and `count-c2.py` name `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh` as a constant. Outside `tools/`, so C2 does not measure it (round 94 amendment).
- **Digest-gate debt (carried).** 31 prefix-only rows and S125 unpinned (`.ufo/waves/round-90/w1/Mo90S01Sources/sources` root). Completing them in place breaks CORPUS rule 2; supersession is mismatch-only (QUALITY 193/195). Recorded in the L0 side channel as a decision for the operator.
- **C2 named limits:** concatenated or `os.path.join('/home', …)` paths; the regex misses Windows, macOS and trailing-dot forms that carry no username.
- **C1 named limit:** the admission hash is checked as a substring of `verified-at:`, not as the commit that introduced the current content.
- **Procedural:** the wave spec was committed in `d8a9b28c`, not together with the contract (`6d82b8d7`), contrary to contract ordering step 1 (disclosed; the spec was committed before the ready file).

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — pointer: `SKILL.md`; this round added none (the claims were on the registry and tools).
- [~] At least one end-to-end domain task executed and logged in LOG.md — pointer: `LOG.md` `## Round 93` (the registry-to-tool repair run end to end, counters at landing).
- [~] Instructions executable by an agent without oral context — pointer: `.ufo/waves/round-93/controls-r93.sh` and `controls-r93-ext.sh` (run by any seat; both ran this round).
- [~] No cross-domain bleed (PROVINCE.md still accurate) — pointer: `PROVINCE.md` (Refuses list; the round touched `tools/` and `corpus/` only; no sibling surface).

No box is `[x]`: no non-author verifier has signed one.

## Stale-lane

Respawn-per-round driver; no other mission of this lane is open. No dormant or silent mission was observed.

## Tool installs

None. The round used only pre-existing tools: `git`, `python3`, `bash`, `sed`, `grep`, `awk`, `tar`, `curl`. Seats reported no installs. The scout's two fetches were plain HTTP GETs of official documentation pages (HTTP 200).

## Wave shape

One v1 wave `w1` under `scripts/hyaku/ufo-wave-policy.json` (band 8–16): 12 seats; residual 0; no second wave. Roles: executor 3, scribe 1, scout 1, reviewer 4, critic 1, mutation-tester 1, connector 1. Attack seats (reviewer, critic, mutation-tester) 6/12 = 50 %. Planner: held by the L1 (the validator rejects `planner`). Dead seats: none (12 of 12 returned output). Routing: policy-bound, not passed.

## Open L0 question

Appended to `.ufo/l0-questions.md` (see the fleet commit): operator decision on whether the digest-gate prefix-only debt (31 rows) should be supersession-eligible under QUALITY 193/195, given CORPUS rule 2.
