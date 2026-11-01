# revenger — round 77 report (hyaku run 16)

## Work performed

Carry-in (addressed first, all three from the r76 non-author closure, status-neutral):

- **Item 1 — census literal-command layout defect.** Re-ran both forms before
  writing anything: the closure contract's literal `sources-census.sh validate
  --root <fleet root> revenger` → **exit 2** (`revenger missing …
  revenger-shokunin/corpus/SOURCES.md` — a lane id resolves to
  `<root>/<id>-shokunin/`, the old-host layout); the sanctioned explicit
  lane-dir form → **exit 0** (31 disclosed W01/W04 warnings, final `ok
  …/fleet/shokunin-binary-forensics/corpus/SOURCES.md`). The sanctioned
  invocation form is now recorded **next to the old-host literal** in
  `SKILL.md` §4a, with both real outputs; the operator-side item itself stays
  routed (r74/r75/r76 lineage). Evidence: `SKILL.md` §4a;
  `corpus/lessons/round-77.md` §Census.
- **Item 2 — the scratch-probe leg, committed (became claim C2).** Both
  provider-gate payloads reproduced live on this host and committed as exact
  producer stdout bytes plus an L1 receipt:
  `corpus/live/runs/round-77/provider-gates/{android-gate.json,firmware-gate.json,receipt.json}`;
  machine-checked per leg by the new `reports/round-77/gate_probe.sh`
  (criterion G) with a mutated-copy negative control. Evidence:
  `reports/round-77/gate-after.log`; S448.
- **Item 3 — two cosmetic wording notes, applied.** (a) the f_probe
  two-decimals score representation (`8.75` vs the r71 counter's `8.8`)
  noted wherever this round quotes F scores (SCORECARD F row; mapping
  AST-verified equal by the r76 spotcheck); (b) the kebab-coverage note —
  all 8 F families have manifest aliases **including `inspect-pe-resources`**
  (unlisted in S445); only `inventory_artifact` lacks an alias — recorded in
  `corpus/lessons/round-77.md` §Carry-in; S445 left byte-untouched
  (append-only registry). Evidence: `corpus/lessons/round-77.md`.

Declared claims (frozen at `5acef36f`, before any after-run):

- **C1 — coverage, criterion F (selected-family record presence):
  browser-runtime.** The r76 routed blocker ("browser needs a caller-supplied
  CDP endpoint") was re-derived first: in REA's usage the caller is whoever
  invokes the CLI, and this host already carries Chrome/156.0.8078.74 (Edge
  present too; nothing installed or updated). Authored
  `corpus/fixtures/browser-r77/` (two inert static files — the committed
  bytes are the source of truth, no generator; `truth.json` pins authored
  anchors, the run pin, and a volatile-not-compared list; `oracle_check.py`
  re-hashes fixture premises on every run), served the committed bytes on
  loopback `http://127.0.0.1:8477`, launched a scratch-profile headless
  Chrome bound to loopback CDP `http://127.0.0.1:9333`, then ONE real
  `rea inspect-web-page` run (rea 6.8.0, built-in `rea-cdp-browser`, exit 0,
  3.498 s, stderr empty), saved as producer-emitted bytes at
  `corpus/live/runs/round-77/` with receipt + LEDGER; identity oracle
  **`ORACLE OK (17/17 checks)`**, including both
  `cdp_hash == sha256(authored script text)` bindings — the producer's own
  content hashes bind the record to the committed bytes. Evidence:
  `reports/round-77/f-after.log`, `oracle-after.log`; S447.
- **C2 — calibration, new bounded criterion G (provider-gate payload
  receipt fidelity).** The committed receipts + probe described in carry-in
  item 2; red-before over the base archive (`gate-red.log`: receipts absent,
  exit 1), green after (`gate-after.log`: LEG0 yes / LEG1 android-match /
  LEG2 firmware-match / LEG3 mutated-copy flagged, exit 0). Android stays
  uncovered, honestly: its gate demands the caller-supplied
  `REA_JADX_MCP_JAR` (jadx-headless-mcp 0.7.1), absent here — now a
  committed receipt, not scratch. Evidence: `reports/round-77/gate-after.log`.

Fresh-start §7 spot-check (the three rejected closures re-read this round;
r71/r72/r73 MANIFEST verdict rows + lane SCORECARD sections): **K-map
admissions (C05/C15)** ruled out — every path requires the wave Q-review
surface, absent on this host (r74 L0 re-checked, still unanswered); **C10**
ruled out — disposed `rejected` by the frozen kill rule in r74;
**r73 C1** ruled out — unresolved by wave release, its pin is the
r74-disposed candidate. Declared claims are reachable by neither a
do-nothing control nor those routes.

Round shape: L1-only (no L2/AgentSwarm dispatch surface on this host; r74 L0
stands, re-checked, unanswered; receipts are L1-authored and disclosed — the
oracle and probe re-derive every verdict from committed bytes). No tool
installed or updated. No new L0 filed (the open r74 L0 covers the dispatch
class; the android jadx-JAR need is recorded as a routed surface in
PROVINCE.md, S448 and the claims, not as a blocking question). considerthese
reviewed (`2026-10-28.md`, 5 proposals): **proposal 3 adopted** — K is now
reported as two numbers (held rows vs rows: **8 held of 15 rows**; frontier
rows named: C05 uncovered, C10 partial, C15 uncovered) in the SCORECARD K row
and this report, closing the r72 denominator-effect ambiguity the verifier
had to correct; proposals 1/2/4/5 not adopted.

## Landed changes

| change | LOG entry | commit |
|---|---|---|
| freeze: claims + sha-pinned probes + red-befores | round-77 entry (freeze via claims.md) | `5acef36fe6cd473308bd57ec103372a2cc17ac4a` |
| landing: browser-r77 fixture (4 files) + round-77 run (7 files incl. provider-gates) + S447/S448 + lesson + PROVINCE browser record + SKILL §4a sanctioned census form | round-77 entry (C1/C2/carry-in lines) | `071de56028ed32180b210c1559eda9ece99ec132` |
| adjudication: SCORECARD section, LOG entry, after/separability/noharm/census/p2 receipts | round-77 entry (holds/trends lines) | `95e6816f192c5230eb12dd3730230070ca2dc2ec` |
| tip receipt: f_probe re-run at the final tip | (receipt only) | `942f42963c9bc7e5f0773b799a9cc9c9b436d906` |

All cited shas are ancestors of pushed `origin/main` = `942f4296…6d906`
(merge-base + ls-remote verified). Mandated post-commit diff checks: freeze 4
files, landing 15 files, adjudication 10 files, tip receipt 1 file — all
non-empty and exactly the intended paths.

## Before → after measurements

- **C1 (F):** `PYTHONUTF8=1 python -B reports/round-76/f_probe.py
  <git-archive tree>/corpus` — before (`f-red.log`, archive of `3e980481`):
  `F_COVERAGE=6/8 score=7.50`, `F_FAMILIES=['archives', 'evm', 'firmware',
  'javascript', 'managed', 'native-static']`; after (`f-after.log`, archive
  of `071de560`; re-run at the final tip `942f4296`, same output,
  `tip-verification.log`): **`F_COVERAGE=7/8 score=8.75`**, `F_FAMILIES` +=
  `browser-runtime`. Disclosed histogram delta vs red: exactly
  `inspect_web_page: 1` (the family record) and `list_browser_targets: 1`
  (discovery aux; in no family set). Note (r76 spotcheck item 3a): f_probe
  prints two decimals; the r71 frozen counter prints one (`8.8`) —
  representation-only, mapping AST-verified equal. Measured commits
  `3e980481` → `942f4296`. Oracle on the committed record:
  `ORACLE OK (17/17 checks)` (`oracle-after.log`, run from the committed
  archive tree).
- **C2 (criterion G):** `bash reports/round-77/gate_probe.sh` — before
  (`gate-red.log`, over the base archive): exit 1,
  `GATE_LEG0_RECEIPTS_PRESENT=no`, `GATE_VERDICT=red`; after
  (`gate-after.log`): exit 0, LEG0 yes, `GATE_LEG1_ANDROID_MATCH=1`,
  `GATE_LEG2_FIRMWARE_MATCH=1`, `GATE_LEG3_NEGCTL_FLAGGED=1` (a mutated
  `details.operation` copy is flagged by the same comparator that passes the
  committed bytes), `GATE_VERDICT=green`. Same measured commits.
- **Separability:** C1-only tree (landing archive minus the provider-gates
  subtree and gate_probe) still prints 7/8 (`f-separability.log`); C2-only
  tree (all browser-r77 fixture/record bytes removed; the probe references
  zero browser-r77 paths — grep count 0) still green
  (`g-separability.log`).
- **Holds:** FRESH_ROWS 18/18 (exit 0); P2 rerun after the PROVINCE edit:
  `P2_SURFACES_RESOLVED=11/11 UNRECORDED_ABSENT=0 STALE_RECORDS=0
  P2_SCORE=10.0` exit 0 (`p2-rerun.log` — the frozen probe's fixed token
  list does not see the new record by construction; wiring it into a future
  P revision is routed); no-harm diff — protected paths (knowledge, README,
  verifiers, SHONEN, LOG, SCORECARD, r71 counter, r76 f_probe) empty on
  `3e980481..071de560` (`noharm-diff.txt`); K untouched (no README/knowledge
  byte changed — blocked route, not attempted).

## Sources & frontier

`corpus/SOURCES.md` rows 446 → 448 (`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'
corpus/SOURCES.md` → 448): +**S447** (own-work tier A — the recorded
inspect-web-page record + fixture; grounds C1) and +**S448** (own-work tier
A — the committed provider-gate receipts + criterion-G probe; grounds C2).
Both opened this round; both claims are sourced claims. No existing row
changed in place. Census: round start — literal form exit 2, sanctioned form
exit 0 (31 W, disclosed W01/W04 classes, final `ok …/corpus/SOURCES.md`);
round end exit 0, same 31 warnings, final `ok`
(`reports/round-77/census-after.log`). Mistakes mined this round (three,
full table `corpus/lessons/round-77.md` `## Mistakes`): assumed observation
(script-source retention under late attach — caught by reading the producer
record before pinning expectations), incomplete red tree (instrument bytes
missing from the first red extraction — self-caught at the red-before),
surface-reachability premise inherited unexamined ("caller-supplied" read as
operator-supplied; re-derived from the tool's contract before any fixture
was authored).

## Trend verdicts

- **expansion — unchanged.** No knowledge entry admitted; K stays 8 held of
  15 rows (5.3) with C05/C10/C15 named; the F row's new record is evidence
  ground for an existing criterion (presence-only, routed debt r63), not a
  new domain surface — though the province census itself gained a true
  present-record (browser/CDP), which is PROVINCE accuracy, not a K move.
- **quality — improved.** A routed scratch-only evidence leg is now
  committed, per-leg machine-checked and negative-controlled (criterion G),
  and F's ground extended to a real current-producer browser-runtime record
  with byte-derived identity (producer cdp_hash == authored sha256).
- **discernment — improved.** The round's own routed-blocker premise
  ("caller-supplied = operator-supplied", this lane's r76 routing) was
  re-derived from the tool's contract before any fixture was authored; the
  corrected reading, the demonstration, and the still-genuinely-blocked
  android family (committed gate receipt) are recorded rather than smoothed
  over.

No axis harmed: K/FRESH/P2 holds green, no protected byte changed, no
verifier or gate touched, freshness hold intact.

CLOSURE-PREP: re-derive C1 by `git archive 942f42963c9bc7e5f0773b799a9cc9c9b436d906 corpus reports/round-76/f_probe.py`, extract, run `PYTHONUTF8=1 python -B <extracted>/reports/round-76/f_probe.py <extracted>/corpus` (expect `F_COVERAGE=7/8 score=8.75`), and `PYTHONUTF8=1 python -B <extracted>/corpus/fixtures/browser-r77/oracle_check.py <extracted>/corpus/fixtures/browser-r77/truth.json <extracted>/corpus/live/runs/round-77/inspection.json` (expect `ORACLE OK (17/17 checks)`); optionally reproduce live per `corpus/live/runs/round-77/receipt.json` (serve `corpus/fixtures/browser-r77` on 127.0.0.1:8477, headless Chrome with `--remote-debugging-port=9333`, `rea list-browser-targets`, `rea inspect-web-page … --allowed-origins http://127.0.0.1:8477`; a fresh run reproduces the oracle verdict, not the stdout bytes — volatile fields listed in truth.json). Re-derive C2 by `git archive 942f42963c9bc7e5f0773b799a9cc9c9b436d906 corpus reports/round-77/gate_probe.sh`, extract, run `bash <extracted>/reports/round-77/gate_probe.sh` (expect exit 0, LEG1/LEG2 = 1, LEG3 flagged, `GATE_VERDICT=green`; needs `rea` on PATH). Carry-in dispositions to check: `SKILL.md` §4a (sanctioned census form next to the literal), `corpus/lessons/round-77.md` §Carry-in items 1–3, and §carry-in of `reports/round-77/claims.md`.

## SHONEN

- `[~]` SKILL.md real decision tables/checklists — §4a gained the sanctioned
  this-host census invocation next to the old-host literal (executed this
  round: exit 2 literal, exit 0 sanctioned, both in the lesson); the box's
  non-lane re-confirmation debt on the CURRENT bytes stands (`SHONEN.md` box
  1; no outside verifier available this round).
- `[~]` At least one end-to-end domain task executed and logged —
  strengthened: a real end-to-end browser-runtime producer chain (serve
  committed bytes → loopback CDP → target discovery → passive inspect →
  17/17 identity oracle), logged (`corpus/live/runs/round-77/LEDGER.md`,
  `LOG.md` round-77 entry); L1-authored receipt disclosed.
- `[~]` Instructions executable without oral context — this round's probes
  ran verbatim from committed archive bytes (`gate-after.log`,
  `f-after.log`, `oracle-after.log`, `tip-verification.log`); no independent
  outside instruction verifier this round.
- `[~]` No cross-domain bleed — PROVINCE.md gained a dated in-province
  present-record (browser/CDP runtime evidence is core province; Q05 honored
  via the demonstrated run); `grep -c ADJ-06 corpus/README.md` = 0 unchanged;
  no cross-domain evidence absorbed.

Assimilation: considerthese `2026-10-28.md` proposal 3 adopted (K reported as
held rows vs rows, two numbers, frontier rows named — applied in the
SCORECARD K row and this report); proposals 1/2/4/5 not adopted; shokuknow
unreachable. Scratch deleted; scratch profile and loopback processes torn
down before finishing.
