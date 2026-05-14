# demo.ps1 — one-command tour of the FDE Simulation repo (Windows PowerShell).
#
# Runs the Calder (insurance) and Helix (finance) prototypes end-to-end
# on synthetic data, with the weighted eval suite at the production-grade
# pass^k=5 threshold. No API key required — drafters fall back to
# deterministic mock outputs.
#
# Total time: about 90 seconds on a typical machine.
# Tested on: Windows PowerShell 5.1+ / PowerShell Core 7+ with Python 3.10+.
#
# Usage:
#   .\demo.ps1
#
# If you hit an execution-policy error, run once:
#   Set-ExecutionPolicy -Scope CurrentUser RemoteSigned

$ErrorActionPreference = "Stop"

$RepoRoot = $PSScriptRoot
$CalderProto = Join-Path $RepoRoot "simulations\1-full-engagement\calder-insurance\02_week2_solution\prototype"
$HelixProto  = Join-Path $RepoRoot "simulations\1-full-engagement\helix-finance\02_week2_solution\prototype"

function Print-Banner {
    param([string]$Text)
    Write-Host ""
    Write-Host "============================================================" -ForegroundColor Cyan
    Write-Host $Text -ForegroundColor Cyan
    Write-Host "============================================================" -ForegroundColor Cyan
    Write-Host ""
}

function Check-Python {
    $py = Get-Command python -ErrorAction SilentlyContinue
    if (-not $py) {
        $py = Get-Command python3 -ErrorAction SilentlyContinue
    }
    if (-not $py) {
        Write-Host "ERROR: Python 3.10+ is required but not found on PATH." -ForegroundColor Red
        Write-Host "Install Python from https://www.python.org/downloads/ and re-run."
        exit 1
    }
    return $py.Source
}

Print-Banner "FDE Simulation — full demo"
Write-Host "This script will:"
Write-Host "  1. Install requirements for both prototypes (one-time)"
Write-Host "  2. Run the Calder insurance prototype on a synthetic FNOL"
Write-Host "  3. Run the Calder eval suite at pass^k=5"
Write-Host "  4. Run the Helix finance prototype on a synthetic earnings call"
Write-Host "  5. Run the Helix eval suite at pass^k=5"
Write-Host ""
Write-Host "Drafters will fall back to deterministic mock outputs if no"
Write-Host "ANTHROPIC_API_KEY is set. Set the key for real LLM calls."
Write-Host ""

$PY = Check-Python

# --- Calder ---
Print-Banner "1/4 — Installing Calder prototype requirements"
Set-Location $CalderProto
& $PY -m pip install -q -r requirements.txt
Write-Host "OK" -ForegroundColor Green

Print-Banner "2/4 — Calder FNOL end-to-end (synthetic claim)"
& $PY scripts/run_e2e.py

Print-Banner "3/4 — Calder eval suite (pass^k=5 production threshold)"
& $PY scripts/run_eval.py

# --- Helix ---
Print-Banner "Installing Helix prototype requirements"
Set-Location $HelixProto
& $PY -m pip install -q -r requirements.txt
Write-Host "OK" -ForegroundColor Green

Print-Banner "4/4 — Helix earnings-note end-to-end (synthetic call)"
& $PY scripts/run_e2e.py

Print-Banner "Helix eval suite (pass^k=5 production threshold)"
& $PY scripts/run_eval.py

# --- Wrap-up ---
Print-Banner "Demo complete"
Write-Host "What you just saw:"
Write-Host "  - Two agent workforces (Calder + Helix) running end-to-end"
Write-Host "    on synthetic data, with examiner-readable audit traces."
Write-Host "  - Two eval suites running at pass^k=5 (production threshold)."
Write-Host "  - Drafters in mock mode — set ANTHROPIC_API_KEY for live LLM calls."
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Yellow
Write-Host "  - Read QUICKSTART.md for the 4 simulation paths"
Write-Host "  - Read frameworks\README.md for the 10 portable frameworks"
Write-Host "  - Try simulations\1-full-engagement\calder-insurance\EXERCISE.md"
Write-Host "    for the 4-week guided engagement"
Write-Host ""

Set-Location $RepoRoot
