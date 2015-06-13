import pytest

import pyfreeimage as pyfi
import tstutil

@pytest.mark.parametrize('img_name, prop_name, expected',
                         [('kochtreffen.jpg', 'fitype', pyfi.FIT_BITMAP),
                          ('kochtreffen.jpg', 'palette_size', 0),
                          ('kochtreffen.jpg', 'bpp', 24),
                          ('kochtreffen.jpg', 'width', 320),
                          ('kochtreffen.jpg', 'height', 200),
                          ('kochtreffen.jpg', 'line', 320*3),
                          ('kochtreffen.jpg', 'pitch', 320*3),
                         ])
def test_property(img_name, prop_name, expected):
    img = tstutil.load_image(img_name)
    actual = getattr(img, prop_name)
    assert actual == expected


def test_copy():
    img1 = tstutil.load_image('5.2.10.tiff')
    img2 = img1.copy()
    assert img1 is not img2
    assert img1._dib != img2._dib
    assert img1.fitype == img2.fitype
    assert img1.width == img2.width
    assert img1.height == img2.height
    assert img1.bpp == img2.bpp


@pytest.mark.parametrize('width, height, bpp, rmask, gmask, bmask, fitype',
                         [(320, 200, 24, 0, 0, 0, pyfi.FIT_BITMAP),
                          (320, 200, 64, 0, 0, 0, pyfi.FIT_DOUBLE)])
def test_empty(width, height, bpp, rmask, gmask, bmask, fitype):
    img = pyfi.image.empty(width, height, bpp, rmask, gmask, bmask, fitype)
    assert img.width == width
    assert img.height == height
    assert img.bpp == bpp
    assert img.fitype == fitype
