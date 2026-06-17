"""
Pytest configuration for REM-Evo test suite.
"""

import pytest
from typing import Dict, List, Set


@pytest.fixture
def basic_theory():
    """Basic theory structure for testing."""
    return {
        "name": "test_theory",
        "axioms": ["a1", "a2"],
        "derivations": ["d1", "d2"],
        "predictions": ["p1"],
        "failures": ["f1"]
    }


@pytest.fixture
def theory_set():
    """Set of diverse theories."""
    return [
        {"name": "t1", "axioms": ["ax1", "ax2"], "predictions": ["pred1"]},
        {"name": "t2", "axioms": ["ax3"], "predictions": ["pred2", "pred3"]},
        {"name": "t3", "axioms": ["ax1", "ax4"], "predictions": ["pred1"]}
    ]


@pytest.fixture
def entropy_function():
    """Fixture for entropy function."""
    return {
        "type": "recursive_entropy",
        "measure": "elimination_capacity"
    }


@pytest.fixture
def elimination_trace():
    """Fixture for elimination traces."""
    return [
        {"iteration": 1, "theory": "t1", "eliminated": False, "work": 0.3},
        {"iteration": 2, "theory": "t2", "eliminated": True, "work": 0.6},
        {"iteration": 3, "theory": "t3", "eliminated": False, "work": 0.2}
    ]


def pytest_configure(config):
    """Register custom markers."""
    config.addinivalue_line("markers", "unit: fast unit tests")
    config.addinivalue_line("markers", "integration: integration tests")
    config.addinivalue_line("markers", "slow: slow tests")
    config.addinivalue_line("markers", "rem_evo: REM-Evo specific tests")
