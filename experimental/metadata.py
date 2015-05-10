import ctypes
import pyfreeimage as pyfi
import pyfreeimage.metadata as md

from pyfreeimage._c_api import libfi as cfi

if __name__ == '__main__':
    img = pyfi.io.load('/Users/sb/Documents/tmp/IMGP3980.jpg')
    print(cfi.FreeImage_GetMetadataCount(pyfi.FIMD_COMMENTS, img._dib))
    print(cfi.FreeImage_GetMetadataCount(pyfi.FIMD_EXIF_MAIN, img._dib))
    print(cfi.FreeImage_GetMetadataCount(pyfi.FIMD_EXIF_EXIF, img._dib))
    print(cfi.FreeImage_GetMetadataCount(pyfi.FIMD_EXIF_GPS, img._dib))
    print(cfi.FreeImage_GetMetadataCount(pyfi.FIMD_EXIF_MAKERNOTE, img._dib))
    print(cfi.FreeImage_GetMetadataCount(pyfi.FIMD_EXIF_INTEROP, img._dib))
    print(cfi.FreeImage_GetMetadataCount(pyfi.FIMD_IPTC, img._dib))
    print(cfi.FreeImage_GetMetadataCount(pyfi.FIMD_XMP, img._dib))
    print(cfi.FreeImage_GetMetadataCount(pyfi.FIMD_GEOTIFF, img._dib))
    print(cfi.FreeImage_GetMetadataCount(pyfi.FIMD_ANIMATION, img._dib))
    print(cfi.FreeImage_GetMetadataCount(pyfi.FIMD_CUSTOM, img._dib))
    print(cfi.FreeImage_GetMetadataCount(pyfi.FIMD_EXIF_RAW, img._dib))

    ptag = ctypes.c_void_p()
    mdmodel = pyfi.FIMD_EXIF_MAIN
    handle = cfi.FreeImage_FindFirstMetadata(mdmodel, img._dib, ctypes.byref(ptag))
    print(cfi.FreeImage_TagToString(mdmodel, ptag, None))
    print(ptag)
    tag = md.Tag(ptag)
    print(tag.key)
    print(tag.description)
    print(tag.id)
    print(tag.type, pyfi.FIDT_ASCII)
    print(tag.count)
    print(tag.length)
    print(tag.value)
    a = tag.value
    print(len(a))
