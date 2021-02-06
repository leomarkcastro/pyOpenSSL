import os

def ecdsa_createKey(private_loc, public_key, newprivate=True, modeName="secp384r1"):
    #type -> openssl ecparam -list_­cur­ves -> on console to get the list of available modeName
    if newprivate: os.system(f'openssl ecparam -genkey -name {modeName} -noout -out {private_loc}')
    os.system(f'openssl ec -in {private_loc} -pubout -out {public_key}')

def ecdsa_certify(input_file, private_key, output_certificate=""):
    os.system(f'openssl dgst -sha256 -sign {private_key} < {input_file} {f"> {output_certificate}" if output_certificate else ""}')

def ecdsa_verify(input_file, public_key, check_certificate):
    os.system(f'openssl dgst -sha256 -verify {public_key} -signature {check_certificate} < {input_file}')

    