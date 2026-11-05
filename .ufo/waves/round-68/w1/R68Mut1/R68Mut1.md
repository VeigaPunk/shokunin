# R68Mut1 — C1 gate mutation probe (tabi round 68, w1, pre-freeze)

Scope: scratch-only mutants of `scripts/check-adjacency-adjudication-r68.mjs` (C1 gate, 15-case selftest). No production or sibling file was modified. Lane base 1746c53de7d56e8aeaf420a68b5b95e6af96adf8. Status: PRE-FREEZE, no claims frozen; the "pending-non-author" rows below are gate fixture rows, not adjudications.

## Axes named
Duplicate key · missing key · quote equality · head equality · author adjudicator · pending polarity. Two detector-edge extras: pending-count check, quote-unresolved check.

## Producer / pin
- Production producer (pristine, unchanged after run): `scripts/check-adjacency-adjudication-r68.mjs`, sha256 `e7f042916833828096c9550b299085934ad195aa318b864cfd7f68cc86963c1e`.
- Runtime: node v24.21.0, git 2.56.0 (system binaries; nothing installed or updated by this seat).
- Scratch-only copies were used; the gate is run as `node <file> --selftest --scratch <dir>`; each mutant got its own fixture dir `fix-<id>` under scratch.

## Baseline (pristine) — receipt `receipts/baseline.json`
- argv: `node /fast/scratch/hyaku/tabi-r68/R68Mut1/gate.mjs --selftest --scratch /fast/scratch/hyaku/tabi-r68/R68Mut1/fixbase`
- rc 0; stdout `{"verdict":"clean","cases":15,"failed":0,...}`; 15/15 cases observed expected rc and expected tokens.

## Mutants — each is exactly one changed line vs. pristine (verified by line diff in the runner)
Mutant files persisted in `mutants/`; per-run receipts (argv, rc, stdout, fixture shas, diff, failed cases) in `receipts/<id>.json`; consolidated in `receipts/index.json`.

| id | file:line | single change | axis | expected | rc | verdict | failing selftest case(s) | mutant sha256 |
|---|---|---|---|---|---|---|---|---|
| M1-dupkey-off | L187 | `if (seen.has(key))` → `if (seen.has(key) && false)` | duplicate key | killed | 1 | KILLED | duplicate-key | 17f9ca3ac5258172af6b3a73be2c344a4962037e244fb8e5a8e2fc8aec308333 |
| M2-missingkey-off | L212 | `if (!seen.has(key))` → `if (false && !seen.has(key))` | missing key | killed | 1 | KILLED | missing-row | 8529da48be8638148e878a869d9b552a8643bb0c8e7ecfb16f1fc31950830f2f |
| M3-quoteeq-off | L193 | `if (quote !== expected.quote)` → `if (false && …)` | quote equality | killed | 1 | KILLED | quote-mismatch (token) | 11d6a6895c83604200c832cc7f4e102468b71442cc170c3c2446cd6a949f0214 |
| M4-headeq-off | L194 | `if (head !== expected.laneHead)` → `if (false && …)` | head equality | killed | 1 | KILLED | head-mismatch (token) | 058969b0d5335e178673609cb6511066fc79e18f948447a093500f2d4bb55ab3 |
| M5-author-tabi-off | L204 | `adjudicator === 'tabi' \|\|` → `false \|\|` | author adjudicator | killed | 1 | KILLED | adjudicator-author | 5fa4e50ce64c67dfa2c865a9fd3a5bcad2efe267c8a988ebf4f816089bb45849 |
| M5b-author-endsWith-off | L204 | `adjudicator.endsWith('-shokunin\ttabi')` → `false` | author adjudicator | survive (dead clause) | 0 | SURVIVED | none | 885eaad9c08b19367c36872012f4b498433cdb6e0a1d437725204da8ee230a7a |
| M6-pendingpolarity-off | L196 | `if (status === 'pending-non-author')` → `!==` | pending polarity | killed | 1 | KILLED | green, pending-fields-dirty, adjudicator-author | b807808bf3f832c81b24f5460b435279b0fbacc014e1e2045b7fc2d14c01ea93 |
| M7-pendingdirty-off | L199 | `if (cell !== '—')` → `if (false && …)` | pending cells clean | killed | 1 | KILLED | pending-fields-dirty | bea4331d76ecedd6fb7e5e80a924f0067d391a96cd1d7fa2ba8273d1a7860681 |
| M8-expectpending-off | L214 | `pending !== Number(args['expect-pending'])` → `false` | pending count (extra) | survive (untested) | 0 | SURVIVED | none | 66bbba31f409c23b9cb3909bbd8f929277b019b007535f6afbac8c90538935e5 |
| M9-quoteunresolved-off | L225 | `else if (!out.content.includes(res.quote))` → `false && …` | quote-at-head (extra) | killed | 1 | KILLED | quote-unresolved | 83ab7108940e38e566cda6ed2da1bcd40bd7e69d0a411e3b20b23fd1999f9642 |

Kill count: 8 of 10 (M1–M4, M5, M6, M7, M9). Survivors: 2 (M5b, M8).

Mutant argv pattern (each): `node <mutant>.mjs --selftest --scratch <scratch>/fix-<id>`; fixture shas recorded per run in each receipt.

## Findings

1. **M5b survives — dead clause, [INFERENCE] equivalent mutant.** `parseTsv` splits every line on `\t`, so no cell can contain a tab; `adjudicator.endsWith('-shokunin\ttabi')` can never be true. The clause is unreachable, so its removal is behaviour-preserving and no fixture can kill it. Either delete the dead clause or replace it with the intended lane check (see finding 3).

2. **M8 survives — no selftest case exercises the pending-count ceiling.** The only use is the green case (`--expect-pending 3`, 3 pending rows), so a wrong count is never observed. Coverage gap in the pending-polarity axis.

3. **Real gate gap (not a mutant): lane-named adjudicator is accepted.** The gate blocks only the literal `tabi`. Probe on the pristine gate (`receipts/adjudicator-literal-probe.json`):
   - `probe-lane-name-adjudicator`: adjudicator `tabi-shokunin`, status `adjudicated-agree` → **rc 0**, `ok:true`, no findings.
   - `probe-literal-author-control`: adjudicator `tabi` → rc 1, `adjudicator-author`.
   The gate header states "the lane itself can never be the adjudicator of record"; the current check does not enforce that for the lane's own name. Recommend an exact-lane check (`tabi-shokunin`) plus a selftest case. Not fixed here (production is out of bounds for this seat).

4. **M3 and M4 are only caught at token level.** For `quote-mismatch` and `head-mismatch` fixtures, the selftest exit code is 1 even with the specific check removed, because downstream `quote-unresolved` / `path-unresolved` fire too. The check is therefore pinned only by the `byCheck` token assertion. If the token check were relaxed, these two checks would have no independent regression coverage.

5. **M6 kill is broad.** Flipping pending polarity also breaks the green case, so polarity is well covered; the kill is not isolated to one case.

## Restoration / hygiene
- Scratch `gate.mjs` restored byte-exact to `pristine.mjs` after each mutant run (asserted by sha in the runner; restore matched pristine sha `e7f042…` each time).
- Production file sha re-checked after all runs: `e7f042916833828096c9550b299085934ad195aa318b864cfd7f68cc86963c1e` (unchanged).
- No git/jj mutation. No subagent. No installs. No sysctl/host/service change. No /tmp use.
- Scratch dir `/fast/scratch/hyaku/tabi-r68/R68Mut1/` deleted after persisting receipts and mutant copies (below).

## Not done / out of scope
- Did not regenerate or assess the C1 worksheet (`.ufo/waves/round-68/counters/build-worksheet-r68.mjs`) or the r[5]→r[6] quote-index correction; that is a sibling's assignment. This probe tested only the gate's selftest behaviour.
- Did not run the C2 selftest or any whole-repo check.

## Evidence index (lane-relative)
- `.ufo/waves/round-68/w1/R68Mut1/mutants/*.mjs` — 10 mutant files (M1, M2, M3, M4, M5, M5b, M6, M7, M8, M9) plus pristine-equal reproduction of M1 verified by sha.
- `.ufo/waves/round-68/w1/R68Mut1/receipts/baseline.json`, `M*.json`, `index.json`, `adjudicator-literal-probe.json`.
- Report location note: the seat spec named `.ufo/waves/round-68/w1/R68Mut1.md`; this report is placed inside the sole output directory `.ufo/waves/round-68/w1/R68Mut1/R68Mut1.md` per the bounds.

## Production drift observed during this seat (addendum)
- After the mutant runs, `scripts/check-adjacency-adjudication-r68.mjs` (untracked in the lane, `git status` `??`) changed on disk at 08:54:35 -0300: size 16420 → 16506, sha256 `e7f042…` → `3bfcee113ddaa7b9cc9284f59afff9094db65d9acab9d10d099f1dc3bbe53de7`. The sole change is one added line in `parseArgs` (`if (key === 'json') { args.json = true; continue; }`, line 59). This seat did not write to production; all of my edits targeted scratch copies. The author of the change is not known to this seat.
- Mutants M1–M9 and the baseline were run against the e7f042 pristine text, which was production at run time. The changed line is outside every mutated line (187, 193, 194, 196, 199, 204, 212, 214, 225), so the mutant results still describe the logic, but they were not re-run on the new file.
- Current-production selftest, run read-only against production with output confined to a fresh scratch dir: argv `node scripts/check-adjacency-adjudication-r68.mjs --selftest --scratch <scratch>/fixcur`; rc 0; stdout `{"verdict":"clean","cases":15,"failed":0,...}`. Stdout persisted at `receipts/current-prod-selftest.out`.
- Gap finding 3 (lane-named adjudicator accepted) was probed on the e7f042 pristine copy; it is not re-probed against the current file.
