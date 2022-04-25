# Python environment

The code you work on will run on a Python environment. Depending on what you installed
(Conda, pyenv, nothing), the ``python`` command can be provided by a variety of sources.

A Python interpreter will also come with its own Python environment. Normally, VS Code will
autodetect the Python environment suitable for your project. You can also tell VS Code what
environment to use.

Typing ``which python`` in a UNIX-like system shows you where the Python interpreter is located.

## Selecting a Python environment in VS Code

CTRL+SHIFT+P `Python: Select interpreter` should show a list of autodetected environments. O

ne can always select a `venv` that is not in the list.

This is the only VS Code setting that:

- won't be stored in the user `settings.json` file: indeed, the Python environment changes project by project

- won't be stored in the project `.vscode/settings.json` file: indeed, paths to Python environments change from computer to computer

Note that, sometimes, VS Code does not activate the proper Python environment in its Terminal tab.
This is due to the Terminal sometimes initializing before the Python VS Code extension,
see [this issue](https://github.com/microsoft/vscode-python/issues/15318).

## Level 1

The easy option is to use [Conda](https://docs.conda.io/en/latest/) to manage Python environments.
VS Code should detect Conda environments automatically. It will remember the Python environment
you select for each project you open.

Then, use ``pip install`` to add the different tools we will discuss to your environment.

## Level 2

In Level 2, we use Poetry, see {ref}`publishing2`. The Poetry-managed virtual environment is
detected by VS Code.

## Installing Jupyter notebooks support

The Python VS Code extension installs support for Jupyter notebooks by default, see [our explanation](../extensions.md).

However, one needs to install the `jupyterlab` PyPI package to use that support.

```bash
pip install jupyterlab
```

or 

```
poetry add --dev jupyterlab
```


## Extra reading

https://code.visualstudio.com/docs/python/environments


