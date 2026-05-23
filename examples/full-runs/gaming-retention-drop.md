# Live-service D7 retention drop after v3.1 — Mobile gaming

## Input (what the user typed)

> I run product at a live-service mobile RPG (5M MAU, 18-month-old). Our D7 retention dropped from 24% to 17% after the v3.1 update (shipped 6 weeks ago) — the biggest patch in a year. ARPDAU is down 12% too. The CEO wants to roll back v3.1; the team wants to ship more content. Help me figure out what's actually broken.

---

## Output (what the skill produced)

Rolling back v3.1 in full and shipping more content are both blunt instruments — the right move is almost certainly a surgical rollback of the 1–2 specific changes that broke a specific session or step, not a full revert or a content sprint that buries the problem. Below is the structured diagnosis.

---

### 1. MECE Categorization

- **Onboarding & first-session experience**
  - Tutorial completion rate and drop-off step
  - Time-to-first meaningful reward (first clear, first gacha pull, first PvP win)
  - New-player difficulty curve after v3.1 rebalancing
- **Core game loop**
  - Session length and sessions-per-day trending vs. pre-v3.1
  - Level/stage difficulty spike at specific progression checkpoints
  - Energy/stamina system pacing — refill rate and cap changes
  - Failure rate at key choke-point levels (quit vs. retry behavior)
- **Monetization & paywall**
  - First paywall placement (at what level/event does the hard stop appear?)
  - IAP conversion rate and average order value pre/post v3.1
  - Gacha or loot-box step — pull rate perception changes
- **Content cadence & meta**
  - Live-ops event calendar gap post-v3.1 ship
  - Power creep from new units/gear introduced in v3.1
  - Guild/social feature changes affecting cooperative play
- **Server & technical performance**
  - Crash rate and ANR (Application Not Responding) frequency by device tier
  - Session start latency and load time changes vs. pre-patch
  - Network error rate during peak hours
- **Cohort mix**
  - New vs. returning player composition shift (acquisition spike post-patch?)
  - Veteran player (D30+) retention vs. new player (D0–D7) retention — separated
  - Platform split (iOS vs. Android) performance divergence

---

### 2. Issue Tree

```text
D7 retention: 24% → 17% (-7pp); ARPDAU -12% post v3.1
├── Onboarding & first-session
│   ├── Tutorial drop-off rate up if v3.1 changed early difficulty curve
│   └── Time-to-first-reward extended (rebalanced progression pacing)
├── Core game loop
│   ├── Difficulty spike at specific stage (likely mid-funnel checkpoint)
│   │   ├── Stage failure rate up → quit rate up at that node
│   │   └── Retry cost (energy spend) deterring continued play
│   ├── Energy/stamina pacing changed — players hitting cap earlier
│   └── Session length declining → daily sessions declining → D7 dropout
├── Monetization & paywall
│   ├── First hard paywall moved earlier in v3.1 (common rebalance side-effect)
│   ├── IAP conversion rate down (supports ARPDAU decline)
│   └── Gacha perceived as less rewarding (pull-rate or drop-rate change in v3.1)
├── Content & meta
│   ├── Live-ops event gap — no major event in first 3 weeks post-v3.1
│   └── New v3.1 units perceived as P2W, reducing free-player engagement
├── Technical / performance
│   ├── Crash rate delta post-patch (especially older Android devices)
│   └── Load time regression on v3.1 assets
└── Cohort mix
    ├── New-player D7 retention (fresh installs since v3.1) vs. pre-patch new players
    └── Veteran-cohort D7 (players returning after dormancy) — should be unaffected if loop-level
```

---

### 3. Hypothesis-Driven Problem Solving

**Hypothesis:** The D7 retention drop is driven primarily by a difficulty or paywall step introduced or shifted in v3.1 that hits new players specifically — veterans are largely unaffected — meaning a surgical rollback or hotfix of that specific mechanic (not a full v3.1 revert or content push) will recover the majority of the lost retention.

| Variable | Expected (if hypothesis true) | Actual / Required Data |
|---|---|---|
| New-player D7 retention (post-v3.1 installs) | Should show the full -7pp drop | Segment cohort by install date before/after v3.1 ship date; pull D7 by cohort |
| Veteran-player D7 retention (control) | Should be flat or minimally affected — veterans have progression buffer | Pull D7 for players with D30+ tenure at time of patch; if also down, loop-level problem not new-player-specific |
| Stage/level funnel drop-off map | Should show a new spike at a specific stage or paywall gate that wasn't there pre-v3.1 | Pull level-completion funnel from analytics; compare pre/post patch at each stage |
| Session failure rate at choke-point levels | Elevated quit rate (not retry) at the specific node | Segment quit vs. retry events at stages 20–40 (likely mid-funnel); compare pre/post |
| IAP conversion rate by level band | Conversion decline concentrated at players who hit the suspected paywall stage | Pull IAP conversion by player level; identify drop-off level band |
| Crash/ANR rate (control) | Should be flat if this is a design problem, not a technical one | Pull crash reporting; if crash rate is flat, technical cause ruled out |
| Content-event participation rate | If live-ops gap is the cause, D7 should recover when next event launches | Cross-reference D7 trend against event calendar; no recovery yet = event gap isn't root cause |

---

### 4. Pareto Focus (80/20)

> **The vital 20%:** One or two specific v3.1 changes are almost certainly responsible for the majority of the D7 drop: either (a) a difficulty spike at a specific mid-funnel stage that wasn't present before (driving quit-not-retry behavior at that node) or (b) a paywall placement that moved 5–10 levels earlier in the progression (cutting off free players before they're invested). Both are identifiable in the level-funnel analytics within 48 hours and fixable via a targeted hotfix or config change — not a full rollback.

**Actively deprioritized (the 80%):**
- Full v3.1 rollback (would also revert improvements and content players are using; loses 6 weeks of work)
- Shipping more content (doesn't fix the broken step; buries it under more progression that new players never reach)
- Lowering IAP prices system-wide (treats ARPDAU symptom, not the retention root cause)
- Crash rate investigation (control row: if veteran retention is flat, it's not a technical issue)
- Live-ops event calendar changes (D7 drop pre-dates any event gap and affects cohorts with no event exposure)
- Full game rebalancing (scope too broad; fix the specific node, not the whole loop)

---

### 5. The "So What?" Test

**Process:** Decomposed the D7 and ARPDAU decline into six MECE domains; traced the most likely cause in the issue tree to a new-player-specific difficulty or paywall step introduced in v3.1; tested that hypothesis against cohort segmentation (new vs. veteran), level-funnel data, IAP conversion by level band, and two control rows (veteran D7, crash rate) designed to rule out systemic or technical causes; applied Pareto to identify the surgical fix over the blunt-instrument alternatives.

**Result:** The veteran-cohort D7 control row is the critical diagnostic: if veteran retention is flat post-v3.1, this is a new-player onboarding or early-progression problem — not a systemic loop or content problem — and the fix is targeted. The level-funnel drop-off map will identify the specific stage within 48 hours of pulling the data. ARPDAU declining in parallel with D7 suggests the broken step is also the first monetization touchpoint — early paywall placement is the lead suspect.

**Insight:** Don't roll back v3.1 in full and don't ship a content sprint. Pull the D7 cohort split (new vs. veteran) and the level-funnel drop-off map before the next live-ops weekly review (owner: Lead Data Analyst, due within 48 hours). If veteran D7 is flat and the funnel shows a new spike at a specific stage, that stage is the hotfix target — adjust difficulty config or paywall placement for that node only, ship as a hotfix within the current weekly window (owner: Lead Game Designer + Engineering). Present the CEO with the surgical-rollback plan and the specific change being reverted — not a binary "roll back everything vs. ship content" choice. Target: D7 recovery to 21%+ within 2 weeks of hotfix; if not recovered, escalate to broader v3.1 audit.

---

## What to notice

- **The surgical-rollback reframe.** Both the CEO's ask (full rollback) and the team's ask (more content) are named and rejected before the analysis runs. The output lands on a third option — hotfix the specific broken node — that neither side proposed.
- **The veteran-cohort control row is load-bearing.** If veterans are also churning at D7, the hypothesis fails and the problem is systemic, not new-player-specific. That single data point changes the entire intervention.
- **Continuity is tight.** The level-funnel spike appears in MECE (core game loop), branches in the issue tree, drives three hypothesis table rows, anchors the Pareto vital 20%, and becomes the specific hotfix instruction in the Insight.
- **Pareto explicitly deprioritizes "ship more content."** This is the most common over-reaction in live-service games. Naming it as the 80% — with a reason — is the discipline.
- **The Insight gives the CEO a reframe, not just an answer.** "Present the CEO with the surgical-rollback plan" — the output coaches how to use the finding, not just what the finding is.
