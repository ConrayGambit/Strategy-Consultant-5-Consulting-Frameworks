# Example: End-to-End Visual Strategy Consultant Output

This is what the master skill produces in a single response when given a real business problem. Use this to (a) verify your installation works and (b) see the output contract in action.

---

## The problem (user input)

> Our enterprise B2B SaaS sales cycle has stretched from 60 days to 110 days over the past six months. New ARR is on track to miss our annual target by ~15%. Leadership wants to know what's happening and what to do — they're considering reorganizing the sales team. I'm the VP of Revenue and I have a board meeting in two weeks.

---

## The response (Visual Strategy Consultant master skill)

You said the problem is the sales cycle stretching from 60 → 110 days, but leadership is considering a reorg of the sales team. Worth flagging: a reorg is expensive insurance against the wrong hypothesis. Before recommending it, this analysis tests whether the cycle stretch is actually a sales-execution problem or a buying-side / product-side problem. I'll proceed with that framing — let me know if you want to reframe.

---

### 1. MECE Categorization

- **Buyer-side dynamics**
  - Procurement processes lengthening industry-wide (macro)
  - Higher number of stakeholders required to approve deals
  - Increased competitive RFPs at evaluation stage
- **Deal characteristics**
  - Average deal size shifting (larger deals = longer cycles)
  - More multi-product / multi-year structures
  - Net-new logo vs. expansion mix shift
- **Sales execution**
  - AE ramp times for newer hires
  - Discounting/pricing approval bottlenecks
  - Late-stage handoffs to legal, security, finance
- **Product fit & differentiation**
  - Feature gaps surfaced during evals
  - Loss of differentiation vs. one or more competitors
  - Reference-customer friction during proof points
- **Pipeline quality**
  - MQL / SQL definitions or sources shifting
  - Deals entering pipeline less qualified than before
  - Stage-gating discipline at handoff

---

### 2. Issue Tree

```text
Sales cycle 60d → 110d
├── Buyer side
│   ├── Procurement scrutiny up post-macro shift
│   ├── More stakeholders per deal (security, legal, finance)
│   └── Multi-vendor RFPs more common
├── Deal mix
│   ├── ACV trending up — bigger deals = longer cycles
│   ├── More multi-year contracts
│   └── Logo vs. expansion ratio shifted
├── Sales execution
│   ├── 6 of 14 AEs hired in last 9 months (ramp drag)
│   ├── Discount-approval cycle lengthened post-CFO change
│   ├── Security review averaging 22 days
│   └── Legal review 18-day average for redlines
├── Product / competitive
│   ├── Two competitors shipped key integrations in Q2
│   ├── References pool concentrated in two industries
│   └── Late-stage feature-gap stalls rising
└── Pipeline quality
    ├── MQL volume up but conversion to SQL down
    ├── Marketing source mix shifted toward content
    └── BDR qualification depth varies by team
```

---

### 3. Hypothesis-Driven Problem Solving

**Hypothesis:** The cycle stretch is dominantly driven by internal handoff bottlenecks (security review, legal redlines, discount approvals) rather than by buyer-side dynamics or AE execution — meaning a sales reorg would not solve it.

| Variable | Expected (if hypothesis true) | Actual / Required Data |
|---|---|---|
| Time spent in late-stage internal review (security + legal + finance) | Should account for ≥40% of total cycle increase | Need to pull stage-time data from CRM — compare 6 mo. ago vs. now |
| Cycle length variance by AE tenure | Should be flat — handoff bottlenecks affect everyone | Need to bucket cycle times by AE tenure band |
| Cycle length by deal size | Should be uniform increase across all bands | Need to pull cycle by ACV band |
| Time-to-first-redlines from legal | Should be the largest single contributor to delay | Currently 18 days — historical baseline ~6 days. Matches if true |
| Win rates by stage (control) | Should be ROUGHLY stable — if hypothesis is right, deals are slow but still closing | Win rate from late-stage to closed-won: 64% (vs. historical 67%). Near-flat ✅ supports hypothesis |
| Buyer-cited reasons for delay (control) | Should NOT show "evaluating alternatives" rising sharply | Need to pull from win/loss interviews |
| New-hire AE quota attainment (control) | If primarily a ramp problem, attainment should diverge by tenure — if hypothesis is right, attainment should be uniformly down | Need to pull attainment by tenure band |

The two control rows (win rate stable, AE attainment uniform) are designed to invalidate the hypothesis. If they show otherwise, the picture changes — could be a competitive issue or a ramp issue, not a handoff issue.

---

### 4. Pareto Focus (80/20)

> **The vital 20%:** Two internal-process bottlenecks likely account for ~70-80% of the cycle stretch: (1) security review averaging 22 days (historical baseline ~8 days) — a single staffing issue post-Q2 reorg of the InfoSec team, and (2) legal redline turnaround at 18 days (historical baseline ~6 days) — a process bottleneck driven by one in-house counsel handling all vendor agreements. Both are fixable in weeks, not quarters.

**Actively deprioritized (the 80%):**
- Sales team reorg (premature — diagnose before restructuring)
- AE ramp programs (ramp is real but ~6 of 14 reps; not the dominant signal)
- Competitive feature gaps (real but not actionable in the 2-week board window)
- BDR qualification training (pipeline quality is degrading but secondary)
- Pricing simplification (root cause is approval velocity, not pricing complexity)
- Marketing source-mix overhaul (treats symptom, not cause)
- Reference customer expansion (helpful but slow)

---

### 5. The "So What?" Test

**Process:** Decomposed cycle-stretch drivers into five MECE categories; mapped them in an issue tree; tested the hypothesis that internal handoff bottlenecks dominate by examining stage-time data, win rates, and AE attainment patterns; isolated the highest-impact root causes via Pareto.

**Result:** Two internal bottlenecks — security review (22-day avg vs. 8-day baseline) and legal redlines (18-day avg vs. 6-day baseline) — together account for ~30 days of the 50-day cycle increase, or ~60% of the gap on existing data. Win rates and AE attainment do not yet show the patterns that would point to competitive or ramp problems. Buyer-side and deal-mix factors contribute, but are not the primary driver.

**Insight:** **Do not reorganize the sales team yet.** A sales reorg won't fix a security-and-legal-velocity problem. **Action for the next two weeks (before the board meeting):** (1) VP Revenue + COO commission a one-week sprint to validate the security/legal bottleneck hypothesis with actual CRM stage-time data, segmented by deal size and AE tenure. (2) Meet with the CISO and General Counsel to scope a 90-day intervention: temporary contract security reviewer + standardized MSA template. (3) Bring to the board not a reorg proposal but a "cycle compression plan" with named owners, 30-day and 90-day targets, and a fallback to revisit reorg if the bottleneck thesis is invalidated. **Owner:** VP Revenue. **Target:** cycle back to ≤80 days within one quarter, ≤65 within two.

---

## How to read this example

Notice what each section is doing:

- **Reframe at the top** — pushed back gently on the leadership-proposed reorg before applying any framework.
- **MECE** is a complete map of where the answer could live.
- **Issue Tree** drills into the map.
- **Hypothesis Test** picks the most likely answer and designs the test, with controls that would invalidate it.
- **Pareto** commits — names the 20% and explicitly deprioritizes a list of legitimate concerns.
- **So What?** lands on a specific, assignable, time-bound action that contradicts the leadership proposal with reasoning.

That's the shape of every output this skill produces. Different problems, same skeleton.
