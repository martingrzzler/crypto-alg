
import random


def gen_key(n):
    return bytes([random.randrange(0, 255) for i in range(n)])


def encrypt(key, message):
    length = min(len(key), len(message))
    return bytes([key[i] ^ message[i] for i in range(length)])


message = "XOR IS UNBREAKABLE".encode()
key = gen_key(len(message))

cipher = encrypt(key, message)
message = encrypt(key, cipher)

print(cipher)
print(message)
