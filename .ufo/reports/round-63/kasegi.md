# Kasegi round 63 — honest stop on the frozen export counter

## Work performed

**Declared C1: depth:verifiability (lowest), nominal score4 held — finite upstream-error discrimination. Verdict: NOT VERIFIED under its own frozen committed-input kill rule; honest stop.** Three named error repairs work, but the frozen export driver omits four historical receipt inputs. No coverage/capability/score increase is claimed.

- Frozen predicate, counter, target, kill rules and candidate digests before production implementation: lane `.ufo/waves/round-63/claims.json`, freeze `d690b92a4834d3a51ba86498d9eb6243f00203db`; base `fdccc6da803965234c1eff5a0fee38b97e6621c1`.
- Implemented bounded propagation: after final-stage error precedence, the first upstream positive status>1 becomes stale with `derive-upstream-exit-N` and stops subsequent && groups. Upstream1 and negative statuses remain ignored. `corpus/instruments/figure-audit.py:98-109`, implementation `ff28e544adc228841a8706c5e72f4de3366391cd`, exact frozen SHA256 `15bcb6c4fbaaa23c2b85e480dff9b9af52e43442de64661f222d8868dd73b997`.
- Prefreeze controls discriminate unchanged base: final collector in candidate mode gives8 probes/3 failures/exit1; candidate8/0. Separate tree probes cover middle-stage and earlier && errors; new threshold/refusal limbs carry3/4 valid exact-once mutants, seven killed, two equivalent controls held, one deliberately invalid control rejected. Evidence: `.ufo/waves/round-63/controls/*prefreeze-r63.txt`, `w1/MutationCollector.md`, `w1/ExecMutants.md`.
- Reopened Project Zero's original disclosed SQLite account (S094) and prepared a documentation-only qualification-review handoff; four located checks pass. No exploit reproduction, new finding, six-file bounty package, reward or submission claim: `.ufo/waves/round-63/domain-review-handoff.md`, `controls/domain-review-ledger-r63.json`.
- Curated S096 own-work/A for local diagnostic evidence only; mined seven mistakes, including the initial cat-exit1 premise and omitted-input counter defect. `corpus/lessons/round-63.md` Gate/Mistakes; `corpus/SOURCES.md:106`. Existing R34/R50/R65/R79/R82 cover these classes; QUALITY intentionally unchanged.

Round shape: ONE validated v1 wave,9 seats: executor3, scribe1, scout1, connector1, reviewer1, critic1, mutation-tester1; attack3/9, connector1, canonical planner held by KasegiR63. WAVE-DONE received before this report; `.ufo/waves/round-63/w1-results.json` records nine nonempty evidence-producing outputs and no dead seat. No replacement/residual call. Configured routes were read, not changed; actual answering models are not inferred from configuration. Scoped sibling screen: `w1/ScopeConnect.md` distinguishes local claim-gate maintenance from tameshi verification methods, chousa research methods, kumitate orchestration and kengaku model evaluation.

## Landed changes

All entries tie to lane `LOG.md:2644-2654` and `corpus/lessons/round-63.md`.

| Pushed lane commit | Landed work |
|---|---|
| `d690b92a4834d3a51ba86498d9eb6243f00203db` | Frozen claim and predata wave/control artifacts, cited by LOG round63 freeze/motivation bullets. |
| `ff28e544adc228841a8706c5e72f4de3366391cd` | Exact candidate integration, selftest35→43, current SKILL registry, S096, lesson and motivating LOG entry. |
| `204a627b32671b6e5e1ee682acbe31714c6d46eb` | Honest frozen-counter failure, SCORECARD grade and separate NONCLAIM four-input collector correction. |
| `c1507ef51e90fe46a9503d1ef191dadbc2aaa2a9` | Settled results, supplemental proof, source census, cleanup and final records. |

Final lane remote proof: `git -C /home/vgpnk/Projects/shokunin/kasegi-shokunin ls-remote origin refs/heads/master` printed `c1507ef51e90fe46a9503d1ef191dadbc2aaa2a9 refs/heads/master`. This is the final lane hash. PROVINCE, knowledge entries, expected inventory and SHONEN deliberately unchanged. Four inherited r57–r60 dispatched markers remain driver debris, excluded from round work; no other inherited lane-authored changes were observed at start.

## Before → after measurements

C1 primary counting command, from the lane root:

```sh
python3 .ufo/waves/round-63/w1/ExecCollector/c1-probes-r63.py --instrument "$PWD/corpus/instruments/figure-audit.py" --work /fast/scratch/hyaku/kasegi-r63/L1/collector-final --mode candidate
```

Exact base instrument under that candidate-mode counter: `HARNESS probes=8 failures=3 mode=candidate`, exit1. Delivered implementation:8/0, exit0. Grep2/Git128/Python7 now stale with exact reasons; cat-missing1 remains green, not a fourth repaired class. Before/after transcripts are `controls/collector-donothing-prefreeze-r63.txt` and `controls/final-verification-r63.txt`.

Full frozen committed-input command:

```sh
python3 .ufo/waves/round-63/controls/verify-r63.py --revision ff28e544adc228841a8706c5e72f4de3366391cd --work /fast/scratch/hyaku/kasegi-r63/L1/committed
```

Observed `VERIFY measurements=7 failures=1`, exit1: collector8/0, trees8/0, selftest43/0, old battery5/5, new battery7/7 (invalid1 is its deliberately invalid CONTROL, not a killed mutant), trial4/4 pass; historical ledger26/35/stale9 fails. The driver omitted `.ufo/waves/round-55/controls/gate-final-r55.txt`, round56 `df3-fixedpoint-r55tip.txt`, round53 `c2-counter-final-r53.txt`, round56 `gate-final-r56.txt`. The new guard correctly exposes their missing upstream inputs. **C1 NOT VERIFIED: its own ledger/committed-run kill rule fires.** A green live-root prefreeze run does not override this. Frozen bytes/predicate/target remain unchanged.

Separate NONCLAIM correction: `python3 .ufo/waves/round-63/controls/verify-r63-supplemental.py --revision 204a627b32671b6e5e1ee682acbe31714c6d46eb --work /fast/scratch/hyaku/kasegi-r63/L1/supplemental` →7 measurements/0 failures, ledger35/35, trial4/4, exit0 (`controls/supplemental-verification-r63.txt`). This proves the missing-input collector correction, not retroactive frozen admission. Replays use explicit historical Git objects and selected committed inputs; they are host-bound, not hermetic exports or sandboxes. Revision input hashes are printed; general standalone gate/digest-hardening conformance is not asserted.

Scores: verifiability4→4 delta0 (nominal; citation-resolution metric untouched), coverage8→8, density9 held/not remeasured. No retirement, split, saturation waiver or repertoire row.

## Sources & frontier

Registry95→96; tiers A85→86/B5→5/C5→5; mined77→78/rejected18→18. Added S096 is scoped own-work/A, following S077 precedent, used-by lesson round63; no old status/recheck/used-by cell changed and all95 old full rows compare unchanged. Evidence: `controls/sources-before-r63.json`, `controls/sources-summary-r63.json`. Reproduce row counts on base/final committed bytes with:

```sh
for rev in fdccc6da803965234c1eff5a0fee38b97e6621c1 c1507ef51e90fe46a9503d1ef191dadbc2aaa2a9; do git show "$rev:corpus/SOURCES.md" | python3 -c 'import re,sys; print(len(re.findall(r"(?m)^ {0,3}\|\s*S[0-9]{3,}\s*\|",sys.stdin.read())))'; done
```

Expected observed counts95,96. Frontier43→43, knowledge81→81; no expansion credit. S096 source opened2026-11-04: code L106-L109 and actual collector transcript, located quotes `if p.returncode > 1:` and `HARNESS probes=8 failures=0 mode=candidate` (each≤25 words). S094 original URL https://projectzero.google/2024/10/from-naptime-to-big-sleep.html reopened2026-11-04; Introduction/S094.txt:18 quote “before it appeared in an official release, so SQLite users were not impacted.” Gate rejects universal superiority/released-user exposure; this is not external authority for the local runner.

Census command both times: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kasegi`.

Start output (`controls/census-start-r63.txt`), exit0:
```text
kasegi W04 S028 duplicate url docs.hackerone.com/en/articles/8494502-safe-harbor-overview-faq across scopes
kasegi W04 S029 duplicate url eur-lex.europa.eu/eli/reg/2024/2847/oj/eng across scopes
kasegi W04 S072 duplicate url bughunters.google.com/about/rules/about-this-section across scopes
kasegi W04 S076 duplicate url docs.github.com/en/code-security/concepts/vulnerability-reporting-and-management/repository-security-advisories across scopes
kasegi W04 S080 duplicate url ossf.github.io/osv-schema across scopes
kasegi W04 S085 duplicate url csrc.nist.gov/schema/nvd/api/2.0/cve_api_json_2.0.schema across scopes
kasegi ok /home/vgpnk/Projects/shokunin/kasegi-shokunin/corpus/SOURCES.md
```
End output (`controls/census-end-r63.txt`), exit0; whitespace normalized here, raw tabs retained in artifacts:
```text
kasegi W04 S028 duplicate url docs.hackerone.com/en/articles/8494502-safe-harbor-overview-faq across scopes
kasegi W04 S029 duplicate url eur-lex.europa.eu/eli/reg/2024/2847/oj/eng across scopes
kasegi W04 S072 duplicate url bughunters.google.com/about/rules/about-this-section across scopes
kasegi W04 S076 duplicate url docs.github.com/en/code-security/concepts/vulnerability-reporting-and-management/repository-security-advisories across scopes
kasegi W04 S080 duplicate url ossf.github.io/osv-schema across scopes
kasegi W04 S085 duplicate url csrc.nist.gov/schema/nvd/api/2.0/cve_api_json_2.0.schema across scopes
kasegi ok /home/vgpnk/Projects/shokunin/kasegi-shokunin/corpus/SOURCES.md
```

Assimilation: none. Exactly considerthese/2026-10-26.md proposal2 mined as bounded disclosed-account review; six-file task remains open, no source-repo/package adoption. No new external registry row or fake expansion. Mistakes M63-1..M63-7 and red-before evidence are in the lesson; outside admit/reject judgment remains with subsequent non-author closure, not dispatched seats.

## Trend verdicts

- **expansion: unchanged** — no new knowledge/frontier/repertoire, despite one legitimate local source row.
- **quality: unchanged** — finite runner repair works, but full frozen claim fails; no stale/false admitted knowledge left unmarked and no stronger source supersession claimed.
- **discernment: unchanged** — failure and reviewer correction are retained; no new outside decision or new criterion is self-certified.

## SHONEN

- [~] Real decision tables/error patterns/checklists/citations: SKILL.md and current gate registry; author assertion, no promotion verifier added.
- [ ] End-to-end bounty task: still open; domain-review-handoff.md is documentation-only, not the proposed six-file task or independent reproduction.
- [~] Executable instructions: finite collector/replay commands above; frozen export defect explicitly disclosed, no universal executability claim.
- [~] Province accuracy/no bleed: PROVINCE.md and w1/ScopeConnect.md; scope/live-target refusal unchanged.

Stale-lane: respawn-per-round; no other mission of this kasegi lane is open. Tool installs/updates: none. Scratch `/fast/scratch/hyaku/kasegi-r63` removed after seats settled (`controls/cleanup-r63.json`). Mandated fleet misroot sweep found no attributable kasegi round63 output (`controls/misroot-sweep-r63.txt`); operator scratch, sibling report and inherited unknown `after` untouched. Open L0 questions remain the pre-existing province re-pointing/R67/R69 and sandbox/decoded-option boundaries; no new question or authorization inferred. Honest stop: do not advance on a green subset of C1.
