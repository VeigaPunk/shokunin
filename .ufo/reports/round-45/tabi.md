# tabi — round 45 report

Lane repo: `C:/Users/jpvei/.zcode/workspace/95b1ba4d-5089-47a4-9fd8-54adebbce2ae/fleet/tabi-shokunin` (master).
Baseline `d252ea17bf8d39ea2e1da9770316146f264f8a0e` → freeze `51ee19219427497b69bbd4567d21c5478f4efbad`
→ measured `fb8e2435000df47d86fbab8ce89c1e8f3d0a733f` → data-corrected (frozen kill-rule flow) and
**cited measured revision `0360b069c5f8465c0a230638b24229e774df7ea3`** → integration tip
`cc34ab50ed8e561e8e9943a5d700e12b60a0dafc` → round-close hygiene tip
`13a22ee17e1fe8f71de8263e343002fa588ef64b` (lane head at filing; pushed; instrument bytes
byte-identical from freeze to tip — `git diff 51ee1921..13a22ee1 -- scripts/chrome-cdp-loopback-round45.mjs .ufo/waves/round-45/counters/` is empty).

## Work performed

- **Fresh-start discipline (binding §7).** Re-spot-checked the r41/r42/r43 rejected closures in
  committed bytes: r41's untracked-receipt limb closed (`corpus/evidence/round41/playwright-egress/`
  receipt+witness are blobs at HEAD); r42's nonce-relabel/synthetic false-green class closed by the
  r44 counter clauses (nonce shape, invocation binding, runner-digest pin); r43's
  false-green/crash class closed this round via the D3 crash receipt. Ruled out for r45
  (reasons recorded in `.ufo/waves/round-45/claims.json` `freshStartNote`): a Firefox/BiDi move
  (surface ABSENT on this host, PROVINCE r44 probe); any wave-settled claim (no dispatch surface,
  L0 open — carry-in D4 routed around, no predicate carries a wave clause); knowledge-note-count
  claims and the bare D1 file edit (do-nothing reachable — D1 is carried as protocol work and
  ratcheted by C1's counter instead); reusing the r36 adjacency meter v4 (its fleet path and delta
  pins bind the old Linux host and lanes absent here).
- **Carry-in D1 (repin append-only).** `.ufo/waves/round-44/claims-amendments.json` (new file;
  the r44 freeze file keeps its blob id `a38b24ee…` byte-for-byte): old
  `d994ab716df4cb97ab007f7f955b000df1091265e77993e7f06331de4b3feb72` → new
  `f796ae84085087b6acde10a7d32787e95589f3202386f33bce7d8dfaaf101cc5` for the r44 C2 counter,
  enforced by C1's checker (relabels, invented repins and future uncovered stale entries refused).
- **Carry-in D2 (correction row).** Lesson round-45 "Carry-in" section: the r44 honest-state C1/C3
  receipts are measured at `8c238799…` (their `rev` fields) while the r44 report lines say
  `844a5b3a…`; per-revision baselines named explicitly (instruments+freeze at `8c238799…`,
  evidence at `844a5b3a…`, read-sets identical, no r44 verdict changes). The r44 report bytes are
  never rewritten.
- **Carry-in D3 (crash receipt).** `.ufo/waves/round-45/measure/d3-r43-pathtype-crash.json` + raw
  stderr: extracted r43 checker bytes (sha256 `2f150b84…`) exit 1 with uncaught
  `TypeError: b.path.replace is not a function` at :196:35 on the pathtype fixture, rebuilt
  deterministically at `7c558d5e2eae93a5f32a8f9235f97775a3fb488c` (same rev as the r44 controls).
- **C1 (calibration)** — the r5 hardening applied to the r44 freeze itself: checker
  `.ufo/waves/round-45/counters/check-r44-freeze-round45.mjs` (freeze-blob pin, per-entry byte
  check of `frozenDigests`, amendment-gated repins, v2 clauses over the r44 controlBindings,
  named-control coverage; selftest 11/11).
- **C2 (coverage capability, sourced S154)** — runner `scripts/chrome-cdp-loopback-round45.mjs`
  (`--browser chrome|edge` declared per invocation; Edge endpoint discovered via the throwaway
  profile's `DevToolsActivePort` file — Edge prints no stderr DevTools line on this host — and
  confirmed by a live `/json/version`) + counter `chrome-cdp-receipt-r45.mjs` (surface grammar,
  browserPath family, per-surface profile, discovery leg, loopback, invocation binding, PNG
  digest, teardown; refuses the r44 chrome receipt). Live Edge run + repro run executed; evidence
  committed as explicit files.
- **C3 (adjacency — the lowest owned axis, 8; nudge inactive)** — meter
  `c1-adjacency-host-v5.mjs` (P1 audit over the 16-row ruled map with status re-derivation,
  P2 roster completeness, P3 owned-ground delta screen with byte+head binding) + ledgers
  `corpus/adjacency-host-audit-r45.tsv` (16 rows) and `corpus/adjacency-host-delta-r45.tsv`
  (12 lane rows + 14 dispositioned hit lines).
- **Census**: start exit 0 (`tabi ok`, the same 21 pre-existing W04 warnings) and end exit 0
  (receipts committed); `check-sources` clean at the tip (rows=154, findings=0).

## Landed changes

| Commit | Content |
|---|---|
| `51ee1921…` | FREEZE (pre-data): claims.json (3 claims, predicates, kill rules, 5 frozen digests, 12 control bindings by sha256+whole-line quotes), C1 checker, C2 runner+counter, C3 meter, D1 amendment, 7 pre-data controls (probes, baseline reds, cross-refusal), S154 staged copy |
| `fb8e2435…` | MEASURED CLAIMS: ledgers (audit 16 rows, delta 26 rows), edge evidence pair, D3 receipt pair, live-run receipts, selftests |
| `0360b069…` | DATA CORRECTION under C3's frozen kill rule: adjacency lane rows re-bound to current sibling heads (chousa advanced mid-measurement; `lane-screen-head-mismatch` caught by the meter; instruments untouched) |
| `cc34ab50…` | INTEGRATION: SCORECARD round-45 block + capabilities row `edge-cdp-loopback-windows` (first-working 45), SOURCES S154 (registry 153→154), knowledge note (61→62), lesson round-45 (Gate + D1/D2/D3 carry-in rows + 4 Mistakes), LOG entry, PROVINCE host-surface Edge update, measured receipts at the cited revision, census-end + check-sources receipts |
| `13a22ee1…` | ROUND-CLOSE: teardown-orphan disclosure (fifth lesson Mistake + LOG line); runner repair routed to round 46 |

All commits made by the plumbing helper, pushed to origin master (`git ls-remote` ==
`cc34ab50…`). LOG.md entries: round-45 section appended (every change above is tied to it).

## Before → after measurements

- **C1**: `node .ufo/waves/round-45/counters/check-r44-freeze-round45.mjs --rev d252ea17bf8d39ea2e1da9770316146f264f8a0e --repo <lane>` → exit 1, findings `amendment-missing` + `frozen-digest-stale` (receipt `measure/c1-checker-red-at-baseline.json`) → `--rev 0360b069c5f8465c0a230638b24229e774df7ea3` → exit 0, 0 findings (receipt `measure/c1-checker-green-at-measured.json`); `--selftest` → `allPass: true` 11/11. Measured commit `0360b069…`.
- **C2**: `git ls-tree -r --name-only d252ea17… -- corpus/evidence/round45 | wc -l` → 0 (control `controls/c2-baseline-count.txt`) → `git ls-tree -r --name-only 0360b069… -- corpus/evidence/round45 | wc -l` → 2; live run `node scripts/chrome-cdp-loopback-round45.mjs --browser edge …` → exit 0 (Edg/156.0.4314.50, `discoveryVia: devtools-active-port`, invocation-bound, PNG 8,194 B sha `7dfce09d…`); counter → exit 0, 0 findings on the committed bytes (`measure/c2-counter-edge-committed.json`); repro run → exit 0 with fresh nonces (receipt `7543027b…`/`10bc2096…`, fixture `2a3f9a27…`/`76926454…`) and byte-identical screenshot; cross-refusal → exit 1 with 5 findings (`controls/c2-counter-refuses-r44-receipt.json`). Measured commit `0360b069…`.
- **C3**: `node .ufo/waves/round-45/counters/c1-adjacency-host-v5.mjs --rev d252ea17… --repo <lane> --fleet <fleet>` → exit 1, 28 findings → `--rev 0360b069…` → exit 0, counts `{roster:16, mapRows:16, auditRows:16, deltaLanes:12}` (receipts `measure/c3-meter-red-at-baseline.json` / `measure/c3-meter-green-at-measured.json`); selftest 13/13. Drift recorded as the result: 6 sibling-absent, 9 stale, 1 moved. Measured commit `0360b069…`.
- **Registry**: `grep -c '^| S[0-9]' corpus/SOURCES.md` 153 → 154. **Knowledge**: `ls corpus/knowledge/*.md | wc -l` 61 → 62. **Evidence**: round45 tree 0 → 2.

## Sources & frontier

SOURCES.md rows: 153 → 154 (command above). One row opened this round: **S154 — Microsoft Edge
DevTools Protocol** (https://learn.microsoft.com/en-us/microsoft-edge/devtools/protocol; curl
fetch 57,251 B, sha256 `ab6c14c5…`, staged copy committed; located quote "The Microsoft Edge
DevTools Protocol matches the APIs of the Chrome DevTools Protocol." — 13 words, 1 verbatim hit;
mined by `corpus/knowledge/chrome-cdp-loopback-round-45.md` and the lesson). C2 rests on S154
(satisfies the sourced-claim requirement). A first URL tried (`…/devtools-protocol/`) redirected
to a legacy EdgeHTML page and was rejected before use. Mistake-mining: four rows in
`corpus/lessons/round-45.md` §Mistakes (two mined from r44 per the §2b duty — the stale pin and
the revision-wording drift; two from this round — the broad keyword list narrowed pre-freeze on a
measured 265+-line noise burden, and the module-import CLI bug). Census start AND end exit 0.

## Trend verdicts

- **expansion: improved** — capabilities row `edge-cdp-loopback-windows` entered (first-working
  45; second Chromium-class surface demonstrated live on this host); new sourced note on uncovered
  ground; registry 153→154; notes 61→62; evidence tree 0→2.
- **quality: improved** — r44 routed defects D1–D3 closed in committed bytes (byte-binding
  checker + append-only amendment; correction of record; captured crash receipt on a
  deterministic fixture); the head binding caught a real sibling move mid-measurement; no admitted
  entry failed a re-check; census and check-sources clean at the tip.
- **discernment: improved** — the round's instruments refused its own outputs twice before
  admission (first C3 measurement red on a stale head — kill-rule data-correction, disclosed;
  broad keyword list rejected pre-freeze) and both refusals are recorded; fresh-start spot-checks
  re-derived three prior rounds' refusal classes from committed bytes. Outside non-author
  admit/reject spot-check remains the closure's duty (pending at filing).

## SHONEN

SHONEN.md exists; no box changes this round (per protocol only a named non-author verifier may
write `[x]`; none did):

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — unchanged; prior evidence pointers stand.
- [~] At least one end-to-end domain task executed and logged in LOG.md — strengthened this round: the live Edge CDP run is committed, logged, and reproducible from committed bytes (`corpus/evidence/round45/edge-cdp/`, LOG round-45 entry); non-author `[x]` still owed.
- [~] Instructions executable by an agent without oral context — strengthened: the r45 runbook deltas are in the note (`chrome-cdp-loopback-round-45.md`); non-author `[x]` still owed.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — PROVINCE host-surface line updated this round (Edge second surface); the contested CDP ground found in `shokunin-reverse-engineering` is routed (delta ledger, contested-open), not absorbed.

Assimilation: `considerthese/` does not exist in the lane repo (checked 2026-10-31) — adopted
nothing. Assimilation: none — shokuknow unreachable.

## Round-close addendum (hygiene, post-integration)

The scratch deletion failed `Device or resource busy` on `cdp-edge-run1/edge-profile/Default/*`:
three re-parented msedge orphan trees survived the runner's `taskkill /T` although every receipt
recorded `chromeTerminated: true` — that clause is truthful about the MAIN child's exit, but Edge
helpers re-parent on this host and outlive the tree kill. Handled: the three orphan roots were
killed PID-scoped (never by image name — the operator's own Edge runs under the same image), a
CimInstance sweep confirms 0 tabi-r45 msedge processes, and the scratch dir is deleted. Recorded
as a fifth Mistake in `corpus/lessons/round-45.md` and in LOG.md; the runner repair (post-run
profile-token sweep or job-object kill) routes to round 46. No frozen byte was amended post-data;
no claim verdict changes — the frozen predicates held as measured at `0360b069…`.

L0: the L2-floor question stands open (r44 tabi line; corroborated by kaidoku/souji lines); this
round routed around it — no claim carries a wave-settled clause.
