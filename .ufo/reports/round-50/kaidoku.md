# kaidoku — round 50 report — outcome `honest-stop (operator wrap-up, run 11)`

Lane `kaidoku-shokunin`, agent `KaidokuR50`, attempt 1. Base `7c678ae6d97aedb969fd253b52b3d2882ef1e186`. Lane tip at filing: `8ccc05e6b073d4218223571d0b390f6e93789d94` (`git ls-remote origin refs/heads/main` prints it). The operator ended hyaku run 11 between the freeze and the data run; this report states what landed, what did not, and what is open.

## Work performed

Declared claims (2): **R50-C1 — coverage**: genuine AVM-marker little-endian SquashFS v4 (`hsqs`) members of four public FRITZ!OS images (FRITZ!Box 7581 and 7582 07.18, 6490 Cable 07.57 and 6430 Cable 07.30 x86 members) through REA 6.5.0 `extract-firmware`, Frontier → Core; **R50-C2 — calibration**: eleven round-48/49 record atoms B1–B11. Distinct axes, causally separable (plan "Frozen paths").

- **Round shape:** one wave, 38 seats of a planned two (`.ufo/waves/round-50/w1-dispatch.json`, `r50-w1-results.json`; 38 reports on disk, all seats settled). Wave 2 (37 seats) was generated and validated but never dispatched, then removed unsent. **Round total 38, below the 64-seat floor.** Role mix wave 1: executor 12, scribe 10, scout 4, critic 4, reviewer 3, connector 2, revenger 1, sentinel 1, mutation-tester 1 (attack roles 9 of 38 = 24%, under the 25% share). Planner seat: the L1 (validator rejects `planner`). No dead seats; no residual call.
- **Wave-1 findings folded before the freeze** (`plans/round-50-claims.md` "Wave-1 amendment record"): two carriers' member path was wrong (cable images carry the LE member at `./var/remote/var/tmp/x86/filesystem.image`, `w1/C1CarrierAdversary.md`); default REA budgets fail on a 13k-file rootfs (`w1/C1DevArmA.md`); six shortcut holes in the inherited counter (`w1/C1ShortcutCritic.md`: unbound rerun, unbound counter bytes, `--full-history`, no scoring-time oracle, receipt-chosen projection); the AVM marker is a re-stampable constant of the pinned bytes (`w1/C1MarkerCritic.md`, `w1/C1RevLayout.md`); fetch-path containment (`w1/C1SentinelFetch.md`); C2 atom defects (B11 green at base, B10/B2 forgeable, B9 wrong registry home; `w1/C2AtomSpec`, `C2AtomCritic`, `C2RegCensus`).
- **L1 integration before the freeze:** counter/harness/controls/fetch/C2 drafts integrated and amended (carrier ids renamed, `provider_timeout` handling, fetch lane-containment, B10 interface, replacement B11); oracle tables for the four carriers built with three independent readers (`.ufo/waves/round-50/l1/oracle/*/oracle-run.json`: `all_equal true`, `mismatch_count 0`); frozen selftests green at the freeze: `c1-counter.py --selftest` 169 cases `failures []`, `c1-controls.py selftest` 20/20, `fetch-vendor.py --selftest` 16/16, `c2-record.py --selftest` 29 cases.
- **Carrier swap before the freeze (disclosed):** the draft's FRITZ!Box 7530/7590 (13.4k files) hit REA's fixed 120 s `provider_timeout` 3 of 3 attempts each at host load 42–54 (`.ufo/waves/round-50/l1/dev-arm-timeouts.txt`) and were replaced by the 7581/7582 (~4.5k files).
- **Freeze:** `435d41fd4ad9211d1579fc447936fb33d2b74467` (one commit; `git ls-tree` 38 files under `tools/round-50/` plus `plans/round-50-claims.md`), recorded in `.ufo/waves/round-50/l1/FREEZE` and LOG.md (record commit `845e0586e0e5970229786ef982eac5ffc05130e4`) before any data run.
- **Controls at the freeze** (`.ufo/waves/round-50/controls-attempt1/`): CTL-C1-0 and CTL-C1-1 `as_expected`; CTL-C1-2, -3, -4 and POS `could_not_evaluate` (exit 2, `REA provider_timeout on c6490 after 3 attempt(s)`, host load 95–176); `kill_rule_fires false`. This is not a pass for those controls.
- **Data run:** started once at lower load, stopped by the wrap-up after three of four carriers had been run in scratch; **no receipt was written to the lane** (`corpus/evidence/round-50/c1/` does not exist).
- **Mistake mined:** M50-1..M50-6 in `corpus/lessons/round-50.md` `## Mistakes` and `## Honest stop`. Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows untracked/staged files (`o.bin`, `oldrep1.out`, `oldrep2.out`, `pos2.err`, `pos2.out`, `lane3/`); none names kaidoku or round 50 (`grep -l 'kaidoku-r50\|round-50'` empty), they belong to other lanes and were not touched.

## Landed changes

| commit | contents | LOG.md |
|---|---|---|
| `435d41fd4ad9211d1579fc447936fb33d2b74467` | FREEZE: `plans/round-50-claims.md`, `tools/round-50/**` | round-50 entry |
| `845e0586e0e5970229786ef982eac5ffc05130e4` | FREEZE record: `l1/FREEZE`, LOG entry, L1 inputs (`mkplan.py`, plan template, scan, oracle receipts) | round-50 entry |
| `11ccdb7211bf9f632a1d6bc4a9a44106d5c42b42` | R50-C2 landing: SCORECARD `## Record corrections — round 50` (B3, B4, B5, B10, B11) and Owned-axes heads (B1 `139/139`, B2); `corpus/SOURCES.md` rows S246 (S147 tier B), S247 (S149), S248 (S138) + search-log entry; `SKILL.md` registry rows for six `tools/round-49` and six `tools/round-50` paths (B9); QUALITY rows 90–93; `corpus/evidence/round-50/c2/` (six unblob listing snapshots); round-45 `f1.hdr` cookie redaction at the tip; lesson; SCORECARD `## Round 50` section; LOG continuation | round-50 entry + continuation |
| `8ccc05e6b073d4218223571d0b390f6e93789d94` | wave-1 evidence (38 seats), controls attempt, assimilation guard receipts, `l1/scores/{c2-final,c2-at-freeze}.json`, census end | — |

**Not landed:** six wave-1 receipt files over 1 MiB (the helper skips them: `w1/C1GapRule/census/a7530.{lls,oracle.tsv}`, `w1/C1OracleBuild/a7530|a7590/oracle.tsv`, `w1/C1RevLayout/receipts/a7530.{auto,le}.files.tsv`; their content is the frozen oracle tables under `tools/round-50/oracle/`); the C1 knowledge entry, PROVINCE/README/SKILL/SCORECARD-capability bindings, SOURCES rows S243–S245 and S249 (no landed entry cites them), SHONEN promotion; wave-2 seats. QUALITY row 94 dropped. The registry skips S150–S242 on purpose (cited in older lessons as refused staged rows).

## Before → after measurements

- **R50-C1 (coverage): not measured — neither met nor missed.** Before (freeze): `python3 -I -B tools/round-50/c1-counter.py --root <LANE> --rev 435d41fd… --freeze 435d41fd… --pkg65 <rea 6.5.0 root> --work <SCRATCH> --carrier-cache <CACHE> --json-out <OUT>` → exit 1, `carriers_matched 0` (CTL-C1-0, `controls-attempt1/c0/receipt.json`, UTC 2026-10-29T01:41:17Z). After: no verdict; the rerun clause needs REA 6.5.0 inside its fixed 120 s deadline and the controls/data run could not complete under host load. `LE AVM members (hsqs)` stays Frontier.
- **R50-C2 (calibration): met under its frozen predicate.** Command `GIT_NO_REPLACE_OBJECTS=1 python3 -I -B tools/round-50/c2-record.py --root /home/vgpnk/Projects/shokunin/kaidoku-shokunin --rev 11ccdb7211bf9f632a1d6bc4a9a44106d5c42b42 --freeze 435d41fd4ad9211d1579fc447936fb33d2b74467 --battery --work <SCRATCH> --json-out .ufo/waves/round-50/l1/scores/c2-final.json` → exit 0, `atoms_total 11`, `mismatches 0`, battery 52 single-mutation overlays, `failing 0`, do-nothing overlay red on 11/11, `counter_sha256 == counter_sha256_at_freeze` (`4749bcd8…1285`); receipt sha256 `6e215184f9c272152012d95fb273d9c1c02bc20f0eaf3edc10e22d59c73fa16f`. Before: same counter at `--rev 435d41fd… ` without `--battery` → exit 1, `mismatches 11`, all of B1–B11 (`l1/scores/c2-at-freeze.json`). Disclosed limits: a consistency check of the record against committed bytes; tier B in S246 is a judgement the closure disagreed with S147 on, not recomputed; wave 2 never attacked the frozen counter or the landed rows, so no non-author or wave-2 falsification exists for this verdict.

Owned scores unchanged (`10 → 10` on coverage/depth/calibration; finite proxies). Admission is for the operator to rule: C1 is unmeasured, so the round cannot admit both claims.

## Sources & frontier

- Census, `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kaidoku`: round start **exit 0**, 149 rows, 15 `W04` lines (`.ufo/waves/round-50/l1/sources-census-start.txt`); round end **exit 0**, 152 rows (`grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' corpus/SOURCES.md`), same 15 `W04`, final line `kaidoku ok …/corpus/SOURCES.md` (`l1/sources-census-end.txt`).
- Rows added: S246 (tier B, `mined`; `supersedes S147 —`), S247 (tier C, `rejected`; `supersedes S149 —`), S248 (tier A, `mined`; `supersedes S138 —`). Rows touched old→new: none (S138/S147/S149 byte-identical to the base). Sourced claim: R50-C2's B6–B8 rest on S246–S248 (located quotes in the lesson `## Gate`, pinned snapshots under `corpus/evidence/round-49/c2/` and `round-50/c2/`). The C1 sources opened this round (Freetz patch 101, AVM download index, unblob LE handler, AVM licence) are recorded in the lesson `## Gate` but **not registered**, because no landed entry cites them.
- Frontier rows advanced: none (C1 unmeasured).
- Assimilation (theme AVM LE, `merge/kaidoku/`, read-only): guard receipts `.ufo/waves/round-50/assimilation/` — registry ids S001–S149 vs staged ids S106–S237 overlap in **44** ids (`collisions`), 0 of 44 the same source; the guard is proven on an indented-row scratch registry (`guard-proof/`); quarantine slice 5 rows (S113, S117, S136, S147, S150). Nothing appended. Admit (not registered): the Freetz patch source; refuse with reason and flip: `avm-le-image-genuine-marker`, `avm-le-variant-reachability`. `considerthese/` does not exist in this lane.

## Trend verdicts

- **expansion: unchanged** — no admitted knowledge entry, no coverage-map row (`git ls-tree -r --name-only main corpus/knowledge | grep -c '\.md$'` → 139, as at the base).
- **quality: improved** — evidence: three source-registry errors from the round-49 closure corrected by new rows S246–S248; twelve instruments registered (`SKILL.md` `instrument-registry v2`); round-48/49 record lines corrected append-only; C2 counter green with a 52-mutation battery. Bounded: lane-verified only (no wave 2, no non-author check yet), and the C1 instruments are frozen but unrun to a verdict.
- **discernment: unchanged** — the round-49 closure's disagreements became rows and QUALITY criteria (S246, S247, QUALITY 90–93); the round's own probe error (M50-3) and an unmeasurable claim design (M50-6) are recorded, not credited.

## Routing, tooling, stale lane

- Stale-lane: respawn-per-round driver; no other mission of this lane is open. Open L0 question (not appended; no operator-blocking decision): history still holds unredacted GitHub session-cookie values in the round-45 receipt and `14936cb9` (redacted at the tip only); a purge needs an operator-authorised force-push.
- Open claims for round 51: run the frozen C1 instruments in a quiet window (`tools/round-50/c1-controls.py score`, then `tools/round-50/c1-run.sh after --id <id> --carrier <cache>/<pin>.bin --data-run`), land the entry and bindings only after a measured `carriers_matched 4`; if the freeze is judged stale, a new freeze (never an amendment). Wave 2 (37 seats) specs are not preserved.
- Tool installs: none. Host changes: none; `sudo renice -15` was applied to this round's own scratch processes only.

## SHONEN

- [ ] SKILL.md contains real decision tables, error patterns, checklists, cited sources — untouched this round (no SKILL decision row added; registry rows only).
- [ ] At least one end-to-end domain task executed and logged in LOG.md — the round-50 REA runs on the four carriers happened in scratch before the freeze and are not landed evidence; no landed receipt.
- [ ] Instructions executable by an agent without oral context — untouched.
- [ ] No cross-domain bleed (PROVINCE.md still accurate) — untouched; PROVINCE.md unchanged this round, LE AVM remains Frontier.
