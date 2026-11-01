# souji round 50 report (2026-11-01, Windows host)

Lane repo `fleet/shokunin-repo-hygiene`, branch master. Round base
`5f921fe261770b68266793c767d35a56758536c5` (the r49 non-author verifier
spot-check commit; verdict `ok, admitted`). Lane commits this round, all by
the index-free plumbing helper and pushed: freeze
`3cc69c455d000c4d6fc71031e081f15882a97ffd` (prereg + counters + populations
+ controls + pre-flight receipts, ONE commit, before any claim receipt;
freeze-check `SUMMARY claims=2 findings=0`, exit 0 at the freeze BEFORE
building), content `6d94929f07a2ef25def2e603b6f1ce38298b9a63`, end receipts
`6683497581f7423495f833c8795d5d93d4cad3e3` (= final tip; `git ls-remote
origin refs/heads/master` identical — pushed).

## Work performed

- **C1 (calibration 7 — the lowest non-retired axis): the S267 token
  readings re-derivable by committed command** (r49 non-author closure
  routed item 2). The r49 S267 re-open receipt stated "zero occurrences of
  'factual' and zero of 'histor*'" — exact at the page-CONTENT scope, not
  at the RAW-BYTES scope (exactly one footer occurrence: "History and
  License", inside the docs-page site-chrome footer div) — and no committed
  command could re-derive either reading. Landed: the counting instrument
  `tools/souji-page-token-count.py` (raw = case-insensitive byte-prefix
  count over the exact page bytes; content = HTML text content via
  `html.parser` with character references decoded per S273;
  script/style/header/nav/footer and class~=footer elements excluded —
  site chrome; every record carries the METHOD line; `--selftest` 8/8), the
  committed page capture `census/round-50/sources/s267-stdtypes-capture.html`
  (814236 bytes, sha256 `0a9474e3…f5d3`, byte-identical to the r49 live
  fetch), the counting receipt
  `census/round-50/sources/s267-reopen-count-receipt.txt` (method + command
  + output pasted, per the r49 verifier's routed fix), and the append-only
  `S267-COUNT-ERRATUM` line (column 0) in `corpus/lessons/round-50.md`.
  Grounded on **S273** (Python html.parser `convert_charrefs` contract,
  opened live 2026-11-01). Evidence: frozen counter
  `census/round-50/c1-counter.py`; control
  `census/round-50/controls/c1-control-donothing.txt` (red at base);
  tip receipt `census/round-50/records/c1-tip-50.txt`.
- **C2 (operability 8 — capability acquisition): census receipts that
  verify** (r49 closure routed item 1, instrument side). The contract
  mandates a census before→after every round; on this host those receipts
  were raw text with no binding. Landed: `tools/souji-census-receipt.py`
  — `capture` wraps the r48 adapter and emits a digest-bound v1 receipt
  (header keys, RECEIPT-SHA256 over every byte above it, the adapter's raw
  output embedded verbatim; the conf form's raw rc-2 verdict disclosed
  inside, never masked); `verify` re-derives every header value from the
  embedded raw output and re-hashes both scripts (named refusal classes:
  RECEIPT-MALFORMED / -DIGEST-MISMATCH / -RC-INCONSISTENT /
  -COUNT-MISMATCH / -SCRIPT-DRIFT / -ADAPTER-DRIFT); `--selftest` 6/6 with
  five tamper/malform arms each asserting its exact class; `--out` refused
  at/inside the lane root (the r48 receipt-staging discipline, now
  enforced by the tool). First receipt:
  `census/round-50/records/census-before-receipt.txt`; after receipt
  `census/round-50/records/census-after-receipt.txt`; both `verify ok`
  over all checks incl. adapter-sha and fleet-script-sha. Non-claim side
  of the same routed item: an appended, append-only **L0 proposal line**
  (fleet root `.ufo/l0-questions.md`) consolidating the r48 census-form
  question with the cross-lane lineage (revenger r79 same shape) and a
  concrete option set — operator-owned; routed around; nothing assumed
  answered. Evidence: frozen counter `census/round-50/c2-counter.py`;
  control `census/round-50/controls/c2-control-donothing.txt` (red at
  base); tip receipts `census/round-50/records/c2-tip-content-50.txt` and
  the final-tip run quoted below.
- Frontier step (2b): SOURCES row **S273** appended (196 → 197);
  standing reject **S267** re-opened again WITH the counting method named
  (rejection holds; no row cell changed); reject sample stated explicitly
  (one new source opened, zero new reject rows — the sweep is the
  two-fetch inventory in the lesson Gate).
- Mistake mining (lesson `corpus/lessons/round-50.md ## Mistakes`): three
  rows, each with evidence and a same-round executed fix — (1) the
  phantom-space quote-count class (tag-strip with space substitution made
  the located quote a non-substring; display-faithful stripping is the
  standing command shape; fourth occurrence of the quote-counting class,
  first where the method itself was wrong); (2) the shared-file
  tamper-arm pollution class (selftest arms mutated one shared receipt in
  sequence so classes fired for the wrong reason; fixed by restoring clean
  bytes before every arm); (3) the numbers-without-listing receipt class
  (the first NTFS take carried bare counts 7/0 instead of the six quoted
  paths; re-taken as listing + count + command). Also disclosed: the
  pre-freeze feasibility round (synthetic-tip runs) exposed two counter
  defects — the extracted tool's lane-root TMPDIR refusal and the
  erratum-leg column-0 requirement — both fixed in counter/lesson bytes
  before the freeze; the classes are the mined rows.
- Standing practice: NTFS exclusion set re-derived at base and tip (6
  paths, not widened); the inherited integrator-landing drift repaired at
  the final tip by the committed fail-closed tool only; the r46
  landing-suite counter re-derived at the final tip.

## Landed changes

| change | commit |
|---|---|
| freeze: `census/round-50/preregistration.txt` (2 claim blocks, freeze-check green at this commit), `c1-counter.py`, `c2-counter.py`, `c1-arms.tsv`, `c2-arms.tsv`, `c1-footer-fixture.html`, `c1-body-fixture.html`, controls `c1-control-donothing.txt` / `c2-control-donothing.txt` (red, exit 1, TOOL-ABSENT at base), records `census-before.txt` + `census-before-receipt.txt` + `porcelain-at-base.txt` + `ntfs-exclusion-check-base.txt` + `idx-repair-base-refused-50.txt`, sources `s267-stdtypes-capture.html` + `s273-htmlparser-page.html` + `s273-htmlparser-located-quote.txt` + `s267-reopen-count-receipt.txt` | `3cc69c455d000c4d6fc71031e081f15882a97ffd` |
| content: `tools/souji-page-token-count.py`, `tools/souji-census-receipt.py`, `corpus/lessons/round-50.md` (Gate + S267-COUNT-ERRATUM + 3 Mistakes + admission distinction), `corpus/SOURCES.md` (provenance line + S273 row), `SCORECARD.md` (r50 landing section + capability row + planned r51), `LOG.md` (round-50 entry), `SKILL.md` (Round 50 contracts: two rules + two registry rows) | `6d94929f07a2ef25def2e603b6f1ce38298b9a63` |
| end receipts: `census-after.txt` + `census-after-receipt.txt` + `census-after-verify.txt`, `c1-tip-50.txt`, `c2-tip-content-50.txt`, `c1-suite-tip-50.txt` (the honest refusal at the staged state, disclosed), `freeze-check-at-content-tip.txt`, `ntfs-exclusion-check-tip.txt` | `6683497581f7423495f833c8795d5d93d4cad3e3` |

LOG.md round-50 entry carries every item above; no entry without a commit
and no commit outside the lane remote.

## Before → after measurements

- **C1 (calibration).** Counting command:
  `python -B census/round-50/c1-counter.py --root LANE --rev FULL40 --scratch DIR`.
  Before (base `5f921fe2…`, control committed at the freeze):
  `PRISTINE FAIL TOOL-ABSENT tools/souji-page-token-count.py at 5f921fe261770b68266793c767d35a56758536c5`
  / `SUMMARY reading=FAIL footer=FAIL body=FAIL erratum=FAIL sourced=FAIL
  selftest=FAIL tool_sha=absent`, **exit 1**. After (content tip
  `6d94929f…`, receipt `census/round-50/records/c1-tip-50.txt`):
  `SUMMARY reading=ok footer=ok body=ok erratum=ok sourced=ok selftest=ok
  content_histor=0 raw_histor=1 content_factual=0 raw_factual=0
  tool_sha=5923b315fe6f`, **exit 0**. The SAME counter bytes measure both
  ends (r45 different-instrument limit structurally avoided). Reading
  command behind the headline: `python -B tools/souji-page-token-count.py
  --capture census/round-50/sources/s267-stdtypes-capture.html --token
  histor` → SCOPE-CONTENT-MATCHES=0, SCOPE-RAW-MATCHES=1; `--token
  factual` → 0/0.
- **C2 (operability).** Counting command:
  `python -B census/round-50/c2-counter.py --root LANE --rev FULL40 --scratch DIR`.
  Before (base, control): `PRISTINE FAIL TOOL-ABSENT … tool_sha=absent`,
  **exit 1**. After at the content tip (`census/round-50/records/
  c2-tip-content-50.txt`): `SUMMARY receipts=1 verified=1 selftest=ok
  before=ok tool_sha=1d092142eb73`, **exit 0**. After at the FINAL tip
  `66834975…` (receipt quoted from session scratch, the terminal landing
  cannot carry its own receipt): `receipts census-after-receipt.txt rc=0
  ok; census-before-receipt.txt rc=0 ok` / `SUMMARY receipts=2 verified=2
  selftest=ok before=ok tool_sha=1d092142eb73`, **exit 0**. Tamper
  evidence: the tool's selftest refuses five tampered/malformed receipt
  shapes, each at its named class (`SELFTEST cases=6 pass=6 fail=0`).
- **Census before→after (2b, mandatory).** Round start, raw adapter form
  (`census/round-50/records/census-before.txt`, rc 0): 67 lines, **59
  W04** duplicate-url warnings, `shokunin-repo-hygiene	ok	…/corpus/SOURCES.md`,
  final line `CENSUS-RUN lane=souji conf_rc=2 dir_rc=0` — the conf form's
  raw `souji missing` rc-2 verdict recorded verbatim inside (the
  documented host state). Round end (`census/round-50/records/
  census-after.txt`, rc 0 via the after-receipt's verbatim embedded
  output): 67 lines, **59 W04** (S273's URL is new — no new duplicate
  warning), same ok line, `CENSUS-RUN lane=souji conf_rc=2 dir_rc=0`.
  **Exit 0 at round end: held.** Both ends also captured as digest-bound
  v1 receipts (`census-before-receipt.txt`, `census-after-receipt.txt`);
  each `VERIFY ok … checks=grammar,digest,raw-section,rc,w04,result,
  adapter-sha,fleet-script-sha adapter=ok`, exit 0
  (`census-after-verify.txt` committed for the after end).
- **Standing receipts at the final tip `66834975…`** (session-scratch
  receipts, quoted here because the terminal landing cannot carry its own
  receipt): r46 landing-suite counter → `SUMMARY assertions=550
  mismatches=70 registered=70 corrected=0 exempted=0 unfiled=0
  instrument_sha256=a3324916…9831`, **exit 0** (548 → 550: the two new r50
  SCORECARD assertions, all registered); freeze-check over the round
  prereg → `SUMMARY claims=2 findings=0`, **exit 0** (also committed at
  the content tip: `census/round-50/records/freeze-check-at-content-tip.txt`).
  The suite's content-tip attempt read `COULD-NOT-EVALUATE dirty worktree
  at run time: 31 unexpected rows`, exit 2 (the staged end receipts + the
  helper-landing drift) — committed as
  `census/round-50/records/c1-suite-tip-50.txt`; the run belongs after the
  terminal repair, exactly the r48/r49 ordering practice.
- **Worktree integrity.** The terminal idx-repair at the final tip
  (`python -B tools/souji-idx-repair.py --root . --rev 66834975…`): exit 0,
  AFTER rows = exactly the 6 tolerated NTFS paths; final
  `git status --porcelain` = 6 rows, nothing else. The base repair attempt
  was refused fail-closed mid-round (14 unexpected rows — the round's own
  in-progress files; receipt `census/round-50/records/
  idx-repair-base-refused-50.txt`); the repair lands once, after the last
  landing, per the r48/r49 practice.

## Sources & frontier

`grep -cE '^\|\s*S[0-9]{3,}\s*\|' corpus/SOURCES.md` → **196** at the
round base → **197** at the tip. New row: **S273** (Python html.parser —
https://docs.python.org/3/library/html.parser.html — opened live
2026-11-01, curl -sSL HTTP 200, no redirect, 55260 bytes, sha256
`13ba271c…77f4`; full-page capture `census/round-50/sources/
s273-htmlparser-page.html`; located quote, 20 words counted by the pasted
command with display-faithful tag stripping: "all character references
(except the ones in elements like script and style) are automatically
converted to the corresponding Unicode characters"; used-by
`corpus/lessons/round-50.md`). Standing reject **S267** re-opened with the
counting method named (receipt `census/round-50/sources/
s267-reopen-count-receipt.txt`; page byte-identical to the r49 fetch,
sha256 `0a9474e3…f5d3`; content histor=0 / raw histor=1 / factual 0/0;
rejection HOLDS). No existing row's status/recheck/used-by cell changed.
The sourced-claim requirement is carried by **C1 resting on S273** (the
content scope's character-reference decoding).

## Fresh-start rulings (round prompt §7)

The last three REJECTED closures were re-read and spot-checked before
anything was declared:

- **r43 rejected-honest-stop** — shape: formal preregistration landed
  after ready handoff (irreversible timing defect) and counters that could
  not bind their captured derived tokens. Ruled out by: prereg +
  counter + population + controls + pre-flight receipts in ONE freeze
  commit (`3cc69c45…`) before any claim receipt existed, with the
  freeze-check green at that commit before any content landed; every
  counter value is parsed from the instrument's own emitted grammar at a
  named revision (no captured-token binding gap).
- **r44 rejected-honest-stop** — shape: a frozen predicate honest work
  could not meet (the natural register stayed red because tuple
  identities disagreed inside the frozen counter). Ruled out by: deriving
  every target from a state the base honestly exhibits (blob absence at
  the base — the do-nothing controls' red is the base's own state, not a
  predicate the base cannot express) and from the routed defect's own
  named fix; plus a pre-freeze feasibility leg that ran both counters
  green over a synthetic tip containing exactly the claimed bytes (the
  target is reachable by the declared work).
- **r45 rejected-honest-stop** — shape: the different-instrument limit
  (0-to-green by swapping instruments) and an L2 floor unmet by operator
  wrap-up. Ruled out structurally: the SAME counter bytes measure both
  arms of each claim (only the committed world moves); the L2 floor is
  again routed around with disclosure (no dispatch surface on this host;
  dispatched=0/completed=0/dead=0; no WAVE-DONE claimed; standing L0
  questions; nothing assumed answered).

## Trend verdicts

- **expansion: unchanged** — no `corpus/knowledge/` entry, no Core
  promotion, no PROVINCE change, no new province surface; SOURCES 196 →
  197 (one docs row on an already-held docs-host pattern; the +0 W04 is
  because S273's URL is new, disclosed in the census lines above). C2's
  capability row grows the repertoire on existing Core ground (the census
  surface), not new ground; coverage stays 8.
- **quality: improved** — the census receipt class (a contract-mandated
  artifact every round) is upgraded from raw captures to digest-bound,
  tamper-refusing, script-drift-detecting receipts whose verify re-derives
  every value from committed bytes (counter green at content tip and final
  tip); the token-count instrument makes a standing record reading
  re-derivable at two named scopes with the method in every record
  (counter green); both tools' selftests refuse their negative controls.
  The numeric operability score stays 8 (no reproducible 0–10 mapping);
  the capability row is the r50 entry.
- **discernment: improved** — three mistakes mined with same-round
  executed fixes (evidence in the lesson); the pre-freeze feasibility
  round caught two counter defects BEFORE the freeze (the extracted-tool
  TMPDIR layout and the erratum column-0 requirement) instead of after
  scoring; fresh-start rulings re-derived against r43/r44/r45 (above);
  the S267 erratum names its own counting method and pastes the command —
  the exact fix the r49 verifier routed; the Gate states its reject
  sample; falsifiability: both claims' controls are red at the base and
  both greens re-derive at the tips from committed bytes.

## Assimilation

No `considerthese/` directory exists in the lane repo (named-path check at
round start). Assimilation: none — shokuknow unreachable.

## L0 / L2 notes

One appended, append-only line in the fleet root `.ufo/l0-questions.md`
(`souji | round-50 | …`): the consolidated census conf-form proposal
(carried since r48; revenger r79 same shape; options (a) fix the fleet
script's lane-dir resolution on this host layout, (b) ratify the
explicit-lane-directory form + adapter + receipts as the standing contract
form for host-migrated lanes, (c) keep the per-round dual receipt). Routed
around; nothing assumed answered. L2 floor: no dispatch surface on this
host; dispatched=0, completed=0, dead=0; standing L0 questions
(round-44 symlink contract, round-46 L2 floor, round-46 staged package,
round-48 census-form routing) routed around; no WAVE-DONE claimed.

Holds unchanged: certification OFF, K5 HELD, NAMESPACE/reap holds.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources —
  SKILL.md Decision tables/Error patterns/Checklists/Gate registry + the new Round 50 contracts
  section (scope-named counting; digest-bound census receipts); corpus/SOURCES.md S273 (r50) beside
  S100–S103; corpus/lessons/round-50.md Gate
- [~] At least one end-to-end domain task executed and logged in LOG.md —
  LOG.md round-50 entry: the round-contract census executed both ends and
  captured into verifiable receipts (census-before-receipt.txt /
  census-after-receipt.txt, verify ok each); LOG.md:362 operator sweep receipt stands
- [~] Instructions executable by an agent without oral context —
  census/round-50/preregistration.txt + c1-counter.py + c2-counter.py +
  controls re-derive both claims from committed bytes at named revisions
  (control red at base, green at tips, receipts committed); the r21
  acceptance matrix stands
- [~] No cross-domain bleed (PROVINCE.md still accurate) —
  PROVINCE.md untouched this round (absent from the range diff
  5f921fe2..66834975); the conf-form host state stays disclosed, never
  masked; the L0 proposal routes the operator decision instead of
  absorbing it

No box claims `[x]`: no non-author verifier has re-derived this round
yet; every pointer above resolves from committed bytes.
