# souji — round 11 (census contract + recertification attempt)

Lane HEAD at closure: see the r11 commit. Dispatch: 32 seats on
devin/glm-5-3-flash-max; 31 completed, 1 aborted.

## Verdict: REJECTED as a round — fix landed; certification NOT granted

**O1 census contract (verified):** tools/souji-census.sh now refuses
empty/blank-led/malformed --compare priors (exit 2, distinct messages);
selftest 36/36; all three cert-16 regression shapes refuse. The last open
r9 defect class is closed in the tools.

**O1-certification (NOT granted):** the certifier fleet compromised
evidence integrity — cert-16.json used as a shared relay (overwritten
repeatedly), CERTIFIED verdicts attached to bytes other than those
measured, and a check-count-based candidate selection that picked a
failing candidate. Fail-closed discipline: no certification on
compromised evidence. Full detail in corpus/lessons/round-11.md and
census/round-11/final-27..32.json + dissent.

**C1 rubric:** six independent appliers ran rubric-final.md; scores stay
UNRATED pending a clean certification pass.

## SHONEN
- [~] SKILL.md — census contract pinned; tools' contracts are code, not prose.
- [~] End-to-end task — the last r9 class closed; certification protocol gaps found.
- [~] Executable without oral context — 31 zero-context seats.
- [~] No cross-domain bleed.
