# kasegi — round 95 report

Lane: kasegi. Round 95, attempt 1. Driver: `2026-11-07T13:47:48-03:00 launch kasegi round=95 pgid=2566176 driver=hyaku-inline attempt=1`.
Lane repo `/home/vgpnk/Projects/shokunin/kasegi-shokunin`; base `9ef0126cc60b7f62baafd04f3e52c45e2a8e2f10`;
freeze `347519f21524d2bc13eb6c91cf3550930a4265b3`; C1 landing `53ec479d71d25cf5be052db794a548a5904564b8`;
C2 landing `38e7319f44a9fab2978b59ffd43faf207cf62b32`; integration `43cc15e8d807a06baf9d2dd789bb121364944169`; wave findings `01ff9865d9367ce5ee9a2bb35dd68cef1bad2100`; results handoff `f6b94519e4716aa251ac39089a9d64a3b727100f`; **lane tip `1e7b42692ef7ee35dc91764c58a0ecf73e02d3fe`** (pushed; `git ls-remote origin refs/heads/master` prints the same hash).

**Declared claims (2, frozen before data in `.ufo/waves/round-95/claims.json`).**

- **C1 — `depth:verifiability`** (lowest non-retired axis, score 4): tranche 10 closes the eleven rows round 94 deferred (nine cell/part rewords on `corpus/knowledge/triage-thresholds.md`, the 396 and 436 repoints the round-94 wave's non-author reviewer wrote) plus five bare `S041.txt` capture citations, under a successor counter with an empty EXCLUDED set whose every fixture clones the pinned base (round-94 defect 1). After: 16 edits, M10 mapped 16/16 excluded 0, meter **1007/1998 → 1008/1994**, controls 15/15 at the landing.
- **C2 — `coverage`** (score 8 held; capability extension of `capture-secret-scan`): `github-refresh-token` (`ghr_` + 76; S142 line 169, S143 line 72) and `gitlab-jwt-token` (the `glcbt-`/`glsat-`/`gliamat-` three-segment `eyJ` forms; S140 lines 429/446/463). After: selftest 101 → 115 cases, K1–K6 pass at the landing.

## Work performed

- **C1 · tranche 10 label set and counts.** `gen-c1.py` derives all sixteen rows from the base revision and refuses any `old` that is not unique; the map carries four `cell-repair`, five `part` and seven `range` rows (`.ufo/waves/round-95/c1/repair-map.tsv`, sha256 `8545eba2…beb6`; labels `cf739497…79d0`).
- **C1 · counter.** `.ufo/waves/round-95/c1/knowledge-meter.py` (sha256 `c0799f4c…8db8`) adds a `part` kind (two disjoint substring edits on one cell, so both keys on a line map without destroying each other's anchor), a snapshot-target check that resolves the capture at the after revision, and a `corpus/knowledge/`-prefixed key form; EXCLUDED is empty.
- **C1 · controls executed before the freeze.** `.ufo/waves/round-95/controls/c1-controls-r95.py` → `c1-controls-r95.txt`: candidate PASS; do-nothing rc 1; partial-row-dropped, extra-unlisted-edit, wrong-new, m5-out-of-range, snapshot-missing, unlabelled-row, part-as-cell, cell-repair-lane-root, two-cells-one-line and wrong-map-sha each rc 1; missing-labels rc 2; `union-applied` PASS against the round-93 counter's rc 1 + Traceback. Every fixture clones the pinned base commit.
- **C1 · post-landing reproduction (round-94 routed defect 1).** The same harness re-run on a clone of the landing prints `C1-CONTROLS-RESULT pass controls=15` (`.ufo/waves/round-95/l1/c1-controls-postlanding-r95.txt`); the round-94 fixture printed 11/12 in the same position.
- **C2 · candidate and gate.** `candidate-scanner.py` (sha256 `66edd661…6707`) adds `github-refresh-token` and `gitlab-jwt-token`; `.ufo/waves/round-95/c2/capability-check.py` (sha256 `9011e1b4…ddf6`) runs K1–K6; `candidate-row.txt` is the SCORECARD row that lands byte-equal; `candidate-allow-row.txt` is the digest-bound allowlist row for the one published `ghr_` placeholder the new shape finds in a round-94 receipt (`.ufo/waves/round-94/w1/ScoutGitLabRules-receipts/06-github-firstparty-examples.txt`, matched bytes 80, sha256 `c7ad99a1…060d`).
- **C2 · controls executed before the freeze.** `.ufo/waves/round-95/controls/c2-controls-r95.txt`: the round-94 instrument at the same revision fails K1 (`cases=101`), K3 (`hits=0` for the six plants) and K5 (row text); the candidate passes K1–K6 at seed 4242.
- **Sources · S142 opened and captured, S143 correction row.** `corpus/source-snapshots/round-95/S142.txt` (GitHub Docs, Refreshing user access tokens; 7,944 bytes; line 169 states the `ghr_` prefix); S143 records GitLab's `ghr_[0-9a-zA-Z]{76}` (line 72 of `github.toml` at 59ada1f4) as a correction row superseding S141's rejected record. Registry **141 → 143**; census `kasegi ok` rc 0.
- **Knowledge entry, criteria and lesson.** `corpus/knowledge/github-refresh-tokens-and-gitlab-jwt-tokens.md` admitted with the three–column QUALITY rows R148 (frozen control fields copied from the executed receipt) and R149 (fixtures clone a pinned revision) and the `corpus/lessons/round-95.md` lesson (Gate, three mined mistakes).
- **Wave w1 (13 seats, one v1 wave; `.ufo/waves/round-95/w1.ready` taken at 14:11 -03; results handoff `.ufo/waves/round-95/w1-results.json`, 13/13 seats, 0 dead).** Attack seats: CriticClaimsC1, CriticClaimsC2, CriticHarm, ReviewC1Sites, ReviewC2Scanner, MutC1Counter, MutC2Counter, SentinelShapes (8/13 = 61.5 %); plus ExecC1Indep, ExecC2Probe, ScoutSources, ConnectorOverlap, ScribeGate. Dead seats: none — 13/13 seats landed reports; MutC1Counter parked after writing four receipts and landed its compiled report on an L1 nudge (18/18 manifest mutants run, no new mutants). Per-seat verdicts: CriticClaimsC1 STANDS on P1–P3 (limbs re-derived from a fresh clone); CriticClaimsC2 STANDS at seeds 77031/913457/20261107; CriticHarm NO HARM on its four checks (three routed, none re-scoring); ReviewC1Sites 14/16 CORRECT, 2 PARTIAL (lines 88 and 90; round-96 labels written), 0 WRONG; ReviewC2Scanner claim STANDS, REQUEST-CHANGES on one documentation defect; MutC1Counter 8 killed / 10 survived of 18 mutants, all survivors routed; MutC2Counter 8/9 killed, F6 survives when the digest pin is absent; SentinelShapes STANDS, 0 MUST-FIX, eight routed; ExecC1Indep AGREE (independent meter 1007/1998 → 1008/1994, exact 14-line set); ExecC2Probe PASS; ScoutSources AGREE on all three anchors, six routed; ConnectorOverlap no sibling overlap and no `considerthese/` proposal touching either claim; ScribeGate 14 entry defects (3 high) and 5 lesson defects, all fixed at integration by adopting its corrected files.

## Landed changes

| Change | LOG.md entry | Commit |
|---|---|---|
| C1 freeze: claims, counter, labels, map, generator, apply helper, controls harness and receipt, wave spec | Round 95 freeze bullet | `347519f2` |
| C2 freeze: candidate scanner, capability gate, candidate row, allowlist row, S142 capture | Round 95 freeze bullet | `347519f2` |
| C1 landing: 16 edits in `triage-thresholds.md` and `iso-29147-divergence-and-clause-crosswalk.md` | Round 95 “C1 landing `53ec479d`” | `53ec479d` |
| C2 landing: `capture-secret-scan.py`, `capture-secret-allow.tsv`, `SCORECARD.md` (capability row) | Round 95 “C2 landing `38e7319f`” | `38e7319f` |
| Wave evidence: spec, dispatch, ready handoff, landing receipt | Round 95 “Wave w1” | `d050e286` |
| Integration: knowledge entry, SOURCES rows and change log, QUALITY R148/R149, lesson, SCORECARD/LOG entries, post-landing controls | Round 95 “Integration” | `43cc15e8` |
| Wave findings integration | Round 95 “Wave findings” | `01ff9865` |

## Before → after measurements

- **C1** — counting command `python3 -B .ufo/waves/round-95/c1/knowledge-meter.py --lane . --base-rev 9ef0126cc60b7f62baafd04f3e52c45e2a8e2f10 --after-rev 53ec479d71d25cf5be052db794a548a5904564b8 --map .ufo/waves/round-95/c1/repair-map.tsv --labels-rev 347519f21524d2bc13eb6c91cf3550930a4265b3 --base-target 1007/1998 --target 1008/1994 --map-sha256 8545eba2c39a1fed66b5d6eba59de973c182208aa8b06d28013417821359beb6 --work <scratch>`, measured against `53ec479d`. Before: `KNOWLEDGE-METER base=1007/1998`, M10 EXCLUDED 10, 396/436 unmapped, post-landing controls 11/12 (round 94). After: `KNOWLEDGE-METER base=1007/1998 after=1008/1994`, M3/M4/M5/M9 pass, `M10 labelled=16 want=16 mapped=16 kinds=cell-repair=4,part=5,range=7 unknown=none unapplied=none`, `KNOWLEDGE-METER-RESULT pass rc=0`, and the pinned-fixture control set `pass controls=15` at the landing (`.ufo/waves/round-95/l1/landing-r95.txt`, `…/l1/c1-controls-postlanding-r95.txt`).
- **C2** — counting command `python3 -B .ufo/waves/round-95/c2/capability-check.py --lane . --rev 38e7319f44a9fab2978b59ffd43faf207cf62b32 --work <scratch> --instrument-sha256 66edd66143ec62f6e40c864817a97383916d7ff67e5ab384e130b65c44516707 --gate-sha256 8b6f849349157a91dd7a2a3998c1f3956e8fed2dbd565c40815660cbd71cc8e6`, measured against `38e7319f`. Before (the round-94 instrument at the same revision): `SELFTEST-RESULT pass cases=101`, `K3 hits=0` for the six plants, K5 row names neither shape → `CAPABILITY-CHECK-RESULT fail rc=1`. After: `cases=115`, `K3 hits=6 missing=none extra=none`, `K5 rows=1 last=87`, `K1–K6 ok`, `CAPABILITY-CHECK-RESULT pass rc=0` (`.ufo/waves/round-95/l1/landing-r95.txt`; controls `…/controls/c2-controls-r95.txt`).
- **No-axis-harm guard** — `git diff --stat 9ef0126c <tip> -- SKILL.md` is empty; `depth:density` stays 273.2 (the report re-runs `corpus/instruments/density.py` with `--label r95`).

## Sources & frontier

- `SOURCES.md` rows before → after: **141 → 143**, counted by `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` (141 at base, 143 at tip). Census command `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kasegi`: **exit 2 at round start is not applicable** (the registry existed) — the round-start run printed `kasegi ok` rc 0 with six inherited W04 warnings; the round-end run prints `kasegi ok` rc 0 with the same six plus the S141/S143 supersession duplicate.
- Rows added by tier: **A: 1 (S142)**, **B: 1 (S143)**, C: 0.
- Rows touched old → new: S142 (new row) → `mined`, used-by `—` → `corpus/instruments/capture-secret-scan.py, corpus/knowledge/github-refresh-tokens-and-gitlab-jwt-tokens.md`; S143 (new correction row) → `mined`, same used-by; S141 stays `rejected` (superseded, its `teaches` record preserved); S140 stays `mined`.
- Frontier rows advanced: none — the two entries land on the credential-shape coverage ground the lane already holds (the `capture-secret-scan` capability), not on a new frontier row; the round says so instead of claiming frontier growth.
- `Assimilation: none` — the staged `merge/kasegi/` ids collide with the lane registry by construction and package adoption waits for a later round (unchanged from round 94).

## Trend verdicts

- **expansion: improved** — registry 141 → 143 with both rows opened this round and `mined`; a first-party source (S142) and a tier-B length rule (S143) enter, and the capability row gains two provider classes. Basis named for the operator: this is registry + capability expansion, not a new `knowledge/` entry on uncovered ground, and the report does not claim the entry-admission form.
- **quality: improved** — eleven deferred rows close with byte-exact edits (M3/M4/M5/M9 pass), five bare capture citations become resolvable paths, the counter's control set reproduces 15/15 after the landing (11/12 was the round-94 state), and QUALITY R148/R149 enter from the two mined process mistakes; no admitted entry failed its re-check.
- **discernment: improved** — the round turns the round-94 spot-check's two high defects into executed controls and quality criteria, files its own three mistakes, and puts every claim's substance in front of the wave's independent seats; the wave's independent seats re-derived both claims (CriticClaimsC1/C2, ExecC1Indep, ExecC2Probe, SentinelShapes) and its reviewers found the two PARTIALs, the stale-instrument docstring and two gate survivors that self-attestation would have missed; ScribeGate's 14 entry defects were accepted and fixed rather than argued.

## SHONEN

- [~] Box 1 — `SKILL.md` decision tables, error patterns, checklists and cited sources: the checklist's standing pointer `corpus/lessons/round-47-verifier-spotcheck.md` (line 94) covers boxes 1, 3 and 4; this round touched no `SKILL.md` byte (`git diff --stat 9ef0126c <tip> -- SKILL.md` empty).
- [~] Box 2 — end-to-end domain task logged: `corpus/practice/curl-h1-1913733/report.md` (round 85) and `corpus/practice/curl-ibb-h1-1997312/report.md` (round 86), both logged in LOG.md; no new practice package this round.
- [~] Box 3 — instructions executable without oral context: `corpus/lessons/round-47-verifier-spotcheck.md` finding; this round adds the claims' commands to `claims.json` and the landing receipts, which a reader can re-run.
- [~] Box 4 — no cross-domain bleed: `PROVINCE.md` unchanged; the round's two sources are credential-format documents inside the lane's province.

## Round shape, seats and hygiene

- Shape: **ONE v1 wave of 13 seats** under `ufo-wave-policy.json` (band 8–16), verified by `node ~/Projects/ufo-fsd-alpha/scripts/ufo-swarm-wave.mjs run --spec .ufo/waves/round-95/w1-spec.json` → `counts.spawn=13 resume=0 total=13`, rc 0. Role mix: 3 critics, 2 reviewers, 2 mutation-testers, 1 sentinel (8/13 attack), 2 executors, 1 scout, 1 connector, 1 scribe. No residual call. Round total 13 seats.
- Planner mapping: the L1 holds the canonical planner seat; the planning data-walk rides ScoutSources (bounded source re-derivation), per the run-15 ruling.
- Dead seats: none (13/13 reported; MutC1Counter landed on an L1 nudge, no replacement).
- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
- Tool installs: none (no upgrade was needed; pacman stayed paused).
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows only `.scratch/*` (orchestrator-owned) and four fleet-root files that name no kasegi/95 path and predate or name other work (`f.txt`, `trail-ids.txt`, `host-list-final.txt`, `dropped-volatile.txt`) — none written by this lane's seats, so none was copied or deleted.
- Open L0: none added this round.

## Erratum (appended after filing; names the text it supersedes)

Filed bytes above are not rewritten. This erratum supersedes: (a) the report's placement of the
scanner docstring defect in “routed to round 96”, (b) the report's “lane tip” hash line, and (c) any
reading of the frozen C2 statement's source line numbers as the regex grammar lines.

1. **Scanner docstring fixed (was routed, now landed).** `corpus/instruments/capture-secret-scan.py`
   now documents `github-refresh-token` and `gitlab-jwt-token` in its “Shapes.” block and no longer
   lists the GitLab JWT forms under “Known limits”; landed in lane commit
   `4ee3455d4944ecef128035c0608c80f4a3884cfc` (new sha256 `3006991a0f479b13fc6e4d1fbc70a9153bd9d336544f8ab009b6eeac6772adfc`).
   The C2 claim's P2 pin remains measured at the C2 landing `38e7319f` (sha `66edd661…`), which is
   unchanged; the doc fix is behaviour-neutral: `capability-check.py --rev 88bc4127` with the new instrument sha prints K1–K6 ok
   (`SELFTEST-RESULT pass cases=115`, `hits=0 allowed=27`), receipt `.ufo/waves/round-95/l1/docfix-r95.txt`.
2. **Frozen C2 statement wording (not reworded).** The frozen statement cites `S140 lines 429, 446,
   463` for the JWT grammar and `S141 line 72` for the 76-character length. Lines 429/446/463 are the
   `keywords` lines; the grammars are on 430/447/464 (the landed docstring and the knowledge entry
   cite both sets). The 76-character length's landed ground is `S143` (correction row superseding
   S141's record, status `mined`, used-by `corpus/instruments/capture-secret-scan.py, corpus/knowledge/github-refresh-tokens-and-gitlab-jwt-tokens.md`);
   S141 stays `rejected`. The frozen claim text is corrected in round 96, never retroactively.
3. **Round-95 capture manifest.** `corpus/source-snapshots/round-95/manifest.json` now exists
   (S142, 7,944 bytes, sha256 `727ba6a0…`, quote anchored at line 169). `capture-binding-check.py`
   prints `MANIFEST round-95 records=1 url_bound=1 fetched=1 archival=0` and `missing_manifest=0`;
   its only remaining FAIL is the pre-existing `rejected-row-anchor S138` (also present at base
   `9ef0126`).
4. **Receipt hygiene (scanner hit on wave evidence).** The corrected docstring made `capture-secret-scan.py --rev` report one hit on a seat receipt:
   `.ufo/waves/round-95/w1/CriticClaimsC2-receipts/03-allow-rows.txt:21` carries the S139 allowlist
   row whose shape cell and digest the `bearer` pattern matches (`bearer<TAB><64 hex>`, 71 bytes,
   sha256 `a75e16b9…87af`). It is not a credential; a digest-bound allowlist row admits exactly those
   bytes (`corpus/instruments/capture-secret-allow.tsv`, lane commit `88bc4127`), and the scanner at
   the tip prints `scanned=2744 hits=0 allowed=27 unused_allow=0 rc=0`.
5. **Lane tip after the erratum work.** `fdaaaf36f1d08dcb209fd45f8c1130009076f909` (pushed;
   `git ls-remote origin refs/heads/master` prints it). Every earlier hash in this report exists and
   is an ancestor of it.
