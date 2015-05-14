import ctypes

from ctypes import cast, c_byte, c_char_p, c_void_p
from weakref import finalize

from pyfreeimage._c_api import cfi as cfi
from pyfreeimage.constants import *

fidt = {FIDT_BYTE: ctypes.c_ubyte,
        FIDT_SHORT: ctypes.c_ushort,
        FIDT_LONG: ctypes.c_ulong,
        FIDT_SBYTE: ctypes.c_byte,
        FIDT_UNDEFINED: ctypes.c_byte,
        FIDT_SSHORT: ctypes.c_short,
        FIDT_SLONG: ctypes.c_long,
        FIDT_FLOAT: ctypes.c_float,
        FIDT_DOUBLE: ctypes.c_double,
        FIDT_IFD: ctypes.c_ulong,
        FIDT_LONG8: ctypes.c_ulonglong,
        FIDT_SLONG8: ctypes.c_longlong,
        FIDT_IFD8: ctypes.c_ulonglong}

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
        tag_type = self.type
        tag_value = cfi.FreeImage_GetTagValue(self._tag)
        try:
            ArrayType = fidt[tag_type]
            return ArrayType.from_address(tag_value)
        except KeyError:
            if tag_type == FIDT_ASCII:
                return ctypes.cast(tag_value, c_char_p).value
            else:
                raise NotImplementedError('Cannot compute value of '
                                          'tag type {}'.format(tag_type))
