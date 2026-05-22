import subprocess, sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent

def run_judge(*args):
    r = subprocess.run(
        [sys.executable, str(ROOT / "evals" / "judge.py"), *args],
        capture_output=True, text=True
    )
    return r.returncode, r.stdout, r.stderr


def test_emit_contains_rubric_and_output():
    """Emit mode: stdout must contain a distinctive phrase from RUBRIC.md,
    the word JSON (from the task instruction), and text from the output file."""
    code, out, err = run_judge(str(ROOT / "evals" / "fixtures" / "good-5fw.md"))
    assert code == 0, f"emit exited {code}; stderr={err}"
    # Distinctive phrase from RUBRIC.md (section 1 header)
    assert "MECE Categorization" in out, "RUBRIC content not found in emitted prompt"
    # Task instruction must tell the judge to return JSON
    assert "JSON" in out, "word 'JSON' not found in emitted prompt"
    # Text from the output file itself
    assert "cloud infrastructure costs" in out, "output file content not found in emitted prompt"


def test_grade_passes():
    """Grade mode on the sample fixture must exit 0 and print Average:"""
    code, out, err = run_judge("--grade", str(ROOT / "evals" / "fixtures" / "judge-sample.json"))
    assert code == 0, f"grade exited {code}; stdout={out}; stderr={err}"
    assert "Average:" in out, f"'Average:' not found in output:\n{out}"


def test_grade_fails_below_min():
    """Same fixture with --min 4.9 must exit 1 (mean ~3.83 < 4.9)."""
    code, out, err = run_judge(
        "--grade", str(ROOT / "evals" / "fixtures" / "judge-sample.json"),
        "--min", "4.9"
    )
    assert code == 1, f"expected exit 1, got {code}; stdout={out}; stderr={err}"
