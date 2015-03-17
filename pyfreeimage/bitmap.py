import functools
import operator

from pyfreeimage._constants import Format, Type
from pyfreeimage._c_api import libfi


_reverse_format = dict((f.value, f) for f in Format)
_reverse_type = dict((t.value, t) for t in Type)


class Bitmap:
    def __init__(self, dib):
        self._dib = dib
        self.fitype = _reverse_type[libfi.FreeImage_GetImageType(dib)]
        self.width = libfi.FreeImage_GetWidth(dib)
        self.height = libfi.FreeImage_GetHeight(dib)
        self.bpp = libfi.FreeImage_GetBPP(dib)

    def __enter__(self):
        return self

    def __exit__(self):
        pass

    def save(self, filename, fif, flags=0):
        """Save the image to a file.

        Args:
            filename (str): File name.
            fif (pyfreeimage.Format): File format.
            flags (int): "or" combination of constants from the
                ``pyfreeimage.ioflags`` module.

        """
        if isinstance(filename, str):
            filename = filename.encode()
        libfi.FreeImage_Save(fif.value, self._dib, filename, flags)

    def copy(self):
        """Return a copy of the image."""
        return Bitmap(libfi.FreeImage_Clone(self._dib))


def get_file_type(filename, size=0):
    """Return the `Type` of the image.

    Args:
        filename (str): File name.
        size (int): unused.
    Returns:
        The type of the image as a :class:`pyfreeimage.Type` instance.
    """
    return _reverse_format[libfi.FreeImage_GetFileType(filename, size)]


def empty(width, height, bpp, rmask=0, gmask=0, bmask=0,
          fitype=Type.BITMAP):
    dib = libfi.FreeImage_AllocateT(fitype.value, width, height, bpp,
                                    rmask, gmask, bmask)
    return Bitmap(dib)


def load(filename, fif=None, flags=0):
    if isinstance(filename, str):
        filename = filename.encode()
    if fif is None:
        fif = libfi.FreeImage_GetFileType(filename, 0)
    else:
        fif = fif.value
    dib=libfi.FreeImage_Load(fif, filename, flags)
    return Bitmap(dib)
