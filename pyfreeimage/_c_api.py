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
init_signature('Load', c_void_p, [c_int, c_char_p, c_int])

__copyright_message__ = libfi.FreeImage_GetCopyrightMessage().decode('ascii')
__version__ = libfi.FreeImage_GetVersion().decode('ascii')
