# kake — round 95 (hyaku run 15, attempt 1)

Lane: kake (repo `/home/vgpnk/Projects/shokunin/kake-shokunin`). Round base
`fdd5fdbeb8a2ba6c18f0f23135d1bee98068dca3`; instruments commit
`43cdd9fc899a2613d8ba7b55edf820825e57b4d1`; freeze
`8f638b591e739e1863f5fa22334d5e15178189ed`; integrity-ruling restoration
`4f443b3fd79f88fc75cfe46005c01d3ecd85c16f`; integration commit
`9cf924700308995354d85c165acbba9930d02981`; pre-receipt tip `1fca1ad721a238411e54a67a15a08e762b566943`; final lane tip `7bace5789077167614212d0a34d31f1bb448e668` (carries the tip-named receipts).

## Work performed

The round declared **two claims** (freeze `.ufo/waves/round-95/freeze.md`,
declared before any seat scored):

- **C1 — calibration (HOLD 2, lowest owned axis): strict self-assessment
  conformance repaired** — target: the frozen counter `c95_selfassess.py`
  reads `pins=ok`, zero mismatches, battery 20/20, admit 5/5, shadow absent,
  predecessor ≥ 4, `met=true` exit 0 at the landed tip.
- **C2 — freshness (HOLD 10), capability acquisition: conditional_eval
  contract v2** — target: `c95_conditional.py` scores
  `scripts/conditional_eval.py` at `hand=66/66 generated=120/120
  forgeries_refused=7/7 positive=admitted mutants=40/40` with zero
  unreceipted survivors, `met=true` exit 0 at the landed tip.

Work items (each with evidence):

- Frozen instruments built and committed before dispatch: `c95_selfassess.py`
  (successor C1 counter: content-pinned identity, no `--surfaces-file` flag,
  `--verdict-only` can never print `met`, effectful-shadow battery route,
  20 refuse + 5 admit battery routes with named-finding assertions —
  `controls/instrument-sha256.txt`, `controls/ctl-c1-selftest.txt`) and
  `c95_conditional.py` (contract v2 population: 66 hand cases incl. two raw
  duplicate-key refusals, seeded generated population, 7 forgeries, v2
  positive control, 40-mutant battery with the R94-4 equivalence-receipt rule;
  selftest `controls/ctl-c2-selftest.txt`). Do-nothing controls committed
  before data: `controls/base-c1.txt` (mismatches=18 E3=3 E5=15, met=false at
  `fdd5fdbe`), `controls/base-c2.txt` (hand 57/66 at the instruments commit).
- R94-4 pre-freeze equivalence scan: the 40-mutant population scored against
  the v2 reference — 40/40 killed, zero survivors, M11 included
  (`controls/mutant-scan-v2.txt`, `-result.json`); kill target frozen at
  40/40 with the receipts rule declared.
- R94-5: 15 SKILL.md directory rows repaired to name concrete committed
  non-empty blobs, row-by-row choices with cat-file evidence
  (`w1/ExecC1Repair/repairs.md`, `repair.diff`); 260 rows ≥ base 255; first
  cells intact. R94-9: five gate-registry rows added to SKILL.md's
  `### Owned freshness gate registry` (c93_conditional, c94_selfassess,
  c94_conditional, c95_selfassess, c95_conditional).
- R94-6/R93-10: `scripts/conditional_eval.py` extended to contract v2
  (clauses C1–C5 of `c2-contract-v2.md`); tool selftest 99/99.
- R94-8: erratum — the round-93 mutant driver's `base_rev 191dd0ed…` names an
  uncommitted worktree state, absent from the lane; the scored blobs are
  pinned exactly (`w1/ExecReceipts/erratum-r94-8.md`; Mistake 3 in
  `corpus/lessons/round-95.md`).
- E3 entry repairs: three tagged in-file head corrections (routes R03/R12) in
  `crawl-budget-consequences.md`, `crux-keyless-check.md`,
  `kimi-subpath-audit.md`.
- Frontier step: source S479 opened (RFC Editor errata page for RFC 9110, one
  GET with receipts `w1/ScoutErrata/`); knowledge entry
  `corpus/knowledge/conditional-list-membership.md` admitted (quotes
  byte-verified, `w1/ScribeEntry/verify-quotes.py`: violations 0); SOURCES
  215 → 216 rows; census exit 0 before and after
  (`controls/census-before.txt`, `controls/census-after.txt`); mistakes mined
  (`corpus/lessons/round-95.md` `## Mistakes` 1–4); mistake-sweep for older
  rounds covered by the routed-defect ledger (§Sources & frontier).
- Integrity ruling: the wave seats (CriticClaims-67, SentinelScope-30 F1)
  caught the post-freeze instrument edit (`Amendment A`, commit `d9be693f`);
  the orchestrator ruled a post-freeze instrument edit cannot score C1 and
  offered (a) restore-and-score-on-frozen-bytes or (b) score-not-admitted;
  option (b) was chosen with option (a)'s mechanics: the frozen bytes were
  restored byte-exact at `4f443b3f`, restore-verification receipts committed
  (`controls/restore-verify-c1-selftest.txt`, `controls/restore-verify-c1-base.txt`
  — the base control reproduced line-1-identical), and no receipt produced
  with the amended counter is integrated anywhere.
- Landed-tip receipts: `controls/after-c1-final.txt`,
  `controls/after-c2-final.txt` (script `w1/ExecReceipts/run-final-receipts.sh`).
- Tools: none installed or upgraded by the lane or any seat (no pacman; the
  only network read was the scout's single errata-page GET).

## Landed changes

Every change carries a `LOG.md` entry (round-95 section) and sits under the
commit(s): instruments + frozen + controls `43cdd9fc`; freeze `8f638b59`;
restoration `4f443b3f`; integration `9cf92470`; final receipts + scorecard +
log `1fca1ad721a238411e54a67a15a08e762b566943`. SKILL.md (15 row repairs + 5 registry rows);
`scripts/conditional_eval.py` (contract v2); three knowledge-entry head
corrections; new `corpus/knowledge/conditional-list-membership.md`;
`corpus/SOURCES.md` +1 row (S479); `corpus/QUALITY.md` +4 criteria (R95-A…
R95-D); new `corpus/lessons/round-95.md`; `.ufo/waves/round-95/` wave evidence
(instruments, frozen, controls, dispatch, all 12 seat report dirs).

## Before → after measurements

- **C1 (calibration): unmet — honest stop under the frozen rule.** (Landed-tip
  receipts re-run at the final tip `1fca1ad7…`: same readings.) Base:
  `mismatches=18 E3=3 E5=15 pins=ok battery=20/20 admit=5/5 shadow=absent
  predecessor_admits=10/19 floor=4 met=false`, exit 1 at `fdd5fdbe`
  (`controls/base-c1.txt`, counting command `python3 -B
  .ufo/waves/round-95/c95_selfassess.py --root . --revision <REV>`). After:
  `mismatches=0 E1=0 E2=0 E3=0 E4=0 E5=0 pins=identity battery=20/20 admit=5/5
  shadow=absent predecessor_admits=10/19 met=false`, exit 1 at `9cf92470`
  (`controls/after-c1-final.txt`) — the zero is real, but the frozen
  instrument's entry head-8 pins fire on exactly the three repaired entries
  (`entry-content:…`), so the frozen predicate cannot certify the declared
  repair route; `met` is false with the repairs and false without them. Score
  stays 2. R95-1 routes the successor (presence pins, frozen before dispatch).
- **C2 (freshness, capability): met on the frozen counter.** Base: `hand=57/66
  generated=79/120 … met=false` exit 1 at the instruments commit
  (`controls/base-c2.txt`; counting command `python3 -B
  .ufo/waves/round-95/c95_conditional.py --root . --revision <REV> --work
  <scratch>`). After: `hand=66/66 generated=120/120 forgeries_refused=7/7
  positive=admitted mutants=40/40 survivors=none anti_table=ok population=ok
  met=true`, exit 0 at `9cf92470` and identically at `1fca1ad7…`
  (`controls/after-c2-final.txt`, shipped by the final tip). Caveats the
  round's own attacks recorded and the report carries: a memorizing
  lookup-table candidate passes the frozen counter (the anti-table digests
  hand inputs only — CriticClaims finding 5); the sandbox is escapable via an
  in-tree symlink (`abspath` not `realpath`) and `os.execv` is unaudited
  (SentinelScope x01–x03, end-to-end confirmed); the C2 counter has no
  effectful-shadow defense (R94-2 was implemented for C1 only); and the
  mutant-kill rule is circular as validation because the v2 reference moved
  (CriticClaims finding 7, both sides recorded). The landed candidate is the
  L1's genuine implementation written before scoring, with a second
  independent implementation agreeing (`w1/ExecC2V2/scoring-v2.txt`:
  `DRIVER VERDICT met=true`) and ExecMutVerify re-deriving 40/40
  (`w1/ExecMutVerify/`). Capability entered with these caveats named; score
  stays 10; the closure owns admission.

No owned axis is harmed: freshness's instrument gained ground (C2) and its
knowledge entry was admitted through the gate; calibration's score does not
move (C1 unmet); no other axis was re-scored; PROVINCE.md, SHONEN.md and the
retired-axis rows are untouched this round.

## Sources & frontier

`SOURCES: 215 → 216 rows` — counting command `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`
(before: 215 at base, receipt `controls/census-before.txt`; after: 216,
receipt `controls/census-after.txt`; both census runs exit 0; the pre-existing
W04 duplicate-URL warnings are the known rfc9110.txt class). Rows added by
tier: S479, tier A, kind dataset, scope "errata status of RFC 9110 sections
5.6/8.8/13.1", status mined, opened 2026-11-05, recheck 90d. Rows touched
old→new: none (no status/recheck/used-by change on existing rows). Frontier
rows advanced: the conditional-request instrument ground (held since r93)
extended by contract v2; the knowledge entry cites S479 + S478/S455/S034.
Sourced claim: C2's knowledge entry rests on S479, opened this round.
Assimilation: none — `merge/kake/SOURCES.append.md` was not adopted; the
collision guard re-derived this round (129 staged ids, 8 collisions,
`.ufo/waves/round-95/assimilation/collisions`; unchanged since round 92).
considerthese: proposal 3 of `considerthese/2026-11-05.md` (held-out vs
frozen divergence) admitted as QUALITY.md criterion R95-D, shown able to fail
on the round-90 divergence record; other proposals not taken.

## Trend verdicts

- **expansion: improved-bounded** — one admitted knowledge entry on
  list-membership ground the coverage map did not hold
  (`corpus/knowledge/conditional-list-membership.md`, cites mined rows S478 +
  S479), the S479 registry row (215 → 216, census exit 0 both ends), and the
  contract-v2 extension of the held conditional-request instrument.
- **quality: improved-bounded** — the corpus repairs landed (15 SKILL rows
  now name committed blobs; three provenance-trio corrections), the tool
  deepened to contract v2 (selftest 99/99) and no admitted entry failed a
  re-check; the calibration CREDIT is withheld because the frozen C1
  instrument cannot certify the route — honest-stop reporting, not a corpus
  regression.
- **discernment: improved-bounded** — the round's own attack seats and the
  orchestrator integrity flag caught the post-freeze instrument edit, the
  amendment was withdrawn from scoring rather than defended, every gate
  decision above carries its recorded admit/reject with reasons, and the
  outside closure spot-check is owed and will sample the Gate.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists,
  cited sources — evidence: `corpus/knowledge/shonen-ledger.json` box 1
  (unchanged scope; the round added 5 registry rows and 15 concrete path
  tokens under the same population rule).
- [ ] At least one end-to-end domain task executed and logged in LOG.md —
  evidence: `corpus/knowledge/shonen-ledger.json` box 2 (`status=gap`,
  unchanged; the round's instruments and audits remain lane-side
  publisher-semantics work, no live property touched).
- [~] Instructions executable by an agent without oral context — evidence:
  `corpus/knowledge/shonen-ledger.json` box 3 scope (`scripts/*.py`,
  counter paths); this round added `c95_*.py` counters with committed entry
  commands in the SKILL.md registry rows.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — evidence:
  `w1/ConnectorScope/overlaps.md` (12 overlaps opened, 8 contested, all
  reported not absorbed; PROVINCE.md untouched); box 4 ledger scope
  (`corpus/knowledge/*.md` sibling-path count unchanged by this round's one
  new entry, which cites RFC rows only).

## Wave settlement (w1-results.json, 12/12 settled, no dead seats): ScoutErrata
"S479-DRAFT admit-ready"; ExecC1Repair "REPAIR-DIFF 15 predicted-E5=0";
ExecC2V2 "C2-CANDIDATE hand=66/66" plus "DRIVER VERDICT met=true";
ExecMutVerify "MUT-VERIFY killed=40/40 survivors=none, freeze_falsifying=false";
ScribeEntry "DRAFTS 3 quotes-verified=21/21"; ReviewC1 "C1-ATTACK refused=27
false-greens=NG01,NG08,NG11" (new false-green shapes, routed R95-5; the seat
also resolved its digest-mismatch observation via w1/AMENDMENT-A.md as an
observation, not a repair license); ReviewC2 "C2-REVIEW agreement=30/30
reference-defects=R1,R2" (both unobservable in the frozen population, routed
R95-6); CriticClaims "CLAIMS C1=falsified-as-declared
C2=gaming-route-found:memorizing-candidate-passes-met" (routed R95-8; its
integrity finding 1 became the ruling above); MutC1 "MUT-C1 mutants=16
killed=15 battery_killed=15" (93.75 %, R94-7 green against round-94's 4/12);
SentinelScope "SCOPE shadows-refused=5 sandbox-escapes=[symlink-read-
outside-subject, os.execv-unaudited] writes-clean=yes" (routed R95-7);
ConnectorScope "CONNECTOR overlaps=12 contested=8" (reported, none absorbed);
ExecReceipts "RECEIPTS erratum=ready script-dryrun=rc=0". One seat-hygiene
note: ReviewC1 left its fixture clone dirs under `w1/ReviewC1/receipts/fixtures/`
(nested scratch git repos); the durable receipts were already committed, the
clones were removed as scratch hygiene and the build scripts preserved flat
(`w1/ReviewC1/receipts/build-scripts/`).

## Round shape

One v1 wave (`w1`), 12 seats under `ufo-wave-policy.json` (band 8–16):
ScoutErrata (scout), ExecC1Repair, ExecC2V2, ExecMutVerify, ExecReceipts
(executors), ScribeEntry (scribe), ReviewC1, ReviewC2 (reviewers),
CriticClaims (critic), MutC1 (mutation-tester), SentinelScope (sentinel),
ConnectorScope (connector). Attack share 5/12 ≈ 42 % ≥ 25 %; connector 1 ≤ 2;
residual calls: none. The §3 L2 floor (planner + connector + 3 executor +
scribe + scout + reviewer + critic) is met inside the wave; the L1 held the
planner seat (frozen-topology seat, never a swarm role). Dead seats:
<DEAD>. Round total: 12 seats. Routing: `task.agentModelOverrides` in
`~/.omp/agent/config.yml` (no model passed); per-seat answering models were
not pinned by the lane and are not claimed.

Stale-lane: this lane's mission is the round-95 round only (respawn-per-round
driver); it was progressing throughout (commits `43cdd9fc` … `1fca1ad721a238411e54a67a15a08e762b566943`).

Open L0 questions: the round-94 question (`kake | round-94 | Ruling wanted on
two honest unmet claims`) stands unanswered; this round adds none.

Tools installed: none (lane and seats; no pacman transaction anywhere).
