"""Tests for GovernanceEngine."""
import pytest
from src.governanceengine import GovernanceEngine

def test_init():
    obj = GovernanceEngine()
    stats = obj.get_stats()
    assert stats["total_ops"] == 0

def test_operation():
    obj = GovernanceEngine()
    result = obj.register_model(input="test")
    assert result["processed"] is True
    assert result["operation"] == "register_model"

def test_multiple_ops():
    obj = GovernanceEngine()
    for m in ['register_model', 'assess_risk', 'check_compliance']:
        getattr(obj, m)(data="test")
    assert obj.get_stats()["total_ops"] == 3

def test_caching():
    obj = GovernanceEngine()
    r1 = obj.register_model(key="same")
    r2 = obj.register_model(key="same")
    assert r2.get("cached") is True

def test_reset():
    obj = GovernanceEngine()
    obj.register_model()
    obj.reset()
    assert obj.get_stats()["total_ops"] == 0

def test_stats():
    obj = GovernanceEngine()
    obj.register_model(x=1)
    obj.assess_risk(y=2)
    stats = obj.get_stats()
    assert stats["total_ops"] == 2
    assert "ops_by_type" in stats
