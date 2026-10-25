# kama — round 29 report (attempt 2, 2026-10-23)

Lane: kama (local model serving and endpoint health; axes operability + calibration). Round shape:
**one v2 wave** — `round-29-w2`, 64 seats, policy `/home/vgpnk/Projects/shokunin/scripts/hyaku/ufo-wave-policy-v2.json`
(band 64–128, attack 42/64 = 65.6%: reviewer 29, critic 6, mutation-tester 7; executor 6, scout 10,
scribe 2, connector 1, sentinel 1, revenger 1, simplifier 1). Dispatched by the orchestrator as one
batched task call per the operator's mid-flight directive (zero seats dispatched from the L1 session).
Wave-slot grant line: `granted lane=kama wave=round-29-w2 seats=64 live=21 pending=65 cap=256`.
First send: 20 live, 44 queued behind the host per-session job limit, all 64 dispatched inline as
seats settled. Residual call: none (all seats are in the single wave). Round total: 64 seats.
Dead seats: none — 64/64 returned. Refusals: none by the L1 (the wave went through the orchestrator).

## Work performed

Declared claims (1–3 allowed): **one claim — C1 (measured, calibration)**, inherited from round-29
attempt 1, independently re-verified by this attempt before any integration:

- **C1 — self-assessment statements checked at their writing revision; the 11 base mismatches now
  carry correction rows with the counter's observed values.** Axis: calibration (tied-lowest assigned
  axis at 7, non-retired; stagnation nudge INACTIVE per CriticStagnation). Surface: the lane's
  self-assessment evidence record (SCORECARD.md/SHONEN.md statements at the commit that wrote each
  line). One-claim rationale: the freeze, 14 pre-data controls and data all predate this attempt;
  the standing "prefer 2 claims" is prefer-not-require, and a second claim would have required a new
  freeze the remaining budget could not honestly complete. The named corpus move riding with C1:
  new knowledge entry `corpus/knowledge/self-assessment-at-writing.md` (ground previously uncovered
  — no lane instrument checked SCORECARD/SHONEN statements at their writing revision).

Work items (each with evidence):

- Inherited attempt-1 state per addendum §5/§6: three pushed commits — `827d1365` freeze
  (counter + preregistration + base receipt), `35b90184` (14 pre-data control receipts),
  `513eba3b` (11 correction rows + mined receipts + echo-repair receipt + prereg-time-check fix).
  Reused after re-verification: the freeze, controls, data, and all narrative files (named below).
  Discarded: `.ufo/waves/round-29/__pycache__/` only (SimplifierLeftovers).
- Independent pre-integration re-verification (L1, no seat): fresh clone at `513eba3b`, frozen
  counter sha256 `fe11d599d064f5749c829394fc813f43921de2f9903e41c7217e3daa4b647383`, receipt
  `statements 69 mismatched_at_base 11 append_only True valid_corrections 11 false_corrections 0
  unresolved 0 met True tip 513eba3ba51a` (this session 15:13 -03).
- Wave w2 verification (64 seats, `.ufo/waves/round-29/w2/`, tally in `w2/INTEGRATION.md`):
  11/11 per-row confirmations (non-counter hand derivation), both closest controls reproduced
  exactly (CtlSourceBounds 9/7/9, CtlBaseTree 6/4/9), frozen bytes verified untampered across all
  three commits, 9+ counter mutants killed, receipts byte-identical under `env -i`, controls
  SUMMARY recomputed 14/14, no-harm structural check clean, sibling-overlap scan (kaidoku class-T
  prior art — reported, not absorbed), scope audit (SentinelScope findings disclosed), timeline
  reconstruction (RevengerPrereg — no post-data shaping; one prospective citation disclosed).
- Integration fixes applied pre-landing (all verified by a dress rehearsal in a scratch clone:
  r29 receipt unchanged 69/11/append True/11 valid/0 false/0 unresolved/met True; next-base
  simulation plants zero new false statements): S174/S176 located-quote paraphrases replaced with
  seat-verified verbatim page text; four P-token cells in the correction table rewritten
  (`MISSION.md:29` → `MISSION.md` line 29 and three siblings — RerunCounter D1: the verbatim tokens
  would otherwise plant 4 new false P statements at the next extraction base); SHONEN line 8
  `accepted-bad = 6` → `accepted-bad is 6` (RerunCounter D2: removes a newly introduced class-Q
  span false at its writing revision); A1 sub-second authoring record (edit 08:37:23.720Z, result
  .732Z) added to SCORECARD + LOG; lesson timestamps aligned to git metadata (freeze 10:55:43Z,
  controls 11:11:28Z, w1 dispatch 12:02:03.361941Z, data 12:02:52Z); lesson "3 surviving mutants"
  corrected to 2 per `mined/survivor-recheck.out`; `mined/patched-513eba3b.out` added (the tool
  correctly still flags the frozen round-28 preregistration at 513eba3b — exit 1 by design);
  controls SUMMARY erratum appended (verdict receipts vs seat-disclosed DIAGNOSTIC copies);
  KQ38 tightened (committed pre-data control receipts; L1-dispatched control call; lane-absolute
  citation paths); knowledge entry H-class description tightened to the parser allowlist; README
  coverage-map row + frontier disposition added; three dangling relative citations made
  lane-absolute; tool docstring/help updated to the three accepted time forms; end-of-round census
  receipt `.ufo/waves/round-29/final/census-end.out`.
- Round-28 spot-check routed repairs (items 1–9, `corpus/lessons/round-28-verifier-spotcheck.md`):
  KQ38 criterion; A1 time record; timing transcript excerpts (sha256-verified); gate-registry
  repair (ExecGateRegistryV2); instrument-registry kinds; echo-recheck exit-2 receipt; lesson Gate
  quote-count correction (8/34 not verbatim); report wording (this report states the round-28 A1
  counter was also met by a post-data declared-bounds projection 20/20); SHONEN box-2 wording.
- Mined mistake (`corpus/lessons/round-29.md` §Mistakes): the lane's own false-timestamp
  falsifier missed the round-28 A1 misdate; `tools/prereg-time-check.py` now reads `~HH:MMZ` and
  ` HH:MMZ` forms; fix shown able to fail (flags 75b78bb4 exit 1, passes d8bf1804 and the current
  tree, selftest 13 cases PASS + aggregate).
- Misroot sweep (L1, fleet root, before this report): `git -C /home/vgpnk/Projects/shokunin
  status --porcelain` — zero kama round-29 artifacts at the fleet root (MisrootSweep seat agreed);
  no fleet-root copies made or deleted by this lane.

## Landed changes

Attempt-1 commits (pushed, inherited and re-verified): `827d1365` freeze; `35b90184` controls;
`513eba3b` C1 data — each tied to LOG.md §Round 29 (attempt-1 entry). Attempt-2 integration commit:
**`6de225c289b7682bf280cffb4a07de3fb7d1275c`** (LOG.md §Round 29 attempt 2 entry; SCORECARD round-29 section;
SHONEN.md line 8; `corpus/QUALITY.md` KQ38/KQ39; `corpus/SOURCES.md` S174–S177;
`corpus/README.md`; `corpus/lessons/round-29.md`; `corpus/knowledge/self-assessment-at-writing.md`;
`tools/prereg-time-check.py`; `.ufo/waves/round-29/{final,mined,w1,w2,controls/SUMMARY.md}`).
Follow-up evidence commit `227dd1eeff955a2ff2471cc2bc7f6eefecda6055` carries the final tip
receipts (`final/c1-6de225c2.out/.json`).

## Before → after measurements

C1 (measured, calibration), counting command (frozen counter, sha256 `fe11d599…7383`):

```
/usr/bin/python3 .ufo/waves/round-29/count-c1.py --repo <fresh clone of the lane remote> \
  --tip 513eba3ba51a142c9936553e3a85918345eb5c4c --out <receipt.json>
```

- Before (base `2aa46e24`, `final`-path `.ufo/waves/round-29/before/c1-base.out`):
  `statements 69 mismatched_at_base 11 append_only True valid_corrections 0 false_corrections 0
  unresolved 11 met False tip 2aa46e2481d2`.
- After (measured commit `513eba3ba51a142c9936553e3a85918345eb5c4c`,
  `.ufo/waves/round-29/final/c1-513eba3b.out`): `statements 69 mismatched_at_base 11
  append_only True valid_corrections 11 false_corrections 0 unresolved 0 met True tip 513eba3ba51a`.
- Do-nothing/control state: all 14 pre-data controls fail the target (`35b90184`,
  `.ufo/waves/round-29/controls/SUMMARY.md`); closest shortcuts: text-only prediction unresolved 9,
  base-tree check unresolved 9. The reference policy (recording the frozen counter's observed
  values — the claimed work) meets it by design.
- Round-end re-verification at the integration tip: same fields `met True` — receipt
  `.ufo/waves/round-29/final/c1-6de225c2.out` at `6de225c289b7682bf280cffb4a07de3fb7d1275c`
  (`statements 69 mismatched_at_base 11 append_only True valid_corrections 11 false_corrections 0
  unresolved 0 met True tip 6de225c289b7`, fresh clone of the pushed remote; committed in
  `227dd1eeff955a2ff2471cc2bc7f6eefecda6055`; the preregistration's `--tip refs/heads/master`
  form resolves only on a remote clone whose master is at the measured commit — pin the explicit
  revision; exit code signals execution, not the verdict).
- Bounded reading (CriticAxisFit/ClaimShape, accepted): the 11 failures are evidence-resolution
  defects (4 pointers that do not resolve as written, 7 quoted outputs not retained verbatim
  outside the self-report files); they do not prove the underlying judgments were wrong.
  Calibration score 7 → 7 (no self-promotion; closure rules).

## Sources & frontier

Command (start and end): `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root
/home/vgpnk/Projects/shokunin kama`. Start: exit 0, 173 registry rows
(`.ufo/waves/round-29/before/census-start.out`, committed with the freeze). End: **exit 0, 177
rows** (`.ufo/waves/round-29/final/census-end.out`; 83 pre-existing W04 duplicate-URL warnings, no
new warning classes). Rows added: **S174–S177 (4, all tier A, kind docs, status mined)** — git-blame,
git-merge-base, git-grep+gitglossary, pretty-formats; each opened this round, located quotes
recorded in the lesson §Gate (S174/S176 repaired to verbatim pre-landing after SrcS174/SrcS176 seat
findings). Rows touched old→new: S177 status `queued → mined`, used-by `— → corpus/knowledge/
self-assessment-at-writing.md + .ufo/waves/round-29/count-c1.py`; S174–S176 used-by staging path →
canonical entry (retain/drop decision for the counter path recorded in the lesson). Frontier rows
advanced: none (frontier unchanged; README round-29 disposition records this). The round's sourced
claim: C1's knowledge entry cites S174–S177. Mined mistake: see Work performed (prereg-time-check).

## Trend verdicts

- **expansion: unchanged** — no new serving/runtime surface; the corpus gains one knowledge entry,
  four SOURCES rows and two QUALITY criteria on existing calibration ground; coverage axis surface
  unchanged by design after three rejected depth-claim shapes.
- **quality: improved** — 11 false self-assessment statements now carry observed values (unresolved
  11 → 0 under the frozen counter); KQ38/KQ39 admission criteria added; round-28 routed repairs
  landed; the lane's timestamp falsifier is now fail-capable on the mistake class that produced the
  round-28 rejection. Evidence: SCORECARD round-29 section; lesson §Mistakes; QUALITY.md.
- **discernment: improved** — the lane can now count its own self-assessment mismatches at writing
  revision instead of asserting calibration (bounded reading disclosed: evidence-resolution
  defects, not proven wrong judgments; recall limit 69 of ≥141 checkable statements disclosed).

## SHONEN

- [~] SKILL.md decision tables/error patterns/checklists — unchanged this round; prior author
  assertion stands, no named non-author verifier. Evidence: SHONEN.md box 1.
- [~] End-to-end domain task executed and logged — round-16/17 live receipts stand; this round's
  work is calibration, not a new domain task. Evidence: SHONEN.md box 2 (wording corrected this
  round: current-controls arm 8/8 rejected; frozen arm accepted-bad 6, K3 inconclusive; verified
  against `controls-frozen.json` by VerifyShonenBox2). No [x] — w1/w2 Confirm/Verify seats are
  lane-dispatched and cannot supply the non-author mark.
- [~] Instructions executable without oral context — unchanged; independent execution review still
  open. Evidence: SHONEN.md box 3.
- [~] No cross-domain bleed — PROVINCE.md unchanged; ConnectorOverlap found kaidoku class-T prior
  art, reported in the lesson, not absorbed. Evidence: SHONEN.md box 4.

## Extras

- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
- Tool installs this attempt: none (no seat installs recorded in w2 reports; pacman untouched).
- Open L0 questions: one appended this round — lane working-copy anchor blocked by a w2 seat's
  in-lane `git fetch` (local master/jj bookmark at operator commit `49f849f`, non-empty `@` based
  on `513eba3b`; helper refuses by design). RESOLVED in-session: the orchestrator re-anchored
  (`jj new 49f849f` + working-copy restore, logged in `.ufo/waves/hyaku/PHASE5.md`), and the
  integration commit landed immediately after (`6de225c2`). The L0 line remains for the operator's
  record.
- Environment notes: origin/master moved to `49f849f292c3` (operator daily-reflection commit,
  descendant of `513eba3b`, touches only `considerthese/2026-10-23.md`); the integration commit
  rebases over it via the helper's recovery path. One pre-steering selftest left residue at
  `/fast/scratch/hyaku/kama-r26/ExecPreregTimeCheck/ptc-selftest-ywq_7og0` (seat-disclosed, scratch
  space). Counter environment limit disclosed: `blame.ignoreRevsFile` config can shift receipts
  (fail-closed; host unset).
