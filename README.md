# sphinx-jekyll-builder

[![PyPI](https://img.shields.io/pypi/v/sphinx-jekyll-builder.svg?style=flat-square)](https://pypi.org/project/sphinx-jekyll-builder)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/sphinx-jekyll-builder.svg?style=flat-square)](https://pypi.org/project/sphinx-jekyll-builder)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/sphinx-jekyll-builder.svg?style=flat-square)](https://pypi.org/project/sphinx-jekyll-builder)
[![GitHub stars](https://img.shields.io/github/stars/codejamninja/sphinx-jekyll-builder.svg?style=flat-square&label=Stars)](https://github.com/codejamninja/sphinx-jekyll-builder)

> sphinx builder that outputs jekyll compatible markdown files with frontmatter

Please ★ this repo if you found it useful ★ ★ ★


## Features

* Generates jekyll


## Installation

```sh
pip3 install sphinx-jekyll-builder
```


## Dependencies

* [Python 3](https://www.python.org)


## Usage

Load extension in configuration.

_conf.py_
```py
extensions = [
    'sphinx_jekyll_builder'
]
```

If using [recommonmark](https://github.com/rtfd/recommonmark), make sure you
explicitly ignore the build files as they will conflict with the system.

_conf.py_
```py
exclude_patterns = [
    'build/*'
]
```

Build jekyll files with Makefile

```sh
make jekyll
```

Build jekyll files with `sphinx-build` command

```sh
cd docs
sphinx-build -M jekyll ./ build
```


## Support

Submit an [issue](https://github.com/codejamninja/sphinx-jekyll-builder/issues/new)


## Screenshots

[Contribute](https://github.com/codejamninja/sphinx-jekyll-builder/blob/master/CONTRIBUTING.md) a screenshot


## Contributing

Review the [guidelines for contributing](https://github.com/codejamninja/sphinx-jekyll-builder/blob/master/CONTRIBUTING.md)


## License

[MIT License](https://github.com/codejamninja/sphinx-jekyll-builder/blob/master/LICENSE)

[Jam Risser](https://codejam.ninja) © 2018


## Changelog

Review the [changelog](https://github.com/codejamninja/sphinx-jekyll-builder/blob/master/CHANGELOG.md)


## Credits

* [Jam Risser](https://codejam.ninja) - Author
* [Matthew Brett](https://github.com/matthew-brett/nb2plots/blob/master/nb2plots/doctree2md.py) - doctree2md


## Support on Liberapay

A ridiculous amount of coffee ☕ ☕ ☕ was consumed in the process of building this project.

[Add some fuel](https://liberapay.com/codejamninja/donate) if you'd like to keep me going!

[![Liberapay receiving](https://img.shields.io/liberapay/receives/codejamninja.svg?style=flat-square)](https://liberapay.com/codejamninja/donate)
[![Liberapay patrons](https://img.shields.io/liberapay/patrons/codejamninja.svg?style=flat-square)](https://liberapay.com/codejamninja/donate)
