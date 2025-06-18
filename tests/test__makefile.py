import pytest


@pytest.fixture
def project(scope="session"):
    print("Setup")
    yield 1
    print("Teardown")


def test__linting_passes(project):
    print(project)
    assert False


def test__tests_pass(): ...


def test__install_succeeds(): ...
