# kagi round 28 — canonical version tokens; derived anchors bound to their feed rows

Lane: kagi-shokunin (secrets & vault ops). Lane tip at report time:
`fdbe306c55df1aef226d8909ca183379ec376c2a` (pushed, `ahead=0`, clean tree).
Frozen BASE: `3553d499577084a6c98d7078906017840bbf7b28`; measured revision of
the round's counters: `5e847472a66fe0b41bfc4c374a3659eace3bd4f8`.

**This is attempt 3 and it is a documentary close, not a craft round.** The
2026-10-21 attempt ended after a provider content-safety refusal (18:31:49Z,
Codex) plus a Devin weekly-quota failure: the lane work was already pushed at
`899c50b`, the report was absent. Fleet records hold the round —
`.tower/comms/inbox/20261024-r100-recovery-census-tower-survey-summary.md:37`
(`kagi | 28 | HOLD — policy | Never dispatch (content-safety/cyber refusal …)`),
`.ufo/l0-questions.md` line 90 (`kagi | round-28 | Documentary safety-stop
disposition required … not permission to bypass a safety refusal`). Attempt 3
therefore **added no claim, measurement, source row, knowledge entry or
capability**, retried no refused work, and rephrased/rerouted nothing: it landed
the pre-refusal authored artifacts (all dated 15:09–15:28 −03, i.e. **before**
the 15:31 refusal) and had eight read-only seats re-run the committed evidence.
Outside admission stays the operator's; this report does not self-admit.

## Declared claims (frozen in `plans/round-28.md` @ `bdf90f58`, before any work)

- **C1 freshness** (`corpus/release-clock.py`): a version token used for an
  anchor, a table observation or a feed entry must be canonical (no leading zero
  in a multi-digit component; ≤18 digits) and bounded; otherwise a *typed*
  finding (exit 1), never a fired release and never a traceback. Sourced by
  `SOURCES.md` S044/S045/S046.
- **C2** (originally booked calibration): a `derived:` row's anchor must be the
  one stable X.Y.Z named by its `feed_source_id` row's anchor cell; mismatch is
  `DERIVATION` (exit 1).
- Booking consequence accepted in-round (`build/CritC2Axis.md:9`): C2 binds a
  registry/release value, which this lane has always scored as freshness — so
  **the round is ONE freshness claim measured by two frozen counting commands**,
  and calibration carries no claim. All six axes stay 9.

## Work performed

- Inherited (2026-10-21 attempt, re-verified this attempt): frozen claims file +
  START census `bdf90f5`; plan corrections `b9a42c0`, `2dfb534`; candidate
  `62a33b1`; FALSIFY repairs `5e84747`; measured outcomes + strict receipt audit
  `899c50b` (`corpus/lessons/round-28.md`, `SCORECARD.md` §Round 28,
  `.ufo/waves/round-28/final/`).
- **C1 measured** — frozen `python3 -I -B .ufo/waves/round-28/tools/c1-measure.py
  <rev> <label> <out.json>`: MISHANDLED **3/4 → 0/4**, TYPED **0/4 → 4/4**, all
  four refusals named `NON-CANONICAL S040`; control `RELEASE_CLOCK: CLEAN
  (on_release=30 bound=30 unbound=0 observed=30 fired=3 derived=15)` exit 0 at
  both revisions. Receipts `final/c1-before.json`, `final/c1-after.json`;
  independent reproduction of both counts by a verification critic
  (`/tmp/c2crit`-class run, byte-identical fixture stdout).
- **C2 measured** — frozen `... c2-measure.py`: groups ACCEPTED CLEAN **4/4 →
  0/4**, DERIVATION exact **0/4 → 4/4** on precisely each group's ids; control
  clean both sides. Receipts `final/c2-before.json`, `final/c2-after.json`; an
  independent critic rebuilt the predicate from scratch and reproduced both
  directions (`DERIVATION S101…S106` on a synthetic registry).
- `tools/round-conformance.py` — round 27 → `VERDICT FAIL` exit 1, round 28 →
  `VERDICT PASS` exit 0 (`final/conformance27.txt`, `final/conformance28.txt`).
- This attempt: re-stamped `corpus/stamps.tsv` (LC_ALL=C, 91 paths, membership
  unchanged) **after** every doc edit, restoring `CLAIM_LEDGER: CLEAN (claims=65
  deferred=0 stamped=91 ids=65 cited=55 labeled_ids=20 orphans=10
  host_skipped=12)` and `REVISION_AUDIT: CLEAN (stale=0 missing=0 dropped=0
  added=28 invalid=0)`; committed the 1.6 MB census input
  `retained-probes/XTagHistory/raw/vault-releases.json` (directory-add skipped
  it for size while its six siblings were committed — reviewer D-1); added
  `__pycache__/` to the lane `.gitignore` after a lane-root `.pyc` leaked
  (reviewer D-2, proven by `git check-ignore -v corpus/__pycache__/x.pyc`);
  corrected three stale/imprecise scorecard cells and six lesson statements
  (below).
- Eight read-only verification seats this attempt (`reviewer`×5, `critic`×2,
  `scout`×1), all completed, none wrote to the repo: census + registry, ledger +
  revision audit, C1 token attack (sandbox `/tmp/critc1`), C2 attack matrix
  (sandbox `/tmp/c2crit`), scorecard cell audit, lesson/frontier conformance,
  live re-open of S044/S045/S046, misroot/scope sweep.
- **Defects the seats found, all recorded rather than smoothed:**
  1. **C1 fail-open, unfixed and routed** — the FALSIFY sentence "the observer
     now refuses any such token" is false for a period-suffixed token:
     `STABLE_TOKEN_RE` (`corpus/release-clock.py:345`) tolerates a sentence
     period but is used only by `derived_anchor_bound`, while the three feed
     tokenizers (`:781-783`) are `$`-anchored. Measured: title `Python 3.15.01.`
     is **dropped**, an older canonical entry becomes newest, the run prints
     `CLEAN` exit 0; a canonical `Python 3.15.1.` is invisible (reads
     not-fired). The frozen fixture set cannot see it (its titles carry no
     period). Recipe routed to round 29: align the three feed regexes' right
     boundary with `(?![A-Za-z0-9+-]|\.[0-9])` and add one positive + one
     negative selftest pair. Not applied here — it would change the measured
     instrument (`fa9bcc02…`) after the frozen receipts, and the HOLD forbids new
     craft work.
  2. C2's "a cell naming two versions binds none" was true only for two *stable*
     tokens (a second prerelease/4-component token passes) — corrected in
     `corpus/lessons/round-28.md` §C2.
  3. C2 marker-flip + own-source-cell edit passes with `derived=0`, wider than
     the named limit — now stated (§Attempt-3 corrigenda 3).
  4. A derived anchor outside the canonical core can register `fired=1` against
     an unrelated observation (ordering never runs) — stated as inherited debt
     (§Attempt-3 corrigenda 4).
  5. `SCORECARD.md` said `Registry 43 → 49` where the measured registry is 51,
     and `selftest 79 → 106` where the measured count is 114 — both cells
     corrected with the qualifying figure.
  6. The misroot relocation has no byte witness (no hash, no `cmp`; the fleet
     copy was never committed) — the lane copy's sha256 `bf25d726…1fe4647` is now
     recorded in the lesson instead of an uncheckable "byte-exact".
- **Frontier step (§2b).** Registry rows are opened this round (all eight new
  rows opened 2026-10-21 in-round; three of them re-opened live today by a seat —
  HTTP 200, quotes FOUND with their anchors, body digests recorded). Mistakes:
  §Mistakes M28-1…M28-4, each with class · evidence · captured-by · fix; the two
  that claim demonstration are pointed at receipts (M28-1 conformance FAIL/PASS;
  M28-2 was pointed at a *superseded draft* and now points at
  `final/c1-before.json`, reviewer finding). Sourced claim: C1 cites S044/S045/
  S046 through the registered rows' `used-by`.

## Landed changes (all via `scripts/hyaku/jj-lane.sh`, each printing `landed <hash>`)

| Commit | Carries |
|---|---|
| `bdf90f58e43fdcae6291224197afe17812a16b55` | frozen `plans/round-28.md` + START census, alone (conformance debt closed) |
| `b9a42c0e`, `2dfb534b` | plan corrections made before any tool/patch commit |
| `62a33b1bd15217ed729df2ca40c8a30aba3076c0` | candidate: canonical tokens + feed-bound derived anchors |
| `5e847472a66fe0b41bfc4c374a3659eace3bd4f8` | FALSIFY repairs (total feed validation, punctuation, raised-anchor witness, S050/S051) — the measured revision |
| `899c50b42634a3a4ad0b28ab7509786315e2fc2b` | measured outcomes, strict receipt audit, honest frozen-fixture conformance |
| `4839d3f17bef95af192cd0185587b6d5a3b0efd4` | **attempt 3**: pre-refusal authored dirt landed unchanged (instrument corrections, `expectation-migrations.json`, separability fixes, lesson CheckLedger correction, 136 seat reports, wave metadata) |
| `fdbe306c55df1aef226d8909ca183379ec376c2a` | **attempt 3**: limits corrigenda, green ledger (91-path re-stamp last), census input + ignore hygiene |

LOG.md §Round 28 (line 1530 ff.) carries the round entry and the appended
attempt-3 record; `SCORECARD.md` §Round 28 carries the pre/post section and the
attempt-3 close note.

## Before → after measurements

| Claim | Counting command (frozen, unchanged since `bdf90f58`) | Before (BASE `3553d49`) | After (measured `5e84747`) |
|---|---|---|---|
| C1 freshness | `python3 -I -B .ufo/waves/round-28/tools/c1-measure.py <rev> <label> <out.json>` | `MISHANDLED 3/4`, `TYPED 0/4`, one fixture OTHER | `MISHANDLED 0/4`, `TYPED 4/4` (all `NON-CANONICAL S040`) |
| C2 (same claim) | `python3 -I -B .ufo/waves/round-28/tools/c2-measure.py <rev> <label> <out.json>` | `groups_accepted_clean=4/4`, `derivation_exact=0/4` | `groups_accepted_clean=0/4`, `derivation_exact=4/4` |
| control | `python3 -I -B corpus/release-clock.py` | `CLEAN (on_release=30 bound=30 unbound=0 observed=30 fired=3 derived=15)` exit 0 | identical, exit 0 |
| ledger | `bash corpus/claim-ledger.sh verify` | n/a | `CLEAN (claims=65 … stamped=91 … host_skipped=12)` at `fdbe306c` |
| stamps | `python3 corpus/revision-audit.py --history c2cab35bc92e57e39e5489bac3386db078345b3f` | n/a | `CLEAN (stale=0 missing=0 dropped=0 added=28 invalid=0)` at `fdbe306c` |

**Contested fixture-conformance, stated not prettified** (inherited, unchanged):
the *literal* frozen C2 construction (TSV edits only, receipt untouched) already
fails at BASE through `RECEIPT-MISMATCH` (`final/literal-before.json`: G1–G4
exit 1, so ACCEPTED 0/4), so the `4/4 → 0/4` delta depends on the pre-tool
receipt-mirroring amendment recorded in `b9a42c0`. Both readings are in the
lesson; the frozen commands and their text were never changed. The 0/4
"accepted" end-state is real either way; the *delta* is what is contested.
Frozen-fixture conformance is therefore **not** declared met.

## Sources & frontier

`SOURCES.md` rows **43 → 51**, counted with
`bash corpus/sources-census.sh` (lane gate) and
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kagi`:

- START `census-start.txt`: exit **0**, 11 `W04` (`rows=43 A=41 C=2 captures=43`, re-derived from the frozen BASE tree by a seat: `rows=43 A=41 B=0 C=2 mined=39 rejected=3 captures=43`).
- END `final/census-end.json`: exit **0**, 14 `W04`; current re-run today is byte-identical to that receipt:
  `SOURCES_CENSUS: CLEAN (rows=51 A=49 B=0 C=2 queued=1 mined=47 rejected=3 entries_sourced=4 legacy=21 captures=51 inrow=16 inrow_only=0 inrow_nonreproducing=12)`.
- Rows added, by tier: **8 × tier A** (S044–S051), all `mined`, all `used-by corpus/lessons/round-28.md`. Three ground the claim (S044 Python integer-string limit, S045 SemVer §2, S046 `int()`), three are frontier leads (S047 GitHub OIDC concepts, S048 secret-scanning concepts, S049 NIST SP 800-57 Pt 1 Rev. 6 IPD), two are falsify corrections (S050 supersedes S047's missing GitHub.com/GHES qualifier, S051 supersedes S049's latest-final/adoption overclaim).
- Rows touched (status / recheck / used-by), old → new: **none**. `git diff 144babc HEAD -- corpus/SOURCES.md` → 29 insertions, 0 deletions; S047/S049 are byte-identical from the candidate to HEAD (append-only, verified).
- Frontier rows advanced: **3** — the three `corpus/README.md` §Frontier leads each gained their first primary row (S047/S048/S049); no knowledge entry or coverage ground is claimed from them.
- Live re-open today (scout, 2026-10-25): S044 200 / `a875a767…` / quote FOUND under `#integer-string-conversion-length-limitation`; S045 200 / `f9d4b8b1…` / FOUND at item 2; S046 200 / `b45ecfa2…` / FOUND under `#int`. Row URLs, anchors and the recorded 301s reproduce.
- Rejections stay as rows with reason + flip (PyPA normalization, Go `x/mod/semver`, npm node-semver, GitHub releases REST, `git-check-ref-format`, CVE-2020-10735, SP 800-57 Rev. 5 final) — reviewer-checked: no admitted quote exceeds **23** words (limit 25), none lacks URL or access date.
- Assimilation: **none** (no `merge/kagi/` theme taken this round).
- `considerthese/`: no such directory in this lane — no proposal mined.

## Trend verdicts

- **expansion — unchanged.** No knowledge entry, governed host surface or
  capability entered. The eight new rows are claim-grounding/frontier-lead rows
  on held ground; the frontier leads are opened but not turned into lane
  knowledge (explicitly refused this round). The last capability remains
  round 25 (release-clock observation).
- **quality — unchanged, with one open defect.** The round's two counters hold
  under independent reproduction and the default gate is still `CLEAN30`, but a
  verification critic found a real C1 fail-open (period-suffixed feed token
  silently dropped) in the shipped clock, and the round's own prose had
  overstated coverage ("refuses any such token"). The prose is corrected and the
  defect routed with a fix recipe; correcting a false sentence is not a quality
  gain, and the defect is not closed.
- **discernment — unchanged.** A seat found three self-assessment errors this
  round (token totality, the C2 "binds none" absolute, an evidence pointer to a
  superseded draft) that the round's own falsify wave had not caught — so
  self-assessment was over-optimistic until an outside check. No independent
  non-author admission was obtained (dispatched seats do not count), so no
  movement is booked either way; the errors are on the record with pointers.

## SHONEN

`SHONEN.md` — all four boxes are `[~]` (a resolvable pointer, no named non-author
verifier; unchanged this round, no box re-marked):

- `[~]` SKILL.md real decision tables / error patterns / cited sources — pointer `SKILL.md` §Vault-ops decision table + `corpus/claim-ledger.sh citations` (this attempt: `CITATION_GATE: CLEAN (cites=1748 docs=71 unresolved=0 ephemeral=0 labeled=13)`); the file's own cited run is `LOG.md:758`.
- `[~]` at least one end-to-end domain task logged — pointer `LOG.md:20` (round-3 stdin→lock→tmux→serve to the 1Password auth gate, exit 1, `handler exited before becoming ready`).
- `[~]` instructions executable without oral context — pointer `corpus/lessons/round-19-recensus.md:45` (seven safe gates re-run green with identity/pathspec conformance); this attempt re-ran the ledger, revision audit, clock selftest (114) and self-counts (60) green.
- `[~]` no cross-domain bleed — pointer `PROVINCE.md` §Surfaces + `corpus/scope-gate.sh` R1–R11 (`LOG.md:686`, `SCOPE_FALSIFY: PASS (caught=18/18 failed=0)`); contested surfaces still reported, not absorbed.

## Round shape, seats and dead seats

- Inherited waves (2026-10-21 attempt, recorded in `wave-outcomes.json`,
  `build-spec.json`, `falsify-spec.json`): **BUILD 73 seats** (executor 9,
  scout 22, reviewer 12, connector 8, critic 8, scribe 6, revenger 3,
  mutation-tester 2, sentinel 2, simplifier 1) and **FALSIFY 64 seats**
  (reviewer 40, mutation-tester 10, critic 8, scout 6) = **137 seats**, 75 + 64
  seat reports on disk. Planner seat = the L1 (canonical, per the orchestrator
  ruling that the validator rejects a `planner` role). BUILD was refused six
  times at the host job limit before dispatching on try 7 (`build-refusals.json`).
- **Shape conformance defect, reported as such:** the BUILD wave is inside the
  v2 band (64–128) — re-validated today: `plan --spec build-spec.json` under the
  v1 policy returns `{"code":"wave_too_wide","message":"a wave carries at most 64
  lanes (got 73)"}`, while the FALSIFY wave validates under both. That makes the
  round a v2-band build wave **plus** a v1-band falsify wave, i.e. neither of the
  two sanctioned shapes, and 137 seats exceeds the ≤128 combined cap.
- The ≤8-seat residual call the earlier attempt planned was refused
  (`residual-refusal.json`: `"reason": "Background job limit reached (100)"`,
  spawned 0).
- **Dead seats / provider deaths:** `wave-outcomes.json` records `"dead": 0`,
  `"provider_deaths": []`, which the attempt-3 record cannot corroborate — the
  L0 line records a Codex content-safety refusal at 18:31:49Z and a final Devin
  weekly-quota failure. Both statements are reported; the "0 dead" figure is
  treated as unverified, and no seat was replaced.
- This attempt: **8 seats in one batched call** (reviewer 5, critic 2, scout 1),
  all completed, 0 dead, read-only (no seat wrote to the repo; the only
  filesystem changes were a lane-root `.pyc` one seat observed and an L1-run
  `git archive` into `/tmp`). Round total across attempts: **145 seats**.

## Inherited state, misroot, scope

- Inherited uncommitted leftovers (all pre-refusal, mtimes 15:09–15:28 −03) are
  now committed at `4839d3f`, unchanged in substance; the only edits attempt 3
  made to them were the corrections listed under *Work performed*.
- Misroot: one seat wrote its report under the fleet `.ufo/waves/round-28/`
  (`ScribeKnowledgeClock.md`); relocated into the lane, fleet copy removed, and
  the sweep at `git -C /home/vgpnk/Projects/shokunin status --porcelain` finds no
  remaining kagi/round-28 content (the fleet-root strays there — `bm.json`,
  `live*.html`, `s395.txt`, `wb2.html`, `unblob.log`, `write`, `xc.xml` — name
  no kagi content and are left to their owners). The relocation lacks a byte
  witness; see work item 6.
- Push scope respected: lane remote only; no sibling repo, no fleet-root
  template/script/state file touched; the read-only `shokuknow` source tree was
  not opened this round.
- Tool installs/upgrades: **none** (no pacman; host pacman transactions are
  paused). All commands used `python3`, `bash`, `git`/`jj` read-only, `curl`.
- Stale-lane: this lane is on the respawn-per-round driver; **no other mission of
  this lane is open**, and round 29 was not started.
- Open L0 questions: `kagi | round-10` (refs redaction prefix), `kagi | round-16`
  (counter/dispatch contract), and **`kagi | round-28`** (documentary
  disposition of the safety refusal). Attempt 3 appends one line recording the
  documentary close and the open C1 code defect.

## Admission

Claim verdicts: **C1 measured** on the frozen fixture set (MISHANDLED 3/4→0/4,
TYPED 0/4→4/4) with an **open, routed** fail-open outside that set; **C2
measured** (4/4→0/4 accepted, 0/4→4/4 exact) with contested frozen-fixture
conformance. No axis is harmed (all six remain 9) and no axis moved. The lane
does **not** admit the round: it is under a policy HOLD, the round's
fixture-conformance question is contested, a real code defect is open, and
independent non-author verification is the operator's.
