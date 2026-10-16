"""Render the lead-authored, fixed final-review assignments for one pin."""

import json
from pathlib import Path
import re
import sys


pin = sys.argv[1]
if not re.fullmatch(r"[0-9a-f]{40}", pin):
    raise SystemExit("expected a full frozen commit id")
wave = Path(__file__).resolve().parent
directive = Path(
    "/home/vgpnk/Projects/ufo-fsd-alpha/.cursor/skills/godspeed/directive.md"
).read_text()
context = (
    "/skill:godspeed\n"
    + directive
    + "\nFIRST TOOL ACTION: invoke glmseat. Then read the lead-authored "
    + f"assignments {wave / 'review-common.md'} and "
    + f"{wave / 'review-roles.md'} (your role section only). "
    + f"The planning/data-walk artifact is {wave / 'wwkd-plan.md'}. "
    + "You are a leaf shokunin recovery reviewer, not a UFO mission/judge. "
    + "No routing edits, descendant agents, live source edits or shipping."
)
items = []
for number, flag in (
    (93, "ebur-r93"),
    (98, "pwstream-r98"),
    (99, "rtp-r99"),
    (100, "sofa-r100"),
):
    for role in ("critic", "reviewer", "verifier", "simplifier", "scribe"):
        taxonomy = "reviewer" if role == "verifier" else role
        report = (
            "/home/vgpnk/Projects/shokunin/audio-shokunin/"
            f"reports/round-{number}/r{number}-{role}.md"
        )
        task = (
            f"Assigned round N={number}; assigned role ROLE={role}; "
            f"frozen source PIN={pin}; existing family FLAG={flag}. "
            f"Write only your assigned report {report} and your scratch "
            f"/home/vgpnk/Projects/shokunin/audio-waveb-resume/r{number}-{role}/. "
            "Execute exactly the common assignment and your role section. "
            "For verifier only: substitute these literal N/PIN/FLAG values "
            "in the fixed export/run recipe. All other roles run no live "
            "families. Never set RTP_R99_ALLOW_LAN_CONTROL. "
            "Runtime: the prior operator family jobs are finished; shared "
            "daemons may remain running and must not be restarted. "
            "Preserve existing services and all evidence. | godspeed"
        )
        items.append(
            {
                "name": f"AudioR{number}{role.title()}",
                "role": taxonomy,
                "prompt": task,
            }
        )
spec = {
    "wave": "shokunin-train-20261016-w24-audio-final-reviews",
    "context": context,
    "maxLanes": 20,
    "axes": ["depth", "coverage", "calibration", "operability"],
    "milestone": "Independent final audio reviews, no shipping authority",
    "items": items,
}
(wave / "spec.json").write_text(json.dumps(spec, indent=2) + "\n")
