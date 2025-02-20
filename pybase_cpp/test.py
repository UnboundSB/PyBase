import ctypes
import os

# Get the absolute path of test.dll

import ctypes

def load_encrypt_dll():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    dll_path = os.path.join(script_dir, "crypter.dll")
    # Load the DLL
    encrypt_lib = ctypes.CDLL(dll_path)

    # Set return type for functions
    encrypt_lib.encrypt.restype = ctypes.c_char_p
    encrypt_lib.decrypt.restype = ctypes.c_char_p

    return encrypt_lib

# Example Usage
if __name__ == "__main__":
    encrypt_lib = load_encrypt_dll()

    text = "HELLO"
    key = "KEY"

    encrypted = encrypt_lib.encrypt(text.encode(), key.encode()).decode()
    decrypted = encrypt_lib.decrypt(encrypted.encode(), key.encode()).decode()

    print("Encrypted:", encrypted)
    print("Decrypted:", decrypted)
