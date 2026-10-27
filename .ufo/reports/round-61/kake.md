# kake round 61 — report

Lane: `kake-shokunin`, attempt 1, L1 `KakeR61`. Round shape: two v1 waves, w1 build **43** seats and w2 falsify **36** seats, **79 total**; no residual call. Lane base `9f07731a873585e655a6518233ea39f5d9fb8204`; final lane tip `51ef86cb4c03eb578339337eb4953615a7a4c9de` (remote-verified).

## Work performed

Declared claims: **C1 calibration** (receipt-lineage watch), **C2 operability/capability** (offline response-header expectation audit), **C3 freshness** (re-open the ten oldest registry rows S001–S010 and pin recheck cadence dates).

- C1 was attacked against the existing round-58 receipt ledger. The c58-only control was already green at both base and measured tip (`events=19 undisclosed=0 met=True`, exit 0); w2 found C1's 12 observed events are a strict subset. The specified C1 counter was absent, so no C1 case score exists. Evidence: `.ufo/waves/round-61/controls/c1-c58-{base,measured}-control.txt`, `w1/ExecC1Counter.md`, `w2/CriticC1C58Overlap.md`, `w2/SentinelC1Path.md`.
- C2 added `scripts/response_snapshot.py`, `scripts/header_audit.py`, and `corpus/knowledge/response-header-expectations.md` on four sources opened this round; the final C2 matrix scores H1–H18 18/18, R3 canonical shape passes, and R4 do-nothing is red. The recorded 12-surface audit produced 13 findings (12 CSP absent, one HSTS absent), exit 1; this is not a live-clean claim. Evidence: `controls/after-c2-header-counter.txt`, `controls/after-c2-real-audit.txt`, `corpus/knowledge/response-header-expectations.md`, `w1/ExecC2HeaderRecon.md`.
- W2 found capture-tool SSRF, proxy, timeout, header-exception and overwrite defects. The final tool blocks non-global peers before the HTTP request, disables environment proxies, enforces a monotonic 20-second per-surface deadline, catches `HTTPException`, removes `--overwrite`, and creates output files exclusively. Local probes: loopback server hit count 0; second write refused with original bytes intact; public HTTPS GET returned 200. The 12 existing captures were not overwritten or re-fetched; they were made by pre-hardening bytes and have zero redirects/cookie/auth headers. Evidence: `controls/capture-hardening.txt`, `controls/capture-hardening-https.txt`, `w2/SentinelC2Capture.md`, `w2/ReviewerC2CaptureReceipts.md`.
- C3 re-opened S001–S010 with ten retained bodies and receipts. Nine rows (S002–S010) received concrete recheck dates; S001 was carried as `anchor_moved` because its fetched primary URL did not verify the full multi-URL anchor. Counter result: 6/6, exit 0 (`pinned=9 carried=1`). Evidence: `controls/after-c3-recheck-pins.json`, `corpus/lessons/round-61.md` §Gate, `w2/CriticC3QuoteTruth.md`.
- The mined mistake is the r56/r57 undisclosed receipt-rewrite class; the c58 control shows the new C1 claim did not add distinct calibration coverage. The round-60 EN quote count was corrected to 22 units. Capture ingress defects found by w2 were also recorded and fixed. Evidence: `corpus/lessons/round-61.md` §Mistakes.
- Curated S430–S433 as four tier-A rows; added the response-header entry to `corpus/README.md` and publisher-side Frontier to `PROVINCE.md`. Assimilation: none; the 12-row shokuknow quarantine slice remains held. Evidence: `corpus/SOURCES.md` S430–S433; `.ufo/waves/round-61/assimilation/quarantine-slice`.
- W1 role mix: executor 16, reviewer 6, scout 5, critic 6, scribe 5, sentinel 2, mutation-tester 1, connector 2. W2: reviewer 12, critic 10, mutation-tester 9, sentinel 3, connector 2. W1 had 43 reports. W2 had 30 reports; six seats settled without a report (CriticC1Claim, CriticC2DoNothing, MutationC1Pending, MutationC2Manifest, ReviewerC1Disclosure, ReviewerC2EntryScope); `w2-results.json` has no last-error field for these partial outputs. No explicit dead status was reported. Results handoffs: `.ufo/waves/round-61/w1-results.json`, `w2-results.json`.
- Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` showed only the expected report draft and unrelated `.scratch/closure-mado-r50.json`; no seat misroots were copied or deleted.

## Landed changes

All changes are described in `kake-shokunin/LOG.md` §Round 61; the final commit carrying the log, lesson, scorecard, registry and hardening is `51ef86cb4c03eb578339337eb4953615a7a4c9de`.

- Frozen three-claim contract, population and w1 spec/dispatch: `eaa9177e2965a50fa038d57254934a53909052b6`.
- Pre-freeze amendments A1–A5: `142dda56e424c642b1c36ac7e5bbba5460c3d56b`, `f512eeea5b566466f3517f6039c42418e1170282`; w2 spec/dispatch: `f5a9b8acc8e4d0995e8ba849c4a9d56ba1ab0a8f`.
- C2/C3 tools, sources, lesson and initial integration: `d2da25de5fcd8d2384cee99b615cd53b083c5887`.
- C2 counter v2, measurements, scorecard/log and C1 removal after falsification: `7b3d8c5976a08da7fb3e961b14fcab53ba2e2966`.
- Final capture hardening and its HTTPS receipt: `51ef86cb4c03eb578339337eb4953615a7a4c9de`.
- Final lane tip remote check: `git ls-remote origin refs/heads/master` → `51ef86cb4c03eb578339337eb4953615a7a4c9de`.

## Before → after measurements

- **C1 calibration — not met.** The declared new lineage counter never landed; the do-nothing c58 ledger already reached the target at base and measured tip: `events=19 undisclosed=0 met=True`, exit 0 → same result, exit 0. Counting command: `python3 -B .ufo/waves/round-58/c58_receipt_rewrites.py --root . --revision <rev> --json`; revisions `9f07731a873585e655a6518233ea39f5d9fb8204` and `d2da25de5fcd8d2384cee99b615cd53b083c5887`. No calibration credit; axis score remains 2.
- **C2 operability — measured.** Base tool absent: `0/18`, exit 1 → `18/18 met=True`, exit 0, R3 shape pass, R4 do-nothing pass. Counting command: `python3 -B .ufo/waves/round-61/c61_header_cases.py --root . --revision d2da25de5fcd8d2384cee99b615cd53b083c5887 --seed 61`; receipt `controls/after-c2-header-counter.txt`. Tool selftest 64/64; counter selftest 7/7 controls. Capability entered; numeric score holds at 10.
- **C3 freshness — predicate met, bounded.** Base control `4/6`, exit 1 → `6/6`, exit 0; S002–S010 pinned, S001 carried as `anchor_moved`. Counting command: `python3 -B .ufo/waves/round-61/c61_recheck_pins.py --root . --revision d2da25de5fcd8d2384cee99b615cd53b083c5887 --json`; receipt `controls/after-c3-recheck-pins.json`. W2 sentinel found the fetch helper cannot reliably re-derive redirect provenance; therefore this report makes no stronger source-origin guarantee than the committed bodies, receipts and quote checks. Numeric freshness score holds at 10.

## Sources & frontier

- Census command at both points: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kake`.

Before census (exit 0):
```text
kake	W04	S033 duplicate url www.rfc-editor.org/rfc/rfc9110.txt across scopes
kake	W04	S088 duplicate url www.rfc-editor.org/rfc/rfc9110.html across scopes
kake	W04	S092 duplicate url html.spec.whatwg.org/multipage/syntax.html across scopes
kake	W04	S098 duplicate url www.rfc-editor.org/rfc/rfc3986.txt across scopes
kake	W04	S099 duplicate url www.rfc-editor.org/rfc/rfc9309.html across scopes
kake	W04	S102 duplicate url www.sitemaps.org/protocol.html across scopes
kake	W04	S110 duplicate url www.w3.org/TR/xml across scopes
kake	W04	S111 duplicate url docs.python.org/3/library/urllib.parse.html across scopes
kake	W04	S115 duplicate url docs.python.org/3/library/urllib.parse.html across scopes
kake	W04	S116 duplicate url docs.python.org/3/library/urllib.parse.html across scopes
kake	W04	S117 duplicate url www.rfc-editor.org/rfc/rfc3986.txt across scopes
kake	W04	S127 duplicate url www.rfc-editor.org/rfc/rfc9844.txt across scopes
kake	W04	S416 duplicate url ziyuan.baidu.com/college/courseinfo?id=1399 across scopes
kake	W04	S417 duplicate url ziyuan.baidu.com/college/courseinfo?id=267&page=15 across scopes
kake	W04	S427 duplicate url developers.google.com/crawling/docs/crawlers-fetchers/overview-google-crawlers across scopes
kake	ok	/home/vgpnk/Projects/shokunin/kake-shokunin/corpus/SOURCES.md
```

After census (exit 0):
```text
kake	W04	S033 duplicate url www.rfc-editor.org/rfc/rfc9110.txt across scopes
kake	W04	S088 duplicate url www.rfc-editor.org/rfc/rfc9110.html across scopes
kake	W04	S092 duplicate url html.spec.whatwg.org/multipage/syntax.html across scopes
kake	W04	S098 duplicate url www.rfc-editor.org/rfc/rfc3986.txt across scopes
kake	W04	S099 duplicate url www.rfc-editor.org/rfc/rfc9309.html across scopes
kake	W04	S102 duplicate url www.sitemaps.org/protocol.html across scopes
kake	W04	S110 duplicate url www.w3.org/TR/xml across scopes
kake	W04	S111 duplicate url docs.python.org/3/library/urllib.parse.html across scopes
kake	W04	S115 duplicate url docs.python.org/3/library/urllib.parse.html across scopes
kake	W04	S116 duplicate url docs.python.org/3/library/urllib.parse.html across scopes
kake	W04	S117 duplicate url www.rfc-editor.org/rfc/rfc3986.txt across scopes
kake	W04	S127 duplicate url www.rfc-editor.org/rfc/rfc9844.txt across scopes
kake	W04	S416 duplicate url ziyuan.baidu.com/college/courseinfo?id=1399 across scopes
kake	W04	S417 duplicate url ziyuan.baidu.com/college/courseinfo?id=267&page=15 across scopes
kake	W04	S427 duplicate url developers.google.com/crawling/docs/crawlers-fetchers/overview-google-crawlers across scopes
kake	W04	S433 duplicate url www.rfc-editor.org/rfc/rfc9110.html across scopes
kake	ok	/home/vgpnk/Projects/shokunin/kake-shokunin/corpus/SOURCES.md
EXIT=0
```
- Before: **167** rows, exit **0**, 15 W04 warnings; output is `.ufo/waves/round-61/controls/census-before.txt`.
- After: **171** rows, exit **0**, 16 W04 warnings; output is `.ufo/waves/round-61/controls/census-after.txt`. The added warning is S433 sharing the RFC 9110 URL with S088 across scopes; no S088 edit.
- Rows added by tier: four tier-A `spec` rows, S430–S433. Rows touched old→new: S002 `on-release→2027-01-17`; S003–S007 `90d→2027-01-17`; S008–S010 `365d→2027-10-19`. S001 stayed `on-release` (honest carry). All changes are in `corpus/lessons/round-61.md` §Gate.
- Frontier advanced: publisher response-header expectations is now held ground with a sourced entry and offline audit; no live conformance or clean-site claim. `Assimilation: none`. Quarantine: 12 rows re-derived, byte-identical to the prior record (sha256 `6d92f4408c7482e59fb93c2085676f7d9c4fedb687bcfd501060f63c15d2d63a`), still held; no row appended from shokuknow.

## Trend verdicts

- **Expansion — improved.** Four new scoped source rows and one publisher-side response-header entry/gate move new frontier ground into held knowledge (`S430–S433`; `corpus/README.md`, `PROVINCE.md`). No live property was repaired or asserted clean.
- **Quality — improved (bounded).** Header-audit matrix met 18/18; capture ingress was hardened against the reproduced SSRF/proxy/overwrite/header-abort cases and the local HTTPS/private-peer probes passed. Limitations remain: source fetch redirect provenance is not re-derived; S432's located Gate quote is a generic lead-in to its ABNF; captured live responses produced 13 policy findings.
- **Discernment — unchanged.** The two waves are lane-author review; no independent non-author closure has yet spot-checked the admit/reject and claim verdicts. C1's honest stop and the S001 carry are recorded for the closure judge.

## SHONEN

- [~] SKILL.md:209,1359–1362 — decision/gate registry now includes the response-header capture/audit commands and limits.
- [~] LOG.md:2239–2250 — C2 capture/audit and C3 source recheck executed and recorded; C1 control stop recorded.
- [~] `scripts/response_snapshot.py`, `scripts/header_audit.py`, and `corpus/knowledge/response-header-expectations.md` — runnable capture/audit instructions; w1 reviewer `ReviewerC2EntryQuotes.md` checked quote spans.
- [~] PROVINCE.md:20–36 and `.ufo/waves/round-61/w1/ConnSiblingOverlap.md` — publisher-side boundary stated; sibling scan found no contested overlap.

Stale-lane: respawn-per-round driver; no other mission of this lane is open. Open prior L0 items remain the quarantine hold and calibration sub-axis ownership; neither was treated as answered. Tool installs/updates: none. No pacman transaction.
