import random


def gen_key():
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
    urne = list(letters)
    key_map = {}

    for c in letters:
        key_map[c] = urne.pop(random.randint(0, len(urne) - 1))

    return key_map


def encrypt(key, message):
    cipher = ""
    for c in message:
        if c in key:
            cipher += key[c]
        else:
            cipher += c
    return cipher


def decrypt(key, cipher):
    dkey = {}
    for a, b in key.items():
        dkey[b] = a

    return encrypt(dkey, cipher)


key = gen_key()
cipher = encrypt(key, "CEASAR IS DEAD")
print(f"Cipher: {cipher}")
message = decrypt(key, cipher)
print(f"Message: {message}")
