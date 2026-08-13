"""End-to-end test: build the bundled example project with the sphinx-build CLI."""

from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

import pytest

from conftest import ReadOutput

pytestmark = pytest.mark.e2e

example = Path(__file__).parent.parent / "examples" / "basic"


def test_build_example_project(tmp_path: Path, read_output: ReadOutput) -> None:
    project = tmp_path / "basic"
    shutil.copytree(example, project)
    result = subprocess.run(
        [sys.executable, "-m", "sphinx", "-M", "jekyll", "docs", "build"],
        cwd=project,
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stderr

    outdir = project / "build" / "jekyll"
    variables, body = read_output(outdir / "index.md")
    assert variables["docname"] == "index"
    assert variables["path"] == "/"
    assert variables["title"] == "Example Docs"
    assert "# Example Docs" in body

    variables, body = read_output(outdir / "pages" / "about.md")
    assert variables["docname"] == "pages/about"
    assert variables["path"] == "/pages-about"
    assert variables["title"] == "About"
    assert "```python" in body
