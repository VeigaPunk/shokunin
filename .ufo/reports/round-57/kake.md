# Round 57 — kake report

Lane `kake-shokunin`, base `28fa0b23e699303725aba2727094531f5e44494d`, measured content revision `32754df75774dd38e8a96fcda375fc93adf97f1e` (the commit at which both the C2 gate and C3 counter
receipts were run and at which the counters were frozen), final lane tip `20217f23eca15862febe14545523832e21584106` (`git ls-remote origin refs/heads/master` prints it). Inherited state: no
`lane-dead-no-report kake round=57` line known to this attempt; nothing inherited. Round-56 verifier spot-check read; routed defects 1–4 addressed below.

## Work performed

Declared claims (frozen in `.ufo/waves/round-57/contract.md` at `b9a5d012f7fd` before any data; counter versions disclosed in its two § Counter versions sections): **C1 calibration** — every
relabel of a measurement receipt in rounds 52–56 is disclosed with its true values and this round's three receipts carry the revision their run covered. **C2 operability (capability
acquisition)** — `scripts/id_resolver.py` (considerthese proposal 2). **C3 freshness (sourced)** — two Baidu dead-link entries on rows opened this round (S421, S422). Axis note for the operator:
calibration is the round-54 bounded sub-axis (score 1, lowest non-retired) and is outside the prompt's operability + freshness list; `w1/CriticAxisClaim.md` argues C1 is operability and C3
coverage/expansion. The declarations stand, the ownership question stays open, scores stay (calibration 1, operability 10, freshness 10). No exploratory claim.

- Round shape: two v1 waves, W1 build + pre-data attacks 40 seats, W2 falsify 37 seats, **77 total**, no residual call; the L1 held the planner seat. W1 roles: executor 12, scout 9, critic 8, scribe 4, reviewer 4,
  connector 2, mutation-tester 1. W2: executor 10, critic 7, reviewer 6, scout 6, mutation-tester 3, connector 2, sentinel 1, revenger 1, simplifier 1. Dead seats: none (40 of 40 and 37 of 37 reports committed;
  one W2 report opens `# MutC3Counter-3`, the seat's variant of its name). Settlement: `.ufo/waves/round-57/settlement.md`. Seat counts come from `w1-results.json`, `w2-results.json`.
- Counters attacked before and after build: W1 found all three version-1 counters met by junk (C1: three bare pin receipts, `w1/CritCheatC1.md`; C2: a 10-line constant printer 5/5, `w1/CritCheatC2.md`; C3: 13 junk files and
  sidebar/CSS quotes, `w1/CritCheatC3.md`) and C1's pin rule self-contradicting (`w1/CriticC1Counter.md` S0) → version 2. W2 attacked version 2 (a judge-importing shim 5/5, off-topic article text 8/8, a merge-shaped relabel,
  a rename out and back, the counter editable after measurement: `w2/CriticAxisWave2.md`, `CritCheatC3V2.md`, `CritCheatC1V2.md`, `ReviewerPinsV2.md`; 44 C1 mutants 40 killed, 38 C3 mutants 27 killed, 31 tool mutants 20 killed) → version 2.1,
  selftests 71 / 120 / 49, counters frozen at the measured revision and pinned by `measured.json`.
- Entries: `corpus/knowledge/baidu-dead-link-types.md` (S421) and `baidu-spider3-dead-link-model.md` (S422); rewritten after 21 sentence-level findings of W2 critics and reviewers (`w2/CriticEntryTypes.md` 11 of 39 sentences,
  `w2/CriticEntryModel.md` 10 of 42, one false 索引 location from `w2/ExecSweepsNegative.md`).
- Re-verification (freshness): fresh GETs of both pages: article blocks byte-identical to the retained bodies, only script-region cache tokens differ; both recheck commands print 1 (`w1/ScoutFreshnessBaidu.md`,
  `w2/ExecReopenS421.md`, `w2/ExecReopenS422.md`); no drift.
- Assimilation: theme Baidu dead-link handling from `merge/kake/`; id lists/collisions/renumber map in `corpus/lessons/round-57.md` § Assimilation: reg 158, staged 129, collisions 8 (S312 S329 S367 S372 S373 S374 S390 S409, the same
  documents), map S403→S421, S408→S422 by document; guard proof `assimilation/guard-proof/` and `w1/ExecIdGuard.files/`. Quarantine slice (12 rows) hand-checked: 10 VERIFIED, 2 ABSENT as registered (S148, S206), none adopted; two re-opened by
  independent seats in W2. Rejected as staged with the page sentence each reason was read against: S390, S409/S410, S404/S414, S358 (lesson § Gate).
- Considerthese: proposal 2 (cross-registry id resolver) implemented as `scripts/id_resolver.py` (C2). Proposals 1 (r56) and 4 (r55) already landed; 3 not taken (one per round).
- Routed defects (r56 spot-check): 1 receipt relabel — C1 and `receipt-errata.json`; 2 S388 reject reason — QUALITY criterion 2 and every reject of this round re-read against its page; 3 disclosed limits — carried; 4 SHONEN — all `[ ]` below.
- Mined mistakes: seven rows in `corpus/lessons/round-57.md` § Mistakes (landing, attribution, vacuous, stale-premise, reference-drift, scope, number-drift) with five QUALITY round-57 criteria.
- Adjacency (reported, not absorbed): the new tool over the fleet (`w2/ExecResolverFleetRuns.md`): 8 of 21 lanes cite ids their own registry lacks (41 ids); one (souji S146) is a missing source row, the rest are DOI fragments, staged ids, filenames and labels.
- Tools installed: none. Misroot sweep (`git -C /home/vgpnk/Projects/shokunin status --porcelain`): untracked fleet-root paths are `.tower/`, `.ufo/waves/round-30/`, `round-31/`, `demo-cwd.txt` (other lanes' or operator state; none names kake or round 57). Open L0 questions: none appended.
- Disclosed limits: C1 re-derives its own report line at T0 and checks the other two receipts' shape, not that their counters ran; C2's G4 reads live sibling registries (snapshot-bounded) and its sandbox needs bubblewrap; the tool is fence-blind in a registry and drops
  non-ASCII knowledge paths at a revision (found by W2 after the freeze: `w2/CriticResolverCheat.md` D1, `w2/ReviewerResolverCode.md` F1; kake's entries are ASCII-named and unfenced); C3 certifies quote text nodes, not support; `SimplifierBuild` deletions not applied;
  `c56_quote_truth.py` is 6/8 at the tip by design (its mirror pins 158 rows).

## Landed changes

| Change | LOG.md entry | Commit |
|---|---|---|
| Frozen contract, counters v1, base controls, retained sources, pre-append mirror | Round 57 | `b9a5d012f7fd` |
| W1 spec/dispatch, gate `--fleet`, span helper | Round 57 | `f7c98ff26928` |
| W1 results; build: two entries, S421/S422 rows, id_resolver, README/PROVINCE/lesson, counters v2 | Round 57 | `cddef5b4fd36` |
| SKILL gate rows, QUALITY criteria, receipt errata, registry append-only fix, W1 settlement | Round 57 | `4b8c73050470` |
| W2 spec/dispatch | Round 57 | `51921b971246` |
| Build revision X: counters v2.1 frozen, tool 49 checks, repaired entries, lesson, W2 reports and settlement (measured content revision) | Round 57 | `32754df75774` |
| T0: measured.json, SCORECARD, LOG, C2/C3 receipts, placeholder C1 receipt | Round 57 | `31b61a4ddfca` |
| C1 receipt written after its run at T0 (lane tip) | Round 57 | `20217f23eca1` |

## Before → after measurements

| Claim | Command (revision) | Before (base `28fa0b23`) | After |
|---|---|---|---|
| C1 calibration | `python3 -B .ufo/waves/round-57/c57_receipt_pins.py --root . --revision <tip>` | `undisclosed_relabels=6 … new_receipts=0 scorecard_pin=0 met=False`, exit 1 (`controls/base-c1-receipt-pins-v2.txt`) | tip `20217f23`: `undisclosed_relabels=0 phantom_errata=0 deleted_receipts=0 new_relabelled=0 new_unpinned=0 new_receipts=3 scorecard_pin=1 met=True`, exit 0 (`controls/after-c1-receipt-pins.txt` is the `--no-bodies` run at T0 `31b61a4d`, pinned to `32754df7`); selftest 71/71 (`controls/c1-selftest-final.txt`) |
| C2 operability | `python3 -B .ufo/waves/round-57/c57_idresolver_gate.py --root . --revision <rev> --fleet /home/vgpnk/Projects/shokunin` | `0/5 met=False`, exit 1 (`controls/base-c2-idresolver-v2.txt`) | `32754df7`: `5/5 met=True`, exit 0 (`controls/after-c2-idresolver.txt`); tool selftest 49/49 (`controls/tool-selftest-final.txt`) |
| C3 freshness | `python3 -B .ufo/waves/round-57/c57_quote_truth.py --root . --revision <rev>` | `0/8 met=False`, exit 1 (`controls/base-c3-quote-truth-v2.txt`); registry 158 rows | `32754df7`: `8/8 met=True`, exit 0 (`controls/after-c3-quote-truth.txt`); registry 160 rows; selftest 120/120 (`controls/c3-selftest-final.txt`) |

Independent checks: `w2/ExecReopenS421.md`/`S422.md` (live re-open, recheck counts, span tables), `w2/ExecGateFlake.md` (genuine tool 5/5 ten of ten runs; junk tools 1/5–4/5; unsorted owners pass by design), `w2/ExecC1Dryrun.md` (the T0 landing sequence in a scratch clone,
three breaks caught), `w2/ExecCensus.md`. Verdict words are author-side; admission belongs to the non-author closure. No receipt carrying a `revision:` line was rewritten after commit (C1 enforces it; the version-1 base receipts stay as history).

## Sources & frontier

- Round-start census: `sources-census.sh validate --root /home/vgpnk/Projects/shokunin kake` → exit 0, 158 rows, 14 W04 (`controls/census-before.txt`, exit file `census-before.exit`). Round-end: exit 0, 160 rows, same 14 W04 ids (`controls/census-after.txt`). Rows: 158 → 160 (`grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'`).
- Added by tier: A 2 (S421, S422). Touched old→new: none (no existing row's status, recheck or used-by changed).
- Frontier rows advanced: per-engine crawl hygiene (Baidu dead-link types and the Spider 3.0 recognition model), the README frontier ground map (one row, 9 → 11 per-engine entries); the first hand-check of the 12-row quarantine slice.
- Assimilation: one theme, 2 entries, 5 staged candidates rejected with reasons and flips in the lesson Gate. Non-author spot-check pending (admits S421/S422; rejects S390, S409/S410, S404/S414, S358; commands in `w2/ScoutSpotcheckPrep.md`).
- Mined mistakes: seven rows with QUALITY round-57 criteria; red-before: `controls/base-c1-receipt-pins-v2.txt` exit 1.
- Sourced claim: C3 rests on S421 and S422 (opened this round); the entries cite them.

## Trend verdicts

- expansion: **improved** — two entries on Baidu dead-link ground the coverage map did not hold (0 knowledge files cited either page or 死链 at base), each citing a `mined` row; plus a capability and the 12-row quarantine hand-check; coverage map 52 → 54 files.
- quality: **improved** — six receipt pins disclosed, three counters and a gate hardened by 77 seats before they scored, entries re-cut after 21 findings, one staging-id leak caught by the new tool before landing; bounded: entry fidelity is reviewer-evidenced, not counter-proved; the tool has two disclosed defects found after the freeze.
- discernment: **unchanged** — admits and rejects are recorded with reasons, flips and the page sentences they were read against, but no non-author spot-check exists yet; the closure decides.

Stale-lane: respawn-per-round driver; no other mission of this lane is open.

## SHONEN

- [ ] SKILL.md contains real decision tables, error patterns, checklists, cited sources (registry rows added this round; no promotion claim)
- [ ] At least one end-to-end domain task executed and logged in LOG.md (untouched as a promotion box)
- [ ] Instructions executable by an agent without oral context (untouched this round)
- [ ] No cross-domain bleed (PROVINCE.md still accurate) (adjacent scan: `w1/ConnSiblingOverlap`-class work not repeated; fleet run of the tool is reported, not absorbed; no non-author verifier yet)
