import hashlib

def hash_generation(passaword: str):
    byte_password = passaword.encode("utf-8")
    hash_password = hashlib.sha256(byte_password)

    return hash_password.hexdigest()