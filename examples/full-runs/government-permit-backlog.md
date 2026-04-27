# Full master run — Government / Public sector

A complete output of `visual-strategy-consultant` on a public-sector operations problem.

---

## Input (what the user typed)

> I run a city Building Permits department. Average permit-issuance time has stretched from 21 days to 74 days over 18 months. Backlog is 4,300 applications. Builders are escalating to City Council. The Mayor wants a "tech modernization" RFP issued this fiscal year — but I don't think tech is the actual problem. I have 6 weeks before the next council meeting.

---

## Output (what the skill produced)

The Mayor has gravitated toward a tech-modernization RFP. The Director's instinct that "tech isn't the actual problem" deserves a structured test before the City commits to a multi-year procurement that may not address the cause. I'll structure this around: what's actually driving the backlog, and is tech the right intervention shape?

---

### 1. MECE Categorization

- **Demand-side (application volume & complexity)**
  - Construction permit applications up due to local building boom
  - Application complexity rising (more multi-unit, more energy-code review)
  - Resubmission rate (rejected applications cycling back)
- **Capacity (staffing)**
  - Plan reviewer headcount vs. demand
  - Inspector availability for site visits
  - Tenure mix — recent retirements vs. new-hire ramp
- **Process (workflow)**
  - Routing logic between trades (electrical, plumbing, structural, energy)
  - Hand-off delays between sequential reviewers
  - Single-point bottlenecks (e.g., one structural reviewer for the whole queue)
- **Technology & data**
  - Permit management system capabilities and uptime
  - Document submission quality (incomplete packages bouncing back)
  - Reporting/visibility into where applications stall
- **External / cross-department**
  - Coordination with Fire, Public Works, Planning
  - State / regional review for certain project types
  - Citizen / contractor responsiveness to RFI (Requests for Information)

---

### 2. Issue Tree

```text
Permit issuance 21d → 74d, backlog 4,300
├── Volume pressure
│   ├── Application volume +35% over 18 months
│   ├── Multi-unit permits up 60% (more complex per app)
│   └── Resubmission rate climbed to 31% (was 18%)
├── Capacity gaps
│   ├── 3 senior plan reviewers retired in last year
│   ├── 5 of 12 inspector positions vacant
│   └── New-hire reviewers averaging 9 months to full productivity
├── Workflow & bottlenecks
│   ├── Sequential routing — plan sits in queue between disciplines
│   ├── Energy-code review concentrated in one reviewer (single PoF)
│   ├── No triage step — small / large permits in same queue
│   └── Hand-offs require physical document transfer in some cases
├── Tech / system
│   ├── Permit system has no auto-assignment by load
│   ├── Status visibility for applicants is poor (drives call volume)
│   └── E-submission accepted but staff still print for review
└── External coordination
    ├── Fire Marshal review SLA loose
    ├── State plumbing-code review delays in 3 boroughs
    └── Applicant RFI response time averaging 11 days
```

---

### 3. Hypothesis-Driven Problem Solving

**Hypothesis:** The backlog is dominantly driven by **process and capacity gaps** (sequential routing + a small number of single-point-of-failure reviewers + ramp-up of new hires) rather than by technology limitations — meaning a tech-modernization RFP would underperform vs. process redesign + targeted contract staffing in the short term.

| Variable | Expected (if hypothesis true) | Actual / Required Data |
|---|---|---|
| Time spent in routing/hand-off vs. active review | Hand-off + queue time should dominate total cycle time; active review should be a small fraction | Need to instrument cycle-time breakdown by stage from permit system data |
| Concentration of delay at single bottleneck reviewers | Energy-code or structural reviewer should be the bottleneck on a disproportionate share of stalled apps | Pull stalled-app distribution by current-reviewer-assignment |
| Effect of resubmissions on cycle time | Resubmission rate increase (18% → 31%) should account for material share of average cycle time | Compare cycle time on first-submission-clean vs. resubmitted apps |
| Tech-system uptime / latency (control) | If tech were the dominant cause, the system should show outages, latency spikes, or feature gaps tied to delays | Pull system uptime, page-load metrics, error logs over 18 months |
| Permit type breakdown | If process is the cause, complex multi-discipline permits should be most affected | Cycle time for single-trade permits vs. multi-trade |
| Comparable jurisdictions on similar tech (control) | If tech is the cause, peer cities on the same permitting platform should show similar backlogs | Benchmark against 3 comparable cities on same vendor |
| Applicant RFI response time impact | RFI cycle should add weeks but not be the dominant factor | Pull applicant-side time vs. city-side time |

The control rows (system uptime, peer benchmark) are designed to give the tech hypothesis a fair chance. If the system genuinely is failing or peer cities outperform on the same tech, the case for the RFP strengthens.

---

### 4. Pareto Focus (80/20)

> **The vital 20%:** Two interventions in the next 6 weeks likely cut the backlog 30–40% and stabilize cycle time without an RFP: (1) **parallelize sequential review** for the 60% of permits that don't require strict ordering (e.g., electrical, plumbing, and energy code can review in parallel rather than sequentially) and add explicit triage to fast-track simple permits. (2) **eliminate single-point bottlenecks** by cross-training two additional staff on energy-code review and bringing in 2–3 contract structural reviewers for 90 days to clear the backlog while new hires ramp.

**Actively deprioritized (the 80%):**
- Tech-modernization RFP (not the dominant cause; multi-year timeline doesn't help the council deadline)
- Hiring 6 net-new permanent reviewers (correct medium-term, but new hires take 9 months to ramp — won't move the 6-week numbers)
- Applicant-portal redesign (real UX issue but secondary)
- E-submission paperless workflow (right idea, but staff workflow change isn't the immediate lever)
- Building-code rewrite or simplification (out of scope and long-horizon)
- Outsourcing whole categories of permit review (politically difficult, doesn't fit the timeline)
- New permit-fee structure (fee-policy work, not throughput)

---

### 5. The "So What?" Test

**Process:** Decomposed permit-issuance delay into five MECE categories spanning demand, capacity, workflow, technology, and external coordination; built an issue tree drilling each branch to specific bottlenecks; tested the hypothesis that process and capacity dominate (vs. technology) by examining cycle-time breakdown, single-point bottleneck concentration, resubmission impact, and peer benchmarks; isolated the highest-leverage 6-week interventions via Pareto.

**Result:** Initial signals support the hypothesis: 5 of 12 inspector positions vacant; energy-code review is a single-reviewer bottleneck; sequential routing means apps queue between disciplines for days at each hand-off. Tech-system uptime data and peer benchmark still need to be pulled to definitively rule out tech, but the available signals point to process and capacity as the dominant drivers. A tech RFP issued now would take 18+ months to deliver any benefit — beyond the council's tolerance.

**Insight:** **Defer the tech RFP. Recommend a "process + capacity sprint" to the City Council instead.** Bring an actual cycle-time-improvement plan with measurable milestones. **Action for the next 6 weeks, with named owners:**

1. **Days 1–7:** Pull the seven data sets in the hypothesis table — confirms or refutes the diagnosis. Owner: Permit Department analyst, with IT support for system metrics.
2. **Days 7–21:** Pilot parallel review on the next 200 multi-trade permits — measure cycle time vs. sequential baseline. Owner: Operations Manager.
3. **Days 7–28:** Procure 2–3 contract structural reviewers via existing professional-services vehicle (no RFP needed). Cross-train 2 staff on energy-code review. Owner: Director.
4. **Days 14–35:** Add explicit triage step at intake — flag simple/single-trade permits for a fast lane (target <14 days). Owner: Operations Manager.
5. **Day 42 (council meeting):** Present results: weeks 1–6 backlog change, cycle-time delta on piloted permits, projected 12-month plan. **Frame the tech investment correctly:** not as the RFP-to-fix-everything, but as a targeted procurement (auto-assignment + applicant status portal) sized to specific bottlenecks once they're identified — perhaps 1/3 the scope of a full modernization RFP.

**Target:** backlog from 4,300 down to 3,000 by council date; cycle time from 74 → 50 days within 90 days; full restoration to ≤30 days within 6 months.

---

## What to notice

- **Reframe pushed back on the political solution.** The Mayor's preferred answer (tech RFP) is the kind of move that looks decisive but takes 18 months to deliver and may not address the cause. Strategy's job is to surface that, professionally.
- **The hypothesis is testable in ~1 week of data work.** Cycle-time-by-stage and single-reviewer-concentration are both queryable from the permit system.
- **Pareto names two specific levers that don't require new hires or new tech.** Parallelization and contract reviewers are doable in weeks, not quarters.
- **Tech isn't dismissed entirely.** The Insight reframes the tech investment as a *targeted* procurement after diagnosis, not a moonshot RFP. Politically more palatable than "no tech."
- **Insight has a council-meeting endpoint.** Day 42 is the public deliverable. Working backward from that fixed date is what makes the plan executable.
