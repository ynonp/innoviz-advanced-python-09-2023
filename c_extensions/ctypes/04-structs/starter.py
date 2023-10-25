"""
This demo creates our very own Timeval struct to match C's

struct timeval {
    time_t tv_sec;       /* access time */
    long tv_usec ;      /* modification time */
};

"""

from ctypes import *
from ctypes.util import find_library
import os
libc = CDLL(find_library("c"))

class Timeval(Structure):
    _fields_ = [
            ("tv_sec", c_long),
            ("tv_usec", c_long),
            ]


times = Timeval()
libc.gettimeofday.restype = int
libc.gettimeofday.argtypes = [POINTER(Timeval), c_void_p]
libc.gettimeofday(pointer(times), None)

print(f"tv_sec = {times.tv_sec}; tv_usec = {times.tv_usec}")
