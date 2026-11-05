# kagi — round 37 (attempt 1)

Lane repo `/home/vgpnk/Projects/shokunin/kagi-shokunin`, branch `master`, lane tip **58121282fbb7a521d0ecf19d7161230330e448fe** (remote verified: `git ls-remote origin refs/heads/master` → `58121282fbb7a521d0ecf19d7161230330e448fe`). Frozen BASE `911ab519b6b07694c3cb9f7d9a7c56e142ad957c` (round-36 landing). Stale-lane: respawn-per-round driver; no other mission of this lane is open. Watchdog: `launch kagi round=37 … attempt=1` only; no inherited earlier attempt.

## Work performed

**Declared claims (1):** **C2 — freshness** (lane axis; lowest non-retired axis tie at 9). Claim: `bash plans/round-37-c2.sh` counts release-feed surfaces (hashicorp/vault releases.atom, openbao/openbao releases.atom, python.org downloads feed.rss) with no `corpus/SOURCES.md` row naming the feed URL and the observed version; BASE **3** → target **0**. Plan frozen alone at `e2030d2` (`plans/round-37.md`); the counter, receipt and six controls committed as predeclaration `04489d4`. No calibration claim: `bash plans/round-36-c1.sh` already reads 0 at HEAD, so the round-36 target is not claimable (`corpus/lessons/round-37.md` §Calibration hold; M37-3). A second claim was not declared because no other BASE gap that a do-nothing control cannot reach was measured.

Work items, each with its evidence:

- Fresh-start reads of the last three rejected closures and spot-checks (rounds 34, 35, 36) plus rounds 32–33: `corpus/lessons/round-3{2,3,4,5,6}-verifier-spotcheck.md`.
- Predeclaration instrument, receipt and executed controls: `plans/round-37-c2.sh`, `plans/round-37-controls.sh`, `plans/round-37.controls.tsv`, `.ufo/waves/round-37/controls/` (commit `04489d4`). Shipped pre-freeze gate: `PREFREEZE: CLEAN (controls=6 mismatch=0)`, `.ufo/waves/round-37/controls/prefreeze-gate.txt`. Control results: no-work 3; superseded-version forgery 3; wrong-URL forgery 3; knowledge-only forgery 3; partial 2; full 0; receipt missing and receipt tampered exit 2 (`controls/c2-controls.txt`).
- Observation receipt: `python3 corpus/release-clock.py --observe` on 2026-11-05, 30 records, sha256 `cb96cfb2…` (`controls/observe-r37.json`).
- Candidate `9efcea7`: rows `S089`, `S090`, `S091` (supersede S034, S035, S039), each opened 2026-11-05 with a located quote in the captured body (vault `<title>v2.2.1</title>` at byte 726; openbao `<title>v2.7.2</title>` at 729; python `<title>Python 3.15.2</title>` at 1583); capture rows in `corpus/source-fetches.tsv`; bodies in `.ufo/waves/round-37/capture/`.
- Frozen counter at candidate: `bash plans/round-37-c2.sh` → **0**.
- Wave `build` (one v1 wave, 10 seats, all settled with output, none dead; `.ufo/waves/round-37/build-results.json`). Seat reports under `.ufo/waves/round-37/build/`: K37ExecRows (AGREE), K37ExecCounter (AGREE), K37ExecEvidence (AGREE; self-counts stale 0, census selftest PASS 70, docs CLEAN 35), K37ScribeDocs (drafts; integrated into SCORECARD/LOG), K37ScoutRegistry (survey; §5.1–5.5 findings integrated), K37ConnFeeds (no sibling overlap), K37ReviewFresh (independent re-fetch, AGREE on all three rows), K37ReviewCounter (15 attacks, wrong=0; ceilings named), K37CriticClaim (counterfeit with invented quotes passes → discipline condition adopted), K37MutCounter (killed 5 of 6; boundary mutant M5 survives the frozen set, killed by an extra probe; routed).
- Ledger migration (QM14): `R21-02`, `R31-02`, `R33-02`, `R34-03` expectations `rows=88 … captures=88` → `rows=91 … captures=91`, notes kept, word-diff verified; record `.ufo/waves/round-37/expectation-migrations.json`. Each new regex matches the live census line.
- Stamp re-pins (QM5): `corpus/stamps.tsv` entries for `corpus/SOURCES.md`, `corpus/source-fetches.tsv`, `corpus/claim-ledger.tsv`. `revision-audit.py --history c2cab35… --root .` → CLEAN (was DRIFT stale=2, then stale=1 before the third pin); `row-identity.sh revision-added` computed (was SETUP).
- Lesson `corpus/lessons/round-37.md`: Gate (three admitted rows, refused candidate shapes), Census, Mistakes M37-1..M37-3, Corrigenda (R36-1, R36-2), Quarantine (8 rows), Wave settlement, Ceilings, Migrations, Routed debt.
- SCORECARD (`SCORECARD.md`): capability row "release-feed anchor currency counter" (first working round 37); round-37 pre-move and post-move sections; "latest first-working round" sentence updated to 37. LOG (`LOG.md`): round-37 entry.

Wave shape: one v1 wave of **10 seats** (band 8–16; L2 floor 8): executor 3, scribe 1, scout 1, connector 1, reviewer 2, critic 1, mutation-tester 1. Attack seats (reviewer + critic + mutation-tester) = 4/10 = 40 %; connector 1. Planner seat held by the L1 (validator rejects `planner`; deviation recorded at plan freeze). No residual call. Round total: **10 seats**. Dead seats: none. Seat models were not pinned by the lane (routing is `task.agentModelOverrides`).

Misroot sweep: fleet `git status --porcelain` shows only the orchestrator-owned `.scratch/run15-state.json` modification; no seat file landed in the fleet root; nothing copied.

## Landed changes

| Change | LOG entry | Commit |
|---|---|---|
| Predeclaration: C2 counter, receipt, controls, runner, TSV | Round 37 — Predeclaration | `04489d4184edb25a01ec8983b3ccedb45c683564` |
| Freeze of plan and claim C2 (alone) | Round 37 — Freeze | `e2030d2794…` (`plans/round-37.md`) |
| Candidate: rows S089–S091, capture rows, lesson | Round 37 — Candidate | `9efcea7` |
| Ledger migrations, stamp re-pins, lesson, SCORECARD, LOG, wave evidence | Round 37 — close | `58121282fbb7a521d0ecf19d7161230330e448fe` |

## Before → after measurements

- **C2 (freshness), counting command:** `cd <extraction> && bash plans/round-37-c2.sh`.
  - BASE `911ab51` with the frozen counter and receipt: **3** (vault, openbao, python surfaces stale). Measured `04489d4` (predeclaration) → 3 and the seat extraction of `911ab51` → 3.
  - Candidate `9efcea7`: **0** (K37ExecCounter, K37ExecRows; re-run at the lane working tree before the close commit `58121282`: 0, rc 0).
  - Controls, frozen expectations, all met: no-work 3, forgeries G1/G2/G3 3, partial 2, full 0; setup exit 2.
- **Lane census** `bash corpus/sources-census.sh`: `CLEAN (rows=88 …)` → `CLEAN (rows=91 A=87 B=2 C=2 queued=1 mined=87 rejected=3 entries_sourced=14 legacy=21 captures=91 inrow=16 inrow_only=0 inrow_nonreproducing=12)`, exit 0.
- **Fleet census** `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kagi`: exit 0 before and after; W04 duplicate-URL lines 16 → 19 (three cross-scope duplicates, no E-finding).
- **Self-counts** `python3 corpus/self-counts.py`: `SELF_COUNTS: POLICY (claims=63 stale=0 …policy=2)` — the two operator-owned POLICY rows only (R29-01/R29-02); unchanged shape.
- **Revision audit** `python3 corpus/revision-audit.py --history c2cab35bc92e57e39e5489bac3386db078345b3f --root .`: `REVISION_AUDIT: CLEAN (stale=0 …)` after re-pins (was DRIFT).

## Sources & frontier

- **SOURCES.md rows before → after:** 88 → 91 (`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`); captures 88 → 91 (lane census above).
- **Rows added by tier:** A ×3 (`S089` vault releases.atom, `S090` openbao releases.atom, `S091` python.org feed.rss), all `mined`, scope release identity; quotes located in captured bodies; access date 2026-11-05.
- **Rows touched old → new:** none. S034, S035, S039 mutable cells (`status`, `recheck`, `used-by`) unchanged; each new row's `teaches` opens `supersedes S0NN —` per CORPUS SOURCES rule 2.
- **Frontier rows advanced:** none moved to core; the release-clock frontier bullet is unchanged (`corpus/README.md` §Frontier; scribe's NO CHANGE reason).
- **Sourced claim:** C2 rests on `S089`, `S090`, `S091` opened this round (`corpus/lessons/round-37.md` §Gate).
- **Mistakes mined (`corpus/lessons/round-37.md` §Mistakes):** M37-1 number drift (round-36 report "five" W04 vs live 16; command output pasted); M37-2 harness landing (first battery ran forgeries against the lane tree before the job was stopped; lane tree verified unchanged; the guard is not yet shown able to fail — routed); M37-3 stale premise (round-36 C1 target already 0 at HEAD).
- **Quarantine (absent-defect register, `kagi` slice):** 8 rows (`S053`, `S071`, `S081`, `S090`, `S091`, `S093`, `S108`, `S113`; class `payload-absent`), none adopted. Hazard: the register's campaign `S090`/`S091` ids collide in spelling with this lane's new rows; nothing from the register is appended.
- **Assimilation:** none. `considerthese/`: no unimplemented proposal taken.
- **Routed to round 38:** located-quote gate against committed bodies; anchor-immutability check (in-place anchor rewrite reads 0 today); boundary control for `2.2.10` (frozen-counter amendment); release-clock table re-point (coupled change; `DERIVATION` and `receipt_matches`); receipt re-observation in a full tree (current receipt errors on rendered-quote rows because it was written without `corpus/source-fetches.tsv`); the round-36 C1 instrument conditions (R36-4); the M37-2 red-before guard run.
- **Non-author spot-check:** pending outside closure (the L1 does not self-admit).

## Trend verdicts

- **expansion — unchanged.** No admitted knowledge entry on uncovered ground; three supersession rows only; no frontier-to-core move.
- **quality — improved.** Three release-feed anchors that named superseded releases now name the observed release, each with a located quote in its captured body and a superseded-claim check by an independent re-fetch (`.ufo/waves/round-37/build/K37ReviewFresh/report.md`: AGREE ×3). Mutable history unchanged. Counter ceilings named rather than hidden (`corpus/lessons/round-37.md` §Ceilings).
- **discernment — unchanged.** The lane's gate decisions are recorded (three admits, refused shapes with reasons). Seat agreement is lane evidence, not outside agreement; the non-author spot-check is pending closure, so no `improved` is claimed.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — pointer: `SKILL.md`, unchanged this round.
- [~] At least one end-to-end domain task executed and logged in LOG.md — pointer: `LOG.md` Round 37 entry (C2 end-to-end: receipt, counter, candidate rows, census, closure-ready controls).
- [~] Instructions executable by an agent without oral context — pointer: `plans/round-37-controls.sh`, `plans/round-37.controls.tsv`, `plans/round-37-c2.sh`.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — pointer: `PROVINCE.md`, unchanged; release-feed ownership noted by K37ConnFeeds (no sibling overlap).

No `[x]` box: no named non-author verifier has checked these boxes this round.
