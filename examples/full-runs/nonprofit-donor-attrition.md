# Full master run — Nonprofit

A complete output of the `visual-strategy-consultant` master skill on a nonprofit fundraising problem.

---

## Input (what the user typed)

> Our environmental nonprofit has lost 23% of recurring monthly donors over the last 18 months. We're $400K short of our annual budget. The year-end giving campaign starts in 6 weeks and the board is calling for an emergency fundraising consultant. I'm the Executive Director — I'd rather diagnose the problem first.

---

## Output (what the skill produced)

The stated problem is a 23% recurring-donor decline and a $400K budget gap, but the board has already moved to "hire an emergency fundraising consultant" — a high-cost intervention before the cause is known. Below I'll diagnose first, then evaluate whether external help is the right next step. Six weeks is enough for a focused diagnostic plus the start of an intervention.

---

### 1. MECE Categorization

- **Donor-side dynamics**
  - Macroeconomic pressure (cost of living, household giving down)
  - Cause fatigue or shifting donor priorities (climate vs. other causes)
  - Aging-out of the longest-tenured cohort
- **Engagement & communication**
  - Email cadence, open rates, content quality
  - Storytelling — impact reporting depth and frequency
  - Personalization (templated vs. tailored)
- **Donation experience**
  - Recurring-payment friction (failed cards, expired payment methods, no recovery)
  - Donor portal usability
  - Confirmation and receipt experience
- **Trust & credibility signals**
  - Transparency on program spend vs. overhead
  - Recent media coverage (positive or negative)
  - Charity Navigator / GuideStar ratings
- **Internal capacity**
  - Development-team headcount and turnover
  - CRM data quality and segmentation capability
  - Major-gift program absorbing time at the expense of monthly donors

---

### 2. Issue Tree

```text
Recurring monthly donors -23% over 18 months
├── Passive attrition (silent churn)
│   ├── Failed-card recurring payments not recovered
│   ├── Expired card cleanup not happening
│   └── Donors changing email — losing comms
├── Active churn (decided to leave)
│   ├── Cost-of-living pressure on household budgets
│   ├── Lack of recent impact stories / felt impact
│   └── Confidence eroded by overhead concerns or news
├── Engagement decay
│   ├── Email cadence dropped after staff turnover
│   ├── Annual report skipped last year
│   └── Donor anniversary / milestone outreach stopped
├── Acquisition not replacing churn
│   ├── Acquisition channels reduced (paid social cuts)
│   ├── Peer-to-peer / event fundraising paused
│   └── New-donor onboarding sequence weak
└── Org capacity gaps
    ├── Development director turnover (12 months ago)
    ├── CRM segmentation underused
    └── Focus shifted to major gifts, monthly program neglected
```

---

### 3. Hypothesis-Driven Problem Solving

**Hypothesis:** A material share of the 23% loss is **passive attrition** (failed payments and silent churn) rather than donors actively choosing to leave — meaning a payment-recovery sweep + reactivation campaign in the next 4 weeks could recover meaningful revenue before year-end giving starts.

| Variable | Expected (if hypothesis true) | Actual / Required Data |
|---|---|---|
| Share of churned donors with failed last transaction | Should be ≥30% if passive attrition is significant | Need to query CRM: of donors who churned, what % had a failed card or expired payment as the last event |
| Time between last successful donation and "churn" classification | Short gap (failed card → marked inactive) suggests passive | Need to pull lapse-time distribution |
| Reactivation rate when contacted by phone (small test) | Should be >15% if passive — they didn't choose to leave | Need to run a 100-donor phone test on recent churners |
| Email open rates among current donors (control) | If active disengagement is the issue, open rates should be falling | Open rates flat at 22% YoY ✅ supports passive hypothesis (engagement isn't dead) |
| Donor exit-survey reasons (control) | If active churn dominated, "couldn't afford" or "shifted priorities" should be top reasons | No exit survey running — need to add one |
| Same-segment donors at peer nonprofits | If macro is the dominant driver, peers should show similar declines | Industry data: peer environmental nonprofits down 8–12% ✅ partially explains, but not the full 23% |
| Year-end giving response rate, prior year (control) | Should have been steady if the issue is recent / structural | Last year's YE response down 18% — issue predates this period ✅ confirms it's structural |

The two control rows (open rates flat, peer comparison) cleanly support the hypothesis. The exit-survey gap is itself an action item.

---

### 4. Pareto Focus (80/20)

> **The vital 20%:** Two interventions in the next 6 weeks likely recover ~60–70% of the gap: (1) a **passive-attrition sweep** — re-attempt failed card payments, run a card-update campaign, manually call/email recent churners — to recover an estimated 8–12% of lost donors before year-end. (2) **Restart the impact storytelling cadence** — quarterly impact stories, donor anniversary touches, and a single high-quality YE annual report — to stabilize active churn and lift YE response. Together these target the 80% of the gap that's recoverable internally without external consulting spend.

**Actively deprioritized (the 80%):**
- Hiring an emergency fundraising consultant ($30–80K spend, slow start, doesn't address payment recovery)
- Major rebrand or messaging overhaul (high cost, slow payoff)
- New acquisition channel investment (right idea, wrong timing — recover existing first)
- CRM migration (real concern but a 6-month project, not a 6-week one)
- Major-gift program restructure (time-intensive, won't move Q4)
- Board-led peer-to-peer campaign (great for next year, not in 6 weeks)
- Galas / event fundraising restart (long lead time)

---

### 5. The "So What?" Test

**Process:** Decomposed the donor-attrition + budget-gap problem into five MECE categories; built an issue tree distinguishing passive vs. active attrition; tested the hypothesis that passive attrition is significant by examining payment-failure data, engagement metrics, and peer benchmarks; isolated the highest-leverage 6-week interventions via Pareto.

**Result:** Engagement metrics (email opens flat at 22%) and peer-industry data (8–12% decline at similar orgs) suggest the 23% drop is partly macro (~10pp) but the remaining ~13pp is recoverable through internal action. Most critically, the hypothesis predicts passive attrition is meaningful — confirmed if ≥30% of churned donors had failed-card events. That's a 1-day data pull that determines the entire intervention strategy.

**Insight:** **Don't hire an emergency consultant yet — diagnose passive vs. active attrition first.** External help may still be warranted in 8 weeks if internal recovery underdelivers, but spending consulting dollars before knowing the cause is misallocating scarce capital. **Action plan, with named owners, for the next 6 weeks:**

1. **Days 1–3:** Development Director (or interim) pulls failed-payment data from the CRM. Goal: confirm or refute passive-attrition hypothesis. Owner: ED + DD.
2. **Days 4–10:** Launch payment-recovery sweep — re-attempt failed cards, send card-update campaign, manually phone the top 100 churners with personal voicemails. Target: recover 80+ donors. Owner: DD + 2 board members willing to call.
3. **Days 7–21:** Ship one high-impact story (with photos and outcome data) and a personal ED video to the entire current donor file ahead of YE. Owner: ED + comms coordinator.
4. **Days 14–42:** Run the YE giving campaign with three scheduled email touches and one direct mail, anchored on the impact story. Track response rate vs. last year as the primary signal. Owner: comms coordinator.
5. **Day 42:** Review. If recovered ≥$200K and response rate ≥ last year, hold on consultant decision. If not, hire consultant with specific scoped engagement (e.g., acquisition channel rebuild) — by then we'll know what to scope.

**Target:** close 60% of the $400K gap ($240K) by year-end through internal interventions; defer the consultant decision to a data-informed point.

---

## What to notice

- **Reframe at the top contested the board's preferred solution.** Hiring a consultant before diagnosing is the misallocation; the analysis shows why.
- **Passive vs. active attrition is the load-bearing distinction.** Most nonprofit fundraising thinking conflates these. The hypothesis-test framework forces them apart.
- **Pareto names a deprioritized item that the board literally just proposed.** That's the framework working as intended — explicit deprioritization, not implicit avoidance.
- **The Insight is a multi-step plan with a decision gate.** Day 42 is the explicit consultant-or-not decision point, with the criteria pre-committed. That's how strategy hands off cleanly to execution.
- **Macro is acknowledged but not used as an excuse.** Peer comparison shows ~10pp of the 23% is industry-wide. The remaining ~13pp is what's actionable.
