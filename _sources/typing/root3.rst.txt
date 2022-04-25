Third step: breaking the code into functions
============================================

In this third step, we break the big ``brent`` function into smaller pieces. The benefits in
this example are minimal: the resulting code is *longer*, and whether it is simpler to read
is debatable.

Nevertheless, this is an illustration of the process.

When breaking up code, it can become cumbersome to move data around: function signatures
can become big. Note that we still have settings as top-level module declarations. Such practices
make it difficult to understand where values come from.

We documented the functions using  
`Google style docstrings <https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html>`_

Example Sphinx autodoc output
-----------------------------

Such documentation strings are automatically understood by Sphinx.

.. autofunction:: root3.inverse_quadratic_interpolation_step

Python code
-----------

.. literalinclude:: root3.py

Sample execution
----------------

We display the execution below.

.. command-output:: python typing/root3.py
