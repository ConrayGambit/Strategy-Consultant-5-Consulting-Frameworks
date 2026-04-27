# Showcase — `hypothesis-driven` (standalone)

## Input

> Build a hypothesis test for: Our marketplace's search-to-purchase conversion has dropped from 8.2% to 5.4% after we relaunched our ranking algorithm 6 weeks ago.

## Output (verbatim)

**Hypothesis:** The new ranking algorithm is deprioritizing products with higher conversion velocity, causing users to encounter lower-converting items earlier in results.

| Variable | Expected (if hypothesis true) | Actual / Required Data |
|---|---|---|
| Conversion rate by product rank position | Products in positions 1-3 should show steeper decline than positions 4-10 | Need segment conversion by rank band pre/post relaunch |
| Click-through rate vs. conversion | CTR stable or rising, but conversion per click falling | Compare pre/post CTR and conversion per session click |
| Search queries with high historical conversion | These should show sharper decline than low-conversion queries | Segment results by historical query performance |
| Dwell time on product detail pages | No material change — users still engaging similarly | Track page session duration pre/post to verify |
| Algorithm ranking factor weights | Top-converting products weighted lower in new model | Pull algorithm config: pre/post factor importance scores |
| User satisfaction scores (control) | Should be stable if hypothesis is false and quality is maintained | Survey data or NPS trend to rule out perceived quality drops |

## What to notice

- **Falsifiable hypothesis.** "Algorithm is deprioritizing high-converting products" — provable or refutable from rank/conversion data.
- **Control row included** (last row): user satisfaction should be stable; if it's tanking, the hypothesis is refuted and the issue is broader (e.g., a quality problem, not a ranking problem).
- **6 rows total** — within the 4–7 default. Each row points to specific data sources or analyses.
- The 5th row pinpoints WHERE the answer lives if the hypothesis is true: pull the algorithm config and check factor weights.
