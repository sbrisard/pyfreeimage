from enum import Enum


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


class Filter(Enum):
    BOX = 0
    BICUBIC = 1
    BILINEAR = 2
    BSPLINE = 3
    CATMULLROM = 4
    LANCZOS3 = 5


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


class JpegOperation(Enum):
    OP_NONE = 0
    OP_FLIP_H = 1
    OP_FLIP_V = 2
    OP_TRANSPOSE = 3
    OP_TRANSVERSE = 4
    OP_ROTATE_90 = 5
    OP_ROTATE_180 = 6
    OP_ROTATE_270 = 7


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


class IOFlag(Enum):
    LOAD_NOPIXELS = 32768
    BMP_DEFAULT = 0
    BMP_SAVE_RLE = 1
    CUT_DEFAULT = 0
    DDS_DEFAULT = 0
    EXR_DEFAULT = 0
    EXR_FLOAT = 1
    EXR_NONE = 2
    EXR_ZIP = 4
    EXR_PIZ = 8
    EXR_PXR24 = 16
    EXR_B44 = 32
    EXR_LC = 64
    FAXG3_DEFAULT = 0
    GIF_DEFAULT = 0
    GIF_LOAD256 = 1
    GIF_PLAYBACK = 2
    HDR_DEFAULT = 0
    ICO_DEFAULT = 0
    ICO_MAKEALPHA = 1
    IFF_DEFAULT = 0
    J2K_DEFAULT = 0
    JP2_DEFAULT = 0
    JPEG_DEFAULT = 0
    JPEG_FAST = 1
    JPEG_ACCURATE = 2
    JPEG_CMYK = 4
    JPEG_EXIFROTATE = 8
    JPEG_GREYSCALE = 16
    JPEG_QUALITYSUPERB = 128
    JPEG_QUALITYGOOD = 256
    JPEG_QUALITYNORMAL = 512
    JPEG_QUALITYAVERAGE = 1024
    JPEG_QUALITYBAD = 2048
    JPEG_PROGRESSIVE = 8192
    JPEG_SUBSAMPLING_411 = 4096
    JPEG_SUBSAMPLING_420 = 16384
    JPEG_SUBSAMPLING_422 = 32768
    JPEG_SUBSAMPLING_444 = 65536
    JPEG_OPTIMIZE = 131072
    JPEG_BASELINE = 262144
    KOALA_DEFAULT = 0
    LBM_DEFAULT = 0
    MNG_DEFAULT = 0
    PCD_DEFAULT = 0
    PCD_BASE = 1
    PCD_BASEDIV4 = 2
    PCD_BASEDIV16 = 3
    PCX_DEFAULT = 0
    PFM_DEFAULT = 0
    PICT_DEFAULT = 0
    PNG_DEFAULT = 0
    PNG_IGNOREGAMMA = 1
    PNG_Z_BEST_SPEED = 1
    PNG_Z_DEFAULT_COMPRESSION = 6
    PNG_Z_BEST_COMPRESSION = 9
    PNG_Z_NO_COMPRESSION = 256
    PNG_INTERLACED = 512
    PSD_DEFAULT = 0
    PSD_CMYK = 1
    PSD_LAB = 2
    RAS_DEFAULT = 0
    RAW_DEFAULT = 0
    RAW_PREVIEW = 1
    RAW_DISPLAY = 2
    RAW_HALFSIZE = 4
    SGI_DEFAULT = 0
    TARGA_DEFAULT = 0
    TARGA_LOAD_RGB888 = 1
    TARGA_SAVE_RLE = 2
    TIFF_DEFAULT = 0
    TIFF_CMYK = 1
    TIFF_PACKBITS = 256
    TIFF_DEFLATE = 512
    TIFF_ADOBE_DEFLATE = 1024
    TIFF_NONE = 2048
    TIFF_CCITTFAX3 = 4096
    TIFF_CCITTFAX4 = 8192
    TIFF_LZW = 16384
    TIFF_JPEG = 32768
    TIFF_LOGLUV = 65536
    WBMP_DEFAULT = 0
    XBM_DEFAULT = 0
    XPM_DEFAULT = 0
    WEBP_DEFAULT = 0
    WEBP_LOSSLESS = 256
    JXR_DEFAULT = 0
    JXR_LOSSLESS = 100
    JXR_PROGRESSIVE = 8192


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


class ToneMappingOperator(Enum):
    DRAGO03 = 0
    REINHARD05 = 1
    FATTAL02 = 2


class Quantize(Enum):
    WUQUANT = 0
    NNQUANT = 1


class ColorType(Enum):
    MINISWHITE = 0
    MINISBLACK = 1
    RGB = 2
    PALETTE = 3
    RGBALPHA = 4
    CMYK = 5
