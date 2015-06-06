import ctypes
import ctypes.util

from ctypes import c_bool, c_char_p, c_int, c_uint, c_uint16, c_uint32, c_void_p

c_void_p_p = ctypes.POINTER(c_void_p)

path_to_cfi = ctypes.util.find_library('freeimage')
if path_to_cfi is not None:
    cfi = ctypes.cdll.LoadLibrary(path_to_cfi)
else:
    raise RuntimeError('Could not locate the FreeImage shared library.')

def init_signature(func_name, restype, argtypes):
    global cfi
    f = getattr(cfi, func_name)
    f.restype = restype
    f.argtypes = argtypes

init_signature('FreeImage_GetVersion', c_char_p, None)
init_signature('FreeImage_GetCopyrightMessage', c_char_p, None)
init_signature('FreeImage_GetFileType', c_int, [c_char_p, c_int])
init_signature('FreeImage_AllocateT', c_void_p,
               [c_int, c_int, c_int, c_int, c_uint, c_uint, c_uint])
init_signature('FreeImage_GetImageType', c_int, [c_void_p])
init_signature('FreeImage_GetColorsUsed', c_uint, [c_void_p])
init_signature('FreeImage_GetBPP', c_uint, [c_void_p])
init_signature('FreeImage_GetWidth', c_uint, [c_void_p])
init_signature('FreeImage_GetHeight', c_uint, [c_void_p])
init_signature('FreeImage_GetLine', c_uint, [c_void_p])
init_signature('FreeImage_GetPitch', c_uint, [c_void_p])
init_signature('FreeImage_Load', c_void_p, [c_int, c_char_p, c_int])
init_signature('FreeImage_Save', c_int, [c_int, c_void_p, c_char_p, c_int])
init_signature('FreeImage_Clone', c_void_p, [c_void_p])
init_signature('FreeImage_Unload', None, [c_void_p])

init_signature('FreeImage_CreateTag', c_void_p, None)
init_signature('FreeImage_DeleteTag', None, [c_void_p])
init_signature('FreeImage_CloneTag', c_void_p, [c_void_p])
init_signature('FreeImage_GetTagKey', c_char_p, [c_void_p])
init_signature('FreeImage_GetTagDescription', c_char_p, [c_void_p])
init_signature('FreeImage_GetTagID', c_uint16, [c_void_p])
init_signature('FreeImage_GetTagType', c_int, [c_void_p])
init_signature('FreeImage_GetTagCount', c_uint32, [c_void_p])
init_signature('FreeImage_GetTagLength', c_uint32, [c_void_p])
init_signature('FreeImage_GetTagValue', c_void_p, [c_void_p])

init_signature('FreeImage_FindFirstMetadata', c_void_p,
               [c_int, c_void_p, c_void_p_p])
init_signature('FreeImage_FindNextMetadata', c_bool, [c_void_p, c_void_p_p])
init_signature('FreeImage_FindCloseMetadata', None, [c_void_p])
init_signature('FreeImage_GetMetadata', c_bool,
               [c_int, c_void_p, c_char_p, c_void_p_p])
init_signature('FreeImage_GetMetadataCount', c_uint, [c_int, c_void_p])
init_signature('FreeImage_TagToString', c_char_p, [c_int, c_void_p, c_char_p])
