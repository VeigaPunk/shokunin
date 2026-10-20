# kaidoku — round 19 (attempt 1), 2026-10-20

## Work performed

Declared claims: **C1 calibration** (tied-lowest owned axis), **C2 freshness** (fleet axis, no owned numeric proxy), and **C3 depth** (owned). Author-side verdicts are **improved / improved / improved**, with the bounded measurements and rejected overstatements below. This is not a self-admission: non-author closure remains required, and the carrier-execution process breach is not waived.

Baseline **B**: `8a8da7e19375aadc66c6bcbff0bbcbb596048fb0`. Verification source **S**: `b26a6c42207a859e70bd892c7e89a5befedf379b`. Retained verification **E**: `2a6229f2fb415ba8efecbc2ae24e69ec89b64986`. Delivered lane tip **A**: `321da6300d5e3cefdb7bca4fa3114714ec166fd4` (all new shipping hashes below are the lane helper's `landed` hashes).

Paths below are lane-relative under `/home/vgpnk/Projects/shokunin/kaidoku-shokunin`, unless identified as fleet paths.

- **C1:** addressed all seven R18 routes with append-only named corrections and revision-scoped substance checks: MIDMAP-LISTSTEP, VALIDATOR-DIGEST, STRICT-BASELINE, HEAD-ALIASES, DEADSEAT-RECORD, REGISTRY-PINNED and INSTALL-RECORD. The new counter runs code/recomputes Git-object digests rather than accepting correction tokens alone. Source evidence: `corpus/lessons/round-18-verifier-spotcheck.md:191-199`; fixes and limits: `corpus/lessons/round-19.md`; measured record: `SCORECARD.md:2505`.
- **C1 falsification:** wave 2 exposed disconnected digest checks, fabricated baseline/cause records, unrelated pinned paths, swapped install hashes, missing reason, alias and flag-forwarding gaps. Integration hardened the actual call chain and input associations. The post-fix producer retained ten killed mutants and exact restoration outputs, not just booleans (`.ufo/waves/round-19/verify/postfix-mutations.stdout`). Its trust boundary is lane-owned code, not hostile Python revisions.
- **C2:** re-read the configured client requests, npx catalog/cache identity, installed skill, doctor outputs, Ghidra/JDK anchors and fallback readers. Updated PROVINCE and SKILL without shifting PROVINCE coordinates. All three config files request the published package version; that is not a running-server/version or whole-environment-health claim. Both audit-wide doctor calls exited 1; their other registration/provider findings remain visible (`evidence/doctor/`, w1 `LiveConfigPins`, `GhidraJdkRecheck`, `FallbackReaders`). No client config was edited.
- **C3:** frozen predictions/rule at `a1140e76fffdc1be032d9d813dbb686157803bbc` precede every round-19 analysis. Eight official Go 1.25.0 toolchain ELF carriers were analyzed; link was pre-excluded for missing build info. A second pass from producer `279e8b19c51658bfd05b9e31a1c0894ab2e70537` is preserved under `runs/pass2/`, using the unchanged predictions. It resolves the first pass's live binding conflict after the validator forward fix; the first pass was not overwritten.
- **C3 result:** vet reports H1-only Invalid index **13902080** in both passes. Seven non-D logs lack the specific `Go analysis failure` signature. The frozen map-path membership rule confirms, but the full-list forecast is rejected: the comparator reports **7/8**, vet exits 1, both aggregate runner exits are 1. Compile also has a deferred RTTI propagation NPE that the extractor's component filter omits. The enormous shared walk candidate is an unmasked-variadic-bit emulator bug; no whole-walk correctness or clean-analysis sweep is claimed (`corpus/knowledge/2026-10-20-r19-go125-toolchain-replay.md`; w2 `KnowledgeMechanism`, `OutcomeCompile`).
- **Carried work:** r12 gets source row S039 and an append-only custody/artifact-drift disclosure; the author withdraws r12's owned-operability improvement rather than adding an owned proxy. Historical outside admission remains unchanged. Custody repo-root, jj sandbox env/path guard and revpin parent wording are corrected. The jj source stays tool-local; kumitate owns the general routed jj facts (`round-19.md`, w1 `JjRowRouting`, w2 `R12Addendum`, `CarryQueue`).

**Swarm evidence.** Every wave was policy-v2 validated and sent as one unchanged validator `taskCall`; the report trailers are validator additions to the spec prompts, not rewritten tasks. L1 held the canonical planner seat because the validator rejects planner as a swarm role. Code writers used separate baseline clones and delivered patches; L1 was the single integration owner.

| Wave | Seats / roles | Outcomes |
|---|---|---|
| W1 build | **90**: executor17, scout23, revenger4, connector8, scribe10, critic6, sentinel2, reviewer18, simplifier2 | 48 reports, 42 reportless: 9 direct 429 errors and 33 parent-session aborts. No replacements |
| W2 falsify | **72**: reviewer48, mutation-tester4, scout10, connector2, critic4, sentinel2, scribe2 | 72 reports, 72 normal stop records, no dead seat. Two job-cap refusals spawned none; the third identical payload spawned 72 |
| Total | **162**, within 200 | All specs, dispatches, registrations, reports and outcome records committed under `.ufo/waves/round-19/` |

Do not equate report presence with terminal state. W1's raw last-assistant records are 50 aborted / 12 error / 28 stop; 17 aborted and 3 error records have reports. `evidence/wave-outcomes/w1-terminal.json` retains all 90, and `wave1-outcomes.json` separately records the 42 missing-report causes. W2's equivalent record has 72 stops. Actual answering providers/models are retained there; no model parameter was passed to seats. After the parent-session 429, verified partial clones were reused; the failed nested-lint patch was retained as rejected evidence, not integrated.

**Stale-lane:** the sole lane mission is this respawn-per-round round 19. It exceeded two driver ticks but was **progressing**, evidenced by its pushed declaration, freeze, implementation and verification commits; the launch digest is `2026-10-20T15:28:58-03:00 launch kaidoku round=19 pgid=2705676 driver=hyaku-inline attempt=1`. It resumed under the same identity after the 429. No other kaidoku mission is open.

**Installs:** no tool installed or upgraded by round 19. The missing round-18 Go install record is now in lesson round-19 `## Installs`: official go.dev tarballs, versions, full SHA-256s, paths, date and reason. Host-wide pacman pause was respected.

## Landed changes

Every item is tied to LOG's round-19 motivation (`LOG.md:2219`) and measured integration (`:2254`); the additional R17 continuity check is at `:2283`.

| Shipping commit | Change / LOG linkage |
|---|---|
| `85589ac757f9ca3cb25efcd702d0963e25c9c4df` | Declared claims, shared seat contract, W1 dispatch/registration, initial census and emulator prescan; LOG round-19 motivation |
| `a1140e76fffdc1be032d9d813dbb686157803bbc` | Frozen C3 predictions/rule and pre-run runner; LOG C3 freeze |
| `4f6c73f81ae8d31de18377d7ff57e4e10140ce48` | W1 patches, routed/carry fixes, freshness rewrite, first-pass evidence and corpus work; LOG C1–C3 |
| `5e364bd5e6016f030a04b4b8c81830477ebdaf51`, `d0690fd44f46d8a7fe9da5f01c6be723d12abd41` | Install-heading parser repair, W2 spec/dispatch records and verification safeguards; lesson's in-round corrections |
| `279e8b19c51658bfd05b9e31a1c0894ab2e70537` | Final producer-validator identity checks and initial W2 integration, before the preserved second pass; LOG pass2 producer |
| `b26a6c42207a859e70bd892c7e89a5befedf379b` | Final W2 code/source-index/citation fixes, all 72 reports, pass2 evidence, model qualifications; verification source S |
| `2a6229f2fb415ba8efecbc2ae24e69ec89b64986` | Executed 62-command verification, 26 content checks, postfix mutation outputs, W2 outcomes; LOG measured records |
| `321da6300d5e3cefdb7bca4fa3114714ec166fd4` | Final scorecard/lesson/log records, current-binding explanation, retained misroot sweep and repaired R17 continuity receipt; LOG measured records and supplement |

No inherited uncommitted lane work existed at dispatch. Non-author round-18 spot-check bytes and older lessons were not edited. R12/r18 knowledge corrections are prefix-preserving addenda.

## Before → after measurements

The instrument code is from S; the B and S arguments select the committed data. C2 additionally reads the named live host configs. Exact argv, stdout/stderr, exits and tool integrity are retained in `.ufo/waves/round-19/verification.json` and `verify/`.

```sh
LANE=/home/vgpnk/Projects/shokunin/kaidoku-shokunin
W="$LANE/.ufo/waves/round-19"
# REV was B and S, respectively:
python3 -I -B "$W/tools/routed-r18.py" --root "$LANE" --rev "$REV" --strict
python3 -I -B "$W/tools/province-pins.py" --root "$LANE" --rev "$REV" --strict
python3 -I -B "$W/measure.py" "$REV"
```

| Claim | B → S | Verdict / numeric proxy |
|---|---|---|
| C1 calibration | open/named/substance **7/7/7 → 0/0/0**, strict exit **1→0**; QUALITY admission rows **21→22**, old rows byte-identical | improved; owned proxy **10.0→10.0**, delta0, tied-lowest worked |
| C2 freshness | mismatched clients **2→0**, strict **1→0**; final **9** stated claims / **0** unstated clients. Census stale **4→0**, ambiguous/unresolved0, undeclared unchanged2 | improved; no owned numeric proxy. Census is still **FAIL/1**, not PASS |
| C3 depth | current validated bound labels with frozen prediction and comparison **0→8** (`c3.bound_validated`, final `run_tree: pass2`); **8/8** pass2 live receipt validations exit0 | improved; owned proxy **10.0→10.0**, delta0. Comparator **7/8**, both aggregate exits1; no exact-model-success claim |

The census command is `python3 -I -B "$LANE/.ufo/gates/c1-census-v10.py" --root "$LANE"`; it has no `--rev`. Comparison uses the retained baseline run and the final source-time live run, not a historical replay over today's working tree. SCOPE/DATED ranges were not widened. Final G11 and scope-marker error lists are empty.

**Executed verification:** at S, **62/62 expected command exits**, **26/26 content checks**, no failed checks or source/tool-integrity mismatch, pin maps equal at the two recorded instants. Expected red exits include both baseline strict counters, census FAIL and vet's full-list compare. The final verifier re-parses every raw bound log and separately checks the frozen H1 membership rule. An async start was refused at the shared job cap; the synchronous pass ran once and succeeded.

New/changed-tool selftests include province-pins45, routed-r18 13, runner29, receipt-validator26, measure118, wave-outcomes33, custody31, jj sandbox9 and citation33 cases. Post-fix mutation evidence: **10 killed / 0 survived**, pristine and relative-root controls exit0 (`verify/postfix-mutations.stdout`). An additional targeted R17 continuity run at S exits0 with all six old routes closed (`evidence/r17-continuity.receipt.json`); it is not counted among the 62.

**No-harm:** command A map **96/96→97/97**, no missing/dangling entries, depth citations **17/17→17/17**, both scores10.0. LOG/SCORECARD and the r12/r18 entries retain B as a byte prefix; prior lessons and r17/r18 runs/predictions remain identical. The round-19 frozen prediction tree is unchanged. No capability entered; saturation10.0/window10 unchanged. These are bounded structural controls, not a semantic audit of the entire old corpus (`verify/controls-r19.stdout`).

## Sources & frontier

Maintained census command, at both start and end:

```sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kaidoku
```

Start (`evidence/census-before.txt`, 15:32:11 -03):

```text
kaidoku W04 S033 duplicate url github.com/NationalSecurityAgency/ghidra/pull/9348 across scopes
kaidoku ok /home/vgpnk/Projects/shokunin/kaidoku-shokunin/corpus/SOURCES.md
exit=0
```

End at S (`verify/sources-census.stdout`, exit in verification.json):

```text
kaidoku W04 S033 duplicate url github.com/NationalSecurityAgency/ghidra/pull/9348 across scopes
kaidoku ok /home/vgpnk/Projects/shokunin/kaidoku-shokunin/corpus/SOURCES.md
exit=0
```

The W04 is the existing S032/S033 supersession warning, not a new malformed row. Census/histogram: **36→39 rows**, tier **A31→34 / B4→4 / C1→1**, status **mined34→37 / rejected2→2** (`w1/SourcesRowAudit.md`, `verify/sources-census-counts.stdout`).

- **S037:** npm publication/integrity identity only; **S038:** official archive/member provenance only; **S039:** historical own-work Evidence-ID experiment with custody/current-artifact limits. All opened this round, quoted with location/access date in lesson `## Gate`, and mined only against existing cited paths. W2 re-opened both external rows; L1 independently re-opened the registry and Go JSON. None of those publication rows is treated as observed analyzer behavior.
- Existing rows S003/S023/S035 gain the r19 entry in used-by; S024/S026/S031 gain the r12 addendum. Only these six used-by cells changed among S001–S036. Exact old→new values are in lesson `R19-USEDBY-APPEND`; status/recheck/evidence cells are unchanged. S037's in-round used-by extension is also recorded.
- Frontier ground advanced: **none**. The new entry deepens the existing held Go row; the coverage-map chain was extended, not a new surface claimed. Mistake mining produced grounded QUALITY #22 with an observed red state (four uncaused r18 seats, exit1) and retained green (exit0).
- Misroot sweep: fleet `git status --porcelain` exit0 retained in `evidence/misroot-status.txt`. Only watchdog/state runtime entries appeared. No seat-authored misroot file, no copy/deletion, driver files untouched.

## Trend verdicts

- **expansion: unchanged.** One new knowledge entry on held Go ground, no new domain surface or capability. Map97/97 is index integrity, not domain expansion.
- **quality: improved.** Current config/skill/cache statements re-verified; r12/r18 corrections are append-only; Go 1.25 outcome evidence and the raw NPE/walk-model refutations are retained without an 8/8-success overclaim. No discovered stale fact is knowingly left unmarked in the corrected scope.
- **discernment: improved (author-side evidence).** The outside-routed R18 dead-seat defect became a lesson-backed QUALITY #22 and a real red/green record. Wave 2 rejected its own false-green checks and unattainable model forecast. Current-round independent admit/reject sampling is **pending**, not asserted by a lane-dispatched seat.

## SHONEN

- [~] Real decision tables/error patterns/checklists with sources: SKILL's Go routing and round-19 partial-forecast table, source rows and the r19 knowledge entry. Author-side evidence only; no promotion verifier.
- [~] End-to-end domain task executed/logged: static toolchain import → run-bound log → comparison/validation, two preserved passes; `LOG.md:2254`, `runs/`, `verification.json`.
- [~] Instructions executable without oral context: 62-command author-side verification and explicit paths/argv; outside execution of the instructions has not been claimed.
- [~] No cross-domain bleed / province accuracy: scoped pin/host corrections, jj kept tool-local and general jj routed to kumitate; historical broader surfaces are not all re-probed. No outside full-province verifier or promotion.

### Conformance, residuals and ownership

- **Process breach:** InstallRecordDraft executed a carrier's `bin/go version` despite the wave prohibition. It is disclosed in lesson Mistakes row5 and excluded from C3 outcome evidence. Hash checks do not prevent or detect prior execution; no enforcement repair is falsely claimed.
- The amendment's future-dated 16:20 timestamp was explicitly withdrawn in a later amendment; Git chronology shows it was committed at 16:09:17 after first-pass observations. The operative C3 rule was already frozen before analysis; it was not changed after outcomes.
- The first pass's live binding really is red after its producer-file forward fix. Final C3 counts use the producer-matched second pass and live exit0 validations, not a waived gate or rewritten receipt.
- Still open/limited: two census undeclared blocks; nested compare-only lint reads; trusted-revision imports are not an OS sandbox and hostile imported code can compromise the counter; adversarial citation snapshot-slug read escape; the argv identity parser's decoy-package-token case; wave-outcomes key collision for a seat named `causes`; jj selftest coverage gaps. Current inputs do not exercise those residual attacks. No adversarial-authenticity or complete-validator claim is made (`w2/ToolCounterScope.md`, `SandboxSecurity.md`, `SkillRegistryOld.md`).
- Operator-owned observation: the 13:35:56 config rewrite dropped OMP's `enabled:false` field. Main was notified; the lane did not edit/restore client config and used the REA CLI only. General jj ownership remains kumitate's; source overlap is reported, not absorbed.
- **L0:** no new lane question. The pre-existing host recovery/pacman pause remains operator-owned. Admission and non-author closure are Main's duty; this lane starts no next round.
