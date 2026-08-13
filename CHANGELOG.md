# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [0.4.0] - 2026-08-12
### Changed
* modernized for current Sphinx (7.x/8.x/9.x) and Python (3.10+)
* rebased on sphinx-markdown-builder 0.6.x (the maintained fork)
* packaging migrated from setup.py to a uv-managed pyproject.toml
* `images` frontmatter now lists the images referenced by the document
  (previously it was always empty)

### Removed
* python 2 support
* munch and pydash dependencies

## [0.2.2] - 2019-25-01
### Changed
* updated sphinx-markdown-builder version

## [0.1.3] - 2018-12-03
### Added
* fixed python2 bug

## [0.1.0] - 2018-11-14
### Added
* title variable
* beta release

## [0.0.1] - 2018-11-14
### Added
* initial release
