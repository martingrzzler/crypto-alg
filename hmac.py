import pyDes
import hashlib


shared_key = "0secret0".encode()
k = pyDes.des(shared_key, pyDes.ECB, None, pad=None, padmode=pyDes.PAD_PKCS5 )

alice_message = "I want only you Bob".encode()

mac = hashlib.sha256()
mac.update(shared_key)
mac.update(alice_message)
mac = mac.digest()

cipher = k.encrypt(alice_message + '.'.encode() + mac)

print(alice_message, mac)

print('Bob decrypting')
message = k.decrypt(cipher, pad=None, padmode=pyDes.PAD_PKCS5)
[msg, mac] = str(message).split('.')

print(f"Bob decrypted message: {msg}, hmac: {mac}")
# check mac
b = hashlib.sha256()
b.update(shared_key)
b.update(msg.encode())
to_check = b.digest()
print(mac)
print("Are the mac equal?")



# Bob decrypting
