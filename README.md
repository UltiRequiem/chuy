# Chuy

![CodeQL](https://github.com/UltiRequiem/chuy/workflows/CodeQL/badge.svg)
![PyTest](https://github.com/UltiRequiem/chuy/workflows/PyTest/badge.svg)
![Pylint](https://github.com/UltiRequiem/chuy/workflows/Pylint/badge.svg)
[![Code Style](https://img.shields.io/badge/Code%20Style-Black-000000.svg)](https://github.com/psf/black)
[![PyPi Version](https://img.shields.io/pypi/v/chuy)](https://pypi.org/project/chuy)
![Repo Size](https://img.shields.io/github/repo-size/ultirequiem/chuy?style=flat-square&label=Repo)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
![Lines of Code](https://img.shields.io/tokei/lines/github.com/UltiRequiem/chuy?color=blue&label=Total%20Lines)

Set alias to long commands and speed up your workflow.
Chuy is inspired in tools like [yarn](https://yarnpkg.com) and [npm](https://github.com/npm/cli).

Although Chuy is written in Python, it can be used for projects of any language,
and even folders that are not projects!

## Example Configuration file

```json
{
  "format": "poetry run black .",
  "lint": "poetry run pylint chuy tests",
  "tests": "poetry run pytest",
  "package": "poetry build && poetry publish"
}
```

This configuration must be in a [`chuy.json`](./chuy.json) file.
Usually this file goes in the root of your project but it can really go anywhere.

## Usage

After having defined the commands in the [chuy.json](./chuy.json) file,
you can now execute them as follows:

```bash
chuy format
 $ poetry run black .
 ....
```

This varies depending on the commands you
have written in the [chuy file](#example-configuration-file).

```bash
chuy lint
 $ poetry run pylint chuy tests
 ....
```

You can also pass multiple commands:

```bash
chuy lint format tests
 $ poetry run pylint chuy tests
 ....

 $ poetry run black .
 ....

 $ poetry run pytest
 ....
```

### License

Chuy is licensed under the [MIT License](./LICENSE).
