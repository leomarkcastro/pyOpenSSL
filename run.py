from src.aes import aes_encrypt, aes_decrypt
from src.sha import sha_encrypt
from src.rsa import rsa_createKey, rsa_key_encrypt, rsa_key_decrypt
from src.ecdsa import ecdsa_createKey, ecdsa_certify, ecdsa_verify

import pyfiglet
import secrets


#os.system(f"openssl help")
#os.system(f"openssl help enc")

# Global Variables
mainImage = "output/lena512color.tiff"

def title():
    # Prompt Section
    out = pyfiglet.figlet_format("Encryption OpenSSL", font="slant")
    print(out)
    [print(f'[{i}] {line}') for i, line in enumerate(["AES", "SHA", "RSA", "ECDSA"])]
    input_mode = input("Select what type of encryption to Test: ")
    input_mode = input_mode.strip()
        
    print(f'\n\n{"-"*100}\n\n')

    return input_mode

input_mode = title()

if input_mode == "0":
    # A symmetric encryption because both encryption and decryption uses the same keys
    # Useful if you want to encrypt a file

    input_mode = input("AES Mode [aes-128-ecb/aes-128-cbc]: ").strip().lower()

    encrypted = f"{mainImage.split('.')[0]}_{input_mode}.{mainImage.split('.')[1]}"
    decrypted = f"{mainImage.split('.')[0]}_{input_mode}_decrypt.{mainImage.split('.')[1]}"

    key = secrets.token_hex(16)

    iv = ""
    if 'cbc' in input_mode:
        iv = secrets.token_hex(16)
    
    aes_encrypt(mainImage, encrypted, key, iv, input_mode)
    aes_decrypt(encrypted, decrypted, key, iv, input_mode)

elif input_mode == "1":
    # Hashing is a one way encryption, meaning once you hashed it, you cannot reverse it to return to its pre-image
    # Useful if you want to have a file into a specific hex length

    input_mode = input("SHA Mode [sha1/sha256/sha512]: ").strip()

    input_mode2 = input("Save File? (y/n): ").strip()

    sha_encrypt(mainImage, f"output/{input_mode}" if 'y' in input_mode2 else '' ,mode=input_mode)

elif input_mode == "2":
    # An assymetric encryption where encryption and decryption uses two different keys
    # Useful if you want to have a central private key where anyone with a public key can send an encrypted message to you and only you can decrypt it

    public_rsakey = "keys/public_rsa.pem"
    private_rsakey = "keys/private_rsa.pem"

    encrypted = f"{mainImage.split('.')[0]}_rsa.{mainImage.split('.')[1]}"
    decrypted = f"{mainImage.split('.')[0]}_rsa_decrypt.{mainImage.split('.')[1]}"

    input_mode = input("Encrypt key (y/n): ").strip()
    
    rsa_createKey(private_rsakey, public_rsakey, newprivate=True ,encrypted=True if 'y' in input_mode else False)
    ret = rsa_key_encrypt(mainImage, encrypted, public_rsakey) # <-- this returns an encrypted file location and the method of encryption

    rsa_key_decrypt(encrypted, decrypted, private_rsakey, ret)

elif input_mode == "3":
    # An assymetric encryption where encryption and decryption uses two different keys
    # Useful as a distributor checker (owner of the private key), files can be sent here, the host will create certification files and everyone with the public key can verify if the file received is a certified copy by verifying it

    public_eckey = "keys/public_ec.pem"
    private_eckey = "keys/private_ec.pem"
    signature = "keys/signature.bin"

    ecdsa_createKey(private_eckey, public_eckey, newprivate=True)
    ecdsa_certify(mainImage, private_eckey, signature)
    ecdsa_verify(mainImage, public_eckey, signature)


print(f'\n\n\n\n\nDone Doing the Encryption')
