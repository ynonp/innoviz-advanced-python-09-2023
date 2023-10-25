from ctypes import *
from ctypes.util import find_library
import os

libc_location = find_library('c')
libc = CDLL(libc_location, use_errno=True)

libc.fopen.restype = c_void_p
fh = libc.fopen(b"foo", "w")
print(fh)

if fh is None:
    error_code = get_errno()
    print(f"Error: {error_code} - {os.strerror(error_code)}")
