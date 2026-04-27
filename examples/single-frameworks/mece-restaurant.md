# MECE — Restaurant industry

A standalone run of the `mece-framework` skill on a restaurant problem.

---

## Input (what the user typed)

> I run a 90-seat farm-to-table restaurant in a mid-sized city. Lunch covers have dropped from ~85/day to ~52/day over the past six months — dinner is steady. I want a MECE breakdown of every plausible driver before I start interviewing staff and pulling POS data.

---

## Output (what the skill produced)

- **Local market & demand**
  - Office workers in the surrounding 4 blocks (return-to-office policies, layoffs)
  - Lunch-rush competitor entries (new fast-casual openings within 0.3 mi)
  - Construction or street-access changes affecting walk-in traffic
- **Customer behavior**
  - Frequency drop from existing regulars (loyalty pattern shift)
  - New-customer acquisition slowing (visibility, discovery)
  - Group-size shift (parties of 4+ down vs. solo / pairs)
- **Menu & value perception**
  - Lunch menu price points vs. nearby competition
  - Speed of service expectation gap (lunch needs <45 min)
  - Menu monotony — same items rotating for too long
- **Operations & throughput**
  - Kitchen ticket time during peak window (12:00–1:15)
  - Server-to-table ratio and table turn velocity
  - Take-out / delivery channel performance
- **Marketing & visibility**
  - Google Business profile freshness (photos, reviews, hours)
  - Local social presence and lunch-specific posts
  - Third-party platform (DoorDash, Yelp) ranking and reviews

---

## What to notice

- **5 categories — the upper end of the default range.** A restaurant with both physical and digital surfaces genuinely has more demand-affecting categories than a typical software business. Flexed within the default rather than padding.
- **No "Other" or "External factors" bucket.** Each category is concrete. "Local market & demand" is a real category with three specific sub-factors; it's not a junk drawer.
- **Sub-factors are testable.** Every leaf is something the operator could investigate in a few days — pull POS data on group sizes, walk a 0.3-mi radius to inventory new competition, check Google Business for photo freshness, etc.
- **Lunch-specific framing.** The user said dinner is steady, so categories focus on lunch-specific drivers (office workers, 45-min service expectation, lunch-menu pricing). A generic restaurant categorization would have missed the daypart specificity.
- **Mutually exclusive check.** "New competitor openings" lives in Local market — not in Marketing — because the framework is about what's affecting demand, not how the restaurant responds. A factor only goes in one category.
