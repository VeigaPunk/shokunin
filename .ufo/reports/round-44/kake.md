# kake — round 44 report

Lane tip (pushed): `942fe187034c0666b5300e134e14b76d5e92a583` (jj-lane helper, `landed` lines:
round-44 commit `297aa62df22ae723e19e1334ddaca9ef28065fbd`, typo fix `5f5c9c42a65b6631f712f059bd0b3714056c7681`,
receipt refresh `942fe187034c0666b5300e134e14b76d5e92a583`). Round commits: 3. Base: `18cb2c28f47c3ec3732ffa06c456e61b3444b1a2` (r43 settle).

## Work performed

Declared claims (2, both measured; zero exploratory):

- **C1 — operability, capability acquisition: the witness-class gate.** The frozen differential
  counter v5 (`.ufo/waves/round-44/c44_count_v5.py`, sha `5cedaa3b…`) + audit driver
  (`c44_audit.py`, sha `8ee2c8bf…`) + ten class modules G1–G10 witness all 27 round-43
  controls registered in `.ufo/waves/round-44/controls-27.tsv` under `--classes v5`, while the
  placebo counter witnesses only seed-luck k<27, the held build `020bc457` meets v5 3/3
  unseeded, and the four r42 canaries + junk control stay red. Capability row entered
  `SCORECARD.md ## Capabilities` this round.
- **C2 — freshness: receipt-derived ledger figures re-derive.** The three r43 ledger figures
  routed by the round-43 verifier spot-check (§8.1 tally, §8.5 do-nothing ratios, §8.5 build
  ratio range) now have last statements equal to the values re-derived from the committed
  receipts; the checker `scripts/ledger_latest_check.py --root .` exits 0. Mismatches 3 → 0.

Work items (evidence pointers):

- Inherited attempt-2 state reused after re-verification: frozen counter/audit bytes,
  `controls-27.tsv` + 27 control tools, placebo, class corpus, `scripts/ledger_latest_check.py`,
  w1 spec/registry and 24 seat reports (`.ufo/waves/round-44/w1/`); inherited receipts
  (`verification/freeze/`, `verification/placebo/`) re-scored per the SCORECARD pre-freeze
  amendments and kept as seat evidence, not claim receipts. Inherited SCORECARD amendments A/B
  and correction 2 preserved and extended (SCORECARD.md:3544-3571).
- G6 build item landed by the L1 from two independently verified seat derivations
  (`.ufo/waves/round-44/w2/ReviewG6Semantics.md`, `w2/MutG6Placebo.md`) after the ExecG6FoldFix
  seat stood down to verification: `classes/g6_fold_pairs.py` (sha `cddc5c7d…`) — IP-literal
  zone-id KELVIN pairs (v3/v4, ≤64 cps) + first-segment KELVIN pairs (v7) + first-segment
  long-s pairs (v8-only). Probe matrix 20/20 exit 1 (`w2/ExecG6FoldFix.md`; L1 run identical).
- Final claim cohorts run in isolated directories (lesson 13): `verification/claim/{after-final,
  placebo-final, v4-final, canary-final}/` + `w2-baseline/` (pre-fix 23/27 reproduction).
- C2 repairs appended to SCORECARD.md/LOG.md with receipt names and derived values; wording
  neutralized per `w2/CriticC2Repair.md` (no unsupported causal claims).
- Wave-2 falsification wave: 32 seats, all returned; every counting command re-run, every new
  source row re-opened, both instruments mutation-tested (`.ufo/waves/round-44/w2/*.md`, 32 reports).
- S131/S132 superseding rows appended to `corpus/SOURCES.md` byte-exact from the lesson
  (`w2/ScribeSourcesRows.md`; census exit 0 before and after).
- Misroot sweep before report: `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows
  only operator/driver files and other lanes' files at the fleet root; **zero kake-r44 misroots**
  (seat reports all landed under the lane). No fleet-root copies to migrate.
- Lesson `corpus/lessons/round-44.md`: Gate (S129/S130 re-opened, locator-corrected quotes) +
  Mistakes 12 (manifest misattribution, `w1/CriticClaimC1.md` a3 + `w1/CriticMathDenominator.md`)
  and 13 (audit-driver receipt-cohort collision, `w2/CriticKillRules.md` + `w2/ExecAfterBaseline.md`).

## Landed changes

- `297aa62d` — SCORECARD.md (round-44 declarations, amendments, C1/C2 measurements, capability
  row), LOG.md (round-44 entry), corpus/SOURCES.md (S131/S132), corpus/lessons/round-44.md,
  scripts/ledger_latest_check.py, `.ufo/waves/round-44/` (specs, registry, classes, controls,
  verification cohorts, w1+w2 seat reports), `.ufo/waves/round-43/w1/CtlPrefixCache.md`
  (inherited r43 late seat report referenced by the r43 settle prose; provenance preserved, not
  edited). LOG.md round-44 entry: lines ~1690-1713.
- `5f5c9c42` — SCORECARD.md typo (pre-G1-fix → pre-G6-fix), found by this L1.
- `942fe187` — refreshed `verification/claim/ledger-after.txt` measured at tip.

## Before → after measurements

**C1** — counting command (frozen in SCORECARD.md:3604-3611, same command both states):

    python3 -B .ufo/waves/round-44/c44_audit.py --root . --controls .ufo/waves/round-44/controls-27.tsv \
      --counter .ufo/waves/round-44/c44_count_v5.py --classes v5 --expect witnessed \
      --build-rev 020bc457 --build-runs 3 --workers 4 --out .ufo/waves/round-44/verification/claim/after-final/after-v5.json

- Before: `.ufo/waves/round-44/verification/claim/placebo-final/placebo.json` — `--expect witnessed`,
  `witnessed 0/27`, exit 1 (fresh; k∈{0,1} across 7 wave-2 audits; inherited receipt 1/27 was one
  seed draw). v4 supporting cohort `v4-final/v4.json`: 0 class witnesses by construction, exit 0
  this draw (25-26/27 in earlier wave-2 draws — seed-dependent, reported per amendment A).
  Pre-fix baseline `w2-baseline/run1|run2/`: 23/27, exit 1 (reproduced twice, fresh seeds).
- After: `after-final/after-v5.json` — `witnessed=27/27 notMet=27 build_met=3/3 ok=True`, exit 0;
  driver `--selftest` exit 0; per-row receipts re-derive at recorded seeds (0 mismatches,
  `w2/ExecAfterBaseline.md`); 27/27 witnesses semantic — no timing-only, no legacy-only, no
  counter-error rows (`w2/CriticKillRules.md`); kill rule 4 clean — no class module reads a
  control file (`w2/CriticKillRules.md`, `w2/ExecG6FoldFix.md`); canary `canary-final/`
  notMet 5/5, exit 0. Measured at commits `297aa62d`/`942fe187` (counter bytes unchanged
  between them; counter sha pinned in every receipt).
- **Verdict: C1 MET** (capability acquired; row in `SCORECARD.md ## Capabilities`).

**C2** — counting command: `python3 -B scripts/ledger_latest_check.py --root .` (exit 0 met /
1 mismatch / 2 unreadable; `--selftest` 2/2).

- Before: `.ufo/waves/round-44/verification/ledger-before.txt` — `3 figures, 3 mismatches`, exit 1.
- After: `.ufo/waves/round-44/verification/claim/ledger-after.txt` — `3 figures, 0 mismatches`,
  exit 0, measured at tip `942fe187`; receipts re-derived from `master` (r43 receipts are
  committed and were not edited — kill rule 1 clean).
- **Verdict: C2 MET** (mismatches 3 → 0).

## Sources & frontier

Census command (frozen manual census): `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kake`

- Before (round start): exit 0 — `ok …/corpus/SOURCES.md` + 12 pre-existing W04 duplicate-url
  warnings (S033, S088, S092, S098, S099, S102, S110, S111, S115, S116, S117, S127).
- After (round end): exit 0 — byte-identical warning set; `ok …/corpus/SOURCES.md`.
- Rows: 130 → 132. Added: S131, S132 (tier: own-work/local-path, status mined, opened
  2026-10-23) — both superseding rows under contract rule 2, byte-exact anchor/teaches cells
  from `corpus/lessons/round-44.md`; originals S129/S130 unchanged. Touched old→new: no other
  row's cells changed (scribe's `git diff --numstat`: `2 0`).
- Frontier rows advanced: none (no recheck-due row was re-opened this round; S129/S130 were
  re-opened as sources for the S131/S132 corrections and the C1/C2 sourced-claim rule — their
  Gate records carry path, access date 2026-10-23, and ≤25-word located quotes).
- Mistake mined: entries 12 and 13 in `corpus/lessons/round-44.md ## Mistakes` (see Work performed).
- Routed source-registry observations (from `w2/ScribeSourcesRows.md`, not fixed): the
  `supersedes S0NN —` marker is unenforced for own-work rows; `corpus/knowledge/claim-count-derivation.md`
  still declares `source: S130`.

## Trend verdicts

- **expansion: improved** — a new capability row entered `SCORECARD.md ## Capabilities`
  (witness-class gate; first working demonstration is C1's before/after pair), SOURCES.md grew
  130 → 132 rows, and the lesson file gained a Gate + two Mistakes entries. No axis retired.
- **quality: improved** — three receipt-derived ledger figures now match their receipts
  (3 → 0 mismatches, exit 0 at tip); the witness classifier and both instruments are
  mutation-tested able-to-fail (`w2/MutClassGate.md`, `w2/MutLedgerChecker.md`,
  `w2/MutG6Placebo.md`); 6 wave-1 reports sample-reviewed with 0 fabrication
  (`w2/ReviewWave1Reports.md`); manifest 27/27 verified (`w2/ReviewManifest.md`).
- **discernment: improved** — the round's premise (r43 spot-check: the frozen counter was blind
  to 27 live-seat controls) is now closed by a gate that proves the observation set, with the
  mixed-witness caveat disclosed (`w2/CriticC1Predicate.md`: repeat-len-band also diverges on
  legacy keys — the predicate counts it; the incremental-closure reading does not) and three
  HIGH latent gate defects routed rather than hidden (`w2/ReviewCounterContract.md`).

## SHONEN

- [ ] SKILL.md contains real decision tables, error patterns, checklists, cited sources — untouched this round (no diff at `942fe187` vs base).
- [~] At least one end-to-end domain task executed and logged in LOG.md — C1/C2 logged in LOG.md round-44 entry (lines ~1690-1713), measured at `942fe187`.
- [ ] Instructions executable by an agent without oral context — unchanged this round.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — PROVINCE.md untouched; all writes inside the lane's web-publishing domain (diff at `942fe187` names only SCORECARD/LOG/corpus/scripts/.ufo).

## Round shape and waves

- Shape: **default — two v1 waves** (policy v1, band 32-64 each; together 67 ≤ 128).
- Wave 1 (inherited from attempt 2 of round 44, orchestrator-loss victim; re-verified, not
  re-dispatched): 35 seats dispatched (spec `.ufo/waves/round-44/w1-spec.json`, registry
  `w1/swarm-registry.json`), build + pre-freeze calibration. **Dead seats: 11 of 35** left no
  report (24 reports on disk; the missing include the four audit-focused seats ExecAudit,
  MutationTesterAudit, ReviewAuditDriver, ReviewLedgerCheck — named by `w2/DistillerWave1.md`;
  last status: dispatched, never delivered; no error text survives the parent freeze).
  Dispositions of wave-1 findings: SCORECARD pre-freeze amendments A/B + correction 2.
- Wave 2 (this attempt): 32 seats, one validated task call (`w2-spec.json`, validator
  `ufo-swarm-wave.mjs run` under `ufo-wave-policy.json`; taskCall dispatched unchanged).
  Role mix: 6 executor, 6 reviewer, 5 critic, 5 scout, 4 scribe, 3 mutation-tester, 1 sentinel,
  1 revenger, 1 simplifier (attack roles 19/32 = 59%). **Dead seats: 0** — all 32 returned; two
  (ExecG6FoldFix, MutClassGate) needed the operator's wrap-up steer and returned with partial
  vs re-scoped results (ExecG6FoldFix re-scoped to verification of the L1-landed G6; both PASS).
- Residual checks: none needed (no leftover attack items).
- Round total: 67 seats. §3 L2 floor met inside wave 1 (11 roles) and again in wave 2;
  the planner seat is the L1's per the frozen-topology ruling; a bounded planning data-walk rode
  the w2 scout seats.
- Seat-route note: per the operator's seat-routing, all seats ran through the host route table
  (`task.agentModelOverrides`); no model aliases were passed or written to the lane.
- The near-duplicate wave-1-style spec drafted pre-steer was **discarded before validation**
  (only `w2-spec.json` was ever validated/dispatched; the draft survived only as the builder
  script `make_w2_spec.py`, committed as wave evidence).
- Future-wave conformance: the operator's two time-box lines will be carried verbatim in every
  future wave spec item (steer 2026-10-23).

## Stale-lane, installs, L0

- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
- Tool installs: none (pacman paused host-wide; nothing installed by the L1 or needed by seats —
  one seat noted using pre-existing `ruff 0.17.1` read-only).
- L0 questions: none this round.
- Routed to round 45 (recorded in SCORECARD.md:3621-3626 and the w2 reports): the audit
  driver's three HIGH latent gate defects (counter-error / tool-absent receipts can witness;
  stale planted receipts accepted — none exercised by this round's receipts), the v4-mode
  predicate text naming ten unexecuted class runs (`w2/CriticHarmGuard.md`), the frozen
  selftest's missing timing-only/error fixtures (`w2/MutClassGate.md` caveat), and the SOURCES
  supersedes-marker enforcement gap.
