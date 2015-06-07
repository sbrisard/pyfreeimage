from pyfreeimage._c_api import cfi
from pyfreeimage.image import Image


def file_format(filename, size=0):
    """Return the format (as a ``FIF_*`` constant) of the file.

    Args:
        filename (str): Name of the file where the image is stored.
        size (int): unused.
    Returns:
        The format as an int.
    """
    return cfi.FreeImage_GetFileType(filename, size)


def load(filename, fif=None, flags=0):
    """Read an image from a file.

    Args:
        filename (str): Name of the file from which the image is read.
        fif (int): File format; one of the ``FIF_*`` constants.
        flags (int): or combination of the I/O flags.
    """
    if isinstance(filename, str):
        filename = filename.encode()
    if fif is None:
        fif = file_format(filename, 0)
    dib = cfi.FreeImage_Load(fif, filename, flags)
    if dib is None:
        # TODO Define new exception
        raise RuntimeError(filename)
    return Image(dib)


def save(filename, image, fif, flags=0):
    """Save the image to a file.

    Args:
        filename (str): Name of the file to which the image is saved.
        image (:class:`pyfreeimage.image.Image`): Image to be saved.
        fif (int): File format; one of the ``FIF_*`` constants.
        flags (int): or combination of the I/O flags.

    """
    if isinstance(filename, str):
        filename = filename.encode()
    cfi.FreeImage_Save(fif, image._dib, filename, flags)
