"""This module defines geometric transformations of images."""


from pyfreeimage._c_api import cfi
from pyfreeimage.constants import FILTER_BSPLINE
from pyfreeimage.image import Image

def rescale(img, width, height, method=FILTER_BSPLINE):
    """Return a new image resized according to the specified dimensions.

    Args:
        img (Image): The image to rescale.
        width (int): The new width.
        height (int): The new height.
        method (int): The interpolation method; one of the ``FILTER_*``
            constants (defaults to ``FILTER_BSPLINE``).
    Returns:
        Image: The resized image as a new instance.

    """
    p = cfi.FreeImage_Rescale(img._dib, width, height, method)
    return Image(p)
