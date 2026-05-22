"""
evals/judge.py — dependency-free LLM-as-judge for content-quality scoring.

Usage:
  EMIT mode (default):
    python evals/judge.py <output.md>
    Reads RUBRIC.md (sibling) + the output file, prints a complete judging prompt
    to stdout. Paste that prompt into any LLM, save its JSON reply, then grade it.

  GRADE mode:
    python evals/judge.py --grade <response.json> [--min 3.5]
    Reads the judge's JSON (file arg or stdin), prints a readable table, computes
    the mean of all numeric scores, and exits 0 if mean >= --min else 1.
    Exit 2 on malformed/missing JSON.

No third-party dependencies. No network. No API key required.
The LLM call happens in whatever model you paste the emitted prompt into —
same philosophy as the plain prompts in this repo.
"""

import argparse
import json
import sys
import os
from pathlib import Path

# On Windows the default stdout codec (cp1252) can't encode some Unicode chars
# (e.g., ≥ in RUBRIC.md).  Reconfigure to UTF-8 when possible.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

RUBRIC_PATH = Path(__file__).resolve().parent / "RUBRIC.md"

JUDGE_TASK = """
---

## YOUR TASK

You are a content-quality judge for management consulting skill output.

Read the rubric above, then read the OUTPUT TO EVALUATE below. Score each rubric
dimension on a scale of 1–5 using this mapping:

  1 = rubric score 0   (missing / wrong format)
  2 = rubric score 1   (present but weak)
  3 = rubric score 2   (solid)
  4 = rubric score 3   (excellent)
  5 = exceptional      (exceeds the rubric's top descriptor)

For each dimension, write ONE short sentence explaining your score.

Return ONLY the following JSON — no prose before or after it, no markdown fences:

{"scores": {"MECE Categorization": {"score": <1-5>, "why": "<short>"}, "Issue Tree": {"score": <1-5>, "why": "<short>"}, "Hypothesis-Driven": {"score": <1-5>, "why": "<short>"}, "Pareto Focus": {"score": <1-5>, "why": "<short>"}, "So What Test": {"score": <1-5>, "why": "<short>"}, "Reframe / Overall Judgment": {"score": <1-5>, "why": "<short>"}}, "overall": "<1-2 sentence verdict>"}

---

## OUTPUT TO EVALUATE

"""


def emit(output_path: Path) -> None:
    """Read RUBRIC.md + output file and print a complete judging prompt to stdout."""
    if not RUBRIC_PATH.exists():
        print(f"ERROR: rubric not found at {RUBRIC_PATH}", file=sys.stderr)
        sys.exit(2)

    if not output_path.exists():
        print(f"ERROR: output file not found: {output_path}", file=sys.stderr)
        sys.exit(2)

    rubric_text = RUBRIC_PATH.read_text(encoding="utf-8")
    output_text = output_path.read_text(encoding="utf-8")

    print("# LLM-as-Judge — Content Quality Evaluation")
    print()
    print("## RUBRIC (verbatim)")
    print()
    print(rubric_text)
    print(JUDGE_TASK)
    print(output_text)


def grade(response_source: str, min_score: float) -> None:
    """Read judge JSON, print table, compute mean, exit 0/1/2."""
    # Load JSON
    try:
        if response_source == "-":
            raw = sys.stdin.read()
        else:
            p = Path(response_source)
            if not p.exists():
                print(f"ERROR: response file not found: {p}", file=sys.stderr)
                sys.exit(2)
            raw = p.read_text(encoding="utf-8")
    except OSError as e:
        print(f"ERROR reading response: {e}", file=sys.stderr)
        sys.exit(2)

    # Parse JSON
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as e:
        print(f"ERROR: malformed JSON — {e}", file=sys.stderr)
        sys.exit(2)

    if not isinstance(data, dict) or "scores" not in data:
        print("ERROR: JSON missing required 'scores' key", file=sys.stderr)
        sys.exit(2)

    scores_obj = data["scores"]
    if not isinstance(scores_obj, dict) or not scores_obj:
        print("ERROR: 'scores' must be a non-empty object", file=sys.stderr)
        sys.exit(2)

    # Validate each dimension
    numeric_scores = []
    rows = []
    for dim, val in scores_obj.items():
        if not isinstance(val, dict):
            print(f"ERROR: score entry for '{dim}' must be an object", file=sys.stderr)
            sys.exit(2)
        if "score" not in val:
            print(f"ERROR: score entry for '{dim}' missing 'score' key", file=sys.stderr)
            sys.exit(2)
        try:
            s = float(val["score"])
        except (TypeError, ValueError):
            print(f"ERROR: score for '{dim}' is not numeric: {val['score']!r}", file=sys.stderr)
            sys.exit(2)
        why = val.get("why", "")
        numeric_scores.append(s)
        rows.append((dim, s, why))

    # Print table
    col_dim = max(len(r[0]) for r in rows)
    col_dim = max(col_dim, len("Dimension"))
    header = f"{'Dimension':<{col_dim}}  {'Score':>5}  Why"
    print(header)
    print("-" * len(header))
    for dim, s, why in rows:
        print(f"{dim:<{col_dim}}  {s:>5.1f}  {why}")

    print()

    # Overall verdict
    overall = data.get("overall", "")
    if overall:
        print(f"Verdict: {overall}")
        print()

    # Mean
    mean = sum(numeric_scores) / len(numeric_scores)
    print(f"Average: {mean:.1f}/5 (min {min_score:.1f})")

    sys.exit(0 if mean >= min_score else 1)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="LLM-as-judge: emit a rubric-based judging prompt or grade a JSON reply."
    )
    parser.add_argument(
        "output",
        nargs="?",
        help="Path to the skill output file to judge (emit mode). Use '-' for stdin.",
    )
    parser.add_argument(
        "--grade",
        metavar="RESPONSE_JSON",
        help="Path to judge's JSON reply (grade mode). Use '-' for stdin.",
    )
    parser.add_argument(
        "--min",
        type=float,
        default=3.5,
        metavar="N",
        help="Minimum average score to exit 0 (default: 3.5).",
    )
    args = parser.parse_args()

    if args.grade is not None:
        grade(args.grade, args.min)
    elif args.output is not None:
        emit(Path(args.output))
    else:
        parser.print_help()
        sys.exit(2)


if __name__ == "__main__":
    main()
