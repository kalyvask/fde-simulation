"""NHTSA narrative augmentation — real-world phrasing for stress testing.

The full NHTSA CRSS public dataset has ~50K crash narratives per year. For the
scaffold we ship a curated in-code corpus of representative narrative SHAPES
(written in the style and tone of real CRSS narratives) so the eval harness
exercises real-world phrasing patterns without requiring a 50MB download.

To use the real corpus, run `data/fetch_data.py --nhtsa` from the engagement
root, then call `load_real_narratives()` below.
"""
from __future__ import annotations

import csv
import random
from pathlib import Path
from typing import Iterator


# In-code corpus: narrative shapes mirroring real NHTSA CRSS records.
# Each has at least one Janet "tell" or a known difficult phrasing pattern.
NHTSA_LIKE_NARRATIVES: list[str] = [
    "Driver of V1 stated he was traveling east on Route 22 in the right lane when V2 changed lanes from the center lane without signaling. V1 stated he didn't have time to react and contact occurred at the right rear quarter panel.",
    "V1 was stopped at a red light at the intersection when V2, also traveling north, failed to stop and rear-ended V1. Driver of V2 stated 'I never saw them' and admitted to looking at her phone.",
    "Driver of V1 was traveling on the GSP southbound when traffic ahead came to a sudden stop. V1 was unable to stop in time and rear-ended V2. Driver V1 stated 'they came out of nowhere' but witness statements indicate V2 had been stopped for approximately 8 seconds.",
    "On the date in question I was operating my vehicle in a manner consistent with applicable state and federal regulations when I was struck without provocation by another driver who was operating their vehicle in a negligent fashion.",
    "V1 driver, a 78-year-old male with passenger his elderly wife, was making a left turn from a stop sign onto Main St when V2 traveling east struck V1 on the driver side door. V1 driver stated visibility was good but he did not see V2.",
    "Both vehicles attempting to merge into single lane during construction. V1 had right of way per signage but V2 driver insisted she had been there first. Damage to both vehicles right front quarter panels. Police on scene.",
    "Three-vehicle crash on I-95 southbound. V1 braked suddenly for stopped traffic, V2 struck V1 in the rear, V3 struck V2 in the rear. V3 driver admitted to following too close. Minor injuries reported by V1 passenger; transported by EMS.",
    "Single-vehicle hydroplaning event on wet roadway. V1 driver lost control after passing through standing water at approximately 55 mph, struck the median barrier, and came to rest in the left lane. No other vehicles involved.",
    "V1 was parked legally on the right side of the street when struck by V2 backing out of a driveway. V2 driver did not check mirrors and was unaware of impact until pedestrian flagged him down. Damage to V1 driver door.",
    "V1 driver stated he was making a U-turn at a designated U-turn area when V2 traveling in the opposite direction struck V1 on the front passenger side. V2 driver claimed V1 entered the intersection on a yellow light.",
    "Rear-end collision at low speed in stop-and-go traffic. V1 came to a complete stop, V2 did not. Driver V2 stated 'the brakes felt soft' and admitted vehicle was overdue for service. No injuries.",
    "V1 was traveling east on Route 1 when a deer entered the roadway. V1 driver braked hard to avoid the deer and was struck in the rear by V2. V2 driver stated V1 'stopped for no reason' but witnesses confirmed deer presence.",
    "V1 driver was making a delivery and double-parked with hazards on. V2 driver, attempting to navigate around V1, struck V1 in the rear bumper. Both drivers exchanged information. Property damage only.",
    "V1 driver was changing lanes on the Turnpike when she struck V2 which was in her blind spot. Driver V1 admitted she did not check before merging and stated 'they came out of nowhere.' V2 driver had a child passenger; no injuries reported.",
    "Side-swipe collision on the ramp from Route 287 to I-78. Both drivers attempted to merge into the same lane. Damage along the entire passenger side of V1 and entire driver side of V2. Both vehicles drivable.",
    "V1, a commercial fleet vehicle, was making a right turn at a low-speed when the rear axle clipped a parked V2 in the adjacent lane. V1 driver did not realize contact had occurred until contacted by police several hours later via plate identification.",
    "V1 was stopped behind V2 at a stop sign. V2 driver, attempting to back up to make space, reversed into V1. V2 driver stated she 'didn't see V1 in the mirror.' Both drivers exited vehicles; no injuries.",
    "Multi-vehicle crash involving 4 vehicles in dense fog conditions on I-80 westbound near Exit 43. Visibility reported at less than 100 feet. Chain-reaction rear-end pattern. State police dispatched; lane closure for cleanup approximately 45 minutes.",
    "V1 driver attempted to pass V2 on the right shoulder during congested traffic. V2 driver, unaware of V1's approach, drifted onto the shoulder and contact occurred. Damage to right side of V2 and front of V1.",
    "V1 was in the process of parallel parking when V2 traveling in the same direction struck V1 in the left rear quarter panel. V2 driver claimed V1's turn signal was not functioning. V1 driver disputes.",
]


def load_in_code_narratives() -> list[str]:
    """The in-code corpus. Always available, no download required."""
    return list(NHTSA_LIKE_NARRATIVES)


def load_real_narratives(crss_csv_path: Path | str) -> list[str]:
    """Load free-text narratives from a real NHTSA CRSS CSV.

    Real CRSS files have a `NARRATIVE` field. If you've run
    `data/fetch_data.py --nhtsa`, point this at the extracted CSV.
    """
    p = Path(crss_csv_path)
    if not p.exists():
        raise FileNotFoundError(f"NHTSA CSV not found at {p}. Run data/fetch_data.py --nhtsa first.")
    out: list[str] = []
    with p.open(encoding="utf-8", errors="ignore") as f:
        reader = csv.DictReader(f)
        for row in reader:
            narrative = row.get("NARRATIVE") or row.get("narrative") or ""
            narrative = narrative.strip()
            if 80 < len(narrative) < 2000:  # filter junk and unreadable extremes
                out.append(narrative)
    return out


def random_narrative(seed: int | None = None) -> str:
    rng = random.Random(seed)
    return rng.choice(NHTSA_LIKE_NARRATIVES)


def generate_fnol_with_real_narrative(
    base_fnol: dict,
    narratives: list[str] | None = None,
    seed: int | None = None,
) -> dict:
    """Replace the synthetic incident_description with one from the corpus."""
    rng = random.Random(seed)
    pool = narratives or NHTSA_LIKE_NARRATIVES
    return {**base_fnol, "incident_description": rng.choice(pool)}
