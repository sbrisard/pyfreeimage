.. -*- coding: utf-8 -*-

Correspondence between C and Python functions
=============================================

The present page lists the original C functions defined in the API doc of FreeImage, as well as their Python counterpart. The tables below give an accurate image of the project advancement.

Bitmap functions
----------------

Metadata functions
------------------

=============================== ===========================================
C                               Python
=============================== ===========================================
``FreeImage_CreateTag``         *Not implemented*
``FreeImage_DeleteTag``         *Not implemented*
``FreeImage_CloneTag``          :func:`pyfreeimage.metadata.Tag.copy`
``FreeImage_GetTagKey``         :func:`pyfreeimage.metadata.Tag.key`
``FreeImage_GetTagDescription`` :func:`pyfreeimage.metadata.Tag.description`
``FreeImage_GetTagID``          :func:`pyfreeimage.metadata.Tag.id`
``FreeImage_GetTagType``        :func:`pyfreeimage.metadata.Tag.type`
``FreeImage_GetTagCount``       :func:`pyfreeimage.metadata.Tag.count`
``FreeImage_GetTagLength``      *Not implemented*
``FreeImage_GetTagValue``       :func:`pyfreeimage.metadata.Tag.value`
``FreeImage_SetTagKey``         *Not implemented*
``FreeImage_SetTagDescription`` *Not implemented*
``FreeImage_SetTagID``          *Not implemented*
``FreeImage_SetTagType``        *Not implemented*
``FreeImage_SetTagCount``       *Not implemented*
``FreeImage_SetTagLength``      *Not implemented*
``FreeImage_SetTagValue``       *Not implemented*
``FreeImage_FindFirstMetadata`` :func:`pyfreeimage.image.Image.tags`
``FreeImage_FindNextMetadata``  :func:`pyfreeimage.image.Image.tags`
``FreeImage_FindCloseMetadata`` :func:`pyfreeimage.image.Image.tags`
``FreeImage_GetMetadata``       :func:`pyfreeimage.image.Image.tag`
``FreeImage_SetMetadata``       *Not implemented*
``FreeImage_GetMetadataCount``  *Not implemented*
``FreeImage_CloneMetadata``     *Not implemented*
``FreeImage_TagToString``       :func:`pyfreeimage.metadata.Tag.value`
=============================== ===========================================


Toolkit functions
-----------------
