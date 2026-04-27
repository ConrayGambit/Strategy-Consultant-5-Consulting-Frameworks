# Issue Trees — Healthcare

A standalone run of the `issue-trees` skill on a hospital-operations problem.

---

## Input (what the user typed)

> 30-day readmission rate for our cardiology service line jumped from 11.2% to 16.8% over two quarters. CMS penalties are at risk. Build me an issue tree of plausible root causes — I'll prioritize from there.

---

## Output (what the skill produced)

```text
30-day cardiology readmissions 11.2% → 16.8%
├── Inpatient care quality
│   ├── Diagnostic accuracy (missed comorbidities)
│   ├── Length-of-stay reductions cutting recovery time
│   └── Medication reconciliation at admission incomplete
├── Discharge process
│   ├── Discharge planning starting too late in stay
│   ├── Patient education on signs of decompensation weak
│   ├── Medication list at discharge vs. admission mismatched
│   └── Care-team handoff to outpatient cardiologist delayed
├── Post-discharge follow-up
│   ├── Time-to-first-outpatient-visit lengthening
│   ├── Telehealth follow-up program reduced post-pandemic
│   ├── Pharmacy access delays for new prescriptions
│   └── Home health referral not consistently made
├── Patient population shift
│   ├── Acuity mix increasing (sicker patients admitted)
│   ├── Older / more comorbid cohort vs. baseline
│   └── Socioeconomic / transportation barriers to follow-up
└── External care coordination
    ├── PCP capacity constraints in catchment area
    ├── Skilled nursing facility partner quality variation
    └── EHR interoperability gaps with external providers
```

---

## What to notice

- **Three levels deep where it warrants it.** Most branches drill to leaves that are testable in days (e.g., "time-to-first-outpatient-visit lengthening" is a single SQL pull from the EHR). One branch (Patient population shift) stays at two levels because the leaves are themselves the testable units.
- **Branches MECE at each level.** "Inpatient care quality" doesn't overlap with "Discharge process" — they're sequential phases of the patient journey. "Post-discharge follow-up" doesn't overlap with "External care coordination" because the latter is about partner organizations, not the patient touchpoint cadence.
- **Categories follow the patient journey.** Inpatient → Discharge → Post-discharge → Population → External. That structure is more useful for a hospital ops leader than generic Quality/Process/Tech buckets, because it maps to the people and systems that own each phase.
- **Leaves are testable but not solutions.** "Discharge planning starting too late in stay" is a hypothesis to investigate, not a solution. The next step would be to run `hypothesis-driven` on the most likely branch, then `pareto-principle` to commit to interventions.
- **Could fall back to indented dashes** if pasting into Slack or an email client that mangles `├──` characters. The fallback is documented in the skill itself.
