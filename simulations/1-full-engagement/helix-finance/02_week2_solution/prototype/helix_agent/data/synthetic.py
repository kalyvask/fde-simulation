"""Synthetic earnings-call generator — placeholder until real data flows.

Schema mirrors what we'd get from EDGAR-CORPUS + ECTSum + Refinitiv consensus.
Once real data is loaded, swap this module with a loader.
"""
from __future__ import annotations

import random
from typing import Any


SAMPLE_TRANSCRIPTS = [
    {
        "ticker": "SAMPLE_TMT",
        "quarter": "Q3 2026",
        "prepared_remarks": "Revenue of $3.2B exceeded our internal expectations. Operating margin expanded 80 basis points. Guidance for Q4 is in the range of $3.4B to $3.5B.",
        "qa_section": "Analyst asked about pricing pressure in the consumer segment; management acknowledged increased competition but maintained confidence in pricing discipline.",
    },
    {
        "ticker": "SAMPLE_INDUSTRIAL",
        "quarter": "Q3 2026",
        "prepared_remarks": "Revenue of $5.1B vs $5.4B prior year. Pricing actions partially offset volume declines. Guidance withdrawn pending Q4 visibility.",
        "qa_section": "Analyst pushed on guidance withdrawal — management cited macro uncertainty without specifics.",
    },
    {
        "ticker": "SAMPLE_CONSUMER",
        "quarter": "Q3 2026",
        "prepared_remarks": "Strong quarter with revenue of $2.8B, up 12% YoY. EPS of $1.45 vs $1.20 consensus. Raising full-year guidance by 5%.",
        "qa_section": "Tone notably more confident than Q2 call — multiple references to 'momentum' and 'inflection.'",
    },
]


def generate_earnings_claim(seed: int | None = None) -> dict[str, Any]:
    if seed is not None:
        random.seed(seed)
    sample = random.choice(SAMPLE_TRANSCRIPTS)
    return {
        "note_id": f"NOTE-{sample['ticker']}-{sample['quarter'].replace(' ', '')}",
        "ticker": sample["ticker"],
        "quarter": sample["quarter"],
        "transcript": sample["prepared_remarks"] + " " + sample["qa_section"],
        "prepared_remarks": sample["prepared_remarks"],
        "qa_section": sample["qa_section"],
        "filing": (
            "10-Q Item 1A (Risk Factors): No material changes from the prior period's "
            "annual report on Form 10-K. Item 2 (MD&A): Revenue growth of 12% YoY driven "
            "by core segment expansion. Operating margin compressed 80bps on supply-side "
            "pressure offset by pricing actions. (Synthetic mock for architecture demo; "
            "production system pulls live FactSet feed.)"
        ),
        "consensus_revenue": "$3.1B",
        "consensus_eps": "$1.30",
        "kpis_extracted": {
            "revenue": "$3.2B",
            "eps": "$1.45",
            "guidance_range": "$3.4B to $3.5B",
        },
        "citations": [
            "transcript:prepared_remarks:line_1",
            "transcript:prepared_remarks:line_2",
            "filing:10q:item_1",
        ],
        "sector": "TMT" if "TMT" in sample["ticker"] else "Industrials",
        "analyst_owner": "Rachel Kim",
    }
