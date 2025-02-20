import ctypes
import os
import sys

# Select DLL or SO based on OS
if sys.platform.startswith("win"):
    lib_name = "crypter.dll"
else:
    lib_name = "crypter.so"

dll_path = os.path.abspath(f"D:\Projects\PyBase\pybase_cpp\{lib_name}")
crypter = ctypes.CDLL(dll_path, mode=ctypes.RTLD_GLOBAL)


# Define function signatures (same as before)
crypter.encrypt_text.argtypes = [ctypes.c_char_p]
crypter.encrypt_text.restype = ctypes.c_char_p

crypter.decrypt_text.argtypes = [ctypes.c_char_p]
crypter.decrypt_text.restype = ctypes.c_char_p

crypter.free_memory.argtypes = [ctypes.c_char_p]
crypter.free_memory.restype = None
