.. _publishing2:

Level 2: Use Poetry and Python virtual environments
===================================================

Poetry has a few advantages:

* It assembles information about the project in a single 
  `pyproject.toml <https://python-poetry.org/docs/pyproject/>`_ file

* It manages dependencies and has a constraint solver for the dependency versions.

* It updates, installs, removes dependencies from the virtual environment linked to the project.

Before you install Poetry, be sure to read :ref:`python_versions`.

Install Poetry
--------------

Poetry is a self-contained command-line tool. Follow the instructions at
`<https://python-poetry.org/docs/#installation>`_. There should not be surprises.

Prepare the project environment with ``python -m venv .venv``
-------------------------------------------------------------

In your project folder, run ``python -m venv .venv`` to create a virtual environment in a ``.venv``
subfolder. This subfolder will be recognized both by Poetry and VS Code when looking for 
environments.

You can set `virtualenvs.in-project <https://python-poetry.org/docs/configuration/#virtualenvsin-project>`_
to ``true`` to perform this step automatically. Run in the shell::

  poetry config settings.virtualenvs.in-project true

Initialize the Poetry configuration
-----------------------------------

In your project folder, run ``poetry init``, which will interactively ask you basic information
about your project.

Then run ``poetry update`` to resolve dependencies and create or update the ``poetry.lock`` file.

The command ``poetry install``, on the other hand, installs/removes Python dependencies in the
virtual environment so that they match exactly what is specified in the ``poetry.lock`` file.

Should you distribute the ``poetry.lock`` files to users, or should you avoid storing it in the
Git repository (using `.gitignore <https://git-scm.com/docs/gitignore>`_)?

* If you are writing a Python library that will be integrated in other projects, do not distribute
  the ``poetry.lock`` file; instead, add it to ``.gitignore``.

* If your users will run your code directly, *do* distribute the ``poetry.lock`` file so that
  their virtual environment will match exactly yours.

To run things in the proper virtual environment
-----------------------------------------------

VS Code will normally run/debug code and open terminals in the ``.venv`` Poetry-managed virtual
environment. If you are running things from the command-line, either do:

* Type ``poetry shell`` to drop in a shell with the virtual environment activated

* Type ``poetry run ipython myscript.py`` or ``poetry run mypy``, ..., to run commands inside
  the virtual environment.

Folder structure
----------------

I use the following folder structure. See `configpile <https://github.com/denisrosset/configpile>`_
for an example.

- ``.github/workflows`` contains the trigger that builds the documentation website.
- ``.vscode`` contains the VS Code settings specific to the project.
- ``docs`` is the Sphinx documentation folder, with ``docs/Makefile`` enabling the 
  documentation build
- ``docs/source`` contains the Sphinx source, including ``conf.py``
- ``src/PROJECTNAME`` contains the module source code.

  It is good practice to put the project under a ``src`` subfolder. Do not worry: Python
  will find your package source files when importing it because ``poetry install`` writes a special
  ``.pth`` file in the ``site-packages`` of your virtual environment.

- ``tests`` for unit tests, will be discovered automatically by VS Code and pytest

Python modules
--------------

I recommend keeping your source files < 1000 lines of code long.