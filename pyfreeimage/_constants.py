from enum import Enum


class Format(Enum):
    UNKNOWN = -1
    BMP = 0
    ICO = 1
    JPEG = 2
    JNG = 3
    KOALA = 4
    LBM = 5
    IFF = 5
    MNG = 6
    PBM = 7
    PBMRAW = 8
    PCD = 9
    PCX = 10
    PGM = 11
    PGMRAW = 12
    PNG = 13
    PPM = 14
    PPMRAW = 15
    RAS = 16
    TARGA = 17
    TIFF = 18
    WBMP = 19
    PSD = 20
    CUT = 21
    XBM = 22
    XPM = 23
    DDS = 24
    GIF = 25
    HDR = 26
    FAXG3 = 27
    SGI = 28
    EXR = 29
    J2K = 30
    JP2 = 31
    PFM = 32
    PICT = 33
    RAW = 34
    WEBP = 35
    JXR = 36


class MetadataModel(Enum):
    NODATA = -1
    COMMENTS = 0
    EXIF_MAIN = 1
    EXIF_EXIF = 2
    EXIF_GPS = 3
    EXIF_MAKERNOTE = 4
    EXIF_INTEROP = 5
    IPTC = 6
    XMP = 7
    GEOTIFF = 8
    ANIMATION = 9
    CUSTOM = 10
    EXIF_RAW = 11


class ColorType(Enum):
    MINISWHITE = 0
    MINISBLACK = 1
    RGB = 2
    PALETTE = 3
    RGBALPHA = 4
    CMYK = 5


class ColorChannel(Enum):
    RGB = 0
    RED = 1
    GREEN = 2
    BLUE = 3
    ALPHA = 4
    BLACK = 5
    REAL = 6
    IMAG = 7
    MAG = 8
    PHASE = 9


class ToneMappingOperator(Enum):
    DRAGO03 = 0
    REINHARD05 = 1
    FATTAL02 = 2


class MetadataType(Enum):
    NOTYPE = 0
    BYTE = 1
    ASCII = 2
    SHORT = 3
    LONG = 4
    RATIONAL = 5
    SBYTE = 6
    UNDEFINED = 7
    SSHORT = 8
    SLONG = 9
    SRATIONAL = 10
    FLOAT = 11
    DOUBLE = 12
    IFD = 13
    PALETTE = 14
    LONG8 = 16
    SLONG8 = 17
    IFD8 = 18


class Quantize(Enum):
    WUQUANT = 0
    NNQUANT = 1


class JpegOperation(Enum):
    OP_NONE = 0
    OP_FLIP_H = 1
    OP_FLIP_V = 2
    OP_TRANSPOSE = 3
    OP_TRANSVERSE = 4
    OP_ROTATE_90 = 5
    OP_ROTATE_180 = 6
    OP_ROTATE_270 = 7


class Type(Enum):
    UNKNOWN = 0
    BITMAP = 1
    UINT16 = 2
    INT16 = 3
    UINT32 = 4
    INT32 = 5
    FLOAT = 6
    DOUBLE = 7
    COMPLEX = 8
    RGB16 = 9
    RGBA16 = 10
    RGBF = 11
    RGBAF = 12


class Dither(Enum):
    FS = 0
    BAYER4x4 = 1
    BAYER8x8 = 2
    CLUSTER6x6 = 3
    CLUSTER8x8 = 4
    CLUSTER16x16 = 5
    BAYER16x16 = 6


class Filter(Enum):
    BOX = 0
    BICUBIC = 1
    BILINEAR = 2
    BSPLINE = 3
    CATMULLROM = 4
    LANCZOS3 = 5
