from ctypes import *
from ctypes.util import find_library

libc = cdll.LoadLibrary(find_library("c"))

# None -> NULL
print(libc.time(None))

# Bytes -> const char *
libc.printf(b"Hello world\n")

# int -> long/int/short
libc.srand(10)

