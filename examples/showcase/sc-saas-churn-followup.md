# Dental SaaS churn + a follow-up turn — `sc-saas`

**Skill:** `sc-saas` — real output produced by a fresh agent reading the SKILL.md and applying it to the problem below (v1.3 consistency pass). No editing.

## Input (what the user typed)

> We're a $25M ARR vertical SaaS for dental practices. Gross logo churn went from 8% to 14% annualized over two quarters. NPS is flat at 41. We raised prices 12% at the start of the period and also migrated everyone to a new billing system. The CEO wants to roll back the price increase.

## Output (what the skill produced)

**Reframe:** "Churn spiked, so roll back the price increase" is likely the wrong framing — two interventions (12% price increase and a billing migration) landed in the same window, and a billing migration is a classic source of *involuntary* churn (failed payment methods, missed invoices, duplicate charges) that looks identical to price-driven churn in a top-line logo number. The reframed question is: "How much of the incremental 6 points of logo churn is voluntary price rejection vs. involuntary billing failure vs. a cohort we should never have acquired?" Proceeding with the reframed question; the analysis below still answers whether a rollback is warranted.

### 1. MECE Categorization

- **Monetization (price increase)**
  - Price-sensitivity by practice size (solo / 2–5 ops / DSO-affiliated)
  - Communication quality and lead time of the increase notice
  - Perceived value vs. the new price point (feature usage, ROI per chair)
  - Discount / grandfathering exceptions and who got them
- **Internal — billing migration**
  - Involuntary churn: failed cards, expired ACH mandates, dunning failures
  - Invoice errors: duplicate charges, wrong tier, tax changes, unexpected proration
  - Payment-method re-entry friction and portal confusion
  - CS/support ticket load during migration window
- **Retention — cohort composition**
  - Churn concentration by acquisition cohort, channel, and contract term
  - Month-to-month vs. annual mix (who could actually leave in-period)
  - Renewal timing overlap with the price change
- **Competitive**
  - Competitor promotions or switch-cost subsidies timed against the increase
  - Save-desk lost-to-competitor reasons vs. "no longer needed"
- **Product fit / Customer Success**
  - Feature adoption and usage trend in churned vs. retained practices
  - CSM coverage and health-score signals pre-churn
  - NPS flatness (41) as evidence that product sentiment did not move

---

### 2. Issue Tree

```text
Gross logo churn 8% → 14% annualized over 2 quarters ($25M ARR dental SaaS)
├── Monetization: 12% price increase
│   ├── Voluntary churn citing price
│   │   ├── Cancel-reason code = "price / too expensive" share
│   │   ├── Churn rate by practice size (solo vs. multi-op vs. DSO)
│   │   └── Churn among grandfathered / exempted accounts (control)
│   ├── Communication & timing
│   │   ├── Days of notice before renewal invoice
│   │   └── Cancel date relative to first increased invoice
│   └── Value perception
│       ├── Usage (claims filed, appts scheduled) in churned vs. retained
│       └── Save-desk acceptance of partial rollback offers
├── Internal: billing system migration
│   ├── Involuntary churn
│   │   ├── Payment-failure rate pre- vs. post-migration
│   │   ├── Dunning sequence completion rate
│   │   └── Churned accounts with zero cancel action (silent lapse)
│   ├── Invoice errors
│   │   ├── Duplicate / incorrect charge ticket count
│   │   └── Refund and credit-memo volume
│   └── Portal friction
│       ├── Payment-method re-entry completion rate
│       └── Billing-support ticket volume vs. baseline
├── Retention: cohort composition
│   ├── Churn by acquisition cohort and channel
│   ├── Month-to-month vs. annual contract mix
│   └── Renewal dates clustered in the period
├── Competitive
│   ├── Lost-to-competitor share in win/loss
│   └── Competitor pricing / promo activity in dental vertical
└── Product fit / CS
    ├── NPS flat at 41 (sentiment did not deteriorate)
    ├── Health-score trend 90 days pre-churn
    └── Feature-adoption gap in churned practices
```

---

### 3. Hypothesis-Driven Problem Solving

**Hypothesis:** The majority of the incremental ~6 points of logo churn is involuntary churn caused by the billing migration (failed payment methods and invoice errors), concentrated in small month-to-month practices, rather than voluntary rejection of the 12% price increase — so rolling back the price would sacrifice roughly $3M of ARR without fixing the churn.

| Variable | Expected (if hypothesis true) | Actual / Required Data |
|---|---|---|
| Payment-failure rate pre- vs. post-migration | Failed-payment rate at least doubles after cutover and stays elevated | Billing system: failed transactions / total invoices by month, old vs. new system |
| Share of churned logos with no cancel action | >50% of incremental churn is silent lapse (dunning exhausted, no cancel request) | Billing + CRM: churned accounts tagged by exit path (cancel request vs. dunning lapse) |
| Cancel-reason code distribution | "Price" cited by <30% of voluntary cancels; "billing problem / charged wrong" rises sharply | Support/CS cancel-reason codes, save-desk notes |
| Churn by contract type | Spike concentrated in month-to-month card-paying solo practices; annual-invoice accounts near baseline | CRM: churn rate by contract term and payment method |
| Churn timing vs. cutover date | Churn clusters in 30–60 days after migration cutover, not at each account's renewal/price-effective date | Billing: churn date minus cutover date vs. churn date minus first increased invoice |
| Grandfathered / price-exempt accounts (control) | Accounts that did NOT receive the increase churn at the same elevated rate — if their churn stayed at ~8%, the hypothesis is wrong and price is the driver | Billing: churn rate for exempted/grandfathered cohort vs. increased cohort |
| NPS and usage trend in churned accounts | NPS and usage flat right up to churn (consistent with 41 flat); no product-sentiment collapse | Product analytics + survey: 90-day pre-churn usage and NPS by churned cohort |

---

### 4. Pareto Focus (80/20)

> **The vital 20%:** (1) Involuntary churn from the billing migration — failed payments, dunning gaps, and invoice errors in month-to-month card-paying solo practices; (2) the grandfathered-vs-increased churn comparison, which is the single cleanest test of whether price is a driver at all.

**Actively deprioritized (the 80%):**
- Rolling back the 12% price increase before the attribution is done
- NPS survey redesign or a new "voice of customer" program (NPS is flat — it is not telling you anything new)
- Competitive repositioning or pricing-page rebrand
- Generic customer-success "health score" overhaul
- Product roadmap changes driven by churned-account feature requests
- Enterprise/DSO expansion motion (not where the churn is)

---

### 5. The "So What?" Test

**Process:** Decomposed the 8% → 14% logo-churn spike across monetization, billing migration, cohort composition, competitive, and product fit; built a testable split between voluntary price rejection and involuntary billing failure, using grandfathered accounts as the control and NPS flatness as corroborating evidence.

**Result:** Two confounded interventions landed in the same window. Flat NPS at 41 argues against a value or sentiment collapse, and a billing migration is the more common source of a sudden logo-churn step-up in SMB-heavy verticals. Until payment-failure, dunning, and exit-path data are split, the price increase cannot be blamed — and a rollback would cost on the order of $3M ARR (12% of $25M) with no guaranteed churn recovery.

**Insight:** Do not roll back the price increase this quarter. Instead: (1) VP Finance / Head of Billing pulls the pre-vs-post-migration payment-failure rate, dunning completion rate, and exit-path tag (cancel vs. silent lapse) for every churned logo in the two quarters — due in 10 business days; (2) VP Customer Success runs the grandfathered-vs-increased churn comparison and cancel-reason recode on the same list — same deadline; (3) RevOps launches an immediate win-back on silently lapsed accounts (card re-entry, fee waiver, 30-day reactivation) — starts this week, results tracked weekly. Decision gate: if grandfathered accounts churned at the same elevated rate, revisit pricing before the next board meeting; if not, the price increase stays and the fix is billing. Owner: CFO chairs; readout to CEO before end of fiscal quarter.

---

## Follow-up (what the user typed next)

> Go deeper on the hypothesis section — add the rows you'd need to separate the price increase from the billing migration.

## Follow-up output (what the skill produced)

### 3. Hypothesis-Driven Problem Solving

**Hypothesis:** The majority of the incremental ~6 points of logo churn is involuntary churn caused by the billing migration (failed payment methods and invoice errors), concentrated in small month-to-month practices, rather than voluntary rejection of the 12% price increase — so rolling back the price would sacrifice roughly $3M of ARR without fixing the churn.

| Variable | Expected (if hypothesis true) | Actual / Required Data |
|---|---|---|
| Payment-failure rate pre- vs. post-migration | Failed-payment rate at least doubles after cutover and stays elevated | Billing system: failed transactions / total invoices by month, old vs. new system |
| Share of churned logos with no cancel action | >50% of incremental churn is silent lapse (dunning exhausted, no cancel request) | Billing + CRM: churned accounts tagged by exit path (cancel request vs. dunning lapse) |
| Cancel-reason code distribution | "Price" cited by <30% of voluntary cancels; "billing problem / charged wrong" rises sharply | Support/CS cancel-reason codes, save-desk notes |
| Churn by contract type and payment method | Spike concentrated in month-to-month card-paying solo practices; annual-invoice accounts near baseline | CRM: churn rate by contract term and payment method |
| Churn timing vs. cutover date | Churn clusters in 30–60 days after migration cutover, not at each account's price-effective date | Billing: churn date minus cutover date vs. churn date minus first increased invoice |
| Grandfathered / price-exempt accounts (control) | Accounts that did NOT receive the increase churn at the same elevated rate — if their churn stayed at ~8%, price is the driver | Billing: churn rate for exempted/grandfathered cohort vs. increased cohort |
| Accounts migrated but not yet repriced (control) | If any cohort hit the new billing system before its price-effective date, its churn is already elevated — if it stayed at ~8%, the migration is exonerated | Billing: churn rate for accounts whose migration date preceded their first increased invoice by 30+ days |
| Accounts repriced before migration (control) | If any cohort received the increased invoice on the old billing system, its churn stayed near ~8% | Billing: churn rate for accounts whose first increased invoice predates their migration cutover |
| Churn date vs. first increased invoice date | Weak clustering — churn does not spike in the 30 days after the first increased invoice | Billing: distribution of (churn date minus first increased invoice date) |
| Involuntary churn by price-exposure status | Payment-failure and lapse rates identical for increased and grandfathered accounts — failure is a system effect, not a price effect | Billing: failed-payment rate split by price-exposed vs. exempt |
| Save-desk outcome by offered remedy | Accounts saved by fixing a billing problem (card re-entry, refund) outnumber those saved by a price concession 3:1 | CS save-desk log: remedy offered, remedy accepted, retained at 60 days |
| Billing-support ticket volume and mix | Billing tickets rise 2–3x post-cutover, dominated by "charged wrong / can't update card" rather than "why did my price go up" | Support system: ticket category volume by week relative to cutover |
| Downgrade rate (price-sensitivity leak) | Downgrade-to-lower-tier rate barely moves — a price-driven story would show downgrades rising alongside churn | Billing: tier-change events by month, pre vs. post increase |
| Churn among practices with highest usage | High-usage practices (most claims, most appointments) churn at the same elevated rate as low-usage ones — a price story would spare the high-ROI users | Product analytics joined to churn list: usage decile vs. churn rate |
| NPS and usage trend in churned accounts | NPS and usage flat right up to churn (consistent with 41 flat); no product-sentiment collapse | Product analytics + survey: 90-day pre-churn usage and NPS by churned cohort |

The three control rows that do the real separating work are the grandfathered cohort, the migrated-but-not-yet-repriced cohort, and the repriced-before-migration cohort. If the rollout of either change was staggered at all — by region, contract anniversary, or payment method — those natural experiments exist in the billing data and will settle the attribution faster than any survey. If both changes hit every account on the same day, fall back to the timing-clustering rows (churn relative to cutover vs. relative to first increased invoice) and the involuntary-by-price-exposure row.

## What to notice

- **The follow-up protocol held.** Asked to "go deeper on the hypothesis section," the skill reproduced *only* §3 in its visual format — it did not re-run the other four sections.
- **Defaults flexed on request.** The first-turn table has the usual 4–7 rows; the follow-up has 15 because the user explicitly asked for more rows to separate two confounded changes. That is the "flex with judgment" clause doing its job.
- **Three natural-experiment controls.** Grandfathered accounts, migrated-but-not-yet-repriced, and repriced-before-migration — the rows that actually separate price from billing.
- **Flat NPS was used, not ignored.** It appears as evidence against a product-sentiment story in both turns.
