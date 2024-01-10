import sys
from cryptography.fernet import Fernet as explore
import base64

def encryption(msg, key):
    temp_enc_msg = base64.b64encode(msg.encode('utf-8'))
    func = Fernet(key)
    enc_msg = func.encrypt(temp_enc_msg)
    return enc_msg

print(encryption(sys.argv[1], sys.argv[2]))
