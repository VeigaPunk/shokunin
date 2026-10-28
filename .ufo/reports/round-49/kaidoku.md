# kaidoku — round 49 report

Lane `kaidoku`, round 49, attempt 1. Lane repo `/home/vgpnk/Projects/shokunin/kaidoku-shokunin`. Base `e4f2cfa5ebff863a4d5d13c040cb0c41be6a40f9`; **single freeze** `decc5697bfd4ec1e9de4a762ad199d9bd9c4230d` (no amendment series); scored revision `00b185045b82af9398e7497d068a14ee3023fecb`; lane tip `623476eef55640258fa5d4ff95a87ba59c49279f` (`git ls-remote origin refs/heads/main` prints it).

## Work performed

**Declared claims:** R49-C1 (coverage: SquashFS v1/v2 `squashfs_v1`/`squashfs_v2`, four standard v1.0/v2.0 fixtures, Frontier → Core through REA 6.5.0 `extract-firmware`) and R49-C2 (calibration: nine round-48 self-assessment atoms A1–A9 counted and repaired). Both are met under their frozen predicates; admission is for the operator to rule (see the limits below).

- Read the round-48 closure (`corpus/lessons/round-48-verifier-spotcheck.md`, rejected-harmed) and its routed defects; designed the round around "one freeze, instrument attacked before the freeze, falsified after the landing". Evidence: `plans/round-49-claims.md` at `decc5697`.
- **Wave 1** (48 seats, `.ufo/waves/round-49/w1/`, committed `14936cb9`) attacked the DRAFT counters and plan; its defects (forgeable provenance clause, unenforced plan sentences, vacuous CTL-C1-5, runner write-scope hazards, C2 inputs read at REV, duplicate-line and quantifier holes) were folded in before the freeze (plan "Wave-1 amendment record"). Freeze commit `decc5697` = plan + `tools/round-49/**` + control fixtures; controls scored at the freeze (`.ufo/waves/round-49/controls/summary.json`, 6/6 as expected, `kill_rule_fires false`).
- C1 data run `c1-run.sh --data-run` → `corpus/evidence/round-49/c1/` at `4aabb0b4` (four receipts, exit 0 each; 3/3/4/4 members published, `gaps []`). Landing `3847f393`…`29883d4e`; **wave 2** (40 seats, `w2/`) reproduced both counting commands and attacked the landed bytes; repairs at `5855962d`/`00b18504`.
- Landed text: entry `corpus/knowledge/2026-10-28-r49-squashfs-v1v2-core.md`, PROVINCE Core row + frontier note, README rows, SOURCES S138/S139/S112 `used-by` + S147–S149 + search-log entries (rounds 48 late and 49), snapshots `corpus/evidence/round-49/c2/`, lesson `corpus/lessons/round-49.md`, QUALITY rows 88–89, SKILL decision-table row, SCORECARD round section + capability row, SHONEN note.
- **Round shape:** two v1 waves, 48 + 40 = **88 seats**, no residual call. Role mix wave 1: executor 10, reviewer 9, scout 9, scribe 6, critic 5, mutation-tester 4, connector 2, revenger 1, sentinel 1, simplifier 1 (attack roles 18/48); wave 2: reviewer 13, scout 9, critic 8, executor 6, mutation-tester 2, connector 1, sentinel 1 (23/40). **Dead seat:** `C2SourcesReopen` (wave 1) settled with a progress line and no report. The L1 held the planner seat (validator rejects `planner`); planning data-walks rode scouts/connectors/revenger. Results: `.ufo/waves/round-49/r49-w1-results.json`, `r49-w2-results.json`.
- Assimilation: none (`considerthese/` absent; `merge/kaidoku/` read-only scout found nothing in province, cheap and not held). Tool installs: none.
- Honest disclosures: wave-1 seats attacked draft bytes that the L1 amended before the freeze; REA ran on the carriers before the freeze (dev arm/POS fixtures); the C1 carriers are the round-44 fixtures (re-run under a restated predicate, **not new data**).

## Landed changes

| change | LOG entry | commit |
|---|---|---|
| wave-1 evidence, drafts, start census | LOG round-49 entry | `14936cb9df3897f89f8bc1eef3fe269f7d7df313` |
| FREEZE (plan, tools, control fixtures) | LOG round-49 entry | `decc5697bfd4ec1e9de4a762ad199d9bd9c4230d` |
| controls scored, FREEZE hash recorded | LOG round-49 entry | `76d7ad6f910c023a5fd56794db2f73948ce30574` |
| C1 data run | LOG "continued" | `4aabb0b4bf716fb564c8406509c40b0a67457800` |
| landing + S147/S148 form fixes + S145 restored byte-identical | LOG "continued" | `3847f3932885e6c8b8d09f1e982db42cda25f2ec`, `188ddeeafa21f9800497c102b8f144096b48d1cd`, `b58f9b192aba548b99d250bb896bbc42c654632c`, `29883d4ec35a31a8393c4ffb220888c44c0bb022` |
| wave-2 repairs, scorecard, log, quality rows | LOG "continued" | `5855962dd30e7a93dffdd1d25aaacc6072015ba3`, `00b185045b82af9398e7497d068a14ee3023fecb` |
| final scores and round-end census | — | `623476eef55640258fa5d4ff95a87ba59c49279f` |

## Before → after measurements

Environment: `GIT_NO_REPLACE_OBJECTS=1`, `HYAKU_SCRATCH=/fast/scratch/hyaku`, measured at `00b185045b82af9398e7497d068a14ee3023fecb`.

| claim | before (freeze) | after | counting command |
|---|---|---|---|
| R49-C1 coverage | exit 1, `carriers_matched 0`, six documentation bindings false (`.ufo/waves/round-49/controls/c0/`) | **exit 0**, `carriers_matched 4`, `failing []`, `bindings_false []`, `frozen_path_changed []` (`.ufo/waves/round-49/l1/scores/c1-final.json`, sha256 `d9e00d41…`) | `python3 -I -B tools/round-49/c1-counter.py --root . --rev 00b18504… --freeze decc5697… --pkg65 ~/.npm/_npx/ad9a3fdbcad992c6/node_modules/rea-agents --work <SCRATCH> --json-out <OUT>` |
| R49-C2 calibration | exit 1, `mismatches 9` (`controls/ctl-c2-0-do-nothing.json`) | **exit 0**, `atoms_total 9`, `mismatches 0`, `battery.failing []`, 16 mutations each red on its own atom, do-nothing red ×9 (`l1/scores/c2-final.json`, sha256 `544167f2…`) | `python3 -I -B tools/round-49/c2-mismatch.py --root . --rev 00b18504… --freeze decc5697… --battery` |

Controls (committed): CTL-C1-0..4 red, CTL-C1-POS exit 0 (`controls/summary.json`). Wave 2 independently reproduced both commands (`w2/W2C1Rescore.md`, `w2/W2C2Rescore.md`, `w2/W2CleanClone.md`).

**Limits and misses (frozen counters, reported and not patched):** the committed C1 receipt does not authenticate writer or round (a relabelled replay scores 4/4, disclosed in the plan); documentation bindings are presence checks; C1 freeze walk misses quoted-name and copy-status adds; C2 misses a second unmarked round-48 search-log entry, non-`is` second statuses for `EX_USAGE`, duplicate keys in one line, and its battery misses 13 of 30 wave-2 mutations; two P49-C2 plan sentences disagree with the code; the round-49 lesson's own freeze header is outside every atom. Full list: `corpus/lessons/round-49.md` `## Wave 2`. Wave-2 seats also found and I repaired: stale pointers, ~20 wrong sentences, session cookies in two wave-1 receipts (redacted at the tip, **history not purged**), 23 misrooted fixture files (relocated to `.ufo/waves/round-49/l1/misroot/`, `cmp`-verified, fleet copy removed).

## Sources & frontier

Census command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kaidoku`. Round start: **exit 0**, 15 W04 duplicate-URL lines, final `kaidoku ok …` (`l1/sources-census-start.txt`). Round end: **exit 0**, same 15 W04 lines, `kaidoku ok …` (`l1/sources-census-end.txt`). Rows `grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' corpus/SOURCES.md`: **146 → 149**. Added: S147 (SEP Popper, tier A as landed, mined, supersedes S145), S148 (man7 `sysexits.h.3head`, tier A, mined, supersedes S146), S149 (FreeBSD sysexits(3), tier C, rejected). Touched old→new: S138 and S139 `used-by` + r49 entry; S112 `used-by` + r49 entry; no status/recheck changes. Sourced claim: the C1 entry cites S112/S138/S139 (S138/S139 re-opened this round, `corpus/lessons/round-49.md` `## Gate`). Frontier advanced: SquashFS v1/v2 Frontier → Core (v1.0/v2.0 only); still Frontier: v2ns, v3 Broadcom/non-standard and DD-WRT no-pad, gzip v3, v4 Broadcom, v2.1, LE AVM, AVM kernels, nested sub-images. Mistakes mined M49-1…M49-5 (reference-drift, vacuous, stale-premise, landing/misroot, credential-class). Gate: ≥1 admit and ≥1 reject recorded; lane-seat disagreements (tiers of S147/S148, S149 provenance, S138 grounding) are recorded and the rows left append-only. `considerthese/`: absent. Assimilation: none. Cross-domain evidence: none (firmware ownership vs revenger remains the open tsukuroi ADJ-06 arbitration, reported not absorbed).

## Trend verdicts

- **expansion — improved:** one admitted entry moving SquashFS v1/v2 Frontier → Core on four fixtures, citing mined rows; capability row added. Bounded: same bytes as round 44, not new data.
- **quality — unchanged:** S145/S146 errors are superseded by S147/S148, but wave 2 found tier, locator and quote-cut defects in the new rows and ~20 wrong sentences (repaired), and counter misses are outstanding.
- **discernment — improved at decision level (unprovable-but-better beyond that):** admit/reject decisions stand under lane-seat review with recorded disagreements; the non-author spot-check is the closure's and is pending.

## SHONEN

[~] Decision-table depth: SKILL decision-table row added; v4 triage table untouched and known to mis-route v2ns (`w2/W2Skill.md`).
[~] End-to-end domain task: REA 6.5.0 `extract-firmware` re-run on four round-44 fixtures (`corpus/evidence/round-49/c1/`, `l1/scores/c1-final.json`); not new data.
[~] Executable instructions: both counters reproduced by a fresh-clone seat (`w2/W2CleanClone.md`); no non-author verifier.
[~] Province boundary: `PROVINCE.md` Round-49 row/frontier note appended, Adjacent unchanged.

**Stale-lane:** respawn-per-round driver; no other mission of this lane is open. **Tool installs:** none. **Misroot sweep:** 23 round-49 fixture files found at the fleet root (`tools/round-49/`), relocated byte-exact and deleted (M49-4); `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows no further kaidoku round-49 path. **Scratch:** `/fast/scratch/hyaku/kaidoku-r49` removed. **Open L0 questions:** none.
