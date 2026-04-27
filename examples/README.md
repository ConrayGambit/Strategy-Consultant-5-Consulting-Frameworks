# Examples

Real input/output pairs showing what the skills produce. Use these to (a) verify your install works, (b) see how the frameworks flex across industries, and (c) calibrate your expectations of what good output looks like.

---

## Featured: full end-to-end run

| File | Industry | Problem |
|---|---|---|
| [example-analysis.md](./example-analysis.md) | B2B SaaS | Sales cycle stretching from 60 to 110 days |

This is the canonical example — it walks through a complete output of the master skill on a complex multi-stakeholder problem, including a reframe-the-question move at the top.

---

## Showcase — actual outputs from skill testing

[`showcase/`](./showcase/) contains real outputs produced during end-to-end skill testing — not curated demos, but the raw responses agents gave when handed a SKILL.md and a real business problem. Every full-master output passed the eval suite at 6/6. **Use this folder to see what the skills actually produce before you install.**

| File | Skill | Problem |
|---|---|---|
| [showcase/vsc-cloud-cost.md](./showcase/vsc-cloud-cost.md) | `visual-strategy-consultant` (5-fw) | $180K → $340K/mo cloud cost spike |
| [showcase/vsc7-bank-loan-cycle.md](./showcase/vsc7-bank-loan-cycle.md) | `visual-strategy-consultant-7` (7-fw) | Bank loan cycle 14 → 31 days, fintech threat |
| [showcase/vsc-saas-nrr-decline.md](./showcase/vsc-saas-nrr-decline.md) | `vsc-saas` (industry pack) | $40M ARR PLG SaaS, NRR 124% → 108% |
| [showcase/mece-ecommerce-conversion.md](./showcase/mece-ecommerce-conversion.md) | `mece-framework` | DTC e-commerce conversion drop |
| [showcase/issue-tree-oee.md](./showcase/issue-tree-oee.md) | `issue-trees` | Manufacturing OEE 78% → 61% |
| [showcase/hypothesis-marketplace-ranking.md](./showcase/hypothesis-marketplace-ranking.md) | `hypothesis-driven` | Marketplace ranking-algorithm conversion drop |
| [showcase/pareto-marketing-focus.md](./showcase/pareto-marketing-focus.md) | `pareto-principle` | Marketing team with 23 active initiatives |
| [showcase/so-what-support-tickets.md](./showcase/so-what-support-tickets.md) | `so-what-test` | Support tickets concentrated in new features |
| [showcase/five-whys-renewal-misses.md](./showcase/five-whys-renewal-misses.md) | `five-whys` | CS team missing 40% of renewal commitments |
| [showcase/pyramid-acquisition-decision.md](./showcase/pyramid-acquisition-decision.md) | `pyramid-principle` | Don't acquire competitor X — exec memo |

See [showcase/README.md](./showcase/README.md) for the full index.

---

## Full master runs (different industries)

These are end-to-end runs of `visual-strategy-consultant` showing how the master skill flexes across very different contexts.

| File | Industry | Problem |
|---|---|---|
| [full-runs/retail-comp-store-decline.md](./full-runs/retail-comp-store-decline.md) | Retail / hospitality | 47-location coffee chain with 6% YoY same-store-sales decline |
| [full-runs/nonprofit-donor-attrition.md](./full-runs/nonprofit-donor-attrition.md) | Nonprofit | Environmental nonprofit losing 23% of recurring monthly donors |
| [full-runs/manufacturing-defect-rate.md](./full-runs/manufacturing-defect-rate.md) | Manufacturing | Industrial-pump defect rate spiked 1.2% → 3.6% in 90 days |
| [full-runs/government-permit-backlog.md](./full-runs/government-permit-backlog.md) | Government / public sector | City building-permits department, 4,300 backlog, 21d → 74d cycle |
| [full-runs/logistics-shipment-delays.md](./full-runs/logistics-shipment-delays.md) | Logistics / 3PL | OTD dropped 96% → 81%, 38%-revenue customer threatening RFP |

---

## Single-framework demos

These show what each individual sub-skill produces on its own, in a domain different from what's used in the SKILL.md file itself.

| File | Framework | Industry |
|---|---|---|
| [single-frameworks/mece-restaurant.md](./single-frameworks/mece-restaurant.md) | MECE | Restaurant — declining lunch covers |
| [single-frameworks/issue-trees-healthcare.md](./single-frameworks/issue-trees-healthcare.md) | Issue Trees | Healthcare — 30-day readmissions rising |
| [single-frameworks/hypothesis-driven-fintech.md](./single-frameworks/hypothesis-driven-fintech.md) | Hypothesis-Driven | Fintech — card decline rate spike |
| [single-frameworks/pareto-content-creator.md](./single-frameworks/pareto-content-creator.md) | Pareto | Content creator — which channels drive subscribers |
| [single-frameworks/so-what-edtech.md](./single-frameworks/so-what-edtech.md) | So What? | EdTech — course completion rates |

---

## How to read these

Each example file follows this structure:

```markdown
# Title

## Input (what the user typed)
> [verbatim user prompt]

## Output (what the skill produced)
[the structured response]

## What to notice
[a few bullets calling out the moves the skill made]
```

The "What to notice" section is the most useful part — it teaches you how to evaluate whether your output is good, not just what it should look like.

---

## Want to contribute an example?

PRs welcome. Pick an industry not yet represented (logistics, biotech, gaming, government, sports, agriculture, etc.) and submit:

1. A realistic 2–3 sentence problem statement as input
2. The output produced by running the master skill (or one sub-skill) on that input
3. A short "What to notice" section calling out judgment calls or framework flexes worth highlighting

See `CONTRIBUTING.md` (coming soon) or just open a PR.
