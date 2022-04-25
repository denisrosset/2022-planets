Tricky parts of type annotations
================================

Type annotations are amazing, please use them.

However, it is good to know when to stop, and when the type checking starts to work against you.

Nevertheless, here are a few interesting directions to explore type annotations further.

.. _validating_types:

Validating types at runtime
---------------------------

By default, types annotations form an additional layer over Python code that does not impact
runtime (except when types are introspected by libraries to provide features, but this is rare).

To check types at runtime, I suggest two libraries:

* `Beartype <https://github.com/beartype/beartype>`_ is designed for speed, verifies instances
  shallowly, but you can ``@beartype`` all your functions/methods with minimal speed impact.

  Beartype does not introspect typed dictionaries or dataclasses well.

* `typeguard <https://github.com/agronholm/typeguard/>`_ verifies passed objects in depth. It is
  slow and comprehensive. Use ``typeguard`` if you want to verify the type of unpickled data for
  example, or when debugging code with type errors.

.. _numpy_types:

Typing NumPy code
-----------------

Main namespace (i.e. ``import numpy as np``) is fully type-annotated as of version ``1.22.0``.

The major pain point with NumPy and types is that ``np.float64`` is mostly interchangeable, but
not equivalent to the standard ``float`` type. Thus, when writing a function such as:

.. code-block:: python

    def square(x):
        return x * x

The return type will be ``np.float64`` when passed a ``np.float64``, and a ``float`` when passed
a ``float``.

I have not yet found a good solution to that problem. One way is to define a ``Float`` alias:

.. code-block:: python

    from typing import Union
    import numpy as np

    Float = Union[np.float64, float]

    def square(x: Float) -> Float:
        return x * x

Documenting NumPy array shapes
------------------------------
There are experiments to document the shape of NumPy arrays, for example `nptyping <https://github.com/ramonhagenaars/nptyping>`_

I expect this area to move quite fast. For now, I'd recommend using ``nptyping``, whose annotations
can be verified by either ``typeguard`` or ``beartype``.

To declare a ``2x2`` integer matrix with ``nptyping``, write:

.. code-block:: python

    from nptyping import NDArray, Int, Shape

    def func(arr: NDArray[Shape["2, 2"], Int]) -> None:
        pass

Astropy
-------

Astropy code is a mix of type-annotated code and ``Any``-annotated code.

Interesting direction: `typing physical quantities <https://docs.astropy.org/en/stable/units/type_hints.html>`_

Disclaimer: I have little experience of astropy.

Typing Pandas code
------------------

Pandas is very type-dynamic, and usually the code constructing Pandas dataframes does not
document the dataframe schema.

There are a few packages that aim to remedy this fact, such as `Pandera <https://pandera.readthedocs.io/en/stable/>`_.

I wrote a thin library that enables the documentation of schemas, `tybles <https://github.com/denisrosset/tybles>`_.

Currently, it wraps only a few Pandas read/write functions. More is planned in the future (and
according to user requests).

It enables schema documentation using dataclasses:

.. code-block:: python

    import tybles as tb
    from dataclasses import dataclass
    import numpy as np
    import pandas as pd

    @dataclass(frozen=True)
    class Planet:
        kepler_id: np.int32
        koi_name: str
        kepler_name: str
        status: str
        period: np.float64

    schema = tb.schema(Planet)
    schema.read_csv("planets.csv")