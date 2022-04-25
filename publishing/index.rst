Specifying dependencies and publishing code
===========================================

Missing dependencies, incompatible versions, or conflicting version requirements are an effective
cause of "works on my computer but not on yours".

At the first level, the idea is to document dependencies, enable a quick installation of those
using ``pip install -r``. The code itself is simply downloaded from GitHub, shared by email, ...
without being packaged further.

At the second level, we use Poetry which is a turn-key solution to manage dependencies, isolate
virtual environments, publish package on `PyPI <https://pypi.org/>`_.

At the third level, we'll want to provide additional guarantees about the code robustness. I wonder
how many academic projects will reach that stage.

**Try out these tools in a sample project before publishing existing code!**

(But please use `TestPyPI <https://test.pypi.org/>`_ to not pollute the Python pacakge namespace).

.. toctree::
    :hidden:

    Index <self>
    python_versions
    level1
    level2
    modules
    level3
    tricky
