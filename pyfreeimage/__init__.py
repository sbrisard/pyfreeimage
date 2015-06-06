"""pyfreeimage is a set of ctypes bindings to the FreeImage library.

Attributes:
    __copyright_message__ (str): The copyright message of the FreeImage
        library.
    __fi_version__ (str): The version of the FreeImage library this
        module is wrapped around.
"""

from pyfreeimage.image import Image, empty
from pyfreeimage.constants import *
from pyfreeimage._c_api import cfi

__copyright_message__ = cfi.FreeImage_GetCopyrightMessage().decode('ascii')
__fi_version__ = cfi.FreeImage_GetVersion().decode('ascii')
