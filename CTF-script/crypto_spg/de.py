from hashlib import sha256
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from base64 import b64decode
import string, random

ALPHABET = string.ascii_letters + string.digits + '~!@#$%^&*'
output_file = 'output.txt'

def generate_password(master_key):
    password = ''

    while master_key:
        bit = master_key & 1
        if bit:
            password += random.choice(ALPHABET[:len(ALPHABET)//2])
        else:
            password += random.choice(ALPHABET[len(ALPHABET)//2:])
        master_key >>= 1

    return password

def decrypt_flag(encrypted_flag, encryption_key):
    cipher = AES.new(encryption_key, AES.MODE_ECB)
    decrypted_flag = unpad(cipher.decrypt(encrypted_flag), 16)
    return decrypted_flag

def main():
    with open(output_file, 'r') as f:
        lines = f.readlines()

    password_line, encrypted_flag_line = lines[0].strip(), lines[1].strip()
    password = password_line.split(": ")[1]
    encrypted_flag = b64decode(encrypted_flag_line.split(": ")[1])

    master_key = 0
    for i, char in enumerate(password):
        if char in ALPHABET[:len(ALPHABET)//2]:
            master_key |= (1 << i)

    encryption_key = sha256(master_key.to_bytes((master_key.bit_length() + 7) // 8, byteorder='little')).digest()
    decrypted_flag = decrypt_flag(encrypted_flag, encryption_key)

    print(f'Decrypted Flag: {decrypted_flag.decode()}')

if __name__ == '__main__':
    main()
