# Publication hold clarification — 2026-11-02

PROTOCOL.md explicitly defines landed as committed and permits operator-gated publication candidates to remain locally committed until release. It also takes precedence over MISSION.md's unconditional push wording on this conflict. Publication approval is currently pending for subsequent public checkpoints.

Therefore completed non-author review and local, committed fleet closure may precede the next training round while reviewed artifacts remain under the publication hold. The parent-added requirement in the cloud round57/58 prompts to wait for a public checkpoint before the next dispatch was unnecessarily stronger than this existing exception; this dated clarification supersedes that requirement prospectively. It does not change frozen claims, verdicts, reviewed history, or any evidence gate.

For every held round:
- Preserve actual author work, frozen inputs, failed attempts, independent review and append-only closure in committed local history.
- Preserve a verified private checkpoint for recovery.
- Mark public durability as pending; never claim a push, approval, or remote checkpoint that did not occur.
- No public push without the required user approval; no alternate route around a denied action, force push, main merge, new credentials or permissions.
- Continue only after substantive non-author closure; no automatic next-round advancement by the author or fabricated counts.

The current roster scope is unchanged. This permits authorized private training to continue, not unauthorized publication.
