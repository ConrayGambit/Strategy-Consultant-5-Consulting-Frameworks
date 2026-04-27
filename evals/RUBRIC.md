# Manual rubric — content quality

The Python scorer (`score.py`) checks structure. This rubric checks substance — the things a regex can't see. Use it for human review or LLM-as-judge passes.

Score each section 0–3:

- **0** — missing or wrong format
- **1** — present but weak (vague, generic, doesn't address the problem)
- **2** — solid (specific, well-structured, no obvious flaws)
- **3** — excellent (sharp, surprising, uncovers the actual move)

Total: 18 (six sections × 3). Anything ≥14 is shippable. ≥16 is genuinely good. <10 means the skill misfired.

---

## 1. MECE Categorization

| Score | Description |
|---|---|
| 3 | Categories are tailored to the specific problem; no overlap; nothing important missing; sub-factors are concrete and investigable |
| 2 | MECE-compliant; categories are relevant; sub-factors are reasonable but a few are generic |
| 1 | Generic People/Process/Tech buckets; some overlap detectable; sub-factors mostly placeholder |
| 0 | Missing, or fails MECE (clear overlap or major gap) |

**What to look for:**
- Could a sub-factor reasonably belong in two categories? → overlap → not MECE.
- Are there relevant factors a smart person would expect but don't appear? → gap → not exhaustive.
- Are sub-factors specific (numbers, named systems) or vague ("operational issues")?

## 2. Issue Tree

| Score | Description |
|---|---|
| 3 | Drills 3+ levels where warranted; leaves are testable in days; branches MECE at each level |
| 2 | 2 levels deep; mostly MECE; leaves are mostly testable |
| 1 | Tree structure but flat (1 level); leaves are vague |
| 0 | Missing, or no tree characters used |

**What to look for:**
- Does each leaf describe something a person could investigate this week?
- Does the depth vary by branch (sign of judgment) or is everything uniformly 2 levels?
- Are nodes short (3–8 words) or rambling sentences?

## 3. Hypothesis-Driven

| Score | Description |
|---|---|
| 3 | Hypothesis is sharp and falsifiable; table has at least one control row; rows are diagnostic; specific data sources or numbers cited |
| 2 | Hypothesis testable; control rows present but weak; rows are reasonable |
| 1 | Hypothesis vague ("we have a problem"); no control rows; rows are restatements of hypothesis |
| 0 | Missing, or no Markdown table |

**What to look for:**
- Could the hypothesis be proven WRONG by data? If not, it's not falsifiable.
- Is at least one row designed to invalidate the hypothesis? Examples: a control segment, a baseline that should be flat, a metric that would move opposite if the hypothesis is wrong.
- Does the third column point to specific data sources ("CRM stage-time data segmented by ACV band") vs. generic ("look at the data")?

## 4. Pareto Focus

| Score | Description |
|---|---|
| 3 | Vital 20% is 1–4 specific items; deprioritized list contains things that genuinely matter (not just filler); explicit commitment language |
| 2 | Vital 20% is reasonable; deprioritization explicit but list is half-filler |
| 1 | "Vital 20%" lists 8+ items (no real prioritization); deprioritized list is all generic / obvious |
| 0 | Missing, or no blockquote; no deprioritization |

**What to look for:**
- Does the vital 20% name SPECIFIC things (named accounts, specific causes) or categories?
- Is the deprioritized list painful to write? (e.g., legitimate concerns the team won't be able to address yet) That's the discipline.
- Is there hedging ("we could consider...") or commitment ("we will not...")?

## 5. "So What?" Test

| Score | Description |
|---|---|
| 3 | Process specific; Result has numbers and rules out alternatives; Insight is assignable to a named person with deadline + target |
| 2 | All three sections present; Insight has owner OR deadline but not both |
| 1 | Insight is a slogan ("we should focus on retention") or restates the Result |
| 0 | Missing, or no labeled sections |

**What to look for:**
- Could you copy the Insight into a Slack DM that says "@person, please own this by [date]" and they would know what to do? If not, it's not assignable.
- Does the Insight name a target metric or quantitative goal?
- Does the Result have numbers that support the Insight, or is it qualitative hand-waving?

## 6. Reframe / overall judgment

| Score | Description |
|---|---|
| 3 | Output opens with a sharp reframe (when warranted); sequencing is logical; ends decisively |
| 2 | No reframe even when one is warranted, but otherwise solid; clean sequencing |
| 1 | Goes through the motions without judgment; reads like template-fill |
| 0 | Major errors (wrong framework structure, hallucinations, contradictions) |

**What to look for:**
- Did the model push back on the user's framing where appropriate? (Not always required — only when the framing is questionable.)
- Are the five sections internally consistent? E.g., does the Insight follow from the Pareto, which follows from the Hypothesis, etc.?
- Any factual claims that look invented? (Usually a sign of hallucination — flag for verification.)

---

## Score sheet

```
Problem: ____________________________________________

  1. MECE              ___/3   _______________________________
  2. Issue Tree        ___/3   _______________________________
  3. Hypothesis        ___/3   _______________________________
  4. Pareto            ___/3   _______________________________
  5. So What?          ___/3   _______________________________
  6. Reframe / overall ___/3   _______________________________
                              ______
  Total                 ___/18

  Verdict:  [ ] Excellent (≥16)
            [ ] Shippable (14–15)
            [ ] Needs revision (10–13)
            [ ] Skill misfired — investigate (<10)
```
