# kaidoku — round 24

Lane-relative paths below resolve under `kaidoku-shokunin/`; wave paths under `.ufo/waves/round-24/`. Fresh held claim, attempt1; no predecessor/inherited replacement work. L1 identity KagiR27-2 was reassigned by Main after completing kagi27; no later kagi work performed.

## Work performed

Declared two distinct-axis claims in `kaidoku-shokunin/.ufo/waves/round-24/claims.json` (freeze `5dc49bfe25d21139693161c786e69c5a11a65bcc`), BASE `fe10219ec6e92c32b7eb40d83fbcac888756c6c1`. Owned finite proxies coverage/depth/calibration tie10.0; coverage is tied-lowest, no stagnation waiver (last capability17, window10).

- **R24-C1 coverage: measured 0/4 → 4/4 held for the finite REA6.5.0 packet-capture family** (`inspect-pcap-client`, `inspect-pcap-capture`, `inspect-packet-fields`, `inspect-packet-capture`). This is not a replacement for the frozen R23 six-verb denominator, which stays4/6, nor network-forensics mastery. Score10.0→10.0. Evidence: `corpus/knowledge/2026-10-21-r24-pcap-family-envelopes.md`, `final/after-c1.json`.
- **R24-C2 calibration: instrument-freeze audit/disclosure, original frozen-byte target NOT MET; disclosed revised-byte target met author-side.** Prior cohort0/10→10/10 disclosed, plus new round24 CLEAN. Original gate at final:9/11 exact, exit1; revised gate:11/11, exit0. Both retained; closure must adjudicate the disclosed supersession, not silently substitute the revised result. Score10.0→10.0. Evidence: `corpus/claim-freezes.tsv`, `final/after-c2-frozen.json`, `after-c2-revised.json`, lesson §Residual review.
- Installed cmake4.4.4 via `uv tool install cmake`; built TShark/capinfos4.6.9 from official Wireshark source into `~/.local/opt/wireshark-4.6.9`. Source SHA256 matches signed SIGNATURES; gpg good signature from a keyserver-fetched Gerald Combs key, without independent fingerprint anchor or web-of-trust path. No pacman transaction. Launcher hashes plus three local library hashes retained; system dependencies remain unpinned (`tool-pins.json`, source S064).
- Produced five original REA6.5.0 envelopes and adjacent byte-equal stdout/run records (`evidence/c1/l1-*`) on three committed Wireshark test captures and the installed registry. Client observation is pathless/null-subject, not artifact-bound. TLS input contains embedded secrets applied by TShark; no lane-supplied key/decryption capability claimed. Reviewer replay reproduced all five IDs and normalized results, not duration bytes (`residual/KagiR27-2.ResC1Envelopes-2.md`).
- Routed r23 defects: restored three README blank separators; committed instruments before freezing claims with SHA256 pins; documented/pinned and re-fetched six external input streams (APKs, sigrok AppImage, Godot archive/member, Wireshark source), with negative checksum control (`repro/inputs.json`, `receipt-2.json`, `final-script-controls.json`). Sigrok recording/synthetic bytes are already tracked. Runtime inputs are not promised to exist in a fresh clone.
- Residual review corrected `-T fields`→`-T json`, conditional `-2`, capinfos-derived counts/times, tool-version validation, timestamp span2002–2018 and separate discovery output budgets. S069/S070/S072 supersede immutable initial rows; S071 reverses the mistaken capinfos rejection. Fetcher symlink/regular-file overwrite/delete, partial cleanup and error typing repaired and rechecked by the same reviewer (`residual/KagiR27-2.ResRepro-2.md`, final-script-controls).
- Executed final snapshot producer12/12 expected conditions, post-hoc L1 selftest17/17, prior no-harm controls, preservation-loss controls, legacy counters and census. Evidence: `final-producer.json`, `final/`, lesson §Final executed measurements.

## Landed changes

All own-lane commits through `scripts/hyaku/jj-lane.sh`; tied to `kaidoku-shokunin/LOG.md:2763` and final delivery `:2789`, SCORECARD round24 `:2885` and final outcome `:2912`.

| Landed commit | Changes / LOG tie |
|---|---|
| `97ade2e5e2dcf6cfd01d0da8634879d14969f9cc` | Counting instruments, producer, tool provenance **before claims** (LOG instrument bullet). |
| `5dc49bfe25d21139693161c786e69c5a11a65bcc` | Frozen C1/C2 declarations, SHA256 pins and actual before records (LOG instrument bullet). |
| `74cd4e33e7114a1cb2c451ea85fd8bd7d3b736a7` | L1 original envelopes/capture bytes (LOG C1 bullet). |
| `9fb4eacd23eb69ee9d659dd041e006e9ccd61480` | Gate supersession1: bare-name instruments reported UNRESOLVED rather than NONE; later appended disclosure in claims.json (LOG C2 bullet). |
| `69e82c48be5614ce96f7c1c32445fe61c4870630` | Initial knowledge/sources, ledger, QUALITY33, lesson, route docs, reproduction receipts, wave specs/refusals (LOG claim bullets; residual seats reviewed this candidate). |
| `5c88c05b8cff9ebd63521c1395fc5295eaded8c3` | Residual factual/source/reproduction repairs, seat reports, byte-bound repro receipts, final producer and post-hoc selftest, LOG/SCORECARD; **measured source** (LOG final delivery). |
| `1e1bbef45ea0b92e443cdca04b814e74dfecbca1` | Final12-check receipts, census, causal overlays, seat census, append-only measured-outcome text (LOG final delivery). |

Final helper: `landed 1e1bbef45ea0b92e443cdca04b814e74dfecbca1`.
Lane `main`: local=remote=`1e1bbef45ea0b92e443cdca04b814e74dfecbca1`, ahead0/behind0, tracked0/untracked0. Last commit adds evidence/outcome text only; no instrument/runtime changes after the measured revision.

## Before → after measurements

Measured source **`5c88c05b8cff9ebd63521c1395fc5295eaded8c3`**, BASE **`fe10219ec6e92c32b7eb40d83fbcac888756c6c1`**. Executed committed producer bytes (SHA256 in `final-producer.json`) in a removed shared clone under `/fast/scratch/hyaku/kaidoku-r24/`:

```sh
python3 -I -B .ufo/waves/round-24/tools/final-measure.py --root <LANE> --rev 5c88c05b8cff9ebd63521c1395fc5295eaded8c3 --out <NEW-DIR>
```

Observed **exit0,12/12 expected finite conditions**. This includes the expected **red** original-instrument C2 result; producer success is not an assertion that every frozen claim passed. Exact executable hashes, argv/cwd/exits/stdout/stderr in `final/*.json`.

| Claim | Counting command | Observed before → after |
|---|---|---|
| R24-C1 | `python3 -I -B .ufo/waves/round-24/tools/count-c1.py --root <LANE> --rev <REV>` | held0/4 (c1_incomplete, exit1) →4/4 (c1_complete, exit0); exact four-verb set as declared. Lexical zero-mention16→12 is separate, not held coverage. |
| R24-C2, revised | `python3 -I -B .ufo/waves/round-24/tools/freeze-gate.py --root <LANE> --rev <REV> --require-clean round-24 --disclosures corpus/claim-freezes.tsv` |0/10 disclosed/exit1 →11/11/exit0. Unchanged historical cohort10/10 all FLAGGED plus new round24 CLEAN; this is ledger agreement, attainable by transcription, not independent verification. |
| R24-C2, original frozen bytes | Same command using the script blob from freeze `5dc49bfe` | At after revision9/11 exact/exit1: revised R17/R18 codes disagree with frozen instrument. **Original frozen-byte criterion not met.** |

C2 original before record and revised before record both retained. Supersession changes historical finding codes (NONE→UNRESOLVED), not historical verdicts or0/10 before value. Round24 was FLAGGED at `9fb4eacd` before the supersession disclosure landed. Instrument ordering exists in Git history; frozen `declared_at` literal16:50Z is wrong (freeze finalized16:44:44Z), disclosed rather than used as timing proof.

Controls and no-harm:
- Post-hoc L1 selftest17/17. It was written after observing candidate69e82c48; not a frozen independent oracle.
- R23 counter stays4/6 (same held set, incomplete exit1); R22 C1 stays1/6 (exit1), C2 dispositions14/14 (exit0).
- Prior1141 files identical; old32 QUALITY criteria retained, +33; LOG/SCORECARD prefixes preserved; map106/106→107/107, citation rules17/17. Whole old SOURCES lines and prior README nonempty rows retained; all README h2 separators blank. Named loss controls red. `final/prior-controls.json`, `preservation-controls.json`, `readme-sources.json`.
- Separate C1-only/C2-only overlays executed by ResSeparability-2: C1 counts4/4 without C2 deliverables; C2 returns11/11 without C1 envelopes. Declared edges: C2 audits C1 instrument history; C1 parses whole SOURCES registry, so malformed S068 causes setup failure (deleting it does not). Retained `evidence/separability/`, residual report.

## Sources & frontier

**63→72 registry rows**, nine added tierA (A57→66, B5/C1 unchanged); mined61→70, rejected2 unchanged. Six source families, three supersessions (S069/S070/S072), no existing committed status/recheck/used-by cells edited. Counting recipe: compare `^| S[0-9]+ |` rows in Git blobs at BASE/measured source; `final/readme-sources.json` records63/72. New rows opened this round; access date, located ≤25-word quotes and decisions in lesson §Gate plus residual correction addenda, retained bodies/metadata under `sources/` and `evidence/tool/`.

S064 release identity; S065/S069 tshark manual; S066/S070 installed REA providers; S067/S072 own envelopes/client qualification; S068 preregistration; S071 capinfos manual. Capinfos rejection reversed after review demonstrated its flip condition (summary counts/times depend on it). Search log groups six families explicitly; initial exclusion and mistaken argv scopes remain historical/superseded, not rewritten. Frontier move is a finite offline packet-capture family; debugger ownership remains unresolved. C1 is sourced from S064+ rows naming its knowledge entry in used-by.

Mandatory census command:
```sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kaidoku
```

**Start conformance defect:** no live start run before source edits. `measure/start-census.json` records an explicitly later BASE-clone reconstruction (same script, copied fleet config), exit0; not presented as a start-time execution. Output:
```text
kaidoku W04 S033 duplicate url github.com/NationalSecurityAgency/ghidra/pull/9348 across scopes
kaidoku W04 S047 duplicate url go.dev/dl/?mode=json&include=all`, across scopes
kaidoku W04 S054 duplicate url developer.android.com/ndk/guides/abis across scopes
kaidoku W04 S062 duplicate url raw.githubusercontent.com/sigrokproject/sigrok-cli/sigrok-cli-0.7.2/doc/sigrok-cli.1 across scopes
kaidoku ok /fast/scratch/kaidoku-r24/census-base-root/kaidoku-shokunin/corpus/SOURCES.md
```

**Live end exit0** (`measure/end-census.json`, actual tab-separated raw output, census script SHA256 recorded):
```text
kaidoku W04 S033 duplicate url github.com/NationalSecurityAgency/ghidra/pull/9348 across scopes
kaidoku W04 S047 duplicate url go.dev/dl/?mode=json&include=all`, across scopes
kaidoku W04 S054 duplicate url developer.android.com/ndk/guides/abis across scopes
kaidoku W04 S062 duplicate url raw.githubusercontent.com/sigrokproject/sigrok-cli/sigrok-cli-0.7.2/doc/sigrok-cli.1 across scopes
kaidoku W04 S069 duplicate url www.wireshark.org/docs/man-pages/tshark.html across scopes
kaidoku ok /home/vgpnk/Projects/shokunin/kaidoku-shokunin/corpus/SOURCES.md
```
Four→five duplicate-URL warnings, no error. New S069 is an explicit same-manual supersession.

Mined mistakes M24-1 instrument-after-claim, M24-2 separator loss, M24-3 scratch-only reproduction, M24-4 own regex gap in lesson; original absent instrument, pin/revision/disclosure negatives and checksum/containment controls actually fail. No extra coverage credit for negative/refusal probes. Fresh outside admission sample remains pending.

## Trend verdicts

- **expansion: improved** — new saved-capture family ground,107th knowledge entry, four actually held verbs (not merely four mentions); R23 remainder unchanged.
- **quality: improved** — source/argv/decryption distinctions corrected by residual review; executable no-harm and input re-acquisition controls retained; limits not suppressed (`final/`, `repro/`).
- **discernment: unchanged** — historical instrument debt now visible and author-side critics found real mistakes, but revised-instrument C2 needs independent adjudication and no fresh outside admit/reject sample yet exists. No scalar.

## SHONEN

- [~] Real decision tables/error patterns/checklists/cited sources — SKILL round24 route, S064–S072; no named independent promotion verifier.
- [~] End-to-end domain task — original saved-capture→REA envelopes→bounded interpretation in knowledge entry, independently replayed by an author-dispatched reviewer; not outside admission or live traffic work.
- [~] Executable without oral context — byte-bound final producer, recorded argv, reproduction manifest/receipts; bounded post-hoc oracle limits disclosed.
- [~] No cross-domain bleed — PROVINCE round24 dated holdings and Adjacent exclusions; kaidoku/revenger L0 unresolved; no box checked by these seats.

## Concurrency, conformance and remaining limits

- Validated BUILD85: executor25/scout19/reviewer15/critic8/mutation-tester2/sentinel1/connector6/scribe8/simplifier1. **20 atomic refusals, zero spawns**, exact error `Background job limit reached (100). Wait for running jobs to finish or cancel one.` Unchanged validator taskCall per retry, slot acquired/released. No dead seats invented from refused spawns.
- Ordinary residual8: critic4/reviewer4, refused once then spawned on try2, **8/8 reports, dead0, replacements0**. Same-identity ResRepro follow-ups add no seats. Exact identities/results in `wave-outcomes.json`, `residual-dispatch.json`, `residual-task-result.txt`; L1 held planner. **64–100-seat heavy-wave floor unfulfilled**; landing bounded work under explicit20-refusal rule, not claiming swarm completion. No second padded wave.
- No model parameters/routing edits. Host roles selected routes; later global routing updates do not retroactively change captured seats. No provider-death claim this round.
- C2 limitations: path forms outside narrow regex, forged supersession hash, later claim-text edits, same-commit-versus-strictly-prior distinction; twelve arc3 `claims-frozen.md` files excluded from frozen round*/claims.json cohort. All eleven actual verdicts independently agreed. Future gate hardening named, not silently implemented after measurement. Claim instruments are not themselves a complete no-harm gate; final producer separately runs preservation checks.
- Literal load-order/tooling-process defect: L1 did not read the complete canonical load-order bundle or RULES.md before installing cmake/building Wireshark. Official channels/no-pacman policy respected; this is disclosed, not a full compliance attestation.
- Fleet no-pathspec misroot sweep found only operator `.ufo/state/*`/watchdog edits and Souji's round22 report, no owned misroot. All left untouched. No sibling/domain repo edits or pushes.
- Removed this round's heavy scratch `/fast/scratch/kaidoku-r24` and `/fast/scratch/hyaku/kaidoku-r24` after retaining measurements/reports/overlay scripts. Installed Wireshark prefix intentionally remains as the usable tool. Removed own /tmp smoke artifacts earlier; no other lane scratch touched.
- **Stale-lane:** only assigned kaidoku24 worked; round25 not started/claimed.
- **Open L0:** existing kaidoku/revenger shipped-artifact/debugger ownership overlap remains unresolved; no new question blocks this offline work. R22's102 reportless seats remain uncredited.
