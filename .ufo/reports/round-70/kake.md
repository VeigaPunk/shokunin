# kake — round 70 (hyaku run 15, attempt 1, 2026-11-03)

Lane repo: `/home/vgpnk/Projects/shokunin/kake-shokunin` (jj-colocated; branch `master`).
Base `e5f6fd9e4c243d092160bc74e8bea24256087173` → final lane tip `2c1a700d12c245b6cde82b251deaf1f8953bf241`
(`git ls-remote origin refs/heads/master` prints it; `jj-lane.sh state` local=remote, ahead=0 behind=0).
No earlier attempt: `.ufo/watchdog.log` has no `lane-dead-no-report kake round=70` line; the working
copy was clean at round open; nothing inherited.

## Work performed

Declared claims (2, distinct axes, causally separable — ConnOverlap's read-set proofs: the C1
counter prints byte-identical output with `corpus/` deleted from a clone, and the census script
contains zero references to SCORECARD/QUALITY/lessons):

- **C1 — calibration (2 → 2, HOLD):** every path-like evidence pointer in `SCORECARD.md` resolves
  at the measured revision or carries a dated calibration annotation. Lowest owned non-retired
  axis (calibration 2; the stagnation nudge does not apply).
- **C2 — freshness (10 → 10, HOLD):** one staged `merge/kake` entry
  (`crux-bigquery-origin-membership.md`, theme: key-free CrUX eligibility routes) adopted into
  `corpus/knowledge/`, re-grounded in-round against a live source opened 2026-11-03.

Work items, each with evidence:

- Frozen contract committed before any seat ran: `.ufo/waves/round-70/contract.md` → `908b20b0`;
  Amendment 0 (pre-dispatch seat shape: the validator refused `labrat` — `unknown_role` — so the
  census probe rides an executor seat and a sentinel joins the attack set) → `d76ae926`;
  Amendment 1 (term refinements after the W1 attacks, before any after-state:
  `.ufo/waves/round-70/amendment-1-note.md`).
- W1 dispatched through the inline spawn handoff: `.ufo/waves/round-70/w1.ready` taken at
  16:34:31 (`w1.ready.dispatched`), 14 seats spawned in tranches, **WAVE-DONE received** with
  `.ufo/waves/round-70/w1-results.json` (14 results, no error fields, no dead seats).
- C1 counter v2 `.ufo/waves/round-70/c70_pointer_audit.py` (selftest 8/8, `controls/selftest-v2.txt`;
  list-form git calls only — SentinelAdoption verified no shell path, hostile-token fixtures created
  nothing); base do-nothing control red (`controls/c1-base-v2.txt`, `unannotated=17` exit 1; the v1
  counter's pre-amendment base receipt `w1/ExecC1Counter/base-run.txt` recorded 19 and is kept as
  history).
- Pointer population enumerated at base: 348 tokens (333 repo / 6 home / 9 tmp), 17 dangling
  (`w1/ScoutPointers/pointers-inventory.json`; independently re-derived by ReviewerPredicates and
  ScribeAdmin).
- `SCORECARD.md` `## Pointer calibration (round 70)`: 17 exact-token rows + one host-independence
  row (`/tmp/kake-r16`), each naming its dated event (W7 prune 2026-10-12 / round-18 sweep
  2026-10-14, W6 consolidation 2026-09-29, 2026-11-01 host migration, scratch-discipline cleanup,
  fleet-root location) — per RevengerTmp's per-round table; append-only against base (counter
  conjunct).
- Assimilation machinery proven before any append: collision guard able-to-fail on an indented-row
  fixture (`w1/ExecMirror/fixture-positive.log`, collisions=1) with a negative control
  (collisions=0); real collision run `reg-ids`=175 / `staged-ids`=129 / `collisions`=8
  (S312 S329 S367 S372 S373 S374 S390 S409 — none adopted; staged S352 does not collide);
  next unused id S438 (explicit scan); normalization red/green — verbatim staged row → census
  E01+E11 exit 1, prose-recheck row → E09 exit 1, normalized row → exit 0
  (`w1/ExecMirror/measure.txt`, `w1/ExecCensusProbe.md`); full-tree mirror census exit 0 before the
  append (corpus-only mirrors false-fail E11 — recorded as a `--file` path-resolution limit).
- Source re-opened with one GET: `w1/ScoutSources/sources/S438-crux-bigquery.html` (HTTP 200,
  110,697 B, sha256 `dd17ea8c…db420`, receipt.json; SentinelAdoption re-derived sha and byte count
  independently; canonical and og:url attributes equal the entry's source URL).
- Adopted entry `corpus/knowledge/crux-bigquery-origin-membership.md` (provenance trio, raw-substring
  blockquotes per the round-55 brand-new-entry bar, cross-reference declaring the delta over the
  held r28 entry, explicit not-run scope note); registry row S438 appended inside `## Registry`
  (NF=13, no escaped pipe, status mined, opened 2026-11-03, recheck `180d`, used-by the entry).
- Round lesson `corpus/lessons/round-70.md` (Mistakes M1–M3, Gate with 4 admits / 3 rejects,
  sourced claims, measurements, residuals); `corpus/QUALITY.md` Round-70 addendum (one criterion,
  able-to-fail commands); `corpus/README.md` coverage-map + frontier-ground-map rows; `LOG.md`
  round-70 entry; `SCORECARD.md` round-70 section.
- L1 tip attacks (scratch clones): removing one calibration row → exit 1; rewriting a base line
  with every row present → `append_only=false` exit 1 (`controls/tip-attacks.txt`).
- Misroot sweep before the report: `git -C /home/vgpnk/Projects/shokunin status --porcelain` shows
  only `.scratch/` run-state files (orchestrator-owned, never a misroot) — no seat wrote into the
  fleet root.

## Landed changes

Every change is tied to the `LOG.md` round-70 entry and one of these lane commits (all pushed;
`landed` lines from `jj-lane.sh`, remote-verified):

| Commit | Carries |
|---|---|
| `908b20b00f7479a61596e93e05104d1cd0054349` | frozen contract (predicates before data) |
| `d76ae92656bc24bc935d28201267a5d8b293de5a` | W1 spec (14 seats) + Amendment 0 |
| `50ec14460d348415aad9abc11c805a0792ba01a7` | counter v2, calibration section (17 rows), adopted entry, S438 row, lesson, QUALITY addendum, README rows, W1 seat evidence, dispatch/ready files |
| `3b54a02070b90391186a3e6dd8eafef2538648a5` | LOG round-70 entry with the measured tip + tip-attack receipts + census-after |
| `51a24ab3fed27e3b043ad5b8f4b0d207ef2ede27` | WAVE-DONE evidence (results.json, final ConnOverlap revision, host-independence calibration row) |
| `2c1a700d12c245b6cde82b251deaf1f8953bf241` | final-tip counter receipt (`controls/c1-tip-final.txt`) |

## Before → after measurements

- **C1 (calibration).** Command:
  `python3 -B .ufo/waves/round-70/c70_pointer_audit.py --root . --revision <rev> --base e5f6fd9e4c243d092160bc74e8bea24256087173`
  - Before, base `e5f6fd9e` (`controls/c1-base-v2.txt`): `pointers=348 dangling=17 annotated=0 unannotated=17 met=false`, exit 1.
  - After, final tip `2c1a700d` (`controls/c1-tip-final.txt`): `pointers=351 dangling=17 annotated=17 unannotated=0 append_only=true met=true`, exit 0.
  - Kill rule: base green would have made C1 unprovable — base is red; the two L1 tip attacks
    (row removed; base line rewritten) both exit 1.
- **C2 (freshness).** Commands and outputs (`controls/c2-after.txt`):
  - Before, base: `test -f corpus/knowledge/crux-bigquery-origin-membership.md` fails;
    `grep -c '^| S438 ' corpus/SOURCES.md` = 0.
  - After, tip `50ec1446`/`2c1a700d`: entry exists, opens with `source: S438 —
    https://developer.chrome.com/docs/crux/bigquery …`, `verified-at: 2026-11-03`, `recheck: 180d`;
    row count 1, NF=13, status mined, opened 2026-11-03, used-by the entry; mandated quote class
    collapsed-only (raw grep 0, collapsed count 1, method stated — three independent derivations);
    receipt sha256/bytes re-derive from the retained file; canonical/og:url = the source URL;
    `sources-census.sh validate --root /home/vgpnk/Projects/shokunin kake` exit 0.

## Sources & frontier

- Census before (round start) and after (round end), both exit 0 with the same 16 W04
  duplicate-url warnings (S033, S088, S092, S098, S099, S102, S110, S111, S115, S116, S117, S127,
  S416, S417, S427, S433), `kake ok`
  (`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kake`;
  after-receipt `controls/census-after-r70.txt`).
- Registry rows 175 → 176. Counting command: `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`.
- Rows added by tier: 1 × tier A docs (S438, Chrome for Developers: CrUX on BigQuery, opened
  2026-11-03, status mined, recheck `180d`, used-by `corpus/knowledge/crux-bigquery-origin-membership.md`).
- Rows touched old→new: none (no status/recheck/used-by cell of an existing row changed).
- Frontier rows advanced: the key-free CrUX origin-membership ground entered the coverage map and
  the frontier ground map (`corpus/README.md` rows "Key-free CrUX origin membership (r70)" and
  "Field performance — key-free CrUX origin membership | r70"); the area stays Frontier (knowledge
  without a gate).
- **Assimilation:** one theme (key-free CrUX eligibility routes) from `merge/kake/`; one entry
  admitted (`crux-bigquery-origin-membership.md`, id S438 renumbered from staged S352 by the
  next-unused rule — the staged id is unused in the lane registry; the measured collision set of
  the staged file is S312 S329 S367 S372 S373 S374 S390 S409, all already adopted, none
  re-appended); one entry rejected (`crux-keyless-check.md`, reasons + flip in the round-70 lesson
  §Gate). The absent-defect-register slice is untouched (kake r58 L0 question stays open). The
  round-70 lesson's Gate records the stripped staged recheck prose and this round's re-derivation
  (the staged raw grep prints 0 today; the recorded "1" was a collapsed-text count).
- **considerthese:** newest file `2026-10-26.md`; proposal 4 (gate-agreement ledger) is the one
  still-unimplemented proposal — it stays refused per its recorded flips (r62: "repeated
  verifier/gate comparisons show a durable need"; r67: verifier-side data, not lane-ownable);
  no new mining without new evidence (ConnOverlap checks: no implementing artifact at base).

## Trend verdicts

- **expansion: improved** — one admitted `knowledge/` entry on coverage-map ground the lane did
  not hold (no held row named BigQuery, `origin_summary`, or a key-free membership route —
  CriticAdoption §1: `grep -c bigquery` on the base registry = 0; ConnOverlap: the URL is new to
  every lane registry fleet-wide), citing the S438 row opened this round.
- **quality: improved** — 17 dangling SCORECARD evidence pointers annotated with dated events
  (before: 0 annotated); the counter is able-to-fail (selftest 8/8, red base, two killed tip
  attacks); the staged-row normalization class is proven red→green at the census gate; no admitted
  entry failed a re-check.
- **discernment: unchanged** — the lane-side gate sample (4 admits / 3 rejects, including
  rejecting the lane's own contract premise) is recorded in the round-70 lesson §Gate, but the
  improved condition needs the outside spot-check's agreement, which is owed to the hyaku closure
  and not claimed here.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md:57` (audit → source-fix → publish checklist), `SKILL.md:208` (owned freshness gate registry); author-asserted, no non-author verifier this round.
- [~] At least one end-to-end domain task executed and logged in LOG.md — the round-70 LOG entry (this round): the assimilation adoption executed end-to-end from staged bytes to a census-gated landed entry, with the C1 calibration instrument landed and measured.
- [ ] Instructions executable by an agent without oral context — residual procedure paths in `SKILL.md:95`, `SKILL.md:356`, `SKILL.md:359` and the corpus citation debt carried in `corpus/lessons/round-69.md` §Known residuals (routed to the next round).
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md:3` (domain line unchanged) and `PROVINCE.md:24` (the CrUX/field-performance frontier the adopted entry sits under); sibling scan found no contest (ConnOverlap §b).

## Round shape, seats, and mechanics

- **Shape:** ONE v1 wave (band 8–16, `scripts/hyaku/ufo-wave-policy.json`), 14 seats, round total
  14; no residual wave. Role mix: 3 scout, 3 executor, 2 scribe, 1 reviewer, 1 critic,
  1 mutation-tester, 1 connector, 1 revenger, 1 sentinel — attack share 4/14 ≈ 28.6 % (≥25 %),
  1 connector seat (≤2), roles span all three run-15 models via `task.agentModelOverrides`
  (never passed a model). No planner seat: the L1 holds the planner role (validator rejects it).
- **Dispatch:** spec validated (`run` refused the first 13-seat draft with `unknown_role` for
  labrat — fixed before any dispatch, recorded in Amendment 0); one `.ready` handoff, taken at
  16:34:31; seats filled in tranches; **WAVE-DONE** received after all 14 settled.
- **Dead seats: 0** (`w1-results.json`: 14 results, no error fields).
- **Seat findings folded in:** Amendment 1 (counter v2 terms, contract corrections); the
  host-independence calibration row (ConnOverlap's proposed move); the Gate's corrected reject
  reason and quote-class resolution (CriticAdoption, ScribeEntries).
- **Stale-lane:** none — this lane's only open mission is this round (respawn-per-round driver).
- **Tool installs:** none by the L1 or any seat; pacman untouched (host pause respected).
  SentinelAdoption ran `npx marked@12` (marked 12.0.2, official npm registry, read-only GFM table
  rendering, cached in `~/.npm/_npx/`, not a PATH install) — recorded per the tooling rule.
- **Scratch:** all seat trees under `/fast/scratch/hyaku/kake-r70/<Seat>/` removed on exit
  (ConnOverlap's dir outlived its report and was removed by the L1 at landing — the seat's own
  defect per the scratch rule, noted here); the L1's scratch removed; nothing left under
  `/fast/scratch/hyaku/kake-r70/` or `/tmp/kake-r70`.
- **Open L0 questions routed around, never treated as answered:** kake r69 (line 260,
  lowercase `~/projects` corpus citations / `--offline` red — C1 touches SCORECARD only, no pin,
  corpus file or scanned lesson line); kake r58 (register-slice adoption); kake r59 (calibration
  sub-axis ownership — the round continues the established practice; CJK quote-unit rule — not
  exercised, all quotes English).
- **Push scope:** only the lane remote and the fleet repo (this report); no domain source tree
  touched; no publish, deploy or DNS action; no live property probed this round.
