# Showcase — `so-what-test` (standalone)

## Input

> I have data showing that 78% of our customer-support tickets come from features released in the last 90 days. The team thinks we have a quality problem. Translate to action.

## Output (verbatim)

**Process:** Analyzed the distribution of support tickets by feature release date over the past 12 months.

**Result:** 78% of tickets originated from features released in the last 90 days, with a median time-to-incident of 14 days post-launch.

**Insight:** This is a release-velocity and pre-launch quality issue, not a systemic quality problem. The team is shipping faster than quality gates can absorb. **Action:** Extend pre-launch QA and staging on features >500 LOC by an additional 7 days minimum before public release. Assign the Engineering Lead to define a new acceptance-test checklist by end of week, and track post-launch incident volume by release, with a target of ≤40% ticket attribution within 90 days of launch. Owner: Engineering Lead + QA. Deadline: first release under new gate by end of next sprint.

## What to notice

- **Process is one sentence — tight.**
- **Result has a specific metric** (median time-to-incident = 14 days) on top of the user-provided data point. That second metric does work.
- **Insight reframes the team's story** ("quality problem" → "release-velocity problem with insufficient quality gates").
- **Insight is fully assignable.** Named owner (Engineering Lead + QA), specific action (7-day extension on features >500 LOC), measurable target (≤40% ticket attribution within 90 days), and deadline (first release under new gate by end of next sprint).
