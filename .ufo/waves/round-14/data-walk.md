# Round 14 data walk — protocol lane

## Scope and baseline

- Mission-owned axes: `fleet-meta` protocol soundness and gate integrity (`MISSION.md` + `AXES.md`).
- `SCORECARD.md` scores both at 8/10. The queued body target was 526→≤470 lines, but that used an older snapshot; use the committed baseline below.
- Baseline: `310967c:PROTOCOL.md` (same 541 lines / 50,603 bytes as `HEAD` `4d518fe`) via `git show 310967c:PROTOCOL.md | wc -l -c`; `f3cbdcf` (526 / 49,269) is historical.
- Final candidate: body 470 lines / 40,917 bytes; appendix 48 lines / 12,106 bytes; required pair 518 lines / 53,023 bytes. Preserve the preceding round-13 marker unchanged.
- The inherited candidate and `.ufo/waves/round-13/` verification evidence are not yet durable. `SCORECARD.md` also has unrelated aggregator-section edits; protocol edits must not stage those hunks.

## Observed checks on the inherited candidate

- `sh .ufo/waves/round-13/verify-protocol.sh PROTOCOL.md --appendix PROTOCOL-APPENDIX.md` → clean, 8 checks, 0 failed; census 169/169, anchors 61/61 (7 not line-exact), modal body 118/105, appendix 20/15, 17 body pointers, 39/32 appendix rows, 13 cross-references / 0 unresolved, body 470/470 and appendix 48/60 lines.
- The same gate with `--selftest` → 18/18 mutation cases passed (8 single-file + 10 paired-appendix cases).
- `.ufo/waves/round-11/verify-census.sh PROTOCOL.md .ufo/waves/round-13/obligation-census-r13.tsv` → 169/169, 0 missing.
- `git diff --check -- PROTOCOL.md` → clean.
- `.ufo/waves/round-13/closure-check.py --selftest` → 19/19. Live `--no-citations` snapshot → exit 1, debt 19, contradictions 0, unrowed terminated 6, pending round 4; history pin anchored at `ae19fca`, prefix `k=48`. This is live fleet debt, not a clean gate or a score gain.

## Paired-artifact cost and review boundary

- The required pair is 518 lines / 53,023 bytes versus the baseline single file's 541 / 50,603: 23 fewer lines but 2,420 more bytes. The body alone moves 541 / 50,603 → 470 / 40,917 (−71 lines, −9,686 bytes); do not call the full pair smaller.
- Manual review compared directly to `310967c:PROTOCOL.md` and restored the promotion minimum evidence, uncommitted-at-completion rule, closure-record contents, dead-daemon/no-kill guarantee, aggregator report scope and ledger reconciliation, domain exclusivity, `CORPUS.md` ownership, and appendix provenance. The candidate-derived 169-predicate census is not independent semantic proof; low-severity rationale cuts remain, so no full-equivalence claim.

## Scope decision

- Select the queued protocol-soundness move because the body target is met. Keep both scores at 8/10: the required pair costs more bytes and the preservation gate is not a semantic-equivalence proof. Keep gate-integrity scoring unchanged, report live closure debt, and avoid edits to watchdog, manifest, sibling repos, or other lane sections.
