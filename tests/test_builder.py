"""Builds small Sphinx projects through the jekyll builder and checks the output."""

from __future__ import annotations

import re

from conftest import BuildProject, ReadOutput

index_rst = """Hello World
===========

Some paragraph with **bold** text.

.. code-block:: python

   print("hi")

.. toctree::
   :hidden:

   guide/gettingStarted
"""

nested_rst = """Getting Started
===============

A nested page.
"""


def test_writes_markdown_with_frontmatter(
    build_project: BuildProject, read_output: ReadOutput
) -> None:
    outdir = build_project(
        {"index.rst": index_rst, "guide/gettingStarted.rst": nested_rst}
    )
    variables, body = read_output(outdir / "index.md")
    assert variables["docname"] == "index"
    assert variables["title"] == "Hello World"
    assert variables["path"] == "/"
    assert variables["images"] == []
    assert re.fullmatch(
        r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z", variables["date"]
    )
    assert "# Hello World" in body
    assert "**bold**" in body
    assert 'print("hi")' in body


def test_nested_docnames_get_kebab_case_paths(
    build_project: BuildProject, read_output: ReadOutput
) -> None:
    outdir = build_project(
        {"index.rst": index_rst, "guide/gettingStarted.rst": nested_rst}
    )
    variables, body = read_output(outdir / "guide" / "gettingStarted.md")
    assert variables["docname"] == "guide/gettingStarted"
    assert variables["path"] == "/guide-getting-started"
    assert variables["title"] == "Getting Started"
    assert "# Getting Started" in body


def test_images_are_listed_in_frontmatter(
    build_project: BuildProject, read_output: ReadOutput, png_pixel: bytes
) -> None:
    outdir = build_project(
        {
            "index.rst": "Pics\n====\n\n.. image:: images/pixel.png\n",
            "images/pixel.png": png_pixel,
        }
    )
    variables, body = read_output(outdir / "index.md")
    assert variables["images"] == ["images/pixel.png"]
    assert "![image](images/pixel.png)" in body


def test_title_falls_back_to_docname(
    build_project: BuildProject, read_output: ReadOutput
) -> None:
    outdir = build_project({"index.rst": "no title here, just a paragraph\n"})
    variables, _body = read_output(outdir / "index.md")
    assert variables["title"] == "index"


def test_builder_loads_via_entry_point(
    build_project: BuildProject, read_output: ReadOutput
) -> None:
    # No extensions in conf.py: sphinx must discover the builder entry point.
    outdir = build_project({"index.rst": "Hi\n==\n"}, conf='project = "Test"\n')
    variables, _body = read_output(outdir / "index.md")
    assert variables["title"] == "Hi"
