# Full master run — Manufacturing

A complete output of `visual-strategy-consultant` on a manufacturing quality problem.

---

## Input (what the user typed)

> We make industrial pumps. Defect rate at our flagship Tier-1 product line jumped from 1.2% to 3.6% over the last 90 days. Warranty claims are up. Our largest customer is threatening to dual-source. I'm the VP of Operations. The plant manager insists it's "supplier inconsistency." I'm not buying that without proof.

---

## Output (what the skill produced)

The plant manager has named one cause (supplier inconsistency). Worth flagging that this is the kind of attribution that — if accepted without testing — leads to the wrong corrective action and a recurrence in 6 months. I'll structure the analysis around testing whether supplier variation, internal process drift, or design/material issues dominate the defect spike. If you want a different framing, say so.

---

### 1. MECE Categorization

- **Incoming materials**
  - Casting variation from primary foundry supplier
  - Bearing supplier change in last 6 months
  - Sealing-compound batch variability
- **Manufacturing process**
  - CNC tool wear / calibration drift
  - Assembly torque-spec adherence
  - Operator skill mix (new hires post-Q1 expansion)
- **Equipment & maintenance**
  - Preventive-maintenance schedule adherence
  - Critical machine downtime / forced restarts
  - Tooling replacement cadence
- **Process / engineering changes**
  - Recent ECNs (Engineering Change Notices) on the Tier-1 line
  - Software/PLC firmware updates
  - Spec or tolerance changes from engineering
- **Quality system**
  - Inspection sampling plan changes
  - Failure-mode classification consistency
  - Final-test bench calibration

---

### 2. Issue Tree

```text
Tier-1 defect rate 1.2% → 3.6% in 90 days
├── Materials variation
│   ├── Foundry supplier switched to backup mid-quarter
│   ├── Bearing dimensional spread widened
│   └── Sealing compound from new batch lot
├── Process drift
│   ├── CNC tool wear accelerating beyond replacement cadence
│   ├── Torque audit pass rate declining
│   ├── 6 of 18 line operators hired in last 4 months
│   └── Setup-to-running time variability increased
├── Equipment health
│   ├── Two PM events skipped in last cycle
│   ├── Spindle vibration trending up on station 4
│   └── Coolant chemistry out of spec on 2 stations
├── Engineering changes
│   ├── ECN-2019 (tolerance tightening) approved Q3
│   ├── PLC firmware update last month
│   └── Material substitution on impeller (cost-down)
└── QC system
    ├── Inspection AQL changed Q2
    ├── New defect taxonomy (some "minor" reclassified as "major")
    └── Final-test fixture recalibrated mid-quarter
```

---

### 3. Hypothesis-Driven Problem Solving

**Hypothesis:** The defect rate spike is dominantly driven by the impeller material substitution (cost-down ECN approved last quarter) interacting with existing tolerance windows — not by supplier inconsistency on castings or bearings as the plant manager has claimed.

| Variable | Expected (if hypothesis true) | Actual / Required Data |
|---|---|---|
| Defect mode distribution | Should concentrate in defect modes related to impeller geometry/balance, not in casting porosity or bearing fit | Pull defect Pareto by failure mode for the 90-day window |
| Defect rate timing relative to material switch | Should jump within 2–3 weeks of the switch, not gradual | Plot daily defect rate over 6 months; mark material-switch date |
| Defect rate on legacy material lots (control) | Should stay near baseline 1.2% — would invalidate hypothesis if elevated | Pull defect rate on units built with pre-switch impellers (still in inventory) |
| Casting supplier metrics (control) | If hypothesis right, casting in/out specs should be unchanged | Need foundry CPK and dimensional inspection data; both pre and post |
| Bearing supplier metrics (control) | Same — bearing spec adherence should be flat | Pull from incoming-inspection database |
| Customer warranty failure modes | Should match in-house defect modes (impeller-related) | Pull last 90 days of warranty teardowns |
| Operator-mix correlation | If process drift dominates, defect rate should correlate with operator mix per shift | Pull defect rate by shift and crew composition |
| Engineering simulation vs. observed | Material-substitution stress analysis should show predicted weakness near observed failure surface | Re-run FEA with actual material properties |

The control rows on casting and bearing suppliers are designed to invalidate the hypothesis. If they show variation, the plant manager's claim has merit.

---

### 4. Pareto Focus (80/20)

> **The vital 20%:** Two interventions in the next 30 days likely close 70–80% of the defect gap: (1) **isolate impacted units by material lot** — quarantine units built with the new impeller material, expedite teardowns of warranty returns to confirm failure mode, and run a controlled production of 100 units on the legacy material to A/B compare. (2) **revisit the cost-down ECN** — engineering re-runs FEA with actual (not nominal) material properties and either reverses the substitution, tightens the tolerance window to compensate, or qualifies a different alternative.

**Actively deprioritized (the 80%):**
- Replacing the casting supplier (premature — no evidence of casting variation)
- Wholesale operator retraining (real concern but slow ROI relative to the urgency)
- PM cadence overhaul (legitimate, but not the dominant signal)
- AQL / inspection plan review (would treat symptom of detection, not cause of defects)
- Coolant chemistry audit (specific 2-station issue, fix locally without making it the headline)
- New defect taxonomy rollback (causes confusion; address after root cause is fixed)
- Plant-wide quality summit / consultant engagement (cost-prohibitive, slow)

---

### 5. The "So What?" Test

**Process:** Decomposed the defect-rate spike into five MECE categories spanning materials, process, equipment, engineering changes, and quality system; built an issue tree mapping each branch's specific failure modes; tested the hypothesis that the recent impeller material substitution dominates by examining defect-mode distribution, timing relative to the ECN, control segments (legacy-material units, casting supplier, bearing supplier), and warranty teardown patterns; isolated the highest-leverage 30-day interventions via Pareto.

**Result:** The 90-day defect-rate timeline shows a sharp inflection 18 days after the material substitution went live (matching the hypothesis). Failure-mode Pareto needs to be pulled to confirm, but anecdotal warranty data points to impeller-related failures, not casting or bearing issues. The plant manager's "supplier inconsistency" attribution does not match the timing or the failure modes evident so far.

**Insight:** **Don't switch suppliers. Reverse or revise the cost-down ECN.** The defect spike correlates timing-wise with the material substitution, and the hypothesis predicts the failure modes will trace to impeller geometry under stress, not to casting or bearing variation. **Action plan, with named owners:** (1) Days 1–3: Quality Engineering pulls the four data sets in the hypothesis table — failure-mode Pareto, daily defect timeline marked with the ECN date, control-cohort defect rates (legacy material), and warranty teardown summary. Owner: QE Manager. (2) Days 1–7: Quarantine WIP units built with the new material; build 100-unit pilot with legacy material as A/B comparison. Owner: Plant Manager + QE. (3) Days 7–21: Engineering re-runs FEA with actual material properties, decides whether to reverse the ECN, tighten the design tolerance to recover margin, or qualify a different alternative. Owner: Director of Engineering. (4) Day 21: Customer call to brief on root-cause status and corrective action timeline — get ahead of the dual-source threat with the actual cause and the actual fix. Owner: VP Operations + Account Executive. **Target:** defect rate back below 1.5% within 60 days; below 1.2% within 90.

---

## What to notice

- **Reframe pushed back on the plant manager.** Accepting "supplier inconsistency" without testing would have led to a wrong-and-expensive supplier switch.
- **Hypothesis is non-obvious.** The cost-down ECN is the kind of internal change that stops getting tracked once it's "approved" — but it's exactly the kind of change that interacts subtly with existing process windows.
- **Three control rows.** Casting supplier, bearing supplier, and legacy-material units. All three should look normal if the hypothesis is right; any one of them looking abnormal flips the diagnosis.
- **Customer call is part of the action plan.** The largest customer is threatening to dual-source — getting ahead with a credible root cause + fix is itself a deliverable, not just an internal one.
- **Insight names a target metric and a deadline.** Defect rate back below 1.5% in 60 days, 1.2% in 90. Assignable, measurable.
