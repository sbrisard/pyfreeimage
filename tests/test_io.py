import pytest

import pyfreeimage as pyfi
import tstutil

@pytest.mark.parametrize('name, format',
                         [('5.2.10.tiff', pyfi.FIF_TIFF),
                          ('kochtreffen.jpg', pyfi.FIF_JPEG),
                          ('kodim22.png', pyfi.FIF_PNG)])
def test_file_type(name, format):
    assert pyfi.io.file_format(tstutil.path_to_image(name)) == format
