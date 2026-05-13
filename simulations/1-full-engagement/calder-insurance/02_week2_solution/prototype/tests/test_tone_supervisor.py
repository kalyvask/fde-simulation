"""Unit tests for the ToneSupervisorAgent.

These tests exercise the deterministic mock-mode grader. The LLM-as-judge path
is exercised end-to-end by the eval harness with ANTHROPIC_API_KEY set.
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

# Force mock mode for these tests so they don't depend on an API key
os.environ["ANTHROPIC_API_KEY"] = ""

sys.path.insert(0, str(Path(__file__).parent.parent))

from calder_agent.agents.tone_supervisor import ToneSupervisorAgent


def make_agent_in_mock_mode():
    a = ToneSupervisorAgent()
    a.client = None
    a.mode = "mock"
    return a


def test_passes_well_formed_draft():
    inputs = {
        "draft_text": (
            "Hi Mr. Patel, I've received your claim about the fender bender at the "
            "Edison distribution center. Here's what happens next: I'll have an estimate "
            "appointment scheduled for you within 10 business days. If anything changes, "
            "please reach Sarah Cole at 555-0100."
        ),
        "claimant_name": "Mr. Patel",
        "incident_description": "Fender bender at the UPS Edison NJ distribution center.",
        "timeline_days": 10,
        "contact_name": "Sarah Cole, Calder Claims",
        "contact_phone": "555-0100",
    }
    agent = make_agent_in_mock_mode()
    result = agent.run(inputs)
    assert result.output["overall_pass"], result.output
    assert all(e["pass"] for e in result.output["elements"].values())


def test_fails_when_name_missing():
    inputs = {
        "draft_text": (
            "Hi there, your claim was received. Estimate within 10 business days. "
            "Call Sarah Cole at 555-0100."
        ),
        "claimant_name": "Mr. Patel",
        "incident_description": "Fender bender at the UPS Edison NJ distribution center.",
        "timeline_days": 10,
        "contact_name": "Sarah Cole, Calder Claims",
        "contact_phone": "555-0100",
    }
    agent = make_agent_in_mock_mode()
    result = agent.run(inputs)
    assert not result.output["overall_pass"]
    assert not result.output["elements"]["name_correct"]["pass"]


def test_fails_when_timeline_missing():
    inputs = {
        "draft_text": (
            "Hi Mr. Patel, your claim about the Edison distribution center incident "
            "was received. We'll review and reach out shortly. Sarah Cole, 555-0100."
        ),
        "claimant_name": "Mr. Patel",
        "incident_description": "Fender bender at the UPS Edison NJ distribution center.",
        "timeline_days": 10,
        "contact_name": "Sarah Cole, Calder Claims",
        "contact_phone": "555-0100",
    }
    agent = make_agent_in_mock_mode()
    result = agent.run(inputs)
    assert not result.output["overall_pass"]
    assert not result.output["elements"]["plannable_timeline"]["pass"]


def test_fails_when_person_to_call_missing():
    inputs = {
        "draft_text": (
            "Hi Mr. Patel, your claim about the Edison distribution center "
            "incident was received. We will review within 10 business days."
        ),
        "claimant_name": "Mr. Patel",
        "incident_description": "Fender bender at the UPS Edison NJ distribution center.",
        "timeline_days": 10,
        "contact_name": "Sarah Cole, Calder Claims",
        "contact_phone": "555-0100",
    }
    agent = make_agent_in_mock_mode()
    result = agent.run(inputs)
    assert not result.output["overall_pass"]
    assert not result.output["elements"]["person_to_call"]["pass"]


def test_fails_form_letter_template():
    """A BPO-style form letter should fail multiple elements."""
    inputs = {
        "draft_text": (
            "Dear Customer, We have received your claim. A representative will "
            "contact you within 30 days. Reference number: CL-2025-NJ-44218."
        ),
        "claimant_name": "Mr. Patel",
        "incident_description": "Fender bender at the UPS Edison NJ distribution center.",
        "timeline_days": 10,
        "contact_name": "Sarah Cole, Calder Claims",
        "contact_phone": "555-0100",
    }
    agent = make_agent_in_mock_mode()
    result = agent.run(inputs)
    assert not result.output["overall_pass"]
    failed = [k for k, v in result.output["elements"].items() if not v["pass"]]
    # Form letter should fail at least name + claim_summarized + person_to_call
    assert "name_correct" in failed
    assert "person_to_call" in failed
