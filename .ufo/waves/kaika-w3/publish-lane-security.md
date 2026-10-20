# Publish lane security scan — 21 physical child repos

Lane: **PublishLaneSentinel** (read-only; no repo writes, no fetch/push, no builds/tests, no scanner install).
Scope: the 21 physical child repos of `local://kaika-publish-scope.json` only. `fleet`, `canonical`, `omp-binding`,
`retired-kimi-mirror` belong to other lanes (PublishCoreSentinel); the UFO repo is out of scope for this session.
Range: recorded base → HEAD per repo. All 21 recorded bases verified ancestors of HEAD (clean new-commit range);
untracked/staged user work is therefore structurally excluded.
Cutoff: 2026-10-20T01:01:00Z UTC. Audio head recorded here is `63593ded480a`; the parent
refreshes the final metadata-only audio head and the root aggregate after this cutoff.

## Method (all read-only)

1. **gitleaks 8.30.1** (`/usr/bin/gitleaks`, distro package; **no install performed** — PublishCoreSentinel confirmed the
   pacman build and owns installation) — `gitleaks git <repo> --log-opts <base>..HEAD`, default ruleset, JSON report into a
   `0700` temp dir, parsed then deleted. Verified there is **no suppression surface**: no `.gitleaksignore`, no
   `.gitleaks.toml`/`gitleaks.toml` in any repo or in the kernel cwd, no `GITLEAKS_CONFIG`/`GITLEAKS_CONFIG_TOML` in env.
2. **Custom bounded regex pass over every added line** (`git diff -U0 <base>..HEAD`), typed patterns: PEM/private-key armour,
   AGE secret keys, AWS/GitHub/GitLab/Slack/Google/OpenAI/Stripe/SendGrid/npm/PyPI/HF/DO token shapes, JWT, Discord/Telegram
   webhooks, `Authorization`/`Bearer`/`Cookie`/`Basic` headers, `op://` and vault/sops/secret/kms/ssm schemes, URL userinfo,
   credential-shaped `key=value` assignments, credential-ish env-var names, `--password/--token/--api-key` CLI flags,
   home/secret-store paths (`.ssh`, `.aws`, `id_*`, `.netrc`, `.env`, `credentials.json`, `service-account*`), cert blocks.
3. **Binary pass**: every added non-text blob — the only ones added in the whole range are the 9 audio WAVs — scanned for
   ASCII secret patterns and home paths.
4. **Targeted context reads** (`git show HEAD:<path>`) only for flagged lines; knowledge/lesson/report docs judged in context.

Redaction discipline: no raw candidate value is echoed in this report; every candidate is given as `path:line` + type +
`sha256[:12]` fingerprint + length. URL userinfo is never printed.

## Result

**No credential value, private vault reference, or auth material was found in the new committed changes of the 21 child
repos.** 0 confirmed secrets. 5 gitleaks hits and 24 regex hits, all triaged benign (F4/F5). Coverage below.

## Coverage

| repo | base | HEAD | commits | files | added lines | gitleaks | regex hits | verdict |
|---|---|---|---|---|---|---|---|---|
| audio | `defbe1286` | `63593ded480a` | 8 | 365 | 88991 | 0 | 0 | clean |
| chousa | `ab19cff53` | `d730ae4c3398` | 3 | 22 | 1273 | 0 | 0 | clean |
| game-dev-2d | `e89905162` | `7461a0868798` | 7 | 48 | 11324 | 0 | 0 | clean |
| game-dev-3d | `7c4e5897d` | `3118be0b18dd` | 4 | 43 | 14469 | 5 | 0 | clean |
| kagi | `aea7a4301` | `1e9e67ff3f8f` | 3 | 18 | 1309 | 0 | 4 | clean |
| kaidoku | `de77d7545` | `767adafb97e2` | 7 | 49 | 1572 | 0 | 0 | clean |
| kake | `cb807bc8d` | `7e17c663b871` | 3 | 49 | 10800 | 0 | 2 | clean |
| kama | `35e9175fc` | `03b5f0e8b9ec` | 3 | 34 | 990 | 0 | 0 | clean |
| kasegi | `94aace220` | `13a51920068c` | 2 | 39 | 839 | 0 | 0 | clean |
| kengaku | `99cf615ca` | `a42bb40c1767` | 4 | 19 | 1413 | 0 | 0 | clean |
| kotoba | `78ee57e5e` | `c61a973b2e02` | 3 | 136 | 29762 | 0 | 0 | clean |
| kotodama | `c42d675be` | `4ad268365524` | 6 | 22 | 2589 | 0 | 0 | clean |
| kumitate | `16a5441a3` | `a5683a96cae2` | 6 | 16 | 2147 | 0 | 1 | clean |
| lore | `6cec83aed` | `6e804e2e5bff` | 4 | 35 | 2074 | 0 | 0 | clean |
| mado | `e1d81d480` | `e3e6a8e6ca49` | 10 | 56 | 2818 | 0 | 4 | clean |
| mori | `20e2255e7` | `bf7cdc4783d0` | 3 | 27 | 1454 | 0 | 0 | clean |
| revenger | `8bbcb4e32` | `cf02419276e5` | 5 | 30 | 2551 | 0 | 0 | clean |
| souji | `dcc8b9e83` | `31984f473ce4` | 4 | 34 | 2381 | 0 | 0 | clean |
| tabi | `40a6de87f` | `9bc89bfe78b1` | 4 | 17 | 1592 | 0 | 0 | clean |
| tameshi | `4eb4cf319` | `a21e9104723e` | 4 | 109 | 4719 | 0 | 13 | clean |
| tsukuroi | `9b70381c5` | `d8ec15d5e6c1` | 5 | 49 | 1801 | 0 | 0 | clean |
| **21 total** | — | — | **98** | **1217** | **186868** | **5** | **24** | **0 secrets** |

Added-line counts are the diff's new-file lines actually scanned (text); the 9 WAVs are covered by the binary pass.
Repo-by-repo verdict: no secret-shaped value; every flagged line resolved to a path, a citation URL, a hash/digest, an
identifier, or prose.

## Findings (all informational — none is a credential)

**F1 — vault-literal masking convention is a documented blind spot for pattern sweeps (low).**
Three independent places record deliberately breaking vault-URI literals so credential sweeps stay silent:
`kake:.ufo/round-20/resume/swarm-dispatch.json:194` ("1 occurrences of the 1Password URI scheme literal … are written as
`op:/ /` so the lane's credential sweep stays silent; no credential value was ever present");
`lore:.ufo/waves/round-103/seats/R103ReviewerPost.md:29` (literal `[vault-ref-scheme]` pattern replaced so the mandatory
credential sweep passes, benign); `kagi:corpus/sources-census.sh:67-71` (needle list assembled from fragments "so this
file never carries a literal the fleet pre-commit sweep matches"). Impact: any regex/pattern sweep — this lane's included —
cannot see masked references, so "clean" here does not prove "no obfuscated ref exists". Compensating control in-tree:
`kagi:corpus/QUALITY.md:24` (QA5) forbids secret values, tokens, session ids and vault/item/field names outright; verified
`op://` literal count in kagi's added lines = 0. **Measured in this lane:** the same broken/split-form search over all 21 added-line sets found only documented masking actions and sweep-detector instruments (see Limits), and no masked form carried a value — so for these 21 repos the statement is "no obfuscated reference carrying a credential was observed", not merely "gitleaks was silent".

**F2 — operator home paths / username in committed evidence (informational).**
Path strings only; no values and no file contents were read. `tameshi:.ufo/evidence/kaika-round-1/capability-demo/env-fingerprint.txt:13`
(`HOME=/home/vgpnk`), same file line 2 (lane path); `tameshi:.ufo/evidence/kaika-round-1/coldread/appendixB/*.out`
(`$HOME/.config/the-janitor/op.env`, fp `sha12=df7e284dd226` len 31 — the most auth-adjacent string found anywhere, and it is a
*path*; the file itself is not in any repo and was not read); `kama:.ufo/round-10/audit/stale-anchors.tsv:19,20,28,33`
(`~/.local/bin/the-janitor`, `~/.local/share/...`); `mori:corpus/evidence/roster-*.log` (`/home/vgpnk/Projects/shokunin/...`);
`kotoba:.ufo/round-46/evidence/w2/sources/fetch-log.json` (`.tower/worktrees/kaika/...` cwd).

**F3 — kasegi knowledge text carries private engagement identifiers (routing note, not a credential).**
New/modified `kasegi` knowledge cites lost operator trees `~/Projects/bounties` and `~/Projects/the-bounty-hunter` and claim/
VDP directory names that embed platform + vendor + finding-class (4 distinct entries across
`corpus/knowledge/{claim-package-contract,ev-model,intake-and-finalize,intake-surface,mission-ledger,operator-queue,ops-invariants,policy-access-playbook,retirement-autopsies,triage-thresholds,vdp-disclosure-packages}.md`
and `corpus/SOURCES.md`). These are disclosure-engagement identities, not secrets; flagged for the content/metadata lane to
decide publishability. Fingerprints on request (the paths are already in the repo text).

**F4 — gitleaks hits are fixture content hashes (no action).**
All 5 hits: `game-dev-3d:reports/round-108/battery/{base-7c4e589-r95-rows,r95-rerun,replay-nonauthor-20261019T222103636356Z,slope-only,full-run-20261019T220450573107Z}.verdicts.json:23`,
rule `generic-api-key`, 64-hex SHA-256 of the fixture file named in the key, value fp `sha12=1e436c3ccd2b` in all five.
Per instruction, hashes are not secrets.

**F5 — regex hits are substring artefacts (no action).**
24 hits: `.env` inside `process.env` (`kake` mutants), `op.env` file *name* (`kagi:PROVINCE.md:49`, `kagi:corpus/README.md:69`,
`tameshi` evidence), namespace label `live.env.gdk_scale` (`mado` evidence), `fcToken(...)` helper call
(`kumitate:scripts/proxy-check.mjs:2010`), and prose `ssh-rsa`/`ssh-ed25519` in `kagi:corpus/knowledge/sops-age-key-rotation.md:37-38`
(no key material).

## F3 follow-up — public-presence determination (requested by Main)

Question: do the F3 engagement/vendor/finding-class identifiers already exist in the public remote snapshot
(`origin/master` = `origin/HEAD` = `3bd13fa`, already fetched locally) and/or the initial base `94aace2`, or are they new
from private-only material? Method: fixed-string `git grep` over each rev's tree (no fetch, no rescan, no mutation), plus a
brace-expansion equivalence check for the one token whose literal spelling is new. Values are not echoed; identifiers are
`sha256[:12]`; "shape" gives family + segment lengths only.

| id (fp) | shape | public @3bd13fa | base @94aace2 | local HEAD | supporting path (public) |
|---|---|---|---|---|---|
| `0b2c5a719f63` | `claims/`13 (len 32) | **yes**, 50 occ / 13 files | yes | yes | `corpus/knowledge/claim-package-contract.md`, `corpus/knowledge/submitted-registry.md`, `corpus/lessons/round-1.md` |
| `8fd44a966947` | len 41, extends `0b2c5a719f63` | **yes**, 27 occ / 8 files | yes | yes | `SKILL.md`, `corpus/knowledge/policy-access-playbook.md` |
| `baa04f615a58` | `claims/`14 (len 40) | **yes**, 89 occ / 12 files | yes | yes | `corpus/knowledge/target-checkouts.md`, `corpus/knowledge/program-quirks.md` |
| `f4078b0bc05f` | `claims/`14 (len 21) | **yes**, 3 occ | yes | yes (+1) | `SKILL.md`, `corpus/instruments/citation-survival.tsv` |
| `572dcb58138d` | `vdp-disclosures/`34 (len 50) | **yes**, 16 occ / 8 files | yes | yes (+1) | `corpus/knowledge/vdp-disclosure-packages.md`, `corpus/knowledge/submitted-registry.md` |
| `167f111c6335` | `claims/`19 (len 26) | literal: **no** (0) | no | yes, 1 occ, `corpus/knowledge/vdp-disclosure-packages.md:35` | components public — platform token `bc0a066d1057` (158 occ), trailing component `a2a1e69c4f83` (4 occ, incl. this file); token equals an expansion of the public brace-form token at `corpus/knowledge/vdp-disclosure-packages.md:4` (public blob `3d239b762a37`) |

Conclusion: 5 of 6 identifiers are literally public already. The sixth is not literally present publicly, but both of its
components are public and it is an expansion of a brace-form token the public snapshot already carries in the same file
(public line 4 reads `claims/<9>-{<4>,<9>}/<6>-<4>-vdp-no-<6>/` in masked shape). So the merge adds an **un-braced
respelling**, not a new identifier disclosure. Containing-file blob contrast: public and base `3d239b762a37` → local
`24d3d1e33989`. Local refs carrying the new spelling: `master` (`13a51920068c`), `kaika/publish-sync` (`922a4dde90b6`).
No source mutation, no rewrite, no tests. Optional zero-delta remediation if wanted: re-brace that one token on
`corpus/knowledge/vdp-disclosure-packages.md:35` (docs-only, same file the parent is already merging).

## Limits

- Committed ranges only (`base..HEAD`). Uncommitted, staged, and untracked work was never read; the excluded user dirs
  (`reports/r107`, `.ufo/r10plans`, `scratch`) and ignored auth/session dirs are absent from all 21 ranges (checked).
- Default gitleaks ruleset only. A separate high-entropy pass over added lines produced 4429 URL/citation-dominated
  candidates; after URL/path filtering, 8 opaque residuals were individually triaged benign (tool-binary digest + evidence id
  in a REA report on `/usr/bin/docker`, 3 seat/agent ids, 2 benchmark row labels, 1 base64 Go-module blob, 1 test-fixture
  string list).
- Binaries: only the 9 added WAVs exist in the range; no archives or encoded payloads were added.
- Masked/obfuscated vault-scheme literals are invisible to *pattern sweeps* (F1). A dedicated search for broken/split forms (`op:/`, `op: /`, `op:/ /`, `op:\\`, concat/`.join(` builders, `needle`/`fragment` builders, `[vault-ref-scheme]`-style placeholders) over all 21 added-line sets returned 130 marker lines — every one a documented masking action or a sweep-detector instrument (kake `op:/ /` in the dispatched rule text + its redaction note; lore `[vault-ref-scheme]` placeholder + L1 notes; game-dev-2d redaction note in copied reports; game-dev-3d policy prose naming `op:`; kagi runtime-built needles in `sources-census.sh`; tabi `/op:\/\//` detector regex; ~110 more are the word "fragment" in SOURCES-fragment prose). No masked form carried a credential value. Residual: an obfuscation shape outside those forms (e.g. base64-encoded scheme, cross-file concatenation) would remain invisible; none observed.
- Per scope, no credential stores, config values, or live targets were read.
- Scanner equality: this lane used the same already-installed gitleaks binary as PublishCoreSentinel; no install race.

## Provenance

- HEADs re-verified unchanged at publication: no drift across the 21 repos since the scan (fleet/canonical/omp-binding/retired-kimi-mirror drift belongs to PublishCoreSentinel's lanes).

- audio: base `defbe1286` → HEAD `63593ded480a2f9b0cf59dc39f7efb72250fe8b7`
- chousa: base `ab19cff53` → HEAD `d730ae4c33989ad9c8535764d4cae77b4db869f6`
- game-dev-2d: base `e89905162` → HEAD `7461a0868798c5fb7a08d119fa71e472172726c5`
- game-dev-3d: base `7c4e5897d` → HEAD `3118be0b18dd7351b1faf6ce99d26a34370793ec`
- kagi: base `aea7a4301` → HEAD `1e9e67ff3f8f9e7118f8a7026c0e79aab9ce42b2`
- kaidoku: base `de77d7545` → HEAD `767adafb97e2eef6980e2ad873d357e16721c467`
- kake: base `cb807bc8d` → HEAD `7e17c663b8713daac27774d49d87c4d44ea30747`
- kama: base `35e9175fc` → HEAD `03b5f0e8b9ec421c0b819b31e1bbc452b61dd0f9`
- kasegi: base `94aace220` → HEAD `13a51920068c48c0c5b3c8c81d5af0df6d4ea337`
- kengaku: base `99cf615ca` → HEAD `a42bb40c1767e1ac24394fadda7301ae5409e7ae`
- kotoba: base `78ee57e5e` → HEAD `c61a973b2e02e1ded169703ddcb06466f4edd8bd`
- kotodama: base `c42d675be` → HEAD `4ad26836552462d28a946ca3b067cab0b5ce3532`
- kumitate: base `16a5441a3` → HEAD `a5683a96cae2fcdcf313e4a3b47dea340d6451a9`
- lore: base `6cec83aed` → HEAD `6e804e2e5bff0edcc260c995a058dd724b0c98c0`
- mado: base `e1d81d480` → HEAD `e3e6a8e6ca493e250fb357343816a88e844c4c63`
- mori: base `20e2255e7` → HEAD `bf7cdc4783d0748d525fbfe3ba8fb3d285eb929a`
- revenger: base `8bbcb4e32` → HEAD `cf02419276e5dd8aafb6fe09d4e9aaa6bcb78c97`
- souji: base `dcc8b9e83` → HEAD `31984f473ce4bdab61a99b16cca194b28108cb81`
- tabi: base `40a6de87f` → HEAD `9bc89bfe78b1c455501b2c7a0d9bd061ea539c21`
- tameshi: base `4eb4cf319` → HEAD `a21e9104723e7a46b794b03b8fdcdd1455696f7e`
- tsukuroi: base `9b70381c5` → HEAD `d8ec15d5e6c1d93370f5a85b929745e26577f4d8`
