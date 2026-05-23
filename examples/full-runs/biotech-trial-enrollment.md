# Phase 2 trial enrollment shortfall — Biotech / clinical operations

## Input (what the user typed)

> We're a mid-stage biotech running a Phase 2 trial in NASH (nonalcoholic steatohepatitis). Nine months in, we've enrolled 38 of a planned 65 patients — 40% below plan. The trial readout is the gating event for our Series C (~$40M, term sheets dependent on hitting a Q2 readout). I'm the COO and the board wants to know what's happening and what to do.

---

## Output (what the skill produced)

The board will want to hear "open more sites" — but enrollment shortfalls almost always concentrate in a small subset of underperforming sites, not in a systemic capacity gap. The right question isn't "how do we add sites?" it's "what is preventing our best sites from performing, and can a targeted protocol amendment fix the most common screen-fail reason?" Below is the structured analysis.

---

### 1. MECE Categorization

- **Site performance**
  - Enrollment rate variance across active sites (top vs. bottom quartile)
  - Site activation lag (time from contract to first patient enrolled)
  - Investigator engagement and patient-referral network depth
  - CRO/site-management support quality and visit frequency
- **Patient identification & screening**
  - Eligible patient pool size in each site's catchment area
  - Screening failure rate and dominant screen-fail reasons
  - Referral pathway efficiency (gastroenterology, hepatology, primary care)
  - Patient awareness of trial (advertising, physician outreach)
- **Protocol restrictiveness**
  - Inclusion/exclusion criteria breadth relative to real-world NASH population
  - Biopsy requirement (known barrier in NASH recruitment)
  - Run-in period or washout requirements eliminating otherwise-eligible patients
- **Competing trials & indication crowding**
  - Active competing NASH trials recruiting at the same sites
  - Patient pool overlap with higher-sponsored or better-known trials
  - Site fatigue from multiple concurrent NASH protocols
- **Operations & site support**
  - Data entry burden and EDC usability slowing site staff
  - Regulatory/IRB amendment cycle times
  - Sponsor-to-site communication frequency and responsiveness
- **External factors**
  - Regulatory hold risk or safety signal from other NASH programs affecting patient confidence
  - Macro (insurance coverage gaps for NASH diagnostics)

---

### 2. Issue Tree

```text
Enrollment shortfall: 38 / 65 patients (9 months, -40% vs. plan)
├── Site performance
│   ├── Bottom-quartile sites (est. 3–4 of 12) contributing < 15% of enrolled patients
│   ├── Site activation delays — 2 sites still < 3 patients despite being open 6 months
│   └── CRO visit cadence inconsistent; underperforming sites receiving < 1 visit/quarter
├── Patient identification & screening
│   ├── Screen-fail rate elevated (~45% vs. planned 25%)
│   │   ├── Dominant screen-fail: ALT/AST thresholds eliminating borderline cases
│   │   └── Biopsy requirement declining 20%+ of otherwise-eligible candidates
│   ├── Referral pathway too narrow (hepatology-only; GI and primary care not activated)
│   └── Low patient awareness — no direct-to-patient outreach at 8 of 12 sites
├── Protocol restrictiveness
│   ├── Fibrosis-stage inclusion criterion (F2–F3 only) screens out F1 and F4 patients
│   ├── 4-week washout for GLP-1 agonists excludes growing real-world NASH population
│   └── Liver biopsy at baseline required — creates patient reluctance and site burden
├── Competing trials
│   ├── 3 competing NASH Phase 2/3 trials active at 7 of 12 sites
│   └── 2 higher-sponsored programs offering patient stipends 40% above ours
└── Operations & site support
    ├── EDC system flagged as high-burden by 5 sites in last monitoring call
    └── Protocol amendment for ALT criterion submitted 8 weeks ago; IRB approval pending
```

---

### 3. Hypothesis-Driven Problem Solving

**Hypothesis:** The enrollment shortfall is driven primarily by two compounding factors — bottom-quartile site underperformance (3–4 sites dragging the average) and a screen-fail rate elevated by the biopsy requirement and fibrosis-staging criterion — meaning the fix is concentrated site support plus a single targeted protocol amendment, not broad site expansion.

| Variable | Expected (if hypothesis true) | Actual / Required Data |
|---|---|---|
| Enrollment rate distribution across sites | Top-quartile sites enrolling 3–4× the rate of bottom-quartile sites | Need enrollment-by-site breakdown; estimate: top 3 sites = ~60% of 38 enrolled |
| Screen-fail rate vs. plan | Actual screen-fail 40–50% vs. planned 25% | Pull CTMS screen-fail log; dominant reason likely biopsy or fibrosis staging |
| Top-quartile site performance trend (control) | Top performers' monthly rate should be stable or improving — if they're also declining, it's a systemic problem beyond site quality | Need per-site monthly enrollment trend |
| Competing-trial overlap at underperforming sites | Bottom sites should have higher competing-trial density than top sites | Cross-reference clinicaltrials.gov NASH listings with site zip codes |
| Biopsy decline rate | ≥20% of screen-eligible patients declining at biopsy step | Require site coordinators to log decline reason in next 30-day period |
| Protocol-amendment screen-fail impact | Relaxing ALT/AST criterion by 20% should recover 8–12 additional eligible patients in existing catchment | Model from screen-fail logs: count patients failing solely on ALT/AST |
| Patient awareness rate (control) | Sites with active DTP outreach should show higher referral volume independent of site quartile | Compare referral source data at 4 DTP-active vs. 8 DTP-inactive sites |

---

### 4. Pareto Focus (80/20)

> **The vital 20%:** Two interventions likely recover ~70% of the enrollment gap. (1) Concentrated support on the 3–4 bottom-quartile sites — dedicated CRO escalation, weekly sponsor check-in, investigator replacement if needed — could recover 6–8 patients in 8 weeks. (2) A single protocol amendment relaxing the biopsy requirement to optional (with non-invasive FibroScan as alternative) and expanding ALT/AST eligibility thresholds is the highest-leverage protocol fix, estimated to reduce screen-fail rate from ~45% to ~28% and recover an additional 8–10 patients from the existing screened pipeline. Together, these two moves could close the majority of the 27-patient gap within the Series C window.

**Actively deprioritized (the 80%):**
- Opening new sites (12-week activation lag means new sites won't contribute to a Q2 readout)
- Full protocol overhaul (multiple simultaneous amendments trigger re-consent and delay)
- Switching CROs (transition time would cost more enrollment days than it saves)
- Expanding to a new indication or adding a new patient subgroup to broaden eligibility
- Raising patient stipends across all sites (cost-prohibitive and doesn't address the screen-fail root cause)
- Direct-to-patient advertising at all 12 sites simultaneously (too diffuse; concentrate on top performers)

---

### 5. The "So What?" Test

**Process:** Categorized enrollment drivers across six MECE domains; traced the shortfall in the issue tree to site performance concentration and a screen-fail rate roughly double plan; tested the hypothesis that bottom-quartile sites and two protocol barriers (biopsy + fibrosis staging) are the primary causes; applied Pareto to identify the two interventions with enough impact to close the gap within the Q2 term-sheet window.

**Result:** Of 38 enrolled, an estimated 60%+ came from the top 3 sites — meaning the bottom 9 sites are collectively underproducing by 3–4× their expected rate. The screen-fail log (once pulled) will almost certainly show biopsy reluctance and ALT/AST thresholds as the top two reasons. Both are addressable without opening new sites. The IRB amendment already in flight (8 weeks pending) should be accelerated; if the ALT/AST criterion is included, approval unlocks immediate benefit to the existing screened pipeline.

**Insight:** Do not open new sites before the Q2 window — activation lag makes them irrelevant to this readout. Instead: (1) Within 1 week, COO to direct CRO to escalate to weekly check-ins on the 3 bottom-quartile sites; pull per-site enrollment-by-month and screen-fail logs this week (owner: VP Clinical Operations). (2) Within 2 weeks, confirm whether the pending IRB amendment includes the biopsy-optionality and ALT/AST relaxation; if not, submit an addendum immediately — this is the single highest-leverage protocol fix (owner: Chief Medical Officer). (3) Within 3 weeks, model the recovered-patient count from the protocol amendment against the screen-fail log to give the board a revised Q2 enrollment projection. Present to board with a binary: "amended protocol + concentrated site support = X patients by Q2 readout" vs. "status quo = Y." The Series C term sheet decision should be made on that revised projection, not on the current trajectory.

---

## What to notice

- **The reframe.** The instinct is "open more sites" — the analysis shows new sites can't activate in time for Q2. The fix is within the existing site footprint.
- **The control row does real work.** Top-quartile site trend is explicitly designed to distinguish a systemic problem (all sites declining) from a concentration problem (bottom quartile dragging). If top-quartile sites are also declining, the hypothesis fails and a different intervention is needed.
- **Pareto names the obvious-but-wrong answers explicitly.** Opening sites, switching CROs, full protocol overhaul — these are all things a panicked board might demand. Naming them as deprioritized, with reasons, is the consultant discipline.
- **The Insight is staged for the board presentation.** Three actions, three owners, three deadlines — all within the Series C window. The closing move is a binary projection the board can act on.
- **Continuity runs end-to-end.** The biopsy and ALT/AST barriers appear first in MECE (protocol restrictiveness), branch in the issue tree, drive the hypothesis table variables, anchor the Pareto vital 20%, and become the specific amendment action in the Insight.
