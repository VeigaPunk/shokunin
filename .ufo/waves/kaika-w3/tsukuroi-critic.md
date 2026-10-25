# W3 critic — tsukuroi, steered round 1

Read-only review of report claims A–C. I did not edit, stage, or commit lane material. This is nonbinding review input, not the integrator’s closure verdict.

## A — adjacency 7→8

- **Strongest counterexample:** `jq '[.routes[]|select(has("state"))]|length' corpus/knowledge/adjacency-handoffs-fleet-r1.json` returns **7**. The exact companion command below lists six `contract-only` labels and one `prepared` label, while the prepared-packet command returns **1**. These are route declarations, not seven exercised cross-domain handoffs.

  ```sh
  jq -c '[.routes[]|.id+":"+.state], .source_pin_recheck.current_match_count, .source_pin_recheck.anchors_hold_count' corpus/knowledge/adjacency-handoffs-fleet-r1.json
  jq '[.routes[]|select(.state=="prepared")]|length' corpus/knowledge/adjacency-handoffs-fleet-r1.json
  ```

- **Evidence:** `corpus/knowledge/adjacency-recheck-2026-10-19.md:42-50` says only ADJ-04 has a packet; `corpus/knowledge/adjacency-handoffs-fleet-r1.md:74-85` says it remains `prepared`, with acknowledgement/acceptance/resolution unobserved. The packet observation predates this round; `git diff 9b70381 549ec0c -- corpus/knowledge/adjacency-handoffs-fleet-r1.md` shows only an appended `Contract keys` block, not a new observation. The report/scorecard correctly make the move conditional on the fleet report being committed; until that transition, it is pending.
- **Stale point-in-time premise:** the pin loop in `before.md:141-166` already re-hashed sibling declarations and returned five matches; `after.md:58-67` recorded the same five matches. Re-running that exact loop now returns four matches and four drifts, adding `tameshi-shokunin` to the drift set. Its committed `PROVINCE.md` lines 3–18 still contain the cited method anchor; the changed material is appended after those lines. Thus the old snapshot is not false, but is no longer current for a later handoff. The receipt sweep `grep -rn 'TSUKUROI-F1-MEM-01' /home/vgpnk/Projects/shokunin/*-shokunin --include='*.md' --include='*.json' | grep -v '^/home/vgpnk/Projects/shokunin/tsukuroi-shokunin' | wc -l` returned **0** sibling receipts.
- **Impacted axes:** adjacency; freshness of the sibling-pin snapshot.
- **Smallest safe correction:** keep the lifecycle vocabulary, but base adjacency credit on the one source-backed packet once the report is actually committed—not on the count of state keys. Append a new pin/hash snapshot before relying on the now-drifted tameshi pin; preserve the old snapshot. Do not infer recipient acceptance.

## B — coverage 8→9 + `sources-registry`

- **Strongest counterexample:** the README row count is not itself a coverage fraction. The exact command in `after.md:75-78` counts **10** at base and **15** at `549ec0c`; those added rows comprise the new domain-note rows at `corpus/README.md:17-20` plus A’s adjacency-recheck row at `:21`. The raw file-search measures are mention/file counts, not independent coverage proof, and can rise from cross-claim references.

  ```sh
  git -C /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/tsukuroi-shokunin show 9b70381:corpus/README.md | grep -c '^| `'
  git -C /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/tsukuroi-shokunin show 549ec0c:corpus/README.md | grep -c '^| `'
  ```

- **Evidence against a substantive failure:** the new domain notes contain source-headed, bounded host findings, rather than empty index padding. The exact frozen census commands in `SOURCES-CONTRACT-v1.md:68-80` were re-run; `bash /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/fleet-census/scripts/sources-census.sh validate /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/tsukuroi-shokunin` returned `tsukuroi-shokunin ok`. The row command `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` returned **34**; malformed-row `awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ && NF!=13 {n++} END{print n+0}' corpus/SOURCES.md` returned **0**. The tier histogram command from contract line 72 returned A=31/B=1/C=2; the status histogram command from line 74 returned mined=26/queued=5/rejected=3. Duplicate-ID, enum, missing-used-by, and reverse-citation checks emitted no findings.
- **Independent source re-opens (sample):** S002’s article body contains “If you configured the systemd hook and unlock LUKS partitions”; S010’s “Avoid certain pacman commands” says “never run pacman -Sy; instead, always use pacman -Syu.” S020’s unit has `CapabilityBoundingSet=CAP_SYS_ADMIN`. The Arch Security Tracker S029 row shows “257.6-1” and “Vulnerable” for systemd, but does not map the issue to the installed version or give its fixed range; that supports the row’s narrow rejection reason, not a claim that the host is safe. S034 `access(2)` matches the permitted-capability quote in its DESCRIPTION paragraph. No sampled quote/provenance contradiction found.
- **Possible no-harm counterexample:** `SKILL.md:1643-45` names `checkupdates` as the safe upstream check while stating `pacman-contrib` is absent. Re-running `pacman -Q pacman-contrib` returned “package ... was not found” (exit 1); the checklist gives no explicit unavailable-helper branch. `corpus/knowledge/pacnew-plane.md:19` records the same absence. This is a possible operability regression, not a source fact error—the absence is disclosed.
- **Impacted axes:** coverage; possible operability risk; the row metric partially overlaps adjacency.
- **Smallest safe correction:** make the coverage claim independently on the new domain-note rows; identify the README row for A as outside B’s count, and treat keyword sweeps as discovery evidence only. If `checkupdates` is absent, explicitly report the upstream package delta as unknown rather than suggesting installation or substituting bare `-Sy`. Preserve the verified registry/census work.

## C — freshness 8→9

- **Strongest counterexample:** the recheck-presence command below returns **25**, but it checks for a matching date/cadence string, not that each procedure was run. Likewise, `grep -L '^source:' corpus/knowledge/*.md | wc -l` returning **0** only proves a matching line exists; for legacy notes the line is inside an appended `## Contract keys` block, not opening metadata. The lesson explicitly preserves original `verified-at` dates unless a block names a current rerun (`corpus/lessons/round-1.md:75-79`).

  ```sh
  for f in $(git ls-tree --name-only 9b70381 corpus/knowledge/ | grep '\.md$'); do grep '^recheck:' "$f" | tail -1 | grep -qE '[0-9]{4}-[0-9]{2}-[0-9]{2}|\b[0-9]+d\b|on-release' && echo ok; done | wc -l
  for k in source verified-at recheck; do echo "no-$k $(grep -L "^$k:" corpus/knowledge/*.md | wc -l)"; done
  ```

- **Evidence of real freshness work:** `grep -lE '^## Erratum \(2026-10-19, fleet round 1\) — D[1-5]' corpus/knowledge/*.md | wc -l` returns **7**; those notes do contain dated source/host rechecks. The baseline archive replay of the metadata command returned source=6, verified-at=11, recheck=11 and the base recheck-presence loop returned **0**; the current metadata command returns 0/0/0 and the current base-note recheck-presence command returns **25**. These are valid contract-key repairs, but not equivalent to fresh verification of every legacy note.
- **Concrete documentation defect:** `SKILL.md:1646-48` reports package transaction and install counts, but supplies a command only for the zero-upgraded count. Independent read-only counts from `/var/log/pacman.log` were:

  ```sh
  awk 'NR>=2287 && /\[PACMAN\] Running .pacman -S / {n++} NR>=2287 && /\[PACMAN\] Running .pacman -Rns / {n++} END{print n+0}' /var/log/pacman.log       # 7
  awk 'NR>=2287 && /\[ALPM\] installed / {n++} END{print n+0}' /var/log/pacman.log                                               # 64
  awk 'NR>=2287 && /\[ALPM\] upgraded/ {n++} END{print n+0}' /var/log/pacman.log                                                 # 0
  awk 'NR>=2287 && /\[PACMAN\] Running .pacman .* -Su/ {n++} END{print n+0}' /var/log/pacman.log                                 # 0
  ```

  The evidence is sound, but `CORPUS.md:33-38` requires each number to carry its command.
- **Impacted axes:** freshness; a small operability/reportability risk from missing command anchors.
- **Smallest safe correction:** count the actually re-verified erratum notes as freshness evidence; label cadence/header work as contract repair, not fresh checks. Append the missing host-log commands in a correction rather than rewriting the filed skill text.

## Review recommendation

Nonbinding: keep A pending until the report-to-`reported` transition lands and refresh its pin snapshot before reuse; B has no sampled source-admission defect but should isolate its domain-note rows from A’s row; C’s errata remain useful, while metadata presence must not be presented as re-verification. These are fixable evidence/attribution issues, not evidence that the underlying knowledge should be deleted. I leave the global admit/reject decision to the integrator.

## Verification boundary

I did not rerun `tools/tsukuroi-census.sh --selftest`: its own help says it writes under `/tmp/tsukuroi-r3-2-selftest.*` (`tools/tsukuroi-census.sh:441-446`), outside the assigned scratch directory. This does not affect the independent source-census validation or the claim counters above.