Challenges of academic code
---------------------------


Structural/institutional
^^^^^^^^^^^^^^^^^^^^^^^^

* Money for software dev. is scarce (see `Magma <http://magma.maths.usyd.edu.au/magma/faq/costs>`_, 
  `SAGE <https://wstein.org/talks/2016-06-sage-bp/bp.pdf>`_)

* Bibliometric evaluation of researchers rarely include code

* Unclear citation guidelines (user-facing code vs. libraries)

* Who owns the code?

  One researcher: idiosyncratic code style, "scratch my current itch", "left for industry"

  Research group: fast turn-over of maintainers, lack of software mentorship


Contextual
^^^^^^^^^^

* It's research! Requirements/scope evolve fast

  Code bases become piles of quick'n'dirty additions/fixes

  Documentation, if written, gets outdated fast.

  Different levels of code stability in the same project

* Rabbit hole: language features as mathematical puzzles

  E.g. type systems. Luckily Python is a sweet spot.

* Programming skills variance

* REPL/Notebook inspired coding

  Lack of modularity

  Mixing of computation and plot/GUI code

* Big dataset / long analysis time (astronomy)

  Impedes code+examples distribution / testing

Python
^^^^^^

* `One way to do it <https://peps.python.org/pep-0020/>`_ ... but Python is 30 years old

  Diversity of approaches in packaging/publishing, Python environment manangement, IDEs, tooling

* Interpreted language with GIL

  Multiprocessing, integrating/publishing C/C++/Fortran code

* Type annotations and numerical/data processing code

  Ongoing process (as of Apr 2022): `astropy <https://www.astropy.org/>`_ is a mixed bag

  `Pandas <https://pandas.pydata.org/>`_ dataframes are difficult to Documentation

  `NumPy <https://numpy.org/>`_ typing is in its early stages; and slows down code analysis

