Level 2: Formatting project by project
--------------------------------------

In Level 2, projects are managed using Poetry, and poetry creates a ``pyproject.toml`` file in the
root project folder where different settings are provided.

Install the tools using::

    poetry add --dev black
    poetry add --dev isort

The ``--dev`` flag signals that users of your code do not need those dependencies merely to run it.

The ``pyproject.toml`` is a standard place to put Black parameters in Python projects, so
that the settings will apply when using other IDEs, or when running
Black from the command line.

Add the following sections to your ``pyproject.toml`` file::

   [tool.black]
   ...
   line-length = 99
   ...

   [tool.isort]
   ...
   line_length = 99
   ...


To trigger the use of ``black`` and ``isort`` in VS Code when saving files, add the following
to the ``.vscode/settings.json`` file in your project folder (*not* your user settings, see :ref:`settings`)::

    "editor.rulers": [99],
    "editor.formatOnSave": true,
    "python.formatting.provider": "black",
    "[python]": {
        "editor.codeActionsOnSave": {
            "source.organizeImports": true
        }
    },
