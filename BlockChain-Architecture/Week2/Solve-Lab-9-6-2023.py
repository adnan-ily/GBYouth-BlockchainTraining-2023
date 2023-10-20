from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization



#Generate a private key

def generateECDSAKeyPair():
    private_key = ec.generate_private_key(
        ec.SECP256K1(),
        default_backend()
    )
    public_key = private_key.public_key()
    return private_key, public_key

#Function ECDSASign(privateKey, message)
def ECDSASign(private_key, message):
    signature = private_key.sign(
        message.encode(),
        ec.ECDSA(hashes.SHA256())
    )
    return signature


def ECDSAVerify(public_key, message, signature):
    try:
        public_key.verify(
            signature,
            message.encode(),
            ec.ECDSA(hashes.SHA256())
        )
        return True
    except InvalidSignature:
        return False


def main():
    # ECDSA
    ECDSAPrivateKey, ECDSAPublicKey = generateECDSAKeyPair()
    message = "Message for ECDSA algorithm"
    signature = ECDSASign(ECDSAPrivateKey, message)
    verified = ECDSAVerify(ECDSAPublicKey, message, signature)

    print("ECDSA:")
    print("ECDSA Public Key:", ECDSAPublicKey.public_bytes(Encoding.PEM, PublicFormat.SubjectPublicKeyInfo).decode())
    print("ECDSA Private Key:", ECDSAPrivateKey.private_bytes(encoding=serialization.Encoding.PEM, format=serialization.PrivateFormat.PKCS8, encryption_algorithm=serialization.NoEncryption()).decode())

    print("Message:", message)
    print("Signature:", signature)
    print("Verification:", verified)


if __name__ == "__main__":
    main()

