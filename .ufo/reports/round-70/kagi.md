# kagi — round 70 report (attempt 1, L1 `KagiR70`)

Lane repo `/home/vgpnk/Projects/shokunin/kagi-shokunin`, branch `master`. Claim BASE
`7bd34832c94b81d4cf9bf34113c4952a7f6d9b04` (round-69 spot-check tip). Final lane hash:
`66f0662b2038c85e98173c3240da610a10989b7c` (`git -C kagi-shokunin ls-remote origin refs/heads/master` → `66f0662b2038c85e98173c3240da610a10989b7c	refs/heads/master`; `jj-lane.sh state` → `local=remote=66f0662b… ahead=0 behind=0`).

## Work performed

**Declared claim (one):** **C1 — coverage, capability acquisition: OpenBao PKI certificate
lifecycle, executed.** Frozen predicate (`plans/round-70.md` §C1 = header of `plans/round-70-c1.sh`):
`C1_PKI_TRIAL: value = number of tests T in {T1..T5} that DISCRIMINATE, when PINS = 1 and
SETUP_OK = 1 and NOSECRET = 1 and NOLEAK = 1 and SOURCED = 1, else 0; target 5 (BASE 0).`
Wording as filed is narrowed by plan Amendments A1–A3 (below). Sourced claim: S170 (opened this
round). No exploratory claim.

- **Freeze before candidate, with executed controls.** Plan, counter (sha256 `8412b665…7192ed`)
  and controls runner landed together with eight executed prefreeze controls in
  `430cee23eeb81ecf663015851e66332bf16f2a74`; every control matched the expected verdict written
  into `plans/round-70-controls.sh` before its first run: F0 BASE `value=0 absent=1` rc 1; P1
  positive reference `value=5` rc 0; F1 echo forgery, F2 shim-sniffing forgery, F3 no-teeth trial
  all `value=0` rc 1; F4 unsourced `sourced=0`; F5 leaking server `noleak=0` (six leaked servers
  reaped); F6 printed token `nosecret=0` (`.ufo/waves/round-70/controls/receipts/*.txt`).
- **Candidate** `0d225553c22f686df24454040102d0502eda5c42`: `corpus/openbao-pki-trial.sh` (T1
  `root/generate/internal` returns no CA private key; T2 a 24h request on a `max_ttl=1h` role is
  issued ≤ 3660 s; T3 a CN outside `allowed_domains` refused while one inside is issued; T4 a
  revoked serial on the mount CRL; T5 a `no_store` leaf not found by serial while a stored control
  is), entry `corpus/knowledge/openbao-pki-certificate-lifecycle.md`, registry rows S170/S171/S172,
  captures `.ufo/waves/round-70/capture/`. Counter on the candidate: `value=5` rc 0
  (`.ufo/waves/round-70/final/c1-candidate.txt`).
- **Measured domain fact.** OpenBao 2.7.2 does not refuse a `ttl` above the role `max_ttl`: it
  issues the leaf clamped to `max_ttl` (observed 3630 s) with the warning `TTL "24h0m0s" is longer
  than permitted maxTTL "1h0m0s", so maxTTL is being used` and exit 0, although S170 says the ttl
  "Cannot be greater than the role's max_ttl value" (`.ufo/waves/round-70/final/l1-probe-observations.txt`).
- **Wave `kagi-r70-w1`, 12 seats** (one v1 wave; validator `counts.spawn=12`,
  `.ufo/waves/round-70/w1-dispatch.json`). Every seat filed a report with `SEAT-STATUS: complete`
  (`.ufo/waves/round-70/w1/*.md`). Attack findings that falsified the claim's **wording** (not its
  number): R70Critic CR-1…CR-11 (entry sentences the counter never reads), R70MutTester MT-1 (T5's
  conjunction is a disjunction at the counter; 6/8 mutants killed), R70Revenger RE-1 (forgeries A
  shim-byte map, C transport bypass, D wrong observable each reach `value=5` — the count does not
  prove execution), R70Sentinel SE-1 (a squatting server would still read `value=5`), SE-2 (dev
  root token on the server argv), SE-3 (NOSECRET reads streams only), R70Connector CN-1 (S105
  already registered the PKI API URL). Each is narrowed in `plans/round-70.md` Amendments A1–A3 and
  reconciled in `.ufo/waves/round-70/claim-falsification.tsv`.
- **Integration** `ba8c73052f4feef5472889d58c3ec475b4f064e0`: entry title scoped to one dev mount,
  every Measured line split into counter-enforced vs observed (receipted), consequence column
  sourced or `[INFERENCE]`; trial launch hardened to the lane's round-52 pattern (token by
  environment only, `-dev-no-store-token`, kernel port + `ss` pid ownership check, `setpriv
  --pdeathsig KILL`, `umask 077`; M70-6); repairs of the harm R70ExecGates measured on the
  candidate (GX-1 docs audit unpinned → stamps pins; GX-2 release-clock unbound → S170/S171 recheck
  `180d`); SKILL.md four PKI decision rows; PROVINCE core line; README coverage-map row and counts;
  SCORECARD round-70 sections + capability row; LOG; lesson; QM101.
- **Counter on the landed revision** `ba8c7305`: `C1_PKI_TRIAL: value=5 discriminating=5 pins=1
  setup_ok=1 nosecret=1 noleak=1 sourced=1 real_rc=0 none_rc=2`, all five
  `real=HOLDS,shim=BROKEN,spec=1,entry=1`, rc 0 (`.ufo/waves/round-70/final/c1-landed.txt`).
- **Harm checks** (`.ufo/waves/round-70/final/`): on the integration tree `ba8c7305`, the
  `claim-ledger.sh verify` FAIL/POLICY/SETUP set matched BASE, but the same receipt carried eight
  `STALE` stamp lines BASE did not (my first diff filtered them out — M70-7; R70ScribeSkill SS-10
  named them; `stamps-recheck.txt`). The eight rows were re-pinned in `17a89648`, and the full
  verify on that revision reads `CLAIM_LEDGER: POLICY (claims=102 policy=5 stamped=177)` rc 2 (BASE: `stamped=173`, POLICY rc 2) with 0 STALE lines and a verdict-class set (FAIL/POLICY/SETUP/STALE/NOT-A-FILE by id) identical to BASE (`claim-ledger-verify-final.txt`, `claim-ledger-verify-final-vs-base.txt`). Also on the landed
  tree: `claim-ledger.sh docs` `DOC_AUDIT: CLEAN (entries=50 row_linked=47 by_hand=3 …
  unpinned=0)`; `plans/round-36-c3.sh` `RELEASE_CLOCK: CLEAN (on_release=32 bound=32 …)`; R36-01
  reads 8 at BASE and 8 on the tree (GX-3's timeout is runtime near the 300 s budget,
  `harm-rechecks.txt`); self-description sweep `MISMATCH n=28 (SD5=4 SD6=23 SD8=1)` equal to BASE
  (`self-description-sweep-landed.txt`); self-counts `stale=4 setup=0`, the same four ids as BASE;
  `claims-declared.sh` adds no mismatch (the round-69 pair is carried).
- **Planner seat:** the L1 held it (the validator rejects `planner`); the bounded planning data
  walk (sibling overlap, frontier recon) rode R70Connector and R70Scout.
- **Corrections to the round-69 report (routed by its spot-check §5 items 1–2; QM97 — the
  superseded sentences stand in that report):** "eight `falsifies-wording` rows" should read six
  `falsifies-wording` + two `falsifies-number` (13 rows: 6/2/5 by
  `awk -F'\t' '$1 !~ /^#/ && NF>0 {print $3}' .ufo/waves/round-69/claim-falsification.tsv | sort | uniq -c`);
  "two pre-existing W04 warnings on S156/S164" should read 25 W04 warnings (S019…S164) by
  `grep -c W04 .ufo/waves/round-69/final/census-round-end.txt`. Mined as M70-2/M70-3.

## Landed changes

| commit (`landed` line of `jj-lane.sh`) | content | LOG.md entry |
|---|---|---|
| `430cee23eeb81ecf663015851e66332bf16f2a74` | freeze: `plans/round-70.md`, `plans/round-70-c1.sh`, `plans/round-70-controls.sh`, control fixtures + receipts, round-start census receipts | `LOG.md` `## round 70` — "Freeze before candidate" |
| `0d225553c22f686df24454040102d0502eda5c42` | candidate: trial, entry, S170–S172, fetch rows, captures | `## round 70` — "C1 (met, wording narrowed)" |
| `ba8c73052f4feef5472889d58c3ec475b4f064e0` | integration: Amendments A1–A3, hardened trial, entry narrowing, stamps/recheck repairs, SKILL/PROVINCE/README/SCORECARD/LOG, lesson, QM101, wave dir | `## round 70` — all bullets |
| `17a89648d2ce9ec7f43044759b1dedea8179138a` | settlement `kagi-r70-w1-results.json`, landed-revision receipts (`final/c1-landed.txt`, census end, verify, sweep), eight stamp re-pins, lesson M70-7 | `## round 70` — "Frontier", "Mistakes mined" |
| `66f0662b2038c85e98173c3240da610a10989b7c` | final receipts on `17a89648` (`final/c1-final.txt`, `final/claim-ledger-verify-final.txt`) | `## round 70` — "C1", "Mistakes mined" (M70-6/M70-7 appended, LOG stamp re-pinned) |

## Before → after measurements

| claim | counting command | BASE (`7bd34832`) | after | measured against |
|---|---|---|---|---|
| C1 coverage | `bash plans/round-70-c1.sh <rev>` | `C1_PKI_TRIAL: value=0 absent=1 pins=1`, rc 1 | `C1_PKI_TRIAL: value=5 discriminating=5 pins=1 setup_ok=1 nosecret=1 noleak=1 sourced=1`, rc 0 | `17a89648d2ce9ec7f43044759b1dedea8179138a` (`final/c1-final.txt`; same reading on `ba8c7305` and `0d225553`) |

Verdict (L1 reading, not admission): **target met on the frozen counter; wording narrowed** — the
claim filed is the count of five shim-discriminating trial verdicts, not proof that any trial
passing the counter executed PKI mechanics (RE-1, SE-1). That the landed trial does execute them
through the `bao` CLI rests on non-author reading (R70Reviewer RV-5 on the candidate bytes;
the post-wave hardening diff is for the closure to review).

Pre-file falsification gate: `python3 scripts/hyaku/prefile-falsification.py --lane kagi --round 70 --wave kagi-r70-w1` → `PREFILE-FALSIFICATION: pass claims=1 rows=10 attack_seats=7 findings=0`, exit 0. Ledger `.ufo/waves/round-70/claim-falsification.tsv`: 10 rows — 5 `falsifies-wording` (Critic, MutTester, Revenger, Sentinel, Connector; all narrowed in `plans/round-70.md` A1/A3), 1 `falsifies-number` (ExecGates: gate harm on the candidate, repaired; not the C1 value), 4 `neutral` (`awk -F'\t' '$1 !~ /^#/ && NF>0 {print $3}' .ufo/waves/round-70/claim-falsification.tsv | sort | uniq -c`).

## Sources & frontier

- Census command (fleet): `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kagi`.
  Round start: stdout `kagi ok`, 25 W04 lines on **stdout**, stderr 0 bytes, **exit 0**
  (`.ufo/waves/round-70/base/census-round-start.{stdout,stderr}.txt`, `.rc`). Round end: stdout
  `kagi	ok	…/corpus/SOURCES.md`, 26 W04 lines (the 26th is S170 — same URL as S105, cross-scope),
  stderr 0 bytes, **exit 0** (`.ufo/waves/round-70/final/census-round-end.{stdout,stderr}.txt`, `.rc`).
- Lane census: `bash corpus/sources-census.sh` → BASE `SOURCES_CENSUS: CLEAN (rows=160 …)`, end
  `SOURCES_CENSUS: CLEAN (rows=163 A=145 B=2 C=16 queued=3 mined=141 rejected=19 entries_sourced=29 …)`.
- Rows before → after: 160 → 163 (`grep -cE '^ {0,3}\| *S[0-9]{3}' corpus/SOURCES.md`). Added by
  tier: A +3 (S170 mined, S171 mined, S172 rejected with flip). Rows touched old → new: S170
  `recheck` on-release → 180d, S171 `recheck` on-release → 180d (same round, GX-2); no existing
  row changed (S105 unchanged).
- Frontier advanced: OpenBao PKI moved from unheld ground to an executed core trial (PROVINCE
  "Core, round 70" line; README coverage-map row; SCORECARD capability row). Frontier leads for the
  next PKI round (non-default issuer CRLs, `leaf_not_after_behavior`, ACME without a token,
  auto-tidy windows, delta CRLs): `.ufo/waves/round-70/w1/R70Scout/frontier.md`.
- Gate decisions for spot-check: admit S170, admit S171, reject S172 (`corpus/lessons/round-70.md` §Gate).
- Mistakes mined: M70-1…M70-7 (`corpus/lessons/round-70.md` §Mistakes), each with a check shown
  able to fail; QM101 enters `corpus/QUALITY.md`.
- Assimilation: none (no `merge/kagi/` theme taken; `considerthese/` not mined this round — latest
  file `considerthese/2026-10-26.md`).

## Trend verdicts

- **expansion: improved** — new admitted entry `corpus/knowledge/openbao-pki-certificate-lifecycle.md`
  on ground the coverage map did not hold, with its coverage-map row (QM100); knowledge files 49 →
  50 (`ls corpus/knowledge/*.md | wc -l`); registry 160 → 163; one new executed trial.
- **quality: improved** — the freeze carried eight executed controls (positive and forgery) before
  any candidate byte, the claim's wording was narrowed to what the instrument enforces on the wave's
  own evidence, and the trial's launch hygiene was raised to the lane's round-52 bar; landed-tree
  gates match BASE (verify failure set identical, sweep n=28, self-counts stale=4).
- **discernment: unchanged** — the round rejected S172 for scope with a flip and caught its own
  over-wide wording before filing, but it also appended S170 without searching the registry for the
  URL (M70-1), froze a counter with three uncovered forgery classes while naming one (M70-5), and
  its own first harm diff missed eight STALE stamp lines a seat had to name (M70-7).

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — evidence: SKILL.md `## Vault-ops decision table` gains four PKI rows citing `corpus/knowledge/openbao-pki-certificate-lifecycle.md` (commit `ba8c7305`); asserted by the author, no non-author verifier named.
- [~] At least one end-to-end domain task executed and logged in LOG.md — evidence: `LOG.md` `## round 70` — `corpus/openbao-pki-trial.sh` run against OpenBao 2.7.2, `OPENBAO_PKI_TRIAL: HOLDS holds=5` (`.ufo/waves/round-70/final/c1-landed.txt`).
- [~] Instructions executable by an agent without oral context — evidence: R70ExecReplica wrote an independent trial from S170 and the plan alone and the frozen counter read `value=5` (`.ufo/waves/round-70/w1/R70ExecReplica.md` RX-1).
- [~] No cross-domain bleed (PROVINCE.md still accurate) — evidence: `.ufo/waves/round-70/w1/R70Connector.md` CN-2/CN-3 (no sibling holds PKI-engine ground; kake owns the TLS consumer side, named in the PROVINCE core line).

## Round shape and other required lines

- Round shape: ONE v1 wave `kagi-r70-w1`, 12 seats, validated under
  `scripts/hyaku/ufo-wave-policy.json` (band 8–16); residual call: none; round total 12. Role mix:
  2 reviewer, 1 critic, 1 mutation-tester (attack 4/12 = 33 %), 1 sentinel, 1 revenger,
  1 connector, 2 executor, 1 scout, 2 scribe. Dead seats: none (`kagi-r70-w1-results.json`: 12 seats, every one with a non-empty final output; every report ends `SEAT-STATUS: complete`).
- Settlement: WAVE-DONE received from the orchestrator after the last seat (R70ScribeSkill) settled; results `/home/vgpnk/Projects/shokunin/kagi-shokunin/.ufo/waves/round-70/kagi-r70-w1-results.json` (committed in `17a89648`). The report was filed after WAVE-DONE.
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` showed no untracked
  file written by this round's seats (only `.scratch/` and pre-existing modifications, untouched).
- Scratch: `/fast/scratch/hyaku/kagi-r70` removed by the L1 after landing.
- Tool installs: none (no seat reported an install).
- Open L0 questions: none new.
- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
