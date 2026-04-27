# Strategy Consultant — 5 Consulting Frameworks
<img width="1082" height="607" alt="image" src="https://github.com/user-attachments/assets/9b56e3bf-f049-4411-a005-00fa963c038f" />

> *Repo: `Strategy-Consultant-5-Consulting-Frameworks`*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Made for Claude](https://img.shields.io/badge/Made%20for-Claude-8A4FFF)](https://claude.com)
[![Skills format](https://img.shields.io/badge/format-Anthropic%20Skills-orange)](https://www.anthropic.com)
[![YouTube](https://img.shields.io/badge/YouTube-ConrayGambit-FF0000?logo=youtube&logoColor=white)](https://youtube.com/@conraygambit)

> Turn any LLM into a Tier-1 strategy consultant who breaks down complex business problems on a whiteboard — MECE, issue trees, hypothesis tests, the Pareto principle, and the "So What?" test, in sequence, every time.

The idea: most LLMs answer business questions in flowing prose that sounds smart but doesn't actually structure your thinking. This repo gives Claude (or any LLM) a strict visual contract: every business problem produces exactly five sections — a MECE breakdown, an ASCII issue tree, a hypothesis-test table, a Pareto blockquote, and a Process/Result/Insight closer. Whiteboard-style, every time. The frameworks aren't new — they're standard McKinsey/BCG/Bain practice — but baking them into a deterministic skill format means you stop getting fluffy answers and start getting consultant-grade ones.

The repo ships several flavors. A **sequential** master that works in any LLM (Claude.ai, ChatGPT, Gemini, anywhere you can paste a system prompt). A **sub-agent** master for Claude Code or Cowork environments that support parallel agent delegation. A **7-framework variant** that adds 5 Whys and Pyramid Principle on top of the canonical five for high-stakes work. And three **industry packs** (SaaS, retail, healthcare) with industry-aware vocabulary and root-cause priors. See the Master Variants table below for which to pick.

---

## What you give it, what it gives back

You give it: *"Our SaaS churn jumped 4 points last quarter and nobody knows why."*

It gives you back, in one response:

1. **MECE breakdown** — every plausible churn driver, organized so nothing overlaps and nothing is missed
2. **Issue Tree** — an ASCII tree decomposing churn into testable root causes
3. **Hypothesis Test** — a table comparing what you'd expect to see if your hypothesis is true vs. what the data actually shows (with at least one control row designed to invalidate the hypothesis)
4. **Pareto Focus** — the 20% of drivers responsible for 80% of the churn, called out in a blockquote, with the deprioritized 80% explicitly named
5. **So What?** — Process / Result / Insight, with an action specific enough to assign to a person with a deadline

**See it in action.** Browse [`examples/showcase/`](./examples/showcase/) for 10 real outputs across industries — every one produced by an agent reading a SKILL.md and applying it to a fresh business problem. Or read the canonical end-to-end walk-through: [`examples/example-analysis.md`](./examples/example-analysis.md).

---

## Quick start

### Claude Code / Cowork on macOS or Linux

```bash
git clone https://github.com/ConrayGambit/Strategy-Consultant-5-Consulting-Frameworks.git
cd Strategy-Consultant-5-Consulting-Frameworks
mkdir -p ~/.claude/skills
cp -r skills/* ~/.claude/skills/
```

Restart Claude Code. Try `/strategy-consultant` and paste in a business problem.

### Claude Code / Cowork on Windows (PowerShell)

```powershell
git clone https://github.com/ConrayGambit/Strategy-Consultant-5-Consulting-Frameworks.git
cd Strategy-Consultant-5-Consulting-Frameworks
$skillsPath = "$env:USERPROFILE\.claude\skills"
if (-not (Test-Path $skillsPath)) { New-Item -ItemType Directory -Path $skillsPath -Force | Out-Null }
Copy-Item -Path .\skills\* -Destination $skillsPath -Recurse -Force
```

### Anywhere else (Claude.ai, ChatGPT, Gemini, local models)

Open [`prompts/strategy-consultant.md`](./prompts/strategy-consultant.md), copy the whole file, paste into your LLM as a system prompt or first message, then ask your business question.

For Custom GPTs and Claude Projects, paste it into the "Instructions" field.

Full per-platform install (including Cowork on Windows, ChatGPT Custom GPT setup, etc.) is in [INSTALLATION.md](./INSTALLATION.md).

After installing, verify everything works using [TESTING.md](./TESTING.md) — it includes a canonical test prompt and pass criteria for each install path.

---

## Repository layout

```
Strategy-Consultant-5-Consulting-Frameworks/
├── skills/                                # Anthropic Skills format (SKILL.md + frontmatter)
│   ├── strategy-consultant/               # Master — 5 frameworks, sequential
│   ├── strategy-consultant-agents/        # Master — 5 frameworks, parallel sub-agents
│   ├── strategy-consultant-7/             # Master — 7 frameworks (adds 5 Whys + Pyramid Principle)
│   ├── mece-framework/                    # Sub-skill: MECE
│   ├── issue-trees/                       # Sub-skill: Issue Trees
│   ├── hypothesis-driven/                 # Sub-skill: Hypothesis-Driven
│   ├── pareto-principle/                  # Sub-skill: Pareto / 80-20
│   ├── so-what-test/                      # Sub-skill: So What?
│   ├── five-whys/                         # Sub-skill: 5 Whys
│   └── pyramid-principle/                 # Sub-skill: Pyramid Principle
├── industry-packs/                        # Industry-tailored master variants
│   ├── saas/SKILL.md                      # sc-saas
│   ├── retail/SKILL.md                    # sc-retail
│   └── healthcare/SKILL.md                # sc-healthcare
├── prompts/                               # LLM-agnostic plain prompts (one per skill)
├── examples/
│   ├── example-analysis.md                # Featured walk-through
│   ├── full-runs/                         # 5 industries: retail, nonprofit, manufacturing, government, logistics
│   ├── single-frameworks/                 # 5 standalone-skill demos in different industries
│   └── showcase/                          # 10 real outputs from end-to-end skill testing
├── evals/                                 # Automated structural scorer + manual rubric
│   ├── score.py                           # Python scorer (no dependencies)
│   ├── RUBRIC.md                          # Manual content-quality rubric
│   └── fixtures/                          # Known-bad samples for regression testing
├── INSTALLATION.md                        # Per-platform install guide
├── TESTING.md                             # Canonical test prompt + per-platform pass criteria
├── CONTRIBUTING.md                        # How to add frameworks, examples, industry packs
├── GITHUB-SETUP.md                        # Notes for forkers
├── LICENSE                                # MIT
└── README.md
```

---

## How it works

The repo only really has three things that matter:

- **`skills/<skill-name>/SKILL.md`** — Anthropic Skills format with YAML frontmatter (name, description) and the actual instructions in markdown. Claude Code and Cowork load these automatically.
- **`prompts/<skill-name>.md`** — Same instructions without the frontmatter. For pasting into ChatGPT, Claude.ai, Gemini, custom GPTs, etc.
- **`examples/`** — Real input/output pairs you can read to calibrate what good output looks like.

The three master skills (`strategy-consultant`, `strategy-consultant-agents`, and `strategy-consultant-7`) are self-contained — they walk through all five (or all seven) frameworks in one response. The seven sub-skills (`mece-framework`, `issue-trees`, `hypothesis-driven`, `pareto-principle`, `so-what-test`, `five-whys`, `pyramid-principle`) are alternatives for when you only want one framework. The industry packs (`sc-saas`, `sc-retail`, `sc-healthcare`) are alternative masters with industry-aware MECE defaults and vocabulary.

---

## Master variants

The repo ships several master skills. Pick the one that fits your need:

| Variant | Frameworks | When to use |
|---|---|---|
| **`strategy-consultant`** (sequential) | 5 — MECE, Issue Tree, Hypothesis, Pareto, So What? | Default. Works in any LLM. One pass, single response. |
| **`strategy-consultant-agents`** (sub-agents) | 5 — same | Claude Code / Cowork only. Delegates each framework to a parallel sub-agent. Best for high-stakes complex problems. |
| **`strategy-consultant-7`** | 7 — adds 5 Whys + Pyramid Principle | High-stakes work that needs both deeper root-cause drilling AND executive-ready communication structure. |
| **`sc-saas`** ([details](./industry-packs/saas/SKILL.md)) | 5 — same | SaaS-specific problems. Industry-aware MECE defaults (NRR, churn, pipeline), native vocabulary, common root-cause priors. |
| **`sc-retail`** ([details](./industry-packs/retail/SKILL.md)) | 5 — same | Retail / hospitality / multi-unit problems. Comp store, foot traffic, basket, mix. |
| **`sc-healthcare`** ([details](./industry-packs/healthcare/SKILL.md)) | 5 — same | Hospital ops / clinical operations. Readmissions, ALOS, throughput, access. |

All variants produce the same output structure (visual contract). They differ in (a) depth of analysis, (b) industry vocabulary, and (c) common root-cause priors.

---

## The five frameworks

| # | Framework | What it does | Visual format |
|---|---|---|---|
| 1 | **MECE** | Categorize factors with no overlap, no gaps | Nested bullet points |
| 2 | **Issue Trees** | Decompose the problem into root causes | ASCII tree |
| 3 | **Hypothesis-Driven** | State a falsifiable hypothesis, design the test | Markdown table (Expected vs. Actual) |
| 4 | **Pareto Principle** | Isolate the 20% of inputs driving 80% of results | Blockquote + deprioritized list |
| 5 | **"So What?" Test** | Translate findings into an actionable insight | Process / Result / Insight |

Each framework is also a standalone skill — invoke `/mece-framework` on its own when that's all you need. The 7-framework variant adds **5 Whys** (drilled root cause) and **Pyramid Principle** (executive-ready communication) as additional standalone sub-skills.

---

## Who is this for?

- **Founders & operators** prepping for board meetings or investor updates who need to think like a consultant without hiring one.
- **PMs and analysts** structuring messy investigations (churn spikes, conversion drops, support backlogs) before they become slide decks.
- **Strategy & consulting professionals** using it as scaffolding for client deliverables — apply the frameworks fast, then layer in real research.
- **Engineering managers and TPMs** running incident retros or capacity reviews where loose thinking is the enemy.
- **MBA students & interview candidates** — mastering these five frameworks is literally the case-interview job.
- **Customer success leaders** doing churn analysis or QBR prep.
- **Sales leaders** running pipeline reviews — the hypothesis test is especially good for "why are deals stalling?"

Unifying thread: **anyone who needs structured business thinking on demand and doesn't want every problem to dissolve into prose**.

---

## Design choices

A few decisions worth surfacing — in case you're forking and wondering why things are the way they are:

- **Visual structure is non-negotiable.** Every framework has a strict output format (nested bullets, ASCII tree, table, blockquote, three labeled sections). Prose-only answers are a failure mode. This is the entire value of the skill.
- **Five frameworks, applied in order.** MECE → Issue Tree → Hypothesis → Pareto → So What is the canonical sequence. Skipping or reordering breaks the logic chain. The 7-framework variant adds 5 Whys (between Issue Tree and Hypothesis) and Pyramid Principle (after So What) — also applied in strict order.
- **Defaults are flexible, MECE is not.** Sub-skills say "3–6 categories" or "4–7 variables" — but tell the model to flex with judgment. The one rule that doesn't flex: categories must be Mutually Exclusive and Collectively Exhaustive. That's the foundation; everything else is style.
- **Three masters, not one.** Sequential works everywhere. Sub-agent works only in agent-capable environments. The 7-framework variant is for high-stakes work. Shipping all three lets users pick without losing reach.
- **Dual format (skills + plain prompts).** Anthropic Skills format works in Claude Code/Cowork. Plain prompts work in everything else. Same content, two distributions.
- **Reframe-the-question is built in.** Sometimes the user's stated problem isn't the real problem. The masters ask one reframe question max before applying the frameworks — pushing back is part of the consultant role.

---

## Roadmap

Shipped in v1.x:

- [x] **5-framework master** (sequential + sub-agent) ✅
- [x] **7 sub-skills**, each invokable standalone (5 canonical + 5 Whys + Pyramid Principle) ✅
- [x] **7-framework variant** — adds 5 Whys (between Issue Tree and Hypothesis) and Pyramid Principle (after So What?) for high-stakes work. See [`skills/strategy-consultant-7/`](./skills/strategy-consultant-7/SKILL.md). ✅
- [x] **Industry packs** — [`sc-saas`](./industry-packs/saas/SKILL.md), [`sc-retail`](./industry-packs/retail/SKILL.md), [`sc-healthcare`](./industry-packs/healthcare/SKILL.md) with industry-specific MECE defaults, vocabulary, and root-cause priors. ✅
- [x] **Eval suite** — automated structural scorer + content rubric in [`evals/`](./evals/). Run `python evals/score.py < output.txt`. ✅
- [x] **21 example files** — 1 featured walk-through, 5 full-run examples (retail, nonprofit, manufacturing, government, logistics), 5 single-framework demos in different industries, and 10 real outputs from end-to-end skill testing in [`examples/showcase/`](./examples/showcase/). ✅
- [x] **Hero illustration** at the top of the README. ✅

Still in flight:

- [ ] **Slack-formatted output mode** — same structure but using indented dashes instead of box-drawing chars (already documented in `issue-trees`; a flag would be cleaner).
- [ ] **LLM-as-judge eval mode** — content-quality scoring against the rubric, not just structural checks.
- [ ] **More industry packs** — fintech, manufacturing, nonprofit, government, edtech.
- [ ] **More example industries** — biotech, gaming, sports, agriculture.
- [ ] **CI integration** — GitHub Action that scores output samples on every PR.
- [ ] **Video walkthrough** on the [ConrayGambit YouTube channel](https://youtube.com/@conraygambit).

If you have ideas, open an issue or DM `@ConrayGambit`.

---

## Contributing

PRs welcome. The frameworks themselves are well-established consulting practice — the value of this repo is in the strict formatting contracts. If you propose changes, please preserve the visual output structure.

To add a new framework:

1. Create `skills/<your-framework>/SKILL.md` with frontmatter
2. Create `prompts/<your-framework>.md` with the same content minus frontmatter
3. Update the master skills to include the new step
4. Add an entry to the framework table above

To add an example:

1. Pick an industry not yet represented (see `examples/README.md` for what's there).
2. Drop a file into `examples/full-runs/` or `examples/single-frameworks/` with the input/output structure used by the existing examples.
3. Update `examples/README.md` to link to it.

See [CONTRIBUTING.md](./CONTRIBUTING.md) for full guidelines.

---

## License

MIT — see [LICENSE](./LICENSE). Use freely, modify freely, ship freely.

---

## Credits & Acknowledgment

> **Acknowledgment:** The core frameworks and structural concepts in this skill are directly adapted from the teachings of **Analyst Academy** on YouTube.
>
> *Source reference:* [5 Consulting Frameworks to Solve Any Problem](https://www.youtube.com/watch?v=uCmTk06aM70)

The five frameworks themselves (MECE, Issue Trees, Hypothesis-Driven Problem Solving, Pareto Principle, "So What?" test) are classic management consulting practice (McKinsey, BCG, Bain). Analyst Academy's video crystallized the *visual output contract* — the idea that each framework should produce a specific, repeatable visual artifact (nested bullets, ASCII tree, comparison table, blockquote, three labeled sections). This repo packages that contract as Claude Skills + LLM-agnostic prompts.

The two additional frameworks in the 7-framework variant — **5 Whys** (Sakichi Toyoda / Toyota Production System) and **Pyramid Principle** (Barbara Minto / McKinsey) — are also well-established practice, packaged with the same visual-contract treatment.

---

## About the packager

Built and packaged by **Nathaniel Bricknell** ([@ConrayGambit](https://github.com/ConrayGambit) on GitHub).

For walkthroughs, demos, and more AI/LLM tooling, check out the [**ConrayGambit**](https://youtube.com/@conraygambit) YouTube channel — including a video walking through this repo and giving full credit to **Analyst Academy** for the original framework framing.

---

### If this saved you time

⭐ **Star this repo** — it helps others find it.
📺 **Subscribe to [ConrayGambit on YouTube](https://youtube.com/@conraygambit)** — for more AI/LLM tools, walkthroughs, and prompt-engineering tutorials.
🔗 **Share it** with the next person you see drowning in unstructured analysis.
