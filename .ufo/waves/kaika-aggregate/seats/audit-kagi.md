# audit-kagi — lane audit at pinned HEAD (round 12 aggregation)

Lane under audit: `/home/vgpnk/Projects/shokunin/kagi-shokunin` (original repo, not a worktree).
Parent-imposed mode: read-only. No child file was edited, staged, or committed; every lane
command below is `git rev-parse`, `git status`, `git archive` (inside the gate), or read-only
`grep`/`awk`/`sed`/`node`. Lane scripts were not executed.

## 1. Revision binding

```
$ git -C /home/vgpnk/Projects/shokunin/kagi-shokunin rev-parse HEAD
1e9e67ff3f8f9e7118f8a7026c0e79aab9ce42b2
$ echo $?
0

$ git -C /home/vgpnk/Projects/shokunin/kagi-shokunin status --porcelain
(no output)
$ echo $?
0
```

Observed: HEAD = `1e9e67ff3f8f9e7118f8a7026c0e79aab9ce42b2`, worktree clean (`dirty=0`).
Lane round derived from committed `LOG.md`: the last round record is
`### Round 21 correction — post-landing review of \`c41af82\` (2026-10-19)` (LOG.md tail,
lines 1033+), and `corpus/lessons/round-21.md` + `plans/round-21.md` exist. **Lane round = 21.**
This is a lane-authored round; it is not the aggregator's round number.

## 2. Gate runs (exact commands, exits)

Gate: `corpus-gate-v1`, header line `# corpus-gate-v1 — CORPUS.md rules recomputed (aggregator lane round 9)`,
script `/home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/fleet-aggregate/.ufo/waves/round-9/corpus-gate.mjs`.

### Run A — default round selector (9), as assigned

```
cd /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/fleet-aggregate
node .ufo/waves/round-9/corpus-gate.mjs --snapshot \
  /home/vgpnk/Projects/shokunin/kagi-shokunin \
  1e9e67ff3f8f9e7118f8a7026c0e79aab9ce42b2
```

Observed header/verdict (verbatim, selected lines):

```
# expect kagi-shokunin@1e9e67f ABSENT (no committed expected verdict for this revision)
# tree kagi-shokunin revision=1e9e67ff3f8f9e7118f8a7026c0e79aab9ce42b2 dirty=0 mode=snapshot
...
# verdict kagi-shokunin failed findings=63 rules=r2,r4,r8 rules-implemented=r2,r4,r7,r8,r10,shonen
# process-exit 1 (failed)
```

`GATE_EXIT=1`. Finding tally (from the same stdout): r2 = 8, r4 = 51, r8 = 4, r10 = 0, shonen = 0,
r7 = 0 (2 notes: 9 templates skipped; 17/71 files without index row, explicitly "not a finding").

### Run B — lane round 21 selector

```
node .ufo/waves/round-9/corpus-gate.mjs --snapshot \
  /home/vgpnk/Projects/shokunin/kagi-shokunin \
  1e9e67ff3f8f9e7118f8a7026c0e79aab9ce42b2 --round 21
```

Observed: `GATE_R21_EXIT=1`, additional finding

```
CR-kagi-shokunin-r10-1: no corpus/lessons/round-21-aggregator-*.md — the round-21 review duty has no emitted lesson (CORPUS.md:21)
# verdict kagi-shokunin failed findings=64 rules=r2,r4,r8,r10
```

Difference between runs = exactly r10-1 (63 → 64). At selector 9, r10 is satisfied by
`corpus/lessons/round-9-aggregator-corpus-verdict.md` (present); the listed aggregator lessons in
the tree are rounds 1, 4, 5, 5-mirror, 8-box3, 9. r10-1 is a fleet-side artifact (the aggregator
has not emitted a round-21 lesson into this lane), not a kagi-authored omission.

No committed expectation exists for this revision (gate says `ABSENT`), so exit-3 drift
precedence was not exercised; the observed exit is the rule-failure exit 1.

## 3. Verdict

**not conformant** at `1e9e67ff3f8f9e7118f8a7026c0e79aab9ce42b2` according to gate exit 1.
Failed rule IDs at default selector: **r2 (8 findings), r4 (51), r8 (4)**. With `--round 21`:
**r2, r4, r8, r10 (1)**. Exact finding lines are reproduced in §4–§6; the full stdout was captured
in this session and every finding cited below was independently re-located in the lane tree.

## 4. r2 — eight lessons without an evidence pointer

Gate output (verbatim, 8 lines):

```
CR-kagi-shokunin-r2-1: lessons/round-1-aggregator-audit.md carries no evidence pointer ... (CORPUS.md:19)
CR-kagi-shokunin-r2-2: lessons/round-10.md carries no evidence pointer ...
CR-kagi-shokunin-r2-3: lessons/round-3.md ...
CR-kagi-shokunin-r2-4: lessons/round-4.md ...
CR-kagi-shokunin-r2-5: lessons/round-5.md ...
CR-kagi-shokunin-r2-6: lessons/round-6.md ...
CR-kagi-shokunin-r2-7: lessons/round-7.md ...
CR-kagi-shokunin-r2-8: lessons/round-8.md ...
```

Predicate as implemented (`corpus-gate.mjs:439`):

```js
const evidenceCited = /\b[0-9a-f]{7,40}\b/.test(body) || /\.ufo\/reports\//.test(body) || /LOG\.md/.test(body);
```

Independent check (literal grep, no LSP server mounted for this seat):

```
cd /home/vgpnk/Projects/shokunin/kagi-shokunin/corpus/lessons
grep -cE '(\b[0-9a-f]{7,40}\b|\.ufo/|LOG\.md)' round-{1-aggregator-audit,10,3,4,5,6,7,8}.md
```

Observed hits per file: `round-1-aggregator-audit.md` 0, `round-10.md` 0, `round-6.md` 0,
`round-7.md` 0, `round-8.md` 0; `round-3.md` 1, `round-4.md` 1, `round-5.md` 1 — and each of those
three single hits is line 3, `Round context: kagi L1 dispatched (\`.ufo/prompts/kagi-round-N.md\`)`.
That is a pointer of a *different kind* (`.ufo/prompts/`, not `.ufo/reports/`), so the gate's literal
predicate correctly excludes it. Those three target paths are also absent from the lane tree:

```
ABSENT .ufo/prompts/kagi-round-3.md
ABSENT .ufo/prompts/kagi-round-4.md
ABSENT .ufo/prompts/kagi-round-5.md
```

So r2-1..r2-8 stand as implemented. Reader-level note (not a rule change): rounds 3–5 do not lack a
pointer in spirit; they cite a *dead* pointer under `.ufo/prompts/`. The gate's finding text names
only "commit hash, `.ufo/reports/` path, or LOG.md", so a reader cannot tell from the finding that a
dead pointer exists in those three files. `round-21.md` is the r2-clean counterexample (tokens
`c41af82`, `aea7a43`, `93ab9a5`, `af8873ca`; no `LOG.md` mention) — the predicate is satisfiable.

## 5. r4 — 51 count-claim findings, with a mechanical class partition

Predicate as implemented (`corpus-gate.mjs:450-463`): canonical surfaces only (`knowledge/**/*.md`,
`lessons/**/*.md`, `corpus/README.md`), skip lines inside a ``` fence, skip any line containing a
backtick, then fire if `COUNT_NOUN_RE` matches. Rule text it cites (actual CORPUS.md line 34, not 28):
"A count carries its command. Any number in a corpus entry (rows, files, lines, packages) is written
as `<number> — <command> <date>`."

I re-parsed the same 51 `file:line` pairs and partitioned them (disjoint; priority order shown):

| class | n | concrete instances |
|---|---|---|
| matched N is a *round reference*, not a count | 4 | `handler-on-disk-state.md:81` "round-6 note"; `op-cli-surface.md:27` "round-10 probes"; `transcript-hygiene.md:123` "round-9 run"; `round-8.md:49` "round-7 commit" |
| matched N is a date/mode value | 2 | `handler-on-disk-state.md:168` "0700 dirs"; `round-6-aggregator-audit.md:165` "0600 file" |
| line sits in an **indented** code block (fence tracker cannot see it) | 2 | `drift-gate.md:170` `bash corpus/drift-pins.sh --selftest # DRIFT_SELFTEST: PASS (13 cases)`; `round-9.md:154` |
| table-row cell | 6 | `drift-gate.md:97`, `round-10.md:68`, `round-13.md:110`, `round-13.md:111`, `round-17.md:120`, `round-21.md:53` ("quote (≤25 words)" — a template header) |
| wrapped prose count (count on a continuation line; command may be on the previous line or in a §Reproduction block) | 37 | e.g. `drift-gate.md:18` "2 of 13 files", `claim-ledger.md:206` "5 checks", `handler-on-disk-state.md:92` "238 rows" |

Consequences a reader must keep: the four round-reference hits are demonstrably *not* count claims
under CORPUS.md:34; the two indented-block hits carry their command literally on the flagged line,
unbackticked, in a rendered code block (`drift-gate.md` §Reproduction, lines 168–176 verified by
read); `round-21.md:53` is a table header template. The remaining 45 are counts whose command, if
present, is not on the same physical line — the rule's `<number> — <command> <date>` pairing is not
what the line-scoped predicate tests. I did not adjudicate these 45 either way; I only verified the
classes. No finding was suppressed or discounted in the verdict: gate exit stays 1.

## 6. r8 — four literal-text credential-class findings

Gate output (verbatim, condensed to the facts):

```
CR-...-r8-1: credential-class bearer occurrences=1 lines=1 files=1 owner=lane literal_shaped=1/1 :: classification=could-not-evaluate ... files=[knowledge/handler-trust-boundary.md] first=knowledge/handler-trust-boundary.md:39 first4="Bear" len=17
CR-...-r8-2: credential-class kv-secret occurrences=3 lines=3 files=3 owner=lane literal_shaped=0/3 ... files=[knowledge/claim-ledger.md,knowledge/control-plane-hardening.md,knowledge/handler-trust-boundary.md] first4="toke" len=72
CR-...-r8-3: credential-class op-ref occurrences=13 lines=12 files=5 owner=aggregator maxseg=3 ... files=[lessons/round-1-aggregator-seed.md, round-4-aggregator-audit.md, round-5-aggregator-audit.md, round-5-aggregator-mirror-..., round-9-aggregator-corpus-verdict.md]
CR-...-r8-4: credential-class op-ref occurrences=70 lines=67 files=24 owner=lane maxseg=3 ...
```

Independent reads:
- r8-1 is line 39 of `knowledge/handler-trust-boundary.md`: `| \`Authorization: Bearer jt-test-pw\` | — | 401 |`.
  The value is the same test password the probe table sets (`OPENCODE_SERVER_PASSWORD=jt-test-pw`);
  it is test-fixture-shaped, and `literal_shaped=1/1` is accurate. Whether that string is also a real
  credential is **not** decidable here (vault read, operator-gated) — the gate's abstention stands, and
  I do not overrule it. The literal occurrence itself is real.
- r8-2: `knowledge/claim-ledger.md:86` reads a POLICY grammar, `first-token:<w>|metachar|backslash|
  empty-quotes|inline-shell|denied-verb:<v>`; `literal_shaped=0/3` is consistent with the bytes.
- r8-3/4: `op-ref` occurrences are literal-text `op://` matches (13 in aggregator-authored lessons,
  routed by the gate to `owner=aggregator`; 70 in lane-authored files). Rule text (CORPUS.md:49-51,
  "No credential material, ever … vault ref paths (`op://…`) stay out of every corpus, including this
  one's examples") is a literal-text rule, so these stand as failed regardless of vault truth.
  The 13 aggregator-owned occurrences are not kagi-fixable; they route to the aggregator.

## 7. SOURCES structural observations (independent of lane scripts)

`corpus/SOURCES.md` at HEAD, bounded to the registry + paths + search log + leads:

```
$ awk -F'|' '/^\| S[0-9]{3} /{print NF}' corpus/SOURCES.md | sort | uniq -c
     16 13                      # every data row has 11 columns
$ grep -oE '^\| S[0-9]{3} ' corpus/SOURCES.md | sort | uniq -d | wc -l
0                              # no duplicate ids
```

Field tallies (fields 5 and 9 of the pipe split): tier `A=14`, `C=2`; status `mined=14`,
`queued=1` (S005), `rejected=1` (S008). Every one of the 16 rows carries a 64-hex fetch digest
(`grep -cE 'Fetch sha256: \`[0-9a-f]{64}\`'` → 16). Every `used-by` path resolves from the lane root:
`corpus/knowledge/onepassword-machine-credentials.md`, `corpus/knowledge/sops-age-key-rotation.md`,
`corpus/knowledge/vault-openbao-token-lease-lifecycle.md` — all PRESENT (one row, S008, has `—`).
`plans/round-21.md` exists and names S001–S016 as allocated, matching the search log's allocation
claim. Two-way linkage spot-check: the vault entry's `source:` names S012–S016 with per-page anchors
and version labels ("newest pinned entry v1.21.x", "OpenBao docs Version 2.7.x"), and rows
S012–S016 all carry `used-by = corpus/knowledge/vault-openbao-token-lease-lifecycle.md`.

These are structural facts only. They do not establish that any anchor quote exists at its cited
section, that any tier assignment is correct, or that the digests match what the URLs serve —
all of that needs network/vault access or the lane's own `sources-census.sh`, which I did not run.

## 8. Provenance/fidelity finding — SOURCES.md search log does not reproduce its own count

Parent-requested scan first, as the negative: across **all 24** `corpus/knowledge/**/*.md`,
`grep -c '^source:' / '^verified-at:' / '^recheck:'` returns 1/1/1 for exactly the three round-21
entries (`onepassword-machine-credentials.md`, `sops-age-key-rotation.md`,
`vault-openbao-token-lease-lifecycle.md`) and 0/0/0 for the other 21 (matches README §Known gaps'
"21 existing knowledge entries"). The ephemeral-path scan over provenance lines is **empty**:

```
$ grep -nE '^(source|verified-at|recheck):.*(\.tower/worktrees|/tmp)' *.md
$ echo $?
1
```

Exact `recheck:` values of the three new entries (no `.tower`/`/tmp` target in any):
- `onepassword-machine-credentials.md:4` — `90d for S001–S004; on-release for S006–S007 — reopen the cited CLI, Service Account, Connect, and Broker sections; check Broker preview status, claim requirements, workflow duration, and integration-key custody.`
- `sops-age-key-rotation.md:5` — `on-release — on a SOPS release or a change to the pages' "Last modified" footer (9b7b84e), re-open S011 §updatekeys/§rotate/§compromise order, S010 §Key groups threshold default, S009 identity lookup …`
- `vault-openbao-token-lease-lifecycle.md:5` — `on-release — on a Vault or OpenBao release, re-open S012 §JWT verification (audience rule, verification options), S013 KV note, S015 TokenReview note, S016 §Token Time-To-Live and §Token type comparison; …`

The one corpus surface that does bind evidence to an ephemeral path is `corpus/SOURCES.md:32`
(§Search log), and its quoted sweep does not reproduce its own count:

```
Where searched: the W1 ART dossier's 29 source leads
(`grep -cE '^\| S[0-9]{3} ' /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/fleet-ledger/.ufo/waves/kaika-w1/kagi-art.md`)
... Identified: 29; screened: 29; included: 15 usable rows (14 mined and 1 queued); excluded: 14 ...
```

Observed by running exactly that command (read-only, dossier mtime 2026-10-19 18:23:20 -0300):

```
$ grep -cE '^\| S[0-9]{3} ' <dossier>
0
$ echo $?
1
$ grep -cE '^\| ?S[0-9]{3}' <dossier>
29
```

Cause, verified from the dossier's bytes: its rows are `|S001|Load secrets into scripts — …`
(no space after the pipe), so a row can never match `^\| S`. The 29 leads do exist; the *quoted
command* cannot see them. This is a provenance/reproducibility finding, not a gate rule and not a
semantic verdict: a reader following the registry's own audit instruction gets 0, not 29. Two
distinct defects compose — (a) the sweep is bound to a `.tower/worktrees` path that is ephemeral by
the parent's own convention, and (b) even at that path the literal pattern is wrong. Historical
evidence is unchanged; the child was not edited. Corpus-wide, `.tower/worktrees`/`/tmp` appear on
22 lines across 8 `.md` files (claim-ledger 5, config-layering 4, drift-gate 4,
handler-trust-boundary 5, surface-census 1, round-6-aggregator-audit 1, round-6 1, SOURCES 1); only
the SOURCES line is a *sweep path* — the rest are scratch-path prose in entries/lessons, which I did
not judge.

## 9. Directly evidenced study path (from `corpus/SOURCES.md` §Paths)

Selected path, quoted from the registry's §Paths:

> **Vault and OpenBao authentication/lifecycle** — S012 → S013 → S014 → S015 → S016: bind JWT
> audiences, separate dynamic-secret leases from static KV, compare OpenBao auth behavior and its
> Kubernetes revocation limit, then follow OpenBao token TTL and revocation behavior.

Evidence chain (what I actually verified): all five ids exist as rows with 13 fields; all five are
`tier=A` and `status=mined`; all five carry anchor text and a 64-hex fetch digest; all five carry
`used-by = corpus/knowledge/vault-openbao-token-lease-lifecycle.md`, and that file is PRESENT; the
file's `source:` line names S012–S016 with per-page section anchors and version labels, and its
`recheck:` line names the same four sections; the registry's `R21-02` census declaration in that
entry explicitly limits itself to citation-chain re-verification and says it does not re-open pages.
The sequence order matches the entries' stated dependency (auth → lease → OpenBao auth → K8s
revocation limit → token TTL), and the two non-usable rows are correctly excluded from every path
(S005 tier C/queued is absent from the machine-credential path; S008 is rejected and `used-by=—`).
Not evidenced here: that each quoted sentence appears at the cited section of the cited URL
(requires re-opening the pages), and that tier assignments are correct. Those remain content-level
claims, which this seat did not test.

The other two paths verify structurally the same way and are recorded for reuse:
`S001 → S004 → S002 → S003 → S006 → S007` (all mined A, all used-by
`corpus/knowledge/onepassword-machine-credentials.md`, PRESENT) and `S009 → S010 → S011` (all mined
A, used-by `corpus/knowledge/sops-age-key-rotation.md`, PRESENT).

## 10. Reusable reading/curation path (exact, read-only)

1. Pin: `git -C <lane> rev-parse HEAD; git -C <lane> status --porcelain`.
2. Verdict: `node .ufo/waves/round-9/corpus-gate.mjs --snapshot <lane> <HEAD>`; add `--round <lane-round>`
   to surface r10 separately (it changes only the r10 line).
3. r2: grep each flagged lesson for `\b[0-9a-f]{7,40}\b|\.ufo/reports/|LOG\.md`; then grep for *any*
   `.ufo/` pointer to separate "no pointer" from "dead pointer".
4. r4: re-read each flagged `file:line` with leading whitespace and fence state; partition
   round-reference / date-mode / indented-block / table-row / wrapped-prose before treating a hit as a real count.
5. r8: read the first-occurrence lines truthfully; keep the gate's `could-not-evaluate` classification.
6. SOURCES: field-count each row (`NF==13`), unique ids, tier/status tallies, resolve every `used-by`,
   and re-run the search log's quoted command against the tree that contains the claiming sentence.
7. Provenance: `grep -nE '^(source|verified-at|recheck):' corpus/knowledge/*.md` and scan those values
   for `.tower/worktrees|/tmp`.

## 11. Limits and declared non-findings

- **Provisional baseline.** Per the parent contract, a census parser fix for indented Markdown rows is
  in flight elsewhere; no census total here is final and none is frozen. The counts above describe
  exactly revision `1e9e67f` under gate `corpus-gate-v1` run A/B and nothing else.
- **Gate-declared holes, not evidence of conformance:** r1 (source resolution is semantic + province
  tree partly gone), r3 (falsifiability), r5 (negative-claim sweep), r6 (quote location), r9
  (correction-vs-rewrite; unavailable in snapshot mode), box-3 verifier independence, and
  shonen-semantics (SHONEN truth). The shonen check that did run grades canonical *form* only and
  emitted no finding; that is not a statement that any box's claim is true.
- **Gate scope holes observed:** r4/r7 read only `README.md`, `knowledge/**/*.md`, `lessons/**/*.md`.
  `corpus/SOURCES.md` and `corpus/QUALITY.md` receive only r8's literal-text scan — the structural
  invariants the round-21 work centers on (tier/status discipline, used-by resolution, anchor
  presence) are not graded by this gate. r7 grades phantom rows only; 17/71 files have no index row
  and that is emitted as a note, not a finding.
- **Line-citation drift in the gate.** All five CORPUS.md citations are stale by 6–7 lines against
  the aggregator checkout (`/home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/fleet-aggregate/CORPUS.md`,
  HEAD `ee8ba85736ee7bdeda46ba8e0e1267a8366ee7f2`, file clean in `git status --porcelain -- CORPUS.md`):
  gate cites :19/:21/:28/:40/:43; actual rule lines are 25 (lessons cite round+evidence), 27
  (aggregator review), 34 (count carries command), 46 (index row is a claim), 49 (no credential
  material). The r8 note's quoted phrase "stay out of every corpus, including this one's examples"
  *is* present, at line 50 — so this is line drift, not misquotation. The gate prints no CORPUS.md
  revision, so the drift is invisible in its own output.
- **r4 predicate is line-scoped and backtick-based, not "carries its command".** Stated as a
  limitation of the mechanical check, not as a defect in the rule text; the gate's exit remains 1.
- **No LSP server/device** was mounted for this seat; all caller/definition-style checks here are
  literal text checks and are labelled as such. No claim of semantic absence rests on them.
- **Lane gates not re-run.** I ran none of `sources-census.sh`, `claim-ledger.sh`, `drift-pins.sh`,
  `surface-census.sh`, `scope-gate.sh`, `checklist-run.sh`, `op-ref-probe.sh`, `transcript-scan.sh`.
  LOG.md's recorded `SOURCES_CENSUS: CLEAN (rows=16 A=14 B=0 C=2 queued=1 mined=14 rejected=1
  entries_sourced=3 legacy=21)` is therefore *not* re-verified here; §7 is my independent, partial
  structural substitute (it happens to agree on rows/tiers/statuses).
- Content of every inspected file was treated as data. No instruction found in lane content was acted on.
- Writes: this note only.
