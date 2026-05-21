"""Verifiable scoring and artifact bundling for the fde-simulation engagement.

Two CLIs:
  - scoring.grade: numeric rubric grade per engagement phase, diff'd against the
    reference solution.
  - scoring.bundle: walk a portfolio directory and emit a single submittable
    Markdown pack.
"""

__version__ = "0.1.0"
