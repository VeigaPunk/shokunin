# kengaku — round 25 (hyaku block 25–34, attempt 1)

Lane: kengaku-shokunin (LLM/model research & evaluation; owned axes novelty + calibration). L1: KengakuR25 (also holds the
frozen planner seat — the wave validator rejects `planner`). Base `6180e4f`. Lane commits: `3f371d2` (pre-registration),
`710409f` (Amendment 1, before any instrument output), `8ea41f9` (integration), `8239a56` (falsify-wave revision),
`9d8a00d` (close; landed `9d8a00d2a69b83a1e83eb41e1d2ee840910949e4` — lane HEAD).

## Work performed

Declared claims (`plans/round-25-claims.md`):
- **C1 — novelty** (legacy label, nominally mapped to canonical coverage; lowest axis 7, tied with coverage 7 — coverage is
  capped, so novelty carries the lowest-axis claim): an offline exact Clopper–Pearson re-verdict of every stored attribution
  verdict in the nine sha256-pinned r21–r23 receipts, with per-leg recall/specificity and share bounds, plus capability
  `interval-reverdict`.
- **C2 — calibration**: mechanical re-derivation of the frozen SCORECARD/SHONEN/PROVINCE/README current-state assertions
  (population frozen at base), plus capability `state-assertion-check`.

Work items:
- Pre-registered populations, interval rule, power ask (n ≥ 17 at zero errors; tightened to N(e) = 17/26/34/41/48/55 by
  CritPowerAsk) and five predictions before any instrument existed (`plans/round-25-claims.md:1-110`, `3f371d2`).
- Built `plans/attrib_calibration.py` (CalibCoreExec + L1): re-derives 119 stored lines in 10 score blocks, `mismatches=0`;
  4 unique samples, 92/92 correct; transitions `FAIL>UNTESTED:2,PASS>INDETERMINATE:1,PASS>PASS:4`
  (`corpus/evidence/round25-calibration/attrib-calibration-summary-v2.txt`). Independent cross-checks: sh+awk oracle
  `plans/fixtures/r25/attrib_oracle.sh`, exact-rational `plans/fixtures/r25/cp_reference.tsv` (861 rows), a third Node parser
  (falsify ThirdParserExec, 0 disagreements).
- Built `plans/state_check.py` (StateCheckExec + L1): base `6180e4f` `mismatch=10` exit 1
  (`state-check-before-6180e4f-v2.txt`) → revised tree `mismatch=0 superseded=1` exit 0 (`state-check-after-v2.txt`).
- Knowledge entry `corpus/knowledge/attribution-interval-calibration.md` with appended §Corrections from wave 2.
- Conformance repairs: D17 `SHONEN.md` regenerated to canonical pointer form; D18 SKILL frontmatter now carries quoted
  triggers, an anti-trigger and a sibling-arbitration note and parses as YAML (`round25-census-after.txt:
  skill_frontmatter_yaml=valid`). D15 (missing r19–23 fleet reports) not fabricated.
- Learning from the r24 outside decisions: every kaika W3 finding F1–F14 re-checked by one wave-1 reviewer each; open ones
  closed by appended corrections (F4 residual, F5, F6, F7 → S036, F10, F11, F12); F3 resolved as already right
  (ReopenS009F3); disposition table `corpus/lessons/round-25.md` §Kaika W3 findings.
- Mistakes mined M23–M38 with red runs (`corpus/lessons/round-25.md` §Mistakes and §Falsify-wave corrections); QUALITY
  Q11, Q12, R11–R15 each cite their lesson row.
- Falsify wave: 87 seats attacked the landed tip; their breaks became Amendment 2 (disclosed as post-output) and appended
  corrections — novelty +1 withdrawn on prior art (cigate, S041), 5 vacuous specificity PASSes removed, the share bound
  relabelled conditional and shown vacuous with its sampling arm, 13 surviving mutants killed, C2's P2d brought to the
  registered rule (base 11 → 10).

## Landed changes

| change | LOG.md entry | commit |
|---|---|---|
| pre-registration + Amendment 1 | `## Round 25` (first bullet) | `3f371d2`, `710409f` |
| C1 instrument, entry, SOURCES S027–S037, gate receipts, C2 instrument, SHONEN/SKILL/PROVINCE/README/QUALITY, lesson, wave-1 evidence | `## Round 25` | `8ea41f9` |
| Amendment 2, appended corrections, S038–S042, hardened instruments, v2 receipts, wave-2 evidence | `### Round 25 falsify-wave revision` | `8239a56` |
| remaining wave-2 seat reports, SHONEN pointer refinement, duplicate-row and id-set checks, lesson corrections | same | `9d8a00d` |

## Before → after measurements

- **C1** — `python3 plans/attrib_calibration.py --summary` (before: instrument absent at `6180e4f`; the round's widened sweep
  `grep -rnE 'Clopper|Wilson|confidence interval' corpus/knowledge` finds only descriptive Wilson intervals in
  `attrib-r21.md`, no exact, per-leg or verdict-carrying interval). After (measured at `9d8a00d`): 35 estimates, PASS 7 /
  INDETERMINATE 11 / UNTESTED 12 / 5 non-firing without verdict; stored verdicts re-verdicted 0/7 → 7/7. Score **7 → 7
  (held)**: the construct is published as tooling (cigate 0.2.0, S041), so the rubric's "already published" cap applies;
  CritNoveltyFresh dissents (+1 fires). Verdict: improved (observable), score held.
- **C2** — `python3 plans/state_check.py --summary`: base `6180e4f` 10 mismatches (v2; v1 counted 11 by testing a `/proc` pid
  pin inside an endpoint row) → 0 at `9d8a00d` (1 superseded by a full-census correction). Narrowest reading of P2c (without
  PROTOCOL.md:432's pointer-only form): 6 → 0. Score **8 → 8 (held)**; rubric +1 needs a scored probe.
- R11/R15 check on this report: `sh kengaku-shokunin/plans/l0_filed_check.sh .ufo/reports/round-25/kengaku.md .ufo/l0-questions.md` → `filed=2 unfiled=0`, exit 0.
- Separability (QUALITY R13): each count re-run with the other claim reverted is unchanged
  (`corpus/evidence/round25-calibration/revert-test.txt`; falsify RevRevertTest reproduced it).
- Round census `sh plans/round25_census.sh`: before `round25-census-before-6180e4f.txt`, after `round25-census-after.txt`.
- Predictions P1–P5: outcomes (1,1,1,1,0) under the literal dedup key, Brier mean 0.0452 (0.0652 if P2 is scored on its
  "same sample" wording); all five were derivable from bytes committed before filing — no calibration credit taken.
- Final suite at the revised tree: `grader.py` `CHECKS n=733 mismatches=0`, PASS; attrib_calibration `--selftest` 18/0;
  state_check `--selftest` ALL PASS; power_table `--check` no drift, `--selftest` 13/13; cp_reference `--verify` failures=0.

## Sources & frontier

- Census command `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kengaku`: round start
  `kengaku ok`, exit 0; round end `kengaku ok`, exit 0 (one W04 warning: S040 shares S035's URL across scopes, as a
  superseding row).
- Rows (`grep -cE '^\| *S[0-9]{3,} *\|' corpus/SOURCES.md`): 26 → 42 (S027–S042). Added by tier: A 14, B 2 (S036 own-work,
  S041 tool). Tiers overall A=24 C=2 → A=38 B=2 C=2; status mined 18 → 30, queued 5 → 9, rejected 3 → 3.
- Rows touched old→new: S011 used-by `corpus/knowledge/llm-judge-calibration.md` → `…, corpus/knowledge/attribution-interval-calibration.md`.
  Superseding rows: S036 ← S025 (tier), S039 ← S034 (teaches), S040 ← S035 (scope; PPI §4.2.2 is prior art), S042 ← S030 (anchor).
- Receipts: `corpus/evidence/round25-sources/gate.md` (URL, access time, sha256, ≤25-word located quote per row; falsify
  addendum). Non-author-style re-opens by wave-2 seats: S011, S027–S035 (hashes reproduced; location slips fixed).
- Sourced claim: the C1 knowledge entry cites S027–S030, S033, S039–S042, S011 and own-work S036/S037.
- Frontier: README §Frontier "Judge calibration applied inward" partly discharged (attribution receipts), with the
  `grader.py` half and the S010 perturbation audit still open. Leads added: Clopper–Pearson 1934 (unopenable), interval-gate
  tooling and papers surfaced by PriorArtWeb.

## Trend verdicts

- **expansion: improved (contested)** — new entry on frontier ground citing mined rows; capabilities `interval-reverdict`
  and `state-assertion-check` entered by demonstration (`SCORECARD.md` §Capabilities). Counter-evidence: at its first
  landing (`8ea41f9`) the entry failed QUALITY Q9 (PPI rejection reason) and Q10 (S030/S011 location slips; the second-seat
  re-read ran after landing) — falsify RevEntryQBar; both were corrected in-round by appended §Corrections and superseding
  rows S040/S042 (M33/M34). If the closure judges the gate at first landing, expansion is **harmed** and the round is a trade.
- **quality: unchanged** — stale point verdicts are now marked (attrib-r21.md erratum, SCORECARD R25-E6) and twelve r24
  findings closed, but the new entry failed parts of its own re-check (share-bound coverage, location slips) and was
  corrected by appended §Corrections; nothing is left unmarked, so not harmed.
- **discernment: unchanged** — the outside spot-check (≥1 admit, ≥1 reject) belongs to the non-author closure; every new
  QUALITY criterion cites a lesson row; the lane's own rejection of PPI was wrong and was superseded (M33).

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md`
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md:7`
- [~] Instructions executable by an agent without oral context — `corpus/lessons/round-8-aggregator-box3-coldrun.md:48`
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md:129`

## Swarm

- Wave 1 build: 92 seats in one validated task call (scout 29, reviewer 18, scribe 13, executor 11, connector 8, critic 8,
  revenger 4, sentinel 1). Dead: 0. Late: SrcReiczigelExact and StateSelftestExec returned after integration (~32 min);
  the first became S038, the second's fixtures were not integrated (its findings were).
- Wave 2 falsify: 87 seats in one validated task call (reviewer 36, scout 24, critic 10, mutation-tester 4, connector 3,
  executor 2, sentinel 2, simplifier 2, revenger 2, scribe 2). Dead: 0. Round total 179 (≤ 200). Planner: L1-held seat.
- Specs/registries: `.ufo/waves/round-25/{build,falsify}-{spec,dispatch}.json`, `{build,falsify}/swarm-registry.json`.
  The harness-required `solutionSpace` field was added to each task; names, roles and task text were passed unchanged.
- Misroots: three wave-1 seat reports (RevF6, RevF9, RevM19Critic) landed at the fleet root; moved byte-exact into the lane
  (`cmp` ok) and the fleet copies deleted (M29). End-of-round sweep (ScribeMisrootSweep + L1): none remaining.

## L0 questions

- kengaku | round-25 | Coverage cap (re-filed; first written only in .ufo/reports/round-24/kengaku.md:221 and never queued — lesson round-25 M23): does a surface explicitly retired to PROVINCE.md §Historical (absent, not governed, dated test -e receipt, now also marked ABSENT on its ## Surfaces row) still count as "declared-but-unresolvable" for the coverage rubric cap? Until ruled, kengaku coverage stays capped at 7.
- kengaku | round-25 | Novelty verdict conversion (re-filed; first written only in .ufo/reports/round-24/kengaku.md:224, never queued): the r21 "novelty axis-move — improved" verdict was never converted to a number; round 25 claims novelty 7 -> 8 on its own rubric legs. Should verdict-only rounds be converted retroactively (and by whom), or stay verdict-only, and is round 25's 7 -> 8 the first numeric move since r14?

(The second question's "claims 7 -> 8" was overtaken in-round: the +1 was withdrawn on prior art; the conversion question stands.)

## Integrator notes

- Report-out (MANIFEST is closure-owned): `MANIFEST.json:2744` states "hyper COVERED (run-2 10/10 = 1.000)"; under the exact
  CP95 rule that is INDETERMINATE on the registered population (PASS 19/19 or 20/20 if run 1 or the deduplicated pair is
  pooled) — falsify ConnCitersOfHyper.
- Report-out to kumitate: leg-share bounds are within-P1 forced/natural sample shares on the shim cascade, never natural
  fallback rates (`PROVINCE.md` round-25 report-outs).
- Sentinel note: SentinelNewFiles flagged loopback endpoint literals and one git `user.name/email` mention; all flagged lines
  predate round 25 (LOG.md:15 is round 9) except loopback mentions in two wave reports. No credential material.
- The SCORECARD round-25 section is superseded by its appended falsify-wave revision; rows stay as landed in `8ea41f9`.

Installs (seats; L1 none): uv `python install 3.12` (cpython 3.12.15, Astral, determinism probe, ReRunCalibSummary);
`uv tool install coverage` 7.16.2 (PyPI, SimplifyCalib); ephemeral `uv run --with` cmarkgfm, scipy 1.18.1, statsmodels 0.15.0
(LessonM28, RevDedupSensitivity, PowerTableExec oracle); mpmath 1.4.1 into a /tmp venv (RevPowerTable); `npx -y js-yaml`
(FrontmatterScribe); omp managed Chromium for the browser tool (SrcReiczigelExact). No pacman transactions.

Stale-lane: respawn-per-round driver; no other mission of this lane is open.
