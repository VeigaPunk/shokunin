# r76 SCRIBE (g2d) — evidence audit + receipt provenance

Read SHARED.md. Audit the lane's evidence integrity for r75->r76:
- verify the landed r75 receipts: re-parse every r75 iw-*.stdout.txt in
  the author/verifier/reviewer run dirs; confirm the pinned values are
  byte-derivable; flag any receipt whose pin can't be re-derived
  (provenance hole).
- verify the r75 fold delta claims: the only receipt diffs should be
  mode=unp on the two twins + unpinned traceback line drift on the two
  fatal rows + srcline on wp. Anything else is a discrepancy — report it.
- witness-gap followup: per-cell rc is now persisted in verdicts.json
  (r75 fold) — confirm the field exists and discriminates fatal/died.
- enumerate uncommitted-vs-committed scratch provenance: which cited
  receipts exist on disk, which are committed, which are claimed but
  absent.
Report -> reports/round-76/r76-scribe.md.
