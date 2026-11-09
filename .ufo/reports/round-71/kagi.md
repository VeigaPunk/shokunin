# kagi — round 71 report (attempt 1, L1 `KagiR71`)

Lane repo `/home/vgpnk/Projects/shokunin/kagi-shokunin`, branch `master`. Claim BASE
`e0e9603a924d73d9621924cc507b50474d11dae7` (round-70 spot-check tip). Final lane hash:
`7e7b3927f436a4a1fe335c26b299d7887e3ce4ba` (`git -C kagi-shokunin ls-remote origin refs/heads/master` →
`7e7b3927f436a4a1fe335c26b299d7887e3ce4ba	refs/heads/master`). The last commit adds receipts under
`.ufo/waves/round-71/final/` only; the measured content revision is `5b5483a6a9f0d3d27b9b3cf16793906178ee24b0`.

## Work performed

**Declared claim (one):** **C1 — depth: OpenBao PKI issuer and revocation channels, executed and
artifact-checked.** Frozen predicate (`plans/round-71.md` §C1 = header of `plans/round-71-c1.sh`):
`C1_PKI_ISSUER_TRIAL: value = number of tests T in {T6..T9} that DISCRIMINATE and whose ARTIFACT
check passes, when PINS = 1 and SETUP_OK = 1 and NOSECRET = 1 and NOLEAK = 1 and SOURCED = 1,
else 0; target 4 (BASE 0).` The wording as filed is narrowed by plan Amendments A1–A2 (below).
Sourced claim: S173, opened this round. No exploratory claim.

- **Freeze before candidate, with executed controls.** The plan, the counter (sha256
  `4d77f19c…8117b`), the runner and nine executed prefreeze controls landed together in
  `1199295573a4eb1791e965178c8643213312943d`. Every control matched the expected verdict written into
  `plans/round-71-controls.sh` before its first run (`.ufo/waves/round-71/controls/receipts/*.txt`):
  - F0 BASE: `value=0 absent=1`, rc 1.
  - P1 positive reference: `value=4`, rc 0, all `art=1`.
  - F1 echo: `value=0`.
  - F2 shim-byte-map (runs nothing): `value=0`. It passes DISCRIMINATE on all four tests (`shim=BROKEN spec=1`) and fails only because every `art=0`. This is the new artifact leg's teeth.
  - F3 no-teeth: `value=0`.
  - F4 unsourced: `sourced=0`.
  - F5 leaking server: `noleak=0`, five servers reaped.
  - F6 key copied into evidence: `nosecret=0`.
  - F7 T7 CRLs swapped: `value=3`, T7 `art=0`.

  Two legs are new compared with round 70: the real run also goes through a wrapper script, and the counter re-checks with openssl the certificates, CRLs and OCSP responses the real run leaves.
- **Candidate** `39e76bc700cf05e7772711f703bdbc3c6e7ac469` contains:
  - `corpus/openbao-pki-issuer-trial.sh` (bytes = P1), with four tests:
    - T6: a `truncate` issuer clips a leaf to its own NotAfter.
    - T7: a revoked leaf of a non-default issuer is on its own issuer's CRL and absent from the default CRL.
    - T8: token-less OCSP requests read `revoked`/`good`.
    - T9: a `no_store` leaf is revoked by proof of possession and listed on the CRL.
  - The entry `corpus/knowledge/openbao-pki-issuer-revocation-channels.md`.
  - Registry row S173 and its fetch row, plus the S170 `used-by` extension.

  The counter on the candidate reads `value=4` rc 0 (`.ufo/waves/round-71/final/c1-candidate.txt`).
- **Measured domain fact.** `bao write pki/issuer/<ref> leaf_not_after_behavior=truncate` (a POST)
  resets `issuer_name` to `""`, after which `unable to find PKI issuer for reference` is returned. S170
  states this: "It does not update only the provided fields." Receipt:
  `.ufo/waves/round-71/final/l1-probe-observations.txt`. The trial re-sends the name. Mined as
  M71-1 and QM102.
- **Wave `w1`, 12 seats** (`.ufo/waves/round-71/w1-dispatch.json` `counts.spawn=12`; settlement
  `.ufo/waves/round-71/w1-results.json`, 12 seats). Attack findings that falsified the claim's
  **wording**, not its number:
  - R71Revenger RE-1: forgery C takes its verdicts from config read-backs while its artifacts are real, and reaches `value=4`. The counter does not bind a verdict to its artifact.
  - R71MutTester MT-1: T9's serial-refusal conjunct is not counted (fixture f-m11 reads `value=4`).
  - R71Sentinel SE-7: NOSECRET is a fixed regex.
  - R71Connector CN-1/CN-2: two frozen pre-move sentences are false against BASE.
  - R71ReviewerSrc SR-1/SR-2: the trial was unstamped, and one inference was unmarked.

  Each is narrowed in `plans/round-71.md` Amendment A1/A2 and reconciled in
  `.ufo/waves/round-71/claim-falsification.tsv`. R71Reviewer reproduced value=4/BASE 0 and F2/F7, and read
  the landed trial: it does no wrapper reads and no local minting (RV-5). R71ExecReplica's
  independent trial reads `value=4`.
- **Integration** `5b5483a6a9f0d3d27b9b3cf16793906178ee24b0`:
  - Amendments A1/A2.
  - Entry narrowing: the T6 table cell, `[INFERENCE]` on the OCSP consequence, Does-not-establish forgeries A/B/C, SE-1/SE-7, and the T9 line.
  - Trial, counter and runner pinned in `corpus/stamps.tsv` (177 → 181), with every changed stamped file re-pinned.
  - S170 anchor cell extended (M71-2).
  - SKILL.md: four PKI decision rows.
  - PROVINCE: core line.
  - README: coverage-map row and the stamp/docs counts.
  - SCORECARD: errata, round-71 sections and capability row.
  - Manifest row `71 C1 depth`.
  - LOG, lesson, QM102.
  - An appended round-71 note on the round-70 entry.
- **Counter on the landed revision** `5b5483a6`:
  - Reading: `C1_PKI_ISSUER_TRIAL: value=4 discriminating=4 pins=1 setup_ok=1 nosecret=1 noleak=1 sourced=1 real_rc=0 none_rc=2`, T6–T9 each `real=HOLDS,shim=BROKEN,spec=1,entry=1,art=1`, rc 0 (`.ufo/waves/round-71/final/c1-landed.txt`).
  - The round-70 counter on the same revision still reads `C1_PKI_TRIAL: value=5` rc 0 (`final/c1-r70-on-landed.txt`).
- **Harm checks.** Both revisions were exported with `git archive` and run the same way, BASE (`.ufo/waves/round-71/base/`) and landed (`final/`):
  - `claim-ledger.sh verify`: BASE `POLICY (claims=102 policy=5 stamped=177)`, landed `stamped=181`. The FAIL/POLICY/MISSING-ID sets are 21/5/58 on both, and they differ only by SCORECARD line numbers shifted by the three inserted lines (`final/harm-diff-base-vs-landed.txt`).
  - Self-description sweep: n=28 at both (SD5=4 SD6=23 SD8=1). The line sets are identical modulo SCORECARD line shifts.
  - Self-counts: `stale=4` at both, with the same four ids.
  - `DOC_AUDIT: CLEAN (entries=51 row_linked=48 by_hand=3 … unpinned=0)`.
  - `RELEASE_CLOCK: CLEAN (on_release=32 bound=32 …)`.
  - `CLAIMS_DECLARED: MISMATCH (claims=67 mismatch=2)`: the carried round-69 pair, no new mismatch.
  - Lane census `CLEAN (rows=164 …)`.

  Disclosed: run inside the lane checkout instead of an archive, the sweep reads n=41 (SD6=36). The extra 13 lines all cite older lessons and SCORECARD rows that this round did not touch (`final/self-description-sweep-inlane-landed.txt`). The concurrent first run also hit the 900 s timeout on `verify` (`final/claim-ledger-verify-integration.txt` rc 124). The archive-to-archive comparison is the one filed. An in-lane BASE reading is not possible without a checkout, so whether n=41 is location-dependent at BASE too is **not measured**.
- **Planner seat:** the L1 held it (the validator rejects `planner`). The bounded recon rode R71Scout and R71Connector.
- **Routed items from the round-70 spot-check:**
  1. SCORECARD errata appended (QM97).
  2. Spec wave id `w1`, so the prefile default resolves; L0 line filed (fleet `f61d1df5`).
  3. Artifact leg, wrapper-script real run and evidence NOSECRET scan carried into this freeze.
  4. Comment-only, no open date in the new counter.
  5. SHONEN unchanged.

## Landed changes

| commit (`landed` line of `jj-lane.sh`) | content | LOG.md entry |
|---|---|---|
| `1199295573a4eb1791e965178c8643213312943d` | freeze: plan, counter, runner, control fixtures and receipts, round-start census, S170/S173 captures | `LOG.md` `## round 71` — "Freeze before candidate" |
| `39e76bc700cf05e7772711f703bdbc3c6e7ac469` | candidate: trial, entry, S173, fetch row, stamps (entry), claims.json, L1 probe receipt | `## round 71` — "C1 (met, wording narrowed)", "Measured domain fact" |
| `5b5483a6a9f0d3d27b9b3cf16793906178ee24b0` | integration: Amendments A1/A2, entry narrowing, stamps, S170 anchor, SKILL/PROVINCE/README/SCORECARD/LOG, lesson, QM102, wave w1 evidence + results + falsification ledger | `## round 71` — all bullets |
| `7e7b3927f436a4a1fe335c26b299d7887e3ce4ba` | landed-revision receipts (`final/c1-landed.txt`, r70 counter, harm diffs, census end) | `## round 71` — "C1", "Frontier" |

## Before → after measurements

| claim | counting command | BASE (`e0e9603a`) | after | measured against |
|---|---|---|---|---|
| C1 depth | `bash plans/round-71-c1.sh <rev>` | `C1_PKI_ISSUER_TRIAL: value=0 absent=1 pins=1`, rc 1 (`controls/receipts/f0-base.txt`) | `C1_PKI_ISSUER_TRIAL: value=4 discriminating=4 pins=1 setup_ok=1 nosecret=1 noleak=1 sourced=1`, rc 0 | `5b5483a6a9f0d3d27b9b3cf16793906178ee24b0` (`final/c1-landed.txt`; same reading on `39e76bc7`) |

L1 reading (not admission): the target is **met on the frozen counter, with the wording narrowed**. The claim
filed is the count of four shim-discriminating trial verdicts whose real-run artifacts pass the
counter's own openssl checks. It is not proof that the verdicts were computed from those
artifacts (RE-1) or that the serial refusal in T9 holds for any trial (MT-1). That the landed trial
executes the mechanics through `bao` and takes each verdict from the mechanic's output rests on
non-author reading (RV-5, RE-4).

Pre-file falsification gate:
`python3 scripts/hyaku/prefile-falsification.py --lane kagi --round 71` →
`PREFILE-FALSIFICATION: pass claims=1 rows=9 attack_seats=7 findings=0`, exit 0 (default wave `w1`). Ledger `.ufo/waves/round-71/claim-falsification.tsv`: 9 rows, with 6
`falsifies-wording` and 3 `neutral` (`awk -F'\t' '$1 !~ /^#/ && NF>0 {print $3}'
.ufo/waves/round-71/claim-falsification.tsv | sort | uniq -c`). Every attack seat is named.

## Sources & frontier

- Census command (fleet): `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kagi`.
  - Round start: stdout `kagi ok` plus 26 W04 lines, stderr 0 bytes, **exit 0** (`.ufo/waves/round-71/base/census-round-start.{stdout,stderr}.txt`, `.rc`).
  - Round end: stdout `kagi	ok	…/corpus/SOURCES.md` plus 26 W04 lines (S173 adds none), stderr 0 bytes, **exit 0** (`.ufo/waves/round-71/final/census-round-end.{stdout,stderr}.txt`, `.rc`).
- Lane census `bash corpus/sources-census.sh`: BASE `CLEAN (rows=163 …)` → landed `CLEAN (rows=164 A=146 … mined=142 … entries_sourced=30 …)`.
- Rows before → after: 163 → 164 (`grep -cE '^ {0,3}\| *S[0-9]{3}' corpus/SOURCES.md`). Added by tier: A +1 (S173 `mined`, OpenBao PKI considerations).
- Rows touched old → new:
  - S170 `used-by`: the round-70 entry → that entry plus the new entry (candidate).
  - S170 anchor cell: extended with the four §sections the new entry cites (integration, M71-2).
  - No status or recheck changed.

  Before appending, the registry was searched for the S173 URL (M70-1 rule): 0 hits at BASE.
- Frontier advanced: the PKI ground moved from one default issuer to issuer-level and
  revocation-channel mechanics: PROVINCE "Core, round 71" line, README coverage-map row, SCORECARD
  capability row. Leads for the next PKI round, measured by R71Scout: an issuer that has left the mount → default CRL, `permit`, and issuer revocation (`.ufo/waves/round-71/w1/R71Scout.md`).
- Gate decisions for spot-check: admit S173. The rotation-primitives page was not admitted (deferred to a rotation entry, R71ReviewerSrc) (`corpus/lessons/round-71.md` §Gate).
- Mistakes mined: M71-1…M71-5 (`corpus/lessons/round-71.md` §Mistakes), each with a check shown able
  to fail or a demonstrated gap. QM102 enters `corpus/QUALITY.md`.
- Assimilation: none (no `merge/kagi/` theme taken). considerthese: `considerthese/2026-10-26.md`
  proposal 3 was mined and refused as written. Its premise no longer reproduces, and its rule is already QM55. Flip condition recorded in the lesson Gate.

## Trend verdicts

- **expansion: improved.** A new admitted entry `corpus/knowledge/openbao-pki-issuer-revocation-channels.md`
  lands on ground the coverage map did not hold, with its coverage-map row (QM100). Knowledge files go 50 →
  51 (`git ls-tree e0e9603a corpus/knowledge/ | wc -l` → 50; `ls corpus/knowledge/*.md | wc -l` → 51).
  The registry goes 163 → 164, and there is one new executed trial.
- **quality: improved.** The freeze carried nine executed controls, positive and forgery. Two of them (F2,
  F7) fail only on the new artifact leg, which closes the round-70 "count does not prove the observable" class
  for swapped or absent artifacts. The wording was narrowed on the wave's own evidence. Landed-tree
  gates match BASE: the verify class sets are identical, the sweep is n=28, and self-counts stale=4 with the same ids.
- **discernment: unchanged.** The S173 admit was searched against the registry first (M70-1 rule
  applied) and survived a non-author re-open (R71ReviewerSrc). But the freeze again named two of
  three forgery classes (M71-4, a repeat of M70-5). Two frozen pre-move sentences were false against
  BASE (M71-3), and T9's refusal conjunct was left uncounted (MT-1).

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources. Evidence: SKILL.md `## Vault-ops decision table` gains four PKI issuer/revocation rows citing `corpus/knowledge/openbao-pki-issuer-revocation-channels.md` (commit `5b5483a6`). Asserted by the author; no non-author verifier is named.
- [~] At least one end-to-end domain task executed and logged in LOG.md. Evidence: `LOG.md` `## round 71`. `corpus/openbao-pki-issuer-trial.sh` ran against OpenBao 2.7.2 and the frozen counter read `value=4` (`.ufo/waves/round-71/final/c1-landed.txt`).
- [~] Instructions executable by an agent without oral context. Evidence: R71ExecReplica wrote an independent trial from the plan and entry alone, and the frozen counter read `value=4` (`.ufo/waves/round-71/w1/R71ExecReplica.md`).
- [~] No cross-domain bleed (PROVINCE.md still accurate). Evidence: `.ufo/waves/round-71/w1/R71Connector.md`. No sibling lane or registry row holds this ground, and the PROVINCE core line was added at integration (CN-4).

## Round shape and other required lines

- Round shape: ONE v1 wave `w1`, 12 seats, validated under
  `scripts/hyaku/ufo-wave-policy.json` (band 8–16). Residual call: none. Round total: 12.
  - Role mix: 2 reviewer, 1 critic, 1 mutation-tester (attack 4/12 = 33 %), 1 sentinel, 1 revenger, 1 connector, 2 executor, 1 scout, 2 scribe.
  - Dead seats: none. `w1-results.json` lists 12 seats, each with a non-empty final output. R71MutTester ended `SEAT-STATUS: partial` (mutant M10 not built); the other 11 ended `complete`.
- Settlement: WAVE-DONE was received from the orchestrator. Results are at
  `/home/vgpnk/Projects/shokunin/kagi-shokunin/.ufo/waves/round-71/w1-results.json` (committed in `5b5483a6`).
  This report was filed after WAVE-DONE.
- Seat incident: R71Sentinel's timing-harness cleanup SIGKILLed three sibling seats' dev servers
  (SE-11, `.ufo/waves/round-71/w1/R71Sentinel/incident-killed-foreign-servers.txt`). It was disclosed, and no
  counted value changed. Mined as M71-5: the next wave context forbids pattern kills.
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` showed only `.scratch/`
  entries, none written by this round's seats. Nothing was moved.
- Scratch: `/fast/scratch/hyaku/kagi-r71` is removed by the L1 after landing.
- Tool installs: none (no seat reported an install).
- Open L0 questions: `kagi | round-71 | Operator-side tooling …` (prefile wave-results naming), fleet commit `f61d1df5`.
- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
