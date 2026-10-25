# R14HomeProvenance — registry-home audit: round-15 closure gate object provenance

Scope executed: read-only static audit of `.ufo/waves/round-15/closure-check.py`,
`fixtures/closure-sample/`, the frozen baselines `frozen/r15-pre-003400` and
`frozen/r15-post-012710`, the history pin `.ufo/history-pin.json`, and the fresh
`before.json`. No gate/selftest/frozen run was executed; the known live crash was
not re-run. All work below is path/digest arithmetic, `git` object inspection and
source reading (permitted by `context.md:13`). Nothing here is a conformance verdict:
**no PASS is inferred from static inspection** — outcomes belong to the parent's
integrated execution.

## 1. Resolution baseline

- Requested baseline commit `99efc52b3a6f3648f7d8e097d78460901ad3c91c` is the repo
  HEAD and matches `before.json.measured_commit` (`before.json:5`).
- `git diff --name-status 99efc52 -- .ufo/waves/round-15` → empty: every audited
  round-15 object in the working tree is byte-identical to its committed form at the
  baseline revision. (Whole-repo drift exists only in files owned by the in-flight
  wave/other lanes: `SCORECARD.md`, `PROTOCOL.md`, `PROTOCOL-APPENDIX.md`, `LOG.md`,
  `.ufo/watchdog.log`, `.ufo/l0-questions.md`, untracked dirs — not in this audit
  surface.)
- Repo root confirmed by the gate's own default rule (`closure-check.py:194-205`):
  `/home/vgpnk/Projects/shokunin` holds `MANIFEST.json` + `.ufo/`.

## 2. Path / revision / digest table

Blob IDs are git SHA-1 at commit `99efc52`; sha256 are content digests of the
working-tree bytes (identical to the blobs, per §1).

### Implementation

| path | mode | blob @99efc52 | sha256 | status |
|---|---|---|---|---|
| `.ufo/waves/round-15/closure-check.py` | 100755 (executable) | `2e5c0afede78f50f94249b4043d6379b8fd54112` | `0ac440f7a3b3a7500568fa469b7efba451ee0eabb9683b827630dcc0869a778c` | verified = `before.json` protected pin, = inherited `protected-before.json.closure_gate_sha256` |

### Frozen baseline `round-15/r15-pre-003400` (closed_at 2026-09-29T00:34:00-03:00)

| file | blob @99efc52 | sha256 (content = pinned in expected.json `inputs`) |
|---|---|---|
| `MANIFEST.json` | `1ad6d404fa6e7a7544848edeea91b356fd84a9f3` | `37fc2f677314794d3fc2b5dd2084f697e3361ffbca61bd2d75b426539d39954f` |
| `watchdog.log` | `0ef69cfa6bf8082c816fb8d9c6c5c1ccbd0b9f08` | `3a70e5e47e4af90dee85ba24d90e4880a53ac9c4ef3029633538f3ee686f94ff` |
| `prompts-index.txt` | `e4670dd0a8187987e26d641681cfe82a73b4e47f` | `d8f2b1a20d5f6cae93723bedeb972bccabb9950815d1179211d710db05deb7ad` |
| `reports-index.txt` | `3081515d66eee1f42569034ccc8acc8f01c634d9` | `5c0a00caf0a0e2ca9efada17777f089bfdbdd9675b87f279108b110804b47a7d` |
| `state-counters.txt` | `f78c3e97e486d331beb1061a15b3c33f130c0ccf` | `ae8165c16fefafb298837ac2c083ba64279adaf1b2b25b29ff4ac0efbf0fa935` |
| `CLOSED_AT.txt` | `a54196224571f3898911daba1f27c7b66122327d` | `9662e4853b755c1c1721db8369b02246c6ab1d182cdd9d3948191d2299b7b2c1` |
| `expected.json` | `6c30a37e5b3c12893f953ea4e654ff6e06a8bd66` | `19d6935b7d84e84ef3946db3d3f3537c615f122f14fbe197aad31023db2ddea9` (= `before.json` protected pin) |

Declared verdict data (from `expected.json`, pinned values only, not executed
results): `exit: 1`; `debt`: 17 triples = 7× `stale_in_flight` + 10×
`unrowed_terminated` (lanes aggregator 9/10, kagi 15/16, kake 15/16, kama 1,
kasegi 16/17, kengaku 12/13, kotoba 15/16, kumitate 15/16, protocol 13/14).

### Frozen baseline `round-15/r15-post-012710` (closed_at 2026-09-29T01:27:10-03:00)

| file | blob @99efc52 | sha256 (content = pinned in expected.json `inputs`) |
|---|---|---|
| `MANIFEST.json` | `50e9e48be9a4bc48b68831a8662aecc42154b329` | `4c47f0ee2056de44558fafd410c0e0ca62dafc0c36939c75b3fac633fd4ac5e9` |
| `watchdog.log` | `17760552527d9676ff6d7789aac63795f435c7ec` | `a5f0ff7670db25e0d1fbc8391531bf4c4cf25265110a17cda27f75259d333c8c` |
| `prompts-index.txt` | `06602412be8082f528ca3188d5ae52cf8598e060` | `1f38a1568fc7e71a708a9a53ec0182a25fb57f80109defd4ed7cb27c370a1850` |
| `reports-index.txt` | `75322146068df766b63ee957af37f5d7497f5ea6` | `8a8cb0a732afaeb0eccd081a1a653f4c808dc449d27a4b4a7d0d486674294d4d` |
| `state-counters.txt` | `8a4075f29b2476f19a45eba13fa3f39930f82f88` | `0f19848e5c37896972b88ee9640e8a68a0910a5d0aacb86fbec4ed2c2e8d096b` |
| `CLOSED_AT.txt` | `5f2040c07fadebea5d32a72b34fcfc4249a10d59` | `859a72c0f5f6d43af8a58d658c6a850292b2d7e464c94edc650427fc01a5bd1a` |
| `expected.json` | `8918b152d233567d04fa1787c3994f0061614122` | `ba78759bc4652f6d73802dda10aafe04cdb48fdd351e803092fc849fda602315` (= `before.json` protected pin) |

Declared verdict data: `exit: 0`; `debt: []`.

Every pinned `inputs` digest above equals the actual file content digest I
recomputed (6/6 per baseline, zero mismatches, zero missing listed files).

### Supporting objects

| path | blob @99efc52 | sha256 | notes |
|---|---|---|---|
| `.ufo/history-pin.json` | `03b9be29bf122324cd824a82377e4429b3ea299d` | `b161cd4106c928472c1eca8395262beb7624e23349743fcd2880e2b416e7f81b` | worktree == commit (empty diff); = `before.json` protected pin |
| `MANIFEST.json` (live) | `ce15a28272f3a64143b98d31dad41c7429909ef0` | `c784fbd40f86ab07a71d0e93f8c957e9048c51820dfd338e41a0249ce7398fa4` | worktree == commit; 142 `rounds` entries; = `before.json` protected pin |
| `.ufo/reports/round-14/protocol.md` | (file on disk) | `d2567df3f11018ebd168918c46c7ea69119e45e41ac2f58140b1bf5634f691b4` | = `before.json` protected pin and inherited `prior_report_sha256`; filed marker intact, byte-prefix obligation still satisfiable |
| `.ufo/waves/round-14/registry-home-rerun/before.json` | untracked at audit time | `6f8e73ef57465f8cbd0096ca0c6696b43e2c3a11554e8d97bf84c1976db8d70f` | no git provenance yet; parent commits it |

`before.json` self-consistency (static re-derivation of its recorded stdout):
at `99efc52:SCORECARD.md`, protocol-registered `closure-check` gate rows = **0** and
root `SKILL.md` **absent** — exactly `protocol_registered_closure_gates=0`,
`root_SKILL_exists=False` (`before.json:10`). Its 7 `protected_sha256` entries: all
recomputed and matched, except the section pointer — see §7 and §9.

## 3. Inputs-map coverage audit (the required check)

Rule enforced: the `inputs` map must cover every file the frozen mode actually
consumes, not just restate its own declared list.

Consumers and their reads:
- `load_frozen` (`closure-check.py:393-450`) reads, from the snapshot dir:
  `MANIFEST.json`, `watchdog.log`, `state-counters.txt`, `prompts-index.txt`,
  `reports-index.txt`.
- `do_frozen` additionally reads `expected.json` (`:1792`).
- Digest verification (`:1801-1818`) checks only the rels listed in `inputs`; an
  unlisted tampered file would **not** be caught — so list-completeness is the
  security-relevant property.

Result per baseline:
- Directory holds exactly 7 files (verified by listing). Both maps declare exactly
  the other 6 — `CLOSED_AT.txt`, `MANIFEST.json`, `prompts-index.txt`,
  `reports-index.txt`, `state-counters.txt`, `watchdog.log`. **All five files
  consumed by `load_frozen` are covered**, plus `CLOSED_AT.txt`.
- `expected.json` cannot self-pin by construction; its external anchors are the
  git blob at `99efc52` (table above) and the `before.json` protected sha256. This
  is the intended design: `freeze-snapshot.py:801-803` hard-codes the file set as
  those six inputs, and `:734-737` fixes the snapshot file set to those six +
  `expected.json`.
- `CLOSED_AT.txt` is declared/pinned but **not read by `closure-check.py` at all**
  (only by the freezer tool, `freeze-snapshot.py:525,790`); its presence is broader
  coverage, not a gap.
- A `--frozen` run against these baselines therefore takes the `status: match`
  digest-verification branch at analysis time (`:1818`), never the
  `snapshot_tampered` (`:1812-1817`) or `unpinned (legacy)` (`:1802-1804`)
  branches, **given the worktree stays as audited**.

CLOSED_AT internal consistency (recomputed): pre — log lines 314 = `wc -l`
`watchdog.log` 314; reports 110 = index rows 110; prompts 105 = 105; counters 9
rows; `manifest_entries 48` = rounds in copied MANIFEST (48, roster 6);
`manifest_source git-ref ae19fca` — copy is byte-identical to
`git show ae19fca:MANIFEST.json` (sha256 `37fc2f67…` equal). post — log 328 = 328;
reports 113 = 113; prompts 108 = 108; entries 74 = 74;
`main_HEAD 8afbc8f` = commit `8afbc8fe8750e330bf74abd8a03d88a9e30b8b3c`,
committer date 2026-09-29T00:19:15-03:00 ≤ its C (00:34:00) ✓; post
`main_HEAD acbd3bc` = `acbd3bc66abb6097934929fcfb38aa532f9fc006`, committer date
2026-09-29T01:27:02-03:00 ≤ its C (01:27:10) ✓.

## 4. Registry pointers vs copied baselines

Four distinct pointer/copy layers — do not conflate them in the registry rows:

1. **Copied baselines** (bytes that live in this repo): the two snapshot dirs under
   `.ufo/waves/round-15/frozen/`. Self-contained, tamper-detectable via their own
   `inputs` digest maps (§3), and committed at `99efc52` with blob IDs in §2.
   - r15-pre `MANIFEST.json` copy is git-reproducible: identical bytes to object
     `ae19fca:MANIFEST.json`.
   - r15-post `MANIFEST.json` copy is a **worktree capture** ("live MANIFEST.json"
     per its CLOSED_AT): those 74-entry bytes are *not* in `acbd3bc` (which still
     holds the 48-entry `37fc2f67…` blob). The first commit carrying them is
     `3687e5a34b7b03a6f7defc161ae2cdf4ce6eb702` (2026-09-29T01:50:09-03:00, ~23 min
     after the snapshot instant) — digest-resolved by me, not recorded in the
     snapshot. Provenance of the post manifest therefore rests on the content
     digest, with `3687e5a` as the earliest git witness.
2. **Registry pointers** (path→digest assertions onto mutable/live objects):
   `before.json.protected_sha256` (7 entries; 6 whole-file, 1 section-selector —
   §7) and `.ufo/history-pin.json` (`manifest_commit ae19fca` + canonical digest —
   §5). These point; they do not copy bytes.
3. **Name pointers**: the qualified frozen names `round-15/r15-pre-003400` and
   `round-15/r15-post-012710` resolve via `_resolve_frozen` (`:1005-1027`):
   `<wave>/<NAME>` → `.ufo/waves/<wave>/frozen/<NAME>` directly; a bare NAME
   searches every `.ufo/waves/*/frozen` root newest-first and fails closed
   (exit 3) on a duplicate name (`:1019-1026`). Roots today: `round-12/frozen`
   (`pre`, `post`, `post-actual`) and `round-15/frozen`. The r15-* names are unique
   across roots, so bare forms resolve — but only the qualified names are
   collision-proof; registry rows should cite the qualified form (as `context.md:6`
   already mandates).
4. **Self-reference gap**: `expected.json` files are pinned only from outside
   (git blob + `before.json`), never from their own map (§3).

## 5. History pin audit (static recomputation of every gate check)

Pin (`99efc52`, clean): `entries 48`, `k 48`, `sha256 ce97497e…0a8e`,
`manifest_commit ae19fca` (=`ae19fca991aa419ac4c8fe25120c0dc1c363a4fb`,
committer 2026-09-28T22:55:48-03:00). Gate logic at `:927-987`; each predicate was
evaluated without running the gate:

- `history_pin_invalid` shape test (`:943-944`): k=48 is int, ≥0, ≤ len(rounds)=142;
  sha is 64-hex → not invalid.
- `history_pin_mismatch` (`:948-954`): canonical sha256 of live `rounds[0:48]`
  (`_canon_sha` = sort_keys/`(",",":")` JSON, `:914-916`) computed =
  `ce97497ed699a8f0939be062d042cf4d6e3e7531116fbe4681593991d67f0a8e` = pin → no
  mismatch (also identical for `99efc52:MANIFEST.json`).
- `history_pin_unverifiable` (`:958-972`): `git show ae19fca:MANIFEST.json`
  succeeds and parses → verifiable.
- `history_pin_unanchored` (`:974-978`): canonical sha of `ae19fca` rounds[0:48] =
  same `ce97497e…` = pin → anchored.
- `history_pin_orphan` (`:980-985`): `ae19fca` is an ancestor of HEAD (`99efc52`) →
  not orphan.
- `history_pin_absent`-class read error (`:939-941`): file parses → not raised.

So on the audited checkout all five pin finding-classes are statically falsified;
the append-only history (48 closed entries, protocol round-13 pass) is intact.
Note the pin check itself only *runs* inside live mode, which currently crashes
(§6) — pin soundness and that crash are independent defects; do not conflate.

## 6. Known live-crash provenance (confirmed statically, NOT re-run)

Inherited evidence `.ufo/waves/round-14/registry-home/live-closure.json` records
command `python3 .ufo/waves/round-15/closure-check.py --repo . --json
--no-citations`, returncode 1, empty stdout, `TypeError: '<' not supported between
instances of 'NoneType' and 'int'`, traceback `main:2042 → do_live:1775 →
analyze:1143`. `protected-before.json` (same dir) names the trigger: live
`MANIFEST.json` entry index 138, `round: null`, `type: "closure"`, all-`ok` lanes
map. I verified statically at `99efc52`: entry #138 has `"round": null` and lanes
{kagi,kake,kama,kasegi,kengaku,kotoba}=ok; line 1143 is
`sorted(all_rows, key=lambda x: (lane_sort(x["lane"]), x["round"], x["entry"]))` —
those six lanes also carry int-round rows, so the tuple comparison reaches
None-vs-int. Additional latent sites the same null reaches if 1143 were fixed:
`v >= r` (`:1147`), sorts at `:1180`, `:1339`, `:1436-1437`, `:1460`. The defect
exists in the audited baseline; per `context.md:7` it stays parent-routed and was
not exercised here.

## 7. Flags / exit map / scope, from source

CLI surface (`main`, `:1980-2006`): `--repo ROOT`, `--json`, `--show-keying`,
`--selftest`, `--frozen NAME|<wave>/NAME`, `--frozen-root DIR`, `--pin PATH`,
`--no-ledger`, `--no-citations`.

Exit semantics (`:90-93`, `:1428-1429`, `:1786-1824`, `:2008-2054`):
- Live: 1 if any debt (contradictions, keying, stale, unrowed, prompt_orphan/
  untracked, `history_pin_*`), else 2 if only could-not-evaluate (`unknown_lane`,
  `unknown_entry_type`; `:106`), else 0. Loader/parse errors → 2 (`:1779-1780`).
- `--frozen`: unresolvable name or missing/unparseable `expected.json` → 3;
  input-digest mismatch → 2 `snapshot_tampered` (comparison skipped, `:1812-1817`);
  pinned-baseline debt match → exit **taken from `expected.json.exit`** (`:1821-
  1822`); mismatch → 1.
- `--selftest`: fixture dirs each need `MANIFEST.json`+`expected.json`; any
  missing baseline → 3; all 27 checks pass → 0 else 1 (`:1914-1916`). Never reads
  the live repo (`:1989-1990`).
- Could-not-evaluate never masks debt (`:73-75`, `:1428`).

Run scope: the gate writes nothing outside stdout/stderr (`:77`); every subprocess
is a read-only git plumbing command (`show`, `log`, `cat-file --batch-check`,
`merge-base --is-ancestor`, `rev-parse --show-toplevel`, `ls-files` — call sites
`:742,756,783,875,906,958,980,1040,1043,1123`). Default live mode additionally
sweeps cited hashes through the operator read-only trees `EXTERNAL_READONLY`
(`:111-114`) — `--no-citations` keeps all git inside the audited repo; frozen mode
disables citations by construction (`:449`). `MAIN_SCOPE` (`:136-148`) is the
protocol/aggregator lane **write** scope used for stale-mission activity
attribution (`:1373`), not a gate write surface; it declares `.ufo/waves/*` (depth
≤4), `PROTOCOL.md`, `SCORECARD.md`, `LOG.md`, `.ufo/history-pin.json`, etc.

Fixtures (`fixtures/closure-sample`): 25 cases at `99efc52` (all with
MANIFEST+expected; +2 in-code unit checks = `--selftest` total 27). Each fixture
`expected.json` declares a **subset** of the ten count keys `do_selftest` consumes
(`:1881-1883`); standard five (`exit`, `debt`, `contradictions`,
`unrowed_terminated`, `pending_round`), widened only in the six universe/CNE cases
(e.g. `kama-counter-admitted`, `unknown-lane-annotation`,
`mint-nonclosure-entry`: +`could_not_evaluate`/`unknown_lane`/`nonclosure`). No
fixture carries an `inputs` digest map (verified across all 25) — fixture baselines
are count-pinned only; byte-tamper protection exists solely for `--frozen` mode.
No fixture declares a key the harness ignores (no inert pins).

## 8. Parent invocation plan (run once, post-integration; nothing here executed by me)

1. Frozen replays (offline, deterministic, no live-repo evidence, no citations):
   - `python3 .ufo/waves/round-15/closure-check.py --frozen round-15/r15-pre-003400 --json`
   - `python3 .ufo/waves/round-15/closure-check.py --frozen round-15/r15-post-012710 --json`
   Qualified names (collision-proof per §4.3). Assert from source semantics:
   `baseline_inputs.status == "match"` (§3 guarantees this on the audited bytes),
   then pinned verdict — pre: 17 debt triples (7 stale_in_flight, 10
   unrowed_terminated), exit 1; post: `debt: []`, exit 0. Any `snapshot_tampered`
   or `MISMATCH` is a real regression, not noise.
2. Fixture selftest (never touches live repo):
   `python3 .ufo/waves/round-15/closure-check.py --selftest --json` — expect 27
   checks; exit 0 only if all pass and no baseline missing.
3. Live mode: **defer** — the §6 defect stands in the committed ledger
   (entry #138) and registry status is registration, not a live clean verdict
   (`context.md:6-7`). When the parent routes the fix, use
   `--repo /home/vgpnk/Projects/shokunin --json --no-citations` to stay
   in-repo; add `--show-keying` only if keying tallies are contested. The pin
   result should print `anchored at ae19fca k=48 prefix=ce97497ed699` (§5).
4. Gate invocation is read-only (§7); safe to run before commit. The prior-file
   prefix obligation: `.ufo/reports/round-14/protocol.md` digest at audit =
   `d2567df3…` — re-verify the appended erratum keeps it an exact byte prefix.

## 9. Unresolved / limits (explicit)

- `SCORECARD.md#aggregator-section` = `7abc0478efcb16d0d2e4bbe57271d52c00da08a8eb33bc76edc272ae5b5cfccf`
  (in `before.json` and inherited `protected-before.json`): **no extraction recipe
  is recorded anywhere**, and eleven candidate section-slicing recipes over both
  `e163d15:SCORECARD.md` and `99efc52:SCORECARD.md` blobs do not reproduce it
  (closest: `bdc22e87…` heading→EOF). Partially redeemable fact I *can* attest:
  every candidate digest is identical at both revisions — the aggregator section
  bytes are unchanged `e163d15..99efc52`, so the "preserve byte-for-byte" clause
  holds in the audited range regardless of recipe. As written the pointer was
  unverifiable — subsequently RESOLVED: the parent supplied the exact recipe after
  this section was first drafted; see §10 erratum. This was a pointer-quality
  finding, not evidence of tampering.
- `before.json` is untracked at audit time: file-digest provenance only, no git
  object until the parent commits it.
- r15-post `MANIFEST.json` ↔ commit `3687e5a` equality is my digest-search
  resolution; the snapshot's own pointer says only "live MANIFEST.json". Earliest
  commit witness; not a claim by the artifact.
- No behavioral execution occurred: exit codes, debt sets and "match" statuses
  above are pinned declared values and source-derived expectations — **not
  observed results**. All PASS/FAIL authority stays with the parent's single
  integrated run.

## 10. Erratum — aggregator-section digest recipe (parent-supplied, verified)

Superseded item: §9 bullet 1 (pointer `SCORECARD.md#aggregator-section`).

Parent (Main, post-initial-draft) supplied the exact comparator recipe used to
produce the fresh `before.json` (and reproduced by the scout):

```python
hashlib.sha256(Path("SCORECARD.md").read_bytes().split(b"## Aggregator lane", 1)[1]).hexdigest()
```

Semantics: SHA-256 over the **raw bytes after the first literal occurrence** of the
18-byte prefix `## Aggregator lane`, excluding the prefix itself, including the
remainder of that heading line and every subsequent byte, with **no newline
normalization** (and, per the split, not just the heading's section — the whole file
tail).

Verification (static digest arithmetic, re-run by this seat after the correction;
no gate executed):

| subject | recipe digest | status |
|---|---|---|
| `e163d15bb1b080ae567ada3b86441455e9808f9b:SCORECARD.md` (inherited `protected-before.json` baseline) | `7abc0478efcb16d0d2e4bbe57271d52c00da08a8eb33bc76edc272ae5b5cfccf` | MATCH recorded pin |
| `99efc52b3a6f3648f7d8e097d78460901ad3c91c:SCORECARD.md` (audit baseline) | `7abc0478efcb16d0d2e4bbe57271d52c00da08a8eb33bc76edc272ae5b5cfccf` | MATCH `before.json` protected pin |
| working tree `SCORECARD.md` at erratum time (sibling wave edits in flight) | `ffeba61c152408c3a46201c0de9e481d7a12419e5d0b332c7f763e9a45db94c3` | differs from pinned value |

Reading: the pointer is fully reproducible at both committed revisions cited by the
before-files — §9's "identical at both revisions" byte-preservation attestation now
carries the exact recipe, not just eleven candidate slices. The third row is an
observation about the mid-edit worktree, not a verdict: a pre-heading protocol
subsection insertion would leave this tail digest unchanged, so the delta means
bytes in the post-heading tail differ from `99efc52` at that instant; the parent
owns the final comparator on the committed state (and `context.md:5` requires the
aggregator section preserved byte-for-byte). My original eleven-candidate battery
missed this variant because every candidate retained the heading prefix or
truncated the tail at the next heading.

No gate, selftest, or frozen baseline was rerun for this erratum.
