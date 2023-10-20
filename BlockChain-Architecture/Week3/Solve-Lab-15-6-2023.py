import hashlib
import base58
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.backends import default_backend


def generate_keys():
    private_key = ec.generate_private_key(ec.SECP256K1(), default_backend())
    public_key = private_key.public_key()
    return private_key, public_key


def generate_wallet_address(public_key):
    public_key_bytes = public_key.public_bytes(
        encoding=serialization.Encoding.X962,
        format=serialization.PublicFormat.UncompressedPoint
    )
    hashed_public_key = hash160(public_key_bytes)
    wallet_address = encode_base58_checksum(b'\x00' + hashed_public_key)
    return wallet_address


def hash160(b):
    import hashlib
    h1 = hashlib.new('ripemd160')
    h1.update(hashlib.sha256(b).digest())
    return h1.digest()


def encode_base58_checksum(b):
    checksum = hashlib.sha256(hashlib.sha256(b).digest()).digest()[:4]
    return base58.b58encode(b + checksum)


private_key, public_key = generate_keys()
wallet_address = generate_wallet_address(public_key)

print("Private Key:", private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
).decode())

print("Public Key:", public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
).decode())

print("Bitcoin Wallet Address:", wallet_address.decode())