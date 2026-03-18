"""Tests for AiGovernanceToolkit."""
from src.core import AiGovernanceToolkit
def test_init(): assert AiGovernanceToolkit().get_stats()["ops"] == 0
def test_op(): c = AiGovernanceToolkit(); c.analyze(x=1); assert c.get_stats()["ops"] == 1
def test_multi(): c = AiGovernanceToolkit(); [c.analyze() for _ in range(5)]; assert c.get_stats()["ops"] == 5
def test_reset(): c = AiGovernanceToolkit(); c.analyze(); c.reset(); assert c.get_stats()["ops"] == 0
def test_service_name(): c = AiGovernanceToolkit(); r = c.analyze(); assert r["service"] == "ai-governance-toolkit"
