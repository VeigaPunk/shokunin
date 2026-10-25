# mado round 27 — workspace-rule table tool; offline gates that fail red (attempt 2)

Lane: mado-shokunin. Base `543f0445e9d60bdfa026c54772d29e8b96bc844b` (r26 admitted). Attempt 1 (phase-4
orchestrator death ~09:30 -03) committed the frozen rulebook, 13 scored C1 controls, sealed held-out H, both
C2 suites and C2-control rescoring, then died before C1 data or any measurement (`lane-dead-no-report mado
round=27`, fleet `.ufo/watchdog.log:931`). Attempt 2 inherited that state, re-verified it (w3 RevProvenance:
PROVENANCE_OK — counter sha256s match `registration.md` pins, seal matches H bytes, suites three-way
byte-equal to their data seats' candidates), and finished the round. Rulebook:
`.ufo/waves/round-27/registration.md` (C1 counter chain v1→v4 and C2 counter v2, each redesign before any
data seat under the kill rule).

Lane tip at report time: `767b12db62ceb3ad38d24a13e4c693b4375ceb5a` (pushed, ahead=0; C1 measured at
`20022a652d201af52c899c4492a7f71be0136b80`, C2 at `0b53bd861104cb8319c698ce622d1b81d3fc66e9`).

## Work performed

Declared claims (2): **C1 — coverage** (sourced): the Hyprland workspace-rule plane (`hyprctl
workspacerules -j`) derived offline from config bytes by a new lane tool, measured against Hyprland v0.56.2
itself through the isolated oracle. **C2 — operability**: the lane's two offline gates
(`quality/counter-selftest.py`, `quality/population-suite.py`) fail when their round-26 subjects are broken
(15 W mutants + sealed held-out H), under the frozen counter `c2/count-v2.py`.

- C1 data rule executed: ExecWsToolA (attempt 1) died mid-flight, unreturned — its inherited bytes landed
  byte-exact at `48b9434a` and were piloted: 19/41, all 22 failures carrying ONEMPTY (its `on-created-empty`
  value slice keeps a leading colon; w3 MutWsTool and CritC1Claim independently located it). ExecWsToolC
  returned an independent implementation (dev: 41/41 on four seeds, BYTE_IDENTICAL raw capture vs Hyprland,
  73/74 on its own 74-case differential, 0 new-class fuzz diffs over 1500 trees); its bytes landed unmodified
  at `20022a65` (data-rule order is return order, not file existence — lesson M27-1).
- C1 official measurement: `PRED-C1-r27-v4 cases_pass=41/41 verdict=TARGET_MET`, exit 0, seed
  `4cfdf858277ad362`, `HOST_SAFETY hyprland_coredumps 1338→1338 delta=0`
  (`.ufo/waves/round-27/evidence/c1-after-20022a65.txt`, measured commit `20022a652d201af52c899c4492a7f71be0136b80`).
- C1 attacks: 13 v4 control shapes re-scored by w2 seats, two-seed receipts (`controls/v4/`, best 32/41
  FileScope); w3 MutWsTool killed 3/3 tool-level mutants on the 13-tree oracle probes (merge-order, gaps
  faces, exact-word bools); w3 CritC1Claim confirmed predicate identity across registration/counter/receipt
  and recorded residual risks (live-HOME snapshot dependency — receipt records the snapshot digest; ExactBool
  blind spot — routed).
- C2 measurement 1 at `48b9434a`: green=17/17, w_killed=15/15, h_killed=12/18 vs h_need=14 —
  `TARGET_MISSED` on three named suite-A survivors of the r26 bind counter (extra-disjunction,
  unstable-conjunction, embed-boundary; receipt `evidence/c2-after-48b9434a.txt`). Registration repair flow
  invoked: w4 repair seats built class mutants from the public names only (sealed H never read — w4 RevRepair
  verified), repaired suite A; first-returned candidate landed unmodified; measurement 2 and final verdict:
  see **Before → after measurements** and SCORECARD.
- Suite B independently confirmed post-measurement (w4 MutSuiteB: 3 fresh checker-class mutants killed,
  46/46 greens, sealed dir never opened).
- Corpus: S178–S182 admitted with located quotes (5 sources: wiki workspace rules, WorkspaceRuleManager,
  CCssGapData, ParserUtils, workspace command normalizer) + S158/S162 used-by extensions; knowledge entry
  `corpus/knowledge/workspace-rules-r27.md` (measurement-status section supersedes the static [INF] schema
  limits); lesson `corpus/lessons/round-27.md` (M27-1 process-loss / return-order rule, M27-2 registry-schema
  E01 — gate quotes live in the lesson `## Gate`, not SOURCES.md — M27-3 premature saturation v1→v4).
- Spotcheck debt (r26 §7) closed: M26-10 PROVINCE+binds docstring (`b6650d5`), SKILL.md registry rows (6
  rows), population-evidence citation in SCORECARD with `evidence/r26-population-after.txt` + the
  hidden-dependency probe, Q36 successor landed (`quality/q36-successor-receipts.txt`; two survivors routed),
  host-safety terms on every receipt.

## Landed changes

- `tools/mado-wsrules.py` — `48b9434a` (A bytes, pilot evidence), replaced by `20022a65` (C bytes, official).
- `quality/counter-selftest.py`, `quality/population-suite.py` — `5c1d495` (data seats A1/B2); suite A
  repaired by ExecRepairA2's first-returned bytes (own 12 class mutants killed, green 8/8, W 15/15 under the
  frozen counter) at `0b53bd86`.
- `corpus/SOURCES.md`, `corpus/knowledge/workspace-rules-r27.md`, `corpus/lessons/round-27.md`, `SKILL.md`
  (registry rows), `SCORECARD.md` (r27 section + r26 citation fix), `LOG.md` — `86f7355b`, `0be82d62`,
  `43fdd7e6`, `cb7c38f0` (LOG).
- Wave evidence: `.ufo/waves/round-27/{w1,w2,w3}` reports and run registries committed (`98ebd5b0`).

## Before → after measurements

- C1: before `543f0445`: `tool=MISSING_TOOL`, 0/41 (`evidence/c1v4-before-543f0445.txt`, counter v4
  sha256 `635ae788…71a1`). After `20022a65`: `python3 -I .ufo/waves/round-27/c1/count-v4.py
  20022a652d201af52c899c4492a7f71be0136b80 --seed 4cfdf858277ad362 --jobs 6` → `cases_pass=41/41
  verdict=TARGET_MET`, exit 0. Command that shows it unmoved: the same counter at any REV whose
  `tools/mado-wsrules.py` prints anything but Hyprland's table (the 13 controls' receipts are the demonstrated
  misses).
- C2: before `543f0445`: suites missing, `green=0/8 w_killed=0/15` (`evidence/c2v2-before-543f0445.txt`).
  After: `python3 -I .ufo/waves/round-27/c2/count-v2.py REV --heldout /fast/scratch/hyaku/mado-r27/heldout
  --seal .ufo/waves/round-27/c2/heldout-seal.txt`. Measurement 1 at `48b9434a` (unrepaired suites):
  `green=17/17 w_killed=15/15 h_killed=12/18 h_need=14 verdict=TARGET_MISSED`, exit 1. Measurement 2 at
  `0b53bd86` (repaired suite A, REV-parametric predicate): `green=17/17 w_killed=15/15 h_killed=15/18
  h_need=14 h_valid=18 invalid=0 verdict=TARGET_MET`, exit 0 (`evidence/c2-after-0b53bd86.txt`). The
  command that shows it unmoved: the same counter at a REV whose suites green-pass a broken subject (the
  measurement-1 receipt is the demonstrated near-miss).

## Sources & frontier

Census (spec command `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root
/home/vgpnk/Projects/shokunin mado`): start exit 1 (E01 fields=2 on S178–S182 gate-quote rows pasted into
SOURCES.md + E11 dangling used-by for the not-yet-landed note/tool — inherited from attempt 1); end exit 0
(w3 RevSourcesFinal independently re-ran: 177 → 182 rows, W04 duplicate-url warnings unchanged from r26).
Rows added: tier A +5 (S178 wiki, S179 manager, S180 gaps parser, S181 int parser, S182 command normalizer).
Rows touched old→new: S158 and S162 used-by + `corpus/knowledge/workspace-rules-r27.md` (logged in the
lesson). Frontier rows advanced: none (all five `mined` on admission). Gate quotes for the five new rows are
in `corpus/lessons/round-27.md ## Gate` (≤25 words, verbatim, per the E01 fix). Sourced claim: C1 rests on
S178–S182 (opened this round) plus S158/S162; the tool's docstring and the knowledge entry cite them.

## Trend verdicts

- expansion — **improved**: new measured surface (workspace-rule table) with a running tool + 5 new A-tier
  source rows; evidence: C1 41/41 receipt, SOURCES 177→182.
- quality — **improved**: two offline gates that now fail red on 15/15 W mutants (and, after repair, the
  sealed-H conjunction — see C2 final verdict); registry rows make them discoverable; evidence:
  `evidence/c2-after-*.txt`, SKILL.md gates table.
- discernment — **improved**: three pre-data counter redesigns under the kill rule (v1/v2/v3 each met by a
  partial reader before data, each retired with receipts kept), the unreturned-candidate return-order ruling
  (M27-1), and the E01 registry-schema fix; evidence: `registration.md` redesign chain, lesson M27-1/M27-3.

## SHONEN

- [~] SKILL.md decision tables/cited sources — six gate registry rows landed (r26+r27, `SKILL.md:631-636`);
  outside-lane verifier independence still not established (inherited note).
- [~] End-to-end domain task logged — C1's tool reproduces the live surface offline; a live `hyprctl
  workspacerules -j` comparison is closure-re-derivable, not lane-run this round.
- [~] Executable instructions — the wave prompts and registration carried full contracts; dispatched
  subagents did the execution (inherited outside-lane promotion bar unchanged).
- [~] No cross-domain bleed — PROVINCE round-27 correction append-only (`b6650d5`, M26-10); untouched this
  attempt otherwise.

Stale-lane: respawn-per-round driver; no other mission open. Tool installs: none (no seat installed tools;
pacman paused throughout). L0: none.

Round shape: attempt 1 — w1 build 39 seats + w2 data/falsify 36 seats (both v1 policy, committed); attempt 2 —
w3 residual 8 seats (in-tree) + w4 repair 4 seats (dispatched by orchestrator per operator directive); round
total 87 seats. Dead seats: ExecWsToolB (attempt 1, orchestrator death — no report, no bytes; last error
text: none recorded, process loss). Planner seat: L1 (validator rejects planner as a swarm role; bounded
data-walks rode scouts/reviewers per the orchestrator ruling). Wave-slot grants: w3 `granted lane=mado wave=w3
seats=8`, w4 `granted lane=mado wave=w4 seats=4`. Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status
--porcelain` — no mado round-27 files at the fleet root (checked each stray's content; none names mado/r27).
