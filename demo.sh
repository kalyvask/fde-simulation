#!/usr/bin/env bash
# demo.sh — one-command tour of the FDE Simulation repo.
#
# Runs the Calder (insurance) and Helix (finance) prototypes end-to-end
# on synthetic data, with the weighted eval suite at the production-grade
# pass^k=5 threshold. No API key required — drafters fall back to
# deterministic mock outputs.
#
# Total time: about 90 seconds on a typical machine.
# Tested on: Python 3.10+, macOS / Linux / Windows WSL.
#
# Usage:
#   bash demo.sh

set -euo pipefail

cyan='\033[0;36m'
green='\033[0;32m'
yellow='\033[1;33m'
reset='\033[0m'

REPO_ROOT="$(cd "$(dirname "$0")" && pwd)"
CALDER_PROTO="$REPO_ROOT/simulations/1-full-engagement/calder-insurance/02_week2_solution/prototype"
HELIX_PROTO="$REPO_ROOT/simulations/1-full-engagement/helix-finance/02_week2_solution/prototype"

print_banner() {
  echo
  printf "${cyan}%s${reset}\n" "============================================================"
  printf "${cyan}%s${reset}\n" "$1"
  printf "${cyan}%s${reset}\n" "============================================================"
  echo
}

check_python() {
  if ! command -v python3 >/dev/null 2>&1 && ! command -v python >/dev/null 2>&1; then
    echo "ERROR: Python 3.10+ is required but not found on PATH."
    echo "Install Python from https://www.python.org/downloads/ and re-run."
    exit 1
  fi
}

# Use python3 if available, else python
PY=$(command -v python3 || command -v python)

print_banner "FDE Simulation — full demo"
echo "This script will:"
echo "  1. Install requirements for both prototypes (one-time)"
echo "  2. Run the Calder insurance prototype on a synthetic FNOL"
echo "  3. Run the Calder eval suite at pass^k=5"
echo "  4. Run the Helix finance prototype on a synthetic earnings call"
echo "  5. Run the Helix eval suite at pass^k=5"
echo
echo "Drafters will fall back to deterministic mock outputs if no"
echo "ANTHROPIC_API_KEY is set. Set the key for real LLM calls."
echo

check_python

# --- Calder ---
print_banner "1/4 — Installing Calder prototype requirements"
cd "$CALDER_PROTO"
$PY -m pip install -q -r requirements.txt
printf "${green}OK${reset}\n"

print_banner "2/4 — Calder FNOL end-to-end (synthetic claim)"
$PY scripts/run_e2e.py

print_banner "3/4 — Calder eval suite (pass^k=5 production threshold)"
$PY scripts/run_eval.py

# --- Helix ---
print_banner "Installing Helix prototype requirements"
cd "$HELIX_PROTO"
$PY -m pip install -q -r requirements.txt
printf "${green}OK${reset}\n"

print_banner "4/4 — Helix earnings-note end-to-end (synthetic call)"
$PY scripts/run_e2e.py

print_banner "Helix eval suite (pass^k=5 production threshold)"
$PY scripts/run_eval.py

# --- Wrap-up ---
print_banner "Demo complete"
echo "What you just saw:"
echo "  - Two agent workforces (Calder + Helix) running end-to-end"
echo "    on synthetic data, with examiner-readable audit traces."
echo "  - Two eval suites running at pass^k=5 (production threshold)."
echo "  - Drafters in mock mode — set ANTHROPIC_API_KEY for live LLM calls."
echo
printf "${yellow}Next steps:${reset}\n"
echo "  - Read QUICKSTART.md for the 4 simulation paths"
echo "  - Read frameworks/README.md for the 10 portable frameworks"
echo "  - Try simulations/1-full-engagement/calder-insurance/EXERCISE.md"
echo "    for the 4-week guided engagement"
echo
