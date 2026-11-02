# Audio historical completion reconciliation — 2026-11-02

## Result first

**Carry forward 94–95 documentary completed-round candidates, not 100 passes.** The range now concerns r1's missing original reviewer report, **not r71**. R71 has a durable owning-integrator final disposition in LOG, despite stale provisional subordinate documents. Six numbers **87,88,93,98,99,100 remain explicitly unadjudicated**. Their substantial work and reviews are real; neither their green subsets nor this audit supplies the missing terminal decision. An evidence-backed honest REJECT is a completed substantive attempt; an orphan, preliminary gate failure or unadjudicated review is not automatically one.

Read-only investigation: no repository scripts executed, no new training, counters, lane/fleet changes, publication, runtime probes, credential or session-store reads. Only this audit file was written. All paths below are relative to `/workspace/scratch/e2fdad13233f/shokunin-training/`; `A/` means `lanes/audio/`, `F/` means `shokunin/`. These conclusions refine, rather than silently overwrite, `audit/four-historical-lanes.md`.

Evidence snapshots:
- Audio HEAD `f9da7ee97e0ba95da1803c2afe9c616c519bae18`.
- Fleet HEAD `46193bc3170020dd2b02de9f000df02b041f167e`.
- Both report `git rev-parse --is-shallow-repository = false`. This establishes complete **available reachable** histories, not custody of the original pre-split repository or every old object.
- Searches included all reachable history in audio, fleet and the recovered `kimi-shokunin` repository for `**/audio-r1-verifier.md`. No original report object/path was found. No protected store was searched.

## 1. R71 terminal review resolved, with document conflicts retained

`A/LOG.md:1157–1184` declares the second-decoder content-versus-suffix claim and work. Crucially, **:1181–1184** says “Verdict: ADMIT … Verifier AGREE 3/3 … (Sol final, wave-10).” This text was introduced in actual report-last commit **`c079abafdcabe5f6afc45d1a8cea6a0af8ee4847`**, not newly reconstructed by this audit (`git show c079abaf -- LOG.md`). It names D1–D3 corrections at **`77768fafa54be43647851b8bf876ecc4b9a2b8b8`** and 84/85 identical shared modes, with the remaining difference disclosed as fifo-hold transition jitter.

Counterevidence remains visible:
- `A/reports/round-71/r71-adjudicator.md:14–19,41–42` says post-landing seats pending and **provisional ADMIT**.
- `A/SCORECARD.md:718–727` still says provisional; `A/LOG.md:1176,1179–1180` retains obsolete probe-score-null and seats-pending text immediately before the final ruling.
- `F/.ufo/reports/round-71/audio.md:13–17` likewise retains the old probe-score error and pending seats. Its initial fleet landing is `7ad01410`; later deletion/restoration commits `35b91714` / `f47ad6ba` do not constitute a new adjudication.

Independent review actually exists: `A/reports/round-71/r71-verifier.md` §§Items1–3 records measured content invariance, prior-r67 stability, fifo hygiene and D1–D3; the verifier explicitly discloses measuring intermediate uncommitted work. `r71-boundary.md` independently confirms D1/D2 corrected at 77768fa and 60/60 hold-sweep legs. `r71-critic.md` reports post-correction state c079aba and residual ASLR normalization defect F1, stale-receipt F2, vacuous accept-half F3, class collapse F4, and qualified stability F5. **`50f55eb9c13441047619448eba51f6e457732395`** subsequently fixes the late critic's module-tag normalization finding. Do not label that late fix independently reverified merely because it landed.

**Conclusion:** r71 qualifies as a documentary completed, substantively reviewed attempt with historical final ADMIT and disclosed defects. A fresh replay-certified admission is not established here. Owning-integrator adoption should append cross-references correcting stale status; it must not erase the earlier provisional report or pretend every requested seat landed.

## 2. R1 original reviewer custody: partial recovery, not invented closure

`A/LOG.md:9–18` records declared seam thresholds, author before/negative-control/restore, named non-author `audio-r1-verifier`, independent pass, and three exact verifier receipts. `A/SCORECARD.md:16–25` gives the historical axis verdicts and the missing `.shokunin/reports/audio-r1-verifier.md` pointer.

Actual round1 work commit **`57ef9c5d88285353116e1029852c43430358faf5`** includes all three cited receipts, fixture/artifact work, LOG and SCORECARD. Original reviewer prose is not included. Historical `A/reports/round-24/r24-history.md:5–13,26–33` explicitly attests an original branch `craft/audio-r1`, a different mint `0f60e765…`, and one tracked addition of that exact reviewer report. This is evidence that the report once existed in a broader original tree; it is not the report itself. The preserved split history starts with different mint `6e71ed4c`; absence here cannot refute the original history witness.

Recovered receipt paths under `A/corpus/live/runs/` at round1 commit:

| Directory / measurements.json | SHA256 |
|---|---|
| `20261012T155752390616Z-normal` | `ab01c27bc3a5843c7babad52b6bdf4895b6dee9077bb0fbc1f8e935b9bf95c1e` |
| `20261012T155752784838Z-failing` | `bc733f7babb6403bf9f9119f7e3699950ecbdf0b49e61dc6d14ecc4688cf54dd` |
| `20261012T155753181244Z-normal` | `ab01c27bc3a5843c7babad52b6bdf4895b6dee9077bb0fbc1f8e935b9bf95c1e` |

The normal/restore receipts are byte-identical; the control carries measured failures including spectrum and seam endpoint jump. These measurements support the LOG-attested review sequence; JSON alone does not independently authenticate which worker ran it. `F/.ufo/waves/kaika-w1/audio-state.md:217` independently records the dead reviewer pointer.

**Conclusion:** r1 is a credible historically completed, LOG-attested candidate, not an invented pass. Conservatively withhold it if original reviewer custody is mandatory: **94**. With acceptance of contemporary LOG plus preserved controls and r24 historical witness: **95**. This audit does not impose or waive the integrator's documentary standard. Remaining custody action: recover the ordinary project Git repository/backup containing original `.shokunin/reports/audio-r1-verifier.md` and original mint/branch, if available; do not search credential/session stores or substitute a new review as the lost original.

## 3. Frozen final-review custody is better than the leaf reports imply

`A/LOG.md:1535–1541` and **`928dde536a028b3ce0c60aac9c346d1b1a5355f1`** preserve twenty advisory reviews and four byte-identical verifier receipts. `A/reports/final-review-evidence.json:1–12` expressly says these are not native judgments and do not verify subsequent repair bytes. All four local receipt bytes were hashed in this audit and match that manifest:

| Path under A/reports | SHA256 |
|---|---|
| `round-93/r93-verifier-receipt.json` | `37efaabcd6ec119708f80d98d26edfb274260c85633b54b0b78649f9238f15a8` |
| `round-98/r98-verifier-receipt.json` | `8520d7c8bf6c59a0f931df62e5333a0f74135b610c33f1cf974a2bd54435561e` |
| `round-99/r99-verifier-receipt.json` | `2b304e9f8ecf6868fb6f5577a29c3ad3c2152c32a81f67a5228b4fc4ee3c5f58` |
| `round-100/r100-verifier-receipt.json` | `42f284789dc1ef0217b0ad4848454a72c563ff2f4c278273d105da02b33a2b25` |

Historical review pin `bb177513a615a32d3bc150ecbdcf78302e110d8c` is **not an available object** (`git cat-file -t` fails). Extant safety commit **`7d7ed474d7a477f9bfe21c24e252993a123dd3c3`** has `corpus/fixtures/measure_audio.py` SHA256 **`801e153b84368bba4a77e85c129376612c797694c435e9104cdad6e62169be2f`**, exactly matching the preserved review-source hash. That is a verified **file-content bridge**, not proof that the two commit identities or complete trees are identical. Future adjudication must use available pins and disclose historical citation translation.

## 4. Six unfinished round dossiers and actual remaining gates

For every row below, terminal decision is still absent: `A/LOG.md:1594–1622`; `A/SCORECARD.md:897–918,965–974,1020–1050`. R101 explicitly preserved that set, including r87/88 failures. Current fleet MANIFEST has audio rows62–65 and101; its r101 admission says C1 historical calibration, 18 unadjudicated axis rows. It does not admit six predecessors. Fleet STATE `:54–66` corroborates their original missing adjudicators.

### R87 — device-binding lattice
- Frozen **d1e687b9** verdict remains **GATE FAIL**, not reproducible green: `r87-verifier.md:20–56`. Four of seven committed-byte runs red; truncated pw-cli log windows and one midi-pin event. Critic ADMIT-with-findings was an opinion, not adjudication (`SCORECARD:906`).
- Combined landed fold **`1977cf4206f5bde37b94debb30139633ca5d85c0`**; `r87-fold.md:21–42` documents full-log refusal matching, post-EOF nonvacuous sysex, self-exit skeleton, explicit missing-data blocks, raw-edge checks, cold-own-id/collision premise repairs, and later green105-leg run under concurrent r88 churn. Receipt sha `895deece0eedb48e5cf9c86077cb15831d1371006fbd74922be69c279601d61c` is a historical report citation, not freshly replayed here.
- Remaining: bind fold report and committed bytes, reconcile original red controls with post-fold evidence, independently rule scope and residual co-tenancy/coverage limits. Can close a substantiated rejected attempt without forcing a win; cannot silently convert the old failure to a pass.

### R88 — Bluetooth absence / witness differences
- `r88-verifier.md:20` preserves reproducibility GATE FAIL although encoded laws passed. Critic recommendation is nonterminal (`SCORECARD:918`).
- Same1977cf42 fold; `r88-fold.md:21–43` repairs dump stable-core membership, foreign stderr separation, latest-error precedence, bounded-frame blocks, enumeration truncation, device-evidence absence and missing-leg checks. Reported green post-fold receipt sha `dded6f2cff9773436cd4ee01a0a97840d2f158f2be74b31ed1e74ae76bacefcc`.
- Remaining: adjudicate bounded claim; `r88-fold.md:55–68` says scrub was armed but never fired in that verification, strict subset/transients may remain blocked, populated-host enumeration can still truncate. Review the negative-control evidence rather than equating co-tenancy alone with executed scrub coverage.

### R93 — ebur128
- Advisory frozen run: `r93-verifier.md:40–50,87–115`,9 entries/90 keys, with notify refusal and duplicated g_default block; no admission. Key count is not90 fully measured laws.
- Subsequent failure/cleanup folds are real: `LOG:1507–1518,1570–1579`; `r93-failure-fold.md:49–55,57–90` preserves an introduced optional-refusal regression and its correction; offline90-row replay is not new native audio. Latest entry repair **`1a974ff6a234f10267006433b47304d0f36affd7`**, source SHA `4e0614f83680964d0edabc1f3942d3b01b8b582ac2ae4c1742e7858bf16306ab`, has nine injected cleanup cases and unchanged scientific-body ASTs.
- Remaining exact review inputs: g_default silent tap/audio-domain gain, one-sided decay band, silent-arm predicates, label scope and repetitions (`r93-critic.md:F3–F5,F7,F10`; reviewer L2); late pw-cli/double-load and final-communicate, header exceptions before cleanup and main receipt writer (`r93-entry-cleanup-fold.md:43–46`). Distinguish fixed entry teardown from universal containment. Independently review the repaired pin and explicitly decide narrowed claims versus rejection; do not relabel old native receipt as repair verification.

### R98 — pw_stream
- Frozen verifier `:51–99` records profiler JSON truncation and xrun ratios unmeasured, plus missing-parent lock bypass. Later shared-lock and cleanup folds address specific safety paths; not a full remeasurement.
- `r98-scope-fold.md:41–77`, latest **`9d92c8baf278af2dc49a3a7b09d17b3ab171ddf2`**, source SHA `72b23e043447557a9c3560e0633cac1fb7d94c964fe9b24f6b4439b7b5dc0007`, binds coordinator names/env; five failing subcases repaired, one private emission witnessed. Preserve prior ENAMETOOLONG setup failure. Do not repeat the obsolete assertion that this is merely selector-only: `LOG:1547–1558` records subsequent producer-name scope work.
- Remaining: profiler/capture blocks and negative-control reachability; entry/main exception receipt containment (`r98-cleanup-fold.md:44–49`); independently adjudicate reader exit-code/empty graph, xw transient guard, fallback t_id witness and timing bounds (`r98-critic:F5,F7`; reviewer M3/M4). Scoped naming observation is not independent full-family certification. Recover/qualify author worktree receipt citations (`r98-verifier:101–115`) separately from the now-preserved verifier receipt.

### R99 — RTP
- Frozen verifier `:41–112` found missing lock, confirmed exact default-off LAN guard, and disclosed that earlier author/integration receipts actually ran physical-LAN controls. Preserve the increased historical control count (`LOG:1542–1546`); no new control is needed to make the ledger look cleaner.
- Loopback fold and changed-entry receipt (`r99-loopback-fold.md:46–65`) establish authored scoped peak0.5, safe default-off control, and teardown—not an independent six-entry replay. Current extant loopback commit **`76b48c6bc8ee1c20e3105fad2d5978b288951c99`**, source SHA `5646861d7c2c914162fea5acd1f5d68a6ff76378acb196dfad73a84e0b9ff86c`.
- Missing-witness fold **`561f44b115e1efcbac2a84af6c20aee1e304da99`**, source SHA `9f242022408b7447cc9afeac44a34d353c37bd8b8cf60efa8e04c3bd780933ec`, addresses missing-client/sink/counter cases, measured flags, exceptions (`LOG:1559–1569`).
- Remaining: adjudicator must check original C1 leak classification against repaired branch-order controls; trace C2/C8 to missing-witness fold, reconcile quantitative author/control mismatches (critic C3/C4), qualify e_sap environment classification (C6), unarmed settings witness (reviewer F5), and main receipt-on-exception limits. Decide default-off LAN coverage as an honest block, not a pass. **Do not enable physical-LAN control under this audit or merely to close a round.**

### R100 — SOFA/spatializer
- Frozen verifier has **9 entries/37 legs**, `r100-verifier.md:49–69,137–174`, not merely3 legs. Three clock legs are the **later changed-entry repair observation** (`LOG:1500–1506`). This corrects the imprecise shorthand in the prior inventory/SCORECARD evidence description without changing status.
- Witness/setup-unwind fold exists at **`781d08804157e5e559d505ef78ca75cd512706ea`**, source SHA `a8760b120fbbb47d091f6d0a674e3630d4fd20b9ee6e366df0f6c57371a019f9`; clock-repair receipt preserved. `r100-witness-fold.md:48–71` expressly limits it to authored3-leg observation, not independent verification of all repairs.
- Remaining explicit inputs: universal entry/receipt exception containment, external termination, no-config/IR-latency missing scope, record-only real shared-store writes, narrow clock margin and original author-receipt custody (`witness-fold:50–56`; reviewer F3/F5/F8; critic F8 tautological n_samples). Assess fully-blocked summary/exit semantics against declared gate, not raw rc0. No perceptual/spatial-audio quality claim is supported by these signal fixtures.

Shared safety fold `A/reports/round-100/shared-lock-fold.md:35–39` itself says lock failure may still exit before receipt and universal containment remains separate. Extant source commit **`cd25a307b4cad49fcfec89354cfddca7f2fed6cd`**, SHA `f753f9a9695d47c0d892833f5347c78fb536e3622d99ccd0f965b24735e8f254`. A corrected lock does not certify every scientific law or exception path.

## 5. Next sequential actionable plan (not executed)

1. Owning integrator adopt the r71 final-LOG evidence and explicitly choose r1 custody treatment, preserving94–95 range until that decision. Append documentary correction only; no historical counter reset or claimed fresh admission.
2. Resume **r87**, then **r88**, then **r93**, **r98**, **r99**, **r100** under their original numbers, one adjudication packet at a time. Each packet: original claim/pin, failures, available content-hash bridge, corrected pin, exact review finding→fold or unresolved mapping, preserved controls, and a non-author terminal review. Prefer already-preserved substantive evidence; demand targeted replay only for the decision-critical unverified changed behavior. A justified narrowed/rejected terminal disposition is acceptable; an administrative closure without substantive review is not.
3. Before any new runtime work, freeze available bytes and confirm environment prerequisites/allowed effects. Keep all historical receipts immutable. r99 physical-LAN opt-in stays off; named coverage blocks survive. Do not replace missing receipts with copied unrelated green runs or label a software injection as native audio.
4. **Stop the100-completed milestone when the integrator has100 evidence-backed terminal attempts**, not100 successes. Starting at94 requires all six; starting at95 needs five, but the remaining unresolved number must stay visible rather than be quietly counted. If continuing to close all six is authorized, finish the existing open loop before proposing fresh breadth work.
5. If additional genuinely new training is then necessary, next unused numbered round is **102**, not87 recycled as a new claim and not a rerun of1–100. Prioritize substantive game-audio depth/breadth (e.g. a predeclared signal-to-game-use limitation with independent negative controls), not another counter-only or ledger-only exercise. Choose the exact claim after the unresolved packets determine actual remaining capability gaps.

No new gate verdict or adoption was issued by this audit. R71 resolution and four recovered receipts are available now; r1 original report custody and six terminal decisions remain the bounded open work.

Final read-only QA: all **20/20 preserved advisory-report SHA256s** also match `reports/final-review-evidence.json`; audio/fleet `git status --porcelain` both empty after audit. Round1 work, r71 final report-last, r87/r88 fold, frozen-review preservation and available safety-source bridge commits above all pass `git merge-base --is-ancestor <commit> HEAD` (exit0). No author/fold runtime observations were replayed.
