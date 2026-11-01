# kotodama — round 80 (Windows host, 2026-10-31/11-01; fresh-session L1)

Lane tip at filing: `b7c5be2b84155266f5c6d4d590a4bedad829da77`, pushed to
origin main (`git ls-remote` matches). Base `a8aaece…` (r79 spot-check
commit). Two claims declared, frozen, landed, counter-verified; the r79
carry-in is fully executed. Scratch dir deleted at close.

## Work performed

- **Carry-in item 1 — W1 hardening of `tools/ledger-token-guard.py` as a
  QUALITY 23 revision with red-befores, plus the never-launched W2 mutation
  pass (claim O, operability).** Four hardenings from the r79 wave's
  adopted-but-unlanded findings: replace-ref refusal + `GIT_NO_REPLACE_OBJECTS`
  env pin (MutPath F6), 1 MiB ledger input cap + deep-JSON stable refusal
  (SentinelLimits F1/F3), expanded `GIT_*` env drop (SentinelLimits F9),
  distinct-observation floor (MutVacuous F7). Selftest battery 9 → 13
  scenarios. Evidence: `reports/round-80/telemetry/w1-w2-guard-revision-run80.txt`
  (§1 red-befores on the r79 bytes, §2 hardened refusals, §3 detection
  regression + 16/16 r79 refusal fixtures intact + the floor firing on the r79
  probe ledgers themselves — the MutVacuous F7 shape, recorded as a behavior
  change in `reports/round-80/counter-revisions.md`, §4 clean 13/13 selftest,
  §5 W2 mutation pass: 5/5 mutants caught, clean scenario green before the
  mutant rows). SKILL.md registry row and SCORECARD capabilities row re-pinned
  to the new sha `cca7db17…f9a`.
- **Carry-in item 2 — the three r79 spot-check wording defects, corrected
  append-only.** `reports/round-80/corrections/r80-annotations.md` binds each
  defect to the filed blob with re-runnable verifications (claims.json "is
  empty" → 27 entries at `44f76d4`, guard path absent; "(20 words)" →
  whitespace-split 16; S897 `python3 -B` → this host runs `python -B`), and a
  `## Corrections — round 80` section is appended to
  `corpus/lessons/round-79.md`. No filed bytes rewritten; no superseding
  registry row spent (disposition recorded).
- **Claim D (depth) — the sea as a lexical surface.**
  `corpus/knowledge/culture-material/maritime-seafaring-lexicon.md` lands as
  the 254th knowledge file: topic/gap/couples/verified-at/recheck/scope
  header, six-decision table, attested anchors with exactly one S-id per
  cited line, craft checklist, non-canon worked example, lore handoff. Three
  sources opened this round by ordinary means (plain curl, HTTP 200 each,
  same-page Wayback captures on file, automation: none): S898 Falconer 1769
  (Gutenberg #57705), S899 Smyth 1867 (Gutenberg #26000), S900 Britannica
  1911 "Ship" (Wikisource). Gap discipline: base topic-line sweep returns 5
  files, all under `civilizations/` — named in the entry's gap cell and
  pointed one-way in §1 (the entry owns no wayfinding).
- **Round instruments:** `reports/round-80/claims.json` (frozen twice — see
  Landed changes), `reports/round-80/accept-o.py` (10 legs) and
  `accept-d.py` (7 legs) with selftests and do-nothing controls, red/green
  distinct-pair fixtures, refusal fixtures, evidence captures, and the
  junk-landing battery (`counters/junk-fixtures.py` + `telemetry/junk-landings.txt`,
  six junk landings each FAILing on its named leg, run against a
  checkout-free plumbing clone because of the R79-M3 uncheckoutable paths).
- **Fresh-start dispositions (read + spot-checked before declaring):** r76 —
  its frozen counter's FAIL is verified on committed bytes
  (`reports/round-76/telemetry/measures-c-final-c28ea.txt`, `ACCEPT-C-76: FAIL
  legs=11/13`); not re-run for a flip. r77 — `grep -c '^## Gate'
  corpus/lessons/round-77.md` = 0 (the records-discipline defect named then);
  this round files its Gate first-class. r78 — the S884 drift is bound by the
  r79 correction (`reports/round-79/corrections/ca79-r78-s884.md`).
  **Ruled out before declaring:** (a) dining/tableware and naming-systems
  coverage entries — carried rejects (r77/r78/r79 Gates), no new evidence, not
  re-litigated; (b) a freshness move — paused by the open round-11 L0
  question, no stagnation-nudge evidence (SCORECARD carries no saturation
  line/window); (c) re-running r76's frozen counters for a flip — a
  do-nothing artifact; (d) integrating the W1 findings into the *round-79
  frozen bytes in place* — would have falsified the r79 graded record; they
  land as a recorded revision instead.

## Landed changes

Commit chain (all by `kotodama-shokunin <kotodama@shokunin.local>`, pushed;
each tied to the LOG.md round-80 entry):

- `08e4fb31` freeze: claims.json, both counters, red/green + refusal fixtures,
  S898–S900 evidence captures.
- `bf95373` pre-landing receipts: do-nothing controls refuse at base (exit 2),
  both counters' selftests PASS at the freeze (QUALITY 23).
- `c365f6c` claim O lands: hardened guard, SKILL.md row re-pin,
  `counter-revisions.md`.
- `66af053` claim D lands: the entry + SOURCES rows S898–S900.
- `70db282` accept-o r2 (NOSTUB fixture committer identity; the crashed first
  graded run committed as the fix's red-before) + evidence capture records
  name their row ids.
- `f480451` **re-freeze (supersedes `08e4fb31` for grading, r79 precedent)**:
  the fleet census's closed kind enum requires `book` — D `row_kinds`
  corrected, O `sibling_paths` extended to the D-side corpus paths so both
  counters grade the shared lands; the failed-census receipt
  (`census-end-e05-kind-enum.txt`) is committed.
- `df38cab` records: lesson (`## Gate`: O+D admitted, carried rejects,
  freshness pause; `## Mistakes` R80-M1..M4 with evidence, captured-by, fix;
  Sources & frontier), SCORECARD round-80 axes section + capabilities row
  re-pin, LOG entry, corrections, junk battery receipts, graded runs, census
  end (exit 0).
- `7439b14` census start receipt (exit 0 at base, 821 rows).
- `b7c5be2` L2 dispatch attempt evidence (below).

## Before → after measurements

- **Claim O (operability):** before — guard sha `504c51c6…` (17822 B) accepts
  all four W1 junk shapes: 1 MiB ledger `PASS pairs=1`; duplicate-observation
  ledger `PASS pairs=2`; deep JSON escapes as an unlabelled `RecursionError`
  traceback; replace-ref ledger graded over shadowed bytes. After — sha
  `cca7db17…` (22640 B) refuses all four at exit 2 with stable labels;
  detection unchanged (red fixture exit 1 failed=3 mismatched=2 vacuous=1;
  green exit 0 PASS pairs=4); selftest 13/13; 5/5 mutants caught. Counting
  command: `python -B reports/round-80/accept-o.py --root <lane> --lands
  f48045141cc3e72d4eb27e5da76369d52bd5bf40 --freeze f48045141cc3e72d4eb27e5da76369d52bd5bf40
  --work <scratch>` → `ACCEPT-O-80: PASS legs=10/10`, exit 0 (re-run fresh at
  the final tip; receipts `lands-o-graded-r3.txt`). Do-nothing control: at
  `--lands` = base the counter refuses, exit 2 (`dry-run-refused-at-base-r2.txt`).
- **Claim D (depth):** before — 253 knowledge files, 821 registry rows, no
  entry owning the surface. After — 254 files, 824 rows, the entry landed.
  Counting command: `python -B reports/round-80/accept-d.py --root <lane>
  --lands f48045141cc3e72d4eb27e5da76369d52bd5bf40 --freeze f48045141cc3e72d4eb27e5da76369d52bd5bf40
  --work <scratch>` → `ACCEPT-D-80: PASS legs=7/7`, exit 0
  (`lands-d-graded-r3.txt`); `grep -cE '^\|\s*S[0-9]{3,}\s*\|'
  corpus/SOURCES.md` = 824 (821 at base); cited-lines lint prints
  `CITED-LINES: 0 finding(s)` on the entry. The ROWS leg's demonstrated
  failure (capture records not naming their row ids at `66af053`) is kept as
  a committed FAIL receipt (`lands-d-graded.txt`) — the leg can fail.
- **Honest failure records kept:** the first accept-o graded run crashed
  before printing legs (counter defect R80-M2; receipt `lands-o-graded.txt`),
  the first D graded run FAILed ROWS 6/7 (`lands-d-graded.txt`), and the
  first census end FAILed E12 then E05 (`census-end-e05-kind-enum.txt`) —
  each fixed and re-run green, none hidden.

## Sources & frontier

`corpus/SOURCES.md` rows 821 → 824 (counting command above; at base `a8aaece`
= 821, at the re-freeze lands = 824). New rows this round, each opened by
ordinary means with its capture record committed under
`reports/round-80/evidence/`: S898 (Falconer 1769, tier A for period marine
terminology), S899 (Smyth 1867, tier A, includes the recorded
sea-superstition entries), S900 (Britannica 1911 "Ship", tier B survey).
Sourced claim: D rests on S898/S899/S900. No prior-row cell changed. Census:
start exit 0 (821 rows, W01/W04 only — `census-start.txt`), end exit 0
(`census-end.txt`); the intermediate failures (E12 row placement, E05 kind
enum) are committed as `census-end-e05-kind-enum.txt` and motivated the
re-freeze. Mistake mining: R80-M1..M4 in `corpus/lessons/round-80.md`
(Windows text-mode fixture corruption at three new write sites; the
ungreppable counter crash; `$?` masked by command substitution; junk-battery
lands geometry), each with evidence pointer, captured-by and fix.

## Trend verdicts

- **expansion: improved** — a new admitted knowledge entry on ground the
  coverage map did not hold, every cited line restating a mined row
  (S898–S900, all `mined` with `used-by` the entry); +3 source rows; no
  admitted entry failed its bar (LEARNING.md expansion observable).
- **quality: unchanged** — no existing entry was re-verified, deepened or
  superseded this round; the guard revision is instrument work (QUALITY 20
  excludes it from quality observables); no entry failed a re-check.
- **discernment: unchanged** — no non-author spot-check was available inside
  the round (below); the gate dispositions (2 admits, 2 carried rejects, the
  freshness pause) are recorded in the lesson's Gate with re-runnable
  receipts so the closure judge can sample admits and rejects from committed
  bytes.

## Swarm floor, stale-lane, assimilation, L0

- **L2 floor: unmet, named, not padded.** An 8-seat batched read-only
  verification wave was authored and submitted through this host's
  dynamic-workflow surface (`.ufo/waves/round-80/l2-attempt/`); it compiled
  cleanly but the host reports execution unavailable in this session, so no
  seat ran. Sibling lanes' draft scripts in the same workspace show the same
  wall. Recorded as a conformance defect of this round; the round's verdicts
  carry their own re-runnable receipts for the closure judge.
- Stale-lane actuator: none — the round ran in one session; no sibling
  mission state is observable from this lane.
- Assimilation: `considerthese/` absent from the lane repo. Assimilation:
  none — shokuknow unreachable.
- L0: no new question appended; the round-11 freshness pause stands as the
  open operator item (same disposition as rounds 77–79).

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md:20`,`:505`,`:564`; the `:767` ledger-token-guard registry row re-pinned this round to sha `cca7db17…` with the 13-scenario selftest; no non-author verifier on record.
- [~] At least one end-to-end domain task executed and logged in LOG.md — round-80 claim D executed end-to-end (sources opened and captured → entry written and linted → frozen counter green); LOG.md round-80 entry; receipts `reports/round-80/telemetry/lands-d-graded-r3.txt` and `lands-o-graded-r3.txt`; no non-author verifier on record.
- [~] Instructions executable by an agent without oral context — both counters and the guard run from committed bytes only (`--root/--lands/--freeze/--work`), selftests build isolated fixtures, and every receipt names its command; this round's runs used only landed bytes plus scratch dirs; no non-author verifier on record.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — PROVINCE.md byte-identical across the round range; writes confined to this lane repo + this report; the census kind-enum constraint and NTFS-path classes are reported as fleet-level observations in the lesson, not absorbed; no non-author verifier on record.

Round marker: claims declared 2 (O operability, D depth); both verdicts
re-derived green on this host at the final tip `b7c5be2b84155266f5c6d4d590a4bedad829da77`;
pushed yes; scratch deleted at close.
