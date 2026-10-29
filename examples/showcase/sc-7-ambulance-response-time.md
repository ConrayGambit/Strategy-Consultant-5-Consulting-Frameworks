# Ambulance response-time compliance — `strategy-consultant-7`

**Skill:** `strategy-consultant-7` — real output produced by a fresh agent reading the SKILL.md and applying it to the problem below (v1.3 consistency pass). No editing.

## Input (what the user typed)

> I'm COO of a 120-vehicle regional ambulance service contracted by three counties. Our response-time compliance (the share of priority-1 calls reached within 8 minutes) has fallen from 91% to 78% over the last five months. Two of the three county contracts have penalty clauses that kick in below 85%, and one comes up for renewal in four months. Call volume is up about 6%. Our board thinks we need to buy 15 more ambulances. What's going on and what should I do?

## Output (what the skill produced)

**Reframe:** A 6% rise in call volume cannot by itself turn 91% compliance into 78% on a 120-vehicle fleet, so the problem is not "we are short 15 ambulances" but "we are producing and losing staffed unit-hours faster than demand is growing" — and with penalties already running and a renewal in four months, the real question is what restores 85%+ inside that window, which new vehicles (9–18 month lead time plus ~130 FTE to staff them) cannot. Do you want me to proceed on the board's framing (fleet size) or on this one (unit-hour recovery within the renewal window)? Proceeding on the reframed framing below.

---

### 1. MECE Categorization

Priority-1 response time = call-received → unit-on-scene. Every driver of the 91% → 78% fall sits in one of five buckets:

- **Demand (what the system must absorb)**
  - Priority-1 call volume (+6% overall; unknown whether concentrated by hour-of-day or by county)
  - Geographic shift of calls (new developments, nursing facilities, highway corridors)
  - Priority mix (share of calls coded P1 by the dispatch center; over-triage inflates the denominator)
- **Supply (staffed unit-hours actually on the road)**
  - Fleet mechanical availability (vehicles in maintenance, awaiting parts, aged chassis)
  - Shift fill rate (vacant paramedic/EMT positions, call-outs, overtime caps, training time)
  - Unit-hours lost to crew breaks, end-of-shift holds, and mandatory rest rules
- **Consumption (unit-hours absorbed per call)**
  - On-scene time
  - Transport time and destination selection
  - Hospital offload / ED wall time
  - Post-call turnaround (restock, decon, paperwork)
- **Deployment and dispatch (where idle units sit and how they are chosen)**
  - Post locations and system-status plan vs. current demand pattern
  - Dispatch rules (closest-unit, level-of-care matching, cross-county mutual aid)
  - Call processing and chute time (call-receipt → unit-en-route)
- **Measurement and contract definition**
  - Clock start/stop definitions per contract (call received vs. dispatched; on-scene vs. patient contact)
  - Exemption clauses (hospital diversion, declared disasters, weather, data errors)
  - Data integrity (CAD/AVL timestamp capture, manual overrides)

---

### 2. Issue Tree

```text
P1 8-minute compliance fell 91% → 78% in 5 months
├── Demand rose faster than it looks
│   ├── Volume +6% overall, but concentrated in peak hours / one county
│   ├── Calls shifted geographically away from current posts
│   └── Dispatch over-triage raised the P1 share of calls
├── Supply of staffed unit-hours fell
│   ├── More vehicles down for maintenance (ageing fleet, parts backlog)
│   ├── Unfilled shifts (vacancies, attrition, overtime caps, burnout)
│   └── Unit-hours lost to breaks / end-of-shift holds / training
├── Unit-hours consumed per call rose  ◄── most likely dominant branch
│   ├── Hospital offload (wall) time lengthened as EDs board patients
│   ├── Longer transports (destination closures, diversion, specialty routing)
│   ├── On-scene time up (acuity, lift assists, protocol changes)
│   └── Turnaround time up (restock, decon, documentation)
├── Deployment and dispatch no longer match demand
│   ├── Post plan not re-optimised since demand pattern shifted
│   ├── Dispatch not sending closest unit (county boundaries, level-of-care rules)
│   └── Call-processing / chute time crept up
└── Measurement and contract mechanics
    ├── Clock definitions differ across the three contracts
    ├── Qualifying exemptions not being claimed (diversion, weather, data errors)
    └── Timestamp capture errors (AVL gaps, manual stops) understating performance
```

---

### 3. 5 Whys

**Starting problem:** Unit-hours consumed per call have risen, so the same staffed fleet now covers fewer calls within 8 minutes.

1. **Why?** Crews are tied up on each call longer — chiefly at the hospital end — so fewer units are available when the next P1 call drops, and the available ones are farther away.
2. **Why?** Receiving EDs are boarding admitted patients and have no beds to accept ambulance patients promptly, so crews wait on the wall; even 15–20 extra minutes on ~300 daily transports is ~75–100 unit-hours a day, the equivalent of 3–4 ambulances parked 24/7.
3. **Why?** There is no agreed offload-time standard or escalation path with the hospitals, so wall time is absorbed silently by the ambulance service rather than triggered as a hospital problem.
4. **Why?** The service has never measured task-time components (chute, scene, transport, offload, turnaround) as managed KPIs — it tracks the compliance percentage and the fleet count, so the leak was invisible until the contract metric broke.
5. **Why?** Capacity is conceived as "number of ambulances" rather than "staffed unit-hours produced minus unit-hours consumed," so nobody owns unit-hour productivity and every shortfall looks like a fleet-size problem — which is exactly how the board is reading it.

**Root cause:** The organisation manages capacity as a vehicle count rather than as unit-hour supply and consumption, so the hospital, staffing, and deployment leaks that actually drove the compliance fall have gone unmeasured, unowned, and unmanaged.

---

### 4. Hypothesis-Driven Problem Solving

**Hypothesis:** At least 70% of the 13-point compliance decline is explained by a fall in effective staffed unit-hours per P1 call — driven by longer hospital offload times and unfilled shifts — not by a shortage of vehicles, so the fleet already contains the capacity needed to return above 85%.

| Variable | Expected (if hypothesis true) | Actual / Required Data |
|---|---|---|
| Vehicles unstaffed at peak (10:00–22:00) | 10+ serviceable ambulances sitting in the yard each peak day because no crew is assigned | Daily peak staffing roster vs. serviceable fleet, last 6 months |
| Shift fill rate | Fallen from ~97% to ≤90%; vacancies and call-outs rising month over month | Scheduling system: posted vs. filled unit-hours by month |
| Hospital offload time (arrive-ED → unit-available) | Up ≥15 minutes per transport over the same 5 months; concentrated at 1–2 EDs | CAD timestamps by destination hospital, monthly medians and 90th percentile |
| Unit-hour utilisation (task hours ÷ staffed hours) | Risen from ~0.40 into the 0.50+ range where response-time tails blow up non-linearly | Monthly UHU by county and hour-of-day |
| Compliance by hour-of-day | Drop concentrated in peak hours and in the county whose EDs board most; overnight compliance roughly unchanged | P1 compliance by hour and county, before vs. after |
| Drive time (en-route → on-scene) for compliant calls | Roughly flat — units that are available still reach scenes as fast as before | CAD en-route-to-arrival medians |
| **Control: fleet mechanical availability** | Flat at ~85–90% serviceable; no spike in out-of-service vehicles | Fleet management out-of-service logs. **If serviceable fleet has dropped sharply, the hypothesis fails and the board's vehicle case strengthens.** |

---

### 5. Pareto Focus (80/20)

> **The vital 20%:** (1) hospital offload/wall time at the one or two EDs that board the most; (2) unfilled peak-hour shifts leaving serviceable ambulances unstaffed; (3) a post/deployment plan that has not been re-cut since demand shifted. These three levers between them can plausibly return 200–300 unit-hours per day — the working equivalent of 8–12 ambulances — without a single new vehicle.

**Actively deprioritized (the 80%):**
- Buying 15 ambulances (~$4–5M capex, ~$10M+/yr in crew cost, 9–18 months to delivery and staffing; it cannot touch the 4-month renewal window and adds nothing if units sit unstaffed)
- Replacing CAD/dispatch software or buying predictive-deployment tools before the basic post plan is fixed
- Shaving call-processing and chute time (tens of seconds; real but small)
- Transport-time and road-network initiatives
- Renegotiating the 8-minute standard itself (counties will read it as weakness mid-decline; revisit only after performance recovers)
- Overnight hours, where compliance is likely still within contract

---

### 6. The "So What?" Test

**Process:** Decomposed P1 response time into demand, staffed-hour supply, per-call consumption, deployment, and measurement; drilled the consumption branch to its root; built a falsifiable test that the fleet is adequate and the shortfall is in unit-hour productivity; isolated the three leaks worth fixing first.

**Result:** A 6% rise in volume is far too small to explain a 13-point compliance fall; the arithmetic only closes if staffed unit-hours have fallen or per-call task time has risen (or both), which points squarely at hospital wall time, unfilled shifts, and a stale deployment plan — and the fleet of 120 vehicles almost certainly already contains the capacity to be above 85%. New ambulances cannot arrive, be staffed, or move the number before the renewal and penalty exposure crystallise.

**Insight:** Take the 15-ambulance purchase off the board agenda and replace it with a 90-day unit-hour recovery program with three named owners and dates:
- *Director of Operations, by day 10:* produce the unit-hour ledger — staffed hours vs. serviceable fleet by hour, task-time components by segment and by hospital, compliance by hour/county — to confirm or kill the hypothesis in one week of data, not months.
- *Chief of EMS / Medical Director, by day 30:* sign offload-time agreements (e.g. 20-minute target, escalation to hospital CNO at 30, cross-county diversion protocol) with the two worst-boarding EDs, and start staging an offload nurse/EMT at the worst one.
- *Director of Operations + HR, by day 30:* fill peak-hour shifts first — peak-shift differentials, a 12-hour power-shift block 10:00–22:00, and overtime rules rewritten so serviceable units are never unstaffed at peak; re-cut the post plan to the current demand map by day 45.
- *COO, by day 14:* review all three contracts for exemption clauses (hospital diversion, declared surge, data errors) and file every qualifying exemption retroactively; open the renewal conversation with the data-backed recovery plan, not with a capital request.

---

### 7. Executive Communication (Pyramid Principle)

**Answer:** Do not buy 15 ambulances; restore 8-minute compliance above 85% within 90 days by recovering the staffed unit-hours we are losing to hospital wall time, unfilled peak shifts, and a stale deployment plan — and bring that recovery, not a capital request, into the county renewal.

1. **The compliance fall is a productivity problem, not a fleet-size problem.**
   - Call volume rose only 6%; a 13-point compliance fall on 120 vehicles only reconciles if staffed hours fell or time-per-call rose.
   - Serviceable vehicles are very likely sitting unstaffed at peak, and crews are losing an estimated 75–100 unit-hours a day on hospital walls — 3–4 ambulances' worth before any other leak.
   - A one-week unit-hour ledger (staffed hours, task-time by segment and hospital, compliance by hour) will confirm or refute this before any money moves.

2. **New ambulances cannot help inside the window that matters.**
   - Chassis lead time is 9–18 months; staffing 15 units 24/7 requires ~130 additional paramedics and EMTs we cannot hire in a market where we already run unfilled shifts.
   - Penalties are accruing now and one contract renews in four months; a $4–5M capex plus $10M+ in annual crew cost would arrive after both decisions are made.
   - Added vehicles that sit unstaffed, or that still queue on the hospital wall, deliver zero compliance improvement.

3. **Three levers return the equivalent of 8–12 ambulances within 90 days.**
   - Hospital offload agreements with the two worst-boarding EDs (20-minute target, escalation at 30, staged offload staff) recover wall time at near-zero cost.
   - Peak-shift differentials and a 10:00–22:00 power-shift block put every serviceable unit on the road when P1 calls actually arrive.
   - Re-cutting the post plan to the current demand map shortens drive time for the units we already have.

4. **The renewal is won on evidence of control, not on capital.**
   - Filing every qualifying contract exemption (diversion, surge, data errors) retroactively reduces penalty exposure immediately.
   - A monthly dashboard of unit-hours, wall time by hospital, and compliance by county gives the counties the transparency that persuades them we own the problem.
   - If the 90-day data shows the fleet genuinely binds after the leaks are fixed, the capital case becomes a precise, defensible number instead of a guess of 15.

## What to notice

- **Scores 8/8 in `--mode 7`.** All seven sections, in order, each in its required visual format.
- **The carry-forward chain is traceable.** The tree flags the dominant branch; the 5 Whys drills exactly that branch; the hypothesis is the 5-Whys root cause stated as a falsifiable claim; the Pareto draws only from factors already named; the Pyramid top-line mirrors the Insight.
- **The root cause is structural, not "people."** "Capacity is managed as a vehicle count, not unit-hours supplied minus consumed" — that is something you can change as a system.
- **The control row is honest.** Fleet mechanical availability is the row that, if it moved, would hand the argument back to the board.
- **Pareto deprioritizes something that matters.** Buying ambulances is on the deprioritized list with the reason (lead time, staffing, window) — the hardest discipline in the framework.
- **One flex to note:** the Insight is four owner/date bullets rather than one. The master allows it (it only requires assignability); the standalone `so-what-test` sub-skill would have asked for one Insight per block.
