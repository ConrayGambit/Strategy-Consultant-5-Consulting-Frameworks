# Industry Packs

Variants of the master skill tailored to specific industries. Each pack adds:

- **Industry-aware MECE categories** — defaults that fit the industry (e.g., a SaaS pack defaults to ARR/NRR/churn dimensions; a retail pack defaults to comp store / traffic / ticket / mix).
- **Common root-cause patterns** — the diagnostic priors that experienced operators in that industry would carry into any problem.
- **Native metric vocabulary** — the right terms (NRR, AOV, OTD, NPS, ALOS, SSS) so the output reads like an industry insider's analysis.
- **A linked worked example** — each pack's `## Example` section points to a real run in [`examples/`](../examples/) that shows the shape the pack must produce.

These are **alternative masters**, not additional steps. Use the industry pack instead of the generic master when the problem is squarely within that industry.

---

## Available packs

| Pack | Skill name | When to use |
|---|---|---|
| [SaaS / B2B software](./saas/SKILL.md) | `sc-saas` | ARR / churn / pipeline / product-led-growth problems |
| [Retail / hospitality](./retail/SKILL.md) | `sc-retail` | Same-store-sales, foot traffic, basket size, store ops |
| [Healthcare / hospital ops](./healthcare/SKILL.md) | `sc-healthcare` | Readmissions, length-of-stay, access, outcomes |
| [Fintech / payments / lending](./fintech/SKILL.md) | `sc-fintech` | Approval/decline, fraud, delinquency, KYC, unit economics |
| [Manufacturing / industrial ops](./manufacturing/SKILL.md) | `sc-manufacturing` | OEE, defect rate, yield, changeover, throughput |
| [Nonprofit / fundraising](./nonprofit/SKILL.md) | `sc-nonprofit` | Donor retention, gift mix, program effectiveness |
| [Public sector / civic ops](./government/SKILL.md) | `sc-government` | Backlogs, cycle time, CSAT, procurement |
| [Edtech / online learning](./edtech/SKILL.md) | `sc-edtech` | Activation, completion, outcomes, monetization |

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

Then invoke `/sc-saas` (or `/sc-retail`, `/sc-healthcare`, `/sc-fintech`, `/sc-manufacturing`, `/sc-nonprofit`, `/sc-government`, `/sc-edtech`) and paste your problem.

To install every pack at once:

**macOS / Linux:**
```bash
for p in industry-packs/*/; do cp -r "$p" ~/.claude/skills/sc-$(basename "$p"); done
```

**Windows (PowerShell):**
```powershell
Get-ChildItem .\industry-packs -Directory | ForEach-Object { Copy-Item -Path $_.FullName -Destination "$env:USERPROFILE\.claude\skills\sc-$($_.Name)" -Recurse -Force }
```

You can install all eight industry packs alongside the generic `strategy-consultant` master — they don't conflict.

Paste-ready prompts for non-Claude-Code users live in `prompts/sc-<industry>.md` — one per pack: [`sc-saas`](../prompts/sc-saas.md), [`sc-retail`](../prompts/sc-retail.md), [`sc-healthcare`](../prompts/sc-healthcare.md), [`sc-fintech`](../prompts/sc-fintech.md), [`sc-manufacturing`](../prompts/sc-manufacturing.md), [`sc-nonprofit`](../prompts/sc-nonprofit.md), [`sc-government`](../prompts/sc-government.md), [`sc-edtech`](../prompts/sc-edtech.md).

---

## When NOT to use an industry pack

- The problem crosses industries (SaaS company in healthcare → use generic master).
- The problem is framed at a level above industry-specific operations (corporate strategy, M&A, capital allocation).
- The user's vocabulary doesn't match the industry conventions (suggests they want neutral framing).

In those cases, use `strategy-consultant` (5-framework) or `strategy-consultant-7` (deeper).

---

## Additional packs

All five originally-planned packs (fintech, manufacturing, nonprofit, government, edtech) shipped in v1.2. PRs welcome for further packs — e.g., insurance, real-estate, energy, telecom, hospitality, marketplaces. See [CONTRIBUTING.md](../CONTRIBUTING.md) for the recipe.
