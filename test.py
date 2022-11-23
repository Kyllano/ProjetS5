import ClientServerClass
import sys
import UserUtils
from cryptography.hazmat.primitives import hashes

users = []


users = UserUtils.importUsers("passwd.txt")

for i in users :
    if isinstance(i, UserUtils.User) :
        print(i.name, i.passwordHash, i.passwordSalt)







"""
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