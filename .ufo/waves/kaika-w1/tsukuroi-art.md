# kaika W1 — ART dossier · lane `tsukuroi` (host operability & repair)

author: `W1ArtTsukuroi` (scout, leaf; no dispatch) · written 2026-10-19 · this file is the only write.

- **Tools.** `web_search` was available. I ran 4 queries. All 4 answers were tier-C synthesized answers, so none is used as support. Two are kept as rejections (§6). Public pages were opened with `read`. Upstream raw files, the GitLab release API and the AUR RPC were fetched with `curl` GETs.
- **Host probes.** The host is `plazir27`. Probes were read-only and non-root: no sudo, no `-Sy`, no transaction, no service action, no file written. Every probe is listed in Appendix A.
- **Lane repo reads.** I read only what the ART shape names: `corpus/README.md`, `PROVINCE.md`, `corpus/QUALITY.md`, the `SKILL.md` headings and the `corpus/knowledge/` filenames, plus targeted greps (§1.2). I also ran one grep-only sweep of `tools/tsukuroi-census.sh` (§6 R7).
- **Prompt injection.** None found in fetched content. No credential material was read.
- **Tags.** **[obs]** = measured now, with the command given · **[inf]** = inference · **[unk]** = unknown.

## 0. Digest

1. **The leading open exposure (J4/U1, no rollback net) now has a mechanism grounded in documentation.** `/` is mode **0555** (`r-x` for its owner, root). The `limine-snapper-sync` unit limits root to `CapabilityBoundingSet=CAP_SYS_ADMIN`. With no `CAP_DAC_OVERRIDE`, creating `/.snapshots` fails with EACCES (errno 13). The lane had recorded this as "none of the obvious candidates explains errno 13". It recurred **8×** between 2026-10-16 and 2026-10-19 (K2).
2. **mkinitcpio v42 (released 2026-09-02) moves the busybox init's root mount from `/new_root` to `/sysroot`.** The host is busybox-based and still on 41.1-1. **2 of its 7 effective runtime hooks hardcode `/new_root`:**
   - `btrfs-overlayfs`. Its upstream master is unchanged, and its `|| return 0` makes the hook a silent no-op after the change.
   - `plymouth`. The Arch packaging `main` branch is unchanged.

   The Arch news feed does not announce this change; only the release notes carry it (K5).
3. **The U2 gate ("upstream delta unmeasurable read-only") can be measured without `-Sy`.** The Arch web JSON API shows the boot chain behind on 5 of 5 sampled packages (K3). Separately, ≥9 lane lines advise an operator to run bare `-Sy`, which contradicts ArchWiki doctrine (D1).
4. **The lane holds no Arch-news gate, no pacnew plane and no recovery entry points.** Each sweep returns 0 hits (§1.2). For the news gate: 20 news items fall in 2025–2026, and 0 require intervention on this host's next `-Syu` (K4). For pacnew: 3 `.pacnew` files are pending (K6).

## 1. Uncovered ground

### 1.1 What the lane holds — counts with commands (run in the lane repo root)

- `25` knowledge notes — `ls corpus/knowledge/*.md | wc -l` (`26` files incl. 1 `.json` — `ls corpus/knowledge/ | wc -l`)
- `1` lesson file (`round-1.md`) — `ls corpus/lessons/*.md | wc -l`
- `5` admission criteria — `grep -cE '^[0-9]+\.' corpus/QUALITY.md`
- `10` coverage-map rows — ``grep -c '^| `' corpus/README.md``
- `3` `## Frontier` bullets — `awk '/^## Frontier/{f=1;next} /^## /{f=0} f && /^- /' corpus/README.md | wc -l`

What those holdings cover:

- **Planes held** (coverage map): package state, systemd user plane, driver/firmware, update safety (v1–v3), the census gate (six planes by r11), journal/boot, the r3 host-health report, an executor sufficiency test, and adjacency handoffs.
- **Knowledge filenames** add: the AUR risk plane, foreign provenance, OOM/kill events, timer drift, boot plane, degraded triage and calibration synthesis.
- **PROVINCE Core:** `pacman -Qkk` loops, foreign/AUR census, systemd user units/timers, journal/boot triage, driver/firmware presence, and the update-safety question "what would `-Syu` touch".
- **What the corpus is made of:** almost entirely measured host state. It holds no external current art; no knowledge note cites an upstream doc, man page or news item as its source.

### 1.2 Sweeps — current-art topics with zero lane coverage [obs, 2026-10-19, repo root]

| topic | sweep | hits |
|---|---|---|
| Arch news / news gate | `grep -rliE 'archlinux\.org/news\|arch news\|informant' corpus SKILL.md PROVINCE.md \| wc -l` | 0 |
| pacnew / pacsave / pacdiff | `grep -rliE 'pacnew\|pacsave\|pacdiff' corpus/ SKILL.md PROVINCE.md \| wc -l` | 0 |
| recovery entry points | `grep -rliE 'rescue\.target\|emergency\.target\|break=premount\|rd\.systemd\|debug_shell\|arch-chroot\|init=/bin/sh' corpus SKILL.md \| wc -l` | 0 |
| Arch Linux Archive (date-pinned rollback) | `grep -rliE 'archive\.archlinux\.org\|Arch Linux Archive' corpus SKILL.md \| wc -l` | 0 |
| pacman 7.x sandbox options | `grep -rliE 'DisableSandbox\|Landlock\|disable-sandbox' corpus SKILL.md \| wc -l` | 0 |
| DAC mode / capability bounding | `grep -rlE 'CAP_DAC_OVERRIDE\|mode 555\|\b555\b' corpus/knowledge \| wc -l` | 0 |
| systemd ≥258 deltas | `grep -rliE 'systemd 26[0-9]\|v26[0-9]\b\|cgroup v1' corpus SKILL.md \| wc -l` | 1 (a version pin only, `systemd-user-plane.md:3`) |
| mkinitcpio drop-ins | `grep -rlE 'mkinitcpio\.conf\.d\|omarchy_hooks' corpus SKILL.md \| wc -l` | 1 (`degraded-triage-r4.md:358-362`) |

(The table escapes `\|` for markdown; in a shell type a plain `|`.)

### 1.3 Uncovered ground → where it lands

- **U-a. News gate.** "Read before upgrading" is absent. It belongs in the SKILL update-safety checklist and the update-safety row → K4.
- **U-b. Config drift (`.pacnew`/`.pacsave`).** Absent. It belongs in the package-state row → K6.
- **U-c. Boot-recovery entry points by initramfs flavor.** Absent. It belongs in the journal-boot and boot-plane rows and in J3 → K5.
- **U-d. Restore paths.** Absent: `snapper rollback` semantics, the Arch Linux Archive (ALA) date-pinned restore, and limine-snapper-sync's restore methods. The lane holds only the exposure ("no rollback net"). These belong in the update-safety row and U1 → K2 and §5 P1.
- **U-e. The initramfs/UKI build path and its 2025–2026 changes.** Covers the mkinitcpio v40 packaged defaults, the v42 busybox `/sysroot` change and drop-in precedence. U3 holds only the hook coupling → K5.
- **U-f. pacman 7.x semantics.** Covers the 7.1 default `SigLevel`, the download sandbox and DownloadUser temp dirs, and the HookDir override rule. Partly held as raw observation only → K1, plus S005/S006.
- **U-g. systemd 258–262 changes against the probe surface and recovery tools.** Absent → §2, R7.
- **U-h. Upstream delta without `-Sy`** (web JSON API; checkupdates mechanism). Held only as [unknown]/[inference] → K3.
- **U-i. Package-verification blind spots** (root-dir mode is unowned). Absent → K2 and D6.

### 1.4 QUALITY.md gaps relative to the SOURCES contract

The current five criteria contain:

- no source-tier rule (tier C may never be the sole support),
- no `recheck:` or expiry rule,
- no rule that an operator action must match distro doctrine,
- no falsifier requirement for mechanism claims.

Proposals for wave 2 are in §7.

## 2. Current art 2025–2026 the corpus does not hold

**pacman / ALPM**

- **pacman 7.1.0 (tagged 2025-11-01).**
  - Changes: default `SigLevel` Required; the downloader sandbox gains syscall filtering and NO_NEW_PRIVS; new fine-grained switches `DisableSandboxFilesystem` and `DisableSandboxSyscalls`; fixes for running as non-root or on NFS. [S006, S007]
  - No newer tag exists as of today (tags feed, held back).
  - [obs] The host runs `7.1.0.r9.g54d9411-2`; upstream is `-3`, built 2026-10-15.
- **pacman 7.0 DownloadUser.** pacman downloads into a temporary directory owned by `DownloadUser` [S006, S005]. This is the documented origin of the host's three `download-*` dirs (`alpm:alpm`, 700) that the lane recorded as P5.
- **Hook override rule.** A same-name hook in a later HookDir overrides the packaged one; a symlink to `/dev/null` disables a hook [S007, S008] → K1.
- **checkupdates mechanism** (pacman-contrib 1.13.1, man footer 2025-12-11). It syncs a temporary DB with the real `local` DB symlinked in, under fakeroot, using `--disable-sandbox-filesystem`, then runs `pacman -Qu --dbpath`. It exits 2 when there are no updates [S009] → K3.
- **Arch web JSON API.** It gives per-package upstream version, build and update dates, and the out-of-date flag, all read-only [S012] → K3.

**Arch news, 2025-01-01 → 2026-10-19.** 20 items (S001). Lane-relevant:

- mkinitcpio ≥42 changes TPM2 PCR measurements (S002).
- An active AUR malicious-packages incident (S003).
- A DDoS on archlinux.org/AUR, with fallbacks: the `pacman-mirrorlist` mirrors and a GitHub AUR mirror (S004).
- Items already in the past on this host: NVIDIA 590 open modules, the linux-firmware vendor split, iptables→nft, .NET 10, removal of the old repos, rsync 3.4.0.

Per-item applicability is in K4.

**mkinitcpio / UKI**

- **v40 (2025-11-04).** Release notes [S015]:
  - meson build;
  - `sd-volatile`, `sd-verity` and `sd-encrypt-opensc`;
  - "install/systemd now supports systemd v258 and onwards";
  - default presets drop the fallback image.
- **Packaged default HOOKS is systemd-based.** [obs] The 41.1 package in the host cache ships `HOOKS=(base systemd autodetect microcode modconf kms keyboard sd-vconsole block filesystems fsck)`. The v39.2 repo default was busybox `udev`. ArchWiki calls the systemd initramfs "the default" [S014].
- **v42 (2026-09-02) and v42.2 (2026-10-01).** Busybox init mounts root at `/sysroot`. `install/systemd` adds `systemd-pcrosseparator.service`. `/etc/crypttab.initramfs` is deprecated in favor of `x-initrd.attach` [S015, S016, S002] → K5.
- **UKI build routes.** mkinitcpio, ukify or kernel-install; `/etc/cmdline.d`; preset `PRESET_uki=` [S017].

**Limine / snapper / Btrfs**

- **Limine automation.** Done through limine-entry-tool, `limine-mkinitcpio-hook` and `limine-snapper-sync`. The wiki documents `MKINITCPIO_FALLBACK`, `ENABLE_UKI` and snapshot entries [S018].
- **limine-snapper-sync** [S019]:
  - restore via rsync, replace or snapper;
  - adds a "backup" entry after a restore;
  - auto-repairs corrupted boot files;
  - recommends an ESP of **≥4 GiB**;
  - "If mismatches occur more than 3 times, Btrfs root and home are set to read-only to prevent further corruption".

  That last behavior is a host-wide side effect the lane should track.
- **Snapper on Arch** [S023]:
  - `create-config` creates `.snapshots`;
  - archinstall < 3.0.5 made a pre-existing `@.snapshots` that breaks `create-config`;
  - snap-pac wraps pacman transactions;
  - booting a read-only snapshot needs an overlay;
  - read `/var/log/snapper.log` first when debugging.
- **Upstream unit hardening.** The upstream unit pins `CapabilityBoundingSet=CAP_SYS_ADMIN` [S020] → K2.

**systemd 258 → 262** (S024; the host runs 261.2, `[core]` ships 262.1-1)

- 258 removes cgroup v1.
- 258 adds the `systemd.break=` / `rd.systemd.break=` boot breakpoints [S025].
- 258 adds a factory-reset target and tool.
- 260 removes the SysV and rc-local generators.
- 261 adds `systemd-pcrosseparator.service`.
- 262: `journalctl` now rejects `-F` combined with filters.
- 262: journal readers salvage entries from truncated active files [inf: counts may shift slightly after an upgrade].
- 262 adds `RestartRandomizedDelaySec=`.

**Recovery practice**

- Stage-by-stage boot diagnosis; the `rescue`, `emergency` and `init=/bin/sh` shells; a debug shell on tty9 [S026].
- Repair by chroot: `arch-chroot -S /mnt`, `pacman --sysroot` [S026].
- Date-pinned whole-system restore through the Arch Linux Archive [S013].
- Never use `btrfs check --repair` unless advised (held back: btrfs-check(8)).

## 3. SOURCES.md rows (30 — paste-ready; every row opened by this scout on 2026-10-19)

| id | source | kind | tier | teaches | status | opened | recheck | used-by |
|---|---|---|---|---|---|---|---|---|
| S001 | Arch Linux News index — https://archlinux.org/news/ | docs | A | the distro's manual-intervention feed; 20 items dated 2025–2026 to check before any wave | watch | 2026-10-19 | weekly | — |
| S002 | News: Mkinitcpio >=42 requires manual intervention for TPM2-based unlocking of LUKS devices (2026-09-22) — https://archlinux.org/news/mkinitcpio-42-requires-manual-intervention-for-tpm2-based-unlocking-of-luks-devices/ | docs | A | systemd-hook + TPM2 LUKS users must re-enroll after PCR 0-7/9/12-14 changes; busybox hosts unaffected | queued | 2026-10-19 | on-release | — |
| S003 | News: Active AUR malicious packages incident (2026-06-12) — https://archlinux.org/news/active-aur-malicious-packages-incident/ | docs | A | ongoing AUR supply-chain advisory: review every PKGBUILD and install-script diff on update | watch | 2026-10-19 | 30d | — |
| S004 | News: Recent service outages (2025-08-21) — https://archlinux.org/news/recent-services-outages/ | docs | A | DDoS fallbacks: pacman-mirrorlist mirrors, GitHub AUR mirror, offline wiki packages | queued | 2026-10-19 | 180d | — |
| S005 | News: Manual intervention for pacman 7.0.0 and local repositories required (2024-09-14) — https://archlinux.org/news/manual-intervention-for-pacman-700-and-local-repositories-required/ | docs | A | older canonical origin of DownloadUser privilege drop and the alpm group requirement | queued | 2026-10-19 | 365d | — |
| S006 | pacman NEWS — https://gitlab.archlinux.org/pacman/pacman/-/raw/master/NEWS | docs | A | 7.0 and 7.1 changes: DownloadUser temp dirs, sandbox switches, SigLevel Required default | watch | 2026-10-19 | on-release | — |
| S007 | pacman.conf(5) — https://man.archlinux.org/man/pacman.conf.5 | docs | A | HookDir precedence (later dirs win), DownloadUser and DisableSandbox* options, CleanMethod | queued | 2026-10-19 | on-release | — |
| S008 | alpm-hooks(5) — https://man.archlinux.org/man/alpm-hooks.5 | docs | A | hook file format, OVERRIDING HOOKS by same name or /dev/null, PostTransaction caveats | queued | 2026-10-19 | on-release | — |
| S009 | checkupdates.sh.in (pacman-contrib master) — https://gitlab.archlinux.org/pacman/pacman-contrib/-/raw/master/src/checkupdates.sh.in | code | A | safe update check: temp dbpath, symlinked local db, fakeroot, exit 2 when none, never touches the sync db | queued | 2026-10-19 | on-release | — |
| S010 | ArchWiki System maintenance (oldid 885170) — https://wiki.archlinux.org/title/System_maintenance | docs | A | doctrine: read news first, never bare -Sy, act on pacnew, revert broken updates, check orphans | queued | 2026-10-19 | 180d | — |
| S011 | ArchWiki pacman/Pacnew and Pacsave (oldid 869214) — https://wiki.archlinux.org/title/Pacman/Pacnew_and_Pacsave | docs | A | 3-way md5 rule, locating .pac files by find or log (log is history not state), pacdiff | queued | 2026-10-19 | 365d | — |
| S012 | ArchWiki Official repositories web interface (oldid 867367) — https://wiki.archlinux.org/title/Official_repositories_web_interface | docs | A | JSON endpoints for read-only upstream versions: /packages/search/json/?name= and per-package /json/ | queued | 2026-10-19 | 180d | — |
| S013 | ArchWiki Arch Linux Archive — https://wiki.archlinux.org/title/Arch_Linux_Archive | docs | A | downgrade one package or restore all packages to a date; never mix ALA with live mirrors | queued | 2026-10-19 | 365d | — |
| S014 | ArchWiki mkinitcpio (oldid 886405) — https://wiki.archlinux.org/title/Mkinitcpio | docs | A | systemd vs busybox initramfs, hook table, drop-ins, break= runtime params, fallback disabled by default | queued | 2026-10-19 | 90d | — |
| S015 | mkinitcpio releases — https://gitlab.archlinux.org/archlinux/mkinitcpio/mkinitcpio/-/tags (notes via /api/v4/projects/archlinux%2Fmkinitcpio%2Fmkinitcpio/releases/v40 and /v42) | docs | A | v40 and v42 release notes incl. busybox root at /sysroot and pcrosseparator; tag dates v40 to v42.2 | watch | 2026-10-19 | on-release | — |
| S016 | mkinitcpio v42 busybox init — https://gitlab.archlinux.org/archlinux/mkinitcpio/mkinitcpio/-/raw/v42/init | code | A | root mounted at /sysroot (init:66-67, switch_root at :110); 0 /new_root refs vs 7 in v41.1 | queued | 2026-10-19 | on-release | — |
| S017 | ArchWiki Unified kernel image — https://wiki.archlinux.org/title/Unified_kernel_image | docs | A | UKI build via mkinitcpio, ukify or kernel-install; /etc/cmdline.d; PRESET_uki | queued | 2026-10-19 | 180d | — |
| S018 | ArchWiki Limine (oldid 887253) — https://wiki.archlinux.org/title/Limine | docs | A | limine-entry-tool config incl. MKINITCPIO_FALLBACK and ENABLE_UKI; snapper integration and overlay hooks | queued | 2026-10-19 | 90d | — |
| S019 | limine-snapper-sync README — https://gitlab.com/Zesko/limine-snapper-sync/-/raw/master/README.md | docs | A | restore methods, backup entry, boot-file auto-repair, ESP >= 4 GiB, read-only root on repeated hash mismatch | queued | 2026-10-19 | on-release | — |
| S020 | limine-snapper-sync.service (upstream unit) — https://gitlab.com/Zesko/limine-snapper-sync/-/raw/master/install/arch-linux/usr/lib/systemd/system/limine-snapper-sync.service | code | A | the hardening block: CapabilityBoundingSet=CAP_SYS_ADMIN, ProtectHome, SystemCallFilter | watch | 2026-10-19 | on-release | — |
| S021 | limine-entry-tool btrfs-overlayfs runtime hook (master) — https://gitlab.com/Zesko/limine-entry-tool/-/raw/master/install/arch-linux/limine-mkinitcpio-hook/usr/lib/initcpio/hooks/btrfs-overlayfs | code | A | snapshot overlay logic; hardcodes root_mnt=/new_root (line 4) and returns 0 if not mounted (line 7) | watch | 2026-10-19 | on-release | — |
| S022 | Arch plymouth packaging initcpio hook (main) — https://gitlab.archlinux.org/archlinux/packaging/packages/plymouth/-/raw/main/plymouth.initcpio_hook | code | A | busybox latehook runs plymouth update-root-fs --new-root-dir=/new_root | watch | 2026-10-19 | on-release | — |
| S023 | ArchWiki Snapper (oldid 870168) — https://wiki.archlinux.org/title/Snapper | docs | B | create-config semantics, archinstall @.snapshots pitfall, snap-pac, read-only snapshot boot; several sections flagged disputed | queued | 2026-10-19 | 180d | — |
| S024 | systemd NEWS — https://raw.githubusercontent.com/systemd/systemd/main/NEWS | docs | A | 258 to 262 deltas: cgroup v1 removed, SysV generators removed, pcrosseparator, journalctl -F with filters rejected | watch | 2026-10-19 | on-release | — |
| S025 | systemd-debug-generator(8) (systemd 262.1) — https://man.archlinux.org/man/systemd-debug-generator.8 | docs | A | systemd.break= and rd.systemd.break= breakpoints (v258), debug_shell on tty9, systemd.mask= | queued | 2026-10-19 | on-release | — |
| S026 | ArchWiki General troubleshooting (oldid 882746) — https://wiki.archlinux.org/title/General_troubleshooting | docs | A | boot-stage triage, recovery shells, chroot repair with arch-chroot -S and pacman --sysroot | queued | 2026-10-19 | 180d | — |
| S027 | capabilities(7) — https://man.archlinux.org/man/capabilities.7 | docs | A | CAP_DAC_OVERRIDE is the root bypass of rwx checks; bounding-set semantics | queued | 2026-10-19 | 365d | — |
| S028 | systemd.exec(5) — https://man.archlinux.org/man/systemd.exec.5 | docs | A | CapabilityBoundingSet= removes unlisted caps from bounding, effective and permitted sets | queued | 2026-10-19 | on-release | — |
| S029 | Arch Linux Security Tracker — https://security.archlinux.org/ | dataset | A | rejected: stale; newest AVG ids carry 2025 CVEs and it lists systemd 257.6-1 vulnerable while core ships 262.1-1 | rejected | 2026-10-19 | 180d | — |
| S030 | web_search synthesized answer, query on limine-snapper-sync CapabilityBoundingSet and 555 root (2026-10-19) | tool | C | rejected: asserts the unit sets CAP_DAC_OVERRIDE, contradicted by S020; AI summary never sole support | rejected | 2026-10-19 | — | — |

Self-check commands (run against this artifact):

- rows: `grep -cE '^\| S[0-9]{3} ' <file>`
- tiers: `grep -E '^\| S[0-9]{3} ' <file> | awk -F'|' '{gsub(/ /,"",$5); print $5}' | sort | uniq -c`

### Opened in this session, held back from rows (cap 30; promote if cited)

- checkupdates(8) https://man.archlinux.org/man/checkupdates.8 — the docs view of S009
- snapper(8) https://man.archlinux.org/man/snapper.8 — rollback semantics: "Creates two new snapshots and sets the default subvolume"
- btrfs-check(8) https://btrfs.readthedocs.io/en/latest/btrfs-check.html — "Do not use --repair unless you are advised to do so by a developer or an experienced user"
- access(2) https://man.archlinux.org/man/access.2 — used for the K2 falsifier
- AUR RPC v5 `https://aur.archlinux.org/rpc/v5/info?arg[]=…`
- pacman tags feed
- package JSON endpoints: systemd, mkinitcpio, pacman, linux, limine, plymouth, informant
- news items: NVIDIA 590, linux-firmware split, Cleaning up old repositories, .NET, iptables→nft

### Leads (unopened)

- **July 2025 AUR malware (CHAOS RAT)** — primary aur-general thread. Only seen as search snippets of secondary coverage, e.g. linuxsecurity.com/features/chaos-rat-in-aur.
- **Forum thread on snapper `create-config`** — https://bbs.archlinux.org/viewtopic.php?id=290007 (the pre-existing `.snapshots` failure).
- **archinstall 3.0.5 release** — https://github.com/archlinux/archinstall/releases/tag/3.0.5 (snapshot layout change cited by S023).
- **limine-snapper-sync issues** — https://gitlab.com/Zesko/limine-snapper-sync/-/issues (search: errno 13, CapabilityBoundingSet, /sysroot).
- **Omarchy installer source** — the likely origin of `/` mode 0555 [unk].
- **systemd factory-reset doc** — https://systemd.io/FACTORY_RESET
- **TPM2 tooling** — systemd-cryptenroll(1), systemd-pcrlock(8) (relevant only after a systemd-hook + TPM2 migration).
- **kernel-modules-hook** — https://archlinux.org/packages/?name=kernel-modules-hook (keeps running-kernel modules after a kernel upgrade).
- **News-gate tooling** — Arch-Update https://github.com/Antiz96/arch-update; informant https://github.com/bradford-smith94/informant.
- **AUR GitHub mirror** — https://github.com/archlinux/aur (fallback during outages).
- **Firmware and Btrfs docs** — https://wiki.archlinux.org/title/Fwupd; https://btrfs.readthedocs.io/en/latest/btrfs-scrub.html; btrfs-progs 7.x release notes (the host runs 7.1-1).
- **mkinitcpio(8)** — runtime parameter reference.
- **Outage thread** — the arch-general thread linked from S004.

## 4. Candidate knowledge entries (6)

### K1 `hook-precedence-receipt` — the `/etc` override won the 90-mkinitcpio-install collision

- **Claim.** On this host, `/etc/pacman.d/hooks/90-mkinitcpio-install.hook` overrides the packaged hook of the same name. The 2026-10-11 kernel wave ran the override.
- **Falsifier.** Any later run printing the packaged output `==> Building image from preset` after the hook name, while the override file still exists.
- **Evidence [obs].**
  - `pacman-conf HookDir` → `/etc/pacman.d/hooks/`.
  - The two `Exec` lines differ: packaged `/usr/share/libalpm/scripts/mkinitcpio install` vs override `/usr/share/libalpm/scripts/limine-mkinitcpio-install`.
  - `grep -c "running '90-mkinitcpio-install.hook'" /var/log/pacman.log` → 3.
  - The override's output `Building UKI for linux (7.2.3-arch1-3)` follows at `pacman.log:1989-1990` (2026-10-11T16:15:38-0300) and at `:1362-1363` (2026-10-03T17:45).
  - The packaged output appears only at `:269-271` (2026-10-03T20:42:02+0000). [inf] That is the installer phase, before the override existed.
- **Sources.**
  - S007 pacman.conf(5) § OPTIONS → HookDir: "Multiple directories can be specified with hooks in later directories taking precedence over hooks in earlier directories."
  - S008 alpm-hooks(5) § OVERRIDING HOOKS: "Hooks may be overridden by placing a file with the same name in a higher priority hook directory."
- **Fills.** Closes the U3 [unknown] at `corpus/knowledge/degraded-triage-r4.md:369-371` and unknown #9 at `:546-547`. Corrects the wording "precedence for earlier hook dirs" (`:370`). Belongs to the update-safety coverage row.
- **Recheck.** `pacman-conf HookDir; grep -H '^Exec' /usr/share/libalpm/hooks/90-mkinitcpio-install.hook /etc/pacman.d/hooks/90-mkinitcpio-install.hook; grep -n -A1 "running '90-mkinitcpio-install.hook'" /var/log/pacman.log`
- **QUALITY.md.**
  - (1) Falsifiable, as above.
  - (2) Cites man-page sections and log line numbers.
  - (3) The installer-phase reading is tagged [inf].
  - (4) The triage note is corrected by an appended erratum, never edited.
  - (5) Nothing rejected.

### K2 `snapper-eacces-mechanism` — why `/.snapshots` creation fails (J4/U1)

- **Claim [inf, grounded in documented mechanism].** `limine-snapper-watcher` fails with `create subvolume failed … errno:13 (Permission denied)` because of two facts together:
  - `/` is mode 0555 `root:root`, so its owner has no write bit;
  - the unit's `CapabilityBoundingSet=CAP_SYS_ADMIN` removes `CAP_DAC_OVERRIDE`, root's bypass of rwx checks.

  The documented common cause (a pre-existing `@.snapshots`) is excluded: the lane measured no `.snapshots` subvolume (`degraded-triage-r4.md:73`; `closeout-r11.md:229`). Also, that cause yields "already exists", not EACCES.
- **Falsifier (operator-only, non-mutating).**
  - `sudo systemd-run --wait --pipe -p CapabilityBoundingSet=CAP_SYS_ADMIN test -w /; echo rc=$?` — predicted rc=1.
  - `sudo test -w /; echo rc=$?` — predicted rc=0.
  - If the first returns 0, the mechanism is refuted. access(2) supports the test: "for the root user, the check uses the set of permitted capabilities rather than the set of effective capabilities".
- **Evidence [obs].**
  - `stat -c '%a %U:%G' /` → `555 root:root`; `getfacl -p /` → `user::r-x`.
  - `systemctl cat limine-snapper-sync.service | grep -n CapabilityBoundingSet` → `14:CapabilityBoundingSet=CAP_SYS_ADMIN`. The same value is in the upstream master unit (S020).
  - `journalctl --no-pager -o short-iso -g 'create subvolume failed' | grep -c 'errno:13'` → 8. Range: 2026-10-16T12:47:26 → 2026-10-19T08:11:47.
  - `snapper list-configs` → header only; `/etc/conf.d/snapper` has `SNAPPER_CONFIGS=""` (mtime 2026-10-19 08:11).
  - **Blind spot.** `pacman -Qo /` → "No package owns /", and `zcat /var/lib/pacman/local/filesystem-*/mtree | grep -cE '^\./?[[:space:]]'` → 0. So `-Qkk` can never see root-dir mode drift.
  - **ESP.** `df -h /boot` → 2.0G size, 279M used (14%), against S019's "A FAT32 boot partition of at least 4 GiB is recommended". `/etc/default/limine:18` `MAX_SNAPSHOT_ENTRIES=5`.
- **Sources.**
  - S027 capabilities(7) § CAP_DAC_OVERRIDE: "Bypass file read, write, and execute permission checks."
  - S028 systemd.exec(5) § CapabilityBoundingSet=: "Capabilities listed will be included in the bounding set, all others are removed."
  - S023 Snapper § Creating a new configuration, Note: "the @.snapshots subvolume will already be mounted to /.snapshots, and the snapper create-config command will fail" (this is the excluded cause).
- **Fills.** J4/U1 mechanism ("none of the obvious candidates explains errno 13", `degraded-triage-r4.md:321-325`); journal-boot §3.1; the package-state blind spot.
- **Operator options (reported, never performed).**
  - (a) `chmod 755 /`. `/` is unowned by any package.
  - (b) A one-time manual `snapper -c root create-config /` with full capabilities, then `SNAPPER_CONFIG_NAME="root"`. [inf] Later snapshot writes go inside `.snapshots` (mode 750, owned by root), so they need no DAC override.
- **Unknowns.** [unk] where the 0555 came from (installer?). [unk] contents of `/var/log/snapper.log` (27 544 B, mode 640 root, mtime 2026-10-19 08:12).
- **QUALITY.md.** (1) Falsifier given. (2) Man pages, unit file and measured anchors. (3) obs/inf/unk split. (4) Appended as an erratum to the J4 record. (5) The excluded cause is kept as a recorded rejection.

### K3 `upstream-delta-without-sy` — measuring U2 with zero host mutation

- **Claims.**
  - (a) [obs] The JSON API and `pacman -Q` show 5 of 5 sampled boot-chain packages behind on 2026-10-19:

    | package | upstream | host |
    |---|---|---|
    | linux | `7.2.11.arch1-1` | `7.2.3.arch1-3` |
    | systemd | `262.1-1` | `261.2-1` |
    | mkinitcpio | `42.2-1` | `41.1-1` |
    | limine | `12.9.3-1` (flagged out of date 2026-10-19) | `12.8.0-1` |
    | pacman | `7.1.0.r9.g54d9411-3` | `-2` |

  - (b) checkupdates never writes `/var/lib/pacman/sync`. It syncs to `${TMPDIR:-/tmp}/checkup-db-${UID}/` with a symlinked `local` via `fakeroot -- pacman -Sy --disable-sandbox-filesystem --dbpath "$CHECKUPDATES_DB" --logfile /dev/null`, then exits 2 when there are no updates (S009, the `if (( SYNC ))` block). This resolves the lane's [inference] at `update-safety-note.md:380-381`. [obs] `fakeroot` is installed (`pacman -Qq fakeroot`).
  - (c) The doctrine-safe operator route is checkupdates or a full `-Syu`, never a bare `-Sy` (see D1).
- **Sources.**
  - S010 § Avoid certain pacman commands: "never run pacman -Sy; instead, always use pacman -Syu."
  - S010 § Partial upgrades are unsupported, Note: "provides a safe way to check for upgrades to installed packages without running a system update".
  - S012 § Package information → Details: "Syntax: /repository/architecture/package/json/".
- **Fills.** U2 "the real gate" (`update-safety-note.md:65-66`; row 14 `UNKNOWN-UPSTREAM` at `:356`); `closeout-r11.md:226` row 5.
- **Boundary.** These are network reads of public pages, so they conflict with the lane's "no external site" discipline. Wave 2 must either amend PROVINCE or keep this as an operator/scout probe. The JSON API does not cover the `[omarchy]` repo [scope limit].
- **Recheck.** `for p in linux systemd mkinitcpio limine pacman; do curl -s "https://archlinux.org/packages/search/json/?name=$p" | jq -r '.results[0]|.pkgname+" "+.pkgver+"-"+.pkgrel'; done; pacman -Q linux systemd mkinitcpio limine pacman`
- **QUALITY.md.** (1) Version strings are falsifiable at capture time. (2) Endpoint plus code location. (3) [obs] capture vs [inf] doctrine reading. (4) The `-Sy` advice is corrected by an appended erratum. (5) Nothing rejected.

### K4 `arch-news-applicability-2025-2026` — the missing "read before upgrading" gate

- **Claim.** 20 Arch news items are dated 2025-01-01 → 2026-10-19. **0 require manual intervention in this host's next `-Syu`.**

  | status | count |
  |---|---|
  | PAST (host already beyond the intervention) | 6 |
  | PENDING but N/A by condition | 1 |
  | ADVISORY, active | 2 |
  | informational | 1 |
  | N/A (package absent) | 10 |

- **Source.** S010 § Read before upgrading the system: "Before upgrading, users are expected to visit the Arch Linux home page to check the latest news". Count: `curl -s https://archlinux.org/news/ | grep -cE '<td>20(25|26)-[0-9]{2}-[0-9]{2}</td>'` → 20.

| date | item | host evidence [obs] | status |
|---|---|---|---|
| 2026-09-22 | mkinitcpio ≥42 TPM2 (S002) | mkinitcpio 41.1-1 (upstream 42.2-1); effective HOOKS busybox `udev`/`encrypt`; bootctl "TPM2 no" (`journal-boot-plane.md:300`) | PENDING, N/A by condition |
| 2026-07-21 | virtualbox-ext-vnc | not installed | N/A |
| 2026-06-12 | AUR malicious packages (S003) | 16 foreign incl. AUR-local; yay installed | ADVISORY (review PKGBUILD diffs) |
| 2026-06-04 | leader election | — | informational |
| 2026-05-25 | varnish → vinyl-cache | not installed | N/A |
| 2026-04-07 | kea | not installed | N/A |
| 2026-04-05 | iptables → nft default | `pacman -Q iptables-nft` resolves to `iptables 1:1.8.13-1`; `.pacsave` census 0 (log `grep -cE 'saved as .*\.pacsave' /var/log/pacman.log` → 0; `/etc/iptables` is world-readable 755, so `find` covers it); ufw host | PAST |
| 2025-12-20 | NVIDIA 590 → open modules | nvidia-open-dkms 610.57.04-1 | PAST |
| 2025-12-11 | .NET 9→10 | dotnet-runtime-10.0 installed | PAST |
| 2025-11-06 | waydroid | not installed | N/A |
| 2025-10-31 | dovecot | not installed | N/A |
| 2025-08-21 | service outages (S004) | single-mirror host (lane U2) | ADVISORY (fallbacks) |
| 2025-08-04 | zabbix | not installed | N/A |
| 2025-06-21 | linux-firmware split | linux-firmware 20260810-2 | PAST |
| 2025-06-20 | Plasma 6.4 X11 | not installed | N/A |
| 2025-06-16 | wine WoW64 | not installed | N/A |
| 2025-04-17 | Valkey replaces Redis | not installed | N/A |
| 2025-02-17 | old repos removed | repo list core, extra, multilib, omarchy (`update-safety-note.md:67-68`) | PAST |
| 2025-02-03 | glibc 2.41 vs Discord | discord not installed | N/A |
| 2025-01-16 | rsync 3.4.0 critical | rsync 3.5.0-1 | PAST |

- **Taste note.** The feed is necessary but not sufficient. The v42 busybox `/sysroot` change that does affect this host (K5) appears only in the release notes, not in the news.
- **Fills.** A new coverage-map row ("news gate") and a missing step in the SKILL update-safety checklist (sweep = 0).
- **Recheck.** `pacman -Q mkinitcpio iptables nvidia-open-dkms dotnet-runtime-10.0 linux-firmware rsync; pacman-conf --repo-list`, plus the curl count above.
- **QUALITY.md.** (1) Each row is falsifiable by `pacman -Q`. (2) Each item is cited. (3) The N/A-by-condition row is [inf]. (4) The entry is append-only per news batch. (5) Nothing rejected.

### K5 `initramfs-flavor-v42-sysroot-and-recovery` — busybox host vs mkinitcpio ≥42, and recovery entry points

- **Claims.**
  - (a) [obs] The effective initramfs is **busybox-based**: drop-in `/etc/mkinitcpio.conf.d/omarchy_hooks.conf:1` (`base udev plymouth keyboard autodetect microcode modconf kms keymap consolefont block encrypt filesystems fsck btrfs-overlayfs`) plus `omarchy_resume.conf:1` (`HOOKS+=(resume)`). `pacman.log:1991-1993` shows "Using drop-in configuration file" for both.
  - (b) [obs] 2 of the 7 effective busybox runtime hooks hardcode `/new_root`:
    - `/usr/lib/initcpio/hooks/btrfs-overlayfs:4` `root_mnt="/new_root"` (limine-mkinitcpio-hook 1.38.0-1.1);
    - `/usr/lib/initcpio/hooks/plymouth:11` `--new-root-dir=/new_root` (plymouth 26.134.222-2).

    Upstream master/main are unchanged as of today (S021 line 4, S022). v41.1 init has 7 `/new_root` refs; v42 init has 0 (S016).
  - (c) [inf] After the pending mkinitcpio upgrade, `btrfs-overlayfs` hits `findmnt --mountpoint "$root_mnt" … || return 0` (S021 line 7) and silently no-ops. A read-only snapshot boot then has no overlay, and S023 warns such boots fail services needing writable `/var`. [unk] how severe plymouth's failed `update-root-fs` is. [unk] whether normal non-snapshot boots are affected. Nothing seen in `init`/`init_functions` v42 suggests a compatibility path.
  - (d) Recovery entry points for this flavor:

    | stage | entry point | source |
    |---|---|---|
    | busybox pre-root, inside the lane's J3 "journal blackout" | `break=premount` / `break=postmount` | S014 |
    | host side, after switch-root | `systemd.break=pre-udev\|pre-basic` (v258), `systemd.debug_shell` (tty9), `rescue`, `emergency`, `init=/bin/sh` | S025, S026 |
    | systemd initrd only — **not** this host | `rd.systemd.break=`, `rd.systemd.debug_shell` | S025 |

- **Sources.**
  - S015 v42 notes § Changes in mkinitcpio: "Busybox-based init now uses /sysroot as the root mountpoint just like the systemd-based one."
  - S014 § Runtime customization: "init pauses the boot process (after loading hooks, but before mounting the root file system) and launches an interactive shell".
  - S025 § systemd.break=: "The option prefixed with "rd." is honored only in the initrd, while the one without prefix is only honored on the host."
  - S026 § Recovery shells: "rescue launches a shell shortly after the root file system is remounted read/write".
- **Fills.** U3 (kernel-wave coupling gains a concrete next-wave regression); boot-plane and journal-boot rows (recovery, sweep 0); J3. Corrects the HOOKS citation at `journal-boot-plane.md:244` (D5).
- **Recheck.** `grep -h '^HOOKS' /etc/mkinitcpio.conf /etc/mkinitcpio.conf.d/*.conf; grep -l '/new_root' $(for h in udev plymouth keymap consolefont encrypt resume btrfs-overlayfs; do echo /usr/lib/initcpio/hooks/$h; done) | wc -l` → 2; `curl -s https://gitlab.archlinux.org/archlinux/mkinitcpio/mkinitcpio/-/raw/v42/init | grep -c '/new_root'` → 0; `pacman -Q mkinitcpio`
- **QUALITY.md.** (1) Claims (a), (b) and the v42 count are falsifiable by grep; (c) is tagged [inf] with its trigger. (2) Code lines are cited. (3) The split is explicit. (4) An erratum is filed for `:244`. (5) Rejected alternative: the "mkinitcpio 42 TPM2 news applies" reading (R5).

### K6 `pacnew-plane` — config drift the lane never measured

- **Claim [obs].** 3 `.pacnew` files are pending, all from the 2026-10-11 wave: `/etc/locale.gen.pacnew` and 2× `/etc/tpm2-tss/fapi-profiles/*.json.pacnew`. 0 `.pacsave` (log census: `grep -cE 'saved as .*\.pacsave' /var/log/pacman.log` → 0). The two census methods agree:
  - log: `grep -cE 'installed as .*\.pacnew' /var/log/pacman.log` → 3 (`pacman.log:1427,1645,1646`);
  - filesystem, non-root: `find /etc \( -name '*.pacnew' -o -name '*.pacsave' \) 2>/dev/null` → the same 3 files, with 12 `Permission denied` dirs skipped (`find … 2>&1 >/dev/null | grep -c 'Permission denied'`).
- **Inferences.**
  - [inf] Low impact: locale config, plus TPM2 profiles on a host without TPM2.
  - [unk] Whether the pending mkinitcpio 42 upgrade writes `/etc/mkinitcpio.conf.pacnew`. It does only if the packaged file changed between 41.1 and 42.2.
- **Sources.** S011 § Why these files are created:
  - "These files require manual intervention from the user and it is good practice to handle them right after every package upgrade or removal."
  - § Locating: "Note that the log does not keep track of the files currently in the filesystem nor the ones that have already been removed" — so both census methods are needed.
- **Fills.** A new package-state coverage row: "config drift (.pacnew/.pacsave)" (sweep = 0). It is also a candidate census arm.
- **Recheck.** The two commands above.
- **QUALITY.md.** (1) Counts carry commands. (2) Sources cited. (3) Impact is [inf]. (4) Append-only. (5) Nothing rejected.

## 5. Paths

- **Rollback net on this host (U1/J4)** — S023 → S018 → S019 → S020 → S028 → S027. Start with snapper concepts and the Arch layout. Then this host's Limine integration. Then the exact unit that fails. Last, the two man pages that explain the denial.
- **Update gate without `-Sy` (U2)** — S010 → S009 → S012 → S001 → S013 → S006 → S005. Order: doctrine; the safe-check mechanism; read-only upstream delta; the news gate; date-pinned rollback; then pacman 7's sandbox and DownloadUser semantics behind the `alpm` download dirs.
- **Boot repair on busybox + LUKS + limine UKI (U3/J3)** — S026 → S014 → S025 → S017 → S015 → S016 → S021 → S022 → S002. Order:
  1. stage model and recovery shells;
  2. initramfs flavors and `break=`;
  3. systemd breakpoints;
  4. the UKI build path;
  5. the pending v42 change and the two hooks it strands;
  6. the TPM2 news, which matters only after a systemd-hook migration.

## 6. Rejected candidates (kept as evidence of taste)

- **R1 Arch Security Tracker (S029) as a current vulnerability source.**
  - [obs] The newest ids on its index are AVG-2901/2904, carrying 2025 CVEs. It lists `systemd 257.6-1` as Vulnerable (AVG-2893) while `[core]` ships 262.1-1.
  - [inf] Stale; `arch-audit` inherits the staleness.
- **R2 status.archlinux.org (opened, not rowed).** The page is JS-rendered; the reader fetch returned "There was an error while fetching the data". Not machine-readable for read-only probes. Use S004 and S001 instead.
- **R3 web_search synthesized answer (S030, tier C).** It fabricated the premise "Your service has `CapabilityBoundingSet=CAP_DAC_OVERRIDE`", which S020 contradicts. The mechanism is re-grounded in S027, S028 and S020 only.
- **R4 web_search synthesized answer on mkinitcpio v40 (opened, not rowed).** It attributes "systemd default since v40" to a third-party README and a forum post. The S015 v40 notes do not state a hook-default change. What is supported: the 41.1 cached package default (systemd) plus S014.
  - [unk] whether the flip came in v40 or v41.
- **R5 "mkinitcpio ≥42 TPM2 re-enroll applies to this host."** It requires the systemd hook plus TPM2-bound LUKS; the host is busybox `encrypt` with no TPM2.
- **R6 "A pre-existing `@.snapshots` explains the snapper failure"** (S023's documented cause). The lane measured no `.snapshots` subvolume, and the error is EACCES, not "already exists".
- **R7 "systemd 262's `journalctl -F` change breaks the census."**
  - `grep -nE 'journalctl[^|]*(\s-F\b|--field)' tools/tsukuroi-census.sh` → 0 matches.
  - The census uses `--list-boots`, `-o json`, `--grep` and `-o short-iso-precise`.

## 7. Defects found (6) and mistake classes mined (4)

**Defects** — each is current art or doctrine contradicting or completing a lane claim. All corrections are new errata; nothing is edited.

- **D1 — bare `-Sy` advised to the operator.** ≥9 lines frame an operator `-Sy` as the U2 resolving step. The sweep below → 9:

  ```bash
  grep -rnE 'sudo pacman -Sy`|[Oo]perator `-Sy`|then `-Sy`|`-Sy` then|`-Sy` and re-run' corpus/knowledge | wc -l
  ```

  - `update-safety-note.md:378`
  - `host-health-report-r3.md:54,314,362`
  - `degraded-triage-r4.md:90,524`
  - `update-safety-v2.md:102,280`
  - `closeout-r11.md:226`
  - plus `driver-firmware-plane.md:192`, which is phrased differently.

  This contradicts S010. Mined: the host itself took one unsupported partial upgrade. `pacman.log:1405` `pacman -Sy --noconfirm fuse2` at 2026-10-11 12:54:13 was followed by the full `-Syu` at 16:13:19 (`:1414`), so the host spent **3 h 19 m 06 s** [computed] in a partial state. The lane recorded the line but never labeled the doctrine breach.
- **D2 — wrong hook-precedence wording, and an unknown left open.** "precedence for earlier hook dirs" (`degraded-triage-r4.md:370`) contradicts S007 ("later directories taking precedence"). The unknown carried at `:546-547` was already answerable from `pacman.log:1989-1990` (K1).
- **D3 — errno 13 left unexplained.** `degraded-triage-r4.md:321-325` records `CapabilityBoundingSet=cap_sys_admin` but never measures the DAC mode of `/`. The sweep for 0555/CAP_DAC_OVERRIDE = 0 (K2).
- **D4 — checkupdates mechanism tagged [inference].** `update-safety-note.md:380-381` says "script is not readable here because the package is absent". The upstream source is readable without installing anything (S009).
- **D5 — wrong HOOKS citation.** `journal-boot-plane.md:244` cites `/etc/mkinitcpio.conf:55` as the host's HOOKS. The effective HOOKS come from the drop-ins (`pacman.log:1991-1993`; recorded later at `degraded-triage-r4.md:358-362`).
- **D6 — census blind spot for `/`.** Package verification cannot see the root directory: `pacman -Qo /` → no owner, and the filesystem mtree has 0 `./` entries. Root-dir mode drift, the J4 cause, is invisible to `-Qkk` and to the census.

**Mistake classes → proposed rules for wave 2**

- **MC1, advice that contradicts distro doctrine (D1).** QUALITY criterion 6: "An operator action naming a pacman verb cites the doctrine row (S010) it follows; bare `-Sy` is never advised."
- **MC2, unknowns carried while the answering evidence is already on disk (D2).** SKILL rule: "Before carrying an [unknown], sweep pacman.log and the journal for the event that would answer it; record the sweep."
- **MC3, a permission denial investigated without the DAC and capability pair (D3).** EACCES checklist:
  1. target dir mode, owner and ACL;
  2. the unit's `CapabilityBoundingSet`;
  3. `ProtectSystem`, `ReadOnlyPaths`, `InaccessiblePaths`;
  4. LSM.
- **MC4, an absent tool treated as an unreadable mechanism (D4).** Rule: "Absent tool ≠ unknown mechanism — read the upstream source or man page (SOURCES row) before tagging [inference]."

Also proposed: QUALITY criterion 7, "external claims cite an S### row with its tier; tier C is never sole support", and criterion 8, "mechanism claims carry a falsifier and every entry a `recheck:`".

## 8. STATE notes observed in passing (for the STATE dossier / wave-2 writer)

- **J4 recurs every boot.** 8 `errno:13` lines from 2026-10-16 to 2026-10-19; the latest is boot `be045967…` at 08:11:47 (command in K2). `/etc/conf.d/snapper` was rewritten at 2026-10-19 08:11 with `SNAPPER_CONFIGS=""`. `/var/log/snapper.log` (mode 640 root, mtime 08:12) is unread.
- **Journal retention moved.** It is now `9` boots (`journalctl --list-boots --no-pager | tail -n +2 | wc -l`); the lane recorded 13.
- **ESP.** 2.0G, 279M used (`df -h /boot`).
- **Limine config.** `/etc/default/limine` has `ENABLE_UKI=yes`, `ENABLE_LIMINE_FALLBACK=yes` and `BOOT_ORDER="*, *fallback, Snapshots"`, and no `MKINITCPIO_FALLBACK` line. [unk] whether a fallback UKI exists: reading `/boot` needs root.
- **Package cache.** It holds only `mkinitcpio-41.1-1`. 42.x has not been downloaded.
- **AUR versions of the omarchy-built helpers.** AUR `limine-mkinitcpio-hook 1.40.0-1` (2026-09-27) vs host 1.38.0-1.1; `limine-snapper-sync 1.32.1-1` (2026-10-03) vs host 1.31.0-1.1. Command: `curl -s 'https://aur.archlinux.org/rpc/v5/info?arg[]=limine-mkinitcpio-hook&arg[]=limine-snapper-sync' | jq -r '.results[]|.Name+" "+.Version'`.

## 9. Measurable deltas wave 2 can claim

Before values were measured 2026-10-19 in the repo root.

- `corpus/SOURCES.md` rows: absent → 0 → up to 30, via `grep -cE '^\| S[0-9]{3} ' corpus/SOURCES.md`. Tiers via the contract's awk command.
- Coverage-map rows: 10 → 10 + k, via ``grep -c '^| `' corpus/README.md``. Candidates: K4 news gate, K6 pacnew plane, K5 recovery/initramfs, K2 blind spot.
- §1.2 sweeps: news 0, pacnew 0, recovery 0, ALA 0, sandbox 0, DAC 0 → ≥1 each, using the same commands.
- Errata correcting D1–D5: 0 → 5, counted as new erratum blocks that cite S010, S007, S027/S028, S009 and the drop-in lines.
- QUALITY criteria: 5 → 8 (§7), via `grep -cE '^[0-9]+\.' corpus/QUALITY.md`.

## Appendix A — read-only probes run by this scout (non-root, 2026-10-19)

- `pacman -Q pacman mkinitcpio systemd limine limine-snapper-sync limine-mkinitcpio-hook snapper btrfs-progs linux linux-firmware nvidia-open-dkms iptables ufw rsync glibc filesystem`
- `pacman -Qq <news-named packages>`; `pacman-conf HookDir`; `pacman -Qo /`
- `ls -la /etc/mkinitcpio.conf.d/`; `grep -Hn '^HOOKS' /etc/mkinitcpio.conf /etc/mkinitcpio.conf.d/*.conf`
- `grep` on `/var/log/pacman.log`: hook runs, drop-ins, `.pacnew` warnings
- `grep -H '^Exec'` on the two 90-mkinitcpio-install hooks
- `find /etc -name '*.pacnew' -o -name '*.pacsave'`
- `stat`/`getfacl` on `/`; `findmnt /`; `df -h /boot`; `findmnt /boot`
- `systemctl cat limine-snapper-sync.service`; `snapper list-configs`; `cat /etc/conf.d/snapper`; `ls -la /var/log/snapper.log /etc/snapper/configs/`
- `journalctl -g` for snapper errors; `journalctl --list-boots`
- `grep` on `/etc/default/limine`
- `zcat` of the `filesystem` mtree; `bsdtar -xOf` of the cached mkinitcpio 41.1 package to stdout
- `grep` on `/usr/lib/initcpio/hooks/*`
- `curl` GETs: archlinux.org news, packages JSON, GitLab raw/API, gitlab.com raw/API, the AUR RPC

Lane-repo greps are listed in §1.2, §6 R7 and D1.
