import subprocess, sys, pathlib
import pytest
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


SHOWCASE = ROOT / "examples" / "showcase"
FULL_RUNS = sorted((ROOT / "examples" / "full-runs").glob("*.md"))


# --- Showcase master / pack outputs (5-framework mode) ---

def test_showcase_cloud_cost_5fw_passes():
    code, out = run(SHOWCASE / "cloud-cost.md")
    assert code == 0, out


def test_showcase_sc_saas_nrr_decline_5fw_passes():
    code, out = run(SHOWCASE / "sc-saas-nrr-decline.md")
    assert code == 0, out


# --- Showcase 7-framework output (must explicitly use --mode 7) ---

def test_showcase_sc7_bank_loan_cycle_7fw_passes():
    code, out = run(SHOWCASE / "sc-7-bank-loan-cycle.md", "--mode", "7")
    assert code == 0, out


# --- All full-run examples (auto-discovered; grows as new examples are added) ---

@pytest.mark.parametrize("path", FULL_RUNS, ids=[p.name for p in FULL_RUNS])
def test_full_run_scores_6_of_6(path):
    code, out = run(path)
    assert code == 0, out
