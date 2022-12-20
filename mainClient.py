import ClientServerClass
import RSAUtils
import time

private, public = RSAUtils.createKeys()

client = ClientServerClass.Client(22222, "127.0.0.1")
client.connect()
print("client connecté !")
print("Reception de la clé...")
publicServer = client.receiveAll()
print("DEBUG!!!!!!!!!!!!!")
publicServer = RSAUtils.publicBytesToPublicKey(publicServer)
print("Clé du server reçue")
time.sleep(1)
print("envoie clé client")
client.send(RSAUtils.publicKeyToPublicBytes(public))

mess = client.receiveAll()
print(RSAUtils.decrypt(mess, private))