# Publishing This Repo to GitHub — Step-by-Step

A user-friendly walkthrough for getting this folder onto GitHub. Pick the path that matches your comfort level.

---

## Path A: GitHub Desktop (easiest, no command line)

**One-time setup:**

1. Install [GitHub Desktop](https://desktop.github.com/) (free).
2. Sign in with your GitHub account (create one at [github.com/signup](https://github.com/signup) if you don't have one).

**Publishing:**

1. Open GitHub Desktop → **File → Add Local Repository** → choose `C:\Claude Workspace\Personal Assistant\visual-strategy-consultant`.
2. It will say "this directory does not appear to be a Git repository — Create a Repository?" Click **Create a Repository**.
3. Fill in:
   - **Name:** `Strategy-Consultant-5-Consulting-Frameworks`
   - **Description:** `Tier-1 strategy-consultant frameworks (MECE, Issue Trees, Hypothesis-Driven, Pareto, So What?) packaged as Claude Skills + LLM-agnostic prompts.`
   - **Git ignore:** None (we already have one)
   - **License:** None (we already have MIT)
4. Click **Create Repository**.
5. Click the big **Publish repository** button at the top.
6. Uncheck "Keep this code private" if you want it public.
7. Click **Publish repository**.

Done. Your repo is live at `github.com/ConrayGambit/Strategy-Consultant-5-Consulting-Frameworks`.

---

## Path B: PowerShell + git (Windows)

**One-time setup:**

1. Install [Git for Windows](https://git-scm.com/download/win).
2. Configure your identity (open PowerShell):

   ```powershell
   git config --global user.name "Your Name"
   git config --global user.email "you@example.com"
   ```

3. Sign in to [github.com](https://github.com) and create a new empty repository named `Strategy-Consultant-5-Consulting-Frameworks`. **Do not** initialize it with a README, .gitignore, or license — you already have those.

**Publishing:**

```powershell
cd "C:\Claude Workspace\Personal Assistant\Strategy-Consultant-5-Consulting-Frameworks"

# Initialize git
git init
git branch -M main

# Stage and commit everything
git add .
git commit -m "Initial commit: Visual Strategy Consultant skills + prompts"

# Connect to GitHub (replace ConrayGambit)
git remote add origin https://github.com/ConrayGambit/Strategy-Consultant-5-Consulting-Frameworks.git

# Push
git push -u origin main
```

If pushing prompts for credentials, GitHub will direct you to authenticate via browser (recommended) or with a personal access token.

---

## Path C: macOS / Linux Terminal

```bash
cd ~/path/to/Strategy-Consultant-5-Consulting-Frameworks
git init
git branch -M main
git add .
git commit -m "Initial commit: Visual Strategy Consultant skills + prompts"
git remote add origin https://github.com/ConrayGambit/Strategy-Consultant-5-Consulting-Frameworks.git
git push -u origin main
```

Same as Path B, just bash syntax.

---

## After publishing — make it discoverable

These small touches make a big difference for adoption:

### 1. Add topics

On your repo page → click the gear icon next to "About" (right sidebar) → add topics:

```
claude  claude-code  cowork  anthropic  llm  prompts  skills
strategy  consulting  mece  issue-tree  pareto  business-frameworks
prompt-engineering  ai-tools
```

Topics are how people discover repos via GitHub search.

### 2. Set the description and website

Same "About" gear icon:

- **Description:** `Tier-1 strategy-consultant frameworks (MECE, Issue Trees, Hypothesis-Driven, Pareto, So What?) packaged as Claude Skills + LLM-agnostic prompts. Drop in any LLM and get whiteboard-style structured analysis.`
- **Website:** the YouTube video URL you'd like attribution to point to, or your own site.

### 3. Pin the repo to your profile

On your GitHub profile → "Customize your pins" → select this repo. Top-of-profile visibility for visitors.

### 4. Add a release

Once you've used it for a few days and feel good about v1.0:

- Repo page → **Releases** (right sidebar) → **Create a new release**
- Tag: `v1.0.0`
- Title: `v1.0.0 — Initial release`
- Description: copy the highlights from your README

Releases give people a stable artifact to install and a changelog over time.

### 5. Optional: Submit to skill directories

If skill marketplaces or directories exist for Claude Skills (check [docs.claude.com](https://docs.claude.com) for the latest), submit your repo. Same for any "awesome-llm-prompts" lists on GitHub — a PR adding a one-line entry usually lands fast.

---

## Updating the repo later

When you make improvements:

```powershell
cd "C:\Claude Workspace\Personal Assistant\Strategy-Consultant-5-Consulting-Frameworks"
git add .
git commit -m "Tighten MECE description; add finance example"
git push
```

For larger changes, work on a branch:

```powershell
git checkout -b feature/add-7-frameworks-version
# edit files...
git add .
git commit -m "Draft 7-framework variant"
git push -u origin feature/add-7-frameworks-version
```

Then open a Pull Request on GitHub to merge it into main when ready.

---

## Common pitfalls

- **"Permission denied" pushing to main.** GitHub may block force-pushes or require 2FA. Check Settings → Branch protection rules.
- **Large file warnings.** This repo should be tiny (text only). If you see warnings, check that you didn't accidentally include `node_modules/`, `.venv/`, or similar — `.gitignore` should prevent this but worth verifying.
- **README not rendering.** Make sure the file is named `README.md` (capital R, capital M, lowercase d). GitHub is case-sensitive.
- **License not showing as "MIT" in the repo header.** Make sure the file is named exactly `LICENSE` (no extension). GitHub auto-detects this.

---

## A nice-to-have: GitHub Actions for link checking

Optional but classy. Create `.github/workflows/links.yml`:

```yaml
name: Check links
on:
  push:
    branches: [main]
  pull_request:
  schedule:
    - cron: '0 0 1 * *'

jobs:
  linkChecker:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: lycheeverse/lychee-action@v1
        with:
          args: --verbose --no-progress './**/*.md'
```

Now if any markdown link in the repo breaks, you'll get a notification. Free quality control.
