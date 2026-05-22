#!/usr/bin/env python3
"""
Strategy Consultant — output scorer.

Reads model output from stdin (or a file argument), scores it against the
visual contract, prints a pass/fail breakdown, and exits with code 0 if all
sections pass, 1 otherwise.

Supports 5-framework mode (default) and 7-framework mode (adds "3. 5 Whys"
and "7. Pyramid Principle", shifting Hypothesis→4, Pareto→5, So What→6).

Usage:
    python evals/score.py < output.txt
    python evals/score.py output.txt
    python evals/score.py output.txt --mode 7
    python evals/score.py output.txt --mode auto   # auto-detect (default)
    cat output.txt | python evals/score.py --quiet  # exit code only

Pure stdlib, no dependencies.
"""

from __future__ import annotations
import argparse
import re
import sys
from dataclasses import dataclass

# Generic "next numbered heading" boundary — works regardless of section number
_NEXT_NUMBERED = r"^#{1,4}\s*\d+\.\s"


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
    heading = re.search(r"^#{1,4}\s*\d+\.\s*MECE", text, re.MULTILINE | re.IGNORECASE)
    if not heading:
        return CheckResult("1. MECE Categorization", False, "Missing heading '### 1. MECE...'")

    # Look for top-level bullets in bold (the category markers)
    section = _section_after(text, heading.start(), next_heading_pattern=_NEXT_NUMBERED)
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
    heading = re.search(r"^#{1,4}\s*\d+\.\s*Issue\s*Tree", text, re.MULTILINE | re.IGNORECASE)
    if not heading:
        return CheckResult("2. Issue Tree", False, "Missing heading '### 2. Issue Tree'")

    section = _section_after(text, heading.start(), next_heading_pattern=_NEXT_NUMBERED)

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


def check_five_whys(text: str) -> CheckResult:
    """Section 3 (7-fw): 5 Whys — at least 5 numbered Why lines + Root cause label."""
    heading = re.search(
        r"^#{1,4}\s*\d+\.\s*(?:5\s*Whys|Five\s+Whys)", text, re.MULTILINE | re.IGNORECASE
    )
    if not heading:
        return CheckResult("3. 5 Whys", False, "Missing heading '### 3. 5 Whys'")

    section = _section_after(text, heading.start(), next_heading_pattern=_NEXT_NUMBERED)

    why_lines = re.findall(r"^\s*\d+\.\s+\*\*Why", section, re.MULTILINE)
    if len(why_lines) < 5:
        return CheckResult(
            "3. 5 Whys", False,
            f"Found {len(why_lines)} '**Why' line(s); need at least 5"
        )

    root_cause = re.search(r"\*\*Root cause:?\*\*", section, re.IGNORECASE)
    if not root_cause:
        return CheckResult("3. 5 Whys", False, "No '**Root cause:**' label found")

    return CheckResult(
        "3. 5 Whys", True,
        f"{len(why_lines)} Why lines, Root cause label present"
    )


def check_hypothesis(text: str) -> CheckResult:
    """Hypothesis — Hypothesis statement + Markdown table (any section number)."""
    heading = re.search(
        r"^#{1,4}\s*\d+\.\s*Hypothesis", text, re.MULTILINE | re.IGNORECASE
    )
    if not heading:
        return CheckResult("3. Hypothesis-Driven", False, "Missing heading '### N. Hypothesis...'")

    section = _section_after(text, heading.start(), next_heading_pattern=_NEXT_NUMBERED)

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
    """Pareto — blockquote naming the vital 20% + deprioritized list (any section number)."""
    heading = re.search(
        r"^#{1,4}\s*\d+\.\s*Pareto", text, re.MULTILINE | re.IGNORECASE
    )
    if not heading:
        return CheckResult("4. Pareto Focus", False, "Missing heading '### N. Pareto...'")

    section = _section_after(text, heading.start(), next_heading_pattern=_NEXT_NUMBERED)

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
    """So What? — Process / Result / Insight, with assignability cue (any section number)."""
    heading = re.search(
        r"^#{1,4}\s*\d+\.\s*(?:The\s+)?[\"']?So\s*What", text, re.MULTILINE | re.IGNORECASE
    )
    if not heading:
        return CheckResult('5. "So What?" Test', False, "Missing heading '### N. So What...'")

    section = _section_after(text, heading.start(), next_heading_pattern=_NEXT_NUMBERED)

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


def check_pyramid(text: str) -> CheckResult:
    """Section 7 (7-fw): Pyramid Principle — Answer label + at least 2 numbered bold arguments."""
    heading = re.search(
        r"^#{1,4}\s*\d+\.\s*(?:Executive\s*Communication|Pyramid)",
        text, re.MULTILINE | re.IGNORECASE
    )
    if not heading:
        return CheckResult(
            "7. Pyramid Principle", False,
            "Missing heading '### N. Executive Communication' or '### N. Pyramid'"
        )

    # To end of doc (last section)
    section = text[heading.start():]

    if not re.search(r"\*\*Answer:?\*\*", section, re.IGNORECASE):
        return CheckResult("7. Pyramid Principle", False, "No '**Answer:**' label found")

    # At least 2 numbered bold arguments
    args = re.findall(r"^\s*\d+\.\s+\*\*", section, re.MULTILINE)
    if len(args) < 2:
        return CheckResult(
            "7. Pyramid Principle", False,
            f"Found {len(args)} numbered bold argument(s); need at least 2"
        )

    return CheckResult(
        "7. Pyramid Principle", True,
        f"Answer present, {len(args)} numbered arguments"
    )


def check_order(text: str, mode: int = 5) -> CheckResult:
    """Sections appear in canonical order for the given mode."""
    if mode == 7:
        names = [
            ("MECE", r"MECE"),
            ("Issue Tree", r"Issue\s*Tree"),
            ("5 Whys", r"(?:5\s*Whys|Five\s+Whys)"),
            ("Hypothesis", r"Hypothesis"),
            ("Pareto", r"Pareto"),
            ("So What", r"(?:The\s+)?[\"']?So\s*What"),
            ("Pyramid", r"(?:Executive\s*Communication|Pyramid)"),
        ]
    else:
        names = [
            ("MECE", r"MECE"),
            ("Issue Tree", r"Issue\s*Tree"),
            ("Hypothesis", r"Hypothesis"),
            ("Pareto", r"Pareto"),
            ("So What", r"(?:The\s+)?[\"']?So\s*What"),
        ]

    positions = []
    for label, pattern in names:
        m = re.search(
            rf"^#{{1,4}}\s*\d+\.\s*{pattern}",
            text, re.MULTILINE | re.IGNORECASE
        )
        if m:
            positions.append((label, m.start()))

    expected = len(names)
    if len(positions) < expected:
        found_names = [p[0] for p in positions]
        missing = [n for n, _ in names if n not in found_names]
        return CheckResult(
            "Order", False,
            f"Only {len(positions)}/{expected} section headings found; missing: {', '.join(missing)}"
        )

    # Confirm strictly increasing positions
    increasing = all(positions[i][1] < positions[i + 1][1] for i in range(len(positions) - 1))
    if not increasing:
        return CheckResult("Order", False, "Sections present but not in canonical order")

    return CheckResult("Order", True, f"Sections 1-{expected} appear in canonical order")


# ---------------------------------------------------------------------------
# Mode detection
# ---------------------------------------------------------------------------

def detect_mode(text: str) -> int:
    """Return 7 if both '5 Whys' and 'Pyramid/Executive Communication' headings present, else 5."""
    has_five_whys = bool(re.search(
        r"^#{1,4}\s*\d+\.\s*(?:5\s*Whys|Five\s+Whys)", text, re.MULTILINE | re.IGNORECASE
    ))
    has_pyramid = bool(re.search(
        r"^#{1,4}\s*\d+\.\s*(?:Executive\s*Communication|Pyramid)", text, re.MULTILINE | re.IGNORECASE
    ))
    return 7 if (has_five_whys and has_pyramid) else 5


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _section_after(text: str, start: int, next_heading_pattern: str) -> str:
    """Return text from start until the next heading matching the pattern.

    Skips past the end of the current heading line before searching for the
    boundary so the heading's own ``#`` characters don't match the pattern.
    """
    rest = text[start:]
    # Advance past the current heading line
    nl = rest.find("\n")
    search_from = nl if nl != -1 else len(rest)
    end_match = re.search(next_heading_pattern, rest[search_from:], re.MULTILINE | re.IGNORECASE)
    if end_match:
        return rest[:search_from + end_match.start()]
    return rest


def _indent_depth(line: str) -> int:
    if not line.strip():
        return 0
    return (len(line) - len(line.lstrip())) // 2 + 1


# ---------------------------------------------------------------------------
# Check lists
# ---------------------------------------------------------------------------

CHECKS_5 = [
    check_mece,
    check_issue_tree,
    check_hypothesis,
    check_pareto,
    check_so_what,
    lambda text: check_order(text, mode=5),
]

CHECKS_7 = [
    check_mece,
    check_issue_tree,
    check_five_whys,
    check_hypothesis,
    check_pareto,
    check_so_what,
    check_pyramid,
    lambda text: check_order(text, mode=7),
]

# Legacy alias kept for any external callers
CHECKS = CHECKS_5


# ---------------------------------------------------------------------------
# Score entry point
# ---------------------------------------------------------------------------

def score(text: str, mode: str = "auto") -> tuple[list[CheckResult], int, int]:
    if mode == "auto":
        resolved = detect_mode(text)
    else:
        resolved = int(mode)

    checks = CHECKS_7 if resolved == 7 else CHECKS_5
    results = [check(text) for check in checks]
    passed = sum(1 for r in results if r.passed)
    return results, passed, len(results)


def format_report(results: list[CheckResult], passed: int, total: int) -> str:
    lines = []
    lines.append("Strategy Consultant - output scorer")
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
    parser = argparse.ArgumentParser(description="Score Strategy Consultant output.")
    parser.add_argument("input", nargs="?", default=None,
                        help="File to read (default: stdin)")
    parser.add_argument("--quiet", action="store_true",
                        help="Suppress report; exit code only")
    parser.add_argument("--mode", choices=["5", "7", "auto"], default="auto",
                        help="Scoring mode: 5-framework, 7-framework, or auto-detect (default: auto)")
    args = parser.parse_args(argv)

    text = (open(args.input, encoding="utf-8").read()
            if args.input else sys.stdin.read())

    results, passed, total = score(text, mode=args.mode)

    if not args.quiet:
        print(format_report(results, passed, total))

    return 0 if passed == total else 1


if __name__ == "__main__":
    raise SystemExit(main())
