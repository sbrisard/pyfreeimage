import ctypes

from ctypes import cast, c_byte, c_char_p, c_void_p
from weakref import finalize

from pyfreeimage._c_api import cfi as cfi
from pyfreeimage.constants import *

type_map = {FIDT_BYTE: ctypes.c_uint8,
            FIDT_SHORT: ctypes.c_uint16,
            FIDT_LONG: ctypes.c_uint32,
            FIDT_RATIONAL: ctypes.c_uint32,
            FIDT_SBYTE: ctypes.c_int8,
            FIDT_UNDEFINED: ctypes.c_byte,
            FIDT_SSHORT: ctypes.c_int16,
            FIDT_SLONG: ctypes.c_int32,
            FIDT_SRATIONAL: ctypes.c_int32,
            FIDT_FLOAT: ctypes.c_float,
            FIDT_DOUBLE: ctypes.c_double,
            FIDT_IFD: ctypes.c_uint32,
            FIDT_PALETTE: ctypes.c_uint8,
            FIDT_LONG8: ctypes.c_uint64,
            FIDT_SLONG8: ctypes.c_int64,
            FIDT_IFD8: ctypes.c_uint64}

class Tag:
    """TODO"""

    def __init__(self, ptag=None):
        self._c_tag = ptag
        #finalize(self, cfi.FreeImage_DeleteTag, self._c_tag)

    def copy(self):
        """Return a deep copy of the tag."""
        return Tag(cfi.FreeImage_CloneTag(self._c_tag))

    @property
    def key(self):
        """The tag field name (unique inside a metadata model)."""
        return cfi.FreeImage_GetTagKey(self._c_tag)

    @property
    def description(self):
        """The tag description."""
        return cfi.FreeImage_GetTagDescription(self._c_tag)

    @property
    def id(self):
        """The tag ID."""
        return cfi.FreeImage_GetTagID(self._c_tag)

    @property
    def type(self):
        """The data type."""
        return cfi.FreeImage_GetTagType(self._c_tag)

    @property
    def length(self):
        """The length of the array returned by :func:`Tag.value`."""
        tag_type = cfi.FreeImage_GetTagType(self._c_tag)
        tag_count = cfi.FreeImage_GetTagCount(self._c_tag)
        if (tag_type == FIDT_RATIONAL) or (tag_type == FIDT_SRATIONAL):
            return 2*tag_count
        elif (tag_type == FIDT_PALETTE):
            return 4*tag_count
        else:
            return tag_count

    @property
    def value(self):
        """TODO"""
        tag_type = self.type
        tag_value = cfi.FreeImage_GetTagValue(self._c_tag)

        # If FIDT_ASCII, return a string
        if tag_type == FIDT_ASCII:
            return ctypes.cast(tag_value, c_char_p).value

        # Return a ctypes array in all other cases
        length = self.length
        return_type = type_map[tag_type]
        if length > 1:
            return_type = return_type*length
        return return_type.from_address(tag_value)
