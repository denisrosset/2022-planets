Level 1: Formatting defaults for all your projects
==================================================

Install the required tools in your Python or Conda environment. Note that ``isort`` and
``black`` have minimal dependencies and should not break your setup.

::

    pip install isort
    pip install black

In the user ``settings.json`` (see :ref:`settings`), add::

    "editor.rulers": [99],
    "editor.formatOnSave": true,
    "python.formatting.provider": "black",
    "python.formatting.blackArgs": ["--line-length=99"],
    "python.sortImports.args": [
        "--profile", "black",
        "--line-length", "99"
    ],
    "[python]": {
        "editor.codeActionsOnSave": {
            "source.organizeImports": true
        }
    },

This will provide defaults for all the Python projects you edit. Replace ``99`` by your prefered
line length.

Skip the ``editor.rulers`` setting if you do not want an indication of the line length in the
editor.
