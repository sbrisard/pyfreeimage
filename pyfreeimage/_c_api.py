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
    f = getattr(cfi, func_name)
    f.restype = restype
    f.argtypes = argtypes

init_signature('FreeImage_GetVersion', c_char_p, None)
init_signature('FreeImage_GetCopyrightMessage', c_char_p, None)
init_signature('FreeImage_GetFileType', c_int, [c_char_p, c_int])
init_signature('FreeImage_AllocateT', c_void_p,
               [c_int, c_int, c_int, c_int, c_uint, c_uint, c_uint])
init_signature('FreeImage_GetImageType', c_int)
init_signature('FreeImage_GetColorsUsed')
init_signature('FreeImage_GetBPP')
init_signature('FreeImage_GetWidth')
init_signature('FreeImage_GetHeight')
init_signature('FreeImage_GetLine')
init_signature('FreeImage_GetPitch')
init_signature('FreeImage_Load', c_void_p, [c_int, c_char_p, c_int])
init_signature('FreeImage_Save', c_int, [c_int, c_void_p, c_char_p, c_int])
init_signature('FreeImage_Clone', c_void_p, [c_void_p])
init_signature('FreeImage_Unload', None, [c_void_p])

init_signature('FreeImage_CreateTag', c_void_p, [])
init_signature('FreeImage_DeleteTag', None)
init_signature('FreeImage_CloneTag', c_void_p)
init_signature('FreeImage_GetTagKey', c_char_p)
init_signature('FreeImage_GetTagDescription', c_char_p)
init_signature('FreeImage_GetTagID', c_uint16)
init_signature('FreeImage_GetTagType', c_int)
init_signature('FreeImage_GetTagCount', c_uint32)
init_signature('FreeImage_GetTagLength', c_uint32)
init_signature('FreeImage_GetTagValue', c_void_p)

init_signature('FreeImage_FindFirstMetadata', c_void_p,
               [c_int, c_void_p, c_void_p_p])
init_signature('FreeImage_FindNextMetadata', c_bool, [c_void_p, c_void_p_p])
init_signature('FreeImage_FindCloseMetadata', None, [c_void_p])
init_signature('FreeImage_GetMetadata', c_bool,
               [c_int, c_void_p, c_char_p, c_void_p_p])
init_signature('FreeImage_GetMetadataCount', c_uint, [c_int, c_void_p])
init_signature('FreeImage_TagToString', c_char_p, [c_int, c_void_p, c_char_p])
