Level 2 (or 3?): documenting the code using Sphinx
==================================================

(There is a lot to say. I'm writing down here what I had to learn through trial and error. Expect
to spend a few days understanding how all the pieces fit together. The result is worth it.)

`Sphinx <https://www.sphinx-doc.org/>`_ is an amazing tool to generate documentation
from `reStructuredText <https://docutils.sourceforge.io/rst.html>`_, Markdown or Jupyter notebook
files.

How to start using Sphinx
-------------------------

The best way is to start with an existing project. I have made a 
`sample Sphinx project <https://github.com/denisrosset/sphinx_example/>`_ so that you can
play with Sphinx immediately.

For a more involved project, including ``level 2``-style packaging of the Python source code,
see my `configpile <https://github.com/denisrosset/configpile>`_ library.

reStructuredText vs Markdown vs Jupyter notebooks
-------------------------------------------------

Advantages of reStructuredText:

* Amazing VS Code support including code completion, and markup checking using the 
  `esbonio <https://marketplace.visualstudio.com/items?itemName=swyddfa.esbonio>`_ extension.

* More principled way of extending the markup language.

* Easier to use at first because of all the Sphinx examples out there.

Advantages of Markdown:

* Supports all Sphinx syntax using Markdown extensions, through the 
  `MyST-NB <https://myst-nb.readthedocs.io>`_ parser.

* Slightly easier to read and write

* Can be cut'n'pasted

* Can be previewed directly in GitHub

Advantages of Jupyter Notebooks:

* Include code examples and results

* Stand on their own

**Convert between markup formats using `Pandoc <https://pandoc.org/>`_!**

Sphinx extensions I use
-----------------------

The clearer theme (I find):

* ``sphinx_book_theme``

To put the magic file for GitHub pages:

* ``sphinx.ext.githubpages``

To include Markdown files, or simply Jupyter notebooks:

* ``myst_nb``

To automatically document API of the code:

* ``sphinx.ext.autodoc`` (automatically document modules/classes)
* ``sphinx.ext.autosummary`` (automatically recurse through Python files)
* ``sphinx.ext.napoleon`` (Google style shorter docstrings)
* ``sphinx_autodoc_typehints`` (recover types from annotations)

To provide hyperlinks to the API of other Python packages:

* ``sphinx.ext.intersphinx``

To include LaTeX math:

* ``sphinx.ext.mathjax``

To install reStructuredText support in VS Code
----------------------------------------------

Install the esbonio server:

.. code-block::
    
    poetry add --dev esbonio

Then add to your ``.vscode/settings.json`` file:

.. code-block:: json

    "esbonio.server.enabled": true,
    "esbonio.sphinx.confDir": "${workspaceFolder}/docs/source",
    "esbonio.sphinx.srcDir": "${workspaceFolder}/docs/source",
    "esbonio.sphinx.buildDir": "${workspaceFolder}/docs/build",

Replace of course the directories depending on the folder structure you use.

Esbonio can be fiddly and a bit resource hungry in VS Code. Use it in projects that are in top
shape.

Use a GitHub action to publish your documentation everytime your code changes
-----------------------------------------------------------------------------

* Add a workflow so that your website is rebuilt every time something is pushed to your
  master/main branch.

  See `this workflow <https://github.com/denisrosset/sphinx_example/blob/main/.github/workflows/build-docs.yml>`_
  for an example.

  The workflow will push a copy of the built HTML website in a new ``gh-pages`` branch.

* Activate the `GitHub Pages <https://pages.github.com/>`_ website in your repository settings.

Alternative: use `Read the Docs <https://readthedocs.org/>`_ who is providing a similar service.