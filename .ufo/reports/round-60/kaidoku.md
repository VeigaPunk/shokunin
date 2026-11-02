# kaidoku round 60 — the halfway receipt-corpus sweep

Lane kaidoku (shipped-artifact reverse engineering with REA), round 60 of the
hyaku campaign — the halfway round for this lane. L1-inline on the Windows
host, 2026-11-01. Base `48c418305b71ea603e58f4fe9bd0dfbf2aafa9e4` (the r59
verifier spot-check commit — r59 closed **admitted true**; the decision is
recorded in the lane's LOG and this round's carry-in commit, QUALITY #34).
Lane tip at filing: `1c1d68805039596bea4498beef5352e42d84ad98`, pushed =
origin/main.

## Work performed

- **Carry-in first (the r59 non-author closure, status-neutral):** the
  outside decision (admitted true, `corpus/lessons/round-59-verifier-spotcheck.md`)
  is recorded in LOG before any claim was measured. The four status-neutral
  notes were routed around, not treated as answered: the r50 "exit 1" prose
  is cited this round with the JSON key name (`exit_code`, value 1 — the
  precision note applied in the fresh-start probe); the 19 standing W04s
  stay named debt at both census ends; the w58 sweep-finding flip condition
  stays on record with the closure's not-firing ruling (re-named by this
  round's duty and re-dispositioned, no copy planted); the kaidoku round-53
  L0 question stays open and unanswered (routed around).
- **R60-C1 (depth, capability acquisition) — `tools/round-60/annotation-sweep.py`,
  the r59 planned candidate executed:** the multi-receipt annotation-consistency
  sweep. One `git ls-tree -r --name-only REV -- .ufo/waves` listing filtered
  to the committed receipt corpus (`.ufo/waves/round-N/l1/scores|records/`),
  each receipt audited by the FROZEN single-receipt gate
  `tools/round-59/annotation-audit.py` (pin `ba9ccbb9…`, worktree bytes
  sha-checked before every run via `--expect-sha256`), one argv subprocess
  per receipt (S260's `subprocess.run` composition, no shell); every finding
  key must be covered exactly by a committed disposition TSV — missing or
  empty row = uncovered, extra row = DISPOSITION_ORPHAN, both exit 1; zero
  receipts or any invocation error = exit 2, never vacuously clean (QUALITY
  #66). Demonstrated red-green-red on the committed base: exit 1 with no
  dispositions (the FIRST complete inventory of the receipt corpus — 188
  receipts, 2 green, 2 findings-class, 184 unevaluable, 0 invocation errors,
  5 findings named, `.ufo/waves/round-60/l1/records/sweep-red-nodispo.txt`);
  exit 0 with all 5 dispositioned (`records/sweep-base-green.txt`); exit 1
  again with one disposition row removed, the uncovered key named
  (`records/sweep-red-missing-key.txt`); selftest 28 cases 0 failures.
  Registered: SKILL registry row (7 cells, pipe-free), SCORECARD capability
  row (first-working round 60), container pin `38614088…`, census3 drift
  census re-run (65 paths at the landing rev, `--check` exit 0 exact at the
  record rev). Evidence: `plans/round-60-claims.md`,
  `.ufo/waves/round-60/l1/scores/c1-before.txt` / `c1-after.txt`,
  `.ufo/waves/round-60/claims.json`.
- **The round's orphaned-evidence duty (operated by the claim):** the
  receipt-audit sweep over the SEVEN host-era containers r53–r59 at the base
  = six clean + the r58 container's quoted bare name (standing disclosed
  named debt; `records/receipt-audit-sweep.txt`); the record-audit over the
  r59 record section = named 21, missing 0, clean
  (`records/record-audit-r59.txt`); the two-direction orphan census named
  FIVE worktree-only paths and all five are dispositioned
  (`records/orphan-census.txt`) — including the round's live discovery:
  **`.ufo/waves/round-59/l1/records/annotation-selfcatch.txt` existed on
  disk since r59 but was never committed** (cat-file rc 128 at the base)
  while committed records cite it as an evidence pointer — repaired by the
  carry-in commit `ec9d93d7` landing the bytes byte-identically (sha256
  `175ef241…` re-hashed from the commit object) with a provenance receipt
  (`records/selfcatch-provenance.txt`), the r58-R2 pattern, before the
  freeze; direction 2 is exactly the 50-path `EX-08/aux/` reserved-name
  class (the PROVINCE-documented host checkout boundary).
- **The sweep's first inventory named one finding for the FIRST time** —
  `.ufo/waves/round-59/l1/scores/c1-after.txt:37:COMMAND_UNREEXECUTABLE`
  (the r59 after-arm landed at the r59 close, after the r59 demos): hand
  re-verified BEFORE its disposition row was written — pasted output 1 =
  record 1, and the exact bound command re-runs to 1 at the revision it
  names (`records/sweep-first-inventory.txt`); the finding is the frozen
  gate's documented fail-closed grammar boundary, not a contradiction. The
  other four findings are the standing disclosed classes (the persistent
  D58-1 pair; the M59-3 prose-mimicry pair), each disposition row citing its
  standing disclosure (`records/sweep-dispositions.tsv`).
- **Fresh-start compliance (operator rule):** r50/r51/r52 re-read and
  spot-checked before declaring — (1) the r50 counter receipt at HEAD
  carries `carriers_matched 2`, `target 4`, `met_target false`,
  `exit_code 1` (the JSON key is `exit_code`); (2) census3 `--historical`
  at `f04b51dd` reproduces exit 1, registry 55 / census 42 / outside 13;
  (3) `00d0bfd0` is an ancestor of main carrying `plans/round-52-claims.md`.
  **Ruled out, with reasons:** the AVM LE-SquashFS Frontier→Core (host-absent
  surfaces unchanged; three rounds died on it); any wave-based claim (no
  dispatch surface; the r53 L0 question open); resuming the r51/r52
  triage-v6 drafts (twice-rejected incomplete instruments); amending any
  frozen container/instrument or filed receipt (the amendment class; the
  round's only landing into historical scope is the worktree-only selfcatch
  file, byte-identical and disclosed).
- **One claim, and why:** the sweep's disposition table IS its green
  condition, so a separate "dispositions" claim would not be causally
  separable from the instrument claim; one genuine verified claim beats an
  inseparable pair. Halfway note: the round's substance — the first complete
  mechanical audit of the lane's own receipt corpus — is the halfway audit
  this lane can honestly perform on this host.

## Landed changes

| commit | change | LOG entry |
|---|---|---|
| `ec9d93d7dcf72ba2aff88b3d72a3e39910bbc820` | carry-in: the r59 outside decision recorded (QUALITY #34) + the orphaned r59 selfcatch receipt lands byte-identically + provenance receipt | carry-in entry |
| `691460faa2f326df71407ed88bfe0a6152a10a3f` | disclosed one-line fixup: the carry-in sha fills the provenance receipt's post-landing verification (M60-2; the landing copy stays as filed) | carry-in entry (disclosed) |
| `eb4f6a7f8b37bc8a8843bcade7cbe959dc7dfff9` | declaration: `tools/round-60/annotation-sweep.py` (committed BEFORE the claims file, QUALITY #33) + `plans/round-60-claims.md` | declaration entry |
| `8e58366300aa30c097c81e68df2d0d30c689ed6f` | operative freeze: `claims.json` (7 pinned instruments) + FREEZE + census-start + before-arm + sweep receipts (selftest, red-nodispo, dispositions TSV, green, red-missing-key, first-inventory) + duty receipts (seven-container sweep, record-audit r59, orphan census) + S260 snapshot | freeze entry |
| `bbdb03abdafd777b10767071f3a16267bcccf866` | landing: SKILL registry row (the glued-insertion self-catch repaired before any commit, M60-1; delta exactly `1 0`) + SCORECARD capability row | landing entry |
| `29083b0c18ecb2620e8a8812688a9b65acedb592` | record: SCORECARD round-60 section + lesson round-60 + SOURCES S260 (Registry position, after S259) + ledger row + gate-preflight receipts + census60-at-landing | record entry |
| `1c1d68805039596bea4498beef5352e42d84ad98` | close: after-arm `c1-after.txt` + gate-landing receipts + census-check-at-record + census-end + lesson gains M60-3 (additions-only) + LOG closing entry | close entry |

Every commit diff-tree-verified against its intended path list (the M55-4
rule); LOG append-only throughout (LOG base→record exactly `38 0` by
numstat; PROVINCE diff empty base→tip; owned-axes rows byte-equal; the SKILL
v6 marker block digest unchanged `946e5359…` at base and record).

## Before → after measurements

**R60-C1 (depth, capability acquisition).** Before (at the base
`48c41830…`, `scores/c1-before.txt`): `git cat-file -e
48c41830…:tools/round-60/annotation-sweep.py` → rc 128; `git show
48c41830…:SKILL.md | grep -c 'annotation-sweep'` → 0; SCORECARD → 0;
`git ls-tree -r --name-only 48c41830… -- .ufo/waves | grep -cE
'^\.ufo/waves/round-[0-9]+/l1/(scores|records)/'` → 188 receipts, 0
complete inventories. After (at the record rev `29083b0c…`,
`scores/c1-after.txt`): instrument present rc 0; SKILL registry rows → 1
(delta exactly `1 0`); the red-green-red demonstrations on the immutable
base (exit 1 / exit 0 / exit 1); selftest 28/0; and the sweep re-run at the
record rev: `python -X utf8 -I -B tools/round-60/annotation-sweep.py --root
. --rev 29083b0c… --expect-sha256 ba9ccbb9… --dispositions
.ufo/waves/round-60/l1/records/sweep-dispositions.tsv` → **exit 0**,
`{"receipts_total": 213, "counts": {"green": 2, "findings": 2,
"unevaluable": 209, "invocation_error": 0}, "findings_total": 5, "exit": 0,
"exit_reason": "inventory complete; 5 finding(s) all dispositioned"}` — at
the close tip `1c1d6880…` the same command re-derives exit 0 over 217
receipts (the close adds four more prose/JSON receipts, all unevaluable
class; verified before this report was filed). A do-nothing control cannot
produce the instrument, the inventory, the disposition-enforced green arm,
or the registration.

**Census before → after (§2b):** start receipt
`.ufo/waves/round-60/l1/census-start.txt` — host-adapted command
`bash <fleet-root>/scripts/sources-census.sh validate --root <fleet-root>
<lane-repo-dir>` → **exit 0**, 19 standing W04, 166 rows (the literal
kaidoku-name form exits 2 on this host, disclosed since r53 — routed
around). End receipt `.ufo/waves/round-60/l1/census-end.txt` → **exit 0**
on run 1 at the record state, 19 standing W04, 167 rows (the S260 row was
placed in its Registry position BEFORE the record commit — the r59 E12
lesson applied pre-landing; a trial census against the pre-commit worktree
also exited 0). Exit 0 at round end: **met**. W04 stays named debt.

**Mistakes mined (§2b, `corpus/lessons/round-60.md` ## Mistakes):** M60-1
(the SKILL insertion anchored on the shared r59 row-tail — glued row,
neighbor's tail cells consumed; the seven-cell recount read 12 cells and
caught it BEFORE any commit; repair verified by numstat `1 0`); M60-2 (a
receipt written before the commit it cites carried a literal placeholder;
the disclosed fixup `691460fa…` fills it, the landing copy stays as filed);
M60-3 (the after-arm draft wrote a SCORECARD probe count from arithmetic —
2 — where the probe prints 3; the pre-close re-derivation of the receipt's
own pasted outputs corrected it BEFORE the close landed — the D58-1 class
caught pre-landing by the round's own discipline).

## Sources & frontier

SOURCES: 166 → 167 rows. Counting command:
`grep -c '^| S' corpus/SOURCES.md` at base → 166 record rows (S-numbered
rows 166 by the census's own count), at the record rev → 167; the new row
**S260** (Python subprocess module documentation,
https://docs.python.org/3/library/subprocess.html, tier A docs, opened this
round with curl; snapshot bytes + sha256 `6e86cc82…85b` at
`.ufo/waves/round-60/l1/s260/`) grounds R60-C1's composition — the frozen
gate runs through `subprocess.run`'s argv form, the documented recommended
helper, no shell; the Gate quote is labelled **composite** per QUALITY #42
(the words `run()` sit inside an inline literal span; locator: the h2
`Using the subprocess Module`). Used-by: `plans/round-60-claims.md`,
`tools/round-60/annotation-sweep.py`, `corpus/lessons/round-60.md` (landed
with the row, the M53-4 rule). Gate rejects this round: extending the
frozen gate instead of a new instrument; planting a third copy of the r58
bare-name receipt; mechanically-generated disposition boilerplate. No
Frontier→Core move; PROVINCE diff empty; S260 is tool documentation, not an
REA surface. Assimilation: none — `considerthese/` does not exist in this
lane (measured at round start); shokuknow unreachable.

## Trend verdicts

- **expansion: unchanged** — no new admitted `knowledge/` entry, no
  coverage-map move (PROVINCE diff empty base→tip), S260 is tool
  documentation; one capability row grows the repertoire, not the map.
- **quality: improved** — the receipt corpus (the lane's whole evidence base
  for the annotation-contradiction class) now carries a mechanical,
  disposition-enforced inventory, demonstrated red-green-red on committed
  bytes with the frozen per-receipt gate composed, never duplicated; the
  registry re-entered its drift census at 65 paths exact; three mistakes
  mined, two of them caught by the round's own instruments/discipline before
  landing.
- **discernment: unchanged pending the outside spot-check** — the round
  executed the r59 planned field verbatim, named its first-inventory finding
  before writing its disposition (and hand-verified it), landed the orphaned
  r59 receipt with provenance and disclosure rather than silently, declared
  one claim rather than an inseparable pair, self-caught its own glued SKILL
  insertion and its own arithmetic probe count before those bytes landed,
  and recorded the r59 outside decision before measuring. The non-author
  closure judge re-derives everything below this line.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists,
  cited sources — the instrument-registry v2 block now carries 65
  census-verified rows including the round-60 sweep row (7 cells, pipe-free);
  craft blocks and the registry re-verified by census3 `--check` exit 0 at
  the record rev (`.ufo/waves/round-60/l1/records/census-check-at-record.txt`).
- [~] At least one end-to-end domain task executed and logged in LOG.md —
  this round's end-to-end task is the receipt-corpus audit itself (red
  inventory → dispositions → green → re-run at record and tip), logged in
  the LOG declaration/freeze/landing/record/close entries with receipts
  under `.ufo/waves/round-60/l1/`.
- [~] Instructions executable by an agent without oral context — the sweep's
  registry row carries the entry command, verdict map, selftest spelling and
  write scope; every receipt pastes its own commands and outputs
  (`records/sweep-base-green.txt` et al. re-derive verbatim).
- [~] No cross-domain bleed (PROVINCE.md still accurate) — PROVINCE diff
  empty base→tip; S260 and the sweep are lane-internal instrumentation, and
  the report claims no domain-surface ground.

No SHONEN box is flipped `[x]` by the author; promotion review stays with
the operator/lane process. The r53 L0 question remains open and unanswered;
routed around, never treated as answered.

ROUND kaidoku r60 done lane_head=1c1d68805039596bea4498beef5352e42d84ad98 pushed=yes claims=1 admitted_self=true
