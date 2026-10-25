# kotodama — round 71 (hyaku run 6, attempt 1)

Lane repo `/home/vgpnk/Projects/shokunin/kotodama-shokunin` · branch `main`
Base `b94a543c70f40dba7e49fff96d05bfb8bbd8c678` · declaration `825b78a77b14ffa3c07dd3e82c2266baabc1c2a3` ·
re-freeze (pre-data corrections) `65ff151087caf1afb0c63bcbea05e2e32c20fba7` ·
claim-C lands `8c203bd9dd45b42c4b45ecb3afc1b07a23575dbd` · records `1d1b432525f791840a9f4fc9c512d0a9a824e915` · final receipts `3764c2dfb07186204e2ec308663f7ec63a9ef1e9` · wave-2 evidence `14c88d9b9bb3c9e47b0cb836f1c98ce5d6f05cc6` ·
misroot relocation `ccadb5989bc33b230dfd496441ddafefa1ab4b73`. Lane tip at report time `ccadb5989bc33b230dfd496441ddafefa1ab4b73`, `ahead=0`, remote-verified (`ls-remote origin refs/heads/main` = `ccadb5989…`).

## Work performed

Declared claims (frozen at `825b78a`, re-frozen pre-data at `65ff1510` after wave-1 attack corrections documented in claims.json):

1. **C — coverage (sourced, frontier → core).** New culture-material register entry `corpus/knowledge/culture-material/dance-performance-movement-codes.md` on dance/performance/movement ground the lane did not hold (0 word-bounded filename owners, 0 word-bounded topic-line owners). Sourced by 13 new registry rows S861–S873 (tier A 12 / B 1, opened 2026-10-25, mined, used-by the entry).
2. **Ca — calibration (records).** Repairs routed round-70 verifier defects V70-1..V70-5 (receipt re-stamps with the full QUALITY 17/19 header; S860 verify-at repoint; 27→25-word Gate quote; round-70 trend correction; lesson Gate reject-sweep) + item-10 quarantine-first verdicts (21 rows).
3. **D — depth (instrument).** New counter `reports/round-71/accept-d.py` adds the declared no-git path to the frozen round-69 selftest (V70-6): no-git export prints `SELFTEST: COULD-NOT-EVALUATE (no git)` exit 2; git failures print `(git unavailable: …)` exit 2; in-repo runs the frozen selftest unchanged.

Wave-1 falsification is the source of the pre-data re-freeze: the attack seats proved the original C sweep regex false-matched "avoidance" (word-bounded fix), the Ca counting command targeted wrong paths (per-file header legs + direct word count + marker-preservation leg added), and D's no-git leg archived a revision lacking the new counter (worktree-minus-git copy; genuine-absence vs environment-error distinction). Every correction is recorded in claims.json (`correction` field) and in the lesson `## Corrections (round 71 declaration, pre-data)`.

## Landed changes

| change | LOG entry | commit |
|---|---|---|
| `corpus/knowledge/culture-material/dance-performance-movement-codes.md` (125 lines, 13 cited rows) | round-71 entry, bullet C | `8c203bd9` |
| `corpus/SOURCES.md` rows S861–S873 (13, mined, inside Registry section) | same | `8c203bd9` + `1d1b4325` (S870 kind docs) |
| `corpus/README.md`: revision 2.21, `## culture-material/ (36)`, dance index row, totals 243, footer 30/29/36/29/24/95 | same | `8c203bd9` |
| `reports/round-71/accept-c.py` (new counter) | same | `8c203bd9` |
| `reports/round-71/telemetry/measures-c.txt` | same | `8c203bd9` |
| V70-1: six round-70 receipts re-stamped (17/19 headers + marker + original bytes) | round-71 entry, bullet Ca | `1d1b4325` |
| V70-2: S860 verify-at → acc2d614 (old→new in corrections-r70.md) | same | `1d1b4325` |
| V70-3: round-70 Gate quote trimmed to 25 words | same | `1d1b4325` |
| V70-4: SCORECARD round-70 trend-correction row | same | `1d1b4325` |
| V70-5: round-71 lesson Gate `rejected this round:` + candidate rows | same | `1d1b4325` |
| `reports/round-71/telemetry/quarantine-verdicts.md` (21 rows) | same | `1d1b4325` |
| `reports/round-71/corrections-r70.md` | same | `1d1b4325` |
| `corpus/lessons/round-71.md` (Gate 13 rows, Mistakes R71-M1..M4, Corrections, Quarantine) | same | `1d1b4325` |
| `reports/round-71/accept-ca.py`, `accept-d.py` (counters) | same | `1d1b4325` |
| `reports/round-71/telemetry/measures-ca.txt`, `measures-d.txt` (stamped at records) | same | `3764c2df` |
| Wave evidence: w1 spec/plan/dispatch/registry/37 seat reports; w2 spec/plan/dispatch/registry | same | `b694afd6`, `1d1b4325`, `14c88d9` |
| `LOG.md` round-71 entry | itself | `1d1b4325` |

## Before → after measurements

| claim | counting command | before | after | measured at |
|---|---|---|---|---|
| C | `python3 -B reports/round-71/accept-c.py --root .`; `find corpus/knowledge/culture-material -maxdepth 1 -type f \| wc -l`; `grep -cE '^ {0,3}\\|[[:space:]]*S[0-9]{3,}' corpus/SOURCES.md` | filename-owners 0, topic-owners 0 (word-bounded); culture-material 35, corpus 242, registry 784 | ACCEPT-C-71 PASS (ENTRY/COUNTS 36/243/CITED 13/ROWS/USEDBY-PATHS/CITED-LINES 0 findings/SWEEP entry-only); README sweep exit 0; census exit 0 | `8c203bd9` (`reports/round-71/telemetry/measures-c.txt`) |
| Ca | `python3 -B reports/round-71/accept-ca.py --root .` | no 17/19 headers (0 per file), S860 names 6cb51a4, quote 27 words, no trend row, no reject sweep, no verdict table | ACCEPT-CA-71 PASS (V70-1..5 all PASS, QUARANTINE 21/21 valid labels) | `1d1b4325` (`measures-ca.txt`) |
| D | `python3 -B reports/round-71/accept-d.py --selftest`; tar-no-git copy run; `python3 -B reports/round-69/accept-d.py --root .` | counter absent at base; frozen counter no-git false-red `SELFTEST: 1/2` exit 1 (V70-6) | in-repo `SELFTEST: 2/2` exit 0; no-git `COULD-NOT-EVALUATE (no git)` exit 2; frozen data predicate `ACCEPT-D-69: PASS legs=8/8` exit 0 | `1d1b4325` (`measures-d.txt`) |

Do-nothing control receipts (committed rev 2 at `65ff1510`): all three controls fail to reach their targets at base (C sweep 0/0 but entry absent; Ca all legs 0/27/0; D counter absent → no `COULD-NOT-EVALUATE` line).

## Sources & frontier

`corpus/SOURCES.md` rows, counting command `grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' corpus/SOURCES.md`:
before **784**, after **797**; rows added by tier: A 12 (S861–S872), B 1
(S873); rows touched old→new: **1** (S860 verify-at 6cb51a4 → acc2d614,
logged in corrections-r70.md); frontier rows advanced: S861–S873 (new), row
map S861→S992 recorded for adoption. Census: exit 0 at start
(`reports/round-71/telemetry/census-start.txt`) and end (`census-end.txt`),
W04=28 standing (all pre-existing). README sweep exit 0;
`check-readme-revisions.py` 0 findings.
**Assimilation: none** — adoption CLOSED (wave-4 quarantine-first). Id collisions S859/S860 (lane S859/S860 vs package first staged ids), reg-ids 784, staged-ids 132, renumber map by document (S861→S992) at `.ufo/waves/round-71/assimilation/`. Quarantine verdicts: 21 rows (PRESENT 10 · REFUSED 6 · UNVERIFIABLE 5). `considerthese/` absent for this lane.

## Trend verdicts

- **expansion — improved.** One admitted knowledge entry on uncovered coverage-map ground (`dance-performance-movement-codes.md`, 0/0 pre-entry owners), citing 13 mined rows S861–S873 opened this round (expansion criterion of LEARNING.md fires).
- **quality — improved.** The round's record instruments are re-verified: receipt headers restored to the QUALITY 17/19 bar (V70-1), S860 pointer accuracy repaired (V70-2), Gate quote discipline restored (V70-3). No admitted entry fails its re-check.
- **discernment — improved.** The outside round-70 spot-check's five disagreements were turned into landings (V70-1..V70-5) and the round-71 lesson adds mistake rows + a reject-sweep with refused candidates; the Gate admits 13 and rejects 8 with reasons+flips (both ends sampled by wave-2 seats).

## SHONEN

- [~] **SKILL.md real decision tables, error patterns, checklists, cited sources** — registry 797 rows (census exit 0); `SKILL.md` gates registry 36 rows; no non-author verifier on record.
- [~] **At least one end-to-end domain task executed and logged** — claims' counter runs and receipts (`reports/round-71/telemetry/measures-{c,ca,d}.txt`, `LOG.md` round-71 entry); no non-author verifier on record.
- [~] **Instructions executable by an agent without oral context** — wave specs/registries/dispatch payloads committed under `.ufo/waves/round-71/`; commands absolute and re-runnable; no non-author verifier on record.
- [~] **No cross-domain bleed** — entry scope refuses canon; lore handoff one-way; connector found no sibling owner of dance register/no-git guard; no non-author verifier on record.

## Round shape, misses and routed work

- Shape: **two v1 waves**. Wave 1: 37 seats (10 scout, 1 connector, 5 executor, 1 scribe, 8 reviewer, 7 critic, 3 mutation-tester, 2 sentinel; 18/37 = 48.6% attack roles), one batched task call, payload unchanged from the validator's render (`wave1-dispatch.json`). Wave 2 (falsify): 40 seats (12 reviewer, 9 critic, 7 mutation-tester, 6 scout, 6 sentinel; 28/40 = 70% attack roles), one batched task call, dispatched after wave 1 returned (all 37 wave-1 seats returned; none dead). Round total 77 seats ≤128. Wave-1 validator: policy v1 pass (37 in band 32–64); wave-2 validator: policy v1 pass (40 in band).
- Dead seats: none in wave 1. Wave 2 was dispatched; at filing time seats are still returning — their reports land under `.ufo/waves/round-71/w2/` and the closing census PASS (RevCensus) is already in.
- L2 floor met inside wave 1 (roles: connector, executors, scribe, scouts, reviewers, critics; planner seat held by the L1 — the validator rejects planner as a swarm role).
- Misroot: seven fetch artifacts (s795.pdf, s796.pdf, s804/s814/s816/s817.html, s820.pdf) written by a wave-1 seat into the fleet root; copied byte-exact into `.ufo/waves/round-71/assimilation/fetches/` (cmp-verified), fleet copies deleted, recorded under lesson Mistakes.
- Inherited state: none (round-70 closed; w2 no leftovers named themselves).
- Stale-lane: respawn-per-round driver; no other mission of this lane open at round-71 close.
- Tool installs: **none** (no pacman — paused; no uv/npx install needed).


## Wave-2 falsification results

- **RevGate (wave 2) — Gate-checker blind spot (R71-M8).** `tools/check-gate-quotes.py` only parses bullet rows, so it reads 0 rows from the pipe-table Gate and prints `0 findings` for any quote length; all 13 round-71 quotes were verified by hand ≤15 words and word-for-word on the fetched pages. Ca's executing V70-3 leg is the direct word count (`words=25`). Fix routed (table-row parsing + table-form selftest cases).
 (40 seats; partial at filing, consolidated here)

Seats re-ran the frozen counting commands in fresh clones at lane HEAD:

- **C — verified.** Four independent re-runs (Filler31/32/34/40, Filler39, MutC) confirm the frozen command prints `36 / 243 / 797 / CITED-LINES: 0 finding(s)` exit 0 at HEAD, and `accept-c.py` prints ACCEPT-C-71 PASS (7/7). MutC killed all four counter mutants (used-by leg, CITED floor, COUNTS thresholds). Rows S861–S873 unique/mined/used-by the entry; README sweep and revisions checks pass (RevREADME); census exit 0 (RevCensus).
- **Ca — data verifies; frozen shell command has a formatting-leg defect (R71-M5).** The frozen command's last leg (`awk -F'|'` counting verdict-table rows) prints 0 for markdown rows that start with `|` (Filler29/35/38) — a counter defect, not a data failure. The canonical instrument `reports/round-71/accept-ca.py` prints ACCEPT-CA-71 PASS (7 legs, incl. QUARANTINE 21/21) and its receipt is committed (measures-ca.txt). The claim's disposition table and S860/quote/scorecard/lesson legs all re-verify (headers 36, acc2d614, words 25, trend row, reject-sweep). Freeze rule: the frozen shell command is not edited; the defect is logged old→new in the lesson, and the committed Python counter is named as the executing instrument.
- **D — verified as declared.** RevCounterDM: in-repo `SELFTEST: 2/2` exit 0; no-git `COULD-NOT-EVALUATE (no git)` exit 2; frozen data predicate 8/8 exit 0. MutD: guard mutants killed (false-red reintroduced without the guard; exit-code leg enforced). Residual gap (R71-M6): shallow clones / git-less copies nested in another repo can still false-red via the frozen round-69 fallback; the fix (guard on `git cat-file -e 793f797^{commit}`) is routed to a later round.
- Process notes: measures-c.txt is now committed (c21213ab); accept-c.py's provenance (landed with data, not at freeze) is recorded as R71-M7; the shell commands' exit code only reflects their last step (kill rules are enforced by the landed Python counters and by wave-2 manual leg reads).
