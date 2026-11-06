# revenger — round 100 (hyaku run 15, attempt 1)

Lane repo `/home/vgpnk/Projects/shokunin/revenger-shokunin`, branch `main`. Base `0350014d30e91da411ee624025d8d1bb7afc6ccf`
(the r99 closure spot-check tip). Claims freeze `05e854ce31a6ad997a28544b4edd104aaff1be81`; instrument freeze
`173abe91a80d79336ca9228643c63d41e0e7635c`; landing `a5e91dd818637031d779a58970c639b04261254d`; wave evidence and final
lane hash `cdb0774b0bbde2797f2e3a1ad660487a7bbccfbf` (verified by `ls-remote`). Round shape: one v1 wave, 12 seats, no residual call.

## Work performed

Declared claims (`reports/round-100/claims.md`, frozen at `05e854ce`):
- **C1 — calibration:** the admission counter's reach over the round-99 fresh holdout. Frozen v8 accepts 12/12 →
  new v9 counter accepts 0/12, with both honest controls, the stub self-test and three no-regression conjuncts.
- **C2 — capability acquisition (coverage):** `apk-manifest-cross-decode` — androguard 4.1.4 and apktool 3.0.3 decode the
  authored APK `corpus/fixtures/apk-r65/fixture.apk` and agree with its `truth.json`; an in-probe same-length tamper must
  be reported by both decoders. `SCORECARD.md` capability table 4 → 5 rows. This is the round's sourced claim (S508, S509).
- **Axis choice:** every owned criterion sits above the 7.0 saturation line (K 14/15, F4 11/11, M 3/3, A1v2 5/5) and no
  capability had entered since round 91 (N = 3), so the AXES.md stagnation nudge waives the lowest-axis obligation.
  ReviewerClaimsR100 recomputed this premise from SCORECARD.md and ruled it `sound` (`.ufo/waves/round-100/w1/ReviewerClaimsR100.md` §2, §9).

Work items:
- Protocol load: the round prompt, fleet MISSION/AXES, the lane SCORECARD (r95–r99 sections), SHONEN.md, LOG tail,
  `corpus/lessons/round-99-verifier-spotcheck.md` (routed defects §5), the r99 wave spec and holdout builder, `skill://swarm`.
- Pre-freeze do-nothing controls committed with the claims: `reports/round-100/controls/c1-do-nothing-v8.log` (v8 12/12,
  sha-pinned r99 receipts) and `controls/c2-base-capability-rows.log` (4 rows, probe absent). Round-start census:
  `controls/census-round-start.log`.
- Wave w1 validated (`UFO_CONFIG_PATH=…/ufo-wave-policy.json … ufo-swarm-wave.mjs run --spec .ufo/waves/round-100/w1-spec.json`,
  rc 0, 12 spawns) and handed off through `.ufo/waves/round-100/w1.ready` (dispatched 19:44:28).
- Builders: ExecCounterV9 (`reports/round-100/c1_k_admit_counter9.py`, 12 new legs, one per r99 class), ExecHarness9
  (`forge_reach9.py`), ExecApkProbe (`cap_apk_probe.py`), ExecControlsR100 (`controls_c2.sh`, `census_line_check.py`).
- Pre-freeze L1 rulings (disclosed in the lesson Gate): (1) `C1_DERIV_RERUN` applies only when the entry declares a
  verbatim-stdout cell rule, because forge_reach8's c14 honest control (the r98 Amendment C entry `1b76b4d`) is not
  derivation-clean by the lane's own `deriv_check.py` (`DERIV_MISMATCH=8` of 17) and declares no such rule; (2) the probe
  was rebuilt to run decoders with `cwd=<scratch>` after a lane-root `androguard.log` appeared (M24); (3) ReviewerClaimsR100's
  harness-fingerprint report F1 was routed to ExecHarness9, answered NOFIX with line references, and later retracted by
  the reviewer.
- Post-freeze L1 runs (`reports/round-100/controls/post-freeze/`): C2 controls, the C2 probe at the freeze and on the landing
  tree, the C1 target run, three no-regression conjuncts, a per-vector rc receipt, the round-end census.
- Attacks (reported, not targets): CriticR100 fresh r100 holdout and attacks A1/A2; ReviewerCapR100 three probe attacks;
  MutationR100 pre-registered mutants (`MutationR100/mutants.json`, written 20:13, before the 20:20 freeze); SentinelR100 sweep.
- Sources opened this round by ScoutSourcesR100: androguard `axml` docs and the Apktool wiki (receipts
  `.ufo/waves/round-100/w1/ScoutSourcesR100/`); the L1 re-checked both located quotes with `grep -c -F` (1 each).

## Landed changes

| commit | what | LOG.md entry |
|---|---|---|
| `05e854ce31a6ad997a28544b4edd104aaff1be81` | claims freeze + pre-freeze do-nothing controls + census start | `LOG.md` `## Round 100` (claims bullet) |
| `173abe91a80d79336ca9228643c63d41e0e7635c` | instrument freeze: v9 counter `8e2eafc8…`, `forge_reach9.py` `3acdd3a9…`, `cap_apk_probe.py` `b2c9d189…`, `controls_c2.sh` `479f690e…`, `census_line_check.py` `c3b754aa…`, wave spec/dispatch | `LOG.md` `## Round 100` (claims/instruments bullet) |
| `a5e91dd818637031d779a58970c639b04261254d` | landing: SCORECARD r100 section + capability row, SOURCES S508/S509, `corpus/lessons/round-100.md`, four SKILL registry rows, LOG entry, post-freeze logs | `LOG.md` `## Round 100` (result bullet) |
| `cdb0774b0bbde2797f2e3a1ad660487a7bbccfbf` | wave evidence (`.ufo/waves/round-100/`, seat findings and receipts, `w1-results.json`) and the mutation row | `LOG.md` `## Round 100` (wave bullet) |

## Before → after measurements

| claim | before → after | counting command | measured against |
|---|---|---|---|
| C1 | `accepted` **12/12 → 0/12** | `PYTHONUTF8=1 python3 -B reports/round-100/forge_reach9.py --counter reports/round-100/c1_k_admit_counter9.py --work <scratch>` → twelve `R100_VECTOR … refused legs=<class leg>`, `R100_ACCEPTED=0/12`, `R100_CONTROL_C02=control-ok`, `R100_CONTROL_C14=control-ok`, `R100_STUB_SELFTEST=ok`, `R100_VERDICT=met`, rc 0 (`post-freeze/c1-v9-frozen.log`). Before: `controls/c1-do-nothing-v8.log`. No-regression: `--self-test` → `SELFTEST_C1V9=OK legs=128`, rc 0 (`noreg1-selftest-v9.log`); `forge_reach8.py --counter <v9>` → `C2_ACCEPTED=0/12`, both controls ok, `C2_VERDICT=met`, rc 0 (`noreg2-forge8-v9.log`); `--profile c14r99 --tree <git archive 173abe91>` → `C1_K_HELD_BACKED=14/15`, `C1_VERDICT=pass`, rc 0 (`noreg3-c14r99-freeze-archive.log`) | clone at `173abe91` (instrument freeze) |
| C2 | rows **4 → 5**; probe absent → `CAP_APK_VERDICT=pass`, rc 0 | `awk '/^## Capabilities/{f=1;next} /^## /{f=0} f && /^\| / && !/^\| Capability/ && !/^\|---/' SCORECARD.md \| wc -l` → 4 at `0350014d`, 5 at `a5e91dd8`; `PYTHONUTF8=1 python3 -B reports/round-100/cap_apk_probe.py --fixture corpus/fixtures/apk-r65 --work <scratch>` → `CAP_FIXTURE_SHA=pass`, `CAP_ANDROGUARD=pass`, `CAP_APKTOOL=pass`, `CAP_TAMPER_DETECTED=pass`, `CAP_APK_VERDICT=pass`, rc 0 (`post-freeze/c2-probe-landing.log`, `c2-probe-freeze.log`). Controls: `bash reports/round-100/controls_c2.sh reports/round-100/cap_apk_probe.py <scratch>` → `C2_CTRL_STUB=refused`, `C2_CTRL_FLIP=refused`, `C2_CONTROLS=control-ok`, rc 0 (`post-freeze/c2-controls.log`) | `0350014d` → `a5e91dd8`; probe on clone `173abe91` and on the landing working tree |

Verdicts (lane-internal; admission is the non-author closure's):
- **C1: met on the frozen predicate; contested.** It is a development-set result. CriticR100's fresh r100 holdout (eight new
  classes): v8 accepts 7/8, v9 accepts 7/8, controls ok (`.ufo/waves/round-100/w1/CriticR100/receipts/logs/holdout100-v{8,9}-c{02,14}.log`).
  CriticR100 A1: the harness reads verdict lines, not the counter's rc, so an rc-0 wrapper still scores `met`. On the real
  v9 run every vector's rc agrees with its verdict (12 × `rc=1 C1_VERDICT=fail`, 2 × `rc=0 C1_VERDICT=pass`,
  `post-freeze/c1-v9-vector-rc.log`), so the measured 0/12 stands; the gap is routed. MutationR100: 12/12 pre-registered del-leg mutants killed, but only by the self-test (0/12 vector-specific: a deleted leg raises KeyError and force-fails); the labelled post-freeze force-pass supplement kills 12/12 vector-specifically, one leg per vector (`.ufo/waves/round-100/w1/MutationR100.md` §3a, §4a).
- **C2: met on the frozen predicate and kill rule; contested.** The named controls (echo stub, byte flip) are refused.
  CriticR100 A2 and ReviewerCapR100 attack 3: a PATH shim keyed on input digests, decoding nothing, passes the frozen
  probe because the tamper value is deterministic (`CriticR100/receipts/logs/cap-probe-shim.log`). CriticR100 recommends
  holding C2; the operator rules. M23: the claims' surface sentence says "the row and the probe cite" S508/S509; the frozen
  probe cites neither (the capability row cites both, which is what the kill rule binds). MutationR100: 1/4 pre-registered probe mutants killed (drop-tamper); compare-only-package, skip-fixture-sha and swallow-decoder-failure survive the frozen controls (§3b). `controls_c2.sh` does not enforce `CAP_FIXTURE_SHA=fail` on the flip as claims §C2(iii) says; the L1's flip run printed it (`post-freeze/c2-controls-detail/control-flip.log`), so (iii) holds by observation, not by the script.
- No axis harmed: `git diff --stat 0350014d a5e91dd8 -- corpus/README.md PROVINCE.md corpus/QUALITY.md SHONEN.md` is empty;
  K stays 14/15.

## Sources & frontier

- Census command: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin revenger`.
  Round start: exit 0; 21 × W01, 13 × W04, 0 E-codes (`reports/round-100/controls/census-round-start.log`).
  Round end: exit 0; 21 × W01, 13 × W04, 0 E-codes (`reports/round-100/controls/post-freeze/census-round-end.log`).
- Rows 507 → 509 (`grep -cE '^ {0,3}\| S[0-9]{3,} ' corpus/SOURCES.md`). Added by tier: A +2 (S508 androguard `axml` docs,
  `https://androguard.readthedocs.io/en/latest/tools/androaxml.html`; S509 Apktool wiki, `https://apktool.org/wiki/the-basics/intro`),
  both `docs`, `mined`, opened 2026-11-05, recheck `on-release`, used-by `corpus/lessons/round-100.md`. Rows touched old→new:
  none (the new rows' cells are logged none → value in the lesson Gate).
- Frontier advanced: the APK family gains a working third-party decode route on this host (capability row). C05 stays
  `uncovered`; the next frontier items are a C05 candidate on these receipts through the gate and the firmware capability
  on `fixtures/firmware-r63`.
- Mined mistakes (`corpus/lessons/round-100.md` `## Mistakes`): M21 census line drops a warning class (fix
  `reports/round-100/census_line_check.py`, shown able to fail: `CENSUS_LINE_CHECK=fail missing=W04` on the r99 report,
  `.ufo/waves/round-100/w1/ExecControlsR100/census-r99-fail.log`); M22 do-nothing commit naming (the r100 controls name the
  base `0350014d`); M23 frozen surface sentence not checked against the frozen probe; M24 decoder log written into the tree.
  This report's census lines under the M21 check: `python3 -B revenger-shokunin/reports/round-100/census_line_check.py --report .ufo/reports/round-100/revenger.md --log revenger-shokunin/reports/round-100/controls/post-freeze/census-round-end.log` → `CENSUS_LINE_CHECK=pass missing=none`, rc 0.
- Assimilation: none (L0 `revenger | round-91` on the 155/155 staged-id collisions is still open; nothing adopted).
- considerthese: no proposal adopted (`considerthese/2026-11-05.md` proposal 4, the producer-attribution census, is carried with no frozen predicate).

## Trend verdicts

- **expansion: improved** — a new capability (APK manifest cross-decode with two decoders and a tamper leg) on a family the
  lane had no working route for, and two tier-A sources opened and mined (S508, S509). Contested by CriticR100 A2 (lookup shim).
- **quality: unchanged** — no knowledge entry was added or changed; the round's instruments are registered probes.
- **discernment: improved, contested** — v9 refuses the twelve routed r99 classes with rc-consistent verdicts and no
  regression on the r98 set or the real tree; the fresh r100 holdout (7/8 accepted by both v9 and v8) shows no
  generalization, and the attacks found two instrument gaps that the lane records rather than hides.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — four registry rows added for the r100 instruments (`SKILL.md` gate registry, `c1_k_admit_counter9` … `census_line_check`); no non-author re-confirmation of the current bytes.
- [~] At least one end-to-end domain task executed and logged in LOG.md — two third-party decoders run on the authored APK against truth with a tamper leg (`reports/round-100/controls/post-freeze/c2-probe-landing.log`; `LOG.md` `## Round 100`); lane-seat review only (ReviewerCapR100).
- [~] Instructions executable by an agent without oral context — every r100 instrument has a registry entry command that seats and the L1 ran as written (`reports/round-100/controls/post-freeze/*.log`); no outside instruction verifier.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — PROVINCE.md byte-unchanged; ConnectorR100 adjacency scan (`.ufo/waves/round-100/w1/ConnectorR100.md` §5); no outside verifier.

## Stale-lane

The driver launch for r100 (`2026-11-05T19:38:35-03:00 launch revenger round=100 … attempt=1`) is this L1's only open
mission; no other mission of this lane is open. Progressing: lane commits `05e854ce`, `173abe91`, `a5e91dd8` and `cdb0774b0bbde2797f2e3a1ad660487a7bbccfbf` since launch.

## Tool installs

None. Used as found: androguard 4.1.4 (uv tool), apktool 3.0.3 (official jar via the `~/.local/bin/apktool` wrapper),
gitleaks 8.30.1 (SentinelR100). No pacman transaction.

## Misroot and inherited-state sweep

- Inherited state at start: lane clean (`jj-lane.sh state` → `ahead=0 behind=0 tracked=0 untracked=0`); no
  `lane-dead-no-report revenger round=100` line in the watchdog log (attempt 1). An empty untracked dir `--profile` at the
  lane root (mtime 2026-11-05 18:11, before this round) is not this round's; git ignores empty dirs; left as found.
- Stray files written this round and removed before any commit: `corpus/fixtures/apk-r65/androguard.log` (the L1's
  exploratory decode, 19:39), the lane-root `androguard.log` (WIP probe, 19:52) and `reports/round-100/__pycache__/` (M24).
- Fleet root: `git -C /home/vgpnk/Projects/shokunin status --porcelain` → `?? .ufo/reports/round-100/revenger.md` (this report) and `?? w4lines.txt` (bare integers, names no lane; SentinelR100 F2/fleet scan) plus orchestrator `.scratch/` edits — no misroot from this lane's seats; nothing moved or deleted.
- Credential sweep (SentinelR100): `reports/round-100/` clean; one upstream per-request analytics token
  (`auth_hydro_click_hmac`) sits inside the fetched GitHub release page `ScoutSourcesR100/apktool-release-v303.html`
  — the L1 deleted that body from the wave dir before the evidence commit (its sha256 `3356d86d…` stays recorded in `fetch-receipts.md`); `gitleaks dir .ufo/waves/round-100 --redact` → no leaks.
- Disk: `/fast/scratch/hyaku` reached 100 % (fleet-wide) at ~21:52; the L1 removed its own and ExecHarness9's leftover
  scratch (`disk-guard.sh status` → 1.0G free afterwards). MutationR100 also hit the full disk (its first supplement attempt stopped at ENOSPC, re-run after cleanup; `MutationR100.md` §2.2); `/fast` back to ~50 % afterwards. `$HYAKU_SCRATCH/revenger-r100` removed after landing.

## Wave

One v1 wave `w1`, 12 seats: executor 4 (ExecCounterV9, ExecHarness9, ExecApkProbe, ExecControlsR100), scout 1
(ScoutSourcesR100), scribe 1 (ScribeLessonR100), connector 1 (ConnectorR100), reviewer 2 (ReviewerClaimsR100,
ReviewerCapR100), critic 1 (CriticR100), mutation-tester 1 (MutationR100), sentinel 1 (SentinelR100). Attack share 4/12.
The L1 held the canonical planner seat. Dead seats: none (all 12 settled; every seat wrote its findings file; `w1-results.json`). Round total: 12 seats.

## Open items and routed work (r101)

1. CriticR100's seven accepted fresh classes (C02-P1..P4, C14-P1..P3) as v10 legs, with a new holdout.
2. forge_reach9: require the counter's rc to agree with its verdict line (CriticR100 A1).
3. `C1_DERIV_RERUN`: the declaration-strip evasion.
4. cap_apk_probe: a random tamper value per run plus a second tampered attribute (CriticR100 A2, ReviewerCapR100 attack 3); cite S508/S509 in the probe (M23); make `controls_c2.sh` require `CAP_FIXTURE_SHA=fail`, add MutationR100's A1/A2 as controls, adopt a force-pass mutation operator, give forge_reach9 builder failures their own outcome; explain apktool reporting versionCode 1 on the CRC-broken flip copy (androguard reported 2).
5. Carried: the C14 entry's Q13 rationale; the C02 no-harm rule (M19); `d-host`; M4 `claude-red-re-bridge.md`; the producer-attribution census; L0 assimilation (open).
