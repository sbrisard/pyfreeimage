import gc

import pyfreeimage as fi


def test():
    from pyfreeimage._c_api import cfi

    allocated = set()
    # Decorate FreeImage_Unload
    old_unload = cfi.FreeImage_Unload
    def new_unload(dib):
        assert dib in allocated
        allocated.remove(dib)
        old_unload(dib)
    cfi.FreeImage_Unload = new_unload

    # Decorate Image.__init__
    old_init = fi.Image.__init__
    def new_init(self, dib):
        assert dib not in allocated
        allocated.add(dib)
        old_init(self, dib)
    fi.Image.__init__ = new_init

    for i in range(100):
        a = fi.empty(640, 480, 8)
    del(a)

    assert len(allocated) == 0

    # Restore undecorated functions
    cfi.FreeImage_Unload = old_unload
    fi.Image.__init__ = old_init
