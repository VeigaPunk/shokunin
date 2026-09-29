# Sentinel scope audit — round 9

Measurement stamp: 2026-09-29 (wall-clock session), main HEAD `62fdfbe` immediately before measurement. Child landed revisions and worktree counts at that stamp: kasegi `b7180b0`/6, kengaku `f09ff1f`/1, kake `a209441`/0, kumitate `e0e5de1`/8, kotoba `63ceba7`/0, kagi `4391b3b`/21. Per the dirty-tree rule, landed-HEAD cells below are the verdict cells; worktree cells for dirty repos are provisional.

## 1. Secret sweep

Sweep command (Python 3; no secret value is printed):

```sh
python3 - <<'PY'
# For every file from `git ls-tree -r HEAD --name-only -- corpus/` and every
# worktree corpus file in each child, plus round-9 wave files, l0 questions,
# planned prompts/reports, run these regex classes. Output is class, path,
# line, first four bytes only, value length, and placeholder/random shape.
classes = {
'op://':r'op://', 'sk-':r'\\bsk-[A-Za-z0-9_-]{6,}',
'ghp_':r'ghp_[A-Za-z0-9]{6,}', 'github_pat_':r'github_pat_[A-Za-z0-9_]{6,}',
'xox[abprs]-':r'xox[abprs]-', 'AKIA':r'AKIA[0-9A-Z]{16}',
'JWT eyJ':r'eyJ[A-Za-z0-9_-]{6,}\\.[A-Za-z0-9_-]{6,}',
'BEGIN PRIVATE KEY':r'-----BEGIN [A-Z ]*PRIVATE KEY-----',
'cookie/set-cookie':r'(?i)\\b(?:set-cookie|cookie):',
'bearer ':r'(?i)\\bbearer\\s+', 'password=':r'(?i)\\bpassword\\s*=',
'token=':r'(?i)\\btoken\\s*=',
}
PY
```

The executed implementation used the same classes plus `gh[posur]_`, `api_key`, `ssh-(rsa|ed25519) AAAA`, and `aws_secret`, scanned all child corpus files at landed HEAD and worktree, all in-window added lines, and main files planned for this integration. A corrected rerun reproduced its own landed corpus counts (`reproducibility check: True`). The first exploratory collector had a global-list bug and is not used as evidence.

### Corpus rule-8 results at landed HEAD

Observed output of `git ls-tree` + `git show HEAD:path` scanner (counts are class hits, not secret values):

| repo / landed HEAD | op:// | sk- | ghp_ | github_pat_ | xox | AKIA | JWT | private key | cookie | bearer | password= | token= | rule 8 verdict |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| kasegi `b7180b0` | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **not conformant**: `op://` hits |
| kengaku `f09ff1f` | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | **not conformant**: `op://`; bearer hit requires review |
| kake `a209441` | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **not conformant**: `op://` |
| kumitate `e0e5de1` | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | **not conformant**: `op://`; token hit requires review |
| kotoba `63ceba7` | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **not conformant**: `op://` |
| kagi `4391b3b` | 55 | 1 | 0 | 0 | 5 | 0 | 0 | 0 | 0 | 5 | 1 | 3 | **not conformant**: multiple rule-8 classes |

Rule: `CORPUS.md` line 43 says “No credential material, ever … vault ref paths (`op://…`) stay out of every corpus, including this one's examples.” Therefore even synthetic-looking `op://` references are defects in corpus material; mechanism-only bearer/token/password examples require owner review, but do not overturn the `op://` verdict. Exact paths/line numbers were emitted by the scanner; for example, landed kagi hits include `corpus/drift-pins.sh:22`, `corpus/knowledge/op-env-refs.md:12`, and `corpus/lessons/round-8.md:21` (only class and first four bytes `op:/` are reported, never the value). Kagi’s worktree-only additions include further `op://` hits and are **provisional**; the landed verdict remains at `4391b3b`.

### Round-8 box-3 files, amendments, new lessons, and commits

All six `corpus/lessons/round-8-aggregator-box3-coldrun.md` files exist at the six landed revisions. The exact command `git diff --stat -- corpus/lessons/round-8-aggregator-box3-coldrun.md` reported no diff for kasegi, kengaku, kake, kumitate, or kotoba; kagi reported `1 file changed, 3 insertions(+), 3 deletions(-)` (provisional worktree amendment).

Added lane lessons since cutoff `2026-09-28T23:46:28Z`, from `git log --since=... --diff-filter=A --name-only -- corpus/lessons/`: kasegi `round-14.md`, kengaku `round-11.md`, kumitate `round-12.md`; kake, kotoba, and kagi had no added lesson in the default HEAD lineage. The full `git log -p --since=2026-09-28T23:46:28Z` added-line sweep was run for each child and the main repo (driver runtime excluded).

Pickaxe command:

```sh
git -C <child> log --since=2026-09-28T23:46:28Z -G'op://|\\bsk-[A-Za-z0-9_-]{6,}|ghp_|github_pat_|xox[abprs]-|AKIA[0-9A-Z]{16}|eyJ[A-Za-z0-9_-]{6,}\\.|BEGIN [A-Z ]*PRIVATE KEY|cookie:|bearer |password=|token=' --format='%h %ad' --date=iso-strict
```

Observed output: **zero matching commits in all six child repos** for every class in the pickaxe regex. This does not erase pre-existing corpus defects; it establishes no matching addition in the since-cutoff commit window.

### Wave fixtures

`glob '**/corpus-gate*'` and the round-9 wave listing found no `corpus-gate.mjs` yet; only `CONTEXT.md` was present at the first sweep. `CONTEXT.md:69` contains the literal rule-text `op://…`, not a vault address. If the planned gate fixtures are added, credential-shaped strings are acceptable only as isolated, committed, no-network fixtures when every value is unmistakably synthetic and marked in-file (e.g. `FIXTURE_ONLY`, `NOT_A_SECRET`, and a comment stating synthetic/non-resolvable); never use a real-looking usable token, a resolvable `op://` path, or a fixture copied into `corpus/`. Detector regexes may contain pattern syntax without a credential value. The gate self-test must prove the fixture path and must not print the matched value.

## 2. Write / push scope audit

Deciding clauses are quoted with source locations.

| planned write | ruling and safe boundary |
|---|---|
| `.ufo/reports/AGGREGATE.md` §14 | Allowed as the aggregator routed-defect ledger; keep append-only and do not rewrite prior rows. The Gate standard says the aggregator ledger is the routed-defect queue, not a second inventory. Safe alternative for unrelated main files: route the defect in this ledger/report rather than editing the target. |
| `SCORECARD.md` aggregator section | Allowed. `PROTOCOL.md:431-433` expressly gives the two main-repo lanes (`protocol`, `aggregator`) `SCORECARD.md` and `LOG.md` at the root. Every score must carry command and measured commit. |
| `LOG.md` round-9 entry | Allowed under the same `PROTOCOL.md:431-433` clause; append only (`PROTOCOL.md:424` says LOG is append-only). |
| `.ufo/reports/round-9/aggregator.md` | Allowed as the aggregator’s own lane report: `PROTOCOL.md:430-431` says lanes write their lane report at `.ufo/reports/round-<N>/<id>.md`. |
| `.ufo/waves/round-9/**` | Allowed as round evidence, but landing belongs to the integration commit: `PROTOCOL.md:434-435` says `.ufo/reports/` and `.ufo/waves/` are written evidence committed with that integration commit. This seat itself may write only its own seat file. |
| `.ufo/l0-questions.md` append | Aggregator **may append a new question** because `PROTOCOL.md:479-485` says lanes append and the aggregator surfaces entries; no lane owns the path. It must never answer/rewrite a filed line. The integrator, not the aggregator, owns durability and commits it with integration. Safe alternative if a question is not needed: do not touch the file; if needed, append the prescribed lane/round/opening-words line and leave it for integrator pathspec. |
| child `corpus/lessons/round-9-aggregator-*.md` | Allowed and aggregator-owned under `CORPUS.md` rule 9 / `PROTOCOL.md:460-463`. Use aggregator identity, not the child/operator identity, and make a narrow local commit. **Do not push**: `MISSION.md:51-56` permits pushes only to main or the lane’s own remote; child repos are sibling lane remotes for the aggregator. |

Forbidden before landing: `.ufo/state/**` and `.ufo/watchdog.log` (runtime; `PROTOCOL.md:436-439` says no lane commit may include them); `MANIFEST.json`, `PROTOCOL.md`, `CORPUS.md`, `MISSION.md`, `AXES.md`, `scripts/` (integrator/operator-side files under `PROTOCOL.md:424-430`); sibling-owned corpus files and in-place corrections (`PROTOCOL.md:460-463`, CORPUS rule 9); and `SHONEN.md` (child lane’s generated promotion artifact, not aggregator scope). Safe alternatives are a routed ledger/report entry, a new aggregator-owned lesson, or an L0 question; do not broaden the commit pathspec.

### Sweep hazard and mitigation

The round-6 precedent is commit `ade32e4`: `git show --stat ade32e4` observed a kagi report commit that included `.ufo/l0-questions.md` and a report move, demonstrating collateral side-channel capture. `PROTOCOL.md:450-452` names the direct hazard: never `commit -a` / `add -A`, because these sweep sibling in-flight edits and integrator working-tree changes. A live child lane can therefore capture a staged aggregator lesson under the wrong identity. Mitigation: coordinate a quiet window, stage only the exact `corpus/lessons/round-9-aggregator-*.md` path, immediately commit with an explicit pathspec and aggregator identity, verify `git show --stat HEAD` contains only that file, and leave the commit local/unpushed. If swept anyway, record the misattribution as a conformance defect and add a new correction lesson; never rewrite another lane’s corpus file.

## Findings

- **S-01 (severity 4, rule 8):** All six landed child corpora have at least one `op://` hit; kagi additionally has `sk-`, xox, bearer, password, and token-shaped hits. These are concrete rule-8 blockers before corpus lessons land.
- **S-02 (severity 3, scope/push):** Pushing aggregator-authored child lessons would violate `MISSION.md` §Push scope; commit locally under aggregator identity and do not push.
- **S-03 (severity 3, scope):** Any commit that includes `.ufo/state`, watchdog, forbidden integrator files, sibling corpus, or `SHONEN.md` violates invariants; use pathspec-limited commits and route instead.
- **S-04 (severity 3, race):** A live lane’s broad commit can sweep a staged aggregator lesson, producing wrong authorship and durability; narrow immediate commits plus `git show --stat` verification are required.

This evidence is author-side for SentinelSeat; it is not a non-author verification of the aggregator’s own artifacts.

### Literal rule-8 reconciliation

The literal-text sweep was re-run after the L1 amendment with the landed revisions above:

```sh
python3 - <<'PY'
# for each child: git ls-tree -r HEAD --name-only -- corpus/; git show HEAD:path;
# count regex `op://`; emit only repo, file, line, first4=`op:/`
PY
```

Observed landed counts: kasegi 2, kengaku 1, kake 2, kumitate 1, kotoba 3, kagi 55. Every occurrence is classified as a schematic/example or sweep-pattern occurrence rather than a demonstrated resolvable vault item; no value is printed, and the file/line/`op:/` prefix is the only identifying output. This classification does **not** make the literal rule pass: under `CORPUS.md:43-46`, each repo is `FAIL-literal / PASS-intent` where the hits are only schematic placeholders. A real-vault-path classification would be `FAIL-literal / FAIL-intent`; none was demonstrated by this read-only sweep. The inherited round-6 “clean” interpretation is not reused. The operator/integrator must either remove all literal `op://` occurrences from corpus entries or amend rule 8 to distinguish schematic placeholders from resolvable references; that conflict is routed as a rule-8 ledger row.
