# if eve knows the algorithm, she can get the correct key by brute force
# Crypto Rule 1 - Kerckhoff's Principle, Eve should not be able to break the cipher even if she knows the cipher
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def gen_key(n):
    key = {}
    count = 0
    for c in letters:
        key[c] = letters[(count + n) % len(letters)]
        count += 1

    return key


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


key = gen_key(3)
cipher = encrypt(key, "CEASAR IS DEAD")


print(cipher)
print(decrypt(key, cipher))

print("\nAttack:\n")
for i in range(len(letters)):
    key = gen_key(i + 1)
    message = encrypt(key, cipher)
    print(message)
