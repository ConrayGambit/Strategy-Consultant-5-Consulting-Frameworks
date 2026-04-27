# Showcase — `visual-strategy-consultant` (5-framework master)

**Eval result:** 6/6 PASS — structurally compliant with the full visual contract.

---

## Input

> Our cloud infrastructure costs at our 200-person SaaS company have ballooned from $180K/month to $340K/month over the past 9 months. Revenue grew only 22% in that time. CFO is asking whether to renegotiate with our cloud vendor or kick off a major refactoring project. I'm the VP of Engineering and I have to present a recommendation to the exec team in 3 weeks.

## Output (verbatim from the skill)

### 1. MECE Categorization

- **Cost Growth Drivers (Supply Side)**
  - Infrastructure scaling (compute, storage, networking capacity increases)
  - Unit cost inflation (vendor price increases, unfavorable contract terms)
  - Architectural waste (inefficient code, poor resource utilization, orphaned services)
  - Operational overhead (redundancy, failed experiments, staging/dev environments)

- **Revenue Growth Constraints (Demand Side)**
  - Customer acquisition limits (CAC, market saturation, sales team capacity)
  - Customer retention gaps (churn, expansion economics)
  - Pricing strategy (ARPU growth lagging infrastructure complexity)

- **Process & Governance Gaps**
  - Cost visibility (no per-service accounting, opaque spend ownership)
  - Approval workflows (deployment friction, lack of cost checkpoints)
  - Team incentives (engineering rewarded for features, not efficiency)

---

### 2. Issue Tree

```text
Cloud Cost Blowout (89% increase / 9 months)
├── Structural Cost Growth
│   ├── Infrastructure Scaling (capacity)
│   │   ├── Customer growth (legitimate)
│   │   ├── Over-provisioning (buffer / edge cases)
│   │   └── Unused capacity (failed experiments, deprecated features)
│   ├── Unit Cost Changes
│   │   ├── Vendor price increases (annual renegotiation cycles)
│   │   └── Unfavorable contract terms (no volume discount, wrong tier)
│   └── Architectural Inefficiency
│       ├── Resource waste (unoptimized queries, compute loops, N+1)
│       ├── Duplicate services (technical debt, migration gaps)
│       └── Runaway processes (memory leaks, runaway jobs)
└── Revenue Alignment Problem
    ├── Revenue grew only 22% (far below cost growth)
    ├── Gross margins under pressure (unit economics degrading)
    └── Growth-to-cost ratio suggests wrong customer mix or pricing
```

---

### 3. Hypothesis-Driven Problem Solving

**Hypothesis:** The cost explosion is primarily driven by architectural waste and over-provisioning, not legitimate customer growth — and refactoring will yield 30–40% cost reduction without revenue impact.

| Variable | Expected (if hypothesis true) | Actual / Required Data |
|---|---|---|
| Cost per customer (normalized) | Declined or flat YoY | Increasing → suggests bloat, not scale |
| Utilization rate by service | <50% peak, <25% average for many services | Audit cloud dashboards for idle/low-use services |
| Infrastructure headcount ratio | Cost growth outpacing eng team size | Cost/eng headcount trending up? |
| Top 5 services by cost | 60%+ of total spend | Pareto audit: do top services have clear ROI? |
| Vendor contract terms | At-capacity tiers, or auto-scaling overages | Review invoices for overage charges, tier mismatches |
| Customer-to-infrastructure ratio | More customers per unit cost | If ratio declined, waste is probable cause |

---

### 4. Pareto Focus (80/20)

> **The vital 20%:** (1) Immediate cost visibility: instrument billing by service/customer/team to expose the 3–5 cost drivers accounting for 70% of spend. (2) Contract renegotiation: exploit vendor lock-in leverage now (threat of migration) to unlock volume discounts or move to consumption-based tiers. (3) Quick architectural wins: retire 2–3 low-traffic services or consolidate databases (low effort, immediate 10–15% relief).

**Actively deprioritized (the 80%):**
- Greenfield architectural redesign (high effort, delayed payoff, may not address immediate cost drivers)
- Migration to multiple cloud vendors (complexity, re-engineering overhead)
- Micro-optimization of individual services (low-leverage; fix the structure first)
- Headcount reduction or process redesign (orthogonal; address cost visibility first)

---

### 5. The "So What?" Test

**Process:** Categorized cost drivers (MECE), decomposed root causes (issue tree), tested hypothesis that waste (not legitimate growth) drives most of the cost explosion, applied 80/20 to isolate high-impact levers.

**Result:** The analysis exposes three parallel but independent pressure points: (1) structural waste in infrastructure (over-provisioning, unused services), (2) unfavorable contract terms, and (3) weak revenue-to-cost growth correlation. A refactoring project alone will fail if the contract is extracting 15–20% in overages; renegotiation alone will fail if 40% of infrastructure is unused. Both must move in parallel.

**Insight:** Before greenfield refactoring, spend 4 weeks on cost forensics and contract re-negotiation. Assign VP Finance to lead vendor discussions (exploit threat of migration); assign a senior engineer to audit top-10 services for utilization and quick retirement wins. Target 15–20% cost reduction from renegotiation + quick wins; use that momentum to business-case a focused 6-month refactor on the remaining 40% of waste. Present exec team with a phased approach: immediate relief (negotiation + quick hits) + strategic fix (refactor). This prevents the false choice between "renegotiate OR refactor" and positions you to do both.

---

## What to notice

- **Reframes the binary.** The user's CFO asked "renegotiate OR refactor." The skill answered "both — sequentially, with cost visibility first." That's the consultant move: refusing a false binary.
- **Pareto is genuinely ruthless.** Greenfield redesign and multi-cloud migration are tempting prestige projects; they're explicitly named as deprioritized.
- **Hypothesis table includes a falsifiable framing.** "Cost per customer" rising is the smoking gun — it would be FALLING if growth were legitimate.
- **Insight is staged and assignable.** Two named owners (VP Finance, senior engineer), two parallel tracks, with a target metric (15–20% reduction in 4 weeks) and a phased follow-on.
