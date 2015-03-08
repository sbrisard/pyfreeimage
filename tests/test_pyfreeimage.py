import pytest

import pyfreeimage as pyfi

from pyfreeimage import Type

def test_get_version():
    assert pyfi.__version__ == '3.16.0'

@pytest.mark.parametrize('name, fitype, width, height, bpp',
                         [(b'data/mountain.tif', Type.BITMAP, 640, 480, 8),
                          (b'data/tulips.tif', Type.BITMAP, 768, 512, 24)])
def test_load(name, fitype, width, height, bpp):
    bitmap = pyfi.load(name)
    assert bitmap.fitype == fitype
    assert bitmap.width == width
    assert bitmap.height == height
    assert bitmap.bpp == bpp
