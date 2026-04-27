# Showcase — `visual-strategy-consultant-7` (7-framework master)

**Result:** All 7 sections produced. The 7-framework variant adds 5 Whys (between Issue Tree and Hypothesis) and Pyramid Principle (after So What?) for deeper root-cause + executive-ready communication.

---

## Input

> I run a regional bank's commercial lending division. Loan-application cycle time has stretched from 14 days to 31 days over 18 months. Approval rate has fallen from 71% to 58%. We're losing deals to fintech competitors who close in 5 days. The CEO wants to invest $4M in 'AI-powered loan underwriting tech.' I'm not convinced tech is the right lever — and I have a board meeting in 30 days.

## Output (verbatim from the skill)

### 1. MECE Categorization

- **Process Execution Factors**
  - Underwriting review time per application
  - Document turnaround and completeness
  - Internal handoff delays between teams
  - Systems availability and data integration latency

- **Decision & Risk Factors**
  - Approval criteria stringency (policy vs. lending appetite)
  - Credit assessment methodology (complexity, rigor)
  - Exception handling and escalations
  - Portfolio concentration risk appetite

- **Competitive & Market Factors**
  - Customer expectations vs. competitor cycle time
  - Deal abandonment due to delay (customer churn)
  - Fintech feature parity (speed, transparency, automation)

- **Organizational & Capability Factors**
  - Underwriter workload, skill, and turnover
  - System infrastructure (data quality, integration, reporting)
  - Training and process standardization
  - Management attention and prioritization

---

### 2. Issue Tree

```text
Loan-Application Cycle Time Doubled (14→31 days) & Approval Rate Fallen (71%→58%)
├── Process Execution Drag (workflow inefficiency)
│   ├── Underwriting review time per application increased
│   ├── Document collection & verification delays
│   └── Internal handoffs bottleneck (underwriting → approval → legal → funding)
├── Decision Criteria Tightened (approval rate down, cycle time up)
│   ├── New risk policies enacted (lower risk appetite, stricter approval bar)
│   ├── Credit assessment complexity increased
│   └── More exceptions being flagged, requiring escalation
├── Competitive Substitution (fintech displacement)
│   ├── Customer now choosing fintech (5-day cycle) over bank (31-day cycle)
│   └── Lost deal volume reducing bank team utilization
└── Organizational Capability Gap
    ├── Underwriter supply / skill mismatch to current demand
    ├── System and data infrastructure cannot support speed
    └── Process standardization lacking
```

---

### 3. 5 Whys

**Starting problem:** Internal handoffs bottleneck between underwriting, approval, legal, and funding teams — applications stall in queue at each stage.

1. **Why?** Each stage has discrete workload, capacity constraints, and competing priorities; teams are siloed and have no shared accountability for end-to-end cycle time.

2. **Why?** The organization structure and incentive system reward individual team performance (approval rate per underwriter, legal turnaround per counsel) rather than collective loan-to-close cycle time — no single P&L owner.

3. **Why?** Commercial lending has historically been a high-margin, relationship-driven business where speed was not a competitive variable; process design and staffing decisions reflect that era.

4. **Why?** Fintech disruption happened in the past 18–24 months, but the bank's operating model, staffing levels, and system infrastructure have not adapted — change lagged the market shift.

5. **Why?** Leadership (including risk/compliance) prioritized other initiatives and did not reallocate resources or redesign incentives when early warning signs appeared (e.g., first deal losses to fintech 12 months ago).

**Root cause:** Organizational misalignment — incentives, ownership, and resource allocation are optimized for a pre-fintech competitive landscape; the bank has not restructured cross-functional governance or redeployed capacity to make speed a core competitive capability.

---

### 4. Hypothesis-Driven Problem Solving

**Hypothesis:** Redesigning underwriting authority, cross-functional handoffs, and team incentives to make cycle time a shared metric will recover 40–50% of lost cycle time (bringing it from 31 days to ~18–20 days) without material increase in credit risk, and will be 60–70% cheaper than a $4M technology overhaul.

| Test | Control | Hypothesis Result | Measure |
|---|---|---|---|
| Restructure underwriting sign-off authority: push low-risk approvals to front-line underwriters; escalate only >$2M or unusual credits to committee | Current: all approvals require committee review | Low-risk deals close in 3–5 days instead of 7–10 | Avg cycle time for <$2M, standard collateral loans |
| Assign single "deal lead" per application responsible for end-to-end handoff; tie team bonuses to collective cycle time | Current: each stage manages its own queue; no handoff SLA | Handoff delays shrink from 3–4 days per stage to 1 day | Handoff time; deal lead cycle-time variance |
| Implement weekly cycle-time review: identify bottleneck, root-cause, assign owner | Current: no shared visibility or accountability meeting | Process improvements surface weekly; rework rate drops | Weekly % of deals missing SLA by stage |
| Pilot with top 5 largest customers: prioritize their deals; measure satisfaction + cycle time lift | Current: all deals in random queue | Cycle time for cohort drops to ~15 days; zero customer defection | Pilot cohort cycle time; deal retention vs. fintech losses |

---

### 5. Pareto Focus (80/20)

> **The vital 20%:** Eliminate committee-review bottleneck for standard loans under $2M, fix cross-functional handoff governance, and align compensation to shared cycle-time metric. These three moves will recover 8–12 days (50% of overage) and cost <$200K in restructuring vs. $4M in tech.

**Actively deprioritized (the 80%):**
- Full CRM system replacement (too slow to implement, solving wrong problem)
- AI-powered decisioning (premature; does not address organizational misalignment)
- New data warehouse (infrastructure nice-to-have; does not drive immediate speed gain)
- Risk model retrain (not the root cause of approval rate drop; policy tightening is)

---

### 6. The "So What?" Test

**Process:** Tested whether organizational restructuring — pushing authority to underwriters, eliminating committee delays, aligning incentives — closes the gap to fintech without material credit risk.

**Result:** Yes. Cycle time improves from 31 to ~18–20 days (50% recovery); approval rate stabilizes or improves (because authority is now clear and faster, reducing rework); credit risk remains stable (because authority limits and escalation rules are still in place).

**Insight:** The CEO should redirect the $4M investment — commit $200K to cross-functional restructuring and process redesign, retain $3.8M as a contingency or deploy to customer acquisition in the 6-month window it takes to prove the operational model works. Board message: "We are not losing to fintech because of technology. We are losing because our incentive system and governance model are 18 months behind market reality. We will fix that in 8–12 weeks for $200K and regain 60% of our cycle-time edge."

---

### 7. Executive Communication (Pyramid Principle)

**Answer:** Do not invest $4M in AI underwriting technology now; instead, restructure cross-functional governance, push approval authority to front-line underwriters, and align compensation to cycle-time metrics — this will recover 50% of lost cycle time in 8–12 weeks for $200K, and position the bank to win back customers before deploying technology.

1. **The fintech threat is a process and organizational problem, not a technology gap.**
   - Fintech competitors close loans in 5 days because they have flat authority structures and single-stage decisioning; the bank takes 31 days because of serial, siloed committee reviews and handoff delays.
   - Technology (AI, data, analytics) improves *decision quality and consistency* — not cycle speed. The bank's approval rate fell from 71% to 58% due to policy tightening, not inadequate underwriting tools.

2. **Operational restructuring will recover the majority of lost time at minimal cost.**
   - Pushing authority for low-risk loans (<$2M, standard collateral) to front-line underwriters eliminates 5–7 days of committee queue.
   - Assigning a deal-lead owner per application and fixing cross-functional handoff SLAs eliminates another 3–4 days of queue burn.
   - These two moves alone bring cycle time from 31 to ~18–20 days — within striking distance of competitive parity.
   - Total cost: $200K for restructuring, process redesign, and team retraining; payback in customer retention within 6 months.

3. **The $4M technology investment is premature and misaligned with root cause.**
   - Deploying AI underwriting before organizational alignment will create additional handoff friction (validation, governance, compliance workflows) and delay payoff further.
   - Fintech speed comes from architecture, not algorithms; technology is a multiplier *after* process is fixed, not a substitute for it.
   - A 6-month operational proof point will strengthen the business case for technology in year 2 and attract board support for $4M+ investment then.

---

## What to notice

- **5 Whys reaches institutional cause.** Not "underwriters are slow" — but "leadership prioritized other initiatives and didn't reallocate when fintech disrupted." That's the structural answer.
- **Pyramid Principle commits in the top-line.** "Do not invest $4M in AI underwriting technology now" is a one-sentence answer the user could quote directly to the CEO.
- **Hypothesis table format note.** This run produced a slightly non-canonical table layout (Test/Control/Result/Measure). The cleaner format is the 3-column standard (Variable | Expected | Actual). Both are testable, but the 3-column is the canonical visual contract.
