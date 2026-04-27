# Showcase — real outputs from the skills

These are ACTUAL outputs produced by the skills during end-to-end testing. Not curated examples — the raw responses agents produced when given the SKILL.md instructions and a real business problem.

Use this folder to (a) calibrate expectations of what the skills produce, (b) verify the visual contract is enforced consistently, and (c) showcase the skills to a stakeholder before they install.

Every output below scored **6/6** on the [eval suite](../../evals/score.py) — structurally compliant with the visual contract.

---

## Master skills

| File | Skill | Test problem | Score |
|---|---|---|---|
| [vsc-cloud-cost.md](./vsc-cloud-cost.md) | `visual-strategy-consultant` (5-fw) | $180K → $340K/mo cloud cost spike at SaaS company | 6/6 ✅ |
| [vsc7-bank-loan-cycle.md](./vsc7-bank-loan-cycle.md) | `visual-strategy-consultant-7` (7-fw) | Regional bank: loan cycle 14 → 31 days, fintech threat | All 7 sections ✅ |

## Sub-skills (standalone)

| File | Skill | Test problem |
|---|---|---|
| [mece-ecommerce-conversion.md](./mece-ecommerce-conversion.md) | `mece-framework` | Outdoor-gear DTC: conversion 4.1% → 2.7% |
| [issue-tree-oee.md](./issue-tree-oee.md) | `issue-trees` | Manufacturing: OEE 78% → 61% |
| [hypothesis-marketplace-ranking.md](./hypothesis-marketplace-ranking.md) | `hypothesis-driven` | Marketplace: ranking-algorithm conversion drop |
| [pareto-marketing-focus.md](./pareto-marketing-focus.md) | `pareto-principle` | Marketing team: 23 active initiatives, burnout |
| [so-what-support-tickets.md](./so-what-support-tickets.md) | `so-what-test` | 78% of support tickets from features < 90 days old |
| [five-whys-renewal-misses.md](./five-whys-renewal-misses.md) | `five-whys` | CS team missing 40% of renewal-call commitments |
| [pyramid-acquisition-decision.md](./pyramid-acquisition-decision.md) | `pyramid-principle` | Don't acquire competitor X — structure for exec team |

## Industry packs

| File | Skill | Test problem | Score |
|---|---|---|---|
| [vsc-saas-nrr-decline.md](./vsc-saas-nrr-decline.md) | `vsc-saas` | $40M ARR PLG SaaS: NRR 124% → 108% | 6/6 ✅ |

---

## What to read for

The "What to notice" sections in [`../full-runs/`](../full-runs/) and [`../single-frameworks/`](../single-frameworks/) explain how to evaluate output quality. Apply the same questions here:

- Is the MECE genuinely MECE (no overlap, nothing missed)?
- Does the issue tree drill at least 2 levels with testable leaves?
- Does the hypothesis include a control row designed to invalidate it?
- Does the Pareto deprioritize specific things (not just trivia)?
- Is the Insight assignable — could you DM it to a person with a deadline?

For 7-framework outputs, additionally:

- Does the 5 Whys reach a structural cause (not "people are bad" or "the world is hard")?
- Does the Pyramid Principle top-line commit specifically (not "we should consider...")?

---

## How these were generated

Each output was produced by spawning a fresh agent, having it Read the relevant SKILL.md from this repo, and applying it to the test problem. No editing, no curation — what you see is what an installed skill produces on a clean run.

Re-running the tests is straightforward — the prompts are simple ("read this SKILL.md, apply it to this problem, output only the structured response"). See [TESTING.md](../../TESTING.md) for the full testing methodology.
