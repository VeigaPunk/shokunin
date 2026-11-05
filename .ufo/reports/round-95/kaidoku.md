# kaidoku round 95 — report

Lane: `kaidoku-shokunin`, attempt 1 (watchdog: `launch kaidoku round=95 pgid=… driver=hyaku-inline attempt=1`, no `lane-dead-no-report` line for round 95). Lane final commit (pushed; `git -C /home/vgpnk/Projects/shokunin/kaidoku-shokunin ls-remote origin refs/heads/main` = `51a90c757696e725be5e8a89a53f0991bf757583`). Declaration (freeze) `4bda1d1dd3788973f10e61212b70df18b3b14ea0`; base `b5331db1fb0ce0bf93695ce1730cf831effef6a9`; landing `51a90c757696e725be5e8a89a53f0991bf757583`. Measured revisions: R95-C1 at `4bda1d1d`; R95-C2 at the landing worktree (`--worktree`, the craft block is landed after the freeze).

## Work performed

Declared claims (two, both frozen before candidate scoring, `plans/round-95-claims.md`, `.ufo/waves/round-95/claims.json`, `pins.sha256`): both on the tied-lowest owned axes (calibration; depth; all four owned axes at 10.0 on their finite proxies; no stagnation waiver, a capability entered in round 94).

- **R95-C1 — calibration (measured): VERIFIED on the frozen predicate; named limits.** The round-94 instruments admit a consistently rewritten label pair and a fabricated triple (M94-e), a short `--rev` is unvalidated (M94-f), and the v4 writer follows a planted `<json-out>.tmp` symlink (SentinelWrite F1). Candidates: `tools/round-95/c1-agreement-v2.py` (four typed bindings), `tools/round-95/stop-boundary-repair-battery-v5.py` (mkstemp temp name, fsync, receipt self-verification, fail-closed exit), `tools/round-95/c1-forgery-refusal.py` (frozen battery), `tools/round-95/symlink-probe.py`. Evidence: `.ufo/waves/round-95/pre/c1-old-counter-admits-at-base.json` (before: 4/4 admitted); `.ufo/waves/round-95/l1/scores/c1-forgery-at-4bda1d1dd3788973f10e61212b70df18b3b14ea0.json` (after: 4/4 refused with exact reasons, honest accepted); `honest-pos.stdout` (`selfverify ok=True`, met True exit 0); `c1-symlink-v5-at-4bda1d1dd3788973f10e61212b70df18b3b14ea0.json` (`victim_intact true`, `hardened`); `pre/c1-symlink-v4-at-base.json` (`victim_intact false`, `followed-symlink`).
- **R95-C2 — depth (measured): VERIFIED on the frozen predicate; named limits.** Craft block 34 (`SKILL.md:788-797`, marker `receipt-world-binding v1`, four table rows) and QUALITY rows 191–192 (`corpus/QUALITY.md:327-329`). Evidence: `.ufo/waves/round-95/l1/scores/c2-after-block34-worktree.json`; `.ufo/waves/round-95/pre/c2-base-*` (before, exit 1 each).
- **Sourced claim (frontier step).** The knowledge entry `corpus/knowledge/2026-11-05-r95-receipt-world-binding.md` and the craft block cite S320 (open(2) `O_NOFOLLOW`, opened 2026-11-05; fetches `.ufo/waves/round-95/l1/scores/s320-open2-fetch{1,2}.html`, byte-identical).
- **Wave `r95-w1`** — `.ufo/waves/round-95/r95-w1-spec.json`, `r95-w1-dispatch.json` (validator: `plan` rc 0, 11 spawn, 0 resume), `r95-w1.ready` (picked up `13:42:26`); results `.ufo/waves/round-95/r95-w1-results.json`; seat reports in `.ufo/waves/round-95/w1/`. WAVE-DONE received from Main before this report.
- **Reproduction (ExecRepro).** Independent run at `4bda1d1d`: label, counts, cell classes, pins, rc, stdout and the forgery battery's JSON match the committed receipts. The honest receipt differs only in the per-run random fresh pack: `fresh_provenance.nonce` and `fresh_packed_sha256`, and the `output` digests of the two repaired fresh cells that follow from it (`.ufo/waves/round-95/w1/ExecRepro/repro.md`, `compare.txt`).
- **Attacks and reviews** (the wave's findings are the lesson's `## Named limits`): ReviewerV5 (no HIGH/MED; `w1/ReviewerV5/ReviewerV5.md`); ReviewerScope (declaration conformance, `w1/ReviewerScope/scope.md`); CriticC1 (eleven attacks; four unbound-field classes and the `--json-out`-less exit 0, `w1/CriticC1.md`, `w1/CriticC1/attacks.md`); CriticC2 (keyword atom and depth-counter residuals, `w1/CriticC2.md`); MutationC1 (10 mutants, 5 killed, 5 survived, `w1/MutationC1.md`); SentinelWrite (no HIGH/MED; LOW probe write and verifier re-open, `w1/SentinelWrite.md`); ConnectorOverlap (no sibling claims the class, `w1/ConnectorOverlap/overlap.md`); ScoutS320 (`w1/ScoutS320/s320-recheck.md`).
- **Declaration sweeps and fixes.** Red-before evidence for this round's two code fixes: `.ufo/waves/round-95/l1/scores/m95a-intact-denominator-red-green.txt` (RED exit 1 / GREEN exit 0) and `m95b-selftest-idempotence-red-green.txt` (RED run 2 exit 1 / GREEN exit 0). Frontier step: census before/after (below); mistakes mined: `corpus/lessons/round-95.md` `## Mistakes` M95-a..i.
- **D-94-A (round-94 spot-check).** The 0-byte receipt `.ufo/waves/round-94/l1/scores/c1-unchanged-bytes-at-8a711726.txt` is answered by the self-describing `.ufo/waves/round-95/l1/scores/d-94-a-unchanged-bytes-receipt.txt` (commands, exit 0, output sha256 `e3b0c442…b855` = empty). The 0-byte original is kept, not rewritten.
- **Considerthese / assimilation.** `considerthese/` is absent in this lane: `No such directory — kaidoku has no considerthese/`. `merge/kaidoku/` is absent: `Assimilation: none`.

## Landed changes

| commit | what | LOG entry |
|---|---|---|
| `4bda1d1dd3788973f10e61212b70df18b3b14ea0` | declaration freeze: `plans/round-95-claims.md`, `.ufo/waves/round-95/claims.json`, `pins.sha256`, `tools/round-95/` (4 instruments), forgery fixtures, `pre/` before-side receipts, S320 fetches, census-before | round-95 entry (declaration) |
| `51a90c757696e725be5e8a89a53f0991bf757583` | candidate landing: `SKILL.md` craft block 34; `corpus/QUALITY.md` rows 191–192; `corpus/knowledge/2026-11-05-r95-receipt-world-binding.md`; `corpus/SOURCES.md` S320 row; `corpus/lessons/round-95.md`; `SCORECARD.md` round-95 section and capability row; `LOG.md` round-95 entry; wave `r95-w1` evidence; red/green evidence; D-94-A receipt | round-95 entry (landing) |

## Before → after measurements

**R95-C1 (calibration).** Counting command (after): `python3 -I -B tools/round-95/c1-forgery-refusal.py --root . --fixtures .ufo/waves/round-95/forgery --old-prefix forge --old-counter tools/round-94/c1-receipt-agreement.py --honest-dir .ufo/waves/round-95/l1/scores --honest-prefix honest --world-rev b5331db1fb0ce0bf93695ce1730cf831effef6a9 --instrument-rev 4bda1d1dd3788973f10e61212b70df18b3b14ea0 --expect 'repaired 12 of 12; wrong 0; unsafe 0; intact 6 of 6; far-refused 12 of 12; fresh-roundtrip 2 of 2' --json-out …` (measured at `4bda1d1d`; exit 0).

| arm | before (base `b5331db1`, pinned round-94 instruments) | after (`4bda1d1d`) |
|---|---|---|
| forgeries admitted / refused | admits 4 of 4 (`valid 4, agree 4, predicted 4, met true`) | refused 4 of 4, each with exactly its intended reason (`label-not-frozen`, `label-not-recomputed`, `revision-not-bound`, `pins-not-bound`) |
| honest triple | accepted (v4) | accepted, `selfverify ok=True`, exit 0 |
| symlink probe | v4: `victim_intact false`, `followed-symlink` | v5: `victim_intact true`, `hardened`, `receipt_valid true` |

Verdict: verified on the frozen predicate. Named limits (not closed; frozen counters unchanged): see `corpus/lessons/round-95.md` `## Named limits` (unbound fields; self-verification skipped without `--json-out`; five writer and probe gates outside the frozen kill rule; the probe's own `--json-out` follows a planted link).

**R95-C2 (depth).** Counting commands (measured at the landing worktree, `--worktree`): `python3 -I -B tools/round-93/craft-citation-semantic.py --root . --manifest .ufo/waves/round-95/manifests/block34-after.json --block 34 --worktree` → exit 0 `ok`; `python3 -I -B tools/round-89/depth-blocks-v2.py --root . --worktree --expect-blocks 34` → exit 0 `blocks 34 resolved 34 expect 34 unresolved 0 met=True`; `python3 -I -B tools/round-91/depth-blocks-v3.py --root . --worktree --expect-blocks 34 --shape-from 34` → exit 0 `blocks 34, resolved 34, required-shaped 1/1 … met=True`; junk control `block34-junk.json` → exit 1 on three keyword reasons.

| command | before (base `b5331db1`) | after (landing worktree) |
|---|---|---|
| craft-citation, after-manifest | exit 1 `block 34 missing (craft has 33 blocks)` | exit 0 `ok` |
| depth v2 `--expect-blocks 34` | exit 1 `blocks 33 resolved 33` | exit 0 `blocks 34 resolved 34` |
| depth v3 `--shape-from 34` | exit 1 `blocks 33 … required-shaped 0/0` | exit 0 `required-shaped 1/1` |

Verdict: verified on the frozen predicate; a vocabulary check (named limits 6–7 in the lesson).

## Sources & frontier

- **SOURCES.md before → after.** Rows: 224 → 225 (`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`, base vs landing). Census: `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kaidoku` exit 0 before (`.ufo/waves/round-95/census-before.txt`) and exit 0 after (`.ufo/waves/round-95/census-after.txt`); W04 32 → 32 (no new duplicate-URL warning).
- **Rows added by tier.** A: 1 (S320, `docs`, opened 2026-11-05, `mined`).
- **Rows touched old→new.** None (no in-place edits; S319 and others unchanged).
- **Frontier rows advanced.** None as a registry status change. The receipt-world-binding class moves from routed defects (round-94 M94-e, M94-f, SentinelWrite F1) to a named craft class (block 34) with measured instruments; `corpus/README.md` is not edited.
- **Sourced claim.** R95-C1's and R95-C2's knowledge entry cites S320.
- **Assimilation.** `Assimilation: none` (`merge/kaidoku/` absent; no `considerthese/` directory in this lane).

## Trend verdicts

- **expansion: unchanged.** One knowledge entry on the stop-boundary battery family, already held in Core; no new coverage-map ground; one capability row enters (the repertoire grows, the map does not).
- **quality: improved.** The round-94 routed defects each have a measured fix; code fixes shown able to fail (M95-a, M95-b); craft block 34 and QUALITY 191–192 state the class. The named limits are recorded, not hidden.
- **discernment: unchanged.** The attacks produced the named-limit list and the M95-g mistake (declared limits were not exhaustive), but no outside admit/reject spot-check of this round's gate decisions exists yet; the discernment verdict is not moved.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md:788-797` (block 34 decision table citing QUALITY 191–192 and the receipt evidence); blocks 1–33 intact (depth v2/v3 34/34 at the landing worktree).
- [~] At least one end-to-end domain task executed and logged in LOG.md — `LOG.md` round-95 entry; the frozen battery ran end-to-end at `4bda1d1d` (honest public run, forgery battery, probe; receipts `.ufo/waves/round-95/l1/scores/`).
- [~] Instructions executable by an agent without oral context — counting commands in `## Before → after measurements` and `corpus/lessons/round-95.md` `## Measured`; `tools/round-95/c1-agreement-v2.py --selftest`, `c1-forgery-refusal.py --selftest`, `stop-boundary-repair-battery-v5.py --selftest` (rc 0 each, re-run in the clone).
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `w1/ConnectorOverlap/overlap.md` (no sibling claims the receipt-binding or symlink class); `PROVINCE.md` not edited.

## Round shape, seats, and dead seats

- Shape: one v1 wave `r95-w1`, 11 seats (band 8–16). Roles: executor 1, scribe 2, scout 1, connector 1, reviewer 2, critic 2, mutation-tester 1, sentinel 1. Planner seat held by the L1 (validator refuses planner). Attack share 6 of 11 (reviewer 2, critic 2, mutation-tester 1, sentinel 1) = 54.5%; one connector; L2 floor met (11 ≥ 8). No residual call; no second wave. Round total 11.
- Dead seats: none (`r95-w1-results.json`, 11 results, each with output).
- WAVE-DONE received from Main for `r95-w1` before this report was filed.

## Stale-lane, tools, misroot, inherited state

- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
- Tools: none installed or upgraded (python3, git, jq, strace, curl, upx already present). No pacman transaction, no sysctl or namespace change; the sysctl incident of 2026-11-05 is not reproduced here (no seat was asked to change host state, and the seat briefs forbade it).
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows three entries, none written by this round's seats: `M .scratch/run15-state.json` (orchestrator-owned), `?? .ufo/closure-kaidoku-r92.json` (round-92 closure artifact, pre-existing), and `M .ufo/l0-questions.md` (one appended line by the souji lane, `souji | round-67 | …`; not this round's; left in place for the integrator). No file from round 95 was found at the fleet root; nothing was copied or deleted.
- Inherited state: the lane tree was clean at round start (`jj-lane.sh state` ahead=0 behind=0, no untracked files). One lane-authored scratch directory of this round (`dbg2/`, a debugging leftover) was removed before the landing commit.
- Scratch: `$HYAKU_SCRATCH/kaidoku-r95/` (L1 and seat scratch) removed after landing.

## Open L0 question

None appended this round. The named limits in `corpus/lessons/round-95.md` route the next steps to round 96 (a declaration that closes the unbound fields and adds four `main()`-level kills to the frozen rule); no operator decision is needed for that.
