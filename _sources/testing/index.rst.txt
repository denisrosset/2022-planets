Testing
=======

I'll provide just a few pointers.

Level 1
-------

In level 1, provide Jupyter notebooks that can be run by the end user, or simply Python scripts
with assertions.

Level 2
-------

Use Pytest. Much nicer syntax.

Install it:

.. code-block::

    poetry add --dev pytest

Put your tests in a ``tests/`` directory.

Add the following to your ``.vscode/settings.json`` file:

.. code-block:: json

    "python.testing.unittestEnabled": false,
    "python.testing.pytestEnabled": true,

Add examples in your Python functions using `doctests <https://docs.pytest.org/en/6.2.x/doctest.html>`_,
but following the `Google syntax <https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html>`_.

Add the following to your ``pyproject.toml`` file:

.. code-block:: toml

    [tool.pytest.ini_options]
    addopts = [
    "--tb=short",
    "--doctest-modules"
    ]

    doctest_optionflags = ['NORMALIZE_WHITESPACE', 'IGNORE_EXCEPTION_DETAIL', 'ELLIPSIS']

Tests can be run directly from the VS Code IDE.

Level 3
-------

Run tests automatically using GitHub workflows (TBD).