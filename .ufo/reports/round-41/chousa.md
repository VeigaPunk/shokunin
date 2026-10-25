# chousa — round 41 report (hyaku inline campaign, attempt 1)

Lane tip (measured and pushed): `a3aac04492a3a5e99e351fc9941fcba801c152fe` on `master` (`jj-lane.sh state`: local=remote, ahead=0 behind=0). Work commit cited for claims: `1bd9001330f19d89ec36592010d4218881ea5941` (ancestor of tip; the tip adds only the SCORECARD entry). Freeze commit: `b173b0943e647f7e3a365689df19debe40fd9dd2`.

## Work performed

Declared claims (2):

- **C1 — operability** (lowest-scored non-retired axis, 3/10): every external invocation attributable to the canonical pin/drift capture — parent capture functions, startup (`SELF`/`TS_UTC`), and the captured `verify-all` child — resolves through a frozen 14-name GNU-verified pin table (r35 wrapper pattern) plus a fixed `CAP_CHILD_PATH=/usr/bin:/bin` child PATH and an `LD_PRELOAD`/`LD_LIBRARY_PATH` scrub.
- **C2 — calibration**: every `W04` duplicate-URL warning emitted by the maintained census carries a committed, evidence-resolving disposition row (join-verified, not advisory prose).

Work items:

- Instrumentation run sized the real surface before freezing: 728 PATH-resolved calls in one `--pin`, 20 across pin+drift parent+child (`corpus/evidence/round41/claims.md` measured-surface paragraph).
- Gate: added `captool_pin_init` + wrappers for `mktemp sed mkdir cat rm sort readlink dirname date tr wc od head stat` (override `RESEARCH_GATE_<NAME>`, refusal `<NAME>_PROVENANCE`); child env now unsets `LD_PRELOAD`/`LD_LIBRARY_PATH` and sets `PATH=$CAP_CHILD_PATH` (`tools/research-gate.sh` r41 block before `SELF`, capture spawn at the env line).
- Counters + controls + receipts under `corpus/evidence/round41/` and `.ufo/waves/round-41/controls/`; dispositions `w04-dispositions.tsv`.
- Sources: S075 (`mktemp(1)` man) and S076 (`sed(1)`+`sed.info` `s` node) opened from installed copies only — zero egress; knowledge `corpus/knowledge/capture-path-pin-r41.md`; QUALITY criteria 57–58; lesson `corpus/lessons/round-41.md` with 4 Mistakes rows + r40-wave dispositions.
- Selftest repair: `metadata-stat-unavailable` now simulates through `RESEARCH_GATE_STAT` (the pin made its PATH shim unreachable); PASS 275/275 after.
- Prepared (not dispatched) a 35-seat v1 wave: `.ufo/waves/round-41/{w1-spec.json,w1-plan.json,w1-dispatch.json}`, validator `plan`/`run` exit 0, fetch-hardened seat contract.

## Landed changes (each tied to LOG.md round-41 entry)

- `b173b0943e647f7e3a365689df19debe40fd9dd2` — freeze: claims.md, c1-count.py, c2-count.py, control gate copy, before-measurements.
- `1bd9001330f19d89ec36592010d4218881ea5941` — gate change, after-receipts, dispositions TSV, knowledge, SOURCES rows S075/S076 + search-log entry, QUALITY 57–58, lesson, README index, LOG.md, wave spec/plan/dispatch/DISPATCH-README.
- `a3aac04492a3a5e99e351fc9941fcba801c152fe` — SCORECARD measured-claims section, routed dispositions, planned r42.

Inherited/uncommitted state: the orchestrator's running round-40 wave has written ~28 seat reports + registry updates under `.ufo/waves/round-40/w1/`; left uncommitted and unaltered (not lane-authored this round; the orchestrator's wave is still settling).

## Before → after measurements

- C1: `python3 corpus/evidence/round41/c1-count.py --gate .ufo/waves/round-41/controls/base-gate-r41.sh` → `CAPTURE_PIN_MATCH=1/12` exit 1 (`.ufo/waves/round-41/controls/control-before.txt`) → `--gate tools/research-gate.sh` → `CAPTURE_PIN_MATCH=12/12` exit 0 (`corpus/evidence/round41/measure-after-c1.txt`), measured at `1bd90013…`; re-verified at tip `a3aac044…` (12/12).
- C2: `python3 corpus/evidence/round41/c2-count.py` with TSV absent → `W04_DISPOSITIONED=0/5` exit 1 (`controls/c2-control-before.txt`) → with `w04-dispositions.tsv` → `5/5` exit 0 (`measure-after-c2.txt`), at `a3aac044…`.
- No-harm: `bash tools/research-gate.sh --selftest` → `PASS (275 cases, 0 skipped)` on landed bytes.

## Sources & frontier

`SOURCES.md` rows 74 → 76 (`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`); tier A 68 → 70, B 1 → 1, C 5 → 5; status mined 50 → 52, queued 19 → 19, rejected 5 → 5; duplicate ids none; enum violations none; mined used-by paths resolve. Rows added by tier: A +2 (S075 `mktemp(1)` installed man, S076 `sed(1)`+`sed.info` installed copies — canonical URLs recorded from roff links, not fetched). Rows touched old→new: none beyond the two additions (no status/recheck/used-by edits). Frontier rows advanced: invocation-pinning subground (PROVINCE-adjacent craft ground; `capture-path-pin-r41.md` cites S075/S076/S067). Search log: one bounded entry (installed-only sweep, open-L0 clause restored — r40-wave F3 remediation). Census exit 0 before and after: `…/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin chousa` → W04 ×4 before, W04 ×5 after (S075 legitimately re-cites the coreutils page at a different anchor; all five dispositioned under C2 — advisory warnings, semantically correct).

## Trend verdicts

- **expansion: improved** — one admitted knowledge entry on unheld subground (capture-invocation pinning) citing mined S075/S076 opened this round.
- **quality: improved** — the capture's invocation surface fails closed on PATH/loader-env interposition (do-nothing control 1/12 → 12/12); selftest 275/275; the only regression was repaired through the documented override channel.
- **discernment: unchanged** — gate decisions (2 admits, 1 fetch rejection) await a non-author spot-check; no lane-dispatched seat counts as independent review.

## Round-40 wave findings — routed dispositions

- SentinelFetchScope F1/F2/F3 (unapproved egress ordered by a seat item; attested-not-evidenced access claim; disclosure regression): confirmed, recorded in `corpus/lessons/round-41.md` + QUALITY 57; the r41 wave contract bans egress and binds all source items to installed files; fleet-report bytes are integrator/operator-owned (not edited lane-side). **Not a committed-tree falsification of round 40.**
- ReviewActivePopulation/ReviewReplacementBindings/ReviewC2Bindings (worktree-vs-commit counter mismatch, 6/6 vs 2/6): confirmed as a measurement-target defect in the r40 counter lineage → QUALITY 58; routed to the counter's next owner; r41 counters pin `--gate`/TSV paths explicitly.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SKILL.md` Gates table; `corpus/knowledge/capture-path-pin-r41.md` (lane assertion; no non-author verifier)
- [~] At least one end-to-end domain task executed and logged in LOG.md — LOG.md round-41 entry; `corpus/evidence/round41/receipts/cells/cells.json` (lane assertion)
- [~] Instructions executable by an agent without oral context — `bash tools/research-gate.sh --selftest` PASS 275/275; `corpus/evidence/round41/{c1,c2}-count.py` run standalone (lane assertion)
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `PROVINCE.md`; pinning work stays inside "this lane's own gates" (lane assertion)

## Round shape / L2

v1 single-wave shape: wave 1 **prepared + validated** (35 seats: executor 6, critic 7, reviewer 6, scout 3, scribe 3, mutation-tester 3, sentinel 3, revenger 2, connector 1, simplifier 1; planner seat held by L1 per validator rule). **0 dispatched, 0 returned, 0 dead** — this seat has no task/AgentSwarm dispatch surface (host surface note); the orchestrator dispatches prepared waves (round-40's identically-prepared wave was dispatched by the orchestrator and is settling now). No wave 2 (requires wave-1 attack items); no residual task call for the same reason. Round total seats dispatched by this seat: 0; prepared wave seats: 35.

Stale-lane: none of this lane's other missions are open (respawn-per-round driver); round-40's orchestrator-dispatched wave is in-flight under `.ufo/waves/round-40/w1/` — progressing (seat reports landing), not silent.

Misroot sweep: `git -C /home/vgpnk/Projects/shokunin status --porcelain` — no seat files landed at fleet root attributable to chousa (`.ufo/state/*` driver files and other lanes' reports untouched; nothing deleted).

Tool installs: none. Host route table read; no model aliases pinned or changed. Pacman paused host-wide; no pacman transaction attempted. No external fetches performed (loopback/installed sources only).

Open L0 questions: fetch-scope `8d77e6c1` remains unanswered (round-41 additions all loopback); one new line appended this round asking whether a wave dispatch item may ever constitute egress approval pending that ruling.

## Erratum (post-filed, supersedes the wording of "worktree-vs-commit" above, 2026-10-24)

The routed defect paragraph above predates the sentinel's committed-tip addendum and is corrected for scope precision: after the r41 gate commit `1bd9001…` landed, the r40 counter at the **current committed tip** (`a3aac044…`, gate sha `2cb04bdd…`) returns `R39_ACTIVE_RECEIPTS=2/6` exit 1 with four `gate-sha256-mismatch` refusals; it returns 6/6 only at the **pinned revision** `6bc90e0` with gate sha `4253c187…`. This is expected receipt-sha binding, not a regression of the frozen r40 predicate and not a fresh worktree-only mismatch — the r40 claim is revision-scoped and replays 6/6 at its pinned bytes. Reissue/pinning-scope design is routed to round 42 (lane tip `d720b1de…`, `corpus/lessons/round-41.md` post-landing addendum). No r40 bytes and no gate bytes were rewritten or reset.
