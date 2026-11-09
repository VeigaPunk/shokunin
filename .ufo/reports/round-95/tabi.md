# tabi — round 95 report (L1 `TabiR95`, attempt 1)

Lane `/home/vgpnk/Projects/shokunin/tabi-shokunin`, branch `master`. Base `7b3912bb`, final lane hash
`333006bdeedec6aec60c26dc067346e192025502` (`git ls-remote origin refs/heads/master` prints it).
Inherited state: none (no `lane-dead-no-report tabi round=95` line; lane clean at start). The r94
spot-check routed items are addressed in `plans/round-95.md` §Record work.

## Work performed

Declared claim (ONE): **C1 — coverage, capability acquisition `chromium-oopif-backendnode-misdelivery-linux`**
(predicate `C1-BACKENDNODE-MISDELIVERY-R95`, sourced S235). A cross-site iframe chooser's `backendNodeId`
B sent on the PAGE session acts on exactly the node the parent renderer holds at id B. If that node is
one of the parent's own file inputs, `DOM.setFileInputFiles` returns no error and fills the PARENT's
input while the child's input stays empty. Otherwise the call fails with `Node is not a file input
element` (any other node) or `No node found for given backend id` (no node).

- Pre-freeze probes: a parent `#p` input at id 302 was filled by the page-session answer (6/6 runs); file
  inputs sit 4 ids apart with ±1 jitter. Evidence: `.ufo/waves/round-95/probes/` (freeze commit `1ecbca38`).
- Instruments: driver `scripts/chrome-cdp-backendnode-misdelivery-round95.mjs` (sha `24947b00d8a1…`),
  counter `scripts/check-backendnode-misdelivery-round95.mjs` (`b7b464daa7c3…`), battery
  `scripts/negatives-backendnode-misdelivery-round95.mjs` (`1a670da5a9ff…`, 77 cases). These include the
  r94 R94Sentinel F1-F4 hardening: nonce passed via the environment, a `mkdtemp` receipt path, launch
  failure → `setup`, `driverRun` included in signal setup output, and a non-file receipt path → `setup`.
- Controls ran before the freeze and were committed with it in `1ecbca38`
  (`.ufo/waves/round-95/controls/rc.txt`): no-work base rc 128; the r94 receipt rc 1; the no-reach control
  rc 1; wrong-site rc 1; positive rc 0 (336 checks); battery 77/77; five setup controls each rc 2 with 0
  chromium left.
- Freeze `1ecbca38` (`claims.json.frozenAt` 22:59:07, before the commit at 22:59:12). Scored `--live` run
  in commit `360d7cc9`: rc 0, clean, 336 checks.
- Wave w1: 12 seats, dispatched 23:02:12, all 12 filed (`.ufo/waves/round-95/w1-results.json`). Six
  further `--live` runs of the pinned driver were all clean.
- Post-wave amendment A1 (`plans/round-95.md`, items 1-6). R95Critic1 and R95Sentinel each returned
  `falsifies-wording`, and A1 narrows the wording to what the instrument actually enforces:
  - some clauses are enforced only by the driver bytes;
  - the receipt-mode binding gaps are named;
  - limit 6 now extends to `--live` when a same-UID process writes the receipt.

  The counter bytes and every number are unchanged. Evidence: lane commit `c67d6a44`.
- Records (commit `c67d6a44`):
  - knowledge note `corpus/knowledge/chromium-oopif-backendnode-misdelivery-round-95.md`;
  - S235 plus a search-log entry;
  - SKILL `## Round 95 gate registry`;
  - README `## Round 95 coverage`;
  - appended corrections to the r92, r93 and r94 notes and to the README r93/r94 summaries (from R95Connector);
  - lesson `corpus/lessons/round-95.md`;
  - SCORECARD round-95 section and capability row;
  - LOG round-95 entry.
- Tip run (commit `9a778917`; measured revision `c67d6a44`): `--live` rc 0, clean, 336 checks, nonce
  `tabi-r95-live-d0b7f38899e0`, receipt committed as `scored/live-receipt-tip.json` (sha `02b5c838…`).
  The freeze-stamp and log-section-claims gates were both clean at the tip.
- Mined gate `scripts/check-scored-receipts-round95.mjs` (r94 D2): round 94 → rc 1, round 95 tip → rc 0
  (`scored/scored-receipts-tip.json`, commit `16f8cf5c`).

Round shape: ONE v1 wave `w1` of 12 seats.

| Role | Seats |
|---|---|
| executor | 3 |
| critic | 3 |
| mutation-tester | 1 |
| reviewer | 1 |
| sentinel | 1 |
| scout | 1 |
| scribe | 1 |
| connector | 1 |

- Attack share (reviewer + critic + mutation-tester): 5/12 = 42 %.
- No residual call. Round total 12. Dead seats 0.
- The L1 held the canonical planner seat. Validator policy v1 (band 8-16).

## Landed changes

| Commit | Content | LOG.md entry |
|---|---|---|
| `1ecbca38` | freeze: plan, claims.json, instruments, controls, probes, staged S235 | LOG `## Round 95` |
| `360d7cc9` | scored `--live` run + committed receipt `corpus/evidence/round95/…/receipt.json` | LOG `## Round 95` |
| `c67d6a44` | records, amendment A1, wave evidence, falsification ledger, mined gate | LOG `## Round 95` |
| `9a778917` | tip `--live` re-run (receipt committed) + tip gates | LOG `## Round 95` |
| `16f8cf5c` | scored-receipt gate output at tip | LOG `## Round 95` |
| `333006bd` | falsification ledger narrowing pointer made resolvable (path form) | LOG `## Round 95` |

## Before → after measurements

C1 counting command:

`node scripts/check-backendnode-misdelivery-round95.mjs --lane /home/vgpnk/Projects/shokunin/tabi-shokunin --expect-driver-sha256 24947b00d8a158ad3fea8f5fb035757b6b98aebf48e85d18d506433619e2ee82 --live --scratch <ABS> --ports <http,child,cdp> --json`

- **Before** (base `7b3912bb`): the command is absent (`git cat-file -e` rc 128). The r94 receipt under the
  frozen counter gives rc 1 with 15 finding ids.
- **After, scored run:** the counter ran against `1ecbca38` (the run's `revision`); the run ships in
  commit `360d7cc9`. Result: rc 0, clean, 336 checks, 0 findings. Branches: 1 misdelivery, 11 collision,
  3 miss.
- **Tip run:** measured revision `c67d6a44`, shipped in `9a778917`. Result: rc 0, clean, 336 checks.
- **Wave reproductions:**
  - R95Exec1: two clean runs.
  - R95Exec2: `--reps 10` clean with 1085 checks and misdelivery in 9/40 P legs; one default run clean.
  - R95Sentinel: one clean baseline run.
- **Flake risk:** P(zero misdelivery legs in a default run) is about 0.01-0.05 (R95Exec2). Limit 3
  already declares it; it is routed to r96.
- Corpus counts: knowledge 107 → 108 (`git ls-tree --name-only master corpus/knowledge/ | wc -l`).
  SOURCES rows 234 → 235 (`grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' corpus/SOURCES.md`).

## Sources & frontier

- Census, both by `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tabi`:
  - start: exit 0 (`.ufo/waves/round-95/census-start.txt`, `tabi ok`; W04 warnings only);
  - end: exit 0 (`.ufo/waves/round-95/census-end.txt`).
- Rows 234 → 235 (+1 tier A: S235, Blink `file_input_type.cc` @155.0.8059.84, `mined`, 90d, used by the
  r95 note). S235 was opened 2026-11-08 22:52. Its quote is lines 396-397/402 (3 words by `wc -w`). Its
  sha `f96265db986a` matches an independent re-open by R95Exec3 and R95Scout.
- Rows touched old → new: none (append-only).
- Rejected: a second row for `inspector_dom_agent.cc`, because it duplicates S231.
- Leads for r96: R95Scout's three candidates and R95Critic3's Puppeteer `Page.ts` chooser-listener finding.
- Sourced claim: C1 rests on S235.
- Mined mistakes, in `corpus/lessons/round-95.md` §Mistakes:
  1. A scored record whose receipt was uncommitted. The new gate was shown able to fail: rc 1 on r94.
  2. Port-range collision with another lane. The free-port precheck caught it.
  3. Wording that leans on an unnamed trust boundary. The §8 ledger caught it.
- Assimilation: none. considerthese: this lane has no `considerthese/` directory.

## Pre-file falsification ledger

`.ufo/waves/round-95/claim-falsification.tsv` has 21 rows: 2 `falsifies-wording` (R95Critic1, R95Sentinel),
both pointing to `plans/round-95.md` (§Post-wave amendment A1), and the rest `neutral`.
`python3 scripts/hyaku/prefile-falsification.py --lane tabi --round 95` →
`PREFILE-FALSIFICATION: pass claims=1 rows=21 attack_seats=7 findings=0`, exit 0. The first run, with the
pointer written as `plans/round-95.md#post-wave-amendment-a1`, gave `narrowing-unresolved` ×2 (exit 1).
The pointer was rewritten to the path form in `333006bd`.

## Trend verdicts

- **expansion: improved.** New capability row, knowledge +1, SOURCES +1.
- **quality: improved.** The r94 F1-F4 defects were fixed, each shown by a control. A mined gate was shown
  able to fail. Seven own-lane over-general statements were corrected by append.
- **discernment: improved.** Two seat `falsifies-wording` findings were turned into explicit narrowings
  before filing, not argued away. Three scout candidates were held as leads rather than bulk-admitted.

## Open items

- Routed to r96 (SCORECARD r95 Planned): the 17 R95Mut battery survivors; R95Critic1 W4/W5; R95Sentinel's
  unwritable-scratch rc 1 (should be `setup`), the `--live` ports/driver-status binding and the
  substitution boundary; the branch-misdelivery flake risk.
- Open L0 questions: none.
- Tool installs: none by the L1. R95Critic3 installed `puppeteer-core@25.16.0` via npm into its own
  scratch (reason: S213 tag match), and it was removed with the scratch.

Stale-lane: respawn-per-round driver; no other mission of this lane is open.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md` `## Round 95 gate registry` (commit `c67d6a44`).
- [~] At least one end-to-end domain task executed and logged in LOG.md — LOG `## Round 95`; scored receipt `corpus/evidence/round95/chromium-oopif-backendnode-misdelivery/receipt.json`.
- [~] Instructions executable by an agent without oral context — six cold `--live` reproductions by lane-dispatched seats (`.ufo/waves/round-95/w1/R95Exec1.md`, `R95Exec2.md`, `R95Sentinel.md`).
- [~] No cross-domain bleed (PROVINCE.md still accurate) — PROVINCE.md unchanged; R95Connector found no sibling-lane overlap.
