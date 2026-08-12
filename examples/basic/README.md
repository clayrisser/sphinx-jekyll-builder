# basic example

A minimal Sphinx project wired up to the jekyll builder.

Build it:

```sh
pip install sphinx-jekyll-builder
sphinx-build -M jekyll docs build
```

The generated markdown files (with Jekyll frontmatter) land in `build/jekyll/`.
