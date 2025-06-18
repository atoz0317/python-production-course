"""Project directory fixture."""

import shutil
import subprocess
from pathlib import Path
from typing import Iterator
from uuid import uuid4

import pytest

from tests.utils.project import (
    generate_project,
    initialize_git_repo,
)


@pytest.fixture(scope="session")
def project_dir() -> Iterator[Path]:
    """Project directory."""
    test_session_id = generate_test_session_id()
    template_values = {"repo_name": f"test-repo-{test_session_id}"}
    generated_repo_dir = generate_project(template_values, test_session_id=test_session_id)
    try:
        initialize_git_repo(generated_repo_dir)
        subprocess.run(["make", "lint-ci"], cwd=generated_repo_dir, check=False)
        yield generated_repo_dir
    finally:
        shutil.rmtree(path=generated_repo_dir)


def generate_test_session_id() -> str:
    """Generate session ID."""
    test_session_id = str(uuid4())[:6]
    return test_session_id
