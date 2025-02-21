import ctypes
import os

def get_dll_path():
    return os.path.join(os.path.dirname(__file__), "crypter.dll")

def encrypt(key, val):
    with open("tmp.txt", "w") as file:
        file.write(f"{key}\n{val}\n")
    
    dll = ctypes.CDLL(get_dll_path())
    dll.encrypt()
    
    with open("tmp.txt", "r") as file:
        file.readline()  # Skip key
        encrypted_text = file.readline().strip()
    
    os.remove("tmp.txt")
    return encrypted_text

def decrypt(key, val):
    with open("tmp.txt", "w") as file:
        file.write(f"{key}\n{val}\n")
    
    dll = ctypes.CDLL(get_dll_path())
    dll.decrypt()
    
    with open("tmp.txt", "r") as file:
        file.readline()  # Skip key
        decrypted_text = file.readline().strip()
    
    os.remove("tmp.txt")
    return decrypted_text


# test case example
def test_vigenere():
    key = "tHE KEY IS SECRET"
    original_text = "The_moDULe IS W0RK1NG FI&3"
    
    encrypted_text = encrypt(key, original_text)
    print(f"Encrypted: {encrypted_text}")
    
    decrypted_text = decrypt(key, encrypted_text)
    print(f"Decrypted: {decrypted_text}")
    
    assert decrypted_text == original_text, "Decryption failed!"

if __name__ == "__main__":
    test_vigenere()