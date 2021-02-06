import os
import secrets

def aes_encrypt(input_file, output_location, key, iv='', mode="aes-128-ebc"):
    """
        Takes an input file and encrypts it with your given mode

        Args:
        ----
        input_file (File Location/String): 
            The file name of input file to be encrypted.\n
        output_location (File Location/String): 
            The location and the name of the file to be saved\n
        key (String): 
            A random key that will be used to encrypt the said file\n
        mode (String, optional): 
            What encryption method will be used. Defaults to "aes-128-ebc".
    """
    os.system(f"openssl enc -{mode} -e -in {input_file} -out {output_location} -K {key} {f'-iv {iv}' if iv else ''}")


def aes_decrypt(input_file, output_location, key, iv='', mode="aes-128-ebc"):
    """
        Takes an input file and decrypts it with your given key in given mode mode

        Args:
        ----
        input_file (File Location/String): 
            The file name of input file to be decrypted.\n
        output_location (File Location/String): 
            The location and the name of the file to be saved\n
        key (String): 
            A random key that will be used to decrypt the said file\n
        mode (String, optional): 
            What encryption method will be used. Defaults to "aes-128-ebc".
    """

    os.system(f"openssl enc -{mode} -d -in {input_file} -out {output_location} -K {key} {f'-iv {iv}' if iv else ''}")