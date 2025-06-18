"""Fixtures."""

from pathlib import Path
from uuid import uuid4

import pytest

THIS_DIR = Path(__file__).parents[1]
PROJECT_DIR = (THIS_DIR / "../").resolve()


@pytest.fixture(scope="session")
def test_session_id() -> str:
    """Test session ID."""
    test_session_id = str(PROJECT_DIR.name) + str(uuid4())[:6]
    return test_session_id
