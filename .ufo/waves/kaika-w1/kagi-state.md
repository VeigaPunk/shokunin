# kagi STATE dossier — kaika W1

2026-10-19 · lane `kagi` (secrets & vault ops) · repo `/home/vgpnk/Projects/shokunin/kagi-shokunin` · read-only.

## Method and limits

- This is the STATE probe: no web research was required, so **no external source row is claimed here** (that is the ART lanes' deliverable).
- **No repo gate was executed.** The wave is read-only and several gates read `op.env` / `opencode.db` session text. Every verdict string quoted below is copied from a committed record or a tracked `.ufo/round-20/*.json`, and is labelled as inherited measurement, not re-run.
- No secret value, session token, account identity or `op://` ref appears in this artifact; no private file was read. Host contact was limited to existence/version probes (`test -e`, `command -v`, `op --version`).
- Host drift since the lane's last measurement: `op --version` → **2.41.0** today; `.ufo/round-20/inspection.json` records `"opVersion": "2.40.0"`. The byte-contract evidence below is one minor version stale.
- Counts are static-file counts; commands are relative to the lane repo unless prefixed with `../` (fleet root).

## 1. Identity

| Field | Value | Evidence / command |
|---|---|---|
| Domain | secrets & vault ops — the-janitor flows, credential-hygiene evidence | `MANIFEST.json` roster row `id=kagi`; `PROVINCE.md:3` |
| Rank | shonen (minted 2026-09-28) | fleet `MANIFEST.json` roster `kagi` — `python3 -c "import json;print([r for r in json.load(open('../MANIFEST.json'))['roster'] if r['id']=='kagi'])"` |
| Branch / HEAD | `master` / `aea7a43` (2026-10-17) | `git branch --show-current`; `git log -1 --format='%h %ad' --date=short` |
| Working tree | clean | `git status --porcelain \| wc -l` → **0** |
| Max round label in lane | **20** | `ls corpus/lessons \| grep -oE '^round-[0-9]+' \| grep -oE '[0-9]+' \| sort -n \| tail -1` → `20` |
| Round 20 status | **blocked attempt, not a completed round**; verified-round increment 0 | `corpus/lessons/round-20.md` §Gate/§Results; `SCORECARD.md:554` §Round 20; `LOG.md:847` |
| Last admitted axis move | **freshness 8 → 9**, dated "round-16 re-dispatch", commit `f4a8dd9` | `SCORECARD.md:508` §Outcome; `LOG.md` §19 bullet dated 2026-10-15 |
| Round 19 | re-census: gates re-ran green, verdicts recorded, **no scalar move** | `corpus/lessons/round-19-recensus.md`; `SCORECARD.md:451` Move log row 19 |
| Fleet ledger max for kagi | **19** lane-rounds; **0** round-20 kagi rows | `python3 -c "import json;m=json.load(open('../MANIFEST.json'));print(max(r['lane_rounds']['kagi'] for r in m['rounds'] if isinstance(r.get('lane_rounds'),dict) and 'kagi' in r['lane_rounds']), sum(1 for r in m['rounds'] if r.get('round')==20 and 'kagi' in json.dumps(r)))"` → `19 0` |
| Next round number | **21** (= max label 20 + 1) — ambiguous, see D6/D11 | derivation above; no `round-21` artifact exists: `ls corpus/lessons \| grep -c '^round-21'` → 0 |

Round-number history has two non-monotonic events, both preserved: a second, explicitly dated **round-16 re-dispatch** was run after rounds 17–19 existed (`SCORECARD.md:468`), and the driver's launch counter 16 was reused while the lane already held rounds 17–19 (`corpus/lessons/round-20.md` §What was actually inherited). Neither is a new round id in the lane's craft history.

## 2. Axes

Scores are author-assigned with pointers (the lane's own ceiling statement). Source table: `sed -n '468,520p' SCORECARD.md` (baseline) plus `SCORECARD.md:554` §Round 20 (before→after verdicts).

| Axis | Score | Evidence pointer | Last change |
|---|---|---|---|
| **depth** | **8** | `corpus/knowledge/op-ref-consumption.md`; ref-resolved masking / `op read` / `op inject` deliberately refused | round 12 |
| coverage | 9 | `corpus/knowledge/adjacency-breadth.md`; 4 count-only breadth pins (live values are substrate debt) | round 17 |
| operability | 9 | `corpus/knowledge/checklist-execution.md`; 16-row executed checklist, no scheduling | round 15 |
| freshness | 9 | four-entry historical-source erratum at `corpus/knowledge/config-layering.md:111-136`, `handler-on-disk-state.md:250-278`, `handler-trust-boundary.md:288-317`, `janitor-env-contract.md:92-113` | round-16 re-dispatch |
| calibration | 9 | `corpus/knowledge/claim-ledger.md`; ledger `cells` audit green at last run | round 13 |
| adjacency | 9 | `corpus/knowledge/adjacency-scope.md`; ownership partition gate | round 16 |

- **Lowest non-retired axis: depth = 8**, sole lowest; every other axis is 9. This is the axis the next round must work (`AXES.md:33-34`).
- **Retired: none** — `sed -n '438,446p' SCORECARD.md` ("None. No axis is saturated…").
- **Saturation line + stagnation window N: undeclared.** `SCORECARD.md:619` says they are "to be declared by the lane on its next round … not asserted by this conformance change." The nudge cannot fire.
- **Capabilities: 0 rows.** `awk '/^## Capabilities/,/^## Saturation/' SCORECARD.md | grep -c '^| '` → **2** (header + "— none yet —" placeholder).
- Score cells are self-scored; the ledger checks pointers, not score relevance (`corpus/knowledge/claim-ledger.md` §Bounds; `SCORECARD.md:508`).

**Planned claims carried in `SCORECARD.md`** (`grep -c '^## Planned' SCORECARD.md` → **6**):

| Block | Line | Target | Status |
|---|---|---|---|
| next axis-move — round 17 close | 345 | depth: one vault-free `op.env` behavior not yet in `op-ref-consumption.md`, or record the unchanged ceiling | standing; round 20 proposed a different vault-free depth behavior (byte fidelity) and blocked before admission |
| next axis-move — round 16 close | 244 | depth byte frontier + coverage breadth | coverage half landed (round 17); depth half standing |
| next axis-move — round 15 close | 371 | checklist `--mutate` negative-fixture mode (`MUTATION: caught=K/K`) | open, unclaimed |
| next axis-move (round 13 close) | 122 | push `by_hand` 3 → ≤1 and move `DOC_AUDIT_RATIO` | open; `by_hand=3` still pinned by `R14-01` |
| round-15 target recorded — not taken | 360 | records why the round-14 target was skipped | history |
| falsified in round 14 | 402 | `row_pointed ≥ half` | measured and falsified; kept as record |

## 3. Corpus

### Counts

| Quantity | Count | Command |
|---|---|---|
| knowledge entries | **21** | `ls corpus/knowledge/*.md \| wc -l` |
| lesson files | **27** | `ls corpus/lessons/*.md \| wc -l` |
| knowledge lines | **3783** | `cat corpus/knowledge/*.md \| wc -l` |
| lesson lines | **2645** | `cat corpus/lessons/*.md \| wc -l` |
| coverage-map rows | **57** | `awk 'NR>=19 && NR<=76 && /^\| /' corpus/README.md \| wc -l` |
| overlap-table rows | **3** | `awk 'NR>=84 && NR<=88 && /^\| /' corpus/README.md \| wc -l` |
| claim-ledger rows | **35** | `grep -cE '^R[0-9]+-[0-9]+' corpus/claim-ledger.tsv` |
| revision stamps | **56** | `grep -cE '^[^#]' corpus/stamps.tsv` |
| `QUALITY.md` criteria | **undefined — file absent** | `test -e corpus/QUALITY.md; echo $?` → **1** |

### Frontmatter conformance (CORPUS.md:17-18)

| Required field | Entries conformant | Command |
|---|---|---|
| `source:` (lowercase) | **0 / 21** | `grep -l '^source:' corpus/knowledge/*.md \| wc -l` |
| `Source:` (capitalised variant) | 7 / 21 | `grep -l '^Source:' corpus/knowledge/*.md \| wc -l` |
| `Source basis:` / `Sources:` | 13 / 21 and 1 / 21 | `grep -l '^Source basis:' corpus/knowledge/*.md \| wc -l`; `grep -l '^Sources:' corpus/knowledge/*.md \| wc -l` |
| `verified-at:` | **0 / 21** | `grep -l '^verified-at:' corpus/knowledge/*.md \| wc -l` |
| `recheck:` | **0 / 21** | `grep -l '^recheck:' corpus/knowledge/*.md \| wc -l` |
| lane's own `Reverify:` link | 21 / 21 | `grep -l '^Reverify:' corpus/knowledge/*.md \| wc -l` |
| lessons with `## Gate` | **2 / 27** (`round-20.md`, `round-8-aggregator-box3-coldrun.md`) | `for f in corpus/lessons/*.md; do grep -q '^## Gate' "$f" && echo "$f"; done \| wc -l` |
| lessons with source/verified-at/recheck | 1 / 27 (`round-20.md` only) | `grep -l '^recheck:' corpus/lessons/*.md \| wc -l` |

The gate does not close this gap: `grep -c 'Reverify' corpus/claim-ledger.sh` → 36, but `grep -c 'recheck' corpus/claim-ledger.sh` → **0**, `grep -c 'verified-at' corpus/claim-ledger.sh` → **0**.

### Overdue recheck

Undefined rather than zero: with `recheck:` in 0/21 entries there is no cadence to compare against 2026-10-19. Age signal instead: 18/21 entries cite `2026-09-28` as their source-read date (`grep -l '2026-09-28' corpus/knowledge/*.md | wc -l` → 18); 5/21 cite a 2026-10 date (`grep -l '2026-10' corpus/knowledge/*.md | wc -l` → 5). So the corpus carries no re-verification clock at all, while the oldest facts are 21 days old and substrate-dependent.

### Index drift (`corpus/README.md`)

| Defect | Count | Command |
|---|---|---|
| lessons on disk but not indexed | **3** — `round-19-recensus.md`, `round-6-aggregator-audit.md`, `round-9-aggregator-corpus-verdict.md` | `for f in corpus/lessons/*.md; do b=$(basename "$f"); grep -qF "lessons/$b" corpus/README.md \|\| echo "$b"; done` |
| knowledge entries on disk but not indexed | **1** — `adjacency-scope.md` | same loop over `corpus/knowledge/*.md` |
| `## Frontier` section | **0** | `grep -c '^## Frontier' corpus/README.md` |
| `## Known gaps` section | **0** | `grep -c '^## Known gaps' corpus/README.md` |

`CORPUS.md:11` defines `README.md` as "index: what's here, coverage map, known gaps, frontier"; the lane's README has the coverage map and overlap table only.

### Skill size (bloat signal, not a verdict)

| Artifact | Size | Command |
|---|---|---|
| `SCORECARD.md` | 621 lines / 77 831 B | `wc -lc SCORECARD.md` |
| `LOG.md` | 963 lines / 68 885 B | `wc -lc LOG.md` |
| `SKILL.md` | 663 lines / 57 062 B | `wc -lc SKILL.md` |
| `corpus/claim-ledger.sh` | 79 301 B | `du -b corpus/claim-ledger.sh` |
| `corpus/scope-gate.sh` | 55 002 B | `du -b corpus/scope-gate.sh` |
| `corpus/op-ref-probe.sh` | 788 lines / 34 362 B | `wc -lc corpus/op-ref-probe.sh` |

`SKILL.md` holds **24** decision-table rows (`awk 'NR>=23 && NR<=47 && /^\| /' SKILL.md | wc -l`), **15** failure-table rows (`awk 'NR>=307 && NR<=327 && /^\| /' SKILL.md | wc -l`), **16** checklist items (`awk 'NR>=421 && NR<=458 && /^- \[ \]/' SKILL.md | wc -l`), **32** anti-pattern bullets (`awk 'NR>=474 && NR<=552 && /^- /' SKILL.md | wc -l`) and **12** falsification bullets (`awk 'NR>=553 && NR<=663 && /^- /' SKILL.md | wc -l`). Two adjacent count claims inside the same file are already stale (D8).

## 4. Mistakes mined

`QUALITY.md` is absent, so **no `QUALITY.md` criterion exists that could capture any mistake** (`test -e corpus/QUALITY.md` → exit 1). The `SKILL.md` anti-pattern sweep is the only in-repo rule surface; keyword counts over `SKILL.md:474-552` are `awk 'NR>=474 && NR<=552' SKILL.md | grep -ci '<kw>'`.

| # | Class | Evidence pointer | Captured by | Proposed criterion (none exists today) |
|---|---|---|---|---|
| M1 | **Overclaim** — an absent source's hash prefix asserted in current voice | `SCORECARD.md:454-466`: `config-layering.md:58` still states `af8873ca…` as current; three entry headers name missing-file prefixes | No. Anti-pattern sweep: `historical`=0, `hash`=1, `absent`=0 | "A property of an absent file appears only under an explicit historical marker; current-voice attribution fails the freshness gate." |
| M2 | **Wrong mechanism attribution** — `uniq -d` on empty input said to exit 1; actually exits 0 | `corpus/lessons/round-15.md:112` §Corrigendum; `SCORECARD.md:238` (round-16 calibration row) | No. Anti-pattern sweep: `uniq`=0 | "An exit-code claim carries the command and the host; a mechanism attribution is re-run before it is cited." |
| M3 | **Fail-open gate** — `SKIP` treated as clean; digest printed for custody; POLICY bypassed in the probe | `corpus/lessons/round-10.md:48` §"The L2 critic's blockers, and what happened to each" (CE3/CE5); round-12 sentinel cases; `SCORECARD.md:71` | No. Anti-pattern sweep: `SKIP`=0; `STALE`=3 only | "A SKIP/UNVERIFIED branch must fail or be counted in the verdict line; a gate that can exit 0 without measuring is a defect." |
| M4 | **False hermeticity** — census selftest claimed scratch-tree proof but executed the real handler; 2/16 cases failed on a substrate-absent host | `corpus/lessons/round-18.md` §"The defect worth fixing" item 1 | Partly: fixed in code (`skip-case … substrate-absent`), not written as a rule | "A selftest advertises only the isolation it proves; any case that touches the real substrate prints SKIP with the reason." |
| M5 | **Unclaimed landing** — 130 lines of probe + records committed with no round id, no claim row, stale stamp, stale selftest expectation | `git show --stat aea7a43` (+130 in `corpus/op-ref-probe.sh`); `corpus/stamps.tsv:45`; `corpus/claim-ledger.tsv:27` (R12-02 pins 29 cases; `.ufo/round-20/local-checks.json` records 36) | No. Anti-pattern sweep: `stamp`=0, `selftest`=0, `verify`=0 | "An artifact lands only with its stamp and claim row updated in the same commit; `verify` is run before the commit." |
| M6 | **Round-identity reuse** — a second round-16 execution and a reused driver counter 16 while rounds 17–19 existed | `SCORECARD.md:468-470`; `corpus/lessons/round-20.md` §"What was actually inherited"; fleet `.ufo/l0-questions.md` has 7 kagi lines (`grep -ci kagi ../.ufo/l0-questions.md` → 7) | No. Anti-pattern sweep: `route`=0 | "Round identity is `(lane, max_recorded+1)`; a reused counter is a dated re-execution, never a new round id." |
| M7 | **Placeholder never filled** — `<FILL ON STAMP>` in a committed lesson | `corpus/lessons/round-13.md:9`; named debt at `corpus/lessons/round-19-recensus.md:40` | No. Anti-pattern sweep: `placeholder`=0 | "A placeholder token in a durable artifact is a failing stamp; `<FILL …>` is allowed only in an uncommitted draft." |
| M8 | **Honest stop (not a defect)** — route admission refused; no dispatch, no receipt, no fabricated completion | `.ufo/round-20/route-admission.mjs`; `corpus/lessons/round-20.md` §Gate: `KAGI_ROUTE_ADMISSION: BLOCKED (roles=7 mismatched=7 …)`, exit 2 | No rule needed; it is evidence of taste — **kept, not corrected** | Preserve as the model for a blocked round; do not convert a blocked attempt into a verified round. |

Rejections kept as taste, from `corpus/lessons/round-20.md` §Gate: promote six PASS rows to "complete dotenv contract" (rejected: exceeds the measured path); dispatch the 32-scope wave on mid/fast/strong roles (rejected: not the operator contract); manufacture a receipt from run/session metadata (rejected: schema validity is not acceptance).

## 5. Contract defects

| # | Defect | Evidence / command | Owner / status |
|---|---|---|---|
| D1 | `corpus/QUALITY.md` absent — required by `CORPUS.md:12` and `LEARNING.md` | `test -e corpus/QUALITY.md; echo $?` → **1** | named process debt in `LOG.md:917`; unblocked only by an owner-written bar |
| D2 | Knowledge entries lack the mandated `source:` / `verified-at:` / `recheck:` trio | 0 / 21 each; see §3 table | lane |
| D3 | 25 / 27 lessons lack `## Gate` (`CORPUS.md:18`) | loop over `corpus/lessons/*.md` → 2 | lane; round-19's own lesson is one of the 25 |
| D4 | `corpus/README.md` has no `## Frontier` and no `## Known gaps` (`CORPUS.md:11`) | `grep -c '^## Frontier'` → 0; `grep -c '^## Known gaps'` → 0 | lane |
| D5 | Index drift: 3 lessons + 1 knowledge entry unindexed | §3 index-drift commands | lane |
| D6 | Fleet ledger has no kagi round-20 row; max `lane_rounds[kagi]` = 19 while the lane records round 20 (blocked) and a 2026-10-17 commit | fleet-ledger `python3 -c` in §1 → `19 0` | integrator ledger; report only |
| D7 | **Stale revision stamps at HEAD**: `LOG.md`, `SCORECARD.md`, `corpus/op-ref-probe.sh` | `grep -E '^(LOG\|SCORECARD)\.md' corpus/stamps.tsv; grep 'corpus/op-ref-probe.sh' corpus/stamps.tsv` → pinned `LOG.md 762 56847`, `SCORECARD.md 446 66069`, `corpus/op-ref-probe.sh 660 28660`; actual `wc -lc LOG.md SCORECARD.md corpus/op-ref-probe.sh` → `963 68885`, `621 77831`, `788 34362`; `sha256sum` of each differs from the pinned hash | lane; the append-only records are pinned at an old revision |
| D8 | Stale counts inside `SKILL.md` | `grep -n '54 stamps + 32 claims\|94 scratch cases' SKILL.md` → **46**, **241**; actual data: 56 stamps (`grep -cE '^[^#]' corpus/stamps.tsv`), 35 claims (`grep -cE '^R[0-9]+-[0-9]+' corpus/claim-ledger.tsv`), 97 selftest cases (pinned by R11-09) | named debt in `corpus/lessons/round-19-recensus.md` §Named debt |
| D9 | Saturation line + stagnation window undeclared; capabilities table empty | `SCORECARD.md:619-621`; capabilities row count → 2 (header + placeholder) | lane; next round per AXES.md |
| D10 | Ignored on-disk bloat: `.ufo/interactive-sessions/` 2.7 MB of raw session JSONL | `du -sh .ufo/interactive-sessions` → `2.7M`; `.gitignore` line 1 ignores it | lane housekeeping; not tracked, not a corpus artifact |
| D11 | Round-label non-monotonicity and a reused launch counter (M6) | `SCORECARD.md:468`; `corpus/lessons/round-20.md` | lane + fleet ledger (D6) |
| D12 | 11 live lowercase `~/projects` path spellings (deleted-path class) | `grep -rn '~/projects' --include='*.md' . \| grep -v Projects \| wc -l` → **11** | named debt in `corpus/lessons/round-19-recensus.md` |
| D13 | `<FILL ON STAMP>` survives in a durable lesson | `corpus/lessons/round-13.md:9` | named debt; never filled |
| D14 | R12-02 pins a superseded selftest count (29) while HEAD's probe emits 36 — `verify` cannot be green on this artifact | `awk -F'\t' '$1=="R12-02"{print $3}' corpus/claim-ledger.tsv`; `.ufo/round-20/local-checks.json` (`OP_REF_SELFTEST: PASS (36 cases)`, exit 0) | introduced by the 2026-10-17 landing (M5) |
| D15 | Committed probe change has no claim row / no lesson / no round id | `grep -c 'DOTENV_BYTES' corpus/claim-ledger.tsv` → **0** | same landing (M5) |

Substrate state (context, not a lane defect): `~/.local/bin/the-janitor`, `~/.config/the-janitor`, `~/.local/state/the-janitor`, `~/.local/bin/tac-check` are all ABSENT (`test -e <path>` → exit 1 for each). 11 claim rows are `substrate`-tagged and DEFER (`SCORECARD.md:329-344`). Live gates therefore print DRIFT/BROKEN/DEFECT by design; re-pinning to the empty host is refused.

## 6. Proposed round (next = 21)

Axis obligation: **depth (8) is the sole lowest non-retired axis**. The three claims below are causally separable and on distinct axes; C1 works the lowest axis. All commands are run from the lane root. None requires vault contact or the absent handler.

### C1 — depth 8 → 9: admit the already-landed dotenv byte-contract arm

The commit `aea7a43` landed a 130-line `--dotenv-bytes` arm and its observations **without** a claim row, without a re-stamp, and without updating R12-02. This claim converts an unclaimed landing into measured depth: it adds the byte-fidelity contract to the domain entry and holds the artifact to the lane's own ledger discipline.

| State | Observation | Command |
|---|---|---|
| before | no ledger row names the arm | `grep -c 'DOTENV_BYTES' corpus/claim-ledger.tsv` → **0** |
| before | stamp pins 660 lines; HEAD has 788 | `awk -F'\t' '$1=="corpus/op-ref-probe.sh"{print $3,$4}' corpus/stamps.tsv` → `660 28660`; `wc -lc corpus/op-ref-probe.sh` → `788 34362` |
| before | selftest row still pins 29 cases | `awk -F'\t' '$1=="R12-02"{print $3}' corpus/claim-ledger.tsv` → `^OP_REF_SELFTEST: PASS \(29 cases\)`; inherited measurement: `.ufo/round-20/local-checks.json` → `PASS (36 cases)` |
| after | two rows exist and hold | `grep -cE '^R21-0[12]' corpus/claim-ledger.tsv` → **2**; `R21-01` = `OP_DOTENV_BYTES: CLEAN (checks=6 failed=0)` exit 0, `R21-02` = `OP_REF_SELFTEST: PASS (36 cases)` exit 0 |
| after | stamp equals HEAD bytes | `test "$(awk -F'\t' '$1=="corpus/op-ref-probe.sh"{print $2}' corpus/stamps.tsv)" = "$(sha256sum corpus/op-ref-probe.sh \| cut -d' ' -f1)"; echo $?` → **0** |
| after | entry carries the six observation ids + the representation limit | `grep -c 'DOTENV_OBS' corpus/knowledge/op-ref-consumption.md` → target **6** |

Falsifiers / limits:
- **Re-measure on op 2.41.0 first.** The only executed evidence is op 2.40.0 (`.ufo/round-20/inspection.json`); pinning the inherited output as current would be the M1 overclaim in a new place.
- The six rows are generated plain-value fixtures under isolated HOME/XDG/env; they prove **representation fidelity**, not handler behavior, not masking of ref-resolved values, not any vault fact.
- The observed shell limit stands as a negative result: `value=$(printf "alpha\n\n")` emitted only hex `61 6c 70 68 61` (`local-checks.json` label `trailing-lf-shell-boundary`), i.e. command substitution drops trailing LFs.
- Capability row candidate: "op-only dotenv byte probe (6 classes, isolated env)" may enter `## Capabilities` **only** with this round's passing demonstration; row count target `2 → 3` under `awk '/^## Capabilities/,/^## Saturation/' SCORECARD.md | grep -c '^| '`.
- Serves `SOURCES.md`: wave 2 should open primary rows for (i) the 1Password CLI `op run --env-file` reference and (ii) the dotenv grammar the fixtures encode. Those are **unopened leads here**, not source rows — this dossier asserts nothing about their content.

### C2 — freshness 9 → 9 (mechanism): give every entry a re-verification clock

| State | Observation | Command |
|---|---|---|
| before | no `verified-at:` and no `recheck:` in any entry | `grep -l '^verified-at:' corpus/knowledge/*.md \| wc -l` → **0**; `grep -l '^recheck:' corpus/knowledge/*.md \| wc -l` → **0** |
| before | `source:` shape absent (7 entries use `Source:`) | `grep -l '^source:' corpus/knowledge/*.md \| wc -l` → **0** |
| before | the gate cannot see the missing fields | `grep -c 'recheck' corpus/claim-ledger.sh` → **0**; `grep -c 'verified-at' corpus/claim-ledger.sh` → **0** |
| after | 21 / 21 carry `source:`, `verified-at:` (2026-10-19+), a cadence (`90d` / `on-release` / `on-substrate-return`) | the three `grep -l` counts above → **21** each |
| after | `docs` mode fails on a missing field, proven by a selftest case | `bash corpus/claim-ledger.sh --selftest` → target `SELFTEST: PASS (≥98 cases)` (current pinned count 97, row `R11-09`); `docs` is run inside `verify` |

Limits: adding fields is a **shape** claim, not re-verification. Three sources remain absent, so most bodies cannot be re-checked; an entry whose cadence is `on-substrate-return` must say so in its text. Serves `SOURCES.md`: once entries cite S-rows, `recheck:` can inherit the row's cadence instead of a hand-written date.

### C3 — calibration 9 → 9: make the index and the scorecard contract complete

| State | Observation | Command |
|---|---|---|
| before | 3 lessons + 1 knowledge entry unindexed | §3 index-drift loop → `3` and `1` |
| before | no frontier / gaps section | `grep -c '^## Frontier' corpus/README.md` → **0**; `grep -c '^## Known gaps' corpus/README.md` → **0** |
| before | saturation undeclared | `sed -n '/^## Saturation/,$p' SCORECARD.md` → "to be declared … not asserted" |
| after | index complete; frontier + gaps present; saturation line + N declared | unindexed → **0** lessons and **0** knowledge; `grep -c '^## Frontier'` → **1**; `grep -c '^## Known gaps'` → **1**; `## Saturation` names a line and an N |

Limits: this is a documents-surface claim, not a path-coverage claim; it must not be booked under coverage (lane precedent: rounds 13/15/16 explicitly refused double-counting). If wave 2 lands the fleet-wide README/frontier template, C3 should be reduced to the saturation declaration + the index rows to avoid a duplicate convention.

### Rejected candidates (kept as taste)

1. Re-pin the drift/census baselines to the now-empty host — rejected: it falsifies the preserved record of what the substrate was (`corpus/lessons/round-18.md`; `SCORECARD.md:329`).
2. Promote the six byte observations to "complete dotenv contract" — rejected: exceeds the measured path (`corpus/lessons/round-20.md` §Gate).
3. Dispatch the rendered 32-scope wave on mid/fast/strong roles — rejected: violates the operator's route contract (`KAGI_ROUTE_ADMISSION: BLOCKED`, exit 2).
4. Add a breadth/coverage claim using the live 20→3 `~/.config/opencode` shrink — rejected: substrate-adjacent host state, and count-only pins cannot prove identity (round-18 carried debt).

## 7. Artifact and evidence paths

| Path | Role |
|---|---|
| `corpus/lessons/round-20.md` | blocked attempt; Gate; rejections |
| `.ufo/reports/round-20/kagi.md` | local report |
| `.ufo/round-20/local-checks.json` | `OP_REF_SELFTEST: PASS (36 cases)`, shell-LF negative, exits |
| `.ufo/round-20/inspection.json` | `OP_DOTENV_BYTES: CLEAN (checks=6 failed=0)`, `opVersion 2.40.0` |
| `.ufo/round-20/route-admission.mjs` | local route gate (BLOCKED, exit 2) |
| `plans/wwkd-round-20-interactive.md` | declared plan for the blocked round |
| `corpus/lessons/round-19-recensus.md` | verdict lines, named debt, audit erratum |
| `corpus/claim-ledger.tsv` / `corpus/stamps.tsv` | the two data files D7/D14/D15 measure |
