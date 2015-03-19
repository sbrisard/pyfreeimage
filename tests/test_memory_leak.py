import pyfreeimage as fi


def test():
    from pyfreeimage._c_api import libfi

    allocated = set()
    # Decorate FreeImage_Unload
    old_unload = libfi.FreeImage_Unload
    def new_unload(dib):
        assert dib in allocated
        allocated.remove(dib)
        old_unload(dib)
    libfi.FreeImage_Unload = new_unload

    # Decorate Bitmap.__init__
    old_init = fi.Bitmap.__init__
    def new_init(self, dib):
        assert dib not in allocated
        allocated.add(dib)
        old_init(self, dib)
    fi.Bitmap.__init__ = new_init

    for i in range(100):
        with fi.empty(640, 480, 8) as a:
            pass

    assert len(allocated) == 0

    # Restore undecorated functions
    libfi.FreeImage_Unload = old_unload
    fi.Bitmap.__init__ = old_init
