import ctypes

from ctypes import cast, c_byte, c_char_p, c_void_p
from weakref import finalize

from pyfreeimage._c_api import cfi as cfi
from pyfreeimage.constants import *

type_map = {FIDT_BYTE: ctypes.c_uint8,
            FIDT_ASCII: ctypes.c_char,
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
    """Class that represents one tag of an image.

    The constructor of this class should not be called directly.

    Args:
        ptag (int): Pointer to the underlying FreeImage structure.
        mdmodel (int): metadata model to which the tag belongs; one of
                       the ``FIMD_*`` constants.
    """

    def __init__(self, ptag, mdmodel=None):
        self._c_tag = ptag
        self.mdmodel = mdmodel
        #finalize(self, cfi.FreeImage_DeleteTag, self._c_tag)

    def copy(self):
        """Return a deep copy of the tag."""
        return Tag(cfi.FreeImage_CloneTag(self._c_tag), self.mdmodel)

    @property
    def key(self):
        """The tag field name."""
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
        """The data type; one of the ``FIDT_*`` constants."""
        return cfi.FreeImage_GetTagType(self._c_tag)

    @property
    def count(self):
        """The number of values of type :func:`Tag.type`."""
        return cfi.FreeImage_GetTagCount(self._c_tag)

    @property
    def value(self):
        """Return a ``ctypes`` array of values.

        The length of the returned array depends on the tag type

          - ``FIDT_ASCII``: the length is the tag count minus one (as the
            string is NULL terminated),
          - ``FIDT_RATIONAL``, ``FIDT_SRATIONAL``: the length is
            twice the tag count,
          - ``FIDT_PALETTE``: the length is four times the tag count,
          - in all other cases, the length is equal to the tag count.

        If the tag type is ``FIDT_ASCII``, the following code will return
        the corresponding bytes string::

            bytes(tag.value)

        See also:
            :func:`Tag.type`, :func:`Tag.count`.
        """
        tag_type = self.type
        length = self.count
        if (tag_type == FIDT_ASCII):
            length -= 1
        elif (tag_type == FIDT_RATIONAL) or (tag_type == FIDT_SRATIONAL):
            length *= 2
        elif (tag_type == FIDT_PALETTE):
            length *= 4
        return_type = type_map[tag_type]*length
        return return_type.from_address(cfi.FreeImage_GetTagValue(self._c_tag))

    def __str__(self):
        if self.mdmodel is not None:
            return cfi.FreeImage_TagToString(self.mdmodel,
                                             self._c_tag, None).decode()
        elif self.type == FIDT_ASCII:
            return bytes(self.value).decode()
        else:
            return str(list(self.value))

    def __repr__(self):
        return 'Tag({}, {})'.format(self._c_tag, self.mdmodel)
