<!-- round-2 AUDIT lane B — re-execution of round-1 verify commands. All commands re-run read-only on the live host; outputs below are the auditor's actual bytes, not the round-1 record. -->

## File: corpus/knowledge/2026-10-13-pe-surface.md

### Verify: `find /usr /opt ~ -maxdepth 6 \( -name '*.exe' -o -name '*.dll' \) 2>/dev/null | wc -l`
- result: confirmed — output `413`, matches claimed count exactly.

### Verify: `file ~/.local/share/godot/export_templates/4.7.2.stable/*.exe ~/.cache/uv/archive-v0/*/setuptools/*.exe`
- result: confirmed — 12 Godot exes (x86_32/x86_64/arm64 × debug/release × console/GUI, Intel i386 / x86-64 / ARM64) plus 8 setuptools exes (cli/gui × 32/64/arm64 + cli.exe/gui.exe stubs). Three ISAs observed via file(1) as claimed; PDB-stripped binaries noted on x86_32/x86_64 Godot builds.

### Verify: `file /usr/share/dotnet/shared/Microsoft.NETCore.App/9.0.19/System.Console.dll`
- result: confirmed — `PE32+ executable for MS Windows 4.00 (DLL), Unknown processor 0xfd1d Mono/.Net assembly, 3 sections`.

### Verify: `readelf -h /usr/share/dotnet/shared/Microsoft.NETCore.App/9.0.19/System.Console.dll; echo $?`
- result: confirmed — `readelf: Error: Not an ELF file - it has the wrong magic bytes at the start`, exit 1.

### Verify: `objdump -f .../windows_release_x86_64.exe; llvm-readobj --file-headers .../setuptools/cli-64.exe | head -20`
- result: confirmed — `file format pei-x86-64`, `architecture: i386:x86-64`, `start address 0x0000000140001470`; llvm-readobj: `Format: COFF-x86-64`, `Machine: IMAGE_FILE_MACHINE_AMD64 (0x8664)`, `SectionCount: 6`.

### Verify: `which wine wine64; pacman -Q wine`
- result: confirmed — both not on PATH; `error: package 'wine' was not found` (pacman exists on this host).

### Verify: `ls .../support/analyzeHeadless; unzip -l .../Base.jar | grep 'opinion/PeLoader.class'; java -version`
- result: confirmed — analyzeHeadless present; `39640  2026-09-21  ghidra/app/util/opinion/PeLoader.class`; `openjdk version "21.0.12.1" 2026-08-18`.

### Verify: `dotnet --list-runtimes; which mono wine`
- result: confirmed — `Microsoft.NETCore.App 9.0.19` and `10.0.11`; mono and wine both absent.

### Verify: `for t in rabin2 r2 radare2 rz-bin mono monodis pedump; do command -v $t ...`
- result: confirmed — all MISSING (also re-checked xxd: MISSING, consistent with the claim's 17-tool sweep).

### Verdict audit: agree — all 8 `admit` verdicts re-verify byte-for-byte on the live host; observed/inferred separation is honest (the PeLoader end-to-end import correctly stays INFERRED; the wine-absence claim correctly keeps qemu/box86 out of scope).

## File: corpus/knowledge/2026-10-13-ghidra-install.md

### Verify: `grep -E 'application\.(version|release\.name|build\.date|revision\.ghidra|java\.min)' .../Ghidra/application.properties`
- result: confirmed — `version=12.1.4`, `release.name=PUBLIC`, `build.date=2026-Sep-21 1613 UTC`, `revision.ghidra=8b6bbb857accdfa20dc5b2f5dea471178c2e9fbc`, `java.min=21`.

### Verify: `ls ~/.local/opt/ghidra_12.1.4_PUBLIC/ && du -sh ...`
- result: confirmed — full distribution tree (Ghidra, support, server, Extensions, docs, GPL, licenses, docker, ghidraRun, bom.json, GettingStarted.{html,md}, LICENSE); `876M`.

### Verify: `file .../support/analyzeHeadless && grep -nE 'MAXMEM_DEFAULT|LAUNCH_MODE|headless' ... | head`
- result: confirmed — Bourne-Again shell script; `MAXMEM_DEFAULT=2G`, `LAUNCH_MODE=fg`, `-Djava.awt.headless=true`, `ParallelGCThreads=2`, `CICompilerCount=2`.

### Verify: `ls .../Ghidra/Processors/ | wc -l && ls .../x86/data/languages/*.sla`
- result: confirmed — `39`; `x86.sla` + `x86-64.sla` present.

### Verify: `file .../Decompiler/os/linux_x86_64/decompile && ls .../Decompiler/os/`
- result: confirmed — `ELF 64-bit LSB executable, x86-64, ... not stripped`; os/ contains only `linux_x86_64` and `win_x86_64`.

### Verify: `java -version 2>&1 | head -1 && grep application.java.min .../application.properties`
- result: confirmed — `openjdk version "21.0.12.1" 2026-08-18` vs `application.java.min=21` (floor met exactly).

### Verify: `ls .../Ghidra/Features/ | wc -l`
- result: **drifted** — actual count is `34`, not the claimed `35`. The enumerated list in the claim is itself 34 names, and the live directory contains exactly those 34 (Base, BSim, …, WildcardAssembler — PyGhidra, FunctionID, PDB, VersionTracking all present). The module *list* is complete and accurate; only the count digit is wrong.

### Verify: `ls .../support/`
- result: confirmed — bsim/bsim_ctl, GhidraGo, pyghidraRun, jshellRun, sleigh, convertStorage, ghidraClean, ghidraDebug, buildGhidraJar, launch.sh/LaunchSupport.jar all present.

### Verdict audit: agree — 7 of 8 admits fully confirmed. On the features candidate: agree-with-correction — `admit` is the right verdict (every named module exists; PyGhidra/BSim/FunctionID verified present), but the literal claim "contains 35 modules" is false by one; the count should be amended to 34 in curation so the corpus doesn't propagate the off-by-one.

## File: corpus/knowledge/2026-10-13-java-runtime.md

### Verify: `/usr/lib/jvm/java-21-openjdk/bin/java -version && .../javac -version && ls -la /usr/lib/jvm/`
- result: confirmed — `openjdk 21.0.12.1`, `javac 21.0.12.1`; `/usr/lib/jvm` holds `default -> java-21-openjdk`, `default-runtime -> java-21-openjdk`, and the single real dir `java-21-openjdk`. Exactly one JDK, full (javac present).

### Verify: `java -version 2>&1 | head -1; readlink -f "$(which java)"; echo "JAVA_HOME=$JAVA_HOME"`
- result: confirmed — same build on PATH; `/usr/bin/java` resolves to `/usr/lib/jvm/java-21-openjdk/bin/java`; `JAVA_HOME=/usr/lib/jvm/java-21-openjdk`. No split-brain.

### Verify: `grep -rn JAVA_HOME ~/.bashrc ~/.profile ~/.bash_profile`
- result: confirmed — `.bashrc:24` and `.profile:4` both export the identical value; `.bash_profile` produces no matches (absent).

### Verify: `sed -n '46,56p' .../GettingStarted.md; grep -n "requires a JDK" .../support/launch.properties`
- result: confirmed — line 54 region: `Java 21 64-bit Runtime and Development Kit (JDK)`; `launch.properties:4` `Ghidra requires a JDK to launch.`

### Verify: `sed -n '98,106p' .../GettingStarted.md; grep -n "JAVA_HOME_OVERRIDE" .../launch.properties; grep -n "launch.sh" .../ghidraRun`
- result: confirmed — Java Notes state JAVA_HOME takes precedence over PATH; `launch.properties:5` `JAVA_HOME_OVERRIDE=` empty; `ghidraRun:29` invokes `support/launch.sh bg jdk ...`.

### Verify: `ls /usr/lib/jvm/ | wc -l; sed -n '147,166p' .../support/launch.sh`
- result: confirmed — `3` entries (2 symlinks + 1 real JDK, as the claim describes); launch.sh range shows the fail-closed path including `ERROR: Failed to find a supported JDK.` — a distro JDK removal would strand Ghidra as claimed.

### Verify: `grep -n "Java, Ghidra" ~/.agents/skills/reverse-engineer-anything/SKILL.md; command -v jadx ida64`
- result: confirmed — SKILL.md line 40 lists `Java, Ghidra, IDA, JADX, Binwalk or Unblob`; `jadx` and `ida64` both absent from PATH (the claim only scoped Java+Ghidra — no overclaim).

### Verdict audit: agree — all 7 `admit` verdicts re-verify exactly; the dual-export drift hazard (`.bashrc:24` + `.profile:4`) and single-JDK fragility are real, falsifiable facts on this host.

## File: corpus/knowledge/2026-10-13-elf-observation-jq.md

### Verify: `file /usr/bin/jq && readelf -h /usr/bin/jq | grep -E 'Class|Data|Type|Machine|ABI'`
- result: confirmed — `ELF 64-bit LSB pie executable, x86-64, ... interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=cc56d2fd644ddd549b5339882e77f22f781525d3, for GNU/Linux 4.4.0, stripped`; ELF64 / little-endian / System V / DYN / X86-64. Header sha256 `e8156675…f7806`, size 30800, mode 0755 root:root — all match the file's recorded identity.

### Verify: `readelf -d /usr/bin/jq | grep NEEDED && readelf -x .interp /usr/bin/jq`
- result: confirmed — exactly `libjq.so.1`, `libonig.so.5`, `libc.so.6`; `.interp` hex dump at file offset `0x3ac` = `/lib64/ld-linux-x86-64.so.2` (28 bytes NUL-terminated).

### Verify: `readelf -S /usr/bin/jq | grep -c symtab; readelf --string-dump=.gnu_debuglink /usr/bin/jq`
- result: confirmed, with a footnote — `grep -c symtab` prints `0` (not the `1` the candidate's suggested-note hedged; `.dynsym` does not contain the substring `symtab`, and `grep -w symtab` prints nothing, exit 1 — no `.symtab`, consistent with `stripped`). `.gnu_debuglink` = `[0] jq.debug` + CRC row. Section count is 28 as recorded.

### Verify: `strings -a /usr/bin/jq | grep -c 'jq-1\.8\.2'` ; `/usr/bin/jq --version`
- result: confirmed — count `0` (no stored literal; only `jq - commandline JSON processor [version %s]` template present); runtime prints `jq-1.8.2`. Two-sided claim holds.

### Verify: `readelf -d /usr/bin/jq | grep -E 'FLAGS|RELR'`; `readelf -n /usr/bin/jq | grep -E 'IBT|SHSTK|baseline'`
- result: confirmed — `FLAGS BIND_NOW`, `FLAGS_1 NOW PIE`, `RELR 0x1890`, `RELRSZ 24`, `RELRENT 8`; notes show `x86 feature: IBT, SHSTK`, `x86 ISA needed: x86-64-baseline`. Minor raw-note discrepancy: the file's OBSERVATION block records `x86 feature used: x86, XMM`; the current binary emits `x86 ISA used: x86-64-baseline` — the verified claim (IBT/SHSTK/baseline) is unaffected. Audit bonus: ran the file's own pending check `readelf -lW /usr/bin/jq | grep GNU_RELRO` → `GNU_RELRO 0x006b70 … R` present, so the "full RELRO" inference the file deliberately left unverified is now confirmed (BIND_NOW + PT_GNU_RELRO both hold).

### Verify: `readelf -h /usr/bin/jq | grep Entry`; `nm -D /usr/bin/jq | grep -w main`  ← the reject's prescribed command
- result: confirmed — `Entry point address: 0x3cf0`; `nm -D` lists 79 dynamic symbols and `grep -w main` returns **empty, exit 1**, exactly as the reject predicted. Independent confirmation: `objdump -d --start-address=0x3cf0` shows the canonical `_start` prologue — `endbr64; xor %ebp,%ebp; lea -0x1cef(%rip),%rdi  # 2020 <main>; call *__libc_start_main@GLIBC_2.34` — i.e., the entry is `_start` and `main` is a *different* address (0x2020) passed as an argument. The rejected claim is not merely unproven; it is affirmatively false.

### Verdict audit: agree — all 5 `admit`s re-verify (with the two trivial raw-note slips above flagged, neither affecting a claim). **The REJECT is itself correct**: `readelf -h` reports `e_entry` as a bare address with no symbol binding; in a stripped PIE that address is the `_start` thunk, and the prescribed `nm -D | grep -w main` is empty while the dynamic table demonstrably has 79 symbols (a true negative, not an empty table). Disassembly seals it — 0x3cf0 is `_start`, `main` lives at 0x2020 via `__libc_start_main`. This is the canonical inference-laundering failure the lane exists to catch, and the reject's predicted evidence reproduced exactly.

## Summary

- 4 files audited, **26 verify commands re-executed** (every `verify:` line plus the reject-prescribed `nm -D | grep -w main` and two audit-initiated extras: `readelf -lW | grep GNU_RELRO`, `objdump -d` at the entry point).
- **Confirmed: 25/26.** One drift: `Ghidra/Features` contains **34 modules, not 35** — the claim's enumerated list is complete and correct; only its count is off by one. Recommend amending the digit; the `admit` verdict stands on substance.
- Minor raw-observation slips that do not affect claims: the `grep -c symtab` hedge predicted `1`, actual `0` (claim still proven); the jq `.note.gnu.property` block records `x86 feature used: x86, XMM`, actual `x86 ISA used: x86-64-baseline`.
- **The deliberate REJECT ("entry point 0x3cf0 is main") is correct** — its prescribed verify produced the predicted empty result against a non-empty 79-symbol dynamic table, and disassembly at 0x3cf0 shows `_start` passing `main` (0x2020) to `__libc_start_main`. Entry ≠ main: the rejected claim is false, not just unevidenced.
- Audit-initiated upgrade: the file's deliberately-unverified "full RELRO" inference now has its missing leg — `PT_GNU_RELRO` program header observed; BIND_NOW + RELRO both hold.
- Round-1 discipline verified end-to-end: observations reproduce verbatim, inferences stayed labeled, and the one retained reject is a sound calibration entry.
