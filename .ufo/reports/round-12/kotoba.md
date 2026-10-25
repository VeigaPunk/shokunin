# kotoba — round 12 report

Lane: `kotoba` (`~/projects/shokunin/kotoba-shokunin`). Axis move: **consistency**
(this lane declares it a `calibration` sub-axis — `AXES.md` has no `consistency`
row; the mismatch is the protocol lane's, filed in round 10 and still open).
Before → after: **9 → 10**, rubric band 10 = *repeated non-author verification in
the opposite direction*.

Scope compliance: every write this round is inside `kotoba-shokunin` (own repo) or
this report plus the round-11 report in `VeigaPunk/shokunin`. Domain source trees
(`ufo-fsd-alpha`, `bounties`, `webzites`) were read-only for the census/sentinel/
connector lanes (`git ls-files`, `git cat-file`, `test -e` only). One operator
directive landed outside the repo (below) at the operator's explicit instruction.

## Round opening — the predecessor round landed first

Round 11 ended with its working tree complete but uncommitted (respawn cut it
before the commit). Per `../PROTOCOL.md` § respawn this round resolved it: three
reported-absent pointer tokens rewritten as prose, the baseline re-recorded with
all nine ids (the draft omitted `corpus.pointers.report_total`, which is why that
id read `expected=None`), and the round-11 work landed as **`4dd7753`**, with the
`round-11` `LOG.md` entry written here — that entry did not exist, one of the four
false-at-HEAD claims this round's census found (`corpus/README.md`'s round-11 row
asserted it). The round-11 report was filed late in the main repo under the lane
identity (`f9dcfd2`), with its cold-run placeholder filled and its missing
`SHONEN` heading supplied.

## The move — a second *witness*, not a second *run*

`verifiers/verify_corpus_independent.py` (776 lines, sha256
`430fe289feb07eff638e33326ac17554f19d7e0579363f9c90137e571671f0e5`) was written
from the class spec by L2 lane `ExecIndependentVerifier`, which authored neither
`verifiers/verify_corpus_integrity.py` nor its baseline and **never read its
source**; it derives the index/pointer/commit classes with its own tokenizer and
counting code, and is baseline-free by construction (its `equal`-class ids print
`observe`, only the six violation classes gate).

Agreement, re-derived by three other lanes and by me:

| world | author's instrument | independent instrument |
|---|---|---|
| landed tree | `9/9 checks pass`, exit 0 | exit 0 |
| numbers | 39 tracked, 43 index tokens, 25 checked pointers, 0 dead, 23 hex citations, 8 excluded, shapes 24 absolute + 1 tilde | identical, including detail sets |
| clone at `d49dfa5` | exit 1, `report_dead=10/19`, `commit_nonhash=1`, shapes `rel 9 / abs 8 / tilde 1 / bare 1` | exit 1, same ten dead sites, same non-hash site |

Agreement was re-run in three live tree states (corpus manifests `632a6b0e…` →
`bc66c2a6…` → `d4c9eaa6…`) with every number unchanged, so it is not a snapshot.
Full record: `corpus/knowledge/independent-verification-round12.md` (in-repo), with
`/tmp/round12/ExecIndependentVerifier/{compare.md,METHOD.md,…}` as the lane's raw
evidence.

**Seven definitional differences adjudicated** (the record's §3; none a verdict
disagreement): `commit_total` key semantics; baseline `equal` mode vs baseline-free
`observe`; index scan scope; glob-bearing pointer bookkeeping; two annotation
differences; raw-candidate counters. One shared property, measured on both: pointer
resolution is host-anchored, so with the host `.ufo` hidden a clone goes dead =
checked (24/24 on the landed tree, 19/19 at `d49dfa5`) **identically in both
instruments** — a second agreement, and the strongest carried gap.

**Two repairs the derivation forced on the author's script** (both pinned by
self-test, live verdicts unchanged):

- the documented quoted-report-pointer context rule could never fire — the
  tokenizer admitted `"` into a token, so the match began at the opening quote and
  `inside_quotes` saw zero quotes; fixture proof: pre-fix `report_total=26 dead=2`
  with the quoted token reported as a promise → repaired `dead=1, quoted=1`, and
  `9/9 checks pass` exit 0 with the quoted line alone;
- the index census read column 2 of *any* table row in `corpus/README.md` while its
  docstring promised the coverage-map section (measured difference today: 0
  tokens) — now scoped to the section, with two new self-test assertions.

`--self-test`: 80 assertions as landed at `4dd7753` → 88 now. Declared, with the
full sha chain and a reachability qualifier for the two pre-commit digests, in
`corpus/knowledge/cold-run-round11.md` §7.

## Verification of the round-12 claim (batch-2 lanes, non-author)

- `CriticSpec` (critic, batch 1) — attacked the claim *before* the landing: three of
  four attack paths already closed by staging; it reproduced the W0 red direction
  itself (both exit 1, same sites, same shapes); it **independently falsified the
  committed blob `391a54f4`** on the quoted-pointer idiom (span began at the quote;
  the promised keys did not exist) and **confirmed** the repaired file on nine
  boundary cases, including a quoted token that *resolves* (context, not
  population). Its named residuals — "agreement falsifies implementations, never
  specs" (a spec-derived battery is the extra act; the committed harness is that act
  for the fault classes) and "authorship is attested, not verifiable" — are recorded
  in the record's §6, not waved away.
- `ReviewerRound12` (reviewer, batch 2) — re-ran both instruments, both self-tests
  (88 / 52 assertions, exit 0), verified the red direction site-by-site, checked both
  `--repo` gates exit 2 on a non-git dir, and confirmed nothing writes inside the
  repo. Its four required fixes were resolved: the harness's `fault-f` expectation
  (now a documented blind-spot row, `ALL PASS` exit 0), the dead round-12 report
  pointer (this report), the census row count (now quoted with its command, both
  numbers recorded), and the §3b overreach (round 11's "shape-only rewrite ≡ no-op"
  re-scoped as incomplete rather than false — an in-grammar rewrite is a no-op, a
  rewrite that leaves the grammar is visible only through the count detector).
- `ScoutReCensus` (scout, batch 2) — delta against batch 1's census: 4 stale rows
  repaired, 22 rows moved again by this round's own landings, 11 sites that lagged
  mid-flight and are now fixed; the round's "no new false claims" bar was met only
  after the fixes it listed (harness exit status, the report pointer, the `[x]`
  boxes, the coverage-row count, the assertion-count chain).

## Counting-claim census (the round's measurement instrument)

Batch-1 lane `ScoutClaimCensus` produced 84+ row-claims with executed commands;
landed in-repo as `corpus/knowledge/claim-census-round12.md` (a new index row) so the
measurement is re-runnable from the repo, not from `/tmp`. Headline verdicts at the
pre-repair tree, quoted with their command: **49 AGREES, 22 STALE, 6 UNEXPRESSIBLE,
3 FALSE-at-HEAD, 3 PARTIAL, 1 DISAGREES**, plus one `planned, unmet` row; the
round-12 reviewer's raw `|`-split counted 86 rows instead — both numbers stand,
which is itself the point (a count carries its command).

Repairs forced by it, all live sites: 24 stale numbers (33→39 tracked files,
19→25 checked pointers, 21→23 citations, 1→8 excluded sites, 18/1→24/1 pointer
shapes, 80→88 assertions), 4 false claims (the missing round-11 `LOG.md` entry; the
cold-run record's byte-identity claim; its mid-landing capture, now labelled
historical; **`SHONEN.md` box 1's own `awk`**, which printed an empty line while
claiming `13/9/9/8` — the fourth instance of the round-11 defect class, in the file
the round-6 audit used that same expression to correct), 9 unexpressible claims
labelled, and round-10's commandless "4 unindexed files" re-qualified (a brace-aware
`comm` reconstruction at `e997d45` yields 7). The **claim-scope rule** adopted with
this: *a per-round record carries its round's number; a live document carries the
current one* — which is why `LOG.md`'s earlier entries and `lessons/round-10/11.md`
keep their values instead of being rewritten.

## Fault harness landed in-repo

`verifiers/fault_injection_corpus.sh` (`--repo/--keep-worlds/--self-test`, exit
0/1/2, per-fault `--no-hardlinks` clone, JSON-only assertions) replaces round 11's
`/tmp` fault table, which was not re-runnable after the scratch wipe. Ten fault
classes, **both** instruments gated: must-fire `a b c d1 d2 e` all fire with the
intended class in both; the equivalent mutation stays clean; the quoted-pointer
idiom is asserted on its counters (context +1, checked population unchanged);
`fault-f` is a **documented blind spot** — a pointer moved *out of* the
`.ufo/reports/round-N/` grammar is invisible to both tokenizers, visible only
through the `equal`-mode count detector in default mode. Live run: `ALL PASS`,
exit 0; `--self-test`: 4 probes, exit 0.

## SHONEN

- `[x]` SKILL.md decision tables / error patterns / checklists / cited sources —
  checked this round by non-author lane `ReviewSHONEN` (printed `awk` run as
  written; per-section split re-derived independently; 36 § Sources targets
  spot-checked, 36 OK / 0 MISS).
- `[x]` end-to-end domain task logged — round-11 corpus verifier + its non-author
  cold run (promoted in round 11 by runner `ColdRunRecord`).
- `[x]` instructions executable without oral context — checked this round by
  `ReviewSHONEN` (three stated procedures run verbatim from a foreign cwd with the
  stated outcomes); it found one cwd assumption, now stated in `SKILL.md`.
- `[~]` no cross-domain bleed — `PROVINCE.md` unchanged; the five external defects
  below were re-verified and routed, not repaired.

## Cross-domain (audited, routed, not absorbed)

- Sibling trigger gap unchanged (`SentinelCross`, batch 1): 0/5 sibling
  `*-shokunin/SKILL.md` descriptions carry a quoted trigger or an arbitration
  clause; the round-8 drop-in rewrites remain producer-ready and unapplied.
- **Two sibling stale-count defects found with reproducers** (`ConnectorCross`):
  kake `corpus/knowledge/ops-automation.md:22-30` — 11 of 77 `state/probe-history.jsonl`
  rows violate `total-ok == violated+errors` (cwd `~/Projects/webzites`); kasegi
  `corpus/knowledge/mission-ledger.md:32-34` — 8 of 718 `ledger/missions.jsonl`
  rows lack `transition`. Owners: kake, kasegi lanes.
- `kumitate scripts/cite-check.mjs` is complementary, not a consolidation
  candidate; **kengaku already ships this round's pattern** — a non-author oracle
  (`corpus/evidence/round10-fleet/probe_ref.py`) re-derived its evidence and
  returned `ALL LAYERS AGREE`; its L2 mutation harness also caught a first grader
  failing its unmutated control. Fleet pattern, not a local invention.
- Fleet commit identity: `kumitate 7a4c9a0` and `kagi ea77bf0` resolve in their own
  repos, authored `shokunin <shokunin@local>` — resolvability fixed, the non-lane
  identity defect reported, not repaired.
- Host config stale outside this province: `~/.agents/AGENTS.md` procedures
  `:55/:57`, dated TAC text `:48/:51`; `~/.config/opencode/agents/ufo.md:7`
  `cascade_note` ~30 days past its own expiry; six `*-shokunin/SKILL.md` sit inside
  no discovery root (0/6 in the union of four roots).
- The aggregator's own artifact carries the same broken `awk` expression
  (`corpus/lessons/round-6-aggregator-audit.md:30`) — aggregator-owned, routed, not
  edited.

## Operator directive honoured (outside the repo, recorded)

`~/.omp/agent/config.yml` — the global cascade now lists
`zai/glm-5.3-flash:max` **before** `opencode-go/glm-5.3-flash:max` in
`retry.fallbackChains.m_zfl` (the alias every `@m_zfl` subagent route resolves to).
YAML re-parsed, `cfg://retry/fallbackChains` shows the new order, backup
`config.yml.bak-zfl-zai-order-20260928-200540`. `m_z53`'s identically shaped chain
was left untouched (not a z-flash alias) and is named here so the omission is a
decision, not an oversight.

## L2 lanes (12, two batched `task` calls; MISSION floor 8)

Batch 1: `ExecIndependentVerifier`, `ScoutWorlds`, `LabratFaults`, `CriticSpec`,
`SentinelCross`, `ConnectorCross`, `PlanRound13`, `ScoutClaimCensus`.
Batch 2: `CriticRound12`, `ReviewerRound12`, `ScoutReCensus`, `ReviewSHONEN`.

## Mission staleness / progress

This mission launched on the round-12 prompt and is `progressing`: commits
`4dd7753` and `7d15407` in the lane repo, the round-12 commit below, plus continuous
file activity under the repo. No stale-lane condition to report.

## Falsifiable next iteration (round 13)

The ceiling: **no verifier in this repo runs a checklist box**. Candidate
(scratch plan by `PlanRound13`, not an in-repo artifact and not citable as
evidence): make `skill.trigger.name_directory` executable — a check that the six
`*-shokunin` frontmatter names match their directories (6/6 today) with a
missing-name fixture that must exit 1 while the live tree exits 0. Falsifier: the
fixture must fire its own class and the live tree must stay green, or the move did
not land. Second candidate: a derivation-owned *expected census* (the baseline is
still authorial — the unfinished half of this round's reversal).

## Artifacts

- `verifiers/verify_corpus_independent.py`, `verifiers/fault_injection_corpus.sh`
- `verifiers/verify_corpus_integrity.py` (two repaired claim/behaviour gaps),
  `verifiers/corpus-baseline.json` (re-recorded)
- `corpus/knowledge/independent-verification-round12.md`,
  `corpus/knowledge/claim-census-round12.md`, `corpus/lessons/round-12.md`
- `corpus/knowledge/cold-run-round11.md` §7, `corpus/knowledge/corpus-integrity-round11.md`
  (landed-counts audit trail), `corpus/README.md` (4 new rows), `SKILL.md`
  (+1 checklist box, +3 Sources entries, cwd note), `SCORECARD.md` (consistency
  9 → 10, depth/operability/coverage/freshness/calibration/adjacency retagged),
  `LOG.md` (round-11 entry written, round-12 entry)
- Commit: `LANE_HASH` in `kotoba-shokunin`; this report committed + pushed in the
  main repo under the lane identity.