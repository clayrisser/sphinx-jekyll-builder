"""Sphinx builder that outputs Jekyll compatible markdown files with frontmatter."""

from __future__ import annotations

import re
from datetime import datetime, timezone
from typing import Any

import yaml
from docutils import nodes
from sphinx.application import Sphinx
from sphinx.locale import __
from sphinx_markdown_builder.builder import MarkdownBuilder
from sphinx_markdown_builder.translator import MarkdownTranslator

__version__ = "0.4.0"

__all__ = ["JekyllBuilder", "JekyllTranslator", "setup"]

kebab_case_words = re.compile(r"[A-Z]+(?=[A-Z][a-z])|[A-Z]?[a-z]+|[A-Z]+|[0-9]+")


def kebab_case(value: str) -> str:
    """Convert a string (e.g. a docname) to kebab-case."""
    return "-".join(
        match.group(0).lower() for match in kebab_case_words.finditer(value)
    )


def get_path(docname: str) -> str:
    """Convert a docname into a Jekyll permalink path."""
    return "/" + kebab_case("" if docname == "index" else docname)


class JekyllTranslator(MarkdownTranslator):
    """Markdown translator that prepends Jekyll YAML frontmatter."""

    def __init__(self, document: nodes.document, builder: JekyllBuilder) -> None:
        super().__init__(document, builder)
        self.jekyll_builder = builder

    def frontmatter(self) -> str:
        docname = self.jekyll_builder.current_doc_name or ""
        title_node = self.document.next_node(nodes.title)
        variables: dict[str, Any] = {
            "date": self.jekyll_builder.build_date,
            "docname": docname,
            "images": sorted(
                {str(node["uri"]) for node in self.document.findall(nodes.image)}
            ),
            "path": get_path(docname),
            "title": title_node.astext() if title_node is not None else docname,
        }
        return "---\n" + yaml.safe_dump(variables) + "---\n\n"

    def astext(self) -> str:
        return self.frontmatter() + super().astext()


class JekyllBuilder(MarkdownBuilder):
    """Markdown builder that emits Jekyll compatible files with frontmatter."""

    name = "jekyll"
    format = "jekyll"
    epilog = __("The jekyll files are in %(outdir)s.")

    default_translator_class = JekyllTranslator

    build_date: str

    def init(self) -> None:
        super().init()
        self.build_date = (
            datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
        )


def setup(app: Sphinx) -> dict[str, Any]:
    app.setup_extension("sphinx_markdown_builder")
    app.add_builder(JekyllBuilder)
    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
