# kotoba round-17 report — calibration 8.0 → 8.5 (governance citations executable; `M36` corrected)

**Lane:** kotoba-shokunin (`depth + consistency`, prompt/skill craft).  
**Child repo:** `/home/vgpnk/Projects/shokunin/kotoba-shokunin` @ `fad752b` (`round-17`).  
**Move:** make repo-root governance-file citation claims machine-checkable, then correct the refuted `M36` literal-tilde-heredoc fixture.  
**Durable evidence:** `corpus/knowledge/checklist-execution-round17.md`, `LOG.md` round-17 entry, `SCORECARD.md` round-17 row.

## Axis decision

`freshness`, `calibration`, and `adjacency` began tied at 8.0. Calibration was the in-scope, evidence-bearing frontier move:

- repo-root `LOG.md` and `SCORECARD.md` carried citation claims but no live gate;
- round 16 established that the recorded `M36` fixture did not model bash’s delimiter;
- adjacency findings belong to sibling lanes, while all six local instruments were already green at the round boundary.

`consistency` remains reconciled as a calibration sub-axis in this lane’s scorecard. The score moves **8.0 → 8.5**; freshness and adjacency do not receive a second scored move.

## Claim under test

> When the target is this repo’s own `SKILL.md`, the checklist verifier examines repo-root `LOG.md` and `SCORECARD.md`. Every non-schematic, non-meta repo-rooted backticked path resolves at HEAD. The rule fails on a planted unquoted dead path and cannot be vetoed by broad prose markers. Separately, `<<~EOF` opens a heredoc whose delimiter is the literal word `~EOF`; the body stays opaque and command scanning resumes only after `~EOF`.

## Red-before evidence

| Surface | Command/probe | Observed red state |
|---|---|---|
| `LOG.md` governance paths | direct pre-rule extraction with the reused `citation_resolve` predicate | 74 subjects, 6 dead-at-HEAD |
| `SCORECARD.md` governance paths | same | 51 subjects, 2 dead-at-HEAD |
| independent count | `R17Review` reimplementation, without importing the verifier | reproduced 74/6 and 51/2 |
| `<<~EOF` clean fixture | pre-patch command gate | FAIL: body token `nonexistent-binary-xyz` treated as a command |
| `<<~EOF` dead-tail fixture | pre-patch command gate | FAIL named phantom body token plus the real dead tail |
| bare-`EOF` mis-termination | pre-patch command gate | FAIL: lines after bare `EOF` still interpreted as commands |
| explicit `--repo .` | bounded parent-hop probe | relative `Path('.')` used the wrong base and changed verdicts |

The eight governance failures classified as: one ellipsis schematic, two literal-`N` templates, three historical repair records, one deliberate dead example, and one sibling pointer lacking an explicit base.

## Landed implementation

1. Added `governance.citation_resolves`, the tenth check in `verifiers/verify_skill_checklist.py`.
   - Runs only for the repository’s own `SKILL.md`.
   - Reads the explicit pair `LOG.md` and `SCORECARD.md`.
   - Reuses the bounded repo-root existence predicate instead of creating a second resolver.
   - Same-line double-quoted spans are counted as historical/meta findings.
   - Ellipsis and literal `round-N` path segments are counted as schematics.
   - Every other extracted subject must resolve; zero checked subjects is a FAIL.
2. Rejected file-level quote parity after it suppressed 17 ordinary live citations. A cross-line quote now remains checked and fails in self-test.
3. Repaired four dead-by-assertion records with the existing quoted-meta idiom; named the sibling base explicitly as:
   - `../kasegi-shokunin/corpus/instruments/resolve.py`
   - `../kasegi-shokunin/corpus/instruments/anchorcheck.py`
4. Corrected `HEREDOC_RE` from `WORD` to optional-literal-tilde `~?WORD`; terminator comparison remains exact.
5. Added three committed fixture pairs:
   - `command-heredoc-tilde`: PASS, 3 subjects / 2 segments;
   - `command-heredoc-tilde-dead`: FAIL, 3 / 2, naming only the real tail;
   - `command-heredoc-tilde-misterm`: PASS, 1 / 1, proving bare `EOF` is not the terminator.
6. Normalized explicit `--repo` values with `.resolve()`; a hermetic child/parent self-test pins the bounded-hop behavior.
7. Updated `SKILL.md`’s verifier summary and scope without exceeding 599/600 lines.

## Final measured state

| Measurement | Result |
|---|---|
| governance population | 134 raw = **125 checked/resolving + 6 quoted meta + 3 schematic**, 0 checked dead |
| checklist checks | **10 × PASS** |
| checklist boxes | 41 mapped = 8 executed / 0 delegated / 33 unexecuted |
| checklist verifier self-test | **0 failures over 1504 assertions** |
| fixture directories | 68 → **71** |
| SKILL lines | **599 / 600** |
| command subjects | 19 subjects / 15 segments |
| SKILL citation subjects | 42 resolving |
| checklist verifier sha256 | `02ccf1b310f7910502f7938d24eb1cfcabe2c521ec42b7ce6420f1869af8df27` |

## Eleven L2 lanes — one batched dispatch

| Lane | Finding | Disposition |
|---|---|---|
| `R17Plan` (planner) | ranked round-18 candidates; sibling citation remeasurement is rank 1, with a no-score condition if the delta is schematic noise | adopted for `planned` |
| `R17Gov` (scout) | classified all 125 pre-state governance subjects and warned that broad prose exclusions can make the gate vacuous | landed narrow syntax-only exclusions |
| `R17Probe` (labrat) | bash treats `~` as part of the `<<~EOF` delimiter word; quoted and tab-stripping boundaries measured | landed minimal regex direction |
| `R17Critic` | rejected corpus-verifier placement because its corpus-only boundary is deliberate; narrowed the claim to HEAD navigability | landed scope/claim limits |
| `R17Sentinel` | supplied quoted delimiter, whitespace, path-hop, symlink, and zero-subject adversaries | landed relevant fixtures; ceilings recorded |
| `R17Revenger` | reconstructed why corpus integrity excludes root governance files | preserved boundary; checklist verifier selected |
| `R17Fixtures` (executor) | drafted three fixture pairs; refuted the requested bare-`EOF` FAIL because bash keeps it inside the heredoc | fixtures landed with corrected verdict |
| `R17Connector` | found no sibling overlap; resolved kasegi prior-art base and routed sibling-owned findings | base repair landed; sibling edits refused |
| `R17Review` | independently reproduced 74/6 and 51/2 and verified citation existence | accepted as author-side corroboration |
| `R17Mutate` | designed M42–M50 candidate mutations | recorded as design only; **not claimed executed** |
| `R17YAGNI` | existing corpus grammar was clean but vacuous for governance; selected predicate reuse over a third instrument | landed simpler design |

## Falsifications retained

- File-level quote tracking was not “more robust”: it hid 17 live claims.
- Broad historical/dead-example prose markers were rejected because they could exclude every current failure and make the check unfailable.
- The requested bare-`EOF` fixture verdict was wrong; bash requires `~EOF` for `<<~EOF`.
- Corpus-integrity placement was rejected; its `corpus/*.md` boundary was an intentional round-11 contract.
- `R17Mutate` supplied a design, not an executed mutation run; no catch-rate is claimed.

## Integration drift caught by the corpus gate

After staging the new knowledge file:

```text
tracked_files=47
report_total=32
report_dead=32
```

All 32 checked report-pointer occurrences used the absent lowercase host base `/home/vgpnk/projects`; the observed report tree is `/home/vgpnk/Projects`. The 32 occurrences across 16 in-repo corpus files were case-corrected without changing their round/lane targets. The fault harness’s `plant_f` anchor carried the same stale base and was corrected too.

The baseline changed only `tracked_files` 46 → 47. Final corpus state:

```text
tracked=47 unindexed=0 stale=0 missing=0
report_dead=0/32
commit_total=27 unresolvable=0 nonhash=0
9/9 checks pass
```

This is unscored integration/freshness repair, not a second axis move.

## Six-instrument landed-tree verification

| Instrument | Observed result |
|---|---|
| `python3 verifiers/verify_harness_claims.py` + `--self-test` | 27/27 checks pass; 0/10 failures |
| `python3 verifiers/verify_surfaces.py` + `--self-test` | 7 live PASS rows; 0/75 failures (negative environment fixtures emit their expected `ERROR` diagnostics) |
| `python3 verifiers/verify_skill_checklist.py` + `--self-test` | 10 live PASS rows; governance 125/6/3; 0/1504 failures |
| `python3 verifiers/verify_corpus_integrity.py` + `--self-test` | 9/9 checks pass; 0/88 failures |
| `python3 verifiers/verify_corpus_independent.py` + `--self-test` | live exit 0; 52 assertions, 0 failures |
| `bash verifiers/fault_injection_corpus.sh --self-test` | four assertion-machine PASS results; `OK` |
| `bash verifiers/fault_injection_corpus.sh` | control + mutations a–h: **ALL PASS**, including the documented `fault-f` blind spot |

The clone-based fault harness was rerun after commit `fad752b`; its committed-state control is clean.

## Band decision

**Calibration 8.0 → 8.5.** The formerly prose-only governance claims are checked by a non-vacuous executable rule with independent pre-state reproduction, fail/pass fixtures, and a stable final population. The parser claim is corrected against measured bash behavior rather than preserved around a faulty fixture.

**9 is withheld.** Existence does not prove content, anchors, revision pins, historical truth, symlink containment, or referent type. Quoted and schematic exclusions are deliberately narrow but remain conventions. Every L2 lane is author-side under the protocol, so `SHONEN.md` remains `[~]`; no promotion mark is claimed.

## Cross-domain — routed, not absorbed

- Round-18 rank 1 is a fresh sibling `SKILL.md` citation census: pre-probe population 225, unresolved 14, distributed 2/1/5/1/5. Those files remain sibling-owned; no edits were made outside kotoba-shokunin and this report.
- The `AXES.md` ↔ `MISSION.md` naming mismatch remains protocol-owned.
- Kasegi citation instruments are prior art only; they were not edited.

## Effective `m_swe` → Daybreak fallback inspection

The exact operator-stated chain is **not visible** in the effective configuration read this round:

```text
modelRoles.m_swe = "devin/swe-2:max"
retry.fallbackChains.m_swe = null
modelRoles.m_daybreak = "openai-codex/gpt-daybreak-blue-latest:max"
```

Daybreak is assigned to the separate `m_daybreak` slow/plan role; it is not configured as `m_swe`’s final/only retry fallback. No genuine `m_swe` capacity failure occurred during this round, so no advancement event exists to record. No failure was forced and no frozen mission/config contract was altered.

## Round 18 frontier

1. Re-measure and route five sibling `SKILL.md` citation populations; award no score if the four-occurrence change from round 16 is only schematic noise.
2. R1 read-verb precision and blast-radius replay.
3. `M23` executable heredocs.
4. D6 prompt literals over the fleet prompt set.
5. `agentdef.*`, `M22`, and `M38` only with named non-vacuity conventions.

Ceilings carried: quoted/trailing tilde delimiters, terminator whitespace, closed citation roots, content/anchor/pin semantics, symlinks, and the zero-live `delegated:` class.
