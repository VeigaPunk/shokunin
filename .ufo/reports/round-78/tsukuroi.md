# tsukuroi — round 78

## Work performed

Declared claims: **C1 depth** (lowest tied axis, 8), six source-grounded finite
journal path-usage examples with reviewer binding; **C2 operability** (9),
operative registry findings 10 → 0. Both verify author-side at the measured
revision; independent outside admission remains pending. No ordinal uplift.

- C1 explains suffix selection, no-follow entry stat, regular-file guard,
  failed-stat skip and allocated blocks times 512, not apparent length.
  Actual source and companion independently read by ReviewUsage; all U1–U6
  hold. Evidence: `corpus/knowledge/journald-path-usage-r78.{md,json}`,
  `.ufo/waves/round-78/w1/ReviewUsage/verdict.json` at lane `a15aff6ea38961cae5e6748b1e8f924a1b454c34`.
- C2 adds eight omitted operative rows and corrects two code-2 maps,
  --repo interfaces and selftest scratch scopes; no existing tool changed
  or deleted. Evidence: `SKILL.md` operative round71 table,
  `w1/ReviewRegistry/{report.md,verdict.json}`, `after/after-C2.txt`.
- Real domain task: metadata-only journald accounting, safe-field config
  recheck and a prepared operator handoff. Allocated **202866688 bytes**
  versus apparent **268435456 bytes**, CLI **193.4M**; exact commands,
  capture UTC and exit0 retained in `w1/ExecHost/receipts/` and `handoff.md`.
  No vacuum/rotate/flush/restart, package transaction or cleanup action.
  Complete journald config was transiently captured before filtering;
  that is disclosed, not called a field-restricted child read.
- Supporting source execution compiles the exact extracted upstream C body
  with declared context shims; six private filesystem fixtures match
  lstat-based expectations. These are not frozen U1–U6 execution matches:
  sparse-file execution replaces the **unexercised failed-stat case**.
  Evidence: `w1/ExecSource/{report.md,provenance.json,receipt.json}`.
- One validated v1 wave **w1: 12 seats**, settled before reporting:
  scout1/executor3/scribe3/connector1/reviewer2/critic1/mutation-tester1;
  strict attack share4/12; L1-held planner, residual0, dead0. Spec/dispatch/
  registry/results are under `.ufo/waves/round-78/`. Routing used the live
  operator table; no model parameter or route override was supplied.
- Kernel restart initially left all result outputs null. The orchestrator
  recovered **actual latest seat outputs** with source/id/timestamp/basis,
  retaining `w1-results.json.pre-recovery-20261104`. ReviewUsage's actual
  final output carries `review_sha256=ed92cb4e52eb2aa5cbdf206eb49e46c9eefa64cdfb06c3bbe658522182d0b66e`,
  matching its final verdict after companion rereview. ExecRegistry and
  ScribeNote recovered later follow-up outputs, not their original finals.
  No vote was rederived or rerun, and no frozen rule changed. Evidence:
  recovered `w1-results.json` and lesson Wave settlement and recovery.
- Limits remain explicit: complete fabricated review/result bundles and
  false companion prose can pass the numeric C1 gate. Actual source/prose
  truth remains a separate frozen kill rule. MutationCounter records
  20 cases/two passes/120 CLI runs,14 rejection mutants killed; CriticFreeze
  retains successful constructions. Registry coverage is not whole-tool
  conformance or Linux execution proof. Evidence: both seats' reports and
  exact attack receipts. C1 lacks shared revision validation; exact
  canonical-copy load order was not fully followed, as lesson discloses.

Cross-domain: no new sibling-owned work absorbed. PROVINCE/SHONEN remain
unchanged; no promotion, package adoption or host-remediation clearance.
Stale-lane: this is the sole round opened here; lane commits show progress;
no successor or additional tsukuroi mission was started. Tool installs: none.
Start helper state was clean; no inherited uncommitted lane work was found.
Mandatory fleet-root sweep is `after/fleet-status.txt`: other-lane/runtime
changes untouched; unattributed untracked `after` contains only
`== SCORECARD diff base-` and was not removed. No attributable misroot found.
Round scratch `/fast/scratch/hyaku/tsukuroi-r78` removed after landing.

## Landed changes

Every item is tied to `LOG.md` **Round 78** and its appended outcome:

| Lane commit | Landed work |
|---|---|
| `07a607df1a5157daafc91bb5c26858af14415f43` | Pre-data declaration, exact source/specification, counter, controls and its registry row |
| `cd71642588c0282a9b73b48f87b415ecdadf6225` | Reviewed examples, two curated source rows, operative-registry repairs, skill/index/lesson, settled wave and recovery evidence |
| `a15aff6ea38961cae5e6748b1e8f924a1b454c34` | Revision-bound measurement receipts, census/sweeps and measured outcomes in LOG/SCORECARD/lesson |

Final lane branch `master` pushed: `git -C /home/vgpnk/Projects/shokunin/tsukuroi-shokunin ls-remote origin refs/heads/master`
printed `a15aff6ea38961cae5e6748b1e8f924a1b454c34 refs/heads/master` before this report.
Only evidence/outcome sections changed after the measured revision; target
JSON, reviewer files, source snapshots, counters and registry rows are unchanged.

## Before → after measurements

Base `b9019a1d0558241bf67cf31ff90256284d8657af` → measured
`cd71642588c0282a9b73b48f87b415ecdadf6225`.

| Claim | Counting command | Before | After | Verdict |
|---|---|---|---|---|
| C1 depth | `python3 tools/measure-journal-usage-r78.py --revision <REV>` | count0/met0/rc1 | count6/met1/rc0 | verified finite target plus separately read truthful source/companion; depth8→8 |
| C2 operability | `python3 tools/check-registry-coverage.py --revision <REV>` | findings10/missing8/registered108/tools116/rc1 | findings0/missing0/registered117/tools117/rc0 | verified discoverability/interface repair; operability9→9 |

Receipts: `.ufo/waves/round-78/after/{before,after}-C{1,2}.txt`,
with revision, tool revision/SHA256, exact argv, stdout and exit headers/footers;
`after/commands.json` records the runner commands. Existing receipt generator
was used through a scratch/shared-clone adapter; target code is unchanged.
C1 selftest15/15, registry selftest23/23, knowledge-reference gate0 findings,
all rc0 at measured revision. No broader test/build/lint suite is claimed.

Pre-data controls (`before/controls.json`): base fails both targets; scripted
source-reading fetch/fill without review and fabricated review without actual
result each C1 count0/rc1. Both counters/specification and source pins retain
frozen bytes (`after/structural.json`). Tool diff adds only the new finite
instrument; no existing tool removed or changed. `after/record-sweep.json`
lists complete removed lines: base→freeze0, freeze→integrated3, base→integrated2,
all disclosed SKILL registry-cell repairs; no historical corpus rewrite.

## Sources & frontier

SOURCES rows **326 → 328**; tier A309→311/B6→6/C11→11;
mined289→290/queued5→5/rejected32→33; Markdown notes95→96.
Command: `git show <REV>:corpus/SOURCES.md` parsed with
`^ {0,3}\|\s*(S[0-9]{3,})\s*\|`; notes:
`git ls-tree -r --name-only <REV> corpus/knowledge` with `.md` suffix count.
Exact algorithm/revision outputs are in `after/structural.json`.

- Added A2/B0/C0: **S327 mined** manager implementation, **S328 rejected**
  broad manual as sole implementation proof. Lesson Gate gives both exact
  URLs,2026-11-04 access dates,located quotes≤25 words and reject flip.
- Existing-row status/recheck/used-by changes: **none**; new IDs only.
  Frontier rows advanced: **0**; existing journald ground is deepened.
- Assimilation: **none**. Staged package/promotion holds remain unresolved.
  Complete lists: `w1/ConnectorScope/{base-reg-ids,freeze-reg-ids,reg-ids,staged-ids,collisions}`;
  base/freeze IDs S001 through S326 inclusive, final S001 through S328,
  staged S200 through S346, final intersection S200 through S328 (**129**;
  base/freeze127). Indented collision control and input hashes are retained;
  renumber map empty, no adoption/append attempted. No stale collision number
  is reused. Existing L0 r64/r75 package-id-drift and r60 whole-SKILL
  disposition questions remain; no new question or permission is invented.
- `considerthese/2026-10-26.md` opened; referenced scoreboard, patch-offset
  and correction-propagation proposals already have rules. No still-unimplemented
  proposal or shokuknow knowledge is claimed adopted this round.
- Mistakes mined: inherited operative-registry debt, missing review binding,
  binding-not-authentication and instrument-checkout scope. Named red-before
  controls and original output are in the lesson, not merely prevention prose.

Required census command, run at start and end:
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tsukuroi`.
Complete retained outputs follow (warnings not suppressed):

Start (`before/census.txt`):
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
tsukuroi	ok	/home/vgpnk/Projects/shokunin/tsukuroi-shokunin/corpus/SOURCES.md

exit_code=0
```

End (`after/census.txt`):
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
tsukuroi	ok	/home/vgpnk/Projects/shokunin/tsukuroi-shokunin/corpus/SOURCES.md

exit_code=0
```

## Trend verdicts

| Trend | Verdict | Evidence |
|---|---|---|
| expansion | unchanged | Existing journald accounting deepened; no frontier/capability promoted; README Round78 |
| quality | improved | Source-grounded examples, actual source/companion reading, real metadata task and ten inherited registry findings repaired; receipts and ReviewUsage/ReviewRegistry |
| discernment | unchanged | Prior outside round77 agrees on admits/rejects; current outside admit/reject check pending, dispatched seats are still this lane |

No observed owned-axis harm is established by this scoped change; inherited
whole-corpus/tool conformance limits are not advertised repaired. Admission
belongs to independent closure, not these author-side measurements.

## SHONEN

- [~] Decision tables/error patterns/checklists/citations: SKILL standing sections plus Round-78 journal path-usage table; SHONEN box1 remains author-side.
- [~] End-to-end domain task: LOG Round78 and `.ufo/waves/round-78/w1/ExecHost/handoff.md`; operator remediation deliberately unexecuted.
- [~] Executable instructions without oral context: exact source/receipt/fixture commands retained; whole-SKILL non-author replay remains unverified, SHONEN box3.
- [~] No cross-domain bleed: PROVINCE unchanged; source/host and operator boundaries preserved in note/lesson and ConnectorScope report; no promotion verifier claimed.
