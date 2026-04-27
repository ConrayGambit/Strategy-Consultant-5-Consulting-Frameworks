# Hypothesis-Driven — Fintech

A standalone run of the `hypothesis-driven` skill on a fintech operations problem.

---

## Input (what the user typed)

> Our consumer card decline rate jumped from 4.1% to 7.8% over six weeks. Customer complaints are climbing. Engineering swears nothing changed in the auth stack. I suspect the new fraud model deployed in week 1 is over-blocking legitimate transactions — but I need a structured test plan before pointing fingers.

---

## Output (what the skill produced)

**Hypothesis:** The new fraud model deployed in week 1 is the dominant driver of the decline-rate jump, with over-blocking concentrated on legitimate transactions in specific MCC categories or geographies the model wasn't well-calibrated for.

| Variable | Expected (if hypothesis true) | Actual / Required Data |
|---|---|---|
| Decline-rate trend pre vs. post fraud-model deploy | Sharp inflection in week 1, not a gradual climb | Need to plot daily decline rate, weeks -8 to +6 |
| Decline rate by MCC category | Concentrated spike in 1–3 MCCs the model wasn't trained on (e.g., subscription billers, foreign merchants) | Need to segment declines by MCC, before vs. after |
| Decline rate by geography | Higher spike in regions underrepresented in training data (e.g., specific countries or states) | Need to segment declines by issuing region |
| Fraud-model "false positive" rate from rebill attempts | Should be high — legitimate retries that succeed on second attempt indicate over-blocking | Need to query auth logs for declined-then-approved sequences within 5 min |
| Actual fraud-loss rate (control) | If model is over-blocking legitimate txns, fraud loss should NOT have improved — declines went up but losses didn't go down | Pull fraud-loss $/100K txns, weekly, weeks -8 to +6 |
| Customer-complaint mix (control) | If hypothesis right, complaints should cluster around "card declined for legitimate purchase" rather than "fraud not caught" | Pull complaint categorization, weeks 1–6 |
| Auth latency or other tech metrics (control) | Should be flat — if these spiked, tech change is more likely | Engineering already says no auth-stack changes; pull metrics anyway |
| Decline rate on cards NOT scored by new model (control) | Should be flat around 4.1% — would invalidate hypothesis if elevated | Pull decline rate for the 8% of cards still on legacy model |

---

## What to notice

- **One hypothesis, falsifiable.** Not "the fraud model is bad" (too vague) but "the new model is over-blocking, concentrated in specific MCCs or geographies." The geography/MCC modifier is what makes it testable.
- **Four control rows out of eight.** Half the table is designed to invalidate the hypothesis — that's the discipline. Fraud-loss rate, complaint mix, auth latency, and the legacy-model cohort all could prove the hypothesis wrong. If they don't, that's strong evidence the hypothesis is right.
- **Legacy-model cohort is the cleanest control.** A subset of cards is still scored by the old model — if their decline rate is flat at 4.1%, the new model is the cause with very high confidence. If their rate also rose, the hypothesis is dead and the cause is elsewhere.
- **The Required-Data column is actionable.** Each row says exactly what to query and over what period. A data analyst could pick this up and finish the table in 1–2 days.
- **The table doesn't yet have actuals.** That's fine — for a test plan, the third column is "what data is needed and where to get it." Once the data arrives, mark each row ✅ or ❌ and the hypothesis is confirmed or refuted.
- **Sequencing for next steps:** if confirmed, the next framework is `pareto-principle` to isolate which MCCs/regions to retrain first. If refuted, go back to `mece-framework` to enumerate other causes.
