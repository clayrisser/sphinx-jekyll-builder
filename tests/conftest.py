"""Shared fixtures for the sphinx-jekyll-builder test suite."""

from __future__ import annotations

import base64
from pathlib import Path
from typing import Any, Callable

import pytest
import yaml
from sphinx.application import Sphinx

default_conf = 'project = "Test"\nextensions = ["sphinx_jekyll_builder"]\n'

BuildProject = Callable[..., Path]
ReadOutput = Callable[[Path], "tuple[dict[str, Any], str]"]


@pytest.fixture
def build_project(tmp_path: Path) -> BuildProject:
    """Build a Sphinx project through the jekyll builder and return the outdir."""

    def _build(sources: dict[str, str | bytes], conf: str = default_conf) -> Path:
        srcdir = tmp_path / "src"
        outdir = tmp_path / "out"
        srcdir.mkdir(exist_ok=True)
        (srcdir / "conf.py").write_text(conf, encoding="utf-8")
        for name, content in sources.items():
            target = srcdir / name
            target.parent.mkdir(parents=True, exist_ok=True)
            if isinstance(content, bytes):
                target.write_bytes(content)
            else:
                target.write_text(content, encoding="utf-8")
        app = Sphinx(
            srcdir=str(srcdir),
            confdir=str(srcdir),
            outdir=str(outdir),
            doctreedir=str(tmp_path / "doctrees"),
            buildername="jekyll",
            status=None,
        )
        app.build()
        return outdir

    return _build


@pytest.fixture
def read_output() -> ReadOutput:
    """Split an emitted markdown file into parsed frontmatter and body."""

    def _read(path: Path) -> tuple[dict[str, Any], str]:
        text = path.read_text(encoding="utf-8")
        assert text.startswith("---\n"), f"missing frontmatter in {path}"
        frontmatter, body = text[len("---\n") :].split("\n---\n", 1)
        return yaml.safe_load(frontmatter), body

    return _read


@pytest.fixture
def png_pixel() -> bytes:
    """A valid 1x1 transparent PNG."""
    return base64.b64decode(
        "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJ"
        "AAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg=="
    )
