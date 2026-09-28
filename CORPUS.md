# Shokunin Corpus Contract

Every shokunin repo carries a proprietary corpus — knowledge about its domain
*and* training lessons about itself. It is the shokunin's memory; it must never
contain generic filler.

## Layout (per child repo)

```
corpus/
  README.md        — index: what's here, coverage map, known gaps
  knowledge/       — domain facts, sourced notes, decision records
  lessons/         — training lessons: what worked/failed this round and why
```

## Rules

- `knowledge/` entries cite a source: file path, command output, or URL.
- `lessons/` entries cite the round and the evidence (LOG.md round, commit, report).
- A corpus entry is falsifiable or marked opinion; no unverifiable claims.
- The aggregator reviews every corpus each round and files gaps as lessons.
