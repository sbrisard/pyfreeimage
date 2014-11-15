import pytest

import pyfreeimage as pyfi

def test_get_version():
    assert pyfi.get_version() == b'3.16.0'
