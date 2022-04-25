Typing and modularizing code
============================

The most efficient way to document code is to use code.

* Use descriptive variable names. Bump the line length if needed. Formerly, memory was scarce,
  and thus older codes use single letter variable names.

* Split your code into functions. This is required when the length reaches more than a few
  hundred lines of codes: it's best to be able to see a whole function in one or two screen
  heights.

  How much you split is a matter of taste. In the example I show, it's not necessarily true
  that the end result is more readable.

* Group related data, especially configuration settings, in dicts or (better) dataclasses.
  
  Use type annotations to describe what the variables are.

* Dinstinguish between mutable and immutable data.

In this section of this website, we show how a few of those features can be applied to a simple
root-finding code.

Typing 101
----------

Type annotations are a "language inside the language". At runtime, they are mostly ignored,
except by a few modern libraries that explicitly exploit them (but you'll know when you
cross that bridge).

Thus, type annotations can be added to your code without changing its runtime behavior *at all*.
Compared to compiled languages, you keep the Python strenght of "having one part of the code
broken while running the rest".

As you annotate your code, you'll reap compounding benefits in the IDE (esp. in VS Code):

* Arguments hints when you write a function/method call.

* Code navigation by clicking on an identifier and pressing F12.

* Safe renaming of attributes / fields / functions / methods across your whole code base.

* Warnings or errors about errors in your code
  (misplaced function arguments, invalid method names etc)

* Displaying the type information in automatically generated documentation

Starting with types
-------------------

Start with a small toy project.

The `standard library documentation <https://docs.python.org/3/library/typing.html>`_ is pretty
good. It includes a `tutorial <https://peps.python.org/pep-0483/>`_.

Complement it with the `mypy cheat sheet <https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html>`_
cheat sheet. I find the mypy cheat sheet slightly more informative.

We'll discuss mypy to automatically check types in a Python project.

Start documenting the following types:

- "primitive" types such as ``int``, ``float``, ``str``.

- think of moving paths and filenames to ``pathlib.Path``

- for optional values that can be ``None``: ``Optional``

- for values that can be of one of a set of types: ``Union``

- the rest can be left alone, or documented as ``Any`` (which is an escape valve)

- do not forget function return types!

Beware of ``NumPy`` scalar types (see :ref:`numpy_types`) that are mostly equivalent to ``float``.

Then start to document collections/data structures. The main useful types are:

- In Python 3.8, you'll have to use ``typing.List[int]``, ``typing.Dict[str, int]`` instead
  of simply writing (> 3.9): ``list[int]`` and ``dict[str, int]``.

- If you want to document that your list is not modified by some code, type it as a 
  ``typing.Sequence``. For your dictionary, use a ``typing.Mapping``. Then, any operation
  that would modify the sequence/mapping will be flagged as an error by Mypy (but it would
  still execute at runtime!).

- Document "functions that take functions", such as root-finding algorithms, using 
  ``typing.Callable``.

- If you are already using dicts to hold a bunch of values, consider typing them using 
  ``TypedDict``.

- To document tuples, use a ``NamedTuple``, but that requires changing your code, not merely
  annotate it.

Telling VS Code to check types
------------------------------

Of course, all this type information is useless if errors are not caught.

I personally use the `mypy <https://mypy.readthedocs.io/>`_ static type checker.

VS Code also includes Pylance by default and Pylance can provide diagnostics too.

Activating Pylance
^^^^^^^^^^^^^^^^^^

This is the easiest.

I advise doing it on a project-by-project basis, so not by modifying the global VS Code settings.

Instead, add the following to the ``.vscode/settings.json`` file in your project folder:

.. code-block:: json

       "python.analysis.diagnosticMode": "workspace",
       "python.analysis.typeCheckingMode": "basic",

If you want to suffer, change ``basic`` to ``strict`` in the above.

More customization is possible, see `this page <https://code.visualstudio.com/docs/python/settings-reference#_code-analysis-settings>`_.

Installing Mypy (level 1)
^^^^^^^^^^^^^^^^^^^^^^^^^

We discussed "code levels" according to how they are packaged. In :ref:`level 1 <publishing1>`,
a project is a collection of few Python files without much ceremonial. Development is done
in some generic Python virtual environment that is often shared between projects.

First, install mypy using ``pip``.

.. code-block::

    pip install mypy

Then, activate Mypy by adding:

.. code-block:: json

       "python.linting.mypyEnabled": true,

to the project ``.vscode/settings.json`` file.

Installing Mypy (level 2)
^^^^^^^^^^^^^^^^^^^^^^^^^

In :ref:`level 2 <publishing2>`, the project is managed using Poetry. Add mypy as a development
dependency and install it.

.. code-block::

    poetry add --dev mypy

As before, add:

.. code-block:: json

       "python.linting.mypyEnabled": true,

to the project ``.vscode/settings.json`` file.

Also, add the following to the ``pyproject.toml`` file, so that mypy knows where to find source
code files:

.. code-block:: toml

    [tool.mypy]
    python_version = "3.8" # or your minimal Python version

    files = [
    "src/PROJECT_NAME",
    "tests",
    ]
    mypy_path = "$MYPY_CONFIG_FILE_DIR/src"

If mypy complains about missing types in libraries, you can add

.. code-block:: toml

    [[tool.mypy.overrides]]
    module = 'parsy' # or whatever module is causing trouble
    ignore_missing_imports = true


.. toctree::
    :hidden:

    Index <self>
    root0
    root1
    root2
    root3
    root4
    root5
    root5_nodoc
    tricky