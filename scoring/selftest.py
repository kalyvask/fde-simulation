"""Key-free self-test for the scoring package.

Validates that the JSON template embedded in every rubric's grader system prompt
is itself parseable JSON once the placeholder tokens are filled in. The grader is
shown this template as the output spec; if the template contains invalid JSON (e.g.
a trailing comma), the model tends to copy the mistake, `grade._extract_json_block`
returns None, and no JSON sidecar gets written — silently breaking `bundle.py`'s
grade table. This guards against that regression without needing an API key.

Run: python -m scoring.selftest
"""

from __future__ import annotations

import json
import re
import sys

from .rubrics import RUBRICS, build_system_prompt

# Mirrors the extraction regex used by scoring.grade._extract_json_block.
_JSON_BLOCK = re.compile(r"```json\s*(\{.*?\})\s*```", re.DOTALL)


def _filled_template(phase) -> str:
    rubric = RUBRICS[phase]
    block = _JSON_BLOCK.findall(build_system_prompt(rubric))[-1]
    block = re.sub(r"<0-3>", "0", block)
    block = re.sub(r"<integer 0-\d+>", str(rubric.max_score), block)
    block = re.sub(r"<one sentence>", "x", block)
    return block


def main() -> int:
    failures = []
    for phase in RUBRICS:
        try:
            json.loads(_filled_template(phase))
        except (json.JSONDecodeError, IndexError) as e:
            failures.append(f"{phase}: {e}")
    if failures:
        for f in failures:
            sys.stderr.write(f"FAIL {f}\n")
        return 1
    print(f"ok: rubric JSON templates valid for {', '.join(RUBRICS)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
