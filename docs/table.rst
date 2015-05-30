.. -*- coding: utf-8 -*-

Correspondence between C and Python functions
=============================================

The present page lists the original C functions defined in the API doc of FreeImage, as well as their Python counterpart. The tables below give an accurate image of the project advancement.


Bitmap functions
----------------


General functions
^^^^^^^^^^^^^^^^^

============================= =========================================
C                             Python
============================= =========================================
FreeImage_Initialise          Not needed [#fn1]_
FreeImage_DeInitialise        Not needed [#fn1]_
FreeImage_GetVersion          :data:`pyfreeimage.__version__`
FreeImage_GetCopyrightMessage :data:`pyfreeimage.__copyright_message__`
FreeImage_SetOutputMessage    Not implemented
============================= =========================================


Bitmap management functions
^^^^^^^^^^^^^^^^^^^^^^^^^^^

======================== ======
C                        Python
======================== ======
FreeImage_Allocate
FreeImage_AllocateT
FreeImage_Load
FreeImage_LoadU
FreeImage_LoadFromHandle
FreeImage_Save
FreeImage_SaveU
FreeImage_SaveToHandle
FreeImage_Clone
FreeImage_Unload
======================== ======


Bitmap information functions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

============================== ======
C                              Python
============================== ======
FreeImage_GetImageType
FreeImage_GetColorsUsed
FreeImage_GetBPP
FreeImage_GetWidth
FreeImage_GetHeight
FreeImage_GetLine
FreeImage_GetPitch
FreeImage_GetDIBSize
FreeImage_GetPalette
FreeImage_GetDotsPerMeterX
FreeImage_GetDotsPerMeterY
FreeImage_SetDotsPerMeterX
FreeImage_SetDotsPerMeterY
FreeImage_GetInfoHeader
FreeImage_GetInfo
FreeImage_GetColorType
FreeImage_GetRedMask
FreeImage_GetGreenMask
FreeImage_GetBlueMask
FreeImage_GetTransparencyCount
FreeImage_GetTransparencyTable
FreeImage_SetTransparencyTable
FreeImage_SetTransparent
FreeImage_IsTransparent
FreeImage_SetTransparentIndex
FreeImage_GetTransparentIndex
FreeImage_HasBackgroundColor
FreeImage_GetBackgroundColor
FreeImage_SetBackgroundColor
FreeImage_HasPixels
FreeImage_GetThumbnail
FreeImage_SetThumbnail
============================== ======


Filetype functions
^^^^^^^^^^^^^^^^^^

=============================== ======
C                               Python
=============================== ======
FreeImage_GetFileType
FreeImage_GetFileTypeU
FreeImage_GetFileTypeFromHandle
FreeImage_GetFileTypeFromMemory
=============================== ======


Pixel access functions
^^^^^^^^^^^^^^^^^^^^^^

======================= ======
C                       Python
======================= ======
FreeImage_GetBits
FreeImage_GetScanLine
FreeImage_GetPixelIndex
FreeImage_GetPixelColor
FreeImage_SetPixelIndex
FreeImage_SetPixelColor
======================= ======


Conversion functions
^^^^^^^^^^^^^^^^^^^^

=============================== ======
C                               Python
=============================== ======
FreeImage_ConvertTo4Bits
FreeImage_ConvertTo8Bits
FreeImage_ConvertToGreyscale
FreeImage_ConvertTo16Bits555
FreeImage_ConvertTo16Bits565
FreeImage_ConvertTo24Bits
FreeImage_ConvertTo32Bits
FreeImage_ColorQuantize
FreeImage_ColorQuantizeEx
FreeImage_Threshold
FreeImage_Dither
FreeImage_ConvertFromRawBits
FreeImage_ConvertToRawBits
FreeImage_ConvertToStandardType
FreeImage_ConvertToFloat
FreeImage_ConvertToRGBF
FreeImage_ConvertToUINT16
FreeImage_ConvertToRGB16
=============================== ======


Tone mapping operators
^^^^^^^^^^^^^^^^^^^^^^

========================= ======
C                         Python
========================= ======
FreeImage_ToneMapping
FreeImage_TmoDrago03
FreeImage_TmoReinhard05
FreeImage_TmoReinhard05Ex
FreeImage_TmoFattal02
========================= ======


ICC profile functions
^^^^^^^^^^^^^^^^^^^^^

=========================== ======
C                           Python
=========================== ======
FreeImage_GetICCProfile
FreeImage_CreateICCProfile
FreeImage_DestroyICCProfile
=========================== ======


Plugin functions
^^^^^^^^^^^^^^^^

================================ ======
C                                Python
================================ ======
FreeImage_GetFIFCount
FreeImage_SetPluginEnabled
FreeImage_IsPluginEnabled
FreeImage_GetFIFFromFormat
FreeImage_GetFIFFromMime
FreeImage_GetFIFMimeType
FreeImage_GetFormatFromFIF
FreeImage_GetFIFExtensionList
FreeImage_GetFIFDescription
FreeImage_GetFIFRegExpr
FreeImage_GetFIFFromFilename
FreeImage_GetFIFFromFilenameU
FreeImage_FIFSupportsReading
FreeImage_FIFSupportsWriting
FreeImage_FIFSupportsExportType
FreeImage_FIFSupportsExportBPP
FreeImage_FIFSupportsICCProfiles
FreeImage_FIFSupportsNoPixels
FreeImage_RegisterLocalPlugin
FreeImage_RegisterExternalPlugin
================================ ======


Multipage functions
^^^^^^^^^^^^^^^^^^^

=================================== ======
C                                   Python
=================================== ======
FreeImage_OpenMultiBitmap
FreeImage_OpenMultiBitmapFromHandle
FreeImage_SaveMultiBitmapToHandle
FreeImage_CloseMultiBitmap
FreeImage_GetPageCount
FreeImage_AppendPage
FreeImage_InsertPage
FreeImage_DeletePage
FreeImage_LockPage
FreeImage_UnlockPage
FreeImage_MovePage
FreeImage_GetLockedPageNumbers
=================================== ======


Memory I/O streams
^^^^^^^^^^^^^^^^^^

=================================== ======
C                                   Python
=================================== ======
FreeImage_OpenMemory
FreeImage_CloseMemory
FreeImage_LoadFromMemory
FreeImage_SaveToMemory
FreeImage_AcquireMemory
FreeImage_TellMemory
FreeImage_SeekMemory
FreeImage_ReadMemory
FreeImage_WriteMemory
FreeImage_LoadMultiBitmapFromMemory
FreeImage_SaveMultiBitmapToMemory
=================================== ======


Compression functions
^^^^^^^^^^^^^^^^^^^^^

======================== ======
C                        Python
======================== ======
FreeImage_ZLibCompress
FreeImage_ZLibUncompress
FreeImage_ZLibGZip
FreeImage_ZLibCRC32
FreeImage_ZlibGUnzip
======================== ======


Helper functions
^^^^^^^^^^^^^^^^

======================== ======
C                        Python
======================== ======
FreeImage_IsLittleEndian
FreeImage_LookupX11Color
FreeImage_LookupSVGColor
======================== ======


Metadata functions
------------------


Tag creation and destruction
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

=================== =====================================
C                   Python
=================== =====================================
FreeImage_CreateTag
FreeImage_DeleteTag
FreeImage_CloneTag  :func:`pyfreeimage.metadata.Tag.copy`
=================== =====================================


Tag accessors
^^^^^^^^^^^^^

=========================== ============================================
C                           Python
=========================== ============================================
FreeImage_GetTagKey         :func:`pyfreeimage.metadata.Tag.key`
FreeImage_GetTagDescription :func:`pyfreeimage.metadata.Tag.description`
FreeImage_GetTagID          :func:`pyfreeimage.metadata.Tag.id`
FreeImage_GetTagType        :func:`pyfreeimage.metadata.Tag.type`
FreeImage_GetTagCount       :func:`pyfreeimage.metadata.Tag.count`
FreeImage_GetTagLength
FreeImage_GetTagValue       :func:`pyfreeimage.metadata.Tag.value`
FreeImage_SetTagKey
FreeImage_SetTagDescription
FreeImage_SetTagID
FreeImage_SetTagType
FreeImage_SetTagCount
FreeImage_SetTagLength
FreeImage_SetTagValue
=========================== ============================================


Metadata iterator
^^^^^^^^^^^^^^^^^

=========================== ====================================
C                           Python
=========================== ====================================
FreeImage_FindFirstMetadata :func:`pyfreeimage.image.Image.tags`
FreeImage_FindNextMetadata  :func:`pyfreeimage.image.Image.tags`
FreeImage_FindCloseMetadata :func:`pyfreeimage.image.Image.tags`
=========================== ====================================


Metadata accessors
^^^^^^^^^^^^^^^^^^

===================== ===================================
C                     Python
===================== ===================================
FreeImage_GetMetadata :func:`pyfreeimage.image.Image.tag`
FreeImage_SetMetadata
===================== ===================================


Metadata helper functions
^^^^^^^^^^^^^^^^^^^^^^^^^

========================== ======================================
C                          Python
========================== ======================================
FreeImage_GetMetadataCount
FreeImage_CloneMetadata
FreeImage_TagToString      :func:`pyfreeimage.metadata.Tag.value`
========================== ======================================


Toolkit functions
-----------------


Rotation and flipping
^^^^^^^^^^^^^^^^^^^^^

======================== ======
C                        Python
======================== ======
FreeImage_Rotate
FreeImage_RotateEx
FreeImage_FlipHorizontal
FreeImage_FlipVertical
======================== ======


Upsampling / downsampling
^^^^^^^^^^^^^^^^^^^^^^^^^

======================= ======
C                       Python
======================= ======
FreeImage_Rescale
FreeImage_MakeThumbnail
======================= ======


Color manipulation
^^^^^^^^^^^^^^^^^^

==================================== ======
C                                    Python
==================================== ======
FreeImage_AdjustCurve
FreeImage_AdjustGamma
FreeImage_AdjustBrightness
FreeImage_AdjustContrast
FreeImage_Invert
FreeImage_GetHistogram
FreeImage_GetAdjustColorsLookupTable
FreeImage_AdjustColors
FreeImage_ApplyColorMapping
FreeImage_SwapColors
FreeImage_ApplyPaletteIndexMapping
FreeImage_SwapPaletteIndices
==================================== ======


Channel processing
^^^^^^^^^^^^^^^^^^

=========================== ======
C                           Python
=========================== ======
FreeImage_GetChannel
FreeImage_SetChannel
FreeImage_GetComplexChannel
FreeImage_SetComplexChannel
=========================== ======


Copy / Paste / Composite routines
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

============================== ======
C                              Python
============================== ======
FreeImage_Copy
FreeImage_Paste
FreeImage_Composite
FreeImage_PreMultiplyWithAlpha
============================== ======


JPEG lossless transformations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

========================================= ======
C                                         Python
========================================= ======
FreeImage_JPEGTransform
FreeImage_JPEGTransformU
FreeImage_JPEGCrop
FreeImage_JPEGCropU
FreeImage_JPEGTransformCombined
FreeImage_JPEGTransformCombinedU
FreeImage_JPEGTransformCombinedFromMemory
========================================= ======


Background filling
^^^^^^^^^^^^^^^^^^

======================== ======
C                        Python
======================== ======
FreeImage_FillBackground
FreeImage_EnlargeCanvas
FreeImage_AllocateEx
FreeImage_AllocateExT
======================== ======


Miscellaneous algorithms
^^^^^^^^^^^^^^^^^^^^^^^^

================================ ======
C                                Python
================================ ======
FreeImage_MultigridPoissonSolver
================================ ======

.. rubric:: Footnotes

.. [#fn1] Automatically called when using the dynamic version of the library.
