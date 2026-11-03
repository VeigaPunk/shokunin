# kake — round 73

## Work performed

The round declared three claims, frozen in `.ufo/waves/round-73/contract.md` at freeze `4c7c53bc563a66ae0676b468966781f023ae0110` (predicates, base controls and the attack corpus committed before any seat ran; pre-freeze diagnosis disclosed in the contract):

- **C1 calibration** (lowest owned axis, score 2, HOLD) — the round-72 bookkeeping cites two receipt files that were never committed (`controls/c1-tip.txt`, `controls/c2-tip.txt` in the LOG.md round-72 entry and the SCORECARD round-72 rows); land append-only corrections and a counter whose grammar sees the wave-relative pointers the round-70 counter cannot (its repo class whitelists only `.ufo|corpus|scripts|handoffs|considerthese` prefixes and it reads SCORECARD.md only — a wave-relative `controls/…` token is never extracted at all).
- **C2 operability** (score 10, HOLD) — a new counter `.ufo/waves/round-73/c73_tmp_v3.py` closes the routed round-72 holes: the `${TMPDIR:-/tmp}` fallback repoint (H1), command verbs outside the frozen 17-word list (H2), a symlinked SKILL.md (H3), and pins the absence phrase against truncation mutants (H4); plus the SKILL.md gate-registry row for it. Sourced on S440 (GNU Bash manual, Shell Parameter Expansion, opened this round).
- **C3 freshness** (score 10, HOLD) — re-pin the one sidecar entry whose `lineSha256` the round-71 S132 used-by edit (`84dcc841`) invalidated, so `scripts/freshness-sweep.mjs --offline` evaluates again at the tip. Evaluable with named drift, not clean.

Work items, each with evidence:

- Freeze commit `4c7c53bc` (lane, via `jj-lane.sh`): contract, attack corpus, base controls (`controls/c0-gate-status-base-c66.txt`, `c1-pointer-base-c70.txt`, `c2-c72-base.txt`, `c3-sweep-base.txt`), S440 source retention (`sources/bash-param.html` sha256 `6b0800fd35c7f9fa8bb66d0eae1cd2e8bae7ded09ad6e89460dda2775a13c8e3`, `receipts.txt`, fetched 2026-11-03T22:33:40Z). CriticClaims verified the working tree byte-identical to the freeze for all seven frozen artifacts (`.ufo/waves/round-73/w1/CriticClaims.md`, "Freeze topology": 7/7 IDENTICAL).
- Wave `w1` (one v1 wave, 11 seats, band 8–16; roles scout 2, executor 3, reviewer 2, scribe 1, critic 1, mutation-tester 1, connector 1; attack share 3/11 = 27 % ≥ 25 % on the run-15 seat list, 4/11 = 36 % counting sentinel per the round-70 SCORECARD convention; the L1 held the planner role): spec `w1-spec.json`, dispatch `w1-dispatch.json`, plan `w1-plan.json`, results `w1-results.json` — 11 seats, all settled, none dead. Dispatched via the inline handoff (`w1.ready` written 19:36, `w1.ready.dispatched` 19:37:13; seats filled in tranches as fleet slots freed).
- Seat deliverables integrated: `c73_tmp_v3.py` (sha256 `9b4d2cd0…b5027`, selftest 41/41) and `c73_wave_pointers.py` (sha256 `37025eff…02e6b`, selftest 6/6) promoted from `w1/` to `.ufo/waves/round-73/`; the S440 row (ScribeRow draft, exact page title from the retained bytes); the LOG.md round-73 entry with the `[r73-correction 2026-11-03]` bullet; the SCORECARD round-73 section plus `## Correction (appended, round 73) — round-72 pointers`; the one-field sidecar re-pin; the SKILL.md `### Round 73 gate registry additions` section appended after line 1396 (past the highest SKILL.md sidecar pin, 935 — a line-213 insertion was measured disruptive by ConnOverlap O2: 22 of 25 pins break, sweep exit 2).
- Landed changes: see below.

## Landed changes

All tied to the LOG.md round-73 entry. Lane commits: round work `c2482e5ce56d589ecd5ddefb0ec8bf1e0c4fde92`, receipts `7f4cdc86b074076e97fe5a9e6ebbc8b569c01364` (both pushed; `git ls-remote origin refs/heads/master` shows `7f4cdc86…`).

- `corpus/knowledge/freshness-sidecar.json` — one entry's `lineSha256` (`b3315f41…` → `4e408131…`), C3. The diff at the tip is exactly that one line (verified over `git diff c1f3d8d4 c2482e5c -- <path>`).
- `SKILL.md` — the round-73 gate-registry section (8 appended lines, one row naming `c73_tmp_v3.py`), C2.
- `corpus/SOURCES.md` — the S440 row appended after S439 (registry 177 → 178 rows), C2's sourced-claim ground and the frontier step.
- `LOG.md` — the round-73 entry including the append-only correction bullet naming both superseded tokens and the resolving `-final` receipts, C1.
- `SCORECARD.md` — the round-73 measured-claims section plus the correction block, C1. Scores unchanged (no score cell edited; diff = 14 appended lines).
- `.ufo/waves/round-73/{contract.md, attack-corpus.txt, controls/ (17 receipts), sources/, w1-spec.json, w1-plan.json, w1-dispatch.json, w1-results.json, w1/ (13 seat files incl. both counter sources and the held-out corpus), c73_tmp_v3.py, c73_wave_pointers.py}` — wave evidence and instruments.
- `corpus/lessons/round-73.md` — the round lesson (Mistakes M1–M3, Gate with 3 admits / 3 rejects, the sourced claim).

Inherited state resolved: the two untracked round-71 dispatcher markers (`.ufo/waves/round-71/w1.ready{,.dispatched}`) named by the round-72 report are committed under this round's entry as historical wave evidence. No other uncommitted lane-authored work was inherited.

## Before → after measurements

- **C1 (calibration)** — counting command `python3 -B .ufo/waves/round-73/c73_wave_pointers.py --root <lane> --revision <rev>` (receipts `controls/c1-base-lane.txt`, `controls/c1-tip-lane.txt`, measured in the landed lane):
  - Before, base `c1f3d8d4`: `C1v1 … pointers=9 dead=2 annotated=0 unannotated=2 append_only=true met=false`, exit 1.
  - After, landed tip `c2482e5c`: `C1v1 … pointers=9 dead=2 annotated=2 unannotated=0 append_only=true met=true`, exit 0.
  - Do-nothing control: the round-70 counter exits 0 at base over the same dead tokens (`controls/c1-pointer-base-c70.txt`) and stays exit 0 at the tip (`controls/c70-tip-lane.txt`) — the blindness is real and no harm landed.
- **C2 (operability)** — counting commands `python3 -B .ufo/waves/round-73/c73_tmp_v3.py --selftest` and `… --corpus .ufo/waves/round-73/attack-corpus.txt [--lane <lane> --revision <rev>]` (receipts `controls/c2-selftest-lane.txt`, `c2-corpus-lane.txt`, `c2-base-lane.txt`, `c2-tip-lane.txt`):
  - Before: the frozen round-72 counter accepts `9/11` frozen attack lines (do-nothing control `controls/c2-c72-control-corpus.txt`; wave-1 MutC2 independently measured 9/11 with a fidelity-checked copy; CriticClaims re-derived the same k=9 and the not-void condition).
  - After: `C2v3 … attack_accepted=0/11 legit_rejected=0/4 selftest=41/41 findings=[] met=True`, exit 0; base `c1f3d8d4` and the landed tip both `findings=[]` exit 0. The frozen round-72 counter stays green at the tip (`controls/c72-tip-lane.txt`).
  - MutC2's corpus blind spots (brace-branch/imperative/phrase mutant survivors) are covered outside the corpus: c73 detects the no-slash brace default directly (required by the frozen corpus's own H1 expectations) and pins the phrase with two selftest truncation cases; its three held-out lines are recorded for a future corpus amendment.
- **C3 (freshness)** — counting command `node scripts/freshness-sweep.mjs --offline` (receipts `controls/c3-sweep-tip-lane.txt`, `c3-selftest-lane.txt`; before-state `controls/c3-sweep-base.txt`):
  - Before, base `c1f3d8d4`: exit 2, `freshness-sweep: Error: paths sidecar binding invalid: corpus/SOURCES.md:140`.
  - After, landed tip: exit 1, stderr clean of `Error:` lines, `VERDICT: DRIFT — §paths: 1 unannotated miss · 1 NOT in pins.pathsMissSet (exit 1, partial: offline)`; `--selftest` `36/36 passed` (isolated `HOME`/`KAKE_SELFTEST_DIR`).
  - Honest reading (ReviewerC1C3 F4/F5, CriticClaims §C3): *evaluable with named drift*, not clean — the named finding is the lowercase `~/projects` citation class already tracked by the open L0 kake|round-69 line, and the re-pinned entry's own absence note is contradicted on this host (M3, routed).

## Sources & frontier

- Census: before — `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kake` exit 0 (`ok`, 177 rows; W04 duplicate-URL warnings pre-existing, warnings allowed). After — same command, exit 0, `ok`, 178 rows.
- Rows before→after: 177 → 178. Rows added by tier: one tier-A `docs` row (S440, GNU Bash manual — Shell Parameter Expansion, opened 2026-11-03, retained bytes `sources/bash-param.html` with a located 9-word quote on line 117 of the line-aligned tag-stripped text). Rows touched old→new: none (no status/recheck/used-by cell changed). Frontier rows advanced: none (S440 backs a claim instrument; no new knowledge entry, no coverage-map move).
- The lesson's `## Gate` records the S440 URL, access date and located quote, and 3 admits + 3 rejects with reasons.
- Assimilation: none. No `merge/kake/` theme was taken (the three frozen claims and the routed-repair scope filled the round; the one candidate theme, `held-url-liveness-2026-10.md`, is recorded in the lesson as a candidate for the next round) and no `considerthese/` proposal was implemented.

## Trend verdicts

- **expansion: unchanged** — no admitted knowledge entry on new coverage-map ground; one curated source row (S440, mined, cited by C2); frontier map unchanged. Evidence: the SOURCES diff (one row), no `corpus/knowledge/` addition.
- **quality: improved** — three instruments repaired or added with able-to-fail evidence: the C1 counter is red at base and green at tip over the same two files; the C2 counter demonstrably rejects 11 corpus attacks its predecessor accepts 9 of (fidelity-checked control); the freshness gate went could-not-evaluate → evaluated with the sidecar delta pinned to one field. No admitted entry failed a re-check (none was due); no gate was weakened to go green — the sweep's exit-1 drift is reported, not suppressed, and CriticClaims verified the re-pin keeps every other sidecar check evaluated.
- **discernment: improved locally** — the round's Gate records 3 admits and 3 substantive rejects with reasons, including rejecting a "clean" freshness reading the lane had every incentive to claim; wave-1 attack seats falsified two draft narratives before landing (the c70 blindness mechanism; the H4 hole shape, which is a mutant-survival class, not a live hole — contract sentence corrected in the lesson). The independent non-author spot-check is owed to the hyaku closure, as recorded in the lesson.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — the gate registry (now including the round-73 row) and S440; `.ufo/waves/round-73/w1/ExecRegistryRow.md` re-derived the table's 8-cell grammar and non-disruptive placement.
- [~] At least one end-to-end domain task executed and logged in LOG.md — the round-73 LOG entry with the three frozen claims measured end-to-end; receipts under `.ufo/waves/round-73/controls/` measured at the landed tip.
- [~] Instructions executable by an agent without oral context — the registry rows' entry/self-test command cells and `.ufo/waves/round-73/contract.md` re-derive every step; CriticClaims re-ran the full battery from committed bytes alone.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — PROVINCE.md untouched this round; the round's only web read was one public GET of the GNU Bash manual page; ConnOverlap found no sibling overlap requiring arbitration (`.ufo/waves/round-73/w1/ConnOverlap.md`).

## Stale-lane

kake's own mission: this round, landed and reported; no other mission of this lane is open (respawn-per-round driver). Age under two driver ticks.

## Tooling

No tool installed or upgraded by the L1 or any seat this round (pacman untouched, per the host-wide pause). Seats recorded the host toolchain versions they used (git 2.56.0, node v24.21.0, Python 3.14.x) and no installs.

## Round shape

One v1 wave `w1` of 11 seats (band 8–16), no residual call, round total 11. Roles: scout 2, executor 3, reviewer 2, scribe 1, critic 1, mutation-tester 1, connector 1; dead seats: none (11/11 settled in `w1-results.json`). Lane commits: freeze `4c7c53bc`, round work `c2482e5c`, receipts `7f4cdc86` (pushed; ls-remote shows the final hash). Report commit follows via `fleet-commit.sh`.
