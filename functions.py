import numpy
import ctypes

_libfunctions = numpy.ctypeslib.load_library("libfunctions",'.')

_libfunctions.hello.argtypes = [ctypes.c_int]
_libfunctions.hello.restype = ctypes.c_void_p

def hello(n):
    return _libfunctions.hello(int(n))
