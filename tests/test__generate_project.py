import json
import shutil
import subprocess
from copy import deepcopy
from pathlib import Path
from typing import Iterator

import pytest

THIS_DIR = Path(__file__).parent
PROJECT_DIR = (THIS_DIR / "../").resolve()


@pytest.fixture
def project_dir() -> Iterator[Path]:
    template_values = {"repo_name": "test-repo"}
    generated_repo_dir = generate_project(template_values)
    yield generated_repo_dir
    shutil.rmtree(path=generated_repo_dir)


def generate_project(template_values: dict[str, str]):
    template_values = deepcopy(template_values)
    cookiecutter_config = {"default_context": template_values}
    cookiecutter_config_fpath = PROJECT_DIR / "tests/cookiecutter.json"

    cookiecutter_config_fpath.write_text((json.dumps(cookiecutter_config)))

    cmd = [
        "cookiecutter",
        str(PROJECT_DIR),
        "--output-dir",
        str(PROJECT_DIR / "sample"),
        "--no-input",
        "--config-file",
        str(cookiecutter_config_fpath),
    ]
    print("COMMAND: ", " ".join(cmd))
    subprocess.run(cmd, check=True)

    generated_repo_dir = PROJECT_DIR / "sample" / template_values["repo_name"]

    return generated_repo_dir


def test__can_generate_project(project_dir: Path):
    assert project_dir.exists()
