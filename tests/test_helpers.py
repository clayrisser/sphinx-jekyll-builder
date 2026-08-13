"""Unit tests for the docname to permalink helpers."""

from __future__ import annotations

import pytest

from sphinx_jekyll_builder import get_path, kebab_case


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        ("index", "index"),
        ("gettingStarted", "getting-started"),
        ("getting_started", "getting-started"),
        ("guide/gettingStarted", "guide-getting-started"),
        ("Foo Bar", "foo-bar"),
        ("HTTPServer", "http-server"),
        ("release-1.2", "release-1-2"),
        ("", ""),
    ],
)
def test_kebab_case(value: str, expected: str) -> None:
    assert kebab_case(value) == expected


@pytest.mark.parametrize(
    ("docname", "expected"),
    [
        ("index", "/"),
        ("about", "/about"),
        ("guide/index", "/guide-index"),
        ("guide/gettingStarted", "/guide-getting-started"),
    ],
)
def test_get_path(docname: str, expected: str) -> None:
    assert get_path(docname) == expected
