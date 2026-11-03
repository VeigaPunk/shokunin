# kagi — round 31 (attempt 1)

Lane: kagi (secrets & vault ops; axes freshness + calibration). Frozen BASE
`655e620651808ac04bb59bfa35b81227f62a031b`; plan commit `4767b045773607fc8ab4cb7ba2fea386e05b53c0`
(plan + START census + BASE controls alone, QM29); plan correction 1 `2d46e5759c02307edb3570c389de650040f98956`;
plan correction 2 `91f7752ba551092eef20f6bd43d6dd798dc88ba0` — both alone, before any work commit.
**Measured revision: `a51c49cddfd3adf51ebe2b378cfc75450d788dce`** (the corrigenda-2 commit; every counter reproduces at it — re-run at the tip below) (lane `master`, local=remote,
verified via `jj-lane.sh state` + `ls-remote`). Wave receipts: `.ufo/waves/round-31/`.

## Work performed

Declared claims (2, distinct axes, causally separable):

- **C1 — calibration (owned axis; 9 → 9): the scorecard cell audit is setup-clean again.** The
  lane's self-assessment audit (`bash corpus/claim-ledger.sh cells`) had been unable to run since
  round 26 (five round sections carried headings outside the parser's `## Round <N> —
  pre-move|post-move` shape; the audit died with `unrecognised round heading`, exit 2, no
  CELL_AUDIT summary — the `RevScorecardShape` debt the round-28 verifier routed and rounds 28–30
  each declined to claim). BASE control: `.ufo/waves/round-31/controls/cells-base.txt`.
- **C2 — coverage (9 → 9): the OIDC workload-federation trust-policy theme moves from frontier
  lead to admitted knowledge** (§10 assimilation: one theme, two entries, 11 registry rows
  renumbered by document, every source re-opened in-round; the lead stood unopened since round 21,
  `corpus/README.md` §Frontier / `corpus/SOURCES.md` §Leads). BASE control:
  `.ufo/waves/round-31/controls/c2-base.txt` (rows=60, entries_sourced=8 — a do-nothing round
  cannot reach the after-state).

Work items, each with its evidence:

- **Plan + controls frozen before data (QM29):** `plans/round-31.md` committed alone with the
  START census receipt (`.ufo/waves/round-31/census-start.txt`, fleet validate exit 0, 14 W04)
  and three BASE control receipts (`controls/cells-base.txt`, `controls/c2-base.txt`,
  `controls/host.txt`); commit `4767b04`.
- **Pre-data attack wave findings folded into plan corrections 1/2** (commits `2d46e57`, `91f7752`,
  both before any work commit): migration set widened 3 → 10 (AttackCells F1: R13-01 also moves);
  predicate tightened to the POLICY-summary shape with `cells ≥ 222` (AttackPred F1/F2: uncited
  cells and a silently dropped section must not pass); landing procedure frozen — `LC_ALL=C`
  full-set stamp (AttackCells F2: ambient UTF-8 re-collates 22 rows), order edits → stamp → row
  migrations → receipt; C2 fallbacks named (post-window refusals, tier fallback).
- **Wave `kagi-r31-build` dispatched and settled** (one v1 wave, 15 seats, band 8–16): 1 scout,
  4 executors, 4 scribes, 1 connector, 1 critic, 3 reviewers, 1 mutation-tester; attack share
  5/15 = 33 % (≥ 25 %); 1 connector (≤ 2); the canonical planner seat held by the L1 (the
  validator refuses `planner`; the bounded planning data-walk rode the L1's BASE probes and the
  CensusBase/CellsRed seats); the labrat probe re-roled to an executor seat (the validator refuses
  `labrat`; recorded, no bypass). Routing through `task.agentModelOverrides` (run-15 map); no
  `model` passed. **13 of 15 seats delivered in-wave; OidcEntry2 delivered LATE (~2 h 20 m after dispatch,
  after the L1's integration commit) and was **reconciled**: its draft is better than the
  L1's integration on one load-bearing point (the JP product page DOES carry a
  product-level Japanese-only status the English-needle sweep missed) and was adopted
  wholesale; RowsDraft never delivered (its collision artifacts were used; the L1 built the
  registry rows). Lesson M31-4 (the stall) + M31-6 (the language-blind absence sweep) record
  both. Residual call: none (the frozen counters + committed receipts verify the landed
  state; the outside check is the closure's).
- **BASE re-derivation (CensusBase, scout):** every declared BASE fact re-derived in-lane and
  MATCH (`base/base-*.txt`); the D1/D2/D3 routed facts confirmed (11 paths; the cited receipt
  holds `stale=8`; `PYTHON_SCRIPT_RE` has no `feed-token-agree`; the CR-trim defect site named);
  the OIDC lead's provenance confirmed (introduced round 21, `c41af82`); no sibling carries any
  `*oidc*` entry; the id space S061–S071 free at BASE.
- **C1 falsifiability probe (CellsRed, executor-roled labrat):** the five-reshape probe completes
  to `CELL_AUDIT: POLICY (cells=210 …)` in a lone clone with the three routed reds reproduced and
  the three identity rows passing in-lane (`build/cells-red-*.txt`); the lone-clone FAILs
  classified as QM22 layout artifacts, not lane defects.
- **Kill-rule evidence (MutGates, mutation-tester):** all three counters killable — the heading
  mutant dies with the setup error; three census capture mutants (row-identity digest, 15-column
  row, 26-word quote) each exit 1 with the named SC_FETCH finding; the R24-06 expectation mutant
  FAILs with `verdict-not-final` under full verify (~120 s per run — no QM12 substitute needed on
  this host). Pristine/mutant/restored receipts: `build/mut-*.txt`.
- **Sibling overlap sweeps (ConnOverlap, connector):** workload-identity ground — NO-OVERLAP
  (0 sibling registry rows for the 11 URLs, 0 citations in history over all 20 lanes; every
  keyword hit classified as a false positive with path:line); scorecard heading-shape class —
  kagi-local (1050 sibling non-conformant headings, but 0 of 20 siblings run a cells-equivalent
  gate — no cross-lane obligation); W04 prediction 14 → 16 recorded
  (`build/ConnOverlap*.txt`).
- **D1 hygiene (routed by the round-30 verifier):** the inherited round-30 seat evidence
  committed — 15 paths (the 11 status entries + the labeled stale drafts + the SUPERSEDED-README
  label the ReviewD2 seat required) — commit `2681f2b`.
- **D2 receipt (routed):** the correctly-produced receipt
  `.ufo/waves/round-31/build/selfcounts-at-r31-tip.txt` (stale=0, policy=2, exit 2, in-lane run)
  supersedes the round-30 report's mislabeled pointer (see Landed changes).
- **C2 source re-opening (SrcOpenA/B/C, executors):** all 11 staged URLs re-opened 2026-11-03
  with the declared profile; 16-column capture drafts + per-URL receipts
  (`src-open/group-{a,b,c}.tsv` + receipts); 9 of 11 campaign fetch pins non-reproducing
  (recorded, not hidden); the two spec pins reproduce exactly.
- **Entry re-grounding (OidcEntry1, scribe):** the staged entry's 8 `source:` lines merged into
  one; in-text refs re-pointed by document; six over-assertions tightened (T1–T6); the staged
  text proven unlandable as-is (census G2: 8× SC_USEDBY_NOCITE + SC_ENTRY_HEADER); the
  end-to-end adopted shape validated CLEAN in scratch (G4).
- **Entry attack (AttackOidc, reviewer):** both staged entries ADMIT-AFTER-FLIP; F-A (the AWS STS
  row asserts what its own re-opened source contradicts — the M30-8 class, caught BEFORE landing
  this time) and F-G (the uniform-preview status bullet = the round-22-rejected reading) are
  load-bearing; 12 further flips named with located evidence; the negative-bound audit checked
  15 absence sentences (2 refuted, 1 half-refuted, 12 hold); the adopted-shape census fixture
  CLEAN; the renumber-overlap trap (staged S064/S065 vs new S064/S065) documented.
- **Predicate attack (AttackPred, critic):** 5 MUST-FIX + 5 NOTE findings, all folded into plan
  corrections 1/2 or the landing; both BASE controls re-derived independently (F14: a do-nothing
  round cannot reach either predicate).
- **C1 landing (L1):** the five headings reshaped via the attack seat's canonical sed
  (`build/AttackCells-reshape.sed`; diff-stat 5/5/5, +30 bytes, line count unchanged); six
  never-audited round-29/30 cells given pointer-only Evidence additions (CensusBase F4's
  uncited-cell finding — repaired, not honest-stopped); `## Lane status` section inserted before
  the first round heading; round-31 pre/post sections added parser-legal from their first commit;
  full stamp set re-pinned under `LC_ALL=C` (102 paths); ten count/identity rows migrated to
  measured values with old→new notes; six new ledger rows (R31-01..06); the eight
  self-description cells re-corrected (stale=0). Commits `2dd3f8c`, `22a7119`.
- **C2 landing (L1):** both entries landed with the flips applied; 11 registry rows appended
  (S061–S071; every mapping verified by URL; the row-identity digests recomputed and verified
  11/11); 11 capture rows appended (`corpus/source-fetches.tsv` lines 104–114); README frontier
  bullet moved to core + coverage row added; PROVINCE core bullet added; §Leads round-31
  disposition + a Paths entry. Commit `d8d1f4f`.
- **Quote-fidelity self-check (L1, post-landing):** every quoted span in both landed entries
  re-verified against freshly fetched bodies — 1 defect found and fixed (the RFC 9700 quote's
  sentence-start capitalization; commit `22a7119`); 3 checker false positives inspected and
  dismissed (anchor text, the entry's own rhetorical question, a regex-span artifact).
- **Late-seat reconciliation (L1):** OidcEntry2's draft adopted as the landed entry 2 (the JP
  product-level status quoted and bounded; the corridor table re-grounded to the counted
  Alibaba cells; the workload-ID negative bound to the named pages); the S066 locator
  corrected AGAIN (the first in-round correction's heading also locates 0; the late seat's
  locate counts found 创建可信实体为身份提供商的RAM角色 → 3 / 限制条件关键字 → 2) in entry 1's
  source line, the S066 registry anchor and the S066 capture location; the S071 registry
  scope cell corrected (the "no release status" absence replaced by the quoted JP status +
  the sweep-language limit); lesson corrigenda + M31-6 appended; commit `ffa4add5`.
- **RowsDraft's independent verification of the landed state (post-WAVE-DONE):** the seat
  re-fetched all eleven sources and audited the LANDED bytes — four material findings fixed in
  corrigenda 2 (commit `a51c49c`): S067's section anchor was wrong TWICE (the aud claim-list
  entry sits under "2. ID Token"; §3.1.3.6 contains zero `aud` occurrences — the L1 re-measured
  independently before adopting); the S063 capture location carried the staged defect's section
  label; S068's "BCP 240" and S064's "twice" locator labels corrected to counted forms; S065's
  `ja-x-mtfrom-en` machine-translation marker recorded with the never-cited-beyond-terminology
  bound and the open flip condition; the S071 tier decision recorded (tier A stands
  post-reconciliation; the tier-B option verified green on a scratch clone); the collision set
  corrected to 9 ids (S052–S060). The census and cells re-ran green after every fix.
- **Frontier step:** census before→after recorded (below); mistakes mined
  (`corpus/lessons/round-31.md` §Mistakes M31-1..M31-5); QM32 landed in `corpus/QUALITY.md`
  (M30-4's proposal, red witness = the round-30 plan); considerthese proposal 2 mined and landed
  (the `lane-status:` convention + four binding rows; proposal 3 not mined — its premise is stale
  since round 29).

## Landed changes

Every change is tied to a `LOG.md` entry (the round-31 entry, appended) and to its commit:

| Commit | Change | LOG tie |
|---|---|---|
| `4767b04` | plan + START census + BASE controls (QM29) | round-31 entry, "plan" line |
| `2d46e57` | plan correction 1 (migration set 3→10; R11-08 exception) | same |
| `91f7752` | plan correction 2 (predicate tightening; landing procedure; C2 fallbacks) | same |
| `2681f2b` | wave instruments + D1 hygiene (15 inherited round-30 paths; stale drafts labeled; the D2 receipt) | round-31 entry, "D1/D2 hygiene" line |
| `d8d1f4f` | C2: two entries, 11 registry rows, 11 capture rows, README frontier/coverage, PROVINCE core bullet, §Leads disposition, Paths entry | round-31 entry, "C2" line |
| `2dd3f8c` | C1: SCORECARD reshape + 6-cell pointers + lane-status section + round-31 sections; stamps re-pin (102); 10 row migrations + 6 new rows; lesson; QM32; LOG entry; doc cells re-corrected | round-31 entry, "C1" line |
| `22a7119` | quote-fidelity fix + stamps re-pin + receipts re-taken | round-31 entry, measurements line |
| `72fd52b` | final receipts (cells/census/self-counts/eol/docs/verify at tip) | same |
| `cb7b9b3` | LOG correction (the late OidcEntry2 reconciled; RowsDraft delivered last) | round-31 entry correction |
| `a51c49c` | corrigenda 2: RowsDraft's independent verification of the landed state (S067 §2 anchor, S063 capture location, S068/S064/S065/S071 cell corrections, the S071 tier record, collision set 9) | lesson corrigenda 2 |
| `ffa4add5` | late-seat reconciliation: OidcEntry2 adopted (JP status found), S066 locator corrected twice, S071 scope corrected, corrigenda + M31-6, stamps re-pin, receipts re-taken | round-31 entry + lesson corrigenda |

The D2 pointer defect is superseded by name: the round-30 report's C1 after-state citation
(`.ufo/waves/round-30/final/receipts/selfcounts-at-tip.txt`, which holds the before-state
`stale=8 … setup=1`) is replaced, for every future reader, by
`.ufo/waves/round-31/build/selfcounts-at-r31-tip.txt` (stale=0, policy=2, exit 2, in-lane run at
the tip) and by `corpus/lessons/round-30.md` line 66 (the lesson's own measured record). The
filed round-30 bytes are not rewritten. Three further round-30 report pointers that did not
resolve at `d00e37e` (`.ufo/waves/round-30/SDraftEntries-report.md`,
`final/c3/registry/used-by.tsv`, `build-results.json`) resolve as of commit `2681f2b`.

## Before → after measurements

**C1 — calibration.** Counting command (frozen in the plan): `bash corpus/claim-ledger.sh cells`
run in `/home/vgpnk/Projects/shokunin/kagi-shokunin`.

- Before (BASE `655e620`, control receipt `controls/cells-base.txt`): `claim-ledger:
  unrecognised round heading in …/SCORECARD.md: '## Round 26 — bounded release-drift response'
  (expected '## Round <N> — pre-move|post-move')`, **exit 2, no CELL_AUDIT line** — the audit
  audited nothing.
- After (measured revision `ffa4add5`, receipt
  `.ufo/waves/round-31/final/receipts/cells-at-tip.txt`): `CELL_AUDIT: POLICY (cells=222
  row_pointed=162 stamp_pointed=103 policy=2)`, exit 2 — the audit completes over the full
  37-section population (cells=222 ≥ the frozen 222 floor); zero `unrecognised round heading`
  findings; the FAIL/POLICY set is exactly {R25-02 (FAIL), R29-01 (POLICY), R29-02 (POLICY)} —
  the three operator-routed ids; zero STALE-POINTER; zero UNCITED; 13 HOST-SKIP + 5 SKIP-SELF
  (named non-finding classes). Grading: `grep -c 'unrecognised round heading'` = 0;
  `grep -c '^CELL_AUDIT:'` = 1; the FAIL/POLICY id set = the three routed ids;
  `grep -c '^STALE-POINTER'` = 0; `grep -c '^UNCITED'` = 0.
- Supporting migrations, each re-run green at the tip: R13-01 36→38, R21-04 68→74, R12-03 99→102,
  R21-02 rows=60→71/entries_sourced=8→10/captures=60→71, R14-01 entries=29→31/row_linked=26→28,
  R22-03 added=36→39, R24-05/R24-06/R24-14/R24-15 identity digests re-pinned (membership
  projections, stable across stamp passes — verified); `python3 corpus/self-counts.py` ⇒
  `SELF_COUNTS: POLICY (claims=62 stale=0 … policy=2)` (the eight doc cells re-corrected;
  the two PV-FEEDTOKEN bindings stay the operator-routed reds); `bash corpus/claim-ledger.sh
  docs` ⇒ `DOC_AUDIT: CLEAN (entries=31 row_linked=28 by_hand=3 …)` exit 0; full `verify` ⇒
  `CLAIM_LEDGER: POLICY (claims=74 policy=2 stamped=102)` with FAIL rows exactly {R11-08 (the
  round's own LOG→report pointer, self-resolving on report filing — the round-30 precedent),
  R25-02} + POLICY {R29-01, R29-02} (`final/receipts/verify-at-tip.txt`).

**C2 — coverage.** Counting command (frozen in the plan): `bash corpus/sources-census.sh` run in
the lane repo.

- Before (BASE `655e620`, control receipt `controls/c2-base.txt`):
  `SOURCES_CENSUS: CLEAN (rows=60 A=57 B=1 C=2 queued=1 mined=56 rejected=3 entries_sourced=8
  legacy=21 captures=60 inrow=16 inrow_only=0 inrow_nonreproducing=12)`, exit 0;
  `grep -L '^source:' corpus/knowledge/*.md | wc -l` = 21; 0 `*oidc*` entries.
- After (measured revision `ffa4add5`, receipt
  `.ufo/waves/round-31/final/receipts/census-c2-at-tip.txt`):
  `SOURCES_CENSUS: CLEAN (rows=71 A=68 B=1 C=2 queued=1 mined=67 rejected=3 entries_sourced=10
  legacy=21 captures=71 inrow=16 inrow_only=0 inrow_nonreproducing=12)`, exit 0 — rows 60 → 71
  (S061–S071), entries_sourced 8 → 10 (the two adopted entries), captures 60 → 71, legacy
  unchanged at 21 (the named gap); `grep -cE '^\|[[:space:]]*S(06[1-9]|07[01])[[:space:]]*\|'
  corpus/SOURCES.md` = 11; the per-row clauses (correction 2 item 3): every adopted row's
  `opened` = 2026-11-03 (the awk check prints nothing) and every id on the entries' `source:`
  lines is in {S061..S071}.

## Sources & frontier

- **Census before → after** (the frozen conformance command):
  `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root
  /home/vgpnk/Projects/shokunin kagi` — round start: **exit 0** (14 W04 duplicate-url warnings,
  allowed; receipt `.ufo/waves/round-31/census-start.txt`); round end: **exit 0** (16 W04 — the
  predicted +2 from S069/S070's already-held URLs under different scopes; warnings only; receipt
  `final/receipts/fleet-census-at-tip.txt`). Both outputs and exit codes are pasted in the
  receipts; exit 0 at round end ✓.
- **Rows before → after: 60 → 71** (`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'
  corpus/SOURCES.md`). Added by tier: **11 tier A** (9 docs, 2 spec); 0 tier B; 0 tier C; 0
  rejected this round (the two load-bearing refusals were staged-reading refusals resolved as
  flips, recorded in the Gate). Status histogram after: queued=1, mined=67, rejected=3.
- **Rows touched old→new: none** — no pre-existing row's status/recheck/used-by changed (the
  entries cite only the new rows; prose mentions do not enter used-by — the house precedent,
  verified by OidcEntry1 F5b's scratch reproduction).
- **Frontier advanced:** the OIDC workload-federation trust-policy lead (round 21) moved to core
  (`corpus/README.md` §Frontier bullet + coverage row; `PROVINCE.md` Core bullet; `SOURCES.md`
  §Leads round-31 disposition). The NIST SP 800-57/800-133 leads stay leads. The 21 legacy
  entries stay the named gap (deliberately unclaimed; `corpus/README.md` §Known gaps).
- **Assimilation (§10): one theme adopted** — OIDC workload-federation trust policy, from
  `/home/vgpnk/Projects/shokuknow/merge/kagi/` (read-only; nothing written there): two entries +
  11 rows, every source re-opened in-round, per-entry gates with ≥1 admit and ≥1 reject-or-flip
  (F-A and F-G are the rejected readings), the collision check run (9 collisions, all resolved by
  the by-document renumber map; artifacts `build/assimilation/`), no staged row appended as-is
  (the census refused the staged shape; the landed shape is census-CLEAN).
- **considerthese:** one still-unimplemented proposal mined (2026-10-26 proposal 2,
  machine-readable lane status) — landed as the `lane-status:` convention + lesson snippet +
  four binding rows, citing `considerthese/2026-10-26.md` + 2026-11-03; proposal 3 not mined
  (premise stale since round 29).
- **Sourced-claim duty:** carried by C2 — every adopted row was opened in-round (capture rows
  104–114; the seats' receipts cross-checked).

## Trend verdicts

- **expansion: improved** — 11 registry rows and 2 admitted entries on ground the coverage map
  did not hold (the round-21 OIDC lead), each citing mined rows opened this round; census rows
  60→71, entries_sourced 8→10, exit 0; the frontier bullet moved to core; no admitted entry
  fails the bar it was admitted under (the flips landed before the commit, unlike round 30).
- **quality: improved** — the cell audit re-armed (222 cells walked, 0 uncited, 0 stale-pointer;
  it had audited nothing since round 26); the eight self-description cells re-corrected
  (self-counts stale=0); the two new entries carry provenance trios, falsifiers and per-feature
  status discipline; the M30-8 class (landed entries contradicting their own sources) was
  prevented pre-landing this time — the STS misreading and the uniform-preview reading were
  refused as staged and re-derived from the re-opened pages before any commit; no admitted entry
  fails its re-check.
- **discernment: improved** — the round's gate exercised rejections with evidence (F-A/F-G
  grounded in re-opened sources; 15 absence sentences audited, 2 refuted and repaired); the
  round-30 outside disagreement (M30-8) became the QM32 criterion plus the pre-landing flip
  discipline — the LEARNING.md improved condition's second arm ("a disagreement becomes a lesson
  that adds a grounded QUALITY.md criterion"). Caveat: this round's own outside spot-check is
  the closure's to run; a disagreement there is the next round's input, reported not smoothed.

No axis is harmed: all six axes stand 9 → 9 with the increments recorded under the claims
(SCORECARD round-31 post-move table); the routed reds (R25-02, R29-01, R29-02) are unchanged
operator-owned state, named in the lane-status line and the predicate — not traded away.

## Stale-lane

One mission open: this round's own (launch `2026-11-03T16:23:55-03:00 kagi round=31 attempt=1`,
watchdog.log) — **progressing** (lane commits `4767b04`…`22a7119` authored by the lane identity
today). No other kagi mission is open.

## Routed defects and open L0 questions

- Round-30 verifier routed defects: D1 (uncommitted round-30 evidence) — disposed, commit
  `2681f2b`; D2 (receipt-pointer defect) — disposed (superseded by name, above); D3 (operator
  items) — routed around, still open; D4 (promotion note) — operator-owned, untouched.
- Open L0 lines touching kagi (never treated as answered): `kagi | round-28` ×2 (the documentary
  safety-stop disposition; the feed-tokenizer ruling — the fix landed in round 29, the ruling is
  still open), `kagi | round-30` ×2 (the `feed-token-agree` registration in `PYTHON_SCRIPT_RE` —
  until it lands, R25-02/R29-01/R29-02 stay red and the cells summary stays POLICY; the fleet
  parser CR-trim defect — fleet-owned, kagi repaired only its own bytes), plus the older
  `kagi | round-10` (cmd_refs prefix-match) and `kagi | round-16` (dispatch-contract
  reconciliation) lines. No new L0 question is filed this round: nothing was blocked that the
  lane could not route around.
- The 2026-10-21 content-safety refusal boundary stayed binding: no claim touched feed-token
  derivation, token totality, or the release-clock tokenizers; no refused work was retried,
  rephrased or rerouted.

## Inherited state

The 15 inherited round-30 paths (11 status entries + the stale-draft labels + the
SUPERSEDED-README) were committed under this round's entry (`2681f2b`) per the
inherited-worktree rule and the round-30 spot-check's routing; the two modified files were
append-only seat reports (+48/+48 lines, 0 deletions). Files the lane did not author were not
touched.

## Tooling

No tool was installed or upgraded by the L1 or any reporting seat (the wave needed none); no
pacman transaction was run (host-wide pause respected). Scratch discipline: every clone/fixture
lived under `/fast/scratch/hyaku/kagi-r31/<seat>/` and was deleted by its seat before yield
(receipts copied into the wave dir first); the L1's scratch (`/fast/scratch/hyaku/kagi-r31/`) is
removed after this report lands.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources —
  Evidence: SKILL.md §Vault-ops decision table, §Failure table, §Credential-hygiene checklist;
  the citation gate re-runs at the tip (`final/receipts/verify-at-tip.txt`, R11-08 self-resolves
  on this report's filing; the round-30 CLEAN baseline stands at LOG.md:758).
- [~] At least one end-to-end domain task executed and logged in LOG.md — Evidence: LOG.md:20
  (round-3 end-to-end pipeline, exit 1, honest stop); this round's end-to-end work is the
  OIDC adoption executed gate-to-gate (census CLEAN at the tip).
- [~] Instructions executable by an agent without oral context — Evidence:
  `corpus/lessons/round-31.md` + `plans/round-31.md` re-derive both claims' counters from
  committed bytes alone; the 13 delivered seats executed their items from the written briefs.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — Evidence: PROVINCE.md §Core round-31
  bullet + the connector sweep (0 sibling claims on the adopted ground;
  `build/ConnOverlap.md`); scope-gate R1–R11 unchanged.
