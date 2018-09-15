fragmuffin_pypitest
=======================

Test rendering of `reStructuredText <http://docutils.sourceforge.net/rst.html>`_
for publishing to PyPI.

Module is **NOT** published to the `official PyPI <https://pypi.org/>`_,
just to `PyPI's test server <https://test.pypi.org/>`_.

Resulting renders to compare:

- `PyPI package <https://test.pypi.org/project/fragmuffin-pypitest>`_
- `GitHub README <https://github.com/fragmuffin/pypi-test>`_

Images
----------

**Basic Linked Image**

.. image:: https://www.python.org/static/community_logos/python-logo-master-v3-TM.png
   :alt: Python is awesome
   :target: https://www.python.org

**Sized** (fail)

.. image:: https://www.python.org/static/community_logos/python-logo-master-v3-TM.png
   :scale: 20 %

**Centered** (fail)

.. image:: https://www.python.org/static/community_logos/python-logo-master-v3-TM.png  
   :align: center

**Inline**

This fictionaly library is |POWERED_BY_PYTHON|, so there.

.. |POWERED_BY_PYTHON| image:: https://www.python.org/static/community_logos/python-powered-w-70x28.png
    :alt: Powered by Python
    :target: https://www.python.org

**SVG**

.. image:: http://dcowden.github.io/cadquery/_static/cadquery_logo_dark.svg


Code Block
--------------------

**Python**

.. code-block:: python

    import time
    print("hi")

    # some comment
    time.sleep(1)
    print("there")


