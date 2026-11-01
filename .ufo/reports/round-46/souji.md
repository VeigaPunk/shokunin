# souji — round 46 (Windows-host landing of the frozen claims)

## Work performed

The round's three claims were frozen 2026-10-30 in
`census/round-46/preregistration.txt` (souji lane,
`census/round-46/preregistration.txt`, base 5540250, freeze tip 7f8fa3ca)
before any wave dispatch; that freeze session died before any after-data
existed. This session executed the frozen claims as written, with one
disclosed host adaptation (Amendment 1, appended to the prereg and committed
BEFORE the after-measurements it affects) and one promised-but-missing kill
rule implemented (Amendment 1 addendum). All paths below are under the lane
repo `shokunin-repo-hygiene/` unless noted.

- **C1 (calibration, lowest axis, 7): tip landing-suite receipt.** Before:
  the frozen counter exits 2 could-not-evaluate on this host — six HEAD
  paths with control-character names cannot be checked out
  (`census/round-46/records/c1-host-before.txt`,
  `c1-host-uncheckoutable.txt`), so the naive clean-tree precondition is
  unsatisfiable here. Amendment 1 (prereg-appended, commit `8a793e7a`,
  `42d86abf`) tolerates exactly staged deletions of control-char-named HEAD
  paths; every other porcelain row still kills. The addendum (commit
  `3144c16b`) implements the frozen sentence's "instrument sha256 != pinned
  value" kill rule, which the frozen counter never implemented, and re-pins
  it to the round-base digest (the frozen "r22-attempt2 bytes" target was
  stale — r32 commit 98e5203 changed the instrument's scratch discipline).
  After: counter green at the suite rev and re-confirmed at the final tip
  (see Measurements). Do-nothing control (committed at freeze, before any
  after-data): unfiled=70, FAILS (`records/c1-control-donothing.txt`). Pin
  mutation witness: exit 2 at r28 rev ed270c4
  (`records/c1-pin-mutation.txt`). Suite rider (r45 routed defect 3):
  `records/c1-suite-index.txt` — declared-evidence tip run, landing gate,
  r45 verifier, record-agreement, coverage-agreement, gate-check, census.
- **C2 (operability, 8): r45 register-verifier selftest.** `--selftest`
  added to `census/round-45/c1-counter.py` (commit `8eabfba3`, LF-normalized
  at `bc50661f`): 11 cases over isolated synthetic git repos in caller
  scratch (population/SCORECARD/stub-instrument fixtures in-process;
  digest/rev/scratch refusals through the real main via subprocess),
  expected exits and finding identifiers pinned in
  `records/c2-selftest-expected.tsv`; run receipt `records/c2-selftest.txt`
  = cases=11 pass=11 fail=0, exit 0. Default path proven byte-behavior-
  identical to the frozen r45 bytes at rev 019bccc9:
  `records/c2-repro-after.txt` and `records/c2-repro-wrong.txt` reproduce
  the frozen r45 SUMMARY+exit exactly. SKILL.md registry row's self-test
  cell updated; the r45 disclosed interface debt is closed.
- **C3 (coverage, 8): F4 restore-collision knowledge entry, sourced.**
  `corpus/knowledge/quarantine-restore-path-reoccupied.md` (commit
  `4b316f22`): a plain rename(2) restore onto a reoccupied origin atomically
  and silently replaces the occupant (S110 re-open); RENAME_NOREPLACE
  refuses with EEXIST (S268, opened 2026-10-30, re-opened live 2026-10-31
  by this session); a receipt-gated restore must refuse or rename aside.
  S269 rejected (trash-spec URL 404). README F4 map row names the entry
  (append-only note at README end). No tool change, no receipt class, no
  deletion or restore authority.
- **Non-claim round work.** (a) Session-workspace dry-run census (the
  context-designated hygiene surface), read-only metadata only:
  `census/round-46/workspace-census.tsv` + `.txt` — 17 lane clones (14
  pushed, 3 no-origin-master: kotodama, binary-forensics,
  reverse-engineering), 15 foreign live scratch dirs untouched,
  `helpers-r74/` noted as a stale-candidate for a future round; nothing
  moved or deleted. (b) Host corrections recorded in PROVINCE.md and the
  lesson (absent conf path `souji-shokunin/`; uncheckoutable paths) —
  protocol work, not failure. (c) L0 question filed (L2 floor on this
  host). Mistakes mined: `corpus/lessons/round-46.md` (CRLF churn;
  unimplemented prereg kill rule + stale pin; unanchored filter loop).
- **L2 floor:** no wave dispatch surface exists on this host; the frozen
  32-seat w1 plan (`.ufo/waves/round-46/w1-spec.json`) was never dispatched
  (dispatched=0, completed=0, dead=0). No WAVE-DONE, no seat output, no
  wave verification claimed. L0 question filed (same surface as kake r65 /
  revenger r74 / kumitate r70).

### FRESH-START spot-check — what was ruled out and why

Read all three rejected closures (r43, r44, r45 reports + MANIFEST notes in
the round prompt §7) before executing. Ruled out:

- r43's "counter does not bind captured derived token" — C1 does not
  re-claim derived-value re-derivation; its target is disposition coverage
  at the tip against the committed 66-key register, measured with the same
  r22-pinned instrument bytes both ends (digest pinned in the counter).
- r44/r43's frozen-oracle conflicts (C2 memorizer, h4/h6 defects) — C2's
  selftest pins per-case expected exits AND finding identifiers in a
  committed table, and separately proves the default path reproduces BOTH
  frozen r45 receipts (green + wrong-token) byte-exactly, so oracle drift
  is detectable rather than asserted.
- r45's "different-instrument 0-to-66 is not a calibration improvement" —
  this round claims no numeric calibration gain and no new corrected
  beliefs (calibration stays 7); C1's before/after is same-instrument
  (unfiled=70 control FAIL -> unfiled=0 green) plus the r45 debts.
- r45's disclosed debts — whole-suite tip validation left unrun (now run:
  `records/c1-suite-index.txt`) and the register verifier's missing
  built-in selftest (now built: C2). Both routed debts are closed, not
  re-disclosed.
- Also ruled out: any deletion/move (dry-run census only — quarantine-
  before-delete law), any wave dispatch (no surface), any new source rows
  beyond the frozen S268/S269 (prereg kill rule).

## Landed changes

All recorded in `LOG.md` "2026-10-31 — Round 46" (one entry, all receipts
under `census/round-46/`). Pushed lane branch master; final lane hash
**`32f48da04846489aeb8f6c5662e9bacd742bf245`**;
`git ls-remote origin refs/heads/master` returns exactly that hash.

| change | commit |
|---|---|
| C1 Amendment 1 (drift tolerance; prereg appended) | `8a793e7ae9131578bdec393982760217f620952f` |
| C1 quote_c_style-exact tolerance | `42d86abf75a7b5cfa63d950db9f5761f73e05651` |
| C1 instrument pin implemented (addendum) | `3144c16bde21380bcbedcb783897d01bc2ee3602` |
| C2 selftest + expected table + receipts + SKILL row | `8eabfba3924778e903537b46ae0c20979b1391a2` |
| C3 knowledge entry + S268/S269 + README F4 row | `4b316f22ef0f9a43cee46ff8fd88b65c4e7d64c4` |
| LF normalization (mistake fix; net diff = intended lines) | `bc50661fc72522356625c53043959e7df915f56f` |
| lesson/PROVINCE/SCORECARD/LOG/workspace census/host receipts | `3f58635243a68876633f0af3263ad06b2fccc338` |
| SCORECARD pointer repair + census-after receipt (suite rev T1) | `5cb9aaa2280171005449408dd019aa5bb4eaeedd` |
| whole-suite tip receipts + pin mutation witness (final tip) | `32f48da04846489aeb8f6c5662e9bacd742bf245` |

Round-base for the diff review: 7f8fa3ca... -> 32f48da0...; nine commits,
every one made through the plumbing helper with named paths only, every one
pushed.

## Before -> after measurements

- **C1** (target: every declared-evidence mismatch dispositioned, unfiled=0,
  sanity M>0 and A>500). Command:
  `python -B census/round-46/c1-counter.py --root LANE --rev FULL40 --work SCRATCH`.
  Before (frozen bytes at 7f8fa3ca, this host): `COULD-NOT-EVALUATE dirty
  worktree at run time`, exit 2 (`records/c1-host-before.txt`); do-nothing
  control at freeze (old host, committed before after-data): unfiled=70,
  FAILS. After at final tip **32f48da0**:
  `SUMMARY assertions=533 mismatches=70 registered=70 corrected=0
  exempted=0 unfiled=0 instrument_sha256=a3324916...`, exit 0
  (`records/c1-tip-green.txt` at suite rev 5cb9aaa2; identical SUMMARY
  re-confirmed at 32f48da0). Kill-rule witnesses: pin mutation exit 2
  (`records/c1-pin-mutation.txt`).
- **C2** (target: selftest green over isolated fixtures; default path
  byte-identical to frozen r45 bytes). Before: `--selftest` exits 2
  unrecognized-argument on frozen r45 bytes. After at bytes bc50661f
  (re-confirmed at 32f48da0): `python -B census/round-45/c1-counter.py
  --selftest --scratch SCRATCH` -> `SUMMARY cases=11 pass=11 fail=0`,
  exit 0 (`records/c2-selftest.txt`); `--root LANE --rev
  019bccc9ac97f3cec1a1dea574cc2f81f57fc967 --scratch SCRATCH` ->
  `SUMMARY population=70 unique=66 registered=66 missing=0
  derived_mismatches=0 ...` exit 0, and with `--register-file` (one derived
  token mutated) -> `registered=65 derived_mismatches=1` exit 1 — both
  byte-identical (stdout SUMMARY + exit) to the frozen r45 receipts
  (`records/c2-repro-after.txt`, `c2-repro-wrong.txt`).
- **C3** (target: grounded F4 8 -> 9; gate-check entries=1 ok=1 fail=0;
  census exit 0; coverage-agreement grounded=27 mapped=27 dangling=0
  mismatches=0). Counting commands, at suite rev 5cb9aaa2 (entry + rows
  committed; unchanged through 32f48da0):
  `git grep -lE '^ground: F4' 5cb9aaa2 -- corpus/knowledge | wc -l` -> 9
  (base 8); `python -B tools/souji-gate-check.py --root LANE --round-date
  2026-10-30 --entries corpus/knowledge/quarantine-restore-path-reoccupied.md
  --snapshot-dir census/round-46/sources` -> `entries=1 ok=1 slice_verdicts=8
  slice_total=8 fail=0`, exit 0 (`records/c3-gate-check.txt`);
  `python -B tools/souji-coverage-agreement.py --root LANE --rev 5cb9aaa2`
  -> `grounded=27 mapped=27 dangling=0 mismatches=0`, exit 0
  (`records/coverage-agreement-tip.txt`).
- **Whole-suite tip receipt** (`records/c1-suite-index.txt`, r45 routed
  defect 3): declared-evidence tip `assertions=533 resolved=463 skipped=849
  mismatches=70` rc 1 (expected; 70 historical mismatches, all
  dispositioned), landing gate rc 2 = could-not-evaluate (no committed
  round-46 report at any pre-orchestrator rev; at 32f48da0: findings=0),
  r45 verifier rc 0, record-agreement rc 1 with mismatches=6 = exactly the
  six host-impossible control-char-named HEAD paths (Amendment 1 subject;
  no other residue).

No owned numeric axis score changed (calibration 7, operability 8, coverage
8): C1 re-derives already-committed dispositions; C2 closes a disclosed
interface debt; C3 adds one entry on existing frontier ground.

## Sources & frontier

Rows **191 -> 193** (`grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'
corpus/SOURCES.md`; 191 at base 7f8fa3ca, 193 at 32f48da0). S268 admitted
(renameat2(2) RENAME_NOREPLACE/EEXIST; opened 2026-10-30 by the freeze
session, capture `census/round-46/sources/renameat2-located-quote.txt`;
re-opened live 2026-10-31 by this session, HTTP 200, quotes re-verified
verbatim). S269 rejected (trash-spec latest URL served HTTP 404;
`census/round-46/sources/trash-latest-404.txt`). S110 re-opened 2026-10-30
(`census/round-46/sources/rename2-reopen.txt`), row unchanged. Gate quotes,
dates, locators: `corpus/lessons/round-46.md` Gate. No existing row's
status/recheck/used-by cell changed; no knowledge entry beyond the frozen C3
entry; no frontier row advanced; no Core promotion.

Census before -> after (validator: fleet `scripts/sources-census.sh`):

- Round start, this host: the conf-name form (`validate --root FLEET-ROOT
  souji`) prints `souji missing` and exits 2 — the conf-declared
  `souji-shokunin/` does not exist here (`records/census-conf-name-host.txt`).
  The documented explicit-lane-directory form validates the real registry:
  `sources-census.sh validate LANE-DIR` -> `shokunin-repo-hygiene ok ...`,
  **exit 0**, 56 W04 duplicate-url warnings, 191 rows
  (`records/census-before.txt`).
- Round end: same command -> `shokunin-repo-hygiene ok ...`, **exit 0**,
  193 rows (`records/census-after.txt`).

Mistake mining: three classes captured in `corpus/lessons/round-46.md`
`## Mistakes` (CRLF churn from text-mode writes; the frozen prereg's
unimplemented kill rule with stale pin target; an unanchored filter loop
that widened a six-path repair — no content change, disclosed). Sourced
claim: C3 rests on S268 (opened this round).

## Trend verdicts

- **expansion: unchanged** — one knowledge entry added on existing F4
  frontier ground (no Core promotion, no new frontier row, no capability-row
  expansion beyond the r45 registry repair); the 32-seat wave plan remains
  undispatched, so no repertoire growth beyond C2's closed debt.
- **quality: unchanged** — operable artifacts improved (selftest, suite
  receipt, pin rule) but no corpus knowledge entry was re-verified or
  superseded this round; the LF normalization restored bytes rather than
  changing content.
- **discernment: improved** — the round's green run was spot-checked before
  filing and produced two real captures: the prereg's kill rule was never
  implemented and its pin target was stale (both fixed under a disclosed
  amendment, mutation-witnessed), and the CRLF churn was caught by landing-
  diff review and repaired with a byte-exact net diff. Three mistakes mined
  with evidence pointers; no self-awarded axis score.

## SHONEN

- [~] Real decision tables/error patterns/checklists/cited sources —
  `SKILL.md` registry row for r45-register-verifier now carries a runnable
  self-test command with a committed expected table;
  `corpus/knowledge/quarantine-restore-path-reoccupied.md` Gate cites S268
  (capture + live re-open). No non-author promotion verifier available this
  session (no wave surface); prior rounds' SHONEN boxes remain author
  assertions.
- [~] End-to-end domain task executed and logged — the session-workspace
  dry-run census (`census/round-46/workspace-census.tsv`) executed the
  lane's census-with-receipts craft on the live hygiene surface; LOG.md
  round-46 entry; nothing moved or deleted (dry-run law).
- [~] Instructions executable without oral context — every claim's counting
  command is pasted above with its receipt path; the C1/C2 instruments run
  from committed bytes at named revisions on this host (python + git only).
- [~] No cross-domain bleed — PROVINCE.md host corrections recorded; no
  deletion authority, credential access, history rewrite or sibling-repo
  mutation; the six uncheckoutable paths were indexed to their HEAD state
  and left otherwise untouched.

Assimilation: none — the lane holds no `considerthese/` directory
(named-path discovery, re-verified 2026-10-31); the shokuknow register is
not reachable from this host; the staged merge/souji package collision
(census/round-46/assimilation/, 58 id collisions) remains L0-held from the
freeze session, nothing adopted. Assimilation: none — shokuknow unreachable.

Open L0 (filed this round): the MISSION L2 floor has no dispatch surface on
this host; the frozen 32-seat w1 plan remains undispatched (dispatched=0);
operator to rule waive/provide/keep-unmet. Carried holds unchanged:
certification OFF, K5 HELD, NAMESPACE/reap holds, r44 symlink-contract
disposition, execution-bound hidden-audit attribution.
