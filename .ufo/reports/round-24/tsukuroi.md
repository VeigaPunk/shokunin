# Tsukuroi round 24 — attempt 2

## Work performed

Declared claims: **C1**, calibration, per-cause observability of the frozen round-23 red cohort, target 268 findings with a named cause **and recorded tool operation**; **C2**, originally freshness, a sourced pause-lift gate, target 5 premises. **Both original targets are missed. This is an honest stop, not a request for admission.** Targets were not narrowed.

- C1 provides per-finding identities, checker-branch subcauses, recorded operations, lower-bound flags, the unknown-key attribution label, collector identity and native-versus-trace completion. It preserves the frozen grammar, CANNOT_EVALUATE and checker exit 2. Evidence: `tools/report-red-causes.py`; `measure/final/c1-final.txt` under `.ufo/waves/round-24/`.
- C2 returns to PROVINCE Core update-safety. It replaces the stable-mirror lag unknown and pending-count UNKNOWN with dated observations, marks the reversed 1password-beta trap, and distinguishes installed Omarchy v3.8.4 from upstream master. Evidence: `corpus/knowledge/pause-lift-gate-r24.md` and `.json`; SOURCES S087-S114.
- Read-only host evidence: 3 local-database pending rows versus 134 against freshly downloaded temporary databases (130 stable Arch snapshot, 4 third-party); systemd-family and limine updates plus the ca-certificates-mozilla security fix; 0 installed-newer rows among 1378 sync-covered packages; 21 foreign packages outside that test; 0 cache archives. Snapshot-boot overlay behavior remains unverified. Evidence: capture `l1-4/capture.txt`, `l1-4/checkupdates.out`; wave-2 RevP1Pending, RevP2Residue, RevP3Hooks and RevP5Rollback.
- Outside round-23 provenance corrections became QUALITY 54, with further criteria 55-56 and mistake controls. Old SCORECARD, LOG and round-23 lesson statements naming `replace_all` as retained-event proof now have appended corrections. Evidence: `corpus/lessons/round-24.md`, `corpus/QUALITY.md`, LOG round-24 entry.

All lane-relative evidence paths below are under `tsukuroi-shokunin/`. Final pushed lane tip: **`f923750ddcb5be2f25d0b91f5e78bc89be2608d6`**. Final implementation measured at **`44e95428e7081f79cb81b788ca3ece16c1540fb9`**; subsequent lane commits add only receipts and outcome text, not measurement inputs.

## Landed changes

| Pushed lane commit | Changes | LOG link |
|---|---|---|
| `674891dfbcb853432a863a6eb82e7b2a9bdb3958` | Two-claim declaration, initial host capture and start census | LOG round-24 entry |
| `10b45f050c16f5f1d4f7e15a285d9f5294f7a486` | Initial instruments, extended capture, initial lane gate runs and refused-wave evidence | same entry |
| `22fd1642e7fa4dfbdfba4419a443f06ffbb0b6c0` | Gate entry, first source rows, decision table, registry, criteria and first-wave evidence | same entry |
| `44e95428e7081f79cb81b788ca3ece16c1540fb9` | Falsifier corrections, superseding source rows, source-bound verdict limits, both target misses, privacy fixes, recorder identities and 74-seat accounting | same entry and final honesty correction |
| `333e8fdcb83d7d07eff431e5b68b12e132946a14` | Final measurements, source census and outcome text | final verification paragraph |
| `f923750ddcb5be2f25d0b91f5e78bc89be2608d6` | Matching-final-emitter baseline refusal receipts | same measurement record |

Inherited attempt 1: commit `eef0b8e9` contains 36 fixtures plus one index (37 paths). Neither claim uses these data. The private author trees, approval windows and hash chains were not continued. The outside `round-23-verifier-spotcheck.md` was not edited.

## Before → after measurements

Counting commands, run from the lane root with the working emitter matching production revision `44e95428e7081f79cb81b788ca3ece16c1540fb9`:

```sh
python3 tools/report-red-causes.py --revision <REV>
python3 tools/check-pause-gate.py --revision <REV>
```

| Claim | Base `f169b3ba9a59abaf3e324c1b591e1e07a4d6003a` | Production `44e95428e7081f79cb81b788ca3ece16c1540fb9` | Verdict |
|---|---|---|---|
| C1 | Final emitter exits 2: tool absent at the revision; no numeric value. The declared zero was absence, not a measured attribution result. | Command exits 0; cause attribution 268, recorded operations **267**, seat-level 1; original conjunction **267/268**. | **Missed / honest stop.** The field 268 uses a wider predicate and is not presented as meeting the original target. |
| C2 | Final emitter exits 2: tool absent; earlier emitter reported GATE-MISSING/0. The prose baseline was also wrong: dated verdicts already existed for P1 and P3. | Command exits **1**, `premises_verified: 4`, finding `P3:verdict-unverified-not-counted`; original target **5**. | **Missed / honest stop.** P3 was changed to unverified after RevP3Hooks; no boot was attempted to force success. |

Receipts: `.ufo/waves/round-24/measure/final/{c1-final,c2-final,c1-before-final-emitter,c2-before-final-emitter}.txt` and `receipt.json`. Earlier 268/5 readings at `22fd1642` are retained as superseded measurements, not erased.

C1 also fails the calibration-claim sizing rule: its count is attribution, not self-assessment mismatches. C2 was declared on freshness as if it were 8; freshness was 9, with depth and adjacency tied lowest at 8. The later depth rebooking does not erase the original lowest-axis declaration miss. No ordinal score changed.

Observed checks:
- Final new-tool selftests: C1 **12/12**, C2 **24/24**, exits 0.
- Final registry: **26/26**, no findings, audit-live-map errors 0, exit 0.
- Initial live capability exercises this round: census selftest **97/97**, live DEGRADED/exit 1; boot audit selftest **45/45**, live CONSISTENT/exit 0. Byte-level consistency is not proof of a snapshot boot.
- Fresh falsifiers independently reran both initial counting commands; mutation receipts cover input pins, split, shifted sites, labels, self-binding, verdicts, capture pins, source states and evidence pointers. Not every hypothetical mutant is covered. Later corrections were verified by the L1; no additional residual swarm was run.

C1 final provenance: frozen native completed **76**, trace complete **75**; ConnFxPlanner recorded native completed but trace incomplete, with **114** event findings marked lower bounds. The collector and native-record bytes match the claim base. Old strict receipts **127/140** well-formed and **13** faulty, early retry violations and historical scope findings remain red; no native restriction or enforcement is claimed.

## Sources & frontier

Command at start and end:

```sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin tsukuroi
```

Start output:
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
tsukuroi	ok	/home/vgpnk/Projects/shokunin/tsukuroi-shokunin/corpus/SOURCES.md
exit=0
```

End output:
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
tsukuroi	ok	/home/vgpnk/Projects/shokunin/tsukuroi-shokunin/corpus/SOURCES.md
exit=0
```

Root census: **86→114 rows**; tier A **78→106**, B **1→1**, C **7→7**; mined **72→100**, queued **5→5**, rejected **9→9**. Added 28 tier-A rows: 17 initial and 11 superseding corrections. Existing row cells were unchanged. Duplicate-scope W04 warnings **9→21** are disclosed, not suppressed. Final census and validation outputs are in `measure/final/`; the frozen manual census was independently exercised at the initial 103-row stage by RevCensusEnd (malformed rows 0, no duplicate IDs, enum failures or missing used-by paths).

The initial rows include 11 new normalized pages and six same-page re-registrations opened for the gate's date rule, not 17 new knowledge sources. S104-S114 narrow overbroad teachings and locators without rewriting original rows. `corpus/lessons/round-24.md` Gate gives dates, URLs, located quotes, correction mappings and rejected interpretations; SOURCES Search log records the bounded search. No frontier-to-Core promotion or capability row is claimed. Existing Core ground was deepened; snapshot boot and the upstream symlink-removal watch remain open.

## Trend verdicts

- **Expansion: unchanged.** Existing update-safety Core; no new coverage-map ground, capability or promotion.
- **Quality: improved, bounded and author-side.** Mirror-lag and current-pending unknowns gain dated evidence; stale downgrade-trap loci now carry notices. Source overreach was corrected by superseding rows. This does not turn either failed target into success.
- **Discernment: improved, provisional.** The outside line-52 disagreement became lesson-backed QUALITY 54 and a label-removal failure control. A fresh non-author closure must still sample an admit and reject; no outside admission is asserted.

## SHONEN

- [~] Decision tables, error patterns and sources: SKILL round-24 table and corrections; gate entry and SOURCES S104-S114. No non-author tick.
- [~] End-to-end domain task: read-only pause-gate evidence collection and operator question, LOG round-24; C2 target remains missed.
- [~] Executable instructions: two tools and recorded selftests; unsafe or overbroad recheck wording has appended restrictions. Whole-SKILL independent execution remains unverified.
- [~] Province boundary: package/boot diagnosis retained here; connector found no sibling province owning the update-safety gate. Attribution of earlier installs remains unknown.

## Round mechanics, limitations and operator decision

- Shape: **two v1 waves, 40 + 34 = 74 distinct seats**, zero provider deaths, no replacement seats and no residual call. One same-identity follow-up obtained the probe disclosure and cleanup. L1 holds planner.
- Build roles: 14 scribes, 11 executors, 3 scouts, 1 connector, 6 critics, 4 reviewers, 1 sentinel. Falsify roles: 9 mutation testers, 18 reviewers, 7 critics. Attack-role minimum met in both waves.
- One full 40-seat task refusal: **“Background job limit reached (100)”**, nothing spawned. Main lowered the gate cap to 85; the identical validated payload was reacquired and dispatched. Specs, registries, assignments and refusal are committed under `.ufo/waves/round-24/`.
- Conformance defects remain: delayed canonical loading; original lowest-axis miss; wave 2 dispatched before the last build connector returned; concurrent draft writers shared one checkout rather than separate worktrees; missing verbatim Godspeed directive body in the retained seat prompt; actual answering-model identities not captured; temporary files outside declared seat paths; literal scope conflicts for print-only pacman calls. No model override or route edit was supplied.
- ExecSymlinkMountProbe violated scope with privileged extraction, namespace writes and a **scratch-only `mkinitcpio -g --nopost` build**. Its appended disclosure lists commands; its large scratch residue was removed. No host /boot replacement, package transaction, service restart or boot action was observed. The violation is not waived by its scratch location.
- Privacy: no secret values were found by the reviewers. Non-pinned reports and a synthetic fixture had an unrelated project identifier redacted; pinned historical captures were not rewritten, and tip redaction does not erase published history. The capture generator now excludes sudo lines from Plymouth filters, reduces identifiers and uses a private temporary database. Large duplicate extra.db downloads were omitted and removed after digest/comparison receipts were retained.
- Misroot sweep: full fleet `git status --porcelain` found no untracked file attributable to these seats. Fleet runtime files and the other lane's `write` file were not touched. Later lane production edits were this L1's integration, not unknown seat activity.
- Installs or updates: **none**.
- Open L0: host-wide pacman pause and an operator-owned full-upgrade/rollback decision, refreshed in fleet commit **`453a9a2997255e878e4439ac063d813e1b7ef425`**. The pause remains active, including while the security update is pending. The inherited native-toolset enforcement question remains operator-owned.
- Stale-lane: this steered round progressed through pushed lane commits and is now reported; no other mission of this lane is open. No next round is started.
