# Matchday attendance & season-ticket renewals down — Pro football club

## Input (what the user typed)

> I'm the COO of a mid-table Premier League-style football club. Matchday attendance is down 18% YoY (avg 24,500 → 20,100 in a 31,000-capacity stadium). Season-ticket renewals came in at 71% (vs 84% the prior year). A new rival club opened 12 miles away and is converting our outer-district fans. The chairman wants a "fan engagement strategy." I'm not sure that's the right question.

---

## Output (what the skill produced)

Your instinct is right — "fan engagement strategy" is the wrong frame. The data pattern here is a geographic-cohort churn problem: outer-district fans are defecting to a closer local alternative, and the fix is a targeted price and access response for that specific segment, not a brand campaign aimed at everyone. Here is the structured analysis.

---

### 1. MECE Categorization

- **On-pitch performance**
  - League position and trajectory vs. prior season
  - Quality of home matchday football (chances, wins, entertainment value)
  - Transfer activity perception (squad investment signal to fans)
- **Matchday experience**
  - Stadium atmosphere and facility quality vs. the new rival's ground
  - Food, beverage, and hospitality offer relative to price paid
  - Accessibility and travel time — particularly for outer-district fans
  - Pre- and post-match entertainment and dwell time
- **Pricing & accessibility**
  - Season-ticket price relative to household income in outer vs. inner districts
  - Match-by-match ticket availability and pricing (secondary market leakage)
  - Family and concession pricing competitiveness vs. new rival
  - Payment plan and installment access for renewals
- **Geographic catchment**
  - Inner-district (≤5 miles) fan retention rate vs. outer-district (5–15 miles)
  - Overlap between club's outer-district fan base and new rival's catchment area
  - Commute and travel cost differential vs. attending the new rival
- **Competition from the new rival**
  - New rival's season-ticket price point and early-bird incentives
  - New rival's matchday experience (proximity, parking, atmosphere for new ground)
  - New rival's fixture calendar — home-fixture clashes pulling shared fans
- **Communication & loyalty programme**
  - Renewal conversion funnel — at what stage did the 13pp drop-off occur?
  - Loyalty points programme perceived value and redemption rate
  - Fan communication frequency and personalization vs. prior year

---

### 2. Issue Tree

```text
Attendance -18% YoY (20,100 avg); season-ticket renewals 84% → 71%
├── Geographic catchment
│   ├── Outer-district fans (5–15 mi) disproportionately churning
│   │   ├── New rival 12 miles away — closer for this segment
│   │   ├── Travel cost and time differential now favors rival
│   │   └── Rival's new ground: parking, modern facilities, lower prices
│   └── Inner-district fans (≤5 mi) — renewal rate likely stable (need to verify)
├── Pricing & accessibility
│   ├── Season-ticket price unchanged despite rival's introductory pricing
│   ├── Outer-district family segment — per-head cost significantly higher vs. rival
│   └── No installment option for renewals (renewal friction)
├── On-pitch performance
│   ├── Mid-table finish — no Champions League, no relegation battle (low stakes games)
│   └── High-profile departures in summer transfer window (squad quality signal)
├── Matchday experience
│   ├── Ageing stadium vs. new-build rival — perceived quality gap for families
│   ├── Food/beverage price complaints concentrated in outer-district survey feedback
│   └── Pre-match entertainment not tailored to family segment
├── Rival competition
│   ├── Rival's introductory season-ticket 30–40% cheaper than incumbent pricing
│   └── Rival fixture calendar — 6 home clashes scheduled this season
└── Communication & loyalty
    ├── Renewal reminder timing late (2 months after season end vs. 4 months prior year)
    └── Loyalty programme rewards perceived as low-value by churned segment
```

---

### 3. Hypothesis-Driven Problem Solving

**Hypothesis:** The attendance and renewal decline is concentrated in the outer-district family segment (5–15 miles from the stadium), driven by the new rival's price and proximity advantage — inner-district fans are largely unaffected, meaning the fix is a targeted price and access intervention for that segment, not a broad engagement campaign.

| Variable | Expected (if hypothesis true) | Actual / Required Data |
|---|---|---|
| Season-ticket renewal rate by distance band | Outer-district (5–15 mi) renewal rate should be materially lower than inner-district (<5 mi) | Pull renewal data by postcode; segment into distance bands from stadium |
| Inner-district renewal rate (control) | Should be near flat (84% → 82% or better) — inner fans have no closer rival alternative | Run postcode analysis; if inner-district is also declining sharply, on-pitch or experience is the driver, not geography |
| Churned fan destination survey | Churned outer-district fans should report attending the new rival as the primary reason | Run 300-person exit survey or email to non-renewers; offer incentive for response |
| Family-segment renewal rate vs. singles | Families with children should churn at higher rate (price sensitivity, travel burden, rival's family offer) | Cross-reference renewal database with family-ticket purchasers from prior year |
| Rival's season-ticket price differential | Rival's all-in family ticket should be 30%+ cheaper for the outer-district segment on a per-mile basis | Pull rival's published pricing; model travel cost at 12-mile journey vs. incumbent |
| Matchday attendance by fixture type (control) | Big-fixture attendance (top-6 opponents, cups) should hold better than routine mid-table home games | Compare YoY attendance by fixture tier; if big games are also down, it's not just routine-game drift |
| Match-by-match buyer composition | Walk-up and single-game buyers should also be declining in outer-district postcodes | Pull match-by-match postcode data for casual buyers |

---

### 4. Pareto Focus (80/20)

> **The vital 20%:** One root cause accounts for the majority of the renewal gap: outer-district family-segment churn to the new local rival, driven by price and proximity. If the postcode analysis confirms inner-district renewal is holding near 84% while outer-district is at 60–65%, roughly 80% of the 13pp aggregate renewal decline traces to that single geographic-cohort. A targeted outer-district family retention offer — early-bird price lock, installment plan, and travel subsidy or free matchday transport — is the highest-leverage intervention before the pre-season renewal window.

**Actively deprioritized (the 80%):**
- Generic fan engagement campaign (undifferentiated spend across all fans; misses the segment-specific cause)
- Loyalty programme redesign (low-value perception is a symptom, not the root cause; rewards don't offset a 30% price differential)
- Stadium redevelopment or capital refurbishment (decade-long horizon; irrelevant to next renewal window)
- Broad matchday experience overhaul (relevant but second-order; families aren't leaving because of food prices, they're leaving because of proximity and cost)
- Increasing marketing spend to acquire new fans to offset churn (acquiring new fans is 5–7× more expensive than retaining existing ones; fix churn first)
- On-pitch investment signals (correct long-term but outside the pre-season renewal decision window)

---

### 5. The "So What?" Test

**Process:** Categorized the attendance and renewal decline across six MECE domains; traced the pattern in the issue tree to a geographic-cohort concentration in outer-district fans rather than systemic disengagement; tested the hypothesis that inner-district renewal is holding (control row) while outer-district churn is driving the aggregate decline; applied Pareto to identify a targeted retention offer as the primary intervention over a generic engagement campaign.

**Result:** The postcode analysis (once pulled) will almost certainly show the 13pp renewal gap concentrating in a 5–15 mile radius band that now has a local rival alternative. Inner-district fans have no comparable alternative and their renewal rate should be near flat — if confirmed, this validates that the problem is geographic and price-driven, not a club-wide engagement failure. The rival's introductory pricing (est. 30–40% cheaper) and proximity advantage are structural; the club cannot close the distance gap but can close the price gap for the specific segment at risk.

**Insight:** Reject the chairman's "fan engagement strategy" framing before the board meeting — it risks diluting budget across a problem that is actually concentrated in one segment. Instead: (1) Within 2 weeks, pull postcode-level renewal data and segment by distance band (owner: Head of Ticketing & Data, due before board presentation). (2) If outer-district renewal is confirmed at ≤65% vs. inner ≥82%, design a targeted outer-district family retention package: season-ticket price lock at prior-year rate (no increase), 12-month installment plan at 0% interest, and a matchday travel subsidy (free coach from two outer-district pick-up points on home matchdays) — model the cost vs. the revenue of recovering 200 season tickets at average yield (owner: Commercial Director + COO, package ready within 3 weeks). (3) Launch the retention offer as an early-bird pre-season window exclusively to outer-district non-renewers by end of next month — before the rival's second-season buzz peaks. Target: outer-district renewal rate back to 78%+ and aggregate attendance recovering to 22,500+ avg by mid-season.

---

## What to notice

- **The reframe politely rejects the chairman's framing.** "Fan engagement strategy" is named and redirected in the opening sentence, before the frameworks run. This is the consultant move — the structured analysis then validates (or refutes) the redirect.
- **The inner-district control row is load-bearing.** If inner-district renewal is also declining sharply, the hypothesis fails — the problem is club-wide (on-pitch, experience, or brand) rather than geographic. That single data point determines whether the targeted intervention or a broader programme is correct.
- **Pareto explicitly names the generic engagement campaign as the 80%.** This is the chairman's preferred response. Naming it as a deprioritized item — with a reason — is the consultant discipline and gives the COO language for the board conversation.
- **The Insight coaches the political move.** "Reject the chairman's framing before the board meeting" — the output tells the COO how to use the finding in the room, not just what the finding is.
- **Continuity is tight.** Outer-district family churn appears in MECE (geographic catchment), branches in the issue tree, drives the hypothesis table's postcode segmentation, anchors the Pareto vital 20%, and becomes the specific retention package in the Insight.
