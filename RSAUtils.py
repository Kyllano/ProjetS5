from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.backends import default_backend
import base64

#Permet de cr
def createKeys() -> tuple[rsa.RSAPrivateKey, rsa.RSAPublicKey]:
    privateKey = rsa.generate_private_key(65537, 2048)
    return privateKey, privateKey.public_key()

def encrypt(message : bytes, publicKey : rsa.RSAPublicKey) -> bytes:
    if (not isinstance(message, bytes) or not isinstance(publicKey, rsa.RSAPublicKey)) :
        raise TypeError("Arguments invalide")
    encryptedMess = publicKey.encrypt(message, padding.OAEP(padding.MGF1(hashes.SHA256()), hashes.SHA256(), None))
    return encryptedMess

def decrypt(encryptedMessage : bytes, privateKey : rsa.RSAPrivateKey) -> str:
    if (not isinstance(encryptedMessage, bytes) or not isinstance(privateKey, rsa.RSAPrivateKey)) :
        raise TypeError("Arguments invalide")
    decryptedMess = privateKey.decrypt(encryptedMessage, padding.OAEP(padding.MGF1(hashes.SHA256()), hashes.SHA256(), None))
    return decryptedMess

def publicKeyToPublicBytes(publicKey : rsa.RSAPublicKey) -> bytes :
    if (not isinstance(publicKey, rsa.RSAPublicKey)) :
        raise TypeError("Arguments invalide")
    publicBytes = publicKey.public_bytes(serialization.Encoding.PEM, serialization.PublicFormat.SubjectPublicKeyInfo)
    return publicBytes

def publicBytesToPublicKey(publicBytes : bytes) -> rsa.RSAPublicKey :
    if (not isinstance(publicBytes, bytes)) :
        raise TypeError("Arguments invalide")
    keyData = '\n'.join(publicBytes.decode('utf-8').splitlines()[1:-1])
    derData = base64.b64decode(keyData)
    publicKey = serialization.load_der_public_key(derData, default_backend())
    return publicKey

def isdigit(num : str) :
    try:
        int(num)
        return True
    except ValueError:
        return False
