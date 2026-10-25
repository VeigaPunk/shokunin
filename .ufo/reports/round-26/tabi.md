# tabi — round 26 report (hyaku run 6, attempt 1)

Lane HEAD: `f47eb2d452f532e2215fb2075c79f31db1ed482d` (round-26 wrap-up
landing; measurement/evidence commit `0c666adc217685e1ece2af8596b732b303a3b15c`;
baseline `4ad4c77eed78bca1a149e65a7ec6a84b5f71c925`).

**Round shape (binding context).** The orchestrator wrapped up the run
mid-round: "start no new waves … land NOW with what you have". No wave was
dispatched. Per the run-6 amendment a round whose swarm never ran gets no
falsification credit; all three frozen claims are recorded **failed (not
executed)** below, and the landed work is the frozen claims, the
policy-validated wave-1 spec, the routed-defect resolutions and the honest
records. The frozen `claims.json` is the resumption point for a fresh round.

## Work performed

Declared claims (1–3) and target axes/capability:

- **C1 — calibration** (routed round-25 LOG next-iteration (b)): extend
  `check-selfassessment.mjs` class m1 to LOG.md round entries.
- **C2 — depth** (lowest non-retired tie at 8): commit decoded S106 source
  evidence + gate it (routed round-25 closure defect 4).
- **C3 — coverage**: assimilate one staged theme (redirect/Retry-After) under
  addendum §10.

Work items:

- Froze the three claims before data — `.ufo/waves/round-26/claims.json`
  (`frozenBeforeData: true`, empty `revisions`), committed at `0c666adc`.
- Recorded the census before — `.ufo/waves/round-26/census-before.txt`
  (exit 0, 106 rows, 16 standing W04 warnings).
- Built and policy-validated wave 1 — `.ufo/waves/round-26/gen-w1.mjs`,
  `w1-spec.json` (34 seats: 9 scout, 8 executor, 4 scribe, 4 reviewer, 4
  critic, 1 connector, 1 revenger, 1 sentinel, 1 mutation-tester, 1
  simplifier), `w1-dispatch.json`; validator exit 0 under
  `ufo-wave-policy.json` (`w1-validate.err` empty). **Never dispatched
  (wrap-up).**
- Resolved routed defect 4 (S106 decoded evidence) — fetched
  `…content_features.cc?format=TEXT` (base64 transfer, encoded 98,604 B,
  sha256 `f17347b2…`), decoded to `corpus/evidence/round-26/sources/
  content-features-154.0.8037.97.cc` (73,952 B / 1,624 lines, sha256
  `9b93fe64…`), anchor `BASE_FEATURE(kBackForwardCache,
  base::FEATURE_ENABLED_BY_DEFAULT);` at line 187 (comment line 186, token
  unique in file) — matches the S106 registry row's anchor; receipt
  `corpus/evidence/round-26/sources/s106.json`. Commands: `base64 -d`,
  `sha256sum`, `grep -n` (all in the receipt).
- Resolved routed defect 3 (untracked `.ufo/waves/round-25/w2/`) — committed
  `swarm-registry.json` as round-25 wave evidence (validator-produced roster
  of the validated-but-undispatched W2 per the round-25 closure erratum).
- Verified the C1 correction's oracle by hand: `node
  scripts/round-evidence-audit.mjs --selftest` → `cases: 13`, exit 0 — so
  LOG.md:1664's `12/12` is stale; the append-only supersession block landed in
  the LOG round-26 entry.
- Wrote the round records — `corpus/lessons/round-26.md` (Gate + two mined
  mistakes), LOG.md round-26 entry, SCORECARD.md round-26 blocks.
- No tool installs this round.

## Landed changes

All in commit `0c666adc217685e1ece2af8596b732b303a3b15c` (+ `f47eb2d4` for the
census-after receipt), each tied to its LOG.md round-26 entry:

- `.ufo/waves/round-25/w2/swarm-registry.json` — routed defect 3 (was the
  only untracked leftover; `git status --porcelain` now clean).
- `.ufo/waves/round-26/{claims.json,census-before.txt,gen-w1.mjs,w1-spec.json,
  w1-dispatch.json,w1-validate.err,s106-encoded.bin}` — frozen claims +
  validated wave evidence.
- `corpus/evidence/round-26/sources/{content-features-154.0.8037.97.cc,
  s106.json}` — routed defect 4.
- `corpus/lessons/round-26.md` — lesson (Gate, Mistakes M1/M2, Corrections).
- `LOG.md`, `SCORECARD.md` — append-only round-26 records.
- `.ufo/waves/round-26/census-after.txt` — `f47eb2d4`.

## Before → after measurements

Per claim — all three **failed (not executed)**; the frozen counting commands
were never satisfiable because the instruments were never built (0-seat
round). What was measured during wrap-up:

- **C1 (calibration)**: frozen counter `node scripts/check-selfassessment.mjs
  --rev <REV> --json` field `mismatches`, target ≥1 at baseline → 0 at tip.
  Measured instead: the unextended counter at baseline → mismatches=0,
  selftest cases=13 (`.ufo/waves/round-26/` spec; LOG entry) — the LOG window
  is uncovered, which is the claim's motivation, not its verification. The
  append-only LOG correction (superseding :1664, oracle `cases: 13` measured
  by the L1, exit 0) landed as evidence-of-record. **Verdict: failed — not
  executed.**
- **C2 (depth)**: frozen counter `node scripts/check-s106-evidence.mjs --rev
  <REV> --json` field `valid`, target 0 → true. Measured instead: `git ls-tree
  -r --name-only 4ad4c77 -- corpus/evidence/round-26` → empty (before);
  evidence bytes + receipt committed (after) — but the frozen counter does not
  exist, so the predicate is not re-derivable. **Verdict: failed — not
  executed** (routed evidence landed regardless).
- **C3 (coverage)**: `git grep -lE '^source: S107 ' 4ad4c77 -- corpus/knowledge
  | wc -l` → 0 (before); at tip → 0 (after) — nothing appended; registry 106 →
  106, census exit 0 both ends. **Verdict: failed — not executed.**

## Sources & frontier

Counting command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh
validate --root /home/vgpnk/Projects/shokunin tabi` — **before**: exit 0, 106
rows (`.ufo/waves/round-26/census-before.txt`); **after**: exit 0, 106 rows
(`.ufo/waves/round-26/census-after.txt`). Rows added by tier: none (A/B/C
unchanged); rows touched old→new: none; frontier rows advanced: none.
Rows opened this round: S106 re-opened (decoded fetch, receipt
`corpus/evidence/round-26/sources/s106.json`) — recorded in the lesson Gate as
an admit-as-evidence; no registry row added or changed. Assimilation:
**none executed** — the staged candidates (S124/S125/S142 theme) were not
re-grounded (no seats); the lesson pre-notes S125 as a likely refuse (its
document already stands as S102 — within-scope duplicate URL) and S142 as a
likely refuse (overlap), both unadjudicated until a round with seats runs the
§10 machinery. Quarantine slice (38 tabi rows): closed since round 22,
verdicts carried, nothing adopted. `considerthese/`: no such directory in this
lane. One mined mistake-family entry: M2 (base64 `?format=TEXT` misread) with
its fix partially landed (evidence committed; QUALITY criterion 67 proposed,
not appended — no review seat).

## Trend verdicts

- **expansion — unchanged.** No knowledge entry admitted, no registry row
  added (106 → 106); the only corpus growth is evidence-of-record for a
  routed defect (S106 bytes), not new domain ground.
- **quality — unprovable-but-better (bounded, author-side).** The S106 row's
  anchor is now backed by committed decoded bytes with a sha256 receipt (the
  r25 closure reader's "Disagree" is answered by bytes, not prose), and the
  stale LOG tally has an append-only correction. No counter verifies either
  mechanically; no non-author reviewer judged them. Reported honestly as
  author-side bounded improvement, not a measured trend.
- **discernment — unchanged.** The round's honest disposition (three claims
  failed rather than prettified) is calibration of record, but no outside
  admit/reject sample exists this round; nothing is promoted.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — unchanged this round; pointer `SKILL.md` §Approval table (`:697`), §Evidence ladder; no non-author verifier new this round.
- [~] At least one end-to-end domain task executed and logged in LOG.md — unchanged this round (last: r25 bfcache journey, `corpus/evidence/round-25/bfcache/`); pointer stands.
- [~] Instructions executable by an agent without oral context — unchanged this round; pointer `corpus/knowledge/executor-test-sufficiency.md` §0, §4.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — unchanged this round; `PROVINCE.md:3-19` refusal routes held; nothing absorbed (sibling scan not run — no connector seat; reported, not asserted).

## Stale-lane

Respawn-per-round driver; no other mission of this lane is open. Next round:
re-dispatch the frozen round-26 claims unchanged from
`.ufo/waves/round-26/claims.json` (resumption point), honoring the wrap-up
disposition recorded in SCORECARD.md.

## Open items (owed, named)

(a) `scripts/report-contract.mjs` (specced as ExecReportPreflight) to
mechanize the M1 report-path fix; (b) QUALITY criterion 67 (decoded-source
evidence for base64 `?format=TEXT` rows), appended with a review seat's read;
(c) C3 assimilation with full §10 machinery incl. the indented-fixture
collision proof; (d) the C1/C2 instruments per the frozen claims.

No L0 questions this round.
