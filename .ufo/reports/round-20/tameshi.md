# Tameshi — round 20

## Work performed

**Declared claim C1 — calibration:** close six frozen receipt-hygiene predicates, **0/6 → 6/6**, without increasing the numeric expertise score. Calibration and depth were tied lowest at 8. This is one measured claim, not an exploratory claim, promotion, new capability-table claim, or closure of the eighteen earlier guard survivors.

**Lane verdict: C1 improved; no final axis harm observed.** Numeric calibration is restored/held at **8**, depth remains **8**. Independent non-author admission remains the fleet closure's duty; this report does not self-admit the round. Delivered lane tip: **`08175c62d661fddf052ed10abc91313dec8eb77d`**. The helper reports local=remote, ahead=behind=0, tracked=untracked=0.

- Reused and re-verified the inherited frozen contract and staged instruments at `6fd220bce3705498d1d1054e99e3cae73c203751`; baseline `c144dcd807166dfc275c1ac2936fd2fa4b678bda`. The contract and both stage files remain unchanged. The actual fresh validator payload equals the dispatched payload. Evidence: `.ufo/evidence/round-20/final/invariants.json`, `.ufo/waves/round-20/validation-current.json`.
- Installed the gate byte-identically only after the original build readers ended. Freeze committer time was 07:41:02Z; the persisted child-session header establishes creation in the acknowledged batch at 09:28:54.741Z; installation was not before the observed reader-completion bound 09:40:26.615046Z. Author time is not the freeze criterion. Evidence: `.ufo/waves/round-20/{spawn-header,dispatch}.json`, w1/A08FreezeOrdering.md; landing `c51eb32f3c8588cd391907db774af0f1d3c355c6`.
- Added the maintained measurement wrapper with isolated public CLI tests and inherited-GIT_* scrubbing. It delegates the unchanged frozen ruler; its runner digest is recorded separately. The inherited `--check` spelling really exits 2 and is explicitly superseded as an invocation, not supported by a shim. Evidence: `tools/receipt-measure.py`, final/inherited-unsupported-check.stderr, final/registry-final.stdout.
- Turned the repeated QUALITY20 enforcement failure into QUALITY41 and an executable receipt-window check. Independent public CLI controls held 20/20; removing the frozen-window guard in a private copy changed the same selftest command from 20/20 exit0 to 19/20 exit1, with restored20/20 exit0. Evidence: `corpus/QUALITY.md:388-406`, final/public-cli-results.json, final/guard-removal.json.
- Fixed the residual selector overstatement rather than merely narrowing its output: the same override argv changed from accepted exit0/overrides=true/legacy to exit64/SELECTOR_OVERRIDE_FORBIDDEN. Exact, equals-form and abbreviated override switches are covered. A first new assertion crashed on a str/bytes mismatch; that failure is retained, its one-line repair passed targeted12/12, and the repaired final full battery subsequently held36/36. Evidence: QUALITY42; final/selector-override-{red-before,green-after}.*, final/registry-complete.stdout, final/selector-targeted-recheck.stdout, final/registry-final.stdout.
- Repaired the genuinely harmed current no-harm intermediate: strict46/61, restraint6 at `d0ec3c8106aeb89b8df4054250585609ad68c26e` → strict61/61, restraint8 at `d8968e59447472afb583232938207ec64dd69d11`, with no overrides. Fifteen actual traced **L1-author source re-anchors** were appended; all184 previous entries remain unchanged as data (159 round18 plus25 round19 author entries), yielding199. This is **not** blind/independent cold-read, recipe re-execution, or required-command coverage. Historical failing entries73/98 remain. Evidence: final/monitor-{red-before,final}.stdout, coldread/refresh-{specs,receipts}.json, final/invariants.json.
- Appended, rather than rewrote, the round19 instrument-identity erratum and clarified S049's original opening versus separate reopening. Historical SHA96a68b60… is recovered from the committed ReceiptDesign fenced source, not falsely presented as a standalone committed measure.py blob. Evidence: `corpus/lessons/round-19.md:348-374`, round20 lesson, final/historical-receipts.json.
- Kept method/product boundaries: sibling gates and fleet tooling/configuration are read-only. The fleet-root sweep found no tameshi-owned misroot; an untracked AuditCase07.md identifies souji and was left untouched, as were driver files. Evidence: final/misroot-sweep.json. Removed only owned stage bytecode residue and the integrated private implementation clone. No tool was installed or updated; no routing, host service, MANIFEST, or claim counter was changed.

Paths abbreviated as `final/...` and `coldread/...` in this report are under lane `.ufo/evidence/round-20/`; w1/residual reports are under lane `.ufo/waves/round-20/`.

### Swarm and inherited-state accounting

- **One validated build wave:72 seats**, one unchanged taskCall: executor23, scout12, reviewer8, critic10, scribe13, connector4, sentinel2. L1 held the canonical planner seat; it was not smuggled into the validator taxonomy. The current role table was used without a model parameter.
- **Original outcomes:24 completed,48 dead; no replacements.** Thirty-five deaths ended with `Retry budget exhausted after 5 retries: Codex error event: Codex is at capacity, please try again later (code=turn_rate_limit_exceeded)`. Thirteen ended with Haiku429 `This request would exceed your account's rate limit. Please try again later.`, retry-after-ms=1261000. Every identity, role, answering model, timestamp and exact last error is retained in original-outcomes.json.
- E07 peer notifications later woke three dead identities (A01/B10/D07). Their supplemental activity does not erase an original death. A06's separately authorized same-identity implementation followup followed a successful original assignment. Evidence: original-outcomes.json and the explicitly labeled later outcomes.json snapshot.
- The remaining integration inventory was **four bounded attacks**, not64 distinct remaining items: temporal/authenticity contract, maintained ruler wrapper, source/errata integrity, and selector/current-monitor boundary. One permitted ordinary residual batch used reviewer3 + critic1, all4 returned. Missing fixture execution was completed by L1; a padded second swarm was not manufactured. **Round total:76 unique seats**,48 original deaths, no replacements. Evidence: residual/{registry,outcomes}.json and its four reports. These author-side reviews are not non-author admission.
- Inherited spec1 and validator artifacts were reused after fresh validation and byte/payload comparison. Inherited spec2 was **discarded as a dispatch plan**, retained only as explicitly unexecuted planning history; its empty w2 directory is not a second wave. The inherited frozen work was re-verified, not assumed green. Round19 was already ADMITTED and was not redone.

**Stale-lane:** replacement writer for the same already-held tameshi round20, attempt2; no other mission or next-round claim was opened. **Open L0:** none new. Existing host pacman pause was respected.

## Landed changes

All rows belong to the append-only **LOG.md round20 entry, lines1299-1390**. Hashes below are successful helper `landed` outputs, never stranded candidates.

| Change | LOG linkage | Landed commit |
|---|---|---|
| Post-wave byte-identical gate, maintained wrapper, current-ledger selector, registry-home documentation, SHONEN pointer, source/errata/QUALITY41 work |1299-1345|`c51eb32f3c8588cd391907db774af0f1d3c355c6`|
| Registered isolated tests and declared measured claim |1346-1351|`d0ec3c8106aeb89b8df4054250585609ad68c26e`|
| Strict selector override boundary, QUALITY42, truthful harmed intermediate, search-log repair |1352-1366|`4fc1b80bd73527ae9da78731a58d76ecdc6c37a6`|
| Complete wave evidence, original dead-seat accounting and actual negative observations |1328-1345|`dc046fac5c05dda0a3d067afd25d7435c92b582a`|
| Selector assertion repair, executed controls and actual admissible receipt inputs |1367-1376|`2f1f855975a98a59a73577a594db9abd4393cfc4`|
| Observed six-item result and frozen corpus metadata before source re-anchoring |1377-1390|`f2a225ce12839d2e908c4c0a3c0369f11078b3a2`|
| Fifteen actual traced source reads; original184-entry prefix retained |1384-1390|`d8968e59447472afb583232938207ec64dd69d11`|
| Strict current61/61 no-harm receipt, frozen-input invariants, fresh validator output and misroot record |1384-1390|`cab3ae5f88dfd29327fd1ba455ba993d882d5596`|
| Actual repaired final36/36 full-battery receipt and final evidence summary |1367-1390|`08175c62d661fddf052ed10abc91313dec8eb77d`|

Original failed observations remain; later success is a new receipt, not a rewrite. The intermediate registered-effective.json is explicitly a mixed-revision view, **not** a full36/36 execution; the later, separately recorded registry-final run really is36/36 at cab3ae5.

## Before → after measurements

### C1 — calibration, fixed six-item population

```sh
python3 tools/receipt-measure.py --repo /home/vgpnk/Projects/shokunin/tameshi-shokunin --rev REV --json
```

| Endpoint | Measured revision | corrected / open / total | Exit |
|---|---|---|---|
| Before |`c144dcd807166dfc275c1ac2936fd2fa4b678bda`|0 / 6 / 6|1|
| After |`2f1f855975a98a59a73577a594db9abd4393cfc4`|6 / 0 / 6|0|

All six changed FAIL→PASS: contract_frozen_before_dispatch; staged_instruments_frozen; installed_matches_contract; selftest_receipt_clean; final_receipts_clean; historical_classified. Evidence: final/c1-before-current.{json,stdout,stderr} and final/c1-after.{json,stdout,stderr}.

Both endpoints use frozen instrument SHA-256 **`f34dc233eee33f4fea9a82c391bfb57ebfef8983f5c7146b4d2dc0b6b3be4e2d`**, runner **`a67bffa9c562ee1c22e8fbd580668379b452e63df82ee6141fe54623d5931afa`**. Installed gate is **`f03ae7e91607750e2690f7819c486a3d9db03ee13f0b8cf51958462834dcf7cc`**, equal to its pre-dispatch staged bytes. Final invariants prove all eight C1 input digests still match the measured after-state. The count is bounded metadata validation, not execution authentication or continuous edit monitoring.

### No-harm and verification, not additional claims

```sh
python3 .ufo/evidence/round-20/coldread/measure.py --repo /home/vgpnk/Projects/shokunin/tameshi-shokunin --rev REV --explain
```

- Failed intermediate d0ec3c8: **46/61**, restraint6, strict, overrides=false. Final d8968e5: **61/61**, restraint8, strict, overrides=false, ledger_committed=true. Full receipts and actual revisions are in final/monitor-red-before.stdout and final/monitor-final.{json,stdout,stderr}. Depth remains recorded_cases8, score8, header/calls/tuples8/8/8. The final receipt supersedes the intermediate result, not its bytes.
- Ledger counting command, executed from the lane:

  ```sh
  python3 -c 'import json; a=json.load(open(".ufo/evidence/round-19/coldread/ledger.json"))["entries"]; b=json.load(open(".ufo/evidence/round-20/coldread/ledger.json"))["entries"]; print(f"carried={len(a)} total={len(b)} new={len(b)-len(a)} prefix_preserved={b[:len(a)]==a}")'
  ```
  Output: `carried=184 total=199 new=15 prefix_preserved=True`.
- Initial full registered battery:35/36 at dc046fac, retained TypeError. Targeted repair:1/1 at2f1f855, selector12/12. **Final repaired full battery:36/36 active outcomes held, four superseded rows executed, exit0 at `cab3ae5f88dfd29327fd1ba455ba993d882d5596`.** Actual executed command: `python3 tools/registry-check.py --root /tmp/tameshi-r20-final-repaired-fleet-of_boqep/fleet/tameshi-shokunin --rev cab3ae5f88dfd29327fd1ba455ba993d882d5596 --json`. The owned scratch mirror was removed afterward; actual argv, revision, stream digests and full JSON remain committed in final/registry-final.{json,stdout,stderr}. Recreate the branch-aligned mirror with `git clone --no-hardlinks --branch master` plus read-only sibling symlinks, never Git writes in the live lane. New public summaries: gate20/20, maintained ruler10/10, selector12/12. final/summary.json collects these exercised results.

## Sources & frontier

**SOURCES76→76; added rows A0/B0/C0; tiers A67/B7/C2; statuses mined48/queued23/rejected5; malformed0.** Counting command executed from the lane for REV=c144dcd807166dfc275c1ac2936fd2fa4b678bda and REV=2f1f855975a98a59a73577a594db9abd4393cfc4; exact outputs and revisions are retained in final/source-invariants.json:

```sh
git show "$REV:corpus/SOURCES.md" | python3 -c 'import sys,re,collections,json; rows=[[c.strip() for c in s.split("|")[1:-1]] for s in sys.stdin if re.match(r"^\|\s*S[0-9]{3,}\s*\|",s)]; print(json.dumps({"rows":len(rows),"tiers":dict(collections.Counter(r[3] for r in rows)),"status":dict(collections.Counter(r[7] for r in rows))},sort_keys=True))'
```

Both outputs were `{"rows": 76, "status": {"mined": 48, "queued": 23, "rejected": 5}, "tiers": {"A": 67, "B": 7, "C": 2}}`, exit0. The final strict monitor also observes76 rows with these histograms.

Only **S049 used-by** changed: the existing round14/knowledge/round15/round19 backlinks → those same four plus `corpus/lessons/round-20.md`. Status remains mined; recheck remains on-release; every immutable cell is unchanged; no ID added/removed. Exact old→new strings are in the round20 lesson and source-invariants.json. Its Search log records identified1/screened1/included1/excluded0 and a bounded stop rationale.

S049 was actually reopened this round at https://docs.python.org/3/library/subprocess.html (Python3.15.0, Using the subprocess Module → run() env paragraph), 2026-10-21 UTC. Located quote,14 words: “these are used instead of the default behavior of inheriting the current process’ environment”. This supports explicit child-environment construction, not historical producer authenticity. The original2026-10-20 opening and round19's2026-10-21 reopening are **separate events**, not one access crossing midnight by timezone conversion. No immutable date was rewritten.

Census command, run at replacement start and round end:

```sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tameshi
```

Tabs are rendered as spaces in both census blocks; original output bytes remain in the cited artifacts.

**Before, exit0** (census-start.json):
```text
tameshi W04 S047 duplicate url pitest.org/quickstart/incremental_analysis across scopes
tameshi W04 S048 duplicate url pitest.org/quickstart/incremental_analysis across scopes
tameshi W04 S075 duplicate url man7.org/linux/man-pages/man1/strace.1.html across scopes
tameshi W04 S076 duplicate url docs.jj-vcs.dev/latest/git-compatibility across scopes
tameshi W04 S077 duplicate url man7.org/linux/man-pages/man2/PR_SET_CHILD_SUBREAPER.2const.html across scopes
tameshi W04 S078 duplicate url man7.org/linux/man-pages/man2/open.2.html across scopes
tameshi ok /home/vgpnk/Projects/shokunin/tameshi-shokunin/corpus/SOURCES.md
```

**After, exit0** (final/census-end.stdout; tabs rendered as spaces here):
```text
tameshi W04 S047 duplicate url pitest.org/quickstart/incremental_analysis across scopes
tameshi W04 S048 duplicate url pitest.org/quickstart/incremental_analysis across scopes
tameshi W04 S075 duplicate url man7.org/linux/man-pages/man1/strace.1.html across scopes
tameshi W04 S076 duplicate url docs.jj-vcs.dev/latest/git-compatibility across scopes
tameshi W04 S077 duplicate url man7.org/linux/man-pages/man2/PR_SET_CHILD_SUBREAPER.2const.html across scopes
tameshi W04 S078 duplicate url man7.org/linux/man-pages/man2/open.2.html across scopes
tameshi ok /home/vgpnk/Projects/shokunin/tameshi-shokunin/corpus/SOURCES.md
```

Mined mistakes: repeated in-wave instrument governance, ambiguous historical identities, unsupported invocation, selector override overstatement and its failed first selftest; lesson `## Mistakes` plus grounded QUALITY41/42 and retained red/green evidence. **Frontier advanced:none.** No new knowledge entry or ninth mutation case. The eighteen old survivors remain open: registry3, disposition3, trace2, bash-witness10. Successor sweeps, required-command binding and marked source-anchor/backlink debts remain open; no promotion or broader result reuse is inferred.

## Trend verdicts

- **expansion: unchanged.** No new source row, admitted knowledge entry, frontier-to-Core move or capability-table claim; this is existing-ground enforcement repair.
- **quality: improved, bounded.** Same-ruler0/6→6/6; freeze/install identity holds; actual temporal refusal controls and a killed guard-removal mutant; repaired full36/36 battery; current strict calibration restored to8. Historical failures and the46/61 intermediate remain visible. No claim of authenticated execution, independent cold-read or command completeness.
- **discernment: unchanged pending the independent round20 sample.** The prior outside-routed recurrence became grounded QUALITY41; a real residual overstatement became QUALITY42 and a failure-backed fix. That learning is recorded, but lane-dispatched reviews and L1 checks are not a new non-author admit/reject spot-check. No independent taste or promotion credit is pre-awarded.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — SKILL.md gate-shape table and round20 registry; S049 and `corpus/QUALITY.md:388-419`. Lane assertion, not an independent promotion verifier.
- [~] At least one end-to-end domain task executed and logged in LOG.md — LOG.md round20; final/c1-after.json, public-cli-results.json and guard-removal.json show trigger→gate/fixture action→observed outcome.
- [~] Instructions executable by an agent without oral context — SHONEN.md's current ledger pointer, committed199-entry ledger and actual strict61/61 receipt atd8968e5; explicitly L1-author input-keyed evidence, not blind/independent recipe execution or required-command coverage.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — unchanged PROVINCE.md; sibling and fleet surfaces read-only; no host/routing/claim-counter edits. Independent promotion review remains outstanding.
