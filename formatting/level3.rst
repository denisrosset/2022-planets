Additional formatting/linting
=============================

You can add `pylint <https://pylint.pycqa.org/en/latest/>`_ to your workflow to catch common
errors/problems.

I only did it in my `configpile <https://github.com/denisrosset/configpile>`_ project, and
would only recommend using it if you are starting a project from scratch. Otherwise the list
of things to "correct" will probably overwhelm you.

``pylint`` tends to be opinionated and it takes time to mold the tool to one's own code style.

To enable ``pylint``, install it using ``poetry add --dev pylint``, and then activate it in
VS Code by adding the following to ``.vscode/settings.json``::

    "python.linting.pylintEnabled": true,
    
I use the following settings in ``pyproject.toml``::

    [tool.pylint.BASIC]

    variable-rgx = "[a-z_][a-z0-9_]{1,30}$" # to allow single character variable names

    [tool.pylint.messages_control]
    disable = [
    "assignment-from-none", # this is caught by mypy and has false positives
    "no-value-for-parameter", # this is caught by mypy and has false positives
    "unused-argument", # happens quite often in OOP hierarchies
    ]

