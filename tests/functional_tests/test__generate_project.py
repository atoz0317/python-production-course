"""Test generate project."""

from pathlib import Path


def test__can_generate_project(project_dir: Path):
    """Test generate."""
    assert project_dir.exists()
