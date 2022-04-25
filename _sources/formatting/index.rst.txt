.. _formatting:

Code formatting
===============

I use two great tools to clean up my code.

- `Black <https://github.com/psf/black>`_ (joke on the Ford Model T) to format the code with 
  a line length limit

- `isort <https://isort.readthedocs.io/en/latest/>`_ to organize imports

Note that Black is pretty slow on files with >10000 lines of code.

Note that ``isort`` will not detect unused imports. This will be the job of the VS Code Python
extension, or of pylint if you install/use it.

The only configuration option of Black is the line length. Details below.

Line length
-----------

While many Python packages have now settled on the use of Black as a
code formatter (which does not have many tweaks! and thus saves time on
style discussion), line length recommendations vary widely.

In 2001, `PEP8 <https://www.python.org/dev/peps/pep-0008/>`_ prescribed
79 characters per line. Twenty years later, modern Python code tends to
use more descriptive, longer identifiers. The introduction of `type
hints <https://www.python.org/dev/peps/pep-0484/>`_ also widens
function/method declarations.

Black's default is 88 characters.

I personally tend to use 99 characters on OOP code with type hints.

See
`<https://jakevdp.github.io/blog/2017/11/09/exploring-line-lengths-in-python-packages/>`_
for additional analysis.

.. toctree::
    :hidden:

    Index <self>
    level1
    level2
    level3
    regions
