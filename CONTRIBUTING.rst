=======================
Contribution guidelines
=======================


Running tests
=============

Use ``tox``::

   pip install tox
   tox


Creating a release
==================

Releases are performed by maintainers.

* Update ``__version__`` in ``djclick/__init__.py`` on ``master`` and make sure
  the changes pass CI before tagging the release.
* Create and push the release tag (for example, ``v2.5.0``).
* The `release workflow <.github/workflows/release.yml>`_ runs on pushed tags
  other than those matching ``*.dev*``. It builds the wheel and source
  distribution with ``python3 -m build``, publishes them to PyPI, and creates
  a GitHub Release with the distribution files and signatures.
* Add the release notes to `GitHub Releases
  <https://github.com/django-commons/django-click/releases>`_. Contributors are
  listed in the `GitHub contributors graph
  <https://github.com/django-commons/django-click/graphs/contributors>`_.
