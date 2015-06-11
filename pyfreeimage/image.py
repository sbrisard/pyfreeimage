"""This module defines the Image class and some basic related functions."""

import ctypes
import functools
import operator

from pyfreeimage.constants import FIMD_EXIF_MAIN
from pyfreeimage.metadata import Tag

try:
    from weakref import finalize
except ImportError:
    from pyfreeimage.wrutils import finalize

import pyfreeimage.constants

from pyfreeimage._c_api import cfi


class Image:
    """Class that represents an image.

    The constructor of this class should not be called directly. Use the
    following functions instead:

    - :func:`pyfreeimage.image.empty`
    - :func:`pyfreeimage.io.load`

    Args:
        dib (int): pointer to the underlying FreeImage structure.
    """

    def __init__(self, dib):
        self._dib = dib
        finalize(self, cfi.FreeImage_Unload, dib)

    @property
    def fitype(self):
        """The type of the image (as a ``FIT_*`` constant)."""
        return cfi.FreeImage_GetImageType(self._dib)

    @property
    def palette_size(self):
        """Return the size of the palette (0 for high-color bitmaps)."""
        return cfi.FreeImage_GetColorsUsed(self._dib)

    @property
    def bpp(self):
        """The number of bits per pixel."""
        return cfi.FreeImage_GetBPP(self._dib)

    @property
    def width(self):
        """The width of the image in pixels."""
        return cfi.FreeImage_GetWidth(self._dib)

    @property
    def height(self):
        """The height of the image in pixels."""
        return cfi.FreeImage_GetHeight(self._dib)

    @property
    def line(self):
        """The width of the image in bytes."""
        return cfi.FreeImage_GetLine(self._dib)

    @property
    def pitch(self):
        """The stride of the underlying data array.

        The pitch is the width of the image in bytes, rounded-up to the
        next 32-bit boundary.

        """
        return cfi.FreeImage_GetPitch(self._dib)

    def copy(self):
        """Return a deep copy of the image."""
        return Image(cfi.FreeImage_Clone(self._dib))

    def tag(self, key, mdmodel=FIMD_EXIF_MAIN):
        """Return a tag attached to the image.

        Args:
            key (str): Metadata field name.
            mdmodel (int): Metadata model; one of the ``FIMD_*`` constants
                (defaults to ``FIMD_EXIF_MAIN``).
        Returns:
            Tag: A new Tag instance.

        """
        if isinstance(key, str):
            key = key.encode()
        ptag = ctypes.c_void_p()
        if cfi.FreeImage_GetMetadata(mdmodel, self._dib, key,
                                     ctypes.byref(ptag)):
            return Tag(ptag, mdmodel)
        else:
            return None

    def tags(self, mdmodel=FIMD_EXIF_MAIN):
        """Return a generator function over the tags of the image.

        Args:
            mdmodel (int): Metadata model; one of the ``FIMD_*`` constants
                (defaults to ``FIMD_EXIF_MAIN``).
        Returns:
            A generator function.

        """
        tag  = Tag(ctypes.c_void_p(), mdmodel)
        pptag = ctypes.byref(tag._c_tag)
        mdhandle = cfi.FreeImage_FindFirstMetadata(mdmodel, self._dib, pptag)
        yield tag.copy()
        while cfi.FreeImage_FindNextMetadata(mdhandle, pptag):
            yield tag.copy()
        cfi.FreeImage_FindCloseMetadata(mdhandle)


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
        Image: A new image instance.

    """
    dib = cfi.FreeImage_AllocateT(fitype, width, height, bpp,
                                  rmask, gmask, bmask)
    return Image(dib)
