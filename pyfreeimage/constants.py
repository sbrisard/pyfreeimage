
# FREE_IMAGE_FORMAT

FIF_UNKNOWN = -1
FIF_BMP = 0
FIF_ICO = 1
FIF_JPEG = 2
FIF_JNG = 3
FIF_KOALA = 4
FIF_LBM = 5
FIF_IFF = 5
FIF_MNG = 6
FIF_PBM = 7
FIF_PBMRAW = 8
FIF_PCD = 9
FIF_PCX = 10
FIF_PGM = 11
FIF_PGMRAW = 12
FIF_PNG = 13
FIF_PPM = 14
FIF_PPMRAW = 15
FIF_RAS = 16
FIF_TARGA = 17
FIF_TIFF = 18
FIF_WBMP = 19
FIF_PSD = 20
FIF_CUT = 21
FIF_XBM = 22
FIF_XPM = 23
FIF_DDS = 24
FIF_GIF = 25
FIF_HDR = 26
FIF_FAXG3 = 27
FIF_SGI = 28
FIF_EXR = 29
FIF_J2K = 30
FIF_JP2 = 31
FIF_PFM = 32
FIF_PICT = 33
FIF_RAW = 34
FIF_WEBP = 35
FIF_JXR = 36

# FREE_IMAGE_FILTER

FILTER_BOX = 0
FILTER_BICUBIC = 1
FILTER_BILINEAR = 2
FILTER_BSPLINE = 3
FILTER_CATMULLROM = 4
FILTER_LANCZOS3 = 5

# FREE_IMAGE_TMO

FITMO_DRAGO03 = 0
FITMO_REINHARD05 = 1
FITMO_FATTAL02 = 2

# FREE_IMAGE_JPEG_OPERATION

FIJPEG_OP_NONE = 0
FIJPEG_OP_FLIP_H = 1
FIJPEG_OP_FLIP_V = 2
FIJPEG_OP_TRANSPOSE = 3
FIJPEG_OP_TRANSVERSE = 4
FIJPEG_OP_ROTATE_90 = 5
FIJPEG_OP_ROTATE_180 = 6
FIJPEG_OP_ROTATE_270 = 7

# FREE_IMAGE_DITHER

FID_FS = 0
FID_BAYER4x4 = 1
FID_BAYER8x8 = 2
FID_CLUSTER6x6 = 3
FID_CLUSTER8x8 = 4
FID_CLUSTER16x16 = 5
FID_BAYER16x16 = 6

# FREE_IMAGE_COLOR_TYPE

FIC_MINISWHITE = 0
FIC_MINISBLACK = 1
FIC_RGB = 2
FIC_PALETTE = 3
FIC_RGBALPHA = 4
FIC_CMYK = 5

# FREE_IMAGE_QUANTIZE

FIQ_WUQUANT = 0
FIQ_NNQUANT = 1

# FREE_IMAGE_MDTYPE

FIDT_NOTYPE = 0
FIDT_BYTE = 1
FIDT_ASCII = 2
FIDT_SHORT = 3
FIDT_LONG = 4
FIDT_RATIONAL = 5
FIDT_SBYTE = 6
FIDT_UNDEFINED = 7
FIDT_SSHORT = 8
FIDT_SLONG = 9
FIDT_SRATIONAL = 10
FIDT_FLOAT = 11
FIDT_DOUBLE = 12
FIDT_IFD = 13
FIDT_PALETTE = 14
FIDT_LONG8 = 16
FIDT_SLONG8 = 17
FIDT_IFD8 = 18

# FREE_IMAGE_MDMODEL

FIMD_NODATA = -1
FIMD_COMMENTS = 0
FIMD_EXIF_MAIN = 1
FIMD_EXIF_EXIF = 2
FIMD_EXIF_GPS = 3
FIMD_EXIF_MAKERNOTE = 4
FIMD_EXIF_INTEROP = 5
FIMD_IPTC = 6
FIMD_XMP = 7
FIMD_GEOTIFF = 8
FIMD_ANIMATION = 9
FIMD_CUSTOM = 10
FIMD_EXIF_RAW = 11

# FREE_IMAGE_COLOR_CHANNEL

FICC_RGB = 0
FICC_RED = 1
FICC_GREEN = 2
FICC_BLUE = 3
FICC_ALPHA = 4
FICC_BLACK = 5
FICC_REAL = 6
FICC_IMAG = 7
FICC_MAG = 8
FICC_PHASE = 9

# FREE_IMAGE_TYPE

FIT_UNKNOWN = 0
FIT_BITMAP = 1
FIT_UINT16 = 2
FIT_INT16 = 3
FIT_UINT32 = 4
FIT_INT32 = 5
FIT_FLOAT = 6
FIT_DOUBLE = 7
FIT_COMPLEX = 8
FIT_RGB16 = 9
FIT_RGBA16 = 10
FIT_RGBF = 11
FIT_RGBAF = 12

# I/O flags

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
