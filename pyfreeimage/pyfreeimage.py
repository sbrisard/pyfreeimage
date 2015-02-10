from .constants import Format
from .constants import Type
from pyfreeimage._c_api import libfi

_reverse_format = dict((f.value, f) for f in Format)
_reverse_type = dict((t.value, t) for t in Type)

def get_version():
    """Return the current version of the library, as a string."""
    return libfi.FreeImage_GetVersion()


def get_copyright_message():
    """Return the copyright text of the library, as a string."""
    return libfi.FreeImage_GetCopyrightMessage()


def get_file_type(filename, size=0):
    """Return the type of the image as an int; `size` is unused."""
    return _reverse_format[libfi.FreeImage_GetFileType(filename, size)]


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

def empty(width, height, bpp, rmask=0, gmask=0, bmask=0,
          fitype=Type.bitmap):
    dib = libfi.FreeImage_AllocateT(fitype.value, width, height, bpp,
                                    rmask, gmask, bmask)
    return Bitmap(dib)

def load(name, fmt=None, flags=0):
    if fmt is None:
        fif = libfi.FreeImage_GetFileType(name, 0)
    else:
        fif = fmt.value
    dib = libfi.FreeImage_Load(fif, name, flags)
    return Bitmap(dib)
