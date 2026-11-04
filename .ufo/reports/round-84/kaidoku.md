# kaidoku — round 84

## Work performed

Declared claims: **R84-C1 calibration**, prefreeze counter-path metadata; **R84-C2 depth**, closure of thirteen declared mutation classes; **R84-C3 coverage**, a bounded three-level nested SquashFS chain. Calibration is tied-lowest; no waiver or retirement. Final pushed lane: `1598ee68943807845f04f52d057e01be6b5ddfe4`.

- Frozen plan `plans/round-84-claims.md`, declaration `e0de2088a7bddc16305357f90ac7e889fa0a0d11`, first container `a5663ddedd157bb9113928f5fe80509d6f3fc7a1`; base `043b89a25241710a68b45526c3287fb3c8d907c3`. Full counter paths occur in all three predicates.
- Integrated real production-path detector cases from ExecPcDetectors and boundary fixtures from ExecSbDetectors; independent BASE reproduction confirms four kills/nine survivors (`.ufo/waves/round-84/w1/ExecMutantBase.md`). ScoutLoci independently verifies fourteen edit anchors and thirteen behavior-relevant mutations.
- Real domain task: reproducible LE v4 gzip chain → independent unsquashfs oracle → REA6.5.0 extraction at depths3/4 → published-byte comparison and provider depth fields. ExecNested and ReviewerC3 independently reproduce the measurement and fixture digests (`w1/ExecNested.md`, `w1/ReviewerC3.md`). No inspected artifact execution.
- Repaired attack findings: table-id write escape, last-container control attribution, missing-key/null confusion, vacuous deepest-level arm, and unfrozen-table acceptance. Original findings remain in seat reports; revised instrument digests and commits are disclosed in `.ufo/waves/round-84/claims.json`. Round82/83 subject changes are separately disclosed in their containers.
- Added sourced knowledge, bounded PROVINCE/Core note, index rows, QUALITY144–147 and mistake mining (`corpus/lessons/round-84.md`). Appended correction of round83's **13→12** quote-word count without rewriting historical evidence (`corpus/lessons/round-83.md`).

Wave: **one v1 wave,14 dispatched/settled,14 substantive report files**, five executor, two scribe, one scout, two reviewer, one critic, one mutation-tester, one sentinel, one connector; attack4/14=28.6%, one connector. L1 holds planner because validator excludes planner. No replacements/residual/dead seats reported. **WAVE-DONE received from Main before filing.** Results artifact `.ufo/waves/round-84/r84-w1-results.json` retains null output fields after an orchestrator kernel restart; report files supply evidence. Runtime IDs/terminal statuses remain absent, not invented; registered names survive in `.ready.dispatched` and `l1/wave-accounting.json`. This retains round83's routed accounting debt rather than falsely declaring it closed.

## Landed changes

Every item is logged under `LOG.md` “round84”.

| Change | Landed commit |
|---|---|
| Counters, controls, plan | `e0de2088a7bddc16305357f90ac7e889fa0a0d11` |
| First claims container | `a5663ddedd157bb9113928f5fe80509d6f3fc7a1` |
| Candidate integration and counter repairs | `b15d8083baf4f6de420fb452bcec13a87f4bb22a` |
| Pins and supersessions | `4a8362be24f1f6bd2843f2971207afc9ca76c15e` |
| Corpus, source registry, capability rows, measurements | `8ae9c8ee734aee7d51311629a33bcbcf67161214` |
| Coverage assessment reconciliation | `26f4e1ba85e0ca85921ea99f3fdd02a619373b78` |
| Settlement evidence and documentation correction | `4419abf6bf27a4d39917fc70d905fd6b17b26e23` |
| Final pin disclosure and committed-byte replays | `16be078adae62713c7e166bdbd642b222edcaca0`, final evidence `1598ee68943807845f04f52d057e01be6b5ddfe4` |

## Before → after measurements

Commands run from the lane; `REV=16be078adae62713c7e166bdbd642b222edcaca0`. Short receipt paths below are under `.ufo/waves/round-84/`.

**C1:** maintained audit at BASE exits0 while reporting round83 FLAGGED/INSTRUMENT_NONE: refusal0/1. New finite gate refuses round83 and accepts round84:1/1 each, mismatch0, control_fired true, exit0 (`pre/c1-maintained-gate-base.json`, `l1/scores/c1-at-final.json`).

```sh
python3 -I -B tools/round-84/freeze-precheck.py --root . --rev "$REV" --container .ufo/waves/round-83/claims.json --expect .ufo/waves/round-83/claims.json=FLAGGED --container .ufo/waves/round-84/claims.json --expect .ufo/waves/round-84/claims.json=CLEAN --control instruments-only --json-out "$OUT"
```

**C2:** same frozen table at BASE:4 killed,9 survivors,exit1 →13 killed,0 survivors/inconclusive/red pristine,table digest matched,exit0 (`pre/c2-base.json`, `l1/scores/c2-at-final.json`).

```sh
python3 -I -B tools/round-84/mutation-closure.py --root . --rev "$REV" --mutants .ufo/waves/round-84/mutants.json --work "$WORK" --json-out "$OUT"
```

**C3:** before is **unmeasured Frontier**, not a measured zero; the pilot preceded declaration and already observed the target. Final replay gives nine true arms:8/8 exact oracle members at both depths; depth3 partial with one depth-limited root and explicit null level3 analysis_depth; depth4 complete with level3 depth3. Control fires (`l1/scores/c3-at-final-with-provider.json`).

```sh
REA_UNBLOB_COMMAND=/home/vgpnk/.local/bin/unblob PATH=/home/vgpnk/.local/bin:$PATH python3 -I -B tools/round-84/nested-sqfs.py --rev "$REV" --work "$WORK" --json-out "$OUT"
```

The final Eval subprocess initially lacked REA_UNBLOB_COMMAND: C3 exit1/capability_unavailable is retained in `c3-at-final.json`. Same committed counter with explicit provider exits0. No failed observation discarded. Producing execution records retain exit/stdout/stderr and environment overrides.

**Verdicts and limits:** finite C1/C2 outputs verify; bounded C3 observation verifies, but **CriticClaims rejects the broader interpretations of all three** (`w1/CriticClaims.md`). Whole-round admission is **not asserted**. C1 is a naming/pinning lint, not semantic counter attribution; a path in kill_rule or negated prose satisfies it. C2 case-name kills do not certify detector semantics: a fabricated case also scores green; candidate bodies were independently reviewed as behavioral. MutationTester finds22 survivors in24 additional pre-integration mutants, including15 genuine gaps outside this table. C3's before/control is not independent: pilot predates freeze and the file-count illustration follows from A1+A3. Provider fields are self-report; fixture pins require external comparison; root matching is suffix-only; sasquatch identity is not pinned. Counter revisions after initial scoring remain disclosed, not retroactively frozen.

Standing checks exercised: final freeze/disclosures exit0; source census exit0; provenance at8ae9c8ee:57 receipts,one declared control,unexpected0; registry census:137 paths,nonconformant0,duplicates0; coverage at26f4e1ba:167/167,two assessment atoms true,mismatches0. Receipts under `l1/scores/`. No whole-domain no-harm certification follows.

## Sources & frontier

Registry **205→208**; tiers **A187/B10/C8→A190/B10/C8**; mined184→186,rejected21→22. Added S301 mksquashfs reproducibility documentation and S302 installed REA6.5.0 depth-limited remedy text (mined,A); S303 tarball-as-unanchored-taxonomy authority rejected,A with flip. Existing row status/recheck/used-by unchanged; new used-by paths cite the round84 knowledge entry and lesson. Located quotes24/18 words, snapshots and hashes: `l1/sources/round-84-sources.json`, lesson `## Gate`.

Counting command (both ends):

```sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kaidoku
```

Start output:26 W04 duplicate-URL warnings, terminal `kaidoku ok /home/vgpnk/Projects/shokunin/kaidoku-shokunin/corpus/SOURCES.md`, **exit0**. End:27 W04 warnings (S303 added), same terminal ok, **exit0**; full end output in `l1/scores/sources-final.execution.json`. Intermediate E11 used-by-before-file failure retained and mined, not suppressed.

Frontier advanced only for the measured **lane-built three-level LE v4 gzip chain** (`PROVINCE.md` round84, `corpus/README.md` round84 note). Other nesting classes remain unmeasured. Three demonstrated capability rows enter SCORECARD; historical expertise proxy scores unchanged. **Assimilation: none**; package `merge/kaidoku/` exists but untouched under this round's three-claim cap. No lane `considerthese/` directory.

## Trend verdicts

- **expansion: improved**, bounded nested-container edge class and demonstrated repertoire; not vendor-nesting mastery (`PROVINCE.md`, C3 receipt).
- **quality: improved**, behavioral cases close the thirteen declared classes and attack-discovered counter defects are repaired with explicit revisions. Broader counter-strength limitations remain (`QUALITY144–147`, seat reports).
- **discernment: unchanged pending independent closure**; author-dispatched reviewers expose limits but are not outside admission authorities. Their adverse verdicts are retained.

Stale-lane: this is exactly round84; no successor mission started by this L1. No tool installed/upgraded; pre-existing mksquashfs/unsquashfs4.7.5, REA6.5.0 npm cache and unblob26.6.4 used. Pacman stayed paused. No new L0 question. Misroot sweep found only orchestrator/sibling changes and unattributed historical root file `after`; left untouched, no own-seat misroot found.

## SHONEN

- [~] Decision tables, error patterns and cited commands: SKILL round84 registry; QUALITY144–147; no outside promotion verifier.
- [~] End-to-end domain task: nested chain→REA→oracle task, LOG round84 and C3 receipt.
- [~] Executable instructions: three measured commands and fourteen seat report files.
- [~] Province boundary: bounded synthetic class explicitly stated; ConnectorScope sibling scan; no universal scope claim or promotion.
