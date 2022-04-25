Fourth step: breaking the data into dicts
=========================================

Dicts are often used to group related data pieces.

A quick'n'dirty upgrade over plain dicts is to type those dicts with `TypedDict <https://peps.python.org/pep-0589/>`_.
Then those dicts can be automatically documented in the Sphinx-generated website.

This is particularly important if those dicts describe serialized data (for example in pickles).

Advantages of typed dicts:

* We know what key/value pairs they contain

* We document the types of the values

* We can add a documentation string to explain what those key/value pairs are

Example Sphinx autodoc output
-----------------------------

.. autoclass:: root4.Settings
   :members:
   :undoc-members:

.. autoclass:: root4.BrentState
   :members:
   :undoc-members:

Python code
-----------

.. literalinclude:: root4.py

Sample execution
----------------

We display the execution below.

.. command-output:: python typing/root4.py
