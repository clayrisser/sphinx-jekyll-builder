# Contributing

We accept contributions of every kind: documentation, code, artwork. Any help is greatly
appreciated. This document contains everything needed to get started with your first contribution.


## Contributing Code

We keep the source code on [GitLab](https://gitlab.com/bitspur/misc/sphinx-jekyll-builder) and take
contributions through merge requests.

For smaller patches and bug fixes just go ahead and either report an issue or submit a merge
request.

It is usually a good idea to discuss major changes with the developers, this will help us
determine whether the contribution would be a good fit for the project and if it is likely to be
accepted. There's nothing worse than seeing your hard work being rejected because it falls outside
of the scope of the project.

Make sure your editor respects the [EditorConfig](http://editorconfig.org) configuration file we
put at the root of the repository.

Our git workflow boils down to:

* The `main` branch is always stable and deployable.
* To work on something new, branch off `main` and give the new branch a descriptive name (e.g.:
  `sort-packages-by-name`, `issue-32`, etc).
* Regularly __rebase__ that branch against `main` and push your work to a branch with the same
  name on the server.
* When you need feedback, help or think you are ready, submit a merge request.
* Once the branch has been merged (or rebased) into `main`, delete it from both your local and
  remote repository.

We invite you to follow
[these guidelines](http://who-t.blogspot.de/2009/12/on-commit-messages.html) to write useful
commit messages.

Additionally, you don't need to add entries to the [CHANGELOG.md](CHANGELOG.md) file, this is our
responsibility.


## Development Environment

The project is managed with [uv](https://docs.astral.sh/uv/) and a Makefile:

```sh
make prepare   # one-time machine setup (asdf toolchain + uv sync)
make test      # unit tests with coverage
make test/e2e  # end-to-end build of the example project
make format    # black
make lint      # black --check + basedpyright
```


## Reading List

* [Keep a Changelog](http://keepachangelog.com/)
* [On Commit Messages](http://who-t.blogspot.de/2009/12/on-commit-messages.html)
* [Semantic Versioning](http://semver.org/)
