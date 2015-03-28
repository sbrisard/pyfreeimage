import glob
import os.path

import pytest

import pyfreeimage as pyfi


PATH_TO_IMAGES = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                              'images')


def load_metro_tiff():
    return pyfi.io.load(os.path.join(PATH_TO_IMAGES, 'metro.tif'))


def pytest_generate_tests(metafunc):
    if metafunc.function == test_load:
        files = glob.glob(os.path.join(PATH_TO_IMAGES, 'metro*'))
        params = [(name, pyfi.FIT_BITMAP,
                   0 if name.find('gray') == -1 else 256,
                   24 if name.find('gray') == -1 else 8,
                   320, 200) for name in files]
        metafunc.parametrize('name, fitype, palette_size, bpp, width, height',
                             params)


def test_load(name, fitype, palette_size, bpp, width, height):
    bitmap = pyfi.io.load(name)
    assert bitmap.fitype == fitype
    assert bitmap.palette_size == palette_size
    assert bitmap.bpp == bpp
    assert bitmap.width == width
    assert bitmap.height == height
    assert bitmap.line == (bitmap.width * bitmap.bpp) // 8


def test_copy():
    img1 = load_metro_tiff()
    img2 = img1.copy()
    assert img1 is not img2
    assert img1._dib != img2._dib
    assert img1.fitype == img2.fitype
    assert img1.width == img2.width
    assert img1.height == img2.height
    assert img1.bpp == img2.bpp
