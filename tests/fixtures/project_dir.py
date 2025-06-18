import shutil
import sys
from pathlib import Path
from typing import Iterator

import pytest

from tests.utils.project import generate_project


@pytest.fixture
def project_dir() -> Iterator[Path]:
    template_values = {"repo_name": "test-repo"}
    generated_repo_dir = generate_project(template_values)
    yield generated_repo_dir
    shutil.rmtree(path=generated_repo_dir)
