.. -*- coding: utf-8 -*-

Installation
============

You need to have the shared version of `FreeImage <http://freeimage.sourceforge.net/>`_ installed on your computer. Check out the bleeding-edge version from `Github <https://github.com/sbrisard/pyfreeimage>`_::

  $ git clone https://github.com/sbrisard/pyfreeimage.git

The installation is standard::

  $ python setup.py install

Notes
-----

  1. pyFreeImage is developed under Python 3.4; however, it should work with older versions of Python (including 2.7). Please report any problem with these versions of Python.
  2. pyFreeImage uses `ctypes.util.find_library('freeimage') <https://docs.python.org/3.4/library/ctypes.html#ctypes.util.find_library>`_ to locate the `FreeImage <http://freeimage.sourceforge.net/>`_ library. Make sure that the library can be reached by this function (see also `Finding shared libraries <https://docs.python.org/3.4/library/ctypes.html#finding-shared-libraries>`_).
