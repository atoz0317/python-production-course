# pylint: disable=all

"""Project."""

import json
import subprocess
from copy import deepcopy
from pathlib import Path
from typing import Dict

PROJECT_DIR = (Path(__file__).parents[1] / "../").resolve()


def initialize_git_repo(repo_dir: Path):
    """Initialize git repo."""
    subprocess.run(["git", "init"], cwd=repo_dir, check=True)
    subprocess.run(["git", "branch", "-M", "main"], cwd=repo_dir, check=True)
    subprocess.run(["git", "add", "--all"], cwd=repo_dir, check=True)
    subprocess.run(["git", "commit", "-m", "'feat: initial commit by pytest'"], cwd=repo_dir, check=True)


def generate_project(template_values: Dict[str, str], test_session_id: str):
    """Generate project."""
    template_values = deepcopy(template_values)
    cookiecutter_config = {"default_context": template_values}
    cookiecutter_config_fpath = PROJECT_DIR / f"tests/cookiecutter-{test_session_id}.json"

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
