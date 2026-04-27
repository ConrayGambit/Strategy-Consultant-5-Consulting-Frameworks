# Installation Guide

Pick the section that matches how you use Claude (or another LLM).

---

## Option 1: Claude Code (macOS / Linux)

Claude Code reads skills from `~/.claude/skills/`. Drop the contents of this repo's `skills/` folder there.

```bash
git clone https://github.com/ConrayGambit/Strategy-Consultant-5-Consulting-Frameworks.git
cd Strategy-Consultant-5-Consulting-Frameworks
mkdir -p ~/.claude/skills
cp -r skills/* ~/.claude/skills/
```

Restart Claude Code. The skills will appear in autocomplete:

- `/visual-strategy-consultant` — full sequential analysis
- `/visual-strategy-consultant-agents` — sub-agent version (parallel deep dives)
- `/mece-framework` — MECE only
- `/issue-trees` — issue tree only
- `/hypothesis-driven` — hypothesis test only
- `/pareto-principle` — Pareto only
- `/so-what-test` — So What? only

---

## Option 1b: Claude Code on Windows (PowerShell)

Open **PowerShell** (regular, not admin) and run:

```powershell
# Clone the repo
git clone https://github.com/ConrayGambit/Strategy-Consultant-5-Consulting-Frameworks.git
cd Strategy-Consultant-5-Consulting-Frameworks

# Create the Claude skills folder if it doesn't exist
$skillsPath = "$env:USERPROFILE\.claude\skills"
if (-not (Test-Path $skillsPath)) { New-Item -ItemType Directory -Path $skillsPath -Force | Out-Null }

# Copy each skill folder into it
Copy-Item -Path .\skills\* -Destination $skillsPath -Recurse -Force

# Verify
Get-ChildItem $skillsPath
```

You should see seven folders listed: the two masters + five framework sub-skills. Restart Claude Code and try `/visual-strategy-consultant`.

**If you don't have git installed:** download the repo as a ZIP from GitHub (green "Code" button → "Download ZIP"), extract it, then:

```powershell
cd "$env:USERPROFILE\Downloads\Strategy-Consultant-5-Consulting-Frameworks-main"
$skillsPath = "$env:USERPROFILE\.claude\skills"
if (-not (Test-Path $skillsPath)) { New-Item -ItemType Directory -Path $skillsPath -Force | Out-Null }
Copy-Item -Path .\skills\* -Destination $skillsPath -Recurse -Force
```

---

## Option 2: Cowork (Anthropic Skills)

Cowork supports the same skills format as Claude Code. Two ways to install:

**A. Copy into the user skills folder.**

Windows (PowerShell):

```powershell
$cwSkills = "$env:APPDATA\Claude\skills"
if (-not (Test-Path $cwSkills)) { New-Item -ItemType Directory -Path $cwSkills -Force | Out-Null }
Copy-Item -Path .\skills\* -Destination $cwSkills -Recurse -Force
```

macOS:

```bash
mkdir -p "$HOME/Library/Application Support/Claude/skills"
cp -r skills/* "$HOME/Library/Application Support/Claude/skills/"
```

Drop each skill folder (`visual-strategy-consultant/`, `mece-framework/`, etc.) into that directory. Restart Cowork.

**B. Bundle as a plugin.** If you want to share with your team, package the `skills/` folder as a Claude Code plugin and host it in a marketplace. See [Claude docs on plugins](https://docs.claude.com).

---

## Option 3: Claude.ai (Projects)

1. Create a new Project in Claude.ai
2. Open the Project's "Custom instructions" or "Project knowledge"
3. Paste the contents of [`prompts/visual-strategy-consultant.md`](./prompts/visual-strategy-consultant.md) into Custom instructions
4. Optionally upload the individual framework prompts as Project knowledge files for reference

---

## Option 4: ChatGPT (Custom GPT)

1. Go to **Explore GPTs → Create**
2. In the "Configure" tab, paste [`prompts/visual-strategy-consultant.md`](./prompts/visual-strategy-consultant.md) into the **Instructions** field
3. Set name, description, and conversation starters (e.g., "Analyze our churn problem", "Break down this operational issue")
4. Save and use

---

## Option 5: Gemini, Mistral, local models, anywhere else

The plain prompts in [`prompts/`](./prompts/) work in any system that accepts a system prompt or a starting message. Two patterns:

**Pattern A — system prompt:** Set the model's system prompt to the contents of `prompts/visual-strategy-consultant.md`. Send your business problem as the first user message.

**Pattern B — pasted preamble:** Paste the prompt as the first message. Add `"Apply this framework to the following problem: <your problem>"` at the end.

---

## Verifying it works

After installation, test with this prompt:

> Our enterprise sales cycle has stretched from 60 days to 110 days over the past six months. Why?

You should get back a structured response with all five visual frameworks (MECE, Issue Tree, Hypothesis Table, Pareto blockquote, So What sections). If any are missing, the system prompt didn't take — re-paste it and try again.

---

## Updating

When new versions ship:

```bash
cd Strategy-Consultant-5-Consulting-Frameworks
git pull
cp -r skills/* ~/.claude/skills/
```

For prompt-based installs (ChatGPT, Claude.ai), re-copy the latest [`prompts/visual-strategy-consultant.md`](./prompts/visual-strategy-consultant.md).
