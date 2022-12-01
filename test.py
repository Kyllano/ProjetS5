import ClientServerClass
import sys
import UserUtils
#from cryptography.hazmat.primitives import hashes
import string
import annuaire


"""
users = []


users = UserUtils.importUsers("passwd.txt")

UserUtils.removeUser("prout", users)

for i in users :
    if isinstance(i, UserUtils.User) :
        print(i.name, i.passwordHash, i.passwordSalt)

print(UserUtils.checkPasswordUser("root", UserUtils.findUser("root", users)))

"""



"""
UserUtils.changePassword("Gus", "POLLOS BROTHA", users)
users.append(UserUtils.User("root", "root", False))
users.append(UserUtils.User("Mr.White", "myPass", False))
users.append(UserUtils.User("Jessy", "IHaveANiceAss", False))
users.append(UserUtils.User("Skyler", "i) [•¡¤¦§¨©ª«¬-®¯±²³¶¹º»¼½¾¿‡•…‪‰‹›⁠⁰€™■･�]", False))

UserUtils.exportUsers(users, "passwd.txt")
"""

"""
passwd = root.password.finalize()
print(passwd)
print(passwd.hex())
"""


annuaire.creerFichierAnuaire()