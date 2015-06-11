.. -*- coding: utf-8 -*-

Dashboard
=========

The present page lists the original C functions defined in the API doc of FreeImage, as well as their Python counterpart. The tables below give an accurate image of the project advancement. The same ordering as the FreeImage documentation is adopted below.


.. contents:: Contents
   :local:


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

======================== ====================================
C                        Python
======================== ====================================
FreeImage_Allocate       Not implemented
FreeImage_AllocateT      :func:`pyfreeimage.image.empty`
FreeImage_Load           :func:`pyfreeimage.io.load`
FreeImage_LoadU          Not implemented [#fn2]_
FreeImage_LoadFromHandle Not implemented
FreeImage_Save           :func:`pyfreeimage.io.save`
FreeImage_SaveU          Not implemented [#fn2]_
FreeImage_SaveToHandle   Not implemented
FreeImage_Clone          :func:`pyfreeimage.image.Image.copy`
FreeImage_Unload         Not exposed [#fn3]_
======================== ====================================


Bitmap information functions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

============================== ============================================
C                              Python
============================== ============================================
FreeImage_GetImageType         :attr:`pyfreeimage.image.Image.fitype`
FreeImage_GetColorsUsed        :attr:`pyfreeimage.image.Image.palette_size`
FreeImage_GetBPP               :attr:`pyfreeimage.image.Image.bpp`
FreeImage_GetWidth             :attr:`pyfreeimage.image.Image.width`
FreeImage_GetHeight            :attr:`pyfreeimage.image.Image.height`
FreeImage_GetLine              :attr:`pyfreeimage.image.Image.line`
FreeImage_GetPitch             :attr:`pyfreeimage.image.Image.pitch`
FreeImage_GetDIBSize           Not implemented
FreeImage_GetPalette           Not implemented
FreeImage_GetDotsPerMeterX     Not implemented
FreeImage_GetDotsPerMeterY     Not implemented
FreeImage_SetDotsPerMeterX     Not implemented
FreeImage_SetDotsPerMeterY     Not implemented
FreeImage_GetInfoHeader        Not implemented
FreeImage_GetInfo              Not implemented
FreeImage_GetColorType         Not implemented
FreeImage_GetRedMask           Not implemented
FreeImage_GetGreenMask         Not implemented
FreeImage_GetBlueMask          Not implemented
FreeImage_GetTransparencyCount Not implemented
FreeImage_GetTransparencyTable Not implemented
FreeImage_SetTransparencyTable Not implemented
FreeImage_SetTransparent       Not implemented
FreeImage_IsTransparent        Not implemented
FreeImage_SetTransparentIndex  Not implemented
FreeImage_GetTransparentIndex  Not implemented
FreeImage_HasBackgroundColor   Not implemented
FreeImage_GetBackgroundColor   Not implemented
FreeImage_SetBackgroundColor   Not implemented
FreeImage_HasPixels            Not implemented
FreeImage_GetThumbnail         Not implemented
FreeImage_SetThumbnail         Not implemented
============================== ============================================


Filetype functions
^^^^^^^^^^^^^^^^^^

=============================== ==================================
C                               Python
=============================== ==================================
FreeImage_GetFileType           :func:`pyfreeimage.io.file_format`
FreeImage_GetFileTypeU          Not implemented
FreeImage_GetFileTypeFromHandle Not implemented
FreeImage_GetFileTypeFromMemory Not implemented
=============================== ==================================


Pixel access functions
^^^^^^^^^^^^^^^^^^^^^^

======================= ===============
C                       Python
======================= ===============
FreeImage_GetBits       Not implemented
FreeImage_GetScanLine   Not implemented
FreeImage_GetPixelIndex Not implemented
FreeImage_GetPixelColor Not implemented
FreeImage_SetPixelIndex Not implemented
FreeImage_SetPixelColor Not implemented
======================= ===============


Conversion functions
^^^^^^^^^^^^^^^^^^^^

=============================== ===============
C                               Python
=============================== ===============
FreeImage_ConvertTo4Bits        Not implemented
FreeImage_ConvertTo8Bits        Not implemented
FreeImage_ConvertToGreyscale    Not implemented
FreeImage_ConvertTo16Bits555    Not implemented
FreeImage_ConvertTo16Bits565    Not implemented
FreeImage_ConvertTo24Bits       Not implemented
FreeImage_ConvertTo32Bits       Not implemented
FreeImage_ColorQuantize         Not implemented
FreeImage_ColorQuantizeEx       Not implemented
FreeImage_Threshold             Not implemented
FreeImage_Dither                Not implemented
FreeImage_ConvertFromRawBits    Not implemented
FreeImage_ConvertToRawBits      Not implemented
FreeImage_ConvertToStandardType Not implemented
FreeImage_ConvertToFloat        Not implemented
FreeImage_ConvertToRGBF         Not implemented
FreeImage_ConvertToUINT16       Not implemented
FreeImage_ConvertToRGB16        Not implemented
=============================== ===============


Tone mapping operators
^^^^^^^^^^^^^^^^^^^^^^

========================= ===============
C                         Python
========================= ===============
FreeImage_ToneMapping     Not implemented
FreeImage_TmoDrago03      Not implemented
FreeImage_TmoReinhard05   Not implemented
FreeImage_TmoReinhard05Ex Not implemented
FreeImage_TmoFattal02     Not implemented
========================= ===============


ICC profile functions
^^^^^^^^^^^^^^^^^^^^^

=========================== ===============
C                           Python
=========================== ===============
FreeImage_GetICCProfile     Not implemented
FreeImage_CreateICCProfile  Not implemented
FreeImage_DestroyICCProfile Not implemented
=========================== ===============


Plugin functions
^^^^^^^^^^^^^^^^

================================ ===============
C                                Python
================================ ===============
FreeImage_GetFIFCount            Not implemented
FreeImage_SetPluginEnabled       Not implemented
FreeImage_IsPluginEnabled        Not implemented
FreeImage_GetFIFFromFormat       Not implemented
FreeImage_GetFIFFromMime         Not implemented
FreeImage_GetFIFMimeType         Not implemented
FreeImage_GetFormatFromFIF       Not implemented
FreeImage_GetFIFExtensionList    Not implemented
FreeImage_GetFIFDescription      Not implemented
FreeImage_GetFIFRegExpr          Not implemented
FreeImage_GetFIFFromFilename     Not implemented
FreeImage_GetFIFFromFilenameU    Not implemented
FreeImage_FIFSupportsReading     Not implemented
FreeImage_FIFSupportsWriting     Not implemented
FreeImage_FIFSupportsExportType  Not implemented
FreeImage_FIFSupportsExportBPP   Not implemented
FreeImage_FIFSupportsICCProfiles Not implemented
FreeImage_FIFSupportsNoPixels    Not implemented
FreeImage_RegisterLocalPlugin    Not implemented
FreeImage_RegisterExternalPlugin Not implemented
================================ ===============


Multipage functions
^^^^^^^^^^^^^^^^^^^

=================================== ===============
C                                   Python
=================================== ===============
FreeImage_OpenMultiBitmap           Not implemented
FreeImage_OpenMultiBitmapFromHandle Not implemented
FreeImage_SaveMultiBitmapToHandle   Not implemented
FreeImage_CloseMultiBitmap          Not implemented
FreeImage_GetPageCount              Not implemented
FreeImage_AppendPage                Not implemented
FreeImage_InsertPage                Not implemented
FreeImage_DeletePage                Not implemented
FreeImage_LockPage                  Not implemented
FreeImage_UnlockPage                Not implemented
FreeImage_MovePage                  Not implemented
FreeImage_GetLockedPageNumbers      Not implemented
=================================== ===============


Memory I/O streams
^^^^^^^^^^^^^^^^^^

=================================== ===============
C                                   Python
=================================== ===============
FreeImage_OpenMemory                Not implemented
FreeImage_CloseMemory               Not implemented
FreeImage_LoadFromMemory            Not implemented
FreeImage_SaveToMemory              Not implemented
FreeImage_AcquireMemory             Not implemented
FreeImage_TellMemory                Not implemented
FreeImage_SeekMemory                Not implemented
FreeImage_ReadMemory                Not implemented
FreeImage_WriteMemory               Not implemented
FreeImage_LoadMultiBitmapFromMemory Not implemented
FreeImage_SaveMultiBitmapToMemory   Not implemented
=================================== ===============


Compression functions
^^^^^^^^^^^^^^^^^^^^^

======================== ===============
C                        Python
======================== ===============
FreeImage_ZLibCompress   Not implemented
FreeImage_ZLibUncompress Not implemented
FreeImage_ZLibGZip       Not implemented
FreeImage_ZLibCRC32      Not implemented
FreeImage_ZlibGUnzip     Not implemented
======================== ===============


Helper functions
^^^^^^^^^^^^^^^^

======================== ===============
C                        Python
======================== ===============
FreeImage_IsLittleEndian Not implemented
FreeImage_LookupX11Color Not implemented
FreeImage_LookupSVGColor Not implemented
======================== ===============


Metadata functions
------------------


Tag creation and destruction
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

=================== =====================================
C                   Python
=================== =====================================
FreeImage_CreateTag Not implemented
FreeImage_DeleteTag Not implemented
FreeImage_CloneTag  :func:`pyfreeimage.metadata.Tag.copy`
=================== =====================================


Tag accessors
^^^^^^^^^^^^^

=========================== ============================================
C                           Python
=========================== ============================================
FreeImage_GetTagKey         :data:`pyfreeimage.metadata.Tag.key`
FreeImage_GetTagDescription :data:`pyfreeimage.metadata.Tag.description`
FreeImage_GetTagID          :data:`pyfreeimage.metadata.Tag.id`
FreeImage_GetTagType        :data:`pyfreeimage.metadata.Tag.type`
FreeImage_GetTagCount       :data:`pyfreeimage.metadata.Tag.count`
FreeImage_GetTagLength      Not implemented
FreeImage_GetTagValue       :data:`pyfreeimage.metadata.Tag.value`
FreeImage_SetTagKey         Not implemented
FreeImage_SetTagDescription Not implemented
FreeImage_SetTagID          Not implemented
FreeImage_SetTagType        Not implemented
FreeImage_SetTagCount       Not implemented
FreeImage_SetTagLength      Not implemented
FreeImage_SetTagValue       Not implemented
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
FreeImage_SetMetadata Not implemented
===================== ===================================


Metadata helper functions
^^^^^^^^^^^^^^^^^^^^^^^^^

========================== ========================================
C                          Python
========================== ========================================
FreeImage_GetMetadataCount Not implemented
FreeImage_CloneMetadata    :func:`pyfreeimage.metadata.Tag.copy`
FreeImage_TagToString      :func:`pyfreeimage.metadata.Tag.__str__`
========================== ========================================


Toolkit functions
-----------------


Rotation and flipping
^^^^^^^^^^^^^^^^^^^^^

======================== ===============
C                        Python
======================== ===============
FreeImage_Rotate         Not implemented
FreeImage_RotateEx       Not implemented
FreeImage_FlipHorizontal Not implemented
FreeImage_FlipVertical   Not implemented
======================== ===============


Upsampling / downsampling
^^^^^^^^^^^^^^^^^^^^^^^^^

======================= ===============
C                       Python
======================= ===============
FreeImage_Rescale       Not implemented
FreeImage_MakeThumbnail Not implemented
======================= ===============


Color manipulation
^^^^^^^^^^^^^^^^^^

==================================== ===============
C                                    Python
==================================== ===============
FreeImage_AdjustCurve                Not implemented
FreeImage_AdjustGamma                Not implemented
FreeImage_AdjustBrightness           Not implemented
FreeImage_AdjustContrast             Not implemented
FreeImage_Invert                     Not implemented
FreeImage_GetHistogram               Not implemented
FreeImage_GetAdjustColorsLookupTable Not implemented
FreeImage_AdjustColors               Not implemented
FreeImage_ApplyColorMapping          Not implemented
FreeImage_SwapColors                 Not implemented
FreeImage_ApplyPaletteIndexMapping   Not implemented
FreeImage_SwapPaletteIndices         Not implemented
==================================== ===============


Channel processing
^^^^^^^^^^^^^^^^^^

=========================== ===============
C                           Python
=========================== ===============
FreeImage_GetChannel        Not implemented
FreeImage_SetChannel        Not implemented
FreeImage_GetComplexChannel Not implemented
FreeImage_SetComplexChannel Not implemented
=========================== ===============


Copy / Paste / Composite routines
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

============================== ===============
C                              Python
============================== ===============
FreeImage_Copy                 Not implemented
FreeImage_Paste                Not implemented
FreeImage_Composite            Not implemented
FreeImage_PreMultiplyWithAlpha Not implemented
============================== ===============


JPEG lossless transformations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

========================================= ===============
C                                         Python
========================================= ===============
FreeImage_JPEGTransform                   Not implemented
FreeImage_JPEGTransformU                  Not implemented
FreeImage_JPEGCrop                        Not implemented
FreeImage_JPEGCropU                       Not implemented
FreeImage_JPEGTransformCombined           Not implemented
FreeImage_JPEGTransformCombinedU          Not implemented
FreeImage_JPEGTransformCombinedFromMemory Not implemented
========================================= ===============


Background filling
^^^^^^^^^^^^^^^^^^

======================== ===============
C                        Python
======================== ===============
FreeImage_FillBackground Not implemented
FreeImage_EnlargeCanvas  Not implemented
FreeImage_AllocateEx     Not implemented
FreeImage_AllocateExT    Not implemented
======================== ===============


Miscellaneous algorithms
^^^^^^^^^^^^^^^^^^^^^^^^

================================ ===============
C                                Python
================================ ===============
FreeImage_MultigridPoissonSolver Not implemented
================================ ===============

.. rubric:: Footnotes

.. [#fn1] Automatically called when using the dynamic version of the library.
.. [#fn2] Works on MS Windows only: a test on the platform should be
          implemented.
.. [#fn3] This function is automatically called on object destruction by means
          of weak references (see also :ref:`memory-leaks`)
