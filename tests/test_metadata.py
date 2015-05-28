import tstutil

def test_Image_dot_tags():
    img = tstutil.load_image('5.2.10.tiff')
    expected = {b'BitsPerSample': 8,
                b'Compression': 1,
                b'ImageLength': 512,
                b'ImageWidth': 512,
                b'PhotometricInterpretation': 1,
                b'PlanarConfiguration': 1,
                b'RowsPerStrip': 16,
                b'SamplesPerPixel': 1,
                b'StripByteCounts': 8192,
                b'StripOffsets': 8}
    for tag in img.tags():
        val = tag.value
        assert len(val) == 1
        assert val[0] == expected[tag.key]

def test_Image_dot_tag():
    img = tstutil.load_image('5.2.10.tiff')
    actual = img.tag(b'RowsPerStrip').value
    assert len(actual)
    assert actual[0] == 16
    assert img.tag(b'inexisting') is None
