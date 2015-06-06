.. -*- coding: utf-8 -*-

For developers
==============

Automatic generation of constants
---------------------------------

.. _memory-leaks:

Potential memory leaks and how to avoid them
--------------------------------------------

Memory leaks in class :class:`pyfreeimage.image.Image`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To make sure that the memory allocated by FreeImage is released when the
related pyfreeimage object is destroyed, we use weak references and the `finalize() <https://docs.python.org/3.4/library/weakref.html#weakref.finalize>`_ function. This function is new in Python 3.4. For earlier version, a replacement is implemented in module :mod:`pyfreeimage.wrutils`.

Potential memory leaks in module :mod:`pyfreeimage.metadata`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

API of module :mod:`pyfreeimage.wrutils`
----------------------------------------

.. automodule:: pyfreeimage.wrutils
   :members:
   :undoc-members:
