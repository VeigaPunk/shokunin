# critic — falsification of the r11 axis-move (post-mint accounting)

Cutoff stamp: `date -u` → `Tue 29 Sep 2026 03:34:30 AM UTC` (00:34 -03). Main HEAD at measurement: `8afbc8f`.
Read-only honored: only this file written; no commits, no child-repo edits.

The axis-move as briefed ("a mint executed with no ledger record; roster still lists 6; re-key the tables")
rests on two false premises. Killable parts are killed below. The *remnant* that survives is narrower
than the brief: ledger staleness in `ROADMAP.md`/open-row bookkeeping and a matcher-specification hazard —
not an unrecorded mint.

---

## 1. "kama was minted" — vs "provisioned but not minted"

**Verdict: REPAIRED-BY-AMENDMENT.** Minted — real, ledgered, and *not* the act the brief describes.

Both sides argued:

- *For minted:* every Lifecycle clause-(b)/(c) artifact exists. `git -C kama-shokunin log --format='%h %ad %s' --date=iso --all` → `9cee9fc 2026-09-28 22:42:49` seed (SKILL.md, PROVINCE.md, SHONEN.md, AGENTS.md, LOG.md **and** `MINT.md` with the roster-scan table clause (a) requires), `c6199a2 23:15:05` round-1. `git -C kama-shokunin remote -v` → `VeigaPunk/kama-shokunin.git` (clause-b remote). `scripts/shokunin-watchdog.sh:14` → `LANES="... kagi kama"` with `LANE_CWD[kama]`/`:29` model/`:40` axes wired (clause-c).
- *For "only provisioned":* `MANIFEST.json` roster has 6 rows, none kama — i.e., not a rostered shokunin; `ROADMAP.md` has no table row; SHONEN boxes unchecked.
- *Decider:* PROTOCOL's own non-closure-entry clause (`PROTOCOL.md:208-210` verbatim): *"a `type: "mint"` entry records a lane-initiated sibling mint … names its mint evidence pointer, the probation note, and whether the roster/ROADMAP.md rows landed or are pending."* The ledger record **exists and is exactly that**: `python3 -c "import json; m=json.load(open('MANIFEST.json')); print(json.dumps([r for r in m['rounds'] if r.get('type')=='mint']))"` → `rounds[36] {round: 11.5, type: mint, notes: "…kama-shokunin minted in probation… Roster row withheld until >=3 verified self-iteration rounds per the new clause"}`. Landed `git log -S '"type": "mint"' -- MANIFEST.json` → `2d19a64 2026-09-28 22:44:21`.
- The brief's chronology is wrong: it dates the mint to `17c1fad` (00:19:02). `git show 17c1fad --stat` → that commit touched `.ufo/state/*`, `watchdog.log`, `MISSION.md` (the "kama row" = MISSION fleet-shape table line 19), `scripts/shokunin-watchdog.sh`, prompts, reports — **zero bytes of MANIFEST.json or ROADMAP.md**. The mint (entry + seed + first watchdog launch 22:44:08) predates the relaunch by ~95 min.

**Amendment:** the move's title is wrong, not void. Re-scope to *"kama is minted-in-probation: `rounds[36]` is the ledger record (closed or needing-closure: D-40 'stays OPEN, blocked-external' at `.ufo/reports/AGGREGATE.md:1318` is stale — the decision it awaited happened); re-run §12.1/§12.2 and add probation-tracking rows, not a roster row."*

## 2. "MANIFEST roster divergence is a defect" (6 rows vs 9 dispatched lanes)

**Verdict: FALSIFIED.** The divergence is the protocol *working as specified*, and no consumer is harmed.

- `PROTOCOL.md:31-32` (clause d, verbatim): *"only after those rounds land does the operator add the `MANIFEST.json` roster row and `ROADMAP.md` table row — probation state is recorded in `rounds[].notes` meanwhile, not as a roster row."* kama completed rounds at cutoff = 1; gate = ≥3. Writing a roster row **now** would itself be the violation.
- Nothing programmatic reads `roster`: `grep -n "MANIFEST\|roster" scripts/shokunin-watchdog.sh` → 0 hits; the fleet is the hardcoded `LANES=` string (`:14`). Dispatch was never gated on the roster.
- `PROTOCOL.md:409` — *"MANIFEST.json is canonical for rank and roster"* — but canonical-for-roster ≠ roster-must-contain-unprobated-lanes; the same file's own Lifecycle defines the probation exception.
- **Residual defect found while attacking (real one):** `grep -n 'kama' ROADMAP.md` → `:80-86` still reads *"decision pending: mint or record a rejection"*. ROADMAP "mirrors" MANIFEST; post-mint it must read minted-in-probation. Proposed queue text (no key): *"ROADMAP.md:80-86 kama row predates the mint it describes as pending — restate as minted-in-probation citing MANIFEST rounds[36]; §12.2's kama row and D-40 same."*

## 3. "dormancy 0/8" — strongest case FOR a dormant lane, then the counter semantics

**Verdict: SURVIVES — REPAIRED-BY-AMENDMENT (matcher + scope must be specified or the headline is vacuous).**

Strongest case built against it:

- **kengaku (counter 14):** `grep -n 'round 1[23]' kengaku-shokunin/LOG.md` → **0 hits**; `git -C kengaku-shokunin log --format='%h %ad %s' --date=iso -- LOG.md` → last touch `f09ff1f 21:15:23 round-11`. Yet `ls -la .ufo/reports/round-13/kengaku.md` → 4220 B real report (committed via `17c1fad`; grades ok+defect at minimum). So kengaku's last two counted pairs = r13(silent)+r11(active) → **one silent round — ACTIVE, but one silent round from dormant.** This is the live watch row.
- **Literal-matcher attack (the real finding):** the inherited scan `^#{2,3} Round [0-9]+` returns **zero** for every repo-formatted lane — `grep -cE '^#{2,3} Round [0-9]+' kagi-shokunin/LOG.md` → 0 (kagi/kake/kasegi/kumitate/kengaku write `- … — round N:` bullets; kama writes `## round 1` lowercase). Under that matcher, 5 lanes show zero LOG activity ever → 5/8 "dormant", proving the matcher, not the verdict, is the defect. Kotoba (`## Round N`) is the only conforming child repo.
- Per-lane recount under the §13.3 convention ("a round-mentioning LOG entry" = any `round[- ]N` token; pairs = last two dispatched+reported, markers excluded): `ls -la .ufo/reports/round-{12..17}/` + `cat .ufo/reports/round-16/kasegi.md` (marker→excluded) + per-lane `git -C <repo> log -3 -- LOG.md`:
  kasegi pair r17+r15 → LOG has both (`round-17 LOG.md:684`, r15 `eb5b590`) ACTIVE;
  kengaku r13(silent)+r11(active) ACTIVE-watch;
  kake r16+r15 LOG ACTIVE; kumitate r16+r15 ACTIVE;
  kotoba r16+r15 ACTIVE (r14 was silent *and* its debt was recorded inside the r15 entry `:526,563` — counts as r14 activity; r15 273 B marker → excluded);
  kagi r16+r15 ACTIVE;
  protocol: r14/r13 reports are 340/275 B markers → excluded; pair falls to r12+r11 (`LOG.md` `## Round 12 — protocol lane`, `## Round 11 — protocol lane`) ACTIVE;
  aggregator: r10 = 187 B marker (`cat .ufo/reports/round-10/aggregator.md`) → excluded; r9+r8 both real (18604 B, 24058 B) with `LOG.md` Round-9/Round-8 aggregator headings → ACTIVE.
- **Counter interpretation:** `.ufo/state/*.round` `11 17 17 2 18 14 17 17 15` = **live round numbers, not completed counts** — each counter increment is the launch (`grep 'launch kama' .ufo/watchdog.log` → `00:19:34 launch kama round=2` and `cat .ufo/state/kama.round` → `2`). The relaunch did **not** reset continuity: `git show 17c1fad -- .ufo/state/*.round` → `2 +-` per file = value bump (e.g. kasegi 17→18), and kama's files were *created* there (`1 +`). No lane lost rounds; sequence continued.
- **0/8 survives** only as 0/8 evaluable lanes; the headline must carry "kama un-evaluable (n=1)" and name the activity matcher — without that, the number is unverifiable.

## 4. "kama cannot be dormant (n=1)" — could it be born dormant?

**Verdict: SURVIVES.** Rule verbatim (`PROTOCOL.md:37-39`): *"Two consecutive dispatched-and-reported rounds with no `LOG.md` activity flag a shonen dormant … undispatched rounds do not count."* kama completed rounds = 1 (`grep 'kama' .ufo/watchdog.log` → launches r1 22:44:08, r2 00:19:34; `ls .ufo/reports/round-2/` → no `kama.md` at cutoff; `grep -n 'kama' .ufo/l0-questions.md` shows r1-era entries only). r1 was dispatched+reported+LOGged (LOG `## round 1`, commit `c6199a2`). Even a hostile reading can't make one round two; mint-side activity (seed) is not a dispatched round. Earliest possible flag: silence in r2 **and** r3. Attacking from the other side also fails — "never requested mint" is irrelevant; the rule keys on dispatched rounds, not consent.

## 5. "fleet-wrap + relaunch counts as dispatched-and-reported" — pair accounting

**Verdict: REPAIRED-BY-AMENDMENT (key on (lane, lane-round); watchdog 'complete' lines are not the ledger).**

- r1 is a genuine pair: `22:44:08 launch` → lane ran ~55 min → report `round-1/kama.md` 10144 B committed `74768ab 23:15:55` → `23:39:57 wrap … complete`. Launch+report+complete = one dispatched-and-reported round. The wrap didn't fabricate it.
- Edge case that must be specified or the table overcounts: the same (kama,r1) pair emits **four** terminal lines — `grep 'kama round=1' .ufo/watchdog.log` → `23:39:57 wrap`, `23:47:29 wrap`, `23:55:00 wrap`, `00:19:33 complete; respawning`. All three wrap lines are the driver's per-tick rediscovery of an already-finished process; the 00:19:33 line is the relaunch replaying persisted state — **no second report, no second LOG entry, no second commit exists** (`git -C kama-shokunin log` → 2 commits total). Anyone deriving dormancy pairs from log lines instead of report files counts 4 rounds for 1.
- Amendment text for the counting contract: *"a dispatched-and-reported pair is keyed by (lane-id, lane-round) and evidenced by launch-line + report-file-at-`.ufo/reports/round-<lane-round>/<lane>.md`; duplicate terminal log lines for one key collapse to one pair."*

## 6. "aggregator scores its own row" — self-audit integrity

**Verdict: SURVIVES (structural note; bounded, disclosed — not a defect to route as-is).** The aggregator row *is* this lane grading itself, and PROTOCOL has no non-author gate for it (the promotion-gate non-author rule at `:45` covers promotions, not dormancy rows). Three mitigations keep it honest: (a) self-row cells are mechanically re-derivable — every claim cites the counting command (this seat re-derived it: r10 marker→excluded, r9+r8 active); (b) AGGREGATE already names the asymmetry verbatim (`:1052`: *"the aggregator's own absence is the aggregator's to file"*) and files self-defects (`§12.4` items 9–12 exist); (c) markers of the self-row (r5 254 B, r10 187 B) are *publicly* graded failed, so the incentive gradient runs against self-leniency. Residual risk = framing/editorial, not arithmetic. Amendment: stamp the self-row cells `self-graded; re-derive: <command>` — disclose, don't pretend independence.

## 7. Standing gap "dormancy never positively tested" — did mint+relaunch create a case?

**Verdict: SURVIVES — no positive case created.** `grep -n 'NOT respawning' .ufo/watchdog.log` → 20 lines, but they are the wrap phase's per-tick re-detection of 9 already-complete lane processes, **not 9 kills**: every lane, kama included, re-launched in the same minute (`00:19:29-34 launch …` ×9). Zero lanes were left dead; zero became dormant; no lane was renamed/dropped (round-1's `kengaku-shokunin.md`/`web-properties-publishing.md` filenames are pre-relaunch naming drift, not identity changes — IDs stable in `LANES=`). What the wrap+relaunch *did* create: (a) the first **double-completion-emit** hazard (claim 5) — a measurement defect class, not a dormancy case; (b) **kengaku r13-silent** — the nearest-ever live precursor: if r14 completes with no LOG entry, kengaku becomes the rule's first positive firing. That is this refresh's genuine watch row. ("0/7" in AGGREGATE is stale only in denominator — 8 evaluable lanes now, plus kama un-evaluable.)

---

## Net call on the axis-move

Ship it, re-scoped: §12.1/§12.2 re-run is real work and overdue (kama needs a probation row in §12.2 → graduated-to-minted-in-probation; D-40 is stale-OPEN; ROADMAP pending-text is stale; §12.1 needs a kama n=1 exemption row + matcher specification). But the brief's headline — *"a mint executed with no ledger record"* — is **false**: `rounds[36] type:"mint"` at `2d19a64 22:44:21` is the record, and the absent roster row is the protocol's probation clause operating correctly, not drift.
