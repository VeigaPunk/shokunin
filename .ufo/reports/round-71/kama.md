# kama round-71 report — one pre-report verdict, a waiver boundary that kills its shims, the province re-derived on this Linux host

lane: kama-shokunin (local model serving & endpoint health) · round 71 · date 2026-11-03
entering `f3ee44f47a9680437eeae63a8fa8807552a65119` · freeze `b43e71a8a5f22b8343e3bb95a012f65c027e540c` · measured lane commit `7fb6cb4e31dc2f96e4815240a12bfe8da4d07e2e` (branch `master`, pushed: `ls-remote` equals the local tip, ahead=0)
round shape: ONE v1 wave, 12 seats (band 8–16; attack share 5/12 = 42%). Driver digest: `2026-11-03T21:27:06-03:00 launch kama round=71 pgid=1551649 driver=hyaku-inline attempt=1`.

## Work performed

Declared claims (1–3, distinct axes; C1 works the lowest assigned non-retired axis, calibration 7):

- **C1 — calibration (capability `pre-report-gate`)**: one registered pre-report gate runs the four
  reconciled instruments plus a round-worktree cleanliness arm and emits a single verdict.
- **C2 — operability**: the census waiver boundary is a registered gate that kills the five round-70
  shims while keeping the landed 22-member census green.
- **C3 — freshness (capability `province-host-claims`)**: every `province-host:` marker and four prose
  claims in `PROVINCE.md` re-derived on this Linux host, with dated, verdict-checked corrections.

Work items, each with its evidence pointer:

- Frozen claims, controls and base receipts: `plans/round-71-claims.md`; the two control scripts
  `.ufo/waves/round-71/controls/{pre-report-shortcut.py,census-shim-control.py}`; base receipts
  `.ufo/waves/round-71/measured/before/{reconciler,newest-closure,receipt-audit,wlc,git-status,pre-report-shortcut,census-shim-control,province-claims}.out`
  (commit `b43e71a8`).
- C1 instrument: `tools/pre-report-gate.py` (five arms; `PRE_REPORT round=<N> arms=5 failed=<f> uncommitted=<u>`;
  exit 0 only when all arms are green). Selftest receipt `PRE_REPORT_SELFTEST pass=6 fail=0`
  (`.ufo/waves/round-71/w1/EX01PreReportGate/selftest.out`); defect fixtures: uncommitted wave file
  (`control-fixture.out` → `failed=1 uncommitted=26`, exit 1), stale closure pointer, missing/dirty/CRLF
  declared paths (six-arm selftest). The instrument runs at the report tip and its receipt is
  `.ufo/waves/round-71/measured/after/pre-report-at-tip.out`.
- C2 instrument: `tools/census-waiver-boundary.py` (seven cases over the census module in-process plus
  the real 22-member run; kills the five named shims by check). Selftest receipt
  `BOUNDARY_SELFTEST pass=8 fail=0`; the failed-waiver fixture exits nonzero; the five shims
  (`s4-refusal-as-fail`, `s5t-hardcoded-total`, `s6w-waiver-swallows-failure`, `s8r-second-call-silent`,
  `s10d-refusal-branch-deleted`) are each rejected with the check named
  (`.ufo/waves/round-71/w1/EX02CensusBoundary/` and `measured/after/boundary-at-tip.out`).
- C3 instrument: `tools/round71-province-host-claims.py` (parses the marker set, probes each surface and
  four declared prose claims, requires a later dated correction whose verdict equals the live probe, and
  prints `PROVINCE_HOST_CLAIMS_REWRITTEN` for a deleted marker). Selftest
  `PROVINCE_HOST_CLAIMS_SELFTEST pass=7 fail=0`; kill arms: flipped verdict leaves `uncovered=1`, wrong
  tag leaves 14, deleted marker exits 1 (`.ufo/waves/round-71/w1/EX03ProvinceClaims/kill*.out`).
  `PROVINCE.md` gains the dated host re-derivation block (12 tag corrections + 4 prose corrections).
- Source/frontier: S542 landed (Git `git-status` porcelain v1 script stability; live fetch 2026-11-03,
  retained bytes sha256 `22ff28ff…0180` at `.ufo/waves/round-71/w1/SCR02SourceRow/source/git-status.html`,
  scratch-mirror census gate exit 0 before the append); S052 re-opened and its `used-by` extended.
- Wave seats: EX01/EX02/EX03 built the three instruments; SCR01 wrote `corpus/knowledge/pre-report-gate.md`;
  SCR02 curated S542/S052; SCT01 independently re-derived all 16 host surfaces (14 contradicted);
  CON01 scanned sibling instruments and the five inherited defects; LAB01 probed the waiver semantics
  (H1/H2 refuted, H3/H4 confirmed); SEN01 audited the waiver/secret/scope boundary; RVW01/CRT01/MT01
  attacked the counters. Wave dispositions (all 12 reports landed; role mix 3 executor / 2 scribe / 1 scout / 1 connector /
1 reviewer / 1 critic / 1 mutation-tester / 1 sentinel / 1 revenger probe; attack share 5/12 = 42%):
EX01 built the gate (re-entry guard, 6-arm selftest) and the control/green fixtures; EX02 built the
boundary (7 cases, 19 selftest arms, byte-pinned embedded shims) and disclosed that case 7 was red at
`e2b860c8` only because the tip's record carried the two defects C1 fixes; EX03 built the province
counter and the corrections draft; SCR01 wrote the knowledge entry and found the recursion path that
removed the gate from the `## Axes` run facts; SCR02 landed S542 (scratch-mirror validated) and extended
S052's `used-by`; SCT01 independently re-derived 16 host surfaces (14 contradicted); CON01 mapped the
sibling overlaps and the five inherited defects; LAB01 confirmed H3/H4 and refuted H1/H2; SEN01 proved
no committed waiver, 0 secret-shaped hits and no scope/service breach; RVW01's four new sixth-shim
candidates are all killed by named checks on the final bytes (C2 HELD), with a version-skew note (v1
bytes let two survive); CRT01 found three C1 survivors (a wrong `--round` name is a vacuous green;
round work outside the wave dir and git-ignored files inside it are invisible) and several C3 gaps —
three of those are repaired in the landed tool (paragraph-identity `REWRITTEN`, calendar-date
validation, exit 2 on an unusable `--scratch`; receipts `measured/hardening/`), the C1 survivors stay
open and are routed to round 72; MT01 ran 19 mutants (C1 6/6 killed; C2 6/7 with `m7` surviving the
`waiver_keeps_not_evaluated` check; C3 5/6 with `m6` surviving the correction-date guard — both are
coverage findings routed to round 72, no predicate change). 0 dead seats: 12/12 seats settled (`w1/w1-results.json`, seats=12, results=12); no seat was replaced.
- Carry-in (round-70 closure §7): the 26 uncommitted round-70 files were committed at the freeze and are
  now graded by C1's fifth arm; the stale "final" receipt, the unreceipted `61f3ec42`→`380ac279` re-run
  and the scratch-tip receipts are corrected by the append-only block
  `corpus/lessons/round-70.md` §L1 corrections; the unregistered boundary control is replaced in kind by
  C2. Measured limitation: `git show --numstat --format= 61f3ec42 380ac279` changes only the dispatch
  marker and results file, which is the invariance the correction cites.

## Landed changes

Every change is tied to the round-71 LOG entry and to the commits that carry it:

| Change | LOG entry | Commit |
|---|---|---|
| Frozen claims, controls, base receipts; the 26 inherited round-70 files | §Round 71, carry-in paragraph | `b43e71a8` |
| `tools/pre-report-gate.py`, `tools/round71-province-host-claims.py`, `tools/census-waiver-boundary.py`; `SCORECARD.md`, `LOG.md`, `PROVINCE.md`, `SKILL.md`, `corpus/`, wave evidence | §Round 71, C1–C3 bullets | ``e2b860c8` (instruments first landed) + `64a2ebee` (wave evidence, hardened C3, lesson, record)` |
| Report-tip receipts (`measured/after/pre-report-at-tip.out`, `measured/after/boundary-at-tip.out`, `measured/after/province-claims-at-tip.out`) | §Round 71, receipts | `1375f51c` (seven green receipts at `4b284653`) + `9458c3d7` (final gate confirmation) + `7fb6cb4e` (lesson final-receipts block; no instrument input changed)` |
| `/home/vgpnk/Projects/shokunin/.ufo/reports/round-71/kama.md` | this report | `the fleet commit that carries this file` |

## Before → after measurements

Each claim's counting command, the before and after values, and the commit each was measured against:

- **C1** — `python3 tools/pre-report-gate.py --repo . --round 71 --tip master`.
  Before (base `f3ee44f4`): the tool is absent; the lane's current practice is the shortcut control on a
  fixture at the round-70 green tip carrying the 26 round-70 files — `SHORTCUT_CONTROL arms=4 failed=0
  uncommitted=26`, exit 0 (`measured/before/pre-report-shortcut.out`), i.e. every instrument green and the
  uncommitted class invisible. Every separate instrument at the round start also disagreed among
  themselves: reconciler `mismatches=1 met=False` and `STALE_CALIBRATION`, receipt audit `unresolved=0`,
  WLC `paths=5 clean=5`.
  After (`4b2846535fd918881ed3fc664aa46ef130a7d568`): `PRE_REPORT round=71 arms=5 failed=0 uncommitted=0`, exit 0, in
  `measured/after/pre-report-at-tip.out`. Kill receipts: `failed=1 uncommitted=26` exit 1 on the
  defect-carrying fixture; five-arm selftest `pass=6 fail=0`.
- **C2** — `python3 tools/census-waiver-boundary.py --census tools/round65-host-census.py`.
  Before (base `f3ee44f4`): the round-70 control accepts all five holes — `SHIM_CONTROL shims=5
  accepted=5 rejected=0` (`measured/before/census-shim-control.out`), and the boundary tool is absent.
  After (`4b2846535fd918881ed3fc664aa46ef130a7d568`): `BOUNDARY cases=7 killed=5 survivors=0`, exit 0
  (`measured/after/boundary-at-tip.out`), with the fail-waiver fixture nonzero and the real census
  `HOST_CENSUS pass=22 fail=0 not_evaluated=0 total=22`.
- **C3** — `python3 tools/round71-province-host-claims.py --repo . --base b43e71a8`.
  Before (base bytes): `PROVINCE_HOST_CLAIMS markers=11 tags=12 extra=4 contradicted=14 uncovered=14
  exit=1` (`measured/before/province-claims.out`). After (`4b2846535fd918881ed3fc664aa46ef130a7d568`): `contradicted=14 uncovered=0
  exit=0` (`measured/after/province-claims-at-tip.out`), with each correction's verdict equal to a live
  probe and a deleted marker still printing `REWRITTEN` (selftest `pass=7 fail=0`).

Population effects: gate-registry `registered 79 → 80` (`python3 tools/gate-registry-check.py --repo .`;
only `tools/round71-province-host-claims.py` matches the gate's declared population regex
`.ufo/waves/round-*/count-*.py | tools/round<N>-*.py`; the other two tools are documented SKILL rows
outside it — the freeze's `79 → 82` expectation was wrong, lesson Mistake 1),
capability rows `15 → 17`, SOURCES rows `281 → 282`, knowledge entries `39 → 40`, uncommitted round-70
files `26 → 0` at the freeze. No production endpoint, consumer config or service was touched; the
registered consumers keep their last recorded `DEAD` state.

## Sources & frontier

- Registry census before → after: `281 → 282` rows. Counting command:
  `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` (`f3ee44f4` → 281; `4b284653` → 282).
- Contract-v1 census: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kama`
  → **exit 0 at round start** (281 rows) and **exit 0 at round end** (282 rows; the transient E11 for the
  two sibling deliverables cleared when the knowledge entry and lesson landed). Warnings unchanged
  (104 W04 + 1 W01); no E codes.
- Rows added by tier: **1 tier A, 0 tier B, 0 tier C** (S542, Git `git-status` §"Porcelain Format
  Version 1"; quote, access date 2026-11-03 and retained-bytes sha256 `22ff28ff…0180` in
  `corpus/lessons/round-71.md` §Gate). Rows touched old→new: S052 `used-by` gained
  `corpus/lessons/round-71.md` (no other cell changed; duplicate URL means no second row).
- Id collision check before any append: lane ids 281, staged `merge/kama/SOURCES.append.md` ids 142,
  collision set **9** (S330, S333, S334, S335, S346, S347, S352, S353, S363), union max S541, next unused
  S542; full lists and counts in `.ufo/waves/round-71/w1/SCR02SourceRow/receipts/`.
- Frontier advanced: the report-time cleanliness class (S542) and the lane's own waiver boundary enter the
  held repertoire as two capabilities (`pre-report-gate`, `province-host-claims`); the cross-lane overlap
  rules for pre-report gates, waiver policy, host-surface reconcilers and receipt-tip binding are now
  recorded in `corpus/knowledge/cross-lane-scope.md` (§"Overlap rules — round 71").
- **Assimilation: none** — `merge/kama/` exists (65 proposed entries, 142 rows) but no entry was
  re-grounded under CORPUS rule 1 this round; its 9-id collision set with the live registry is recorded
  in the lesson Gate, so nothing was bulk-appended.

## Trend verdicts

- **expansion — improved**: two capability rows entered (`pre-report-gate`, `province-host-claims`), each
  demonstrated running (defect fixtures killed; green receipts at the tip), and one new tier-A source row
  (S542) entered the registry. The knowledge count grew 39 → 40 on ground the coverage map did not hold
  (the pre-report cleanliness arm).
- **quality — improved**: three instruments now do what their rows claim (the reconciled set runs as one
  gate, the census boundary kills the five shims the round-70 control accepted, the province markers are
  probed rather than trusted); the round-70 closure's defects 2/3/5 were corrected by append with the
  invariance diff named, and the round-71 selftests are red on defect fixtures and green at the tip. No
  admitted entry was found false or stale and left unmarked.
- **discernment — improved / pending outside check**: the round's own gate samples use recorded
  rejections (flipped verdict, wrong tag, deleted marker, five shims) and the shortcut control for each
  counter; the non-author closure has not yet ruled on this round. No `[x]` is claimed.

Axes: operability 8, freshness 8, depth 7, coverage 9, calibration 7, adjacency 7 — held; no axis harmed.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — pointer: `SKILL.md` §§Decision table / Error signatures / Checklist (lane tip `7fb6cb4e31dc2f96e4815240a12bfe8da4d07e2e`); the round-71 registry rows add the three new instruments. No named non-author verifier.
- [~] At least one end-to-end domain task executed and logged in LOG.md — pointer: `LOG.md` §Round 71 (three instruments built, run, defect-fixtured and green at the tip) plus the lane-owned live fixture receipts `.ufo/waves/round-16/live/receipt.json` (historical). No promotion mark claimed.
- [~] Instructions executable by an agent without oral context — pointer: `SKILL.md` §Checklist and `corpus/knowledge/pre-report-gate.md` (exact CLI, output contract, decision table, limits); independent execution review remains open.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — pointer: `PROVINCE.md` §Write boundary + §Host re-derivation — round 71 and `corpus/knowledge/cross-lane-scope.md` §Overlap rules — round 71; routing and credentials stay sibling/operator-owned. No cross-domain absorption this round.

## L0, stale-lane, tooling

- L0: the kama round-65 NTFS-path question stays unanswered; routed around (this Linux host checks the
  `|`-path out). No new L0 question filed.
- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
- Tool installs/upgrades this round: none (curl, coreutils, python3, git and jj present; no package
  command run). pacman stayed paused per the addendum guard.
