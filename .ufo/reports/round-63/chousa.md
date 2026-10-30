# chousa — round 63 report (attempt 2)

**Outcome: both declared claims landed and measured on their frozen counters; no wave was dispatched — the
orchestrator paused new campaign dispatches on 2026-10-30 — so the round's L2 floor is unmet and is reported
as such.** Lane repo `/home/vgpnk/Projects/shokunin/chousa-shokunin`, branch `master`, lane HEAD
`4a11a71d2e22f2588539b253318cc114bd79b859` (`git ls-remote origin refs/heads/master` →
`4a11a71d2e22f2588539b253318cc114bd79b859 refs/heads/master`; `jj-lane.sh state` → `ahead=0 behind=0
tracked=0 untracked=0`). Freeze commit `e5166179197b43c77b58d56b89b8e2523aed0dd3`; base
`4ece131ca826c646bd28a50802d41bc78d8a9717`. Agent id `ChousaR63`. Routing per the run map, never passed a
model. Stale-lane: respawn-per-round driver; no other mission of this lane is open. Tool installs: none
(pacman paused; nothing installed or upgraded). L0 lines: none added; the lane's open L0 questions are
unchanged (round-62 size-watch threshold `chousa | round-62`, round-57 admission ruling, round-56 cache —
all routed around, none blocking this round's work).

**Attempt inheritance.** Attempt 1 (run 11, 2026-10-28) froze claims at `62876ef9…`, landed both its claims,
and was ended by the operator's wrap-up before its wave settled; the closure never ran, the claim was
released, and the orchestrator re-dispatched the same round. Attempt 1's report (superseded in this path, in
fleet git history), its frozen `claims.md`, verdicts, instruments and wave evidence stand as its record; its
42 seat reports were re-read as this round's findings-of-record (`corpus/evidence/round63/claims-a2.md`
narrates the inheritance). Nothing was discarded: the attempt-1 wave findings ARE this round's input data.

## Work performed

Declared claims (2, frozen in `corpus/evidence/round63/claims-a2.md` before any after-measurement; freeze
commit `e5166179…`):

- **C1 — operability** (the lane's only numerically scored axis, historical 3/10, not moved): the attempt-1
  wave's routed falsifier class — zero-gate run, six judge holes, path-keyed forger, 55-line overfit oracle,
  G04/G05 false positives — is closed in a hardened battery `corpus/evidence/round63/c1-battery-v2.py`
  (29 legs: CLEAN, D01–D17, B01–B08, Z01–Z03; strict judge; seeded-random paths/environment; keyword-free
  planted words) and in the amended `tools/lane-preflight.py`. Tag `plumbing`.
- **C2 — calibration** (unmeasured axis; no numeric score invented): `tools/claims-audit.py` — a committed
  checker that flags machine-checkable false statements in a frozen claims file from a rule file; on the two
  committed errata'd claims files it flags the six mechanically-checkable of the eighteen erratum statements.
  Sourced on rows S146–S148 opened this round (S149 rejected). Tag `plumbing`.

Round shape: **0 seats** — no wave, no residual call. The orchestrator's irc of 2026-10-30: "Provider
failures now span minimax plan exhaustion, Cursor pricing, Anthropic 429, ZAI 429 and Devin permission
denial. Do not request new waves/replacement seats just to retry these failures. Finish reachable existing
documentary/defensive work and report any required unperformed work honestly; wait for existing wave handoff
before filing." and "New campaign dispatches paused pending provider availability; no route changes
authorized by this message." No `.ready` file was written; no seat died (none was spawned); the two earlier
irc directives (preserve artifacts, no exploit reproduction or external-target testing) were honored — the
round's exhibits are local fixed-output and lexical tools against the lane's own battery, no network, no
credentials, no external target.

Work items, each with evidence:

- **Protocol load** and read of attempt 1's committed findings: `CritC1JudgeHoles.md` (six judge holes +
  strict rules S1–S3, tested), `CritC1PathKeyed.md` (the `token` forger's recognition ladder and the
  keyword-free plant fix), `CritC1DiffOverfit.md` (the 55-line oracle, byte-exact in its appendix),
  `CritC1Skip.md` (zero-gate legs Z01–Z03 with expected outputs), `CritC1GateRules.md` (G04/G05 false
  positives on kagi `caught=18/18` and the kake brace shorthand, with rule fixes), `CritCalibration.md` +
  both errata (the 18 false-statement instances).
- **G04/G05 fixes** in `tools/lane-preflight.py` per the finding: G04 skips a path token whose first segment
  names nothing under root and rejects `=`-bearing tokens; G05 strips a trailing `:N`/`:N-M`, a trailing `.`
  and `)`, and expands `{a,b}` brace members. Verified: lane `PREFLIGHT=5/5`; kagi/kake/tameshi real roots
  `--only G04,G05` → `2/2` on each (was kagi G04 FAIL 1, kake G05 FAIL 1); the frozen attempt-1 battery still
  passes the amended tool in three runs (`controls/c1-on-fixed-tool.txt`).
- **Exhibits** (`corpus/evidence/round63/controls/exhibits/`): E01 the frozen reference (the zero-gate
  exit-0 tool), E02–E07 the six judge-hole lies as fixed-output probes, E08 `forge-token.py` (a committed
  re-creation of the wave's `token` forger: recognition ladder + content classification + old-rules
  fallback), E09 `overfit-oracle.py` (the wave's oracle extracted byte-exact from the committed finding,
  sha256 prefix `9ebbe9b8a8d61137`), plus three honest-output controls; runner
  `controls/run-exhibit-receipts.py`.
- **v2 battery** `c1-battery-v2.py` (frozen, digest `0fbfd076e9a6235c`): strict judge (control characters,
  id-paired contract gate names, no non-contract stdout lines, distinct summary members, usage runs name the
  bad id on stderr, zero-gate runs exit 2 with `PREFLIGHT=0/0`), legs D16/D17 (selftest broken, source text
  kept), benign legs B07/B08 (the false-positive shapes), zero legs Z01–Z03, seeded-random harness shapes,
  keyword-free plants.
- **Claims-audit checker** `tools/claims-audit.py` (frozen, digest `d48247f9c77ac1e7`): seven rule classes,
  `FLAGGED=k/n` contract, selftest (3 cases, TMPDIR fixtures + scratch git repo), probe `audit-probe.py`
  (`PROBE_FACTS=11/11`, `audit-probe.txt`); rule files `audit/audit-r62.tsv` (erratum rows 1, 13),
  `audit/audit-r63.tsv` (E1–E4), `audit/audit-a2.tsv` (this round's own claims, all PASS).
- **Pre-freeze controls**: `controls/exhibits/exhibit-v1-before.txt` (the frozen battery accepts the
  falsifier class 9/9), `controls/audit-before.txt` (checker absent at base, exit 2, measured in a
  `git archive` export of the base), `controls/c1-on-fixed-tool.txt`.
- **Frontier step**: census start/end exit 0 (`.ufo/waves/round-63/census-{start,end}-a2.txt`); rows
  S146–S149 with Gate quotes (access date 2026-10-30, local installed pages; no URL fetched); mistakes mined
  (below); assimilation none (round-42 quarantine verdicts stand; id-collision check re-run: 64 of 114
  staged ids already in the registry, `.ufo/waves/round-63/assimilation/`); considerthese unchanged
  (`CT-20261019-4` stays the operator's open L0).
- **L2 floor**: not met — no wave, per the orchestrator pause quoted above. The attack items the wave would
  have carried are routed in `corpus/lessons/round-63-attempt2.md` (a non-author re-run of every counting
  command, a mutation pass on both instruments, the source re-opens, the entailment read, the spot-check, a
  non-author forger author).
- **Slip, disclosed**: the `LOG.md` round entry was appended with a bash heredoc instead of the edit tool
  (the lane's own lesson class from round 62/63); the appended bytes were re-read against the intended text
  and the file is append-only intact. One more process slip caught and fixed mid-round: two new scripts and
  one receipt first quoted a pipeline stage's exit code instead of the command's — regenerated with
  `PIPESTATUS` capture (lesson mistake 4).

## Landed changes

| change | LOG.md entry | commit |
|---|---|---|
| claims-a2 freeze, `c1-battery-v2.py`, exhibits + honest controls + runner, `claims-audit.py`, rule files `audit-r62/r63/a2.tsv`, probe + `audit-probe.txt`, before receipts (`exhibit-v1-before.txt`, `audit-before.txt`, `c1-on-fixed-tool.txt`), planned-row amendment, census start, assimilation collision evidence | `LOG.md` `## Round 63 (attempt 2)` | `e5166179197b43c77b58d56b89b8e2523aed0dd3` |
| `tools/lane-preflight.py` G04/G05 amendments, `tools/claims-audit.py`, `corpus/knowledge/self-claim-audit-r63.md`, registry rows S146–S149, README index row, SKILL.md gate rows (r63 row amended, `claims-audit` row added), lesson `corpus/lessons/round-63-attempt2.md`, SCORECARD capability row + attempt-2 verdict, after receipts (`exhibit-v2-after.txt`, `c1v2-landed-runs.txt`, `c1v2-nulls-v2.txt`, `preflight-full-run-final.txt`, `audit-after.txt`), census end | `LOG.md` `## Round 63 (attempt 2)` | `4a11a71d2e22f2588539b253318cc114bd79b859` |

Not landed: any wave-dependent verification (the L2 floor items above); the round-62 v3-counter line
(superseded — reasons in the lesson's routed section); `RevG02.md`'s ten gate defects (routed to the next
battery round).

## Before → after measurements

All counters run on the committed bytes; `git diff --stat 4a11a71d… --` over every measured path is empty.

- **C1 operability.** Command `python3 corpus/evidence/round63/controls/run-exhibit-receipts.py --battery
  {v1,v2} --fleet <fleet> --work <dir>` and `python3 corpus/evidence/round63/c1-battery-v2.py --tool
  tools/lane-preflight.py --fleet <fleet> --work <dir>`, measured at lane tip `4a11a71d…`. **Before** (the
  frozen `c1-battery.py` over the exhibit set, `controls/exhibits/exhibit-v1-before.txt`): E01, E08, E09
  `BATTERY=PASS` in full, E02–E07 `LEG … ok` on their legs, honest controls ok — **9/9 accepted**, exit 0 on
  the three full runs. **After** (`controls/exhibits/exhibit-v2-after.txt`): all nine rejected — E01 fails
  B07/B08 + Z01–Z03, E02–E07 rejected per leg (formfeed → control character; wrong name → non-contract line;
  glued status → non-contract lines; usage gates/silence → no output lines + bad id on stderr; duplicate
  member → malformed summary), E08 and E09 `BATTERY=FAIL` in full (D16/D17 + B07/B08 + Z) — and the landed
  tool `CLEAN=1/1 DEFECTS=17/17 BENIGN=8/8 ZERO=3/3 BATTERY=PASS` exit 0 in three fresh-seed runs
  (`controls/c1v2-landed-runs.txt`), nulls `BATTERY=FAIL` exit 1 (`controls/c1v2-nulls-v2.txt`), full
  preflight `PREFLIGHT=8/8 FAILED=none ENV=none SKIPPED=none` exit 0
  (`controls/preflight-full-run-final.txt`). Verdict: **improved** on the frozen predicate.
- **C2 calibration.** Commands `python3 tools/claims-audit.py --claims <claims> --audit <rules> --root .`,
  `--selftest`, and `python3 corpus/evidence/round63/audit-probe.py`, measured at lane tip `4a11a71d…`.
  **Before**: tool absent at the base — both commands exit 2 in a `git archive` export of `4ece131c…`
  (`controls/audit-before.txt`). **After**: `FLAGGED=2/2 AUDIT=FAIL` exit 1 (round-62 claims, erratum rows 1
  and 13 — the seat count vs the 66-item spec; S138 absent from `## Leads` at the round-62 base revision) and
  `FLAGGED=4/4 AUDIT=FAIL` exit 1 (attempt-1 claims E1–E4 — controls added in the freeze commit itself; the
  "header file" that is a man page; the heading quote that does not occur; the lane-wide claim swept only in
  `corpus/knowledge`), `AUDIT_SELFTEST=PASS (3 cases)` exit 0, `PROBE_FACTS=11/11` exit 0, and this round's
  own claims `FLAGGED=0/4 AUDIT=PASS` exit 0 pre-freeze (`controls/audit-after.txt`,
  `corpus/evidence/round63/audit-a2-result.txt`). Verdict: **improved** on the frozen predicate.

## Sources & frontier

Census command `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root
/home/vgpnk/Projects/shokunin chousa`:

- **Start** (`.ufo/waves/round-63/census-start-a2.txt`), exit 0: five pre-existing `W04` duplicate-url
  warnings (S051, S053, S073, S074, S075), `chousa ok`. **End** (`census-end-a2.txt`), exit 0, `chousa ok`,
  the same five warnings, none new.
- Rows before → after, `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`: **145 → 149**;
  malformed (NF≠13) 0; tiers A/B/C 113/25/7 → 116/26/7; status mined/queued/rejected 118/19/8 → 121/19/9.
- Rows added by tier: A 3 (S146 `grep(1)`, grep 3.12-2, rendered line 29; S147 `git-log(1)`, git 2.56.0-1,
  rendered line 1376; S149 `file(1)` rejected); B 1 (S148 the audit probe output, own-work).
- Rows touched old → new: none. Frontier rows advanced: none (the topic was not in `## Leads`).
- Sourced claim: C2's entry `corpus/knowledge/self-claim-audit-r63.md` cites S146, S147, S148, each opened
  2026-10-30; the lesson's `## Gate` records each row's file, access date and located ≤25-word quote, 3
  admits and 1 reject; the non-author spot-check is asked to re-open admit S147 and reject S149. Local files
  only, no URL fetched.
- Assimilation: none — the wave-4 quarantine duty was discharged in round 42 (24-row slice verdicted, zero
  rows present, `corpus/evidence/round42/quarantine-verdicts.tsv`); adoption stays closed for a second,
  independent reason: the id-collision check found **64 of the staged package's 114 staged ids already
  occupied** in the lane registry (`.ufo/waves/round-63/assimilation/{reg-ids,staged-ids,collisions}` —
  reg 145 rows, staged 114, collisions 64). Any future adoption must renumber staged ids by document in
  scratch.
- considerthese: `CT-20261019-4` (SKILL.md size-watch threshold) stays an open operator question (L0 line of
  round 62, unchanged); no new proposal mined this round.
- Mistakes mined: four rows in `corpus/lessons/round-63-attempt2.md` `## Mistakes`, each with class,
  evidence, captured-by and fix; red-before shown for all four (the first v2 receipt run, the probe bring-up
  fixture, the first exhibit/probe receipts, the superseded rc lines).

## Trend verdicts

- **expansion — improved (narrowly).** One admitted entry on ground `corpus/knowledge` did not hold
  (`grep -rl 'claims-audit' corpus/knowledge` printed nothing at the base), citing three rows opened this
  round; one capability row (Claims audit) and one SKILL.md gate registration entered the repertoire.
- **quality — improved (narrowly).** The demonstrated false-positive class (G04/G05 on real sibling files)
  is fixed and pinned as benign legs; the attempt-1 battery's demonstrated acceptance of the falsifier class
  is closed by a measured v2 (9/9 exhibits rejected, honest controls kept, nulls still failing); no admitted
  entry was found false.
- **discernment — unchanged.** The non-author spot-check named in the lesson (S147 admit, S149 reject) and
  the entry's entailment read could not run — the wave that carries non-author judgment was not dispatched;
  the claims rest on frozen counters and committed controls, and the outside check is routed to the next
  round with the attack items.

**L2 floor: unmet this round** (0 seats; orchestrator dispatch pause, quoted above). Round total 0 seats;
wave sizes: none; dead seats: none; residual calls: none.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — the amended
  `chousa lane-preflight (r63)` gate row and the new `claims-audit` gate row (SKILL.md lines 154–155) cite
  the v2 battery, the exhibits, the rule files and the receipts; lane assertion, no non-author verifier named.
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md` `## Round 63 (attempt 2)`:
  the attempt-1 findings re-read, the falsifier class exhibited against both batteries, the erratum
  statements mechanised into rule files and flagged 6/6; lane assertion, no non-author verifier named.
- [~] Instructions executable by an agent without oral context — the four C1/C2 counting commands and their
  receipts are committed (`claims-a2.md` §Frozen instruments; `controls/audit-after.txt`;
  `controls/exhibits/exhibit-v2-after.txt`); lane assertion, no non-author verifier named.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — sibling roots were read only (the G04/G05
  verification ran the tool read-only on kagi/kake/tameshi; no sibling file written); PROVINCE.md unchanged;
  lane assertion, no non-author verifier named.

## Open claims and routed work for the next round

Carried in `corpus/lessons/round-63-attempt2.md` `## Routed to the next round`: the non-author run of every
counting command and the S147/S149 spot-check; a mutation pass on `c1-battery-v2.py` and `claims-audit.py`
(both are L1-authored and unattacked this round); a non-author forger author for the v2 exhibit set;
`RevG02.md`'s ten gate defects; an existence-assert rule for `__file__`-derived paths (lesson mistake 3);
the round-62 v3-counter line if the forger-armory thread continues; `CT-20261019-4` stays with the operator.
No L0 question was added this round.
