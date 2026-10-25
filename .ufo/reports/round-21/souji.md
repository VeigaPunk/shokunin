# souji — round 21

## Work performed

Declared claims (frozen before implementation): **C1 calibration** (lowest axis7), catch implicit fleet-root read attempts; **C2 operability**, make the18-step acceptance replayable from a non-author scratch clone; **C3 coverage**, repair F5 reason output with synthetic-only canaries. Author-measured verdict: **improved** on each bounded claim; outside admission remains pending. Numeric score deltas are0 (legacy-unmapped7/8/8), not invented score gains.

- **Priority privacy repair:** `tools/souji-proc-census.sh` shares eight secret patterns across cmd/reason, retains selected secret-bearing argv provenance and bounds the complete reason to160 bytes. `--reason-only argv|fd` uses the production parser/formatter and exits before process enumeration. Same27-case oracle: old6/27→27/27, fabricated leaks19→0, max454→160 bytes. S100/S101; `census/round-21/final-code-verification.json`, `reason-oracle-before.txt`, `cmd-compatibility.json` (8 byte-equal cmd probes).
- **Priority replay repair:** current entry is `census/round-21/run-acceptance.py`; no lane-path or source-HEAD equality guard. It clones at full durable rev, keeps byte binding/exclusive outside-source output, derives r16/r18 fixture roots from their own files and verifies the immutable historical agreement against original artifact bytes. Three source shapes0/3→3/3, each18/18 original r20 predicates. Nullable HEAD and original remote-ref roots are supported; keep-only sources remain refused. `accepted-matrix.json`, `remote-source-after.json`, `final-code-verification.json`.
- **Calibration/process response:** new minor V-READ-ROOT supplements, never replaces, old classes. Full original192-file corpus3539 calls,2372 read-call oracle keys: tp3/fp0/fn0/missing0/extra0, all401 older per-call tuples identical. Three raw-export flags are2 distinct attempts. Oracle1942 direct independent keys +430 identical-call transfers;7 late labels excluded; one Bash-as-grep row corrected by a fresh residual critic. `oracle-acceptance.json`, `read-root-oracle-provenance.json`, `.ufo/waves/round-21/full-corpus-restoration.txt`.
- **Falsification:** four private-clone mutation probes report killed mutants: new read class(14 failures), reason mask/bound(23), argv provenance(3), source-output guard(2), with exact restoration hashes. `.ufo/waves/round-21/w2/Mutate*.md`. Own final checks:32/32,4/4,27/27,8/8,3/3 plus the replay cases above; no live proc fixture.
- **Frontier/mistakes:** S100–S103 opened by L1 (source seats died), three mined/one retained rejection; Q47–Q50 and `corpus/lessons/round-21.md` mine the routed r20 failures. No frontier promotion or new knowledge pathname. `census/round-21/domain-counts-final.json`.
- **Final gate:** corrected invocation at `e33d2959d06d246ba1f3018df43030dd195d6347` returns0, findings0,48 registry scripts,13 changed scripts,13 pins,3 measured records,8 carried paragraphs,62 reports. `census/round-21/landing-closed.json`. Initial red8 receipt retained: explicit fleet-root classification was missing and five prior-round exceptions were stale; removed only those obsolete exceptions, not genuine findings.

### Scope, remaining limits and authority

No live process census, credential/private-value probe, r18 proc selftest, signalling or inherited reap was performed by the measurements. Historical agreement handling hashes/stages committed original bytes; it is not a new process observation or exposure assessment.

**Not process-scope-clean:** L1's early ancestor-directory-name discovery is disclosed/void as evidence; RevengeReasonOmission's forbidden historical-snapshot search returned committed snapshot/TSV rows (excluded from all evidence; raw output not exported). AttackCorpus18 wrote7 labels after seeing the predicate; those votes were excluded. All kept reports are under the lane; mandatory fleet `git status --porcelain` misroot sweep found no own-seat suspect (`fleet-misroot-sweep.json`). No operator-sweep contents were opened/staged, no unrelated files deleted. Only23 exclusively created r21 scratch paths were removed; canonical evidence remains (`fixture-cleanup.json`).

The r20 report's **“operator explicitly upheld”** is withdrawn: recorded evidence only says **“Parent Main confirmed operator/Kagi ownership.”** This assignment authorizes the present synthetic repair, not historical exposure inspection, reaping or snapshot purge. Certification OFF, K5 HELD; inherited reap and NAMESPACE pin remain held, historical exposure remains operator/Kagi-owned. No new L0 question.

Inherited r20 result-predicate limits remain OPEN and explicit: Python bool/int equality, summary stderr acceptance, count-not-name cache checks. The residual reviewer confirms these predate C2 and do not falsify its narrow clone-replay claim. Actual final step stderr is empty and all33 cache-check names match the original receipt. This is selected-summary parity, not malicious-producer attestation, full-source integrity or bit-identical reproducible builds. Source samples cover HEAD/bare/tracked status (matrix also refs), not ignored/untracked contents or cleanliness. Rendered delimiters and clipped targets remain bounded/unknown; no global audit certification.

### Swarm accounting

| dispatch | seats and role mix | completed / provider-dead | evidence |
|---|---|---|---|
| validated W1 |73: executor12, scout26, scribe12, reviewer9, critic6, revenger3, sentinel2, simplifier2, connector1 |31 /42 | `.ufo/waves/round-21/w1-spec.json`, w1-dispatch.json, w1/swarm-registry.json, w1-outcomes.json |
| validated W2 |75: scout23, revenger19, reviewer18, executor6, critic4, mutation-tester4, connector1 |30 /45 | w2-spec.json, w2-dispatch.json, w2/swarm-registry.json, w2-outcomes.json |
| ordinary post-wave residual checks (not a padded third swarm) |2: critic1, reviewer1; new merged-oracle/nullable-HEAD-ref-transfer integration checks |2 /0 | residual-spec.json, residual-outcomes.json, residual/ reports |

Total150 actual seats,87 provider-dead,0 replacements. Two all73 cap refusals preceded W1's unchanged third dispatch; one all2 refusal preceded residual dispatch. W2 dispatched once. L1 SoujiR21 holds the canonical planner seat; one connector per wave (minimal per Main routing steer). Specs used policyv2 and exact validator taskCall payloads, no model parameter. New routing affected only fresh residual reviews, not captured waves. Provider error excerpts and per-seat outcomes are durable in `.ufo/waves/round-21/provider-error-excerpts.json`:33 Codex capacity,12 Haiku429,8 Zai429 type1302,1 Antigravity quota429,17 Charm402,16 Devin weekly quota.

Stale-lane: progressing (lane-authored commits throughout); only souji round21 is open in this respawn-per-round lane. No other souji mission or next round started. Tools installed/updated: **none**.

## Landed changes

Every row is tied to `LOG.md` “2026-10-21 — round21 routed privacy/replay repairs…” and its final corrections; `corpus/lessons/round-21.md` records the specific before states, mistakes and dispositions.

| change | pushed commit(s) |
|---|---|
| preregistration / copied r20 outside closure | `544c8358039a07e8b45e6db72312da5c8d965275`, `b2a11849da60479717fd4da6ee95809e2aaa1cb5` |
| clone replay + relocated r16/r18 fixtures | `8513d6ac97076f34ff94a3fc1979c13e69c2d19a` |
| exact frozen18-step inventory / outside-source output guard | `ff425ab835614f38205426330b9cdb93fd267045` |
| nullable source HEAD / baseline identity guards | `7753ed488ea8cdecd3a2e8b08a73ad335804e5a2`, `54eb2d0fb81e9cb5cf5b30430bcfa4b67ddc84ec` |
| original source remotes preserved privately, never jj roots | `195715439a08165ed7319ee6348844fcfba60029` |
| implicit read class / renderer-edge and exact prior-tuple preservation | `f2248c026bcce5f3a919fa6ac57cd8d9ca18cffa`, `894fc9309aaf037d939a263e2dc726ea1a6bb4b2` |
| shared reason redaction, bound, argv provenance, proc-free canary | `4d5bf78432de7f4afe38e6bf195fd7843bdcb7e3` (final check at1957154) |
| source curation, Q47–Q50, knowledge/SKILL/PROVINCE corrections | `4b826a52cb4519b413b874fc9a3d26074c8a33b6`, `4eb2fda51c9917abd734c7e411f98cbb59c5c0fe` |
| current exception lifecycle cleanup, original red gate retained | `e33d2959d06d246ba1f3018df43030dd195d6347` |
| final evidence, independent oracle, terminal accounting, zero gate and cleanup | **`41553adb139d06511dc386bb3ce4326aebfba675`** |

Lane tip/remote equality observed: `41553adb139d06511dc386bb3ce4326aebfba675`, ahead0/behind0/tracked0. The only untracked item is the inherited operator-owned `census/operator-sweep-20261019/`, intentionally unread/unstaged; round-authored work is clean. No inherited lane-authored round21 attempt existed.

## Before → after measurements

| claim | counting command and observations | measured revisions / retained output |
|---|---|---|
| C1 calibration | `python3 -B tests/fixtures/r21-read-root.py --tool T --base-tool B`:18/32→32/32,14 discriminators. `r21-read-render-edges.py --tool T`:0/4→4/4. `python3 -B census/round-21/count-read-root.py --tool T --transcripts census/round-20/transcripts/final --transcripts census/round-20/transcripts/recovery --transcripts census/round-20/transcripts/recovery-final --oracle census/round-21/read-root-oracle.tsv`:0→3 raw flags; final tp3/fp0/fn0/labelled2372/missing0/extra0, all401 prior tuples equal | baseline `6ff3413bba9c8430c3b0bc4d2052e21d0407183f`; final code `195715439a08165ed7319ee6348844fcfba60029` (same auditor bytes as54eb2d0); `read-full-before.json`, `oracle-acceptance.json`, `final-code-verification.json` |
| C2 operability | `bash census/round-21/replay-matrix.sh --runner RUNNER --rev FULL40 --lane LOCAL --work NEW`:0/3→3/3, each18/18, selected summaries equal. `r21-replay-boundaries.py`:4/8→8/8; `r21-source-head.py`:2/3→3/3; `r21-source-refs.py`:remote-only0/1→1/1 (18/18), `--keep-only` retains exit2/no output | old runner `5ff75657427c4793fbf1f124d794f1c99359d74e`; C2-alone18/18 at8513d6ac proves separability; final1957154; `replay-before.txt`, `accepted-matrix.json`, `remote-source-before.json`, `remote-source-after.json`, `final-code-verification.json` |
| C3 coverage | `bash tests/fixtures/r21-reason-canary.sh --tool T --base B` (old-emission arm adds `--baseline-as-tool`):6/27→27/27, leaks19→0, max454→160; two arbitrary-input sinks with the inherited patterns1/2→2/2. Non-secret controls byte-exact;8 cmd probes byte-equal | base6ff3413, repair4d5bf784, final1957154; `reason-oracle-before.txt`, `final-code-verification.json`, `cmd-compatibility.json`; S100/S101 |

B files are extracted from the named full baseline revision; fixture digest guards reject altered inputs. Scores stay7/8/8 with numeric delta0. No universal privacy, full scanner recheck or scope-clean wave is inferred.

Scratch-clone replay (no lane mutation; output outside the clone):

```sh
CHECK=$(mktemp -d /var/tmp/souji-r21-replay.XXXXXX)
git clone --quiet --no-local /home/vgpnk/Projects/shokunin/souji-shokunin "$CHECK/src"
git -C "$CHECK/src" show 6ff3413bba9c8430c3b0bc4d2052e21d0407183f:tools/souji-proc-census.sh > "$CHECK/proc-base.sh"
python3 -B "$CHECK/src/census/round-21/run-acceptance.py" --root "$CHECK/src" --rev 195715439a08165ed7319ee6348844fcfba60029 --output "$CHECK/acceptance.json"
bash "$CHECK/src/tests/fixtures/r21-reason-canary.sh" --tool "$CHECK/src/tools/souji-proc-census.sh" --base "$CHECK/proc-base.sh"
```

## Sources & frontier

Frozen contractv1 applied. Rows99→103; A95→99, B3/C1 unchanged; mined78→81, queued15 unchanged, rejected6→7; malformed rows0, duplicate-ID/enum errors0. Source counts from `python3 -B census/round-13/count-claims.py 6ff3413bba9c8430c3b0bc4d2052e21d0407183f` and the same command at1957154 (`domain-counts-before.json`, `domain-counts-final.json`). Admitted-marked knowledge paths7→7—not a fresh outside-admission count. No frontier moved to Core.

- S100 CWE-532, S101 OWASP Logging, S102 git-clone: opened this round by L1 and mined; located ≤25-word quotes/access dates in the lesson Gate. F5 knowledge cites S100/S101.
- S103 Reproducible Builds definition: opened and rejected as support for bit-identical build claims from acceptance logs; explicit reversal condition retained. Outside reviewer can sample this reject and S100 admit.
- Existing row status/recheck/used-by changes: **none**. Unopened source-scribe candidates get no invented row. Search log records four identified/screened, three mined, one rejected.
- Mistakes R21-M1–M7, subsequent source/oracle ordering and landing-gate corrections are in the lesson; each actual code repair has a red-before witness. No static expectation is relabelled as a run.

Both census runs used:
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin souji`.
W04 duplicate-URL warnings are retained, not hidden. Before output/exit:

```text
souji	W04	S035 duplicate url git-scm.com/docs/git-repo across scopes
souji	W04	S036 duplicate url git-scm.com/docs/git across scopes
souji	W04	S038 duplicate url www.gnu.org/software/coreutils/manual/html_node/timeout-invocation.html across scopes
souji	W04	S049 duplicate url git-scm.com/docs/git across scopes
souji	W04	S057 duplicate url git-scm.com/docs/git-config across scopes
souji	W04	S058 duplicate url git-scm.com/docs/git-worktree across scopes
souji	W04	S059 duplicate url git-scm.com/docs/gitattributes across scopes
souji	W04	S063 duplicate url git-scm.com/docs/git-gc across scopes
souji	W04	S065 duplicate url www.gnu.org/software/bash/manual/html_node/The-Set-Builtin.html across scopes
souji	W04	S072 duplicate url www.gnu.org/software/bash/manual/html_node/The-Set-Builtin.html across scopes
souji	W04	S073 duplicate url man7.org/linux/man-pages/man2/kill.2.html across scopes
souji	W04	S075 duplicate url man7.org/linux/man-pages/man5/proc_pid_stat.5.html across scopes
souji	W04	S076 duplicate url man7.org/linux/man-pages/man5/proc_pid_exe.5.html across scopes
souji	W04	S077 duplicate url man7.org/linux/man-pages/man2/open.2.html across scopes
souji	W04	S086 duplicate url man7.org/linux/man-pages/man5/proc_pid_fd.5.html across scopes
souji	W04	S087 duplicate url man7.org/linux/man-pages/man5/proc_pid_wchan.5.html across scopes
souji	W04	S088 duplicate url man7.org/linux/man-pages/man5/proc_pid_status.5.html across scopes
souji	W04	S089 duplicate url git-scm.com/docs/git across scopes
souji	W04	S090 duplicate url git-scm.com/docs/git-filter-branch across scopes
souji	W04	S091 duplicate url git-scm.com/docs/git-rev-parse across scopes
souji	W04	S092 duplicate url git-scm.com/docs/git-for-each-ref across scopes
souji	W04	S093 duplicate url git-scm.com/docs/git-diff across scopes
souji	W04	S094 duplicate url www.gnu.org/software/coreutils/manual/html_node/timeout-invocation.html across scopes
souji	W04	S095 duplicate url man7.org/linux/man-pages/man5/proc_pid_fd.5.html across scopes
souji	W04	S096 duplicate url man7.org/linux/man-pages/man5/proc_pid_fd.5.html across scopes
souji	W04	S097 duplicate url git-scm.com/docs/git-filter-branch across scopes
souji	W04	S098 duplicate url www.gnu.org/software/coreutils/manual/html_node/timeout-invocation.html across scopes
souji	W04	S099 duplicate url git-scm.com/docs/git-rev-parse across scopes
souji	ok	/home/vgpnk/Projects/shokunin/souji-shokunin/corpus/SOURCES.md
exit=0 command=/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin souji
```

After output/exit:

```text
souji	W04	S035 duplicate url git-scm.com/docs/git-repo across scopes
souji	W04	S036 duplicate url git-scm.com/docs/git across scopes
souji	W04	S038 duplicate url www.gnu.org/software/coreutils/manual/html_node/timeout-invocation.html across scopes
souji	W04	S049 duplicate url git-scm.com/docs/git across scopes
souji	W04	S057 duplicate url git-scm.com/docs/git-config across scopes
souji	W04	S058 duplicate url git-scm.com/docs/git-worktree across scopes
souji	W04	S059 duplicate url git-scm.com/docs/gitattributes across scopes
souji	W04	S063 duplicate url git-scm.com/docs/git-gc across scopes
souji	W04	S065 duplicate url www.gnu.org/software/bash/manual/html_node/The-Set-Builtin.html across scopes
souji	W04	S072 duplicate url www.gnu.org/software/bash/manual/html_node/The-Set-Builtin.html across scopes
souji	W04	S073 duplicate url man7.org/linux/man-pages/man2/kill.2.html across scopes
souji	W04	S075 duplicate url man7.org/linux/man-pages/man5/proc_pid_stat.5.html across scopes
souji	W04	S076 duplicate url man7.org/linux/man-pages/man5/proc_pid_exe.5.html across scopes
souji	W04	S077 duplicate url man7.org/linux/man-pages/man2/open.2.html across scopes
souji	W04	S086 duplicate url man7.org/linux/man-pages/man5/proc_pid_fd.5.html across scopes
souji	W04	S087 duplicate url man7.org/linux/man-pages/man5/proc_pid_wchan.5.html across scopes
souji	W04	S088 duplicate url man7.org/linux/man-pages/man5/proc_pid_status.5.html across scopes
souji	W04	S089 duplicate url git-scm.com/docs/git across scopes
souji	W04	S090 duplicate url git-scm.com/docs/git-filter-branch across scopes
souji	W04	S091 duplicate url git-scm.com/docs/git-rev-parse across scopes
souji	W04	S092 duplicate url git-scm.com/docs/git-for-each-ref across scopes
souji	W04	S093 duplicate url git-scm.com/docs/git-diff across scopes
souji	W04	S094 duplicate url www.gnu.org/software/coreutils/manual/html_node/timeout-invocation.html across scopes
souji	W04	S095 duplicate url man7.org/linux/man-pages/man5/proc_pid_fd.5.html across scopes
souji	W04	S096 duplicate url man7.org/linux/man-pages/man5/proc_pid_fd.5.html across scopes
souji	W04	S097 duplicate url git-scm.com/docs/git-filter-branch across scopes
souji	W04	S098 duplicate url www.gnu.org/software/coreutils/manual/html_node/timeout-invocation.html across scopes
souji	W04	S099 duplicate url git-scm.com/docs/git-rev-parse across scopes
souji	ok	/home/vgpnk/Projects/shokunin/souji-shokunin/corpus/SOURCES.md

exit=0
```

## Trend verdicts

- **expansion: unchanged** — no new uncovered knowledge pathname/frontier promotion; source-row growth is not knowledge growth. Existing F5 entry deepened; new replay capability is separately demonstrated in SCORECARD.
- **quality: improved** — current reason output is repaired and bounded under synthetic canaries; independent-path replay and source-shape refusals are exercised. Unknown secret patterns, historical exposure and inherited result-predicate robustness are not falsely certified.
- **discernment: improved (author assessment)** — r20 outside disagreements became lesson-backed Q47–Q50 and shown-able-to-fail fixes; false vacuity/count-only/partial-corpus inferences were corrected, process deviations disclosed. Outside admit/reject spot-check and round admission remain pending; these seats are author-side.

## SHONEN

- [~] Real decision tables/error patterns/checklists and sources — `SKILL.md`, `corpus/SOURCES.md` S100–S103, `corpus/lessons/round-21.md`; no non-author promotion verdict asserted.
- [~] End-to-end domain task logged — inherited operator task `LOG.md:362` remains the named evidence; no new cleanup authorization fabricated.
- [~] Instructions executable without oral context — `census/round-21/accepted-matrix.json`, `remote-source-after.json`, scratch-clone recipe above.
- [~] No cross-domain bleed asserted within the stated province — `PROVINCE.md` r21 privacy boundary and `.ufo/waves/round-21/w1/ConnSiblingOverlap.md`; credentials/exposure Kagi, host/fleet health Mori, fixture craft Tameshi. No [x] without a named outside verifier.
