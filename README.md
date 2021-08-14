# Chuy

![CodeQL](https://github.com/UltiRequiem/chuy/workflows/CodeQL/badge.svg)
![PyTest](https://github.com/UltiRequiem/chuy/workflows/PyTest/badge.svg)
![Pylint](https://github.com/UltiRequiem/chuy/workflows/Pylint/badge.svg)
[![Code Style](https://img.shields.io/badge/Code%20Style-Black-000000.svg)](https://github.com/psf/black)
[![PyPi Version](https://img.shields.io/pypi/v/chuy)](https://pypi.org/project/chuy)
![Repo Size](https://img.shields.io/github/repo-size/ultirequiem/chuy?style=flat-square&label=Repo)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
![Lines of Code](https://img.shields.io/tokei/lines/github.com/UltiRequiem/chuy?color=blue&label=Total%20Lines)

## Example configuration file

```json
{
  "format": "poetry run black .",
  "lint": "poetry run pylint chuy tests",
  "test": "poetry run pytest",
  "package": "poetry build && poetry publish"
}
```

## Usage

```bash
chuy format  # {"format": "poetry run black ."} on chuy.json
```
