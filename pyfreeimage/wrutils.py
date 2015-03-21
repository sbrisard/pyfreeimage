'''
A simple replacement for the `weakref.finalize` object, new in Python 3.4.

Largely inspired from Benjamin Peterson's `Calling (C-level) finalizers without __del__ (Python recipe) <http://code.activestate.com/recipes/577242-calling-c-level-finalizers-without-__del__/>`_.

'''
import sys
import traceback
import weakref

_weakrefs = {}

class Callback:
    def __init__(self, func, *args, **kwargs):
        self.func = func
        self.args = args
        self.kwargs = kwargs

    def __call__(self, wr):
        try:
            self.func(*self.args, **self.kwargs)
        except Exception:
            print('Exception while calling {}'.format(self.func),
                  file=sys.stderr)
            traceback.print_exc()
        del _weakrefs[id(wr)]


def finalize(obj, func, *args, **kwargs):
    wr = weakref.ref(obj, Callback(func, *args, **kwargs))
    _weakrefs[id(wr)] = wr
