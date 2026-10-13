# Round-15 closure review — gate-integrity lane (ClosureReviewer)

Scope: `.ufo/waves/round-15/round15-entries.json` (18-entry draft), `.ufo/waves/round-15/closure-check.py` (round-15 gate, post-L1-amendment), `/tmp/fleet-override.yml` (visible surface only). Review is read-only; every claim below was re-executed, not trusted.

Temporal scope: this review froze the first 18-entry append before the
six-entry follow-up, two note-only corrections, final prompt-parser guard,
and digest-pinned snapshots. Its structural verdict remains evidence for that
append; final counts and controls are in `mutation-gate.md` §FINAL,
`exec-gate.md` §§6/8, and `frozen/r15-{pre-003400,post-012710}/`.

**Verdict: PASS on every contract item; one non-blocking accuracy flag (stale quoted gate verdicts in two notes after the L1 `EXTERNAL_READONLY` amendment).**

Mid-review environment change observed (not interference): at 2026-09-29T01:21 the draft was appended to `MANIFEST.json` (uncommitted, entries 48–65, `closed_at` filled `2026-09-29T00:34:00-03:00`), and two in-flight missions landed reports (aggregator r11 `b159992` 01:24:49; kengaku r14 `896660a` 01:22:57). Consequence: the live repo itself is now the post-append smoke — all "post-append" results below are the real gate run on the real repo.

## 1. Ledger validation — `round15-entries.json`

| Contract item | Result | Evidence |
|---|---|---|
| JSON shape / 18 entries / 26 lane rows | **PASS** | `python3` parse: `entries: 18`, `lane rows: 26`. Types: 13 `closure-correction` + 5 `closure`. |
| Every closure-correction carries exact `supersedes.entry` | **PASS** | All 13 have `supersedes` = `{round, type, date, entry:int}`. Re-verified targets against `MANIFEST.json` `rounds[]`: index in range, `round`/`type`/`date` triple matches target, corrected lane present in target `lanes`. Targets: #45 ×5 (r15), #27 ×2 (r14), #44, #21, #38, #14, #13, #43 — all resolve; e.g. `rounds[45]` is `r15 closure 2026-09-28` carrying `kake/kotoba/kumitate/kagi: in-flight` + `protocol: not-dispatched`. Gate agrees: post-append run reports **0 supersedes contradictions**. |
| No duplicate `(lane, round)` rows | **PASS** | Counter over all 26 (lane, entry.round) pairs: `dups: {}`. |
| No `not-dispatched` | **PASS** | Status tally: `ok=11, in-flight=9, failed=6, not-dispatched=0`. |
| In-flight rows carry `closed_at` placeholder + own round key | **PASS** | All 9 in-flight rows sit in entries whose `closed_at` is the literal `"CLOSED_AT"` (draft placeholder, correctly filled to `…T00:34:00-03:00` in the applied MANIFEST) and whose `entry.round` equals the described lane-round: protocol r15@#52, kengaku r14@#54, aggregator r11@#58, kama r2@#62, kake/kumitate/kotoba/kagi r17@#64, kasegi r18@#65. The one `lane_rounds` annotation (aggregator r10 entry, `lane_rounds[aggregator]=10`) equals its `round` key — annotation, never a re-key, consistent with P:247-256 and gate `analyze:1143` (`v == r` → continue). |
| kama r1 round=1 + r2 round=2 | **PASS** | `kama` rows: `(1, ok)`, `(2, in-flight)` — first entries ever naming kama (`existing kama rows: []` in live manifest; `rounds[36]` is the `mint` record, no `lanes`). Gate admits them: `kama 1 ok entry #61`, `kama 2 in-flight entry #62`. |

Structural: every entry carries `date: 2026-09-29`, `type` in the adjudicated vocabulary, `lanes` a map, `closed_at` present on every entry (all 18 carry in-flight or supersede rows; none needs `lane_rounds` except the one annotation present).

## 2. Marker predicates — re-run on the six files

Predicate (P:150-155 / `_grade_file:462`): bytes < 400 AND no hex run ≥7 AND no `SHONEN` heading. Commands: `stat -c%s`, `grep -oE '(^|[^0-9a-fA-F])[0-9a-f]{7,}([^0-9a-fA-F]|$)' | wc -l`, `grep -cE '^#{1,6}[[:space:]]*SHONEN'`, `git ls-files --error-unmatch`, `head -1`.

| File | bytes | hex | SHONEN | tracked | first line | Note match |
|---|---|---|---|---|---|---|
| round-13/protocol.md | 275 | 0 | 0 | T | `# protocol round-13 closeout (marker)` | exact |
| round-14/protocol.md | 340 | 0 | 0 | T | `# protocol round-14 closeout (marker)` | exact |
| round-10/aggregator.md | 187 | 0 | 0 | T | `# aggregator round-10 closeout (marker)` | exact |
| round-12/kengaku.md | 274 | 0 | 0 | T | `# kengaku round-12 closeout (marker)` | exact |
| round-15/kotoba.md | 273 | 0 | 0 | T | `# kotoba round-15 closeout (marker)` | exact |
| round-16/kasegi.md | 273 | 0 | 0 | T | `# kasegi round-16 closeout (marker)` | exact |

All six are markers → `failed` rows correct. Introducing commits verified (`git log --diff-filter=A`): r13 proto `17c1fad` (fleet relaunch, operator), r14 proto `ef36757` (integrator), r10 agg `f5d8507` (integrator), r12 kengaku `17c1fad`, r15 kotoba `4419fb9` (**kotoba-shokunin** — the note's "lane-identity commit whose subject claims an axis move the file body does not record" checks out), r16 kasegi `17c1fad`. **PASS.**

## 3. Ok-row spot checks — all verified

`stat -c%s` + SHONEN + hex-token count + `git ls-files` + introducing commit + `git merge-base --is-ancestor <intro> HEAD` + cited-hash ancestry in child repos:

- **kake r15** 7486 B, sho=0 (defect noted), 9 unique tokens (note's count; my raw count 10 = `9c28d29` twice — not an error), intro `3069841` operator, ancestor.
- **kumitate r15** 9072 B, sho=1, intro `4d518fe` (subject literally records the recovery), ancestor; `637d181`, `dffbf0e` ancestors of kumitate-shokunin HEAD.
- **kagi r15** 13554 B, sho=0, intro `3485880` operator, ancestor; `2486643` ancestor of kagi-shokunin HEAD.
- **kengaku r13** 4220 B, sho=0, 0 hex tokens, intro `17c1fad` (swept), ancestor — ok + defects as noted; a `failed` row here would trip `failed-vs-report` (real report present).
- **aggregator r9** 18604 B, sho=1, 31 unique tokens (raw 36), intro `cc6d9d4` **aggregator-shokunin** (clean lane identity — the draft's only defect-free attribution), ancestor; sampled child-repo citations all ancestors (`0f2dca0` kasegi, `0f658ff` kotoba, `4214101` kake, `4391b3b` kagi, `7a099b2` kumitate).
- **kama r1** 10144 B, sho=0, 8 tokens, intro `74768ab` operator, ancestor; `c6199a2` = kama-shokunin HEAD (verified: `merge-base` rc 0, `log -1` subject `round-1: operability axis — runnable endpoint-identity gate`); `0522e67a`, `5725fa7d3` ancestors of `origin-work/ufo-fsd-alpha` HEAD.
- **r16** (kake 12005, kumitate 15354, kotoba 9700, kagi 15021 B) — all tracked, intro commits `c3b0c0e`/`5846679`/`208db49`/`17c1fad` all ancestors of main HEAD; `637d181`/`db61be0` kumitate ancestors + `5725fa7d3`/`93798be12` ufo-fsd ancestors; `b25f37a` kotoba ancestor; `587fda0` kagi ancestor.
- **kasegi r17** 4708 B, tracked, intro `17c1fad`, ancestor — see flag §5a.

Log-line digests: every quoted `launch`/`complete`/`wrap` line greps exactly once (×3 for the kama r1 wraps) in `.ufo/watchdog.log` with the quoted timestamps (`grep -c` per line, spot list of 44 lines → all 1× or the stated multiplicities). Counters: `.ufo/state/{protocol,aggregator,kasegi,kengaku,kake,kumitate,kotoba,kagi,kama}.round` = 15,11,18,14,17,17,17,17,2 — every value the notes claim. All nine `complete <lane> round=<N>` greps → 0; all nine report paths absent at the probe instant (two since landed, §below). **PASS.**

## 4. Gate trust semantics vs PROTOCOL.md / PROTOCOL-APPENDIX.md — no regression found

- **Dynamic lane universe** (`_lane_universe:293`): roster ∪ base `LANES` ∪ `.ufo/state/*.round` ∪ dispatch/complete/wrap-line lanes ∪ prompt-file lanes — implements A:42 verbatim, including the m10 residual fix (log lines alone admit a lane). Live run: `lane universe: 9 lanes … counter-only (probation, no roster row): kama`; zero `unknown_lane` findings; `kama 1 ok` / `kama 2 in-flight` graded normally — the r12-gate `unknown-lane` pair is fully explained by its hardcoded LANES, as J6 claims. Fixture `kama-counter-admitted` passes.
- **`unknown_lane` classification**: readable-but-unknown ids now join the universe by design (A:42); only grammar-unreadable tokens (loose-RE `foreign` buckets) and `lane_rounds` annotations outside the universe yield `unknown_lane` findings → `COULD_NOT_EVALUATE_CLASSES` → exit 2 only when debt-free (`analyze:1415`). Consistent; `foreign_prompts` is unreachable by construction (universe is closed over prompt lanes before the partition) — dead-but-harmless code path, note only.
- **Wrap handling**: `RE_WRAP` + `RE_WRAP_LOOSE` (`:122-128`, parse `:489-494`, merged into `raw_completes` with `verb: "wrap"`). 22 wrap lines + 104 complete lines = 126 completes, matching J7(c). Termination evidence per P:224-231 — correct: a wrap line says `complete`. Fixture `wrap-terminated-unreported` passes.
- **Non-closure entries**: `NONCLOSURE_TYPES = (mint, scaffold, work, ops)` — recognized and reported, `lanes` maps kept out of the ledger as `unadjudicable` (`build_ledger:577-592`); anything else → `unknown_entry_type` (CNE). Live run reports the 5 non-closure entries verbatim (#0 scaffold, #1/#3 work, #2 ops, #36 mint). P:208-211 honored — never silent.
- **History pin** (`_history_pin_check:923-983`): canonical-JSON sha256 of `rounds[0:k]` vs pin, then anchor `git show <commit>:MANIFEST.json` re-hash + `merge-base --is-ancestor` — exactly P:271-274's "pinned + anchored" model. Live: `anchored at ae19fca k=48 prefix=ce97497ed699` — appends did not invalidate it, as designed.
- **Empty watchdog-driver exclusion**: docstring `:15-20` documents it as a reserved error sink read by nothing; `load_live:360` reads only `.ufo/watchdog.log`; file is 0 B, untracked, no driver reference. J7(b) confirmed. No stray-traceback→dispatch path exists.
- **Frozen mode**: `--frozen` resolves under `.ufo/waves/*/frozen`, fails closed on duplicate names (`_resolve_frozen:1015-1022`); citations disabled in frozen (`load_frozen:449`). Consistent with A:45.
- **Exit map**: `EXIT_DEBT if debt else (EXIT_ERROR if cne else EXIT_OK)` (`:1415`) — CNE never masks debt. Observed: exit 0 (debt-free), exit 1 (after two reports landed mid-review → `stale_in_flight` debt=2, `suggested: ok` — the intended re-confirmation loop, not a defect of the ledger or gate).
- **Selftest**: `--selftest` → `24/24 passed`, including `unknown-lane-annotation` (exit 2, cne=2), `ambiguous-supersedes`, `lanes-list-duplicate`, `not-dispatched-without-lane_rounds`, `wrap-terminated-unreported`, `kama-counter-admitted`, `mint-nonclosure-entry`.

### Gate gaps observed (informational, none blocking this draft)

- **Unparseable `closed_at` silently disables liveness checks**: `build_ledger` requires `closed_at` *present* but `analyze` uses `iso()` — a garbage string parses to `None` and every `<= closed_at` check is skipped (`:1199-1208`, `:1249-1256`). The draft's literal `"CLOSED_AT"` would have sailed through unverified had it been appended unfilled; the applier filled it correctly. A `closed_at`-not-ISO contradiction rule would close this class (gate owner, future round).
- **9-digit all-digit runIds classify `dead`**: runId filter in `citation_sweep:836` exempts only `len >= 10`, so kama's `101125103`-shaped tokens read `dead` even though `hash_identity_note` skips them (no a-f). Informational-only (citation findings never drive a status), but it inflates the `dead` tally (live: dead=136, many runId-shaped).
- **`unknown_lane` can't fire for a ledger row of a never-seen lane**: a `lanes` map naming a readable-but-unknown lane id raises a `contradiction` (debt, exit 1) while an unreadable log token raises CNE (exit 2). Asymmetric by design per the taxonomy comment — flagging only because the docstring (`:52-54`) describes the narrower case.

## 5. Flags

- **a) [medium, non-blocking] Stale quoted gate verdicts in two durable notes after the L1 `EXTERNAL_READONLY` amendment.** `closure-check.py:112-114` now reads `["~/Projects/bounties", "~/Projects/origin-work/open-bug-bounties", "~/Projects/webzites", "~/Projects/origin-work/ufo-fsd-alpha", "~/Projects/charter-ufo-fsd"]` (L1 correction, verified present). With the new tree in the sweep, kasegi r17's `1307b8b` **resolves as a commit and is an ancestor of `open-bug-bounties` HEAD — it is the HEAD** (`rev-parse` equal; subject `M03/M04 metamask-sdk-channel-inject REPORT+READY`). The appended notes for kasegi r17 (entry #64) and kengaku r13 (#56) quote the gate flagging `1307b8b`/other tokens `dead` — true when drafted, mechanically unreproducible now. Row statuses unaffected (the file remains non-marker ≥400 B → `ok`; the defect's substance — no resolvable commit *in the lane's own repo* — still stands since obb is not kasegi's repo). Next pass SHOULD refresh the quoted lines; no ledger or gate change needed. Also confirmed: the other previously-dead tokens I sampled (`68939d0c`, `6ca2a358`, `fb365e38`, `2ee8abae`) still resolve nowhere post-amendment, so the broad `dead` claims in the kake r15/r16 notes remain accurate.
- **b) [low] Header J5 says past ~00:34:34 the in-flight rows "read as `stale_in_flight` debt."** Observed: at age ~3780 s the same rows render under "Live in-flight (compliant)" + "Stale missions (activity probe, not a verdict)" with debt=0 — `stale_in_flight` fires only on *termination since closed_at* (`analyze:1217-1234`), which is what the two later-landed reports produced (`debt=2, suggested: ok` for aggregator r11 + kengaku r14 — the intended loop, now due for a re-confirmation pass). The re-confirmation duty stands; the header's mechanism description is inaccurate.
- **c) [info] Notes for entries #53/#59 say wrap lines are "not matched by the gate's RE_COMPLETE"** — literally true (RE_WRAP is a third regex) but the r15 gate *does* count them as termination (`wrap-terminated-unreported` fixture). Read as describing the r12 gate; no correction needed.
- **d) [info] Unadjudicable-dispatch asymmetry noted in §4 third bullet; dead `foreign_prompts` path.** Cosmetic.

## 6. Effective config — `/tmp/fleet-override.yml` (reported verbatim, nothing inferred)

```yaml
task:
  agentModelOverrides:
    planner: "@m_lunamax"      connector: "@m_lunamax"
    executor: "@m_flash"       scribe: "@m_flash"        scout: "@m_flash"
    reviewer: "@m_zfl"         critic: "@m_zfl"          sentinel: "@m_zfl"
    revenger: "@m_zfl"         labrat: "@m_zfl"          mutation-tester: "@m_zfl"
    simplifier: "@m_zfl"       distiller: "@m_zfl"
```

The file is the task-agent override map: no `m_swe` key, no `modelRoles`, no `retry`/`fallbackChains` section visible here. **No m_swe fallback inferred from absence** — this file simply does not carry that surface.

## Blocking list

None. Draft is internally consistent, supersedes targets exact, all measured claims reproduced, gate semantics conform to PROTOCOL.md + PROTOCOL-APPENDIX.md, and the applied manifest closes cleanly (post-append live run: `closure-check: ok debt=0 … exit 0` at 01:2x pre-landing; current exit 1 is the intended re-confirmation debt for the two reports that landed mid-review, with `suggested: ok`).

## Commands run (all real, outputs above)

`json.load` + structural assertions (eval); `stat -c%s`, `grep -oE '(^|[^0-9a-fA-F])[0-9a-f]{7,}([^0-9a-fA-F]|$)' | wc -l`, `grep -cE '^#{1,6}[[:space:]]*SHONEN'`, `head -1` ×6 marker files + ×11 ok files; `git ls-files --error-unmatch`; `git log --diff-filter=A -1 --format=…` per report; `git merge-base --is-ancestor <h> HEAD` in main + kagi/kumitate/kotoba/kama + `origin-work/ufo-fsd-alpha` + `origin-work/open-bug-bounties`; `grep -c ' <line>' .ufo/watchdog.log` ×44; `cat .ufo/state/*.round` ×9; `ls` on 9 report paths; `git ls-files -o --exclude-standard .ufo/prompts`; `python3 .ufo/waves/round-15/closure-check.py --repo . [--no-citations]` (3 runs, exits 0/1/1 across the mid-review landings); `python3 .ufo/waves/round-15/closure-check.py --selftest` (24/24).
