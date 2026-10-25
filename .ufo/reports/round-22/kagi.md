# kagi — round 22, attempt 1

## Work performed

Declared claims: **C1 — calibration capability:** acquire a runnable, feature-bound typed credential reviewer rather than count authored criteria; **C2 — freshness:** reconcile revision-pointer drift and historical pin/expectation migrations without laundering unavailable source facts. Freshness and calibration tied at the lowest owned score, 9. Both scalar scores remain **9→9**; no statistical calibration gain or depth move is claimed. These are demonstrated engineering changes, **not author admission of the round**. Independent non-author closure must assess the disclosed safety/conformance deviations below.

- Corrected the previous outside admit disagreement: Actions public preview versus custom-OIDC public beta, Business prerequisites, named feature status anchors, product/token-type separation and Vault JWT-role versus OIDC qualifiers. Original E1/E3 bodies remain marked history; the active reading is `kagi-shokunin/corpus/knowledge/feature-bound-credential-review.md`. Evidence: `kagi-shokunin/corpus/lessons/round-22.md` §§Gate/Mistakes and `round-22-source-errata.md` §Gate; QUALITY QA10/QM13/QM14.
- Implemented `corpus/feature-claims.py` plus its reviewed JSON catalog. `--input` adjudicates one unlabeled, root-confined typed record against pinned sources/anchors; expected labels cannot be supplied by callers. Unknown/unjudgeable results are distinct from false claims and bar failures. Evidence: `kagi-shokunin/.ufo/waves/round-22/final-verification.json`, R22-01/R22-02, and the four `falsify/Mut*.md` reports.
- Added `corpus/revision-audit.py`: current-file SHA-256/LF/byte comparison, historical membership, strict path/regular-file handling, administrative-metadata/hardlink refusal and canonical full commit IDs. The before tree actually reports six stale pins, not the prior verifier's historical five: the later LOG change is the sixth. Evidence: `before-runnable.json`, `pin-only-ablation.json`, `final-verification.json`, R22-03/R22-04 under the round evidence directory.
- Explained the nine deleted diff lines: **nine same-path replacements, zero lost stamp members**. Preserved exact old/new rows, complete member sets and the four historical expectation changes; no fictional rows were restored. Evidence: `round21-migrations.json`, `historical-correction-pins.json`, `historical-membership-completion.json`, `pin-migrations-integration.json` and `pin-migration-errata.json`.
- Preserved every original pin member, corrected the six inherited mismatches, and journaled every changed current tuple. The outside verifier was a pre-existing unpinned artifact, not newly authored content; the separate retro-pin erratum corrects its initial null provenance. Final membership is 70 = original63 + seven reviewed pin additions. Evidence: R12-03, `pin-migrations-falsifier-repairs.json`, `pin-migrations-outcome-metadata.json`.
- Fresh falsification found FIFO hangs, invisible malformed/case-variant score headings, a metadata-fingerprint boundary, long SHA-256 abbreviations and ignored mode arguments. Original implementation identities repaired them in separate private clones. The exact blocked Round20 record remains; completeness/vacuity guards remain. Evidence: `falsify/SentinelClaimInput.md`, `RunCellsMalformed.md`, `SentinelHistoryInput.md`, and `heading-regressions-final.json`.
- Appended bounded historical-source/local-contract errata instead of relabeling unavailable host facts as current. Legacy source-header migration remains unclaimed and the credential detector was not weakened. Evidence: named Entry01–Entry24 build/falsify reports, `corpus/QUALITY.md`, SKILL's round-22 execution boundary and gate registry.

## Landed changes

All lane landings below are the helper's final **landed** hashes after push verification; diagnostic rewrite hashes are not cited.

| Landing | Changes / LOG linkage |
|---|---|
| `8ada17a50a25a75e6fc4a8cf880c87a85c67c8a3` | Initial source/active-reading corrections, executable reviewer and revision audit, parser support, reviewed integration pins and genuine build-wave evidence. LOG §22 and §Fresh-wave findings; measured freeze `integration-manifest.json`. |
| `4be5da3cac11a1db64c3e0a77246fd7f2bdee413` | Fresh-falsifier repairs, late S022/S023 source corrections, final authorized verification, explicit migration/receipt/privacy evidence. LOG §Round-22 fresh-wave findings and §Measured closure; this is the measured code/data revision. |
| `254d632ed2f6174e1ffcfe636a17b5e18284212f` | Measured SCORECARD/outcome metadata and reviewed pin refresh; code, catalog and ledger are byte-identical to the measured revision. LOG §Round-22 measured closure. Final lane landing. |

Only `scripts/hyaku/jj-lane.sh` committed/pushed the lane; this report uses the serialized fleet helper. No MANIFEST, fleet scripts/config/state, sibling repo, domain source tree or host configuration was edited by the integration owner. The mandatory unscoped fleet status sweep identified no owned misroots; only protected driver baseline paths were untracked, and none were read or changed (`fleet-misroot-sweep.json`).

## Before → after measurements

Run lane commands from `/home/vgpnk/Projects/shokunin/kagi-shokunin`. Full argv, output, expected exit/last-line expression and observed exit are committed in `kagi-shokunin/.ufo/waves/round-22/final-verification.json`. Before means the isolated immutable BASE tree `c2cab35bc92e57e39e5489bac3386db078345b3f`, not a moving mid-build tree.

| Claim | Before → after | Counting / exercise command | Measured revision |
|---|---|---|---|
| C1 calibration capability | executable reviewer absent → one working capability; after selftest12, four bounded controls admitted; ten bad controls refused (two false-claim, eight bar-fail); three unjudgeable boundaries excluded | `test -f corpus/feature-claims.py` on before/current trees (exit1→0), plus `python3 corpus/feature-claims.py --selftest`; `--phase before` exit1, `--phase after` exit0, `--phase boundary` exit2; independent `--input` mutation/control pairs | `4be5da3cac11a1db64c3e0a77246fd7f2bdee413`; code/data unchanged at final landing |
| C2 freshness/pointer integrity | stale6→0; missing0/dropped0; original63 retained, total70 with seven reviewed pin additions | `python3 corpus/revision-audit.py --root <tree> --history c2cab35bc92e57e39e5489bac3386db078345b3f` on exact before/current states; before exit1, after exit0 | measured code/data revision above; final post-metadata check at `254d632ed2f6174e1ffcfe636a17b5e18284212f` also CLEAN |

A fresh-session before tree can be reproduced by cloning the lane into an empty scratch directory with `git clone --no-hardlinks --no-checkout`, then checking out BASE **only inside that scratch clone** before invoking the current auditor with `--root <scratch>`. Never run that checkout against the live lane. `pin-only-ablation.json` proves C2 independently: only the isolated BASE pin snapshot changed, six stale became zero, no C1 file was copied. C1's initial working execution occurred while live pins were still stale.

Final authorized checks: **31/31 safe ledger rows passed**. Executed IDs: R11-05/07/08/09/10/11; R12-02/03; R13-01/02; R14-01; R15-02/03/04/05; R16-02/04/05/06; R17-02/03; R18-02/03; R21-01/02/03/04; R22-01/02/03/04. Duplicate ledger rows do not become extra unique test credit.

**Skipped, unexecuted by the integrator:** R11-01/02/03/04/06, R12-01, R15-01, R13-03, R16-01/03, R17-01 (host/substrate-dependent or transitively private); R18-01 (untagged host-private drift probe). No full live `verify` or `cells` is credited. R21-01 is the account-free plain-value byte fixture under isolated HOME/XDG, not a vault reference/account operation.

Actually observed selftests: ledger121, feature12, revision17, source47; safe inherited rows also pass drift13, op-ref36, checklist34, scope61 and transcript seeded/WAL fixtures. The identical retained heading inputs now match **17/17** expectations; nine former silent-clean attacks fail or expose unpointed cells, with positive blocked/completeness controls preserved.

Post-outcome-metadata checks, run against the final landing (all exit0):

```text
REVISION_AUDIT: CLEAN (stale=0 missing=0 dropped=0 added=7 invalid=0)
CITATION_GATE: CLEAN (cites=1215 docs=63 unresolved=0 ephemeral=0 labeled=13)
kagi\tok\t/home/vgpnk/Projects/shokunin/kagi-shokunin/corpus/SOURCES.md
```

Commands respectively: `python3 corpus/revision-audit.py --history <BASE>`; `bash corpus/claim-ledger.sh citations`; `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kagi`.

## Sources & frontier

Required fleet census, before and after: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kagi` → `kagi ok <lane>/corpus/SOURCES.md`, **exit0 both times**.

Lane census `bash corpus/sources-census.sh`:

```text
before: SOURCES_CENSUS: CLEAN (rows=16 A=14 B=0 C=2 queued=1 mined=14 rejected=1 entries_sourced=3 legacy=21) ; exit0
after:  SOURCES_CENSUS: CLEAN (rows=23 A=21 B=0 C=2 queued=1 mined=21 rejected=1 entries_sourced=4 legacy=21) ; exit0
```

- Added S017–S023: seven docs/A/mined correction or feature rows; original S001–S016 are full-line byte-identical. Distinct URLs **16→18**, not seven new websites/pages. The two new URLs are the [Actions feature page](https://www.1password.dev/brokered-access/github-actions/) and [custom-workflow feature page](https://www.1password.dev/brokered-access/custom-workflow/). The exact executable row/URL/tier/status `counting_argv` and both exit0 outputs are in `registry-census-details.json`.
- S017/S018 own status anchors, S019 setup eligibility, S020 dated announcement and S021 product/token-type context were opened this round; S022/S023 late corrections were author-opened and checked by the same fresh source identities. URLs, dates and located ≤25-word quotes are in `corpus/lessons/round-22.md` and `round-22-source-errata.md` §§Gate.
- Existing status/recheck/used-by fields did not change. Before first landing, new S017–S020 used-by changed from the round lesson alone to lesson + active review; each old→new is logged. S021 initially listed both. S022/S023 cite the new source-errata lesson. Rejected S008 remains a reason/flip row, independently reopened; S005 remains an unused tier-C lead.
- The custom-workflow unopened lead advanced to S018 with a preserved appended disposition. No OIDC-federation deployment, scanner, NIST or vault-structure coverage was absorbed. Legacy21 remains an explicit gap, not a fake header/depth gain.
- The local census is retained for entry/source reciprocity and corpus policy in addition to the fleet contract check; neither checker reopens pages or proves vendor truth. S020's per-response HTML digest is a capture attestation, not a live drift pin. Exact catalog/reference projection and product-versus-feature eligibility limits remain explicit.

## Trend verdicts

- **expansion — improved, bounded:** one demonstrated executable review capability enters the repertoire. Knowledge-coverage ground is unchanged; the new active entry corrects held E1/E3 ground, not new coverage. The earlier index's “unchanged” describes that coverage component, not repertoire growth.
- **quality — improved in the declared artifacts:** six stale pointers repaired with provenance, wrong source/feature/product readings superseded, actual fail-closed defects repaired, 31 safe rows and retained regressions pass. No source currentness is inferred from hashes.
- **discernment — improved, bounded:** the outside round-21 disagreement became QA10 with a lesson and genuine reject/control behavior; contradictory advisory receipts were challenged, withdrawn and quarantined rather than credited. This is **not** a new non-author agreement statistic or calibration scalar. Fresh outside spot-check/admission remains the parent's duty.

These are artifact-level lane verdicts. The safety deviations below are not erased by green engineering checks; the lane does **not** certify whole-round no-harm/conformance or admit its own round.

## SHONEN

- [~] Real decision tables/error patterns/checklists/cited sources — SKILL's domain tables, active feature review, gate registry and QA10; final citation command CLEAN. No named non-author promotion verifier this round.
- [~] End-to-end domain task executed/logged — outside E1/E3 rejection → opened primary feature/product sources → local typed reject/control executions → corrected handoff in LOG §22 and this report; earlier negative auth-gate task remains historical. No live credential workflow claimed.
- [~] Executable without oral context — documented `--input`, root/path constraints, gate commands, pinned catalog and selftests; `final-verification.json` plus retained fixture bytes. Outside closure still pending.
- [~] No cross-domain ownership absorbed — PROVINCE preserves browser/research-method/scanner/terminal-action boundaries; connector findings corroborate. Unauthorized legacy host-gate invocations are disclosed below, not treated as compliance proof.

## Wave accounting and safety/conformance

- **Build:** validated policy-v2, one atomic task call, **64 seats**: scout40, executor3, scribe4, reviewer7, critic4, connector4, sentinel2. L1 KagiR22 held the canonical planner seat; no forbidden planner swarm role. Sixty reports returned; four scribe seats died: DraftE1, DraftE3, DraftCriteria, DraftHistory. Actual last error: `anthropic/claude-haiku-5-5` HTTP429 `rate_limit_error`, “This request would exceed your account's rate limit. Please try again later.” `retry-after-ms=8211000` (DraftE3 8212000). Dead seats were never respawned or credited; L1 authored the missing bounded prose.
- **Falsify:** dispatched only after build returns/integration, separately validated, one atomic task call, **66 fresh seats**: reviewer25, scout21, mutation-tester4, executor8, critic4, connector2, sentinel2. All66 returned; no dead fresh seats. Four independent input mutants were killed with valid controls retained. The actual new CriticNoTrade ID was `KagiR22.CriticNoTrade-2`; one initially guessed registry ID was corrected from the original task receipt by registry-only rerender/record, **no extra task dispatch**.
- **Round:** 130 unique seats, zero capacity refusals, no wave shrinking/splitting/padding or model parameter. Original implementation/source identities resumed for private fixes and bounded final-row checks; those are continuity, not replacement seats. Specs, registries, original spawn receipts, freeze and summaries are under `kagi-shokunin/.ufo/waves/round-22/`.
- **Uncredited/unsafe verification:** ReopenSource20's unknown `revision` token defaulted to full verify; AttackActiveReview's alleged two-row positional selection also ran the full path including private R18-01. AttackActiveReview then asserted impossible history/selection semantics; both claims were withdrawn and its report is not used to verify this round. Complete private-surface receipts were not retained, so **no clean whole-round secret-access attestation is inferred**. No private/account data was re-read to reconstruct it. The new positional guard rejects such mistakes before reads. See `review-evidence-quarantine*.json` and the amended reports. No vault/account operation or retained credential value is reported, but the authorization breaches stand.
- **Scratch collision:** FixCellParser's initial tar extraction targeted `/tmp/kagi-shokunin`, not its assigned clone. Prior contents/effects were unobserved; the unexpected directory was preserved, no unsupported loss/restoration claim made, and the same identity continued only in its assigned private clone. Parent confirmed it was not using that path.
- **Install/update record:** no L1 install. Build Entry07 reports an unnecessary `opencode` version launcher probe bootstrapped **node@26.12.0 via mise** and resolved opencode-ai via npx (version not established; no system installation claimed). No pacman transaction, service restart or boot write was reported. No host rollback or clean-impact certification is claimed. Falsification context explicitly prohibited those launchers/package tools and host loopback probes; earlier refused passive health/CDP observations are disclosed in the lesson.
- **Privacy:** four reference-shaped example spans in two build reports were redacted before H1, with no original path retained/printed; final added-material sweep found no prohibited token/reference/private-key material. Evidence is counts-only. Legacy generic documentation is not relabeled as freshly scanned by adding headers.
- **Stale-lane:** this is the in-session r22 mission only, with landed activity and no other kagi round opened by this session; no r23 work started. Shared helper hold was respected until Main's verified release. No promotion or MANIFEST write.
- **L0:** no new operator question appended. Independent closure must rule on admission/safety deviations before progression; inherited operator-owned terminal actions and contested browser lease remain unassigned here.
