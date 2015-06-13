import pytest

import pyfreeimage as pyfi
import tstutil


@pytest.mark.parametrize('name, width, height',
                         [('kochtreffen.jpg', 160, 100)])
def test_rescale(name, width, height):
    img = pyfi.transform.rescale(tstutil.load_image(name), width, height)
    assert img.width == width
    assert img.height == height
