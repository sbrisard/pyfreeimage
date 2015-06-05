import ctypes
import ctypes.util

from ctypes import c_bool, c_char_p, c_int, c_uint, c_uint16, c_uint32, c_void_p

c_void_p_p = ctypes.POINTER(c_void_p)

path_to_cfi = ctypes.util.find_library('freeimage')
if path_to_cfi is not None:
    cfi = ctypes.cdll.LoadLibrary(path_to_cfi)
else:
    raise RuntimeError('Could not locate the FreeImage shared library.')

def init_signature(func_name, restype=c_uint, argtypes=[c_void_p]):
    global cfi
    f = getattr(cfi, 'FreeImage_' + func_name)
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
init_signature('GetPitch')
init_signature('Load', c_void_p, [c_int, c_char_p, c_int])
init_signature('Save', c_int, [c_int, c_void_p, c_char_p, c_int])
init_signature('Clone', c_void_p, [c_void_p])
init_signature('Unload', None, [c_void_p])

init_signature('CreateTag', c_void_p, [])
init_signature('DeleteTag', None)
init_signature('CloneTag', c_void_p)
init_signature('GetTagKey', c_char_p)
init_signature('GetTagDescription', c_char_p)
init_signature('GetTagID', c_uint16)
init_signature('GetTagType', c_int)
init_signature('GetTagCount', c_uint32)
init_signature('GetTagLength', c_uint32)
init_signature('GetTagValue', c_void_p)

init_signature('FindFirstMetadata', c_void_p, [c_int, c_void_p, c_void_p_p])
init_signature('FindNextMetadata', c_bool, [c_void_p, c_void_p_p])
init_signature('FindCloseMetadata', None, [c_void_p])
init_signature('GetMetadata', c_bool, [c_int, c_void_p, c_char_p, c_void_p_p])
init_signature('GetMetadataCount', c_uint, [c_int, c_void_p])
init_signature('TagToString', c_char_p, [c_int, c_void_p, c_char_p])
