import glob
import os.path

import pytest

import pyfreeimage as pyfi

from pyfreeimage import Type


def path_to_reference_images():
    return os.path.join(os.path.dirname(os.path.realpath(__file__)),
                        'images')


def pytest_generate_tests(metafunc):
    if metafunc.function == test_load:
        files = glob.glob(os.path.join(path_to_reference_images(), 'metro*'))
        params = [(name, Type.BITMAP, 320, 200,
                   24 if name.find('gray') == -1 else 8) for name in files]
        metafunc.parametrize('name, fitype, width, height, bpp', params)


def test_load(name, fitype, width, height, bpp):
    bitmap = pyfi.load(name)
    assert bitmap.fitype == fitype
    assert bitmap.width == width
    assert bitmap.height == height
    assert bitmap.bpp == bpp
