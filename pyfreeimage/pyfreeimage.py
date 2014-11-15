import ctypes

from ctypes import c_char_p
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

init_signature('GetVersion', c_char_p, None)
