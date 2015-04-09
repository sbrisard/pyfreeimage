from pyfreeimage._c_api import libfi
from pyfreeimage.bitmap import Bitmap


def get_file_format(filename, size=0):
    """Return the format (as a ``FIF_*`` constant) of the file.

    Args:
        filename (str): Name of the file where the image is stored.
        size (int): unused.
    Returns:
        The format as an int.
    """
    return libfi.FreeImage_GetFileType(filename, size)


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
        fif = get_file_format(filename, 0)
    dib=libfi.FreeImage_Load(fif, filename, flags)
    return Bitmap(dib)


def save(filename, image, fif, flags=0):
    """Save the image to a file.

    Args:
        filename (str): Name of the file to which the image is saved.
        image (:class:`pyfreeimage.bitmap.Bitmap`): Image to be saved.
        fif (int): File format; one of the ``FIF_*`` constants.
        flags (int): or combination of the I/O flags.

    """
    if isinstance(filename, str):
        filename = filename.encode()
    libfi.FreeImage_Save(fif.value, self._dib, filename, flags)
