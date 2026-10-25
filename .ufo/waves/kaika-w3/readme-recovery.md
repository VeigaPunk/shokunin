# Aggregate README ownership recovery

ReadmeOwnershipProbe reconstructed both successful basename edits byte-exactly: all root README changes were from KaikaAggregateR12, with no unrelated user delta. Root draft MD5 `01b90164f06a6d5a35d50cf71faa5b17` (8554 bytes) was preserved at `.tower/quarantine/kaika-fleetroot-20261019/aggregate-README.md`, then transferred to the assigned aggregate worktree by absolute path. Parent corrected its inverted authority paragraphs there. Only after preservation, the original root README was restored to its unchanged HEAD blob, MD5 `6b15b3cb6e834c04fe6b6e581663933a`. Final corrected README will land through the aggregate branch; no user change was discarded.

All future worker edits use absolute assigned paths. Source record: `readme-ownership.md`.
