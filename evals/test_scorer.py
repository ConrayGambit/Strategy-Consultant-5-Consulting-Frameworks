import subprocess, sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent

def run(path, *args):
    r = subprocess.run([sys.executable, str(ROOT/"evals"/"score.py"), str(path), *args],
                       capture_output=True, text=True)
    return r.returncode, r.stdout

def test_bad_fixture_fails():
    code, _ = run(ROOT/"evals/fixtures/bad-prose-only.md")
    assert code == 1

def test_good_5fw_passes():
    code, out = run(ROOT/"evals/fixtures/good-5fw.md")
    assert code == 0, out

def test_good_7fw_passes_in_7_mode():
    code, out = run(ROOT/"evals/fixtures/good-7fw.md", "--mode", "7")
    assert code == 0, out

def test_auto_detects_7fw():
    code, out = run(ROOT/"evals/fixtures/good-7fw.md")  # auto-detect, no flag
    assert code == 0, out
