#!/usr/bin/env python3
"""
Visual Strategy Consultant — output scorer.

Reads model output from stdin (or a file argument), scores it against the
5-section visual contract, prints a pass/fail breakdown, and exits with
code 0 if all sections pass, 1 otherwise.

Usage:
    python evals/score.py < output.txt
    python evals/score.py output.txt
    cat output.txt | python evals/score.py --quiet  # exit code only

Pure stdlib, no dependencies.
"""

from __future__ import annotations
import argparse
import re
import sys
from dataclasses import dataclass


# ---------------------------------------------------------------------------
# Scoring data classes
# ---------------------------------------------------------------------------

@dataclass
class CheckResult:
    name: str
    passed: bool
    detail: str = ""


# ---------------------------------------------------------------------------
# Individual section checks
# ---------------------------------------------------------------------------

def check_mece(text: str) -> CheckResult:
    """Section 1: MECE — heading + at least 3 top-level nested bullet groups."""
    heading = re.search(r"^#{1,4}\s*1\.\s*MECE", text, re.MULTILINE | re.IGNORECASE)
    if not heading:
        return CheckResult("1. MECE Categorization", False, "Missing heading '### 1. MECE...'")

    # Look for top-level bullets in bold (the category markers)
    section = _section_after(text, heading.start(), next_heading_pattern=r"^#{1,4}\s*2\.")
    bold_bullets = re.findall(r"^[-*]\s+\*\*[^*]+\*\*", section, re.MULTILINE)

    if len(bold_bullets) < 3:
        return CheckResult(
            "1. MECE Categorization", False,
            f"Found {len(bold_bullets)} bold top-level bullet(s); need at least 3 categories"
        )

    # Verify there are nested bullets under categories
    nested = re.findall(r"^\s{2,}[-*]\s+", section, re.MULTILINE)
    if len(nested) < 3:
        return CheckResult(
            "1. MECE Categorization", False,
            f"Found {len(nested)} nested sub-factor(s); MECE needs sub-factors under categories"
        )

    return CheckResult(
        "1. MECE Categorization", True,
        f"{len(bold_bullets)} categories, {len(nested)} sub-factors"
    )


def check_issue_tree(text: str) -> CheckResult:
    """Section 2: Issue Tree — fenced code block with box-drawing tree characters."""
    heading = re.search(r"^#{1,4}\s*2\.\s*Issue\s*Tree", text, re.MULTILINE | re.IGNORECASE)
    if not heading:
        return CheckResult("2. Issue Tree", False, "Missing heading '### 2. Issue Tree'")

    section = _section_after(text, heading.start(), next_heading_pattern=r"^#{1,4}\s*3\.")

    # Look for box-drawing characters within a fenced code block
    code_blocks = re.findall(r"```[a-zA-Z]*\n(.*?)```", section, re.DOTALL)
    if not code_blocks:
        return CheckResult("2. Issue Tree", False, "No fenced code block found")

    tree_block = next(
        (b for b in code_blocks if "├──" in b or "└──" in b),
        None
    )

    # Fallback: indented-dash tree is also valid
    if tree_block is None:
        # Check for a tree-like structure with indented dashes
        for block in code_blocks:
            indented_dashes = re.findall(r"^\s{2,}-\s+", block, re.MULTILINE)
            if len(indented_dashes) >= 3:
                # Looks like a fallback tree
                depth = max(_indent_depth(line) for line in block.splitlines() if line.strip().startswith("-"))
                return CheckResult(
                    "2. Issue Tree", True,
                    f"Indented-dash fallback tree, depth {depth}"
                )
        return CheckResult(
            "2. Issue Tree", False,
            "Code block found but no box-drawing chars (├── │ └──) and no indented-dash fallback"
        )

    # Count tree depth via leading whitespace + box-drawing nesting
    levels = set()
    for line in tree_block.splitlines():
        if "├──" in line or "└──" in line:
            indent = len(line) - len(line.lstrip())
            levels.add(indent)
    depth = len(levels)
    if depth < 1:
        return CheckResult("2. Issue Tree", False, "Tree has no detectable branches")

    return CheckResult("2. Issue Tree", True, f"Box-drawing tree, ~{depth} level(s) deep")


def check_hypothesis(text: str) -> CheckResult:
    """Section 3: Hypothesis-Driven — Hypothesis statement + Markdown table."""
    heading = re.search(
        r"^#{1,4}\s*3\.\s*Hypothesis", text, re.MULTILINE | re.IGNORECASE
    )
    if not heading:
        return CheckResult("3. Hypothesis-Driven", False, "Missing heading '### 3. Hypothesis...'")

    section = _section_after(text, heading.start(), next_heading_pattern=r"^#{1,4}\s*4\.")

    if not re.search(r"\*\*Hypothesis:?\*\*", section, re.IGNORECASE):
        return CheckResult(
            "3. Hypothesis-Driven", False,
            "No '**Hypothesis:**' label found"
        )

    # Find a Markdown table — header row of pipes plus separator row of dashes
    table_match = re.search(
        r"\|.*\|.*\|\s*\n\s*\|[-:\s|]+\|\s*\n((?:.*\|.*\|.*\n?)+)",
        section
    )
    if not table_match:
        return CheckResult("3. Hypothesis-Driven", False, "No Markdown table found")

    body = table_match.group(1)
    rows = [r for r in body.strip().splitlines() if r.strip().startswith("|")]
    if len(rows) < 4:
        return CheckResult(
            "3. Hypothesis-Driven", False,
            f"Table has {len(rows)} data rows; need at least 4"
        )

    return CheckResult(
        "3. Hypothesis-Driven", True,
        f"Hypothesis stated, table with {len(rows)} rows"
    )


def check_pareto(text: str) -> CheckResult:
    """Section 4: Pareto — blockquote naming the vital 20% + deprioritized list."""
    heading = re.search(
        r"^#{1,4}\s*4\.\s*Pareto", text, re.MULTILINE | re.IGNORECASE
    )
    if not heading:
        return CheckResult("4. Pareto Focus", False, "Missing heading '### 4. Pareto...'")

    section = _section_after(text, heading.start(), next_heading_pattern=r"^#{1,4}\s*5\.")

    blockquote = re.search(
        r"^>\s+.*(?:vital\s+20|the\s+20\s*%|20%).*",
        section, re.MULTILINE | re.IGNORECASE
    )
    if not blockquote:
        # Looser: any blockquote with content > 30 chars
        any_bq = re.search(r"^>\s+\S.{30,}", section, re.MULTILINE)
        if not any_bq:
            return CheckResult(
                "4. Pareto Focus", False,
                "No blockquote (`>`) naming the vital 20%"
            )

    deprioritized = re.search(
        r"deprioritized|the\s+80\s*%|actively\s+deprior", section, re.IGNORECASE
    )
    if not deprioritized:
        return CheckResult(
            "4. Pareto Focus", False,
            "No 'deprioritized' / 'the 80%' label found"
        )

    # Verify there's a list after the deprioritization label
    after = section[deprioritized.start():]
    bullets = re.findall(r"^[-*]\s+\S", after, re.MULTILINE)
    if len(bullets) < 3:
        return CheckResult(
            "4. Pareto Focus", False,
            f"Found {len(bullets)} deprioritized item(s); list should have at least 3"
        )

    return CheckResult(
        "4. Pareto Focus", True,
        f"Blockquote present, {len(bullets)} deprioritized items"
    )


def check_so_what(text: str) -> CheckResult:
    """Section 5: So What? — Process / Result / Insight, with assignability cue."""
    heading = re.search(
        r"^#{1,4}\s*5\.\s*(?:The\s+)?[\"']?So\s*What", text, re.MULTILINE | re.IGNORECASE
    )
    if not heading:
        return CheckResult('5. "So What?" Test', False, "Missing heading '### 5. So What...'")

    section = text[heading.start():]

    process = re.search(r"\*\*Process:?\*\*", section, re.IGNORECASE)
    result = re.search(r"\*\*Result:?\*\*", section, re.IGNORECASE)
    insight = re.search(r"\*\*Insight:?\*\*", section, re.IGNORECASE)

    missing = [name for name, m in [("Process", process), ("Result", result), ("Insight", insight)] if not m]
    if missing:
        return CheckResult(
            '5. "So What?" Test', False,
            f"Missing label(s): {', '.join(missing)}"
        )

    insight_text = section[insight.end():insight.end() + 1500]
    # Cue indicating assignability: a deadline word, a date, or a "by ..." phrase
    has_deadline = re.search(
        r"\b(?:by|within|next|target|owner|q[1-4]|days?|weeks?|months?|"
        r"\d+\s*(?:days?|weeks?|months?)|monday|tuesday|wednesday|thursday|"
        r"friday|saturday|sunday|EOW|EOM|EOQ|deadline)\b",
        insight_text, re.IGNORECASE
    )
    if not has_deadline:
        return CheckResult(
            '5. "So What?" Test', False,
            "Insight present but no deadline/owner cue (by/within/next/target/owner/days/etc.)"
        )

    return CheckResult(
        '5. "So What?" Test', True,
        "Process / Result / Insight all present; assignability cue found"
    )


def check_order(text: str) -> CheckResult:
    """All five sections appear in canonical order 1 -> 2 -> 3 -> 4 -> 5."""
    positions = []
    for n, label in enumerate(
        ["MECE", "Issue\\s*Tree", "Hypothesis", "Pareto", "(?:The\\s+)?[\"']?So\\s*What"], start=1
    ):
        m = re.search(rf"^#{{1,4}}\s*{n}\.\s*{label}", text, re.MULTILINE | re.IGNORECASE)
        if m:
            positions.append((n, m.start()))

    if len(positions) < 5:
        return CheckResult("Order", False, f"Only {len(positions)}/5 section headings found")

    # Confirm strictly increasing positions
    increasing = all(positions[i][1] < positions[i + 1][1] for i in range(len(positions) - 1))
    if not increasing:
        return CheckResult("Order", False, "Sections present but not in canonical order")

    return CheckResult("Order", True, "Sections 1–5 appear in canonical order")


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _section_after(text: str, start: int, next_heading_pattern: str) -> str:
    """Return text from start until the next heading matching the pattern."""
    rest = text[start:]
    end_match = re.search(next_heading_pattern, rest, re.MULTILINE | re.IGNORECASE)
    return rest[:end_match.start()] if end_match else rest


def _indent_depth(line: str) -> int:
    if not line.strip():
        return 0
    return (len(line) - len(line.lstrip())) // 2 + 1


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

CHECKS = [
    check_mece,
    check_issue_tree,
    check_hypothesis,
    check_pareto,
    check_so_what,
    check_order,
]


def score(text: str) -> tuple[list[CheckResult], int, int]:
    results = [check(text) for check in CHECKS]
    passed = sum(1 for r in results if r.passed)
    return results, passed, len(results)


def format_report(results: list[CheckResult], passed: int, total: int) -> str:
    lines = []
    lines.append("Visual Strategy Consultant — output scorer")
    lines.append("=" * 50)
    for r in results:
        mark = "PASS" if r.passed else "FAIL"
        lines.append(f"  [{mark}] {r.name}")
        if r.detail:
            lines.append(f"         {r.detail}")
    lines.append("-" * 50)
    lines.append(f"  Result: {passed}/{total} checks passed")
    lines.append("")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Score Visual Strategy Consultant output.")
    parser.add_argument("input", nargs="?", default=None,
                        help="File to read (default: stdin)")
    parser.add_argument("--quiet", action="store_true",
                        help="Suppress report; exit code only")
    args = parser.parse_args(argv)

    text = (open(args.input, encoding="utf-8").read()
            if args.input else sys.stdin.read())

    results, passed, total = score(text)

    if not args.quiet:
        print(format_report(results, passed, total))

    return 0 if passed == total else 1


if __name__ == "__main__":
    raise SystemExit(main())
