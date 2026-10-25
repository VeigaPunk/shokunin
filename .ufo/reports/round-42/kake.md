# kake round 42 — report (attempt 2 of 2 this session)

Lane: kake-shokunin. Base: `1ef7a0e9` (round 41, rejected-harmed). Lane HEAD at report:
`5949e66ffe803859372adc975dd7392f0f07d626` (round-42 verdict commit; parent `68586658268c…`).
Attempt 1 of round 42 (`KakeR42`) died with the phase-4 orchestrator after wave 2 returned, no verdict or
commit; this attempt inherited its leftovers per addendum §5, re-verified each, discarded none.

## Work performed

Declared claims (1, per the round prompt's prefer-2 sizing rule — one claim was what the repair allowed):

1. **C1 — operability: runnable cost of the held round-41 URL rule** (`scripts/sitemap_audit.py` URL
   section; the round-41 tool `50287ac6…` kept, its zone-id tightening declared, its cost repriced).
   Predicate (frozen at declaration `1e1da697`, = `PREDICATE` in `c42_count_v3.py` = every receipt's
   `predicate` field): *met: the tool's exit code and output equal the round-41 tool's on every generated
   run, and its median CPU time on each of the five timing shapes is at most 2.0 times the round-40 tool's.*
   Counting command: `python3 -B .ufo/waves/round-42/c42_count_v3.py --root . --revision <rev> --out <receipt>`
   (counter sha256 `ce2d5a0c…`; exit 0 met / 1 not met / 2 cannot evaluate). C1 also rests on a source row
   opened this round: the zone-id disposition is grounded in S124 (RFC 9844), satisfying the frontier
   step's sourced-claim item. **Verdict: NOT MET** — see below.

Work items:

- Counter program v1 (`7bfc32c5…`), rejected pre-freeze (do-nothing met draft 1; nine wave-1 controls met
  v1 with witnesses or a forged timing line) → v2 (`01d3fb8d…`) → **v3 (`ce2d5a0c…`)** frozen before the
  build was scored: run E (every ASCII unit, percent form, boundary code point and Unicode look-alike in
  eleven slots), non-dumpable bwrap runner, append-only timing file, `os.urandom` scoring seeds.
  Evidence: `SCORECARD.md` "Round 42 — counter v2/v3 replaces…"; receipts `verification/{pre,pre-v2,v3probe,w1v3}/`.
- Wave 1 (`kake-r42-w1`, 33 seats, 0 dead, 0 refused): 86 control tools re-scored under v3 (3 meet, all
  behaviour-equal by the frozen 31,415-value differential); build `020bc457` chosen pre-scoring
  (`ExecBuildIndependent`'s byte-table scanner; `ExecBuildRegex` rejected, fails Python 3.10) and scored
  met ×3. Evidence: `w1-dispatch-log.txt`, `score_v3.sh`, `verification/build/`, `equivalence/`.
- Wave 2 (`kake-r42-w2`, 34 seats, 0 dead, 0 refused): attacked the scored build; integrated by this
  attempt. Evidence: `w2/` (34 reports), L1 re-scores `verification/w2v3/L1-*.json`.
- Verdict landing: SCORECARD "wave-2 attack results and verdict"; lesson Mistakes 5–6; registry repairs
  S126–S128 + used-by old→new logs; `census-after.txt`. Commits `68586658268c…`, `5949e66ffe…`.

## Landed changes

- `SCORECARD.md` — wave-2 results, kill-rule verdict, routed defects 1–7, trend lines
  (`SCORECARD.md`, commit `68586658268c…`; LOG.md entry "Round 42 attempt 2").
- `corpus/lessons/round-42.md` — Gate rows for S126–S128; used-by old→new for S123/S124; attempt-2
  correction of the S117–S119 used-by shorthand; Mistakes 5 (counter coverage: port length, repetition
  classes) and 6 (freeze provenance) (`68586658268c…`).
- `corpus/SOURCES.md` — S123/S124 `used-by` repairs (rule-2 cells, logged); S126–S128 superseding rows
  (`68586658268c…`).
- `scripts/sitemap_audit.py` build `020bc457` (tool `914ebdee…`) + selftest (235 fixtures, `bebd834b…`) —
  landed by attempt 1 (`721310b1`, in lane history); unchanged by attempt 2.
- `.ufo/waves/round-42/` — wave specs, dispatch logs, registries, counter v1–v3, controls, equivalence
  differential, verification receipts incl. `w2v3/`, `census-after.txt`; plus the 1.3 MB wave-1 control
  evidence file (`5949e66ffe…`).

## Before → after measurements

- C1 counting command (frozen above), measured against the round-41 tool at base (`1ef7a0e9`): **before —
  not met** (equality 10/10 but T1 4.17–4.28, T2 2.73–2.83, T5 7.81–7.81 × the round-40 tool;
  `verification/v3probe/donothing-{1,2}.json`). Build `020bc457`: **after — met on the counter's own
  receipts** (three random seeds; ratios T1 0.98–1.06, T2 1.28–1.72, T3 1.39, T4 1.24–1.28, T5 1.09–1.17;
  `verification/build/c1-v3-020bc457-{1,2,3}.json`; reproduced by wave-2 `RerunBuildA/B`).
  **Round verdict: NOT MET** — the frozen kill rule (2) fires: four live-seat controls meet v3 with
  witnesses (`MutBuildAuthority` M8-port-five-digits; `CtlFreshCache` v1_casefold, v2_prefix32,
  v4_hosttable), each re-scored met by the L1 under fresh seeds (`verification/w2v3/L1-*.json`). The
  miss is reported, not relabelled; the build's behaviour-equality itself is intact (wave-2 differentials
  ~7.2M values, 0 mismatches; harm H1–H5 re-verified — `w2/ReviewBuildFinal.md`,
  `w2/ReviewBuildDifferential.md`, `w2/ReviewHarm*.md`, `w2/ReviewInfoBuild.md`).
- Frontier census: `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kake` —
  before: exit 0 (`.ufo/waves/round-42/census-before.txt`); after: exit 0 (`census-after.txt`).
  Rows 128 → 131; mined +1 net of supersessions (S126–S128; S125/S128 rejections).

## Sources & frontier

`corpus/SOURCES.md` rows before → after: 128 → 131 (census command above, exit 0 both ends). Added by
tier: A +3 (S126 re docs, S127/S128 spec). Touched old→new (rule-2-permitted cells only, logged in
`corpus/lessons/round-42.md`): S123 `used-by` `SCORECARD.md, corpus/lessons/round-42.md` →
`corpus/lessons/round-42.md`; S124 `used-by` `SCORECARD.md, corpus/lessons/round-42.md` →
`SKILL.md, corpus/lessons/round-42.md`. Frontier rows advanced: S123→S126 (teaches wording + Gate
decision corrected per `ReopenPythonRe`), S124→S127 (zone-id grounding per `ReopenRFC9844`),
S125→S128 (contract-required `flip:` added per `ReviewSourcesRule2`); all three re-opened by wave-2
seats 2026-10-23T12:13Z, bytes equal to the 11:24:53Z retentions. Rejections: S125 and S128 stay
rejected (RFC 6874 obsoleted by RFC 9844). Mined mistakes: 6 in `corpus/lessons/round-42.md`
(round-41 harm rule; counter-too-weak ×3; round-41 rule-2 edits; L1 clock read; counter coverage gaps;
freeze provenance). Sourced claim: C1's zone-id disposition cites S124.

## Trend verdicts

- **expansion: unchanged** — no capability enters the table (C1 not met); registry grew within the
  existing SOURCES capability only.
- **quality: harmed-bound** — the claimed improvement does not verify (kill rule 2), which bounds the
  round's quality move; within it, real knowledge landed: the counter's coverage gaps (port length,
  repetition classes) are named with able-to-fail receipts, the build's behaviour-equality is established
  on ~7.2M differential values, and the registry's round-41 rule-2 breaches are repaired.
- **discernment: improved (author-side; outside spot-check owed)** — an honest negative result reported
  against the lane's own interest; four meeting controls self-reported with witnesses instead of
  relabelled; freeze-provenance defect disclosed rather than repaired post hoc.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — round-42
  scanner/zone-id sections committed at `721310b1`; wave-2 `ReviewCommentFix` verified the comment against
  SKILL.md and observed behaviour (HOLDS).
- [ ] At least one end-to-end domain task executed and logged in LOG.md — not this round: C1 (the end-to-end
  repricing) is NOT MET; the LOG records the negative result honestly.
- [~] Instructions executable by an agent without oral context — selftest 235/235 on build and round-41
  tool under Python 3.14.8 and 3.10.22 (`verification/harm/selftest-*.txt`; wave-2 `ReviewHarmSelftest`).
- [~] No cross-domain bleed (PROVINCE.md still accurate) — PROVINCE untouched; wave-2 `ScoutSiblingCost`
  scanned all sibling repos: no lane copied the round-41 regex or its cost.

## Round shape and waves

Shape: **two v1 waves** (policy v1 band 32–64), total 67 seats ≤ 128. Wave 1 build (33 seats: 10
executor, 9 mutation-tester, 3 reviewer, 3 critic, 3 scout, 3 scribe, 1 sentinel, 1 connector; the §3
planner seat is the L1 per the frozen-topology ruling, recorded here; 0 dead, 0 refused) — recon, counter
drafting, control building/scoring, first falsifiers. Wave 2 falsify (34 seats: 15 reviewer, 7
mutation-tester, 5 scout, 4 executor, 3 critic — 73.5% attack; 0 dead, 0 refused) — dispatched after
wave 1 returned, against the scored build. Round total: **67 seats**, no residual call (the verdict is
determined by the returned seats; further seats would be padding). No seat was dispatched by attempt 2;
per the mid-flight orchestrator directive, any further seat would have routed through the orchestrator —
none was needed. Mid-round orchestrator directive noted: no new dispatches from the L1 session; both
waves were already running/returned from attempt 1, so the directive changed nothing this round.

## Stale-lane and extras

- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
- Tool installs this attempt: none (host `jq`, `python3` 3.14.8, uv-managed Python 3.10.22 already
  present; attempt 1 installed nothing new either).
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` — no untracked fleet-root file
  names kake round 42 (wave-2 `ReviewMisroot` agrees; the fleet-root junk files are not ours, untouched).
- Dead seats: none across both waves (w1: 33/33 returned; w2: 34/34 returned). Attempt 1's L1 process died
  with the phase-4 orchestrator (~09:30–13:00 -03 window); its in-repo work is committed above.
- Open L0 questions: none appended this attempt. The freeze-provenance disposition (routed defect 1) and
  the exploratory-presentation option recommended by `w2/CriticKillRule.md` are left to the canonical
  closure rather than the L0 channel.

## Admission note

Every claim verifies or fails on its frozen counter — here: C1 fails it (kill rule 2, four witnessed
meeting controls). No axis is observed harmed on the exercised checks (H1–H5 hold with the disclosed
scope qualifications); round 41 stays rejected-harmed and its tool not admitted. Driver completion is not
admission; independent non-author verification remains required.
