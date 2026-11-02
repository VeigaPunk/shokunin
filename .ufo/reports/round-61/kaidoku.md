# kaidoku — round 61 report

Lane `kaidoku-shokunin`, agent `KaidokuR61`, L1-inline on the Windows host
(2026-11-01). Round base `2d976fba2bfc3b85dcc0546f9ec8e149fa2185fe` (the r60
verifier spot-check commit; lane `main` tip at round start, pushed =
origin/main). Tip at filing: `d790d82a5011be00186f1a38a9c5427c4e50c5dc`
(`git ls-remote origin refs/heads/main` prints it; verified immediately
before this report was written). Fresh-start round (the prompt's §7 list
r50/r51/r52 re-read and spot-checked before declaring; probes pasted in
`.ufo/waves/round-61/l1/scores/freshstart-spotcheck.txt`: the r50 honest-stop
report present at the fleet root naming the run-11 wrap-up stop, r51's
`wave-accounting.json` carrying `floor64_met: false` as filed, r52's
SCORECARD section naming both claims unprovable, the 19 W04 standing at both
census ends). Ruled out: none of the three rejections was for an inflated or
unverifiable claim — all were operator/provider honest-stops — so the bar
this round cleared is the do-nothing control test, and both declared claims
have red before-arms at the base.

## Work performed

Declared claims (2, causally separable, distinct owned axes; coverage /
depth / calibration sit tied at 10.0 in `SCORECARD.md`, so both are
lowest-axis claims; stagnation nudge not fired — window N=10, last
capability r60, r61 = 1/10):

- **R61-C1 — calibration: the round-60 closure's routed note 1 (D60-1)
  closes append-only.** The r60 after-arm receipt
  `.ufo/waves/round-60/l1/scores/c1-after.txt` says "SKILL delta
  landing→record exactly `1 0` by numstat"; the `1 0` numstat is the
  freeze→landing edge (the landing `bbdb03ab…` added the registry row) and
  landing→record re-derives `0 0` — the r60 non-author closure's precision
  note, routed to this round. The correction landed append-only: a
  correction block appended to the defective receipt (filed bytes stay as
  filed; the append is additions-only `14 0`), the correction receipt
  `.ufo/waves/round-61/l1/scores/d601-correction.txt` with all three true
  edges re-derived, a NEW LOG correction entry, and the SCORECARD round-61
  section naming both sibling sites — the LOG r60-close entry ("the SKILL
  delta landing→record exactly `1 0`") and the SCORECARD round-60 atom T7
  ("the SKILL delta landing→tip exactly `1 0`"; landing→tip re-derives
  `0 0`, base→tip is `1 0`). Evidence: `scores/c1-before.txt` (before) and
  `scores/d601-correction.txt` (after).
- **R61-C2 — depth, capability acquisition: the edge-numstat class becomes
  an instrument.** `tools/round-61/numstat-edge-audit.py` (pin `6b967e20…`,
  committed at the declaration BEFORE the claims file, QUALITY #33): a
  receipt's committed bytes are scanned for rev-name bindings and for edge
  claims of the strict grammar SUBJECT delta A→B exactly `x y`; every claim
  is re-derived by `git diff --numstat` as an argv subprocess; binary edges
  and unresolvable names fail closed; zero claims is exit 2, never
  vacuously clean (QUALITY #66). Demonstrated red on the routed defect
  itself, on both siblings, fail-closed and zero-claimed; registered (SKILL
  registry row 7 cells pipe-free, SCORECARD capability row, census3 drift
  census 66 paths). Evidence: `scores/c2-before.txt` (before) and
  `records/edge-green-correction.txt` + `records/edge-persistent-c1after.txt`
  (after).
- **Carry-in duties (routed, status-neutral):** (1) the precision
  correction above — with the two sibling sites the closure's note implies,
  named honestly rather than quietly; (2) the 19 standing W04
  duplicate-url warnings remain named debt at both census ends (never
  waived into clean); (3) the kaidoku round-53 L0 question remains open and
  unanswered — routed around, never treated as answered.
- **The orphaned-evidence duty ran to dispositions:** the receipt-audit
  sweep over the EIGHT host-era containers r53–r60 at the base — six clean
  + TWO findings of the same quotation class (the r58 container's standing
  bare name, AND the r60 container's bare name, named for the first time
  because round-60's own container enters the sweep for the first time and
  its T5 atom quotes the r58 finding); the new finding was hand re-verified
  BEFORE its disposition (`records/r60-finding-hand-reverify.txt`: the name
  appears at exactly one line of the container, the T5 quotation; the bytes
  exist under round-54 and round-55, byte-identical sha256 `b508a78a…`) and
  dispositioned before the landing (`records/duty-finding-dispositions.txt`;
  NO copy planted — the fourth refusal). The record-audit over the r60
  record section: named 21, missing 0, clean
  (`records/record-audit-r60.txt`). The two-direction orphan census
  (`records/orphan-census.txt`): three worktree-only paths outside the wave
  dir (the r55 first-chain orphan retained-and-disclosed per r58 reject 1;
  two gitignored .pyc caches) + 15 wave-dir files that landed with the
  freeze; direction 2 = exactly the 50-path `EX-08/aux/` reserved-name
  class.
- **The standing halfway sweep re-ran** at the record rev (the r60 planned
  field): `records/sweep-at-r61-record.txt` — exit 0, 235 receipts, the 5
  standing findings unchanged and all dispositioned by the committed TSV,
  0 invocation errors; the round-61 receipts add no annotation-grammar
  shapes, exactly as designed (the correction block deliberately avoids
  restating the strict claim shape).
- **No wave** — no dispatch surface exists on this host; the kaidoku
  round-53 L0 question stays open and unanswered.

## Landed changes

| commit | change | LOG entry |
|---|---|---|
| `319e5244f088fc01cca7b0b8259f0ce5085e7b48` | carry-in: the r60 non-author closure recorded (admitted true, spot-check path `corpus/lessons/round-60-verifier-spotcheck.md`, QUALITY #34) before any claim was measured; note 1 accepted as the routed correction target D60-1 with the two sibling sites named; the 19 W04 + the r53 L0 routing named | carry-in entry |
| `9eb5f0e4cb134a320abbd2e9679c69d4dea8c6b6` | declaration: `tools/round-61/numstat-edge-audit.py` (committed BEFORE the claims file, QUALITY #33) + `plans/round-61-claims.md` (the fresh-start spot-check probes pasted) | declaration entry |
| `5286dccf86bdb598af23fd3a034592af5a5c97b6` | operative freeze: `claims.json` (8 pinned instruments) + FREEZE + census-start + both before-arms + fresh-start probes + the edge-gate demo receipts (selftest, three reds, fail-closed, zero-claims) + duty receipts (eight-container sweep, hand re-verification, dispositions, record-audit, orphan census) + S261 snapshot + the M61-1 draft note | freeze entry |
| `e97e621e21bd285bbff2cc95c184c16f10efb04a` | landing: the D60-1 correction appends to the r60 c1-after (additions-only `14 0`, the first 37 lines byte-identical `873c447f…`) + the correction receipt `scores/d601-correction.txt` (three true edge claims, full 40-hex bindings, no placeholder — the M60-2 rule) + the SKILL registry row (7 cells, pipe-free — the M61-2 self-catch) + the SCORECARD capability row (first-working round 61) | landing entry |
| `1fcb9ab90aa776d17da3ac3d69e8662563cab786` | record: SCORECARD round-61 section + lesson round-61 (Gate S261 + three rejects, M61-1..M61-3) + SOURCES S261 (167→168, Registry position after S260) + ledger row round-61 (CLEAN) + gate pre-flight receipt + census61-at-landing (66 paths) | record entry |
| `d790d82a5011be00186f1a38a9c5427c4e50c5dc` | close: after-arm `scores/c1-after.txt` at the record rev + the green arm (exit 0, 3 claims) + the persistent arm (exit 1, line 10 only) + the sweep re-run at the record rev (exit 0, 235 receipts) + census-check-at-record (66/66 exact) + gate-landing (rc 0, round-59/60/61 CLEAN, disclosures 36/36 exact) + census-end (exit 0, 19 W04, 168 rows) + LOG closing entry | close entry |

Every commit diff-tree-verified against its intended path list (the M55-4
rule); LOG append-only throughout (base→tip exactly `40 0` by numstat);
PROVINCE diff empty base→tip; the owned-axes rows byte-equal base→tip; the
SKILL delta freeze→tip exactly `1 0` — precisely the one added registry row,
the edge named correctly this round's own atoms (the D60-1 lesson applied to
the round itself); the SKILL v6 marker-block digest unchanged `946e5359…` at
base and record; the r60 filed bytes never amended except the ONE disclosed
additions-only append to `c1-after.txt`.

## Before → after measurements

**R61-C1 (calibration).** Before (at the base `2d976fba…`,
`scores/c1-before.txt`): `git cat-file -e
2d976fba…:.ufo/waves/round-61/l1/scores/d601-correction.txt` → rc 128; the
mislabel as filed at all three sites — `git show <base>:…c1-after.txt |
grep -c 'landing→record exactly'` → 1, `git show <base>:LOG.md | grep -c
'the SKILL delta landing→record exactly'` → 1, `git show <base>:SCORECARD.md
| grep -c 'delta landing→tip exactly'` → 1; no correction block (grep 0);
the true edges re-derived (freeze→landing `1 0`; landing→record empty;
landing→close-tip empty; base→record `1 0`). After (at the record rev
`1fcb9ab9…`, `scores/c1-after.txt`): the correction receipt present rc 0;
the correction block present (grep 1); the append additions-only —
`git diff --numstat 5286dccf… e97e621e… -- …c1-after.txt` → exactly `14 0`;
the corrected edges on the record: `git diff --numstat bbdb03ab…
29083b0c… -- SKILL.md` → empty (landing→record `0 0`); the correction
receipt re-derives green under the round's own gate (`records/edge-green-
correction.txt`: exit 0, 3 claims, 0 findings) while the defect's own
receipt keeps firing at line 10 only (`records/edge-persistent-c1after.txt`:
exit 1, NUMSTAT_EDGE_MISMATCH@10). A do-nothing control cannot produce the
correction block, the receipt, the LOG/SCORECARD corrections, or the
append-only proof.

**R61-C2 (depth, capability acquisition).** Before (at the base,
`scores/c2-before.txt`): `git cat-file -e
2d976fba…:tools/round-61/numstat-edge-audit.py` → rc 128;
`git show 2d976fba…:SKILL.md | grep -c 'numstat-edge-audit'` → 0;
SCORECARD → 0; `git ls-tree -r --name-only 2d976fba… -- .ufo/waves | grep -c
'records/edge-'` → 0. After (at the record rev): instrument present rc 0;
SKILL registry rows → 1 (7 cells, pipe-free; the SKILL delta freeze→record
exactly `1 0`); SCORECARD matching lines → 3 (the capability row, the
section's header para, the section's claim row); selftest 25/0
(`records/edge-selftest.txt`); RED on the routed defect at the base —
`python -X utf8 -I -B tools/round-61/numstat-edge-audit.py --root .
--receipt .ufo/waves/round-60/l1/scores/c1-after.txt --rev 2d976fba…` →
exit 1, NUMSTAT_EDGE_MISMATCH@10, claims `1 0`, re-derives `0 0`, resolved
from the receipt's own header bindings — the routed defect named
mechanically for the first time (`records/edge-red-c1after.txt`); RED on
the T7 sibling (exit 1, @4606; the r59 T8 `freeze→fixup` `1 0` atom green
on the same run; `records/edge-red-scorecard.txt`); RED on the LOG
r60-close sibling (exit 1, @3857; the r59 entry's true claim green on the
same run; `records/edge-red-log.txt`); fail-closed arm (no overrides: 2×
NUMSTAT_NAME_UNRESOLVED; `records/edge-failclosed-scorecard.txt`);
zero-claims arm (exit 2; `records/edge-uneval-d581.txt`); GREEN on the
correction receipt at its landing rev (exit 0, 3 claims;
`records/edge-green-correction.txt`); PERSISTENT (exit 1, line 10 only;
`records/edge-persistent-c1after.txt`); census3 `--generate` 66 paths at
the landing rev, `--check` at the record rev exit 0 exact 66/66. A
do-nothing control cannot produce the gate, the demos, or the registrations.

**Census before → after (§2b):** start receipt
`.ufo/waves/round-61/l1/census-start.txt` — host-adapted command
`bash <fleet-root>/scripts/sources-census.sh validate --root <fleet-root>
<lane-repo-dir>` → exit 0, 19 standing W04, 167 rows (the literal
kaidoku-name form exits 2 on this host, disclosed since r53 — routed
around). End receipt `.ufo/waves/round-61/l1/census-end.txt` → exit 0 on
run 1 at the record state, 19 standing W04, 168 rows. Exit 0 at round end:
met. W04 stays named debt.

**Mistakes mined (§2b, `corpus/lessons/round-61.md` ## Mistakes):** M61-1
(an edge written where the probe's edge belongs — the before-arm's baseline
probe drafted against the r60 round base, where the probe prints `37 0`, and
corrected to the r60 close tip, where the edge is empty, BEFORE any commit —
the D60-1 class firing on this round's own draft); M61-2 (the registry-row
draft carried the gate's own subject alternation, whose three literal pipes
made the row read 10 cells; the seven-cell recount caught it pre-landing;
the alternation spelled out in words); M61-3 (the stale index on this host
makes `git diff HEAD -- <path>` report landed files as deleted — `0 37` —
while the worktree bytes are byte-identical; the honest measurements are
hash-identity for worktree-vs-blob and rev-to-rev numstat for landed
deltas).

## Sources & frontier

SOURCES: 167 → 168 rows. Counting command: `grep -c '^| S' corpus/SOURCES.md`
at the base → 167, at the record rev → 168. New row: S261 — the git-diff
documentation (tier A docs, mined; snapshot `.ufo/waves/round-61/l1/s261/`,
git-diff.html sha256 `5ae80d1deee5dc2c1acafff5491c5ba019629b9a785e6781a3e8a411cf9e22ed`,
229155 bytes, fetched read-only with curl 2026-11-01; the Gate quote — 24
words — labelled composite per QUALITY #42, the locator the `OPTIONS`
heading verified programmatically per QUALITY #91), the sourced claim for
R61-C2 (the `--numstat` semantics the edge gate re-derives with, and the
binary `- -` sentence behind the NUMSTAT_BINARY fail-closed class); row and
used-by targets (`plans/round-61-claims.md`, `tools/round-61/numstat-edge-
audit.py`, `corpus/lessons/round-61.md`) landed with the row in the record
commit (the M53-4 rule); the row placed in its Registry position directly
after S260 BEFORE the record commit (the r59 E12 lesson applied
pre-landing). The 19 standing W04 duplicate-url warnings remain named debt
at both ends.

## Trend verdicts

- **expansion: unchanged** — no new admitted `knowledge/` entry; PROVINCE
  diff empty base→tip (verified); S261 is tool documentation, not an REA
  surface; one capability row grows the repertoire table, not the coverage
  map.
- **quality: improved** — the routed edge-mislabel class (three sites
  named by the r60 closure and its lineage) now carries a mechanical gate
  demonstrated red on every site with the true r59 claims green on the same
  runs; the correction closes append-only with every edge re-derived from
  committed bytes; the standing sweep re-entered its halfway audit at 235
  receipts with the findings set unchanged; the registry re-entered its
  drift census at 66 paths exact; three mistakes mined, all self-caught
  before landing; no admitted entry failed a re-check.
- **discernment: unchanged pending the outside spot-check** — the round
  executed the routed note verbatim and extended it to the two sibling
  sites honestly rather than quietly; the duty's new eighth-container
  finding was hand re-verified and dispositioned before the landing, with a
  fourth refusal to plant the copy; the round self-caught its own edge
  draft (M61-1) and its own registry-row pipes (M61-2) before any commit;
  no unverified claim landed. LEARNING.md's improved condition ("the
  spot-check agrees with the gate on admits and rejects") requires the
  outside check that is still pending.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists,
  cited sources — the instrument registry re-entered its drift census at 66
  paths exact this round (`records/census61-at-landing.json`,
  `records/census-check-at-record.txt`); the v6 marker-block digest
  unchanged `946e5359…`; author-asserted with resolvable pointers.
- [~] At least one end-to-end domain task executed and logged in LOG.md —
  the routed D60-1 correction closed end-to-end with receipts (carry-in →
  correction append → gate demos → census); LOG base→tip exactly `40 0`;
  author-asserted with resolvable pointers.
- [~] Instructions executable by an agent without oral context — the new
  gate's registry row carries its entry command, verdict map, selftest
  spelling, pinned-value path and write scope (SKILL.md instrument-registry
  v2); every demo receipt transcribes its exact argv; author-asserted with
  resolvable pointers.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — PROVINCE diff
  empty base→tip (numstat-verified); S261 is tool documentation recorded in
  the corpus, not a province surface; author-asserted with resolvable
  pointers.

No `[x]` flip is written by the author; the canonical SHONEN.md remains
unchecked and the promotion decision belongs to the operator/promotion
process.

Assimilation: `considerthese/` does not exist in this lane (measured at
round start) and nothing was adopted from it; Assimilation: none — shokuknow
unreachable.
