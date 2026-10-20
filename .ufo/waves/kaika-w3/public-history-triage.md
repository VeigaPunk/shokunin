# Public-history triage — souji + omp-binding `generic-api-key` hits

Scope: the 6 `generic-api-key` findings enumerated in `local://kaika-public-history-scan.json`
for repos `souji` (5) and `omp-binding` (1). `canonical` had 0 findings and was not re-examined.
No history was rescanned, no code modified, no remote visibility changed.

Method: each finding was reproduced in isolation with the same scanner build and config used by the
aggregate run (gitleaks 8.30.1, default config, no ignore/allow), by materialising only the single
blob at the finding's commit into a private temp dir (`0700`) and running `gitleaks dir`. Matched
values were captured programmatically, classified, and then discarded; **no candidate value is
printed here** — each finding carries `sha256(match)[:12]` as a verifiable, non-reversible
coordinate. Context lines below are masked.

Reproduction fidelity: all 6 reproduced at the identical `File`/`StartLine` and identical rule ID;
column spans and entropy are recorded per finding. The rule's own entropy floor (3.5) is what
separates these six from the thousands of other prose tokens in the same files — every one sits
just above it (3.54–4.31).

| # | repo | path:line | rule | fingerprint | class | blocker |
|---|------|-----------|------|-------------|-------|---------|
| S1 | souji | `census/round-11/seat-23.json:92` | generic-api-key | `43d57548258b105ee7fabd923ecc30d91037d015:census/round-11/seat-23.json:generic-api-key:92` | false positive — prose label list | no |
| S2 | souji | `census/round-8/seat-16-inventory.json:543` | generic-api-key | `6d749f17a3e13b9f71259830f2d4ec4a93393134:census/round-8/seat-16-inventory.json:generic-api-key:543` | false positive — prose label list | no |
| S3 | souji | `census/round-8/seat-16-verdicts.json:711` | generic-api-key | `6d749f17a3e13b9f71259830f2d4ec4a93393134:census/round-8/seat-16-verdicts.json:generic-api-key:711` | false positive — prose label list (same value as S2) | no |
| S4 | souji | `tests/fixtures/case-F10/expected.json:47` | generic-api-key | `9435e464a2dc8c421f0d97b0ce178463748ce38d:tests/fixtures/case-F10/expected.json:generic-api-key:47` | synthetic test canary (by design) | no |
| S5 | souji | `census/round-6/seat-69.json:1` (col 3799-3827) | generic-api-key | `b5db5cf27b5c993ed1832cb917ddeff77a080dd0:census/round-6/seat-69.json:generic-api-key:1` | false positive — local scratch dir basename | no |
| O1 | omp-binding | `shokunin/drill-keeper/corpus/2026-10-09-self-test-probes.md:15` (col 183-202) | generic-api-key | `6791f6a4c43262848103f393fdef68220cd73c54:shokunin/drill-keeper/corpus/2026-10-09-self-test-probes.md:generic-api-key:15` | false positive — documented probe-id in a catalog | no |

## Per-finding evidence

### S1 — `census/round-11/seat-23.json:92`
- Match: 33 chars, entropy 3.582, no digits, `sha256[:12]=58793d151ea2`; file blob `bcbc272af79f…`.
- Line: `"secret_handling": "<match> secret-shaped flags are name-based; no secret-shaped file contents were read…"`.
- Class: **prose label list**, not a credential. The value is five slash-joined lowercase sibling
  repo short names (segment lengths 8/4/8/4/5); each segment resolves to an existing sibling project
  directory (`<seg>-shokunin`) under `/home/vgpnk/Projects/shokunin`. Verified by equality, not by eye.
- Why the rule fired: the JSON *key* `secret_handling` supplies the keyword, `": "` supplies the
  separator, and the path-shaped prose that follows clears the entropy floor.
- Corroboration: the same record states the seat's secret flags are name-based and that no
  secret-shaped file contents were read or emitted by that census.

### S2 / S3 — `census/round-8/seat-16-inventory.json:543` and `…-verdicts.json:711`
- Same value in both files: 25 chars, entropy 3.539, no digits, `sha256[:12]=e9fb8453def3`
  (blobs `ac9deabddaf2…` and `cb00f1b942e9…`); column 6-40 / 5-39.
- Line shape: `"token": "<match>",` inside a `{"kind": "fs:path", "locations": [...]}` census record.
- Class: **prose label list**. The value is three slash-joined lowercase labels (5/9/9) that equal, by
  exact string comparison, souji's own artifact-class phrase — the three cleanup classes named in its
  mint narrative ("a cleaner shokunin (掃除) for … artifacts"); the literal is intentionally not echoed
  here. It is not a repo path: the exact string is absent from the commit tree.
- Decisive grounding: the verdicts file's own adjudication for this record is
  `"status": "NON-POINTER(prose-list)"`, `"detail": "slash-joined prose/labels; string-level, no probe"`.
- Occurrences: exactly 3 in the repo (LOG.md prose line 6, plus these two census files).

### S4 — `tests/fixtures/case-F10/expected.json:47`
- Match: 27 chars, entropy 4.310, `sha256[:12]=f957993f5e0e`; blob `f046084c1d24…`.
- Line: `"creds.pem": "<match>"` inside the fixture's `"leak_canaries"` object.
- Class: **synthetic test canary**, by construction. Shape is a human-readable
  `SOUJI-<case>-CANARY-<role>-<hex6>` label; no provider prefix, no key material.
- The same string is planted in `tests/fixtures/case-F10/creds.pem`, whose header reads
  "synthetic placeholder, not a key, never read" and whose body is `PEM-PLACEHOLDER: fixture-data-only`
  (no PEM private-key block, 132 bytes). Sibling canary in `app.env` alongside
  `FAKE_API_KEY=fixture-not-a-real-key`. The fixture README states the files are
  "synthetic, non-functional placeholders", and `expected.json` asserts that the tool's
  stdout+stderr contains **neither** canary. Publishing it is the fixture's purpose.

### S5 — `census/round-6/seat-69.json:1`
- Match: 22 chars, entropy 3.538, `sha256[:12]=fcb311e88de9`; blob `adfb2c86b028…`; the host file is a
  3.6 MB single-line JSON.
- Context: an entry `{"key": "<match>", "count": <bytes>}` inside `by_top_level_bytes` of a read-only
  scratch census (`"mode":"dry-run-read-only"`, root `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.scratch`).
- Class: **local scratch directory basename** (path component), not a credential. Grounding: the exact
  string is an existing entry among the 2445 entries of that local scratch root (verified by
  `os.path.exists`), and its siblings in the same list are the same class of scratch run-dir names.
  Shape `a99-a99-a99-aaaaaaaaaa`, i.e. a run-dir name with a random suffix.
- Rule fired on the `"key":"…"` idiom (keyword `key` + `":"` separator).
- The census declares `"secret_rule"` (basename match on `*.env|.env|.env.*|.envrc|*credential*|*secret*|id_*|*.pem`)
  and states secret-shaped paths are **never opened** (`content_read_cap: 200`), so no secret-shaped
  contents are in this file — only names/counts.

### O1 — `shokunin/drill-keeper/corpus/2026-10-09-self-test-probes.md:15`
- Match: 13 chars, entropy 3.547, no digits, `sha256[:12]=0866f4ac68d4`; blob `933ee362bb49…`.
- Context: a prose enumeration of negative drill-probe categories —
  "…, unknown keys, **<match>** expect, duration bounds, pending/referenced discipline, …".
- Class: **documented probe id / prose label**. Shape is 7 lowercase letters + `/` + 5 lowercase
  letters; both segments occur as ordinary standalone lowercase words across omp docs at HEAD
  (9 and 237 files respectively). The file itself is a probe catalog ("58 negative drill probes, each
  mapping a probe id to an expected refusal substring") for a self-test harness.
- Rule fired on `keys, ` (keyword + comma separator).
- Reachability: the file was archived by `0bddb85` ("archive 26 keepers") and is **still at HEAD** as
  `archive/shokunin-2026-10-09/corpora/drill-keeper/corpus/2026-10-09-self-test-probes.md`; the finding
  commit `6791f6a4` is an ancestor of `main` (and of `tower/shokunin3/drill-keeper`), so the string is
  on published history and on the published tip, not only in unreachable objects.

## Verdict

**No credential, and no uncertain credential, in either repo. None of the 6 findings blocks the
public flip, and no rotation or history rewrite is required for them.**

- 5 of 6 are false positives of the `generic-api-key` rule on prose/path tokens (S1, S2, S3, S5, O1):
  a repo-name list, souji's artifact-class phrase, a local scratch directory name, and a drill probe id.
- 1 of 6 is an intentional synthetic test canary whose fixture asserts it never leaks (S4).
- Zero findings carry a provider prefix (`AKIA…`, `ghp_…`, `sk-…`, `AIza…`, `eyJ…`, `-----BEGIN …`, etc.),
  and none has a shape consistent with a live credential.

Reachability note for the flip decision: these strings are already in the *published tip* as well as in
history (all 5 souji paths exist at `refs/heads/master`; the omp string exists at HEAD under the
archived corpus path). Since none is sensitive, history rewriting would buy nothing here.

Escalation rule applied: had any match been real or uncertain, the required remedy would have been
rotate-then-rewrite with the visibility flip held — not applicable, nothing triggered.

## Non-blocking hygiene observations (not credential exposure)

1. `census/round-6/seat-69.json` publishes the operator's absolute project root
   (`/home/vgpnk/Projects/shokunin/kotodama-shokunin/.scratch`) and local scratch directory names.
   This is local-path disclosure, not secret disclosure.
2. `census/round-8/*` and `census/round-11/*` likewise embed local absolute paths in `resolved` fields.
3. The `generic-api-key` rule will keep flagging this class of prose in `census/**` on every future
   scan. If a clean scan record is wanted later, a repo-scoped allowlist for those census paths is the
   smallest fix; that is a code change and was deliberately not made under this read-only assignment.

## Addendum — post-scan delta coverage (added 2026-10-19)

The aggregate scan's commit counts no longer match the live mirrors (scan: souji 23 / canonical 16 /
omp-binding 174; mirrors now: souji 27 / omp-binding 178, and the local `kimi-shokunin` clone exposes 8
reachable commits on `main` only). To keep the flip clearance honest rather than assume the scan's tip,
the un-scanned tail was closed with bounded, targeted runs — no whole-history rescan.

- **souji tail: 0 findings.** Range `2f303dc..HEAD` = 5 commits (`dcc8b9e`, `d7266c5`, `de9187e`,
  `2a363a0`, `31984f4`, all 2026-10-19), 34 files changed / 2397 insertions, scanned with
  `gitleaks git` 8.30.1 default config, `--redact=100` → 0 findings. Harness control: the same command
  over `9435e464^..9435e464` correctly re-reports the F10 canary (1 hit), so the 0-result is a real
  scan, not a no-op range.
- **omp-binding tail: covered.** Range `0bddb85..HEAD` is a single commit (`b8c699c`), audited clean by
  `PublishCoreSentinel`; the flagged archive blob is byte-identical at base and HEAD (verified by blob
  OID equality), so the tail cannot alter the disposition.
- **canonical: covered by the peer's range, with a stated limit.** `PublishCoreSentinel` audited
  canonical `bc7d690..e737d2ea` (HEAD, created after the aggregate scan) clean. I could not re-verify
  the scan's "16 reachable commits" locally — the mirror the scan used is not present; the working copy
  at `/home/vgpnk/Projects/kimi-shokunin` is `main`-only with 8 reachable commits. Recorded as a limit,
  not a claim.

Net: aggregate scan ∪ this triage ∪ the peer's range scans ∪ the souji tail scan now covers the
published tips of all three repos. **Verdict unchanged: no credential, no blocker, no rewrite needed.**
