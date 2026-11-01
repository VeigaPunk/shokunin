# tabi — round 49 report (Windows host)

Lane repo: `fleet/tabi-shokunin` (branch master). Baseline
`10ea3d96c0eed6d0e7240f57f7a30d8ef73689b1` (the r48 spot-check tip). FRESH-START
ruling honored: the r42/r43/r47 refused claim classes are named in the freeze's
`freshStartNote` and ruled out (see "What was ruled out and why").

## Work performed

- **Freeze-first round** — `.ufo/waves/round-49/claims.json` + instruments +
  round-open controls committed at `7700daf8e1168648c6cb2608880617817b0dda62`
  BEFORE any data commit: three frozen predicates with kill rules and
  frozenDigests; meter v9 (const/comment/schema retarget of v8, selftest 16/16,
  47-line committed diff); webview2 runner v2 (resolve-at-launch + `--nav` +
  `--path-selftest` 6/6); receipt counter r49 (paths contract + nav legs, 8-case
  refusal-fixture selftest); round-open controls (C1 red, C2 v1-relative red);
  census START receipt; orphan-evidence sweep receipt. Evidence:
  `.ufo/waves/round-49/` at the freeze commit.
- **C1 adjacency (lowest owned axis, 8)** — the regression-gate re-bind: at
  round open the inherited r48 generation measured RED (15 findings: 11 head +
  2 sha + 2 lines; receipt taken before any lane write,
  `controls/c1-meter-red-at-round-open.json`); audit-r49 (16 rows = 10 unchanged
  + 6 sibling-absent) and delta-r49 (12 lanes + 16 line rows) re-bound at one
  fresh snapshot, dispositions carried by exact whole-line quote match, 0 new
  adjudications; the meter head-raced twice under the frozen correction flow and
  went GREEN at correction 2 (within the two-cycle kill rule). Evidence:
  `measure/c1-meter-green-at-data.json` at `5fa183842a9925b3e18ea5f9df039984d47d5666`.
- **C2 operability (the r48-closure routed item 1; sourced S160 opened this
  round)** — the routed foot-gun fixed in a versioned runner: the frozen r48
  bytes measured RED on a relative `--scratch` (exit 1
  `no-devtools-active-port`; the real profile anchored at the HOST EXE
  directory — exactly S160's UDF contract — with a live DevToolsActivePort the
  runner never polled; receipts
  `controls/c2-v1-relative-scratch-red-{receipt.json,stdout.json,anchor.txt}`);
  `scripts/webview2-cdp-loopback-round49.mjs` resolves `--scratch`/`--out` at
  launch and records given-vs-resolved in the receipt; the SAME relative shape
  went GREEN at `b026dc34368e06eb46ebdd925b132595751ffa4c`; counter green,
  absolute-equivalence control green, 8/8 refusal-fixture selftest,
  `--path-selftest` 6/6, symmetric cross-refusals; the frozen r48 bytes
  documented absolute-only via dated appends (knowledge note + PROVINCE), never
  edited.
- **C3 coverage (the r48 note's declared residual, exercised)** — cross-page
  navigation over an inline loopback HTTP fixture: `Page.navigate` to
  `/a.html`, the page's OWN anchor clicked to `/b.html` (mechanism
  `anchor-click`), per-page URL/title/PNG evidence, invocation-bound nonce,
  teardown sweep 0; capability row `webview2-http-cross-page-nav-windows`
  (first-working 49) enters the SCORECARD table; the r48 residual superseded by
  a dated append. Evidence: `corpus/evidence/round49/webview2-nav/` at
  `36f8579bf2fbabd71d8a15142e1c9cf29e27bb02`.
- **Carry-in item 2 (orphaned-evidence hygiene)** — the round-open sweep
  (`controls/orphan-evidence-sweep.txt`, committed at the freeze) found the
  literal cited-but-uncommitted set EMPTY: every receipt cited by committed lane
  bytes and by the fleet-side tabi reports r44–r48 is a blob at HEAD (579 + 42
  unique cited paths checked with `git cat-file -e HEAD:<path>`); 205 of the 208
  `git ls-files --others` hits are in-HEAD blobs (the host's stale git index —
  the same artifact that makes `git status` garbage and m3 read 425); the three
  genuinely-uncommitted r44 receipts (never cited anywhere) were landed anyway
  as the hygiene act: `6e080c17f8e568446a535c845c4387b795b3a1f6` (explicit
  treecommit paths). The standing selfassessment m3 mismatch is disclosed as
  the index artifact, not unlanded evidence.
- **Carry-in item 3 (L2-floor L0)** — `tabi | round-44` stays open; routed
  around (fourth round running), L1-inline, no wave-settled clause in any
  predicate.
- **Frontier** — S160 opened (Microsoft Learn, User data folder: the UDF
  anchors at the directory the host app's `.exe` runs in); registry 159 → 160,
  the row inserted INSIDE the Registry table after S159 (the r48 E12 lesson
  applied pre-emptively); knowledge note round-49 append (absolute-paths caveat
  + the r49 recheck surface + the residual supersession); PROVINCE round-49
  line; lesson `corpus/lessons/round-49.md` (Gate + 4 Mistakes + census);
  SCORECARD round-49 block; LOG entry; README round-49 section.

### What was ruled out and why (fresh-start duty)

- r42's refusal class (counters that green nonce-relabeled/synthetic receipts
  over committed bytes): ruled out — both r49 counters re-hash the committed
  driver/host bytes against the receipt pins, require the invocation-bound
  nonce echo, Edg/ identity and a keyed teardown to 0, and ship hand-declared
  refusal fixtures (tampered shot, chrome relabel, cross-schema r48 receipt,
  wrong nonce/profile prefixes); the r44 chrome receipt is refused with 19
  findings and the r48 counter refuses a r49 receipt with 4.
- r43's refusal class (four in-model do-nothing seats): not reachable — no
  wave/seat claim is declared (the L2-floor L0 stays open and routed around);
  every claim's evidence is a live run of committed instruments on this host.
- r47's refusal class (a frozen after-state reasoned, not measured): ruled out
  — no after-state number is asserted from arithmetic; C1's after is the
  meter's own exit-0/0-findings run at the data revision; C2's and C3's
  after-states are live receipts produced after the freeze by sha-frozen
  instruments.
- Do-nothing control bar (§9): C1's red is what nothing-done reaches (15
  findings) and green requires the re-bind; C2's red is the r48 bytes' own
  failure on the routed invocation and green requires the resolve-at-launch
  repair plus a live run; C3's baseline is 0 evidence files and the nav
  receipts require a live cross-page navigation.

## Landed changes

| Commit | Content |
|---|---|
| `7700daf8e1168648c6cb2608880617817b0dda62` | round-49 FREEZE (pre-data): claims.json + meter v9 + runner v2 + counter r49 + fixtures + round-open controls + census START + orphan sweep receipt (28 files, all additions) |
| `6e080c17f8e568446a535c845c4387b795b3a1f6` | carry-in hygiene: the three uncited r44 receipts landed (explicit treecommit paths) |
| `eb89957ff39e645de813c75033fc7828117e0c5a` | C1 data: audit-r49 + delta-r49 (first snapshot) |
| `44dde54f354693838076bc4532a93b693693a7ce` | C1 correction 1 (frozen flow): kotodama + binary-forensics head race |
| `5fa183842a9925b3e18ea5f9df039984d47d5666` | C1 correction 2 (**cited measured revision**): kasegi + kotodama head race; meter GREEN |
| `b026dc34368e06eb46ebdd925b132595751ffa4c` | C2 data: `corpus/evidence/round49/webview2-relscratch/` |
| `36f8579bf2fbabd71d8a15142e1c9cf29e27bb02` | C3 data: `corpus/evidence/round49/webview2-nav/` |
| `c0b187b7659b3d623837e315d67483f3be5ca8e8` (integration, pushed) | SOURCES S160 + lesson round-49 + SCORECARD round-49 block + LOG entry + README section + knowledge-note append + PROVINCE line + all measure/ receipts (greens, cross-refusals, census END, check-sources, selfassessment) + the absolute-equivalence control |

LOG.md carries the round-49 entry tying every change above to its commit; the
SCORECARD round-49 block carries the claims table and the capabilities row.

## Before → after measurements

- **C1 adjacency** (at `5fa183842a9925b3e18ea5f9df039984d47d5666`):
  - Before: `node .ufo/waves/round-48/counters/c1-adjacency-host-v8.mjs --rev
    10ea3d96… --repo <lane> --fleet <fleet> --json` → exit 1, predicate=false,
    **findingCount 15** (receipt
    `.ufo/waves/round-49/controls/c1-meter-red-at-round-open.json`, round open).
  - After: `node .ufo/waves/round-49/counters/c1-adjacency-host-v9.mjs --rev
    5fa18384… --repo <lane> --fleet <fleet> --json` → exit 0, predicate=true,
    **findingCount 0** (`.ufo/waves/round-49/measure/c1-meter-green-at-data.json`).
    Selftest 16/16 (`measure/c1-meter-v9-selftest.json`); v8→v9 diff 47 lines,
    comment/const/schema only. Ledgers: `awk -F'\t' 'NR>1{n[$2]++}
    END{for(k in n) print k, n[k]}' corpus/adjacency-host-audit-r49.tsv` →
    `unchanged 10 / sibling-absent 6`; delta-r49 = 12 lane rows + 16 line rows;
    0 new adjudications.
- **C2 operability** (at `b026dc34368e06eb46ebdd925b132595751ffa4c`):
  - Before: `node scripts/webview2-cdp-loopback-round48.mjs --scratch relscratch
    --out r.json` (cwd: scratch) → exit 1, `no-devtools-active-port`
    (waitedMs 15568), profile anchored at `<cwd>/relscratch/relscratch/…`
    (receipts `controls/c2-v1-relative-scratch-red-*`).
  - After: `node scripts/webview2-cdp-loopback-round49.mjs --scratch relgreen
    --out r.json` → exit 0 (paths block, invocation-bound nonce, PNG 7,617 B,
    sweep 0; `corpus/evidence/round49/webview2-relscratch/receipt.json`).
  - Counter: `node .ufo/waves/round-49/counters/webview2-receipt-r49.mjs
    corpus/evidence/round49/webview2-relscratch/receipt.json --shot
    corpus/evidence/round49/webview2-relscratch/receipt.png --driver
    scripts/webview2-cdp-loopback-round49.mjs --hostsrc
    scripts/webview2-host-round48.cs` → exit 0, **0 findings**
    (`measure/c2-counter-green-at-data.json`). Selftests: counter `--selftest`
    **8/8**; `--path-selftest` **6/6**. Absolute-equivalence control:
    counter-green, no `paths-absolute-not-identity`
    (`controls/c2-v2-absolute-equivalence-receipt.json`). Cross-refusals: r44
    chrome receipt refused with **19 findings**
    (`measure/c2-counter-crossrefusal-r44.json`); the r48 counter refuses the
    r49 receipt with **4 findings** (`measure/c2-r48counter-refuses-r49.json`).
- **C3 coverage** (at `36f8579bf2fbabd71d8a15142e1c9cf29e27bb02`):
  - `git ls-tree -r --name-only <REV> -- corpus/evidence/round49/webview2-nav |
    wc -l` → 0 → **3** (receipt.json + receipt-page-a.png + receipt-page-b.png).
  - Counter with both nav legs → exit 0, **0 findings**
    (`measure/c3-counter-green-at-data.json`). Live facts: fixture port 61114,
    pages `/a.html` → `/b.html` same-origin distinct URLs, titles "tabi-r49 nav
    fixture A/B", PNGs 6,781/7,002 B, invocation-bound nonce, Edg/156.0.4314.50,
    teardown sweep 0.
  - Residual supersession: `grep -c 'cross-page navigation were not exercised'
    corpus/knowledge/webview2-cdp-loopback-round-48.md` → 1 at baseline; the
    dated append supersedes it.

## Sources & frontier

Registry 159 → 160: `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'
corpus/SOURCES.md` → 159 at baseline, **160** at the tip (S160 inserted inside
the Registry table after S159). S160 opened this round: Microsoft Learn,
"User data folder" (WebView2 concepts) — raw-fetched 87,802 B
(`wc -c`), sha256 `5c93b4fd95f3903914ae2d4fde9ff324f1d96d56f7ecf5107bc94d43c62d81f2`,
staged at `.ufo/waves/round-49/sources/user-data-folder.html`; quote
"On this platform, the default UDF location is the directory that the app
executable (.exe) is running in" (18 words; disclosed at 3 verbatim hits across
the page's platform sections; the Win32 section is this lane's surface).
Census: START exit 0 (`measure/census-start.txt`, 22 pre-existing W04), END
exit 0 (`measure/census-end.txt`, W04 unchanged at 22). check-sources at the
integration tip: exit 0, `verdict=clean rows=160 … findings=0`
(`measure/check-sources-at-integration.txt`). Mistake mining: 5 rows in
`corpus/lessons/round-49.md` (two counter defects caught by the fixture
selftest before the freeze; the ledger summarizer misread; a path-selftest case
bug; the selfassessment gate's EPERM temp-cleanup crash, re-run with both
receipts kept), each with evidence pointer, captured-by and fix. Sourced claim: C2 rests
on S160.

## Trend verdicts

- **expansion: improved** — the webview2 surface's measured page model grew
  from a single data:-URL page to cross-page HTTP navigation (0 → 3 committed
  evidence files, live anchor-click hop, counter-checked); capability row
  `webview2-http-cross-page-nav-windows` (first-working 49) enters the table;
  S160 moves the UDF path contract from measured-but-undocumented to a held,
  recheckable row (159 → 160). No axis harmed.
- **quality: improved** — the routed foot-gun closed with a versioned repair
  measured on both sides (v1-relative red with the exe-dir anchor; v2-relative
  green) plus an absolute-equivalence control proving the repair changes
  nothing else; the counter family grew to 8 refusal fixtures and demonstrated
  two symmetric cross-refusals; the adjacency gate survived two live head races
  inside its frozen correction budget and reads green; the three genuinely
  orphaned r44 receipts landed; no admitted entry failed a re-check.
- **discernment: improved** — every after-state is an instrument output at a
  named revision (the r47 discipline held); the fixture selftest caught two
  real counter defects BEFORE any data relied on the counter, disclosed as
  mistakes with the failing first reads; the hygiene sweep refused to find work
  that wasn't there (the cited-but-uncommitted set is empty) while still
  landing the three orphans it did find; the correction flow consumed exactly
  its allowed budget and both raced receipts are committed (correction 1) or
  disclosed as overwritten-in-place (the first race).

## SHONEN

Lane still has SHONEN.md (promotion checklist; 4 boxes). No `[x]` is written
by the author (only a non-author verifier counts — orchestrator ruling, kaika
round 1):

- [~] SKILL.md contains real decision tables, error patterns, checklists,
  cited sources — `SKILL.md` §Approval table, §Evidence ladder, §Runbook;
  unchanged this round.
- [~] At least one end-to-end domain task executed and logged in LOG.md — this
  round adds two more end-to-end runs (C2's relative-scratch green and C3's
  cross-page navigation, both live on the webview2 surface with committed
  receipts); logged in the LOG.md round-49 entry. The r48 non-author closure
  additionally live-re-ran the r48 capability end-to-end
  (`corpus/lessons/round-48-verifier-spotcheck.md` §2 C3).
- [~] Instructions executable by an agent without oral context —
  `corpus/knowledge/executor-test-sufficiency.md` (verdict SUFFICIENT); the r49
  runner's usage line is self-contained (`--path-selftest` runs with no
  browser).
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md`
  updated with the round-49 runner line; refusal routes unchanged; the mado
  rendering-pixel question stays routed (out of province, L0 open).

Assimilation: none — shokuknow unreachable.
