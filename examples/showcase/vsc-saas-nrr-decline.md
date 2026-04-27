# Showcase — `vsc-saas` (industry pack)

**Eval result:** 6/6 PASS — produced after the industry-pack SKILL.md was patched to inline the visual contract. Compare to `vsc-cloud-cost.md` (the generic master) — same visual format, but native SaaS vocabulary (NRR, GRR, CSM, ACV, PQL).

---

## Input

> Our PLG-led $40M ARR data-tooling SaaS has seen NRR drop from 124% to 108% over four quarters. GRR is roughly stable at 91% — so the problem is in expansion, not in logo retention. Activation rate (time-to-first-value) has held steady. Multi-product attach has plateaued. CEO wants to know whether to (a) hire a Customer Success VP, (b) launch a fourth product, or (c) reorganize the expansion motion. I'm the Chief Revenue Officer.

## Output (verbatim)

### 1. MECE Categorization

- **Retention (logo churn)**
  - Customer segmentation churn profile (GTM segment, ACV, geography, cohort)
  - Product capability gaps vs. competitive set
  - Support/onboarding quality by cohort
- **Expansion Motion Failure**
  - CSM capacity and tier routing
  - Expansion playbook decay
  - Product adoption blockers
- **Acquisition Quality Shift**
  - Inbound segment mix change
  - Sales-assisted cohort performance degradation
  - Feature-market fit erosion in high-value segments
- **Monetization Execution**
  - Pricing/packaging alignment to expansion motion
  - Discount/contraction discipline breakdown
  - Packaging mismatch vs. multi-product attach thesis
- **Go-to-Market Alignment**
  - Sales / CSM / Product communication on expansion priorities
  - GTM motion assignment

---

### 2. Issue Tree

```text
NRR Decline 124% → 108%
├── GRR Stable @ 91%
│   └── Logo retention NOT the issue
├── Expansion Rate Decline
│   ├── CSM Motion Failure
│   │   ├── CSM headcount ratio vs. ARR growth
│   │   ├── CSM tier routing
│   │   └── Expansion playbook execution
│   ├── Product Expansion Blockers
│   │   ├── Seat-growth friction
│   │   └── Multi-product attach stalled
│   └── Acquisition Cohort Quality Shift
│       ├── PLG cohort expansion DNA weaker
│       └── Sales-assisted segment shift
├── Activation Held Steady
│   └── Not a problem
└── Product Attach Plateau
    ├── Expansion pricing/bundling misaligned
    └── Cross-sell motion deprioritized
```

---

### 3. Hypothesis-Driven Problem Solving

**Hypothesis:** The CSM motion was not re-resourced to support the expansion motion at scale, and accounts are stratifying into touch-starved cohorts; meanwhile, the product attachment plateau signals missing integrations or feature gaps in the upsell narrative.

| Variable | Expected (if hypothesis true) | Actual / Required Data |
|---|---|---|
| CSM:ACV ratio trend | Ratio deteriorated; CSMs added <10% YoY, ACV per CSM stable/growing | Pull headcount growth vs. ACV per CSM, touch frequency by account-size cohort |
| Upsell win rate by motion | Strategic accounts (QBR-based) show 35%+ attach; touch-starved show <15% | Measure: % of target accounts contacted with upsell motion vs. $ expansion won |
| Feature-completeness vs. competition | Top downgraded accounts cite specific feature; multi-product buyers <40% adoption in adjacent modules | Win/loss: feature-gap reasons; product adoption rates |
| Expansion DNA of acquisition cohorts | Recent 8 quarters of cohorts show declining expansion rates | Cohort analysis: NRR by quarter-of-acquisition, segmented Sales vs. PLG |
| Net logo retention stable (control) | GRR at 91% confirms churn not accelerating — would invalidate hypothesis if churn were rising | Monthly/quarterly churn rate trend confirms flat |

---

### 4. Pareto Focus (80/20)

> **The vital 20%:** CSM re-resourcing and tier-routing to expansion-ready cohorts (mid-market/enterprise accounts with consumption upside), paired with ruthless diagnosis of the multi-product attachment gap (feature blocker? pricing? GTM message?).

**Actively deprioritized (the 80%):**
- General "customer success transformation" initiatives (frameworks, NPS surveys)
- Rebranding or product-positioning changes
- Sales hiring or sales-motion overhaul (sales is not the constraint; expansion is)
- Launching a fourth product (don't expand portfolio without diagnosing why attach is flat)
- Organizational restructuring for its own sake

---

### 5. The "So What?" Test

**Process:** Analyzed NRR decline (124% → 108%) against GRR floor (91%); identified that logo retention is stable and the problem is purely expansion motion. Built issue tree mapping CSM under-resourcing, expansion playbook decay, and acquisition-cohort quality to net dollar retention, then prioritized the CSM motion as the vital 20%.

**Result:** CSM capacity is the binding constraint. Expansion accounts are not being touched with discipline, and product attach has stalled because the expansion narrative is unclear or not resourced. The three-product portfolio exists but is not moving as upsell.

**Insight:** Do NOT hire a Customer Success VP on top of an under-resourced CSM book — you'll compound the problem. Instead, (1) conduct a CSM-motion audit by account-size segment within 2 weeks; (2) identify the top 15–20 accounts with highest expansion DNA and run a 4-week concentrated CSM outreach with a defined upsell play, measuring attach and NRR lift; (3) diagnose the multi-product attachment stall in parallel in a 2-week product review. Owner: CRO chairs weekly. Target: 8 weeks to know whether CSM motion or product motion is the constraint. The fourth-product launch is a NO for now.

---

## What to notice

- **Native SaaS vocabulary throughout.** NRR, GRR, ACV, PQL, CSM, "expansion motion," "PLG cohort." A SaaS operator would recognize this analysis as written by a peer, not a generalist.
- **Reframes the binary.** The user offered three options (CS VP / 4th product / reorg). The skill said "the question is wrong — the binding constraint is CSM capacity and product-attach diagnosis, not org or product expansion."
- **CONTRAST with the bug version.** Before the SKILL.md was patched (see test history), the model produced a 6-column hypothesis table, no Pareto blockquote, and rolled So What? into prose. The fix forced the canonical visual contract while preserving the SaaS-specific defaults.
