# WaveDistiller — round-15 deduplicated findings

Scope: every scratch file present at synthesis time. Findings survive only when the lane supplies an executed command and observed result. Drafts, plans, placeholders, assertions marked `[INFERENCE]`, and the corrupted tail of ItemReviewer are not evidence.

## Deduplicated findings (strongest evidence pointers)

1. **The checklist has 16 items (8 + 8); no revision held 15.** Evidence: `ItemsScout.md:12-31`, `awk '/^## Credential-hygiene checklist/,/^## Evidence-receipt patterns/' SKILL.md | grep -c '^- [ ]'` => 16; historical `git show ... | awk ... | grep -c ...` => 10,12,13,14,16. Corroborated by `LogScribe.md:20-31` and `EntryDraftExecutor.md:1-9`, each with commands. **Triage: blocker** where shipped prose still says “15-item”; otherwise record.

2. **The pre-move 12/manual split was prose, not a recomputed verdict, and no pre-move checklist gate existed.** Evidence: `ItemsScout.md:49-74`, commands `grep -n ... SCORECARD.md` and `ls corpus/checklist*` (no such file), plus `grep -rln 'Credential-hygiene\|hygiene checklist' corpus/*.sh` => no match in `ReportDraftExecutor.md:64-73`. **Triage: record** (the landed gate supersedes the pre-state).

3. **The landed gate is live and green at 9 runnable / 7 by-hand.** Evidence: `LogScribe.md:35-67`, commands `bash corpus/checklist-run.sh`, `--selftest`, `--list`, `--only E1/E2` => `CHECKLIST_RATIO: runnable=9/16 floor=8 by_hand=7`, `CHECKLIST_RUN: CLEAN ... failed=0`, `CHECKLIST_SELFTEST: PASS (28 cases)`, `CHECKLIST_LIST: rows=16 runnable=9 by_hand=7`. Corroborated by `HostScout.md:300-320` and `EntryDraftExecutor.md:1-16`. **Triage: record (shipped evidence).**

4. **The landed TSV shape is 8 columns with lead-based item↔row bijection, not the brief’s 6-column shape.** Evidence: `ItemsScout.md:230-250`, `grep`/source inspection of `checklist-run.sh`; `EntryDraftExecutor.md:44-81`. **Triage: record and ensure docs describe landed shape; blocker only if shipped docs still claim 6 columns.**

5. **The gate’s first execution exposed and then fixed real defects:** silent `uniq -d`/pipefail death, empty-last-line extraction death, H4 front-matter trailing-newline false defect, E4’s three documented placeholder literals, missing `the-janitor run`/ledger deny rules, and one-way bijection detection. Evidence: `LogScribe.md:74-113`, `EntryDraftExecutor.md:300-344`, commands include `bash corpus/checklist-run.sh` => zero output / E4+H4 failures, then green 28-case selftest. **Triage: record as fixed landing defects; blocker only if the final run is not green.**

6. **E4’s ref scan has a material allowlist blind spot.** Evidence: `ItemsScout.md:357-373` and `LogScribe.md:62-73`, command comparing `grep ... op://... | grep -vE 'op://(FakeVault|wal|vault)/' | wc -l` => 0 versus raw => 5. A real reference under vault name `vault`, `wal`, or `FakeVault` is invisible. **Triage: blocker for shipped risk disclosure; fix is optional only if L1 explicitly accepts the stated ceiling.**

7. **H8’s shipped control-plane check does not reject non-loopback listeners.** Evidence: `HostScout.md:300-360`, scratch socket command with wildcard bind => `CONTROL_PLANE: password_refs=0 listeners=1 established=0` and the shipped ERE passes it; proposed `non_loopback=0` arm is not yet landed. **Triage: blocker: change the row before commit or explicitly remove the item’s containment claim.**

8. **The flock attribution is wrong in two committed notes.** Evidence: `HostScout.md:245-279`, commands `grep -nic lock ~/.config/the-janitor/client.py` => 0 and `grep -n 'LOCK_FILE\|flock' ~/.local/bin/the-janitor` => wrapper flock sites; `PROVINCE.md:12` and `corpus/surface-census.tsv:22` still say client.py owns lock. **Triage: blocker: correct both notes or state deferral; do not leave a false correction in LOG.**

9. **The planner’s strict duty-vs-premise reading yields 3 runnable / 13 by-hand, conflicting with the shipped criterion’s 9/7.** Evidence: `CheckPlanner.md:1-63` ends `runnable=3 by_hand=13`; `LogScribe.md:35-67` executes and records 9/7; `ItemsScout.md:275-335` reports three readings (3, 4–5, 9). **Triage: record contradiction; do not choose a side.**

10. **The H7 row accepts exit 0|1 but a missing DB returns exit 2, although purge/absent DB is described as legitimate.** Evidence: `ItemsScout.md:275-310`, command `bash corpus/transcript-scan.sh --db /nonexistent/none.db` => exit 2. **Triage: blocker or explicit scope decision before commit; current row can false-fail a prescribed purge state.**

11. **The H1/E1/other runnable rows check premises, not the operator duties they name.** Evidence: `ItemReviewer.md:10-27` executes all nine row commands and records their outputs; `ItemsScout.md:342-355` and `EntryDraftExecutor.md:190-250` document the same boundary. **Triage: record as the gate’s stated limitation, not a defect unless report claims verification.**

12. **HostScout executed safe row probes and verified `ss -l` is required to see LISTEN sockets.** Evidence: `HostScout.md:1-35`, commands `ss -Htn` (empty) vs `ss -Htnl`/`ss -Htna` (LISTEN), plus mutation proofs for overlay, permissions, and handoff checks. **Triage: record.**

13. **LiveLabrat independently verified the safe listener probe without starting the handler.** Evidence: `LiveLabrat.md:1-35`, `/tmp` listener plus `ss -ltnH` => one listener on scratch port and zero on 40961, then SIGTERM cleanup. **Triage: record.**

14. **Sibling sweep found no duplicate per-item command→verdict runner.** Evidence: `SiblingConnector.md:1-45`, source inspection of kotoba/kumitate/kasegi/kengaku/kake; no sibling command was run. **Triage: record-only adjacency.**

15. **ItemReviewer contains a corrupted/non-repo tail, not usable evidence.** Evidence: `ItemReviewer.md:27-60` abruptly introduces unrelated identifiers (`node-drop`, `t_purt_iterator.inc`, etc.) after a coherent gate audit. No repo command/result grounds that text. **Triage: noise; exclude the injected tail from findings.**

16. **TsvMutator and ClassCritic supplied plans only, not mutation verdicts.** Evidence: `TsvMutator.md:1-28` ends with “further sections are appended”; `ClassCritic.md:1-11` lists attack axes and says “cause being isolated” only. **Triage: noise; no executed finding survives from either file.**

## Triage summary

### Blockers before commit
- Remove/update every live “15-item” assertion using the executed 16-item census.
- Correct `PROVINCE.md:12` and `corpus/surface-census.tsv:22` lock ownership, or explicitly defer it; never report it as fixed when it is not.
- Fix H8’s non-loopback false-clean (or remove the stronger containment claim).
- Resolve H7’s missing-DB exit-2 behavior against the checklist’s prescribed purge state.
- Make the report/LOG disclose E4’s vault-name allowlist ceiling and the 3/13 dissent; no unresolved placeholders or unexecuted adversarial results may ship.

### Recorded-only
- Green 9/7 gate evidence and 28 selftests; 8-column lead bijection and defect vocabulary.
- Fixed first-contact defects; host probe portability and safe socket observations.
- Baseline counts (ledger 18, stamps 44, rounds 12, knowledge 17) from `LogScribe.md:53-57`.
- Sibling adjacency/no-duplicate result and premise-vs-duty limitation.

### Noise / dropped
- TsvMutator plan-only payload cage; ClassCritic plan-only attack axes.
- ItemReviewer’s unrelated corrupted tail and its unsupported “counterexample”.
- Unresolved placeholders and lane roster prose without an executed command/result.

## Contradictions between lanes (both sides quoted)

1. **Split criterion:** `CheckPlanner.md:63` says `runnable=3 by_hand=13`; `LogScribe.md:35-67` says executed gate output `runnable=9/16 ... by_hand=7`. This is a genuine criterion disagreement, not a measurement typo.
2. **Pre-move command census:** `LogScribe.md:20-31` says four items name runnable gate commands (items 1,2,5,15); `ReportDraftExecutor.md:64-73` says five items name executable commands (items 1,5,6,9,15). Predicates/rosters differ and neither should be silently merged.
3. **Row contract:** the original brief described six columns and `skipped=0`; `ItemsScout.md:230-250` and `EntryDraftExecutor.md:44-81` show the landed eight-column `lead`/`reason` shape and no `skipped` field. This is a design divergence; shipped documentation must use the landed form.
4. **Lock owner:** `LogScribe.md:42-48`/`145-149` reports client.py has zero lock references and wrapper owns flock; stale committed notes quoted in `HostScout.md:245-260` attribute lock to client.py. This contradiction requires the blocker fix.

## Completeness
All scratch files present at synthesis time are classified: executed findings are listed, duplicate claims collapsed, unsupported/planning text dropped as noise, and contradictions preserved without choosing a side.
