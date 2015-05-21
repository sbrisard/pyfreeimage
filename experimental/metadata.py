import ctypes
import pyfreeimage as pyfi
import pyfreeimage.metadata as md

from ctypes import c_char_p, c_short

from pyfreeimage._c_api import cfi

c_short_p = ctypes.POINTER(c_short)

def tags(image, mdmodel):
    tagp  = ctypes.c_void_p()
    tagpp = ctypes.byref(tagp)
    tag = md.Tag(tagp, mdmodel)
    mdhandle = cfi.FreeImage_FindFirstMetadata(mdmodel, image._dib, tagpp)
    yield tag.copy()
    while cfi.FreeImage_FindNextMetadata(mdhandle, tagpp):
        yield tag.copy()
    cfi.FreeImage_FindCloseMetadata(mdhandle)


if __name__ == '__main__':
    img = pyfi.io.load('/Users/sbrisard/Documents/tmp/IMGP3980.jpg')
    # print(cfi.FreeImage_GetMetadataCount(pyfi.FIMD_COMMENTS, img._dib))
    print(cfi.FreeImage_GetMetadataCount(pyfi.FIMD_EXIF_MAIN, img._dib))
    # print(cfi.FreeImage_GetMetadataCount(pyfi.FIMD_EXIF_EXIF, img._dib))
    # print(cfi.FreeImage_GetMetadataCount(pyfi.FIMD_EXIF_GPS, img._dib))
    # print(cfi.FreeImage_GetMetadataCount(pyfi.FIMD_EXIF_MAKERNOTE, img._dib))
    # print(cfi.FreeImage_GetMetadataCount(pyfi.FIMD_EXIF_INTEROP, img._dib))
    # print(cfi.FreeImage_GetMetadataCount(pyfi.FIMD_IPTC, img._dib))
    # print(cfi.FreeImage_GetMetadataCount(pyfi.FIMD_XMP, img._dib))
    # print(cfi.FreeImage_GetMetadataCount(pyfi.FIMD_GEOTIFF, img._dib))
    # print(cfi.FreeImage_GetMetadataCount(pyfi.FIMD_ANIMATION, img._dib))
    # print(cfi.FreeImage_GetMetadataCount(pyfi.FIMD_CUSTOM, img._dib))
    # print(cfi.FreeImage_GetMetadataCount(pyfi.FIMD_EXIF_RAW, img._dib))

    tagp = ctypes.c_void_p()
    mdmodel = pyfi.FIMD_EXIF_MAIN
    mdhandle = cfi.FreeImage_FindFirstMetadata(mdmodel, img._dib,
                                               ctypes.byref(tagp))

    for tag in tags(img, mdmodel):
        s = cfi.FreeImage_TagToString(mdmodel, tag._c_tag, None)
        print('Type = {}, count = {}, key = {}, value = {}, {}'.format(tag.type, tag.count, tag.key, s, tag.value))
        print(tag)
        print(tag.value)
        if tag.type == pyfi.FIDT_ASCII:
            print(bytes(tag.value))
