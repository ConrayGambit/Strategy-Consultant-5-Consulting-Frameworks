# Evals

Automated grading for skill output against the visual contract. Use this to:

- Verify a new install produces correct output without manually eyeballing it
- Regression-test changes to the SKILL.md files
- Compare output quality across LLM providers (Claude, ChatGPT, Gemini)

---

## Quick start

```bash
# From the repo root — 5-framework output (default)
python evals/score.py < your-output.txt

# 7-framework output (adds 5 Whys + Pyramid sections)
python evals/score.py your-output.txt --mode 7

# Auto-detect mode (inspects headings, picks 5 or 7 automatically)
python evals/score.py your-output.txt --mode auto
```

You can also pipe directly from a CLI:

```bash
echo "Our churn jumped 4 points last quarter and nobody knows why." \
  | claude --skill strategy-consultant \
  | python evals/score.py
```

The script reads model output from stdin, scores it against the rubric, and prints a passing/failing breakdown. Exit code is `0` if all checks pass, `1` if any section fails.

---

## Modes

| Flag | Sections scored | Use for |
|---|---|---|
| `--mode 5` (or omit) | 6 checks (MECE, Issue Tree, Hypothesis, Pareto, So What, Order) | `strategy-consultant` 5-framework master |
| `--mode 7` | 8 checks (adds 5 Whys, Pyramid) | `strategy-consultant-7` 7-framework master |
| `--mode auto` | auto-detects by inspecting headings | default; works for both |

---

## What it checks

The scorer is a deterministic, regex-based check — not an LLM-as-judge. It catches structural failures (missing sections, wrong format) but cannot judge content quality. Use the [rubric](./RUBRIC.md) for that.

### 5-framework checks

| # | Check | Pass criteria |
|---|---|---|
| 1 | MECE section present | Heading matches `N. MECE`, contains nested bullets with at least 3 categories |
| 2 | Issue Tree present | Fenced code block contains `├──`, `│`, and `└──` characters; at least 2 levels deep |
| 3 | Hypothesis present | "Hypothesis:" prefix found; Markdown table follows with at least 4 rows |
| 4 | Pareto present | Markdown blockquote (`>`) with "vital 20%" or similar; deprioritized list follows |
| 5 | So What present | Three labeled sections: Process, Result, Insight. Insight contains a deadline-like cue |
| 6 | Order correctness | Sections appear in canonical order: 1 → 2 → 3 → 4 → 5 |

### 7-framework checks (adds 2 more)

| # | Check | Pass criteria |
|---|---|---|
| 3 | 5 Whys present | Heading matches `N. 5 Whys`; ≥5 numbered `**Why` lines; `**Root cause:**` label |
| 7 | Pyramid Principle present | Heading matches `N. Pyramid` or `N. Executive Communication`; `**Answer:**` label; ≥2 numbered bold arguments |

---

## Running the test suite

```bash
python -m pytest evals/test_scorer.py -v
```

Expected output: 4 tests, all passing.

---

## Files

- [`score.py`](./score.py) — the scorer. ~479 lines of pure stdlib Python (no dependencies).
- [`test_scorer.py`](./test_scorer.py) — pytest harness; 4 tests covering bad fixture, good-5fw, good-7fw (explicit mode), and good-7fw (auto-detect).
- [`RUBRIC.md`](./RUBRIC.md) — manual rubric for content-quality assessment (what the regex can't see).
- [`fixtures/`](./fixtures/) — known-good and known-bad output samples for testing the scorer itself.
  - `bad-prose-only.md` — should score 1 (always fails)
  - `good-5fw.md` — canonical 5-framework output; should score 6/6
  - `good-7fw.md` — canonical 7-framework output; should score 8/8

---

## Limitations

- **Can't detect MECE violations.** Two overlapping categories will pass the structural check.
- **Can't judge whether a hypothesis is genuinely falsifiable.** A vague hypothesis with a structured table will pass.
- **Can't tell if the Pareto 20% is the actual 20%.** Anything in a blockquote passes.
- **Insight assignability** is checked weakly — it looks for date-like or owner-like cues, but a sentence like "we should focus by next week" would pass.

For content-quality grading, use [`RUBRIC.md`](./RUBRIC.md) with a human reviewer, or use [`judge.py`](./judge.py) for an LLM-as-judge pass.

---

## LLM-as-judge (content quality)

`judge.py` turns the rubric into an LLM-judgeable prompt and grades the reply. It complements (not replaces) `score.py` — the scorer catches structural failures; the judge catches content failures that a regex can't see (e.g., a non-MECE MECE section, an unfalsifiable hypothesis, a Pareto that lists 10 items).

Fully dependency-free. No API key. The LLM call happens in whatever model you paste the emitted prompt into — same philosophy as the plain prompts in this repo.

### Emit mode — produce the judging prompt

```bash
python evals/judge.py evals/fixtures/good-5fw.md
```

This prints a complete prompt to stdout: the full rubric text verbatim, the output to evaluate, and a task instruction telling the judge to score each dimension 1–5 and return a specific JSON structure. Pipe it or copy-paste into any LLM.

```bash
# Pipe to a file for later use
python evals/judge.py your-output.md > judging-prompt.txt
```

### Grade mode — score a judge reply

After your LLM returns its JSON, save it to a file and run:

```bash
python evals/judge.py --grade judge-reply.json
```

This prints a readable table (dimension | score | why), computes the mean of all numeric scores, and prints `Average: X.X/5 (min 3.5)`. Exit code is `0` if mean ≥ `--min` (default 3.5), `1` if below, `2` on malformed JSON.

```bash
# Raise the bar
python evals/judge.py --grade judge-reply.json --min 4.0

# Read from stdin
cat judge-reply.json | python evals/judge.py --grade -
```

### Expected JSON schema from the judge

```json
{
  "scores": {
    "<dimension>": {"score": <1-5>, "why": "<short reason>"},
    ...
  },
  "overall": "<1-2 sentence verdict>"
}
```

A sample valid reply is at [`fixtures/judge-sample.json`](./fixtures/judge-sample.json).

### Running the judge test suite

```bash
python -m pytest evals/test_judge.py -v
```

Expected output: 3 tests, all passing.

---

## Roadmap

- [x] LLM-as-judge mode — `judge.py` emits a rubric-based judging prompt and grades the JSON reply (content quality 1–5). Dependency-free, no API key. ✅
- [ ] Multi-provider comparison harness (run the same prompt against Claude, GPT, Gemini, score each)
- [ ] CI integration — GitHub Action that scores PR-changed output samples automatically
