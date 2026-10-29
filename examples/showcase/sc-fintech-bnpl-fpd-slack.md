# BNPL first-payment default spike — `sc-fintech` in Slack mode

**Skill:** `sc-fintech` — real output produced by a fresh agent reading the SKILL.md and applying it to the problem below (v1.3 consistency pass). No editing.

## Input (what the user typed)

> I run risk at a mid-size BNPL lender (about $900M annual originations). Over the last two months our first-payment default rate on new loans has gone from 2.1% to 3.9%. Approval rate is roughly unchanged at 61%. We shipped a new underwriting model (v4) nine weeks ago and also launched a partnership with a large electronics retailer seven weeks ago. The CFO wants to pull the new model. I need to post this analysis in Slack to the exec channel, so please format it for Slack.

## Output (what the skill produced)

**Reframe:** Before you pull v4 — the question as posed is "did the new model break," but the timing fits a different mechanism at least as well: the electronics-retailer launch (week 7) shifted your originated population toward a higher-ticket, thinner-file, fraud-attractive merchant cohort, and a composition shift at the same approval rate would move first-payment default exactly this way without v4 having mis-scored anyone. Do you want to proceed on the original framing (v4 is the cause) or the reframed one (merchant-mix shift vs. model, decided by cohort cut)? Proceeding below on the reframed framing.

### 1. MECE Categorization

- **Customer & credit risk**
  - v4 score calibration drift (PD by score band vs. v3 backtest)
  - Underwriting cutoff / swap-set changes at the 61% approval line
  - Applicant composition shift (new-to-file, thin-file, income band, age of bureau file)
- **Merchant & channel mix**
  - Electronics-retailer share of originations and its standalone FPD
  - Average ticket, term length, and down-payment mix by merchant
  - Legacy-merchant FPD trend in isolation
- **Fraud & risk controls**
  - First-party fraud / never-pay (synthetic ID, bust-out) concentrated at high-resale-value SKUs
  - Third-party fraud: device, velocity, and ID-verification rule coverage on the new integration
  - Rule-set differences between the retailer's checkout path and existing paths
- **Product & UX / integration**
  - Retailer-side prequal or soft-pull flow bypassing steps in the standard funnel
  - Autopay enrollment and payment-method capture at checkout
  - First-installment timing relative to delivery / return window
- **Operations & collections**
  - First-payment reminder cadence and dunning on the new volume
  - Payment-processor retry / decline-reason-code behavior on the retailer cohort
  - Returns and refund reversals being booked as missed first payments
- **External & macro**
  - Seasonal electronics demand and promotional financing spikes
  - Macro delinquency drift in comparable unsecured consumer credit

### 2. Issue Tree

```text
- First-payment default rose 2.1% -> 3.9% over two months at a flat 61% approval rate
  - Customer & credit risk (v4 model)
    - Does v4 PD-by-score-band match v3's realized FPD on the same applicants (swap-set analysis)?
    - Did the 61% line move from "who" we approve even if "how many" is unchanged?
    - Did thin-file / new-to-credit share of approvals rise after v4 cut-over?
  - Merchant & channel mix (electronics retailer)
    - What share of weekly originations is the retailer, and what is its standalone FPD?
    - Is legacy-merchant FPD flat (2.1%) when the retailer is excluded?
    - Does average ticket / term on the retailer cohort exceed the book average?
  - Fraud & risk controls
    - Is never-pay (zero payments ever) rising faster than late-first-payment?
    - Are device / ID / velocity rules enabled on the retailer checkout path?
    - Are defaults concentrated in resellable SKUs (phones, consoles, GPUs)?
  - Product & integration
    - Does the retailer flow skip autopay or payment-method verification?
    - Does the first installment land before delivery or inside the return window?
  - Operations & collections
    - Did first-payment dunning capacity keep pace with the volume step-up?
    - Are refund / return reversals being coded as missed first payments?
  - External
    - Does comparable unsecured consumer FPD show a similar two-month rise?
```

### 3. Hypothesis-Driven Problem Solving

**Hypothesis:** The FPD rise is driven by the electronics-retailer cohort (higher ticket, thinner file, weaker fraud controls on the new checkout path), not by v4 mis-scoring; excluding the retailer, FPD on v4-scored loans is within 30 bps of the 2.1% baseline.

| Variable | Expected (if hypothesis true) | Actual / Required Data |
|---|---|---|
| Legacy-merchant FPD, v4-scored, wks 1-9 | Flat at ~2.1-2.4% | Ledger: FPD by merchant x score-model flag |
| Retailer-cohort standalone FPD | 6-9%, driving the blended lift | Ledger: FPD for retailer merchant ID, wks 3-9 |
| v4 vs v3 FPD on matched swap-set | No material gap by score band | Decision-engine logs: dual-scored population |
| Never-pay share of FPD (0 payments) | Rising, concentrated in retailer cohort | Collections: zero-payment flag by merchant |
| Fraud rule hits on retailer path | Lower rule coverage / fewer step-ups | Rule engine: rules fired per app by channel |
| Control: v4-scored loans weeks 1-2 (pre-retailer) | FPD ~2.1%, no step-up at v4 cut-over | Ledger: FPD for wk 1-2 v4 originations |
| Control: v3-scored retailer apps (if any champion/challenger) | Same elevated FPD as v4-scored retailer apps | Decision-engine logs: model version by app |

### 4. Pareto Focus (80/20)

> **The vital 20%:** (1) The merchant-level FPD cut — retailer cohort vs. legacy book; (2) the v4 pre-retailer control window (weeks 1-2); (3) never-pay share and fraud-rule coverage on the retailer checkout path.

**Actively deprioritized (the 80%):**
- Rolling back v4 before the cohort cut is done
- A blanket fraud-rule tightening across all merchants
- Full v4 model re-validation / re-build
- Macro and seasonality benchmarking beyond a single comparison series
- Collections-capacity and dunning-cadence studies
- Returns / refund coding cleanup (check it, but it will not explain 180 bps)

### 5. The "So What?" Test

**Process:** Decomposed the 2.1% -> 3.9% first-payment default rise across credit model, merchant mix, fraud controls, integration, ops, and macro; built a hypothesis that the electronics-retailer cohort — not v4 — carries the lift, with two control cuts (v4 pre-retailer weeks, and any v3-scored retailer apps) that would falsify it.

**Result:** Approval rate is flat at 61%, so the "how many" did not change — the "who" did. v4 cut over two weeks before the retailer launched, giving a clean control window; if FPD in that window sits near 2.1%, the model is exonerated. On $900M annual originations (~$75M/month), 180 bps of incremental FPD is roughly $1.35M/month of new first-payment losses — the CFO is right to escalate, but pulling v4 does not touch the cause if the lift is merchant-driven, and it would cost you the swap-set benefit v4 was shipped to deliver.

**Insight:** Do not pull v4 this week. Head of Credit Risk owns a three-cut readout by Friday: (a) FPD by merchant x score-model flag, weekly, wks 1-9; (b) v4-only, pre-retailer FPD as the control; (c) never-pay share and fraud-rule fire-rate on the retailer path vs. legacy paths. If the retailer cohort carries the lift, Head of Fraud ships a retailer-specific control package the following Monday — ID / device step-up, velocity caps, and a ticket-size or SKU-based cutoff — ahead of month-end loss accrual and the next board risk review. If instead the v4 control window also shows the step-up, revert to v3 the same day and bring the swap-set analysis to the exec channel.

## What to notice

- **Slack mode worked.** The user named Slack as the destination, so the issue tree is an indented-dash tree with zero box-drawing characters — and the scorer still passes it 6/6 via the fallback path.
- **The reframe is the whole analysis.** "Pull v4" vs. "the retailer cohort changed who you approve at the same 61%" — stated in one sentence, then proceeded. Flat approval rate is the clue the skill picked up on.
- **Two control rows that could kill the hypothesis.** v4-scored loans in the two weeks before the retailer launched is a clean natural experiment; the skill found it rather than inventing data.
- **Fintech vocabulary and cadence.** FPD, never-pay, swap-set, BIN/SKU fraud concentration, month-end loss accrual as the deadline — reads like a risk lead wrote it.
- **The Insight carries a kill switch.** It commits to *not* pulling v4, but names the exact result that would reverse that call the same day.
