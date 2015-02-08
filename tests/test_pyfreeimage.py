import pytest

import pyfreeimage.pyfreeimage as pyfi

from pyfreeimage.pyfreeimage import Type

def test_get_version():
    assert pyfi.get_version() == b'3.16.0'

@pytest.mark.parametrize('name, fitype, width, height, bpp',
                         [(b'data/mountain.tif', Type.bitmap, 640, 480, 8),
                          (b'data/tulips.tif', Type.bitmap, 768, 512, 24)])
def test_load(name, fitype, width, height, bpp):
    bitmap = pyfi.load(name)
    assert bitmap.itype == fitype
    assert bitmap.width == width
    assert bitmap.height == height
    assert bitmap.bpp == bpp
