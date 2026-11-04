# Tsukuroi round80 — honest stop

## Work performed

Declared **C1 depth**:42 pinned service-restart cells with a digest-bound review,
0→42. **C2 operability**:two named gates with public selftests and byte-bound
receipts,0→2. C1 verifies; **C2 misses (0→1)** because its frozen lookup invents
a different registry label. Overall **not admitted / honest stop**, no target
narrowing or counter rewrite. Lowest non-retired depth8 is worked; no ordinal uplift.

- Added the six-cause × seven-setting upstream Restart= matrix, conditional on stops,
  oneshot, clean statuses, main-process overrides and start limits; S330 and final
  byte-bound reviewer file: `corpus/knowledge/service-restart-matrix-r80.md`,
  `.json`, `.ufo/waves/round-80/w1/ReviewMatrix/verdict.json`.
- Repaired `tools/count-kr-rows-r69.py` and `tools/check-transaction-order-r39.py`
  with real public-CLI selftests; final-source main rerun10/10 and9/9 rc0.
  Executor red controls rc3; receipts in `w1/ExecKR/` and `w1/ExecTransaction/`.
- Froze predicate/counter/expected/source and executed11 pre-data controls before
  seats existed (`before/controls.json`, freeze61ec89ec). Positives were synthetic;
  the C2 row-name mismatch they hid remains an honest miss.
- Real domain task: four read-only commands, all rc0; system failed units0,
  user failed scopes2; journald Restart=always, dbus-broker Restart=no,
  both Result=success/NRestarts0. No cause or future restart inferred;
  `w1/ExecHost/handoff.md`. No package transaction, restart or remediation.
- Mined r79's omitted null-output binding failure, current wrong-label control,
  reviewer-caught draft contradictions and isolation issue into the lesson and
  QUALITY111/112 (`corpus/lessons/round-80.md`). R79 stays rejected.
- One v1 wave10: executor3/scribe2/scout1/connector1/reviewer1/critic1/mutation-tester1;
  attack allocation3/10, actual delivered reviewer1; **8 delivered,2 dead**, residual0.
  L1 planner was declared before dispatch (validator forbids spawning planner).
  WAVE-DONE received before this report. Results have null outputs after kernel
  restart; seat files bind evidence; no votes reconstructed (`after/settlement.json`).

All wave pointers above are beneath `.ufo/waves/round-80/` in the lane.

## Landed changes

Final pushed lane hash **cdcab9f3a6c1046919b84503b7c02935c3a49410**; `git ls-remote origin refs/heads/master`
printed that exact hash. No inherited uncommitted work at entry.

| Landed commit | Changes | Matching LOG.md entry |
|---|---|---|
|61ec89ec6e6f284b6fba2127721359e6931a5789|counter, expected matrix, raw source, pre-data controls, declaration|Round80 motivating evidence and pre-data freeze|
|aad05ef173176cf5223f7c315297240c2db1abe2|validated10-seat spec, dispatch and registry|same motivating/freeze entry, planned wave evidence|
|160b8889703dd22b38c89368871f27517af02c1f|reviewed knowledge/S330, two repaired tools, truthful registry, QUALITY/lesson/index and wave files|Round80 integration after WAVE-DONE|
|cdcab9f3a6c1046919b84503b7c02935c3a49410|revision-bound receipts, frozen-miss outcome, structural/source counts and dead-seat evidence|Round80 revision-bound measures and honest stop|

C2 keeps the established `transaction-order-r39` row name. No duplicate or renamed
row was created just to satisfy `check-transaction-order-r39` in the frozen reader.
The new counter's own helper-only absent-reader selftest is **gate-standard debt**,
explicit in its registry; neither that nor the remaining inherited gates is
claimed conformant. PROVINCE/SHONEN and operator-owned input remain untouched.

## Before → after measurements

Base **467a9b7891a5939dab8460ec6f591fbb16bd82e9**; measured implementation
**160b8889703dd22b38c89368871f27517af02c1f**. Exact argv/output/rc and working
directory: `.ufo/waves/round-80/after/commands.json`.

|Claim|Counting command from lane root, substitute each revision|Before|After|Verdict|
|---|---|---|---|---|
|C1 depth|`python3 tools/measure-round80.py --revision <REV> --claim C1`|count0,target42,rc1|count42,target42,met,rc0|verified author-side; depth8→8|
|C2 operability|`python3 tools/measure-round80.py --revision <REV> --claim C2`|count0,target2,rc1|count1,target2,gate-standard,rc1|not verified; operability9→9|

C1 review binds JSON SHA05abbf14… and final companion81006519…; six holds.
The source digest and frozen instrument SHA688766756d0fb73ffb8f1d746e3377d58532bd4afa0a3aa92489c61165614d1d
are unchanged. Equality/digest arithmetic is not semantic entailment or authenticity:
a fully fabricated complete binding bundle can still pass. Per-source review
remains a separate kill rule. C2 receipts are static evidence, not execution by
its counting tool. Its actual-label miss is not rescued by the working selftests.

Main verification, once after integration: selftests from a selective exact-revision
external export (not Git-writing tests in the lane), KR10/10 and transaction9/9,
rc0. Supporting gates at measured revision: registry120/120/findings0 rc0;
knowledge references98 notes/dangling0 rc0; line endings403 files/violations0 rc0.
Header gate rc1 keeps exactly two inherited findings in r71/r72 notes;
`after/header-debt-continuity.json` proves both bytes unchanged from base.
No new-note header finding. These bounded checks are not a universal no-harm proof.

## Sources & frontier

SOURCES329→330; A312→313,B6 unchanged,C11 unchanged; mined291→292,
queued5/rejected33 unchanged. **Added S330:A/docs/mined**, opened2026-11-04;
row supports the admitted companion and matrix. Existing-row status/recheck/used-by
old→new:none. Source table command used: `git show <REV>:corpus/SOURCES.md`,
then spacing-tolerant `^ {0,3}\|\s*S[0-9]{3,}\s*\|` row selection and tier/status
cell histograms; exact base/after populations in `before/source-counts.json`
and `after/structural.json`. No frontier row advanced, capability or scope transfer.

Gate holds one admit and four retained reject candidates with located≤25-word
quotes, reasons and flips; `corpus/lessons/round-80.md`. Scout re-fetched pinned
source and independently read42/42 cells. Reviewer is author-side; the required
outside admit/reject check remains for closure.

Assimilation:none. Package and promotion remain operator-held; staged S330 names
an own-work mirror capture, not this document; no package bytes/rows adopted and
no arithmetic renumbering. Mined exactly one latest still-unimplemented reflection:
`considerthese/2026-10-26.md` burst-aware reading, QUALITY112. Connector's claim
that other already-covered proposals were unimplemented was not adopted.
ADJ06/OUT009 kaidoku/revenger ownership arbitration remains open and untouched.

Canonical command both times:
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tsukuroi`

Start output (exit0; durable `before/census.txt`):
```text
tsukuroi	W04	S038 duplicate url man.archlinux.org/man/access.2 across scopes
tsukuroi	W04	S041 duplicate url man.archlinux.org/man/systemd.exec.5 across scopes
tsukuroi	W04	S042 duplicate url github.com/omacom/omarchy/issues/8047 across scopes
tsukuroi	W04	S043 duplicate url github.com/omacom/omarchy/issues/6629 across scopes
tsukuroi	W04	S044 duplicate url man.archlinux.org/man/systemd.exec.5 across scopes
tsukuroi	W04	S046 duplicate url man.archlinux.org/man/systemd.exec.5 across scopes
tsukuroi	W04	S049 duplicate url man.archlinux.org/man/pacman.8 across scopes
tsukuroi	W04	S058 duplicate url gitlab.archlinux.org/archlinux/mkinitcpio/mkinitcpio/-/raw/v42.2/init across scopes
tsukuroi	W04	S082 duplicate url git-scm.com/docs/git-rev-parse/2.56.0 across scopes
tsukuroi	W04	S087 duplicate url archlinux.org/news across scopes
tsukuroi	W04	S089 duplicate url man.archlinux.org/man/pacman.8 across scopes
tsukuroi	W04	S090 duplicate url man.archlinux.org/man/pacman.8 across scopes
tsukuroi	W04	S092 duplicate url wiki.archlinux.org/title/System_maintenance?oldid=885170 across scopes
tsukuroi	W04	S095 duplicate url gitlab.archlinux.org/archlinux/mkinitcpio/mkinitcpio/-/merge_requests/482 across scopes
tsukuroi	W04	S098 duplicate url gitlab.com/Zesko/limine-entry-tool/-/raw/master/install/arch-linux/limine-mkinitcpio-hook/usr/lib/initcpio/hooks/btrfs-overlayfs across scopes
tsukuroi	W04	S105 duplicate url archlinux.org/news/update-to-ca-certificates-mozilla-31311-1-to-prevent-man-in-the-middle-attacks across scopes
tsukuroi	W04	S106 duplicate url man.archlinux.org/man/pacman.8 across scopes
tsukuroi	W04	S107 duplicate url man.archlinux.org/man/pacman.8 across scopes
tsukuroi	W04	S108 duplicate url wiki.archlinux.org/title/Downgrading_packages?oldid=887421 across scopes
tsukuroi	W04	S109 duplicate url gitlab.archlinux.org/archlinux/mkinitcpio/mkinitcpio/-/raw/v42.2/functions across scopes
tsukuroi	W04	S111 duplicate url gitlab.archlinux.org/archlinux/packaging/packages/plymouth/-/raw/26.134.222-3/plymouth.initcpio_hook across scopes
tsukuroi	W04	S126 duplicate url raw.githubusercontent.com/systemd/systemd/v262/man/oomd.conf.xml across scopes
tsukuroi	W04	S136 duplicate url raw.githubusercontent.com/systemd/systemd/v262/man/systemd.resource-control.xml across scopes
tsukuroi	W04	S137 duplicate url raw.githubusercontent.com/systemd/systemd/v262/man/systemd-oomd.service.xml across scopes
tsukuroi	W04	S138 duplicate url raw.githubusercontent.com/torvalds/linux/v7.2/Documentation/admin-guide/cgroup-v2.rst across scopes
tsukuroi	W04	S149 duplicate url raw.githubusercontent.com/torvalds/linux/v7.2/mm/oom_kill.c across scopes
tsukuroi	W04	S155 duplicate url raw.githubusercontent.com/kdave/btrfs-progs/v7.1/Documentation/mkfs.btrfs.rst across scopes
tsukuroi	W04	S158 duplicate url raw.githubusercontent.com/torvalds/linux/v7.2/fs/btrfs/sysfs.c across scopes
tsukuroi	W04	S182 duplicate url raw.githubusercontent.com/torvalds/linux/v7.2/mm/oom_kill.c across scopes
tsukuroi	W04	S184 duplicate url raw.githubusercontent.com/systemd/systemd/v262/man/systemd-oomd.service.xml across scopes
tsukuroi	W04	S185 duplicate url raw.githubusercontent.com/torvalds/linux/v7.2/Documentation/accounting/psi.rst across scopes
tsukuroi	W04	S203 duplicate url man7.org/linux/man-pages/man3/errno.3.html across scopes
tsukuroi	W04	S204 duplicate url man7.org/linux/man-pages/man3/errno.3.html across scopes
tsukuroi	W04	S217 duplicate url gitlab.archlinux.org/pacman/pacman/-/blob/54d9411/lib/libalpm/trans.c across scopes
tsukuroi	W04	S221 duplicate url gitlab.archlinux.org/pacman/pacman/-/blob/54d9411/lib/libalpm/util.c across scopes
tsukuroi	W04	S222 duplicate url gitlab.archlinux.org/pacman/pacman/-/blob/54d9411/lib/libalpm/trans.c across scopes
tsukuroi	W04	S223 duplicate url gitlab.archlinux.org/pacman/pacman/-/blob/54d9411/lib/libalpm/hook.c across scopes
tsukuroi	W04	S224 duplicate url gitlab.archlinux.org/pacman/pacman/-/blob/54d9411/doc/alpm-hooks.5.asciidoc across scopes
tsukuroi	W04	S226 duplicate url gitlab.archlinux.org/pacman/pacman/-/blob/54d9411/doc/alpm-hooks.5.asciidoc across scopes
tsukuroi	W04	S230 duplicate url gitlab.archlinux.org/pacman/pacman/-/blob/54d9411/lib/libalpm/add.c across scopes
tsukuroi	W04	S260 duplicate url docs.python.org/3.13/using/windows.html across scopes
tsukuroi	W04	S265 duplicate url learn.microsoft.com/en-us/windows-server/administration/windows-commands/sc-query across scopes
tsukuroi	W04	S280 duplicate url gitlab.com/Zesko/limine-entry-tool/-/raw/master/install/arch-linux/limine-mkinitcpio-hook/usr/lib/initcpio/hooks/btrfs-overlayfs across scopes
tsukuroi	W04	S281 duplicate url gitlab.archlinux.org/archlinux/packaging/packages/plymouth/-/raw/main/plymouth.initcpio_hook across scopes
tsukuroi	W04	S283 duplicate url api.github.com/repos/systemd/systemd/releases/tags/v262 across scopes
tsukuroi	W04	S294 duplicate url raw.githubusercontent.com/torvalds/linux/v7.2/Documentation/admin-guide/tainted-kernels.rst across scopes
tsukuroi	W04	S322 duplicate url raw.githubusercontent.com/systemd/systemd/v262/src/core/transaction.c across scopes
tsukuroi	W04	S323 duplicate url raw.githubusercontent.com/systemd/systemd/v262/man/journald.conf.xml across scopes
tsukuroi	W04	S325 duplicate url raw.githubusercontent.com/systemd/systemd/v262/src/journal/journald-manager.c across scopes
tsukuroi	W04	S327 duplicate url raw.githubusercontent.com/systemd/systemd/v262/src/journal/journald-manager.c across scopes
tsukuroi	W04	S328 duplicate url raw.githubusercontent.com/systemd/systemd/v262/man/journalctl.xml across scopes
tsukuroi	W04	S329 duplicate url raw.githubusercontent.com/systemd/systemd/v262/man/systemd.unit.xml across scopes
tsukuroi	ok	/home/vgpnk/Projects/shokunin/tsukuroi-shokunin/corpus/SOURCES.md

exit=0
```

End output (exit0; durable `after/end-census.txt`):
```text
tsukuroi	W04	S038 duplicate url man.archlinux.org/man/access.2 across scopes
tsukuroi	W04	S041 duplicate url man.archlinux.org/man/systemd.exec.5 across scopes
tsukuroi	W04	S042 duplicate url github.com/omacom/omarchy/issues/8047 across scopes
tsukuroi	W04	S043 duplicate url github.com/omacom/omarchy/issues/6629 across scopes
tsukuroi	W04	S044 duplicate url man.archlinux.org/man/systemd.exec.5 across scopes
tsukuroi	W04	S046 duplicate url man.archlinux.org/man/systemd.exec.5 across scopes
tsukuroi	W04	S049 duplicate url man.archlinux.org/man/pacman.8 across scopes
tsukuroi	W04	S058 duplicate url gitlab.archlinux.org/archlinux/mkinitcpio/mkinitcpio/-/raw/v42.2/init across scopes
tsukuroi	W04	S082 duplicate url git-scm.com/docs/git-rev-parse/2.56.0 across scopes
tsukuroi	W04	S087 duplicate url archlinux.org/news across scopes
tsukuroi	W04	S089 duplicate url man.archlinux.org/man/pacman.8 across scopes
tsukuroi	W04	S090 duplicate url man.archlinux.org/man/pacman.8 across scopes
tsukuroi	W04	S092 duplicate url wiki.archlinux.org/title/System_maintenance?oldid=885170 across scopes
tsukuroi	W04	S095 duplicate url gitlab.archlinux.org/archlinux/mkinitcpio/mkinitcpio/-/merge_requests/482 across scopes
tsukuroi	W04	S098 duplicate url gitlab.com/Zesko/limine-entry-tool/-/raw/master/install/arch-linux/limine-mkinitcpio-hook/usr/lib/initcpio/hooks/btrfs-overlayfs across scopes
tsukuroi	W04	S105 duplicate url archlinux.org/news/update-to-ca-certificates-mozilla-31311-1-to-prevent-man-in-the-middle-attacks across scopes
tsukuroi	W04	S106 duplicate url man.archlinux.org/man/pacman.8 across scopes
tsukuroi	W04	S107 duplicate url man.archlinux.org/man/pacman.8 across scopes
tsukuroi	W04	S108 duplicate url wiki.archlinux.org/title/Downgrading_packages?oldid=887421 across scopes
tsukuroi	W04	S109 duplicate url gitlab.archlinux.org/archlinux/mkinitcpio/mkinitcpio/-/raw/v42.2/functions across scopes
tsukuroi	W04	S111 duplicate url gitlab.archlinux.org/archlinux/packaging/packages/plymouth/-/raw/26.134.222-3/plymouth.initcpio_hook across scopes
tsukuroi	W04	S126 duplicate url raw.githubusercontent.com/systemd/systemd/v262/man/oomd.conf.xml across scopes
tsukuroi	W04	S136 duplicate url raw.githubusercontent.com/systemd/systemd/v262/man/systemd.resource-control.xml across scopes
tsukuroi	W04	S137 duplicate url raw.githubusercontent.com/systemd/systemd/v262/man/systemd-oomd.service.xml across scopes
tsukuroi	W04	S138 duplicate url raw.githubusercontent.com/torvalds/linux/v7.2/Documentation/admin-guide/cgroup-v2.rst across scopes
tsukuroi	W04	S149 duplicate url raw.githubusercontent.com/torvalds/linux/v7.2/mm/oom_kill.c across scopes
tsukuroi	W04	S155 duplicate url raw.githubusercontent.com/kdave/btrfs-progs/v7.1/Documentation/mkfs.btrfs.rst across scopes
tsukuroi	W04	S158 duplicate url raw.githubusercontent.com/torvalds/linux/v7.2/fs/btrfs/sysfs.c across scopes
tsukuroi	W04	S182 duplicate url raw.githubusercontent.com/torvalds/linux/v7.2/mm/oom_kill.c across scopes
tsukuroi	W04	S184 duplicate url raw.githubusercontent.com/systemd/systemd/v262/man/systemd-oomd.service.xml across scopes
tsukuroi	W04	S185 duplicate url raw.githubusercontent.com/torvalds/linux/v7.2/Documentation/accounting/psi.rst across scopes
tsukuroi	W04	S203 duplicate url man7.org/linux/man-pages/man3/errno.3.html across scopes
tsukuroi	W04	S204 duplicate url man7.org/linux/man-pages/man3/errno.3.html across scopes
tsukuroi	W04	S217 duplicate url gitlab.archlinux.org/pacman/pacman/-/blob/54d9411/lib/libalpm/trans.c across scopes
tsukuroi	W04	S221 duplicate url gitlab.archlinux.org/pacman/pacman/-/blob/54d9411/lib/libalpm/util.c across scopes
tsukuroi	W04	S222 duplicate url gitlab.archlinux.org/pacman/pacman/-/blob/54d9411/lib/libalpm/trans.c across scopes
tsukuroi	W04	S223 duplicate url gitlab.archlinux.org/pacman/pacman/-/blob/54d9411/lib/libalpm/hook.c across scopes
tsukuroi	W04	S224 duplicate url gitlab.archlinux.org/pacman/pacman/-/blob/54d9411/doc/alpm-hooks.5.asciidoc across scopes
tsukuroi	W04	S226 duplicate url gitlab.archlinux.org/pacman/pacman/-/blob/54d9411/doc/alpm-hooks.5.asciidoc across scopes
tsukuroi	W04	S230 duplicate url gitlab.archlinux.org/pacman/pacman/-/blob/54d9411/lib/libalpm/add.c across scopes
tsukuroi	W04	S260 duplicate url docs.python.org/3.13/using/windows.html across scopes
tsukuroi	W04	S265 duplicate url learn.microsoft.com/en-us/windows-server/administration/windows-commands/sc-query across scopes
tsukuroi	W04	S280 duplicate url gitlab.com/Zesko/limine-entry-tool/-/raw/master/install/arch-linux/limine-mkinitcpio-hook/usr/lib/initcpio/hooks/btrfs-overlayfs across scopes
tsukuroi	W04	S281 duplicate url gitlab.archlinux.org/archlinux/packaging/packages/plymouth/-/raw/main/plymouth.initcpio_hook across scopes
tsukuroi	W04	S283 duplicate url api.github.com/repos/systemd/systemd/releases/tags/v262 across scopes
tsukuroi	W04	S294 duplicate url raw.githubusercontent.com/torvalds/linux/v7.2/Documentation/admin-guide/tainted-kernels.rst across scopes
tsukuroi	W04	S322 duplicate url raw.githubusercontent.com/systemd/systemd/v262/src/core/transaction.c across scopes
tsukuroi	W04	S323 duplicate url raw.githubusercontent.com/systemd/systemd/v262/man/journald.conf.xml across scopes
tsukuroi	W04	S325 duplicate url raw.githubusercontent.com/systemd/systemd/v262/src/journal/journald-manager.c across scopes
tsukuroi	W04	S327 duplicate url raw.githubusercontent.com/systemd/systemd/v262/src/journal/journald-manager.c across scopes
tsukuroi	W04	S328 duplicate url raw.githubusercontent.com/systemd/systemd/v262/man/journalctl.xml across scopes
tsukuroi	W04	S329 duplicate url raw.githubusercontent.com/systemd/systemd/v262/man/systemd.unit.xml across scopes
tsukuroi	ok	/home/vgpnk/Projects/shokunin/tsukuroi-shokunin/corpus/SOURCES.md

exit=0
```

## Trend verdicts

- **expansion:unchanged** — existing systemd service surface deepened; no frontier
  promotion, capability or new province ground (README Round80).
- **quality:unchanged** — source-grounded new matrix and two real selftests landed,
  but no prior admitted knowledge note was superseded/reverified by this claim;
  frozen C2 misses and counter selftest conformance debt remain explicit.
- **discernment:improved** — outside r79 omission (second unreachable binding leg)
  becomes an evidence-backed lesson/QUALITY112; current control identity failure
  becomes QUALITY111. This round's outside gate-decision check is still pending.

Two dead seats: CriticCounter-2 and MutationCounter-3, exact observed error
`402 Upstream request failed: Insufficient account funds (type=server_error)`,
provider opencode-go/model deepseek-v4.1-flash. No deliverables, no replacement,
no mutant/critic kills claimed. Main supplied observed terminal status and fixed
later routing in fleet commit f7de7779; this lane changed no routing.
Actual execution-scope deviations: ScoutSource fetched additional versions/API/code
and read installed man data beyond its pinned-URL assignment; supplemental results
are not claimed as authorized scope or installed-build proof. Executor syntax
compilation exceeded the specifically named selftest/red-control commands. These
are recorded, not retroactively authorized. Review caught KR ambient-environment
and PATH inheritance before final copy; final fixed allowlist is receipt-bound.
No attributable seat-to-seat harm observed in eight delivered reports; provider
fault is not attributed to a sibling. Lost output is preserved honestly.

Stale-lane:this single-round assignment progressed through the listed commits;
no additional lane round/mission launched. Tool installs/updates:none. Scratch
`/fast/scratch/hyaku/tsukuroi-r80` removed after durable receipts. Disk guard before
main verification:tmp30%/90.7G free, scratch60%/324.8G free, status0.
Fleet-root misroot sweep (`after/fleet-status.txt`) found no identifiable round80
lane artifact; operator `.scratch`, sibling files and an unowned `after` file
were left untouched. Open L0:existing ADJ06/OUT009 arbitration and operator-held
assimilation/promotion; no new operator decision needed or question appended.

## SHONEN

- [~] Real tables/patterns/checklists/sources — SKILL.md and final service-restart note;
  author-side evidence, no non-author promotion mark.
- [~] End-to-end domain task — `w1/ExecHost/handoff.md`, LOG Round80 integration;
  four observed read-only commands and operator-boundary handoff.
- [~] Executable without oral context — explicit argv/receipts and two public selftests;
  whole-SKILL post-append independent replay remains unexecuted (SHONEN.md box3).
- [~] No cross-domain bleed — unchanged PROVINCE and ConnectorScope boundary scan;
  contested ADJ06/OUT009 remains unresolved, never absorbed.
