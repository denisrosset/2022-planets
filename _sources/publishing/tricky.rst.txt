Tricky parts
============

Feedback is welcome!

Including Cython/C/C++/Fortran code in Poetry projects
------------------------------------------------------

That's a Level 2 minimum problem! I have not tested the following solutions.

* Isolate the Cython/C/C++/Fortran code in its own Python package

  and follow pre-Poetry practices to package/publish that code. Make the main Poetry-managed
  project depend on this smaller package.

  Consider making the package with native code an optional dependency if parts of the Python code
  can be run without it. See `extras <https://python-poetry.org/docs/pyproject/#extras>`_.

* Provide a source distribution 
  (`sdist <https://docs.python.org/3/distutils/sourcedist.html>`_) using Poetry, include a 
  ```build.py``` script. This is undocumented, see issues:
  `11 <https://github.com/python-poetry/poetry/issues/11>`_, 
  `137 <https://github.com/python-poetry/poetry/issues/137>`_, 
  `2470 <https://github.com/python-poetry/poetry/issues/2740>`_

* Provide binary wheels
  Python distribution is moving to a precompiled `wheels <https://realpython.com/python-wheels/>`_ 
  distribution model. Much nicer for the user, more headaches for library maintainers.

  Big projects (Numpy, etc) have continuous integration (CI) pipelines in the cloud to automatically
  build the wheels for various Windows/macOS/Linux versions *and* Python versions.

  The `cibuildwheel <https://github.com/pypa/cibuildwheel>`_ package may help, and it
  integrates with GitHub Actions (not tested)

Conflicts between code dependencies and Sphinx/VS Code dependencies
-------------------------------------------------------------------

Most tools I'm advocating in this talk have few dependencies by design. Sphinx is the exception.
The combination of Sphinx + `esbonio <https://github.com/swyddfa/esbonio>`_ pulls a lot of
dependencies which can lead to friction.

Unfortunately, generating the Sphinx documentation depends on the documented project if one
wants to generate API pages, so there is no easy way out there (for now).
