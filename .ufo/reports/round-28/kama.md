# kama — round 28 report (attempt 1, L1 KamaR28)

Lane repo `/home/vgpnk/Projects/shokunin/kama-shokunin`, base `4179301f`, lane
tip `bdb2a5b4e41010659661342b42c79c34cbf9e43c` (pushed; `jj-lane.sh state`:
`local=remote=bdb2a5b4… ahead=0 behind=0 tracked=0 untracked=0`). No earlier
attempt of round 28 exists (`.ufo/watchdog.log` holds only the round-28 launch
line). Nothing was inherited.

## Work performed

Declared claim (one; frozen in `.ufo/waves/round-28/preregistration.json` at
`d8bf1804` before any control or data seat, amended A1 at `75b78bb4`):

- **C1 (measured, axis depth)**: SKILL.md gains `## Round-28 request-field
  outcomes`. It is a decision table of what llama-server b11755 does with one
  out-of-range or transformed value of a request field declared in
  `tools/server/server-schema.cpp` @704366d76. The server either rejects with
  HTTP 400 and the field's hard bounds, or stores a different value in
  `generation_settings`. The data is 34 registered rows (F28-01..F28-34),
  `registry/request-field-outcomes-r28.json` and SOURCES S140-S173. Target:
  `counted >= 18`. It is the round's sourced claim.

Work items:

- **Feasibility and surface choice (L1)**:
  - A scan of request-error literals new to the lane found 55 candidates, of
    which 2-3 can be reached over HTTP (scratch only). Rounds 26-27 had no
    producible data on that ground.
  - The request-field schema was absent from the lane: zero lane-document hits
    (`.ufo/waves/round-28/w1/out/ScoutProvince/grep-hits.txt`).
- **Freeze `d8bf1804`**:
  - counter `.ufo/waves/round-28/count-c1.py` (A0 sha256 `e6a706bb…0540c`);
  - pinned snapshot `server-schema.cpp` (sha256 `1f9d7b73…4050`, equal to the
    GitHub raw fetch);
  - base receipt `before/c1-base.out` (counted 0);
  - pilot `before/pilot-receipt.json`: 2 scratch rows counted 2. Their fields
    are excluded from the data.
- **Pre-freeze control call (10 seats, `5ebe7b1b`, `controls/HOLDS.md`)**:
  - Evidential results: do-nothing 0, junk 0/30, label-keyed 12/41,
    source-blind 14/38, duplicate-field 0/26.
  - Five holds (see Round shape).
  - No control met 18, so the counter was not changed.
- **Wave 1 (32 seats)**:
  - 17 data seats measured every declared field live on their own ports
    48201-48217. They returned 34 row drafts plus no-row evidence.
  - Repairs, recon and first falsifiers (outputs listed below).
- **Amendment A1 (`75b78bb4`)**:
  - Data seats returned rows whose stored value is only a generic type
    conversion (float32 saturation, uint32 wrap, truncation).
  - A1 makes clause (e) refuse those rows (`e:generic-conversion`); nothing
    else changed.
  - Timing (corrected by wave-2 critic CriticA1Legitimacy): A1 was written
    after data seat DataG01 had checked its drafts with A0 counter functions
    at 08:35:54Z. It was written before any data row was committed. See Gate
    and Trend verdicts.
- **A1 control call (3 seats, `fb10d9da`, `controls-A1/`)**:
  - A type-only conversion policy counts **20/52 under A0 (meets the target)**
    and 0/52 under A1.
  - The pre-freeze fixtures re-scored under A1 reach at most 9.
  - A fixed policy built from the README and field names reaches 11/38.
- **Data landed (`e49b4cf7`)**, then measured from a fresh clone of the remote
  (see Before → after).
- **Wave 2 (32 seats, falsify)**:
  - 17 RowReview seats each re-measured 2 rows live. All 34 outcomes
    reproduced, and every SOURCES URL and quote was re-opened.
  - Prose defects in 16 meaning cells and 3 intro sentences were found and
    corrected (`9ce5bd37`, `c23ebaa4`). The counted cells are byte-unchanged
    (ResProseCorrections).
- **Repairs: round-27 spot-check routed defects 1-7**
  (`corpus/lessons/round-28.md` §Repairs):
  - 1: `.ufo/waves/round-25/count-c2.py` now recomputes every cell from the
    sha256-bound raw bytes.
    - Forged cells now give `observed 11 bound False` (before the fix:
      `observed 14 bound True`).
    - The committed receipt still gives `registered 14 observed 14 bound
      True`.
    - ExecCountC2Fix built the fix; ReviewCountC2Fix confirmed it holds.
    - Disclosed limit: a coordinated forgery of cell, raw body and hash still
      passes.
  - 2, 4 and 5: `corpus/QUALITY.md` `## Round 28 qualification -- KQ37`
    (append-only; ReviewQualityAppend: holds).
  - 3: SKILL.md `## Round-28 instrument registry` retires the round-27 counter
    and registers this round's counter, the repaired count-c2,
    `tools/gate-registry-check.py` and `tools/echo-recheck.py`.
  - 5 and 6: `corpus/knowledge/echo-discriminating-counters.md` now states the
    boundary scope and a runnable recheck line. `tools/echo-recheck.py` gave
    `same 6/6` twice and refused an existing path with exit 2 (ExecEchoRecheck,
    ReviewEchoRecheck).
  - 7: corrected below.
- **Frontier step**:
  - Census before and after: exit 0 both times.
  - 34 SOURCES rows added.
  - Mined mistakes: lesson §Mistakes, 5 rows, each with a committed fix
    receipt.
  - Sourced claim: C1 cites S140-S173.
- **Round-27 report corrections (routed defect 7)**:
  - The round-27 residual call spawned at **07:23:39Z**
    (`.ufo/waves/round-27/residual/spawn-result.txt`), not about 07:27Z.
  - `8057282c` also added `census-final.out` and
    `sources-append-only-final.out`
    (`.ufo/waves/round-28/final/r27-8057282c-stat.out`).
- **Misroot sweep**: `git -C /home/vgpnk/Projects/shokunin status --porcelain`
  shows no file written by a kama seat. The untracked root files predate the
  round and hold no kama content.

## Landed changes

| commit (`landed` line) | LOG.md entry | content |
|---|---|---|
| `d8bf1804ce52c30343f3e41cbae41c9640db9a64` | "Round 28 — request-field outcomes" | C1 freeze: counter A0, preregistration, base and pilot receipts, snapshot |
| `5ebe7b1b2defa4d8109de8fcc9b28f13dd6fb5f6` | same | pre-freeze control receipts, HOLDS.md |
| `75b78bb4900aae1edcdb6b229bb8c572c20fcbce` | same ("Evidence that motivated A1") | amendment A1: counter, preregistration, A1 pilot receipts |
| `fb10d9dab3565470a4a8c52f9e1e118950b7ccac` | same | A1 control receipts |
| `e49b4cf77046024551ba83d490ef83d9dee061ed` | same | C1 data (SKILL section, registry, S140-S173), wave-1 evidence, repairs 1-6, tools, instrument registry, lesson draft |
| `9ce5bd377562117b3340709639d5d0eafe791bc1` | same ("Wave 2 (falsify, 32 seats)") | wave-2 evidence, meaning-cell corrections, SCORECARD/LOG/README/PROVINCE round-28 sections, final receipts, lesson |
| `c23ebaa4883a9960ffbff8f20e6130fae8e22036` | "Round-28 source-digest correction", "Round-28 count corrections" | residual review evidence; prose, digest and LOG count corrections; final census |
| `bdb2a5b4e41010659661342b42c79c34cbf9e43c` | same | final C1 receipt at `c23ebaa4` |

## Before → after measurements

- **C1**:
  - Command: `/usr/bin/python3 .ufo/waves/round-28/count-c1.py --out
    <receipt.json>`, run from a fresh clone of the lane remote. Counter sha256
    `a38faefeeb48be9fd3590b5077030ed6b7cef08dcaf1ca0540b464bd222749a5` (A1).
  - Before, base `4179301f` (`before/c1-base.out`): `registered 0 counted 0
    target 18 met False not-counted []`.
  - After, measured at `c23ebaa4` (`final/c1-c23ebaa4.out`, exit 0):
    `registered 34 counted 26 target 18 met True`. The 8 rows not counted
    (F28-11, 14, 16, 17, 21, 22, 25, 26) are all `e:generic-conversion`.
  - The same result holds at `e49b4cf7` and `9ce5bd37`. Wave-2 seat
    RecountFreshClone reproduced it independently.
  - The A0 counter (frozen before data, sha256 `e6a706bb…0540c`) on the same
    trees gives `registered 34 counted 34 target 18 met True`
    (`final/c1-A0-9ce5bd37.out`).
  - Unmoved command: the same counter at base prints counted 0.
- **Self-assessment check (calibration)**: non-author seat ResSelfAssessment
  found **3 mismatches in 46 checkable statements**.
  - Two are LOG counts. They are corrected by an appended entry in
    `c23ebaa4`.
  - One is an inherited round-17 SHONEN wording, left open.

## Gate

Real rejects, with reasons (full table in `corpus/lessons/round-28.md` §Gate):

- **ReviewerCounterCode: amend the counter a third time (exact-cell match,
  duplicate-id rule, int64 tolerance). Rejected.**
  - A1 is declared the last amendment.
  - The landed rows use exact cells and unique ids (RecountFreshClone), so
    these are recorded limits.
- **DataG03/05/07/08 drafts: count the float32-saturation rows and seed/n_probs
  as field knowledge. Rejected.** They are generic conversions of the value
  sent. They stay in the table and are not counted.
- **DataG12: add json_schema → grammar as a row. Rejected.** The stored GBNF
  contains `|`, which the frozen table cannot hold. This is disclosed.
- **ExecShortcutPostData: its 20/20 from declared limits shows C1 met by a
  shortcut. Rejected as a source-blind control.**
  - It reads each field's declared bounds, which is the source half of the
    claimed work.
  - It is kept as a counter limit: the writer need not run the server, and
    clause (c) checks SOURCES text without a fetch.
- **ScribeSkillRegistryRows: keep "withdrawn before data" as the round-27
  disposition. Rejected.** The round-27 closure ruled C1 a miss.

Admitted:

- CriticA1Legitimacy's timing correction.
- 16 meaning-cell corrections plus intro/no-row sentences.
- The gate-registry check's occurrence-only limit.
- The instrument-registry scope fixes.
- The missing mistake-receipt fixes.

## Sources & frontier

Count command: `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`.

| Measurement | Before | After |
|---|---|---|
| SOURCES rows | 139 at `4179301f` | 173 at the tip |
| Rows added by tier | — | A: 34 (S140-S173, code, llama.cpp server-schema.cpp @704366d76, one row per declaring line); B: 0; C: 0 |

- **Rows touched old→new**: none. There was no status, recheck or used-by
  change, and no row was superseded.
- **Opening**: each new row was opened this round by the data seat named in
  the lesson Gate. Each seat's own curl hashed `1f9d7b73…4050`, equal to the
  pin; wave-2 seats re-fetched every row's URL. Quotes are mechanically
  verbatim (`final/quote-check.out`: gate quotes 34, not-verbatim 0).
- **Census before**: `scripts/sources-census.sh validate --root
  /home/vgpnk/Projects/shokunin kama` → exit 0, `kama ok`
  (`.ufo/waves/round-28/before/census-start.out`).
- **Census after**: the same command → exit 0, `kama ok`, W04 duplicate-URL
  advisories only (`final/census-final.out`).
- **Append-only**: `tools/sources-append-only.py --from 4179301f --to 9ce5bd37`
  → "no append-only violations" (`final/sources-append-only-final.out`).
- **Frontier advanced**: the request-field schema moved from absent to core.
  - Evidence: README `## Frontier disposition — round 28` and the PROVINCE.md
    round-28 core note.
  - Still open: other endpoints, json_schema → grammar, launch-dependent
    bounds under other argv, other builds and engines.

## Trend verdicts

- **expansion: improved.**
  - New ground: a surface absent from PROVINCE.md and from every frontier
    list now has 26 counted, live-verified, sourced field outcomes. They fall
    into three mechanism families: 13 hard-bound rejects, 7 silent clamps and
    6 handler transforms (CriticDepthAxisPostData).
  - 34 new tier-A sources.
- **quality: unchanged (author reading).** The claim is a depth move, but the
  author does not promote it:
  - Under the rule frozen before data (A0), a type-only control also meets the
    counter (20/52).
  - A1, which refuses that control, was written after a data seat had checked
    drafts with A0 counter functions.
  - Per the round prompt (§6 item 9), "a rule changed after any seat has
    scored is not the claim's rule".
  - Depth is held at 7 in SCORECARD; the non-author closure rules.
  - The repairs (count-c2 binding, KQ37 text, the runnable recheck) fix
    defects and are not counted as a gain.
- **discernment: improved.**
  - Wave seats found the counter's generic-conversion blind spot before the
    data landed.
  - The lane disclosed it with both rule results instead of choosing the
    favourable one.
  - Wave-2 reviewers caught 16 over-general meaning cells, and each was
    corrected with evidence.
  - The round-27 routed defects became one QUALITY qualification, two tools
    and one registry block.

## Round shape, seats and holds

- **Shape**: two v1 waves, plus three ordinary calls: the pre-freeze control
  call (Main's control-wave correction), an A1 control call and one residual
  call.
  - **Pre-freeze control call**: 10 seats (executor 6, mutation-tester 4).
    Gate `kama-r28-ctl` granted 10 at 08:14:33Z.
  - **Wave 1** (`w1/spec.json`): validated under `ufo-wave-policy.json`
    (validator exit 0), 32 seats (executor 21, scribe 4, reviewer 3, scout 2,
    connector 1, critic 1).
    - Gate granted 08:30:28Z.
    - The first send was refused for all 32 with `Background job limit reached
      (100). Wait for running jobs to finish or cancel one.`
    - The unchanged seats were resent in chunks of 12/12/8, which spawned at
      08:31:50Z, 08:32:50Z and 08:33:50Z (`w1/spawn-result.txt`; the
      harness suffixed names `-2`).
  - **A1 control call**: 3 executor seats, gate granted 08:39:44Z.
  - **Wave 2** (`w2/spec.json`): validated v1, 32 seats (reviewer 28, critic 2,
    executor 1, scout 1). One send at 08:57:46Z, no refusal.
  - **Residual call**: 4 seats (reviewer 3, critic 1), 09:18Z.
- **Total**: 81 seats (≤128).
- **§3 floor** (inside wave 1):
  - planner: the L1 (the validator rejects `planner`; the planning data walk
    was the L1's feasibility scan);
  - connector: ConnectorSiblings (no contested scope);
  - executors (21), scribes (4), scouts (2), reviewers and critic.
- **Routing**: per Main 08:2xZ, every control seat that builds and runs code
  after the first call went to executor; critics were read-only.
- **Dead seats**: none.
- **Holds** (never re-sent, findings not used as evidence):
  - CtlNoReader: `Codex error event: This content was flagged for possible
    cybersecurity risk ... (code=cyber_policy)`.
  - CtlObjectStore and CtlAllFalse: `Refusal (cyber): This request triggered
    restrictions on violative cyber content and was blocked under Anthropic's
    Usage Policy.`
  - CtlEcho and CtlSourceMisuse: their output ended with an automatic model
    switch after a safety filter (`Claude Opus 5.5 hit a safety filter ...
    switched to Claude Opus 4.8`).
  - Classes left without an evidential receipt: no-reader, object-store,
    all-false, echo, source-misuse.
- **Settle**: every seat returned before its deadline; none was cancelled.
  Seat gates were released after each call settled.
- **Port note**: RowReview02's assigned port 48302 was held by harness
  infrastructure (`node proxy-tmp.cjs`). It used 48303 after RowReview03 had
  finished and disclosed the substitution.

## Open items at report time

- **C1 disposition**: met under both A0 (34/34) and A1 (26/34). It carries a
  disclosed freeze breach (A1 after a seat scored data), and a type-only
  shortcut meets A0. Final ruling belongs to the non-author closure.
- **Counter limits recorded, not repaired**:
  - substring cell match;
  - no duplicate-id rule;
  - pilot exclusion not enforced in code;
  - clause (c) is text-only;
  - the meaning cell is checked only for word count.
- **SHONEN.md box 2**: an inherited round-17 wording mismatch
  (ResSelfAssessment). Open.
- **L0 questions**: none.
- **Tool installs**: none by the L1. No seat reported an install.
- **Stale-lane**: respawn-per-round driver; no other mission of this lane is
  open.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited
  sources → `SKILL.md` `## Round-28 request-field outcomes` (34 rows, S140-S173).
  Wave-2 RowReview seats re-measured every row, but that is evidence, not a
  promotion mark; no `[x]`.
- [~] At least one end-to-end domain task executed and logged in LOG.md →
  `LOG.md` §round 16/17; this round's live measurements are under
  `.ufo/waves/round-28/w1/out/DataG*/` and `final/`. ResSelfAssessment flags
  the box's round-17 wording (open).
- [~] Instructions executable by an agent without oral context → `SKILL.md`
  §Checklist; `tools/echo-recheck.py` and `tools/gate-registry-check.py` added
  with registry rows; no non-author mark.
- [~] No cross-domain bleed (PROVINCE.md still accurate) → `PROVINCE.md`
  round-28 core note; ConnectorSiblings found no contested scope.
