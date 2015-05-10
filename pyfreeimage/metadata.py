import ctypes

from ctypes import cast, c_byte, c_char_p, c_void_p
from weakref import finalize

from pyfreeimage._c_api import cfi as cfi
from pyfreeimage.constants import *

fidt = {FIDT_BYTE: ctypes.c_byte,
        FIDT_ASCII: ctypes.c_byte}

class Tag:
    def __init__(self, ptag=None):
        self._tag = ptag
        #finalize(self, cfi.FreeImage_DeleteTag, self._tag)

    def copy(self):
        """Return a deep copy of the tag."""
        return Tag(cfi.FreeImage_CloneTag(self._tag))

    @property
    def key(self):
        """The tag field name (unique inside a metadata model)."""
        return cfi.FreeImage_GetTagKey(self._tag)

    @property
    def description(self):
        """The tag description."""
        return cfi.FreeImage_GetTagDescription(self._tag)

    @property
    def id(self):
        """The tag ID."""
        return cfi.FreeImage_GetTagID(self._tag)

    @property
    def type(self):
        """The data type."""
        return cfi.FreeImage_GetTagType(self._tag)

    @property
    def count(self):
        return cfi.FreeImage_GetTagCount(self._tag)

    @property
    def length(self):
        return cfi.FreeImage_GetTagLength(self._tag)

    @property
    def value(self):
        type = self.type
        data = cfi.FreeImage_GetTagValue(self._tag)
        if type == FIDT_ASCII:
            #return cast(cfi.FreeImage_GetTagValue(self._tag), c_char_p).value
            array_type = c_byte * self.count
            return array_type.from_address(data)
