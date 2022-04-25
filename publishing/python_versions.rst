.. _python_versions:

Python versions
---------------

We want to use a relatively modern Python version. Part of the scientific Python
ecosystem works with `NEP 29 <https://numpy.org/neps/nep-0029-deprecation_policy.html>`_,
including `astropy <https://github.com/astropy/astropy-APEs/blob/main/APE18.rst>`_.

* Python 3.8 is a safe bet until mid-2023 per NEP 29.

* Python 3.9 brings a `much better syntax <https://peps.python.org/pep-0585/>`_
  for type annotations of collections.

* Python 3.10 brings `pattern matching <https://peps.python.org/pep-0636/>`_ and quite a few
  improvements to dataclasses.


Use the system interpreter
^^^^^^^^^^^^^^^^^^^^^^^^^^

If your Python system interpreter is good enough (e.g. Python 3.8 on Linux), excellent!
No need to bother with Conda or additional tools.

Use Conda
^^^^^^^^^

Conda is fine, especially if you rely on non-Python data/scientific packages. It is especially
simple to use for beginners.

If you want to minimize friction and use Conda with Poetry, I advise the following.

* `Create <https://docs.conda.io/projects/conda/en/latest/commands/create.html>`_ a fresh Conda
  environment, and install the 
  `Python <https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-python.html>`_
  version of your choice only.

  We do this so that preinstalled Python packages in your regular Conda environment are *not*
  available in your Poetry project. Thus, you will know immediately about missing dependencies.
 
  If you run your code inside the "wrong" Conda environment, things should be fine, but run
  at least once in a while your code in a clean environment.
  
Use pyenv
^^^^^^^^^

`pyenv <https://github.com/pyenv/pyenv>`_ is the more UNIX-like tool to switch between different
Python interpreters.

It modifies less things on the system than Conda, which is why I personally prefer it.

Note that on Linux, I had to add the following to my ``.bashrc`` initialization script::

  export PYENV_ROOT="$HOME/.pyenv"
  export PATH="$PYENV_ROOT/bin:$PATH"
  eval "$(pyenv init --path)"
  eval "$(pyenv init -)"
  eval "$(pyenv virtualenv-init -)"
  
Pyenv is useful if you want to automatically test your code with different Python versions using
e.g. `tox <https://tox.wiki/en/latest/index.html>`_, but this is level 3 stuff.
