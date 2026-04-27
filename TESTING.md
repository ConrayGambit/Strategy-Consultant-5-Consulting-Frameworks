# Testing the Skills

How to verify your install works end-to-end across each platform. Use this after installation to confirm everything's wired up before relying on the skills for real work.

---

## The canonical test prompt

Paste this exact problem into your install. It's designed to exercise all five frameworks (it's specific enough to test, ambiguous enough to require judgment, and has a "wrong" reframe baked in):

> Our enterprise B2B SaaS sales cycle has stretched from 60 days to 110 days over the past six months. New ARR is on track to miss our annual target by ~15%. Leadership wants to know what's happening and what to do — they're considering reorganizing the sales team. I'm the VP of Revenue and I have a board meeting in two weeks.

The expected output is documented in [`examples/example-analysis.md`](./examples/example-analysis.md). Your output won't match word-for-word, but it should match the *shape* — five sections in order, with the correct visual format for each.

---

## What "passing" looks like

A correct output has all five of these:

| # | Section | Pass criteria |
|---|---|---|
| 1 | MECE Categorization | 3–6 nested bullet groups, top-level in **bold**, no overlapping factors |
| 2 | Issue Tree | Fenced code block with ASCII tree using `├──`, `│`, `└──`; at least 2 levels deep |
| 3 | Hypothesis-Driven | One-sentence falsifiable hypothesis + Markdown table; at least one row designed as a control (something that should NOT match if the hypothesis is true) |
| 4 | Pareto Focus | Markdown blockquote naming the vital 20% (1–4 specific items) + bulleted list of deprioritized items |
| 5 | "So What?" Test | Three labeled sections: **Process:** / **Result:** / **Insight:**; the Insight names a who, what, by-when, and target |

**Bonus signal of a strong run:** the response opens with a one-sentence reframe of the original question (challenging the leadership-proposed sales reorg before applying the frameworks). This isn't required on every prompt — the skill is supposed to reframe only when the framing is questionable — but on this particular test prompt, a reframe is the consultant move.

---

## Test by install path

### Path 1: Claude Code on macOS / Linux

```bash
# Verify install
ls ~/.claude/skills/
# Expected: 7 directories — visual-strategy-consultant, visual-strategy-consultant-agents, mece-framework, issue-trees, hypothesis-driven, pareto-principle, so-what-test
```

In Claude Code:

1. Type `/visual-strategy-consultant` (autocomplete should suggest it).
2. Paste the canonical test prompt.
3. Verify the output matches the pass criteria above.

To test a single sub-skill:

1. Type `/mece-framework`
2. Paste: *"I'm the VP of Engineering and our incident rate has doubled in the last quarter."*
3. Verify nested bullets only — no other sections should appear.

### Path 2: Claude Code on Windows (PowerShell)

```powershell
# Verify install
Get-ChildItem "$env:USERPROFILE\.claude\skills"
# Expected: 7 directories
```

Then same in-app test as Path 1.

### Path 3: Cowork on Windows (PowerShell)

```powershell
# Verify install
Get-ChildItem "$env:APPDATA\Claude\skills"
# Expected: 7 directories
```

Restart Cowork. In a new chat, type `/visual-strategy-consultant` and paste the test prompt.

### Path 4: Cowork on macOS

```bash
ls "$HOME/Library/Application Support/Claude/skills"
# Expected: 7 directories
```

Restart Cowork. Same in-app test.

### Path 5: Claude.ai (paste-as-system-prompt)

1. Open a new conversation at [claude.ai](https://claude.ai).
2. Copy the entire contents of [`prompts/visual-strategy-consultant.md`](./prompts/visual-strategy-consultant.md).
3. Paste as the first message.
4. Send. Claude will acknowledge.
5. Send the canonical test prompt as the second message.
6. Verify the output matches the pass criteria.

### Path 6: Claude.ai Project

1. Create a new Project at [claude.ai](https://claude.ai).
2. Open Custom Instructions.
3. Paste the entire contents of [`prompts/visual-strategy-consultant.md`](./prompts/visual-strategy-consultant.md).
4. Save.
5. Start a chat in the Project.
6. Send the canonical test prompt.
7. Verify the output matches the pass criteria.

### Path 7: ChatGPT Custom GPT

1. Go to **Explore GPTs → Create**.
2. In the **Configure** tab, paste [`prompts/visual-strategy-consultant.md`](./prompts/visual-strategy-consultant.md) into the Instructions field.
3. Set the name and description.
4. Save and open the GPT.
5. Send the canonical test prompt.
6. Verify the output matches the pass criteria.

ChatGPT may render the ASCII tree slightly differently from Claude — that's fine as long as the structure is intact.

### Path 8: Gemini, Mistral, local models, etc.

1. Set the model's system prompt to the contents of [`prompts/visual-strategy-consultant.md`](./prompts/visual-strategy-consultant.md), or paste it as the first user message.
2. Send the canonical test prompt.
3. Verify the output matches the pass criteria.

Smaller models (under ~7B parameters) may struggle with the full 5-section structure — they'll often skip the Pareto blockquote or produce vague Insights. That's a model limitation, not a skill bug.

---

## Common failure modes

| Symptom | Likely cause | Fix |
|---|---|---|
| Skill not found in Claude Code autocomplete | Skills directory wrong, or app not restarted | Re-check install path; quit and relaunch the app |
| Output is prose, no visual structure | System prompt wasn't applied (paste-based installs) | Re-paste; in some chat UIs, you have to send before it takes effect |
| Some sections missing (e.g., no Issue Tree) | Model truncated, or system prompt was too long combined with question | Try sub-skills individually, or use a model with a larger context window |
| ASCII tree renders as boxes / question marks | Renderer doesn't support box-drawing characters | Skill should auto-fall back to indented dashes — if not, ask explicitly: "use indented dashes for the tree" |
| Insight is vague / unassignable | Model dropped the assignability requirement | Add to your prompt: "make the Insight specific enough to assign to a person with a deadline" |
| Reframe missing on a problem that obviously deserves one | Model interpreted the problem too literally | Add: "before applying the frameworks, check whether the framing of the problem is itself the issue" |

---

## Sub-skill tests (single-framework)

If you want to test each sub-skill individually, use these one-line prompts:

| Skill | Test prompt |
|---|---|
| `mece-framework` | "Categorize the factors that could explain why our restaurant's lunch covers dropped from 85/day to 52/day." |
| `issue-trees` | "Build an issue tree for: 30-day cardiology readmissions jumped from 11.2% to 16.8%." |
| `hypothesis-driven` | "Build a hypothesis test for: card decline rate jumped from 4.1% to 7.8% after a fraud-model deploy." |
| `pareto-principle` | "Apply 80/20 to: I'm a YouTuber with three pillars (AI tutorials, business strategy, productivity) — which should I focus on?" |
| `so-what-test` | "I have data showing 64% of bootcamp dropouts happen weeks 3–5 when curriculum compresses backend modules. Translate to action." |

Each should produce ONLY the visual format of that single framework — no other sections.

---

## Reporting bugs

If a skill produces output that violates its visual contract:

1. Save the exact prompt you used.
2. Save the exact output you got.
3. Note the platform (Claude Code, Claude.ai, ChatGPT, etc.) and any model identifier.
4. Open an issue: [github.com/ConrayGambit/Strategy-Consultant-5-Consulting-Frameworks/issues](https://github.com/ConrayGambit/Strategy-Consultant-5-Consulting-Frameworks/issues).

Bugs in the skill content (not model behavior) get fixed quickly. Model-behavior bugs are harder — sometimes the prompt needs sharpening, sometimes the model is the limit.
