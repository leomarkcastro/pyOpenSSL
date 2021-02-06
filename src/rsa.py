import os

def rsa_createKey_mime(private_loc, public_loc):
    """
        Is this even the proper way to do this.This creates a new public and private key pair with a few questions on prompt

        Args:
        -----
            private_loc (File Location / String): 
                File Location and Name where to save Private Key.
            public_loc (File Location / String): 
                File Location and Name where to save the Private Key.
        
        What happens here:
        ------------------
            This i think creates a new key with rsa-2048 algorithm that then produces a private and public key
            Public key is used to encrypt any message that will be sent to the private key holder 
    """

    os.system(f'openssl req -x509 -nodes -newkey rsa:2048 -keyout {private_loc} -out {public_loc}')

def rsa_encrypt_mime(input_file, output_loc, public_key):
    """
        This encrypts an input file with aes-256-cbc algorithm wrapped around a public key < supposed to be encrypted by an RSA key.

        Args:
            input_file (str): 
                Location of the file
            output_loc (str): 
                Location of the output file
            public_key (str): 
                Location of the public key
    """

    os.system(f"openssl smime -encrypt -binary -in {input_file} -out {output_loc} -outform DER {public_key}")

def rsa_decrypt_mime(input_file, output_loc, private_key):
    """
        This decrypts an input file wrapped in a mime 

        Args:
            input_file (str): 
                Location of the file
            output_loc (str): 
                Location of the output file
            public_key (str): 
                Location of the public key
    """

    os.system(f"openssl smime -decrypt -in {input_file} -binary -inform DEM -inkey {private_key} -out {output_loc}")



def rsa_createKey(private_loc, public_loc, newprivate=True, encrypted=True):
    """Creates a public private key using rsa-2048 alrorithm

    Args:
        private_loc (str): Location where to save the private key (receiver)
        public_loc (str): Location where to save the public key (sender)
        encrypted (bool, optional): Use encryption using aes256. Defaults to False.
    """
    if newprivate : os.system(f"openssl genrsa {'-aes256' if encrypted else ''} -out {private_loc} 2048")
    os.system(f"openssl rsa -in {private_loc} -pubout -out {public_loc}")

def rsa_key_encrypt(input_file, output_loc, public_key, key="", encrypt_method="-aes-256-cbc"):
    if not key:
        key = "keys/_runtimekey"
        os.system(f"openssl rand -hex 32 > {key}")

    return_value = f"{key}_enc"
    
    os.system(f'openssl enc -p {encrypt_method} -salt -in {input_file} -out {output_loc} -pass file:./{key}')
    os.system(f'openssl rsautl -encrypt -inkey {public_key} -pubin -in {key} -out {return_value}')
    
    """
        enc: Encoding with Ciphers
        -p: Print the key, initialization vector and salt value (if used)
        -aes-256-cbc: AES Encryption with a 256 bit key and CBC mode
        -in: Input file name
        -salt: Add a salt to password
        -out: Output file name
        -pass: Password source. Possible values for arg are pass:password or file:filename, where password is your password and filename is file containing the password.
    """ 

    # Returns an rsa encrypted code and what file encrypting method was covered by the rsa algorithm
    return [return_value, encrypt_method]

def rsa_key_decrypt(input_file, output_loc, private_key, encrypted_data):

    decrypted_key = f"{encrypted_data[0]}_dec"

    os.system(f'openssl rsautl -decrypt -inkey {private_key} -in {encrypted_data[0]} -out {decrypted_key}')
    os.system(f'openssl enc -d -p {encrypted_data[1]} -salt -in {input_file} -out {output_loc} -pass file:{decrypted_key}')


if __name__ == "__main__":
    os.system("openssl genrsa -out key.pem 4096")

    os.system("openssl rsa -in key.pem -pubout -out pub.pem")

    os.system("echo test test test > file.txt ")

    os.system("openssl rsautl -encrypt -inkey pub.pem -pubin -in file.txt -out file.bin")

    os.system("openssl rsautl -decrypt -inkey key.pem -in file.bin")