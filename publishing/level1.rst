.. _publishing1:

Level 1: requirements.txt, "clone the repo" deployment
======================================================

* Document the minimal Python version required in a ``README.md`` file or similar. 

* Let the end user manage their Python environments with the required Python version. 
  They are probably using Conda, and creating new Conda environments is not too difficult.

* List all dependencies in a 
  `requirements.txt <https://pip.pypa.io/en/stable/reference/requirements-file-format/>`_ file.
  
  If you want to force version numbers, use the 
  `pip freeze <https://pip.pypa.io/en/stable/cli/pip_freeze/>`_ command. I'd advocate to replace
  the exact ``astropy==5.0.1`` numbers to minimal version numbers such as ``astropy>=5.0.0``.

  If you find that your requirements start to be complex, move to the :ref:`Level 2 <publishing2>`
  approach.

* People install your dependencies by running 
  `pip install -r requirements.txt <https://pip.pypa.io/en/stable/cli/pip_install/>`_.

* People reuse your code by coping the Python files in their own projects, or by adding your
  source folder to their Python path.
