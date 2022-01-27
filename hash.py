import hashlib

m = "My secret password".encode()
sha256 = hashlib.sha256()
sha256.update(m)
hash = sha256.digest()

print(hash)
