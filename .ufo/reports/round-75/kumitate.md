# kumitate round 75 — report

Lane: kumitate-shokunin (axes: operability + coverage — orchestration & tooling) · round 75 attempt 1 ·
host Linux 7.2.11-arch1-1 x86_64 (plazir27), node v24.21.0, installed harness `omp/18.15.0` ·
base `c38382d547a1ec21bb7f51b4c08ef08053e7abae` (round-74 close) · measured close rev
`2c7b7203b658959b4fff87f80a4166d7b55c7190` · receipts rev `402428f546ad843cb8c3c744a0313dba77865cf9` ·
final lane tip `c775e9b1f1079e875937f82b287be10e8ae7f61a` (`ls-remote origin refs/heads/master` =
`c775e9b1…`; the pre-filing gate receipts are that commit) · report committed on the fleet repo by `fleet-commit.sh --as kumitate`.

**Declared claims (2, distinct axes).** **C1 — coverage:omp (new live sub-axis): declare and bind every
member of the OMP agent plane**, 3 → 10, instrument `scripts/omp-census.mjs`. **C2 — operability
(integer held at 9, terminal under `f_O`): capability acquisition `origin-tip-drift`**, instrument
`scripts/proxy-check.mjs --tip-drift`. Frozen predicates, kill rules, pre-registered scores and
controls live in `.ufo/waves/round-75/plan.md` (frozen before any seat ran).

**Round shape.** ONE v1 wave of **12 seats** under `scripts/hyaku/ufo-wave-policy.json` (band 8–16),
validated spec + dispatch at `fd7862d4…`; the L1 holds the canonical planner seat (validator rejects
`planner` as a swarm role; orchestrator ruling 2026-10-19). Roles: scouts 2, executors 2, scribes 2,
mutation-testers 2, sentinel 1, reviewer 1, critic 1, connector 1 — attack roles 5/12 = 42 % (the
wave-census tool's fixed attack set counts 4/12 = 33 %), connectors 1. Seats settled 12/12, **dead 0**
(`close/seat-census.txt`, `close/wave-census.txt`).

## Work performed

- **C1 mechanism — declare and bind the OMP plane.** `scripts/omp-census.mjs` gained the base member
  `lsp.json` (source S224) and three chain families — `config-pre` and `agent-pre-named` (source S225)
  and `models-corrupt` (source S054, with the per-store opt-in disclosed as not located) — plus a
  note-binding arm (`--note`, `bound=<b>/<n>`, `NOTE_UNBOUND`, `NOTE_MISSING` exit 2) and 20 selftest
  cases (29 → 49). Evidence: `scripts/omp-census.mjs:1-120` (contract + rules),
  `build/K75ExecCensusRules/K75ExecCensusRules.patch`, `close/census.txt`, `close/census-selftest.txt`.
- **C1 note binding.** `corpus/knowledge/omp-agent-root.md` (74 → 108 lines) now names all 26 base members
  and 9 family ids at internals level and records the two new sources in its provenance trio; it is what
  `OMP_CENSUS: CLEAN … bound=35/35` reads. Evidence: `corpus/knowledge/omp-agent-root.md:1-12`,
  `build/K75ScribeNote/omp-agent-root.md`.
- **C1 adversarial tightening (critic counterexample).** The critic showed that a note whose only content
  is an HTML comment listing every name read `bound=35/35` (`build/K75CriticClaims/note-stuffing.json`).
  Before any claim verdict the L1 tightened the arm — HTML comments are stripped and a name must be a
  visible identifier token — and added two selftest cases; the counterexample is now a red case
  (`close/specificity.txt` third block: 35 `NOTE_UNBOUND`, exit 1; suite 49 cases).
- **C1 specificity and kill proofs.** Shape fixture plus one bogus member → `UNLISTED bogus-member-75.txt`
  exit 1; a 34/35 note → `NOTE_UNBOUND models-corrupt` exit 1 (`close/specificity.txt`); five drop-unit
  mutants each flip the suite to `VERDICT: FAIL` with sorted `FAIL` names identical on an immediate
  rerun (`close/c1-mutants.txt`).
- **C2 mechanism — `--tip-drift`.** `scripts/proxy-check.mjs` gained the additive read-only mode
  (pin → origin HEAD, `commits`, changed paths classified by the proxy's own layer predicates,
  `IN_SYNC` 0 / `MOVED` 1 / `FAIL-CLOSED` 2, `--json`, help text) and 8 hermetic cases (124 → 132).
  Evidence: `scripts/proxy-check.mjs` (mode block + `tipDriftResult`), `build/K75ExecTipDrift/`,
  `close/tip-drift.txt`, `close/proxy-selftest.txt`.
- **C2 kill proofs.** Six mutants: M1/M2/M3/M6 killed; **M4 survives** and is disclosed — the
  fail-closed arm is covered by three sequential guards, so removing the head-null refusal alone still
  yields exit 2; M4b (all four refusal returns neutralized) is killed by the wrong token
  (`FAIL-CLOSED INTERNAL_ERROR`) (`close/c2-mutants.txt`).
- **Sources opened.** S224 (oh-my-pi `docs/lsp-config.md`, tag v18.15.0 `3fedf8d5…`, byte-identical at
  `main`: 17254 bytes, sha256 `04b56a7d…`) and S225 (fleet run-state records, own-work tier B) — capture
  and exemption registered (`close/sources-gates.txt`). Coverage note: 2 scouts + 2 scribes served the
  Gate drafts (`w1/K75ScoutLspDocs.md`, `w1/K75ScoutBackupRecords.md`, `w1/K75ScribeNote.md`).
- **Routed repairs (not claims).** (i) 4th spotcheck-coverage recurrence: README rows +
  `readme-map.json` covered entries for `lessons/round-74-verifier-spotcheck.md` and
  `lessons/round-75.md` → `README_MAP: CLEAN files=181 rows=181 covered=181` (`close/readme-map.txt`);
  (ii) round-74 erratum naming the superseded `25e7eccc…` pin destination (`SCORECARD.md` `## Round 75
  erratum`); (iii) D2/D3 receipt headers (`rev=`, `date=`, `exit=`, `live=` on every `close/` file);
  (iv) considerthese proposal 2 → `QUALITY.md` Q71; (v) SKILL.md gate-registry rows updated for both
  tools, `PROVINCE.md` moved the plane into Core, `corpus/README.md` `## Frontier` records the advance.
- **Stanza re-measure, same work commit.** A 821 → 833, C2/C2_total 179 → 181, `pin.proxy-check`
  `aabf389e…` → `92465ddc…`, `pin.omp-census` `fd4d1c4e…` → `c7065f9d…`; `PROXY: MATCH` under
  `--strict` at `2c7b7203…` (`close/proxy-check-strict.txt`). Nothing else was fitted.
- **Freeze review.** Reviewer seat raised six items across two messages (missing prerequisite sweeps in
  `open/prereqs.txt`, the junk-control clause wording, the hardlink fixture mechanism, the single-line
  verdict form, the C1(c) final-line form, `live=` headers); all were accepted and landed append-only in
  `58a90f29…` (Amendment 1) and `9fe7f1ea…` (Amendment 2) before any claim verdict
  (`w1/K75ReviewFreeze.md`).

## Landed changes

| change | LOG.md entry | commit |
|---|---|---|
| Census rules + binding arm + 20 cases; proxy `--tip-drift` + 8 cases; note, S224/S225, Q71, PROVINCE/README/SKILL, SCORECARD round-75 section + axes row `coverage:omp` + capability row `origin-tip-drift` + Move-log rows + erratum + `## Planned` r76, lesson | `LOG.md` round-75 entry (appended) | `3876217` |
| Stanza A re-measure 832 → 833 (the sentinel's probe script landed after the first measurement) | same entry | `2c7b7203` |
| Close receipts at the measured rev (census, selftests, specificity, mutants, tip-drift, map, sources, seat census, checklists) | same entry | `402428f5` |
| Wave census receipt (12 seats, attack 4, reports 12/12) | same entry | `f297289f` |
| Pre-filing gate receipts (`ROUND_GATE: CLEAN checks=10`, `REPORT_RECEIPT: CLEAN`) | same entry | `c775e9b1` |

All four commits are on `master`, pushed; `ls-remote origin refs/heads/master` reads `f297289f…`.
Freeze/fixture commits preceding the work: `72610fde` (plan + open/base + controls), `fd7862d4`
(validated spec + dispatch), `58a90f29`, `9fe7f1ea` (amendments).

## Before → after measurements

**C1 — counting command:** `cd /home/vgpnk/Projects/shokunin/kumitate-shokunin && node
scripts/omp-census.mjs; echo exit=$?`
- Before at base `c38382d5…` (`base/omp-census-base.txt`, `open/gates-open.txt`):
  `OMP_CENSUS: DRIFT (root=/home/vgpnk/.omp/agent entries=64 findings=40)` + 40 `UNLISTED` lines,
  exit 1 ⇒ `floor(10 × (64−40)/64)` = **3**.
- After at `2c7b7203…` (`close/census.txt`): `OMP_CENSUS: CLEAN (root=/home/vgpnk/.omp/agent
  entries=64 findings=0 bound=35/35)`, exit 0 ⇒ `floor(10 × 64/64)` = **10**. Selftest
  `VERDICT: PASS (49 cases)` (`close/census-selftest.txt`).
- **Verdict: verifies under the corrected reading of clause (c); the literal clause (c) does not verify
  — see Predicate corrections.** Score 3 → 10.

**C2 — counting command:** `node scripts/proxy-check.mjs --tip-drift; echo exit=$?`
- Before at base (`base/tip-drift-base.txt`, `open/modes-open.txt`): `proxy-check: unknown argument:
  --tip-drift` + usage, exit 64.
- After at `2c7b7203…` (`close/tip-drift.txt`): `ORIGIN_TIP_DRIFT: MOVED pin=31c465f15669
  origin=fb7157fcf146 commits=58 changed=241 scripts=57 runtime=23 other=161` exit 1; `--origin
  /fast/scratch/hyaku/kumitate-pin/src` → `IN_SYNC … commits=0 changed=0 scripts=0 runtime=0 other=0`
  exit 0; `--origin /tmp` → `FAIL-CLOSED SRC_REV_UNVERIFIABLE /tmp` exit 2. `PROXY_SELFTEST: 132/132
  pass` (`close/proxy-selftest.txt`); default `--strict` `PROXY: MATCH` exit 0.
- **Verdict: verifies.** Operability integer stays 9 (terminal `f_O`); the capability row
  `origin-tip-drift` enters `SCORECARD.md` `## Capabilities`.

**Supporting readings at the close rev.** Checklists `CHECKLIST: 33/33 pass`, `VERDICT: PASS` exit 0
(`close/checklists-AFTER.txt`) — at open `30/33` with the proxy, census and readme-map items red
(`open/checklists-open.txt`); `README_MAP: CLEAN files=181 rows=181 covered=181` (was `DRIFT files=180
rows=179`, `open/maps-open.txt`); `PROXY: MATCH` (was `DRIFT (C2_TOTAL_DRIFT 179 vs 180; AXES_DRIFT
coverage row=10 derived=9)`, `open/gates-open.txt`); sources census exit 0 at both ends
(`open/census-start.txt`, `close/census-end.txt`, six carried W04); `SOURCES_CHECK: CLEAN (rows=164 …)`,
`SOURCE_CAPTURE: CLEAN captures=56`, `SOURCE_DUPES: CLEAN`, `CITE_SOURCES: CLEAN cited=211`
(`close/sources-gates.txt`).

## Predicate corrections (disclosed, pre-verdict)

The year's lesson (kumitate r42) is that a predicate changed after data is not the claim's predicate.
Nothing below changes a target, kill rule or frozen sentence; each is disclosed so the closure judge can
rule on it.

1. **C1 clause (c) — literal reading does not verify.** The frozen text required the selftest's final
   line to be `VERDICT: PASS`; the tool's preserved final line is `VERDICT: PASS (29 cases)` at base
   (`open/modes-open.txt:4`) and `(49 cases)` at close. The literal clause fails identically before and
   after and cannot discriminate; the corrected reading (`VERDICT: PASS (n cases)`, n ≥ 34, exit 0)
   verifies. Reported under both readings; no literal conformance is claimed.
2. **C1 binding arm tightened after the critic counterexample** (HTML-comment / superstring notes no
   longer bind; two new red cases). This makes the measured arm stricter than the executor's first
   implementation, in the direction of the frozen intent ("bind", not "mention"); its residual limit is
   disclosed (a fenced code block is visible text and still binds).
3. **C1 plan's file/sidecar split.** The plan says the 7 `agent.db.pre-*` findings are "4 files + 3
   sidecars"; they are 3 files + 4 sidecars (kimi58-unblock and kimiroute carry `-shm`/`-wal`;
   `pre-merge` carries none). The total 7 and every counter are unaffected; mined in the lesson
   `## Mistakes` (`number-drift`).
4. **Fixture mechanism.** Plan (b) said "files hardlinked"; the committed builder creates shape-only
   empty files with the live member's mode because `/home` and `/fast` are different devices
   (Amendment 1). Substance unchanged.
5. **Receipt completeness.** `open/prereqs.txt` at the freeze commit carried only identity/version lines;
   the mode sweep and the 57/23/161 classification the plan quotes were appended at `58a90f29…`
   (append-only; the freeze bytes are unchanged) and mined as the round's `plan-quotes-receipt` mistake.

## Sources & frontier

- **Census before → after.** `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root
  /home/vgpnk/Projects/shokunin kumitate` — start: `open/census-start.txt`, `exit=0` (six carried W04);
  end: `close/census-end.txt`, `exit=0` (same six W04). Round start and end both exit 0.
- **Rows.** `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` → **162** at base
  (`git show c38382d5:corpus/SOURCES.md`) → **164** at close (`SOURCES_CHECK: CLEAN (rows=164 …)`).
  Added by tier: **A +1** (S224), **B +1** (S225), C +0. Rows touched old→new: **none** (no
  `status`/`recheck`/`used-by` edit to an existing row; the registry is append-only this round).
- **Frontier rows advanced.** The OMP harness **agent plane** moved from `PROVINCE.md` Frontier into
  Core (`PROVINCE.md` core band bullet; `corpus/README.md` `## Frontier` advance line): 40 of the
  plane's 64 depth-1 members were undeclared at open, 0 at close, and the note binds 35 declarations.
  S224/S225 are the grounding rows; no other frontier band moved.
- **Gate decisions this round.** **Admit S224** (oh-my-pi docs, tier A; URL, access date 2026-11-04 and
  ≤25-word quotes are in `corpus/lessons/round-75.md` `## Gate`; capture `build/L1/lsp-config.md`).
  **Admit S225** (own-work, tier B; four fleet records with line anchors + the zero-hit source sweep).
  **Reject** the `merge/kumitate/` assimilation package (proportionality; flip: a dedicated assimilation
  round) and **reject** `models.db`'s per-store `recoverCorruption` opt-in as an admitted fact (not
  located in the pinned tree; flip: locate the argument at the models.db open site). Spot-check: pending
  the non-author closure.
- **Assimilation (§10): none this round** — the package was rejected at round 74 and re-rejected here on
  proportionality; considerthese proposal 2 was mined into Q71.

## Trend verdicts

- **expansion: improved.** The plane's frontier band advanced into core on ground the coverage map did
  not hold at internals level (40 undeclared members → 0; two admitted source rows; a new live sub-axis
  `coverage:omp` with a re-derivable score). No admitted entry failed its bar.
- **quality: improved.** Both suites grew with cases that hold real counterexamples (49 census cases
  including the comment-only and superstring arms; 132 proxy cases including the three tip-drift arms);
  five C1 drop-unit mutants killed with identical reruns and six C2 mutants (five killed, one disclosed
  survivor with a second, killed mutant covering the same arm); checklists `33/33` and `PROXY: MATCH`
  at close; Q71 adds a registry↔Gate pointer check.
- **discernment: improved.** The critic's decisive counterexample (an invisible-comment note reading
  `bound=35/35`) was turned into a tightened arm, two selftest cases and a disclosable limit instead of
  being argued away; the reviewer's six FREEZE-FIX items became two append-only amendments before any
  verdict; the C1(c) literal/corrected split and the M4 survivor are reported rather than smoothed. The
  outside spot-check remains the closure's to write.

## Round mechanics, limits, inherited state

- **Wave/dispatch.** One v1 wave: `w1-spec.json` (12 items) and `w1-dispatch.json` validated under the
  policy (band 8–16) and committed at `fd7862d4…`; the inline handoff wrote
  `.ufo/waves/round-75/w1.ready` (`l1: KumitateR75`) and the orchestrator dispatched it
  (`w1.ready.dispatched`, 12 names); results `w1-results.json` (12 settled, 0 dead), reports
  `w1/*.md` 12/12 (`close/seat-census.txt`, `close/wave-census.txt`). Residual calls: 0. Round total:
  **12 seats** (the §3 floor was met inside the wave).
- **Limits named.** (i) the note-binding arm is mention-binding, not semantic reading; (ii) the
  `coverage:omp` integer is not an `AXIS_ROWS` term, so `proxy-check` does not derive it (disclosed in
  the axes row); (iii) the `models-corrupt` writer's per-store opt-in is not located; (iv) `A` counted
  runnable files under `.ufo/waves/round-75/**` (probe scripts and harnesses), so its 821 → 833 move is
  evidence accrual, not new product capability (Q26 rules `A` out as claim evidence); (v) a moved origin
  is a legitimate state, so `--tip-drift` exits 1 by design and must not be added to the default
  checklist as an expected-0 item.
- **Inherited state.** No uncommitted lane leftovers existed at open (`git status --porcelain` empty at
  the base). The fleet-root `after` file is not this lane's (created 2026-11-03 20:05, before launch);
  left untouched. No operator/aggregator files edited; MANIFEST untouched.
- **Tool installs/updates:** none. **pacman:** untouched (host-wide pause respected).
- **L0 questions:** none added (nothing blocked on an operator decision).
- **Stale-lane:** not applicable — this round's mission is the only one open for this lane (respawn-per-
  round driver); the round ran to completion and filed here.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — the gate
  registry carries 24 rows with entry command, self-test and pin home (both touched rows updated this
  round, `SKILL.md:610`, `:617`), the `## Verifiable checklist` executes 33/33 (`close/checklists-AFTER.txt`),
  and the new rules cite S224/S225/S054; verifier: pending non-author closure.
- [~] At least one end-to-end domain task executed and logged in LOG.md — this round's two claims ran
  end-to-end on the real host (`close/census.txt`, `close/tip-drift.txt`) and the LOG round-75 entry
  carries their evidence pointers; verifier: pending non-author closure.
- [~] Instructions executable by an agent without oral context — the frozen plan, wave spec, receipts and
  `corpus/lessons/round-75.md` carry every command and expected line; a reader can re-run each receipt's
  argv; verifier: pending non-author closure.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — the connector scanned all 20 sibling lanes and
  the fleet (`OVERLAP: named — tameshi, mado, kotoba, kaidoku, kama, kasegi, mori, chousa, tabi; CONTESTED:
  none`, `w1/K75ConnectorOverlap.md`); the plane's member **content** stays outside this lane (mado's
  refusal boundary respected), and `PROVINCE.md` records the new core band; verifier: pending non-author
  closure.

## Erratum (appended after filing; names the text it extends, the filed bytes above are unchanged)

`round-gate.mjs --close` cannot run on this lane: the jj-colocated repo keeps git `HEAD` detached by
design, so the close arm fail-closes `UPSTREAM_MISSING` (`fatal: HEAD does not point to a branch`) —
receipt `close/round-gate-close.txt`, exit 2 — while the audit arm is `ROUND_GATE: CLEAN
(round=75 lane=kumitate checks=10 errors=0 warnings=0)`. Routed defect: the close arm should read the
lane branch (`master`) or accept a `--branch` argument on jj lanes instead of `HEAD`/`@{u}`; it is a
gate/host defect, not a round-work defect. The pre-report remote check the protocol names was run and
matches: `git -C … ls-remote origin refs/heads/master` printed the lane tip.
