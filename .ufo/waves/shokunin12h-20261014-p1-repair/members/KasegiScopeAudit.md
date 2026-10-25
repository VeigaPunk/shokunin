# KasegiScopeAudit — baseline scope audit

Advisory only. Not a native judge verdict, not a lane round report, not a receipt, and not an admission. Lane tree was read-only. No gate script was executed (`resolve.py` writes `citation-survival.md`; parent owns gate runs after integration). No build, lint, test, or formatter.

Measured revision: `d1e6e8f3931a2bfbeb4319b9b41980c1e801e9f1` (matches `baselines.json` kasegi.head). Worktree dirty only as `?? plans/`. `KASEGI_MIRROR`, `KASEGI_ORIGIN_ROOT`, `KASEGI_LANE_ROOT`, and `UFO_SRC` were unset in this process.

Axes applied: freshness, operability, calibration, adjacency.

## What the captured gate actually covers

`evidence/kasegi-before.json` ran `python3 corpus/instruments/anchorcheck.py SKILL.md` at that revision, exit 0, summary `7 in-range / 0 bad / LOST-RECORDED=306 / BASE-ABSENT=0`. That matches `SCORECARD.md:134`. It does not cover corpus files, `resolve.py`, semantic support, or any path the `CITE` regex does not recognize.

The seven recognized non-lost `SKILL.md` anchors are all lane-internal:

- `SKILL.md:120` → `corpus/knowledge/program-quirks.md:10` (fee gate). Supports the parenthetical.
- `SKILL.md:132` → `corpus/knowledge/policy-access-playbook.md:13` (terms-gated SIX). Supports the row.
- `SKILL.md:338` → `corpus/knowledge/ops-invariants.md:24` (`gitMutationBlocker`). Supports the lost-tree sentence.
- `SKILL.md:416` → `corpus/knowledge/intake-and-finalize.md:78-92` (finalize filter/tag span). Supports the lost-tree sentence.
- `SKILL.md:696-697` → `corpus/knowledge/ufo-archive-2026.md:150-154` and `:145-149`. Support the two table rows.
- `SKILL.md:821` → `corpus/knowledge/mission-control.md:3` (lost `fleet-dispatch.mjs` recorded as 427 lines). Supports that historical count.

Those seven are not evidence that external or historical anchors were re-opened.

Province roots remeasured this pass, all `ABSENT`: `~/Projects/bounties`, `~/Projects/the-bounty-hunter`, `~/Projects/origin-work` (including `open-bug-bounties`, `the-bounty-hunter`, `ufo-fsd-alpha`), `~/Projects/open-bug-bounties`. `find ~ -maxdepth 5` for `*bount*` / `*bug-bount*` outside this lane printed nothing. `~/Projects/ufo-fsd-alpha` is `PRESENT`, `HEAD` still `964f443ee53df0ce06bd689af01f0dea031b01f9`. `scripts/ufo-sighting.mjs` exists (210188 bytes). Copies of the ufo skill are 600 lines (`.cursor/skills/ufo/SKILL.md`, `.omp/skills/ufo/SKILL.md`, `skills/ufo/SKILL.md`, and the package copies). `.ufo/missions/` is still absent, so the `hunt-*` dangling claim still holds. The worktree is not clean: `M README.md`, `M config/ufo.json`, `M crates/ufo-core-runtime/bundled/config.json`, `M crates/ufo-core-runtime/bundled/omp-seat-routing.json`, `M scripts/fleet-dispatcher.test.mjs`. Those names were not content-read.

## Findings

### 1. High — explicit-prefix override does not re-point the gate

`anchorcheck.py:26-31` and `:36-41` say the checked base is `$KASEGI_ORIGIN_ROOT` / `$KASEGI_MIRROR`, else the first existing candidate. `SCORECARD.md:159-160` says restoring the mirror and setting `$KASEGI_MIRROR` re-points the gates without edits.

The implementation does not join the derived root. Explicit cites always expand the literal prefix:

- `anchorcheck.py:165-167` — `path = os.path.realpath(os.path.expanduser(rel))` for `~/Projects/origin-work/open-bug-bounties/…`
- `anchorcheck.py:180-182` — same for `~/Projects/the-bounty-hunter/…`

The derived root is only a confinement boundary. A logic copy of that branch, pointed at a temporary tree that actually contained `claim-packages/queue.json`, classified `~/Projects/origin-work/open-bug-bounties/claim-packages/queue.json` as `OUTSIDE-BASE`. The file existed under the derived root and did not exist at the expanded literal path.

On this host, with both candidates absent and no override, an unmarked explicit cite is `BASE-ABSENT` rather than `OUTSIDE-BASE`. The mis-verdict is latent until the documented override or the second candidate (`~/Projects/open-bug-bounties`, `~/Projects/origin-work/the-bounty-hunter`) exists. The contract text is false now.

`resolve.py` has the same split: `$KASEGI_MIRROR` is joined only for bounty-prefix and relative fallbacks (`resolve.py:174-188`). An absolute `~/Projects/the-bounty-hunter/…` cite is domain `other` and uses `exists_any` on the literal path (`resolve.py:178-180`). There is no `KASEGI_ORIGIN_ROOT` in `resolve.py`.

Proposed delta (GateRepair, narrow): for an explicit prefix, strip the literal prefix and join the suffix onto the derived root, then confine. Do not treat a second-candidate directory as the frozen mirror or the origin repo without a HEAD check (`1cfbd86` / `1307b8b`). An explicit bad override must stay bad (current `_derive_root` already returns the override without falling through; keep that).

### 2. High — restore unblock cannot re-check `[lost-base]` / `[lost-tree]` anchors

`anchorcheck.py:231-234` counts a lost prefix as `LOST-RECORDED` and `continue`s before any root is consulted. `citation-bases.md:62-65` says that is intentional. `SCORECARD.md:156-160` then says any checkout of `1cfbd86` plus `$KASEGI_MIRROR` satisfies the anchors without edits. That unblock is false: the 306 `SKILL.md` lost anchors stay "not checked" until the prefixes are removed. Removing them is an edit. A restored tree therefore does not move `bad` or `BASE-ABSENT` for the marked set.

Proposed delta (RecordPrep, not a silent gate behavior change): rewrite the `MIRROR-SOURCE-LOST` unblock to say the prefixes must be stripped, or a separate re-open mode must be added, before the gate will range-check them. Do not make lost prefixes resolve by default; that would collapse the historical/live boundary the vocabulary exists to keep.

### 3. High — `$UFO_SRC` derivation is claimed and absent

Still-live claims:

- `LOG.md:800-802` — "`$UFO_SRC`/`ufo-fsd-alpha` candidates in anchorcheck"
- `SCORECARD.md:163-165` — "derived `$UFO_SRC` candidates list the new path first"
- `corpus/knowledge/root-loss-2026-10-12.md:54-56` — instruments derive `$KASEGI_MIRROR` / `$KASEGI_ORIGIN_ROOT` / `$UFO_SRC`

Search of `kasegi-shokunin` for `UFO_SRC` hits only those prose files. `anchorcheck.py` candidates are the bounty-hunter and open-bug-bounties paths (`:75-82`). The `CITE` regex (`anchorcheck.py:104`) does not match `~/Projects/ufo-fsd-alpha/`. An independent token walk found 14 backtick tokens containing `ufo-fsd-alpha` that the anchor regex does not recognize, including the live ones at `SKILL.md:28`, `corpus/knowledge/ufo-archive-2026.md:31`, and `corpus/knowledge/ufo-workspaces.md:171` / `:312`. Adding a derive without extending the matcher would check zero current citations. That would be a manufactured repair.

The live existence claims that were remeasured still hold: relocated tree present, HEAD unchanged, sighting script present, skill copies 600 lines, no `.ufo/missions/`. Those are not gate results.

Proposed delta (RecordPrep): retract the three `$UFO_SRC` sentences. Name the live ufo paths as resolver-visible only (`citation-survival.tsv` `RESOLVES` on the directory and on `scripts/ufo-sighting.mjs`), not anchor-gated. Cross-domain owner if a real `$UFO_SRC` fail-closed chain is wanted later: the ufo substrate / kumitate, not this lane's bounty matcher.

### 4. High — documented blob pin is not installed; in-range checks the wrong bytes

`citation-bases.md:70-75` says `SKILL.md:NNN` spans in `corpus/knowledge/triage-thresholds.md` are pinned to blob `fc6d398`, and that `anchorcheck.py` reads `<!-- pin: SKILL.md fc6d398 -->`. A search for `<!--\s*pin:` in the lane found no such comment. The only `pin: SKILL.md` hit is the prose instruction itself.

`anchorcheck.py` therefore resolves bare `SKILL.md:NN` against the current file (`LANE_DIRS` includes `.`). `resolve.py`'s line-anchor table does the same and reports those anchors in range (`citation-survival.md:112-140`, current file 1012 lines).

Counterexample, measured:

- `triage-thresholds.md:58` says `SKILL.md:117` MATCHES `attempts() >= MAX_ATTEMPTS` (2).
- Current `SKILL.md:117` is a lost-tree provenance cite for `claims/hackerone-anthropic/honest-zero-claude-code/provenance.json:29`. It does not say that.
- `git show fc6d398:SKILL.md` line 117 is `status-file TERMINAL + telemetry attempts()≥2` (blob length 546). That line supports the MATCHES cell.
- The same sentence now lives at current `SKILL.md:191`.

Second counterexample: `triage-thresholds.md:88-90` SUPERSEDES `SKILL.md:113-114` and `:175-176` as the queue-score formula. Current `SKILL.md:113-114` are provenance-pin lost-tree cites. Blob `fc6d398` lines 113-114 are the dispatch-ordering formula. A mechanical in-range verdict on the current file accepts the wrong text.

Bare `SKILL.md` cites in corpus markdown that `anchorcheck` would lane-hit: 43, mostly in `triage-thresholds.md`. They were not all semantically reviewed. The class is enough: no pin comment means current-file in-range is not historical support.

Proposed delta (RecordPrep): put the HTML pin comment in `triage-thresholds.md`, or re-cite every bare `SKILL.md:NN` against current lines after reading them. Do not count the census "67 in range / 0 out of range" (`citation-survival.md:105`) as semantic clearance of those pins. GateRepair should not invent a pin from prose.

### 5. Medium — scorecard rates do not match the committed census

`SCORECARD.md:134` says corpus `116/1142 = 10.16%` and lane `132/1469 = 8.99%`. The committed census of record says corpus `116/1144 = 10.14%` and lane `132/1471 = 8.97%` (`citation-survival.md:32-33`). SKILL `32/506 = 6.32%` matches. Numerator matches; corpus denominator is +2. Same HEAD, so this is transcription or a census regenerated after the sentence was written, not a new measurement. Do not re-pin the scorecard to a preferred rate.

Proposed delta (RecordPrep): quote `citation-survival.md:31-33` exactly and name the 2-citation denominator delta as transcription debt.

Related calibration hole in that same census: 7 of the 9 `RESOLVES` rows are directory or glob tokens, not external anchors (`citation-survival.tsv`): `/`, `/home`, `/home/vgpnk`, `/tmp`, `~` (scope SKILL), `~/Projects`, `~/Projects/**` (glob). Only `~/Projects/ufo-fsd-alpha` and `…/scripts/ufo-sighting.mjs` are the relocated tree. The published 9 is not 9 live external sources. `~` is inside the SKILL numerator.

### 6. Medium — live vocabulary cites the wrong resolver lines

Mechanically in range, semantically drifted. `citation-survival.md:147-150` marks all four in range.

| Cite | Claim | Bytes at that range |
|---|---|---|
| `citation-bases.md:16` → `resolve.py:164-172` | relative resolver tries only the lane root | end of `exists_any` plus start of bounty-prefix `classify`. Relative logic is `resolve.py:181-189`, and it also tries the mirror. |
| `citation-bases.md:41` → `resolve.py:161-163` | other-root rule | glob-match return inside `exists_any`. Other-root rule is `resolve.py:178-180` (docstring `:29-31`). |
| `citation-bases.md` rule 5 → `resolve.py:74` | line-anchor rule rejects comma lists | `EXTS` regex. `LINEANCHOR` is `resolve.py:76`. |

`citation-bases.md:31` is the one unmarked explicit mirror anchor in live docs: `~/Projects/the-bounty-hunter/ops/rank.mjs:55-58`, used as an example of a classification that is now lost. It is not `[lost-base]`-prefixed, so `anchorcheck` would report `BASE-ABSENT`, which is not in `bad` (`anchorcheck.py:60-61`, `:269-270`). A corpus-wide anchor run would still exit with that token not failed. The vocabulary file violates its own prefix rule (`citation-bases.md:62-64`) in a way the gate cannot fail.

Proposed delta (RecordPrep): re-cite the three resolver lines; prefix the rank.mjs example or take it out of backticks.

### 7. Medium — present-tense province lead is live-false; UFO child list has drifted

`SCORECARD.md:14-18`, under "read this first", still says "Two roots survive" and names `~/Projects/the-bounty-hunter` and `~/Projects/origin-work/open-bug-bounties` as present. Round-19 (`SCORECARD.md:121-128`) and `PROVINCE.md:16-22` correct that later. The lead is what a reader hits first. `PROVINCE.md:5-15` is labeled round-15 status; the round-19 paragraph is accurate against this pass's `test -d` results. `SKILL.md:815-820` still says the mirror "resolves" the ev-report spans, inside a round-15 section, after the file header has already said the mirror is absent.

`ufo-workspaces.md:171-172` and `root-loss-2026-10-12.md:19-20` say `.ufo/` holds only `cache`, `scopes`, `sighting`, `statusline-cache.json`, `statusline-full.stamp`. This pass also found `contract-sync/` and `rs-self-iter-blocked.json`. `missions/` is still absent. The exclusivity claim is stale; the dangling-`hunt-*` negative is not.

Proposed delta (RecordPrep): mark the scorecard lead historical and point at the round-19 paragraph. Errata the `.ufo/` child list as as-of `2026-10-14T12:44Z`, not exclusive. Do not absorb the new children into kasegi. Cross-domain owner for the substrate inventory: kumitate / ufo. `ufo-workspaces.md:317-318` already routes router mechanics there; keep that refusal.

`citation-bases.md:72` tells the reader to run `git -C /home/vgpnk/projects/shokunin/kasegi-shokunin show fc6d398:SKILL.md`. That path is `ABSENT`. The lane is `/home/vgpnk/Projects/shokunin/kasegi-shokunin`. The command as written cannot resolve the pin it documents.

### 8. Lower — gate fail-open and matcher holes (missing coverage, not a current red SKILL run)

- `anchorcheck.py` `main` returns `None`, so `sys.exit` is 0 even when `bad > 0`. `BASE-ABSENT` is excluded from `bad`. Forgetting `[lost-base]` on an absent-base cite does not fail the gate. Eight unmarked bare cites in corpus markdown would be `BASE-ABSENT` today, including `root-loss-2026-10-12.md:61` `queue.json:11-12`.
- Bare names: `anchorcheck` searches `LANE_DIRS` (`:100`, `:198-205`) and will `IN-RANGE` `ops-invariants.md:18`. `resolve.py` joins only the lane root (`:181-184`) and classifies that token `GONE`. `citation-bases.md:14-16` warns about the resolver and is itself a token the anchor gate would pass. The instruments disagree, and a clean `SKILL.md` receipt hides it.
- `git_show` (`anchorcheck.py:124-126`) range-checks `split('\\n')`, which is one past the last real line when the blob ends in a newline. The live-file path uses an iterator count (`:222-224`). Latent `IN-RANGE(PIN)` one line past EOF. No pin comment is installed, so this is not currently exercised.
- No HEAD identity check when a candidate directory exists. Path presence is treated as the frozen mirror. Latent while those paths are absent.
- `SKILL.md:976-1012` lists `~/Projects/bounties/…` without in-token `[lost-tree]` prefixes. The section header says they are lost. The anchor regex does not see most of them (no `:line`, or braces). Gate-invisible, prose-covered. Not a live-open claim if the header is read.
- `CORPUS.md` requires `source:`, `verified-at:`, and `recheck:` on knowledge entries. None of the 25 `corpus/knowledge/*.md` files carry that full header. Pre-existing record-contract gap, not a gate defect. Not a reason to invent headers this wave.

## Unresolved debt

- `RECEIPT-STORE-LOST` and `MIRROR-SOURCE-LOST` (`SCORECARD.md:150-160`) remain real. Unblock text for the mirror override is wrong (findings 1 and 2). Restoring a tree still does not make `[lost-base]` anchors openable to the gate.
- `ORIGIN-REPO-LOST` unblock ("none needed; `$UFO_SRC` is derived") is false (finding 3). Live ufo existence was remeasured; it is not gate-covered.
- Planned Airtable severity/decree comparison (`SCORECARD.md:167-174`) was not done. Both the lost-tree package and the origin-work package that "materially differs" are absent. The `[lost-tree]` anchors were not re-verified. Do not replace them with circular corpus cites to raise the fraction. Unblock: operator restores `open-bug-bounties` or declares the claims permanently attested. Same L0 row already in `.ufo/l0-questions.md` (kasegi round-15). Province re-point remains an operator decision; this audit does not re-scope.
- Census self-check shell in `citation-survival.md:80` globs `corpus/*/*.md`, which includes the generated report that `resolve.py` excludes (`GENERATED_REPORT`). Not re-run. Do not treat that pipeline as a second measurement of `1471`.

## Cross-domain owners

| Item | Owner |
|---|---|
| Explicit-prefix join onto the derived root; keep bad overrides bad | KasegiGateRepair, only if parent accepts a code change. Docstring and scorecard are already falsified. Current host does not mis-open a file today. |
| Retract `$UFO_SRC` sentences; fix mirror unblock; install or drop the `fc6d398` pin; quote the committed census; mark the scorecard lead historical; fix the lowercase `projects` path; prefix `citation-bases.md:31` | KasegiRecordPrep. This seat did not edit those files. |
| New `.ufo/` children; any real `$UFO_SRC` fail-closed chain | kumitate / ufo substrate. Kasegi should errata, not absorb. |
| Province re-point and permanent attestation of lost receipt claims | Operator, existing L0 row. |

## Residual risk and verification gaps

- Official `anchorcheck.py` / `resolve.py` were not re-run. The before receipt is the gate evidence. Independent classification used the same `CITE` / `LOST` patterns in a separate process.
- Semantic review covered the seven live `SKILL.md` anchors and the pin counterexamples, not the 306 lost anchors and not all 43 bare `SKILL.md` cites.
- UFO dirty-file contents were not read. Credentials were not opened.
- Gate files were unmodified at report time (`HEAD` still `d1e6e8f`, status still only `?? plans/`). This is the baseline inventory, not a post-integration acceptance pass.
