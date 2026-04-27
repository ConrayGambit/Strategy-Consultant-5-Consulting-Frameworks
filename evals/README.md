# Evals

Automated grading for skill output against the visual contract. Use this to:

- Verify a new install produces correct output without manually eyeballing it
- Regression-test changes to the SKILL.md files
- Compare output quality across LLM providers (Claude, ChatGPT, Gemini)

---

## Quick start

```bash
# From the repo root
python evals/score.py < your-output.txt
```

You can also pipe directly from a CLI:

```bash
echo "Our churn jumped 4 points last quarter and nobody knows why." \
  | claude --skill visual-strategy-consultant \
  | python evals/score.py
```

The script reads model output from stdin, scores it against the 5-section rubric, and prints a passing/failing breakdown. Exit code is `0` if pass, `1` if any section fails.

---

## What it checks

The scorer is a deterministic, regex-based check — not an LLM-as-judge. It catches structural failures (missing sections, wrong format) but cannot judge content quality. Use the [rubric](./RUBRIC.md) for that.

| # | Check | Pass criteria |
|---|---|---|
| 1 | MECE section present | Heading matches `1. MECE`, contains nested bullets with at least 3 categories |
| 2 | Issue Tree present | Fenced code block contains `├──`, `│`, and `└──` characters; at least 2 levels deep |
| 3 | Hypothesis present | "Hypothesis:" prefix found; Markdown table follows with at least 4 rows |
| 4 | Pareto present | Markdown blockquote (`>`) with "vital 20%" or similar; deprioritized list follows |
| 5 | So What present | Three labeled sections: Process, Result, Insight. Insight contains a deadline-like cue (date, "by", "next [day]", etc.) |
| 6 | Order correctness | Sections appear in canonical order: 1 → 2 → 3 → 4 → 5 |

---

## Files

- [`score.py`](./score.py) — the scorer. ~200 lines of pure stdlib Python (no dependencies).
- [`RUBRIC.md`](./RUBRIC.md) — manual rubric for content-quality assessment (what the regex can't see).
- [`fixtures/`](./fixtures/) — known-good and known-bad output samples for testing the scorer itself.

---

## Limitations

- **Can't detect MECE violations.** Two overlapping categories will pass the structural check.
- **Can't judge whether a hypothesis is genuinely falsifiable.** A vague hypothesis with a structured table will pass.
- **Can't tell if the Pareto 20% is the actual 20%.** Anything in a blockquote passes.
- **Insight assignability** is checked weakly — it looks for date-like or owner-like cues, but a sentence like "we should focus by next week" would pass.

For content-quality grading, use [`RUBRIC.md`](./RUBRIC.md) with a human reviewer, or run an LLM-as-judge pass (see roadmap).

---

## Roadmap

- [ ] LLM-as-judge mode that reads output and rates content quality 1–5 against the rubric
- [ ] Multi-provider comparison harness (run the same prompt against Claude, GPT, Gemini, score each)
- [ ] CI integration — GitHub Action that scores PR-changed output samples automatically
