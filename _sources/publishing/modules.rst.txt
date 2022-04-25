Python modules
==============

At level 1, your project is small enough that it fits confortably in a single source code file
(except example scripts, Jupyter notebooks that will be separate). Or one main module that imports
a few helpers modules.

Note that the advice below is (mostly) appropriate when going for a level 2 organization with a 
``src/PROJECTNAME`` folder, but parts of it can be used at any time.

Helpful VS Code features such a code navigation, refactoring start to break down when files are
larger than a few thousand lines of code (especially in NumPy intensive code). Files longer
than 10000 lines will require features to be selectively disabled, and even Black will take
tens of seconds to run.

The key is to split the code in `modules <https://docs.python.org/3/tutorial/modules.html>`_, the
real difficulty is to decide how it should be split.

Ideally, you can split your code into layers, when high-level functions/classes use
lower-level functions/classes but not vice-versa.

A tool such as `Jonga <https://github.com/bwohlberg/jonga>`_ may help if you are facing a
code base written by someone else.

How to import identifiers
-------------------------

Some packages are so widely used that people import their base module directly using a prefix,
and prefix every use of an identifier:

.. code-block:: python

    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt # to demonstrate submodule import

    mat = np.zeros((2, 2))

For other modules, I prefer to import only what I need:

.. code-block:: python

    from dataclasses import dataclass, is_dataclass

    @dataclass(frozen=True)
    class Point:
        x: float
        y: float

    assert is_dataclass(Point)

and when I use an identifier that has not been imported, VS Code will suggest importing it from
one of the packages in the virtual environment, and :ref:`isort <formatting>` will group and
clean up all these imports.

Circular imports
----------------

Unlike compiled languages, what a module offers (functions, classes) is added to the module
dictionnary by executing code.

Thus, having two modules importing each other would send the Python interpreter in a circular
recursive loop. Python will instead throw an exception and hint that the problem may be due
to circular imports.

How to break the cycle? Here are suggestions, when modules X and Y depend on each other.

* Take out the parts of X and Y that depend on each other, put it in a module Z, have X and Y
  depend on Z, and no longer on each other.

* If the dependency occurs only in type annotations, put the imports required by type annotations
  in a ``if TYPE_CHECKING:`` fence, see `this page <https://adamj.eu/tech/2021/05/13/python-type-hints-how-to-fix-circular-imports/>`_.

* In either X or Y, import the identifier *inside* the function/method that uses it, not at
  top-level. This is considered bad Python style and linters such as pylint will complain,
  learn how to silence them case by case.

Relative imports
----------------

Inside a Python package, I like to 
`relative imports <https://realpython.com/absolute-vs-relative-python-imports/>`_. They highlight
the difference between identifiers I import from the Python standard library or dependencies,
and imports from my own code.

Also, ``isort`` will conveniently separate them at the top of the source file.

Module documentation
--------------------

It is a good idea to include a top-level docstring in every Python file, even if it is just
a few lines explaining what part of the code resides in the module.

Such docstring will be used by `sphinx.ext.autodoc <https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html>`_
when building the API documentation.

See `this StackOverflow question <https://stackoverflow.com/questions/47071959/how-to-include-docstrings-comments-located-in-a-module-but-outside-of-class-and>`_
as to where to put the docstring.

Reexporting identifiers
-----------------------

For the library author, it is convenient to split the code into different modules. However, the
library user may complain about importing frequently used identifiers from a variety of submodules.

Commonly, Python packages reexport identifiers in their base ``__init__.py`` file, stressing that
fact by adding the reexported identifiers in the ``__all__`` variable. The ``__all__`` variable
is also used by mypy to see whether the use of a "reexported" identifier is legit.

See for example the `__init__.py <https://github.com/denisrosset/configpile/blob/main/src/configpile/__init__.py>`_
file in my configpile library.
