from Crypto.Cipher import AES
import time
import sys
import base64
import uuid

def generate_password(password):
    try:
        encryptor = AES.new(password, AES.MODE_CBC, b'0000000000000000')
        ciphertext = encryptor.encrypt("%016d" % (int(time.time()), ))
        return ciphertext.encode('hex')
    except Exception as e:
        print e
        return None

if __name__ == "__main__":
    print generate_password(sys.argv[1])
