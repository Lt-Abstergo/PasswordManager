# AES 256 encryption/decryption using CryptoDome library

import base64
import hashlib
import os
from Crypto import Random
from Crypto.Cipher import AES


#   Pads the input with spaces to form a 16bit block
def pad(s):
    block_size = 16
    remainder = len(s) % block_size
    padding_needed = block_size - remainder
    return s + padding_needed * ' '


#   Removes the unnecessary padding
def un_pad(s):
    return s.rstrip()


#   Generates a random Salt, IV
#   uses hashed private key to reduce intrusion
def encrypt(plain_text, password):
    salt = os.urandom(AES.block_size)
    iv = Random.new().read(AES.block_size)
    private_key = hashlib.scrypt(password.encode(), salt=salt, n=2 ** 14, r=8, p=1, dklen=32)
    padded_text = pad(plain_text)
    padded_text = padded_text.encode("utf8")
    cipher_config = AES.new(private_key, AES.MODE_CBC, iv)
    return {
        'c_t': base64.b64encode(cipher_config.encrypt(padded_text)),
        's': base64.b64encode(salt),
        'i': base64.b64encode(iv)
    }


def decrypt(enc_dict, password):
    salt = base64.b64decode(enc_dict['s'])
    enc = base64.b64decode(enc_dict['c_t'])
    iv = base64.b64decode(enc_dict['i'])
    private_key = hashlib.scrypt(password.encode(), salt=salt, n=2 ** 14, r=8, p=1, dklen=32)
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    decrypted = cipher.decrypt(enc)
    original = un_pad(decrypted)
    try:
        ret_val = original.decode()
        return ret_val
    except UnicodeDecodeError:
        return 0
