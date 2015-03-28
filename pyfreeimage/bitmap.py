import functools
import operator

try:
    from weakref import finalize
except ImportError:
    from pyfreeimage.wrutils import finalize

import pyfreeimage.constants

from pyfreeimage._c_api import libfi


class Bitmap:
    """Class that represents all images.

    The constructor of this class should not be called directly. Use the
    following functions instead:

    - :func:`pyfreeimage.bitmap.empty`
    - :func:`pyfreeimage.io.load`

    Args:
        dib (int): pointer to the underlying FreeImage structure.
    """

    def __init__(self, dib):
        self._dib = dib
        finalize(self, libfi.FreeImage_Unload, dib)

    @property
    def fitype(self):
        """The type of the image (as a ``FIT_*`` constant)."""
        return libfi.FreeImage_GetImageType(self._dib)

    @property
    def palette_size(self):
        """Return the size of the palette (0 for high-color bitmaps.'"""
        return libfi.FreeImage_GetColorsUsed(self._dib)

    @property
    def bpp(self):
        """The number of bits per pixel."""
        return libfi.FreeImage_GetBPP(self._dib)

    @property
    def width(self):
        """The width of the image in pixels."""
        return libfi.FreeImage_GetWidth(self._dib)

    @property
    def height(self):
        """The height of the image in pixels."""
        return libfi.FreeImage_GetHeight(self._dib)

    @property
    def line(self):
        """The width of the image in bytes."""
        return libfi.FreeImage_GetLine(self._dib)

    @property
    def pitch(self):
        """The stride of the underlying data array.

        The pitch is the width of the image in bytes, rounded-up to the
        next 32-bit boundary.

        """
        return libfi.FreeImage_GetPitch(self._dib)

    def copy(self):
        """Return a deep copy of the image."""
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
          fitype=pyfreeimage.constants.FIT_BITMAP):
    """Return a new image of specified shape, bit depth and type.

    The returned image is filled with zeros. For 8-bit images only,
    this function builds a default greyscale palette.

    Args:
        width (int): Width of the image.
        height (int): Height of the image.
        bpp (int): Bit depth.
        rmask (int): Bit layout of the red component.
        gmask (int): Bit layout of the green component.
        bmask (int): Bit layout of the blue component.
        fitype (int): Type of the image (one of the ``FIT_*`` constants).
    Returns:
        A new instance of :class:`pyfreeimage.bitmap.Bitmap`.

    """
    dib = libfi.FreeImage_AllocateT(fitype, width, height, bpp,
                                    rmask, gmask, bmask)
    return Bitmap(dib)
