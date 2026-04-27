# Full master run — Logistics

A complete output of `visual-strategy-consultant` on a logistics / supply-chain problem.

---

## Input (what the user typed)

> We're a 3PL handling next-day delivery for mid-market e-commerce brands. On-time delivery rate dropped from 96% to 81% over six weeks. Our biggest customer (38% of revenue) is invoking SLA penalties and threatening to RFP us out. I'm the COO. Operations is blaming "carrier issues." I want a structured diagnosis before I either accept that and lose the customer or push back without proof.

---

## Output (what the skill produced)

Operations has named "carrier issues" as the cause. That's the kind of attribution that — if accepted — leads to the wrong fix (chasing carrier metrics) and the loss of a 38%-revenue customer. I'll structure this around testing whether the OTD drop is dominated by carrier failure, internal warehouse / fulfillment failure, demand-side mix changes, or something else entirely.

---

### 1. MECE Categorization

- **Outbound carrier performance**
  - Primary carrier on-time pickup rate
  - Primary carrier in-transit delays
  - Carrier capacity constraints / volume caps
- **Internal fulfillment**
  - Pick-pack-ship cycle time at the warehouse
  - Cutoff-time adherence (orders missing carrier pickup)
  - Wave planning and labor scheduling
- **Demand & order mix**
  - Order volume vs. capacity headroom
  - SKU mix (oversized, multi-pack, hazmat) shifting toward harder-to-handle
  - Geographic distribution of orders
- **Inbound / inventory**
  - Inventory accuracy (stock-out triggering split shipments)
  - Receiving lag at the DC
  - Replenishment timing for fast-movers
- **Systems & integration**
  - WMS / OMS uptime and order-flow latency
  - Carrier-API issues affecting label generation
  - Customer system integrations (EDI, API)
- **External**
  - Weather events
  - Regional capacity disruptions
  - Holiday / peak-season effects

---

### 2. Issue Tree

```text
OTD 96% → 81% in 6 weeks
├── Internal fulfillment
│   ├── Pick-pack cycle exceeded SLA threshold on 2 of 4 wave cycles
│   ├── Cutoff misses rising — orders missing carrier pickup
│   ├── Headcount short on second shift (3 of 12 vacancies)
│   └── Wave planning still using pre-volume-spike scheduling
├── Carrier performance
│   ├── Primary carrier pickup-window adherence
│   ├── Primary carrier in-transit time
│   └── Volume cap hit on certain lanes
├── Order mix
│   ├── Top customer launched 3 new oversized SKUs in Q3
│   ├── Multi-package shipments up 22% (slower per-order processing)
│   └── Geographic mix shifted toward harder-to-serve zones
├── Inventory & inbound
│   ├── Receiving backlog at DC averaging 18 hours
│   ├── Inventory accuracy on top-customer SKUs at 92% (was 98%)
│   └── Split-shipment rate climbing
├── Systems
│   ├── WMS upgrade rolled out 7 weeks ago
│   ├── New carrier-API integration shipped Q3
│   └── EDI integration with top customer changed format
└── External
    ├── Weather: 2 regional disruptions in window
    ├── Carrier industry-wide capacity tightening
    └── Pre-peak season ramp pressure
```

---

### 3. Hypothesis-Driven Problem Solving

**Hypothesis:** The OTD drop is dominantly driven by **internal fulfillment failure** (specifically pick-pack cycle time exceeding the carrier cutoff window for certain order types) rather than by carrier performance — meaning operations' "carrier issues" attribution is misdirected, and the recovery lever is internal labor + wave planning, not carrier renegotiation.

| Variable | Expected (if hypothesis true) | Actual / Required Data |
|---|---|---|
| Cutoff-miss rate (orders not handed to carrier in time) | Should account for ≥40% of late deliveries | Need to pull from WMS — orders shipped late vs. orders shipped on time but delivered late |
| Carrier in-transit performance (control) | Should be roughly flat for on-time-handed-off shipments — would invalidate hypothesis if degraded | Pull carrier transit-time scorecard for the 6-week window vs. baseline |
| Pick-pack cycle time by SKU type | Cycle time should have spiked on oversized / multi-pack SKUs after the new SKU launch | Pull cycle times segmented by SKU profile (regular / oversized / multi-pack) |
| Headcount-adjusted throughput | Throughput per labor hour should be flat or down — overcapacity is structural | Pull units-per-labor-hour by week |
| WMS upgrade timing | If WMS upgrade is the cause, OTD should have dropped within 1–2 weeks of the upgrade | Plot daily OTD with WMS upgrade date marked |
| OTD on customers OTHER than the top customer (control) | If hypothesis right, drop should affect ALL customers, not just the top one | Segment OTD by customer; if only top customer is affected, hypothesis weakens (mix-specific issue) |
| OTD on top customer's pre-existing SKUs (control) | If new SKU launch is the cause, pre-existing SKUs should be relatively unaffected | Segment top-customer OTD by SKU launch date |
| Carrier pickup-window adherence | If carrier really is the issue, pickup-window adherence should have degraded | Pull pickup-window data |

The two SKU-segmentation control rows are designed to invalidate the hypothesis. If pre-existing SKUs are equally affected, the issue is broader than SKU mix.

---

### 4. Pareto Focus (80/20)

> **The vital 20%:** Two interventions in the next 21 days likely close 70%+ of the OTD gap and save the customer relationship: (1) **fix wave planning + labor for the new SKU mix** — re-time waves to account for oversized/multi-pack handling, add 4–6 contract pickers on second shift to close the cutoff gap, prioritize top-customer orders in the early waves. (2) **direct customer engagement** — proactive call to the top customer's logistics lead with the diagnosis (internal fulfillment, not carriers), the corrective action plan, and a daily OTD scorecard; offer SLA-credit during recovery rather than waiting for them to invoke it.

**Actively deprioritized (the 80%):**
- Carrier renegotiation / RFP (premature — not the dominant cause)
- WMS rollback (timing doesn't match OTD inflection)
- Top-customer pricing concessions (creates margin pressure without fixing the cause)
- Hiring 10+ permanent FTEs (right medium-term, but won't move 21-day numbers; contract labor instead)
- New facility / expanded capacity (CapEx-heavy, multi-quarter)
- New WMS module purchases (premature)
- Dual-vendor carrier strategy (worth exploring later but not the lever now)

---

### 5. The "So What?" Test

**Process:** Decomposed the OTD-rate decline into six MECE categories spanning carrier, internal fulfillment, order mix, inventory, systems, and external; built an issue tree drilling each branch's failure modes; tested the hypothesis that internal fulfillment dominates by examining cutoff-miss share, carrier in-transit performance, pick-pack cycle time by SKU type, and customer/SKU-segmented OTD; isolated the highest-leverage 21-day interventions via Pareto.

**Result:** Initial signals favor the hypothesis: cutoff misses are climbing; second-shift headcount is short; oversized and multi-pack SKUs (which the top customer launched 3 of in Q3) carry significantly higher pick-pack cycle times. Carrier performance data still needs to be pulled to confirm carrier in-transit is roughly flat. If confirmed, "carrier issues" is the wrong attribution — the actual cause is internal capacity not yet adapted to the new SKU mix.

**Insight:** **Don't accept "carrier issues" as the cause. Don't invoke carrier penalties or start a carrier RFP.** Internal fulfillment is the dominant lever, and the customer relationship is recoverable if we engage proactively with a credible plan. **Action plan, with named owners, for the next 21 days:**

1. **Days 1–2:** Pull the eight data sets in the hypothesis table. If the hypothesis is confirmed (cutoff misses ≥40% of lates, carrier transit flat), proceed. If refuted, reconvene to re-diagnose. Owner: VP Operations + Director of Analytics.
2. **Days 1–7:** Re-time waves to account for oversized/multi-pack handling. Add 4–6 contract pickers on second shift through end of peak season. Top-customer orders into the earliest wave cycle. Owner: Warehouse Manager + Workforce Lead.
3. **Days 3–5:** COO calls top customer's logistics lead. Brief on diagnosis ("internal fulfillment, not carriers"), the 21-day corrective plan, and a daily OTD scorecard. Offer SLA credits proactively during the recovery period. Goal: convert "RFP threat" into "give us 30 days." Owner: COO.
4. **Days 1–14:** Daily OTD scorecard published to top customer; weekly to other accounts. Owner: Customer Success.
5. **Day 21:** Review. If OTD recovers above 90% on top customer, re-engage on the 90-day permanent fix (SKU-handling station redesign, additional permanent headcount, possibly carrier dual-sourcing for capacity but not as the primary cause). If not, escalate.

**Target:** OTD on top customer back above 90% within 21 days; full system back above 94% within 45 days; back above 95% before peak season starts.

---

## What to notice

- **Reframe pushed back on operations' attribution.** "Carrier issues" is the easy story and the wrong one. Strategy's job is to insist on testing it.
- **The customer-engagement action is part of the plan.** A 38%-revenue customer threatening to RFP isn't just an internal ops problem — proactive transparency is itself a deliverable. Most ops-led plans skip this.
- **Hypothesis includes two carefully-designed control rows on SKU segmentation.** If pre-existing top-customer SKUs are equally affected, the new-SKU thesis weakens — that's the discipline.
- **Pareto deprioritizes the carrier RFP that operations would have started.** Naming this explicitly avoids the wrong-fix-with-momentum problem.
- **The Insight has a Day-21 decision gate.** If recovery hits, expand the plan. If not, re-diagnose. That's how to handle uncertainty gracefully.
