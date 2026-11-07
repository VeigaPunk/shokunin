# kasegi — round 96 report

Lane: kasegi. Round 96, attempt 1. Driver: `2026-11-07T15:01:16-03:00 launch kasegi round=96 pgid=4033329 driver=hyaku-inline attempt=1`.
Lane repo `/home/vgpnk/Projects/shokunin/kasegi-shokunin`; base `d8a2bb0a2bdc2f6337ea2f849a1a557297067ad6`;
freeze `804e7bc344df0808c880815dde077c28be5db18a`; C1 landing `3c0581e2616df7a10af494a785b479d5e5293749`;
C2 landing `7ef1d365eb523a83b2567342a6c0f585ab028ab0`.

**Declared claims (2, frozen before data in `.ufo/waves/round-96/claims.json`).**

- **C1 — `depth:verifiability`** (lowest non-retired axis, score 4): tranche 11 lands the five round-95 non-author labels — `SKILL.md:182-184` → `SKILL.md:182-185` on `triage-thresholds.md:88` and inside `SKILL.md:182-184,255-257` on `:90`; the last bare `S041.txt:1680-1681` becomes its committed capture path at `iso-29147-divergence-and-clause-crosswalk.md:13`; the two prose pointers on `:36` narrow `(L1832-1834)` → `(L1832-1833)` and the e) pointer `(L1835)` → `(L1834)`. The round-96 counter adds the prose-pointer `part` binding in M4 (the edited substring is exactly the key and only its `(L...)` numbers change), so the two prose rows are bound rather than refused. The control set ships eleven attributing fixtures: each negative fixture's failing-limb set equals the set declared in the harness, which the round-95 mutation campaign could not do (10 of 18 mutants survived because no negative fixture isolated its rule). After: meter **1030/2027 → 1032/2028**, 12 controls and 11 attribution fixtures pass at the landing.
- **C2 — `coverage`** (score 8 held; capability extension of `capture-secret-scan`): seven GitLab shapes S140 publishes and the round-95 scanner could not express — the routable and versioned-routable forms of `glpat-` (S140 lines 30, 51), `glrt-`/`glrtr-` (136), `gldt-` (324), `glagent-` (358) and `glwt-` (375), plus `gitlab-pipeline-trigger-token` (`glptt-` exactly 20 or exactly 40, line 73). After: selftest **115 → 128** cases, K1–K6 pass at the landing.

## Work performed

- **C1 · freeze.** `claims.json` with both predicates, kill rules and do-nothing controls; the round-96 counter (sha256 `fadd0ede…`) = the round-95 counter plus the prose-pointer M4 branch and its docstring clause; the five-row map (`7d9bb49f…`) generated from the frozen label set by `.ufo/waves/round-96/c1/gen-c1.py` (each `old` must occur exactly once on its base line, each `new` must be absent); the control harness (`d47328ae…`) with 12 controls and per-fixture declared FAIL sets. Evidence: `.ufo/waves/round-96/claims.json`, `.ufo/waves/round-96/c1/`, commit `804e7bc3`.
- **C1 · controls executed before the freeze.** `.ufo/waves/round-96/controls/c1-controls-r96.txt`: candidate rc 0; do-nothing rc 1 on `M1,M3`; `missing-labels` rc 2; `wrong-map-sha` `M6`; `extra-unlisted-edit` `M3`; `r95-no-prose-branch` `M4,M5`; `row-old-absent-only` `M3`; `map-not-label` `M9`; `snapshot-missing-only` `M4,M5`; `unknown-kind-row` `M10`; `unlabelled-only` `M9,M10`; `unapplied-only` `M10`; `ATTRIBUTION pass fixtures=11`, `C1-CONTROLS-RESULT pass controls=12`.
- **C1 · landing.** Five edits on four lines in two files, applied from the map (not hand-typed): `corpus/knowledge/triage-thresholds.md` and `corpus/knowledge/iso-29147-divergence-and-clause-crosswalk.md`. Meter at the landing `1030/2027 → 1032/2028`, M0–M10 pass (`.ufo/waves/round-96/l1/c1-landing-r96.txt`). Commit `3c0581e2`; `git diff-tree` names exactly those two paths.
- **C1 · post-landing reproduction (R149).** The same harness re-run on a clone of the landing prints 12/12 and `ATTRIBUTION pass fixtures=11` (`.ufo/waves/round-96/l1/c1-controls-postlanding-r96.txt`).
- **C2 · freeze.** `.ufo/waves/round-96/c2/candidate-scanner.py` (sha256 `71876619…`) adds seven shapes to `GITLAB_PATTERNS` plus their docstring entries; the docstring's known-limits list drops the six families this round detects and names the ones that remain; 13 selftest cases added (7 positives, 6 boundary negatives). `.ufo/waves/round-96/c2/capability-check.py` (K1–K6) and `candidate-row.txt` (the SCORECARD row that lands byte-equal).
- **C2 · landing.** `corpus/instruments/capture-secret-scan.py` and the `capture-secret-scan` SCORECARD row. K1–K6 pass at `7ef1d365` at seeds 4242 and 20261107 (`.ufo/waves/round-96/l1/c2-landing-r96.txt`): K1 `cases=128`, K2 `scanned=2744 hits=0 allowed=27 unused_allow=0`, K3 `hits=7 missing=none extra=none`, K4 `base_new_shape_hits=0 old_shapes_missing=none`, K5 `rows=1 last=87 named=True`, K6 `aws-sts-session-token` still reported on the round-86 freeze. Commit `7ef1d365`.
- **Sources · S144 admitted and mined, S145 rejected.** `corpus/source-snapshots/round-96/S144.txt` (GitLab Docs Security — Tokens; HTTP 200; 17,591 bytes / 419 lines; sha256 `d6e52927…`) captured with the lane's own `capture-source.py` (intake gate, hits=0) and bound by `corpus/source-snapshots/round-96/manifest.json` (sha256, bytes, lines, quote anchors). S145 (GitLab Docs REST API authentication) opened, read and rejected: no prefix or length. S140 re-opened from its committed capture for the seven rules (the live raw URL answered 403 this round). Registry **143 → 145**; census `kasegi ok` rc 0.
- **Knowledge entry, criteria and lesson.** `corpus/knowledge/gitlab-routable-and-versioned-token-forms.md` admitted (7 in-range citation instances, 0 bad; `anchorcheck.py`); QUALITY R150/R151/R152; `corpus/lessons/round-96.md` with the Gate and six mined mistakes.
- **Wave w1 (13 seats, one v1 wave; `.ufo/waves/round-96/w1.ready` taken at 15:20:02 -03; results handoff `.ufo/waves/round-96/w1-results.json`).** Attack seats: CriticClaimsC1, CriticClaimsC2, CriticHarm, ReviewC1Sites, ReviewC2Scanner, MutC1Counter, MutC2Counter, SentinelShapes (8/13 = 61.5 %); plus ExecC1Indep, ExecC2Probe, ScoutSources, ConnectorOverlap, ScribeGate. All 13 seats settled, 0 dead; per-seat verdicts are in the wave-findings section below.

## Landed changes

| Change | LOG.md entry | Commit |
|---|---|---|
| C1 freeze: claims, counter, map, labels, generator, control harness and executed receipt | Round 96 freeze bullet | `804e7bc3` |
| C2 freeze: candidate scanner, capability gate, candidate row | Round 96 freeze bullet | `804e7bc3` |
| C1 landing: five edits in `triage-thresholds.md` and `iso-29147-divergence-and-clause-crosswalk.md` | Round 96 “C1 landing `3c0581e2`” | `3c0581e2` |
| C2 landing: `capture-secret-scan.py`, `SCORECARD.md` capability row | Round 96 “C2 landing `7ef1d365`” | `7ef1d365` |
| Landing receipts and post-landing controls | Round 96 “Controls after the landing” | `b7f59c60` |
| Integration: knowledge entry, SOURCES rows and change log, QUALITY R150–R152, lesson, SCORECARD section, LOG entry | Round 96 “Integration” | `b7f59c60` |

## Before → after measurements

- **C1** — counting command `python3 -B .ufo/waves/round-96/c1/knowledge-meter.py --lane . --base-rev d8a2bb0a2bdc2f6337ea2f849a1a557297067ad6 --after-rev 3c0581e2616df7a10af494a785b479d5e5293749 --map .ufo/waves/round-96/c1/repair-map.tsv --labels-rev 804e7bc344df0808c880815dde077c28be5db18a --base-target 1030/2027 --target 1032/2028 --map-sha256 7d9bb49f366a594df3cd13e5651a6db4aabef1ab4b5a7081d89fd5f8c68b1d0f --work <scratch>`, measured against `3c0581e2`. Before: `KNOWLEDGE-METER rev=d8a2bb0a rate=1030/2027`; the five labels unapplied; the round-95 control set's negatives multi-defect (r95 mutation campaign: 8 killed, 10 survived). After: `base=1030/2027 after=1032/2028`, `M3 bad_lines=0 old_not_once=0 dup_rows=0`, `M4 bad=none`, `M5 out_of_range=none`, `M9 rows=5 unbound=none`, `M10 labelled=5 want=5 mapped=5 kinds=part=4,range=1 unknown=none`, `M6` the frozen map sha, `KNOWLEDGE-METER-RESULT pass rc=0`; controls 12/12 and `ATTRIBUTION pass fixtures=11` at the landing.
- **C2** — counting command `python3 -B .ufo/waves/round-96/c2/capability-check.py --lane . --rev 7ef1d365eb523a83b2567342a6c0f585ab028ab0 --work <scratch> --instrument-sha256 71876619a62875049a5526a03806aa740e3ead122aacdc1499fe153be3048ac9 --gate-sha256 8b6f849349157a91dd7a2a3998c1f3956e8fed2dbd565c40815660cbd71cc8e6`, measured against `7ef1d365`. Before (the round-95 instrument at the same revision): `cases=115`, K4 `base_new_shape_hits=0` for the seven plants → `CAPABILITY-CHECK-RESULT fail rc=1`. After: `cases=128`, `K3 hits=7 missing=none extra=none`, K1–K6 ok, `CAPABILITY-CHECK-RESULT pass rc=0` at seeds 4242 and 20261107.
- **No-axis-harm guard** — `git diff --stat d8a2bb0a <tip> -- SKILL.md` is empty; `depth:density` stays 273.2 (`python3 corpus/instruments/density.py SKILL.md --label r96`).

## Sources & frontier

- `SOURCES.md` rows before → after: **143 → 145**, counted by `grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' corpus/SOURCES.md` (143 at base, 145 in the working tree). Census command `bash scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kasegi`: round start printed `kasegi ok` rc 0 with six inherited W04 warnings; round end prints `kasegi ok` rc 0 with the same six plus the S143/S141 supersession duplicate (seven W04 total).
- Rows added by tier: **A: 1 (S144)**, **B: 1 (S145, rejected)**, C: 0.
- Rows touched old → new: S144 (new row) → `mined`, used-by `—` → `corpus/instruments/capture-secret-scan.py, corpus/knowledge/gitlab-routable-and-versioned-token-forms.md`; S145 (new row) → `rejected`, used-by `—`; S140 re-opened from its capture (live raw URL 403), status `mined` and used-by unchanged.
- Frontier rows advanced: none — the round lands on the credential-shape coverage ground the lane already holds (the `capture-secret-scan` capability), not on a new frontier row; the report says so instead of claiming frontier growth.
- `Assimilation: none` — the staged `merge/kasegi/` ids collide with the lane registry by construction and package adoption waits for a later round (unchanged from rounds 94–95).

## Trend verdicts

- **expansion: improved** — registry 143 → 145 with S144 opened this round and `mined`; a first-party prefix statement enters (S144) beside the machine-readable rules file (S140), and the capability row gains seven shapes. Basis named for the operator: this is registry + capability expansion, not a new `knowledge/` entry on uncovered frontier ground, and the report does not claim the entry-admission form.
- **quality: improved** — five deferred citation rows close with byte-exact edits (M3/M4/M5/M9 pass); the control set now attributes every negative fixture to a declared limb set (the round-95 state was 10 of 18 mutants alive); the scanner's docstring stops listing six families it now detects; QUALITY R150–R152 enter from the three mined fixture defects; no admitted entry failed its re-check (`anchorcheck.py` 0 bad on the new entry).
- **discernment: improved** — six mistakes are mined from this round's own work, three of them caught by the harness's attribution check before the freeze (a harness crash, a malformed label row, a duplicate (site, key) pair); the round also re-measured its own base instead of carrying the previous round's meter reading (M96-6), and the wave's independent seats re-derived both claims (see wave findings).

## SHONEN

- [~] Box 1 — `SKILL.md` decision tables, error patterns, checklists and cited sources: the standing pointer `corpus/lessons/round-47-verifier-spotcheck.md` (line 94) covers boxes 1, 3 and 4; this round touched no `SKILL.md` byte (`git diff --stat d8a2bb0a <tip> -- SKILL.md` empty).
- [~] Box 2 — end-to-end domain task logged: `corpus/practice/curl-h1-1913733/report.md` (round 85) and `corpus/practice/curl-ibb-h1-1997312/report.md` (round 86), both logged in LOG.md; no new practice package this round.
- [~] Box 3 — instructions executable without oral context: the claims' commands, the frozen pins and the landing receipts are committed; a reader can re-run `claims.json`'s `command` fields.
- [~] Box 4 — no cross-domain bleed: `PROVINCE.md` unchanged; the round's two sources are credential-format documents inside the lane's province.

## Round shape, seats and hygiene

- Shape: **ONE v1 wave of 13 seats** under `ufo-wave-policy.json` (band 8–16), verified by `node ~/Projects/ufo-fsd-alpha/scripts/ufo-swarm-wave.mjs run --spec .ufo/waves/round-96/w1-spec.json` → `counts.spawn=13 resume=0 total=13`, rc 0; results handoff `.ufo/waves/round-96/w1-results.json` (13 seats, 0 dead). Role mix: 3 critics, 2 reviewers, 2 mutation-testers, 1 sentinel (8/13 attack = 61.5 %), 2 executors, 1 scout, 1 connector, 1 scribe. No residual call. Round total 13 seats.
- Planner mapping: the L1 holds the canonical planner seat; the planning data-walk rides ScoutSources (bounded source re-derivation), per the run-15 ruling.
- Stale-lane: respawn-per-round driver; no other mission of this lane is open.
- Tool installs: none (no upgrade was needed; pacman stayed paused).
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows only `.scratch/*` (orchestrator-owned) and four fleet-root files that name no kasegi/96 path (`f.txt`, `trail-ids.txt`, `host-list-final.txt`, `dropped-volatile.txt`, all predating this round) — none written by this lane's seats, so none was copied or deleted.
- Open L0: none added this round.

## Wave findings (13-seat v1 wave, round-96 w1)

All 13 seats settled; 0 dead (`.ufo/waves/round-96/w1-results.json`, `seats: 13`). Verdicts, all re-derived by non-author seats from the frozen revs:

- **C1** — CriticClaimsC1: **STANDS on P1–P4** at `3c0581e` (M0 `1030/2027`, M1 `1032/2028`, M3/M4/M5/M9/M10 as frozen, M6 the map sha, `after_rev=3c0581e…`; controls 12/12 and `ATTRIBUTION pass fixtures=11`; the landing diff names exactly the two knowledge files). ExecC1Indep: **AGREE** on all three items — an independent census reproduces 1030/2027 → 1032/2028 (numerator +2 via two INTERNAL additions, denominator +1 via one GONE removal, no class flips), the frozen map applied to a `git archive` extract is byte-identical to the landing, and the diff is five edits on four lines. ReviewC1Sites: **5/5 CORRECT, 0 PARTIAL, 0 WRONG**; the round-97 label set is empty (`ReviewC1Sites-receipts/round97-labels.tsv`).
- **C2** — CriticClaimsC2: **STANDS** at three seeds of its own (K1–K6 re-derived; the seven shapes checked against S140). ExecC2Probe: **STANDS** — 21 S140-derived positives (bare / JSON / escape-terminator) hit exactly their shape, 21 boundary negatives produce no hit, and the round-95 instrument misses all 22 positives. ReviewC2Scanner: **APPROVE** with four routed findings. SentinelShapes: **C2 STANDS**, 0 MUST-FIX, 7 routed findings (highest: an encoded `.` in a routable/versioned tail is undetected and undocumented).
- **Harm** — CriticHarm: **NO HARM** on all four checks (density guard and governance files; citation tokens byte-unchanged and resolution; the C2 scanner cannot mask an earlier shape; allowlist unchanged and the `--rev` run clean).
- **Mutation** — MutC1Counter: the C1 predicate **STANDS** re-derived at the landed revs; the ten round-95 survivors were rebuilt as single-point edits and **6 are killed, 4 survive** — killed: s02 and s08 by `map-not-label`, s04 by `snapshot-missing-only`, s07 by `unapplied-only`, s06 and s09 by `unlabelled-only` (the last two are *attribution-only* kills: the rc stays 1 and the limb set shrinks, which is exactly what the attribution limb is for). Survivors: m06 (no cell-repair fixture shipped), s01 (the `row-old-absent-only` fixture's old `(L1819)` does occur on base line 36, so it fails via `bad_lines`, not `old_not_once`), s03 (equivalent clause) and s05 (the unknown-kind pair is also unapplied, so M10 still fails). MutC2Counter: 8 of 14 single-point scanner mutants killed behaviourally, **6 survive** (routable tail widened to `{1,2}`; the versioned right boundary; the deploy-token prefix — hit/no-hit equivalent; the versioned head floor 26; the `glpat-versioned` left boundary; and the prefix-drop equivalent).
- **Sources** — ScoutSources: both claims re-derived (C1 and C2 counters re-run at their landings); S140 live-verified (HTTP 200, 20,228 bytes, sha256 `14854f71…` = the round-94 manifest's raw digest); the S144 page re-fetched and confirmed as the row this round already holds (so no second prefix page was admitted); one reject candidate proposed with four reasons.
- **Drafts** — ScribeGate: three drafts complete (Gate, Mistakes, knowledge entry) and seven routed findings F1–F7 against the landed integration; F1 (the runner versioned prefix statement) and F7 (the plain `glagent-` 50-character limit) were repaired in `6299582b`, F2/F3/F4 (census cwd, 20-word quote, capture line count 418) likewise, F5 (no machine receipt for the two pre-freeze repairs) is answered by `.ufo/waves/round-96/controls/c1-prefreeze-defects-r96.txt`, and F6 (the S140 403 claim) by `.ufo/waves/round-96/l1/s140-live-fetch-r96.txt` plus the seat's 200 receipt.
- **Scope** — ConnectorOverlap: **STANDS**; all 20 sibling repos scanned, none holds a citation meter, the GitLab routable shapes or limb-attribution fixtures; no `considerthese/` proposal touches either claim; no sibling cites S140; the shapes stay in kasegi's province (capture hygiene), not kagi's.

Routed to round 97 (no claim re-scored):

1. MutC1Counter m06: ship a `cell-two-values` must-accept fixture (the counter accepts a cell row with two values; no fixture proves it).
2. MutC1Counter s01: the old-absent fixture must use a pointer that does not occur on the line (a genuine absent-old probe kills the mutant).
3. MutC1Counter s05: an unknown-kind label whose pair is not also unapplied, so M10's `unknown` limb is the only failure.
4. MutC2Counter survivors: plants for a 26-character versioned head, a token preceded by a letter (left boundary), a routable tail `{1,2}` widening and the versioned right boundary; the deploy-token prefix is hit/no-hit equivalent and should be documented, not planted.
5. SentinelShapes R1: an encoded `.` in a routable/versioned tail is undetected and undocumented; R2 (escape terminators whose last byte is alphanumeric) carried from round 93.
6. ReviewC2Scanner F1–F4: the runner versioned shape omits the published instance prefix (behaviour-equivalent, span differs); the docstring's known-limits rewrite drops the plain `glagent-` 50-character form (a one-line repair blocked this round by the instrument pin); the `/trigger/pipeline` limit wording; boundary negatives exist only for `glpat-` and `glptt-`.
7. ExecC1Indep observation 1: the pre-freeze controls receipt names scratch revs (`freeze=179deaaa…`, `candidate=f60c11a3…`) that do not resolve in the repo; the post-landing receipt names the real freeze and landing.
8. ScribeGate F5: the two pre-freeze fixture repairs have an L1 observation record, not a machine receipt.

## Erratum (appended after filing; names the text it supersedes)

Filed bytes above are not rewritten. This erratum adds the hashes the filed text leaves implicit.

1. **Wave-findings commit and final lane tip.** The wave evidence, seat reports and receipts,
   the SCORECARD qualifiers, the lesson's M96-7 and wave-findings section, the LOG wave bullet and
   the S140 live-verification correction landed at `e2f4f94a4f6a50b73048d34d0ffbc8d8e2ba0432`,
   which is the final lane tip: `git -C kasegi-shokunin ls-remote origin refs/heads/master` prints
   `e2f4f94a…`, `jj-lane.sh state` prints `local=e2f4f94a remote=e2f4f94a ahead=0 behind=0
   tracked=0 untracked=0`.
2. **Two post-landing controls receipts, one committed.** The harness wrote
   `.ufo/waves/round-96/l1/c1-controls-r96.txt` on its post-landing run (12 controls, `ATTRIBUTION
   pass fixtures=11`) and the same run's console log was copied to
   `.ufo/waves/round-96/l1/c1-controls-postlanding-r96.txt`; the two are verdict-identical (the
   harness copy adds the scratch `work=` path). Only the log copy is committed; the duplicate was
   removed so the lane worktree stays clean.
3. **S140 live verification.** The filed Sources section says the L1's `/-/raw/` fetch answered 403;
   the wave's ScoutSources re-fetched the same pinned URL and got HTTP 200 with sha256
   `14854f71…` equal to the round-94 manifest, so the source is live-verified this round (the
   lesson and the SOURCES change log carry the correction; the 403 receipt carries an appended
   note).
