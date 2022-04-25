Second step: script to module
=============================

In this second step, we put the algorithm in its own function. We keep the "cos" example,
inside a ``if __name__ == "__main__":`` code fence that executes only if the script is 
run with a ``python root2.py`` invocation.

The settings are variables declared at the module level. It is not considered good programming
practice (similar to the use of global variables), but is simpler.

The script ``root2.py`` is now a Python module that can be imported in other files:

.. code-block:: python

    from root2 import brent

    print(brent(cos, 0.0, 3.0))

Here is the code, with minimal changes.

.. literalinclude:: root2.py

and we display the execution below.

.. command-output:: python typing/root2.py
