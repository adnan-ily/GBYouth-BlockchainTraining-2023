import random
import hashlib
import ecdsa
from ecdsa import SigningKey, SECP256k1
from hashlib import sha256

def generateTxid():
    return hashlib.sha256(str(random.randint(1, 1000000)).encode()).hexdigest()

def generateInput():
    prevTxid = generateTxid()
    prevOutputIndex = random.randint(0, 5)
    return prevTxid, prevOutputIndex

def generateOutput():
    recipientAddress = 'recipient_address_' + str(random.randint(1, 100))
    amount = round(random.uniform(0.001, 1.0), 8)
    return recipientAddress, amount

def generateTransactionFee():
    return round(random.uniform(0.0001, 0.001), 8)

def generateRandomTransaction():
    txid, inputPrevTxid, inputPrevOutputIndex = generateTxid(), *generateInput()
    outputRecipientAddress, outputAmount = generateOutput()
    transactionFee = generateTransactionFee()
    return txid, inputPrevTxid, inputPrevOutputIndex, outputRecipientAddress, outputAmount, transactionFee

def concatenateString(txid, inputPrevTxid, inputPrevOutputIndex, outputRecipientAddress, outputAmount, transactionFee):
    transactionData = str(txid) + str(inputPrevTxid) + str(inputPrevOutputIndex) + str(outputRecipientAddress) + str(outputAmount) + str(transactionFee)
    return transactionData

def generateECDSAKeyPair():
    ECDSAPrivateKey = SigningKey.generate(curve=SECP256k1)
    ECDSAPublicKey = ECDSAPrivateKey.get_verifying_key()
    return ECDSAPrivateKey, ECDSAPublicKey

def ECDSASign(privateKey, message):
    signature = privateKey.sign(message)
    return signature

def ECDSAVerify(publicKey, message, signature):
    try:
        publicKey.verify(signature, message)
        return True
    except:
        return False

def main():
    txid, inputPrevTxid, inputPrevOutputIndex, outputRecipientAddress, outputAmount, transactionFee = generateRandomTransaction()
    transactionDataAsMessage = concatenateString(txid, inputPrevTxid, inputPrevOutputIndex, outputRecipientAddress, outputAmount, transactionFee).encode()
    transactionDataAsMessageSHA256Hashed = hashlib.sha256(transactionDataAsMessage).hexdigest()
    ECDSAPrivateKey, ECDSAPublicKey = generateECDSAKeyPair()
    signature = ECDSASign(ECDSAPrivateKey, transactionDataAsMessageSHA256Hashed)
    verified = ECDSAVerify(ECDSAPublicKey, transactionDataAsMessageSHA256Hashed, signature)
    print("ECDSA:")
    print("ECDSA Public Key:", ECDSAPublicKey.to_string().hex())
    print("ECDSA Private Key:", ECDSAPrivateKey.to_string().hex())
    print("transactionDataAsMessageSHA256Hashed:", transactionDataAsMessageSHA256Hashed)
    print("Signature:", signature.hex())
    print("Verification:", verified)

main()
