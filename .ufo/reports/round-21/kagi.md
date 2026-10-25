# kagi — round 21 report (kaika campaign, 2026-10-19)

Lane `kagi` (secrets & vault ops). Steered round **21** (kaika steer table, kagi row). Lane worktree
`/home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/kagi-shokunin`, branch `kaika/round`, base `aea7a43`.
**Lane HEAD at report time: `e1544c1`** (round work `c41af82`, post-landing correction `e1544c1`; both
authored `kagi-shokunin <kagi@shokunin.local>`; check: `git -C <worktree> merge-base --is-ancestor c41af82 e1544c1`).
Collision check before work: no kagi report in either round-21 reports directory (`ls` listed only
`kotodama.md`), no round-21 entry in the lane `LOG.md`.

## Work performed

Declared claims (3, distinct axes, `plans/round-21.md`):

- **C1 — depth 8 → 9** (lowest of the six scores; the round-20 attempt's declared open claim): admit the
  `--dotenv-bytes` arm that `aea7a43` landed unclaimed.
- **C2 — calibration 9 → 9, measured sub-moves** (owned axis; freshness and calibration tie at 9, so C2
  carries the lowest-owned-axis duty): mine the lane's own mistakes into `corpus/QUALITY.md` criteria,
  each citing its lesson; regenerate `SHONEN.md` canonical.
- **C3 — capability (source registry + census gate) + coverage 9 → 9**: `corpus/SOURCES.md` per contract
  v1, `corpus/sources-census.sh`, three knowledge entries on uncovered ground citing `mined` rows.

Prerequisite (contract repair, not a claim): `corpus/QUALITY.md` §Admission bar QA1–QA8, written before
dispatch; C2 appends below it, C3 reads only it, C1 touches neither.

Work items:

- Re-measured the byte contract on the new op release: `op --version` → `2.41.0`;
  `bash corpus/op-ref-probe.sh --dotenv-bytes` → `OP_DOTENV_BYTES: CLEAN (checks=6 failed=0)`, exit 0;
  `--selftest` → `OP_REF_SELFTEST: PASS (36 cases)`; shell-substitution negative ` 61 6c 70 68 61`.
  Evidence: `corpus/knowledge/op-ref-consumption.md` §11; ledger `R21-01`, `R12-02` (`corpus/claim-ledger.tsv`).
- Admission bar + mistakes: `corpus/QUALITY.md` (QA1–QA9, QM1–QM12), `corpus/lessons/round-21.md`
  §Mistakes M1–M12 (pointers re-opened), `SHONEN.md` canonical (`[x]` 4 → 0).
- Sources: 16 rows opened 2026-10-19 with fetch sha256 per row (`corpus/SOURCES.md` `teaches` cells),
  `## Paths`, `## Search log`, `## Leads (unopened)`; gate `corpus/sources-census.sh` (ledger `R21-02`,
  `R21-03`).
- Entries admitted: `corpus/knowledge/onepassword-machine-credentials.md`,
  `corpus/knowledge/sops-age-key-rotation.md`, `corpus/knowledge/vault-openbao-token-lease-lifecycle.md`
  (each with an appended erratum from the post-landing review); `corpus/README.md` coverage rows,
  `## Frontier`, `## Known gaps`; `PROVINCE.md` §Core / Frontier / Adjacent (round 21).
- Ledger reconciliation: `R12-03` (63 stamps), `R13-01` (23 headings — it had been left at 20 by round 20),
  `R14-01` (24/21), `R21-04` (39 rows); stamps re-pinned for every touched/new file only.
- L2 swarm: one batched `task` call of **11** taxonomy roles, no model passed, each prompt led by
  `/skill:godspeed` + the verbatim `directive.md` bytes — `W2RoundKagi.Planner-3`, `Connector-3`, `Scout-3`,
  `ExecDepth-3`, `ExecSources-3`, `ExecEntries-3`, `ExecGate-3`, `Scribe-3`, `Reviewer-3`, `Critic-3`,
  `Sentinel-3`. The batch was refused twice (`Background job limit reached (100)`) and spawned on the third
  identical call. Provider exhaustion: all four executors died (`resource_exhausted`, then
  `turn_rate_limit_exceeded` on their `-4` re-dispatch); recovered by `ExecSources-4`, `ExecEntries-5`,
  `ExecGate-5`, with the ExecDepth slice finished by the L1. No claim was shrunk.
- Post-landing falsification (`W2RoundKagi.PostReviewer`, `W2RoundKagi.PostCritic`) on `c41af82`; fixes by
  `W2RoundKagi.ExecGateFix` and the L1 landed as `e1544c1` (lesson §Post-landing review).
- Verification at `e1544c1`: 26 hermetic/repo-only ledger rows re-run individually, 26/26 PASS (incl.
  `R21-01..04`, `R12-02`, `R12-03`, `R13-01`, `R14-01`, `R11-09`); stamp check
  `sha256sum --check` → only the 5 named-debt rows differ; `claim-ledger.sh citations` → the same 23
  pre-existing unresolved fleet `.ufo/` pointers before and after, none in round-21 lines.
  `claim-ledger.sh verify` was **not** run (its `R18-01` row reads host files through `drift-pins.sh`).
- Credential sweep on both commits' staged diffs (fleet pattern) printed nothing; domain sweep on added
  lines (age secret key, Vault/OpenBao token, JWT, service-account token shapes) printed nothing.

## Landed changes

| change | LOG.md entry | commit |
|---|---|---|
| byte-fidelity section §11 + `Reverify` R21-01; `R21-01` row; `R12-02` 29 → 36; probe stamp; `PROVINCE.md` count | `LOG.md` §21 (C1 bullet) | `c41af82` |
| `corpus/QUALITY.md` QA1–QA8 + QM1–QM11; `corpus/lessons/round-21.md` §Mistakes, §Gate, §Named debt; `SHONEN.md` regenerated | `LOG.md` §21 (C2 bullet) | `c41af82` |
| `corpus/SOURCES.md`; `corpus/sources-census.sh`; three entries; README index/Frontier/Known gaps; `PROVINCE.md` §Core/Frontier/Adjacent; `SKILL.md` two decision rows + counts; ledger `R21-02..04`, `R12-03`, `R13-01`, `R14-01`; stamps | `LOG.md` §21 (C3 bullet) | `c41af82` |
| `SCORECARD.md` §Round 21 pre/post, move log, §Planned (round 21 close), capabilities (2 rows), saturation declared | `LOG.md` §21 | `c41af82` |
| gate fail-open fixes (selftest 40 → 47, `R21-03`); errata on E1/E2/E3; QA9, QM12; README/SKILL/PROVINCE counts; `SCORECARD.md` §Round-21 correction; lesson §Post-landing review | `LOG.md` §Round 21 correction | `e1544c1` |

## Before → after measurements

All commands from the lane root; **before at `aea7a43`, after at `e1544c1`** (re-run on that commit's clean tree).

| claim | counting command | before | after |
|---|---|---|---|
| C1 | `grep -c 'DOTENV_OBS' corpus/knowledge/op-ref-consumption.md` | 0 | 6 |
| C1 | `grep -c 'DOTENV_BYTES' corpus/claim-ledger.tsv` | 0 | 1 (`R21-01`) |
| C1 | `awk -F'\t' '$1=="R12-02"{print $3}' corpus/claim-ledger.tsv` | `(29 cases)` (probe printed 36 → row red) | `(36 cases)`, row PASS |
| C1 | `bash corpus/op-ref-probe.sh --dotenv-bytes` (op 2.41.0) | unrowed; last run op 2.40.0 | `OP_DOTENV_BYTES: CLEAN (checks=6 failed=0)`, exit 0 |
| C1 | probe stamp equality (`test "$(awk -F'\t' '$1=="corpus/op-ref-probe.sh"{print $2}' corpus/stamps.tsv)" = "$(sha256sum corpus/op-ref-probe.sh \| cut -d' ' -f1)"; echo $?`) | 1 | 0 |
| C2 | `awk -F'\|' '/^\| M[0-9]/ && $6 ~ /QM/' corpus/lessons/round-21.md \| wc -l` | 0 (file absent) | 11 (of 12 classes; the honest stop keeps none) |
| C2 | `awk -F'\|' '/^\| Q[AM][0-9]/' corpus/QUALITY.md \| wc -l` | 0 (`test -e corpus/QUALITY.md` → 1) | 21 (19 at `c41af82`) |
| C2 | `grep -c '^- \[x\]' SHONEN.md` | 4 (lane-dispatched verifiers = author attestation) | 0 (`[~]` = 4) |
| C3 | `bash corpus/sources-census.sh` | absent | `SOURCES_CENSUS: CLEAN (rows=16 A=14 B=0 C=2 queued=1 mined=14 rejected=1 entries_sourced=3 legacy=21)`, exit 0 |
| C3 | `bash corpus/sources-census.sh --selftest` | absent | `SOURCES_CENSUS_SELFTEST: PASS (47 cases)` |
| C3 | `ls corpus/knowledge/*.md \| wc -l` | 21 | 24 |
| C3 | `grep -c '^## Frontier' corpus/README.md`; `grep -c '^## Known gaps' corpus/README.md` | 0; 0 | 1; 1 |
| C3 | `awk '/^## Capabilities/,/^## Saturation/' SCORECARD.md \| grep -c '^\| '` | 2 (header + placeholder) | 3 (header + 2 rows) |

Contract census (SOURCES-CONTRACT-v1 §Census, all clean at `e1544c1`): rows 16; malformed 0; tiers
`A=14 C=2`; statuses `mined=14 queued=1 rejected=1`; duplicate ids: none; enum/tier-inflation: none;
missing used-by: none.

Per-claim self-verdicts (pending non-author verification): **C1 holds** (post-landing reviewer `holds`,
critic `holds-with-limits`: the six classes were first seen on op 2.40.0; this round re-measured, pinned
and documented them). **C2 holds-with-limits** (audit facts, score not raised; QM5 was unmet as written at
`c41af82`, superseded by QM12; outside spot-check pending). **C3: capability holds after `e1544c1`;
coverage admission contested** — at `c41af82` the critic judged E1 and E3 to fail the bar on scope
(eligibility omitted; Kubernetes path generalised; OpenBao TTL labelled Vault/OpenBao; KV "nothing
expires"), and the reviewer found four census fail-open paths. Both were corrected in-round by appended
errata and gate fixes; whether errata repair an admission is the operator's ruling. No axis harmed found:
freshness, operability, adjacency scores unchanged and no previously green ledger row turned red.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources
  `SKILL.md` §Vault-ops decision table rows 46–48 (round-21 rows cite `corpus/QUALITY.md`, three knowledge entries); `SHONEN.md` evidence line 1
- [~] At least one end-to-end domain task executed and logged in LOG.md
  `LOG.md` §21 — `op run --env-file` byte contract executed on op 2.41.0 (`R21-01`, exit 0); historical end-to-end: `LOG.md` round-3 entry
- [~] Instructions executable by an agent without oral context
  `bash corpus/sources-census.sh --selftest` (47 cases) and 26 re-run ledger rows at `e1544c1`; `corpus/README.md` index
- [~] No cross-domain bleed (PROVINCE.md still accurate)
  `PROVINCE.md` §Core / Frontier / Adjacent (round 21); connector sweep `agent://W2RoundKagi.Connector-3` — no sibling claims the new ground

## Sources & frontier

- SOURCES rows before → after: 0 (`test -e corpus/SOURCES.md` → 1 at `aea7a43`) → **16**
  (`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` at `e1544c1`).
- Added by tier: A = 14 (vendor docs/announcement for their own product, each scoped), C = 2 (S005 product
  page kept `queued` as a lead, rejected as mechanism support; S008 SOPS README `rejected` — it is now a
  pointer stub; flip recorded).
- Rows touched in place old → new: none (all new). Leads added after the post-landing review: Vault KV v2
  API / KV overview; Credential Broker custom-OIDC sub-page.
- Frontier rows advanced: README `## Frontier` created with 3 areas (OIDC workload-federation trust policy;
  secret-scanning detection vs verification; NIST key-management draft status), each pointing at SOURCES
  leads; three areas moved into documented core (machine-credential custody, SOPS/age rotation,
  Vault/OpenBao clocks).
- Search log: 29 identified (W1 ART dossier), 16 opened, 13 left as leads, 1 rejected; stop rationale in
  `corpus/SOURCES.md` §Search log.

## Mistakes

- Classes mined: **12** (`corpus/lessons/round-21.md` §Mistakes M1–M12: overclaim of absent sources,
  wrong mechanism attribution, fail-open verdict, false hermeticity, unclaimed landing, round-identity
  reuse, placeholder in a durable artifact, honest stop (model, kept), freeze not honoured,
  advertised-but-unwired mode, absence claim without a valid sweep, misattributed citation). Captured-by
  before: none of 12; after: 11 (M8 is the model).
- Criteria added: QA1–QA8 (admission bar), QM1–QM11 (one per uncaptured class), QA9 and QM12 (from the
  post-landing review) — 21 rows, each citing its lesson (`corpus/QUALITY.md`).
- Mistakes made this round and caught in-round: two entries admitted past a bar that did not check
  qualifier survival (→ QA9); a gate written with four fail-open paths (QM3's class, recurring); QM5 unmet
  as written (→ QM12). One critic finding (S007 "public beta") not reproduced — recorded as unverified.

## Trend verdicts

- **expansion: improved** — three admitted entries on ground no coverage-map row held, each citing `mined`
  rows (`ls corpus/knowledge/*.md | wc -l` 21 → 24), two capability rows. Disclosed: two entries failed a
  re-read of their own sources at `c41af82` and carry errata at `e1544c1`; if the operator rules that an
  erratum does not repair an admission, this is `harmed` for those two.
- **quality: improved** — a stale count pin (`R12-02`) and an unclaimed landing re-verified on the new op
  release and pinned; `R13-01`/`R14-01`/`R12-03` reconciled; every scope defect found was marked by an
  erratum, none left unmarked.
- **discernment: unchanged** — the outside admit/reject spot-check has not happened (lesson §Gate
  §Spot-check: pending, nothing inferred). Lane-internal disagreements became lessons with grounded
  criteria (QA9, QM12), but the lane's own L2s are still the lane.

## L0 questions

- kagi | round-21 | `claim-ledger.sh cells` exits 2 on the filed heading `## Round 20 — interactive attempt; blocked, not completed (2026-10-15)` (since `93ab9a5`). May the lane re-title that filed heading (with an appended erratum quoting the old text), or must the gate learn an attempt-section shape instead?
- kagi | round-21 | Five stamps are stale on files edited by the round-16 re-dispatch erratum and round 18 (`corpus/knowledge/config-layering.md`, `handler-on-disk-state.md`, `handler-trust-boundary.md`, `janitor-env-contract.md`, `corpus/lessons/round-18.md`). Re-pin them as reviewed, or keep them as named debt?
- kagi | round-21 | The fleet credential sweep runs over the whole `git diff --cached`, removed lines included, so a line that already contains the reference-scheme token (e.g. `SKILL.md` §Falsification, `PASS (29 cases)`) can never be corrected without a sweep hit. Should the sweep scan added lines only (`git diff --cached -U0 | grep '^+'`)?

## Integrator notes

- **No push.** The standing operator rule "No push" overrides `MISSION.md`'s commit-then-push;
  `PROTOCOL.md` §Fleet-2 conventions names the precedence. Both lane commits are local on `kaika/round`.
- Report not committed in the ledger worktree (per §6.1); integrator commits it under
  `--author="kagi-shokunin <kagi@shokunin.local>"`.
- **Out-of-scope shell activity:** my first shell call this round hit the silent `cd` failure and ran
  read-only `ls`/`wc` in the fleet root. No file was written outside the lane worktree and this report.
- Provider exhaustion (executor route) and the 100-job cap are recorded in `corpus/lessons/round-21.md`
  §Provider exhaustion.
- Fleet ledger: `MANIFEST.json` has no kagi round-20 row while the lane records round 20 as a blocked
  attempt (STATE dossier D6), integrator ledger only.
- Cross-domain evidence: none absorbed. Adjacent ground (chousa research method; chousa/kasegi/kumitate
  secret-shaped tripwires; kama's credential-broker refusal; kaidoku and tsukuroi 1Password binary and
  package reads; kake's musketeer profile lease) is listed in `PROVINCE.md` §Core / Frontier / Adjacent.
- Stale-lane actuator: no mission of this lane is open beyond two driver ticks (no driver dispatch this
  round; in-session lane).
- Non-author verification still owed (orchestrator): ≥1 admit + ≥1 reject spot-check (candidates:
  admit E2 `corpus/knowledge/sops-age-key-rotation.md`; reject S008 or the "Broker removes every secret
  from CI" candidate), ≥3 SOURCES rows re-opened, every counting command above re-run on `e1544c1`.
