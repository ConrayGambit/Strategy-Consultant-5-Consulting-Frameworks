# Industry Packs

Variants of the master skill tailored to specific industries. Each pack adds:

- **Industry-aware MECE categories** — defaults that fit the industry (e.g., a SaaS pack defaults to ARR/NRR/churn dimensions; a retail pack defaults to comp store / traffic / ticket / mix).
- **Common root-cause patterns** — the diagnostic priors that experienced operators in that industry would carry into any problem.
- **Native metric vocabulary** — the right terms (NRR, AOV, OTD, NPS, ALOS, SSS) so the output reads like an industry insider's analysis.
- **Industry-specific examples** in the SKILL.md body.

These are **alternative masters**, not additional steps. Use the industry pack instead of the generic master when the problem is squarely within that industry.

---

## Available packs

| Pack | Skill name | When to use |
|---|---|---|
| [SaaS / B2B software](./saas/SKILL.md) | `sc-saas` | ARR / churn / pipeline / product-led-growth problems |
| [Retail / hospitality](./retail/SKILL.md) | `sc-retail` | Same-store-sales, foot traffic, basket size, store ops |
| [Healthcare / hospital ops](./healthcare/SKILL.md) | `sc-healthcare` | Readmissions, length-of-stay, access, outcomes |

---

## Installation

Same as the main skills folder — copy the relevant industry pack into your skills directory:

**macOS / Linux:**
```bash
cp -r industry-packs/saas ~/.claude/skills/sc-saas
```

**Windows (PowerShell):**
```powershell
Copy-Item -Path .\industry-packs\saas\ -Destination "$env:USERPROFILE\.claude\skills\sc-saas\" -Recurse
```

Then invoke `/sc-saas` (or `/sc-retail`, `/sc-healthcare`) and paste your problem.

You can install all three industry packs alongside the generic `strategy-consultant` master — they don't conflict.

Paste-ready prompts for non-Claude-Code users live in [`prompts/sc-saas.md`](../prompts/sc-saas.md), [`prompts/sc-retail.md`](../prompts/sc-retail.md), and [`prompts/sc-healthcare.md`](../prompts/sc-healthcare.md).

---

## When NOT to use an industry pack

- The problem crosses industries (SaaS company in healthcare → use generic master).
- The problem is framed at a level above industry-specific operations (corporate strategy, M&A, capital allocation).
- The user's vocabulary doesn't match the industry conventions (suggests they want neutral framing).

In those cases, use `strategy-consultant` (5-framework) or `strategy-consultant-7` (deeper).

---

## Roadmap — additional packs

PRs welcome. High-priority next packs:

- `sc-fintech` — payments, lending, fraud, regulatory
- `sc-manufacturing` — defect rates, OEE, supply chain
- `sc-nonprofit` — fundraising, donor retention, program effectiveness
- `sc-government` — backlog reduction, citizen satisfaction, procurement
- `sc-edtech` — completion, learning outcomes, monetization

See [CONTRIBUTING.md](../CONTRIBUTING.md) for the recipe.
