# if some individual bits get flipped it's not a problem because the rest of the message will
# be decrypted independantly
# but they are not authentic by default

class KeyStream:
    def __init__(self, key=1):
        self.initial = key
        self.next = key

    def rand(self):
        self.next = (1103515245 * self.next + 12345) % 2**31
        return self.next

    def get_key_byte(self):
        return self.rand() % 256

    def reset(self):
        self.next = self.initial


def encrypt(key: KeyStream, message: str):
    return bytes([message[i] ^ key.get_key_byte() for i in range(len(message))])


key = KeyStream()

message = "Stream Cipher don't require long keys".encode()
cipher = encrypt(key, message)
print(f"Cipher: {cipher}")
key.reset()
print(f"Message: {encrypt(key, cipher)}")

# -------- Authenticity fault -------------

# xor ing with zero doesn't change anything
# Bob can modify the message if he knows the original message and the cipher like this
# C = Cipher, K = Key, B = Bob's byte
# 1. Alice M xor K = C
# 2. Bob   M xor B = B'
# 3. Bob   C xor B' = B''
# 4. Alice B'' xor K = B


def alter(cipher: bytes):
    mod = [0] * len(cipher)
    mod[14] = ord(' ') ^ ord('1')
    mod[15] = ord(' ') ^ ord('0')
    mod[16] = ord('1') ^ ord('0')
    return bytes([mod[i] ^ cipher[i] for i in range(len(cipher))])


print("Alice and Bob vulnerablility")
alice_msg = "Send to Bob:    10$".encode()
print(f"Message Alice: {alice_msg}")
key.reset()
cipher = encrypt(key, alice_msg)
print(f"Cipher in transmission: {cipher}")
cipher = alter(cipher)
print(f"altered cipher:         {cipher}")
key.reset()
print(f"Decrypted Altered Message: {encrypt(key, cipher)}")
