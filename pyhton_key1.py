import os

KEY_FILE = "lock_key.txt"
INPUT_FILE = "plain.txt"
OUTPUT_FILE = "py1.txt"
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.backends import default_backend
import os

def read_key(path):
    with open(path, "rb") as f:
        key = f.read().strip()
    if not key:
        raise ValueError("Kalit bo'sh. Iltimos lock_key.txt ga kalit yozing.")
    return key

def xor_bytes(data: bytes, key: bytes) -> bytes:
    out = bytearray(len(data))
    klen = len(key)
    for i, b in enumerate(data):
        out[i] = b ^ key[i % klen]
    return bytes(out)

def main():
    # Agar kalit fayl bo'lmasa, yaratib qo'yamiz
    if not os.path.exists(KEY_FILE):
        with open(KEY_FILE, "wb") as f:
            f.write(b"mysecretkey123")  # kalit yoziladi
        print(f"{KEY_FILE} yaratildi.")

    if not os.path.exists(INPUT_FILE):
        print(f"{INPUT_FILE} (plaintext) topilmadi. plain.txt ga matn yozing.")
        return

    key = read_key(KEY_FILE)
    with open(INPUT_FILE, "rb") as f:
        plain = f.read()

    cipher = xor_bytes(plain, key)
    with open(OUTPUT_FILE, "wb") as f:
        f.write(cipher)

    print(f"Shifrlash bajarildi va natijani qayerdan topamiz. Natija: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
