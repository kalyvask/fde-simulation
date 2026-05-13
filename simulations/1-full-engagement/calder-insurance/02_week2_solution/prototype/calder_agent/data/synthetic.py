"""Synthetic FNOL generator — placeholder until Greg's 500-claim pull lands.

The schema mirrors what we expect from the real pull. Once real data is
available, swap this module with a loader; the rest of the workforce is
schema-stable.
"""
from __future__ import annotations

import random
from datetime import datetime, timedelta
from typing import Any


NJ_DESCRIPTIONS = [
    "I was driving on the GSP and the car ahead of me braked suddenly. I rear-ended them.",
    "I was parked at a Wawa and someone hit my car while I was inside.",
    "Side-swiped on Route 1 by a driver changing lanes without signaling.",
    "Fender bender at the UPS Edison NJ distribution center while making a delivery.",
    "Backed into a parked vehicle in our office parking lot.",
]

PA_DESCRIPTIONS = [
    "Hit by another vehicle while parked outside a Wawa near Philadelphia.",
    "Lost control on a wet road on I-95 and hit the guardrail.",
    "Rear-ended in stop-and-go traffic on the Schuylkill Expressway.",
]

CLAIMANT_NAMES = [
    "Mr. Patel", "Ms. Johnson", "John Smith", "Sarah Lee",
    "Acme Distributors LLC", "Mrs. Wong", "Mr. Sullivan", "Ms. Garcia",
]


def generate_fnol(
    state: str = "NJ",
    channel: str = "web",
    lob: str = "comm_auto",
    seed: int | None = None,
) -> dict[str, Any]:
    if seed is not None:
        random.seed(seed)

    descriptions = NJ_DESCRIPTIONS if state == "NJ" else PA_DESCRIPTIONS

    return {
        "claim_id": f"CL-{datetime.now().year}-{state}-{random.randint(10000, 99999)}",
        "policy_id": f"POL-{random.randint(100000, 999999)}",
        "channel": channel,
        "lob": lob,
        "state": state,
        "claimant_name": random.choice(CLAIMANT_NAMES),
        "incident_date": (
            datetime.now() - timedelta(days=random.randint(1, 7))
        ).date().isoformat(),
        "incident_description": random.choice(descriptions),
        "estimated_damage": random.choice([1500, 2400, 3200, 4800]),
        "first_time_customer": random.random() < 0.3,
        "has_child_or_elderly_party": random.random() < 0.05,
        "has_prior_claim_in_12_months": random.random() < 0.1,
        "touches_coverage_decision": False,  # v1 wedge does not touch coverage
        "touches_settlement_decision": False,
    }
