# kasegi — round 78 report (attempt 1)

Lane HEAD (landed, remote-verified): `c2f4119b13bd8afd2679521fd815a1a2356cbd39` (branch `master`; `ls-remote origin refs/heads/master` prints the same hash). Freeze commit `2d81fe84506b323fb32beb137d5bd21db6a5c13d`; base `0687cca8645884aba30c8eb5fa2d8ecaca7245cf`.

## Work performed

Declared claims (frozen at `2d81fe84`, `.ufo/waves/round-78/claims.json`):

- **C1 — depth:verifiability** (lowest non-retired axis, score 4): successor to the recheck-cwd census counter — refuse a missing/non-directory TMPDIR with exit 2, and make the named-kill set of eight mutants die by assertion. **Verdict: NOT VERIFIED** (the candidate kills 7 of 8; K-X2 survives under the frozen transform). Candidate not landed.
- **C2 — coverage** (score 8): admit Frontier F54 on S112 (the OSV.dev `POST /v1/querybatch` page), narrowed to seven batch-specific clauses (Q01, Q02, Q03, Q09, Q10, Q11, Q13). **Verdict: VERIFIED on B0–B7.**

Work items (evidence pointers):

- Round-start census: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kasegi` → exit 0, `ok …/corpus/SOURCES.md`, six inherited W04 duplicate-url warnings (S028, S029, S072, S076, S080, S085).
- Live re-open of S112 this round: `curl https://google.github.io/osv.dev/post-v1-querybatch/` → HTTP 200, 30406 bytes (2026-11-05). Seven frozen quotes present after tag-boundary whitespace normalization.
- Pre-freeze source-recheck: `.ufo/waves/round-78/controls/c2-prerecheck-r78.txt` (`S112:sha256 OK`, seven `anchor=<n>-ok`, rc 0); new manifest `corpus/source-snapshots/round-78/manifest.json` over byte-identical snapshot `S112.txt` (sha256 `f3ca0465…0907`).
- Do-nothing controls (committed in the freeze): `controls/c1-donothing-selftest-r78.txt` (base `cases=6 failures=0`, rc 0), `controls/c1-base-realtree-census-r78.txt` (`entries=91 … conformant`, rc 0), `controls/c1-base-missing-tmpdir-r78.txt` (nonexistent TMPDIR → `FileNotFoundError`, rc 1), `controls/c2-donothing-counters-r78.txt` (FRONTIER-CENSUS rows 53, knowledge 91, registry 112), `controls/c2-recheck-audit-base-r78.txt` (expected 91, exit 0).
- Wave `w1`: one v1 wave of 12 seats, plan validated (`w1-plan.out`, rc 0), dispatch `w1-dispatch.json` (spawn 12, resume 0), ready file `w1.ready` (dispatched), results `w1-results.json` (12 settled). Seat outputs under `.ufo/waves/round-78/w1/`.
- C1 build (`ExecC1Build`): candidate `w1/successor/recheck-cwd-census.py` (sha256 `f6849971…457db1`); selftest `cases=13 failures=0` rc 0; TMPDIR refusal rc 2 with `recheck-cwd: TMPDIR … is not a directory`, no traceback (`successor/tmpdir-refusal.out/.err`); real-tree census `entries=91 … conformant` rc 0. Kill table (`ExecC1Build.md`): K-M1..K-M5, K-X1, K-M8 rc 1; **K-X2 rc 0**.
- C1 attack: `ReviewC1` Finding 1 (BLOCKER) — K-X2 not killed by any check (P3 fails 7/8); `MutC1` reproduces the r77 reference survivors X1, X2, K-M8 (`cases=12 failures=0`) and proposes an assertion fix (`MutC1-proposals.patch`); `CriticClaims` — C1 "weak as frozen, one amendment from sound"; `SentinelC1` — provisional, no candidate verdict (its run preceded the candidate's existence).
- C2 build: `ExecC2Build` landing set in `w1/c2/` (SOURCES.md, knowledge-expected.txt, README.md, PROVINCE.md, bookkeeping.txt); `ExecC2Replay` independent re-measure (`ExecC2Replay.md`).
- C2 entry: `ScribeEntry` draft (`w1/c2/osv-post-batch-query-contract.md`, sha256 `78cd76ba…438d8`), reviewed byte-identical at landing by `ReviewC2` (`w1/ReviewC2.md`: no blocker; B0–B7 hold; B7 literal command needs the fleet conf, the explicit-dir form passes).
- C2 distinctness: `ScoutDistinct.md` §1 — Q01, Q03, Q11 NOVEL; Q02, Q09, Q10, Q13 PARTLY-HELD (the held part attributed to F31 / F51 and not re-taught); 0 HELD. Q12, Q07, Q08 excluded (F51-held); Q04, Q05, Q06 excluded (cross-references).
- C2 critic: `CriticClaims.md` — C2 "sound", with two hardening recommendations (an entry clause-set enforcement predicate; a threshold-qualifier note) routed to the successor (see Other report items).
- Adjacency: `ConnectorOverlap.md` — sibling-lane overlap scan for querybatch / S112.
- Lesson drafts from `ScribeLesson`; the L1 corrected the verdict header, the M77-3 status (not landed), the S112 row line, and the landing-hash references before landing (`corpus/lessons/round-78.md`).
- Lane landing: `scripts/hyaku/jj-lane.sh commit … --as kasegi` → `landed c2f4119b`.

## Landed changes

- **`c2f4119b`** (this round's landing, LOG.md `## Round 78`, SCORECARD.md `## Round 78`):
  - `corpus/knowledge/osv-post-batch-query-contract.md` — new F54 entry (seven clauses only; "Not claimed" line for Q04–Q08, Q12).
  - `corpus/SOURCES.md:124` — S112 `queued` → `mined`; `used-by` `—` → the entry path. One row changed.
  - `corpus/instruments/knowledge-expected.txt` — one line added (93 → 94 lines; 91 → 92 `.md` rows).
  - `corpus/README.md` — Frontier F54 row; `PROVINCE.md` — F54 admitted line.
  - `corpus/lessons/round-78.md`, `SCORECARD.md`, `LOG.md`, and `.ufo/waves/round-78/` (claims, mutant table, controls, wave receipts, seat outputs).
- **`2d81fe84`** (freeze, before any scoring): `.ufo/waves/round-78/claims.json`, `c1-mutant-transforms.md`, `controls/`, `corpus/source-snapshots/round-78/` (manifest, S112.txt).
- **Not landed:** the C1 candidate (`.ufo/waves/round-78/w1/successor/recheck-cwd-census.py`, sha `f6849971…`). The lane's `corpus/instruments/recheck-cwd-census.py` stays at base sha `e666ae11…` (verified in ExecC1Build and ReviewC1).

## Before → after measurements

**C1 (NOT VERIFIED; score 4 → 4).** Counting command over each mutant (`TMPDIR=<scratch> python3 -B <mutant>.py --selftest`), killed = rc ≠ 0 with a FAIL line:

- Before (base / r77 reference, `.ufo/waves/round-77/c1-amended-reference.py`): named kills 5 of 8 (K-X1, K-X2, K-M8 survive); nonexistent TMPDIR → rc 1 traceback (`controls/c1-base-missing-tmpdir-r78.txt`).
- After (candidate `f6849971…`, not landed): named kills 7 of 8 (K-X2 rc 0); nonexistent TMPDIR → rc 2 with `recheck-cwd: TMPDIR …`; selftest `cases=13 failures=0`.
- Measured against the candidate built at the round-78 tip (`ExecC1Build.md`), not against a landed commit.

**C2 (VERIFIED; coverage 8 held).** Counting command: `python3 corpus/instruments/frontier-recheck-count.py ; ls corpus/knowledge/*.md | wc -l ; grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`.

- Before (base `0687cca8`): FRONTIER-CENSUS `rows=53 admitted=53`; knowledge 91; registry 112 (S112 queued).
- After (landed `c2f4119b`): FRONTIER-CENSUS `rows=54 admitted=54 closed=54 problem-rows=0 registry=112`, `FRONTIER-PASS F54 ids=S112`, rc 0; knowledge 92; registry 112 (S112 mined).
- Other landed-tree checks (rc 0): `source-recheck.py … --source S112` (seven anchored OK); `capture-binding-check.py` (`records=92 bound=92 unbound=0`); `recheck-cwd-census.py` (`entries=92 … exit0_foreign=70 … conformant`); `recheck-audit.py` (`expected=92 missing=0 unexpected=0 exit=0`); `sources-census.sh validate --root … kasegi` → exit 0 (six inherited W04 only).

## Sources & frontier

- **SOURCES.md rows before → after:** 112 → 112 (counting command `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`, exit 0 at both).
- **Rows added by tier:** none (no new source row this round).
- **Rows touched old → new:** S112 status `queued` → `mined`; used-by `—` → `corpus/knowledge/osv-post-batch-query-contract.md`. Logged in `corpus/lessons/round-78.md` § Sources.
- **Sources opened this round (frontier step):** S112 re-opened live 2026-11-05 (HTTP 200). The round's sourced claim (C2) rests on this row.
- **Frontier rows advanced:** F54 admitted (one entry; seven of thirteen pinned clauses; four not claimed with reasons).
- **Rejections:** the six non-claimed clauses (Q04–Q08, Q12) are recorded with reasons in the entry's "Not claimed" line and in the lesson.
- **Census (round start / end):** `sources-census.sh validate --root /home/vgpnk/Projects/shokunin kasegi` → exit 0 / exit 0 (six W04, unchanged).
- **Assimilation:** none (the staged `merge/kasegi` package collides on 82 of 112 registry ids; `S112` TC260 collides with this lane's S112; L0 pending; nothing adopted).
- **considerthese:** none touched. The 2026-10-26 items are either fleet-process (quiescence gate, wave-evidence cap, cadence) or already mined (the ledger covers items 1, 2, 5, 7).
- **Quarantine:** no absent-defect register row touched; none appended.
- **Mistake mined:** M77-3 (census crashes on a nonexistent TMPDIR; class environment-assumption; captured-by none). Fix built and shown able to fail (base rc 1 traceback vs candidate rc 2), **not landed**; M77-3 stays open as a routed defect for the successor round (`corpus/lessons/round-78.md` § Mistakes).

## Trend verdicts

- **expansion: improved.** Knowledge 91 → 92; F54 on uncovered ground (three novel clauses Q01, Q03, Q11; four partly-held clauses whose held part is attributed to F31 / F51 and not re-taught).
- **quality: unchanged.** No instrument moved (the C1 candidate is not landed); no admitted entry superseded or re-verified.
- **discernment: unchanged.** C1 was refused honestly on its own kill rule; the critic and reviewer objections are routed rather than papered over.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — pointer: `corpus/knowledge/osv-post-batch-query-contract.md` (new F54 entry, S112 quotes at `S112.txt:24,166,168,169,195`).
- [ ] At least one end-to-end domain task executed and logged in LOG.md — not touched this round.
- [~] Instructions executable by an agent without oral context — pointer: `.ufo/waves/round-78/controls/` (runnable do-nothing and counting commands with their outputs).
- [~] No cross-domain bleed (PROVINCE.md still accurate) — pointer: `PROVINCE.md` F54 line; `.ufo/waves/round-78/w1/ConnectorOverlap.md`.

## Other report items

- **Stale-lane:** respawn-per-round driver; no other mission of this lane is open.
- **Tooling installs:** none this round.
- **Seats:** 12 spawned, 12 settled (WAVE-DONE received); no dead seats. Round total 12 (no residual call). Attack seats 5 of 12 (reviewer ×2, critic, mutation-tester, sentinel). Connector seats 1. `SentinelC1` settled without a candidate verdict (its run preceded the candidate's existence); the candidate's security review is provisional and the candidate is not landed.
- **Inherited state:** none. The round launched on attempt 1 (`watchdog.log` 10:47:08); no `lane-dead-no-report` line for round 78.
- **Misroot sweep:** `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows only other lanes' files (`.scratch/run15-state.json`, `.ufo/closure-kaidoku-r92.json`); no seat-written misroot.
- **L0:** no new question appended. Open items routed around, not answered: staged `S112` / TC260 id collision (R-77-E, nothing adopted); source-recheck anchor-window semantics (R-77-D; the round-78 manifest uses exact lines); round-72 api_key narrowing; round-76 Q01 option A/B.
- **Routed defects and carry-forward for round 79:**
  - C1 K-X2 class: a successor must add an independent assertion on the case-6 limb (the `gate-consume` body is otherwise unkilled) before freezing; the r77 kill set (X1, X2, K-M8) is the required class. The transform table as frozen was not satisfiable against the candidate's structure (the K-X2 anchor text differs).
  - C2 hardening (critic): an entry clause-set enforcement predicate, and a threshold-qualifier note for Q10/Q11 (the `Q12` qualifier) — both out of this round's frozen predicate.
  - C2 B7 command: the literal `--root /home/vgpnk/Projects/shokunin kasegi` form needs the fleet conf; the explicit-dir form passes. The successor should freeze the explicit-dir form.
  - The four partly-held clauses are a judgment call under B6's paraphrase half; the literal half (0/7 quote hits) holds. Recorded so an outside reviewer can overturn it.
  - Endpoints R-77-F: three of four still open (one endpoint per round).
- **Frontier note:** `corpus/instruments/capture-binding-check` reports `orphan=S040-live.txt` in its audit output (pre-existing, not from this round).
