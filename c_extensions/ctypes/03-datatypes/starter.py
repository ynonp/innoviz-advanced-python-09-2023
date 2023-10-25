from ctypes import *
from ctypes.util import find_library

libc = cdll.LoadLibrary(find_library('c'))
libm = cdll.LoadLibrary(find_library('m'))

# Fail - pow wants doubles
print(libm.pow(2, 3))

# Works - use c_double, returns c_double
libm.pow.restype = c_double
libm.pow.argtypes = [c_double, c_double]
print(libm.pow(c_double(2), c_double(3)))

x = c_int(7)
x.value = 13
print(x.value)

