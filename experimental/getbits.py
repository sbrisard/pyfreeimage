import ctypes

import os.path
import numpy.ctypeslib
import pyfreeimage as fi

from numpy.lib.stride_tricks import as_strided

from pyfreeimage._c_api import cfi, init_signature

if __name__ == '__main__':

    init_signature('GetBits', ctypes.POINTER(ctypes.c_ubyte),
                   [ctypes.c_void_p])

    path = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                        '..',
                        'tests',
                        'images')
    img = fi.io.load(os.path.join(path, 'metro-gray.tif'))

    data = numpy.ctypeslib.as_array(cfi.FreeImage_GetBits(img._dib),
                                    shape=(img.line * img.height,))

    new_shape = (img.height, img.width)
    new_strides = (img.line, 1)
    a = as_strided(data, shape=new_shape, strides=new_strides)

    b = a[::-1, :].copy()

    img = fi.io.load(os.path.join(path, 'metro.tif'))

    data = numpy.ctypeslib.as_array(cfi.FreeImage_GetBits(img._dib),
                                    shape=(img.line * img.height,))

    new_shape = (img.height, img.width, 3)
    new_strides = (img.line, 3, 1)
    a = as_strided(data, shape=new_shape, strides=new_strides)

    c = a[::-1, :, ::-1].copy()
