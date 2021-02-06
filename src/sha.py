import os

def sha_encrypt(input_file, output_location="", mode="sha256"):
    """
        Takes an input file hashes its value

        Args:
        ----
        input_file (File Location/String): 
            The file name of input file to be hashed.\n
        output_location (File Location/String): 
            The location and the name of the file to be save. Is optional\n
        mode (String, optional): 
            What hashing  method will be used. Defaults to "sha256".
    """

    os.system(f"openssl dgst -{mode} {input_file} {f'> {output_location}' if output_location else ''}")