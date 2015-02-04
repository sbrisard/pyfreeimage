import ctypes

from ctypes import c_char_p
from ctypes import c_int
from ctypes import c_uint
from ctypes import c_void_p

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
    def __init__(self, dib):
        self._dib = dib

    def __enter__(self):
        return self

    def __exit__(self):
        pass

def empty(type, width, height, bpp, rmask=0, gmask=0, bmask=0,
          fitype='FIT_BITMAP'):
    libfi.FreeImage_AllocateT(fitype, width, height, bpp, rmask, gmask, bmask)

init_signature('GetVersion', c_char_p, None)
init_signature('GetCopyrightMessage', c_char_p, None)
init_signature('GetFileType', c_int, [c_char_p, c_int])
init_signature('AllocateT', c_void_p, [c_int, # type
                                       c_int, c_int, # width, depth
                                       c_int, # bpp
                                       c_uint, c_uint, c_uint]) # RGB masks
init_signature('GetBPP', c_uint, [c_void_p])
