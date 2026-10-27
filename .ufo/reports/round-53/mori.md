# mori — round 53 report (attempt 2, L1 MoriR53a2; attempt 1 L1 MoriR53)

Lane `mori-shokunin`, branch `master`. Entering tip `20edafa59b38dac1ca358893f0259b1f436372d3`; freeze
`f4da3fd400fa88a6db8ea544a4f7045c15d2410e`; data `2a4213bf8da72f7cd78189baa5bb9be825dca1df`; wave spec
`95cf78eef71979f9b740ef6bc3c5299b6beff86e`; post-wave data corrections `fd86307ad54c13edb8b6dd13182a2ad196f42fcd`;
orchestrator salvage `0df803033fba2386b10f5dcc6aa96bdef65cba15`; measured revision (final integration tip)
`0b36d23e596276c70725873621fe15a28c87189f`; final lane tip `28401324ca5e0205645490d8e538b30d5ef4d1bf` (receipts commit;
`git -C mori-shokunin ls-remote origin refs/heads/master` prints it). This report's own commit is named by command, never by
placeholder (QUALITY 147): `git log --format=%H -1 -- .ufo/reports/round-53/mori.md` on the fleet repo.

## Work performed

Declared claims (frozen at `f4da3fd4`, `.ufo/waves/round-53/contract.md`), two, no exploratory claim:
**C1 — freshness** (a lowest axis, tied at 5): the 46 v7.2-pinned located-quote claim rows of
`memavailable-estimate-r51.md` and `overcommit-commit-limit-r52.md` (`recheck: on-release`) re-verified at Linux
v7.3, tagged 2026-10-18 — ledger `corpus/knowledge/kernel-v7.3-recheck-r53.md`, rows S502–S510, two-voter RECHECK
arm. **C2 — coverage, with a capability row**: the commit ledger (`CommitLimit`/`Committed_AS`) as a runway surface
read by the new read-only `tools/mori-commit-runway.py`, by overcommit mode and, under mode 2, against the per-CPU
error band — fixtures, `--selftest`, SKILL registry row, entry `corpus/knowledge/commit-runway-read-r53.md`
(S511–S514).

- Attempt 1 (MoriR53, all landed and pushed before it died): census start rc 0, 23 W04
  (`.ufo/waves/round-53/evidence/census-start.txt`); freeze `f4da3fd4` with both counters and selftests
  (`C1_SELFTEST pass=37 fail=0`, `C2_SELFTEST pass=30 fail=0`), ten control receipts, sweeps, twelve source copies,
  `freeze-sha256.txt`; data `2a4213bf` (`evidence/c1-at-data.txt`: `C1=unmet … voted=0 … failed=votes`;
  `evidence/c2-at-data.txt`: `C2=met … n=23 … agree=80`); wave `w1` (67 seats, v2, validated) spec `95cf78ee`;
  post-wave corrections `fd86307a` (tool bounded reads, strict parsing, case-id guard, +3 cases, 5 hostile
  checks; two-sided band reading; CPU-hotplug limit; S514).
- Attempt 1 died at 2026-10-26 23:57:36 -03 (orchestrator session exit, SIGHUP during an operator `omp update`; not a
  lane defect). The orchestrator committed its uncommitted tree as salvage `0df80303` (81 files: 66 w1 seat reports,
  `w1-results.json`, LOG/PROVINCE/SHONEN/QUALITY/README/SOURCES drafts, ledger prose, the lesson).
- Attempt 2 re-verified the salvage before citing it (`corpus/lessons/round-53.md` `## Attempt 2`): freeze
  `sha256sum -c` rc 0; `C1=met … voted=46 dissent=0` and `C2=met … n=31 … agree=80` at `0df80303`
  (`evidence/c1-at-salvage.txt`, `evidence/c2-at-salvage.txt`); the 46 voted ledger rows byte-unchanged since
  `2a4213bf`. **Reused:** every salvaged file (the 66 settled w1 reports and their outputs in `w1-results.json`, all
  drafts), after the residual call below attacked the drafts no w1 seat had seen. **Discarded:** nothing wholesale;
  corrected in place: LOG's dangling `c1-at-landed`/`c2-at-landed`/`census-end` pointers, the band entry's
  overclaims, PROVINCE's fault-attribution sentence, SHONEN pointers, the lesson M2 probe wording, two ledger
  change-table cells (commits `7b90a3c6`, `0b36d23e`).
- SCORECARD (`34d97cd3`): the round-52 closure's routed defect 1 — an appended `**Round-52 correction:**` naming the
  superseded `items=42 … locators=27` and the receipt's `items=43 … locators=28` (`SCORECARD.md:2773`); the
  `## Round 53` section with claim rows whose numbers are those of the receipts their cells cite, the capability
  row `round-53 C2`, limits and `Planned (round 54)` (`SCORECARD.md:2783-2848`).
- Residual call `a2r1` (8 seats, `.ufo/waves/round-53/a2r1/`, `a2r1-results.json`): re-dispatched the dead w1
  item (ledger prose) and attacked the salvage. Integrated: `Mo53a2CritBandEntry` (3 MED, 2 LOW — checked against
  `percpu_counter.c.v7.2:258-283`: a dying CPU recomputes the generic `percpu_counter_batch`, not
  `vm_committed_as_batch`; boot-time computation `mm_init.c.v7.2:226-233`), `Mo53a2CritDrafts` (2 HIGH dangling
  receipts, 1 MED PROVINCE), `Mo53a2RevLedgerProse` (2 LOW, checked by `diff` of the copies), `Mo53a2RevQuality`
  (1 LOW). No-change verdicts: `Mo53a2RevToolPostWave`, `Mo53a2RevScorecard`, `Mo53a2CritNoHarm`,
  `Mo53a2RevSourcesAnchors` (anchor resolution left UNVERIFIED — named limit).
- No-harm checks by the L1: `python3 tools/mori-pin-check.py --rev R` → `PIN_CHECK=met tally_pins=36 … mismatches=0`
  at `20edafa5`, `tally_pins=37 … mismatches=0` at `0b36d23e` (`evidence/pin-check-at-landed.txt`); census end rc 0,
  23 W04 (`evidence/census-end.txt`); `mori-commit-runway.py --selftest` `PASS 31/31`
  (`evidence/selftests/mori-commit-runway-a2.txt`).
- Planner seat: held by the L1 (the validator rejects `planner`).
- Round-52 report erratum: its own commit, left as `[FILL]` (`.ufo/reports/round-52/mori.md:5`, `:46`), is
  `aacd7a83027cdee8e950a2c39d490feaed3be13c` (`git log --format=%H -1 -- .ufo/reports/round-52/mori.md`).

## Landed changes

| commit | what | LOG.md |
|---|---|---|
| `f4da3fd4` | freeze: contract, counters, controls, receipts, census-start, sweeps, source copies | Round 53 header (`LOG.md:2841`) |
| `2a4213bf` | data: v7.3 ledger, S502–S513, tool + fixtures + SKILL Round53, band entry | Round 53 C1/C2 |
| `95cf78ee` | wave w1 spec (67, v2 validated), dispatch, at-data receipts | Round 53 header |
| `fd86307a` | post-wave data corrections (tool hardening, band two-sided, S514) | Round 53 "Wave corrections" |
| `0df80303` | orchestrator salvage of attempt-1 drafts and w1 state (re-verified by attempt 2) | Round 53 attempt-2 note (`LOG.md:2880`) |
| `34d97cd3` | SCORECARD round-52 correction + round-53 section; lesson M6, attempt-2 section; at-salvage receipts | attempt-2 note |
| `7b90a3c6` | a2r1 dispatch + 7 reports; band entry/SKILL/PROVINCE/LOG/SHONEN/lesson corrections | attempt-2 note |
| `0b36d23e` | a2r1 settled (ledger prose report, results); ledger change-table cells; lesson a2r1 findings | attempt-2 note |
| `28401324` | receipts at `0b36d23e`: c1/c2-at-landed, census-end, pin-check-at-landed, runway selftest | attempt-2 note |

## Before → after measurements

- **C1** — `python3 .ufo/waves/round-53/count-c1.py R`.
  - Before (`20edafa5`): `C1=unmet scope=46 rows=0 matched=0 status_ok=0 quote_ok=0 source_rows=bad pins=bad
    provenance=bad held=0 absent=0 holds=0 changed=0 voted=0 dissent=0 … failed=ledger_absent,pins`, exit 1
    (`evidence/control-c1-do-nothing.txt`).
  - After (`0b36d23e`): `C1=met scope=46 rows=46 matched=46 status_ok=46 quote_ok=46 source_rows=ok pins=ok
    provenance=ok held=44 absent=2 holds=46 changed=0 voted=46 dissent=0`, exit 0 (`evidence/c1-at-landed.txt`).
  - Controls (pre-data): all-held, v72-copies, no-votes unmet; witness met (feasibility, disclosed).
- **C2** — `python3 .ufo/waves/round-53/count-c2.py R --scratch DIR`.
  - Before (`20edafa5`): `C2=unmet tool=absent selftest=error n=0 fixtures=80 agree=0 disagree=0 registry=bad
    live=error failed=registry,tool_absent`, exit 1 (`evidence/control-c2-do-nothing.txt`).
  - After (`0b36d23e`): `C2=met tool=present selftest=pass n=31 fixtures=80 agree=80 disagree=0 registry=ok
    live=ok`, exit 0 (`evidence/c2-at-landed.txt`).
  - Controls: mode-blind (`agree=53`), no-band (71), memoriser (71) unmet; witness met (disclosed).
- Named limits (contract + wave): `held` proves words still occur, not same place or meaning (votes carry the
  meaning; votes are lane seats); C1 voter identity is the report filename; C2's REF and the tool share one author
  (two independent oracles agreed); C2's exit-code arm has no selftest; this host is mode 0, so the mode-2 band has
  no live leg; S502–S514 anchor corrections rest on one seat's check. All routed to `Planned (round 54)`.

## Sources & frontier

- Census `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin mori`: start rc 0, 23 W04
  (`evidence/census-start.txt`); end rc 0, 23 W04 (`evidence/census-end.txt`). Registry rows
  (`grep -cE '^ {0,3}\| *S[0-9]{3,} ' corpus/SOURCES.md`): 274 at `20edafa5` → 287 at `28401324`.
- Rows added: 13, all tier A (S502–S510 v7.3 docs/code, S511–S513 v7.2 band sources, S514 `mm_init.c` v7.3), opened
  2026-10-26, Gate quotes in `corpus/lessons/round-53.md` `## Gate`. Rejected (rows-as-decisions in the Gate):
  raw.githubusercontent.com v7.3 locator (HTTP 429), rendered `latest` docs.
- Rows touched old→new: S499 `used-by` + `commit-runway-read-r53.md`; in-round anchor/teaches corrections to S502,
  S503, S504, S505, S507, S508, S511, S512 (lesson Gate, `### Rows touched old→new`).
- Frontier: the commit ledger moves from knowledge (round 52) into a tool (README `## Round-53 coverage additions`);
  FR8 stays open (no calibrated threshold); lead added: v7.3 `panic_on_unrecoverable_memory_failure`
  (`SOURCES.md` `## Leads (unopened)`).
- Sourced claims: C1 rests on S502–S510, C2 on S511–S514.
- Mistakes mined (lesson `## Mistakes`): M1 SCORECARD row numbers from the wrong receipt; M2 `[FILL]` self-citation;
  M3 the v7.3 trigger unanswered eight days; M4 two lane-tree writes by w1 seats; M5 one-sided band reading; M6
  integration drafts left uncommitted until the session died.
- Assimilation: none — `merge/mori/` holds 0 files on either claim's ground (`evidence/sweeps.txt`).
- considerthese: `considerthese/2026-10-26.md` suggestion 2 — the round-52 wave's 61 distinct HIGH/MED flags
  followed forward: 13 fixed, 18 routed, 30 dropped (`w1/Mo53ExecConsiderthese.md`; lesson section).

## Trend verdicts

- **expansion: improved.** A tool on commit-ledger runway ground no mori tool read (sweep: 0 hits in `tools/` at
  `20edafa5`), a capability row, 13 tier-A rows.
- **quality: improved.** 46 release-pinned rows re-read at v7.3 with pinned copies fetched by two independent
  channels; the band entry tightened after two attack passes; tool hardened against 5 hostile-input classes.
- **discernment: unprovable-but-better** pending the non-author closure: the round-52 closure's D1/D2 turned into
  QUALITY 146/147 and an appended correction; two locators rejected with flip conditions; the salvage was attacked
  before reuse. Admit/reject candidates for spot-check: admit S510, reject the raw v7.3 locator.

## SHONEN

- [~] SKILL.md decision tables, error patterns, checklists, cited sources — `SKILL.md:1178` (Round53); `corpus/QUALITY.md:1383-1477`
- [~] an end-to-end domain task executed and logged — `LOG.md:2841-2888`; `.ufo/waves/round-53/evidence/c2-at-landed.txt`
- [~] instructions executable without oral context — `python3 -I -B tools/mori-commit-runway.py --selftest` (31/31, `evidence/selftests/mori-commit-runway-a2.txt`); `evidence/pin-check-at-landed.txt` (37 pins, 0 mismatches)
- [~] no cross-domain bleed — `PROVINCE.md:451-456`; `corpus/knowledge/commit-runway-read-r53.md:54` Boundaries

## Extras and defects

- Round shape: one v2 wave `w1` (attempt 1) of 67 seats — reviewer 12, critic 12, executor 20, mutation-tester 3,
  sentinel 4, scout 2, connector 2, scribe 10, revenger 1, simplifier 1 (attack 27/67); 66 settled, 1 dead
  (`Mo53RevLedgerProse`, killed in the session exit with no output and no report). Attempt 2: one residual call
  `a2r1` of 8 seats (reviewer 5, critic 3), 0 dead. Round total 75 (64–128 band). Reused from attempt 1: 66 seats;
  re-dispatched: 1 item (as `Mo53a2RevLedgerProse`).
- Misroot sweep (`git -C /home/vgpnk/Projects/shokunin status --porcelain`): only `.ufo/reports/round-45/kengaku.md` and
  `.ufo/reports/round-48/mado.md` (other lanes; untouched); no mori misroot. Scratch `/fast/scratch/hyaku/mori-r53`
  removed.
- Inherited, not authored this round and left untouched: tracked lane-root files `0`, `base.c`, `main.c`,
  `meminfo.c`, `oom_kill.c`, `sd-main.c`, `user@.service.in` (from 2026-10-22/23) and the empty `--repo/` dir.
- Round-52 closure routed defects: 1 → SCORECARD correction; 2 → report commit by command + erratum above; 3 →
  `Planned (round 54)`.
- Stale-lane: respawn-per-round driver; no other mori mission is open.
- Tool installs: none. Open L0 questions: none.
