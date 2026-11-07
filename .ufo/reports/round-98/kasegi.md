# kasegi — round 98 report

Lane: kasegi. Round 98, attempt 1. Driver: `2026-11-07T17:17:59-03:00 launch kasegi round=98 pgid=245383 driver=hyaku-inline attempt=1`.

**Declared claims (2).** C1 — `depth:verifiability` (lowest non-retired axis, score 4): the citation census of record becomes a reading of a named revision. C2 — `coverage` (score 8 held): the `capture-secret-scan` capability gains the four further GitLab rules S140 publishes and a right boundary on five round-97 shapes. Both are frozen in `.ufo/waves/round-98/claims.json` (freeze `12bb2f98cf9d07bcbc8b62985516cc3ff65d9ae8`, base `2133f5bd993aaf34efad795d5e0b588485401fb2`).

**Verdicts: C1 NOT VERIFIED on P1/P2 (P3 stands); C2 VERIFIED-pending-closure on K1–K7, with a statement erratum.** The wave falsified C1's central label — the "revision-stable" pinned rate flips with the verifier's scratch parent — and this report does not prettify it. The round is therefore **not admitted** as a whole; the operator rules.

## Work performed

- **C1 — revision-pinned census of record.** Wrote `corpus/instruments/census-at-rev.py` (extracts `git archive REV`, runs the extract's own `resolve.py`, reports a pinned INTERNAL-only rate beside the host-inclusive rate and the host-owned count, caches one measurement per revision) and regenerated `corpus/instruments/citation-survival.md` at the C2 landing revision. Evidence: `CENSUS-CHECK pass rev=e2caf4a1561b544a6ea684b0bcfa975f7e7f6061 skill=162/732 corpus=2551/7559 lane=2589/7961 host_owned=78` (`.ufo/waves/round-98/l1/c1-controls-postlanding-r98.txt:2`); landed at `e2d3de7b847f8e9bac72a5bc4dea455ea051cf1a`.
- **C1 — control set.** `.ufo/waves/round-98/controls/c1-controls-r98.py` builds a scratch fixture clone (base checked out explicitly), commits the candidate instrument and census, and runs eight controls with declared fail-reason sets. Evidence: `C1-CONTROLS-RESULT pass controls=8 rc=0` and `ATTRIBUTION pass fixtures=8` (`.ufo/waves/round-98/controls/c1-controls-r98-postfix.txt`; post-landing re-run `.ufo/waves/round-98/l1/c1-controls-postlanding-r98.txt:6-14`).
- **C2 — four further S140 rules and the widened boundary.** `corpus/instruments/capture-secret-scan.py` gains `gitlab-ci-build-token` (S140:293), `gitlab-iam-refresh-token` (S140:480), `gitlab-iam-authorization-code` (S140:497) and `gitlab-session-cookie` (S140:549-551), and the five round-97 shapes `gitlab-runner-registration-token`, `gitlab-feed-token`, `gitlab-oauth-app-secret`, `gitlab-feed-token-v2`, `gitlab-scim-oauth-token` now use `(?![A-Za-z0-9])` — a superset of S140's punct/space/EOL class (the statement's "S140's own class" is corrected by erratum). Selftest 148 → 170. Landed at `e2caf4a1`.
- **C2 — capability gate.** `.ufo/waves/round-98/c2/capability-check.py` (K1-K7) generates every plant value from the rule's own alphabet and length, so a literal-locked matcher cannot pass K3 (the round-97 spot-check's defect 3). Evidence: `CAPABILITY-CHECK-RESULT pass rc=0` at the landing at seeds 20261107 and 4242 (`.ufo/waves/round-98/l1/c2-landing-r98.txt`); candidate receipt `.ufo/waves/round-98/controls/c2-gate-candidate-r98.txt`; do-nothing receipt `.ufo/waves/round-98/controls/c2-gate-donothing-r98.txt` (`K1/K3/K5/K7 FAIL`).
- **C2 — knowledge entry.** `corpus/knowledge/gitlab-iam-ci-build-and-session-token-shapes.md` cites S140 (four rules, verbatim), S144 (`glcbt-`, `_gitlab_session=`), S148 (the session cookie's 64-hex value and optional `cell-<ID>-` prefix) and S149 (the two IAM prefixes), with the falsifiable rule, the recheck command and the corrected limits.
- **Frontier — sources.** S140 and S144 re-opened this round (S140 live `/-/raw/` HTTP 403, Cloudflare challenge, 6,078 bytes; S144 live HTTP 200, 67,805 bytes, sha256 `765becf3…`); the wave's ScoutSources found the upstream per-rule prose files and the two new rows S148/S149 were opened and fetched live via the repository-files API (HTTP 200 at their recorded digests). Evidence: `.ufo/waves/round-98/l1/source-reopen-r98.txt`; `corpus/SOURCES.md` rows S140/S144/S148/S149 and the round-98 bullets.
- **Frontier — mistakes mined.** `corpus/lessons/round-98.md` `## Mistakes` carries six rows (M98-1…M98-6), each with class, evidence pointer, captured-by and fix.
- **Routed-defect capture.** The round-97 spot-check's defect 1 (the C1 counter's M4 accepts a wrong-instrument label) is captured as `corpus/QUALITY.md` R155; the wave's two findings are R157 (census confinement) and R158 (pin integrity).
- **Wave.** One v1 wave, 13 seats (`.ufo/waves/round-98/w1-spec.json`, `w1-dispatch.json` `counts.spawn=13`, `w1.ready`), roles: 3 critic, 2 reviewer, 2 mutation-tester, 1 sentinel, 2 executor, 1 scout, 1 connector, 1 scribe — 8 of 13 attack seats (62 %). The first dispatch attempt was refused by the validator (`invalid_spec: spec.milestone exceeds 256 bytes`, `.ufo/waves/round-98/w1-dispatch.err`); the milestone was shortened and the same wave validated.
- **Wave integration.** The 13 seat reports and their receipts are committed under `.ufo/waves/round-98/w1/`; the wave evidence was scanned and 1,257 credential-shaped fixture values in 17 files were redacted structurally (R153; line numbering preserved, before/after digests in `.ufo/waves/round-98/l1/redaction-r98-w1.txt`), and the clean re-scan prints `hits=0`.

## Landed changes

| Change | LOG entry | Commit |
|---|---|---|
| Freeze: `claims.json` (C1/C2 predicates, kill rules, do-nothing controls, the erratum), the C1 control harness and its receipt, the C2 capability gate, the candidate and do-nothing gate receipts, the wave generator | Round 98 bullet 1 | `12bb2f98cf9d07bcbc8b62985516cc3ff65d9ae8` |
| C2: four S140 shapes + the widened boundary (selftest 148 → 170), the knowledge entry, the SCORECARD capability row, the round-94 receipt redaction | Round 98 bullet 2 | `e2caf4a1561b544a6ea684b0bcfa975f7e7f6061` |
| C1: `census-at-rev.py`, the census of record regenerated at `e2caf4a1`, the claim erratum, the post-fix control receipt | Round 98 bullet 3 | `e2d3de7b847f8e9bac72a5bc4dea455ea051cf1a` |
| Integration: lesson (six mistakes + wave findings), SCORECARD round-98 section (C1 NOT VERIFIED, C2 VERIFIED with erratum), LOG, SOURCES (S148/S149, used-by completed), QUALITY R155/R156/R157/R158, the instrument's doc-only corrections (F1/F2/F4), the knowledge entry's F3/D4 fixes, the l1 receipts | Round 98 bullets 4–5 | `279077467801f5792e7739e2b1182c27e924b16d` |
| Wave evidence: spec, dispatch, ready/ready.dispatched, results (13/13 settled, 0 dead), the validator refusal, the 13 seat reports and receipts, the structural redaction | Round 98 bullet 5 | `d00c9ecc83b08bb488548e72c1a2792a03743041` |

## Before → after measurements

| Claim | Before | After | Counting command | Commit measured |
|---|---|---|---|---|
| C1 — **NOT VERIFIED on P1/P2; P3 stands** | the census of record recorded SKILL **132/701 = 18.83 %**, corpus 1202/4766, lane 1227/5152, scope 224 files, with no revision | the census records `measured-at: e2caf4a1…` with pinned SKILL **162/732 = 22.13 %**, corpus 2551/7559, lane **2589/7961 = 32.52 %**, host-inclusive SKILL 166/732, host-owned 78 — but the pinned rate is **not revision-stable** (the same rev measures 2589/7961 clean and 2591/7961 with a contaminated scratch parent), the exact command failed `rc=2` under earlyoom in the wave, and the frozen `harness_sha256` matches no committed harness | `python3 -B corpus/instruments/census-at-rev.py --lane . --check corpus/instruments/citation-survival.md --work <scratch>` | `e2d3de7b` (census), measured-at `e2caf4a1`; wave receipts `.ufo/waves/round-98/w1/CriticClaimsC1.md`, `ReviewC1Census.md` |
| C2 — **VERIFIED-pending-closure on K1–K7** | selftest 148 cases; four shapes absent; five shapes' right boundary refuses a real token followed by `_`/`-`; the round-97 instrument misses all nine planted shapes | selftest **170** cases; the four shapes present; the five boundaries widened; K1–K7 pass at the landing at two seeds; K7: base widened hits 0 → landing 5 | `python3 -B .ufo/waves/round-98/c2/capability-check.py --lane . --rev e2caf4a1561b544a6ea684b0bcfa975f7e7f6061 --work <scratch> --instrument-sha256 45f8d226b65e5bf16b9323bfc246c2748319713af5740a608838d6a6eb6f9f0e --gate-sha256 8b6f849349157a91dd7a2a3998c1f3956e8fed2dbd565c40815660cbd71cc8e6` | `e2caf4a1` |
| — (guard) | depth:density 273.2 | 273.2, unchanged (`SKILL.md` untouched) | `python3 corpus/instruments/density.py SKILL.md --label r98`; `git diff --stat 2133f5bd <tip> -- SKILL.md` empty | `e2d3de7b` |

## Sources & frontier

Census before → after (same command both sides):

```
$ cd /home/vgpnk/Projects/shokunin && bash scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kasegi
kasegi ok  /home/vgpnk/Projects/shokunin/kasegi-shokunin/corpus/SOURCES.md   (rc 0)
```

- Rows: **147 → 149** (`grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' corpus/SOURCES.md` prints 147 at the base and 149 in the working tree); malformed rows 0; the seven inherited W04 duplicate-URL warnings unchanged (S028, S029, S072, S076, S080, S085, S143).
- Rows added by tier: **S148** (`docs`, tier A, `mined`) — GitLab secret-detection rule prose, `rules/mit/gitlab/gitlab_session_cookie.md` at commit 59ada1f4, which states the session cookie's 64-character hexadecimal value and the optional `cell-<ID>-` prefix; **S149** (`docs`, tier B, `mined`) — the same repository's per-rule prose for the two IAM forms (`gitlab_iam_refresh_token.md`, `gitlab_iam_authorization_code.md`), which state the `gliamrt-`/`gliamac-` prefixes and the IAM service's availability qualifier. Both were opened this round (HTTP 200 via the repository-files API at their recorded digests); the Gate block records URL, access date and a ≤25-word located quote for each.
- Rows touched old → new: **S140** used-by `corpus/instruments/capture-secret-scan.py` → `corpus/instruments/capture-secret-scan.py, corpus/knowledge/github-refresh-tokens-and-gitlab-jwt-tokens.md, corpus/knowledge/gitlab-remaining-token-families.md, corpus/knowledge/gitlab-routable-and-versioned-token-forms.md, corpus/knowledge/gitlab-iam-ci-build-and-session-token-shapes.md`; **S144** used-by `corpus/instruments/capture-secret-scan.py, corpus/knowledge/gitlab-routable-and-versioned-token-forms.md` → `…, corpus/knowledge/gitlab-remaining-token-families.md, corpus/knowledge/gitlab-iam-ci-build-and-session-token-shapes.md`. Both statuses stay `mined`, both rechecks stay `180d`. The round's earlier "no new row" assertion was false and is corrected in `corpus/SOURCES.md` and the lesson.
- Frontier rows advanced: none (no F-row admission this round; the round is a capability/verifiability move, not a frontier admission).
- Sources opened this round: S140 (live 403, capture is the base), S144 (live 200, 67,805 bytes), S148/S149 (live 200, API, digests recorded). Evidence `.ufo/waves/round-98/l1/source-reopen-r98.txt`.
- Assimilation: none adopted (the staged ids collide with the lane registry by construction; package adoption waits for a later round).

## Trend verdicts

- **expansion: improved** — the four further S140 rules land as a sourced knowledge entry on ground the coverage map does not hold (no credential-shape row); two new rows (S148 tier A, S149 tier B) ground the session cookie's value format and the IAM prefixes in the vendor's prose; the `capture-secret-scan` capability row is extended; S140/S144 `used-by` cells were completed.
- **quality: improved** — the scanner gains four published shapes and the widened boundary (selftest 148 → 170); the census of record is now a reading of a named revision with a pinned rate beside the host-inclusive one (before: `132/701` from an unnamed 224-file tree); the wave-evidence redaction (1,257 values) and the doc-only corrections (F1/F2/F3/F4) are landed; R155/R156/R157/R158 added.
- **discernment: improved** — six mistakes mined, and the wave's falsification of C1 is reported rather than smoothed over: the "revision-stable" label is false, the harness pin matches no committed harness, the control set kills only 5 of 12 mutants, and the check verifies only the pinned line. The wave's C2 qualifiers (the boundary superset, the unbound ci-build boundary, the session-cookie strictness) are recorded and routed.

## SHONEN

- `[~]` SKILL.md contains real decision tables, error patterns, checklists, cited sources — evidence `corpus/lessons/round-47-verifier-spotcheck.md:94`; unchanged this round (`git diff --stat 2133f5bd <tip> -- SKILL.md` empty).
- `[~]` At least one end-to-end domain task executed and logged in LOG.md — evidence `corpus/practice/curl-h1-1913733/report.md` and `corpus/practice/curl-ibb-h1-1997312/report.md`; unchanged this round.
- `[~]` Instructions executable by an agent without oral context — evidence `corpus/lessons/round-47-verifier-spotcheck.md` (Declared-root recheck observations); unchanged this round.
- `[~]` No cross-domain bleed (PROVINCE.md still accurate) — evidence `PROVINCE.md`; unchanged this round (`git diff --stat 2133f5bd <tip> -- PROVINCE.md` empty).

## Round shape

One v1 wave of 13 seats under `scripts/hyaku/ufo-wave-policy.json` (band 8–16), 13/13 settled, 0 dead; attack seats 8/13 = 62 % (3 critic, 2 reviewer, 2 mutation-tester, 1 sentinel); 2 executor, 1 scout, 1 connector, 1 scribe. The L1 holds the canonical planner seat (the validator rejects a `planner` lane); no bounded planning data-walk rode another seat. Residual call: none. Round total 13 seats.

## Wave findings

All thirteen seats settled; none died (`.ufo/waves/round-98/w1-results.json`, `seats=13`).

**C1 — NOT VERIFIED on P1 and P2; P3 stands.** CriticClaimsC1: the exact frozen command printed `CENSUS-CHECK fail reason=resolve-rc-15 rc=2` on three attempts (earlyoom SIGTERM on the 2–3.5 GB `resolve.py` child, journal-attributed), and — the substantive defect — the pinned rate is not revision-stable: the same revision `e2caf4a1` measures 2589/7961 in a clean scratch and 2591/7961 in a scratch whose parent carries `MISSION.md` and `.ufo/…`, because two `../` citations (`corpus/knowledge/source-tree-loss-2026-09-28.md:315`, `corpus/lessons/round-20-recensus.md:4`) resolve against the extract's parent; the landed census passes against one cache and fails `pinned-mismatch` against the other. ReviewC1Census reached the same finding independently (F1) while re-deriving the numbers (VERIFIED: 162/732, 2551/7559, 2589/7961, host-owned 78). ExecC1Indep AGREE on the numbers and P3. MutC1Counter: 5/12 mutants killed, 7/12 survive (measured-at format/length, `--write` revision validation, the host-owned line, body provenance, resolve rc, pinned semantics). CriticHarm: H1 the frozen `harness_sha256` matches no committed harness (freeze `0488d796…`, landing `d9713268…`), H2 the `\-` SyntaxWarning. ScribeGate: D1 the dispatch's census numbers are the base reading, D2 the harness pin, D3 the used-by gaps, D4 the entry's stale `verified-at`, D5 the redaction line count, D6 the uncommitted live page, D7 the tally, D8 uncommitted evidence, D11 the 219 figure — all corrected in the integration commit. The check also verifies only the pinned line: body hand-edits, host-line tampering, a `measured-at` re-point and a poisoned cache all pass (CriticClaimsC1 §4). Routed to round 99: confine `../` walk-outs to the measured tree (R157); re-pin the harness and the instrument (R158); strengthen the check to verify the body and the host-owned line; add controls for the seven survivors.

**C2 — STANDS on K1–K7.** CriticClaimsC2 PASS at seeds 777001 and 424242 (no kill condition met); ExecC2Probe CONFIRMED (12/12 grammar-derived positives, 15/15 negatives, 0 extra; the round-97 instrument misses 22/22); MutC2Counter 13/13 required mutants killed; SentinelShapes PASS for all nine shapes; ScoutSources STANDS against gitleaks 8.30.1 running the upstream rules (1048 probes, 180 mismatches all tails upstream cannot match, zero divergences on the two IAM shapes); ConnectorOverlap NONE (no sibling overlap). Qualifiers: F1 the widened boundary is a superset of S140's class, not the class (statement erratum; the regex is kept), F2 the SyntaxWarning, F3 the entry's line-break limit contradicted the instrument, F4 the S140 line citation (294 → 293), G1 the ci-build boundary is unbound by K3 (M14 survives), G3 K3 does not bind the session context (M16, killed by K2), G4 the selftest does not bind the registration length (M17), and the behavioural limbs are passable without the sha pin (counter-coverage). ScoutSources also found the upstream per-rule prose files: S148/S149 are added and the round's "no new row" assertion is corrected.

## Stale-lane

Respawn-per-round driver; no other mission of this lane is open.

## Tool installs

None.

## Open L0 questions

None new. The standing questions (the lost domain roots, kasegi round-15) remain open and are not affected by this round.
