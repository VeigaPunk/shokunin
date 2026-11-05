# kake — round 96 report (hyaku run 15, attempt 1)

Lane repo `/home/vgpnk/Projects/shokunin/kake-shokunin`; round base
`bde9869144f69c5a459c0d2c93f5135922fe3a8d`; final lane tip
`9177e65823ee29fd52c4d4c0b3105c18bc63ee9a` (pushed; `git ls-remote origin
refs/heads/master` prints it — pre-report gate PASS). Dispatch digest
(copied from `.ufo/watchdog.log`): `2026-11-05T14:27:28-03:00 launch kake
round=96 pgid=290456 driver=hyaku-inline attempt=1`; no
`lane-dead-no-report kake round=96` line exists — attempt 1 is the first
attempt and inherits nothing.

## Work performed

Two declared claims (1–3 cap), each an axis-move on a distinct owned axis,
plus the frontier step. Neither claim advances its axis score; both are
reported at their verdicts and left to the non-author closure.

- **C1 (calibration, HOLD 2, lowest owned axis): the routed R95-1/R95-5/
  R95-7-C1 instrument defects close.** The successor self-assessment
  counter `.ufo/waves/round-96/c96_selfassess.py` was authored and frozen
  BEFORE the wave (instruments commit `7ae3e9b0…`, freeze `049e8eca…`,
  digests pinned in `controls/instrument-sha256.txt`): knowledge entries
  pinned by presence (R95-1), the round-95 false-green shapes NG01/NG08/
  NG11 refused as class rules (R95-5), sys.path scrub extended to the
  working directory and every PYTHONPATH entry and the false `python3 -I`
  docstring sentence removed (R95-7 C1 items). Battery: 22 defect routes +
  the F2 canned wrapper = 23 refusals, 5 clean admissions, the F1e
  effectful-shadow route, and a predecessor differential that must admit
  all three NG routes (`ng_pred_admits=3/3` liveness). Evidence:
  `.ufo/waves/round-96/freeze.md`; selftest receipt
  `controls/ctl-c1-selftest.txt` (13/13 planted findings, battery 23/23,
  `--surfaces-file` refused); surfaces generated at the base by the
  committed read-only generator `gen-surfaces.py`
  (`frozen/c1-surfaces.json`, digest `c1caa585…`, pins lessons=90
  entries=83 rows=260 criteria=40).
- **C2 (freshness, HOLD 10, capability acquisition): the revalidation
  exchange over supplied values, contract v1.** The counter
  `.ufo/waves/round-96/c96_reval.py` (frozen `ec40aec1…`) scores the
  candidate `scripts/reval_exchange.py` over 37 hand cases, 120 seeded
  generated cases, 6 frozen forgeries, a frozen positive control and a
  14-mutant population; contract `.ufo/waves/round-96/reval-contract-v1.md`
  grounds every clause in RFC 9111 §4.3 (quotes at retained-body lines
  848, 852, 861, 935, 938, 944). Evidence: `controls/base-c2.txt`
  (`candidate=absent … met=false`, the do-nothing control),
  `controls/ctl-c2-selftest.txt` (7/7 fixtures, mutants 14/14,
  anti_table ok). **The claim lands unmet (honest stop):** the frozen
  counter crashes on every candidate-present scoring run —
  `NameError: name 'mutants' is not defined` at `c96_reval.py:624`
  (SentinelScope r08 with five candidate variants; CriticClaims C2-01 with
  a committed candidate in a scratch clone). Per the freeze's own rule the
  frozen bytes are not amended; the defect routes as R96-1. The candidate
  still lands and is independently verified: ReviewReval's fresh,
  non-overlapping 24-case grid agrees 24/24 with zero tool, contract or
  reference defects (`.ufo/waves/round-96/w1/ReviewReval/grid.md`,
  `receipt-nonoverlap.txt`); no Capabilities row enters (round-64
  precedent: no frozen-counter pass, no row).
- **Frontier step.** SOURCES row S480 opened and admitted (scout fetch of
  `https://www.rfc-editor.org/rfc/rfc9111.txt`, HTTP 200, 84 477 bytes,
  sha `aeb52adb…` byte-identical to the retained round-93 body, 6/6 clause
  quotes located — `w1/ScoutRFC/fetch.txt`); knowledge entry
  `corpus/knowledge/revalidation-exchange.md` admitted (provenance trio
  first, cites S480 + re-reads S456/S476, 13/13 quotes verified,
  `w1/ScribeEntry/quotes-verified.txt`); census before → after run and
  exit 0 at both ends; mistake mining below; C2 is the round's sourced
  claim (its contract, entry and row cite S480).
- **Wave shape: one v1 wave, 12 seats, ONE batched dispatch through the
  inline spawn handoff** (ready file `w1.ready`, taken 2026-11-05T15:16:55;
  spec `w1-spec.json`, dispatch `w1-dispatch.json`, results
  `w1-results.json`). Roles: scout 1 (ScoutRFC-3), executors 4 (ExecReval,
  ExecC1Guard, ExecRegistry-7, ExecReceipts-6), scribe 1 (ScribeEntry-28),
  reviewers 2 (ReviewC1-26, ReviewReval), critic 1 (CriticClaims-68),
  mutation-tester 1 (MutReval), sentinel 1 (SentinelScope-32), connector 1
  (ConnectorScope-22) — attack share 5/12 ≈ 42% (≥25%), connector 1 (≤2).
  The protocol §3 planner seat is held by the L1 (this round's data-walk
  rode ScoutRFC's source opening and ConnectorScope's sibling scan);
  the validator rejects `planner` as a swarm role and no planner seat was
  dispatched. **All 12 seats settled; no dead seats.** Residual calls:
  none. Routing never named a model; `task.agentModelOverrides` decided.
- **Routed items from round 95, each addressed:** R95-1/R95-5/R95-7-C1 →
  closed in C1's successor (receipted above); R95-2 → filed as the round's
  L0 question (fleet arbitration; kake adopts nothing silently;
  `w1/ConnectorScope/overlaps96.md`, verdict `CONNECTOR overlaps=12
  contested=8`, K43 re-verified at kumitate `0bff4bab`); R95-3 → the
  chousa round-79 criterion 146 citation landed inside QUALITY R96-A
  (cited at the sibling's current HEAD, never ported); R95-4 → the
  round-95 closure discharged it (spot-check §"R95-4 closure duty");
  R95-6 and R95-7's C2-side items → routed forward untouched (this round
  did not amend the conditional_eval line's frozen counter); R95-8 → the
  generated-input digestion is built into `c96_reval.py` from day one
  (and its bypass routes R96-2); the round-95 spot-check's new item 5 →
  this report uses the bare trend vocabulary with bounds in prose; item 6
  → the stale freeze.md digest instruction is superseded in the round
  lesson (filed bytes untouched; `w1/ExecReceipts/freeze-supersession.md`).
- **Attack evidence this round produced (routed to round 97):** ReviewC1
  `refused=8 false-greens=RX01,RX02,RX03b,RX09` (decision tokens in HTML
  comments, fenced code, whole-Gate fences; subdir round-number hijack);
  CriticClaims `routes=26 reached=14` — C1's laundering (absence
  annotation), vocabulary stuffing and `git replace` substitution routes,
  and C2's memorizing tables over raw-JSON keys, base64/half-hex/minified
  digests and positional seed-order tables (on a counterfactual probe
  copy, because the frozen counter crashes first); MutReval
  `frozen=14/14 new=12 newsurvivors=N05,N06,N07,N08,N11` (refusal
  coarseness); SentinelScope `refused=28 escaped=F1,F2,F3,F4` (the crash,
  git-from-PATH, unaudited kill/metadata vectors, no C2 effectful-shadow
  defense). All recorded in `corpus/lessons/round-96.md` §Routed.
- **Misroot sweep:** `git -C /home/vgpnk/Projects/shokunin status
  --porcelain` shows only `.scratch/run15-state.json` (orchestrator-owned
  run state — never a misroot) and the closure session's `MANIFEST.json`
  work (integrator-owned); no seat wrote at the fleet root; nothing copied
  or deleted.
- **Scratch:** L1 scratch `/fast/scratch/hyaku/kake-r96/` removed after
  landing; every seat prompt carried its own scratch root and the
  delete-before-yield duty (seat reports record their own hygiene).

## Landed changes

All lane changes are tied to a `LOG.md` entry (## Round 96) and landed by
`jj-lane.sh --as kake`; each hash below is the helper's `landed` line and
is an ancestor of the pushed tip `9177e658…`.

| Commit | Carries |
|---|---|
| `7ae3e9b07e2435f7fde6e73838d9fa14488b8dda` | C1 successor counter `c96_selfassess.py`, C2 counter `c96_reval.py`, contract v1, surfaces generator + frozen fixtures (`frozen/c1-surfaces.json`, `c2-population.sha256`, `pos-good-reval.py`, six `neg-*.py`, `mutants-reval.json`), pre-freeze controls (`base-c1-predecessor.txt`, `c1-successor-at-base.txt`, `base-c2.txt`, `ctl-c1-selftest.txt`, `ctl-c2-selftest.txt`, `instrument-sha256.txt`) |
| `049e8eca2f0fa5e981232eb4efe367357dce578c` | the claim freeze (predicates, counters, kill rules, targets — committed before any seat scored) |
| `7dc9bf43b6bd6ddae741f5b3af1d7e4224990428` | `scripts/reval_exchange.py` (the C2 candidate); SKILL.md gate-registry rows for both counters; `corpus/SOURCES.md` S480; `corpus/knowledge/revalidation-exchange.md`; `corpus/QUALITY.md` criterion R96-A (with the chousa criterion-146 citation, R95-3) |
| `05c19fd1246ceca7d2949bf8b57888ed72f76e1e` | `corpus/lessons/round-96.md` (Gate, Mistakes, Routed); `LOG.md` ## Round 96; `SCORECARD.md` round-96 section; wave evidence (`w1/`, spec, dispatch, results, ready files) |
| `1098dccd79e76f92a5772c17089e93b3de9c2c44` | the round lesson's Gate reject decisions (capability row and package adoption) — the E1 repair the final receipts demanded |
| `9177e65823ee29fd52c4d4c0b3105c18bc63ee9a` | landed-tip receipts (`controls/after-c1-successor.txt`, `controls/after-c1-predecessor.txt`, `controls/census-after.txt`) |

The L0 question line (`kake | round-96 | R95-2 fleet kill-predicate
arbitration owed …`) is appended to `.ufo/l0-questions.md` and lands with
this report's fleet commit.

## Before → after measurements

- **C1 — met on the frozen predicate.** Counting commands (frozen):
  `python3 -B .ufo/waves/round-96/c96_selfassess.py --root . --revision
  <REV> --work <scratch>` and the differential control
  `python3 -B .ufo/waves/round-95/c95_selfassess.py --root . --revision
  <REV> --work <scratch>`.
  - Before (do-nothing controls, base `bde9869144f69c5a459c0d2c93f5135922fe3a8d`,
    committed pre-freeze): successor `pins=ok mismatches=0 battery=23/23
    admit=5/5 shadow=absent predecessor_admits=6/22 ng_pred_admits=3/3
    met=true` exit 0 (`controls/c1-successor-at-base.txt` — the claimed
    instrument scoring itself); the lane's held instrument, the frozen
    predecessor, reads `pins=identity battery=20/20 met=false` exit 1
    (`controls/base-c1-predecessor.txt`, counter digest `8fd27d62…`).
  - After (landed tip `1098dccd79e76f92a5772c17089e93b3de9c2c44`, receipts
    at `9177e658…`): successor `lessons=91 entries=84 rows=262 criteria=40
    mismatches=0 E1=0 E2=0 E3=0 E4=0 E5=0 pins=ok battery=23/23 admit=5/5
    shadow=absent predecessor_admits=6/22 floor=4 ng_pred_admits=3/3
    self_pin=ok met=true` exit 0 (`controls/after-c1-successor.txt`);
    predecessor unchanged `pins=identity met=false` exit 1
    (`controls/after-c1-predecessor.txt`). Score stays 2; the instrument
    is falsified by the round's own attack seats (R96-3/R96-4) and the
    freeze's do-nothing wording defect is recorded (lesson Mistake 3) —
    the closure owns admission.
- **C2 — unmet (honest stop).** Counting command (frozen):
  `python3 -B .ufo/waves/round-96/c96_reval.py --root . --revision <REV>
  --work <scratch>`.
  - Before (base `bde9869144f69c5a459c0d2c93f5135922fe3a8d`):
    `candidate=absent hand=0/37 generated=0/120 forgeries_refused=0/6
    positive=refused mutants=0/14 survivors=none anti_table=ok
    population=ok seed=96 met=false` exit 1 (`controls/base-c2.txt`).
  - After (candidate landed at `7dc9bf43…`): **unscoreable by the frozen
    instrument** — every candidate-present run dies rc=1 with
    `NameError: name 'mutants' is not defined` (SentinelScope r08;
    CriticClaims C2-01). No after receipt is forged: the honest verdict is
    unmet, the fix routes R96-1, the candidate's independent verification
    is ReviewReval 24/24 (`w1/ReviewReval/grid.md`), and no Capabilities
    row enters. Score stays 10.

## Sources & frontier

- Counting command: `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'
  corpus/SOURCES.md` → **216 → 217**. Census
  `bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate
  --root /home/vgpnk/Projects/shokunin kake` → **exit 0 at the landed tip**
  (`controls/census-after.txt`), with the pre-existing W04 duplicate-URL
  warning class (40 lines) and no E-class findings. One mid-integration
  census run (taken after the S480 append but before the round lesson
  landed) exited 1 on `E11 S480 missing used-by
  corpus/lessons/round-96.md` — the E11 existence check firing ahead of
  the lesson commit; the final tip clears it, and the receipt records the
  final state.
- Rows added by tier: **A: 1 (S480, spec)**; B: 0; C: 0; rejected: 0.
- Rows touched old→new: none (no status/recheck/used-by flips on existing
  rows; S480 lands `mined` with `used-by` naming its two real consumers).
- Frontier rows advanced: §4.3.1/§4.3.3 validation-exchange ground entered
  the registry (distinct scope from S456's storage/freshness reading and
  S476's §4.3.2 cache-role reading) and backs the round's knowledge entry.
  Still open per `corpus/README.md` and the SCORECARD planned section:
  storage/key identity (RFC 9111 §4.1), serving stale without a client
  directive, the merged 304 field set (§4.3.4), live-cache observation,
  and every routed counter defect (R96-1…R96-4).
- Sourced claim: C2 rests on S480 (opened this round; entry + contract
  cite it).
- Assimilation: **none** — `merge/kake` still collides on 8 ids
  (re-derived this round: registry 217 ids, staged 129, collisions 8 —
  `w1/ExecReceipts/assimilation/{reg-ids,staged-ids,collisions}`); the
  adoption Gate entry records the flip condition. considerthese: none
  taken this round.

## Trend verdicts

- **expansion: unchanged** — one admitted knowledge entry plus the S480
  registry row (216 → 217, census exit 0), but the capability they back
  does not enter the repertoire this round (no frozen-counter pass), so
  the repertoire the coverage map measures is unchanged; the registry
  growth is recorded, not claimed as repertoire expansion. Evidence:
  `corpus/knowledge/revalidation-exchange.md`, `controls/census-after.txt`.
- **quality: improved** — the corpus repairs landed and are now
  certifiable (presence-pinned successor counter `met=true` at the tip;
  15 SKILL rows and three entry-head repairs from round 95 finally carry a
  passing identity surface), two gate-registry rows landed, the S480/entry
  pair is quote-verified (13/13), and no admitted entry failed a re-check;
  the C2 counter defect is receipted rather than papered over. Evidence:
  `controls/after-c1-successor.txt`; `w1/ExecRegistry/resolution-receipts.txt`;
  `w1/ScribeEntry/quotes-verified.txt`.
- **discernment: unchanged** — the round's own attack seats falsified both
  instruments (ReviewC1 four new false-greens; CriticClaims 14 reached
  routes; SentinelScope F1–F4; MutReval 5 survivors) and the C2 crash
  stopped the round honestly instead of being patched post-freeze; the
  freeze's do-nothing wording defect is recorded as Mistake 3, not
  defended. No disagreement was left unlearned — each became a routed
  class rule or a lesson row — but the verdict stays unchanged because the
  improvement claim belongs to the outside closure's spot-check, which is
  owed. Evidence: `corpus/lessons/round-96.md` §Mistakes/§Routed;
  `w1/{ReviewC1,CriticClaims,SentinelScope,MutReval}/`.

## SHONEN

- [~] Box 1 (decision tables / error patterns / checklists with resolvable sources) — author-asserted: SKILL.md carries the decision tables, error-pattern lists and checklists with committed-blob citations; the two new gate-registry rows resolve (`w1/ExecRegistry/resolution-receipts.txt`, rows=2 resolved=8/8). No non-author verifier this round; promotion stays operator-owned.
- [ ] Box 2 (an end-to-end task executed and logged) — unchanged gap; the round-95 spot-check keeps box 2 at `[ ]` and nothing this round discharges it.
- [~] Box 3 (instructions executable without oral context) — author-asserted: the frozen counters carry self-contained CLI contracts (docstring + registry rows + freeze); a reader re-runs every receipt from the named commands. No non-author verifier this round.
- [~] Box 4 (no cross-domain bleed; PROVINCE.md accurate) — author-asserted: the wave's sibling reads stayed read-only (ConnectorScope wrote only inside `w1/`), contested ground is reported, not absorbed (`w1/ConnectorScope/overlaps96.md`); PROVINCE.md untouched this round. No non-author verifier this round.

## Extras

- **Stale-lane:** none — this lane's only open mission is this round
  (respawn-per-round driver); no mission older than two driver ticks.
- **Tool installs:** none (no pacman; network limited to the scout's one
  rfc-editor GET). No tool/version/channel records to report.
- **Open L0 questions:** `kake | round-94` (two honest unmet claims) stays
  unanswered — routed around, not assumed; this round adds `kake |
  round-96` (R95-2 fleet kill-predicate arbitration).
- **Wave details:** 12 seats, one v1 wave, band 8–16 under
  `ufo-wave-policy.json`; dispatch adopted at 2026-11-05T15:16:55; results
  `w1-results.json`; dead seats: none. A wave seat that reproduces a
  digest mismatch on a frozen instrument reported it rather than patched —
  as did every attack seat; no frozen byte changed after the freeze
  commit, verifiable against `controls/instrument-sha256.txt`.
