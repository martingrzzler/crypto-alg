from email import message
from pyDes import *

message = "0123456701234567"
key = "DESCRYPT"
iv = bytes([0]*8)
k = des(key, ECB, iv, pad=None, padmode=PAD_PKCS5)

cipher = k.encrypt(message)

# altering one block makes the whole block unreadable