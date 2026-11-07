# kumitate — round 97 report (hyaku run 15, attempt 1)

Lane `kumitate-shokunin`, branch `master`. Base `477afff790787cd2ce48ccf976afafcb5aef0cbc` (r96 closure spot-check
tip) → final `243fecd13de2ddc01e830bffbce6758ddb64cee9`. L1 `KumitateR97` (holds the §3 planner seat). Prompt `.ufo/prompts/kumitate-round-97.md`.
No earlier attempt of this round (`.ufo/watchdog.log`: one `launch kumitate round=97 … attempt=1`, no
`lane-dead-no-report`).

## Work performed

Declared claims (1): **C1 — operability** (lowest non-retired axis; integer 9, terminal under `f_O`): the lane gate
`scripts/sources-check.mjs` reads `corpus/SOURCES.md` `## Registry` membership exactly as the fleet census `row_pass`
does (rule R97: section state from `sourceText.split('\n')` with CR kept; `^ {0,3}##[ \t]` sets the section to its
`[ \t]`-trimmed text, inside iff exactly `Registry`; `^ {0,3}#[ \t]` clears; starts outside; rows and per-row checks
unchanged). Sourced on S276 (ECMA-262 2025), opened this round. Not exploratory. Every coverage row is a harm surface.

- Pre-freeze adoption of the r96 verifier spot-check into the README map (M94-1 ordering): `017bdd74`,
  `.ufo/waves/round-97/close-l1/adopt-r96-spotcheck.txt` (DRIFT → `README_MAP: CLEAN files=249`).
- Freeze `38eb197c17de7ce0dc562539f2f31f41bea037ec`: `plan.md` (rule, predicate, kill rules K1–K4), frozen counter
  `probe/probe97-c1.mjs` (nonce, census-grammar-derived 19 459-case battery on LF / whole-CRLF / mixed-CRLF fixtures,
  census run live; arms a–f), generator `probe/make-controls97.py`, 17 pre-data controls (`controls/*.txt`:
  `ctl-positive` HELD, `ctl-nothing` + 15 one-clause violations UNMET), open battery + census (`open/`).
- Wave w1 spec + validator dispatch `8535793d` (`w1-spec.json`, `w1-dispatch.json`, 11 seats, v1 policy); handed off
  via `w1.ready`; WAVE-DONE received; `w1-results.json` 11 results, 0 dead.
- Integration M `69fb6943dd0d87165cbb73954a952ce9cb6753ec` = K97ExecTool READY bytes (sha256 `ccbf1619…`, selftest
  46 → 68); frozen counter at M `C97_C1: HELD a=1/1 b=1/1 c=1/1 d=1/1 e=1/1 f=1/1` ×2
  (`.ufo/waves/round-97/close/probe1.txt`, `probe2.txt`).
- M2 `f33786f0354bcda8fdd09f95cee487f14bf4e49c`: three selftest arms for K97Mutation's counter-only kills
  (m18/m19/m25), selftest 71/71 (`close-l1/selftest-M2.txt`), the three mutants now fail (`close-l1/m2-teeth.txt`,
  `M2_TEETH: killed=3/3`); counter at M2 HELD ×2 (`close/probe-m2-1.txt`, `probe-m2-2.txt`, `tool_sha256=acccb0d7…`).
- K2 re-mutation of the shipped M2 bytes: `REMUT: killed=15/15`, reference block 71/71 PASS
  (`close-l1/integration-remut.txt`); first run discarded as invalid (M97-2, `close-l1/integration-remut-run1-invalid.txt`).
- Attacks: K97Reviewer (no blocker, 30 hand cases vs live census; `w1/K97Reviewer.md`); K97CriticA (six counter
  constructions outside the class grid reach HELD — routed; `x-replay` HELD own seed / UNMET fresh seed = M97-1 fix
  shown able to fail; `K97CriticA/constructions.md`); K97CriticB (framing sound: the CRLF class is live in six sibling
  lanes, 13 blobs 2026-11-01..04; `w1/K97CriticB.md`); K97CriticC (H97 SURVIVES 1 274/1 274, BASE 1 143;
  `K97CriticC/H97.md`); K97Mutation (28 mutants: 21 selftest, 3 counter-only, 4 equivalent; `K97Mutation/mutants.md`);
  K97Connector (round-gate r96 vs candidate vs census 19 459/19 459 on all three fixtures; sibling transfer;
  `w1/K97Connector.md`); K97ExecHarm (BASE vs candidate `--json` byte-identical on the real lane; consumer list;
  `w1/K97ExecHarm.md`); K97Scout (fleet heading classes: 0 CRLF in current registries; `w1/K97Scout.md`).
- Close `647de5c1`: lesson `corpus/lessons/round-97.md`, knowledge `corpus/knowledge/sources-check-registry-section.md`
  (verified-at M2), S276 + search-log entry, QUALITY Q91, SKILL sources-check row, README map rows, LOG r97, SCORECARD
  stanza re-declared + r97 disposition + r98 pre-registration; Q89 `WORDCOUNT: CLEAN pairs=2`, Q90
  `LESSON_URLS: CLEAN new=1` (`close-l1/q89-round-97.txt`, `q90-round-97.txt`).
- Final receipts `243fecd13de2ddc01e830bffbce6758ddb64cee9`: `close/battery-final.txt` (all CLEAN / exit 0, `PROXY: MATCH` incl. `--strict`),
  `close/census-after.txt` (exit 0), `close/q88-r97.txt`.

## Landed changes

| lane commit | LOG.md entry | change |
|---|---|---|
| `017bdd7446c6f7bff5f7f9d63196af5e25c3a3ea` | `## Round 97` | r96 spot-check adopted into README map before the freeze |
| `38eb197c17de7ce0dc562539f2f31f41bea037ec` | `## Round 97` (Declared) | freeze: plan, counter, generator, 17 controls, open receipts |
| `8535793de5701b467af3d5d2b224630f6f3aec13` | `## Round 97` | wave w1 spec + validated dispatch |
| `69fb6943dd0d87165cbb73954a952ce9cb6753ec` | `## Round 97` (M) | `scripts/sources-check.mjs` R97 section reader (READY sha256 `ccbf1619…`) |
| `f33786f0354bcda8fdd09f95cee487f14bf4e49c` | `## Round 97` (M2) | three selftest arms (68 → 71) |
| `e95dcb5820f2515533a897cf664c9538b06b188a` | `## Round 97` | wave evidence (11 seat dirs, trailers, results) + L1 close receipts |
| `647de5c18a3ff9304ca74aacb053f9cc2807f7e6` | `## Round 97` + one-line record | lesson, knowledge, S276, Q91, SKILL, README map, LOG, SCORECARD |
| `243fecd13de2ddc01e830bffbce6758ddb64cee9` | `## Round 97` | final battery, census after, Q88 receipt; SCORECARD move-log row 97 + `## Planned` pointer to the r98 pre-registration |

## Before → after measurements

| claim | counting command | before (commit) | after (commit) |
|---|---|---|---|
| C1 operability | `node .ufo/waves/round-97/probe/probe97-c1.mjs --tool <git show REV:scripts/sources-check.mjs> --work <scratch> --freeze 38eb197c… --rev REV` | `C97_C1: UNMET a=0/1 b=0/1 c=0/1 d=1/1 e=1/1 f=1/1` — BASE disagrees with the census on 738 / 5 220 / 2 999 of 19 459 cases (`controls/ctl-nothing.txt`, base bytes `5402b210…` = `477afff7`) | `C97_C1: HELD a=1/1 b=1/1 c=1/1 d=1/1 e=1/1 f=1/1` ×2 at M `69fb6943` (`ccbf1619…`) and ×2 at M2 `f33786f0` (`acccb0d7…`) — 19 459/19 459 on each fixture |

Supporting: selftest `node scripts/sources-check.mjs --selftest` 46/46 → 71/71; re-mutation 15/15 at M2. Axis
integers: operability 9 → 9 (terminal), every coverage row 10 → 10 (`node scripts/proxy-check.mjs --strict` →
`PROXY: MATCH … operability=9 … coverage=10` at `243fecd13de2ddc01e830bffbce6758ddb64cee9`).

## Sources & frontier

SOURCES rows before → after: **213 → 214** (`grep -cE '^ {0,3}\| S[0-9]{3}' corpus/SOURCES.md` at `477afff7` /
`647de5c1`). Added by tier: A +1 (S276 ECMA-262 2025, https://tc39.es/ecma262/2025/, opened 2026-11-07, `mined`,
`on-release`, used-by `corpus/knowledge/sources-check-registry-section.md`). Rows touched old→new: none. Frontier
advanced: the lane's second registry reader now on the census grammar (knowledge entry cites S276, S275, S274).
Census `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kumitate`: round start exit 0
(`open/census-before.txt`), round end exit 0 (`close/census-after.txt`; W04 warnings only). Mined mistakes: M97-1
(fixed-identity counters → Q91, shown able to fail) and M97-2 (L1 helper read post-integration bytes) in
`corpus/lessons/round-97.md` `## Mistakes`. Sourced claim: C1 rests on S276. Assimilation: none (no `merge/kumitate/`
theme fits a section reader). considerthese: not mined this round (latest `considerthese/2026-11-06.md`; no proposal
fits C1).

## Trend verdicts

- **expansion: improved** — new knowledge `sources-check-registry-section.md` citing S276 (opened, re-opened by the L1:
  `close-l1/l1-open-ecma262.txt`); SOURCES 213 → 214.
- **quality: improved** — the lane gate now agrees with the census on every class of the 19 459-case grammar battery
  (was 738 / 5 220 / 2 999 disagreements) and on 1 274/1 274 differential cases (BASE 1 143); selftest 46 → 71;
  re-mutation 15/15; real-lane `--json` byte-identical (no harm).
- **discernment: improved** — the counter's own blind spot recorded as a rejection (six HELD constructions, routed),
  JS/CommonMark readers rejected with flip conditions, two mistakes mined with fixes shown able to fail.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md:614` sources-check row now carries the R97 section decision (lane commit `647de5c1`); no non-author verifier yet.
- [~] At least one end-to-end domain task executed and logged in LOG.md — LOG.md `## Round 97` (tool, frozen nonce counter and live fleet census exercised end to end; M and M2 measured).
- [~] Instructions executable by an agent without oral context — `node scripts/sources-check.mjs --selftest` → `SOURCES_SELFTEST: 71/71 pass`, exit 0 (`.ufo/waves/round-97/close-l1/selftest-M2.txt`).
- [ ] No cross-domain bleed (PROVINCE.md still accurate) — PROVINCE.md untouched this round.

## Round shape, seats, extras

- Shape: ONE v1 wave `w1`, **11 seats** (executor ×2, scribe ×2, scout, connector, reviewer, critic ×3,
  mutation-tester); attack 5/11 = 45 %; no residual call; round total 11. Dead seats: 0 (`w1-results.json`). Every
  role was validator-accepted (r96 routed item 2). K97ExecTool wrote READY late; seats attacked `ctl-positive` or the
  builder's on-disk bytes and said so; READY sha256 `ccbf1619…` is the integrated M.
- Counter finding (status-neutral, routed to r98): K97CriticA's six constructions outside the class grid reach HELD;
  the frozen verdict stands (K4), the shipped bytes rest on R97 by construction plus selftest and differential.
- Lane leftover resolved: K97ScribeSources' 7 MB ECMA-262 capture (`captures/ecma262-2025.html`, over the helper's
  1 MiB limit) was moved out of the lane to scratch, not committed; its sha256 `c1f9a159…` is in
  `K97ScribeSources/quotes.md` and `close-l1/l1-open-ecma262.txt`.
- L0 questions: none new; `kumitate | round-96` (census `\r` split) stays open.
- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
- Misroot sweep: none from this round (`close-l1/misroot-sweep.txt`; `trail-ids.txt` at the fleet root predates the round).
- Tool installs: none (L1 and every seat trailer that mentions it: none).
