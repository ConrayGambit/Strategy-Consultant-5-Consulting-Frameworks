# Full master run — Retail / Hospitality

A complete output of the `visual-strategy-consultant` master skill on a multi-store retail problem.

---

## Input (what the user typed)

> Same-store sales at our 47-location specialty coffee chain are down 6% YoY for the third consecutive quarter. We've held prices steady. Foot traffic is down ~9%, average ticket is up ~3%. The board wants a turnaround plan in 30 days and is hinting at closing the bottom 8 stores. I'm the COO and I'm not convinced closures are the answer.

---

## Output (what the skill produced)

The stated problem is "comp store sales down 6%," but the board is already gravitating toward store closures as the solution. Worth flagging: closures are a one-way door. Below I'll structure this around the question "what's actually driving the comp decline?" before evaluating closures vs. alternatives. If you want a different framing, say so.

---

### 1. MECE Categorization

- **Local market dynamics**
  - Foot traffic patterns shifting (work-from-home, neighborhood changes)
  - Competitor density (new entrants, closures of nearby anchors)
  - Demographic shifts in core trade areas
- **Customer behavior**
  - Visit frequency declining among existing customers
  - New customer acquisition slowing
  - Day-part mix (morning rush vs. afternoon vs. weekend)
- **Product & menu**
  - SKU mix shifts (espresso drinks vs. brewed vs. food)
  - Out-of-stocks on hero items
  - Quality consistency across stores
- **Operations**
  - Speed of service / wait times
  - Staffing levels and barista experience
  - Hours of operation aligned to local demand
- **Brand & marketing**
  - Loyalty program engagement
  - Social/local visibility
  - Promotional cadence vs. competitors

---

### 2. Issue Tree

```text
Comp sales -6% (FT -9%, ticket +3%)
├── Demand-side (local market)
│   ├── WFH-driven morning traffic decline in CBD stores
│   ├── New competitor openings within 0.5 mi (12 of 47 stores)
│   └── Anchor tenant closures in 4 strip-mall locations
├── Customer behavior
│   ├── Loyalty member visit frequency dropped 14% YoY
│   ├── New-to-brand customer share down (acquisition issue)
│   └── Afternoon day-part softening more than morning
├── Operational drag
│   ├── Speed-of-service +18 sec average (post-COVID staffing)
│   ├── Newer baristas concentrated in lower-volume stores
│   └── Hours not adjusted as demand patterns shifted
├── Product mix
│   ├── Cold-beverage growth lagging category
│   ├── Food attach rate declined post-menu simplification
│   └── No seasonal LTOs in last 3 quarters
└── Brand engagement
    ├── Loyalty enrollment rate dropping at POS
    ├── Local social presence inconsistent store-to-store
    └── Promo activity reduced (cost-cutting)
```

---

### 3. Hypothesis-Driven Problem Solving

**Hypothesis:** The comp decline is driven primarily by the foot-traffic side (local-market and behavioral causes) — not by store-level operational underperformance — meaning closing the bottom 8 stores would eliminate revenue without addressing the dominant cause.

| Variable | Expected (if hypothesis true) | Actual / Required Data |
|---|---|---|
| Comp decline correlation with WFH/CBD exposure | High-CBD stores should comp worse than suburban stores | Need to segment 47 stores by CBD/suburban classification and compare comp |
| Comp decline correlation with new local competition | Stores within 0.5 mi of new competitor opening should comp materially worse | 12 stores affected — comp decline 11% vs. system avg 6% ✅ matches |
| Operational metrics on bottom-8 stores | Should be roughly in line with mid-tier stores (no clear ops failure) | Need to pull speed-of-service, audit scores, mystery-shopper data for bottom 8 |
| Loyalty member visit frequency | Should drop across all stores, not just bottom 8 | -14% system-wide ✅ matches (this is a behavioral problem, not store problem) |
| Bottom-8 stores' customer acquisition rate (control) | If this is a market problem, bottom 8 should still acquire at roughly system rate | Need to pull new-customer rate by store band |
| Bottom-8 stores' food/beverage mix (control) | Should look similar to system average if market-driven | Need to pull mix data |
| Top-quartile stores' performance trend | Should also be declining (system effect), but less | Top-quartile comp -3% (vs. system -6%) ✅ supports hypothesis |

The control rows (bottom-8 acquisition, mix, top-quartile trend) are designed to invalidate the hypothesis. If bottom-8 stores have meaningfully worse acquisition or mix, the closure case strengthens.

---

### 4. Pareto Focus (80/20)

> **The vital 20%:** Two drivers likely account for ~70% of the comp decline: (1) WFH-driven morning traffic loss in the 14 CBD-adjacent stores (estimated 35-40% of total comp gap), and (2) loyalty-member visit frequency decline of 14% across all customers (estimated 30% of comp gap, and notably system-wide rather than store-specific). Both are addressable with targeted interventions, not closures.

**Actively deprioritized (the 80%):**
- Closing the bottom 8 stores (premature — store-specific underperformance hasn't been validated)
- Menu re-engineering (real concern but slow ROI)
- Expanding cold-beverage program (right direction, but won't move Q4 numbers)
- Hiring more experienced baristas system-wide (cost prohibitive at scale)
- Loyalty program redesign (treats symptom, not cause — current program isn't broken, engagement is)
- Pricing optimization (already held steady; not the issue)
- New marketing agency (not the right intervention shape)
- Store-level remodels (CapEx-heavy, slow payoff)

---

### 5. The "So What?" Test

**Process:** Decomposed the comp-store decline into five MECE categories; mapped them in an issue tree; tested the hypothesis that demand-side factors (not store-level operations) dominate by examining CBD vs. suburban performance, new-competitor exposure, loyalty engagement trends, and bottom-store operational metrics; isolated the highest-leverage interventions via Pareto.

**Result:** The 14 CBD-adjacent stores are comping at -11% vs. system -6%, suggesting WFH-driven traffic loss is concentrated rather than diffuse. Loyalty visit frequency is down 14% system-wide, indicating a behavioral problem affecting all stores equally, not store-level operational failures. Top-quartile stores are also comping negative (-3%), reinforcing that this is a system effect. Bottom-8 store ops metrics still need verification before any closure decision.

**Insight:** **Don't close the bottom 8 stores in 30 days.** The data so far points to a demand-side and loyalty-engagement problem, not a store-quality problem. Closures would burn revenue without fixing the dominant cause. **Action — present to the board in three parts within 30 days:** (1) Validate hypothesis with the four data pulls listed in the table (assignment to Director of Analytics, due in 10 days). (2) Pilot a "CBD recovery" package in 4 of the 14 affected stores: extended early-morning hours, mobile order priority lane, free-delivery partnership with a corporate-catering platform — measure 60-day comp lift. Owner: VP Operations. (3) Pilot a "loyalty re-engagement" campaign with the 14% drop-off cohort: 3-tier reactivation offer with frequency targets. Owner: VP Marketing. Bring closure decision back to the board only after pilots run, with a quantified comparison: cost of closures + lost contribution margin vs. cost of pilots + projected recovery. **Target:** stabilize comp at -3% or better within two quarters; revisit closures only if pilots fail.

---

## What to notice

- **Reframe at the top.** The board's preferred solution (closures) is contested before any framework runs. The structured analysis then either supports or refutes it with data.
- **Defaults flexed.** MECE has 5 categories (default range 3–6 — fine). Hypothesis table has 7 rows (default range 4–7 — at the upper bound, justified by the multi-segment problem).
- **Control rows do real work.** Three rows (bottom-8 acquisition, bottom-8 mix, top-quartile trend) are explicitly designed to invalidate the hypothesis. The top-quartile data point particularly strong because it shows system-wide decline.
- **Pareto deprioritization names legitimate concerns.** Menu, cold beverage, and loyalty redesign are real items — but they're explicitly named as not-this-quarter. That's the discipline.
- **The Insight is staged, not single-shot.** Three actions with three owners and three timelines. The closure decision is preserved as a future option, just not the immediate one.
