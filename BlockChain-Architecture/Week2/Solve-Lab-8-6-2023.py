import hashlib
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import rsa, dsa
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric.padding import PKCS1v15

def generate_rsa_keys():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    public_key = private_key.public_key()
    return private_key, public_key

def generate_dsa_keys():
    private_key = dsa.generate_private_key(
        key_size=2048
    )
    public_key = private_key.public_key()
    return private_key, public_key
    
message = "HI, adnan ali you are greeat"

def encrypt_rsa(message, public_key):
    encrypted_message = public_key.encrypt(
        message.encode('utf-8'),
        padding.PKCS1v15(
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return encrypted_message


def decrypt_rsa(encrypted_message, private_key):
    decrypted_message = private_key.decrypt(
        encrypted_message,
        padding.PKCS1v15(
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return decrypted_message.decode('utf-8')


def sign_dsa(message, private_key):
    signature = private_key.sign(
        message.encode('utf-8'),
        hashes.SHA256()
    )
    return signature


def verify_dsa(message, signature, public_key):
    try:
        public_key.verify(
            signature,
            message.encode('utf-8'),
            hashes.SHA256()
        )
        return True
    except InvalidSignature:
        return False

rsa_private_key, rsa_public_key = generate_rsa_keys()

encrypted_message = encrypt_rsa(message, rsa_public_key)
decrypted_message = decrypt_rsa(encrypted_message, rsa_private_key)

print(f"Original message: {message}")
print(f"Decrypted message: {decrypted_message}")

dsa_private_key, dsa_public_key = generate_dsa_keys()

signature = sign_dsa(message, dsa_private_key)
verification_result = verify_dsa(message, signature, dsa_public_key)

print(f"Signature verification result: {verification_result}")