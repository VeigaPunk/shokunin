# kaidoku — round 42 report (L1 KaidokuR42, attempt 1)

Lane `kaidoku-shokunin`, branch `main`: base `c4a38ea2fcd7a7da096358f9bf462c9a4be3c33c` → final `af50af81751bbb02316c9bc9a0459ca96707b0c0` (pushed; `git ls-remote origin refs/heads/main` prints it).

## Work performed

Declared claims (frozen at `d1681696dd63ca4f9b8a09ffa8fa3e2de5e2b51b`, `plans/round-42-claims.md`):
**R42-C1 — coverage:** SquashFS v3 (`squashfs_v3`, `squashfs_v3_ddwrt`) through REA `extract-firmware` moves Frontier → Core on four published images (also a capability acquisition).
**R42-C2 — depth:** SquashFS triage table v4 (SKILL rule block 21) covering the whole SquashFS handler family, scored against an independent evaluator on a held-out set seeded by the freeze.

- Draft claims and wave-1 dispatch: `fdabdfa4`; wave 1 = 43 seats, all settled (`.ufo/waves/round-42/r42-w1-results.json`, reports `.ufo/waves/round-42/w1/`).
- Oracle decision: `unsquashfs` 4.7.5 reads no LZMA v3 (`w1/R42C1DevRun.md`, `w1/R42CritC1Draft.md` §3); the L1 built backhand-cli 0.25.5 with `v3,v3_lzma` and paired it with 7-Zip (`tools/round-42/sqfs3-oracle.py`; L1 check 156/156 on a dev image).
- C2 precedence amendment A1 (container-depth row, residue row, failing-handler column) after `w1/R42CritC2Draft.md` showed the draft was mostly a re-score (`plans/round-42-claims.md:85-134`); grammar verified 0 divergence classes over 4,478,976 tuples (`w1/R42C2Grammar.md`).
- Sentinel H1–H5 provenance bindings adopted: fetch receipts (`.ufo/waves/round-42/c1/fetch-*.json`), frozen prior pins and REA package digests (`tools/round-42/prior-pins.json`, `rea-pkg.json`), fixed PATH and an unblob log tee (`tools/round-42/unblob-logtee.sh`) so `extract-env.json` names the extract command.
- QUALITY 84 dry runs before the freeze caught three defects (`.ufo/waves/round-42/l1/dryrun-c1-pre.json`, `dryrun-c2-pre.json`, `dryrun-c2-pre2.json`); final dry runs: C1 dev arm 4/4 carriers (`l1/dryrun-c1.json`), C2 78/78 exit 0 (`l1/dryrun-c2.json`).
- Selftests at the freeze (`.ufo/waves/round-42/l1/selftests/`): interpreter 123/123, evaluator 45/45, C2 counter 79/79, C1 counter 121 cases 0 failures, fetch 36/36, c1-extra 41/41, prefile gate 12/12, oracle 0 failures.
- Freeze `d1681696`; controls `b024051c`; data `d5e22b51`; C1 landing `eb8215ac`; scores `d4b4b4fb`; lesson/SCORECARD/LOG/SHONEN `46486e7a`; lesson pointer fix `af50af81`.

## Landed changes

| change | LOG.md entry | commit |
|---|---|---|
| draft claims, start census, wave-1 spec/dispatch | `## Round 42` | `fdabdfa46fd1652ce370fa72fca1d00751d01528` |
| freeze: claims, `tools/round-42/*`, carriers/fetch receipts/oracles, C2 fixtures + dev arm + controls, SKILL rule block 21 + entry `2026-10-26-r42-sqfs-triage-v4`, S130, dry runs, wave-1 evidence | `## Round 42` | `d1681696dd63ca4f9b8a09ffa8fa3e2de5e2b51b` |
| control receipts | `## Round 42` | `b024051cb5be767c507f6ea933fdece87defa677` |
| data (C1 receipts, C2 held-out) | `## Round 42` | `d5e22b5154efffde3d18ea2cb8e526c7650f5524` |
| C1 landing: PROVINCE `## Round-42 additions to Core`, entry `2026-10-26-r42-squashfs-v3-core`, README rows, S131–S134 | `## Round 42` | `eb8215ac87860f0e52745a4f842485bf8a6fe3b8` |
| score receipts | `## Round 42` | `d4b4b4fb82e3da3bd11ed57ed6693f938f4d726c` |
| lesson `corpus/lessons/round-42.md`, QUALITY 85, SCORECARD `## Round 42` + capability row, LOG, SHONEN, block-21 citation, end census | `## Round 42` | `46486e7a78dee30412eb55aca56e6621b7c6e5d0` |
| lesson pointer fix | `## Round 42` | `af50af81751bbb02316c9bc9a0459ca96707b0c0` |

## Before → after measurements

- **R42-C1 (coverage):** before `carriers_matched 0`, exit 1 at the freeze (CTL-C1-0, `.ufo/waves/round-42/controls/c1/ctl-c1-0-do-nothing.json`); round-41 receipts relabelled 0/4 (CTL-C1-1). After `carriers_matched 4`, every binding true, `frozen_path_changed []`, exit 0, counter-time REA rerun included (`.ufo/waves/round-42/l1/scores/c1-at-eb8215ac.json`, `counter_sha256 0f5052f9…`). Command: `python3 -I -B tools/round-42/c1-counter.py --root <LANE> --rev eb8215ac --freeze d1681696 --pkg65 /home/vgpnk/.npm/_npx/ad9a3fdbcad992c6/node_modules/rea-agents --carrier-cache <CACHE> --work <S> --json-out <OUT>` (cache from `tools/round-42/fetch-carrier.py --spec .ufo/waves/round-42/c1/fetch-spec.json`). Measured at `eb8215ac`. **Author verdict: met.**
- **R42-C2 (depth):** before exit 2 `no_manifest_at_rev` at the freeze (`controls/c2/c2-counter-at-freeze.json`); base SKILL and the v3 table under the v4 marker 0/78 on the dev arm (`controls/c2/dev-scores-prefreeze.json`, no control at full score). After `matched 78` of 78, `combo_unseen_majority` 19/24, but `observed_features_match_declared` false (combo C02 declares gap kinds without `depth-limited`; REA observed it), exit 1 (`l1/scores/c2-at-eb8215ac.json`). Command: `python3 -I -B tools/round-42/c2-counter.py --root <LANE> --rev eb8215ac --freeze d1681696 --json-out <OUT>`. Measured at `eb8215ac`. **Author verdict: not met — honest stop** under the frozen rule (not changed after scoring).
- Owned-axis proxies (command A, `.ufo/waves/round-42/w1/artifacts/R42ScoutCalib/command-a.py <rev>`): base `c4a38ea2` coverage 133/133, rule blocks 20/20 resolving; tip `46486e7a` 135/135, 21/21. At `d4b4b4fb` (before the block-21 citation was added) depth read 20/21 = 9.52; repaired in `46486e7a` — no axis left harmed.

## Sources & frontier

- Census (`scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kaidoku`): start exit 0 (`.ufo/waves/round-42/census-start.txt`), end exit 0, `kaidoku ok`, 0 errors (`.ufo/waves/round-42/census-end.txt`).
- SOURCES rows 129 → 134, all tier A, `mined`: S130 unblob 26.6.4 SquashFS fixtures (C2), S131/S132 OpenWrt Kamikaze 8.09.2 atheros / 8.09 x86 listings + md5sums, S133/S134 DD-WRT v24 listings + MD5SUMS (C1). Rows touched old→new: none. Frontier advanced: SquashFS v3 (`squashfs_v3`, `squashfs_v3_ddwrt`) Frontier → Core.
- Sourced claim: R42-C1's entry cites S131–S134 (opened 22:53Z this round); R42-C2's entry cites S130.
- Mined mistakes: M42-1 (probe frozen on one writer's fixtures; caught by the dry run), M42-2 (generator declared tuple predicted, not observed — the C2 stop), M42-3 (tool interface seams) → QUALITY 85.
- Assimilation: none adopted (review `w1/R42Assim.md` kept; id collisions 24, guard proven, quarantine slice unchanged, `w1/R42AssimIds.md`). considerthese: no `considerthese/` directory exists in this lane.
- Cross-domain evidence: none encountered — sibling scan `w1/R42ConnSibling.md` finds one toolchain overlap (revenger-shokunin REA+unblob), no sibling holding SquashFS v1–v3 or these carriers; PROVINCE `## Adjacent` unchanged.

## Trend verdicts

- **expansion: improved** — SquashFS v3 moved Frontier → Core on four published images from two publishers, both byte orders, two handlers (C1 4/4); map 133 → 135; capability row entered.
- **quality: improved** — round-41 routed defects R41-CL1, CL2, CL4 and closure D1, D4, D5 fixed with selftested tools; three defects caught by dry runs before data; QUALITY 85.
- **discernment: unchanged** — C2 was stopped under its frozen rule and reported, but no outside spot-check exists yet and no wave 2 attacked the landing; the closure decides.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SHONEN.md:6`; 21/21 rule blocks resolve (command A at `46486e7a`); block 21's claim stopped.
- [~] At least one end-to-end domain task executed and logged in LOG.md — `SHONEN.md:8`; REA on four published v3 rootfs, C1 4/4 at `eb8215ac`, LOG `## Round 42`.
- [~] Instructions executable by an agent without oral context — `SHONEN.md:10`; v4 table executed by `tools/round-42/sqfs-triage-v4.py` 78/78 vs the evaluator (claim stopped on a binding).
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `SHONEN.md:12`; PROVINCE append-only (`## Round-42 additions to Core`), `## Adjacent` unchanged.

## Round shape and conformance

- Shape: one v1 wave of 43 seats (executor 17, critic 8, scribe 4, reviewer 4, connector 3, mutation-tester 2, scout 2, revenger 1, sentinel 1, simplifier 1); 0 dead; no residual call. **Round total 43 — below the run-9 floor of 64**: wave 2 (falsify) was not dispatched because the L1 ran out of run budget after integration; this is a conformance defect (routed R42-CL2), not hidden. Planner seat held by the L1; planning data-walk rode critic/scout items.
- Inherited state: the round-41 L1 landed `ae5dc3f3` (wave-2 settle) at 21:44Z during this round; no round-41 leftovers remained (`w1/R42Late41.md`).
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` lists only `.scratch/` (orchestrator-owned) — no seat file misrooted.
- Pre-file gate: `tools/round-42/prefile-gate.py --round 42` GATE GREEN at `af50af81`.
- Tool install: backhand-cli 0.25.5, `cargo install backhand-cli --version 0.25.5 --locked --no-default-features --features v3,v3_lzma,gzip,xz --root ~/.local/opt/backhand-0.25.5-v3` (crates.io; reason: a non-sasquatch LZMA v3 oracle reader). No pacman use.
- Open L0 questions: none added.
- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
