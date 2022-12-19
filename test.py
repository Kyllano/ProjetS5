import ClientServerClass
import string
import sys
import RSAUtils
import UserUtils
import annuaire
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding





users = []
users = UserUtils.importUsers("passwd.txt")

#UserUtils.addUser("root", "root", users)
#annuaire.removeRightsAnnuaires("root", "coucou")
ann = annuaire.importAnnuaire("root")
annuaire.addContact("root", "jean", "tamere", "mymail@mail", None, "01875269")
annuaire.addContact("root", "jean", "tamere", "mymail@mail", None, "01875269")
annuaire.addContact("root", "jean", "tamere", "mymail@mail", None, "01875269")




"""
private, public = RSAUtils.createKeys()


pubBytes = public.public_bytes(serialization.Encoding.PEM, serialization.PublicFormat.SubjectPublicKeyInfo)
pubKey = public
pubBytes = RSAUtils.publicKeyToPublicBytes(pubKey)
pubKey = RSAUtils.publicBytesToPublicKey(pubBytes)
"""



"""

mess = 'coucou!'
pubBytes = RSAUtils.publicKeyToPublicBytes(public)
public = RSAUtils.publicBytesToPublicKey(pubBytes)
encrypted = RSAUtils.encrypt(mess, public)
decrypted = RSAUtils.decrypt(encrypted, private)
print(decrypted)





UserUtils.removeUser("prout", users)

for i in users :
    if isinstance(i, UserUtils.User) :
        print(i.name, i.passwordHash, i.passwordSalt)

print(UserUtils.checkPasswordUser("root", UserUtils.findUser("root", users)))


UserUtils.changePassword("Gus", "POLLOS BROTHA", users)
users.append(UserUtils.User("root", "root", False))
users.append(UserUtils.User("Mr.White", "myPass", False))
users.append(UserUtils.User("Jessy", "IHaveANiceAss", False))
users.append(UserUtils.User("Skyler", "i) [•¡¤¦§¨©ª«¬-®¯±²³¶¹º»¼½¾¿‡•…‪‰‹›⁠⁰€™■･�]", False))

UserUtils.exportUsers(users, "passwd.txt")


passwd = root.password.finalize()
print(passwd)
print(passwd.hex())
"""