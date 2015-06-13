import gc

import pyfreeimage as pyfi


def test():
    allocated = set()
    # Decorate FreeImage_Unload
    old_unload = pyfi.cfi.FreeImage_Unload
    def new_unload(dib):
        assert dib in allocated
        allocated.remove(dib)
        old_unload(dib)
    pyfi.cfi.FreeImage_Unload = new_unload

    # Decorate Image.__init__
    old_init = pyfi.Image.__init__
    def new_init(self, dib):
        assert dib not in allocated
        allocated.add(dib)
        old_init(self, dib)
    pyfi.Image.__init__ = new_init

    for i in range(100):
        a = pyfi.empty(640, 480, 8)
    del(a)

    assert len(allocated) == 0

    # Restore undecorated functions
    pyfi.cfi.FreeImage_Unload = old_unload
    pyfi.Image.__init__ = old_init
