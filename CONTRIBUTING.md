# Contributing

Thanks for considering a contribution. The bar for changes is low for content (examples, docs) and higher for changes to the skill output contracts (because consistency *is* the value of this repo).

---

## What's easy to contribute

- **More example input/output pairs.** Pick an industry not yet represented (logistics, biotech, gaming, government, sports, agriculture, education, manufacturing, etc.) and drop a file into `examples/full-runs/` or `examples/single-frameworks/`. See existing files for the format. Update `examples/README.md` to link to it.
- **Translations of the prompts.** Spanish, Mandarin, Japanese, Hindi, etc. Drop into `prompts/<lang>/` with the same filenames.
- **Typos, broken links, formatting fixes.** Just open a PR.
- **New install paths.** Cowork on Linux? VS Code MCP? Add a section to `INSTALLATION.md`.
- **Bug reports.** If a skill produces output that violates its visual contract (e.g., MECE without a blockquote, So What? without an assignable Insight), open an issue with the prompt that triggered it.

## What needs more discussion (open an issue first)

- **New frameworks.** The current five are the canonical sequence. Adding a sixth (e.g., Pyramid Principle, First-Principles Decomposition, Force Field Analysis) is a real change — open an issue to discuss before submitting a PR.
- **Changes to the visual contracts.** Switching MECE from nested bullets to numbered lists, changing the Pareto blockquote to a callout, etc. Visual structure is the entire value of the repo, so changes need rationale.
- **Major reorganization** of the repo layout. Discuss first.

## How to submit a PR

1. Fork the repo on GitHub.
2. Make your changes on a feature branch (`feature/add-government-example`, `fix/typo-in-mece-skill`, etc.).
3. Commit with a descriptive message.
4. Open a PR with:
   - **What** you changed
   - **Why** (briefly)
   - **How to verify** (e.g., "paste `prompts/...` into Claude.ai and test with this problem...")

Small PRs ship fast. Large ones get a 2-week conversation. Make small ones if you can.

## Style for examples

If you're adding an example input/output pair, follow this structure:

```markdown
# Title — Industry / Framework

## Input (what the user typed)
> [verbatim user prompt]

## Output (what the skill produced)
[the structured response]

## What to notice
- [bullet 1: a judgment call the skill made]
- [bullet 2: a default that was flexed]
- [bullet 3: a subtle move worth highlighting]
```

The "What to notice" section is the most useful part for readers. Don't skip it.

## Style for skill changes

- Keep `description:` fields under ~50 words.
- Frame rules as defaults with explicit flex points where judgment matters; only mark a rule "doesn't flex" when it's load-bearing.
- Include at least one concrete example in the SKILL.md body.
- Add a footer linking to the LICENSE.

## Code of conduct

Be kind. Critique ideas, not people. Maintainer reserves the right to close PRs that don't fit the project's direction without obligation to explain at length — but will always explain in good faith.

## License

By contributing, you agree your contributions are licensed under the same MIT license as the project. See [LICENSE](./LICENSE).
