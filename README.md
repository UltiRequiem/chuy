# Chuy

[![PyPi Version](https://img.shields.io/pypi/v/chuy)](https://pypi.org/project/chuy)

Create aliases for long commands and speed up your workflow, inspired by tools like
[yarn](https://github.com/yarnpkg/berry) and [npm](https://github.com/npm/cli).

Although Chuy is written in Python, it can be used with projects written in any language.

## Install

You can install [Chuy](https://pypi.org/project/chuy) from PyPI like any other
package:

```bash
pip install chuy
```

To get the lastest version:

```bash
pip install git+https://github.com/UltiRequiem/chuy
```

## Example Configuration file

Using [`JSON`](./chuy.json) format:

```json
{
  "format": "poetry run black .",
  "lint": "poetry run pylint chuy tests",
  "tests": "poetry run pytest",
  "package": "poetry build && poetry publish"
}
```

Using [`TOML`](./chuy.toml) format:

```toml
[chuy]
format = "poetry run black ."
lint = "poetry run pylint chuy tests"
tests = "poetry run pytest"
package = "poetry build && poetry publish"
```

Using the [`pyproject.toml`](./pyproject.toml) file:

```toml
[tool.chuy]
format = "poetry run black ."
lint = "poetry run pylint chuy tests"
tests = "poetry run pytest"
package = "poetry build && poetry publish"
```

The configuration file usually goes in the root of your project,
but it can be placed anywhere.

## Usage

Once you've defined your commands in the
[configuration file](#example-configuration-file), you can now execute them as
follows:

```bash
chuy format
 $ poetry run black .
 ....
```

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

## Tricks

If you don't specify a command, Chuy will display a menu listing
all available commands. You can then select one or more commands to execute.

## Screenshots

Normal usage:

![Screenshot Normal Usage](https://i.imgur.com/sOu86gu.png)

When you don't specify a command:

![Screenshot Menu](https://i.imgur.com/nFd4Bz9.png)

## License

This project is licensed under the [MIT License](./LICENSE).
