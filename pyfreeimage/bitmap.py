import functools
import operator

try:
    from weakref import finalize
except ImportError:
    from pyfreeimage.wrutils import finalize

from pyfreeimage.constants import FIT_BITMAP
from pyfreeimage._c_api import libfi


class Bitmap:
    def __init__(self, dib):
        self._dib = dib
        self.fitype = libfi.FreeImage_GetImageType(dib)
        self.width = libfi.FreeImage_GetWidth(dib)
        self.height = libfi.FreeImage_GetHeight(dib)
        self.bpp = libfi.FreeImage_GetBPP(dib)
        finalize(self, libfi.FreeImage_Unload, dib)

    def copy(self):
        """Return a copy of the image."""
        return Bitmap(libfi.FreeImage_Clone(self._dib))


def get_file_format(filename, size=0):
    """Return the format (as a ``FIF_*`` constant) of the file.

    Args:
        filename (str): Name of the file where the image is stored.
        size (int): unused.
    Returns:
        The format as an int.
    """
    return libfi.FreeImage_GetFileType(filename, size)


def empty(width, height, bpp, rmask=0, gmask=0, bmask=0,
          fitype=FIT_BITMAP):
    dib = libfi.FreeImage_AllocateT(fitype, width, height, bpp,
                                    rmask, gmask, bmask)
    return Bitmap(dib)


def load(filename, fif=None, flags=0):
    """Read an image from a file.

    Args:
        filename (str): Name of the file from which the image is read.
        fif (int): File format; one of the ``FIF_*`` constants.
        flags (int): or combination of the I/O flags.
    """
    if isinstance(filename, str):
        filename = filename.encode()
    if fif is None:
        fif = libfi.FreeImage_GetFileType(filename, 0)
    dib=libfi.FreeImage_Load(fif, filename, flags)
    return Bitmap(dib)


def save(filename, fif, flags=0):
    """Save the image to a file.

    Args:
        filename (str): Name of the file to which the image is saved.
        image (:class:`Bitmap`): Image to be saved.
        fif (int): File format; one of the ``FIF_*`` constants.
        flags (int): or combination of the I/O flags.

    """
    if isinstance(filename, str):
        filename = filename.encode()
    libfi.FreeImage_Save(fif.value, self._dib, filename, flags)
