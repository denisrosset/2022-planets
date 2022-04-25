Fifth step: dataclasses
========================

Python `dataclasses <https://docs.python.org/3/library/dataclasses.html>`_ are amazing
alternatives to dicts when passing data around. Actually, I use them by default for the classes
in my code, except if I have a reason not to (I cannot think of an example at the moment actually).

In the code below, we moved the two dicts to proper dataclasses, and demonstrate the following
advantages we gained.

Mutable vs immutable data
-------------------------

We can declare dataclasses to be *frozen*. This means that their values cannot be modified after
they are constructed, i.e. their instances are immutable objects.

Making a distinction between mutable and immutable pieces of data is great when we need to
understand how data flows through a program.

In our code, the settings are immutable, as they are not modified during code execution (rather,
different ``Settings`` instances can be constructed and used at different times).

The ``BrentState`` class is immutable as well. The Brent step method returns a new updated instance
at every step.

However, this is feasible in this example as the data concerned is quite small (a few 
floating-point numbers). When dealing with larger datasets, often we will modify the data in place
(a standard linear algebra example: in-place LU decomposition of matrices).

To have a mutable dataclass, one simply omits the ``(frozen=True)`` qualifier.

Methods
-------

Dataclasses can have methods. This enables us to group functions related to a piece of data.

When some dataclass fields are derived from the values of other fields, as is the case for the
initial state of Brent's algorithm, we can use 
`static methods <https://realpython.com/instance-class-and-static-methods-demystified/#static-methods>`_
instead of fiddling with the ``__init__`` method.
This works better with frozen dataclasses, inheritance and default parameters etc.

Also, we can provide additional static methods such as ``read_from_json`` to construct instances
from various sources.

We use the ``__post_init__`` method to verify the soundness of the constructed object,
again using `assertions <https://realpython.com/python-assert-statement/>`_.

Documenting invariants
----------------------

A OOP principle is to have `class invariants <https://en.wikipedia.org/wiki/Class_invariant>`_,
i.e. constraints that are satisfied when an instance is constructed, and are preserved during
code execution.

For example, in our ``BrentState`` class, we preserve the fact that ``b`` is the best-known
approximation so far and that ``f(a)`` and ``f(b)`` have opposite signs.


Example Sphinx autodoc output
-----------------------------

.. autoclass:: root5.Settings
   :members:
   :undoc-members:

.. autoclass:: root5.BrentState
   :members:
   :undoc-members:

Python code
-----------

.. literalinclude:: root5.py

Sample execution
----------------

We display the execution below.

.. command-output:: python typing/root5.py
