import sys
from cryptography.fernet import Fernet as explore
import base64

def generate_key(size):
    key = os.urandom(size)
    key = base64.urlsafe_b64encode(key)
    return key.decode()

def encrypt(message, key):
    message = message.encode()
    key = key.encode()
    key = base64.urlsafe_b64decode(key)
    encrypted = []
    for i, byte in enumerate(message):
        encrypted_byte = byte ^ key[i % len(key)]
        encrypted.append(encrypted_byte)
    encrypted = bytes(encrypted)
    encrypted = base64.urlsafe_b64encode(encrypted)
    return encrypted.decode()

def decrypt(encrypted, key):
    encrypted = encrypted.encode()
    key = key.encode()
    encrypted = base64.urlsafe_b64decode(encrypted)
    key = base64.urlsafe_b64decode(key)
    decrypted = []
    for i, byte in enumerate(encrypted):
        decrypted_byte = byte ^ key[i % len(key)]
        decrypted.append(decrypted_byte)
    decrypted = bytes(decrypted)
    decrypted = decrypted.decode()
    return decrypted

def test_encryption_function(message):
    reversed_message = message[::-1]
    encrypted_message = reversed_message + "_notsecure"
    return encrypted_message

def encryption(msg):
    temp_enc_msg = base64.b64encode(msg)
    enc_msg = f.encrypt(temp_enc_msg)
    return enc_msg
    
def post_encryption(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            encrypted_text += shifted_char
        else:
            encrypted_text += char
    return encrypted_text


flag = sys.argv[1]
key = "this_will_be_replaced_later"
f = explore(key)
encrypted_flag = encryption(flag)
print(encrypted_message)
