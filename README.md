# sphinx-jekyll-builder

[![PyPI](https://img.shields.io/pypi/v/sphinx-jekyll-builder.svg?style=flat-square)](https://pypi.org/project/sphinx-jekyll-builder)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/sphinx-jekyll-builder.svg?style=flat-square)](https://pypi.org/project/sphinx-jekyll-builder)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/sphinx-jekyll-builder.svg?style=flat-square)](https://pypi.org/project/sphinx-jekyll-builder)

![](assets/sphinx-jekyll-builder.png)

> sphinx builder that outputs jekyll compatible markdown files with frontmatter

Please ★ this repo if you found it useful ★ ★ ★

## Features

* Generates markdown
* Supports frontmatter
* Compatible with [jekyll](https://jekyllrb.com)
* Compatible with [gatsby](https://www.gatsbyjs.org/)

## Installation

```sh
pip install sphinx-jekyll-builder
```

## Dependencies

* [Python 3](https://www.python.org) (3.10 or newer)
* [Sphinx](https://www.sphinx-doc.org) 7.x or newer

## Usage

Load extension in configuration.

_conf.py_

```py
extensions = [
    'sphinx_jekyll_builder'
]
```

Build jekyll files with the `sphinx-build` command

```sh
cd docs
sphinx-build -M jekyll ./ build
```

The generated markdown lands in `build/jekyll/`. Every file starts with a YAML
frontmatter block:

```md
---
date: '2026-08-12T17:30:40.529Z'
docname: guide/gettingStarted
images: []
path: /guide-getting-started
title: Getting Started
---

# Getting Started
```

| variable  | description                                              |
| --------- | -------------------------------------------------------- |
| `date`    | build timestamp (ISO 8601, JavaScript compatible)        |
| `docname` | the sphinx docname                                       |
| `images`  | images referenced by the document                        |
| `path`    | kebab-case permalink derived from the docname            |
| `title`   | the document title (falls back to the docname)           |

A ready-to-build sample project lives in [examples/basic](examples/basic).

## Development

```sh
make prepare  # one-time machine setup (asdf toolchain + uv sync)
make build    # build sdist + wheel into dist/
make test     # unit tests with coverage
make test/e2e # build the example project through the sphinx-build CLI
make format   # black
make lint     # black --check + basedpyright
```

## Support

Submit an [issue](https://gitlab.com/bitspur/misc/sphinx-jekyll-builder/-/issues/new)

## Contributing

Review the [guidelines for contributing](CONTRIBUTING.md)

## License

[MIT License](LICENSE)

[Clay Risser](https://clayrisser.com) © 2018 - 2026

## Changelog

Review the [changelog](CHANGELOG.md)

## Credits

* [Clay Risser](https://clayrisser.com) - Author
* [Matthew Brett](https://github.com/matthew-brett/nb2plots/blob/master/nb2plots/doctree2md.py) - doctree2md
* [Liran Funaro](https://github.com/liran-funaro/sphinx-markdown-builder) - sphinx-markdown-builder
