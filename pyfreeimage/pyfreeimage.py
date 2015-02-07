import ctypes

from ctypes import c_char_p
from ctypes import c_int
from ctypes import c_uint
from ctypes import c_void_p

from constants import Type

libfi = ctypes.cdll.LoadLibrary('/opt/local/lib/libfreeimage.dylib')


def init_signature(func_name, restype=c_uint, argtypes=[c_void_p]):
    global libfi
    f = getattr(libfi, 'FreeImage_' + func_name)
    f.restype = restype
    f.argtypes = argtypes

def get_version():
    """Return the current version of the library, as a string."""
    return libfi.FreeImage_GetVersion()


def get_copyright_message():
    """Return the copyright text of the library, as a string."""
    return libfi.FreeImage_GetCopyrightMessage()


def get_file_type(filename, size=0):
    """Return the type of the image as an int; `size` is unused."""
    return libfi.FreeImage_GetFileType(filename, size)


class Bitmap:
    _type = dict((t.value, t) for t in Type)

    def __init__(self, dib):
        self._dib = dib
        self.itype = Bitmap._type[libfi.FreeImage_GetImageType(dib)]
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

init_signature('GetVersion', c_char_p, None)
init_signature('GetCopyrightMessage', c_char_p, None)
init_signature('GetFileType', c_int, [c_char_p, c_int])
init_signature('AllocateT', c_void_p, [c_int, # type
                                       c_int, c_int, # width, depth
                                       c_int, # bpp
                                       c_uint, c_uint, c_uint]) # RGB masks
init_signature('GetImageType', c_int)
init_signature('GetColorsUsed')
init_signature('GetBPP')
init_signature('GetWidth')
init_signature('GetHeight')
init_signature('GetLine')
