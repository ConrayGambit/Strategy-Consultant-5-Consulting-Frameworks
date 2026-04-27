# Showcase — `issue-trees` (standalone)

## Input

> Build an issue tree for: Our manufacturing plant's overall equipment effectiveness (OEE) has dropped from 78% to 61% over the past two quarters.

## Output (verbatim)

```text
OEE 78% → 61% Decline
├── Equipment Availability
│   ├── Mechanical failures increasing
│   ├── Scheduled maintenance backlogs
│   └── Unplanned downtime spikes
├── Performance / Speed
│   ├── Cycle time creeping upward
│   ├── Operator skill degradation
│   └── Settings drift from baseline
└── Quality / Defect Rate
    ├── Scrap rate acceleration
    ├── Rework volume increasing
    └── Root cause variability rising
```

## What to notice

- **MECE at the root.** The three branches map to the three OEE components (Availability × Performance × Quality). Domain-correct decomposition.
- **Two levels deep.** Three sub-factors per branch, each testable from plant-floor data.
- **Box-drawing characters used correctly** (`├──`, `│`, `└──`).
- Standalone use — no MECE, no hypothesis, no Pareto. Just the tree, as the skill specifies.
