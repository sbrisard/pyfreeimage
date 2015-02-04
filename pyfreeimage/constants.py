from enum import Enum


class Type(Enum):
    unknown = 0
    bitmap = 1
    uint16 = 2
    int16 = 3
    uint32 = 4
    int32 = 5
    float = 6
    double = 7
    complex = 8
    rgb16 = 9
    rgba16 = 10
    rgbf = 11
    rgbaf = 12


class Format(Enum):
    unknown = -1
    bmp = 0
    ico = 1
    jpeg = 2
    jng = 3
    koala = 4
    lbm = 5
    iff = 5
    mng = 6
    pbm = 7
    pbmraw = 8
    pcd = 9
    pcx = 10
    pgm = 11
    pgmraw = 12
    png = 13
    ppm = 14
    ppmraw = 15
    ras = 16
    targa = 17
    tiff = 18
    wbmp = 19
    psd = 20
    cut = 21
    xbm = 22
    xpm = 23
    dds = 24
    gif = 25
    hdr = 26
    faxg3 = 27
    sgi = 28
    exr = 29
    j2k = 30
    jp2 = 31
    pfm = 32
    pict = 33
    raw = 34
    webp = 35
    jxr = 36
