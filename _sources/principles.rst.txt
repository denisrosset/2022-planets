Goals and principles in this talk
---------------------------------

Goals
^^^^^

* make code more maintainable

* low-effort documentation

* minimal effort code publishing

Principles
^^^^^^^^^^

* Keep information in one place (code + tests + documentation)

* Tools/features that can be used incrementally and scale with skills

* Take in account how fast the code is changing


Advice you already heard
------------------------

* Use version control

  I like GitHub (automation through Azure, publishing documentation, collaboration tools,
  network effect); GitLab has bigger caps on file/repository size.

  `Branches <https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell>`_ for making
  quick'n'dirty mods away from the main development line

  `Submodules <https://git-scm.com/book/en/v2/Git-Tools-Submodules>`_ to separate code from
  (often big) datasets (advanced)

* Comment your code (micro)

  Descriptive names for variables/functions (IDE rename)

  Split code into functions

  Type annotations

* Comment your code (macro)

  Docstrings instead of comments

  Refer to publications

Things we'll look at
--------------------

* Use a good IDE

* Code formatting

* Type annotations

* Web documentation

* Testing

* Managing dependencies, modularizing code and publishing
