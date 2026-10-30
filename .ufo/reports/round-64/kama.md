# Kama — round 64 (attempt 2): wave-f falsification settled; both claims end not verified

Outcome: the run-11 honest stop left wave f undispatched (21 seats spawned, zero reports);
this attempt re-validated the committed wave spec (tasks byte-identical, `plan` exit 0),
re-dispatched it through the inline handoff (`f.ready` l1 `KamaR64` → `f.ready.dispatched`),
and integrated all 42 settled seats. **C1 operability and C2 calibration are both measured
`met=True` on their amended instruments and both end not verified — falsified by wave-f
receipts.** Scores stay operability 8 / calibration 7; no capability enters; no axis harmed;
the round is not admitted by its author. One knowledge entry admitted (frontier step).
Final lane tip `7b00be78ca49ce634515881fe3ddb86262f23872` (`jj-lane.sh state`: local ==
remote, ahead=0, tracked=0 untracked=0; `git ls-remote origin refs/heads/master` prints it).

## Work performed

Declared claims (frozen `.ufo/waves/round-64/controls/freeze.txt` at `f6a4ea9a`, amendments
1/1a/1b disclosed in the same file): **C1 operability** — the process answering the live
`/v1/completions` request plane is the pinned llama-server, bound from procfs
(`tools/kama-completion-live.py` v3 + `tools/round64-c1-counter.py`, 91 controls, 8 evaluator
plants); **C2 calibration** (lowest assigned axis, 7) — the claim registry proves the work was
done rather than printed (`tools/round64-c2-counter.py`, `registry/capability-claims-r64.tsv`,
`registry/capability-regress-r64.tsv`, reconciler `closure_ptr`, `tools/shortcut-tally.py`
56–63). No exploratory claim. Round shape: **two v1 waves summing 84** (b 42 + f 42; band
64–128), no residual call, **round total 84 seats, 0 dead**.

- Pre-dispatch re-validation: `ufo-swarm-wave.mjs plan` on `f/f-spec.json` exit 0, context and
  all 42 tasks byte-identical to the committed `f/f-dispatch.json`; counters re-run green at
  the wave tip `23b3fdb1a925…` (C1 `controls_targeted=91/91 eval_selftest=8/8 met=True`, 74 s;
  C2 all frozen fields `met=True`, 23 s; receipts `.ufo/waves/round-64/measured/attempt2/{c1,c2}.out`).
- Attempt-1 partial seat outputs (10 dirs from the 21 stopped seats) moved byte-exact to
  `.ufo/waves/round-64/f/out-attempt1/` before the re-dispatch (commit `9549c0b9`); the L1
  scratch clone, work dirs and the 60 G wave scratch were purged after landing
  (`/fast/scratch/hyaku/kama-r64` now empty).
- Wave f: 42 seats (mutation-tester 22, critic 5, reviewer 5, executor 4, scribe 3, connector 2,
  sentinel 1; 33/42 ≈ 79 % attack-share roles), all settled per the orchestrator's WAVE-DONE;
  evidence `f/f-results.json`, 26 report files, 5 evidence-only out dirs, 11 seats returned
  progress transcripts only (preserved byte-exact as `f/out-missing-*.txt`, extracted by the L1;
  named in the lesson attempt-2 section). All three executor items returned decisive receipts:
  X11 (C1 stability 1/5 sequential `met`, all failures `bind_holders` under load, fail-closed),
  X12 (C2 stability 6/6 `met=True`), X13 (counting commands re-derived at the tip), X14
  (red-before chain: base `met=False`; round-63 counter still accepts forge-A 44/44; forge-B
  does not apply to the v2 tool — patch-index mismatch, recorded as a blocker for that one
  replay; the MT15 receipts stand).
- **C1 falsifiers (receipts in `f/`):** `MT22` b3 — a pre-started **root** daemon holds a second
  `::1:<runport>` listener; the counter's own snapshot prints two listeners and still prints
  `met=True 91/91`; `MT22` (f) — the serving listener in a private user+net namespace is
  invisible (procfs net tables are per-namespace); `MT23` (d) — the tool sends seed 4242 on the
  wire while the receipt self-reports the drawn seed, and passes (temperature 0 masks it);
  `MT25` D_gap600 — a lazily-mapped model is never file-backed at snapshot time and evades
  `bind_ref_files` (`met=True 91/91`); `MT30` F3 — the acknowledged non-dumpable-helper limit
  re-realized (`pidfd_getfd` LISTEN duplicate); `RV08` — cleanup kills identity-matched but
  unowned holders, and `pid_gone` still conflates an unreadable `/proc/<pid>/stat` with gone;
  `SB06` — counter mutants `m_live_status`/`m_finish_gate` survive; `CR06` DEFECT 1 — the
  freeze's quoted amended sentence reads "89 targeted controls" where the instrument grades 91
  (AMENDMENT 1a's parenthetical is false of its own file), DEFECT 2 — "unreadable pid_gone
  fails closed" only partly delivered.
- **C2 falsifiers:** `MT41` F1 — a caller `PYTHONPATH` shadow rewrote a git REF and the counter
  certified the base tip (honest `met=False`) as `met=True 120/120`, a do-nothing false pass;
  `MT41` T1–T3 — bound/planted tip code wrote into the lane clone, the export and outside
  `--work` through committed symlinks while controls stayed credited; `CR07` mutants M1/M2/M3/
  M4/M8/M9 survived (SHONEN `[~]→[x]` with a fabricated verifier; falsified calibration-row
  counts; evidence pointers to nonexistent files; deleted round-63 limits paragraph; deleted
  unpinned bound tool; deleted SHONEN.md) while M5/M6/M11 were killed; `CR05` m9 — reconciler
  blind beyond its graded window; `MT38` — the shortcut-tally reader is topic-blind (a
  `no-disclosure` round flips to disclosed from other rounds' text, demonstrated on a
  neutralized clone); `MT33` — bound rows read unpinned tip files (`tools/kama-probe.sh`,
  `tests/ollama-evidence/cases.json`), exploit included; `MT39` — `controls_rejected` prints
  `120/120` while the counter's own baseline fails (`met` itself stayed honest); `MT37` —
  work-refusal guard mutants W2/W3 widen acceptance and B5 shows a same-commit self-closure
  pointer satisfies the numeric predicate. Killed on the way: `MT40`'s nine mandated mutants,
  `MT37` B1–B4/B7, `RV06` reconciler selftest 5/5.
- Frontier: SB04's revised entry admitted as `corpus/knowledge/process-bound-listener.md`
  (line anchors re-derived at `23b3fdb1`; my re-run of its recheck printed
  `quotes OK=31/31`, exit 0, receipt `measured/attempt2/recheck-quotes-rerun.out`); I appended
  a wave-f addendum naming each realized limit with seat pointers. SOURCES in-place flips
  applied (below). KQ116 and KQ117 appended to `corpus/QUALITY.md`; lesson attempt-2 section
  plus Mistakes 13–15 appended to `corpus/lessons/round-64.md`.
- KR06 (round-63 closure routed defect): still recorded, not repaired — upstream (S526)
  documents no `system_fingerprint` format; the 9–40-hex bound is receipt-derived observed
  shape (`b11755-704366d76`, 9 hex), graded only in the frozen r62/r63 honest-stop instruments;
  the round-64 claim does not rest on it.
- Misroot sweep (`git -C /home/vgpnk/Projects/shokunin status --porcelain`): one non-kama
  stray at the fleet root (`rerun-daemons.log`, another lane's) — not touched; `.scratch/` is
  orchestrator-owned; no kama file found at the fleet root this attempt.
- Tools installed/updated: none (L1 and, per reports, no seat); pacman not used. Assimilation:
  none (quarantine slice unchanged from round 63; nothing adopted from `merge/kama/`).
  considerthese: `2026-10-24.md` proposal 2 landed in attempt 1 as KQ113 +
  `tools/recheck-quotes.py`. L0: no new question filed; prior kama lines (176, 184–187, 194,
  195, 208) remain unanswered and were routed around, none blocking.

## Landed changes

All lane commits printed `landed <hash>` via `jj-lane.sh` and are pushed (LOG.md §Round 64
attempt 2 maps them):

- `9549c0b9679e5445cb9e6b0d6413c8fb357b9986` — attempt-1 partial wave-f outputs moved to
  `f/out-attempt1/`.
- `6203f6f5c3dde650fe004ab855249c29e1189aba` — pre-dispatch receipts (C1/C2 at wave tip, scans
  at `9549c0b9`, census attempt2-start).
- `e45a4f1b1720482dba7c27077cce4d7a65acc285` — integration: entry
  `corpus/knowledge/process-bound-listener.md` (+ wave-f addendum), SOURCES flips, lesson
  attempt-2 + Mistakes 13–15, QUALITY KQ116–KQ117, SCORECARD attempt-2 section, LOG entry,
  wave-f evidence (`f/` reports, out dirs, `f-results.json`, extracted transcripts),
  `measured/attempt2/`, census end.
- `831f0939c6cfabfdf72d84ed955fd344ff3b4372` — wave bookkeeping (`f.ready.partial` deletion
  record, `f.ready.dispatched`, SB04's fetched source bytes the entry cites,
  `source/proc_pid_exe.5.html`, `proc_pid_maps.5.html`, `proc_net_tcp.v7.2.rst`,
  `SB04KnowledgeRevise-fetch.sha256`).
- `7b00be78ca49ce634515881fe3ddb86262f23872` — MT32 concurrent-run monitors (two >1 MiB .gz,
  named files) — **final lane HEAD**.
- Gates re-run after the edits: `sources-census.sh validate --root … kama` exit 0
  (`census/attempt2-end.out`); `tools/sources-append-only.py --selftest` 45/45;
  `tools/round42-selfdesc-reconcile.py` `closure_ptr=1 mismatches=0 met=True`;
  `tools/append-only-audit.py` exit 0 (`regressed=0 vanished=0 unmatched=0`; its five
  `unbound` declaration notes are pre-existing record quirks, none introduced this round).
- Not landed: no capability row (C1 unverified, so `live-completion-request-plane` stays out);
  S535/S536 stay rejected; SCORECARD axis scores unchanged.

## Before → after measurements

- **C1 operability 8→8 (not verified):** before (do-nothing base `0c1eff3c`):
  `tool_present=1 live_ok=0/1 controls_targeted=0/0 of 91 eval_selftest=0/8 errors=1
  met=False` (`controls/c1-base-final-counter.txt`) → measured at wave tip `23b3fdb1`:
  `python3 tools/round64-c1-counter.py --repo <lane> --tip 23b3fdb1a925129a9961cf551f6d40bf251602cb
  --work <fresh>` → `tool_present=1 live_ok=1/1 controls_targeted=91/91 of 91 families_exact=1
  eval_selftest=8/8 errors=0 met=True`, exit 0 (`measured/attempt2/c1.out`; X14 reproduced the
  chain). Wave-f falsification: five survivor classes + defects + 4-of-8 load flakes above —
  the counter counts, the claim does not verify. Measured commit `7b00be78` carries the bytes.
- **C2 calibration 7→7 (not verified):** before: base `covered=0/12 … tally_disclosed=1/8
  controls_rejected=0/120 errors=2 met=False` (`controls/c2-base.txt`) → measured:
  `python3 tools/round64-c2-counter.py --repo <lane> --tip 23b3fdb1a925129a9961cf551f6d40bf251602cb
  --work <fresh>` → `covered=12/12 mismatches=0 pinned=13/13 deps_pinned=2/2
  regress_flipped=12/12 printers_rejected=12/12 idle_ok=1 work_reuse_refused=1 closure_ptr=1
  recon_mismatches=0 tally_disclosed=8/8 tally_selftest=1 sens_selftest=4/4
  controls_rejected=120/120 errors=0 met=True`, exit 0 (`measured/attempt2/c2.out`; X12 6/6
  stable). Wave-f falsification: caller-env false pass, sandbox escapes, six surviving
  self-description mutants, tally topic-blindness, unpinned row deps.
- Supporting at lane tip `7b00be78` (scans run at `9549c0b9`, bytes unchanged since):
  `digest-ledger scan` `unknown=0`, `hexrun-census scan` `unknown=0`, reconciler `met=True`,
  `shortcut-tally --rounds 56-63` non-`no-disclosure` for 8/8 (`measured/attempt2/`).

## Sources & frontier

- Census before → after: `.ufo/waves/round-64/census/{attempt2-start,attempt2-end}.out`,
  `sources-census.sh validate --root /home/vgpnk/Projects/shokunin kama` **exit 0 at start and
  at end**; counting command `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`
  → **276 before, 276 after** (no rows appended; the admitted entry cites only held rows;
  X13's at-tip count 272 reflects tip `23b3fdb1`, which predates attempt-1's S533–S536).
- Rows added by tier: none this attempt (attempt 1 added S529–S536, tier A: 6 queued, 2
  rejected). Rows touched old→new (in-place status/used-by only): S529–S534 `queued → mined`,
  `used-by` `— → corpus/knowledge/process-bound-listener.md, corpus/lessons/round-64.md`;
  S049 `used-by` `+corpus/knowledge/process-bound-listener.md`; S495, S496, S499 `used-by`
  `+corpus/knowledge/process-bound-listener.md`. All flips logged old→new in the lesson
  attempt-2 section.
- Frontier rows advanced: S529–S534 queued→mined on the admitted entry; frontier ground
  gained: process identity of a running server from procfs (previously only S049/S495/S496/S499
  fragments). Sourced claim: C1 (freeze + counter docstring cite S529–S534; located quotes in
  the lesson §Gate; the entry re-opened all cited man pages 2026-10-30 with retained sha256
  bytes).
- Assimilation: none. QUARANTINE: register slice unchanged; nothing adopted this round.

## Trend verdicts

- **Expansion — improved:** one admitted knowledge entry on ground the lane did not hold
  (`corpus/knowledge/process-bound-listener.md`, 234 lines, every quote and line anchor
  re-derived and re-verified this round), six SOURCES rows advanced queued→mined. Limit: no new
  registered row and no assigned-axis move claimed.
- **Quality — improved, narrowly:** the corpus gained a verified-anchored entry plus two
  admission bars learned from receipts (KQ116 caller-environment binding, KQ117 registry binds
  every file its rows read), and the wave mapped each instrument's failure set with committed
  evidence. The instruments themselves ended falsified, so no quality credit is taken for them.
- **Discernment — unchanged:** calibration stays 7; the lane's attempt-1 self-assessment
  ("measured met, not verified") was exactly what the wave then demonstrated, the reconciler
  found zero self-description mismatches (`closure_ptr=1 mismatches=0`), and admission stays
  with the independent non-author closure, which remains pending (driver completion is not
  admission).

## Stale-lane

Stale-lane: progressing; one lane mission, round 64 only; this attempt closes the round's
falsification step left open by the run-11 wrap-up. No other kama mission is open.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — unchanged this round (`git diff f6a4ea9a 7b00be78 -- SKILL.md` empty); no non-author verifier this attempt.
- [~] At least one end-to-end domain task executed and logged in LOG.md — LOG.md §Round 64 (attempt 2); live counter runs with receipts at `measured/attempt2/{c1,c2}.out` and 26 wave-f seat reports under `.ufo/waves/round-64/f/`; no non-author verifier (closure pending).
- [~] Instructions executable by an agent without oral context — the counting commands above were re-derived independently by X13 at the wave tip and re-run by the L1; no non-author verifier.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — PROVINCE.md unchanged this round (`git diff f6a4ea9a 7b00be78 -- PROVINCE.md` empty); wave-f CN03/CN04 read across waves without absorbing sibling ground; no non-author verifier.
