# souji — round 43 (attempt 2)

## Work performed

Declared claims: **C1 calibration**, three historical self-assessment corrections; **C2 operability**, defensive freeze-check grammar; **C3 coverage**, sixteen drift-survivor classes plus leaf-symlink refusal. Lowest non-retired axis: calibration 7. Targets and counters inherited unchanged; no target narrowed.

- C1 target measured met, but its counter does not bind the correction's captured derived value; actual values were separately checked. D3 is a measured-versus-carrier revision clarification, not a false receipt-header repair. Evidence: `census/round-43/records/c1-landed.txt`, `census/round-43/waves/w1/R43rederiveR43D1.md` through `R43rederiveR43D3.md`, lesson `corpus/lessons/round-43.md`.
- C2 checker repaired: first-wins repeated keys, explicit unattached keys, strict ASCII Round values, Control symlink refusal, Control/preregistration edit detection; self-test **41/41**. Frozen counter still **red**: h4 expects a literal starred class, h6 omits its own post-freeze edit finding. No counterfeit finding or oracle amendment. Evidence: `records/c2-landed.txt`, `records/c2-selftest.txt`, `records/c2-hidden-full.txt` under `census/round-43/`.
- C3 **not landed as a capability**: legacy r38 fixture requires leaf-symlink resolution/write, while the frozen new target requires refusal. Main's independent candidate run is 11/12, solely that conflict. Production drift tool and old fixture unchanged. Further frozen wrapper/sniff defects are retained. Evidence: `records/c3-contract-conflict.txt`, `waves/w1/R43reviewer01.md`.
- One validated **v2 wave, 68 seats**, attack share **34/68**. Roles: executor 11, critic 8, mutation-tester 20, scout 12, reviewer 6, sentinel 2, revenger 2, connector 3, simplifier 2, scribe 2. L1 held planner; no residual/replacement. Orchestrator WAVE-DONE received before filing. 33 nonempty returned outputs (some incomplete), **35 terminal provider errors**, not clearance. Durable dispatch/results: `census/round-43/waves/`; exact answering models and terminal errors: `census/round-43/records/seat-terminal-evidence.json`.
- Inherited attempt-1 instruments/controls/source snapshots reused; malformed wave names normalized before validation. Formal preregistration was absent and landed after ready handoff: irreversible **timing conformance defect**, disclosed. Frozen files unchanged after registration. Evidence: `census/round-43/preregistration.txt`, commits below.
- Three connector scans report adjacent mechanisms, not a proven ownership collision; chousa research checks, kaidoku replacement semantics and kumitate input-link policy were not absorbed. Evidence: `census/round-43/waves/w1/R43connector01.md`, `R43connectorA.md`, `R43connectorB.md`.
- Misroot sweep `git -C /home/vgpnk/Projects/shokunin status --porcelain` showed only operator `.scratch/goal-20261029-hyaku-run12.md` and mori-r61 `count-c1.cover`/`count-c2.cover`; provenance inspected, all untouched. No souji misroot found. Receipt: `census/round-43/records/wave-summary.json`. Owned scratch removed after landing.

**Admission:** not claimed. C1 reaches its numeric target, but its instrument has substantive limits; C2/C3 miss unchanged targets. Exercised C2 retention stays green; exhaustive no-axis-harm and outside admit/reject clearance remain unverified. No score delta; calibration 7 / operability 8 / coverage 8 unchanged. Certification OFF, K5 HELD, NAMESPACE hold unchanged.

**Stale-lane:** respawn-per-round; no other souji mission is open. No new L0 question added; inherited operator/pacman holds remain. Tool installs/updates: none; pacman remained paused. Hardware-auth/provider-denied work stayed unverified, with no bypass or route change.

## Landed changes

Every item is recorded in `LOG.md:1943-1966` (round-43 entry and addenda).

| commit | landed work |
|---|---|
| `41e69c38cf9420e0304530f32a02c72ad72b7fe5` | inherited counters/populations, source snapshots, census start |
| `f8c805dbfa7f45814cf9a7270fa8bbffb41a8373` | inherited instrument adjustments, C1/C3 controls, correction fixture |
| `13de0e84b45efd1113f077d58fc1e89bc586a013` | inherited C2 before receipt |
| `8dfad888d7b7673de41cdcd92f30244c16e38519` | unchanged formal registration and re-executed red controls |
| `d48afbdcf033a3a2327653ba195e4a973fc71979` | historical correction lines, S260–S262 grounding |
| `d1954ced70eca671e63684386452cf99fdabea87` | defensive freeze checker, 41-case self-test, Q106, registry and honest failed-oracle receipts |
| `2346109226412975144428072c69ff43e243337a` | SCORECARD/LOG/index measurements, S263 discovery-channel correction |
| `db1f1e89738cabd30276dd46acf4ac3860a44718` | settled-wave capture, exact terminal evidence, final census |
| `a637122161afb0ee257aba4335312a50378cb7c9` | explicitly land two >1 MiB connector evidence files skipped by directory commit; record red-before capture and correction |

Final lane branch **master**, pushed hash **`a637122161afb0ee257aba4335312a50378cb7c9`**. Required `git -C /home/vgpnk/Projects/shokunin/souji-shokunin ls-remote origin refs/heads/master` printed `a637122161afb0ee257aba4335312a50378cb7c9	refs/heads/master`.
Committed capture check: `bash tools/souji-wave-evidence-capture.sh LANE 43 --verify --rev a637122161afb0ee257aba4335312a50378cb7c9` → `records=228 failed=0 uncovered=0`, exit 0. Before corrective commit: failed=2, exit 4 (`records/capture-committed-red.txt`); lesson M43-3 preserves the failure.

## Before → after measurements

Run each command from the lane, replacing LANE/REV/DIR with the repository, full commit, and owned scratch directory. Before revision: `13de0e84b45efd1113f077d58fc1e89bc586a013`. After revision: `d1954ced70eca671e63684386452cf99fdabea87`; receipts carry exact argv. Bookkeeping remeasurement at `2346109226412975144428072c69ff43e243337a` retains C1 target and historical mismatch count.

| claim | command | before → after | verdict |
|---|---|---|---|
| C1 | `python3 -B census/round-43/c1-counter.py --root LANE --rev REV --scratch DIR` | required=3 registered=0 missing=3, exit 1 → required=3 registered=3 missing=0 rederived=3 rederive_failed=0 new_mismatches=0, exit 0 | numeric target met; captured-derived binding, prose scope and freeze-timing limits disclosed |
| C2 | `python3 -B census/round-43/c2-counter.py --root LANE --rev REV --scratch DIR` | newtable=2/9 hidden=RED real=RED, exit 1 → newtable=9/9 r42table=ok hidden=RED real=ok selftest=ok tmpdir=ok, exit 1 | **target unmet**, not redefined |
| C3 | `python3 -B census/round-43/c3-counter.py --root LANE --rev REV --scratch DIR` | killed=0 survived=16 cases=0, exit 1 → same, exit 1 | **target unmet**; no partial fixture installed |

Receipts: `census/round-43/controls/c{1,2,3}-resume-before.txt` and `records/c{1,2,3}-landed.txt`. C1 correction fixture: r43 column 10/10 and r42 signature column 10/10, exit 0 (`records/c1-discrimination.txt`); r42 CRLF-signature attribution is not actually exercised, and mutation review finds 9/19 survivors. No exhaustive language-coverage claim. Declared evidence after bookkeeping: `python3 -B tools/souji-declared-evidence.py --root LANE --rev 2346109226412975144428072c69ff43e243337a --file SCORECARD.md` → `assertions=502 resolved=432 skipped=824 mismatches=70`, exit 1; all 70 are historical, C1 new_mismatches=0 (`records/bookkeeping-remeasure.txt`).

## Sources & frontier

Census command both ends:
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin souji`.
Registry rows **183 → 187**, W04 warning rows **52 → 54**, exits **0 → 0**. Count rows with `grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`; count W04 as tab-delimited emitted finding rows, not the inherited footer. Receipts: `census/round-43/records/census-before.txt`, `records/census-final.txt`. The inherited before footer incorrectly says W04=0; actual emitted warnings below are 52, preserved and corrected in lesson.

Added four tier-A scoped rows: S260 symlink existence semantics (C3 documentary grounding), S261 subprocess stderr/environment semantics (C2/C3 grounding), S262 rejected preservation-authority inference, S263 primary PYTHONPATH discovery source correcting r42 review item 5. No old status/recheck/used-by cells changed; new statuses mined=3/rejected=1. Gate quotes, URLs, dates and admit/reject reasons: `corpus/lessons/round-43.md` Gate and addendum. No knowledge entry or capability added, no frontier ground promoted to Core. Assimilation: none. No `considerthese/` directory in this lane. Outside source spot-check pending; lane seats are not non-author reviewers for admission.

Before validator output (exit 0):
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
souji	W04	S106 duplicate url docs.python.org/3/library/json.html across scopes
souji	W04	S108 duplicate url docs.python.org/3/builtins/exceptions.html across scopes
souji	W04	S123 duplicate url git-scm.com/docs/git-worktree across scopes
souji	W04	S124 duplicate url git-scm.com/docs/gitrepository-layout across scopes
souji	W04	S125 duplicate url git-scm.com/docs/git across scopes
souji	W04	S126 duplicate url git-scm.com/docs/git-worktree across scopes
souji	W04	S210 duplicate url raw.githubusercontent.com/GNOME/glib/2.84.0/gio/glocalfile.c across scopes
souji	W04	S216 duplicate url man7.org/linux/man-pages/man2/statx.2.html across scopes
souji	W04	S225 duplicate url man7.org/linux/man-pages/man5/proc_pid_fd.5.html across scopes
souji	W04	S232 duplicate url git-scm.com/docs/git-worktree across scopes
souji	W04	S236 duplicate url git-scm.com/docs/git across scopes
souji	W04	S237 duplicate url git-scm.com/docs/git across scopes
souji	W04	S238 duplicate url git-scm.com/docs/git-config across scopes
souji	W04	S240 duplicate url git-scm.com/docs/git-cat-file across scopes
souji	W04	S241 duplicate url man7.org/linux/man-pages/man7/fifo.7.html across scopes
souji	W04	S242 duplicate url man7.org/linux/man-pages/man2/open.2.html across scopes
souji	W04	S244 duplicate url git-scm.com/docs/git-merge-base across scopes
souji	W04	S245 duplicate url man7.org/linux/man-pages/man2/open.2.html across scopes
souji	W04	S246 duplicate url man7.org/linux/man-pages/man7/pipe.7.html across scopes
souji	W04	S250 duplicate url git-scm.com/docs/gitrevisions across scopes
souji	W04	S251 duplicate url git-scm.com/docs/git-merge-base across scopes
souji	W04	S255 duplicate url docs.python.org/3/library/inspect.html across scopes
souji	W04	S256 duplicate url docs.python.org/3/library/codecs.html across scopes
souji	W04	S257 duplicate url raw.githubusercontent.com/GNOME/gvfs/1.62.0/daemon/trashlib/trashitem.c across scopes
souji	ok	/home/vgpnk/Projects/shokunin/souji-shokunin/corpus/SOURCES.md
```
After validator output (exit 0):
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
souji	W04	S106 duplicate url docs.python.org/3/library/json.html across scopes
souji	W04	S108 duplicate url docs.python.org/3/builtins/exceptions.html across scopes
souji	W04	S123 duplicate url git-scm.com/docs/git-worktree across scopes
souji	W04	S124 duplicate url git-scm.com/docs/gitrepository-layout across scopes
souji	W04	S125 duplicate url git-scm.com/docs/git across scopes
souji	W04	S126 duplicate url git-scm.com/docs/git-worktree across scopes
souji	W04	S210 duplicate url raw.githubusercontent.com/GNOME/glib/2.84.0/gio/glocalfile.c across scopes
souji	W04	S216 duplicate url man7.org/linux/man-pages/man2/statx.2.html across scopes
souji	W04	S225 duplicate url man7.org/linux/man-pages/man5/proc_pid_fd.5.html across scopes
souji	W04	S232 duplicate url git-scm.com/docs/git-worktree across scopes
souji	W04	S236 duplicate url git-scm.com/docs/git across scopes
souji	W04	S237 duplicate url git-scm.com/docs/git across scopes
souji	W04	S238 duplicate url git-scm.com/docs/git-config across scopes
souji	W04	S240 duplicate url git-scm.com/docs/git-cat-file across scopes
souji	W04	S241 duplicate url man7.org/linux/man-pages/man7/fifo.7.html across scopes
souji	W04	S242 duplicate url man7.org/linux/man-pages/man2/open.2.html across scopes
souji	W04	S244 duplicate url git-scm.com/docs/git-merge-base across scopes
souji	W04	S245 duplicate url man7.org/linux/man-pages/man2/open.2.html across scopes
souji	W04	S246 duplicate url man7.org/linux/man-pages/man7/pipe.7.html across scopes
souji	W04	S250 duplicate url git-scm.com/docs/gitrevisions across scopes
souji	W04	S251 duplicate url git-scm.com/docs/git-merge-base across scopes
souji	W04	S255 duplicate url docs.python.org/3/library/inspect.html across scopes
souji	W04	S256 duplicate url docs.python.org/3/library/codecs.html across scopes
souji	W04	S257 duplicate url raw.githubusercontent.com/GNOME/gvfs/1.62.0/daemon/trashlib/trashitem.c across scopes
souji	W04	S261 duplicate url docs.python.org/3/library/subprocess.html across scopes
souji	W04	S262 duplicate url man7.org/linux/man-pages/man2/symlink.2.html across scopes
souji	ok	/home/vgpnk/Projects/shokunin/souji-shokunin/corpus/SOURCES.md
```

## Trend verdicts

- **expansion — unchanged:** no admitted knowledge entry, capability or frontier-to-core move (`corpus/README.md`, SCORECARD round-43 rows).
- **quality — unchanged:** defensive tool improves exercised behavior, but no knowledge entry re-verification/supersession and both C2/C3 full targets remain unmet; no corpus-wide quality increase asserted.
- **discernment — unchanged:** Q106 and sourced S263 capture real oracle/provenance mistakes, but no outside admit-and-reject spot-check is yet on record. New checks are not self-attested admission.

## SHONEN

- [~] Decision tables/error patterns/checklists/cited sources — `SKILL.md:26-187`, registry at `SKILL.md:189`; no non-author promotion verifier assigned.
- [~] End-to-end domain task logged — `LOG.md:362`, inherited operator-approved pushed-artifact sweep; no new removal authority claimed.
- [~] Executable instructions — `census/round-43/preregistration.txt`, three counters and exact receipts; frozen-oracle defects explicitly documented.
- [~] Province boundaries — `PROVINCE.md`, three connector reports; no external-target, credential, history or operator-config mutation.

### Terminal seat failures

35 provider-error endings, no replacements. Exact per-seat error/model/earlier fallback errors are durable in `census/round-43/records/seat-terminal-evidence.json`; final errors:

- `R43critic01`: Codex error event: You’re approved for Daybreak Blue, but this response cannot be shown as this session was not authenticated with one of your authorized hardware keys. Please re-authenticate with your hardware key and try your request again. (code=cyber_policy)
- `R43critic02`: Codex error event: You’re approved for Daybreak Blue, but this response cannot be shown as this session was not authenticated with one of your authorized hardware keys. Please re-authenticate with your hardware key and try your request again. (code=cyber_policy)
- `R43scribe02`: Cursor USAGE_PRICING_REQUIRED: DeepSeek V4.1 Flash 1017 is not included in your weekly usage: Buy credits or switch to a Grok model to continue.
- `R43mutanchorS13`: 429 {"type":"error","error":{"type":"rate_limit_error","message":"Token Plan usage limit reached: Upgrade your Token Plan or purchase Credits for more usage. (2056)"},"request_id":"0733637ca9f7024a169870cb01201962"}
- `R43mutanchorS17`: 429 {"type":"error","error":{"type":"rate_limit_error","message":"Token Plan usage limit reached: Upgrade your Token Plan or purchase Credits for more usage. (2056)"},"request_id":"0733637d4660320e54a4e8b3256458dc"}
- `R43mutanchorS22`: 429 {"type":"error","error":{"type":"rate_limit_error","message":"Token Plan usage limit reached: Upgrade your Token Plan or purchase Credits for more usage. (2056)"},"request_id":"0733637fcf1c00447150c65a27bb1a61"}
- `R43mutanchorS25`: 429 {"type":"error","error":{"type":"rate_limit_error","message":"Token Plan usage limit reached: Upgrade your Token Plan or purchase Credits for more usage. (2056)"},"request_id":"0733638024598c4d27bab5482b194c72"}
- `R43mutanchorS33`: 429 {"type":"error","error":{"type":"rate_limit_error","message":"The Token Plan usage limit has been reached. To avoid interruption, please upgrade your plan or buy credits and turn on auto consumption. (2067)"},"request_id":"0733637f46b07b4b22c8519f2854ed9d"}
- `R43mutanchorS34`: 429 {"type":"error","error":{"type":"rate_limit_error","message":"The Token Plan usage limit has been reached. To avoid interruption, please upgrade your plan or buy credits and turn on auto consumption. (2067)"},"request_id":"07336380c3efb75a45bebd27152d5305"}
- `R43mutanchorS35`: 429 {"type":"error","error":{"type":"rate_limit_error","message":"Token Plan usage limit reached: Upgrade your Token Plan or purchase Credits for more usage. (2056)"},"request_id":"07336382a57279eeb323965fc0ff4d5a"}
- `R43mutanchorS43`: 429 {"type":"error","error":{"type":"rate_limit_error","message":"Token Plan usage limit reached: Upgrade your Token Plan or purchase Credits for more usage. (2056)"},"request_id":"073363844f352902b4ff3b3326dac671"}
- `R43mutanchorS44`: 429 {"type":"error","error":{"type":"rate_limit_error","message":"Token Plan usage limit reached: Upgrade your Token Plan or purchase Credits for more usage. (2056)"},"request_id":"0733638421fb24496f99d77b0695e442"}
- `R43mutanchorS53`: 429 {"type":"error","error":{"type":"rate_limit_error","message":"The Token Plan usage limit has been reached. To avoid interruption, please upgrade your plan or buy credits and turn on auto consumption. (2067)"},"request_id":"073363857c93b9067e48a9ae92ab386e"}
- `R43mutanchorS58`: 429 {"type":"error","error":{"type":"rate_limit_error","message":"The Token Plan usage limit has been reached. To avoid interruption, please upgrade your plan or buy credits and turn on auto consumption. (2067)"},"request_id":"07336386bb2de48a08db8eafade86779"}
- `R43mutanchorS63`: 429 {"type":"error","error":{"type":"rate_limit_error","message":"The Token Plan usage limit has been reached. To avoid interruption, please upgrade your plan or buy credits and turn on auto consumption. (2067)"},"request_id":"07336387d0ec021a0427e08da13d09c0"}
- `R43mutanchorS73`: 429 {"type":"error","error":{"type":"rate_limit_error","message":"Token Plan usage limit reached: Upgrade your Token Plan or purchase Credits for more usage. (2056)"},"request_id":"073363872ba746099408f8ebb46868fa"}
- `R43casebuildA`: 429 {"type":"error","error":{"type":"rate_limit_error","message":"The Token Plan usage limit has been reached. To avoid interruption, please upgrade your plan or buy credits and turn on auto consumption. (2067)"},"request_id":"0733638cfef947d56b62fc9a5782c124"}
- `R43casebuildB`: 429 {"type":"error","error":{"type":"rate_limit_error","message":"Token Plan usage limit reached: Upgrade your Token Plan or purchase Credits for more usage. (2056)"},"request_id":"0733638c0a1eda5020b3042e36a47a56"}
- `R43casebuildC`: 429 {"type":"error","error":{"type":"rate_limit_error","message":"The Token Plan usage limit has been reached. To avoid interruption, please upgrade your plan or buy credits and turn on auto consumption. (2067)"},"request_id":"0733638dff34f0c14891a5639334f3fd"}
- `R43classauditKEYDUPLICATE`: Cursor USAGE_PRICING_REQUIRED: DeepSeek V4.1 Flash 1017 is not included in your weekly usage: Buy credits or switch to a Grok model to continue.
- `R43classauditUNATTACHEDKEY`: Cursor USAGE_PRICING_REQUIRED: DeepSeek V4.1 Flash 1017 is not included in your weekly usage: Buy credits or switch to a Grok model to continue.
- `R43classauditROUNDMALFORMED`: Cursor USAGE_PRICING_REQUIRED: DeepSeek V4.1 Flash 1017 is not included in your weekly usage: Buy credits or switch to a Grok model to continue.
- `R43classauditCONTROLSYMLINK`: Cursor USAGE_PRICING_REQUIRED: DeepSeek V4.1 Flash 1017 is not included in your weekly usage: Buy credits or switch to a Grok model to continue.
- `R43classauditFROZENEDITEDextende`: Cursor USAGE_PRICING_REQUIRED: DeepSeek V4.1 Flash 1017 is not included in your weekly usage: Buy credits or switch to a Grok model to continue.
- `R43classauditCRLFprereg`: Cursor USAGE_PRICING_REQUIRED: DeepSeek V4.1 Flash 1017 is not included in your weekly usage: Buy credits or switch to a Grok model to continue.
- `R43scoutH`: Cursor USAGE_PRICING_REQUIRED: DeepSeek V4.1 Flash 1017 is not included in your weekly usage: Buy credits or switch to a Grok model to continue.
- `R43scoutHT`: Cursor USAGE_PRICING_REQUIRED: DeepSeek V4.1 Flash 1017 is not included in your weekly usage: Buy credits or switch to a Grok model to continue.
- `R43revenger02`: Devin stream error permission_denied: This model is no longer available for your account. Please switch to a different model.
- `R43sentinel02`: 429 {"type":"error","error":{"type":"rate_limit_error","message":"The Token Plan usage limit has been reached. To avoid interruption, please upgrade your plan or buy credits and turn on auto consumption. (2067)"},"request_id":"0733639b5b32ea5d19819414ee4955a7"}
- `R43simplifier02`: Cursor USAGE_PRICING_REQUIRED: DeepSeek V4.1 Flash 1017 is not included in your weekly usage: Buy credits or switch to a Grok model to continue.
- `R43mutationtester03`: 429 {"type":"error","error":{"type":"rate_limit_error","message":"Token Plan usage limit reached: Upgrade your Token Plan or purchase Credits for more usage. (2056)"},"request_id":"0733639c1de97f982b9d2af80731e0ae"}
- `R43critic04`: 429 {"type":"error","error":{"type":"rate_limit_error","message":"The Token Plan usage limit has been reached. To avoid interruption, please upgrade your plan or buy credits and turn on auto consumption. (2067)"},"request_id":"0733639dc513f8e57a2b8c95fa26a96b"}
- `R43critic05`: 429 {"type":"error","error":{"type":"rate_limit_error","message":"Token Plan usage limit reached: Upgrade your Token Plan or purchase Credits for more usage. (2056)"},"request_id":"0733639f60da2ecdba3811446838bf36"}
- `R43mutationtester04`: 429 {"type":"error","error":{"type":"rate_limit_error","message":"Token Plan usage limit reached: Upgrade your Token Plan or purchase Credits for more usage. (2056)"},"request_id":"0733639f25d7ea5e42c15afc6ffd45c6"}
- `R43scout03b`: Cursor USAGE_PRICING_REQUIRED: DeepSeek V4.1 Flash 1017 is not included in your weekly usage: Buy credits or switch to a Grok model to continue.
