# kaidoku — round 58 report (the r57-closure routed carry-in closes with receipts; the registry-drift census runs again)

Lane `kaidoku-shokunin`, L1-inline on the Windows host, 2026-11-01. Round base
`42c794afc5cdf2f72d80edb839cfbcbfe32e6bad` (the r57 verifier spot-check commit;
pushed = origin/main at round start). Filing tip `d16bb4703440531e45d54562ca32f633f7d27e70`
(pushed; `git ls-remote origin refs/heads/main` = local HEAD, re-verified at filing).
Operative freeze `37e49cf33537ff182265c42f3fa546b1c0c0c0fa` (the first commit adding
`.ufo/waves/round-58/claims.json`). No wave (no dispatch surface on this host; the
kaidoku round-53 L0 question stays open and unanswered — routed around, never
treated as answered). No new instrument: six frozen tools pinned in the container
and audited by the R29 gate. Both claims are offline over committed bytes.

## Work performed

Declared claims (2, causally separable, distinct owned axes — coverage/depth/calibration
sit tied at 10.0 in `SCORECARD.md`, so each is a lowest axis): **R58-C1 — calibration**:
the r57-closure routed carry-in set R1–R4 closes with committed, append-only artifacts
(the coordinator-routed precision note and orphaned-evidence hygiene duty, plus the r57
planned W04 item); **R58-C2 — depth**: the routed registry-drift census runs again after
a data-side registry-row repair (every instrument frozen). Sourced claim: S258 (the GFM
spec, opened this round) grounds C2's defect class and repair side.

- **Fresh-start compliance executed first** (`plans/round-58-claims.md`): r50/r51/r52
  fleet reports re-read and spot-checked against the lane record — r50's counter receipt
  re-read at HEAD shows `carriers_matched 2` of `target 4`; r51's
  `census3.py --historical` at the r51 claims base `f04b51dd…` reproduces exit 1,
  registry 55 / census 42 / outside 13; r52's tip `00d0bfd0…` is an ancestor carrying its
  claims file. **Ruled out**: (1) the AVM LE-SquashFS Frontier→Core (host-absent surfaces;
  three rounds died on it); (2) any wave-based claim (no dispatch surface; the r53 L0
  question open); (3) resuming the r51/r52 triage-v6 drafts (twice-rejected incomplete
  instruments). None of the three rejections died on offline committed-byte work.
- **R1 (spot-check §7 defect 2, the precision carry-in):** the r57 report's "exactly the
  26 files named above" counted named items (the `s257/` snapshot + digests as one item)
  while distinct filesystem paths number 27; the correction note of record is the landing
  LOG entry's first bullet at `05865b6d63b43b6f732e9013c86980d79ddcb52c` (marker
  re-derived in `.ufo/waves/round-58/l1/scores/c1-after.txt`).
- **R2 (the orphaned-evidence hygiene duty):** the sweep ran at the base with receipts —
  `tools/round-56/receipt-audit.py` over the five host-era containers
  (`.ufo/waves/round-58/l1/records/receipt-audit-sweep.txt`: four clean + one FAILED),
  `tools/round-57/record-receipt-audit.py` over the last three record sections (r55
  named 13 missing 1; r56/r57 green), and the worktree-vs-tree orphan census
  (`records/orphan-census.txt`: 3 worktree-only paths dispositioned). **The sweep named
  one live finding and the repair landed**: `.ufo/waves/round-55/l1/scores/freeze-gate-tip-90f3a9b9.json`
  — claimed by the r55 container T2 and the r55 SCORECARD landing-receipts list, while its
  bytes were committed under round-54 (the M55-4 pathspec defect's actual landing). A
  byte-identical copy (sha256 `b508a78ae25880c094ea42d74c48874d248b0cd527c60e4e951028ebccb23df1`,
  equal to the committed round-54 original) landed at the named path at `05865b6d…`; the
  r55 container then audits clean (checked 4) and the r55 record section resolves 13/13
  (`records/record-audit-green-r55.txt`). No frozen byte edited; the r55 freeze-era red
  demo stays red; the r56 texts stay true at the revs they cite.
- **R3/R4 (the W04 item):** `records/w04-supersedes-probe.txt` — the fleet census script's
  committed bytes (sha256 `3fb72615…4a64e30`, byte-identical at both fleet heads read this
  round) carry the `supersedes S[0-9]{3}` guard in the E04 branch only; the W04 branch
  tests neither status nor supersedes. The routed "census-safe W04 supersedes set" is the
  empty set as named; the 19 standing warnings are dispositioned row-by-row (first holder
  named) in `records/w04-disposition.tsv`. W04 stays named debt (19 at both census ends).
- **R58-C2:** at the base the routed drift census cannot run — `census3.py --check` exits 2,
  `registry row must have seven cells` (`.ufo/waves/round-58/l1/scores/c2-before.txt`): the
  r55 `v6-block-digest.py` registry row's purpose cell used the GFM-escaped pipe, which the
  frozen parser's plain-pipe split reads as eight cells. The repair is data-side only
  (S258 grounds the side; the parser stays frozen): the fragment reworded to
  "table-pipe-leading", SKILL delta exactly one line (`git diff --numstat 37e49cf3… --
  SKILL.md` → `1  1`), 63 rows / 0 malformed, `--generate` at the landing derives 63 paths,
  `--check` at the record commit `536c48650a5ccc435387b2060638a9d8a4bebf44` exits 0 exact
  (`records/census-check-at-record.txt`). Historical mode stays exit 1 (frozen census2, the
  r51 authority note — reported as-is); v6 triage-table digest `946e5359…` byte-identical
  base→landing (no-harm, `records/historical-and-v6-noharm.txt`).
- **Self-caught incidents, disclosed in-round:** **M58-1** — the first two helper calls
  (`634d12d6…` / `9e8ee220…`) were invoked with absolute Windows paths; the helper resolves
  repo-relative, so both attempts landed base-tree + one bogus empty `C:` directory and NO
  payload. Caught by the immediate diff-tree re-derivation; both are ancestors of main and
  pushed, disclosed in LOG/container/FREEZE, never cited as evidence; the recovery freeze
  `37e49cf3…` carries every intended path and removes the bogus `C:` entry. **M58-3** — the
  first orphan census run string-compared git's default-quoted listing against raw worktree
  names and reported two COMMITTED non-ASCII round-39 fixture paths as worktree-only;
  re-run with `-c core.quotepath=off` both resolve (2 and 2); the true orphan count is 3;
  corrected before anything acted on the false orphans. **E11 catch** — the round-end census
  caught this round's own S258 used-by drafting defect (an unresolvable annotation token in
  the cell); corrected to the bare comma-separated path form, landing with the close
  (`census-end.txt` carries both runs). **Post-close correction (disclosed, `d16bb470…`)** —
  the close entry's tip-audit count was written from arithmetic ("named 23"); the observed
  runs are `named 18, missing 5` at the record rev and `named 18, missing 0` at the tip;
  corrected with both runs pasted (the M57-1 class, caught immediately post-close).

## Landed changes

| commit | contents | LOG.md |
|---|---|---|
| `634d12d622e71f51c604704dfef66c88091ed441` | helper attempt (absolute paths): landed base-tree + bogus empty `C:` dir, NO payload — M58-1, disclosed, never evidence | (entry landed with the recovery freeze) |
| `9e8ee220ce399fa11b23e1617862e3247d993491` | helper attempt (same defect): same shape — disclosed | (entry landed with the recovery freeze) |
| `37e49cf33537ff182265c42f3fa546b1c0c0c0fa` | **operative freeze (recovery)**: plans/round-58-claims.md, claims.json, FREEZE, census-start, c1-before, c2-before, orphan-census, receipt-audit-sweep, w04-supersedes-probe, w04-disposition.tsv, s258/ (gfm.html + digests), LOG declaration+freeze+recovery entries, bogus `C:` removed (13 paths, diff-tree verified) | declaration, freeze, and recovery entries |
| `05865b6d63b43b6f732e9013c86980d79ddcb52c` | **landing**: the sweep-named receipt lands byte-identically at the r55 path (A), SKILL registry row reword (1 line), LOG landing entry carrying R1's correction note (3 paths) | landing entry |
| `536c48650a5ccc435387b2060638a9d8a4bebf44` | **record**: SCORECARD round-58 section, lesson round-58 (Gate + M58-1..M58-3), SOURCES S258 (164→165), ledger row round-58, gate-preflight receipts, record-audit-green-r55, historical-and-v6-noharm, census58-at-landing.json (10 paths) | record entry |
| `3e1dc2db8c760b63bed79d87f49ec823ebe82544` | **close**: S258 used-by E11 correction, c1-after, c2-after, census-check-at-record, gate-landing receipts, census-end receipt, LOG close entry (8 paths) | close entry |
| `d16bb4703440531e45d54562ca32f633f7d27e70` | **post-close correction (disclosed)**: the close entry's tip-audit count corrected to the observed named 18 missing 0 | correction entry |

Base→tip deltas: LOG 50/0 (append-only), SCORECARD 85/0, SKILL 1/1, SOURCES 1/0,
PROVINCE empty, owned-axes rows byte-equal (sha256 `f5da8986…` at both ends).

## Before → after measurements

- **R58-C1 (calibration).** Before at the base `42c794af…`: `git show 42c794af…:LOG.md |
  grep -c '27 distinct filesystem paths'` → 0; `git ls-tree -r --name-only 42c794af… --
  .ufo/waves/round-58/ | wc -l` → 0; the sweep names `RECEIPT_ABSENT
  freeze-gate-tip-90f3a9b9.json` in round-55 scope (receipt
  `records/receipt-audit-sweep.txt`). After at the landing/record: the marker probe → 1
  (`scores/c1-after.txt`, rev `536c4865…`); `git ls-tree -r --name-only 05865b6d… --
  .ufo/waves/round-55/l1/scores/ | grep -c 'freeze-gate-tip-90f3a9b9.json'` → 1;
  `receipt-audit.py --claims .ufo/waves/round-55/claims.json --rev 05865b6d…` → clean,
  checked 4; `record-receipt-audit.py --record SCORECARD.md --heading "Round 55" --rev
  05865b6d…` → named 13, missing 0 (`records/record-audit-green-r55.txt`). Measured at
  `05865b6d…` / `536c4865…`.
- **R58-C2 (depth).** Before at the base: `python -X utf8 -I -B tools/round-51/census3.py
  --root . --rev 42c794af… --check` → exit 2, `registry row must have seven cells`
  (`scores/c2-before.txt`; selftest 20/0 — instrument healthy, data broken). After at the
  record commit: the same `--check` form against the committed generated inventory →
  exit 0, registry 63 / census 63, outside [], unregistered [], duplicates []
  (`scores/c2-after.txt` + `records/census-check-at-record.txt`, rev `536c4865…`); selftest
  20/0 at the unchanged pin `a7538e5f…`. Measured at `536c4865…`.
- **Gates:** pre-flight at the operative freeze → audited 33, clean 13, round-58 CLEAN,
  disclosures 32/33 exact + missing [round-58] (exit 1 honestly printed,
  `scores/gate-preflight.txt`); landing at the record commit → exit 0, audited 33, clean 13,
  disclosures 33/33 exact, round-55/56/57/58 all CLEAN (`scores/gate-landing.txt`).

## Sources & frontier

SOURCES rows before→after: `grep -c '^| S' corpus/SOURCES.md` → 164 at the base, 165 at
the tip (the S258 insertion; counting command also in the census receipts:
`sources-rows=164` start, `sources-rows=165` end). S258 (GitHub Flavored Markdown Spec,
tables extension, tier A spec, opened this round with curl; snapshot
`.ufo/waves/round-58/l1/s258/`, sha256 `b153d814fdfc8624bb6da7449162c1cd707a637f7d1c1b636eb44b9cf63fa220`;
located quote, 15 words: "Include a pipe in a cell's content by escaping it, including
inside other inline spans:") — mined: grounds M58-2's writer/reader grammar conflict and
the repair side (data into the reader's grammar; the parser stays frozen). Its used-by
targets landed in the same commit as the row (the M53-4 rule); the row's used-by cell was
corrected once this round (the E11 catch, disclosed). Census: start exit 0 (19 standing
W04, 164 rows — `.ufo/waves/round-58/l1/census-start.txt`); end exit 0 (19 standing W04,
165 rows — `census-end.txt`, run 1 at the record state honestly shows the E11 the census
caught, run 2 is the round-end state; exit 0 re-derived at the pushed tip at filing:
rc=0, 19 W04). The literal census name form exits 2 on this host (disclosed since r53);
the host-adapted explicit-dir form is used. Frontier: no PROVINCE move this round
(expansion unchanged); W04 stays named debt with the routed item closed
vacuous-as-named.

## Trend verdicts

- **expansion: unchanged** — PROVINCE diff empty base→tip (no Frontier→Core move);
  S258 grounds a writer/reader grammar boundary in tooling formats, not an REA surface;
  no new knowledge-surface entries.
- **quality: improved** — the lane's named-absent evidence count drops 1 → 0 with the
  byte-identical receipt landing (the r55 container and record section now fully resolve);
  a registry unparseable by its own drift census for three rounds parses again and
  re-enters that census with an exact-equality green; the routed W04 item resolves to its
  precise truth with per-row dispositions; the R29 gate audits the freeze CLEAN and the
  landing 33/33; every filed text outside the round's own appends is byte-identical.
- **discernment: unchanged pending the outside spot-check** — the round executes the
  routed list verbatim, self-caught its own helper incident (M58-1) before any payload-less
  state was cited, corrected its own census before filing (M58-3), let the end-census catch
  its own S258 drafting defect, and corrected its own close-entry count from observed
  output post-close — consistent with improved, but the outside non-author check decides
  (LEARNING.md); not self-certified.

Assimilation: none — `considerthese/` does not exist in this lane (measured at round
start); the shokuknow register is unreachable from this host. Assimilation: none —
shokuknow unreachable.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources —
  resolvable pointer: the instrument-registry v2 block parses 63 rows / 0 malformed at the
  tip (`python -X utf8 -I -B tools/round-51/census3.py --root . --rev d16bb470… --check
  --census .ufo/waves/round-58/l1/records/census58-at-landing.json` → exit 0); the v6
  triage-table digest `946e5359…` re-derives (`records/historical-and-v6-noharm.txt`).
- [~] At least one end-to-end domain task executed and logged in LOG.md — resolvable
  pointer: this round's routed-duty execution, logged in the round-58 LOG entries with
  receipts under `.ufo/waves/round-58/l1/` (the sweep → named finding → byte-identical
  repair → green audits, all on committed bytes).
- [~] Instructions executable by an agent without oral context — resolvable pointer:
  every probe this round is a pasteable command with observed output in the committed
  receipts (`scores/c1-before.txt`, `scores/c2-before.txt`, `records/*`), re-derived by
  plain git/python one-liners.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — resolvable pointer: PROVINCE
  diff empty base→tip (`git diff 42c794af… d16bb470… -- PROVINCE.md` is empty); S258
  recorded as spec documentation, not an REA surface.

(SHONEN.md itself stays byte-identical to the canonical template; the boxes carry `[~]`
here with the pointers above, not `[x]` — no non-author verifier has checked them.)
