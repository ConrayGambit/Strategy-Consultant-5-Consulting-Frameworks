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
| [SaaS / B2B software](./saas/SKILL.md) | `vsc-saas` | ARR / churn / pipeline / product-led-growth problems |
| [Retail / hospitality](./retail/SKILL.md) | `vsc-retail` | Same-store-sales, foot traffic, basket size, store ops |
| [Healthcare / hospital ops](./healthcare/SKILL.md) | `vsc-healthcare` | Readmissions, length-of-stay, access, outcomes |

---

## Installation

Same as the main skills folder — copy the relevant industry pack into your skills directory:

**macOS / Linux:**
```bash
cp -r industry-packs/saas ~/.claude/skills/vsc-saas
```

**Windows (PowerShell):**
```powershell
Copy-Item -Path .\industry-packs\saas\ -Destination "$env:USERPROFILE\.claude\skills\vsc-saas\" -Recurse
```

Then invoke `/vsc-saas` (or `/vsc-retail`, `/vsc-healthcare`) and paste your problem.

You can install all three industry packs alongside the generic `visual-strategy-consultant` master — they don't conflict.

---

## When NOT to use an industry pack

- The problem crosses industries (SaaS company in healthcare → use generic master).
- The problem is framed at a level above industry-specific operations (corporate strategy, M&A, capital allocation).
- The user's vocabulary doesn't match the industry conventions (suggests they want neutral framing).

In those cases, use `visual-strategy-consultant` (5-framework) or `visual-strategy-consultant-7` (deeper).

---

## Roadmap — additional packs

PRs welcome. High-priority next packs:

- `vsc-fintech` — payments, lending, fraud, regulatory
- `vsc-manufacturing` — defect rates, OEE, supply chain
- `vsc-nonprofit` — fundraising, donor retention, program effectiveness
- `vsc-government` — backlog reduction, citizen satisfaction, procurement
- `vsc-edtech` — completion, learning outcomes, monetization

See [CONTRIBUTING.md](../CONTRIBUTING.md) for the recipe.
