# Lead-Authored Host Lock And Summary Repair

Status: implementation contract, not a completed repair.

All final-family and r91/r92/r96/r97 lock callers ignore None. Existing
locks are tree-relative, unbounded and silent on open failure. The lead
has read all four final-family helpers and verified these signatures in
the current source. The r90/r95 proven helpers are deliberately unchanged.

Add `import stat` with the top-level imports. Add this exact helper
before _pwstream_r98_family_lock:

```python
def _audio_host_family_lock(family, wait_s=30.0):
    """Bounded per-user/per-family exclusion, independent of checkout/env."""
    if re.fullmatch(r"[a-z0-9-]+", family) is None:
        raise ValueError("invalid audio family lock name")
    path = Path("/tmp") / f"shokunin-audio-{os.getuid()}-{family}.lock"
    fd = None
    try:
        fd = os.open(str(path), os.O_RDWR | os.O_CREAT | os.O_NOFOLLOW, 0o600)
        meta = os.fstat(fd)
        if (meta.st_uid != os.getuid() or not stat.S_ISREG(meta.st_mode)
                or meta.st_nlink != 1 or meta.st_mode & 0o077):
            raise OSError("non-private or non-regular family lock")
        deadline = time.monotonic() + max(0.0, wait_s)
        while True:
            try:
                fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
                break
            except BlockingIOError:
                remain = deadline - time.monotonic()
                if remain <= 0:
                    raise RuntimeError(
                        f"audio family lock {family}: wait timed out")
                time.sleep(min(0.05, remain))
        os.ftruncate(fd, 0)
        os.write(fd, f"pid={os.getpid()} family={family}\n".encode())
        return fd
    except (OSError, RuntimeError) as exc:
        if fd is not None:
            os.close(fd)
        raise RuntimeError(f"audio family lock {family} unavailable: {exc}") from exc
```

Replace each of these eight helper bodies with the exact three-line
wrapper template below. Preserve its existing no-argument signature.

| existing helper | literal family |
| --- | --- |
| _gstfrz_r91_family_lock | gstfrz-r91 |
| _fc92_family_lock | filterchain-r92 |
| _ebur_r93_family_lock | ebur-r93 |
| _pulsecli_r96_family_lock | pulsecli-r96 |
| _wppol_r97_family_lock | wppol-r97 |
| _pwstream_r98_family_lock | pwstream-r98 |
| _rtp_r99_family_lock | rtp-r99 |
| _sofa_r100_family_lock | sofa-r100 |

```python
def HELPER():
    """Require the shared host-global bounded family lock."""
    return _audio_host_family_lock("FAMILY")
```

Do not run or change a native UFO judge, routing or score. This is the
audio fixture's Unix flock only. Never unlink a real family's lock file.
A timeout/open refusal raises before any family entry starts; it cannot
silently launch unlocked. It is a named hard refusal, not a fabricated
measurement receipt. This prerequisite hard-refusal path can exit with
stderr before the main receipt writer; universal receipt-on-exception
containment is a separately disclosed remaining fold, not part of this
lock fix. Existing return-fd lifetime (until process exit)
is unchanged. The timeout is runtime exclusion policy, not a domain
measurement band.

At main's final summary, preserve failed construction and bool(failed).
Add exactly this blocked mapping and additive JSON field:

```python
    blocked = {k: v["coverage_blocked"] for k, v in measurements.items()
               if v.get("coverage_blocked")}
    print(json.dumps({"receipt": str(out / "measurements.json"),
                      "failures": failed, "coverage_blocked": blocked}))
```

Do not infer measured coverage from dictionary sizes, change partial-block
exit semantics, or alter the receipt format. The CLI will now disclose
its already-receipted blocks instead of displaying failures:{} alone.

## Mechanical Verification Recipe

Copy the lead-authored host-lock-test.py from this directory verbatim to
corpus/fixtures/test_audio_host_lock.py. Its synthetic lock names include
a uuid and never name a production family. It touches no audio/network.
Run it after the patch; the original missing helper is already covered
by the final verifiers' direct unlocked-export observations, so do not
claim a missing-function baseline as empirical proof of those failures.

Keep source-before/source-after copies and exact source-only diff in a
fresh proof directory. Compile source/test via compile(); run the test
with python3 -B, retain raw stdout/stderr/rc. Preserve r97's accepted diff.
No live family, report edit, commit, push, service change or history
operation in this mechanical step.
